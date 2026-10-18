"""scenes.py — Manim scenes for banking-domain-interview-end-to-end-v2 (cli-explainer) — v3.
5 output beats (B01, B02, B05, B08, B09); the other 7 render via Remotion.
Claude-skin palette: cream ground, warm ink, one terracotta accent, plus a teal→crimson
gradient for delinquency buckets (current → charge-off).
Scene classes must be declared as plain Scene subclasses named B0X_Name — run.sh finds them by regex.
No LaTeX (Text/Pango only).

THE RECEIPT (ACTUAL-CODE LAW, option b): B05's balances and B08's cohort mix are parsed at render
time from `sql/*.out` — SQLite runs of the MySQL queries shown in B04/B07 (`sql/make_sqlite.py`
allows only four documented MySQL→SQLite swaps, disclosed on screen) against the book's Cascade
Savings ledger (`sql/cascade.sql`) and a generated Harborline sample (`sql/gen_harborline.py`).

Every scene carries the "Supriya" corner handle (PM requirement 4 / LOGO LAW) — `handle()`.
TIMING: DUR from beat_sheet.json (`actual_duration_s`); cues by word position in the narration.
"""
from manim import *
from pathlib import Path
import json, re
from collections import defaultdict
import numpy as np

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/banking-domain-interview-prep-week5-6-7/2026-08-31-banking-domain-interview-part1")
HERE = Path(__file__).resolve().parent
if not (HERE / "sql").is_dir():
    HERE = _REEL

CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
TEAL = "#1F6F5C"; CRIMSON = "#BF3339"; SEC = "#6B6357"; RULE = "#D9D4C7"
MONO = "PT Mono"

# ── data: the real query output ───────────────────────────────────────────────

def read_out(name):
    lines = [l for l in (HERE / "sql" / name).read_text().splitlines() if l.strip()]
    rule = lines[1]
    spans, i = [], 0
    while i < len(rule):
        if rule[i] == "-":
            j = i
            while j < len(rule) and rule[j] == "-":
                j += 1
            spans.append((i, j)); i = j
        else:
            i += 1
    cut = lambda l: [l[a:(spans[k + 1][0] if k + 1 < len(spans) else None)].strip()
                     for k, (a, _) in enumerate(spans)]
    head = cut(lines[0])
    return [dict(zip(head, cut(l))) for l in lines[2:]]


BALANCES = [(r["month_start"], float(r["eom_balance"])) for r in read_out("running_balance_fixed.out")]
POSTINGS = [(d, float(a)) for d, a in re.findall(r"\(\d+, \d+, '([\d-]+) [\d:]+', +(-?[\d.]+), '\w+'",
                                                   (HERE / "sql" / "cascade.sql").read_text())]
CARRIED = sum(a for d, a in POSTINGS if d < "2026-01-01")
ACCOUNT = int(re.search(r"INSERT INTO accounts VALUES \((\d+)", (HERE / "sql" / "cascade.sql").read_text()).group(1))

BUCKETS = ["current", "30", "60", "90+", "charge_off"]
VINTAGE = defaultdict(dict)                       # months_on_book -> bucket -> (count, pct)
for r in read_out("vintage_curve.out"):
    VINTAGE[int(r["months_on_book"])][r["dpd_bucket"]] = (int(r["accounts_in_bucket"]), float(r["pct_of_cohort"]))
MOBS = sorted(VINTAGE)
TOTALS = {m: sum(c for c, _ in VINTAGE[m].values()) for m in MOBS}
assert len(set(TOTALS.values())) == 1, "cohort total changed across months — check the fixture for duplicates"
COHORT_N = TOTALS[MOBS[0]]

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun",
          "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
mon = lambda iso: f"{MONTHS[iso[5:7]]} {iso[:4]}"
money = lambda v: ("−" if v < 0 else "") + f"${abs(v):,.2f}"

# ── timing ────────────────────────────────────────────────────────────────────

BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def _norm(w):
    return w.strip(".,:;!?\"'“”").lower()


