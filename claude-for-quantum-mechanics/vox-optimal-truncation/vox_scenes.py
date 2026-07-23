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


# ── B01: COLD OPEN — student runs corrections, each smaller ──────────────────
class B01_TermsConverging(Scene):
    def construct(self):
        dur = DUR.get("B01", 8.0)
        title = Text("Quartic oscillator corrections", font=DISPLAY,
                     font_size=32, color=INK).move_to(UP * 3.0)
        # show 8 bars shrinking (illustrative values from the example seed)
        values = [0.18, 0.12, 0.035, 0.015, 0.006, 0.002, 0.0005, 0.0001]
        bar_w = 0.55
        gap = 0.10
        total_w = len(values) * (bar_w + gap) - gap
        bars = VGroup()
        labels = VGroup()
        for i, v in enumerate(values):
            h = v * 18  # scale for visibility; tallest = 0.18*18 = 3.24 units
            h = max(h, 0.08)
            b = Rectangle(width=bar_w, height=h, fill_color=TEAL, fill_opacity=1,
                          stroke_width=0)
            b.move_to(RIGHT * (i * (bar_w + gap) - total_w / 2 + bar_w / 2) + UP * (h / 2 - 2.0))
            bars.add(b)
            lbl = Text(str(i + 1), font=MONO, font_size=18, color=INK)
            lbl.move_to(b.get_bottom() + DOWN * 0.25)
            labels.add(lbl)
        x_label = Text("Term number", font=SERIF, font_size=22, color=INK,
                       slant=ITALIC).move_to(DOWN * 3.2)
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(bars), run_time=dur * 0.55)
        self.play(FadeIn(labels), FadeIn(x_label), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B02: COLD OPEN — term 11 explodes ───────────────────────────────────────
class B02_TermsExplode(Scene):
    def construct(self):
        dur = DUR.get("B02", 8.0)
        values_good = [0.18, 0.12, 0.035, 0.015, 0.006, 0.002, 0.0005, 0.0001]
        values_bad = [0.003, 0.04, 0.28, 1.6]
        bar_w = 0.45
        gap = 0.08
        n_total = len(values_good) + len(values_bad)
        total_w = n_total * (bar_w + gap) - gap
        bars = VGroup()
        for i, v in enumerate(values_good):
            h = max(v * 18, 0.08)
            b = Rectangle(width=bar_w, height=h, fill_color=TEAL, fill_opacity=1,
                          stroke_width=0)
            b.move_to(RIGHT * (i * (bar_w + gap) - total_w / 2 + bar_w / 2) + UP * (h / 2 - 2.5))
            bars.add(b)
        self.add(bars)
        # Add the exploding bars one by one
        for j, v in enumerate(values_bad):
            i = len(values_good) + j
            h = max(v * 4.0, 0.08)
            h = min(h, 5.8)
            b = Rectangle(width=bar_w, height=h, fill_color=CRIMSON, fill_opacity=1,
                          stroke_width=0)
            b.move_to(RIGHT * (i * (bar_w + gap) - total_w / 2 + bar_w / 2) + UP * (h / 2 - 2.5))
            self.play(GrowFromEdge(b, DOWN), run_time=dur * 0.18)
        explode_label = Text("Blows up!", font=DISPLAY, font_size=30, color=CRIMSON)
        explode_label.move_to(RIGHT * 2.5 + UP * 2.2)
        self.play(FadeIn(explode_label), run_time=dur * 0.10)
        self.wait(dur * 0.10)


# ── B03: THE QUESTION — card beat (no scene class needed, CARD type) ─────────
# CARD type, no scene class


# ── B04: THE PROBLEM — power series expansion idea ──────────────────────────
class B04_PowerSeries(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        title = Text("Energy as a power series in lambda", font=DISPLAY,
                     font_size=30, color=INK).move_to(UP * 3.0)
        # Show the expansion schematically as labeled terms
        terms = ["E(0)", "   +lambda E(1)", "   +lambda^2 E(2)", "   +lambda^3 E(3)", "   + ..."]
        colors = [INK, TEAL, TEAL, TEAL, INK]
        line = VGroup()
        x_pos = -5.0
        for term_str, col in zip(terms, colors):
            t = Text(term_str, font=MONO, font_size=26, color=col)
            t.move_to(RIGHT * x_pos + t.width / 2 * RIGHT)
            x_pos += t.width + 0.1
            line.add(t)
        line.move_to(ORIGIN)
        arrow = Arrow(start=UP * 1.0, end=DOWN * 0.8, color=CRIMSON, buff=0.1,
                      stroke_width=3)
        arrow.move_to(RIGHT * 3.0)
        small_label = Text("Smaller when lambda < 1", font=SERIF, font_size=22,
                           color=CRIMSON, slant=ITALIC).next_to(arrow, RIGHT, buff=0.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(line), run_time=dur * 0.50)
        self.play(GrowArrow(arrow), FadeIn(small_label), run_time=dur * 0.30)
        self.wait(dur * 0.20)


# ── B05: THE PROBLEM — convergence expectation ───────────────────────────────
class B05_ConvergencePromise(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        # Partial sums converging to a limit
        partial_sums = [0.82, 0.94, 0.975, 0.990, 0.996, 0.998, 0.9985, 0.9986]
        exact = 1.0
        dots = VGroup()
        for i, s in enumerate(partial_sums):
            x = -4.0 + i * 1.0
            y = (s - 0.9) * 20 - 2.0  # scale to visible range
            d = Dot(point=RIGHT * x + UP * y, radius=0.12, color=TEAL)
            dots.add(d)
        # Dashed horizontal line at exact = 1.0 -> y = (1.0-0.9)*20-2.0 = 0.0
        limit_line = DashedLine(start=LEFT * 4.5 + UP * 0.0,
                                end=RIGHT * 4.5 + UP * 0.0,
                                color=INK, stroke_width=1.5, dash_length=0.15)
        limit_label = Text("exact value", font=SERIF, font_size=22, color=INK,
                           slant=ITALIC).move_to(RIGHT * 5.2 + UP * 0.35)
        x_axis = Line(LEFT * 4.8, RIGHT * 4.8, color=INK, stroke_width=1.5).move_to(DOWN * 2.5)
        self.play(Create(x_axis), Create(limit_line), FadeIn(limit_label), run_time=0.5)
        self.play(Create(dots), run_time=dur * 0.60)
        arrow_in = Arrow(start=dots[-1].get_center() + UP * 0.5,
                         end=limit_line.get_center() + RIGHT * 3.0,
                         color=TEAL, buff=0.05, stroke_width=2)
        self.play(GrowArrow(arrow_in), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B07: THE MECHANISM — flip coupling negative ──────────────────────────────
class B07_FlipCoupling(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        axes = Axes(x_range=[-3.0, 3.0, 1.0], y_range=[-2.0, 6.0, 1.0],
                    x_length=7.0, y_length=5.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        # Positive lambda potential (stable parabola + quartic)
        lam_pos = 0.15
        curve_pos = axes.plot(lambda x: 0.5 * x**2 + lam_pos * x**4,
                              color=TEAL, stroke_width=3)
        label_pos = Text("+lambda (stable)", font=SERIF, font_size=22, color=TEAL,
                         slant=ITALIC).move_to(RIGHT * 4.0 + UP * 1.8)
        self.play(Create(axes), run_time=0.4)
        self.play(Create(curve_pos), FadeIn(label_pos), run_time=dur * 0.40)
        # Negative lambda (unstable)
        lam_neg = -0.15
        curve_neg = axes.plot(lambda x: 0.5 * x**2 + lam_neg * x**4,
                              x_range=[-2.8, 2.8], color=CRIMSON, stroke_width=3)
        label_neg = Text("-lambda (unstable)", font=SERIF, font_size=22, color=CRIMSON,
                         slant=ITALIC).move_to(RIGHT * 3.8 + DOWN * 0.5)
        self.play(Create(curve_neg), FadeIn(label_neg), run_time=dur * 0.40)
        self.wait(dur * 0.20)


# ── B08: THE MECHANISM — no ground state for negative lambda ─────────────────
class B08_NoGroundState(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        # Show negative-lambda potential dipping to -infinity at edges
        axes = Axes(x_range=[-3.2, 3.2, 1.0], y_range=[-5.0, 3.0, 1.0],
                    x_length=7.5, y_length=5.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        lam_neg = -0.2
        curve = axes.plot(lambda x: 0.5 * x**2 + lam_neg * x**4,
                          x_range=[-3.0, 3.0], color=CRIMSON, stroke_width=3)
        escape_arrow_l = Arrow(start=axes.c2p(-2.2, -1.5), end=axes.c2p(-3.0, -4.5),
                               color=CRIMSON, stroke_width=3, buff=0)
        escape_arrow_r = Arrow(start=axes.c2p(2.2, -1.5), end=axes.c2p(3.0, -4.5),
                               color=CRIMSON, stroke_width=3, buff=0)
        label = Text("Particle escapes to infinity", font=DISPLAY,
                     font_size=28, color=CRIMSON).move_to(UP * 2.8)
        self.play(Create(axes), run_time=0.4)
        self.play(Create(curve), run_time=dur * 0.35)
        self.play(GrowArrow(escape_arrow_l), GrowArrow(escape_arrow_r), run_time=dur * 0.30)
        self.play(FadeIn(label), run_time=dur * 0.15)
        self.wait(dur * 0.20)


# ── B09: THE MECHANISM — singularity on negative axis ────────────────────────
class B09_Singularity(Scene):
    def construct(self):
        dur = DUR.get("B09", 11.0)
        # Real lambda axis with singularity marked
        axis = NumberLine(x_range=[-4.0, 4.0, 1.0], length=8.0,
                          include_numbers=False, color=INK, stroke_width=2)
        axis.move_to(ORIGIN)
        zero_dot = Dot(axis.n2p(0), color=INK, radius=0.1)
        zero_lbl = Text("0", font=MONO, font_size=24, color=INK).next_to(zero_dot, DOWN, buff=0.2)
        sing_dot = Dot(axis.n2p(-2.5), color=CRIMSON, radius=0.16)
        sing_lbl = Text("singularity", font=SERIF, font_size=22, color=CRIMSON,
                        slant=ITALIC).next_to(sing_dot, UP, buff=0.25)
        pos_region = Line(axis.n2p(0), axis.n2p(3.8), color=TEAL, stroke_width=5)
        pos_lbl = Text("Taylor series lives here", font=SERIF, font_size=20,
                       color=TEAL, slant=ITALIC).move_to(np.array([2.0, 0.7, 0.0]))
        radius_brace = BraceBetweenPoints(axis.n2p(0), axis.n2p(-2.5), direction=DOWN)
        radius_lbl = Text("radius of convergence = 0", font=SERIF, font_size=20,
                          color=CRIMSON, slant=ITALIC).next_to(radius_brace, DOWN, buff=0.2)
        lambda_lbl = Text("lambda", font=SERIF, font_size=24, color=INK,
                          slant=ITALIC).next_to(axis, RIGHT, buff=0.2)
        self.play(Create(axis), FadeIn(zero_dot), FadeIn(zero_lbl), FadeIn(lambda_lbl),
                  run_time=0.5)
        self.play(Create(pos_region), FadeIn(pos_lbl), run_time=dur * 0.30)
        self.play(FadeIn(sing_dot), FadeIn(sing_lbl), run_time=dur * 0.25)
        self.play(Create(radius_brace), FadeIn(radius_lbl), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B10: THE MECHANISM — factorial growth ────────────────────────────────────
class B10_FactorialGrowth(Scene):
    def construct(self):
        dur = DUR.get("B10", 10.0)
        # Two curves: lambda^k (shrinking) and k! * lambda^k (eventually blowing up)
        axes = Axes(x_range=[0, 14, 2], y_range=[0, 3.5, 0.5],
                    x_length=8.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.5)
        lam = 0.05
        import math
        pts_lam = [(k, min(lam**k * 15, 3.4)) for k in range(1, 14)]
        pts_fact = [(k, min(math.factorial(k) * lam**k, 3.4)) for k in range(1, 14)]
        path_lam = axes.plot_line_graph([p[0] for p in pts_lam],
                                         [p[1] for p in pts_lam],
                                         line_color=TEAL, stroke_width=3,
                                         add_vertex_dots=True,
                                         vertex_dot_radius=0.07,
                                         vertex_dot_style={"color": TEAL})
        path_fact = axes.plot_line_graph([p[0] for p in pts_fact],
                                          [p[1] for p in pts_fact],
                                          line_color=CRIMSON, stroke_width=3,
                                          add_vertex_dots=True,
                                          vertex_dot_radius=0.07,
                                          vertex_dot_style={"color": CRIMSON})
        lbl_lam = Text("lambda^k (shrinking)", font=SERIF, font_size=20, color=TEAL,
                       slant=ITALIC).move_to(RIGHT * 3.0 + UP * 2.8)
        lbl_fact = Text("k! * lambda^k (eventually explodes)", font=SERIF,
                        font_size=20, color=CRIMSON, slant=ITALIC).move_to(RIGHT * 1.5 + DOWN * 2.8)
        x_label = Text("Term k", font=SERIF, font_size=20, color=INK,
                       slant=ITALIC).next_to(axes, RIGHT, buff=0.15)
        self.play(Create(axes), FadeIn(x_label), run_time=0.4)
        self.play(Create(path_lam), FadeIn(lbl_lam), run_time=dur * 0.40)
        self.play(Create(path_fact), FadeIn(lbl_fact), run_time=dur * 0.40)
        self.wait(dur * 0.20)


# ── B11: THE MECHANISM — crossover point ─────────────────────────────────────
class B11_Crossover(Scene):
    def construct(self):
        dur = DUR.get("B11", 11.0)
        axes = Axes(x_range=[0, 14, 2], y_range=[0, 3.5, 0.5],
                    x_length=8.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.5)
        import math
        lam = 0.05
        pts_term = [(k, min(math.factorial(k) * lam**k, 3.4)) for k in range(1, 14)]
        path_term = axes.plot_line_graph([p[0] for p in pts_term],
                                          [p[1] for p in pts_term],
                                          line_color=INK, stroke_width=3,
                                          add_vertex_dots=True,
                                          vertex_dot_radius=0.07,
                                          vertex_dot_style={"color": INK})
        # Crossover at k ~ 8 (1/lam = 20, but for lam=0.05 the crossover is around k=8-10)
        cross_k = 8
        cross_pt = axes.c2p(cross_k, min(math.factorial(cross_k) * lam**cross_k, 3.4))
        cross_dot = Dot(cross_pt, radius=0.14, color=GOLD)
        cross_dot.set_fill(GOLD, 1).set_stroke(INK, width=1.5)
        cross_lbl = Text("crossover (N*)", font=SERIF, font_size=22, color=INK,
                         slant=ITALIC).next_to(cross_dot, UP, buff=0.3)
        shrink_arrow = Arrow(start=axes.c2p(2, 2.5), end=axes.c2p(cross_k - 1, 0.5),
                             color=TEAL, stroke_width=2, buff=0.1)
        grow_arrow = Arrow(start=axes.c2p(cross_k + 1, 0.5), end=axes.c2p(12, 2.8),
                           color=CRIMSON, stroke_width=2, buff=0.1)
        self.play(Create(axes), run_time=0.4)
        self.play(Create(path_term), run_time=dur * 0.35)
        self.play(FadeIn(cross_dot), FadeIn(cross_lbl), run_time=dur * 0.20)
        self.play(GrowArrow(shrink_arrow), GrowArrow(grow_arrow), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B12: THE MECHANISM — U-shaped error curve ────────────────────────────────
class B12_UCurve(Scene):
    def construct(self):
        dur = DUR.get("B12", 12.0)
        axes = Axes(x_range=[0, 16, 2], y_range=[0, 3.5, 0.5],
                    x_length=8.5, y_length=5.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        # U-shaped curve: descends, hits minimum at N*, rises steeply
        import math
        def error_curve(k):
            # Synthetic U-shaped error curve
            if k == 0:
                return 3.0
            val = 3.0 * math.exp(-k * 0.4) + 0.003 * math.factorial(min(k, 12)) * (0.05 ** k)
            return min(val, 3.4)
        n_star = 8
        ks = list(range(0, 16))
        es = [error_curve(k) for k in ks]
        curve = axes.plot_line_graph(ks, es, line_color=INK, stroke_width=3,
                                     add_vertex_dots=False)
        # Highlight the minimum
        min_pt = axes.c2p(n_star, error_curve(n_star))
        min_dot = Dot(min_pt, radius=0.15, color=GOLD)
        min_dot.set_fill(GOLD, 1).set_stroke(INK, width=1.5)
        min_lbl = Text("N* (optimal)", font=DISPLAY, font_size=26, color=INK)
        min_lbl.next_to(min_dot, UP + RIGHT, buff=0.3)
        x_lbl = Text("Truncation order N", font=SERIF, font_size=20, color=INK,
                     slant=ITALIC).next_to(axes, RIGHT, buff=0.1)
        y_lbl = Text("Error", font=SERIF, font_size=20, color=INK,
                     slant=ITALIC).next_to(axes, UP + LEFT * 4.0, buff=0.1)
        teal_region = axes.get_area(
            axes.plot(lambda x: error_curve(int(round(x))), x_range=[0, n_star], color=TEAL),
            x_range=[0, n_star], color=TEAL, opacity=0.15)
        crimson_region = axes.get_area(
            axes.plot(lambda x: error_curve(min(int(round(x)), 14)), x_range=[n_star, 15], color=CRIMSON),
            x_range=[n_star, 15], color=CRIMSON, opacity=0.15)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(curve), run_time=dur * 0.40)
        self.play(FadeIn(teal_region), FadeIn(crimson_region), run_time=dur * 0.20)
        self.play(FadeIn(min_dot), FadeIn(min_lbl), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B13: THE MECHANISM — card beat (CARD type) — no scene class needed ────────


# ── B15: THE IMPLICATION — QED accuracy ──────────────────────────────────────
class B15_QEDAccuracy(Scene):
    def construct(self):
        dur = DUR.get("B15", 10.0)
        # Simple comparison: QED prediction vs experiment
        title = Text("QED: prediction vs. experiment", font=DISPLAY,
                     font_size=32, color=INK).move_to(UP * 3.0)
        pred_lbl = Text("QED prediction", font=SERIF, font_size=26, color=TEAL,
                        slant=ITALIC).move_to(LEFT * 2.5 + UP * 0.8)
        exp_lbl = Text("Experiment", font=SERIF, font_size=26, color=INK,
                       slant=ITALIC).move_to(RIGHT * 2.5 + UP * 0.8)
        pred_val = Text("1.001 159 652 180 73", font=MONO, font_size=28,
                        color=TEAL).move_to(LEFT * 2.5 + DOWN * 0.3)
        exp_val = Text("1.001 159 652 180 73", font=MONO, font_size=28,
                       color=INK).move_to(RIGHT * 2.5 + DOWN * 0.3)
        match_lbl = Text("12 decimal places", font=DISPLAY, font_size=30,
                         color=TEAL).move_to(DOWN * 1.8)
        divider = Line(UP * 1.5, DOWN * 0.8, color=INK, stroke_width=1.5).move_to(ORIGIN)
        highlight = Rectangle(width=5.6, height=0.55, fill_color=GOLD, fill_opacity=0.35,
                              stroke_width=0).move_to(DOWN * 1.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(pred_lbl), FadeIn(exp_lbl), Create(divider), run_time=dur * 0.20)
        self.play(FadeIn(pred_val), FadeIn(exp_val), run_time=dur * 0.30)
        self.play(divider.animate.scale(1.05), run_time=dur * 0.05)
        self.play(FadeIn(match_lbl), FadeIn(highlight), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B16: THE EXAMPLE — illustrative student numbers ──────────────────────────
class B16_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B16", 14.0)
        title = Text("Illustrative: lambda = 0.05", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.0)
        subtitle = Text("(invented numbers, labeled illustrative)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.45)
        terms_good = ["1: 0.82", "2: 0.94", "3: 0.975", "4: 0.990",
                      "5: 0.996", "6: 0.998", "7: 0.9985", "8: 0.9986"]
        terms_bad = ["9: 1.002", "10: 1.015", "11: 1.07", "12: 1.4"]
        col_g = VGroup()
        for i, t in enumerate(terms_good):
            lbl = Text(t, font=MONO, font_size=22, color=TEAL)
            lbl.move_to(LEFT * 3.5 + UP * (1.5 - i * 0.45))
            col_g.add(lbl)
        col_b = VGroup()
        for i, t in enumerate(terms_bad):
            lbl = Text(t, font=MONO, font_size=22, color=CRIMSON)
            lbl.move_to(RIGHT * 2.0 + UP * (1.5 - i * 0.45))
            col_b.add(lbl)
        optimal_lbl = Text("STOP HERE (N*=8)", font=DISPLAY, font_size=24,
                           color=INK).move_to(LEFT * 3.5 + DOWN * 2.5)
        star_line = Line(LEFT * 1.0 + DOWN * 2.0, RIGHT * 4.5 + DOWN * 2.0,
                         color=INK, stroke_width=1.5)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(Create(col_g), run_time=dur * 0.35)
        self.play(Create(col_b), run_time=dur * 0.25)
        self.play(Create(star_line), FadeIn(optimal_lbl), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B17: RECAP — card beat (CARD type) — no scene class needed ───────────────
