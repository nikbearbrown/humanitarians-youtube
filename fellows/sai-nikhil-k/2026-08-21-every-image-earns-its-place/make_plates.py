#!/usr/bin/env python3
"""make_plates.py — compose the two Immer screenshots into presentation plates.

WHY THIS EXISTS. The two source screenshots are 1676x1054 and 1658x1052, i.e.
roughly 1.59:1. The reel is 16:9 (1.778) and the Shorts cut is 9:16.
compile.py fits stills with a single GLOBAL metadata.fit, and its default
("crop") scales to fill and then centre-crops — which on these two images shaves
~128px off the top at 4K and takes the "Immer / National Loon Center" lockup on
the landing page and the "NATIONAL LOON CENTER" kicker on the dashboard with it.
fit="pad" would keep them, but pads with the newsprint cream (0xF3EBDD)
hardcoded in vf_fit. So both plates are composed here at the exact output ratio,
and metadata.fit becomes a no-op for these beats.

GROUND IS THE REEL'S CREAM, NOT THE APP'S BLACK. The first pass put the
screenshots full-bleed on their own sampled near-black (17,19,22). Gate V called
it — ink/background separation 0.23-0.24 against a 0.30 floor — and the contact
sheet showed the real problem, which was bigger than the metric: every other
beat in this reel is cream, so two near-black plates read as a different film
spliced in. Seating the dark UI as a CARD on the deck-pattern ground (#F2F0E9)
fixes the contrast reading and the tonal continuity in one move, and the card
edge now does the job the sampled ground was doing.

MARGINS ARE SIZED FOR THE MOVE, NOT THE FRAME. B04 is ken-burnsed, and
compile.py's zoompan pushes content OUTWARD as it zooms (z=1.08 toward
shot.focus). The first pass sized the card to the frame, cleared title-safe as a
still, and then bled over the right edge once it was moving — two BLOCKERs. The
card box is now 2960 wide, so a 1.08 zoom biased to focus x=0.34 still leaves
roughly 275px of margin against a 108px inset.

The portrait plates go to pantry/<bid>-916.png, the ONE human override slot
shorts.py honours for user media — otherwise it would centre-cut these landscape
screenshots to a narrow vertical slice. They will still read as UNDERFILL in
Gate V: a 1.59:1 image can only be so tall in a 9:16 frame. That is structural,
not a defect, and it is a MAJOR rather than a BLOCKER.

Run:  python3 make_plates.py          # needs Pillow (system python3, not .venv)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
# Sources live INSIDE the reel (rule 4: videos travel with their book). The
# originals were captured to ~/Desktop and had already been cleared off it
# partway through this build, so images/*-source.png were recovered from the
# first-pass portrait plates — which carried the full uncropped capture at only
# 1.13x. Replace these two files and re-run if the originals resurface; the
# round trip costs a little sharpness that a fresh capture would not.
SRC = HERE / "images"

GROUND = (242, 240, 233)     # #F2F0E9 — the deckPatterns ground, so B04/B05 sit
                             # with the illustration beats either side of them
INK = (61, 57, 41)           # #3D3929
MUTE = (122, 114, 101)       # #7A7265
EDGE = (198, 194, 182)       # card rule: reads on cream without competing

SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"

SHOTS = {
    "B04": {
        "src": SRC / "B04-source.png",
        "kicker": "IMMER  ·  NATIONAL LOON CENTER",
        "caption": "LOVABLE MOCK  ·  USER FLOW, NOT A BUILD",
        # Landscape only: the capture has ~30% empty page below the three
        # feature cards. Trimming it lets the content sit larger in a 16:9
        # frame. The PORTRAIT plate keeps the full height on purpose — there
        # the extra vertical extent is what fills the 9:16 frame.
        "keep_h_16x9": 0.73,
        # Conservative box: this is the ken-burnsed beat, so it needs zoom
        # headroom inside the title-safe inset.
        "box_16x9": (2960, 1480),
    },
    "B05": {
        "src": SRC / "B05-source.png",
        "kicker": "IMMER  ·  ANALYZE  →  REVIEW  →  DATASET",
        # DOUBLE-CHECK LAW: this screen is full of Lovable's placeholder
        # figures. The narration says so out loud; the plate says so on screen,
        # so a frame lifted out of the video still carries the disclaimer.
        "caption": "MOCK DATA  ·  EVERY FIGURE ON THIS SCREEN IS A PLACEHOLDER",
        # The capture ends mid-row through "Conservation Insights"; drop that
        # sliver so the plate does not show a half-rendered component.
        "keep_h_16x9": 0.945,
        # This beat HOLDS, so it needs no zoom headroom and can run as large as
        # the title-safe inset allows — it is dense 11px UI type and legibility
        # is the whole point of showing it.
        "box_16x9": (3200, 1560),
    },
}


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


def plate(spec, W, H, box, out, keep_h=1.0, k_size=50, c_size=46):
    im = Image.open(spec["src"]).convert("RGB")
    if keep_h < 1.0:
        im = im.crop((0, 0, im.width, round(im.height * keep_h)))
    sw, sh = im.size
    bw, bh = box
    scale = min(bw / sw, bh / sh)
    w, h = round(sw * scale), round(sh * scale)
    im = im.resize((w, h), Image.LANCZOS)

    plate = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(plate)
    fk, fc = font(k_size), font(c_size)

    # Centre the whole GROUP — kicker, card, caption — so the plate reads as
    # balanced rather than top-weighted.
    k_gap, c_gap = 118, 104
    group_h = k_size + k_gap + h + c_gap + c_size
    y0 = (H - group_h) // 2
    x = (W - w) // 2
    y_card = y0 + k_size + k_gap

    centered_tracked(d, y0, spec["kicker"], fk, MUTE, 5, W)
    plate.paste(im, (x, y_card))
    d.rectangle([x - 2, y_card - 2, x + w + 1, y_card + h + 1], outline=EDGE, width=3)
    centered_tracked(d, y_card + h + c_gap, spec["caption"], fc, INK, 5, W)

    out.parent.mkdir(parents=True, exist_ok=True)
    plate.save(out)
    print(f"[plates] {out.relative_to(HERE)}  {W}x{H}  card {w}x{h} "
          f"({w / sw:.2f}x upscale)  side margin {x}px")


for bid, spec in SHOTS.items():
    if not spec["src"].exists():
        raise SystemExit(f"missing source screenshot: {spec['src']}")
    # 16:9 master plate. 2960 wide leaves room for B04's ken-burns zoom to
    # expand without crossing the title-safe inset (see module docstring).
    plate(spec, 3840, 2160, box=spec["box_16x9"],
          out=HERE / "media" / f"{bid}.png", keep_h=spec["keep_h_16x9"])
    # 9:16 Shorts plate — full capture height, larger type for a phone.
    plate(spec, 2160, 3840, box=(1860, 2350),
          # c_size 44, not 52: B05's caption is 52 characters and at 52px it
          # ran to within 69px of the frame edge, inside the title-safe inset.
          out=HERE / "pantry" / f"{bid}-916.png", k_size=54, c_size=44)
