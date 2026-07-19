"""receiving-vs-producing — vox_scenes.py
Why AI Produces Lesson Plans Where the Teacher Does All the Thinking
"""
from vox_graphics import *
import numpy as np


class B04_LessonAudit(Scene):
    """THE PROBLEM — three activities, all RECEIVING, labeled."""
    def construct(self):
        activities = [
            ("Teacher demonstrates\ncombustion reaction", "teacher thinks"),
            ("Students copy the equation\n(worksheet)", "look up answer"),
            ("Homework problem set", "feedback deferred 3 weeks"),
        ]

        rows = VGroup()
        for act_name, sub_label in activities:
            act_box = Rectangle(width=5.5, height=1.2)
            act_box.set_fill(GROUND, 1).set_stroke(SLATE, 1.0, opacity=0.5)
            act_txt = Text(act_name, font=SERIF, color=INK, font_size=20, line_spacing=1.2)
            if act_txt.width > 5.1:
                act_txt.scale_to_fit_width(5.1)
            act_txt.move_to(act_box)
            act_card = VGroup(act_box, act_txt)

            tag_box = Rectangle(width=2.4, height=1.2)
            tag_box.set_fill(CRIMSON, 1).set_stroke(width=0)
            tag_txt = Text("RECEIVING", font=DISPLAY, color=WHITE, font_size=17, weight="BOLD")
            tag_txt.move_to(tag_box)
            tag_card = VGroup(tag_box, tag_txt)

            row = VGroup(act_card, tag_card)
            row.arrange(RIGHT, buff=0.3)

            sub_txt = Text(sub_label, font=SERIF, color=CRIMSON,
                           font_size=16, slant=ITALIC)
            sub_txt.next_to(tag_box, DOWN, buff=0.1)

            rows.add(VGroup(row, sub_txt))

        rows.arrange(DOWN, buff=0.45)
        rows.move_to(ORIGIN)

        title = Text("Claude's lesson plan — cognitive labor audit",
                     font=DISPLAY, color=INK, font_size=18, weight="MEDIUM")
        title.next_to(rows, UP, buff=0.45)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row[0]), run_time=0.5)
            self.play(FadeIn(row[1], shift=DOWN * 0.1), run_time=0.4)
        self.wait(14.5)


