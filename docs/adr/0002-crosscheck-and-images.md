# ADR 0002 — codex 교차 검증과 이미지 파이프라인

- 상태: 채택
- 날짜: 2026-06-02

## 맥락

이 책의 신뢰도는 (1) **8원칙 정의·출처·코드의 사실 정확성**과 (2) 개념을 풀어주는 **이미지**가 좌우한다. 집필을 Claude 한 모델이 하면 그 모델의 사각지대(예: 원칙 순서 혼동, 출처 오귀속, 정본이 명시 안 한 카운트를 단정)가 그대로 책에 남고, 이미지를 AI 래스터로 생성하면 재현·수정·일관성이 깨진다.

> 메타: 교차검증은 곧 **원칙 5(기계적 강제)·7(자율 루프의 피드백)**, 이미지 파이프라인은 **원칙 4(에이전트 가독성)·결정론**의 예제다.

## 결정

### 1. 교차 검증 = 독립 모델(codex)
- 집필(Claude) 외에 **codex CLI**(`codex exec`)로 기술 사실을 독립 검증한다 → 모델 다양성으로 사각지대를 줄인다. 특히 **원칙 번호·이름·정의·순서**와 출처·명칭, 그리고 "정본에서 도출한 8원칙"이라는 비정본 카운트 표기를 점검.
- 신뢰성 장치: `--output-schema`(JSON Schema 강제) + `-o`(최종 메시지 파일) + `sandbox_mode=read-only`(원고 수정 불가) + stdin DEVNULL(멈춤 방지).
- `scripts/crosscheck.py`가 원고 본문 + `verified-facts.md`를 codex에 넘겨 `{verdict, severity, evidence, fix}` 배열을 받는다. 결과는 `.harness-cache/crosscheck/<slug>.json`.
- **reviewed 게이트 = 4중**: `verify.py`(기계) + `md-doc-reviewer`(Claude) + `crosscheck.py`(codex) + `/humanize`(문체). 넷이 합의해야 reviewed. 통과 시 front-matter `crosscheck: pass`·`humanized: pass`를 자동 도장 → 없으면 `verify.py`가 발행을 막는다.
- 두 모델이 엇갈리면 정본(openai.com/index/harness-engineering)을 근거로 사람이 결정한다.

### 2. 이미지 = 코드(SVG) → 결정론적 렌더
- 개념 다이어그램(에이전트 루프·상태 통합·reducer 등)은 **AI 래스터 생성 금지**. `assets/diagrams/<slug>/*.svg`를 코드로 작성(진실의 원천).
- `scripts/render_images.py`가 `rsvg-convert`로 `assets/screenshots/<slug>/*.png`(@2x) 생성. SVG 수정 시 재렌더.
- 전 장 일관성을 위해 하우스 스타일(색·폰트·치수)을 `conventions.md` §8에 고정. 폰트 `Apple SD Gothic Neo`로 한글 글리프 보장, 코드 라벨은 monospace 허용.
- 렌더 후 PNG를 Read로 **눈 검수**한 뒤 채택. 스크린샷(실제 화면)만 `/browse`·`/qa`로 캡처.

## 근거

- codex `--output-schema`는 자유 텍스트 파싱의 불안정성을 제거해 스크립트화·재실행이 가능하다.
- SVG-as-code는 diff·롤백·일관성·재현성에서 AI 이미지보다 우월하며, 본 하네스의 "텍스트 SoT → 산출물" 철학과 일치한다.
- 둘 다 결정론적이거나 게이트화되어 "신뢰할 수준"의 요구를 만족한다.

## 대안 / 기각

- 단일 모델 자기검토: 사각지대 동일, 기각.
- Mermaid(mmdc): chromium 다운로드 필요로 무겁고 불안정 → `rsvg-convert` 채택.

## 영향

- 집필 비용에 codex 1회 호출(수십 초~수 분)이 추가되나, 원칙을 틀리게 가르치는 비용보다 싸다.
- `.harness-cache/`는 gitignore(검증 산출물). 다이어그램 SVG와 렌더 PNG는 커밋(리뷰 가시성).
