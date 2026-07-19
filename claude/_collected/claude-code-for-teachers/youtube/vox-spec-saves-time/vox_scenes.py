"""vox_scenes.py — vox-spec-saves-time
Why the 90-Second Request Takes 12 Minutes and the 8-Second Request Takes 45.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B03) gets no scene — compiles as slate.
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
        t1 = Text("Why the 90-second request takes 12 minutes", font=SERIF,
                  color=INK, font_size=38)
        t2 = Text("and the 8-second one takes 45", font=SERIF,
                  color=CRIMSON, font_size=38)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(7.4)


class B02_RequestResult(Scene):
    def construct(self):
        # Left: the 8-word prompt
        prompt_bg = Rectangle(width=5.0, height=2.2)
        prompt_bg.set_fill(SLATE, 0.07).set_stroke(SLATE, 1.2)
        prompt_bg.move_to(LEFT * 3.5 + UP * 1.0)

        prompt_label = Text("The request:", font=DISPLAY, color=INK,
                            font_size=20, weight="MEDIUM")
        prompt_label.next_to(prompt_bg, UP, buff=0.2)

        prompt_text = Text("Add a syllabus page", font=MONO,
                           color=CRIMSON, font_size=22)
        prompt_text.move_to(prompt_bg.get_center() + UP * 0.1)
        prompt_words = Text("8 words", font=SERIF, color=SLATE, font_size=18)
        prompt_words.move_to(prompt_bg.get_center() + DOWN * 0.5)

        # Right: Claude's defaults
        right_bg = Rectangle(width=5.5, height=4.5)
        right_bg.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        right_bg.move_to(RIGHT * 3.0)

        right_header = Text("Claude's defaults", font=DISPLAY, color=CRIMSON,
                            font_size=20, weight="MEDIUM")
        right_header.next_to(right_bg.get_top() + DOWN * 0.45, ORIGIN)

        defaults = VGroup(
            Text("JavaScript-rendered table", font=SERIF, color=INK, font_size=20),
            Text("CDN-loaded Google Font", font=SERIF, color=INK, font_size=20),
            Text("inline styles throughout", font=SERIF, color=INK, font_size=20),
        )
        defaults.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        defaults.move_to(right_bg.get_center() + DOWN * 0.1)

        cost_label = SerifLabel("45 min to fix", accent=CRIMSON, size=22)
        cost_label.next_to(right_bg, DOWN, buff=0.3)

        self.play(FadeIn(prompt_bg), FadeIn(prompt_label), run_time=0.5)
        self.play(FadeIn(prompt_text), FadeIn(prompt_words), run_time=0.4)
        self.play(FadeIn(right_bg), FadeIn(right_header), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d, shift=RIGHT * 0.1) for d in defaults],
                              lag_ratio=0.25, run_time=0.9))
        self.play(FadeIn(cost_label), run_time=0.4)
        self.wait(8.3)


class B04_Question(Scene):
    def construct(self):
        line1 = Text("More words,", font=SERIF, color=INK, font_size=46)
        line2 = Text("less time.", font=SERIF, color=TEAL, font_size=46)
        line3 = Text("Why?", font=SERIF, color=INK, font_size=46)
        question = VGroup(line1, line2, line3).arrange(DOWN, center=True, buff=0.25)
        question.scale_to_fit_width(10.0)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.2,
                    question.get_corner(DR) + DOWN * 0.2,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(line1), run_time=0.5)
        self.play(FadeIn(line2), run_time=0.5)
        self.play(FadeIn(line3), Create(rule), run_time=0.6)
        self.wait(7.4)


class B05_FourDecisions(Scene):
    def construct(self):
        title = Text("four decisions delegated to Claude", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        decisions = [
            "file path",
            "CSS approach",
            "JavaScript inclusion",
            "external dependencies",
        ]
        rows = VGroup()
        for decision in decisions:
            row_bg = Rectangle(width=10.0, height=1.1)
            row_bg.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.0)
            decision_text = Text(decision, font=SERIF, color=INK, font_size=24)
            decision_text.move_to(row_bg.get_center() + LEFT * 2.0)
            claude_label = Text("Claude decides", font=DISPLAY, color=CRIMSON,
                                font_size=18, weight="MEDIUM")
            claude_label.move_to(row_bg.get_center() + RIGHT * 3.0)
            rows.add(VGroup(row_bg, decision_text, claude_label))

        rows.arrange(DOWN, buff=0.35)
        rows.move_to(ORIGIN + DOWN * 0.2)

        cost_label = SerifLabel("45 min correcting four wrong defaults", accent=CRIMSON, size=20)
        cost_label.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.5)
        self.play(FadeIn(cost_label), run_time=0.4)
        self.wait(7.6)


class B06_FiveElements(Scene):
    def construct(self):
        title = Text("the five-element specification", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        elements = [
            ("Operation", "the specific file and action"),
            ("Invariants", "what must not change"),
            ("Context", "CLAUDE.md rules for this step"),
            ("Output format", "what done looks like"),
            ("Negative constraint", "what Claude must not do"),
        ]
        rows = VGroup()
        for label, desc in elements:
            row_bg = Rectangle(width=11.0, height=1.0)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.2)
            label_text = Text(label, font=DISPLAY, color=TEAL,
                              font_size=20, weight="MEDIUM")
            label_text.move_to(row_bg.get_center() + LEFT * 3.2)
            desc_text = Text(desc, font=SERIF, color=INK, font_size=20)
            desc_text.move_to(row_bg.get_center() + RIGHT * 1.5)
            rows.add(VGroup(row_bg, label_text, desc_text))

        rows.arrange(DOWN, buff=0.2)
        rows.move_to(ORIGIN + DOWN * 0.1)
        rows.scale_to_fit_width(13.0)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.45)
        self.wait(9.25)


class B07_ComparisonTable(Scene):
    def construct(self):
        title = Text("request vs specification", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.65)

        col1_h = Text("Request", font=DISPLAY, color=CRIMSON,
                      font_size=22, weight="MEDIUM")
        col2_h = Text("Specification", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        col1_h.move_to(LEFT * 3.5 + UP * 1.8)
        col2_h.move_to(RIGHT * 2.8 + UP * 1.8)

        header_rule = Line(LEFT * 6.5 + UP * 1.35, RIGHT * 6.5 + UP * 1.35,
                           stroke_width=1.0, color=SLATE)

        rows_data = [
            ("(generic name)", "Create src/syllabus.html"),
            ("(implicit)", "No other files modified"),
            ("(none)", "Per CLAUDE.md: vanilla HTML"),
            ("(a page)", "Semantic table, nav link, 375px"),
            ("(none)", "No JS, no CDN, no new deps"),
        ]
        req_col = VGroup()
        spec_col = VGroup()
        for req, spec in rows_data:
            r = Text(req, font=SERIF, color=CRIMSON, font_size=19)
            s = Text(spec, font=SERIF, color=TEAL, font_size=19)
            req_col.add(r)
            spec_col.add(s)

        req_col.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        spec_col.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        req_col.move_to(LEFT * 3.5 + UP * 0.3)
        spec_col.move_to(RIGHT * 2.5 + UP * 0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(col1_h), FadeIn(col2_h), run_time=0.4)
        self.play(Create(header_rule), run_time=0.3)
        for r, s in zip(req_col, spec_col):
            self.play(FadeIn(r), FadeIn(s), run_time=0.4)
        self.wait(6.8)


class B08_TimeComparison(Scene):
    def construct(self):
        title = Text("the same decisions — different moment", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Left: specification path
        left_label = Text("specification", font=DISPLAY, color=TEAL,
                          font_size=22, weight="MEDIUM")
        left_label.move_to(LEFT * 3.8 + UP * 1.8)

        spec_write = Rectangle(width=1.5, height=1.0)
        spec_write.set_fill(TEAL, 0.8).set_stroke(TEAL, 0)
        spec_write.move_to(LEFT * 4.8 + UP * 0.4)
        spec_write_label = Text("90s", font=MONO, color=INK, font_size=18)
        spec_write_label.move_to(spec_write.get_center())

        spec_build = Rectangle(width=3.5, height=1.0)
        spec_build.set_fill(TEAL, 0.5).set_stroke(TEAL, 0)
        spec_build.move_to(LEFT * 2.55 + UP * 0.4)
        spec_build_label = Text("12 min build", font=MONO, color=INK, font_size=18)
        spec_build_label.move_to(spec_build.get_center())

        spec_total = SerifLabel("12 min 90s total", accent=TEAL, size=18)
        spec_total.move_to(LEFT * 3.8 + DOWN * 0.4)

        # Right: request path
        right_label = Text("request", font=DISPLAY, color=CRIMSON,
                           font_size=22, weight="MEDIUM")
        right_label.move_to(RIGHT * 2.8 + UP * 1.8)

        req_write = Rectangle(width=0.3, height=1.0)
        req_write.set_fill(INK, 0.6).set_stroke(INK, 0)
        req_write.move_to(RIGHT * 1.45 + UP * 0.4)
        req_write_label = Text("8s", font=MONO, color=INK, font_size=14)
        req_write_label.move_to(req_write.get_center())

        req_build = Rectangle(width=4.5, height=1.0)
        req_build.set_fill(CRIMSON, 0.7).set_stroke(CRIMSON, 0)
        req_build.move_to(RIGHT * 3.75 + UP * 0.4)
        req_build_label = Text("45 min correction", font=MONO, color=INK, font_size=18)
        req_build_label.move_to(req_build.get_center())

        req_total = SerifLabel("45 min total", accent=CRIMSON, size=18)
        req_total.move_to(RIGHT * 2.8 + DOWN * 0.4)

        divider = DashedLine(UP * 2.5, DOWN * 2.5, stroke_width=1.0, color=SLATE)
        divider.move_to(ORIGIN + LEFT * 0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_label), FadeIn(right_label), Create(divider), run_time=0.5)
        self.play(FadeIn(spec_write), FadeIn(spec_write_label), run_time=0.4)
        self.play(FadeIn(spec_build), FadeIn(spec_build_label), run_time=0.5)
        self.play(FadeIn(spec_total), run_time=0.3)
        self.play(FadeIn(req_write), FadeIn(req_write_label), run_time=0.3)
        self.play(FadeIn(req_build), FadeIn(req_build_label), run_time=0.5)
        self.play(FadeIn(req_total), run_time=0.3)
        self.wait(7.7)


class B09_ClassroomCase(Scene):
    def construct(self):
        title = Text("classroom case", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Left: request path -> CDN blocked
        left_bg = Rectangle(width=5.5, height=4.2)
        left_bg.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        left_bg.to_edge(LEFT, buff=0.8)

        left_h = Text("without constraint", font=DISPLAY, color=CRIMSON,
                      font_size=20, weight="MEDIUM")
        left_h.next_to(left_bg.get_top() + DOWN * 0.45, ORIGIN)

        left_step1 = Text("request: add resources page", font=SERIF, color=INK, font_size=19)
        left_step2 = Text("Claude: JS accordion + Google Fonts", font=SERIF, color=INK, font_size=18)
        left_step3 = Text("school server blocks CDN", font=SERIF, color=CRIMSON, font_size=19)
        left_items = VGroup(left_step1, left_step2, left_step3)
        left_items.arrange(DOWN, center=True, buff=0.4)
        left_items.move_to(left_bg.get_center() + DOWN * 0.1)

        cost_badge = LabelChip("38 min cleanup", accent=CRIMSON, size=18)
        cost_badge.next_to(left_bg, DOWN, buff=0.3)

        # Right: negative constraint -> clean
        right_bg = Rectangle(width=5.5, height=4.2)
        right_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        right_bg.to_edge(RIGHT, buff=0.8)

        right_h = Text("with constraint", font=DISPLAY, color=TEAL,
                       font_size=20, weight="MEDIUM")
        right_h.next_to(right_bg.get_top() + DOWN * 0.45, ORIGIN)

        right_l1 = Text("negative constraint:", font=SERIF, color=INK, font_size=19)
        right_l2 = Text("no JS, no CDN fonts", font=SERIF, color=TEAL, font_size=19)
        right_l3 = Text("clean page: first attempt", font=SERIF, color=TEAL, font_size=19)
        right_items = VGroup(right_l1, right_l2, right_l3)
        right_items.arrange(DOWN, center=True, buff=0.4)
        right_items.move_to(right_bg.get_center() + DOWN * 0.1)

        saved_badge = LabelChip("38 min saved", accent=TEAL, size=18)
        saved_badge.next_to(right_bg, DOWN, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(left_h), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in left_items],
                              lag_ratio=0.25, run_time=0.9))
        self.play(FadeIn(cost_badge), run_time=0.4)
        self.play(FadeIn(right_bg), FadeIn(right_h), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in right_items],
                              lag_ratio=0.25, run_time=0.9))
        self.play(FadeIn(saved_badge), run_time=0.4)
        self.wait(7.0)


class B10_PracticalCard(Scene):
    def construct(self):
        title = Text("the five-element format", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        elements = [
            "Operation — the specific file and action",
            "Invariants — what must not change",
            "Context — the CLAUDE.md rules",
            "Output format — what done looks like",
            "Negative constraint — what must not happen",
        ]
        rows = VGroup()
        for elem in elements:
            row_bg = Rectangle(width=11.0, height=1.0)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.0)
            row_text = Text(elem, font=SERIF, color=INK, font_size=22)
            row_text.move_to(row_bg.get_center())
            rows.add(VGroup(row_bg, row_text))

        rows.arrange(DOWN, buff=0.2)
        rows.move_to(ORIGIN + UP * 0.2)
        rows.scale_to_fit_width(13.0)

        time_note = SerifLabel("first time: 3-5 min  tenth time: 90 sec", accent=SLATE, size=20)
        time_note.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(time_note), run_time=0.5)
        self.wait(7.5)


class B11_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("The decisions happen either way.", font=SERIF, color=INK, font_size=40)
        m2 = Text("The spec makes them yours.", font=SERIF, color=TEAL, font_size=40)
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
