#!/usr/bin/env python3
"""Week 28 long film (16:9): every beat is a pure function of time t, tied to the Whisper word clock (mp3/timings.json).

Voice: Kokoro am_onyx (make_audio.py VOICE); audio is NOT regenerated here. Reuses the still builder's drawing helpers
(build_long_stills) so the video's last frames equal the approved stills.

  /opt/homebrew/bin/python3.12 build_long_motion.py --frame B04 12.3 out.png     # one frame, for inspection
  /opt/homebrew/bin/python3.12 build_long_motion.py --render                      # all frames -> _frames/Bxx/
  /opt/homebrew/bin/python3.12 build_long_motion.py --encode                      # beats, master, previews
  /opt/homebrew/bin/python3.12 build_long_motion.py --all                         # render + encode

3840x2160, 30 fps, H.264 yuv420p; master audio loudnormed once to I=-14, TP=-1.5.
"""
import json
import math
import shutil
import subprocess
import sys
from multiprocessing import Pool
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import build_long_stills as bl                                     # noqa: E402
from c28_common import (BORDER, CARD, GHOST, INK, INK_SOFT, PAGE, S, SEND, SKY_BLUEGREY, SKY_GREY, SKY_YELLOW, SPARK,  # noqa: E402
                        SWATCH_BLACK, SWATCH_DARK_CYAN, SWATCH_DARK_GREY, SWATCH_LIGHT_YELLOW, hex2rgb, landscape, mix,
                        strip)

FPS = 30
TIM = json.loads((HERE / "mp3" / "timings.json").read_text())
FRAMES = HERE / "_frames"
BEATS = HERE / "_beats"
PREVIEW = HERE / "_preview"
MASTER = HERE / "color-never-hears-the-music.mp4"
ORDER = [f"B{i:02d}" for i in range(1, 14)]

M, W = bl.M, bl.W
SRC_X, SRC_BASE = bl.SRC_X, bl.SRC_BASE
STRIP_X, STRIP_Y, STRIP_SIZE = bl.STRIP_X, bl.STRIP_Y, bl.STRIP_SIZE
PANEL_Y0, PANEL_Y1, CAPTION_Y = bl.PANEL_Y0, bl.PANEL_Y1, bl.CAPTION_Y
BLANK = bl.BLANK_SKY
HS, SW = bl.HAPPY_STRONG, bl.SAD_WEAK
CAP = bl.CAP


# ----------------------------------------------------------------------------- time helpers

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ramp(t, t0, d=0.35):
    return ease((t - t0) / d)


def band(t, t0, t1, d=0.35):
    return ramp(t, t0, d) * (1 - ramp(t, t1, d))


def lerp(a, b, p):
    return a + (b - a) * p


def lerp2(a, b, p):
    return (lerp(a[0], b[0], p), lerp(a[1], b[1], p))


def seg(t, a, b):
    """seconds of [a, b] elapsed at time t"""
    return max(0.0, min(t, b) - a)


class A:
    """with A(cv, alpha): draw a group at that alpha (cv.alpha is restored)."""
    def __init__(self, cv, a):
        self.cv, self.a = cv, a

    def __enter__(self):
        self.old = self.cv.alpha
        self.cv.alpha = self.old * self.a
        return self.a > 0.004

    def __exit__(self, *x):
        self.cv.alpha = self.old


def headline(cv, items):
    for s, a in items:
        with A(cv, a):
            bl.headline(cv, s)


def src(cv, s, a=1.0):
    with A(cv, a):
        bl.source(cv, s)


def play(cv, x, y, a):
    with A(cv, a):
        bl.play_icon(cv, x, y, True)


# ----------------------------------------------------------------------------- the beats

def b01(cv, t):
    cA, cB, cE = 16.557, 24.557, 32.557
    hold = ramp(t, cE, 0.4)
    headline(cv, [("Which sky goes with which?", 1)])
    phA = 0.10 + 0.004 * t + 0.10 * seg(t, cA, cB)
    phB = 0.60 + 0.004 * t + 0.03 * seg(t, cB, cE)
    landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, mix(SKY_GREY, SKY_BLUEGREY, hold), phA)
    landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, mix(SKY_GREY, SKY_YELLOW, hold), phB)
    capA, capB = ramp(t, 3.3) * (1 - hold), ramp(t, 5.0) * (1 - hold)
    with A(cv, capA):
        bl.panel_caption(cv, M, CAPTION_Y, "A", "quick, bright")
    with A(cv, capB):
        bl.panel_caption(cv, 980, CAPTION_Y, "B", "slow, low")
    with A(cv, hold):
        cv.text(M + 8, CAPTION_Y, "1", "serifm", 52, fill=INK, anchor="ls")
        cv.text(980 + 8, CAPTION_Y, "2", "serifm", 52, fill=INK, anchor="ls")
    pa, pb = band(t, cA, cB, 0.1), band(t, cB, cE, 0.1)
    play(cv, 560, CAPTION_Y - 30, pa)
    play(cv, 1425, CAPTION_Y - 30, pb)
    with A(cv, pa):
        cv.text(SRC_X + 100, 740, "Clip A is playing", "sans", 32, fill=INK_SOFT)
    with A(cv, pb):
        cv.text(SRC_X + 100, 740, "Clip B is playing", "sans", 32, fill=INK_SOFT)
    with A(cv, hold):
        bl.chip(cv, 1120, 700, 300, 72, "pick one", fill=INK, outline=INK, fg=PAGE, size=36)
    halo = band(t, 10.9, 15.8)
    with A(cv, halo):
        cv.rect(STRIP_X - 118, STRIP_Y - 54, STRIP_X + STRIP_SIZE + 140, STRIP_Y + STRIP_SIZE + 44, outline=SPARK, width=4, r=14)
    bl.small_strip(cv, music=(0, 0))
    src(cv, "Illustration: two synthesized tunes, two painted skies. Not data.")


