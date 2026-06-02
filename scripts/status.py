#!/usr/bin/env python3
"""집필 진행 상태 표 — '지금 어디까지 했나'를 즉시 보여준다 (Observability).

front-matter의 status/page_id를 toc.json 순서대로 스캔.
사용: python3 scripts/status.py
"""
from __future__ import annotations
import os

from _harness import (chapter_path, iter_toc_chapters, load_toc,
                      parse_front_matter)

ICON = {"skeleton": "·", "draft": "✎", "reviewed": "✓", "published": "★", "missing": "✗"}
ORDER = ["skeleton", "draft", "reviewed", "published"]


def main():
    toc = load_toc()
    counts = {k: 0 for k in ORDER}
    missing = 0
    rows = []
    cur_part = None
    for part, ch in iter_toc_chapters(toc):
        label = "부록" if part.get("is_appendix") else f"{part['part']}부"
        if label != cur_part:
            rows.append(("PART", f"{label}. {part['title']}"))
            cur_part = label
        path = chapter_path(ch["slug"])
        if not os.path.exists(path):
            rows.append(("CH", f"  {ICON['missing']} [{ch['chapter']}] {ch['title']}  (파일 없음)"))
            missing += 1
            continue
        with open(path, encoding="utf-8") as f:
            fm, _ = parse_front_matter(f.read())
        st = fm.get("status", "skeleton")
        if st in counts:
            counts[st] += 1
        pid = fm.get("wikidocs_page_id")
        tag = f"  page_id={pid}" if pid else ""
        rows.append(("CH", f"  {ICON.get(st, '?')} [{ch['chapter']}] {ch['title']}  <{st}>{tag}"))

    print(f"\n📖 {toc['book']['subject']}  (book_id={toc['book'].get('wikidocs_book_id')})\n")
    for kind, line in rows:
        print(line if kind == "CH" else f"\n■ {line}")

    total = sum(counts.values()) + missing
    print("\n" + "─" * 40)
    summary = "  ".join(f"{ICON[k]} {k} {counts[k]}" for k in ORDER)
    print(f"합계 {total}장   {summary}   ✗ missing {missing}")
    done = counts["published"]
    if total:
        print(f"출판 진척: {done}/{total} ({done * 100 // total}%)")


if __name__ == "__main__":
    main()
