"""
scenes.py — claude-liam-political-neutrality-eval-paired-prompts
Political Neutrality: Measuring Even-Handedness with Paired Prompts.
Source: Anthropic — Political Neutrality Evaluation
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
        "After Anthropic — Political Neutrality Evaluation",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_PairedPromptDesign(Scene):
    def construct(self):
        dur = 19.0

        title = Text("Same Structure. Opposite Direction.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Template in center, two instances below
        template_box = RoundedRectangle(
            width=7.0, height=1.0, corner_radius=0.14,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([0, 1.8, 0])
        template_lbl = Text(
            'Template: "Summarize [SUBJECT]\'s position on [POLICY]."',
            font_size=15, color=SOFT
        )
        template_lbl.move_to(template_box)
        self.play(FadeIn(template_box), Write(template_lbl), run_time=0.5)

        # Left instance
        left_box = RoundedRectangle(
            width=5.2, height=1.6, corner_radius=0.14,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([-3.2, 0.0, 0])
        left_lbl = Text(
            'Left subject:\nDemocratic senator\non climate policy',
            font_size=14, color=INK
        )
        left_lbl.move_to(left_box)
        self.play(FadeIn(left_box), FadeIn(left_lbl), run_time=0.35)

        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=GHOST, stroke_width=2.0)
        arrow.move_to([0, 0.0, 0])
        self.play(GrowArrow(arrow), run_time=0.25)

        right_box = RoundedRectangle(
            width=5.2, height=1.6, corner_radius=0.14,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([3.2, 0.0, 0])
        right_lbl = Text(
            'Right subject:\nRepublican senator\non climate policy',
            font_size=14, color=SPARK
        )
        right_lbl.move_to(right_box)
        self.play(FadeIn(right_box), FadeIn(right_lbl), run_time=0.35)

        signal = Text(
            "Divergence in output = the signal.",
            font_size=19, color=SPARK, weight=BOLD
        )
        signal.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(signal), run_time=0.4)
        self.wait(dur - 5.0)


class B02_EvenHandednessMetric(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Even-Handedness Is a Delta, Not a Vibe.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Dimension", "Bias signal", "How to measure"]
        col_xs = [-4.5, 0.0, 4.5]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=17, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("Response length",     "One side longer",     "Word count delta"),
            ("Willingness to engage","One side refused",    "Refusal rate delta"),
            ("Tone / hedging",      "One side more hedged", "Hedge phrase count"),
        ]
        for i, (dim, signal, measure) in enumerate(rows):
            y = 1.0 - i * 1.0
            vals = [dim, signal, measure]
            cols = [INK, SPARK, SOFT]
            for val, x, col in zip(vals, col_xs, cols):
                t = Text(val, font_size=15, color=col)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.2)

        rule = Text(
            "None of these are invisible. All three produce numeric outputs.",
            font_size=17, color=SOFT
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 6.0)


class B03_EvalDesignRules(Scene):
    def construct(self):
        dur = 21.0

        title = Text("Three Rules for a Valid Neutrality Eval.", font_size=33, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        rules = [
            ("1. Structural identity",
             "Same verb, same subject position,\nsame tone in the question."),
            ("2. Many pairs, not one",
             "One pair is anecdote.\nMeasure across many topics."),
            ("3. Measure output quality",
             "Engagement alone is not enough.\nAsymmetric quality is still bias."),
        ]
        for i, (rule_hdr, rule_body) in enumerate(rules):
            y = 1.4 - i * 1.5
            col = SPARK if i == 0 else INK
            hdr = Text(rule_hdr, font_size=18, color=col, weight=BOLD)
            hdr.move_to([-1.5, y, 0])
            body = Text(rule_body, font_size=14, color=SOFT)
            body.move_to([3.0, y - 0.2, 0])
            line = Line([-6.5, y - 0.6, 0], [6.5, y - 0.6, 0], color=BORDER, stroke_width=0.8)
            self.play(FadeIn(hdr), FadeIn(body), run_time=0.35)
            self.play(FadeIn(line), run_time=0.15)

        note = Text(
            "Engagement ≠ even-handedness. Measure the output, not just the refusal.",
            font_size=16, color=SPARK, weight=BOLD
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 6.0)
