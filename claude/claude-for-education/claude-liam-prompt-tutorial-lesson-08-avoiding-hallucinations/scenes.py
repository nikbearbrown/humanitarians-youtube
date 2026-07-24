"""
scenes.py — claude-liam-prompt-tutorial-lesson-08-avoiding-hallucinations
Grounding: The Only Reliable Way to Stop Claude from Hallucinating.
Source: Anthropic prompt engineering tutorial Lesson 08
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Anthropic Prompt Engineering Tutorial — Lesson 08",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_HallucinationMechanism(Scene):
    def construct(self):
        dur = 20.8

        title = Text("Confidence and Correctness Are Uncorrelated.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two columns: confident correct vs confident wrong
        # Bar chart showing confidence vs correctness are independent

        ground_y = -2.2
        ground = Line(LEFT * 5.5, RIGHT * 5.5, color=BORDER, stroke_width=1.5).shift(DOWN * 2.2)
        self.add(ground)

        def make_bar(x, w, h_frac, col):
            h = h_frac * 4.0
            r = Rectangle(width=w, height=h, color=col, fill_color=col, fill_opacity=0.85, stroke_width=0)
            r.move_to([x, ground_y + h / 2, 0])
            return r

        bw = 1.4
        # Case A: confident, correct
        a_conf = make_bar(-3.5, bw, 0.85, INK)
        a_corr = make_bar(-2.0, bw, 0.85, INK)
        a_lbl = Text("Confident\n+ Correct", font_size=15, color=SOFT)
        a_lbl.move_to([-2.75, ground_y - 0.55, 0])

        # Case B: confident, WRONG — terracotta
        b_conf = make_bar(1.5, bw, 0.85, INK)
        b_corr = make_bar(3.0, bw, 0.15, SPARK)  # correctness is LOW
        b_lbl = Text("Confident\n+ Wrong", font_size=15, color=SPARK)
        b_lbl.move_to([2.25, ground_y - 0.55, 0])

        col_labels = ["Confidence", "Correctness", "Confidence", "Correctness"]
        col_xs = [-3.5, -2.0, 1.5, 3.0]
        col_cols = [SOFT, SOFT, SOFT, SPARK]
        for lbl, x, c in zip(col_labels, col_xs, col_cols):
            t = Text(lbl, font_size=12, color=c)
            t.move_to([x, ground_y - 0.25, 0])
            self.add(t)

        verdict = Text("A confident hallucination looks identical to a confident correct answer.", font_size=18, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)

        y_lbl = Text("Level", font_size=16, color=SOFT)
        y_lbl.to_edge(LEFT, buff=0.4).shift(UP * 0.5)
        self.add(y_lbl)

        self.play(Create(a_conf), Create(a_corr), FadeIn(a_lbl), run_time=0.7)
        self.wait(0.3)
        self.play(Create(b_conf), Create(b_corr), FadeIn(b_lbl), run_time=0.7)
        self.wait(0.4)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 4.6)


class B02_GroundingPattern(Scene):
    def construct(self):
        dur = 21.2

        title = Text("Grounding: Three Parts.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        steps = [
            ("1", "Provide the source document\nin the prompt.", INK),
            ("2", "Answer only from that document.", INK),
            ("3", "Say 'I don't know' if the\nanswer isn't in the source.", SPARK),
        ]

        for i, (num, text, col) in enumerate(steps):
            y = 1.5 - i * 1.2
            box = RoundedRectangle(
                width=9.0, height=0.95, corner_radius=0.12,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([0.5, y, 0])
            num_t = Text(num + ".", font_size=22, color=col, weight=BOLD)
            num_t.move_to([-4.5, y, 0])
            txt_t = Text(text, font_size=17, color=col)
            txt_t.move_to(box).shift(LEFT * 0.2)
            self.play(FadeIn(box), Write(num_t), Write(txt_t), run_time=0.55)
            self.wait(0.2)

        # Before/after bar
        before_lbl = Text("Ungrounded hallucination rate", font_size=16, color=SOFT)
        before_lbl.move_to([-3.0, -2.0, 0])
        before_bar = Rectangle(width=4.5, height=0.5, color=INK, fill_color=INK, fill_opacity=0.7, stroke_width=0)
        before_bar.move_to([1.5, -2.0, 0])

        after_lbl = Text("Grounded hallucination rate", font_size=16, color=SOFT)
        after_lbl.move_to([-3.0, -2.75, 0])
        after_bar = Rectangle(width=0.5, height=0.5, color=SPARK, fill_color=SPARK, fill_opacity=0.7, stroke_width=0)
        after_bar.move_to([-1.25, -2.75, 0])

        self.play(Write(before_lbl), FadeIn(before_bar), run_time=0.5)
        self.play(Write(after_lbl), FadeIn(after_bar), run_time=0.5)
        self.wait(dur - 6.0)


class B03_CitationVerification(Scene):
    def construct(self):
        dur = 21.2

        title = Text("The Verifiable Citation Is the Audit Trail.", font_size=33, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Three-step verification flow
        steps = ["Claude's answer", "Cited passage", "Source doc check"]
        arrows = []
        boxes = []
        xs = [-4.5, 0.0, 4.5]
        for s, x in zip(steps, xs):
            b = RoundedRectangle(
                width=3.4, height=1.2, corner_radius=0.15,
                color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([x, 1.2, 0])
            t = Text(s, font_size=18, color=INK)
            t.move_to(b)
            boxes.append(VGroup(b, t))

        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i].get_right() + RIGHT * 0.05,
                boxes[i+1].get_left() + LEFT * 0.05,
                color=GHOST, stroke_width=2, buff=0.05
            )
            arrows.append(a)

        # Good: found in source
        good_box = Rectangle(
            width=4.5, height=0.9, color=INK,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([0, -0.5, 0])
        good_txt = Text("Found verbatim in source — grounded.", font_size=16, color=INK)
        good_txt.move_to(good_box)

        # Bad: not found
        bad_box = Rectangle(
            width=4.5, height=0.9, color=SPARK,
            fill_color=PAGE, fill_opacity=1, stroke_width=2
        ).move_to([0, -1.7, 0])
        bad_txt = Text("Not in source — hallucinated citation.", font_size=16, color=SPARK, weight=BOLD)
        bad_txt.move_to(bad_box)

        verdict = Text("If you can't find the passage in the source, the answer is not grounded.", font_size=17, color=SOFT)
        verdict.to_edge(DOWN, buff=0.55)

        for grp in boxes:
            self.play(FadeIn(grp), run_time=0.4)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.3)
        self.wait(0.3)
        self.play(Create(good_box), Write(good_txt), run_time=0.5)
        self.play(Create(bad_box), Write(bad_txt), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 5.5)
