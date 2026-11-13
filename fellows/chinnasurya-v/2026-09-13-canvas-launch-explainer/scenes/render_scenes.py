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




# ─────────────────────────────────────────────────────────────── scenes ──
def EL(weight=1):
    """Elastic segment. Weighted — an establishing state must never hold as
    long as the settled state carrying the content."""
    return ("el", weight)


def zone(L, top):
    """Usable vertical band between the header and the footer rule. Every
    scene places by FRACTION of this band, so content fills the frame at any
    canvas size instead of clustering at the top."""
    bot = L.bottom - 150
    return bot, bot - top


def fy(top, avail, f):
    return int(top + avail * f)


def b00(L):
    t1, t2 = "HOW A CANVAS", "LAUNCH WORKS"
    def draw(st):
        img, d = frame(L)
        rule(d, L, L.my, SIGNAL, 16)
        f = fit(DISPLAY, 470, t1, L.right - L.mx, -0.02)
        y = int(L.h * 0.26)
        if st >= 1: track(d, (L.mx, y), t1, f, PAPER)
        if st >= 2: track(d, (L.mx, y + int(f.size * 1.20)), t2, f, PAPER)
        if st >= 3:
            rule(d, L, int(L.h * 0.74), MUTE, 8)
            d.text((L.mx, int(L.h * 0.74) + 54), "LTI 1.3  ·  END TO END",
                   font=F(MONOB, L.h1), fill=SIGNAL)
        footer(d, L, "what happens between the click and the tool knowing you")
        return img
    return [(6, lambda: draw(0)), (8, lambda: draw(1)),
            (8, lambda: draw(2)), (EL(6), lambda: draw(3))]


def b01(L):
    qs = ["WHO ARE YOU?", "WHICH COURSE?", "WHAT ROLE?"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE PROBLEM")
        bot, av = zone(L, y0)
        bt, bb = fy(y0, av, 0.02), fy(y0, av, 0.34)
        lx1, rx0 = 1560, 2280
        box(d, L.mx, bt, lx1, bb, PAPER, 7)
        box(d, rx0, bt, L.right, bb, PAPER, 7)
        f = fit(DISPLAY, L.h1, "CANVAS", lx1 - L.mx - 120, -0.02)
        track(d, (L.mx + 64, (bt + bb) / 2 - f.size * 0.72), "CANVAS", f, PAPER)
        f2 = fit(DISPLAY, L.h1, "YOUR TOOL", L.right - rx0 - 120, -0.02)
        track(d, (rx0 + 64, (bt + bb) / 2 - f2.size * 0.72), "YOUR TOOL", f2, PAPER)
        arrow(d, lx1 + 80, rx0 - 80, int((bt + bb) / 2), MUTE, 10, 40)
        for i, q in enumerate(qs):
            if st >= i + 1:
                yy = fy(y0, av, 0.48 + i * 0.19)
                marker(d, L.mx, yy + 20, 62, SIGNAL if i == 0 else MUTE)
                d.text((L.mx + 130, yy), q, font=F(MONOB, L.h2), fill=PAPER)
        footer(d, L, "a separate app · on a different server · that cannot just believe the browser")
        return img
    return [(10, lambda: draw(0)), (5, lambda: draw(1)), (5, lambda: draw(2)),
            (EL(6), lambda: draw(3))]


def b02(L):
    left  = ["client_id", "deployment_id", "authorization endpoint", "jwks_url"]
    right = ["login endpoint", "redirect_uri", "jwks endpoint"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "REGISTRATION COMES FIRST")
        bot, av = zone(L, y0)
        cx = 1980
        d.text((L.mx, fy(y0, av, 0.0)), "CANVAS ISSUES", font=F(MONOB, L.data), fill=SIGNAL)
        d.text((cx,   fy(y0, av, 0.0)), "THE TOOL REGISTERS", font=F(MONOB, L.data), fill=SIGNAL)
        for i, t in enumerate(left):
            if st >= i + 1:
                yy = fy(y0, av, 0.16 + i * 0.155)
                marker(d, L.mx, yy + 18, 52, MUTE)
                d.text((L.mx + 110, yy), t, font=fit(MONO, L.body, t, 1480), fill=PAPER)
        for i, t in enumerate(right):
            if st >= len(left) + i + 1:
                yy = fy(y0, av, 0.16 + i * 0.155)
                marker(d, cx, yy + 18, 52, MUTE)
                d.text((cx + 110, yy), t, font=fit(MONO, L.body, t, 1380), fill=PAPER)
        if st >= 8:
            ly = fy(y0, av, 0.84)
            rule(d, L, ly, SIGNAL, 14)
            txt = "TRUST IS SET UP BEFORE THE FIRST LAUNCH"
            d.text((L.mx, ly + 54), txt, font=fit(MONOB, L.h2, txt, L.right - L.mx), fill=PAPER)
        footer(d, L, "nothing is negotiated during the launch itself")
        return img
    segs = [(10, lambda: draw(0))]
    segs += [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 8)]
    segs += [(EL(7), lambda: draw(8))]
    return segs


