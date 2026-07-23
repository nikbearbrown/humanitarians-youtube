"""vox_scenes.py — The Base Rate Problem: Why 0.68 Is Not 68%
(vox-base-rate-gap, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 is the only STILL (ai media slot) and has no scene here.

Color law:
  TEAL   = corrected posterior / true probability / employers who actually filed
  CRIMSON = raw score / overstatement / false positives
  GOLD   = editor's-pen highlight — once in B10 only

Exclusions honored: no Bayes formula, no odds-form, no calibration curve,
no four-diagnostic-questions list. Mechanism via axis visual and counts only.
"""
import sys, json, pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}

import numpy as np


# ────────────────────────────────────────────────────────────── B01 Title card

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The Base Rate Problem", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Why 0.68 Is Not 68%", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ────────────────────────────────────────────────────────────── B03 Score card

class B03_ScoreCard(Scene):
    """Filing stats card: 12 filings, 80% approval, score 0.68 in crimson."""
    def construct(self):
        total = DUR["B03"]

        # Three data rows
        labels = ["LCA filings", "H-1B approval rate", "Sponsorship score"]
        values = ["12", "80%", "0.68"]
        colors = [TEAL, TEAL, CRIMSON]

        eyebrow = Text("Cambridge biotech · pharmaceutical SIC", font=DISPLAY,
                       color=SLATE, font_size=18)
        eyebrow.to_edge(UP, buff=0.7)

        rows = VGroup()
        for lbl, val, col in zip(labels, values, colors):
            ltext = Text(lbl, font=SERIF, color=INK, font_size=24)
            vtext = Text(val, font=DISPLAY, color=col, font_size=34, weight=BOLD)
            row = VGroup(ltext, vtext).arrange(RIGHT, buff=0.5)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35).move_to(DOWN * 0.1)

        # Separator line under score
        sep = Line(LEFT * 3.0 + UP * 0.55, RIGHT * 3.0 + UP * 0.55,
                   color=INK, stroke_width=1).set_opacity(0.3)
        question = Text("So why is 0.68 not 68%?", font=SERIF, color=CRIMSON,
                        font_size=26, slant=ITALIC)
        question.next_to(rows, DOWN, buff=0.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.12) for r in rows],
                              lag_ratio=0.3), run_time=1.2)
        self.play(Create(sep), run_time=0.4)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.7))


# ────────────────────────────────────────────────────────────── B04 Question card

class B04_QuestionCard(Scene):
    """THE QUESTION: gap formula on screen."""
    def construct(self):
        total = DUR["B04"]
        t1 = Text("A score of 0.68 should mean", font=DISPLAY, color=INK,
                  font_size=26, weight=BOLD)
        t2 = Text("a 68% chance of sponsorship.", font=DISPLAY, color=CRIMSON,
                  font_size=26, weight=BOLD)
        t3 = Text("Here is the case where it means closer to 40%.", font=DISPLAY,
                  color=INK, font_size=22)
        t4 = Text("Why?", font=DISPLAY, color=TEAL, font_size=32, weight=BOLD)

        block = VGroup(t1, t2, t3, t4).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(t4.get_corner(DL) + DOWN * 0.1, t4.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)

        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), run_time=0.5)
        self.play(FadeIn(t4), Create(u), run_time=0.7)
        self.wait(max(0.3, total - 2.0))


# ────────────────────────────────────────────────────────────── B05 SIC base rate

class B05_SICBase(Scene):
    """Isotype grid: 100 squares, 8 teal (filed LCA), 92 slate (never filed)."""
    def construct(self):
        total = DUR["B05"]
        eye = Text("pharmaceutical / medicine manufacturing SIC", font=DISPLAY,
                   color=SLATE, font_size=18)
        eye.to_edge(UP, buff=0.7)

        grid = IsotypeGrid(
            counts=[8, 92],
            colors=[TEAL, SLATE],
            per_row=10,
            size=0.32,
            gap=0.10,
            mark="square"
        )
        grid.move_to(DOWN * 0.1)

        chip_filed = LabelChip("8 filed LCA", accent=TEAL, size=22)
        chip_never = LabelChip("92 never filed", accent=SLATE, size=22)
        chips = VGroup(chip_filed, chip_never).arrange(RIGHT, buff=0.6)
        chips.next_to(grid, DOWN, buff=0.45)

        subtext = Text("of every 100 employers in this SIC code", font=SERIF,
                       color=INK, font_size=20, slant=ITALIC)
        subtext.next_to(chips, DOWN, buff=0.25)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(grid.count_up(run_time=min(3.5, total - 2.5)), run_time=3.5)
        self.play(FadeIn(chip_filed), FadeIn(chip_never), run_time=0.6)
        self.play(FadeIn(subtext, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 5.1))


