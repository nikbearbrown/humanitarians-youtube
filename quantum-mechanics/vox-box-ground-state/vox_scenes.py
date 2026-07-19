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
    """Title card: Why a Particle in a Box Cannot Sit Still."""

    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text(
            "Why a Particle in a Box\nCannot Sit Still",
            font=DISPLAY, color=INK, font_size=40, line_spacing=1.3
        ).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])

        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B02_ClassicalMarble(Scene):
    """Classical marble in a box at rest — zero energy, CRIMSON dot on floor."""

    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Box outline
        box = Rectangle(width=8.0, height=3.5, color=INK, stroke_width=3, fill_opacity=0)
        box.move_to([0, -0.3, 0])

        # Floor line
        floor = Line([-4.0, -2.05, 0], [4.0, -2.05, 0], color=INK, stroke_width=2.5)

        # Classical marble (CRIMSON dot)
        marble = Dot(color=CRIMSON, radius=0.22).move_to([0, -1.8, 0])

        # Energy = 0 label
        e_label = Text("Energy = 0", font=MONO, color=CRIMSON, font_size=28).move_to([0, 1.8, 0])
        sub_label = Text("perfectly still", font=SERIF, color=INK, font_size=22,
                         slant=ITALIC).move_to([0, 1.3, 0])

        self.play(Create(box), Create(floor), run_time=0.6)
        self.play(FadeIn(marble, shift=DOWN * 0.5), run_time=0.5)
        self.play(FadeIn(e_label, shift=UP * 0.2), FadeIn(sub_label, shift=UP * 0.2), run_time=0.6)
        # Marble shifts slightly to show it's truly at rest
        self.play(marble.animate.shift(LEFT * 0.2), run_time=0.3)
        self.play(marble.animate.shift(RIGHT * 0.2), run_time=0.3)
        self.wait(dur - 2.3)


class B03_QuestionCard(Scene):
    """THE QUESTION: Classical predicts E=0 allowed; quantum lowest energy > 0. Why?"""

    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text(
            "Classical physics predicts E = 0 is allowed.\nThe quantum lowest energy is above zero. Why?",
            font=DISPLAY, color=INK, font_size=26, line_spacing=1.3
        ).move_to([0, 0.4, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])

        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_BoxWalls(Scene):
    """Box with hard walls; wavefunction drawn going to zero at both walls."""

    def construct(self):
        dur = DUR.get("B04", 10.0)
        x_left = -3.5
        x_right = 3.5

        # Box walls — thick vertical lines
        wall_l = Line([x_left, -2.5, 0], [x_left, 2.5, 0], color=INK, stroke_width=5)
        wall_r = Line([x_right, -2.5, 0], [x_right, 2.5, 0], color=INK, stroke_width=5)
        floor_line = Line([x_left, -2.5, 0], [x_right, -2.5, 0], color=INK, stroke_width=2)

        wall_lbl_l = SerifLabel("wall", accent=INK, size=22).move_to([x_left - 0.7, 2.8, 0])
        wall_lbl_r = SerifLabel("wall", accent=INK, size=22).move_to([x_right + 0.7, 2.8, 0])

        # Zero markers at walls
        zero_l = Text("psi = 0", font=MONO, color=TEAL, font_size=22).move_to([x_left, -3.2, 0])
        zero_r = Text("psi = 0", font=MONO, color=TEAL, font_size=22).move_to([x_right, -3.2, 0])

        # Wavefunction: full arch from wall to wall
        x_vals = np.linspace(x_left, x_right, 200)
        psi_pts = [np.array([x, 1.8 * np.sin(np.pi * (x - x_left) / (x_right - x_left)), 0])
                   for x in x_vals]
        psi = VMobject(color=TEAL, stroke_width=3)
        psi.set_points_smoothly(psi_pts)

        self.play(Create(wall_l), Create(wall_r), Create(floor_line), run_time=0.6)
        self.play(FadeIn(wall_lbl_l), FadeIn(wall_lbl_r), run_time=0.4)
        self.play(Create(psi), run_time=dur * 0.4)
        self.play(FadeIn(zero_l, shift=UP * 0.2), FadeIn(zero_r, shift=UP * 0.2), run_time=0.5)
        self.wait(dur * 0.2)


