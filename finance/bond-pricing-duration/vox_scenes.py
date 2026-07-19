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


class B04_PriceYieldCurve(Scene):
    def construct(self):
        # Coordinate mapping:
        # x: YTM in [0.02, 0.10] -> x_plot = -5.0 + (YTM-0.02)/0.08*10
        # y: price in [600, 1500] -> y_plot = -2.5 + (price-600)/900*5.0

        def to_x(ytm):
            return -5.0 + (ytm - 0.02) / 0.08 * 10.0

        def to_y(price):
            return -2.5 + (price - 600.0) / 900.0 * 5.0

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

        # ---- Title ----
        title = Text("BOND PRICE vs YIELD — DURATION", color=INK, font_size=32, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # ---- Axes ----
        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)

        # to_y(1000) = -2.5 + 400/900*5 = -2.5 + 2.222 = -0.278
        par_y = to_y(1000)

        tick_labels = VGroup(
            cream_label("2%",   [to_x(0.02), -2.9, 0]),
            cream_label("6%",   [to_x(0.06), -2.9, 0]),
            cream_label("10%",  [to_x(0.10), -2.9, 0]),
            cream_label("$600", [-5.4, to_y(600),  0]),
            cream_label("$1000",[-5.6, par_y,       0]),
            cream_label("$1400",[-5.6, to_y(1400), 0]),
        )

        axis_labels = VGroup(
            Text("YTM", color=SLATE, font_size=22).move_to([-3.5, -3.1, 0]),
            Text("Price ($)", color=SLATE, font_size=18).move_to([-5.6, 1.5, 0]),
        )

        # ---- Par value line ----
        par_line = DashedLine((-5.0, par_y, 0), (5.0, par_y, 0),
                              color=SLATE, dash_length=0.2)
        par_label = cream_label("Par = $1,000", [3.5, par_y + 0.3, 0], font_size=22, txt_color=SLATE)

        # ---- Price-yield curve (pre-computed) ----
        PY_PAIRS = [
            (0.02, 1404), (0.03, 1213), (0.04, 1081), (0.05, 1000),
            (0.06, 926),  (0.07, 859),  (0.08, 799),  (0.09, 744), (0.10, 692)
        ]
        py_pts = [[to_x(ytm), to_y(price), 0] for ytm, price in PY_PAIRS]
        curve_segs = VGroup()
        for i in range(len(py_pts) - 1):
            curve_segs.add(Line(py_pts[i], py_pts[i+1], color=CRIMSON, stroke_width=3))
        price_yield_curve = curve_segs

        # ---- Tangent line at YTM=5% ----
        # slope in plot space = -0.34 (pre-computed approximation)
        atm_px, atm_py = to_x(0.05), par_y  # (0.0, -0.278)
        slope = -0.34
        # tangent from x=-4 to x=4
        tan_x1, tan_x2 = -4.0, 4.0
        tan_y1 = atm_py - slope * (atm_px - tan_x1)  # = -0.278 + 0.34*4 = 1.082
        tan_y2 = atm_py + slope * (tan_x2 - atm_px)  # = -0.278 - 0.34*4 = -1.638
        tangent_line = Line((tan_x1, tan_y1, 0), (tan_x2, tan_y2, 0),
                            color=GOLD, stroke_width=2.5)
        tangent_label = cream_label("Duration approx.", [-2.8, 1.5, 0], font_size=22, txt_color=SLATE)

        # ---- ATM dot ----
        atm_dot = Dot([atm_px, atm_py, 0], color=CRIMSON)
        atm_label = cream_label("YTM=5%, P=$1000", [1.5, atm_py + 0.45, 0], font_size=22, txt_color=CRIMSON)

        verdict_text = cream_label("ModDur 7.7: 1% yield rise -> ~7.7% price drop",
                                   [1.5, -3.1, 0], font_size=19, txt_color=INK)

        # ---- Sequence (7 play() calls) ----
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(FadeIn(par_line), Write(par_label))
        self.play(Create(price_yield_curve))
        self.play(FadeIn(atm_dot), Write(atm_label))
        self.play(FadeIn(tangent_line), Write(tangent_label))
        self.play(Write(verdict_text))