# ────────────────────────────────────────────────────────────── B06 Prior axis

class B06_PriorAxis(Scene):
    """Horizontal probability axis, single teal marker at 0.08, labeled PRIOR."""
    def construct(self):
        total = DUR["B06"]

        # Axis
        ax_left = LEFT * 5.5
        ax_right = RIGHT * 5.5
        axis = Line(ax_left, ax_right, color=INK, stroke_width=2.5)
        tick_0 = Line(ax_left + DOWN * 0.18, ax_left + UP * 0.18,
                      color=INK, stroke_width=2)
        tick_1 = Line(ax_right + DOWN * 0.18, ax_right + UP * 0.18,
                      color=INK, stroke_width=2)
        label_0 = Text("0", font=MONO, color=INK, font_size=22)
        label_0.next_to(tick_0, DOWN, buff=0.15)
        label_1 = Text("1", font=MONO, color=INK, font_size=22)
        label_1.next_to(tick_1, DOWN, buff=0.15)

        axis_group = VGroup(axis, tick_0, tick_1, label_0, label_1)
        axis_group.move_to(DOWN * 0.2)

        # Prior marker at 0.08
        prior_x = ax_left + RIGHT * (11.0 * 0.08)
        prior_dot = Dot(prior_x, radius=0.18, color=TEAL)
        prior_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)

        prior_val = Text("0.08", font=MONO, color=TEAL, font_size=24, weight=BOLD)
        prior_val.next_to(prior_dot, UP, buff=0.25)

        prior_chip = LabelChip("SIC prior", accent=TEAL, size=22)
        prior_chip.next_to(prior_dot, DOWN, buff=0.4)

        axis_title = Text("probability of sponsorship", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC)
        axis_title.to_edge(UP, buff=0.7)

        self.play(FadeIn(axis_title), Create(axis_group), run_time=0.9)
        self.play(FadeIn(prior_dot, scale=0.5), run_time=0.5)
        self.play(FadeIn(prior_val), FadeIn(prior_chip), run_time=0.6)
        self.wait(max(0.3, total - 2.0))


# ────────────────────────────────────────────────────────────── B07 Three markers

