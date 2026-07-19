"""outcome-before-topic — vox_scenes.py
Why Telling Claude the Topic Is the Wrong First Step
"""
from vox_graphics import *


class B04_NaiveTopicChain(Scene):
    """THE PROBLEM — naive chain: topic -> Claude -> lesson -> learning."""
    def construct(self):
        labels = ["TOPIC", "CLAUDE", "LESSON", "LEARNING"]
        blocks = VGroup()
        arrows = VGroup()
        for lbl in labels:
            box = Rectangle(width=2.6, height=0.95)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=22, weight="MEDIUM")
            if txt.width > 2.3:
                txt.scale_to_fit_width(2.3)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        # Build full chain with arrows
        chain_parts = []
        for i, blk in enumerate(blocks):
            chain_parts.append(blk)
            if i < len(blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
                chain_parts.append(arr)
                arrows.add(arr)
        chain = VGroup(*chain_parts)
        chain.arrange(RIGHT, buff=0.18)
        chain.move_to(ORIGIN)

        self.play(FadeIn(blocks[0], scale=0.9), run_time=0.6)
        self.play(GrowArrow(chain[1]), FadeIn(blocks[1], scale=0.9), run_time=0.7)
        self.play(GrowArrow(chain[3]), FadeIn(blocks[2], scale=0.9), run_time=0.7)
        self.play(GrowArrow(chain[5]), FadeIn(blocks[3], scale=0.9), run_time=0.7)
        self.wait(9.0)


class B05_GapRevealed(Scene):
    """THE PROBLEM — the gap between LESSON and LEARNING opens."""
    def construct(self):
        labels = ["TOPIC", "CLAUDE", "LESSON", "LEARNING"]
        colors_fill = [TEAL, TEAL, TEAL, TEAL]
        blocks = VGroup()
        for lbl, col in zip(labels, colors_fill):
            box = Rectangle(width=2.6, height=0.95)
            box.set_fill(col, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=22, weight="MEDIUM")
            if txt.width > 2.3:
                txt.scale_to_fit_width(2.3)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        arr1 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
        arr2 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
        arr3 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=CRIMSON, stroke_width=2.5)
        chain_parts = [blocks[0], arr1, blocks[1], arr2, blocks[2], arr3, blocks[3]]
        chain = VGroup(*chain_parts)
        chain.arrange(RIGHT, buff=0.18)
        chain.move_to(ORIGIN)

        # Show full chain
        self.play(FadeIn(chain, shift=DOWN * 0.1), run_time=0.8)
        self.wait(1.0)

        # Last block slides right to open the gap
        gap_label = SerifLabel("coverage does not equal learning", accent=CRIMSON, size=24)
        gap_label.move_to(blocks[3].get_center() + UP * 1.4)

        self.play(
            blocks[3].animate.shift(RIGHT * 0.8),
            arr3.animate.set_color(CRIMSON),
            run_time=0.9,
        )
        self.play(
            Write(gap_label[0]),
            Create(gap_label[1]),
            run_time=0.8,
        )
        self.wait(7.5)


class B06_MechanismCard(Scene):
    """MECHANISM section card."""
    def construct(self):
        chip = LabelChip("Claude generates what you ask for", accent=SLATE, size=26)
        chip2 = LabelChip("not what students need", accent=CRIMSON, size=26)
        VGroup(chip, chip2).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(chip, scale=0.9), run_time=0.6)
        self.play(FadeIn(chip2, scale=0.9), run_time=0.6)
        self.wait(9.0)


class B07_TwoPrompts(Scene):
    """THE EXAMPLE — two prompt cards side by side."""
    def construct(self):
        # Left: short topic prompt (CRIMSON border)
        left_box = Rectangle(width=5.2, height=2.6)
        left_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        left_txt = Text(
            "Give me a lesson\non fractions.",
            font=SERIF, color=INK, font_size=26, line_spacing=1.3,
        )
        left_txt.move_to(left_box)
        left_count = SerifLabel("6 words", accent=CRIMSON, size=22)
        left_count.next_to(left_box, DOWN, buff=0.28)
        left_card = VGroup(left_box, left_txt)

        # Right: outcome-anchored prompt (TEAL border)
        right_box = Rectangle(width=5.2, height=2.6)
        right_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        right_content = Text(
            "6th-grade, dividing fractions.\n"
            "Students believe dividing makes\n"
            "things smaller. Need: prediction\n"
            "activity + visual resolution.",
            font=SERIF, color=INK, font_size=20, line_spacing=1.3,
        )
        right_content.move_to(right_box)
        right_count = SerifLabel("38 words", accent=TEAL, size=22)
        right_count.next_to(right_box, DOWN, buff=0.28)
        right_card = VGroup(right_box, right_content)

        pair = VGroup(left_card, right_card).arrange(RIGHT, buff=0.8)
        pair.move_to(UP * 0.4)

        self.play(
            FadeIn(left_card, shift=RIGHT * 0.3),
            FadeIn(right_card, shift=LEFT * 0.3),
            run_time=1.0,
        )
        self.play(
            Write(left_count[0]),
            Create(left_count[1]),
            Write(right_count[0]),
            Create(right_count[1]),
            run_time=0.9,
        )
        self.wait(10.0)


