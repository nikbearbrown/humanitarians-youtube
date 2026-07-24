"""vox_scenes.py — vox-ai-feedback-bias
Why AI Feedback That Passes Every Check Can Still Harm Your Students.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B04) gets no scene — compiles as slate.
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
        t1 = Text("Why AI feedback that passes", font=SERIF, color=INK, font_size=42)
        t2 = Text("every check can still harm your students", font=SERIF, color=INK, font_size=42)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.2)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(7.4)


class B02_MarcusReport(Scene):
    def construct(self):
        title = Text("Marcus — accurate flags", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        card = Rectangle(width=9.0, height=4.8)
        card.set_fill(TEAL, 0.05).set_stroke(TEAL, 1.5)
        card.move_to(ORIGIN + DOWN * 0.15)

        flags = [
            "thesis present but unfocused",
            "evidence not tied to claim",
            "conclusion restates introduction",
        ]
        items = VGroup()
        for flag in flags:
            row = VGroup(
                Text("✓", font=SERIF, color=TEAL, font_size=26),
                Text(flag, font=SERIF, color=INK, font_size=24),
            )
            row.arrange(RIGHT, buff=0.35)
            items.add(row)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        items.move_to(card.get_center())

        useful_label = SerifLabel("useful", accent=TEAL, size=22)
        useful_label.next_to(card, DOWN, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(card), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(row, shift=RIGHT * 0.15) for row in items],
                              lag_ratio=0.25, run_time=1.0))
        self.play(FadeIn(useful_label), run_time=0.4)
        self.wait(8.6)


class B03_SaraReport(Scene):
    def construct(self):
        title = Text("Sara — technically correct, pedagogically harmful", font=SERIF,
                     color=INK, font_size=24)
        title.to_edge(UP, buff=0.7)
        title.scale_to_fit_width(13.0)

        # Left: what the rubric sees
        left_bg = Rectangle(width=5.5, height=4.5)
        left_bg.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        left_bg.to_edge(LEFT, buff=0.8)

        left_header = Text("rubric sees", font=DISPLAY, color=CRIMSON,
                           font_size=20, weight="MEDIUM")
        left_header.next_to(left_bg.get_top() + DOWN * 0.4, ORIGIN)

        rubric_lines = VGroup(
            Text("multiple grammar errors", font=SERIF, color=INK, font_size=20),
            Text("(preposition use)", font=SERIF, color=INK, font_size=20),
        )
        rubric_lines.arrange(DOWN, center=True, buff=0.25)
        rubric_lines.move_to(left_bg.get_center() + UP * 0.3)

        recommendation = Text("grammar review first", font=SERIF,
                              color=CRIMSON, font_size=22)
        recommendation.next_to(rubric_lines, DOWN, buff=0.45)

        # Right: what's actually there
        right_bg = Rectangle(width=5.5, height=4.5)
        right_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        right_bg.to_edge(RIGHT, buff=0.8)

        right_header = Text("actual work", font=DISPLAY, color=TEAL,
                            font_size=20, weight="MEDIUM")
        right_header.next_to(right_bg.get_top() + DOWN * 0.4, ORIGIN)

        actual_lines = VGroup(
            Text("strong arguments", font=SERIF, color=TEAL, font_size=22),
            Text("idiomatic for her background", font=SERIF, color=INK, font_size=20),
        )
        actual_lines.arrange(DOWN, center=True, buff=0.3)
        actual_lines.move_to(right_bg.get_center())

        harm_label = SerifLabel("buried", accent=CRIMSON, size=20)
        harm_label.next_to(left_bg, DOWN, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.4)
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.4)
        self.play(FadeIn(rubric_lines), FadeIn(actual_lines), run_time=0.6)
        self.play(FadeIn(recommendation), run_time=0.5)
        self.play(FadeIn(harm_label), run_time=0.4)
        self.wait(8.2)


class B05_Question(Scene):
    def construct(self):
        line1 = Text("0.93 accuracy.", font=SERIF, color=INK, font_size=42)
        line2 = Text("25% underperformance for some students.", font=SERIF,
                     color=CRIMSON, font_size=36)
        line3 = Text("How?", font=SERIF, color=INK, font_size=42)
        question = VGroup(line1, line2, line3).arrange(DOWN, center=True, buff=0.3)
        question.scale_to_fit_width(11.5)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.15,
                    question.get_corner(DR) + DOWN * 0.15,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(line1), run_time=0.6)
        self.play(FadeIn(line2), run_time=0.6)
        self.play(FadeIn(line3), Create(rule), run_time=0.6)
        self.wait(7.2)


class B06_AccuracyDistribution(Scene):
    def construct(self):
        title = Text("the accuracy number is real — so is the gap", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Horizontal bar: teal (86-93%) + crimson (7-14%)
        bar_width = 11.0
        bar_height = 1.2
        teal_w = bar_width * 0.895  # midpoint ~89.5%
        crimson_w = bar_width - teal_w

        teal_bar = Rectangle(width=teal_w, height=bar_height)
        teal_bar.set_fill(TEAL, 0.8).set_stroke(TEAL, 0)
        crimson_bar = Rectangle(width=crimson_w, height=bar_height)
        crimson_bar.set_fill(CRIMSON, 0.8).set_stroke(CRIMSON, 0)

        bar_group = VGroup(teal_bar, crimson_bar).arrange(RIGHT, buff=0)
        bar_group.move_to(ORIGIN + UP * 0.3)

        teal_label = Text("86-93% agreement zone", font=DISPLAY, color=INK,
                          font_size=20, weight="MEDIUM")
        teal_label.move_to(teal_bar.get_center())

        crimson_label_t = Text("7-14%", font=DISPLAY, color=INK,
                               font_size=18, weight="MEDIUM")
        crimson_label_t.move_to(crimson_bar.get_center() + UP * 0.1)

        not_random = SerifLabel("not random", accent=CRIMSON, size=20)
        not_random.next_to(crimson_bar, DOWN, buff=0.35)

        sub_label = SerifLabel("2024–2025 studies: 0.86–0.93 correlation with human raters",
                               accent=SLATE, size=18)
        sub_label.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(teal_bar), run_time=0.8)
        self.play(FadeIn(teal_label), run_time=0.4)
        self.play(FadeIn(crimson_bar), run_time=0.5)
        self.play(FadeIn(crimson_label_t), run_time=0.3)
        self.play(FadeIn(not_random), run_time=0.4)
        self.play(FadeIn(sub_label), run_time=0.4)
        self.wait(9.6)


class B07_BiasInTail(Scene):
    def construct(self):
        title = Text("the bias lives in the tail", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        bar_width = 11.0
        bar_height = 1.1
        teal_w = bar_width * 0.895
        crimson_w = bar_width - teal_w

        teal_bar = Rectangle(width=teal_w, height=bar_height)
        teal_bar.set_fill(TEAL, 0.7).set_stroke(TEAL, 0)
        crimson_bar = Rectangle(width=crimson_w, height=bar_height)
        crimson_bar.set_fill(CRIMSON, 0.8).set_stroke(CRIMSON, 0)

        bar_group = VGroup(teal_bar, crimson_bar).arrange(RIGHT, buff=0)
        bar_group.move_to(ORIGIN + UP * 1.0)

        teal_label = Text("agreement zone", font=DISPLAY, color=INK,
                          font_size=18, weight="MEDIUM")
        teal_label.move_to(teal_bar.get_center())

        # Student names in crimson zone
        sara_chip = LabelChip("Sara (ESL)  -10.3%", accent=CRIMSON, size=18)
        sara_chip.next_to(crimson_bar, DOWN, buff=0.5)

        jaden_chip = LabelChip("Jaden (AAVE)  -25%", accent=CRIMSON, size=18)
        jaden_chip.next_to(sara_chip, DOWN, buff=0.3)

        judgment_label = SerifLabel("where teacher judgment matters most", accent=SLATE, size=20)
        judgment_label.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(teal_bar), FadeIn(teal_label), run_time=0.5)
        self.play(FadeIn(crimson_bar), run_time=0.4)
        self.play(FadeIn(sara_chip), run_time=0.5)
        self.play(FadeIn(jaden_chip), run_time=0.5)
        self.play(FadeIn(judgment_label), run_time=0.4)
        self.wait(8.2)


class B08_PassedAllChecks(Scene):
    def construct(self):
        title = Text("the dangerous middle", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Three gates
        gate_labels = ["Hook check", "CLAUDE.md check", "handoff condition"]
        gates = VGroup()
        for label in gate_labels:
            bg = Rectangle(width=3.2, height=1.4)
            bg.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
            row = VGroup(
                Text("PASSED", font=DISPLAY, color=TEAL, font_size=20, weight="MEDIUM"),
                Text(label, font=SERIF, color=INK, font_size=20),
            )
            row.arrange(DOWN, center=True, buff=0.15)
            row.move_to(bg.get_center())
            gates.add(VGroup(bg, row))

        gates.arrange(RIGHT, buff=0.5)
        gates.move_to(ORIGIN + UP * 0.6)

        harmful_label = SerifLabel("pedagogically harmful", accent=CRIMSON, size=24)
        harmful_label.next_to(gates, DOWN, buff=0.5)

        # Arrow pointing back up
        arrow = Arrow(harmful_label.get_top() + UP * 0.1,
                      gates.get_bottom() + DOWN * 0.1,
                      stroke_width=2.5, color=CRIMSON, buff=0.05)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(g, shift=UP * 0.15) for g in gates],
                              lag_ratio=0.2, run_time=1.0))
        self.play(FadeIn(harmful_label), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.6)
        self.wait(7.9)


class B09_NarrowingPrinciple(Scene):
    def construct(self):
        title = Text("the narrowing principle", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Left: Claude column
        left_bg = Rectangle(width=5.5, height=4.5)
        left_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        left_bg.to_edge(LEFT, buff=0.8)

        left_header = Text("Claude", font=DISPLAY, color=TEAL,
                           font_size=22, weight="MEDIUM")
        left_header.next_to(left_bg.get_top() + DOWN * 0.45, ORIGIN)

        left_l1 = Text("reads all submissions", font=SERIF, color=INK, font_size=20)
        left_l2 = Text("detects cohort patterns", font=SERIF, color=INK, font_size=20)
        left_l3 = Text("per-student flags only", font=SERIF, color=TEAL, font_size=20)
        left_items = VGroup(left_l1, left_l2, left_l3).arrange(DOWN, center=True, buff=0.35)
        left_items.move_to(left_bg.get_center() + DOWN * 0.1)

        # Arrow
        arrow = Arrow(left_bg.get_right() + RIGHT * 0.05,
                      left_bg.get_right() + RIGHT * 1.35,
                      stroke_width=3, color=INK, buff=0.0)

        # Right: Teacher column
        right_bg = Rectangle(width=5.5, height=4.5)
        right_bg.set_fill(SLATE, 0.06).set_stroke(SLATE, 1.5)
        right_bg.to_edge(RIGHT, buff=0.8)

        right_header = Text("Teacher", font=DISPLAY, color=INK,
                            font_size=22, weight="MEDIUM")
        right_header.next_to(right_bg.get_top() + DOWN * 0.45, ORIGIN)

        right_l1 = Text("reads flags", font=SERIF, color=INK, font_size=20)
        right_l2 = Text("knows the student", font=SERIF, color=INK, font_size=20)
        right_l3 = Text("writes the feedback", font=SERIF, color=INK, font_size=20)
        right_items = VGroup(right_l1, right_l2, right_l3).arrange(DOWN, center=True, buff=0.35)
        right_items.move_to(right_bg.get_center() + DOWN * 0.1)

        interpretation = SerifLabel("interpretation stays human", accent=SLATE, size=20)
        interpretation.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(left_header), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in left_items],
                              lag_ratio=0.2, run_time=0.8))
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(right_bg), FadeIn(right_header), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in right_items],
                              lag_ratio=0.2, run_time=0.8))
        self.play(FadeIn(interpretation), run_time=0.4)
        self.wait(8.0)


class B10_KeishaExample(Scene):
    def construct(self):
        title = Text("neutral flag — teacher writes", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Left: neutral flag card
        left_bg = Rectangle(width=5.6, height=4.6)
        left_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        left_bg.to_edge(LEFT, buff=0.8)

        left_header = Text("Claude's flag", font=DISPLAY, color=TEAL,
                           font_size=20, weight="MEDIUM")
        left_header.next_to(left_bg.get_top() + DOWN * 0.45, ORIGIN)

        flag_lines = VGroup(
            Text("thesis: present", font=SERIF, color=INK, font_size=19),
            Text("argument strongest: ¶2–4", font=SERIF, color=TEAL, font_size=19),
            Text("three surface divergences", font=SERIF, color=INK, font_size=19),
            Text("from SAE (listed)", font=SERIF, color=INK, font_size=19),
        )
        flag_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        flag_lines.move_to(left_bg.get_center() + DOWN * 0.15)

        # Dividing line
        divider = DashedLine(
            left_bg.get_right() + RIGHT * 0.1 + UP * 2.0,
            left_bg.get_right() + RIGHT * 0.1 + DOWN * 2.0,
            stroke_width=1.5, color=SLATE
        )
        interp_label = SerifLabel("interpretation stays\nwith the teacher", accent=SLATE, size=18)
        interp_label.next_to(divider, RIGHT, buff=0.15)

        # Right: teacher feedback card
        right_bg = Rectangle(width=5.0, height=4.6)
        right_bg.set_fill(SLATE, 0.06).set_stroke(SLATE, 1.5)
        right_bg.to_edge(RIGHT, buff=0.8)

        right_header = Text("Seth's feedback", font=DISPLAY, color=INK,
                            font_size=20, weight="MEDIUM")
        right_header.next_to(right_bg.get_top() + DOWN * 0.45, ORIGIN)

        feedback_l1 = Text("engages with argument", font=SERIF, color=TEAL, font_size=19)
        feedback_l2 = Text("no grammar-first", font=SERIF, color=INK, font_size=19)
        feedback_l3 = Text("recommendation", font=SERIF, color=INK, font_size=19)
        feedback_lines = VGroup(feedback_l1, feedback_l2, feedback_l3)
        feedback_lines.arrange(DOWN, center=True, buff=0.3)
        feedback_lines.move_to(right_bg.get_center() + DOWN * 0.15)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_bg), FadeIn(left_header), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in flag_lines],
                              lag_ratio=0.2, run_time=0.9))
        self.play(Create(divider), FadeIn(interp_label), run_time=0.6)
        self.play(FadeIn(right_bg), FadeIn(right_header), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in feedback_lines],
                              lag_ratio=0.2, run_time=0.8))
        self.wait(8.2)


class B11_EquityConditions(Scene):
    def construct(self):
        title = Text("equity handoff conditions", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Two-column table header
        col1_h = Text("automatable", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        col2_h = Text("requires judgment", font=DISPLAY, color=INK,
                      font_size=22, weight="MEDIUM")

        col1_h.move_to(LEFT * 3.3 + UP * 1.7)
        col2_h.move_to(RIGHT * 2.5 + UP * 1.7)

        rule = Line(LEFT * 6.5 + UP * 1.3, RIGHT * 6.5 + UP * 1.3,
                    stroke_width=1.0, color=SLATE)

        # Automatable rows
        auto_items = VGroup(
            Text("no numeric grades in flags", font=SERIF, color=INK, font_size=20),
            Text("no normative register labels", font=SERIF, color=INK, font_size=20),
        )
        auto_items.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        auto_items.move_to(LEFT * 3.3 + UP * 0.4)

        # Judgment rows
        judge_items = VGroup(
            Text("ESL flag reports: teacher review", font=SERIF, color=INK, font_size=20),
            Text("AAVE flags: teacher review", font=SERIF, color=INK, font_size=20),
        )
        judge_items.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        judge_items.move_to(RIGHT * 2.5 + UP * 0.4)

        # Teacher icons (simple)
        icons = VGroup()
        for item in judge_items:
            icon = Text("⊕", font=SERIF, color=INK, font_size=20)
            icon.next_to(item, LEFT, buff=0.25)
            icons.add(icon)

        encode_label = SerifLabel("encode what you can — review what you cannot",
                                  accent=SLATE, size=20)
        encode_label.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(col1_h), FadeIn(col2_h), run_time=0.5)
        self.play(Create(rule), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(t) for t in auto_items],
                              lag_ratio=0.2, run_time=0.7))
        self.play(LaggedStart(*[FadeIn(t) for t in judge_items],
                              lag_ratio=0.2, run_time=0.7))
        self.play(LaggedStart(*[FadeIn(icon) for icon in icons],
                              lag_ratio=0.2, run_time=0.5))
        self.play(FadeIn(encode_label), run_time=0.4)
        self.wait(7.8)


class B12_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Claude detects.", font=SERIF, color=TEAL, font_size=44)
        m2 = Text("You interpret.", font=SERIF, color=INK, font_size=44)
        m3 = Text("That is the architecture.", font=SERIF, color=INK, font_size=36)
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
        self.wait(10.0)
