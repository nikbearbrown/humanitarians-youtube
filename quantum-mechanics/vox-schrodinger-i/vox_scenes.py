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
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.8)
        headline = Text("Why the i in\nSchrodinger's Equation\nChanges Everything",
                        font=DISPLAY, font_size=36, color=INK,
                        line_spacing=1.2).move_to(DOWN * 0.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(headline), run_time=1.0)
        self.wait(duration - 1.5)


# ---------------------------------------------------------------------------
# B02 — Two equations side by side (GRAPHIC beat — compare)
# ---------------------------------------------------------------------------
class B02_TwoEquations(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Left: Schrodinger (TEAL)
        label_wave = Text("WITH  i  (Schrodinger)", font=DISPLAY, font_size=24,
                          color=TEAL).move_to(LEFT * 3.5 + UP * 2.2)
        box_wave = Rectangle(width=5.2, height=3.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 2)
        box_wave.move_to(LEFT * 3.5)
        eq_wave = Text("ih  d/dt  psi  =  -(h^2/2m)  d^2/dx^2  psi",
                       font="PT Mono", font_size=16, color=TEAL).move_to(LEFT * 3.5 + UP * 0.2)
        tag_wave = Text("wave  -->  propagates", font=DISPLAY, font_size=20,
                        color=TEAL).move_to(LEFT * 3.5 + DOWN * 0.8)

        # Right: diffusion (CRIMSON)
        label_diff = Text("WITHOUT  i  (diffusion)", font=DISPLAY, font_size=24,
                          color=CRIMSON).move_to(RIGHT * 3.5 + UP * 2.2)
        box_diff = Rectangle(width=5.2, height=3.0).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 2)
        box_diff.move_to(RIGHT * 3.5)
        eq_diff = Text("h  d/dt  psi  =  (h^2/2m)  d^2/dx^2  psi",
                       font="PT Mono", font_size=16, color=CRIMSON).move_to(RIGHT * 3.5 + UP * 0.2)
        tag_diff = Text("spreads  irreversibly", font=DISPLAY, font_size=20,
                        color=CRIMSON).move_to(RIGHT * 3.5 + DOWN * 0.8)

        divider = Line(UP * 2.8, DOWN * 2.8, color=INK, stroke_width=1).set_opacity(0.3)

        self.play(
            GrowFromCenter(box_wave), GrowFromCenter(box_diff),
            run_time=0.8
        )
        self.play(
            FadeIn(label_wave), FadeIn(label_diff),
            run_time=0.5
        )
        self.play(
            Write(eq_wave), Write(eq_diff),
            run_time=1.2
        )
        self.play(
            FadeIn(tag_wave), FadeIn(tag_diff),
            Create(divider),
            run_time=0.8
        )
        self.wait(duration - 3.5)


