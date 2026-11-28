#!/usr/bin/env python3
"""Claude-palette chart plates for The Loud Quiet. — 16:9 and 9:16, not photographs."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PAGE, INK, SOFT, SPARK, BORDER = "#FAF9F5", "#3D3929", "#73705F", "#D97757", "#E5E2D9"
ART = Path("/Users/komalganapathy/Desktop/brutalist.art/runtime/fonts/EB_Garamond/static")
SERIF = str(ART / "EBGaramond-Medium.ttf")
SERIF_I = str(ART / "EBGaramond-Italic.ttf")
SANS = "/System/Library/Fonts/Avenir Next.ttc"
OUT = Path(__file__).resolve().parents[1]


def font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except OSError:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", size)


def text(draw, xy, s, f, fill=INK, anchor="lt"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)


def plate(w, h):
    im = Image.new("RGB", (w, h), PAGE)
    d = ImageDraw.Draw(im)
    return im, d


def header(d, w, y, kicker, title, sub, sizes):
    fk, ft, fs = (font(SANS, sizes[0], 1), font(SERIF, sizes[1]), font(SERIF, sizes[2]))
    text(d, (w * 0.08, y), kicker.upper(), fk, SOFT)
    text(d, (w * 0.08, y + sizes[0] * 1.8), title, ft, INK)
    text(d, (w * 0.08, y + sizes[0] * 1.8 + sizes[1] * 1.15), sub, fs, SOFT)
    return y + sizes[0] * 1.8 + sizes[1] * 1.15 + sizes[2] * 1.6


def footer(d, w, h, source, falsifier, sizes):
    ff, fi = font(SANS, sizes[0], 1), font(SERIF_I, sizes[1])
    d.line((w * 0.08, h * 0.90, w * 0.92, h * 0.90), fill=BORDER, width=3)
    text(d, (w * 0.08, h * 0.925), source, ff, SOFT)
    text(d, (w * 0.08, h * 0.96), falsifier, fi, SPARK)


def vbars(path, w, h, kicker, title, sub, rows, source, falsifier, accent=0):
    """rows: list of (label, value, display)"""
    im, d = plate(w, h)
    s = (int(h * 0.018), int(h * 0.055), int(h * 0.028)) if w > h else (int(w * 0.028), int(w * 0.072), int(w * 0.036))
    top = header(d, w, h * 0.07, kicker, title, sub, s)
    max_v = max(r[1] for r in rows) or 1
    n = len(rows)
    plot_t, plot_b = top + h * 0.04, h * 0.82
    plot_l, plot_r = w * 0.10, w * 0.90
    gap = (plot_r - plot_l) / n
    bar_w = gap * (0.72 if n <= 2 else 0.50)
    fl = font(SANS, int(h * 0.022), 1)
    fv = font(SERIF, int(h * 0.038))
    for i, (label, value, display) in enumerate(rows):
        x = plot_l + i * gap + (gap - bar_w) / 2
        bh = (value / max_v) * (plot_b - plot_t) * 0.92
        y = plot_b - bh
        d.rectangle([x, y, x + bar_w, plot_b], fill=SPARK if i == accent else INK)
        text(d, (x + bar_w / 2, y - h * 0.018), display, fv, INK, "mb")
        # wrap label
        words = label.split()
        ly = plot_b + h * 0.018
        for line in ([" ".join(words[:2]), " ".join(words[2:])] if len(words) > 2 else [label]):
            if line:
                text(d, (x + bar_w / 2, ly), line.upper(), fl, SPARK if i == accent else INK, "mt")
                ly += int(h * 0.024)
    d.rectangle([plot_l, plot_b, plot_r, plot_b + 3], fill=INK)
    footer(d, w, h, source, falsifier, (int(h * 0.016), int(h * 0.024)))
    im.save(path)
    print("wrote", path, im.size)


def hbars(path, w, h, kicker, title, sub, rows, source, falsifier, accent=0):
    im, d = plate(w, h)
    s = (int(w * 0.032), int(w * 0.070), int(w * 0.034))
    top = header(d, w, h * 0.06, kicker, title, sub, s)
    max_v = max(r[1] for r in rows) or 1
    n = len(rows)
    plot_t, plot_b = top + h * 0.02, h * 0.82
    plot_l, plot_r = w * 0.10, w * 0.90
    row_h = (plot_b - plot_t) / n
    fl = font(SANS, int(w * 0.032), 1)
    fv = font(SERIF, int(w * 0.048))
    for i, (label, value, display) in enumerate(rows):
        y0 = plot_t + i * row_h
        text(d, (plot_l, y0 + row_h * 0.12), label.upper(), fl, SPARK if i == accent else INK)
        bar_top = y0 + row_h * 0.38
        bar_h = row_h * 0.32
        bw = (value / max_v) * (plot_r - plot_l) * 0.92
        d.rectangle([plot_l, bar_top, plot_l + bw, bar_top + bar_h], fill=SPARK if i == accent else INK)
        text(d, (plot_l + bw + w * 0.02, bar_top + bar_h / 2), display, fv, INK, "lm")
    footer(d, w, h, source, falsifier, (int(w * 0.022), int(w * 0.032)))
    im.save(path)
    print("wrote", path, im.size)


def two_number(path, w, h, kicker, title, sub, left, right, delta, source, falsifier):
    im, d = plate(w, h)
    portrait = h > w
    s = (int((h if not portrait else w) * (0.018 if not portrait else 0.032)),
         int((h if not portrait else w) * (0.055 if not portrait else 0.070)),
         int((h if not portrait else w) * (0.028 if not portrait else 0.034)))
    header(d, w, h * 0.07, kicker, title, sub, s)
    fn = font(SERIF, int(h * 0.14 if not portrait else w * 0.16))
    fy = font(SANS, int(h * 0.028 if not portrait else w * 0.040), 1)
    fd = font(SERIF_I, int(h * 0.045 if not portrait else w * 0.055))
    if portrait:
        cx, y1, y2 = w / 2, h * 0.38, h * 0.62
        text(d, (cx, y1), left[1], fn, INK, "mm")
        text(d, (cx, y1 + h * 0.07), left[0].upper(), fy, SOFT, "mt")
        text(d, (cx, (y1 + y2) / 2), delta, fd, SPARK, "mm")
        text(d, (cx, y2), right[1], fn, SPARK, "mm")
        text(d, (cx, y2 + h * 0.07), right[0].upper(), fy, SPARK, "mt")
    else:
        text(d, (w * 0.24, h * 0.50), left[1], fn, INK, "mm")
        text(d, (w * 0.24, h * 0.64), left[0].upper(), fy, SOFT, "mt")
        text(d, (w * 0.50, h * 0.46), "→", fd, SPARK, "mm")
        text(d, (w * 0.50, h * 0.54), delta.replace("→  ", ""), fd, SPARK, "mm")
        text(d, (w * 0.76, h * 0.50), right[1], fn, SPARK, "mm")
        text(d, (w * 0.76, h * 0.64), right[0].upper(), fy, SPARK, "mt")
    footer(d, w, h, source, falsifier, (int((h if not portrait else w) * (0.016 if not portrait else 0.022)),
                                        int((h if not portrait else w) * (0.024 if not portrait else 0.032))))
    im.save(path)
    print("wrote", path, im.size)


def main():
    searches = [
        ("old-money style", 25000, "25,000"),
        ("quiet luxury", 6100, "6,100"),
        ("stealth wealth", 2200, "2,200"),
    ]
    listen = [
        ("reputation", 77, "77%"),
        ("awareness", 52, "52%"),
    ]
    src1 = "Karen Millen via Robb Report · 20 Apr 2023 · monthly Google searches"
    fal1 = "A search is not a sale."
    src2 = "Bain & Company / Altagamma · 18 Nov 2026 · personal luxury goods"
    fal2 = "Loud talk is not more shoppers."
    src3 = "Meltwater · State of Social 2025 · among teams that already listen"
    fal3 = "Listening is not a verdict on quiet."

    vbars(OUT / "media/B02.png", 3840, 2160, "chart 1 · volume", "Three searches. One month.",
          "Monthly Google searches after Succession S4.", searches, src1, fal1, accent=1)
    hbars(OUT / "pantry/B02-916.png", 2160, 3840, "chart 1 · volume", "Three searches.",
          "Monthly Google searches after Succession S4.", searches, src1, fal1, accent=1)
    two_number(OUT / "media/B03.png", 3840, 2160, "chart 2 · shoppers", "The talk stayed. The count did not.",
               "Personal luxury goods consumer base.",
               ("2025", "330M"), ("2026", "315M"), "→  about 15 million fewer", src2, fal2)
    two_number(OUT / "pantry/B03-916.png", 2160, 3840, "chart 2 · shoppers", "The count moved.",
               "Personal luxury goods consumer base.",
               ("2025", "330M"), ("2026", "315M"), "→  about 15 million fewer", src2, fal2)
    vbars(OUT / "media/B04.png", 3840, 2160, "chart 3 · why they listen", "Reputation first. Then awareness.",
          "Share of listening teams naming each goal.", listen, src3, fal3, accent=0)
    hbars(OUT / "pantry/B04-916.png", 2160, 3840, "chart 3 · why they listen", "Why they listen.",
          "Share of listening teams naming each goal.", listen, src3, fal3, accent=0)
    for name in ("B02", "B03", "B04"):
        (OUT / "pantry" / f"{name}.png").write_bytes((OUT / "media" / f"{name}.png").read_bytes())


if __name__ == "__main__":
    main()
