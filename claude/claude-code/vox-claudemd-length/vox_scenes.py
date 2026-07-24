"""vox_scenes.py — vox-claudemd-length
Why CLAUDE.md Breaks When It Gets Too Long.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B05) gets no scene — compiles as slate.
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
        t1 = Text("Why CLAUDE.md breaks", font=SERIF, color=INK, font_size=44)
        t2 = Text("when it gets too long", font=SERIF, color=CRIMSON, font_size=44)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(7.4)


class B02_GrowingDoc(Scene):
    def construct(self):
        title = Text("CLAUDE.md grows across builds", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Three document bars growing taller
        bar_stages = [
            ("Build 1", "47 lines", TEAL, 1.0),
            ("Build 2", "80 lines", TEAL, 1.7),
            ("Build 3", "220 lines", CRIMSON, 4.0),
        ]

        bars = VGroup()
        bar_labels = VGroup()
        line_labels = VGroup()

        x_positions = [-3.5, 0.0, 3.5]
        for (stage, lines, col, height), x in zip(bar_stages, x_positions):
            bar = Rectangle(width=2.0, height=height)
            bar.set_fill(col, 0.7).set_stroke(col, 0)
            bar.move_to(np.array([x, -1.0 + height / 2 - 2.0, 0]))
            stage_label = Text(stage, font=DISPLAY, color=INK,
                               font_size=18, weight="MEDIUM")
            stage_label.next_to(bar, DOWN, buff=0.2)
            line_label = Text(lines, font=MONO, color=col, font_size=18)
            line_label.next_to(bar, UP, buff=0.2)
            bars.add(bar)
            bar_labels.add(stage_label)
            line_labels.add(line_label)

        # Compliance meter (simplified as a bar on the right)
        compliance_label = Text("rule compliance", font=SERIF, color=INK, font_size=22)
        compliance_label.to_edge(RIGHT, buff=1.5).shift(UP * 1.5)

        meter_high = Rectangle(width=1.0, height=2.5)
        meter_high.set_fill(TEAL, 0.8).set_stroke(TEAL, 0)
        meter_high.move_to(RIGHT * 5.5 + UP * 0.3)
        meter_dip = Rectangle(width=1.0, height=1.2)
        meter_dip.set_fill(CRIMSON, 0.7).set_stroke(CRIMSON, 0)
        meter_dip.move_to(RIGHT * 5.5 + DOWN * 0.9)
        dip_label = SerifLabel("dips at 220", accent=CRIMSON, size=18)
        dip_label.next_to(meter_dip, DOWN, buff=0.2)

        self.play(FadeIn(title), run_time=0.5)
        for bar, bl, ll in zip(bars, bar_labels, line_labels):
            self.play(FadeIn(bar, shift=UP * 0.2), FadeIn(bl), FadeIn(ll), run_time=0.5)
        self.play(FadeIn(compliance_label), FadeIn(meter_high), run_time=0.5)
        self.play(FadeIn(meter_dip), FadeIn(dip_label), run_time=0.5)
        self.wait(8.5)


class B03_Question(Scene):
    def construct(self):
        l1 = Text("More rules.", font=SERIF, color=INK, font_size=46)
        l2 = Text("Less compliance.", font=SERIF, color=CRIMSON, font_size=46)
        l3 = Text("Why?", font=SERIF, color=INK, font_size=46)
        question = VGroup(l1, l2, l3).arrange(DOWN, center=True, buff=0.3)
        question.scale_to_fit_width(10.5)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.2,
                    question.get_corner(DR) + DOWN * 0.2,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(l1), run_time=0.5)
        self.play(FadeIn(l2), run_time=0.5)
        self.play(FadeIn(l3), Create(rule), run_time=0.6)
        self.wait(7.4)


class B04_CompetingContext(Scene):
    def construct(self):
        title = Text("the rule competes with noise", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Document representation growing with noise
        base_entries = VGroup(
            Text("Vanilla CSS only", font=SERIF, color=TEAL, font_size=20),
            Text("No Tailwind, no preprocessor", font=SERIF, color=INK, font_size=19),
            Text("school server: static HTML only", font=SERIF, color=INK, font_size=19),
        )
        base_entries.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        base_entries.move_to(ORIGIN + UP * 1.0)

        noise_entries = VGroup(
            Text("Sprint goal: finish grading by Friday", font=SERIF, color=CRIMSON, font_size=18),
            Text("Colleague phone: 617-555-0109", font=SERIF, color=CRIMSON, font_size=18),
            Text("Vanilla CSS (duplicate)", font=SERIF, color=CRIMSON, font_size=18),
            Text("Vanilla CSS only no Tailwind (dup.)", font=SERIF, color=CRIMSON, font_size=18),
        )
        noise_entries.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        noise_entries.next_to(base_entries, DOWN, buff=0.3)

        noise_label = SerifLabel("CLAUDE.md is advisory — compliance is probabilistic", accent=SLATE, size=20)
        noise_label.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(e) for e in base_entries],
                              lag_ratio=0.15, run_time=0.7))
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.1) for e in noise_entries],
                              lag_ratio=0.2, run_time=1.0))
        self.play(FadeIn(noise_label), run_time=0.4)
        self.wait(8.4)


class B06_ThreeMove(Scene):
    def construct(self):
        title = Text("the three-move fix", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        moves = [
            ("CLAUDE.md", "under 200 lines — five categories only"),
            ("Skills", "workflow content — loaded on demand"),
            ("Hooks", "inviolable rules — execute regardless"),
        ]
        rows = VGroup()
        for label, desc in moves:
            row_bg = Rectangle(width=11.5, height=1.2)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.2)
            label_text = Text(label, font=DISPLAY, color=TEAL,
                              font_size=22, weight="MEDIUM")
            label_text.move_to(row_bg.get_center() + LEFT * 3.8)
            desc_text = Text(desc, font=SERIF, color=INK, font_size=20)
            desc_text.move_to(row_bg.get_center() + RIGHT * 1.2)
            rows.add(VGroup(row_bg, label_text, desc_text))

        rows.arrange(DOWN, buff=0.4)
        rows.move_to(ORIGIN + DOWN * 0.1)
        rows.scale_to_fit_width(13.5)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.5)
        self.wait(8.5)


class B07_ComplianceMeter(Scene):
    def construct(self):
        title = Text("signal-to-noise degrades with length", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Horizontal axis
        axis = Line(LEFT * 5.5 + DOWN * 0.5, RIGHT * 5.0 + DOWN * 0.5,
                    stroke_width=2.0, color=SLATE)

        # Axis labels
        line_marks = [("50", -4.5), ("100", -2.0), ("200", 0.5), ("300", 3.0)]
        mark_group = VGroup()
        for label, x in line_marks:
            mark = Line(np.array([x, -0.6, 0]), np.array([x, -0.4, 0]),
                        stroke_width=1.5, color=SLATE)
            text = Text(label + " lines", font=MONO, color=SLATE, font_size=16)
            text.move_to(np.array([x, -0.9, 0]))
            mark_group.add(mark, text)

        axis_label = Text("CLAUDE.md length", font=SERIF, color=SLATE, font_size=18)
        axis_label.next_to(axis, RIGHT, buff=0.3)

        # Compliance curve (piecewise segments)
        pts_teal = [
            np.array([-4.5, 2.0, 0]),
            np.array([-2.0, 2.0, 0]),
            np.array([0.5, 1.7, 0]),
        ]
        pts_crimson = [
            np.array([0.5, 1.7, 0]),
            np.array([3.0, 0.5, 0]),
        ]

        seg_teal = VGroup()
        for i in range(len(pts_teal) - 1):
            seg_teal.add(Line(pts_teal[i], pts_teal[i + 1],
                              stroke_width=3.5, color=TEAL))

        seg_crimson = VGroup()
        for i in range(len(pts_crimson) - 1):
            seg_crimson.add(Line(pts_crimson[i], pts_crimson[i + 1],
                                 stroke_width=3.5, color=CRIMSON))

        compliance_label = Text("compliance", font=SERIF, color=SLATE, font_size=18)
        compliance_label.move_to(LEFT * 5.5 + UP * 1.8)

        dip_label = SerifLabel("dips at 200", accent=CRIMSON, size=20)
        dip_label.move_to(np.array([0.5, 1.3, 0]))

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(axis), FadeIn(mark_group), run_time=0.5)
        self.play(FadeIn(compliance_label), run_time=0.3)
        self.play(LaggedStart(*[Create(s) for s in seg_teal],
                              lag_ratio=0.3, run_time=0.8))
        self.play(LaggedStart(*[Create(s) for s in seg_crimson],
                              lag_ratio=0.3, run_time=0.6))
        self.play(FadeIn(dip_label), run_time=0.4)
        self.wait(8.0)


class B08_AuditQuestions(Scene):
    def construct(self):
        title = Text("audit each entry", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        questions = [
            ("Claude infers from code?", "cut it"),
            ("Changes session to session?", "move to TODO.md"),
            ("A workflow you repeat?", "move to Skill"),
            ("Must hold without exception?", "convert to Hook"),
        ]
        rows = VGroup()
        for question, action in questions:
            row_bg = Rectangle(width=12.0, height=1.1)
            row_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.0)
            q_text = Text(question, font=SERIF, color=INK, font_size=20)
            q_text.move_to(row_bg.get_center() + LEFT * 2.5)
            a_text = Text(action, font=DISPLAY, color=TEAL,
                          font_size=20, weight="MEDIUM")
            a_text.move_to(row_bg.get_center() + RIGHT * 3.5)
            rows.add(VGroup(row_bg, q_text, a_text))

        rows.arrange(DOWN, buff=0.3)
        rows.move_to(ORIGIN + DOWN * 0.1)
        rows.scale_to_fit_width(13.5)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.4)
        self.wait(7.4)


class B09_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Short and specific.", font=SERIF, color=TEAL, font_size=44)
        m2 = Text("Not long and aspirational.", font=SERIF, color=INK, font_size=44)
        main_text = VGroup(m1, m2).arrange(DOWN, center=True, buff=0.35)
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
