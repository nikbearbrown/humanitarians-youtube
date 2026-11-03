#!/usr/bin/env python3
"""make_plates.py — compose the LoonNet prediction sheets into presentation plates.

WHY THIS EXISTS. Two beats in this reel are the author's own evidence: B02, the
full prediction mosaic YOLO prints at validation, and B04, four frames pulled out
of it because they are the four things the model actually does. Neither can be a
straight paste, and neither can take the pipeline's default motion.

1. NO KEN BURNS, NO CENTRE CUT. Same trap as week 09-04-01, same answer. B02's
   argument is the RANGE ACROSS ALL SIXTEEN CELLS — a bird that fills half its
   frame in one, four dark pixels in another. compile.py's zoompan pushes ~8%
   outward and clips the outer cells; shorts.py's centre cut keeps the middle
   37.5% of the width and would throw away columns 1 and 4. So both plates HOLD
   (shot.motion = "hold") and the portrait plate is RE-TILED, not cropped.

2. THE PORTRAIT CELLS ARE PICKED BY MEASUREMENT, NOT BY EYE. In a YOLO mosaic a
   label bar is drawn at its box's top-left and is NOT clipped to the cell, so a
   wide caption runs into the neighbour. That breaks a re-tile in TWO directions,
   and screening for only one of them is the trap: the cell to the right of a
   wide caption inherits an orphaned blue fragment, and the cell that OWNS the
   caption has it sliced mid-word once the neighbour is gone. The first cut of
   this plate screened only for inherited fragments, picked r1c3 and r3c3, and
   both shore frames rendered as "common lo". `--audit` now prints both sets and
   asserts PORTRAIT_CELLS avoids each. In val_batch0_pred.jpg the three column-3
   shore frames bleed right and the three column-4 frames inherit, which spends
   the far end of the scale ramp — those shore frames are the most distant
   subjects in the batch. They are given up rather than shown sliced.

3. THE PORTRAIT PLATE IS A DIFFERENT SHEET AND SAYS SO. Eight of the sixteen
   cells, re-laid 2 wide x 4 tall: the LEFT column is frames where the bird fills
   the picture, the RIGHT column frames where it does not, so the scale argument
   reads as a column contrast on a phone. Eight cells at 2.0x land 960px wide in
   a 2160x3840 plate against ~630px for sixteen cells in the landscape one — the
   portrait cut is the MORE legible of the two, not a degraded fallback.
   DOUBLE-CHECK LAW: it is a subset, so its caption says "8 OF 16 FRAMES,
   RE-TILED" and never implies the whole batch is on screen.

4. B04 IS FOUR PANELS AND ONE OF THEM IS A SUCCESS. The beat is the failure
   audit, and an audit that shows only failures is an argument, not evidence. So
   panel 1 is the drone frame where two birds four pixels across were both found.
   The other three are the duplicate, the vegetation false positive, and the
   fog frame the model returned nothing on. Panel captions name the file, so any
   claim in the narration can be walked back to a frame.

CONFIDENCE FIGURES ARE READ OFF THE PLATE, NOT COMPUTED. Every number the voice
says about a specific frame (0.3, 0.8, 0.9) is printed in the source mosaic by
the YOLO plotter itself. The reel's aggregate figures are a hand audit and are
labelled as one on the B07 verdict card — see SOURCES.md.

GROUND IS THE REEL'S CREAM (#FAF9F5, the Claude page), matching the bookends so
the evidence beats sit in the same room as the rest of the reel.

Run:  python3 make_plates.py           # needs Pillow (system python3, NOT .venv)
      python3 make_plates.py --audit   # re-check label-bar bleed, write nothing
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC0 = HERE / "images" / "B02-source.jpg"      # val_batch0_pred.jpg, 1920x1280, 4x4 of 480x320
SRC1 = HERE / "images" / "B02b-source.jpg"     # val_batch1_pred.jpg, 1920x1920, 4x4 of 480x480

GROUND = (250, 249, 245)     # #FAF9F5 — CLAUDE.PAGE, the reel's ground
INK = (61, 57, 41)           # #3D3929 — CLAUDE.INK
MUTE = (115, 112, 95)        # #73705F — CLAUDE.INK_SOFT
EDGE = (198, 194, 182)       # card rule: reads on cream without competing
ACCENT = (217, 119, 87)      # #D97757 — terracotta, one moment per plate

SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
SANS_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# A cell is only re-tileable if its label bars cross NEITHER of its vertical
# edges, and the two failures look different on the plate:
#   INHERIT_LEFT — a fragment of the LEFT neighbour's caption appears, belonging
#                  to a picture the viewer is no longer looking at.
#   BLEED_RIGHT  — the cell's OWN caption is sliced mid-word at the plate edge.
# The first version of this file screened only for INHERIT_LEFT, picked r1c3 and
# r3c3, and both shore frames came out reading "common lo". Both sets below are
# printed by --audit; re-run it if the source sheet is ever regenerated.
INHERIT_LEFT = {(1, 4), (2, 4), (3, 4)}
BLEED_RIGHT = {(1, 3), (2, 3), (3, 3)}
UNSAFE = INHERIT_LEFT | BLEED_RIGHT

# 8 of 16, laid 2 wide x 4 tall. LEFT column: the bird fills the frame. RIGHT
# column: it does not. (row, col) into val_batch0_pred.jpg's 4x4 grid.
# Every cell is outside UNSAFE — the far shore frames, which would have carried
# the scale ramp furthest, all bleed right and are spent rather than sliced.
PORTRAIT_CELLS = [
    (2, 1), (3, 1),   # the close-up that got three boxes  |  drone, two birds ~4px
    (4, 2), (4, 4),   # a full-frame bird                  |  the reed bed, small ducks
    (1, 1), (1, 2),   # a full-frame bird                  |  mid-distance, on chop
    (3, 2), (4, 3),   # a bird coming out of a dive        |  mid-distance, clean water
]

KICKER_02 = "FIRST ITERATION  ·  LOONNET  ·  THE VALIDATION SET, AS THE MODEL RETURNED IT"
KICKER_04 = "FOUR FRAMES  ·  WHAT IT FINDS, WHAT IT DOUBLES, WHAT IT INVENTS, WHAT IT MISSES"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def plate(w, h):
    im = Image.new("RGB", (w, h), GROUND)
    return im, ImageDraw.Draw(im)


def kicker(d, x, y, s, size):
    f = font(SANS_B, size)
    d.text((x, y), s, font=f, fill=MUTE)
    return y + size + int(size * 0.55)


def caption(d, x, y, w, lines, size, accent_first_word=False):
    """Caption block. Each line is (text, colour)."""
    f = font(SANS, size)
    for s, col in lines:
        d.text((x, y), s, font=f, fill=col)
        y += int(size * 1.45)
    return y


def card(im, d, box_im, x, y, w, h, rule=True, align="center"):
    """Paste box_im fitted into (x,y,w,h) with a hairline rule around it.

    align="left" matters on the portrait plate: four 3:2 frames stacked in a
    2160-wide column are height-constrained, so a centred paste floats each
    image ~430px right of the caption that names it and the panel stops reading
    as one unit. Left-aligned, image and label share an edge.
    """
    sc = min(w / box_im.width, h / box_im.height)
    nw, nh = int(box_im.width * sc), int(box_im.height * sc)
    ox = x if align == "left" else x + (w - nw) // 2
    oy = y + (h - nh) // 2
    im.paste(box_im.resize((nw, nh), Image.LANCZOS), (ox, oy))
    if rule:
        d.rectangle([ox - 1, oy - 1, ox + nw, oy + nh], outline=EDGE, width=2)
    return ox, oy, nw, nh


def cell(src, r, c, cw, ch):
    return src.crop(((c - 1) * cw, (r - 1) * ch, c * cw, r * ch))


# ─────────────────────────────────────────────────────────────────────────────
def audit():
    """Scan vertical cell boundaries for solid label-bar fill that crosses them."""
    import numpy as np
    for path, cols, rows in [(SRC0, 4, 4), (SRC1, 4, 4)]:
        a = np.asarray(Image.open(path).convert("RGB")).astype(int)
        H, W, _ = a.shape
        cw, ch = W // cols, H // rows
        R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
        bar = (B > 150) & (B - R > 90) & (B - G > 90)   # label fill, not white text
        inherits, bleeds = set(), set()
        for k in range(1, cols):
            for r in range(rows):
                n = int(bar[r * ch:(r + 1) * ch, k * cw - 3:k * cw + 3].sum())
                if n > 15:
                    bleeds.add((r + 1, k))        # left of the boundary: own bar sliced
                    inherits.add((r + 1, k + 1))  # right of it: inherits a fragment
        print(f"{path.name}")
        print(f"  inherit a fragment from the left : {sorted(inherits) or 'none'}")
        print(f"  own bar sliced at the right edge : {sorted(bleeds) or 'none'}")
        if path is SRC0:
            ok = (inherits == INHERIT_LEFT and bleeds == BLEED_RIGHT)
            print(f"  constants in this file           : "
                  f"{'MATCH' if ok else 'STALE — UPDATE INHERIT_LEFT/BLEED_RIGHT'}")
            clash = [c for c in PORTRAIT_CELLS if c in (inherits | bleeds)]
            print(f"  PORTRAIT_CELLS clashes           : {clash or 'none'}")


# ─────────────────────────────────────────────────────────────────────────────
def b02_landscape():
    """3840x2160 — the whole sheet, held, on cream."""
    W, H = 3840, 2160
    im, d = plate(W, H)
    M = 200
    y = kicker(d, M, M, KICKER_02, 34)
    cap_h = 150
    src = Image.open(SRC0)
    card(im, d, src, M, y, W - 2 * M, H - y - M - cap_h)
    cy = H - M - cap_h + 10
    caption(d, M, cy, W - 2 * M, [
        ("16 of the 26 held-out frames · blue boxes and confidence scores are the model's own output",
         INK),
        ("Two classes were trained: common loon, and non loon.", MUTE),
    ], 38)
    out = HERE / "media" / "B02.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out)
    print("wrote", out.relative_to(HERE))


def b02_portrait():
    """2160x3840 — 8 of 16 cells, re-tiled 2x4, near/far paired by row."""
    W, H = 2160, 3840
    im, d = plate(W, H)
    MX, MY = 120, 200
    y = kicker(d, MX, MY, "8 OF 16 FRAMES, RE-TILED", 40)
    src = Image.open(SRC0)
    cw, ch = 480, 320
    gap = 24
    tw = (W - 2 * MX - gap) // 2          # 960
    th = int(tw * ch / cw)               # 640
    cap_h = 210
    grid_h = 4 * th + 3 * gap
    top = y + max(0, (H - MY - cap_h - y - grid_h) // 2)
    for i, (r, c) in enumerate(PORTRAIT_CELLS):
        assert (r, c) not in UNSAFE, f"r{r}c{c} inherits a label fragment"
        t = cell(src, r, c, cw, ch).resize((tw, th), Image.LANCZOS)
        x = MX + (i % 2) * (tw + gap)
        yy = top + (i // 2) * (th + gap)
        im.paste(t, (x, yy))
        d.rectangle([x - 1, yy - 1, x + tw, yy + th], outline=EDGE, width=2)
    cy = H - MY - cap_h + 10
    caption(d, MX, cy, W - 2 * MX, [
        ("Left column: the bird fills the frame.", INK),
        ("Right column: it does not. 8 of the 16 frames", MUTE),
        ("on this batch sheet, re-tiled — not the whole set.", MUTE),
    ], 46)
    out = HERE / "pantry" / "B02-916.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out)
    print("wrote", out.relative_to(HERE))


# The four panels: (source, row, col, cell-w, cell-h, tag, tag-colour, sub)
PANELS = [
    (SRC0, 3, 1, 480, 320, "FOUND",         INK,    "two birds, a few pixels each — both detected, 0.6 and 0.8"),
    (SRC0, 2, 1, 480, 320, "COUNTED TWICE", ACCENT, "one bird, three overlapping boxes"),
    (SRC0, 4, 4, 480, 320, "NOT A LOON",    ACCENT, "the reed bed is boxed; a duck is called a loon at 0.3"),
    (SRC1, 1, 3, 480, 480, "NOT FOUND",     ACCENT, "two loons in fog — the model returned nothing"),
]


def b04_landscape():
    """3840x2160 — four panels, 2x2, one success and three failures."""
    W, H = 3840, 2160
    im, d = plate(W, H)
    M = 200
    y = kicker(d, M, M, KICKER_04, 34)
    gap_x, gap_y = 70, 64
    lab_h = 116
    pw = (W - 2 * M - gap_x) // 2
    ph = (H - y - M - gap_y - 2 * lab_h) // 2
    f_tag, f_sub = font(SANS_B, 42), font(SANS, 33)
    for i, (src, r, c, cw, ch, tag, col, sub) in enumerate(PANELS):
        x = M + (i % 2) * (pw + gap_x)
        yy = y + (i // 2) * (ph + lab_h + gap_y)
        card(im, d, cell(Image.open(src), r, c, cw, ch), x, yy, pw, ph)
        d.text((x, yy + ph + 18), tag, font=f_tag, fill=col)
        d.text((x, yy + ph + 72), sub, font=f_sub, fill=MUTE)
    out = HERE / "media" / "B04.png"
    im.save(out)
    print("wrote", out.relative_to(HERE))


def b04_portrait():
    """2160x3840 — the same four panels stacked 1x4."""
    W, H = 2160, 3840
    im, d = plate(W, H)
    MX, MY = 120, 200
    y = kicker(d, MX, MY, "FOUR FRAMES", 40)
    gap, lab_h = 40, 132
    pw = W - 2 * MX
    ph = (H - y - MY - 3 * gap - 4 * lab_h) // 4
    f_tag, f_sub = font(SANS_B, 50), font(SANS, 36)
    for i, (src, r, c, cw, ch, tag, col, sub) in enumerate(PANELS):
        yy = y + i * (ph + lab_h + gap)
        card(im, d, cell(Image.open(src), r, c, cw, ch), MX, yy, pw, ph, align="left")
        d.text((MX, yy + ph + 20), tag, font=f_tag, fill=col)
        d.text((MX, yy + ph + 82), sub, font=f_sub, fill=MUTE)
    out = HERE / "pantry" / "B04-916.png"
    im.save(out)
    print("wrote", out.relative_to(HERE))


if __name__ == "__main__":
    if "--audit" in sys.argv:
        audit()
    else:
        b02_landscape()
        b02_portrait()
        b04_landscape()
        b04_portrait()