# ---------------------------------------------------------------------------
# B03 — Highlight the i (GRAPHIC beat — Transform)
# ---------------------------------------------------------------------------
class B03_HighlightI(Scene):
    def construct(self):
        duration = DUR.get("B03", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        full_eq = Text("ih  d/dt  psi  =  -(h^2/2m)  d^2/dx^2  psi",
                       font="PT Mono", font_size=28, color=INK).move_to(UP * 0.5)

        # Highlight box around the "i"
        i_highlight = Rectangle(width=0.55, height=0.65).set_fill(GOLD, 0.5).set_stroke(GOLD, 2)
        i_highlight.move_to(full_eq.get_left() + RIGHT * 0.28 + UP * 0.0)

        without_i = Text("h  d/dt  psi  =  (h^2/2m)  d^2/dx^2  psi",
                         font="PT Mono", font_size=28, color=CRIMSON).move_to(DOWN * 1.2)
        label_without = Text("remove the i ---> diffusion", font=DISPLAY, font_size=22,
                             color=CRIMSON).move_to(DOWN * 2.3)

        self.play(Write(full_eq), run_time=1.0)
        self.play(GrowFromCenter(i_highlight), run_time=0.6)
        self.play(
            Transform(full_eq.copy(), without_i),
            run_time=1.0
        )
        self.play(FadeIn(label_without), run_time=0.5)
        self.wait(duration - 3.3)


# ---------------------------------------------------------------------------
# B04 — THE QUESTION card (CARD beat)
# ---------------------------------------------------------------------------
class B04_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B04", 8.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 2.8)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        line1 = Text("Two equations, one factor of i apart.", font=SERIF, font_size=28, color=INK).move_to(UP * 1.4)
        line2 = Text("One propagates a wave. One spreads heat.", font=SERIF, font_size=26, color=INK).move_to(UP * 0.5)
        line3 = Text("Why does one symbol decide", font=SERIF, font_size=26, color=INK).move_to(DOWN * 0.4)
        line4 = Text("whether quantum mechanics works at all?", font=SERIF, font_size=26, color=INK).move_to(DOWN * 1.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.6)
        self.play(Write(line1), run_time=0.6)
        self.play(Write(line2), run_time=0.7)
        self.play(Write(line3), Write(line4), run_time=0.7)
        self.wait(duration - 2.6)


# ---------------------------------------------------------------------------
# B05 — Diffusion spreading (GRAPHIC beat — Create)
# ---------------------------------------------------------------------------
class B05_DiffusionSpread(Scene):
    def construct(self):
        duration = DUR.get("B05", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Diffusion (no i)", font=DISPLAY, font_size=26, color=CRIMSON).move_to(UP * 3.0)

        # x-axis
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2).move_to(DOWN * 1.5)
        ax_label = Text("position", font=DISPLAY, font_size=18, color=INK).move_to(DOWN * 2.1)

        # Initial Gaussian (narrow, CRIMSON)
        def gaussian_points(sigma, n=60):
            xs = np.linspace(-5, 5, n)
            ys = np.exp(-xs**2 / (2 * sigma**2))
            return [np.array([x * 0.9, y * 1.6 - 1.5, 0]) for x, y in zip(xs, ys)]

        curve0 = VMobject().set_points_as_corners(gaussian_points(0.5))
        curve0.set_stroke(CRIMSON, 3).set_fill(opacity=0)
        curve1 = VMobject().set_points_as_corners(gaussian_points(1.4))
        curve1.set_stroke(CRIMSON, 2).set_fill(opacity=0)
        curve2 = VMobject().set_points_as_corners(gaussian_points(2.8))
        curve2.set_stroke(CRIMSON, 1).set_fill(opacity=0).set_opacity(0.5)

        label_t0 = Text("t = 0", font=DISPLAY, font_size=16, color=CRIMSON).move_to(LEFT * 4.0 + UP * 0.5)
        label_t1 = Text("later", font=DISPLAY, font_size=16, color=CRIMSON).move_to(LEFT * 1.5 + UP * 0.0)
        label_t2 = Text("later still", font=DISPLAY, font_size=16, color=CRIMSON).move_to(RIGHT * 2.0 + DOWN * 0.3)

        self.play(Create(axis), FadeIn(ax_label), FadeIn(title), run_time=0.7)
        self.play(Create(curve0), FadeIn(label_t0), run_time=0.8)
        self.play(Transform(curve0.copy(), curve1), FadeIn(label_t1), run_time=1.0)
        self.play(Transform(curve0.copy(), curve2), FadeIn(label_t2), run_time=1.2)
        self.wait(duration - 3.9)


# ---------------------------------------------------------------------------
# B07 — No-i electron packet dissolves (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_PacketDissolves(Scene):
    def construct(self):
        duration = DUR.get("B07", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Electron packet WITHOUT i", font=DISPLAY, font_size=26,
                     color=CRIMSON).move_to(UP * 3.0)
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2).move_to(DOWN * 1.5)
        ax_label = Text("position", font=DISPLAY, font_size=18, color=INK).move_to(DOWN * 2.1)

        def gauss(sigma, xshift=0, n=60):
            xs = np.linspace(-5, 5, n)
            ys = np.exp(-(xs - xshift)**2 / (2 * sigma**2))
            return [np.array([x * 0.9, y * 1.8 - 1.5, 0]) for x, y in zip(xs, ys)]

        curve_start = VMobject().set_points_as_corners(gauss(0.4))
        curve_start.set_stroke(CRIMSON, 3).set_fill(opacity=0)

        curve_spread = VMobject().set_points_as_corners(gauss(3.5))
        curve_spread.set_stroke(CRIMSON, 1).set_fill(opacity=0).set_opacity(0.4)

        stamp = Text("smear -- never returns", font=DISPLAY, font_size=20,
                     color=CRIMSON).move_to(DOWN * 0.3)

        self.play(Create(axis), FadeIn(ax_label), FadeIn(title), run_time=0.7)
        self.play(Create(curve_start), run_time=0.7)
        self.play(Transform(curve_start, curve_spread), run_time=1.8)
        self.play(FadeIn(stamp), run_time=0.5)
        self.wait(duration - 3.9)


