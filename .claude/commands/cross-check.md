---
description: codex(독립 모델)로 한 장의 기술 사실을 교차 검증한다
argument-hint: <slug> (예: ch08-factor05-unify-state)
---

`$ARGUMENTS` 장을 **다른 모델(codex)** 로 교차 검증한다. 집필은 Claude가 했으니, 독립 모델이 기술 사실을 한 번 더 본다(모델 다양성 = 신뢰성). 특히 **factor 번호·이름·정의·순서**와 출처·명칭이 정본과 맞는지 본다.

```bash
python3 scripts/crosscheck.py $ARGUMENTS
```

- read-only 샌드박스 + `--output-schema`로 구조화 JSON을 강제하므로 결과가 안정적이다.
- 결과는 `.harness-cache/crosscheck/<slug>.json`에 저장된다.
- `verdict=incorrect`(특히 severity high/critical)는 **반드시** 원고를 고친다. `uncertain`은 context7 MCP·정본 문서로 직접 확인.
- codex와 Claude 판단이 엇갈리면 정본(github.com/humanlayer/12-factor-agents)을 근거로 사용자에게 보고하고 결정한다(어느 한쪽을 맹신하지 않는다).
- 차단급 오류가 없고 verify.py·md-doc-reviewer도 통과하면 front-matter `status: reviewed`로 올린다.

모델을 바꾸려면: `python3 scripts/crosscheck.py $ARGUMENTS --model <name>`
사실 레지스트리 자체 점검: `python3 scripts/crosscheck.py --facts`