class B07_ThreeMarkers(Scene):
    """Three markers on probability axis: prior 0.08 teal-left, raw score 0.68
    crimson-right, correction arrow sweeping left."""
    def construct(self):
        total = DUR["B07"]

        ax_left = LEFT * 5.5
        ax_right = RIGHT * 5.5
        axis = Line(ax_left, ax_right, color=INK, stroke_width=2.5)
        tick_0 = Line(ax_left + DOWN * 0.18, ax_left + UP * 0.18,
                      color=INK, stroke_width=2)
        tick_1 = Line(ax_right + DOWN * 0.18, ax_right + UP * 0.18,
                      color=INK, stroke_width=2)
        label_0 = Text("0", font=MONO, color=INK, font_size=22)
        label_0.next_to(tick_0, DOWN, buff=0.15)
        label_1 = Text("1", font=MONO, color=INK, font_size=22)
        label_1.next_to(tick_1, DOWN, buff=0.15)
        axis_group = VGroup(axis, tick_0, tick_1, label_0, label_1)
        axis_group.move_to(DOWN * 0.2)

        span = 11.0  # axis width in Manim units

        # Prior dot at 0.08
        prior_x = ax_left + RIGHT * (span * 0.08)
        prior_dot = Dot(prior_x, radius=0.18, color=TEAL)
        prior_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        prior_val = Text("0.08", font=MONO, color=TEAL, font_size=22, weight=BOLD)
        prior_val.next_to(prior_dot, UP, buff=0.22)
        prior_chip = LabelChip("SIC prior", accent=TEAL, size=20)
        prior_chip.next_to(prior_dot, DOWN, buff=0.35)

        # Raw score dot at 0.68
        raw_x = ax_left + RIGHT * (span * 0.68)
        raw_dot = Dot(raw_x, radius=0.18, color=CRIMSON)
        raw_dot.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        raw_val = Text("0.68", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        raw_val.next_to(raw_dot, UP, buff=0.22)
        raw_chip = LabelChip("raw score", accent=CRIMSON, size=20)
        raw_chip.next_to(raw_dot, DOWN, buff=0.35)

        axis_title = Text("probability of sponsorship", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC)
        axis_title.to_edge(UP, buff=0.7)

        self.play(FadeIn(axis_title), Create(axis_group), run_time=0.8)
        self.play(FadeIn(prior_dot, scale=0.5), FadeIn(prior_val),
                  FadeIn(prior_chip), run_time=0.6)
        self.play(FadeIn(raw_dot, scale=0.5), FadeIn(raw_val),
                  FadeIn(raw_chip), run_time=0.6)
        self.wait(max(0.3, total - 2.0))


# ────────────────────────────────────────────────────────────── B08 Corrected posterior

class B08_CorrectedPosterior(Scene):
    """Correction arrow sweeps from 0.68 leftward to ~0.40 teal marker."""
    def construct(self):
        total = DUR["B08"]

        ax_left = LEFT * 5.5
        ax_right = RIGHT * 5.5
        axis = Line(ax_left, ax_right, color=INK, stroke_width=2.5)
        tick_0 = Line(ax_left + DOWN * 0.18, ax_left + UP * 0.18,
                      color=INK, stroke_width=2)
        tick_1 = Line(ax_right + DOWN * 0.18, ax_right + UP * 0.18,
                      color=INK, stroke_width=2)
        label_0 = Text("0", font=MONO, color=INK, font_size=22)
        label_0.next_to(tick_0, DOWN, buff=0.15)
        label_1 = Text("1", font=MONO, color=INK, font_size=22)
        label_1.next_to(tick_1, DOWN, buff=0.15)
        axis_group = VGroup(axis, tick_0, tick_1, label_0, label_1)
        axis_group.move_to(DOWN * 0.2)

        span = 11.0

        # Prior dot at 0.08 (small, faded anchor)
        prior_x = ax_left + RIGHT * (span * 0.08)
        prior_dot = Dot(prior_x, radius=0.13, color=TEAL)
        prior_dot.set_fill(TEAL, 0.5).set_stroke(width=0, opacity=0)
        prior_val = Text("0.08", font=MONO, color=TEAL, font_size=18)
        prior_val.next_to(prior_dot, DOWN, buff=0.2)
        prior_chip = LabelChip("prior", accent=TEAL, size=18)
        prior_chip.next_to(prior_dot, UP, buff=0.25)

        # Raw score dot at 0.68 in crimson
        raw_x = ax_left + RIGHT * (span * 0.68)
        raw_dot = Dot(raw_x, radius=0.18, color=CRIMSON)
        raw_dot.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        raw_val = Text("0.68", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        raw_val.next_to(raw_dot, UP, buff=0.22)
        raw_chip = LabelChip("raw score", accent=CRIMSON, size=20)
        raw_chip.next_to(raw_dot, DOWN, buff=0.35)

        # Posterior dot at 0.40 in teal
        post_x = ax_left + RIGHT * (span * 0.40)
        post_dot = Dot(post_x, radius=0.18, color=TEAL)
        post_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        post_val = Text("~0.40", font=MONO, color=TEAL, font_size=22, weight=BOLD)
        post_val.next_to(post_dot, UP, buff=0.22)
        post_chip = LabelChip("corrected", accent=TEAL, size=20)
        post_chip.next_to(post_dot, DOWN, buff=0.35)

        # Correction arrow from raw to posterior (sweeps left)
        corr_arrow = Arrow(raw_x + UP * 0.05, post_x + UP * 0.05,
                           color=INK, stroke_width=3, buff=0.22,
                           max_tip_length_to_length_ratio=0.18)

        overstate_label = SerifLabel("overstatement: 50-75%", CRIMSON, size=22)
        overstate_label.move_to(UP * 2.5)

        axis_title = Text("probability of sponsorship", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC)
        axis_title.to_edge(UP, buff=0.7)

        self.play(FadeIn(axis_title), Create(axis_group), run_time=0.7)
        self.play(FadeIn(prior_dot, scale=0.5), FadeIn(prior_val),
                  FadeIn(prior_chip), run_time=0.4)
        self.play(FadeIn(raw_dot, scale=0.5), FadeIn(raw_val),
                  FadeIn(raw_chip), run_time=0.5)
        self.play(GrowArrow(corr_arrow), run_time=0.9)
        self.play(FadeIn(post_dot, scale=0.5), FadeIn(post_val),
                  FadeIn(post_chip), run_time=0.6)
        self.play(FadeIn(overstate_label, shift=DOWN * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 3.6))


# ────────────────────────────────────────────────────────────── B09 Mechanism card

class B09_MechanismCard(Scene):
    """Core mechanism statement card."""
    def construct(self):
        total = DUR["B09"]
        t1 = Text("A signal is only as strong", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("as the base rate it works against.", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t3 = Text("92% of employers in this SIC code never sponsor.", font=SERIF,
                  color=CRIMSON, font_size=24, slant=ITALIC)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 1.5))


# ────────────────────────────────────────────────────────────── B10 Gap label

class B10_GapLabel(Scene):
    """Probability axis with all three markers; GOLD highlight on the gap
    between 0.68 and 0.40; label 'the overstatement'."""
    def construct(self):
        total = DUR["B10"]

        ax_left = LEFT * 5.5
        ax_right = RIGHT * 5.5
        axis = Line(ax_left, ax_right, color=INK, stroke_width=2.5)
        tick_0 = Line(ax_left + DOWN * 0.18, ax_left + UP * 0.18,
                      color=INK, stroke_width=2)
        tick_1 = Line(ax_right + DOWN * 0.18, ax_right + UP * 0.18,
                      color=INK, stroke_width=2)
        label_0 = Text("0", font=MONO, color=INK, font_size=22)
        label_0.next_to(tick_0, DOWN, buff=0.15)
        label_1 = Text("1", font=MONO, color=INK, font_size=22)
        label_1.next_to(tick_1, DOWN, buff=0.15)
        axis_group = VGroup(axis, tick_0, tick_1, label_0, label_1)
        axis_group.move_to(DOWN * 0.2)

        span = 11.0

        # Prior dot
        prior_x = ax_left + RIGHT * (span * 0.08)
        prior_dot = Dot(prior_x, radius=0.13, color=TEAL)
        prior_dot.set_fill(TEAL, 0.5).set_stroke(width=0, opacity=0)

        # Raw score dot
        raw_x = ax_left + RIGHT * (span * 0.68)
        raw_dot = Dot(raw_x, radius=0.18, color=CRIMSON)
        raw_dot.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        raw_val = Text("0.68", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        raw_val.next_to(raw_dot, UP, buff=0.22)

        # Posterior dot
        post_x = ax_left + RIGHT * (span * 0.40)
        post_dot = Dot(post_x, radius=0.18, color=TEAL)
        post_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        post_val = Text("~0.40", font=MONO, color=TEAL, font_size=22, weight=BOLD)
        post_val.next_to(post_dot, UP, buff=0.22)

        # GOLD highlighter sweep over the gap between ~0.40 and 0.68
        gap_mid_x = (post_x + raw_x) / 2
        gap_w = (raw_x - post_x)[0] + 0.15
        gold_bar = Rectangle(width=gap_w, height=0.45)
        gold_bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        gold_bar.move_to(gap_mid_x + DOWN * 0.22)
        gold_bar._qc_intentional = True   # highlighter bar sits over the axis line

        gap_label = SerifLabel("the overstatement", CRIMSON, size=24)
        gap_label.next_to(gold_bar, DOWN, buff=0.45)

        axis_title = Text("probability of sponsorship", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC)
        axis_title.to_edge(UP, buff=0.7)

        self.play(FadeIn(axis_title), Create(axis_group), run_time=0.7)
        self.play(FadeIn(prior_dot, scale=0.5), run_time=0.3)
        self.play(FadeIn(raw_dot, scale=0.5), FadeIn(raw_val), run_time=0.4)
        self.play(FadeIn(post_dot, scale=0.5), FadeIn(post_val), run_time=0.4)
        self.play(FadeIn(gold_bar, scale=0.85), run_time=0.6)
        self.play(FadeIn(gap_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.9))


# ────────────────────────────────────────────────────────────── B11 1000-company grid

class B11_ThousandGrid(Scene):
    """Isotype grid: 1000 squares, 80 teal (true filers), 920 slate (never filed).
    Illustrative — consistent with real 8% base rate."""
    def construct(self):
        total = DUR["B11"]

        eye = Text("1,000 companies in this SIC code (illustrative)", font=DISPLAY,
                   color=SLATE, font_size=17)
        eye.to_edge(UP, buff=0.55)

        grid = IsotypeGrid(
            counts=[80, 920],
            colors=[TEAL, SLATE],
            per_row=40,
            size=0.12,
            gap=0.05,
            mark="square"
        )
        grid.move_to(DOWN * 0.15)

        chip_filed = LabelChip("80 filed LCA", accent=TEAL, size=20)
        chip_never = LabelChip("920 never filed", accent=SLATE, size=20)
        chips = VGroup(chip_filed, chip_never).arrange(RIGHT, buff=0.5)
        chips.next_to(grid, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.4)
        self.play(grid.count_up(run_time=min(4.5, total - 2.0)), run_time=4.5)
        self.play(FadeIn(chip_filed), FadeIn(chip_never), run_time=0.6)
        self.wait(max(0.3, total - 5.5))


# ────────────────────────────────────────────────────────────── B12 Flag breakdown

class B12_FlagBreakdown(Scene):
    """100 flagged squares: 64 teal (genuine), 36 crimson (false positives).
    Illustrative."""
    def construct(self):
        total = DUR["B12"]

        eye = Text("The scorer flags 100 companies as likely sponsors (illustrative)",
                   font=DISPLAY, color=SLATE, font_size=16)
        eye.to_edge(UP, buff=0.55)

        # Start with 100 crimson (all flagged)
        all_flagged = IsotypeGrid(
            counts=[100],
            colors=[CRIMSON],
            per_row=10,
            size=0.30,
            gap=0.09,
            mark="square"
        )
        all_flagged.move_to(DOWN * 0.1)

        # End state: 64 teal + 36 crimson
        breakdown = IsotypeGrid(
            counts=[64, 36],
            colors=[TEAL, CRIMSON],
            per_row=10,
            size=0.30,
            gap=0.09,
            mark="square"
        )
        breakdown.move_to(DOWN * 0.1)

        chip_genuine = LabelChip("64 genuine sponsors", accent=TEAL, size=20)
        chip_false = LabelChip("36 false positives", accent=CRIMSON, size=20)
        chips = VGroup(chip_genuine, chip_false).arrange(RIGHT, buff=0.5)
        chips.next_to(breakdown, DOWN, buff=0.38)

        self.play(FadeIn(eye), run_time=0.4)
        self.play(all_flagged.count_up(run_time=2.0), run_time=2.0)
        self.play(Transform(all_flagged, breakdown), run_time=1.2)
        self.play(FadeIn(chip_genuine), FadeIn(chip_false), run_time=0.6)
        self.wait(max(0.3, total - 4.2))


# ────────────────────────────────────────────────────────────── B13 Endcard

class B13_Endcard(Scene):
    def construct(self):
        total = DUR["B13"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("0.68 means closer to 0.40.", font=DISPLAY, color=CRIMSON,
                  font_size=34, weight=BOLD)
        t2 = Text("The base rate pulls the signal back.", font=DISPLAY, color=INK,
                  font_size=26)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.1)
        u = Line(t1.get_corner(DL) + DOWN * 0.12, t1.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=0.8)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 1.9))
