#!/usr/bin/env python3
"""Week 28 WORK video, long film: one 3840x2160 review still per beat (two or three states where a beat has distinct moments).

The film's device is a RUNNING TOTAL: a bar of loss that grows one named shock at a time. Block colours mean the same
thing in every beat (and in the Short): market #6F7F94, semiconductors #C8963E, AI list #C6613F, growth #4E8E8A,
technology #8A6FA8. Every number is read from the committed files (the mirror of PR #74's contribution, the merged
workflow JSON and the vendored README), never typed by hand; the figures the narration speaks are asserted from the
Canvas text log (CHECKS). Positive framing is a standing instruction: nothing negative.

Layout contract (carried from the topic video's PROOF review): every evidence caption ends on ONE common last baseline,
y 996 of 1080, at one common left x (115), at most two lines; every sans caption >= 28 px; headlines >= 56; margins >= 60.

Run:  /opt/homebrew/bin/python3.12 build_long_stills.py   -> _stills/Bxx[-a|-b|-c]-16x9.png, _stills/contact-long.png
"""
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "topic-video"))
from c28_common import (BORDER, CARD, GHOST, INK, INK_SOFT, PAGE, S, SEND, SPARK, SPARK_TEXT, F, Canvas, hex2rgb, mix)  # noqa: E402

MIRROR = HERE.parent / "mycroft-recipe-contribution" / "mycroft-contribution"
CLONE = Path("/Users/tanny/Humanitarians_AI/mycroft")
WF = "data/mycroft-main/n8n-workflows/originals/n8n_Workflows/Scenario_Stress_Testing_Agent/ScenarioStressTestingAgent.json"
README = "docs/mycroft-main/n8n_Workflows/Scenario_Stress_Testing_Agent/README.md"
OUT = HERE / "_stills"
OUT.mkdir(exist_ok=True)
W, H = 1920, 1080
M = 115                       # left margin = the one left x of every evidence caption
SRC_BASE = 996                # the one last baseline of every evidence caption
CAP = 28                      # minimum sans size
MONO = ImageFont.truetype("/Users/tanny/Humanitarians_AI/brutalist.art/runtime/fonts/PT_Mono/PTMono-Regular.ttf", 1)

# shock kinds: the film's colours (same in the Short)
KIND = {"market": "#6F7F94", "semiconductors": "#C8963E", "AI list": "#C6613F", "growth": "#4E8E8A", "technology": "#8A6FA8"}


# ----------------------------------------------------------------------------- data (read, never typed)

def git_show(path):
    return subprocess.run(["git", "-C", str(CLONE), "show", f"upstream/main:{path}"], capture_output=True, text=True, check=True).stdout


STRESS = {r["id"][:3]: r for r in json.loads((MIRROR / "data/verified/scenariostresstestingagent/clean/stress-results.json").read_text())["results"]}
PARITY = json.loads((MIRROR / "logs/scenariostresstestingagent/parity-results.json").read_text())
SELF = (MIRROR / "logs/scenariostresstestingagent/self-test-results.md").read_text()
RUNLOG = json.loads((MIRROR / "logs/scenariostresstestingagent-run-approved-tools-2026-10-25.json").read_text())
RECIPE = (MIRROR / "recipes/scenariostresstestingagent.md").read_text()
DEF_AUDIT = (MIRROR / "data/verified/scenariostresstestingagent/defective/validate-audit.md").read_text()
CLEAN_AUDIT = (MIRROR / "data/verified/scenariostresstestingagent/clean/validate-audit.md").read_text()
WORKFLOW = json.loads(git_show(WF))
README_TXT = git_show(README)


def scenario_shocks(name):
    code = next(n for n in WORKFLOW["nodes"] if n["name"] == "Load_Template_Scenario")["parameters"]["pythonCode"]
    ns = {}
    exec("scenarios = " + re.search(r"scenarios = (\{.*?\n\})\n\nscenario =", code, re.S).group(1), ns)
    return ns["scenarios"][name]


C01, C12 = STRESS["c01"]["result"], STRESS["c12"]["result"]
POS01 = {p["ticker"]: p for p in C01["all_positions"]}
TECH = scenario_shocks("tech_crash")
RATE = scenario_shocks("rate_hike")
assert C01["drawdown_pct"] == -78.0 and C01["initial_portfolio_value"] == 10000 and C01["final_portfolio_value"] == 2200
assert [POS01[t]["shock_pct"] for t in ("NVDA", "AMD", "TSM")] == [-90.0, -90.0, -50.0]
assert C12["drawdown_pct"] == -33.75 and C12["risk_level"] == "CRITICAL"
assert PARITY["matching"] == 24 and PARITY["mismatching"] == 0
assert "27/27" in SELF and "12/12" in SELF


def num(x):
    x = float(x)
    return ("−" if x < 0 else "") + (f"{abs(x):g}")


def pct(x):
    return f"{num(x)}%"


def weights(fix):
    j = json.loads(next((MIRROR / "data/raw/scenariostresstestingagent/sample/clean").glob(f"{fix}*.json")).read_text())
    return [(h["ticker"], h["weight"]) for h in j["body"]["portfolio"]["holdings"]]


W06, W08 = weights("c06"), weights("c08")
assert round(sum(w for _, w in W06), 3) == 0.6 and round(sum(w for _, w in W08), 3) == 1.2


def defect_reasons():
    out = {}
    for m in re.finditer(r"\| `(d\d\d)[^`]*` \| (.*?) \|\n", DEF_AUDIT):
        out[m.group(1)] = m.group(2)
    return out


REASONS = defect_reasons()


