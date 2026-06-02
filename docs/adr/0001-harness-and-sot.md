# ADR 0001 — 하네스 구조와 진실의 원천

- 상태: 채택
- 날짜: 2026-06-02

## 맥락

위키독스에 개발자용 기술서 **"12-Factor Agents로 배우는 하네스 엔지니어링"**을 MCP 자동화로 발행한다. 집필·검수·발행이 여러 세션에 걸쳐 진행되고, factor 정의·출처·명칭이 반복 등장하며, 위키독스에는 명시적 순서 파라미터가 없다(생성 순서 = 표시 순서). 에이전트가 세션이 끊겨도 일관되게 이어 작업할 환경이 필요하다.

> 메타: 이 책이 가르치는 12-Factor 원칙(특히 5·6·12 — 상태 통합·재개·무상태 리듀서)을 **이 하네스가 그대로 실천**한다. 그래서 이 ADR의 결정은 곧 책의 예제이기도 하다.

## 결정

1. **원고 SoT = 로컬 마크다운** (`manuscript/<slug>.md`). 집필→검수→발행은 로컬에서 끝내고 wikidocs MCP로 push. 위키독스는 발행 타깃이지 SoT가 아니다.
2. **구조 SoT = `docs/toc.json`.** 부/장/링크의 단일 원천. 장 추가·이동은 toc.json을 고친 뒤 `scaffold.py`로 반영.
3. **사실 SoT = `docs/verified-facts.md`.** factor 번호·이름·정의·순서 + 출처·명칭 + 금지표현(denylist). `verify.py`가 강제.
4. **진행 상태 = 각 원고 front-matter** (`status`, `wikidocs_page_id`). 별도 매니페스트를 저장하지 않아 drift를 원천 차단. 상태는 `status.py`가 front-matter를 스캔해 생성(저장 안 함) — **Factor 5(상태 통합)·12(무상태 리듀서)의 실물**.
5. **검증 = 스크립트 invariant.** `verify.py`가 front-matter 스키마·템플릿 섹션·official_links 일치·denylist·crosscheck 게이트를 검사하고, PASS가 발행의 전제.

## 근거

- 로컬 SoT는 diff·롤백·검수·재현성에서 위키독스 직접 집필보다 우월하다(에이전트 친화).
- front-matter 단일 상태원은 "매니페스트 ↔ 파일" 이중 기록의 drift를 없앤다.
- 사실/구조를 기계가 읽는 단일 파일로 두면 "한 곳을 고치면 검증이 따라온다"는 invariant가 성립한다.

## 대안

- 위키독스 직접 집필: 검증·재개·버전관리가 약해 기각.
- 별도 manifest.json: front-matter와 중복되어 drift 위험, 기각.
- YAML toc: stdlib 파서 부재로 의존성 발생 → JSON 채택.

## 영향

- 새 장 추가 절차가 고정된다(toc.json → scaffold → write → verify → publish).
- 4부 케이스 스터디는 이 ADR과 스크립트들을 **의도적으로 본문에 노출**해 해부한다(도구 노출 경계의 명시적 예외).
