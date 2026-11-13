#!/usr/bin/env python3
"""The Short: ONE continuous 9:16 scene, 2160x3840, scene(t) is a pure function of time (no cuts).

A flat landscape whose sky carries the argument: grey while undecided, yellow with the quick tune, blue-grey with
the slow one. From S02 a two-scale strip (HAPPY-SAD across, STRONG-WEAK up) appears; a music dot and a colour dot
meet on it, move to the paper's own two examples, split apart in the swap, and the loop closes on the yellow sky.

  /opt/homebrew/bin/python3.12 short/build_short.py --cues     # line starts (Whisper clock if present, else plan)
  /opt/homebrew/bin/python3.12 short/build_short.py --stills   # review stills -> short/_stills/ + contact sheet + change measure
  /opt/homebrew/bin/python3.12 short/build_short.py --render   # all frames -> short/_frames/ + _qc/render_log.json (text log per frame)
  /opt/homebrew/bin/python3.12 short/build_short.py --encode   # frames -> short/_video/short-silent.mp4 (H.264 4K portrait, 30 fps)

Layout contract (SHORT-SCRIPT.md): all ink inside x 60..900, y 230..1440 (logical 1080x1920); nothing right of 920
in the lower half; type floor 34 px; headline 56 px at y 270 changing every line; source lines 34 px in the lowest
band; label stacks one line at a time. Illustration colours, not data.
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location("c28", ROOT / "c28_common.py")
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)

W, H = 1080, 1920
SAFE_L, SAFE_R, SAFE_T, SAFE_B = 60, 900, 230, 1440
FPS = 30
TITLE = "Color Never Hears the Music: Why a Fast Tune Gets a Yellow Sky"

# ---------------------------------------------------------------- the clock
PLAN = {"S01": 0.0, "S02": 10.0, "S03": 19.0, "S04": 35.0, "S05": 50.0, "S06": 62.0, "S07": 72.0, "S08": 80.0, "END": 92.0}
NWIN = {"S01": 5, "S02": 4, "S03": 7, "S04": 7, "S05": 5, "S06": 4, "S07": 4, "S08": 5}   # schedule windows per line


def line_starts():
    """Line starts from the Whisper clock (short/mp3/timings_short.json) when it exists; otherwise the plan times."""
    p = HERE / "mp3" / "timings_short.json"
    if not p.exists():
        return dict(PLAN), "plan"
    tm = json.loads(p.read_text())
    out = {}
    for s in tm["sentences"]:
        out.setdefault(s["line"], s["start"])
    ids = sorted(out)
    assert len(ids) == 8, ids
    # each line runs from its first word to the next line's first word; the first line starts at 0, the last ends at the track end
    starts = {k: (0.0 if k == "S01" else max(0.0, out[k] - 0.2)) for k in ids}
    starts["END"] = float(tm["duration_s"])
    return starts, "whisper"


OV = {}      # line -> {boundary index: time}: schedule boundaries moved onto the word they illustrate (set by anchor_windows)
ANCH = {}    # named word times from the Whisper clock


def _wt(words, prefix, lo, hi=None):
    for w, s0, e0 in words:
        if s0 >= lo and (hi is None or s0 <= hi) and w.lower().strip(".,?!'\" -").startswith(prefix):
            return s0
    raise KeyError((prefix, lo))


def anchor_windows(L):
    """Tie the reveal moments to the words that say them (the even split of a line into windows put several labels 1.5-2.5 s
    off the word). Boundaries are the schedule's window edges; only the edges named here move."""
    p = HERE / "mp3" / "timings_short.json"
    if not p.exists():
        return
    words = json.loads(p.read_text())["words"]
    w = lambda pre, lo, hi=None: _wt(words, pre, lo, hi)
    OV.clear()
    OV["S02"] = {1: w("i'm", L["S02"]) - 0.05, 2: w("if", L["S02"]), 3: w("quick", L["S02"] + 3.0)}
    OV["S03"] = {1: w("97", L["S03"]) - 0.1, 2: w("picked", L["S03"]) - 0.1, 3: w("quick", L["S03"] + 6) - 0.1,
                 4: w("slow", L["S03"] + 6) - 0.2, 5: w("slow", L["S03"] + 6) + 0.15, 6: w("minor", L["S03"] + 6) - 0.1}
    OV["S04"] = {0: w("matching", L["S04"]) - 0.5, 1: w("feeling", L["S04"]) + 0.1, 2: w("rated", L["S04"]) + 0.6,
                 3: w("happy", L["S04"]), 4: w("weak", L["S04"]) - 0.4, 5: w("lined", L["S04"]) - 0.1, 6: w("closely", L["S04"]) + 0.1}
    OV["S05"] = {1: w("bach", L["S05"]) - 0.05, 2: w("saturated", L["S05"]) - 0.15, 3: w("brahms", L["S05"]) - 0.15,
                 4: w("brahms", L["S05"]) + 0.15}
    OV["S06"] = {1: w("quick", L["S06"]) - 0.2, 2: w("feelings", L["S06"]) - 0.2, 3: w("longer", L["S06"]) + 0.1}
    OV["S07"] = {0: w("correlation", L["S07"]) - 0.15, 1: w("two", L["S07"] + 3) - 0.15, 2: w("western", L["S07"]) - 0.15}
    OV["S08"] = {1: w("case", L["S08"]), 2: w("full", L["S08"]) - 0.5, 3: w("color", L["S08"] + 2) - 0.25}
    ANCH.update({"bach": w("bach", L["S03"]), "mozart": w("mozart", L["S03"]), "brahms": w("brahms", L["S03"])})


