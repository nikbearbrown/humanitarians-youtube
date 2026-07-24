"""vox_scenes.py — vox-handoff-conditions
Why 'Looks Good' Fails as a Gate and What to Write Instead.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B06) gets no scene — compiles as slate.
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
        t1 = Text("Why 'looks good' fails as a gate", font=SERIF,
                  color=INK, font_size=42)
        t2 = Text("and what to write instead", font=SERIF,
                  color=TEAL, font_size=42)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(7.4)


class B02_LinkFailure(Scene):
    def construct(self):
        title = Text("same link — two environments", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Left: local dev passes
        left_bg = Rectangle(width=5.5, height=4.5)
        left_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        left_bg.to_edge(LEFT, buff=0.8)

        left_h = Text("local dev", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        left_h.next_to(left_bg.get_top() + DOWN * 0.45, ORIGIN)

        left_link = Text("syllabus.html", font=MONO, color=INK, font_size=22)
        left_link.move_to(left_bg.get_center() + UP * 0.3)
        left_pass = Text("link resolves", font=SERIF, color=TEAL, font_size=22)
        left_pass.move_to(left_bg.get_center() + DOWN * 0.3)

        # Right: school server fails
        right_bg = Rectangle(width=5.5, height=4.5)
        right_bg.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        right_bg.to_edge(RIGHT, buff=0.8)

        right_h = Text("school server", font=DISPLAY, color=CRIMSON,
                       font_size=22, weight="MEDIUM")
        right_h.next_to(right_bg.get_top() + DOWN * 0.45, ORIGIN)

        right_link = Text("syllabus.html", font=MONO, color=INK, font_size=22)
        right_link.move_to(right_bg.get_center() + UP * 0.3)
        right_fail = Text("404 not found", font=SERIF, color=CRIMSON, font_size=22)
        right_fail.move_to(right_bg.get_center() + DOWN * 0.3)

        note = SerifLabel("page-relative path: works on local, fails on server", accent=SLATE, size=18)
        note.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(left_h), run_time=0.5)
        self.play(FadeIn(left_link), FadeIn(left_pass), run_time=0.4)
        self.play(FadeIn(right_bg), FadeIn(right_h), run_time=0.5)
        self.play(FadeIn(right_link), FadeIn(right_fail), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(8.2)


class B03_Question(Scene):
    def construct(self):
        l1 = Text("Exit 0.", font=SERIF, color=INK, font_size=42)
        l2 = Text("Looks good.", font=SERIF, color=INK, font_size=42)
        l3 = Text("Link broken three days later.", font=SERIF, color=CRIMSON, font_size=36)
        l4 = Text("Why?", font=SERIF, color=INK, font_size=42)
        question = VGroup(l1, l2, l3, l4).arrange(DOWN, center=True, buff=0.25)
        question.scale_to_fit_width(11.0)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.15,
                    question.get_corner(DR) + DOWN * 0.15,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(l1), run_time=0.4)
        self.play(FadeIn(l2), run_time=0.4)
        self.play(FadeIn(l3), run_time=0.4)
        self.play(FadeIn(l4), Create(rule), run_time=0.5)
        self.wait(7.3)


class B04_ThreeProperties(Scene):
    def construct(self):
        title = Text("a handoff condition has three properties", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        properties = ["Specific", "Testable", "Binary"]
        teal_rows = VGroup()
        crimson_xs = VGroup()

        for prop in properties:
            row_bg = Rectangle(width=5.5, height=1.2)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.2)
            row_text = Text(prop, font=DISPLAY, color=TEAL,
                            font_size=22, weight="MEDIUM")
            row_text.move_to(row_bg.get_center())
            teal_rows.add(VGroup(row_bg, row_text))

        teal_rows.arrange(DOWN, buff=0.3)
        teal_rows.move_to(LEFT * 2.5 + UP * 0.2)

        # Looks good column
        looks_good_h = Text("looks good", font=DISPLAY, color=CRIMSON,
                            font_size=22, weight="MEDIUM")
        looks_good_h.move_to(RIGHT * 2.5 + UP * 2.0)

        for i, row in enumerate(teal_rows):
            x_bg = Rectangle(width=3.0, height=1.2)
            x_bg.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.2)
            x_text = Text("fails", font=SERIF, color=CRIMSON, font_size=22)
            x_group = VGroup(x_bg, x_text)
            x_group.move_to(RIGHT * 2.5 + row.get_center()[1] * UP)
            x_text.move_to(x_bg.get_center())
            crimson_xs.add(x_group)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(looks_good_h), run_time=0.4)
        for row, x in zip(teal_rows, crimson_xs):
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.4)
            self.play(FadeIn(x, shift=LEFT * 0.1), run_time=0.4)
        self.wait(8.0)


class B05_WeakVsStrong(Scene):
    def construct(self):
        title = Text("weak condition vs strong condition", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.65)

        col1_h = Text("Weak", font=DISPLAY, color=CRIMSON,
                      font_size=22, weight="MEDIUM")
        col2_h = Text("Strong", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        col1_h.move_to(LEFT * 3.5 + UP * 1.8)
        col2_h.move_to(RIGHT * 2.8 + UP * 1.8)

        header_rule = Line(LEFT * 6.5 + UP * 1.35, RIGHT * 6.5 + UP * 1.35,
                           stroke_width=1.0, color=SLATE)

        weak_items = VGroup(
            Text("looks good", font=SERIF, color=CRIMSON, font_size=20),
            Text("renders", font=SERIF, color=CRIMSON, font_size=20),
            Text("no errors", font=SERIF, color=CRIMSON, font_size=20),
        )
        strong_items = VGroup(
            Text("renders at 375px, no h-scroll", font=SERIF, color=TEAL, font_size=20),
            Text("every link 200s on deployment", font=SERIF, color=TEAL, font_size=20),
            Text("change only in expected files", font=SERIF, color=TEAL, font_size=20),
        )

        weak_items.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        strong_items.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        weak_items.move_to(LEFT * 3.5 + UP * 0.2)
        strong_items.move_to(RIGHT * 2.5 + UP * 0.2)

        # Bug label at bottom
        bug_label = SerifLabel("bug slips through", accent=CRIMSON, size=20)
        bug_label.next_to(weak_items, DOWN, buff=0.4)
        blocked_label = SerifLabel("bug blocked", accent=TEAL, size=20)
        blocked_label.next_to(strong_items, DOWN, buff=0.4)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(col1_h), FadeIn(col2_h), Create(header_rule), run_time=0.5)
        for w, s in zip(weak_items, strong_items):
            self.play(FadeIn(w), FadeIn(s), run_time=0.4)
        self.play(FadeIn(bug_label), FadeIn(blocked_label), run_time=0.5)
        self.wait(8.1)


class B07_ContextPollution(Scene):
    def construct(self):
        title = Text("forward correction compounds", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Context bar filling with segments
        segments = [
            ("failed step", CRIMSON, 0.8),
            ("correction 1", CRIMSON, 0.7),
            ("correction 2", CRIMSON, 0.6),
            ("next prompt ?", SLATE, 0.5),
        ]
        bars = VGroup()
        labels = VGroup()
        x_pos = -5.5
        for seg_label, col, opacity in segments:
            w = 2.5
            bar = Rectangle(width=w, height=1.2)
            bar.set_fill(col, opacity).set_stroke(col, 0)
            bar.move_to(np.array([x_pos + w / 2, 0.3, 0]))
            label = Text(seg_label, font=SERIF, color=INK, font_size=18)
            label.move_to(bar.get_center())
            bars.add(bar)
            labels.add(label)
            x_pos += w + 0.1

        arrow_label = SerifLabel("next prompt runs against failure history", accent=CRIMSON, size=20)
        arrow_label.to_edge(DOWN, buff=0.8)

        two_fails = SerifLabel("two failures on same step: /clear and start over", accent=SLATE, size=20)
        two_fails.next_to(arrow_label, UP, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        for bar, label in zip(bars, labels):
            self.play(FadeIn(bar), FadeIn(label), run_time=0.4)
        self.play(FadeIn(arrow_label), run_time=0.4)
        self.play(FadeIn(two_fails), run_time=0.4)
        self.wait(8.8)


class B08_RevertRespecify(Scene):
    def construct(self):
        title = Text("revert and respecify", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Step 1: /rewind
        left_bg = Rectangle(width=5.5, height=4.5)
        left_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        left_bg.to_edge(LEFT, buff=0.8)

        left_h = Text("/rewind", font=MONO, color=TEAL, font_size=26)
        left_h.next_to(left_bg.get_top() + DOWN * 0.5, ORIGIN)

        left_l1 = Text("failed step removed", font=SERIF, color=INK, font_size=20)
        left_l2 = Text("from context", font=SERIF, color=INK, font_size=20)
        left_l3 = Text("from file system", font=SERIF, color=TEAL, font_size=20)
        left_items = VGroup(left_l1, left_l2, left_l3)
        left_items.arrange(DOWN, center=True, buff=0.35)
        left_items.move_to(left_bg.get_center() + DOWN * 0.15)

        # Arrow
        arrow = Arrow(left_bg.get_right() + RIGHT * 0.1,
                      left_bg.get_right() + RIGHT * 1.3,
                      stroke_width=3, color=INK, buff=0.0)

        # Step 2: respecify
        right_bg = Rectangle(width=5.5, height=4.5)
        right_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        right_bg.to_edge(RIGHT, buff=0.8)

        right_h = Text("respecify", font=DISPLAY, color=TEAL,
                       font_size=22, weight="MEDIUM")
        right_h.next_to(right_bg.get_top() + DOWN * 0.5, ORIGIN)

        right_l1 = Text("add failure as", font=SERIF, color=INK, font_size=20)
        right_l2 = Text("negative constraint", font=SERIF, color=INK, font_size=20)
        right_l3 = Text("run from clean state", font=SERIF, color=TEAL, font_size=20)
        right_items = VGroup(right_l1, right_l2, right_l3)
        right_items.arrange(DOWN, center=True, buff=0.35)
        right_items.move_to(right_bg.get_center() + DOWN * 0.15)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(left_h), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in left_items],
                              lag_ratio=0.2, run_time=0.8))
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(right_bg), FadeIn(right_h), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in right_items],
                              lag_ratio=0.2, run_time=0.8))
        self.wait(7.9)


class B09_PracticalCard(Scene):
    def construct(self):
        title = Text("before any build step", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        rows_data = [
            "Write the condition before approving",
            "Condition fails: /rewind + respecify",
            "Two failures: /clear + start fresh",
        ]
        rows = VGroup()
        for text in rows_data:
            row_bg = Rectangle(width=11.0, height=1.2)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.2)
            row_text = Text(text, font=SERIF, color=INK, font_size=22)
            row_text.move_to(row_bg.get_center())
            rows.add(VGroup(row_bg, row_text))

        rows.arrange(DOWN, buff=0.4)
        rows.move_to(ORIGIN + DOWN * 0.2)
        rows.scale_to_fit_width(13.0)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.5)
        self.wait(8.0)


class B10_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Not 'looks good.'", font=SERIF, color=CRIMSON, font_size=40)
        m2 = Text("Specific. Testable. Binary.", font=SERIF, color=TEAL, font_size=40)
        m3 = Text("Written before the step.", font=SERIF, color=INK, font_size=36)
        main_text = VGroup(m1, m2, m3).arrange(DOWN, center=True, buff=0.3)
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
