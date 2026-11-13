#!/usr/bin/env python3
"""The work-video Short, "Minus Seventy-Eight": ONE continuous 9:16 scene, 2160x3840, scene(t) a pure function of time.

The device is a bar that builds: a block of loss that grows one named shock at a time, coloured by the kind of shock.
The headline number (-78%) is taken apart into the first holding's blocks (-15, -35, -40 = -90), the other two bars
(-90, -50), the shares (40/30/30) and the sum (36 + 27 + 15 = 78); my Python copy runs beside the original code
(24 of 24), and the number returns with its parts standing underneath. The loop closes on the opening state.

  /opt/homebrew/bin/python3.12 short/build_short.py --cues     # line starts (Whisper clock if present, else plan)
  /opt/homebrew/bin/python3.12 short/build_short.py --stills   # review stills -> short/_stills/ + contact sheet + change measure
  --render / --encode: not implemented yet (they raise NotImplementedError; the review of the stills comes first)

Every figure is read from committed files (the c01 stress result, the parity result, the workflow JSON read with
`git show upstream/main:...` in the Mycroft clone) and the decomposition of each holding's shock is recomputed from the
workflow's own scenario template and engine lists, then asserted against the committed result.

Layout contract (SHORT-SCRIPT.md): all ink inside x 60..900, y 230..1440 (logical 1080x1920); nothing right of 920 in
the lower half; type floor 34 px; headline 56 px at y 270 changing every line; sources 34 px in the lowest band.
Illustration colours; every portfolio invented.
"""
import ast
import importlib.util
import json
import math
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).parent
ROOT = HERE.parent
TOPIC = ROOT.parent / "topic-video"
spec = importlib.util.spec_from_file_location("c28", TOPIC / "c28_common.py")
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)

CONTRIB = ROOT.parent / "mycroft-recipe-contribution" / "mycroft-contribution"
MYCROFT = Path("/Users/tanny/Humanitarians_AI/mycroft")
WORKFLOW = ("data/mycroft-main/n8n-workflows/originals/n8n_Workflows/Scenario_Stress_Testing_Agent/"
            "ScenarioStressTestingAgent.json")

W, H = 1080, 1920
SAFE_L, SAFE_R, SAFE_T, SAFE_B = 60, 900, 230, 1440
FPS = 30
TITLE = "The Sum Behind the Number: Taking Apart a Stress Test"

# shock colours, the same as the long film
C_MARKET, C_SECTOR, C_AI, C_GROWTH, C_TECH = "#6F7F94", "#C8963E", "#C6613F", "#4E8E8A", "#8A6FA8"
KIND_COLOR = {"market": C_MARKET, "semiconductor": C_SECTOR, "ai_stocks": C_AI, "growth_stocks": C_GROWTH, "tech_sector": C_TECH}
KIND_LABEL = {"market": "market", "semiconductor": "semiconductors", "ai_stocks": "AI list", "growth_stocks": "growth", "tech_sector": "technology"}
KIND_TEXT = {"market": "#FFFFFF", "semiconductor": cm.INK, "ai_stocks": "#FFFFFF", "growth_stocks": "#FFFFFF", "tech_sector": "#FFFFFF"}


# ---------------------------------------------------------------- committed data
def load_data():
    wf = json.loads(subprocess.run(["git", "show", f"upstream/main:{WORKFLOW}"], cwd=MYCROFT, capture_output=True, text=True,
                                   check=True).stdout)
    node = {n["name"]: n["parameters"] for n in wf["nodes"]}
    tpl = node["Load_Template_Scenario"]["pythonCode"]
    scenarios = {}
    exec("scenarios = " + re.search(r"scenarios = (\{.*?\n\})\n\nscenario =", tpl, re.S).group(1), scenarios)
    eng = node["Stress_Test_Engine"]["pythonCode"]
    sector_map = ast.literal_eval(re.search(r"sector_map = (\{.*?\})", eng, re.S).group(1))
    ai_stocks = ast.literal_eval(re.search(r"ai_stocks = (\[.*?\])", eng, re.S).group(1))
    growth = ast.literal_eval(re.search(r"growth_stocks = (\[.*?\])", eng, re.S).group(1))
    res = json.loads((CONTRIB / "data/verified/scenariostresstestingagent/clean/stress-results.json").read_text())["results"]
    by = {r["id"][:3]: r["result"] for r in res if r.get("result")}
    par = json.loads((CONTRIB / "logs/scenariostresstestingagent/parity-results.json").read_text())
    shocks = scenarios["scenarios"]["tech_crash"]["shocks"]
    c01 = by["c01"]
    holdings = []
    for p in c01["all_positions"]:
        tk = p["ticker"]
        sector = sector_map.get(tk, "tech_sector")
        parts = [("market", round(shocks["market"] * 100))]
        if shocks.get(sector):
            parts.append((sector, round(shocks[sector] * 100)))
        if tk in ai_stocks and shocks.get("ai_stocks"):
            parts.append(("ai_stocks", round(shocks["ai_stocks"] * 100)))
        total = sum(v for _, v in parts)
        assert abs(total - p["shock_pct"]) < 1e-6, (tk, total, p["shock_pct"])      # the blocks add to the committed result
        holdings.append({"ticker": tk, "weight": p["weight"], "shock_pct": p["shock_pct"], "parts": parts,
                         "in_ai": tk in ai_stocks})
    book = c01["drawdown_pct"]
    assert abs(sum(h["weight"] * -h["shock_pct"] for h in holdings) + book) < 1e-6          # 36 + 27 + 15 = 78
    rows = []
    prow = {r["id"].split("/")[-1][:3]: r for r in par["rows"]}
    for cid in ("c01", "c02", "c04", "c05", "c11", "c12"):
        assert prow[cid]["match"] is True
        rows.append((cid, by[cid]["scenario_name"], by[cid]["drawdown_pct"]))
    return {"shocks": shocks, "holdings": holdings, "book": book, "parity": (par["matching"], par["requests"]), "rows": rows,
            "initial": c01["initial_portfolio_value"], "final": c01["final_portfolio_value"]}


D = load_data()
NUM = f"−{abs(D['book']):.0f}%"                       # "−78%"
assert NUM == "−78%", NUM


# ---------------------------------------------------------------- the clock
PLAN = {"S01": 0.0, "S02": 9.0, "S03": 21.0, "S04": 36.0, "S05": 49.0, "S06": 58.0, "S07": 66.0, "S08": 73.0, "END": 83.0}
NWIN = {"S01": 4, "S02": 6, "S03": 6, "S04": 6, "S05": 4, "S06": 6, "S07": 4, "S08": 5}       # schedule windows per line


def line_starts():
    p = HERE / "mp3" / "timings_short.json"
    if not p.exists():
        return dict(PLAN), "plan"
    tm = json.loads(p.read_text())
    out = {}
    for s in tm["sentences"]:
        out.setdefault(s["line"], s["start"])
    ids = sorted(out)
    assert len(ids) == 8, ids
    starts = {k: (0.0 if k == "S01" else max(0.0, out[k] - 0.2)) for k in ids}
    starts["END"] = float(tm["duration_s"])
    return starts, "whisper"



XT = {}        # (line, name) -> time of an extra event, from the Whisper words when available


def xt(L, line, name):
    return XT[(line, name)]


FB = {"S01": {}, "S02": {"wk": .25, "n1": .12, "n2": .30, "n3": .50, "n4": .72},
      "S03": {"title": .45, "short": .10, "named": .14, "named2": .17, "named3": .20, "named4": .23, "pct": .31, "count": .42, "m": .50, "s": .62, "a": .74, "t": .88, "mv": .55, "sv": .66, "av": .78, "tv": .92},
      "S04": {"add": .10, "shocks": .14, "belong": .18, "first": .27, "market": .34, "semi": .42, "ai": .55, "t15": .68, "t35": .74, "t40": .82, "t90": .90},
      "S05": {"second": .05, "n90": .38, "third": .50, "off": .55, "n50": .72, "diff": .88},
      "S06": {"share": .10, "p40": .17, "p30": .30, "p30b": .43, "a36": .56, "a27": .66, "a15": .80, "a78": .92}}


