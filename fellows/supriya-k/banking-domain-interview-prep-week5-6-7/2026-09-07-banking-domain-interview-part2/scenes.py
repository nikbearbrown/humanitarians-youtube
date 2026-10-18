"""scenes.py — Manim scenes for banking-domain-sql-running-total-bug (cli-explainer) — v3.
5 output beats (B01, B02, B05, B08, B09); the other 7 render via Remotion.
Claude-skin palette: cream ground, warm ink, one terracotta accent, plus a functional
teal/crimson pair for right/wrong data (never swapped).
Scene classes must be declared as plain Scene subclasses named B0X_Name — run.sh finds them by regex.
No LaTeX (Text/Pango only).

THE RECEIPT (ACTUAL-CODE LAW, option b): every posting and balance on screen is parsed at render
time — postings from `sql/cascade.sql` (the book's Cascade Savings schema), balances from
`sql/*.out`, the SQLite run of the MySQL queries shown in B04/B07 (`sql/make_sqlite.py` swaps
only DATE_FORMAT -> strftime, disclosed on screen in B05/B08). Nothing is typed in by hand.

Every scene carries the "Supriya" corner handle (PM requirement 4 / LOGO LAW) — `handle()`.

TIMING: DUR is read from beat_sheet.json — `actual_duration_s` once audio exists,
`estimated_duration_s` before. Narration cues are placed by the cue phrase's word position in
that beat's narration_text, scaled to DUR, so regenerated audio re-times the scenes.
"""
from manim import *
from pathlib import Path
import json, re
import numpy as np

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/banking-domain-interview-prep-week5-6-7/2026-09-07-banking-domain-interview-part2")
HERE = Path(__file__).resolve().parent
if not (HERE / "sql").is_dir():
    HERE = _REEL

CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
TEAL = "#1F6F5C"; CRIMSON = "#BF3339"; SEC = "#6B6357"; RULE = "#D9D4C7"
MONO = "PT Mono"

# ── data: the fixture and the real query output ───────────────────────────────

POSTINGS = [(int(i), int(a), d, float(amt), kind) for i, a, d, amt, kind in re.findall(
    r"\((\d+), (\d+), '([\d-]+) [\d:]+', +(-?[\d.]+), '(\w+)'", (HERE / "sql" / "cascade.sql").read_text())]
ACCOUNT = POSTINGS[0][1]
WINDOW_START = "2026-01-01"


def read_out(name):
    """Parse a sqlite3 `-header -column` .out file into a list of dicts."""
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


BUGGY = [(r["month_start"], float(r["eom_balance"])) for r in read_out("running_balance_buggy.out")]
FIXED = [(r["month_start"], float(r["eom_balance"])) for r in read_out("running_balance_fixed.out")]
CARRIED = sum(a for _, _, d, a, _ in POSTINGS if d < WINDOW_START)       # history before the window
assert FIXED[0][1] - BUGGY[0][1] == CARRIED, "fixture no longer shows the dropped history"

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun",
          "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
mon = lambda iso: f"{MONTHS[iso[5:7]]} {iso[:4]}"
money = lambda v: ("−" if v < 0 else "") + f"${abs(v):,.2f}"

# ── timing: from the beat sheet ───────────────────────────────────────────────

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
    """A vector checkmark (a real shape, so Gate A sees it change)."""
    mark = VMobject(color=color, stroke_width=7)
    mark.set_points_as_corners([np.array([-0.5, 0.05, 0]) * size, np.array([-0.1, -0.45, 0]) * size,
                                np.array([0.55, 0.5, 0]) * size])
    return mark


def badge(text, color, size=30):
    t = Text(text, color=color, font_size=size, weight="BOLD")
    box = RoundedRectangle(corner_radius=0.12, width=t.width + 0.7, height=t.height + 0.42,
                           stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=0.08)
    return VGroup(box, t.move_to(box))


def disclosure():
    return Text(f"real run: sql/ · SQLite (DATE_FORMAT → strftime)", font=MONO, color=SEC,
                font_size=20).to_corner(DL, buff=0.9)


# ── B01 — PROBLEM: the balance is the sum of every posting ────────────────────

