# 위키독스 출판 런북 (wikidocs MCP)

> 로컬 `manuscript/*.md`(SoT) → wikidocs 로 올리는 **재현 가능한** 절차.
> 위키독스 계층: **부(part) > 장(chapter) > 절(section)**. 명시적 순서 파라미터 없음 → **생성 순서 = 표시 순서**.

---

## 사전 점검

```bash
python3 scripts/verify.py          # 원고 규약·사실·링크 검증 (실패 시 push 금지)
python3 scripts/status.py          # 현재 진행 상태 표
```

`status`가 `reviewed`인 장만 push 대상. `verify` 통과가 push의 전제 조건이다(여기엔 codex 교차검증 강제가 포함).

---

## 1단계 — 책 생성 (최초 1회)

```
mcp__wikidocs__create_book(subject, summary, open_yn="N")  →  book_id
```

- `subject`/`summary`/`open_yn` 값은 `docs/toc.json`의 `book` 블록 사용
  (subject = "8원칙으로 살펴보는 하네스 엔지니어링 — 에이전트가 일하는 코드베이스 만들기").
- 받은 `book_id`를 `docs/toc.json`의 `wikidocs_book_id`에 기록 + 커밋.
- **초안은 비공개(`open_yn="N"`)**. 완성 후 마지막에 공개 전환.

## 2단계 — 부(part) 페이지 생성

`docs/toc.json`의 parts를 **순서대로**:

```
mcp__wikidocs__create_page(book_id, subject="1부. 하네스 엔지니어링 입문", content="<부 소개>")  # parent_id 생략 = 최상위
```

- 받은 page_id를 해당 부 하위 모든 장의 front-matter `parent_page_id`에 기록.

## 3단계 — 장(chapter) 페이지 생성·갱신

각 `reviewed` 장에 대해:

- 신규: `create_page(book_id, subject=title, content=<본문>, parent_id=<부 page_id>)` → page_id 받음
- 기존(재push): `update_page(page_id, subject, content)`
- front-matter에 `wikidocs_page_id` 기록, `status: published`로 갱신, 커밋.

> 본문 content는 manuscript의 front-matter를 **제외한** 마크다운 본문만.

## 4단계 — 이미지 삽입

```
mcp__wikidocs__upload_page_image(page_id, <assets/screenshots/<slug>/*.png>)
```

업로드가 돌려준 URL을 본문 마크다운 이미지 링크로 치환 후 `update_page`.

## 5단계 — 구조 검증

```
mcp__wikidocs__get_book_toc(book_id)
```

- `docs/toc.json` 순서와 일치하는지 대조.
- 이동/수정: `update_page(page_id, parent_id=...)` (`parent_id=-1` = 최상위로).

## 6단계 — 공개 전환 (전체 완성 후)

모든 장 `published` + 전체 검수 완료 시 책/페이지를 공개로 전환.

---

## 멱등성·재개 규칙

- page_id는 **front-matter에만** 기록 → 세션이 끊겨도 `status.py`로 어디까지 했는지 즉시 복원. (Factor 6·12)
- 같은 장을 다시 올릴 땐 `create`가 아니라 `update_page`(page_id 존재 시). 중복 페이지 생성 금지.
- toc.json의 `wikidocs_book_id`가 채워져 있으면 1단계 건너뛴다.

## 빠른 참조 — MCP 도구

| 작업 | 도구 |
|---|---|
| 책 생성 | `mcp__wikidocs__create_book` |
| 목차 조회 | `mcp__wikidocs__get_book_toc` |
| 페이지 생성 | `mcp__wikidocs__create_page` |
| 페이지 수정/이동 | `mcp__wikidocs__update_page` |
| 페이지 본문 조회 | `mcp__wikidocs__get_page` |
| 이미지 업로드 | `mcp__wikidocs__upload_page_image` |
| 책 목록 | `mcp__wikidocs__list_books` |