def b03(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "TWO KEYPAIRS · NO SHARED SECRET")
        bot, av = zone(L, y0)
        bt, bb = fy(y0, av, 0.0), fy(y0, av, 0.44)
        lx1, rx0 = 1560, 2280
        for x0, x1, name in ((L.mx, lx1, "CANVAS"), (rx0, L.right, "THE TOOL")):
            box(d, x0, bt, x1, bb, PAPER, 7)
            d.text((x0 + 60, bt + 48), name, font=F(MONOB, L.data), fill=PAPER)
            h = (bb - bt)
            d.rectangle([x0 + 60, bt + int(h * 0.36), x1 - 60, bt + int(h * 0.58)], fill=SIGNAL)
            d.text((x0 + 96, bt + int(h * 0.40)), "PRIVATE KEY",
                   font=F(MONOB, L.data), fill=GROUND)
            box(d, x0 + 60, bt + int(h * 0.66), x1 - 60, bt + int(h * 0.88), MUTE, 6)
            d.text((x0 + 96, bt + int(h * 0.70)), "PUBLIC — /jwks",
                   font=F(MONO, L.data), fill=MUTE)
        if st >= 1:
            d.text((L.mx, fy(y0, av, 0.54)), "CANVAS SIGNS  ·  THE TOOL VERIFIES",
                   font=F(MONOB, L.data), fill=PAPER)
            arrow(d, L.mx, L.right, fy(y0, av, 0.68), PAPER, 10, 42)
        if st >= 2:
            d.text((L.mx, fy(y0, av, 0.78)), "THE TOOL SIGNS  ·  CANVAS VERIFIES",
                   font=F(MONOB, L.data), fill=SIGNAL)
            arrow(d, L.right, L.mx, fy(y0, av, 0.92), SIGNAL, 10, 42)
        footer(d, L, "RS256  ·  neither side ever ships the other a password")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1)), (EL(6), lambda: draw(2))]


STATIONS = ["01 LOGIN", "02 ID_TOKEN", "03 VERIFY", "04 SPEND"]


def b04(L):
    rows = ["iss — which platform is calling",
            "login_hint — which user is arriving",
            "target_link_uri — where they were headed"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "MOVE ONE · THE LOGIN CALL")
        y = stations(d, L, y0, 0, STATIONS)
        bot, av = zone(L, y)
        for i, t in enumerate(rows):
            if st >= i + 1:
                yy = fy(y, av, 0.06 + i * 0.21)
                marker(d, L.mx, yy + 18, 52, MUTE)
                d.text((L.mx + 110, yy), t,
                       font=fit(MONO, L.body, t, L.right - L.mx - 160), fill=PAPER)
        if st >= 4:
            ly = fy(y, av, 0.78)
            rule(d, L, ly, SIGNAL, 14)
            txt = "state + nonce  →  STORED SERVER-SIDE"
            d.text((L.mx, ly + 54), txt,
                   font=fit(MONOB, L.h2, txt, L.right - L.mx), fill=SIGNAL)
        footer(d, L, "you do not trust the call yet")
        return img
    return [(10, lambda: draw(0)), (5, lambda: draw(1)), (5, lambda: draw(2)),
            (5, lambda: draw(3)), (EL(7), lambda: draw(4))]


