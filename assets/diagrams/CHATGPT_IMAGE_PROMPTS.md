# ChatGPT 이미지 생성용 프롬프트 — 본문 다이어그램 17개

> 이 책의 17개 개념 다이어그램(`assets/diagrams/<slug>/01-*.svg`)을 ChatGPT(DALL·E / GPT-image)로 만들 때 쓰는 프롬프트. **각 장의 코드블록 하나가 그 자체로 완결**이라, 통째로 복사해 붙여넣으면 된다(스타일 프리앰블이 안에 이미 들어 있음).
>
> **정본 이미지는 여전히 SVG다.** 프로젝트 규칙(Rule 4)상 본문 다이어그램은 결정론적 SVG가 진실의 원천이고 AI 래스터는 금지. 이 산출물은 **슬라이드·홍보·썸네일·변형 탐색용** 대체본이다.
>
> **한글 렌더 한계.** 이미지 생성기는 한글을 자주 깨뜨린다. 그래서 라벨은 표지 모티프대로 **대문자 영문**으로 통일했다. 한글이 꼭 필요하면 영문으로 뽑은 뒤 텍스트만 Figma/Keynote로 덧입히길 권장. 각 블록 위 `원본:` 줄은 한글 의미 참고용(복사 대상 아님).

**연속 생성 팁:** 두 번째 장부터는 프롬프트 끝에 `Use the exact same style, palette, and stroke weight as the previous image.` 한 줄을 더 붙이면 17장 룩이 더 잘 붙는다.

---

### 1. ch01 — 하네스가 에이전트를 감싼다
원본: 코딩 에이전트를 중심에 두고 기록 시스템(P3·4)·기계적 불변식(P5)·관측성(P2)·피드백 루프(P1·7·8)가 둘레를 감싸는 환경이 하네스다.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A central white rounded node "CODING AGENT" with a tiny inner caption "ONE MODEL CALL". Four labeled satellite blocks form a ring that ENCLOSES the center, each with a thin arrow pointing inward: SYSTEM OF RECORD (docs · schema · plans), MECHANICAL INVARIANTS (linters · structural tests), OBSERVABILITY (logs · metrics · screens), FEEDBACK LOOP (run · verify · self-fix). A thin outer halo around the whole ring conveys "everything around the agent is the harness." Title: "THE HARNESS WRAPS THE AGENT".
```

### 2. ch02 — 프롬프트로 때우기 vs 환경을 고치기
원본: 같은 증상(에이전트가 매번 인증 로직을 제멋대로 재구현)에 두 반응 — 프롬프트 때우기는 반짝 통과 후 재발, 환경 고치기는 docs 기록(P3)+구조 테스트(P5)로 영구 적용.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A two-column comparison split by a thin vertical divider, with one shared symptom across the top: "AGENT RE-IMPLEMENTS AUTH ITS OWN WAY". Left column (muted) titled "PATCH THE PROMPT": one arrow passes once, then a small red #E5484D dashed loop returns to the same mistake, labeled "RECURS NEXT SESSION". Right column (blue, solid) titled "FIX THE ENVIRONMENT": symptom -> "RECORD DECISION IN docs/ (P3)" -> "BLOCK WITH STRUCTURAL TEST (P5)" -> green #36B37E check "PERMANENT FOR ALL FUTURE RUNS". Title: "PROMPT vs ENVIRONMENT".
```