def fill_fallback(L):
    keys = sorted(k for k in L if k.startswith("S"))
    for line, d in FB.items():
        t0 = L[line]
        t1 = L[keys[keys.index(line) + 1]] if keys.index(line) + 1 < len(keys) else L["END"]
        for name, f in d.items():
            XT[(line, name)] = t0 + (t1 - t0) * f


OV = {}


def _norm(w):
    return re.sub(r"[^a-z0-9.−-]", "", w.lower())


def _wt(words, alts, lo, hi=None):
    alts = [alts] if isinstance(alts, str) else alts
    for w, s0, e0 in words:
        if s0 >= lo and (hi is None or s0 <= hi) and any(_norm(w).startswith(a) for a in alts):
            return s0
    raise KeyError((alts, lo))


def anchor_windows(L):
    """Move schedule edges onto the words they illustrate (an even split of a line put labels 1-2 s off their words).
    Missing words fall back to the even split (that edge simply stays where it was)."""
    p = HERE / "mp3" / "timings_short.json"
    OV.clear()
    fill_fallback(L)
    if not p.exists():
        return
    words = json.loads(p.read_text())["words"]

    def w(alts, lo, hi=None):
        return _wt(words, alts, lo, hi)

    def put(line, edges):
        for i, f in edges.items():
            try:
                OV.setdefault(line, {})[i] = f()
            except KeyError:
                pass
    s = lambda k: L[k]
    put("S01", {1: lambda: w("chip", s("S01")), 2: lambda: w("where", s("S01") + 3), 3: lambda: w("come", s("S01") + 3) + 0.2})
    put("S02", {1: lambda: w("im", s("S02")), 2: lambda: w("mycroft", s("S02")), 3: lambda: w("stress", s("S02")),
                4: lambda: w("invented", s("S02") + 3), 5: lambda: w("advice", s("S02") + 3)})
    put("S03", {1: lambda: w("short", s("S03")), 2: lambda: w("market", w("names", s("S03"))),
                3: lambda: w("semi", w("names", s("S03"))), 4: lambda: w("ai", w("names", s("S03"))),
                5: lambda: w("tech", w("names", s("S03")) + 1.0)})
    put("S04", {1: lambda: w("market", s("S04") + 1.5), 2: lambda: w("market", s("S04") + 1.5) + 0.5,
                3: lambda: w("semi", s("S04")), 4: lambda: w("ai", s("S04") + 3),
                5: lambda: w("ninety", s("S04") + 5) + 0.4})
    put("S05", {1: lambda: w(["ninety", "90"], s("S05")), 2: lambda: w("third", s("S05")),
                3: lambda: w(["fifty", "50"], s("S05"))})
    put("S06", {1: lambda: w("forty", s("S06")), 2: lambda: w(["thirty-six", "36"], s("S06")),
                3: lambda: w(["twenty-seven", "27"], s("S06")), 4: lambda: w(["fifteen", "15"], s("S06") + 2),
                5: lambda: w(["seventy-eight", "78"], s("S06"))})
    put("S07", {1: lambda: w("ran", s("S07")), 2: lambda: w(["twenty-four", "24"], s("S07")),
                3: lambda: w("matched", s("S07"))})
    put("S08", {1: lambda: w("ask", s("S08")), 2: lambda: w("full", s("S08")), 3: lambda: w("the", w("is", w("film", s("S08"))))})

    def x(line, name, f):
        try:
            XT[(line, name)] = f()
        except KeyError:
            pass
    x("S02", "n1", lambda: w("tanmay", s("S02"))); x("S02", "n2", lambda: w("mycroft", s("S02")))
    x("S02", "wk", lambda: w("week", s("S02")))
    x("S02", "n3", lambda: w("stress", s("S02"))); x("S02", "n4", lambda: w("invented", s("S02") + 3))
    nm = lambda: w("named", s("S03"))
    x("S03", "short", lambda: w("short", s("S03")))
    x("S03", "named", lambda: nm()); x("S03", "named2", lambda: nm() + 0.2); x("S03", "named3", lambda: nm() + 0.5)
    x("S03", "named4", lambda: nm() + 0.8)
    x("S03", "pct", lambda: w("percentage", s("S03")))
    x("S03", "title", lambda: w("this", s("S03") + 2))
    x("S03", "count", lambda: w(["4", "four"], s("S03") + 4))
    x("S03", "m", lambda: w("market", s("S03") + 6) if False else w("whole", s("S03") + 6) + 0.1)
    x("S03", "s", lambda: w("semi", s("S03"))); x("S03", "a", lambda: w("ai", s("S03") + 8))
    x("S03", "t", lambda: w("tech", s("S03") + 12) if False else w("technology", s("S03")))
    x("S03", "mv", lambda: w(["15", "fifteen"], xt(L, "S03", "m"))); x("S03", "sv", lambda: w(["35", "thirty-five"], xt(L, "S03", "s")))
    x("S03", "av", lambda: w(["40", "forty"], xt(L, "S03", "a"))); x("S03", "tv", lambda: w(["30", "thirty"], xt(L, "S03", "t")))
    x("S04", "add", lambda: w("add", s("S04"))); x("S04", "shocks", lambda: w("shocks", s("S04")))
    x("S04", "belong", lambda: w("holding", s("S04"))); x("S04", "first", lambda: w("first", s("S04")))
    x("S04", "market", lambda: w("market", s("S04") + 2.5)); x("S04", "semi", lambda: w("semi", s("S04")))
    x("S04", "ai", lambda: w("ai", s("S04") + 5))
    x("S04", "t15", lambda: w(["15", "fifteen"], s("S04") + 6)); x("S04", "t35", lambda: w(["35", "thirty-five"], s("S04") + 6))
    x("S04", "t40", lambda: w(["40", "forty"], s("S04") + 6)); x("S04", "t90", lambda: w(["90", "ninety"], s("S04") + 6))
    x("S05", "second", lambda: w("second", s("S05"))); x("S05", "n90", lambda: w(["90", "ninety"], s("S05")))
    x("S05", "third", lambda: w("third", s("S05"))); x("S05", "off", lambda: w("off", s("S05")))
    x("S05", "n50", lambda: w(["50", "fifty"], s("S05") + 2)); x("S05", "diff", lambda: w("different", s("S05")))
    x("S06", "share", lambda: w("share", s("S06")))
    p40 = lambda: w(["40", "forty"], s("S06"))
    p30 = lambda: w(["30", "thirty"], p40() + 0.1)
    x("S06", "p40", lambda: p40()); x("S06", "p30", lambda: p30())
    x("S06", "p30b", lambda: w(["30", "thirty"], p30() + 0.1))
    x("S06", "a36", lambda: w(["36", "thirty-six"], s("S06") + 3)); x("S06", "a27", lambda: w(["27", "twenty-seven"], s("S06")))
    x("S06", "a15", lambda: w(["15", "fifteen"], s("S06") + 4)); x("S06", "a78", lambda: w(["78", "seventy-eight"], s("S06")))


def win(L, line, k):
    keys = sorted(k_ for k_ in L if k_.startswith("S"))
    t0 = L[line]
    t1 = L[keys[keys.index(line) + 1]] if keys.index(line) + 1 < len(keys) else L["END"]
    n = NWIN[line]
    b = [t0 + (t1 - t0) * i / n for i in range(n + 1)]
    for i, v in OV.get(line, {}).items():
        b[i] = v
    for i in range(1, n + 1):
        b[i] = min(max(b[i], b[i - 1] + 0.05), t1)
    return b[k], b[k + 1]


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return 0.5 - 0.5 * math.cos(math.pi * x)


def ramp(t, t0, t1):
    return ease((t - t0) / max(t1 - t0, 1e-6))


def lerp(a, b, p):
    return a + (b - a) * p


def a_in(t, t0, d=0.35):
    return ramp(t, t0, t0 + d)


def a_out(t, t1, d=0.3):
    return 1 - ramp(t, t1 - d, t1)


def ctext(cv, x, y, s, kind="sans", size=34, fill=cm.INK, anchor="ls"):
    cv.text(x, y, s, kind, size, fill=fill, anchor=anchor)


LOOP_FADE = 1.0
HEADLINES = {"S01": f"Where does {NUM} come from?", "S02": "It's a sum", "S03": "A scenario is a list",
             "S04": "One holding, three blocks", "S05": "Same crash, different sums", "S06": "Add the shares",
             "S07": "Run beside the original", "S08": "Ask what was added"}
