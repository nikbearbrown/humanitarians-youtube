#!/usr/bin/env python3
"""make_plates.py — compose the YOLO label mosaic into presentation plates.

WHY THIS EXISTS. B02 is the evidence beat: the author's own label mosaic,
`val_batch0_labels.jpg`, the read-back the YOLO toolchain prints of the
annotated set with its boxes drawn on. The source is 1920x1280 (3:2) and is
itself a 4x4 contact sheet of 480x320 tiles. Two things follow, and they are
the whole reason this file exists rather than a straight paste:

1. NO KEN BURNS, AND NO CENTRE CUT. The beat's argument is the RANGE ACROSS
   ALL SIXTEEN TILES — a bird that fills half its frame in one cell and is
   four dark pixels in another. compile.py's zoompan pushes ~8% outward, which
   clips the outer cells; shorts.py's centre cut keeps the middle 37.5% of the
   width, i.e. it would slice columns 1 and 2 in half and throw away the two
   tiles the argument depends on. So the landscape plate HOLDS
   (shot.motion = "hold") and the portrait plate is RE-TILED, not cropped.

2. THE PORTRAIT PLATE IS A DIFFERENT SHEET, AND SAYS SO. It is eight of the
   sixteen tiles, re-laid 2 wide x 4 tall, each row deliberately pairing a
   near/large subject with a far/small one so the scale argument reads
   vertically on a phone. Eight tiles at 2.02x land ~970px wide in a
   2160x3840 plate, against ~615px for sixteen tiles in the landscape one —
   the portrait cut is the MORE legible of the two, not a degraded fallback.
   DOUBLE-CHECK LAW: it is a subset, so its caption states "8 OF 16 TILES,
   RE-TILED" and never implies the viewer is seeing the whole batch.

CARD SIZE IS SET BY LEGIBILITY, NOT BY TASTE. Plate 2160 tall, 108px
title-safe inset, minus kicker + gaps + caption, leaves ~1640px for the card;
at 3:2 that is 2460x1640, so a source tile lands 615px wide. The per-tile
FILENAMES in the mosaic are ~20px in the source, i.e. ~26px on a 3840 plate —
present but not comfortably readable. That is why the three capture paths
(web / Nikon / drone, read off the `web_`, `nikon_` and `dji_` prefixes) are
carried as TYPE on B01's chip grid and in the narration, and the plate is
never asked to prove them by itself. See SOURCES.md.

GROUND IS THE REEL'S CREAM (#FAF9F5, the Claude page). Five of the eight beats
sit on it; only the two deck patterns use #F2F0E9, and the two creams are a
step apart. Seating the mosaic as a captioned card on cream rather than
full-bleed keeps tonal continuity with the bookends and gives Gate V a real
ink/ground separation to measure on a plate whose own subjects are dark birds
on mid-grey water.

Run:  python3 make_plates.py      # needs Pillow (system python3, NOT .venv)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC = HERE / "images" / "B02-source.jpg"

GROUND = (250, 249, 245)     # #FAF9F5 — CLAUDE.PAGE, the reel's ground
INK = (61, 57, 41)           # #3D3929 — CLAUDE.INK
MUTE = (115, 112, 95)        # #73705F — CLAUDE.INK_SOFT
EDGE = (198, 194, 182)       # card rule: reads on cream without competing

SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"

KICKER = "ANNOTATION PASS  ·  WEEK TWO  ·  LABELS AS THE TRAINER READS THEM BACK"

# DOUBLE-CHECK LAW: each caption states exactly what its own plate is.
# "16 tiles" / "8 of 16" are counts of what is VISIBLE ON THAT PLATE. Neither
# is a dataset total, and no dataset total is asserted on either plate — the
# only figure the author supplied (about 136 images) lives in the narration
# and on the type beats, never lettered onto the photograph.
CAPTION_169 = "AUTHOR'S OWN LABEL MOSAIC  ·  16 TILES  ·  ONE CLASS: COMMON LOON"
CAPTION_916 = "AUTHOR'S OWN LABEL MOSAIC  ·  8 OF 16 TILES, RE-TILED  ·  ONE CLASS"

# Source is a 4x4 sheet of 480x320 cells (1920/4, 1280/4 — verified exact).
COLS, ROWS = 4, 4

# The portrait re-tile, as (row, col) into the source sheet.
#
# ORDERED AS A SCALE RAMP, LARGEST SUBJECT FIRST. Read top to bottom the sheet
# goes from a bird that fills its frame to a bird that is four dark pixels on
# open water — so the plate itself performs the beat's argument instead of
# merely containing it. On a phone, where the viewer travels the plate
# vertically, a ramp reads; the source sheet's arbitrary order does not.
#
# WHICH CELLS ARE ELIGIBLE, AND WHY IT IS NOT A FREE CHOICE. In the source
# mosaic the per-tile filename and the `common loon` box captions are drawn
# without clipping, so the long `nikon_*` names OVERFLOW their cell to the
# right. Slicing on the cell grid therefore does two different things:
#   · a cell whose OWN caption overflows loses its tail — reads as ordinary
#     truncation, acceptable;
#   · a cell whose LEFT NEIGHBOUR overflowed inherits an ORPHAN FRAGMENT — a
#     floating "oon" belonging to no visible box, which reads as a rendering
#     bug and invites the viewer to distrust the plate.
# Column 3 sits downstream of the long nikon names, so (0,3), (1,3) and (2,3)
# are excluded on those grounds — not for composition. (3,3) survives because
# its left neighbour is a short `web_*` name. Every cell below is
# orphan-free; (1,2) truncates its own filename tail and nothing else.
PORTRAIT_TILES = [
    [(1, 0), (1, 1)],      # nearest — headshot; clean swimmer
    [(2, 1), (3, 1)],      # mid     — wing flap; green water
    [(0, 1), (3, 3)],      # small   — mid swimmer; three instances in reeds
    [(2, 0), (1, 2)],      # smallest— dji, two specks; nikon, distant shoreline
]


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


def tiles(im):
    """Slice the source contact sheet into its 4x4 grid of cells."""
    tw, th = im.width // COLS, im.height // ROWS
    return {(r, c): im.crop((c * tw, r * th, (c + 1) * tw, (r + 1) * th))
            for r in range(ROWS) for c in range(COLS)}, tw, th


def retile(im, layout):
    """Rebuild a sheet from `layout` — a list of rows of (row, col) source cells."""
    cells, tw, th = tiles(im)
    w, h = len(layout[0]) * tw, len(layout) * th
    out = Image.new("RGB", (w, h), GROUND)
    for r, row in enumerate(layout):
        for c, key in enumerate(row):
            out.paste(cells[key], (c * tw, r * th))
    return out


def plate(im, W, H, box, out, caption, k_size=46, c_size=42, k_gap=110, c_gap=95,
          label=""):
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
    group_h = k_size + k_gap + h + c_gap + c_size
    y0 = (H - group_h) // 2
    x = (W - w) // 2
    y_card = y0 + k_size + k_gap

    centered_tracked(d, y0, KICKER, fk, MUTE, 4, W)
    p.paste(card, (x, y_card))
    d.rectangle([x - 2, y_card - 2, x + w + 1, y_card + h + 1], outline=EDGE, width=3)
    centered_tracked(d, y_card + h + c_gap, caption, fc, INK, 4, W)

    out.parent.mkdir(parents=True, exist_ok=True)
    p.save(out)

    inset = min(x, y0)
    print(f"[plates] {out.relative_to(HERE)}  {W}x{H}  card {w}x{h} "
          f"({w / sw:.2f}x)  side margin {x}px  top margin {y0}px  "
          f"min inset {inset}px {'OK' if inset >= 108 else '⚠ INSIDE TITLE-SAFE'}")
    print(f"[plates]   {label} tile {round(sw / len(PORTRAIT_TILES[0]) * scale) if label == '9:16' else round(sw / COLS * scale)}px wide "
          f"·  filename type ≈{round(20 * scale)}px")


src = Image.open(SRC).convert("RGB")
print(f"[plates] source {src.size}  ratio {src.width / src.height:.3f}  "
      f"grid {COLS}x{ROWS} of {src.width // COLS}x{src.height // ROWS}")

# 16:9 master plate. All sixteen tiles, uncropped — the range across the whole
# sheet IS the beat, so nothing is trimmed and the beat holds instead of pushing.
# Height binds: 1640/1280 = 1.281 → a 2460x1640 card.
plate(src, 3840, 2160, box=(3500, 1640),
      out=HERE / "media" / "B02.png", caption=CAPTION_169, label="16:9")

# 9:16 Shorts plate — a composed RE-TILE, not a centre cut. Width binds:
# 1900/960 = 1.979 → a 1900x2533 card, tiles ~950px wide. 1900 rather than the
# available 1944 so the card RULE clears the 108px title-safe inset instead of
# landing exactly on it.
plate(retile(src, PORTRAIT_TILES), 2160, 3840, box=(1900, 3300),
      out=HERE / "pantry" / "B02-916.png", caption=CAPTION_916,
      k_size=40, c_size=38, label="9:16")
