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
        title = Text("Why a Barrier Can\nSuddenly Turn Invisible",
                     font=DISPLAY, color=INK, font_size=38, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        sub = Text("the Ramsauer resonance", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_NormalBarrier(Scene):
    """Normal barrier: partial transmission and partial reflection."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Barrier block
        barrier = Rectangle(width=1.5, height=4.5, fill_color=INK, fill_opacity=0.25,
                             stroke_color=INK, stroke_width=2.5).move_to([0, 0, 0])
        bar_lbl = SerifLabel("barrier", accent=INK, size=20).move_to([0, -2.7, 0])

        # Incoming arrow
        inc = Arrow(start=[-5.5, 0.8, 0], end=[-1.0, 0.8, 0], color=TEAL, stroke_width=3, buff=0.1)
        inc_lbl = SerifLabel("incoming", accent=TEAL, size=18).move_to([-4.0, 1.4, 0])

        # Transmitted arrow (smaller)
        trans = Arrow(start=[1.0, 0.8, 0], end=[4.5, 0.8, 0], color=TEAL, stroke_width=2, buff=0.1)
        trans_lbl = LabelChip("T < 100%", accent=TEAL, size=18).move_to([3.5, 1.5, 0])

        # Reflected arrow
        refl = Arrow(start=[-1.5, -0.5, 0], end=[-5.0, -0.5, 0], color=CRIMSON, stroke_width=2, buff=0.1)
        refl_lbl = LabelChip("R > 0", accent=CRIMSON, size=18).move_to([-3.5, -1.2, 0])

        self.play(FadeIn(barrier), FadeIn(bar_lbl), run_time=0.4)
        self.play(GrowArrow(inc), FadeIn(inc_lbl), run_time=0.5)
        self.play(GrowArrow(trans), GrowFromCenter(trans_lbl), run_time=0.4)
        self.play(GrowArrow(refl), GrowFromCenter(refl_lbl), run_time=0.4)
        self.wait(dur - 1.9)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Normal barrier: always some reflection.\nAt one special energy: zero reflection.\nHow does a solid barrier turn invisible?",
                     font=DISPLAY, color=INK, font_size=18, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_InsideBarrier(Scene):
    """Wave shorter inside barrier due to higher kinetic energy."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        x_left = np.linspace(-6.0, -1.0, 150)
        x_inside = np.linspace(-1.0, 1.0, 100)
        x_right = np.linspace(1.0, 6.0, 150)
        k_out = 1.5
        k_in = 3.5  # shorter wavelength inside

        left_pts = [np.array([x, 1.5 * np.sin(k_out * x * 2), 0]) for x in x_left]
        inside_pts = [np.array([x, 1.5 * np.sin(k_in * x * 2), 0]) for x in x_inside]
        right_pts = [np.array([x, 1.5 * np.sin(k_out * x * 2), 0]) for x in x_right]

        left_wave = VMobject(color=TEAL, stroke_width=3)
        left_wave.set_points_smoothly(left_pts)
        inside_wave = VMobject(color=TEAL, stroke_width=3, stroke_opacity=0.9)
        inside_wave.set_points_smoothly(inside_pts)
        right_wave = VMobject(color=TEAL, stroke_width=3)
        right_wave.set_points_smoothly(right_pts)

        barrier = Rectangle(width=2.0, height=4.5, fill_color=INK, fill_opacity=0.12,
                             stroke_color=INK, stroke_width=2).move_to([0, 0, 0])

        lbl_out = SerifLabel("long lambda outside", accent=INK, size=18).move_to([-4.0, -2.5, 0])
        lbl_in = SerifLabel("short lambda inside\n(higher KE)", accent=TEAL, size=18).move_to([0, -2.8, 0])

        self.play(FadeIn(barrier), run_time=0.3)
        self.play(Create(left_wave), Create(inside_wave), Create(right_wave), run_time=0.7)
        self.play(FadeIn(lbl_out), FadeIn(lbl_in), run_time=0.4)
        self.wait(dur - 1.6)


class B05_TwoReflections(Scene):
    """Barrier showing front-wall and back-wall reflections."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        barrier = Rectangle(width=2.5, height=5.0, fill_color=INK, fill_opacity=0.15,
                             stroke_color=INK, stroke_width=2.5).move_to([0, 0, 0])

        # Incoming
        inc = Arrow(start=[-5.5, 1.0, 0], end=[-1.5, 1.0, 0], color=TEAL, stroke_width=3, buff=0.1)

        # Front wall reflection
        refl1 = Arrow(start=[-1.5, 0.0, 0], end=[-5.0, 0.0, 0], color=CRIMSON, stroke_width=2.5, buff=0.1)
        r1_lbl = SerifLabel("front wall reflects", accent=CRIMSON, size=18).move_to([-3.5, 0.6, 0])

        # Back wall reflection (exits left via inside bounce)
        refl2 = Arrow(start=[1.5, -1.0, 0], end=[-5.5, -1.0, 0], color=CRIMSON, stroke_width=1.5,
                      stroke_opacity=0.8, buff=0.1)
        r2_lbl = SerifLabel("back wall reflects back", accent=CRIMSON, size=18).move_to([-2.5, -1.7, 0])

        question_lbl = LabelChip("do these two cancel?", accent=TEAL, size=20).move_to([3.5, 0.0, 0])

        self.play(FadeIn(barrier), run_time=0.3)
        self.play(GrowArrow(inc), run_time=0.4)
        self.play(GrowArrow(refl1), FadeIn(r1_lbl), run_time=0.5)
        self.play(GrowArrow(refl2), FadeIn(r2_lbl), run_time=0.5)
        self.play(GrowFromCenter(question_lbl), run_time=0.4)
        self.wait(dur - 2.3)


class B06_CancellationCondition(Scene):
    """Two reflected waves out of phase — destructive interference."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        x_vals = np.linspace(-5.5, 5.5, 400)

        # Wave 1 (front wall reflection)
        w1_pts = [np.array([x, 1.5 * np.sin(3 * x), 0]) for x in x_vals]
        wave1 = VMobject(color=CRIMSON, stroke_width=2.5)
        wave1.set_points_smoothly(w1_pts)
        lbl1 = SerifLabel("front wall: wave 1", accent=CRIMSON, size=18).move_to([-3.0, 3.0, 0])

        # Wave 2 (back wall, phase-shifted by pi = exactly out of phase)
        w2_pts = [np.array([x, 1.5 * np.sin(3 * x + np.pi), 0]) for x in x_vals]
        wave2 = VMobject(color=CRIMSON, stroke_width=2.5, stroke_opacity=0.6)
        wave2.set_points_smoothly(w2_pts)
        lbl2 = SerifLabel("back wall: wave 2", accent=CRIMSON, size=18).move_to([3.0, -3.0, 0])

        # Sum = zero
        sum_line = Line([-5.5, -0.3, 0], [5.5, -0.3, 0], color=TEAL, stroke_width=3)
        sum_lbl = LabelChip("sum = zero: no reflection", accent=TEAL, size=22).move_to([0, -3.8, 0])

        condition_lbl = SerifLabel("condition: L = n * lambda/2 inside", accent=INK, size=20).move_to([0, 3.5, 0])

        self.play(Create(wave1), FadeIn(lbl1), run_time=0.5)
        self.play(Create(wave2), FadeIn(lbl2), run_time=0.5)
        self.play(Create(sum_line), run_time=0.4)
        self.play(GrowFromCenter(sum_lbl), run_time=0.4)
        self.play(FadeIn(condition_lbl), run_time=0.4)
        self.wait(dur - 2.4)


class B07_ARCoatingAnalogy(Scene):
    """Side-by-side: optical thin film / quantum barrier."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: optical AR coating
        left_title = SerifLabel("anti-reflection coating", accent=INK, size=20).move_to([-3.5, 3.2, 0])
        film = Rectangle(width=0.5, height=5.0, fill_color=TEAL, fill_opacity=0.3,
                         stroke_color=TEAL, stroke_width=2).move_to([-3.5, 0, 0])
        film_lbl = SerifLabel("thin film", accent=TEAL, size=16).move_to([-3.5, -2.8, 0])
        light_in = Arrow(start=[-6.2, 0.8, 0], end=[-4.0, 0.8, 0], color=TEAL, stroke_width=2.5, buff=0)
        light_thru = Arrow(start=[-3.0, 0.8, 0], end=[-0.5, 0.8, 0], color=TEAL, stroke_width=2.5, buff=0)

        # Right: quantum barrier
        right_title = SerifLabel("quantum barrier", accent=TEAL, size=20).move_to([3.5, 3.2, 0])
        q_bar = Rectangle(width=1.0, height=5.0, fill_color=INK, fill_opacity=0.2,
                          stroke_color=INK, stroke_width=2).move_to([3.5, 0, 0])
        q_bar_lbl = SerifLabel("potential well", accent=INK, size=16).move_to([3.5, -2.8, 0])
        q_in = Arrow(start=[0.5, 0.8, 0], end=[3.0, 0.8, 0], color=TEAL, stroke_width=2.5, buff=0)
        q_thru = Arrow(start=[4.0, 0.8, 0], end=[6.3, 0.8, 0], color=TEAL, stroke_width=2.5, buff=0)

        same_lbl = LabelChip("same physics", accent=TEAL, size=22).move_to([0, -3.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(
            FadeIn(left_title), FadeIn(film), FadeIn(film_lbl),
            GrowArrow(light_in), GrowArrow(light_thru),
            run_time=0.7
        )
        self.play(
            FadeIn(right_title), FadeIn(q_bar), FadeIn(q_bar_lbl),
            GrowArrow(q_in), GrowArrow(q_thru),
            run_time=0.7
        )
        self.play(GrowFromCenter(same_lbl), run_time=0.4)
        self.wait(dur - 2.2)


class B08_ResonanceCondition(Scene):
    """Formula 2*k2*L = n*pi and T vs energy bar chart."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        formula = Text("2 * k2 * L = n * pi",
                       font=MONO, color=TEAL, font_size=36).move_to([0, 2.5, 0])
        formula_lbl = SerifLabel("resonance condition (n = 1, 2, 3, ...)", accent=INK, size=20).move_to([0, 1.5, 0])

        # T vs energy bar chart — peaks at resonances
        energies = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
        heights = [0.3, 0.15, 2.2, 0.2, 0.1, 2.0, 0.15]  # resonance peaks at ~2.5 and ~5.5
        colors = [CRIMSON if h < 1.0 else TEAL for h in heights]

        ax_x = Line([-4.5, -1.2, 0], [4.5, -1.2, 0], color=INK, stroke_width=1.5)
        ax_y = Line([-4.5, -1.2, 0], [-4.5, 1.5, 0], color=INK, stroke_width=1.5)
        x_lbl = SerifLabel("energy", accent=INK, size=18).move_to([4.5, -1.6, 0])
        y_lbl = SerifLabel("T", accent=TEAL, size=18).move_to([-4.9, 1.2, 0])
        t1_lbl = LabelChip("T=1", accent=TEAL, size=16).move_to([-4.0, 1.2, 0])

        bars = VGroup()
        for i, (e, h, c) in enumerate(zip(energies, heights, colors)):
            x_pos = -3.5 + i * 1.1
            bar = Rectangle(width=0.7, height=min(h, 2.2),
                            fill_color=c, fill_opacity=0.8, stroke_width=0).move_to(
                [x_pos, -1.2 + min(h, 2.2) / 2, 0])
            bars.add(bar)

        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(formula_lbl), run_time=0.3)
        self.play(Create(ax_x), Create(ax_y), FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(t1_lbl), run_time=0.4)
        self.play(Create(bars), run_time=dur * 0.5)
        self.wait(dur * 0.1)


