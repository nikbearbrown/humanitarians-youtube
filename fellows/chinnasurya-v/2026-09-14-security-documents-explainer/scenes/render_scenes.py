#!/usr/bin/env python3
"""Per-script renderer — How a Canvas Launch Works (LTI 1.3).

Unique state PNGs -> hard-linked frame sequence -> frame-exact mp4.
Hard cuts only; no interpolation between states.
"""
import argparse, json, os, shutil, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FPS = 24
GROUND, PAPER = (0x0A, 0x0A, 0x0A), (0xF2, 0xF0, 0xEB)
SIGNAL, MUTE  = (0xE8, 0x45, 0x2C), (0x6B, 0x6B, 0x6B)


def find_font(cands):
    for path, idx in cands:
        if Path(path).exists():
            return path, idx
    raise SystemExit(f"no font found among {[c[0] for c in cands]}")

DISPLAY = find_font([("/System/Library/Fonts/HelveticaNeue.ttc", 1),
                     ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 0),
                     ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 0)])
MONO    = find_font([("/System/Library/Fonts/Menlo.ttc", 0),
                     ("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", 0),
                     ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 0)])
MONOB   = find_font([("/System/Library/Fonts/Menlo.ttc", 1),
                     ("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 0),
                     ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 0)])


def F(spec, size):
    return ImageFont.truetype(spec[0], int(size), index=spec[1])


def fit(spec, size, text, maxw, tracking=0.0):
    """Shrink until it fits maxw. Overflow is a gate-V blocker, so never risk it."""
    s = int(size)
    while s > 14:
        f = F(spec, s)
        w = sum(f.getlength(c) + tracking * s for c in text)
        if w <= maxw:
            return f
        s = int(s * 0.94)
    return F(spec, 14)


