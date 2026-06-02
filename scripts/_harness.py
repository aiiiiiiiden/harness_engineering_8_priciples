"""하네스 공통 헬퍼 — stdlib만 사용 (의존성 zero).

front-matter 파서는 이 프로젝트가 쓰는 부분집합만 지원한다:
  - key: scalar  (int / "quoted" / null / bare 문자열)
  - key:
      - 리스트 아이템 (문자열 스칼라)
"""
from __future__ import annotations
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSCRIPT_DIR = os.path.join(ROOT, "manuscript")
TOC_PATH = os.path.join(ROOT, "docs", "toc.json")


def load_toc():
    with open(TOC_PATH, encoding="utf-8") as f:
        return json.load(f)


def iter_toc_chapters(toc):
    """(part_dict, chapter_dict) 튜플을 toc 순서대로 산출."""
    for part in toc["parts"]:
        for ch in part["chapters"]:
            yield part, ch


def _coerce(value: str):
    v = value.strip()
    if v in ("null", "~", ""):
        return None
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def parse_front_matter(text: str):
    """마크다운 텍스트에서 (front_matter_dict, body) 반환. front-matter 없으면 ({}, text)."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    block, body = m.group(1), m.group(2)
    data = {}
    current_list_key = None
    for raw in block.splitlines():
        if not raw.strip():
            continue
        list_item = re.match(r"^\s+-\s+(.*)$", raw)
        if list_item and current_list_key is not None:
            data[current_list_key].append(_coerce(list_item.group(1)))
            continue
        kv = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", raw)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2)
        if val.strip() == "":
            data[key] = []
            current_list_key = key
        else:
            data[key] = _coerce(val)
            current_list_key = None
    return data, body


def set_front_matter_key(text: str, key: str, value) -> str:
    """front-matter 블록에서 `key:` 스칼라를 value로 교체(없으면 닫는 --- 앞에 삽입).
    본문은 보존한다. 스크립트가 검증 결과를 원고에 도장 찍을 때 사용."""
    val_str = "null" if value is None else (f'"{value}"' if isinstance(value, str) else str(value))
    m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n?)(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError("front-matter 없음")
    head, block, close, body = m.groups()
    line = f"{key}: {val_str}"
    if re.search(rf"^{re.escape(key)}:.*$", block, re.MULTILINE):
        block = re.sub(rf"^{re.escape(key)}:.*$", line, block, count=1, flags=re.MULTILINE)
    else:
        block = block + "\n" + line
    return head + block + close + body


def chapter_path(slug: str) -> str:
    return os.path.join(MANUSCRIPT_DIR, f"{slug}.md")


def iter_manuscript_files():
    if not os.path.isdir(MANUSCRIPT_DIR):
        return
    for name in sorted(os.listdir(MANUSCRIPT_DIR)):
        if name.endswith(".md") and not name.startswith("_"):
            path = os.path.join(MANUSCRIPT_DIR, name)
            with open(path, encoding="utf-8") as f:
                yield path, f.read()
