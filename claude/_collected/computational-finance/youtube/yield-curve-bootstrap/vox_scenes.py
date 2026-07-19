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


class B04_YieldCurve(Scene):
    def construct(self):
        # Coordinate mapping:
        # x: maturity in [0,11] -> x_plot = -5.0 + (mat/11)*10
        # y: zero rate in [0.03,0.07] -> y_plot = -2.5 + (rate-0.03)/0.04*5

        def to_x(mat):
            return -5.0 + (mat / 11.0) * 10.0

        def to_y(rate):
            return -2.5 + (rate - 0.03) / 0.04 * 5.0

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

        # Pre-computed zero rates
        ZERO_RATES = [(1, 0.0352), (2, 0.0408), (3, 0.0462), (5, 0.0542), (10, 0.0628)]

        # ---- Title ----
        title = Text("BOOTSTRAPPED YIELD CURVE", color=INK, font_size=34, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # ---- Axes ----
        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)

        tick_labels = VGroup(
            cream_label("0",   [-5.0, -2.9, 0]),
            cream_label("5",   [to_x(5), -2.9, 0]),
            cream_label("10",  [to_x(10), -2.9, 0]),
            cream_label("3%",  [-5.3, to_y(0.03), 0]),
            cream_label("5%",  [-5.3, to_y(0.05), 0]),
            cream_label("7%",  [-5.3, to_y(0.07), 0]),
        )

        axis_labels = VGroup(
            Text("Maturity (years)", color=SLATE, font_size=20).move_to([-4.0, -3.1, 0]),
            Text("Zero Rate", color=SLATE, font_size=20).move_to([-5.6, 0.5, 0]),
        )

        # ---- Bond yield dots (slightly below zero rate dots) ----
        bond_yield_dots = VGroup()
        for mat, rate in ZERO_RATES:
            px, py = to_x(mat), to_y(rate) - 0.12
            d = Dot(radius=0.10, color=SLATE, fill_opacity=0.6)
            d.move_to([px, py, 0])
            bond_yield_dots.add(d)

        # ---- Zero rate dots ----
        zero_rate_dots = VGroup()
        zero_pts = []
        for mat, rate in ZERO_RATES:
            px, py = to_x(mat), to_y(rate)
            d = Dot(radius=0.14, color=CRIMSON)
            d.move_to([px, py, 0])
            zero_rate_dots.add(d)
            zero_pts.append([px, py, 0])

        # ---- Yield curve segments (one per pair of dots) ----
        yield_curve_segs = []
        for i in range(len(zero_pts) - 1):
            seg = Line(zero_pts[i], zero_pts[i+1], color=CRIMSON, stroke_width=3)
            yield_curve_segs.append(seg)

        # ---- Key labels ----
        z1_pos = zero_pts[0]
        z10_pos = zero_pts[-1]
        z1_label = cream_label("z1=3.52%", [z1_pos[0] + 0.4, z1_pos[1] - 0.55, 0], font_size=20, txt_color=CRIMSON)
        z10_label = cream_label("z10=6.28%", [z10_pos[0] - 0.8, z10_pos[1] + 0.4, 0], font_size=20, txt_color=CRIMSON)

        verdict_text = cream_label("Upward slope: longer maturities demand higher rates",
                                   [2.5, -3.1, 0], font_size=18, txt_color=INK)

        # ---- Sequence (7 play() calls) ----
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(*[FadeIn(d) for d in bond_yield_dots])
        self.play(*[FadeIn(d) for d in zero_rate_dots])
        self.play(*[Create(seg) for seg in yield_curve_segs])
        self.play(Write(z1_label), Write(z10_label))
        self.play(Write(verdict_text))