def blend(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

GRIDC = blend(GROUND, MUTE, 0.12)


class Layout:
    """12 columns. Margins sit OUTSIDE the gate-V title-safe inset."""
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.portrait = h > w
        ref = 1080.0 if self.portrait else 1920.0
        self.mx = int((54 if self.portrait else 96) * (w / ref)) + 60
        self.my = int((96 if self.portrait else 54) * (w / ref)) + 60
        self.gutter = 72 if self.portrait else 120
        self.cols = 12
        inner = w - 2 * self.mx
        self.col = (inner - self.gutter * (self.cols - 1)) / self.cols
        s = 1.18 if self.portrait else 1.0
        self.display = int(280 * s * (0.70 if self.portrait else 1))
        self.h1      = int(200 * s)
        self.h2      = int(140 * s)
        self.body    = int(108 * s)
        self.data    = int(88 * s)
        self.caption = int(62 * s)

    def x(self, c):    return self.mx + c * (self.col + self.gutter)
    def span(self, n): return n * self.col + (n - 1) * self.gutter
    @property
    def right(self):  return self.w - self.mx
    @property
    def bottom(self): return self.h - self.my


def frame(L, grid=True):
    img = Image.new("RGB", (L.w, L.h), GROUND)
    d = ImageDraw.Draw(img)
    if grid:
        for c in range(L.cols + 1):
            x = int(L.mx + c * (L.col + L.gutter) - (L.gutter / 2 if c else 0))
            if L.mx <= x <= L.right:
                d.rectangle([x, L.my, x + 2, L.bottom], fill=GRIDC)
    return img, d


def track(d, xy, text, font, fill, tracking=-0.02):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + tracking * font.size
    return x


def box(d, x0, y0, x1, y1, color, wd=6):
    d.rectangle([x0, y0, x1, y0 + wd], fill=color)
    d.rectangle([x0, y1 - wd, x1, y1], fill=color)
    d.rectangle([x0, y0, x0 + wd, y1], fill=color)
    d.rectangle([x1 - wd, y0, x1, y1], fill=color)


def arrow(d, x0, x1, y, color, wd=8, head=34):
    right = x1 > x0
    sx, ex = (x0, x1 - head) if right else (x0, x1 + head)
    d.rectangle([min(sx, ex), y - wd // 2, max(sx, ex), y + wd // 2], fill=color)
    if right:
        d.polygon([(x1, y), (x1 - head, y - head * 0.62), (x1 - head, y + head * 0.62)], fill=color)
    else:
        d.polygon([(x1, y), (x1 + head, y - head * 0.62), (x1 + head, y + head * 0.62)], fill=color)


def rule(d, L, y, color=MUTE, wd=8, x0=None, x1=None):
    d.rectangle([x0 or L.mx, y, x1 or L.right, y + wd], fill=color)


def marker(d, x, y, size, color):
    d.rectangle([x, y, x + size, y + size], fill=color)


def footer(d, L, text):
    rule(d, L, L.bottom - 92, MUTE, 6)
    d.text((L.mx, L.bottom - 70), text, font=F(MONO, L.caption), fill=MUTE)


def head(d, L, kicker, y=None):
    y = L.my if y is None else y
    rule(d, L, y, SIGNAL, 12)
    d.text((L.mx, y + 34), kicker, font=F(MONOB, L.caption), fill=MUTE)
    return y + 34 + L.caption + 46


def stations(d, L, y, lit, labels):
    """Four handshake stations; the active one in signal, the rest mute."""
    n = len(labels)
    gap = 46
    wpx = (L.right - L.mx - gap * (n - 1)) / n
    for i, lab in enumerate(labels):
        x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
        on = (i == lit)
        col = SIGNAL if on else MUTE
        if on:
            d.rectangle([x0, y, x1, y + 170], fill=SIGNAL)
        else:
            box(d, x0, y, x1, y + 170, MUTE, 5)
        f = fit(MONOB, L.data, lab, wpx - 56)
        d.text((x0 + 32, y + 170 // 2 - f.size * 0.72),
               lab, font=f, fill=GROUND if on else col)
    return y + 170 + 60




# ─────────────────────────────────────────────────────────────── scenes ──\n
def EL(weight=1):
    return ("el", weight)


def zone(L, top):
    bot = L.bottom - 150
    return bot, bot - top


def fy(top, avail, f):
    return int(top + avail * f)


def arrow_v(d, y0, y1, x, color, wd=8, hd=34):
    down = y1 > y0
    sy, ey = (y0, y1 - hd) if down else (y0, y1 + hd)
    d.rectangle([x - wd // 2, min(sy, ey), x + wd // 2, max(sy, ey)], fill=color)
    if down:
        d.polygon([(x, y1), (x - hd * 0.62, y1 - hd), (x + hd * 0.62, y1 - hd)], fill=color)
    else:
        d.polygon([(x, y1), (x - hd * 0.62, y1 + hd), (x + hd * 0.62, y1 + hd)], fill=color)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


DOCS = [("01", "SECURITY REVIEW"), ("02", "FERPA DATA FLOW"),
        ("03", "ARCHITECTURE + HOSTING"), ("04", "HECVAT LITE")]


def doccards(d, L, y, lit, h=240, small=False):
    """The four-document index. Recurs in most beats; `lit` is the active one."""
    gap = 40
    wpx = (L.right - L.mx - gap * 3) / 4
    nf = F(DISPLAY, int(h * (0.34 if not small else 0.40)))
    tf = F(MONOB, int(h * (0.155 if not small else 0.20)))
    for i, (num, title) in enumerate(DOCS):
        x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
        on = (i == lit)
        if on:
            d.rectangle([x0, y, x1, y + h], fill=SIGNAL)
            fg = GROUND
        else:
            box(d, x0, y, x1, y + h, MUTE if lit >= 0 else PAPER, 5)
            fg = MUTE if lit >= 0 else PAPER
        d.text((x0 + 26, y + 18), num, font=nf, fill=fg)
        if not small:
            ls = wrap(title, tf, wpx - 52)
            for j, ln in enumerate(ls[:2]):
                d.text((x0 + 26, y + 26 + nf.size * 1.05 + j * tf.size * 1.30),
                       ln, font=tf, fill=fg)
    return y + h + 60


def b00(L):
    def draw(st):
        img, d = frame(L)
        rule(d, L, L.my, SIGNAL, 16)
        f = fit(DISPLAY, 470, "FOUR", L.right - L.mx, -0.02)
        y = int(L.h * 0.26)
        if st >= 1: track(d, (L.mx, y), "FOUR", f, PAPER)
        if st >= 2: track(d, (L.mx, y + int(f.size * 1.20)), "DOCUMENTS", f, PAPER)
        if st >= 3:
            rule(d, L, int(L.h * 0.74), MUTE, 8)
            d.text((L.mx, int(L.h * 0.74) + 54), "WHAT THE REVIEW ASKED FOR",
                   font=F(MONOB, L.h1), fill=SIGNAL)
        footer(d, L, "getting a Canvas integration through a university security review")
        return img
    return [(6, lambda: draw(0)), (8, lambda: draw(1)), (8, lambda: draw(2)),
            (EL(6), lambda: draw(3))]


def b01(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "ONE QUESTION")
        bot, av = zone(L, y0)
        gap = 40
        wpx = (L.right - L.mx - gap * 3) / 4
        h = int(av * 0.46)
        ytop = fy(y0, av, 0.06)
        nf = F(DISPLAY, int(h * 0.34)); tf = F(MONOB, int(h * 0.145))
        for i, (num, title) in enumerate(DOCS):
            if st < i + 1:
                continue
            x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
            box(d, x0, ytop, x1, ytop + h, PAPER, 6)
            d.text((x0 + 28, ytop + 22), num, font=nf, fill=SIGNAL)
            for j, ln in enumerate(wrap(title, tf, wpx - 56)[:2]):
                d.text((x0 + 28, ytop + 30 + nf.size * 1.05 + j * tf.size * 1.3),
                       ln, font=tf, fill=PAPER)
        if st >= 5:
            ly = fy(y0, av, 0.72)
            rule(d, L, ly, SIGNAL, 14)
            d.text((L.mx, ly + 52), "EACH ANSWERS A DIFFERENT DOUBT",
                   font=F(MONOB, L.h2), fill=PAPER)
        footer(d, L, "we asked for one developer key")
        return img
    return [(8, lambda: draw(0))] + \
           [(5, (lambda s: lambda: draw(s))(i)) for i in range(1, 5)] + \
           [(EL(7), lambda: draw(5))]


def b02(L):
    ok = ["SIGNATURE", "ISS", "AUD", "EXP", "ALG PINNED"]
    fixed = ["decoded, never verified", "role check could be tricked",
             "open registration endpoint", "credentials in plain text"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "DOCUMENT ONE · THE SECURITY REVIEW")
        y = doccards(d, L, y0, 0)
        bot, av = zone(L, y)
        cx = 1980
        d.text((L.mx, fy(y, av, 0.0)), "WHAT IT VERIFIES", font=F(MONOB, L.data), fill=PAPER)
        d.text((cx,   fy(y, av, 0.0)), "WHAT IT ADMITS", font=F(MONOB, L.data), fill=SIGNAL)
        for i, t in enumerate(ok):
            if st >= 1:
                yy = fy(y, av, 0.17 + i * 0.155)
                marker(d, L.mx, yy + 14, 44, MUTE)
                d.text((L.mx + 96, yy), t, font=F(MONO, L.body), fill=PAPER)
        for i, t in enumerate(fixed):
            if st >= i + 2:
                yy = fy(y, av, 0.17 + i * 0.155)
                marker(d, cx, yy + 14, 44, SIGNAL)
                d.text((cx + 96, yy), t, font=fit(MONO, L.body, t, 1400), fill=PAPER)
        footer(d, L, "found and fixed — not only what is right")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1))] + \
           [(5, (lambda s: lambda: draw(s))(i)) for i in range(2, 5)] + \
           [(EL(7), lambda: draw(5))]


def b03(L):
    rows = [("user identifier", "account matching", "relationship"),
            ("role", "authorization level", "relationship"),
            ("nonce", "replay defence", "10 MIN"),
            ("launch record", "audit", "1 HR")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "DOCUMENT TWO · FERPA DATA FLOW")
        y = doccards(d, L, y0, 1)
        bot, av = zone(L, y)
        c1, c2, c3 = L.mx, 1620, 2980
        hf = F(MONOB, L.data)
        d.text((c1, fy(y, av, 0.0)), "RECEIVED", font=hf, fill=SIGNAL)
        d.text((c2, fy(y, av, 0.0)), "WHY", font=hf, fill=SIGNAL)
        d.text((c3, fy(y, av, 0.0)), "KEPT FOR", font=hf, fill=SIGNAL)
        for i, (a, b_, c) in enumerate(rows):
            if st < i + 1:
                continue
            yy = fy(y, av, 0.18 + i * 0.15)
            d.text((c1, yy), a, font=fit(MONO, L.body, a, 1280), fill=PAPER)
            d.text((c2, yy), b_, font=fit(MONO, L.body, b_, 1280), fill=MUTE)
            d.text((c3, yy), c, font=fit(MONOB, L.body, c, L.right - c3),
                   fill=SIGNAL if c != "relationship" else MUTE)
        if st >= 5:
            sy = fy(y, av, 0.82)
            rule(d, L, sy, MUTE, 6)
            gap = 26
            wpx = (L.right - L.mx - gap * 5) / 6
            for i in range(6):
                x0 = int(L.mx + i * (wpx + gap))
                on = (i == 3)
                if on:
                    d.rectangle([x0, sy + 46, int(x0 + wpx), sy + 148], fill=SIGNAL)
                    d.text((x0 + 20, sy + 76), "NO IDS", font=F(MONOB, L.caption), fill=GROUND)
                else:
                    box(d, x0, sy + 46, int(x0 + wpx), sy + 148, MUTE, 5)
            d.text((L.mx, sy + 172), "SIX SUBPROCESSORS — EACH WITH WHAT IT RECEIVES",
                   font=F(MONO, L.caption), fill=MUTE)
        footer(d, L, "school official · 34 CFR 99.31(a)(1)")
        return img
    return [(10, lambda: draw(0))] + \
           [(5, (lambda s: lambda: draw(s))(i)) for i in range(1, 5)] + \
           [(EL(8), lambda: draw(5))]


def b04(L):
    path = ["CANVAS", "TLS TERMINATION", "THE HUB", "DATABASE"]
    vals = [("RPO", "2 MIN"), ("SEGMENTS", "105"), ("FAILURES", "0")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "DOCUMENT THREE · ARCHITECTURE + HOSTING")
        y = doccards(d, L, y0, 2)
        bot, av = zone(L, y)
        bw = 1500
        for i, p in enumerate(path):
            t0 = fy(y, av, 0.02 + i * 0.25)
            t1 = fy(y, av, 0.02 + i * 0.25 + 0.15)
            box(d, L.mx, t0, L.mx + bw, t1, PAPER, 6)
            d.text((L.mx + 44, (t0 + t1) / 2 - L.data * 0.72), p,
                   font=F(MONOB, L.data), fill=PAPER)
            if i < 3:
                arrow_v(d, t1 + 12, fy(y, av, 0.02 + (i + 1) * 0.25) - 12,
                        L.mx + 200, MUTE, 8, 30)
        if st >= 1:
            for i, (k, v) in enumerate(vals):
                yy = fy(y, av, 0.10 + i * 0.28)
                d.text((2200, yy), k, font=F(MONO, L.caption), fill=MUTE)
                d.text((2200, yy + 56), v,
                       font=fit(MONOB, L.h1, v, L.right - 2200), fill=SIGNAL)
        if st >= 2:
            txt = "MEASURED — NOT PROMISED"
            d.text((2200, fy(y, av, 0.88)), txt,
                   font=fit(MONOB, L.body, txt, L.right - 2200), fill=PAPER)
        footer(d, L, "continuous write-ahead-log archiving, read from the database")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1)), (EL(6), lambda: draw(2))]


