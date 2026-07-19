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
        title = Text("Why a Warm Box Doesn't Glow\nWith Infinite Energy",
                     font=DISPLAY, color=INK, font_size=34, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        sub = Text("the ultraviolet catastrophe", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_BoxRadiation(Scene):
    """Hot box with radiation waves inside."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        box = Rectangle(width=5.0, height=4.0, color=INK, stroke_width=3, fill_opacity=0).move_to([0, 0, 0])
        temp_lbl = LabelChip("T = 3000 K", accent=CRIMSON, size=22).move_to([0, -3.0, 0])

        # Radiation waves inside box
        x_vals = np.linspace(-2.3, 2.3, 200)
        for i, k in enumerate([2, 4, 6]):
            amp = 0.4
            pts = [np.array([x, amp * np.sin(k * x) + (i - 1) * 0.8, 0]) for x in x_vals]
            wave = VMobject(color=CRIMSON, stroke_width=1.5, stroke_opacity=0.7)
            wave.set_points_smoothly(pts)
            self.add(wave)

        radiate_lbl = SerifLabel("radiation modes inside", accent=INK, size=20).move_to([0, 2.5, 0])

        self.play(Create(box), FadeIn(radiate_lbl), run_time=0.5)
        self.play(GrowFromCenter(temp_lbl), run_time=0.4)
        self.wait(dur - 1.1)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Classical: every wave mode gets same energy.\nShorter wavelengths: more modes.\nTotal energy: infinite.\nBut real ovens don't explode. Why?",
                     font=DISPLAY, color=INK, font_size=17, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_ClassicalCurve(Scene):
    """Rayleigh-Jeans curve climbing to infinity."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Axes
        ax_x = Arrow(start=[-5.5, -3.0, 0], end=[5.5, -3.0, 0], color=INK, stroke_width=2, buff=0)
        ax_y = Arrow(start=[-5.5, -3.0, 0], end=[-5.5, 3.5, 0], color=INK, stroke_width=2, buff=0)
        x_lbl = SerifLabel("frequency", accent=INK, size=18).move_to([5.5, -3.4, 0])
        y_lbl = SerifLabel("energy per mode", accent=INK, size=18).move_to([-3.5, 3.4, 0])

        # Classical Rayleigh-Jeans: proportional to freq^2 (rising)
        freqs = np.linspace(0.1, 4.0, 100)
        rj_height_scale = 0.4
        rj_pts = [np.array([-5.0 + f * 2.5, -3.0 + rj_height_scale * f ** 2, 0]) for f in freqs]
        rj_curve = VMobject(color=CRIMSON, stroke_width=3)
        rj_curve.set_points_smoothly(rj_pts)
        rj_lbl = LabelChip("Rayleigh-Jeans: rises forever", accent=CRIMSON, size=20).move_to([2.5, 2.8, 0])

        arrow_up = Arrow(start=[4.5, 1.0, 0], end=[4.5, 3.0, 0], color=CRIMSON, stroke_width=3, buff=0.1)

        self.play(GrowArrow(ax_x), GrowArrow(ax_y), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(rj_curve), run_time=dur * 0.4)
        self.play(GrowFromCenter(rj_lbl), GrowArrow(arrow_up), run_time=0.4)
        self.wait(dur * 0.15)


class B05_QuantumFix(Scene):
    """Discrete energy steps vs continuous: the Planck insight."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: classical continuous
        left_title = SerifLabel("classical: continuous", accent=CRIMSON, size=20).move_to([-3.5, 3.2, 0])
        ax_l = Line([-5.5, -2.5, 0], [-0.5, -2.5, 0], color=INK, stroke_width=1.5)
        cont_arrow = Arrow(start=[-5.0, -2.5, 0], end=[-5.0, 2.5, 0], color=CRIMSON, stroke_width=3, buff=0)
        fill_l = Rectangle(width=1.5, height=3.5, fill_color=CRIMSON, fill_opacity=0.3,
                           stroke_width=0).move_to([-3.0, -0.5, 0])
        any_e_lbl = SerifLabel("any energy", accent=CRIMSON, size=18).move_to([-3.0, -2.2, 0])

        # Right: quantum discrete steps
        right_title = SerifLabel("quantum: discrete", accent=TEAL, size=20).move_to([3.5, 3.2, 0])
        ax_r = Line([0.5, -2.5, 0], [5.5, -2.5, 0], color=INK, stroke_width=1.5)
        for i in range(5):
            step = Line([1.0, -2.5 + i * 1.0, 0], [5.0, -2.5 + i * 1.0, 0],
                        color=TEAL, stroke_width=2.5)
            self.add(step)
        step_lbl = SerifLabel("n * hν only", accent=TEAL, size=18).move_to([3.0, -2.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), Create(ax_l), GrowArrow(cont_arrow), FadeIn(fill_l), FadeIn(any_e_lbl), run_time=0.7)
        self.play(FadeIn(right_title), Create(ax_r), FadeIn(step_lbl), run_time=0.6)
        self.wait(dur - 1.7)


class B06_HighFreqStarved(Scene):
    """High-frequency modes: hν >> kBT, nearly empty."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Axes
        ax_x = Arrow(start=[-5.5, -3.0, 0], end=[5.5, -3.0, 0], color=INK, stroke_width=2, buff=0)
        ax_y = Arrow(start=[-5.5, -3.0, 0], end=[-5.5, 2.5, 0], color=INK, stroke_width=2, buff=0)
        x_lbl = SerifLabel("frequency", accent=INK, size=18).move_to([5.5, -3.4, 0])
        y_lbl = SerifLabel("occupancy", accent=INK, size=18).move_to([-3.2, 2.6, 0])

        # kBT threshold line
        threshold = DashedLine([-5.5, -1.0, 0], [5.5, -1.0, 0], color=TEAL, stroke_width=2, dash_length=0.2)
        kt_lbl = SerifLabel("kBT threshold", accent=TEAL, size=18).move_to([-2.5, -0.5, 0])

        # Low freq: above threshold (TEAL filled)
        low_bar = Rectangle(width=3.5, height=2.0, fill_color=TEAL, fill_opacity=0.7,
                            stroke_width=0).move_to([-3.5, -2.0, 0])
        low_lbl = SerifLabel("low freq: hν < kBT\nmode excited", accent=TEAL, size=18).move_to([-3.0, 1.5, 0])

        # High freq: below threshold (CRIMSON very small)
        hi_bar = Rectangle(width=3.0, height=0.3, fill_color=CRIMSON, fill_opacity=0.7,
                           stroke_width=0).move_to([3.5, -2.85, 0])
        hi_lbl = SerifLabel("high freq: hν >> kBT\nnearly empty", accent=CRIMSON, size=18).move_to([3.5, 0.5, 0])

        self.play(GrowArrow(ax_x), GrowArrow(ax_y), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(threshold), FadeIn(kt_lbl), run_time=0.4)
        self.play(FadeIn(low_bar), FadeIn(low_lbl), run_time=0.5)
        self.play(FadeIn(hi_bar), FadeIn(hi_lbl), run_time=0.5)
        self.wait(dur - 2.1)


class B07_PlanckvsCurves(Scene):
    """Both curves: CRIMSON Rayleigh-Jeans diverges, TEAL Planck peaks and falls."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        ax_x = Arrow(start=[-5.5, -3.0, 0], end=[5.5, -3.0, 0], color=INK, stroke_width=2, buff=0)
        ax_y = Arrow(start=[-5.5, -3.0, 0], end=[-5.5, 3.5, 0], color=INK, stroke_width=2, buff=0)
        x_lbl = SerifLabel("frequency", accent=INK, size=18).move_to([5.5, -3.4, 0])

        freqs = np.linspace(0.05, 5.0, 200)
        # Rayleigh-Jeans: ~ freq^2
        rj_pts = []
        for f in freqs:
            y = -3.0 + 0.3 * f ** 2
            if y < 3.5:
                rj_pts.append(np.array([-5.0 + f * 2.0, y, 0]))
        rj_curve = VMobject(color=CRIMSON, stroke_width=2.5)
        rj_curve.set_points_smoothly(rj_pts)

        # Planck: ~ freq^3 / (exp(freq/0.8) - 1)
        planck_pts = []
        for f in freqs:
            y_raw = f ** 3 / (np.exp(f / 0.8) - 1) if np.exp(f / 0.8) > 1 else 0
            y = -3.0 + 1.2 * y_raw / 0.8
            if -3.5 < y < 3.5:
                planck_pts.append(np.array([-5.0 + f * 2.0, y, 0]))
        planck_curve = VMobject(color=TEAL, stroke_width=3)
        planck_curve.set_points_smoothly(planck_pts)

        rj_lbl = LabelChip("Rayleigh-Jeans", accent=CRIMSON, size=18).move_to([4.0, 2.5, 0])
        planck_lbl = LabelChip("Planck", accent=TEAL, size=18).move_to([-1.0, 2.5, 0])

        self.play(GrowArrow(ax_x), GrowArrow(ax_y), FadeIn(x_lbl), run_time=0.4)
        self.play(Create(rj_curve), GrowFromCenter(rj_lbl), run_time=0.6)
        self.play(Create(planck_curve), GrowFromCenter(planck_lbl), run_time=0.6)
        self.wait(dur - 1.8)


class B08_WholePackets(Scene):
    """Integer quanta staircase vs continuous ramp."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: continuous ramp
        left_title = SerifLabel("continuous energy", accent=CRIMSON, size=20).move_to([-3.5, 3.2, 0])
        ramp = Line([-5.5, -2.5, 0], [-0.5, 2.5, 0], color=CRIMSON, stroke_width=3)
        ramp_lbl = SerifLabel("any fraction allowed", accent=CRIMSON, size=18).move_to([-3.0, -1.5, 0])

        # Right: integer staircase
        right_title = SerifLabel("quantized energy", accent=TEAL, size=20).move_to([3.5, 3.2, 0])
        for i in range(5):
            h = -2.5 + i * 1.1
            h_next = h + 1.1
            step_h = Line([0.5 + i * 0.8, h, 0], [0.5 + (i + 1) * 0.8, h, 0],
                          color=TEAL, stroke_width=3)
            step_v = Line([0.5 + (i + 1) * 0.8, h, 0], [0.5 + (i + 1) * 0.8, h_next, 0],
                          color=TEAL, stroke_width=3)
            self.add(step_h, step_v)
        stair_lbl = SerifLabel("whole packets: 0, 1hv, 2hv...", accent=TEAL, size=18).move_to([3.5, -1.8, 0])

        insight = LabelChip("nature bills in whole packets", accent=TEAL, size=20).move_to([0, -3.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), Create(ramp), FadeIn(ramp_lbl), run_time=0.6)
        self.play(FadeIn(right_title), FadeIn(stair_lbl), run_time=0.5)
        self.play(GrowFromCenter(insight), run_time=0.4)
        self.wait(dur - 1.9)


class B09_Example(Scene):
    """Illustrative: 3000K, kBT=0.26 eV, hν=2.1 eV for 600 nm."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        temp_lbl = Text("T = 3000 K", font=MONO, color=INK, font_size=26).move_to([-3.5, 2.5, 0])

        # kBT bar
        kt_bar = Rectangle(width=1.3, height=2.6, fill_color=TEAL, fill_opacity=0.8,
                           stroke_width=0).move_to([-2.0, -1.7, 0])
        kt_val = Text("kBT = 0.26 eV", font=MONO, color=TEAL, font_size=22).move_to([-2.0, -3.2, 0])

        # hν bar (much taller)
        hnu_bar = Rectangle(width=1.3, height=5.0, fill_color=CRIMSON, fill_opacity=0.8,
                            stroke_width=0).move_to([2.0, -0.5, 0])
        hnu_val = Text("hv = 2.1 eV (600 nm)", font=MONO, color=CRIMSON, font_size=22).move_to([2.0, -3.2, 0])

        ratio_lbl = SerifLabel("hv / kBT ~ 8", accent=INK, size=22).move_to([5.0, 1.0, 0])
        conclusion = LabelChip("mode stays nearly empty", accent=TEAL, size=20).move_to([0, 3.5, 0])

        self.play(FadeIn(ill_lbl), FadeIn(temp_lbl), run_time=0.4)
        self.play(FadeIn(kt_bar), FadeIn(kt_val), run_time=0.4)
        self.play(FadeIn(hnu_bar), FadeIn(hnu_val), run_time=0.4)
        self.play(FadeIn(ratio_lbl), run_time=0.3)
        self.play(GrowFromCenter(conclusion), run_time=0.4)
        self.wait(dur - 2.1)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Classical: equal energy per mode.\nQuantum: needs one full packet.\nHigh-frequency modes stay empty.\nThe curve bends back down.",
                      font=DISPLAY, color=INK, font_size=18, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.8, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
