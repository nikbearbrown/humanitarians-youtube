"""rubric-adjective-trap — vox_scenes.py
Why "Good" in a Rubric Teaches Students Nothing About Quality
"""
from vox_graphics import *
import numpy as np


class B04_AdjectiveChain(Scene):
    """THE PROBLEM — quality adjective defines quality with itself (circular)."""
    def construct(self):
        # Rubric cell: EXCELLENT -> CRIMSON box with 'Demonstrates sophisticated analysis'
        level_box = Rectangle(width=3.0, height=1.0)
        level_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.5)
        level_lbl = Text("EXCELLENT", font=DISPLAY, color=INK, font_size=18, weight="BOLD")
        level_lbl.move_to(level_box)
        level_card = VGroup(level_box, level_lbl)

        arrow_lr = Arrow(ORIGIN, RIGHT * 0.5, buff=0, color=INK, stroke_width=2.5)

        criteria_box = Rectangle(width=5.5, height=1.0)
        criteria_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2.0)
        criteria_txt = Text(
            "Demonstrates sophisticated analysis",
            font=SERIF, color=INK, font_size=20,
        )
        if criteria_txt.width > 5.2:
            criteria_txt.scale_to_fit_width(5.2)
        criteria_txt.move_to(criteria_box)
        criteria_card = VGroup(criteria_box, criteria_txt)

        row = VGroup(level_card, arrow_lr, criteria_card)
        row.arrange(RIGHT, buff=0.3)
        row.move_to(UP * 0.9)

        # Highlight 'sophisticated' word in CRIMSON
        highlight = SurroundingRectangle(criteria_txt, color=CRIMSON, buff=0.05, stroke_width=1.5)

        # Circular arrow: from 'sophisticated' back to 'EXCELLENT'
        circ_label = Text(
            "defines quality\nwith quality",
            font=SERIF, color=CRIMSON, font_size=19, line_spacing=1.2, slant=ITALIC,
        )
        circ_label.move_to(DOWN * 0.5)

        circ_arrow = CurvedArrow(
            criteria_box.get_left() + LEFT * 0.05,
            level_box.get_bottom() + DOWN * 0.05,
            angle=-PI / 2.5,
            color=CRIMSON,
            stroke_width=2,
        )

        # TEAL 'fix' hint at bottom
        fix_note = SerifLabel("observable alternative: what you'd see in the work", accent=TEAL, size=20)
        fix_note.move_to(DOWN * 2.2)

        self.play(FadeIn(level_card), GrowArrow(arrow_lr), FadeIn(criteria_card), run_time=0.8)
        self.play(Create(highlight), run_time=0.5)
        self.play(Create(circ_arrow), run_time=0.7)
        self.play(FadeIn(circ_label, shift=UP * 0.1), run_time=0.6)
        self.play(
            Write(fix_note[0]),
            Create(fix_note[1]),
            run_time=0.7,
        )
        self.wait(13.7)