SOURCES = {"S01": "Invented portfolio · scenario arithmetic, not a prediction.",
           "S02": "Mycroft · Scenario Stress Testing Agent · PR #74.",
           "S03": "The workflow's own template (Tech Sector Crash).",
           "S04": "c01 · stress-results.json; the workflow's README worked example.",
           "S05": "c01 · stress-results.json (all_positions).",
           "S06": "c01 · stress-results.json.",
           "S07": f"parity-results.json · {D['parity'][0]} of {D['parity'][1]} identical.",
           "S08": "Invented portfolios throughout."}
SRC_BASE = {1: [1432], 2: [1391, 1432]}


def which_line(L, t):
    keys = sorted(k for k in L if k.startswith("S"))
    cur = keys[0]
    for k in keys:
        if t >= L[k]:
            cur = k
    return cur


def loop_p(L, t):
    return ramp(t, L["END"] - LOOP_FADE, L["END"])


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


def chip_w(cv, s, size=36, pad=14):
    return cv.tw(s, "sansm", size) + 2 * pad


def chip(cv, x, y, s, size=36, pad=14, fill=cm.CARD, a=1.0, fg=cm.INK):
    a0 = cv.alpha
    cv.alpha = a0 * a
    w_ = cv.tw(s, "sansm", size) + 2 * pad
    cv.rect(x, y, x + w_, y + size + 2 * pad - 4, fill=fill, outline=cm.BORDER, width=2, r=8)
    ctext(cv, x + pad, y + pad + size * 0.80, s, "sansm", size, fill=fg)
    cv.alpha = a0
    return w_


def draw_headline(cv, L, t):
    keys = sorted(k for k in L if k.startswith("S"))
    cur = which_line(L, t)
    i = keys.index(cur)
    items = []
    if i > 0 and t < L[cur] + 0.2:
        items.append((HEADLINES[keys[i - 1]], 1 - ramp(t, L[cur], L[cur] + 0.2)))
    items.append((HEADLINES[cur], ramp(t, L[cur] + 0.2, L[cur] + 0.4) if i > 0 else 1.0))
    lp = loop_p(L, t)
    if lp > 0:
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


# ---------------------------------------------------------------- the headline number
def number_state(L, t):
    """(size, baseline, lit 0..1). Opening: 260 px at 650. S02: shrinks to the top. S08: back to full size."""
    lit = 0.0
    big, small = (260, 710), (104, 405)
    if t < L["S02"]:
        size, base = big
    elif t < L["S08"]:
        p = ramp(t, L["S02"], L["S02"] + 0.95)
        size, base = lerp(big[0], small[0], p), lerp(big[1], small[1], p)
        if t >= L["S06"]:
            a = xt(L, "S06", "a78")
            lit = ramp(t, a, a + 0.5) * (1 - ramp(t, L["S07"], L["S07"] + 0.8))
    else:
        top = (260, 600)
        p = ramp(t, win(L, "S08", 0)[0], win(L, "S08", 0)[0] + 1.2)
        size, base = lerp(small[0], top[0], p), lerp(small[1], top[1], p)
        lp = loop_p(L, t)
        if lp > 0:
            q = ramp(lp, 0.35, 1.0)
            size, base = lerp(top[0], big[0], q), lerp(top[1], big[1], q)
    return size, base, lit


def draw_number(cv, L, t):
    size, base, lit = number_state(L, t)
    col = cm.mix(cm.INK, cm.SPARK_TEXT, lit)
    ctext(cv, SAFE_L, base, NUM, "serifm", int(round(size)), fill=col)


# ---------------------------------------------------------------- bars
BAR_X, BAR_SCALE = 100, 700 / 90.0         # px per percentage point: 90 points = 700 px


def block_geom(parts):
    out, x = [], BAR_X
    for kind, v in parts:
        w_ = abs(v) * BAR_SCALE
        out.append((kind, v, x, x + w_))
        x += w_
    return out


def draw_block(cv, kind, v, x0, x1, y0, y1, prog=1.0, label=True, size=52, lab_a=1.0):
    """One block of a bar; prog grows it from its left edge; the numeral fades in with lab_a (the number word)."""
    x1 = x0 + (x1 - x0) * prog
    if x1 - x0 < 2:
        return
    cv.rect(x0, y0, x1, y1, fill=KIND_COLOR[kind], outline="#FAF9F5", width=2)
    if label and prog > 0.95 and lab_a > 0.01:
        a0 = cv.alpha
        cv.alpha = a0 * lab_a
        ctext(cv, (x0 + x1) / 2, (y0 + y1) / 2 + size * 0.34, f"−{abs(v):d}", "sansm", size, fill=KIND_TEXT[kind], anchor="ms")
        cv.alpha = a0


def bar(cv, h, y0, y1, prog_list, label_size=52, labels=True, lab_alphas=None):
    """prog_list: growth 0..1 per block of the holding (draw order)."""
    geo = block_geom(h["parts"])
    la = lab_alphas or [1.0] * len(geo)
    for (kind, v, x0, x1), pr, a_ in zip(geo, prog_list, la):
        draw_block(cv, kind, v, x0, x1, y0, y1, pr, label=labels, size=label_size, lab_a=a_)
    return geo


def dashed_rect(cv, x0, y0, x1, y1, color, a):
    d = ImageDraw.Draw(cv.im, "RGBA")
    S_ = cm.S
    col = cm.rgba(color, a)
    for xx in range(int(x0 * S_), int(x1 * S_), 24 * S_):
        xe = min(xx + 12 * S_, x1 * S_)
        d.line([(xx, y0 * S_), (xe, y0 * S_)], fill=col, width=3 * S_)
        d.line([(xx, y1 * S_), (xe, y1 * S_)], fill=col, width=3 * S_)
    d.line([(x0 * S_, y0 * S_), (x0 * S_, y1 * S_)], fill=col, width=3 * S_)
    d.line([(x1 * S_, y0 * S_), (x1 * S_, y1 * S_)], fill=col, width=3 * S_)


def dashed_rect(cv, x0, y0, x1, y1, color, a):
    d = ImageDraw.Draw(cv.im, "RGBA")
    S_ = cm.S
    col = cm.rgba(color, a)
    for xx in range(int(x0 * S_), int(x1 * S_), 24 * S_):
        xe = min(xx + 12 * S_, x1 * S_)
        d.line([(xx, y0 * S_), (xe, y0 * S_)], fill=col, width=3 * S_)
        d.line([(xx, y1 * S_), (xe, y1 * S_)], fill=col, width=3 * S_)
    d.line([(x0 * S_, y0 * S_), (x0 * S_, y1 * S_)], fill=col, width=3 * S_)
    d.line([(x1 * S_, y0 * S_), (x1 * S_, y1 * S_)], fill=col, width=3 * S_)


# row geometry for the three bars (S05, S06): label baseline, bar top, share-bar top; all bars 112 px tall
ROW_LABEL = (545, 760, 975)
ROW_Y0 = (570, 785, 1000)
ROW_H = 112
SHARE_Y = (694, 909, 1124)
NUMSZ = 52                      # block numerals (>= 44)


