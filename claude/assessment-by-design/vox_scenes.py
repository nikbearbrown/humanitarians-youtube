"""assessment-by-design — vox_scenes.py
Why AI Makes Assessment Cheat-Proof or Irrelevant — There Is No Middle Ground
"""
from vox_graphics import *
import numpy as np


class B04_NaiveBanChain(Scene):
    """THE PROBLEM — naive model: ban + detection -> valid assessment."""
    def construct(self):
        labels = ["AI BAN", "DETECTION\nLAYER", "VALID\nASSESSMENT"]
        blocks = VGroup()
        arrows = []
        for lbl in labels:
            box = Rectangle(width=2.9, height=1.1)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=20, weight="MEDIUM",
                       line_spacing=1.2)
            if txt.width > 2.6:
                txt.scale_to_fit_width(2.6)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        chain_parts = []
        for i, blk in enumerate(blocks):
            chain_parts.append(blk)
            if i < len(blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
                chain_parts.append(arr)
                arrows.append(arr)
        chain = VGroup(*chain_parts)
        chain.arrange(RIGHT, buff=0.25)
        chain.move_to(ORIGIN)

        self.play(FadeIn(blocks[0], scale=0.9), run_time=0.6)
        self.play(GrowArrow(chain[1]), FadeIn(blocks[1], scale=0.9), run_time=0.7)
        self.play(GrowArrow(chain[3]), FadeIn(blocks[2], scale=0.9), run_time=0.7)
        self.wait(9.0)


class B05_DesignVsDetection(Scene):
    """THE PROBLEM — design never changed, gap opens."""
    def construct(self):
        labels = ["AI BAN", "DETECTION\nLAYER", "VALID\nASSESSMENT"]
        blocks = VGroup()
        for lbl in labels:
            box = Rectangle(width=2.9, height=1.1)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=20, weight="MEDIUM",
                       line_spacing=1.2)
            if txt.width > 2.6:
                txt.scale_to_fit_width(2.6)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        arr1 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
        arr2 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=CRIMSON, stroke_width=2.5)
        chain_parts = [blocks[0], arr1, blocks[1], arr2, blocks[2]]
        chain = VGroup(*chain_parts)
        chain.arrange(RIGHT, buff=0.25)
        chain.move_to(UP * 0.3)

        self.play(FadeIn(chain, shift=DOWN * 0.1), run_time=0.8)
        self.wait(0.8)

        # The last block slides right, gap opens
        gap_label = LabelChip("design never changed", accent=CRIMSON, size=20)
        gap_label.move_to(blocks[2].get_center() + UP * 1.6)

        note = SerifLabel("detection responds to absence of evidence", accent=CRIMSON, size=22)
        note.next_to(chain, DOWN, buff=0.9)

        self.play(
            blocks[2].animate.shift(RIGHT * 0.7),
            arr2.animate.set_color(CRIMSON),
            run_time=1.0,
        )
        self.play(FadeIn(gap_label, shift=DOWN * 0.15), run_time=0.6)
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.8,
        )
        self.wait(7.0)


class B06_MechanismCard(Scene):
    """MECHANISM section card."""
    def construct(self):
        chip = LabelChip("three design moves produce the evidence", accent=SLATE, size=26)
        chip.move_to(ORIGIN)
        self.play(FadeIn(chip, scale=0.9), run_time=0.7)
        self.wait(9.5)


