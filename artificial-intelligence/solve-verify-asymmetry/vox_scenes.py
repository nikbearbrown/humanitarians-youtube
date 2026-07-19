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


class B04_SolveVerifyBars(Scene):
    def construct(self):
        PROBLEMS = ["Arithmetic", "Algebra", "Quadratic", "Combinatorics", "Proof"]
        RATIOS = [3, 20, 40, 100, 300]
        BAR_COLORS = [PASS_CLR, GOLD, GOLD, CRIMSON, CRIMSON]
        BAR_XS = [-4.0, -2.0, 0.0, 2.0, 4.0]
        BAR_W = 1.5
        Y_BOTTOM = -2.5

        title = Text("SOLVE-VERIFY ASYMMETRY", color=INK, font_size=36, weight=BOLD).move_to([0, 3.2, 0])

        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)

        # y-tick labels — 0x moved slightly above the x-axis to avoid line overlap
        tick_data = [("0x", -2.2), ("50x", 0.0), ("100x", 2.5)]
        y_tick_labels = VGroup()
        for label_str, label_y in tick_data:
            bg = Rectangle(width=0.7, height=0.35, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([-4.6, label_y, 0])
            txt = Text(label_str, color=INK, font_size=20).move_to([-4.6, label_y, 0])
            y_tick_labels.add(bg, txt)

        # Build bars
        bars = VGroup()
        for i, (ratio, color, bx) in enumerate(zip(RATIOS, BAR_COLORS, BAR_XS)):
            clipped = min(ratio, 100)
            bar_h = (clipped / 100.0) * 5.0
            bar = Rectangle(width=BAR_W, height=bar_h,
                            fill_color=color, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0)
            bar.move_to([bx, Y_BOTTOM + bar_h / 2, 0])
            bars.add(bar)

        bar1, bar2, bar3, bar4, bar5 = bars

        # Ratio labels above bars
        ratio_label_data = [
            ("3x", BAR_XS[0], Y_BOTTOM + (min(3, 100)/100)*5.0 + 0.25),
            ("20x", BAR_XS[1], Y_BOTTOM + (min(20, 100)/100)*5.0 + 0.25),
            ("40x", BAR_XS[2], Y_BOTTOM + (min(40, 100)/100)*5.0 + 0.25),
            ("100x", BAR_XS[3], Y_BOTTOM + 5.0 + 0.25),
            ("300x", BAR_XS[4], Y_BOTTOM + 5.0 + 0.25),
        ]
        ratio_labels = VGroup()
        for txt_str, lx, ly in ratio_label_data:
            bg = Rectangle(width=0.75, height=0.38, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([lx, ly, 0])
            txt = Text(txt_str, color=INK, font_size=22).move_to([lx, ly, 0])
            ratio_labels.add(bg, txt)

        # Overflow arrow for Proof bar (ratio=300, clipped at 100)
        overflow_arrow = Arrow(
            start=[BAR_XS[4], 2.5, 0],
            end=[BAR_XS[4], 3.0, 0],
            color=CRIMSON,
            stroke_width=3
        )

        # Problem name labels below x-axis
        problem_labels = VGroup()
        for prob_str, px in zip(PROBLEMS, BAR_XS):
            bg = Rectangle(width=1.5, height=0.35, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([px, -2.9, 0])
            txt = Text(prob_str, color=INK, font_size=18).move_to([px, -2.9, 0])
            problem_labels.add(bg, txt)

        verdict_text = Text(
            "Faster AI, wider gap — NP-hard by design",
            color=CRIMSON, font_size=26
        ).move_to([0, -3.2, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(y_tick_labels))
        self.play(GrowFromEdge(bar1, DOWN), GrowFromEdge(bar2, DOWN))
        self.play(GrowFromEdge(bar3, DOWN))
        self.play(GrowFromEdge(bar4, DOWN), GrowFromEdge(bar5, DOWN))
        self.play(
            *[Write(lbl) for lbl in ratio_labels],
            *[Write(lbl) for lbl in problem_labels],
            FadeIn(overflow_arrow)
        )
        self.play(Write(verdict_text))
