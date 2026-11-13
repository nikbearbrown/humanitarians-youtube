"""
Manim scenes for hussain-bond-pricing-duration (16:9 master)
B01_ProblemSetup    — cash-flow timeline + inverse price/yield indicator
B04_PriceYieldCurve — price-yield curve, par line, tangent (duration) at 5%
B07_ConvexityCompare — actual vs duration-only vs duration+convexity, +/-2% shocks

All bond math verified against the closed-form formulas (Hull; Fabozzi):
  price(y)      = sum(C/(1+y)^t) + F/(1+y)^T
  MacDur(y)     = sum(t*C/(1+y)^t + T*F/(1+y)^T) / price
  ModDur(y)     = MacDur / (1+y)
  Convexity(y)  = sum(t*(t+1)*C/(1+y)^(t+2) + T*(T+1)*F/(1+y)^(T+2)) / price
Bond: face=1000, coupon=5% annual, T=10 years.
"""
from manim import *

BG     = "#FAF9F5"
INK    = "#3D3929"
ACCENT = "#D97757"   # the one terracotta moment
MUTE   = "#B7AFA2"   # duration-only (the naive, superseded estimate)

FACE, COUPON, T = 1000.0, 50.0, 10


def price(ytm):
    cf = [COUPON / (1 + ytm) ** t for t in range(1, T + 1)]
    cf[-1] += FACE / (1 + ytm) ** T
    return sum(cf)


PY_PAIRS = [(y / 100, price(y / 100)) for y in range(2, 11)]
PAR_Y, MOD_DUR, CONVEXITY = 1000.0, 7.72, 75.0


def cream_label(txt, pos, font_size=20, color=INK):
    t = Text(txt, color=color, font_size=font_size).move_to(pos)
    bg = Rectangle(width=t.width + 0.18, height=t.height + 0.12,
                    fill_color=BG, fill_opacity=1, stroke_width=0).move_to(pos)
    return VGroup(bg, t)


class B01_ProblemSetup(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("A BOND IS A LOAN WITH A FIXED SCHEDULE", color=INK,
                      font_size=30, weight="BOLD").to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.8)

        # ---- cash-flow timeline: 9 coupons + final coupon+face ----
        axis = Line([-5.6, 0.3, 0], [5.6, 0.3, 0], color=INK, stroke_width=2)
        self.play(Create(axis), run_time=0.5)

        n = 10
        xs = [-5.0 + i * (10.0 / (n - 1)) for i in range(n)]
        arrows, labels = VGroup(), VGroup()
        for i, x in enumerate(xs):
            is_last = i == n - 1
            h = 1.6 if is_last else 0.7
            color = ACCENT if is_last else INK
            arrow = Arrow([x, 0.3, 0], [x, 0.3 + h, 0], color=color,
                           stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.15)
            arrows.add(arrow)
            txt = "$1,050" if is_last else "$50"
            labels.add(Text(txt, color=color, font_size=15).next_to(arrow, UP, buff=0.08))
        year_labels = VGroup(*[
            Text(f"yr {i+1}", color=INK, font_size=13).next_to([x, 0.3, 0], DOWN, buff=0.15)
            for i, x in enumerate(xs)
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08),
                   run_time=1.8)
        self.play(FadeIn(labels), FadeIn(year_labels), run_time=0.6)

        formula = Text(
            "Price = sum of  C / (1+y)^t  +  F / (1+y)^T",
            color=INK, font_size=30
        ).next_to(axis, DOWN, buff=1.3)
        self.play(Write(formula), run_time=1.0)

        # ---- inverse relationship indicator ----
        yield_up = VGroup(
            Text("yield", color=INK, font_size=20),
            Arrow([0, 0, 0], [0, 0.5, 0], color=ACCENT, stroke_width=4, buff=0),
        ).arrange(RIGHT, buff=0.15).move_to([-3.2, -3.0, 0])
        price_down = VGroup(
            Text("price", color=INK, font_size=20),
            Arrow([0, 0.5, 0], [0, 0, 0], color=ACCENT, stroke_width=4, buff=0),
        ).arrange(RIGHT, buff=0.15).move_to([3.2, -3.0, 0])
        verdict = Text("Duration measures how much.", color=INK, font_size=22,
                        weight="BOLD").move_to([0, -3.2, 0])
        self.play(FadeIn(yield_up), FadeIn(price_down), run_time=0.6)
        self.play(Write(verdict), run_time=0.6)
        self.wait(1.0)