class B07_ThreeMoves(Scene):
    """THE EXAMPLE — three-stage timeline."""
    def construct(self):
        # Horizontal timeline
        timeline = Line(LEFT * 5.8, RIGHT * 5.8, color=INK, stroke_width=2.5)
        timeline.move_to(ORIGIN)

        milestones = [
            (-4.5, "WEEK 1", "Annotated bibliography\n(own words)"),
            (0.0,  "WEEK 2", "Novel case introduced"),
            (4.5,  "WEEK 3", "Office-hour check-in"),
        ]

        dots = VGroup()
        labels = VGroup()
        for x, week_lbl, desc in milestones:
            dot = Dot(point=np.array([x, 0.0, 0.0]), radius=0.18, color=TEAL)
            dot.set_fill(TEAL, 1)
            week = Text(week_lbl, font=DISPLAY, color=TEAL, font_size=19, weight="MEDIUM")
            week.move_to(np.array([x, 0.55, 0.0]))
            desc_txt = Text(desc, font=SERIF, color=INK, font_size=20, line_spacing=1.25)
            if desc_txt.width > 3.0:
                desc_txt.scale_to_fit_width(3.0)
            desc_txt.move_to(np.array([x, -0.85, 0.0]))
            dots.add(dot)
            labels.add(VGroup(week, desc_txt))

        self.play(Create(timeline), run_time=0.7)
        for dot, lbl in zip(dots, labels):
            self.play(
                FadeIn(dot, scale=0.8),
                Write(lbl[0]),
                FadeIn(lbl[1], shift=DOWN * 0.1),
                run_time=0.8,
            )
        self.wait(9.5)


class B08_TransferTask(Scene):
    """THE EXAMPLE — general topic vs. novel case."""
    def construct(self):
        # Left: general topic (CRIMSON border)
        left_box = Rectangle(width=5.0, height=2.8)
        left_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        left_txt = Text(
            "General topic\nAI can be pre-primed",
            font=SERIF, color=INK, font_size=26, line_spacing=1.4,
        )
        left_txt.move_to(left_box)
        left_card = VGroup(left_box, left_txt)

        # Right: novel case (TEAL border)
        right_box = Rectangle(width=5.0, height=2.8)
        right_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        right_txt = Text(
            "Novel case,\nintroduced late",
            font=SERIF, color=INK, font_size=26, line_spacing=1.4,
        )
        right_txt.move_to(right_box)
        right_card = VGroup(right_box, right_txt)

        pair = VGroup(left_card, right_card).arrange(RIGHT, buff=1.0)
        pair.move_to(UP * 0.4)

        note = SerifLabel("transfer measures what was actually learned", accent=TEAL, size=23)
        note.next_to(pair, DOWN, buff=0.55)

        self.play(
            FadeIn(left_card, shift=RIGHT * 0.25),
            FadeIn(right_card, shift=LEFT * 0.25),
            run_time=1.0,
        )
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.8,
        )
        self.wait(8.5)


class B09_OralCheck(Scene):
    """THE EXAMPLE — oral check fork: engaged vs. substituted."""
    def construct(self):
        question_box = Rectangle(width=10.0, height=1.2)
        question_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        question_box.to_edge(UP, buff=1.2)
        q_txt = Text(
            "Tell me about your most useful source.",
            font=SERIF, color=INK, font_size=26,
        )
        q_txt.move_to(question_box)

        # Fork paths
        left_box = Rectangle(width=4.5, height=2.0)
        left_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        left_txt = Text(
            "Engaged student:\ncan explain, reasons visible",
            font=SERIF, color=INK, font_size=22, line_spacing=1.3,
        )
        left_txt.move_to(left_box)
        left_card = VGroup(left_box, left_txt)

        right_box = Rectangle(width=4.5, height=2.0)
        right_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        right_txt = Text(
            "Substituted:\ncannot explain, difficulty visible",
            font=SERIF, color=INK, font_size=22, line_spacing=1.3,
        )
        right_txt.move_to(right_box)
        right_card = VGroup(right_box, right_txt)

        fork = VGroup(left_card, right_card).arrange(RIGHT, buff=1.0)
        fork.move_to(DOWN * 0.8)

        # Arrow from question down to fork
        fork_arrow = Arrow(
            question_box.get_bottom(),
            fork.get_top() + UP * 0.1,
            buff=0.15, color=INK, stroke_width=2,
        )

        evidence_label = SerifLabel("this is evidence", accent=TEAL, size=24)
        evidence_label.next_to(fork, DOWN, buff=0.45)

        self.play(FadeIn(VGroup(question_box, q_txt), shift=DOWN * 0.1), run_time=0.7)
        self.play(GrowArrow(fork_arrow), run_time=0.6)
        self.play(
            FadeIn(left_card, shift=DOWN * 0.1),
            FadeIn(right_card, shift=DOWN * 0.1),
            run_time=0.9,
        )
        self.play(
            Write(evidence_label[0]),
            Create(evidence_label[1]),
            run_time=0.7,
        )
        self.wait(7.0)


