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


class B04_AnomalyBars(Scene):
    def construct(self):
        # Title
        title = Text("REGIME-AWARE vs GLOBAL BASELINE",
                     color=INK, weight=BOLD, font_size=36).move_to([0, 3.2, 0])

        # Axes
        y_axis = Line([-4.8, -2.5, 0], [-4.8, 2.5, 0], color=INK, stroke_width=2)
        x_axis = Line([-4.8, -2.5, 0], [4.8, -2.5, 0], color=INK, stroke_width=2)

        # y-tick labels with CREAM bg rects
        def make_tick_label(text_str, x, y):
            lbl = Text(text_str, color=INK, font_size=22)
            lbl.move_to([x, y, 0])
            bg = Rectangle(
                width=lbl.width + 0.15, height=lbl.height + 0.08,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(lbl.get_center())
            return VGroup(bg, lbl)

        y_ticks = VGroup(
            make_tick_label("0%",   -5.2, -2.5),
            make_tick_label("50%",  -5.2,  0.0),
            make_tick_label("100%", -5.2,  2.5),
        )

        # Gridline at 50%
        gridline = Line([-4.8, 0.0, 0], [4.8, 0.0, 0],
                        color=SLATE, stroke_width=0.5, stroke_opacity=0.4)

        # LEFT BAR — GLOBAL BASELINE (100%, height 5.0, bottom at -2.5, center at (−2.0, 0.0))
        left_bar = Rectangle(
            width=2.5, height=5.0,
            fill_color=CRIMSON, fill_opacity=0.85,
            stroke_width=0, stroke_opacity=0
        ).move_to([-2.0, 0.0, 0])

        left_label = Text("GLOBAL BASELINE", color=INK, font_size=26).move_to([-2.0, 2.8, 0])
        left_pct   = Text("100%", color=INK, weight=BOLD, font_size=40).move_to([-2.0, 0.3, 0])
        left_f1    = Text("F1 = 0.00", color=INK, font_size=24).move_to([-2.0, -0.5, 0])

        # RIGHT BAR — REGIME-AWARE (66%, height 3.3, bottom at -2.5, center at (2.0, -0.85))
        right_bar = Rectangle(
            width=2.5, height=3.3,
            fill_color=PASS_CLR, fill_opacity=0.85,
            stroke_width=0, stroke_opacity=0
        ).move_to([2.0, -0.85, 0])

        right_label = Text("REGIME-AWARE", color=INK, font_size=26).move_to([2.0, 1.2, 0])
        right_pct   = Text("66%", color=INK, weight=BOLD, font_size=40).move_to([2.0, -0.5, 0])
        right_f1    = Text("F1 > 0", color=INK, font_size=24).move_to([2.0, -1.2, 0])

        # Verdict
        verdict_text = Text(
            "Causal fix: condition on regime (back-door blocked)",
            color=INK, font_size=26
        ).move_to([0, -3.2, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(y_axis), FadeIn(x_axis), FadeIn(y_ticks))
        self.play(GrowFromEdge(left_bar, DOWN))
        self.play(Write(left_label), Write(left_pct), Write(left_f1))
        self.play(GrowFromEdge(right_bar, DOWN))
        self.play(Write(right_label), Write(right_pct), Write(right_f1))
        self.play(Write(verdict_text))
        self.wait(1)