class B04_PriceYieldCurve(Scene):
    def construct(self):
        self.camera.background_color = BG

        def to_x(ytm):
            return -5.0 + (ytm - 0.02) / 0.08 * 10.0

        def to_y(p):
            return -2.5 + (p - 650.0) / 700.0 * 5.0

        title = Text("BOND PRICE vs YIELD — DURATION", color=INK,
                      font_size=30, weight="BOLD").move_to([0, 3.15, 0])
        self.play(Write(title), run_time=0.7)

        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)
        par_y = to_y(PAR_Y)

        ticks = VGroup(
            cream_label("2%", [to_x(0.02), -2.9, 0], 18),
            cream_label("6%", [to_x(0.06), -2.9, 0], 18),
            cream_label("10%", [to_x(0.10), -2.9, 0], 18),
            cream_label("$693", [-5.7, to_y(692.77), 0], 16),
            cream_label("$1,000", [-5.8, par_y, 0], 17),
            cream_label("$1,269", [-5.7, to_y(1269.48), 0], 16),
        )
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(ticks), run_time=0.8)

        par_line = DashedLine((-5.0, par_y, 0), (5.0, par_y, 0), color=INK, dash_length=0.2,
                                stroke_width=1.5)
        par_label = cream_label("Par = $1,000", [3.0, par_y + 1.0, 0], 18)
        self.play(FadeIn(par_line), Write(par_label), run_time=0.6)

        pts = [[to_x(y), to_y(p), 0] for y, p in PY_PAIRS]
        curve = VGroup(*[Line(pts[i], pts[i + 1], color=INK, stroke_width=3)
                          for i in range(len(pts) - 1)])
        self.play(Create(curve), run_time=1.4)

        atm_x, atm_y = to_x(0.05), par_y
        atm_dot = Dot([atm_x, atm_y, 0], color=ACCENT, radius=0.09)
        atm_label = cream_label("YTM = 5%, P = $1,000", [atm_x + 1.5, atm_y + 1.1, 0], 20, ACCENT)
        self.play(FadeIn(atm_dot), Write(atm_label), run_time=0.6)

        # tangent slope in plot-space: dP/dy(real) = -ModDur*P ; scale to axes
        # real slope = -7.72 * 1000 = -7720 $/unit-yield; plot scale: dx=10/0.08, dy=5/700
        real_slope = -MOD_DUR * PAR_Y
        plot_slope = real_slope * (5.0 / 700.0) / (10.0 / 0.08)
        tan_x1, tan_x2 = atm_x - 3.0, atm_x + 3.0
        tan_y1 = atm_y - plot_slope * 3.0
        tan_y2 = atm_y + plot_slope * 3.0
        tangent = Line([tan_x1, tan_y1, 0], [tan_x2, tan_y2, 0], color=ACCENT, stroke_width=2.5)
        tangent_label = cream_label("tangent slope ≈ −7.72", [-3.6, 1.8, 0], 19, ACCENT)
        self.play(FadeIn(tangent), Write(tangent_label), run_time=0.6)
        self.wait(1.5)


class B07_ConvexityCompare(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("DURATION vs DURATION + CONVEXITY", color=INK,
                      font_size=28, weight="BOLD").to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.7)

        # rows: (label, actual, dur_only, dur_conv)
        rows = [
            ("Yield +2% (7%)", 859.53, 845.57, 860.56),
            ("Yield −2% (3%)", 1170.60, 1154.43, 1169.43),
        ]
        max_p = 1250.0
        bar_w = 5.4
        left_x = -5.6

        legend = VGroup(
            VGroup(Square(0.22, fill_color=INK, fill_opacity=1, stroke_width=0),
                   Text("actual", color=INK, font_size=18)).arrange(RIGHT, buff=0.12),
            VGroup(Square(0.22, fill_color=MUTE, fill_opacity=1, stroke_width=0),
                   Text("duration only", color=INK, font_size=18)).arrange(RIGHT, buff=0.12),
            VGroup(Square(0.22, fill_color=ACCENT, fill_opacity=1, stroke_width=0),
                   Text("duration + convexity", color=INK, font_size=18)).arrange(RIGHT, buff=0.12),
        ).arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(legend), run_time=0.5)

        y0 = 1.4
        for label, actual, dur_only, dur_conv in rows:
            row_label = Text(label, color=INK, font_size=22, weight="BOLD").move_to(
                [left_x + 0.4, y0 + 0.9, 0]).align_to([left_x, 0, 0], LEFT)
            self.play(Write(row_label), run_time=0.4)

            bars = [("actual", actual, INK), ("duration only", dur_only, MUTE),
                    ("duration + convexity", dur_conv, ACCENT)]
            for j, (name, val, color) in enumerate(bars):
                y = y0 + 0.4 - j * 0.55
                bg_bar = Rectangle(width=bar_w, height=0.4, fill_color=INK,
                                    fill_opacity=0.06, stroke_width=0).move_to(
                    [left_x + bar_w / 2, y, 0])
                w = bar_w * val / max_p
                bar = Rectangle(width=0.001, height=0.4, fill_color=color,
                                  fill_opacity=0.95, stroke_width=0).move_to(
                    [left_x, y, 0]).align_to(bg_bar, LEFT)
                val_label = Text(f"${val:,.2f}", color=color, font_size=17)
                self.add(bg_bar)
                self.play(bar.animate.stretch_to_fit_width(w, about_edge=LEFT),
                           run_time=0.5)
                val_label.next_to(bg_bar, RIGHT, buff=0.15)
                self.play(Write(val_label), run_time=0.2)
            y0 -= 2.3

        summary = Text("Convexity closes most of the gap — in both directions.",
                        color=INK, font_size=22, weight="BOLD").to_edge(DOWN, buff=0.65)
        self.play(Write(summary), run_time=0.6)
        self.wait(1.2)
