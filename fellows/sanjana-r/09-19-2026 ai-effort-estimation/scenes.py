# -*- coding: utf-8 -*-
"""
Manim output scenes for the AI Effort Estimation reel.
  B01_GutGuess   -- the gut sprint total vs where similar work actually landed
  B02_Method     -- reference-class forecasting: 4 steps (framework, shown first)
  B05_PointPlan  -- v1 output: three single-point estimates, total 10, false precision
  B08_Ranges     -- v2 output: P50-P80 ranges, gut on the optimistic edge, 10 -> ~19,
                    plus the no-reference-class edge case (falsifiability, shown)
  B09_Summary    -- the reusable 3-question rubric + the honest-unknown rule
Claude fidelity palette (cream ground, warm ink, one terracotta accent).
Every number is computed here from one seed-locked dataset, so the reel agrees
with its own CODE beats (estimate.py v1/v2).
"""
import numpy as np
from manim import *

PALETTE = {
    "bg":      "#FAF9F5",   # cream
    "ink":     "#3D3929",   # warm ink
    "accent":  "#D97757",   # terracotta (the ONE accent)
    "muted":   "#B7AE9E",   # dim
    "good":    "#4A7C59",   # green
    "panel":   "#EFEBE1",   # soft panel
}

# ---- one shared dataset (matches estimate.py in the CODE beats) --------------
CLASSES = {
    "integration": [4, 6, 7, 9, 14],   # OAuth-shaped work: fat tail
    "ui_form":     [1, 2, 2, 3],       # a settings page
    "crud":        [2, 3, 3, 4, 6],    # a plain endpoint
}
VELOCITY = 1.15
# (label, class, gut single-point estimate)
TASKS = [
    ("OAuth login",     "integration", 5),
    ("Settings page",   "ui_form",     2),
    ("Export endpoint", "crud",        3),
]

def rng_of(cls):
    a = np.array(CLASSES[cls], float)
    p50, p80 = np.percentile(a, [50, 80]) * VELOCITY
    return round(float(p50), 1), round(float(p80), 1)

GUT_TOTAL = sum(g for _, _, g in TASKS)                     # 10
P80_TOTAL = sum(rng_of(c)[1] for _, c, _ in TASKS)          # ~19.3


def title_text(s, fs=40):
    return Text(s, font="DejaVu Serif", color=PALETTE["ink"],
                font_size=fs, weight=BOLD).to_edge(UP, buff=0.5)