def b05(L):
    secs = ["PRODUCT", "DATA + PRIVACY", "ENCRYPTION", "ACCESS CONTROL",
            "APP SECURITY", "AI / LLM", "INFRASTRUCTURE"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "DOCUMENT FOUR · HECVAT LITE")
        y = doccards(d, L, y0, 3)
        bot, av = zone(L, y)
        for i, t in enumerate(secs):
            if st < i + 1:
                continue
            col, row = divmod(i, 4)
            x = L.mx if col == 0 else 1980
            yy = fy(y, av, 0.02 + row * 0.20)
            marker(d, x, yy + 14, 46, SIGNAL if col == 0 else MUTE)
            d.text((x + 100, yy), t, font=F(MONOB, L.body), fill=PAPER)
        if st >= 8:
            ly = fy(y, av, 0.86)
            rule(d, L, ly, SIGNAL, 12)
            d.text((L.mx, ly + 48), "A STANDARD FORM — YOU DO NOT PICK THE QUESTIONS",
                   font=fit(MONOB, L.h2, "A STANDARD FORM — YOU DO NOT PICK THE QUESTIONS",
                            L.right - L.mx), fill=PAPER)
        footer(d, L, "the questionnaire every vendor gets")
        return img
    return [(8, lambda: draw(0))] + \
           [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 8)] + \
           [(EL(7), lambda: draw(8))]


