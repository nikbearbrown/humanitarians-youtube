"""vox_scenes.py — vox-buildlog-assessment
Why Your Students' CLAUDE.md Is the Best Evidence They Conducted the Build.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B07) gets no scene — compiles as slate.
"""
import sys
import pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403


class B01_Title(Scene):
    def construct(self):
        eyebrow = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                       color=INK, font_size=22, weight="MEDIUM")
        eyebrow.to_edge(UP, buff=0.7)
        t1 = Text("Why the build log is", font=SERIF, color=INK, font_size=44)
        t2 = Text("the assessment you cannot fake", font=SERIF, color=TEAL, font_size=44)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=TEAL)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(8.4)


class B02_TwoLogs(Scene):
    def construct(self):
        title = Text("two build logs — same code", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Left column: Student A (teal, conducting)
        left_header = Text("Student A", font=DISPLAY,
                           color=TEAL, font_size=20, weight="MEDIUM")
        left_header.move_to(np.array([-4.2, 1.8, 0]))

        left_items = [
            "five-element specification",
            "plan-mode edit documented",
            "three handoff conditions",
            "capacity labels [PA] [PF]",
            "/rewind + respec",
            "Lessons Learned entry",
        ]
        left_group = VGroup()
        for item in left_items:
            row = Text(item, font=SERIF, color=TEAL, font_size=16)
            left_group.add(row)
        left_group.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        left_group.next_to(left_header, DOWN, buff=0.35)

        # Right column: Student B (crimson, bare prompts)
        right_header = Text("Student B", font=DISPLAY,
                            color=CRIMSON, font_size=20, weight="MEDIUM")
        right_header.move_to(np.array([3.0, 1.8, 0]))

        right_items = [
            "add a contact page",
            "make it look better",
            "fix the link",
            "(no gates)",
            "(no conditions)",
            "(no labels)",
        ]
        right_group = VGroup()
        for item in right_items:
            row = Text(item, font=SERIF, color=CRIMSON, font_size=16)
            right_group.add(row)
        right_group.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        right_group.next_to(right_header, DOWN, buff=0.35)

        divider = Line(UP * 2.2 + ORIGIN, DOWN * 2.3 + ORIGIN,
                       stroke_width=1.2, color=SLATE)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.5)
        for litem, ritem in zip(left_group, right_group):
            self.play(FadeIn(litem), FadeIn(ritem), run_time=0.35)
        self.wait(7.5)


class B03_Question(Scene):
    def construct(self):
        l1 = Text("Same code.", font=SERIF, color=INK, font_size=48)
        l2 = Text("Different discipline.", font=SERIF, color=TEAL, font_size=48)
        l3 = Text("How do you tell?", font=SERIF, color=INK, font_size=48)
        question = VGroup(l1, l2, l3).arrange(DOWN, center=True, buff=0.3)
        question.scale_to_fit_width(12.0)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.2,
                    question.get_corner(DR) + DOWN * 0.2,
                    stroke_width=1.5, color=TEAL)
        self.play(FadeIn(l1), run_time=0.5)
        self.play(FadeIn(l2), run_time=0.5)
        self.play(FadeIn(l3), Create(rule), run_time=0.6)
        self.wait(7.4)


