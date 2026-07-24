"""artifact-vs-learning — vox_scenes.py
Why a Polished Lesson Plan Can Fail Every Student in the Room

One Scene per GRAPHIC/CARD beat with source=own.
STILL ai beats (B02) have no scene — they compile as slates.
"""
from vox_graphics import *


class B03_PlanVsOutcome(Scene):
    """COLD OPEN — polished plan beside the blank exit ticket."""
    def construct(self):
        # Left: lesson plan card (TEAL border)
        plan_box = Rectangle(width=4.8, height=3.2)
        plan_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        plan_lines = VGroup(
            Text("Warm-up activity", font=SERIF, color=INK, font_size=22),
            Text("Vocabulary list", font=SERIF, color=INK, font_size=22),
            Text("Three learning tasks", font=SERIF, color=INK, font_size=22),
            Text("Exit ticket", font=SERIF, color=INK, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        plan_lines.move_to(plan_box)
        plan_card = VGroup(plan_box, plan_lines)

        # Right: exit ticket (blank, CRIMSON border)
        ticket_box = Rectangle(width=4.8, height=3.2)
        ticket_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        ticket_q = Text("What would a cell do", font=SERIF, color=INK, font_size=20)
        ticket_q2 = Text("without ATP?", font=SERIF, color=INK, font_size=20)
        ticket_blank = Rectangle(width=3.8, height=1.1)
        ticket_blank.set_fill(GROUND, 1).set_stroke(INK, 1)
        ticket_content = VGroup(ticket_q, ticket_q2, ticket_blank).arrange(DOWN, buff=0.22)
        ticket_content.move_to(ticket_box)
        ticket_card = VGroup(ticket_box, ticket_content)

        pair = VGroup(plan_card, ticket_card).arrange(RIGHT, buff=1.0)
        pair.move_to(UP * 0.3)

        plan_label = SerifLabel("coherent artifact", accent=TEAL, size=24)
        plan_label.next_to(plan_card, DOWN, buff=0.3)
        ticket_label = SerifLabel("no learning", accent=CRIMSON, size=24)
        ticket_label.next_to(ticket_card, DOWN, buff=0.3)

        self.play(
            FadeIn(plan_card, shift=RIGHT * 0.3),
            FadeIn(ticket_card, shift=LEFT * 0.3),
            run_time=1.2,
        )
        self.play(
            Write(plan_label[0]),
            Create(plan_label[1]),
            Write(ticket_label[0]),
            Create(ticket_label[1]),
            run_time=1.0,
        )
        self.wait(7.0)


class B04_TheQuestion(Scene):
    """THE QUESTION beat — on screen and in narration."""
    def construct(self):
        q = Text(
            "A polished plan should predict understanding.",
            font=SERIF, color=INK, font_size=32,
        )
        q2 = Text(
            "Here it didn't. Why?",
            font=SERIF, color=INK, font_size=32,
        )
        block = VGroup(q, q2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        if block.width > 11.0:
            block.scale_to_fit_width(11.0)
        block.move_to(ORIGIN)
        self.play(FadeIn(q, shift=DOWN * 0.15), run_time=0.9)
        self.play(FadeIn(q2, shift=DOWN * 0.15), run_time=0.7)
        self.wait(7.5)


class B05_NaiveChain(Scene):
    """THE PROBLEM — naive chain: better plan -> student learning."""
    def construct(self):
        labels = ["BETTER PLAN", "FAITHFUL USE", "STUDENT LEARNING"]
        blocks = VGroup()
        for lbl in labels:
            box = Rectangle(width=3.2, height=1.1)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=22, weight="MEDIUM")
            if txt.width > 2.9:
                txt.scale_to_fit_width(2.9)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        arrows = VGroup()
        chain = VGroup()
        for i, blk in enumerate(blocks):
            chain.add(blk)
            if i < len(blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.6, buff=0, color=INK, stroke_width=2.5)
                chain.add(arr)
                arrows.add(arr)
        chain.arrange(RIGHT, buff=0.25)
        chain.move_to(ORIGIN)

        # Reveal each block-arrow pair in sequence
        self.play(FadeIn(blocks[0], scale=0.92), run_time=0.7)
        self.play(
            GrowArrow(chain[1]),
            FadeIn(blocks[1], scale=0.92),
            run_time=0.8,
        )
        self.play(
            GrowArrow(chain[3]),
            FadeIn(blocks[2], scale=0.92),
            run_time=0.8,
        )
        self.wait(9.0)


class B06_WhatClaudeMisses(Scene):
    """THE PROBLEM — what Claude cannot access."""
    def construct(self):
        # Residual 'BETTER PLAN' block at top
        plan_box = Rectangle(width=3.2, height=1.1)
        plan_box.set_fill(TEAL, 1).set_stroke(width=0)
        plan_txt = Text("BETTER PLAN", font=DISPLAY, color=WHITE, font_size=22, weight="MEDIUM")
        plan_txt.move_to(plan_box)
        plan_block = VGroup(plan_box, plan_txt)
        plan_block.to_edge(UP, buff=1.2).to_edge(LEFT, buff=1.5)

        missing_items = [
            "prior knowledge",
            "specific misconceptions",
            "evidence of understanding",
        ]
        chips = VGroup()
        for item in missing_items:
            chip = LabelChip(item, accent=CRIMSON, size=24)
            chips.add(chip)
        chips.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        chips.next_to(plan_block, DOWN, buff=0.6, aligned_edge=LEFT)

        note_label = SerifLabel("Claude cannot access this", accent=CRIMSON, size=26)
        note_label.next_to(chips, DOWN, buff=0.5, aligned_edge=LEFT)

        # Strike lines over chips
        strikes = VGroup()
        for chip in chips:
            strike = Line(
                chip.get_left() + LEFT * 0.05,
                chip.get_right() + RIGHT * 0.05,
                color=CRIMSON, stroke_width=2.0,
            )
            strikes.add(strike)

        self.play(FadeIn(plan_block, shift=DOWN * 0.2), run_time=0.6)
        for i, (chip, strike) in enumerate(zip(chips, strikes)):
            self.play(FadeIn(chip, scale=0.9), run_time=0.5)
            self.play(Create(strike), run_time=0.4)
        self.play(
            Write(note_label[0]),
            Create(note_label[1]),
            run_time=0.9,
        )
        self.wait(5.5)


class B07_MechanismCard(Scene):
    """MECHANISM section card."""
    def construct(self):
        chip = LabelChip("Claude optimizes for artifact quality", accent=SLATE, size=28)
        chip.move_to(ORIGIN)
        self.play(FadeIn(chip, scale=0.9), run_time=0.8)
        self.wait(9.5)


class B08_ParkPlan(Scene):
    """THE EXAMPLE — Ms. Park's lesson plan, all three activities ticked."""
    def construct(self):
        eyebrow = Text("Ms. Park | Water Cycle", font=DISPLAY, color=SLATE,
                       font_size=24, weight="MEDIUM")
        eyebrow.to_edge(UP, buff=0.8)

        activities = [
            "Diagram activity",
            "Vocabulary matching",
            "Fill-in-the-blank check",
        ]
        rows = VGroup()
        ticks = VGroup()
        dots = VGroup()
        for act in activities:
            row_box = Rectangle(width=7.5, height=0.8)
            row_box.set_fill(GROUND, 1).set_stroke(TEAL, 1.5)
            act_txt = Text(act, font=SERIF, color=INK, font_size=26)
            act_txt.move_to(row_box.get_left() + RIGHT * 0.4, aligned_edge=LEFT)

            tick = Text("v", font=SERIF, color=TEAL, font_size=28, weight="BOLD")
            tick.move_to(row_box.get_right() + LEFT * 0.35)

            dot = Dot(radius=0.13, color=INK)
            dot.next_to(row_box, LEFT, buff=0.3)

            rows.add(VGroup(row_box, act_txt))
            ticks.add(tick)
            dots.add(dot)

        plan_stack = VGroup(rows[0], rows[1], rows[2]).arrange(DOWN, buff=0.25)
        plan_stack.move_to(DOWN * 0.2)

        # Re-position dots and ticks to actual row positions
        for i in range(3):
            dots[i].next_to(rows[i], LEFT, buff=0.3)
            ticks[i].move_to(rows[i].get_right() + LEFT * 0.35)

        self.play(Write(eyebrow), run_time=0.7)
        self.play(FadeIn(rows[0], shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(rows[1], shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(rows[2], shift=DOWN * 0.1), run_time=0.5)
        # Student dots and ticks appear in sequence
        for i in range(3):
            self.play(FadeIn(dots[i], scale=0.8), run_time=0.4)
            self.play(FadeIn(ticks[i], scale=1.2), run_time=0.4)
        self.wait(6.5)


class B09_ExitBlank(Scene):
    """THE EXAMPLE — 22 of 28 student squares blank on exit ticket."""
    def construct(self):
        # IsotypeGrid: 22 CRIMSON (blank), 6 TEAL (answered)
        grid = IsotypeGrid(
            counts=[6, 22],
            colors=[TEAL, CRIMSON],
            per_row=7,
            size=0.38,
            gap=0.14,
        )
        grid.move_to(UP * 0.3)

        label_answered = SerifLabel("6 answered", accent=TEAL, size=24)
        label_blank = SerifLabel("22 blank", accent=CRIMSON, size=24)
        label_answered.next_to(grid, DOWN, buff=0.4).shift(LEFT * 2.5)
        label_blank.next_to(grid, DOWN, buff=0.4).shift(RIGHT * 2.0)

        note = SerifLabel("outcome never named in the plan", accent=INK, size=22)
        note.next_to(label_blank, DOWN, buff=0.45).shift(LEFT * 2.0)

        self.play(grid.count_up(3.5, lag_ratio=0.008))
        self.play(
            Write(label_answered[0]),
            Create(label_answered[1]),
            Write(label_blank[0]),
            Create(label_blank[1]),
            run_time=0.9,
        )
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.8,
        )
        self.wait(6.0)


class B10_QuoteCard(Scene):
    """THE IMPLICATION — quote card."""
    def construct(self):
        quote_text = (
            "A lesson plan is a proposal\n"
            "for conditions under which\n"
            "learning might happen.\n"
            "It is not learning itself."
        )
        q = Text(quote_text, font=SERIF, color=INK, font_size=32, line_spacing=1.4)
        if q.width > 11.0:
            q.scale_to_fit_width(11.0)
        q.move_to(UP * 0.4)

        attr = Text(
            "— the artifact vs. learning distinction",
            font=SERIF, color=SLATE, font_size=22, slant=ITALIC,
        )
        attr.next_to(q, DOWN, buff=0.55, aligned_edge=LEFT)

        self.play(FadeIn(q, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(attr, shift=DOWN * 0.1), run_time=0.7)
        self.wait(8.5)


class B11_OutcomeFirst(Scene):
    """THE PRACTICE — vague vs. observable outcome."""
    def construct(self):
        # Left: vague (CRIMSON)
        vague_box = Rectangle(width=5.0, height=2.2)
        vague_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        vague_txt = Text(
            "Understand\nthe water cycle",
            font=SERIF, color=INK, font_size=28, line_spacing=1.3,
        )
        vague_txt.move_to(vague_box)
        vague_card = VGroup(vague_box, vague_txt)

        # Right: specific (TEAL)
        specific_box = Rectangle(width=5.0, height=2.2)
        specific_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        specific_txt = Text(
            "Explain why rain falls\nas liquid, not vapor",
            font=SERIF, color=INK, font_size=26, line_spacing=1.3,
        )
        specific_txt.move_to(specific_box)
        specific_card = VGroup(specific_box, specific_txt)

        pair = VGroup(vague_card, specific_card).arrange(RIGHT, buff=1.2)
        pair.move_to(UP * 0.3)

        vague_label = SerifLabel("topical", accent=CRIMSON, size=23)
        vague_label.next_to(vague_card, DOWN, buff=0.3)
        specific_label = SerifLabel("name this first", accent=TEAL, size=23)
        specific_label.next_to(specific_card, DOWN, buff=0.3)

        self.play(
            FadeIn(vague_card, shift=RIGHT * 0.25),
            FadeIn(specific_card, shift=LEFT * 0.25),
            run_time=1.0,
        )
        self.play(
            Write(vague_label[0]),
            Create(vague_label[1]),
            run_time=0.7,
        )
        self.play(
            Write(specific_label[0]),
            Create(specific_label[1]),
            run_time=0.7,
        )
        self.wait(9.5)


class B12_NaiveFixed(Scene):
    """THE PRACTICE — repaired chain with named outcome first."""
    def construct(self):
        labels = ["NAMED OUTCOME", "ALIGNED PLAN", "STUDENT TRANSFER"]
        blocks = VGroup()
        for lbl in labels:
            box = Rectangle(width=3.0, height=1.0)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=20, weight="MEDIUM")
            if txt.width > 2.7:
                txt.scale_to_fit_width(2.7)
            txt.move_to(box)
            blocks.add(VGroup(box, txt))

        # Old (broken) chain: middle two blocks first, without NAMED OUTCOME
        old_chain_labels = ["BETTER PLAN", "FAITHFUL USE", "STUDENT LEARNING"]
        old_blocks = VGroup()
        for lbl in old_chain_labels:
            box = Rectangle(width=3.0, height=1.0)
            box.set_fill(SLATE, 0.6).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=18, weight="MEDIUM")
            if txt.width > 2.7:
                txt.scale_to_fit_width(2.7)
            txt.move_to(box)
            old_blocks.add(VGroup(box, txt))

        old_arr1 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2)
        old_arr2 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2)
        old_chain_items = VGroup(
            old_blocks[0], old_arr1, old_blocks[1], old_arr2, old_blocks[2]
        )
        old_chain_items.arrange(RIGHT, buff=0.2)
        old_chain_items.move_to(UP * 0.5)

        # Show old chain briefly, then transform
        self.play(FadeIn(old_chain_items, shift=DOWN * 0.15), run_time=0.8)
        self.wait(1.2)

        # New chain positions
        arr1 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
        arr2 = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)
        new_chain = VGroup(blocks[0], arr1, blocks[1], arr2, blocks[2])
        new_chain.arrange(RIGHT, buff=0.2)
        new_chain.move_to(UP * 0.5)

        self.play(
            FadeOut(old_chain_items, shift=UP * 0.2),
            FadeIn(new_chain, shift=DOWN * 0.2),
            run_time=1.2,
        )
        self.wait(9.0)