def win(L, line, k):
    """(t0, t1) of window k (0-based) of the line's n schedule windows (edges moved onto words by anchor_windows)."""
    keys = sorted(k_ for k_ in L if k_.startswith("S"))
    t0 = L[line]
    t1 = L[keys[keys.index(line) + 1]] if keys.index(line) + 1 < len(keys) else L["END"]
    n = NWIN[line]
    b = [t0 + (t1 - t0) * i / n for i in range(n + 1)]
    for i, v in OV.get(line, {}).items():
        b[i] = v
    for i in range(1, n + 1):          # keep the edges increasing and inside the line
        b[i] = min(max(b[i], b[i - 1] + 0.05), t1)
    return b[k], b[k + 1]


def fo(t, end, d=0.3):
    """1 until `d` s before `end`, then 0: overlays fade out instead of vanishing on a line boundary."""
    return 1 - ramp(t, end - d, end)


def ctext(cv, x, y, s, kind="sans", size=24, fill=cm.INK, anchor="ls"):
    """All Short text is placed by BASELINE (c28 Canvas.text defaults to the top-left 'la')."""
    cv.text(x, y, s, kind, size, fill=fill, anchor=anchor)


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return 0.5 - 0.5 * math.cos(math.pi * x)


def ramp(t, t0, t1):
    return ease((t - t0) / max(t1 - t0, 1e-6))


def lerp(a, b, p):
    return a + (b - a) * p


# ---------------------------------------------------------------- layout
# 1080x1920 logical. Budget: headline 230-285, landscape 330-820 (full safe width), strip 400 px at y 886 (labels STRONG
# above, WEAK below), sources in the lowest band. A 600 px landscape AND a 400 px strip cannot both fit above the source
# band (330+600+490+100 > 1440), so the landscape is 490 px tall. Every label stack, counter, swatch and title lives
# ON the landscape as a chip, which is why nothing below it ever collides with the strip.
LOOP_TO_GREY = True                               # True: the last 0.7 s eases yellow -> the opening grey, last frame = frame 0 state
LOOP_FADE = 1.0     # was 0.7: the landscape growing back and the sky greying in 0.7 s measured 3.05 grey levels per frame, the largest in the film
LX0, LY0, LX1, LY1 = 60, 330, 900, 820            # landscape
STRIP_X, STRIP_Y, STRIP_SZ = 145, 936, 400
DOT_R = 24                                        # logical px (>= 22)
SRC_BASE = {1: [1432], 2: [1391, 1432], 3: [1350, 1391, 1432]}   # source-line baselines (lowest safe band)

HEADLINES = {"S01": "Which sky goes with which?", "S02": "Most listeners pick yellow for quick",
             "S03": "A real test, two countries", "S04": "They match through feeling", "S05": "Their own example",
             "S06": "Swap them and it clashes", "S07": "Strong, not a law", "S08": "Test your own"}
SOURCES = {"S01": "Illustration: our tunes, our skies. Not data.",
           "S02": "Palmer et al., PNAS 2013: US and Mexico.",
           "S03": "Palmer, Schloss, Xu & Prado-León, PNAS 110(22), 2013.",
           "S04": "Emotion ratings, music vs. chosen colors: 0.89–0.99 (Palmer et al. 2013). Correlation, not proof.",
           "S05": "The paper's own example of its idea (Palmer et al. 2013).",
           "S06": "Illustration. Not data.",
           "S07": "Palmer et al. 2013: unclear for non-Western scales.",
           "S08": "Palmer et al. tested US and Mexico only."}

# strip spots (x: SAD -1 .. HAPPY +1, y: WEAK -1 .. STRONG +1)
SPOT_MATCH_M, SPOT_MATCH_C = (-0.70, -0.38), (-0.50, -0.48)
SPOT_HAPPY, SPOT_SAD = (0.75, 0.10), (-0.75, -0.10)


def sky_rgb(yel, blu):
    """Sky colour: grey -> yellow (S01/S02), and blue-grey <-> yellow THROUGH a warm grey. Mixing yellow with blue
    directly passes through a muddy green, which reads as neither warmer nor cooler."""
    if blu <= 0.001:
        return cm.mix(cm.SKY_GREY, cm.SKY_YELLOW, yel)
    if yel <= 0.001:
        return cm.mix(cm.SKY_GREY, cm.SKY_BLUEGREY, blu)
    p = yel / max(yel + blu, 1e-6)           # 0 = blue-grey, 1 = yellow
    return cm.mix(cm.SKY_BLUEGREY, cm.SKY_GREY, p * 2) if p < 0.5 else cm.mix(cm.SKY_GREY, cm.SKY_YELLOW, p * 2 - 1)


def which_line(L, t):
    keys = sorted(k for k in L if k.startswith("S"))
    cur = keys[0]
    for k in keys:
        if t >= L[k]:
            cur = k
    return cur


def local(L, t):
    """(line, window index, fraction through that window)."""
    line = which_line(L, t)
    for k in range(NWIN[line]):
        a, b = win(L, line, k)
        if t < b or k == NWIN[line] - 1:
            return line, k, clamp((t - a) / max(b - a, 1e-6))
    raise AssertionError