def b06(L):
    answers = [("SOC 2", "NO"), ("THIRD-PARTY PEN TEST", "NONE"),
               ("ADMIN MFA", "CONFIRMING")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE ANSWERS THAT SAY NO")
        bot, av = zone(L, y0)
        for i, (k, v) in enumerate(answers):
            if st < i + 1:
                continue
            t0 = fy(y0, av, 0.02 + i * 0.262)
            t1 = fy(y0, av, 0.02 + i * 0.262 + 0.225)
            bh = t1 - t0
            box(d, L.mx, t0, L.right, t1, SIGNAL, 7)
            d.text((L.mx + 56, t0 + int(bh * 0.10)), k, font=F(MONOB, L.data), fill=MUTE)
            # Answer must sit INSIDE the box: size from box height, not a constant.
            f = fit(DISPLAY, int(bh * 0.44), v, L.right - L.mx - 130, -0.02)
            track(d, (L.mx + 56, t0 + int(bh * 0.42)), v, f, SIGNAL)
        if st >= 4:
            ly = fy(y0, av, 0.86)
            rule(d, L, ly, PAPER, 10)
            d.text((L.mx, ly + 50), "ALL YES IS NOT A GOOD SIGN",
                   font=F(MONOB, L.h2), fill=PAPER)
        footer(d, L, "a questionnaire answered entirely in the affirmative is an unread one")
        return img
    return [(8, lambda: draw(0)), (6, lambda: draw(1)), (6, lambda: draw(2)),
            (EL(8), lambda: draw(4))]


def b07(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE ONE STILL OPEN")
        y = doccards(d, L, y0, -1, h=150, small=True)
        bot, av = zone(L, y)
        if st >= 1:
            gap = 40
            wpx = (L.right - L.mx - gap * 3) / 4
            for i in range(4):
                x0 = int(L.mx + i * (wpx + gap))
                marker(d, int(x0 + wpx - 78), y - 132, 40, SIGNAL)
        t0, t1 = fy(y, av, 0.10), fy(y, av, 0.42)
        box(d, L.mx, t0, L.right, t1, SIGNAL, 8)
        txt = "BACKUP RETENTION — STILL CONFIRMING"
        d.text((L.mx + 56, (t0 + t1) / 2 - L.h2 * 0.72), txt,
               font=fit(MONOB, L.h2, txt, L.right - L.mx - 130), fill=SIGNAL)
        if st >= 2:
            d.text((L.mx, fy(y, av, 0.56)), "A PLAN SETTING · NOT VISIBLE FROM THE DATABASE",
                   font=fit(MONO, L.body, "A PLAN SETTING · NOT VISIBLE FROM THE DATABASE",
                            L.right - L.mx), fill=MUTE)
            ly = fy(y, av, 0.78)
            rule(d, L, ly, PAPER, 10)
            d.text((L.mx, ly + 50), "NAMED — NOT OMITTED", font=F(MONOB, L.h2), fill=PAPER)
        footer(d, L, "it appears in all four documents")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1)), (EL(6), lambda: draw(2))]