# ---------------------------------------------------------------------------
# B08 — Section card: THE MECHANISM (CARD beat)
# ---------------------------------------------------------------------------
class B08_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B08", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("What the i actually does", font=DISPLAY, font_size=52,
                        color=INK).move_to(DOWN * 0.2)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.8)
        self.wait(duration - 1.3)


# ---------------------------------------------------------------------------
# B09 — No-i: derivatives add, push outward (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B09_DerivativesAdd(Scene):
    def construct(self):
        duration = DUR.get("B09", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Without i: both terms push OUTWARD", font=DISPLAY, font_size=24,
                     color=CRIMSON).move_to(UP * 3.0)

        # Central dot representing the amplitude peak
        center_dot = Dot(radius=0.35, color=CRIMSON).move_to(ORIGIN)
        center_label = Text("amplitude\npeak", font=DISPLAY, font_size=18,
                            color=CRIMSON).move_to(UP * 0.85)

        # Two arrows pointing outward — the derivatives
        arrow_left = Arrow(LEFT * 0.5, LEFT * 3.0, color=CRIMSON, buff=0,
                           stroke_width=4, max_tip_length_to_length_ratio=0.18)
        arrow_right = Arrow(RIGHT * 0.5, RIGHT * 3.0, color=CRIMSON, buff=0,
                            stroke_width=4, max_tip_length_to_length_ratio=0.18)

        label_dt = SerifLabel("time deriv.").move_to(LEFT * 2.0 + DOWN * 0.55)
        label_dx = SerifLabel("space deriv.").move_to(RIGHT * 2.0 + DOWN * 0.55)

        conclusion = Text("Sum: amplitude drains away = DIFFUSION", font=DISPLAY, font_size=22,
                          color=CRIMSON).move_to(DOWN * 2.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(center_dot), FadeIn(center_label), run_time=0.7)
        self.play(GrowArrow(arrow_left), GrowArrow(arrow_right), run_time=1.0)
        self.play(FadeIn(label_dt), FadeIn(label_dx), run_time=0.6)
        center_dot.set_opacity(0.3)
        self.play(
            center_dot.animate.scale(0.2),
            run_time=1.5
        )
        self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(duration - 5.1)