# ---------------------------------------------------------------- state functions of t
def sky_state(L, t):
    """(yellow, blue) amounts, 0..1."""
    s02, s03, s04, s05, s06, s07, s08 = (L[k] for k in ("S02", "S03", "S04", "S05", "S06", "S07", "S08"))
    if t < s02:
        return 0.0, 0.0
    if t < s03:                                   # warms to yellow: starts at S02 w0, done by S02 w2
        p = ramp(t, win(L, "S02", 0)[0], win(L, "S02", 2)[0])
        return p, 0.0
    if t < s04:                                   # yellow until the tune slows, then cools to blue-grey by the end of S03
        p = ramp(t, win(L, "S03", 5)[0], L["S04"])
        return 1 - p, p
    if t < s05:
        return 0.0, 1.0
    if t < s06:                                   # Bach yellow (S05 w2), Brahms cools (S05 w3-w4)
        up = ramp(t, win(L, "S05", 1)[0], win(L, "S05", 2)[0])
        down = ramp(t, win(L, "S05", 3)[0], win(L, "S05", 4)[1])
        y = up * (1 - down)
        return y, 1 - y
    if t < s07:
        return 0.0, 1.0
    if t < s08:                                   # drifts slowly warmer across S07 w2-w3
        p = ramp(t, win(L, "S07", 1)[0], L["S08"]) * 0.45
        return p, 1 - p
    p = ramp(t, win(L, "S08", 0)[0], win(L, "S08", 1)[0])    # warms back to yellow
    y0 = 0.45
    y = lerp(y0, 1.0, p)
    return y, 1 - y


def tune_speed(L, t):
    """Cloud speed: fast under the quick tune, slow under the slow one (phase units per second)."""
    q, sl = 0.16, 0.03
    s = lambda k: L[k]
    if t < win(L, "S01", 2)[0]:
        return q
    if t < s("S02"):
        return sl
    if t < win(L, "S03", 4)[0]:
        return q
    if t < s("S05"):
        return sl
    if t < win(L, "S05", 3)[0]:
        return q
    if t < s("S06"):
        return sl
    if t < s("S07"):
        return q
    if t < s("S08"):
        return sl
    return q


_phase_cache = {}


def cloud_phase(L, t):
    key = tuple(round(v, 3) for v in L.values())
    if key not in _phase_cache:
        dt = 0.05
        n = int(L["END"] / dt) + 2
        tab = [0.0]
        for i in range(n):
            tab.append(tab[-1] + tune_speed(L, i * dt) * dt)
        _phase_cache[key] = tab
    tab = _phase_cache[key]
    x = clamp(t, 0, L["END"]) / 0.05
    i = int(x)
    return lerp(tab[i], tab[min(i + 1, len(tab) - 1)], x - i)


def strip_state(L, t):
    """(dim, labels, music_xy, color_xy) for the strip; dim 0 = absent."""
    s02, s03, s04, s05, s06, s07, s08 = (L[k] for k in ("S02", "S03", "S04", "S05", "S06", "S07", "S08"))
    dim, labels, music, color = 0.0, False, None, None
    if t >= win(L, "S02", 3)[0]:
        dim = 0.8 * ramp(t, win(L, "S02", 3)[0], win(L, "S02", 3)[1])
    if t >= s04:
        dim = lerp(0.8, 1.0, ramp(t, win(L, "S04", 0)[0], win(L, "S04", 0)[1]))
        labels = t >= win(L, "S04", 1)[0]
    if t >= win(L, "S04", 2)[0]:                  # music dot slides in from the top right
        p = ramp(t, win(L, "S04", 2)[0], win(L, "S04", 2)[1])
        music = (lerp(0.9, SPOT_MATCH_M[0], p), lerp(0.9, SPOT_MATCH_M[1], p))
    if t >= win(L, "S04", 3)[0]:                  # colour dot slides in from the bottom right
        p = ramp(t, win(L, "S04", 3)[0], win(L, "S04", 3)[1])
        color = (lerp(0.9, SPOT_MATCH_C[0], p), lerp(-0.9, SPOT_MATCH_C[1], p))
    if t >= s05:                                  # to the HAPPY end, then to the SAD end
        a = ramp(t, win(L, "S05", 0)[0], win(L, "S05", 1)[0])
        b = ramp(t, win(L, "S05", 3)[0], win(L, "S05", 4)[0] + 0.9)
        def where(spot0, spot1, spot2):
            x = lerp(lerp(spot0[0], spot1[0], a), spot2[0], b)
            y = lerp(lerp(spot0[1], spot1[1], a), spot2[1], b)
            return (x, y)
        music = where(SPOT_MATCH_M, SPOT_HAPPY, SPOT_SAD)
        color = where(SPOT_MATCH_C, (SPOT_HAPPY[0] - 0.20, SPOT_HAPPY[1] - 0.10), (SPOT_SAD[0] + 0.20, SPOT_SAD[1] + 0.10))
    if t >= s06:                                  # the swap: music (quick) goes to HAPPY, colour (blue-grey) stays at SAD
        p = ramp(t, win(L, "S06", 1)[0], win(L, "S06", 2)[0])
        music = (lerp(SPOT_SAD[0], SPOT_HAPPY[0], p), lerp(SPOT_SAD[1], SPOT_HAPPY[1], p))
        color = (SPOT_SAD[0] + 0.20, SPOT_SAD[1] + 0.10)
    if t >= s07:
        dim = lerp(1.0, 0.55, ramp(t, s07, win(L, "S07", 1)[0]))
    if t >= s08:
        dim = 0.55 * (1 - ramp(t, win(L, "S08", 2)[0], win(L, "S08", 2)[1]))
    return dim, labels, music, color