### 3. ch03 — 하네스의 다섯 부품
원본: 하네스를 다섯 부품으로 해부 — 진입점·맵(P3), 기록시스템(P3·4), 기계적 강제(P5), 관측성(P2), 피드백 루프(P1·7·8). P6은 부품 가로지르는 운영정책. 하단 띠 L1→L5.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: Five white rounded component blocks in an exploded "anatomy" layout, each with a small "(Pn)" tag: 1 ENTRYPOINT & MAP (P3), 2 SYSTEM OF RECORD (P3·P4), 3 MECHANICAL ENFORCEMENT (P5), 4 OBSERVABILITY (P2), 5 FEEDBACK LOOP (P1·P7·P8). A thin horizontal ribbon crosses the parts labeled "MERGE POLICY (P6) — CROSS-CUTTING". At the bottom, a maturity ribbon with a dashed connector: "FROM AN EMPTY REPO (L1) ┄▶ INTERLOCKED AUTONOMY (L5)". Title: "ANATOMY OF A HARNESS — FIVE PARTS".
```

### 4. ch04 — 사람은 조종, 에이전트는 실행
원본: 사람은 조종(우선순위·의도를 수용기준으로 번역·검증), 에이전트는 실행(코드 작성). 수용기준→실행→검증결과 루프. 사람이 실행으로 내려가면 그 지점이 병목.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: Two roles facing each other with a clean clockwise loop. Left node "HUMAN — STEER" with three stacked micro-labels: SET PRIORITIES / TRANSLATE INTENT -> ACCEPTANCE CRITERIA / VERIFY RESULTS. Right node "AGENT — EXECUTE" with micro-label WRITE CODE. Top arrow (human -> agent) labeled "ACCEPTANCE CRITERIA"; bottom arrow (agent -> human) labeled "VERIFICATION RESULTS". A red #E5484D dashed arrow drags the human DOWN into the execute side, marked "HUMAN DROPS TO EXECUTE = THROUGHPUT BOTTLENECK". Title: "HUMANS STEER, AGENTS EXECUTE".
```

### 5. ch05 — 에이전트의 눈 (자가 검증 루프)
원본: 에이전트가 boot.sh로 앱 부팅→통합테스트→로그(LogQL)·메트릭(PromQL)·스크린샷(CDP) 읽어 판정. 실패하면 로그 읽고 고쳐 다시. 앱 내부가 노출돼야 추측이 검증.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A closed clockwise self-verification loop of white nodes joined by thin blue arrows: BOOT APP (boot.sh) -> RUN INTEGRATION TESTS -> READ SIGNALS -> JUDGE. "READ SIGNALS" fans into three small eye-like chips: LOGS (LogQL), METRICS (PromQL), SCREENSHOT (CDP). From JUDGE, a green #36B37E arrow "PASS" exits; a red #E5484D arrow "FAIL -> READ LOGS & FIX" routes back to BOOT APP. Subtitle: "IF YOU CAN'T VERIFY IT, YOU DIDN'T FIX IT". Title: "GIVE THE AGENT EYES".
```

### 6. ch06 — 맵이지 매뉴얼이 아니다
원본: 왼쪽 거대 단일 AGENTS.md(매뉴얼)는 낡은 규칙 뒤섞여 컨텍스트 밀어내고 드리프트. 오른쪽 짧은 맵(~100줄)이 구조화된 docs/(design-docs·exec-plans·references) 가리키고 필요한 깊이로만 진입.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: Two-column contrast. Left (muted, red-tinged) titled "MANUAL": one huge overstuffed document block "AGENTS.md — EVERYTHING" crammed with faint mixed/old rules, tagged red #E5484D "STALE RULES · DRIFT · BLOWS THE CONTEXT". Right (blue, clean) titled "MAP": a slim block "AGENTS.md (~100 LINES)" with thin arrows pointing out to a structured tree docs/ { DESIGN-DOCS, EXEC-PLANS, REFERENCES }; a reader arrow descends "ONLY AS DEEP AS NEEDED" (progressive disclosure). Title: "A MAP, NOT A MANUAL".
```