def b02(cv, t):
    swap = ramp(t, 3.9, 0.9)
    head2 = ramp(t, 11.5)
    headline(cv, [("Which sky goes with which?", 1 - head2), ("What are we actually matching?", head2)])
    ph = 0.10 + 0.01 * t
    landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, mix(SKY_BLUEGREY, SKY_YELLOW, swap), ph)
    landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, mix(SKY_YELLOW, SKY_BLUEGREY, swap), ph + 0.5)
    lab = 1 - ramp(t, 3.9, 0.5)
    with A(cv, lab):
        cv.text(M + 8, CAPTION_Y, "1", "serifm", 52, fill=INK, anchor="ls")
        cv.text(980 + 8, CAPTION_Y, "2", "serifm", 52, fill=INK, anchor="ls")
    with A(cv, ramp(t, 4.4)):
        bl.panel_caption(cv, M, CAPTION_Y, "A", "quick, bright")
        bl.panel_caption(cv, 980, CAPTION_Y, "B", "slow, low")
    with A(cv, 1 - ramp(t, 3.0, 0.3)):
        bl.chip(cv, 1120, 700, 300, 72, "pick one", fill=INK, outline=INK, fg=PAGE, size=36)
    with A(cv, ramp(t, 12.0)):
        cv.rect(STRIP_X - 118, STRIP_Y - 54, STRIP_X + STRIP_SIZE + 140, STRIP_Y + STRIP_SIZE + 44, outline=SPARK, width=4, r=14)
    bl.small_strip(cv, music=(0, 0))
    with A(cv, ramp(t, 5.6)):
        cv.text(SRC_X + 100, 740, "Most listeners put yellow on the quick one", "serifi", 44, fill=INK_SOFT)
    with A(cv, ramp(t, 12.0)):
        cv.text(SRC_X + 100, 810, "two scales: happy to sad,  strong to weak", "sans", 32, fill=INK_SOFT)


def _array(cv, rings_best, rings_worst, a_arr):
    hues, levels, arr, extras = bl.hue_array()
    ax, ay, cw, chh, gap = 1040, 250, 86, 62, 8
    best = {("yellow", "S"), ("yellow", "L"), ("orange", "S"), ("orange", "L"), ("chartreuse", "L")}
    worst = {("blue", "D"), ("purple", "D"), ("cyan", "D"), ("purple", "M"), ("blue", "M")}
    with A(cv, a_arr):
        for hi, (hn, _) in enumerate(hues):
            for li, (ln, _, _) in enumerate(levels):
                x, y = ax + hi * (cw + gap), ay + li * (chh + gap)
                cv.rect(x, y, x + cw, y + chh, fill=arr[(hn, ln)], outline=BORDER, width=1, r=4)
        for ei, ec in enumerate(extras):
            x, y = ax + ei * (cw + gap), ay + 4 * (chh + gap)
            cv.rect(x, y, x + cw, y + chh, fill=ec, outline=BORDER, width=1, r=4)
        cv.text(ax, ay - 20, "37 colors", "serifm", 40, fill=INK, anchor="ls")
    for key, ring, col, label, lx in [(best, rings_best, "#2E8B57", "five fit best", ax), (worst, rings_worst, "#C0392B", "five fit worst", ax + 260)]:
        with A(cv, ring):
            for hi, (hn, _) in enumerate(hues):
                for li, (ln, _, _) in enumerate(levels):
                    if (hn, ln) in key:
                        x, y = ax + hi * (cw + gap), ay + li * (chh + gap)
                        cv.rect(x - 5, y - 5, x + cw + 5, y + chh + 5, outline=col, width=5, r=8)
            cv.text(lx, ay + 5 * (chh + gap) + 42, label, "sansm", CAP, fill=col)


def b03(cv, t):
    pb = ramp(t, 19.4, 0.5)
    pa = 1 - pb
    # ---- a: the design
    with A(cv, pa):
        bl.headline(cv, "A real test: 18 pieces, 97 listeners")
        with A(cv, ramp(t, 0.2)):
            cv.text(M, 166, "2013 · orchestral music, 50 s each", "sans", CAP, fill=INK_SOFT)
        with A(cv, ramp(t, 2.8)):
            bl.grid_3x2(cv, M - 20, 260)
        with A(cv, ramp(t, 4.6)):
            cv.text(M + 90, 560, "B Bach · M Mozart · Br Brahms: 18 pieces", "sans", CAP, fill=INK_SOFT)
        x0g = M - 20 + 110
        for ci, t0 in enumerate([8.0, 8.6, 9.1]):          # SLOW, MEDIUM, FAST as they are said
            with A(cv, band(t, t0, t0 + 0.9, 0.2)):
                cv.rect(x0g + ci * 218 - 4, 256, x0g + ci * 218 + 214, 520, outline=SPARK, width=4, r=10)
        for ri, t0 in enumerate([9.7, 10.2]):               # MAJOR, MINOR
            with A(cv, band(t, t0, t0 + 0.8, 0.2)):
                cv.rect(x0g - 4, 256 + ri * 126, x0g + 3 * 218 - 4, 256 + ri * 126 + 122, outline=SPARK, width=4, r=10)
        for k, (lab, t0) in enumerate([("US · 48 listeners", 12.1), ("Mexico · 49 listeners", 12.9)]):
            with A(cv, ramp(t, t0)):
                bl.chip(cv, 520, 608 + k * 68, 330, 56, lab, size=CAP)
        _array(cv, ramp(t, 16.2), ramp(t, 18.5), ramp(t, 14.3))
        with A(cv, ramp(t, 16.2)):
            cv.text(1040, 250 + 5 * 70 + 86, "(ringed for one tune: an illustration of the design)", "sans", CAP, fill=INK_SOFT)
        src(cv, "Palmer, Schloss, Xu & Prado-León, PNAS 110(22), 2013. UC Berkeley and Univ. of Guadalajara. 48 US + 49 Mexican listeners.")
    # ---- b: the finding (direction only)
    with A(cv, pb):
        bl.headline(cv, "Same pattern in both countries")
        for k, (x, title, sub, base, t0) in enumerate([
                (M, "FAST + MAJOR", "lighter, more saturated, yellower", SKY_YELLOW, 20.3),
                (1000, "SLOW + MINOR", "darker, greyer, bluer", SKY_BLUEGREY, 24.7)]):
            with A(cv, ramp(t, t0)):
                cv.rect(x, 170, x + 800, 600, fill=CARD, outline=BORDER, width=2, r=14)
                cv.text(x + 30, 232, title, "serifm", 44, fill=INK, anchor="ls")
                cv.text(x + 30, 282, sub, "sans", 32, fill=INK_SOFT, anchor="ls")
                shades = ([mix(base, "#FFFFFF", 0.55), mix(base, "#FFFFFF", 0.25), base, mix(base, "#8B6914", 0.25)] if k == 0
                          else [mix(base, "#FFFFFF", 0.15), base, mix(base, "#2A3441", 0.35), mix(base, "#14181F", 0.55)])
                for si, c in enumerate(shades):
                    cv.rect(x + 30 + si * 185, 320, x + 30 + si * 185 + 165, 500, fill=c, outline=BORDER, width=2, r=8)
                cv.text(x + 30, 560, "illustration of the direction of the finding", "sans", CAP, fill=INK_SOFT, anchor="ls")
        with A(cv, ramp(t, 19.9)):
            cv.text(SRC_X + 100, 740, "United States and Mexico", "serifi", 44, fill=INK_SOFT)
        src(cv, "Palmer, Schloss, Xu & Prado-León, PNAS 110(22), 2013. The paper's own figures are not reproduced.")
    bl.small_strip(cv, music=(0, 0))


