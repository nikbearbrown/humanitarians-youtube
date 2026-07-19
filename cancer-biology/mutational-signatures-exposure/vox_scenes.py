import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# mutational-signatures-exposure — Research Mutational Signatures: What Can a Tumor Genome Tell You About Exposure History?
# CANCER BIOLOGY · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_MutationalSignatures(Scene):
    def construct(self):
        d = DUR.get('B04', 14)
        title = Text("Five Major Mutational Signatures", font=SERIF, color=INK, font_size=28, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)

        sigs = [
            ("SBS4", "tobacco", 3.2, INK),
            ("SBS7", "UV", 2.4, SLATE),
            ("SBS2/13", "APOBEC", 2.0, SLATE),
            ("SBS6", "MMR-defect", 3.0, CRIMSON),
            ("SBS22", "aflatoxin", 1.6, SLATE),
        ]
        baseline_y = -2.0
        bar_w = 0.9
        spacing = 2.1
        total_w = (len(sigs) - 1) * spacing
        start_x = -total_w / 2

        for i, (code, exposure, height, clr) in enumerate(sigs):
            x = start_x + i * spacing
            bar = Rectangle(width=bar_w, height=height)
            bar.set_fill(clr, 0.75 if clr == CRIMSON else 0.55)
            bar.set_stroke(clr, 1.5)
            bar.move_to([x, baseline_y + height / 2, 0])

            lbl_code = Text(code, font=SERIF, color=clr, font_size=17)
            lbl_code.move_to([x, baseline_y - 0.3, 0])
            lbl_exp = Text(exposure, font=SERIF, color=SLATE, font_size=14)
            lbl_exp.move_to([x, baseline_y - 0.7, 0])

            self.play(GrowFromEdge(bar, DOWN), run_time=0.45)
            self.play(FadeIn(lbl_code), FadeIn(lbl_exp), run_time=0.25)

        baseline = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2)
        baseline.move_to([0, baseline_y, 0])
        self.play(Create(baseline), run_time=0.3)
        self.wait(max(0.1, d - 7.5))


class B06_MutationalSignatures2(Scene):
    def construct(self):
        d = DUR.get('B06', 12)
        title = Text("SBS6: Clinically Actionable", font=SERIF, color=INK, font_size=28, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)

        # SBS6 bar
        bar = Rectangle(width=1.5, height=2.8)
        bar.set_fill(CRIMSON, 0.75).set_stroke(CRIMSON, 2)
        bar.move_to(LEFT * 2.0 + DOWN * 0.6)
        lbl = Text("SBS6  MMR-defect", font=SERIF, color=CRIMSON, font_size=22)
        lbl.move_to(LEFT * 2.0 + DOWN * 2.3)
        self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), run_time=0.6)

        # Callout
        callout_box = Rectangle(width=5.0, height=1.2)
        callout_box.set_fill(GOLD, 0.6).set_stroke(CRIMSON, 2)
        callout_box.move_to(RIGHT * 2.0 + DOWN * 0.6)
        callout_txt = Text("MSI-high detected\npembrolizumab eligible", font=SERIF, color=CRIMSON, font_size=20)
        callout_txt.move_to(RIGHT * 2.0 + DOWN * 0.6)
        self.play(Create(callout_box), run_time=0.4)
        self.play(FadeIn(callout_txt, shift=RIGHT * 0.2), run_time=0.4)

        arrow = Arrow(LEFT * 0.6 + DOWN * 0.6, RIGHT * 0.4 + DOWN * 0.6, color=CRIMSON, stroke_width=3)
        self.play(Create(arrow), run_time=0.3)
        self.wait(max(0.1, d - 4.5))