class B04_WhatAICantGenerate(Scene):
    def construct(self):
        title = Text("AI generates the code — not the decision record", font=SERIF,
                     color=INK, font_size=24)
        title.to_edge(UP, buff=0.7)

        # Left box: what AI can generate (crimson)
        left_box = Rectangle(width=4.5, height=3.0)
        left_box.set_fill(GROUND, 0).set_stroke(CRIMSON, 2.0)
        left_box.move_to(np.array([-3.5, -0.3, 0]))
        left_title = Text("AI can generate", font=DISPLAY,
                          color=CRIMSON, font_size=18, weight="MEDIUM")
        left_title.next_to(left_box, UP, buff=0.15)
        left_content = Text("working HTML / CSS / JS", font=MONO, color=INK, font_size=17)
        left_content.move_to(left_box.get_center())

        # Right box: what AI cannot generate (teal)
        right_box = Rectangle(width=5.5, height=3.8)
        right_box.set_fill(GROUND, 0).set_stroke(TEAL, 2.0)
        right_box.move_to(np.array([3.5, -0.3, 0]))
        right_title = Text("AI cannot generate", font=DISPLAY,
                           color=TEAL, font_size=18, weight="MEDIUM")
        right_title.next_to(right_box, UP, buff=0.15)

        right_items = VGroup(
            Text("spec written before the prompt", font=SERIF, color=TEAL, font_size=15),
            Text("plan-mode edit made by student", font=SERIF, color=TEAL, font_size=15),
            Text("handoff condition that gated step", font=SERIF, color=TEAL, font_size=15),
            Text("/rewind + respec on failure", font=SERIF, color=TEAL, font_size=15),
        )
        right_items.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        right_items.move_to(right_box.get_center())

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(left_box), FadeIn(left_title), run_time=0.4)
        self.play(FadeIn(left_content), run_time=0.4)
        self.play(Create(right_box), FadeIn(right_title), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(item) for item in right_items],
                              lag_ratio=0.2, run_time=0.8))
        self.wait(8.5)


class B05_RubricFive(Scene):
    def construct(self):
        title = Text("the build-log rubric", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        dimensions = [
            ("1.", "Specification quality",
             "five elements specific and load-bearing"),
            ("2.", "Gate execution",
             "every step gated, plan-mode edits noted"),
            ("3.", "Handoff conditions",
             "testable, binary; /rewind documented"),
            ("4.", "Capacity labeling",
             "at least three capacities labeled"),
            ("5.", "Lessons learned",
             "one entry suitable for CLAUDE.md"),
        ]

        rows = VGroup()
        for num, label, desc in dimensions:
            row_bg = Rectangle(width=12.5, height=1.0)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.2)
            num_text = Text(num, font=MONO, color=TEAL, font_size=20)
            num_text.move_to(row_bg.get_center() + LEFT * 5.5)
            label_text = Text(label, font=DISPLAY, color=TEAL,
                              font_size=18, weight="MEDIUM")
            label_text.move_to(row_bg.get_center() + LEFT * 2.5)
            desc_text = Text(desc, font=SERIF, color=INK, font_size=16)
            desc_text.move_to(row_bg.get_center() + RIGHT * 2.5)
            score_text = Text("0-4", font=MONO, color=SLATE, font_size=17)
            score_text.move_to(row_bg.get_center() + RIGHT * 5.7)
            rows.add(VGroup(row_bg, num_text, label_text, desc_text, score_text))

        rows.arrange(DOWN, buff=0.28)
        rows.move_to(ORIGIN + DOWN * 0.1)
        rows.scale_to_fit_width(13.5)

        total = Text("Total: 20 points", font=SERIF, color=SLATE, font_size=18)
        total.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.4)
        self.play(FadeIn(total), run_time=0.4)
        self.wait(8.5)