def cue(bid, phrase):
    words = BEATS[bid]["narration_text"].split()
    target = phrase.split()
    for i in range(len(words) - len(target) + 1):
        if [_norm(w) for w in words[i:i + len(target)]] == [_norm(t) for t in target]:
            return dur(bid) * i / len(words)
    raise ValueError(f"{bid}: cue phrase not in narration: {phrase!r}")


def handle(scene):
    h = Text("Supriya", color=SEC, font_size=26, weight="BOLD").set_opacity(0.8)
    h.to_corner(DR, buff=0.9)
    scene.add(h)
    return h


class Clock:
    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = dur(bid)
        scene.camera.background_color = CREAM
        handle(scene)

    def run(self, *anims, rt=0.6):
        self.s.play(*anims, run_time=rt); self.t += rt

    def until(self, phrase):
        at = cue(self.bid, phrase)
        if at > self.t:
            self.s.wait(at - self.t); self.t = at

    def pad(self):
        self.s.wait(max(0.4, self.DUR - self.t - 0.2))


def checkmark(color=TEAL, size=0.34):
    mark = VMobject(color=color, stroke_width=7)
    mark.set_points_as_corners([np.array([-0.5, 0.05, 0]) * size, np.array([-0.1, -0.45, 0]) * size,
                                np.array([0.55, 0.5, 0]) * size])
    return mark


def chip(label, color, size=28, fill=0.12, w=None):
    t = Text(label, color=color, weight="BOLD", font_size=size)
    box = RoundedRectangle(corner_radius=0.3, width=w or t.width + 0.7, height=t.height + 0.45,
                           stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=fill)
    return VGroup(box, t.move_to(box))


def disclosure():
    return Text("real run: sql/ · SQLite (MySQL-only functions swapped)", font=MONO, color=SEC,
                font_size=18).to_corner(DL, buff=0.9)


# ── B01 — PROBLEM: the second language ────────────────────────────────────────

class B01_TheSecondLanguage(Scene):
    def construct(self):
        c = Clock(self, "B01")
        head = Text("You already have this.", color=INK, weight="BOLD", font_size=40).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), rt=0.5)
        base = VGroup(*[chip(s, TEAL, 30, 0.0) for s in ["joins", "cohorts", "dashboards"]]).arrange(RIGHT, buff=0.4).move_to([0, 1.75, 0])
        c.until("skills you already have")
        c.run(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in base], lag_ratio=0.25), rt=0.8)
        layer = Text("+ the layer banking adds", color=TERRACOTTA, weight="BOLD", font_size=30).move_to([0, 0.75, 0])
        regs = VGroup(*[chip(s, TERRACOTTA, 30) for s in ["OCC", "CFPB"]])
        ratios = VGroup(*[chip(s, TERRACOTTA, 30) for s in ["CET1", "LCR"]])
        row = VGroup(regs.arrange(RIGHT, buff=0.3), ratios.arrange(RIGHT, buff=0.3)).arrange(RIGHT, buff=1.0).move_to([0, -0.25, 0])
        sub = VGroup(Text("regulators", color=SEC, font_size=22).next_to(regs, DOWN, buff=0.15),
                     Text("ratios", color=SEC, font_size=22).next_to(ratios, DOWN, buff=0.15))
        c.until("second language")
        c.run(FadeIn(layer), rt=0.4)
        c.until("regulators like")
        c.run(FadeIn(regs, shift=DOWN * 0.3), FadeIn(sub[0]), rt=0.5)
        c.until("ratios like")
        c.run(FadeIn(ratios, shift=DOWN * 0.3), FadeIn(sub[1]), rt=0.5)
        qs = VGroup(chip("regulatory-reportable?", INK, 30, 0.06), chip("could it be fraud?", INK, 30, 0.06)).arrange(RIGHT, buff=0.5).move_to([0, -2.3, 0])
        c.until("regulatory-reportable")
        c.run(FadeIn(qs[0], shift=UP * 0.15), FadeIn(qs[1], shift=UP * 0.15), rt=0.5)
        c.pad()


# ── B02 — the book's six-part map (book.md:13-18) ─────────────────────────────