class B05_HalfWave(Scene):
    """Half-wavelength arch inside box — the minimum possible wavefunction."""

    def construct(self):
        dur = DUR.get("B05", 10.0)
        x_left = -3.5
        x_right = 3.5

        wall_l = Line([x_left, -2.5, 0], [x_left, 2.5, 0], color=INK, stroke_width=5)
        wall_r = Line([x_right, -2.5, 0], [x_right, 2.5, 0], color=INK, stroke_width=5)

        x_vals = np.linspace(x_left, x_right, 200)

        # Ground state: n=1, half-wave
        psi1_pts = [np.array([x, 2.0 * np.sin(np.pi * (x - x_left) / (x_right - x_left)), 0])
                    for x in x_vals]
        psi1 = VMobject(color=TEAL, stroke_width=3)
        psi1.set_points_smoothly(psi1_pts)

        # Half-wavelength bracket
        brace_y = -3.2
        brace = Line([x_left, brace_y, 0], [x_right, brace_y, 0],
                     color=TEAL, stroke_width=2)
        tick_l = Line([x_left, brace_y - 0.15, 0], [x_left, brace_y + 0.15, 0],
                      color=TEAL, stroke_width=2)
        tick_r = Line([x_right, brace_y - 0.15, 0], [x_right, brace_y + 0.15, 0],
                      color=TEAL, stroke_width=2)
        half_lbl = SerifLabel("one half-wavelength", accent=TEAL, size=22).move_to([0, brace_y - 0.5, 0])

        ground_lbl = LabelChip("ground state", accent=TEAL, size=22).move_to([0, 3.1, 0])

        self.play(Create(wall_l), Create(wall_r), run_time=0.4)
        self.play(Create(psi1), run_time=dur * 0.4)
        self.play(
            Create(brace), FadeIn(tick_l), FadeIn(tick_r), FadeIn(half_lbl),
            run_time=0.5
        )
        self.play(GrowFromCenter(ground_lbl), run_time=0.4)
        self.wait(dur * 0.2)


class B06_MinimumShape(Scene):
    """Compare: could the arch be any flatter? Show n=1 vs attempts at flatter curves."""

    def construct(self):
        dur = DUR.get("B06", 11.0)
        x_left = -3.5
        x_right = 3.5

        wall_l = Line([x_left, -2.5, 0], [x_left, 2.5, 0], color=INK, stroke_width=5)
        wall_r = Line([x_right, -2.5, 0], [x_right, 2.5, 0], color=INK, stroke_width=5)

        x_vals = np.linspace(x_left, x_right, 200)

        # Ground state arch
        psi_pts = [np.array([x, 1.8 * np.sin(np.pi * (x - x_left) / (x_right - x_left)), 0])
                   for x in x_vals]
        psi = VMobject(color=TEAL, stroke_width=3)
        psi.set_points_smoothly(psi_pts)

        # "Flatter" attempt that can't satisfy boundary conditions
        flat_pts = [np.array([x, 0.3 * np.sin(np.pi * (x - x_left) / (x_right - x_left)), 0])
                    for x in x_vals]
        flat_wave = VMobject(color=CRIMSON, stroke_width=2.5, stroke_opacity=0.7)
        flat_wave.set_points_smoothly(flat_pts)

        label_real = SerifLabel("this arch is the minimum", accent=TEAL, size=22).move_to([0, -2.8, 0])
        label_flat = SerifLabel("flatter means smaller curvature", accent=CRIMSON, size=22).move_to([0, -3.3, 0])

        self.play(Create(wall_l), Create(wall_r), run_time=0.3)
        self.play(Create(psi), run_time=dur * 0.3)
        self.play(FadeIn(label_real, shift=UP * 0.2), run_time=0.4)
        self.play(Create(flat_wave), run_time=0.5)
        self.play(FadeIn(label_flat, shift=UP * 0.2), run_time=0.4)
        self.wait(dur * 0.3)


