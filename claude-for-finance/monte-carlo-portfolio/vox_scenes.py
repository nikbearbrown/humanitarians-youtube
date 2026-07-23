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


class B04_PortfolioPaths(Scene):
    def construct(self):
        import numpy as np

        # ---- Generate paths INSIDE construct() ----
        rng_fixed = np.random.default_rng(42)
        n_paths, T_years, steps = 20, 30, 360
        dt = T_years / steps
        mu, sigma, V0 = 0.07, 0.15, 100000.0
        returns = (mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*rng_fixed.normal(0, 1, (n_paths, steps))
        paths = V0 * np.exp(np.cumsum(returns, axis=1))
        # sample at yearly intervals
        yearly = np.hstack([np.full((n_paths, 1), V0), paths[:, 11::12]])  # (20, 31)

        # clip terminal values for display
        y_max = 3e6

        def to_x(year):
            return -5.0 + (year / 30.0) * 10.0

        def to_y(val):
            y = -2.5 + (val / y_max) * 5.0
            return max(-2.5, min(2.5, y))

        # ---- Title ----
        title = Text("MONTE CARLO PORTFOLIO (N=10,000)", color=INK, font_size=30, weight=BOLD)
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
            cream_label("0",    [-5.0, -2.9, 0]),
            cream_label("10",   [to_x(10), -2.9, 0]),
            cream_label("20",   [to_x(20), -2.9, 0]),
            cream_label("30",   [ 5.0, -2.9, 0]),
            cream_label("$0",   [-5.3, -2.5, 0]),
            cream_label("$1.5M",[-5.4,  0.0, 0]),
            cream_label("$3M",  [-5.3,  2.5, 0]),
        )

        axis_labels = VGroup(
            Text("Years", color=SLATE, font_size=22).move_to([0, -3.1, 0]),
        )

        # ---- Sort paths by terminal value ----
        terminal_vals = yearly[:, -1]
        sorted_idx = np.argsort(terminal_vals)
        median_idx = sorted_idx[n_paths // 2]   # index 10
        p5_idx = sorted_idx[0]                  # lowest
        p95_idx = sorted_idx[-1]                # highest

        # ---- Build background paths (all except median) ----
        years = list(range(31))
        background_paths = []
        for i in range(n_paths):
            if i == median_idx:
                continue
            pts = [[to_x(yr), to_y(yearly[i, yr]), 0] for yr in years]
            segs = VGroup()
            for j in range(len(pts) - 1):
                segs.add(Line(pts[j], pts[j+1], color=SLATE, stroke_width=0.8, stroke_opacity=0.4))
            background_paths.append(segs)

        # ---- Median path ----
        med_pts = [[to_x(yr), to_y(yearly[median_idx, yr]), 0] for yr in years]
        med_segs = VGroup()
        for j in range(len(med_pts) - 1):
            med_segs.add(Line(med_pts[j], med_pts[j+1], color=CRIMSON, stroke_width=2.5))
        median_path = med_segs

        med_term_y = to_y(yearly[median_idx, -1])
        med_term_y_clamped = max(-2.3, min(2.3, med_term_y))
        median_label = cream_label("median", [5.4, med_term_y_clamped, 0], font_size=20, txt_color=CRIMSON)

        # ---- P5 path ----
        p5_pts = [[to_x(yr), to_y(yearly[p5_idx, yr]), 0] for yr in years]
        p5_segs = VGroup()
        for j in range(len(p5_pts) - 1):
            p5_segs.add(Line(p5_pts[j], p5_pts[j+1], color=CRIMSON, stroke_width=1.5, stroke_opacity=0.6))
        p5_path = p5_segs

        p5_term_y = to_y(yearly[p5_idx, -1])
        p5_term_y_clamped = max(-2.3, min(2.3, p5_term_y))

        # ---- P95 path ----
        p95_pts = [[to_x(yr), to_y(yearly[p95_idx, yr]), 0] for yr in years]
        p95_segs = VGroup()
        for j in range(len(p95_pts) - 1):
            p95_segs.add(Line(p95_pts[j], p95_pts[j+1], color=PASS_CLR, stroke_width=1.5, stroke_opacity=0.6))
        p95_path = p95_segs

        p95_term_y = to_y(yearly[p95_idx, -1])
        p95_term_y_clamped = max(-2.3, min(2.3, p95_term_y))

        # stagger labels if they overlap
        p5_label = cream_label("P5", [5.4, p5_term_y_clamped, 0], font_size=20, txt_color=CRIMSON)
        p95_label = cream_label("P95", [5.4, p95_term_y_clamped, 0], font_size=20, txt_color=PASS_CLR)

        verdict_text = cream_label("5% end below $200k", [2.5, -3.1, 0], font_size=22, txt_color=CRIMSON)

        # ---- Sequence (6 play() calls) ----
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(*[FadeIn(p) for p in background_paths])
        self.play(FadeIn(median_path), Write(median_label))
        self.play(FadeIn(p5_path), FadeIn(p95_path))
        self.play(Write(p5_label), Write(p95_label), Write(verdict_text))
