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
        title = Text("Why One Electron Builds an\nInterference Pattern by Itself",
                     font=DISPLAY, color=INK, font_size=36, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B02_WaterWaves(Scene):
    """Two-slit interference with waves — classic demo."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        x_vals = np.linspace(-6, 6, 300)

        # Two slits at y=0, x=-1 and x=+1
        # Interference pattern on screen at right
        screen_x = 5.5

        # Draw the double-slit barrier
        slit_top = Line([-0.2, 3.5, 0], [-0.2, 0.4, 0], color=INK, stroke_width=5)
        slit_gap1 = Line([-0.2, 0.3, 0], [-0.2, -0.3, 0], color=TEAL, stroke_width=1)
        slit_mid = Line([-0.2, -0.4, 0], [-0.2, 0.4, 0], color=INK, stroke_width=5)
        # Actually simplified: just two vertical lines with gaps
        barrier_top = Line([-0.2, 3.8, 0], [-0.2, 0.8, 0], color=INK, stroke_width=5)
        barrier_mid = Line([-0.2, 0.2, 0], [-0.2, -0.2, 0], color=INK, stroke_width=5)
        barrier_bot = Line([-0.2, -0.8, 0], [-0.2, -3.8, 0], color=INK, stroke_width=5)

        # Incoming wave (left)
        inc_wave = VMobject(color=TEAL, stroke_width=2.5)
        inc_pts = []
        for x in np.linspace(-5.5, -0.3, 100):
            inc_pts.append(np.array([x, 0.8 * np.sin(5 * x + 2), 0]))
        inc_wave.set_points_smoothly(inc_pts)

        # Interference fringes on screen (bright/dark)
        bright_y = [2.5, 1.0, -0.5, -2.0]
        dark_y = [1.75, 0.25, -1.25, -2.75]

        screen = Line([screen_x, -3.8, 0], [screen_x, 3.8, 0], color=INK, stroke_width=2.5)
        bright_lines = VGroup(*[
            Line([screen_x - 0.15, y, 0], [screen_x + 0.15, y, 0], color=TEAL, stroke_width=5)
            for y in bright_y
        ])
        bright_lbl = SerifLabel("bright fringes", accent=TEAL, size=20).move_to([6.0, 2.5, 0])

        self.play(
            Create(barrier_top), Create(barrier_mid), Create(barrier_bot),
            run_time=0.4
        )
        self.play(Create(inc_wave), run_time=0.5)
        self.play(Create(screen), run_time=0.3)
        self.play(Create(bright_lines), FadeIn(bright_lbl), run_time=dur * 0.4)
        self.wait(dur * 0.2)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("One electron at a time.\nClassical predicts a smear.\nThe experiment shows fringes. Why?",
                     font=DISPLAY, color=INK, font_size=24, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_SingleDots(Scene):
    """Dots accumulating on screen — particle detections."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Screen
        screen = Rectangle(width=3.0, height=6.5, color=INK, stroke_width=2.5, fill_opacity=0)
        screen.move_to([3.0, 0, 0])

        screen_lbl = SerifLabel("detector screen", accent=INK, size=20).move_to([3.0, -3.6, 0])

        # Individual dot
        dot1 = Dot(color=CRIMSON, radius=0.12).move_to([3.0, 1.5, 0])
        label1 = SerifLabel("one electron", accent=CRIMSON, size=20).move_to([-2.0, 1.5, 0])

        self.play(Create(screen), FadeIn(screen_lbl), run_time=0.4)
        self.play(FadeIn(label1), run_time=0.3)
        self.play(FadeIn(dot1, scale=2.0), run_time=0.4)
        self.play(dot1.animate.scale(0.7), run_time=0.2)

        # A few more dots in random positions
        positions = [(2.7, 0.8), (3.3, -1.2), (2.9, -0.3), (3.1, 2.2), (2.6, -1.8)]
        dots = VGroup()
        for px, py in positions:
            d = Dot(color=CRIMSON, radius=0.1).move_to([px, py, 0])
            dots.add(d)

        for d in dots:
            self.play(FadeIn(d, scale=1.5), run_time=0.2)

        self.wait(dur * 0.3)


class B05_WaveFunctionBothSlits(Scene):
    """Single electron's wave function spreading from two slits."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Barrier with two slits
        barrier_top = Line([0.0, 3.8, 0], [0.0, 0.8, 0], color=INK, stroke_width=5)
        barrier_mid = Line([0.0, 0.2, 0], [0.0, -0.2, 0], color=INK, stroke_width=5)
        barrier_bot = Line([0.0, -0.8, 0], [0.0, -3.8, 0], color=INK, stroke_width=5)

        # Wave from upper slit
        upper_center = [0, 0.5, 0]
        lower_center = [0, -0.5, 0]

        # Circular wavefronts from each slit
        circles_upper = VGroup(*[
            Circle(radius=r, color=TEAL, stroke_width=1.5, stroke_opacity=0.7)
            .move_to(upper_center)
            for r in [1.0, 2.0, 3.0]
        ])
        circles_lower = VGroup(*[
            Circle(radius=r, color=TEAL, stroke_width=1.5, stroke_opacity=0.7)
            .move_to(lower_center)
            for r in [1.0, 2.0, 3.0]
        ])

        lbl = SerifLabel("wave through both slits", accent=TEAL, size=22).move_to([4.0, 3.2, 0])

        self.play(
            Create(barrier_top), Create(barrier_mid), Create(barrier_bot),
            run_time=0.4
        )
        self.play(Create(circles_upper), Create(circles_lower), run_time=dur * 0.5)
        self.play(FadeIn(lbl), run_time=0.4)
        self.wait(dur * 0.2)


class B06_Interference(Scene):
    """Probability density pattern — bright/dark alternation."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Vertical screen on the right
        screen_x = 4.0
        screen = Line([screen_x, -3.5, 0], [screen_x, 3.5, 0], color=INK, stroke_width=2.5)

        # Interference pattern as rectangles of varying intensity
        fringe_y = [2.4, 1.2, 0, -1.2, -2.4]
        fringes = VGroup(*[
            Rectangle(width=0.8, height=0.8, fill_color=TEAL, fill_opacity=0.8,
                      stroke_width=0).move_to([screen_x + 0.4, y, 0])
            for y in fringe_y
        ])
        dark_y = [1.8, 0.6, -0.6, -1.8]
        darks = VGroup(*[
            Rectangle(width=0.8, height=0.8, fill_color=INK, fill_opacity=0.1,
                      stroke_width=0).move_to([screen_x + 0.4, y, 0])
            for y in dark_y
        ])

        prob_lbl = SerifLabel("probability density |psi|^2", accent=TEAL, size=22).move_to([3.0, -3.2, 0])
        bright_lbl = LabelChip("BRIGHT = high probability", accent=TEAL, size=18).move_to([-1.5, 2.2, 0])
        dark_lbl = LabelChip("DARK = near zero", accent=INK, size=18).move_to([-1.5, 1.6, 0])

        self.play(Create(screen), run_time=0.3)
        self.play(Create(fringes), Create(darks), run_time=dur * 0.4)
        self.play(FadeIn(prob_lbl), FadeIn(bright_lbl), FadeIn(dark_lbl), run_time=0.6)
        self.wait(dur * 0.3)


class B07_PatternBuilds(Scene):
    """Dots accumulating into fringe pattern."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        np.random.seed(42)

        screen_x = 3.5
        screen = Line([screen_x - 1.5, -3.5, 0], [screen_x - 1.5, 3.5, 0],
                      color=INK, stroke_width=2.5)

        # Dots sampled from interference distribution
        bright_y = [2.4, 1.2, 0.0, -1.2, -2.4]
        all_dots = VGroup()
        dot_positions = []
        for _ in range(30):
            cy = np.random.choice(bright_y) + np.random.normal(0, 0.25)
            cx = np.random.normal(screen_x - 1.5, 0.15)
            dot_positions.append((cx, np.clip(cy, -3.3, 3.3)))

        self.play(Create(screen), run_time=0.3)
        for i, (px, py) in enumerate(dot_positions[:30]):
            d = Dot(color=CRIMSON, radius=0.08).move_to([px, py, 0])
            all_dots.add(d)
            self.play(FadeIn(d), run_time=0.08)

        count_lbl = SerifLabel("fringes emerge from dots", accent=TEAL, size=24).move_to([0, -3.2, 0])
        self.play(FadeIn(count_lbl), run_time=0.4)
        self.wait(dur * 0.2)


class B08_DeBroglieLabel(Scene):
    """de Broglie formula lambda = h/p with arrows."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        formula = Text("lambda = h / p", font=MONO, color=TEAL, font_size=44).move_to([0, 1.0, 0])

        lbl_h = SerifLabel("Planck's constant", accent=INK, size=22).move_to([-2.5, -0.5, 0])
        lbl_p = SerifLabel("momentum", accent=INK, size=22).move_to([2.5, -0.5, 0])
        lbl_l = SerifLabel("wavelength", accent=TEAL, size=22).move_to([0, 2.5, 0])

        arr_h = Arrow(start=[-2.5, -0.2, 0], end=[-1.2, 0.8, 0], color=INK, stroke_width=2, buff=0.1)
        arr_p = Arrow(start=[2.5, -0.2, 0], end=[1.2, 0.8, 0], color=INK, stroke_width=2, buff=0.1)

        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.8)
        self.play(
            FadeIn(lbl_l),
            GrowArrow(arr_h), FadeIn(lbl_h),
            GrowArrow(arr_p), FadeIn(lbl_p),
            run_time=0.7
        )
        self.wait(dur - 1.7)


class B09_Example(Scene):
    """Illustrative: 54 eV electron, lambda ~ 0.17 nm."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        params = Text("E = 54 eV", font=MONO, color=TEAL, font_size=30).move_to([0, 2.0, 0])
        arrow = Arrow(start=[0, 1.5, 0], end=[0, 0.5, 0], color=INK, stroke_width=2.5, buff=0.1)
        result = Text("lambda ~ 0.17 nm", font=MONO, color=TEAL, font_size=36).move_to([0, 0.0, 0])
        comparison = Text("comparable to atom spacing", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC).move_to([0, -1.0, 0])
        fringe_lbl = SerifLabel("fringe spacing measurable", accent=TEAL, size=22).move_to([0, -2.0, 0])

        self.play(FadeIn(ill_lbl), FadeIn(params), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.play(FadeIn(result, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(comparison), FadeIn(fringe_lbl), run_time=0.5)
        self.wait(dur - 1.7)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("One electron. Both slits.\nOne dot. The wave was the whole electron.",
                      font=DISPLAY, color=INK, font_size=30, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.2, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
