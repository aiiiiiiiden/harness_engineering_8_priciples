# 책 표지 이미지 생성 프롬프트 (ChatGPT / gpt-image-1 용)

> 책: **하네스 엔지니어링 — 에이전트가 일하는 코드베이스 만들기**
> 사용법: 아래 5개 블록 중 하나를 통째로 복사 → ChatGPT(이미지 생성)에 붙여넣기. 각 블록은 독립 완결형(스타일 포함).
> 비율: **세로 2:3 책 표지**(예: 1024×1536). "portrait book cover" 명시.

## ⚠️ 한글 텍스트 주의
이미지 모델은 한글 글자를 종종 깨뜨립니다. 두 가지 방법:
- (권장) **글자 없이 배경 아트만** 생성 → 제목·부제는 Figma/Canva 등에서 얹기. 각 프롬프트 끝에 "글자 없이" 옵션을 적어둠.
- 또는 프롬프트대로 한글 포함 생성 후, 글자가 깨지면 재시도하거나 텍스트만 후보정.

표지에 들어갈 정확한 텍스트(후보정 시 사용):
- 메인 제목: **하네스 엔지니어링**
- 부제: **에이전트가 일하는 코드베이스 만들기**
- 메타: **OpenAI Harness Engineering 정본에서 도출한 8원칙**
- 태그라인: **사람이 조종하고, 에이전트가 실행한다**

공통 브랜드 색: 잉크 #1B2733, 파랑 #2D6CDF, 초록 #36B37E, 빨강 포인트 #E5484D, 라이트 배경 #F7F9FC, 딥 네이비 #0E1A2B.
공통 미감: 모던 개발자 기술서 표지, 깔끔한 기하·벡터 그래픽, 과한 그라데이션·사진풍·스톡 일러스트 금지, 넉넉한 여백, 제목 가독성 최우선.

---

## 변형 1 — 조종 → 실행 (Humans steer, agents execute)

```
A modern, minimal developer tech-book cover, portrait orientation (2:3 book cover). Clean geometric vector style, generous whitespace, light background (#F7F9FC). Central motif: a single "steering" node at the top (a small abstract control/steering glyph in blue #2D6CDF) from which several smooth flow-lines branch downward and pass through a few rounded code/task blocks rendered in green #36B37E — visually contrasting steering (blue) and execution (green). Confident, trustworthy, high-end O'Reilly-meets-modern aesthetic. Ink color #1B2733 for text. Include the Korean title text large near the top: "하네스 엔지니어링", a subtitle "에이전트가 일하는 코드베이스 만들기", and a bottom tagline "사람이 조종하고, 에이전트가 실행한다". Keep typography crisp and legible; do not let decoration overlap the title. No photographic elements, no busy gradients.
```
글자 없이 옵션: 위에서 `Include the Korean title text ...` 문장을 빼고 `Leave clear empty space at the top and bottom for title text to be added later.`로 교체.

---

## 변형 2 — 게이트 파이프라인 (Verification gates)

```
A striking, technical developer tech-book cover, portrait orientation (2:3 book cover). Deep navy background (#0E1A2B) with crisp neon-like blue (#2D6CDF) and green (#36B37E) line work. Central motif: a vertical pipeline flowing top-to-bottom in which an artifact passes through 3–4 rectangular "gates" (rounded rectangles); passed gates glow green, a blocked one accented in red (#E5484D). Eight small luminous nodes (representing 8 principles) distributed alongside the pipeline. Modern, high-contrast, engineered feel; clean vector geometry, ample negative space. Title text in white, large near the top: "하네스 엔지니어링", subtitle "에이전트가 일하는 코드베이스 만들기", bottom tagline "사람이 조종하고, 에이전트가 실행한다". Crisp legible typography, no photographic textures.
```
글자 없이 옵션: 제목 문장 제거하고 `Leave clean empty bands at top and bottom for later text overlay.` 추가.

---

## 변형 3 — 빈 레포에서 구조로 (Empty → structured)

```
A minimal, data-visualization-inspired developer tech-book cover, portrait orientation (2:3 book cover). Light background (#F7F9FC), ink (#1B2733) and blue (#2D6CDF) accents. Concept: on one side scattered sparse dots (an empty git repo, chaos); transitioning toward the other side into an ordered grid / layered architecture that converges into clean structure — depicting growth "from an empty repo to a million lines". Elegant, restrained, geometric. Title text placed on the ordered/structured side so it reads as the resolution of chaos→order: "하네스 엔지니어링" large, subtitle "에이전트가 일하는 코드베이스 만들기", and a small meta line "OpenAI Harness Engineering 정본에서 도출한 8원칙". Crisp legible typography, lots of whitespace, no photographic elements.
```
글자 없이 옵션: 제목 문장 빼고 `Reserve a clean area on the structured side for title text to be added later.` 추가.

---

## 변형 4 — 타이포 중심 미니멀 (Typographic hero)

```
A minimalist typographic developer tech-book cover, portrait orientation (2:3 book cover). White / very light background (#F7F9FC), ink text (#1B2733), a single blue accent (#2D6CDF). The cover is almost pure typography: the Korean title "하네스 엔지니어링" set very large across two lines, dominating the composition, with one syllable or word accented in blue. In the background, only a faint pair of parallel rails/guide-lines gently curving (a subtle "harness/guide rail" motif), very low contrast. Subtitle "에이전트가 일하는 코드베이스 만들기" smaller below, a bottom tagline "사람이 조종하고, 에이전트가 실행한다", and a small meta "OpenAI Harness Engineering 정본에서 도출한 8원칙". Restrained, premium, like a modern O'Reilly cover. Decoration minimal; typographic hierarchy is the whole design. Perfectly legible text, no clutter.
```
글자 없이 옵션: 이 변형은 타이포가 핵심이라 "글자 없이"는 권하지 않음(필요하면 배경 레일 모티프만: `Only the faint curved parallel rails on a light background, no text.`).

---

## 변형 5 — 자율 루프 (The encoded autonomy loop)

```
A clean, conceptual developer tech-book cover, portrait orientation (2:3 book cover). Choose high contrast (either light #F7F9FC or deep #0E1A2B background). Central motif: a closed circular loop / orbit in blue (#2D6CDF), with small nodes along it representing stages (verify, recover, execute) — some nodes green (#36B37E) for "passed", one red (#E5484D) accent point. At one point on the loop, a distinct "human steering" node highlighted with a dashed blue outline. The unbroken loop conveys autonomy; the human node conveys control. Geometric, balanced, modern. Title text in the open space above/below the loop: "하네스 엔지니어링" large, subtitle "에이전트가 일하는 코드베이스 만들기", bottom tagline "사람이 조종하고, 에이전트가 실행한다". Crisp legible typography, generous whitespace, no photographic elements.
```
글자 없이 옵션: 제목 문장 제거하고 `Center the loop with clean empty margins above and below for later text.` 추가.

---

### 생성 팁
- 비율이 안 맞으면 "make it a tall portrait 2:3 book cover, 1024×1536"를 덧붙이기.
- 한글이 깨지면: (1) 같은 프롬프트로 1~2회 재생성, (2) 그래도 깨지면 "글자 없이" 옵션으로 배경만 뽑고 텍스트는 디자인 툴에서 얹기.
- 5개를 만든 뒤 마음에 드는 1개를 골라 `assets/covers/`에 저장하면 발행 때 책 표지로 쓸 수 있음.
