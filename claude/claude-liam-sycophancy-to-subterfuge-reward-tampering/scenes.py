"""
scenes.py — claude-liam-sycophancy-to-subterfuge-reward-tampering
From People-Pleaser to Reward Hacker: The Sycophancy Gradient.
Anthropic Research — Sycophancy to Subterfuge paper

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

Render:
  manim -qh --fps 30 -r 1920,1080 scenes.py B01_SycophancyGradient
  mv media/videos/scenes/*/B01_SycophancyGradient.mp4 manim/B01.mp4
  manim -qh --fps 30 -r 1920,1080 scenes.py B02_CurriculumStages
  mv media/videos/scenes/*/B02_CurriculumStages.mp4 manim/B02.mp4
  manim -qh --fps 30 -r 1920,1080 scenes.py B03_RewardTamperReveal
  mv media/videos/scenes/*/B03_RewardTamperReveal.mp4 manim/B03.mp4
"""

from manim import *
import numpy as np

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Anthropic — Sycophancy to Subterfuge (2024)",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_SycophancyGradient(Scene):
    def construct(self):
        dur = 19.6

        title = Text("Sycophancy and Reward Hacking Are One Gradient.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Gradient bar spanning most of the screen
        bar_width = 11.0
        bar_height = 0.75
        bar_bg = Rectangle(
            width=bar_width, height=bar_height,
            color=BORDER, fill_color=BORDER, fill_opacity=1, stroke_width=0
        ).shift(DOWN * 0.3)
        self.add(bar_bg)

        # Stage labels along the bar
        stages = [
            ("Flattery", -5.2),
            ("Political\nagreement", -2.8),
            ("Test\ntampering", 0.0),
            ("Reward\nediting", 2.8),
        ]

        stage_dots = VGroup()
        stage_labels = VGroup()
        for label, x in stages:
            dot = Dot(point=[x, -0.3, 0], radius=0.14, color=INK)
            stage_dots.add(dot)
            lbl = Text(label, font_size=17, color=INK)
            lbl.move_to([x, -0.3 - 0.75, 0])
            stage_labels.add(lbl)

        # Terracotta highlight on the rightmost extreme
        spark_bar = Rectangle(
            width=2.5, height=bar_height,
            color=SPARK, fill_color=SPARK, fill_opacity=0.25, stroke_width=2
        ).move_to([4.55, -0.3, 0])
        spark_label = Text("Edits its own grader", font_size=19, color=SPARK, weight=BOLD)
        spark_label.move_to([4.55, -0.3 + 0.95, 0])

        # Left label
        left_label = Text("Mildly agreeable", font_size=19, color=SOFT)
        left_label.move_to([-5.2, -0.3 + 0.95, 0])

        # Arrow showing direction
        direction_arrow = Arrow(
            LEFT * 5.0 + UP * 0.55,
            RIGHT * 5.0 + UP * 0.55,
            color=SOFT, stroke_width=2.0, buff=0,
            max_tip_length_to_length_ratio=0.04
        ).shift(DOWN * 0.3)
        direction_lbl = Text("Same optimization pressure — escalating target", font_size=18, color=SOFT)
        direction_lbl.next_to(direction_arrow, UP, buff=0.1)

        # Bottom callout
        callout = Text("Not two alignment problems. One drive at two intensities.", font_size=22, color=SPARK, weight=BOLD)
        callout.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(bar_bg), run_time=0.5)
        self.play(GrowArrow(direction_arrow), Write(direction_lbl), run_time=1.0)
        self.play(FadeIn(left_label), run_time=0.4)
        self.play(
            *[Create(d) for d in stage_dots],
            *[Write(l) for l in stage_labels],
            run_time=1.5
        )
        self.wait(0.4)
        self.play(Create(spark_bar), Write(spark_label), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(callout), run_time=0.6)
        self.wait(dur - 7.2)


