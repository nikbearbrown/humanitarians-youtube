#!/usr/bin/env python3
"""Week 28 long film: one 3840x2160 review still per beat (two or three states where a beat has distinct moments).

Standalone Pillow drawer on top of c28_common (palette, Canvas, landscape(), strip(), swatch()). Every figure the
narration speaks is printed on screen in the same still, and asserted from the Canvas text log (see CHECKS).
Visuals follow BEATS-DRAFT.md ('Visual' and 'Source on screen'). Tunes, skies and swatches are illustrations.

Layout contract (after PROOF-REVIEW-RENDERED.md):
  * every source caption ends on ONE common last baseline, y 996 of 1080, at one common left x (520), at most two lines;
  * the strip is 300 px logical (labels 28), lower left: box y 660..960, WEAK label on the same 996 baseline;
  * every sans caption is >= 28 px (the grid tile initials are 28 too; nothing is below 28);
  * free zones: above y 610 across the page, and right of x 620 down to y 920.

Run:  /opt/homebrew/bin/python3.12 build_long_stills.py     -> _stills/Bxx[-a|-b]-16x9.png, _stills/contact-long.png
"""
import colorsys
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from c28_common import (BORDER, CARD, GHOST, INK, INK_SOFT, PAGE, S, SEND, SKY_BLUEGREY, SKY_GREY, SKY_YELLOW, SPARK,
                        SWATCH_BLACK, SWATCH_DARK_CYAN, SWATCH_DARK_GREY, SWATCH_LIGHT_YELLOW, F, Canvas, hex2rgb,
                        landscape, mix, rgba, sky_color, strip, swatch)

OUT = HERE / "_stills"
OUT.mkdir(exist_ok=True)
W, H = 1920, 1080
M = 115
STRIP_X, STRIP_Y, STRIP_SIZE = 170, 660, 300       # the strip, lower left, on screen from frame one
SRC_X, SRC_BASE = 520, 996                          # the one source band: common left x, common last baseline
SRC_W = W - M - SRC_X
BLANK_SKY = "#ECEBE5"
HAPPY_STRONG = (0.7, 0.6)
SAD_WEAK = (-0.7, -0.6)
CAP = 28                                            # minimum sans size


# ----------------------------------------------------------------------------- helpers

def hexc(rgb):
    return "#%02x%02x%02x" % tuple(int(round(v)) for v in rgb)


def wrap(cv, s, kind, size, width):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if cv.tw(t, kind, size) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def new():
    return Canvas(W, H, min_sans=CAP)


def headline(cv, s, y=104):
    cv.text(M, y, s, "serifm", 60, fill=INK, anchor="ls")


def source(cv, s, x=SRC_X, width=SRC_W, size=CAP):
    """Source caption: the LAST line always sits on baseline SRC_BASE; at most two lines; one common left x."""
    lines = wrap(cv, s, "sans", size, width)
    assert len(lines) <= 2, f"source needs {len(lines)} lines: {s}"
    for i, ln in enumerate(lines):
        cv.text(x, SRC_BASE - 36 * (len(lines) - 1 - i), ln, "sans", size, fill=INK_SOFT)


def small_strip(cv, music=(0, 0), color=None, **kw):
    return strip(cv, STRIP_X, STRIP_Y, STRIP_SIZE, music=music, color=color, label_px=CAP, **kw)


def chip(cv, x, y, w, h, s, fill=CARD, outline=BORDER, size=CAP, fg=INK, kind="sansm", width=2):
    cv.rect(x, y, x + w, y + h, fill=fill, outline=outline, width=width, r=h / 2)
    cv.text(x + w / 2, y + h / 2 + size * 0.35, s, kind, size, fill=fg, anchor="ms")


def arrow(cv, x0, y0, x1, y1, fill=INK, width=4, head=18):
    cv.line([(x0, y0), (x1, y1)], fill=fill, width=width)
    a = math.atan2(y1 - y0, x1 - x0)
    pts = [(x1, y1), (x1 - head * math.cos(a - 0.45), y1 - head * math.sin(a - 0.45)),
           (x1 - head * math.cos(a + 0.45), y1 - head * math.sin(a + 0.45))]
    cv.poly(pts, fill)


def dashed(cv, x0, y0, x1, y1, fill=INK, width=3, dash=14, gap=10):
    L = math.hypot(x1 - x0, y1 - y0)
    n = int(L // (dash + gap)) + 1
    for i in range(n):
        a = i * (dash + gap) / L
        b = min(1.0, (i * (dash + gap) + dash) / L)
        cv.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)], fill=fill, width=width)


def pie(cv, cx, cy, r, a0, a1, fill):
    if cv.alpha <= 0.01:
        return
    cv.d.pieslice([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], a0, a1, fill=rgba(fill, cv.alpha))


def arc(cv, cx, cy, r, a0, a1, fill=INK, width=8):
    if cv.alpha <= 0.01:
        return
    cv.d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], a0, a1, fill=rgba(fill, cv.alpha), width=round(width * S))


