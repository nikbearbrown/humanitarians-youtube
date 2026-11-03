#!/usr/bin/env python3
"""Portrait gate on the PIXELS of rendered 9:16 stills (PROOF-REVIEW-2, Do X #1).

Documents can't see this class of defect (BEATS.md, governing observation), so it reads frames:

  ZONE  text ink below 75% of the height (YouTube Shorts' caption/title/buttons) or above 12% (top bar)
  CLIP  text ink flush against a card's bottom edge: the card cut its own last line off.
        PARTIAL by nature: a line hidden entirely below the edge leaves no pixels to read, and the
        edge must be a mostly-white row (so compressed frames don't false-positive). It catches B11,
        not B18/B20. ZONE is the real portrait gate: every card frame fails ZONE anyway.

"Ink" = pixels close to the palette's text colours (INK, INK_SOFT, SPARK). Card edges are found as the
white card surface meeting the cream page in the centre column. Exit 1 on any failure.

  python3 portrait_check.py _stills/*-9x16.png          # report
  python3 portrait_check.py short/_stills/*.png          # gate for the Short
"""
import sys
from pathlib import Path

from PIL import Image

TEXT = [(0x3D, 0x39, 0x29), (0x73, 0x70, 0x5F), (0xD9, 0x77, 0x57), (0xA9, 0xA4, 0x91)]  # INK, INK_SOFT, SPARK, GHOST
CARD, PAGE = (255, 255, 255), (0xFA, 0xF9, 0xF5)
TOP, BOTTOM = 0.12, 0.75
CLIP_BAND = 14          # px above a card's bottom edge that must be free of text (1080-wide frames)


def near(px, ref, tol):
    return all(abs(a - b) <= tol for a, b in zip(px, ref))


def check(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    px = im.load()
    ink_rows = []
    for y in range(0, h, 2):
        if any(any(near(px[x, y], c, 40) for c in TEXT) for x in range(int(w * 0.04), int(w * 0.96), 3)):
            ink_rows.append(y)
    out = []
    if ink_rows:
        lo, hi = max(ink_rows), min(ink_rows)
        if lo > h * BOTTOM:
            out.append(f"ZONE text down to {lo / h:.0%} of height (limit {BOTTOM:.0%})")
        if hi < h * TOP:
            out.append(f"ZONE text up to {hi / h:.0%} of height (limit {TOP:.0%})")
    # the lowest card's bottom edge: scan UP from the bottom, along a margin column inside the card
    # (x = 8% of width avoids text), to the first white card pixel
    # a card edge counts only if most of that row is card-white (a stray near-white pixel in a compressed
    # frame or a non-card beat is not a card: that false-positived 29/31 master frames, W26 Short v2)
    def card_row(y):
        xs = range(int(w * 0.08), int(w * 0.92), 6)
        return sum(near(px[x, y], CARD, 6) for x in xs) >= 0.6 * len(xs)
    edge = next((y for y in range(h - 1, 0, -1) if card_row(y)), None)
    if edge is not None and edge < h - 2:
        band = range(max(0, edge - CLIP_BAND), edge)
        if any(any(near(px[x, yy], c, 40) for c in TEXT[:2]) for yy in band
               for x in range(int(w * 0.06), int(w * 0.94), 2)):
            out.append(f"CLIP text flush against the card's bottom edge at {edge / h:.0%} of height")
    return out


def main(paths):
    fails = 0
    for p in sorted(paths):
        res = check(p)
        fails += bool(res)
        print(f"{Path(p).name:22} {'OK' if not res else ' · '.join(res)}")
    print(f"\n{fails} of {len(paths)} portrait frames fail")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
