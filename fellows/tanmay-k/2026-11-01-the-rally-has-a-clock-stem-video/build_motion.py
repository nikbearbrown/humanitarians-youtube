#!/usr/bin/env python3
"""Week 29 motion: each beat is a set of STAGES (full 3840x2160 slates, cumulative or state-driven), cross-faded on the cue times in CUES.json.

A stage image is drawn once with Pillow (no alpha tricks); the fade between two stages is a true Image.blend, so the old element
leaves exactly as the new one arrives (old = 1 - e, new = e, one eased progress). Each beat dissolves from the previous beat's last
frame over the first 0.25 s. Frames are written as JPEG (q 95, 4:4:4) and joined with ffmpeg's concat demuxer; static holds are one
image with a duration, only the fades are per-frame.

Run:  /opt/homebrew/bin/python3.12 build_motion.py            -> all beats, 4 in parallel  -> _beats/Bxx.mp4 (silent), _motion/stages-check
      /opt/homebrew/bin/python3.12 build_motion.py B07 B09    -> only those beats
"""
import json, math, shutil, subprocess, sys
from multiprocessing import Pool
from pathlib import Path
from PIL import Image
import build_slates as bs
from build_slates import (Canvas, Fld, S, W, H, M, PAGE, INK, INK_SOFT, GHOST, SPARK, SEND, BORDER, CARD, R, ORD, old, new, can6, must,
                          gap6, title, chip, card, bars, table, F)
import sim_model as sm

HERE = Path(__file__).parent
CUES = json.loads((HERE / "CUES.json").read_text())
FPS, FADE, RAMP_FADE, DISSOLVE = 30, 0.35, 0.10, 0.25


class G(Canvas):
    """Canvas whose draw calls are gated: an element drawn while self.k > self.stage is skipped."""
    def __init__(self, stage):
        super().__init__(); self.stage, self.k = stage, 0
    def _on(self): return self.k <= self.stage
    def text(self, *a, **k):
        if self._on(): super().text(*a, **k)
    def rect(self, *a, **k):
        if self._on(): super().rect(*a, **k)
    def line(self, *a, **k):
        if self._on(): super().line(*a, **k)
    def dot(self, *a, **k):
        if self._on(): super().dot(*a, **k)
    def dash(self, p0, p1, **k):
        if self._on(): super().dash(p0, p1, **k)


def ramp(t0, t1, n):
    """n stage times evenly spread over [t0, t1)."""
    return [t0 + (t1 - t0) * i / n for i in range(n)]

def ev(bid, name):
    for e in CUES[bid]["events"]:
        if e["event"] == name: return e["t"]
    raise KeyError((bid, name))


# ------------------------------------------------------------------ stage drawers (stage -> 4K image)
def d_b00(stage):
    cv = G(stage); title(cv, "Shot six")
    fl = Fld(cv, old, M, 190, 1.15); mid = old.H / 2
    fl.paddle("R", mid)
    n = 0 if stage == 0 else min(stage, 6)
    if n == 0: fl.paddle("L", mid)
    can = 2.0 * old.T(max(n, 1) - 1)
    if n >= 1:
        fl.paddle("L", mid, fill="#EDEBE1", outline=GHOST)
        cv.dash(fl.p(old.W - 14, mid), fl.p(10, 0), fill=SPARK, width=3)
        fl.ball(8, 0, 10)
        yd = old.h / 2 if n < 6 else mid - can6
        fl.paddle("L", yd, fill=INK)
    cv.text(1250, 190, "SHOT", "sans", 28, INK_SOFT)
    if n >= 1: cv.text(1250, 215, str(n), "serif", 230, SEND if n == 6 else INK)
    for i in range(6):
        cx = 1262 + i * 44
        if i < n: cv.dot(cx, 560, 15, SPARK if i == 5 else INK)
        else: cv.dot(cx, 560, 15, "#EDEBE1")
        cv.text(cx, 594, str(i + 1), "sans", 24, INK_SOFT, "ma")
    bars(cv, 1250, 640, 540, can, must, maxv=300)
    if stage >= 7:
        bx = fl.p(24, 0)[0]; cv.line([(bx, fl.p(0, 0)[1]), (bx, fl.p(0, gap6)[1])], SEND, 4)
        ly = fl.p(0, 190)[1]; cv.line([(bx, fl.p(0, gap6 / 2)[1]), (bx, ly - 8)], SEND, 2)
        cv.text(bx - 6, ly, f"{gap6:.1f} px short", "sans", 28, SPARK)
        cv.text(M, 830, "paddle speed 2.0: the paddle reached as far as it can, and the ball still went by.", "serif", 30, INK)
    chip(cv, old); return cv.im

