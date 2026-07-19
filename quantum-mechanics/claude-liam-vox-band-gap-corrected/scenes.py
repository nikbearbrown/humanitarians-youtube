import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np
import math

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ── B01: Cold open — metal / semiconductor / insulator ──────────────────────

class LegacyOpeningThreeMaterials(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)

        title = Text("The Band Gap", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Three columns
        col_x = [-3.5, 0.0, 3.5]
        labels = ["METAL", "SEMI-\nCONDUCTOR", "INSULATOR"]
        gap_heights = [0.0, 0.6, 1.8]  # gap in scene units

        cols = VGroup()
        for x, lbl, gh in zip(col_x, labels, gap_heights):
            # Filled band (below)
            filled = Rectangle(width=1.8, height=1.4, color=TEAL,
                               fill_opacity=0.6, stroke_width=1
                               ).move_to(np.array([x, -0.8, 0.0]))
            # Empty band (above)
            empty = Rectangle(width=1.8, height=1.4, color=SLATE,
                              fill_opacity=0.2, stroke_width=1
                              ).move_to(np.array([x, -0.8 + 1.4 + gh, 0.0]))
            # Gap region (forbidden)
            if gh > 0:
                gap_rect = Rectangle(width=1.8, height=gh, color=CRIMSON,
                                     fill_opacity=0.15, stroke_width=0
                                     ).move_to(np.array([x, -0.8 + 1.4 + gh/2 - gh/2, 0.0]))
                cols.add(filled, empty, gap_rect)
            else:
                cols.add(filled, empty)
            # Label
            col_lbl = Text(lbl, font=DISPLAY, font_size=20,
                           color=INK, weight=BOLD).move_to(np.array([x, -2.5, 0.0]))
            cols.add(col_lbl)

        self.play(FadeIn(cols), run_time=1.2)
        self.wait(max(0.1, dur - 1.2))


# ── B02: Cold open — two standing waves, gap made visible ───────────────────

class B02_TwoStandingWaves(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)

        title = Text("Two Standing Waves, One Gap", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # ψ+ density (cos²): peaks at x = 0, a, 2a, ...
        x_vals = np.linspace(0, 2 * math.pi, 200)
        # Left panel: ψ+
        plus_curve = ParametricFunction(
            lambda t: np.array([t * 4.0 / (2 * math.pi) - 5.5,
                                math.cos(t) ** 2 * 1.4 - 0.4, 0.0]),
            t_range=[0, 2 * math.pi], color=TEAL, stroke_width=3)
        # Right panel: ψ-
        minus_curve = ParametricFunction(
            lambda t: np.array([t * 4.0 / (2 * math.pi) + 0.5,
                                math.sin(t) ** 2 * 1.4 - 0.4, 0.0]),
            t_range=[0, 2 * math.pi], color=CRIMSON, stroke_width=3)

        # Ion positions (dots) for ψ+
        ion_x = [t * 4.0 / (2 * math.pi) - 5.5 for t in [0, math.pi, 2 * math.pi]]
        ions_plus = VGroup(*[Dot(np.array([x, -0.4, 0.0]), radius=0.10, color=INK)
                              for x in ion_x])

        # Ion positions for ψ-
        ions_minus = VGroup(*[Dot(np.array([t * 4.0 / (2 * math.pi) + 0.5, -0.4, 0.0]),
                                  radius=0.10, color=INK)
                               for t in [0, math.pi, 2 * math.pi]])

        plus_lbl = Text("ψ₊: on ions", font=SERIF, font_size=22,
                        color=TEAL, slant=ITALIC).move_to(np.array([-3.5, 1.6, 0.0]))
        minus_lbl = Text("ψ₋: between ions", font=SERIF, font_size=22,
                         color=CRIMSON, slant=ITALIC).move_to(np.array([2.5, 1.6, 0.0]))
        gap_lbl = Text("gap", font=DISPLAY, font_size=26,
                       color=INK, weight=BOLD).move_to(np.array([0.0, -2.5, 0.0]))
        gap_arrow = DoubleArrow(np.array([0.0, -0.2, 0.0]),
                                np.array([0.0, -2.2, 0.0]),
                                buff=0, color=INK, stroke_width=2)

        self.play(
            Create(plus_curve), Create(minus_curve),
            FadeIn(ions_plus), FadeIn(ions_minus),
            run_time=1.0,
        )
        self.play(FadeIn(plus_lbl), FadeIn(minus_lbl), run_time=0.5)
        self.play(FadeIn(gap_arrow), FadeIn(gap_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.0 - 0.5 - 0.5))


class B03_ModelQuestion(Scene):
    def construct(self):
        dur = DUR.get("B03", 8.0)
        eyebrow = Text("THE QUESTION", font=MONO, font_size=18, color=CRIMSON).to_edge(UP)
        line1 = Text("Same free energy.", font=DISPLAY, font_size=34, color=INK)
        line2 = Text("Two standing waves.", font=DISPLAY, font_size=34, color=TEAL)
        line3 = Text("Why two crystal energies?", font=DISPLAY, font_size=34, color=INK)
        group = VGroup(line1, line2, line3).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        self.play(FadeIn(eyebrow), FadeIn(group), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B04: Free electron parabola ─────────────────────────────────────────────

class B04_FreeParabola(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)

        title = Text("Free Electrons: No Gap", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        ax = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 6.5, 2],
            x_length=8.0,
            y_length=5.0,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([0.0, -0.5, 0.0]))

        x_lbl = Text("k", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([4.2, -0.5, 0.0]))
        y_lbl = Text("E", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([-4.5, 2.3, 0.0]))

        self.play(FadeIn(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)

        parabola = ax.plot(lambda k: k ** 2, x_range=[-2.5, 2.5], color=TEAL,
                           stroke_width=3)
        self.play(Create(parabola), run_time=dur * 0.50)

        free_lbl = Text("E = ℏ²k²/2m", font=SERIF, font_size=24,
                        color=TEAL, slant=ITALIC).move_to(np.array([2.8, 1.5, 0.0]))
        all_lbl = Text("all energies allowed", font=SERIF, font_size=22,
                       color=INK, slant=ITALIC).move_to(np.array([0.0, -2.5, 0.0]))
        self.play(FadeIn(free_lbl), FadeIn(all_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.5 - dur * 0.50 - 0.5))


# ── B05: Zone boundary and Bragg coupling ────────────────────────────────────

class B05_ZoneBoundary(Scene):
    def construct(self):
        dur = DUR.get("B05", 11.0)

        title = Text("Bragg Reflection at the Zone Boundary", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        ax = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 6.5, 2],
            x_length=8.0,
            y_length=5.0,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([0.0, -0.5, 0.0]))

        x_lbl = Text("k", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([4.2, -0.5, 0.0]))
        y_lbl = Text("E", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([-4.5, 2.3, 0.0]))

        parabola = ax.plot(lambda k: k ** 2, x_range=[-2.5, 2.5], color=INK,
                           stroke_width=2, stroke_opacity=0.4)

        self.play(FadeIn(ax), FadeIn(x_lbl), FadeIn(y_lbl),
                  FadeIn(parabola), run_time=0.5)

        # Zone boundary at k = ±π/a ≈ ±1.0 in normalized units
        zone_line_r = DashedLine(np.array([2.0, -0.5, 0.0]),
                                 np.array([2.0, 2.5, 0.0]),
                                 color=CRIMSON, stroke_width=2, dash_length=0.15)
        zone_line_l = DashedLine(np.array([-2.0, -0.5, 0.0]),
                                 np.array([-2.0, 2.5, 0.0]),
                                 color=CRIMSON, stroke_width=2, dash_length=0.15)
        zone_lbl = Text("k = ±π/a", font=SERIF, font_size=22,
                        color=CRIMSON, slant=ITALIC).move_to(np.array([0.0, -2.0, 0.0]))

        self.play(Create(zone_line_r), Create(zone_line_l),
                  FadeIn(zone_lbl), run_time=0.6)

        # Bragg coupling arrow
        bragg_arrow = DoubleArrow(np.array([-1.8, 2.2, 0.0]),
                                  np.array([1.8, 2.2, 0.0]),
                                  buff=0, color=CRIMSON, stroke_width=2)
        bragg_lbl = Text("Bragg: λ = 2a", font=SERIF, font_size=22,
                         color=CRIMSON, slant=ITALIC).move_to(np.array([0.0, 2.5, 0.0]))

        self.play(Create(bragg_arrow), FadeIn(bragg_lbl), run_time=0.6)
        self.wait(max(0.1, dur - 0.5 - 0.6 - 0.6))


# ── B06: Two standing waves: ψ+ and ψ- ──────────────────────────────────────

class B06_StandingWaves(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)

        title = Text("Two Standing Waves", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Left panel: ψ+ = cos(πx/a), density = cos²
        # Right panel: ψ- = sin(πx/a), density = sin²
        n_periods = 3
        x_range_plus = np.linspace(0, n_periods * 2 * math.pi, 300)

        plus_curve = ParametricFunction(
            lambda t: np.array([t * 3.5 / (n_periods * 2 * math.pi) - 5.0,
                                math.cos(t / n_periods * n_periods) ** 2 * 1.6 - 0.5, 0.0]),
            t_range=[0, n_periods * 2 * math.pi], color=TEAL, stroke_width=3)

        minus_curve = ParametricFunction(
            lambda t: np.array([t * 3.5 / (n_periods * 2 * math.pi) + 0.5,
                                math.sin(t / n_periods * n_periods) ** 2 * 1.6 - 0.5, 0.0]),
            t_range=[0, n_periods * 2 * math.pi], color=CRIMSON, stroke_width=3)

        # Ion dots for both panels
        n_ions = n_periods + 1
        ions_plus = VGroup()
        ions_minus = VGroup()
        for i in range(n_ions):
            frac = i / n_periods
            x_p = frac * 3.5 - 5.0
            x_m = frac * 3.5 + 0.5
            ions_plus.add(Dot(np.array([x_p, -0.5, 0.0]), radius=0.10, color=INK))
            ions_minus.add(Dot(np.array([x_m, -0.5, 0.0]), radius=0.10, color=INK))

        plus_lbl = Text("ψ₊ = cos(πx/a)\n|ψ₊|² peaks ON ions",
                        font=SERIF, font_size=20, color=TEAL, slant=ITALIC
                        ).move_to(np.array([-3.2, 1.8, 0.0]))
        minus_lbl = Text("ψ₋ = sin(πx/a)\n|ψ₋|² peaks BETWEEN ions",
                         font=SERIF, font_size=20, color=CRIMSON, slant=ITALIC
                         ).move_to(np.array([2.3, 1.8, 0.0]))

        divider = Line(np.array([0.0, -2.0, 0.0]), np.array([0.0, 0.8, 0.0]),
                       color=SLATE, stroke_width=1, stroke_opacity=0.5)

        self.play(Create(plus_curve), FadeIn(ions_plus), run_time=0.8)
        self.play(Create(minus_curve), FadeIn(ions_minus), run_time=0.8)
        self.play(FadeIn(plus_lbl), FadeIn(minus_lbl), FadeIn(divider), run_time=0.5)
        self.wait(max(0.1, dur - 0.8 - 0.8 - 0.5))


# ── B07: Energy split — gap opens ────────────────────────────────────────────

class B07_GapOpens(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)

        title = Text("Weak periodic potential: a gap opens", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Degenerate level before split
        degen_line = DashedLine(np.array([-2.0, 0.5, 0.0]),
                                np.array([2.0, 0.5, 0.0]),
                                color=SLATE, stroke_width=2, dash_length=0.15)
        degen_lbl = Text("degenerate before lattice", font=SERIF, font_size=20,
                         color=SLATE, slant=ITALIC).move_to(np.array([0.0, 0.9, 0.0]))

        self.play(Create(degen_line), FadeIn(degen_lbl), run_time=0.5)

        # Split into ψ+ (lower, TEAL) and ψ- (higher, CRIMSON)
        plus_line = Line(np.array([-3.5, -1.2, 0.0]),
                         np.array([3.5, -1.2, 0.0]),
                         color=TEAL, stroke_width=4)
        minus_line = Line(np.array([-3.5, 2.2, 0.0]),
                          np.array([3.5, 2.2, 0.0]),
                          color=CRIMSON, stroke_width=4)

        plus_e_lbl = Text("E₊ = E₀ − |V_G|", font=SERIF, font_size=22,
                          color=TEAL, slant=ITALIC).move_to(np.array([-3.1, -0.8, 0.0]))
        minus_e_lbl = Text("E₋ = E₀ + |V_G|", font=SERIF, font_size=22,
                           color=CRIMSON, slant=ITALIC).move_to(np.array([-3.1, 2.6, 0.0]))

        self.play(
            Create(plus_line), FadeIn(plus_e_lbl),
            Create(minus_line), FadeIn(minus_e_lbl),
            run_time=dur * 0.40,
        )

        # Gap arrow
        gap_arrow = DoubleArrow(np.array([3.8, -1.2, 0.0]),
                                np.array([3.8, 2.2, 0.0]),
                                buff=0, color=INK, stroke_width=2)
        gap_lbl = Text("gap\n= 2|V_G|", font=DISPLAY, font_size=22,
                       color=INK, weight=BOLD).move_to(np.array([5.0, 0.5, 0.0]))

        plus_desc = Text("ψ₊ on ions → lower E", font=SERIF, font_size=20,
                         color=TEAL, slant=ITALIC).move_to(np.array([1.5, -1.7, 0.0]))
        minus_desc = Text("ψ₋ between ions → higher E", font=SERIF, font_size=20,
                          color=CRIMSON, slant=ITALIC).move_to(np.array([1.5, -2.5, 0.0]))

        self.play(Create(gap_arrow), FadeIn(gap_lbl),
                  FadeIn(plus_desc), FadeIn(minus_desc), run_time=0.6)
        self.wait(max(0.1, dur - 0.5 - dur * 0.40 - 0.6))


# ── B08: Band structure with gap ─────────────────────────────────────────────

class B08_BandStructure(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        title = Text("Two-state model: gap = 2|V_G|", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        ax = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 7.0, 2],
            x_length=8.0,
            y_length=5.5,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([0.0, -0.5, 0.0]))

        x_lbl = Text("k", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([4.2, -0.5, 0.0]))
        y_lbl = Text("E", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([-4.5, 2.5, 0.0]))

        self.play(FadeIn(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)

        # Lower band: parabola with flattening near k=±1 (zone boundary)
        # Use piecewise: below the gap
        lower_band = ax.plot(lambda k: k**2 - 0.6 * math.exp(-8*(abs(k)-1.0)**2),
                             x_range=[-2.0, 2.0], color=TEAL, stroke_width=3)
        # Upper band: parabola shifted up with gap
        upper_band = ax.plot(lambda k: k**2 + 1.2 * math.exp(-8*(abs(k)-1.0)**2),
                             x_range=[-2.0, 2.0], color=CRIMSON, stroke_width=3)

        self.play(Create(lower_band), run_time=dur * 0.30)
        self.play(Create(upper_band), run_time=dur * 0.30)

        # Gap at zone boundary label
        gap_annot = Text("gap = 2|V_G|", font=SERIF, font_size=22,
                         color=INK, slant=ITALIC).move_to(np.array([3.0, 2.0, 0.0]))
        strong_lbl = Text("valid near this crossing\nfor a weak periodic potential", font=SERIF, font_size=20,
                          color=SLATE, slant=ITALIC).move_to(np.array([0.0, -2.4, 0.0]))

        self.play(FadeIn(gap_annot), FadeIn(strong_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.4 - dur * 0.60 - 0.5))


# ── B09: Metal / semiconductor / insulator classification ────────────────────

class B09_Classification(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)

        title = Text("How bands help classify materials", font=DISPLAY, font_size=25,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        col_x = [-3.8, 0.0, 3.8]
        mat_labels = ["METAL", "SEMI-\nCONDUCTOR", "INSULATOR"]
        gap_sizes = [0.0, 0.7, 2.0]
        fermi_offsets = [0.7, -0.35, -0.35]   # Fermi level relative to valence top

        cols = VGroup()
        for x, lbl, gh, fo in zip(col_x, mat_labels, gap_sizes, fermi_offsets):
            valence_top = -0.3
            # Valence band (filled, TEAL)
            valence = Rectangle(width=2.0, height=2.0, color=TEAL,
                                fill_opacity=0.5, stroke_width=1
                                ).move_to(np.array([x, valence_top - 1.0, 0.0]))
            # Conduction band (empty, SLATE)
            cond_bot = valence_top + gh
            cond = Rectangle(width=2.0, height=2.0, color=SLATE,
                             fill_opacity=0.2, stroke_width=1
                             ).move_to(np.array([x, cond_bot + 1.0, 0.0]))
            # Gap fill
            if gh > 0:
                gap_fill = Rectangle(width=2.0, height=gh, color=CRIMSON,
                                     fill_opacity=0.2, stroke_width=0
                                     ).move_to(np.array([x, valence_top + gh/2, 0.0]))
                cols.add(valence, cond, gap_fill)
            else:
                cols.add(valence, cond)

            # Fermi level line
            fermi_y = valence_top + fo
            fermi = DashedLine(np.array([x - 0.9, fermi_y, 0.0]),
                               np.array([x + 0.9, fermi_y, 0.0]),
                               color=GOLD, stroke_width=2, dash_length=0.12)
            cols.add(fermi)
            # Labels
            mat_lbl = Text(lbl, font=DISPLAY, font_size=18, color=INK, weight=BOLD
                           ).move_to(np.array([x, -2.6, 0.0]))
            cols.add(mat_lbl)

        cols.scale(0.84).shift(DOWN * 0.35)
        self.play(FadeIn(cols), run_time=1.2)
        fermi_key = Text("— Fermi level", font=SERIF, font_size=20,
                         color=INK, slant=ITALIC).move_to(np.array([0.0, -3.2, 0.0]))
        self.play(FadeIn(fermi_key), run_time=0.4)
        self.wait(max(0.1, dur - 1.2 - 0.4))


# ── B10: Silicon example ──────────────────────────────────────────────────────

class B10_ToyModelExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)

        title = Text("Toy model — not a silicon calculation", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Simple schematic of a weak-potential two-state model
        valence = Rectangle(width=7.0, height=1.5, color=TEAL,
                            fill_opacity=0.5, stroke_width=2
                            ).move_to(np.array([0.0, -1.5, 0.0]))
        cond = Rectangle(width=7.0, height=1.5, color=SLATE,
                         fill_opacity=0.2, stroke_width=2
                         ).move_to(np.array([0.0, 0.75, 0.0]))
        gap_fill = Rectangle(width=7.0, height=1.1, color=CRIMSON,
                             fill_opacity=0.15, stroke_width=0
                             ).move_to(np.array([0.0, -0.05, 0.0]))

        valence_lbl = Text("Valence band (filled)", font=SERIF, font_size=20,
                           color=TEAL, slant=ITALIC).move_to(np.array([0.0, -1.5, 0.0]))
        cond_lbl = Text("Conduction band (empty)", font=SERIF, font_size=20,
                        color=SLATE, slant=ITALIC).move_to(np.array([0.0, 0.75, 0.0]))
        gap_lbl = Text("gap = 1.1 eV", font=DISPLAY, font_size=22,
                       color=CRIMSON, weight=BOLD).move_to(np.array([0.0, -0.05, 0.0]))

        self.play(FadeIn(valence), FadeIn(cond), FadeIn(gap_fill), run_time=0.5)
        self.play(FadeIn(valence_lbl), FadeIn(cond_lbl), FadeIn(gap_lbl), run_time=0.5)

        # Theory prediction
        theory_box = Rectangle(width=6.0, height=1.2, color=SLATE,
                               fill_opacity=0.08, stroke_width=1
                               ).move_to(np.array([0.0, -2.8, 0.0]))
        theory_lbl = Text("|V_G| = 0.55 eV  →  model gap = 1.10 eV",
                          font=SERIF, font_size=20, color=INK, slant=ITALIC
                          ).move_to(np.array([0.0, -2.8, 0.0]))
        self.play(FadeIn(theory_box), FadeIn(theory_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.5 - 0.5 - 0.5))


class B11_ModelRecap(Scene):
    def construct(self):
        dur = DUR.get("B11", 11.0)
        title = Text("THE MODEL CHAIN", font=DISPLAY, font_size=30, color=INK).to_edge(UP)
        items = ["zone-boundary degeneracy", "Bragg mixing", "two standing waves",
                 "different potential averages", "forbidden gap"]
        rows = VGroup(*[Text(x, font=SERIF, font_size=24,
                            color=TEAL if i == 4 else INK) for i, x in enumerate(items)])
        rows.arrange(DOWN, buff=0.32).move_to(ORIGIN)
        arrows = VGroup(*[Text("↓", font=DISPLAY, font_size=20, color=CRIMSON)
                          for _ in range(4)])
        for i, arrow in enumerate(arrows):
            arrow.move_to((rows[i].get_bottom() + rows[i + 1].get_top()) / 2)
        self.play(FadeIn(title), FadeIn(rows), FadeIn(arrows), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


class B12_YourTurn(Scene):
    def construct(self):
        dur = DUR.get("B12", 13.0)
        title = Text("YOUR TURN", font=DISPLAY, font_size=32, color=INK).to_edge(UP)
        prompt = Text("Weak-potential model", font=SERIF, font_size=26, color=INK)
        data = Text("|V_G| = 0.30 eV", font=SERIF, font_size=34, color=TEAL)
        ask = Text("What zone-boundary gap does the model predict?", font=SERIF,
                   font_size=25, color=INK)
        group = VGroup(prompt, data, ask).arrange(DOWN, buff=0.7).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(group), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


class B13_YourTurnAnswer(Scene):
    def construct(self):
        dur = DUR.get("B13", 9.0)
        title = Text("MODEL ANSWER", font=DISPLAY, font_size=30, color=INK).to_edge(UP)
        equation = Text("gap = 2|V_G| = 2(0.30 eV) = 0.60 eV",
                        font=SERIF, font_size=32, color=TEAL)
        scope = Text("This result is for the stated two-state weak-potential model.",
                     font=SERIF, font_size=22, color=SLATE, slant=ITALIC).next_to(equation, DOWN, buff=0.8)
        self.play(FadeIn(title), Write(equation), run_time=1.2)
        self.play(FadeIn(scope), run_time=0.5)
        self.wait(max(0.1, dur - 1.7))


class B14_CorrectTitleOutro(Scene):
    def construct(self):
        dur = DUR.get("B14", 5.0)
        self.camera.background_color = "#201F1C"
        title = Text("Where a Band Gap Comes From", font=DISPLAY,
                     font_size=34, color="#F2EFE8")
        credit = Text("Liam, in for Bear", font=SERIF, font_size=20,
                      color="#D97757").next_to(title, DOWN, buff=0.45)
        series = Text("QUANTUM MECHANICS  ·  VOLUME THREE", font=MONO,
                      font_size=14, color="#AAA49A").next_to(credit, DOWN, buff=0.35)
        self.play(FadeIn(title), FadeIn(credit), FadeIn(series), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))
