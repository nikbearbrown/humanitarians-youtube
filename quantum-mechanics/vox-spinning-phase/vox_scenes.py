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
        title = Text("Why a Stationary State\nIs Secretly Spinning",
                     font=DISPLAY, color=INK, font_size=36, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])
        sub = Text("the hidden phase", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_StaticHistogram(Scene):
    """Two identical histograms at t=0 and t=later — nothing changes."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Left histogram (t = 0)
        lbl_t0 = SerifLabel("measurement at t = 0", accent=INK, size=20).move_to([-3.5, 3.0, 0])
        bar_heights_l = [1.0, 2.2, 3.4, 2.8, 1.6, 0.8]
        bars_l = VGroup()
        for i, h in enumerate(bar_heights_l):
            b = Rectangle(width=0.55, height=h, fill_color=CRIMSON, fill_opacity=0.8,
                          stroke_width=0).move_to([-5.0 + i * 0.65, h / 2 - 2.5, 0])
            bars_l.add(b)

        # Right histogram (t = later) — identical
        lbl_t1 = SerifLabel("measurement at t = later", accent=INK, size=20).move_to([2.5, 3.0, 0])
        bars_r = VGroup()
        for i, h in enumerate(bar_heights_l):
            b = Rectangle(width=0.55, height=h, fill_color=CRIMSON, fill_opacity=0.8,
                          stroke_width=0).move_to([1.0 + i * 0.65, h / 2 - 2.5, 0])
            bars_r.add(b)

        equal_lbl = LabelChip("same every time", accent=CRIMSON, size=20).move_to([0, -3.2, 0])

        self.play(FadeIn(lbl_t0), run_time=0.3)
        self.play(Create(bars_l), run_time=0.7)
        self.play(FadeIn(lbl_t1), run_time=0.3)
        self.play(Create(bars_r), run_time=0.7)
        self.play(GrowFromCenter(equal_lbl), run_time=0.4)
        self.wait(dur - 2.5)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("The wave function has a rotating phase.\nMeasurements stay constant.\nHow can a spinning thing cast a still shadow?",
                     font=DISPLAY, color=INK, font_size=18, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_ClockHand(Scene):
    """Complex plane: clock hand with length and direction."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Axes
        ax_re = Arrow(start=[-3.5, 0, 0], end=[3.5, 0, 0], color=INK, stroke_width=2, buff=0)
        ax_im = Arrow(start=[0, -3.5, 0], end=[0, 3.5, 0], color=INK, stroke_width=2, buff=0)
        re_lbl = SerifLabel("Re", accent=INK, size=22).move_to([3.8, 0, 0])
        im_lbl = SerifLabel("Im", accent=INK, size=22).move_to([0, 3.8, 0])

        # Clock hand at angle 45 degrees
        angle = PI / 4
        end_pt = np.array([2.5 * np.cos(angle), 2.5 * np.sin(angle), 0])
        hand = Arrow(start=[0, 0, 0], end=end_pt, color=TEAL, stroke_width=4, buff=0)
        dot_end = Dot(color=TEAL, radius=0.12).move_to(end_pt)

        length_lbl = SerifLabel("length = |psi|", accent=TEAL, size=22).move_to([1.5, -1.2, 0])
        dir_lbl = SerifLabel("direction = phase", accent=INK, size=20).move_to([-2.5, 1.5, 0])

        self.play(GrowArrow(ax_re), GrowArrow(ax_im), FadeIn(re_lbl), FadeIn(im_lbl), run_time=0.6)
        self.play(GrowArrow(hand), FadeIn(dot_end), run_time=0.7)
        self.play(FadeIn(length_lbl), FadeIn(dir_lbl), run_time=0.5)
        self.wait(dur - 2.0)


class B05_SpinningClock(Scene):
    """Clock hand rotating — phase spinning at rate E/hbar."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Axes
        ax_re = Line([-3.0, 0, 0], [3.0, 0, 0], color=INK, stroke_width=1.5)
        ax_im = Line([0, -3.0, 0], [0, 3.0, 0], color=INK, stroke_width=1.5)

        # Clock hand that will rotate
        initial_angle = 0.0
        hand_len = 2.2
        start_pt = np.array([hand_len * np.cos(initial_angle), hand_len * np.sin(initial_angle), 0])
        hand = Arrow(start=[0, 0, 0], end=start_pt, color=TEAL, stroke_width=4, buff=0)

        rate_lbl = LabelChip("rate = E / hbar", accent=TEAL, size=22).move_to([0, -3.5, 0])
        faster_lbl = SerifLabel("higher E = faster spin", accent=INK, size=20).move_to([3.5, 2.5, 0])

        self.play(Create(ax_re), Create(ax_im), run_time=0.3)
        self.play(GrowArrow(hand), run_time=0.4)
        self.play(FadeIn(rate_lbl), run_time=0.3)
        # Rotate the hand around the origin
        self.play(Rotate(hand, angle=TAU * 1.5, about_point=ORIGIN), run_time=dur * 0.55)
        self.play(FadeIn(faster_lbl), run_time=0.4)
        self.wait(dur * 0.15)


class B06_ShadowStill(Scene):
    """Spinning clock hand above; its shadow (|psi|^2) stays constant below."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Dividing line
        divider = DashedLine([-6.5, 0, 0], [6.5, 0, 0], color=INK, stroke_width=1.5, dash_length=0.2)
        top_lbl = SerifLabel("wave function (spinning)", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        bot_lbl = SerifLabel("probability density (still)", accent=CRIMSON, size=20).move_to([-3.5, -3.2, 0])

        # Spinning hand in top half
        ax_re = Line([-2.5, 1.5, 0], [2.5, 1.5, 0], color=INK, stroke_width=1.2)
        ax_im = Line([0, 0.2, 0], [0, 2.8, 0], color=INK, stroke_width=1.2)
        hand_len = 1.6
        hand_start = np.array([hand_len, 1.5, 0])
        hand = Arrow(start=[0, 1.5, 0], end=hand_start, color=TEAL, stroke_width=4, buff=0)

        # Shadow rectangle — stays the same width regardless of rotation
        shadow = Rectangle(width=3.2, height=0.6,
                           fill_color=CRIMSON, fill_opacity=0.75, stroke_width=0).move_to([0, -1.5, 0])
        shadow_eq = Text("|psi|^2 = const", font=MONO, color=CRIMSON, font_size=24).move_to([0, -2.5, 0])

        self.play(
            Create(divider),
            FadeIn(top_lbl), FadeIn(bot_lbl),
            run_time=0.5
        )
        self.play(Create(ax_re), Create(ax_im), GrowArrow(hand), run_time=0.5)
        self.play(FadeIn(shadow), run_time=0.4)
        # Rotate clock while shadow stays put
        self.play(
            Rotate(hand, angle=TAU * 1.5, about_point=[0, 1.5, 0]),
            run_time=dur * 0.55
        )
        self.play(FadeIn(shadow_eq), run_time=0.4)
        self.wait(dur * 0.1)


class B07_ClockAndShadow(Scene):
    """Side-by-side: clock (wave function) vs shadow (|psi|^2)."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Vertical divider
        divider = Line([0, -3.8, 0], [0, 3.8, 0], color=INK, stroke_width=1.5)

        # Left panel: spinning clock
        left_title = SerifLabel("wave function", accent=TEAL, size=22).move_to([-3.5, 3.2, 0])
        ax_re_l = Line([-5.5, 0.5, 0], [-0.3, 0.5, 0], color=INK, stroke_width=1.2)
        ax_im_l = Line([-2.9, -1.0, 0], [-2.9, 2.0, 0], color=INK, stroke_width=1.2)
        hand_l = Arrow(start=[-2.9, 0.5, 0], end=[-1.5, 1.6, 0], color=TEAL, stroke_width=4, buff=0)
        spin_lbl = LabelChip("spinning", accent=TEAL, size=18).move_to([-3.5, -2.2, 0])

        # Right panel: shadow bar
        right_title = SerifLabel("probability |psi|^2", accent=CRIMSON, size=22).move_to([3.5, 3.2, 0])
        shadow_bar = Rectangle(width=2.8, height=0.8,
                               fill_color=CRIMSON, fill_opacity=0.8, stroke_width=0).move_to([3.5, 0.5, 0])
        still_lbl = LabelChip("constant", accent=CRIMSON, size=18).move_to([3.5, -2.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(
            FadeIn(left_title), Create(ax_re_l), Create(ax_im_l), GrowArrow(hand_l),
            run_time=0.6
        )
        self.play(
            FadeIn(right_title), FadeIn(shadow_bar),
            run_time=0.5
        )
        self.play(GrowFromCenter(spin_lbl), GrowFromCenter(still_lbl), run_time=0.4)
        # Rotate left hand, shadow stays
        self.play(
            Rotate(hand_l, angle=TAU, about_point=[-2.9, 0.5, 0]),
            run_time=dur * 0.5
        )
        self.wait(dur * 0.1)


class B08_TwoRates(Scene):
    """Two clocks at different rates; when mixed, shadow oscillates."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        # Two clock panels at top
        # Left clock: lower energy (slower)
        ax1 = Line([-5.5, 2.0, 0], [-3.5, 2.0, 0], color=INK, stroke_width=1.2)
        ay1 = Line([-4.5, 1.0, 0], [-4.5, 3.0, 0], color=INK, stroke_width=1.2)
        hand1 = Arrow(start=[-4.5, 2.0, 0], end=[-3.6, 2.7, 0], color=TEAL, stroke_width=3, buff=0)
        lbl1 = SerifLabel("E1 — slow spin", accent=TEAL, size=18).move_to([-4.5, 0.5, 0])

        # Right clock: higher energy (faster)
        ax2 = Line([3.5, 2.0, 0], [5.5, 2.0, 0], color=INK, stroke_width=1.2)
        ay2 = Line([4.5, 1.0, 0], [4.5, 3.0, 0], color=INK, stroke_width=1.2)
        hand2 = Arrow(start=[4.5, 2.0, 0], end=[5.4, 2.7, 0], color=TEAL, stroke_width=3, buff=0)
        lbl2 = SerifLabel("E2 — fast spin", accent=TEAL, size=18).move_to([4.5, 0.5, 0])

        # Mixed shadow at bottom: oscillates
        shadow_mixed = Rectangle(width=2.0, height=0.5,
                                 fill_color=CRIMSON, fill_opacity=0.8, stroke_width=0).move_to([0, -1.5, 0])
        shadow_lbl = LabelChip("mixed: shadow moves", accent=CRIMSON, size=20).move_to([0, -2.5, 0])

        note = SerifLabel("single eigenstate: shadow still\nmixed eigenstates: shadow oscillates",
                          accent=INK, size=18).move_to([0, -3.4, 0])

        self.play(
            Create(ax1), Create(ay1), GrowArrow(hand1), FadeIn(lbl1),
            Create(ax2), Create(ay2), GrowArrow(hand2), FadeIn(lbl2),
            run_time=0.7
        )
        self.play(
            Rotate(hand1, angle=TAU * 0.8, about_point=[-4.5, 2.0, 0]),
            Rotate(hand2, angle=TAU * 1.6, about_point=[4.5, 2.0, 0]),
            run_time=dur * 0.4
        )
        self.play(FadeIn(shadow_mixed), run_time=0.4)
        # Animate shadow width to show oscillation
        self.play(
            shadow_mixed.animate.stretch_to_fit_width(3.5),
            run_time=0.5
        )
        self.play(
            shadow_mixed.animate.stretch_to_fit_width(1.2),
            run_time=0.5
        )
        self.play(GrowFromCenter(shadow_lbl), run_time=0.3)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur * 0.1)


class B09_Example(Scene):
    """Illustrative: 1 eV ground state, omega ~ 1.5e15 rad/s."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        params = Text("E = 1 eV", font=MONO, color=TEAL, font_size=32).move_to([0, 2.2, 0])
        arrow = Arrow(start=[0, 1.7, 0], end=[0, 0.7, 0], color=INK, stroke_width=2.5, buff=0.1)
        result = Text("omega = E / hbar", font=MONO, color=TEAL, font_size=28).move_to([0, 0.2, 0])
        arrow2 = Arrow(start=[0, -0.3, 0], end=[0, -1.3, 0], color=INK, stroke_width=2.5, buff=0.1)
        value = Text("~ 1.5 x 10^15 rad/s", font=MONO, color=TEAL, font_size=32).move_to([0, -1.8, 0])
        compare = Text("a million times faster than visible light",
                       font=SERIF, color=INK, font_size=20, slant=ITALIC).move_to([0, -2.8, 0])

        self.play(FadeIn(ill_lbl), FadeIn(params), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.play(FadeIn(result), run_time=0.4)
        self.play(GrowArrow(arrow2), run_time=0.3)
        self.play(FadeIn(value, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(compare), run_time=0.4)
        self.wait(dur - 2.3)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("The wave function spins.\nThe probability is its shadow.\nThe shadow holds still.",
                      font=DISPLAY, color=INK, font_size=28, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.2, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