def d_b01(stage):
    cv = G(stage); title(cv, "The claim")
    for i, t in enumerate(["no perfect defense", "a game to eleven"]):
        cv.k = i + 1; y = 230 + i * 250; card(cv, M, y, W - M, y + 200); cv.text(M + 60, y + 52, f"“{t}”", "serifi", 100, INK)
    cv.k = 2; cv.text(M, 770, "Two phrases from an essay in the Humanitarians AI repo.", "sans", 30, INK_SOFT)
    cv.k = 3; cv.text(M, 850, "When is it true? A sentence like that should come with a number.", "serif", 52, SEND)
    return cv.im

def d_b02(stage):
    cv = G(stage); title(cv, "The smallest Pong")
    fl = Fld(cv, old, M, 190, 1.0)
    cv.k = 1; fl.paddle("L", 200); fl.paddle("R", 330)
    ax = M - 36; cv.line([(ax, 330), (ax, 440)], INK_SOFT, 3); cv.line([(ax - 8, 346), (ax, 330), (ax + 8, 346)], INK_SOFT, 3); cv.line([(ax - 8, 424), (ax, 440), (ax + 8, 424)], INK_SOFT, 3)
    cv.k = 2; fl.ball(500, 150, 9); cv.text(M, 750, "paddles move up and down only; the ball bounces off the top and bottom", "sans", 26, INK_SOFT)
    cv.k = 3; card(cv, 1020, 190, W - M, 590)
    cv.text(1060, 215, "WHERE THE BALL HITS THE PADDLE", "sans", 24, INK_SOFT); cv.text(1060, 250, "steers where it goes", "serif", 44, INK)
    px, py = 1100, 350; cv.rect(px, py, px + 16, py + 180, fill=INK)
    for dy, ang, lab in ((24, -0.3, "top: up"), (90, 0.0, "middle: straight"), (156, 0.3, "bottom: down")):
        x0, y0 = px + 16, py + dy; cv.line([(x0, y0), (x0 + 200, y0 + 100 * ang)], SEND, 4); cv.dot(x0, y0, 7, SPARK)
        cv.text(x0 + 225, y0 + 100 * ang - 14, lab, "sans", 24, INK_SOFT)
    cv.k = 4; cv.text(M, 830, "This is my model, not any machine you remember.", "serif", 44, INK); chip(cv, old)
    cv.k = 5; card(cv, 1020, 620, W - M, 900, True); cv.text(1060, 645, "EVERY NUMBER COMES FROM THESE", "sans", 24, SPARK)
    for i, s in enumerate([f"field  {old.W:.0f} by {old.H:.0f}", f"paddle  {old.h:.0f} long", f"ball starts at  {old.vx0:.0f} per tick", f"speeds up  {old.g*100:.0f}% every shot"]):
        cv.text(1060, 690 + i * 48, s, "serif", 36, INK)
    return cv.im

def d_b03(stage):
    cv = G(stage); title(cv, "What the defender knows")
    fl = Fld(cv, old, M, 190, 1.0); fl.paddle("L", old.H / 2, fill="#EDEBE1", outline=GHOST); fl.paddle("R", 120)
    cv.k = 1; ya, vy = 120.0, 1.35 * old.vx0; pts = []; n = 143
    for i in range(n + 1):
        x = old.W - 14 - i * (old.W - 28) / n; pts.append(fl.p(x, old.fold(ya + vy * i * old.T(0) / n)))
    for a, b in zip(pts[::6], pts[3::6]): cv.line([a, b], SPARK, 3)
    fl.ball(old.W - 14, ya, 9)
    cv.k = 2; cv.text(M, 740, "direction is fixed at the hit:", "serif", 36, INK); cv.text(M, 785, "the defender sees where it is going.", "serif", 36, INK)
    cv.k = 3; card(cv, 1020, 190, W - M, 410); cv.text(1060, 215, "ONE CROSSING", "sans", 24, INK_SOFT); cv.text(1060, 250, f"{old.T(0):.0f} ticks", "serif", 72, SEND)
    cv.text(1060, 335, "that is all the time there is", "serif", 32, INK_SOFT)
    cv.k = 4; bars(cv, 1020, 460, 780, 2.0 * old.T(0), must, maxv=300)
    cv.k = 5; cv.text(1020, 665, "CAN TRAVEL: how far the paddle can go in one crossing", "sans", 24, SPARK)
    cv.k = 6; cv.text(1020, 705, "MUST TRAVEL: how far the worst shot makes it go", "sans", 24, SPARK)
    chip(cv, old); return cv.im

