import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------------------
# B01 — Title card (CARD beat)
# ---------------------------------------------------------------------------
class B01_Title(Scene):
    def construct(self):
        duration = DUR.get("B01", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 1.9)
        rule1 = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=2.5).move_to(UP * 1.1)
        rule2 = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 1.5)
        mid_box = Rectangle(width=13.0, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        mid_box.move_to(UP * 0.2)
        accent_dot = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.9)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.9)
        mid_rule = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=0.8).move_to(DOWN * 0.5)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline1 = Text("Why Moving a Tip 1 Angstrom Closer", font=DISPLAY, font_size=34,
                         color=INK).move_to(UP * 0.2)
        headline2 = Text("Changes Tunneling Current by 7", font=DISPLAY, font_size=34,
                         color=TEAL).move_to(DOWN * 0.9)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(mid_box), run_time=0.4)
        self.play(Write(headline1), run_time=0.4)
        self.play(Create(mid_rule), run_time=0.3)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(accent_dot), FadeIn(accent_dot2), run_time=0.3)
        self.play(Write(headline2), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B02 — Binnig & Rohrer 1981: 1 Å step = 7× current (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_BinnigRohrer(Scene):
    def construct(self):
        duration = DUR.get("B02", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Surface
        surface = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=3).move_to(DOWN * 1.5)

        # Tip body
        tip_body = Rectangle(width=1.2, height=1.8).set_fill(SLATE, 0.7).set_stroke(INK, 2)
        tip_body.move_to(UP * 1.6)

        # Gap brace + label
        gap_brace = DoubleArrow(UP * 0.15, DOWN * 1.4, color=INK, buff=0,
                                stroke_width=2, max_tip_length_to_length_ratio=0.15)
        gap_brace.move_to(RIGHT * 1.8 + DOWN * 0.6)

        # Current box (baseline)
        curr_box = Rectangle(width=3.5, height=1.0).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        curr_box.move_to(LEFT * 4.2 + UP * 0.5)

        # Lower arrow (CRIMSON)
        lower_arr = Arrow(UP * 2.6, UP * 0.8, color=CRIMSON, buff=0,
                          stroke_width=3, max_tip_length_to_length_ratio=0.2)
        lower_arr.move_to(ORIGIN + UP * 1.7)

        # Result box (bright TEAL)
        result_box = Rectangle(width=4.0, height=1.0).set_fill(TEAL, 0.28).set_stroke(TEAL, 2.5)
        result_box.move_to(LEFT * 4.2 + DOWN * 0.7)

        # Factor highlight dot
        factor_dot = Dot(radius=0.18, color=TEAL).move_to(LEFT * 6.0 + DOWN * 0.7)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(Create(surface), run_time=0.4)
        self.play(GrowFromCenter(tip_body), run_time=0.4)
        self.play(GrowArrow(gap_brace), run_time=0.4)
        self.play(GrowFromCenter(curr_box), run_time=0.4)
        self.play(GrowArrow(lower_arr), run_time=0.4)
        self.play(GrowFromCenter(result_box), run_time=0.4)
        self.play(FadeIn(factor_dot), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B03 — THE QUESTION card (CARD beat)
# ---------------------------------------------------------------------------
class B03_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B03", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 2.8)
        rule1 = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        content_box = Rectangle(width=13.5, height=3.0).set_fill(SLATE, 0.05).set_stroke(SLATE, 1)
        content_box.move_to(UP * 0.5)
        inner_box = Rectangle(width=12.0, height=1.1).set_fill(SLATE, 0.08).set_stroke(SLATE, 0.8)
        inner_box.move_to(UP * 1.3)
        rule2 = Line(LEFT * 3.0, RIGHT * 3.0, color=TEAL, stroke_width=2).move_to(DOWN * 0.15)
        teal_dot = Dot(radius=0.14, color=TEAL).move_to(LEFT * 3.3 + DOWN * 0.15)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 3.3 + DOWN * 0.15)
        question_box = Rectangle(width=12.0, height=1.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        question_box.move_to(DOWN * 1.3)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.0).move_to(DOWN * 2.2)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.8)
        line1 = Text("Moving a conductor closer should gradually increase current.", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 1.3)
        line2 = Text("Here a 1-angstrom step multiplies current by 7.", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 0.4)
        line3 = Text("Why does a change smaller than an atom", font=SERIF,
                     font_size=24, color=INK).move_to(DOWN * 0.55)
        line4 = Text("produce such a dramatic response?", font=SERIF,
                     font_size=24, color=TEAL).move_to(DOWN * 1.3)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(GrowFromCenter(inner_box), run_time=0.3)
        self.play(Write(line1), run_time=0.3)
        self.play(Write(line2), run_time=0.3)
        self.play(Create(rule2), FadeIn(teal_dot), FadeIn(teal_dot2), run_time=0.3)
        self.play(Write(line3), run_time=0.3)
        self.play(GrowFromCenter(question_box), run_time=0.3)
        self.play(Write(line4), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.9))


