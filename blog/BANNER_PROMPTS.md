# 블로그 배너 이미지 생성 프롬프트 (ChatGPT / gpt-image-1 용)

> 글: **에이전트가 짠 코드는 왜 프로덕션에서 무너질까 — 하네스 엔지니어링 8원칙과 4가지 패턴** (`blog/harness-engineering-blog.md`)
> 용도: 블로그 상단 히어로 배너 · 소셜 공유 카드(OG 이미지) · 썸네일.
> 사용법: 아래 블록 중 하나를 통째로 복사 → ChatGPT(이미지 생성)에 붙여넣기. 각 블록은 독립 완결형(스타일 포함).
> **스타일은 이 책의 기존 표지·다이어그램과 동일 계열**(같은 팔레트·기하 벡터 미감)이라, 일관성을 위해 **기존 표지(`assets/covers/cover-empty-to-structured.png`)나 다이어그램 렌더(`assets/diagrams/chatgpt-renders/*.ko.png`) 1장을 첨부**하고 "match the attached image's style exactly"를 맨 앞에 붙이면 룩이 잘 붙는다.

## 비율 / 크기
- **히어로 배너(가로 와이드)**: 16:9 (예: 1600×900). 소셜 공유는 **OG 카드 1.91:1**(1200×630)이 표준.
- ⚠️ gpt-image-1의 네이티브 가로 사이즈는 **1536×1024(3:2)** 뿐 → 1536×1024로 생성한 뒤 **좌우/상하 크롭**으로 16:9나 1.91:1을 맞춘다. 각 프롬프트에 "generous margins on all sides safe for cropping"을 넣어 크롭해도 구도가 살게 했다.

## ⚠️ 한글 텍스트 주의 (표지 문서와 동일 정책)
이미지 모델은 한글 글자를 자주 깨뜨린다. 두 가지 방법:
- **(권장) 글자 없이 배경 아트만** 생성 → 제목·후크는 Figma/Canva에서 얹기. 각 프롬프트 끝에 "글자 없이" 옵션을 적어 둠.
- 아트 안의 라벨이 필요하면 다이어그램 규칙대로 **대문자 영문(UPPERCASE English)** 으로만 둔다(한글 라벨 금지).

배너에 얹을 정확한 텍스트(후보정용):
- 키커(작게): **8원칙으로 살펴보는**
- 메인: **하네스 엔지니어링**
- 후크/부제: **에이전트가 짠 코드는 왜 프로덕션에서 무너질까** (또는 **8원칙 + 4가지 패턴**)
- 태그라인: **사람이 조종하고, 에이전트가 실행한다**

## 공통 브랜드 (표지·다이어그램과 동일)
- 색: 잉크 `#1B2733`, 흐린 텍스트 `#5B6B7A`, 파랑 `#2D6CDF`, 초록 `#36B37E`(통과/성공 전용), 빨강 `#E5484D`(차단/실패 전용), 라이트 배경 `#F7F9FC`, 딥 네이비 `#0E1A2B`.
- 미감: 모던 개발자 기술서, 깔끔한 기하·플랫 벡터, 얇은 선(2.5–3.5px)·작고 깔끔한 화살촉, 흰 라운드 박스(반경 ~14px·2px 테두리), 넉넉한 여백. **사진풍·3D·과한 그라데이션·스톡 일러스트 금지.**

---

## 변형 1 — 조종→실행 + 8원칙 + 4패턴 (히어로 종합)

```
A modern, minimal developer-blog hero banner, landscape orientation, wide 16:9 (generate 1536×1024 with generous margins on all sides, safe for cropping). Flat geometric vector style, NOT 3D, no photo, clean thin-line work, airy whitespace. Palette: light background #F7F9FC, ink #1B2733, muted #5B6B7A, primary blue #2D6CDF, green #36B37E for pass/success only, red #E5484D for block/fail only. Composition flows left → right: on the LEFT a single "steering" node (small abstract control glyph, blue #2D6CDF) labeled "HUMANS STEER"; smooth blue flow-lines branch rightward into a row of rounded execution blocks (green #36B37E) labeled "AGENTS EXECUTE". Along the MIDDLE band, eight small luminous nodes in a gentle arc represent "8 PRINCIPLES". On the RIGHT, four stacked rounded tiles represent the patterns: "SOURCE OF TRUTH", "VERIFICATION GATES", "DETERMINISTIC ARTIFACTS", "MULTI-AGENT". UPPERCASE English labels only, short and legible; monospace for any code identifiers. Reserve a clean quiet band across the top for a title overlay. Crisp, premium, O'Reilly-meets-modern engineering aesthetic; no busy gradients, no photographic texture.
```
글자 없이 옵션: 위 라벨 문장들을 빼고 `Keep all labels minimal or omit them; leave a clean empty band across the top and along the left for title text to be added later.`로 교체.

---