# =============================================================== B01 PROBLEM ==
class B01_GutGuess(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = title_text("A gut number ignores your history")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        # the confident gut plan
        plan_eq = Text("5 + 2 + 3  =  10 days", font="DejaVu Sans",
                       color=PALETTE["ink"], font_size=44, weight=BOLD).move_to([0, 1.9, 0])
        sub = Text("the sprint plan: one best guess per task, added up",
                   font="DejaVu Sans", color=PALETTE["muted"],
                   font_size=24).next_to(plan_eq, DOWN, buff=0.22)
        self.play(Write(plan_eq), run_time=1.1)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(3.2)   # "we picture it going well... ten days"

        # day axis for the cloud of what similar sprints actually took
        DMIN, DMAX = 4, 26
        XL, XW, BASE = -6.0, 12.0, -2.7
        def x_of(d): return XL + (d - DMIN) / (DMAX - DMIN) * XW
        ax = Line([XL - 0.3, BASE, 0], [XL + XW + 0.3, BASE, 0],
                  color=PALETTE["ink"], stroke_width=3)
        cap = Text("similar sprints, actual days", font="DejaVu Sans",
                   color=PALETTE["muted"], font_size=22).next_to(ax, DOWN, buff=0.72)
        ticks = VGroup()
        for d in range(5, 27, 5):
            t = Line([x_of(d), BASE, 0], [x_of(d), BASE - 0.13, 0],
                     color=PALETTE["ink"], stroke_width=3)
            l = Text(str(d), font="DejaVu Sans", color=PALETTE["ink"],
                     font_size=19).next_to(t, DOWN, buff=0.1)
            ticks.add(t, l)
        self.play(plan_eq.animate.scale(0.62).move_to([0, 2.55, 0]),
                  FadeOut(sub), Create(ax), FadeIn(ticks), FadeIn(cap), run_time=1.0)

        # gut marker at 10 -- sits on the optimistic edge
        gx = x_of(GUT_TOTAL)
        gut_ln = DashedLine([gx, BASE, 0], [gx, BASE + 3.9, 0],
                            color=PALETTE["ink"], stroke_width=5)
        gut_lbl = Text("your plan: 10", font="DejaVu Sans", color=PALETTE["ink"],
                       font_size=24, weight=BOLD)
        gut_lbl.next_to([gx, BASE + 3.9, 0], UP, buff=0.12).shift(LEFT * 0.7)
        self.play(Create(gut_ln), FadeIn(gut_lbl), run_time=0.8)
        self.wait(2.0)

        # cloud: many sprints = sum of one actual per class * velocity
        rs = np.random.RandomState(7)
        sums = (rs.choice(CLASSES["integration"], 2200)
                + rs.choice(CLASSES["ui_form"], 2200)
                + rs.choice(CLASSES["crud"], 2200)) * VELOCITY
        counts, edges = np.histogram(sums, bins=np.arange(DMIN, DMAX + 1, 1))
        m = counts.max()
        bw = (XW / (DMAX - DMIN)) * 0.9
        bars = VGroup()
        for c, left in zip(counts, edges[:-1]):
            h = max((c / m) * 3.6, 0.001)
            b = Rectangle(width=bw, height=h, stroke_width=0,
                          fill_color=PALETTE["accent"], fill_opacity=0.8)
            b.move_to([x_of(left + 0.5), BASE + h / 2, 0])
            bars.add(b)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                              lag_ratio=0.03, run_time=5.0))
        self.wait(1.6)   # "the same kind of work, last time"

        # clear the plan equation so the punch line owns the top band (no overlap)
        self.play(FadeOut(plan_eq), run_time=0.4)
        note = Text("the same work, last time: usually LATER than the plan",
                    font="DejaVu Sans", color=PALETTE["accent"], font_size=27,
                    weight=BOLD).move_to([0, 2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.2), run_time=1.0)
        self.wait(4.2)   # "the planning fallacy", held


