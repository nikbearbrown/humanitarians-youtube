"""
scenes.py — claude-liam-model-written-evals-sycophancy
Model-Written Evals: Generating 50k Sycophancy Questions.
Source: Perez et al. 2022 — Discovering LM Behaviors with Model-Written Evaluations
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
        "After Perez et al. 2022 — Model-Written Evaluations, Anthropic",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_GenerationPipeline(Scene):
    def construct(self):
        dur = 22.0

        title = Text("Seeds Are Human. Scale Is the Model.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Three-step pipeline
        steps = [
            ("1. Hand-write seeds",    "~12 expert items",         INK),
            ("2. Generate at scale",   "50,000 via model",         SPARK),
            ("3. Quality filter",      "Classifier gates output",  SOFT),
        ]
        xs = [-4.2, 0.0, 4.2]
        arrows_xs = [(-2.5, -1.7), (1.6, 2.4)]

        for (step, detail, col), x in zip(steps, xs):
            box = RoundedRectangle(
                width=3.6, height=1.8, corner_radius=0.18,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, 0.5, 0])
            lbl = Text(step, font_size=15, color=col, weight=BOLD)
            lbl.move_to(box).shift(UP * 0.4)
            dtl = Text(detail, font_size=14, color=SOFT)
            dtl.move_to(box).shift(DOWN * 0.3)
            self.play(FadeIn(VGroup(box, lbl, dtl)), run_time=0.35)

        for (ax1, ax2) in arrows_xs:
            arr = Arrow([ax1, 0.5, 0], [ax2, 0.5, 0], color=GHOST,
                        stroke_width=1.8, max_tip_length_to_length_ratio=0.12)
            self.play(GrowArrow(arr), run_time=0.25)

        note = Text(
            "Cost: weeks, not years. Human judgment on the criterion, not every item.",
            font_size=16, color=SOFT
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 6.0)


class B02_HumanValidation(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Validate a Sample. Ship the Set.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Visual: 50k items, sample highlighted
        total_lbl = Text("50,000 generated items", font_size=18, color=SOFT)
        total_lbl.move_to([0, 2.0, 0])
        self.play(FadeIn(total_lbl), run_time=0.3)

        # Grid of dots
        dots = VGroup()
        for row in range(5):
            for col in range(20):
                d = Dot(radius=0.08, color=GHOST)
                d.move_to([-4.75 + col * 0.5, 1.0 - row * 0.4, 0])
                dots.add(d)
        self.play(FadeIn(dots), run_time=0.4)

        # Highlight sample (first 10)
        sample_highlight = SurroundingRectangle(
            VGroup(*dots[:10]), color=SPARK, stroke_width=2.0, buff=0.05
        )
        sample_lbl = Text("Human sample", font_size=14, color=SPARK, weight=BOLD)
        sample_lbl.next_to(sample_highlight, UP, buff=0.1)
        self.play(FadeIn(sample_highlight), Write(sample_lbl), run_time=0.4)

        # Decision
        pass_box = RoundedRectangle(
            width=4.0, height=1.0, corner_radius=0.14,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([-2.5, -1.5, 0])
        pass_lbl = Text("PASS → ship full set", font_size=16, color=INK)
        pass_lbl.move_to(pass_box)

        fail_box = RoundedRectangle(
            width=4.0, height=1.0, corner_radius=0.14,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([2.5, -1.5, 0])
        fail_lbl = Text("FAIL → adjust prompt, rerun", font_size=16, color=SPARK)
        fail_lbl.move_to(fail_box)

        self.play(FadeIn(pass_box), FadeIn(pass_lbl), FadeIn(fail_box), FadeIn(fail_lbl), run_time=0.5)
        self.wait(dur - 5.5)


class B03_WhatItFound(Scene):
    def construct(self):
        dur = 19.0

        title = Text("A Number You Can Track Across Versions.", font_size=33, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two sycophancy behaviors as comparison bars
        behaviors = [
            ("Agrees with confident false\nstatements", 0.62),
            ("Changes correct answer when\npushed back", 0.47),
        ]
        bar_color = SPARK
        for i, (label, rate) in enumerate(behaviors):
            y = 1.2 - i * 1.8
            lbl = Text(label, font_size=15, color=INK)
            lbl.move_to([-3.0, y, 0])

            # Bar background
            bg = Rectangle(
                width=5.0, height=0.55,
                fill_color=BORDER, fill_opacity=1, stroke_width=0
            ).move_to([2.5, y, 0])
            self.add(bg)

            # Filled bar
            filled_w = 5.0 * rate
            filled = Rectangle(
                width=filled_w, height=0.55,
                fill_color=bar_color, fill_opacity=1, stroke_width=0
            )
            filled.align_to(bg, LEFT)
            filled.shift(RIGHT * ((5.0 - filled_w) / 2 * 0) )
            filled.move_to([0, y, 0])
            filled.align_to(bg, LEFT)

            rate_lbl = Text(f"{int(rate*100)}%", font_size=16, color=INK, weight=BOLD)
            rate_lbl.next_to(bg, RIGHT, buff=0.15)

            self.play(FadeIn(lbl), FadeIn(bg), FadeIn(filled), FadeIn(rate_lbl), run_time=0.4)

        verdict = Text(
            "Sycophancy rate: a regression test for honesty.",
            font_size=18, color=SPARK, weight=BOLD
        )
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.4)
        self.wait(dur - 5.0)
