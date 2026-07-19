"""data-minimization-prompt — vox_scenes.py
Why Pasting a Student's Name into Claude Is a Privacy Decision, Not a Prompt
"""
from vox_graphics import *
import numpy as np


class B03_TwoPrompts(Scene):
    """THE PROBLEM — unsafe vs. minimized prompt windows side by side."""
    def construct(self):
        # Left: Version A (CRIMSON — identifiable)
        left_box = Rectangle(width=5.5, height=4.5)
        left_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        left_header = Text("VERSION A", font=DISPLAY, color=CRIMSON, font_size=16, weight="BOLD")
        left_header.move_to(left_box.get_top() + DOWN * 0.4)

        left_lines = VGroup(
            Text("Student: Maria Chen", font=MONO, color=CRIMSON, font_size=16),
            Text("Grade: 78% (below target)", font=MONO, color=CRIMSON, font_size=16),
            Text("IEP label: dyslexia", font=MONO, color=CRIMSON, font_size=16),
            Text("Counselor note: anxiety,\nstress at home", font=MONO, color=CRIMSON,
                 font_size=16, line_spacing=1.2),
        )
        left_lines.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        left_lines.move_to(left_box.get_center() + DOWN * 0.2)
        left_card = VGroup(left_box, left_header, left_lines)

        # Right: Version B (TEAL — minimized)
        right_box = Rectangle(width=5.5, height=4.5)
        right_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        right_header = Text("VERSION B", font=DISPLAY, color=TEAL, font_size=16, weight="BOLD")
        right_header.move_to(right_box.get_top() + DOWN * 0.4)

        right_lines = VGroup(
            Text("Student: [Student A]", font=MONO, color=TEAL, font_size=16),
            Text("Performance: [below target]", font=MONO, color=TEAL, font_size=16),
            Text("[documented accommodation]", font=MONO, color=TEAL, font_size=16),
            Text("Struggling with complex texts\nand time management", font=SERIF,
                 color=INK, font_size=16, line_spacing=1.2),
        )
        right_lines.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        right_lines.move_to(right_box.get_center() + DOWN * 0.2)
        right_card = VGroup(right_box, right_header, right_lines)

        pair = VGroup(left_card, right_card).arrange(RIGHT, buff=0.7)
        pair.move_to(UP * 0.3)

        note = SerifLabel("same useful output · no regulated data transmitted", accent=TEAL, size=20)
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
        self.wait(22.3)


class B05_RedactionCheck(Scene):
    """THE PRACTICE — prompt window with live identifier replacement."""
    def construct(self):
        # Prompt window frame
        window = Rectangle(width=10.5, height=4.2)
        window.set_fill(WHITE, 1).set_stroke(SLATE, 1.5)
        window.move_to(UP * 0.5)

        # Title bar
        title_bar = Rectangle(width=10.5, height=0.55)
        title_bar.set_fill(SLATE, 0.18).set_stroke(width=0)
        title_bar.move_to(window.get_top() + DOWN * 0.275)
        title_txt = Text("Claude · New conversation", font=MONO, color=INK, font_size=14)
        title_txt.move_to(title_bar)

        # Prompt lines — each with a CRIMSON identifier that gets replaced
        line_data = [
            ("Help with support plans for  ", "Maria Chen", "[Student A]"),
            ("Accommodation:  ", "dyslexia, anxiety", "[documented accommodation]"),
            ("Date of concern:  ", "November 12", "[last month]"),
            ("Current grade:  ", "78%", "[below target]"),
        ]

        prompt_group = VGroup()
        crimson_parts = []
        teal_parts = []

        y_start = 1.2
        for prefix, bad, good in line_data:
            prefix_txt = Text(prefix, font=MONO, color=INK, font_size=17)
            bad_txt = Text(bad, font=MONO, color=CRIMSON, font_size=17)
            good_txt = Text(good, font=MONO, color=TEAL, font_size=17)

            row = VGroup(prefix_txt, bad_txt)
            row.arrange(RIGHT, buff=0.0)
            row.move_to(window.get_left() + RIGHT * (row.width / 2 + 0.5) + UP * (y_start - len(prompt_group) * 0.72))
            row.align_to(window.get_left() + RIGHT * 0.5, LEFT)

            good_txt.move_to(bad_txt.get_center())
            prompt_group.add(row)
            crimson_parts.append(bad_txt)
            teal_parts.append(good_txt)

        bracket = Brace(window, direction=RIGHT, color=TEAL)
        bracket_lbl = Text("redaction practice", font=DISPLAY, color=TEAL,
                           font_size=16, weight="MEDIUM")
        bracket_lbl.next_to(bracket, RIGHT, buff=0.2)

        instruction = SerifLabel("if the redacted version still lets Claude help — use it", accent=TEAL, size=20)
        instruction.next_to(window, DOWN, buff=0.35)

        self.play(FadeIn(window), FadeIn(title_bar), FadeIn(title_txt), run_time=0.4)
        for row in prompt_group:
            self.play(Write(row[0]), Write(row[1]), run_time=0.5)
        self.wait(0.5)
        self.play(Create(bracket), FadeIn(bracket_lbl), run_time=0.5)
        for bad, good in zip(crimson_parts, teal_parts):
            self.play(
                FadeOut(bad, shift=UP * 0.1),
                FadeIn(good, shift=DOWN * 0.1),
                run_time=0.45,
            )
        self.play(
            Write(instruction[0]),
            Create(instruction[1]),
            run_time=0.7,
        )
        self.wait(11.0)
