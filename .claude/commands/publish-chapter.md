---
description: reviewed 상태인 장을 위키독스에 올린다
argument-hint: <slug> (생략 시 reviewed 전체)
---

`docs/publishing-runbook.md`를 따라 `$ARGUMENTS`(또는 status=reviewed인 모든 장)를 위키독스에 올린다.

전제: `python3 scripts/verify.py`가 PASS여야 한다(여기엔 **codex 교차검증 강제**가 포함된다 — reviewed/published인데 `crosscheck != pass`면 verify가 FAIL). 실패 시 중단하고 원인을 보고한다.

핵심 규칙:
- `docs/toc.json`의 `wikidocs_book_id`가 null이면 먼저 `create_book`(open_yn="N") → book_id를 toc.json에 기록.
- 부(part) 페이지가 없으면 toc 순서대로 생성 → 각 장 front-matter `parent_page_id`에 기록.
- 장: front-matter에 `wikidocs_page_id`가 있으면 `update_page`, 없으면 `create_page`(parent_id=부 page_id). **중복 생성 금지**.
- 올린 본문은 front-matter를 제외한 마크다운 본문만.
- 이미지는 `upload_page_image` 후 URL로 치환.
- push 성공 시 front-matter `wikidocs_page_id` 기록 + `status: published`.
- 마지막에 `get_book_toc`로 toc.json 순서와 일치하는지 검증.
