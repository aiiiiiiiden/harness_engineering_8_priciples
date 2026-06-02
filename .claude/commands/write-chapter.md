---
description: 한 장을 규약대로 집필(draft)한다
argument-hint: <slug 또는 장 번호> (예: ch05-factor02-own-your-prompts 또는 5)
---

`$ARGUMENTS` 장을 집필한다. 절차:

1. `docs/conventions.md`(톤·템플릿·용어)와 `docs/verified-facts.md`(factor 정의·출처·명칭)를 먼저 읽는다.
2. `manuscript/<slug>.md`를 연다. front-matter의 `official_links`만 "공식 출처"에 쓴다.
3. **factor 장이면 정본을 근거로 삼는다**: 해당 factor의 원문(github.com/humanlayer/12-factor-agents/blob/main/content/...)을 확인하고, 번호·이름·정의·순서를 `verified-facts.md` §2와 일치시킨다. 코드/API는 **context7 MCP**로 교차 확인 후 `last_verified`를 오늘로 갱신.
4. 표준 6개 섹션을 개발자 톤으로 채운다(한 줄 정의 + 코드/의사코드, 추상 훈계 금지). "왜 중요한가"는 이 원칙을 어겼을 때 무너지는 지점을 구체적으로.
5. 본문 도구 노출: Claude Code·MCP·Agent SDK·codex 등 하네스 도구는 OK. **gstack·개인 스킬·이 레포의 사적 스크립트는 비노출**(단 4부 케이스 스터디는 예외).
6. 개념 비유가 필요하면 `/make-diagram <slug> "<설명>"`으로 다이어그램(SVG)을 만든다. CLI/터미널 화면은 `/browse`·`/qa`로 캡처해 `assets/screenshots/<slug>/`에 저장.
7. 완료하면 front-matter `status: draft`로 바꾸고 `python3 scripts/verify.py`를 돌려 통과시킨다.
8. (선택) 초안이 'AI 티'가 나면 `/humanize`로 윤문한다 — **내용은 한 글자도 바꾸지 않는다**.

**reviewed로 올리기 전 3중 검증**: `verify.py` + `md-doc-reviewer` + `/cross-check <slug>`(codex 독립 검증)를 모두 통과시킨다. factor 정의·코드가 있는 장은 cross-check 필수.
