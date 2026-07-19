"""feedback-that-replaces — vox_scenes.py
Why Helpful Feedback Can Steal the Student's Own Learning
"""
from vox_graphics import *
import numpy as np


class B04_NaiveFeedbackChain(Scene):
    """THE PROBLEM — naive chain: specific feedback -> understanding -> skill."""
    def construct(self):
        labels = ["SPECIFIC\nFEEDBACK", "STUDENT\nUNDERSTANDS", "SKILL\nIMPROVES"]
        blocks = VGroup()
        arrows = []
        for lbl in labels:
            box = Rectangle(width=3.0, height=1.1)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=19, weight="MEDIUM",
                       line_spacing=1.2)
            if txt.width > 2.7:
                txt.scale_to_fit_width(2.7)
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
        chain.arrange(RIGHT, buff=0.22)
        chain.move_to(ORIGIN)

        self.play(FadeIn(blocks[0], scale=0.9), run_time=0.6)
        self.play(GrowArrow(chain[1]), FadeIn(blocks[1], scale=0.9), run_time=0.7)
        self.play(GrowArrow(chain[3]), FadeIn(blocks[2], scale=0.9), run_time=0.7)
        self.wait(8.0)


class B05_GapClosedByFeedback(Scene):
    """THE PROBLEM — directive feedback closes the gap from outside."""
    def construct(self):
        draft_box = Rectangle(width=3.0, height=1.4)
        draft_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        draft_txt = Text("STUDENT DRAFT", font=DISPLAY, color=CRIMSON,
                         font_size=20, weight="MEDIUM")
        draft_txt.move_to(draft_box)
        draft_card = VGroup(draft_box, draft_txt)
        draft_card.to_edge(LEFT, buff=1.2).move_to(draft_card.get_center() + UP * 0.0)

        standard_box = Rectangle(width=3.0, height=1.4)
        standard_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        standard_txt = Text("STANDARD", font=DISPLAY, color=TEAL,
                            font_size=20, weight="MEDIUM")
        standard_txt.move_to(standard_box)
        standard_card = VGroup(standard_box, standard_txt)
        standard_card.to_edge(RIGHT, buff=1.2)

        gap_mid_x = (draft_card.get_right()[0] + standard_card.get_left()[0]) / 2
        gap_center = np.array([gap_mid_x, 0.0, 0.0])

        # Directive feedback label
        directive_chip = LabelChip("DIRECTIVE FEEDBACK", accent=CRIMSON, size=20)
        directive_chip.move_to(gap_center + UP * 1.8)

        # Bridge (starts narrow, slides across)
        bridge = Rectangle(width=0.1, height=0.35)
        bridge.set_fill(CRIMSON, 1).set_stroke(width=0)
        bridge.move_to(gap_center)

        gap_label = SerifLabel("gap closed by feedback, not by student", accent=CRIMSON, size=22)
        gap_label.move_to(gap_center + DOWN * 1.4)

        self.play(
            FadeIn(draft_card, shift=RIGHT * 0.2),
            FadeIn(standard_card, shift=LEFT * 0.2),
            run_time=0.8,
        )
        self.play(FadeIn(directive_chip, shift=DOWN * 0.15), run_time=0.6)
        # Bridge grows to fill the gap
        gap_width = standard_card.get_left()[0] - draft_card.get_right()[0]
        self.play(
            bridge.animate.stretch_to_fit_width(max(0.1, gap_width)),
            run_time=0.8,
        )
        self.play(bridge.animate.move_to(gap_center), run_time=0.5)
        self.play(
            Write(gap_label[0]),
            Create(gap_label[1]),
            run_time=0.8,
        )
        self.wait(7.0)


class B06_MechanismCard(Scene):
    """MECHANISM section card — three feedback types."""
    def construct(self):
        chip1 = LabelChip("TYPE 1: describe", accent=SLATE, size=24)
        chip2 = LabelChip("TYPE 2: ask", accent=TEAL, size=24)
        chip3 = LabelChip("TYPE 3: rewrite", accent=CRIMSON, size=24)
        VGroup(chip1, chip2, chip3).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        self.play(FadeIn(chip1, scale=0.9), run_time=0.5)
        self.play(FadeIn(chip2, scale=0.9), run_time=0.5)
        self.play(FadeIn(chip3, scale=0.9), run_time=0.5)
        self.wait(9.0)