def b04(cv, t):
    bl.headline(cv, "They match through feeling")
    nx = 270
    sx, sy, ss = 600, 200, 440
    mpos, cpos = (0.30, 0.34), (0.30, 0.34)
    # the strip is present from frame one, dots arrive on the words
    dm, dc = ramp(t, 6.6), ramp(t, 7.2)
    strip(cv, sx, sy, ss, music=None, color=None, label_px=CAP)
    px, py = (sx + ss / 2 + mpos[0] * (ss / 2 - ss * 0.12), sy + ss / 2 - mpos[1] * (ss / 2 - ss * 0.12))
    with A(cv, dc):
        cv.ellipse(px, py, ss * 0.052, fill=SPARK, outline=INK, width=2)
    with A(cv, dm):
        cv.ellipse(px, py, ss * 0.052, fill=INK)
    with A(cv, ramp(t, 2.7)):
        cv.ellipse(nx, 300, 34, fill=INK)
        cv.text(nx, 250, "MUSIC", "sansm", 30, fill=INK, anchor="ms")
    with A(cv, ramp(t, 3.4)):
        cv.ellipse(nx, 560, 34, fill=SPARK, outline=INK, width=3)
        cv.text(nx, 630, "COLOR", "sansm", 30, fill=INK, anchor="ms")
    if dm > 0.5:
        with A(cv, dm):
            bl.arrow(cv, nx + 40, 300, lerp(nx + 40, px - 22, dm), lerp(300, py - 10, dm), fill=INK, width=4)
    if dc > 0.5:
        with A(cv, dc):
            bl.arrow(cv, nx + 40, 560, lerp(nx + 40, px - 22, dc), lerp(560, py + 12, dc), fill=SPARK, width=4)
            cv.ellipse(px, py, ss * 0.052 + 14, outline=SPARK, width=6)
    dl = ramp(t, 16.3)
    with A(cv, dl):
        bl.dashed(cv, nx, 350, nx, 508, fill=GHOST, width=4)
    with A(cv, ramp(t, 16.9)):
        cv.line([(nx - 28, 404), (nx + 28, 454)], fill="#C0392B", width=6)
        cv.line([(nx - 28, 454), (nx + 28, 404)], fill="#C0392B", width=6)
    with A(cv, ramp(t, 18.6)):
        cv.text(nx, 720, "through feeling", "serifi", 38, fill=INK_SOFT, anchor="ms")
    rx = 1230
    with A(cv, ramp(t, 8.8)):
        cv.text(rx, 215, "rated on the same feelings (US)", "sansm", CAP, fill=INK_SOFT, anchor="ls")
    rows = [("happy / sad", ".97", 9.2), ("lively / dreary", ".99", 14.0), ("strong / weak", ".96", 10.9), ("angry / calm", ".89", 14.0)]
    for i, (lab, val, t0) in enumerate(rows):
        y = 290 + i * 90
        cv.line([(rx, y + 58), (rx + 575, y + 58)], fill=BORDER, width=2)
        with A(cv, ramp(t, t0)):
            cv.text(rx, y + 38, lab, "sans", 32, fill=INK, anchor="ls")
            cv.text(rx + 575, y + 44, val, "serifm", 60, fill=SPARK, anchor="rs")
    with A(cv, ramp(t, 19.4)):
        bl.chip(cv, rx, 680, 575, 64, "correlation, not proof of mechanism", fill="#FBF0EA", outline=SPARK, size=CAP, fg=SEND)
    src(cv, "Emotion ratings of the 18 pieces vs. of the colors picked for them, US participants (Palmer et al. 2013). Mexico: .97, .96, .96, .93.")


