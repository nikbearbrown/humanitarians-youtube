#!/usr/bin/env python3
"""Per-script renderer — What Actually Crosses (Canvas <-> hub).

Core (layout, fonts, elastic allocation, assembly) reused verbatim from
medhavy-it-requirements; only the scene functions are new.
Unique state PNGs -> hard-linked frame sequence -> frame-exact mp4.
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



# ─────────────────────────────────────────────────────────────── scenes ──
def node(d, L, x0, x1, y, h, label, color, filled=False):
    """A system block: CANVAS or THE HUB."""
    if filled:
        d.rectangle([x0, y, x1, y + h], fill=color); fg = GROUND
    else:
        box(d, x0, y, x1, y + h, color, 6); fg = color
    f = fit(MONOB, int(h * 0.30), label, (x1 - x0) - 56)
    d.text((x0 + 28, y + h / 2 - f.size * 0.70), label, font=f, fill=fg)


def pill(d, L, cx, y, w, h, label, color):
    """A labelled block riding on an arrow."""
    x0, x1 = int(cx - w / 2), int(cx + w / 2)
    d.rectangle([x0, y, x1, y + h], fill=color)
    f = fit(MONOB, int(h * 0.42), label, w - 44)
    d.text((x0 + 22, y + h / 2 - f.size * 0.70), label, font=f, fill=GROUND)


def strike(d, x0, x1, y, color, wd=14):
    d.rectangle([x0, y - wd // 2, x1, y + wd // 2], fill=color)



def title_card(L, foot, reveal=4):
    """Three display lines + subtitle, all sized to clear the footer rule.

    The subtitle was colliding with the footer at h1; both the rule position
    and the subtitle size are now derived from the footer, not guessed.
    """
    img, d = frame(L)
    rule(d, L, L.my, SIGNAL, 16)
    sub = F(MONOB, L.h2)
    ry = int(L.bottom - 92 - 60 - sub.size - 50)   # clear of the footer rule
    y = int(L.h * 0.14)
    cap = int((ry - 90 - y) / 3.30)
    f = fit(DISPLAY, min(430, cap), "ACTUALLY", L.right - L.mx, -0.02)
    for i, w in enumerate(("WHAT", "ACTUALLY", "CROSSES")):
        if reveal >= i + 1:
            track(d, (L.mx, y + int(f.size * 1.18) * i), w, f, PAPER)
    if reveal >= 4:
        rule(d, L, ry, MUTE, 8)
        d.text((L.mx, ry + 50), "CANVAS <-> HUB", font=sub, fill=SIGNAL)
    footer(d, L, foot)
    return img


def b00(L):
    foot = "what moves between Canvas and the hub, and what deliberately does not"
    return [(6, lambda: title_card(L, foot, 0)), (7, lambda: title_card(L, foot, 1)),
            (7, lambda: title_card(L, foot, 2)), (7, lambda: title_card(L, foot, 3)),
            (EL(6), lambda: title_card(L, foot, 4))]


def b01(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE ASSUMPTION")
        bot, av = zone(L, y0)
        h = int(av * 0.30)
        ny = fy(y0, av, 0.16)
        wpx = int((L.right - L.mx) * 0.30)
        lx0, lx1 = L.mx, L.mx + wpx
        rx1, rx0 = L.right, L.right - wpx
        node(d, L, lx0, lx1, ny, h, "CANVAS", PAPER)
        node(d, L, rx0, rx1, ny, h, "THE HUB", PAPER)
        mid = ny + h // 2
        if st >= 1:
            arrow(d, lx1 + 60, rx0 - 60, mid, MUTE, 16, 44)
            arrow(d, rx0 - 60, lx1 + 60, mid, MUTE, 16, 44)
        if st >= 2:
            cx = (lx1 + rx0) / 2
            r = int((rx0 - lx1) * 0.16)
            d.line([(cx - r, mid - r), (cx + r, mid + r)], fill=SIGNAL, width=26)
            d.line([(cx - r, mid + r), (cx + r, mid - r)], fill=SIGNAL, width=26)
        if st >= 3:
            cy = fy(y0, av, 0.70)
            rule(d, L, cy, SIGNAL, 14)
            f = fit(MONOB, L.h2, "NOT SYNCHRONISED - AND THAT IS A DECISION", L.right - L.mx)
            d.text((L.mx, cy + 50), "NOT SYNCHRONISED - AND THAT IS A DECISION", font=f, fill=PAPER)
        footer(d, L, "rosters one way, grades the other: that is not what we built")
        return img
    return [(9, lambda: draw(0)), (EL(4), lambda: draw(1)),
            (EL(4), lambda: draw(2)), (EL(6), lambda: draw(3))]


def b02(L):
    lines = ["ON CLICK - NOT ON A SCHEDULE", "NO BACKGROUND FETCH", "NO CLICK, NO DATA"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "ONE THING CROSSES")
        bot, av = zone(L, y0)
        h = int(av * 0.26)
        ny = fy(y0, av, 0.04)
        wpx = int((L.right - L.mx) * 0.26)
        lx1 = L.mx + wpx; rx0 = L.right - wpx
        node(d, L, L.mx, lx1, ny, h, "CANVAS", PAPER)
        node(d, L, rx0, L.right, ny, h, "THE HUB", PAPER)
        mid = ny + h // 2
        if st >= 1:
            arrow(d, lx1 + 50, rx0 - 50, mid, SIGNAL, 14, 44)
            pill(d, L, (lx1 + rx0) / 2, mid - int(h * 0.26), int(wpx * 1.15),
                 int(h * 0.52), "LAUNCH TOKEN", SIGNAL)
        ty = fy(y0, av, 0.52)
        lf = F(MONOB, L.body)
        for i, ln in enumerate(lines):
            if st >= 2 + i:
                marker(d, L.mx, ty + i * int(lf.size * 1.75) + int(lf.size * 0.18),
                       int(lf.size * 0.42), SIGNAL)
                d.text((L.mx + int(lf.size * 0.95), ty + i * int(lf.size * 1.75)),
                       ln, font=lf, fill=PAPER)
        footer(d, L, "the launch token, and only when a student clicks")
        return img
    return [(8, lambda: draw(0)), (EL(5), lambda: draw(1))] + \
           [(3, (lambda s: lambda: draw(s))(2 + i)) for i in range(2)] + \
           [(EL(6), lambda: draw(4))]


def b03(L):
    rows = [("canvas:9f2a...", "medhavy:u_41c8"), ("canvas:3b7e...", "medhavy:u_52da"),
            ("canvas:c014...", "medhavy:u_6f03")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE DATABASE FILLS LAZILY")
        bot, av = zone(L, y0)
        hf = F(MONOB, L.h2)
        hy = fy(y0, av, 0.04)
        d.text((L.mx, hy), "lti_user_links", font=hf, fill=SIGNAL)
        rule(d, L, hy + int(hf.size * 1.5), MUTE, 6)
        rf = F(MONO, L.data)
        ry = hy + int(hf.size * 1.5) + 54
        colw = (L.right - L.mx)
        for i, (a, b) in enumerate(rows):
            if st < i + 1:
                continue
            yy = ry + i * int(rf.size * 2.3)
            d.text((L.mx, yy), a, font=rf, fill=PAPER)
            ax0 = L.mx + int(colw * 0.34); ax1 = L.mx + int(colw * 0.46)
            arrow(d, ax0, ax1, yy + int(rf.size * 0.55), MUTE, 6, 26)
            d.text((L.mx + int(colw * 0.50), yy), b, font=rf, fill=PAPER)
        if st >= 4:
            cy = fy(y0, av, 0.78)
            rule(d, L, cy, SIGNAL, 14)
            t = "WRITTEN ON ARRIVAL - NEVER PRE-COPIED"
            d.text((L.mx, cy + 50), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "the database fills up as people arrive")
        return img
    return [(8, lambda: draw(0))] + \
           [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(7), lambda: draw(4))]


def b04(L):
    cards = [("NAMES AND ROLE PROVISIONING", "reads the class roster"),
             ("ASSIGNMENT AND GRADE SERVICES", "writes to the gradebook")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE TWO SERVICES WE DID NOT TAKE")
        bot, av = zone(L, y0)
        h = int(av * 0.22)
        gap = 46
        for i, (t, sub) in enumerate(cards):
            if st < i + 1:
                continue
            yy = fy(y0, av, 0.03) + i * (h + gap)
            box(d, L.mx, yy, L.right, yy + h, PAPER, 6)
            tf = fit(MONOB, int(h * 0.26), t, (L.right - L.mx) - 56)
            d.text((L.mx + 28, yy + int(h * 0.08)), t, font=tf, fill=PAPER)
            sf = F(MONO, int(h * 0.19))
            d.text((L.mx + 28, yy + int(h * 0.68)), sub, font=sf, fill=MUTE)
            if st >= 3:
                strike(d, L.mx, L.right, yy + h // 2, SIGNAL, 16)
        if st >= 4:
            cy = fy(y0, av, 0.60)
            d.text((L.mx, cy), "scopes: []", font=F(MONOB, L.h1), fill=SIGNAL)
        if st >= 5:
            cy = fy(y0, av, 0.82)
            rule(d, L, cy, SIGNAL, 14)
            t = "NEVER REQUESTED - NOT MERELY DISABLED"
            d.text((L.mx, cy + 50), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "a permission you request at registration, and we did not")
        return img
    return [(8, lambda: draw(0)), (6, lambda: draw(1)), (EL(4), lambda: draw(2)),
            (EL(4), lambda: draw(3)), (EL(4), lambda: draw(4)), (EL(5), lambda: draw(5))]


def b05(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE ONE PATH BACK")
        bot, av = zone(L, y0)
        h = int(av * 0.28)
        ny = fy(y0, av, 0.12)
        wpx = int((L.right - L.mx) * 0.26)
        lx1 = L.mx + wpx; rx0 = L.right - wpx
        node(d, L, L.mx, lx1, ny, h, "CANVAS", MUTE)
        node(d, L, rx0, L.right, ny, h, "THE HUB", MUTE)
        mid = ny + h // 2
        if st >= 1:
            arrow(d, rx0 - 50, lx1 + 50, mid, SIGNAL, 14, 44)
            pill(d, L, (lx1 + rx0) / 2, mid - int(h * 0.24), int(wpx * 1.25),
                 int(h * 0.48), "CONTENT POINTER", SIGNAL)
        if st >= 2:
            cy = fy(y0, av, 0.70)
            d.text((L.mx, cy), "LtiDeepLinkingRequest", font=F(MONOB, L.h1), fill=PAPER)
            rule(d, L, cy + int(L.h1 * 1.5), MUTE, 6)
            d.text((L.mx, cy + int(L.h1 * 1.5) + 40),
                   "THE ONLY TOOL-TO-PLATFORM MESSAGE WE CARRY",
                   font=F(MONOB, L.caption), fill=MUTE)
        footer(d, L, "deep linking: the instructor picks, we hand back a pointer")
        return img
    return [(8, lambda: draw(0)), (EL(5), lambda: draw(1)), (EL(6), lambda: draw(2))]


def b06(L):
    steps = ["QUIZ SUBMITTED", "GRADED SERVER SIDE", "STORED"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE HONEST GAP")
        bot, av = zone(L, y0)
        h = int(av * 0.20)
        yy = fy(y0, av, 0.10)
        gap = 54
        n = len(steps)
        wpx = (L.right - L.mx - gap * n) / (n + 1.45)
        for i, s in enumerate(steps):
            if st < i + 1:
                continue
            x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
            node(d, L, x0, x1, yy, h, s, PAPER)
            if i and st >= i + 1:
                arrow(d, x0 - gap + 8, x0 - 8, yy + h // 2, MUTE, 8, 28)
        if st >= 4:
            x0 = int(L.mx + n * (wpx + gap)); x1 = L.right
            arrow(d, x0 - gap + 8, x0 - 8, yy + h // 2, SIGNAL, 10, 30)
            d.rectangle([x0, yy, x1, yy + h], fill=SIGNAL)
            t = "NO ROUTE TO THE GRADEBOOK"
            tf = fit(MONOB, int(h * 0.26), t, (x1 - x0) - 44)
            for j, ln in enumerate(wrap(t, tf, (x1 - x0) - 44)[:3]):
                d.text((x0 + 22, yy + int(h * 0.16) + j * int(tf.size * 1.35)),
                       ln, font=tf, fill=GROUND)
        if st >= 5:
            cy = fy(y0, av, 0.62)
            rule(d, L, cy, MUTE, 8)
            cap = "a comment marks where the job would go. the job does not exist yet."
            d.text((L.mx, cy + 44),
                   cap, font=fit(MONO, L.body, cap, L.right - L.mx), fill=PAPER)
        footer(d, L, "the score sits in our database and goes nowhere")
        return img
    return [(8, lambda: draw(0))] + \
           [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(5), lambda: draw(4)), (EL(8), lambda: draw(5))]


def b07(L):
    opts = [("KEEP IT CLOSED", ["no roster", "no grades", "smallest surface"]),
            ("OPEN IT", ["request AGS", "reopen the data review"])]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE REAL QUESTION")
        bot, av = zone(L, y0)
        gap = 70
        wpx = (L.right - L.mx - gap) / 2
        h = int(av * 0.56)
        yy = fy(y0, av, 0.04)
        for i, (t, bullets) in enumerate(opts):
            if st < i + 1:
                continue
            x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
            box(d, x0, yy, x1, yy + h, PAPER, 6)
            tf = fit(MONOB, int(h * 0.15), t, wpx - 56)
            d.text((x0 + 28, yy + int(h * 0.09)), t, font=tf, fill=PAPER)
            bf = F(MONO, int(h * 0.098))
            for j, b in enumerate(bullets):
                by = yy + int(h * 0.36) + j * int(bf.size * 1.65)
                marker(d, x0 + 28, by + int(bf.size * 0.26), int(bf.size * 0.34), MUTE)
                d.text((x0 + 28 + int(bf.size * 0.80), by), b, font=bf, fill=MUTE)
        if st >= 3:
            cy = fy(y0, av, 0.78)
            rule(d, L, cy, SIGNAL, 14)
            t = "A DECISION - NOT A TODO"
            d.text((L.mx, cy + 50), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "a decision about scope, not a missing function")
        return img
    return [(8, lambda: draw(0)), (6, lambda: draw(1)), (EL(5), lambda: draw(2)),
            (EL(6), lambda: draw(3))]


def b08(L):
    rows = ["ONE TOKEN - PER CLICK - ONE DIRECTION", "ONE CONTENT POINTER BACK", "NOTHING ELSE"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "AS OF TODAY")
        bot, av = zone(L, y0)
        rf = F(MONOB, L.h2)
        ry = fy(y0, av, 0.10)
        for i, r in enumerate(rows):
            if st < i + 1:
                continue
            f = fit(MONOB, L.h2, r, L.right - L.mx - int(rf.size * 0.95))
            yy = ry + i * int(rf.size * 2.1)
            marker(d, L.mx, yy + int(f.size * 0.18), int(f.size * 0.42), SIGNAL)
            d.text((L.mx + int(f.size * 0.95), yy), r, font=f, fill=PAPER)
        footer(d, L, "what actually crosses")
        return img
    def title():
        return title_card(L, "medhavy canvas lti 1.3")

    return [(6, lambda: draw(0))] + \
           [(3, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(5), lambda: draw(3)), (EL(5), title)]


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
