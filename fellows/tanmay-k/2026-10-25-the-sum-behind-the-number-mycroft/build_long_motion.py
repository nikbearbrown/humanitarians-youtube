#!/usr/bin/env python3
"""Week 28 WORK video, long film (16:9): every beat is a pure function of time t, tied to the Whisper word clock
(mp3/timings.json). Voice: Kokoro am_onyx (make_audio.py); audio is NOT regenerated here. The drawing helpers and data
come from build_long_stills (so the last frames equal the approved stills), parametrised by time.

A running total grows one named shock at a time: blocks land on 'fifteen', 'thirty-five', 'forty'; arithmetic types in
term by term; every element appears on the word it illustrates (never before it, within about 0.4 s after).

  --frame B04 12.3 out.png     one frame (full size; add LOWRES=1 in the environment for 960x540)
  --lowres                     all frames at 960x540 -> _frames_lowres/Bxx/ (the cheap checks run on these)
  --check                      timing vs word cues, collisions, text sizes, static stretches, on the low-res timeline
  --render                     all frames at 3840x2160 -> _frames/Bxx/
  --encode                     per-beat 4K mp4 with audio, the master, 720p previews
  --all                        render + encode
Cheap checks FIRST (--lowres then --check); one full-size render afterwards.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "topic-video"))
LOWRES = bool(os.environ.get("LOWRES"))
if LOWRES:                                   # cheap pass: drawn at scale 1 (1920x1080), saved at 960x540
    import c28_common
    c28_common.S = 1
    c28_common._fc.clear()
sys.path.insert(0, str(HERE))
import build_long_stills as bl                                    # noqa: E402
if LOWRES:
    bl.S = 1
from c28_common import BORDER, CARD, GHOST, INK, INK_SOFT, PAGE, SEND, SPARK, hex2rgb, mix  # noqa: E402
from PIL import Image                                             # noqa: E402

FPS = 30
TIM = json.loads((HERE / "mp3" / "timings.json").read_text())
ORDER = [f"B{i:02d}" for i in range(1, 12)]
FRAMES = HERE / ("_frames_lowres" if LOWRES else "_frames")
BEATS, PREVIEW, SILENT = HERE / "_beats", HERE / "_preview", HERE / "_silent"
MASTER = HERE / "the-sum-behind-the-number.mp4"
M, KIND, CAP = bl.M, bl.KIND, bl.CAP
TICK = bl.TICKER_LABEL


# ----------------------------------------------------------------------------- time helpers

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ramp(t, t0, d=0.35):
    return ease((t - t0) / d)


def lerp(a, b, p):
    return a + (b - a) * p


class A:
    """with A(cv, a): draw a group at that alpha (cv.alpha is restored)."""
    def __init__(self, cv, a):
        self.cv, self.a = cv, a

    def __enter__(self):
        self.old = self.cv.alpha
        self.cv.alpha = self.old * self.a
        return self.a > 0.004

    def __exit__(self, *x):
        self.cv.alpha = self.old


def states(t, cues, d=0.3):
    """alphas for N+1 sequential states switching at `cues`: state i fades out just before cue i, state i+1 fades in at it."""
    out = []
    for i in range(len(cues) + 1):
        a = 1.0 if i == 0 else ramp(t, cues[i - 1], d)
        if i < len(cues):
            a *= 1 - ramp(t, cues[i] - d, d)
        out.append(a)
    return out


def W(b, tok, nth=0):
    """start time (s) of the nth Whisper word of beat b whose letters/digits match tok (tolerant of punctuation)."""
    norm = lambda w: re.sub(r"[^a-z0-9.%$]", "", w.lower()).strip(".")
    hits = [w[1] for w in TIM[b]["words"] if norm(w[0]) == norm(tok)]
    assert len(hits) > nth, (b, tok, hits)
    return hits[nth]


def cue_set(cv, s, c):
    cv.cues[s] = min(cv.cues.get(s, c), c)


def bp(t, c):
    """(growth, text alpha) of a block whose word is at c: it grows in 0.25 s, its number fades in over the next 0.15 s."""
    return ramp(t, c, 0.25), ramp(t, c + 0.25, 0.15)


def tx(cv, x, y, s, kind="sans", size=28, fill=INK, anchor="ls", cue=None):
    """cv.text that registers the word cue it illustrates (the timing check reads cv.cues)."""
    if cue is not None:
        cue_set(cv, s, cue)
    cv.text(x, y, s, kind, size, fill=fill, anchor=anchor)


def ev(cv, s, a=1.0, cue=0.0):
    with A(cv, a):
        lines = bl.wrap(cv, s, "sans", CAP, bl.W - 2 * M)
        for i, ln in enumerate(lines):
            tx(cv, M, bl.SRC_BASE - 40 * (len(lines) - 1 - i), ln, "sans", CAP, INK_SOFT, cue=cue)


def head(cv, items, a=1.0):
    for s, al in items:
        with A(cv, al * a):
            cv.text(M, 130, s, "serifm", 64, fill=INK, anchor="ls")


def grow_bar(cv, x, y, h, blocks, scale, size, prog, cues=None):
    """blocks [(kind, pct)] drawn left to right; prog[i] = (growth, text alpha): the block grows, then its number fades in."""
    cx = x
    for i, (kind, p) in enumerate(blocks):
        g, ta = prog[i]
        if g <= 0.004:
            break
        w = abs(p) * scale * g
        col = KIND[kind]
        cv.rect(cx, y, cx + w, y + h, fill=col, outline=PAGE, width=3)
        if ta > 0.004:
            with A(cv, ta):
                tx(cv, cx + w / 2, y + h / 2 + size * 0.34, bl.num(p), "serifm", size, bl.text_on(col), "ms", cue=None if not cues else cues[i])
        cx += w
    return cx


# ----------------------------------------------------------------------------- the beats

C01 = bl.C01
EV_B = f"Evidence: stress-results.json · c01 · NVDA · the workflow's Load_Template_Scenario node · {TICK}"
EV_B3 = f"Evidence: stress-results.json · c01 · NVDA: shock_pct −90.0, loss −3,600.0 · the workflow's README (a vendored file) · {TICK}"


def b01(cv, t):
    w1 = W("B01", "minus")
    head(cv, [("Where does −78% come from?", ramp(t, W("B01", "where")))])
    with A(cv, ramp(t, 0.0)):
        tx(cv, 1010, 290, C01["scenario_name"], "sansm", 48, INK, cue=0.0)
    with A(cv, ramp(t, w1)):
        tx(cv, M, 440, "−78.0%", "serifm", 250, SEND, cue=w1)
    c10, c22 = W("B01", "$10"), W("B01", "2")
    with A(cv, ramp(t, c10)):
        tx(cv, 1010, 380, "$10,000", "sansm", 56, INK, cue=c10)
    with A(cv, ramp(t, c22)):
        tx(cv, 1010 + cv.tw("$10,000", "sansm", 56), 380, " → $2,200", "sansm", 56, INK, cue=c22)
    for i, tk in enumerate(("NVDA", "AMD", "TSM")):
        c = W("B01", "three") + 0.3 * i
        with A(cv, ramp(t, c)):
            bl.chip(cv, M + i * 290, 520, 260, 80, f"{tk} {int(bl.POS01[tk]['weight'] * 100)}%")
            cue_set(cv, f"{tk} {int(bl.POS01[tk]['weight'] * 100)}%", c)
    cm = W("B01", "78")
    with A(cv, ramp(t, cm)):
        tx(cv, M, 720, "made of: ?", "sansm", 44, INK_SOFT, cue=cm)
        bl.dashed_outline(cv, M, 750, 900, 110)
        cv.text(M + 450, 825, "?", "serifm", 72, fill=GHOST, anchor="ms")
    ev(cv, f"Evidence: stress-results.json · c01 (drawdown_pct {C01['drawdown_pct']}, initial 10,000, final 2,200) · {TICK}", ramp(t, 0.6), 0.6)


def b02(cv, t):
    head(cv, [("What this is", 1)])
    # the name line, then it clears before the quote card arrives
    nm = ramp(t, W("B02", "tanmay")) * (1 - ramp(t, W("B02", "this", 1) - 0.1, 0.3))
    with A(cv, nm):
        tx(cv, M, 270, "Tanmay Kulkarni · Humanitarians AI", "sansm", 44, INK, cue=W("B02", "tanmay"))
    cq = W("B02", "mycroft")
    with A(cv, ramp(t, cq)):
        cv.rect(M, 190, bl.W - M, 340, fill=CARD, outline=BORDER, width=2, r=14)
        tx(cv, M + 40, 290, "“Mycroft: both a book and a working agentic repository”", "serifi", 50, INK, cue=cq)
    cs = W("B02", "scenario")
    with A(cv, ramp(t, cs)):
        tx(cv, M, 400, "Scenario Stress Testing Agent", "sansm", 52, INK, cue=cs)
    cp = W("B02", "testing")
    with A(cv, ramp(t, cp)):
        bl.mono(cv, M, 450, "recipes/scenariostresstestingagent.md", 30, INK_SOFT)
    cl = W("B02", "shocks")
    with A(cv, ramp(t, cl)):
        tx(cv, M, 530, "the workflow's local steps", "sans", CAP, INK_SOFT, cue=cl)
    steps = [("validate the portfolio", cl), ("pick the scenario", W("B02", "named")), ("apply the shocks", W("B02", "reports"))]
    for i, (s, c) in enumerate(steps):
        x = M + i * 560
        with A(cv, ramp(t, c)):
            bl.chip(cv, x, 556, 470, 84, s, size=34)
            cue_set(cv, s, c)
            if i < 2:
                bl.arrow(cv, x + 480, 598, x + 548, 598)
    cpr = W("B02", "recipes")
    with A(cv, ramp(t, cpr)):
        bl.pill(cv, M, 700, 460, 80, "PR #74 · merged", outline=SPARK, fg=SEND, size=40)
        cue_set(cv, "PR #74 · merged", cpr)
    cd = W("B02", "portfolios")
    with A(cv, ramp(t, cd)):
        cv.rect(M, 810, bl.W - M, 900, fill=CARD, outline=BORDER, width=2, r=12)
    xs = M + 36
    for seg_, c_ in (("Invented portfolios", cd), (" · tickers from the workflow's own map", W("B02", "tickers")), (" · not investment advice", W("B02", "not", 1))):
        with A(cv, ramp(t, c_)):
            tx(cv, xs, 868, seg_, "sansm", 34, INK, cue=c_)
        xs += cv.tw(seg_, "sansm", 34)
    ev(cv, "Evidence: the repository README · recipes/scenariostresstestingagent.md · PR #74, merged 2026-10-26 (merge commit 5d60312)", ramp(t, 0.6), 0.6)


def b03(cv, t):
    cg = W("B03", "hold")
    hs = states(t, [cg])
    head(cv, [("A scenario is a list", hs[0]), ("Hold a guess", hs[1])])
    dim = 1 - 0.65 * ramp(t, cg)
    sh = TECH_ROWS
    cues = [W("B03", "market"), W("B03", "technology"), W("B03", "semiconductors"), W("B03", "ai"), W("B03", "fifth")]
    with A(cv, dim * ramp(t, 0.2)):
        cv.rect(M, 190, 1000, 740, fill=CARD, outline=BORDER, width=2, r=14)
    with A(cv, dim * ramp(t, W("B03", "tech"))):
        tx(cv, M + 36, 256, bl.TECH["name"], "sansm", 40, INK, cue=W("B03", "tech"))
    y = 330
    for (kind, label, v), c in zip(sh, cues[:4]):
        with A(cv, dim * ramp(t, c)):
            cv.rect(M + 36, y - 30, M + 76, y + 10, fill=KIND[kind])
            tx(cv, M + 100, y, label, "sansm", 40, INK, cue=c)
            tx(cv, 940, y, bl.pct(v * 100), "serifm", 52, INK, "rs", cue=c)
        y += 92
    with A(cv, dim * ramp(t, cues[4])):
        cv.rect(M + 36, y - 30, M + 76, y + 10, fill=GHOST)
        tx(cv, M + 100, y, "volatility number", "sansm", 40, INK, cue=cues[4])
        tx(cv, 940, y, f"{bl.TECH['shocks']['volatility_spike']:g}", "serifm", 52, INK, "rs", cue=cues[4])
    cr = W("B03", "engine's")
    rule = ramp(t, cr) * (1 - ramp(t, cg - 0.4, 0.3))
    with A(cv, rule):
        for i, ln in enumerate(bl.wrap(cv, "The engine's rule: for each holding, add up the shocks that belong to it.", "serifi", 48, 640)):
            tx(cv, 1110, 300 + i * 66, ln, "serifi", 48, INK, cue=cr)
    cs_ = W("B03", "shortlist")
    with A(cv, ramp(t, cs_) * (1 - ramp(t, cg - 0.4, 0.3))):
        tx(cv, M, 800, "the workflow's own template", "sans", CAP, INK_SOFT, cue=cs_)
    cq = cg + 0.7
    with A(cv, ramp(t, cq)):
        cv.rect(1060, 190, bl.W - M, 450, fill=CARD, outline=SPARK, width=3, r=14)
        for i, ln in enumerate(bl.wrap(cv, "market −15% → the biggest holding falls how far?", "serifm", 54, 680)):
            tx(cv, 1100, 270 + i * 70, ln, "serifm", 54, INK, cue=cq)
    cb = W("B03", "how")
    with A(cv, ramp(t, cb)):
        tx(cv, 1060, 540, "NVDA", "sansm", 34, INK_SOFT, cue=cb)
        bl.dashed_outline(cv, 1060, 560, 700, 100)
        cv.text(1060 + 350, 630, "?", "serifm", 72, fill=GHOST, anchor="ms")
    e = states(t, [cg])
    ev(cv, "Evidence: the workflow's Load_Template_Scenario node (tech_crash), as committed in the merged workflow file", e[0])
    ev(cv, "Evidence: the workflow's Load_Template_Scenario node (tech_crash) · " + TICK, e[1], cg)


TECH_ROWS = bl.SHOCK_ROWS


def b04(cv, t):
    cu = [W("B04", "15"), W("B04", "35"), W("B04", "40")]
    hs = states(t, [cu[1], cu[2]])
    head(cv, [("One holding, one block", hs[0]), ("A second block lands", hs[1]), ("The blocks add up", hs[2])])
    cl = W("B04", "holding")
    with A(cv, ramp(t, cl)):
        tx(cv, M, 250, "NVDA · the biggest holding", "sansm", 40, INK_SOFT, cue=cl)
        bl.dashed_outline(cv, M, 290, 900, 140, fill=GHOST, width=2)
    blocks = [("market", -15), ("semiconductors", -35), ("AI list", -40)]
    grow_bar(cv, M, 290, 140, blocks, 10, 64, [bp(t, c) for c in cu], cues=cu)
    caps = ["market −15: every holding belongs to it", "semiconductors −35: its sector", "AI stocks −40: it is on the AI list"]
    for j, c in enumerate(cu):
        with A(cv, ramp(t, c + 0.15)):
            y = 520 + j * 72
            cv.rect(M, y - 30, M + 40, y + 8, fill=KIND[blocks[j][0]])
            tx(cv, M + 64, y, caps[j], "sans", 38, INK, cue=c + 0.15)
    cc = W("B04", "everything")
    with A(cv, ramp(t, cu[0])):
        tx(cv, 1090, 290, "running total", "sans", CAP, INK_SOFT, cue=cu[0])
    c90 = W("B04", "90")
    ts = states(t, [cu[1], cu[2], c90])
    for i, (s, col, c) in enumerate((("−15", INK, cu[0]), ("−50", INK, cu[1]), ("−90", INK, cu[2]), ("−90", SEND, c90))):
        al = ts[i] if i else ts[0] * ramp(t, cu[0])
        if i == 3:
            al = ts[3]
        with A(cv, al):
            tx(cv, 1090, 450, s, "serifm", 190, col, cue=c)
    cr = W("B04", "readme")
    with A(cv, ramp(t, cr)):
        bl.pill(cv, 1090, 520, 420, 60, "README worked example", outline=SPARK, fg=SEND, size=30)
        cue_set(cv, "README worked example", cr)
        cv.rect(1090, 600, 1090 + 715, 600 + 270, fill=CARD, outline=BORDER, width=2, r=12)
    m = re.search(r"Market shock:\s+(-\d+%)\s+Semiconductor:\s+(-\d+%)\s+AI stocks:\s+(-\d+%)\s+.*?Total impact:\s+(-\d+%)", bl.README_TXT, re.S)
    rows = [("Market shock:", m.group(1)), ("Semiconductor:", m.group(2)), ("AI stocks:", m.group(3)), ("Total impact:", m.group(4))]
    rc = [cr + 0.5, cr + 0.9, cr + 1.3, W("B04", "example")]
    for i, ((a, b), c) in enumerate(zip(rows, rc)):
        yy = 600 + 62 + i * 58
        with A(cv, ramp(t, c)):
            if i == 3:
                cv.line([(1090 + 30, yy - 44), (1090 + 715 - 30, yy - 44)], fill=BORDER, width=2)
            bl.mono(cv, 1090 + 30, yy, a, 30, INK)
            cue_set(cv, a, c)
            bl.mono(cv, 1090 + 715 - 30 - 30 * 0.6 * len(b), yy, b, 30, SEND if i == 3 else INK)
    ca = W("B04", "names")
    with A(cv, ramp(t, ca)):
        tx(cv, M, 780, "another way to combine them is named in the README", "sans", 34, INK_SOFT, cue=ca)
    e = states(t, [cr])
    ev(cv, EV_B, e[0])
    ev(cv, EV_B3, e[1], cr)


def rowspec_b05(p):
    """layout a (p=0) to layout b (p=1): y, bar height, number size, legend y."""
    return lambda r: (lerp(230 + r * 160, 500 + r * 100, p), lerp(110, 74, p), lerp(52, 40, p))


def b05(cv, t):
    cm = W("B05", "number")
    p = ease((t - (cm - 0.1)) / 0.5)                 # the bars move to the second layout as the number returns
    hs = states(t, [cm + 0.1])
    head(cv, [("Same crash, different sums", hs[0]), ("The number, taken apart", hs[1])])
    nv = [("market", -15), ("semiconductors", -35), ("AI list", -40)]
    ts_ = [("market", -15), ("semiconductors", -35)]
    cuT = [W("B05", "15"), W("B05", "35")]
    cuA = W("B05", "90", 1)
    c_nv, c_amd = W("B05", "first"), W("B05", "90", 1)
    rows = [("NVDA", 40, nv, [c_nv, c_nv + 0.12, c_nv + 0.24]), ("AMD", 30, nv, [c_amd, c_amd + 0.12, c_amd + 0.24]), ("TSM", 30, ts_, cuT)]
    spec = rowspec_b05(p)
    sh = [W("B05", "40"), W("B05", "30", 0), W("B05", "30", 1)]
    for r, (name, share, blocks, cues) in enumerate(rows):
        y, h, size = spec(r)
        tw_all = sum(abs(v) for _, v in blocks) * 8
        lc = {0: c_nv, 1: W("B05", "second"), 2: W("B05", "third")}[r]
        fs = 36 if p < 0.5 else 34
        with A(cv, ramp(t, lc)):
            tx(cv, M, y + h / 2 + 12, name, "sansm", fs, INK, cue=lc)
        with A(cv, ramp(t, sh[r])):
            tx(cv, M + cv.tw(name + " ", "sansm", fs), y + h / 2 + 12, f"{share}%", "sansm", fs, INK, cue=sh[r])
        grow_bar(cv, 360, y, h, blocks, 8, int(round(size)), [bp(t, c) for c in cues], cues=cues)
        totv = sum(v for _, v in blocks)
        ct = cues[-1] + 0.45
        with A(cv, ramp(t, ct) * (1 - p)):
            tx(cv, 360 + tw_all + 30, y + 74, f"{bl.num(totv)}", "serifm", 56, SEND if r == 2 else INK, cue=ct)
    leg = ramp(t, cuT[0])
    with A(cv, leg):
        bl.legend(cv, M, lerp(800, 850, p), ["market", "semiconductors", "AI list"])
        cue_set(cv, "market", cuT[0])
    # the sum, term by term (right column), fading out as the number returns
    col = 1 - ramp(t, cm - 0.15, 0.3)
    for i, ((w_, pp, res), c) in enumerate(zip((("0.40", 90, 36), ("0.30", 90, 27), ("0.30", 50, 15)), (W("B05", "36"), W("B05", "27"), W("B05", "15", 1)))):
        with A(cv, ramp(t, c) * col):
            tx(cv, 1250, 320 + i * 96, f"{w_} × {pp} = {res}", "serifm", 60, INK, cue=c)
    c78 = W("B05", "78")
    with A(cv, ramp(t, c78) * col):
        cv.line([(1250, 590), (1805, 590)], fill=INK_SOFT, width=3)
        tx(cv, 1250, 680, "total 78", "serifm", 80, SEND, cue=c78)
    cn = W("B05", "50")
    with A(cv, ramp(t, cn + 0.5) * col):
        for k, ln in enumerate(bl.wrap(cv, "NVDA and AMD are on the AI list; TSM is not, so it takes −50.", "sans", CAP, 560)):
            tx(cv, 1250, 750 + k * 38, ln, "sans", CAP, INK_SOFT, cue=cn + 0.5)
    # the number returns, with its parts under it
    cb = cm + 0.35
    with A(cv, ramp(t, cb)):
        tx(cv, M, 400, "−78.0%", "serifm", 220, SEND, cue=cb)
        tx(cv, 1010, 300, C01["scenario_name"], "sansm", 44, INK, cue=cb)
        tx(cv, 1010, 380, "36 + 27 + 15 = 78", "serifm", 60, INK, cue=cb)
    e = states(t, [cm + 0.1])
    ev(cv, f"Evidence: stress-results.json · c01 · all_positions: −90, −90, −50 · {TICK}", e[0])
    ev(cv, f"Evidence: stress-results.json · c01 · drawdown_pct {C01['drawdown_pct']} · {TICK}", e[1], cm + 0.1)


def b06(cv, t):
    head(cv, [("A milder scenario, the same rule", 1)])
    sh = bl.RATE["shocks"]
    segs = [("Aggressive Rate Hike:", W("B06", "aggressive")), (f" market {bl.pct(sh['market'] * 100)}", W("B06", "10")),
            (f" · growth stocks {bl.pct(sh['growth_stocks'] * 100)}", W("B06", "20")), (f" · technology sector {bl.pct(sh['tech_sector'] * 100)}", W("B06", "15"))]
    x = M
    for s, c in segs:
        with A(cv, ramp(t, c)):
            tx(cv, x, 205, s, "sans", 34, INK_SOFT, cue=c)
        x += cv.tw(s, "sans", 34)
    items = []
    for p_ in bl.C12["all_positions"]:
        b = [("market", sh["market"] * 100)]
        if p_["ticker"] == "TSLA":
            b += [("technology", sh["tech_sector"] * 100)]
        b += [("growth", sh["growth_stocks"] * 100)]
        items.append((p_["ticker"], int(p_["weight"] * 100), b))
    c_rows = W("B06", "four")
    c30 = W("B06", "30", 0)
    cT = W("B06", "block")
    c45 = W("B06", "45")
    for r, (tk, share, blocks) in enumerate(items):
        y = 260 + r * 120
        c = c_rows + 0.3 * r
        with A(cv, ramp(t, c)):
            tx(cv, M, y + 58, f"{tk} {share}%", "sansm", 34, INK, cue=c)
        if tk == "TSLA":
            seq = [(blocks[0], c), (blocks[1], cT), (blocks[2], c + 0.15)]
        else:
            seq = [(blocks[0], c), (blocks[1], c + 0.15)]
        cx = 360
        for (kind, v), ck in seq:
            g, ta = bp(t, ck)
            wpx = abs(v) * 10 * g
            if wpx < 0.5:
                continue
            col = KIND[kind]
            cv.rect(cx, y, cx + wpx, y + 88, fill=col, outline=PAGE, width=3)
            if ta > 0.004:
                with A(cv, ta):
                    tx(cv, cx + wpx / 2, y + 88 / 2 + 44 * 0.34, bl.num(v), "serifm", 44, bl.text_on(col), "ms", cue=ck)
            if tk == "TSLA" and kind == "technology":
                with A(cv, g * ramp(t, cT + 0.25, 0.15) * (1 - ramp(t, c45 + 1.5, 0.4))):
                    cv.rect(cx - 3, y - 3, cx + wpx + 3, y + 88 + 3, outline=INK, width=4)
            cx += wpx
        if tk == "TSLA":
            with A(cv, ramp(t, c45)):
                tx(cv, 360 + 450 + 30, y + 58, "−45", "serifm", 52, SEND, cue=c45)
        else:
            with A(cv, ramp(t, c30 + 0.1 * r)):
                tx(cv, 360 + 300 + 30, y + 58, "−30", "serifm", 52, INK, cue=c30 + 0.1 * r)
    with A(cv, ramp(t, c_rows)):
        bl.legend(cv, M, 780, ["market", "technology", "growth"])
        cue_set(cv, "market", c_rows)
    cn = W("B06", "33")
    with A(cv, ramp(t, cn)):
        tx(cv, 1280, 360, f"{abs(bl.C12['drawdown_pct']):g}%", "serifm", 190, SEND, cue=cn)
    cc = W("B06", "critical")
    with A(cv, ramp(t, cc)):
        bl.pill(cv, 1280, 400, 360, 70, bl.C12["risk_level"].lower(), outline=SPARK, fg=SEND, size=40)
        cue_set(cv, "critical", cc)
    ca = W("B06", "above")
    with A(cv, ramp(t, ca)):
        tx(cv, 1280, 520, "above 30%: critical", "sans", CAP + 2, INK_SOFT, cue=ca)
        tx(cv, 1280, 566, "the workflow's label", "sans", CAP, INK_SOFT, cue=ca)
    ev(cv, f"Evidence: stress-results.json · c12 · all_positions −45, −30, −30, −30 · drawdown_pct {bl.C12['drawdown_pct']} · risk_level {bl.C12['risk_level']} · {TICK}",
       ramp(t, 0.6), 0.6)


def b07(cv, t):
    cB = W("B07", "12")
    hs = states(t, [cB - 0.15])
    head(cv, [("Run beside the original", hs[0]), ("Twelve deliberate breaks", hs[1])])
    fields = [("total loss", "−7,800"), ("drawdown", f"{bl.num(C01['drawdown_pct'])}.0%"),
              ("final value", f"{int(C01['final_portfolio_value']):,}"), ("risk level", C01["risk_level"].lower())]
    c_orig, c_copy = W("B07", "original"), W("B07", "second")
    for k, (title, c) in enumerate((("original code", c_orig), ("my copy", c_copy))):
        x = M + k * 440
        with A(cv, ramp(t, c)):
            cv.rect(x, 190, x + 415, 560, fill=CARD, outline=BORDER, width=2, r=14)
            tx(cv, x + 24, 250, title, "sansm", 40, INK, cue=c)
        for r, (lab, val) in enumerate(fields):
            cr = W("B07", "ran") + 0.4 * r
            with A(cv, ramp(t, cr)):
                tx(cv, x + 24, 330 + r * 70, lab, "sans", CAP, INK_SOFT, cue=cr)
                tx(cv, x + 391, 330 + r * 70, val, "sansm", 34, INK, "rs", cue=cr)
    cw = W("B07", "straight")
    with A(cv, ramp(t, cw)):
        tx(cv, M, 616, "the original code is run straight from the workflow file", "sans", CAP, INK_SOFT, cue=cw)
    c24, cm = W("B07", "24"), W("B07", "matched")
    k = int(round(24 * clamp((t - c24) / (cm - c24 + 0.0))))
    with A(cv, ramp(t, c24)):
        tx(cv, M, 730, f"{k} of {bl.PARITY['requests']}", "serifm", 110, SEND)
    with A(cv, ramp(t, cm)):
        tx(cv, M + 470, 730, "identical", "sansm", 48, INK, cue=cm)
    ce = W("B07", "every", 0)
    with A(cv, ramp(t, ce)):
        tx(cv, M, 780, "every number, every label, every message", "sans", CAP, INK_SOFT, cue=ce)
    rows = bl.self_rows()
    cbk = W("B07", "12") + 0.1
    for i, r in enumerate(rows):
        y = 230 + i * 56
        c = cbk + i * 0.19
        with A(cv, ramp(t, c, 0.2)):
            cv.rect(1010, y - 36, 1805, y + 10, fill=CARD, outline=BORDER, width=2, r=10)
            tx(cv, 1030, y, f"BREAK: {r}", "sans", CAP, INK, cue=c)
        with A(cv, ramp(t, c + 0.15, 0.2)):
            tx(cv, 1785, y, "caught", "sansm", CAP, SEND, "rs", cue=c + 0.15)
    cs = W("B07", "caught")
    with A(cv, ramp(t, cs)):
        tx(cv, M, 850, "27 of 27 checks as expected", "serifm", 44, INK, cue=cs)
        tx(cv, M, 908, "12 of 12 deliberate breaks caught", "serifm", 44, INK, cue=cs)
    ev(cv, f"Evidence: parity-results.json · requests {bl.PARITY['requests']}, matching {bl.PARITY['matching']}, mismatching {bl.PARITY['mismatching']} · self-test-results.md · checks 27/27 · deliberate breaks caught 12/12", ramp(t, 0.6), 0.6)


def b08(cv, t):
    cs = W("B08", "ticker") - 0.25
    hs = states(t, [cs])
    head(cv, [("The checks keep the sum honest", hs[0]), ("Each stop carries its reason", hs[1])])
    for i, (ph_, c_) in enumerate((("reads each portfolio", W("B08", "reads")), ("with the workflow's own rules", W("B08", "own")),
                                   ("and one addition of mine", W("B08", "one", 0)), ("and it protects the sum", W("B08", "protects")))):
        with A(cv, ramp(t, c_) * (1 - ramp(t, W("B08", "six") - 0.45, 0.3))):
            tx(cv, M, 270 + i * 64, ph_, "sans", 34, INK, cue=c_)
    cg = W("B08", "validator")
    with A(cv, ramp(t, cg) * hs[0]):
        cv.rect(840, 190, 1000, 760, fill=mix(PAGE, SPARK, 0.12), outline=SPARK, width=3, r=10)
        tx(cv, 920, 740, "validator", "sansm", CAP, SEND, "ms", cue=cg)
    cu = [(W("B08", "six"), W("B08", "accepted"), W("B08", "to")), (W("B08", "1"), W("B08", "rescales"), W("B08", "one", 1))]
    for i, (fix, wts) in enumerate((("c06", bl.W06), ("c08", bl.W08))):
        y = 220 + i * 240
        tot = round(sum(w for _, w in wts), 3)
        c1, c2, c3 = cu[i]
        with A(cv, ramp(t, c1) * hs[0]):
            cv.rect(M, y, 560, y + 190, fill=CARD, outline=BORDER, width=2, r=12)
            tx(cv, M + 30, y + 50, fix, "sansm", 34, INK_SOFT, cue=c1)
            tx(cv, M + 30, y + 120, "weights total", "sans", CAP, INK_SOFT, cue=c1)
            tx(cv, 530, y + 130, f"{tot:g}", "serifm", 80, INK, "rs", cue=c1)
        with A(cv, ramp(t, c1 + 0.2) * hs[0]):
            bl.arrow(cv, 580, y + 95, 830, y + 95)
        with A(cv, ramp(t, c2) * hs[0]):
            bl.arrow(cv, 1010, y + 95, 1160, y + 95)
            cv.rect(1180, y, 1805, y + 190, fill=CARD, outline=BORDER, width=2, r=12)
            tx(cv, 1210, y + 56, "accepted · rescaled to", "sans", CAP + 2, INK_SOFT, cue=c2)
        with A(cv, ramp(t, c3) * hs[0]):
            tx(cv, 1210, y + 150, "1.0", "serifm", 80, SEND, cue=c3)
    c12_ = W("B08", "one", 1) if False else cu[1][2]
    with A(cv, ramp(t, c12_) * hs[0]):
        tx(cv, M, 740, "12 of 12 clean portfolios accepted", "sansm", 40, INK, cue=c12_)
    cd = [W("B08", "no", 0), W("B08", "share"), W("B08", "empty")]
    for i, key in enumerate(("d03", "d05", "d09")):
        y = 220 + i * 150
        with A(cv, ramp(t, cd[i]) * hs[1]):
            cv.rect(M, y, 560, y + 112, fill=CARD, outline=BORDER, width=2, r=12)
            tx(cv, M + 30, y + 66, key, "sansm", 40, INK_SOFT, cue=cd[i])
            cv.rect(700, y - 10, 760, y + 122, fill=INK_SOFT)
            cv.rect(715, y + 36, 727, y + 76, fill="#FFFFFF")
            cv.rect(733, y + 36, 745, y + 76, fill="#FFFFFF")
            cv.rect(850, y, bl.W - M, y + 112, fill=CARD, outline=BORDER, width=2, r=12)
            reason = bl.short_reason(key)
            reason = reason[0].upper() + reason[1:]
            lines = bl.wrap(cv, reason, "sansm", 34, 880)[:2]
            for k, ln in enumerate(lines):
                tx(cv, 880, y + (68 if len(lines) == 1 else 42) + k * 50, ln, "sansm", 34, INK, cue=cd[i])
    ct = W("B08", "ten")
    with A(cv, ramp(t, ct) * hs[1]):
        tx(cv, M, 740, "10 of 10 stopped, each for its own reason", "sansm", 40, INK, cue=ct)
    cn = W("B08", "sum", 1)
    with A(cv, ramp(t, cn) * hs[1]):
        tx(cv, M, 800, "a sum of nothing never reaches the screen", "serifi", 48, INK_SOFT, cue=cn)
    ev(cv, "Evidence: validate-audit.md (clean: requests in 12, accepted 12) · c06 and c08 · Invented", hs[0])
    ev(cv, "Evidence: validate-audit.md (defective: requests in 10, rejected 10, each with its reason) · Invented", hs[1], cs)


def b09(cv, t):
    cq = W("B09", "five") - 0.1
    hs = states(t, [W("B09", "that") - 0.05])
    head(cv, [("Staying in the sample", hs[0]), ("A good list for next time", hs[1])])
    hand = bl.RUNLOG["handoffs_not_made"]
    names = {"Fetch_Data": "market-data request", "Basic LLM Chain / Groq Chat Model": "call to a model", "Respond to Webhook": "reply to a caller"}
    cw = W("B09", "written")
    with A(cv, ramp(t, cw)):
        tx(cv, M, 220, "written down as hand-offs, not approved", "sansm", 36, INK_SOFT, cue=cw)
    rowcue = {"Fetch_Data": W("B09", "market"), "Basic LLM Chain / Groq Chat Model": W("B09", "call"), "Respond to Webhook": W("B09", "reply")}
    for i, h in enumerate(hand):
        y = 250 + i * 128
        c = rowcue[h["node"]]
        with A(cv, ramp(t, c)):
            cv.rect(M, y, 960, y + 104, fill=CARD, outline=BORDER, width=2, r=12)
            tx(cv, M + 28, y + 46, names[h["node"]], "sansm", 36, INK, cue=c)
            bl.mono(cv, M + 28, y + 86, f"approved_for_live_action: {str(h['approved_for_live_action']).lower()}", 28, SEND)
            cue_set(cv, f"approved_for_live_action: {str(h['approved_for_live_action']).lower()}", c)
    cc = W("B09", "five")
    with A(cv, ramp(t, cc)):
        cv.rect(1040, 250, bl.W - M, 460, fill=CARD, outline=BORDER, width=2, r=12)
        tx(cv, 1040, 520, "open items", "sansm", 36, INK_SOFT, cue=cc)
    fm = re.match(r"---\n(.*?)\n---", bl.RECIPE, re.S).group(1).splitlines()
    keep = [ln for ln in fm if ln.split(":")[0] in ("status", "todos_open", "recipe_version")]
    for i, ln in enumerate(keep):
        c = cc + 0.4 + 0.4 * i
        with A(cv, ramp(t, c)):
            bl.mono(cv, 1070, 320 + i * 56, ln, 32, INK)
            cue_set(cv, ln, c)
    items = ["step 2 · ingest declared inputs", "step 4 · transform and quality check", "step 6 · produce human report",
             "map · respond to webhook", "map · human report script"]
    for i, s in enumerate(items):
        c = cc + 0.5 + 0.35 * i
        with A(cv, ramp(t, c)):
            y = 570 + i * 56
            cv.rect(1040, y - 28, 1070, y + 2, outline=INK_SOFT, width=3, r=4)
            tx(cv, 1092, y, s, "sans", 30, INK, cue=c)
    cn = W("B09", "nothing")
    with A(cv, ramp(t, cn)):
        tx(cv, M, 750, "nothing here calls the outside world", "serifi", 52, INK, cue=cn)
    cd = W("B09", "draft")
    with A(cv, ramp(t, cd)):
        tx(cv, M, 820, "5 items open · draft, on purpose", "sansm", 40, INK_SOFT, cue=cd)
    ev(cv, "Evidence: the step-5 run log (handoffs_not_made, approved_for_live_action false) · the recipe frontmatter (status DRAFT, todos_open 5)", 1.0)


def b10(cv, t):
    ca = W("B10", "ask")
    with A(cv, 1.0):
        tx(cv, 1150, 400, "−78.0%", "serifm", 190, mix(PAGE, SEND, 0.22), cue=None)
        a0 = cv.alpha
        cv.alpha = 0.3
        for r, blocks in enumerate([[("market", -15), ("semiconductors", -35), ("AI list", -40)]] * 2 + [[("market", -15), ("semiconductors", -35)]]):
            bl.bar(cv, 1150, 470 + r * 90, 64, blocks, 6.5, size=34)
        cv.alpha = a0
    with A(cv, ramp(t, ca)):
        cv.text(M, 130, "Ask what was added", "serifm", 64, fill=INK, anchor="ls")
        cue_set(cv, "Ask what was added", ca)
    qs = [("Which shocks?", W("B10", "which", 0)), ("From which lists?", W("B10", "from")), ("Has anyone run the adder beside the original?", W("B10", "has"))]
    y = 250
    for q, c in qs:
        for ln in bl.wrap(cv, q, "serifm", 60, 900):
            with A(cv, ramp(t, c)):
                tx(cv, M, y, ln, "serifm", 60, INK, cue=c)
            y += 76
        y += 24
    cg = W("B10", "a", 1)
    with A(cv, ramp(t, cg)):
        tx(cv, M, y + 40, "A good answer names the terms.", "serifi", 72, SEND, cue=cg)
    ev(cv, f"Evidence: the number is stress-results.json · c01 · drawdown_pct {C01['drawdown_pct']} · {TICK}", 1.0)


def b11(cv, t):
    c1 = W("B11", "tanmay")
    with A(cv, ramp(t, c1)):
        tx(cv, M, 440, "Tanmay Kulkarni · @HumanitariansAI", "sans", 48, INK_SOFT, cue=c1)
        cv.line([(M, 500), (900, 500)], fill=BORDER, width=3)
    c2 = W("B11", "humanitarians")
    with A(cv, ramp(t, c2)):
        tx(cv, M, 360, "Humanitarians AI", "serifm", 104, INK, cue=c2)
    c3 = W("B11", "contribution")
    with A(cv, ramp(t, c3)):
        tx(cv, M, 590, "github.com/nikbearbrown/mycroft · PR #74", "sansm", 44, INK, cue=c3)
    c4 = W("B11", "mycroft")
    with A(cv, ramp(t, c4)):
        bl.mono(cv, M, 650, "recipes/scenariostresstestingagent.md", 34, INK_SOFT)
        cue_set(cv, "recipes/scenariostresstestingagent.md", c4)
    for i, blocks in enumerate([[("market", -15), ("semiconductors", -35), ("AI list", -40)]] * 2 + [[("market", -15), ("semiconductors", -35)]]):
        c = c3 + 0.3 * i
        with A(cv, ramp(t, c)):
            bl.bar(cv, 1130, 300 + i * 110, 90, blocks, 7, size=44)
    ev(cv, f"Evidence: PR #74 merged 2026-10-26 (merge commit 5d60312) · {TICK}", 1.0)


FUNCS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06, "B07": b07, "B08": b08, "B09": b09, "B10": b10, "B11": b11}


def duration(b):
    return TIM[b]["duration_s"]


def nframes(b):
    return int(round(duration(b) * FPS))


def new_canvas():
    cv = bl.new()
    cv.cues = {}
    return cv


def frame(b, t, return_canvas=False):
    cv = new_canvas()
    FUNCS[b](cv, t)
    im = cv.im
    fade = 1.0
    if b == "B01":
        fade = clamp(t / 0.5)                                  # the film's first frame eases up from the cream page
    if b == "B11":
        fade = 1.0 - clamp((t - (duration(b) - 0.8)) / 0.8)    # the last frame eases back to cream over 0.8 s
    if fade < 0.999:
        base = Image.new("RGB", im.size, hex2rgb(PAGE))
        im = Image.blend(base, im, fade)
    return (im, cv) if return_canvas else im


# ----------------------------------------------------------------------------- render / check / encode

def _job(args):
    b, i = args
    out = FRAMES / b / f"{i:05d}.png"
    if out.exists():
        return
    im = frame(b, i / FPS)
    if LOWRES:
        im = im.resize((960, 540), Image.LANCZOS)
    im.save(out, compress_level=1)


def render(only=None, workers=3):
    jobs = []
    for b in ORDER:
        if only and b not in only:
            continue
        (FRAMES / b).mkdir(parents=True, exist_ok=True)
        jobs += [(b, i) for i in range(nframes(b))]
    print(f"rendering {len(jobs)} frames ({'960x540' if LOWRES else '3840x2160'}) with {workers} workers", flush=True)
    with Pool(workers) as p:
        for k, _ in enumerate(p.imap_unordered(_job, jobs, chunksize=6)):
            if k % 500 == 0:
                print(f"  {k}/{len(jobs)}", flush=True)


def _scan(b):
    """per-beat timeline scan: cue timing, collisions, text sizes (runs in a worker)."""
    first_any, first_full, hard, small, tight_all = {}, {}, set(), set(), set()
    for i in range(nframes(b)):
        t = i / FPS
        cv = new_canvas()
        FUNCS[b](cv, t)
        for (s, size, alpha, x, y) in cv.log:
            first_any.setdefault(s, t) if alpha >= 0.02 else None
            if alpha >= 0.9:
                first_full.setdefault(s, t)
            if size < CAP and bl.W and s.strip() and not s.startswith("−") and size < 28:
                small.add((s, size))
        h, tight = bl.collisions(cv)
        for x in h:
            hard.add((round(t, 1), x))
        for x in tight:
            tight_all.add(x)
    return b, first_any, first_full, hard, small, dict(cv.cues), tight_all


def check():
    out = []
    with Pool(3) as p:
        res = p.map(_scan, ORDER)
    bad = 0
    for b, fa, ff, hard, small, cues, tight in res:
        early, late = [], []
        for s, c in cues.items():
            if s in fa and fa[s] < c - 1.5 / FPS:
                early.append((s, round(fa[s], 2), round(c, 2)))
            if s in ff and ff[s] > c + 0.45:
                late.append((s, round(ff[s], 2), round(c, 2)))
            if s not in fa:
                late.append((s, "never", round(c, 2)))
        print(f"{b}: cues {len(cues)} · early {len(early)} · late {len(late)} · collisions {len(hard)} · small type {len(small)} · tight gaps {len(tight)}")
        for tg in sorted(tight)[:5]:
            print("   TIGHT", tg)
        for e in early[:6]:
            print("   EARLY", e)
        for e in late[:6]:
            print("   LATE", e)
        for h in sorted(hard)[:6]:
            print("   COLLISION", h)
        for s_ in sorted(small)[:4]:
            print("   SMALL", s_)
        bad += len(early) + len(late) + len(hard) + len(small)
    print("total problems:", bad)
    return bad


def sh(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"FAILED: {' '.join(map(str, cmd))}\n{r.stderr[-1500:]}")
    return r


def encode():
    BEATS.mkdir(exist_ok=True)
    PREVIEW.mkdir(exist_ok=True)
    SILENT.mkdir(exist_ok=True)
    for b in ORDER:
        n = nframes(b)
        if "--reuse" in sys.argv and (SILENT / f"{b}.mp4").exists():
            continue
        sh(["ffmpeg", "-y", "-loglevel", "error", "-framerate", FPS, "-i", FRAMES / b / "%05d.png", "-frames:v", n, "-c:v", "libx264",
            "-crf", 16, "-preset", "medium", "-pix_fmt", "yuv420p", "-g", 30, "-movflags", "+faststart", SILENT / f"{b}.mp4"])
        print("encoded", b, n, "frames", flush=True)
    lst = SILENT / "list.txt"
    lst.write_text("".join(f"file '{SILENT / (b + '.mp4')}'\n" for b in ORDER))
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", 0, "-i", lst, "-c", "copy", SILENT / "master_video.mp4"])
    parts = []
    for b in ORDER:
        d = nframes(b) / FPS
        p = SILENT / f"{b}.wav"
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", HERE / "mp3" / f"beat-{b}.wav", "-af", "apad", "-t", f"{d:.6f}", "-ar", 48000, "-ac", 1, p])
        parts.append(p)
    (SILENT / "alist.txt").write_text("".join(f"file '{p}'\n" for p in parts))
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", 0, "-i", SILENT / "alist.txt", "-c", "copy", SILENT / "master_raw.wav"])
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(SILENT / "master_raw.wav"), "-af", "loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    js = json.loads(r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1])
    af = (f"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={js['input_i']}:measured_LRA={js['input_lra']}:measured_TP={js['input_tp']}"
          f":measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", SILENT / "master_raw.wav", "-af", af, "-ar", 48000, "-ac", 1, SILENT / "master_norm.wav"])
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", SILENT / "master_video.mp4", "-i", SILENT / "master_norm.wav", "-c:v", "copy", "-c:a", "aac",
        "-b:a", "192k", "-ar", 48000, "-ac", 1, "-shortest", "-movflags", "+faststart", MASTER])
    t0 = 0.0
    for b in ORDER:
        d = nframes(b) / FPS
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", SILENT / f"{b}.mp4", "-ss", f"{t0:.6f}", "-t", f"{d:.6f}", "-i", SILENT / "master_norm.wav",
            "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", 48000, "-ac", 1, "-movflags", "+faststart", BEATS / f"{b}.mp4"])
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", BEATS / f"{b}.mp4", "-vf", "scale=1280:720", "-c:v", "libx264", "-b:v", "4M", "-maxrate", "5M",
            "-bufsize", "8M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", PREVIEW / f"{b}.mp4"])
        t0 += d
    print("master:", MASTER)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--reuse"]
    if a[:1] == ["--frame"]:
        frame(a[1], float(a[2])).save(a[3])
    elif a[:1] == ["--lowres"]:
        render(a[1:] or None)
    elif a[:1] == ["--check"]:
        sys.exit(1 if check() else 0)
    elif a[:1] == ["--render"]:
        render(a[1:] or None)
    elif a[:1] == ["--encode"]:
        encode()
    elif a[:1] == ["--all"]:
        render()
        encode()
    else:
        print(__doc__)
