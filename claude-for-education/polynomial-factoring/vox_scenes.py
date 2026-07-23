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


def _node(text, x, y, w=3.2, h=0.65, clr=None):
    clr = clr or "#2A1A0E"
    box = RoundedRectangle(corner_radius=0.13, width=w, height=h,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_color=clr, stroke_width=2)
    box.move_to([x, y, 0])
    lbl = Text(text, font="Prism", font_size=14, color=clr)
    lbl.move_to([x, y, 0])
    return VGroup(box, lbl)


class B04_FactoringTree(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Factoring Decision Tree", font="Prism",
                     font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        n0 = _node("Step 1: Extract GCF", 0, 2.5, w=3.5)
        self.play(FadeIn(n0), run_time=0.4)

        a1 = Arrow(start=[0, 2.17, 0], end=[0, 1.55, 0], color=INK, stroke_width=2)
        self.play(GrowArrow(a1), run_time=0.3)
        n1 = _node("Step 2: How many terms?", 0, 1.2, w=3.5)
        self.play(FadeIn(n1), run_time=0.4)

        a2a = Arrow(start=[-0.5, 0.88, 0], end=[-2.8, 0.28, 0], color=INK, stroke_width=2)
        self.play(GrowArrow(a2a), run_time=0.3)
        t2a = Text("2 terms", font="Prism", font_size=13, color=SLATE)
        t2a.move_to([-2.2, 0.75, 0])
        self.play(FadeIn(t2a), run_time=0.2)
        n2a = _node("Diff. of squares?\na²−b²=(a+b)(a−b)", -2.8, -0.1, w=3.5, clr=CRIMSON)
        self.play(FadeIn(n2a), run_time=0.4)

        a2b = Arrow(start=[0.5, 0.88, 0], end=[2.8, 0.28, 0], color=INK, stroke_width=2)
        self.play(GrowArrow(a2b), run_time=0.3)
        t2b = Text("3 terms", font="Prism", font_size=13, color=SLATE)
        t2b.move_to([2.3, 0.75, 0])
        self.play(FadeIn(t2b), run_time=0.2)
        n2b = _node("Trinomial:\nfind p·q=c, p+q=b", 2.8, -0.1, w=3.2, clr=CRIMSON)
        self.play(FadeIn(n2b), run_time=0.4)

        a3 = Arrow(start=[2.8, -0.43, 0], end=[2.8, -1.13, 0], color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(a3), run_time=0.3)
        n3 = _node("(x+p)(x+q)", 2.8, -1.5, w=2.5, clr=CRIMSON)
        self.play(FadeIn(n3), run_time=0.4)
        self.wait(max(0, dur - 5.5))


class B06_FactoringExample(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Worked Example: x² + 5x + 6",
                     font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            ("Step 1:", "GCF? — none",                                SLATE),
            ("Step 2:", "3 terms → trinomial strategy",               SLATE),
            ("Step 3:", "a=1, so find p,q: p·q=6, p+q=5",            INK),
            ("Pairs:",  "1×6 (sum 7✗), 2×3 (sum 5 ✓)",              INK),
            ("Answer:", "(x + 2)(x + 3)",                            CRIMSON),
            ("Check:",  "x²+3x+2x+6 = x²+5x+6  ✓",                 INK),
        ]
        y_top = 2.2
        for i, (step, result, clr) in enumerate(steps):
            y = y_top - i * 0.78
            s = Text(step, font="Prism", font_size=15, color=SLATE, weight=BOLD)
            s.move_to([-5.5, y, 0], aligned_edge=LEFT)
            r = Text(result, font="Prism", font_size=17, color=clr)
            r.move_to([-2.8, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(s), FadeIn(r), run_time=0.3)

        box = Rectangle(width=3.0, height=0.7, fill_color=GOLD,
                        fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        box.move_to([0, -2.5, 0])
        box_lbl = Text("(x+2)(x+3)", font="Prism", font_size=24, color=CRIMSON, weight=BOLD)
        box_lbl.move_to([0, -2.5, 0])
        self.play(GrowFromCenter(box), run_time=0.4)
        self.play(FadeIn(box_lbl), run_time=0.3)
        self.wait(max(0, dur - len(steps) * 0.3 - 1.5))
