"""build_cards.py — PIL-rendered PNG cards for B00 and B05.

Output: media/B00.png  media/B05.png
Run:    python3 build_cards.py

Design tokens (newsprint vox):
  GROUND  #F3EBDD   INK     #2F2A26
  TERRA   #D35F43   TEAL    #3D5A80
  HAIRLINE #D4D4D4
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
GROUND  = (243, 235, 221)
INK     = (47,  42,  38)
TERRA   = (211, 95,  67)
TEAL    = (61,  90,  128)
WHITE   = (255, 255, 255)
HAIRLINE_C = (212, 212, 212)

OUT = Path(__file__).parent / "media"
OUT.mkdir(exist_ok=True)

# ── font resolution ──────────────────────────────────────────────────────────
FONT_DIR = Path(__file__).resolve().parents[5] / "brutalist-art/runtime/fonts"

def _font(name_fragment, size):
    """Search runtime/fonts for a TTF matching the fragment, fall back to default."""
    for ttf in FONT_DIR.rglob("*.ttf"):
        if name_fragment.lower() in ttf.name.lower():
            try:
                return ImageFont.truetype(str(ttf), size)
            except Exception:
                pass
    return ImageFont.load_default(size=size)

def text_center(draw, text, y, font, color=INK):
    """Draw text centered horizontally at y."""
    bb = draw.textbbox((0, 0), text, font=font)
    tw = bb[2] - bb[0]
    x = (W - tw) / 2
    draw.text((x, y), text, font=font, fill=color)
    return bb[3] - bb[1]   # height

def hairline(draw, y, margin=80, color=HAIRLINE_C):
    draw.line([(margin, y), (W - margin, y)], fill=color, width=2)


# ══════════════════════════════════════════════════════════════════════════════
# B00 — Opening title card
# "Build This." large serif + "The FAANG window." subtitle
# ══════════════════════════════════════════════════════════════════════════════

def build_B00():
    img  = Image.new("RGB", (W, H), GROUND)
    draw = ImageDraw.Draw(img)

    f_title    = _font("Garamond", 110)
    f_period   = _font("Garamond", 110)
    f_sub      = _font("Garamond",  46)
    f_greeting = _font("Garamond",  28)
    f_handle   = _font("Montserrat", 22) if True else _font("Garamond", 22)

    # greeting — top left
    draw.text((72, 52), "Olá, Kore", font=f_greeting, fill=TEAL)

    # title "Build This" + terracotta period on same baseline
    title_str  = "Build This"
    period_str = "."

    bb_title  = draw.textbbox((0, 0), title_str,  font=f_title)
    bb_period = draw.textbbox((0, 0), period_str, font=f_period)

    tw_title  = bb_title[2]  - bb_title[0]
    tw_period = bb_period[2] - bb_period[0]
    total_w   = tw_title + tw_period + 4

    x0 = (W - total_w) / 2
    y0 = H // 2 - 90

    draw.text((x0, y0), title_str,  font=f_title,  fill=INK)
    draw.text((x0 + tw_title + 4, y0), period_str, font=f_period, fill=TERRA)

    # hairline
    line_y = y0 + (bb_title[3] - bb_title[1]) + 22
    hairline(draw, line_y, margin=160)

    # subtitle
    sub_y = line_y + 22
    text_center(draw, "The FAANG window.", sub_y, f_sub, color=INK)

    # handle — bottom right
    handle = "@HumanitariansAI"
    bb_h = draw.textbbox((0, 0), handle, font=f_handle)
    hw = bb_h[2] - bb_h[0]
    hh = bb_h[3] - bb_h[1]
    hx = W - hw - 64
    hy = H - hh - 52
    draw.text((hx, hy), handle, font=f_handle, fill=TEAL)
    draw.line([(hx, hy + hh + 4), (hx + hw, hy + hh + 4)],
              fill=TERRA, width=2)

    img.save(OUT / "B00.png")
    print(f"[cards] wrote media/B00.png  {W}×{H}")


# ══════════════════════════════════════════════════════════════════════════════
# B05 — CTA card
# "bearbrown.co" large serif, #BuildThis tag, @HumanitariansAI handle,
# "Kore, in for Humanitarians AI." sign-off
# ══════════════════════════════════════════════════════════════════════════════

def build_B05():
    img  = Image.new("RGB", (W, H), GROUND)
    draw = ImageDraw.Draw(img)

    f_url     = _font("Garamond", 96)
    f_tag     = _font("Montserrat", 34) if True else _font("Garamond", 34)
    f_handle  = _font("Montserrat", 24) if True else _font("Garamond", 24)
    f_signoff = _font("Garamond", 30)

    # top hairline
    hairline(draw, 80, margin=72)

    # URL — centered
    url = "bearbrown.co"
    bb  = draw.textbbox((0, 0), url, font=f_url)
    uw  = bb[2] - bb[0]
    uh  = bb[3] - bb[1]
    ux  = (W - uw) / 2
    uy  = H // 2 - uh - 30
    draw.text((ux, uy), url, font=f_url, fill=INK)

    # terracotta underline on url
    draw.line([(ux, uy + uh + 8), (ux + uw, uy + uh + 8)],
              fill=TERRA, width=3)

    # bottom hairline
    hairline(draw, uy + uh + 20)

    # #BuildThis tag
    tag_y = uy + uh + 38
    text_center(draw, "#BuildThis", tag_y, f_tag, color=TERRA)

    # @HumanitariansAI handle — bottom right
    handle = "@HumanitariansAI"
    bb_h = draw.textbbox((0, 0), handle, font=f_handle)
    hw = bb_h[2] - bb_h[0]
    hh = bb_h[3] - bb_h[1]
    hx = W - hw - 64
    hy = H - hh - 52
    draw.text((hx, hy), handle, font=f_handle, fill=INK)
    draw.line([(hx, hy + hh + 4), (hx + hw, hy + hh + 4)],
              fill=TERRA, width=2)

    # sign-off — bottom left
    signoff = "Kore, in for Humanitarians AI."
    bb_s = draw.textbbox((0, 0), signoff, font=f_signoff)
    draw.text((72, hy), signoff, font=f_signoff, fill=INK)

    img.save(OUT / "B05.png")
    print(f"[cards] wrote media/B05.png  {W}×{H}")


if __name__ == "__main__":
    build_B00()
    build_B05()
    print("[cards] done — drop into clips/ via: python3 ../../../../../../brutalist-art/runtime/scripts/compile.py . --review")