# ---------------------------------------------------------------- drawing helpers
def wrap_lines(cv, s, kind, size, maxw):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t_ = (cur + " " + w_).strip()
        if cv.tw(t_, kind, size) <= maxw:
            cur = t_
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    return lines


def chip(cv, x, y, s, size=36, pad=14, fill=cm.CARD, a=1.0):
    """White chip with ink text; (x, y) is the top-left of the chip."""
    a0 = cv.alpha
    cv.alpha = a0 * a
    w_ = cv.tw(s, "sansm", size) + 2 * pad
    cv.rect(x, y, x + w_, y + size + 2 * pad - 4, fill=fill, outline=cm.BORDER, width=2, r=8)
    ctext(cv, x + pad, y + pad + size * 0.80, s, "sansm", size, fill=cm.INK)
    cv.alpha = a0
    return w_


def loop_p(L, t):
    """0..1 over the last LOOP_FADE seconds when LOOP_TO_GREY, else 0."""
    return ramp(t, L["END"] - LOOP_FADE, L["END"]) if LOOP_TO_GREY else 0.0


def draw_headline(cv, L, t):
    keys = sorted(k for k in L if k.startswith("S"))
    cur = which_line(L, t)
    i = keys.index(cur)
    # one headline at a time: the old one fades out in the first 0.2 s of the new line, the new one fades in over the next 0.2 s
    # (a cross-fade drew both texts at half strength on top of each other)
    items = []
    if i > 0 and t < L[cur] + 0.2:
        items.append((HEADLINES[keys[i - 1]], 1 - ramp(t, L[cur], L[cur] + 0.2)))
    items.append((HEADLINES[cur], ramp(t, L[cur] + 0.2, L[cur] + 0.4) if i > 0 else 1.0))
    lp = loop_p(L, t)
    if lp > 0:                                   # loop: the closing headline fades out, then the opening one fades in
        items = [(h, a * (1 - ramp(lp, 0.0, 0.5))) for h, a in items] + [(HEADLINES["S01"], ramp(lp, 0.5, 1.0))]
    for h, a in items:
        cv.alpha = a
        ctext(cv, SAFE_L, 270, h, "serifm", 56, fill=cm.INK)
    cv.alpha = 1.0


def draw_source(cv, L, t):
    keys = sorted(k for k in L if k.startswith("S"))
    cur = which_line(L, t)
    i = keys.index(cur)
    items = ([(keys[i - 1], 1 - ramp(t, L[cur], L[cur] + 0.2))] if i > 0 and t < L[cur] + 0.2 else []) + \
            [(cur, ramp(t, L[cur] + 0.2, L[cur] + 0.4) if i > 0 else 1.0)]
    lp = loop_p(L, t)
    if lp > 0:
        items = [(k, a * (1 - ramp(lp, 0.0, 0.5))) for k, a in items] + [("S01", ramp(lp, 0.5, 1.0))]
    for line, a in items:
        cv.alpha = a
        lines = wrap_lines(cv, SOURCES[line], "sans", 34, SAFE_R - SAFE_L)
        assert len(lines) <= 2, (line, lines)
        for b, ln in zip(SRC_BASE[len(lines)], lines):
            ctext(cv, SAFE_L, b, ln, "sans", 34, fill=cm.INK_SOFT)
    cv.alpha = 1.0


def chip_stack(cv, entries, size=40, x=None, y0=None, gap=10):
    """Label chips stacked top-left on the sky: [(text, alpha)]. One entry per line, never more than three."""
    assert len(entries) <= 3
    x = LX0 + 18 if x is None else x
    y = LY0 + 18 if y0 is None else y0
    for s_, a in entries:
        chip(cv, x, y, s_, size=size, a=a)
        y += size + 28 + gap


def swatch_chip(cv, x, y, color, lines, a=1.0, size=36):
    """White chip with a colour square and a one- or two-line label; (x, y) is the top-left."""
    a0 = cv.alpha
    cv.alpha = a0 * a
    tw = max(cv.tw(ln, "sansm", size) for ln in lines)
    h = max(80, 34 + len(lines) * (size + 6))
    cv.rect(x, y, x + 20 + 96 + 16 + tw + 20, y + h, fill=cm.CARD, outline=cm.BORDER, width=2, r=10)
    cv.rect(x + 20, y + (h - 60) / 2, x + 20 + 96, y + (h - 60) / 2 + 60, fill=color, outline=cm.BORDER, width=2, r=6)
    for i, ln in enumerate(lines):
        ctext(cv, x + 20 + 96 + 16, y + 20 + size * 0.85 + i * (size + 6), ln, "sansm", size, fill=cm.INK)
    cv.alpha = a0


def landscape_bottom(L, t):
    """Before the strip exists the landscape fills the frame down to y 1240; it settles to 820 as the strip hint fades in."""
    a = win(L, "S02", 3)[0]
    base = lerp(1240, LY1, ramp(t, a - 0.3, a + 2.1))      # 2.4 s: a faster settle showed up in the gate as a near-cut (3.6 grey levels per frame)
    return int(round(lerp(base, 1240, loop_p(L, t))))      # the loop: the landscape grows back to the opening frame


