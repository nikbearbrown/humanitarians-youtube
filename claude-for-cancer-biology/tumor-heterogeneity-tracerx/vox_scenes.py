import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# tumor-heterogeneity-tracerx — Clonal tree
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


class B04_ClonalTree(Scene):
    def construct(self):
        dur = DUR.get("B04", 22.0)
        title = Text("Tumor Heterogeneity: The TRACERx Problem",
                     font="Prism", font_size=24, color=INK, weight=BOLD)
        title.move_to([0, 3.5, 0])
        self.play(FadeIn(title), run_time=0.4)

        trunk = Rectangle(width=3.5, height=0.7, fill_color=SLATE,
                          fill_opacity=0.18, stroke_color=INK, stroke_width=2)
        trunk.move_to([0, 2.4, 0])
        trunk_lbl = Text("Trunk: TP53, KRAS  (100% of cells)", font="Prism",
                         font_size=16, color=INK)
        trunk_lbl.move_to([0, 2.4, 0])
        self.play(GrowFromCenter(trunk), run_time=0.5)
        self.play(FadeIn(trunk_lbl), run_time=0.3)

        v_line = Line(start=[0, 2.05, 0], end=[0, 1.3, 0], color=INK, stroke_width=2)
        self.play(GrowFromEdge(v_line, UP), run_time=0.3)

        h_line = Line(start=[-3.2, 1.3, 0], end=[3.2, 1.3, 0], color=INK, stroke_width=2)
        self.play(GrowFromEdge(h_line, LEFT), run_time=0.5)

        subclones = [
            (-3.2, "Subclone A\nCDKN2A loss", CRIMSON),
            ( 0.0, "Subclone B\nPIK3CA mut",  CRIMSON),
            ( 3.2, "Subclone C\nMYC amp",     CRIMSON),
        ]
        for x, label, clr in subclones:
            vl = Line(start=[x, 1.3, 0], end=[x, 0.6, 0], color=INK, stroke_width=2)
            self.play(GrowFromEdge(vl, UP), run_time=0.3)
            box = Rectangle(width=2.8, height=0.78, fill_color=CREAM,
                            fill_opacity=1, stroke_color=clr, stroke_width=2)
            box.move_to([x, 0.2, 0])
            lbl = Text(label, font="Prism", font_size=14, color=clr)
            lbl.move_to([x, 0.2, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(FadeIn(lbl), run_time=0.2)

        biopsy_arr = Arrow(start=[-3.2, -0.2, 0], end=[-3.2, -0.9, 0],
                           color=CRIMSON, stroke_width=3)
        self.play(GrowArrow(biopsy_arr), run_time=0.4)
        biopsy_lbl = Text("Single biopsy ->\nsubclone A only", font="Prism",
                          font_size=14, color=CRIMSON)
        biopsy_lbl.move_to([-3.2, -1.55, 0])
        self.play(FadeIn(biopsy_lbl), run_time=0.3)

        missed = Text("Subclones B + C: missed. Therapy targets 33% of the tumor.",
                      font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        missed.move_to([1.3, -2.7, 0])
        self.play(FadeIn(missed), run_time=0.4)
        self.wait(max(0.1, dur - 6.0))


class B06_ClonalTree2(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Solution: Multi-Region Sampling + ctDNA",
                     font="Prism", font_size=24, color=INK, weight=BOLD)
        title.move_to([0, 3.5, 0])
        self.play(FadeIn(title), run_time=0.4)

        left_hdr = Text("Single Biopsy", font="Prism", font_size=20,
                        color=CRIMSON, weight=BOLD)
        left_hdr.move_to([-3.5, 2.5, 0])
        self.play(FadeIn(left_hdr), run_time=0.3)
        left_box = Rectangle(width=4.5, height=3.5, fill_color=CREAM,
                             fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        left_box.move_to([-3.5, 0.5, 0])
        self.play(GrowFromCenter(left_box), run_time=0.4)
        left_txt = Text("Sees: trunk only\nMisses: branches A, B, C\nResult: incomplete",
                        font="Prism", font_size=15, color=INK)
        left_txt.move_to([-3.5, 0.5, 0])
        self.play(FadeIn(left_txt), run_time=0.3)

        right_hdr = Text("ctDNA + Multi-Region", font="Prism", font_size=20,
                         color=INK, weight=BOLD)
        right_hdr.move_to([3.0, 2.5, 0])
        self.play(FadeIn(right_hdr), run_time=0.3)
        right_box = Rectangle(width=4.5, height=3.5, fill_color=CREAM,
                              fill_opacity=1, stroke_color=INK, stroke_width=2)
        right_box.move_to([3.0, 0.5, 0])
        self.play(GrowFromCenter(right_box), run_time=0.4)
        right_txt = Text("Sees: trunk + all branches\nctDNA reads all subclones\nResult: complete map",
                         font="Prism", font_size=15, color=INK)
        right_txt.move_to([3.0, 0.5, 0])
        self.play(FadeIn(right_txt), run_time=0.3)

        note = Text("TRACERx: 10+ biopsies per tumor, tracking evolution in real time.",
                    font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.1, dur - 4.5))
