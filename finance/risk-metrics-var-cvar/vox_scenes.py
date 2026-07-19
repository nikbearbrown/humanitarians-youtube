import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_ReturnHistogram(Scene):
    def construct(self):
        import numpy as np

        # ---- Generate returns INSIDE construct() ----
        rng_fixed = np.random.default_rng(123)
        returns = rng_fixed.normal(0.0003, 0.01, 10000)

        # ---- Histogram with 30 bins from -4% to 4% ----
        bin_edges = np.linspace(-0.04, 0.04, 31)
        counts, _ = np.histogram(returns, bins=bin_edges)
        max_count = float(counts.max())
        bin_width_data = 0.08 / 30.0

        # VaR thresholds
        var_95 = float(np.percentile(returns, 5))   # approx -0.01621
        var_99 = float(np.percentile(returns, 1))   # approx -0.02296

        def ret_to_x(ret):
            return -5.0 + (ret + 0.04) / 0.08 * 10.0

        def count_to_y(count):
            return -2.5 + (count / max_count) * 5.0

        x_var95 = ret_to_x(var_95)
        x_var99 = ret_to_x(var_99)

        # ---- Title ----
        title = Text("VAR AND CVAR — RETURN DISTRIBUTION", color=INK, font_size=30, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # ---- Axes ----
        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)

        def cream_label(txt, pos, font_size=20, txt_color=INK):
            t = Text(txt, color=txt_color, font_size=font_size)
            t.move_to(pos)
            bg = Rectangle(
                width=t.width + 0.18, height=t.height + 0.12,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bg.move_to(pos)
            return VGroup(bg, t)

        tick_labels = VGroup(
            cream_label("-4%", [-5.0, -2.9, 0]),
            cream_label("0%",  [ 0.0, -2.9, 0]),
            cream_label("+4%", [ 5.0, -2.9, 0]),
        )

        axis_labels = VGroup(
            Text("Daily Return", color=SLATE, font_size=20).move_to([-3.0, -3.1, 0]),
        )

        # ---- Build histogram bars ----
        plot_bar_width = 10.0 / 30.0  # in plot units
        normal_bars = []
        tail_bars = []

        for i in range(30):
            edge_l = bin_edges[i]
            edge_r = bin_edges[i + 1]
            bin_center_data = (edge_l + edge_r) / 2.0
            x_center = ret_to_x(bin_center_data)
            bar_h = count_to_y(counts[i]) - (-2.5)
            if bar_h <= 0:
                continue
            bar_y_center = -2.5 + bar_h / 2.0
            rect = Rectangle(
                width=plot_bar_width,
                height=bar_h,
                stroke_width=0, stroke_opacity=0,
            )
            rect.move_to([x_center, bar_y_center, 0])
            if edge_r <= var_95:
                rect.set_fill(CRIMSON, opacity=1.0)
                tail_bars.append(rect)
            else:
                rect.set_fill(SLATE, opacity=0.7)
                normal_bars.append(rect)

        # ---- VaR lines ----
        var95_line = DashedLine((x_var95, -2.5, 0), (x_var95, 2.5, 0),
                                color=CRIMSON, stroke_width=2)
        var95_label = cream_label("95% VaR", [x_var95 - 0.8, 2.0, 0], font_size=22, txt_color=CRIMSON)

        var99_line = DashedLine((x_var99, -2.5, 0), (x_var99, 2.5, 0),
                                color="#800000", stroke_width=2)
        var99_label = cream_label("99% VaR", [x_var99 - 0.9, 1.3, 0], font_size=22, txt_color="#800000")

        verdict_text = cream_label("CVaR: expected loss GIVEN a bad day",
                                   [1.0, -3.1, 0], font_size=22, txt_color=CRIMSON)

        # ---- Sequence (6 play() calls) ----
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(*[FadeIn(bar) for bar in normal_bars])
        self.play(*[FadeIn(bar) for bar in tail_bars])
        self.play(FadeIn(var95_line), Write(var95_label), FadeIn(var99_line), Write(var99_label))
        self.play(Write(verdict_text))
