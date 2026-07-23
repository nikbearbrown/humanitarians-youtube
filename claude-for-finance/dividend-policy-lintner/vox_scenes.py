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


class B04_LintnerDividend(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"

        years = [2019, 2020, 2021, 2022, 2023]
        actual = [4.08, 4.24, 4.52, 4.76, 5.00]
        target = [3.80, 4.10, 4.40, 4.65, 4.90]
        predicted = [3.92, 4.12, 4.36, 4.62, 4.88]

        # y scale: $3.50 to $5.20, y_plot from -2.0 to 2.5
        y_min_val = 3.50; y_max_val = 5.20
        y_min_plot = -2.0; y_max_plot = 2.5
        y_scale = (y_max_plot - y_min_plot) / (y_max_val - y_min_val)
        y_base = y_min_plot

        def vy(v):
            return y_min_plot + (v - y_min_val) * y_scale

        # Bar positions
        bar_xs = [-3.6, -1.8, 0.0, 1.8, 3.6]
        bar_w = 1.2

        title = Text(
            "Lintner's Smoothing Model: Dividends Don't Lie",
            font="Georgia", font_size=20, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Axes
        x_axis = Line([-4.5, y_base, 0], [4.5, y_base, 0],
                      stroke_width=2, color=ManimColor(SLATE))
        y_axis = Line([-4.5, y_base, 0], [-4.5, y_max_plot + 0.2, 0],
                      stroke_width=2, color=ManimColor(SLATE))

        # y-ticks at $3.50, $4.00, $4.50, $5.00
        y_tick_vals = [3.50, 4.00, 4.50, 5.00]
        y_tick_labels = ["$3.50", "$4.00", "$4.50", "$5.00"]
        y_ticks = VGroup()
        for v, lbl in zip(y_tick_vals, y_tick_labels):
            ty = vy(v)
            tick = Line([-4.5, ty, 0], [-4.65, ty, 0], stroke_width=1, color=ManimColor(SLATE))
            bg = Rectangle(width=0.65, height=0.24, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([-5.05, ty, 0])
            lbl_obj = Text(lbl, font="Georgia", font_size=12, color=ManimColor(SLATE)
                           ).move_to([-5.05, ty, 0])
            y_ticks.add(VGroup(tick, bg, lbl_obj))

        axes = VGroup(x_axis, y_axis, y_ticks)

        # Bars
        bars = VGroup()
        for i, (bx, val) in enumerate(zip(bar_xs, actual)):
            bar_top = vy(val)
            bar_h = bar_top - y_base
            bar = Rectangle(
                width=bar_w, height=bar_h,
                fill_color=ManimColor(GOLD), fill_opacity=1.0,
                stroke_width=0, stroke_opacity=0
            ).move_to([bx, y_base + bar_h / 2, 0])
            # value label above bar
            val_bg = Rectangle(width=0.6, height=0.24, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([bx, bar_top + 0.2, 0])
            val_lbl = Text(f"${val:.2f}", font="Georgia", font_size=12, color=ManimColor(INK)
                           ).move_to([bx, bar_top + 0.2, 0])
            # year label below x-axis
            yr_bg = Rectangle(width=0.55, height=0.22, fill_color=ManimColor(CREAM),
                              fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                              ).move_to([bx, y_base - 0.2, 0])
            yr_lbl = Text(str(years[i]), font="Georgia", font_size=11, color=ManimColor(SLATE)
                          ).move_to([bx, y_base - 0.2, 0])
            bars.add(VGroup(bar, val_bg, val_lbl, yr_bg, yr_lbl))

        # Target line (CRIMSON dashed)
        target_pts = [[bar_xs[i], vy(target[i]), 0] for i in range(5)]
        target_segs = VGroup()
        for i in range(4):
            seg = Line(target_pts[i], target_pts[i+1], stroke_width=2, color=ManimColor(CRIMSON))
            seg.set_dash([0.12, 0.08])
            target_segs.add(seg)
        target_dots = VGroup(*[Dot(pt, radius=0.06, color=ManimColor(CRIMSON)) for pt in target_pts])
        target_group = VGroup(target_segs, target_dots)

        # Predicted line (SLATE solid)
        pred_pts = [[bar_xs[i], vy(predicted[i]), 0] for i in range(5)]
        pred_segs = VGroup()
        for i in range(4):
            seg = Line(pred_pts[i], pred_pts[i+1], stroke_width=2, color=ManimColor(SLATE))
            pred_segs.add(seg)
        pred_dots = VGroup(*[Dot(pt, radius=0.06, color=ManimColor(SLATE)) for pt in pred_pts])
        pred_group = VGroup(pred_segs, pred_dots)

        # Parameters box — moved to lower-right, away from target/predicted lines
        params_bg = Rectangle(width=2.4, height=0.75, fill_color=ManimColor(CREAM),
                              fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                              ).move_to([3.2, -0.8, 0])
        params_t1 = Text("Target payout: 72%", font="Georgia", font_size=11, color=ManimColor(INK)
                         ).move_to([3.2, -0.58, 0])
        params_t2 = Text("Smoothing s: 0.38", font="Georgia", font_size=11, color=ManimColor(INK)
                         ).move_to([3.2, -0.80, 0])
        params_t3 = Text("Sustain. EPS: $6.94", font="Georgia", font_size=11, color=ManimColor(INK)
                         ).move_to([3.2, -1.02, 0])
        params_box = VGroup(params_bg, params_t1, params_t2, params_t3)

        # Legend
        swatch_gold = Rectangle(width=0.3, height=0.22, fill_color=ManimColor(GOLD),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([-3.6, -2.65, 0])
        lbl_gold = Text("Actual dividend", font="Georgia", font_size=12, color=ManimColor(INK))
        lbl_gold.next_to(swatch_gold, RIGHT, buff=0.1)

        crim_dash = Line([-1.0, -2.65, 0], [-0.55, -2.65, 0],
                         stroke_width=2, color=ManimColor(CRIMSON))
        crim_dash.set_dash([0.1, 0.07])
        lbl_target = Text("Lintner target", font="Georgia", font_size=12, color=ManimColor(INK)
                          ).move_to([0.4, -2.65, 0])

        slate_line = Line([1.5, -2.65, 0], [1.95, -2.65, 0],
                          stroke_width=2, color=ManimColor(SLATE))
        lbl_pred = Text("Predicted", font="Georgia", font_size=12, color=ManimColor(INK)
                        ).move_to([2.7, -2.65, 0])

        legend = VGroup(swatch_gold, lbl_gold, crim_dash, lbl_target, slate_line, lbl_pred)

        # Verdict
        verdict_bg = Rectangle(width=4.0, height=0.28, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([0, -3.1, 0])
        verdict = Text(
            "Current EPS $6.65 > Sustainability $6.94 -- MONITOR",
            font="Georgia", font_size=13, color=ManimColor(INK)
        ).move_to([0, -3.1, 0])

        # Animation
        self.play(Write(title))                                     # 1
        self.play(Create(axes))                                     # 2
        self.play(FadeIn(bars))                                     # 3
        self.play(Create(target_group))                             # 4
        self.play(Create(pred_group))                               # 5
        self.play(FadeIn(legend), FadeIn(params_box))               # 6
        self.play(FadeIn(verdict_bg), FadeIn(verdict))              # 7
