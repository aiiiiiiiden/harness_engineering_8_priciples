# 집필 규약 (Conventions)

> 새 장을 쓰기 전 이 문서를 따른다. 규약 위반은 `scripts/verify.py`가 가능한 범위에서 자동 검출한다.

---

## 1. 대상 독자와 톤

- **독자**: LLM 에이전트·AI 앱을 만드는 **개발자**(주니어~미드 레벨). 파이썬/JS를 읽을 수 있고, LLM API를 한 번쯤 호출해 봤다.
- **약속**: "데모는 되는데 프로덕션에서 무너지는 에이전트"를, **12가지 원칙으로 신뢰할 수 있는 하네스**로 바꾼다.
- **톤**: 명확한 존댓말. 개념은 **한 줄 정의 + 구체 예시(코드/의사코드)** 로. 추상적 훈계 금지.
- **금지**: 출처 없는 단정, "그냥 이렇게 하면 됩니다"식 생략, 검증 안 된 주장. 모든 factor 설명은 정본(`docs/verified-facts.md`)과 일치.
- **자기참조 활용**: 이 레포 자체가 하나의 하네스다. 가능하면 추상 개념을 **이 레포의 실제 파일**(`toc.json`, `verify.py`, `crosscheck.py` 등)로 예시한다. 단 이는 4부에서 본격적으로, 본문 전반에서는 보조적으로만.

## 2. 파일·디렉토리 규약

- 장 원고 = `manuscript/<slug>.md` **1장 1파일**. slug는 `docs/toc.json`이 정한다.
- 다이어그램 소스 = `assets/diagrams/<slug>/NN-이름.svg`, 렌더 결과 = `assets/screenshots/<slug>/NN-이름.png`.
- 원고 구조의 단일 원천은 `docs/toc.json`. 장 추가/삭제/이동은 **toc.json을 먼저** 고치고 `scripts/scaffold.py` 재실행.

## 3. 장별 표준 템플릿 (필수 섹션)

모든 장은 아래 H2 섹션을 **이 순서대로** 포함한다. `scripts/verify.py`가 존재를 검사한다.

```markdown
## 이 장에서 배우는 것
## 핵심 개념
## 왜 중요한가
## 하네스에 적용하기
## 안티패턴과 함정
## 핵심 정리 / 체크리스트
```

- **핵심 개념**: 해당 factor/패턴을 한 줄 정의 + 비유 + 정본 인용으로 푼다.
- **왜 중요한가**: 이 원칙을 어겼을 때 **무엇이 무너지는가**(데모→프로덕션 격차)를 구체적으로.
- **하네스에 적용하기**: 실제 코드/의사코드/디렉토리 구조. 가능하면 이 레포의 파일로 예시.
- **안티패턴과 함정**: 흔한 잘못된 적용과 그 증상.
- **공식 출처**: 각 장 `docs/toc.json`의 `official_links`만 사용. 새 링크는 toc.json에 먼저 등록.

## 4. Front-matter 규격 (필수)

각 `manuscript/*.md`는 YAML front-matter로 시작한다. `scripts/verify.py`가 스키마를 검사한다.

```yaml
---
part: 2                       # 정수 또는 "부록"
chapter: 5                    # 정수 또는 "A"~"C"
slug: ch05-factor02-own-your-prompts
title: "Factor 2 — 프롬프트를 직접 소유하라"
status: skeleton              # skeleton | draft | reviewed | published
wikidocs_page_id: null        # push 후 채움
parent_page_id: null          # 소속 '부' 페이지 id
official_links:               # toc.json과 일치해야 함
  - https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md
last_verified: null           # 사실 검증 완료일 (YYYY-MM-DD)
crosscheck: null              # null | pass | fail  ← crosscheck.py가 자동 기록
crosscheck_date: null         # codex 교차검증 실행일 (YYYY-MM-DD)
---
```

> `crosscheck`/`crosscheck_date`는 **손으로 적지 않는다**. `python3 scripts/crosscheck.py <slug>`가 결과를 자동으로 도장 찍는다. `verify.py`는 `status: reviewed|published`인데 `crosscheck != pass`이면 FAIL시켜 발행을 막는다.

### status 생애주기

`skeleton` → `draft`(본문 작성) → `reviewed`(아래 **3중 검증** 통과) → `published`(wikidocs push 완료, page_id 기록).