def d_b04(stage):
    cv = G(stage); title(cv, "The worst shot")
    fl = Fld(cv, old, M, 190, 1.0); ya = old.H / 2; fl.paddle("R", ya)
    cv.k = 1; k = 17
    for i in range(k):
        ly = i * old.H / (k - 1); ext = i in (0, k - 1)
        if not ext or stage >= 3: cv.line([fl.p(old.W - 14, ya), fl.p(14, ly)], SPARK if ext else "#E8C9BA", 4 if ext else 2)
        else: cv.line([fl.p(old.W - 14, ya), fl.p(14, ly)], "#E8C9BA", 2)
        cv.dot(*fl.p(8, ly), 9 if (ext and stage >= 3) else 6, SPARK if (ext and stage >= 3) else GHOST)
    cv.k = 2; fl.paddle("L", old.H / 2, fill=INK); cv.text(M, 735, "The defender cannot know the aim in advance, so it waits in the middle.", "serif", 34, INK)
    cv.k = 3; cv.text(fl.p(330, 0)[0], fl.p(0, 0)[1] + 14, "worst shot: lands at the edge", "sans", 24, SPARK)
    cv.text(M, 785, f"The farthest landing is half the field away: {old.H/2:.1f} px.", "serif", 34, INK)
    cv.k = 4; card(cv, 1100, 190, W - M, 520, True); cv.text(1140, 215, "HALF THE FIELD", "sans", 24, SPARK); cv.text(1140, 250, f"{old.H/2:.1f}", "serif", 110, SEND)
    cv.text(1140, 390, f"less the paddle's own half-length, {old.h/2:.0f}", "serif", 32, INK_SOFT); cv.text(1140, 435, f"= must travel {must:.1f} px", "serif", 40, INK)
    chip(cv, old); return cv.im

def d_b05(stage):
    cv = G(stage); title(cv, "The line")
    shot6 = stage >= 3
    can = can6 if shot6 else 2.0 * old.T(0)
    bars(cv, M, 190, 900, can, must, maxv=300)
    cv.text(M, 400, "shot six: it cannot" if shot6 else "shot one: it can", "sans", 24, SPARK)
    cv.k = 1; cv.text(M, 470, "Can the paddle travel as far as it must?", "serif", 44, INK)
    cv.k = 2
    if stage == 2: cv.text(M, 540, "can travel \u2265 must travel: a perfect defense exists", "serif", 36, INK_SOFT)
    if stage >= 3: cv.text(M, 540, "can travel < must travel: there is none", "serif", 36, SEND)
    cv.k = 4; card(cv, 1100, 190, W - M, 560, True); cv.text(1140, 215, "PADDLE SPEED / BALL SIDEWAYS SPEED", "sans", 24, SPARK)
    cv.text(1140, 255, f"{R['line_full']:.2f}", "serif", 180, SEND); cv.text(1140, 470, "a little over a quarter", "serif", 40, INK)
    cv.k = 5; card(cv, M, 620, W - M, 930); cv.text(M + 40, 650, "THE FORM, FOR ANY FIELD", "sans", 24, INK_SOFT)
    cv.text(M + 40, 695, "the defender's reach in one flight   against   half the free height", "serif", 52, INK)
    cv.text(M + 40, 790, f"({old.H:.0f} \u2212 {old.h:.0f}) \u00f7 (2 \u00d7 {old.W:.0f})  =  {R['line_full']:.3f}", "sans", 36, INK)
    cv.text(M + 40, 855, "a brute-force search that tries every aim found 0.272", "sans", 26, INK_SOFT)
    chip(cv, old); return cv.im

def d_b06(stage):
    cv = G(stage); title(cv, "Turn the dial")
    cv.text(M, 150, "same rally, same rules, only the paddle's speed changes", "serif", 34, INK_SOFT)
    rows = [(1.0, "too slow", 0), (2.0, "middle", 5), (3.0, "fast", 13)]
    # shown dots per row: row1 -> stage>=1 shows 1; row2 stages 2..7 -> 1..6; row3 stages 8..21 -> 1..14
    shown = [1 if stage >= 1 else 0, 0 if stage < 2 else min(stage - 1, 6), 0 if stage < 8 else min(stage - 7, 14)]
    for i, (vp, name, brk) in enumerate(rows):
        y = 250 + i * 190; cv.text(M, y - 6, f"paddle speed {vp:.1f}", "sans", 28, INK); cv.text(M, y + 34, name, "sans", 24, INK_SOFT)
        for j in range(15):
            cx = 520 + j * 78
            if j < shown[i]:
                col = INK if j < brk else SPARK; cv.dot(cx, y + 20, 22, col)
                if j == brk: cv.text(cx, y + 56, f"shot {j+1}", "sans", 24, SPARK, "ma")
                else: cv.text(cx, y + 56, str(j + 1), "sans", 24, INK_SOFT, "ma")
            else:
                cv.dot(cx, y + 20, 22, "#EDEBE1"); cv.text(cx, y + 56, str(j + 1), "sans", 24, GHOST, "ma")
    if stage >= 22:
        cv.text(M, 850, "filled = defended    orange = the shot that gets past", "sans", 24, INK_SOFT)
        cv.text(M, 900, f"breaks on shot {R['bk_old'][1.0]+1}, shot {R['bk_old'][2.0]+1}, shot {R['bk_old'][3.0]+1}", "serif", 44, SEND)
    chip(cv, old); return cv.im