class B01_RunningBalanceStakes(Scene):
    def construct(self):
        c = Clock(self, "B01")
        head = Text("“What's the balance today?”", color=INK, weight="BOLD", font_size=44).to_edge(UP, buff=0.75)
        sub = Text("= the sum of every posting up to today", color=SEC, font_size=28).next_to(head, DOWN, buff=0.22)
        c.run(FadeIn(head), FadeIn(sub, shift=UP * 0.15), rt=0.8)

        rows, run = VGroup(), 0.0
        for k, (_, _, d, amt, kind) in enumerate(POSTINGS):
            run += amt
            pre = d < WINDOW_START
            row = VGroup(Text(d, font=MONO, font_size=28, color=INK),
                         Text(f"{kind}", font=MONO, font_size=28, color=SEC),
                         Text(money(amt), font=MONO, font_size=28, color=INK),
                         Text(money(run), font=MONO, font_size=28, color=TEAL, weight="BOLD"))
            for j, x in enumerate([-5.9, -2.85, 0.1, 2.85]):
                row[j].move_to([x, 1.0 - k * 0.88, 0], aligned_edge=LEFT)
            rows.add(row)
        hdr = VGroup(*[Text(s, font=MONO, font_size=22, color=SEC).move_to([x, 1.75, 0], aligned_edge=LEFT)
                       for s, x in zip(["posted_at", "type", "amount", "running balance"], [-5.9, -2.85, 0.1, 2.85])])
        c.until("get that running total right")
        c.run(FadeIn(hdr), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rows], lag_ratio=0.3), rt=1.6)

        c.until("one clause out of order")
        boundary_y = 1.0 - 0.5 * 0.88
        cutline = DashedLine([-6.0, boundary_y, 0], [6.0, boundary_y, 0], color=CRIMSON, stroke_width=4)
        tag = Text(f"- - -  reporting window starts {WINDOW_START}", color=CRIMSON, font_size=24).move_to([0, -2.3, 0])
        c.run(Create(cutline), FadeIn(tag), rt=0.6)
        pre_rows = VGroup(*[r for r, p in zip(rows, POSTINGS) if p[2] < WINDOW_START])
        c.run(pre_rows.animate.set_opacity(0.28), rt=0.6)
        c.until("still runs")
        note = badge("No error. No warning.", CRIMSON, 32).move_to([0, -2.95, 0])
        c.run(FadeIn(note, scale=0.95), rt=0.5)
        c.pad()


# ── B02 — the rule: inside ONE query, WHERE runs before SUM() OVER ─────────────

class B02_FilterOrderSplit(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = Text("Inside one query, WHERE runs before SUM() OVER", color=INK, weight="BOLD", font_size=36).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), rt=0.5)

        cte = RoundedRectangle(corner_radius=0.18, width=12.4, height=4.3, stroke_color=INK, stroke_width=3,
                               fill_color="#FFFFFF", fill_opacity=1).move_to([0, -0.55, 0])
        name = Text("WITH running AS ( … )", font=MONO, font_size=26, color=SEC).next_to(cte, UP, buff=0.12).align_to(cte, LEFT)
        steps = VGroup(*[Text(s, font=MONO, font_size=26, color=INK, weight="BOLD")
                         for s in ["FROM transactions", f"WHERE posted_at >= '{WINDOW_START}'", "SUM(amount) OVER (…)"]])
        for k, s in enumerate(steps):
            s.move_to([-5.7, 0.95 - k * 1.35, 0], aligned_edge=LEFT)
        arrows = VGroup(*[Arrow(steps[k].get_bottom() + DOWN * 0.05 + RIGHT * 0.3 - RIGHT * (steps[k].width / 2 - 0.3),
                                steps[k + 1].get_top() + UP * 0.05 + RIGHT * 0.3 - RIGHT * (steps[k + 1].width / 2 - 0.3),
                                buff=0, color=SEC, stroke_width=4) for k in range(2)])
        c.until("a window function runs after where")
        c.run(Create(cte), FadeIn(name), FadeIn(steps[0]), rt=0.6)
        c.run(GrowArrow(arrows[0]), FadeIn(steps[1]), rt=0.5)
        c.run(GrowArrow(arrows[1]), FadeIn(steps[2]), rt=0.5)

        chips = VGroup()
        for k, (_, _, d, amt, _) in enumerate(POSTINGS):
            chip = Text(f"{d}  {money(amt)}", font=MONO, font_size=24, color=INK)
            chip.move_to([3.95, 1.15 - k * 0.6, 0])
            chips.add(chip)
        c.until("the sum only sees")
        c.run(FadeIn(chips), rt=0.5)
        dropped = VGroup(*[ch for ch, p in zip(chips, POSTINGS) if p[2] < WINDOW_START])
        kept = VGroup(*[ch for ch, p in zip(chips, POSTINGS) if p[2] >= WINDOW_START])
        strike = VGroup(*[SurroundingRectangle(ch, color=CRIMSON, buff=0.1, stroke_width=4) for ch in dropped])
        c.run(Create(strike), dropped.animate.set_color(CRIMSON), rt=0.5)
        c.until("everything posted before")
        c.run(kept.animate.set_color(TEAL), FadeOut(VGroup(dropped, strike), shift=LEFT * 0.4), rt=0.6)
        gone = Text(f"{money(CARRIED)} of history never reaches the sum", color=CRIMSON, font_size=28, weight="BOLD")
        gone.next_to(cte, DOWN, buff=0.3)
        c.run(FadeIn(gone), rt=0.4)
        c.pad()