# ---------------------------------------------------------------------------
# B04 — Classical expectation: linear current vs distance (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalLinear(Scene):
    def construct(self):
        duration = DUR.get("B04", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        ax_origin = LEFT * 4.5 + DOWN * 2.5
        x_axis = Arrow(ax_origin, ax_origin + RIGHT * 8.0, color=INK, buff=0,
                       stroke_width=2, max_tip_length_to_length_ratio=0.06)
        y_axis = Arrow(ax_origin, ax_origin + UP * 5.5, color=INK, buff=0,
                       stroke_width=2, max_tip_length_to_length_ratio=0.06)

        # Linear line (CRIMSON)
        p_start = ax_origin + RIGHT * 0.5 + UP * 4.5
        p_end   = ax_origin + RIGHT * 7.5 + UP * 0.3
        linear_line = Line(p_start, p_end, color=CRIMSON, stroke_width=3)

        # Classical label box
        classical_box = Rectangle(width=4.5, height=0.8).set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.5)
        classical_box.move_to(ax_origin + RIGHT * 2.5 + UP * 4.0)

        # Step marker (1 angstrom step on x-axis)
        step_bar = Rectangle(width=0.6, height=0.25).set_fill(CRIMSON, 0.5).set_stroke(CRIMSON, 1)
        step_bar.move_to(ax_origin + RIGHT * 4.2 + DOWN * 0.05)

        # Step tick line
        tick_line = Line(ax_origin + RIGHT * 4.5, ax_origin + RIGHT * 4.5 + UP * 0.3,
                         color=CRIMSON, stroke_width=2)

        # Note box
        note_box = Rectangle(width=7.5, height=0.8).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.2)
        note_box.move_to(DOWN * 3.3)

        # Expectation dot
        expect_dot = Dot(radius=0.15, color=CRIMSON).move_to(ax_origin + RIGHT * 4.5 + UP * 2.5)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(GrowArrow(x_axis), run_time=0.4)
        self.play(GrowArrow(y_axis), run_time=0.4)
        self.play(Create(linear_line), run_time=0.5)
        self.play(GrowFromCenter(classical_box), run_time=0.4)
        self.play(GrowFromCenter(step_bar), run_time=0.3)
        self.play(Create(tick_line), run_time=0.3)
        self.play(FadeIn(expect_dot), run_time=0.3)
        self.play(GrowFromCenter(note_box), run_time=0.4)
        self.wait(max(0.1, duration - 3.7))