def b05(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "MOVE TWO · THE TOKEN COMES BACK")
        y = stations(d, L, y0, 1, STATIONS)
        bot, av = zone(L, y)
        bt, bb = fy(y, av, 0.08), fy(y, av, 0.44)
        box(d, L.mx, bt, 1100, bb, PAPER, 7)
        d.text((L.mx + 48, (bt + bb) / 2 - L.data * 0.72), "CANVAS",
               font=F(MONOB, L.data), fill=PAPER)
        box(d, 2740, bt, L.right, bb, PAPER, 7)
        d.text((2740 + 48, (bt + bb) / 2 - L.data * 0.72), "THE TOOL",
               font=F(MONOB, L.data), fill=PAPER)
        if st >= 1:
            arrow(d, 1100 + 70, 2740 - 70, int((bt + bb) / 2), SIGNAL, 12, 46)
            d.rectangle([1520, bt + 40, 2330, bb - 40], fill=SIGNAL)
            d.text((1520 + 54, (bt + bb) / 2 - L.data * 0.76), "id_token (JWT)",
                   font=F(MONOB, L.data), fill=GROUND)
        if st >= 2:
            d.text((L.mx, fy(y, av, 0.60)), "response_mode = form_post",
                   font=F(MONOB, L.h2), fill=PAPER)
            rule(d, L, fy(y, av, 0.80), MUTE, 8)
            d.text((L.mx, fy(y, av, 0.80) + 54), "NOT IN THE URL  ·  NOT IN THE LOG",
                   font=F(MONO, L.body), fill=MUTE)
        footer(d, L, "a signed, self-contained statement about who this person is")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1)), (EL(6), lambda: draw(2))]


def b06(L):
    claims = [("sub", "a stable user identifier"), ("name", "display"),
              ("email", "identity matching"), ("roles", "student or instructor"),
              ("context", "course id and title"),
              ("resource_link", "which content they clicked"),
              ("custom", "which textbook to open"),
              ("deployment_id", "which installation"),
              ("message_type", "which kind of launch"),
              ("version", "which LTI version")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHAT THE TOKEN SAYS")
        bot, av = zone(L, y0)
        cx = 1980
        for i, (k, v) in enumerate(claims):
            if st < i + 1:
                continue
            col, row = divmod(i, 5)
            x = L.mx if col == 0 else cx
            yy = fy(y0, av, 0.02 + row * 0.196)
            marker(d, x, yy + 18, 54, SIGNAL if col == 0 else MUTE)
            d.text((x + 112, yy), k, font=fit(MONOB, L.data, k, 560), fill=PAPER)
            d.text((x + 112, yy + 104), v, font=fit(MONO, L.caption, v, 1380), fill=MUTE)
        footer(d, L, "the claims — identity, role, course, content pointer, protocol")
        return img
    segs = [(8, lambda: draw(0))]
    segs += [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 10)]
    segs += [(EL(8), lambda: draw(10))]
    return segs


def b07(L):
    checks = ["SIGNATURE — RS256 against Canvas's published keys",
              "ISS — it came from the platform you registered",
              "AUD — it was meant for you",
              "EXP — it has not expired"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "MOVE THREE · VERIFY")
        y = stations(d, L, y0, 2, STATIONS)
        bot, av = zone(L, y)
        for i, t in enumerate(checks):
            if st >= i + 1:
                yy = fy(y, av, 0.04 + i * 0.165)
                marker(d, L.mx, yy + 16, 58, SIGNAL)
                d.text((L.mx + 120, yy), t,
                       font=fit(MONO, L.body, t, L.right - L.mx - 170), fill=PAPER)
        if st >= 5:
            ly = fy(y, av, 0.80)
            rule(d, L, ly, SIGNAL, 14)
            d.text((L.mx, ly + 54), "ALG PINNED — RS256", font=F(MONOB, L.h2), fill=SIGNAL)
        footer(d, L, "four separate checks, not one")
        return img
    return [(8, lambda: draw(0))] + \
           [(5, (lambda s: lambda: draw(s))(i)) for i in range(1, 5)] + \
           [(EL(7), lambda: draw(5))]


