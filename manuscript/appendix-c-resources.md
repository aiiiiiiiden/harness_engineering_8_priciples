---
part: 부록
chapter: C
slug: appendix-c-resources
title: "참고 자료"
status: "published"
wikidocs_page_id: 363239
parent_page_id: 363217
official_links:
  - https://openai.com/index/harness-engineering/
  - https://code.claude.com/docs
  - https://modelcontextprotocol.io
last_verified: 2026-06-03
crosscheck: "pass"
crosscheck_date: "2026-06-05"
humanized: "pass"
humanized_date: "2026-06-03"
---

## 이 장에서 배우는 것

이 부록은 더 깊이 파고들 때 펴는 **1차 출처 지도**입니다. 이 책의 모든 주장이 어디에 접지하는지, 실습 도구의 공식 문서는 어디인지, 그리고 각 장이 원문의 어느 절에서 나왔는지를 한곳에 모았습니다. 2차 요약(블로그·영상)이 아니라 **원문**으로 곧장 가는 길을 알려드립니다.

## 핵심 개념

자료를 세 층으로 나눕니다. **1차 출처(원문)**가 가장 위, 그 아래 **실습 도구 공식 문서**, 맨 아래 **이 책의 내부 기준(SoT)**입니다. 주장을 확인할 때는 항상 위층부터 봅니다.

### (가) 1차 출처 — 원문

| 자료 | 무엇 | 링크 |
|---|---|---|
| **Harness Engineering** (OpenAI, Ryan Lopopolo, 2026-02-11) | 이 책의 원문. "사람이 조종하고, 에이전트가 실행한다"와 8원칙의 도출 근거. 빈 저장소에서 5개월간 약 100만 줄을 Codex만으로 구축한 실험 보고. | https://openai.com/index/harness-engineering/ |

> 이 책의 8원칙은 위 글의 **11개 절 중 원칙을 담은 8개 절에서 도출**한 것입니다(원문은 원칙을 번호로 매기지 않습니다). 절 ↔ 원칙 대응은 아래 (라)를 보세요.

### (나) 실습 도구 공식 문서

| 도구 | 무엇 | 링크 |
|---|---|---|
| **Claude Code · Claude Agent SDK** | 실습에 쓰는 코딩 에이전트 CLI와, 에이전트를 만드는 SDK(과거 "Claude Code SDK"에서 변경). | https://code.claude.com/docs |
| **MCP (Model Context Protocol)** | 에이전트와 외부 도구·데이터를 연결하는 공개 프로토콜의 명세. | https://modelcontextprotocol.io |
| **OpenAI Codex** | 원문 실험의 코딩 에이전트. 원문 글과 같은 출처에서 다룬다. | https://openai.com/index/harness-engineering/ |

> 외부 라이브러리 문서는 원문의 방식대로 **요약본을 프로젝트 저장소에 둡니다**. `docs/references/*-llms.txt`에 핵심만 추려 버전 관리하면, 에이전트가 매번 외부를 긁지 않고도 안정적으로 참조합니다(원칙 3, ch06).

### (다) 이 책의 내부 기준 (Source of Truth)

이 책 자체가 하나의 하네스라, 사실과 구조의 기준이 프로젝트 저장소 안에 있습니다. 원문 인용을 검증하려면 이 파일들과 대조하세요.

| 파일 | 역할 |
|---|---|
| `docs/verified-facts.md` | 8원칙 정의·출처·명칭의 진실의 원천. 원문 절 매핑과 denylist 포함. |
| `docs/conventions.md` | 집필 규약. §5가 용어 표준(부록 B와 한 쌍). |
| `docs/toc.json` | 책 구조의 단일 원천. 각 장의 `official_links`가 여기서 정해진다. |
| `docs/adr/` | 핵심 결정 기록(하네스·SoT, 교차검증·이미지, 하네스 엔지니어링 피벗, 본문 다이어그램=ChatGPT 한국어 래스터). |

### (라) 장 ↔ 원문 절 대응

각 장이 원문의 어느 절에 접지하는지입니다. 원문 절 제목은 원문(영문) 그대로 옮겼습니다.

| 이 책 | 원문 절 (verbatim) |
|---|---|
| 1부 (ch01~03) 입문 | We started with an empty git repository *(실험 도입)* |
| 원칙 1 (ch04) | Redefining the role of the engineer |
| 원칙 2 (ch05) | Increasing application legibility |
| 원칙 3 (ch06) | We made repository knowledge the system of record |
| 원칙 4 (ch07) | Agent legibility is the goal |
| 원칙 5 (ch08) | Enforcing architecture and taste |
| 원칙 6 (ch09) | Throughput changes the merge philosophy |
| *(원칙 미승격)* | What "agent-generated" actually means *(개념 절 → 철학·원칙 5·7 배경)* |
| 원칙 7 (ch10) | Increasing levels of autonomy |
| 원칙 8 (ch11) | Entropy and garbage collection |
| 맺음 참고 | What we're still learning *(원칙 아님)* |