def play_icon(cv, x, y, active=True):
    col = INK if active else GHOST
    cv.poly([(x, y), (x, y + 30), (x + 26, y + 15)], col)


def panel_caption(cv, x, y, letter, name):
    cv.text(x, y, letter, "serifm", 44, fill=INK, anchor="ls")
    cv.text(x + 46, y - 2, name, "sans", 30, fill=INK_SOFT, anchor="ls")


def hue_array():
    """37 colors: 8 hues x 4 lightness-saturation levels + 3 greys, white, black (the design in the paper's Fig. 1)."""
    hues = [("red", 350), ("orange", 28), ("yellow", 54), ("chartreuse", 80), ("green", 145), ("cyan", 185), ("blue", 212), ("purple", 285)]
    levels = [("S", 0.95, 1.0), ("L", 0.38, 1.0), ("M", 0.40, 0.62), ("D", 1.0, 0.55)]
    out = {}
    for hn, h in hues:
        for ln, s, v in levels:
            out[(hn, ln)] = hexc([c * 255 for c in colorsys.hsv_to_rgb(h / 360, s, v)])
    extras = ["#B0B0AC", "#7A7A76", "#444441", "#FFFFFF", "#111110"]
    return hues, levels, out, extras


# ----------------------------------------------------------------------------- the beats

STILLS = {}      # name -> canvas
CHECKS = {}      # name -> strings that must appear in that still's text log


def put(name, cv, must=()):
    STILLS[name] = cv
    CHECKS[name] = list(must)


PANEL_Y0, PANEL_Y1 = 150, 540       # the two landscape panels (B01, B02, B12)
CAPTION_Y = 592


def b01():
    for state in ("a", "b"):
        cv = new()
        headline(cv, "Which sky goes with which?")
        if state == "a":
            landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, BLANK_SKY, 0.1)
            landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, BLANK_SKY, 0.6)
            panel_caption(cv, M, CAPTION_Y, "A", "quick, bright")
            panel_caption(cv, 980, CAPTION_Y, "B", "slow, low")
            play_icon(cv, 560, CAPTION_Y - 30, True)
            cv.text(SRC_X + 100, 740, "Clip A is playing", "sans", 32, fill=INK_SOFT)
            small_strip(cv, music=(0, 0))
            source(cv, "Illustration: two synthesized tunes, two painted skies. Not data.")
            put("B01-a", cv, ["Which sky goes with which?", "quick, bright", "slow, low", "STRONG", "WEAK", "SAD", "HAPPY", "Not data"])
        else:
            landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, sky_color(0, 1), 0.2)          # 1 = blue-grey (does NOT match play order)
            landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, sky_color(1, 0), 0.6)       # 2 = yellow
            cv.text(M + 8, CAPTION_Y, "1", "serifm", 52, fill=INK, anchor="ls")
            cv.text(980 + 8, CAPTION_Y, "2", "serifm", 52, fill=INK, anchor="ls")
            chip(cv, 1120, 700, 300, 72, "pick one", fill=INK, outline=INK, fg=PAGE, size=36)
            small_strip(cv, music=(0, 0))
            source(cv, "Illustration: two synthesized tunes, two painted skies. Not data.")
            put("B01-b", cv, ["Which sky goes with which?", "pick one", "STRONG", "WEAK", "Not data"])


def b02():
    cv = new()
    headline(cv, "What are we actually matching?")
    landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, SKY_YELLOW, 0.1)
    landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, SKY_BLUEGREY, 0.6)
    panel_caption(cv, M, CAPTION_Y, "A", "quick, bright")
    panel_caption(cv, 980, CAPTION_Y, "B", "slow, low")
    # the strip's two scale names pulse once: an accent halo around the strip and its labels
    cv.rect(STRIP_X - 118, STRIP_Y - 54, STRIP_X + STRIP_SIZE + 140, STRIP_Y + STRIP_SIZE + 44, outline=SPARK, width=4, r=14)
    small_strip(cv, music=(0, 0))
    cv.text(SRC_X + 100, 740, "Most listeners put yellow on the quick one", "serifi", 44, fill=INK_SOFT)
    cv.text(SRC_X + 100, 810, "two scales: happy to sad,  strong to weak", "sans", 32, fill=INK_SOFT)
    put("B02", cv, ["What are we actually matching?", "STRONG", "WEAK", "SAD", "HAPPY"])