def d_b07(stage):
    cv = G(stage); title(cv, "The clock")
    x0, y0, w, h = 190, 240, 880, 600; cv.rect(x0, y0, x0 + w, y0 + h, fill=CARD, outline=BORDER, width=2)
    vmax = 480.0; xs = lambda s_: x0 + (s_ - 0.5) * w / 15.5; ys = lambda v: y0 + h - v / vmax * h
    for v in (0, 100, 200, 300, 400): cv.dash((x0, ys(v)), (x0 + w, ys(v)), fill="#EDEBE1", width=1); cv.text(x0 - 14, ys(v), str(v), "sans", 24, INK_SOFT, "rm")
    for s_ in range(1, 16): cv.text(xs(s_), y0 + h + 14, str(s_), "sans", 24, INK_SOFT, "ma")
    cv.text(x0 + w / 2, y0 + h + 52, "shot", "sans", 24, INK_SOFT, "ma"); cv.text(M, y0 - 38, "px the paddle can travel in one crossing", "sans", 24, INK_SOFT)
    cv.dash((x0, ys(must)), (x0 + w, ys(must)), fill=SEND, width=3); cv.text(x0 + w + 16, ys(must) - 14, f"must travel {must:.1f}", "sans", 24, SPARK)
    upto = 0 if stage < 2 else min(stage - 1, 15)       # stages 2..16 reveal shots 1..15
    for vp, col, lab in ((3.0, GHOST, "paddle speed 3.0"), (2.0, INK, "paddle speed 2.0")):
        pts = [(xs(s_), ys(vp * old.T(s_ - 1))) for s_ in range(1, 16)]
        if upto >= 2: cv.line(pts[:upto], col, 4)
        for p_ in pts[:upto]: cv.dot(*p_, 6, col)
        if upto >= 1: cv.text(pts[0][0] + 30, pts[0][1] - 48, lab, "sans", 24, col if col != GHOST else INK_SOFT)
        if stage >= 17:
            b = R['bk_old'][vp] + 1; cv.dot(*pts[b - 1], 12, SPARK); cv.text(pts[b - 1][0], pts[b - 1][1] + 26, f"shot {b}", "sans", 24, SPARK, "ma")
    tx = 1330
    cv.k = 1; cv.text(tx, 250, "The ball speeds up", "serif", 40, INK); cv.text(tx, 298, "on every shot.", "serif", 40, INK)
    cv.k = 2; cv.text(tx, 380, "So the crossing gets shorter,", "serif", 40, INK); cv.text(tx, 428, "and what the paddle can cover", "serif", 40, INK); cv.text(tx, 476, "in one crossing shrinks with it.", "serif", 40, INK)
    if stage >= 2:
        s_now = min(max(upto, 1), 15) if stage < 17 else 6
        bars(cv, tx, 730, 480, 2.0 * old.T(s_now - 1), must, maxv=300, tag=f"shot {s_now}, paddle speed 2.0", l1="CAN TRAVEL", l2="MUST TRAVEL")
    cv.k = 18; cv.text(tx, 560, "In my model,", "serif", 46, SEND); cv.text(tx, 614, "a rally has a clock inside it.", "serif", 46, SEND)
    chip(cv, old); return cv.im

def d_b08(stage):
    cv = G(stage); title(cv, "Predicted, then found")
    widths = [260, 470, 470, 420]; x = M; y = 230; cols = ["PADDLE SPEED", "ARITHMETIC SAYS", "SO THE BREAK IS SHOT", "THE SEARCH FOUND"]
    cx = x
    for c, wd in zip(cols, widths): cv.text(cx, y, c, "sans", 24, INK_SOFT); cx += wd
    cv.line([(x, y + 40), (x + sum(widths), y + 40)], BORDER, 2)
    data = [(2.0, 1), (3.0, 3)]
    for i, (vp, st0) in enumerate(data):
        yy = y + 62 + i * 110
        vals = [f"{vp:.1f}", f"{R['spd'][vp]:.2f} speed-ups", ORD[R['pred_old'][vp] + 1], ORD[R['bk_old'][vp] + 1]]
        for j, (v, wd) in enumerate(zip(vals, widths)):
            need = {0: st0, 1: st0, 2: st0, 3: (2 if i == 0 else 4)}[j]
            cv.k = need; cx = x + sum(widths[:j]); cv.text(cx, yy, v, "serif", 52, SEND if j >= 2 else INK)
    cv.k = 3; cv.text(M, 590, "The search tries every aim at every shot. The arithmetic is one line.", "serif", 40, INK)
    cv.text(M, 650, "They agree, so the line can be trusted for this model.", "serif", 40, INK)
    cv.text(M, 780, "ln(speed / (0.271 × 6)) / ln(1.05) speed-ups, rounded up to the next shot", "sans", 26, INK_SOFT)
    chip(cv, old); return cv.im

