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


class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Why a Particle Bounces Off a Cliff\nIt Could Easily Clear",
                     font=DISPLAY, color=INK, font_size=32, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        sub = Text("the quantum reflection paradox", font=SERIF, color=INK, font_size=20, slant=ITALIC).move_to([0, -1.0, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_ClassicalBall(Scene):
    """Classical ball rolling off a downhill step — always continues, no reflection."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Platform profile
        left_ground = Line([-6.0, 0.5, 0], [-1.5, 0.5, 0], color=INK, stroke_width=4)
        step_face = Line([-1.5, 0.5, 0], [-1.5, -1.0, 0], color=INK, stroke_width=4)
        right_ground = Line([-1.5, -1.0, 0], [6.0, -1.0, 0], color=INK, stroke_width=4)

        # Ball on left
        ball = Circle(radius=0.3, color=CRIMSON, fill_opacity=0.9, stroke_width=0).move_to([-5.0, 0.9, 0])
        ball_lbl = SerifLabel("classical ball", accent=CRIMSON, size=20).move_to([-5.0, 1.6, 0])

        # Motion arrow
        motion_arrow = Arrow(start=[-4.5, 0.9, 0], end=[-3.0, 0.9, 0],
                             color=CRIMSON, stroke_width=3, buff=0.1)

        # Ball reaches step and goes down/right
        no_reflect_lbl = LabelChip("zero reflection", accent=TEAL, size=22).move_to([2.5, 0.5, 0])
        after_arrow = Arrow(start=[0.0, -0.6, 0], end=[4.5, -0.6, 0],
                            color=TEAL, stroke_width=3, buff=0.1)
        faster_lbl = SerifLabel("speeds up (gains kinetic energy)", accent=TEAL, size=18).move_to([2.5, -2.0, 0])

        self.play(
            Create(left_ground), Create(step_face), Create(right_ground),
            run_time=0.4
        )
        self.play(FadeIn(ball), FadeIn(ball_lbl), run_time=0.3)
        self.play(GrowArrow(motion_arrow), run_time=0.4)
        self.play(
            ball.animate.move_to([2.5, -0.6, 0]),
            run_time=dur * 0.35
        )
        self.play(GrowArrow(after_arrow), FadeIn(faster_lbl), run_time=0.4)
        self.play(GrowFromCenter(no_reflect_lbl), run_time=0.4)
        self.wait(dur * 0.1)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Enough energy to clear the step.\nClassical: always passes.\nQuantum: partly bounces.\nWhat is doing the reflecting?",
                     font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_WavelengthChange(Scene):
    """Wave on left (longer wavelength) vs wave on right (shorter wavelength) at step."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        x_left = np.linspace(-6.0, -0.5, 200)
        x_right = np.linspace(-0.5, 6.0, 200)
        k_left = 1.5   # smaller k = longer lambda
        k_right = 2.5  # larger k = shorter lambda

        left_pts = [np.array([x, 1.5 * np.sin(k_left * x * 2), 0]) for x in x_left]
        right_pts = [np.array([x, 1.5 * np.sin(k_right * x * 2), 0]) for x in x_right]

        left_wave = VMobject(color=CRIMSON, stroke_width=3)
        left_wave.set_points_smoothly(left_pts)
        right_wave = VMobject(color=TEAL, stroke_width=3)
        right_wave.set_points_smoothly(right_pts)

        # Step line
        step = Line([-0.5, -2.5, 0], [-0.5, 2.5, 0], color=INK, stroke_width=3, stroke_opacity=0.7)

        # Labels
        lbl_l = SerifLabel("long lambda\nlow k (slow)", accent=CRIMSON, size=20).move_to([-4.0, -2.5, 0])
        lbl_r = SerifLabel("short lambda\nhigh k (fast)", accent=TEAL, size=20).move_to([3.5, -2.5, 0])
        step_lbl = LabelChip("step boundary", accent=INK, size=18).move_to([-0.5, 3.0, 0])

        self.play(Create(step), FadeIn(step_lbl), run_time=0.3)
        self.play(Create(left_wave), FadeIn(lbl_l), run_time=0.6)
        self.play(Create(right_wave), FadeIn(lbl_r), run_time=0.6)
        self.wait(dur - 1.7)


class B05_BoundarySplit(Scene):
    """Wave splits at step: transmitted (TEAL) and reflected (CRIMSON)."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        x_inc = np.linspace(-6.0, 0, 150)
        x_trans = np.linspace(0, 5.5, 150)
        x_refl = np.linspace(-6.0, 0, 150)

        # Incoming
        inc_pts = [np.array([x, 1.5 * np.sin(2 * x), 0]) for x in x_inc]
        inc_wave = VMobject(color=TEAL, stroke_width=3)
        inc_wave.set_points_smoothly(inc_pts)
        inc_lbl = SerifLabel("incoming", accent=TEAL, size=18).move_to([-3.5, 2.5, 0])

        # Boundary
        boundary = Line([0, -3.0, 0], [0, 3.0, 0], color=INK, stroke_width=2.5)

        # Transmitted (smaller amplitude, shorter wavelength on right)
        trans_pts = [np.array([x, 1.1 * np.sin(3 * x), 0]) for x in x_trans]
        trans_wave = VMobject(color=TEAL, stroke_width=3)
        trans_wave.set_points_smoothly(trans_pts)
        trans_lbl = LabelChip("transmitted", accent=TEAL, size=18).move_to([3.5, 2.5, 0])

        # Reflected (smaller amplitude, same wavelength on left, going back)
        refl_pts = [np.array([x, 0.5 * np.sin(-2 * x), 0]) for x in x_refl]
        refl_wave = VMobject(color=CRIMSON, stroke_width=2)
        refl_wave.set_points_smoothly(refl_pts)
        refl_lbl = LabelChip("reflected", accent=CRIMSON, size=18).move_to([-3.5, -2.5, 0])

        match_lbl = SerifLabel("wave function must match at boundary", accent=INK, size=18).move_to([0, -3.5, 0])

        self.play(Create(boundary), run_time=0.2)
        self.play(Create(inc_wave), FadeIn(inc_lbl), run_time=0.5)
        self.play(Create(trans_wave), FadeIn(trans_lbl), run_time=0.5)
        self.play(Create(refl_wave), FadeIn(refl_lbl), run_time=0.5)
        self.play(FadeIn(match_lbl), run_time=0.4)
        self.wait(dur - 2.3)


class B06_ImpedanceMismatch(Scene):
    """Two-panel: light at glass surface / quantum at a potential step."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.5)

        # Left: light at glass
        left_title = SerifLabel("light at glass", accent=INK, size=20).move_to([-3.5, 3.0, 0])
        air_rect = Rectangle(width=3.0, height=6.0, fill_color=WHITE, fill_opacity=0.3,
                             stroke_width=0).move_to([-5.0, 0, 0])
        glass_rect = Rectangle(width=2.5, height=6.0, fill_color=TEAL, fill_opacity=0.15,
                               stroke_width=0).move_to([-1.25, 0, 0])
        glass_lbl = SerifLabel("glass", accent=TEAL, size=18).move_to([-1.5, -2.0, 0])
        light_in = Arrow(start=[-6.0, 0.5, 0], end=[-3.2, 0.5, 0], color=TEAL, stroke_width=2.5, buff=0)
        light_trans = Arrow(start=[-2.8, 0.5, 0], end=[-0.5, 0.5, 0], color=TEAL, stroke_width=2.5, buff=0)
        light_refl = Arrow(start=[-3.2, -0.5, 0], end=[-5.5, -0.5, 0], color=CRIMSON, stroke_width=2, buff=0)
        reflect_pct = SerifLabel("~4% reflects", accent=CRIMSON, size=18).move_to([-4.5, -1.2, 0])

        # Right: quantum step
        right_title = SerifLabel("quantum step", accent=TEAL, size=20).move_to([3.5, 3.0, 0])
        step_line = Line([2.0, -2.0, 0], [2.0, 2.0, 0], color=INK, stroke_width=3)
        q_in = Arrow(start=[0.5, 0.5, 0], end=[1.6, 0.5, 0], color=TEAL, stroke_width=2.5, buff=0)
        q_trans = Arrow(start=[2.4, 0.5, 0], end=[5.5, 0.5, 0], color=TEAL, stroke_width=2.5, buff=0)
        q_refl = Arrow(start=[1.6, -0.5, 0], end=[0.3, -0.5, 0], color=CRIMSON, stroke_width=2, buff=0)
        q_reflect_pct = SerifLabel("small R", accent=CRIMSON, size=18).move_to([1.0, -1.2, 0])

        analogy_lbl = LabelChip("same physics: impedance mismatch", accent=INK, size=18).move_to([0, -3.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(
            FadeIn(left_title), FadeIn(glass_rect),
            GrowArrow(light_in), GrowArrow(light_trans), GrowArrow(light_refl),
            FadeIn(glass_lbl), FadeIn(reflect_pct),
            run_time=0.8
        )
        self.play(
            FadeIn(right_title), Create(step_line),
            GrowArrow(q_in), GrowArrow(q_trans), GrowArrow(q_refl),
            FadeIn(q_reflect_pct),
            run_time=0.8
        )
        self.play(GrowFromCenter(analogy_lbl), run_time=0.4)
        self.wait(dur - 2.4)


class B07_SharpVsGradual(Scene):
    """Sharp step: big reflected wave. Gradual slope: tiny reflected wave."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: sharp step
        sharp_title = SerifLabel("sharp step", accent=CRIMSON, size=20).move_to([-3.5, 3.2, 0])
        step_sharp = VGroup(
            Line([-5.0, 1.0, 0], [-1.5, 1.0, 0], color=INK, stroke_width=3),
            Line([-1.5, 1.0, 0], [-1.5, -1.0, 0], color=INK, stroke_width=3),
            Line([-1.5, -1.0, 0], [-0.2, -1.0, 0], color=INK, stroke_width=3)
        )
        refl_big = Arrow(start=[-2.0, 0.5, 0], end=[-4.5, 0.5, 0],
                         color=CRIMSON, stroke_width=4, buff=0)
        big_lbl = LabelChip("large R", accent=CRIMSON, size=20).move_to([-3.2, -0.3, 0])

        # Right: gradual slope
        grad_title = SerifLabel("gradual slope", accent=TEAL, size=20).move_to([3.5, 3.2, 0])
        x_slope = np.linspace(0.2, 5.5, 100)
        slope_pts = [np.array([x, 1.0 - 2.0 / (1 + np.exp(-(x - 3.0))), 0]) for x in x_slope]
        slope_curve = VMobject(color=INK, stroke_width=3)
        slope_curve.set_points_smoothly(slope_pts)
        refl_small = Arrow(start=[1.5, 0.5, 0], end=[0.3, 0.5, 0],
                           color=CRIMSON, stroke_width=1.5, buff=0)
        small_lbl = LabelChip("tiny R", accent=TEAL, size=20).move_to([3.2, -0.5, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(sharp_title), Create(step_sharp), run_time=0.5)
        self.play(GrowArrow(refl_big), GrowFromCenter(big_lbl), run_time=0.4)
        self.play(FadeIn(grad_title), Create(slope_curve), run_time=0.5)
        self.play(GrowArrow(refl_small), GrowFromCenter(small_lbl), run_time=0.4)
        self.wait(dur - 2.2)


class B08_ReflectionFormula(Scene):
    """R = ((k1-k2)/(k1+k2))^2 with wave-number diagram."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        formula = Text("R = ((k1 - k2) / (k1 + k2))^2",
                       font=MONO, color=TEAL, font_size=34).move_to([0, 1.5, 0])

        k1_lbl = SerifLabel("k1 = left side wave number", accent=CRIMSON, size=22).move_to([-2.5, 0.0, 0])
        k2_lbl = SerifLabel("k2 = right side wave number", accent=TEAL, size=22).move_to([2.5, 0.0, 0])

        note = SerifLabel("R = 0 when k1 = k2 (no mismatch)\nR grows as k1 and k2 diverge",
                          accent=INK, size=20).move_to([0, -1.5, 0])

        sym_note = LabelChip("same formula for step up or down", accent=TEAL, size=20).move_to([0, -2.8, 0])

        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(k1_lbl), FadeIn(k2_lbl), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.play(GrowFromCenter(sym_note), run_time=0.4)
        self.wait(dur - 2.3)


class B09_Example(Scene):
    """Illustrative: 4 eV electron, 3 eV step down, R ~ 2%."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        e_in = Text("E = 4 eV", font=MONO, color=TEAL, font_size=28).move_to([-3.0, 2.5, 0])
        v_step = Text("step down: 3 eV", font=MONO, color=INK, font_size=24).move_to([2.5, 2.5, 0])
        arrow1 = Arrow(start=[0, 2.0, 0], end=[0, 1.0, 0], color=INK, stroke_width=2.5, buff=0.1)
        e_far = Text("E_far = 7 eV", font=MONO, color=TEAL, font_size=28).move_to([0, 0.4, 0])

        arrow2 = Arrow(start=[0, -0.1, 0], end=[0, -1.1, 0], color=INK, stroke_width=2.5, buff=0.1)
        k_ratio = Text("k1/k2 = sqrt(4/7) ~ 0.76", font=MONO, color=INK, font_size=22).move_to([0, -1.6, 0])
        arrow3 = Arrow(start=[0, -2.1, 0], end=[0, -2.9, 0], color=INK, stroke_width=2, buff=0.1)
        result = Text("R ~ 2%", font=MONO, color=CRIMSON, font_size=32).move_to([0, -3.4, 0])

        self.play(FadeIn(ill_lbl), FadeIn(e_in), FadeIn(v_step), run_time=0.5)
        self.play(GrowArrow(arrow1), run_time=0.3)
        self.play(FadeIn(e_far), run_time=0.3)
        self.play(GrowArrow(arrow2), run_time=0.2)
        self.play(FadeIn(k_ratio), run_time=0.3)
        self.play(GrowArrow(arrow3), run_time=0.2)
        self.play(FadeIn(result, shift=DOWN * 0.2), run_time=0.4)
        self.wait(dur - 2.4)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Not the energy — the mismatch.\nSudden wavelength change splits the wave.\nPart passes. Part bounces.",
                      font=DISPLAY, color=INK, font_size=22, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.2, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
