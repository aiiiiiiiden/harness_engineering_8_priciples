# 검증된 핵심 사실 레지스트리 (Single Source of Truth)

> 이 책 전체에서 반복 등장하는 **출처·명칭·factor 정의**의 단일 원천.
> 모든 장은 이 표와 일치해야 한다. 불일치는 버그다 → `scripts/verify.py`가 자동 검출.
> 사실이 바뀌면 **여기를 먼저 고치고**, 그 다음 본문을 고친다.
> 마지막 검증일: 2026-06-02

---

## 1. 출처·명칭 사실 표

| key | 값 | 근거 / 비고 |
|---|---|---|
| `twelve_factor_name` | **12-Factor Agents** (한국어: 12가지 원칙) | "12계명"·"12법칙" 등 비표준 명칭 금지 |
| `twelve_factor_author` | **HumanLayer** (Dexter Horthy 주도) | Anthropic/OpenAI가 만든 것이 아님 |
| `twelve_factor_repo` | `github.com/humanlayer/12-factor-agents` | 정본(canonical) 출처 |
| `twelve_factor_count` | **12개** (정본) | 일부 블로그가 13번째(pre-fetch context)를 덧붙이나 정본은 12개. 추가 factor는 "비정본"으로 명시 |
| `twelve_factor_origin` | Heroku의 **12-Factor App**(Adam Wiggins, 2011)에서 영감 | App과 Agents는 **다른 문서** — 혼동 금지 |
| `claude_code_docs_domain` | `code.claude.com/docs` | `docs.claude.com` 에서 변경됨. 구 도메인 표기 금지 |
| `mcp_spec_site` | `modelcontextprotocol.io` | MCP 공식 명세 |
| `agent_sdk_name` | **Claude Agent SDK** | 과거 명칭 "Claude Code SDK"에서 변경 |

## 2. 12 Factor 정본 명칭 (한국어 표준 번역 — 전 장 통일)

| # | 영문 (정본) | 한국어 표준어 |
|---|---|---|
| 1 | Natural Language to Tool Calls | 자연어를 도구 호출로 |
| 2 | Own your prompts | 프롬프트를 직접 소유하라 |
| 3 | Own your context window | 컨텍스트 윈도를 직접 소유하라 |
| 4 | Tools are structured outputs | 도구는 구조화된 출력일 뿐 |
| 5 | Unify execution state and business state | 실행 상태와 비즈니스 상태를 통합하라 |
| 6 | Launch / Pause / Resume with simple APIs | 간단한 API로 시작·중단·재개 |
| 7 | Contact humans with tool calls | 사람과의 소통도 도구 호출로 |
| 8 | Own your control flow | 제어 흐름을 직접 소유하라 |
| 9 | Compact errors into context window | 에러를 컨텍스트에 압축해 넣어라 |
| 10 | Small, focused agents | 작고 집중된 에이전트 |
| 11 | Trigger from anywhere | 어디서든 트리거하라 |
| 12 | Make your agent a stateless reducer | 에이전트를 무상태 리듀서로 |

> factor 번호·이름·순서는 위 표가 마스터다. 본문에서 다른 순서/이름을 쓰면 `crosscheck.py`(codex)가 잡는다.

---

## 3. 금지 표현 (denylist) — 비표준·오류

`scripts/verify.py`가 원고에서 아래 패턴을 발견하면 실패시킨다.

| 금지 패턴 | 이유 | 올바른 표현 |
|---|---|---|
| `12계명`, `12 법칙` | 비표준 명칭 | 12가지 원칙 / 12 Factor |
| `OpenAI가 만든`, `OpenAI가 발표한` (12-Factor 맥락) | 출처 오류 | HumanLayer(Dexter Horthy)가 정리 |
| `Anthropic이 만든 12-Factor` | 출처 오류 | HumanLayer가 정리 |
| `docs.claude.com/docs` | 구 도메인 | code.claude.com/docs |

> 새 오류 패턴을 발견하면 이 표에 추가하고 `scripts/verify.py`의 `DENYLIST`에도 반영한다.

---

## 4. 도구 노출 경계 (이 책은 기술서이므로 완화된 규칙)

이 책의 **독자는 에이전트/LLM 앱을 만드는 개발자**다. 따라서 본문은 하네스·에이전트 도구를 자유롭게 다룬다.

**본문에 등장 가능 (주제 그 자체)**

- Claude Code (CLI/SDK), Claude Agent SDK
- MCP (Model Context Protocol)
- 구조화 출력(structured outputs)·JSON Schema
- codex 같은 독립 모델 CLI (교차검증 예시)
- 일반적인 에이전트 패턴(서브에이전트, 컨텍스트 관리 등)

**본문 비노출 (저자 전용)**

- gstack 등 저자 개인 스킬·매크로 (독자 환경에 없음)
- 이 레포의 사적인 스크립트/커맨드 — **단, 4부 "케이스 스터디"에서는 의도적으로 해부**한다(예외).
