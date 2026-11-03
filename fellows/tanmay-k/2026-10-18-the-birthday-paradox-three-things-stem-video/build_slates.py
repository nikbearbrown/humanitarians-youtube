#!/usr/bin/env python3
"""Week 27 review stills: one 3840x2160 slate per beat, at the moment of assertion.

Standalone Pillow drawer (no shared-toolkit code): house look is the Claude-cream palette and the
bundled EB Garamond + Inter fonts (OFL). Every number on a slate is COMPUTED here from the data
files and the exact formulas, not typed by hand, then asserted against the figures the narration
speaks (see CHECKS at the bottom). Math is laid out structurally (real radical, real fraction bar),
never as a text fallback.

Run:  /opt/homebrew/bin/python3.12 build_slates.py        -> _stills/B01-16x9.png ... B18-16x9.png
"""
import csv, json, math, random, sys
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
OUT = HERE / "_stills"
OUT.mkdir(exist_ok=True)
FONTS = Path("brutalist.art/runtime/fonts")  # the toolkit checkout; adjust to where it lives
S = 2                      # logical 1920x1080 -> 3840x2160 (4K master)
W, H = 1920, 1080
M = 115                    # left margin

# palette (house: ink on cream)
PAGE, CARD, BORDER = "#FAF9F5", "#FFFFFF", "#E5E2D9"
INK, INK_SOFT, GHOST, SPARK, SEND, PILL = "#3D3929", "#73705F", "#A9A491", "#D97757", "#C6613F", "#EDEBE1"
SPARK_TEXT = "#B5532F"   # 4.7:1 on cream: small accent text (SPARK itself is 2.96:1)
GHOST_TEXT = "#73705F"   # inactive-card text = INK_SOFT, 4.7:1 on cream