class B07_CurvatureMomentum(Scene):
    """Curvature of wavefunction = spatial frequency = momentum."""

    def construct(self):
        dur = DUR.get("B07", 10.0)
        x_left = -5.5
        x_right = 5.5
        x_vals = np.linspace(x_left, x_right, 300)

        # Tight arch (high curvature, high momentum)
        tight_pts = [np.array([x, 1.8 * np.sin(2 * np.pi * (x - x_left) / (x_right - x_left)), 0])
                     for x in x_vals]
        tight = VMobject(color=CRIMSON, stroke_width=3)
        tight.set_points_smoothly(tight_pts)

        # Loose arch (lower curvature, lower momentum)
        loose_pts = [np.array([x, 1.8 * np.sin(np.pi * (x - x_left) / (x_right - x_left)), 0])
                     for x in x_vals]
        loose = VMobject(color=TEAL, stroke_width=3)
        loose.set_points_smoothly(loose_pts)

        lbl_tight = SerifLabel("tight arch: higher momentum", accent=CRIMSON, size=22).move_to([0, -2.5, 0])
        lbl_loose = SerifLabel("loose arch: lower momentum", accent=TEAL, size=22).move_to([0, -3.1, 0])

        # Momentum arrows
        arr_tight = Arrow(start=[-1.5, 2.3, 0], end=[1.5, 2.3, 0],
                          color=CRIMSON, stroke_width=3.5, buff=0)
        arr_loose = Arrow(start=[-0.8, 2.8, 0], end=[0.8, 2.8, 0],
                          color=TEAL, stroke_width=3.5, buff=0)

        self.play(Create(loose), Create(tight), run_time=dur * 0.35)
        self.play(GrowArrow(arr_tight), GrowArrow(arr_loose), run_time=0.6)
        self.play(FadeIn(lbl_tight), FadeIn(lbl_loose), run_time=0.5)
        self.wait(dur * 0.3)


class B08_ConfinementEnergy(Scene):
    """Two boxes: narrow vs wide. Narrower box = tighter arch = higher energy."""

    def construct(self):
        dur = DUR.get("B08", 10.0)
        # Narrow box (left side)
        nw = 2.5
        nl = -5.5
        nr = nl + nw
        wall_nl = Line([nl, -2.5, 0], [nl, 2.5, 0], color=INK, stroke_width=5)
        wall_nr = Line([nr, -2.5, 0], [nr, 2.5, 0], color=INK, stroke_width=5)
        x_n = np.linspace(nl, nr, 100)
        psi_n_pts = [np.array([x, 2.2 * np.sin(np.pi * (x - nl) / nw), 0]) for x in x_n]
        psi_n = VMobject(color=CRIMSON, stroke_width=3)
        psi_n.set_points_smoothly(psi_n_pts)
        lbl_n = SerifLabel("narrow box\nhigher energy", accent=CRIMSON, size=20).move_to([nl + nw / 2, -3.2, 0])

        # Wide box (right side)
        ww = 5.0
        wl = 0.5
        wr = wl + ww
        wall_wl = Line([wl, -2.5, 0], [wl, 2.5, 0], color=INK, stroke_width=5)
        wall_wr = Line([wr, -2.5, 0], [wr, 2.5, 0], color=INK, stroke_width=5)
        x_w = np.linspace(wl, wr, 150)
        psi_w_pts = [np.array([x, 1.3 * np.sin(np.pi * (x - wl) / ww), 0]) for x in x_w]
        psi_w = VMobject(color=TEAL, stroke_width=3)
        psi_w.set_points_smoothly(psi_w_pts)
        lbl_w = SerifLabel("wide box\nlower energy", accent=TEAL, size=20).move_to([wl + ww / 2, -3.2, 0])

        self.play(
            Create(wall_nl), Create(wall_nr), Create(wall_wl), Create(wall_wr),
            run_time=0.6
        )
        self.play(Create(psi_n), Create(psi_w), run_time=dur * 0.4)
        self.play(FadeIn(lbl_n), FadeIn(lbl_w), run_time=0.5)
        self.wait(dur * 0.3)