## 변형 2 — 검증 게이트 파이프라인 (가로, 임팩트형)

```
A striking technical developer-blog hero banner, landscape orientation, wide 16:9 (generate 1536×1024 with generous margins safe for cropping). Deep navy background #0E1A2B with crisp neon-like blue #2D6CDF and green #36B37E line work; flat vector, NOT 3D, no photo. Central motif: a HORIZONTAL pipeline flowing left-to-right in which an artifact passes through 3–4 rounded rectangular "gates"; passed gates glow green #36B37E, one blocked gate accented red #E5484D. The last gate is highlighted and labeled "DIFFERENT MODEL" to convey model-diversity cross-checking. Eight small luminous nodes (the 8 principles) distributed along the rail. Clean engineered feel, high contrast, ample negative space. UPPERCASE English labels only, short, legible white/blue text. Leave a clean quiet area (upper-left or top band) for a title overlay. No photographic textures, no heavy gradients.
```
글자 없이 옵션: 라벨 문장 제거하고 `Omit text labels; leave a clean empty band at the top for later title overlay.` 추가.

---

## 변형 3 — 빈 레포 → 구조 (채택 표지와 동일 모티프, 가로 배너)

> 채택 표지(`cover-empty-to-structured.png`)의 chaos→order 모티프를 **가로 배너로 재구성**. 표지와 같은 룩을 원하면 그 표지를 첨부하고 아래를 붙여넣기.

```
A minimal, data-visualization-inspired developer-blog hero banner, landscape orientation, wide 16:9 (generate 1536×1024 with generous margins safe for cropping). Light background #F7F9FC, ink #1B2733 and blue #2D6CDF accents; flat geometric vector, NOT 3D, no photo, lots of whitespace. Concept, read LEFT → RIGHT: on the left, scattered sparse dots (an empty git repository, chaos); flowing rightward they organize into an ordered grid / layered architecture that converges into clean structure — depicting growth "from an empty repo to a million lines". Keep the densest, most ordered structure on the right. Elegant, restrained, geometric. Reserve a clean quiet area on the upper portion (away from the dense structure) for a title overlay. Crisp legible UPPERCASE English mini-labels at most (e.g., "EMPTY REPO" left, "STRUCTURED" right); no Korean text, no photographic elements, no busy gradients.
```
글자 없이 옵션: 라벨 문장 빼고 `Reserve a clean upper band for title text to be added later; no in-art labels.` 추가.

---

## 변형 4 — 타이포 히어로 (OG 카드 / 미니멀)

> 소셜 공유 카드(1.91:1, 1200×630)나 텍스트 중심 썸네일용. 타이포가 디자인의 핵심.

```
A minimalist typographic developer-blog social card, landscape orientation, wide ~1.91:1 (generate 1536×1024 with generous side margins safe for cropping to 1200×630). Very light background #F7F9FC, ink text #1B2733, a single blue accent #2D6CDF; flat, no photo, no 3D. The card is almost pure typography on the left two-thirds: a small kicker line "8원칙으로 살펴보는" above a very large main title "하네스 엔지니어링" (one accented syllable in blue), with a smaller line "8원칙 + 4가지 패턴" below. On the right third, a subtle low-contrast motif: a faint pair of parallel guide-rails (a "harness/guide rail") gently curving, plus eight tiny dots along an arc — very low contrast, never overlapping the text. Restrained, premium, modern O'Reilly feel; perfectly legible typography; generous whitespace; no clutter.
```
글자 없이 옵션: 타이포가 핵심이라 비권장. 배경만 원하면 `Only the faint curved parallel guide-rails and eight tiny dots on a light #F7F9FC background, no text.`

---

### 생성 팁
- **일관성 1순위:** 첫 컷을 뽑은 뒤 이어지는 변형엔 프롬프트 끝에 `Use the exact same style, palette, and stroke weight as the previous image.` 한 줄을 추가. 책 룩과 붙이려면 기존 표지/다이어그램 렌더를 **첨부**하고 "match the attached image's style exactly"를 맨 앞에 추가.
- **크롭 마감:** 1536×1024로 생성 → 히어로는 16:9(예: 1536×864), OG 카드는 1.91:1(1200×630)로 좌우/상하 크롭. "generous margins" 덕에 크롭해도 구도가 살아야 정상.
- **한글이 깨지면:** (1) 같은 프롬프트로 1~2회 재생성, (2) 그래도 깨지면 "글자 없이"로 배경만 뽑고 제목·후크는 Figma/Canva에서 얹기. 키커("8원칙으로 살펴보는")는 작아서 가장 잘 깨짐 — 후보정 1순위.
- 결정론 원칙(ADR 0004)상 이 배너는 **홍보·썸네일용 생성 래스터**다(본문 다이어그램의 SVG 소스 규칙과 별개). 최종 채택본은 `assets/`에 저장해 보관.