class B10_QuoteCard(Scene):
    """THE IMPLICATION — quote card."""
    def construct(self):
        q = Text(
            "Redesign produces evidence.\nDetection responds to the absence of it.",
            font=SERIF, color=INK, font_size=30, line_spacing=1.4,
        )
        if q.width > 11.0:
            q.scale_to_fit_width(11.0)
        q.move_to(UP * 0.5)

        attr = Text(
            "— the distinction that changes the design problem",
            font=SERIF, color=SLATE, font_size=22, slant=ITALIC,
        )
        attr.next_to(q, DOWN, buff=0.55, aligned_edge=LEFT)

        self.play(FadeIn(q, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(attr, shift=DOWN * 0.1), run_time=0.7)
        self.wait(8.5)


class B11_DiagnosticQuestion(Scene):
    """THE PRACTICE — the one diagnostic question."""
    def construct(self):
        pad = Rectangle(width=10.5, height=4.0)
        pad.set_fill(WHITE, 1).set_stroke(INK, 1.5)
        pad.move_to(UP * 0.3)

        rules = VGroup(*[
            Line(
                pad.get_left() + RIGHT * 0.4 + UP * (0.9 - i * 0.7),
                pad.get_right() + LEFT * 0.4 + UP * (0.9 - i * 0.7),
                stroke_width=0.8, color=SLATE, stroke_opacity=0.35,
            )
            for i in range(5)
        ])

        q_txt = Text(
            "What can Claude produce that would pass\n"
            "this assignment without the student\n"
            "understanding the material?",
            font=SERIF, color=INK, font_size=24, line_spacing=1.3,
        )
        if q_txt.width > 9.5:
            q_txt.scale_to_fit_width(9.5)
        q_txt.move_to(pad.get_center() + UP * 0.3)

        bracket = Brace(q_txt, direction=RIGHT, color=TEAL)
        bracket_lbl = Text("the diagnostic", font=DISPLAY, color=TEAL,
                           font_size=20, weight="MEDIUM")
        bracket_lbl.next_to(bracket, RIGHT, buff=0.2)

        instruction = SerifLabel(
            "if the answer is 'most of it' — add one design move",
            accent=TEAL, size=22,
        )
        instruction.next_to(pad, DOWN, buff=0.35)

        self.play(FadeIn(pad), Create(rules), run_time=0.6)
        self.play(Write(q_txt), run_time=2.0)
        self.play(
            Create(bracket),
            FadeIn(bracket_lbl, shift=RIGHT * 0.1),
            run_time=0.7,
        )
        self.play(
            Write(instruction[0]),
            Create(instruction[1]),
            run_time=0.8,
        )
        self.wait(6.5)


class B12_RepairedChain(Scene):
    """THE PRACTICE — repaired chain: design -> evidence -> validity."""
    def construct(self):
        labels = ["OUTCOME-\nGROUNDED\nDESIGN", "MULTIPLE\nEVIDENCE\nPOINTS", "VALID\nASSESSMENT"]
        blocks = VGroup()
        for lbl in labels:
            box = Rectangle(width=3.2, height=1.4)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=17, weight="MEDIUM",
                       line_spacing=1.15)
            if txt.width > 2.9:
                txt.scale_to_fit_width(2.9)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        chain_parts = []
        for i, blk in enumerate(blocks):
            chain_parts.append(blk)
            if i < len(blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=TEAL, stroke_width=2.5)
                chain_parts.append(arr)
        chain = VGroup(*chain_parts)
        chain.arrange(RIGHT, buff=0.22)
        chain.move_to(UP * 0.4)

        note = SerifLabel("the design is the integrity", accent=TEAL, size=26)
        note.next_to(chain, DOWN, buff=0.7)

        self.play(FadeIn(blocks[0], scale=0.9), run_time=0.5)
        self.play(GrowArrow(chain[1]), FadeIn(blocks[1], scale=0.9), run_time=0.7)
        self.play(GrowArrow(chain[3]), FadeIn(blocks[2], scale=0.9), run_time=0.7)
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.8,
        )
        self.wait(7.5)