def dot(cv, p, fill, outline=None, r=DOT_R):
    cv.ellipse(p[0], p[1], r, fill=fill, outline=outline, width=3 if outline else 1)


def strip_px(p):
    cx, cy = STRIP_X + STRIP_SZ / 2, STRIP_Y + STRIP_SZ / 2
    pad = STRIP_SZ * 0.12
    return cx + p[0] * (STRIP_SZ / 2 - pad), cy - p[1] * (STRIP_SZ / 2 - pad)


def scene(L, t, S_scale=None):
    """Draw the whole Short at time t. Returns the Canvas."""
    cv = cm.Canvas(W, H, min_sans=34)
    draw_headline(cv, L, t)
    yel, blu = sky_state(L, t)
    lp = loop_p(L, t)
    if lp > 0:                                    # last 0.7 s: yellow eases back to the opening grey
        yel, blu = yel * (1 - lp), blu * (1 - lp)
    ly1 = landscape_bottom(L, t)
    cm.landscape(cv, LX0, LY0, LX1, ly1, sky_rgb(yel, blu), cloud_phase=cloud_phase(L, t))
    s02, s03, s04, s05, s06, s07, s08 = (L[k] for k in ("S02", "S03", "S04", "S05", "S06", "S07", "S08"))
    # S01: which tune is playing (chip top-left of the sky)
    if t < s02:
        a0, a1 = win(L, "S01", 0)[0], win(L, "S01", 2)[0]
        if t < a1:
            chip(cv, LX0 + 18, LY0 + 18, "A: quick, bright", a=ramp(t, a0, a0 + 0.4))
        else:
            chip(cv, LX0 + 18, LY0 + 18, "B: slow, low", a=ramp(t, a1, a1 + 0.4) * fo(t, s02))
    # S01-S02: the two candidate skies as swatch chips at the foot of the landscape; the quick one is ringed in S02
    sw_a = 0.0
    if t >= win(L, "S01", 4)[0]:
        sw_a = ramp(t, win(L, "S01", 4)[0], win(L, "S01", 4)[0] + 0.5)
    if t >= s02:
        sw_a = 1 - ramp(t, win(L, "S02", 3)[0], win(L, "S02", 3)[0] + 0.4)
    if sw_a > 0.01:
        sy = ly1 - 96
        swatch_chip(cv, LX0 + 18, sy, cm.SKY_BLUEGREY, ["1 blue-grey"], a=sw_a)
        x2 = LX0 + 18 + 380
        swatch_chip(cv, x2, sy, cm.SKY_YELLOW, ["2 yellow"], a=sw_a)
        if t >= s02:
            ra = ramp(t, win(L, "S02", 2)[0], win(L, "S02", 2)[0] + 0.4) * (0.8 + 0.2 * math.sin((t - s02) * 5)) * sw_a
            cv.alpha = clamp(ra)
            cv.rect(x2 - 8, sy - 8, x2 + 20 + 96 + 16 + cv.tw("2 yellow", "sansm", 36) + 20 + 8, sy + 80 + 8, outline=cm.SPARK, width=5, r=14)
            chip(cv, x2, sy - 76, "quick tune", size=36, a=1.0)
            cv.alpha = 1.0
    # S02: name line, top-left of the sky
    if s02 <= t < s03 + 0.5:
        a = ramp(t, win(L, "S02", 1)[0], win(L, "S02", 1)[0] + 0.5) * (1 - ramp(t, s03, s03 + 0.5))
        if a > 0.01:
            chip(cv, LX0 + 18, LY0 + 18, "Tanmay Kulkarni · Humanitarians AI", a=a)
    # S03: chip stack, then the two results one at a time
    if s03 <= t < s04:
        c0 = win(L, "S03", 3)[0]
        clear = 1 - ramp(t, c0 - 0.3, c0)
        t0 = win(L, "S03", 0)[0]
        tail = fo(t, s04)
        if t < c0:
            nm_t = [ANCH["bach"] - 0.1, ANCH["mozart"] - 0.1, ANCH["brahms"] - 0.1]
            x = LX0 + 18
            words = ["Bach", "Mozart", "Brahms"]
            # composers revealed one by one inside ONE chip row: draw the chip for the names revealed so far
            shown = [w_ for w_, tt in zip(words, nm_t) if t >= tt]
            if shown:
                a = ramp(t, nm_t[0], nm_t[0] + 0.3) * clear * tail
                chip(cv, x, LY0 + 18, " · ".join(shown), size=40, a=a)
            entries = []
            if t >= win(L, "S03", 1)[0]:
                entries.append(("97 listeners · US + Mexico", ramp(t, win(L, "S03", 1)[0], win(L, "S03", 1)[0] + 0.4) * clear * tail))
            if t >= win(L, "S03", 2)[0]:
                entries.append(("picked colors for each piece", ramp(t, win(L, "S03", 2)[0], win(L, "S03", 2)[0] + 0.4) * clear * tail))
            y = LY0 + 18 + 78
            for s_, a in entries:
                chip(cv, x, y, s_, size=40, a=a)
                y += 78
        else:
            q_a = ramp(t, c0, c0 + 0.4) * (1 - ramp(t, win(L, "S03", 5)[0] - 0.2, win(L, "S03", 5)[0] + 0.2)) * tail
            s_a = ramp(t, win(L, "S03", 6)[0], win(L, "S03", 6)[0] + 0.4) * tail
            chip(cv, LX0 + 18, LY0 + 18, "quick + major → lighter, yellower", size=40, a=q_a)
            chip(cv, LX0 + 18, LY0 + 18, "slow + minor → darker, bluer", size=40, a=s_a)
    # S04: ratings counter chip
    if s04 <= t < s05:
        c_a = ramp(t, win(L, "S04", 5)[0], win(L, "S04", 5)[0] + 0.4) * fo(t, s05)
        if c_a > 0.01:
            val = 0.99 * ramp(t, win(L, "S04", 5)[0], win(L, "S04", 6)[0])
            a0 = cv.alpha
            cv.alpha = c_a
            cap = "ratings of music vs. colors:"
            cv.rect(LX0 + 18, LY0 + 18, LX0 + 18 + 520, LY0 + 18 + 150, fill=cm.CARD, outline=cm.BORDER, width=2, r=10)
            ctext(cv, LX0 + 36, LY0 + 18 + 48, cap, "sans", 36, fill=cm.INK_SOFT)
            ctext(cv, LX0 + 36, LY0 + 18 + 126, "up to ", "sans", 36, fill=cm.INK_SOFT)
            ctext(cv, LX0 + 36 + cv.tw("up to ", "sans", 36), LY0 + 18 + 130, f"{val:.2f}", "serifm", 84, fill=cm.SPARK)
            assert cv.tw(cap, "sans", 36) < 480
            cv.alpha = a0
    # S05: the paper's own examples as swatch chips at the foot of the landscape
    if s05 <= t < s06:
        b_in = ramp(t, win(L, "S05", 1)[0], win(L, "S05", 1)[0] + 0.4) * (1 - ramp(t, win(L, "S05", 3)[0], win(L, "S05", 3)[0] + 0.4)) * fo(t, s06)
        sw_in = ramp(t, win(L, "S05", 2)[0], win(L, "S05", 2)[0] + 0.4) * (1 - ramp(t, win(L, "S05", 3)[0], win(L, "S05", 3)[0] + 0.4)) * fo(t, s06)
        r_in = ramp(t, win(L, "S05", 4)[0], win(L, "S05", 4)[0] + 0.4) * fo(t, s06)
        sy = LY1 - 96
        if b_in > 0.01:
            # label first (w1), the colour square lands a window later (w2): a text-only chip, then the full chip
            if sw_in > 0.01:
                swatch_chip(cv, LX0 + 18, sy, cm.SKY_YELLOW, ["Bach · fast dance"], a=min(sw_in, 1.0))
            else:
                chip(cv, LX0 + 18, sy, "Bach · fast dance", size=36, a=b_in)
        if r_in > 0.01:
            swatch_chip(cv, LX0 + 18, sy, cm.SWATCH_DARK_GREY, ["Brahms · slow Adagio"], a=r_in)
    # S06: the word for the gap
    if s06 <= t < s07:
        a = ramp(t, win(L, "S06", 2)[0], win(L, "S06", 2)[0] + 0.4) * fo(t, s07)
        cv.alpha = a
        cv.rect(LX0 + 18, LY0 + 18, LX0 + 18 + 260, LY0 + 18 + 84, fill=cm.CARD, outline=cm.BORDER, width=2, r=10)
        ctext(cv, LX0 + 18 + 24, LY0 + 18 + 62, "disagree", "serifm", 56, fill=cm.SPARK)
        cv.alpha = 1.0
    # S07: the limit, three chips one at a time
    if s07 <= t < s08:
        ents = [("correlation", win(L, "S07", 0)[0]), ("2 countries", win(L, "S07", 1)[0]), ("Western classical only", win(L, "S07", 2)[0])]
        chip_stack(cv, [(s_, ramp(t, t0, t0 + 0.4) * (1 - ramp(t, s08 - 0.4, s08))) for s_, t0 in ents], size=40)
    # strip + dots (dots drawn here at DOT_R, not by the shared helper)
    dim, labels, music, color = strip_state(L, t)
    if dim > 0.01:
        cm.strip(cv, STRIP_X, STRIP_Y, STRIP_SZ, music=None, color=None, show_labels=False, label_px=36, dim=dim)
        if labels:
            # SAD / HAPPY sit outside the card; STRONG / WEAK sit INSIDE it (top and bottom centre), so the card can drop 50 px
            # without WEAK meeting the source lines (a label below a card at y 936 would end at y 1380, in the source band)
            a0 = cv.alpha
            cv.alpha = a0 * dim
            cx, cy = STRIP_X + STRIP_SZ / 2, STRIP_Y + STRIP_SZ / 2
            for txt, x_, y_, anc in (("SAD", STRIP_X - 12, cy + 13, "rs"), ("HAPPY", STRIP_X + STRIP_SZ + 12, cy + 13, "ls"),
                                     ("STRONG", cx, STRIP_Y + 54, "ms"), ("WEAK", cx, STRIP_Y + STRIP_SZ - 20, "ms")):
                if anc == "ms":
                    w_ = cv.tw(txt, "sansm", 36)
                    cv.rect(x_ - w_ / 2 - 10, y_ - 34, x_ + w_ / 2 + 10, y_ + 10, fill=cm.CARD)      # card-coloured backing hides the cross-hair
                ctext(cv, x_, y_, txt, "sansm", 36, fill=cm.INK_SOFT, anchor=anc)
            cv.alpha = a0
        a0 = cv.alpha
        cv.alpha = a0 * dim
        pm_ = strip_px(music) if music is not None else None
        pc_ = strip_px(color) if color is not None else None
        if pc_:
            dot(cv, pc_, cm.SPARK, outline=cm.INK)
        if pm_:
            dot(cv, pm_, cm.INK)
        cv.alpha = a0
        if s04 <= t < s05 and pm_ and pc_:                 # the dots meet: a ring pulses
            a_, b_ = win(L, "S04", 4)
            if a_ <= t < b_ + 0.6:
                p = ramp(t, a_, b_ + 0.6)
                cx, cy = (pm_[0] + pc_[0]) / 2, (pm_[1] + pc_[1]) / 2
                cv.alpha = dim * (1 - p)
                cv.ellipse(cx, cy, 36 + 50 * p, outline=cm.SPARK, width=4)
                cv.alpha = 1.0
        if s06 <= t < s07 and pm_ and pc_:                 # the gap between the dots
            g = ramp(t, win(L, "S06", 2)[0], win(L, "S06", 2)[1])
            pulse = 1 + 0.25 * math.sin(max(0.0, t - win(L, "S06", 3)[0]) * 7) if t >= win(L, "S06", 3)[0] else 1.0
            cv.alpha = dim * g
            (x0, y0), (x1, y1) = pm_, pc_
            n = 16
            for i in range(0, n, 2):
                cv.line([(lerp(x0, x1, i / n), lerp(y0, y1, i / n)), (lerp(x0, x1, (i + 1) / n), lerp(y0, y1, (i + 1) / n))], fill=cm.SPARK, width=5 * pulse)
            cv.alpha = 1.0
    # S08 closing title over the foot of the landscape
    if t >= win(L, "S08", 3)[0]:
        a = ramp(t, win(L, "S08", 3)[0], win(L, "S08", 3)[0] + 0.8) * (1 - ramp(lp, 0.0, 0.5))
        cv.alpha = a
        cv.rect(SAFE_L, 570, SAFE_R, 810, fill=cm.CARD, outline=cm.BORDER, width=2, r=14)
        lines = wrap_lines(cv, TITLE, "serifm", 52, SAFE_R - SAFE_L - 60)
        assert len(lines) <= 3, lines
        for i, ln in enumerate(lines):
            ctext(cv, SAFE_L + 30, 640 + i * 62, ln, "serifm", 52, fill=cm.INK)
        ctext(cv, SAFE_L + 30, 640 + len(lines) * 62 + 14, "Humanitarians AI", "sansm", 36, fill=cm.INK_SOFT)
        cv.alpha = 1.0
    draw_source(cv, L, t)
    return cv