# ---------------------------------------------------------------------------
# B05 — Electrons tunnel; probability falls exponentially (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_TunnelingIntro(Scene):
    def construct(self):
        duration = DUR.get("B05", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left conductor block
        left_block = Rectangle(width=3.5, height=4.0).set_fill(SLATE, 0.6).set_stroke(INK, 2)
        left_block.move_to(LEFT * 4.2)

        # Right conductor block
        right_block = Rectangle(width=3.5, height=4.0).set_fill(SLATE, 0.6).set_stroke(INK, 2)
        right_block.move_to(RIGHT * 4.2)

        # Vacuum gap brace
        gap_brace = DoubleArrow(LEFT * 2.4 + UP * 1.5, RIGHT * 2.4 + UP * 1.5, color=INK, buff=0,
                                stroke_width=2, max_tip_length_to_length_ratio=0.08)

        # Classical barrier (CRIMSON rectangle)
        cross_bar = Rectangle(width=4.8, height=0.5).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        cross_bar.move_to(DOWN * 0.3)

        # Tunneling wave (TEAL)
        tunnel_pts = [LEFT * 2.4 + RIGHT * t * 0.18 +
                      UP * 0.35 * np.exp(-t * 0.55) * np.sin(t * 1.2)
                      for t in range(28)]
        tunnel_wave = VMobject(color=TEAL, stroke_width=3)
        tunnel_wave.set_points_smoothly(tunnel_pts)

        # Probability arrow pointing down (TEAL)
        prob_arr = Arrow(LEFT * 0.5 + UP * 2.2, LEFT * 0.5 + UP * 0.8, color=TEAL, buff=0,
                         stroke_width=3, max_tip_length_to_length_ratio=0.2)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(GrowFromCenter(left_block), run_time=0.5)
        self.play(GrowFromCenter(right_block), run_time=0.5)
        self.play(GrowArrow(gap_brace), run_time=0.4)
        self.play(GrowFromCenter(cross_bar), run_time=0.4)
        self.play(Create(tunnel_wave), run_time=0.6)
        self.play(GrowArrow(prob_arr), run_time=0.4)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B06 — THE MECHANISM section card (CARD beat)
# ---------------------------------------------------------------------------
class B06_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B06", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 1.9)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        teal_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=3).move_to(UP * 1.05)
        headline_bg = Rectangle(width=12.5, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        headline_bg.move_to(UP * 0.2)
        formula_box = Rectangle(width=9.5, height=1.2).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 5.3 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 5.3 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("Tunneling decays as", font=DISPLAY, font_size=44, color=INK).move_to(UP * 0.2)
        formula = Text("e to the minus 2 kappa d", font=DISPLAY, font_size=34,
                       color=TEAL).move_to(DOWN * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(GrowFromCenter(headline_bg), run_time=0.3)
        self.play(Write(headline), run_time=0.5)
        self.play(GrowFromCenter(formula_box), run_time=0.4)
        self.play(FadeIn(teal_dot1), FadeIn(teal_dot2), run_time=0.3)
        self.play(Write(formula), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B07 — Wavefunction decay: e^(-2κd), κ≈1Å⁻¹, each Å gives ×7.4 (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_WavefunctionDecay(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left conductor wall
        left_wall = Rectangle(width=2.5, height=5.5).set_fill(SLATE, 0.5).set_stroke(INK, 2)
        left_wall.move_to(LEFT * 5.5)

        # Exponential decay envelope (TEAL)
        x_vals = np.linspace(0, 6.5, 80)
        decay_pts_top = [LEFT * 4.2 + RIGHT * x + UP * 2.0 * np.exp(-0.9 * x) for x in x_vals]
        decay_pts_bot = [LEFT * 4.2 + RIGHT * x + DOWN * 2.0 * np.exp(-0.9 * x) for x in x_vals]
        decay_top = VMobject(color=TEAL, stroke_width=3)
        decay_top.set_points_smoothly(decay_pts_top)
        decay_bot = VMobject(color=TEAL, stroke_width=3)
        decay_bot.set_points_smoothly(decay_pts_bot)

        # Formula box
        formula_box = Rectangle(width=7.5, height=1.1).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        formula_box.move_to(RIGHT * 3.8 + UP * 1.0)

        # kappa box
        kappa_box = Rectangle(width=6.5, height=0.8).set_fill(SLATE, 0.10).set_stroke(SLATE, 1.5)
        kappa_box.move_to(RIGHT * 3.5 + DOWN * 0.2)

        # Multiplier box
        mult_box = Rectangle(width=6.5, height=1.0).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        mult_box.move_to(RIGHT * 3.5 + DOWN * 1.5)

        # Decay marker dot at 1 Å
        marker_dot = Dot(radius=0.15, color=TEAL).move_to(LEFT * 4.2 + RIGHT * 1.1 + UP * 0.68)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(left_wall), run_time=0.5)
        self.play(Create(decay_top), Create(decay_bot), run_time=0.7)
        self.play(FadeIn(marker_dot), run_time=0.3)
        self.play(GrowFromCenter(formula_box), run_time=0.5)
        self.play(GrowFromCenter(kappa_box), run_time=0.4)
        self.play(GrowFromCenter(mult_box), run_time=0.4)
        self.wait(max(0.1, duration - 3.8))


# ---------------------------------------------------------------------------
# B08 — Log current vs distance: straight line on log scale (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_LogPlot(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        ax_origin = LEFT * 4.5 + DOWN * 2.5
        x_ax = Arrow(ax_origin, ax_origin + RIGHT * 8.5, color=INK, buff=0,
                     stroke_width=2, max_tip_length_to_length_ratio=0.05)
        y_ax = Arrow(ax_origin, ax_origin + UP * 5.8, color=INK, buff=0,
                     stroke_width=2, max_tip_length_to_length_ratio=0.05)

        # Classical: curved (CRIMSON)
        classical_pts = [ax_origin + RIGHT * (0.5 + t * 0.5) + UP * (5.2 / (1.0 + t * 0.55))
                         for t in range(14)]
        classical_curve = VMobject(color=CRIMSON, stroke_width=2.5)
        classical_curve.set_points_smoothly(classical_pts)

        # Classical label box
        classical_lbl_box = Rectangle(width=3.8, height=0.7).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.2)
        classical_lbl_box.move_to(ax_origin + RIGHT * 1.8 + UP * 4.5)

        # Exponential: straight line (TEAL)
        exp_start = ax_origin + RIGHT * 0.5 + UP * 5.3
        exp_end   = ax_origin + RIGHT * 7.8 + UP * 0.2
        exp_line  = Line(exp_start, exp_end, color=TEAL, stroke_width=3)

        # Exp label box
        exp_lbl_box = Rectangle(width=5.0, height=0.7).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.5)
        exp_lbl_box.move_to(ax_origin + RIGHT * 5.5 + UP * 3.2)

        # Slope annotation box
        slope_box = Rectangle(width=4.0, height=0.8).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        slope_box.move_to(ax_origin + RIGHT * 3.5 + UP * 1.4)

        # Difference callout dot
        diff_dot = Dot(radius=0.18, color=TEAL).move_to(ax_origin + RIGHT * 4.5 + UP * 2.5)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowArrow(x_ax), GrowArrow(y_ax), run_time=0.5)
        self.play(Create(classical_curve), run_time=0.6)
        self.play(GrowFromCenter(classical_lbl_box), run_time=0.4)
        self.play(Create(exp_line), run_time=0.5)
        self.play(GrowFromCenter(exp_lbl_box), run_time=0.4)
        self.play(GrowFromCenter(slope_box), run_time=0.4)
        self.play(FadeIn(diff_dot), run_time=0.3)
        self.wait(max(0.1, duration - 4.2))


# ---------------------------------------------------------------------------
# B09 — THE IMPLICATION section card (CARD beat)
# ---------------------------------------------------------------------------
class B09_ImplicationCard(Scene):
    def construct(self):
        duration = DUR.get("B09", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 1.9)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        teal_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=3).move_to(UP * 1.05)
        headline_bg = Rectangle(width=12.5, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        headline_bg.move_to(UP * 0.2)
        formula_box = Rectangle(width=8.5, height=1.2).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 4.8 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 4.8 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE IMPLICATION", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 1.9)
        headline = Text("The exponential reads", font=DISPLAY, font_size=44,
                        color=INK).move_to(UP * 0.2)
        formula = Text("single-atom bumps", font=DISPLAY, font_size=38,
                       color=TEAL).move_to(DOWN * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(GrowFromCenter(headline_bg), run_time=0.3)
        self.play(Write(headline), run_time=0.5)
        self.play(GrowFromCenter(formula_box), run_time=0.4)
        self.play(FadeIn(teal_dot1), FadeIn(teal_dot2), run_time=0.3)
        self.play(Write(formula), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B10 — STILL·ai: STM tip over atomic surface (no scene class needed)
# ---------------------------------------------------------------------------
# B10 is a STILL·ai beat — no Scene class here, the slate image is used directly.


# ---------------------------------------------------------------------------
# B11 — Without exponential, no atomic resolution (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_ResolutionArgument(Scene):
    def construct(self):
        duration = DUR.get("B11", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left: linear (CRIMSON)
        box_linear = Rectangle(width=5.5, height=4.5).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 2)
        box_linear.move_to(LEFT * 3.5 + DOWN * 0.5)

        # Right: exponential (TEAL)
        box_exp = Rectangle(width=5.5, height=4.5).set_fill(TEAL, 0.06).set_stroke(TEAL, 2)
        box_exp.move_to(RIGHT * 3.5 + DOWN * 0.5)

        # Divider
        divider = Line(UP * 2.8, DOWN * 3.8, color=INK, stroke_width=1.5).set_opacity(0.4)

        # Label boxes
        label_linear_box = Rectangle(width=3.5, height=0.65).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 1.5)
        label_linear_box.move_to(LEFT * 3.5 + UP * 1.8)
        label_exp_box = Rectangle(width=4.5, height=0.65).set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        label_exp_box.move_to(RIGHT * 3.5 + UP * 1.8)

        # Current arrows (linear: similar heights)
        arr_lin1 = Arrow(LEFT * 4.5 + DOWN * 1.5, LEFT * 4.5 + DOWN * 0.85,
                         color=CRIMSON, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.3)
        arr_lin2 = Arrow(LEFT * 3.5 + DOWN * 1.5, LEFT * 3.5 + DOWN * 0.65,
                         color=CRIMSON, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.3)
        arr_lin3 = Arrow(LEFT * 2.5 + DOWN * 1.5, LEFT * 2.5 + DOWN * 0.85,
                         color=CRIMSON, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.3)

        # Current arrows (exponential: middle dramatically taller)
        arr_exp1 = Arrow(RIGHT * 2.5 + DOWN * 1.5, RIGHT * 2.5 + DOWN * 0.85,
                         color=TEAL, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.3)
        arr_exp2 = Arrow(RIGHT * 3.5 + DOWN * 1.5, RIGHT * 3.5 + UP * 1.0,
                         color=TEAL, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.15)
        arr_exp3 = Arrow(RIGHT * 4.5 + DOWN * 1.5, RIGHT * 4.5 + DOWN * 0.85,
                         color=TEAL, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.3)

        # Conclusion box
        conclusion_box = Rectangle(width=8.5, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        conclusion_box.move_to(DOWN * 3.0)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(box_linear), GrowFromCenter(box_exp), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(label_linear_box), GrowFromCenter(label_exp_box), run_time=0.4)
        self.play(GrowArrow(arr_lin1), GrowArrow(arr_lin2), GrowArrow(arr_lin3), run_time=0.5)
        self.play(GrowArrow(arr_exp1), GrowArrow(arr_exp2), GrowArrow(arr_exp3), run_time=0.5)
        self.play(GrowFromCenter(conclusion_box), run_time=0.4)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B12 — THE EXAMPLE card (CARD beat)
# ---------------------------------------------------------------------------
class B12_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B12", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 2.0)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.2)
        headline_box = Rectangle(width=11.0, height=1.1).set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        headline_box.move_to(UP * 0.3)
        sub_bar = Rectangle(width=4.0, height=0.6).set_fill(SLATE, 0.12).set_stroke(SLATE, 1)
        sub_bar.move_to(DOWN * 0.9)
        accent_rule = Line(LEFT * 3.5, RIGHT * 3.5, color=TEAL, stroke_width=2).move_to(DOWN * 0.35)
        teal_dot = Dot(radius=0.12, color=TEAL).move_to(LEFT * 3.8 + DOWN * 0.35)
        teal_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.35)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.6)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.0)
        headline = Text("Tip over silicon at 5 angstroms", font=DISPLAY, font_size=38,
                        color=INK).move_to(UP * 0.3)
        sub = Text("(illustrative)", font=SERIF, font_size=24,
                   color=SLATE).move_to(DOWN * 0.9)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(headline_box), run_time=0.4)
        self.play(Write(headline), run_time=0.5)
        self.play(Create(accent_rule), run_time=0.3)
        self.play(FadeIn(teal_dot), FadeIn(teal_dot2), run_time=0.3)
        self.play(GrowFromCenter(sub_bar), run_time=0.3)
        self.play(FadeIn(sub), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B13 — Worked example: φ=4eV, κ=1.02Å⁻¹, gap 4/5/6 Å (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 19.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Kappa box at top
        kappa_box = Rectangle(width=8.0, height=0.75).set_fill(SLATE, 0.10).set_stroke(SLATE, 1.5)
        kappa_box.move_to(UP * 2.4)

        # Gap 5 Å: current I_0 (baseline)
        box5 = Rectangle(width=4.0, height=2.3).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        box5.move_to(LEFT * 5.0 + UP * 0.5)

        # Gap 6 Å: current I_0 / 7.4
        box6 = Rectangle(width=4.0, height=2.3).set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2)
        box6.move_to(ORIGIN + UP * 0.5)

        # Gap 4 Å: current 7.4 × I_0
        box4 = Rectangle(width=4.0, height=2.3).set_fill(TEAL, 0.22).set_stroke(TEAL, 2.5)
        box4.move_to(RIGHT * 5.0 + UP * 0.5)

        # Connection lines between boxes
        conn1 = Arrow(LEFT * 3.0 + UP * 0.5, LEFT * 2.05 + UP * 0.5, color=CRIMSON, buff=0,
                      stroke_width=2, max_tip_length_to_length_ratio=0.3)
        conn2 = Arrow(RIGHT * 2.05 + UP * 0.5, RIGHT * 3.0 + UP * 0.5, color=TEAL, buff=0,
                      stroke_width=2, max_tip_length_to_length_ratio=0.3)

        # Bottom conclusion bar
        conclusion_box = Rectangle(width=13.0, height=0.9).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        conclusion_box.move_to(DOWN * 2.5)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(kappa_box), run_time=0.4)
        self.play(GrowFromCenter(box5), run_time=0.5)
        self.play(GrowFromCenter(box6), run_time=0.5)
        self.play(GrowFromCenter(box4), run_time=0.5)
        self.play(GrowArrow(conn1), GrowArrow(conn2), run_time=0.5)
        self.play(GrowFromCenter(conclusion_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.2))


# ---------------------------------------------------------------------------
# B14 — RECAP endcard (CARD beat)
# ---------------------------------------------------------------------------
class B14_Recap(Scene):
    def construct(self):
        duration = DUR.get("B14", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 2.8)
        rule1 = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        highlight_box = Rectangle(width=12.5, height=1.1).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        highlight_box.move_to(UP * 1.3)
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=1.5).move_to(DOWN * 0.0)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.0)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.0)
        content_box = Rectangle(width=12.5, height=1.4).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        content_box.move_to(DOWN * 0.45)
        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.2)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        line1 = Text("Each angstrom of gap multiplies current by e-squared ~7.", font=DISPLAY,
                     font_size=26, color=TEAL).move_to(UP * 1.3)
        line2 = Text("The exponential of quantum tunneling", font=SERIF, font_size=26,
                     color=INK).move_to(UP * 0.4)
        line3 = Text("gives the STM its atomic resolution.", font=SERIF, font_size=26,
                     color=INK).move_to(DOWN * 0.5)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(highlight_box), run_time=0.4)
        self.play(Write(line1), run_time=0.5)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(accent_dot1), FadeIn(accent_dot2), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.3)
        self.play(Write(line2), run_time=0.4)
        self.play(Write(line3), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.0))
