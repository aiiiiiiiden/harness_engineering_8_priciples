# 집필 규약 (Conventions)

> 새 장을 쓰기 전 이 문서를 따른다. 규약 위반은 `scripts/verify.py`가 가능한 범위에서 자동 검출한다.

---

## 1. 대상 독자와 톤

- **독자**: 에이전트가 일하는 코드베이스를 만드는 **개발자**(주니어~미드 레벨). 파이썬/JS를 읽을 수 있고, 코딩 에이전트(Codex·Claude Code 등)를 한 번쯤 써 봤다.
- **약속**: "에이전트한테 시켰더니 엉망이 되는 코드베이스"를, **하네스 엔지니어링 8원칙으로 에이전트가 안정적으로 일하는 환경**으로 바꾼다.
- **톤**: 명확한 존댓말. 개념은 **한 줄 정의 + 구체 예시(코드/의사코드)** 로. 추상적 훈계 금지.
- **금지**: 출처 없는 단정, "그냥 이렇게 하면 됩니다"식 생략, 검증 안 된 주장. 모든 원칙 설명은 정본(`docs/verified-facts.md`)과 일치.
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
slug: ch05-principle2-make-app-legible
title: "원칙 2 — 애플리케이션을 에이전트가 읽게 하라"
status: skeleton              # skeleton | draft | reviewed | published
wikidocs_page_id: null        # push 후 채움
parent_page_id: null          # 소속 '부' 페이지 id
official_links:               # toc.json과 일치해야 함
  - https://openai.com/index/harness-engineering/
