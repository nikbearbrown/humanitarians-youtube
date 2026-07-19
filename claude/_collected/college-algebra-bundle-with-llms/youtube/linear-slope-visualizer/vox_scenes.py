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


class B04_SlopeVisualizer(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Slope = Rise / Run", font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        x_ax = Line(start=[-5.5, 0.0, 0], end=[5.5, 0.0, 0], color=SLATE, stroke_width=2)
        y_ax = Line(start=[0.0, -2.8, 0], end=[0.0, 2.8, 0], color=SLATE, stroke_width=2)
        self.play(Create(x_ax), run_time=0.4)
        self.play(Create(y_ax), run_time=0.4)
        slope_line = Line(start=[-1.75, -2.5, 0], end=[0.75, 2.5, 0], color=CRIMSON, stroke_width=3)
        self.play(Create(slope_line), run_time=0.5)
        y_int = Dot(point=[0.0, 1.0, 0], color=INK, radius=0.12)
        self.play(GrowFromCenter(y_int), run_time=0.25)
        run_seg = Line(start=[0.0, 1.0, 0], end=[1.0, 1.0, 0], color=SLATE, stroke_width=2)
        rise_seg = Line(start=[1.0, 1.0, 0], end=[1.0, 3.0, 0], color=CRIMSON, stroke_width=3)
        hyp = Line(start=[0.0, 1.0, 0], end=[1.0, 3.0, 0], color=GOLD, stroke_width=1.5)
        self.play(Create(run_seg), run_time=0.3)
        self.play(Create(rise_seg), run_time=0.3)
        self.play(Create(hyp), run_time=0.25)
        run_lbl = Text("run=1", font="Prism", font_size=16, color=SLATE)
        run_lbl.move_to([0.5, 0.7, 0])
        self.play(FadeIn(run_lbl), run_time=0.25)
        rise_lbl = Text("rise=2", font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
        rise_lbl.move_to([1.55, 2.0, 0])
        self.play(FadeIn(rise_lbl), run_time=0.25)
        slope_box = Rectangle(width=3.5, height=0.7, fill_color=GOLD,
                              fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        slope_box.move_to([-3.5, -2.0, 0])
        self.play(GrowFromCenter(slope_box), run_time=0.35)
        slope_lbl2 = Text("m = 2/1 = 2", font="Prism", font_size=20, color=CRIMSON, weight=BOLD)
        slope_lbl2.move_to([-3.5, -2.0, 0])
        self.play(FadeIn(slope_lbl2), run_time=0.3)
        self.wait(max(0, dur - 6.0))


class B06_ParallelPerp(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Parallel & Perpendicular Lines", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        div = Line(start=[0, 2.7, 0], end=[0, -2.8, 0], color=SLATE, stroke_width=1.5)
        self.play(GrowFromEdge(div, UP), run_time=0.4)
        lh = Text("Parallel Lines", font="Prism", font_size=17, color=INK, weight=BOLD)
        lh.move_to([-3.0, 2.4, 0])
        self.play(FadeIn(lh), run_time=0.3)
        pl1 = Line(start=[-5.5, -2.0, 0], end=[-1.5, 2.0, 0], color=CRIMSON, stroke_width=3)
        pl2 = Line(start=[-5.5, -0.5, 0], end=[-1.5, 1.5, 0], color=INK, stroke_width=3)
        self.play(Create(pl1), run_time=0.4)
        self.play(Create(pl2), run_time=0.4)
        pm_lbl = Text("same slope m=2", font="Prism", font_size=15, color=CRIMSON)
        pm_lbl.move_to([-3.0, -1.5, 0])
        self.play(FadeIn(pm_lbl), run_time=0.3)
        pm_box = Rectangle(width=2.5, height=0.55, fill_color=CREAM,
                           fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        pm_box.move_to([-3.0, -2.1, 0])
        pm_txt = Text("never intersect", font="Prism", font_size=14, color=CRIMSON)
        pm_txt.move_to([-3.0, -2.1, 0])
        self.play(GrowFromCenter(pm_box), run_time=0.3)
        self.play(FadeIn(pm_txt), run_time=0.25)
        rh_box = Rectangle(width=3.2, height=0.5, fill_color=CREAM,
                           fill_opacity=1, stroke_color=SLATE, stroke_width=1)
        rh_box.move_to([3.0, 2.4, 0])
        self.play(GrowFromCenter(rh_box), run_time=0.2)
        rh = Text("Perpendicular Lines", font="Prism", font_size=17, color=INK, weight=BOLD)
        rh.move_to([3.0, 2.4, 0])
        self.play(FadeIn(rh), run_time=0.3)
        pp1 = Line(start=[0.5, -2.5, 0], end=[2.5, 1.8, 0], color=CRIMSON, stroke_width=3)
        pp2 = Line(start=[0.5, 0.4, 0], end=[5.5, -1.7, 0], color=INK, stroke_width=3)
        self.play(Create(pp1), run_time=0.4)
        self.play(Create(pp2), run_time=0.4)
        perp_lbl = Text("m1 x m2 = -1", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        perp_lbl.move_to([3.0, -1.5, 0])
        self.play(FadeIn(perp_lbl), run_time=0.3)
        perp_box = Rectangle(width=2.8, height=0.55, fill_color=GOLD,
                             fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        perp_box.move_to([3.0, -2.1, 0])
        perp_txt = Text("meet at 90 deg", font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        perp_txt.move_to([3.0, -2.1, 0])
        self.play(GrowFromCenter(perp_box), run_time=0.3)
        self.play(FadeIn(perp_txt), run_time=0.25)
        self.wait(max(0, dur - 6.0))
