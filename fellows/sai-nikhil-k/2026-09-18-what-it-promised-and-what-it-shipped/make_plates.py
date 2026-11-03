#!/usr/bin/env python3
"""make_plates.py — compose Gavia's own result screen into presentation plates.

WHY THIS EXISTS. B02 is the author's evidence that the application exists and
runs: his own capture of Gavia 0.1.0 returning a detection. Under
EXECUTABLE-EVIDENCE.md that still IS the evidence — it is a source artifact, not
a picture of a computation we could run ourselves — so it goes on screen
unretouched. But it cannot be a straight paste, for two reasons.

1. NO KEN BURNS, NO CENTRE CUT. compile.py's zoompan pushes ~8% outward, which
   walks the "PROTOTYPE FOR CONSERVATION RESEARCH" footer and the top nav out of
   frame — and that footer is the honesty disclosure the verdict beat quotes. So
   the beat HOLDS (shot.motion = "hold"). shorts.py's centre cut is worse: it
   keeps the middle ~37.5% of the width, which throws away the entire
   right-hand Detection details panel, i.e. the 82% the narration says out loud.

2. THE PORTRAIT PLATE IS A DIFFERENT SHEET. Instead of cropping, it RE-COMPOSES
   the same screen as three stacked blocks in reading order — the verdict banner,
   the boxed bird, then the confidence panel. On a phone that reads better than
   the landscape original, not worse: the 82% is ~4x larger than a centre cut
   would leave it. Because the two plates order their blocks differently, the
   narration carries NO positional reference ("the panel on the right") — the
   same mp3 plays over both.

WHAT IS NOT DONE HERE. No bounding box, label, percentage, button or footer is
redrawn, recoloured or repositioned. The only additions are the reel's cream
ground, a thin card rule, a kicker and a source caption. The two secondary
screens (previous checks, about) appear in the landscape plate as thumbnails at
their own aspect, because the narration mentions the history page.

FIGURES. The only number these plates put on screen is the one already inside
the author's capture: 82% on one box in one photograph. That is a PER-IMAGE
detection confidence and nothing else — the model card's metrics live on B03.

GROUND is the reel's cream (#FAF9F5, CLAUDE.PAGE) so the evidence beat sits in
the same room as the bookends.

Run:  python3 make_plates.py           # needs Pillow (system python3, NOT .venv)
      python3 make_plates.py --audit   # dump the crop regions, write no plates
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC_DETECT = HERE / "images" / "B02-source-detect.jpg"    # 1600x1371, the result screen
SRC_HIST = HERE / "images" / "B02-source-history.jpg"     # previous checks
SRC_ABOUT = HERE / "images" / "B02-source-about.jpg"      # about

GROUND = (250, 249, 245)   # #FAF9F5 — CLAUDE.PAGE, the reel's ground
INK = (61, 57, 41)         # #3D3929 — CLAUDE.INK
MUTE = (115, 112, 95)      # #73705F — CLAUDE.INK_SOFT
EDGE = (198, 194, 182)     # card rule: reads on cream without competing

# GATE V measures against a title-safe inset and calls anything outside it
# edge-bleed. The first cut of these plates used 150-168px margins on a 3840
# frame and was blocked on left/right/bottom at B02_50 and B02_85 (2026-09-18).
# 6% of the short edge clears it with room to spare in both aspects.
SAFE_FRAC = 0.06


def safe(w, h):
    """Title-safe inset in px for a frame, measured off the SHORT edge."""
    return round(min(w, h) * SAFE_FRAC)


def assert_inside(name, w, h, x0, y0, x1, y1):
    m = safe(w, h)
    assert x0 >= m and y0 >= m and x1 <= w - m and y1 <= h - m, (
        f"{name} outside title-safe ({m}px): box=({x0},{y0})-({x1},{y1}) in {w}x{h}")

SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
SANS_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# Crop regions inside SRC_DETECT (1600x1371 native, so these are 1:1 pixels).
# Verified with --audit before the plates were composed.
BANNER = (193, 163, 1387, 322)    # "CHECK COMPLETE / 1 loon detected"
PHOTO = (193, 353, 923, 925)      # the boxed bird + "Highlighted areas..." line
DETAIL = (950, 352, 1392, 700)    # Detection details: 82%, the bar, "Loon 82%"

KICKER = "GAVIA 0.1.0  ·  THE RESULT SCREEN, AS THE APPLICATION DREW IT"
CAPTION = ("Author's own capture of Gavia 0.1.0 · unretouched — no box, label, "
           "percentage or footer redrawn or repositioned")
CAPTION_916 = ("Author's own capture of Gavia 0.1.0, re-composed as three blocks — "
               "nothing inside them redrawn")
NOTE_916 = "82% is the score on this one box in this one photograph — not a model metric"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def centred(d, y, s, f, fill):
    d.text(((d.im.size[0] - text_w(d, s, f)) / 2, y), s, font=f, fill=fill)


def carded(plate, im, box, rule=3):
    """Paste im at box (x, y, w, h) with a thin rule around it."""
    x, y, w, h = box
    im = im.resize((w, h), Image.LANCZOS)
    plate.paste(im, (x, y))
    ImageDraw.Draw(plate).rectangle([x - rule, y - rule, x + w + rule - 1, y + h + rule - 1],
                                    outline=EDGE, width=rule)


def fit(size, w=None, h=None):
    """Scale (w0, h0) to a target width or height, preserving aspect."""
    w0, h0 = size
    if w:
        return (w, round(w * h0 / w0))
    return (round(h * w0 / h0), h)


def audit():
    det = Image.open(SRC_DETECT)
    print(f"SRC_DETECT {det.size}")
    for name, box in (("BANNER", BANNER), ("PHOTO", PHOTO), ("DETAIL", DETAIL)):
        w, h = box[2] - box[0], box[3] - box[1]
        assert 0 <= box[0] < box[2] <= det.size[0] and 0 <= box[1] < box[3] <= det.size[1], name
        out = HERE / "images" / f"_audit-{name.lower()}.png"
        det.crop(box).save(out)
        print(f"  {name:<7} {box}  {w}x{h}  aspect {w/h:.3f}  -> {out.name}")
    for p in (SRC_HIST, SRC_ABOUT):
        print(f"  {p.name}  {Image.open(p).size}")


def landscape():
    """3840x2160. The result screen at size, the two other screens as thumbnails."""
    W, H = 3840, 2160
    M = safe(W, H)                      # 130px
    plate = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(plate)
    f_kick, f_cap = font(SANS_B, 44), font(SANS, 38)

    left = M + 80                        # 210: clears title-safe with margin
    d.text((left, 120), KICKER, font=f_kick, fill=MUTE)
    d.line([(left, 196), (W - left, 196)], fill=EDGE, width=3)

    # The result screen, full, scaled to the working height.
    det = Image.open(SRC_DETECT)
    main_h = 1520
    main_w = fit(det.size, h=main_h)[0]
    carded(plate, det, (left, 280, main_w, main_h))
    assert_inside("B02 main", W, H, left, 280, left + main_w, 280 + main_h)

    # The other two screens, stacked to the right at a common width.
    # The two secondary screens are constrained by HEIGHT, not width: the About
    # capture is 2562x2108, much taller than the others, and fitting it to the
    # column width ran it off the bottom of the plate and through the caption.
    col_x = left + main_w + 140
    col_w = W - col_x - left
    thumb_h = 600
    y = 280
    for src, label in ((SRC_HIST, "Previous checks — kept on your own disk"),
                       (SRC_ABOUT, "About — the tool's own note on its limits")):
        im = Image.open(src)
        tw, th = fit(im.size, h=thumb_h)
        assert tw <= col_w, f"{src.name} thumbnail {tw}px wider than column {col_w}px"
        tx = col_x + (col_w - tw) // 2
        carded(plate, im, (tx, y, tw, th))
        d.text((tx, y + th + 30), label, font=f_cap, fill=MUTE)
        assert_inside("B02 thumb", W, H, tx, y, tx + tw, y + th + 60)
        y += th + 150

    cap_y = H - 200
    assert y < cap_y, f"thumbnail column overruns the caption: bottom at {y}"
    centred(d, cap_y, CAPTION, f_cap, MUTE)
    assert cap_y + 50 <= H - M, "caption crosses title-safe bottom"
    out = HERE / "media" / "B02.png"
    plate.save(out)
    print(f"wrote {out.relative_to(HERE)}  {W}x{H}")


def portrait():
    """2160x3840. The same screen RE-COMPOSED as three stacked blocks."""
    W, H = 2160, 3840
    M = safe(W, H)                      # 130px
    plate = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(plate)
    f_kick, f_cap, f_note = font(SANS_B, 46), font(SANS, 40), font(SANS_B, 44)
    det = Image.open(SRC_DETECT)

    centred(d, 200, "GAVIA 0.1.0  ·  ONE IMAGE IN", f_kick, MUTE)
    d.line([(M + 40, 286), (W - M - 40, 286)], fill=EDGE, width=3)

    y = 380
    for box, width in ((BANNER, 1760), (PHOTO, 1700), (DETAIL, 1380)):
        crop = det.crop(box)
        bw, bh = fit(crop.size, w=width)
        carded(plate, crop, ((W - bw) // 2, y, bw, bh))
        y += bh + 110

    note_y, cap_y = y + 30, H - 300
    centred(d, note_y, NOTE_916, f_note, INK)
    centred(d, cap_y, CAPTION_916, f_cap, MUTE)
    assert note_y + 60 < cap_y, f"portrait stack overruns the caption: note at {note_y}"
    assert cap_y + 50 <= H - M, "caption crosses title-safe bottom"
    out = HERE / "pantry" / "B02-916.png"
    plate.save(out)
    print(f"wrote {out.relative_to(HERE)}  {W}x{H}   stack bottom y={y}")


if __name__ == "__main__":
    if "--audit" in sys.argv:
        audit()
    else:
        audit()
        landscape()
        portrait()