last_verified: null           # 사실 검증 완료일 (YYYY-MM-DD)
crosscheck: null              # null | pass | fail  ← crosscheck.py가 자동 기록
crosscheck_date: null         # codex 교차검증 실행일 (YYYY-MM-DD)
humanized: null               # null | pass        ← /humanize 윤문 통과 후 도장
humanized_date: null          # 문체 윤문 완료일 (YYYY-MM-DD)
---
```

> `crosscheck`/`crosscheck_date`는 **손으로 적지 않는다**. `python3 scripts/crosscheck.py <slug>`가 결과를 자동으로 도장 찍는다. `humanized`/`humanized_date`는 `/humanize` 파이프라인이 문체 윤문을 끝내고 naturalness-reviewer가 통과시킨 뒤 `pass`로 적는다. `verify.py`는 `status: reviewed|published`인데 `crosscheck != pass` **또는** `humanized != pass`이면 FAIL시켜 발행을 막는다.

### status 생애주기

`skeleton` → `draft`(본문 작성) → `reviewed`(아래 **4중 검증** 통과) → `published`(wikidocs push 완료, page_id 기록).

**reviewed로 올리는 4중 검증 게이트** (방어선 넷, 서로 독립 — 앞 셋은 사실·기술, 넷째는 문체):
1. `python3 scripts/verify.py` — 기계적(front-matter·템플릿·링크·denylist·게이트 강제). 결정론적.
2. `md-doc-reviewer` 스킬 — 같은 모델(Claude)의 심층 검수(설명 오류·코드 오류·오타).
3. `python3 scripts/crosscheck.py <slug>` — **독립 모델(codex)** 의 기술 사실 검증. factor 번호·이름·정의, API·명칭·출처 오류를 모델 다양성으로 잡는다. **통과 시 front-matter `crosscheck: pass`가 자동 기록되고, 이게 없으면 verify.py가 reviewed/published를 막는다(강제 게이트).**
4. `/humanize` (humanize-korean 파이프라인) — **문체** 검수. 번역투·기계적 병렬·불릿/이모지 과다 등 AI 티를 제거한다. **내용·사실은 한 글자도 바꾸지 않는다**(content-fidelity-auditor가 불변을 검증). 통과 시 `humanized: pass`를 도장 찍고, 이게 없으면 verify.py가 reviewed/published를 막는다(강제 게이트). 윤문 후 **사실 불변 확인을 위해 verify.py를 다시 돌린다**.

> 게이트 1~3은 "맞는 내용인가"(사실·기술), 게이트 4는 "사람이 쓴 글처럼 읽히는가"(문체)를 본다. 한글 기술서의 신뢰도는 둘 다 필요하다.

> 사실 레지스트리 자체도 주기적으로 검증한다: `python3 scripts/crosscheck.py --facts` → `docs/verified-facts.md`를 codex가 공식 출처에 비추어 점검.

## 5. 용어 일관성 (terminology)

같은 개념은 같은 단어로. 혼용 금지.

| 표준어 | 쓰지 말 것 |
|---|---|
| 하네스(harness) | 래퍼, 프레임워크(맥락상 구분), 껍데기 |
| 코딩 에이전트 | AI, 봇(맥락상 구분) |
| 컨텍스트 윈도 | 컨텍스트 창, 윈도우 |
| 가독성(legibility) | 판독성, 읽힘성(혼용 금지) |
| 기계적 강제(mechanical enforcement) | 자동 검사(좁음), 강제화 |
| 기록 시스템(system of record) | 기록 체계, SoR(본문 한글 우선) |
| 불변식(invariant) | 불변 조건(혼용 가능하나 '불변식' 우선) |
| 진실의 원천(SoT) | 단일 진실 공급원(장황) |

> 8원칙의 한국어 표준 번역은 `docs/verified-facts.md` §2가 마스터. 용어 사전은 부록 B(`appendix-b-glossary`)가 마스터.

## 6. 사실·출처 규약

- 원칙 번호·이름·정의·순서, 출처·명칭은 **반드시** `docs/verified-facts.md`와 일치.
- 코드 예시(린터·구조적 테스트·관측성·도구 스키마 등)의 API 정확성은 **context7 MCP**로 교차 확인 후 `last_verified` 갱신.
- **8원칙은 이 책이 정본에서 도출한 커리큘럼**이다. 정본(OpenAI)은 원칙을 번호로 명시하지 않으므로, 본문은 "정본이 정한 8원칙"이 아니라 **"정본에서 도출한 8원칙"** 으로 제시하고 각 원칙을 정본 절에 접지한다.

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

### 다이어그램 하우스 스타일 (전 장 일관성 — 표지와 한 가족)

> **시각 언어의 기준은 책 표지**(`assets/covers/`)다. 표지에서 도출한 "조화—의미색 유지" 시스템을 전 다이어그램이 따른다: **잉크+파랑 단색조를 기본**으로 절제·여백·얇은 선을 쓰되, **통과/차단 같은 의미는 초록·빨강 액센트로만** 남긴다(기본 색이 아니라 의미가 있을 때만).

| 토큰 | 값 |
|---|---|
| 배경 | `#F7F9FC` (넉넉한 여백 · 에어리) |
| 본문 잉크 | `#1B2733` / 보조 텍스트 `#5B6B7A` |
| **주조색(기본 블록·흐름·강조)** | `#2D6CDF` (파랑) — 박스 기본 테두리·주 화살표는 파랑 또는 잉크 |
| **의미 액센트(절제)** | 통과/성공 `#36B37E`(초록), 차단/실패 `#E5484D`(빨강). **의미가 있을 때만**, 기본 색으로 남발 금지 |
| 선 굵기 | **얇고 섬세하게.** 블록 테두리 `stroke-width 2`(강조만 2.5), 화살표 `2.5~3.5`(표지처럼 델리킷). 과거 3~6은 지양 |
| 블록 | 흰 배경 `#FFFFFF`, 모서리 `rx=14~16`, 얇은 테두리 |
| 모티프(표지 차용) | ① 입자(dot) 필드(흩어짐→수렴, "빈 레포→구조"류에) ② **대문자 영문 마이크로 라벨 + 점선 커넥터**(예: `FROM AN EMPTY REPO ┄▶ TO A MILLION LINES`) ③ 얇은 아웃라인 계층 스택 |
| 폰트 | `Apple SD Gothic Neo, sans-serif` (한글) + 코드/영문 라벨 `ui-monospace, Menlo` |
| 캔버스 | width 1200 기준, 제목(상단 중앙 27/700)·부제(16, 보조색)·하단 핵심 1줄 |
| 톤 | 모던·데이터비주얼·절제. 한글 우선(영문 병기), 코드/의사코드 라벨 허용 |

> 기존 다이어그램(ch06·08·10·12~17)은 이 시스템으로 **단계적 재작성** 중이다(표지 확정 후). 새 다이어그램은 처음부터 이 표를 따른다.
> 본문 삽입은 wikidocs push 단계에서 `upload_page_image`로 처리(런북 참조).
