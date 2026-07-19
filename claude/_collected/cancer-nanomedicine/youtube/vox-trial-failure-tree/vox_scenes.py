"""vox_scenes.py — The Cancer Trial That Couldn't Diagnose Its Own Failure
(vox-trial-failure-tree, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT beat. B02 and B11 are STILL·ai slots —
no scene classes for those. Durations read from beat_sheet.json (actuals after
audio lock; estimates as fallback).

Render everything:
  bash vox/scripts/vox_run.sh cancer-nanomedicine/youtube/vox-trial-failure-tree

Color law: TEAL = diagnosable / fix confirmed / delivery succeeded;
           CRIMSON = failure / unattributable / broken;
           GOLD = editor's pen, once (B05 quote).
           SLATE = structural boxes. GOLD never used as Text color.

Exclusions honored: NO companion diagnostic, NO accelerated approval,
NO three-arm design, NO specific assay protocols.
"""
import sys, pathlib
# resolve toolkit manim library from this file's location (works wherever the reel lives)
_TOOLKIT = pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
sys.path.insert(0, str(_TOOLKIT))
from vox_graphics import *
from vox_graphics import _quote_scene
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _box(label, color, w=2.6, h=0.72, font_size=22):
    """Filled rounded rect with a white display label inside."""
    rect = RoundedRectangle(corner_radius=0.12, width=w, height=h)
    rect.set_fill(color, 1).set_stroke(width=0, opacity=0)
    txt = Text(label.upper(), font=DISPLAY, color=WHITE,
               font_size=int(font_size * 0.88), weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(rect)
    return VGroup(rect, txt)


def _branch_line(start, end, color=CRIMSON, stroke_width=3):
    return Line(start, end, color=color, stroke_width=stroke_width)


def _fix_arrow(start, end, color=TEAL, stroke_width=3):
    return Arrow(start, end, color=color, stroke_width=stroke_width,
                 buff=0.05, tip_length=0.18)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The Cancer Trial That Couldn't", font=DISPLAY, color=INK,
                  font_size=30, weight=BOLD)
        t2 = Text("Diagnose Its Own Failure", font=DISPLAY, color=CRIMSON,
                  font_size=32, weight=BOLD)
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
        q1 = Text("A nanoparticle trial in cancer patients", font=SERIF,
                  color=INK, font_size=26)
        q2 = Text("produces a negative result.", font=SERIF,
                  color=INK, font_size=26)
        q3 = Text("Before spending $80M — what should the team", font=SERIF,
                  color=INK, font_size=26)
        q4 = Text("have measured first, and why can't the", font=SERIF,
                  color=INK, font_size=26)
        q5 = Text("response readout tell them?", font=SERIF,
                  color=CRIMSON, font_size=26, weight=BOLD)
        block = VGroup(q1, q2, q3, q4, q5).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        if block.width > 12.0:
            block.scale_to_fit_width(12.0)
        u = Line(q5.get_corner(DL) + DOWN * 0.1, q5.get_corner(DR) + DOWN * 0.1,
                 color=CRIMSON, stroke_width=1.5)
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.9)
        self.play(FadeIn(q3), FadeIn(q4), run_time=0.9)
        self.play(FadeIn(q5), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.6))


class B04_BinaryEndpoint(Scene):
    def construct(self):
        total = DUR["B04"]
        # Central endpoint box in SLATE
        center_box = _box("RESPONSE ENDPOINT", SLATE, w=3.2, h=0.76, font_size=22)
        center_box.move_to(UP * 1.2)
        # Two arms
        l_end = LEFT * 3.2 + DOWN * 0.6
        r_end = RIGHT * 3.2 + DOWN * 0.6
        fork_pt = center_box.get_bottom() + DOWN * 0.5
        line_l = Line(fork_pt, l_end, color=INK, stroke_width=2.5)
        line_r = Line(fork_pt, r_end, color=INK, stroke_width=2.5)
        worked_box = _box("WORKED", TEAL, w=2.4, h=0.66)
        worked_box.move_to(l_end + DOWN * 0.36)
        didnt_box = _box("DIDN'T", CRIMSON, w=2.4, h=0.66)
        didnt_box.move_to(r_end + DOWN * 0.36)
        lbl = SerifLabel("the only signal", INK, size=22).move_to(DOWN * 2.3)
        self.play(FadeIn(center_box, shift=DOWN * 0.2), run_time=0.7)
        self.play(Create(line_l), Create(line_r), run_time=0.7)
        self.play(FadeIn(worked_box, shift=UP * 0.15),
                  FadeIn(didnt_box, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.7))


