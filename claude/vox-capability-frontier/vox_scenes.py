"""vox_scenes.py — Why AI Makes You Better At Exactly the Tasks It Makes You
Dangerously Worse At (vox-capability-frontier, slate cut, 16:9)

Color law: TEAL = inside frontier / reliable; CRIMSON = outside frontier / confident failure.
Exclusions: NO benchmark tech details, NO BCG methodology, NO task taxonomies.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 10.0, "B03": 10.0, "B04": 11.0, "B05": 12.0,
    "B06": 12.0, "B07": 12.0, "B08": 10.0, "B09": 14.0,
    "B10": 11.0, "B12": 12.0, "B13": 13.0, "B14": 13.0,
    "B15": 11.0, "B16": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _doc_chip(label, accent, width=3.6, height=2.2):
    """A document-style chip."""
    box = Rectangle(width=width, height=height)
    box.set_fill(accent, 0.12).set_stroke(accent, 1.8)
    txt = Text(label, font=SERIF, color=INK, font_size=24)
    txt.move_to(box)
    return VGroup(box, txt)


class B02_TwoOutputs(Scene):
    def construct(self):
        total = DUR["B02"]
        left = _doc_chip("DELIVERABLE A", TEAL).move_to(LEFT * 3.0)
        right = _doc_chip("DELIVERABLE B", CRIMSON).move_to(RIGHT * 3.0)
        # both look identical surface-wise — show them the same style first
        left[0].set_fill(SLATE, 0.12).set_stroke(SLATE, 1.8)
        right[0].set_fill(SLATE, 0.12).set_stroke(SLATE, 1.8)
        eye = Text("two deliverables from AI", font=SERIF, color=INK, font_size=26)
        eye.to_edge(UP, buff=0.7)
        question = Text("Which is correct?", font=SERIF, color=INK, font_size=30)
        question.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(left), FadeIn(right), run_time=0.9)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.0))


class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL, font_size=22, weight="MEDIUM")
        q1 = Text("Why didn't the quality of the output", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        q2 = Text("tell them which task was failing?", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.16, q2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


class B04_NaiveExpect(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = Text("THE NAIVE EXPECTATION", font=DISPLAY, color=SLATE, font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.7)
        correct = LabelChip("CORRECT OUTPUT", accent=TEAL, size=26)
        correct.move_to(LEFT * 3.0 + UP * 0.5)
        uncertain = LabelChip("UNCERTAIN OUTPUT", accent=SLATE, size=26)
        uncertain.move_to(RIGHT * 3.0 + UP * 0.5)
        label = SerifLabel("what we expect: wrong output feels different", SLATE, size=22)
        label.next_to(VGroup(correct, uncertain), DOWN, buff=0.6)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(correct), run_time=0.6)
        self.play(FadeIn(uncertain), run_time=0.6)
        self.play(FadeIn(label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B05_JaggedFrontier(Scene):
    def construct(self):
        total = DUR["B05"]
        # background zones
        inside_bg = Rectangle(width=6.5, height=5.5)
        inside_bg.set_fill(TEAL, 0.06).set_stroke(width=0, opacity=0)
        inside_bg.move_to(LEFT * 3.25)
        outside_bg = Rectangle(width=6.5, height=5.5)
        outside_bg.set_fill(CRIMSON, 0.06).set_stroke(width=0, opacity=0)
        outside_bg.move_to(RIGHT * 3.25)

        # jagged frontier line
        pts = [
            np.array([-0.2, 3.0, 0]),
            np.array([0.4, 1.5, 0]),
            np.array([-0.5, 0.5, 0]),
            np.array([0.6, -0.5, 0]),
            np.array([-0.3, -1.5, 0]),
            np.array([0.5, -2.8, 0]),
        ]
        frontier = VMobject(color=INK, stroke_width=5)
        frontier.set_points_smoothly(pts)

        inside_lbl = LabelChip("INSIDE", accent=TEAL, size=28)
        inside_lbl.move_to(LEFT * 3.5 + UP * 0.3)
        outside_lbl = LabelChip("OUTSIDE", accent=CRIMSON, size=28)
        outside_lbl.move_to(RIGHT * 3.5 + UP * 0.3)

        inside_sub = SerifLabel("reliable", TEAL, size=24)
        inside_sub.next_to(inside_lbl, DOWN, buff=0.3)
        outside_sub = SerifLabel("confident failure", CRIMSON, size=24)
        outside_sub.next_to(outside_lbl, DOWN, buff=0.3)

        self.play(FadeIn(inside_bg), FadeIn(outside_bg), run_time=0.6)
        self.play(Create(frontier), run_time=1.2)
        self.play(FadeIn(inside_lbl), FadeIn(outside_lbl), run_time=0.7)
        self.play(FadeIn(inside_sub), FadeIn(outside_sub), run_time=0.6)
        self.wait(max(0.5, total - 3.1))


class B06_InsideFrontier(Scene):
    def construct(self):
        total = DUR["B06"]
        zone = Rectangle(width=13.0, height=5.0)
        zone.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        zone.move_to(ORIGIN)
        chip_lbl = LabelChip("INSIDE FRONTIER", accent=TEAL, size=24)
        chip_lbl.to_edge(UP, buff=0.6)

        task = Rectangle(width=2.4, height=1.2)
        task.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.5)
        task_t = Text("TASK", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        task_t.move_to(task)
        task_g = VGroup(task, task_t).move_to(LEFT * 4.5)

        output = Rectangle(width=2.8, height=1.2)
        output.set_fill(TEAL, 0.25).set_stroke(TEAL, 2.0)
        output_t = Text("IMPROVED OUTPUT", font=DISPLAY, color=INK, font_size=20, weight="MEDIUM")
        output_t.move_to(output)
        output_g = VGroup(output, output_t).move_to(RIGHT * 4.5)

        arrow = Arrow(LEFT * 2.8, RIGHT * 2.8, color=TEAL, stroke_width=4, buff=0.0)

        self.play(FadeIn(zone), FadeIn(chip_lbl), run_time=0.7)
        self.play(FadeIn(task_g), run_time=0.5)
        self.play(Create(arrow), run_time=0.6)
        self.play(FadeIn(output_g), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B07_OutsideFrontier(Scene):
    def construct(self):
        total = DUR["B07"]
        zone = Rectangle(width=13.0, height=5.0)
        zone.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        zone.move_to(ORIGIN)
        chip_lbl = LabelChip("OUTSIDE FRONTIER", accent=CRIMSON, size=24)
        chip_lbl.to_edge(UP, buff=0.6)

        task = Rectangle(width=2.4, height=1.2)
        task.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.5)
        task_t = Text("TASK", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        task_t.move_to(task)
        task_g = VGroup(task, task_t).move_to(LEFT * 4.5)

        output = Rectangle(width=2.8, height=1.2)
        output.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.5)
        output_t = Text("OUTPUT", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        output_t.move_to(output)
        output_g = VGroup(output, output_t).move_to(RIGHT * 3.5 + UP * 0.3)

        wrong_chip = LabelChip("WRONG", accent=CRIMSON, size=26)
        wrong_chip.next_to(output_g, DOWN, buff=0.2)

        arrow = Arrow(LEFT * 2.8, RIGHT * 2.0, color=CRIMSON, stroke_width=4, buff=0.0)

        self.play(FadeIn(zone), FadeIn(chip_lbl), run_time=0.7)
        self.play(FadeIn(task_g), run_time=0.5)
        self.play(Create(arrow), run_time=0.6)
        self.play(FadeIn(output_g), run_time=0.5)
        self.play(FadeIn(wrong_chip, scale=0.8), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B08_BoundaryCard(Scene):
    def construct(self):
        total = DUR["B08"]
        t1 = Text("The boundary is not labeled", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("in the output.", font=SERIF, color=CRIMSON,
                  font_size=50, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


class B09_TwoConsultants(Scene):
    def construct(self):
        total = DUR["B09"]
        # top lane (inside)
        top_zone = Rectangle(width=12.0, height=2.2)
        top_zone.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.2).move_to(UP * 1.4)
        top_lbl = LabelChip("INSIDE FRONTIER", accent=TEAL, size=18)
        top_lbl.move_to(LEFT * 4.8 + UP * 1.4)
        top_task = Rectangle(width=1.6, height=0.8)
        top_task.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.3)
        top_task_t = Text("synthesis", font=SERIF, color=INK, font_size=18)
        top_task_t.move_to(top_task)
        top_g = VGroup(top_task, top_task_t).move_to(LEFT * 1.5 + UP * 1.4)
        top_output = Rectangle(width=2.0, height=0.8)
        top_output.set_fill(TEAL, 0.25).set_stroke(TEAL, 1.5)
        top_output_t = Text("CORRECT", font=DISPLAY, color=INK, font_size=16, weight="MEDIUM")
        top_output_t.move_to(top_output)
        top_out_g = VGroup(top_output, top_output_t).move_to(RIGHT * 3.5 + UP * 1.4)

        # bottom lane (outside)
        bot_zone = Rectangle(width=12.0, height=2.2)
        bot_zone.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.2).move_to(DOWN * 1.4)
        bot_lbl = LabelChip("OUTSIDE FRONTIER", accent=CRIMSON, size=18)
        bot_lbl.move_to(LEFT * 4.8 + DOWN * 1.4)
        bot_task = Rectangle(width=1.6, height=0.8)
        bot_task.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.3)
        bot_task_t = Text("edge case", font=SERIF, color=INK, font_size=18)
        bot_task_t.move_to(bot_task)
        bot_g = VGroup(bot_task, bot_task_t).move_to(LEFT * 1.5 + DOWN * 1.4)
        # same-looking output as top
        bot_output = Rectangle(width=2.0, height=0.8)
        bot_output.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.5)
        bot_output_t = Text("OUTPUT", font=DISPLAY, color=INK, font_size=16, weight="MEDIUM")
        bot_output_t.move_to(bot_output)
        bot_out_g = VGroup(bot_output, bot_output_t).move_to(RIGHT * 3.5 + DOWN * 1.2)
        bot_wrong = LabelChip("WRONG", accent=CRIMSON, size=16)
        bot_wrong.next_to(bot_out_g, DOWN, buff=0.15)

        self.play(FadeIn(top_zone), FadeIn(bot_zone), run_time=0.6)
        self.play(FadeIn(top_lbl), FadeIn(bot_lbl), run_time=0.5)
        self.play(FadeIn(top_g), FadeIn(bot_g), run_time=0.7)
        self.play(top_g.animate.shift(RIGHT * 4.0),
                  bot_g.animate.shift(RIGHT * 4.0), run_time=1.0)
        self.play(FadeIn(top_out_g), FadeIn(bot_out_g), run_time=0.7)
        self.play(FadeIn(bot_wrong), run_time=0.5)
        self.wait(max(0.5, total - 4.0))


class B10_TwoOutcomes(Scene):
    def construct(self):
        total = DUR["B10"]
        # left: person A (inside frontier) - better
        a_chip = LabelChip("CONSULTANT A", accent=TEAL, size=24)
        a_chip.move_to(LEFT * 3.5 + UP * 1.0)
        a_better = SerifLabel("BETTER outcome", TEAL, size=28)
        a_better.next_to(a_chip, DOWN, buff=0.55)
        a_out = LabelChip("POLISHED OUTPUT", accent=SLATE, size=18)
        a_out.next_to(a_better, DOWN, buff=0.45)

        # right: person B (outside frontier) - worse
        b_chip = LabelChip("CONSULTANT B", accent=CRIMSON, size=24)
        b_chip.move_to(RIGHT * 3.5 + UP * 1.0)
        b_worse = SerifLabel("WORSE outcome", CRIMSON, size=28)
        b_worse.next_to(b_chip, DOWN, buff=0.55)
        b_out = LabelChip("POLISHED OUTPUT", accent=SLATE, size=18)
        b_out.next_to(b_worse, DOWN, buff=0.45)

        equal_note = SerifLabel("same surface, opposite results", SLATE, size=22)
        equal_note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(a_chip), FadeIn(b_chip), run_time=0.7)
        self.play(FadeIn(a_better), FadeIn(b_worse), run_time=0.7)
        self.play(FadeIn(a_out), FadeIn(b_out), run_time=0.6)
        self.play(FadeIn(equal_note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.5))


class B12_TheMove(Scene):
    def construct(self):
        total = DUR["B12"]
        question = Text("Which zone am I in?", font=SERIF, color=INK,
                        font_size=40, weight="BOLD")
        question.to_edge(UP, buff=0.8)

        inside_chip = LabelChip("WELL-TESTED TERRITORY", accent=TEAL, size=24)
        inside_chip.move_to(LEFT * 3.2 + DOWN * 0.2)
        inside_sub = SerifLabel("seen a thousand times", TEAL, size=22)
        inside_sub.next_to(inside_chip, DOWN, buff=0.3)

        outside_chip = LabelChip("NOVEL EDGE CASE", accent=CRIMSON, size=24)
        outside_chip.move_to(RIGHT * 3.2 + DOWN * 0.2)
        outside_sub = SerifLabel("confabulating fluently", CRIMSON, size=22)
        outside_sub.next_to(outside_chip, DOWN, buff=0.3)

        self.play(FadeIn(question), run_time=0.7)
        self.play(FadeIn(inside_chip), FadeIn(outside_chip), run_time=0.7)
        self.play(FadeIn(inside_sub), FadeIn(outside_sub), run_time=0.6)
        self.wait(max(0.5, total - 2.0))


class B13_TwoGates(Scene):
    def construct(self):
        total = DUR["B13"]
        # top row: inside frontier
        top_in = LabelChip("INSIDE", accent=TEAL, size=22)
        top_in.move_to(LEFT * 4.5 + UP * 1.2)
        top_gate = Rectangle(width=2.0, height=1.0)
        top_gate.set_fill(TEAL, 0.15).set_stroke(TEAL, 2.0).move_to(UP * 1.2)
        top_gate_t = Text("SAMPLE CHECK", font=DISPLAY, color=INK, font_size=18, weight="MEDIUM")
        top_gate_t.move_to(top_gate)
        top_out = LabelChip("TRUST + VERIFY", accent=TEAL, size=22)
        top_out.move_to(RIGHT * 4.5 + UP * 1.2)
        top_arr1 = Arrow(LEFT * 2.8 + UP * 1.2, LEFT * 1.1 + UP * 1.2,
                         color=TEAL, stroke_width=3, buff=0.0)
        top_arr2 = Arrow(RIGHT * 1.1 + UP * 1.2, RIGHT * 2.8 + UP * 1.2,
                         color=TEAL, stroke_width=3, buff=0.0)

        # bottom row: outside frontier
        bot_in = LabelChip("OUTSIDE", accent=CRIMSON, size=22)
        bot_in.move_to(LEFT * 4.5 + DOWN * 1.2)
        bot_gate = Rectangle(width=2.0, height=1.0)
        bot_gate.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2.0).move_to(DOWN * 1.2)
        bot_gate_t = Text("TREAT AS DRAFT", font=DISPLAY, color=INK, font_size=18, weight="MEDIUM")
        bot_gate_t.move_to(bot_gate)
        bot_out = LabelChip("APPLY JUDGMENT", accent=CRIMSON, size=22)
        bot_out.move_to(RIGHT * 4.5 + DOWN * 1.2)
        bot_arr1 = Arrow(LEFT * 2.8 + DOWN * 1.2, LEFT * 1.1 + DOWN * 1.2,
                         color=CRIMSON, stroke_width=3, buff=0.0)
        bot_arr2 = Arrow(RIGHT * 1.1 + DOWN * 1.2, RIGHT * 2.8 + DOWN * 1.2,
                         color=CRIMSON, stroke_width=3, buff=0.0)

        self.play(FadeIn(top_in), FadeIn(bot_in), run_time=0.6)
        self.play(Create(top_arr1), Create(bot_arr1), run_time=0.5)
        self.play(FadeIn(top_gate), FadeIn(top_gate_t),
                  FadeIn(bot_gate), FadeIn(bot_gate_t), run_time=0.7)
        self.play(Create(top_arr2), Create(bot_arr2), run_time=0.5)
        self.play(FadeIn(top_out), FadeIn(bot_out), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B14_WorkedExample(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("same assignment, different zones", font=SERIF,
                   color=INK, font_size=26)
        eye.to_edge(UP, buff=0.7)

        left_chip = LabelChip("SYNTHESIS", accent=TEAL, size=26)
        left_chip.move_to(LEFT * 3.5 + UP * 0.5)
        left_sub = SerifLabel("inside frontier", TEAL, size=22)
        left_sub.next_to(left_chip, DOWN, buff=0.3)
        left_out = LabelChip("VERIFIED", accent=TEAL, size=22)
        left_out.next_to(left_sub, DOWN, buff=0.35)

        right_chip = LabelChip("NOVEL FORECAST", accent=CRIMSON, size=26)
        right_chip.move_to(RIGHT * 3.5 + UP * 0.5)
        right_sub = SerifLabel("outside frontier", CRIMSON, size=22)
        right_sub.next_to(right_chip, DOWN, buff=0.3)
        right_out = LabelChip("WRONG", accent=CRIMSON, size=22)
        right_out.next_to(right_sub, DOWN, buff=0.35)

        looks_same = SerifLabel("both outputs look equally polished", SLATE, size=22)
        looks_same.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(left_chip), FadeIn(right_chip), run_time=0.7)
        self.play(FadeIn(left_sub), FadeIn(right_sub), run_time=0.6)
        self.play(FadeIn(left_out), FadeIn(right_out), run_time=0.6)
        self.play(FadeIn(looks_same, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B15_PracticeCard(Scene):
    def construct(self):
        total = DUR["B15"]
        t1 = Text("Has the AI seen this a thousand times?", font=SERIF, color=INK,
                  font_size=38, weight="BOLD")
        t2 = Text("If not, treat it as a draft.", font=SERIF, color=CRIMSON,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


class B16_End(Scene):
    def construct(self):
        total = DUR["B16"]
        eye = Text("AGENTIC AI", font=DISPLAY, color=TEAL, font_size=22, weight="MEDIUM")
        t1 = Text("The frontier is real.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("The output won't show you where you stand.", font=SERIF, color=TEAL,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 2.2))