PARTS = [("I", "Banking\nLandscape", "banking landscape"), ("II", "Regulation\n& Risk", "regulation and risk"),
         ("III", "Data\nStack", "data stack"), ("IV", "Technical\nPrep", "technical prep"),
         ("V", "Behavioral,\nCase & Systems", "behavioral"), ("VI", "Day-Of", "day-of")]


class B02_SixPartMap(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = Text("Six parts", color=INK, weight="BOLD", font_size=44).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), rt=0.5)
        boxes = VGroup()
        for num, label, _ in PARTS:
            box = RoundedRectangle(corner_radius=0.12, width=1.95, height=3.4, color=TEAL, stroke_width=3.5,
                                   fill_color="#FFFFFF", fill_opacity=1)
            n = Text(num, color=TERRACOTTA, weight="BOLD", font_size=44)
            lb = VGroup(*[Text(x, color=INK, font_size=26) for x in label.split("\n")]).arrange(DOWN, buff=0.08)
            if lb.width > 1.75:
                lb.scale_to_fit_width(1.75)
            VGroup(n, lb).arrange(DOWN, buff=0.45).move_to(box)
            boxes.add(VGroup(box, n, lb))
        boxes.arrange(RIGHT, buff=0.2).move_to([0, 0.35, 0])
        sub = chip("Part IV: 40+ SQL problems · Python for banking", TERRACOTTA, 28).move_to([0, -2.35, 0])
        for k, ((_, _, word), b) in enumerate(zip(PARTS[:4], boxes[:4])):
            c.until(word)
            c.run(FadeIn(b, shift=UP * 0.2), *([FadeIn(sub)] if k == 3 else []), rt=0.4)
        c.until(PARTS[4][2])
        c.run(FadeIn(boxes[4], shift=UP * 0.2), FadeIn(boxes[5], shift=UP * 0.2), rt=0.5)
        c.pad()


# ── B05 / B08 — OUTPUT ────────────────────────────────────────────────────────

class B05_CorrectBalance(Scene):
    def construct(self):
        c = Clock(self, "B05")
        head = Text(f"Cascade Savings · account {ACCOUNT}", color=INK, weight="BOLD", font_size=36).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        carried = Text(f"carried into January: {money(CARRIED)}", color=TEAL, font_size=30).next_to(head, DOWN, buff=0.3)
        c.until("twelve thousand")
        c.run(FadeIn(carried), rt=0.4)
        hdr = VGroup(Text("Month", color=SEC, font_size=30).move_to([-2.2, 1.6, 0]),
                     Text("EOM balance", color=SEC, font_size=30).move_to([2.2, 1.6, 0]))
        rule = Line([-4.4, 1.2, 0], [4.4, 1.2, 0], color=RULE, stroke_width=3)
        body = VGroup(*[VGroup(Text(mon(m), color=INK, font_size=40).move_to([-2.2, 0.6 - k * 0.85, 0]),
                               Text(money(v), font=MONO, color=TEAL, font_size=44, weight="BOLD").move_to([2.2, 0.6 - k * 0.85, 0]))
                        for k, (m, v) in enumerate(BALANCES)])
        c.until("month-end balances")
        c.run(FadeIn(hdr), Create(rule), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in body], lag_ratio=0.3), rt=1.0)
        c.until("true ones")
        b = chip("Sum first. Filter after.", TEAL, 32, 0.08).move_to([0, -2.25, 0])
        c.run(FadeIn(b, scale=0.95), rt=0.4)
        c.pad()