def d_b09(stage):
    cv = G(stage); title(cv, "The second dial")
    fl = Fld(cv, old, M, 190, 0.85); ya = old.H / 2; fl.paddle("R", ya); fl.paddle("L", old.H / 2)
    cv.k = 1; q = 0.25; half = q * old.W; lo, hi = max(0, ya - half), min(old.H, ya + half)
    for ly in (lo, hi): cv.line([fl.p(old.W - 14, ya), fl.p(14, ly)], SPARK, 4)
    for i in range(1, 6): cv.line([fl.p(old.W - 14, ya), fl.p(14, lo + i * (hi - lo) / 6)], "#E8C9BA", 2)
    cv.text(M, 680, "a hit steers the ball less:", "serif", 34, INK); cv.text(M, 722, "up and down speed at most a quarter of sideways speed", "serif", 34, INK)
    cv.k = 2; cv.text(1000, 190, "THE LINE DROPS", "sans", 24, INK_SOFT)
    cv.text(1000, 225, f"{R['line_full']:.3f}", "serif", 90, GHOST); cv.text(1280, 255, "→", "serif", 60, INK); cv.text(1360, 225, f"{R['line_narrow']:.3f}", "serif", 90, SEND)
    cv.text(M, 860, f"0.25 − {old.h:.0f} ÷ (2 × {old.W:.0f}) = {R['line_narrow']:.3f}", "sans", 26, INK_SOFT)
    base, sc = 1000, 40
    cv.k = 3; cv.text(1000, 345, "WHERE THE DEFENSE BREAKS, PADDLE SPEEDS 2.0 AND 3.0", "sans", 24, INK_SOFT)
    hl = 0 if stage < 5 else min(stage - 4, 19)          # stages 5..23 walk the count 1..19
    for s_ in range(1, 21): cv.rect(base + (s_ - 1) * sc, 395, base + s_ * sc - 4, 435, fill="#EDEBE1")
    for s_ in (1, 5, 10, 15, 20): cv.text(base + (s_ - 1) * sc + 18, 445, str(s_), "sans", 24, INK_SOFT, "ma")
    for vp in (2.0, 3.0): cv.rect(base + R['bk_old'][vp] * sc, 395, base + (R['bk_old'][vp] + 1) * sc - 4, 435, fill=GHOST)
    cv.rect(1000, 490, 1030, 516, fill=GHOST); cv.text(1044, 486, "full aim", "sans", 24, INK_SOFT)
    cv.rect(1200, 490, 1230, 516, fill=SEND); cv.text(1244, 486, "predicted: aim at most a quarter", "sans", 24, INK_SOFT)
    pred = [R['pred_narrow'][2.0] + 1, R['pred_narrow'][3.0] + 1]
    if stage >= 3: cv.rect(base + (pred[0] - 1) * sc, 395, base + pred[0] * sc - 4, 435, fill=SEND)
    if stage >= 4: cv.rect(base + (pred[1] - 1) * sc, 395, base + pred[1] * sc - 4, 435, fill=SEND)
    if hl:
        cv.rect(base + (hl - 1) * sc - 3, 389, base + hl * sc + 1, 441, outline=INK, width=4)
        cv.text(base + (hl - 1) * sc + 18, 350 + 0, "", "sans", 24, INK)
    cv.k = 24; card(cv, 1000, 560, W - M, 850, True); cv.text(1040, 585, "ARITHMETIC FIRST, THEN THE COUNT", "sans", 24, SPARK)
    rows = [("full aim", f"{ORD[R['bk_old'][2.0]+1]}, {ORD[R['bk_old'][3.0]+1]}", INK_SOFT), ("predicted", f"{ORD[R['pred_narrow'][2.0]+1]}, {ORD[R['pred_narrow'][3.0]+1]}", INK),
            ("found", f"{ORD[R['bk_narrow'][2.0]+1]}, {ORD[R['bk_narrow'][3.0]+1]}", SEND)]
    for i, (a, b, c) in enumerate(rows): cv.text(1040, 635 + i * 68, a, "serif", 40, INK_SOFT); cv.text(1300, 635 + i * 68, b, "serif", 44, c)
    chip(cv, old, "   aim limited to a quarter"); return cv.im