# ── B05 / B08 — OUTPUT: the end-of-month balances that come back ──────────────

def balance_table(rows, color):
    hdr = VGroup(Text("Month", color=SEC, font_size=30), Text("EOM balance", color=SEC, font_size=30))
    hdr[0].move_to([-2.2, 1.75, 0]); hdr[1].move_to([2.2, 1.75, 0])
    rule = Line([-4.4, 1.35, 0], [4.4, 1.35, 0], color=RULE, stroke_width=3)
    body = VGroup()
    for k, (m, v) in enumerate(rows):
        y = 0.8 - k * 0.8
        body.add(VGroup(Text(mon(m), color=INK, font_size=38).move_to([-2.2, y, 0]),
                        Text(money(v), font=MONO, color=color, font_size=42, weight="BOLD").move_to([2.2, y, 0])))
    return hdr, rule, body


class B05_TruncatedBalance(Scene):
    def construct(self):
        c = Clock(self, "B05")
        head = Text(f"Cascade Savings · account {ACCOUNT} — buggy query", color=INK, weight="BOLD", font_size=34).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        carried = Text(f"carried into January: {money(CARRIED)}", color=TEAL, font_size=30).next_to(head, DOWN, buff=0.3)
        c.until("twelve thousand")
        c.run(FadeIn(carried), rt=0.4)
        hdr, rule, body = balance_table(BUGGY, CRIMSON)
        c.until("the query says")
        c.run(FadeIn(hdr), Create(rule), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in body], lag_ratio=0.3), rt=1.0)
        c.until("net change")
        b = badge("not a balance — the net change since January", CRIMSON, 30).move_to([0, -2.05, 0])
        c.run(FadeIn(b, scale=0.95), rt=0.5)
        c.pad()


class B08_CorrectedBalance(Scene):
    def construct(self):
        c = Clock(self, "B08")
        head = Text(f"Cascade Savings · account {ACCOUNT} — fixed query", color=INK, weight="BOLD", font_size=34).to_edge(UP, buff=0.75)
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        hdr, rule, body = balance_table(FIXED, TEAL)
        c.until("run it again")
        c.run(FadeIn(hdr), Create(rule), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in body], lag_ratio=0.3), rt=1.0)
        jan_wd = sum(a for _, _, d, a, _ in POSTINGS if d.startswith(FIXED[0][0][:7]))
        math = Text(f"{money(CARRIED)} {'−' if jan_wd < 0 else '+'} {money(abs(jan_wd))} = {money(FIXED[0][1])}",
                    font=MONO, color=TEAL, font_size=30).next_to(body, DOWN, buff=0.35)
        c.until("minus the one")
        c.run(FadeIn(math), rt=0.4)
        c.until("nothing invented")
        b = badge("Nothing invented. Nothing lost.", TEAL, 30).move_to([0, -2.4, 0])
        c.run(FadeIn(b, scale=0.95), rt=0.4)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_TheLesson(Scene):
    def construct(self):
        c = Clock(self, "B09")
        head = Text("The lesson", color=INK, weight="BOLD", font_size=46).to_edge(UP, buff=0.75)
        bar = Line(head.get_corner(DL) + DOWN * 0.15, head.get_corner(DR) + DOWN * 0.15, color=TERRACOTTA, stroke_width=6)
        c.run(FadeIn(head), Create(bar), rt=0.5)
        lines = ["The bug was a filter applied before the sum.",
                 "Run the total over the whole ledger first.",
                 "Narrow to the reporting window after."]
        cues = ["filter applied", "compute the running total", "narrow to"]
        items = VGroup()
        for k, l in enumerate(lines):
            t = Text(l, color=INK, font_size=38).move_to([-5.0, 1.15 - k * 1.25, 0], aligned_edge=LEFT)
            items.add(VGroup(checkmark().next_to(t, LEFT, buff=0.35), t))
        for it, w in zip(items, cues):
            c.until(w)
            c.run(Create(it[0]), FadeIn(it[1], shift=RIGHT * 0.1), rt=0.5)
        c.pad()
