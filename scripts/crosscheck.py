#!/usr/bin/env python3
"""codex(독립 모델) 교차 검증 — 원고의 기술적 사실만 점검 (모델 다양성).

Claude(집필자)와 다른 모델(codex)이 같은 원고를 보게 해, 한 모델이 놓친
factor 번호·이름·정의·순서, API·명칭·출처 오류를 잡는다. 문체/톤은 보지 않는다.

신뢰성 장치:
  - codex exec --output-schema 로 JSON 스키마를 강제 → 구조화된 결과 보장
  - read-only 샌드박스 (원고를 수정하지 못함)
  - 결과를 .harness-cache/crosscheck/<slug>.json 에 보존

사용:
    python3 scripts/crosscheck.py <slug>          # 한 장 교차검증(+front-matter 도장)
    python3 scripts/crosscheck.py --facts         # 사실 레지스트리(docs/verified-facts.md) 자체 검증
    python3 scripts/crosscheck.py <slug> --model gpt-5
환경변수: CODEX_MODEL 로 모델 지정 가능.

종료코드: incorrect(high/critical) 발견 시 1, 그 외 0.
"""
from __future__ import annotations
import datetime
import json
import os
import subprocess
import sys

from _harness import ROOT, chapter_path, parse_front_matter, set_front_matter_key

CACHE_DIR = os.path.join(ROOT, ".harness-cache", "crosscheck")
FACTS_PATH = os.path.join(ROOT, "docs", "verified-facts.md")

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["findings", "summary"],
    "properties": {
        "summary": {"type": "string"},
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["claim", "verdict", "severity", "evidence", "fix"],
                "properties": {
                    "claim": {"type": "string", "description": "원고가 주장하는 기술적 사실"},
                    "verdict": {"type": "string", "enum": ["correct", "incorrect", "uncertain"]},
                    "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
                    "evidence": {"type": "string", "description": "판단 근거(공식문서/원문 등)"},
                    "fix": {"type": "string", "description": "incorrect/uncertain일 때 수정안, 아니면 빈 문자열"},
                },
            },
        },
    },
}

PROMPT_TMPL = """너는 한국어 기술서 **"8원칙으로 살펴보는 하네스 엔지니어링 — 에이전트가 일하는 코드베이스 만들기"**(개발자 대상)의 **독립 기술 검수자**다.
아래 원고의 **기술적 사실만** 검증하라. 문체·톤·맞춤법은 절대 언급하지 마라.

검증 대상:
- 하네스 엔지니어링 **원칙의 번호·이름·정의·순서** (원문: OpenAI "Harness Engineering", openai.com/index/harness-engineering, Ryan Lopopolo, 2026-02-11).
- 출처·명칭·실험 사실 (빈 레포→100만 줄, Codex, "사람이 조종·에이전트가 실행" 등). ⚠️ 원문은 원칙을 번호로 명시하지 않으므로, 원고가 "원문이 정한 N원칙"으로 단정하면 incorrect, "원문에서 도출한 8원칙"으로 표기하면 correct로 본다.
- 코드/의사코드의 정확성(린터·구조적 테스트·관측성·도구 스키마 등), API·CLI·도메인 표기.

기준이 되는 '검증된 사실 레지스트리'(이것과 어긋나면 incorrect):
<verified_facts>
{facts}
</verified_facts>

원고(<{slug}>):
<manuscript>
{body}
</manuscript>

각 기술적 주장에 대해 verdict(correct/incorrect/uncertain), severity, evidence(근거), fix(수정안)를 매겨
스키마에 맞는 JSON으로만 답하라. 확신이 없으면 uncertain으로, 추측으로 correct 처리하지 마라.
"""


def run_codex(prompt: str, schema_path: str, out_path: str, model: str | None) -> tuple[int, str]:
    cmd = ["codex", "exec", "--skip-git-repo-check",
           "-c", 'sandbox_mode="read-only"',
           "--output-schema", schema_path, "-o", out_path]
    if model:
        cmd += ["-m", model]
    cmd.append(prompt)
    # stdin을 닫지 않으면 codex exec가 "Reading additional input from stdin..."에서 멈춘다.
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=600,
                          stdin=subprocess.DEVNULL)
    return proc.returncode, proc.stderr


FACTS_PROMPT = """너는 한국어 기술서 "8원칙으로 살펴보는 하네스 엔지니어링 — 에이전트가 일하는 코드베이스 만들기"의 **독립 기술 검수자**다.
아래는 이 책 전체가 사실의 기준으로 삼는 '검증된 사실 레지스트리'다.
각 사실을 **공식 출처**(openai.com/index/harness-engineering, code.claude.com, modelcontextprotocol.io 등)에 비추어 검증하라.
특히 하네스 엔지니어링 원문(OpenAI, Ryan Lopopolo, 2026-02-11)의 출처·저자·실험 사실, 그리고 8원칙의 이름·순서가 원문 절과 일치하는지 본다.
⚠️ 원문은 원칙을 번호로 명시하지 않는다. 레지스트리가 8개를 "원문이 정한 것"으로 단정하면 incorrect, "이 책이 원문 절에서 도출한 것"으로 명시하면 correct로 본다.
값이 틀렸거나, 옛 정보이거나, 출처상 확인되지 않으면 incorrect/uncertain으로 표시하고 evidence에 근거 URL을, fix에 올바른 값을 적어라.
맞으면 correct. 추측으로 correct 처리하지 마라. claim에는 검증한 항목(key 또는 한 줄 요약)을 넣어라.

<verified_facts>
{facts}
</verified_facts>
스키마에 맞는 JSON으로만 답하라."""