> 3부(ch12~15)와 4부(ch16~17)는 특정 절이 아니라 8원칙을 **합치는** 패턴과 이 책 하네스의 자기 해부라, 위 절들을 가로지릅니다.

## 왜 중요한가

참고 자료를 정리하는 일은 장식이 아니라 **신뢰의 사슬**입니다. 기술서의 주장은 추적 가능해야 합니다. 독자가 "정말 그런가?"를 1차 출처에서 직접 확인할 수 있어야 하고, 그러려면 출처가 2차 요약이 아니라 원문을 가리켜야 합니다.

이건 원칙 3(기록 시스템)을 책이라는 산출물에 적용한 것입니다. 원문은 "에이전트가 검색할 수 없는 지식은 없는 것과 같다"고 했는데, 독자에게도 똑같습니다. 본문이 "원문에 따르면…"이라고만 하고 어느 절인지 가리키지 않으면, 그 주장은 검증할 수 없는 채로 남습니다.

규모에서 더 분명해집니다. 장이 스무 개로 늘면 출처도 흩어집니다. 링크를 한곳(`toc.json`)에 등록하고 기계로 점검하지 않으면, 죽은 링크와 어긋난 인용이 조용히 쌓여 엔트로피(원칙 8)가 됩니다.

## 하네스에 적용하기

이 책은 참고 링크를 **구조로** 관리합니다. 사람이 기억하는 대신 프로젝트 저장소가 강제합니다.

| 단계 | 아티팩트 | 역할 |
|---|---|---|
| 1. 링크 등록 | `docs/toc.json`의 각 장 `official_links` | 링크의 단일 원천 |
| 2. `scaffold.py` | `manuscript/<slug>.md` front-matter의 `official_links` | toc.json과 일치해야 함 |
| 3. `verify.py` | 본문의 공식 도메인 링크 | `official_links`에 없으면 경고 |

`scripts/verify.py`는 두 가지를 봅니다. front-matter의 `official_links`가 `toc.json`과 어긋나면 **에러**로 막고, 본문에 등장한 공식 도메인 링크가 그 목록에 없으면 **경고**합니다. 그래서 새 출처를 인용하려면 `toc.json`에 먼저 등록하는 습관이 강제됩니다. 이 부록을 쓸 때도 `code.claude.com/docs`와 `modelcontextprotocol.io`를 먼저 `toc.json`에 넣고서야 본문에 인용했습니다.

여러분의 프로젝트라면, 외부 문서를 직접 링크만 걸어두기보다 핵심을 `docs/references/`에 요약해 버전 관리하고, 링크 목록을 한 파일에 모아 죽은 링크를 주기적으로 점검하는 것에서 시작하면 됩니다.

## 안티패턴과 함정

- **2차 출처로 때우기.** 원문 대신 그것을 요약한 블로그나 영상을 인용하는 것. 요약은 틀리거나 낡기 쉽습니다. 항상 원문을 먼저 가리키고, 2차 자료는 보조로만 둡니다.
- **죽은 링크 방치.** 링크를 걸고 점검하지 않는 것. URL이 바뀌거나 사라져도 아무도 모릅니다. 링크를 한곳에 모아 기계로 점검합니다.
- **출처를 본문에만 두기.** 인용 링크를 `toc.json`에 등록하지 않은 채 본문에만 적어두면, 장마다 출처가 흩어져 점검할 수 없습니다. 링크는 구조(`toc.json`)에 먼저 등록합니다.
- **버전 없는 인용.** "원문에 따르면"으로 끝내고 어느 절인지 안 밝히는 것. 독자가 확인할 수 없습니다. 위 (라)처럼 절 단위로 접지합니다.

## 핵심 정리 / 체크리스트

- [ ] 주장은 **1차 출처**(원문·공식 문서)로 추적 가능해야 한다. 2차 요약은 보조.
- [ ] 8원칙의 근거는 원문 11개 절 중 8개. 절 ↔ 원칙 대응은 위 (라)를 따른다.
- [ ] 외부 문서는 `docs/references/*-llms.txt`로 **요약해 프로젝트 저장소에 둔다**(원칙 3).
- [ ] 인용 링크는 `toc.json`에 **먼저 등록**하고 본문에 쓴다(`verify.py`가 점검).
- [ ] 사실의 기준은 `docs/verified-facts.md`, 용어는 `docs/conventions.md` §5와 부록 B다.

## 공식 출처

- https://openai.com/index/harness-engineering/
- https://code.claude.com/docs
- https://modelcontextprotocol.io
