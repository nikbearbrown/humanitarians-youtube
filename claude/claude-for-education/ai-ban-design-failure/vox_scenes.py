"""ai-ban-design-failure — vox_scenes.py
Why Banning AI from Assignments Usually Teaches the Wrong Lesson
"""
from vox_graphics import *
import numpy as np


class B04_BanFailureMap(Scene):
    """THE PROBLEM — ban + detection → assignment unchanged; design failure not addressed."""
    def construct(self):
        # Left side: BAN CHAIN (CRIMSON)
        ban_box = Rectangle(width=3.0, height=1.1)
        ban_box.set_fill(CRIMSON, 1).set_stroke(width=0)
        ban_txt = Text("AI BAN", font=DISPLAY, color=WHITE, font_size=22, weight="BOLD")
        ban_txt.move_to(ban_box)
        ban_card = VGroup(ban_box, ban_txt)

        arr_down = Arrow(ORIGIN, DOWN * 0.5, buff=0, color=CRIMSON, stroke_width=2.5)

        detect_box = Rectangle(width=3.0, height=1.1)
        detect_box.set_fill(CRIMSON, 0.7).set_stroke(width=0)
        detect_txt = Text("DETECTION", font=DISPLAY, color=WHITE, font_size=22, weight="MEDIUM")
        detect_txt.move_to(detect_box)
        detect_card = VGroup(detect_box, detect_txt)

        ban_col = VGroup(ban_card, arr_down, detect_card)
        ban_col.arrange(DOWN, buff=0.2)
        ban_col.move_to(LEFT * 3.2 + UP * 0.4)

        # Right side: ASSIGNMENT UNCHANGED (SLATE, muted)
        assign_box = Rectangle(width=4.0, height=2.5)
        assign_box.set_fill(GROUND, 1).set_stroke(SLATE, 1.5)
        assign_txt = Text(
            "ASSIGNMENT\nUNCHANGED",
            font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM",
            line_spacing=1.2,
        )
        assign_txt.move_to(assign_box)
        assign_card = VGroup(assign_box, assign_txt)
        assign_card.move_to(RIGHT * 2.8 + UP * 0.4)

        # Gap arrow: points from ban chain down to "design failure"
        gap_arr = Arrow(
            ban_col.get_right() + RIGHT * 0.1,
            assign_card.get_left() + LEFT * 0.1,
            buff=0.05, color=CRIMSON, stroke_width=2, stroke_opacity=0.7,
        )

        gap_lbl = Text("design failure\nnot addressed", font=SERIF, color=CRIMSON,
                       font_size=19, line_spacing=1.2, slant=ITALIC)
        gap_lbl.move_to(gap_arr.get_center() + UP * 0.65)

        note = SerifLabel("the ban adds a rule — it doesn't fix the assignment", accent=CRIMSON, size=21)
        note.next_to(assign_card, DOWN, buff=0.5)

        self.play(FadeIn(ban_card, scale=0.9), run_time=0.6)
        self.play(GrowArrow(arr_down), FadeIn(detect_card, scale=0.9), run_time=0.6)
        self.play(FadeIn(assign_card), run_time=0.6)
        self.play(GrowArrow(gap_arr), FadeIn(gap_lbl), run_time=0.7)
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.7,
        )
        self.wait(10.8)


class B05_FourModes(Scene):
    """THE MECHANISM — four policy modes, appearing in sequence."""
    def construct(self):
        modes = [
            ("MODE 1", "PROHIBITED",
             "Unassisted skill-building\nor in-class work"),
            ("MODE 2", "PERMITTED WITH\nDISCLOSURE",
             "AI plausible; judgment\nmust be student's"),
            ("MODE 3", "REQUIRED FOR\nPROCESS",
             "AI literacy is itself\nthe learning outcome"),
            ("MODE 4", "REFLECTIVE USE",
             "Student uses AI; then\nreflects on its role"),
        ]

        cards = VGroup()
        for num, name, desc in modes:
            box = Rectangle(width=5.5, height=1.55)
            box.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.8)
            num_txt = Text(num, font=DISPLAY, color=TEAL, font_size=16, weight="BOLD")
            name_txt = Text(name, font=DISPLAY, color=INK, font_size=16, weight="BOLD",
                            line_spacing=1.15)
            desc_txt = Text(desc, font=SERIF, color=INK, font_size=16, line_spacing=1.2)
            row = VGroup(num_txt, name_txt, desc_txt)
            row.arrange(RIGHT, buff=0.35)
            if row.width > 5.2:
                row.scale_to_fit_width(5.2)
            row.move_to(box)
            cards.add(VGroup(box, row))

        cards.arrange(DOWN, buff=0.25)
        cards.move_to(ORIGIN)

        header = Text("FOUR POLICY MODES", font=DISPLAY, color=TEAL,
                      font_size=20, weight="BOLD")
        header.next_to(cards, UP, buff=0.4)

        self.play(FadeIn(header), run_time=0.5)
        for card in cards:
            self.play(FadeIn(card, shift=DOWN * 0.1), run_time=0.55)
        self.wait(16.8)


