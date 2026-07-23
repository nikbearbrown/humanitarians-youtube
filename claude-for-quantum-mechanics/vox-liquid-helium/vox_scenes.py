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


# ── B01 Title Card ────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 2.2, 0])
        title = Text("Why Liquid Helium Refuses to\nFreeze Even at Absolute Zero",
                     font=DISPLAY, font_size=28, color=INK, weight=BOLD, line_spacing=1.2).move_to([0, 0.4, 0])
        sub = Text("zero-point energy", font=SERIF, font_size=22, color=SLATE, slant=ITALIC).move_to([0, -1.2, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(dur - 1.3)


# ── B02 Noble Gas Comparison ──────────────────────────────────────────────────
class B02_NobleGasComparison(Scene):
    def construct(self):
        dur = DUR.get("B02", 10.0)

        # Temperature axis (horizontal)
        t_axis = Arrow([-6.0, 0.0, 0], [5.5, 0.0, 0], color=INK, stroke_width=2,
                       max_tip_length_to_length_ratio=0.06, buff=0)
        t_lbl = Text("Temperature", font=DISPLAY, font_size=16, color=INK).move_to([5.3, -0.4, 0])
        zero_mark = Line([- 5.5, -0.15, 0], [-5.5, 0.15, 0], color=INK, stroke_width=2)
        zero_lbl = Text("0 K", font=MONO, font_size=14, color=INK).move_to([-5.5, -0.45, 0])

        # Noble gases: freeze temperature marks
        gases = [
            ("Neon\n24.6 K", -3.5, CRIMSON),
            ("Argon\n83.8 K", -1.0, CRIMSON),
            ("Krypton\n115.8 K", 1.5, CRIMSON),
        ]

        freeze_lines = VGroup()
        freeze_labels = VGroup()
        freeze_dots = VGroup()
        for name, x, color in gases:
            line = Line([x, -0.2, 0], [x, 1.4, 0], color=color, stroke_width=2)
            lbl = Text(name, font=DISPLAY, font_size=13, color=color).move_to([x, 2.0, 0])
            dot = Dot([x, 0.0, 0], color=color, radius=0.1)
            freeze_lines.add(line)
            freeze_labels.add(lbl)
            freeze_dots.add(dot)

        # Helium: stays liquid along bottom
        he_line = Line([-5.5, -0.8, 0], [5.0, -0.8, 0], color=TEAL, stroke_width=4)
        he_dot = Dot([-5.5, -0.8, 0], color=TEAL, radius=0.1)
        he_lbl = Text("Helium — stays liquid to 0 K", font=DISPLAY, font_size=15, color=TEAL).move_to([-1.0, -1.5, 0])

        # Cross for "never freezes" over He line near 0 K
        cross_lbl = Text("no freeze!", font=SERIF, font_size=14, color=TEAL, slant=ITALIC).move_to([-5.2, -2.0, 0])
        cross_line = Line([-5.8, -2.3, 0], [-4.6, -2.3, 0], color=TEAL, stroke_width=1.5)

        self.play(GrowArrow(t_axis), FadeIn(t_lbl), run_time=0.4)
        self.play(Create(zero_mark), FadeIn(zero_lbl), run_time=0.3)
        self.play(Create(freeze_lines), FadeIn(freeze_dots), run_time=0.4)
        self.play(FadeIn(freeze_labels), run_time=0.35)
        self.play(Create(he_line), FadeIn(he_dot), run_time=0.4)
        self.play(FadeIn(he_lbl), run_time=0.3)
        self.play(FadeIn(cross_lbl), Create(cross_line), run_time=0.3)
        self.wait(dur - 2.45)


# ── B03 Question Card ─────────────────────────────────────────────────────────
class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        q = Text("At 0 K: no thermal motion remains.\nNeon: solid crystal.\nHelium: still liquid. Why?",
                 font=SERIF, font_size=18, color=INK, line_spacing=1.4).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(dur - 0.9)


# ── B04 Zero-Point Energy ─────────────────────────────────────────────────────
class B04_ZeroPointEnergy(Scene):
    def construct(self):
        dur = DUR.get("B04", 10.0)

        # Parabola (harmonic well)
        parabola = FunctionGraph(
            lambda x: 0.5 * x ** 2 - 2.0,
            x_range=[-3.5, 3.5],
            color=INK, stroke_width=2.5
        )

        # Classical floor: bottom of well
        classical_floor = DashedLine([-3.0, -2.0, 0], [3.0, -2.0, 0], color=CRIMSON, stroke_width=2, dash_length=0.15)
        classical_lbl = Text("classical: E = 0 possible", font=DISPLAY, font_size=14, color=CRIMSON).move_to([0, -2.5, 0])

        # Quantum ZPE floor
        zpe_y = -0.6
        zpe_floor = Line([-3.5, zpe_y, 0], [3.5, zpe_y, 0], color=TEAL, stroke_width=2.5)
        zpe_lbl = Text("ZPE = ℏω/2 (quantum minimum)", font=DISPLAY, font_size=14, color=TEAL).move_to([0, -0.15, 0])

        # Wavefunction sitting above ZPE
        wave = FunctionGraph(
            lambda x: 0.6 * np.exp(-x ** 2 / 1.2) + zpe_y,
            x_range=[-3.0, 3.0],
            color=TEAL, stroke_width=2.5
        )

        # Bracket showing ZPE gap
        bracket_line = Line([3.8, -2.0, 0], [3.8, zpe_y, 0], color=TEAL, stroke_width=2)
        bracket_top = Line([3.5, zpe_y, 0], [4.1, zpe_y, 0], color=TEAL, stroke_width=1.5)
        bracket_bot = Line([3.5, -2.0, 0], [4.1, -2.0, 0], color=TEAL, stroke_width=1.5)
        bracket_lbl = Text("ZPE", font=MONO, font_size=15, color=TEAL).move_to([5.0, -1.3, 0])

        # Uncertainty principle label
        unc_lbl = Text("σₓ small → σₚ large → KE > 0", font=SERIF, font_size=14, color=INK, slant=ITALIC).move_to([0, 2.5, 0])

        self.play(Create(parabola), run_time=0.4)
        self.play(Create(classical_floor), FadeIn(classical_lbl), run_time=0.35)
        self.play(Create(zpe_floor), FadeIn(zpe_lbl), run_time=0.35)
        self.play(Create(wave), run_time=0.4)
        self.play(Create(bracket_line), Create(bracket_top), Create(bracket_bot), FadeIn(bracket_lbl), run_time=0.4)
        self.play(FadeIn(unc_lbl), run_time=0.3)
        self.wait(dur - 2.2)


# ── B05 Helium Confinement ────────────────────────────────────────────────────
class B05_HeliumConfinement(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)

        # He atom circle
        he_circle = Circle(radius=1.5, color=TEAL, fill_color=TEAL, fill_opacity=0.15).move_to([-2.5, 0.0, 0])
        he_atom = Circle(radius=0.25, color=TEAL, fill_color=TEAL, fill_opacity=0.9).move_to([-2.5, 0.0, 0])
        he_lbl = Text("He", font=DISPLAY, font_size=16, color=INK, weight=BOLD).move_to([-2.5, 0.0, 0])

        # Confinement diameter label
        diam_arrow = DoubleArrow([-4.0, -1.9, 0], [-1.0, -1.9, 0], color=INK, stroke_width=2,
                                 max_tip_length_to_length_ratio=0.12, buff=0)
        diam_lbl = Text("3 Å confinement", font=MONO, font_size=15, color=INK).move_to([-2.5, -2.4, 0])

        # Neighbor atoms (pressing in)
        neighbor_positions = [(0.5, 0.0), (-5.5, 0.0), (-2.5, 2.0), (-2.5, -2.0)]
        neighbors = VGroup()
        for x, y in neighbor_positions:
            n = Circle(radius=0.22, color=SLATE, fill_color=SLATE, fill_opacity=0.5).move_to([x, y, 0])
            neighbors.add(n)

        # ZPE calculation box
        zpe_box = Rectangle(width=5.0, height=1.8, color=TEAL, fill_color=TEAL, fill_opacity=0.1).move_to([3.5, 0.5, 0])
        zpe_calc = Text("ZPE ≈ 10 meV per atom", font=MONO, font_size=16, color=TEAL).move_to([3.5, 0.7, 0])
        zpe_unc = Text("(from σₓ = 1.5 Å,\nσₓσₚ ≥ ℏ/2)", font=SERIF, font_size=13, color=SLATE, slant=ITALIC).move_to([3.5, 0.0, 0])

        # Jitter arrows
        jitter_arrows = VGroup()
        for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
            arr = Arrow(
                [-2.5, 0.0, 0],
                [-2.5 + 0.7 * np.cos(angle), 0.7 * np.sin(angle), 0],
                color=TEAL, stroke_width=1.5,
                max_tip_length_to_length_ratio=0.25, buff=0.25
            )
            jitter_arrows.add(arr)

        self.play(Create(he_circle), FadeIn(he_atom), FadeIn(he_lbl), run_time=0.4)
        self.play(FadeIn(neighbors), run_time=0.35)
        self.play(Create(diam_arrow), FadeIn(diam_lbl), run_time=0.35)
        self.play(*[GrowArrow(a) for a in jitter_arrows], run_time=0.4)
        self.play(FadeIn(zpe_box), FadeIn(zpe_calc), run_time=0.35)
        self.play(FadeIn(zpe_unc), run_time=0.3)
        self.wait(dur - 2.1)


# ── B06 Energy Comparison ─────────────────────────────────────────────────────
class B06_EnergyComparison(Scene):
    def construct(self):
        dur = DUR.get("B06", 11.0)

        # Y axis
        y_axis = Arrow([0, -2.5, 0], [0, 3.0, 0], color=INK, stroke_width=2,
                       max_tip_length_to_length_ratio=0.08, buff=0)
        y_lbl = Text("energy (meV)", font=DISPLAY, font_size=14, color=INK).move_to([-1.5, 3.1, 0])

        # ZPE bar (tall — 10 meV)
        zpe_h = 4.0
        zpe_bar = Rectangle(width=2.0, height=zpe_h, color=TEAL, fill_color=TEAL, fill_opacity=0.7).move_to([-2.5, -2.5 + zpe_h/2, 0])
        zpe_bar_lbl = Text("ZPE\n10 meV", font=DISPLAY, font_size=16, color=TEAL, weight=BOLD).move_to([-2.5, 2.3, 0])

        # Binding bar (short — 1 meV)
        bind_h = 0.4
        bind_bar = Rectangle(width=2.0, height=bind_h, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.7).move_to([2.5, -2.5 + bind_h/2, 0])
        bind_bar_lbl = Text("vdW binding\n~1 meV", font=DISPLAY, font_size=16, color=CRIMSON, weight=BOLD).move_to([2.5, 0.5, 0])

        # X axis labels
        zpe_x_lbl = Text("ZPE", font=MONO, font_size=14, color=TEAL).move_to([-2.5, -2.9, 0])
        bind_x_lbl = Text("binding", font=MONO, font_size=14, color=CRIMSON).move_to([2.5, -2.9, 0])

        # Win label
        win_box = Rectangle(width=7.0, height=0.65, color=TEAL, fill_color=TEAL, fill_opacity=0.15).move_to([0, -3.5, 0])
        win_lbl = Text("ZPE >> binding  →  atoms shake free", font=DISPLAY, font_size=15, color=TEAL).move_to(win_box)

        # Ratio indicator dot and connector
        ratio_dot = Dot([-2.5, 1.5, 0], color=TEAL, radius=0.1)
        cross_line = Line([2.1, 0.3, 0], [2.9, 0.3, 0], color=CRIMSON, stroke_width=1.5)

        self.play(GrowArrow(y_axis), FadeIn(y_lbl), run_time=0.4)
        self.play(FadeIn(zpe_bar), run_time=0.35)
        self.play(FadeIn(zpe_bar_lbl), FadeIn(zpe_x_lbl), run_time=0.3)
        self.play(FadeIn(bind_bar), run_time=0.3)
        self.play(FadeIn(bind_bar_lbl), FadeIn(bind_x_lbl), run_time=0.3)
        self.play(FadeIn(ratio_dot), run_time=0.2)
        self.play(Create(cross_line), run_time=0.25)
        self.play(FadeIn(win_box), FadeIn(win_lbl), run_time=0.35)
        self.wait(dur - 2.4)


# ── B07 Mass Comparison ───────────────────────────────────────────────────────
class B07_MassComparison(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)

        # Two columns
        he_box = Rectangle(width=5.0, height=6.0, color=TEAL, fill_color=TEAL, fill_opacity=0.06).move_to([-3.2, 0.0, 0])
        ne_box = Rectangle(width=5.0, height=6.0, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.06).move_to([3.2, 0.0, 0])

        he_title = Text("Helium (m = 4 u)", font=DISPLAY, font_size=17, color=TEAL, weight=BOLD).move_to([-3.2, 2.7, 0])
        ne_title = Text("Neon (m = 20 u)", font=DISPLAY, font_size=17, color=CRIMSON, weight=BOLD).move_to([3.2, 2.7, 0])

        divider = Line([-3.2, 2.3, 0], [-3.2 + 6.4, 2.3, 0], color=INK, stroke_width=0.8)

        # ZPE rows
        he_zpe = Text("ZPE: ~10 meV", font=MONO, font_size=15, color=TEAL).move_to([-3.2, 1.7, 0])
        ne_zpe = Text("ZPE: ~2 meV", font=MONO, font_size=15, color=CRIMSON).move_to([3.2, 1.7, 0])

        # Binding rows
        he_bind = Text("binding: ~1 meV", font=MONO, font_size=15, color=TEAL).move_to([-3.2, 1.0, 0])
        ne_bind = Text("binding: ~3 meV", font=MONO, font_size=15, color=CRIMSON).move_to([3.2, 1.0, 0])

        # Outcome
        he_out = Text("ZPE > binding\n→ liquid at 0 K", font=SERIF, font_size=15, color=TEAL, slant=ITALIC).move_to([-3.2, -0.4, 0])
        ne_out = Text("ZPE < binding\n→ freezes at 24.6 K", font=SERIF, font_size=15, color=CRIMSON, slant=ITALIC).move_to([3.2, -0.4, 0])

        # Outcome arrows
        he_arrow = Arrow([-3.2, -1.5, 0], [-3.2, -2.2, 0], color=TEAL, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.25, buff=0)
        ne_arrow = Arrow([3.2, -1.5, 0], [3.2, -2.2, 0], color=CRIMSON, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.25, buff=0)
        he_final = Text("liquid ✓", font=DISPLAY, font_size=16, color=TEAL).move_to([-3.2, -2.6, 0])
        ne_final = Text("solid ✓", font=DISPLAY, font_size=16, color=CRIMSON).move_to([3.2, -2.6, 0])

        # Extra geometric variety
        he_dot = Dot([-3.2, 2.2, 0], color=TEAL, radius=0.1)
        ne_dot = Dot([3.2, 2.2, 0], color=CRIMSON, radius=0.1)
        he_bar_zpe = Rectangle(width=0.8, height=1.2, color=TEAL, fill_color=TEAL, fill_opacity=0.5).move_to([-4.0, -1.8, 0])
        ne_bar_bind = Rectangle(width=0.8, height=0.5, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.5).move_to([2.5, -1.8, 0])

        self.play(FadeIn(he_box), FadeIn(ne_box), run_time=0.4)
        self.play(FadeIn(he_title), FadeIn(ne_title), run_time=0.35)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(he_dot), FadeIn(ne_dot), run_time=0.2)
        self.play(FadeIn(he_zpe), FadeIn(ne_zpe), run_time=0.3)
        self.play(FadeIn(he_bind), FadeIn(ne_bind), run_time=0.3)
        self.play(FadeIn(he_bar_zpe), FadeIn(ne_bar_bind), run_time=0.3)
        self.play(FadeIn(he_out), FadeIn(ne_out), run_time=0.35)
        self.play(GrowArrow(he_arrow), GrowArrow(ne_arrow), run_time=0.35)
        self.play(FadeIn(he_final), FadeIn(ne_final), run_time=0.3)
        self.wait(dur - 3.05)


# ── B08 Pressure Freezes ──────────────────────────────────────────────────────
class B08_PressureFreezes(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        # He container at 1 atm
        container1 = Rectangle(width=3.0, height=3.5, color=TEAL, fill_color=TEAL, fill_opacity=0.1).move_to([-3.5, 0.2, 0])
        container1_lbl = Text("He at 1 atm\n0 K", font=DISPLAY, font_size=15, color=INK).move_to([-3.5, 1.8, 0])
        liquid_lbl = Text("liquid", font=SERIF, font_size=18, color=TEAL, slant=ITALIC).move_to([-3.5, 0.2, 0])

        # He atoms sloshing (3 dots)
        dots_left = VGroup()
        for x, y in [(-4.3, -0.3), (-3.5, 0.2), (-2.7, -0.5)]:
            d = Dot([x, y, 0], color=TEAL, radius=0.22)
            dots_left.add(d)

        # Pressure arrow
        press_arrow = Arrow([-0.5, 0.2, 0], [0.5, 0.2, 0], color=INK, stroke_width=3,
                            max_tip_length_to_length_ratio=0.2, buff=0)
        press_lbl = Text("> 25 atm", font=DISPLAY, font_size=15, color=INK).move_to([0, 0.7, 0])

        # He container at 25 atm — frozen lattice
        container2 = Rectangle(width=2.5, height=3.0, color=SLATE, fill_color=SLATE, fill_opacity=0.1).move_to([3.5, 0.2, 0])
        container2_lbl = Text("He at 25 atm\n0 K", font=DISPLAY, font_size=15, color=INK).move_to([3.5, 1.7, 0])
        solid_lbl = Text("solid", font=SERIF, font_size=18, color=SLATE, slant=ITALIC).move_to([3.5, 0.2, 0])

        # Frozen atoms (grid)
        dots_right = VGroup()
        for x, y in [(3.0, -0.2), (3.5, -0.2), (4.0, -0.2),
                     (3.0, 0.3), (3.5, 0.3), (4.0, 0.3)]:
            d = Dot([x, y, 0], color=SLATE, radius=0.18)
            dots_right.add(d)

        # Lattice lines
        lat_lines = VGroup()
        for x in [3.0, 3.5, 4.0]:
            lat_lines.add(Line([x, -0.4, 0], [x, 0.5, 0], color=SLATE, stroke_width=1))
        for y in [-0.2, 0.3]:
            lat_lines.add(Line([2.8, y, 0], [4.2, y, 0], color=SLATE, stroke_width=1))

        # Bottom note
        note = Text("ZPE < deeper binding well", font=SERIF, font_size=14, color=INK, slant=ITALIC).move_to([0, -2.5, 0])

        self.play(FadeIn(container1), FadeIn(container1_lbl), run_time=0.4)
        self.play(FadeIn(dots_left), FadeIn(liquid_lbl), run_time=0.35)
        self.play(GrowArrow(press_arrow), FadeIn(press_lbl), run_time=0.35)
        self.play(FadeIn(container2), FadeIn(container2_lbl), run_time=0.35)
        self.play(Create(lat_lines), run_time=0.35)
        self.play(FadeIn(dots_right), FadeIn(solid_lbl), run_time=0.3)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(dur - 2.4)


# ── B09 Zero-Point Real ───────────────────────────────────────────────────────
class B09_ZeroPointReal(Scene):
    def construct(self):
        dur = DUR.get("B09", 9.0)

        systems = [
            ("liquid He", -4.5),
            ("Casimir plates", 0.0),
            ("vacuum", 4.5),
        ]

        boxes = VGroup()
        labels = VGroup()
        zpe_labels = VGroup()
        dividers = VGroup()
        dots = VGroup()

        for name, x in systems:
            box = Rectangle(width=3.2, height=3.2, color=TEAL, fill_color=TEAL, fill_opacity=0.07).move_to([x, 0.3, 0])
            lbl = Text(name, font=DISPLAY, font_size=15, color=INK, weight=BOLD).move_to([x, 1.55, 0])
            zpe = Text("zero-point\nenergy", font=SERIF, font_size=14, color=TEAL, slant=ITALIC).move_to([x, 0.3, 0])
            div = Line([x - 1.4, 1.2, 0], [x + 1.4, 1.2, 0], color=TEAL, stroke_width=0.8)
            d = Dot([x, -0.8, 0], color=TEAL, radius=0.08)
            boxes.add(box)
            labels.add(lbl)
            zpe_labels.add(zpe)
            dividers.add(div)
            dots.add(d)

        bottom = Text("confinement always costs kinetic energy",
                      font=SERIF, font_size=17, color=INK, slant=ITALIC).move_to([0, -2.0, 0])
        underline = Line([-4.5, -2.3, 0], [4.5, -2.3, 0], color=TEAL, stroke_width=1.5)
        confirm_arrow = Arrow([-1.0, -2.8, 0], [1.0, -2.8, 0], color=TEAL, stroke_width=2,
                              max_tip_length_to_length_ratio=0.2, buff=0)

        self.play(Create(boxes), run_time=0.4)
        self.play(FadeIn(labels), run_time=0.35)
        self.play(Create(dividers), run_time=0.25)
        self.play(FadeIn(zpe_labels), run_time=0.35)
        self.play(FadeIn(dots), run_time=0.25)
        self.play(FadeIn(bottom), run_time=0.3)
        self.play(Create(underline), run_time=0.25)
        self.play(GrowArrow(confirm_arrow), run_time=0.3)
        self.wait(dur - 2.45)


# ── B10 Recap Card ────────────────────────────────────────────────────────────
class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        recap = Text(
            "ZPE = hbar*omega/2. Confinement costs energy.\nHe: ZPE 10 meV > binding 1 meV.\nLiquid at 0 K. Frozen only above 25 atm.",
            font=SERIF, font_size=17, color=INK, line_spacing=1.5
        ).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(recap), run_time=0.5)
        self.wait(dur - 0.9)