class B08_VintageCurve(Scene):
    def construct(self):
        c = Clock(self, "B08")
        head = Text("Harborline Card Co. — Jan 2025 sample cohort", color=INK, weight="BOLD", font_size=34).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        colors = [interpolate_color(ManimColor(TEAL), ManimColor(CRIMSON), i / (len(BUCKETS) - 1)) for i in range(len(BUCKETS))]
        bar_h, bar_w, base_y = 3.3, 2.2, -1.45
        xs = [-3.9, 0.0, 3.9]
        cols = VGroup(); labels = VGroup(); pcts = VGroup()
        for x, m in zip(xs, MOBS):
            segs, y = VGroup(), base_y
            for b, col in zip(BUCKETS, colors):
                n, p = VINTAGE[m].get(b, (0, 0.0))
                if n == 0:
                    continue
                h = bar_h * n / COHORT_N
                segs.add(Rectangle(width=bar_w, height=h, stroke_width=1, stroke_color=CREAM, fill_color=col,
                                   fill_opacity=0.95).move_to([x, y + h / 2, 0]))
                y += h
            cols.add(segs)
            labels.add(Text(f"month {m}", color=INK, weight="BOLD", font_size=30).move_to([x, base_y - 0.4, 0]))
            cur = VINTAGE[m]["current"][1]
            p90, pco = (VINTAGE[m].get(b, (0, 0.0))[1] for b in ("90+", "charge_off"))
            pcts.add(Text(f"{cur:g}% current · {p90:g}% 90+ · {pco:g}% c-o", color=SEC, font_size=19).move_to([x, base_y + bar_h + 0.3, 0]))
        c.until("month three")
        c.run(GrowFromEdge(cols[0], DOWN), FadeIn(labels[0]), FadeIn(pcts[0]), rt=0.6)
        c.run(GrowFromEdge(cols[1], DOWN), FadeIn(labels[1]), FadeIn(pcts[1]), rt=0.6)
        c.until("month nine")
        c.run(GrowFromEdge(cols[2], DOWN), FadeIn(labels[2]), FadeIn(pcts[2]), rt=0.6)
        legend = VGroup(*[VGroup(Square(side_length=0.3, fill_color=col, fill_opacity=0.95, stroke_width=0),
                                 Text(b, color=SEC, font_size=22)).arrange(RIGHT, buff=0.12) for b, col in zip(BUCKETS, colors)]
                        ).arrange(RIGHT, buff=0.45).move_to([0, base_y - 0.95, 0])
        c.run(FadeIn(legend), rt=0.4)
        c.until("each column adds back")
        ns = VGroup(*[Text(f"n = {TOTALS[m]}", color=TEAL, font_size=24, weight="BOLD").next_to(pcts[k], UP, buff=0.12) for k, m in enumerate(MOBS)])
        c.run(LaggedStart(*[FadeIn(n) for n in ns], lag_ratio=0.2), rt=0.6)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_TwoMoves(Scene):
    def construct(self):
        c = Clock(self, "B09")
        head = Text("Two moves", color=INK, weight="BOLD", font_size=52).move_to([-3.9, 2.75, 0])
        bar = Line(head.get_corner(DL) + DOWN * 0.15, head.get_corner(DR) + DOWN * 0.15, color=TERRACOTTA, stroke_width=7)
        c.run(FadeIn(head), Create(bar), rt=0.5)
        rows = VGroup()
        for t in ["Get the SQL evaluation order right", "Never lose the cohort"]:
            txt = Text(t, color=INK, font_size=46)
            rows.add(VGroup(checkmark(size=0.55).next_to(txt, LEFT, buff=0.4), txt))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(bar, DOWN, buff=0.6).align_to(head, LEFT).shift(RIGHT * 0.6)
        for r, w in zip(rows, ["evaluation order", "never lose the cohort"]):
            c.until(w)
            c.run(Create(r[0]), FadeIn(r[1], shift=RIGHT * 0.15), rt=0.5)
        rest = Text("the rest of the book →", color=SEC, font_size=30, slant="ITALIC").next_to(rows, DOWN, buff=0.55).align_to(head, LEFT)
        chips = VGroup(*[chip(s, TEAL, 26, 0.0) for s in ["regulatory metrics", "data stack", "behavioral & case rounds"]]
                       ).arrange(RIGHT, buff=0.3).next_to(rest, DOWN, buff=0.3).align_to(head, LEFT)
        c.until("the rest of the book")
        c.run(FadeIn(rest), LaggedStart(*[FadeIn(x, shift=UP * 0.1) for x in chips], lag_ratio=0.25), rt=0.9)
        c.pad()
