# 8원칙으로 살펴보는 하네스 엔지니어링

**에이전트가 일하는 코드베이스 만들기** — 코딩 에이전트가 데모를 넘어 프로덕션 규모로 일하도록, 모델의 지능이 아니라 **환경의 견고함**으로 코드베이스를 설계하는 법을 다루는 책 프로젝트입니다.

> **이 저장소는 책 한 권을 집필·출판하는 프로젝트입니다. 산출물은 코드가 아니라 원고입니다.**
> 그리고 메타적으로, **이 저장소 자체가 하네스 엔지니어링 원칙으로 만든 하네스 예시**입니다 — 4부 케이스 스터디에서 스스로를 해부하고 8원칙으로 채점합니다.

📖 **위키독스에서 전문 읽기:** https://wikidocs.net/book/20064
✍️ **소개 글(블로그):** [`blog/harness-engineering-blog.md`](blog/harness-engineering-blog.md)

---

## 하네스 엔지니어링이란?

토대는 OpenAI가 공개한 원문 _[Harness Engineering](https://openai.com/index/harness-engineering/)_(Ryan Lopopolo, 2026)입니다. 빈 git 저장소에서 시작해 약 5개월간 사람이 코드를 한 줄도 직접 작성하지 않고 약 100만 줄짜리 제품을 코딩 에이전트(Codex)만으로 구축한 사내 실험의 기록입니다. 모든 것의 뿌리가 되는 한 줄 명제는 이렇습니다.

> **사람이 조종하고, 에이전트가 실행한다 (Humans steer, agents execute).**

> ℹ️ 원문은 서술형 글이라 원칙을 번호로 열거하지 않습니다. 아래 **8원칙은 이 책이 원문에서 도출한** 커리큘럼이며, 각 원칙은 원문의 특정 절에 1:1로 접지합니다.

## 하네스 엔지니어링 8원칙

| # | 원칙 | 한 줄 요약 | 장 |
|---|---|---|---|
| 1 | 사람이 조종하고, 에이전트가 실행한다 | 사람의 역할을 코드 작성에서 환경 설계·의도 명시·피드백 루프로 재정의한다. | [04장](https://wikidocs.net/363222) |
| 2 | 애플리케이션을 에이전트가 읽게 하라 | 로그·상태·동작을 에이전트가 관측하도록 앱을 계측한다. | [05장](https://wikidocs.net/363223) |
| 3 | 프로젝트 저장소 지식을 기록 시스템으로 삼아라 | 지식을 버전 관리되는 저장소 아티팩트로 둔다 — 백과사전이 아니라 지도 + 구조화된 `docs/`. | [06장](https://wikidocs.net/363224) |
| 4 | 에이전트 가독성에 최적화하라 | 사람 취향보다 에이전트가 읽기 쉬운 구조(작은 진입점·명시적 경계)를 우선한다. | [07장](https://wikidocs.net/363226) |
| 5 | 아키텍처와 취향을 기계적으로 강제하라 | 규칙을 문서가 아니라 린터·구조적 테스트·CI로 강제한다. | [08장](https://wikidocs.net/363227) |
| 6 | 처리량에 맞춰 병합 철학을 바꿔라 | 에이전트 처리량이 사람의 리뷰 범위를 넘으면 병합 규칙을 다시 짠다. | [09장](https://wikidocs.net/363228) |
| 7 | 자율 루프를 시스템으로 구축하라 | 반복 작업을 백그라운드 태스크·루프로 구축해 자율 수준을 점증시킨다. | [10장](https://wikidocs.net/363229) |
| 8 | 엔트로피를 가비지 컬렉션하라 | AI 생성물의 드리프트를 "황금 원칙" + 반복 정리 태스크로 GC한다. | [11장](https://wikidocs.net/363230) |

## 원칙을 조합하는 4가지 패턴 (3부)

| 패턴 | 한 줄 요약 | 장 |
|---|---|---|
| 진실의 원천(SoT) | 사실·구조의 권위 있는 출처를 한 곳에 두고 나머지는 파생시킨다. | [12장](https://wikidocs.net/363231) |
| 검증 게이트와 모델 다양성 | 가장 강한 게이트는 생성에 쓴 모델과 **다른 모델**로 검증하는 게이트다. | [13장](https://wikidocs.net/363232) |
| 결정론적 산출물 | 산출물은 소스에서 재현 가능하게 생성한다 — 같은 입력은 늘 같은 출력. | [14장](https://wikidocs.net/363233) |
| 멀티 에이전트 오케스트레이션 | 큰 작업을 분해해 여러 에이전트로 병렬·파이프라인 처리한다. | [15장](https://wikidocs.net/363234) |

## 목차

- **1부 — 하네스 엔지니어링 입문** ([1](https://wikidocs.net/363218)·[2](https://wikidocs.net/363219)·[3](https://wikidocs.net/363220))
- **2부 — 하네스 엔지니어링 8원칙** (4~11장, 위 표)
- **3부 — 하네스 엔지니어링 패턴** (12~15장, 위 표)
- **4부 — 하네스 엔지니어링 케이스 스터디** ([16. 책 집필 하네스](https://wikidocs.net/363235)·[17. 스코어카드로 하네스 평가하기](https://wikidocs.net/363236))
- **부록** ([A. 치트시트](https://wikidocs.net/363237)·[B. 용어 사전](https://wikidocs.net/363238)·[C. 참고 자료](https://wikidocs.net/363239))

현재 전 24장 발행 완료(`python3 scripts/status.py`로 확인).

---

## 이 저장소 자체가 하나의 하네스다

이 책은 8원칙으로 만든 하네스 안에서 집필되었습니다. 그 골격이 이 저장소에 그대로 들어 있습니다 (4부에서 해부).

![골든 워크플로우: 구조의 진실의 원천인 toc.json에서 scaffold.py가 원고 골격을 결정론적으로 생성하고, 집필된 draft는 4중 검증 게이트(verify.py 기계 검증 · md-doc-reviewer 기술 검수 · crosscheck.py codex 독립 모델 교차검증 · humanize 문체)를 모두 통과해야 reviewed가 되어 위키독스로 발행된다. 하나라도 실패하면 차단된다.](assets/diagrams/chatgpt-renders/ch16-harness-case-study.ko.png)

| 도구 | 역할 | 대응 원칙 |
|---|---|---|
| `docs/toc.json` | 책 구조의 **진실의 원천** | 원칙 3 · 패턴(SoT) |
| `docs/verified-facts.md` | 반복 사실(8원칙·출처·수치)의 SoT + denylist | 원칙 3 |
| `scripts/scaffold.py` | `toc.json`에서 원고 골격을 **결정론적·멱등**으로 생성 | 결정론적 산출물 |
| `scripts/status.py` | front-matter를 스캔해 진척 복원(별도 매니페스트 없음) | 원칙 4 |
| `scripts/verify.py` | 규약·링크·denylist·게이트 도장을 **기계적으로 강제** | 원칙 5 |
| `scripts/crosscheck.py` | 집필 모델과 **다른 모델(codex)** 로 사실 교차검증 | 원칙 1 · 패턴(모델 다양성) |

각 원고의 진행 상태(`status`, `crosscheck`, `humanized`, `wikidocs_page_id`)는 **원고 front-matter 안에** 삽니다. `verify.py`는 `reviewed`/`published`인데 교차검증·윤문 도장이 없으면 빌드를 실패시켜, "검증을 깜빡한 발행"을 코드로 막습니다.

### 빠른 시작 (저자/기여자용)

```bash
python3 scripts/status.py     # 장별 상태 + 진척률
python3 scripts/verify.py     # 원고 규약·사실·링크 검증 (게이트)
```

## 저장소 구조

```
README.md            ← 지금 이 파일
CLAUDE.md / AGENTS.md ← 에이전트 진입점(지도)
BOOK_PLAN.md         ← 설계 원본
docs/
  toc.json           ← 구조 SoT
  verified-facts.md  ← 사실 SoT(8원칙 정의) + denylist
  conventions.md     ← 집필 규약
  publishing-runbook.md
  adr/               ← 결정 기록(ADR)
manuscript/<slug>.md ← 원고 (front-matter + 본문, 1장 1파일)
scripts/             ← scaffold/status/verify/crosscheck/render_images
assets/
  diagrams/<slug>/*.svg          ← 다이어그램 소스(버전관리)
  diagrams/chatgpt-renders/*.png ← 발행용 한국어 래스터(ADR 0004)
  covers/                        ← 표지 + 생성 프롬프트
blog/                ← 소개 글 + 배너 이미지 프롬프트
```

## 출처 / 라이선스

- 원문 1차 출처: OpenAI, _Harness Engineering: leveraging Codex in an agent-first world_ (Ryan Lopopolo, 2026) — https://openai.com/index/harness-engineering/
- 8원칙은 원문에서 **도출**한 이 책의 커리큘럼이며, "원문이 정한 원칙"이 아닙니다. 사실의 단일 원천은 [`docs/verified-facts.md`](docs/verified-facts.md)입니다.
- 본문 전문은 위키독스에서 읽을 수 있습니다: https://wikidocs.net/book/20064
