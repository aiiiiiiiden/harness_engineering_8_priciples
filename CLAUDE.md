# CLAUDE.md — 에이전트 진입점

> **이 레포는 책 한 권을 집필·출판하는 프로젝트다.** 코드가 아니라 원고가 산출물이다.
> 책: **"하네스 엔지니어링 — 에이전트가 일하는 코드베이스 만들기"** (에이전트/LLM 앱 개발자 대상) → 위키독스(WikiDocs)에 발행.
> OpenAI의 *Harness Engineering* 정본(Ryan Lopopolo, 2026)을 **8원칙으로 도출**해 한 장씩 풀고, 빈 레포에서 시작한 샘플 프로젝트를 원칙마다 키운다.
> 메타: **이 레포 자체가 하네스 엔지니어링 원칙으로 만든 하네스 예시**다. 4부 케이스 스터디에서 스스로를 해부·채점한다.
> 새 세션은 이 파일부터 읽고, 막히면 아래 "지도"의 해당 문서로 점프한다.

## 지금 어디까지 했나 (제일 먼저)

```bash
python3 scripts/status.py     # 장별 상태(skeleton/draft/reviewed/published) + 진척률
python3 scripts/verify.py     # 원고 규약·사실·링크 검증
```

진행 상태는 **각 원고의 front-matter에만** 저장된다(머릿속·외부 금지). 세션이 끊겨도 위 두 명령으로 즉시 복원된다. ← 이게 원칙 3·4(리포지터리가 기록 시스템·진실의 원천)의 실물이다.

## 지도 (필요할 때 점프)

| 알고 싶은 것 | 문서 |
|---|---|
| 무엇을·왜 만드나, 전체 콘셉트 | `BOOK_PLAN.md` (설계 원본) |
| 책 구조(부/장/링크)의 단일 원천 | `docs/toc.json` ← 구조 변경은 **여기 먼저** |
| 톤·용어·장 템플릿·front-matter 규격 | `docs/conventions.md` |
| 8원칙 정의·출처·명칭 등 반복 사실 | `docs/verified-facts.md` (SoT) |
| 위키독스에 올리는 절차 | `docs/publishing-runbook.md` |
| 핵심 결정의 이유 | `docs/adr/` |
| 실제 원고 | `manuscript/<slug>.md` (1장 1파일) |
| 다이어그램·스크린샷 | `assets/diagrams/<slug>/`, `assets/screenshots/<slug>/` |

## 골든 워크플로우

```
toc.json (구조)
   └─ scaffold.py ─▶ manuscript/*.md 골격(skeleton)
        └─ /write-chapter ─▶ 본문 작성 + context7 사실확인 + (필요시) /make-diagram ─▶ status: draft
             └─ 4중 검증 게이트 ─▶ status: reviewed
             │     1) verify.py (기계적)   2) md-doc-reviewer (Claude)
             │     3) crosscheck.py (codex·독립 모델)   4) /humanize (문체·AI 티 제거)
             └─ /publish-chapter ─▶ wikidocs MCP push(본문+이미지) ─▶ status: published
```

**신뢰성의 핵심 = 모델 다양성.** 집필은 Claude, 사실 검증은 **codex(다른 모델)** 가 독립적으로 한 번 더. 두 모델 + 기계 검증이 합의해야 reviewed. 이미지는 **AI 생성이 아니라 SVG 코드 → 결정론적 렌더**라 재현 가능. (이 책이 가르치는 원칙을 이 하네스가 그대로 실천한다.)

## 프로젝트 커맨드

| 커맨드 | 용도 |
|---|---|
| `/book-status` | 진행 상태 + 검증 결과 보고 |
| `/write-chapter <slug>` | 한 장을 규약대로 집필(draft) |
| `/cross-check <slug>` | codex(독립 모델)로 기술 사실 교차 검증 |
| `/make-diagram <slug>` | 개념 다이어그램을 SVG로 작성→렌더 |
| `/publish-chapter <slug>` | reviewed 장을 위키독스에 올림 |

윤문(저자 전용): 초안이 'AI 티'가 날 때 `/humanize`(한글 자연스러움 파이프라인). 본문 사실은 건드리지 않는다.