def grid_3x2(cv, x0, y0, cw=210, ch=118, highlight=None, grey_others=False, tint=True):
    """SLOW/MEDIUM/FAST columns x MAJOR/MINOR rows; three composer tiles (B, M, Br) in each cell = 18."""
    cols, rows = ["SLOW", "MEDIUM", "FAST"], ["MAJOR", "MINOR"]
    for ci, c in enumerate(cols):
        cv.text(x0 + 110 + ci * (cw + 8) + cw / 2, y0 - 14, c, "sansm", CAP, fill=INK_SOFT, anchor="ms")
    for ri, r in enumerate(rows):
        cv.text(x0 + 100, y0 + ri * (ch + 8) + ch / 2 + 10, r, "sansm", CAP, fill=INK_SOFT, anchor="rs")
    for ri in range(2):
        for ci in range(3):
            x = x0 + 110 + ci * (cw + 8)
            y = y0 + ri * (ch + 8)
            key = (cols[ci], rows[ri])
            fill = CARD
            if tint and key == ("FAST", "MAJOR"):
                fill = mix(SKY_YELLOW, "#FFFFFF", 0.7)
            if tint and key == ("SLOW", "MINOR"):
                fill = mix(SKY_BLUEGREY, "#FFFFFF", 0.7)
            ol = BORDER
            if highlight == key:
                fill, ol = mix(SPARK, "#FFFFFF", 0.82), SPARK
            elif grey_others:
                fill = "#EDEBE4"
            cv.rect(x, y, x + cw, y + ch, fill=fill, outline=ol, width=3 if highlight == key else 2, r=10)
            tw_ = (cw - 16 - 12) / 3
            for ti, lab in enumerate(["B", "M", "Br"]):
                tx = x + 8 + ti * (tw_ + 6)
                live = not grey_others or highlight == key
                cv.rect(tx, y + 38, tx + tw_, y + 82, fill=PAGE if live else "#E4E1D8", outline=BORDER, width=2, r=6)
                cv.text(tx + tw_ / 2, y + 71, lab, "sansm", CAP, fill=INK if live else GHOST, anchor="ms")


def b03():
    hues, levels, arr, extras = hue_array()
    # ---- a: the design
    cv = new()
    headline(cv, "A real test: 18 pieces, 97 listeners")
    cv.text(M, 166, "2013 · orchestral music, 50 s each", "sans", CAP, fill=INK_SOFT)
    grid_3x2(cv, M - 20, 260)
    cv.text(M + 90, 560, "B Bach · M Mozart · Br Brahms: 18 pieces", "sans", CAP, fill=INK_SOFT)
    ax, ay, cw, chh, gap = 1040, 250, 86, 62, 8
    best = {("yellow", "S"), ("yellow", "L"), ("orange", "S"), ("orange", "L"), ("chartreuse", "L")}
    worst = {("blue", "D"), ("purple", "D"), ("cyan", "D"), ("purple", "M"), ("blue", "M")}
    for hi, (hn, _) in enumerate(hues):
        for li, (ln, _, _) in enumerate(levels):
            x = ax + hi * (cw + gap)
            y = ay + li * (chh + gap)
            cv.rect(x, y, x + cw, y + chh, fill=arr[(hn, ln)], outline=BORDER, width=1, r=4)
            if (hn, ln) in best:
                cv.rect(x - 5, y - 5, x + cw + 5, y + chh + 5, outline="#2E8B57", width=5, r=8)
            if (hn, ln) in worst:
                cv.rect(x - 5, y - 5, x + cw + 5, y + chh + 5, outline="#C0392B", width=5, r=8)
    for ei, ec in enumerate(extras):
        x = ax + ei * (cw + gap)
        y = ay + 4 * (chh + gap)
        cv.rect(x, y, x + cw, y + chh, fill=ec, outline=BORDER, width=1, r=4)
    cv.text(ax, ay - 20, "37 colors", "serifm", 40, fill=INK, anchor="ls")
    cv.text(ax, ay + 5 * (chh + gap) + 42, "five fit best", "sansm", CAP, fill="#2E8B57")
    cv.text(ax + 260, ay + 5 * (chh + gap) + 42, "five fit worst", "sansm", CAP, fill="#C0392B")
    cv.text(ax, ay + 5 * (chh + gap) + 86, "(ringed for one tune: an illustration of the design)", "sans", CAP, fill=INK_SOFT)
    small_strip(cv, music=(0, 0))
    source(cv, "Palmer, Schloss, Xu & Prado-León, PNAS 110(22), 2013. UC Berkeley and Univ. of Guadalajara. 48 US + 49 Mexican listeners.")
    put("B03-a", cv, ["18 pieces", "97 listeners", "37 colors", "2013", "50 s", "Univ. of Guadalajara", "five fit best", "five fit worst"])
    # ---- b: the finding (direction only)
    cv = new()
    headline(cv, "Same pattern in both countries")
    for k, (x, title, sub, base) in enumerate([
            (M, "FAST + MAJOR", "lighter, more saturated, yellower", SKY_YELLOW),
            (1000, "SLOW + MINOR", "darker, greyer, bluer", SKY_BLUEGREY)]):
        cv.rect(x, 170, x + 800, 600, fill=CARD, outline=BORDER, width=2, r=14)
        cv.text(x + 30, 232, title, "serifm", 44, fill=INK, anchor="ls")
        cv.text(x + 30, 282, sub, "sans", 32, fill=INK_SOFT, anchor="ls")
        shades = ([mix(base, "#FFFFFF", 0.55), mix(base, "#FFFFFF", 0.25), base, mix(base, "#8B6914", 0.25)] if k == 0
                  else [mix(base, "#FFFFFF", 0.15), base, mix(base, "#2A3441", 0.35), mix(base, "#14181F", 0.55)])
        for si, c in enumerate(shades):
            cv.rect(x + 30 + si * 185, 320, x + 30 + si * 185 + 165, 500, fill=c, outline=BORDER, width=2, r=8)
        cv.text(x + 30, 560, "illustration of the direction of the finding", "sans", CAP, fill=INK_SOFT, anchor="ls")
    cv.text(SRC_X + 100, 740, "United States and Mexico", "serifi", 44, fill=INK_SOFT)
    small_strip(cv, music=(0, 0))
    source(cv, "Palmer, Schloss, Xu & Prado-León, PNAS 110(22), 2013. The paper's own figures are not reproduced.")
    put("B03-b", cv, ["FAST + MAJOR", "SLOW + MINOR", "lighter, more saturated, yellower", "darker, greyer, bluer"])


