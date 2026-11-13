#!/usr/bin/env python3
"""Week 28 shared drawing helpers for BOTH formats (long 16:9 and Short 9:16).

One look for the whole film: Claude-cream page, ink text, one accent. The scene is a flat landscape whose SKY
carries the argument (yellow = quick/bright, blue-grey = slow/low, grey = undecided), and a two-scale STRIP
(HAPPY-SAD across, STRONG-WEAK up) that is the film's method (Palmer et al. 2013's two emotion dimensions).

Everything draws with real alpha blending (RGB base + RGBA overlay; text fades through a scaled mask), because an
RGBA base replaced pixels and made every fade a pop (Week 27). Colours are fixed here so both formats match.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONTS = Path("/Users/tanny/Humanitarians_AI/brutalist.art/runtime/fonts")
S = 2   # logical pixels x2: 1920x1080 -> 3840x2160, 1080x1920 -> 2160x3840

PAGE, CARD, BORDER = "#FAF9F5", "#FFFFFF", "#E5E2D9"
INK, INK_SOFT, GHOST, SPARK, SEND = "#3D3929", "#73705F", "#A9A491", "#D97757", "#C6613F"
SPARK_TEXT = "#B5532F"          # 4.7:1 on cream, for small accent text

# The three skies. Illustration colours made for the film, not data.
SKY_YELLOW = "#F2C230"          # saturated, light, yellow  (quick, major)
SKY_BLUEGREY = "#5E7690"        # desaturated, dark, blue   (slow, minor)
SKY_GREY = "#B9B8B2"            # undecided
HILL = ["#A5A397", "#85847A", "#66655D"]   # neutral warm greys: do not bias the sky
SWATCH_LIGHT_YELLOW = "#F7E39A"
SWATCH_DARK_GREY = "#4A4A47"
SWATCH_DARK_CYAN = "#1F6F78"
SWATCH_BLACK = "#1B1B1A"


def hex2rgb(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def mix(a, b, t):
    t = max(0.0, min(1.0, t))
    a, b = hex2rgb(a), hex2rgb(b)
    return "#%02x%02x%02x" % tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def sky_color(yellow=0.0, blue=0.0):
    """Sky colour from how yellow / how blue-grey it is (0..1 each); grey when both are 0."""
    c = SKY_GREY
    c = mix(c, SKY_YELLOW, yellow)
    return mix(c, SKY_BLUEGREY, blue)


_fc = {}
def F(kind, size):
    key = (kind, size)
    if key not in _fc:
        p = {"serif": FONTS / "EB_Garamond/static/EBGaramond-Regular.ttf",
             "serifi": FONTS / "EB_Garamond/static/EBGaramond-Italic.ttf",
             "serifm": FONTS / "EB_Garamond/static/EBGaramond-Medium.ttf",
             "sans": FONTS / "Inter/static/Inter_28pt-Regular.ttf",
             "sansm": FONTS / "Inter/static/Inter_28pt-Medium.ttf"}[kind]
        _fc[key] = ImageFont.truetype(str(p), round(size * S))
    return _fc[key]


def rgba(c, a=1.0):
    c = hex2rgb(c) if isinstance(c, str) else tuple(c)[:3]
    return c + (int(255 * max(0.0, min(1.0, a))),)


class Canvas:
    """RGB base + RGBA drawing; every primitive honours cv.alpha; logs the text it draws (for on-screen checks)."""

    def __init__(self, w, h, min_sans=24):
        self.w, self.h, self.min_sans = w, h, min_sans
        self.im = Image.new("RGB", (w * S, h * S), PAGE)
        self.d = ImageDraw.Draw(self.im, "RGBA")
        self.alpha = 1.0
        self.log = []   # (text, size, alpha, x, y)

    def tw(self, s, kind, size):
        return F(kind, size).getlength(s) / S

    def text(self, x, y, s, kind="sans", size=24, fill=INK, anchor="la"):
        if kind.startswith("sans"):
            assert size >= self.min_sans, f"type below {self.min_sans}px: {s!r} at {size}"
        if self.alpha <= 0.01:
            return
        if fill == SPARK:
            fill = SPARK_TEXT if size < 48 else SEND
        self.log.append((s, size, round(self.alpha, 2), x, y))
        font = F(kind, size)
        l, t_, r, b = font.getbbox(s, anchor=anchor)
        pad = 3
        mask = Image.new("L", (r - l + 2 * pad, b - t_ + 2 * pad), 0)
        ImageDraw.Draw(mask).text((-l + pad, -t_ + pad), s, font=font, fill=255, anchor=anchor)
        a = max(0.0, min(1.0, self.alpha))
        if a < 0.999:
            mask = mask.point(lambda v: int(v * a))
        self.im.paste(rgba(fill)[:3], (int(round(x * S + l - pad)), int(round(y * S + t_ - pad))), mask)

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        if self.alpha <= 0.01:
            return
        box = (x0 * S, y0 * S, x1 * S, y1 * S)
        f = rgba(fill, self.alpha) if fill else None
        o = rgba(outline, self.alpha) if outline else None
        if r:
            self.d.rounded_rectangle(box, radius=r * S, fill=f, outline=o, width=round(width * S))
        else:
            self.d.rectangle(box, fill=f, outline=o, width=round(width * S))

    def line(self, pts, fill=INK, width=2):
        if self.alpha > 0.01:
            self.d.line([(x * S, y * S) for x, y in pts], fill=rgba(fill, self.alpha), width=round(width * S), joint="curve")

    def ellipse(self, cx, cy, rx, ry=None, fill=None, outline=None, width=1):
        if self.alpha <= 0.01:
            return
        ry = rx if ry is None else ry
        self.d.ellipse([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S],
                       fill=rgba(fill, self.alpha) if fill else None,
                       outline=rgba(outline, self.alpha) if outline else None, width=round(width * S))

    def poly(self, pts, fill):
        if self.alpha > 0.01:
            self.d.polygon([(x * S, y * S) for x, y in pts], fill=rgba(fill, self.alpha))

    def save(self, path):
        self.im.save(path)


# ----------------------------------------------------------------------------- the landscape

def landscape(cv, x0, y0, x1, y1, sky, cloud_phase=0.0, clouds=True, label=None):
    """Flat landscape in the box, clipped to it. `sky` is a hex colour. Clouds are lighter blobs that drift with
    cloud_phase (0..1+). Drawn on a temporary canvas and pasted, so nothing spills over the box edge."""
    if cv.alpha <= 0.01:
        return
    w, h = x1 - x0, y1 - y0
    tmp = Canvas(w, h)
    tmp.rect(0, 0, w, h, fill=sky)
    if clouds:
        light = mix(sky, "#FFFFFF", 0.38)
        for i, (fx, fy, fw) in enumerate([(0.18, 0.22, 0.16), (0.55, 0.14, 0.20), (0.82, 0.30, 0.13)]):
            cx = ((fx + cloud_phase * (0.5 + 0.25 * i)) % 1.2 - 0.1) * w
            cy = fy * h
            for dx, dy, k in [(0, 0, 1.0), (-0.45, 0.25, 0.7), (0.5, 0.2, 0.75)]:
                tmp.ellipse(cx + dx * fw * w, cy + dy * fw * h * 0.4, fw * w * 0.5 * k, fw * h * 0.5 * k * 0.55, fill=light)
    base = h * 0.58
    for li, (amp, ph, col) in enumerate([(0.07, 0.0, HILL[0]), (0.06, 1.7, HILL[1]), (0.05, 3.1, HILL[2])]):
        top = base + li * h * 0.11
        pts = [(0, h)]
        n = 48
        for k in range(n + 1):
            xx = w * k / n
            yy = top - h * amp * (0.55 + 0.45 * math.sin(k / n * 6.28 * (1 + li * 0.5) + ph))
            pts.append((xx, min(yy, h)))
        pts.append((w, h))
        tmp.poly(pts, col)
    box = (int(round(x0 * S)), int(round(y0 * S)))
    if cv.alpha < 0.999:
        region = cv.im.crop((box[0], box[1], box[0] + tmp.im.width, box[1] + tmp.im.height))
        tmp.im = Image.blend(region, tmp.im, cv.alpha)
    cv.im.paste(tmp.im, box)
    if label:
        cv.text(x0 + 18, y0 + 14, label, "sansm", 28, fill=INK)


# ----------------------------------------------------------------------------- the strip (the method)

def strip(cv, x0, y0, size, music=None, color=None, show_labels=True, label_px=28, dim=1.0, note=None):
    """The two-scale strip: HAPPY-SAD across (SAD left, HAPPY right), STRONG-WEAK up (STRONG top).
    music / color are (x, y) in [-1, 1] or None. Returns the pixel position of each dot."""
    a0 = cv.alpha
    cv.alpha = a0 * dim
    cv.rect(x0, y0, x0 + size, y0 + size, fill=CARD, outline=BORDER, width=2, r=10)
    cx, cy = x0 + size / 2, y0 + size / 2
    cv.line([(x0 + 14, cy), (x0 + size - 14, cy)], fill=BORDER, width=2)
    cv.line([(cx, y0 + 14), (cx, y0 + size - 14)], fill=BORDER, width=2)
    pos = {}
    pad = size * 0.12

    def at(p):
        return (cx + p[0] * (size / 2 - pad), cy - p[1] * (size / 2 - pad))

    if show_labels:
        cv.text(x0 + size / 2, y0 - 12, "STRONG", "sansm", label_px, fill=INK_SOFT, anchor="ms")
        cv.text(x0 + size / 2, y0 + size + label_px + 8, "WEAK", "sansm", label_px, fill=INK_SOFT, anchor="ms")
        cv.text(x0 - 12, cy + label_px * 0.35, "SAD", "sansm", label_px, fill=INK_SOFT, anchor="rs")
        cv.text(x0 + size + 12, cy + label_px * 0.35, "HAPPY", "sansm", label_px, fill=INK_SOFT, anchor="ls")
    if color is not None:
        px, py = at(color)
        cv.ellipse(px, py, size * 0.052, fill=SPARK, outline=INK, width=2)
        pos["color"] = (px, py)
    if music is not None:
        px, py = at(music)
        cv.ellipse(px, py, size * 0.052, fill=INK)
        pos["music"] = (px, py)
    if note:
        cv.text(x0 + size / 2, y0 + size + label_px * 2.4, note, "sans", label_px, fill=INK_SOFT, anchor="ms")
    cv.alpha = a0
    return pos


def swatch(cv, x, y, w, h, color, label=None, label_px=26, outline=True):
    cv.rect(x, y, x + w, y + h, fill=color, outline=BORDER if outline else None, width=2, r=6)
    if label:
        cv.text(x + w / 2, y + h + label_px + 6, label, "sans", label_px, fill=INK_SOFT, anchor="ms")


def source_line(cv, x, y, s, size=26):
    cv.text(x, y, s, "sans", size, fill=INK_SOFT)
