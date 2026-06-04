#!/usr/bin/env python3
"""docs/toc.json → manuscript/*.md 골격 생성 (멱등).

이미 존재하는 파일은 건드리지 않는다(작성 중 원고 보호).
toc.json에서 장을 추가/이동/삭제한 뒤 다시 실행하면 누락분만 생성.

사용:
    python3 scripts/scaffold.py            # 누락 골격 생성
    python3 scripts/scaffold.py --dry-run  # 무엇이 생성될지만 출력
"""
from __future__ import annotations
import os
import sys

from _harness import MANUSCRIPT_DIR, chapter_path, iter_toc_chapters, load_toc

TEMPLATE = """---
part: {part}
chapter: {chapter}
slug: {slug}
title: "{title}"
status: skeleton
wikidocs_page_id: null
parent_page_id: null
official_links:
{links_yaml}
last_verified: null
crosscheck: null
crosscheck_date: null
humanized: null
humanized_date: null
---

## 이 장에서 배우는 것

<!-- 한 줄로: 이 장을 끝내면 독자가 무엇을 할 수 있나 -->

## 핵심 개념

<!-- factor/패턴 한 줄 정의 + 비유 + 원문 인용 -->

## 왜 중요한가

<!-- 이 원칙을 어기면 무엇이 무너지는가 (데모→프로덕션 격차) -->

## 하네스에 적용하기

<!-- 실제 코드/의사코드/디렉토리 구조. 가능하면 이 레포 파일로 예시 -->

## 안티패턴과 함정

<!-- 흔한 잘못된 적용과 그 증상 -->

## 핵심 정리 / 체크리스트

- [ ]

## 공식 출처

{links_md}
"""


def links_block(links):
    if not links:
        return "  []", "<!-- toc.json의 official_links만 사용 -->"
    yaml = "\n".join(f"  - {u}" for u in links)
    md = "\n".join(f"- {u}" for u in links)
    return yaml, md


def main():
    dry = "--dry-run" in sys.argv
    os.makedirs(MANUSCRIPT_DIR, exist_ok=True)
    toc = load_toc()
    created, skipped = 0, 0
    for part, ch in iter_toc_chapters(toc):
        path = chapter_path(ch["slug"])
        if os.path.exists(path):
            skipped += 1
            continue
        part_label = "부록" if part.get("is_appendix") else part["part"]
        links_yaml, links_md = links_block(ch.get("official_links", []))
        content = TEMPLATE.format(
            part=part_label,
            chapter=ch["chapter"],
            slug=ch["slug"],
            title=ch["title"].replace('"', "'"),
            links_yaml=links_yaml,
            links_md=links_md,
        )
        if dry:
            print(f"[would create] {os.path.relpath(path)}")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[created] {os.path.relpath(path)}")
        created += 1
    print(f"\n생성 {created} · 기존유지 {skipped}" + (" (dry-run)" if dry else ""))


if __name__ == "__main__":
    main()
