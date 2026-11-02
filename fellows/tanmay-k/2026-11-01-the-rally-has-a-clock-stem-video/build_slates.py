#!/usr/bin/env python3
"""Week 29 review stills: one 3840x2160 slate per beat (B00-B13), at the moment of assertion.

Standalone Pillow drawer (house look as Week 27: cream page, EB Garamond + Inter, OFL fonts). Every figure is
COMPUTED from sim_model.py, then asserted against the signed narration (checks() runs first).
Run: /opt/homebrew/bin/python3.12 build_slates.py   -> _stills/B00-16x9.png ... B13-16x9.png
"""
import math, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sim_model as sm

HERE = Path(__file__).parent
OUT = HERE / "_stills"; OUT.mkdir(exist_ok=True)
FONTS = Path("/Users/tanny/Humanitarians_AI/brutalist.art/runtime/fonts")
S, W, H, M = 2, 1920, 1080, 115
PAGE, CARD, BORDER = "#FAF9F5", "#FFFFFF", "#E5E2D9"
INK, INK_SOFT, GHOST, SPARK, SEND = "#3D3929", "#73705F", "#A9A491", "#D97757", "#C6613F"
SPARK_TEXT, GHOST_TEXT = "#B5532F", "#73705F"
R = sm.checks()
ORD = {1:"first",2:"second",3:"third",4:"fourth",5:"fifth",6:"sixth",7:"seventh",8:"eighth",9:"ninth",10:"tenth",11:"eleventh",
       12:"twelfth",13:"thirteenth",14:"fourteenth",15:"fifteenth",16:"sixteenth",17:"seventeenth",18:"eighteenth",19:"nineteenth",
       20:"twentieth",27:"twenty-seventh"}
_fc = {}
def F(kind, size):
    k = (kind, size)
    if k not in _fc:
        p = {"serif": "EB_Garamond/static/EBGaramond-Regular.ttf", "serifi": "EB_Garamond/static/EBGaramond-Italic.ttf",
             "serifm": "EB_Garamond/static/EBGaramond-Medium.ttf", "sans": "Inter/static/Inter_28pt-Regular.ttf",
             "sansm": "Inter/static/Inter_28pt-Medium.ttf"}[kind]
        _fc[k] = ImageFont.truetype(str(FONTS / p), round(size * S))
    return _fc[k]

