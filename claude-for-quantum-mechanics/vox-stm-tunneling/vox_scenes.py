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
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.6, 0])
        title = Text("Why a Microscope Can\nFeel a Single Atom", font=DISPLAY, font_size=34,
                     color=INK, weight=BOLD, line_spacing=1.2).move_to([0, -0.2, 0])
        sub = Text("quantum tunneling", font=SERIF, font_size=22, color=SLATE, slant=ITALIC).move_to([0, -1.6, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(dur - 1.3)


# ── B02 STM Setup ─────────────────────────────────────────────────────────────
class B02_STMSetup(Scene):
    def construct(self):
        dur = DUR.get("B02", 10.0)

        # Surface: a row of atom bumps
        surface_y = -1.5
        surface = Line([-6.0, surface_y, 0], [6.0, surface_y, 0], color=INK, stroke_width=2)
        atoms = VGroup()
        for x in np.linspace(-4.5, 4.5, 9):
            a = Circle(radius=0.35, color=INK, fill_color=SLATE, fill_opacity=0.6).move_to([x, surface_y + 0.35, 0])
            atoms.add(a)

        # STM tip
        tip_x = 0.0
        tip_y = surface_y + 0.35 + 0.35 + 0.55  # above the center atom
        tip_body = Polygon(
            [tip_x - 0.6, tip_y + 1.2, 0],
            [tip_x + 0.6, tip_y + 1.2, 0],
            [tip_x, tip_y, 0],
            color=INK, fill_color=SLATE, fill_opacity=0.8
        )
        tip_dot = Dot([tip_x, tip_y, 0], color=TEAL, radius=0.08)

        # Gap label
        gap_line = DashedLine([tip_x + 0.8, tip_y, 0], [tip_x + 0.8, surface_y + 0.7, 0],
                               color=CRIMSON, stroke_width=1.5, dash_length=0.12)
        gap_lbl = Text("d ≈ 5 Å", font=MONO, font_size=16, color=CRIMSON).next_to(gap_line, RIGHT, buff=0.15)

        # Current arrow
        current_arrow = Arrow([tip_x, tip_y - 0.05, 0], [tip_x, surface_y + 0.75, 0],
                               color=TEAL, stroke_width=3, max_tip_length_to_length_ratio=0.2, buff=0)
        current_lbl = Text("I (tunneling)", font=SERIF, font_size=16, color=TEAL, slant=ITALIC).next_to(current_arrow, LEFT, buff=0.2)

        self.play(Create(surface), run_time=0.3)
        self.play(Create(atoms), run_time=0.4)
        self.play(FadeIn(tip_body), FadeIn(tip_dot), run_time=0.4)
        self.play(Create(gap_line), FadeIn(gap_lbl), run_time=0.4)
        self.play(GrowArrow(current_arrow), run_time=0.4)
        self.play(FadeIn(current_lbl), run_time=0.3)
        self.wait(dur - 2.2)


# ── B03 Question Card ─────────────────────────────────────────────────────────
class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        q = Text("The tip never touches.\nClassically, no current should flow.\nWhy does it?",
                 font=SERIF, font_size=17, color=INK, line_spacing=1.4).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(dur - 0.9)


# ── B04 Wavefunction Decay ────────────────────────────────────────────────────
class B04_WavefunctionDecay(Scene):
    def construct(self):
        dur = DUR.get("B04", 10.0)

        # Metal tip region (left) and metal surface region (right)
        tip_region = Rectangle(width=2.5, height=4.0, color=SLATE, fill_color=SLATE, fill_opacity=0.25).move_to([-4.5, 0, 0])
        tip_lbl = Text("tip\n(metal)", font=DISPLAY, font_size=14, color=SLATE).move_to([-4.5, 1.6, 0])
        surface_region = Rectangle(width=2.5, height=4.0, color=SLATE, fill_color=SLATE, fill_opacity=0.25).move_to([4.5, 0, 0])
        surface_lbl = Text("surface\n(metal)", font=DISPLAY, font_size=14, color=SLATE).move_to([4.5, 1.6, 0])

        # Barrier region
        barrier = Rectangle(width=2.0, height=4.0, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.12).move_to([0, 0, 0])
        barrier_lbl = Text("vacuum gap", font=DISPLAY, font_size=13, color=CRIMSON).move_to([0, 1.8, 0])

        # Exponential decay curve inside barrier
        kappa = 1.025
        x_left = -1.0
        x_right = 1.0
        psi_scale = 1.6
        decay_curve = FunctionGraph(
            lambda x: psi_scale * np.exp(-kappa * (x - x_left)),
            x_range=[x_left, x_right],
            color=TEAL, stroke_width=3
        )

        # Waveform on left (oscillating)
        wave_left = FunctionGraph(
            lambda x: 0.5 * np.sin(3 * (x + 3.7)),
            x_range=[-5.7, -1.0],
            color=TEAL, stroke_width=2.5
        )

        # Small transmitted wave on right
        wave_right = FunctionGraph(
            lambda x: 0.12 * np.sin(3 * (x - 1.0)),
            x_range=[1.0, 3.7],
            color=TEAL, stroke_width=2.5
        )

        # Formula
        formula_lbl = Text("ψ ~ e^(−κd)", font=MONO, font_size=20, color=INK).move_to([0, -2.0, 0])
        kappa_lbl = Text("κ ≈ 1.025 Å⁻¹", font=MONO, font_size=16, color=CRIMSON).move_to([0, -2.6, 0])

        self.play(FadeIn(tip_region), FadeIn(surface_region), run_time=0.3)
        self.play(FadeIn(barrier), FadeIn(barrier_lbl), run_time=0.35)
        self.play(FadeIn(tip_lbl), FadeIn(surface_lbl), run_time=0.3)
        self.play(Create(wave_left), run_time=0.5)
        self.play(Create(decay_curve), run_time=0.6)
        self.play(Create(wave_right), run_time=0.4)
        self.play(FadeIn(formula_lbl), run_time=0.3)
        self.play(FadeIn(kappa_lbl), run_time=0.3)
        self.wait(dur - 3.05)


# ── B05 Current Formula ───────────────────────────────────────────────────────
class B05_CurrentFormula(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)

        # Formula
        formula = Text("I  ∝  e^(−2κd)", font=MONO, font_size=32, color=INK).move_to([0, 2.8, 0])
        formula_underline = Line([-3.0, 2.45, 0], [3.0, 2.45, 0], color=TEAL, stroke_width=1.5)
        kappa_box = Rectangle(width=3.8, height=0.55, color=TEAL, fill_color=TEAL, fill_opacity=0.15).move_to([0, 1.95, 0])
        kappa_lbl = Text("κ ≈ 1.025 Å⁻¹  for  φ = 4 eV", font=MONO, font_size=16, color=TEAL).move_to(kappa_box)

        # Axes
        ax = Axes(
            x_range=[3, 9, 1],
            y_range=[0, 1.1, 0.25],
            x_length=7.0,
            y_length=3.2,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False
        ).move_to([0.3, -0.7, 0])
        x_lbl = Text("gap d (Å)", font=DISPLAY, font_size=14, color=INK).next_to(ax, DOWN, buff=0.2)
        y_lbl = Text("I (norm.)", font=DISPLAY, font_size=14, color=INK).next_to(ax, LEFT, buff=0.25)

        kappa_val = 1.025
        i_max = np.exp(-2 * kappa_val * 3)
        decay_line = ax.plot(
            lambda x: np.exp(-2 * kappa_val * x) / i_max,
            x_range=[3, 9],
            color=TEAL, stroke_width=2.5
        )

        # Individual dots for each gap value
        dot_3 = Dot(ax.coords_to_point(3, np.exp(-2*kappa_val*3)/i_max), color=TEAL, radius=0.1)
        dot_5 = Dot(ax.coords_to_point(5, np.exp(-2*kappa_val*5)/i_max), color=TEAL, radius=0.1)
        dot_7 = Dot(ax.coords_to_point(7, np.exp(-2*kappa_val*7)/i_max), color=TEAL, radius=0.1)

        # Annotation arrow pointing to the steep drop
        steep_arrow = Arrow(
            ax.coords_to_point(6.5, 0.25),
            ax.coords_to_point(5.5, 0.08),
            color=CRIMSON, stroke_width=2,
            max_tip_length_to_length_ratio=0.25, buff=0
        )
        steep_lbl = Text("steep!", font=DISPLAY, font_size=14, color=CRIMSON).next_to(steep_arrow.get_start(), RIGHT, buff=0.1)

        self.play(FadeIn(formula), run_time=0.4)
        self.play(Create(formula_underline), run_time=0.3)
        self.play(FadeIn(kappa_box), FadeIn(kappa_lbl), run_time=0.4)
        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(decay_line), run_time=0.7)
        self.play(FadeIn(dot_3), run_time=0.2)
        self.play(FadeIn(dot_5), run_time=0.2)
        self.play(FadeIn(dot_7), run_time=0.2)
        self.play(GrowArrow(steep_arrow), FadeIn(steep_lbl), run_time=0.4)
        self.wait(dur - 3.3)


# ── B06 Exponential Sensitivity ───────────────────────────────────────────────
class B06_ExponentialSensitivity(Scene):
    def construct(self):
        dur = DUR.get("B06", 11.0)

        # Left panel: gap d
        left_label = Text("gap = d", font=DISPLAY, font_size=18, color=INK).move_to([-4.5, 2.5, 0])
        tip_l = Polygon([-4.5 - 0.5, 2.0, 0], [-4.5 + 0.5, 2.0, 0], [-4.5, 1.3, 0],
                        color=INK, fill_color=SLATE, fill_opacity=0.8)
        surface_l = Line([-6.0, -0.5, 0], [-2.5, -0.5, 0], color=INK, stroke_width=2)
        gap_l = DashedLine([-4.5, 1.3, 0], [-4.5, -0.5, 0], color=INK, stroke_width=1.5, dash_length=0.1)
        i_label_l = Text("I₀", font=MONO, font_size=22, color=TEAL).move_to([-3.8, 0.5, 0])

        # Right panel: gap d + 1Å
        right_label = Text("gap = d + 1 Å", font=DISPLAY, font_size=18, color=INK).move_to([2.5, 2.5, 0])
        tip_r = Polygon([2.5 - 0.5, 2.0, 0], [2.5 + 0.5, 2.0, 0], [2.5, 1.3, 0],
                        color=INK, fill_color=SLATE, fill_opacity=0.8)
        surface_r = Line([0.5, -0.5, 0], [4.5, -0.5, 0], color=INK, stroke_width=2)
        gap_r = DashedLine([2.5, 1.3, 0], [2.5, -0.5, 0], color=CRIMSON, stroke_width=1.5, dash_length=0.1)
        i_label_r = Text("I₀ / 7.4", font=MONO, font_size=22, color=CRIMSON).move_to([3.2, 0.5, 0])

        # Factor label
        factor_line = Line([-1.5, 0.0, 0], [0.0, 0.0, 0], color=INK, stroke_width=1.5)
        factor_arrow = Arrow([0.0, 0.0, 0], [1.0, 0.0, 0], color=INK, stroke_width=2,
                             max_tip_length_to_length_ratio=0.25, buff=0)
        factor_lbl = Text("÷ e² ≈ ÷ 7.4", font=MONO, font_size=16, color=CRIMSON).move_to([-0.5, 0.55, 0])

        # Result box
        result_box = Rectangle(width=4.5, height=0.6, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.12).move_to([0, -2.0, 0])
        result_lbl = Text("1 Å  →  current × (1/7)", font=MONO, font_size=18, color=CRIMSON).move_to(result_box)

        self.play(FadeIn(left_label), FadeIn(tip_l), FadeIn(surface_l), run_time=0.4)
        self.play(Create(gap_l), FadeIn(i_label_l), run_time=0.4)
        self.play(FadeIn(right_label), FadeIn(tip_r), FadeIn(surface_r), run_time=0.4)
        self.play(Create(gap_r), FadeIn(i_label_r), run_time=0.4)
        self.play(Create(factor_line), run_time=0.3)
        self.play(GrowArrow(factor_arrow), FadeIn(factor_lbl), run_time=0.4)
        self.play(FadeIn(result_box), FadeIn(result_lbl), run_time=0.4)
        self.wait(dur - 2.7)


# ── B07 Tip Atom Dominates ────────────────────────────────────────────────────
class B07_TipAtomDominates(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)

        # Surface
        surface = Line([-6.0, -1.8, 0], [6.0, -1.8, 0], color=INK, stroke_width=2)
        for x in np.linspace(-5.0, 5.0, 11):
            self.add(Circle(radius=0.28, color=INK, fill_color=SLATE, fill_opacity=0.5).move_to([x, -1.52, 0]))

        # Tip body (jagged apex)
        tip_body = Polygon(
            [-0.7, 3.0, 0], [0.7, 3.0, 0],
            [0.35, 1.8, 0], [0.15, 1.5, 0], [0.0, 1.1, 0],
            color=INK, fill_color=SLATE, fill_opacity=0.8
        )

        # Apex atom (TEAL — closest)
        apex_atom = Circle(radius=0.22, color=TEAL, fill_color=TEAL, fill_opacity=0.9).move_to([0, 0.88, 0])
        apex_lbl = Text("front atom", font=DISPLAY, font_size=14, color=TEAL).next_to(apex_atom, LEFT, buff=0.3)

        # Second atom on tip side (CRIMSON — further)
        second_atom = Circle(radius=0.18, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.5).move_to([0.35, 1.15, 0])
        second_lbl = Text("next atom\n(1 Å further)", font=DISPLAY, font_size=12, color=CRIMSON).next_to(second_atom, RIGHT, buff=0.2)

        # Current arrows
        big_arrow = Arrow([0.0, 0.66, 0], [0.0, -1.2, 0], color=TEAL, stroke_width=4,
                          max_tip_length_to_length_ratio=0.15, buff=0)
        big_current_lbl = Text("I", font=MONO, font_size=22, color=TEAL).next_to(big_arrow, LEFT, buff=0.15)

        small_arrow = Arrow([0.7, 0.95, 0], [0.7, -0.6, 0], color=CRIMSON, stroke_width=1.5,
                            max_tip_length_to_length_ratio=0.2, buff=0)
        small_current_lbl = Text("I/7", font=MONO, font_size=16, color=CRIMSON).next_to(small_arrow, RIGHT, buff=0.12)

        self.play(Create(surface), run_time=0.3)
        self.play(FadeIn(tip_body), run_time=0.4)
        self.play(FadeIn(apex_atom), FadeIn(apex_lbl), run_time=0.4)
        self.play(FadeIn(second_atom), FadeIn(second_lbl), run_time=0.4)
        self.play(GrowArrow(big_arrow), FadeIn(big_current_lbl), run_time=0.4)
        self.play(GrowArrow(small_arrow), FadeIn(small_current_lbl), run_time=0.4)
        self.wait(dur - 2.3)


# ── B08 Scan Trace ────────────────────────────────────────────────────────────
class B08_ScanTrace(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        # Surface atoms (row)
        surface_y = -1.5
        n_atoms = 7
        xs = np.linspace(-4.5, 4.5, n_atoms)
        surface_line = Line([-5.5, surface_y, 0], [5.5, surface_y, 0], color=INK, stroke_width=2)
        atom_circles = VGroup()
        for x in xs:
            a = Circle(radius=0.32, color=INK, fill_color=SLATE, fill_opacity=0.6).move_to([x, surface_y + 0.32, 0])
            atom_circles.add(a)

        # Current trace above
        trace_y_base = 1.2
        trace_pts = []
        for i, x in enumerate(xs):
            trace_pts.append([x, trace_y_base + 0.8, 0])  # peak over each atom
            if i < len(xs) - 1:
                mid_x = (x + xs[i+1]) / 2
                trace_pts.append([mid_x, trace_y_base, 0])  # valley between atoms

        trace_curve = VMobject(color=TEAL, stroke_width=3)
        trace_curve.set_points_smoothly([np.array(p) for p in trace_pts])

        trace_lbl = Text("tunneling current I(x)", font=SERIF, font_size=15, color=TEAL, slant=ITALIC).move_to([0, 2.6, 0])
        surface_lbl = Text("surface topography", font=SERIF, font_size=15, color=SLATE, slant=ITALIC).move_to([0, -2.3, 0])

        # Tip (moving)
        tip = Polygon([-0.35, 0.0, 0], [0.35, 0.0, 0], [0.0, -0.45, 0],
                      color=INK, fill_color=SLATE, fill_opacity=0.8).move_to([xs[0], 0.8, 0])

        # Vertical dashed guide lines (atom ↔ peak)
        guides = VGroup()
        for x in xs:
            g = DashedLine([x, surface_y + 0.64, 0], [x, trace_y_base + 0.8, 0],
                           color=INK, stroke_width=1.0, dash_length=0.1)
            guides.add(g)

        self.play(Create(surface_line), run_time=0.3)
        self.play(Create(atom_circles), run_time=0.4)
        self.play(FadeIn(tip), run_time=0.3)
        self.play(FadeIn(trace_lbl), FadeIn(surface_lbl), run_time=0.3)
        self.play(Create(trace_curve), run_time=1.5)
        self.play(FadeIn(guides), run_time=0.4)
        self.play(tip.animate.move_to([xs[-1], 0.8, 0]), run_time=1.5, rate_func=linear)
        self.wait(dur - 4.7)


# ── B09 Tunneling Universal ───────────────────────────────────────────────────
class B09_TunnelingUniversal(Scene):
    def construct(self):
        dur = DUR.get("B09", 9.0)

        systems = [
            ("STM", -4.5),
            ("alpha decay", 0.0),
            ("photosynthesis", 4.5),
        ]

        boxes = VGroup()
        labels = VGroup()
        curves = VGroup()
        formulas = VGroup()
        dividers = VGroup()
        dot_markers = VGroup()

        for name, x in systems:
            box = Rectangle(width=3.0, height=3.0, color=TEAL, fill_color=TEAL, fill_opacity=0.07).move_to([x, 0.3, 0])
            lbl = Text(name, font=DISPLAY, font_size=15, color=INK, weight=BOLD).move_to([x, 1.55, 0])
            curve = FunctionGraph(
                lambda t, x_=x: 0.7 * np.exp(-1.1 * (t - (x_ - 1.1))),
                x_range=[x - 1.1, x + 1.1],
                color=TEAL, stroke_width=2.5
            )
            fml = Text("e^(−2κd)", font=MONO, font_size=13, color=SLATE).move_to([x, -0.75, 0])
            divider = Line([x - 1.3, 1.2, 0], [x + 1.3, 1.2, 0], color=TEAL, stroke_width=1.0)
            dot = Dot([x - 1.0, 0.6, 0], color=TEAL, radius=0.07)
            boxes.add(box)
            labels.add(lbl)
            curves.add(curve)
            formulas.add(fml)
            dividers.add(divider)
            dot_markers.add(dot)

        # Bottom label
        bottom = Text("same exponential decay", font=SERIF, font_size=18, color=INK, slant=ITALIC).move_to([0, -2.0, 0])
        bottom_line = Line([-3.5, -2.3, 0], [3.5, -2.3, 0], color=TEAL, stroke_width=1.5)
        # Highlight arrow
        highlight_arrow = Arrow([-1.0, -1.6, 0], [1.0, -1.6, 0], color=TEAL, stroke_width=2,
                                max_tip_length_to_length_ratio=0.2, buff=0)

        self.play(Create(boxes), run_time=0.4)
        self.play(FadeIn(labels), run_time=0.35)
        self.play(Create(dividers), run_time=0.3)
        self.play(Create(curves), run_time=0.5)
        self.play(FadeIn(dot_markers), run_time=0.3)
        self.play(FadeIn(formulas), run_time=0.35)
        self.play(FadeIn(bottom), run_time=0.3)
        self.play(Create(bottom_line), run_time=0.25)
        self.play(GrowArrow(highlight_arrow), run_time=0.3)
        self.wait(dur - 3.05)


# ── B10 Recap Card ────────────────────────────────────────────────────────────
class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        recap = Text(
            "psi ~ e^(-kd). Current ~ e^(-2kd).\n1 angstrom = factor of ~7-10.\nExponential ruler: atomic resolution.",
            font=SERIF, font_size=18, color=INK, line_spacing=1.5
        ).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(recap), run_time=0.5)
        self.wait(dur - 0.9)