def d_b10(stage):
    cv = G(stage); title(cv, "A different field")
    sc = 0.5
    for i, (f, lab, ln) in enumerate([(old, "858 by 525, paddle 60", R['line_full']), (new, "1200 by 500, paddle 50", R['line_new'])]):
        cv.k = 0 if i == 0 else 1; x0 = M + i * 880; fl = Fld(cv, f, x0, 190, sc); fl.paddle("L", f.H / 2); fl.paddle("R", f.H / 2)
        for ly in (0, f.H): cv.line([fl.p(f.W - 14, f.H / 2), fl.p(14, ly)], SPARK, 3)
        cv.text(x0, 190 + 262 + 16, lab, "sans", 26, INK_SOFT)
        cv.k = 0 if i == 0 else 2; cv.text(x0, 190 + 262 + 52, f"line  {ln:.4g}", "serif", 52, SEND if i else INK)
    cv.k = 5; cv.text(M + 440 + 190, 360, "same form", "serifi", 44, SPARK)
    x = M; y = 640; widths = [360, 640, 520]
    cv.k = 3
    for j, c in enumerate(["PADDLE SPEED", "ARITHMETIC SAYS SHOT", "THE SEARCH FOUND"]): cv.text(x + sum(widths[:j]), y, c, "sans", 24, INK_SOFT)
    cv.line([(x, y + 40), (x + sum(widths), y + 40)], BORDER, 2)
    for i, vp in enumerate((1.5, 2.5, 4.0)):
        yy = y + 62 + i * 84
        cv.k = 3; cv.text(x, yy, f"{vp:.1f}", "serif", 52, INK); cv.text(x + widths[0], yy, ORD[R['pred_new'][vp] + 1], "serif", 52, SEND)
        cv.k = 4; cv.text(x + widths[0] + widths[1], yy, ORD[R['bk_new'][vp] + 1], "serif", 52, SEND)
    chip(cv, new if stage >= 1 else old); return cv.im

def d_b11(stage):
    cv = G(stage); title(cv, "Which rule?")
    xs = [M, 700, 1285]; w = 520
    texts = [("DIAL ONE", "how fast the paddle moves", [f"speed {vp:.1f}: shot {R['bk_old'][vp]+1}" for vp in (1.0, 2.0, 3.0)]),
             ("DIAL TWO", "how much a hit can steer", [f"full aim: shot {R['bk_old'][2.0]+1}, {R['bk_old'][3.0]+1}", f"narrow aim: shot {R['bk_narrow'][2.0]+1}, {R['bk_narrow'][3.0]+1}"]),
             ("REMOVE THE SPEED-UP", "the ball never gets faster", ["speed 2.0: no break", "speed 3.0: no break", "in 200 shots"])]
    for i, (a, b, ls) in enumerate(texts):
        cv.k = i + 1; card(cv, xs[i], 200, xs[i] + w, 640, i == 2); cv.text(xs[i] + 30, 225, a, "sans", 24, SPARK if i == 2 else INK_SOFT)
        cv.wrap(xs[i] + 30, 265, b, "serif", 40, INK, w - 60, 1.15)
        for j, l in enumerate(ls): cv.text(xs[i] + 30, 400 + j * 62, l, "serif", 38, SEND if i == 2 else INK)
    cv.k = 4; cv.text(M, 740, "A fast enough paddle, against a ball that never speeds up, held for two hundred shots.", "serif", 44, INK)
    cv.text(M, 805, "The speeding up is what makes the sentence true.", "serif", 44, SEND)
    chip(cv, old); return cv.im

def d_b12(stage):
    cv = G(stage); title(cv, "What this does not claim")
    cv.text(M, 190, "A model, not a machine. Left out on purpose:", "serif", 52, INK)
    for i, s in enumerate(["spin on the ball", "human reaction time", "the edges of the paddle", "numbers from any real machine"]):
        cv.k = i + 1; y = 300 + i * 120; card(cv, M, y, 1000, y + 90); cv.text(M + 36, y + 14, s, "serif", 48, INK)
    cv.k = 5; cv.text(M, 830, "It shows when a rule set can be defended perfectly.", "serif", 44, INK)
    cv.k = 6; cv.text(M, 890, "It does not say how any particular game was built.", "serif", 44, INK_SOFT)
    chip(cv, old); return cv.im

