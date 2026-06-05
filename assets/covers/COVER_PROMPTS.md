# 책 표지 이미지 생성 프롬프트 (ChatGPT / gpt-image-1 용)

> 책: **8원칙으로 살펴보는 하네스 엔지니어링 — 에이전트가 일하는 코드베이스 만들기**
> 사용법: 아래 5개 블록 중 하나를 통째로 복사 → ChatGPT(이미지 생성)에 붙여넣기. 각 블록은 독립 완결형(스타일 포함).
> 비율: **세로 10:13 책 표지**(위키독스 표지 권장 비율, 예: 1000×1300). "portrait book cover, 10:13 aspect ratio" 명시.
> ⚠️ gpt-image-1의 네이티브 세로 사이즈는 1024×1536(2:3)뿐이라 정확히 10:13이 안 나올 수 있음 → 1024×1536으로 생성 후 **상하 크롭으로 10:13(예: 1024×1331)** 맞추기. 크롭을 전제로 상하 여백을 넉넉히 잡도록 각 프롬프트에 명시해 둠.

## ⚠️ 한글 텍스트 주의
이미지 모델은 한글 글자를 종종 깨뜨립니다. 두 가지 방법:
- (권장) **글자 없이 배경 아트만** 생성 → 제목·부제는 Figma/Canva 등에서 얹기. 각 프롬프트 끝에 "글자 없이" 옵션을 적어둠.
- 또는 프롬프트대로 한글 포함 생성 후, 글자가 깨지면 재시도하거나 텍스트만 후보정.

표지에 들어갈 정확한 텍스트(후보정 시 사용):
- 키커(작게, 메인 제목 위): **8원칙으로 살펴보는**
- 메인 제목: **하네스 엔지니어링**
- 부제: **에이전트가 일하는 코드베이스 만들기**
- 태그라인: **사람이 조종하고, 에이전트가 실행한다**

> 전체 제목은 "8원칙으로 살펴보는 하네스 엔지니어링"이지만, 표지에서는 **키커("8원칙으로 살펴보는") + 메인("하네스 엔지니어링")의 2단 록업**으로 조판해야 가독성이 산다. 한 줄로 욱여넣지 말 것.

공통 브랜드 색: 잉크 #1B2733, 파랑 #2D6CDF, 초록 #36B37E, 빨강 포인트 #E5484D, 라이트 배경 #F7F9FC, 딥 네이비 #0E1A2B.
공통 미감: 모던 개발자 기술서 표지, 깔끔한 기하·벡터 그래픽, 과한 그라데이션·사진풍·스톡 일러스트 금지, 넉넉한 여백, 제목 가독성 최우선.

---

## 변형 1 — 조종 → 실행 (Humans steer, agents execute)

```
A modern, minimal developer tech-book cover, portrait orientation, 10:13 aspect ratio book cover (slightly taller than 3:4; keep generous top and bottom margins safe for cropping). Clean geometric vector style, generous whitespace, light background (#F7F9FC). Central motif: a single "steering" node at the top (a small abstract control/steering glyph in blue #2D6CDF) from which several smooth flow-lines branch downward and pass through a few rounded code/task blocks rendered in green #36B37E — visually contrasting steering (blue) and execution (green). Confident, trustworthy, high-end O'Reilly-meets-modern aesthetic. Ink color #1B2733 for text. Title lockup near the top as two tiers: a small kicker line "8원칙으로 살펴보는" above, then the main Korean title very large: "하네스 엔지니어링", followed by a smaller subtitle "에이전트가 일하는 코드베이스 만들기", and a bottom tagline "사람이 조종하고, 에이전트가 실행한다". Keep typography crisp and legible; do not let decoration overlap the title. No photographic elements, no busy gradients.
```
글자 없이 옵션: 위에서 `Title lockup near the top ...` 문장을 빼고 `Leave clear empty space at the top and bottom for title text to be added later.`로 교체.

---

## 변형 2 — 게이트 파이프라인 (Verification gates)

