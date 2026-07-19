"""
scenes.py — claude-liam-quickstarts-computer-use-best-practices
Computer Use in Production: The $50 Screenshot Problem.
Source: Anthropic Quickstarts — computer-use-best-practices

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider
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
        "After Anthropic Quickstarts — computer-use-best-practices",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_NaiveLoop(Scene):
    def construct(self):
        dur = 19.6

        title = Text("The Naive Loop Burns Money.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        steps = ["Screenshot", "Full-res\nimage", "Tokens", "Action"]
        xs = [-4.5, -1.5, 1.5, 4.5]
        boxes = []
        for s, x in zip(steps, xs):
            b = RoundedRectangle(
                width=2.6, height=1.4, corner_radius=0.15,
                color=BORDER, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([x, 0.6, 0])
            t = Text(s, font_size=20, color=INK)
            t.move_to(b)
            boxes.append(VGroup(b, t))

        arrows = []
        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i].get_right() + RIGHT * 0.05,
                boxes[i+1].get_left() + LEFT * 0.05,
                color=GHOST, stroke_width=2, buff=0.05
            )
            arrows.append(a)

        # Repeat arrow looping back
        loop_arrow = CurvedArrow(
            boxes[-1].get_bottom() + DOWN * 0.1,
            boxes[0].get_bottom() + DOWN * 0.1,
            color=SOFT, stroke_width=1.8, angle=-TAU/3
        )
        step_lbl = Text("× 50 steps", font_size=20, color=SOFT)
        step_lbl.move_to([0, -1.6, 0])

        # Cost meter
        cost_lbl = Text("Token cost per run:", font_size=20, color=SOFT)
        cost_lbl.move_to([-2.0, -2.8, 0])
        cost_val = Text("$$$", font_size=34, color=SPARK, weight=BOLD)
        cost_val.move_to([1.8, -2.8, 0])

        for grp in boxes:
            self.play(FadeIn(grp), run_time=0.3)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.3)
        self.wait(0.3)
        self.play(Create(loop_arrow), Write(step_lbl), run_time=0.8)
        self.wait(0.4)
        self.play(Write(cost_lbl), FadeIn(cost_val), run_time=0.6)
        self.wait(dur - 5.8)


class B02_ImagePruning(Scene):
    def construct(self):
        dur = 21.5

        title = Text("Resize. Prune. Cache.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Before bar
        before_lbl = Text("Before", font_size=20, color=SOFT, weight=BOLD)
        before_lbl.move_to([-4.5, 1.8, 0])
        before_bar = Rectangle(
            width=8.5, height=0.7, color=INK,
            fill_color=INK, fill_opacity=0.85, stroke_width=0
        ).move_to([-0.75, 1.8, 0])
        before_val = Text("~180,000 tokens", font_size=18, color=PAGE, weight=BOLD)
        before_val.move_to(before_bar)

        # After resize
        resize_lbl = Text("After resize", font_size=20, color=SOFT)
        resize_lbl.move_to([-4.5, 0.7, 0])
        resize_bar = Rectangle(
            width=5.0, height=0.7, color=SOFT,
            fill_color=SOFT, fill_opacity=0.8, stroke_width=0
        ).move_to([-2.5, 0.7, 0])
        resize_val = Text("~60,000 tokens", font_size=18, color=PAGE)
        resize_val.move_to(resize_bar)

        # After prune
        prune_lbl = Text("After prune", font_size=20, color=SOFT)
        prune_lbl.move_to([-4.5, -0.4, 0])
        prune_bar = Rectangle(
            width=2.5, height=0.7, color=SOFT,
            fill_color=SOFT, fill_opacity=0.6, stroke_width=0
        ).move_to([-3.75, -0.4, 0])
        prune_val = Text("~20,000", font_size=18, color=INK)
        prune_val.next_to(prune_bar, RIGHT, buff=0.2)

        # Cache annotation
        cache_box = Rectangle(
            width=4.5, height=0.9, color=SPARK,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([0, -1.6, 0])
        cache_txt = Text("System prompt cached — free on repeat calls", font_size=17, color=SPARK)
        cache_txt.move_to(cache_box)

        verdict = Text("Same task. A fraction of the cost.", font_size=21, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)

        self.play(Write(before_lbl), FadeIn(before_bar), Write(before_val), run_time=0.7)
        self.wait(0.3)
        self.play(Write(resize_lbl), FadeIn(resize_bar), Write(resize_val), run_time=0.7)
        self.wait(0.3)
        self.play(Write(prune_lbl), FadeIn(prune_bar), Write(prune_val), run_time=0.7)
        self.wait(0.4)
        self.play(Create(cache_box), Write(cache_txt), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 6.4)


class B03_BatchedCalls(Scene):
    def construct(self):
        dur = 22.3

        title = Text("Batch Calls. Record Everything.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        col_left = -4.0
        col_right = 2.5
        divider = Line(UP * 2.2, DOWN * 1.8, color=BORDER, stroke_width=1.5)
        self.add(divider)

        hdr_naive = Text("Naive", font_size=21, color=INK, weight=BOLD)
        hdr_naive.move_to([col_left, 2.0, 0])
        hdr_batch = Text("Batched", font_size=21, color=SPARK, weight=BOLD)
        hdr_batch.move_to([col_right, 2.0, 0])
        self.add(hdr_naive, hdr_batch)

        naive_steps = ["Click menu", "Wait", "Screenshot", "Observe", "Next step"]
        batch_steps = ["Click + declare\nexpected state", "Verify once", "Next step"]

        for i, s in enumerate(naive_steps):
            b = Rectangle(width=3.2, height=0.55, color=BORDER, fill_color=PAGE, fill_opacity=1, stroke_width=1.2)
            b.move_to([col_left, 1.2 - i * 0.7, 0])
            t = Text(s, font_size=16, color=SOFT)
            t.move_to(b)
            self.play(FadeIn(VGroup(b, t)), run_time=0.25)

        for i, s in enumerate(batch_steps):
            col = SPARK if i == 0 else INK
            b = Rectangle(width=3.8, height=0.7, color=SPARK if i == 0 else BORDER,
                          fill_color=PAGE, fill_opacity=1, stroke_width=1.6)
            b.move_to([col_right, 1.1 - i * 0.85, 0])
            t = Text(s, font_size=16, color=col)
            t.move_to(b)
            self.play(FadeIn(VGroup(b, t)), run_time=0.35)

        # Trajectory log
        traj_box = Rectangle(
            width=10.5, height=1.0, color=BORDER,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([0, -1.5, 0])
        traj_txt = Text("Trajectory log: {action, target, ts, screenshot_delta} per step — replay & audit", font_size=15, color=SOFT)
        traj_txt.move_to(traj_box)
        self.play(Create(traj_box), Write(traj_txt), run_time=0.7)

        verdict = Text("The demo has none of this. The production agent has all of it.", font_size=19, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 7.2)