def b04():
    cv = new()
    headline(cv, "They match through feeling")
    nx = 270
    cv.ellipse(nx, 300, 34, fill=INK)
    cv.text(nx, 250, "MUSIC", "sansm", 30, fill=INK, anchor="ms")
    cv.ellipse(nx, 560, 34, fill=SPARK, outline=INK, width=3)
    cv.text(nx, 630, "COLOR", "sansm", 30, fill=INK, anchor="ms")
    dashed(cv, nx, 350, nx, 508, fill=GHOST, width=4)
    cv.line([(nx - 28, 404), (nx + 28, 454)], fill="#C0392B", width=6)
    cv.line([(nx - 28, 454), (nx + 28, 404)], fill="#C0392B", width=6)
    cv.text(nx, 720, "through feeling", "serifi", 38, fill=INK_SOFT, anchor="ms")
    sx, sy, ss = 600, 200, 440
    pos = strip(cv, sx, sy, ss, music=(0.30, 0.34), color=(0.30, 0.34), label_px=CAP)
    px, py = pos["music"]
    cv.ellipse(px, py, ss * 0.052 + 14, outline=SPARK, width=6)      # the color dot sits on the same spot, ringed so both read
    arrow(cv, nx + 40, 300, px - 22, py - 10, fill=INK, width=4)
    arrow(cv, nx + 40, 560, px - 22, py + 12, fill=SPARK, width=4)
    rx = 1230
    cv.text(rx, 215, "rated on the same feelings (US)", "sansm", CAP, fill=INK_SOFT, anchor="ls")
    rows = [("happy / sad", ".97"), ("lively / dreary", ".99"), ("strong / weak", ".96"), ("angry / calm", ".89")]
    for i, (lab, val) in enumerate(rows):
        y = 290 + i * 90
        cv.text(rx, y + 38, lab, "sans", 32, fill=INK, anchor="ls")
        cv.text(rx + 575, y + 44, val, "serifm", 60, fill=SPARK, anchor="rs")
        cv.line([(rx, y + 58), (rx + 575, y + 58)], fill=BORDER, width=2)
    chip(cv, rx, 680, 575, 64, "correlation, not proof of mechanism", fill="#FBF0EA", outline=SPARK, size=CAP, fg=SEND)
    source(cv, "Emotion ratings of the 18 pieces vs. of the colors picked for them, US participants (Palmer et al. 2013). Mexico: .97, .96, .96, .93.")
    put("B04", cv, [".97", ".99", ".96", ".89", "correlation, not proof of mechanism", "MUSIC", "COLOR", "Mexico: .97, .96, .96, .93", "through feeling"])


def swatch_row(cv, x0, y, items, lit, w=130, h=90, gap=18):
    for i, (c, lab) in enumerate(items):
        x = x0 + i * (w + gap)
        a = cv.alpha
        if i not in lit:
            cv.alpha = a * 0.35
        cv.rect(x, y, x + w, y + h, fill=c, outline=BORDER, width=2, r=8)
        if i in lit:
            cv.rect(x - 6, y - 6, x + w + 6, y + h + 6, outline=SPARK, width=5, r=12)
        cv.alpha = a


