"""vox_scenes.py — Why Using AI More Made These Engineers Learn Less
(vox-fluency-learning, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 is a STILL · ai beat and has no scene class here.

Color law:
  TEAL   = interrogation / learning / comprehension / good trajectory
  CRIMSON= delegation / no-learning / output-only / bad trajectory
  GOLD   = fill highlight only, never text
  INK    = body text, neutral labels

Exclusions honored: no vibe-coding etymology, no AI policy debate,
no Kosmyna EEG study, no IBM hiring. One RCT only (Anthropic 2026, n=52).

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _bar(width, height, color, alpha=1.0):
    r = Rectangle(width=width, height=height)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


def _bracket_label(mob, text, color=INK, direction=UP, buff=0.22):
    brace = Brace(mob, direction, color=color)
    label = SerifLabel(text, color, size=24)
    label.next_to(brace, direction, buff=buff)
    return VGroup(brace, label)


# ================================================================ B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Why Using AI More", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Made Engineers Learn Less", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ================================================================ B03 TheQuestion

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        line1 = Text("Using AI should make you better at the task.",
                     font=SERIF, color=INK, font_size=26, weight=BOLD)
        line2 = Text("Here is the controlled experiment where it didn't.",
                     font=SERIF, color=INK, font_size=26)
        line3 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=46, weight=BOLD)
        block = VGroup(line1, line2, line3).arrange(DOWN, buff=0.28).move_to(ORIGIN)
        # gold highlight behind "Why?"
        hl = Rectangle(width=line3.width + 0.3, height=line3.height + 0.15)
        hl.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        hl.move_to(line3.get_center())
        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), run_time=0.7)
        self.play(FadeIn(hl), FadeIn(line3, scale=1.05), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


# ================================================================ B04 TheTrial

class B04_TheTrial(Scene):
    def construct(self):
        total = DUR["B04"]
        # Two panels: hand-coding group vs AI-assisted group
        panel_w, panel_h = 3.8, 3.2
        lc = LEFT * 3.2
        rc = RIGHT * 3.2

        def _panel(center, label_txt, chip_color):
            box = Rectangle(width=panel_w, height=panel_h)
            box.set_fill(WHITE, 0.25).set_stroke("#C9C2B4", 1.6)
            box.move_to(center)
            chip = LabelChip(label_txt, accent=chip_color, size=20)
            chip.next_to(box, UP, buff=0.2)
            return VGroup(box, chip)

        lpanel = _panel(lc, "hand-coding", INK)
        rpanel = _panel(rc, "AI-assisted", INK)

        # "same problem · same time" label in the seam
        seam = SerifLabel("same problem · same time", INK, size=22)
        seam.move_to(ORIGIN + UP * 1.6)

        # comprehension quiz chip at bottom
        quiz = LabelChip("comprehension quiz", accent=SLATE, size=22)
        quiz.move_to(DOWN * 2.6)

        self.play(FadeIn(lpanel, shift=RIGHT * 0.5), FadeIn(rpanel, shift=LEFT * 0.5),
                  run_time=1.0)
        self.play(FadeIn(seam), run_time=0.6)
        self.play(FadeIn(quiz, scale=0.9), run_time=0.6)
        self.wait(max(0.3, total - 2.2))


# ================================================================ B05 TheGap

class B05_TheGap(Scene):
    def construct(self):
        total = DUR["B05"]
        baseline = DOWN * 1.8
        max_h = 3.6
        bar_w = 1.6

        # bars heights proportional (67% and 50% of max_h relative to 100)
        h_hand = max_h * 0.67
        h_ai   = max_h * 0.50

        lx = LEFT * 2.2
        rx = RIGHT * 2.2

        bhand = _bar(bar_w, h_hand, TEAL)
        bhand.move_to(baseline + UP * h_hand / 2 + lx)
        bai = _bar(bar_w, h_ai, CRIMSON)
        bai.move_to(baseline + UP * h_ai / 2 + rx)

        # baseline
        bl = Line(LEFT * 4.0 + baseline, RIGHT * 4.0 + baseline,
                  color=INK, stroke_width=1.5)

        # percentage labels
        pct_hand = Text("67%", font=MONO, color=TEAL, font_size=34, weight=BOLD)
        pct_hand.next_to(bhand, UP, buff=0.18)
        pct_ai = Text("50%", font=MONO, color=CRIMSON, font_size=34, weight=BOLD)
        pct_ai.next_to(bai, UP, buff=0.18)

        # bar chips
        chip_hand = LabelChip("hand-coding", accent=TEAL, size=22)
        chip_hand.next_to(bhand, DOWN, buff=0.22)
        chip_ai = LabelChip("AI-assisted", accent=CRIMSON, size=22)
        chip_ai.next_to(bai, DOWN, buff=0.22)

        # gap bracket
        top_hand = bhand.get_top()
        top_ai = bai.get_top()
        gap_line = DashedLine(top_hand + RIGHT * (bar_w / 2 + 0.1),
                              top_ai + LEFT * (bar_w / 2 + 0.1),
                              color=INK, stroke_width=1.5, dash_length=0.15)
        gap_label = SerifLabel("17 points", INK, size=24)
        gap_label.next_to(gap_line, UP, buff=0.15)

        self.play(Create(bl), run_time=0.4)
        self.play(FadeIn(bhand, shift=UP * 0.3), FadeIn(pct_hand), FadeIn(chip_hand),
                  run_time=0.9)
        self.play(FadeIn(bai, shift=UP * 0.3), FadeIn(pct_ai), FadeIn(chip_ai),
                  run_time=0.9)
        self.play(Create(gap_line), FadeIn(gap_label), run_time=0.7)
        self.wait(max(0.3, total - 2.9))


# ================================================================ B06 InsideTheGroup

class B06_InsideTheGroup(Scene):
    def construct(self):
        total = DUR["B06"]
        baseline = DOWN * 1.8
        max_h = 3.6
        bar_w = 1.4

        # The AI-assisted bar from B05 is CRIMSON at 50%
        ai_h = max_h * 0.50
        # Split into interrogation (75% midpoint of 65–86) and delegation (32% midpoint of 24–39)
        int_h = max_h * 0.75
        del_h = max_h * 0.32

        xc = ORIGIN  # center reference

        # original AI bar
        bai = _bar(bar_w * 2.2, ai_h, CRIMSON, alpha=0.25)
        bai.move_to(baseline + UP * ai_h / 2)
        ai_chip = LabelChip("AI-assisted (avg 50%)", accent=CRIMSON, size=18)
        ai_chip.next_to(bai, DOWN, buff=0.2)

        # the two sub-bars
        lx = LEFT * 1.5
        rx = RIGHT * 1.5
        bint = _bar(bar_w, int_h, TEAL)
        bint.move_to(baseline + UP * int_h / 2 + lx)
        bdel = _bar(bar_w, del_h, CRIMSON)
        bdel.move_to(baseline + UP * del_h / 2 + rx)

        chip_int = LabelChip("interrogation", accent=TEAL, size=22)
        chip_int.next_to(bint, DOWN, buff=0.2)
        chip_del = LabelChip("delegation", accent=CRIMSON, size=22)
        chip_del.next_to(bdel, DOWN, buff=0.2)

        pct_int = Text("65-86%", font=MONO, color=TEAL, font_size=28, weight=BOLD)
        pct_int.next_to(bint, UP, buff=0.15)
        pct_del = Text("24-39%", font=MONO, color=CRIMSON, font_size=28, weight=BOLD)
        pct_del.next_to(bdel, UP, buff=0.15)

        bl = Line(LEFT * 4.5 + baseline, RIGHT * 4.5 + baseline,
                  color=INK, stroke_width=1.5)

        self.play(Create(bl), FadeIn(bai), FadeIn(ai_chip), run_time=0.8)
        self.play(FadeIn(bint, shift=UP * 0.3), FadeIn(chip_int), FadeIn(pct_int),
                  run_time=0.9)
        self.play(FadeIn(bdel, shift=UP * 0.2), FadeIn(chip_del), FadeIn(pct_del),
                  run_time=0.9)
        self.wait(max(0.3, total - 2.6))


# ================================================================ B07 ThreeBarReveal

class B07_ThreeBarReveal(Scene):
    def construct(self):
        total = DUR["B07"]
        baseline = DOWN * 1.8
        max_h = 3.8
        bar_w = 1.5

        # Three bars: hand-coding 67%, AI-interrogation ~75% (TEAL both), AI-delegation ~32% (CRIMSON)
        h_hand = max_h * 0.67
        h_int  = max_h * 0.75
        h_del  = max_h * 0.32

        lx = LEFT * 3.2
        cx = ORIGIN
        rx = RIGHT * 3.2

        bhand = _bar(bar_w, h_hand, TEAL)
        bhand.move_to(baseline + UP * h_hand / 2 + lx)
        bint = _bar(bar_w, h_int, TEAL)
        bint.move_to(baseline + UP * h_int / 2 + cx)
        bdel = _bar(bar_w, h_del, CRIMSON)
        bdel.move_to(baseline + UP * h_del / 2 + rx)

        bl = Line(LEFT * 5.0 + baseline, RIGHT * 5.0 + baseline,
                  color=INK, stroke_width=1.5)

        # reference line at ~67% height
        ref_y = baseline + UP * h_hand
        ref_line = DashedLine(lx + LEFT * 0.6 + ref_y,
                              rx + RIGHT * 0.6 + ref_y,
                              color=INK, stroke_width=1.2, dash_length=0.12)

        chip_hand = LabelChip("hand-coding", accent=TEAL, size=19)
        chip_hand.next_to(bhand, DOWN, buff=0.2)
        chip_int = LabelChip("AI + interrogation", accent=TEAL, size=19)
        chip_int.next_to(bint, DOWN, buff=0.2)
        chip_del = LabelChip("AI + delegation", accent=CRIMSON, size=19)
        chip_del.next_to(bdel, DOWN, buff=0.2)

        pct_hand = Text("67%", font=MONO, color=TEAL, font_size=30, weight=BOLD)
        pct_hand.next_to(bhand, UP, buff=0.15)
        pct_int = Text("65-86%", font=MONO, color=TEAL, font_size=26, weight=BOLD)
        pct_int.next_to(bint, UP, buff=0.15)
        pct_del = Text("24-39%", font=MONO, color=CRIMSON, font_size=30, weight=BOLD)
        pct_del.next_to(bdel, UP, buff=0.15)

        self.play(Create(bl), run_time=0.4)
        self.play(FadeIn(bhand, shift=UP * 0.3), FadeIn(chip_hand), FadeIn(pct_hand),
                  run_time=0.8)
        self.play(FadeIn(bint, shift=UP * 0.3), FadeIn(chip_int), FadeIn(pct_int),
                  run_time=0.8)
        self.play(Create(ref_line), run_time=0.5)
        self.play(FadeIn(bdel, shift=UP * 0.2), FadeIn(chip_del), FadeIn(pct_del),
                  run_time=0.8)
        self.wait(max(0.3, total - 3.3))


# ================================================================ B08 TheMechanism

class B08_TheMechanism(Scene):
    def construct(self):
        _quote_scene(self,
                     "Execution and comprehension are different events.",
                     "— the variable is what the human does while it runs",
                     GOLD,
                     "different events",
                     DUR["B08"])


# ================================================================ B09 TheImplication

class B09_TheImplication(Scene):
    def construct(self):
        total = DUR["B09"]
        baseline = DOWN * 1.8
        max_h = 3.4
        bar_w = 1.3

        h_hand = max_h * 0.67
        h_int  = max_h * 0.75
        h_del  = max_h * 0.32

        lx = LEFT * 3.0
        cx = ORIGIN
        rx = RIGHT * 3.0

        bhand = _bar(bar_w, h_hand, TEAL, alpha=0.6)
        bhand.move_to(baseline + UP * h_hand / 2 + lx)
        bint = _bar(bar_w, h_int, TEAL, alpha=0.6)
        bint.move_to(baseline + UP * h_int / 2 + cx)
        bdel = _bar(bar_w, h_del, CRIMSON, alpha=0.6)
        bdel.move_to(baseline + UP * h_del / 2 + rx)

        bl = Line(LEFT * 4.5 + baseline, RIGHT * 4.5 + baseline,
                  color=INK, stroke_width=1.5)

        chip_del = LabelChip("AI + delegation", accent=CRIMSON, size=18)
        chip_del.next_to(bdel, DOWN, buff=0.18)

        # annotation on the collapsed bar
        ann1 = SerifLabel("output is perfect", CRIMSON, size=22)
        ann1.next_to(bdel, RIGHT, buff=0.4)
        ann2 = SerifLabel("learning never happened", CRIMSON, size=22)
        ann2.next_to(ann1, DOWN, buff=0.25)

        # HandRing on the delegation bar
        ring = HandRing(bdel, color=CRIMSON)

        self.play(Create(bl), FadeIn(bhand), FadeIn(bint), FadeIn(bdel),
                  FadeIn(chip_del), run_time=1.0)
        self.play(Create(ring), run_time=1.0)
        self.play(FadeIn(ann1, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(ann2, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B10 PriyaAndJames

class B10_PriyaAndJames(Scene):
    def construct(self):
        total = DUR["B10"]

        lx = LEFT * 3.1
        rx = RIGHT * 3.1
        panel_w, panel_h = 3.4, 4.8

        # left panel: Priya / interrogation
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.8)
        lbox.move_to(lx + UP * 0.1)
        lname = LabelChip("Priya", accent=TEAL, size=26)
        lname.next_to(lbox, UP, buff=0.2)

        # steps
        lstep1 = SerifLabel("reads every line", TEAL, size=20)
        lstep2 = SerifLabel("asks why", TEAL, size=20)
        lstep3 = SerifLabel("challenges answers", TEAL, size=20)
        lsteps = VGroup(lstep1, lstep2, lstep3).arrange(DOWN, buff=0.32)
        lsteps.move_to(lx + UP * 0.6)

        # result
        lresult = Text("71%", font=MONO, color=TEAL, font_size=52, weight=BOLD)
        lresult.move_to(lx + DOWN * 1.6)
        lillus = SerifLabel("illustrative", TEAL, size=18)
        lillus.next_to(lresult, DOWN, buff=0.12)

        # right panel: James / delegation
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.8)
        rbox.move_to(rx + UP * 0.1)
        rname = LabelChip("James", accent=CRIMSON, size=26)
        rname.next_to(rbox, UP, buff=0.2)

        rstep1 = SerifLabel("pastes prompts", CRIMSON, size=20)
        rstep2 = SerifLabel("accepts outputs", CRIMSON, size=20)
        rsteps = VGroup(rstep1, rstep2).arrange(DOWN, buff=0.32)
        rsteps.move_to(rx + UP * 0.35)

        rresult = Text("31%", font=MONO, color=CRIMSON, font_size=52, weight=BOLD)
        rresult.move_to(rx + DOWN * 1.6)
        rillus = SerifLabel("illustrative", CRIMSON, size=18)
        rillus.next_to(rresult, DOWN, buff=0.12)

        # "same code on screen" label at top center
        same_label = SerifLabel("same code on screen after two hours", INK, size=20)
        same_label.to_edge(UP, buff=0.45)

        self.play(FadeIn(lbox), FadeIn(lname), FadeIn(rbox), FadeIn(rname),
                  run_time=0.8)
        self.play(FadeIn(same_label), run_time=0.5)
        self.play(FadeIn(lsteps), FadeIn(rsteps), run_time=0.8)
        self.play(FadeIn(lresult), FadeIn(rresult), run_time=0.6)
        self.play(FadeIn(lillus), FadeIn(rillus), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


# ================================================================ B11 Endcard

class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The tool was identical.", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("The checking was not.", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        sub = Text("from The Reallocation Engine", font=SERIF, color=INK, font_size=20)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.0))