def d_b13(stage):
    cv = G(stage); title(cv, "Your turn")
    cf = sm.Field(W=1000, H=500, h=50)
    card(cv, M, 190, 1000, 500, True); cv.text(M + 40, 215, "THE LINE", "sans", 24, SPARK)
    cv.k = 2; cv.text(M + 40, 265, "(height − paddle) ÷ (2 × width)", "serif", 56, INK)
    cv.k = 1; cv.text(M + 40, 335, f"({cf.H:.0f} − {cf.h:.0f}) ÷ (2 × {cf.W:.0f})  =  " + ("?" if stage < 3 else f"{R['line_card']:.3f}"), "serif", 64, SEND)
    cv.text(M + 40, 440, "field 1000 wide, 500 tall, paddle 50 long", "sans", 24, INK_SOFT)
    for i, (r, verdict, on) in enumerate([(0.25, "a perfect defense at the serve", True), (0.20, "not a perfect defense", False)]):
        cv.k = 4; y = 540 + i * 180; card(cv, M, y, 1000, y + 156)
        cv.text(M + 40, y + 24, f"paddle at {r:.2f} of the ball's speed", "serif", 44, INK); cv.text(M + 40, y + 88, verdict, "serif", 44, SEND if on else INK_SOFT)
        cv.text(940, y + 24, ">" if r > R['line_card'] else "<", "serif", 80, SEND, "ra")
    cv.k = 5; cv.text(1100, 215, "ONE DIAL, ONLY ONE:", "sans", 24, INK_SOFT)
    cv.k = 6; cv.text(1100, 255, "where would you put it?", "serif", 64, INK)
    for i, s in enumerate(["how fast the paddle moves", "how much a hit can steer", "how fast the ball speeds up"]): cv.text(1130, 370 + i * 64, s, "serif", 40, INK_SOFT)
    return cv.im


DRAW = {f"B{n:02d}": globals()[f"d_b{n:02d}"] for n in range(14)}

# ------------------------------------------------------------------ cue -> stage timeline per beat: [(t, stage, fade_s)]
def timeline(bid):
    e = lambda n: ev(bid, n); T = []
    def add(t, st, f=FADE): T.append((t, st, f))
    if bid == "B00":
        for k in range(1, 6): add(e(f"counter_{k}"), k, 0.14)   # a digit swap: keep the double image brief
        add(e("counter_6_ball_goes_past"), 6, 0.14); add(e("gap_callout"), 7)
    elif bid == "B01": add(e("chip_no_perfect_defense"), 1); add(e("chip_game_to_eleven"), 2); add(e("question_line"), 3)
    elif bid == "B02":
        for n, s_ in (("paddle_arrows", 1), ("bounce_note", 2), ("steering_card", 3), ("name_chip", 4), ("constants_card_lit", 5)): add(e(n), s_)
    elif bid == "B03":
        for n, s_ in (("ball_launch_path", 1), ("defender_sees", 2), ("timer_bar", 3), ("bars_highlight", 4), ("can_bar_pulse", 5), ("must_bar_pulse", 6)): add(e(n), s_)
    elif bid == "B04":
        for n, s_ in (("fan_all_aims", 1), ("defender_waits_middle", 2), ("extremes_lit", 3), ("half_field_card", 4)): add(e(n), s_)
    elif bid == "B05":
        for n, s_ in (("compare", 1), ("exists", 2), ("none_exists", 3), ("ratio_0_27", 4), ("form_card", 5)): add(e(n), s_)
    elif bid == "B06":
        add(e("row1_break_1"), 1)
        for i, t in enumerate(ramp(e("row2_fill_to_6"), e("row3_fill_to_14") - 0.1, 6)): add(t, 2 + i, RAMP_FADE)
        for i, t in enumerate(ramp(e("row3_fill_to_14"), e("same_rules") - 0.1, 14)): add(t, 8 + i, RAMP_FADE)
        add(e("same_rules"), 22)
    elif bid == "B07":
        add(e("ball_speeds_up"), 1)
        for i, t in enumerate(ramp(e("curves_draw"), e("bars_sink") - 0.2, 15)): add(t, 2 + i, RAMP_FADE)
        add(e("bars_sink"), 17); add(e("in_my_model"), 18)
    elif bid == "B08":
        for n, s_ in (("row1_arithmetic", 1), ("row1_found", 2), ("row2_arith_and_found", 3), ("fourteenth_found", 4)): add(e(n), s_)
    elif bid == "B09":
        for n, s_ in (("wedge_narrows", 1), ("line_drops", 2), ("tick_tenth", 3), ("tick_nineteenth", 4)): add(e(n), s_)
        t0, t10, t19 = e("count_starts"), e("count_lands_tenth"), e("count_lands_nineteenth")
        for i, t in enumerate(ramp(t0, t10, 10)): add(t, 5 + i, RAMP_FADE)
        for i, t in enumerate(ramp(t10, t19, 9)): add(t, 15 + i, RAMP_FADE)
        add(t19 + 0.5, 24)
    elif bid == "B10":
        for n, s_ in (("size_chip", 1), ("line_0_1875", 2), ("predicted_col", 3), ("found_col", 4), ("same_form", 5)): add(e(n), s_)
    elif bid == "B11":
        for n, s_ in (("dial_one", 1), ("dial_two", 2), ("no_speedup_card", 3), ("speeding_up_line", 4)): add(e(n), s_)
    elif bid == "B12":
        for n, s_ in (("item_spin", 1), ("item_reaction", 2), ("item_paddle_edges", 3), ("item_real_machine", 4), ("shows_line", 5), ("does_not_line", 6)): add(e(n), s_)
    elif bid == "B13":
        for n, s_ in (("case_numbers", 1), ("line_formula", 2), ("answer_0_225", 3), ("verdict_cards", 4), ("last_question", 5), ("dial_question", 6)): add(e(n), s_)
    T.sort()
    assert all(T[i][0] < T[i + 1][0] for i in range(len(T) - 1)), (bid, "stage times not increasing", T)
    assert not T or T[-1][0] < CUES[bid]["duration_s"], (bid, "stage after end")
    return T


