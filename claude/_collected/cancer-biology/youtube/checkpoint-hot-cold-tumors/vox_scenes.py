import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# checkpoint-hot-cold-tumors — Research Checkpoint Immunotherapy Response Rates
# CANCER BIOLOGY · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_CheckpointBarchart(Scene):
    def construct(self):
        d = DUR.get('B04', 14)
        title = Text("Anti-PD-1 Response Rates", font=SERIF, color=INK, font_size=26, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        cancers = [
            ("Hodgkin lymphoma", 0.72, "hot", CRIMSON),
            ("Melanoma", 0.40, "hot", CRIMSON),
            ("MSI-high CRC", 0.36, "hot", CRIMSON),
            ("NSCLC PD-L1 high", 0.30, "excluded", SLATE),
            ("TNBC", 0.18, "cold", SLATE),
            ("Pancreatic", 0.04, "cold", SLATE),
        ]
        max_orr = 0.72
        bar_max_w = 5.5
        bar_h = 0.52
        y_start = 2.1
        y_step = 0.8
        label_x = -3.2

        baseline = Line([label_x, y_start + 0.4, 0], [label_x, y_start - len(cancers)*y_step, 0],
                        color=INK, stroke_width=1.5)
        self.play(Create(baseline), run_time=0.3)

        for i, (name, orr, phenotype, clr) in enumerate(cancers):
            y = y_start - i * y_step
            bar_w = (orr / max_orr) * bar_max_w
            bar = Rectangle(width=bar_w, height=bar_h)
            bar.set_fill(clr, 0.7).set_stroke(clr, 1)
            bar.move_to([label_x + bar_w / 2, y, 0])

            name_lbl = Text(name, font=SERIF, color=INK, font_size=16)
            name_lbl.move_to([label_x - 0.1, y, 0])
            name_lbl.align_to([label_x - 0.15, y, 0], RIGHT)

            pct_lbl = Text(f"{int(orr*100)}%", font=MONO, color=clr, font_size=16)
            pct_lbl.move_to([label_x + bar_w + 0.3, y, 0])

            self.play(GrowFromEdge(bar, LEFT), run_time=0.3)
            self.play(FadeIn(name_lbl), FadeIn(pct_lbl), run_time=0.2)

        self.wait(max(0.1, d - 7.5))


class B06_CheckpointBarchart2(Scene):
    def construct(self):
        d = DUR.get('B06', 12)
        title = Text("Pancreatic: Cold-to-Hot Conversions", font=SERIF, color=INK, font_size=24, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        # Baseline pancreatic bar
        base_bar = Rectangle(width=0.35, height=0.6).set_fill(SLATE, 0.6).set_stroke(SLATE, 1.5)
        base_bar.move_to(LEFT * 3.0 + UP * 0.8)
        base_lbl = Text("Pancreatic alone  4%", font=SERIF, color=SLATE, font_size=19)
        base_lbl.move_to(RIGHT * 0.6 + UP * 0.8)
        self.play(GrowFromEdge(base_bar, LEFT), FadeIn(base_lbl), run_time=0.5)

        # Combination attempt note
        note_box = Rectangle(width=6.0, height=1.0).set_fill(GOLD, 0.4).set_stroke(CRIMSON, 1.5)
        note_box.move_to(DOWN * 0.5)
        note_txt = Text("Combination strategies: no Phase 3 improvement yet", font=SERIF, color=CRIMSON, font_size=19)
        note_txt.move_to(DOWN * 0.5)
        self.play(Create(note_box), run_time=0.4)
        self.play(FadeIn(note_txt, shift=UP * 0.15), run_time=0.4)

        sub = Text("STING agonists / oncolytic virus / RT + CPI -- Phase 1-2 only", font=SERIF, color=SLATE, font_size=17)
        sub.move_to(DOWN * 1.6)
        self.play(FadeIn(sub, shift=DOWN * 0.15), run_time=0.3)
        self.wait(max(0.1, d - 5.0))