```
A striking, technical developer tech-book cover, portrait orientation, 10:13 aspect ratio book cover (keep generous top and bottom margins safe for cropping). Deep navy background (#0E1A2B) with crisp neon-like blue (#2D6CDF) and green (#36B37E) line work. Central motif: a vertical pipeline flowing top-to-bottom in which an artifact passes through 3–4 rectangular "gates" (rounded rectangles); passed gates glow green, a blocked one accented in red (#E5484D). Eight small luminous nodes (representing the 8 principles) distributed alongside the pipeline. Modern, high-contrast, engineered feel; clean vector geometry, ample negative space. Title text in white near the top as a two-tier lockup: small kicker "8원칙으로 살펴보는" above the large main title "하네스 엔지니어링", subtitle "에이전트가 일하는 코드베이스 만들기", bottom tagline "사람이 조종하고, 에이전트가 실행한다". Crisp legible typography, no photographic textures.
```
글자 없이 옵션: 제목 문장 제거하고 `Leave clean empty bands at top and bottom for later text overlay.` 추가.

---

## 변형 3 — 빈 레포에서 구조로 (Empty → structured)

```
A minimal, data-visualization-inspired developer tech-book cover, portrait orientation, 10:13 aspect ratio book cover (keep generous top and bottom margins safe for cropping). Light background (#F7F9FC), ink (#1B2733) and blue (#2D6CDF) accents. Concept: on one side scattered sparse dots (an empty git repo, chaos); transitioning toward the other side into an ordered grid / layered architecture that converges into clean structure — depicting growth "from an empty repo to a million lines". Elegant, restrained, geometric. Title lockup placed on the ordered/structured side so it reads as the resolution of chaos→order: small kicker "8원칙으로 살펴보는" above the large main title "하네스 엔지니어링", with subtitle "에이전트가 일하는 코드베이스 만들기" below. Crisp legible typography, lots of whitespace, no photographic elements.
```
글자 없이 옵션: 제목 문장 빼고 `Reserve a clean area on the structured side for title text to be added later.` 추가.

---

## 변형 3-R — 기존 표지 리메이크: 타이틀 가독성 강화 (스타일 유지)

> 현재 채택본(`cover-empty-to-structured.png`, 변형 3)의 **스타일·모티프·색은 그대로 두고**, 콘텐츠 배치와 레이아웃만 다시 짜서 키커·메인 제목·부제가 또렷하게 읽히도록 만드는 프롬프트.
> **권장 사용법: 기존 표지 이미지를 첨부하고** 아래 블록을 붙여넣기(스타일 레퍼런스로 쓰게 함). 첨부 없이 단독 생성해도 동작하도록 스타일 서술을 포함해 둠.

```
Redesign the layout of the attached book cover while strictly preserving its visual style: light background (#F7F9FC), ink (#1B2733) and blue (#2D6CDF) accents, minimal data-visualization aesthetic, the "scattered sparse dots converging into an ordered grid / layered architecture" motif (chaos → order), elegant, restrained, geometric, portrait 10:13 aspect ratio book cover (keep generous top and bottom margins safe for cropping). Do NOT change the art style, color palette, or motif — only restructure the composition for title legibility. New layout: dedicate the TOP ~40% of the cover to a clean, nearly empty band for the title lockup with strong contrast against the background; compress the dots→structure motif into the LOWER ~55%, flowing left-to-right, with its highest visual density kept away from all text. Title lockup, top-aligned and left-aligned, in this order and scale: (1) small kicker "8원칙으로 살펴보는" with a subtle blue accent, (2) the main Korean title "하네스 엔지니어링" set VERY LARGE — at least twice the kicker size, the single most dominant element on the cover, ink #1B2733 at full opacity, (3) subtitle "에이전트가 일하는 코드베이스 만들기" at roughly 40% of the main title size with clear spacing below it. Optional small tagline "사람이 조종하고, 에이전트가 실행한다" near the bottom edge, clear of the motif. Ensure every text block sits on a quiet area — no dots, lines, or grid elements behind or overlapping any letterform. Crisp, perfectly legible Korean typography; generous whitespace; no photographic elements; no busy gradients.
```