### 7. ch07 — 에이전트 가독성 최적화
원본: 같은 결정('소프트 삭제')이 Slack/머릿속에만 있으면(가독성 낮음) 에이전트가 물리삭제→데이터 소실. docs(P3)+구조테스트(P5)+버전 스키마면(가독성 높음) 코드·스키마·문서로 규칙 추론.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: The same decision "SOFT DELETE — NEVER HARD DELETE" routed two ways. Top path "LOW LEGIBILITY": decision lives only in faint chat bubbles "SLACK / IN SOMEONE'S HEAD" -> agent -> red #E5484D outcome "WRITES HARD DELETE -> DATA LOST". Bottom path "HIGH LEGIBILITY": same decision encoded into three white blocks DOCS (P3) · STRUCTURAL TEST (P5) · VERSIONED SCHEMA -> agent reads code+schema+docs -> green #36B37E outcome "INFERS THE RULE CORRECTLY". Title: "OPTIMIZE FOR AGENT LEGIBILITY".
```

### 8. ch08 — 계층 강제
원본: 각 도메인은 한 방향 계층(Types→Config→Repo→Service→Runtime→UI). 교차관심사(인증·텔레메트리·플래그)는 Providers 단일 인터페이스로만 유입. 허용 안 된 에지(UI→Repo 직접)는 린터·구조테스트가 빌드에서 차단.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A vertical one-directional layer stack of thin outlined bands, arrows flowing one way only: TYPES -> CONFIG -> REPO -> SERVICE -> RUNTIME -> UI. On the side, a single vertical interface column "PROVIDERS" feeds cross-cutting concerns (AUTH · TELEMETRY · FEATURE FLAGS) into the stack through ONE entry only. Draw one illegal shortcut edge "UI -> REPO (DIRECT)" crossed out with a red #E5484D X tagged "BLOCKED AT BUILD BY LINTER / STRUCTURAL TEST". Title: "ENFORCE ARCHITECTURE IN THE BUILD".
```

### 9. ch09 — 처리량과 병합 철학
원본: 사람속도 기본값은 모든 PR 사람승인+단발 플래키 무기한 차단→PR 줄섬. 처리량정책(P6)은 짧은 PR·빠른 병합·필요시만 승인·불변식만 차단하는 최소 게이트.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: Two-column policy comparison, each showing small PR chips flowing toward a merge gate. Left "HUMAN-SPEED DEFAULT": many PR chips QUEUE in a long line behind a heavy gate; tags "EVERY PR NEEDS HUMAN APPROVAL" and red #E5484D "ONE FLAKY TEST BLOCKS FOREVER" (a traffic jam). Right "THROUGHPUT POLICY (P6)": PR chips flow through a minimal gate quickly with green #36B37E flow; tags "SHORT-LIVED PRs · MERGE FAST", "HUMAN APPROVES ONLY WHEN NEEDED", and one firm block "INVARIANTS STILL BLOCK (P5)". Title: "THROUGHPUT RESHAPES MERGE".
```

### 10. ch10 — 자율 루프 인코딩
원본: 한 프롬프트가 닫힌 루프 — 상태검증→버그재현→수정→앱 실행검증(P2)→PR→피드백 응답→빌드실패 감지·수정. 판단 필요시만 사람 에스컬레이션(P1), 통과하면 병합.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A large closed clockwise loop of small white step-nodes joined by thin blue arrows: VERIFY STATE -> REPRODUCE BUG -> IMPLEMENT FIX -> RUN & VERIFY APP (P2) -> OPEN PR -> RESPOND TO FEEDBACK -> DETECT BUILD FAILURE & FIX -> back to start. One branch arrow leaves the loop upward only "WHEN JUDGMENT NEEDED -> ESCALATE TO HUMAN (P1)"; a green #36B37E arrow exits "PASS -> MERGE". Caption: "ENCODED VERIFY & RECOVERY STEPS KEEP THE LOOP UNBROKEN". Title: "ENCODE THE AUTONOMY LOOP".
```

