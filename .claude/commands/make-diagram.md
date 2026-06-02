---
description: 개념 다이어그램을 SVG로 작성하고 PNG로 렌더한다
argument-hint: <slug> "<다이어그램 설명>" (예: ch15-factor12-stateless-reducer "f(events)→next_action")
---

`$ARGUMENTS`의 개념 다이어그램을 만든다. **AI 래스터 이미지로 생성하지 않는다** — SVG를 코드로 작성한다(재현·diff 가능).

절차:
1. `docs/conventions.md` §8의 **하우스 스타일**(배경 #F7F9FC, 잉크 #1B2733, 파랑 #2D6CDF, 초록 테두리 #36B37E, 안티패턴 빨강 #E5484D, 폰트 `Apple SD Gothic Neo` + 코드 라벨 monospace)을 따른다.
2. `assets/diagrams/<slug>/NN-이름.svg`로 저장. 개발자 친화 — 에이전트 루프/상태/reducer 같은 흐름은 코드·의사코드 라벨 허용, 한글 우선(영문 병기).
3. 렌더:
   ```bash
   python3 scripts/render_images.py <slug>
   ```
4. 생성된 `assets/screenshots/<slug>/NN-이름.png`를 **Read로 열어 눈으로 검수**한다(한글 글리프 깨짐·텍스트 잘림·정렬). 문제 있으면 SVG를 고치고 재렌더.
5. 본문(`manuscript/<slug>.md`)에서 해당 이미지를 참조한다. 실제 업로드는 `/publish-chapter`가 처리.