def b08(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHAT THE DOCUMENTS ACTUALLY DESCRIBE")
        y = doccards(d, L, y0, -1)
        bot, av = zone(L, y)
        if st >= 1:
            d.text((L.mx, fy(y, av, 0.16)), "WHAT WAS ALREADY TRUE",
                   font=F(MONOB, L.h2), fill=PAPER)
        if st >= 2:
            d.text((L.mx, fy(y, av, 0.46)), "OR WHAT WE FIXED WHEN ASKED",
                   font=F(MONOB, L.h2), fill=SIGNAL)
        footer(d, L, "that is the whole value of being asked")
        return img

    def title():
        img, d = frame(L)
        rule(d, L, L.my, SIGNAL, 16)
        f = fit(DISPLAY, 470, "FOUR", L.right - L.mx, -0.02)
        y = int(L.h * 0.26)
        track(d, (L.mx, y), "FOUR", f, PAPER)
        track(d, (L.mx, y + int(f.size * 1.20)), "DOCUMENTS", f, PAPER)
        rule(d, L, int(L.h * 0.74), MUTE, 8)
        d.text((L.mx, int(L.h * 0.74) + 54), "WHAT THE REVIEW ASKED FOR",
               font=F(MONOB, L.h1), fill=SIGNAL)
        footer(d, L, "none of it was built for the review")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1)),
            (EL(5), lambda: draw(2)), (EL(4), title)]