### 11. ch11 — 엔트로피와 가비지 컬렉션
원본: 위쪽은 패턴 복제로 명명표류·죽은코드·문서불일치 번지는 엔트로피. 아래쪽은 두 장치 — 황금원칙(리포 인코딩) + 편차스캔→품질등급→리팩터PR→자동병합 GC 루프. 금요일 수동청소(주20%)는 확장 안 됨.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: Top half "ENTROPY" — an agent duplicating patterns, spreading faint red #E5484D spots labeled NAMING DRIFT · DEAD CODE · DOC MISMATCH creeping outward. Bottom half "GARBAGE COLLECTION" — two clean blue mechanisms sweeping it up: (1) a block "GOLDEN PRINCIPLES (ENCODED IN REPO)", (2) a continuous loop SCAN DEVIATION -> UPDATE QUALITY GRADE -> SMALL REFACTOR PR -> AUTO-MERGE. A small crossed-out muted-red note "FRIDAY MANUAL CLEANUP (20% OF WEEK) — DOES NOT SCALE". Title: "GARBAGE-COLLECT ENTROPY".
```

### 12. ch12 — 진실의 원천 흐름
원본: 권위 있는 한 곳(SoT)에 사실 두고 파생물(문서·페이지·본문인용)은 거기서 생성/가리킴. 단방향(SoT→파생), 사람은 파생 직접 안 고침, 어긋남은 기계 점검, 고칠 땐 SoT 먼저.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: One authoritative white block on the left labeled "SOURCE OF TRUTH (SoT)". One-directional thin blue arrows fan out to derived artifacts on the right: DOCS · PAGE · QUOTE-IN-BODY, each marked "DERIVED — GENERATED / POINTS BACK". A small machine/check icon spans the arrows labeled "MACHINE CHECKS DERIVED == SoT". A human figure tries to edit a derived artifact directly but is blocked with a red #E5484D "DON'T EDIT DERIVED"; instead a green #36B37E arrow "FIX SoT FIRST -> DERIVED FOLLOWS". Title: "SINGLE SOURCE OF TRUTH".
```

### 13. ch13 — 검증 게이트와 모델 다양성
원본: 산출물이 게이트1 기계검사(스키마·규칙·링크, 결정론, P5)→게이트2 의미검사(같은 모델)→게이트3 독립검사(다른 모델 교차검증, 모델 다양성) 직렬 통과. 셋 합의해야 통과, 하나라도 실패하면 차단.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: An artifact chip passes through THREE gates in series left to right, thin blue flow, each gate a thin vertical bar: GATE 1 — MECHANICAL CHECK (schema · rules · links · deterministic, P5), GATE 2 — SEMANTIC REVIEW (same model, deep read), GATE 3 — INDEPENDENT CHECK (different model cross-verifies facts — MODEL DIVERSITY). A green #36B37E "PASS" continues only when all three agree; show a red #E5484D "BLOCKED HERE" stop wherever a gate fails. Title: "THREE GATES MUST AGREE".
```

### 14. ch14 — 결정론적 산출물 파이프라인
원본: 소스(코드, SoT)→결정론적 생성기→산출물(파생, 재생성 가능). diagram.svg→png, schema.sql→types.ts, openapi.yaml→SDK. CI가 재생성본↔커밋본 diff(P5), 일치 통과/불일치 차단.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A horizontal pipeline: SOURCE (code · SoT) -> DETERMINISTIC GENERATOR (a gear/box) -> ARTIFACT (derived · regenerable). Three stacked concrete example rows in monospace micro-labels: "diagram.svg > render > png", "schema.sql > codegen > types.ts", "openapi.yaml > gen > sdk". Below, a CI node diffs "REGENERATED" vs "COMMITTED": green #36B37E "MATCH -> PASS" vs red #E5484D "MISMATCH -> BLOCK (P5)". Title: "DETERMINISTIC ARTIFACTS — CODE IS THE SOURCE OF TRUTH".
```

