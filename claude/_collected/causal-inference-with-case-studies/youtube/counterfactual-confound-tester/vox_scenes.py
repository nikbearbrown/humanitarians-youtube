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

# Pre-define marker x-positions as constants (no random() calls)
SEASONAL_X = [-4.5, -3.8, -3.0, -1.5, 0.0, 1.5, 3.0, 4.5]  # will dissolve
GENUINE_X  = [-2.5, 0.5, 2.5, 4.0]                           # will survive


class B04_AblationTimeline(Scene):
    def construct(self):
        # Title
        title = Text("COUNTERFACTUAL CONFOUND TEST",
                     color=INK, weight=BOLD, font_size=36).move_to([0, 3.2, 0])

        # x-axis timeline
        x_axis = Line([-5.5, -2.0, 0], [5.5, -2.0, 0], color=INK, stroke_width=2)

        # x-axis label with CREAM bg
        x_lbl_txt = Text("Time (days)", color=SLATE, font_size=24)
        x_lbl_txt.move_to([0, -2.7, 0])
        x_lbl_bg = Rectangle(
            width=x_lbl_txt.width + 0.15, height=x_lbl_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to(x_lbl_txt.get_center())
        x_label = VGroup(x_lbl_bg, x_lbl_txt)

        # Month tick marks: 12 evenly spaced from x=-5.0 to x=5.0
        tick_xs = [-5.0 + i * (10.0 / 11) for i in range(12)]
        tick_marks = VGroup(*[
            Line([tx, -2.1, 0], [tx, -2.0, 0], color=SLATE, stroke_width=1)
            for tx in tick_xs
        ])

        # Left axis label — kept within safe area (x >= -5.8, safe x <= -6.3)
        left_axis_lbl = Text("DISRUPTION\nFLAGGED", color=INK, font_size=20).move_to([-4.8, 0.5, 0])

        # Flags: all have bottom edge at y=-2.0, so center at (x, -1.5)
        seasonal_flags = VGroup(*[
            Rectangle(
                width=0.3, height=1.0,
                fill_color=CRIMSON, fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0
            ).move_to([sx, -1.5, 0])
            for sx in SEASONAL_X
        ])

        genuine_flags = VGroup(*[
            Rectangle(
                width=0.3, height=1.0,
                fill_color=PASS_CLR, fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0
            ).move_to([gx, -1.5, 0])
            for gx in GENUINE_X
        ])

        # Counter before ablation
        counter_before = Text("Predictions >= 80% confidence: 12",
                              color=INK, font_size=28).move_to([0, 1.0, 0])

        # Panel labels
        baseline_label  = Text("BASELINE", color=INK, weight=BOLD, font_size=30).move_to([-3.5, 2.5, 0])
        ablation_label  = Text("AFTER ABLATION", color=CRIMSON, weight=BOLD, font_size=30).move_to([2.5, 2.5, 0])

        # Counter after ablation — different y to avoid static overlap in gate check
        counter_after = Text("After ablation: 4 survive | 8 dissolved (67% seasonal)",
                             color=CRIMSON, font_size=24).move_to([0, 0.4, 0])

        # Verdict
        verdict_text = Text("33% of predictions were operational signal",
                            color=PASS_CLR, font_size=26).move_to([0, -3.0, 0])

        # 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(tick_marks), FadeIn(x_label))
        self.play(*[FadeIn(f) for f in seasonal_flags],
                  *[FadeIn(f) for f in genuine_flags],
                  Write(counter_before))
        self.play(Write(baseline_label))
        self.play(*[FadeOut(f) for f in seasonal_flags], FadeIn(ablation_label))
        self.play(FadeOut(counter_before), FadeIn(counter_after), Write(verdict_text))
        self.wait(1)