def b05(cv, t):
    bl.headline(cv, "The paper's own example")
    to_b = ramp(t, 9.3, 0.5)
    sky = mix(mix(SKY_GREY, SKY_YELLOW, ramp(t, 7.0, 0.8)), SKY_BLUEGREY, ramp(t, 12.2, 0.8))
    landscape(cv, 880, 150, 1805, 540, sky, 0.1 + 0.012 * t)
    p1 = ramp(t, 4.0, 0.9)
    p2 = ramp(t, 11.7, 0.9)
    pos = lerp2(lerp2((0, 0), HS, p1), SW, p2)
    ps = strip(cv, 170, 190, 420, music=pos, color=pos, label_px=CAP)
    cv.ellipse(ps["music"][0], ps["music"][1], 420 * 0.052 + 14, outline=SPARK, width=6)
    with A(cv, ramp(t, 2.3) * (1 - to_b)):
        cv.text(880, 596, "Bach · fast dance in F major", "serifm", 44, fill=INK, anchor="ls")
    with A(cv, ramp(t, 4.0) * (1 - to_b)):
        cv.text(880, 642, "rated: happy, strong", "sans", 32, fill=INK_SOFT, anchor="ls")
    with A(cv, ramp(t, 9.3)):
        cv.text(880, 596, "Brahms · slow Adagio in C minor", "serifm", 44, fill=INK, anchor="ls")
    with A(cv, ramp(t, 11.7)):
        cv.text(880, 642, "rated: sad, weak", "sans", 32, fill=INK_SOFT, anchor="ls")
    itemsA = [(SKY_YELLOW, ""), (SWATCH_LIGHT_YELLOW, ""), ("#B8C4D6", ""), ("#8A5A9B", ""), (SWATCH_DARK_GREY, "")]
    itemsB = [(SKY_YELLOW, ""), (SWATCH_BLACK, ""), (SWATCH_DARK_GREY, ""), (SWATCH_DARK_CYAN, ""), (SWATCH_LIGHT_YELLOW, "")]
    with A(cv, ramp(t, 5.1) * (1 - to_b)):
        bl.swatch_row(cv, 880, 690, itemsA, lit={0, 1} if t > 7.0 else set())
    with A(cv, ramp(t, 9.5)):
        bl.swatch_row(cv, 880, 690, itemsB, lit={1, 2, 3} if t > 12.5 else set())
    with A(cv, band(t, 7.0, 9.3)):
        cv.text(880, 830, "saturated yellow  ·  light yellow", "sans", CAP, fill=INK_SOFT, anchor="ls")
    with A(cv, ramp(t, 12.5)):
        cv.text(880, 810, "black  ·  dark grey  ·  dark cyan", "sans", CAP, fill=INK_SOFT, anchor="ls")
    with A(cv, ramp(t, 14.2)):
        cv.rect(SRC_X, 840, 1805, 930, fill=CARD, outline=BORDER, width=2, r=12)
    for i, (s, t0) in enumerate([("1  rate the sound", 14.9), ("2  rate the color", 15.9), ("3  do they agree?", 17.0)]):
        with A(cv, ramp(t, t0)):
            cv.text(SRC_X + 40 + i * 400, 898, s, "serifm", 38, fill=INK, anchor="ls")
    src(cv, "The paper's own example of its idea (Palmer et al. 2013).")


def b06(cv, t):
    bl.headline(cv, "Sorting comes before the words")
    ty, x_start, x_end = 500, 200, 1720
    cv.line([(x_start, ty), (x_end, ty)], fill=INK, width=4)
    pos = {0: x_start, 6: x_start + (x_end - x_start) * 6 / 24, 18: x_start + (x_end - x_start) * 18 / 24}
    cols = ["#D8573C", "#F2C230", "#3E8E5B", "#3B6FB6", "#8A5A9B", "#E58A3C"]
    for m, lab, t0 in [(0, "birth", 0.0), (6, "6 mo", 4.6), (18, "18 mo", 7.0)]:
        with A(cv, ramp(t, t0) if t0 else 1.0):
            x = pos[m]
            cv.line([(x, ty - 18), (x, ty + 18)], fill=INK, width=4)
            cv.text(x, ty + 62, lab, "serifm", 40, fill=INK, anchor="ms")
    for m, cx, t0 in [(0, pos[0] + 150, 0.0), (6, pos[6], 4.6), (18, pos[18], 7.0)]:
        cy, r = 300, 108
        with A(cv, ramp(t, t0) if t0 else 1.0):
            if m == 0:
                cv.ellipse(cx, cy, r, fill="#C9C8C2", outline=BORDER, width=2)
                cv.text(cx, cy + 12, "grey", "serifi", 40, fill=INK_SOFT, anchor="ms")
            else:
                for k, c in enumerate(cols):
                    bl.pie(cv, cx, cy, r, k * 60 - 90, k * 60 - 30, c)
                cv.ellipse(cx, cy, r, outline=INK, width=3)
                cv.ellipse(cx, cy, 32, fill=PAGE, outline=INK, width=3)
            if m == 6:
                cv.text(cx, cy - r - 24, "category", "serifm", 40, fill=SEND, anchor="ms")
            if m == 18:
                cv.text(cx, cy - r - 24, "name", "serifm", 40, fill=SEND, anchor="ms")
    for k, (w, c) in enumerate([("red", "#D8573C"), ("blue", "#3B6FB6"), ("yellow", "#B58B00")]):
        with A(cv, ramp(t, 7.4 + 0.3 * k)):
            bl.chip(cv, pos[18] + 108 + 30, 220 + k * 70, 160, 54, w, size=30, fg=c)
    with A(cv, ramp(t, 8.3)):
        cv.text(SRC_X + 100, 760, "the sorting arrives before the words", "serifi", 44, fill=INK_SOFT)
    bl.small_strip(cv, music=(0, 0))
    src(cv, "From an essay we read.")


