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


class B04_QuadraticInequality(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Solve: x^2 - x - 6 < 0", font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        step1_box = Rectangle(width=7.0, height=0.65, fill_color=CREAM,
                              fill_opacity=1, stroke_color=INK, stroke_width=2)
        step1_box.move_to([0, 2.5, 0])
        self.play(GrowFromCenter(step1_box), run_time=0.35)
        step1_lbl = Text("Step 1: Factor  (x-3)(x+2) < 0", font="Prism", font_size=18, color=INK)
        step1_lbl.move_to([0, 2.5, 0])
        self.play(FadeIn(step1_lbl), run_time=0.3)
        step2_box = Rectangle(width=5.5, height=0.65, fill_color=CREAM,
                              fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        step2_box.move_to([0, 1.7, 0])
        self.play(GrowFromCenter(step2_box), run_time=0.3)
        step2_lbl = Text("Roots: x = 3  and  x = -2", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        step2_lbl.move_to([0, 1.7, 0])
        self.play(FadeIn(step2_lbl), run_time=0.3)
        sign_line = Line(start=[-5.5, 0.5, 0], end=[5.5, 0.5, 0], color=SLATE, stroke_width=2)
        self.play(Create(sign_line), run_time=0.4)
        root_left = Line(start=[-2.0, 0.3, 0], end=[-2.0, 0.7, 0], color=CRIMSON, stroke_width=3)
        root_right = Line(start=[3.0, 0.3, 0], end=[3.0, 0.7, 0], color=CRIMSON, stroke_width=3)
        self.play(Create(root_left), Create(root_right), run_time=0.35)
        rl_bg = Rectangle(width=1.2, height=0.35, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        rl_bg.move_to([-2.0, 0.05, 0])
        rr_bg = Rectangle(width=1.0, height=0.35, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        rr_bg.move_to([3.0, 0.05, 0])
        self.play(FadeIn(rl_bg), FadeIn(rr_bg), run_time=0.1)
        rl_lbl = Text("x=-2", font="Prism", font_size=14, color=CRIMSON)
        rl_lbl.move_to([-2.0, 0.05, 0])
        rr_lbl = Text("x=3", font="Prism", font_size=14, color=CRIMSON)
        rr_lbl.move_to([3.0, 0.05, 0])
        self.play(FadeIn(rl_lbl), FadeIn(rr_lbl), run_time=0.25)
        neg_lbl = Text("-", font="Prism", font_size=40, color=CRIMSON, weight=BOLD)
        neg_lbl.move_to([0.5, 1.1, 0])
        pos_l_lbl = Text("+", font="Prism", font_size=40, color=SLATE, weight=BOLD)
        pos_l_lbl.move_to([-4.0, 1.1, 0])
        pos_r_lbl = Text("+", font="Prism", font_size=40, color=SLATE, weight=BOLD)
        pos_r_lbl.move_to([5.0, 1.1, 0])
        self.play(FadeIn(neg_lbl), run_time=0.25)
        self.play(FadeIn(pos_l_lbl), FadeIn(pos_r_lbl), run_time=0.25)
        sol_box = Rectangle(width=4.5, height=0.7, fill_color=GOLD,
                            fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        sol_box.move_to([0, -0.7, 0])
        self.play(GrowFromCenter(sol_box), run_time=0.35)
        sol_lbl = Text("Solution: -2 < x < 3", font="Prism", font_size=20, color=CRIMSON, weight=BOLD)
        sol_lbl.move_to([0, -0.7, 0])
        self.play(FadeIn(sol_lbl), run_time=0.3)
        check_box = Rectangle(width=6.0, height=0.65, fill_color=CREAM,
                              fill_opacity=1, stroke_color=INK, stroke_width=2)
        check_box.move_to([0, -1.7, 0])
        self.play(GrowFromCenter(check_box), run_time=0.3)
        check_lbl = Text("Check x=0: (0-3)(0+2) = -6 < 0  v", font="Prism", font_size=16, color=INK)
        check_lbl.move_to([0, -1.7, 0])
        self.play(FadeIn(check_lbl), run_time=0.25)
        self.wait(max(0, dur - 7.0))


class B06_NumberLineSolution(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Solution on a Number Line", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        int_box = Rectangle(width=5.0, height=0.7, fill_color=GOLD,
                            fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        int_box.move_to([0, 2.5, 0])
        self.play(GrowFromCenter(int_box), run_time=0.35)
        int_lbl = Text("Solution: (-2, 3) open interval", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        int_lbl.move_to([0, 2.5, 0])
        self.play(FadeIn(int_lbl), run_time=0.3)
        n_line = Line(start=[-5.5, 0.5, 0], end=[5.5, 0.5, 0], color=SLATE, stroke_width=2)
        self.play(Create(n_line), run_time=0.4)
        for xv in [-4,-3,-2,-1,0,1,2,3,4,5]:
            sx = xv * 0.9
            tick = Line(start=[sx, 0.35, 0], end=[sx, 0.65, 0], color=SLATE, stroke_width=2)
            self.play(GrowFromCenter(tick), run_time=0.1)
        oc_left = Circle(radius=0.15, color=CRIMSON, stroke_width=3, fill_opacity=0)
        oc_left.move_to([-1.8, 0.5, 0])
        oc_right = Circle(radius=0.15, color=CRIMSON, stroke_width=3, fill_opacity=0)
        oc_right.move_to([2.7, 0.5, 0])
        self.play(GrowFromCenter(oc_left), run_time=0.3)
        self.play(GrowFromCenter(oc_right), run_time=0.3)
        sol_line = Line(start=[-1.65, 0.5, 0], end=[2.55, 0.5, 0], color=CRIMSON, stroke_width=8)
        self.play(Create(sol_line), run_time=0.4)
        l_bg = Rectangle(width=1.0, height=0.35, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        l_bg.move_to([-1.8, 0.1, 0])
        r_bg = Rectangle(width=0.9, height=0.35, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        r_bg.move_to([2.7, 0.1, 0])
        self.play(FadeIn(l_bg), FadeIn(r_bg), run_time=0.1)
        l_lbl = Text("x=-2", font="Prism", font_size=14, color=CRIMSON)
        l_lbl.move_to([-1.8, 0.1, 0])
        r_lbl = Text("x=3", font="Prism", font_size=14, color=CRIMSON)
        r_lbl.move_to([2.7, 0.1, 0])
        self.play(FadeIn(l_lbl), FadeIn(r_lbl), run_time=0.25)
        excl_box = Rectangle(width=5.5, height=0.65, fill_color=CREAM,
                             fill_opacity=1, stroke_color=INK, stroke_width=1.5)
        excl_box.move_to([0, -0.5, 0])
        self.play(GrowFromCenter(excl_box), run_time=0.3)
        excl_lbl = Text("Open circles: x=-2 and x=3 excluded", font="Prism", font_size=15, color=INK)
        excl_lbl.move_to([0, -0.5, 0])
        self.play(FadeIn(excl_lbl), run_time=0.25)
        set_box = Rectangle(width=5.0, height=0.7, fill_color=CREAM,
                            fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        set_box.move_to([0, -1.5, 0])
        self.play(GrowFromCenter(set_box), run_time=0.3)
        set_lbl = Text("{x in R | -2 < x < 3}", font="Prism", font_size=17, color=CRIMSON)
        set_lbl.move_to([0, -1.5, 0])
        self.play(FadeIn(set_lbl), run_time=0.25)
        self.wait(max(0, dur - 6.0))
