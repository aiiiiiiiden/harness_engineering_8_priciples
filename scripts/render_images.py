#!/usr/bin/env python3
"""다이어그램 렌더 — assets/diagrams/<slug>/*.svg → assets/screenshots/<slug>/*.png

다이어그램은 '코드(SVG)'가 진실의 원천이다. PNG는 파생물 → 발행 직전 재생성한다.
이렇게 하면 다이어그램이 diff·재현 가능하고, 31장 전체에서 일관된 스타일을 강제할 수 있다.

신뢰성: rsvg-convert(결정론적 렌더) 사용. 2배 해상도(@2x)로 선명하게.
PNG는 스크린샷과 같은 폴더에 모여 발행 시 한 번에 업로드된다.

사용:
    python3 scripts/render_images.py            # 변경된 SVG만 렌더
    python3 scripts/render_images.py --all      # 전부 다시 렌더
    python3 scripts/render_images.py <slug>     # 특정 장만
"""
from __future__ import annotations
import os
import shutil
import subprocess
import sys

from _harness import ROOT

DIAGRAMS_DIR = os.path.join(ROOT, "assets", "diagrams")
OUT_BASE = os.path.join(ROOT, "assets", "screenshots")
SCALE = 2  # @2x


def needs_render(svg: str, png: str, force: bool) -> bool:
    if force or not os.path.exists(png):
        return True
    return os.path.getmtime(svg) > os.path.getmtime(png)


def main():
    if not shutil.which("rsvg-convert"):
        sys.exit("rsvg-convert 가 필요합니다: brew install librsvg")
    force = "--all" in sys.argv
    slug_filter = next((a for a in sys.argv[1:] if not a.startswith("--")), None)

    if not os.path.isdir(DIAGRAMS_DIR):
        print(f"다이어그램 소스 없음: {os.path.relpath(DIAGRAMS_DIR)} (assets/diagrams/<slug>/*.svg 에 SVG를 둬라)")
        return

    rendered, skipped = 0, 0
    for slug in sorted(os.listdir(DIAGRAMS_DIR)):
        src_dir = os.path.join(DIAGRAMS_DIR, slug)
        if not os.path.isdir(src_dir):
            continue
        if slug_filter and slug != slug_filter:
            continue
        out_dir = os.path.join(OUT_BASE, slug)
        os.makedirs(out_dir, exist_ok=True)
        for name in sorted(os.listdir(src_dir)):
            if not name.endswith(".svg"):
                continue
            svg = os.path.join(src_dir, name)
            png = os.path.join(out_dir, name[:-4] + ".png")
            if not needs_render(svg, png, force):
                skipped += 1
                continue
            subprocess.run(["rsvg-convert", "-z", str(SCALE), svg, "-o", png], check=True)
            print(f"[rendered] {os.path.relpath(png)}")
            rendered += 1
    print(f"\n렌더 {rendered} · 최신유지 {skipped}")


if __name__ == "__main__":
    main()
