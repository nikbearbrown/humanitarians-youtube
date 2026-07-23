"""vox_scenes.py — Why Fit Can't Save a Non-Sponsor: The Bayesian Role Scorer
(vox-fit-nonsponsor, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B02 is the STILL (ai slot) — no scene here.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything:
  bash vox/scripts/vox_run.sh the-reallocation-engine/youtube/vox-fit-nonsponsor

Color law:
  TEAL   = sponsoring company / composite above threshold / Apply
  CRIMSON = non-sponsor / collapsed composite / Skip
  GOLD   = single editor highlight (B08 only)
  SLATE  = structural scaffolding (axis lines, gate markers)

Card exclusions: NO Eightfold lawsuit; NO fit-score internals; NO Override.
Illustrative numbers: B02, B07, B10 — labeled in FACTCHECK.
"""
import sys
import json
import os
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _bar_segment(height, color, width=1.8, opacity=0.92):
    """One stacked-bar segment."""
    r = Rectangle(width=width, height=height)
    r.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return r


def _weight_label(text, color=INK, size=22):
    return Text(text, font=MONO, color=color, font_size=size)


def _chip(text, color):
    return LabelChip(text, accent=color, size=22)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Why Fit Can't Save a Non-Sponsor", font=DISPLAY, color=INK,
                  font_size=24, weight=BOLD)
        t2 = Text("The Bayesian Role Scorer", font=DISPLAY, color=CRIMSON,
                  font_size=26, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Fit = 0.85.", font=DISPLAY, color=INK, font_size=44, weight=BOLD)
        q2 = Text("The engine says Skip.", font=DISPLAY, color=CRIMSON,
                  font_size=36, weight=BOLD)
        q3 = Text("Why?", font=SERIF, color=INK, font_size=52, weight=BOLD,
                  slant=ITALIC)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.28).move_to(UP * 0.2)
        u = Line(q2.get_corner(DL) + DOWN * 0.12, q2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(q2), Create(u), run_time=0.9)
        self.play(FadeIn(q3, scale=0.92), run_time=0.8)
        self.wait(max(0.3, total - 2.4))