class B05_ObservableVsAdjective(Scene):
    """THE MECHANISM — adjective chain vs. observable criteria side-by-side."""
    def construct(self):
        # Left: ADJECTIVE CHAIN
        left_box = Rectangle(width=5.0, height=4.0)
        left_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        left_header = Text("ADJECTIVE CHAIN", font=DISPLAY, color=CRIMSON, font_size=18, weight="BOLD")
        left_header.move_to(left_box.get_top() + DOWN * 0.45)

        adjectives = VGroup(
            Text("sophisticated", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
            Text("strong", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
            Text("excellent", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
            Text("good", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
        )
        adjectives.arrange(DOWN, buff=0.3)
        adjectives.move_to(left_box.get_center() + DOWN * 0.1)
        left_card = VGroup(left_box, left_header, adjectives)

        # Right: OBSERVABLE CRITERIA
        right_box = Rectangle(width=5.0, height=4.0)
        right_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        right_header = Text("OBSERVABLE CRITERIA", font=DISPLAY, color=TEAL, font_size=18, weight="BOLD")
        right_header.move_to(right_box.get_top() + DOWN * 0.45)

        obs_txt = Text(
            "Each paragraph connects\nevidence to its claim.\n\nThe explanation interprets —\nit does not restate.",
            font=SERIF, color=INK, font_size=19, line_spacing=1.3,
        )
        if obs_txt.width > 4.5:
            obs_txt.scale_to_fit_width(4.5)
        obs_txt.move_to(right_box.get_center() + DOWN * 0.1)
        right_card = VGroup(right_box, right_header, obs_txt)

        pair = VGroup(left_card, right_card).arrange(RIGHT, buff=0.9)
        pair.move_to(UP * 0.3)

        note = SerifLabel("student can self-assess before submitting", accent=TEAL, size=21)
        note.next_to(pair, DOWN, buff=0.4)

        self.play(
            FadeIn(left_card, shift=RIGHT * 0.25),
            FadeIn(right_card, shift=LEFT * 0.25),
            run_time=1.0,
        )
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.7,
        )
        self.wait(14.8)


class B06_RubricTransform(Scene):
    """THE EXAMPLE — morph: old vague cell rewrites into observable description."""
    def construct(self):
        # Background frame
        pad = Rectangle(width=11.0, height=4.2)
        pad.set_fill(WHITE, 1).set_stroke(INK, 1.5)
        pad.move_to(UP * 0.2)

        # Criteria column label
        criterion_lbl = Text("ANALYSIS", font=DISPLAY, color=INK, font_size=18, weight="BOLD")
        criterion_lbl.move_to(pad.get_left() + RIGHT * 1.0 + UP * 1.3)

        sep_line = Line(
            pad.get_top() + RIGHT * (-5.5 + 2.3),
            pad.get_bottom() + RIGHT * (-5.5 + 2.3),
            color=SLATE, stroke_width=0.8, stroke_opacity=0.4,
        )

        # Level label
        level_lbl = Text("EXEMPLARY", font=DISPLAY, color=INK, font_size=18, weight="BOLD")
        level_lbl.move_to(pad.get_center() + UP * 1.3 + RIGHT * 0.6)

        # Old (CRIMSON) text — appears first
        old_txt = Text(
            "Demonstrates sophisticated\nanalysis of the topic.",
            font=SERIF, color=CRIMSON, font_size=22, line_spacing=1.3,
        )
        if old_txt.width > 6.5:
            old_txt.scale_to_fit_width(6.5)
        old_txt.move_to(pad.get_center() + DOWN * 0.3 + RIGHT * 0.6)

        old_label = Text("BEFORE — quality word", font=DISPLAY, color=CRIMSON,
                         font_size=15, weight="MEDIUM")
        old_label.next_to(old_txt, UP, buff=0.18)

        # New (TEAL) text — replaces old
        new_txt = Text(
            "Each body paragraph connects\nevidence to the paragraph's claim.\nThe explanation interprets —\nit does not restate.",
            font=SERIF, color=TEAL, font_size=19, line_spacing=1.25,
        )
        if new_txt.width > 6.5:
            new_txt.scale_to_fit_width(6.5)
        new_txt.move_to(pad.get_center() + DOWN * 0.15 + RIGHT * 0.6)

        new_label = Text("AFTER — observable", font=DISPLAY, color=TEAL,
                         font_size=15, weight="MEDIUM")
        new_label.next_to(new_txt, UP, buff=0.18)

        note = SerifLabel("Claude drafts · teacher decides", accent=TEAL, size=20)
        note.next_to(pad, DOWN, buff=0.35)

        self.play(FadeIn(pad), Create(sep_line), run_time=0.5)
        self.play(Write(criterion_lbl), Write(level_lbl), run_time=0.6)
        self.play(FadeIn(old_label), Write(old_txt), run_time=1.0)
        self.wait(1.0)
        self.play(
            FadeOut(old_txt, shift=UP * 0.15),
            FadeOut(old_label, shift=UP * 0.15),
            run_time=0.6,
        )
        self.play(FadeIn(new_label, shift=DOWN * 0.1), Write(new_txt), run_time=1.5)
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.7,
        )
        self.wait(16.7)


class B08_AuditPrompt(Scene):
    """THE PRACTICE — one diagnostic prompt on notepad card."""
    def construct(self):
        pad = Rectangle(width=10.5, height=3.8)
        pad.set_fill(WHITE, 1).set_stroke(INK, 1.5)
        pad.move_to(UP * 0.4)

        rules = VGroup(*[
            Line(
                pad.get_left() + RIGHT * 0.4 + UP * (0.8 - i * 0.7),
                pad.get_right() + LEFT * 0.4 + UP * (0.8 - i * 0.7),
                stroke_width=0.8, color=SLATE, stroke_opacity=0.35,
            )
            for i in range(5)
        ])

        q_txt = Text(
            "Identify any performance level descriptions\n"
            "that use quality words rather than\n"
            "observable behaviors — and list what you'd\n"
            "need to know to write an observable alternative.",
            font=SERIF, color=INK, font_size=21, line_spacing=1.3,
        )
        if q_txt.width > 9.5:
            q_txt.scale_to_fit_width(9.5)
        q_txt.move_to(pad.get_center() + UP * 0.2)

        bracket = Brace(q_txt, direction=RIGHT, color=TEAL)
        bracket_lbl = Text("the audit", font=DISPLAY, color=TEAL,
                           font_size=18, weight="MEDIUM")
        bracket_lbl.next_to(bracket, RIGHT, buff=0.2)

        instruction = SerifLabel(
            "if it flags your whole rubric — you have the right rubric problem",
            accent=TEAL, size=20,
        )
        instruction.next_to(pad, DOWN, buff=0.3)

        self.play(FadeIn(pad), Create(rules), run_time=0.5)
        self.play(Write(q_txt), run_time=2.0)
        self.play(
            Create(bracket),
            FadeIn(bracket_lbl, shift=RIGHT * 0.1),
            run_time=0.6,
        )
        self.play(
            Write(instruction[0]),
            Create(instruction[1]),
            run_time=0.7,
        )
        self.wait(11.7)


class B09_TwoGates(Scene):
    """THE PRACTICE — two TEAL gate cards: observable + human."""
    def construct(self):
        # Card 1: OBSERVABLE
        box1 = Rectangle(width=10.0, height=1.6)
        box1.set_fill(TEAL, 0.12).set_stroke(TEAL, 2.0)
        txt1_header = Text("OBSERVABLE", font=DISPLAY, color=TEAL, font_size=18, weight="BOLD")
        txt1_body = Text(
            "reviewer + reader can agree on whether the criterion is met\n— without extra interpretation from the teacher",
            font=SERIF, color=INK, font_size=20, line_spacing=1.3,
        )
        if txt1_body.width > 9.3:
            txt1_body.scale_to_fit_width(9.3)
        card1_content = VGroup(txt1_header, txt1_body)
        card1_content.arrange(DOWN, buff=0.12)
        card1_content.move_to(box1)
        card1 = VGroup(box1, card1_content)

        # Card 2: HUMAN GATE
        box2 = Rectangle(width=10.0, height=1.6)
        box2.set_fill(TEAL, 0.22).set_stroke(TEAL, 2.0)
        txt2_header = Text("HUMAN GATE", font=DISPLAY, color=TEAL, font_size=18, weight="BOLD")
        txt2_body = Text(
            "Claude drafts the observable criteria — teacher decides what quality means",
            font=SERIF, color=INK, font_size=20, line_spacing=1.3,
        )
        if txt2_body.width > 9.3:
            txt2_body.scale_to_fit_width(9.3)
        card2_content = VGroup(txt2_header, txt2_body)
        card2_content.arrange(DOWN, buff=0.12)
        card2_content.move_to(box2)
        card2 = VGroup(box2, card2_content)

        stack = VGroup(card1, card2)
        stack.arrange(DOWN, buff=0.5)
        stack.move_to(ORIGIN)

        self.play(FadeIn(card1, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(card2, shift=DOWN * 0.15), run_time=0.7)
        self.wait(14.6)
