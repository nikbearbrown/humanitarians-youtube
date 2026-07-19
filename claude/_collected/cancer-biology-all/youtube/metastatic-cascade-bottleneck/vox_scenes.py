import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# metastatic-cascade-bottleneck — Metastatic funnel
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


class B04_MetastaticFunnel(Scene):
    def construct(self):
        dur = DUR.get("B04", 22.0)
        title = Text("The Metastatic Cascade: 99.99% Failure Rate",
                     font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            ("Shed from tumor",       "10^6 / day",    2.5),
            ("Survive intravasation", "~5,000",             1.5),
            ("Survive circulation",   "~500",               0.5),
            ("Extravasate",           "~50",               -0.5),
            ("Form micromet",         "~5",                -1.5),
            ("Form macrometastasis",  "~1 in 10^5",   -2.5),
        ]
        for i, (label, count, y) in enumerate(steps):
            w = 5.8 - i * 0.65
            bar = Rectangle(width=w, height=0.56, fill_color=CREAM,
                            fill_opacity=1, stroke_color=INK, stroke_width=1.5)
            bar.move_to([0, y, 0])
            lbl = Text(label, font="Prism", font_size=15, color=INK)
            lbl.move_to([-w / 2 - 0.15, y, 0], aligned_edge=RIGHT)
            cnt = Text(count, font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
            cnt.move_to([w / 2 + 0.15, y, 0], aligned_edge=LEFT)
            self.play(GrowFromCenter(bar), run_time=0.4)
            self.play(FadeIn(lbl), FadeIn(cnt), run_time=0.2)

        note = Text("< 0.001% of shed cells form distant metastases",
                    font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
        note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(max(0.1, dur - len(steps) * 0.6 - 1.2))


class B06_MetastaticFunnel2(Scene):
    def construct(self):
        dur = DUR.get("B06", 15.0)
        title = Text("Intervention Points in the Cascade",
                     font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        rows = [
            ("Shedding",        "Surgery/ablation",          INK),
            ("Intravasation",   "Anti-VEGF (bevacizumab)",   INK),
            ("Circulation",     "CTC capture (experimental)", SLATE),
            ("Extravasation",   "CXCR4 antagonists (pre-clin)", SLATE),
            ("Micromet",        "Dormancy induction (no Rx)", CRIMSON),
            ("Macrometastasis", "Systemic Rx <- target now",  CRIMSON),
        ]
        y_top = 2.5
        gap   = 0.95
        for i, (step, strategy, clr) in enumerate(rows):
            y = y_top - i * gap
            w = 5.5 - i * 0.45
            bar = Rectangle(width=w, height=0.72, fill_color=CREAM,
                            fill_opacity=1, stroke_color=clr, stroke_width=2)
            bar.move_to([-0.5, y, 0])
            step_lbl = Text(step, font="Prism", font_size=13, color=clr, weight=BOLD)
            step_lbl.move_to([-0.5, y + 0.18, 0])
            strat_lbl = Text(strategy, font="Prism", font_size=12, color=clr)
            strat_lbl.move_to([-0.5, y - 0.18, 0])
            self.play(GrowFromCenter(bar), run_time=0.4)
            self.play(FadeIn(step_lbl), FadeIn(strat_lbl), run_time=0.25)

        note = Text("Most approvals target step 6 -- the least efficient place to intervene.",
                    font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(max(0.1, dur - len(rows) * 0.65 - 1.0))