class B04_Inputs(Scene):
    def construct(self):
        total = DUR["B04"]
        # Four input rows: sponsorship (0.35, TEAL), fit (0.30, TEAL),
        # liveness (gate, SLATE), timeline (gate, SLATE)
        rows_data = [
            ("Sponsorship", "weight 0.35", TEAL, "VOTE"),
            ("Fit", "weight 0.30", TEAL, "VOTE"),
            ("Liveness", "multiplier", SLATE, "GATE"),
            ("Timeline", "multiplier", SLATE, "GATE"),
        ]
        rows = VGroup()
        for name, sub, color, kind in rows_data:
            name_t = Text(name, font=DISPLAY, color=INK, font_size=26, weight=BOLD)
            sub_t = Text(sub, font=MONO, color=color, font_size=20)
            kind_c = LabelChip(kind, accent=color, size=18)
            row = VGroup(name_t, sub_t, kind_c).arrange(RIGHT, buff=0.45,
                                                         aligned_edge=LEFT)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.38).move_to(LEFT * 1.5)

        # A composite arrow to the right
        arrow = Arrow(LEFT * 0.2 + DOWN * 0.1, RIGHT * 1.9 + DOWN * 0.1,
                      color=INK, stroke_width=3, buff=0.1)
        comp_label = Text("composite", font=SERIF, color=INK, font_size=24,
                          slant=ITALIC)
        comp_label.next_to(arrow, UP, buff=0.18)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rows],
                              lag_ratio=0.18), run_time=1.4)
        self.play(GrowArrow(arrow), FadeIn(comp_label), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


class B05_WhyDominant(Scene):
    def construct(self):
        total = DUR["B05"]
        # Two weight bars side by side
        bar_h_total = 3.5
        sp_h = bar_h_total * 0.35
        fit_h = bar_h_total * 0.30

        sp_bar = _bar_segment(sp_h, TEAL, width=1.6)
        fit_bar = _bar_segment(fit_h, TEAL, width=1.6)

        sp_bar.move_to(LEFT * 2.2 + DOWN * (bar_h_total - sp_h) / 2)
        fit_bar.move_to(RIGHT * 0.3 + DOWN * (bar_h_total - fit_h) / 2)

        sp_label = Text("Sponsorship", font=DISPLAY, color=INK, font_size=22,
                        weight=BOLD)
        sp_val = Text("0.35", font=MONO, color=TEAL, font_size=28)
        sp_group = VGroup(sp_label, sp_val).arrange(DOWN, buff=0.1)
        sp_group.next_to(sp_bar, DOWN, buff=0.22)

        fit_label = Text("Fit", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        fit_val = Text("0.30", font=MONO, color=TEAL, font_size=28)
        fit_group = VGroup(fit_label, fit_val).arrange(DOWN, buff=0.1)
        fit_group.next_to(fit_bar, DOWN, buff=0.22)

        invis_chip = _chip("invisible rejection", CRIMSON)
        invis_chip.next_to(sp_bar, RIGHT, buff=0.55).shift(UP * 0.3)

        self.play(FadeIn(sp_bar, shift=UP * 0.3), FadeIn(sp_group), run_time=0.9)
        self.play(FadeIn(fit_bar, shift=UP * 0.3), FadeIn(fit_group), run_time=0.8)
        self.play(FadeIn(invis_chip, shift=LEFT * 0.2), run_time=0.7)
        self.wait(max(0.3, total - 2.4))


class B06_SponsorBar(Scene):
    """Cambridge biotech — TEAL composite above threshold — Apply."""
    def construct(self):
        total = DUR["B06"]
        bar_x = LEFT * 1.8
        bar_w = 2.0

        # Heights proportional to contribution (illustrative)
        # sponsorship: 0.9 * 0.35 = 0.315
        # fit: 0.70 * 0.30 = 0.21
        # liveness+timeline multiplier markers (visual only, not numeric segments)
        scale = 5.5  # pixels per unit
        sp_h = 0.315 * scale
        fit_h = 0.21 * scale
        gate_h = 0.32  # thin stripe for gate markers

        sp_seg = _bar_segment(sp_h, TEAL, width=bar_w)
        fit_seg = _bar_segment(fit_h, TEAL, width=bar_w)
        liv_seg = _bar_segment(gate_h, SLATE, width=bar_w, opacity=0.55)
        tim_seg = _bar_segment(gate_h, SLATE, width=bar_w, opacity=0.55)

        # stack bottom-up: timeline, liveness, fit, sponsorship
        tim_seg.move_to(bar_x)
        liv_seg.next_to(tim_seg, UP, buff=0)
        fit_seg.next_to(liv_seg, UP, buff=0)
        sp_seg.next_to(fit_seg, UP, buff=0)

        stack = VGroup(tim_seg, liv_seg, fit_seg, sp_seg)
        stack_bottom = tim_seg.get_bottom()[1]
        stack_top = sp_seg.get_top()[1]

        # threshold line at 0.3 threshold equivalent
        threshold_y = stack_bottom + 0.3 * scale
        thr_line = DashedLine(
            LEFT * 3.8 + UP * threshold_y,
            RIGHT * 0.5 + UP * threshold_y,
            color=INK, stroke_width=2, dash_length=0.18)
        thr_label = Text("threshold", font=SERIF, color=INK, font_size=18,
                         slant=ITALIC)
        thr_label.next_to(thr_line, RIGHT, buff=0.15)

        # company label
        company = Text("Cambridge biotech", font=DISPLAY, color=TEAL,
                       font_size=22, weight=BOLD)
        company.next_to(stack, UP, buff=0.32)

        # weight annotations
        sp_ann = SerifLabel("0.9 x 0.35 = 0.315", TEAL, size=18)
        sp_ann.next_to(sp_seg, RIGHT, buff=0.25)
        fit_ann = SerifLabel("0.70 x 0.30 = 0.21", TEAL, size=18)
        fit_ann.next_to(fit_seg, RIGHT, buff=0.25)

        apply_chip = _chip("Apply", TEAL)
        apply_chip.move_to(RIGHT * 3.0 + UP * 1.2)

        self.play(FadeIn(thr_line), FadeIn(thr_label), run_time=0.6)
        self.play(FadeIn(company), run_time=0.5)
        self.play(FadeIn(sp_seg, shift=UP * 0.3), FadeIn(sp_ann), run_time=0.7)
        self.play(FadeIn(fit_seg, shift=UP * 0.2), FadeIn(fit_ann), run_time=0.6)
        self.play(FadeIn(liv_seg), FadeIn(tim_seg), run_time=0.5)
        self.play(FadeIn(apply_chip, scale=0.9), run_time=0.6)
        self.wait(max(0.3, total - 3.5))


class B07_NonSponsorBar(Scene):
    """BrandCo — CRIMSON sponsorship sliver, composite collapses — Skip."""
    def construct(self):
        total = DUR["B07"]
        bar_x = LEFT * 1.8
        bar_w = 2.0
        scale = 5.5

        # BrandCo: sponsorship 0.05 * 0.35 = 0.0175 ≈ 0.018
        sp_h = max(0.018 * scale, 0.08)   # minimum visible sliver
        fit_h = 0.21 * scale               # same fit as biotech
        gate_h = 0.32

        sp_seg = _bar_segment(sp_h, CRIMSON, width=bar_w)
        fit_seg = _bar_segment(fit_h, TEAL, width=bar_w)
        liv_seg = _bar_segment(gate_h, SLATE, width=bar_w, opacity=0.55)
        tim_seg = _bar_segment(gate_h, SLATE, width=bar_w, opacity=0.55)

        tim_seg.move_to(bar_x)
        liv_seg.next_to(tim_seg, UP, buff=0)
        fit_seg.next_to(liv_seg, UP, buff=0)
        sp_seg.next_to(fit_seg, UP, buff=0)

        stack_bottom = tim_seg.get_bottom()[1]

        threshold_y = stack_bottom + 0.3 * scale
        thr_line = DashedLine(
            LEFT * 3.8 + UP * threshold_y,
            RIGHT * 0.5 + UP * threshold_y,
            color=INK, stroke_width=2, dash_length=0.18)
        thr_label = Text("threshold", font=SERIF, color=INK, font_size=18,
                         slant=ITALIC)
        thr_label.next_to(thr_line, RIGHT, buff=0.15)

        company = Text("BrandCo", font=DISPLAY, color=CRIMSON,
                       font_size=22, weight=BOLD)
        company.next_to(sp_seg, UP, buff=0.32)

        sp_ann = SerifLabel("0.05 x 0.35 = 0.018", CRIMSON, size=18)
        sp_ann.next_to(sp_seg, RIGHT, buff=0.25)
        fit_ann = SerifLabel("0.70 x 0.30 = 0.21", TEAL, size=18)
        fit_ann.next_to(fit_seg, RIGHT, buff=0.25)

        skip_chip = _chip("Skip", CRIMSON)
        skip_chip.move_to(RIGHT * 3.0 + UP * 0.2)

        self.play(FadeIn(thr_line), FadeIn(thr_label), run_time=0.6)
        self.play(FadeIn(company), run_time=0.5)
        # Sponsorship sliver appears first — dramatic reveal of near-nothing
        self.play(FadeIn(sp_seg, scale=0.9), FadeIn(sp_ann), run_time=0.7)
        self.play(FadeIn(fit_seg, shift=DOWN * 0.15), FadeIn(fit_ann), run_time=0.6)
        self.play(FadeIn(liv_seg), FadeIn(tim_seg), run_time=0.5)
        self.play(FadeIn(skip_chip, scale=0.9), run_time=0.6)
        self.wait(max(0.3, total - 3.5))


class B08_SideBySide(Scene):
    """Both bars, side by side — GOLD sweep on the sponsorship row."""
    def construct(self):
        total = DUR["B08"]
        bar_w = 1.7
        scale = 5.0

        # Left bar: biotech (TEAL)
        left_x = LEFT * 3.5
        sp_h_t = 0.315 * scale
        fit_h = 0.21 * scale
        gate_h = 0.28

        def _build_stack(x_center, sp_color, sp_height):
            tim = _bar_segment(gate_h, SLATE, width=bar_w, opacity=0.55).move_to(x_center)
            liv = _bar_segment(gate_h, SLATE, width=bar_w, opacity=0.55)
            liv.next_to(tim, UP, buff=0)
            fit = _bar_segment(fit_h, TEAL, width=bar_w)
            fit.next_to(liv, UP, buff=0)
            sp = _bar_segment(sp_height, sp_color, width=bar_w)
            sp.next_to(fit, UP, buff=0)
            return VGroup(tim, liv, fit, sp), tim, fit, sp

        lstack, ltim, lfit, lsp = _build_stack(left_x, TEAL, sp_h_t)

        right_x = RIGHT * 0.5
        sp_h_b = max(0.018 * scale, 0.07)
        rstack, rtim, rfit, rsp = _build_stack(right_x, CRIMSON, sp_h_b)

        # Threshold line
        bottom_y = ltim.get_bottom()[1]
        thr_y = bottom_y + 0.3 * scale
        thr_line = DashedLine(
            LEFT * 5.2 + UP * thr_y,
            RIGHT * 2.2 + UP * thr_y,
            color=INK, stroke_width=2, dash_length=0.18)

        # Company labels
        lc_label = Text("Cambridge biotech", font=DISPLAY, color=TEAL,
                        font_size=19, weight=BOLD)
        lc_label.next_to(lsp, UP, buff=0.25)
        rc_label = Text("BrandCo", font=DISPLAY, color=CRIMSON,
                        font_size=19, weight=BOLD)
        rc_label.next_to(rsp, UP, buff=0.25)

        # Contribution annotations below bars
        l_ann = SerifLabel("0.315", TEAL, size=20)
        l_ann.next_to(lsp, RIGHT, buff=0.2)
        r_ann = SerifLabel("0.018", CRIMSON, size=20)
        r_ann.next_to(rsp, RIGHT, buff=0.2)

        # GOLD highlight: a horizontal sweep band behind the sponsorship row of both bars
        # Position the GOLD bar to span both sponsorship segments at the right height
        lsp_y = lsp.get_center()[1]
        gold_bar = Rectangle(width=6.5, height=max(sp_h_t, 0.4))
        gold_bar.set_fill(GOLD, 0.38).set_stroke(width=0, opacity=0)
        gold_bar.move_to(UP * lsp_y + RIGHT * (left_x[0] + right_x[0]) / 2)

        self.play(FadeIn(lstack), FadeIn(rstack),
                  FadeIn(lc_label), FadeIn(rc_label),
                  FadeIn(thr_line), run_time=1.2)
        self.play(FadeIn(l_ann), FadeIn(r_ann), run_time=0.7)
        # GOLD sweep — the editor's highlight on the decisive row
        self.play(FadeIn(gold_bar, scale=0.85), run_time=0.9)
        self.wait(max(0.3, total - 2.8))


class B09_DecisionRegion(Scene):
    """Apply/Consider/Skip quadrant — two points at identical fit, different sponsorship."""
    def construct(self):
        total = DUR["B09"]

        # Axes
        ax_orig = LEFT * 4.2 + DOWN * 2.8
        ax_len_x = 7.2
        ax_len_y = 5.4

        x_axis = Arrow(ax_orig, ax_orig + RIGHT * ax_len_x,
                       color=INK, stroke_width=2.5, buff=0)
        y_axis = Arrow(ax_orig, ax_orig + UP * ax_len_y,
                       color=INK, stroke_width=2.5, buff=0)

        x_label = Text("Sponsorship probability", font=SERIF, color=INK,
                       font_size=20, slant=ITALIC)
        x_label.next_to(x_axis, DOWN, buff=0.22)
        y_label = Text("Fit score", font=SERIF, color=INK,
                       font_size=20, slant=ITALIC)
        y_label.next_to(y_axis, LEFT, buff=0.2)

        # Region fills (three rectangles)
        # Apply: top-right quadrant
        apply_rect = Rectangle(width=3.5, height=2.6)
        apply_rect.set_fill(TEAL, 0.18).set_stroke(width=0, opacity=0)
        apply_rect.move_to(ax_orig + RIGHT * 5.3 + UP * 4.0)

        # Skip: bottom-left quadrant
        skip_rect = Rectangle(width=3.6, height=2.6)
        skip_rect.set_fill(CRIMSON, 0.15).set_stroke(width=0, opacity=0)
        skip_rect.move_to(ax_orig + RIGHT * 1.8 + UP * 1.3)

        # Consider: the two mixed corners (approximate as center band)
        consider_rect = Rectangle(width=7.0, height=1.0)
        consider_rect.set_fill(SLATE, 0.12).set_stroke(width=0, opacity=0)
        consider_rect.move_to(ax_orig + RIGHT * 3.5 + UP * 2.7)

        apply_chip = LabelChip("Apply", accent=TEAL, size=22)
        apply_chip.move_to(ax_orig + RIGHT * 5.5 + UP * 4.3)
        skip_chip = LabelChip("Skip", accent=CRIMSON, size=22)
        skip_chip.move_to(ax_orig + RIGHT * 1.5 + UP * 1.0)
        consider_chip = LabelChip("Consider", accent=SLATE, size=20)
        consider_chip.move_to(ax_orig + RIGHT * 3.7 + UP * 2.7)

        # Two data points at identical y (fit=0.70) but different x
        # Biotech: sponsorship ~0.9 → far right
        # BrandCo: sponsorship ~0.05 → far left
        dot_y = ax_orig + UP * (0.70 * ax_len_y)
        biotech_pt = Dot(ax_orig + RIGHT * 0.9 * ax_len_x + UP * 0.70 * ax_len_y,
                         color=TEAL, radius=0.14)
        brandco_pt = Dot(ax_orig + RIGHT * 0.05 * ax_len_x + UP * 0.70 * ax_len_y,
                         color=CRIMSON, radius=0.14)

        biotech_ann = Text("biotech", font=SERIF, color=TEAL, font_size=18,
                           slant=ITALIC)
        biotech_ann.next_to(biotech_pt, UP, buff=0.14)
        brandco_ann = Text("BrandCo", font=SERIF, color=CRIMSON, font_size=18,
                           slant=ITALIC)
        brandco_ann.next_to(brandco_pt, DOWN, buff=0.14)

        # Horizontal dashed line at fit=0.70 to show identical fit
        fit_line = DashedLine(
            ax_orig + UP * 0.70 * ax_len_y,
            ax_orig + RIGHT * ax_len_x + UP * 0.70 * ax_len_y,
            color=INK, stroke_width=1.4, dash_length=0.15)

        self.play(Create(x_axis), Create(y_axis),
                  FadeIn(x_label), FadeIn(y_label), run_time=0.9)
        self.play(FadeIn(apply_rect), FadeIn(skip_rect), FadeIn(consider_rect),
                  run_time=0.8)
        self.play(FadeIn(apply_chip), FadeIn(skip_chip), FadeIn(consider_chip),
                  run_time=0.6)
        self.play(Create(fit_line), run_time=0.5)
        self.play(FadeIn(biotech_pt, scale=1.4), FadeIn(biotech_ann), run_time=0.6)
        self.play(FadeIn(brandco_pt, scale=1.4), FadeIn(brandco_ann), run_time=0.6)
        self.wait(max(0.3, total - 4.0))


class B10_Example(Scene):
    """Illustrative worked arithmetic: biotech vs BrandCo two-column table."""
    def construct(self):
        total = DUR["B10"]

        eyebrow = LabelChip("illustrative example", accent=SLATE, size=20)
        eyebrow.to_edge(UP, buff=0.55)

        # Column headers
        left_head = Text("Cambridge biotech", font=DISPLAY, color=TEAL,
                         font_size=22, weight=BOLD)
        right_head = Text("BrandCo", font=DISPLAY, color=CRIMSON,
                          font_size=22, weight=BOLD)

        col_x_l = LEFT * 3.0
        col_x_r = RIGHT * 1.5

        left_head.move_to(col_x_l + UP * 2.6)
        right_head.move_to(col_x_r + UP * 2.6)

        # Divider (structural column separator — intentionally spans the frame)
        divider = Line(UP * 2.2, DOWN * 2.6, color=INK, stroke_width=1.5)
        divider.move_to(LEFT * 0.5)
        divider._qc_intentional = True   # structural column line, not striking text

        # Row data: (label, left value, right value, left color, right color)
        rows_data = [
            ("Sponsorship term",
             "0.9 x 0.35 = 0.315", TEAL,
             "0.05 x 0.35 = 0.018", CRIMSON),
            ("Fit term",
             "0.70 x 0.30 = 0.21", TEAL,
             "0.70 x 0.30 = 0.21", TEAL),
            ("Sum (before gates)",
             "0.525 x gates", TEAL,
             "0.228 x gates", CRIMSON),
            ("Result",
             "above threshold", TEAL,
             "below threshold", CRIMSON),
        ]

        row_mobs_l = VGroup()
        row_mobs_r = VGroup()

        for i, (label, lval, lcol, rval, rcol) in enumerate(rows_data):
            y = 1.8 - i * 1.1
            lbl = Text(label, font=SERIF, color=SLATE, font_size=17, slant=ITALIC)
            lbl.move_to(LEFT * 5.8 + UP * y, aligned_edge=LEFT)

            lv = Text(lval, font=MONO, color=lcol, font_size=20)
            lv.move_to(col_x_l + UP * y)
            rv = Text(rval, font=MONO, color=rcol, font_size=20)
            rv.move_to(col_x_r + UP * y)

            row_mobs_l.add(VGroup(lbl, lv))
            row_mobs_r.add(rv)

        # Verdict chips
        apply_v = LabelChip("Apply", accent=TEAL, size=22)
        apply_v.move_to(col_x_l + DOWN * 2.2)
        skip_v = LabelChip("Skip", accent=CRIMSON, size=22)
        skip_v.move_to(col_x_r + DOWN * 2.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(left_head), FadeIn(right_head), Create(divider), run_time=0.8)
        for rl, rr in zip(row_mobs_l, row_mobs_r):
            self.play(FadeIn(rl, shift=RIGHT * 0.15),
                      FadeIn(rr, shift=LEFT * 0.15), run_time=0.55)
        self.play(FadeIn(apply_v, scale=0.9), FadeIn(skip_v, scale=0.9), run_time=0.7)
        self.wait(max(0.3, total - 0.5 - 0.8 - 4 * 0.55 - 0.7))


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Fit is a vote.", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("Sponsorship decides.", font=DISPLAY, color=CRIMSON,
                  font_size=42, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        topic = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL,
                     font_size=18)
        topic.next_to(block, DOWN, buff=0.7)
        self.play(FadeIn(t1, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.2))
