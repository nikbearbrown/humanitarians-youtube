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
        mid_box = Rectangle(width=13.5, height=1.15).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        mid_box.move_to(UP * 0.2)
        rule2 = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 1.5)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.9)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.9)
        mid_rule = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=0.8).move_to(DOWN * 0.5)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline = Text("Why an Electron Needs Two Full Turns to Come Back", font=DISPLAY,
                        font_size=28, color=INK).move_to(UP * 0.2)
        sub = Text("The spinor and the 720° rule", font=SERIF, font_size=24,
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
# B02 — Classical vector rotates 360°, returns identical (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_ClassicalRotation(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Circle track for rotation
        circle_track = Circle(radius=2.0, color=CRIMSON, stroke_width=1.5).set_opacity(0.35)
        circle_track.move_to(DOWN * 0.3)

        # Classical vector arrow
        vec_arrow = Arrow(DOWN * 0.3, DOWN * 0.3 + RIGHT * 2.0,
                          color=CRIMSON, buff=0, stroke_width=4,
                          max_tip_length_to_length_ratio=0.22)

        # Return label box
        return_box = Rectangle(width=5.0, height=0.8).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        return_box.move_to(DOWN * 2.8)

        # Side annotation panel
        annotation_panel = Rectangle(width=5.5, height=3.5).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        annotation_panel.move_to(RIGHT * 5.0 + DOWN * 0.3)

        # Factor label box
        factor_box = Rectangle(width=4.2, height=0.75).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        factor_box.move_to(RIGHT * 5.0 + UP * 0.8)
        result_box = Rectangle(width=4.2, height=0.75).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        result_box.move_to(RIGHT * 5.0 + DOWN * 0.2)

        divider_v = Line(UP * 2.5, DOWN * 3.0, color=INK, stroke_width=1.0).move_to(RIGHT * 2.5).set_opacity(0.3)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(circle_track), run_time=0.4)
        self.play(GrowArrow(vec_arrow), run_time=0.4)
        self.play(Create(divider_v), run_time=0.3)
        self.play(GrowFromCenter(annotation_panel), run_time=0.4)
        self.play(GrowFromCenter(factor_box), run_time=0.3)
        self.play(GrowFromCenter(result_box), run_time=0.3)
        self.play(GrowFromCenter(return_box), run_time=0.4)
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
        content_box = Rectangle(width=13.5, height=2.8).set_fill(SLATE, 0.05).set_stroke(SLATE, 1)
        content_box.move_to(UP * 0.5)
        inner_box = Rectangle(width=12.0, height=1.1).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        inner_box.move_to(DOWN * 0.3)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 3.5 + DOWN * 0.3)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 3.5 + DOWN * 0.3)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.0).move_to(DOWN * 2.0)
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=2).move_to(DOWN * 1.2)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.8)
        line1 = Text("How can 360° rotation change anything?", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 1.3)
        line2 = Text("Every direction looks the same after one turn.", font=SERIF,
                     font_size=24, color=TEAL).move_to(DOWN * 0.3)
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
# B04 — Classical e^{iθ} at θ=2π → +1 (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalFactor(Scene):
    def construct(self):
        duration = DUR.get("B04", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Unit circle
        unit_circ = Circle(radius=2.2, color=CRIMSON, stroke_width=2).set_opacity(0.5).move_to(LEFT * 2.5 + DOWN * 0.3)

        # Point at angle θ
        theta_angle = np.pi / 3
        pt_x = LEFT * 2.5 + DOWN * 0.3 + RIGHT * 2.2 * np.cos(theta_angle) + UP * 2.2 * np.sin(theta_angle)
        theta_arc = Arc(radius=0.8, start_angle=0, angle=theta_angle,
                        color=CRIMSON, stroke_width=2).move_to(LEFT * 2.5 + DOWN * 0.3)
        radius_line = Line(LEFT * 2.5 + DOWN * 0.3, pt_x, color=CRIMSON, stroke_width=3)

        # θ = 2π label box
        angle_box = Rectangle(width=3.5, height=0.7).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        angle_box.move_to(LEFT * 2.5 + DOWN * 2.5)

        # Right side: classical formula panel
        formula_panel = Rectangle(width=6.0, height=5.0).set_fill(SLATE, 0.06).set_stroke(SLATE, 1.5)
        formula_panel.move_to(RIGHT * 4.5 + DOWN * 0.3)

        factor_box_1 = Rectangle(width=5.0, height=0.75).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        factor_box_1.move_to(RIGHT * 4.5 + UP * 0.9)
        factor_box_2 = Rectangle(width=5.0, height=0.75).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        factor_box_2.move_to(RIGHT * 4.5 + DOWN * 0.1)
        result_box = Rectangle(width=4.5, height=0.8).set_fill(CRIMSON, 0.22).set_stroke(CRIMSON, 2.5)
        result_box.move_to(RIGHT * 4.5 + DOWN * 1.3)

        divider = Line(UP * 2.5, DOWN * 3.0, color=INK, stroke_width=1.0).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(unit_circ), run_time=0.4)
        self.play(Create(theta_arc), run_time=0.3)
        self.play(Create(radius_line), run_time=0.3)
        self.play(GrowFromCenter(angle_box), run_time=0.3)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(formula_panel), run_time=0.4)
        self.play(GrowFromCenter(factor_box_1), run_time=0.3)
        self.play(GrowFromCenter(factor_box_2), run_time=0.3)
        self.play(GrowFromCenter(result_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.2))