class B06_RedesignTimeline(Scene):
    """THE EXAMPLE — five-stage timeline with mode tags."""
    def construct(self):
        timeline = Line(LEFT * 5.8, RIGHT * 5.8, color=INK, stroke_width=2.5)
        timeline.move_to(ORIGIN)

        stages = [
            (-4.8, "WEEK 1", "Problem statement\n(timed, in-class)", "M1", CRIMSON),
            (-2.4, "WEEK 2", "Annotated source log\n(AI with disclosure)", "M2", TEAL),
            (0.0,  "WEEK 3", "Draft + AI-use log", "M2", TEAL),
            (2.4,  "WEEK 4", "Oral conference\n(AI cannot attend)", "M1", CRIMSON),
            (4.8,  "WEEK 5", "Final essay +\nrevision note", "M2", TEAL),
        ]

        dots = VGroup()
        labels = VGroup()
        for x, week, desc, mode, color in stages:
            dot = Dot(point=np.array([x, 0.0, 0.0]), radius=0.18, color=color)
            dot.set_fill(color, 1)

            week_txt = Text(week, font=DISPLAY, color=color, font_size=16, weight="MEDIUM")
            week_txt.move_to(np.array([x, 0.55, 0.0]))

            mode_txt = Text(mode, font=DISPLAY, color=color, font_size=14, weight="BOLD")
            mode_txt.move_to(np.array([x, 0.92, 0.0]))

            desc_txt = Text(desc, font=SERIF, color=INK, font_size=16, line_spacing=1.2)
            if desc_txt.width > 2.2:
                desc_txt.scale_to_fit_width(2.2)
            desc_txt.move_to(np.array([x, -0.8, 0.0]))

            dots.add(dot)
            labels.add(VGroup(week_txt, mode_txt, desc_txt))

        note = SerifLabel("AI is permitted with disclosure at stages 2, 3, 5 — the oral conference is not", accent=TEAL, size=18)
        note.move_to(DOWN * 2.1)

        self.play(Create(timeline), run_time=0.6)
        for dot, lbl in zip(dots, labels):
            self.play(
                FadeIn(dot, scale=0.8),
                Write(lbl[0]),
                Write(lbl[1]),
                FadeIn(lbl[2], shift=DOWN * 0.1),
                run_time=0.7,
            )
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.7,
        )
        self.wait(18.5)


class B08_ThreeAuditQuestions(Scene):
    """THE PRACTICE — three audit questions write in sequence."""
    def construct(self):
        questions = [
            "1.  What intellectual skill is this\n"
            "     assignment designed to build?",
            "2.  Can AI produce the artifact\n"
            "     without that skill being exercised?",
            "3.  Which mode fits this\n"
            "     assignment's purpose?",
        ]

        q_objects = VGroup()
        for q in questions:
            txt = Text(q, font=SERIF, color=INK, font_size=22, line_spacing=1.3)
            if txt.width > 10.0:
                txt.scale_to_fit_width(10.0)
            q_objects.add(txt)

        q_objects.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        q_objects.move_to(UP * 0.5)

        note = SerifLabel("name the mode  ·  state the reason", accent=TEAL, size=22)
        note.next_to(q_objects, DOWN, buff=0.55)

        for q in q_objects:
            self.play(Write(q), run_time=1.0)
        self.play(
            Write(note[0]),
            Create(note[1]),
            run_time=0.7,
        )
        self.wait(15.8)