class B08_DivergingOutputs(Scene):
    """THE EXAMPLE — activity chips under each prompt."""
    def construct(self):
        # Headers (placeholder boxes for prompt location)
        left_header = Rectangle(width=5.2, height=1.0)
        left_header.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 1.5)
        left_hdr_txt = Text("topic prompt", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC)
        left_hdr_txt.move_to(left_header)

        right_header = Rectangle(width=5.2, height=1.0)
        right_header.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        right_hdr_txt = Text("outcome-anchored prompt", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        right_hdr_txt.move_to(right_header)

        headers = VGroup(
            VGroup(left_header, left_hdr_txt),
            VGroup(right_header, right_hdr_txt),
        ).arrange(RIGHT, buff=0.8)
        headers.to_edge(UP, buff=0.9)

        # Left activities (CRIMSON chips)
        left_acts = ["Define fraction", "Write the rule", "Practice problems"]
        left_chips = VGroup(*[LabelChip(a, accent=CRIMSON, size=21) for a in left_acts])
        left_chips.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        left_chips.next_to(headers[0], DOWN, buff=0.45, aligned_edge=LEFT)

        # Right activities (TEAL chips)
        right_acts = [
            "Predict: 6 div 1/2 > or < 6?",
            "Fraction strips: resolve",
            "Explain why the answer is 12",
        ]
        right_chips = VGroup(*[LabelChip(a, accent=TEAL, size=20) for a in right_acts])
        right_chips.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        right_chips.next_to(headers[1], DOWN, buff=0.45, aligned_edge=LEFT)

        self.play(FadeIn(headers, shift=DOWN * 0.1), run_time=0.7)
        for lc, rc in zip(left_chips, right_chips):
            self.play(
                FadeIn(lc, shift=DOWN * 0.1),
                FadeIn(rc, shift=DOWN * 0.1),
                run_time=0.7,
            )
        self.wait(7.0)


class B09_QuoteCard(Scene):
    """THE IMPLICATION — quote card."""
    def construct(self):
        q = Text(
            "He knew it all.\nHe just hadn't written it down first.",
            font=SERIF, color=INK, font_size=36, line_spacing=1.4,
        )
        if q.width > 11.5:
            q.scale_to_fit_width(11.5)
        q.move_to(UP * 0.5)

        attr = Text(
            "— the only thing the second prompt adds",
            font=SERIF, color=SLATE, font_size=22, slant=ITALIC,
        )
        attr.next_to(q, DOWN, buff=0.55, aligned_edge=LEFT)

        self.play(FadeIn(q, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(attr, shift=DOWN * 0.1), run_time=0.7)
        self.wait(9.5)


class B10_AlignmentFixed(Scene):
    """THE MECHANISM repaired — aligned chain."""
    def construct(self):
        labels = ["NAMED\nOUTCOME", "ANCHORED\nPROMPT", "ALIGNED\nLESSON", "STUDENT\nTRANSFER"]
        blocks = VGroup()
        for lbl in labels:
            box = Rectangle(width=2.6, height=1.1)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=18, weight="MEDIUM",
                       line_spacing=1.2)
            if txt.width > 2.3:
                txt.scale_to_fit_width(2.3)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        arrows = []
        chain_parts = []
        for i, blk in enumerate(blocks):
            chain_parts.append(blk)
            if i < len(blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=TEAL, stroke_width=2.5)
                chain_parts.append(arr)
                arrows.append(arr)
        chain = VGroup(*chain_parts)
        chain.arrange(RIGHT, buff=0.18)
        chain.move_to(UP * 0.3)

        note = SerifLabel("alignment is what the prompt enables", accent=TEAL, size=24)
        note.next_to(chain, DOWN, buff=0.65)

        self.play(FadeIn(blocks[0], scale=0.9), run_time=0.5)
        for i in range(3):
            self.play(
                GrowArrow(chain_parts[i * 2 + 1]),
                FadeIn(blocks[i + 1], scale=0.9),
                run_time=0.7,
            )
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.8,
        )
        self.wait(7.5)


