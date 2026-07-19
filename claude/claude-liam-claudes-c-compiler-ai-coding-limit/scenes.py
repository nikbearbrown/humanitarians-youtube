"""
scenes.py — claude-liam-claudes-c-compiler-ai-coding-limit
Claude Wrote a C Compiler From Scratch: What That Actually Proves.
Source: Anthropic engineering — claudes-c-compiler

Palette: Claude brand
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
        "After Anthropic Engineering — Claude's C Compiler (2024)",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_CompilerPipeline(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Eight Stages. No External Toolchain.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        stages = ["Lexer", "Parser", "AST", "SSA IR", "Optimizer", "Code Gen", "Assembler", "Linker"]
        n = len(stages)
        box_w = 1.55
        gap = 0.18
        total = n * box_w + (n - 1) * gap
        start_x = -total / 2 + box_w / 2

        boxes = []
        for i, s in enumerate(stages):
            x = start_x + i * (box_w + gap)
            is_spark = s in ("SSA IR", "Code Gen")
            col = SPARK if is_spark else INK
            b = Rectangle(
                width=box_w, height=1.2, color=col,
                fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([x, 0.4, 0])
            t = Text(s, font_size=14, color=col)
            t.move_to(b)
            boxes.append(VGroup(b, t))

        arrows = []
        for i in range(n - 1):
            a = Arrow(
                boxes[i].get_right() + RIGHT * 0.02,
                boxes[i+1].get_left() + LEFT * 0.02,
                color=GHOST, stroke_width=1.5, buff=0.02,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.append(a)

        # Target architectures
        targets = Text("Targets: x86-64  ·  i686  ·  AArch64  ·  RISC-V", font_size=18, color=SOFT)
        targets.move_to([0, -0.8, 0])

        no_dep = Text("Zero external toolchain dependencies.", font_size=20, color=SPARK, weight=BOLD)
        no_dep.to_edge(DOWN, buff=0.55)

        for grp in boxes:
            self.play(FadeIn(grp), run_time=0.2)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.15)
        self.wait(0.3)
        self.play(FadeIn(targets), run_time=0.5)
        self.play(FadeIn(no_dep), run_time=0.5)
        self.wait(dur - 5.5)


class B02_TDDMethod(Scene):
    def construct(self):
        dur = 20.4

        title = Text("The Constraint Is the Method.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        divider = Line(UP * 2.2, DOWN * 2.8, color=BORDER, stroke_width=1.5)
        self.add(divider)

        hdr_human = Text("Human writes", font_size=22, color=SOFT, weight=BOLD)
        hdr_human.move_to([-3.5, 1.9, 0])
        hdr_claude = Text("Claude writes", font_size=22, color=INK, weight=BOLD)
        hdr_claude.move_to([3.5, 1.9, 0])
        self.add(hdr_human, hdr_claude)

        human_items = [
            "Tests only.",
            "No hints after setup.",
            "No pair-programming.",
        ]
        claude_items = [
            "Everything else.",
            "Iterates against tests.",
            "Diagnoses failures alone.",
        ]

        for i, (h, c) in enumerate(zip(human_items, claude_items)):
            y = 1.0 - i * 1.0
            h_txt = Text(h, font_size=18, color=SOFT)
            h_txt.move_to([-3.5, y, 0])
            c_txt = Text(c, font_size=18, color=INK)
            c_txt.move_to([3.5, y, 0])
            self.play(FadeIn(h_txt), FadeIn(c_txt), run_time=0.45)
            self.wait(0.2)

        verdict = Text("One rule. The method is the constraint.", font_size=20, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 5.5)


class B03_CaveatFinding(Scene):
    def construct(self):
        dur = 22.3

        title = Text("The Caveat Is the Finding.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Quote box
        quote_box = Rectangle(
            width=10.5, height=1.4, color=SPARK,
            fill_color=PAGE, fill_opacity=1, stroke_width=2
        ).move_to([0, 1.6, 0])
        quote_txt = Text(
            '"I do not recommend you use this code —\nnone of it has been validated for correctness."',
            font_size=18, color=SPARK
        )
        quote_txt.move_to(quote_box)
        quote_src = Text("— Anthropic Engineering README", font_size=14, color=GHOST)
        quote_src.next_to(quote_box, DOWN, buff=0.1)

        # Two columns
        col_left_x = -3.0
        col_right_x = 3.0
        divider = Line([0, 0.6, 0], [0, -2.2, 0], color=BORDER, stroke_width=1.5)

        proved_lbl = Text("What it proved", font_size=18, color=INK, weight=BOLD)
        proved_lbl.move_to([col_left_x, 0.4, 0])
        not_lbl = Text("What it did not prove", font_size=18, color=SPARK, weight=BOLD)
        not_lbl.move_to([col_right_x, 0.4, 0])

        proved = ["Claude can build\nlarge, structured\nsoftware autonomously.", "TDD drives long-horizon\nagent tasks."]
        not_proved = ["Production-safe code.", "Validated correctness\non real workloads."]

        for i, (p, n) in enumerate(zip(proved, not_proved)):
            y = -0.4 - i * 0.9
            p_txt = Text(p, font_size=15, color=INK)
            p_txt.move_to([col_left_x, y, 0])
            n_txt = Text(n, font_size=15, color=SPARK)
            n_txt.move_to([col_right_x, y, 0])
            self.play(FadeIn(p_txt), FadeIn(n_txt), run_time=0.4)

        self.play(FadeIn(quote_box), Write(quote_txt), FadeIn(quote_src), Create(divider),
                  Write(proved_lbl), Write(not_lbl), run_time=1.2)
        self.wait(dur - 4.2)