class B09_FlatIsVoid(Scene):
    """Flat line at zero = no particle. Compare: real arch vs flat zero line."""

    def construct(self):
        dur = DUR.get("B09", 11.0)
        x_left = -3.5
        x_right = 3.5

        wall_l = Line([x_left, -2.5, 0], [x_left, 2.5, 0], color=INK, stroke_width=5)
        wall_r = Line([x_right, -2.5, 0], [x_right, 2.5, 0], color=INK, stroke_width=5)

        x_vals = np.linspace(x_left, x_right, 200)

        # Real ground state
        psi_pts = [np.array([x, 1.8 * np.sin(np.pi * (x - x_left) / (x_right - x_left)), 0])
                   for x in x_vals]
        psi = VMobject(color=TEAL, stroke_width=3)
        psi.set_points_smoothly(psi_pts)

        # Flat line: this would be "E=0" but it's zero everywhere
        flat_pts = [np.array([x, 0.0, 0]) for x in x_vals]
        flat_line = VMobject(color=CRIMSON, stroke_width=2.5)
        flat_line.set_points_smoothly(flat_pts)

        lbl_arch = SerifLabel("arch: particle exists", accent=TEAL, size=24).move_to([0, 3.0, 0])
        lbl_flat = SerifLabel("flat zero: no particle anywhere", accent=CRIMSON, size=24).move_to([0, -3.2, 0])

        self.play(Create(wall_l), Create(wall_r), run_time=0.4)
        self.play(Create(psi), run_time=0.6)
        self.play(FadeIn(lbl_arch, shift=UP * 0.2), run_time=0.4)
        self.play(Create(flat_line), run_time=0.5)
        self.play(FadeIn(lbl_flat, shift=UP * 0.2), run_time=0.4)
        self.wait(dur - 2.3)


class B10_Example(Scene):
    """Illustrative: 1 nm box, E1 ~ 0.38 eV. Energy level diagram."""

    def construct(self):
        dur = DUR.get("B10", 12.0)
        # Axis for energy
        axis = Line([-3.0, -3.0, 0], [-3.0, 3.0, 0], color=INK, stroke_width=2.5)
        e_label = Text("energy", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([-3.8, 3.3, 0])

        # Zero energy level (CRIMSON = forbidden classical)
        zero_line = Line([-2.8, -2.5, 0], [3.5, -2.5, 0], color=CRIMSON,
                         stroke_width=2, stroke_opacity=0.6)
        zero_lbl = Text("E = 0", font=MONO, color=CRIMSON, font_size=20).move_to([4.3, -2.5, 0])

        # E1 ground state level (TEAL = quantum allowed)
        e1_y = -1.0
        e1_line = Line([-2.8, e1_y, 0], [3.5, e1_y, 0], color=TEAL, stroke_width=3)
        e1_lbl = Text("E1 ~ 0.38 eV", font=MONO, color=TEAL, font_size=22).move_to([5.2, e1_y, 0])

        # Small wavefunction arch on the E1 line
        x_vals = np.linspace(-2.5, 2.5, 100)
        arch_pts = [np.array([x, 0.8 * np.sin(np.pi * (x + 2.5) / 5.0) + e1_y, 0]) for x in x_vals]
        arch = VMobject(color=TEAL, stroke_width=2)
        arch.set_points_smoothly(arch_pts)

        # Gap arrow from E=0 to E1
        gap_arr = Arrow(start=[-2.5, -2.4, 0], end=[-2.5, e1_y + 0.05, 0],
                        color=INK, stroke_width=2.5, buff=0.05)

        # Illustrative label
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([0, 3.3, 0])
        box_lbl = SerifLabel("1 nm box, electron", accent=TEAL, size=20).move_to([0, 2.7, 0])

        self.play(Create(axis), FadeIn(e_label), run_time=0.5)
        self.play(Create(zero_line), FadeIn(zero_lbl), run_time=0.5)
        self.play(Create(e1_line), FadeIn(e1_lbl), run_time=0.5)
        self.play(Create(arch), run_time=0.5)
        self.play(GrowArrow(gap_arr), run_time=0.5)
        self.play(FadeIn(ill_lbl), FadeIn(box_lbl), run_time=0.4)
        self.wait(dur - 3.4)


class B11_RecapCard(Scene):
    """RECAP endcard: arch -> momentum -> energy -> zero forbidden + QUANTUM MECHANICS."""

    def construct(self):
        dur = DUR.get("B11", 9.0)
        answer = Text(
            "The wavefunction must arch.\nAny arch is momentum.\nMomentum is energy.\nZero is forbidden.",
            font=DISPLAY, color=INK, font_size=24, line_spacing=1.3
        ).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.2, 0])

        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