class B09_Example(Scene):
    """Illustrative: 0.3 nm barrier, 5 eV depth, resonance ~3 eV."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        params = VGroup(
            Text("barrier width L = 0.3 nm", font=MONO, color=INK, font_size=24).move_to([0, 2.5, 0]),
            Text("well depth V0 = 5 eV", font=MONO, color=INK, font_size=24).move_to([0, 1.8, 0]),
        )
        arrow = Arrow(start=[0, 1.2, 0], end=[0, 0.3, 0], color=INK, stroke_width=2.5, buff=0.1)
        result = Text("first resonance ~ 3 eV", font=MONO, color=TEAL, font_size=30).move_to([0, -0.2, 0])
        condition = Text("L = 1/2 * lambda_inside", font=MONO, color=TEAL, font_size=24).move_to([0, -1.0, 0])
        outcome = LabelChip("T = 1: zero reflection", accent=TEAL, size=22).move_to([0, -2.0, 0])

        self.play(FadeIn(ill_lbl), FadeIn(params), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.play(FadeIn(result), run_time=0.4)
        self.play(FadeIn(condition), run_time=0.3)
        self.play(GrowFromCenter(outcome), run_time=0.4)
        self.wait(dur - 2.1)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("The barrier fights itself.\nReflections from both walls cancel.\nAt the right energy: everything through.",
                      font=DISPLAY, color=INK, font_size=22, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.2, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
