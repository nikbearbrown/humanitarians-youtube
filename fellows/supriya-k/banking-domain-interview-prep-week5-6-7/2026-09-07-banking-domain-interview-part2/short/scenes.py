"""scenes.py — portrait (9:16) Manim scenes for banking-domain-sql-running-total-bug/short.
Full-length short (no beats cut): all 5 Manim beats re-laid-out for portrait — B01, B02, B05,
B08, B09. Not shrunk copies: the portrait frame is narrow in x (frame_width=4.5, Gate B safe
±1.95) and unchanged in y (frame_height=8.0, safe ±3.4), so every layout is restacked vertically.

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the same postings
parsed from ../sql/cascade.sql, the same balances from ../sql/*.out, the same measured audio
durations and narration cues. Scene classes must be plain Scene subclasses named B0X_Name.
"""
from manim import *
from pathlib import Path
import importlib.util

config.frame_width = 4.5
config.frame_height = 8.0

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/banking-domain-interview-prep-week5-6-7/2026-09-07-banking-domain-interview-part2")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "sql").is_dir():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

CREAM, INK, TERRACOTTA, TEAL, CRIMSON, SEC, RULE, MONO = L.CREAM, L.INK, L.TERRACOTTA, L.TEAL, L.CRIMSON, L.SEC, L.RULE, L.MONO
POSTINGS, ACCOUNT, WINDOW_START, BUGGY, FIXED, CARRIED = L.POSTINGS, L.ACCOUNT, L.WINDOW_START, L.BUGGY, L.FIXED, L.CARRIED
mon, money = L.mon, L.money
SAFE_X = 1.95


def handle(scene):
    h = Text("Supriya", color=SEC, font_size=18, weight="BOLD").set_opacity(0.8)
    h.move_to([SAFE_X - 0.05, -3.22, 0], aligned_edge=RIGHT)
    scene.add(h)
    return h


class Clock(L.Clock):
    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = L.dur(bid)
        scene.camera.background_color = CREAM
        handle(scene)


def fit(m, w):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def lines(texts, size, color=INK, bold=True, buff=0.08):
    return VGroup(*[Text(t, color=color, font_size=size, weight="BOLD" if bold else "NORMAL") for t in texts]).arrange(DOWN, buff=buff)


def badge(text_lines, color, size=20):
    t = lines(text_lines, size, color)
    box = RoundedRectangle(corner_radius=0.1, width=min(t.width + 0.4, 3.9), height=t.height + 0.32,
                           stroke_color=color, stroke_width=3, fill_color=color, fill_opacity=0.08)
    fit(t, box.width - 0.3)
    return VGroup(box, t.move_to(box))


def disclosure():
    return fit(Text("real run: sql/ · SQLite (DATE_FORMAT → strftime)", font=MONO, color=SEC, font_size=13), 3.8).move_to([0, -2.85, 0])


class B01_RunningBalanceStakes(Scene):
    def construct(self):
        c = Clock(self, "B01")
        head = lines(["“What's the", "balance today?”"], 30).move_to([0, 3.0, 0])
        sub = fit(Text("= the sum of every posting up to today", color=SEC, font_size=18), 3.8).next_to(head, DOWN, buff=0.15)
        c.run(FadeIn(head), FadeIn(sub), rt=0.8)
        cards, run = VGroup(), 0.0
        for k, (_, _, d, amt, kind) in enumerate(POSTINGS):
            run += amt
            top = Text(f"{d} · {kind}", font=MONO, font_size=18, color=INK)
            bot = Text(f"{money(amt)}  →  {money(run)}", font=MONO, font_size=20, color=TEAL, weight="BOLD")
            g = VGroup(top, bot).arrange(DOWN, buff=0.06, aligned_edge=LEFT).move_to([-1.8, 1.55 - k * 0.82, 0], aligned_edge=LEFT)
            cards.add(g)
        c.until("get that running total right")
        c.run(LaggedStart(*[FadeIn(g, shift=UP * 0.1) for g in cards], lag_ratio=0.3), rt=1.6)
        c.until("one clause out of order")
        y = (cards[0].get_bottom()[1] + cards[1].get_top()[1]) / 2
        cut = DashedLine([-1.9, y, 0], [1.9, y, 0], color=CRIMSON, stroke_width=3)
        tag = fit(Text(f"- - -  window starts {WINDOW_START}", color=CRIMSON, font_size=18), 3.8).move_to([0, -1.85, 0])
        c.run(Create(cut), FadeIn(tag), rt=0.6)
        c.run(VGroup(*[g for g, p in zip(cards, POSTINGS) if p[2] < WINDOW_START]).animate.set_opacity(0.28), rt=0.6)
        c.until("still runs")
        c.run(FadeIn(badge(["No error.", "No warning."], CRIMSON, 24).move_to([0, -2.6, 0]), scale=0.95), rt=0.5)
        c.pad()


