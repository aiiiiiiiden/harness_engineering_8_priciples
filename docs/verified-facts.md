# 검증된 핵심 사실 레지스트리 (Single Source of Truth)

> 이 책 전체에서 반복 등장하는 **출처·명칭·원칙 정의**의 단일 원천.
> 모든 장은 이 표와 일치해야 한다. 불일치는 버그다 → `scripts/verify.py`가 자동 검출.
> 사실이 바뀌면 **여기를 먼저 고치고**, 그 다음 본문을 고친다.
> 마지막 검증일: 2026-06-03

---

## 1. 출처·명칭 사실 표

| key | 값 | 근거 / 비고 |
|---|---|---|
| `harness_eng_name` | **Harness Engineering** (한국어: 하네스 엔지니어링) | 정본 제목 "Harness engineering: leveraging Codex in an agent-first world" |
| `harness_eng_author` | **OpenAI** (Ryan Lopopolo, Member of Technical Staff) | 개인이 아니라 OpenAI 팀의 사내 실험 보고. 저자 표기는 Ryan Lopopolo |
| `harness_eng_source` | `openai.com/index/harness-engineering/` | 정본(canonical) 출처. 발행일 2026-02-11 |
| `harness_eng_philosophy` | **"사람이 조종하고, 에이전트가 실행한다"** (Humans steer, agents execute) | 정본의 핵심 한 줄. 모든 원칙의 뿌리 |
| `harness_eng_experiment` | 빈 git 리포(2025-08 말 첫 커밋)에서 5개월간 **약 100만 줄**을 **Codex 에이전트만으로**(사람 손코딩 0줄) 구축. 수동 대비 **약 1/10 시간**으로 추정 | 엔지니어 3→7명, 약 1,500 PR, 내부 베타 출시·실사용. "약 1/10 시간"은 정본 추정치 |
| `entropy_friday_cleanup` | 엔트로피 대응 초기엔 **매주 금요일(엔지니어링 시간의 약 20%)** 을 "AI 슬로프" 수동 정리에 썼으나 생성 속도를 못 따라가, **"황금 원칙" + 반복 Codex 정리 태스크**(doc-gardening)로 전환 | 정본 "Entropy and garbage collection" 절. 원칙 8(ch11)·부록 A 근거 |
| `principle_count` | **8개** (이 책이 정본에서 도출) | ⚠️ 정본은 원칙을 번호로 명시하지 않는다. 8개 구분은 **이 책의 편집적 도출**이며 각 원칙은 정본의 특정 절·인용에 1:1 접지한다 |
| `codex_name` | **OpenAI Codex** | 정본 실험의 코딩 에이전트. 사람은 거의 전적으로 프롬프트로만 상호작용 |
| `ralph_wiggum_loop` | 에이전트 검토자가 모두 만족할 때까지 반복하는 피드백 루프 | 정본이 자기 PR 완성 과정을 "사실상 Ralph Wiggum Loop"라 부름 |
| `claude_code_docs_domain` | `code.claude.com/docs` | `docs.claude.com` 에서 변경됨. 구 도메인 표기 금지. (실습 도구 문서) |
| `mcp_spec_site` | `modelcontextprotocol.io` | MCP 공식 명세 (실습 도구) |
| `agent_sdk_name` | **Claude Agent SDK** | 과거 명칭 "Claude Code SDK"에서 변경 (실습 도구) |

## 2. 하네스 엔지니어링 8원칙 (이 책이 정본에서 도출 — 전 장 통일)

> ⚠️ **비정본 카운트 주의.** OpenAI 정본은 서술형 글이며 원칙을 번호로 열거하지 않는다. 정본 본문은 **11개 절**로 구성되는데(아래 "정본 절 전체 순서" 참조), 이 책은 그중 **원칙을 담은 8개 절을 한 원칙씩 선별·도출**했다. 나머지 3개 절 — 실험 도입부("We started with an empty git repository"), 개념 절("What \"agent-generated\" actually means"), 맺음("What we're still learning") — 은 **원칙으로 승격하지 않고** 맥락으로만 활용한다(실험 도입부는 `harness_eng_experiment`에, "agent-generated" 개념 절은 철학·원칙 5·7의 배경으로 흡수). 따라서 "한 절당 한 원칙(1:1 전수 매핑)"이라고 말하면 **틀리다** — 원칙이 안 된 절이 존재한다. 각 원칙은 정본의 해당 절에 직접 접지하며, 본문은 이를 "정본이 명시한 8원칙"으로 단정하지 않고 "정본에서 도출한 8원칙"으로 제시한다.

| # | 영문 (도출 명칭) | 한국어 표준어 | 정본 절(근거, verbatim) |
|---|---|---|---|
| 1 | Humans steer, agents execute | 사람이 조종하고, 에이전트가 실행한다 | Redefining the role of the engineer |
| 2 | Make the application legible to agents | 애플리케이션을 에이전트가 읽게 하라 | Increasing application legibility |
| 3 | Repository knowledge as a system of record | 리포지터리 지식을 기록 시스템으로 | We made repository knowledge the system of record |
| 4 | Optimize for agent legibility | 에이전트 가독성에 최적화하라 | Agent legibility is the goal |
| 5 | Enforce architecture and taste mechanically | 아키텍처와 취향을 기계적으로 강제하라 | Enforcing architecture and taste |
| 6 | Let throughput reshape merge philosophy | 처리량에 맞춰 병합 철학을 바꿔라 | Throughput changes the merge philosophy |
| 7 | Encode the autonomy loop | 자율 루프를 시스템에 인코딩하라 | Increasing levels of autonomy |
| 8 | Garbage-collect entropy | 엔트로피를 가비지 컬렉션하라 | Entropy and garbage collection |

