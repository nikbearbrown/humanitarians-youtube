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
        accent_dot = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.9)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.9)
        mid_rule = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=0.8).move_to(DOWN * 0.5)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline1 = Text("Why a Particle in a Box Cannot Sit Still", font=DISPLAY, font_size=34,
                         color=INK).move_to(UP * 0.2)
        headline2 = Text("The quantum energy floor", font=DISPLAY, font_size=28,
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
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B02 — Energy level ladder with floating ground state (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_EnergyLadder(Scene):
    def construct(self):
        duration = DUR.get("B02", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Box walls
        wall_left = Line(DOWN * 3.0, UP * 3.0, color=INK, stroke_width=4).move_to(LEFT * 3.5)
        wall_right = Line(DOWN * 3.0, UP * 3.0, color=INK, stroke_width=4).move_to(RIGHT * 3.5)
        floor_line = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=2).move_to(DOWN * 3.2)

        # Energy levels (TEAL)
        e1 = Line(LEFT * 2.8, RIGHT * 2.8, color=TEAL, stroke_width=3).move_to(LEFT * 0.0 + DOWN * 1.5)
        e2 = Line(LEFT * 2.8, RIGHT * 2.8, color=TEAL, stroke_width=2.5).move_to(LEFT * 0.0 + UP * 0.3)
        e3 = Line(LEFT * 2.8, RIGHT * 2.8, color=TEAL, stroke_width=2.0).move_to(LEFT * 0.0 + UP * 2.5)

        # Zero-point gap highlight
        gap_rect = Rectangle(width=7.0, height=1.7).set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        gap_rect.move_to(DOWN * 2.35)

        # Gap brace
        gap_brace = DoubleArrow(DOWN * 3.0, DOWN * 1.4, color=TEAL, buff=0,
                                stroke_width=2, max_tip_length_to_length_ratio=0.15)
        gap_brace.move_to(LEFT * 5.0 + DOWN * 2.2)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(wall_left), Create(wall_right), run_time=0.5)
        self.play(Create(floor_line), run_time=0.3)
        self.play(Create(e1), run_time=0.4)
        self.play(Create(e2), run_time=0.4)
        self.play(Create(e3), run_time=0.4)
        self.play(GrowFromCenter(gap_rect), run_time=0.4)
        self.play(GrowArrow(gap_brace), run_time=0.4)
        self.wait(max(0.1, duration - 3.6))


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
        line1 = Text("Classically, a particle at rest has zero energy.", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 1.3)
        line2 = Text("Here the ground state always floats above zero.", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 0.4)
        line3 = Text("Why can't the bottom rung sit on the floor?", font=SERIF,
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
        self.play(GrowFromCenter(question_box), run_time=0.3)
        self.play(Write(line3), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B04 — Classical expectation: particle can be stopped (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalRest(Scene):
    def construct(self):
        duration = DUR.get("B04", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Box
        wall_left = Line(DOWN * 2.5, UP * 1.5, color=INK, stroke_width=4).move_to(LEFT * 3.5 + DOWN * 0.5)
        wall_right = Line(DOWN * 2.5, UP * 1.5, color=INK, stroke_width=4).move_to(RIGHT * 3.5 + DOWN * 0.5)
        floor = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=2).move_to(DOWN * 3.2)

        # Classical particle as dot at floor level
        particle = Dot(radius=0.3, color=CRIMSON).move_to(DOWN * 2.8)
        motion_line = Line(DOWN * 2.8 + LEFT * 2.0, DOWN * 2.8 + RIGHT * 2.0,
                           color=CRIMSON, stroke_width=2)

        # Energy level at floor (CRIMSON)
        classical_e = Line(LEFT * 3.2, RIGHT * 3.2, color=CRIMSON, stroke_width=3).move_to(DOWN * 3.0)
        classical_label_box = Rectangle(width=3.5, height=0.7).set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.5)
        classical_label_box.move_to(RIGHT * 5.5 + DOWN * 3.0)

        # Down arrow: remove energy
        remove_arr = Arrow(DOWN * 1.8, DOWN * 2.8, color=CRIMSON, buff=0,
                           stroke_width=3, max_tip_length_to_length_ratio=0.2)
        remove_arr.move_to(LEFT * 5.0 + DOWN * 2.3)

        # Zero label
        zero_box = Rectangle(width=3.0, height=0.7).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        zero_box.move_to(LEFT * 5.0 + DOWN * 3.0)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(wall_left), Create(wall_right), run_time=0.5)
        self.play(Create(floor), run_time=0.3)
        self.play(FadeIn(particle), Create(motion_line), run_time=0.4)
        self.play(Create(classical_e), run_time=0.3)
        self.play(GrowFromCenter(classical_label_box), run_time=0.3)
        self.play(GrowArrow(remove_arr), run_time=0.4)
        self.play(GrowFromCenter(zero_box), run_time=0.4)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B05 — Wavefunction boundary conditions: half-wave fits (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_HalfWaveFit(Scene):
    def construct(self):
        duration = DUR.get("B05", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Box walls
        wall_left = Line(DOWN * 2.5, UP * 2.0, color=INK, stroke_width=4).move_to(LEFT * 4.0)
        wall_right = Line(DOWN * 2.5, UP * 2.0, color=INK, stroke_width=4).move_to(RIGHT * 4.0)

        # Boundary condition dots (zeros at walls)
        bc_dot_left = Dot(radius=0.18, color=TEAL).move_to(LEFT * 4.0 + DOWN * 0.5)
        bc_dot_right = Dot(radius=0.18, color=TEAL).move_to(RIGHT * 4.0 + DOWN * 0.5)

        # Half-wave fitting (TEAL)
        x_vals = np.linspace(0, np.pi, 50)
        wave_pts = [LEFT * 4.0 + RIGHT * (i / (len(x_vals) - 1)) * 8.0 +
                    UP * 1.8 * np.sin(x) for i, x in enumerate(x_vals)]
        half_wave = VMobject(color=TEAL, stroke_width=3)
        half_wave.set_points_smoothly(wave_pts)

        # Label: one half-wavelength
        half_brace = DoubleArrow(LEFT * 4.0 + DOWN * 2.0, RIGHT * 4.0 + DOWN * 2.0,
                                 color=TEAL, buff=0, stroke_width=2,
                                 max_tip_length_to_length_ratio=0.08)
        half_label_box = Rectangle(width=4.5, height=0.7).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.5)
        half_label_box.move_to(DOWN * 2.8)

        # Zero-crossings highlight
        bc_bar_left = Rectangle(width=0.6, height=3.5).set_fill(TEAL, 0.08).set_stroke(TEAL, 1)
        bc_bar_left.move_to(LEFT * 4.0 + DOWN * 0.3)
        bc_bar_right = Rectangle(width=0.6, height=3.5).set_fill(TEAL, 0.08).set_stroke(TEAL, 1)
        bc_bar_right.move_to(RIGHT * 4.0 + DOWN * 0.3)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(wall_left), Create(wall_right), run_time=0.5)
        self.play(GrowFromCenter(bc_bar_left), GrowFromCenter(bc_bar_right), run_time=0.4)
        self.play(FadeIn(bc_dot_left), FadeIn(bc_dot_right), run_time=0.3)
        self.play(Create(half_wave), run_time=0.7)
        self.play(GrowArrow(half_brace), run_time=0.4)
        self.play(GrowFromCenter(half_label_box), run_time=0.4)
        self.wait(max(0.1, duration - 3.8))


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
        formula_box = Rectangle(width=11.0, height=1.2).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 6.0 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 6.0 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("Fitting the half-wave forces curvature", font=DISPLAY, font_size=36,
                        color=INK).move_to(UP * 0.2)
        formula = Text("curvature is kinetic energy", font=DISPLAY, font_size=32,
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
# B07 — Flat wave vs curved wave: curvature = energy (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_CurvatureEnergy(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left panel: flat wave (CRIMSON = zero kinetic energy)
        flat_box = Rectangle(width=6.0, height=4.5).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 2)
        flat_box.move_to(LEFT * 4.0 + DOWN * 0.3)
        flat_label_box = Rectangle(width=4.0, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        flat_label_box.move_to(LEFT * 4.0 + UP * 1.8)
        flat_wave = Line(LEFT * 6.8 + DOWN * 0.3, LEFT * 1.2 + DOWN * 0.3,
                         color=CRIMSON, stroke_width=3)
        flat_e_box = Rectangle(width=3.5, height=0.65).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        flat_e_box.move_to(LEFT * 4.0 + DOWN * 1.8)

        # Right panel: curved wave (TEAL = nonzero kinetic energy)
        curved_box = Rectangle(width=6.0, height=4.5).set_fill(TEAL, 0.05).set_stroke(TEAL, 2)
        curved_box.move_to(RIGHT * 4.0 + DOWN * 0.3)
        curved_label_box = Rectangle(width=4.0, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        curved_label_box.move_to(RIGHT * 4.0 + UP * 1.8)

        x_vals = np.linspace(0, np.pi, 50)
        curve_pts = [RIGHT * 1.3 + RIGHT * (i / (len(x_vals) - 1)) * 5.4 +
                     UP * 1.4 * np.sin(x) + DOWN * 0.3 for i, x in enumerate(x_vals)]
        curved_wave = VMobject(color=TEAL, stroke_width=3)
        curved_wave.set_points_smoothly(curve_pts)

        curved_e_box = Rectangle(width=3.5, height=0.65).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        curved_e_box.move_to(RIGHT * 4.0 + DOWN * 1.8)

        divider = Line(UP * 2.5, DOWN * 3.0, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(flat_box), GrowFromCenter(curved_box), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(flat_label_box), GrowFromCenter(curved_label_box), run_time=0.4)
        self.play(Create(flat_wave), Create(curved_wave), run_time=0.7)
        self.play(GrowFromCenter(flat_e_box), run_time=0.4)
        self.play(GrowFromCenter(curved_e_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


# ---------------------------------------------------------------------------
# B08 — Narrower box: wave curves more, energy rises as 1/L² (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_NarrowerBox(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Wide box (TEAL, lower energy)
        wall_l_wide = Line(DOWN * 2.0, UP * 2.0, color=INK, stroke_width=3).move_to(LEFT * 4.5 + DOWN * 0.0)
        wall_r_wide = Line(DOWN * 2.0, UP * 2.0, color=INK, stroke_width=3).move_to(RIGHT * 0.5 + DOWN * 0.0)
        x_wide = np.linspace(0, np.pi, 50)
        pts_wide = [LEFT * 4.5 + RIGHT * (i / (len(x_wide) - 1)) * 5.0 +
                    UP * 1.0 * np.sin(x) for i, x in enumerate(x_wide)]
        wave_wide = VMobject(color=TEAL, stroke_width=2.5)
        wave_wide.set_points_smoothly(pts_wide)
        e_wide_box = Rectangle(width=2.8, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        e_wide_box.move_to(LEFT * 2.0 + DOWN * 1.8)

        # Narrow box (TEAL, higher energy)
        wall_l_narrow = Line(DOWN * 2.0, UP * 2.0, color=INK, stroke_width=3).move_to(RIGHT * 2.0 + DOWN * 0.0)
        wall_r_narrow = Line(DOWN * 2.0, UP * 2.0, color=INK, stroke_width=3).move_to(RIGHT * 4.5 + DOWN * 0.0)
        x_narrow = np.linspace(0, np.pi, 50)
        pts_narrow = [RIGHT * 2.0 + RIGHT * (i / (len(x_narrow) - 1)) * 2.5 +
                      UP * 1.6 * np.sin(x) for i, x in enumerate(x_narrow)]
        wave_narrow = VMobject(color=TEAL, stroke_width=2.5)
        wave_narrow.set_points_smoothly(pts_narrow)
        e_narrow_box = Rectangle(width=2.8, height=0.65).set_fill(TEAL, 0.22).set_stroke(TEAL, 2.0)
        e_narrow_box.move_to(RIGHT * 3.25 + DOWN * 1.8)

        # Scaling formula box
        formula_box = Rectangle(width=6.0, height=0.8).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 3.2)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(wall_l_wide), Create(wall_r_wide), run_time=0.5)
        self.play(Create(wave_wide), run_time=0.5)
        self.play(GrowFromCenter(e_wide_box), run_time=0.4)
        self.play(Create(wall_l_narrow), Create(wall_r_narrow), run_time=0.5)
        self.play(Create(wave_narrow), run_time=0.5)
        self.play(GrowFromCenter(e_narrow_box), run_time=0.4)
        self.play(GrowFromCenter(formula_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.3))


# ---------------------------------------------------------------------------
# B09 — THE IMPLICATION card (CARD beat)
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
        formula_box = Rectangle(width=7.0, height=1.2).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 4.0 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 4.0 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE IMPLICATION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("Tighter box,", font=DISPLAY, font_size=44, color=INK).move_to(UP * 0.2)
        formula = Text("higher floor", font=DISPLAY, font_size=38, color=TEAL).move_to(DOWN * 1.1)
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
# B10 — STILL·ai: liquid helium refusing to freeze (no scene class needed)
# ---------------------------------------------------------------------------
# B10 — confinement beyond the box: zero-point motion blocks freezing
# Rebuilt as native motion so the free-only Claude-Liam cut carries no AI-media slate.
class B10_ZeroPointHelium(Scene):
    def construct(self):
        duration = DUR.get("B10", 15.13)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0)
        title = Text("Zero-Point Motion Survives", font=DISPLAY, font_size=40, color=INK)
        title.to_edge(UP, buff=0.65)
        rule = Line(LEFT * 5.8, RIGHT * 5.8, color=TEAL, stroke_width=3).next_to(title, DOWN, buff=0.25)

        atoms = VGroup()
        for row in range(3):
            for col in range(6):
                atom = Dot(radius=0.20, color=TEAL)
                atom.move_to(LEFT * 4.5 + RIGHT * col * 1.8 + UP * (1.45 - row * 1.45))
                atoms.add(atom)

        lattice = VGroup()
        for row in range(3):
            lattice.add(Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.2).move_to(UP * (1.45 - row * 1.45)))
        for col in range(6):
            lattice.add(Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=1.2).move_to(LEFT * 4.5 + RIGHT * col * 1.8))
        lattice.set_opacity(0.22)

        floor = Text("Cooling removes thermal motion — not the quantum floor.",
                     font=SERIF, font_size=30, color=INK).to_edge(DOWN, buff=0.75)

        self.add(bg)
        self.play(Write(title), Create(rule), run_time=1.0)
        self.play(Create(lattice), FadeIn(atoms), run_time=1.2)
        base = [a.get_center() for a in atoms]
        for phase in range(5):
            targets = []
            for i, p in enumerate(base):
                dx = 0.13 * np.sin(phase * 1.7 + i * 0.9)
                dy = 0.13 * np.cos(phase * 1.3 + i * 1.1)
                targets.append(p + RIGHT * dx + UP * dy)
            self.play(*[a.animate.move_to(p) for a, p in zip(atoms, targets)], run_time=0.75)
        self.play(Write(floor), run_time=0.8)
        self.wait(max(0.1, duration - 6.75))


# ---------------------------------------------------------------------------
# B11 — Zero-point energy is irreducible: not thermal (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_Irreducible(Scene):
    def construct(self):
        duration = DUR.get("B11", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Two scenarios
        # Left: thermal energy (CRIMSON - removable)
        box_thermal = Rectangle(width=5.5, height=4.0).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 2)
        box_thermal.move_to(LEFT * 3.5 + DOWN * 0.5)
        label_thermal_box = Rectangle(width=4.0, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        label_thermal_box.move_to(LEFT * 3.5 + UP * 1.8)
        down_arr = Arrow(LEFT * 3.5 + DOWN * 0.2, LEFT * 3.5 + DOWN * 1.5, color=CRIMSON, buff=0,
                         stroke_width=3, max_tip_length_to_length_ratio=0.25)
        removal_box = Rectangle(width=4.0, height=0.65).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 1.5)
        removal_box.move_to(LEFT * 3.5 + DOWN * 2.2)

        # Right: zero-point energy (TEAL - irreducible)
        box_zpe = Rectangle(width=5.5, height=4.0).set_fill(TEAL, 0.06).set_stroke(TEAL, 2)
        box_zpe.move_to(RIGHT * 3.5 + DOWN * 0.5)
        label_zpe_box = Rectangle(width=4.5, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_zpe_box.move_to(RIGHT * 3.5 + UP * 1.8)
        floor_line = Line(RIGHT * 1.3, RIGHT * 5.7, color=TEAL, stroke_width=3).move_to(DOWN * 1.5)
        locked_box = Rectangle(width=4.0, height=0.65).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        locked_box.move_to(RIGHT * 3.5 + DOWN * 2.2)

        divider = Line(UP * 2.5, DOWN * 3.0, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(box_thermal), GrowFromCenter(box_zpe), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(label_thermal_box), GrowFromCenter(label_zpe_box), run_time=0.4)
        self.play(GrowArrow(down_arr), run_time=0.4)
        self.play(GrowFromCenter(removal_box), run_time=0.4)
        self.play(Create(floor_line), run_time=0.4)
        self.play(GrowFromCenter(locked_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


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
        headline_box = Rectangle(width=10.0, height=1.1).set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        headline_box.move_to(UP * 0.3)
        sub_bar = Rectangle(width=4.0, height=0.6).set_fill(SLATE, 0.12).set_stroke(SLATE, 1)
        sub_bar.move_to(DOWN * 0.9)
        accent_rule = Line(LEFT * 3.5, RIGHT * 3.5, color=TEAL, stroke_width=2).move_to(DOWN * 0.35)
        teal_dot = Dot(radius=0.12, color=TEAL).move_to(LEFT * 3.8 + DOWN * 0.35)
        teal_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.35)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.6)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.0)
        headline = Text("Electron in a 0.5 nm box", font=DISPLAY, font_size=38,
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
# B13 — Worked example: L=0.5nm, E_1≈1.5eV; double L, E drops by 4 (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 18.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Formula box at top
        formula_box = Rectangle(width=9.0, height=0.75).set_fill(SLATE, 0.10).set_stroke(SLATE, 1.5)
        formula_box.move_to(UP * 2.4)

        # Box 1: L = 0.5 nm → E_1 = 1.5 eV
        box1 = Rectangle(width=4.5, height=2.3).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        box1.move_to(LEFT * 4.5 + UP * 0.5)
        d1_line1 = Text("L = 0.5 nm", font="PT Mono", font_size=18,
                        color=INK).move_to(LEFT * 4.5 + UP * 1.0)
        d1_line2 = Text("E-1 = 1.5 eV", font="PT Mono", font_size=20,
                        color=TEAL).move_to(LEFT * 4.5 + UP * 0.2)
        d1_line3 = Text("atomic size", font=DISPLAY, font_size=16,
                        color=SLATE).move_to(LEFT * 4.5 + DOWN * 0.4)

        # Box 2: L = 1.0 nm → E_1 = 0.37 eV (double width, quarter energy)
        box2 = Rectangle(width=4.5, height=2.3).set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
        box2.move_to(RIGHT * 2.5 + UP * 0.5)
        d2_line1 = Text("L = 1.0 nm", font="PT Mono", font_size=18,
                        color=INK).move_to(RIGHT * 2.5 + UP * 1.0)
        d2_line2 = Text("E-1 = 0.37 eV", font="PT Mono", font_size=20,
                        color=TEAL).move_to(RIGHT * 2.5 + UP * 0.2)
        d2_line3 = Text("double width", font=DISPLAY, font_size=16,
                        color=SLATE).move_to(RIGHT * 2.5 + DOWN * 0.4)

        # Factor arrow between boxes
        factor_arr = Arrow(LEFT * 2.2 + UP * 0.5, LEFT * 0.3 + UP * 0.5, color=TEAL, buff=0,
                           stroke_width=2, max_tip_length_to_length_ratio=0.2)
        factor_box = Rectangle(width=2.8, height=0.65).set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        factor_box.move_to(LEFT * 1.25 + UP * 0.5)

        # Scaling conclusion
        conclusion_box = Rectangle(width=12.0, height=0.9).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        conclusion_box.move_to(DOWN * 2.5)

        # Bottom accent rule
        bottom_rule = Line(LEFT * 6.0, RIGHT * 6.0, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.2)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(formula_box), run_time=0.4)
        self.play(GrowFromCenter(box1), run_time=0.5)
        self.play(FadeIn(d1_line1), FadeIn(d1_line2), FadeIn(d1_line3), run_time=0.4)
        self.play(GrowFromCenter(box2), run_time=0.5)
        self.play(FadeIn(d2_line1), FadeIn(d2_line2), FadeIn(d2_line3), run_time=0.4)
        self.play(GrowArrow(factor_arr), run_time=0.4)
        self.play(GrowFromCenter(factor_box), run_time=0.4)
        self.play(GrowFromCenter(conclusion_box), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.2))


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
        line1 = Text("Confinement forces curvature. Curvature is energy.", font=DISPLAY,
                     font_size=26, color=TEAL).move_to(UP * 1.3)
        line2 = Text("The quantum floor cannot be removed.", font=SERIF, font_size=26,
                     color=INK).move_to(UP * 0.4)
        line3 = Text("That is the zero-point energy.", font=SERIF, font_size=26,
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
