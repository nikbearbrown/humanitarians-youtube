"""Compose the B02 evidence plate for claude-sai-what-it-stopped-needing.

B02 shows clauding's entire interface: three menu bar states. There is no
screenshot to use, so the plate is a RENDERING — and it says so on its own face.
Nothing here is eyeballed:

  * the spark is the app's own asset, data/spark.png, extracted from
    src/clauding/logo.py (a 60x60 alpha mask, tinted at runtime exactly as
    bar.py does it rather than shipped once per colour);
  * the three strings are transcribed character-for-character from README.md
    and from bar_text() in bar.py;
  * the two colours are the literal constants in bar.py --
    BRAND_ORANGE (0.851, 0.467, 0.341) and AMBER (0.95, 0.73, 0.18) --
    and the idle tint is bar.py's resting colour, black at 55% alpha on a
    light bar.

Run under the ANACONDA python3, which has Pillow. The .venv does not.
(The audio step is the reverse: .venv/bin/python has kokoro_onnx, this one
does not.)

    python3 make_plates.py

Writes media/B02.png (3840x2160) and pantry/B02-916.png (2160x3840).
"""

from PIL import Image, ImageDraw, ImageFont

GROUND = (250, 249, 245)        # #FAF9F5, the Claude cream
INK = (41, 37, 36)              # warm near-black
MUTE = (120, 113, 108)          # caption / secondary
RULE = (222, 218, 210)

BRAND_ORANGE = (217, 119, 87)   # bar.py:50  (0.851, 0.467, 0.341)
AMBER = (242, 186, 46)          # bar.py:51  (0.95, 0.73, 0.18)
IDLE_TINT = (41, 37, 36, 140)   # bar.py:146 colorWithWhite(0.0, alpha 0.55)

FONT = "/System/Library/Fonts/SFNS.ttf"
FONT_FALLBACK = "/System/Library/Fonts/HelveticaNeue.ttc"

# state label, icon kind, the literal bar text
STATES = [
    ("idle",     "spark", "Opus 5 · xhigh",            "nothing running"),
    ("clauding", "spark", "Clauding… Opus 5 · xhigh",  "a turn is in progress"),
    ("waiting",  "dot",   "Waiting for input",         "Claude needs you"),
]


def font(px):
    try:
        return ImageFont.truetype(FONT, px)
    except OSError:
        return ImageFont.truetype(FONT_FALLBACK, px)


def spark(size, rgba):
    """The app's alpha mask, filled with one colour — bar.py's _tinted()."""
    mask = Image.open("data/spark.png").convert("RGBA").resize(
        (size, size), Image.LANCZOS
    ).split()[-1]
    layer = Image.new("RGBA", (size, size), rgba)
    layer.putalpha(mask)
    return layer


def dot(size, rgb):
    """A filled circle, for the state where the spark would understate things."""
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    pad = size * 0.18
    d.ellipse([pad, pad, size - pad, size - pad], fill=rgb + (255,))
    return layer


def plate(W, H, *, portrait):
    im = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(im)

    if portrait:
        icon_px, text_px, label_px, cap_px = 150, 132, 76, 62
        left, row_h, top = int(W * 0.10), int(H * 0.200), int(H * 0.255)
        gutter = int(W * 0.10)
        label_above = True
    else:
        icon_px, text_px, label_px, cap_px = 132, 116, 68, 56
        left, row_h, top = int(W * 0.215), int(H * 0.200), int(H * 0.265)
        gutter = int(W * 0.075)
        label_above = False

    f_text, f_label, f_cap = font(text_px), font(label_px), font(cap_px)
    f_spark = font(int(cap_px * 0.95))

    # header
    d.text((gutter, int(H * 0.090)), "CLAUDING 1.0.0 · THE ENTIRE INTERFACE",
           font=f_spark, fill=MUTE)
    rule_y = int(H * 0.090) + cap_px * 1.9
    d.line([(gutter, rule_y), (W - gutter, rule_y)], fill=RULE, width=3)

    for i, (label, kind, text, gloss) in enumerate(STATES):
        y = top + i * row_h
        accent = {"idle": IDLE_TINT[:3], "clauding": BRAND_ORANGE, "waiting": AMBER}[label]

        if label_above:
            d.text((left, y - label_px * 1.5), label.upper(), font=f_label, fill=accent)
            x = left
        else:
            # right-align the state name into its own column
            w = d.textlength(label.upper(), font=f_label)
            d.text((left - w - int(W * 0.035), y + (icon_px - label_px) * 0.62),
                   label.upper(), font=f_label, fill=accent)
            x = left

        icon = spark(icon_px, IDLE_TINT) if label == "idle" else (
            spark(icon_px, BRAND_ORANGE + (255,)) if kind == "spark" else dot(icon_px, AMBER)
        )
        im.paste(icon, (x, y), icon)

        d.text((x + icon_px + int(icon_px * 0.34), y + (icon_px - text_px) * 0.46),
               text, font=f_text, fill=INK)
        d.text((x + icon_px + int(icon_px * 0.34), y + icon_px * 1.06),
               gloss, font=f_cap, fill=MUTE)

    foot = ("A RENDERING, NOT A SCREENSHOT — the three strings are transcribed from "
            "README.md and bar_text() in bar.py;")
    foot2 = ("the mark is the app's own 60×60 asset from logo.py, tinted with bar.py's "
             "own colour constants.")
    if portrait:
        foot = "A RENDERING, NOT A SCREENSHOT."
        foot2 = "Strings, mark and colours are the app's own."
    foot_y = H - int(H * 0.150)
    d.line([(gutter, foot_y - cap_px * 1.1), (W - gutter, foot_y - cap_px * 1.1)],
           fill=RULE, width=3)
    d.text((gutter, foot_y), foot, font=f_cap, fill=MUTE)
    d.text((gutter, foot_y + cap_px * 1.55), foot2, font=f_cap, fill=MUTE)
    return im


def main():
    plate(3840, 2160, portrait=False).save("media/B02.png")
    plate(2160, 3840, portrait=True).save("pantry/B02-916.png")
    print("wrote media/B02.png (3840x2160)")
    print("wrote pantry/B02-916.png (2160x3840)")


if __name__ == "__main__":
    main()