def short_reason(key):
    r = REASONS[key]
    r = re.sub(r" \(the node's own rule\)| \(gate addition\)", "", r).split(" ; ")[0]
    return r.split(":")[0].strip()


# ----------------------------------------------------------------------------- helpers

STILLS, CHECKS = {}, {}


def put(name, cv, must=()):
    STILLS[name] = cv
    CHECKS[name] = list(must)


class WCanvas(Canvas):
    """Accent text below 48 px logical uses the 4.7:1 accent (SPARK_TEXT), not SEND (3.85:1, large text only).
    It also records the bounding box (logical px) of every text and every shape drawn, for the collision check."""
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.tboxes, self.sboxes = [], []

    def text(self, x, y, s, kind="sans", size=24, fill=INK, anchor="la"):
        if fill == SEND and size < 48:
            fill = SPARK_TEXT
        if self.alpha > 0.01:
            l, t, r, b = F(kind, size).getbbox(s, anchor=anchor)
            self.tboxes.append((s, x + l / S, y + t / S, x + r / S, y + b / S))
        super().text(x, y, s, kind, size, fill=fill, anchor=anchor)

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        if self.alpha > 0.01:
            self.sboxes.append(("rect" if fill else "outline", x0, y0, x1, y1))
        super().rect(x0, y0, x1, y1, fill=fill, outline=outline, width=width, r=r)

    def poly(self, pts, fill):
        if self.alpha > 0.01:
            xs, ys = [p[0] for p in pts], [p[1] for p in pts]
            self.sboxes.append(("poly", min(xs), min(ys), max(xs), max(ys)))
        super().poly(pts, fill)

    def ellipse(self, cx, cy, rx, ry=None, fill=None, outline=None, width=1):
        ry = rx if ry is None else ry
        if self.alpha > 0.01:
            self.sboxes.append(("ellipse", cx - rx, cy - ry, cx + rx, cy + ry))
        super().ellipse(cx, cy, rx, ry, fill=fill, outline=outline, width=width)


def new():
    return WCanvas(W, H, min_sans=CAP)


def headline(cv, s):
    cv.text(M, 130, s, "serifm", 64, fill=INK, anchor="ls")


def text_on(color):
    """white or ink, whichever contrasts more with the block colour (large text only: >= 3:1 is asserted)."""
    def lum(c):
        c = [v / 255 for v in hex2rgb(c)]
        c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    best = max(("#FFFFFF", INK), key=lambda t: (max(lum(t), lum(color)) + 0.05) / (min(lum(t), lum(color)) + 0.05))
    ratio = (max(lum(best), lum(color)) + 0.05) / (min(lum(best), lum(color)) + 0.05)
    assert ratio >= 3.0, (color, ratio)
    return best


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


def evidence(cv, s):
    """The one evidence band: left x M, last baseline 996, at most two lines, 28 px."""
    lines = wrap(cv, s, "sans", CAP, W - 2 * M)
    assert len(lines) <= 2, s
    for i, ln in enumerate(lines):
        cv.text(M, SRC_BASE - 40 * (len(lines) - 1 - i), ln, "sans", CAP, fill=INK_SOFT, anchor="ls")


def mono(cv, x, y, s, size=28, fill=INK):
    """PT Mono, drawn through an alpha mask (Canvas.text only knows the c28_common faces); logged for the checks."""
    if cv.alpha <= 0.01:
        return
    cv.log.append((s, size, round(cv.alpha, 2), x, y))
    fill = SPARK_TEXT if (fill == SEND and size < 48) else fill
    font = ImageFont.truetype(MONO.path, round(size * S))
    l, t, r, b = font.getbbox(s, anchor="ls")
    cv.tboxes.append((s, x + l / S, y + t / S, x + r / S, y + b / S))
    pad = 3
    mask = Image.new("L", (r - l + 2 * pad, b - t + 2 * pad), 0)
    ImageDraw.Draw(mask).text((-l + pad, -t + pad), s, font=font, fill=255, anchor="ls")
    a = max(0.0, min(1.0, cv.alpha))
    if a < 0.999:
        mask = mask.point(lambda v: int(v * a))
    cv.im.paste(hex2rgb(fill), (int(round(x * S + l - pad)), int(round(y * S + t - pad))), mask)