# ---------------------------------------------------------------- stills
def still_times(L):
    def mid(line, k, f=0.5):
        a, b = win(L, line, k)
        return a + (b - a) * f
    return [
        ("S01-a", mid("S01", 0, 0.8)), ("S01-b", mid("S01", 3, 0.6)), ("S01-c", mid("S01", 4, 0.8)),
        ("S02-a", mid("S02", 1, 0.8)), ("S02-b", mid("S02", 3, 0.5)),
        ("S03-a", mid("S03", 2, 0.9)), ("S03-b", mid("S03", 3, 0.7)), ("S03-c", mid("S03", 6, 0.7)),
        ("S04-a", mid("S04", 1, 0.8)), ("S04-b", mid("S04", 3, 0.5)), ("S04-c", mid("S04", 5, 0.5)), ("S04-d", mid("S04", 6, 0.9)),
        ("S05-a", mid("S05", 1, 0.8)), ("S05-b", mid("S05", 2, 0.9)), ("S05-c", mid("S05", 4, 0.9)),
        ("S06-a", mid("S06", 0, 0.9)), ("S06-b", mid("S06", 3, 0.6)),
        ("S07-a", mid("S07", 2, 0.9)), ("S07-b", mid("S07", 3, 0.7)),
        ("S08-a", mid("S08", 1, 0.8)), ("S08-b", mid("S08", 3, 0.4)), ("S08-c", L["END"] - LOOP_FADE - 0.3), ("S08-d", L["END"] - 0.02),
    ]