def ease(p): p = max(0.0, min(1.0, p)); return p * p * (3 - 2 * p)

def render_beat(bid, prev_final_stage=None):
    out = HERE / "_motion" / bid; shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    dur = CUES[bid]["duration_s"]; nf = round(dur * FPS); T = timeline(bid); draw = DRAW[bid]
    cache = {}
    def img(s_):
        if s_ not in cache:
            if len(cache) > 3: cache.pop(next(iter(cache)))
            cache[s_] = draw(s_)
        return cache[s_]
    prev_img = None
    if prev_final_stage is not None:
        pb, ps = prev_final_stage; prev_img = DRAW[pb](ps)
    states = [(0.0, 0, 0.0)] + T            # (t, stage, fade)
    files = []   # (path, nframes)
    last_key = None; static_count = 0
    def flush(key, path):
        pass
    seq = []   # per-frame key: ('s', stage) static or ('b', stage_a, stage_b, e) blend or ('d', e)
    for i in range(nf):
        t = i / FPS; j = max(k for k, (tt, _s, _f) in enumerate(states) if tt <= t + 1e-9)
        tj, sj, fj = states[j]
        if j > 0 and fj > 0 and t - tj < fj: key = ("b", states[j - 1][1], sj, round(ease((t - tj) / fj), 3))
        else: key = ("s", sj)
        if prev_img is not None and t < DISSOLVE: key = ("d", key, round(ease(t / DISSOLVE), 3))
        seq.append(key)
    # write images
    concat = []; n = 0; idx = 0
    def resolve(key):
        if key[0] == "s": return img(key[1])
        if key[0] == "b": return Image.blend(img(key[1]), img(key[2]), key[3])
        a = prev_img; b = resolve(key[1]); return Image.blend(a, b, key[2])
    i = 0
    while i < nf:
        key = seq[i]; run = 1
        if key[0] == "s":
            while i + run < nf and seq[i + run] == key: run += 1
        p = out / f"f{idx:05d}.jpg"; resolve(key).save(p, quality=95, subsampling=0)
        concat.append((p, run / FPS)); idx += 1; i += run
    lst = out / "list.txt"
    with open(lst, "w") as fh:
        for p, d in concat: fh.write(f"file '{p.name}'\nduration {d:.6f}\n")
        fh.write(f"file '{concat[-1][0].name}'\n")
    dst = HERE / "_beats"; dst.mkdir(exist_ok=True); mp4 = dst / f"{bid}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-r", str(FPS), "-vsync", "cfr",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "12", "-pix_fmt", "yuv420p", "-frames:v", str(nf), str(mp4)], check=True)
    for p, _ in concat: p.unlink()
    return bid, nf, len(concat), T[-1][1] if T else 0

FINAL = {}
def job(args):
    bid, prev = args
    return render_beat(bid, prev)

if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if a.startswith("B")] or sorted(DRAW)
    # last stage of each beat, for the dissolve from the previous beat
    final = {b: (b, (timeline(b)[-1][1] if timeline(b) else 0)) for b in DRAW}
    order = sorted(DRAW); jobs = [(b, final[order[order.index(b) - 1]] if order.index(b) > 0 else None) for b in ids]
    with Pool(4) as p:
        for bid, nf, nimg, last in p.imap_unordered(job, jobs): print(f"{bid}: {nf} frames, {nimg} images, last stage {last}", flush=True)