# ---------------------------------------------------------------------------
# B05 — Spinor uses θ/2; at θ=2π, factor = −1 (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_SpinorMinus(Scene):
    def construct(self):
        duration = DUR.get("B05", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left: classical unit circle (CRIMSON)
        circ_c = Circle(radius=1.5, color=CRIMSON, stroke_width=2).set_opacity(0.5).move_to(LEFT * 4.5 + DOWN * 0.3)
        box_c = Rectangle(width=4.5, height=4.0).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.5)
        box_c.move_to(LEFT * 4.5 + DOWN * 0.3)
        label_c = Rectangle(width=3.8, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        label_c.move_to(LEFT * 4.5 + UP * 2.0)
        # Classical arrow at 2π = angle 0 (returns to +x)
        arr_c = Arrow(LEFT * 4.5 + DOWN * 0.3, LEFT * 4.5 + DOWN * 0.3 + RIGHT * 1.5,
                      color=CRIMSON, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.22)
        result_c = Rectangle(width=3.8, height=0.65).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        result_c.move_to(LEFT * 4.5 + DOWN * 2.2)

        # Right: spinor unit circle (TEAL)
        circ_t = Circle(radius=1.5, color=TEAL, stroke_width=2).set_opacity(0.5).move_to(RIGHT * 2.5 + DOWN * 0.3)
        box_t = Rectangle(width=4.5, height=4.0).set_fill(TEAL, 0.05).set_stroke(TEAL, 1.5)
        box_t.move_to(RIGHT * 2.5 + DOWN * 0.3)
        label_t = Rectangle(width=3.8, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_t.move_to(RIGHT * 2.5 + UP * 2.0)
        # Spinor at 2π → points in -x (π from original)
        arr_t = Arrow(RIGHT * 2.5 + DOWN * 0.3, RIGHT * 2.5 + DOWN * 0.3 + LEFT * 1.5,
                      color=TEAL, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.22)
        result_t = Rectangle(width=3.8, height=0.65).set_fill(TEAL, 0.22).set_stroke(TEAL, 2.5)
        result_t.move_to(RIGHT * 2.5 + DOWN * 2.2)

        divider = Line(UP * 2.5, DOWN * 3.2, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(box_c), GrowFromCenter(box_t), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(label_c), GrowFromCenter(label_t), run_time=0.4)
        self.play(Create(circ_c), Create(circ_t), run_time=0.4)
        self.play(GrowArrow(arr_c), run_time=0.3)
        self.play(GrowFromCenter(result_c), run_time=0.3)
        self.play(GrowArrow(arr_t), run_time=0.3)
        self.play(GrowFromCenter(result_t), run_time=0.3)
        self.wait(max(0.1, duration - 4.3))


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
        formula_box = Rectangle(width=9.5, height=1.1).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.2)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 5.5 + DOWN * 1.2)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 5.5 + DOWN * 1.2)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.1)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("Rotation uses θ/2 — the spinor double cover", font=DISPLAY, font_size=32,
                        color=INK).move_to(UP * 0.2)
        formula = Text("360° → −1     ·     720° → +1", font=MONO, font_size=28,
                       color=TEAL).move_to(DOWN * 1.2)
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
# B07 — Sign flag: 0° to 720°, flip at 360°, restore at 720° (GRAPHIC)
# ---------------------------------------------------------------------------
class B07_SignFlag(Scene):
    def construct(self):
        duration = DUR.get("B07", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Timeline bar
        timeline = Line(LEFT * 6.5, RIGHT * 6.5, color=INK, stroke_width=2).move_to(UP * 0.5)

        # Tick marks: 0, 360, 720
        tick_0 = Line(UP * 0.8, UP * 0.2, color=INK, stroke_width=2).move_to(LEFT * 6.5 + UP * 0.5)
        tick_360 = Line(UP * 0.8, UP * 0.2, color=INK, stroke_width=2).move_to(ORIGIN + UP * 0.5)
        tick_720 = Line(UP * 0.8, UP * 0.2, color=INK, stroke_width=2).move_to(RIGHT * 6.5 + UP * 0.5)

        # Classical arrow band (CRIMSON) — full width returns same
        band_c = Rectangle(width=13.0, height=0.7).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        band_c.move_to(UP * 1.9)

        # Spinor: first half negative (TEAL, darker)
        band_t1 = Rectangle(width=6.5, height=0.7).set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        band_t1.move_to(LEFT * 3.25 + DOWN * 0.2)
        band_t2 = Rectangle(width=6.5, height=0.7).set_fill(TEAL, 0.22).set_stroke(TEAL, 2)
        band_t2.move_to(RIGHT * 3.25 + DOWN * 0.2)

        # Sign labels (placeholder boxes)
        sign_c = Rectangle(width=3.5, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        sign_c.move_to(UP * 1.9)
        sign_t_neg = Rectangle(width=2.5, height=0.65).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        sign_t_neg.move_to(LEFT * 3.25 + DOWN * 0.2)
        sign_t_pos = Rectangle(width=2.5, height=0.65).set_fill(TEAL, 0.25).set_stroke(TEAL, 2.5)
        sign_t_pos.move_to(RIGHT * 3.25 + DOWN * 0.2)

        # Flip arrow at 360°
        flip_arr = Arrow(ORIGIN + UP * 1.4, ORIGIN + DOWN * 0.7,
                         color=TEAL, buff=0, stroke_width=3,
                         max_tip_length_to_length_ratio=0.25)

        # Bottom conclusion
        conclusion_box = Rectangle(width=12.0, height=0.8).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        conclusion_box.move_to(DOWN * 2.2)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(timeline), run_time=0.3)
        self.play(Create(tick_0), Create(tick_360), Create(tick_720), run_time=0.3)
        self.play(GrowFromCenter(band_c), run_time=0.4)
        self.play(GrowFromCenter(sign_c), run_time=0.3)
        self.play(GrowFromCenter(band_t1), run_time=0.4)
        self.play(GrowArrow(flip_arr), run_time=0.4)
        self.play(GrowFromCenter(band_t2), run_time=0.4)
        self.play(GrowFromCenter(sign_t_neg), GrowFromCenter(sign_t_pos), run_time=0.4)
        self.play(GrowFromCenter(conclusion_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.8))


# ---------------------------------------------------------------------------
# B08 — Neutron interferometer schematic (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_Interferometer(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Input beam
        beam_in = Arrow(LEFT * 7.0 + UP * 0.3, LEFT * 4.5 + UP * 0.3,
                        color=TEAL, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.15)

        # Beam splitter box
        splitter = Rectangle(width=0.9, height=2.5).set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        splitter.move_to(LEFT * 4.0 + UP * 0.3)

        # Upper path (no rotation)
        path_upper = Line(LEFT * 3.5 + UP * 1.1, RIGHT * 1.5 + UP * 1.1, color=TEAL, stroke_width=2.5)

        # Lower path (through B field)
        path_lower = Line(LEFT * 3.5 + DOWN * 0.5, RIGHT * 1.5 + DOWN * 0.5, color=TEAL, stroke_width=2.5)

        # B field box on lower path
        bfield_box = Rectangle(width=2.5, height=1.1).set_fill(TEAL, 0.18).set_stroke(TEAL, 2.5)
        bfield_box.move_to(LEFT * 1.0 + DOWN * 0.5)

        # Recombiner box
        recombiner = Rectangle(width=0.9, height=2.5).set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        recombiner.move_to(RIGHT * 2.0 + UP * 0.3)

        # Detector + fringe pattern
        detector_box = Rectangle(width=2.5, height=3.5).set_fill(TEAL, 0.08).set_stroke(TEAL, 2)
        detector_box.move_to(RIGHT * 5.0 + UP * 0.3)

        # Fringe lines in detector (shifted)
        fringes = []
        for i in range(5):
            y = -1.4 + i * 0.7
            fringes.append(Line(RIGHT * 4.0 + UP * y, RIGHT * 6.0 + UP * y,
                                color=TEAL, stroke_width=1.5))

        result_box = Rectangle(width=6.0, height=0.8).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        result_box.move_to(DOWN * 2.8)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowArrow(beam_in), run_time=0.4)
        self.play(GrowFromCenter(splitter), run_time=0.3)
        self.play(Create(path_upper), Create(path_lower), run_time=0.4)
        self.play(GrowFromCenter(bfield_box), run_time=0.4)
        self.play(GrowFromCenter(recombiner), run_time=0.3)
        self.play(GrowFromCenter(detector_box), run_time=0.3)
        self.play(*[Create(f) for f in fringes], run_time=0.4)
        self.play(GrowFromCenter(result_box), run_time=0.4)
        self.wait(max(0.1, duration - 4.5))


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
        confirm_box = Rectangle(width=10.5, height=1.1).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        confirm_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 6.0 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 6.0 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE IMPLICATION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("The minus sign is physically real — measured in 1975", font=DISPLAY,
                        font_size=28, color=INK).move_to(UP * 0.2)
        confirm = Text("Werner · Colella · Overhauser · Eagen   (+ Rauch et al.)", font=DISPLAY,
                       font_size=22, color=TEAL).move_to(DOWN * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(GrowFromCenter(headline_bg), run_time=0.3)
        self.play(Write(headline), run_time=0.5)
        self.play(GrowFromCenter(confirm_box), run_time=0.4)
        self.play(FadeIn(teal_dot1), FadeIn(teal_dot2), run_time=0.3)
        self.play(Write(confirm), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.6))