def b08(L):
    def strip(d, L, y0, y1, label, mid, end, color):
        box(d, L.mx, y0, L.right, y1, color, 7)
        cy = int((y0 + y1) / 2)
        f = F(MONOB, L.data)
        d.text((L.mx + 64, cy - f.size * 0.72), label, font=f, fill=color)
        x = L.mx + 64 + f.getlength(label) + 100
        arrow(d, x, x + 250, cy, color, 8, 34); x += 330
        d.text((x, cy - f.size * 0.72), mid, font=f, fill=color)
        x += f.getlength(mid) + 100
        arrow(d, x, x + 250, cy, color, 8, 34); x += 330
        d.text((x, cy - f.size * 0.82), end, font=F(MONOB, L.h2), fill=color)

    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "MOVE FOUR · AND ONLY ONCE")
        bot, av = zone(L, y0)
        strip(d, L, fy(y0, av, 0.02), fy(y0, av, 0.24), "LAUNCH 01", "MATCH", "OK", PAPER)
        if st >= 1:
            strip(d, L, fy(y0, av, 0.34), fy(y0, av, 0.56),
                  "LAUNCH 01 REPLAYED", "NO MATCH", "REJECTED", SIGNAL)
        if st >= 2:
            yy = fy(y0, av, 0.70)
            rule(d, L, yy, MUTE, 8)
            d.text((L.mx, yy + 54), "NONCE — 10 MIN", font=F(MONOB, L.h2), fill=PAPER)
            d.text((L.mx, fy(y0, av, 0.89)), "LAUNCH AUDIT — 1 HR, THEN PURGED",
                   font=F(MONO, L.body), fill=MUTE)
        footer(d, L, "consumed on read — the second attempt finds nothing to match")
        return img
    return [(10, lambda: draw(0)), (8, lambda: draw(1)), (EL(6), lambda: draw(2))]


def b09(L):
    bands = [("ROLE", "matched to an official identifier list", PAPER),
             ("ACCESS", "evaluated server-side, on every request", PAPER),
             ("SCOPES", "none for grades, none for the roster", SIGNAL)]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHAT YOU DO WITH IT")
        bot, av = zone(L, y0)
        for i, (k, v, col) in enumerate(bands):
            if st < i + 1:
                continue
            t0 = fy(y0, av, 0.02 + i * 0.335)
            t1 = fy(y0, av, 0.02 + i * 0.335 + 0.27)
            box(d, L.mx, t0, L.right, t1, col, 7)
            d.text((L.mx + 64, t0 + 54), k, font=F(MONOB, L.h2), fill=col)
            d.text((L.mx + 64, t0 + 54 + L.h2 + 34), v,
                   font=fit(MONO, L.body, v, L.right - L.mx - 160), fill=MUTE)
        footer(d, L, "a permission you never requested cannot leak")
        return img
    return [(8, lambda: draw(0)), (6, lambda: draw(1)), (6, lambda: draw(2)),
            (EL(7), lambda: draw(3))]


def b10(L):
    words = ["REGISTER", "SIGN", "VERIFY", "SPEND"]
    def draw(st):
        img, d = frame(L)
        rule(d, L, L.my, SIGNAL, 16)
        bot, av = zone(L, L.my + 60)
        for i, w in enumerate(words):
            if st >= i + 1:
                yy = fy(L.my + 60, av, 0.02 + i * 0.245)
                marker(d, L.mx, yy + 52, 72, SIGNAL if i == 3 else MUTE)
                f = fit(DISPLAY, 300, w, L.right - L.mx - 200, -0.02)
                track(d, (L.mx + 150, yy), w, f, PAPER if i < 3 else SIGNAL)
        footer(d, L, "the launch is not where the trust comes from")
        return img

    def title():
        img, d = frame(L)
        rule(d, L, L.my, SIGNAL, 16)
        f = fit(DISPLAY, 470, "HOW A CANVAS", L.right - L.mx, -0.02)
        y = int(L.h * 0.26)
        track(d, (L.mx, y), "HOW A CANVAS", f, PAPER)
        track(d, (L.mx, y + int(f.size * 1.20)), "LAUNCH WORKS", f, PAPER)
        rule(d, L, int(L.h * 0.74), MUTE, 8)
        d.text((L.mx, int(L.h * 0.74) + 54), "LTI 1.3  ·  END TO END",
               font=F(MONOB, L.h1), fill=SIGNAL)
        footer(d, L, "the registration is")
        return img
    return [(8, lambda: draw(1)), (8, lambda: draw(2)), (8, lambda: draw(3)),
            (EL(5), lambda: draw(4)), (EL(4), title)]


SCENES = {"B00": b00, "B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05,
          "B06": b06, "B07": b07, "B08": b08, "B09": b09, "B10": b10}


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
