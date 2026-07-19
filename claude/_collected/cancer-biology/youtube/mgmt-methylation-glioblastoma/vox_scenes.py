import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# mgmt-methylation-glioblastoma — Research the MGMT Methylation Biomarker
# CANCER BIOLOGY · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_MGMTDecisionTree(Scene):
    def construct(self):
        d = DUR.get('B04', 14)
        # Root
        root_box = Rectangle(width=3.2, height=0.7).set_fill(WHITE, 0).set_stroke(INK, 2)
        root_txt = Text("GBM Patient", font=SERIF, color=INK, font_size=22)
        root_grp = VGroup(root_box, root_txt).move_to(UP * 2.8)
        self.play(Create(root_box), FadeIn(root_txt), run_time=0.4)

        # Test node
        test_box = Rectangle(width=3.8, height=0.7).set_fill(WHITE, 0).set_stroke(SLATE, 2)
        test_txt = Text("MGMT methylation test", font=SERIF, color=SLATE, font_size=20)
        test_grp = VGroup(test_box, test_txt).move_to(UP * 1.4)
        stem = Line(UP * 2.45, UP * 1.75, color=INK, stroke_width=2)
        self.play(Create(stem), run_time=0.2)
        self.play(Create(test_box), FadeIn(test_txt), run_time=0.4)

        # Left branch: methylated
        lbranch = Line(UP * 1.05, LEFT * 3.0 + UP * 0.1, color=INK, stroke_width=2)
        self.play(Create(lbranch), run_time=0.3)
        lbox = Rectangle(width=3.0, height=0.7).set_fill(WHITE, 0).set_stroke(INK, 2)
        ltxt = Text("Methylated  40-45%", font=SERIF, color=INK, font_size=18)
        VGroup(lbox, ltxt).move_to(LEFT * 3.0 + DOWN * 0.3)
        self.play(Create(lbox), FadeIn(ltxt), run_time=0.35)
        lresult = Text("+5.3 months OS", font=SERIF, color=INK, font_size=17)
        lresult.move_to(LEFT * 3.0 + DOWN * 1.1)
        self.play(FadeIn(lresult, shift=DOWN * 0.2), run_time=0.3)

        # Right branch: unmethylated
        rbranch = Line(UP * 1.05, RIGHT * 3.0 + UP * 0.1, color=CRIMSON, stroke_width=2)
        self.play(Create(rbranch), run_time=0.3)
        rbox = Rectangle(width=3.2, height=0.7).set_fill(GOLD, 0.5).set_stroke(CRIMSON, 2)
        rtxt = Text("Unmethylated  55-60%", font=SERIF, color=CRIMSON, font_size=18)
        VGroup(rbox, rtxt).move_to(RIGHT * 3.0 + DOWN * 0.3)
        self.play(Create(rbox), FadeIn(rtxt), run_time=0.35)
        rresult = Text("minimal benefit", font=SERIF, color=CRIMSON, font_size=17)
        rresult.move_to(RIGHT * 3.0 + DOWN * 1.1)
        self.play(FadeIn(rresult, shift=DOWN * 0.2), run_time=0.3)

        self.wait(max(0.1, d - 6.5))


class B06_MGMTDecisionTree2(Scene):
    def construct(self):
        d = DUR.get('B06', 12)
        title = Text("Unmethylated GBM: Trial Options", font=SERIF, color=INK, font_size=26, weight="BOLD")
        title.move_to(UP * 3.0)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        # Unmethylated node
        ubox = Rectangle(width=3.2, height=0.7).set_fill(GOLD, 0.4).set_stroke(CRIMSON, 2)
        utxt = Text("Unmethylated GBM", font=SERIF, color=CRIMSON, font_size=20)
        VGroup(ubox, utxt).move_to(UP * 1.5)
        self.play(Create(ubox), FadeIn(utxt), run_time=0.4)

        # Standard
        lbranch = Line(UP * 1.15, LEFT * 2.5 + UP * 0.3, color=INK, stroke_width=2)
        self.play(Create(lbranch), run_time=0.25)
        lb = Rectangle(width=2.8, height=0.65).set_fill(WHITE, 0).set_stroke(INK, 2)
        lt = Text("TMZ (standard)", font=SERIF, color=SLATE, font_size=18)
        VGroup(lb, lt).move_to(LEFT * 2.5 + DOWN * 0.2)
        self.play(Create(lb), FadeIn(lt), run_time=0.35)

        # Trial alternative (dashed)
        rbranch = DashedLine(UP * 1.15, RIGHT * 2.5 + UP * 0.3, color=CRIMSON, stroke_width=2)
        self.play(Create(rbranch), run_time=0.35)
        rb = Rectangle(width=3.0, height=0.65).set_fill(GOLD, 0.5).set_stroke(CRIMSON, 2)
        rt = Text("Alternative regimen (trial)", font=SERIF, color=CRIMSON, font_size=18)
        VGroup(rb, rt).move_to(RIGHT * 2.5 + DOWN * 0.2)
        self.play(Create(rb), FadeIn(rt), run_time=0.4)

        note = Text("No Phase 3 evidence for alternative yet", font=SERIF, color=SLATE, font_size=17)
        note.move_to(DOWN * 1.3)
        self.play(FadeIn(note, shift=DOWN * 0.2), run_time=0.3)
        self.wait(max(0.1, d - 5.5))
