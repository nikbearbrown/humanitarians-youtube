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


class B04_CallPriceCurve(Scene):
    def construct(self):
        # ---- Title ----
        title = Text("BLACK-SCHOLES CALL PRICE", color=INK, font_size=34, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # ---- Axes ----
        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)

        # helper: make a labeled text with CREAM bg
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

        # x-tick labels at y=-2.9
        tick_labels = VGroup(
            cream_label("S=60",  [-5.0, -2.9, 0]),
            cream_label("S=100", [ 0.0, -2.9, 0]),
            cream_label("S=140", [ 5.0, -2.9, 0]),
            cream_label("$0",    [-5.25, -2.5, 0]),
            cream_label("$22",   [-5.25,  0.0, 0]),
            cream_label("$45",   [-5.25,  2.5, 0]),
        )

        # axis labels — keep y-label at readable position, no overlap with y-ticks
        x_axis_label = Text("Spot Price (S)", color=SLATE, font_size=22)
        x_axis_label.move_to([0, -3.3, 0])
        # y-axis label: rotate it and place inside safe area
        y_axis_label = Text("Call Price ($)", color=SLATE, font_size=18)
        y_axis_label.rotate(1.5708)  # 90 degrees
        y_axis_label.move_to([-5.7, 0, 0])
        axis_labels = VGroup(x_axis_label, y_axis_label)

        # ---- Strike line at K=100 (x=0) ----
        strike_line = DashedLine((0.0, -2.5, 0), (0.0, 3.0, 0),
                                 color=SLATE, stroke_width=1, dash_length=0.15)
        strike_label = cream_label("K=100", [0.6, 2.75, 0], font_size=22, txt_color=SLATE)

        # ---- Payoff (intrinsic value) hockey stick ----
        flat_seg = Line((-5.0, -2.5, 0), (0.0, -2.5, 0),
                        color=SLATE, stroke_width=2, stroke_opacity=0.6)
        rise_seg = Line((0.0, -2.5, 0), (5.0, 1.94, 0),
                        color=SLATE, stroke_width=2, stroke_opacity=0.6)
        payoff_lines = VGroup(flat_seg, rise_seg)
        # label placed in open space, away from the curve
        payoff_label = cream_label("Intrinsic value", [2.8, 0.9, 0], font_size=22, txt_color=SLATE)

        # ---- Black-Scholes curve (pre-computed) ----
        BS_PTS = [
            (60, 0.02), (70, 0.52), (80, 2.20), (90, 6.40),
            (95, 8.80), (100, 10.45), (105, 12.25), (110, 14.60),
            (120, 20.50), (130, 27.50), (140, 35.00)
        ]

        def to_plot(S, price):
            x = -5.0 + (S - 60) / 80.0 * 10.0
            y = -2.5 + (price / 45.0) * 5.0
            return [x, y, 0]

        plot_pts = [to_plot(S, p) for S, p in BS_PTS]
        segs = VGroup()
        for i in range(len(plot_pts) - 1):
            segs.add(Line(plot_pts[i], plot_pts[i+1], color=CRIMSON, stroke_width=3))
        bs_curve = segs

        # ---- ATM marker ----
        atm_y = -2.5 + (10.45 / 45.0) * 5.0
        atm_dot = Dot([0.0, atm_y, 0], color=CRIMSON)
        # place label away from curve — lower right, clear of the BS curve
        atm_label = cream_label("ATM: $10.45", [1.8, -1.8, 0], font_size=22, txt_color=CRIMSON)

        # ---- Sequence (7 play() calls) ----
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(tick_labels))
        self.play(FadeIn(strike_line), Write(strike_label))
        self.play(FadeIn(payoff_lines), Write(payoff_label))
        self.play(Create(bs_curve))
        self.play(FadeIn(atm_dot), Write(atm_label))
        self.play(Write(axis_labels))