def draw_stage(cv, L, t):
    s04, s05, s06, s07 = L["S04"], L["S05"], L["S06"], L["S07"]
    if not (s04 + 0.29 <= t < s07 + 0.4):
        return
    hs = D["holdings"]
    a_all = a_in(t, s04 + 0.3, 0.3) * a_out(t, s07 + 0.4, 0.4)
    cv.alpha = a_all
    # ---- the first holding (S04: large; S05: it moves up into the first of three rows)
    h = hs[0]
    g = ramp(t, s05 - 0.1, s05 + 0.5)
    lab_y = lerp(560, ROW_LABEL[0], g)
    y0, y1 = lerp(590, ROW_Y0[0], g), lerp(720, ROW_Y0[0] + ROW_H, g)
    geo = block_geom(h["parts"])
    tf = xt(L, "S04", "first")
    typed(cv, BAR_X, lab_y, f"first chip stock \u00b7 {h['ticker']}", t, tf, 1.7, "sansm", 40, cm.INK, a_all)
    cv.alpha = a_all
    cv.rect(BAR_X, y0, BAR_X + 700, y1, outline=cm.BORDER, width=2)
    land = [xt(L, "S04", "market"), xt(L, "S04", "semi"), xt(L, "S04", "ai")]
    ghost = [xt(L, "S04", "add"), xt(L, "S04", "shocks"), xt(L, "S04", "belong")]
    prog = [ramp(t, tt, tt + 0.55) for tt in land]
    for (kind, v, x0, x1), gt, pr in zip(geo, ghost, prog):
        ga = a_in(t, gt, 0.5) * (1 - pr)
        if ga > 0.01:
            cv.alpha = a_all * ga
            cv.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, fill=cm.mix(cm.PAGE, KIND_COLOR[kind], 0.40))
            dashed_rect(cv, x0 + 2, y0 + 2, x1 - 2, y1 - 2, KIND_COLOR[kind], 0.8 * cv.alpha)
            cv.alpha = a_all * ga * clamp(1 - 6 * pr)
            ctext(cv, (x0 + x1) / 2, (y0 + y1) / 2 + 17, "?", "sansm", 52, fill=cm.GHOST, anchor="ms")
    cv.alpha = a_all
    lab = [a_in(t, xt(L, "S04", "t15"), 0.3), a_in(t, xt(L, "S04", "t35"), 0.3), a_in(t, xt(L, "S04", "t40"), 0.3)]
    bar(cv, h, y0, y1, prog, label_size=NUMSZ, lab_alphas=lab)
    names_a = a_out(t, s05, 0.3)
    if names_a > 0.01:
        cv.alpha = a_all * names_a
        for (kind, v, x0, x1), lt in zip(geo, land):
            cv.alpha = a_all * names_a * a_in(t, lt, 0.3)
            ctext(cv, (x0 + x1) / 2, 772, KIND_LABEL[kind], "sans", 36, fill=cm.INK_SOFT, anchor="ms")
        cv.alpha = a_all * names_a
        marks = [(xt(L, "S04", "t15"), 15), (xt(L, "S04", "t35"), 50), (xt(L, "S04", "t90"), 90)]
        shown = [(tt, v) for tt, v in marks if t >= tt]
        if shown:
            tt, v = shown[-1]
            cv.alpha = a_all * names_a * a_in(t, tt, 0.25)
            ctext(cv, BAR_X, 965, f"\u2212{v}", "serifm", 150, fill=cm.INK)
            cv.alpha = a_all * names_a
            ctext(cv, BAR_X + 300, 965, "running total", "sans", 36, fill=cm.INK_SOFT)
        typed_chip(cv, BAR_X, 1070, "the README prints this sum", t, xt(L, "S04", "t90") - 0.7, 0.7, size=40, a=a_all * names_a)
        typed(cv, BAR_X, 1200, "the workflow's own worked example", t, xt(L, "S04", "t90") - 0.1, 0.4, "sans", 36, cm.INK_SOFT, a_all * names_a)
    cv.alpha = a_all
    done1 = a_in(t, xt(L, "S05", "second") - 0.2, 0.4)
    if done1 > 0.01:
        cv.alpha = a_all * done1
        ctext(cv, SAFE_R, lab_y, f"\u2212{abs(h['shock_pct']):.0f}", "serifm", 70, fill=cm.INK, anchor="rs")
    cv.alpha = a_all
    # ---- the other two bars (S05)
    for idx in (1, 2):
        ly, by0 = ROW_LABEL[idx], ROW_Y0[idx]
        hh = hs[idx]
        st = xt(L, "S05", "second" if idx == 1 else "third")
        fin = xt(L, "S05", "n90" if idx == 1 else "n50")
        ap = a_in(t, st, 0.3)
        if ap < 0.01:
            continue
        name = "second chip stock" if idx == 1 else "third chip stock"
        typed(cv, BAR_X, ly, f"{name} \u00b7 {hh['ticker']}", t, st, 1.0, "sansm", 40, cm.INK, a_all)
        cv.alpha = a_all * ap
        cv.rect(BAR_X, by0, BAR_X + 700, by0 + ROW_H, outline=cm.BORDER, width=2)
        geo2 = block_geom(hh["parts"])
        pr = [ramp(t, st + 0.1 + 0.4 * k, st + 0.1 + 0.4 * k + 0.5) for k in range(len(geo2))]
        bar(cv, hh, by0, by0 + ROW_H, pr, label_size=NUMSZ)
        if not hh["in_ai"]:
            x_ai0 = geo2[-1][3]
            x_ai1 = x_ai0 + 40 * BAR_SCALE
            la = a_in(t, xt(L, "S05", "off"), 0.4)
            cv.alpha = a_all * la
            dashed_rect(cv, x_ai0, by0, x_ai1, by0 + ROW_H, C_AI, 0.7 * cv.alpha)
            ctext(cv, (x_ai0 + x_ai1) / 2, by0 + ROW_H / 2 + 12, "off the AI list", "sans", 36, fill=cm.INK_SOFT, anchor="ms")
        va = a_in(t, fin, 0.4)
        dd_ = a_in(t, xt(L, "S05", "diff"), 0.4) * a_out(t, s06 + 1.0, 0.5) if idx == 2 else 0.0
        cv.alpha = a_all * va * clamp(1 - 2 * dd_)
        ctext(cv, SAFE_R, ly, f"\u2212{abs(hh['shock_pct']):.0f}", "serifm", 70, fill=cm.INK, anchor="rs")
    da = a_in(t, xt(L, "S05", "diff"), 0.4) * a_out(t, s06 + 1.0, 0.5)
    if da > 0.01:
        cv.alpha = a_all * da
        # "a different sum": a thick underline under the third bar and its value turns to the accent colour
        cv.rect(BAR_X, ROW_Y0[2] + ROW_H + 10, BAR_X + 700, ROW_Y0[2] + ROW_H + 24, fill=cm.SPARK)
        cv.alpha = a_all * clamp(2 * da - 1)
        ctext(cv, SAFE_R, ROW_LABEL[2], f"\u2212{abs(hs[2]['shock_pct']):.0f}", "serifm", 70, fill=cm.SPARK_TEXT, anchor="rs")
    cv.alpha = a_all
    # ---- the shares (S06) and the arithmetic
    if t >= s06 - 0.05:
        ca = a_in(t, xt(L, "S06", "share"), 0.4)
        cv.alpha = a_all * ca
        ctext(cv, BAR_X, 1200, "each holding's share of the book", "sans", 36, fill=cm.INK_SOFT)
        for idx, key in ((0, "p40"), (1, "p30"), (2, "p30b")):
            hh = hs[idx]
            gp = ramp(t, xt(L, "S06", key), xt(L, "S06", key) + 0.6)
            cv.alpha = a_all * gp
            sy = SHARE_Y[idx]
            cv.rect(BAR_X, sy, BAR_X + 700 * hh["weight"] * gp, sy + 22, fill=cm.SPARK)
            cv.alpha = a_all * a_in(t, xt(L, "S06", key), 0.35)
            nm = f"{'first' if idx == 0 else 'second' if idx == 1 else 'third'} chip stock \u00b7 {hh['ticker']}"
            x = BAR_X + cv.tw(nm, "sansm", 40) + 24
            ctext(cv, x, ROW_LABEL[idx], f"\u00b7 {hh['weight'] * 100:.0f}%", "sansm", 40, fill=cm.SPARK_TEXT)
        terms = [(f"{abs(hs[0]['weight'] * hs[0]['shock_pct']):.0f}", "a36"), (f"+ {abs(hs[1]['weight'] * hs[1]['shock_pct']):.0f}", "a27"),
                 (f"+ {abs(hs[2]['weight'] * hs[2]['shock_pct']):.0f}", "a15"), (f"= {abs(D['book']):.0f}", "a78")]
        x = SAFE_L
        for txt, key in terms:
            cv.alpha = a_all * a_in(t, xt(L, "S06", key), 0.3)
            ctext(cv, x, 1305, txt, "serifm", 108, fill=cm.SPARK_TEXT if key == "a78" else cm.INK)
            x += cv.tw(txt + " ", "serifm", 108)
        assert x - cv.tw(" ", "serifm", 108) <= SAFE_R, x          # the arithmetic fits the safe width
    cv.alpha = 1.0