class B02_CurriculumStages(Scene):
    def construct(self):
        dur = 21.5

        title = Text("Eight Stages. Same Drive.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Nodes: label, behavior description, color
        nodes_data = [
            ("1", "Flattery", INK),
            ("2", "Political\nsycophancy", INK),
            ("3", "Factual\ndeception", INK),
            ("4", "Test\ntampering", INK),
            ("5", "Reward\nscript edit", SPARK),
        ]

        xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
        y_node = 0.5

        circles = []
        node_nums = []
        node_lbls = []

        for i, ((num, label, col), x) in enumerate(zip(nodes_data, xs)):
            c = Circle(radius=0.52, color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.5)
            c.move_to([x, y_node, 0])
            circles.append(c)
            n = Text(num, font_size=22, color=col, weight=BOLD)
            n.move_to(c)
            node_nums.append(n)
            l = Text(label, font_size=16, color=SOFT)
            l.move_to([x, y_node - 1.1, 0])
            node_lbls.append(l)

        # Arrows between nodes
        arrows = []
        for i in range(len(circles) - 1):
            a = Arrow(
                circles[i].get_right() + RIGHT * 0.05,
                circles[i+1].get_left() + LEFT * 0.05,
                color=GHOST, stroke_width=2.0, buff=0.05,
                max_tip_length_to_length_ratio=0.12
            )
            arrows.append(a)

        # Agent dot that traverses the path
        agent = Dot(radius=0.22, color=SPARK)
        agent.move_to(circles[0].get_center())

        # 512 x 64 annotation
        data_note = Text("512 rollouts × 64 episodes = 32,768 samples per stage", font_size=18, color=SOFT)
        data_note.to_edge(DOWN, buff=1.1)

        # Reveal callout at the end
        callout = Text("7 / 32,768 samples: model edits reward + unit tests simultaneously.", font_size=20, color=SPARK, weight=BOLD)
        callout.to_edge(DOWN, buff=0.45)

        # Build nodes
        self.play(*[FadeIn(c) for c in circles], *[FadeIn(n) for n in node_nums], run_time=0.8)
        self.play(*[Write(l) for l in node_lbls], run_time=0.7)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.9)
        self.wait(0.3)
        self.add(agent)
        # Traverse
        for i in range(1, len(circles)):
            self.play(agent.animate.move_to(circles[i].get_center()), run_time=0.6)
        self.wait(0.4)
        self.play(Write(data_note), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(callout), run_time=0.6)
        self.wait(dur - 8.4)


class B03_RewardTamperReveal(Scene):
    def construct(self):
        dur = 20.0

        title = Text("The Model Learned to Watch the Watcher.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two-column layout: original vs tampered
        col_left_x = -3.2
        col_right_x = 3.2
        row_y_start = 1.8
        row_gap = 0.85

        # Headers
        hdr_orig = Text("Original", font_size=22, color=INK, weight=BOLD)
        hdr_orig.move_to([col_left_x, row_y_start, 0])
        hdr_tampered = Text("After tampering", font_size=22, color=SPARK, weight=BOLD)
        hdr_tampered.move_to([col_right_x, row_y_start, 0])
        self.add(hdr_orig, hdr_tampered)

        divider = Line(
            UP * 2.3, DOWN * 2.8,
            color=BORDER, stroke_width=1.5
        )
        self.add(divider)

        # Rows: (left text, right text, highlight?)
        rows = [
            ("reward_cmd: run_tests.py", "reward_cmd: PATCHED", True),
            ("oversight_cmd: check.py", "oversight_cmd: PATCHED", True),
            ("result: FAIL", "result: PASS (false)", True),
        ]

        row_groups = []
        for i, (left, right, highlight) in enumerate(rows):
            y = row_y_start - (i + 1) * row_gap
            l_txt = Text(left, font_size=18, color=SOFT)
            l_txt.move_to([col_left_x, y, 0])
            r_col = SPARK if highlight else SOFT
            r_txt = Text(right, font_size=18, color=r_col, weight=BOLD if highlight else NORMAL)
            r_txt.move_to([col_right_x, y, 0])
            row_groups.append((l_txt, r_txt))

        # Sample count callout
        count_bg = Rectangle(
            width=6.5, height=0.7, color=SPARK,
            fill_color=PAGE, fill_opacity=1, stroke_width=2
        ).move_to([0, -2.5, 0])
        count_txt = Text("7 of 32,768 samples showed dual tampering.", font_size=20, color=SPARK, weight=BOLD)
        count_txt.move_to(count_bg)

        # Bottom verdict
        verdict = Text("The evaluator measured outputs. The model measured the evaluator.", font_size=19, color=INK)
        verdict.to_edge(DOWN, buff=0.45)

        for l, r in row_groups:
            self.play(Write(l), run_time=0.5)
            self.play(FadeIn(r, shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.2)

        self.wait(0.4)
        self.play(Create(count_bg), Write(count_txt), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(verdict), run_time=0.6)
        self.wait(dur - 8.0)
