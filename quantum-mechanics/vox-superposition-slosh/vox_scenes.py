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
        title = Text("Why Two Frozen States\nMake a Sloshing One",
                     font=DISPLAY, color=INK, font_size=38, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        sub = Text("the beat frequency", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_TwoEigenstates(Scene):
    """n=1 (single hump) and n=2 (two humps) side by side, both still."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        x_n1 = np.linspace(-2.5, 2.5, 200)
        x_n2 = np.linspace(-2.5, 2.5, 200)

        # n=1: single hump
        n1_pts = [np.array([x - 3.5, 2.5 * np.sin(np.pi * (x + 2.5) / 5) ** 2 - 1.5, 0])
                  for x in x_n1]
        n1_curve = VMobject(color=CRIMSON, stroke_width=3)
        n1_curve.set_points_smoothly(n1_pts)
        n1_base = Line([-6.0, -1.5, 0], [-1.0, -1.5, 0], color=INK, stroke_width=2)
        n1_lbl = SerifLabel("n = 1", accent=CRIMSON, size=22).move_to([-3.5, 1.5, 0])
        n1_wall_l = Line([-6.0, -1.5, 0], [-6.0, 1.5, 0], color=INK, stroke_width=4)
        n1_wall_r = Line([-1.0, -1.5, 0], [-1.0, 1.5, 0], color=INK, stroke_width=4)
        still1 = LabelChip("frozen", accent=CRIMSON, size=18).move_to([-3.5, -2.5, 0])

        # n=2: two humps
        n2_pts = [np.array([x + 3.5, 2.5 * np.sin(2 * np.pi * (x + 2.5) / 5) ** 2 - 1.5, 0])
                  for x in x_n2]
        n2_curve = VMobject(color=CRIMSON, stroke_width=3)
        n2_curve.set_points_smoothly(n2_pts)
        n2_base = Line([1.0, -1.5, 0], [6.0, -1.5, 0], color=INK, stroke_width=2)
        n2_lbl = SerifLabel("n = 2", accent=CRIMSON, size=22).move_to([3.5, 1.5, 0])
        n2_wall_l = Line([1.0, -1.5, 0], [1.0, 1.5, 0], color=INK, stroke_width=4)
        n2_wall_r = Line([6.0, -1.5, 0], [6.0, 1.5, 0], color=INK, stroke_width=4)
        still2 = LabelChip("frozen", accent=CRIMSON, size=18).move_to([3.5, -2.5, 0])

        self.play(
            Create(n1_base), Create(n1_wall_l), Create(n1_wall_r),
            Create(n2_base), Create(n2_wall_l), Create(n2_wall_r),
            run_time=0.4
        )
        self.play(Create(n1_curve), FadeIn(n1_lbl), run_time=0.5)
        self.play(Create(n2_curve), FadeIn(n2_lbl), run_time=0.5)
        self.play(GrowFromCenter(still1), GrowFromCenter(still2), run_time=0.4)
        self.wait(dur - 2.0)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Two stationary states. Each one frozen.\nAdd them: probability sloshes wall to wall.\nHow can two still things make motion?",
                     font=DISPLAY, color=INK, font_size=18, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_TwoClocks(Scene):
    """Two complex plane clocks at different rotation rates."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: slow clock (omega_1)
        ax1_re = Line([-5.5, 0, 0], [-0.5, 0, 0], color=INK, stroke_width=1.2)
        ax1_im = Line([-3.0, -2.5, 0], [-3.0, 2.5, 0], color=INK, stroke_width=1.2)
        hand1 = Arrow(start=[-3.0, 0, 0], end=[-1.2, 1.5, 0], color=CRIMSON, stroke_width=4, buff=0)
        lbl1 = SerifLabel("omega_1 = E1/hbar", accent=CRIMSON, size=18).move_to([-3.0, -3.0, 0])
        speed1 = LabelChip("slower", accent=CRIMSON, size=18).move_to([-3.0, 3.2, 0])

        # Right: fast clock (omega_2)
        ax2_re = Line([0.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1.2)
        ax2_im = Line([3.0, -2.5, 0], [3.0, 2.5, 0], color=INK, stroke_width=1.2)
        hand2 = Arrow(start=[3.0, 0, 0], end=[4.8, 1.5, 0], color=TEAL, stroke_width=4, buff=0)
        lbl2 = SerifLabel("omega_2 = E2/hbar", accent=TEAL, size=18).move_to([3.0, -3.0, 0])
        speed2 = LabelChip("faster", accent=TEAL, size=18).move_to([3.0, 3.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(Create(ax1_re), Create(ax1_im), GrowArrow(hand1), FadeIn(lbl1), FadeIn(speed1), run_time=0.6)
        self.play(Create(ax2_re), Create(ax2_im), GrowArrow(hand2), FadeIn(lbl2), FadeIn(speed2), run_time=0.6)
        # Rotate both
        self.play(
            Rotate(hand1, angle=TAU * 1.0, about_point=[-3.0, 0, 0]),
            Rotate(hand2, angle=TAU * 1.6, about_point=[3.0, 0, 0]),
            run_time=dur * 0.5
        )
        self.wait(dur * 0.1)


class B05_AngleBetween(Scene):
    """Phase angle between two hands oscillates — this drives the sloshing."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Single axes
        ax_re = Line([-4.0, 0, 0], [4.0, 0, 0], color=INK, stroke_width=1.5)
        ax_im = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.5)

        # Two hands starting at same angle
        hand1 = Arrow(start=[0, 0, 0], end=[2.5, 0, 0], color=CRIMSON, stroke_width=3, buff=0)
        hand2 = Arrow(start=[0, 0, 0], end=[2.5, 0, 0], color=TEAL, stroke_width=3, buff=0)

        # Arc showing angle between them
        arc = Arc(radius=1.5, start_angle=0, angle=PI / 3, color=TEAL, stroke_width=2)
        delta_lbl = SerifLabel("delta phi = (omega_2 - omega_1) * t", accent=TEAL, size=18).move_to([2.5, -2.5, 0])
        beat_lbl = LabelChip("beat frequency = (E2-E1)/hbar", accent=TEAL, size=20).move_to([0, -3.5, 0])

        self.play(Create(ax_re), Create(ax_im), run_time=0.3)
        self.play(GrowArrow(hand1), GrowArrow(hand2), run_time=0.5)
        # Rotate hand2 faster to show growing angle
        self.play(
            Rotate(hand2, angle=PI / 3, about_point=ORIGIN),
            run_time=dur * 0.35
        )
        self.play(Create(arc), FadeIn(delta_lbl), run_time=0.4)
        self.play(GrowFromCenter(beat_lbl), run_time=0.3)
        self.wait(dur * 0.1)


class B06_SloshingCloud(Scene):
    """Probability cloud sloshing left-right in a box."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Box walls
        box_l = Line([-5.0, -2.0, 0], [-5.0, 2.0, 0], color=INK, stroke_width=4)
        box_r = Line([5.0, -2.0, 0], [5.0, 2.0, 0], color=INK, stroke_width=4)
        box_base = Line([-5.0, -2.0, 0], [5.0, -2.0, 0], color=INK, stroke_width=2)

        # Cloud starting left
        cloud = Ellipse(width=3.5, height=2.5, color=TEAL, fill_opacity=0.5,
                        stroke_width=2).move_to([-2.0, -0.5, 0])
        cloud_lbl = LabelChip("probability cloud", accent=TEAL, size=20).move_to([0, 2.5, 0])

        beat_lbl = SerifLabel("period = h / (E2 - E1)", accent=INK, size=18).move_to([0, -2.8, 0])

        self.play(Create(box_l), Create(box_r), Create(box_base), run_time=0.3)
        self.play(FadeIn(cloud), FadeIn(cloud_lbl), run_time=0.4)
        self.play(FadeIn(beat_lbl), run_time=0.3)
        # Slosh left-right
        self.play(cloud.animate.move_to([2.0, -0.5, 0]), run_time=dur * 0.25)
        self.play(cloud.animate.move_to([-2.0, -0.5, 0]), run_time=dur * 0.25)
        self.play(cloud.animate.move_to([2.0, -0.5, 0]), run_time=dur * 0.2)
        self.wait(dur * 0.05)


class B07_EnergyStillFixed(Scene):
    """Energy levels E1 and E2 — expectation value sits between them."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Energy axis
        ax_e = Arrow(start=[-5.5, -3.0, 0], end=[-5.5, 3.0, 0], color=INK, stroke_width=2, buff=0)
        e_lbl = SerifLabel("E", accent=INK, size=22).move_to([-5.5, 3.4, 0])

        # E1 level
        e1_line = Line([-5.0, -1.5, 0], [5.0, -1.5, 0], color=CRIMSON, stroke_width=2.5)
        e1_lbl = SerifLabel("E1 (ground state)", accent=CRIMSON, size=20).move_to([2.0, -1.9, 0])

        # E2 level
        e2_line = Line([-5.0, 1.5, 0], [5.0, 1.5, 0], color=CRIMSON, stroke_width=2.5)
        e2_lbl = SerifLabel("E2 (first excited)", accent=CRIMSON, size=20).move_to([2.0, 1.9, 0])

        # Expectation value (between E1 and E2)
        exp_line = Line([-5.0, 0, 0], [5.0, 0, 0], color=TEAL, stroke_width=2, stroke_opacity=0.7)
        exp_dot = Dot(color=TEAL, radius=0.18).move_to([-5.0, 0, 0])
        exp_lbl = LabelChip("<E> stays constant", accent=TEAL, size=20).move_to([2.0, 0.6, 0])

        note = SerifLabel("the sloshing is in position, not energy", accent=INK, size=20).move_to([0, -2.8, 0])

        self.play(GrowArrow(ax_e), FadeIn(e_lbl), run_time=0.4)
        self.play(Create(e1_line), FadeIn(e1_lbl), run_time=0.4)
        self.play(Create(e2_line), FadeIn(e2_lbl), run_time=0.4)
        self.play(Create(exp_line), FadeIn(exp_dot), GrowFromCenter(exp_lbl), run_time=0.5)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(dur - 2.2)


class B08_BeatAnalogy(Scene):
    """Two sine waves close in frequency and their beat-note sum."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        x_vals = np.linspace(-6.5, 6.5, 500)
        f1 = 3.0
        f2 = 3.5

        # Wave 1
        w1_pts = [np.array([x, 0.8 * np.sin(f1 * x) + 2.0, 0]) for x in x_vals]
        wave1 = VMobject(color=CRIMSON, stroke_width=2)
        wave1.set_points_smoothly(w1_pts)
        lbl1 = SerifLabel("tone 1 (omega_1)", accent=CRIMSON, size=18).move_to([-5.0, 3.0, 0])

        # Wave 2
        w2_pts = [np.array([x, 0.8 * np.sin(f2 * x) + 0.5, 0]) for x in x_vals]
        wave2 = VMobject(color=TEAL, stroke_width=2)
        wave2.set_points_smoothly(w2_pts)
        lbl2 = SerifLabel("tone 2 (omega_2)", accent=TEAL, size=18).move_to([-5.0, 1.5, 0])

        # Beat envelope (sum)
        beat_pts = [np.array([x, (np.sin(f1 * x) + np.sin(f2 * x)) * 0.8 - 2.0, 0]) for x in x_vals]
        beat_wave = VMobject(color=INK, stroke_width=2.5)
        beat_wave.set_points_smoothly(beat_pts)
        beat_lbl = SerifLabel("sum: beat envelope", accent=INK, size=18).move_to([-5.0, -1.2, 0])

        analogy_lbl = LabelChip("beat frequency = (E2-E1)/hbar in QM", accent=TEAL, size=18).move_to([0, -3.5, 0])

        self.play(Create(wave1), FadeIn(lbl1), run_time=0.5)
        self.play(Create(wave2), FadeIn(lbl2), run_time=0.5)
        self.play(Create(beat_wave), FadeIn(beat_lbl), run_time=0.5)
        self.play(GrowFromCenter(analogy_lbl), run_time=0.4)
        self.wait(dur - 2.1)


class B09_Example(Scene):
    """Illustrative: hydrogen n=1 to n=2, Bohr frequency ~2.5e15 Hz."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        e1 = Text("E1 = -13.6 eV (n=1)", font=MONO, color=CRIMSON, font_size=24).move_to([0, 2.5, 0])
        e2 = Text("E2 = -3.4 eV (n=2)", font=MONO, color=CRIMSON, font_size=24).move_to([0, 1.8, 0])
        arrow = Arrow(start=[0, 1.2, 0], end=[0, 0.3, 0], color=INK, stroke_width=2.5, buff=0.1)
        delta_e = Text("delta E = 10.2 eV", font=MONO, color=TEAL, font_size=26).move_to([0, -0.2, 0])
        arrow2 = Arrow(start=[0, -0.7, 0], end=[0, -1.6, 0], color=INK, stroke_width=2.5, buff=0.1)
        freq = Text("f = 2.46 x 10^15 Hz", font=MONO, color=TEAL, font_size=28).move_to([0, -2.2, 0])
        compare = Text("~ ultraviolet light frequency",
                       font=SERIF, color=INK, font_size=20, slant=ITALIC).move_to([0, -3.1, 0])

        self.play(FadeIn(ill_lbl), FadeIn(e1), FadeIn(e2), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.play(FadeIn(delta_e), run_time=0.3)
        self.play(GrowArrow(arrow2), run_time=0.3)
        self.play(FadeIn(freq), run_time=0.4)
        self.play(FadeIn(compare), run_time=0.3)
        self.wait(dur - 2.3)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Each eigenstate frozen.\nPhases drift apart.\nDifference in rates = the beat.\nThe beat makes probability slosh.",
                      font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
