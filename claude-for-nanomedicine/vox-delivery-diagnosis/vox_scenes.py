"""vox_scenes.py — Same Non-Response, Two Opposite Fixes: Did the Drug Fail, or
Never Arrive? (vox-delivery-diagnosis, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT beat. B02 and B08 are STILL·ai slots
and have no scene here — they compile as slates until media is dropped.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-nanomedicine/youtube/vox-delivery-diagnosis

Color law:
  TEAL   = delivery confirmed / particle in tumor / the correct fix
  CRIMSON = delivery failed / particle in liver-spleen / the wrong move
  GOLD   = editor's-pen highlighter fill ONLY (B06 DOCUMENT), never text
  SLATE  = entity/structural chips (imaging labels in B07)

Card exclusions honored: NO modality physics, NO FDG, NO activatable probes,
NO release-vs-target-engagement caveat. Binary only: delivery failure vs biology
failure, disambiguated by one image.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, json, os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 13)}


# ---------------------------------------------------------------- B01 Title (CARD)

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Same Non-Response, Two Opposite Fixes:", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        t2 = Text("Did the Drug Fail, or Never Arrive?", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B03 Question (CARD)

class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q_line1 = Text("A nanoparticle drug trial fails.", font=DISPLAY, color=INK,
                        font_size=22, weight=BOLD)
        q_line2 = Text("The team proposes switching to a more potent payload.", font=DISPLAY,
                        color=INK, font_size=20)
        q_line3 = Text("Before spending the money —", font=DISPLAY, color=INK, font_size=20)
        q_line4 = Text("what should they have measured first,", font=DISPLAY, color=CRIMSON,
                        font_size=22, weight=BOLD)
        q_line5 = Text("and why can't the response endpoint tell them?", font=DISPLAY,
                        color=CRIMSON, font_size=22, weight=BOLD)
        block = VGroup(q_line1, q_line2, q_line3, q_line4, q_line5).arrange(DOWN, buff=0.22)
        block.move_to(ORIGIN)
        u = Line(q_line5.get_corner(DL) + DOWN * 0.12,
                 q_line5.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=1.8)
        self.play(FadeIn(q_line1), run_time=0.7)
        self.play(FadeIn(VGroup(q_line2, q_line3)), run_time=0.8)
        self.play(FadeIn(VGroup(q_line4, q_line5)), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B04 TwoCauses (GRAPHIC)

class B04_TwoCauses(Scene):
    def construct(self):
        total = DUR["B04"]

        # central outcome box
        outcome_box = Rectangle(width=4.2, height=1.0)
        outcome_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2.5)
        outcome_box.move_to(DOWN * 1.8)
        outcome_label = Text("NO TUMOR SHRINKAGE", font=DISPLAY, color=CRIMSON,
                             font_size=20, weight=BOLD)
        outcome_label.move_to(outcome_box.get_center())

        # two cause chips above
        cause_left = LabelChip("Drug too weak", accent=CRIMSON, size=22)
        cause_left.move_to(UP * 1.2 + LEFT * 3.2)
        cause_right = LabelChip("Particle never arrived", accent=CRIMSON, size=22)
        cause_right.move_to(UP * 1.2 + RIGHT * 3.2)

        # arrows from causes down to outcome
        arr_left = Arrow(cause_left.get_bottom(), outcome_box.get_top() + LEFT * 1.0,
                         color=CRIMSON, stroke_width=2.5, tip_length=0.2, buff=0.12)
        arr_right = Arrow(cause_right.get_bottom(), outcome_box.get_top() + RIGHT * 1.0,
                          color=CRIMSON, stroke_width=2.5, tip_length=0.2, buff=0.12)

        # same outcome label
        same_label = SerifLabel("same outcome", CRIMSON, size=24)
        same_label.next_to(outcome_box, DOWN, buff=0.35)

        self.play(FadeIn(outcome_box), FadeIn(outcome_label), run_time=0.8)
        self.play(FadeIn(cause_left, shift=DOWN * 0.3),
                  FadeIn(cause_right, shift=DOWN * 0.3), run_time=0.7)
        self.play(Create(arr_left), Create(arr_right), run_time=0.9)
        self.play(FadeIn(same_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B05 OppositeFixes (GRAPHIC)

class B05_OppositeFixes(Scene):
    def construct(self):
        total = DUR["B05"]

        # left column: drug failure
        drug_header = LabelChip("Drug failure", accent=CRIMSON, size=22)
        drug_header.move_to(LEFT * 3.2 + UP * 2.2)
        drug_fix_label = SerifLabel("fix the drug", TEAL, size=24)
        drug_fix_label.move_to(LEFT * 3.2 + UP * 0.5)
        drug_chips = VGroup(
            LabelChip("New target", accent=TEAL, size=20),
            LabelChip("Higher potency", accent=TEAL, size=20),
        ).arrange(DOWN, buff=0.25).move_to(LEFT * 3.2 + DOWN * 0.8)

        # right column: delivery failure
        delivery_header = LabelChip("Delivery failure", accent=CRIMSON, size=22)
        delivery_header.move_to(RIGHT * 3.2 + UP * 2.2)
        delivery_fix_label = SerifLabel("fix the particle", TEAL, size=24)
        delivery_fix_label.move_to(RIGHT * 3.2 + UP * 0.5)
        delivery_chips = VGroup(
            LabelChip("PEG coating", accent=TEAL, size=20),
            LabelChip("Size", accent=TEAL, size=20),
            LabelChip("Surface chemistry", accent=TEAL, size=20),
        ).arrange(DOWN, buff=0.25).move_to(RIGHT * 3.2 + DOWN * 1.0)

        # divider
        divider = Line(UP * 2.8, DOWN * 2.8, color=INK, stroke_width=1.2)
        divider.set_stroke(opacity=0.3)

        self.play(FadeIn(divider), run_time=0.4)
        self.play(FadeIn(drug_header, shift=DOWN * 0.3),
                  FadeIn(delivery_header, shift=DOWN * 0.3), run_time=0.7)
        self.play(FadeIn(drug_fix_label), FadeIn(delivery_fix_label), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in drug_chips],
                              lag_ratio=0.15, run_time=0.8),
                  LaggedStart(*[FadeIn(c, scale=0.9) for c in delivery_chips],
                              lag_ratio=0.15, run_time=0.8))
        self.wait(max(0.5, total - 2.9))


# ---------------------------------------------------------------- B06 Quote (DOCUMENT)

class B06_QuoteToxin(Scene):
    def construct(self):
        _quote_scene(self,
                     "A more potent drug in the same particle would have loaded those organs with more toxin.",
                     "— Cancer Nanomedicine, Chapter 6",
                     None,
                     "more toxin",
                     DUR["B06"])


# ---------------------------------------------------------------- B07 LabeledParticle (GRAPHIC)

class B07_LabeledParticle(Scene):
    def construct(self):
        total = DUR["B07"]

        # particle circle at center-left
        particle = Circle(radius=0.55)
        particle.set_fill(SLATE, 0.85).set_stroke(SLATE, 2.0)
        particle.move_to(LEFT * 3.5 + UP * 0.3)

        # chip beneath the circle labels it
        particle_chip = LabelChip("Nanoparticle", accent=SLATE, size=18)
        particle_chip.next_to(particle, DOWN, buff=0.25)

        # three imaging label chips fanning out to the right
        chip_fluor = LabelChip("Fluorescent dye", accent=SLATE, size=18)
        chip_mri = LabelChip("Iron oxide (MRI)", accent=SLATE, size=18)
        chip_pet = LabelChip("Radiolabel (PET)", accent=SLATE, size=18)
        chips = VGroup(chip_fluor, chip_mri, chip_pet).arrange(DOWN, buff=0.35)
        chips.move_to(RIGHT * 1.5 + UP * 0.3)

        # lines from particle to each chip
        line_f = Line(particle.get_right(), chip_fluor.get_left() + LEFT * 0.1,
                      color=SLATE, stroke_width=1.5)
        line_m = Line(particle.get_right(), chip_mri.get_left() + LEFT * 0.1,
                      color=SLATE, stroke_width=1.5)
        line_p = Line(particle.get_right(), chip_pet.get_left() + LEFT * 0.1,
                      color=SLATE, stroke_width=1.5)

        # body outline on the right — simple rectangle representing body
        body = Rectangle(width=1.8, height=3.2)
        body.set_fill(GROUND, 1).set_stroke(INK, 1.8)
        body.set_stroke(opacity=0.4)
        body.move_to(RIGHT * 5.5 + UP * 0.0)

        # scan line that sweeps down
        scan_line = Line(body.get_left() + UP * 1.6, body.get_right() + UP * 1.6,
                         color=TEAL, stroke_width=2.5)

        scan_label = SerifLabel("track it", TEAL, size=22)
        scan_label.next_to(body, UP, buff=0.25)

        self.play(FadeIn(particle), FadeIn(particle_chip), run_time=0.7)
        self.play(Create(line_f), Create(line_m), Create(line_p), run_time=0.7)
        self.play(LaggedStart(FadeIn(chip_fluor, shift=LEFT * 0.3),
                              FadeIn(chip_mri, shift=LEFT * 0.3),
                              FadeIn(chip_pet, shift=LEFT * 0.3),
                              lag_ratio=0.2, run_time=0.9))
        self.play(FadeIn(body), FadeIn(scan_label), run_time=0.6)
        self.play(scan_line.animate.shift(DOWN * 3.2), run_time=1.8)
        self.wait(max(0.5, total - 4.7))


# ---------------------------------------------------------------- B09 DeliveryFix (GRAPHIC)

class B09_DeliveryFix(Scene):
    def construct(self):
        total = DUR["B09"]

        # header chip
        header = LabelChip("Particles in liver / spleen", accent=CRIMSON, size=22)
        header.move_to(UP * 2.5)

        # down arrow
        arr_down = Arrow(header.get_bottom(), header.get_bottom() + DOWN * 0.8,
                         color=CRIMSON, stroke_width=2.5, tip_length=0.2, buff=0.08)

        # diagnosis label
        diag = Text("DELIVERY FAILED", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        diag.move_to(UP * 0.9)

        # fix chips stacking down
        fix_header = SerifLabel("fix the particle", TEAL, size=26)
        fix_header.move_to(UP * 0.0)
        chip1 = LabelChip("Improve PEGylation", accent=TEAL, size=20)
        chip2 = LabelChip("Reduce particle size", accent=TEAL, size=20)
        chip3 = LabelChip("Adjust surface charge", accent=TEAL, size=20)
        fix_chips = VGroup(chip1, chip2, chip3).arrange(DOWN, buff=0.28)
        fix_chips.move_to(DOWN * 1.5)

        self.play(FadeIn(header, shift=DOWN * 0.3), run_time=0.6)
        self.play(Create(arr_down), run_time=0.4)
        self.play(FadeIn(diag), run_time=0.6)
        self.play(FadeIn(fix_header, shift=DOWN * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.92) for c in fix_chips],
                              lag_ratio=0.2, run_time=1.0))
        self.wait(max(0.5, total - 3.1))


# ---------------------------------------------------------------- B10 Quote (DOCUMENT)

class B10_QuoteDelivery(Scene):
    def construct(self):
        _quote_scene(self,
                     "Particles in the tumor means delivery succeeded. The payload or biology is the limiting step.",
                     "— Cancer Nanomedicine, Chapter 6",
                     None,
                     "delivery succeeded",
                     DUR["B10"])


# ---------------------------------------------------------------- B11 TwoPrograms (GRAPHIC) — THE EXAMPLE

class B11_TwoPrograms(Scene):
    def construct(self):
        total = DUR["B11"]

        # illustrative label at top
        illus = Text("illustrative", font=DISPLAY, color=SLATE, font_size=18)
        illus.set_stroke(opacity=0.6)
        illus.to_edge(UP, buff=0.35)

        # ---- Program A column (left) ----
        a_header = LabelChip("Program A", accent=CRIMSON, size=22)
        a_header.move_to(LEFT * 3.4 + UP * 1.8)

        a_method = SerifLabel("response only", CRIMSON, size=20)
        a_method.move_to(LEFT * 3.4 + UP * 0.8)

        a_result = Text("7%", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)
        a_result.move_to(LEFT * 3.4 + DOWN * 0.2)

        a_sub = Text("response", font=DISPLAY, color=CRIMSON, font_size=20)
        a_sub.next_to(a_result, DOWN, buff=0.08)

        a_outcome = LabelChip("Trial closed", accent=CRIMSON, size=22)
        a_outcome.move_to(LEFT * 3.4 + DOWN * 1.5)

        # ---- Program B column (right) ----
        b_header = LabelChip("Program B", accent=TEAL, size=22)
        b_header.move_to(RIGHT * 3.0 + UP * 1.8)

        b_method = SerifLabel("biodistribution first", TEAL, size=20)
        b_method.move_to(RIGHT * 3.0 + UP * 0.8)

        # bar chart: liver 75%+ (crimson) vs tumor <3% (teal)
        bar_liver = Rectangle(width=2.2, height=0.55)
        bar_liver.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        bar_liver.move_to(RIGHT * 2.6 + DOWN * 0.15)
        liver_label = Text("Liver  75%+", font=DISPLAY, color=CRIMSON, font_size=16)
        liver_label.next_to(bar_liver, RIGHT, buff=0.15)

        bar_tumor = Rectangle(width=0.28, height=0.55)
        bar_tumor.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        bar_tumor.move_to(RIGHT * 2.6 + DOWN * 0.85)
        tumor_label = Text("Tumor  <3%", font=DISPLAY, color=TEAL, font_size=16)
        tumor_label.next_to(bar_tumor, RIGHT, buff=0.15)

        b_fix = LabelChip("Redesign PEG", accent=TEAL, size=20)
        b_fix.move_to(RIGHT * 3.0 + DOWN * 1.5)

        b_outcome_num = Text("21%", font=DISPLAY, color=TEAL, font_size=36, weight=BOLD)
        b_outcome_num.move_to(RIGHT * 3.0 + DOWN * 2.35)
        b_outcome_sub = Text("response", font=DISPLAY, color=TEAL, font_size=18)
        b_outcome_sub.next_to(b_outcome_num, DOWN, buff=0.06)

        # divider
        div = Line(UP * 2.5, DOWN * 3.0, color=INK, stroke_width=1.2)
        div.set_stroke(opacity=0.25)

        self.play(FadeIn(illus), FadeIn(div), run_time=0.5)
        self.play(FadeIn(a_header, shift=DOWN * 0.2), FadeIn(b_header, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(a_method), FadeIn(b_method), run_time=0.6)
        self.play(FadeIn(a_result), FadeIn(a_sub), run_time=0.6)
        self.play(FadeIn(a_outcome), run_time=0.5)
        # Program B reveals: bar chart
        self.play(FadeIn(bar_liver), FadeIn(liver_label), run_time=0.7)
        self.play(FadeIn(bar_tumor), FadeIn(tumor_label), run_time=0.7)
        self.play(FadeIn(b_fix), run_time=0.5)
        self.play(FadeIn(b_outcome_num), FadeIn(b_outcome_sub), run_time=0.7)
        self.wait(max(0.5, total - 5.4))


# ---------------------------------------------------------------- B12 Endcard (CARD)

class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Measure where the particle went", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("before changing the drug.", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 1.6))
