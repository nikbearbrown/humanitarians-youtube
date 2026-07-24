"""
scenes.py — claude-liam-prompt-engineering-precognition
Precognition: Why Telling Claude to Think First Doubles Accuracy.
Source: Anthropic prompt engineering tutorial Lesson 06
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
        "After Anthropic Prompt Engineering Tutorial — Lesson 06",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_AutoregressiveMechanism(Scene):
    def construct(self):
        dur = 20.4

        title = Text("Wrong Token. Wrong Distribution.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Token boxes in a sequence
        tokens = ["A", "bat", "costs", "$1", "more,", "so", "ball", "=", "$0.10"]
        xs = [-5.5 + i * 1.35 for i in range(len(tokens))]
        token_boxes = []
        for tok, x in zip(tokens, xs):
            is_wrong = tok in ("$0.10",)
            col = SPARK if is_wrong else INK
            b = Rectangle(width=1.1, height=0.65, color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.8)
            b.move_to([x, 0.8, 0])
            t = Text(tok, font_size=13, color=col)
            t.move_to(b)
            token_boxes.append(VGroup(b, t))

        # Conditioning arrows
        arrows = []
        for i in range(len(token_boxes) - 1):
            a = Arrow(
                token_boxes[i].get_right() + RIGHT * 0.02,
                token_boxes[i+1].get_left() + LEFT * 0.02,
                color=GHOST, stroke_width=1.2, buff=0.02,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.append(a)

        # Error cascade annotation
        cascade = Text("Each token conditions on all prior tokens — error cascades.", font_size=18, color=SOFT)
        cascade.move_to([0, -0.3, 0])

        wrong_note = Text("Wrong anchor. Subsequent tokens follow from here.", font_size=17, color=SPARK, weight=BOLD)
        wrong_note.to_edge(DOWN, buff=0.55)

        for grp in token_boxes:
            self.play(FadeIn(grp), run_time=0.18)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.12)
        self.wait(0.3)
        self.play(FadeIn(cascade), run_time=0.5)
        self.play(FadeIn(wrong_note), run_time=0.5)
        self.wait(dur - 6.2)


class B02_ChainOfThought(Scene):
    def construct(self):
        dur = 21.2

        title = Text("Put the Work on Paper Before Committing.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Left: no CoT
        left_hdr = Text("Without CoT", font_size=20, color=SOFT, weight=BOLD)
        left_hdr.move_to([-4.0, 2.2, 0])
        left_q = Text("Bat + ball = $1.10\nBat is $1 more.\nBall = ?", font_size=17, color=SOFT)
        left_q.move_to([-4.0, 1.2, 0])
        left_arrow = Arrow(LEFT * 4.0 + UP * 0.3, LEFT * 4.0 + DOWN * 0.4,
                           color=GHOST, stroke_width=2, buff=0)
        left_ans = Text("$0.10  ✗", font_size=24, color=SPARK, weight=BOLD)
        left_ans.move_to([-4.0, -0.8, 0])

        # Right: with CoT
        right_hdr = Text("With CoT", font_size=20, color=INK, weight=BOLD)
        right_hdr.move_to([2.5, 2.2, 0])
        steps = [
            "Let ball = x",
            "Bat = x + 1",
            "x + (x+1) = 1.10",
            "2x = 0.10",
            "x = $0.05  ✓",
        ]
        step_grps = []
        for i, s in enumerate(steps):
            is_ans = "✓" in s
            col = SPARK if is_ans else INK
            t = Text(s, font_size=17, color=col, weight=BOLD if is_ans else NORMAL)
            t.move_to([2.5, 1.3 - i * 0.65, 0])
            step_grps.append(t)

        divider = Line(UP * 2.3, DOWN * 2.5, color=BORDER, stroke_width=1.5)
        self.add(divider)

        verdict = Text("Intermediate tokens shift the distribution toward the correct answer.", font_size=17, color=SOFT)
        verdict.to_edge(DOWN, buff=0.55)

        self.play(Write(left_hdr), FadeIn(left_q), run_time=0.5)
        self.play(GrowArrow(left_arrow), FadeIn(left_ans), run_time=0.5)
        self.wait(0.3)
        self.play(Write(right_hdr), run_time=0.3)
        for s in step_grps:
            self.play(FadeIn(s), run_time=0.28)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 5.8)


class B03_CoTScope(Scene):
    def construct(self):
        dur = 21.9

        title = Text("When CoT Helps. When It Hurts.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        divider = Line(UP * 2.1, DOWN * 2.5, color=BORDER, stroke_width=1.5)
        self.add(divider)

        hdr_helps = Text("CoT helps", font_size=21, color=INK, weight=BOLD)
        hdr_helps.move_to([-3.5, 1.9, 0])
        hdr_hurts = Text("CoT hurts or is noise", font_size=21, color=SPARK, weight=BOLD)
        hdr_hurts.move_to([3.5, 1.9, 0])
        self.add(hdr_helps, hdr_hurts)

        helps = ["Multi-step math", "Logic puzzles", "Complex code", "Ambiguous instructions"]
        hurts = ["Simple factual lookup", "Yes/no classification", "Single-word answers", "Retrieval from context"]

        for i, (h, ht) in enumerate(zip(helps, hurts)):
            y = 1.1 - i * 0.85
            h_txt = Text(h, font_size=17, color=INK)
            h_txt.move_to([-3.5, y, 0])
            ht_txt = Text(ht, font_size=17, color=SPARK)
            ht_txt.move_to([3.5, y, 0])
            self.play(Write(h_txt), FadeIn(ht_txt), run_time=0.38)

        note = Text("Extended thinking (token budget) is a different mechanism — don't conflate.", font_size=16, color=SOFT)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(dur - 5.5)
