import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# car-t-solid-tumor-barrier — CAR-T vs solid tumors
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


class B04_CARTApprovals(Scene):
    def construct(self):
        dur = DUR.get("B04", 22.0)
        data = [
            ("B-ALL (pediatric)", 85, INK),
            ("DLBCL",             40, INK),
            ("Multiple Myeloma",  73, INK),
            ("GBM (solid)",        8, CRIMSON),
            ("Pancreatic (solid)", 3, CRIMSON),
        ]
        title = Text("CAR-T: Hematologic vs. Solid Tumors", font="Prism",
                     font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.3, 0])
        self.play(FadeIn(title), run_time=0.4)

        label_x = -4.2
        bar_x0  = -3.5
        bar_max_w = 5.5
        bar_h = 0.42
        gap   = 0.9
        y_top = 2.0

        for i, (label, val, clr) in enumerate(data):
            y = y_top - i * gap
            lbl = Text(label, font="Prism", font_size=18, color=SLATE)
            lbl.move_to([label_x, y, 0], aligned_edge=RIGHT)
            self.play(FadeIn(lbl), run_time=0.2)

            bw  = (val / 100.0) * bar_max_w
            bar = Rectangle(width=bw, height=bar_h, fill_color=clr,
                            fill_opacity=0.85, stroke_width=0)
            bar.move_to([bar_x0 + bw / 2, y, 0])
            self.play(GrowFromEdge(bar, LEFT), run_time=0.5)

            pct = Text(f"{val}%", font="Prism", font_size=16, color=clr, weight=BOLD)
            pct.next_to(bar, RIGHT, buff=0.12)
            self.play(FadeIn(pct), run_time=0.2)

        sub = Text("ORR — FDA-approved indications (hematologic) vs. investigational (solid)",
                   font="Prism", font_size=13, color=SLATE)
        sub.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(sub), run_time=0.3)
        self.wait(max(0.1, dur - len(data) * 0.9 - 1.5))


class B06_CARTBarriers(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        barriers = [
            "1.  Antigen heterogeneity — not all cells express the target",
            "2.  T cell exhaustion in the immunosuppressive TME",
            "3.  Physical stroma barriers block T cell trafficking",
            "4.  Poor trafficking — CAR-T cannot find the tumor",
            "5.  On-target off-tumor toxicity limits safe dosing",
        ]
        title = Text("Why Solid Tumors Resist CAR-T", font="Prism",
                     font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.3, 0])
        self.play(FadeIn(title), run_time=0.4)

        y_top = 1.9
        gap   = 0.9
        for i, barrier in enumerate(barriers):
            y = y_top - i * gap
            dot = Dot(point=[-5.8, y, 0], color=CRIMSON, radius=0.12)
            txt = Text(barrier, font="Prism", font_size=17, color=INK)
            txt.move_to([-5.0, y, 0], aligned_edge=LEFT)
            self.play(GrowFromCenter(dot), run_time=0.25)
            self.play(FadeIn(txt), run_time=0.3)

        callout = Text("Each barrier is a separate unsolved engineering problem.",
                       font="Prism", font_size=17, color=CRIMSON, weight=BOLD)
        callout.move_to([0, -3.3, 0])
        self.play(FadeIn(callout), run_time=0.4)
        self.wait(max(0.1, dur - len(barriers) * 0.55 - 1.2))