class B05_Quote(Scene):
    def construct(self):
        _quote_scene(self,
                     "The result cannot be attributed to delivery failure,\npayload failure, or biology failure.",
                     "— Cancer Nanomedicine, Chapter 12",
                     None,
                     "attributed",
                     DUR["B05"])


class B06_ThreeFailures(Scene):
    def construct(self):
        total = DUR["B06"]
        # Top: NEGATIVE RESPONSE box
        neg_box = _box("NEGATIVE RESPONSE", CRIMSON, w=3.2, h=0.72, font_size=22)
        neg_box.move_to(UP * 2.8)
        # Three branch endpoints
        l_pos = LEFT * 4.2 + DOWN * 0.4
        c_pos = ORIGIN + DOWN * 0.4
        r_pos = RIGHT * 4.2 + DOWN * 0.4
        fork_pt = neg_box.get_bottom() + DOWN * 0.3
        # split lines from fork
        mid_l = LEFT * 2.1 + DOWN * 0.1
        mid_r = RIGHT * 2.1 + DOWN * 0.1
        h_line = Line(mid_l, mid_r, color=CRIMSON, stroke_width=3)
        h_line.move_to(fork_pt + DOWN * 0.6)
        stem = Line(fork_pt, fork_pt + DOWN * 0.6, color=CRIMSON, stroke_width=3)
        line_l = Line(h_line.get_left(), l_pos, color=CRIMSON, stroke_width=3)
        line_c = Line(h_line.get_center(), c_pos, color=CRIMSON, stroke_width=3)
        line_r = Line(h_line.get_right(), r_pos, color=CRIMSON, stroke_width=3)
        # Three failure boxes
        del_box = _box("DELIVERY\nFAILURE", CRIMSON, w=2.5, h=0.88, font_size=20)
        del_box.move_to(l_pos + DOWN * 0.46)
        pay_box = _box("PAYLOAD\nFAILURE", CRIMSON, w=2.5, h=0.88, font_size=20)
        pay_box.move_to(c_pos + DOWN * 0.46)
        bio_box = _box("BIOLOGY\nFAILURE", CRIMSON, w=2.5, h=0.88, font_size=20)
        bio_box.move_to(r_pos + DOWN * 0.46)
        self.play(FadeIn(neg_box, shift=DOWN * 0.15), run_time=0.6)
        self.play(Create(stem), run_time=0.4)
        self.play(Create(h_line), run_time=0.5)
        self.play(Create(line_l), Create(line_c), Create(line_r), run_time=0.7)
        self.play(FadeIn(del_box, shift=UP * 0.12),
                  FadeIn(pay_box, shift=UP * 0.12),
                  FadeIn(bio_box, shift=UP * 0.12), run_time=0.9)
        self.wait(max(0.3, total - 3.1))


