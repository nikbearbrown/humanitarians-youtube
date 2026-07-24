"""vox_scenes.py — Why the Same AI Tool Helps a Teacher and Harms a Student
(vox-phase-gate, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = capability building / human cognitive work / kept;
           CRIMSON = capability borrowing / delegated cognitive work / lost.
Never swap mid-film.

Exclusions: NO extended neuroscience of synaptic plasticity, NO specific
curriculum reform proposals, NO comparison of particular educational AI platforms.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 10.0, "B03": 10.0, "B04": 11.0, "B05": 12.0,
    "B06": 12.0, "B07": 11.0, "B08": 12.0, "B09": 13.0,
    "B10": 11.0, "B11": 12.0, "B12": 12.0, "B14": 12.0,
    "B15": 10.0, "B16": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- B01 — same tool, two outcomes

class B01_SameTool(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("SAME TOOL — TWO OUTCOMES", font=DISPLAY, color=SLATE,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.0, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        # Left: TEACHER
        teacher_head = Text("TEACHER + AI", font=DISPLAY, color=TEAL,
                            font_size=20, weight="MEDIUM")
        teacher_head.move_to(LEFT * 3.3 + UP * 1.4)
        teacher_out = LabelChip("BETTER TEACHING", accent=TEAL, size=22)
        teacher_out.move_to(LEFT * 3.3)

        # Right: STUDENT
        student_head = Text("STUDENT + AI", font=DISPLAY, color=CRIMSON,
                            font_size=20, weight="MEDIUM")
        student_head.move_to(RIGHT * 3.3 + UP * 1.4)
        student_out = LabelChip("LEARNED NOTHING", accent=CRIMSON, size=22)
        student_out.move_to(RIGHT * 3.3)

        ai_chip = LabelChip("SAME AI TOOL", accent=SLATE, size=20)
        ai_chip.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(teacher_head), FadeIn(student_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(teacher_out), run_time=0.5)
        self.play(FadeIn(student_out), run_time=0.5)
        self.play(FadeIn(ai_chip, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Same tool — one improved,", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("one was harmed. Why?", font=SERIF,
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

        teacher_chip = LabelChip("TEACHER + AI", accent=TEAL, size=22)
        teacher_chip.move_to(LEFT * 4.2 + UP * 0.5)

        student_chip = LabelChip("STUDENT + AI", accent=TEAL, size=22)
        student_chip.move_to(LEFT * 4.2 + DOWN * 0.5)

        a1 = Arrow(LEFT * 2.5 + UP * 0.5, LEFT * 0.6 + UP * 0.5,
                   color=TEAL, stroke_width=3, buff=0.0)
        a2 = Arrow(LEFT * 2.5 + DOWN * 0.5, LEFT * 0.6 + DOWN * 0.5,
                   color=TEAL, stroke_width=3, buff=0.0)

        better_chip = LabelChip("BETTER OUTCOME", accent=TEAL, size=22)
        better_chip.move_to(RIGHT * 1.2)

        naive_label = SerifLabel("the naive expectation", SLATE, size=24)
        naive_label.next_to(better_chip, DOWN, buff=0.8)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(teacher_chip), FadeIn(student_chip), run_time=0.5)
        self.play(Create(a1), Create(a2), run_time=0.6)
        self.play(FadeIn(better_chip), run_time=0.5)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


# ---------------------------------------------------------------- B05 — phase gate concept

class B05_PhaseGate(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("THE PHASE GATE", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        timeline = Line(LEFT * 5.8, RIGHT * 5.8, color=SLATE, stroke_width=2.0)
        timeline.move_to(ORIGIN)

        gate_line = Line(UP * 1.5, DOWN * 1.5, color=INK, stroke_width=3.5)
        gate_line.move_to(ORIGIN)

        ai_zone = Rectangle(width=4.8, height=1.4)
        ai_zone.set_fill(SLATE, 0.10).set_stroke(SLATE, 1.6)
        ai_zone.move_to(LEFT * 2.9)
        ai_text = Text("AI handles X", font=DISPLAY, color=INK,
                       font_size=22, weight="MEDIUM")
        ai_text.move_to(ai_zone)

        human_zone = Rectangle(width=4.8, height=1.4)
        human_zone.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.6)
        human_zone.move_to(RIGHT * 2.9)
        human_text = Text("HUMAN handles Y", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        human_text.move_to(human_zone)

        gate_label = SerifLabel("gate is at Z", TEAL, size=22)
        gate_label.next_to(gate_line, DOWN, buff=0.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(Create(timeline), run_time=0.4)
        self.play(FadeIn(ai_zone), FadeIn(ai_text), run_time=0.6)
        self.play(Create(gate_line), run_time=0.4)
        self.play(FadeIn(human_zone), FadeIn(human_text), run_time=0.6)
        self.play(FadeIn(gate_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B06 — teacher gate

class B06_TeacherGate(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("TEACHER PHASE GATE", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        timeline = Line(LEFT * 5.8, RIGHT * 5.8, color=SLATE, stroke_width=1.5)
        timeline.move_to(DOWN * 0.1)

        gate_line = Line(UP * 1.5, DOWN * 1.5, color=INK, stroke_width=3.0)
        gate_line.move_to(ORIGIN)

        ai_zone = Rectangle(width=4.8, height=2.0)
        ai_zone.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.4)
        ai_zone.move_to(LEFT * 2.9 + UP * 0.0)

        ai_chips = VGroup(
            LabelChip("QUIZ DRAFTS", accent=SLATE, size=18),
            LabelChip("SOURCES", accent=SLATE, size=18),
            LabelChip("FORMATTING", accent=SLATE, size=18),
        ).arrange(DOWN, buff=0.22)
        ai_chips.move_to(LEFT * 2.9)

        human_zone = Rectangle(width=4.8, height=2.0)
        human_zone.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.6)
        human_zone.move_to(RIGHT * 2.9)

        human_chips = VGroup(
            LabelChip("LESSON DELIVERY", accent=TEAL, size=18),
            LabelChip("STUDENT RELATIONSHIP", accent=TEAL, size=18),
        ).arrange(DOWN, buff=0.3)
        human_chips.move_to(RIGHT * 2.9)

        gate_label = SerifLabel("where teaching lives", TEAL, size=20)
        gate_label.next_to(human_zone, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(Create(timeline), run_time=0.4)
        self.play(FadeIn(ai_zone), FadeIn(ai_chips), run_time=0.6)
        self.play(Create(gate_line), run_time=0.4)
        self.play(FadeIn(human_zone), FadeIn(human_chips), run_time=0.6)
        self.play(FadeIn(gate_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B07 — substitution card

class B07_SubstitutionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("AI handling the learning work", font=SERIF, color=INK,
                  font_size=38, weight="BOLD")
        t2 = Text("is substitution, not assistance.", font=SERIF, color=CRIMSON,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B08 — student gate

class B08_StudentGate(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("STUDENT PHASE GATE", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        timeline = Line(LEFT * 5.8, RIGHT * 5.8, color=SLATE, stroke_width=1.5)
        timeline.move_to(DOWN * 0.1)

        gate_line = Line(UP * 1.5, DOWN * 1.5, color=INK, stroke_width=3.0)
        gate_line.move_to(ORIGIN)

        ai_zone = Rectangle(width=4.8, height=2.0)
        ai_zone.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.4)
        ai_zone.move_to(LEFT * 2.9)

        ai_chips = VGroup(
            LabelChip("LOCATE SOURCES", accent=SLATE, size=18),
            LabelChip("BUILD OUTLINE", accent=SLATE, size=18),
            LabelChip("FORMATTING", accent=SLATE, size=18),
        ).arrange(DOWN, buff=0.22)
        ai_chips.move_to(LEFT * 2.9)

        human_zone = Rectangle(width=4.8, height=2.0)
        human_zone.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.6)
        human_zone.move_to(RIGHT * 2.9)

        human_chips = VGroup(
            LabelChip("ARGUMENT", accent=TEAL, size=18),
            LabelChip("SYNTHESIS", accent=TEAL, size=18),
            LabelChip("REVISION", accent=TEAL, size=18),
        ).arrange(DOWN, buff=0.22)
        human_chips.move_to(RIGHT * 2.9)

        gate_label = SerifLabel("where learning lives", TEAL, size=20)
        gate_label.next_to(human_zone, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(Create(timeline), run_time=0.4)
        self.play(FadeIn(ai_zone), FadeIn(ai_chips), run_time=0.6)
        self.play(Create(gate_line), run_time=0.4)
        self.play(FadeIn(human_zone), FadeIn(human_chips), run_time=0.6)
        self.play(FadeIn(gate_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B09 — Tariq and Priya

class B09_TariqPriya(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("TARIQ vs PRIYA", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.2, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        # Column headers
        tariq_head = Text("TARIQ", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        tariq_head.move_to(LEFT * 3.3 + UP * 1.4)
        priya_head = Text("PRIYA", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        priya_head.move_to(RIGHT * 3.3 + UP * 1.4)

        # Essay row
        tariq_method = Text("AI drafts essay / 20 min", font=SERIF,
                            color=CRIMSON, font_size=18)
        tariq_method.move_to(LEFT * 3.3 + UP * 0.6)
        priya_method = Text("AI outline / 90 min writing", font=SERIF,
                            color=TEAL, font_size=18)
        priya_method.move_to(RIGHT * 3.3 + UP * 0.6)

        # Grade row
        grade_label = SerifLabel("grade:", SLATE, size=20)
        grade_label.move_to(LEFT * 5.5 + DOWN * 0.1)
        tariq_grade = Text("B+", font=MONO, color=TEAL,
                           font_size=36, weight="BOLD")
        tariq_grade.move_to(LEFT * 3.3 + DOWN * 0.1)
        priya_grade = Text("B+", font=MONO, color=TEAL,
                           font_size=36, weight="BOLD")
        priya_grade.move_to(RIGHT * 3.3 + DOWN * 0.1)

        div2 = Line(LEFT * 5.8 + DOWN * 0.6, RIGHT * 5.8 + DOWN * 0.6,
                    color=SLATE, stroke_width=0.8)

        # 3-month row
        later_label = SerifLabel("3 months later:", SLATE, size=18)
        later_label.move_to(LEFT * 5.1 + DOWN * 1.2)
        tariq_later = LabelChip("CANNOT ARGUE", accent=CRIMSON, size=18)
        tariq_later.move_to(LEFT * 3.3 + DOWN * 1.2)
        priya_later = LabelChip("CAN ARGUE", accent=TEAL, size=18)
        priya_later.move_to(RIGHT * 3.3 + DOWN * 1.2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(tariq_head), FadeIn(priya_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(tariq_method), FadeIn(priya_method), run_time=0.6)
        self.play(FadeIn(tariq_grade), FadeIn(priya_grade), FadeIn(grade_label), run_time=0.5)
        self.play(Create(div2), run_time=0.3)
        self.play(FadeIn(tariq_later), FadeIn(priya_later), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


# ---------------------------------------------------------------- B10 — gate position card

class B10_GatePositionCard(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("The gate position determines", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("whether AI amplifies or substitutes.", font=SERIF, color=TEAL,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B11 — two kinds of load

class B11_TwoKinds(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("EXTRANEOUS vs GERMANE LOAD", font=DISPLAY, color=SLATE,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Row 1: EXTRANEOUS (can delegate)
        ext_chip = LabelChip("EXTRANEOUS LOAD", accent=SLATE, size=22)
        ext_chip.move_to(LEFT * 3.8 + UP * 0.8)
        ext_desc = Text("formatting / boilerplate / organizing", font=SERIF,
                        color=INK, font_size=20)
        ext_desc.move_to(RIGHT * 1.5 + UP * 0.8)
        ext_out = LabelChip("DELEGATE TO AI", accent=TEAL, size=18)
        ext_out.next_to(ext_desc, RIGHT, buff=0.5)

        div = Line(LEFT * 5.8 + DOWN * 0.1, RIGHT * 5.8 + DOWN * 0.1,
                   color=SLATE, stroke_width=0.7)

        # Row 2: GERMANE (keep it)
        germ_chip = LabelChip("GERMANE LOAD", accent=TEAL, size=22)
        germ_chip.move_to(LEFT * 3.8 + DOWN * 0.9)
        germ_desc = Text("argument / synthesis / judgment", font=SERIF,
                         color=INK, font_size=20)
        germ_desc.move_to(RIGHT * 1.5 + DOWN * 0.9)
        germ_out = LabelChip("KEEP IT", accent=TEAL, size=18)
        germ_out.next_to(germ_desc, RIGHT, buff=0.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(ext_chip), FadeIn(ext_desc), run_time=0.6)
        self.play(FadeIn(ext_out), run_time=0.4)
        self.play(Create(div), run_time=0.3)
        self.play(FadeIn(germ_chip), FadeIn(germ_desc), run_time=0.6)
        self.play(FadeIn(germ_out), run_time=0.4)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B12 — gate placement

class B12_GatePlacement(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("PLACE THE GATE WHERE LEARNING LIVES", font=DISPLAY, color=TEAL,
                   font_size=17, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Task bar
        task_bar = Rectangle(width=11.0, height=0.8)
        task_bar.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.4)
        task_bar.move_to(UP * 0.3)

        # Learning zone (teal highlight)
        learn_zone = Rectangle(width=5.0, height=0.8)
        learn_zone.set_fill(TEAL, 0.18).set_stroke(TEAL, 1.8)
        learn_zone.move_to(RIGHT * 2.7 + UP * 0.3)

        learn_label = Text("LEARNING LIVES HERE", font=DISPLAY, color=TEAL,
                           font_size=18, weight="MEDIUM")
        learn_label.move_to(RIGHT * 2.7 + UP * 0.3)

        # Gate marker
        gate_line = Line(UP * 1.2, DOWN * 0.4, color=INK, stroke_width=3.5)
        gate_line.move_to(RIGHT * 0.2 + UP * 0.4)

        ai_tag = Text("AI zone", font=SERIF, color=SLATE, font_size=20)
        ai_tag.move_to(LEFT * 2.6 + DOWN * 0.7)

        human_tag = Text("human zone", font=SERIF, color=TEAL, font_size=20)
        human_tag.move_to(RIGHT * 2.7 + DOWN * 0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(task_bar), run_time=0.4)
        self.play(FadeIn(learn_zone), FadeIn(learn_label), run_time=0.6)
        self.play(Create(gate_line), run_time=0.4)
        self.play(FadeIn(ai_tag), FadeIn(human_tag), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


# ---------------------------------------------------------------- B14 — the check

class B14_TheCheck(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("THE CAPABILITY CHECK", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        diamond = Square(side_length=2.2)
        diamond.rotate(45 * DEGREES)
        diamond.set_fill(GROUND, 1).set_stroke(INK, 2.5)
        diamond.move_to(ORIGIN + UP * 0.1)

        q_line1 = Text("Builds the", font=SERIF, color=INK, font_size=20)
        q_line2 = Text("capability?", font=SERIF, color=INK, font_size=20)
        q_block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.1)
        q_block.move_to(diamond)

        yes_label = Text("YES", font=DISPLAY, color=TEAL,
                         font_size=22, weight="BOLD")
        yes_label.next_to(diamond, RIGHT, buff=0.5)

        keep_chip = LabelChip("KEEP IT", accent=TEAL, size=22)
        keep_chip.next_to(yes_label, RIGHT, buff=0.5)

        no_label = Text("NO", font=DISPLAY, color=SLATE,
                        font_size=22, weight="BOLD")
        no_label.next_to(diamond, DOWN, buff=0.5)

        delegate_chip = LabelChip("DELEGATE TO AI", accent=SLATE, size=22)
        delegate_chip.next_to(no_label, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(diamond), FadeIn(q_block), run_time=0.8)
        self.play(FadeIn(yes_label), FadeIn(keep_chip), run_time=0.6)
        self.play(FadeIn(no_label), FadeIn(delegate_chip), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B15 — principle card

class B15_PrincipleCard(Scene):
    def construct(self):
        total = DUR["B15"]
        t1 = Text("The gate is where the human", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("cognitive work is irreplaceable.", font=SERIF, color=TEAL,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B16 — endcard

class B16_End(Scene):
    def construct(self):
        total = DUR["B16"]

        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("Gate position determines", font=SERIF, color=INK,
                  font_size=36, weight="BOLD")
        t2 = Text("whether AI amplifies or replaces you.", font=SERIF, color=TEAL,
                  font_size=36, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.8))