def b07(cv, t):
    h2 = ramp(t, 22.4)
    headline(cv, [("How far does the match travel?", 1 - h2), ("Strong, not a law", h2)])
    items = [(M, "WHITE", "#FFFFFF", ["purity, in much of the West", "mourning, in many Eastern cultures"], 17.2, [18.9, 20.5]),
             (500, "GREEN", "#3E8E5B", ["growth, in much of the West", "infidelity, in some East Asian contexts"], 21.4, [21.7, 21.9])]
    for x, name, col, caps, t0, tc in items:
        with A(cv, ramp(t, t0)):
            cv.text(x, 205, name, "sansm", 30, fill=INK_SOFT, anchor="ls")
            cv.rect(x, 225, x + 210, 380, fill=col, outline=BORDER, width=3, r=10)
        for ci, c in enumerate(caps):
            with A(cv, ramp(t, tc[ci])):
                for li, ln in enumerate(bl.wrap(cv, c, "sans", CAP, 350)):
                    cv.text(x, 436 + ci * 120 + li * 34, ln, "sans", CAP, fill=INK, anchor="ls")
                cv.line([(x, 404 + ci * 120), (x + 350, 404 + ci * 120)], fill=BORDER, width=2)
    tx = 1000
    with A(cv, ramp(t, 1.4)):
        cv.rect(tx, 190, 1805, 700, fill=CARD, outline=BORDER, width=2, r=14)
        cv.text(tx + 30, 245, "US ↔ Mexico (r)", "serifm", 44, fill=INK, anchor="ls")
    for i, (lab, v, t0) in enumerate([("red–green", ".88", 6.4), ("yellow–blue", ".96", 7.0), ("light–dark", ".97", 7.3), ("saturation", ".95", 7.9)]):
        y = 290 + i * 70
        with A(cv, ramp(t, t0)):
            cv.text(tx + 30, y + 44, lab, "sans", 32, fill=INK, anchor="ls")
            cv.text(tx + 765, y + 48, v, "serifm", 50, fill=INK, anchor="rs")
            cv.line([(tx + 30, y + 62), (tx + 765, y + 62)], fill=BORDER, width=2)
    with A(cv, ramp(t, 14.1)):
        cv.text(tx + 30, 640, "nonwestern scales: untested", "serifm", 40, fill=SEND, anchor="ls")
    bl.small_strip(cv, music=(0, 0))
    src(cv, "Palmer et al. 2013 (cross-culture correlations; 'unclear' for nonwestern music). Symbolism: from an essay we read.")


def b08(cv, t):
    bl.headline(cv, "Same length. Very different pulse.")
    x0, x1, T = 300, 1760, 40.0
    calm = [10, 9, 12, 9]
    busy = [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3]
    scale = (x1 - x0) / T
    for row, (durs, lab, base, y, t0) in enumerate([(calm, "calm", SKY_BLUEGREY, 180, 5.3), (busy, "busy", SKY_YELLOW, 390, 6.4)]):
        cv.text(M, y + 62, lab, "serifm", 44, fill=INK, anchor="ls")
        x, acc = x0, 0.0
        for i, d in enumerate(durs):
            w = d * scale
            c = mix(base, "#FFFFFF", 0.28 if i % 2 else 0.0)
            with A(cv, ramp(t, t0 + 0.12 * i, 0.3)):
                cv.rect(x, y, x + w - 4, y + 110, fill=c, outline=None, r=6)
                cv.text(x + (w - 4) / 2, y + 70, f"{d} s", "sansm", CAP, fill=PAGE if row == 0 else INK, anchor="ms")
                acc += d
                xx = x0 + acc * scale - 2
                cv.line([(xx, y + 122), (xx, y + 146)], fill=INK_SOFT, width=2)
            x += w
        with A(cv, ramp(t, 8.5 if row == 0 else 10.8)):
            cv.text(x0, y + 190, "long scenes, 7–12 s each" if row == 0 else "short scenes, 1–3 s each", "sans", CAP, fill=INK_SOFT, anchor="ls")
    ph = lerp(x0, x1, clamp((t - 12.3) / (19.5 - 12.3)))
    with A(cv, ramp(t, 12.3)):
        cv.line([(ph, 160), (ph, 540)], fill=SPARK, width=5)
    with A(cv, ramp(t, 16.1)):
        cv.text(SRC_X + 100, 760, "calm: cool colors   ·   busy: warm colors", "serifi", 40, fill=INK_SOFT)
    bl.small_strip(cv, music=(0, 0))
    src(cv, "A rule of thumb from an essay we read: calm scenes 7–12 s, busy scenes 1–3 s.")


def b09(cv, t):
    bl.headline(cv, "60 four-year-olds, 9 minutes")
    cols = [("FAST CARTOON", 420, [0.46, 0.52, 0.40, 0.55], INK, 6.7), ("SLOWER CARTOON", 960, [0.80, 0.84, 0.76, 0.82], INK_SOFT, 8.0),
            ("DRAW", 1500, [0.82, 0.78, 0.80, 0.85], INK_SOFT, 8.7)]
    gr = ramp(t, 12.2, 0.7)
    for name, cx, bars, col, t0 in cols:
        with A(cv, ramp(t, t0)):
            cv.text(cx, 186, name, "sansm", 30, fill=col, anchor="ms")
        for i in range(20):
            r, c = divmod(i, 5)
            with A(cv, ramp(t, t0 + 0.04 * i, 0.25)):
                cv.ellipse(cx - 96 + c * 48, 224 + r * 34, 12, fill=col)
        with A(cv, ramp(t, 12.0)):
            cv.line([(cx - 120, 540), (cx + 120, 540)], fill=INK_SOFT, width=2)
            cv.text(cx, 578, "4 tasks, right afterwards", "sans", CAP, fill=INK_SOFT, anchor="ms")
        for j, v in enumerate(bars):
            bx, h = cx - 108 + j * 60, v * 190 * gr
            if h > 1:
                cv.rect(bx, 540 - h, bx + 44, 540, fill=SPARK if name == "FAST CARTOON" else "#C9C6B8", outline=None, r=4)
    with A(cv, ramp(t, 14.9)):
        bl.chip(cv, 520, 680, 880, 64, "pacing, not color  ·  immediate  ·  four-year-olds", fill="#FBF0EA", outline=SPARK, size=30, fg=SEND)
    with A(cv, ramp(t, 6.7)):
        cv.text(SRC_X + 100, 810, "each dot is one child (illustrative layout)", "sans", CAP, fill=INK_SOFT)
    bl.small_strip(cv, music=(0, 0))
    src(cv, "Lillard & Peterson, Pediatrics 128(4), 2011. Bar heights are illustrative; the paper reports significant differences, not these values.")


