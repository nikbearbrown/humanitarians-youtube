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


class B04_PrimeFactorTimer(Scene):
    def construct(self):
        import math

        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=max(len(txt)*0.12, 0.3)+0.12, height=0.32,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # Title
        title = Text(
            "PRIME FACTORIZATION — THE RSA ASYMMETRY",
            font_size=26, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Log scale: log10(microseconds), 0→9 maps to y=-2.5→2.5
        # y = -2.5 + (log_val / 9.0) * 5.0

        def log_y(microseconds):
            if microseconds <= 0:
                return -2.5
            lv = math.log10(microseconds)
            return -2.5 + (lv / 9.0) * 5.0

        SIZES = ["3-digit", "5-digit", "7-digit", "9-digit"]
        GROUP_X = [-3.5, -1.0, 1.5, 4.0]

        MULTIPLY_US = [5, 8, 12, 15]
        FACTOR_US   = [1000, 50000, 5000000, 300000000]
        RATIOS      = ["200x", "6,250x", "416k x", "20B x"]

        BAR_W = 0.7
        BOTTOM_Y = -2.5

        x_axis_line = Line((-5.5,-2.5,0),(5.5,-2.5,0), color=INK, stroke_width=1.5)

        # y-tick labels — "1μs" is at log_y(1)=-2.5 which sits on x-axis; raise it 0.2
        y_lbl_1us  = tick_label("1μs",  (-5.4, log_y(1)+0.2,    0), fontsize=14)
        y_lbl_1ms  = tick_label("1ms",  (-5.4, log_y(1000),     0), fontsize=14)
        y_lbl_1s   = tick_label("1s",   (-5.4, log_y(1000000),  0), fontsize=14)
        y_lbl_5min = tick_label("5min", (-5.4, log_y(300000000),0), fontsize=14)
        y_tick_labels = VGroup(y_lbl_1us, y_lbl_1ms, y_lbl_1s, y_lbl_5min)

        # y-axis label
        y_ax_bg = Rectangle(width=2.5, height=0.32, fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0).move_to((-5.2,0,0))
        y_ax_txt = Text("Time (log)", font_size=17, color=SLATE).move_to((-5.2,0,0))
        y_axis_label = VGroup(y_ax_bg, y_ax_txt)

        # x-tick labels (group labels)
        x_tick_labels = VGroup(*[
            tick_label(s, (GROUP_X[i], -2.85, 0), fontsize=15)
            for i, s in enumerate(SIZES)
        ])

        # Build bars
        multiply_bars = VGroup()
        factor_bars   = VGroup()

        for i, gx in enumerate(GROUP_X):
            mul_us  = MULTIPLY_US[i]
            fac_us  = FACTOR_US[i]

            mul_y_top = log_y(mul_us)
            mul_h = mul_y_top - BOTTOM_Y
            mul_h = max(mul_h, 0.05)
            mul_bar = Rectangle(
                width=BAR_W, height=mul_h,
                fill_color=PASS_CLR, fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0
            ).move_to((gx - BAR_W/2 - 0.05, BOTTOM_Y + mul_h/2, 0))
            multiply_bars.add(mul_bar)

            fac_y_top = log_y(fac_us)
            fac_h = fac_y_top - BOTTOM_Y
            fac_h = max(fac_h, 0.05)
            fac_bar = Rectangle(
                width=BAR_W, height=fac_h,
                fill_color=CRIMSON, fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0
            ).move_to((gx + BAR_W/2 + 0.05, BOTTOM_Y + fac_h/2, 0))
            factor_bars.add(fac_bar)

        # Ratio labels above each factor bar
        ratio_labels = VGroup()
        for i, gx in enumerate(GROUP_X):
            fac_us  = FACTOR_US[i]
            fac_y_top = log_y(fac_us)
            lbl = tick_label(RATIOS[i], (gx + BAR_W/2 + 0.05, fac_y_top + 0.22, 0),
                             fontsize=14, color=CRIMSON)
            ratio_labels.add(lbl)

        # Legend (top-left area)
        leg_y = 2.6
        leg_x0 = -5.0
        leg_mul_rect = Rectangle(width=0.45, height=0.28, fill_color=PASS_CLR, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0).move_to((leg_x0, leg_y, 0))
        leg_mul_txt = Text("Multiply", font_size=15, color=INK).move_to((leg_x0+0.85, leg_y, 0))
        leg_fac_rect = Rectangle(width=0.45, height=0.28, fill_color=CRIMSON, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0).move_to((leg_x0+2.0, leg_y, 0))
        leg_fac_txt = Text("Factor", font_size=15, color=INK).move_to((leg_x0+2.85, leg_y, 0))
        legend = VGroup(leg_mul_rect, leg_mul_txt, leg_fac_rect, leg_fac_txt)

        # Verdict
        verdict_bg = Rectangle(width=9.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0,-3.15,0))
        verdict_txt = Text("Multiplication: O(n^2) -- Factorization: exponential",
                           font_size=22, color=CRIMSON, weight=BOLD).move_to((0,-3.15,0))
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # --- Sequence (7 play() calls) ---
        self.play(Write(title))
        self.play(
            FadeIn(x_axis_line),
            FadeIn(y_tick_labels),
            FadeIn(x_tick_labels),
            FadeIn(y_axis_label)
        )
        self.play(FadeIn(legend))
        self.play(*[GrowFromEdge(b, DOWN) for b in multiply_bars])
        self.play(*[GrowFromEdge(b, DOWN) for b in factor_bars])
        self.play(*[Write(r) for r in ratio_labels])
        self.play(Write(verdict_text))
        self.wait(1)
