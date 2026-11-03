#!/usr/bin/env python3
"""make_plates.py — compose the annotation screenshot into presentation plates.

WHY THIS EXISTS. B03 is the evidence beat: a real frame from this week's
annotation pass, two loons boxed by hand. The source capture is 2354x1320,
i.e. 1.783 — near enough to 16:9 that the landscape plate needs no reframing
at all. The 9:16 Shorts cut is the problem. shorts.py centre-cuts user media,
and a centre cut of this frame keeps the middle 31.6% of its width: x 805-1549
in source pixels. The boxes live at x 927-1344, so they would SURVIVE that cut
by about 120px on the left and 205px on the right. Surviving is not the same as
being composed, and a cut that close to the edge of the subject is one
re-capture away from decapitating it. Both plates are built here instead, and
the portrait one goes to pantry/B03-916.png — the one human override slot
shorts.py honours for user media.

GROUND IS THE REEL'S CREAM. Every other beat in this reel is the deckPatterns
ground (#F2F0E9). A full-bleed grey-blue lake plate would read as a different
film spliced in, and Gate V would have a fair complaint about ink/background
separation on an image whose subject is two small dark birds on mid-grey water.
Seating the photograph as a captioned card on the cream fixes the tonal
continuity and the contrast reading in one move, and the card rule does the
work the frame edge was doing.

THE PORTRAIT CROP IS NOT A CENTRE CUT. It is 1180px wide (0.894:1) at the full
source height, centred on the box centroid at x=1135.5. That ratio is chosen so
the card fills a 9:16 plate without the structural UNDERFILL that a 16:9 image
in a 9:16 frame always trips. Keeping the FULL HEIGHT is deliberate: the beat's
argument is how much of the frame is not a loon, and vertical empty water is
what carries that on a phone once the horizontal has been taken away.

MARGINS ARE SIZED FOR THE MOVE. B03 is ken-burnsed, and compile.py's zoompan
pushes content outward as it zooms (z=1.08 toward shot.focus). The card box is
2960 wide so a 1.08 zoom still leaves real margin against the 108px title-safe
inset — the same sizing 08-21's moving plate needed.

This script PRINTS the box centroid in plate coordinates. That is not a
diagnostic: it is the number that goes into shot.focus in beat_sheet.json, and
it is not the source centroid, because matting the card moves the subject.

Run:  python3 make_plates.py          # needs Pillow (system python3, not .venv)
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC = HERE / "images" / "B03-source.png"

GROUND = (242, 240, 233)     # #F2F0E9 — the deckPatterns ground
INK = (61, 57, 41)           # #3D3929
MUTE = (122, 114, 101)       # #7A7265
EDGE = (198, 194, 182)       # card rule: reads on cream without competing

SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"

KICKER = "ANNOTATION PASS  ·  WEEK ONE"
# DOUBLE-CHECK LAW: this plate states exactly what it is and nothing more.
# Two boxes is a COUNT OF WHAT IS VISIBLE IN THIS FRAME — it is not a dataset
# total, and no dataset total is asserted anywhere in this reel.
CAPTION = "AUTHOR'S OWN FRAME  ·  TWO INSTANCES BOXED BY HAND"

# Portrait crop: full source height, 1180px wide, centred on the box centroid.
PORTRAIT_W = 1180


def font(size):
    try:
        return ImageFont.truetype(SANS, size)
    except Exception:
        return ImageFont.load_default()


def tracked(draw, xy, text, f, fill, track):
    """Draw letterspaced text (Pillow has no tracking)."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + track


def tracked_width(draw, text, f, track):
    return sum(draw.textlength(c, font=f) for c in text) + track * (len(text) - 1)


def centered_tracked(draw, y, text, f, fill, track, W):
    tracked(draw, ((W - tracked_width(draw, text, f, track)) / 2, y), text, f, fill, track)


def box_bounds(im):
    """Locate the green annotation rectangles so focus can be derived, not guessed."""
    a = np.array(im.convert("RGB")).astype(int)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    m = (g > 120) & (g - r > 60) & (g - b > 60)
    ys, xs = np.nonzero(m)
    if not len(xs):
        raise SystemExit("no green annotation boxes found in the source capture")
    return xs.min(), xs.max(), ys.min(), ys.max()


def plate(im, W, H, box, out, k_size=50, c_size=46, label=""):
    sw, sh = im.size
    bw, bh = box
    scale = min(bw / sw, bh / sh)
    w, h = round(sw * scale), round(sh * scale)
    card = im.resize((w, h), Image.LANCZOS)

    p = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(p)
    fk, fc = font(k_size), font(c_size)

    # Centre the whole GROUP — kicker, card, caption — so the plate reads as
    # balanced rather than top-weighted.
    k_gap, c_gap = 118, 104
    group_h = k_size + k_gap + h + c_gap + c_size
    y0 = (H - group_h) // 2
    x = (W - w) // 2
    y_card = y0 + k_size + k_gap

    centered_tracked(d, y0, KICKER, fk, MUTE, 5, W)
    p.paste(card, (x, y_card))
    d.rectangle([x - 2, y_card - 2, x + w + 1, y_card + h + 1], outline=EDGE, width=3)
    centered_tracked(d, y_card + h + c_gap, CAPTION, fc, INK, 5, W)

    out.parent.mkdir(parents=True, exist_ok=True)
    p.save(out)

    # The focus number for beat_sheet.json, in PLATE space.
    x0b, x1b, y0b, y1b = box_bounds(im)
    fx = (x + (x0b + x1b) / 2 * scale) / W
    fy = (y_card + (y0b + y1b) / 2 * scale) / H
    print(f"[plates] {out.relative_to(HERE)}  {W}x{H}  card {w}x{h} "
          f"({w / sw:.2f}x upscale)  side margin {x}px  top margin {y_card}px")
    print(f"[plates]   {label} box centroid in plate space: "
          f"focus [{fx:.3f}, {fy:.3f}]  ·  boxes span {(x1b - x0b) * scale / W * 100:.1f}% of frame width")
    return fx, fy


src = Image.open(SRC).convert("RGB")
bx0, bx1, by0, by1 = box_bounds(src)
print(f"[plates] source {src.size}  ratio {src.width / src.height:.3f}  "
      f"boxes x{bx0}-{bx1} y{by0}-{by1}  centroid "
      f"({(bx0 + bx1) / 2 / src.width:.3f}, {(by0 + by1) / 2 / src.height:.3f})")

# 16:9 master plate. Full uncropped frame — the emptiness around the birds is
# the beat's argument, so nothing is trimmed. 2960 wide leaves ken-burns
# headroom inside the title-safe inset.
plate(src, 3840, 2160, box=(2960, 1480),
      out=HERE / "media" / "B03.png", label="16:9")

# 9:16 Shorts plate — a composed portrait crop, NOT a centre cut, at larger type
# for a phone. Full height retained on purpose (see module docstring).
cx = (bx0 + bx1) / 2
left = round(cx - PORTRAIT_W / 2)
left = max(0, min(left, src.width - PORTRAIT_W))
print(f"[plates] portrait crop: x{left}-{left + PORTRAIT_W} of {src.width} "
      f"(centre cut would have been x{round(src.width * .342)}-{round(src.width * .658)})")
plate(src.crop((left, 0, left + PORTRAIT_W, src.height)),
      2160, 3840, box=(1860, 2400),
      out=HERE / "pantry" / "B03-916.png", k_size=54, c_size=40, label="9:16")