# ---------------------------------------------------------------- the early scenes
def draw_opening(cv, L, t):
    """S01 and the loop: chips, the empty stack outline with its label, the first block sinking through the whole line,
    the typed question. Everything sits lower than in the first build so the safe area is used."""
    lp = loop_p(L, t)
    a_chips = 0.0
    if t < L["S02"]:
        a_chips = 0.35 + 0.35 * a_in(t, win(L, "S01", 1)[0], 0.5)
    if L["S02"] <= t < L["S02"] + 0.7:
        a_chips = 0.7 * (1 - ramp(t, L["S02"], L["S02"] + 0.7))
    a_chips = max(a_chips, 0.7 * ramp(lp, 0.55, 1.0))
    a_out_ = 0.0
    if t < L["S02"] + 0.7:
        a_out_ = 1.0 - (ramp(t, L["S02"], L["S02"] + 0.7) if t >= L["S02"] else 0.0)
    a_out_ = max(a_out_, ramp(lp, 0.55, 1.0))
    # chips on two rows (two chips, then one) so every chip ends well before the stack outline (left edge x 690)
    for i, h in enumerate(D["holdings"]):
        cv.alpha = a_chips
        cx = SAFE_L if i != 1 else SAFE_L + chip_w(cv, f"{D['holdings'][0]['ticker']} {D['holdings'][0]['weight'] * 100:.0f}%", 40) + 16
        cy = 790 if i < 2 else 872
        chip(cv, cx, cy, f"{h['ticker']} {h['weight'] * 100:.0f}%", size=40)
    if a_out_ > 0.01:
        pulse = 0.0
        a, b = win(L, "S01", 3)
        if a <= t <= b:
            pulse = 0.5 * math.sin(math.pi * clamp((t - a) / max(b - a, 1e-6)))
        cv.alpha = a_out_ * (0.75 + 0.25 * pulse)
        cv.rect(690, 360, 880, 1000, outline=cm.GHOST, width=4, r=10)
        cv.alpha = a_out_
        ctext(cv, 690, 1060, "what is it?", "sansm", 40, fill=cm.INK_SOFT)
        drift = clamp((t - 0.2) / max(L["S02"] - 0.6, 1e-6))
        cv.alpha = a_out_ * 0.55 * drift * (1 - lp)
        cv.rect(694, lerp(390, 900, drift), 876, lerp(390, 900, drift) + 96, fill=C_MARKET)
    cv.alpha = 1.0
    qa = a_in(t, win(L, "S01", 2)[0], 0.2)
    if t >= L["S02"]:
        qa *= 1 - ramp(t, L["S02"], L["S02"] + 0.7)
    qa = max(qa * (1 if lp == 0 else 1 - lp), 0)
    if qa > 0.01:
        a, b = win(L, "S01", 2)
        q = "What was added?"
        n = int(len(q) * clamp((t - a) / max(0.7 * (b - a), 1e-6)))
        cv.alpha = qa
        ctext(cv, SAFE_L, 1010, q[:max(n, 0)], "sansm", 48, fill=cm.INK)
    cv.alpha = 1.0


def typed(cv, x, y, s_, t, t0, dur, kind, size, fill, a=1.0):
    n = int(len(s_) * clamp((t - t0) / dur))
    if n > 0 and a > 0.01:
        cv.alpha = a
        ctext(cv, x, y, s_[:n], kind, size, fill=fill)
        cv.alpha = 1.0


def typed_chip(cv, x, y, s_, t, t0, dur, size=36, a=1.0):
    """A chip whose box appears at once and whose text types in (typing is a change the eye and the check both see)."""
    cv.alpha = a * a_in(t, t0, 0.25)
    w_ = cv.tw(s_, "sansm", size) + 28
    cv.rect(x, y, x + w_, y + size + 24, fill=cm.CARD, outline=cm.BORDER, width=2, r=8)
    typed(cv, x + 14, y + 14 + size * 0.80, s_, t, t0 + 0.1, dur, "sansm", size, cm.INK, a)


def typed(cv, x, y, s_, t, t0, dur, kind, size, fill, a=1.0):
    n = int(len(s_) * clamp((t - t0) / dur))
    if n > 0 and a > 0.01:
        cv.alpha = a
        ctext(cv, x, y, s_[:n], kind, size, fill=fill)
        cv.alpha = 1.0


def typed_chip(cv, x, y, s_, t, t0, dur, size=36, a=1.0):
    """A chip whose box appears at once and whose text types in (typing is a change the eye and the check both see)."""
    cv.alpha = a * a_in(t, t0, 0.25)
    w_ = cv.tw(s_, "sansm", size) + 28
    cv.rect(x, y, x + w_, y + size + 24, fill=cm.CARD, outline=cm.BORDER, width=2, r=8)
    typed(cv, x + 14, y + 14 + size * 0.80, s_, t, t0 + 0.1, dur, "sansm", size, cm.INK, a)


def draw_s02(cv, L, t):
    if not (L["S02"] <= t < L["S03"] + 0.4):
        return
    fade = a_out(t, L["S03"] + 0.3, 0.3)
    typed(cv, SAFE_L, 590, "Tanmay Kulkarni \u00b7 Humanitarians AI", t, max(xt(L, "S02", "n1"), L["S02"] + 0.6), 1.6, "sansm", 48, cm.INK, fade)
    typed_chip(cv, SAFE_L, 665, "this week \u00b7 PR #74", t, xt(L, "S02", "wk"), 1.0, size=40, a=fade)
    typed_chip(cv, SAFE_L, 775, "Mycroft \u00b7 open repository of finance pipelines", t, xt(L, "S02", "n2"), 2.6, size=38, a=fade)
    typed_chip(cv, SAFE_L, 885, "Scenario Stress Testing Agent", t, xt(L, "S02", "n3"), 2.0, size=40, a=fade)
    typed_chip(cv, SAFE_L, 995, "invented portfolio \u00b7 not investment advice", t, xt(L, "S02", "n4"), 2.2, size=40, a=fade)
    cv.alpha = 1.0


def draw_s03(cv, L, t):
    if not (L["S03"] <= t < L["S04"] + 0.4):
        return
    a_card = a_in(t, L["S03"] + 0.15, 0.4) * a_out(t, L["S04"] + 0.3, 0.3)
    cv.alpha = a_card
    cv.rect(SAFE_L, 460, SAFE_R, 1310, fill=cm.CARD, outline=cm.BORDER, width=2, r=14)
    typed(cv, SAFE_L + 40, 545, "Tech Sector Crash", t, xt(L, "S03", "title"), 1.8, "serifm", 56, cm.INK, a_card)
    typed(cv, SAFE_L + 40, 602, "a short list of named shocks", t, xt(L, "S03", "short"), 1.3, "sans", 38, cm.INK_SOFT, a_card)
    ca = a_in(t, xt(L, "S03", "count"), 0.4)
    if ca > 0.01:
        cv.alpha = a_card * ca
        chip(cv, 590, 485, "4 price shocks", size=40)
    sh = D["shocks"]
    rows = [("market", "market", sh["market"], "m"), ("semiconductor", "semiconductors", sh["semiconductor"], "s"),
            ("ai_stocks", "AI stocks", sh["ai_stocks"], "a"), ("tech_sector", "technology", sh["tech_sector"], "t")]
    for i, (kind, label, v, key) in enumerate(rows):
        y = 665 + i * 140
        slot = a_in(t, xt(L, "S03", ["named", "named2", "named3", "named4"][i]), 0.4)
        ph = a_in(t, xt(L, "S03", "pct") + 0.7 * i, 0.4)
        fill = a_in(t, xt(L, "S03", key), 0.4)
        vfill = a_in(t, xt(L, "S03", key + "v"), 0.4)
        if slot < 0.01:
            continue
        cv.alpha = a_card * slot
        cv.rect(SAFE_L + 40, y, SAFE_L + 124, y + 84, fill=cm.mix(cm.BORDER, KIND_COLOR[kind], max(fill, 0.45 * ph)), outline=cm.BORDER, width=2)
        cv.alpha = a_card * fill
        ctext(cv, SAFE_L + 156, y + 58, label, "sansm", 48, fill=cm.INK)
        cv.alpha = a_card * vfill
        ctext(cv, SAFE_R - 40, y + 64, f"\u2212{abs(v) * 100:.0f}%", "serifm", 68, fill=cm.INK, anchor="rs")
        cv.alpha = a_card * ph * clamp(1 - 2 * vfill)
        ctext(cv, SAFE_R - 40, y + 64, "\u2212?%", "serifm", 68, fill=cm.GHOST, anchor="rs")
    cv.alpha = a_card
    ctext(cv, SAFE_L + 40, 1275, "the workflow's own template", "sans", 36, fill=cm.INK_SOFT)
    cv.alpha = 1.0