def b05():
    methodcard = ["1  rate the sound", "2  rate the color", "3  do they agree?"]
    for state in ("a", "b"):
        cv = new()
        headline(cv, "The paper's own example")
        happy = state == "a"
        sky = SKY_YELLOW if happy else SKY_BLUEGREY
        landscape(cv, 880, 150, 1805, 540, sky, 0.1 if happy else 0.5)
        mus = HAPPY_STRONG if happy else SAD_WEAK
        pos = strip(cv, 170, 190, 420, music=mus, color=mus, label_px=CAP)
        cv.ellipse(pos["music"][0], pos["music"][1], 420 * 0.052 + 14, outline=SPARK, width=6)
        if happy:
            cv.text(880, 596, "Bach · fast dance in F major", "serifm", 44, fill=INK, anchor="ls")
            cv.text(880, 642, "rated: happy, strong", "sans", 32, fill=INK_SOFT, anchor="ls")
            items = [(SKY_YELLOW, ""), (SWATCH_LIGHT_YELLOW, ""), ("#B8C4D6", ""), ("#8A5A9B", ""), (SWATCH_DARK_GREY, "")]
            swatch_row(cv, 880, 690, items, lit={0, 1})
            cv.text(880, 830, "saturated yellow  ·  light yellow", "sans", CAP, fill=INK_SOFT, anchor="ls")
            key = "B05-a"
            must = ["Bach", "F major", "happy, strong", "saturated yellow", "light yellow"]
        else:
            cv.text(880, 596, "Brahms · slow Adagio in C minor", "serifm", 44, fill=INK, anchor="ls")
            cv.text(880, 642, "rated: sad, weak", "sans", 32, fill=INK_SOFT, anchor="ls")
            items = [(SKY_YELLOW, ""), (SWATCH_BLACK, ""), (SWATCH_DARK_GREY, ""), (SWATCH_DARK_CYAN, ""), (SWATCH_LIGHT_YELLOW, "")]
            swatch_row(cv, 880, 690, items, lit={1, 2, 3})
            cv.text(880, 810, "black  ·  dark grey  ·  dark cyan", "sans", CAP, fill=INK_SOFT, anchor="ls")
            cv.rect(SRC_X, 840, 1805, 930, fill=CARD, outline=BORDER, width=2, r=12)
            for i, t in enumerate(methodcard):
                cv.text(SRC_X + 40 + i * 400, 898, t, "serifm", 38, fill=INK, anchor="ls")
            key = "B05-b"
            must = ["Brahms", "C minor", "sad, weak", "black", "dark grey", "dark cyan", "1  rate the sound", "3  do they agree?"]
        source(cv, "The paper's own example of its idea (Palmer et al. 2013).")
        put(key, cv, must + ["STRONG", "WEAK", "The paper's own example"])


def b06():
    cv = new()
    headline(cv, "Sorting comes before the words")
    ty = 500
    x_start, x_end = 200, 1720
    cv.line([(x_start, ty), (x_end, ty)], fill=INK, width=4)
    pos = {0: x_start, 6: x_start + (x_end - x_start) * 6 / 24, 18: x_start + (x_end - x_start) * 18 / 24}
    for m, lab in [(0, "birth"), (6, "6 mo"), (18, "18 mo")]:
        x = pos[m]
        cv.line([(x, ty - 18), (x, ty + 18)], fill=INK, width=4)
        cv.text(x, ty + 62, lab, "serifm", 40, fill=INK, anchor="ms")
    cols = ["#D8573C", "#F2C230", "#3E8E5B", "#3B6FB6", "#8A5A9B", "#E58A3C"]
    for m, cx in [(0, pos[0] + 150), (6, pos[6]), (18, pos[18])]:
        cy, r = 300, 108
        if m == 0:
            cv.ellipse(cx, cy, r, fill="#C9C8C2", outline=BORDER, width=2)
            cv.text(cx, cy + 12, "grey", "serifi", 40, fill=INK_SOFT, anchor="ms")
        else:
            for k, c in enumerate(cols):
                pie(cv, cx, cy, r, k * 60 - 90, k * 60 - 30, c)
            cv.ellipse(cx, cy, r, outline=INK, width=3)
            cv.ellipse(cx, cy, 32, fill=PAGE, outline=INK, width=3)
        if m == 6:
            cv.text(cx, cy - r - 24, "category", "serifm", 40, fill=SEND, anchor="ms")
        if m == 18:
            cv.text(cx, cy - r - 24, "name", "serifm", 40, fill=SEND, anchor="ms")
            for k, (w, c) in enumerate([("red", "#D8573C"), ("blue", "#3B6FB6"), ("yellow", "#B58B00")]):
                chip(cv, cx + r + 30, 220 + k * 70, 160, 54, w, size=30, fg=c)
    cv.text(SRC_X + 100, 760, "the sorting arrives before the words", "serifi", 44, fill=INK_SOFT)
    small_strip(cv, music=(0, 0))
    source(cv, "From an essay we read.")
    put("B06", cv, ["6 mo", "18 mo", "category", "name", "From an essay we read."])


