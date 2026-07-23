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


class B04_DomainHole(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("f(x) = 1/(x−2): Vertical Asymptote",
                     font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        # Function label
        func_lbl = Text("f(x) = 1 / (x − 2)", font="Prism", font_size=32, color=INK, weight=BOLD)
        func_lbl.move_to([0, 2.5, 0])
        self.play(FadeIn(func_lbl), run_time=0.4)

        # Number line showing domain
        nline = Line(start=[-5.5, 1.2, 0], end=[5.5, 1.2, 0], color=SLATE, stroke_width=2)
        self.play(GrowFromCenter(nline), run_time=0.4)

        # Tick marks at key x-values
        for x_pos, label in [(-4.0, "0"), (-1.0, "1"), (2.0, "3"), (5.0, "4")]:
            tick = Line(start=[x_pos, 1.0, 0], end=[x_pos, 1.4, 0], color=SLATE, stroke_width=2)
            self.play(GrowFromCenter(tick), run_time=0.15)

        # Mark x=2 on number line with a bold CRIMSON tick
        tick2 = Line(start=[2.0, 0.8, 0], end=[2.0, 1.6, 0], color=CRIMSON, stroke_width=3)
        self.play(GrowFromCenter(tick2), run_time=0.3)

        # Show the substitution f(2) = 1/0
        box_sub = Rectangle(width=4.5, height=1.0, fill_color=CREAM,
                            fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        box_sub.move_to([0, 0.0, 0])
        self.play(GrowFromCenter(box_sub), run_time=0.35)

        sub_lbl = Text("f(2) = 1/(2−2) = 1/0  → UNDEFINED", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        sub_lbl.move_to([0, 0.0, 0])
        self.play(FadeIn(sub_lbl), run_time=0.3)

        # Vertical asymptote line
        va = DashedLine(
            start=[2.0, -1.0, 0],
            end=[2.0, 1.5, 0],
            color=CRIMSON, stroke_width=2, dash_length=0.15
        )
        self.play(Create(va), run_time=0.4)

        # Arrow showing f → +∞ from right
        arr_r = Arrow(start=[3.5, -0.7, 0], end=[2.3, -0.2, 0], color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(arr_r), run_time=0.3)

        # Arrow showing f → −∞ from left
        arr_l = Arrow(start=[0.5, -0.7, 0], end=[1.7, -0.2, 0], color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(arr_l), run_time=0.3)

        # Domain box
        dom_box = Rectangle(width=5.5, height=0.65, fill_color=CREAM,
                            fill_opacity=1, stroke_color=INK, stroke_width=2)
        dom_box.move_to([0, -1.8, 0])
        self.play(GrowFromCenter(dom_box), run_time=0.35)

        dom = Text("Domain: (−∞, 2) ∪ (2, +∞)  — x ≠ 2", font="Prism", font_size=17, color=INK)
        dom.move_to([0, -1.8, 0])
        self.play(FadeIn(dom), run_time=0.3)

        # Dot showing where the hole WOULD be
        excl_dot = Circle(radius=0.18, color=CRIMSON, stroke_width=3, fill_opacity=0)
        excl_dot.move_to([2.0, 1.2, 0])
        self.play(GrowFromCenter(excl_dot), run_time=0.35)

        self.wait(max(0, dur - 6.0))


class B06_DomainHole2(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Hole vs Asymptote: Two Different Restrictions",
                     font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        # Vertical divider
        div = Line(start=[0, 2.8, 0], end=[0, -2.8, 0], color=SLATE, stroke_width=1.5)
        self.play(GrowFromEdge(div, UP), run_time=0.4)

        # Left panel header box
        left_box = Rectangle(width=5.5, height=0.7, fill_color=CREAM,
                             fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        left_box.move_to([-3.0, 2.5, 0])
        self.play(GrowFromCenter(left_box), run_time=0.3)
        left_hdr = Text("f(x) = 1/(x−2)", font="Prism", font_size=17, color=CRIMSON, weight=BOLD)
        left_hdr.move_to([-3.0, 2.5, 0])
        self.play(FadeIn(left_hdr), run_time=0.2)

        for i, line in enumerate(["f(2) = undefined", "f→±∞ as x→2", "Vertical ASYMPTOTE", "Cannot fill in"]):
            clr = CRIMSON if "ASYMPTOTE" in line else INK
            lbl = Text(line, font="Prism", font_size=15, color=clr)
            lbl.move_to([-3.0, 1.7 - i * 0.65, 0])
            self.play(FadeIn(lbl), run_time=0.25)

        # Left asymptote visual — dashed vertical line
        va_left = DashedLine(start=[-3.0, 0.2, 0], end=[-3.0, -1.2, 0],
                             color=CRIMSON, stroke_width=2, dash_length=0.12)
        self.play(Create(va_left), run_time=0.3)

        # Right panel header box
        right_box = Rectangle(width=5.5, height=0.7, fill_color=CREAM,
                              fill_opacity=1, stroke_color=INK, stroke_width=2)
        right_box.move_to([3.0, 2.5, 0])
        self.play(GrowFromCenter(right_box), run_time=0.3)
        right_hdr = Text("g(x) = (x²−4)/(x−2)", font="Prism", font_size=17, color=INK, weight=BOLD)
        right_hdr.move_to([3.0, 2.5, 0])
        self.play(FadeIn(right_hdr), run_time=0.2)

        for i, line in enumerate(["g(2) = 0/0 indeterminate", "= (x+2)(x−2)/(x−2)", "= x+2  for x≠2", "HOLE at (2, 4) ← open circle"]):
            clr = CRIMSON if "HOLE" in line else INK
            lbl = Text(line, font="Prism", font_size=15, color=clr)
            lbl.move_to([3.0, 1.7 - i * 0.65, 0])
            self.play(FadeIn(lbl), run_time=0.25)

        # Right hole visual — open circle showing removable discontinuity
        hole = Circle(radius=0.18, color=CRIMSON, stroke_width=3, fill_opacity=0)
        hole.move_to([3.0, -1.3, 0])
        self.play(GrowFromCenter(hole), run_time=0.4)

        # Arrow pointing to hole
        arr_hole = Arrow(start=[4.5, -1.3, 0], end=[3.25, -1.3, 0], color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(arr_hole), run_time=0.3)

        # Bottom summary dot
        sum_dot = Dot(point=[0, -2.4, 0], color=CRIMSON, radius=0.12)
        self.play(GrowFromCenter(sum_dot), run_time=0.2)

        self.wait(max(0, dur - 6.0))
