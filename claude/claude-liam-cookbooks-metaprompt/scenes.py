"""
scenes.py — claude-liam-cookbooks-metaprompt
The Anthropic Metaprompt: Task Description to Production Prompt.
Source: Anthropic Cookbooks — Metaprompt
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
        "After Anthropic Cookbooks — Metaprompt",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_MetapromptIO(Scene):
    def construct(self):
        dur = 20.0

        title = Text("One Input. One Complete Template.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Input box
        in_box = RoundedRectangle(
            width=5.0, height=1.8, corner_radius=0.18,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.6
        ).move_to([-3.5, 0.4, 0])
        in_hdr = Text("Input", font_size=16, color=SOFT, weight=BOLD)
        in_hdr.next_to(in_box, UP, buff=0.1)
        in_body = Text(
            '"Classify customer emails\nby urgency level."',
            font_size=14, color=SOFT
        )
        in_body.move_to(in_box)
        self.play(FadeIn(in_box), Write(in_hdr), FadeIn(in_body), run_time=0.5)

        # Arrow
        arrow = Arrow(
            start=[-0.8, 0.4, 0], end=[0.8, 0.4, 0],
            color=SPARK, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.15
        )
        meta_lbl = Text("metaprompt", font_size=13, color=SPARK)
        meta_lbl.next_to(arrow, UP, buff=0.1)
        self.play(GrowArrow(arrow), FadeIn(meta_lbl), run_time=0.4)

        # Output box
        out_box = RoundedRectangle(
            width=5.0, height=1.8, corner_radius=0.18,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([3.5, 0.4, 0])
        out_hdr = Text("Output", font_size=16, color=SPARK, weight=BOLD)
        out_hdr.next_to(out_box, UP, buff=0.1)
        out_body = Text(
            "Full prompt template:\nrole, context, format,\nlogic, edge cases.",
            font_size=13, color=INK
        )
        out_body.move_to(out_box)
        self.play(FadeIn(out_box), Write(out_hdr), FadeIn(out_body), run_time=0.5)

        note = Text(
            "Blank page → structured draft. Best-practices baked in.",
            font_size=17, color=SOFT
        )
        note.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 5.0)


class B02_OutputComponents(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Six Components, One Description.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        components = [
            ("Role",          "Who Claude is in this task"),
            ("Context",       "Background knowledge needed"),
            ("Input format",  "How data arrives"),
            ("Instructions",  "Step-by-step task logic"),
            ("Output format", "What the response looks like"),
            ("Edge cases",    "Explicit exception handling"),
        ]
        cols = [SPARK, SPARK, INK, INK, SPARK, INK]
        for i, ((comp, desc), col) in enumerate(zip(components, cols)):
            col_x = -2.8 if i % 2 == 0 else 2.8
            y = 1.8 - (i // 2) * 1.3
            box = RoundedRectangle(
                width=4.6, height=0.9, corner_radius=0.12,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.6
            ).move_to([col_x, y, 0])
            lbl = Text(comp, font_size=15, color=col, weight=BOLD)
            lbl.move_to(box).shift(LEFT * 1.0)
            dtl = Text(desc, font_size=13, color=SOFT)
            dtl.move_to(box).shift(RIGHT * 0.6)
            self.play(FadeIn(VGroup(box, lbl, dtl)), run_time=0.25)

        note = Text("Review, edit, promote to production.", font_size=17, color=SPARK, weight=BOLD)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 6.0)


class B03_WhenToUse(Scene):
    def construct(self):
        dur = 19.0

        title = Text("Generate the Draft. Own the Review.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Metaprompt does", "You must do"]
        col_xs = [-3.0, 3.0]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            col = SPARK if x < 0 else INK
            t = Text(hdr, font_size=19, color=col, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line([0, 2.5, 0], [0, -2.5, 0], color=BORDER, stroke_width=1.2)
        self.play(FadeIn(div), run_time=0.2)

        left_items = [
            "Apply best-practice structure",
            "Scaffold six components",
            "Remove blank-page paralysis",
        ]
        right_items = [
            "Verify against real inputs",
            "Add your schema and edge cases",
            "Iterate on failures you've seen",
        ]
        for i, (l, r) in enumerate(zip(left_items, right_items)):
            y = 1.2 - i * 1.1
            lt = Text(l, font_size=14, color=SPARK)
            lt.move_to([-3.0, y, 0])
            rt = Text(r, font_size=14, color=INK)
            rt.move_to([3.0, y, 0])
            self.play(FadeIn(lt), FadeIn(rt), run_time=0.3)

        verdict = Text(
            "Strong first draft. Final judgment is yours.",
            font_size=18, color=SOFT
        )
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.4)
        self.wait(dur - 5.5)