> ⚠️ **원칙 6 → 7 사이 비연속.** 정본에서 "Throughput changes the merge philosophy"(원칙 6) 다음 절은 원칙 7이 아니라 **"What \"agent-generated\" actually means"**(원칙 미승격 개념 절)이고, 그 다음이 "Increasing levels of autonomy"(원칙 7)다. 8원칙은 정본 절 순서를 **따르되 연속 매핑은 아니다**.

#### 정본 절 전체 순서 (11개, verbatim — 매핑 검증 기준)

1. We started with an empty git repository — *(원칙 아님: 실험 도입 → `harness_eng_experiment`)*
2. Redefining the role of the engineer — **원칙 1**
3. Increasing application legibility — **원칙 2**
4. We made repository knowledge the system of record — **원칙 3**
5. Agent legibility is the goal — **원칙 4**
6. Enforcing architecture and taste — **원칙 5**
7. Throughput changes the merge philosophy — **원칙 6**
8. What "agent-generated" actually means — *(원칙 아님: 개념 절)*
9. Increasing levels of autonomy — **원칙 7**
10. Entropy and garbage collection — **원칙 8**
11. What we're still learning — *(원칙 아님: 맺음)*

> 원칙 번호·이름·순서는 위 표가 마스터다. 본문에서 다른 순서/이름을 쓰거나 "1:1 전수 매핑"으로 단정하면 `crosscheck.py`(codex)가 잡는다.

### 핵심 아티팩트 (정본이 명명 — 본문에서 사례로 인용 가능)

`AGENTS.md`(약 100줄, 맵 역할) · `ARCHITECTURE.md` · 구조화된 `docs/`(design-docs·exec-plans(active/completed)·tech-debt-tracker.md·product-specs·references) · 맞춤형 린터 + 구조적 테스트 · doc-gardening 에이전트 · 실행 계획(execution plans, active/completed로 구분) · 계층 모델(Types → Config → Repo → Service → Runtime → UI, 교차관심사는 Providers 인터페이스) · Chrome DevTools Protocol 연동 · LogQL/PromQL 관측성 · "황금 원칙(Golden Principles)" · 수용 기준(acceptance criteria) · 품질 등급(QUALITY_SCORE).

---

## 3. 금지 표현 (denylist) — 비표준·오류

`scripts/verify.py`가 원고에서 아래 패턴을 발견하면 실패시킨다.

| 금지 패턴 | 이유 | 올바른 표현 |
|---|---|---|
| `OpenAI의 8원칙`, `OpenAI가 정의한 8원칙`, `정본의 8원칙`(공식 카운트 단정) | 출처 오류 — 정본은 원칙을 번호로 명시하지 않음 | "정본에서 도출한 8원칙" / "이 책의 8원칙" |
| `한 절당 한 원칙으로 도출`(1:1 전수 매핑 단정) | 출처 오류 — 정본 11개 절 중 8개만 원칙(도입부·"agent-generated" 개념 절·맺음은 미승격) | "8개 절을 한 원칙씩 선별·도출" |
| `12-Factor Agents`, `12 Factor Agents` | 폐기된 구 주제 (피벗으로 제거) | 하네스 엔지니어링(Harness Engineering) |
| `HumanLayer`, `Dexter Horthy` | 폐기된 구 출처 | OpenAI / Ryan Lopopolo |
| `12계명`, `12법칙` | 비표준 명칭 | (해당 없음 — 8원칙) |
| `docs.claude.com/docs` | 구 도메인 | code.claude.com/docs |

> 새 오류 패턴을 발견하면 이 표에 추가하고 `scripts/verify.py`의 `DENYLIST`에도 반영한다.

---

## 4. 도구 노출 경계 (이 책은 기술서이므로 완화된 규칙)

이 책의 **독자는 에이전트/LLM 앱을 만드는 개발자**다. 따라서 본문은 하네스·에이전트 도구를 자유롭게 다룬다.

**본문에 등장 가능 (주제 그 자체)**

- OpenAI Codex, Claude Code (CLI/SDK), Claude Agent SDK
- MCP (Model Context Protocol)
- 구조화 출력(structured outputs)·JSON Schema
- codex 같은 독립 모델 CLI (교차검증 예시)
- 일반적인 에이전트 패턴(서브에이전트, 컨텍스트 관리, 관측성, 린터/CI 등)

**본문 비노출 (저자 전용)**

- gstack 등 저자 개인 스킬·매크로 (독자 환경에 없음)
- 이 레포의 사적인 스크립트/커맨드 — **단, 4부 "케이스 스터디"에서는 의도적으로 해부**한다(예외).