def ink_bbox(im, bg=(250, 249, 245)):
    a = np.asarray(im.convert("RGB")).astype(int)
    d = np.abs(a - np.array(bg)).sum(axis=2) > 12
    ys, xs = np.where(d)
    return xs.min() / cm.S, xs.max() / cm.S, ys.min() / cm.S, ys.max() / cm.S


def check_still(name, cv):
    l, r, t, b = ink_bbox(cv.im)
    ok = l >= SAFE_L - 3 and r <= SAFE_R + 3 and t >= SAFE_T - 6 and b <= SAFE_B + 3
    for s, size, a, x, y in cv.log:
        assert size >= 34 or a < 0.02, (name, s, size)
        assert SAFE_T - 6 <= y <= SAFE_B + 3, (name, s, y)
    return ok, (round(l), round(r), round(t), round(b))


def make_stills(L, src):
    out = HERE / "_stills"
    out.mkdir(exist_ok=True)
    report, thumbs = [], []
    for name, t in still_times(L):
        cv = scene(L, t)
        ok, bb = check_still(name, cv)
        cv.save(out / f"{name}-9x16.png")
        report.append((name, round(t, 2), ok, bb))
        thumbs.append((name, cv.im.resize((360, 640), Image.LANCZOS)))
        print(f"{name} t={t:6.2f}s  ink x{bb[0]}-{bb[1]} y{bb[2]}-{bb[3]}  {'OK' if ok else 'OUTSIDE SAFE AREA'}", flush=True)
    # contact sheet, 4 across
    cols = 4
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * 380 + 20, rows * 680 + 20), "#DDDACF")
    from PIL import ImageDraw
    d = ImageDraw.Draw(sheet)
    for i, (name, im) in enumerate(thumbs):
        x, y = 20 + (i % cols) * 380, 20 + (i // cols) * 680
        sheet.paste(im, (x, y))
        d.text((x + 6, y + 648), name, fill="#3D3929")
    sheet.save(out / "contact-short.png")
    return report


def change_measure(L, step=0.5, gap=2.5, thr=0.30):
    """Percent of pixels that differ between frames `gap` s apart, at 540x960, across the whole film."""
    from multiprocessing import Pool
    ts = [round(i * step, 3) for i in range(int((L["END"] - gap) / step) + 1)]
    return ts, gap, thr


def frame_small(args):
    L, t = args
    anchor_windows(L)
    cm.S = 1          # logical 1080x1920, then halved to 540x960 (c28's canvas needs an integer scale)
    cm._fc.clear()
    cv = scene(L, t)
    return np.asarray(cv.im.convert("L").resize((540, 960), Image.LANCZOS)).astype(np.int16)


def run_change_measure(L):
    from multiprocessing import Pool
    step, gap, thr = 0.5, 2.5, 0.30
    times = sorted(set([round(i * step, 3) for i in range(int(L["END"] / step) + 1)] + [round(i * step + gap, 3) for i in range(int((L["END"] - gap) / step) + 1)]))
    times = [t for t in times if t <= L["END"] - 0.01]
    with Pool(8) as p:
        frames = dict(zip(times, p.map(frame_small, [(L, t) for t in times])))
    res = []
    for t in times:
        t2 = round(t + gap, 3)
        if t2 in frames:
            diff = (np.abs(frames[t] - frames[t2]) > 12).mean() * 100
            res.append((t, diff))
    low = [(t, round(d, 3)) for t, d in res if d < thr]
    return res, low, thr


_L = None


def _init(L):
    global _L
    _L = L
    anchor_windows(L)      # worker processes start fresh: they need the word-anchored edges too


def render_frame(i):
    """Render frame i (t = i / FPS) to _frames/, return its text log for the gate (strings drawn at alpha > 0.3)."""
    t = i / FPS
    cv = scene(_L, t)
    cv.im.save(HERE / "_frames" / f"{i:05d}.png", compress_level=1)
    return i, [(sx, size, a, round(x), round(y)) for sx, size, a, x, y in cv.log if a > 0.3]


def render_all(L, workers=8):
    from multiprocessing import Pool
    (HERE / "_frames").mkdir(exist_ok=True)
    (HERE / "_qc").mkdir(exist_ok=True)
    n = int(L["END"] * FPS)                       # 75.55 s -> 2266 frames; the video is n / FPS long
    log = {}
    with Pool(workers, initializer=_init, initargs=(L,)) as p:
        for k, (i, texts) in enumerate(p.imap(render_frame, range(n), chunksize=4)):
            log[i] = texts
            if k % 200 == 0:
                print(f"  frame {k}/{n}", flush=True)
    (HERE / "_qc" / "render_log.json").write_text(json.dumps({"fps": FPS, "frames": n, "log": log}))
    print(f"{n} frames rendered ({n / FPS:.3f} s)")


def encode():
    import subprocess
    (HERE / "_video").mkdir(exist_ok=True)
    out = HERE / "_video" / "short-silent.mp4"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(HERE / "_frames" / "%05d.png"),
           "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p", "-c:v", "libx264", "-crf", "16", "-preset", "medium",
           "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    print("encoded", out.name, round(out.stat().st_size / 1e6, 1), "MB")


if __name__ == "__main__":
    args = sys.argv[1:]
    L, src = line_starts()
    anchor_windows(L)
    if "--render" in args:
        print(f"clock: {src}; END {L['END']:.3f} s")
        render_all(L)
    if "--encode" in args:
        encode()
    if "--cues" in args:
        print(src, json.dumps({k: round(v, 2) for k, v in L.items()}))
    if "--stills" in args:
        print(f"clock: {src}")
        rep = make_stills(L, src)
        bad = [r for r in rep if not r[2]]
        print(f"{len(rep)} stills, {len(bad)} outside the safe area")
        if "--no-measure" not in args:
            res, low, thr = run_change_measure(L)
            print(f"change measure ({len(res)} pairs, 2.5 s apart, 540x960, % of pixels changed): "
                  f"min {min(d for _, d in res):.3f}%, median {sorted(d for _, d in res)[len(res)//2]:.3f}%")
            print("windows under", thr, "%:", low if low else "none")
            print("five lowest (t, %):", sorted([(round(t, 1), round(d, 2)) for t, d in res], key=lambda x: x[1])[:5])
