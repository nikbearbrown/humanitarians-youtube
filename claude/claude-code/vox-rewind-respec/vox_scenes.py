"""vox_scenes.py — vox-rewind-respec
Why Rewriting the Wrong Fix Makes the Build Worse, Not Better.
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
        t1 = Text("Why rewriting the wrong fix", font=SERIF, color=INK, font_size=40)
        t2 = Text("makes the build worse, not better", font=SERIF, color=CRIMSON, font_size=40)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(8.4)


class B02_ForwardFails(Scene):
    def construct(self):
        title = Text("the session log grows — two failures", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        log_entries = [
            ("Step: add About page", "[PASS]", TEAL),
            ("Handoff: link 404s on school server", "[FAIL]", CRIMSON),
            ("Fix request: fix the broken link", "", INK),
            ("Claude output: ./syllabus.html", "", INK),
            ("Handoff: link 404s again", "[FAIL]", CRIMSON),
        ]

        log_group = VGroup()
        for label, badge, col in log_entries:
            row = VGroup()
            text = Text(label, font=MONO, color=col, font_size=18)
            row.add(text)
            if badge:
                badge_text = Text(badge, font=DISPLAY, color=col,
                                  font_size=18, weight="MEDIUM")
                badge_text.next_to(text, RIGHT, buff=0.3)
                row.add(badge_text)
            log_group.add(row)

        log_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        log_group.move_to(ORIGIN + LEFT * 1.5 + DOWN * 0.2)

        # Context bar on the right
        bar_outline = Rectangle(width=1.2, height=4.0)
        bar_outline.set_fill(GROUND, 0).set_stroke(SLATE, 1.5)
        bar_outline.move_to(np.array([5.5, -0.2, 0]))
        ctx_label = Text("context", font=SERIF, color=SLATE, font_size=16)
        ctx_label.next_to(bar_outline, UP, buff=0.1)

        # Context fills crimson with each failure
        ctx_fill_1 = Rectangle(width=1.2, height=1.2)
        ctx_fill_1.set_fill(CRIMSON, 0.7).set_stroke(CRIMSON, 0)
        ctx_fill_1.move_to(bar_outline.get_bottom() + UP * 0.6)
        ctx_fill_2 = Rectangle(width=1.2, height=1.2)
        ctx_fill_2.set_fill(CRIMSON, 0.7).set_stroke(CRIMSON, 0)
        ctx_fill_2.next_to(ctx_fill_1, UP, buff=0)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(bar_outline), FadeIn(ctx_label), run_time=0.4)
        for i, row in enumerate(log_group):
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.35)
            if i == 1:
                self.play(FadeIn(ctx_fill_1), run_time=0.3)
            elif i == 4:
                self.play(FadeIn(ctx_fill_2), run_time=0.3)
        self.wait(7.5)


class B03_Question(Scene):
    def construct(self):
        l1 = Text("Two fixes.", font=SERIF, color=INK, font_size=46)
        l2 = Text("Worse than the original failure.", font=SERIF, color=CRIMSON, font_size=46)
        l3 = Text("Why?", font=SERIF, color=INK, font_size=46)
        question = VGroup(l1, l2, l3).arrange(DOWN, center=True, buff=0.3)
        question.scale_to_fit_width(11.5)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.2,
                    question.get_corner(DR) + DOWN * 0.2,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(l1), run_time=0.5)
        self.play(FadeIn(l2), run_time=0.5)
        self.play(FadeIn(l3), Create(rule), run_time=0.6)
        self.wait(7.4)


class B04_ContextPollution(Scene):
    def construct(self):
        title = Text("failure history treated as constraint", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Context bar
        bar_w = 2.0
        bar_h = 4.5
        bar_x = -4.0
        outline = Rectangle(width=bar_w, height=bar_h)
        outline.set_fill(GROUND, 0).set_stroke(SLATE, 1.5)
        outline.move_to(np.array([bar_x, -0.3, 0]))

        # Original spec (teal, small, at bottom)
        spec_h = bar_h * 0.20
        spec_block = Rectangle(width=bar_w, height=spec_h)
        spec_block.set_fill(TEAL, 0.75).set_stroke(TEAL, 0)
        spec_block.move_to(outline.get_bottom() + UP * (spec_h / 2))
        spec_lbl = Text("original spec", font=MONO, color=INK, font_size=13)
        spec_lbl.move_to(spec_block.get_center())

        # Failure blocks (crimson, stacking up)
        failure_entries = [
            "original failure",
            "failed fix 1",
            "failed fix 2",
        ]
        fail_h = bar_h * 0.25
        fail_blocks = []
        current = spec_block.get_top()
        for label in failure_entries:
            fb = Rectangle(width=bar_w, height=fail_h)
            fb.set_fill(CRIMSON, 0.72).set_stroke(CRIMSON, 0)
            fb.move_to(current + UP * (fail_h / 2))
            fl = Text(label, font=MONO, color=INK, font_size=12)
            fl.move_to(fb.get_center())
            fail_blocks.append((fb, fl))
            current = fb.get_top()

        # Right annotation
        annotation_lines = [
            "Claude reasons against",
            "the entire failure history.",
            "The clean solution",
            "was never tried.",
        ]
        ann_group = VGroup(*[Text(l, font=SERIF, color=INK, font_size=19)
                              for l in annotation_lines])
        ann_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ann_group.move_to(np.array([2.8, 0.0, 0]))

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(outline), FadeIn(spec_block), FadeIn(spec_lbl), run_time=0.5)
        self.play(FadeIn(ann_group[0]), FadeIn(ann_group[1]), run_time=0.4)
        for i, (fb, fl) in enumerate(fail_blocks):
            self.play(FadeIn(fb), FadeIn(fl), run_time=0.4)
        self.play(FadeIn(ann_group[2]), FadeIn(ann_group[3]), run_time=0.4)
        self.wait(8.5)


class B05_RewindClean(Scene):
    def construct(self):
        title = Text("/rewind restores conversation + file system", font=SERIF,
                     color=INK, font_size=24)
        title.to_edge(UP, buff=0.7)

        # Left box: polluted (crimson)
        left_box = Rectangle(width=4.8, height=3.5)
        left_box.set_fill(GROUND, 0).set_stroke(CRIMSON, 2.0)
        left_box.move_to(np.array([-3.5, -0.3, 0]))
        left_title = Text("before /rewind", font=DISPLAY,
                          color=CRIMSON, font_size=18, weight="MEDIUM")
        left_title.next_to(left_box, UP, buff=0.15)

        left_items = VGroup(
            Text("original failure", font=MONO, color=CRIMSON, font_size=15),
            Text("failed fix 1", font=MONO, color=CRIMSON, font_size=15),
            Text("failed fix 2", font=MONO, color=CRIMSON, font_size=15),
            Text("context polluted", font=SERIF, color=CRIMSON, font_size=15),
        )
        left_items.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        left_items.move_to(left_box.get_center())

        # Right box: clean (teal)
        right_box = Rectangle(width=4.8, height=3.5)
        right_box.set_fill(GROUND, 0).set_stroke(TEAL, 2.0)
        right_box.move_to(np.array([3.5, -0.3, 0]))
        right_title = Text("after /rewind", font=DISPLAY,
                           color=TEAL, font_size=18, weight="MEDIUM")
        right_title.next_to(right_box, UP, buff=0.15)

        right_items = VGroup(
            Text("checkpoint restored", font=MONO, color=TEAL, font_size=15),
            Text("files restored", font=MONO, color=TEAL, font_size=15),
            Text("failures gone", font=SERIF, color=TEAL, font_size=15),
        )
        right_items.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        right_items.move_to(right_box.get_center())

        # Arrow
        rewind_arrow = Arrow(left_box.get_right(), right_box.get_left(),
                             buff=0.1, stroke_width=2.5, color=TEAL,
                             tip_length=0.22)
        rewind_label = Text("/rewind", font=MONO, color=TEAL, font_size=20)
        rewind_label.next_to(rewind_arrow, UP, buff=0.12)

        footer = Text("conversation + file system both restored to checkpoint",
                      font=SERIF, color=SLATE, font_size=18)
        footer.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(left_box), FadeIn(left_title), run_time=0.4)
        self.play(FadeIn(left_items), run_time=0.5)
        self.play(Create(rewind_arrow), FadeIn(rewind_label), run_time=0.5)
        self.play(Create(right_box), FadeIn(right_title), run_time=0.4)
        self.play(FadeIn(right_items), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(8.5)


class B07_TwoFailureRule(Scene):
    def construct(self):
        title = Text("the two-failure rule", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Decision tree nodes
        start = Text("handoff fails", font=SERIF, color=CRIMSON, font_size=20)
        start.move_to(np.array([-4.5, 1.2, 0]))

        fix1 = Text("first correction", font=SERIF, color=INK, font_size=18)
        fix1.move_to(np.array([-1.5, 1.2, 0]))

        success_node = Text("success -> proceed", font=SERIF, color=TEAL, font_size=18)
        success_node.move_to(np.array([-1.5, -0.3, 0]))

        fail2 = Text("fails again", font=SERIF, color=CRIMSON, font_size=18)
        fail2.move_to(np.array([1.5, 1.2, 0]))

        fix2 = Text("second correction", font=SERIF, color=INK, font_size=18)
        fix2.move_to(np.array([4.0, 1.2, 0]))

        clear_node = Text("/clear + rewrite spec", font=MONO, color=TEAL, font_size=18)
        clear_node.move_to(np.array([4.0, -0.3, 0]))

        two_fail_label = SerifLabel("two failures: start fresh", accent=CRIMSON, size=18)
        two_fail_label.to_edge(DOWN, buff=0.7)

        # Arrows
        arrow1 = Arrow(start.get_right(), fix1.get_left(),
                       buff=0.1, stroke_width=2.0, color=INK, tip_length=0.18)
        arrow_success = Arrow(fix1.get_bottom(), success_node.get_top(),
                              buff=0.1, stroke_width=2.0, color=TEAL, tip_length=0.18)
        arrow_fail2 = Arrow(fix1.get_right(), fail2.get_left(),
                            buff=0.1, stroke_width=2.0, color=CRIMSON, tip_length=0.18)
        arrow3 = Arrow(fail2.get_right(), fix2.get_left(),
                       buff=0.1, stroke_width=2.0, color=INK, tip_length=0.18)
        arrow_clear = Arrow(fix2.get_bottom(), clear_node.get_top(),
                            buff=0.1, stroke_width=2.0, color=TEAL, tip_length=0.18)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(start), run_time=0.4)
        self.play(Create(arrow1), FadeIn(fix1), run_time=0.4)
        self.play(Create(arrow_success), FadeIn(success_node), run_time=0.4)
        self.play(Create(arrow_fail2), FadeIn(fail2), run_time=0.4)
        self.play(Create(arrow3), FadeIn(fix2), run_time=0.4)
        self.play(Create(arrow_clear), FadeIn(clear_node), run_time=0.4)
        self.play(FadeIn(two_fail_label), run_time=0.4)
        self.wait(8.0)


class B08_CostComparison(Scene):
    def construct(self):
        title = Text("the cost of forward correction vs. /rewind", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Two horizontal time bars
        # Left: forward correction grows to 90 min
        left_y = 0.8
        right_y = -1.0

        # Forward correction bar
        fc_label = Text("forward correction", font=DISPLAY,
                        color=CRIMSON, font_size=18, weight="MEDIUM")
        fc_label.move_to(np.array([-3.5, left_y + 0.6, 0]))

        fc_base = Rectangle(width=2.0, height=0.6)
        fc_base.set_fill(TEAL, 0.6).set_stroke(TEAL, 0)
        fc_base.move_to(np.array([-5.0, left_y, 0]))
        fc_base_lbl = Text("15 min", font=MONO, color=INK, font_size=14)
        fc_base_lbl.move_to(fc_base.get_center())

        fc_extra = Rectangle(width=7.5, height=0.6)
        fc_extra.set_fill(CRIMSON, 0.72).set_stroke(CRIMSON, 0)
        fc_extra.next_to(fc_base, RIGHT, buff=0)
        fc_extra_lbl = Text("+75 min of compounding failures", font=MONO,
                            color=INK, font_size=14)
        fc_extra_lbl.move_to(fc_extra.get_center())

        fc_total = Text("90 min total", font=SERIF, color=CRIMSON, font_size=18)
        fc_total.next_to(fc_extra, RIGHT, buff=0.2)

        # /rewind + respec bar
        rw_label = Text("/rewind + respec", font=DISPLAY,
                        color=TEAL, font_size=18, weight="MEDIUM")
        rw_label.move_to(np.array([-3.5, right_y + 0.6, 0]))

        rw_bar = Rectangle(width=2.0, height=0.6)
        rw_bar.set_fill(TEAL, 0.75).set_stroke(TEAL, 0)
        rw_bar.move_to(np.array([-5.0, right_y, 0]))
        rw_bar_lbl = Text("15 min", font=MONO, color=INK, font_size=14)
        rw_bar_lbl.move_to(rw_bar.get_center())

        rw_note = Text("clean state, one constraint added", font=SERIF,
                       color=TEAL, font_size=18)
        rw_note.next_to(rw_bar, RIGHT, buff=0.4)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(fc_label), FadeIn(rw_label), run_time=0.4)
        self.play(FadeIn(fc_base), FadeIn(fc_base_lbl), run_time=0.4)
        self.play(FadeIn(fc_extra), FadeIn(fc_extra_lbl),
                  FadeIn(fc_total), run_time=0.6)
        self.play(FadeIn(rw_bar), FadeIn(rw_bar_lbl), run_time=0.4)
        self.play(FadeIn(rw_note), run_time=0.4)
        self.wait(8.0)


class B09_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Handoff catches it.", font=SERIF, color=TEAL, font_size=40)
        m2 = Text("/rewind removes it.", font=SERIF, color=INK, font_size=40)
        m3 = Text("Respec carries it forward.", font=SERIF, color=TEAL, font_size=40)
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