def b07():
    cv = new()
    headline(cv, "Strong, not a law")
    for k, (x, name, col, caps) in enumerate([
            (M, "WHITE", "#FFFFFF", ["purity, in much of the West", "mourning, in many Eastern cultures"]),
            (500, "GREEN", "#3E8E5B", ["growth, in much of the West", "infidelity, in some East Asian contexts"])]):
        cv.text(x, 205, name, "sansm", 30, fill=INK_SOFT, anchor="ls")
        cv.rect(x, 225, x + 210, 380, fill=col, outline=BORDER, width=3, r=10)
        for ci, c in enumerate(caps):
            ls = wrap(cv, c, "sans", CAP, 350)
            for li, ln in enumerate(ls):
                cv.text(x, 436 + ci * 120 + li * 34, ln, "sans", CAP, fill=INK, anchor="ls")
            cv.line([(x, 404 + ci * 120), (x + 350, 404 + ci * 120)], fill=BORDER, width=2)
    tx = 1000
    cv.rect(tx, 190, 1805, 700, fill=CARD, outline=BORDER, width=2, r=14)
    cv.text(tx + 30, 245, "US ↔ Mexico (r)", "serifm", 44, fill=INK, anchor="ls")
    rows = [("red–green", ".88"), ("yellow–blue", ".96"), ("light–dark", ".97"), ("saturation", ".95")]
    for i, (lab, v) in enumerate(rows):
        y = 290 + i * 70
        cv.text(tx + 30, y + 44, lab, "sans", 32, fill=INK, anchor="ls")
        cv.text(tx + 765, y + 48, v, "serifm", 50, fill=INK, anchor="rs")
        cv.line([(tx + 30, y + 62), (tx + 765, y + 62)], fill=BORDER, width=2)
    cv.text(tx + 30, 640, "nonwestern scales: untested", "serifm", 40, fill=SEND, anchor="ls")
    small_strip(cv, music=(0, 0))
    source(cv, "Palmer et al. 2013 (cross-culture correlations; 'unclear' for nonwestern music). Symbolism: from an essay we read.")
    put("B07", cv, ["WHITE", "GREEN", ".88", ".96", ".97", ".95", "nonwestern scales: untested", "essay"])


def b08():
    cv = new()
    headline(cv, "Same length. Very different pulse.")
    x0, x1 = 300, 1760
    T = 40.0
    calm = [10, 9, 12, 9]
    busy = [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3]
    assert sum(calm) == T and sum(busy) == T and len(busy) == 14, (sum(calm), sum(busy), len(busy))
    scale = (x1 - x0) / T
    for row, (durs, lab, base, y) in enumerate([(calm, "calm", SKY_BLUEGREY, 180), (busy, "busy", SKY_YELLOW, 390)]):
        cv.text(M, y + 62, lab, "serifm", 44, fill=INK, anchor="ls")
        x = x0
        for i, d in enumerate(durs):
            w = d * scale
            c = mix(base, "#FFFFFF", 0.28 if i % 2 else 0.0)
            cv.rect(x, y, x + w - 4, y + 110, fill=c, outline=None, r=6)
            cv.text(x + (w - 4) / 2, y + 70, f"{d} s", "sansm", CAP, fill=PAGE if row == 0 else INK, anchor="ms")
            x += w
        cv.text(x0, y + 190, "long scenes, 7–12 s each" if row == 0 else "short scenes, 1–3 s each", "sans", CAP, fill=INK_SOFT, anchor="ls")
    ph = x0 + 0.58 * (x1 - x0)
    cv.line([(ph, 160), (ph, 540)], fill=SPARK, width=5)
    for durs, y in [(busy, 390), (calm, 180)]:
        acc = 0
        for d in durs:
            acc += d
            xx = x0 + acc * scale - 2
            cv.line([(xx, y + 122), (xx, y + 146)], fill=INK_SOFT, width=2)
    cv.text(SRC_X + 100, 760, "calm: cool colors   ·   busy: warm colors", "serifi", 40, fill=INK_SOFT)
    small_strip(cv, music=(0, 0))
    source(cv, "A rule of thumb from an essay we read: calm scenes 7–12 s, busy scenes 1–3 s.")
    put("B08", cv, ["7–12 s", "1–3 s", "calm", "busy", "an essay we read"])


def b09():
    cv = new()
    headline(cv, "60 four-year-olds, 9 minutes")
    cols = [("FAST CARTOON", 420, [0.46, 0.52, 0.40, 0.55], INK), ("SLOWER CARTOON", 960, [0.80, 0.84, 0.76, 0.82], INK_SOFT),
            ("DRAW", 1500, [0.82, 0.78, 0.80, 0.85], INK_SOFT)]
    for name, cx, bars, col in cols:
        cv.text(cx, 186, name, "sansm", 30, fill=col, anchor="ms")
        for i in range(20):
            r, c = divmod(i, 5)
            cv.ellipse(cx - 96 + c * 48, 224 + r * 34, 12, fill=col)
        for j, v in enumerate(bars):
            bx = cx - 108 + j * 60
            h = v * 190
            cv.rect(bx, 540 - h, bx + 44, 540, fill=SPARK if name == "FAST CARTOON" else "#C9C6B8", outline=None, r=4)
        cv.line([(cx - 120, 540), (cx + 120, 540)], fill=INK_SOFT, width=2)
        cv.text(cx, 578, "4 tasks, right afterwards", "sans", CAP, fill=INK_SOFT, anchor="ms")
    chip(cv, 520, 680, 880, 64, "pacing, not color  ·  immediate  ·  four-year-olds", fill="#FBF0EA", outline=SPARK, size=30, fg=SEND)
    cv.text(SRC_X + 100, 810, "each dot is one child (illustrative layout)", "sans", CAP, fill=INK_SOFT)
    small_strip(cv, music=(0, 0))
    source(cv, "Lillard & Peterson, Pediatrics 128(4), 2011. Bar heights are illustrative; the paper reports significant differences, not these values.")
    put("B09", cv, ["60 four-year-olds", "9 minutes", "FAST CARTOON", "SLOWER CARTOON", "DRAW", "pacing, not color", "immediate", "four-year-olds", "2011"])