def draw_s07(cv, L, t):
    if not (L["S07"] - 0.01 <= t < L["S08"] + 0.5):
        return
    a_all = a_in(t, L["S07"] + 0.3, 0.4) * a_out(t, L["S08"] + 0.5, 0.4)
    cv.alpha = a_all
    ctext(cv, SAFE_L, 545, "original code", "sansm", 48, fill=cm.INK)
    ra_ = a_in(t, win(L, "S07", 0)[0] + 0.3, 0.4)
    cv.alpha = a_all * ra_
    ctext(cv, 480, 545, "Python copy", "sansm", 48, fill=cm.INK)
    n = len(D["rows"])
    a1, b1 = win(L, "S07", 1)
    for i, (cid, scen, dd) in enumerate(D["rows"]):
        y = 660 + i * 100
        cv.alpha = a_all
        ctext(cv, SAFE_L, y, f"{cid}  \u2212{abs(dd):g}%", "sans", 46, fill=cm.INK)
        rp = ramp(t, a1 + (b1 - a1) * i / n, a1 + (b1 - a1) * (i + 1) / n + 0.3)
        cv.alpha = a_all * rp
        ctext(cv, 480, y, f"{cid}  \u2212{abs(dd):g}%", "sans", 46, fill=cm.INK)
        tx, ty = 830, y - 14
        cv.line([(tx, ty), (tx + 14, ty + 16), (tx + 40, ty - 22)], fill=C_GROWTH, width=8)
    a2, b2 = win(L, "S07", 2)
    a3, b3 = win(L, "S07", 3)
    k = int(round(D["parity"][0] * ramp(t, a2, a3 + 0.5)))
    ca = a_in(t, a2, 0.3)
    cv.alpha = a_all * ca
    ctext(cv, SAFE_L, 1312, f"{k} of {D['parity'][1]}", "serifm", 140, fill=cm.SPARK_TEXT if k == D["parity"][0] else cm.INK)
    ia = a_in(t, a3 + 0.2, 0.4)
    cv.alpha = a_all * ia
    ctext(cv, 700, 1312, "identical", "sansm", 48, fill=cm.INK_SOFT)
    cv.alpha = 1.0


def draw_s08(cv, L, t):
    if t < L["S08"]:
        return
    lp = loop_p(L, t)
    ba = a_in(t, win(L, "S08", 1)[0], 0.5) * (1 - ramp(lp, 0.0, 0.4))
    scale = 560 / 90.0
    cv.alpha = ba
    for i, h in enumerate(D["holdings"]):
        y = 665 + i * 80
        x = SAFE_L
        for kind, v in h["parts"]:
            w_ = abs(v) * scale
            cv.rect(x, y, x + w_, y + 58, fill=KIND_COLOR[kind], outline="#FAF9F5", width=2)
            x += w_
        ctext(cv, SAFE_R, y + 46, f"\u2212{abs(h['shock_pct']):.0f}", "serifm", 60, fill=cm.INK, anchor="rs")
    ca = a_in(t, win(L, "S08", 2)[0], 0.5) * (1 - ramp(lp, 0.0, 0.4))
    cv.alpha = ca
    cv.rect(SAFE_L, 960, SAFE_R, 1310, fill=cm.CARD, outline=cm.BORDER, width=2, r=14)
    ta0 = win(L, "S08", 3)[0]
    lines = wrap_lines(cv, TITLE, "serifm", 56, SAFE_R - SAFE_L - 80)
    nchar = int(len(TITLE) * clamp((t - ta0) / 1.4))
    shown = TITLE[:nchar]
    y = 1045
    off = 0
    for ln in lines:
        part = shown[off:off + len(ln)] if off < len(shown) else ""
        ctext(cv, SAFE_L + 40, y, part, "serifm", 56, fill=cm.INK)
        off += len(ln) + 1
        y += 72
    ctext(cv, SAFE_L + 40, 1270, "Humanitarians AI", "sansm", 44, fill=cm.INK_SOFT)
    cv.alpha = 1.0

# ---------------------------------------------------------------- the overlap check
class LogCanvas(cm.Canvas):
    """c28's Canvas that also records the boxes of the visible text and shapes it draws (alpha > 0.3)."""

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.tboxes, self.sboxes = [], []

    def text(self, x, y, s, kind="sans", size=24, fill=cm.INK, anchor="la"):
        super().text(x, y, s, kind, size, fill=fill, anchor=anchor)
        if self.alpha > 0.3 and s.strip():
            w_ = self.tw(s, kind, size)
            x0 = x if anchor[0] == "l" else (x - w_ if anchor[0] == "r" else x - w_ / 2)
            self.tboxes.append((x0, y - 0.78 * size, x0 + w_, y + 0.22 * size, s))

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        super().rect(x0, y0, x1, y1, fill=fill, outline=outline, width=width, r=r)
        if self.alpha > 0.3 and (fill or outline) and (x1 - x0) > 3 and (y1 - y0) > 3:
            self.sboxes.append((x0, y0, x1, y1, f"shape@{round(x0)},{round(y0)}"))


def _inter(a, b):
    w_ = min(a[2], b[2]) - max(a[0], b[0])
    h_ = min(a[3], b[3]) - max(a[1], b[1])
    return (w_ * h_) if (w_ > 0 and h_ > 0) else 0.0


def _inside(a, b, tol=4):
    """a lies inside b (within tol)."""
    return a[0] >= b[0] - tol and a[1] >= b[1] - tol and a[2] <= b[2] + tol and a[3] <= b[3] + tol


def collisions(cv):
    """Text vs shape, shape vs shape, text vs text. Text inside its own container (fully inside a shape) is intentional;
    a shape lying fully inside another (blocks in their bar, a chip's box in a card) is intentional."""
    out = []
    T, S_ = cv.tboxes, cv.sboxes
    for t_ in T:
        for sh in S_:
            if _inter(t_, sh) > 8 and not _inside(t_, sh):
                out.append(("text/shape", t_[4], sh[4]))
    for i, a in enumerate(S_):
        for b in S_[i + 1:]:
            if _inter(a, b) > 40 and not _inside(a, b) and not _inside(b, a):
                out.append(("shape/shape", a[4], b[4]))
    for i, a in enumerate(T):
        for b in T[i + 1:]:
            if _inter(a, b) > 12:
                out.append(("text/text", a[4], b[4]))
    return out


# ---------------------------------------------------------------- the scene
def scene(L, t):
    cv = LogCanvas(W, H, min_sans=34)
    draw_headline(cv, L, t)
    draw_number(cv, L, t)
    draw_opening(cv, L, t)
    draw_s02(cv, L, t)
    draw_s03(cv, L, t)
    draw_stage(cv, L, t)
    draw_s07(cv, L, t)
    draw_s08(cv, L, t)
    draw_source(cv, L, t)
    cv.alpha = 1.0
    return cv


