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


# ── B01: Cold open — four levels split into three ────────────────────────────

class LegacyFourToThreeOpening(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)

        title = Text("Linear Stark Effect", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Four degenerate levels on left
        degen_y = 0.0
        left_x = -4.0
        right_x = 4.0

        # Four thin lines at left, same y
        level_labels = ["2s", "2p₀", "2p₊₁", "2p₋₁"]
        left_levels = VGroup()
        for i, lbl in enumerate(level_labels):
            line = Line(np.array([left_x, degen_y + i * 0.06 - 0.09, 0.0]),
                        np.array([left_x + 1.2, degen_y + i * 0.06 - 0.09, 0.0]),
                        color=INK, stroke_width=2)
            left_levels.add(line)

        degen_lbl = Text("4 states", font=SERIF, font_size=20, color=INK,
                         slant=ITALIC).move_to(np.array([left_x + 0.6, degen_y - 0.6, 0.0]))

        field_arrow = Arrow(np.array([0.0, -2.0, 0.0]),
                            np.array([0.0, 2.0, 0.0]),
                            buff=0, color=SLATE, stroke_width=2)
        field_lbl = Text("ε", font=SERIF, font_size=28, color=SLATE,
                         slant=ITALIC).move_to(np.array([0.3, 2.1, 0.0]))

        # Three lines on right (split)
        top_line = Line(np.array([right_x - 1.2, 1.5, 0.0]),
                        np.array([right_x, 1.5, 0.0]), color=CRIMSON, stroke_width=3)
        mid_line1 = Line(np.array([right_x - 1.2, 0.0, 0.0]),
                         np.array([right_x, 0.0, 0.0]), color=SLATE, stroke_width=5)
        mid_line2 = Line(np.array([right_x - 1.2, 0.08, 0.0]),
                         np.array([right_x, 0.08, 0.0]), color=SLATE, stroke_width=5)
        bot_line = Line(np.array([right_x - 1.2, -1.5, 0.0]),
                        np.array([right_x, -1.5, 0.0]), color=TEAL, stroke_width=3)

        top_lbl = Text("+3a₀eε", font=SERIF, font_size=18, color=CRIMSON,
                       slant=ITALIC).move_to(np.array([right_x + 1.2, 1.5, 0.0]))
        mid_lbl = Text("× 2", font=DISPLAY, font_size=20, color=SLATE,
                       weight=BOLD).move_to(np.array([right_x + 1.0, 0.04, 0.0]))
        bot_lbl = Text("−3a₀eε", font=SERIF, font_size=18, color=TEAL,
                       slant=ITALIC).move_to(np.array([right_x + 1.2, -1.5, 0.0]))

        self.play(FadeIn(left_levels), FadeIn(degen_lbl), run_time=0.5)
        self.play(FadeIn(field_arrow), FadeIn(field_lbl), run_time=0.4)

        self.play(
            Create(top_line), FadeIn(top_lbl),
            Create(mid_line1), Create(mid_line2), FadeIn(mid_lbl),
            Create(bot_line), FadeIn(bot_lbl),
            run_time=dur * 0.50,
        )
        self.wait(max(0.1, dur - 0.5 - 0.4 - dur * 0.50))


# ── B02: Cold open — lopsided clouds ─────────────────────────────────────────

class B02_LopsidedClouds(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)

        title = Text("Two Ways to Be Lopsided", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Nucleus dot
        nuc_l = Dot(np.array([-3.5, 0.0, 0.0]), radius=0.12, color=INK)
        nuc_r = Dot(np.array([3.5, 0.0, 0.0]), radius=0.12, color=INK)

        # Left: TEAL cloud — more density below (sum state, lower energy)
        cloud_l_top = Ellipse(width=1.6, height=0.9, color=TEAL,
                              fill_opacity=0.25, stroke_width=1
                              ).move_to(np.array([-3.5, 0.6, 0.0]))
        cloud_l_bot = Ellipse(width=2.0, height=1.4, color=TEAL,
                              fill_opacity=0.50, stroke_width=1
                              ).move_to(np.array([-3.5, -0.7, 0.0]))

        # Right: CRIMSON cloud — more density above (difference state, higher energy)
        cloud_r_top = Ellipse(width=2.0, height=1.4, color=CRIMSON,
                              fill_opacity=0.50, stroke_width=1
                              ).move_to(np.array([3.5, 0.7, 0.0]))
        cloud_r_bot = Ellipse(width=1.6, height=0.9, color=CRIMSON,
                              fill_opacity=0.25, stroke_width=1
                              ).move_to(np.array([3.5, -0.6, 0.0]))

        teal_lbl = Text("(|2s⟩+|2p₀⟩)/√2\nleans with field → low E",
                        font=SERIF, font_size=18, color=TEAL, slant=ITALIC
                        ).move_to(np.array([-3.5, -2.2, 0.0]))
        crimson_lbl = Text("(|2s⟩−|2p₀⟩)/√2\nleans against field → high E",
                           font=SERIF, font_size=18, color=CRIMSON, slant=ITALIC
                           ).move_to(np.array([3.5, -2.2, 0.0]))

        self.play(FadeIn(nuc_l), FadeIn(nuc_r), run_time=0.3)
        self.play(FadeIn(cloud_l_top), FadeIn(cloud_l_bot),
                  FadeIn(cloud_r_top), FadeIn(cloud_r_bot), run_time=0.8)
        self.play(FadeIn(teal_lbl), FadeIn(crimson_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.3 - 0.8 - 0.5))


# ── B04: The problem — four degenerate states ────────────────────────────────

class B04_FourDegenerate(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)

        title = Text("Ideal Coulomb model: four n=2 states", font=DISPLAY, font_size=27,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Four horizontal lines at same height
        line_y = 0.5
        level_data = [("2s", -3.2), ("2p₀", -1.0), ("2p₊₁", 1.0), ("2p₋₁", 3.2)]

        levels = VGroup()
        lbls = VGroup()
        for name, x in level_data:
            line = Line(np.array([x - 0.8, line_y, 0.0]),
                        np.array([x + 0.8, line_y, 0.0]),
                        color=INK, stroke_width=3)
            lbl = Text(name, font=DISPLAY, font_size=22, color=INK
                       ).move_to(np.array([x, line_y + 0.5, 0.0]))
            levels.add(line)
            lbls.add(lbl)

        energy_lbl = Text("−3.4 eV", font=SERIF, font_size=22, color=INK,
                          slant=ITALIC).move_to(np.array([5.0, line_y, 0.0]))
        degen_lbl = Text("all degenerate", font=SERIF, font_size=22,
                         color=CRIMSON, slant=ITALIC).move_to(np.array([0.0, -1.2, 0.0]))
        problem_lbl = Text("fine structure and Lamb shift omitted here",
                           font=SERIF, font_size=20, color=CRIMSON, slant=ITALIC
                           ).move_to(np.array([0.0, -2.2, 0.0]))

        self.play(LaggedStart(*[FadeIn(l) for l in levels],
                              lag_ratio=0.2, run_time=0.8))
        self.play(FadeIn(lbls), FadeIn(energy_lbl), run_time=0.4)
        self.play(FadeIn(degen_lbl), run_time=0.4)
        self.play(FadeIn(problem_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.8 - 0.4 - 0.4 - 0.4))


# ── B05: The 4×4 matrix ──────────────────────────────────────────────────────

class B05_Matrix4x4(Scene):
    def construct(self):
        dur = DUR.get("B05", 11.0)

        title = Text("Build the 4×4 Perturbation Matrix", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # 4×4 grid of squares
        cell_size = 1.1
        grid = VGroup()
        row_labels = ["⟨2s|", "⟨2p₀|", "⟨2p₊₁|", "⟨2p₋₁|"]
        col_labels = ["|2s⟩", "|2p₀⟩", "|2p₊₁⟩", "|2p₋₁⟩"]

        for i in range(4):
            for j in range(4):
                x = (j - 1.5) * cell_size
                y = (1.5 - i) * cell_size
                cell = Rectangle(width=cell_size * 0.9, height=cell_size * 0.9,
                                 color=SLATE, fill_opacity=0.1, stroke_width=1
                                 ).move_to(np.array([x, y, 0.0]))
                q = Text("?", font=DISPLAY, font_size=24, color=INK
                         ).move_to(np.array([x, y, 0.0]))
                grid.add(cell, q)

        # Row and column labels
        r_lbls = VGroup()
        c_lbls = VGroup()
        for i, rl in enumerate(row_labels):
            r_lbl = Text(rl, font=SERIF, font_size=18, color=INK,
                         slant=ITALIC).move_to(np.array([-2.5, (1.5 - i) * cell_size, 0.0]))
            r_lbls.add(r_lbl)
        for j, cl in enumerate(col_labels):
            c_lbl = Text(cl, font=SERIF, font_size=18, color=INK,
                         slant=ITALIC).move_to(np.array([(j - 1.5) * cell_size, 2.6, 0.0]))
            c_lbls.add(c_lbl)

        count_lbl = Text("16 integrals", font=DISPLAY, font_size=24,
                         color=CRIMSON, weight=BOLD).move_to(np.array([0.0, -2.5, 0.0]))

        self.play(FadeIn(grid), run_time=0.6)
        self.play(FadeIn(r_lbls), FadeIn(c_lbls), run_time=0.5)
        self.play(FadeIn(count_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.6 - 0.5 - 0.4))


# ── B06: symmetry filters the perturbation matrix ────────────────────────────

class B06_ParityKills(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)

        title = Text("Parity + Δm = 0 leave one coupling", font=DISPLAY, font_size=27,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        cell_size = 1.1
        # Hermitian pair: one independent real integral.
        surviving = {(0, 1), (1, 0)}

        cells = []
        for i in range(4):
            for j in range(4):
                x = (j - 1.5) * cell_size
                y = (1.5 - i) * cell_size
                is_surviving = (i, j) in surviving
                col = TEAL if is_surviving else SLATE
                opacity = 0.6 if is_surviving else 0.1
                cell = Rectangle(width=cell_size * 0.9, height=cell_size * 0.9,
                                 color=col, fill_opacity=opacity, stroke_width=1
                                 ).move_to(np.array([x, y, 0.0]))
                txt = Text("−3a₀" if is_surviving else "0", font=DISPLAY,
                           font_size=20 if is_surviving else 18,
                           color=TEAL if is_surviving else SLATE
                           ).move_to(np.array([x, y, 0.0]))
                cells.append(VGroup(cell, txt))

        grid = VGroup(*cells)

        parity_lbl = Text("parity: opposite parity required   ·   z symmetry: Δm = 0", font=SERIF,
                          font_size=20, color=INK, slant=ITALIC
                          ).move_to(np.array([0.0, -2.0, 0.0]))
        survive_lbl = Text("2 conjugate entries · 1 independent integral: −3a₀", font=SERIF,
                           font_size=20, color=TEAL, slant=ITALIC
                           ).move_to(np.array([0.0, -2.8, 0.0]))

        self.play(FadeIn(grid), run_time=0.8)
        self.play(FadeIn(parity_lbl), run_time=0.4)
        self.play(FadeIn(survive_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.8 - 0.4 - 0.4))


# ── B07: Three levels — good states ──────────────────────────────────────────

class B07_ThreeLevels(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)

        title = Text("Three Levels from Four States", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Level diagram
        left_x = -3.0
        right_x = 3.0

        # Degenerate on left
        for i in range(4):
            dline = Line(np.array([left_x - 0.8, 0.0 + i * 0.06 - 0.09, 0.0]),
                         np.array([left_x + 0.8, 0.0 + i * 0.06 - 0.09, 0.0]),
                         color=INK, stroke_width=2)
            self.add(dline)
        degen_lbl = Text("degenerate", font=SERIF, font_size=18,
                         color=SLATE, slant=ITALIC).move_to(np.array([left_x, -0.7, 0.0]))
        self.add(degen_lbl)

        # Fan lines from degen to split
        fan_top = Line(np.array([left_x + 0.8, 0.0, 0.0]),
                       np.array([right_x - 0.8, 1.8, 0.0]),
                       color=CRIMSON, stroke_width=1, stroke_opacity=0.4)
        fan_bot = Line(np.array([left_x + 0.8, 0.0, 0.0]),
                       np.array([right_x - 0.8, -1.8, 0.0]),
                       color=TEAL, stroke_width=1, stroke_opacity=0.4)

        # Three levels on right
        top_line = Line(np.array([right_x - 0.8, 1.8, 0.0]),
                        np.array([right_x + 0.8, 1.8, 0.0]),
                        color=CRIMSON, stroke_width=3)
        mid_lineA = Line(np.array([right_x - 0.8, 0.1, 0.0]),
                         np.array([right_x + 0.8, 0.1, 0.0]),
                         color=SLATE, stroke_width=4)
        mid_lineB = Line(np.array([right_x - 0.8, -0.1, 0.0]),
                         np.array([right_x + 0.8, -0.1, 0.0]),
                         color=SLATE, stroke_width=4)
        bot_line = Line(np.array([right_x - 0.8, -1.8, 0.0]),
                        np.array([right_x + 0.8, -1.8, 0.0]),
                        color=TEAL, stroke_width=3)

        top_e = Text("+3a₀eε", font=SERIF, font_size=18, color=CRIMSON,
                     slant=ITALIC).move_to(np.array([right_x + 1.8, 1.8, 0.0]))
        mid_e = Text("0 (×2)", font=SERIF, font_size=18, color=SLATE,
                     slant=ITALIC).move_to(np.array([right_x + 1.6, 0.0, 0.0]))
        bot_e = Text("−3a₀eε", font=SERIF, font_size=18, color=TEAL,
                     slant=ITALIC).move_to(np.array([right_x + 1.8, -1.8, 0.0]))

        top_state = Text("(|2s⟩−|2p₀⟩)/√2", font=SERIF, font_size=16,
                         color=CRIMSON, slant=ITALIC).move_to(np.array([right_x, 2.4, 0.0]))
        bot_state = Text("(|2s⟩+|2p₀⟩)/√2", font=SERIF, font_size=16,
                         color=TEAL, slant=ITALIC).move_to(np.array([right_x, -2.4, 0.0]))
        mid_state = Text("2p±1 (symmetric)", font=SERIF, font_size=16,
                         color=SLATE, slant=ITALIC).move_to(np.array([right_x, -0.7, 0.0]))

        self.play(FadeIn(fan_top), FadeIn(fan_bot), run_time=0.4)
        self.play(
            Create(top_line), Create(mid_lineA), Create(mid_lineB), Create(bot_line),
            run_time=dur * 0.40,
        )
        self.play(
            FadeIn(top_e), FadeIn(mid_e), FadeIn(bot_e),
            FadeIn(top_state), FadeIn(bot_state), FadeIn(mid_state),
            run_time=0.6,
        )
        self.wait(max(0.1, dur - 0.4 - dur * 0.40 - 0.6))


# ── B08: Lopsided clouds → permanent dipole ──────────────────────────────────

class B08_LopsidedDipole(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        title = Text("Lopsided Cloud = Permanent Dipole", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Field arrow (vertical)
        field_arr = Arrow(np.array([0.0, -2.8, 0.0]),
                          np.array([0.0, 2.8, 0.0]),
                          buff=0, color=SLATE, stroke_width=2)
        field_lbl = Text("ε", font=SERIF, font_size=28, color=SLATE,
                         slant=ITALIC).move_to(np.array([0.5, 2.7, 0.0]))

        # Left: TEAL — sum state — more density below (cloud heavier below)
        nuc_l = Dot(np.array([-3.0, 0.0, 0.0]), radius=0.12, color=INK)
        cl_top = Ellipse(width=1.4, height=0.8, color=TEAL,
                         fill_opacity=0.25, stroke_width=1
                         ).move_to(np.array([-3.0, 0.5, 0.0]))
        cl_bot = Ellipse(width=1.9, height=1.3, color=TEAL,
                         fill_opacity=0.55, stroke_width=1
                         ).move_to(np.array([-3.0, -0.6, 0.0]))
        l_lbl = Text("lower E\n−3a₀eε", font=SERIF, font_size=18, color=TEAL,
                     slant=ITALIC).move_to(np.array([-3.0, -2.2, 0.0]))

        # Right: CRIMSON — diff state — more density above
        nuc_r = Dot(np.array([3.0, 0.0, 0.0]), radius=0.12, color=INK)
        cr_top = Ellipse(width=1.9, height=1.3, color=CRIMSON,
                         fill_opacity=0.55, stroke_width=1
                         ).move_to(np.array([3.0, 0.6, 0.0]))
        cr_bot = Ellipse(width=1.4, height=0.8, color=CRIMSON,
                         fill_opacity=0.25, stroke_width=1
                         ).move_to(np.array([3.0, -0.5, 0.0]))
        r_lbl = Text("higher E\n+3a₀eε", font=SERIF, font_size=18, color=CRIMSON,
                     slant=ITALIC).move_to(np.array([3.0, -2.2, 0.0]))

        self.play(FadeIn(field_arr), FadeIn(field_lbl), run_time=0.4)
        self.play(FadeIn(nuc_l), FadeIn(nuc_r),
                  FadeIn(cl_top), FadeIn(cl_bot),
                  FadeIn(cr_top), FadeIn(cr_bot), run_time=0.8)
        self.play(FadeIn(l_lbl), FadeIn(r_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.4 - 0.8 - 0.4))


# ── B09: Linear vs quadratic Stark ───────────────────────────────────────────

class B09_LinearVsQuadratic(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)

        title = Text("Ideal limit: degenerate → linear; 1s → quadratic", font=DISPLAY,
                     font_size=24, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Left panel: n=2 linear split
        ax_l = Axes(
            x_range=[0, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=4.5,
            y_length=3.8,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([-3.0, -0.3, 0.0]))

        upper_l = ax_l.plot(lambda e: e, x_range=[0, 2.0], color=CRIMSON, stroke_width=3)
        lower_l = ax_l.plot(lambda e: -e, x_range=[0, 2.0], color=TEAL, stroke_width=3)
        mid_l = ax_l.plot(lambda e: 0.0, x_range=[0, 2.0], color=SLATE,
                          stroke_width=4, stroke_opacity=0.6)

        x_l_lbl = Text("ε", font=SERIF, font_size=22, color=INK, slant=ITALIC
                       ).move_to(np.array([-0.7, -0.3, 0.0]))
        panel_l_lbl = Text("n=2: linear", font=SERIF, font_size=20,
                           color=INK, slant=ITALIC).move_to(np.array([-3.0, -2.5, 0.0]))

        # Right panel: n=1 quadratic (tiny)
        ax_r = Axes(
            x_range=[0, 2.5, 1],
            y_range=[-0.5, 0.5, 0.5],
            x_length=4.5,
            y_length=3.8,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([3.0, -0.3, 0.0]))

        quad_r = ax_r.plot(lambda e: -0.2 * e**2, x_range=[0, 2.2], color=SLATE,
                           stroke_width=3)
        x_r_lbl = Text("ε", font=SERIF, font_size=22, color=INK, slant=ITALIC
                       ).move_to(np.array([5.3, -0.3, 0.0]))
        panel_r_lbl = Text("n=1: quadratic\n(much smaller)", font=SERIF,
                           font_size=20, color=INK, slant=ITALIC
                           ).move_to(np.array([3.0, -2.5, 0.0]))

        self.play(FadeIn(ax_l), FadeIn(ax_r), run_time=0.4)
        self.play(Create(upper_l), Create(lower_l), Create(mid_l),
                  Create(quad_r), run_time=dur * 0.50)
        self.play(FadeIn(x_l_lbl), FadeIn(x_r_lbl),
                  FadeIn(panel_l_lbl), FadeIn(panel_r_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.4 - dur * 0.50 - 0.5))


# ── B10: Example — numerical splitting ───────────────────────────────────────

class B10_NumericalExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)

        title = Text("At ε = 10⁵ V/cm: ±16 meV Shift", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        ax = Axes(
            x_range=[0, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=8.0,
            y_length=5.5,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([0.0, -0.5, 0.0]))

        x_lbl = Text("ε (arb)", font=SERIF, font_size=22, color=INK, slant=ITALIC
                     ).move_to(np.array([4.3, -0.5, 0.0]))
        y_lbl = Text("ΔE", font=SERIF, font_size=22, color=INK, slant=ITALIC
                     ).move_to(np.array([-4.6, 2.2, 0.0]))

        self.play(FadeIn(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)

        upper = ax.plot(lambda e: e, x_range=[0, 2.0], color=CRIMSON, stroke_width=3)
        middle = ax.plot(lambda e: 0.0, x_range=[0, 2.0], color=SLATE,
                         stroke_width=5, stroke_opacity=0.7)
        lower = ax.plot(lambda e: -e, x_range=[0, 2.0], color=TEAL, stroke_width=3)

        self.play(Create(upper), Create(middle), Create(lower), run_time=dur * 0.40)

        # Mark at ε=1 (illustrative = 10⁵ V/cm)
        dot_top = Dot(ax.c2p(1.0, 1.0), radius=0.10, color=CRIMSON)
        dot_bot = Dot(ax.c2p(1.0, -1.0), radius=0.10, color=TEAL)
        lbl_top = Text("+16 meV", font=DISPLAY, font_size=20,
                       color=CRIMSON).move_to(np.array([2.5, 2.0, 0.0]))
        lbl_bot = Text("−16 meV", font=DISPLAY, font_size=20,
                       color=TEAL).move_to(np.array([2.5, -2.0, 0.0]))
        bright_lbl = Text("energy shifts only — not line intensities", font=SERIF, font_size=20,
                          color=SLATE, slant=ITALIC).move_to(np.array([-1.2, 0.4, 0.0]))

        self.play(FadeIn(dot_top), FadeIn(dot_bot),
                  FadeIn(lbl_top), FadeIn(lbl_bot),
                  FadeIn(bright_lbl), run_time=0.6)
        self.wait(max(0.1, dur - 0.4 - dur * 0.40 - 0.6))


class B03_StarkQuestion(Scene):
    def construct(self):
        dur = DUR.get("B03", 8.0)
        title = Text("THE QUESTION", font=MONO, font_size=18, color=CRIMSON).to_edge(UP)
        lines = VGroup(
            Text("Which matrix elements survive?", font=DISPLAY, font_size=33, color=INK),
            Text("Why does one independent coupling", font=DISPLAY, font_size=30, color=INK),
            Text("control the first-order split?", font=DISPLAY, font_size=30, color=TEAL),
        ).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(lines), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


class B11_SpectrumCaveat(Scene):
    def construct(self):
        dur = DUR.get("B11", 12.0)
        title = Text("ENERGY LEVELS ≠ AUTOMATIC LINE INTENSITIES", font=DISPLAY,
                     font_size=25, color=INK).to_edge(UP)
        left = Text("Model gives", font=SERIF, font_size=24, color=TEAL)
        left_items = Text("3 first-order energies\n2-fold unshifted level", font=SERIF,
                          font_size=23, color=INK, line_spacing=1.3).next_to(left, DOWN, buff=0.4)
        right = Text("Spectra also need", font=SERIF, font_size=24, color=CRIMSON)
        right_items = Text("transitions · populations\npolarization · geometry", font=SERIF,
                           font_size=23, color=INK, line_spacing=1.3).next_to(right, DOWN, buff=0.4)
        lg = VGroup(left, left_items).move_to(LEFT * 3)
        rg = VGroup(right, right_items).move_to(RIGHT * 3)
        self.play(FadeIn(title), FadeIn(lg), FadeIn(rg), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


class B12_YourTurn(Scene):
    def construct(self):
        dur = DUR.get("B12", 12.0)
        title = Text("YOUR TURN", font=DISPLAY, font_size=32, color=INK).to_edge(UP)
        prompt = Text("If the electric field is cut in half,", font=SERIF, font_size=29, color=INK)
        ask = Text("what happens to ΔE = ±3a₀eℰ?", font=SERIF, font_size=31, color=TEAL)
        group = VGroup(prompt, ask).arrange(DOWN, buff=0.7).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(group), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


class B13_YourTurnAnswer(Scene):
    def construct(self):
        dur = DUR.get("B13", 8.0)
        title = Text("ANSWER: THE SHIFT IS HALVED", font=DISPLAY, font_size=29, color=INK).to_edge(UP)
        eq = Text("ℰ → ℰ/2   ⇒   ΔE → ΔE/2", font=SERIF, font_size=38, color=TEAL)
        note = Text("The two signs remain; m = ±1 stays unshifted at first order.",
                    font=SERIF, font_size=22, color=SLATE).next_to(eq, DOWN, buff=0.7)
        self.play(FadeIn(title), Write(eq), FadeIn(note), run_time=1.2)
        self.wait(max(0.1, dur - 1.2))


class B14_CorrectTitleOutro(Scene):
    def construct(self):
        dur = DUR.get("B14", 5.0)
        self.camera.background_color = "#201F1C"
        title = Text("Four States, Three First-Order Energies", font=DISPLAY,
                     font_size=32, color="#F2EFE8")
        credit = Text("Kore, in for Humanitarians AI", font=SERIF, font_size=20,
                      color="#D97757").next_to(title, DOWN, buff=0.45)
        series = Text("QUANTUM MECHANICS  ·  VOLUME THREE", font=MONO,
                      font_size=14, color="#AAA49A").next_to(credit, DOWN, buff=0.35)
        self.play(FadeIn(title), FadeIn(credit), FadeIn(series), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))