글자 없이 옵션: 제목 문장들을 빼고 `Keep the top ~40% of the cover as a clean empty band for title text to be added later; compress the dots→structure motif into the lower half.`로 교체 → 텍스트는 디자인 툴에서 얹기.

생성 팁: 첨부 이미지 없이 돌리면 모티프가 달라질 수 있음 → 그땐 기존 표지를 함께 첨부하고 "match the attached cover's style exactly"를 프롬프트 맨 앞에 한 줄 추가. 한글 타이포가 깨지면 "글자 없이" 옵션이 1순위.

---

## 변형 4 — 타이포 중심 미니멀 (Typographic hero)

```
A minimalist typographic developer tech-book cover, portrait orientation, 10:13 aspect ratio book cover (keep generous top and bottom margins safe for cropping). White / very light background (#F7F9FC), ink text (#1B2733), a single blue accent (#2D6CDF). The cover is almost pure typography: a small kicker line "8원칙으로 살펴보는" sitting above the main Korean title "하네스 엔지니어링" set very large across two lines, dominating the composition, with one syllable or word accented in blue. The kicker may carry a subtle blue numeral "8" treatment. In the background, only a faint pair of parallel rails/guide-lines gently curving (a subtle "harness/guide rail" motif), very low contrast. Subtitle "에이전트가 일하는 코드베이스 만들기" smaller below, and a bottom tagline "사람이 조종하고, 에이전트가 실행한다". Restrained, premium, like a modern O'Reilly cover. Decoration minimal; typographic hierarchy is the whole design. Perfectly legible text, no clutter.
```
글자 없이 옵션: 이 변형은 타이포가 핵심이라 "글자 없이"는 권하지 않음(필요하면 배경 레일 모티프만: `Only the faint curved parallel rails on a light background, no text.`).

---

## 변형 5 — 자율 루프 (The encoded autonomy loop)

```
A clean, conceptual developer tech-book cover, portrait orientation, 10:13 aspect ratio book cover (keep generous top and bottom margins safe for cropping). Choose high contrast (either light #F7F9FC or deep #0E1A2B background). Central motif: a closed circular loop / orbit in blue (#2D6CDF), with eight small nodes along it representing the 8 principles — some nodes green (#36B37E) for "passed", one red (#E5484D) accent point. At one point on the loop, a distinct "human steering" node highlighted with a dashed blue outline. The unbroken loop conveys autonomy; the human node conveys control. Geometric, balanced, modern. Title lockup in the open space above the loop: small kicker "8원칙으로 살펴보는" above the large main title "하네스 엔지니어링", subtitle "에이전트가 일하는 코드베이스 만들기", bottom tagline "사람이 조종하고, 에이전트가 실행한다". Crisp legible typography, generous whitespace, no photographic elements.
```
글자 없이 옵션: 제목 문장 제거하고 `Center the loop with clean empty margins above and below for later text.` 추가.

---

### 생성 팁
- gpt-image-1은 10:13을 직접 지원하지 않음 → **1024×1536(세로)으로 생성 → 상하 크롭해 10:13(예: 1024×1331)** 으로 마감. 프롬프트의 "generous top/bottom margins" 덕에 크롭해도 구도가 살아야 정상.
- 위키독스 업로드용 최종 크기 예: 1000×1300 (또는 500×650).
- 한글이 깨지면: (1) 같은 프롬프트로 1~2회 재생성, (2) 그래도 깨지면 "글자 없이" 옵션으로 배경만 뽑고 텍스트는 디자인 툴에서 얹기. 특히 키커("8원칙으로 살펴보는")는 작은 글자라 깨지기 쉬움 — 후보정 1순위.
- 5개를 만든 뒤 마음에 드는 1개를 골라 `assets/covers/`에 저장하면 발행 때 책 표지로 쓸 수 있음.