def run_facts(model):
    with open(FACTS_PATH, encoding="utf-8") as f:
        facts = f.read()
    os.makedirs(CACHE_DIR, exist_ok=True)
    schema_path = os.path.join(CACHE_DIR, "_schema.json")
    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(SCHEMA, f)
    out_path = os.path.join(CACHE_DIR, "_verified-facts.json")
    print(f"⟳ codex로 사실 레지스트리 검증 중… (model={model or '기본'})")
    rc, err = run_codex(FACTS_PROMPT.format(facts=facts), schema_path, out_path, model)
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        print(f"❌ codex 출력 없음 (rc={rc})\n{err[-500:]}")
        sys.exit(2)
    with open(out_path, encoding="utf-8") as f:
        data = json.load(f)
    findings = data.get("findings", [])
    print(f"\n🤖 codex 요약: {data.get('summary', '')}\n")
    bad = 0
    for fd in findings:
        icon = {"correct": "✅", "incorrect": "❌", "uncertain": "❓"}.get(fd["verdict"], "•")
        print(f"{icon} [{fd['severity']}] {fd['claim']}")
        if fd["verdict"] != "correct":
            print(f"     근거: {fd['evidence']}")
            if fd.get("fix"):
                print(f"     수정: {fd['fix']}")
            bad += 1
    print("\n" + "─" * 40)
    print(f"findings {len(findings)} · 의심/오류 {bad}  →  결과: {os.path.relpath(out_path)}")
    if bad:
        print("⚠️ 레지스트리에 검토 필요 항목이 있다. docs/verified-facts.md 를 확인/수정하라.")
        sys.exit(1)
    print("PASS ✅ (레지스트리 codex 기준)")


def main():
    model = os.environ.get("CODEX_MODEL")
    if "--model" in sys.argv:
        model = sys.argv[sys.argv.index("--model") + 1]
    if "--facts" in sys.argv:
        run_facts(model)
        return
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("사용법: python3 scripts/crosscheck.py <slug> | --facts [--model NAME]")
    slug = args[0]

    path = chapter_path(slug)
    if not os.path.exists(path):
        sys.exit(f"원고 없음: {path}")
    with open(path, encoding="utf-8") as f:
        _, body = parse_front_matter(f.read())
    with open(FACTS_PATH, encoding="utf-8") as f:
        facts = f.read()

    os.makedirs(CACHE_DIR, exist_ok=True)
    schema_path = os.path.join(CACHE_DIR, "_schema.json")
    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(SCHEMA, f)
    out_path = os.path.join(CACHE_DIR, f"{slug}.json")

    prompt = PROMPT_TMPL.format(facts=facts, slug=slug, body=body)
    print(f"⟳ codex 교차검증 실행 중… (slug={slug}, model={model or '기본'})")
    rc, err = run_codex(prompt, schema_path, out_path, model)
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        print(f"❌ codex 출력 없음 (rc={rc})\n{err[-500:]}")
        sys.exit(2)
    with open(out_path, encoding="utf-8") as f:
        data = json.load(f)

    findings = data.get("findings", [])
    print(f"\n🤖 codex 요약: {data.get('summary', '')}\n")
    blockers = 0
    for fd in findings:
        icon = {"correct": "✅", "incorrect": "❌", "uncertain": "❓"}.get(fd["verdict"], "•")
        print(f"{icon} [{fd['severity']}] {fd['claim']}")
        if fd["verdict"] != "correct":
            print(f"     근거: {fd['evidence']}")
            if fd.get("fix"):
                print(f"     수정: {fd['fix']}")
        if fd["verdict"] == "incorrect" and fd["severity"] in ("critical", "high"):
            blockers += 1
    # 결과를 원고 front-matter에 도장 → verify.py가 reviewed/published에서 강제
    result = "fail" if blockers else "pass"
    today = datetime.date.today().isoformat()
    with open(path, encoding="utf-8") as f:
        src = f.read()
    src = set_front_matter_key(src, "crosscheck", result)
    src = set_front_matter_key(src, "crosscheck_date", today)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)

    print("\n" + "─" * 40)
    print(f"findings {len(findings)} · 차단급 incorrect {blockers}  →  결과: {os.path.relpath(out_path)}")
    print(f"front-matter 기록: crosscheck={result}, crosscheck_date={today}")
    if blockers:
        print("FAIL — 차단급 오류를 수정한 뒤 다시 crosscheck를 돌려야 reviewed로 올릴 수 있다.")
        sys.exit(1)
    print("PASS ✅ (codex 기준)")


if __name__ == "__main__":
    main()
