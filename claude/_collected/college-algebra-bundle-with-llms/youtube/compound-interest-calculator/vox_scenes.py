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


class B04_CompoundCurves(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Compound Interest: Frequency Comparison", font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        cases = [
            ("n=1\nannual",    2594, SLATE),
            ("n=4\nquarterly", 2685, INK),
            ("n=12\nmonthly",  2707, CRIMSON),
            ("n=365\ndaily",   2718, CRIMSON),
            ("n=inf\ncontin.", 2718, CRIMSON),
        ]
        bar_bottom = -2.5
        bar_scale = 2.5 / 220
        bar_width = 1.4
        x_positions = [-4.5, -2.2, 0.0, 2.2, 4.5]
        base_line = Line(start=[-5.5, bar_bottom, 0], end=[5.5, bar_bottom, 0], color=INK, stroke_width=2)
        self.play(Create(base_line), run_time=0.4)
        for (label, A, clr), xc in zip(cases, x_positions):
            bar_h = (A - 2500) * bar_scale
            bar = Rectangle(width=bar_width, height=max(bar_h, 0.1),
                           fill_color=clr, fill_opacity=0.7,
                           stroke_color=clr, stroke_width=2)
            bar.move_to([xc, bar_bottom + bar_h/2, 0])
            self.play(GrowFromEdge(bar, DOWN), run_time=0.4)
            A_bg = Rectangle(width=1.4, height=0.4, fill_color=CREAM, fill_opacity=1, stroke_width=0)
            A_bg.move_to([xc, bar_bottom + bar_h + 0.28, 0])
            self.play(FadeIn(A_bg), run_time=0.05)
            A_lbl = Text(f"${A:,}", font="Prism", font_size=14, color=clr, weight=BOLD)
            A_lbl.move_to([xc, bar_bottom + bar_h + 0.28, 0])
            self.play(FadeIn(A_lbl), run_time=0.2)
            n_lbl = Text(label, font="Prism", font_size=12, color=INK)
            n_lbl.move_to([xc, bar_bottom - 0.4, 0])
            self.play(FadeIn(n_lbl), run_time=0.2)
        self.wait(max(0, dur - 5.0))


class B06_ContinuousVsDiscrete(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("The Continuous Limit: A = Pe^(rt)", font="Prism", font_size=24, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        limit_box = Rectangle(width=8.5, height=0.75, fill_color=CREAM,
                              fill_opacity=1, stroke_color=INK, stroke_width=2)
        limit_box.move_to([0, 2.5, 0])
        self.play(GrowFromCenter(limit_box), run_time=0.35)
        limit_lbl = Text("As n goes to inf: (1+r/n)^n approaches e^r", font="Prism", font_size=17, color=INK)
        limit_lbl.move_to([0, 2.5, 0])
        self.play(FadeIn(limit_lbl), run_time=0.3)
        arrow_down = Arrow(start=[0, 2.1, 0], end=[0, 1.5, 0], color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(arrow_down), run_time=0.3)
        cont_box = Rectangle(width=6.0, height=0.75, fill_color=GOLD,
                             fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        cont_box.move_to([0, 1.1, 0])
        self.play(GrowFromCenter(cont_box), run_time=0.35)
        cont_lbl = Text("Continuous: A = Pe^(rt)", font="Prism", font_size=21, color=CRIMSON, weight=BOLD)
        cont_lbl.move_to([0, 1.1, 0])
        self.play(FadeIn(cont_lbl), run_time=0.3)
        ex_line = Line(start=[-5.5, 0.4, 0], end=[5.5, 0.4, 0], color=SLATE, stroke_width=1.5)
        self.play(Create(ex_line), run_time=0.3)
        ex_box = Rectangle(width=5.5, height=0.4, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        ex_box.move_to([0, 0.05, 0])
        self.play(FadeIn(ex_box), run_time=0.1)
        ex_hdr = Text("P=$1000, r=10%, t=10 yrs", font="Prism", font_size=16, color=SLATE)
        ex_hdr.move_to([0, 0.05, 0])
        self.play(FadeIn(ex_hdr), run_time=0.25)
        disc_box = Rectangle(width=4.0, height=1.0, fill_color=CREAM,
                             fill_opacity=1, stroke_color=SLATE, stroke_width=2)
        disc_box.move_to([-3.0, -0.9, 0])
        disc_lbl1 = Text("Monthly (n=12)", font="Prism", font_size=15, color=SLATE)
        disc_lbl1.move_to([-3.0, -0.65, 0])
        disc_lbl2 = Text("A = $2,707", font="Prism", font_size=18, color=INK, weight=BOLD)
        disc_lbl2.move_to([-3.0, -1.15, 0])
        self.play(GrowFromCenter(disc_box), run_time=0.35)
        self.play(FadeIn(disc_lbl1), FadeIn(disc_lbl2), run_time=0.3)
        vs_lbl = Text("vs", font="Prism", font_size=20, color=SLATE, weight=BOLD)
        vs_lbl.move_to([0, -0.9, 0])
        self.play(FadeIn(vs_lbl), run_time=0.2)
        cont_box2 = Rectangle(width=4.0, height=1.0, fill_color=GOLD,
                              fill_opacity=0.8, stroke_color=CRIMSON, stroke_width=2)
        cont_box2.move_to([3.0, -0.9, 0])
        cont_lbl1 = Text("Continuous", font="Prism", font_size=15, color=CRIMSON)
        cont_lbl1.move_to([3.0, -0.65, 0])
        cont_lbl2 = Text("A = $2,718", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        cont_lbl2.move_to([3.0, -1.15, 0])
        self.play(GrowFromCenter(cont_box2), run_time=0.35)
        self.play(FadeIn(cont_lbl1), FadeIn(cont_lbl2), run_time=0.3)
        e_box = Rectangle(width=5.5, height=0.65, fill_color=CREAM,
                          fill_opacity=1, stroke_color=INK, stroke_width=2)
        e_box.move_to([0, -2.3, 0])
        self.play(GrowFromCenter(e_box), run_time=0.3)
        e_lbl = Text("e = 2.71828... (Euler's number)", font="Prism", font_size=16, color=INK)
        e_lbl.move_to([0, -2.3, 0])
        self.play(FadeIn(e_lbl), run_time=0.25)
        self.wait(max(0, dur - 6.5))