class B11_WrittenOutcome(Scene):
    """THE PRACTICE — the one-sentence outcome written on a notepad."""
    def construct(self):
        # Notepad card
        pad = Rectangle(width=9.0, height=3.5)
        pad.set_fill(WHITE, 1).set_stroke(INK, 1.5)
        pad.move_to(UP * 0.4)

        # Rule lines
        rules = VGroup(*[
            Line(
                pad.get_left() + RIGHT * 0.35 + UP * (0.8 - i * 0.7),
                pad.get_right() + LEFT * 0.35 + UP * (0.8 - i * 0.7),
                stroke_width=0.8, color=SLATE, stroke_opacity=0.4,
            )
            for i in range(4)
        ])

        outcome_txt = Text(
            "Students will explain why 6 / (1/2) = 12.",
            font=SERIF, color=INK, font_size=30,
        )
        if outcome_txt.width > 8.0:
            outcome_txt.scale_to_fit_width(8.0)
        outcome_txt.move_to(pad.get_center() + UP * 0.3)

        bracket = Line(
            outcome_txt.get_left() + LEFT * 0.3 + DOWN * 0.1,
            outcome_txt.get_left() + LEFT * 0.3 + UP * 0.1,
            color=TEAL, stroke_width=3,
        )
        bracket_top = Line(
            outcome_txt.get_left() + LEFT * 0.3 + UP * 0.1,
            outcome_txt.get_left() + LEFT * 0.15 + UP * 0.1,
            color=TEAL, stroke_width=3,
        )
        bracket_bot = Line(
            outcome_txt.get_left() + LEFT * 0.3 + DOWN * 0.1,
            outcome_txt.get_left() + LEFT * 0.15 + DOWN * 0.1,
            color=TEAL, stroke_width=3,
        )

        lbl = Text("outcome", font=DISPLAY, color=TEAL, font_size=20, weight="MEDIUM")
        lbl.next_to(bracket, LEFT, buff=0.15)

        instruction = SerifLabel("write this before you open Claude", accent=TEAL, size=24)
        instruction.next_to(pad, DOWN, buff=0.4)

        self.play(FadeIn(pad), Create(rules), run_time=0.7)
        self.play(Write(outcome_txt), run_time=1.8)
        self.play(
            Create(VGroup(bracket, bracket_top, bracket_bot)),
            FadeIn(lbl, shift=LEFT * 0.1),
            run_time=0.7,
        )
        self.play(
            Write(instruction[0]),
            Create(instruction[1]),
            run_time=0.8,
        )
        self.wait(8.0)


class B12_TwoPathCards(Scene):
    """THE PRACTICE — two paths: topic-first vs. outcome-first."""
    def construct(self):
        def make_path(labels, color):
            parts = []
            for i, lbl in enumerate(labels):
                box = Rectangle(width=2.6, height=0.85)
                box.set_fill(color, 1).set_stroke(width=0)
                txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=18, weight="MEDIUM")
                if txt.width > 2.3:
                    txt.scale_to_fit_width(2.3)
                txt.move_to(box)
                parts.append(VGroup(box, txt))
                if i < len(labels) - 1:
                    arr = Arrow(ORIGIN, RIGHT * 0.45, buff=0, color=color, stroke_width=2)
                    parts.append(arr)
            row = VGroup(*parts)
            row.arrange(RIGHT, buff=0.14)
            return row

        top_path = make_path(["TOPIC", "PROMPT", "COVERAGE"], CRIMSON)
        bot_path = make_path(["OUTCOME", "PROMPT", "TRANSFER"], TEAL)

        top_path.move_to(UP * 0.8)
        bot_path.move_to(DOWN * 0.8)

        top_lbl = SerifLabel("without the outcome", accent=CRIMSON, size=22)
        top_lbl.next_to(top_path, LEFT, buff=0.4)
        bot_lbl = SerifLabel("with the outcome", accent=TEAL, size=22)
        bot_lbl.next_to(bot_path, LEFT, buff=0.4)

        self.play(FadeIn(top_path, shift=DOWN * 0.1), run_time=0.8)
        self.play(
            Write(top_lbl[0]),
            Create(top_lbl[1]),
            run_time=0.6,
        )
        self.play(FadeIn(bot_path, shift=DOWN * 0.1), run_time=0.8)
        self.play(
            Write(bot_lbl[0]),
            Create(bot_lbl[1]),
            run_time=0.6,
        )
        self.wait(7.5)