검증·이미지 스크립트:
```bash
python3 scripts/crosscheck.py <slug>    # codex 교차검증 (read-only, JSON 강제)
python3 scripts/render_images.py        # assets/diagrams/**/*.svg → screenshots/**/*.png(@2x)
```

## 절대 규칙 (위반은 버그)

1. **사실 일치**: 원칙 번호·이름·정의·순서, 출처·명칭은 `docs/verified-facts.md`와 반드시 일치. 8원칙은 정본에서 **도출**한 것이므로 "정본이 정한 8원칙"으로 단정 금지("도출한 8원칙"). 어기면 `verify.py`가 FAIL.
2. **구조 단일 원천**: 장 추가/이동/삭제는 `docs/toc.json`을 먼저 고치고 `python3 scripts/scaffold.py` 실행. 원고 파일을 임의로 만들지 않는다.
3. **push 전 4중 검증 (강제)**: `verify.py` PASS + `md-doc-reviewer` + `crosscheck.py`(codex) + `/humanize`(문체) PASS, 그리고 `status: reviewed` 가 아니면 위키독스에 올리지 않는다.
   - codex 교차검증과 humanize는 **강제 게이트**다. `crosscheck.py`는 `crosscheck: pass`를, `/humanize`는 `humanized: pass`를 front-matter에 도장 찍고, `verify.py`는 reviewed/published인데 둘 중 하나라도 `!= pass`면 FAIL시킨다.
   - humanize는 **문체만** 손대고 내용·사실은 불변(content-fidelity-auditor가 검증). 윤문 후 verify.py를 다시 돌려 사실 불변을 확인한다.
   - 사실 레지스트리 자체 점검: `python3 scripts/crosscheck.py --facts`.
4. **이미지는 코드로**: 개념 다이어그램은 AI 래스터 생성 금지. SVG(`assets/diagrams/<slug>/`)로 작성→`render_images.py`로 렌더→**PNG를 Read로 눈 검수**. 스크린샷만 `/browse`·`/qa` 캡처.
5. **page_id 기록**: 위키독스에 올린 뒤 page_id를 front-matter에 적는다. 같은 장 재발행은 `update_page`(중복 생성 금지).
6. **도구 노출 경계**: 이 책은 기술서라 Claude Code·MCP·Agent SDK·codex 등 하네스 도구를 본문에서 다룬다. 단 **gstack·개인 스킬**, 이 레포의 사적 스크립트/커맨드는 본문 비노출 — **예외: 4부 케이스 스터디**는 의도적으로 해부.
7. **코드·API 정확성**: 코드 예시는 **context7 MCP**로 교차 확인 후 front-matter `last_verified` 갱신.

## 도구

- **wikidocs MCP** — 책/페이지 생성·수정·이미지 업로드 (런북 참조)
- **context7 MCP** — Claude Agent SDK·MCP·관련 라이브러리 최신 문서 교차 확인
- **codex CLI** — 독립 모델 기술 사실 교차검증 (`scripts/crosscheck.py`, read-only)
- **rsvg-convert** — SVG 다이어그램 → PNG 렌더 (`scripts/render_images.py`)
- **`/browse`, `/qa`** — 터미널/CLI 화면 스크린샷
- **md-doc-reviewer** — 원고 기술 정확성·코드·오타 검수 (reviewed 전 단계)
- **humanize-korean** — AI 티 제거 윤문(저자 전용, 내용 불변)

## 디렉토리

```
CLAUDE.md            ← 지금 이 파일 (진입점)
BOOK_PLAN.md         ← 설계 원본
docs/
  toc.json           ← 구조 SoT
  conventions.md     ← 집필 규약
  verified-facts.md  ← 사실 SoT(8원칙 정의) + denylist
  publishing-runbook.md
  adr/               ← 결정 기록 (0001 하네스·SoT, 0002 교차검증·이미지, 0003 하네스 엔지니어링 피벗)
manuscript/<slug>.md ← 원고 (front-matter + 본문)
scripts/             ← scaffold/status/verify/crosscheck/render_images (저자 전용)
assets/diagrams/<slug>/*.svg     ← 다이어그램 소스(SoT)
assets/screenshots/<slug>/*.png  ← 렌더된 다이어그램 + 캡처 (발행 시 업로드)
```