SCENES = {"B00": b00, "B01": b01, "B02": b02, "B03": b03, "B04": b04,
          "B05": b05, "B06": b06, "B07": b07, "B08": b08}


# ──────────────────────────────────────────────────────────── assembly ──
def allocate(segs, total):
    fixed = sum(f for f, _ in segs if isinstance(f, int))
    ws = [(i, 1 if f is None else f[1])
          for i, (f, _) in enumerate(segs) if not isinstance(f, int)]
    out = [f if isinstance(f, int) else 0 for f, _ in segs]
    left, wsum, acc = total - fixed, sum(w for _, w in ws) or 1, 0
    for j, (i, w) in enumerate(ws):
        share = left * w // wsum if j < len(ws) - 1 else left - acc
        out[i] = share; acc += share
    drift = total - sum(out)
    if drift:
        out[-1] = max(1, out[-1] + drift)
    return out


def render_beat(bid, L, dur, outdir, workroot):
    total = max(1, round(dur * FPS))
    segs = SCENES[bid](L)
    counts = allocate(segs, total)
    work = workroot / bid
    (work / "states").mkdir(parents=True); (work / "frames").mkdir()
    n = 0
    for idx, ((_, fn), cnt) in enumerate(zip(segs, counts)):
        if cnt <= 0:
            continue
        st = work / "states" / f"s{idx:04d}.png"
        fn().save(st, compress_level=1)
        for _ in range(cnt):
            n += 1
            os.link(st, work / "frames" / f"{n:06d}.png")
    out = outdir / f"{bid}.mp4"
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS),
                    "-i", str(work / "frames" / "%06d.png"),
                    "-c:v", "libx264", "-preset", "medium", "-crf", "16",
                    "-pix_fmt", "yuv420p", "-color_primaries", "bt709",
                    "-color_trc", "bt709", "-colorspace", "bt709", str(out)],
                   check=True, capture_output=True)
    shutil.rmtree(work)
    return out, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    ap.add_argument("--sheet"); ap.add_argument("--out"); ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    reel = Path(__file__).resolve().parent.parent
    sheet = json.loads(Path(a.sheet or reel / "beat_sheet.json").read_text())
    W, H = (3840, 2160) if a.aspect == "16:9" else (2160, 3840)
    L, outdir = Layout(W, H), Path(a.out or reel / "media")
    outdir.mkdir(parents=True, exist_ok=True)
    workroot = Path(tempfile.mkdtemp(prefix="scenes-"))
    print(f"[render] {a.aspect} {W}x{H} @{FPS}fps -> {outdir}")
    for b in sheet["beats"]:
        bid = b["beat_id"]
        if a.only and bid not in a.only:
            continue
        if bid not in SCENES:
            print(f"[render] {bid}: no scene defined — skipped"); continue
        dur = b.get("actual_duration_s") or b["estimated_duration_s"]
        out, n = render_beat(bid, L, float(dur), outdir, workroot)
        print(f"[render] {bid} {float(dur):>6.2f}s {n:>5d} frames -> {out.name}")
    shutil.rmtree(workroot, ignore_errors=True)


if __name__ == "__main__":
    main()