# ============================================================= B02 FRAMEWORK ==
class B02_Method(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = title_text("Reference-class forecasting - four steps")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        steps = [
            ("1", "DESCRIBE", "what kind of\nwork is this,\nreally?"),
            ("2", "MATCH", "find similar\ntasks you've\nalready finished"),
            ("3", "DISTRIBUTION", "what they\nACTUALLY took,\nnot the hope"),
            ("4", "CALIBRATE", "adjust for\nvelocity ->\na range"),
        ]
        cards = VGroup()
        for num, head, body in steps:
            box = RoundedRectangle(corner_radius=0.14, width=2.9, height=3.0,
                                   stroke_color=PALETTE["muted"], stroke_width=2,
                                   fill_color=PALETTE["panel"], fill_opacity=1.0)
            n = Text(num, font="DejaVu Serif", color=PALETTE["accent"],
                     font_size=44, weight=BOLD).move_to(box.get_top() + DOWN * 0.55)
            h = Text(head, font="DejaVu Sans", color=PALETTE["ink"],
                     font_size=23, weight=BOLD).move_to(box.get_center() + UP * 0.35)
            b = Text(body, font="DejaVu Sans", color=PALETTE["muted"],
                     font_size=19, line_spacing=0.8).move_to(box.get_center() + DOWN * 0.78)
            cards.add(VGroup(box, n, h, b))
        cards.arrange(RIGHT, buff=0.5).move_to([0, -0.3, 0])

        arrows = VGroup()
        for i in range(3):
            a = Arrow(cards[i].get_right(), cards[i + 1].get_left(),
                      buff=0.08, color=PALETTE["ink"], stroke_width=4,
                      max_tip_length_to_length_ratio=0.4)
            arrows.add(a)

        for i, card in enumerate(cards):
            box = card[0]
            self.play(FadeIn(card, shift=UP * 0.2),
                      box.animate.set_stroke(PALETTE["accent"], width=4), run_time=0.8)
            self.play(box.animate.set_stroke(PALETTE["muted"], width=2), run_time=0.3)
            if i < 3:
                self.play(GrowArrow(arrows[i]), run_time=0.4)
            self.wait(5.0 if i < 3 else 4.0)

        foot = Text("your estimate now comes from evidence, not optimism",
                    font="DejaVu Sans", color=PALETTE["accent"], font_size=26,
                    weight=BOLD).move_to([0, -3.35, 0])
        self.play(FadeIn(foot, shift=UP * 0.15), run_time=0.9)
        self.wait(1.6)


# --------- shared per-task-row geometry for B05 / B08 -------------------------
ROW_XL, ROW_XW = -2.4, 6.6      # track spans days 0..16
DAY_MAX = 16.0
def row_x(day):
    return ROW_XL + (day / DAY_MAX) * ROW_XW

def gridlines(y_top, y_bot):
    g = VGroup()
    for d in (5, 10, 15):
        ln = DashedLine([row_x(d), y_bot, 0], [row_x(d), y_top, 0],
                        color=PALETTE["muted"], stroke_width=1.2,
                        dash_length=0.06).set_opacity(0.5)
        lbl = Text(str(d), font="DejaVu Sans", color=PALETTE["muted"],
                   font_size=18).move_to([row_x(d), y_bot - 0.28, 0])
        g.add(ln, lbl)
    unit = Text("days", font="DejaVu Sans", color=PALETTE["muted"],
                font_size=18).move_to([row_x(16) + 0.5, y_bot - 0.28, 0])
    g.add(unit)
    return g


# ============================================================ B05 OUTPUT v1 ==
class B05_PointPlan(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = title_text("v1: three tidy numbers")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)

        ys = [1.7, 0.5, -0.7]
        grid = gridlines(2.3, -1.3)
        self.play(FadeIn(grid), run_time=0.6)

        rows = VGroup()
        for (name, cls, gut), y in zip(TASKS, ys):
            nm = Text(name, font="DejaVu Sans", color=PALETTE["ink"],
                      font_size=26, weight=BOLD).move_to([-5.0, y, 0])
            track = Line([row_x(0), y, 0], [row_x(16), y, 0],
                         color=PALETTE["panel"], stroke_width=3)
            dot = Dot([row_x(gut), y, 0], radius=0.13, color=PALETTE["ink"])
            val = Text(f"{gut} days", font="DejaVu Sans", color=PALETTE["ink"],
                       font_size=24, weight=BOLD).next_to(dot, UP, buff=0.12)
            rows.add(VGroup(nm, track, dot, val))

        for r in rows:
            self.play(FadeIn(r[0]), Create(r[1]), run_time=0.4)
            self.play(GrowFromCenter(r[2]), FadeIn(r[3], shift=UP * 0.1), run_time=0.5)
            self.wait(1.4)

        total = Text(f"sprint total = {GUT_TOTAL} days", font="DejaVu Sans",
                     color=PALETTE["ink"], font_size=34, weight=BOLD).move_to([0, -2.4, 0])
        self.play(Write(total), run_time=0.9)
        self.wait(1.8)

        q = Text("...but how sure are we? (no ranges, no history)",
                 font="DejaVu Sans", color=PALETTE["accent"], font_size=27,
                 weight=BOLD).move_to([0, -3.3, 0])
        self.play(FadeIn(q, shift=UP * 0.15), run_time=0.9)
        self.wait(4.0)   # "a guess wearing the costume of a measurement", held


# ============================================================ B08 OUTPUT v2 ==
class B08_Ranges(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = title_text("v2: ranges from real history")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)

        ys = [2.1, 1.0, -0.1]
        grid = gridlines(2.7, -1.55)
        self.play(FadeIn(grid), run_time=0.6)

        for (name, cls, gut), y in zip(TASKS, ys):
            p50, p80 = rng_of(cls)
            nm = Text(name, font="DejaVu Sans", color=PALETTE["ink"],
                      font_size=25, weight=BOLD).move_to([-5.05, y, 0])
            self.play(FadeIn(nm), run_time=0.3)

            # the P50..P80 band
            band = Rectangle(width=row_x(p80) - row_x(p50), height=0.34,
                             stroke_width=0, fill_color=PALETTE["accent"],
                             fill_opacity=0.75)
            band.move_to([(row_x(p50) + row_x(p80)) / 2, y, 0])
            rng_lbl = Text(f"{p50:.1f}-{p80:.1f}", font="DejaVu Sans",
                           color=PALETTE["accent"], font_size=23, weight=BOLD)
            rng_lbl.next_to(band, RIGHT, buff=0.25)
            self.play(GrowFromEdge(band, LEFT), FadeIn(rng_lbl), run_time=0.7)

            # the old gut point -- lands on the optimistic edge
            gdot = Dot([row_x(gut), y, 0], radius=0.11, color=PALETTE["ink"])
            gtxt = Text(f"gut {gut}", font="DejaVu Sans", color=PALETTE["ink"],
                        font_size=19).next_to(gdot, DOWN, buff=0.1)
            self.play(GrowFromCenter(gdot), FadeIn(gtxt), run_time=0.5)
            self.wait(1.6)

        # the falsifiability row: no reference class -> spike it
        yn = -1.35
        nm = Text("DB migration", font="DejaVu Sans", color=PALETTE["muted"],
                  font_size=25, weight=BOLD).move_to([-5.05, yn, 0])
        flag = Text("no reference class -> spike it first",
                    font="DejaVu Sans", color=PALETTE["good"], font_size=24,
                    weight=BOLD).move_to([row_x(8), yn, 0])
        self.play(FadeIn(nm), FadeIn(flag, shift=RIGHT * 0.15), run_time=0.8)
        self.wait(3.2)   # "we don't fake a number, we flag it to spike"

        # totals, side by side -- the effect as a NUMBER, not just bars
        g_box = VGroup(
            Text("gut", font="DejaVu Sans", color=PALETTE["muted"],
                 font_size=24, weight=BOLD),
            Text(f"{GUT_TOTAL}", font="DejaVu Serif", color=PALETTE["muted"],
                 font_size=52, weight=BOLD),
            Text("days", font="DejaVu Sans", color=PALETTE["muted"], font_size=22),
        ).arrange(DOWN, buff=0.06).move_to([-2.3, -3.05, 0])
        arrow = Arrow([-1.2, -3.05, 0], [0.4, -3.05, 0], buff=0.05,
                      color=PALETTE["ink"], stroke_width=5)
        h_box = VGroup(
            Text("honest P80", font="DejaVu Sans", color=PALETTE["accent"],
                 font_size=24, weight=BOLD),
            Text(f"~{P80_TOTAL:.0f}", font="DejaVu Serif", color=PALETTE["accent"],
                 font_size=52, weight=BOLD),
            Text("days", font="DejaVu Sans", color=PALETTE["accent"], font_size=22),
        ).arrange(DOWN, buff=0.06).move_to([1.9, -3.05, 0])
        self.play(FadeIn(g_box), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(h_box, shift=RIGHT * 0.2), run_time=0.9)
        self.wait(4.0)   # "from ten days to about nineteen", held


# =============================================================== B09 SUMMARY ==
class B09_Summary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = title_text("The rubric - ask three questions")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)

        qs = [
            ("1", "REFERENCE CLASS", "what kind of work is this, really?"),
            ("2", "WHAT IT ACTUALLY TOOK", "read the spread of past work, not the best case"),
            ("3", "VELOCITY", "are we faster or slower than that history now?"),
        ]
        rows = VGroup()
        for num, head, gloss in qs:
            n = Text(num, font="DejaVu Serif", color=PALETTE["accent"],
                     font_size=46, weight=BOLD)
            h = Text(head, font="DejaVu Sans", color=PALETTE["ink"],
                     font_size=30, weight=BOLD)
            g = Text(gloss, font="DejaVu Sans", color=PALETTE["muted"], font_size=23)
            txt = VGroup(h, g).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            rows.add(VGroup(n, txt).arrange(RIGHT, buff=0.4, aligned_edge=UP))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to([-0.4, 0.5, 0])

        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.7)
            self.wait(3.0)

        msg = Text("report a RANGE, not a point   -   no reference class? spike it, don't fake it",
                   font="DejaVu Sans", color=PALETTE["ink"], font_size=24,
                   weight=BOLD).move_to([0, -3.1, 0])
        card = RoundedRectangle(corner_radius=0.12, width=msg.width + 0.7, height=1.1,
                                stroke_color=PALETTE["accent"], stroke_width=2.5,
                                fill_color=PALETTE["panel"], fill_opacity=1.0)
        card.move_to(msg.get_center())
        msg.set_z_index(1)
        self.play(FadeIn(card), Write(msg), run_time=1.2)
        self.wait(4.0)
