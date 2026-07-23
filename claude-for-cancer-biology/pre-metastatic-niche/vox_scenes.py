import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# pre-metastatic-niche — Exosome schematic
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


class B04_ExosomeSchematic(Scene):
    def construct(self):
        dur = DUR.get("B04", 22.0)
        title = Text("Pre-Metastatic Niche: Real Estate Before Colonization",
                     font="Prism", font_size=21, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        nodes = [
            (-5.0, "Primary\nTumor",       INK),
            (-1.8, "Exosomes\navb5->liver", CRIMSON),
            ( 1.4, "MDSC\nRecruitment",    CRIMSON),
            ( 4.2, "CTC\nColonization",    CRIMSON),
        ]
        circles = []
        for x, label, clr in nodes:
            circ = Circle(radius=0.72, fill_color=CREAM, fill_opacity=1,
                          stroke_color=clr, stroke_width=2)
            circ.move_to([x, 0.7, 0])
            lbl = Text(label, font="Prism", font_size=13, color=clr)
            lbl.move_to([x, 0.7, 0])
            self.play(GrowFromCenter(circ), run_time=0.4)
            self.play(FadeIn(lbl), run_time=0.2)
            circles.append((x, circ))

        arrow_pairs = [
            ((-4.28, 0.7, 0), (-2.52, 0.7, 0)),
            ((-1.08, 0.7, 0), ( 0.68, 0.7, 0)),
            (( 2.12, 0.7, 0), ( 3.48, 0.7, 0)),
        ]
        for start, end in arrow_pairs:
            arr = Arrow(start=start, end=end, color=INK, stroke_width=2)
            self.play(GrowArrow(arr), run_time=0.3)

        sub_labels = [
            (-5.0, "Sheds exosomes\nwith integrin\naddress codes"),
            (-1.8, "Exosome binds\nliver; remodels\nfibronectin/ECM"),
            ( 1.4, "MDSCs recruited;\nimmuno-\nsuppressive niche"),
            ( 4.2, "CTC arrives to\nprepared zone\n-> colonizes"),
        ]
        for x, label in sub_labels:
            lbl = Text(label, font="Prism", font_size=12, color=SLATE)
            lbl.move_to([x, -1.1, 0])
            self.play(FadeIn(lbl), run_time=0.25)

        note = Text("Organ specificity encoded in exosome integrin surface -- before any cancer cell arrives.",
                    font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(max(0.1, dur - 5.0))


class B06_ExosomeSchematic2(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Blocking the Niche: Anti-Integrin Intervention",
                     font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            (-4.5, 1.4, "Tumor\nexosome",     INK),
            (-1.5, 1.4, "avb5\nbinds liver",  CRIMSON),
            ( 1.5, 1.4, "Fibronectin\ndeposited",  CRIMSON),
            ( 4.5, 1.4, "MDSC + CTC\nniche",        CRIMSON),
        ]
        for x, y, label, clr in steps:
            box = Rectangle(width=2.5, height=1.0, fill_color=CREAM,
                            fill_opacity=1, stroke_color=clr, stroke_width=2)
            box.move_to([x, y, 0])
            lbl = Text(label, font="Prism", font_size=14, color=clr)
            lbl.move_to([x, y, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(FadeIn(lbl), run_time=0.2)

        for i in range(len(steps) - 1):
            x1 = steps[i][0] + 1.25
            x2 = steps[i+1][0] - 1.25
            y  = steps[i][1]
            arr = Arrow(start=[x1, y, 0], end=[x2, y, 0], color=INK, stroke_width=2)
            self.play(GrowArrow(arr), run_time=0.3)

        block = Rectangle(width=2.5, height=0.42, fill_color=GOLD,
                          fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        block.move_to([-1.5, 2.25, 0])
        block_lbl = Text("BLOCK: anti-avb5 Ab", font="Prism",
                         font_size=13, color=CRIMSON, weight=BOLD)
        block_lbl.move_to([-1.5, 2.25, 0])
        block_arr = Arrow(start=[-1.5, 2.04, 0], end=[-1.5, 1.62, 0],
                         color=CRIMSON, stroke_width=2)
        self.play(GrowFromCenter(block), run_time=0.4)
        self.play(FadeIn(block_lbl), run_time=0.2)
        self.play(GrowArrow(block_arr), run_time=0.3)

        ev_txt = Text("Kaplan 2005 (Nature): VEGFR1 blockade prevents niche formation in vivo.",
                      font="Prism", font_size=13, color=INK)
        ev_box = SurroundingRectangle(ev_txt, color=SLATE, buff=0.2, stroke_width=1)
        VGroup(ev_txt, ev_box).move_to([0, -1.2, 0])
        self.play(GrowFromCenter(ev_box), run_time=0.4)
        self.play(FadeIn(ev_txt), run_time=0.3)

        note = Text("Block the landing zone -- not the cells that haven't arrived yet.",
                    font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(max(0.1, dur - 5.5))
