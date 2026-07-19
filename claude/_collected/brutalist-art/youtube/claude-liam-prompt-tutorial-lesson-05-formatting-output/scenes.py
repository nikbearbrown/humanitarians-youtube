"""
scenes.py — claude-liam-prompt-tutorial-lesson-05-formatting-output
Output Formatting: The Prefill Technique and When to Control Format.
Source: Anthropic Prompt Engineering Interactive Tutorial — Lesson 05
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
        "After Anthropic Prompt Engineering Tutorial — Lesson 05",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_PrefillTechnique(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Prefill Is a Structural Constraint, Not a Request.", font_size=31, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Without prefill
        no_hdr = Text("Without prefill", font_size=16, color=SPARK, weight=BOLD)
        no_hdr.move_to([-3.5, 2.0, 0])
        self.play(FadeIn(no_hdr), run_time=0.3)

        no_lines = [
            ("Human:", GHOST, '"Extract facts as JSON."'),
            ("Assistant:", SOFT, '"Sure! Here are the facts:'),
            ("", SOFT, '{"fact1": "..."}'),
        ]
        for i, (role, rcol, text) in enumerate(no_lines):
            role_t = Text(role, font_size=13, color=rcol, weight=BOLD) if role else Text("", font_size=13)
            role_t.move_to([-4.8, 1.2 - i * 0.6, 0])
            text_t = Text(text, font_size=13, color=INK)
            text_t.move_to([-3.0, 1.2 - i * 0.6, 0])
            self.play(FadeIn(role_t), FadeIn(text_t), run_time=0.2)

        # Divider
        div = Line([0, 2.3, 0], [0, -2.3, 0], color=BORDER, stroke_width=1.2)
        self.play(FadeIn(div), run_time=0.2)

        # With prefill
        yes_hdr = Text("With prefill", font_size=16, color=INK, weight=BOLD)
        yes_hdr.move_to([3.5, 2.0, 0])
        self.play(FadeIn(yes_hdr), run_time=0.3)

        yes_lines = [
            ("Human:", GHOST, '"Extract facts as JSON."'),
            ("Assistant:", SOFT, '"{"  ← prefill seed'),
            ("", INK,  '"fact1": "...",'),
            ("", INK,  '"fact2": "..."}'),
        ]
        for i, (role, rcol, text) in enumerate(yes_lines):
            role_t = Text(role, font_size=13, color=rcol, weight=BOLD) if role else Text("", font_size=13)
            role_t.move_to([1.8, 1.2 - i * 0.6, 0])
            text_t = Text(text, font_size=13, color=INK)
            text_t.move_to([3.5, 1.2 - i * 0.6, 0])
            self.play(FadeIn(role_t), FadeIn(text_t), run_time=0.2)

        note = Text(
            "Prefill = context already in sequence. Model completes, not restarts.",
            font_size=16, color=SPARK, weight=BOLD
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 6.0)


class B02_FormatDecisionMatrix(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Match Format to Consumer.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Format", "Use when consumer is", "Example"]
        col_xs = [-4.5, 0.0, 4.5]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=17, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("JSON",          "Code parsing it",       SPARK, '{"key": "val"}'),
            ("Markdown",      "A rendered UI",          INK,  "## Heading\\n- item"),
            ("Plain prose",   "Human reading directly", SOFT, "The answer is X."),
            ("Numbered list", "Strict-order sequence",  INK,  "1. First\\n2. Second"),
        ]
        for i, (fmt, consumer, col, example) in enumerate(rows):
            y = 1.0 - i * 0.85
            vals = [fmt, consumer, example]
            vcols = [col, SOFT, GHOST]
            for val, x, vcol in zip(vals, col_xs, vcols):
                t = Text(val, font_size=13, color=vcol)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.2)

        verdict = Text(
            "Wrong format = friction downstream.",
            font_size=18, color=SPARK, weight=BOLD
        )
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.4)
        self.wait(dur - 6.0)


class B03_FormatPitfalls(Scene):
    def construct(self):
        dur = 21.0

        title = Text("Format Is Invisible When Right. Visible When Wrong.", font_size=29, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        pitfalls = [
            ("1. Under-specifying",
             "Expected JSON, got prose.\nFailed the downstream parser."),
            ("2. Over-specifying",
             "Bullet points on a simple fact.\nAdds structure with no value."),
            ("3. Wrong context",
             "Markdown in raw output.\nAsterisks appear as characters."),
        ]
        for i, (label, detail) in enumerate(pitfalls):
            y = 1.5 - i * 1.4
            col = SPARK if i == 0 else INK
            lbl = Text(label, font_size=17, color=col, weight=BOLD)
            lbl.move_to([-2.0, y, 0])
            dtl = Text(detail, font_size=14, color=SOFT)
            dtl.move_to([3.0, y - 0.1, 0])
            sep = Line([-6.5, y - 0.65, 0], [6.5, y - 0.65, 0], color=BORDER, stroke_width=0.8)
            self.play(FadeIn(lbl), FadeIn(dtl), run_time=0.35)
            self.play(FadeIn(sep), run_time=0.15)

        rule = Text(
            "Format invisible when right. Visible — and painful — when wrong.",
            font_size=16, color=SOFT
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.5)
