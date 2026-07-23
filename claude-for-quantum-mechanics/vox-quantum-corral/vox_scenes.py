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


def draw_ring_pattern(center, radius, n_nodes, color, stroke_width=2.0):
    """Draw n concentric rings in a circle (approximating radial standing-wave pattern)."""
    rings = VGroup()
    outer = Circle(radius=radius, color=color, stroke_width=stroke_width + 1.0).move_to(center)
    rings.add(outer)
    for i in range(1, n_nodes + 1):
        r = radius * i / (n_nodes + 1)
        ring = Circle(radius=r, color=color, stroke_width=stroke_width).move_to(center)
        rings.add(ring)
    return rings


# ── B01 Title Card ────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 2.2, 0])
        title = Text("Why 48 Iron Atoms Make Quantum\nRipples Nobody Placed There",
                     font=DISPLAY, font_size=27, color=INK, weight=BOLD, line_spacing=1.2).move_to([0, 0.5, 0])
        sub = Text("the quantum corral", font=SERIF, font_size=22, color=SLATE, slant=ITALIC).move_to([0, -1.1, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(dur - 1.3)


# ── B02 Corral Setup ──────────────────────────────────────────────────────────
class B02_CorralSetup(Scene):
    def construct(self):
        dur = DUR.get("B02", 10.0)

        # Ring of iron atoms
        n_atoms = 24
        R = 2.2
        atom_dots = VGroup()
        for i in range(n_atoms):
            angle = 2 * np.pi * i / n_atoms
            x = R * np.cos(angle)
            y = R * np.sin(angle)
            d = Dot([x, y, 0], color=CRIMSON, radius=0.14)
            atom_dots.add(d)

        ring_label = Text("48 iron atoms", font=DISPLAY, font_size=14, color=CRIMSON).move_to([0, -3.0, 0])

        # Electron wave inside
        wave_circle = Circle(radius=0.8, color=TEAL, stroke_width=2).move_to([0, 0, 0])
        wave_ring2 = Circle(radius=1.5, color=TEAL, stroke_width=1.5).move_to([0, 0, 0])

        # Reflection arrow
        inc_arrow = Arrow([0.0, 0.0, 0], [R - 0.3, 0.0, 0], color=TEAL, stroke_width=2,
                          max_tip_length_to_length_ratio=0.2, buff=0)
        refl_arrow = Arrow([R - 0.3, 0.0, 0], [0.0, 0.0, 0], color=TEAL, stroke_width=2,
                           max_tip_length_to_length_ratio=0.2, buff=0)
        bounce_lbl = Text("wave bounces", font=SERIF, font_size=14, color=TEAL, slant=ITALIC).move_to([0, -1.5, 0])

        # Surface label
        surface_lbl = Text("copper surface", font=DISPLAY, font_size=13, color=SLATE).move_to([4.0, -3.0, 0])
        surface_line = Line([-6.0, -3.4, 0], [6.0, -3.4, 0], color=SLATE, stroke_width=1.5, stroke_opacity=0.5)

        self.play(Create(surface_line), FadeIn(surface_lbl), run_time=0.3)
        self.play(Create(atom_dots), run_time=0.5)
        self.play(FadeIn(ring_label), run_time=0.3)
        self.play(Create(wave_circle), run_time=0.35)
        self.play(Create(wave_ring2), run_time=0.3)
        self.play(GrowArrow(inc_arrow), run_time=0.3)
        self.play(GrowArrow(refl_arrow), FadeIn(bounce_lbl), run_time=0.3)
        self.wait(dur - 2.35)


# ── B03 Question Card ─────────────────────────────────────────────────────────
class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        q = Text("Classical: smooth distribution inside.\nQuantum corral: sharp rings appear.\nWhere do the rings come from?",
                 font=SERIF, font_size=17, color=INK, line_spacing=1.4).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(dur - 0.9)


# ── B04 Fitting Condition ─────────────────────────────────────────────────────
class B04_FittingCondition(Scene):
    def construct(self):
        dur = DUR.get("B04", 10.0)

        R = 2.0

        # Left: fitting wave (TEAL)
        left_cx = -3.5
        left_circle = Circle(radius=R, color=TEAL, stroke_width=2.5).move_to([left_cx, 0, 0])
        left_title = Text("fits: ψ = 0 at boundary", font=DISPLAY, font_size=14, color=TEAL).move_to([left_cx, 2.7, 0])
        # Radial wave fitting
        left_wave = FunctionGraph(
            lambda x: 0.8 * np.sin(np.pi * (x - (left_cx - R)) / (2 * R)),
            x_range=[left_cx - R, left_cx + R],
            color=TEAL, stroke_width=2.5
        )
        left_dot_l = Dot([left_cx - R, 0, 0], color=TEAL, radius=0.1)
        left_dot_r = Dot([left_cx + R, 0, 0], color=TEAL, radius=0.1)
        left_check = Text("✓", font=DISPLAY, font_size=28, color=TEAL).move_to([left_cx, -2.7, 0])

        # Right: non-fitting wave (CRIMSON)
        right_cx = 3.5
        right_circle = Circle(radius=R, color=CRIMSON, stroke_width=2.5).move_to([right_cx, 0, 0])
        right_title = Text("doesn't fit: ψ ≠ 0 at boundary", font=DISPLAY, font_size=14, color=CRIMSON).move_to([right_cx, 2.7, 0])
        # Non-fitting wave
        right_wave = FunctionGraph(
            lambda x: 0.8 * np.sin(1.7 * np.pi * (x - (right_cx - R)) / (2 * R)),
            x_range=[right_cx - R, right_cx + R],
            color=CRIMSON, stroke_width=2.5
        )
        right_x = Text("✗", font=DISPLAY, font_size=28, color=CRIMSON).move_to([right_cx, -2.7, 0])

        # Divider
        div = Line([0, -3.0, 0], [0, 3.0, 0], color=INK, stroke_width=1, stroke_opacity=0.3)

        # Extra geometric variety: node markers and fit indicator
        left_node = Dot([left_cx, 0.0, 0], color=TEAL, radius=0.1)
        right_arrow = Arrow([right_cx, -1.0, 0], [right_cx + 0.8, -2.0, 0], color=CRIMSON,
                            stroke_width=2, max_tip_length_to_length_ratio=0.25, buff=0)

        self.play(Create(div), run_time=0.2)
        self.play(Create(left_circle), run_time=0.3)
        self.play(Create(right_circle), run_time=0.3)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.35)
        self.play(Create(left_wave), run_time=0.4)
        self.play(Create(right_wave), run_time=0.4)
        self.play(FadeIn(left_dot_l), FadeIn(left_dot_r), run_time=0.25)
        self.play(FadeIn(left_node), run_time=0.2)
        self.play(GrowArrow(right_arrow), run_time=0.25)
        self.play(FadeIn(left_check), FadeIn(right_x), run_time=0.3)
        self.wait(dur - 2.9)


# ── B05 Standing Modes ────────────────────────────────────────────────────────
class B05_StandingModes(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)

        R = 1.5
        modes = [
            ("n = 1", -4.5, 0),
            ("n = 2", 0.0, 1),
            ("n = 3", 4.5, 2),
        ]

        all_circles = VGroup()
        all_rings = VGroup()
        all_labels = VGroup()
        all_dots = VGroup()

        for name, x, n_rings in modes:
            outer = Circle(radius=R, color=TEAL, stroke_width=2).move_to([x, 0.2, 0])
            all_circles.add(outer)

            # Central filled circle (peak)
            center_dot = Dot([x, 0.2, 0], color=TEAL, radius=0.3, fill_opacity=0.6)
            all_dots.add(center_dot)

            for i in range(1, n_rings + 1):
                r = R * i / (n_rings + 1)
                ring = Circle(radius=r, color=TEAL, stroke_width=1.5).move_to([x, 0.2, 0])
                all_rings.add(ring)

            lbl = Text(name, font=DISPLAY, font_size=16, color=INK, weight=BOLD).move_to([x, -2.0, 0])
            all_labels.add(lbl)

        desc_n1 = Text("1 peak", font=SERIF, font_size=13, color=TEAL, slant=ITALIC).move_to([-4.5, -2.5, 0])
        desc_n2 = Text("peak + 1 ring", font=SERIF, font_size=13, color=TEAL, slant=ITALIC).move_to([0.0, -2.5, 0])
        desc_n3 = Text("peak + 2 rings", font=SERIF, font_size=13, color=TEAL, slant=ITALIC).move_to([4.5, -2.5, 0])
        descs = VGroup(desc_n1, desc_n2, desc_n3)

        title = Text("only discrete modes survive", font=DISPLAY, font_size=17, color=INK, weight=BOLD).move_to([0, 2.7, 0])
        title_line = Line([-4.5, 2.4, 0], [4.5, 2.4, 0], color=TEAL, stroke_width=1.2)

        # Extra geometric: radius markers and connector dots
        mode_dots = VGroup()
        for name, x, n_rings in modes:
            d = Dot([x + R + 0.2, 0.2, 0], color=TEAL, radius=0.08)
            mode_dots.add(d)
        connector_line = Line([-5.5, -1.7, 0], [5.5, -1.7, 0], color=TEAL, stroke_width=1.0)

        self.play(FadeIn(title), Create(title_line), run_time=0.4)
        self.play(Create(all_circles), run_time=0.4)
        self.play(FadeIn(all_dots), run_time=0.3)
        self.play(Create(all_rings), run_time=0.4)
        self.play(FadeIn(mode_dots), run_time=0.25)
        self.play(FadeIn(all_labels), run_time=0.3)
        self.play(FadeIn(descs), run_time=0.3)
        self.play(Create(connector_line), run_time=0.25)
        self.wait(dur - 2.6)


# ── B06 Wavelength Fit ────────────────────────────────────────────────────────
class B06_WavelengthFit(Scene):
    def construct(self):
        dur = DUR.get("B06", 10.0)

        # Corral circle
        R = 2.2
        corral = Circle(radius=R, color=INK, stroke_width=2.5).move_to([0, 0, 0])
        radius_label = Text("r = 7 nm", font=MONO, font_size=15, color=INK).move_to([2.0, -2.7, 0])

        # Diameter arrow
        diam_arrow = DoubleArrow([-R, 0.0, 0], [R, 0.0, 0], color=INK, stroke_width=2,
                                  max_tip_length_to_length_ratio=0.1, buff=0)
        diam_lbl = Text("diameter = 14 nm", font=MONO, font_size=15, color=INK).move_to([0, 0.45, 0])

        # Ground-state wave (half wavelength fits)
        wave = FunctionGraph(
            lambda x: 0.8 * np.sin(np.pi * (x + R) / (2 * R)),
            x_range=[-R, R],
            color=TEAL, stroke_width=3
        )
        wave_lbl = Text("λ/2 = 7 nm  →  λ = 14 nm", font=MONO, font_size=15, color=TEAL).move_to([0, -0.5, 0])

        # Iron atoms on ring
        n = 16
        atom_dots = VGroup()
        for i in range(n):
            angle = 2 * np.pi * i / n
            d = Dot([R * np.cos(angle), R * np.sin(angle), 0], color=CRIMSON, radius=0.13)
            atom_dots.add(d)

        # Fitting label
        fit_box = Rectangle(width=5.5, height=0.65, color=TEAL, fill_color=TEAL, fill_opacity=0.15).move_to([0, -3.2, 0])
        fit_lbl = Text("ground state: one half-wavelength across corral", font=DISPLAY, font_size=13, color=TEAL).move_to(fit_box)

        self.play(Create(corral), run_time=0.35)
        self.play(Create(atom_dots), run_time=0.4)
        self.play(Create(diam_arrow), FadeIn(diam_lbl), run_time=0.35)
        self.play(Create(wave), FadeIn(wave_lbl), run_time=0.4)
        self.play(FadeIn(radius_label), run_time=0.25)
        self.play(FadeIn(fit_box), FadeIn(fit_lbl), run_time=0.35)
        self.wait(dur - 2.1)


# ── B07 Guitar Analogy ────────────────────────────────────────────────────────
class B07_GuitarAnalogy(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)

        # Guitar string (left panel)
        string_y_base = 1.5
        string_title = Text("guitar string", font=DISPLAY, font_size=16, color=INK).move_to([-4.5, 3.0, 0])
        string_left = Dot([-6.0, string_y_base, 0], color=INK, radius=0.1)
        string_right = Dot([-2.0, string_y_base, 0], color=INK, radius=0.1)
        string_body = Line([-6.0, string_y_base, 0], [-2.0, string_y_base, 0], color=INK, stroke_width=1.5)

        # Harmonics
        harmonics = VGroup()
        for n, y_off in [(1, 0.0), (2, -1.2), (3, -2.4)]:
            h = FunctionGraph(
                lambda x, n_=n: 0.4 * np.sin(n_ * np.pi * (x + 6.0) / 4.0),
                x_range=[-6.0, -2.0],
                color=TEAL, stroke_width=2
            ).shift([0, string_y_base + y_off - 1.2, 0])
            lbl = Text(f"n={n}", font=MONO, font_size=13, color=TEAL).move_to([-6.5, string_y_base + y_off - 1.2, 0])
            harmonics.add(h)
            harmonics.add(lbl)

        # Corral (right panel)
        corral_title = Text("quantum corral", font=DISPLAY, font_size=16, color=INK).move_to([3.5, 3.0, 0])
        R_c = 1.5
        corral_c = Circle(radius=R_c, color=INK, stroke_width=2).move_to([3.5, 0.5, 0])
        corral_rings = draw_ring_pattern([3.5, 0.5, 0], R_c, 1, TEAL, stroke_width=2)

        # Connecting label
        conn = Text("same principle:\nonly fitting waves survive",
                    font=SERIF, font_size=15, color=SLATE, slant=ITALIC).move_to([-0.5, -3.0, 0])
        div = Line([0, -1.5, 0], [0, 3.2, 0], color=INK, stroke_width=1, stroke_opacity=0.3)

        self.play(Create(div), run_time=0.2)
        self.play(FadeIn(string_title), FadeIn(corral_title), run_time=0.35)
        self.play(Create(string_body), FadeIn(string_left), FadeIn(string_right), run_time=0.35)
        self.play(Create(harmonics), run_time=0.5)
        self.play(Create(corral_c), run_time=0.3)
        self.play(Create(corral_rings), run_time=0.35)
        self.play(FadeIn(conn), run_time=0.3)
        self.wait(dur - 2.25)


# ── B08 Quantization Universal ────────────────────────────────────────────────
class B08_QuantizationUniversal(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        systems = [
            ("quantum corral", -4.5),
            ("quantum dot", 0.0),
            ("atom", 4.5),
        ]

        boxes = VGroup()
        labels = VGroup()
        dividers = VGroup()
        desc_labels = VGroup()
        arrows = VGroup()
        dots = VGroup()

        for name, x in systems:
            box = Rectangle(width=3.2, height=3.5, color=TEAL, fill_color=TEAL, fill_opacity=0.07).move_to([x, 0.3, 0])
            lbl = Text(name, font=DISPLAY, font_size=14, color=INK, weight=BOLD).move_to([x, 1.7, 0])
            div = Line([x - 1.4, 1.35, 0], [x + 1.4, 1.35, 0], color=TEAL, stroke_width=0.8)
            desc = Text("boundary →\ndiscrete modes", font=SERIF, font_size=13, color=TEAL, slant=ITALIC).move_to([x, 0.3, 0])
            arr = Arrow([x, -0.7, 0], [x, -1.2, 0], color=TEAL, stroke_width=2,
                        max_tip_length_to_length_ratio=0.3, buff=0)
            d = Dot([x, -1.5, 0], color=TEAL, radius=0.08)
            boxes.add(box)
            labels.add(lbl)
            dividers.add(div)
            desc_labels.add(desc)
            arrows.add(arr)
            dots.add(d)

        title_lbl = Text("quantization is universal",
                         font=SERIF, font_size=18, color=INK, slant=ITALIC).move_to([0, -2.2, 0])
        underline = Line([-3.8, -2.5, 0], [3.8, -2.5, 0], color=TEAL, stroke_width=1.5)

        self.play(Create(boxes), run_time=0.4)
        self.play(FadeIn(labels), run_time=0.35)
        self.play(Create(dividers), run_time=0.25)
        self.play(FadeIn(desc_labels), run_time=0.35)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.35)
        self.play(FadeIn(dots), run_time=0.25)
        self.play(FadeIn(title_lbl), Create(underline), run_time=0.3)
        self.wait(dur - 2.25)


# ── B09 Corral Citation ───────────────────────────────────────────────────────
class B09_CorralCitation(Scene):
    def construct(self):
        dur = DUR.get("B09", 9.0)

        # Citation box
        cite_box = Rectangle(width=10.0, height=1.4, color=SLATE, fill_color=SLATE, fill_opacity=0.08).move_to([0, 2.0, 0])
        cite_lbl = Text("Crommie, Lutz & Eigler — Science 262, 218 (1993)", font=MONO, font_size=15, color=SLATE).move_to([0, 2.1, 0])
        cite_sub = Text("Confinement of electrons to quantum corrals on a metal surface",
                        font=SERIF, font_size=13, color=SLATE, slant=ITALIC).move_to([0, 1.65, 0])

        # Corral diagram
        R_c = 1.5
        corral_main = Circle(radius=R_c, color=INK, stroke_width=2.5).move_to([0, -0.5, 0])
        rings_pattern = draw_ring_pattern([0, -0.5, 0], R_c, 2, TEAL, stroke_width=2)

        # "Wave function as photograph" label
        photo_lbl = Text("wave function as a photograph", font=SERIF, font_size=17, color=TEAL, slant=ITALIC).move_to([0, -2.7, 0])
        photo_line = Line([-3.5, -3.0, 0], [3.5, -3.0, 0], color=TEAL, stroke_width=1.5)

        # Nobel chip
        ibm_chip = LabelChip("IBM Almaden 1993", accent=SLATE, size=18).move_to([-3.0, -3.5, 0])

        # Extra geometric variety
        center_dot = Dot([0, -0.5, 0], color=TEAL, radius=0.12)
        radial_arrow = Arrow([0, -0.5, 0], [R_c, -0.5, 0], color=TEAL, stroke_width=2,
                             max_tip_length_to_length_ratio=0.2, buff=0)

        self.play(FadeIn(cite_box), FadeIn(cite_lbl), run_time=0.4)
        self.play(FadeIn(cite_sub), run_time=0.3)
        self.play(Create(corral_main), run_time=0.35)
        self.play(FadeIn(center_dot), run_time=0.2)
        self.play(Create(rings_pattern), run_time=0.4)
        self.play(GrowArrow(radial_arrow), run_time=0.3)
        self.play(FadeIn(photo_lbl), run_time=0.3)
        self.play(Create(photo_line), run_time=0.25)
        self.play(GrowFromCenter(ibm_chip), run_time=0.3)
        self.wait(dur - 2.8)


# ── B10 Recap Card ────────────────────────────────────────────────────────────
class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        recap = Text(
            "Ring wall: only fitting modes survive.\nDiscrete nodes = rings in the image.\nQuantization made visible (1993).",
            font=SERIF, font_size=18, color=INK, line_spacing=1.5
        ).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(recap), run_time=0.5)
        self.wait(dur - 0.9)