HOLD10 = 22.102 + 0.45


def b10(cv, t):
    bl.headline(cv, "Where does fast + minor land?")
    sx, sy, ss = 240, 210, 380
    strip(cv, sx, sy, ss, music=None, color=None, label_px=CAP)
    cx, cy = sx + ss / 2, sy + ss / 2
    p1, p2 = ramp(t, 3.1, 0.7), ramp(t, 4.6, 0.7)
    if p1 > 0.02:
        with A(cv, min(1.0, p1 * 2)):
            bl.arrow(cv, cx, cy, lerp(cx, cx + 105, p1), lerp(cy, cy - 125, p1), fill=SPARK, width=6, head=24)
    if p2 > 0.02:
        with A(cv, min(1.0, p2 * 2)):
            bl.arrow(cv, cx, cy, lerp(cx, cx - 135, p2), lerp(cy, cy + 5, p2), fill=INK, width=6, head=24)
    with A(cv, ramp(t, 3.8)):
        cv.text(cx + 40, cy - 148, "FAST → strong, lively", "sansm", CAP, fill=SEND, anchor="ms")
    with A(cv, ramp(t, 4.8)):
        cv.text(sx + 18, cy + 55, "MINOR → sad", "sansm", CAP, fill=INK, anchor="ls")
    with A(cv, ramp(t, 5.8)):
        bl.grid_3x2(cv, 790, 250, cw=190, ch=118, highlight=None, grey_others=False, tint=False)
    hl = ramp(t, 7.5)
    with A(cv, hl):
        bl.grid_3x2(cv, 790, 250, cw=190, ch=118, highlight=("FAST", "MINOR"), grey_others=True, tint=False)
    with A(cv, ramp(t, 8.0)):
        cv.text(790, 570, "FAST + MINOR is in the data", "serifm", 38, fill=INK, anchor="ls")
    with A(cv, band(t, 11.4, 14.8) * 0.9):
        cv.ellipse(cx, cy, 30 + 8 * math.sin(t * 5), outline=SPARK, width=5)
    with A(cv, ramp(t, 14.8)):
        cv.text(790, 630, "lighter or darker than slow minor's?", "sans", 30, fill=INK, anchor="ls")
    with A(cv, ramp(t, 15.5)):
        bl.chip(cv, 790, 648, 220, 56, "LIGHTER")
        bl.chip(cv, 1030, 648, 220, 56, "DARKER")
    with A(cv, ramp(t, 17.2)):
        cv.text(790, 758, "more or less saturated than fast major's?", "sans", 30, fill=INK, anchor="ls")
    with A(cv, ramp(t, 17.9)):
        bl.chip(cv, 790, 776, 220, 56, "MORE")
        bl.chip(cv, 1030, 776, 220, 56, "LESS")
    # countdown ring: appears with 'Pause here', counts down through the 6-s hold
    rx, ry = 1665, 335
    with A(cv, ramp(t, 19.7)):
        bl.arc(cv, rx, ry, 80, 0, 360, fill=BORDER, width=12)
        rem = clamp(HOLD10 + 6.0 - t, 0.0, 6.0)
        frac = rem / 6.0 if t > HOLD10 else 1.0
        digit = 6 if t <= HOLD10 else max(1, min(6, math.ceil(rem)))
        if frac > 0.003:
            bl.arc(cv, rx, ry, 80, -90, -90 + 360 * frac, fill=SPARK, width=12)
        cv.text(rx, ry + 22, str(digit), "serifm", 72, fill=INK, anchor="ms")
        cv.text(rx, ry + 120, "pause,", "sans", CAP, fill=INK_SOFT, anchor="ms")
        cv.text(rx, ry + 156, "write both down", "sans", CAP, fill=INK_SOFT, anchor="ms")
    # the four-step card fades in 2 s into the hold, to the right of the answer slots (slots stay visible)
    with A(cv, ramp(t, HOLD10 + 2.0, 0.5)):
        cv.rect(1370, 520, 1805, 930, fill=CARD, outline=BORDER, width=2, r=14)
        steps = ["1  place tempo's push", "2  place mode's push", "3  predict: between,", "     or closer to one pole", "4  check against the data"]
        for i, s in enumerate(steps):
            cv.text(1394, 578 + i * 70, s, "serifm", 34, fill=INK, anchor="ls")
    src(cv, "Design: Palmer et al. 2013 crossed tempo × mode (slow/medium/fast × major/minor).")


