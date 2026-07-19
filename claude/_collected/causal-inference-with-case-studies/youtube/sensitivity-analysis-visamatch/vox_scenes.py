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

# Curve data points: (E, OR) -> (x_plot, y_plot)
# x: E in [1,5] -> x_plot = -5.0 + (E-1)/4 * 10.0
# y: OR in [0,3] -> y_plot = -2.5 + (OR/3) * 5.0
_CURVE_POINTS = [
    (1.0, 2.5),
    (1.5, 2.2),
    (2.0, 1.8),
    (2.5, 1.4),
    (3.2, 1.0),
    (4.0, 0.6),
    (5.0, 0.4),
]


def _ex(E):
    return -5.0 + (E - 1.0) / 4.0 * 10.0


def _ey(OR):
    return -2.5 + (OR / 3.0) * 5.0


class B04_EValueCurve(Scene):
    def construct(self):
        # Title
        title = Text("E-VALUE SENSITIVITY ANALYSIS",
                     color=INK, weight=BOLD, font_size=36).move_to([0, 3.2, 0])

        # Axes
        y_axis = Line([-5.0, -2.5, 0], [-5.0, 2.5, 0], color=INK, stroke_width=2)
        x_axis = Line([-5.0, -2.5, 0], [ 5.0, -2.5, 0], color=INK, stroke_width=2)

        # Helper to make a tick label with CREAM bg
        def tick_lbl(text_str, x, y):
            t = Text(text_str, color=INK, font_size=20)
            t.move_to([x, y, 0])
            bg = Rectangle(
                width=t.width + 0.12, height=t.height + 0.08,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(t.get_center())
            return VGroup(bg, t)

        # x-tick labels
        x_ticks = VGroup(
            tick_lbl("E=1.0", -5.0, -2.9),
            tick_lbl("E=2.0", -2.5, -2.9),
            tick_lbl("E=3.0",  0.0, -2.9),
            tick_lbl("E=5.0",  5.0, -2.9),
        )

        # y-tick labels
        y_ticks = VGroup(
            tick_lbl("OR=0", -5.5, -2.5),
            tick_lbl("OR=1", -5.5, _ey(1.0)),
            tick_lbl("OR=2", -5.5, _ey(2.0)),
            tick_lbl("OR=3", -5.5,  2.5),
        )

        # Axis labels — x label at y=-3.2, ticks at -2.9 (gap 0.3)
        x_axis_lbl_txt = Text("E (unmeasured confounding strength)", color=SLATE, font_size=20)
        x_axis_lbl_txt.move_to([0, -3.2, 0])
        x_axis_lbl_bg = Rectangle(
            width=x_axis_lbl_txt.width + 0.15, height=x_axis_lbl_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(x_axis_lbl_txt.get_center())
        x_axis_label = VGroup(x_axis_lbl_bg, x_axis_lbl_txt)

        # y_axis_lbl: add CREAM bg so it does not trigger W5 text-on-line
        y_axis_lbl_txt = Text("Odds Ratio", color=SLATE, font_size=20)
        y_axis_lbl_txt.move_to([-5.6, 0.0, 0])
        y_axis_lbl_bg = Rectangle(
            width=y_axis_lbl_txt.width + 0.15, height=y_axis_lbl_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(y_axis_lbl_txt.get_center())
        y_axis_lbl = VGroup(y_axis_lbl_bg, y_axis_lbl_txt)

        tick_labels = VGroup(x_ticks, y_ticks)
        axis_labels = VGroup(x_axis_label, y_axis_lbl)

        # OR=1 null dashed line at y = _ey(1.0)
        null_y = _ey(1.0)  # -0.833...
        null_line = DashedLine([-5.0, null_y, 0], [5.0, null_y, 0],
                               color=SLATE, dash_length=0.2)
        null_lbl_txt = Text("OR = 1 (null)", color=SLATE, font_size=22)
        null_lbl_txt.move_to([3.5, null_y + 0.28, 0])
        null_lbl_bg = Rectangle(
            width=null_lbl_txt.width + 0.15, height=null_lbl_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(null_lbl_txt.get_center())
        null_label = VGroup(null_lbl_bg, null_lbl_txt)

        # Sensitivity curve as VGroup of Line segments
        curve_pts = [[_ex(E), _ey(OR), 0] for E, OR in _CURVE_POINTS]
        curve_segments = VGroup(*[
            Line(curve_pts[i], curve_pts[i + 1], color=INK, stroke_width=2.5)
            for i in range(len(curve_pts) - 1)
        ])

        # E-value crossing at E=3.2, OR=1.0
        ev_x = _ex(3.2)  # 0.5
        ev_y = null_y    # _ey(1.0) = -0.833
        evalue_vline = DashedLine([ev_x, -2.5, 0], [ev_x, ev_y, 0],
                                   color=CRIMSON, dash_length=0.15)
        evalue_dot = Dot(point=[ev_x, ev_y, 0], color=CRIMSON, radius=0.12)

        ev_lbl_txt = Text("E-value = 3.2", color=CRIMSON, weight=BOLD, font_size=28)
        ev_lbl_txt.move_to([2.2, ev_y + 0.6, 0])
        ev_lbl_bg = Rectangle(
            width=ev_lbl_txt.width + 0.15, height=ev_lbl_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(ev_lbl_txt.get_center())
        evalue_label = VGroup(ev_lbl_bg, ev_lbl_txt)

        evalue_arrow = Arrow(
            start=[2.0, ev_y + 0.15, 0],
            end=[ev_x + 0.15, ev_y, 0],
            color=CRIMSON, tip_length=0.15, buff=0.0
        )

        # Verdict — placed in upper chart area with CREAM bg, within safe area
        verdict_txt_raw = Text("confounding OR > 3.2 to explain result away",
                               color=INK, font_size=22)
        verdict_txt_raw.move_to([-0.5, 2.2, 0])
        verdict_bg2 = Rectangle(
            width=verdict_txt_raw.width + 0.18, height=verdict_txt_raw.height + 0.1,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(verdict_txt_raw.get_center())
        verdict_txt = VGroup(verdict_bg2, verdict_txt_raw)

        # 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(y_axis), FadeIn(x_axis),
                  FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(FadeIn(null_line), Write(null_label))
        self.play(Create(curve_segments))
        self.play(FadeIn(evalue_vline), FadeIn(evalue_dot),
                  Write(evalue_label), FadeIn(evalue_arrow))
        self.play(Write(verdict_txt))
        self.wait(1)
