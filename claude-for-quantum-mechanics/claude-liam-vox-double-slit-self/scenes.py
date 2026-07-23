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
        headline = Text("Why One Electron Interferes With Itself", font=DISPLAY, font_size=32,
                        color=INK).move_to(UP * 0.2)
        sub = Text("The Tonomura experiment, 1989", font=SERIF, font_size=24,
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
# B02 — Classical bullets: two lumps, no fringes (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_ClassicalBullets(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Source (left)
        source_box = Rectangle(width=1.5, height=1.5).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        source_box.move_to(LEFT * 6.5 + DOWN * 0.3)

        # Wall with two slits
        wall_top = Rectangle(width=0.6, height=2.2).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_top.move_to(LEFT * 1.5 + UP * 1.8)
        wall_mid = Rectangle(width=0.6, height=1.0).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_mid.move_to(LEFT * 1.5 + DOWN * 0.3)
        wall_bot = Rectangle(width=0.6, height=2.2).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_bot.move_to(LEFT * 1.5 + DOWN * 2.4)

        # Two trajectory arrows (CRIMSON)
        traj_upper = Arrow(LEFT * 5.8 + UP * 0.2, LEFT * 1.8 + UP * 0.8,
                           color=CRIMSON, buff=0, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.15)
        traj_lower = Arrow(LEFT * 5.8 + DOWN * 0.8, LEFT * 1.8 + DOWN * 1.3,
                           color=CRIMSON, buff=0, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.15)

        # Detector (right) — two lumps
        detector_panel = Rectangle(width=2.0, height=7.0).set_fill(SLATE, 0.06).set_stroke(SLATE, 1.5)
        detector_panel.move_to(RIGHT * 5.5 + DOWN * 0.3)
        lump_upper = Rectangle(width=1.5, height=1.8).set_fill(CRIMSON, 0.20).set_stroke(CRIMSON, 2)
        lump_upper.move_to(RIGHT * 5.5 + UP * 1.0)
        lump_lower = Rectangle(width=1.5, height=1.8).set_fill(CRIMSON, 0.20).set_stroke(CRIMSON, 2)
        lump_lower.move_to(RIGHT * 5.5 + DOWN * 1.6)

        # Label boxes
        result_label = Rectangle(width=4.5, height=0.7).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        result_label.move_to(RIGHT * 5.5 + DOWN * 3.5)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(source_box), run_time=0.3)
        self.play(GrowFromCenter(wall_top), GrowFromCenter(wall_mid), GrowFromCenter(wall_bot), run_time=0.5)
        self.play(GrowArrow(traj_upper), GrowArrow(traj_lower), run_time=0.4)
        self.play(GrowFromCenter(detector_panel), run_time=0.3)
        self.play(GrowFromCenter(lump_upper), GrowFromCenter(lump_lower), run_time=0.4)
        self.play(GrowFromCenter(result_label), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


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
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=2).move_to(DOWN * 1.1)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.8)
        line1 = Text("If each electron is a single particle,", font=SERIF,
                     font_size=24, color=INK).move_to(UP * 1.3)
        line2 = Text("where does the interference pattern come from?", font=SERIF,
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
# B04 — Classical definite path fails (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalPath(Scene):
    def construct(self):
        duration = DUR.get("B04", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Wall barrier
        wall_top = Rectangle(width=0.7, height=2.8).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_top.move_to(ORIGIN + UP * 2.0)
        wall_bot = Rectangle(width=0.7, height=2.8).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_bot.move_to(ORIGIN + DOWN * 2.0)

        # Definite trajectory A (CRIMSON) — through slit A only
        path_A = Arrow(LEFT * 5.5 + UP * 0.5, LEFT * 0.5 + UP * 0.5,
                       color=CRIMSON, buff=0, stroke_width=3,
                       max_tip_length_to_length_ratio=0.15)
        path_A_out = Arrow(RIGHT * 0.5 + UP * 0.5, RIGHT * 5.5 + UP * 0.5,
                           color=CRIMSON, buff=0, stroke_width=3,
                           max_tip_length_to_length_ratio=0.15)

        # Definite trajectory B (shown as dashed) — through slit B
        path_B = Arrow(LEFT * 5.5 + DOWN * 0.5, LEFT * 0.5 + DOWN * 0.5,
                       color=CRIMSON, buff=0, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.15)
        path_B_out = Arrow(RIGHT * 0.5 + DOWN * 0.5, RIGHT * 5.5 + DOWN * 0.5,
                           color=CRIMSON, buff=0, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.15)

        # Result: two separate spots on detector (CRIMSON)
        spot_A = Rectangle(width=2.2, height=0.9).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        spot_A.move_to(RIGHT * 6.5 + UP * 0.5)
        spot_B = Rectangle(width=2.2, height=0.9).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        spot_B.move_to(RIGHT * 6.5 + DOWN * 0.5)

        # No-fringes label
        no_fringes = Rectangle(width=4.0, height=0.7).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        no_fringes.move_to(RIGHT * 6.5 + DOWN * 2.5)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(wall_top), GrowFromCenter(wall_bot), run_time=0.5)
        self.play(GrowArrow(path_A), run_time=0.4)
        self.play(GrowArrow(path_A_out), run_time=0.4)
        self.play(GrowArrow(path_B), run_time=0.4)
        self.play(GrowArrow(path_B_out), run_time=0.4)
        self.play(GrowFromCenter(spot_A), GrowFromCenter(spot_B), run_time=0.4)
        self.play(GrowFromCenter(no_fringes), run_time=0.4)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B05 — de Broglie wave amplitude through both slits (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_WaveAmplitude(Scene):
    def construct(self):
        duration = DUR.get("B05", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Source wavefront panel (left side)
        source_panel = Rectangle(width=3.0, height=5.5).set_fill(TEAL, 0.05).set_stroke(TEAL, 1.5)
        source_panel.move_to(LEFT * 5.0 + DOWN * 0.3)

        # Wall
        wall_top = Rectangle(width=0.5, height=2.5).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_top.move_to(LEFT * 1.5 + UP * 1.8)
        wall_bot = Rectangle(width=0.5, height=2.5).set_fill(INK, 0.25).set_stroke(INK, 2)
        wall_bot.move_to(LEFT * 1.5 + DOWN * 1.8)

        # Wave arcs from each slit (TEAL)
        wave_arc_A = Arc(radius=2.0, start_angle=-np.pi/2, angle=np.pi,
                         color=TEAL, stroke_width=2).move_to(LEFT * 1.5 + UP * 0.5)
        wave_arc_B = Arc(radius=2.0, start_angle=-np.pi/2, angle=np.pi,
                         color=TEAL, stroke_width=2).move_to(LEFT * 1.5 + DOWN * 0.5)

        # Interference zone (TEAL fill)
        interference_zone = Rectangle(width=4.0, height=5.5).set_fill(TEAL, 0.06).set_stroke(TEAL, 1)
        interference_zone.move_to(RIGHT * 3.0 + DOWN * 0.3)

        # de Broglie label box
        debroglie_box = Rectangle(width=5.0, height=0.7).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        debroglie_box.move_to(LEFT * 5.0 + DOWN * 2.5)

        # Result: fringe pattern indicated
        fringe_result = Rectangle(width=3.5, height=0.7).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        fringe_result.move_to(RIGHT * 4.5 + DOWN * 3.0)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(source_panel), run_time=0.4)
        self.play(GrowFromCenter(wall_top), GrowFromCenter(wall_bot), run_time=0.4)
        self.play(Create(wave_arc_A), run_time=0.4)
        self.play(Create(wave_arc_B), run_time=0.4)
        self.play(GrowFromCenter(interference_zone), run_time=0.4)
        self.play(GrowFromCenter(debroglie_box), run_time=0.3)
        self.play(GrowFromCenter(fringe_result), run_time=0.4)
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
        headline_bg = Rectangle(width=12.5, height=1.35).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        headline_bg.move_to(UP * 0.2)
        formula_box = Rectangle(width=5.5, height=0.85).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(DOWN * 1.2)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 3.5 + DOWN * 1.2)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 3.5 + DOWN * 1.2)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("The amplitude passes through both slits.\nSquare it to get probability.", font=DISPLAY,
                        font_size=30, color=INK).move_to(UP * 0.2)
        formula = Text("λ = h / p", font=MONO, font_size=30,
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
# B07 — Interference fringes; single dot lands in bright region (GRAPHIC)
# ---------------------------------------------------------------------------
class B07_FringePattern(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Two slits (left)
        wall_top = Rectangle(width=0.5, height=2.5).set_fill(INK, 0.22).set_stroke(INK, 2)
        wall_top.move_to(LEFT * 4.5 + UP * 1.7)
        wall_bot = Rectangle(width=0.5, height=2.5).set_fill(INK, 0.22).set_stroke(INK, 2)
        wall_bot.move_to(LEFT * 4.5 + DOWN * 1.7)

        # Wave spreading from slits
        spread_A = Arc(radius=3.5, start_angle=-np.pi/3, angle=2*np.pi/3,
                       color=TEAL, stroke_width=2).set_opacity(0.5).move_to(LEFT * 4.5 + UP * 0.5)
        spread_B = Arc(radius=3.5, start_angle=-np.pi/3, angle=2*np.pi/3,
                       color=TEAL, stroke_width=2).set_opacity(0.5).move_to(LEFT * 4.5 + DOWN * 0.5)

        # Detector screen (right)
        screen = Rectangle(width=0.5, height=7.0).set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        screen.move_to(RIGHT * 5.5 + DOWN * 0.3)

        # Bright fringes on detector
        fringe_y = [2.2, 1.1, 0.0, -1.1, -2.2]
        fringe_widths = [0.6, 1.0, 1.2, 1.0, 0.6]
        fringes = []
        for y, w in zip(fringe_y, fringe_widths):
            f = Rectangle(width=0.4, height=w).set_fill(TEAL, 0.25).set_stroke(TEAL, 1.5)
            f.move_to(RIGHT * 5.5 + UP * y + DOWN * 0.3)
            fringes.append(f)

        # Single dot landing
        single_dot = Dot(radius=0.18, color=TEAL).move_to(RIGHT * 5.5 + DOWN * 0.3)

        # Labels
        bright_label = Rectangle(width=3.5, height=0.65).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        bright_label.move_to(RIGHT * 5.5 + DOWN * 3.5)
        dark_label = Rectangle(width=3.5, height=0.65).set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        dark_label.move_to(RIGHT * 5.5 + DOWN * 4.4)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(wall_top), GrowFromCenter(wall_bot), run_time=0.4)
        self.play(Create(spread_A), Create(spread_B), run_time=0.5)
        self.play(GrowFromCenter(screen), run_time=0.3)
        self.play(*[GrowFromCenter(f) for f in fringes], run_time=0.5)
        self.play(FadeIn(single_dot), run_time=0.3)
        self.play(GrowFromCenter(bright_label), run_time=0.3)
        self.play(GrowFromCenter(dark_label), run_time=0.3)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B08 — Dot accumulation: 100, 1000, 70000 electrons (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_DotAccumulation(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Three detector panels
        panel1 = Rectangle(width=3.5, height=5.5).set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        panel1.move_to(LEFT * 5.0 + DOWN * 0.3)
        label1 = Rectangle(width=3.0, height=0.65).set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        label1.move_to(LEFT * 5.0 + DOWN * 3.4)

        panel2 = Rectangle(width=3.5, height=5.5).set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        panel2.move_to(ORIGIN + DOWN * 0.3)
        label2 = Rectangle(width=3.0, height=0.65).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        label2.move_to(ORIGIN + DOWN * 3.4)

        panel3 = Rectangle(width=3.5, height=5.5).set_fill(TEAL, 0.06).set_stroke(TEAL, 2)
        panel3.move_to(RIGHT * 5.0 + DOWN * 0.3)
        label3 = Rectangle(width=3.0, height=0.65).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        label3.move_to(RIGHT * 5.0 + DOWN * 3.4)

        # Sparse dots in panel1 (random, few)
        rng = [(-1.2, 0.8), (0.3, -1.0), (-0.5, 0.2), (0.7, 1.2), (-0.9, -0.5)]
        dots1 = [Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.0 + RIGHT * x + UP * y + DOWN * 0.3)
                 for x, y in rng]

        # Faint fringes in panel2 (some structure)
        fringe2_a = Rectangle(width=2.5, height=0.5).set_fill(TEAL, 0.12).set_stroke(TEAL, 0.8)
        fringe2_a.move_to(ORIGIN + UP * 1.0 + DOWN * 0.3)
        fringe2_b = Rectangle(width=2.5, height=0.5).set_fill(TEAL, 0.08).set_stroke(TEAL, 0.5)
        fringe2_b.move_to(ORIGIN + DOWN * 0.3)
        fringe2_c = Rectangle(width=2.5, height=0.5).set_fill(TEAL, 0.12).set_stroke(TEAL, 0.8)
        fringe2_c.move_to(ORIGIN + DOWN * 1.6)

        # Clear fringes in panel3
        fringe3_y = [1.8, 0.9, 0.0, -0.9, -1.8]
        fringes3 = []
        for y in fringe3_y:
            f = Rectangle(width=2.8, height=0.65).set_fill(TEAL, 0.22).set_stroke(TEAL, 1.5)
            f.move_to(RIGHT * 5.0 + UP * y + DOWN * 0.3)
            fringes3.append(f)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(panel1), GrowFromCenter(panel2), GrowFromCenter(panel3), run_time=0.5)
        self.play(*[FadeIn(d) for d in dots1], run_time=0.3)
        self.play(GrowFromCenter(label1), run_time=0.3)
        self.play(GrowFromCenter(fringe2_a), GrowFromCenter(fringe2_b), GrowFromCenter(fringe2_c), run_time=0.4)
        self.play(GrowFromCenter(label2), run_time=0.3)
        self.play(*[GrowFromCenter(f) for f in fringes3], run_time=0.5)
        self.play(GrowFromCenter(label3), run_time=0.3)
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
        imply_box = Rectangle(width=8.0, height=1.1).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        imply_box.move_to(DOWN * 1.1)
        teal_dot1 = Dot(radius=0.14, color=TEAL).move_to(LEFT * 5.0 + DOWN * 1.1)
        teal_dot2 = Dot(radius=0.14, color=TEAL).move_to(RIGHT * 5.0 + DOWN * 1.1)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        eyebrow = Text("THE IMPLICATION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.9)
        headline = Text("One electron — both slits at once", font=DISPLAY,
                        font_size=36, color=INK).move_to(UP * 0.2)
        imply = Text("Tonomura et al. · Hitachi · 1989", font=DISPLAY,
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
# B10 — one-electron-at-a-time buildup, deterministically reconstructed.
# ---------------------------------------------------------------------------
class B10_TonomuraBuildup(Scene):
    def construct(self):
        duration = DUR.get("B10", 14.8)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0)
        title = Text("One Electron at a Time", font=DISPLAY, font_size=42, color=INK).to_edge(UP, buff=0.65)
        screen = Rectangle(width=11.0, height=5.4).set_fill(SLATE, 0.04).set_stroke(INK, 2).move_to(DOWN * 0.15)
        count = Text("0 detections", font="PT Mono", font_size=25, color=TEAL).to_corner(UR, buff=0.8)
        rng = np.random.default_rng(1989)
        points = []
        while len(points) < 320:
            x = rng.uniform(-5.1, 5.1)
            y = rng.uniform(-2.45, 2.45)
            probability = np.exp(-0.20 * y * y) * (0.18 + 0.82 * np.cos(3.2 * y) ** 2)
            if rng.random() < probability:
                points.append(Dot(point=RIGHT * x + UP * y + DOWN * 0.15,
                                  radius=0.035, color=TEAL, fill_opacity=0.82))
        self.add(bg)
        self.play(Write(title), Create(screen), FadeIn(count), run_time=1.0)
        for end in [12, 40, 100, 200, 320]:
            start = 0 if end == 12 else [12, 40, 100, 200][[40, 100, 200, 320].index(end)]
            batch = VGroup(*points[start:end])
            new_count = Text(f"{end} detections", font="PT Mono", font_size=25, color=TEAL).move_to(count)
            self.play(LaggedStart(*[FadeIn(dot) for dot in batch], lag_ratio=0.01),
                      Transform(count, new_count), run_time=1.15)
        verdict = Text("Random dots. Deterministic pattern.", font=SERIF, font_size=31, color=INK).move_to(DOWN * 3.05)
        self.play(Write(verdict), run_time=0.8)
        self.wait(max(0.1, duration - 7.55))


# ---------------------------------------------------------------------------
# B11 — Wave function through both slits; which-slit question crossed out (GRAPHIC)
# ---------------------------------------------------------------------------
class B11_WhichSlit(Scene):
    def construct(self):
        duration = DUR.get("B11", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Double-slit schematic (center)
        wall_t = Rectangle(width=0.5, height=2.0).set_fill(INK, 0.22).set_stroke(INK, 2)
        wall_t.move_to(ORIGIN + UP * 1.5)
        wall_b = Rectangle(width=0.5, height=2.0).set_fill(INK, 0.22).set_stroke(INK, 2)
        wall_b.move_to(ORIGIN + DOWN * 1.5)

        # Two wave paths (TEAL) through both slits
        path_both_A = Arrow(LEFT * 5.5 + DOWN * 0.3, LEFT * 0.4 + UP * 0.5,
                            color=TEAL, buff=0, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.15)
        path_both_B = Arrow(LEFT * 5.5 + DOWN * 0.3, LEFT * 0.4 + DOWN * 0.5,
                            color=TEAL, buff=0, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.15)

        # Fringe pattern on right (TEAL)
        fringes = []
        for y in [1.5, 0.5, -0.5, -1.5]:
            f = Rectangle(width=2.0, height=0.6).set_fill(TEAL, 0.20).set_stroke(TEAL, 1.5)
            f.move_to(RIGHT * 5.0 + UP * y)
            fringes.append(f)

        # "Which slit?" label crossed out (CRIMSON)
        which_box = Rectangle(width=4.5, height=0.8).set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2)
        which_box.move_to(DOWN * 3.0)
        cross_line = Line(DOWN * 3.0 + LEFT * 2.3, DOWN * 3.0 + RIGHT * 2.3,
                          color=CRIMSON, stroke_width=4)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(wall_t), GrowFromCenter(wall_b), run_time=0.4)
        self.play(GrowArrow(path_both_A), run_time=0.3)
        self.play(GrowArrow(path_both_B), run_time=0.3)
        self.play(*[GrowFromCenter(f) for f in fringes], run_time=0.5)
        self.play(GrowFromCenter(which_box), run_time=0.3)
        self.play(Create(cross_line), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


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
        sub_bar = Rectangle(width=6.5, height=0.6).set_fill(SLATE, 0.12).set_stroke(SLATE, 1)
        sub_bar.move_to(DOWN * 0.9)
        accent_rule = Line(LEFT * 3.5, RIGHT * 3.5, color=TEAL, stroke_width=2).move_to(DOWN * 0.35)
        teal_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 3.8 + DOWN * 0.35)
        teal_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.35)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.6)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22,
                       color=SLATE).move_to(UP * 2.0)
        headline = Text("50 keV electron · λ = 0.0055 nm", font=MONO, font_size=32,
                        color=INK).move_to(UP * 0.3)
        sub = Text("(Tonomura beam energy, illustrative)", font=SERIF, font_size=20,
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
# B13 — Worked example: λ calculation for 50 keV electron (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 17.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title_bar = Rectangle(width=14, height=0.45).set_fill(SLATE, 0.12).set_stroke(width=0)
        title_bar.move_to(UP * 3.3)

        # Top formula banner
        formula_banner = Rectangle(width=11.0, height=0.8).set_fill(SLATE, 0.10).set_stroke(SLATE, 1.5)
        formula_banner.move_to(UP * 2.4)

        # Step 1 box: K = 50 keV
        step1_box = Rectangle(width=4.0, height=1.8).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.5)
        step1_box.move_to(LEFT * 5.5 + UP * 0.8)

        # Step 2 box: p = √(2mK)
        step2_box = Rectangle(width=4.0, height=1.8).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        step2_box.move_to(LEFT * 0.5 + UP * 0.8)

        # Step 3 box: λ = h/p ≈ 0.0055 nm
        step3_box = Rectangle(width=4.0, height=1.8).set_fill(TEAL, 0.18).set_stroke(TEAL, 2.5)
        step3_box.move_to(RIGHT * 5.0 + UP * 0.8)

        # Arrows between steps
        arr12 = Arrow(LEFT * 3.5 + UP * 0.8, LEFT * 2.5 + UP * 0.8,
                      color=TEAL, buff=0, stroke_width=2,
                      max_tip_length_to_length_ratio=0.25)
        arr23 = Arrow(RIGHT * 1.5 + UP * 0.8, RIGHT * 3.0 + UP * 0.8,
                      color=TEAL, buff=0, stroke_width=2,
                      max_tip_length_to_length_ratio=0.25)

        # Fringe calculation box
        fringe_box = Rectangle(width=12.0, height=1.0).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        fringe_box.move_to(DOWN * 1.5)

        # Bottom result box
        result_box = Rectangle(width=10.0, height=0.8).set_fill(TEAL, 0.18).set_stroke(TEAL, 2)
        result_box.move_to(DOWN * 2.8)

        # Bottom rule
        bottom_rule = Line(LEFT * 6.0, RIGHT * 6.0, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.5)

        self.play(FadeIn(title_bar), run_time=0.4)
        self.play(GrowFromCenter(formula_banner), run_time=0.4)
        self.play(GrowFromCenter(step1_box), run_time=0.4)
        self.play(GrowArrow(arr12), run_time=0.3)
        self.play(GrowFromCenter(step2_box), run_time=0.4)
        self.play(GrowArrow(arr23), run_time=0.3)
        self.play(GrowFromCenter(step3_box), run_time=0.4)
        self.play(GrowFromCenter(fringe_box), run_time=0.4)
        self.play(GrowFromCenter(result_box), run_time=0.4)
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
        highlight_box = Rectangle(width=12.5, height=1.25).set_fill(TEAL, 0.10).set_stroke(TEAL, 2)
        highlight_box.move_to(UP * 1.1)
        rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=TEAL, stroke_width=1.5).move_to(DOWN * 0.0)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 0.0)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 0.0)
        content_box = Rectangle(width=12.5, height=1.7).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        content_box.move_to(DOWN * 0.6)
        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.0).move_to(DOWN * 1.7)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        line1 = Text("The amplitude passes through both slits.", font=DISPLAY,
                     font_size=26, color=TEAL).move_to(UP * 1.3)
        line2 = Text("The pattern is the proof.", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 0.7)
        line3 = Text("One electron, one shot — and still, fringes.", font=SERIF,
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