def b11(cv, t):
    bl.headline(cv, "Fast minor landed between")
    axes = [("saturation", "unsaturated", "saturated", -38, 20, 45), ("light–dark", "dark", "light", -40, 25, 45),
            ("yellow–blue", "blue", "yellow", -40, 5, 20)]
    ax0, ax1 = 330, 1230

    def X(v):
        return ax0 + (v + 80) / 160 * (ax1 - ax0)
    for i, (name, lo, hi, sm, fm, fM) in enumerate(axes):
        y = 220 + i * 150
        with A(cv, ramp(t, 1.0 + 0.2 * i)):
            cv.text(M, y + 8, name, "sansm", 30, fill=INK, anchor="ls")
            cv.line([(ax0, y), (ax1, y)], fill=INK_SOFT, width=3)
            cv.line([(X(0), y - 14), (X(0), y + 14)], fill=INK_SOFT, width=2)
            cv.text(ax0, y + 56, lo, "sans", CAP, fill=INK_SOFT, anchor="ls")
            cv.text(ax1, y + 56, hi, "sans", CAP, fill=INK_SOFT, anchor="rs")
        with A(cv, ramp(t, 8.1 + 0.15 * i)):
            cv.ellipse(X(sm), y, 20, fill=SKY_BLUEGREY, outline=INK, width=2)
        with A(cv, ramp(t, 9.4 + 0.15 * i)):
            cv.ellipse(X(fM), y, 20, fill=SKY_YELLOW, outline=INK, width=2)
        slide = ramp(t, 5.0 + 0.2 * i, 0.7)
        with A(cv, min(1.0, slide * 2)):
            cv.ellipse(lerp(X(0), X(fm), slide), y, 20, fill=SPARK, outline=INK, width=3)
    for k, (col, lab, t0) in enumerate([(SKY_BLUEGREY, "slow minor", 8.1), (SPARK, "fast minor", 5.0), (SKY_YELLOW, "fast major", 9.4)]):
        with A(cv, ramp(t, t0)):
            cv.ellipse(SRC_X + 100 + k * 330 + 16, 700, 16, fill=col, outline=INK, width=2)
            cv.text(SRC_X + 100 + k * 330 + 48, 710, lab, "sansm", CAP, fill=INK, anchor="ls")
    with A(cv, ramp(t, 1.0)):
        cv.text(SRC_X + 100, 790, "approximate, read from chart (US listeners, averaged over composers)", "sans", CAP, fill=INK_SOFT)
    with A(cv, ramp(t, 14.5)):
        cv.text(1350, 235, "your two answers", "sansm", CAP, fill=INK_SOFT, anchor="ls")
    with A(cv, ramp(t, 14.9)):
        bl.chip(cv, 1350, 260, 455, 64, "✓ lighter than slow minor", fill="#EAF4EC", outline="#2E8B57", fg="#1F6B3E")
    with A(cv, ramp(t, 15.4)):
        bl.chip(cv, 1350, 345, 455, 64, "✓ less saturated than fast major", fill="#EAF4EC", outline="#2E8B57", fg="#1F6B3E")
    with A(cv, ramp(t, 15.9)):
        cv.text(1350, 480, "= between", "serifm", 60, fill=SEND, anchor="ls")
    for i, (name, lo, hi, sm, fm, fM) in enumerate(axes):
        y = 220 + i * 150
        with A(cv, band(t, 14.6, 16.2, 0.3)):
            cv.ellipse(X(fm), y, 30, outline=SPARK, width=5)
        with A(cv, band(t, 16.4, 19.8, 0.3)):
            cv.ellipse(X(sm), y, 30, outline=SEND, width=5)
            cv.ellipse(X(fM), y, 30, outline=SEND, width=5)
    sp = ramp(t, 13.4, 0.8)
    bl.small_strip(cv, music=lerp2((0, 0), (0.25, 0.1), sp), color=lerp2((0, 0), (0.25, 0.1), sp))
    src(cv, "Palmer et al. 2013, Fig. 2 (US participants, averaged over composers); values read from the chart, approximate. Paper: faster tempo and major mode each shifted colors (P < 0.001).")


def b12(cv, t):
    bl.headline(cv, "The same sky, swapped")
    HS0 = 13.55
    swap = ramp(t, 2.0, 0.9)
    fastp = seg(t, HS0, HS0 + 4.0)
    slowp = seg(t, HS0 + 4.0, HS0 + 8.0)
    ph = 0.10 + 0.008 * t + 0.06 * fastp + 0.015 * slowp
    landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, mix(SKY_YELLOW, SKY_BLUEGREY, swap), ph)
    landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, mix(SKY_BLUEGREY, SKY_YELLOW, swap), ph + 0.5)
    with A(cv, 1 - ramp(t, 3.0)):
        bl.panel_caption(cv, M, CAPTION_Y, "A", "quick, bright")
        bl.panel_caption(cv, 980, CAPTION_Y, "B", "slow, low")
    with A(cv, ramp(t, 3.3)):
        bl.panel_caption(cv, M, CAPTION_Y, "A", "quick tune, blue-grey sky")
        bl.panel_caption(cv, 980, CAPTION_Y, "B", "slow tune, yellow sky")
    gp = ramp(t, 5.8, 1.2)
    mpos = HS
    cpos = lerp2((0.65, 0.55), SW, gp)
    ps = strip(cv, STRIP_X, STRIP_Y, STRIP_SIZE, music=mpos, color=cpos, label_px=CAP)
    with A(cv, ramp(t, 6.0)):
        bl.dashed(cv, ps["music"][0], ps["music"][1], ps["color"][0], ps["color"][1], fill="#C0392B", width=4)
    with A(cv, ramp(t, 11.4)):
        cv.text(SRC_X + 100, 770, "the feelings disagree", "serifm", 48, fill=SEND, anchor="ls")
    with A(cv, ramp(t, 11.8)):
        cv.text(SRC_X + 100, 826, "music marker: happy, strong   ·   color marker: sad, weak", "sans", CAP, fill=INK_SOFT, anchor="ls")
    with A(cv, band(t, HS0, HS0 + 4.0, 0.1)):
        cv.text(SRC_X + 100, 880, "quick tune playing over the blue-grey sky", "sans", 32, fill=INK_SOFT)
    with A(cv, band(t, HS0 + 4.0, HS0 + 8.0, 0.1)):
        cv.text(SRC_X + 100, 880, "slow tune playing over the yellow sky", "sans", 32, fill=INK_SOFT)
    src(cv, "Illustration. Not data.")