class B06_ScoreScale(Scene):
    def construct(self):
        title = Text("score interpretation", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Horizontal scale
        axis = Line(LEFT * 5.5 + UP * 0.2, RIGHT * 5.5 + UP * 0.2,
                    stroke_width=2.0, color=SLATE)

        # Four segments
        segments = [
            (-5.5, -2.0, CRIMSON, "absent", "0-5"),
            (-2.0, 0.5, GOLD, "uneven", "6-10"),
            (0.5, 3.0, SLATE, "partial", "11-15"),
            (3.0, 5.5, TEAL, "conducting\nevident", "16-20"),
        ]

        seg_group = VGroup()
        for x_start, x_end, col, label, score in segments:
            width = x_end - x_start
            seg = Rectangle(width=width, height=0.8)
            seg.set_fill(col, 0.6).set_stroke(col, 0)
            seg.move_to(np.array([(x_start + x_end) / 2, 0.2, 0]))
            score_lbl = Text(score, font=MONO, color=INK, font_size=15)
            score_lbl.move_to(seg.get_center())
            label_lbl = Text(label, font=SERIF, color=INK, font_size=14)
            label_lbl.next_to(seg, DOWN, buff=0.2)
            seg_group.add(VGroup(seg, score_lbl, label_lbl))

        # Student markers
        # Student A at 17 (in teal segment at ~x=4.5)
        marker_a = Triangle(fill_color=TEAL, fill_opacity=1.0,
                            stroke_color=TEAL, stroke_width=0)
        marker_a.scale(0.2)
        marker_a.move_to(np.array([4.5, 0.85, 0]))
        label_a = Text("A: 17", font=DISPLAY, color=TEAL,
                       font_size=16, weight="MEDIUM")
        label_a.next_to(marker_a, UP, buff=0.1)

        # Student B at 7 (in amber segment at ~x=-0.8)
        marker_b = Triangle(fill_color=CRIMSON, fill_opacity=1.0,
                            stroke_color=CRIMSON, stroke_width=0)
        marker_b.scale(0.2)
        marker_b.move_to(np.array([-0.8, 0.85, 0]))
        label_b = Text("B: 7", font=DISPLAY, color=CRIMSON,
                       font_size=16, weight="MEDIUM")
        label_b.next_to(marker_b, UP, buff=0.1)

        footer = Text("the code grade and the build-log score can diverge substantially — that is the point",
                      font=SERIF, color=SLATE, font_size=17)
        footer.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(axis), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(s) for s in seg_group],
                              lag_ratio=0.15, run_time=0.8))
        self.play(FadeIn(marker_a), FadeIn(label_a),
                  FadeIn(marker_b), FadeIn(label_b), run_time=0.6)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(7.5)


class B08_AssessmentPlan(Scene):
    def construct(self):
        title = Text("formative first, summative at capstone", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        rows_data = [
            ("Build 1", "formative",
             "shapes feedback and conversation — not graded"),
            ("Build 2", "formative",
             "rubric calibration via peer review"),
            ("Build 3 (capstone)", "summative",
             "build log supplements or replaces code grade"),
        ]

        rows = VGroup()
        for build, assessment, desc in rows_data:
            row_bg = Rectangle(width=12.5, height=1.2)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
            build_text = Text(build, font=MONO, color=TEAL, font_size=20)
            build_text.move_to(row_bg.get_center() + LEFT * 4.2)
            assess_text = Text(assessment, font=DISPLAY, color=INK,
                               font_size=18, weight="MEDIUM")
            assess_text.move_to(row_bg.get_center() + LEFT * 0.5)
            desc_text = Text(desc, font=SERIF, color=SLATE, font_size=15)
            desc_text.move_to(row_bg.get_center() + RIGHT * 3.2)
            rows.add(VGroup(row_bg, build_text, assess_text, desc_text))

        rows.arrange(DOWN, buff=0.45)
        rows.move_to(ORIGIN + DOWN * 0.1)
        rows.scale_to_fit_width(13.5)

        footer = Text("peer review handles scoring; teacher reviews disagreements",
                      font=SERIF, color=SLATE, font_size=18)
        footer.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(7.5)


class B09_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Assess the build log.", font=SERIF, color=TEAL, font_size=46)
        m2 = Text("That is the conducting", font=SERIF, color=INK, font_size=46)
        m3 = Text("you cannot fake.", font=SERIF, color=TEAL, font_size=46)
        main_text = VGroup(m1, m2, m3).arrange(DOWN, center=True, buff=0.35)
        main_text.scale_to_fit_width(12.0)
        main_text.move_to(ORIGIN + UP * 0.2)

        rule = Line(main_text.get_corner(DL) + DOWN * 0.15,
                    main_text.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=TEAL)

        handle = Text("@nikbearbrown", font=SERIF, color=CRIMSON, font_size=24)
        handle.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(main_text), Create(rule), run_time=1.0)
        self.play(FadeIn(handle), run_time=0.5)
        self.wait(8.0)
