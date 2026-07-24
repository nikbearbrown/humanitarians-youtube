import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_SolveVerifyBars(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Solve vs. Verify: The Time Gap", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        subtitle_bg = Rectangle(width=8.0, height=0.55, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0)
        subtitle_bg.move_to([0, 2.8, 0])
        self.play(GrowFromCenter(subtitle_bg), run_time=0.2)
        subtitle = Text("Same task: top_three_by_gpa with tie-breaking", font="Prism", font_size=15, color=SLATE)
        subtitle.move_to([0, 2.8, 0])
        self.play(FadeIn(subtitle), run_time=0.2)
        base_line = Line(start=[-5.5, -1.5, 0], end=[5.5, -1.5, 0], color=INK, stroke_width=2)
        self.play(Create(base_line), run_time=0.3)
        claude_h = 0.3
        claude_bar = Rectangle(width=2.2, height=claude_h, fill_color=GOLD, fill_opacity=0.9,
                               stroke_color=INK, stroke_width=2)
        claude_bar.move_to([-2.5, -1.5 + claude_h/2, 0])
        self.play(GrowFromEdge(claude_bar, DOWN), run_time=0.4)
        cb_bg = Rectangle(width=1.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        cb_bg.move_to([-2.5, -1.5 + claude_h + 0.35, 0])
        cb_val = Text("8 sec", font="Prism", font_size=18, color=INK, weight=BOLD)
        cb_val.move_to([-2.5, -1.5 + claude_h + 0.35, 0])
        self.play(GrowFromCenter(cb_bg), FadeIn(cb_val), run_time=0.25)
        cl_bg = Rectangle(width=2.8, height=0.45, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        cl_bg.move_to([-2.5, -2.05, 0])
        cl_lbl = Text("Claude solve", font="Prism", font_size=15, color=INK)
        cl_lbl.move_to([-2.5, -2.05, 0])
        self.play(GrowFromCenter(cl_bg), FadeIn(cl_lbl), run_time=0.2)
        human_h = 3.0
        human_bar = Rectangle(width=2.2, height=human_h, fill_color=CRIMSON, fill_opacity=0.75,
                              stroke_color=CRIMSON, stroke_width=2)
        human_bar.move_to([2.5, -1.5 + human_h/2, 0])
        self.play(GrowFromEdge(human_bar, DOWN), run_time=0.6)
        hb_bg = Rectangle(width=2.0, height=0.5, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        hb_bg.move_to([2.5, -1.5 + human_h + 0.35, 0])
        hb_val = Text("4 min", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        hb_val.move_to([2.5, -1.5 + human_h + 0.35, 0])
        self.play(GrowFromCenter(hb_bg), FadeIn(hb_val), run_time=0.25)
        hl_bg = Rectangle(width=3.0, height=0.45, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        hl_bg.move_to([2.5, -2.05, 0])
        hl_lbl = Text("Human verify", font="Prism", font_size=15, color=CRIMSON)
        hl_lbl.move_to([2.5, -2.05, 0])
        self.play(GrowFromCenter(hl_bg), FadeIn(hl_lbl), run_time=0.2)
        ratio_box = Rectangle(width=5.5, height=0.65, fill_color=GOLD, fill_opacity=0.9,
                              stroke_color=CRIMSON, stroke_width=2)
        ratio_box.move_to([0, -2.75, 0])
        self.play(GrowFromCenter(ratio_box), run_time=0.35)
        ratio_lbl = Text("Verify is 30x slower -- and verify catches the bug", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        ratio_lbl.move_to([0, -2.75, 0])
        self.play(FadeIn(ratio_lbl), run_time=0.3)
        self.wait(max(0, dur - 6.0))


class B06_AsymmetryTrend(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("The Gap Is Widening", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdr_line = Line(start=[-5.5, 2.5, 0], end=[5.5, 2.5, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        hdrs = ["Year", "Solve speed", "Verify speed", "Ratio", "Gap"]
        x_pos = [-4.0, -1.8, 0.5, 2.5, 4.2]
        for h, xp in zip(hdrs, x_pos):
            lbl = Text(h, font="Prism", font_size=14, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.75, 0])
            self.play(FadeIn(lbl), run_time=0.1)
        data = [
            ("2023", "1x",  "1x", "1:1",  "baseline", CREAM),
            ("2024", "2x",  "1x", "2:1",  "2x wider",  CREAM),
            ("2025", "4x",  "1x", "4:1",  "4x wider",  "#FFF0F0"),
            ("2026", "8x",  "1x", "8:1",  "8x wider",  GOLD),
        ]
        y_top = 1.8
        for i, (yr, solve, verify, ratio, gap, bg) in enumerate(data):
            y = y_top - i * 0.85
            row_bg = Rectangle(width=11.0, height=0.72, fill_color=bg, fill_opacity=0.7,
                               stroke_color=SLATE, stroke_width=0.5)
            row_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(row_bg), run_time=0.2)
            clr = CRIMSON if i >= 2 else INK
            for val, xp in zip([yr, solve, verify, ratio, gap], x_pos):
                lbl = Text(val, font="Prism", font_size=14, color=clr if val in [ratio, gap] else INK)
                lbl.move_to([xp, y, 0])
                self.play(FadeIn(lbl), run_time=0.1)
        rule_box = Rectangle(width=8.0, height=0.65, fill_color=CREAM, fill_opacity=1,
                             stroke_color=CRIMSON, stroke_width=2)
        rule_box.move_to([0, -1.7, 0])
        self.play(GrowFromCenter(rule_box), run_time=0.35)
        rule_lbl = Text("Compete on solve: you lose.  Invest in verify: you win.", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        rule_lbl.move_to([0, -1.7, 0])
        self.play(FadeIn(rule_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))