def b10():
    for state in ("a", "b"):
        cv = new()
        headline(cv, "Where does fast + minor land?")
        sx, sy, ss = 240, 210, 380
        strip(cv, sx, sy, ss, music=None, color=None, label_px=CAP)
        cx, cy = sx + ss / 2, sy + ss / 2
        arrow(cv, cx, cy, cx + 105, cy - 125, fill=SPARK, width=6, head=24)
        arrow(cv, cx, cy, cx - 135, cy + 5, fill=INK, width=6, head=24)
        cv.text(cx + 40, cy - 148, "FAST → strong, lively", "sansm", CAP, fill=SEND, anchor="ms")
        cv.text(sx + 18, cy + 55, "MINOR → sad", "sansm", CAP, fill=INK, anchor="ls")
        grid_3x2(cv, 790, 250, cw=190, ch=118, highlight=("FAST", "MINOR"), grey_others=True, tint=False)
        if state == "a":
            cv.text(790, 570, "FAST + MINOR is in the data", "serifm", 38, fill=INK, anchor="ls")
            cv.text(790, 630, "lighter or darker than slow minor's?", "sans", 30, fill=INK, anchor="ls")
            chip(cv, 790, 648, 220, 56, "LIGHTER")
            chip(cv, 1030, 648, 220, 56, "DARKER")
            cv.text(790, 758, "more or less saturated than fast major's?", "sans", 30, fill=INK, anchor="ls")
            chip(cv, 790, 776, 220, 56, "MORE")
            chip(cv, 1030, 776, 220, 56, "LESS")
            rx, ry = 1620, 400
            arc(cv, rx, ry, 90, 0, 360, fill=BORDER, width=12)
            arc(cv, rx, ry, 90, -90, 190, fill=SPARK, width=12)
            cv.text(rx, ry + 24, "6", "serifm", 80, fill=INK, anchor="ms")
            cv.text(rx, ry + 150, "pause, write both down", "sans", CAP, fill=INK_SOFT, anchor="ms")
            source(cv, "Design: Palmer et al. 2013 crossed tempo × mode (slow/medium/fast × major/minor).")
            put("B10-a", cv, ["Where does fast + minor land?", "FAST → strong, lively", "MINOR → sad", "LIGHTER", "DARKER", "MORE", "LESS", "slow/medium/fast"])
        else:
            cv.rect(790, 560, 1805, 920, fill=CARD, outline=BORDER, width=2, r=14)
            steps = ["1  place tempo's push", "2  place mode's push", "3  predict: between, or closer to one pole", "4  check against the data"]
            for i, t in enumerate(steps):
                cv.text(830, 626 + i * 74, t, "serifm", 40, fill=INK, anchor="ls")
            source(cv, "Design: Palmer et al. 2013 crossed tempo × mode (slow/medium/fast × major/minor).")
            put("B10-b", cv, ["1  place tempo's push", "4  check against the data", "slow/medium/fast"])


def b11():
    cv = new()
    headline(cv, "Fast minor landed between")
    axes = [("saturation", "unsaturated", "saturated", -38, 20, 45),
            ("light–dark", "dark", "light", -40, 25, 45),
            ("yellow–blue", "blue", "yellow", -40, 5, 20)]
    ax0, ax1 = 330, 1230

    def X(v):
        return ax0 + (v + 80) / 160 * (ax1 - ax0)
    for i, (name, lo, hi, sm, fm, fM) in enumerate(axes):
        y = 220 + i * 150
        cv.text(M, y + 8, name, "sansm", 30, fill=INK, anchor="ls")
        cv.line([(ax0, y), (ax1, y)], fill=INK_SOFT, width=3)
        cv.line([(X(0), y - 14), (X(0), y + 14)], fill=INK_SOFT, width=2)
        cv.text(ax0, y + 56, lo, "sans", CAP, fill=INK_SOFT, anchor="ls")
        cv.text(ax1, y + 56, hi, "sans", CAP, fill=INK_SOFT, anchor="rs")
        cv.ellipse(X(sm), y, 20, fill=SKY_BLUEGREY, outline=INK, width=2)
        cv.ellipse(X(fM), y, 20, fill=SKY_YELLOW, outline=INK, width=2)
        cv.ellipse(X(fm), y, 20, fill=SPARK, outline=INK, width=3)
    # legend and the note sit to the right of the strip
    for k, (col, lab) in enumerate([(SKY_BLUEGREY, "slow minor"), (SPARK, "fast minor"), (SKY_YELLOW, "fast major")]):
        cv.ellipse(SRC_X + 100 + k * 330 + 16, 700, 16, fill=col, outline=INK, width=2)
        cv.text(SRC_X + 100 + k * 330 + 48, 710, lab, "sansm", CAP, fill=INK, anchor="ls")
    cv.text(SRC_X + 100, 790, "approximate, read from chart (US listeners, averaged over composers)", "sans", CAP, fill=INK_SOFT)
    cv.text(1350, 235, "your two answers", "sansm", CAP, fill=INK_SOFT, anchor="ls")
    chip(cv, 1350, 260, 455, 64, "✓ lighter than slow minor", fill="#EAF4EC", outline="#2E8B57", fg="#1F6B3E")
    chip(cv, 1350, 345, 455, 64, "✓ less saturated than fast major", fill="#EAF4EC", outline="#2E8B57", fg="#1F6B3E")
    cv.text(1350, 480, "= between", "serifm", 60, fill=SEND, anchor="ls")
    small_strip(cv, music=(0.25, 0.1), color=(0.25, 0.1))
    source(cv, "Palmer et al. 2013, Fig. 2 (US participants, averaged over composers); values read from the chart, approximate. Paper: faster tempo and major mode each shifted colors (P < 0.001).")
    put("B11", cv, ["approximate, read from chart", "slow minor", "fast minor", "fast major", "between", "P < 0.001", "Fig. 2"])