# ---------------------------------------------------------------------------
# B10 — neutron interferometer: the minus sign becomes an observable fringe.
# ---------------------------------------------------------------------------
class B10_InterferometerMinusSign(Scene):
    def construct(self):
        duration = DUR.get("B10", 12.8)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0)
        title = Text("A Minus Sign You Can Measure", font=DISPLAY, font_size=40, color=INK).to_edge(UP, buff=0.65)
        splitter = Dot(radius=0.22, color=TEAL).move_to(LEFT * 5)
        merge = Dot(radius=0.22, color=TEAL).move_to(RIGHT * 3.6)
        upper = VMobject(color=INK, stroke_width=4).set_points_smoothly([
            LEFT * 5, LEFT * 2.6 + UP * 2, RIGHT * 1.2 + UP * 2, RIGHT * 3.6])
        lower = VMobject(color=CRIMSON, stroke_width=4).set_points_smoothly([
            LEFT * 5, LEFT * 2.6 + DOWN * 2, RIGHT * 1.2 + DOWN * 2, RIGHT * 3.6])
        spin = Circle(radius=0.65, color=CRIMSON, stroke_width=4).move_to(DOWN * 2)
        minus = Text("−1", font="PT Mono", font_size=34, color=CRIMSON).next_to(spin, RIGHT, buff=0.25)
        detector = Rectangle(width=1.0, height=5.2).set_fill(TEAL, 0.10).set_stroke(TEAL, 2).move_to(RIGHT * 5.4)
        fringes = VGroup(*[
            Line(LEFT * 0.35, RIGHT * 0.35, color=TEAL if i % 2 == 0 else INK, stroke_width=5)
            .move_to(RIGHT * 5.4 + UP * (i - 4) * 0.5) for i in range(9)
        ])
        caption = Text("Relative phase shifts the interference pattern", font=SERIF, font_size=30, color=INK).to_edge(DOWN, buff=0.55)
        self.add(bg)
        self.play(Write(title), FadeIn(splitter), FadeIn(merge), run_time=0.9)
        self.play(Create(upper), Create(lower), run_time=1.4)
        self.play(Create(spin), Rotate(spin, angle=TAU), run_time=1.4)
        self.play(FadeIn(minus), run_time=0.5)
        self.play(Create(detector), LaggedStart(*[Create(f) for f in fringes], lag_ratio=0.08), run_time=1.3)
        self.play(Write(caption), run_time=0.8)
        self.wait(max(0.1, duration - 6.3))