class Canvas:
    def __init__(self):
        self.im = Image.new("RGB", (W * S, H * S), PAGE); self.d = ImageDraw.Draw(self.im); self.log = []
    def text(self, x, y, s, kind="sans", size=24, fill=INK, anchor="la"):
        if kind.startswith("sans") and size < 24: size = 24
        if fill == SPARK: fill = SPARK_TEXT if size < 48 else SEND
        if fill == GHOST: fill = GHOST_TEXT
        self.log.append((s, kind, size)); self.d.text((x * S, y * S), s, font=F(kind, size), fill=fill, anchor=anchor)
    def tw(self, s, kind, size): return F(kind, size).getlength(s) / S
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        b = (x0 * S, y0 * S, x1 * S, y1 * S)
        (self.d.rounded_rectangle(b, radius=r * S, fill=fill, outline=outline, width=round(width * S)) if r
         else self.d.rectangle(b, fill=fill, outline=outline, width=round(width * S)))
    def line(self, pts, fill=INK, width=2):
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=round(width * S), joint="curve")
    def dash(self, p0, p1, fill=GHOST, width=2, on=10, off=9):
        (x0, y0), (x1, y1) = p0, p1; L = math.hypot(x1 - x0, y1 - y0); n = max(1, int(L // (on + off)))
        for i in range(n + 1):
            a = i * (on + off) / L; b = min(1, (i * (on + off) + on) / L)
            if a >= 1: break
            self.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)], fill, width)
    def dot(self, x, y, r, fill=INK, outline=None, width=1):
        self.d.ellipse(((x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S), fill=fill, outline=outline, width=round(width * S))
    def wrap(self, x, y, s, kind, size, fill, maxw, lh=1.3):
        words, lines, cur = s.split(), [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if self.tw(t, kind, size) <= maxw: cur = t
            else: lines.append(cur); cur = w_
        lines.append(cur)
        for i, l in enumerate(lines): self.text(x, y + i * size * lh, l, kind, size, fill)
        return y + len(lines) * size * lh
    def save(self, name): self.im.save(OUT / name, optimize=True)

def title(cv, s): cv.text(M, 68, s, "serif", 62, INK)
def chip(cv, f, extra=""):
    s = f"OUR MODEL   field {f.W:.0f} x {f.H:.0f}   paddle {f.h:.0f}   ball starts at {f.vx0:.0f}   +{f.g*100:.0f}% per shot"
    cv.text(M, 1010, s + extra, "sans", 24, INK_SOFT)
def card(cv, x0, y0, x1, y1, on=False):
    cv.rect(x0, y0, x1, y1, fill=CARD, outline=SPARK if on else BORDER, width=3 if on else 2, r=12)

class Fld:
    """Field drawn at scale sc with origin (x0,y0); maps model (x,y) -> logical px. Attacker right, defender left."""
    def __init__(self, cv, f, x0, y0, sc, paddles=True):
        self.cv, self.f, self.x0, self.y0, self.sc = cv, f, x0, y0, sc
        cv.rect(x0, y0, x0 + f.W * sc, y0 + f.H * sc, fill=CARD, outline=BORDER, width=2)
    def p(self, x, y): return (self.x0 + x * self.sc, self.y0 + y * self.sc)
    def paddle(self, side, yc, fill=INK, outline=None):
        f, sc = self.f, self.sc; t = 14
        x = (-t * 0.0) if side == "L" else f.W
        xa, ya = self.p(x if side == "R" else -t * 0.0, yc - f.h / 2); xb, yb = self.p(x + (t if side == "R" else t), yc + f.h / 2)
        if side == "L": xa, xb = self.p(0, 0)[0], self.p(t, 0)[0]
        else: xa, xb = self.p(f.W - t, 0)[0], self.p(f.W, 0)[0]
        self.cv.rect(xa, ya, xb, yb, fill=fill, outline=outline, width=2)
    def ball(self, x, y, r=8, fill=SPARK): self.cv.dot(*self.p(x, y), r, fill)

def bars(cv, x, y, w, can, must, tag="", maxv=300, hi=False, l1="PADDLE CAN TRAVEL IN ONE CROSSING", l2="PADDLE MUST TRAVEL"):
    """The framework widget: two bars (can travel / must travel) with the line at 'must'."""
    cv.text(x, y, l1, "sans", 24, INK_SOFT)
    cv.rect(x, y + 34, x + w, y + 70, fill="#EDEBE1", r=4); L = min(w, w * can / maxv)
    cv.rect(x, y + 34, x + L, y + 70, fill=INK if can >= must else SPARK, r=4)
    cv.text(x + w, y, f"{can:.0f} px", "sans", 24, INK, "ra")
    cv.text(x, y + 100, l2, "sans", 24, INK_SOFT)
    cv.rect(x, y + 134, x + w, y + 170, fill="#EDEBE1", r=4); cv.rect(x, y + 134, x + w * must / maxv, y + 170, fill=GHOST, r=4)
    cv.text(x + w, y + 100, f"{must:.1f} px", "sans", 24, INK, "ra")
    lx = x + w * must / maxv; cv.dash((lx, y + 34), (lx, y + 176), fill=SEND, width=3)
    if tag: cv.text(x, y + 190, tag, "sans", 24, SPARK)

def shot_dots(cv, x, y, n_def, n_total, r=15, gap=44, brk=True):
    for i in range(n_total):
        cx = x + i * gap
        if i < n_def: cv.dot(cx, y, r, INK)
        else: cv.dot(cx, y, r, SPARK)
        cv.text(cx, y + 34, str(i + 1), "sans", 24, INK_SOFT, "ma")

old, new = sm.OLD, sm.NEW
n6 = 5                      # zero-based index of the sixth shot
T6, vx6 = old.T(n6), old.vx(n6)
can6 = 2.0 * T6; must = (old.H - old.h) / 2        # 224 vs 232.5
gap6 = must - can6
assert abs(can6 - 224.0) < 1 and abs(gap6 - 8.4) < 0.5

def b00():
    cv = Canvas(); title(cv, "Shot six")
    fl = Fld(cv, old, M, 190, 1.15)
    yd0 = old.H / 2; yd1 = yd0 - can6
    fl.paddle("L", yd0, fill="#EDEBE1", outline=GHOST); fl.paddle("L", yd1, fill=INK)
    fl.paddle("R", old.H / 2, fill=INK)
    cv.dash(fl.p(old.W - 14, old.H / 2), fl.p(10, 0), fill=SPARK, width=3)
    fl.ball(8, 0, 10)
    bx = fl.p(24, 0)[0]; cv.line([(bx, fl.p(0, 0)[1]), (bx, fl.p(0, gap6)[1])], SEND, 4)
    ly = fl.p(0, 190)[1]; cv.line([(bx, fl.p(0, gap6 / 2)[1]), (bx, ly - 8)], SEND, 2)
    cv.text(bx - 6, ly, f"{gap6:.1f} px short", "sans", 28, SPARK)
    cv.text(fl.p(40, 0)[0], fl.p(0, yd0)[1] + 50, "where the paddle started", "sans", 24, INK_SOFT)
    cv.text(M, 830, "paddle speed 2.0: the paddle reached as far as it can, and the ball still went by.", "serif", 30, INK)
    cv.text(1250, 190, "SHOT", "sans", 28, INK_SOFT); cv.text(1250, 215, "6", "serif", 230, SEND)
    shot_dots(cv, 1262, 560, 5, 6)
    bars(cv, 1250, 640, 540, can6, must, maxv=300)
    chip(cv, old); return cv

def b01():
    cv = Canvas(); title(cv, "The claim")
    for i, t in enumerate(["no perfect defense", "a game to eleven"]):
        y = 230 + i * 250; card(cv, M, y, W - M, y + 200); cv.text(M + 60, y + 52, f"“{t}”", "serifi", 100, INK)
    cv.text(M, 770, "Two phrases from an essay in the Humanitarians AI repo.", "sans", 30, INK_SOFT)
    cv.text(M, 850, "When is it true? A sentence like that should come with a number.", "serif", 52, SEND)
    return cv

def b02():
    cv = Canvas(); title(cv, "The smallest Pong")
    fl = Fld(cv, old, M, 190, 1.0)
    fl.paddle("L", 200); fl.paddle("R", 330); fl.ball(500, 150, 9)
    ax = M - 36   # arrows: paddles move up and down only
    cv.line([(ax, 330), (ax, 440)], INK_SOFT, 3); cv.line([(ax - 8, 346), (ax, 330), (ax + 8, 346)], INK_SOFT, 3); cv.line([(ax - 8, 424), (ax, 440), (ax + 8, 424)], INK_SOFT, 3)
    cv.text(M, 750, "paddles move up and down only; the ball bounces off the top and bottom", "sans", 26, INK_SOFT)
    card(cv, 1020, 190, W - M, 590)
    cv.text(1060, 215, "WHERE THE BALL HITS THE PADDLE", "sans", 24, INK_SOFT); cv.text(1060, 250, "steers where it goes", "serif", 44, INK)
    px, py = 1100, 350; cv.rect(px, py, px + 16, py + 180, fill=INK)
    for dy, ang, lab in ((24, -0.3, "top: up"), (90, 0.0, "middle: straight"), (156, 0.3, "bottom: down")):
        x0, y0 = px + 16, py + dy; cv.line([(x0, y0), (x0 + 200, y0 + 100 * ang)], SEND, 4); cv.dot(x0, y0, 7, SPARK)
        cv.text(x0 + 225, y0 + 100 * ang - 14, lab, "sans", 24, INK_SOFT)
    card(cv, 1020, 620, W - M, 900, True)
    cv.text(1060, 645, "EVERY NUMBER COMES FROM THESE", "sans", 24, SPARK)
    for i, s in enumerate([f"field  {old.W:.0f} by {old.H:.0f}", f"paddle  {old.h:.0f} long", f"ball starts at  {old.vx0:.0f} per tick",
                           f"speeds up  {old.g*100:.0f}% every shot"]): cv.text(1060, 690 + i * 48, s, "serif", 36, INK)
    cv.text(M, 830, "This is my model, not any machine you remember.", "serif", 44, INK)
    chip(cv, old); return cv

def b03():
    cv = Canvas(); title(cv, "What the defender knows")
    fl = Fld(cv, old, M, 190, 1.0); fl.paddle("L", old.H / 2, fill="#EDEBE1", outline=GHOST); fl.paddle("R", 120)
    ya, vy = 120.0, 1.35 * old.vx0; pts = []; n = 143
    for i in range(n + 1):
        x = old.W - 14 - i * (old.W - 28) / n; pts.append(fl.p(x, old.fold(ya + vy * i * old.T(0) / n)))
    for a, b in zip(pts[::6], pts[3::6]): cv.line([a, b], SPARK, 3)
    fl.ball(old.W - 14, ya, 9)
    cv.text(M, 740, "direction is fixed at the hit:", "serif", 36, INK); cv.text(M, 785, "the defender sees where it is going.", "serif", 36, INK)
    card(cv, 1020, 190, W - M, 410)
    cv.text(1060, 215, "ONE CROSSING", "sans", 24, INK_SOFT); cv.text(1060, 250, f"{old.T(0):.0f} ticks", "serif", 72, SEND)
    cv.text(1060, 335, "that is all the time there is", "serif", 32, INK_SOFT)
    bars(cv, 1020, 460, 780, 2.0 * old.T(0), must, maxv=300, tag="the two bars: can travel, must travel", hi=True)
    chip(cv, old); return cv

def b04():
    cv = Canvas(); title(cv, "The worst shot")
    fl = Fld(cv, old, M, 190, 1.0); ya = old.H / 2
    fl.paddle("R", ya); fl.paddle("L", old.H / 2, fill=INK)
    k = 17
    for i in range(k):
        ly = i * old.H / (k - 1); ext = i in (0, k - 1)
        cv.line([fl.p(old.W - 14, ya), fl.p(14, ly)], SPARK if ext else "#E8C9BA", 4 if ext else 2)
        cv.dot(*fl.p(8, ly), 6 if not ext else 9, SPARK if ext else GHOST)
    cv.text(fl.p(330, 0)[0], fl.p(0, 0)[1] + 14, "worst shot: lands at the edge", "sans", 24, SPARK)
    cv.text(M, 735, "The defender cannot know the aim in advance, so it waits in the middle.", "serif", 34, INK)
    cv.text(M, 785, f"The farthest landing is half the field away: {old.H/2:.1f} px.", "serif", 34, INK)
    card(cv, 1100, 190, W - M, 520, True)
    cv.text(1140, 215, "HALF THE FIELD", "sans", 24, SPARK); cv.text(1140, 250, f"{old.H/2:.1f}", "serif", 110, SEND)
    cv.text(1140, 390, f"less the paddle's own half-length, {old.h/2:.0f}", "serif", 32, INK_SOFT)
    cv.text(1140, 435, f"= must travel {must:.1f} px", "serif", 40, INK)
    chip(cv, old); return cv

def b05():
    cv = Canvas(); title(cv, "The line")
    bars(cv, M, 190, 900, can6 * 1.0, must, maxv=300, tag="at shot six the bar has sunk below the line")
    card(cv, 1100, 190, W - M, 560, True)
    cv.text(1140, 215, "PADDLE SPEED / BALL SIDEWAYS SPEED", "sans", 24, SPARK); cv.text(1140, 255, f"{R['line_full']:.2f}", "serif", 180, SEND)
    cv.text(1140, 470, "a little over a quarter", "serif", 40, INK)
    card(cv, M, 620, W - M, 930)
    cv.text(M + 40, 650, "THE FORM, FOR ANY FIELD", "sans", 24, INK_SOFT)
    cv.text(M + 40, 695, "the defender's reach in one flight   against   half the free height", "serif", 52, INK)
    cv.text(M + 40, 790, f"({old.H:.0f} − {old.h:.0f}) ÷ (2 × {old.W:.0f})  =  {R['line_full']:.3f}", "sans", 36, INK)
    cv.text(M + 40, 855, "a brute-force search that tries every aim found 0.272", "sans", 26, INK_SOFT)
    chip(cv, old); return cv

def lanes_row(cv, y, label, speed, brk, nmax=15, sub=""):
    cv.text(M, y - 6, label, "sans", 28, INK); cv.text(M, y + 34, sub, "sans", 24, INK_SOFT)
    x0 = 520
    for i in range(nmax):
        cx = x0 + i * 78
        if i < brk: cv.dot(cx, y + 20, 22, INK)
        elif i == brk: cv.dot(cx, y + 20, 22, SPARK); cv.text(cx, y + 56, f"shot {i+1}", "sans", 24, SPARK, "ma")
        else: cv.dot(cx, y + 20, 22, "#EDEBE1")
        if i != brk: cv.text(cx, y + 56, str(i + 1), "sans", 24, GHOST, "ma")

def b06():
    cv = Canvas(); title(cv, "Turn the dial")
    cv.text(M, 150, "same rally, same rules, only the paddle's speed changes", "serif", 34, INK_SOFT)
    for i, (vp, name) in enumerate([(1.0, "too slow"), (2.0, "middle"), (3.0, "fast")]):
        y = 250 + i * 190; b = R['bk_old'][vp]
        lanes_row(cv, y, f"paddle speed {vp:.1f}", vp, b, sub=name)
    cv.text(M, 850, "filled = defended    orange = the shot that gets past", "sans", 24, INK_SOFT)
    cv.text(M, 900, f"breaks on shot {R['bk_old'][1.0]+1}, shot {R['bk_old'][2.0]+1}, shot {R['bk_old'][3.0]+1}", "serif", 44, SEND)
    chip(cv, old); return cv

def b07():
    cv = Canvas(); title(cv, "The clock")
    x0, y0, w, h = 190, 240, 880, 600; cv.rect(x0, y0, x0 + w, y0 + h, fill=CARD, outline=BORDER, width=2)
    vmax = 480.0; xs = lambda s: x0 + (s - 0.5) * w / 15.5; ys = lambda v: y0 + h - v / vmax * h
    for v in (0, 100, 200, 300, 400): cv.dash((x0, ys(v)), (x0 + w, ys(v)), "#EDEBE1", 1); cv.text(x0 - 14, ys(v), str(v), "sans", 24, INK_SOFT, "rm")
    for s_ in range(1, 16): cv.text(xs(s_), y0 + h + 14, str(s_), "sans", 24, INK_SOFT, "ma")
    cv.text(x0 + w / 2, y0 + h + 52, "shot", "sans", 24, INK_SOFT, "ma"); cv.text(M, y0 - 38, "px the paddle can travel in one crossing", "sans", 24, INK_SOFT)
    cv.dash((x0, ys(must)), (x0 + w, ys(must)), SEND, 3); cv.text(x0 + w + 16, ys(must) - 14, f"must travel {must:.1f}", "sans", 24, SPARK)
    for vp, col, lab in ((3.0, GHOST, "paddle speed 3.0"), (2.0, INK, "paddle speed 2.0")):
        pts = [(xs(s_), ys(vp * old.T(s_ - 1))) for s_ in range(1, 16)]; cv.line(pts, col, 4)
        for p_ in pts: cv.dot(*p_, 6, col)
        b = R['bk_old'][vp] + 1; cv.dot(*pts[b - 1], 12, SPARK); cv.text(pts[b - 1][0], pts[b - 1][1] + 26, f"shot {b}", "sans", 24, SPARK, "ma")
        cv.text(pts[0][0] + 30, pts[0][1] - 48, lab, "sans", 24, col if col != GHOST else INK_SOFT)
    tx = 1330
    cv.text(tx, 250, "The ball speeds up", "serif", 40, INK); cv.text(tx, 298, "on every shot.", "serif", 40, INK)
    cv.text(tx, 380, "So the crossing gets shorter,", "serif", 40, INK); cv.text(tx, 428, "and what the paddle can cover", "serif", 40, INK)
    cv.text(tx, 476, "in one crossing shrinks with it.", "serif", 40, INK)
    cv.text(tx, 560, "In my model,", "serif", 46, SEND); cv.text(tx, 614, "a rally has a clock inside it.", "serif", 46, SEND)
    bars(cv, tx, 730, 480, can6, must, maxv=300, tag="shot six, paddle speed 2.0", l1="CAN TRAVEL", l2="MUST TRAVEL")
    chip(cv, old); return cv

def table(cv, x, y, cols, rows, widths, rh=96, hl=None):
    cx = x
    for c, wd in zip(cols, widths): cv.text(cx, y, c, "sans", 24, INK_SOFT); cx += wd
    cv.line([(x, y + 40), (x + sum(widths), y + 40)], BORDER, 2)
    for i, r in enumerate(rows):
        cx = x
        for j, (c, wd) in enumerate(zip(r, widths)):
            cv.text(cx, y + 62 + i * rh, c, "serif", 52, SEND if (hl and j in hl) else INK); cx += wd

def b08():
    cv = Canvas(); title(cv, "Predicted, then found")
    rows = []
    for vp in (2.0, 3.0):
        rows.append([f"{vp:.1f}", f"{R['spd'][vp]:.2f} speed-ups", ORD[R['pred_old'][vp] + 1], ORD[R['bk_old'][vp] + 1]])
    table(cv, M, 230, ["PADDLE SPEED", "ARITHMETIC SAYS", "SO THE BREAK IS SHOT", "THE SEARCH FOUND"], rows, [260, 470, 470, 420], 110, hl=(2, 3))
    cv.text(M, 590, "The search tries every aim at every shot. The arithmetic is one line.", "serif", 40, INK)
    cv.text(M, 650, "They agree, so the line can be trusted for this model.", "serif", 40, INK)
    cv.text(M, 780, "ln(speed / (0.271 x 6)) / ln(1.05) speed-ups, rounded up to the next shot", "sans", 26, INK_SOFT)
    chip(cv, old); return cv

def b09():
    cv = Canvas(); title(cv, "The second dial")
    fl = Fld(cv, old, M, 190, 0.85); ya = old.H / 2; fl.paddle("R", ya); fl.paddle("L", old.H / 2)
    q = 0.25; half = q * old.W; lo, hi = max(0, ya - half), min(old.H, ya + half)
    for ly in (lo, hi): cv.line([fl.p(old.W - 14, ya), fl.p(14, ly)], SPARK, 4)
    for i in range(1, 6):
        ly = lo + i * (hi - lo) / 6; cv.line([fl.p(old.W - 14, ya), fl.p(14, ly)], "#E8C9BA", 2)
    cv.text(M, 680, "a hit steers the ball less:", "serif", 34, INK); cv.text(M, 722, "up and down speed at most a quarter of sideways speed", "serif", 34, INK)
    cv.text(M, 860, f"0.25 \u2212 {old.h:.0f} \u00f7 (2 \u00d7 {old.W:.0f}) = {R['line_narrow']:.3f}", "sans", 26, INK_SOFT)
    cv.text(1000, 190, "THE LINE DROPS", "sans", 24, INK_SOFT)
    cv.text(1000, 225, f"{R['line_full']:.3f}", "serif", 90, GHOST); cv.text(1280, 255, "\u2192", "serif", 60, INK); cv.text(1360, 225, f"{R['line_narrow']:.3f}", "serif", 90, SEND)
    cv.text(1000, 345, "WHERE THE DEFENSE BREAKS, PADDLE SPEEDS 2.0 AND 3.0", "sans", 24, INK_SOFT)
    base, sc = 1000, 40
    for s_ in range(1, 21): cv.rect(base + (s_ - 1) * sc, 395, base + s_ * sc - 4, 435, fill="#EDEBE1")
    for s_ in (1, 5, 10, 15, 20): cv.text(base + (s_ - 1) * sc + 18, 445, str(s_), "sans", 24, INK_SOFT, "ma")
    for vp in (2.0, 3.0):
        for who, col in ((R['bk_old'][vp] + 1, GHOST), (R['pred_narrow'][vp] + 1, SEND)):
            cv.rect(base + (who - 1) * sc, 395, base + who * sc - 4, 435, fill=col)
    cv.rect(1000, 490, 1030, 516, fill=GHOST); cv.text(1044, 486, "full aim", "sans", 24, INK_SOFT)
    cv.rect(1200, 490, 1230, 516, fill=SEND); cv.text(1244, 486, "aim at most a quarter", "sans", 24, INK_SOFT)
    card(cv, 1000, 560, W - M, 850, True)
    cv.text(1040, 585, "ARITHMETIC FIRST, THEN THE COUNT", "sans", 24, SPARK)
    rows = [("full aim", f"{ORD[R['bk_old'][2.0]+1]}, {ORD[R['bk_old'][3.0]+1]}", INK_SOFT),
            ("predicted", f"{ORD[R['pred_narrow'][2.0]+1]}, {ORD[R['pred_narrow'][3.0]+1]}", INK),
            ("found", f"{ORD[R['bk_narrow'][2.0]+1]}, {ORD[R['bk_narrow'][3.0]+1]}", SEND)]
    for i, (a, b, c) in enumerate(rows):
        cv.text(1040, 635 + i * 68, a, "serif", 40, INK_SOFT); cv.text(1300, 635 + i * 68, b, "serif", 44, c)
    chip(cv, old, "   aim limited to a quarter"); return cv

def b10():
    cv = Canvas(); title(cv, "A different field")
    sc = 0.5
    for i, (f, lab, ln) in enumerate([(old, "858 by 525, paddle 60", R['line_full']), (new, "1200 by 500, paddle 50", R['line_new'])]):
        x0 = M + i * 880; fl = Fld(cv, f, x0, 190, sc); fl.paddle("L", f.H / 2); fl.paddle("R", f.H / 2)
        for ly in (0, f.H): cv.line([fl.p(f.W - 14, f.H / 2), fl.p(14, ly)], SPARK, 3)
        cv.text(x0, 190 + 262 + 16, lab, "sans", 26, INK_SOFT); cv.text(x0, 190 + 262 + 52, f"line  {ln:.4g}", "serif", 52, SEND if i else INK)
    cv.text(M + 440 + 190, 360, "same form", "serifi", 44, SPARK)
    rows = [[f"{vp:.1f}", ORD[R['pred_new'][vp] + 1], ORD[R['bk_new'][vp] + 1]] for vp in (1.5, 2.5, 4.0)]
    table(cv, M, 640, ["PADDLE SPEED", "ARITHMETIC SAYS SHOT", "THE SEARCH FOUND"], rows, [360, 640, 520], 84, hl=(1, 2))
    chip(cv, new); return cv

def b11():
    cv = Canvas(); title(cv, "Which rule?")
    xs = [M, 700, 1285]; w = 520
    texts = [("DIAL ONE", "how fast the paddle moves", [f"speed {vp:.1f}: shot {R['bk_old'][vp]+1}" for vp in (1.0, 2.0, 3.0)]),
             ("DIAL TWO", "how much a hit can steer", [f"full aim: shot {R['bk_old'][2.0]+1}, {R['bk_old'][3.0]+1}", f"narrow aim: shot {R['bk_narrow'][2.0]+1}, {R['bk_narrow'][3.0]+1}"]),
             ("REMOVE THE SPEED-UP", "the ball never gets faster", ["speed 2.0: no break", "speed 3.0: no break", "in 200 shots"])]
    for i, (a, b, ls) in enumerate(texts):
        card(cv, xs[i], 200, xs[i] + w, 640, i == 2); cv.text(xs[i] + 30, 225, a, "sans", 24, SPARK if i == 2 else INK_SOFT)
        cv.wrap(xs[i] + 30, 265, b, "serif", 40, INK, w - 60, 1.15)
        for j, l in enumerate(ls): cv.text(xs[i] + 30, 400 + j * 62, l, "serif", 38, SEND if i == 2 else INK)
    cv.text(M, 740, "A fast enough paddle, against a ball that never speeds up, held for two hundred shots.", "serif", 44, INK)
    cv.text(M, 805, "The speeding up is what makes the sentence true.", "serif", 44, SEND)
    chip(cv, old); return cv

def b12():
    cv = Canvas(); title(cv, "What this does not claim")
    cv.text(M, 190, "A model, not a machine. Left out on purpose:", "serif", 52, INK)
    for i, s in enumerate(["spin on the ball", "human reaction time", "the edges of the paddle", "numbers from any real machine"]):
        y = 300 + i * 120; card(cv, M, y, 1000, y + 90); cv.text(M + 36, y + 14, s, "serif", 48, INK)
    cv.text(M, 830, "It shows when a rule set can be defended perfectly.", "serif", 44, INK)
    cv.text(M, 890, "It does not say how any particular game was built.", "serif", 44, INK_SOFT)
    chip(cv, old); return cv

def b13(hold=False):
    cv = Canvas(); title(cv, "Your turn")
    cf = sm.Field(W=1000, H=500, h=50)
    card(cv, M, 190, 1000, 500, True); cv.text(M + 40, 215, "THE LINE", "sans", 24, SPARK)
    cv.text(M + 40, 265, "(height − paddle) ÷ (2 × width)", "serif", 56, INK)
    cv.text(M + 40, 335, f"({cf.H:.0f} − {cf.h:.0f}) ÷ (2 × {cf.W:.0f})  =  " + ("?" if hold else f"{R['line_card']:.3f}"), "serif", 64, SEND)
    if hold:
        cv.text(M, 960, "work it out: five-second hold", "sans", 24, GHOST); return cv
    cv.text(M + 40, 440, "field 1000 wide, 500 tall, paddle 50 long", "sans", 24, INK_SOFT)
    for i, (r, verdict, on) in enumerate([(0.25, "a perfect defense at the serve", True), (0.20, "not a perfect defense", False)]):
        y = 540 + i * 180; card(cv, M, y, 1000, y + 156)
        cv.text(M + 40, y + 24, f"paddle at {r:.2f} of the ball's speed", "serif", 44, INK); cv.text(M + 40, y + 88, verdict, "serif", 44, SEND if on else INK_SOFT)
        cv.text(940, y + 24, ">" if r > R['line_card'] else "<", "serif", 80, SEND, "ra")
    assert 0.25 > R['line_card'] > 0.20
    cv.text(1100, 215, "ONE DIAL, ONLY ONE:", "sans", 24, INK_SOFT); cv.text(1100, 255, "where would you put it?", "serif", 64, INK)
    for i, s in enumerate(["how fast the paddle moves", "how much a hit can steer", "how fast the ball speeds up"]): cv.text(1130, 370 + i * 64, s, "serif", 40, INK_SOFT)
    cv.text(M, 960, "answer shown after a five-second hold", "sans", 24, GHOST)
    return cv

BEATS = [("B00", b00), ("B01", b01), ("B02", b02), ("B03", b03), ("B04", b04), ("B05", b05), ("B06", b06),
         ("B07", b07), ("B08", b08), ("B09", b09), ("B10", b10), ("B11", b11), ("B12", b12), ("B13", b13)]
if __name__ == "__main__":
    only = sys.argv[1:]
    dump = []
    for bid, fn in BEATS:
        if only and bid not in only: continue
        cv = fn(); cv.save(f"{bid}-16x9.png"); dump.append(f"## {bid}\n" + "\n".join(f"{k:7s} {sz:>4}  {s}" for s, k, sz in cv.log))
        print("wrote", bid)
        if bid == "B13": b13(hold=True).save("B13-hold-16x9.png"); print("wrote B13-hold")
    (HERE / "_stills" / "onscreen.txt").write_text("\n".join(dump))
