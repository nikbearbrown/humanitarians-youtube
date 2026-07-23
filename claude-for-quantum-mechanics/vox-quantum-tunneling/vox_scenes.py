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
        title = Text("Why a Particle Can Walk\nThrough a Wall",
                     font=DISPLAY, color=INK, font_size=40, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B02_ClassicalBounce(Scene):
    """Classical ball bouncing off barrier it can't climb."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Ground
        ground = Line([-6.0, -2.5, 0], [6.0, -2.5, 0], color=INK, stroke_width=2)
        # Barrier (rectangular)
        barrier = Rectangle(width=1.5, height=3.0, color=CRIMSON,
                            fill_color=CRIMSON, fill_opacity=0.3, stroke_width=2.5)
        barrier.move_to([1.0, -1.0, 0])
        barrier_lbl = SerifLabel("barrier", accent=CRIMSON, size=22).move_to([1.0, 1.0, 0])

        # Ball (SLATE = classical)
        ball = Dot(color=SLATE, radius=0.2).move_to([-4.0, -2.2, 0])
        # Energy label
        e_lbl = Text("E < V0", font=MONO, color=INK, font_size=24).move_to([-4.0, -3.2, 0])

        self.play(Create(ground), FadeIn(barrier), FadeIn(barrier_lbl), run_time=0.5)
        self.play(FadeIn(ball), FadeIn(e_lbl), run_time=0.3)
        # Ball moves right, hits barrier, bounces back
        self.play(ball.animate.move_to([-0.2, -2.2, 0]), run_time=dur * 0.35, rate_func=linear)
        self.play(ball.animate.move_to([-4.0, -2.2, 0]), run_time=dur * 0.35, rate_func=linear)
        self.wait(dur * 0.1)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Classical predicts total reflection\nwhen E < V. Some fraction\ntransmits anyway. Why?",
                     font=DISPLAY, color=INK, font_size=26, line_spacing=1.3).move_to([0, 0.4, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_ExponentialDecay(Scene):
    """Wavefunction decaying exponentially inside barrier."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        x_vals = np.linspace(-5.0, 5.0, 300)
        x_barrier_start = 0.0
        x_barrier_end = 3.5
        kappa = 1.0

        # Barrier region
        barrier_box = Rectangle(width=3.5, height=5.0, color=CRIMSON,
                                fill_color=CRIMSON, fill_opacity=0.15, stroke_width=2)
        barrier_box.move_to([1.75, 0, 0])

        # Incoming wave (left of barrier)
        inc_pts = [np.array([x, 1.5 * np.sin(3 * x + 1), 0]) for x in np.linspace(-5.0, 0.0, 150)]
        inc_wave = VMobject(color=TEAL, stroke_width=2.5)
        inc_wave.set_points_smoothly(inc_pts)

        # Decaying exponential inside barrier
        dec_pts = [np.array([x, 1.5 * np.exp(-kappa * x), 0])
                   for x in np.linspace(0.0, x_barrier_end, 100)]
        dec_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        dec_wave.set_points_smoothly(dec_pts)

        lbl_in = SerifLabel("incoming wave", accent=TEAL, size=22).move_to([-3.0, 2.5, 0])
        lbl_dec = SerifLabel("decaying inside barrier", accent=CRIMSON, size=22).move_to([1.75, -2.5, 0])

        self.play(FadeIn(barrier_box), run_time=0.4)
        self.play(Create(inc_wave), run_time=0.5)
        self.play(Create(dec_wave), FadeIn(lbl_in), FadeIn(lbl_dec), run_time=dur * 0.5)
        self.wait(dur * 0.2)


class B05_TailEmerges(Scene):
    """Thin barrier: decaying exponential reaches far side and launches transmitted wave."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        x_vals = np.linspace(-5.5, 5.5, 400)
        L = 2.0
        kappa = 0.9

        # Thin barrier region
        barrier_box = Rectangle(width=L, height=5.0, color=CRIMSON,
                                fill_color=CRIMSON, fill_opacity=0.15, stroke_width=2)
        barrier_box.move_to([L / 2, 0, 0])

        # Incoming
        inc_pts = [np.array([x, 1.5 * np.sin(3 * x + 1), 0]) for x in np.linspace(-5.0, 0.0, 150)]
        inc_wave = VMobject(color=TEAL, stroke_width=2.5)
        inc_wave.set_points_smoothly(inc_pts)

        # Decay inside
        val_at_end = 1.5 * np.exp(-kappa * L)
        dec_pts = [np.array([x, 1.5 * np.exp(-kappa * x), 0]) for x in np.linspace(0.0, L, 80)]
        dec_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        dec_wave.set_points_smoothly(dec_pts)

        # Transmitted wave (right of barrier)
        trans_pts = [np.array([x, val_at_end * np.sin(3 * (x - L)), 0])
                     for x in np.linspace(L, 5.0, 150)]
        trans_wave = VMobject(color=TEAL, stroke_width=2, stroke_opacity=0.8)
        trans_wave.set_points_smoothly(trans_pts)

        lbl_trans = LabelChip("transmitted", accent=TEAL, size=20).move_to([3.8, 2.0, 0])
        lbl_small = SerifLabel("smaller amplitude", accent=TEAL, size=20).move_to([3.8, 1.4, 0])

        self.play(FadeIn(barrier_box), run_time=0.3)
        self.play(Create(inc_wave), Create(dec_wave), run_time=0.6)
        self.play(Create(trans_wave), FadeIn(lbl_trans), FadeIn(lbl_small), run_time=dur * 0.5)
        self.wait(dur * 0.2)


class B06_TransmissionVsWidth(Scene):
    """T vs barrier width L: exponential fall-off. CRIMSON curve dropping steeply."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Axes
        ax_x = Line([-5.0, -2.5, 0], [5.0, -2.5, 0], color=INK, stroke_width=2.5)
        ax_y = Line([-5.0, -2.5, 0], [-5.0, 2.8, 0], color=INK, stroke_width=2.5)
        x_lbl = SerifLabel("barrier width L", accent=INK, size=22).move_to([0, -3.3, 0])
        y_lbl = SerifLabel("transmission T", accent=INK, size=22).move_to([-6.0, 0.0, 0])

        # Curve: T ~ e^(-2*kappa*L), normalized so L=0 -> T~1
        L_vals = np.linspace(0, 10, 200)
        kappa = 1.0
        x_scale = 0.9
        y_scale = 3.5
        pts = []
        for Lv in L_vals:
            xc = -5.0 + Lv * x_scale
            yc = -2.5 + np.exp(-2 * kappa * Lv) * y_scale
            if -5.0 <= xc <= 5.0:
                pts.append(np.array([xc, yc, 0]))

        curve = VMobject(color=CRIMSON, stroke_width=3)
        curve.set_points_smoothly(pts)

        formula_lbl = Text("T ~ e^(-2kL)", font=MONO, color=CRIMSON, font_size=26).move_to([2.0, 1.5, 0])

        self.play(Create(ax_x), Create(ax_y), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(curve), run_time=dur * 0.5)
        self.play(FadeIn(formula_lbl, scale=1.1), run_time=0.4)
        self.wait(dur * 0.2)


class B07_SameEnergy(Scene):
    """Before and after barrier: particle energy arrows same height."""
    def construct(self):
        dur = DUR.get("B07", 9.0)
        # Barrier
        barrier = Rectangle(width=2.0, height=4.0, color=CRIMSON,
                            fill_color=CRIMSON, fill_opacity=0.2, stroke_width=2.5)
        barrier.move_to([0, 0, 0])
        barrier_lbl = SerifLabel("barrier V0", accent=CRIMSON, size=22).move_to([0, 2.5, 0])

        # Energy arrows (same height on both sides)
        e_before = Arrow(start=[-4.5, -1.5, 0], end=[-4.5, 0.3, 0],
                         color=TEAL, stroke_width=4, buff=0)
        e_after = Arrow(start=[4.5, -1.5, 0], end=[4.5, 0.3, 0],
                        color=TEAL, stroke_width=4, buff=0)
        lbl_before = Text("E", font=MONO, color=TEAL, font_size=28).move_to([-4.5, 0.8, 0])
        lbl_after = Text("E", font=MONO, color=TEAL, font_size=28).move_to([4.5, 0.8, 0])
        equal_lbl = SerifLabel("same energy", accent=TEAL, size=22).move_to([0, -2.8, 0])

        self.play(FadeIn(barrier), FadeIn(barrier_lbl), run_time=0.4)
        self.play(GrowArrow(e_before), GrowArrow(e_after), run_time=0.7)
        self.play(FadeIn(lbl_before), FadeIn(lbl_after), run_time=0.3)
        self.play(FadeIn(equal_lbl, shift=UP * 0.2), run_time=0.4)
        self.wait(dur - 1.8)


class B08_RealWorld(Scene):
    """Three application chips: alpha decay, STM, solar fusion."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        chip1 = LabelChip("ALPHA DECAY", accent=TEAL, size=24).move_to([-3.5, 1.0, 0])
        chip2 = LabelChip("STM IMAGING", accent=TEAL, size=24).move_to([0, 1.0, 0])
        chip3 = LabelChip("SOLAR FUSION", accent=TEAL, size=24).move_to([3.5, 1.0, 0])

        desc1 = Text("nuclear alpha\ndecay", font=SERIF,
                     color=INK, font_size=18, slant=ITALIC).move_to([-3.5, -0.5, 0])
        desc2 = Text("atomic\nimaging", font=SERIF,
                     color=INK, font_size=18, slant=ITALIC).move_to([0, -0.5, 0])
        desc3 = Text("solar\nfusion", font=SERIF,
                     color=INK, font_size=18, slant=ITALIC).move_to([3.5, -0.5, 0])

        self.play(GrowFromCenter(chip1), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)
        self.play(GrowFromCenter(chip3), run_time=0.4)
        self.play(FadeIn(desc1), FadeIn(desc2), FadeIn(desc3), run_time=0.6)
        self.wait(dur - 1.8)


class B09_Example(Scene):
    """Illustrative: 1 eV electron, 5 eV barrier, 5 A wide -> T ~ 10^-4."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([5.0, 3.3, 0])

        # Setup text
        params = Text("E = 1 eV    V0 = 5 eV    L = 5 A", font=MONO, color=INK, font_size=24).move_to([0, 2.0, 0])

        # Barrier diagram
        barrier = Rectangle(width=2.5, height=3.0, color=CRIMSON,
                            fill_color=CRIMSON, fill_opacity=0.2, stroke_width=2.5)
        barrier.move_to([0, -0.5, 0])
        v0_lbl = Text("5 eV", font=MONO, color=CRIMSON, font_size=22).move_to([0, 1.2, 0])
        e_line = Line([-4.0, -1.5, 0], [4.0, -1.5, 0], color=TEAL, stroke_width=2.5)
        e_lbl = Text("E = 1 eV", font=MONO, color=TEAL, font_size=20).move_to([5.0, -1.5, 0])

        # Result
        result_lbl = LabelChip("T ~ 1 in 10,000", accent=TEAL, size=24).move_to([0, -3.0, 0])

        self.play(FadeIn(ill_lbl), FadeIn(params), run_time=0.5)
        self.play(FadeIn(barrier), FadeIn(v0_lbl), Create(e_line), FadeIn(e_lbl), run_time=0.7)
        self.play(GrowFromCenter(result_lbl), run_time=0.5)
        self.wait(dur - 1.7)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Exponentials never reach zero.\nThe leak is the tunnel.",
                      font=DISPLAY, color=INK, font_size=34, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.2, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