# ---------------------------------------------------------------- stills
def still_times(L):
    def mid(line, k, f=0.5):
        a, b = win(L, line, k)
        return a + (b - a) * f
    X = lambda line, name, d=0.0: xt(L, line, name) + d
    return [
        ("S01-a", mid("S01", 1, 0.8)), ("S01-b", mid("S01", 2, 0.9)), ("S01-c", mid("S01", 3, 0.7)),
        ("S02-a", X("S02", "n3", -0.15)), ("S02-b", X("S02", "n4", 2.4)),
        ("S03-a", X("S03", "pct", 1.9)), ("S03-b", X("S03", "t", 1.8)),
        ("S04-a", X("S04", "belong", 0.8)), ("S04-b", X("S04", "ai", 0.9)), ("S04-c", X("S04", "t90", 0.4)),
        ("S05-a", X("S05", "n90", 0.6)), ("S05-b", X("S05", "diff", 0.9)),
        ("S06-a", X("S06", "p30b", 0.6)), ("S06-b", X("S06", "a78", 0.8)),
        ("S07-a", win(L, "S07", 2)[0] - 0.05), ("S07-b", mid("S07", 3, 0.9)),
        ("S08-a", mid("S08", 1, 0.95)), ("S08-b", mid("S08", 3, 0.95)), ("S08-c", L["END"] - LOOP_FADE - 0.2), ("S08-d", L["END"] - 0.02),
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


SPOKEN = {"S01": ["78"], "S03": ["15", "35", "40"], "S04": ["15", "35", "40", "90"], "S05": ["90", "50"],
          "S06": ["36", "27", "15", "78"], "S07": ["24"], "S02": ["74"]}
STILL_LINE = {}


COLL = []


def make_stills(L, src):
    out = HERE / "_stills"
    out.mkdir(exist_ok=True)
    report, thumbs, logs = [], [], {}
    for name, t in still_times(L):
        cv = scene(L, t)
        ok, bb = check_still(name, cv)
        cv.save(out / f"{name}-9x16.png")
        for kind, a, b in collisions(cv):
            COLL.append((name, kind, a, b))
            print(f"   COLLISION {name}: {kind}: {a!r} x {b!r}")
        report.append((name, round(t, 2), ok, bb))
        logs[name] = " | ".join(s for s, size, a, x, y in cv.log if a > 0.3)
        thumbs.append((name, cv.im.resize((360, 640), Image.LANCZOS)))
        print(f"{name} t={t:6.2f}s  ink x{bb[0]}-{bb[1]} y{bb[2]}-{bb[3]}  {'OK' if ok else 'OUTSIDE SAFE AREA'}", flush=True)
    # the figures the narration speaks must be on screen in the line's own stills
    for line, figs in SPOKEN.items():
        text = " ".join(v for k, v in logs.items() if k.startswith(line))
        for f in figs:
            assert f in text, (line, f)
    cols = 4
    rows = math.ceil(len(thumbs) / cols)
    sheet = Image.new("RGB", (cols * 380 + 20, rows * 680 + 20), "#DDDACF")
    d = ImageDraw.Draw(sheet)
    for i, (name, im) in enumerate(thumbs):
        x, y = 20 + (i % cols) * 380, 20 + (i // cols) * 680
        sheet.paste(im, (x, y))
        d.text((x + 6, y + 648), name, fill="#3D3929")
    sheet.save(out / "contact-short.png")
    (out / "collisions.json").write_text(json.dumps(COLL, indent=1, ensure_ascii=False))
    print(f"overlap check: {len(COLL)} collision(s) in {len(report)} stills")
    (out / "text-log.json").write_text(json.dumps(logs, indent=1, ensure_ascii=False))
    return report


def frame_small(args):
    L, t = args
    anchor_windows(L)
    cm.S = 1
    cm._fc.clear()
    cv = scene(L, t)
    return np.asarray(cv.im.convert("L").resize((540, 960), Image.LANCZOS)).astype(np.int16)


def run_change_measure(L):
    from multiprocessing import Pool
    step, gap, thr = 0.5, 2.5, 0.30
    times = sorted(set([round(i * step, 3) for i in range(int(L["END"] / step) + 1)] + [round(i * step + gap, 3) for i in range(int((L["END"] - gap) / step) + 1)]))
    times = [t for t in times if t <= L["END"] - 0.01]
    with Pool(3) as p:
        frames = dict(zip(times, p.map(frame_small, [(L, t) for t in times])))
    res = []
    for t in times:
        t2 = round(t + gap, 3)
        if t2 in frames:
            res.append((t, (np.abs(frames[t] - frames[t2]) > 12).mean() * 100))
    return res, [(t, round(d_, 3)) for t, d_ in res if d_ < thr], thr


# ---------------------------------------------------------------- the video
NF = lambda L: int(round(L["END"] * FPS))          # frames in the video (END is the audio length)


def _init(L, S_):
    global _L
    _L = L
    cm.S = S_
    cm._fc.clear()
    anchor_windows(L)


def render_frame(i):
    """Full-size frame i (t = i / FPS) to _frames/, with the text it drew (alpha > 0.3) for the gate."""
    cv = scene(_L, i / FPS)
    cv.im.save(HERE / "_frames" / f"{i:05d}.png", compress_level=1)
    return i, [(sx, size, round(a, 2), round(x), round(y)) for sx, size, a, x, y in cv.log if a > 0.3]


def render_all(L, workers=3):
    from multiprocessing import Pool
    (HERE / "_frames").mkdir(exist_ok=True)
    (HERE / "_qc").mkdir(exist_ok=True)
    n = NF(L)
    log = {}
    with Pool(workers, initializer=_init, initargs=(L, 2)) as p:
        for k, (i, texts) in enumerate(p.imap(render_frame, range(n), chunksize=4)):
            log[i] = texts
            if k % 200 == 0:
                print(f"  frame {k}/{n}", flush=True)
    (HERE / "_qc" / "render_log.json").write_text(json.dumps({"fps": FPS, "frames": n, "log": log}))
    print(f"{n} frames rendered ({n / FPS:.3f} s)")


def lowres_frame(i):
    """540x960 gray frame i, its drawn text and its collisions (logical coordinates), for the cheap checks."""
    cv = scene(_L, i / FPS)
    g = np.asarray(cv.im.convert("L").resize((540, 960), Image.BOX), dtype=np.uint8)
    texts = [(sx, size, round(a, 2), round(x), round(y)) for sx, size, a, x, y in cv.log if a > 0.3]
    return i, g, texts, [(k, a_, b_) for k, a_, b_ in collisions(cv)]


def lowres_all(L, workers=3):
    from multiprocessing import Pool
    n = NF(L)
    (HERE / "_lowres").mkdir(exist_ok=True)
    (HERE / "_qc").mkdir(exist_ok=True)
    mm = np.lib.format.open_memmap(HERE / "_lowres" / "gray.npy", mode="w+", dtype=np.uint8, shape=(n, 960, 540))
    log, coll = {}, {}
    with Pool(workers, initializer=_init, initargs=(L, 1)) as p:
        for k, (i, g, texts, cs) in enumerate(p.imap(lowres_frame, range(n), chunksize=8)):
            mm[i] = g
            log[i] = texts
            if cs:
                coll[i] = cs
    mm.flush()
    (HERE / "_qc" / "lowres_log.json").write_text(json.dumps({"fps": FPS, "frames": n, "log": log, "collisions": coll}))
    print(f"{n} low-resolution frames; {len(coll)} frames with a collision")


def rerender_changed(L, workers=3):
    """Re-render only the frames that drew one of the strings changed after the full render ("made of: ?", the typed question,
    "semis", "my Python copy"); every other frame's drawing code is untouched, so its PNG stays. Updates the render log."""
    from multiprocessing import Pool
    old = json.loads((HERE / "_qc" / "render_log.json").read_text())
    log = {int(k): v for k, v in old["log"].items()}
    gone = {"made of: ?", "semis", "my Python copy"}
    q_old = "What is it made of?"
    todo = [i for i, v in log.items() if any(e[0] in gone or (e[1] == 48 and e[0] and q_old.startswith(e[0]) and e[4] in (940, 1010)) for e in v)]
    todo.sort()
    print(f"re-rendering {len(todo)} of {len(log)} frames")
    with Pool(workers, initializer=_init, initargs=(L, 2)) as p:
        for i, texts in p.imap(render_frame, todo, chunksize=4):
            log[i] = texts
    (HERE / "_qc" / "render_log.json").write_text(json.dumps({"fps": FPS, "frames": old["frames"], "log": log}))
    return todo


def typed_prefix(full):
    return lambda e: bool(e[0]) and full.startswith(e[0])


def exact(txt, size=None):
    return lambda e: e[0] == txt and (size is None or e[1] == size)


def events(L):
    """(label, predicate on a drawn-text entry, the word it illustrates, word search start). Every one must first show
    0..0.4 s AFTER its word, never before."""
    s = lambda k: L[k]
    return [
        ("S01 question typed", typed_prefix("What was added?"), "where", s("S01") + 3),
        ("S02 name typed", typed_prefix("Tanmay Kulkarni \u00b7 Humanitarians AI"), "tanmay", s("S02")),
        ("S02 this-week chip", typed_prefix("this week \u00b7 PR #74"), "week", s("S02")),
        ("S02 Mycroft chip", typed_prefix("Mycroft \u00b7 open repository of finance pipelines"), "mycroft", s("S02")),
        ("S02 recipe chip", typed_prefix("Scenario Stress Testing Agent"), "stress", s("S02")),
        ("S02 invented chip", typed_prefix("invented portfolio \u00b7 not investment advice"), "invented", s("S02") + 3),
        ("S03 caption typed", typed_prefix("a short list of named shocks"), "short", s("S03")),
        ("S03 title typed", typed_prefix("Tech Sector Crash"), "this", s("S03") + 2),
        ("S03 placeholder -?%", exact("\u2212?%"), "percentage", s("S03")),
        ("S03 '4 price shocks'", exact("4 price shocks"), ["4", "four"], s("S03") + 4),
        ("S03 label market", exact("market", 48), "market", None),
        ("S03 value -15%", exact("\u221215%"), ["15"], None),
        ("S03 label semiconductors", exact("semiconductors", 48), "semi", s("S03")),
        ("S03 value -35%", exact("\u221235%"), ["35"], None),
        ("S03 label AI stocks", exact("AI stocks", 48), "ai", s("S03") + 8),
        ("S03 value -40%", exact("\u221240%"), ["40"], None),
        ("S03 label technology", exact("technology", 48), "technology", s("S03")),
        ("S03 value -30%", exact("\u221230%"), ["30"], None),
        ("S04 first-holding label typed", typed_prefix("first chip stock \u00b7 NVDA"), "first", s("S04")),
        ("S04 name 'market'", exact("market", 36), "market", s("S04") + 1.5),
        ("S04 name 'semiconductors'", exact("semiconductors", 36), "semi", s("S04")),
        ("S04 name 'AI list'", exact("AI list", 36), "ai", s("S04") + 3),
        ("S04 numeral -15", exact("\u221215", 52), ["15"], None),
        ("S04 numeral -35", exact("\u221235", 52), ["35"], None),
        ("S04 numeral -40", exact("\u221240", 52), ["40"], None),
        ("S04 running total -15", exact("\u221215", 150), ["15"], s("S04") + 6),
        ("S04 running total -50", exact("\u221250", 150), ["35"], s("S04") + 6),
        ("S04 running total -90", exact("\u221290", 150), ["90"], s("S04") + 6),
        ("S05 second-holding label typed", typed_prefix("second chip stock \u00b7 AMD"), "second", s("S05")),
        ("S05 value -90 (second row)", lambda e: e[0] == "\u221290" and e[1] == 70 and e[4] == ROW_LABEL[1], ["90"], s("S05")),
        ("S05 third-holding label typed", typed_prefix("third chip stock \u00b7 TSM"), "third", s("S05")),
        ("S05 'off the AI list'", exact("off the AI list", 36), "off", s("S05")),
        ("S05 value -50", exact("\u221250", 70), ["50"], s("S05")),
        ("S06 share 40%", exact("\u00b7 40%", 40), ["40"], s("S06")),
        ("S06 arithmetic 36", exact("36", 108), ["36"], s("S06")),
        ("S06 arithmetic + 27", exact("+ 27", 108), ["27"], s("S06")),
        ("S06 arithmetic + 15", exact("+ 15", 108), ["15"], s("S06") + 2),
        ("S06 arithmetic = 78", exact("= 78", 108), ["78"], s("S06")),
        ("S07 counter starts", lambda e: e[1] == 140 and " of 24" in e[0], ["24"], s("S07")),
        ("S08 title typed", typed_prefix(TITLE), "the", None),
    ]


def event_times(L, words, lo_default=None):
    """The word time of each event: the first matching word at or after the search start (None: after the previous event)."""
    out, prev = [], 0.0
    for label, pred, alts, lo in events(L):
        alts_ = [alts] if isinstance(alts, str) else alts
        start = prev if lo is None else lo
        if label == "S08 title typed":
            start = _wt(words, "is", _wt(words, "film", L["S08"]))
        if label == "S03 label market":
            start = _wt(words, "names", L["S03"])
        if label == "S06 share 40%":
            alts_ = ["40"]
        try:
            wt = _wt(words, alts_, start)
        except KeyError:
            wt = None
        out.append((label, pred, wt))
        if wt is not None:
            prev = wt
    return out


def lowcheck(L):
    d = json.loads((HERE / "_qc" / "lowres_log.json").read_text())
    log = {int(k): v for k, v in d["log"].items()}
    g = np.load(HERE / "_lowres" / "gray.npy", mmap_mode="r")
    n = len(g)
    words = json.loads((HERE / "mp3" / "timings_short.json").read_text())["words"]
    print(f"== low-resolution checks on {n} frames ({n / FPS:.2f} s), clock: {line_starts()[1]}")
    # (a) label / block / figure timing against the words
    bad = 0
    for label, pred, wt in event_times(L, words):
        if wt is None:
            print(f"   ?? {label}: word not found")
            bad += 1
            continue
        lo_i = max(int((wt - 1.2) * FPS), 0)
        first = None
        for i in range(lo_i, min(int((wt + 2.5) * FPS), n)):
            if any(pred(e) for e in log[i]):
                first = i / FPS
                break
        dt = None if first is None else first - wt
        okk = dt is not None and -0.034 <= dt <= 0.40
        bad += not okk
        print(f"   {'ok ' if okk else 'BAD'} {label:34s} word {wt:6.2f}s  first on screen {('%6.2f' % first) if first is not None else '  none'}s  delta {('%+.2f' % dt) if dt is not None else '-'}")
    print(f"(a) event timing: {len(events(L)) - bad}/{len(events(L))} within 0..0.4 s after their word")
    # (b) hard cuts
    means = np.array([np.abs(g[i + 1].astype(np.int16) - g[i].astype(np.int16)).mean() for i in range(n - 1)])
    top = np.argsort(means)[::-1][:3]
    print(f"(b) largest frame-to-frame change {means.max():.2f} grey levels (limit 3.0), at {[round((i + 1) / FPS, 2) for i in top]} s")
    # (c) collisions
    print(f"(c) frames with a collision: {len(d['collisions'])}")
    for i, cs in list(d["collisions"].items())[:6]:
        print("    t=%.2f" % (int(i) / FPS), cs[:2])
    # (d) change between frames 2.5 s apart; and the longest static run
    gap = int(2.5 * FPS)
    pair = [((np.abs(g[i + gap].astype(np.int16) - g[i].astype(np.int16)) > 12).mean() * 100, i / FPS) for i in range(0, n - gap, 15)]
    mn = min(pair)
    print(f"(d) change 2.5 s apart: min {mn[0]:.3f}% at {mn[1]:.1f} s, median {float(np.median([p_[0] for p_ in pair])):.3f}%; windows under 0.3%: {[(round(t_, 1), round(v, 3)) for v, t_ in pair if v < 0.3] or 'none'}")
    moved = [(np.abs(g[i + 1].astype(np.int16) - g[i].astype(np.int16)) > 10).sum() for i in range(n - 1)]
    run = best = at = 0
    for i, mv in enumerate(moved):
        run = run + 1 if mv < 10 else 0
        if run > best:
            best, at = run, i
    print(f"    longest static run (fewer than 10 pixels changing between frames) {best / FPS:.2f} s, ends {at / FPS:.1f} s")


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
    if "--lowres" in args:
        lowres_all(L)
    if "--lowcheck" in args:
        lowcheck(L)
    if "--rerender" in args:
        rerender_changed(L)
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
    if "--overlaps" in args:
        # the overlap check on the whole timeline, every 0.25 s (logical coordinates do not depend on the render scale)
        cm.S = 1
        cm._fc.clear()
        found = {}
        tt = 0.0
        while tt < L["END"]:
            cv = scene(L, tt)
            for kind, a_, b_ in collisions(cv):
                found.setdefault((kind, a_, b_), []).append(round(tt, 2))
            tt += 0.25
        for (kind, a_, b_), ts_ in found.items():
            print(f"{kind}: {a_!r} x {b_!r} at t = {ts_[0]}..{ts_[-1]} ({len(ts_)} samples)")
        print(f"overlap check over the timeline: {len(found)} distinct collision(s) in {int(L['END'] / 0.25)} samples")
    if "--measure" in args:
        res, low, thr = run_change_measure(L)
        ds = [d_ for _, d_ in res]
        print(f"change measure (2.5 s apart, 540x960): min {min(ds):.3f}%, median {float(np.median(ds)):.3f}%, "
              f"windows under {thr}%: {low or 'none'}")
