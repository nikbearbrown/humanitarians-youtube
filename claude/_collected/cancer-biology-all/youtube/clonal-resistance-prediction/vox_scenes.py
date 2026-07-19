import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# clonal-resistance-prediction — EGFR resistance cascade
# CANCER BIOLOGY ALL · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

INK     = "#2A1A0E"
CREAM   = "#FFFFFF"
CRIMSON = "#C8102E"
SLATE   = "#545454"
GOLD    = "#F6D8DC"


def _node(text, x, y, clr=None, font_size=16, w=3.0, h=0.65):
    clr = clr or "#2A1A0E"
    box = RoundedRectangle(corner_radius=0.14, width=w, height=h,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_color=clr, stroke_width=2)
    box.move_to([x, y, 0])
    lbl = Text(text, font="Prism", font_size=font_size, color=clr)
    lbl.move_to([x, y, 0])
    return VGroup(box, lbl)


class B04_ClonalDecisionTree(Scene):
    def construct(self):
        dur = DUR.get("B04", 22.0)
        title = Text("EGFR Resistance: The Clonal Decision Tree",
                     font="Prism", font_size=24, color=INK, weight=BOLD)
        title.move_to([0, 3.5, 0])
        self.play(FadeIn(title), run_time=0.4)

        n0 = _node("EGFR+ NSCLC", 0, 2.5, INK)
        self.play(FadeIn(n0), run_time=0.4)

        arr1 = Arrow(start=[0, 2.17, 0], end=[0, 1.55, 0], color=INK, stroke_width=2)
        lbl1 = Text("1st/2nd-gen TKI", font="Prism", font_size=13, color=SLATE)
        lbl1.next_to(arr1, RIGHT, buff=0.1)
        self.play(GrowArrow(arr1), run_time=0.4)
        self.play(FadeIn(lbl1), run_time=0.2)

        n1 = _node("Acquired Resistance", 0, 1.0, CRIMSON)
        self.play(FadeIn(n1), run_time=0.4)

        arr2a = Arrow(start=[-0.5, 0.67, 0], end=[-2.8, 0.1, 0], color=INK, stroke_width=2)
        lbl2a = Text("T790M (55%)", font="Prism", font_size=13, color=SLATE)
        lbl2a.move_to([-2.1, 0.55, 0])
        self.play(GrowArrow(arr2a), run_time=0.4)
        self.play(FadeIn(lbl2a), run_time=0.2)
        n2a = _node("Osimertinib", -2.8, -0.3, INK)
        self.play(FadeIn(n2a), run_time=0.4)

        arr2b = Arrow(start=[0.5, 0.67, 0], end=[2.8, 0.1, 0], color=INK, stroke_width=2)
        lbl2b = Text("MET/HER2 amp (20%)", font="Prism", font_size=12, color=SLATE)
        lbl2b.move_to([2.6, 0.55, 0])
        self.play(GrowArrow(arr2b), run_time=0.4)
        self.play(FadeIn(lbl2b), run_time=0.2)
        n2b = _node("No approved Rx", 2.8, -0.3, CRIMSON)
        self.play(FadeIn(n2b), run_time=0.4)

        arr3 = Arrow(start=[-2.8, -0.62, 0], end=[-2.8, -1.35, 0],
                     color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(arr3), run_time=0.3)
        n3 = _node("C797S -> Trial only", -2.8, -1.7, CRIMSON)
        self.play(FadeIn(n3), run_time=0.4)

        self.wait(max(0.1, dur - 5.5))


class B06_ClonalDecisionTree2(Scene):
    def construct(self):
        dur = DUR.get("B06", 16.0)
        title = Text("ctDNA Surveillance: The 3-6 Month Window",
                     font="Prism", font_size=24, color=INK, weight=BOLD)
        title.move_to([0, 3.5, 0])
        self.play(FadeIn(title), run_time=0.4)

        axis = Line(start=[-5.5, 1.0, 0], end=[5.5, 1.0, 0], color=INK, stroke_width=2)
        self.play(GrowFromEdge(axis, LEFT), run_time=0.6)
        axis_lbl = Text("Time on therapy ->", font="Prism", font_size=13, color=SLATE)
        axis_lbl.move_to([0, 0.55, 0])
        self.play(FadeIn(axis_lbl), run_time=0.2)

        events = [
            (-4.5, "Treatment\nstart",    INK,     1.8),
            (-1.2, "ctDNA\nrises",        CRIMSON, 0.1),
            ( 1.8, "Imaging\ndetects",    CRIMSON, 1.8),
            ( 4.5, "Clinical\nprogress",  CRIMSON, 0.1),
        ]
        for x, label, clr, y_lbl in events:
            tick = Line(start=[x, 1.15, 0], end=[x, 0.85, 0], color=clr, stroke_width=3)
            self.play(GrowFromCenter(tick), run_time=0.25)
            lbl = Text(label, font="Prism", font_size=13, color=clr)
            lbl.move_to([x, y_lbl, 0])
            self.play(FadeIn(lbl), run_time=0.2)

        window = Line(start=[-1.2, 1.0, 0], end=[1.8, 1.0, 0], color=GOLD, stroke_width=8)
        self.play(GrowFromEdge(window, LEFT), run_time=0.5)
        win_lbl = Text("3-6 mo intervention window", font="Prism",
                       font_size=14, color=CRIMSON, weight=BOLD)
        win_lbl.move_to([0.3, -0.3, 0])
        self.play(FadeIn(win_lbl), run_time=0.3)

        note = Text("Switch therapy at ctDNA rise -- before imaging progression",
                    font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        note.move_to([0, -2.8, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.1, dur - 5.0))
