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
        mid_box = Rectangle(width=13.0, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        mid_box.move_to(UP * 0.2)
        rule2 = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 1.5)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.9)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.9)
        mid_rule = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=0.8).move_to(DOWN * 0.5)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline = Text("Why a Stationary State Isn't Standing Still", font=DISPLAY, font_size=32,
                        color=INK).move_to(UP * 0.2)
        sub = Text("The invisible spin", font=SERIF, font_size=26,
                   color=TEAL).move_to(DOWN * 0.9)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(mid_box), run_time=0.4)
        self.play(Write(headline), run_time=0.4)
        self.play(Create(mid_rule), run_time=0.3)
        self.play(FadeIn(accent_dot1), FadeIn(accent_dot2), run_time=0.3)
        self.play(Create(rule2), run_time=0.3)
        self.play(Write(sub), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B02 — Single phasor rotating; |ψ|² flat (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_SinglePhasor(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left panel: phasor diagram
        panel_left = Rectangle(width=6.5, height=6.5).set_fill(SLATE, 0.05).set_stroke(SLATE, 1.5)
        panel_left.move_to(LEFT * 3.8 + DOWN * 0.3)

        # Complex plane circle
        circle = Circle(radius=1.8, color=TEAL, stroke_width=2).move_to(LEFT * 3.8 + DOWN * 0.3)

        # Phasor arrow (rotating)
        phasor = Arrow(LEFT * 3.8 + DOWN * 0.3,
                       LEFT * 3.8 + DOWN * 0.3 + RIGHT * 1.8,
                       color=TEAL, buff=0, stroke_width=3,
                       max_tip_length_to_length_ratio=0.25)

        # Right panel: probability density (flat)
        panel_right = Rectangle(width=6.5, height=6.5).set_fill(CRIMSON, 0.04).set_stroke(CRIMSON, 1.5)
        panel_right.move_to(RIGHT * 3.8 + DOWN * 0.3)

        # Flat probability density line
        prob_flat = Line(RIGHT * 0.7, RIGHT * 6.9, color=CRIMSON, stroke_width=3).move_to(DOWN * 0.3)

        # Label boxes
        label_left = Rectangle(width=4.5, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_left.move_to(LEFT * 3.8 + UP * 2.7)
        label_right = Rectangle(width=4.5, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        label_right.move_to(RIGHT * 3.8 + UP * 2.7)

        divider = Line(UP * 2.5, DOWN * 3.5, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(panel_left), GrowFromCenter(panel_right), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(Create(circle), run_time=0.4)
        self.play(GrowArrow(phasor), run_time=0.4)
        self.play(GrowFromCenter(label_left), GrowFromCenter(label_right), run_time=0.4)
        self.play(Create(prob_flat), run_time=0.4)
        self.wait(max(0.1, duration - 3.4))


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
        content_box = Rectangle(width=13.5, height=2.6).set_fill(SLATE, 0.05).set_stroke(SLATE, 1)
        content_box.move_to(UP * 0.6)
        inner_box = Rectangle(width=12.0, height=1.1).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        inner_box.move_to(DOWN * 0.2)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 3.5 + DOWN * 0.2)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 3.5 + DOWN * 0.2)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.0).move_to(DOWN * 2.0)
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=2).move_to(DOWN * 1.0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.8)
        line1 = Text("If a stationary state never oscillates,", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 1.3)
        line2 = Text("where do spectral lines come from?", font=SERIF,
                     font_size=24, color=TEAL).move_to(DOWN * 0.2)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(Write(line1), run_time=0.3)
        self.play(GrowFromCenter(inner_box), run_time=0.3)
        self.play(FadeIn(teal_dot1), FadeIn(teal_dot2), run_time=0.3)
        self.play(Write(line2), run_time=0.3)
        self.play(Create(rule2), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.4))


# ---------------------------------------------------------------------------
# B04 — Classical: oscillating charge emits, static charge silent (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalSilence(Scene):
    def construct(self):
        duration = DUR.get("B04", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left: oscillating charge (emits) — TEAL
        box_emit = Rectangle(width=6.0, height=4.5).set_fill(TEAL, 0.06).set_stroke(TEAL, 2)
        box_emit.move_to(LEFT * 3.8 + DOWN * 0.5)
        label_emit = Rectangle(width=4.2, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_emit.move_to(LEFT * 3.8 + UP * 1.8)
        charge_emit = Dot(radius=0.3, color=TEAL).move_to(LEFT * 3.8 + DOWN * 0.5)
        emit_arrow = Arrow(LEFT * 3.8 + DOWN * 0.5, LEFT * 1.2 + DOWN * 0.5,
                           color=TEAL, buff=0.3, stroke_width=3,
                           max_tip_length_to_length_ratio=0.2)
        result_emit = Rectangle(width=3.8, height=0.65).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        result_emit.move_to(LEFT * 3.8 + DOWN * 2.2)

        # Right: static charge (silent) — CRIMSON
        box_silent = Rectangle(width=6.0, height=4.5).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 2)
        box_silent.move_to(RIGHT * 3.8 + DOWN * 0.5)
        label_silent = Rectangle(width=4.2, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        label_silent.move_to(RIGHT * 3.8 + UP * 1.8)
        charge_static = Dot(radius=0.3, color=CRIMSON).move_to(RIGHT * 3.8 + DOWN * 0.5)
        result_silent = Rectangle(width=3.8, height=0.65).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        result_silent.move_to(RIGHT * 3.8 + DOWN * 2.2)

        divider = Line(UP * 2.5, DOWN * 3.0, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(box_emit), GrowFromCenter(box_silent), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(label_emit), GrowFromCenter(label_silent), run_time=0.4)
        self.play(FadeIn(charge_emit), FadeIn(charge_static), run_time=0.3)
        self.play(GrowArrow(emit_arrow), run_time=0.4)
        self.play(GrowFromCenter(result_emit), run_time=0.4)
        self.play(GrowFromCenter(result_silent), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


# ---------------------------------------------------------------------------
# B05 — Single eigenstate: phase rotates but |ψ|² flat (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_InvisibleRotation(Scene):
    def construct(self):
        duration = DUR.get("B05", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Complex plane panel
        phase_panel = Rectangle(width=6.0, height=5.5).set_fill(SLATE, 0.05).set_stroke(SLATE, 1.5)
        phase_panel.move_to(LEFT * 3.5 + DOWN * 0.2)

        # Unit circle
        unit_circle = Circle(radius=1.8, color=TEAL, stroke_width=2).move_to(LEFT * 3.5 + DOWN * 0.2)

        # Axes
        axis_re = Line(LEFT * 5.0 + DOWN * 0.2, LEFT * 2.0 + DOWN * 0.2, color=INK, stroke_width=1).set_opacity(0.4)
        axis_im = Line(LEFT * 3.5 + DOWN * 2.0, LEFT * 3.5 + UP * 1.6, color=INK, stroke_width=1).set_opacity(0.4)

        # Phasor at angle 45 deg
        phasor_end = LEFT * 3.5 + DOWN * 0.2 + RIGHT * 1.8 * np.cos(np.pi / 4) + UP * 1.8 * np.sin(np.pi / 4)
        phasor = Arrow(LEFT * 3.5 + DOWN * 0.2, phasor_end,
                       color=TEAL, buff=0, stroke_width=3.5,
                       max_tip_length_to_length_ratio=0.25)

        # Phase label box
        phase_label_box = Rectangle(width=3.5, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        phase_label_box.move_to(LEFT * 3.5 + DOWN * 2.4)

        # Right: probability density (flat) panel
        prob_panel = Rectangle(width=6.0, height=5.5).set_fill(CRIMSON, 0.04).set_stroke(CRIMSON, 1.5)
        prob_panel.move_to(RIGHT * 3.5 + DOWN * 0.2)

        # Flat |ψ|² line
        x_vals = np.linspace(-0.5, 6.5, 40)
        density_pts = [RIGHT * (0.7 + v * 5.6 / 6.0) + DOWN * 0.2 for v in np.linspace(0, 1, 40)]
        prob_line = VMobject(color=CRIMSON, stroke_width=3)
        prob_line.set_points_smoothly(density_pts)

        # Constant label box
        const_box = Rectangle(width=3.8, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        const_box.move_to(RIGHT * 3.5 + DOWN * 2.4)

        divider = Line(UP * 2.5, DOWN * 3.5, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(phase_panel), GrowFromCenter(prob_panel), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(Create(unit_circle), run_time=0.4)
        self.play(Create(axis_re), Create(axis_im), run_time=0.3)
        self.play(GrowArrow(phasor), run_time=0.4)
        self.play(GrowFromCenter(phase_label_box), run_time=0.3)
        self.play(Create(prob_line), run_time=0.5)
        self.play(GrowFromCenter(const_box), run_time=0.3)
        self.wait(max(0.1, duration - 4.2))


# ---------------------------------------------------------------------------
# B06 — THE MECHANISM card (CARD beat)
# ---------------------------------------------------------------------------
class B06_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B06", 6.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 1.9)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        teal_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=3).move_to(UP * 1.05)
        headline_bg = Rectangle(width=12.5, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        headline_bg.move_to(UP * 0.2)
        formula_box = Rectangle(width=9.0, height=0.9).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 5.5 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 5.5 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("Two phases beat at the Bohr frequency", font=DISPLAY, font_size=34,
                        color=INK).move_to(UP * 0.2)
        formula = Text("f = (E₂ − E₁) / h", font=MONO, font_size=28,
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
# B07 — Two phasors beating; |ψ|² oscillating (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_TwoPhasors(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left: two-phasor panel
        phasor_panel = Rectangle(width=6.5, height=6.0).set_fill(SLATE, 0.05).set_stroke(SLATE, 1.5)
        phasor_panel.move_to(LEFT * 3.8 + DOWN * 0.2)

        # Unit circle
        unit_circ = Circle(radius=1.7, color=TEAL, stroke_width=1.5).set_opacity(0.4).move_to(LEFT * 3.8 + DOWN * 0.2)

        # Phasor 1 (E1, slower rotation) — TEAL
        p1 = Arrow(LEFT * 3.8 + DOWN * 0.2,
                   LEFT * 3.8 + DOWN * 0.2 + RIGHT * 1.5,
                   color=TEAL, buff=0, stroke_width=3,
                   max_tip_length_to_length_ratio=0.22)
        # Phasor 2 (E2, faster rotation) — offset angle
        angle2 = np.pi / 3
        p2 = Arrow(LEFT * 3.8 + DOWN * 0.2,
                   LEFT * 3.8 + DOWN * 0.2 + RIGHT * 1.5 * np.cos(angle2) + UP * 1.5 * np.sin(angle2),
                   color=GOLD, buff=0, stroke_width=3,
                   max_tip_length_to_length_ratio=0.22)

        # Difference arrow
        diff_arr = Arrow(LEFT * 3.8 + DOWN * 0.2 + RIGHT * 1.5,
                         LEFT * 3.8 + DOWN * 0.2 + RIGHT * 1.5 * np.cos(angle2) + UP * 1.5 * np.sin(angle2),
                         color=CRIMSON, buff=0, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.2)

        # Right: oscillating probability density panel
        prob_panel = Rectangle(width=6.5, height=6.0).set_fill(TEAL, 0.04).set_stroke(TEAL, 1.5)
        prob_panel.move_to(RIGHT * 3.8 + DOWN * 0.2)

        # Oscillating density curve
        x_vals = np.linspace(0, np.pi * 2, 60)
        osc_pts = [RIGHT * (0.7 + v * 5.6 / (2 * np.pi)) + DOWN * 0.2 +
                   UP * 0.8 * np.sin(v) for i, v in enumerate(x_vals)]
        osc_curve = VMobject(color=TEAL, stroke_width=3)
        osc_curve.set_points_smoothly(osc_pts)

        # Beat frequency label box
        beat_box = Rectangle(width=4.5, height=0.7).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        beat_box.move_to(RIGHT * 3.8 + DOWN * 2.5)

        divider = Line(UP * 2.5, DOWN * 3.5, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(phasor_panel), GrowFromCenter(prob_panel), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(Create(unit_circ), run_time=0.3)
        self.play(GrowArrow(p1), run_time=0.4)
        self.play(GrowArrow(p2), run_time=0.4)
        self.play(GrowArrow(diff_arr), run_time=0.4)
        self.play(Create(osc_curve), run_time=0.6)
        self.play(GrowFromCenter(beat_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B08 — Probability cloud rocks back and forth → spectral emission (GRAPHIC)
# ---------------------------------------------------------------------------
class B08_ProbabilitySlosh(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Box for particle
        wall_left = Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=4).move_to(LEFT * 5.0)
        wall_right = Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=4).move_to(RIGHT * 0.5)

        # Sloshing probability density (shifted left — peak at left)
        x_vals = np.linspace(0, np.pi, 50)
        pts_left = [LEFT * 5.0 + RIGHT * (i / (len(x_vals) - 1)) * 5.5 +
                    UP * 1.5 * np.sin(x) + DOWN * 0.5 for i, x in enumerate(x_vals)]
        density_slosh = VMobject(color=TEAL, stroke_width=3)
        density_slosh.set_points_smoothly(pts_left)

        # Floor line
        floor_line = Line(LEFT * 5.5, RIGHT * 1.0, color=INK, stroke_width=1.5).move_to(DOWN * 2.2)

        # Emission arrow (photon out to the right)
        emission_arr = Arrow(RIGHT * 0.7 + DOWN * 0.5, RIGHT * 4.5 + DOWN * 0.5,
                             color=TEAL, buff=0, stroke_width=3,
                             max_tip_length_to_length_ratio=0.2)

        # Frequency label box
        freq_box = Rectangle(width=5.0, height=0.8).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        freq_box.move_to(RIGHT * 3.0 + UP * 0.8)

        # Bottom conclusion box
        conclusion_box = Rectangle(width=12.0, height=0.9).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        conclusion_box.move_to(DOWN * 3.0)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(wall_left), Create(wall_right), run_time=0.5)
        self.play(Create(floor_line), run_time=0.3)
        self.play(Create(density_slosh), run_time=0.6)
        self.play(GrowArrow(emission_arr), run_time=0.4)
        self.play(GrowFromCenter(freq_box), run_time=0.4)
        self.play(GrowFromCenter(conclusion_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


# ---------------------------------------------------------------------------
# B09 — THE IMPLICATION card (CARD beat)
# ---------------------------------------------------------------------------
class B09_ImplicationCard(Scene):
    def construct(self):
        duration = DUR.get("B09", 5.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 1.9)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        teal_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=3).move_to(UP * 1.05)
        headline_bg = Rectangle(width=12.5, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        headline_bg.move_to(UP * 0.2)
        imply_box = Rectangle(width=10.0, height=1.1).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        imply_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 6.0 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 6.0 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE IMPLICATION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("Every spectral line is a beating pair of phases", font=DISPLAY,
                        font_size=32, color=INK).move_to(UP * 0.2)
        imply = Text("single phase: silent   ·   two phases: spectral line", font=DISPLAY,
                     font_size=24, color=TEAL).move_to(DOWN * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(GrowFromCenter(headline_bg), run_time=0.3)
        self.play(Write(headline), run_time=0.5)
        self.play(GrowFromCenter(imply_box), run_time=0.4)
        self.play(FadeIn(teal_dot1), FadeIn(teal_dot2), run_time=0.3)
        self.play(Write(imply), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B10 — STILL·ai: hydrogen Balmer spectrum (no Scene class needed)
# ---------------------------------------------------------------------------
# B10 is a STILL·ai beat — no Scene class here.


# ---------------------------------------------------------------------------
# B11 — Single vs two eigenstates: silence vs beating (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_SingleVsTwo(Scene):
    def construct(self):
        duration = DUR.get("B11", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left panel: one phasor — silent (CRIMSON)
        box_one = Rectangle(width=5.5, height=5.5).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 2)
        box_one.move_to(LEFT * 3.5 + DOWN * 0.3)
        label_one = Rectangle(width=4.2, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        label_one.move_to(LEFT * 3.5 + UP * 2.2)
        circ_one = Circle(radius=1.4, color=CRIMSON, stroke_width=2).set_opacity(0.5).move_to(LEFT * 3.5 + DOWN * 0.3)
        arrow_one = Arrow(LEFT * 3.5 + DOWN * 0.3, LEFT * 3.5 + DOWN * 0.3 + RIGHT * 1.4,
                          color=CRIMSON, buff=0, stroke_width=3,
                          max_tip_length_to_length_ratio=0.25)
        silent_box = Rectangle(width=3.5, height=0.65).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        silent_box.move_to(LEFT * 3.5 + DOWN * 2.5)

        # Right panel: two phasors — beating (TEAL)
        box_two = Rectangle(width=5.5, height=5.5).set_fill(TEAL, 0.05).set_stroke(TEAL, 2)
        box_two.move_to(RIGHT * 3.5 + DOWN * 0.3)
        label_two = Rectangle(width=4.2, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_two.move_to(RIGHT * 3.5 + UP * 2.2)
        circ_two = Circle(radius=1.4, color=TEAL, stroke_width=2).set_opacity(0.5).move_to(RIGHT * 3.5 + DOWN * 0.3)
        arrow_two_a = Arrow(RIGHT * 3.5 + DOWN * 0.3, RIGHT * 3.5 + DOWN * 0.3 + RIGHT * 1.4,
                            color=TEAL, buff=0, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.22)
        arrow_two_b = Arrow(RIGHT * 3.5 + DOWN * 0.3,
                            RIGHT * 3.5 + DOWN * 0.3 + RIGHT * 1.0 + UP * 1.0,
                            color=GOLD, buff=0, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.22)
        beat_result = Rectangle(width=3.5, height=0.65).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        beat_result.move_to(RIGHT * 3.5 + DOWN * 2.5)

        divider = Line(UP * 2.5, DOWN * 3.5, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(box_one), GrowFromCenter(box_two), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(label_one), GrowFromCenter(label_two), run_time=0.4)
        self.play(Create(circ_one), Create(circ_two), run_time=0.4)
        self.play(GrowArrow(arrow_one), run_time=0.3)
        self.play(GrowArrow(arrow_two_a), GrowArrow(arrow_two_b), run_time=0.4)
        self.play(GrowFromCenter(silent_box), run_time=0.3)
        self.play(GrowFromCenter(beat_result), run_time=0.3)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B12 — THE EXAMPLE card (CARD beat)
# ---------------------------------------------------------------------------
class B12_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B12", 4.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        eyebrow_bar.move_to(UP * 2.0)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.2)
        headline_box = Rectangle(width=10.0, height=1.1).set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        headline_box.move_to(UP * 0.3)
        sub_bar = Rectangle(width=4.0, height=0.6).set_fill(SLATE, 0.12).set_stroke(SLATE, 1)
        sub_bar.move_to(DOWN * 0.9)
        accent_rule = Line(LEFT * 3.5, RIGHT * 3.5, color=TEAL, stroke_width=2).move_to(DOWN * 0.35)
        teal_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 3.8 + DOWN * 0.35)
        teal_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.35)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.6)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.0)
        headline = Text("Particle in a 1 nm box", font=DISPLAY, font_size=38,
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
        self.play(FadeIn(teal_dot1), FadeIn(teal_dot2), run_time=0.3)
        self.play(GrowFromCenter(sub_bar), run_time=0.3)
        self.play(FadeIn(sub), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B13 — Worked example: E₁, E₂, ΔE, frequency (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 18.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Formula row box (top)
        formula_box = Rectangle(width=10.0, height=0.75).set_fill(SLATE, 0.10).set_stroke(SLATE, 1.5)
        formula_box.move_to(UP * 2.4)

        # E1 box (left)
        e1_box = Rectangle(width=4.5, height=2.2).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        e1_box.move_to(LEFT * 5.0 + UP * 0.5)

        # E2 box (center-left)
        e2_box = Rectangle(width=4.5, height=2.2).set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
        e2_box.move_to(LEFT * 0.2 + UP * 0.5)

        # Delta E arrow between E1 and E2
        delta_arr = Arrow(LEFT * 2.7 + UP * 0.5, LEFT * 0.5 + RIGHT * 0.5 + UP * 0.5,
                          color=TEAL, buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.2)

        # Delta E label box
        delta_box = Rectangle(width=3.2, height=0.7).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        delta_box.move_to(LEFT * 1.6 + UP * 0.5)

        # Frequency result box (right)
        freq_box = Rectangle(width=4.5, height=2.2).set_fill(TEAL, 0.18).set_stroke(TEAL, 2.5)
        freq_box.move_to(RIGHT * 4.5 + UP * 0.5)

        # Conclusion bar
        conclusion_bar = Rectangle(width=12.5, height=0.9).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        conclusion_bar.move_to(DOWN * 2.5)

        # Bottom accent rule
        bottom_rule = Line(LEFT * 6.0, RIGHT * 6.0, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.2)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(formula_box), run_time=0.4)
        self.play(GrowFromCenter(e1_box), run_time=0.4)
        self.play(GrowFromCenter(e2_box), run_time=0.4)
        self.play(GrowArrow(delta_arr), run_time=0.4)
        self.play(GrowFromCenter(delta_box), run_time=0.3)
        self.play(GrowFromCenter(freq_box), run_time=0.4)
        self.play(GrowFromCenter(conclusion_bar), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.0))


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
        highlight_box = Rectangle(width=12.5, height=1.45).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        highlight_box.move_to(UP * 1.1)
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=1.5).move_to(DOWN * 0.0)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.0)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.0)
        content_box = Rectangle(width=12.5, height=1.7).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        content_box.move_to(DOWN * 0.6)
        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.7)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        line1 = Text("The phase rotates. Two phases beat.", font=DISPLAY,
                     font_size=28, color=TEAL).move_to(UP * 1.3)
        line2 = Text("Every spectral line is that beat.", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 0.7)
        line3 = Text("A stationary state is not static — it spins.", font=SERIF,
                     font_size=24, color=INK).move_to(DOWN * 0.3)
        line4 = Text("That is quantum mechanics.", font=SERIF,
                     font_size=22, color=INK).move_to(DOWN * 0.9)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(highlight_box), run_time=0.4)
        self.play(Write(line1), run_time=0.4)
        self.play(Write(line2), run_time=0.4)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(accent_dot1), FadeIn(accent_dot2), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.3)
        self.play(Write(line3), run_time=0.4)
        self.play(Write(line4), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.5))
