# 12-Factor Agents로 배우는 하네스 엔지니어링 — 책 집필 계획서

> 에이전트/LLM 앱 개발자 대상. HumanLayer의 **12-Factor Agents**를 한 장씩 풀어
> "데모는 되는데 프로덕션에서 무너지는 에이전트"를 **신뢰할 수 있는 하네스**로 바꾸는 법을 가르친다.
> 플랫폼: 위키독스(WikiDocs). 작성일 기준: 2026-06.

---

## 0. 콘셉트와 차별점

- **대상 독자**: LLM API를 한 번쯤 호출해 본 개발자(주니어~미드). "프레임워크가 다 해주겠지" 했다가 프로덕션에서 막힌 사람.
- **약속**: 프레임워크의 마법에 기대지 말고 **제어 흐름·컨텍스트·프롬프트·상태를 직접 소유**해 신뢰성을 확보한다.
- **핵심 텍스트**: HumanLayer(Dexter Horthy)의 [12-Factor Agents](https://github.com/humanlayer/12-factor-agents). Heroku의 12-Factor App에서 영감받은 LLM 에이전트 버전.
- **차별점**:
  1. 12개 factor를 **한 장에 하나씩** 한국어로 정밀 해설(정본 인용 + 코드).
  2. factor를 합쳐 실제 **하네스 패턴**으로 조립(3부).
  3. **메타 구성** — 이 책을 집필한 하네스(이 레포)를 4부에서 직접 해부하고, 12 Factors로 스스로를 채점한다.
- **러닝 스레드**: 책 전체에서 하나의 가상 에이전트("배포 봇")를 12 factor에 맞춰 점진적으로 강건하게 만든다.

---

## 1. 전체 목차 (위키독스 계층: 부 > 장 > 절)

> 구조의 단일 원천은 `docs/toc.json`. 아래는 사람이 읽는 사본이다. 변경은 toc.json에 먼저.

### 1부. 하네스 엔지니어링 입문
1. 하네스 엔지니어링이란 무엇인가
2. 왜 12-Factor인가 — App에서 Agent로
3. 하네스의 해부학 — 이 책의 실습 환경 미리보기

### 2부. 12 Factors — 한 장에 하나씩
4. Factor 1 — 자연어를 도구 호출로
5. Factor 2 — 프롬프트를 직접 소유하라
6. Factor 3 — 컨텍스트 윈도를 직접 소유하라
7. Factor 4 — 도구는 구조화된 출력일 뿐
8. Factor 5 — 실행 상태와 비즈니스 상태를 통합하라
9. Factor 6 — 간단한 API로 시작·중단·재개
10. Factor 7 — 사람과의 소통도 도구 호출로
11. Factor 8 — 제어 흐름을 직접 소유하라
12. Factor 9 — 에러를 컨텍스트에 압축해 넣어라
13. Factor 10 — 작고 집중된 에이전트
14. Factor 11 — 어디서든 트리거하라
15. Factor 12 — 에이전트를 무상태 리듀서로

### 3부. 하네스 패턴 — Factor를 합치다
16. 진실의 원천(SoT) 설계하기 (Factor 5·12)
17. 검증 게이트와 모델 다양성으로 신뢰성 확보 (Factor 4·7)
18. 결정론적 산출물 — 코드가 진실의 원천 (Factor 8)
19. 멀티 에이전트 오케스트레이션 (Factor 10)

### 4부. 케이스 스터디 — 이 책을 만든 하네스
20. 책 집필 하네스 해부 (toc·scaffold·verify·crosscheck)
21. 12 Factors로 내 하네스 평가하기 (스코어카드)

### 부록
- A. 12 Factors 치트시트 (한 장 요약)
- B. 용어 사전 (하네스·에이전트·컨텍스트 등)
- C. 참고 자료 / 원문 링크 모음

---

## 2. 검증된 핵심 사실 (집필 시 반영)

> 단일 원천은 `docs/verified-facts.md`. 요약:

| 항목 | 확인된 사실 |
|---|---|
| 명칭 | **12-Factor Agents** (한국어 "12가지 원칙"). "12계명/12법칙" 금지 |
| 저자/출처 | **HumanLayer**(Dexter Horthy 주도), `github.com/humanlayer/12-factor-agents` |
| factor 개수 | **12개**(정본). 13번째(pre-fetch context)는 비정본 → 표기 시 명시 |
| 기원 | Heroku **12-Factor App**(Adam Wiggins, 2011)에서 영감. App ≠ Agents |
| Claude Code 문서 | `code.claude.com/docs` (구 `docs.claude.com` 금지) |
| MCP | `modelcontextprotocol.io` 공식 명세 |

---

## 2-1. 도구(MCP / Skill / Agent) 매핑

> 이 책은 **기술서**라 하네스 도구가 곧 주제다. 그래도 두 종류를 구분한다.

### (A) 본문에 등장 가능 — 주제 그 자체
Claude Code(CLI/SDK), Claude Agent SDK, MCP, 구조화 출력/JSON Schema, codex 같은 독립 모델 CLI, 일반 에이전트 패턴.

### (B) 저자 전용 — 본문 비노출 (4부 케이스 스터디는 예외)
| 집필 단계 | 도구 | 용도 |
|---|---|---|
| 사실 검증 | **context7 MCP** | Agent SDK·MCP·라이브러리 최신 문서 교차확인 |
| 교차검증 | **codex CLI**(`crosscheck.py`) | 독립 모델로 factor·코드 사실 검증 |
| 다이어그램 | SVG + `render_images.py` | 결정론적 개념도 |
| 스크린샷/QA | `/browse`, `/qa` | 터미널/CLI 화면 캡처 |
| 윤문 | `humanize-korean` | AI 티 제거(내용 불변) |
| 출판 | **wikidocs MCP** | 책/페이지 생성·수정·이미지 |
| 검수 | `md-doc-reviewer` | 코드·기술 오류·오타 |

---

## 3. 위키독스 제작 워크플로우 (MCP 자동화)

- 계층은 `parent_id` 트리로 구현. **명시적 순서 파라미터 없음 → 생성 순서 = 표시 순서**.
- 순서: `create_book` → 부/장을 toc 순서대로 `create_page` → 하위 절은 상위 page_id를 parent_id로 → `get_book_toc`로 검증.
- 권장: 초안은 비공개(`open_yn=N`), 완성 후 공개. 자세한 절차는 `docs/publishing-runbook.md`.

---

## 4. 집필 진행 계획

1. **단계 1 — 골격 생성**: `scaffold.py`로 5개 부 + 24개 장(부록 포함) 골격 생성. → 뼈대 확정.
2. **단계 2 — 파일럿 집필**: 1부(3장)를 본문까지 완성해 톤·분량·다이어그램 규칙 확정.
3. **단계 3 — Factor 집필**: 2부 12장을 정본 한 편씩 매핑해 작성(각 장 cross-check 필수 — factor 정의가 핵심).
4. **단계 4 — 패턴·케이스 스터디**: 3·4부에서 factor를 합치고 이 하네스를 해부·채점.
5. **단계 5 — 검수·공개**: 3중 검증 통과 후 공개 전환.

### 장별 표준 템플릿
```
## 이 장에서 배우는 것
## 핵심 개념
## 왜 중요한가
## 하네스에 적용하기
## 안티패턴과 함정
## 핵심 정리 / 체크리스트
```