class B07_DeliveryFailure(Scene):
    def construct(self):
        total = DUR["B07"]
        # Delivery failure branch — particle path to liver, fix arrow
        title = LabelChip("DELIVERY FAILURE", accent=CRIMSON, size=24)
        title.move_to(UP * 2.8)
        # Particle injected -> diverts to liver
        particle_lbl = SerifLabel("particle injected", INK, size=22)
        particle_lbl.move_to(LEFT * 4.8 + UP * 0.6)
        liver_box = _box("LIVER / SPLEEN", CRIMSON, w=2.8, h=0.68, font_size=20)
        liver_box.move_to(LEFT * 1.0 + UP * 0.6)
        tumor_box = _box("TUMOR", SLATE, w=2.2, h=0.68, font_size=20)
        tumor_box.move_to(RIGHT * 4.0 + UP * 0.6)
        # X on tumor box (no particle arrives)
        x_l = Line(tumor_box.get_corner(UL), tumor_box.get_corner(DR),
                   color=CRIMSON, stroke_width=3)
        x_r = Line(tumor_box.get_corner(UR), tumor_box.get_corner(DL),
                   color=CRIMSON, stroke_width=3)
        x_l._qc_intentional = True
        x_r._qc_intentional = True
        # Arrow to liver (delivery goes wrong)
        arr_liver = Arrow(particle_lbl.get_right(), liver_box.get_left(),
                          color=CRIMSON, stroke_width=3, buff=0.1, tip_length=0.18)
        # Dashed line to tumor (unreached)
        arr_tumor = DashedLine(liver_box.get_right(), tumor_box.get_left(),
                               color=SLATE, stroke_width=2, dash_length=0.18)
        # Fix arrow below
        fix_lbl = SerifLabel("PARTICLE NEVER ARRIVED", CRIMSON, size=22)
        fix_lbl.move_to(DOWN * 0.7)
        fix_arrow = _fix_arrow(DOWN * 1.5 + LEFT * 0.5, DOWN * 1.5 + RIGHT * 0.5)
        fix_chip = _box("FIX: REDESIGN THE PARTICLE", TEAL, w=3.6, h=0.66, font_size=19)
        fix_chip.move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(particle_lbl, shift=RIGHT * 0.3), run_time=0.5)
        self.play(Create(arr_liver), FadeIn(liver_box, shift=LEFT * 0.2), run_time=0.8)
        self.play(Create(arr_tumor), FadeIn(tumor_box), run_time=0.6)
        self.play(Create(x_l), Create(x_r), run_time=0.5)
        self.play(FadeIn(fix_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(Create(fix_arrow), FadeIn(fix_chip, shift=DOWN * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 4.1))


class B08_PayloadFailure(Scene):
    def construct(self):
        total = DUR["B08"]
        title = LabelChip("PAYLOAD FAILURE", accent=CRIMSON, size=24)
        title.move_to(UP * 2.8)
        # Particle arrives at tumor (delivery OK in TEAL)
        particle_lbl = SerifLabel("particle injected", INK, size=22)
        particle_lbl.move_to(LEFT * 4.8 + UP * 0.6)
        tumor_box = _box("TUMOR", TEAL, w=2.2, h=0.68, font_size=20)
        tumor_box.move_to(LEFT * 1.2 + UP * 0.6)
        arr_tumor = Arrow(particle_lbl.get_right(), tumor_box.get_left(),
                          color=TEAL, stroke_width=3, buff=0.1, tip_length=0.18)
        # Premature release — burst outside tumor cell
        burst_lbl = SerifLabel("PAYLOAD RELEASED EARLY", CRIMSON, size=22)
        burst_lbl.move_to(RIGHT * 2.8 + UP * 0.6)
        # A small starburst shape using a circle with jagged effect (approximated by polygon)
        burst = RegularPolygon(n=8, radius=0.55, color=CRIMSON)
        burst.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.5)
        burst.move_to(RIGHT * 2.8 + UP * 1.6)
        # Fix
        fix_lbl = SerifLabel("payload never reached tumor cells", CRIMSON, size=20)
        fix_lbl.move_to(DOWN * 0.7)
        fix_arrow = _fix_arrow(DOWN * 1.5 + LEFT * 0.5, DOWN * 1.5 + RIGHT * 0.5)
        fix_chip = _box("FIX: REDESIGN RELEASE MECHANISM", TEAL, w=4.0, h=0.66, font_size=18)
        fix_chip.move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(particle_lbl, shift=RIGHT * 0.3), run_time=0.5)
        self.play(Create(arr_tumor), FadeIn(tumor_box, shift=LEFT * 0.2), run_time=0.7)
        self.play(GrowFromCenter(burst), FadeIn(burst_lbl, shift=LEFT * 0.1), run_time=0.8)
        self.play(FadeIn(fix_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(Create(fix_arrow), FadeIn(fix_chip, shift=DOWN * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 3.7))


class B09_BiologyFailure(Scene):
    def construct(self):
        total = DUR["B09"]
        title = LabelChip("BIOLOGY FAILURE", accent=CRIMSON, size=24)
        title.move_to(UP * 2.8)
        # Particle path to tumor in TEAL, release in TEAL
        particle_lbl = SerifLabel("particle injected", INK, size=22)
        particle_lbl.move_to(LEFT * 4.8 + UP * 0.6)
        tumor_box = _box("TUMOR", TEAL, w=2.2, h=0.68, font_size=20)
        tumor_box.move_to(LEFT * 1.2 + UP * 0.6)
        arr_tumor = Arrow(particle_lbl.get_right(), tumor_box.get_left(),
                          color=TEAL, stroke_width=3, buff=0.1, tip_length=0.18)
        # Cell that doesn't respond — CRIMSON X
        cell_circle = Circle(radius=0.7, color=SLATE)
        cell_circle.set_fill(SLATE, 0.15).set_stroke(SLATE, 2.5)
        cell_circle.move_to(RIGHT * 2.8 + UP * 0.6)
        no_response_lbl = SerifLabel("NO RESPONSE", CRIMSON, size=22)
        no_response_lbl.move_to(RIGHT * 2.8 + UP * 1.7)
        x_l = Line(cell_circle.get_corner(UL) + RIGHT * 0.15 + DOWN * 0.15,
                   cell_circle.get_corner(DR) + LEFT * 0.15 + UP * 0.15,
                   color=CRIMSON, stroke_width=3)
        x_r = Line(cell_circle.get_corner(UR) + LEFT * 0.15 + DOWN * 0.15,
                   cell_circle.get_corner(DL) + RIGHT * 0.15 + UP * 0.15,
                   color=CRIMSON, stroke_width=3)
        x_l._qc_intentional = True
        x_r._qc_intentional = True
        # Fix
        fix_lbl = SerifLabel("delivery and release confirmed — biology resisted", CRIMSON, size=18)
        fix_lbl.move_to(DOWN * 0.7)
        fix_arrow = _fix_arrow(DOWN * 1.5 + LEFT * 0.5, DOWN * 1.5 + RIGHT * 0.5)
        fix_chip = _box("FIX: TRY A DIFFERENT TARGET", TEAL, w=3.6, h=0.66, font_size=19)
        fix_chip.move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(particle_lbl, shift=RIGHT * 0.3), run_time=0.5)
        self.play(Create(arr_tumor), FadeIn(tumor_box, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(cell_circle), run_time=0.5)
        self.play(Create(x_l), Create(x_r), FadeIn(no_response_lbl), run_time=0.7)
        self.play(FadeIn(fix_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(Create(fix_arrow), FadeIn(fix_chip, shift=DOWN * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 4.1))


class B10_FullTree(Scene):
    def construct(self):
        total = DUR["B10"]
        # "Response only" blocker at very top
        blocker = Rectangle(width=13.0, height=0.72)
        blocker.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        blocker.move_to(UP * 3.3)
        blocker_lbl = Text("RESPONSE ONLY — CANNOT SEE BELOW THIS LINE",
                           font=DISPLAY, color=CRIMSON,
                           font_size=int(14 * 0.88), weight="MEDIUM")
        blocker_lbl.move_to(blocker)
        # NEGATIVE box
        neg_box = _box("NEGATIVE RESPONSE", CRIMSON, w=3.0, h=0.66, font_size=20)
        neg_box.move_to(UP * 2.3)
        # Tree structure — compact
        fork_pt = neg_box.get_bottom() + DOWN * 0.28
        l_pos = LEFT * 4.0 + DOWN * 0.15
        c_pos = ORIGIN + DOWN * 0.15
        r_pos = RIGHT * 4.0 + DOWN * 0.15
        h_line = Line(LEFT * 2.0 + fork_pt[1] * UP + DOWN * 0.3,
                      RIGHT * 2.0 + fork_pt[1] * UP + DOWN * 0.3,
                      color=CRIMSON, stroke_width=2.5)
        stem = Line(fork_pt, h_line.get_center(), color=CRIMSON, stroke_width=2.5)
        line_l = Line(h_line.get_left(), l_pos, color=CRIMSON, stroke_width=2.5)
        line_c = Line(h_line.get_center(), c_pos, color=CRIMSON, stroke_width=2.5)
        line_r = Line(h_line.get_right(), r_pos, color=CRIMSON, stroke_width=2.5)
        # Three failure boxes (compact)
        del_box = _box("DELIVERY\nFAILURE", CRIMSON, w=2.4, h=0.82, font_size=18)
        del_box.move_to(l_pos + DOWN * 0.43)
        pay_box = _box("PAYLOAD\nFAILURE", CRIMSON, w=2.4, h=0.82, font_size=18)
        pay_box.move_to(c_pos + DOWN * 0.43)
        bio_box = _box("BIOLOGY\nFAILURE", CRIMSON, w=2.4, h=0.82, font_size=18)
        bio_box.move_to(r_pos + DOWN * 0.43)
        # TEAL fix arrows pointing down from each box
        fix_del = _fix_arrow(del_box.get_bottom() + DOWN * 0.05,
                             del_box.get_bottom() + DOWN * 0.55)
        fix_pay = _fix_arrow(pay_box.get_bottom() + DOWN * 0.05,
                             pay_box.get_bottom() + DOWN * 0.55)
        fix_bio = _fix_arrow(bio_box.get_bottom() + DOWN * 0.05,
                             bio_box.get_bottom() + DOWN * 0.55)
        fix_del_lbl = _box("FIX THE PARTICLE", TEAL, w=2.4, h=0.6, font_size=17)
        fix_del_lbl.next_to(fix_del, DOWN, buff=0.05)
        fix_pay_lbl = _box("FIX THE RELEASE", TEAL, w=2.4, h=0.6, font_size=17)
        fix_pay_lbl.next_to(fix_pay, DOWN, buff=0.05)
        fix_bio_lbl = _box("CHANGE TARGET", TEAL, w=2.4, h=0.6, font_size=17)
        fix_bio_lbl.next_to(fix_bio, DOWN, buff=0.05)
        # Build the scene
        self.play(FadeIn(blocker), FadeIn(blocker_lbl), run_time=0.6)
        self.play(FadeIn(neg_box, shift=DOWN * 0.1), run_time=0.5)
        self.play(Create(stem), run_time=0.3)
        self.play(Create(h_line), run_time=0.4)
        self.play(Create(line_l), Create(line_c), Create(line_r), run_time=0.6)
        self.play(FadeIn(del_box, shift=UP * 0.1),
                  FadeIn(pay_box, shift=UP * 0.1),
                  FadeIn(bio_box, shift=UP * 0.1), run_time=0.8)
        self.play(Create(fix_del), Create(fix_pay), Create(fix_bio), run_time=0.5)
        self.play(FadeIn(fix_del_lbl), FadeIn(fix_pay_lbl), FadeIn(fix_bio_lbl),
                  run_time=0.6)
        self.wait(max(0.3, total - 4.3))


class B12_TwoPrograms(Scene):
    def construct(self):
        total = DUR["B12"]
        # Illustrative label at top (inside safe area y <= 3.4)
        illus = LabelChip("ILLUSTRATIVE", accent=SLATE, size=20)
        illus.move_to(UP * 3.0)
        # Two column headers
        prog_a = LabelChip("PROGRAM A", accent=CRIMSON, size=22)
        prog_a.move_to(LEFT * 3.5 + UP * 2.6)
        prog_b = LabelChip("PROGRAM B", accent=TEAL, size=22)
        prog_b.move_to(RIGHT * 3.5 + UP * 2.6)
        # Divider (starts below illus label at UP * 2.5 to avoid W5 text-on-line)
        div = Line(UP * 2.5, DOWN * 3.4, color=INK, stroke_width=1.5)
        div.move_to(ORIGIN)
        # Program A content
        a_meas = SerifLabel("response only", CRIMSON, size=20)
        a_meas.move_to(LEFT * 3.5 + UP * 1.8)
        a_result = _box("7% RESPONSE", CRIMSON, w=2.6, h=0.64, font_size=20)
        a_result.move_to(LEFT * 3.5 + UP * 1.0)
        a_closed = _box("PROGRAM CLOSED", CRIMSON, w=2.6, h=0.64, font_size=18)
        a_closed.move_to(LEFT * 3.5 + UP * 0.1)
        a_note = SerifLabel("cause unknown", CRIMSON, size=18)
        a_note.move_to(LEFT * 3.5 + DOWN * 0.7)
        # Program B content (shifted up slightly to make room for bar labels)
        b_step1 = _box("TRACER COHORT FIRST", SLATE, w=3.0, h=0.60, font_size=17)
        b_step1.move_to(RIGHT * 3.5 + UP * 1.95)
        b_n = SerifLabel("10 patients", INK, size=18)
        b_n.move_to(RIGHT * 3.5 + UP * 1.35)
        # Mini bar chart: liver vs tumor
        bar_bg = Rectangle(width=2.4, height=0.55)
        bar_bg.set_fill(WHITE, 0.4).set_stroke("#C9C2B4", 1)
        bar_bg.move_to(RIGHT * 3.5 + UP * 0.65)
        liver_bar = Rectangle(width=2.4 * 0.78, height=0.41)
        liver_bar.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        liver_bar.align_to(bar_bg, LEFT).shift(RIGHT * 0.01)
        tumor_bar = Rectangle(width=2.4 * 0.04, height=0.41)
        tumor_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        tumor_bar.align_to(bar_bg, LEFT).shift(RIGHT * 0.01)
        # Bar labels as serif below bar (W6-safe: INK-based, no adrift white text)
        bar_note = SerifLabel("LIVER >75%  /  TUMOR <3%", INK, size=16)
        bar_note.next_to(bar_bg, DOWN, buff=0.1)
        b_diag = _box("DELIVERY FAILURE DIAGNOSED", CRIMSON, w=3.0, h=0.58, font_size=16)
        b_diag.move_to(RIGHT * 3.5 + DOWN * 0.3)
        b_fix = _box("REDESIGNED PEG COATING", TEAL, w=3.0, h=0.58, font_size=16)
        b_fix.move_to(RIGHT * 3.5 + DOWN * 1.05)
        b_result = _box("21% RESPONSE", TEAL, w=3.0, h=0.60, font_size=19)
        b_result.move_to(RIGHT * 3.5 + DOWN * 1.85)
        # Build sequence
        self.play(FadeIn(illus), run_time=0.4)
        self.play(FadeIn(prog_a), FadeIn(prog_b), Create(div), run_time=0.7)
        # Program A builds fast
        self.play(FadeIn(a_meas), run_time=0.4)
        self.play(FadeIn(a_result, shift=DOWN * 0.1),
                  FadeIn(a_closed, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(a_note), run_time=0.4)
        # Program B builds step by step
        self.play(FadeIn(b_step1, shift=DOWN * 0.1), FadeIn(b_n), run_time=0.6)
        self.play(FadeIn(bar_bg), FadeIn(liver_bar), FadeIn(tumor_bar),
                  FadeIn(bar_note), run_time=0.8)
        self.play(FadeIn(b_diag, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(b_fix, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(b_result, shift=DOWN * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 5.6))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("A negative result is only informative", font=DISPLAY,
                  color=INK, font_size=28, weight=BOLD)
        t2 = Text("if the trial was designed to diagnose it.", font=DISPLAY,
                  color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.1)
        if block.width > 12.5:
            block.scale_to_fit_width(12.5)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.2))
