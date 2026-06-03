#!/usr/bin/env python3
"""원고 규약·사실 검증기 (Invariant Enforcement).

검사 항목:
  E (error, push 차단):
    - front-matter 필수 키 존재 + status 값 유효
    - 파일명 slug == front-matter slug, 그리고 toc.json에 존재
    - front-matter official_links == toc.json official_links
    - 금지 표현(denylist) 미포함  ← docs/verified-facts.md 와 동기화
    - reviewed/published 인데 crosscheck != pass 이면 차단(codex 교차검증 강제)
    - status >= draft 인 장은 표준 템플릿 H2 섹션을 모두 포함
  W (warning):
    - toc.json에 있으나 파일 없는 장
    - 본문에 등장하는 공식문서 도메인 링크가 toc.json에 미등록

사용:
    python3 scripts/verify.py            # errors 있으면 exit 1
    python3 scripts/verify.py --strict   # warnings도 exit 1
"""
from __future__ import annotations
import os
import re
import sys

from _harness import (chapter_path, iter_manuscript_files, iter_toc_chapters,
                      load_toc, parse_front_matter)

REQUIRED_KEYS = ["part", "chapter", "slug", "title", "status",
                 "wikidocs_page_id", "parent_page_id", "official_links", "last_verified",
                 "crosscheck", "crosscheck_date", "humanized", "humanized_date"]
VALID_STATUS = {"skeleton", "draft", "reviewed", "published"}
GATED_STATUS = {"reviewed", "published"}  # codex 교차검증 통과를 강제하는 상태
REQUIRED_SECTIONS = [
    "이 장에서 배우는 것", "핵심 개념", "왜 중요한가",
    "하네스에 적용하기", "안티패턴과 함정", "핵심 정리 / 체크리스트",
]
# docs/verified-facts.md 의 denylist 와 동기화할 것
DENYLIST = [
    (r"OpenAI(이|가)?\s*(만든|발표한|정의한|공식)?\s*(5|8|12)\s*원칙",
     "출처 오류 — 정본은 원칙을 번호로 명시하지 않음. '정본에서 도출한 8원칙'으로"),
    (r"한\s*절당\s*한\s*원칙으로\s*도출",
     "출처 오류 — 정본 11개 절 중 8개만 원칙으로 도출(1:1 전수 매핑 아님). '8개 절을 한 원칙씩 선별·도출'로"),
    (r"12[\s-]*Factor\s*Agents?", "폐기된 구 주제 — '하네스 엔지니어링(Harness Engineering)'으로"),
    (r"HumanLayer", "폐기된 구 출처 — OpenAI / Ryan Lopopolo로"),
    (r"Dexter\s*Horthy", "폐기된 구 출처 — OpenAI / Ryan Lopopolo로"),
    (r"12\s*계명", "비표준 명칭 (해당 없음 — 8원칙)"),
    (r"12\s*법칙", "비표준 명칭 (해당 없음 — 8원칙)"),
    (r"docs\.claude\.com/docs", "구 도메인 — 'code.claude.com/docs'로"),
]
OFFICIAL_DOMAINS = re.compile(
    r"https?://(?:openai\.com|"
    r"code\.claude\.com|docs\.claude\.com|modelcontextprotocol\.io|"
    r"deepwiki\.com|www\.anthropic\.com)\S*")


def main():
    strict = "--strict" in sys.argv
    toc = load_toc()
    by_slug = {ch["slug"]: (part, ch) for part, ch in iter_toc_chapters(toc)}

    errors, warnings = [], []

    # W: toc엔 있으나 파일 없는 장
    for slug, (_, ch) in by_slug.items():
        if not os.path.exists(chapter_path(slug)):
            warnings.append(f"{slug}: toc.json에 있으나 원고 파일 없음 (scaffold.py 실행)")

    for path, text in iter_manuscript_files():
        rel = os.path.relpath(path)
        fm, body = parse_front_matter(text)
        if not fm:
            errors.append(f"{rel}: front-matter 없음")
            continue

        for k in REQUIRED_KEYS:
            if k not in fm:
                errors.append(f"{rel}: front-matter 필수 키 '{k}' 누락")

        status = fm.get("status")
        if status not in VALID_STATUS:
            errors.append(f"{rel}: status '{status}' 유효하지 않음 {sorted(VALID_STATUS)}")

        fname_slug = os.path.basename(path)[:-3]
        if fm.get("slug") != fname_slug:
            errors.append(f"{rel}: 파일명({fname_slug}) ≠ front-matter slug({fm.get('slug')})")

        if fname_slug not in by_slug:
            errors.append(f"{rel}: toc.json에 없는 slug")
        else:
            toc_links = by_slug[fname_slug][1].get("official_links", [])
            fm_links = fm.get("official_links") or []
            if sorted(toc_links) != sorted(fm_links):
                errors.append(f"{rel}: official_links가 toc.json과 불일치\n"
                              f"      toc: {toc_links}\n      fm : {fm_links}")

        # denylist
        for pat, hint in DENYLIST:
            for m in re.finditer(pat, body):
                errors.append(f"{rel}: 금지 표현 '{m.group(0)}' — {hint}")

        # codex 교차검증 강제: reviewed/published는 crosscheck=pass 필수
        if status in GATED_STATUS and fm.get("crosscheck") != "pass":
            errors.append(f"{rel}: status '{status}'인데 crosscheck != pass "
                          f"(현재: {fm.get('crosscheck')}). `python3 scripts/crosscheck.py {fname_slug}` 통과 필요")

        # humanize 문체 검수 강제: reviewed/published는 humanized=pass 필수
        if status in GATED_STATUS and fm.get("humanized") != "pass":
            errors.append(f"{rel}: status '{status}'인데 humanized != pass "
                          f"(현재: {fm.get('humanized')}). `/humanize`로 AI 티 윤문 후 humanized: pass 도장 필요")

        # 템플릿 섹션 (draft 이상)
        if status in {"draft", "reviewed", "published"}:
            heads = set(re.findall(r"^##\s+(.*?)\s*$", body, re.MULTILINE))
            for sec in REQUIRED_SECTIONS:
                if sec not in heads:
                    errors.append(f"{rel}: 필수 섹션 '## {sec}' 누락")

        # W: 미등록 공식 링크
        toc_links = set(by_slug.get(fname_slug, (None, {}))[1].get("official_links", []))
        for m in OFFICIAL_DOMAINS.finditer(body):
            url = m.group(0).rstrip(").,")
            if url not in toc_links:
                warnings.append(f"{rel}: 본문 공식링크 '{url}' 가 toc.json 미등록")

    # 출력
    for w in warnings:
        print(f"⚠️  {w}")
    for e in errors:
        print(f"❌ {e}")
    print("\n" + "─" * 40)
    print(f"errors {len(errors)} · warnings {len(warnings)}")
    if errors or (strict and warnings):
        print("FAIL")
        sys.exit(1)
    print("PASS ✅")


if __name__ == "__main__":
    main()
