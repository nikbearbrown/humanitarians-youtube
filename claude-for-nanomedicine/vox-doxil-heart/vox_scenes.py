"""vox_scenes.py — Doxil's Real Job Isn't Hitting the Tumor, It's Protecting the Heart
(vox-doxil-heart, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
B02 and B06 are STILL·ai beats and have no scene here.
Durations read from this reel's beat_sheet.json.

Color law:
  TEAL   #1F6F5C = protected / spared / cardiac-safe / Doxil outcome
  CRIMSON #BF3339 = exposed / damaged / toxic / free-drug path
  GOLD   #F5D061 = single highlighter in B08 DOCUMENT beat only

Exclusions honored: no Onivyde, no Vyxeos, no three-benefit framework,
no EPR mechanism detail, no platform decision tree.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 13)}


# ---------------------------------------------------------------- helpers

def _rect(w, h, color, alpha=1.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


def _bar(height, color, width=1.2):
    b = Rectangle(width=width, height=height)
    b.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return b


def _particle(center, color=TEAL, radius=0.18):
    c = Circle(radius=radius)
    c.set_fill(color, 1).set_stroke(width=0, opacity=0)
    c.move_to(center)
    return c


def _drug_dot(center, color=CRIMSON):
    d = Dot(radius=0.07, color=color)
    d.move_to(center)
    return d


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Doxil's Real Job Isn't Hitting the Tumor —", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        t2 = Text("It's Protecting the Heart", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        panel = Rectangle(width=12.0, height=5.8)
        panel.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        panel.move_to(ORIGIN)
        q1 = Text("Doxil was approved because it delivers", font=SERIF, color=WHITE,
                  font_size=28)
        q2 = Text("doxorubicin to tumors.", font=SERIF, color=WHITE,
                  font_size=28)
        q3 = Text("But the trial outcome that got it approved", font=SERIF,
                  color=WHITE, font_size=28)
        q4 = Text("was cardiac protection.", font=SERIF, color=TEAL,
                  font_size=30, weight=BOLD)
        body = VGroup(q1, q2, q3, q4).arrange(DOWN, buff=0.22).move_to(UP * 0.55)
        dek = Text("How did fixing the tumor deliver a different organ?",
                   font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        dek.next_to(body, DOWN, buff=0.45)
        content = VGroup(body, dek)
        self.play(FadeIn(panel), run_time=0.5)
        self.play(FadeIn(body, shift=UP * 0.12), run_time=1.1)
        self.play(FadeIn(dek, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.3, total - 2.4))


class B04_DoxDistrib(Scene):
    def construct(self):
        total = DUR["B04"]
        # Central vessel bar
        vessel = _rect(0.6, 3.2, INK, alpha=0.15)
        vessel.move_to(ORIGIN)
        vessel_label = SerifLabel("bloodstream", SLATE, size=20).next_to(vessel, DOWN, buff=0.25)

        # Tumor side (left, teal)
        tumor_box = _rect(2.2, 1.8, TEAL, alpha=0.12)
        tumor_box.set_stroke(TEAL, 1.8)
        tumor_box.move_to(LEFT * 4.2 + UP * 0.2)
        tumor_label = LabelChip("TUMOR", accent=TEAL, size=24)
        tumor_label.next_to(tumor_box, UP, buff=0.2)

        # Heart side (right, crimson)
        heart_box = _rect(2.2, 1.8, CRIMSON, alpha=0.12)
        heart_box.set_stroke(CRIMSON, 1.8)
        heart_box.move_to(RIGHT * 4.2 + UP * 0.2)
        heart_label = LabelChip("HEART", accent=CRIMSON, size=24)
        heart_label.next_to(heart_box, UP, buff=0.2)

        # Drug dots fanning from vessel
        left_dots = VGroup(*[_drug_dot(LEFT * (1.2 + 0.7 * i) + UP * (0.3 - 0.2 * i), TEAL)
                              for i in range(4)])
        right_dots = VGroup(*[_drug_dot(RIGHT * (1.2 + 0.7 * i) + UP * (0.3 - 0.2 * i), CRIMSON)
                               for i in range(4)])

        note = Text("Free drug distributes everywhere", font=SERIF, color=INK,
                    font_size=22, slant=ITALIC)
        note.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(vessel), FadeIn(vessel_label), run_time=0.7)
        self.play(FadeIn(tumor_box), FadeIn(tumor_label),
                  FadeIn(heart_box), FadeIn(heart_label), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(d, scale=0.8) for d in left_dots],
                               lag_ratio=0.15),
                  LaggedStart(*[FadeIn(d, scale=0.8) for d in right_dots],
                               lag_ratio=0.15),
                  run_time=1.0)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


class B05_DoseMeter(Scene):
    def construct(self):
        total = DUR["B05"]
        # Bar background
        bg = _rect(1.6, 5.0, INK, alpha=0.08)
        bg.set_stroke("#C9C2B4", 1.6)
        bg.move_to(LEFT * 0.8 + DOWN * 0.3)

        # The fill bar (starts at bottom, grows up)
        bar_full_h = 4.4
        bar = _rect(1.4, 0.1, CRIMSON, alpha=0.9)
        bar.move_to(bg.get_bottom() + UP * 0.1)
        bar.set_stroke(width=0, opacity=0)

        # Threshold line
        threshold_y = bg.get_bottom()[1] + bar_full_h * 0.82
        thresh_line = Line(
            LEFT * 1.9 + UP * threshold_y,
            RIGHT * 0.5 + UP * threshold_y,
            color=CRIMSON, stroke_width=2.5
        )
        thresh_label = Text("360 mg/m² lifetime",
                            font=DISPLAY, color=CRIMSON, font_size=20)
        thresh_label.next_to(thresh_line, RIGHT, buff=0.2)

        # Cardiomyopathy risk label
        risk_label = LabelChip("CARDIOMYOPATHY RISK", accent=CRIMSON, size=20)
        risk_label.next_to(bg, UP, buff=0.4)

        # Axis label
        axis_label = SerifLabel("cumulative cardiac dose", SLATE, size=22)
        axis_label.next_to(bg, DOWN, buff=0.35)

        # Grow bar to full height
        bar_grown = _rect(1.4, bar_full_h, CRIMSON, alpha=0.9)
        bar_grown.move_to(bg.get_bottom() + UP * bar_full_h / 2 + UP * 0.05)
        bar_grown.set_stroke(width=0, opacity=0)

        self.play(FadeIn(bg), FadeIn(axis_label), run_time=0.7)
        self.play(ReplacementTransform(bar, bar_grown), run_time=1.6)
        self.play(Create(thresh_line), FadeIn(thresh_label), run_time=0.7)
        self.play(FadeIn(risk_label, shift=DOWN * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.6))


class B07_HeartSpared(Scene):
    def construct(self):
        total = DUR["B07"]
        # Vessel path — a horizontal line representing cardiac microvasculature
        vessel = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=3)
        vessel.move_to(UP * 0.8)
        vessel_label = SerifLabel("cardiac microvasculature", SLATE, size=20)
        vessel_label.next_to(vessel, UP, buff=0.2)

        # Heart box (right)
        heart_box = _rect(2.4, 2.2, TEAL, alpha=0.12)
        heart_box.set_stroke(TEAL, 1.8)
        heart_box.move_to(RIGHT * 3.8 + DOWN * 1.5)
        heart_label = LabelChip("HEART", accent=TEAL, size=26)
        heart_label.next_to(heart_box, DOWN, buff=0.2)
        spared_label = SerifLabel("spared", TEAL, size=24)
        spared_label.move_to(heart_box.get_center())

        # Doxil particle (teal circle) traveling along vessel
        particle = _particle(LEFT * 5.5 + UP * 0.8, TEAL, radius=0.2)
        # Drug sealed label
        sealed_chip = LabelChip("DRUG SEALED INSIDE", accent=TEAL, size=18)
        sealed_chip.next_to(particle, DOWN, buff=0.3)

        # Free drug comparison (crimson dots, bottom)
        free_label = SerifLabel("free doxorubicin (comparison)", CRIMSON, size=20)
        free_label.to_edge(DOWN, buff=1.0)
        free_dots = VGroup(*[_drug_dot(LEFT * (3.0 - 1.5 * i) + DOWN * 1.7, CRIMSON)
                              for i in range(5)])

        self.play(Create(vessel), FadeIn(vessel_label), run_time=0.7)
        self.play(FadeIn(heart_box), FadeIn(heart_label), run_time=0.6)
        self.play(FadeIn(particle), FadeIn(sealed_chip), run_time=0.6)
        # Particle moves along vessel toward (and past) heart
        self.play(
            particle.animate.shift(RIGHT * 11.0),
            sealed_chip.animate.shift(RIGHT * 11.0),
            run_time=2.0
        )
        self.play(FadeIn(spared_label, scale=0.9), run_time=0.5)
        # Show free drug comparison
        self.play(FadeIn(free_label), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(d, scale=0.8) for d in free_dots],
                               lag_ratio=0.15), run_time=0.7)
        self.wait(max(0.3, total - 5.5))


class B08_QuoteCard(Scene):
    def construct(self):
        _quote_scene(self,
                     "The primary benefit is that less drug reaches the heart.",
                     "— the clinical mechanism behind Doxil's approval",
                     None,
                     "less drug reaches the heart",
                     DUR["B08"])


class B09_MisreadingDoxil(Scene):
    def construct(self):
        total = DUR["B09"]
        # Two columns: What teams think vs What Doxil actually does
        left_header = LabelChip("WHAT TEAMS THINK", accent=CRIMSON, size=20)
        left_header.move_to(LEFT * 3.4 + UP * 2.8)

        right_header = LabelChip("WHAT DOXIL DOES", accent=TEAL, size=20)
        right_header.move_to(RIGHT * 3.4 + UP * 2.8)

        divider = Line(UP * 3.2, DOWN * 3.0, color=INK, stroke_width=1.5)
        divider.set_stroke(opacity=0.3)

        left_text = Text("EPR: drug loads the tumor", font=SERIF, color=CRIMSON,
                         font_size=26)
        left_text.move_to(LEFT * 3.4 + UP * 0.8)

        right_text = Text("Drug stays out of the heart", font=SERIF, color=TEAL,
                          font_size=26)
        right_text.move_to(RIGHT * 3.4 + UP * 0.8)

        # X over left column
        x_left = Text("X", font=DISPLAY, color=CRIMSON, font_size=80, weight=BOLD)
        x_left.move_to(LEFT * 3.4 + DOWN * 1.0)

        # Check indicator right
        check_right = Text("the win", font=DISPLAY, color=TEAL, font_size=36, weight=BOLD)
        check_right.move_to(RIGHT * 3.4 + DOWN * 1.0)
        check_u = Line(check_right.get_corner(DL) + DOWN * 0.1,
                       check_right.get_corner(DR) + DOWN * 0.1,
                       color=TEAL, stroke_width=2)

        self.play(FadeIn(divider), run_time=0.4)
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.7)
        self.play(FadeIn(left_text), FadeIn(right_text), run_time=0.8)
        self.play(FadeIn(x_left, scale=0.7), run_time=0.6)
        self.play(FadeIn(check_right), Create(check_u), run_time=0.7)
        self.wait(max(0.3, total - 3.2))


class B10_WrongTool(Scene):
    def construct(self):
        total = DUR["B10"]
        # Left box: their drug
        left_box = _rect(4.2, 3.0, CRIMSON, alpha=0.07)
        left_box.set_stroke(CRIMSON, 1.6)
        left_box.move_to(LEFT * 3.5 + UP * 0.4)

        left_title = LabelChip("THEIR DRUG", accent=SLATE, size=22)
        left_title.next_to(left_box, UP, buff=0.2)

        left_line1 = Text("No cardiac toxicity", font=SERIF, color=INK, font_size=22)
        left_line2 = Text("Solvent problem", font=SERIF, color=CRIMSON, font_size=22)
        left_lines = VGroup(left_line1, left_line2).arrange(DOWN, buff=0.3)
        left_lines.move_to(left_box.get_center())

        # Right box: Doxil solution
        right_box = _rect(4.2, 3.0, TEAL, alpha=0.07)
        right_box.set_stroke(TEAL, 1.6)
        right_box.move_to(RIGHT * 3.5 + UP * 0.4)

        right_title = LabelChip("DOXIL SOLUTION", accent=SLATE, size=22)
        right_title.next_to(right_box, UP, buff=0.2)

        right_line1 = Text("Protects the heart", font=SERIF, color=TEAL, font_size=22)
        right_line2 = Text("(from cardiac toxicity)", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        right_lines = VGroup(right_line1, right_line2).arrange(DOWN, buff=0.3)
        right_lines.move_to(right_box.get_center())

        # Mismatch X between them
        mismatch = Text("X", font=DISPLAY, color=CRIMSON, font_size=80, weight=BOLD)
        mismatch.move_to(ORIGIN + UP * 0.4)

        # Wasted time note
        waste_label = SerifLabel("one year wasted", CRIMSON, size=24)
        waste_label.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(left_box), FadeIn(left_title),
                  FadeIn(right_box), FadeIn(right_title), run_time=0.8)
        self.play(FadeIn(left_lines), FadeIn(right_lines), run_time=0.8)
        self.play(FadeIn(mismatch, scale=0.7), run_time=0.6)
        self.play(FadeIn(waste_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.8))


class B11_Example(Scene):
    def construct(self):
        total = DUR["B11"]
        # Illustrative label at top
        illus = Text("illustrative", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        illus.to_edge(UP, buff=0.4)

        # Column headers
        a_header = LabelChip("PATIENT A: FREE DOX", accent=CRIMSON, size=20)
        a_header.move_to(LEFT * 3.2 + UP * 2.6)

        b_header = LabelChip("PATIENT B: DOXIL", accent=TEAL, size=20)
        b_header.move_to(RIGHT * 3.2 + UP * 2.6)

        # 6 cycle blocks per patient
        def _cycles(color, center):
            blocks = VGroup()
            for i in range(6):
                bl = _rect(1.4, 0.28, color, alpha=0.85)
                bl.set_stroke(GROUND, 1.5)
                bl.move_to(center + DOWN * i * 0.34)
                blocks.add(bl)
            return blocks

        a_cycles = _cycles(CRIMSON, LEFT * 3.2 + UP * 1.6)
        b_cycles = _cycles(TEAL, RIGHT * 3.2 + UP * 1.6)

        # Cardiac bar — Patient A reaches threshold
        a_bar_bg = _rect(0.8, 2.8, INK, alpha=0.07)
        a_bar_bg.set_stroke("#C9C2B4", 1.4)
        a_bar_bg.move_to(LEFT * 1.4 + DOWN * 0.6)
        a_bar_fill = _rect(0.7, 2.56, CRIMSON, alpha=0.85)
        a_bar_fill.move_to(LEFT * 1.4 + DOWN * 0.68)
        a_bar_fill.set_stroke(width=0, opacity=0)
        a_thresh = Line(LEFT * 1.9, LEFT * 0.8,
                        color=CRIMSON, stroke_width=2.5)
        a_thresh.move_to(LEFT * 1.4 + DOWN * 0.68 + UP * 1.2)
        a_thresh_label = Text("360 mg/m²", font=DISPLAY, color=CRIMSON, font_size=16)
        a_thresh_label.next_to(a_thresh, RIGHT, buff=0.1)

        # Cardiac bar — Patient B lower
        b_bar_bg = _rect(0.8, 2.8, INK, alpha=0.07)
        b_bar_bg.set_stroke("#C9C2B4", 1.4)
        b_bar_bg.move_to(RIGHT * 1.4 + DOWN * 0.6)
        b_bar_fill = _rect(0.7, 1.53, TEAL, alpha=0.85)
        b_bar_fill.move_to(RIGHT * 1.4 + DOWN * 1.14)
        b_bar_fill.set_stroke(width=0, opacity=0)
        b_reduction = SerifLabel("~40% lower", TEAL, size=20)
        b_reduction.next_to(b_bar_bg, RIGHT, buff=0.15)

        # Shared bar labels
        a_bar_title = Text("cardiac", font=SERIF, color=INK, font_size=18)
        a_bar_title.next_to(a_bar_bg, UP, buff=0.18)
        b_bar_title = Text("cardiac", font=SERIF, color=INK, font_size=18)
        b_bar_title.next_to(b_bar_bg, UP, buff=0.18)

        # Same tumor response brace
        brace_group = VGroup(a_header, b_header)
        same_note = SerifLabel("same tumor response rate", SLATE, size=20)
        same_note.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(illus), run_time=0.4)
        self.play(FadeIn(a_header), FadeIn(b_header), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(bl, shift=DOWN * 0.05) for bl in a_cycles], lag_ratio=0.08),
            LaggedStart(*[FadeIn(bl, shift=DOWN * 0.05) for bl in b_cycles], lag_ratio=0.08),
            run_time=1.2
        )
        self.play(FadeIn(a_bar_bg), FadeIn(b_bar_bg),
                  FadeIn(a_bar_title), FadeIn(b_bar_title), run_time=0.7)
        self.play(FadeIn(a_bar_fill, shift=UP * 0.1), run_time=0.8)
        self.play(Create(a_thresh), FadeIn(a_thresh_label), run_time=0.5)
        self.play(FadeIn(b_bar_fill, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(b_reduction), run_time=0.5)
        self.play(FadeIn(same_note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 6.1))


class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Doxil's win: less drug to the heart —", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("not more to the tumor.", font=DISPLAY, color=CRIMSON,
                  font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))