# ---------------------------------------------------------------------------
# B10 — i rotates contribution 90 degrees (GRAPHIC beat — Rotate)
# ---------------------------------------------------------------------------
class B10_IRotates(Scene):
    def construct(self):
        duration = DUR.get("B10", 14.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("With i: time deriv. rotated 90 degrees", font=DISPLAY, font_size=24,
                     color=TEAL).move_to(UP * 3.2)

        # Draw complex plane axes
        real_ax = Line(LEFT * 2.2, RIGHT * 2.2, color=INK, stroke_width=1.5).move_to(LEFT * 3.5)
        imag_ax = Line(DOWN * 2.2, UP * 2.2, color=INK, stroke_width=1.5).move_to(LEFT * 3.5)
        real_label = Text("Re", font=DISPLAY, font_size=18, color=INK).move_to(LEFT * 1.0 + DOWN * 0.35)
        imag_label = Text("Im", font=DISPLAY, font_size=18, color=INK).move_to(LEFT * 3.8 + UP * 2.0)

        # Arrow pointing right (no i — diffusion direction)
        arrow_real = Arrow(LEFT * 3.5, LEFT * 1.3, color=CRIMSON, buff=0,
                           stroke_width=4, max_tip_length_to_length_ratio=0.18)
        label_real = SerifLabel("no i: drains").move_to(LEFT * 2.2 + DOWN * 0.65)

        # Arrow pointing up (with i — rotated 90 deg)
        arrow_imag = Arrow(LEFT * 3.5, LEFT * 3.5 + UP * 2.0, color=TEAL, buff=0,
                           stroke_width=4, max_tip_length_to_length_ratio=0.18)
        label_imag = SerifLabel("with i: rotated").move_to(LEFT * 2.5 + UP * 1.1)

        # Right side: interference diagram
        right_title = Text("Result: interference, not diffusion", font=DISPLAY, font_size=22,
                           color=TEAL).move_to(RIGHT * 2.5 + UP * 1.5)

        axis_r = Line(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=2).move_to(RIGHT * 2.5 + DOWN * 1.0)
        def wave_points(n=80):
            xs = np.linspace(-1.5, 1.5, n)
            ys = np.sin(xs * 3.5) * 0.8
            return [np.array([x + 2.5, y - 1.0, 0]) for x, y in zip(xs, ys)]
        wave_curve = VMobject().set_points_as_corners(wave_points())
        wave_curve.set_stroke(TEAL, 3).set_fill(opacity=0)

        self.play(FadeIn(title), run_time=0.5)
        self.play(
            Create(real_ax), Create(imag_ax),
            FadeIn(real_label), FadeIn(imag_label),
            run_time=0.8
        )
        self.play(GrowArrow(arrow_real), FadeIn(label_real), run_time=0.8)
        self.play(
            Rotate(arrow_real, angle=PI/2, about_point=LEFT * 3.5),
            run_time=1.2
        )
        self.play(GrowArrow(arrow_imag), FadeIn(label_imag), run_time=0.7)
        self.play(
            FadeIn(right_title), Create(axis_r),
            run_time=0.6
        )
        self.play(Create(wave_curve), run_time=1.2)
        self.wait(duration - 6.0)


# ---------------------------------------------------------------------------
# B11 — Section card: probability conservation (CARD beat — rhythm break)
# ---------------------------------------------------------------------------
class B11_ProbCard(Scene):
    def construct(self):
        duration = DUR.get("B11", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("The i keeps probability\nfrom leaking away", font=DISPLAY,
                        font_size=44, color=INK, line_spacing=1.2).move_to(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.9)
        self.wait(duration - 1.4)


# ---------------------------------------------------------------------------
# B12 — Probability leaking without i (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B12_ProbLeaks(Scene):
    def construct(self):
        duration = DUR.get("B12", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Without i: total probability leaks", font=DISPLAY, font_size=26,
                     color=CRIMSON).move_to(UP * 3.2)

        # A "probability gauge" bar that drains
        gauge_bg = Rectangle(width=6.0, height=0.7).set_fill(SLATE, 0.15).set_stroke(INK, 1.5)
        gauge_bg.move_to(UP * 0.5)
        gauge_fill = Rectangle(width=6.0, height=0.7).set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        gauge_fill.move_to(UP * 0.5)
        gauge_label = Text("total  |psi|^2 = 1", font="PT Mono", font_size=22,
                           color=CRIMSON).move_to(UP * 1.45)

        # Target for drain animation: a nearly-empty bar anchored to the left edge of gauge_bg
        left_x = gauge_bg.get_left()[0]
        gauge_empty = Rectangle(width=0.15, height=0.7).set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        gauge_empty.move_to(np.array([left_x + 0.075, 0.5, 0]))

        consequence = Text("No stable atoms. No interference.\nNo spectral lines.", font=DISPLAY,
                           font_size=24, color=CRIMSON, line_spacing=1.2).move_to(DOWN * 1.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(gauge_bg), FadeIn(gauge_label), run_time=0.6)
        self.play(GrowFromCenter(gauge_fill), run_time=0.5)
        self.play(
            Transform(gauge_fill, gauge_empty),
            run_time=2.0
        )
        self.play(FadeIn(consequence), run_time=0.7)
        self.wait(duration - 4.5)


# ---------------------------------------------------------------------------
# B13 — THE IMPLICATION section card (CARD beat)
# ---------------------------------------------------------------------------
class B13_ImplicationCard(Scene):
    def construct(self):
        duration = DUR.get("B13", 8.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE IMPLICATION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("The i is not optional", font=DISPLAY, font_size=52,
                        color=INK).move_to(DOWN * 0.1)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.8)
        self.wait(duration - 1.3)


# ---------------------------------------------------------------------------
# B14 — THE EXAMPLE section card (CARD beat)
# ---------------------------------------------------------------------------
class B14_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B14", 8.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 2.0)
        headline = Text("An electron in a 1 nm pocket", font=DISPLAY, font_size=46,
                        color=INK).move_to(UP * 0.5)
        sub = Text("(illustrative)", font=SERIF, font_size=26,
                   color=SLATE).move_to(DOWN * 0.8)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(duration - 1.7)


# ---------------------------------------------------------------------------
# B15 — Side-by-side packet comparison (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B15_PacketComparison(Scene):
    def construct(self):
        duration = DUR.get("B15", 18.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Column labels
        left_title = Text("WITHOUT i", font=DISPLAY, font_size=24,
                          color=CRIMSON).move_to(LEFT * 3.5 + UP * 3.0)
        right_title = Text("WITH i (Schrodinger)", font=DISPLAY, font_size=24,
                           color=TEAL).move_to(RIGHT * 3.2 + UP * 3.0)
        divider = Line(UP * 3.5, DOWN * 3.5, color=INK, stroke_width=1).set_opacity(0.25)

        # Left axis / right axis
        left_ax = Line(LEFT * 6.2, LEFT * 0.5, color=INK, stroke_width=2).move_to(LEFT * 3.35 + DOWN * 1.8)
        right_ax = Line(LEFT * 0.0, RIGHT * 6.2, color=INK, stroke_width=2).move_to(RIGHT * 3.1 + DOWN * 1.8)

        # Left: spreading curve (CRIMSON)
        def left_start(n=60):
            xs = np.linspace(-6, 0, n)
            ys = np.exp(-(xs + 3)**2 / (2 * 0.3**2))
            return [np.array([x, y * 1.8 - 1.8, 0]) for x, y in zip(xs, ys)]

        def left_end(n=60):
            xs = np.linspace(-6, 0, n)
            ys = np.exp(-(xs + 3)**2 / (2 * 2.5**2)) * 0.3
            return [np.array([x, y * 1.8 - 1.8, 0]) for x, y in zip(xs, ys)]

        left_curve = VMobject().set_points_as_corners(left_start())
        left_curve.set_stroke(CRIMSON, 3).set_fill(opacity=0)
        left_end_mob = VMobject().set_points_as_corners(left_end())
        left_end_mob.set_stroke(CRIMSON, 1).set_fill(opacity=0)

        left_note = Text("10 nm wide in 3 fs", font=DISPLAY, font_size=18,
                         color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 2.7)

        # Right: traveling packet (TEAL)
        def right_gauss(xc, n=60):
            xs = np.linspace(0.5, 7.0, n)
            ys = np.exp(-(xs - xc)**2 / (2 * 0.35**2))
            return [np.array([x - 0.5, y * 1.8 - 1.8, 0]) for x, y in zip(xs, ys)]

        right_curve = VMobject().set_points_as_corners(right_gauss(1.5))
        right_curve.set_stroke(TEAL, 3).set_fill(opacity=0)
        right_moved = VMobject().set_points_as_corners(right_gauss(4.8))
        right_moved.set_stroke(TEAL, 3).set_fill(opacity=0)

        detector = Rectangle(width=0.25, height=1.5).set_fill(TEAL, 0.6).set_stroke(TEAL, 2)
        detector.move_to(RIGHT * 5.8 + DOWN * 1.1)
        detector_label = Text("detector", font=DISPLAY, font_size=16,
                              color=TEAL).move_to(RIGHT * 5.8 + DOWN * 2.1)

        right_note = Text("arrives intact -- 5 nm gap crossed", font=DISPLAY, font_size=18,
                          color=TEAL).move_to(RIGHT * 3.1 + DOWN * 2.7)

        self.play(
            FadeIn(left_title), FadeIn(right_title), Create(divider),
            run_time=0.7
        )
        self.play(
            Create(left_ax), Create(right_ax),
            run_time=0.6
        )
        self.play(
            Create(left_curve), Create(right_curve),
            run_time=0.9
        )
        self.play(
            Transform(left_curve, left_end_mob),
            Transform(right_curve, right_moved),
            run_time=2.5
        )
        self.play(
            FadeIn(left_note), FadeIn(right_note),
            GrowFromCenter(detector), FadeIn(detector_label),
            run_time=1.0
        )
        self.wait(duration - 6.5)


# ---------------------------------------------------------------------------
# B16 — RECAP endcard (CARD beat)
# ---------------------------------------------------------------------------
class B16_Recap(Scene):
    def construct(self):
        duration = DUR.get("B16", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        line1 = Text("Remove the i:", font=DISPLAY, font_size=34,
                     color=CRIMSON).move_to(UP * 1.1)
        line2 = Text("wave becomes heat, spreading forever.", font=SERIF, font_size=30,
                     color=CRIMSON).move_to(UP * 0.3)
        line3 = Text("Keep it:", font=DISPLAY, font_size=34,
                     color=TEAL).move_to(DOWN * 0.7)
        line4 = Text("amplitude propagates coherently.", font=SERIF, font_size=30,
                     color=TEAL).move_to(DOWN * 1.5)
        kicker = Text("The i is why quantum mechanics exists.", font=DISPLAY,
                      font_size=28, color=INK).move_to(DOWN * 2.8)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(line1), Write(line2), run_time=1.0)
        self.play(Write(line3), Write(line4), run_time=1.0)
        self.play(FadeIn(kicker), run_time=0.6)
        self.wait(duration - 3.1)