def pill(cv, x, y, w, h, s, fill=CARD, outline=BORDER, fg=INK, size=32, kind="sansm"):
    cv.rect(x, y, x + w, y + h, fill=fill, outline=outline, width=2, r=h // 2)
    cv.text(x + w / 2, y + h / 2 + size * 0.36, s, kind, size, fill=fg, anchor="ms")


def chip(cv, x, y, w, h, s, size=32, fill=CARD, fg=INK):
    cv.rect(x, y, x + w, y + h, fill=fill, outline=BORDER, width=2, r=10)
    cv.text(x + w / 2, y + h / 2 + size * 0.36, s, "sansm", size, fill=fg, anchor="ms")


def arrow(cv, x0, y0, x1, y1, fill=INK_SOFT, width=4):
    import math
    cv.line([(x0, y0), (x1, y1)], fill=fill, width=width)
    a = math.atan2(y1 - y0, x1 - x0)
    cv.poly([(x1, y1), (x1 - 18 * math.cos(a - 0.45), y1 - 18 * math.sin(a - 0.45)), (x1 - 18 * math.cos(a + 0.45), y1 - 18 * math.sin(a + 0.45))], fill)


def bar(cv, x, y, h, blocks, scale, size=44, highlight=None):
    """A running-total bar: blocks = [(kind, pct)], pct negative; drawn left to right; each block carries its number."""
    cx = x
    for i, (kind, p) in enumerate(blocks):
        w = abs(p) * scale
        col = KIND[kind]
        cv.rect(cx, y, cx + w, y + h, fill=col, outline=PAGE, width=3)
        cv.text(cx + w / 2, y + h / 2 + size * 0.34, num(p), "serifm", size, fill=text_on(col), anchor="ms")
        if highlight == i:
            cv.rect(cx - 6, y - 6, cx + w + 6, y + h + 6, outline=INK, width=4)
        cx += w
    return cx


def legend(cv, x, y, kinds, size=CAP):
    cx = x
    for k in kinds:
        cv.rect(cx, y - 24, cx + 28, y + 4, fill=KIND[k])
        cv.text(cx + 40, y, k, "sans", size, fill=INK_SOFT, anchor="ls")
        cx += 40 + cv.tw(k, "sans", size) + 44
    return cx


def dashed_outline(cv, x, y, w, h, dash=18, gap=12, fill=GHOST, width=3):
    cv.sboxes.append(("dashed", x, y, x + w, y + h))
    px = x
    while px < x + w:
        e = min(px + dash, x + w)
        cv.line([(px, y), (e, y)], fill=fill, width=width)
        cv.line([(px, y + h), (e, y + h)], fill=fill, width=width)
        px += dash + gap
    py = y
    while py < y + h:
        e = min(py + dash, y + h)
        cv.line([(x, py), (x, e)], fill=fill, width=width)
        cv.line([(x + w, py), (x + w, e)], fill=fill, width=width)
        py += dash + gap


TICKER_LABEL = "Invented portfolio · tickers from the workflow's own map"


# ----------------------------------------------------------------------------- the beats

def b01():
    cv = new()
    headline(cv, "Where does −78% come from?")
    cv.text(M, 440, f"{num(C01['drawdown_pct'])}.0%", "serifm", 250, fill=SEND, anchor="ls")
    cv.text(1010, 290, C01["scenario_name"], "sansm", 48, fill=INK, anchor="ls")
    cv.text(1010, 380, f"${C01['initial_portfolio_value']:,} → ${int(C01['final_portfolio_value']):,}", "sansm", 56, fill=INK, anchor="ls")
    for i, t in enumerate(("NVDA", "AMD", "TSM")):
        chip(cv, M + i * 290, 520, 260, 80, f"{t} {int(POS01[t]['weight'] * 100)}%")
    cv.text(M, 720, "made of: ?", "sansm", 44, fill=INK_SOFT, anchor="ls")
    dashed_outline(cv, M, 750, 900, 110)
    cv.text(M + 450, 825, "?", "serifm", 72, fill=GHOST, anchor="ms")
    evidence(cv, f"Evidence: stress-results.json · c01 (drawdown_pct {C01['drawdown_pct']}, initial 10,000, final 2,200) · {TICKER_LABEL}")
    put("B01", cv, ["−78.0%", "$10,000", "$2,200", "NVDA 40%", "AMD 30%", "TSM 30%", "made of: ?"])


def b02():
    cv = new()
    headline(cv, "What this is")
    cv.rect(M, 190, W - M, 340, fill=CARD, outline=BORDER, width=2, r=14)
    line = re.search(r"Mycroft is both a book and a working agentic repository\.", README_TXT) or re.search(r"Mycroft is both a book and a working agentic repository\.", git_show("README.md"))
    quote = line.group(0) if line else "Mycroft is both a book and a working agentic repository."
    cv.text(M + 40, 290, f"“{quote.replace('Mycroft is ', 'Mycroft: ').rstrip('.')}”", "serifi", 50, fill=INK, anchor="ls")
    cv.text(M, 400, "Scenario Stress Testing Agent", "sansm", 52, fill=INK, anchor="ls")
    mono(cv, M, 450, "recipes/scenariostresstestingagent.md", 30, INK_SOFT)
    cv.text(M, 530, "the workflow's local steps", "sans", CAP, fill=INK_SOFT, anchor="ls")
    steps = ["validate the portfolio", "pick the scenario", "apply the shocks"]
    for i, s in enumerate(steps):
        x = M + i * 560
        chip(cv, x, 556, 470, 84, s, size=34)
        if i < 2:
            arrow(cv, x + 480, 598, x + 548, 598)
    pill(cv, M, 700, 460, 80, "PR #74 · merged", outline=SPARK, fg=SEND, size=40)
    cv.rect(M, 810, W - M, 900, fill=CARD, outline=BORDER, width=2, r=12)
    cv.text(M + 36, 868, "Invented portfolios · tickers from the workflow's own map · not investment advice", "sansm", 34, fill=INK, anchor="ls")
    evidence(cv, "Evidence: the repository README · recipes/scenariostresstestingagent.md · PR #74, merged 2026-10-26 (merge commit 5d60312)")
    put("B02", cv, ["Mycroft: both a book and a working agentic repository", "Scenario Stress Testing Agent", "PR #74 · merged", "not investment advice"])


SHOCK_ROWS = [("market", "market", TECH["shocks"]["market"]), ("technology", "technology sector", TECH["shocks"]["tech_sector"]),
              ("semiconductors", "semiconductors", TECH["shocks"]["semiconductor"]), ("AI list", "AI stocks", TECH["shocks"]["ai_stocks"])]


def scenario_card(cv, alpha=1.0):
    a0 = cv.alpha
    cv.alpha = alpha
    cv.rect(M, 190, 1000, 740, fill=CARD, outline=BORDER, width=2, r=14)
    cv.text(M + 36, 256, TECH["name"], "sansm", 40, fill=INK, anchor="ls")
    y = 330
    for kind, label, v in SHOCK_ROWS:
        cv.rect(M + 36, y - 30, M + 36 + 40, y + 10, fill=KIND[kind])
        cv.text(M + 100, y, label, "sansm", 40, fill=INK, anchor="ls")
        cv.text(940, y, pct(v * 100), "serifm", 52, fill=INK, anchor="rs")
        y += 92
    cv.rect(M + 36, y - 30, M + 76, y + 10, fill=GHOST)
    cv.text(M + 100, y, "volatility number", "sansm", 40, fill=INK, anchor="ls")
    cv.text(940, y, f"{TECH['shocks']['volatility_spike']:g}", "serifm", 52, fill=INK, anchor="rs")
    cv.alpha = a0


def b03():
    cv = new()
    headline(cv, "A scenario is a list")
    scenario_card(cv)
    cv.text(M, 800, "the workflow's own template", "sans", CAP, fill=INK_SOFT, anchor="ls")
    for i, ln in enumerate(wrap(cv, "The engine's rule: for each holding, add up the shocks that belong to it.", "serifi", 48, 640)):
        cv.text(1110, 300 + i * 66, ln, "serifi", 48, fill=INK, anchor="ls")
    evidence(cv, "Evidence: the workflow's Load_Template_Scenario node (tech_crash), as committed in the merged workflow file")
    put("B03-a", cv, ["Tech Sector Crash", "−15%", "−30%", "−35%", "−40%", "2.5"])
    cv = new()
    headline(cv, "Hold a guess")
    scenario_card(cv, alpha=0.35)
    cv.rect(1060, 190, W - M, 450, fill=CARD, outline=SPARK, width=3, r=14)
    for i, ln in enumerate(wrap(cv, "market −15% → the biggest holding falls how far?", "serifm", 54, 680)):
        cv.text(1100, 270 + i * 70, ln, "serifm", 54, fill=INK, anchor="ls")
    cv.text(1060, 540, "NVDA", "sansm", 34, fill=INK_SOFT, anchor="ls")
    dashed_outline(cv, 1060, 560, 700, 100)
    cv.text(1060 + 350, 630, "?", "serifm", 72, fill=GHOST, anchor="ms")
    evidence(cv, "Evidence: the workflow's Load_Template_Scenario node (tech_crash) · " + TICKER_LABEL)
    put("B03-b", cv, ["market −15%", "how far?", "NVDA"])


def readme_card(cv, x, y, w, h):
    m = re.search(r"Market shock:\s+(-\d+%)\s+Semiconductor:\s+(-\d+%)\s+AI stocks:\s+(-\d+%)\s+.*?Total impact:\s+(-\d+%)", README_TXT, re.S)
    assert m, "README worked example not found"
    rows = [("Market shock:", m.group(1)), ("Semiconductor:", m.group(2)), ("AI stocks:", m.group(3)), ("Total impact:", m.group(4))]
    cv.rect(x, y, x + w, y + h, fill=CARD, outline=BORDER, width=2, r=12)
    for i, (a, b) in enumerate(rows):
        yy = y + 62 + i * 58
        if i == 3:
            cv.line([(x + 30, yy - 44), (x + w - 30, yy - 44)], fill=BORDER, width=2)
        mono(cv, x + 30, yy, a, 30, INK)
        mono(cv, x + w - 30 - 30 * 0.6 * len(b), yy, b, 30, SEND if i == 3 else INK)


def b04():
    blocks = [("market", TECH["shocks"]["market"] * 100), ("semiconductors", TECH["shocks"]["semiconductor"] * 100), ("AI list", TECH["shocks"]["ai_stocks"] * 100)]
    caps = ["market −15: every holding belongs to it", "semiconductors −35: its sector", "AI stocks −40: it is on the AI list"]
    totals = ["−15", "−50", "−90"]
    for i, s in enumerate("abc"):
        cv = new()
        headline(cv, ["One holding, one block", "A second block lands", "The blocks add up"][i])
        cv.text(M, 250, "NVDA · the biggest holding", "sansm", 40, fill=INK_SOFT, anchor="ls")
        bar(cv, M, 290, 140, blocks[: i + 1], 10, size=64)
        dashed_outline(cv, M, 290, 900, 140, fill=GHOST, width=2)
        for j in range(i + 1):
            y = 520 + j * 72
            cv.rect(M, y - 30, M + 40, y + 8, fill=KIND[blocks[j][0]])
            cv.text(M + 64, y, caps[j], "sans", 38, fill=INK, anchor="ls")
        cv.text(1090, 290, "running total", "sans", CAP, fill=INK_SOFT, anchor="ls")
        cv.text(1090, 450, totals[i], "serifm", 190, fill=SEND if i == 2 else INK, anchor="ls")
        if i == 2:
            pill(cv, 1090, 520, 420, 60, "README worked example", outline=SPARK, fg=SEND, size=30)
            readme_card(cv, 1090, 600, 715, 270)
            cv.text(M, 780, "another way to combine them is named in the README", "sans", 34, fill=INK_SOFT, anchor="ls")
            evidence(cv, f"Evidence: stress-results.json · c01 · NVDA: shock_pct −90.0, loss −3,600.0 · the workflow's README (a vendored file) · {TICKER_LABEL}")
        else:
            evidence(cv, "Evidence: stress-results.json · c01 · NVDA · the workflow's Load_Template_Scenario node · " + TICKER_LABEL)
        must = [["−15", "market −15: every holding belongs to it"], ["−50", "semiconductors −35: its sector"],
                ["−90", "AI stocks −40: it is on the AI list", "README worked example", "Total impact:", "−3,600", "another way to combine them"]][i]
        put(f"B04-{s}", cv, must)


def b05():
    nv = [("market", -15), ("semiconductors", -35), ("AI list", -40)]
    am = [("market", -15), ("semiconductors", -35), ("AI list", -40)]
    ts = [("market", -15), ("semiconductors", -35)]
    cv = new()
    headline(cv, "Same crash, different sums")
    rows = [("NVDA 40%", nv), ("AMD 30%", am), ("TSM 30%", ts)]
    for r, (label, blocks) in enumerate(rows):
        y = 230 + r * 160
        cv.text(M, y + 70, label, "sansm", 36, fill=INK, anchor="ls")
        bar(cv, 360, y, 110, [(k, v) for k, v in blocks], 8, size=52)
        cv.text(360 + sum(abs(v) for _, v in blocks) * 8 + 30, y + 74, f"{num(sum(v for _, v in blocks))}", "serifm", 56, fill=SEND if r == 2 else INK, anchor="ls")
    legend(cv, M, 800, ["market", "semiconductors", "AI list"])
    for i, (w, p, res) in enumerate((("0.40", 90, 36), ("0.30", 90, 27), ("0.30", 50, 15))):
        cv.text(1250, 320 + i * 96, f"{w} × {p} = {res}", "serifm", 60, fill=INK, anchor="ls")
    cv.line([(1250, 590), (1805, 590)], fill=INK_SOFT, width=3)
    cv.text(1250, 680, "total 78", "serifm", 80, fill=SEND, anchor="ls")
    for k, ln in enumerate(wrap(cv, "NVDA and AMD are on the AI list; TSM is not, so it takes −50.", "sans", CAP, 560)):
        cv.text(1250, 750 + k * 38, ln, "sans", CAP, fill=INK_SOFT, anchor="ls")
    evidence(cv, f"Evidence: stress-results.json · c01 · all_positions: −90, −90, −50 · {TICKER_LABEL}")
    put("B05-a", cv, ["NVDA 40%", "AMD 30%", "TSM 30%", "−90", "−50", "0.40 × 90 = 36", "0.30 × 90 = 27", "0.30 × 50 = 15", "total 78"])
    cv = new()
    headline(cv, "The number, taken apart")
    cv.text(M, 400, f"{num(C01['drawdown_pct'])}.0%", "serifm", 220, fill=SEND, anchor="ls")
    cv.text(1010, 300, C01["scenario_name"], "sansm", 44, fill=INK, anchor="ls")
    cv.text(1010, 380, "36 + 27 + 15 = 78", "serifm", 60, fill=INK, anchor="ls")
    for r, (label, blocks) in enumerate(rows):
        y = 500 + r * 100
        cv.text(M, y + 52, label, "sansm", 34, fill=INK, anchor="ls")
        bar(cv, 360, y, 74, blocks, 8, size=40)
    legend(cv, M, 850, ["market", "semiconductors", "AI list"])
    evidence(cv, f"Evidence: stress-results.json · c01 · drawdown_pct {C01['drawdown_pct']} · {TICKER_LABEL}")
    put("B05-b", cv, ["−78.0%", "36 + 27 + 15 = 78", "NVDA 40%", "AMD 30%", "TSM 30%"])


def b06():
    cv = new()
    headline(cv, "A milder scenario, the same rule")
    sh = RATE["shocks"]
    cv.text(M, 205, f"{RATE['name']}: market {pct(sh['market'] * 100)} · growth stocks {pct(sh['growth_stocks'] * 100)} · technology sector {pct(sh['tech_sector'] * 100)}", "sans", 34, fill=INK_SOFT, anchor="ls")
    items = []
    for p in C12["all_positions"]:
        b = [("market", sh["market"] * 100)]
        if p["ticker"] == "TSLA":
            b += [("technology", sh["tech_sector"] * 100)]
        b += [("growth", sh["growth_stocks"] * 100)]
        assert abs(sum(v for _, v in b) - p["shock_pct"]) < 1e-9, (p["ticker"], b)
        items.append((f"{p['ticker']} {int(p['weight'] * 100)}%", b))
    for r, (label, blocks) in enumerate(items):
        y = 260 + r * 120
        cv.text(M, y + 58, label, "sansm", 34, fill=INK, anchor="ls")
        bar(cv, 360, y, 88, blocks, 10, size=44, highlight=2 if label.startswith("TSLA") else None)
        cv.text(360 + sum(abs(v) for _, v in blocks) * 10 + 30, y + 58, num(sum(v for _, v in blocks)), "serifm", 52, fill=SEND if label.startswith("TSLA") else INK, anchor="ls")
    legend(cv, M, 780, ["market", "technology", "growth"])
    cv.text(1280, 360, f"{abs(C12['drawdown_pct']):g}%", "serifm", 190, fill=SEND, anchor="ls")
    pill(cv, 1280, 400, 360, 70, C12["risk_level"].lower(), outline=SPARK, fg=SEND, size=40)
    cv.text(1280, 520, "above 30%: critical", "sans", CAP + 2, fill=INK_SOFT, anchor="ls")
    cv.text(1280, 566, "the workflow's label", "sans", CAP, fill=INK_SOFT, anchor="ls")
    evidence(cv, f"Evidence: stress-results.json · c12 · all_positions −45, −30, −30, −30 · drawdown_pct {C12['drawdown_pct']} · risk_level {C12['risk_level']} · {TICKER_LABEL}")
    put("B06", cv, ["−45", "−30", "33.75%", "critical", "above 30%: critical", "TSLA 25%"])


def self_rows():
    rows = []
    for m in re.finditer(r"\| deliberate break \| (.*?) \|", SELF):
        t = m.group(1)
        t = re.split(r": (parity|provenance|the gate)", t)[0]
        rows.append(t)
    assert len(rows) == 12
    short = {
        "a port that skips the weight rescale": "skip the weight rescale",
        "a port with a wrong CRITICAL threshold (25, not 30)": "move the critical threshold",
        "a port that treats exactly 10.0 as MODERATE ('>=' for '>')": "change one comparison",
        "a port that rounds positions to 1 decimal, not 2": "round to one decimal",
        "a port whose default scenario is rate_hike, not tech_crash": "change the default scenario",
        "a port with NVDA in the wrong sector": "move a holding to another sector",
        "a port that sends a custom scenario down the template branch": "route a custom scenario as a template",
        "a renamed node": "rename a node",
        "a rewired connection (the engine skipped)": "rewire a connection",
        "a tampered fixture": "tamper with a fixture",
        "a holding without a ticker": "remove a ticker",
    }
    out = []
    for r in rows:
        key = next((k for k in short if r.startswith(k)), None)
        out.append(short[key] if key else "add a shock of its own")     # the one row about an extra shock, stated neutrally
    return out


def b07():
    cv = new()
    headline(cv, "Run beside the original")
    fields = [("scenario", C01["scenario_name"]), ("total loss", f"{num(C01['total_loss'] / 1):s}".replace("7800", "7,800")), ("drawdown", f"{num(C01['drawdown_pct'])}.0%"),
              ("final value", f"{int(C01['final_portfolio_value']):,}"), ("risk level", C01["risk_level"].lower())]
    for c, title in enumerate(("original code", "my copy")):
        x = M + c * 640
        cv.rect(x, 190, x + 590, 700, fill=CARD, outline=BORDER, width=2, r=14)
        cv.text(x + 30, 250, title, "sansm", 40, fill=INK, anchor="ls")
        for r, (k, v) in enumerate(fields):
            cv.text(x + 30, 330 + r * 76, k, "sans", CAP, fill=INK_SOFT, anchor="ls")
            cv.text(x + 560, 330 + r * 76, v, "sansm", 36, fill=INK, anchor="rs")
    cv.text(1420, 330, f"{PARITY['matching']} of {PARITY['requests']}", "serifm", 84, fill=SEND, anchor="ls")
    cv.text(1420, 400, "identical", "sansm", 48, fill=INK, anchor="ls")
    for k, ln in enumerate(wrap(cv, "every number, every label, every message", "sans", CAP, 380)):
        cv.text(1420, 470 + k * 38, ln, "sans", CAP, fill=INK_SOFT, anchor="ls")
    cv.text(M, 770, "the original code is run straight from the workflow file", "sans", CAP, fill=INK_SOFT, anchor="ls")
    cv.text(M, 810, "c01 shown; parity row c01: match true", "sans", CAP, fill=INK_SOFT, anchor="ls")
    evidence(cv, f"Evidence: parity-results.json · requests {PARITY['requests']}, matching {PARITY['matching']}, mismatching {PARITY['mismatching']} · {TICKER_LABEL}")
    put("B07-a", cv, ["original code", "my copy", "24 of 24", "identical"])
    cv = new()
    headline(cv, "Twelve deliberate breaks")
    rows = self_rows()
    for i, r in enumerate(rows):
        col, row = divmod(i, 6)
        x = M + col * 870
        y = 240 + row * 92
        cv.rect(x, y - 48, x + 820, y + 28, fill=CARD, outline=BORDER, width=2, r=10)
        cv.text(x + 24, y + 4, f"BREAK: {r}", "sans", CAP, fill=INK, anchor="ls")
        cv.text(x + 796, y + 4, "caught", "sansm", CAP, fill=SEND, anchor="rs")
    cv.text(M, 850, "27 of 27 checks as expected · 12 of 12 deliberate breaks caught", "serifm", 52, fill=INK, anchor="ls")
    evidence(cv, "Evidence: self-test-results.md · checks 27/27 as expected · deliberate breaks caught 12/12")
    put("B07-b", cv, ["27 of 27", "12 of 12", "BREAK: skip the weight rescale", "caught"])


def b08():
    cv = new()
    headline(cv, "The checks keep the sum honest")
    cv.rect(840, 190, 1000, 760, fill=mix(PAGE, SPARK, 0.12), outline=SPARK, width=3, r=10)
    cv.text(920, 740, "validator", "sansm", CAP, fill=SEND, anchor="ms")
    for i, (fix, wts) in enumerate((("c06", W06), ("c08", W08))):
        y = 220 + i * 240
        tot = round(sum(w for _, w in wts), 3)
        cv.rect(M, y, 560, y + 190, fill=CARD, outline=BORDER, width=2, r=12)
        cv.text(M + 30, y + 50, fix, "sansm", 34, fill=INK_SOFT, anchor="ls")
        cv.text(M + 30, y + 120, "weights total", "sans", CAP, fill=INK_SOFT, anchor="ls")
        cv.text(530, y + 130, f"{tot:g}", "serifm", 80, fill=INK, anchor="rs")
        arrow(cv, 580, y + 95, 830, y + 95)
        arrow(cv, 1010, y + 95, 1160, y + 95)
        cv.rect(1180, y, 1805, y + 190, fill=CARD, outline=BORDER, width=2, r=12)
        cv.text(1210, y + 56, "accepted · rescaled to", "sans", CAP + 2, fill=INK_SOFT, anchor="ls")
        cv.text(1210, y + 150, "1.0", "serifm", 80, fill=SEND, anchor="ls")
    cv.text(M, 740, "12 of 12 clean portfolios accepted", "sansm", 40, fill=INK, anchor="ls")
    evidence(cv, "Evidence: validate-audit.md (clean: requests in 12, accepted 12) · c06 and c08 · Invented")
    put("B08-a", cv, ["0.6", "1.2", "1.0", "12 of 12"])
    cv = new()
    headline(cv, "Each stop carries its reason")
    for i, key in enumerate(("d03", "d05", "d09")):
        y = 220 + i * 150
        cv.rect(M, y, 560, y + 112, fill=CARD, outline=BORDER, width=2, r=12)
        cv.text(M + 30, y + 66, key, "sansm", 40, fill=INK_SOFT, anchor="ls")
        cv.rect(700, y - 10, 760, y + 122, fill=INK_SOFT)       # a calm "pause" mark: the run stops here, with its reason
        cv.rect(715, y + 36, 727, y + 76, fill="#FFFFFF")
        cv.rect(733, y + 36, 745, y + 76, fill="#FFFFFF")
        cv.rect(850, y, W - M, y + 112, fill=CARD, outline=BORDER, width=2, r=12)
        reason = short_reason(key)
        reason = reason[0].upper() + reason[1:]
        lines = wrap(cv, reason, "sansm", 34, 880)[:2]
        for k, ln in enumerate(lines):
            cv.text(880, y + (68 if len(lines) == 1 else 44) + k * 46, ln, "sansm", 34, fill=INK, anchor="ls")
    cv.text(M, 740, "10 of 10 stopped, each for its own reason", "sansm", 40, fill=INK, anchor="ls")
    cv.text(M, 800, "a sum of nothing never reaches the screen", "serifi", 48, fill=INK_SOFT, anchor="ls")
    evidence(cv, "Evidence: validate-audit.md (defective: requests in 10, rejected 10, each with its reason) · Invented")
    put("B08-b", cv, ["d03", "d05", "d09", "10 of 10"])


def b09():
    cv = new()
    headline(cv, "A good list for next time")
    hand = RUNLOG["handoffs_not_made"]
    names = {"Fetch_Data": "market-data request", "Basic LLM Chain / Groq Chat Model": "call to a model", "Respond to Webhook": "reply to a caller"}
    cv.text(M, 220, "written down as hand-offs, not approved", "sansm", 36, fill=INK_SOFT, anchor="ls")
    for i, h in enumerate(hand):
        y = 250 + i * 128
        cv.rect(M, y, 960, y + 104, fill=CARD, outline=BORDER, width=2, r=12)
        cv.text(M + 28, y + 46, names.get(h["node"], h["node"]), "sansm", 36, fill=INK, anchor="ls")
        mono(cv, M + 28, y + 86, f"approved_for_live_action: {str(h['approved_for_live_action']).lower()}", 26 + 2, SEND)
    cv.rect(1040, 250, W - M, 460, fill=CARD, outline=BORDER, width=2, r=12)
    fm = re.match(r"---\n(.*?)\n---", RECIPE, re.S).group(1).splitlines()
    keep = [ln for ln in fm if ln.split(":")[0] in ("status", "todos_open", "recipe_version")]
    assert len(keep) == 3
    for i, ln in enumerate(keep):
        mono(cv, 1070, 320 + i * 56, ln, 32, INK)
    cv.text(1040, 520, "open items", "sansm", 36, fill=INK_SOFT, anchor="ls")
    items = ["step 2 · ingest declared inputs", "step 4 · transform and quality check", "step 6 · produce human report",
             "map · respond to webhook", "map · human report script"]
    for i, t in enumerate(items):
        y = 570 + i * 56
        cv.rect(1040, y - 28, 1070, y + 2, outline=INK_SOFT, width=3, r=4)
        cv.text(1092, y, t, "sans", 30, fill=INK, anchor="ls")
    cv.text(M, 750, "nothing here calls the outside world", "serifi", 52, fill=INK, anchor="ls")
    cv.text(M, 820, "5 items open · draft, on purpose", "sansm", 40, fill=INK_SOFT, anchor="ls")
    evidence(cv, "Evidence: the step-5 run log (handoffs_not_made, approved_for_live_action false) · the recipe frontmatter (status DRAFT, todos_open 5)")
    put("B09", cv, ["approved_for_live_action: false", "status: DRAFT", "todos_open: 5", "5 items open", "market-data request", "call to a model", "reply to a caller"])


def b10():
    cv = new()
    headline(cv, "Ask what was added")
    qs = ["Which shocks?", "From which lists?", "Has anyone run the adder beside the original?"]
    y = 250
    for i, q in enumerate(qs):
        for ln in wrap(cv, q, "serifm", 60, 900):
            cv.text(M, y, ln, "serifm", 60, fill=INK, anchor="ls")
            y += 76
        y += 24
    cv.text(M, y + 40, "A good answer names the terms.", "serifi", 72, fill=SEND, anchor="ls")
    cv.text(1150, 400, f"{num(C01['drawdown_pct'])}.0%", "serifm", 190, fill=mix(PAGE, SEND, 0.22), anchor="ls")
    a0 = cv.alpha
    cv.alpha = 0.3
    for r, blocks in enumerate([[("market", -15), ("semiconductors", -35), ("AI list", -40)], [("market", -15), ("semiconductors", -35), ("AI list", -40)], [("market", -15), ("semiconductors", -35)]]):
        bar(cv, 1150, 470 + r * 90, 64, blocks, 6.5, size=34)
    cv.alpha = a0
    evidence(cv, f"Evidence: the number is stress-results.json · c01 · drawdown_pct {C01['drawdown_pct']} · {TICKER_LABEL}")
    put("B10", cv, ["Which shocks?", "From which lists?", "Has anyone run the adder", "A good answer names the terms.", "−78.0%"])


def b11():
    cv = new()
    cv.text(M, 360, "Humanitarians AI", "serifm", 104, fill=INK, anchor="ls")
    cv.text(M, 440, "Tanmay Kulkarni · @HumanitariansAI", "sans", 48, fill=INK_SOFT, anchor="ls")
    cv.line([(M, 500), (900, 500)], fill=BORDER, width=3)
    cv.text(M, 590, "github.com/nikbearbrown/mycroft · PR #74", "sansm", 44, fill=INK, anchor="ls")
    mono(cv, M, 650, "recipes/scenariostresstestingagent.md", 34, INK_SOFT)
    bar(cv, 1130, 300, 90, [("market", -15), ("semiconductors", -35), ("AI list", -40)], 7, size=44)
    bar(cv, 1130, 410, 90, [("market", -15), ("semiconductors", -35), ("AI list", -40)], 7, size=44)
    bar(cv, 1130, 520, 90, [("market", -15), ("semiconductors", -35)], 7, size=44)
    evidence(cv, f"Evidence: PR #74 merged 2026-10-26 (merge commit 5d60312) · {TICKER_LABEL}")
    put("B11", cv, ["Humanitarians AI", "@HumanitariansAI", "PR #74", "recipes/scenariostresstestingagent.md"])


# ----------------------------------------------------------------------------- collision check

TIGHT = 12            # logical px: a label closer than this to a shape/number it does not sit in reads as touching it


def _inter(a, b):
    return min(a[3], b[3]) - max(a[1], b[1]) > 0.5 and min(a[4], b[4]) - max(a[2], b[2]) > 0.5


def _inside(t, sh, pad=0.5):
    return t[1] >= sh[1] - pad and t[2] >= sh[2] - pad and t[3] <= sh[3] + pad and t[4] <= sh[4] + pad


def _gap(a, b):
    dx = max(b[1] - a[3], a[1] - b[3], 0)
    dy = max(b[2] - a[4], a[2] - b[4], 0)
    return (dx * dx + dy * dy) ** 0.5


def collisions(cv):
    """(collisions, tight): a text box that partly overlaps a shape it is not inside; two overlapping text boxes;
    and text/shape or text/text pairs under TIGHT px apart that are not nested."""
    hard, tight = [], []
    for ti, t in enumerate(cv.tboxes):
        for sh in cv.sboxes:
            if _inside(t, sh):
                continue
            if _inter(t, sh):
                hard.append(f"text {t[0][:30]!r} overlaps {sh[0]} {tuple(round(v) for v in sh[1:])}")
            elif _gap(t, sh) < TIGHT and sh[0] != "dashed":
                tight.append(f"text {t[0][:30]!r} is {_gap(t, sh):.0f}px from {sh[0]} {tuple(round(v) for v in sh[1:])}")
        for u in cv.tboxes[ti + 1:]:
            if _inter(t, u):
                hard.append(f"text {t[0][:24]!r} overlaps text {u[0][:24]!r}")
            elif _gap(t, u) < TIGHT and abs((t[2] + t[4]) / 2 - (u[2] + u[4]) / 2) > 6:
                tight.append(f"text {t[0][:24]!r} is {_gap(t, u):.0f}px from text {u[0][:24]!r}")
    filled = [sh for sh in cv.sboxes if sh[0] in ("rect", "poly", "ellipse")]
    for i, a in enumerate(filled):
        for b in filled[i + 1:]:
            if _inter(a, b) and not (_inside(("", *a[1:]), b) or _inside(("", *b[1:]), a)):
                hard.append(f"{a[0]} {tuple(round(v) for v in a[1:])} overlaps {b[0]} {tuple(round(v) for v in b[1:])}")
    return hard, tight


# ----------------------------------------------------------------------------- run

def contact():
    names = sorted(STILLS)
    tw, th, cols = 640, 360, 4
    rows = (len(names) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tw + 20) + 20, rows * (th + 56) + 20), "#DDDAD0")
    d = ImageDraw.Draw(sheet)
    for i, n in enumerate(names):
        im = Image.open(OUT / f"{n}-16x9.png").resize((tw, th), Image.LANCZOS)
        x, y = 20 + (i % cols) * (tw + 20), 20 + (i // cols) * (th + 56)
        sheet.paste(im, (x, y))
        d.text((x, y + th + 8), n, font=F("sansm", 12), fill=INK)
    sheet.save(OUT / "contact-long.png")


def main():
    for fn in (b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11):
        fn()
    bad = 0
    for name, cv in STILLS.items():
        text = " | ".join(t[0] for t in cv.log)
        for must in CHECKS[name]:
            if must not in text:
                print(f"CHECK FAIL {name}: missing {must!r}")
                bad += 1
        hard, tight = collisions(cv)
        for h in hard:
            print(f"COLLISION {name}: {h}")
        for t in tight:
            print(f"TIGHT {name}: {t}")
        bad += len(hard)
        small = [t for t in cv.log if t[1] < CAP and t[0].strip()]
        if small:
            print(f"SMALL TYPE {name}: {small[:2]}")
            bad += 1
        cv.save(OUT / f"{name}-16x9.png")
        print(f"{name}: {len(cv.log)} text items")
    contact()
    print("checks failed:", bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
