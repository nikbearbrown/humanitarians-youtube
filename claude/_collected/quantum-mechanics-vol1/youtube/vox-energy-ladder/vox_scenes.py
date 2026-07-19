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
        title = Text("Why the Energy Ladder\nClimbs in Equal Steps",
                     font=DISPLAY, color=INK, font_size=36, line_spacing=1.3).move_to([0, 0.5, 0])
        sub = Text("the quantum harmonic oscillator",
                   font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([0, -0.8, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_ClassicalVsQuantum(Scene):
    """Left: classical continuous energy; Right: quantum discrete rungs."""
    def construct(self):
        dur = DUR.get("B02", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: classical — shaded continuous band
        left_title = SerifLabel("classical: any energy", accent=CRIMSON, size=20).move_to([-3.5, 3.2, 0])
        band = Rectangle(width=3.0, height=5.5, fill_color=CRIMSON, fill_opacity=0.18,
                         stroke_color=CRIMSON, stroke_width=1.5).move_to([-3.5, -0.2, 0])
        arrow_l = Arrow(start=[-3.5, -3.0, 0], end=[-3.5, 2.8, 0],
                        color=CRIMSON, stroke_width=2, buff=0)
        e_lbl_l = SerifLabel("E", accent=CRIMSON, size=20).move_to([-5.5, 2.8, 0])

        # Right: quantum — discrete rungs
        right_title = SerifLabel("quantum: discrete rungs", accent=TEAL, size=20).move_to([3.5, 3.2, 0])
        rung_ys = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
        rungs = VGroup(*[
            Line([1.5, y, 0], [5.5, y, 0], color=TEAL, stroke_width=2.5)
            for y in rung_ys
        ])
        arrow_r = Arrow(start=[0.3, -3.0, 0], end=[0.3, 2.8, 0],
                        color=INK, stroke_width=2, buff=0)
        e_lbl_r = SerifLabel("E", accent=INK, size=20).move_to([0.0, 3.0, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(GrowArrow(arrow_l), FadeIn(left_title), run_time=0.4)
        self.play(FadeIn(band), run_time=0.4)
        self.play(FadeIn(e_lbl_l), run_time=0.2)
        self.play(GrowArrow(arrow_r), FadeIn(right_title), run_time=0.4)
        self.play(Create(rungs), run_time=0.6)
        self.play(FadeIn(e_lbl_r), run_time=0.2)
        self.wait(dur - 2.6)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Any smooth trap looks like a parabola near its bottom.\nEnergy is restricted to discrete rungs.\nHow does a smooth curve force a staircase?",
                     font=DISPLAY, color=INK, font_size=16, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_LadderOperators(Scene):
    """Ladder diagram with a+ raising and a- lowering by hbar*omega each."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Draw three rungs one at a time
        rung_ys = [-1.5, 0.0, 1.5]
        rung_labels = ["n", "n+1", "n+2"]

        rung0 = Line([-2.5, -1.5, 0], [2.5, -1.5, 0], color=TEAL, stroke_width=2.5)
        lbl0 = SerifLabel("n", accent=TEAL, size=18).move_to([-3.3, -1.5, 0])
        rung1 = Line([-2.5, 0.0, 0], [2.5, 0.0, 0], color=TEAL, stroke_width=2.5)
        lbl1 = SerifLabel("n+1", accent=TEAL, size=18).move_to([-3.3, 0.0, 0])
        rung2 = Line([-2.5, 1.5, 0], [2.5, 1.5, 0], color=TEAL, stroke_width=2.5)
        lbl2 = SerifLabel("n+2", accent=TEAL, size=18).move_to([-3.3, 1.5, 0])

        # Spacing labels
        sp1 = SerifLabel("hbar*omega", accent=INK, size=18).move_to([3.5, -0.75, 0])
        sp2 = SerifLabel("hbar*omega", accent=INK, size=18).move_to([3.5, 0.75, 0])
        tick1 = Line([2.8, -1.5, 0], [2.8, 0.0, 0], color=INK, stroke_width=1.2)
        tick2 = Line([2.8, 0.0, 0], [2.8, 1.5, 0], color=INK, stroke_width=1.2)

        # Raising arrow
        a_up = Arrow(start=[-1.5, -1.5, 0], end=[-1.5, 1.5, 0],
                     color=TEAL, stroke_width=2.5, buff=0.1)
        a_up_lbl = SerifLabel("a+  raises", accent=TEAL, size=18).move_to([-4.8, 0.0, 0])

        # Lowering arrow
        a_dn = Arrow(start=[1.5, 1.5, 0], end=[1.5, -1.5, 0],
                     color=CRIMSON, stroke_width=2.5, buff=0.1)
        a_dn_lbl = SerifLabel("a-  lowers", accent=CRIMSON, size=18).move_to([4.8, 0.0, 0])

        self.play(Create(rung0), FadeIn(lbl0), run_time=0.3)
        self.play(Create(rung1), FadeIn(lbl1), run_time=0.3)
        self.play(Create(rung2), FadeIn(lbl2), run_time=0.3)
        self.play(Create(tick1), FadeIn(sp1), run_time=0.3)
        self.play(Create(tick2), FadeIn(sp2), run_time=0.3)
        self.play(GrowArrow(a_up), FadeIn(a_up_lbl), run_time=0.5)
        self.play(GrowArrow(a_dn), FadeIn(a_dn_lbl), run_time=0.5)
        self.wait(dur - 2.7)


class B05_GroundState(Scene):
    """Bottom rung; a- hits the floor — ladder must have a bottom."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Higher rungs faded in first
        r1 = Line([-2.5, 0.0, 0], [2.5, 0.0, 0], color=TEAL, stroke_width=1.5)
        r2 = Line([-2.5, 1.5, 0], [2.5, 1.5, 0], color=TEAL, stroke_width=1.5)
        r3 = Line([-2.5, 3.0, 0], [2.5, 3.0, 0], color=TEAL, stroke_width=1.5)
        for r in [r1, r2, r3]:
            r.set_opacity(0.3)

        # Floor
        floor = Line([-5.5, -3.0, 0], [5.5, -3.0, 0], color=INK, stroke_width=2.5)
        floor_lbl = SerifLabel("no lower rung possible", accent=INK, size=18).move_to([0, -3.5, 0])

        # Ground rung
        g_rung = Line([-2.5, -1.5, 0], [2.5, -1.5, 0], color=TEAL, stroke_width=3.0)
        g_lbl = SerifLabel("n = 0  (ground state)", accent=TEAL, size=20).move_to([0, -0.9, 0])

        # a- arrow pointing down hits floor
        a_dn = Arrow(start=[0.0, -1.5, 0], end=[0.0, -3.0, 0],
                     color=CRIMSON, stroke_width=2.5, buff=0.05)
        a_lbl = SerifLabel("a- |0> = 0", accent=CRIMSON, size=20).move_to([2.8, -2.2, 0])

        self.play(FadeIn(r1), FadeIn(r2), FadeIn(r3), run_time=0.3)
        self.play(Create(floor), run_time=0.3)
        self.play(FadeIn(floor_lbl), run_time=0.3)
        self.play(Create(g_rung), run_time=0.3)
        self.play(FadeIn(g_lbl), run_time=0.3)
        self.play(GrowArrow(a_dn), run_time=0.4)
        self.play(FadeIn(a_lbl), run_time=0.3)
        self.wait(dur - 2.4)


class B06_ZeroPoint(Scene):
    """Parabola with classical zero vs quantum E_0 = hbar*omega/2."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Parabola
        x_vals = np.linspace(-4.0, 4.0, 200)
        pts = [np.array([x, 0.3 * x**2 - 3.0, 0]) for x in x_vals]
        parabola = VMobject(color=INK, stroke_width=2.0)
        parabola.set_points_smoothly(pts)

        # Classical minimum at bottom
        class_line = DashedLine([-4.5, -3.0, 0], [4.5, -3.0, 0],
                                 color=CRIMSON, stroke_width=2.0, dash_length=0.15)
        class_lbl = SerifLabel("classical min  E = 0", accent=CRIMSON, size=20).move_to([0, -3.5, 0])

        # Quantum ground state
        quantum_line = Line([-4.5, -2.1, 0], [4.5, -2.1, 0], color=TEAL, stroke_width=2.5)
        quantum_lbl = SerifLabel("E_0 = hbar*omega / 2", accent=TEAL, size=20).move_to([0, -1.5, 0])

        # Bracket between lines
        brace_start = [-5.0, -3.0, 0]
        brace_end = [-5.0, -2.1, 0]
        brace = DoubleArrow(start=brace_start, end=brace_end,
                            color=TEAL, stroke_width=2.0, buff=0)
        zpe_lbl = SerifLabel("zero-point energy", accent=TEAL, size=18).move_to([-3.5, -2.55, 0])

        self.play(Create(parabola), run_time=0.4)
        self.play(Create(class_line), run_time=0.3)
        self.play(FadeIn(class_lbl), run_time=0.3)
        self.play(Create(quantum_line), run_time=0.3)
        self.play(FadeIn(quantum_lbl), run_time=0.3)
        self.play(GrowFromCenter(brace), run_time=0.4)
        self.play(FadeIn(zpe_lbl), run_time=0.3)
        self.wait(dur - 2.5)


class B07_FullLadder(Scene):
    """Full En = (n+1/2)*hbar*omega inside parabola, n=0..5."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Parabola
        x_vals = np.linspace(-5.5, 5.5, 300)
        pts = [np.array([x, 0.22 * x**2 - 3.2, 0]) for x in x_vals
               if 0.22 * x**2 - 3.2 <= 3.5]
        parabola = VMobject(color=INK, stroke_width=2.0)
        parabola.set_points_smoothly(pts)

        # Energy rungs
        rung_data = []
        for n in range(6):
            e_val = (n + 0.5) * 1.1  # scaled for display
            y = e_val - 3.2
            # Width from classical turning points E = 1/2 m w^2 x^2
            x_max = min(np.sqrt(e_val / 0.22), 5.0)
            rung_data.append((n, y, x_max))

        rungs = VGroup()
        labels = VGroup()
        for n, y, x_max in rung_data:
            r = Line([-x_max, y, 0], [x_max, y, 0], color=TEAL, stroke_width=2.0)
            lbl = Text(f"n={n}", font=MONO, color=TEAL, font_size=14).move_to([x_max + 0.5, y, 0])
            rungs.add(r)
            labels.add(lbl)

        formula = Text("E_n = (n + 1/2) * hbar*omega",
                       font=MONO, color=TEAL, font_size=22).move_to([0, 3.2, 0])

        self.play(Create(parabola), run_time=0.4)
        # Add rungs one at a time for variety
        for i, (r, lbl) in enumerate(zip(rungs, labels)):
            self.play(Create(r), FadeIn(lbl), run_time=0.25)
        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.5)
        self.wait(max(dur - 0.4 - 6 * 0.25 - 0.5, 1.0))


class B08_InfraredSpectrum(Scene):
    """Evenly spaced absorption lines — the ruler."""
    def construct(self):
        dur = DUR.get("B08", 11.0)
        # Axes
        ax_x = Arrow(start=[-5.5, -2.5, 0], end=[5.5, -2.5, 0],
                     color=INK, stroke_width=2, buff=0)
        freq_lbl = SerifLabel("frequency", accent=INK, size=20).move_to([5.5, -3.1, 0])

        # Evenly spaced absorption lines (TEAL)
        line_positions = [-3.5, -2.1, -0.7, 0.7, 2.1, 3.5]
        lines = VGroup(*[
            Line([x, -2.5, 0], [x, 1.5, 0], color=TEAL, stroke_width=3.0)
            for x in line_positions
        ])

        # Ruler brace
        r_brace = DoubleArrow(start=[-3.5, -3.2, 0], end=[3.5, -3.2, 0],
                               color=TEAL, stroke_width=1.8, buff=0)
        r_lbl = SerifLabel("evenly spaced = omega", accent=TEAL, size=20).move_to([0, -3.8, 0])

        ruler_chip = LabelChip("looks like a ruler", accent=TEAL, size=20).move_to([0, 2.5, 0])

        self.play(GrowArrow(ax_x), FadeIn(freq_lbl), run_time=0.4)
        # Draw lines one by one for visual variety
        for line in lines:
            self.play(Create(line), run_time=0.2)
        self.play(GrowFromCenter(r_brace), run_time=0.4)
        self.play(FadeIn(r_lbl), run_time=0.3)
        self.play(GrowFromCenter(ruler_chip), run_time=0.4)
        self.wait(max(dur - 0.4 - 6 * 0.2 - 0.4 - 0.3 - 0.4, 1.0))


class B09_HeliumExample(Scene):
    """Helium zero-point motion prevents crystallization."""
    def construct(self):
        dur = DUR.get("B09", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: classical — helium locked in lattice (CRIMSON crossed out)
        left_title = SerifLabel("classical: lattice", accent=CRIMSON, size=20).move_to([-3.5, 3.2, 0])
        grid_pts = [(-4.5 + 0.9 * c, -1.2 + 0.9 * r)
                    for r in range(4) for c in range(4)]
        lattice = VGroup(*[
            Circle(radius=0.28, color=CRIMSON, fill_color=CRIMSON,
                   fill_opacity=0.3, stroke_width=1.5).move_to([x, y, 0])
            for x, y in grid_pts
        ])
        cross = VGroup(
            Line([-5.8, -2.5, 0], [-1.2, 2.5, 0], color=CRIMSON, stroke_width=4),
            Line([-1.2, -2.5, 0], [-5.8, 2.5, 0], color=CRIMSON, stroke_width=4),
        )

        # Right: quantum — helium jittering (TEAL)
        right_title = SerifLabel("quantum: jitter wins", accent=TEAL, size=20).move_to([3.5, 3.2, 0])
        he_atoms = VGroup(*[
            Circle(radius=0.28, color=TEAL, fill_color=TEAL,
                   fill_opacity=0.3, stroke_width=1.5).move_to(
                [2.0 + 1.2 * (i % 3) + 0.15 * np.sin(i * 1.3),
                 -1.2 + 1.2 * (i // 3) + 0.15 * np.cos(i * 0.9), 0])
            for i in range(9)
        ])
        zp_chip = LabelChip("zero-point energy > binding energy", accent=TEAL, size=16).move_to([3.5, -2.8, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), run_time=0.3)
        self.play(Create(lattice), run_time=0.5)
        self.play(Create(cross), run_time=0.3)
        self.play(FadeIn(right_title), run_time=0.3)
        self.play(Create(he_atoms), run_time=0.5)
        self.play(GrowFromCenter(zp_chip), run_time=0.4)
        self.wait(dur - 2.7)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Smooth trap = oscillator.\nEnergy is discrete.\nSpacing = hbar*omega.\nLowest rung: not zero — hbar*omega/2.",
                      font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