# ---------------------------------------------------------------------------
# B11 — Classical loop closes at 360°; spinor loop closes at 720° (GRAPHIC)
# ---------------------------------------------------------------------------
class B11_LoopComparison(Scene):
    def construct(self):
        duration = DUR.get("B11", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Left: classical (CRIMSON) — small circle
        box_c = Rectangle(width=5.5, height=5.5).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 2)
        box_c.move_to(LEFT * 3.5 + DOWN * 0.3)
        label_c = Rectangle(width=4.2, height=0.65).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        label_c.move_to(LEFT * 3.5 + UP * 2.2)
        loop_c = Circle(radius=1.3, color=CRIMSON, stroke_width=3).move_to(LEFT * 3.5 + DOWN * 0.3)
        angle_c = Rectangle(width=3.2, height=0.65).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        angle_c.move_to(LEFT * 3.5 + DOWN * 2.2)

        # Right: spinor (TEAL) — larger loop (Mobius-like concept)
        box_t = Rectangle(width=5.5, height=5.5).set_fill(TEAL, 0.05).set_stroke(TEAL, 2)
        box_t.move_to(RIGHT * 3.5 + DOWN * 0.3)
        label_t = Rectangle(width=4.2, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_t.move_to(RIGHT * 3.5 + UP * 2.2)
        # Draw a figure-8 style double loop to suggest 720° closure
        loop_t_inner = Circle(radius=0.8, color=TEAL, stroke_width=2).move_to(RIGHT * 3.5 + DOWN * 0.0)
        loop_t_outer = Circle(radius=1.5, color=TEAL, stroke_width=2.5).set_opacity(0.5).move_to(RIGHT * 3.5 + DOWN * 0.3)
        angle_t = Rectangle(width=3.2, height=0.65).set_fill(TEAL, 0.22).set_stroke(TEAL, 2.5)
        angle_t.move_to(RIGHT * 3.5 + DOWN * 2.2)

        divider = Line(UP * 2.5, DOWN * 3.5, color=INK, stroke_width=1.5).set_opacity(0.35)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(box_c), GrowFromCenter(box_t), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(label_c), GrowFromCenter(label_t), run_time=0.4)
        self.play(Create(loop_c), run_time=0.4)
        self.play(GrowFromCenter(angle_c), run_time=0.3)
        self.play(Create(loop_t_inner), Create(loop_t_outer), run_time=0.5)
        self.play(GrowFromCenter(angle_t), run_time=0.3)
        self.wait(max(0.1, duration - 4.3))


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
        headline_box = Rectangle(width=11.0, height=1.1).set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        headline_box.move_to(UP * 0.3)
        sub_bar = Rectangle(width=4.0, height=0.6).set_fill(SLATE, 0.12).set_stroke(SLATE, 1)
        sub_bar.move_to(DOWN * 0.9)
        accent_rule = Line(LEFT * 3.5, RIGHT * 3.5, color=TEAL, stroke_width=2).move_to(DOWN * 0.35)
        teal_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 3.8 + DOWN * 0.35)
        teal_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.35)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.6)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.0)
        headline = Text("Neutron beam · 1975 · Werner et al.", font=DISPLAY, font_size=34,
                        color=INK).move_to(UP * 0.3)
        sub = Text("(measured)", font=SERIF, font_size=24,
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
# B13 — I vs θ graph, period 4π (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_IvsTheta(Scene):
    def construct(self):
        duration = DUR.get("B13", 17.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Axes
        x_axis = Line(LEFT * 6.5 + DOWN * 1.5, RIGHT * 6.5 + DOWN * 1.5, color=INK, stroke_width=2)
        y_axis = Line(LEFT * 6.5 + DOWN * 2.5, LEFT * 6.5 + UP * 2.5, color=INK, stroke_width=2)

        # Tick marks at 0, 2π (=360°), 4π (=720°)
        tick_2pi = Line(LEFT * 6.5 + RIGHT * 6.5 + DOWN * 1.7, LEFT * 6.5 + RIGHT * 6.5 + DOWN * 1.3,
                        color=INK, stroke_width=2).move_to(ORIGIN + DOWN * 1.5)
        tick_4pi = Line(RIGHT * 6.5 + DOWN * 1.7, RIGHT * 6.5 + DOWN * 1.3,
                        color=INK, stroke_width=2).move_to(RIGHT * 6.5 + DOWN * 1.5)

        # Classical I(θ) = 1 (flat CRIMSON line)
        classical_line = Line(LEFT * 6.5 + UP * 0.5, RIGHT * 6.5 + UP * 0.5,
                              color=CRIMSON, stroke_width=2.5).set_opacity(0.6)

        # Spinor I(θ) = cos²(θ/4) — period 4π (TEAL cosine curve)
        x_vals = np.linspace(0, 4 * np.pi, 100)
        # Map x_vals (0 to 4π) to screen x (-6.5 to +6.5)
        curve_pts = [LEFT * 6.5 + RIGHT * (v / (4 * np.pi)) * 13.0 +
                     DOWN * 1.5 + UP * (1.8 * (np.cos(v / 2))**2) for v in x_vals]
        spinor_curve = VMobject(color=TEAL, stroke_width=3)
        spinor_curve.set_points_smoothly(curve_pts)

        # Data point circles at key angles
        dot_0 = Dot(radius=0.18, color=TEAL).move_to(LEFT * 6.5 + DOWN * 1.5 + UP * 1.8)
        dot_360 = Dot(radius=0.18, color=TEAL).move_to(ORIGIN + DOWN * 1.5)
        dot_720 = Dot(radius=0.18, color=TEAL).move_to(RIGHT * 6.5 + DOWN * 1.5 + UP * 1.8)

        # Label boxes at key points
        label_0 = Rectangle(width=2.0, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        label_0.move_to(LEFT * 6.5 + DOWN * 2.5)
        label_360 = Rectangle(width=2.0, height=0.65).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        label_360.move_to(ORIGIN + DOWN * 2.5)
        label_720 = Rectangle(width=2.0, height=0.65).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        label_720.move_to(RIGHT * 6.5 + DOWN * 2.5)

        # Conclusion box
        conclusion_box = Rectangle(width=10.0, height=0.8).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        conclusion_box.move_to(UP * 3.0)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(Create(x_axis), Create(y_axis), run_time=0.4)
        self.play(Create(tick_2pi), Create(tick_4pi), run_time=0.3)
        self.play(Create(classical_line), run_time=0.3)
        self.play(Create(spinor_curve), run_time=0.8)
        self.play(FadeIn(dot_0), FadeIn(dot_360), FadeIn(dot_720), run_time=0.3)
        self.play(GrowFromCenter(label_0), run_time=0.3)
        self.play(GrowFromCenter(label_360), run_time=0.3)
        self.play(GrowFromCenter(label_720), run_time=0.3)
        self.play(GrowFromCenter(conclusion_box), run_time=0.4)
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
        highlight_box = Rectangle(width=12.5, height=1.35).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        highlight_box.move_to(UP * 1.1)
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=1.5).move_to(DOWN * 0.0)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.0)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.0)
        content_box = Rectangle(width=12.5, height=1.7).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        content_box.move_to(DOWN * 0.6)
        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.7)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        line1 = Text("360° flips the sign. 720° restores it.", font=DISPLAY,
                     font_size=26, color=TEAL).move_to(UP * 1.3)
        line2 = Text("The minus sign is measured — not imagined.", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 0.7)
        line3 = Text("Spin-½ is not a tiny spinning ball.", font=SERIF,
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