### 15. ch15 — 멀티 에이전트 오케스트레이션
원본: 오케스트레이터가 작업 분해→격리 컨텍스트·제한 도구 서브에이전트 A·B·C로 병렬 팬아웃→합류·중재. 직렬 파이프라인은 탐지→변환→검증→게이트통과? 흐르고 실패시 루프(P7) 회귀. 출력 요약만 전달.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: Top — a fan-out topology: an "ORCHESTRATOR" node DECOMPOSES work and branches to three parallel white sub-agent nodes "SUB-AGENT A / B / C" (each tagged "ISOLATED CONTEXT · LIMITED TOOLS"), then they JOIN back into a "MERGE / ARBITRATE" node. Bottom — a serial pipeline lane: DETECT -> TRANSFORM -> VERIFY -> GATE PASS? with a green #36B37E "PASS" forward and a red #E5484D "FAIL -> LOOP BACK (P7)" return arrow. Small note "ONLY OUTPUT SUMMARY PASSES DOWNSTREAM". Title: "MULTI-AGENT ORCHESTRATION".
```

### 16. ch16 — 골든 워크플로우
원본: 구조 SoT toc.json→scaffold.py 골격 결정론 생성→draft가 4중 게이트(verify.py 기계·md-doc-reviewer·crosscheck.py codex 독립모델·humanize 문체) 모두 통과해야 reviewed→위키독스 발행. 하나라도 실패하면 차단.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A left-to-right golden workflow: "toc.json (STRUCTURE SoT)" -> "scaffold.py -> MANUSCRIPT SKELETON (deterministic)" -> "DRAFT" -> a stacked FOUR-GATE column that all must pass: G1 verify.py (MECHANICAL), G2 md-doc-reviewer (SAME MODEL), G3 crosscheck.py (CODEX — INDEPENDENT MODEL), G4 humanize (STYLE) -> green #36B37E "REVIEWED" -> "PUBLISH TO WIKIDOCS". Any gate failing shows a red #E5484D "BLOCKED" stop. Title: "THE GOLDEN WORKFLOW".
```

### 17. ch17 — 성숙도 사다리 (L1→L5)
원본: L1 없음(빈 레포)→L2 문서화(강제 없음)→L3 구조화(SoT·맵·스크립트, 수동점검)→L4 강제(게이트 코드 차단)→L5 자율(게이트 루프 인코딩·모델다양성·엔트로피 자동GC). 문서 위 구조, 구조 위 강제, 그 위 자율.
```
Flat vector technical infographic, modern and minimal, airy white space, NOT 3D, no photo, clean thin-line style. Palette: background #F7F9FC, ink text #1B2733, muted text #5B6B7A, primary blue #2D6CDF for default boxes and arrows; green #36B37E ONLY for pass/success, red #E5484D ONLY for block/fail. White rounded boxes (radius ~14px, thin 2px borders), delicate thin arrows (2.5–3.5px) with small clean arrowheads (no big filled triangles). UPPERCASE English labels only, short and legible; monospace for code identifiers. Landscape ~1200px, bold centered title.

Scene: A rising staircase of five thin outlined steps ascending left to right, each a labeled band: L1 — NONE (EMPTY REPO), L2 — DOCUMENTED (conventions, no enforcement), L3 — STRUCTURED (SoT · MAP · SCRIPTS, manual checks), L4 — ENFORCED (gates block in code), L5 — AUTONOMOUS (gates encoded in the loop · model diversity · auto-GC of entropy). Convey the stacking: STRUCTURE rests on DOCS, MECHANICAL ENFORCEMENT on STRUCTURE, AUTONOMY LOOP on top. Blue for the climb, a green #36B37E crown at L5. Title: "HARNESS MATURITY LADDER (L1 -> L5)".
```

---

## 한글이 꼭 필요할 때
이미지 생성기는 한글을 거의 못 쓴다. 위 프롬프트로 **영문 라벨 버전을 깔끔히 뽑은 뒤**, 텍스트만 Figma / Keynote / Pages에서 한글로 덧입히는 워크플로우를 권장한다. 정본 다이어그램은 여전히 `assets/diagrams/<slug>/*.svg`이며, 이 산출물은 슬라이드·홍보·변형 탐색용이다.