**reviewed로 올리는 3중 검증 게이트** (방어선 셋, 서로 독립):
1. `python3 scripts/verify.py` — 기계적(front-matter·템플릿·링크·denylist). 결정론적.
2. `md-doc-reviewer` 스킬 — 같은 모델(Claude)의 심층 검수(설명 오류·코드 오류·오타).
3. `python3 scripts/crosscheck.py <slug>` — **독립 모델(codex)** 의 기술 사실 검증. factor 번호·이름·정의, API·명칭·출처 오류를 모델 다양성으로 잡는다. **통과 시 front-matter `crosscheck: pass`가 자동 기록되고, 이게 없으면 verify.py가 reviewed/published를 막는다(강제 게이트).**

> 사실 레지스트리 자체도 주기적으로 검증한다: `python3 scripts/crosscheck.py --facts` → `docs/verified-facts.md`를 codex가 공식 출처에 비추어 점검.

## 5. 용어 일관성 (terminology)

같은 개념은 같은 단어로. 혼용 금지.

| 표준어 | 쓰지 말 것 |
|---|---|
| 하네스(harness) | 래퍼, 프레임워크(맥락상 구분), 껍데기 |
| 컨텍스트 윈도 | 컨텍스트 창, 윈도우 |
| 도구 호출(tool call) | 함수 호출(LLM 맥락에선 혼란), 툴콜 |
| 구조화 출력 | 정형 출력, structured output(본문 한글 우선) |
| 12가지 원칙 / 12 Factor | 12계명, 12법칙 |
| 무상태(stateless) | 스테이트리스(본문 한글 우선) |
| 진실의 원천(SoT) | 단일 진실 공급원(장황) |

> factor의 한국어 표준 번역은 `docs/verified-facts.md` §2가 마스터. 용어 사전은 부록 B(`appendix-b-glossary`)가 마스터.

## 6. 사실·출처 규약

- factor 번호·이름·정의·순서, 출처·명칭은 **반드시** `docs/verified-facts.md`와 일치.
- 코드 예시(에이전트 루프·도구 스키마 등)의 API 정확성은 **context7 MCP**로 교차 확인 후 `last_verified` 갱신.
- 정본에 없는 주장(예: "13번째 factor")은 **비정본임을 명시**한다.

## 7. 도구 노출 규약

- 이 책은 기술서이므로 Claude Code·MCP·Agent SDK·구조화 출력·codex 등 **하네스 도구를 본문에서 자유롭게 다룬다**(주제 그 자체).
- 단 **gstack·저자 개인 스킬**, 이 레포의 사적 스크립트/커맨드는 본문 비노출. **예외**: 4부 케이스 스터디는 이 하네스를 의도적으로 해부한다.

## 8. 이미지 규약 (다이어그램 · 스크린샷)

### (a) 다이어그램 — 코드가 진실의 원천
- 개념 흐름도(에이전트 루프, 상태 통합, reducer 등)는 **AI 래스터 이미지로 생성하지 않는다**. **SVG를 코드로 작성**한다(재현·diff 가능).
- 소스: `assets/diagrams/<slug>/NN-이름.svg` (커밋 대상).
- 렌더: `python3 scripts/render_images.py` → `assets/screenshots/<slug>/NN-이름.png`(@2x). SVG 수정 시 재렌더.
- 렌더 후 **PNG를 Read로 눈 검수**(한글 글리프·잘림).

### (b) 스크린샷 — 실제 화면
- 터미널/CLI 출력·코드 에디터 화면은 `/browse`·`/qa` 또는 실제 캡처 → `assets/screenshots/<slug>/NN-설명.png`. API 키·토큰 **마스킹**.

### 다이어그램 하우스 스타일 (전 장 일관성)
| 토큰 | 값 |
|---|---|
| 배경 | `#F7F9FC` |
| 본문 잉크 | `#1B2733` / 보조 텍스트 `#5B6B7A` |
| 주조색(소스/강조 블록) | `#2D6CDF` (파랑) |
| 성공/대상 블록 테두리 | `#36B37E` (초록) |
| 경고/안티패턴 | `#E5484D` (빨강) |
| 폰트 | `Apple SD Gothic Neo, sans-serif` (한글 글리프 보장) + 코드 라벨 `ui-monospace, Menlo` |
| 캔버스 | width 1200 기준, 블록 모서리 `rx=20`, 화살표 `stroke-width 6` |
| 톤 | 개발자 친화 — 다이어그램에 코드/의사코드 라벨 허용, 한글 우선(영문 병기) |

> 본문 삽입은 wikidocs push 단계에서 `upload_page_image`로 처리(런북 참조).
