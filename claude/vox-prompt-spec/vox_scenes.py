"""vox_scenes.py — Why 'Make This Better' Is Not a Prompt
(vox-prompt-spec, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = specified / inspectable / correct output;
           CRIMSON = vague / generic / wrong for context.
Never swap mid-film.

Exclusions: NO deep XML tag syntax tutorial, NO prompting-framework
literature comparison, NO extended chain-of-thought research.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 10.0, "B05": 11.0,
    "B06": 11.0, "B07": 11.0, "B08": 11.0, "B09": 10.0,
    "B10": 10.0, "B11": 10.0, "B12": 10.0, "B14": 11.0,
    "B15": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- B01 — opening scenario

class B01_OpeningScenario(Scene):
    def construct(self):
        total = DUR["B01"]

        # Chat bubble shape
        bubble = Rectangle(width=5.5, height=1.1)
        bubble.set_fill(SLATE, 0.10).set_stroke(SLATE, 1.5)
        bubble.move_to(UP * 1.3)

        request_text = Text("Can you improve my methods section?",
                            font=SERIF, color=INK, font_size=20)
        request_text.move_to(bubble)

        output_chip = LabelChip("POLISHED REWRITE", accent=TEAL, size=22)
        output_chip.move_to(DOWN * 0.1)

        wrong_chip = LabelChip("WRONG FOR HER JOURNAL", accent=CRIMSON, size=20)
        wrong_chip.move_to(DOWN * 1.1)

        note = SerifLabel("fluent — and wrong", CRIMSON, size=22)
        note.move_to(DOWN * 1.95)

        self.play(FadeIn(bubble), run_time=0.5)
        self.play(FadeIn(request_text), run_time=0.5)
        self.play(FadeIn(output_chip), run_time=0.5)
        self.play(FadeIn(wrong_chip), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.4))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Why did 'improve this'", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("produce the wrong improvement?", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.16, q2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B04 — naive model

class B04_NaiveModel(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = Text("THE NAIVE EXPECTATION", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.7)

        vague_chip = LabelChip("VAGUE REQUEST", accent=CRIMSON, size=24)
        vague_chip.move_to(LEFT * 3.3)

        arrow = Arrow(LEFT * 1.7, RIGHT * 0.5,
                      color=TEAL, stroke_width=3, buff=0.0)

        right_chip = LabelChip("RIGHT IMPROVEMENT", accent=TEAL, size=22)
        right_chip.move_to(RIGHT * 2.8)

        naive_label = SerifLabel("model infers context automatically", SLATE, size=22)
        naive_label.move_to(ORIGIN + DOWN * 1.3)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(vague_chip), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(right_chip), run_time=0.5)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


# ---------------------------------------------------------------- B05 — frame completion

class B05_FrameCompletion(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("VAGUE FRAME -> GENERIC STANDARD APPLIED", font=DISPLAY,
                   color=SLATE, font_size=16, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 1.5, color=SLATE, stroke_width=0.8)
        divider.move_to(ORIGIN)

        left_head = Text("VAGUE PROMPT", font=DISPLAY, color=CRIMSON,
                         font_size=18, weight="MEDIUM")
        left_head.move_to(LEFT * 3.0 + UP * 1.4)

        left_c1 = SerifLabel("no evaluation criteria", CRIMSON, size=18)
        left_c1.move_to(LEFT * 3.0 + UP * 0.55)
        left_c2 = SerifLabel("no source constraints", CRIMSON, size=18)
        left_c2.move_to(LEFT * 3.0 + DOWN * 0.05)
        left_c3 = SerifLabel("no scope limits", CRIMSON, size=18)
        left_c3.move_to(LEFT * 3.0 + DOWN * 0.65)

        right_head = Text("GENERIC STANDARD", font=DISPLAY, color=CRIMSON,
                          font_size=18, weight="MEDIUM")
        right_head.move_to(RIGHT * 3.0 + UP * 1.4)

        right_c1 = SerifLabel("clean prose", CRIMSON, size=18)
        right_c1.move_to(RIGHT * 3.0 + UP * 0.55)
        right_c2 = SerifLabel("shorter sentences", CRIMSON, size=18)
        right_c2.move_to(RIGHT * 3.0 + DOWN * 0.05)
        right_c3 = SerifLabel("standard structure", CRIMSON, size=18)
        right_c3.move_to(RIGHT * 3.0 + DOWN * 0.65)

        note = SerifLabel("wrong for your actual situation", CRIMSON, size=20)
        note.move_to(ORIGIN + DOWN * 2.0)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(left_head), FadeIn(right_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(left_c1), FadeIn(right_c1), run_time=0.4)
        self.play(FadeIn(left_c2), FadeIn(right_c2), run_time=0.4)
        self.play(FadeIn(left_c3), FadeIn(right_c3), run_time=0.4)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B06 — specification card

class B06_SpecCard(Scene):
    def construct(self):
        total = DUR["B06"]
        t1 = Text("A prompt is a specification", font=SERIF, color=TEAL,
                  font_size=44, weight="BOLD")
        t2 = Text("of work.", font=SERIF, color=TEAL,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B07 — six components

class B07_SixComponents(Scene):
    def construct(self):
        total = DUR["B07"]
        eye = Text("SIX SPECIFICATION COMPONENTS", font=DISPLAY, color=TEAL,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Two columns of 3
        labels_left = ["TASK", "CONTEXT", "SOURCE MATERIAL"]
        labels_right = ["CONSTRAINTS", "OUTPUT FORMAT", "EVALUATION CRITERIA"]

        chips_left = VGroup(*[LabelChip(l, accent=TEAL, size=20) for l in labels_left])
        chips_left.arrange(DOWN, buff=0.28)
        chips_left.move_to(LEFT * 2.8 + DOWN * 0.1)

        # The three commonly-missing ones are on the right — use CRIMSON
        chips_right = VGroup(*[LabelChip(l, accent=CRIMSON, size=20) for l in labels_right])
        chips_right.arrange(DOWN, buff=0.28)
        chips_right.move_to(RIGHT * 2.8 + DOWN * 0.1)

        missing_label = SerifLabel("commonly missing", CRIMSON, size=20)
        missing_label.move_to(RIGHT * 2.8 + DOWN * 2.05)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips_left],
                              lag_ratio=0.1, run_time=1.0))
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips_right],
                              lag_ratio=0.1, run_time=1.0))
        self.play(FadeIn(missing_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B08 — Priya vs Rohan

class B08_PriyaRohan(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("PRIYA vs ROHAN: SAME TASK, DIFFERENT SPECIFICATIONS", font=DISPLAY,
                   color=SLATE, font_size=13, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.2, color=SLATE, stroke_width=0.8)
        divider.move_to(ORIGIN)

        priya_head = Text("PRIYA", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        priya_head.move_to(LEFT * 3.3 + UP * 1.4)

        rohan_head = Text("ROHAN", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        rohan_head.move_to(RIGHT * 3.3 + UP * 1.4)

        priya_method = Text("vague: improve this", font=SERIF, color=CRIMSON, font_size=18)
        priya_method.move_to(LEFT * 3.3 + UP * 0.65)

        rohan_method = Text("CHI venue + flag overclaims", font=SERIF, color=TEAL, font_size=18)
        rohan_method.move_to(RIGHT * 3.3 + UP * 0.65)

        priya_out = LabelChip("POLISHED REWRITE", accent=TEAL, size=18)
        priya_out.move_to(LEFT * 3.3 + DOWN * 0.15)

        rohan_out1 = LabelChip("DIAGNOSIS FIRST", accent=TEAL, size=18)
        rohan_out1.move_to(RIGHT * 3.3 + DOWN * 0.15)

        priya_warn = LabelChip("WRONG FOR CHI VENUE", accent=CRIMSON, size=16)
        priya_warn.move_to(LEFT * 3.3 + DOWN * 1.05)

        rohan_note = SerifLabel("inspectable", TEAL, size=20)
        rohan_note.move_to(RIGHT * 3.3 + DOWN * 1.05)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(priya_head), FadeIn(rohan_head), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(priya_method), FadeIn(rohan_method), run_time=0.5)
        self.play(FadeIn(priya_out), FadeIn(rohan_out1), run_time=0.5)
        self.play(FadeIn(priya_warn), FadeIn(rohan_note), run_time=0.5)
        self.wait(max(0.5, total - 2.7))


# ---------------------------------------------------------------- B09 — practice check

class B09_PracticeCheck(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("THE SPECIFICATION CHECK", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        labels = [
            "WHAT DOES BETTER MEAN HERE?",
            "WHAT SOURCE MATERIAL IS VALID?",
            "WHAT MUST IT NOT DO?",
        ]
        chips = VGroup(*[LabelChip(l, accent=TEAL, size=20) for l in labels])
        chips.arrange(DOWN, buff=0.35)
        chips.move_to(ORIGIN)

        sub = SerifLabel("before sending any prompt", TEAL, size=22)
        sub.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips],
                              lag_ratio=0.15, run_time=1.2))
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.2))


# ---------------------------------------------------------------- B10 — inspectability card

class B10_InspectCard(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Can you inspect the output", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("against your own criteria?", font=SERIF, color=TEAL,
                  font_size=42, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B11 — bad prompt card

class B11_BadPromptCard(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("A bad prompt returns", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("something polished and wrong.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B12 — work order

class B12_WorkOrder(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE WORK ORDER", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        labels = [
            "TASK",
            "CONTEXT",
            "SOURCE MATERIAL",
            "CONSTRAINTS",
            "OUTPUT FORMAT",
            "EVALUATION CRITERIA",
        ]
        chips = VGroup(*[LabelChip(l, accent=TEAL, size=20) for l in labels])
        chips.arrange(DOWN, buff=0.22)
        chips.move_to(ORIGIN + DOWN * 0.2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips],
                              lag_ratio=0.08, run_time=1.4))
        self.wait(max(0.5, total - 1.9))


# ---------------------------------------------------------------- B14 — specification failure card

class B14_SpecFailure(Scene):
    def construct(self):
        total = DUR["B14"]
        t1 = Text("The model did what you asked.", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        t2 = Text("You asked for the wrong thing.", font=SERIF, color=CRIMSON,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        u1 = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                  color=TEAL, stroke_width=2)
        u2 = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                  color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), Create(u1), run_time=0.8)
        self.play(FadeIn(t2), Create(u2), run_time=0.8)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B15 — endcard

class B15_End(Scene):
    def construct(self):
        total = DUR["B15"]

        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("State what success looks like", font=SERIF, color=INK,
                  font_size=38, weight="BOLD")
        t2 = Text("before Claude decides.", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.8))