def mix(a, b, t):
    a = tuple(int(a[i:i + 2], 16) for i in (1, 3, 5)); b = tuple(int(b[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


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


class Canvas:
    def __init__(self, stage=99):
        self.stage, self.k, self.maxk = stage, 0, 0
        self.im = Image.new("RGB", (W * S, H * S), PAGE)
        self.d = ImageDraw.Draw(self.im)
        self.log = []

    def _on(self):
        self.maxk = max(self.maxk, self.k)
        return self.k <= self.stage

    def text(self, x, y, s, kind="sans", size=24, fill=INK, anchor="la"):
        if not self._on(): return
        if kind.startswith("sans") and size < 24: size = 24
        if fill == SPARK: fill = SPARK_TEXT if size < 48 else SEND
        if fill == GHOST: fill = GHOST_TEXT
        self.log.append((s, kind, size, fill))
        self.d.text((x * S, y * S), s, font=F(kind, size), fill=fill, anchor=anchor)

    def tw(self, s, kind, size):
        return F(kind, size).getlength(s) / S

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        if not self._on(): return
        box = (x0 * S, y0 * S, x1 * S, y1 * S)
        if r: self.d.rounded_rectangle(box, radius=r * S, fill=fill, outline=outline, width=round(width * S))
        else: self.d.rectangle(box, fill=fill, outline=outline, width=round(width * S))

    def line(self, pts, fill=INK, width=2):
        if not self._on(): return
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=round(width * S), joint="curve")

    def dot(self, x, y, r, fill=INK, outline=None, width=1):
        if not self._on(): return
        self.d.ellipse(((x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S), fill=fill,
                       outline=outline, width=round(width * S))

    def wrap(self, x, y, s, kind, size, fill, maxw, lh=1.3, anchor="la"):
        words, lines, cur = s.split(), [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if self.tw(t, kind, size) <= maxw: cur = t
            else: lines.append(cur); cur = w_
        lines.append(cur)
        for i, l in enumerate(lines): self.text(x, y + i * size * lh, l, kind, size, fill, anchor)
        return y + len(lines) * size * lh

    def wrap_count(self, s, kind, size, maxw):
        words, n, cur = s.split(), 1, ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if self.tw(t, kind, size) <= maxw: cur = t
            else: n += 1; cur = w_
        return n

    def save(self, name):
        self.im.save(OUT / name, optimize=True)


# ---------------------------------------------------------------- math (structured layout)
class Math:
    """Tiny structural typesetter: runs, radicals with a vinculum, fractions with a bar."""
    def __init__(self, cv, size):
        self.cv, self.F = cv, size

    def _run(self, s, kind, size):
        return ("run", s, kind, size, self.cv.tw(s, kind, size))

    def var(self, s, size=None): return self._run(s, "serifi", size or self.F)
    def txt(self, s, size=None): return self._run(s, "serif", size or self.F)
    def op(self, s, size=None):
        size = size or self.F
        return ("op", s, size, self.cv.tw(s, "serif", size) + size * 0.5)   # padded operator

    def paren(self, ch):
        size = self.F * 1.5
        return ("paren", ch, size, self.cv.tw(ch, "serif", size))

    def sqrt(self, inner): return ("sqrt", inner, self.width(inner) + self.F * 0.62)
    def frac(self, num, den):
        fs = self.F * 0.72
        return ("frac", num, den, max(self.width(num), self.width(den)) + self.F * 0.2)

    def width(self, items):
        return sum(i[-1] for i in items)

    def draw(self, x, yb, items, color=INK):
        """x = left, yb = baseline (logical px). returns right x."""
        cv, F_ = self.cv, self.F
        for it in items:
            k = it[0]
            if k == "run":
                _, s, kind, size, w = it
                cv.text(x, yb, s, kind, size, color, "ls")
            elif k == "op":
                _, s, size, w = it
                cv.text(x + size * 0.25, yb, s, "serif", size, color, "ls")
            elif k == "paren":
                _, ch, size, w = it
                cv.text(x, yb + F_ * 0.16, ch, "serif", size, color, "ls")
            elif k == "sqrt":
                _, inner, w = it
                iw = self.width(inner); top = yb - F_ * 0.92
                t = F_ * 0.05
                cv.line([(x, yb - F_ * 0.36), (x + F_ * 0.12, yb - F_ * 0.30), (x + F_ * 0.24, yb + F_ * 0.10),
                         (x + F_ * 0.50, top), (x + F_ * 0.55 + iw, top)], color, t)
                self.draw(x + F_ * 0.58, yb, inner, color)
            elif k == "frac":
                _, num, den, w = it
                ax = yb - F_ * 0.30
                nw, dw = self.width(num), self.width(den)
                cv.line([(x + F_ * 0.04, ax), (x + w - F_ * 0.04, ax)], color, F_ * 0.04)
                self.draw(x + (w - nw) / 2, ax - F_ * 0.16, num, color)
                self.draw(x + (w - dw) / 2, ax + F_ * 0.84, den, color)
            x += it[-1]
        return x


def rule_items(m, d_label="d"):
    # n ~ round( 1.2 sqrt(d) + 1/2 )
    return [m.var("n"), m.op("≈"), m.txt("round"), m.paren("("), m.txt("1.2"), m.op("×"), m.sqrt([m.var(d_label)]),
            m.op("+"), m.frac([m.txt("1")], [m.txt("2")]), m.paren(")")]


# ---------------------------------------------------------------- numbers (computed, never typed)
def pm(n, d):
    if n > d: return 1.0
    q = 1.0
    for i in range(n): q *= (d - i) / d
    return 1 - q


def n50(d):
    n = 2
    while pm(n, d) < .5: n += 1
    return n


def rule_n(d): return math.floor(1.2 * math.sqrt(d) + 1.0)


cl = json.load(open(HERE / "cluster-rates.json"))
mr = json.load(open(HERE / "match-rates.json"))
sq = json.load(open(HERE / "sqrt-rule.json"))
births = defaultdict(int)
for r_ in csv.DictReader(open(HERE / "data/US_births_2000-2014_SSA.csv")):
    births[(int(r_["month"]), int(r_["date_of_month"]))] += int(r_["births"])
MDAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
tot366 = sum(births.values())
ratio366 = {k: v / tot366 * 366 for k, v in births.items()}                 # with Feb 29, mean over 366 days
tot365 = sum(v for k, v in births.items() if k != (2, 29))
ratio365 = {k: v / tot365 * 365 for k, v in births.items() if k != (2, 29)}  # Feb 29 dropped
UNI23 = pm(23, 365)
REAL23 = mr["real"]["SSA 2000-2014 | with Feb 29"]["23"]["exact"]
pct = lambda x, nd=1: f"{x * 100:.{nd}f}%"


# ---------------------------------------------------------------- shared parts
SRC_FONT = 26


def heading(cv, s): cv.text(M, 120, s, "serif", 56, INK, "ls")


def source(cv, s):
    cv.k = 0
    if not s: return
    n = cv.wrap_count(s, "sans", SRC_FONT, W - 2 * M)
    cv.wrap(M, H - 96 - n * SRC_FONT * 1.35, s, "sans", SRC_FONT, INK_SOFT, W - 2 * M, 1.35)


CHAPTERS = ["PEOPLE", "EVENNESS", "DAYS"]


def strip(cv, active, readings=None, y=160, big=False):
    """Chapter index: three cards, the active one in the accent."""
    n, gap = 3, 28
    cw = (W - 2 * M - gap * (n - 1)) / n
    h = 94 if not big else 200
    for i, name in enumerate(CHAPTERS):
        x = M + i * (cw + gap)
        on = active is None or i == active
        cv.rect(x, y, x + cw, y + h, fill=CARD if on else PAGE, outline=SPARK if (active == i) else BORDER,
                width=3 if active == i else 1.5, r=10)
        cv.text(x + 22, y + 12, name, "sansm", 24, SPARK if active == i else (INK_SOFT if on else GHOST))
        sub = ["how many are in the group", "how uneven the birthdays are", "how many days they land on"][i]
        cv.text(x + 22, y + 50, sub, "serif", 25, INK if on else GHOST)
        if readings:
            cv.text(x + 22, y + 82, readings[i][0], "serif", 52, INK)
            cv.text(x + 22, y + 152, readings[i][1], "sans", 21, INK_SOFT)
    return y + h


def grid(cv, x0, y0, cell=30, gap=3, color=None, feb29=False, dim=None, outline_feb29=False, only=None, labels=True):
    """12 rows (months) x 31 columns (day of month). color(m,d)->hex. dim(m,d)->True fades a cell."""
    step = cell + gap
    for mi in range(12):
        if labels: cv.text(x0 - 12, y0 + mi * step + cell / 2, MONTHS[mi], "sans", 17, INK_SOFT, "rm")
        for d in range(1, MDAYS[mi] + 1):
            if (mi + 1, d) == (2, 29) and not feb29: continue
            if only and not only(mi + 1, d): continue
            c = color(mi + 1, d) if color else BORDER
            if dim and dim(mi + 1, d): c = mix(c, PAGE, 0.65)
            cv.rect(x0 + (d - 1) * step, y0 + mi * step, x0 + (d - 1) * step + cell, y0 + mi * step + cell, fill=c, r=3)
    return step


def cell_xy(x0, y0, m, d, cell=30, gap=3):
    step = cell + gap
    return x0 + (m_ := (d - 1)) * step + cell / 2, y0 + (m - 1) * step + cell / 2


def draw_dots(cv, x0, y0, days, ring=None, r=9, cell=30, gap=3, ks=None):
    seen = defaultdict(int)
    for i_, (m, d) in enumerate(days):
        if ks: cv.k = ks[min(i_ * len(ks) // len(days), len(ks) - 1)]
        cx, cy = cell_xy(x0, y0, m, d, cell, gap)
        k = seen[(m, d)]; seen[(m, d)] += 1
        off = (-5.5, 0) if (ring and k == 0 and (m, d) == ring) else ((5.5, 0) if ring and (m, d) == ring else (0, 0))
        cv.dot(cx + off[0], cy + off[1], r * (0.72 if (m, d) == ring else 1), fill=INK)
    if ring:
        if ks: cv.k = ks[-1]
        cx, cy = cell_xy(x0, y0, ring[0], ring[1], cell, gap)
        cv.dot(cx, cy, 20, fill=None, outline=SPARK, width=3.5)


def big_number(cv, x, y, s, label, size=150, color=INK):
    cv.text(x, y, s, "serif", size, color, "ls")
    cv.text(x, y + 38, label.upper(), "sansm", 21, INK_SOFT)


def draw_days(rng, pool, n, want_pair):
    while True:
        s = [rng.choice(pool) for _ in range(n)]
        dup = [k for k, c in __import__("collections").Counter(s).items() if c > 1]
        if want_pair == "one" and len(dup) == 1 and __import__("collections").Counter(s)[dup[0]] == 2: return s, dup[0]
        if want_pair == "any" and dup: return s, dup[0]


ALL365 = [(m, d) for m in range(1, 13) for d in range(1, MDAYS[m - 1] + 1) if (m, d) != (2, 29)]
GX, GY = 175, 290       # shared grid origin (logical px)


# ---------------------------------------------------------------- beats
def b01(stage=99):
    cv = Canvas(stage); heading(cv, "Two of these twenty-three share a day")
    days, ring = draw_days(random.Random(2701), ALL365, 23, "one")
    grid(cv, GX, GY); draw_dots(cv, GX, GY, days, ring, ks=(1, 2, 3)); cv.k = 0
    cv.text(GX, GY + 12 * 33 + 40, "An illustration: one random group of 23 people, one dot each.", "serif", 30, INK_SOFT)
    cv.k = 4
    cv.text(1300, 420, pct(UNI23), "serif", 170, SPARK, "ls")
    cv.wrap(1300, 470, "of random groups of 23 people have a shared birthday", "serif", 32, INK, 520)
    source(cv, "Our simulation and exact calculation (see the next chapters). Illustration: one random group of 23, seed 2701. Not data.")
    return cv


def b02(stage=99):
    cv = Canvas(stage); heading(cv, "Three things could change that figure")
    cw, gap = (W - 2 * M - 56) / 3, 28
    for i, name in enumerate(CHAPTERS):
        cv.k = i + 1
        x = M + i * (cw + gap); y = 240
        cv.rect(x, y, x + cw, y + 300, fill=CARD, outline=BORDER, width=1.5, r=14)
        cv.text(x + 36, y + 40, name, "sansm", 28, SPARK)
        cv.wrap(x + 36, y + 100, ["how many people are in the group", "how uneven the birthdays are",
                                  "how many days they have to land on"][i], "serif", 50, INK, cw - 72, 1.15)
    cv.k = 4
    cv.rect(M, 620, M + 8, 740, fill=SPARK)
    cv.wrap(M + 30, 628, "Hold a guess. One barely matters, one matters the way you'd expect, and one decides almost everything.",
            "sansm", 36, INK, 1500, 1.35)
    return cv


def b03(stage=99):
    cv = Canvas(stage); heading(cv, "Count pairs, not people"); strip(cv, 0)
    cx, cy, R = 560, 640, 300
    pts = [(cx + R * math.cos(2 * math.pi * i / 23 - math.pi / 2), cy + R * math.sin(2 * math.pi * i / 23 - math.pi / 2)) for i in range(23)]
    cv.k = 2
    for i in range(23):
        for j in range(i + 1, 23): cv.line([pts[i], pts[j]], mix(SPARK, PAGE, 0.72), 1.1)
    cv.k = 1
    for p in pts: cv.dot(p[0], p[1], 11, INK)
    m = Math(cv, 92)
    items = [m.frac([m.txt("23"), m.op("×"), m.txt("22")], [m.txt("2")]), m.op("="), m.txt("253")]
    cv.k = 3
    cv.text(1180, 470, "PAIRS", "sansm", 24, INK_SOFT)
    m.draw(1180, 640, items)
    cv.k = 4
    cv.wrap(1180, 745, "Each pair is a small chance, and 253 small chances pile up faster than your gut expects.", "serif", 34, INK, 600, 1.3)
    source(cv, "23 × 22 ÷ 2 = 253  ·  Our calculation.")
    return cv


def b04(stage=99):
    cv = Canvas(stage); heading(cv, "First change: the people"); strip(cv, 0)
    # curve of exact odds vs people, even days
    x0, y0, x1, y1 = 205, 290, 1180, 840
    cv.rect(x0, y0, x1, y1, fill=CARD, outline=BORDER, width=1.5, r=6)
    mx = 62
    X = lambda n: x0 + (x1 - x0) * n / mx
    Y = lambda p: y1 - (y1 - y0 - 70) * p
    for p in (0, .25, .5, .75, 1.0):
        cv.line([(x0, Y(p)), (x1, Y(p))], BORDER, 1); cv.text(x0 - 12, Y(p), f"{int(p * 100)}%", "sans", 19, INK_SOFT, "rm")
    for n in (0, 10, 20, 30, 40, 50, 60):
        cv.text(X(n), y1 + 12, str(n), "sans", 19, INK_SOFT, "ma")
    cv.text((x0 + x1) / 2, y1 + 48, "people in the group", "sans", 24, INK_SOFT, "ma")
    cv.k = 1
    cv.line([(X(n), Y(pm(n, 365))) for n in range(1, mx)], INK, 3.5)
    for n in (10, 23, 30, 50, 57):
        on = n == 23
        cv.k = {10: 3, 23: 2, 30: 4, 50: 5, 57: 6}[n]
        cv.dot(X(n), Y(pm(n, 365)), 11 if on else 9, SPARK if on else INK)
        lab = f"{n} people  {pct(pm(n, 365))}"
        pos = {50: (-48, -44, "ra"), 57: (72, -44, "ra")}.get(n, (16, 10, "la"))
        cv.text(X(n) + pos[0], Y(pm(n, 365)) + pos[1], lab, "sansm", 22, SPARK if on else INK, pos[2])
    cv.k = 2
    big_number(cv, 1290, 420, pct(UNI23), "23 people, even days", 140, SPARK)
    cv.text(1290, 505, f"exact calculation: {UNI23 * 100:.2f}%", "sans", 26, INK_SOFT)
    cv.text(1290, 560, "400,000 random groups agree.", "serif", 30, INK)
    source(cv, "Our simulation: 400,000 groups, seed 2701. Exact calculation also shown. Even days assumed.")
    return cv


def b05(stage=99):
    cv = Canvas(stage); heading(cv, "Some pair, or a pair with you"); strip(cv, 0)
    pw = (W - 2 * M - 60) / 2
    mine = 1 - (364 / 365) ** 22
    for i, (lab, big, sub, extra) in enumerate([
        ("any pair among 23 people", pct(UNI23), "chance of a shared birthday", "23 people make 253 pairs"),
        ("someone shares YOUR birthday", pct(mine), "chance, with 22 others in the room",
         f"even odds need {math.ceil(math.log(.5) / math.log(364 / 365))} other people")]):
        cv.k = i + 1
        x = M + i * (pw + 60)
        cv.rect(x, 290, x + pw, 780, fill=CARD, outline=SPARK if i == 1 else BORDER, width=3 if i == 1 else 1.5, r=14)
        cv.text(x + 40, 330, lab.upper(), "sansm", 24, SPARK if i == 1 else INK_SOFT)
        cv.text(x + 40, 560, big, "serif", 190, INK, "ls")
        cv.text(x + 44, 620, sub, "serif", 36, INK)
        cv.text(x + 44, 700, extra, "serif", 36, INK_SOFT)
    cv.k = 3
    cv.text(W / 2, 840, "Same crowd, a different question.", "serifi", 38, INK_SOFT, "ma")
    source(cv, "Our calculation. Even days assumed.")
    return cv


def b06(stage=99):
    cv = Canvas(stage); heading(cv, "Second change: how even the days are"); strip(cv, 1)
    lo, hi = 0.55, 1.12
    col = lambda m, d: mix(PILL, SPARK, max(0, min(1, (ratio366[(m, d)] - lo) / (hi - lo))))
    grid(cv, GX, GY + 20, color=lambda m, d: BORDER, feb29=True)
    cv.k = 1
    grid(cv, GX, GY + 20, color=col, feb29=True, labels=False)
    step = 33
    fx, fy = cell_xy(GX, GY + 20, 2, 29)
    cv.k = 3
    cv.dot(fx, fy, 19, fill=None, outline=INK, width=3)
    cv.line([(fx + 22, fy), (fx + 90, fy - 6)], INK, 2)
    cv.text(fx + 98, fy - 22, "Feb 29: about a quarter of a normal day,", "serif", 28, INK)
    cv.text(fx + 98, fy + 8, "because it exists one year in four", "serif", 28, INK_SOFT)
    # legend
    cv.k = 1
    lx, ly = GX, GY + 20 + 12 * step + 24
    for i in range(240):
        cv.rect(lx + i * 2, ly, lx + i * 2 + 2, ly + 18, fill=mix(PILL, SPARK, i / 239))
    cv.text(lx, ly + 28, "quieter days", "sans", 19, INK_SOFT); cv.text(lx + 480, ly + 28, "busier days", "sans", 19, INK_SOFT, "ra")
    mx_day = max(ratio366, key=ratio366.get)
    cv.k = 2
    cv.text(1300, 470, "BUSIEST DAY", "sansm", 22, INK_SOFT)
    cv.text(1300, 580, f"+{(ratio366[mx_day] - 1) * 100:.0f}%", "serif", 110, SPARK, "ls")
    cv.text(1300, 625, "above an average day", "serif", 32, INK)
    cv.k = 3
    cv.text(1300, 700, "FEB 29", "sansm", 22, INK_SOFT)
    cv.text(1300, 800, f"{ratio366[(2, 29)] * 100:.0f}%", "serif", 100, INK, "ls")
    cv.text(1300, 845, "of an average day", "serif", 32, INK)
    cv.k = 0
    cv.text(M, 892, "Births data: US NCHS and SSA via FiveThirtyEight (CC BY 4.0)", "sansm", 28, INK)
    source(cv, "US federal births per calendar day, 2000–2014, pooled. Colour shows each day's share of births.")
    return cv


def b07(stage=99):
    cv = Canvas(stage); heading(cv, "The real calendar barely moves the odds"); strip(cv, 1)
    pw = (W - 2 * M - 60) / 2
    for i, (lab, v) in enumerate([("even days", UNI23), ("real calendar", REAL23)]):
        cv.k = i
        x = M + i * (pw + 60)
        cv.rect(x, 290, x + pw, 700, fill=CARD, outline=SPARK if i else BORDER, width=3 if i else 1.5, r=14)
        cv.text(x + 40, 330, lab.upper(), "sansm", 24, SPARK if i else INK_SOFT)
        cv.text(x + 40, 560, pct(v), "serif", 200, INK, "ls")
        cv.text(x + 44, 620, "23 people, chance of a shared birthday", "serif", 32, INK_SOFT)
    cv.k = 2
    diff = (REAL23 - UNI23) * 100
    cv.text(W / 2, 780, f"a difference of {diff:.1f} points", "serif", 48, INK, "ma")
    cv.text(W / 2, 850, "Uneven days can only raise the odds, and here they raise them by a tenth of a point at most.", "serif", 30, INK_SOFT, "ma")
    source(cv, "Our simulation and exact calculation on national births, 2000–2014.")
    return cv


def b08(stage=99):
    cv = Canvas(stage); heading(cv, "Why so small: nearly every day is close to average"); strip(cv, 1)
    x0, y0, x1, y1 = 205, 290, 1750, 740
    cv.rect(x0, y0, x1, y1, fill=CARD, outline=BORDER, width=1.5, r=6)
    lo_, hi_ = 0.5, 1.2
    Y = lambda r: y1 - (y1 - y0) * (r - lo_) / (hi_ - lo_)
    cv.k = 1
    cv.rect(x0, Y(1.1), x1, Y(0.9), fill=mix(SPARK, CARD, 0.82))
    for r_ in (0.6, 0.8, 1.0, 1.2):
        cv.line([(x0, Y(r_)), (x1, Y(r_))], BORDER, 1); cv.text(x0 - 12, Y(r_), f"{int(r_ * 100)}%", "sans", 19, INK_SOFT, "rm")
    bw = (x1 - x0) / 365
    inside = 0
    for i, (m, d) in enumerate(ALL365):
        r_ = ratio365[(m, d)]; ok = 0.9 <= r_ <= 1.1; inside += ok
        top, bot = sorted((Y(max(min(r_, hi_), lo_)), Y(1.0)))
        cv.rect(x0 + i * bw, top, x0 + i * bw + max(bw * 0.8, 1.2), max(bot, top + 1.5), fill=INK if ok else SPARK)
    cv.text(x0 + 12, y1 + 16, "each bar: one calendar day, January to December", "sans", 20, INK_SOFT)
    cv.text(x1, y1 + 16, "share of an average day", "sans", 20, INK_SOFT, "ra")
    cv.k = 1
    cv.text(M, 815, f"{inside / 365 * 100:.0f}% of days sit within 10% of average", "serifm", 54, INK)
    cv.k = 2
    cv.text(M, 885, "The shaded band is ±10%. Days outside it are marked in the accent.", "serif", 30, INK_SOFT)
    source(cv, "Our count, SSA births 2000–2014, Feb 29 excluded.")
    return cv


WIN90 = [(m, d) for m in (1, 2, 3) for d in range(1, MDAYS[m - 1] + 1) if (m, d) != (2, 29)]   # Jan 1 - Mar 31 = 90 days


def b09(stage=99):
    cv = Canvas(stage); heading(cv, "Third change: how many days there are"); strip(cv, 2)
    inb = lambda m, d: (m, d) in WIN90
    grid(cv, GX, GY, color=lambda m, d: BORDER, dim=lambda m, d: True)
    cv.k = 1
    grid(cv, GX, GY, color=lambda m, d: mix(SPARK, PAGE, 0.78), only=inb, labels=False)
    days, ring = draw_days(random.Random(2702), WIN90, 23, "any")
    cv.k = 2
    draw_dots(cv, GX, GY, days, ring)
    cv.text(GX, GY + 12 * 33 + 36, "Illustration: 23 people all born inside the same 90 days (January 1 to March 31).", "serif", 28, INK_SOFT)
    full = cl["365"]["mean"]; w90 = cl["90"]["mean"]
    cv.k = 3
    big_number(cv, 1300, 420, pct(w90), "23 people, 90-day window", 150, SPARK)
    cv.k = 4
    cv.text(1300, 520, f"full year: {pct(full)}", "serif", 40, INK_SOFT)
    cv.text(1300, 580, "a quarter of the calendar", "serif", 34, INK)
    source(cv, "Our calculation, 90-day window, real weights. Illustration: one random group, seed 2702. Not data.")
    return cv


def table(cv, x, y, headers, rows, colw, rowh=64, hl_col=None, big=False, row_k=None, col_k=None):
    fs = 34 if not big else 38
    cv.rect(x, y, x + sum(colw), y + rowh, fill=PILL)
    cx = x
    for ci_, (h, w_) in enumerate(zip(headers, colw)):
        if col_k: cv.k = col_k[ci_]
        cv.text(cx + 24, y + rowh / 2, h.upper(), "sansm", 20, INK_SOFT, "lm"); cx += w_
    if col_k: cv.k = min(col_k)
    for ri, row in enumerate(rows):
        if row_k: cv.k = row_k[ri]
        yy = y + rowh * (ri + 1)
        cv.rect(x, yy, x + sum(colw), yy + rowh, fill=CARD, outline=BORDER, width=1)
        cx = x
        for ci, (cell, w_) in enumerate(zip(row, colw)):
            if col_k: cv.k = col_k[ci]
            cv.text(cx + 24, yy + rowh / 2, str(cell), "serifm" if ci == hl_col else "serif", fs, SPARK if ci == hl_col else INK, "lm")
            cx += w_
        if col_k: cv.k = min(col_k)
    if row_k: cv.k = 0
    return y + rowh * (len(rows) + 1)


def band(cv, x, y, w, days, total=365, h=26):
    cv.rect(x, y, x + w, y + h, fill=BORDER, r=4)
    cv.rect(x, y, x + max(6, w * days / total), y + h, fill=SPARK, r=4)


def b10(stage=99):
    cv = Canvas(stage); heading(cv, "Slide the window"); strip(cv, 2)
    rows = []
    for dd, lab in ((365, "full year"), (180, "half a year"), (90, "ninety days"), (60, "sixty days"), (30, "same month")):
        v = cl[str(dd)]["mean"]
        rows.append((f"{dd} days", lab, "above 99.99%" if v > .99995 else f"{v * 100:.2f}%"))
    y = table(cv, M, 290, ["window", "", "chance of a shared birthday"], rows, [260, 340, 600], 70, row_k=[1, 2, 3, 4, 5])
    for i, dd in enumerate((365, 180, 90, 60, 30)):
        cv.k = i + 1
        band(cv, 1450, 290 + 70 * (i + 1) + 22, 340, dd)
    cv.k = 6
    cv.text(M, y + 50, "With a window of 7 days, 23 people can't avoid sharing: there aren't enough days.", "serif", 36, INK)
    cv.k = 1
    cv.text(1450, 290 + 22, "share of the year", "sansm", 20, INK_SOFT, "la")
    source(cv, "Our calculation, 23 people, real weights.")
    return cv


def b11(stage=99):
    cv = Canvas(stage); heading(cv, "How many people it takes for even odds"); strip(cv, 2)
    rows = []
    for dd, lab in ((365, "a whole year"), (90, "ninety days"), (60, "sixty days"), (30, "thirty days"), (14, "a fortnight"), (7, "a week")):
        rows.append((f"{dd} days", lab, n50(dd)))
    y = table(cv, M, 290, ["window", "", "people for even odds"], rows, [260, 340, 560], 66, hl_col=2, row_k=[1, 2, 3, 4, 5, 6])
    for i, dd in enumerate((365, 90, 60, 30, 14, 7)):
        cv.k = i + 1
        band(cv, 1450, 290 + 66 * (i + 1) + 20, 340, dd)
    cv.k = 1
    cv.text(1450, 290 + 20, "share of the year", "sansm", 20, INK_SOFT, "la")
    source(cv, "Our calculation; smallest group with at least a 50% chance. Real and even days give the same counts.")
    return cv


def b12(stage=99):
    cv = Canvas(stage); heading(cv, "What actually moved the odds")
    reads = [(f"{pct(pm(10, 365), 0)} → {pct(pm(57, 365), 0)}", "10 → 57 people"),
             (f"{pct(UNI23)} → {pct(REAL23)}", "even days → real calendar"),
             (f"{pct(cl['365']['mean'])} → {pct(cl['90']['mean'])}", "365-day year → 90-day window")]
    cw, gap, y, h = (W - 2 * M - 56) / 3, 28, 190, 200
    for i, name in enumerate(CHAPTERS):
        x = M + i * (cw + gap)
        cv.k = 2
        cv.rect(x, y, x + cw, y + h, fill=CARD, outline=BORDER, width=1.5, r=10)
        cv.text(x + 22, y + 12, name, "sansm", 24, INK_SOFT)
        cv.text(x + 22, y + 50, ["how many are in the group", "how uneven the birthdays are", "how many days they land on"][i], "serif", 25, INK)
        cv.k = 3 + i
        cv.text(x + 22, y + 82, reads[i][0], "serif", 52, INK)
        cv.text(x + 22, y + 152, reads[i][1], "sans", 21, INK_SOFT)
        t, col = [("moves as you'd expect", INK_SOFT), ("barely moves", INK_SOFT), ("decides almost everything", SPARK)][i]
        cv.text(x + 22, 425, t, "serifi", 36, col)
    cv.k = 1
    cv.rect(M, 560, M + 8, 720, fill=SPARK)
    cv.text(M + 30, 566, "INSIDE THE 90-DAY WINDOW", "sansm", 22, INK_SOFT)
    cv.text(M + 30, 650, f"real calendar  {cl['90']['mean'] * 100:.2f}%     even days  {cl['90']['uniform_same_W'] * 100:.2f}%", "serif", 54, INK, "ls")
    cv.text(M + 30, 700, "A tenth of a point at most: seasons weren't the story.", "serif", 32, INK_SOFT, "ls")
    source(cv, "Our calculation.")
    return cv


RAW = [365, 180, 90, 60, 30, 14, 7]


def check(cv, x, y, ok=True, size=15):
    if ok: cv.line([(x - size, y), (x - size * 0.35, y + size * 0.7), (x + size, y - size * 0.8)], SPARK, 4)
    else: cv.line([(x - size * 0.7, y - size * 0.7), (x + size * 0.7, y + size * 0.7)], SEND, 4); cv.line([(x - size * 0.7, y + size * 0.7), (x + size * 0.7, y - size * 0.7)], SEND, 4)


def b13(stage=99):
    cv = Canvas(stage); heading(cv, "The rule")
    m = Math(cv, 80)
    cv.text(M, 215, "n = PEOPLE NEEDED FOR EVEN ODDS     d = NUMBER OF EQUALLY LIKELY DAYS (SLOTS)", "sansm", 21, INK_SOFT)
    items = rule_items(m)
    cv.k = 2
    xr = m.draw(M, 350, items)
    cv.text(xr + 30, 350, "round halves up", "sans", 24, INK_SOFT, "ls")
    cv.k = 1
    rows = [(f"{dd}", f"{math.sqrt(dd):.2f}", rule_n(dd), n50(dd), "") for dd in RAW]
    colw = [200, 250, 250, 300, 100]
    yt = 410
    table(cv, M, yt, ["days d", "square root", "rule gives", "exact answer", ""], rows, colw, 52, hl_col=3, col_k=[1, 3, 4, 1, 1])
    cv.k = 5
    for i, dd in enumerate(RAW):
        check(cv, M + sum(colw[:4]) + 50, yt + 52 * (i + 1) + 26, rule_n(dd) == n50(dd))
    rv = sq["rule_vs_exact"]; tot = rv["range"][1] - rv["range"][0] + 1
    cv.k = 6
    cv.rect(M, 846, M + 8, 912, fill=SPARK)
    cv.text(M + 28, 844, f"exact for {tot - rv['mismatches']:,} of {tot:,} slot counts (2 to 2,000);", "sansm", 27, INK)
    cv.text(M + 28, 880, f"off by one for the other {rv['mismatches']}; never more.", "sansm", 27, INK)
    cv.k = 2
    cv.wrap(1450, 440, "Square root of the days, times 1.2, plus a half, rounded.", "serif", 36, INK, 380, 1.3)
    source(cv, "Our calculation. Checked against the exact answer for every slot count from 2 to 2,000.")
    return cv


def b14(stage=99):
    cv = Canvas(stage); heading(cv, "A school year still covers every day once")
    order = [(m, d) for m in list(range(9, 13)) + list(range(1, 9)) for d in range(1, MDAYS[m - 1] + 1) if (m, d) != (2, 29)]
    rank = {k: i for i, k in enumerate(order)}
    grid(cv, GX, GY - 30, color=lambda m, d: BORDER)
    cv.k = 1
    grid(cv, GX, GY - 30, color=lambda m, d: mix(SPARK, PAGE, 0.80 - 0.35 * rank[(m, d)] / 364), labels=False)
    cv.k = 2
    cv.wrap(GX, GY - 30 + 12 * 33 + 24, "Born between a September 1 cutoff and the next August 31: all 365 calendar days appear once.", "serif", 28, INK_SOFT, 1000)
    cv.text(GX + 1023 + 10, GY - 30 + 8 * 33 + 15, "← cutoff: Sep 1", "sansm", 20, SPARK, "lm")
    cv.k = 3
    cv.text(1400, 380, "ONE SCHOOL-YEAR COHORT", "sansm", 22, INK_SOFT)
    cv.text(1400, 540, pct(cl["365"]["mean"]), "serif", 130, SPARK, "ls")
    cv.k = 4
    cv.wrap(1400, 580, "the same as the full year: it only squeezes if the group is pinned to a narrow stretch of days.", "serif", 32, INK, 420, 1.3)
    source(cv, "Property of the calendar model (shading runs from the September 1 cutoff). Our calculation, real weights.")
    return cv


def b15(stage=99):
    cv = Canvas(stage); heading(cv, "A new case: birth months")
    cw = 118
    cv.k = 1
    for i in range(12):
        cv.rect(M + i * (cw + 8), 180, M + i * (cw + 8) + cw, 260, fill=CARD, outline=BORDER, width=1.5, r=8)
        cv.text(M + i * (cw + 8) + cw / 2, 220, MONTHS[i], "serifm", 34, INK, "mm")
    cv.text(M, 320, "12 slots, if every month were equally likely", "sans", 24, INK_SOFT)
    m = Math(cv, 66)
    steps = [
        [m.sqrt([m.txt("12")]), m.op("≈"), m.txt(f"{math.sqrt(12):.2f}")],
        [m.txt("1.2"), m.op("×"), m.txt(f"{math.sqrt(12):.2f}"), m.op("+"), m.frac([m.txt("1")], [m.txt("2")]), m.op("="), m.txt(f"{1.2 * math.sqrt(12) + .5:.2f}"),
         m.op("→"), m.txt(str(rule_n(12)))],
    ]
    y = 440
    for si, st in enumerate(steps):
        cv.k = 2 + si
        m.draw(M, y, st); y += 120
    cv.k = 5
    cv.text(M, 700, "CHECK, EXACT", "sansm", 22, INK_SOFT)
    for i, n in enumerate((4, 5)):
        cv.k = 5 + i
        x = M + i * 470
        cv.rect(x, 730, x + 420, 880, fill=CARD, outline=SPARK if n == 5 else BORDER, width=3 if n == 5 else 1.5, r=12)
        cv.text(x + 28, 760, f"{n} PEOPLE", "sansm", 22, SPARK if n == 5 else INK_SOFT)
        cv.text(x + 28, 860, pct(pm(n, 12), 0), "serif", 96, INK, "ls")
    cv.k = 4
    cv.wrap(1180, 760, "Five people are enough for even odds that two share a birth month.", "serif", 38, INK, 600, 1.3)
    source(cv, "Our calculation. Equal months assumed.")
    return cv


def b16(stage=99):
    cv = Canvas(stage); heading(cv, "Your turn")
    cv.text(M, 250, "A CLASS OF PEOPLE, EACH PICKING A RANDOM NUMBER FROM 1 TO 50", "sansm", 24, INK_SOFT)
    cv.text(M, 420, "50 slots.", "serifm", 130, INK, "ls")
    cv.k = 1
    cv.text(M, 510, "How many people before two probably match?", "serif", 54, INK)
    m = Math(cv, 72)
    cv.k = 2
    xr = m.draw(M, 690, rule_items(m))
    cv.text(xr + 30, 690, "round halves up", "sans", 24, INK_SOFT, "ls")
    cv.text(M, 770, "n = people needed    d = number of slots", "sans", 24, INK_SOFT)
    cv.k = 3
    cv.text(M, 815, "Tempting, and wrong: half the slots, 25.", "serifi", 36, INK_SOFT)
    cv.k = 4
    cv.rect(M, 880, W - M, 900, fill=BORDER, r=6)
    left = 8 - max(0, min(8, stage - 4)) if stage < 99 else 8
    if stage >= 99: left = 8
    frac = left / 8
    cv.rect(M, 880, M + (W - 2 * M) * frac, 900, fill=SPARK, r=6)
    cv.text(W - M, 915, f"{left} s", "sansm", 24, INK_SOFT, "ra")
    return cv


def b17(stage=99):
    cv = Canvas(stage); heading(cv, "The answer: nine")
    m = Math(cv, 72)
    cv.k = 1
    m.draw(M, 300, [m.sqrt([m.txt("50")]), m.op("≈"), m.txt(f"{math.sqrt(50):.2f}")])
    cv.k = 2
    m.draw(M, 430, [m.txt("1.2"), m.op("×"), m.txt(f"{math.sqrt(50):.2f}"), m.op("+"), m.frac([m.txt("1")], [m.txt("2")]), m.op("="),
                    m.txt(f"{1.2 * math.sqrt(50) + .5:.2f}"), m.op("→"), m.txt(str(rule_n(50)))])
    for i, n in enumerate((9, 8)):
        cv.k = 3 + i
        x = M + i * 520
        cv.rect(x, 520, x + 470, 760, fill=CARD, outline=SPARK if n == 9 else BORDER, width=3 if n == 9 else 1.5, r=12)
        cv.text(x + 30, 556, f"{n} PEOPLE", "sansm", 24, SPARK if n == 9 else INK_SOFT)
        cv.text(x + 30, 700, pct(pm(n, 50), 0), "serif", 130, INK, "ls")
    cv.k = 5
    cv.text(M, 830, "25", "serif", 64, GHOST, "ls")
    cv.line([(M - 6, 810), (M + 62, 784)], SEND, 4)
    cv.text(M + 100, 826, "half the slots, the tempting wrong answer", "serifi", 34, INK_SOFT, "ls")
    cv.k = 6
    cv.text(1180, 600, "The slots set the scale,", "serifm", 46, INK, "ls")
    cv.text(1180, 660, "and their square root", "serifm", 46, INK, "ls")
    cv.text(1180, 720, "sets the crowd.", "serifm", 46, SPARK, "ls")
    source(cv, "Our calculation. Random picks, equally likely.")
    return cv


def b18(stage=99):
    cv = Canvas(stage)
    m = Math(cv, 110)
    items = rule_items(m)
    w = m.width(items)
    m.draw((W - w) / 2, 480, items)
    cv.k = 1
    cv.text(W / 2, 640, "Ask how many slots they could fall into. The square root of that number is about how many it takes.", "serif", 34, INK_SOFT, "ma")
    cv.k = 2
    cv.text(W / 2, 840, "Tanmay Kulkarni, in for Humanitarians AI", "serifm", 44, INK, "ma")
    cv.text(W / 2, 910, "Births data: US NCHS and SSA via FiveThirtyEight (CC BY 4.0). Simulations by the author.", "sans", 26, INK_SOFT, "ma")
    return cv


BEATS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06, "B07": b07, "B08": b08, "B09": b09,
         "B10": b10, "B11": b11, "B12": b12, "B13": b13, "B14": b14, "B15": b15, "B16": b16, "B17": b17, "B18": b18}

# ---------------------------------------------------------------- checks: slate numbers vs spoken figures
def checks():
    r = lambda x, nd=0: round(x * 100, nd)
    assert r(UNI23, 1) == 50.7 and r(REAL23, 1) == 50.8
    assert [r(pm(n, 365)) for n in (10, 30, 50)] == [12, 71, 97] and r(pm(57, 365), 1) >= 99
    assert round((1 - (364 / 365) ** 22) * 100, 1) == 5.9 and math.ceil(math.log(.5) / math.log(364 / 365)) == 253
    mx = max(ratio366, key=ratio366.get)
    assert round((ratio366[mx] - 1) * 100) == 12 and round(ratio366[(2, 29)] * 100) == 25
    assert [r(cl[str(d)]["mean"], 0) for d in (365, 180, 90, 60)] == [51, 77, 95, 99]
    assert [n50(d) for d in (365, 90, 60, 30, 14, 7)] == [23, 12, 10, 7, 5, 4]
    assert r(pm(4, 12)) == 43 and r(pm(5, 12)) == 62 and rule_n(12) == 5
    assert r(pm(9, 50)) == 53 and r(pm(8, 50)) == 45 and rule_n(50) == 9
    assert all(rule_n(d) == n50(d) for d in RAW)
    assert sum(0.9 <= ratio365[k] <= 1.1 for k in ALL365) / 365 > 0.96 - 0.005
    print("checks OK: slate numbers match every figure the narration speaks")


if __name__ == "__main__":
    checks()
    only = sys.argv[1:] or list(BEATS)
    for bid in only:
        BEATS[bid]().save(f"{bid}-16x9.png"); print("wrote", f"{bid}-16x9.png")