def b12():
    cv = new()
    headline(cv, "The same sky, swapped")
    landscape(cv, M, PANEL_Y0, 940, PANEL_Y1, SKY_BLUEGREY, 0.1)
    landscape(cv, 980, PANEL_Y0, 1805, PANEL_Y1, SKY_YELLOW, 0.6)
    panel_caption(cv, M, CAPTION_Y, "A", "quick tune, blue-grey sky")
    panel_caption(cv, 980, CAPTION_Y, "B", "slow tune, yellow sky")
    pos = strip(cv, STRIP_X, STRIP_Y, STRIP_SIZE, music=HAPPY_STRONG, color=SAD_WEAK, label_px=CAP)
    dashed(cv, pos["music"][0], pos["music"][1], pos["color"][0], pos["color"][1], fill="#C0392B", width=4)
    cv.text(SRC_X + 100, 770, "the feelings disagree", "serifm", 48, fill=SEND, anchor="ls")
    cv.text(SRC_X + 100, 826, "music marker: happy, strong   ·   color marker: sad, weak", "sans", CAP, fill=INK_SOFT, anchor="ls")
    source(cv, "Illustration. Not data.")
    put("B12", cv, ["The same sky, swapped", "the feelings disagree", "Not data"])


def b13():
    cv = new()
    # left column: the sign-off
    cv.text(M, 430, "Humanitarians AI", "serifm", 100, fill=INK, anchor="ls")
    cv.text(M, 510, "Tanmay Kulkarni", "sans", 44, fill=INK_SOFT, anchor="ls")
    cv.line([(M, 560), (M + 780, 560)], fill=BORDER, width=3)
    cv.text(M, 622, "The study: Palmer, Schloss, Xu & Prado-León,", "sans", 30, fill=INK, anchor="ls")
    cv.text(M, 666, "PNAS 110(22), 2013", "sans", 30, fill=INK, anchor="ls")
    cv.text(M, 750, "It began with an essay we read.", "serifi", 42, fill=INK_SOFT, anchor="ls")
    # right column: the film's motif at full colour, two clipped landscapes stacked, no labels
    landscape(cv, 1000, 160, 1800, 520, SKY_YELLOW, 0.15)
    landscape(cv, 1000, 560, 1800, 920, SKY_BLUEGREY, 0.65)
    put("B13", cv, ["Humanitarians AI", "Tanmay Kulkarni", "Palmer, Schloss, Xu & Prado-León", "essay we read"])


# ----------------------------------------------------------------------------- run

def contact():
    names = sorted(STILLS)
    tw, th = 640, 360
    cols = 4
    rows = (len(names) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tw + 20) + 20, rows * (th + 56) + 20), "#DDDAD0")
    d = ImageDraw.Draw(sheet)
    for i, n in enumerate(names):
        im = Image.open(OUT / f"{n}-16x9.png").resize((tw, th), Image.LANCZOS)
        x = 20 + (i % cols) * (tw + 20)
        y = 20 + (i // cols) * (th + 56)
        sheet.paste(im, (x, y))
        d.text((x, y + th + 8), n, font=F("sansm", 12), fill=INK)
    sheet.save(OUT / "contact-long.png")


def main():
    for fn in (b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12, b13):
        fn()
    bad = 0
    for name, cv in STILLS.items():
        text = " | ".join(t[0] for t in cv.log)
        for must in CHECKS[name]:
            if must not in text:
                print(f"CHECK FAIL {name}: missing {must!r}")
                bad += 1
        small = [t for t in cv.log if t[1] < CAP and not t[0].strip() == ""]
        assert not small or all(isinstance(t[0], str) for t in small)
        cv.save(OUT / f"{name}-16x9.png")
        print(f"{name}: {len(cv.log)} text items")
    contact()
    print("checks failed:", bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