class B07_TypeThreeExample(Scene):
    """THE EXAMPLE — Type 3 directive rewrite."""
    def construct(self):
        card_box = Rectangle(width=11.0, height=5.0)
        card_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        card_box.move_to(ORIGIN)

        thesis_lbl = Text("STUDENT THESIS:", font=DISPLAY, color=CRIMSON,
                          font_size=20, weight="MEDIUM")
        thesis_txt = Text(
            "World War I: nationalism, militarism,\nalliance system — a listing.",
            font=SERIF, color=INK, font_size=22, line_spacing=1.3,
        )

        draft_lbl = Text("CLAUDE DRAFT A:", font=DISPLAY, color=CRIMSON,
                         font_size=20, weight="MEDIUM")
        draft_txt = Text(
            "Revise your thesis to argue nationalism\n"
            "was the primary trigger, with the\n"
            "alliance system as its amplifier.",
            font=SERIF, color=INK, font_size=22, line_spacing=1.3,
        )

        type_chip = LabelChip("TYPE 3 - directive rewrite", accent=CRIMSON, size=22)

        content = VGroup(
            VGroup(thesis_lbl, thesis_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            VGroup(draft_lbl, draft_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            type_chip,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        content.move_to(card_box).shift(LEFT * 0.5)

        self.play(FadeIn(card_box, scale=0.95), run_time=0.6)
        self.play(
            Write(content[0][0]),
            FadeIn(content[0][1], shift=DOWN * 0.1),
            run_time=0.9,
        )
        self.play(
            Write(content[1][0]),
            FadeIn(content[1][1], shift=DOWN * 0.1),
            run_time=0.9,
        )
        self.play(FadeIn(content[2], scale=0.9), run_time=0.6)
        self.wait(9.0)


class B08_TypeTwoExample(Scene):
    """THE EXAMPLE — Type 2 coaching question."""
    def construct(self):
        card_box = Rectangle(width=11.0, height=4.2)
        card_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        card_box.move_to(ORIGIN)

        draft_lbl = Text("CLAUDE DRAFT B:", font=DISPLAY, color=TEAL,
                         font_size=20, weight="MEDIUM")
        draft_txt = Text(
            "If a reader asked — what relationship\n"
            "between these causes matters most? —\n"
            "what would you want them to understand?",
            font=SERIF, color=INK, font_size=24, line_spacing=1.4,
        )

        type_chip = LabelChip("TYPE 2 - coaching question", accent=TEAL, size=22)

        content = VGroup(
            VGroup(draft_lbl, draft_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.25),
            type_chip,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(card_box).shift(LEFT * 0.5)

        self.play(FadeIn(card_box, scale=0.95), run_time=0.6)
        self.play(
            Write(content[0][0]),
            FadeIn(content[0][1], shift=DOWN * 0.1),
            run_time=1.0,
        )
        self.play(FadeIn(content[1], scale=0.9), run_time=0.6)
        self.wait(9.5)


class B09_QuoteCard(Scene):
    """THE IMPLICATION — quote card."""
    def construct(self):
        q = Text(
            "Type Three produces a better draft.\nType Two produces a better drafter.",
            font=SERIF, color=INK, font_size=30, line_spacing=1.4,
        )
        if q.width > 11.0:
            q.scale_to_fit_width(11.0)
        q.move_to(UP * 0.5)

        attr = Text(
            "— the distinction that determines who learns",
            font=SERIF, color=SLATE, font_size=22, slant=ITALIC,
        )
        attr.next_to(q, DOWN, buff=0.55, aligned_edge=LEFT)

        self.play(FadeIn(q, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(attr, shift=DOWN * 0.1), run_time=0.7)
        self.wait(8.5)


class B10_TwoConstraints(Scene):
    """THE PRACTICE — two constraints in the prompt."""
    def construct(self):
        prompt_box = Rectangle(width=10.5, height=4.5)
        prompt_box.set_fill(GROUND, 1).set_stroke(SLATE, 1.5)
        prompt_box.move_to(UP * 0.3)

        request_txt = Text(
            "Draft feedback on this student's thesis ...",
            font=SERIF, color=INK, font_size=24, slant=ITALIC,
        )
        request_txt.move_to(prompt_box.get_top() + DOWN * 0.7)

        divider = Line(
            prompt_box.get_left() + RIGHT * 0.4 + DOWN * 0.1,
            prompt_box.get_right() + LEFT * 0.4 + DOWN * 0.1,
            stroke_width=1.0, color=SLATE, stroke_opacity=0.5,
        )
        divider.next_to(request_txt, DOWN, buff=0.3)

        c1 = Text(
            "1. Draft three coaching questions, not a correction.",
            font=SERIF, color=TEAL, font_size=24,
        )
        c2 = Text(
            "2. Do not rewrite any of the student's sentences.",
            font=SERIF, color=TEAL, font_size=24,
        )
        constraints = VGroup(c1, c2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        constraints.next_to(divider, DOWN, buff=0.35, aligned_edge=LEFT)
        constraints.shift(RIGHT * 0.4)

        bracket = Brace(constraints, direction=LEFT, color=TEAL)
        bracket_lbl = Text("these two lines", font=DISPLAY, color=TEAL,
                           font_size=20, weight="MEDIUM")
        bracket_lbl.next_to(bracket, LEFT, buff=0.2)

        self.play(FadeIn(prompt_box, scale=0.96), run_time=0.5)
        self.play(Write(request_txt), run_time=0.8)
        self.play(Create(divider), run_time=0.4)
        self.play(Write(c1), run_time=0.9)
        self.play(Write(c2), run_time=0.9)
        self.play(
            Create(bracket),
            FadeIn(bracket_lbl, shift=LEFT * 0.1),
            run_time=0.8,
        )
        self.wait(7.5)


class B11_SelectTheQuestion(Scene):
    """THE PRACTICE — teacher selects from three coaching question options."""
    def construct(self):
        questions = [
            "What relationship between causes\nwould a skeptic challenge most?",
            "If a reader asked: what relationship\nmatters most — what would you say?",
            "Which cause made the others\npossible? Can you argue that?",
        ]
        chips = VGroup()
        for q in questions:
            box = Rectangle(width=9.0, height=1.1)
            box.set_fill(GROUND, 1).set_stroke(TEAL, 1.8)
            txt = Text(q, font=SERIF, color=INK, font_size=22, line_spacing=1.25)
            if txt.width > 8.4:
                txt.scale_to_fit_width(8.4)
            txt.move_to(box)
            chips.add(VGroup(box, txt))
        chips.arrange(DOWN, buff=0.35)
        chips.move_to(UP * 0.3)

        # Ring around the middle one
        ring = HandRing(chips[1], color=TEAL, wobble=0.04)

        note = SerifLabel("teacher selects; student does the thinking", accent=TEAL, size=23)
        note.next_to(chips, DOWN, buff=0.45)

        for chip in chips:
            self.play(FadeIn(chip, shift=DOWN * 0.1), run_time=0.5)
        self.play(Create(ring), run_time=1.0)
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.8,
        )
        self.wait(7.5)


class B12_GapClosedByStudent(Scene):
    """THE PRACTICE — student closes the gap with coaching support."""
    def construct(self):
        draft_box = Rectangle(width=3.0, height=1.4)
        draft_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        draft_txt = Text("STUDENT DRAFT", font=DISPLAY, color=TEAL,
                         font_size=18, weight="MEDIUM")
        draft_txt.move_to(draft_box)
        draft_card = VGroup(draft_box, draft_txt)
        draft_card.to_edge(LEFT, buff=1.2)

        standard_box = Rectangle(width=3.0, height=1.4)
        standard_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        standard_txt = Text("STANDARD", font=DISPLAY, color=TEAL,
                            font_size=18, weight="MEDIUM")
        standard_txt.move_to(standard_box)
        standard_card = VGroup(standard_box, standard_txt)
        standard_card.to_edge(RIGHT, buff=1.2)

        gap_mid_x = (draft_card.get_right()[0] + standard_card.get_left()[0]) / 2
        gap_center = np.array([gap_mid_x, 0.0, 0.0])
        gap_width = standard_card.get_left()[0] - draft_card.get_right()[0]

        # Bridge extends from the LEFT (student) side
        bridge = Rectangle(width=0.1, height=0.35)
        bridge.set_fill(TEAL, 1).set_stroke(width=0)
        bridge.move_to(draft_card.get_right() + RIGHT * 0.05)

        gap_label = SerifLabel("student closes the gap", accent=TEAL, size=24)
        gap_label.move_to(gap_center + UP * 1.6)

        note = SerifLabel("coaching question enables this", accent=SLATE, size=21)
        note.move_to(gap_center + DOWN * 1.4)

        self.play(
            FadeIn(draft_card, shift=RIGHT * 0.2),
            FadeIn(standard_card, shift=LEFT * 0.2),
            run_time=0.8,
        )
        # Bridge extends from draft side to standard
        self.play(
            bridge.animate.stretch_to_fit_width(max(0.1, gap_width)),
            run_time=0.8,
        )
        self.play(bridge.animate.move_to(gap_center), run_time=0.4)
        self.play(
            Write(gap_label[0]),
            Create(gap_label[1]),
            run_time=0.7,
        )
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.6,
        )
        self.wait(6.0)