def b13(cv, t):
    cv.text(M, 430, "Humanitarians AI", "serifm", 100, fill=INK, anchor="ls")
    cv.text(M, 510, "Tanmay Kulkarni", "sans", 44, fill=INK_SOFT, anchor="ls")
    cv.line([(M, 560), (M + 780, 560)], fill=BORDER, width=3)
    cv.text(M, 622, "The study: Palmer, Schloss, Xu & Prado-León,", "sans", 30, fill=INK, anchor="ls")
    cv.text(M, 666, "PNAS 110(22), 2013", "sans", 30, fill=INK, anchor="ls")
    cv.text(M, 750, "It began with an essay we read.", "serifi", 42, fill=INK_SOFT, anchor="ls")
    landscape(cv, 1000, 160, 1800, 520, SKY_YELLOW, 0.15 + 0.012 * t)
    landscape(cv, 1000, 560, 1800, 920, SKY_BLUEGREY, 0.65 + 0.012 * t)


FUNCS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06, "B07": b07, "B08": b08, "B09": b09,
         "B10": b10, "B11": b11, "B12": b12, "B13": b13}


def duration(b):
    return TIM[b]["duration_s"]


def nframes(b):
    return int(round(duration(b) * FPS))


def frame(b, t, film_start=False):
    cv = bl.new()
    FUNCS[b](cv, t)
    im = cv.im
    fade = 1.0
    if b == "B01":
        fade = ramp(t, 0.0, 0.5) if t < 0.5 else 1.0             # the film's first frame fades up from the cream page
        fade = clamp(t / 0.5)
    if b == "B13":
        T = duration(b)
        fade = 1.0 - clamp((t - (T - 0.8)) / 0.8)               # final 0.8 s fades to the cream page
    if fade < 0.999:
        base = Image.new("RGB", im.size, hex2rgb(PAGE))
        im = Image.blend(base, im, fade)
    return im


# ----------------------------------------------------------------------------- render / encode

def _job(args):
    b, i = args
    out = FRAMES / b / f"{i:05d}.png"
    if out.exists():
        return
    frame(b, i / FPS).save(out, compress_level=1)


def render(only=None):
    jobs = []
    for b in ORDER:
        if only and b not in only:
            continue
        (FRAMES / b).mkdir(parents=True, exist_ok=True)
        jobs += [(b, i) for i in range(nframes(b))]
    print(f"rendering {len(jobs)} frames with 8 workers", flush=True)
    with Pool(8) as p:
        for k, _ in enumerate(p.imap_unordered(_job, jobs, chunksize=6)):
            if k % 300 == 0:
                print(f"  {k}/{len(jobs)}", flush=True)


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"FAILED: {' '.join(map(str, cmd))}\n{r.stderr[-1500:]}")
    return r


def encode():
    BEATS.mkdir(exist_ok=True)
    PREVIEW.mkdir(exist_ok=True)
    silent = HERE / "_silent"
    silent.mkdir(exist_ok=True)
    for b in ORDER:
        n = nframes(b)
        if "--reuse" in sys.argv and (silent / f"{b}.mp4").exists():
            continue
        sh(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(FRAMES / b / "%05d.png"),
            "-frames:v", str(n), "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-g", "30",
            "-movflags", "+faststart", str(silent / f"{b}.mp4")])
        print("encoded", b, n, "frames", flush=True)
    # master video = beats concatenated (all beats share codec params): stream copy
    lst = silent / "list.txt"
    lst.write_text("".join(f"file '{silent / (b + '.mp4')}'\n" for b in ORDER))
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(silent / "master_video.mp4")])
    # audio: concatenate the beat mixes (each trimmed or padded to exactly its frame count), normalise ONCE
    parts = []
    for b in ORDER:
        d = nframes(b) / FPS
        p = silent / f"{b}.wav"
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "mp3" / f"beat-{b}.mix.wav"), "-af", "apad", "-t", f"{d:.6f}",
            "-ar", "48000", "-ac", "1", str(p)])
        parts.append(p)
    (silent / "alist.txt").write_text("".join(f"file '{p}'\n" for p in parts))
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(silent / "alist.txt"), "-c", "copy",
        str(silent / "master_raw.wav")])
    # two-pass loudnorm for an accurate I=-14 / TP=-1.5
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(silent / "master_raw.wav"), "-af",
                        "loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    js = json.loads(r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1])
    af = (f"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={js['input_i']}:measured_LRA={js['input_lra']}:measured_TP={js['input_tp']}"
          f":measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent / "master_raw.wav"), "-af", af, "-ar", "48000", "-ac", "1",
        str(silent / "master_norm.wav")])
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent / "master_video.mp4"), "-i", str(silent / "master_norm.wav"),
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "1", "-shortest", "-movflags", "+faststart", str(MASTER)])
    # per-beat files with the beat's slice of the normalised audio, and 720p previews
    t0 = 0.0
    for b in ORDER:
        d = nframes(b) / FPS
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent / f"{b}.mp4"), "-ss", f"{t0:.6f}", "-t", f"{d:.6f}",
            "-i", str(silent / "master_norm.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-ar", "48000", "-ac", "1", "-movflags", "+faststart", str(BEATS / f"{b}.mp4")])
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(BEATS / f"{b}.mp4"), "-vf", "scale=1280:720", "-c:v", "libx264",
            "-b:v", "4M", "-maxrate", "5M", "-bufsize", "8M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
            "-movflags", "+faststart", str(PREVIEW / f"{b}.mp4")])
        t0 += d
    print("master:", MASTER)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--frame"]:
        frame(a[1], float(a[2])).save(a[3])
    elif a[:1] == ["--render"]:
        render(a[1:] or None)
    elif a[:1] == ["--encode"]:
        encode()
    elif a[:1] == ["--all"]:
        render()
        encode()
    else:
        print(__doc__)
