"""
scenes.py — claude-liam-prompt-tutorial-lesson-07-few-shot-prompting
Few-Shot Prompting: Implicit Style Encoding via Examples.
Source: Anthropic Prompt Engineering Interactive Tutorial — Lesson 07
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
        "After Anthropic Prompt Engineering Tutorial — Lesson 07",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_HowExamplesWork(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Input-Output Pairs. Model Generalizes.", font_size=35, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Three example pairs + target
        example_data = [
            ("Ex 1 input", "Ex 1 output"),
            ("Ex 2 input", "Ex 2 output"),
            ("Ex 3 input", "Ex 3 output"),
            ("Target input", "← model generates"),
        ]
        cols = [INK, INK, INK, SPARK]
        for i, ((inp, out), col) in enumerate(zip(example_data, cols)):
            y = 1.6 - i * 0.9
            in_box = RoundedRectangle(
                width=3.8, height=0.65, corner_radius=0.1,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.6
            ).move_to([-3.0, y, 0])
            in_lbl = Text(inp, font_size=13, color=col)
            in_lbl.move_to(in_box)

            arr = Arrow([-0.9, y, 0], [0.2, y, 0], color=GHOST,
                        stroke_width=1.5, max_tip_length_to_length_ratio=0.15)

            out_box = RoundedRectangle(
                width=3.8, height=0.65, corner_radius=0.1,
                color=col, fill_color=PAGE, fill_opacity=1,
                stroke_width=1.6 if i < 3 else 2.5
            ).move_to([3.0, y, 0])
            out_lbl = Text(out, font_size=13, color=col, weight=BOLD if i == 3 else NORMAL)
            out_lbl.move_to(out_box)
            self.play(FadeIn(in_box), FadeIn(in_lbl), GrowArrow(arr),
                      FadeIn(out_box), FadeIn(out_lbl), run_time=0.3)

        note = Text(
            "3-5 examples is sufficient. The pattern is the prompt.",
            font_size=17, color=SPARK, weight=BOLD
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 5.5)


class B02_WhatExamplesEncode(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Examples Compress Five Specifications at Once.", font_size=30, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Left: what examples encode; right: instruction equivalent
        headers = ["Examples encode", "Instruction equivalent"]
        col_xs = [-3.2, 3.2]
        for hdr, x in zip(headers, col_xs):
            col = SPARK if x < 0 else SOFT
            t = Text(hdr, font_size=17, color=col, weight=BOLD)
            t.move_to([x, 2.1, 0])
            self.add(t)
        div = Line([0, 2.4, 0], [0, -2.4, 0], color=BORDER, stroke_width=1.2)
        self.play(FadeIn(div), run_time=0.2)

        items = [
            ("Output length",         "1 sentence"),
            ("Vocabulary register",   "1 paragraph"),
            ("Structural template",   "1 paragraph"),
            ("Domain jargon",         "1 paragraph"),
            ("Edge-case handling",    "1 paragraph"),
        ]
        for i, (left, right) in enumerate(items):
            y = 1.3 - i * 0.85
            lt = Text(left, font_size=14, color=SPARK)
            lt.move_to([-3.2, y, 0])
            rt = Text(right, font_size=14, color=SOFT)
            rt.move_to([3.2, y, 0])
            self.play(FadeIn(lt), FadeIn(rt), run_time=0.25)

        verdict = Text(
            "Examples compress. Instructions expand.",
            font_size=18, color=INK, weight=BOLD
        )
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.4)
        self.wait(dur - 5.5)


class B03_ExampleQuality(Scene):
    def construct(self):
        dur = 21.0

        title = Text("Quality Matters More Than Count.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        rules = [
            ("1. Representative",
             "Do not pick only edge cases.\nTypical inputs teach typical outputs."),
            ("2. Internally consistent",
             "Mixed style teaches inconsistency.\nAll examples must share the target register."),
            ("3. Match target distribution",
             "If real inputs are technical,\nexamples must be technical."),
        ]
        for i, (label, detail) in enumerate(rules):
            y = 1.5 - i * 1.4
            col = SPARK if i == 0 else INK
            lbl = Text(label, font_size=17, color=col, weight=BOLD)
            lbl.move_to([-2.2, y, 0])
            dtl = Text(detail, font_size=14, color=SOFT)
            dtl.move_to([3.2, y - 0.1, 0])
            sep = Line([-6.5, y - 0.65, 0], [6.5, y - 0.65, 0], color=BORDER, stroke_width=0.8)
            self.play(FadeIn(lbl), FadeIn(dtl), run_time=0.35)
            self.play(FadeIn(sep), run_time=0.15)

        rule = Text(
            "One bad example contaminates the pattern.",
            font_size=17, color=SPARK, weight=BOLD
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.5)