class B02_FilterOrderSplit(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = lines(["Inside one query,", "WHERE runs before", "SUM() OVER"], 24).move_to([0, 2.9, 0])
        c.run(FadeIn(head), rt=0.5)
        name = Text("WITH running AS ( … )", font=MONO, font_size=16, color=SEC).move_to([-1.85, 1.95, 0], aligned_edge=LEFT)
        steps = VGroup(*[Text(s, font=MONO, font_size=18, color=INK, weight="BOLD")
                         for s in ["FROM transactions", f"WHERE posted_at >=", f"  '{WINDOW_START}'", "SUM(amount) OVER (…)"]])
        steps.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fit(steps, 3.4).move_to([0, 0.75, 0])
        box = SurroundingRectangle(steps, color=INK, buff=0.22, corner_radius=0.12, stroke_width=3)
        c.until("a window function runs after where")
        c.run(Create(box), FadeIn(name), LaggedStart(*[FadeIn(s) for s in steps], lag_ratio=0.3), rt=1.2)
        chips = VGroup(*[Text(f"{d}  {money(a)}", font=MONO, font_size=18, color=INK) for _, _, d, a, _ in POSTINGS]
                       ).arrange(DOWN, buff=0.14).move_to([0, -1.2, 0])
        c.until("the sum only sees")
        c.run(FadeIn(chips), rt=0.5)
        dropped = VGroup(*[ch for ch, p in zip(chips, POSTINGS) if p[2] < WINDOW_START])
        kept = VGroup(*[ch for ch, p in zip(chips, POSTINGS) if p[2] >= WINDOW_START])
        rect = VGroup(*[SurroundingRectangle(ch, color=CRIMSON, buff=0.06, stroke_width=3) for ch in dropped])
        c.run(Create(rect), dropped.animate.set_color(CRIMSON), rt=0.5)
        c.until("everything posted before")
        c.run(kept.animate.set_color(TEAL), FadeOut(VGroup(dropped, rect), shift=LEFT * 0.3), rt=0.6)
        gone = lines([f"{money(CARRIED)} of history", "never reaches the sum"], 20, CRIMSON).move_to([0, -2.6, 0])
        c.run(FadeIn(gone), rt=0.4)
        c.pad()


def table(rows, color):
    hdr = VGroup(Text("Month", color=SEC, font_size=18), Text("EOM balance", color=SEC, font_size=18))
    hdr[0].move_to([-1.0, 1.2, 0]); hdr[1].move_to([0.95, 1.2, 0])
    rule = Line([-1.9, 0.98, 0], [1.9, 0.98, 0], color=RULE, stroke_width=2)
    body = VGroup()
    for k, (m, v) in enumerate(rows):
        y = 0.6 - k * 0.6
        body.add(VGroup(Text(mon(m), color=INK, font_size=22).move_to([-1.0, y, 0]),
                        Text(money(v), font=MONO, color=color, font_size=24, weight="BOLD").move_to([0.95, y, 0])))
    return hdr, rule, body


class B05_TruncatedBalance(Scene):
    def construct(self):
        c = Clock(self, "B05")
        head = lines(["Cascade Savings", f"account {ACCOUNT}", "buggy query"], 22).move_to([0, 2.85, 0])
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        carried = fit(Text(f"carried into January: {money(CARRIED)}", color=TEAL, font_size=18), 3.8).move_to([0, 1.75, 0])
        c.until("twelve thousand")
        c.run(FadeIn(carried), rt=0.4)
        hdr, rule, body = table(BUGGY, CRIMSON)
        c.until("the query says")
        c.run(FadeIn(hdr), Create(rule), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in body], lag_ratio=0.3), rt=1.0)
        c.until("net change")
        c.run(FadeIn(badge(["not a balance —", "the net change", "since January"], CRIMSON, 20).move_to([0, -1.75, 0]), scale=0.95), rt=0.5)
        c.pad()


class B08_CorrectedBalance(Scene):
    def construct(self):
        c = Clock(self, "B08")
        head = lines(["Cascade Savings", f"account {ACCOUNT}", "fixed query"], 22).move_to([0, 2.85, 0])
        c.run(FadeIn(head), FadeIn(disclosure()), rt=0.5)
        hdr, rule, body = table(FIXED, TEAL)
        c.until("run it again")
        c.run(FadeIn(hdr), Create(rule), LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in body], lag_ratio=0.3), rt=1.0)
        jan = sum(a for _, _, d, a, _ in POSTINGS if d.startswith(FIXED[0][0][:7]))
        math = fit(Text(f"{money(CARRIED)} {'−' if jan < 0 else '+'} {money(abs(jan))} = {money(FIXED[0][1])}",
                        font=MONO, color=TEAL, font_size=18), 3.8).move_to([0, -1.25, 0])
        c.until("minus the one")
        c.run(FadeIn(math), rt=0.4)
        c.until("nothing invented")
        c.run(FadeIn(badge(["Nothing invented.", "Nothing lost."], TEAL, 22).move_to([0, -2.1, 0]), scale=0.95), rt=0.4)
        c.pad()


class B09_TheLesson(Scene):
    def construct(self):
        c = Clock(self, "B09")
        head = Text("The lesson", color=INK, weight="BOLD", font_size=32).move_to([0, 2.9, 0])
        bar = Line(head.get_corner(DL) + DOWN * 0.1, head.get_corner(DR) + DOWN * 0.1, color=TERRACOTTA, stroke_width=5)
        c.run(FadeIn(head), Create(bar), rt=0.5)
        items = VGroup()
        for k, ls in enumerate([["The bug was a filter", "applied before the sum."],
                                ["Run the total over", "the whole ledger first."],
                                ["Narrow to the reporting", "window after."]]):
            t = VGroup(*[Text(x, color=INK, font_size=22) for x in ls]).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            t.move_to([-1.45, 1.6 - k * 1.45, 0], aligned_edge=LEFT + UP)
            items.add(VGroup(L.checkmark(size=0.24).next_to(t, LEFT, buff=0.15).align_to(t, UP).shift(DOWN * 0.05), t))
        for it, w in zip(items, ["filter applied", "compute the running total", "narrow to"]):
            c.until(w)
            c.run(Create(it[0]), FadeIn(it[1], shift=RIGHT * 0.1), rt=0.5)
        c.pad()