class B05_ReceivingVsProducing(Scene):
    """THE MECHANISM — receiving vs. producing side-by-side."""
    def construct(self):
        # Header question
        header = Text("Who is doing the thinking?", font=DISPLAY, color=INK,
                      font_size=22, weight="BOLD")
        header.move_to(UP * 2.8)

        # Left: RECEIVING (CRIMSON)
        left_box = Rectangle(width=5.0, height=3.8)
        left_box.set_fill(GROUND, 1).set_stroke(CRIMSON, 2.5)
        left_header = Text("RECEIVING", font=DISPLAY, color=CRIMSON,
                           font_size=20, weight="BOLD")
        left_header.move_to(left_box.get_top() + DOWN * 0.45)

        receiving_words = ["watching", "listening", "copying", "looking up"]
        rw_group = VGroup(*[
            Text(w, font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC)
            for w in receiving_words
        ])
        rw_group.arrange(DOWN, buff=0.28)
        rw_group.move_to(left_box.get_center() + DOWN * 0.1)
        left_card = VGroup(left_box, left_header, rw_group)

        # Right: PRODUCING (TEAL)
        right_box = Rectangle(width=5.0, height=3.8)
        right_box.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        right_header = Text("PRODUCING", font=DISPLAY, color=TEAL,
                            font_size=20, weight="BOLD")
        right_header.move_to(right_box.get_top() + DOWN * 0.45)

        producing_words = ["retrieving", "applying", "explaining", "predicting"]
        pw_group = VGroup(*[
            Text(w, font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
            for w in producing_words
        ])
        pw_group.arrange(DOWN, buff=0.28)
        pw_group.move_to(right_box.get_center() + DOWN * 0.1)
        right_card = VGroup(right_box, right_header, pw_group)

        pair = VGroup(left_card, right_card).arrange(RIGHT, buff=0.8)
        pair.move_to(DOWN * 0.1)

        self.play(FadeIn(header), run_time=0.5)
        self.play(
            FadeIn(left_box), FadeIn(left_header),
            FadeIn(right_box), FadeIn(right_header),
            run_time=0.6,
        )
        for rw, pw in zip(rw_group, pw_group):
            self.play(
                FadeIn(rw, shift=DOWN * 0.08),
                FadeIn(pw, shift=DOWN * 0.08),
                run_time=0.45,
            )
        self.wait(12.5)


class B06_ActivityFlip(Scene):
    """THE EXAMPLE — three activities flip CRIMSON→TEAL with redesign desc."""
    def construct(self):
        rows_data = [
            (
                "Teacher demo: combustion reaction",
                "students predict products → compare to observation",
            ),
            (
                "Students copy the equation",
                "students write equation from own prediction notes",
            ),
            (
                "Worksheet: 'What are the reactants?'",
                "'Why oxygen? What happens in a sealed container?'",
            ),
        ]

        rows = VGroup()
        for old_act, new_act in rows_data:
            act_txt = Text(old_act, font=SERIF, color=INK, font_size=18, line_spacing=1.2)
            if act_txt.width > 6.5:
                act_txt.scale_to_fit_width(6.5)

            old_tag_box = Rectangle(width=2.3, height=0.8)
            old_tag_box.set_fill(CRIMSON, 1).set_stroke(width=0)
            old_tag_txt = Text("RECEIVING", font=DISPLAY, color=WHITE,
                               font_size=14, weight="BOLD")
            old_tag_txt.move_to(old_tag_box)
            old_tag = VGroup(old_tag_box, old_tag_txt)

            new_tag_box = Rectangle(width=2.3, height=0.8)
            new_tag_box.set_fill(TEAL, 1).set_stroke(width=0)
            new_tag_txt = Text("PRODUCING", font=DISPLAY, color=WHITE,
                               font_size=14, weight="BOLD")
            new_tag_txt.move_to(new_tag_box)
            new_tag = VGroup(new_tag_box, new_tag_txt)
            new_tag.move_to(old_tag.get_center())

            new_desc = Text(new_act, font=SERIF, color=TEAL, font_size=15, line_spacing=1.2)
            if new_desc.width > 6.5:
                new_desc.scale_to_fit_width(6.5)

            row_top = VGroup(act_txt, old_tag)
            row_top.arrange(RIGHT, buff=0.4)
            rows.add(VGroup(row_top, old_tag, new_tag, new_desc))

        rows.arrange(DOWN, buff=0.6)
        rows.move_to(ORIGIN)

        for i, row in enumerate(rows):
            row_top = row[0]
            old_tag = row[1]
            new_tag = row[2]
            new_desc = row[3]

            new_tag.move_to(old_tag.get_center())
            new_desc.next_to(row_top, DOWN, buff=0.15)

            self.play(FadeIn(row_top), run_time=0.5)
            self.play(
                FadeOut(old_tag, scale=0.85),
                FadeIn(new_tag, scale=1.1),
                run_time=0.5,
            )
            self.play(FadeIn(new_desc, shift=DOWN * 0.1), run_time=0.5)

        self.wait(21.0)


class B08_AuditPrompt(Scene):
    """THE PRACTICE — cognitive labor audit on notepad card."""
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
            "For every major activity in the plan,\n"
            "write one word:\n"
            "receiving   or   producing.",
            font=SERIF, color=INK, font_size=24, line_spacing=1.4,
        )
        if q_txt.width > 9.5:
            q_txt.scale_to_fit_width(9.5)
        q_txt.move_to(pad.get_center() + UP * 0.25)

        bracket = Brace(q_txt, direction=RIGHT, color=TEAL)
        bracket_lbl = Text("the audit", font=DISPLAY, color=TEAL,
                           font_size=18, weight="MEDIUM")
        bracket_lbl.next_to(bracket, RIGHT, buff=0.2)

        instruction = SerifLabel(
            "one receiving moment → one producing redesign",
            accent=TEAL, size=21,
        )
        instruction.next_to(pad, DOWN, buff=0.3)

        self.play(FadeIn(pad), Create(rules), run_time=0.5)
        self.play(Write(q_txt), run_time=1.8)
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
        self.wait(12.4)
