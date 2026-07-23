import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# beta-carotene-false-positive — Research Cancer Epidemiology and the Beta-Carotene False Positive
# CANCER BIOLOGY · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_BradfordHillChecklist(Scene):
    def construct(self):
        d = DUR.get('B04', 14)
        title = Text("Bradford Hill Criteria: Beta-Carotene", font=SERIF, color=INK, font_size=24, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        criteria = [
            ("Strength of association", "pass"),
            ("Consistency", "pass"),
            ("Specificity", "pass"),
            ("Temporality", "pass"),
            ("Biological gradient", "pass"),
            ("Experiment", "REVERSED"),
        ]
        y_start = 2.0
        y_step = 0.72
        for i, (criterion, verdict) in enumerate(criteria):
            y = y_start - i * y_step
            is_fail = verdict == "REVERSED"
            clr = CRIMSON if is_fail else INK
            box = Rectangle(width=5.8, height=0.55)
            box.set_fill(GOLD if is_fail else WHITE, 0.5 if is_fail else 0)
            box.set_stroke(clr, 1.8)
            box.move_to([0.5, y, 0])
            crit_txt = Text(criterion, font=SERIF, color=INK, font_size=18)
            crit_txt.move_to([0.5, y, 0]).align_to(box, LEFT).shift(RIGHT * 0.2)
            verdict_txt = Text(verdict, font=SERIF, color=clr, font_size=18, weight="BOLD" if is_fail else "NORMAL")
            verdict_txt.move_to([0.5, y, 0]).align_to(box, RIGHT).shift(LEFT * 0.2)
            self.play(Create(box), FadeIn(crit_txt), FadeIn(verdict_txt), run_time=0.38)

        note = Text("+17-28% lung cancer risk in smokers (ATBC, CARET)", font=SERIF, color=CRIMSON, font_size=17)
        note.move_to(DOWN * 2.4)
        self.play(FadeIn(note, shift=DOWN * 0.2), run_time=0.35)
        self.wait(max(0.1, d - 8.0))


class B06_BradfordHillChecklist2(Scene):
    def construct(self):
        d = DUR.get('B06', 12)
        title = Text("Same Pattern: Vitamin D", font=SERIF, color=INK, font_size=26, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        rows = [
            ("Observational signal", "lower cancer risk in high-vit-D populations", INK),
            ("Biological plausibility", "VDR in most cancer-relevant cell types", INK),
            ("Experiment (VITAL trial)", "no significant cancer risk reduction", CRIMSON),
        ]
        y_start = 1.5
        y_step = 1.0
        for i, (label, finding, clr) in enumerate(rows):
            y = y_start - i * y_step
            box = Rectangle(width=6.5, height=0.75)
            box.set_fill(GOLD if clr == CRIMSON else WHITE, 0.4 if clr == CRIMSON else 0)
            box.set_stroke(clr, 1.8)
            box.move_to([0, y, 0])
            top_txt = Text(label, font=SERIF, color=SLATE, font_size=16, weight="BOLD")
            top_txt.move_to([0, y + 0.14, 0])
            bot_txt = Text(finding, font=SERIF, color=clr, font_size=16)
            bot_txt.move_to([0, y - 0.14, 0])
            self.play(Create(box), FadeIn(top_txt), FadeIn(bot_txt), run_time=0.45)

        note = Text("Confounding satisfies every criterion except Experiment", font=SERIF, color=SLATE, font_size=18)
        note.move_to(DOWN * 2.2)
        self.play(FadeIn(note, shift=DOWN * 0.2), run_time=0.35)
        self.wait(max(0.1, d - 5.5))
