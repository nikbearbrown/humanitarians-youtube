"""scenes.py — Manim for claude-liam-accelerator-routing. Source: embedded-ai Ch. 08"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_OpStreamFast(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("80% of Ops: NPU Fast Lane", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # NPU lane
        lane_label = Text("NPU lane  (conv, matmul, pool)", font_size=16, color=SOFT)
        lane_label.move_to([-1, 1.0, 0])
        self.play(FadeIn(lane_label))

        # Draw a series of small op squares flowing into NPU box
        npu_box = Rectangle(width=2.5, height=1.2, color=SOFT, stroke_width=2, fill_opacity=0)
        npu_box.move_to([3.0, 0.0, 0])
        npu_lbl = Text("NPU\n10×", font_size=18, color=SOFT, weight="BOLD")
        npu_lbl.move_to(npu_box.get_center())
        self.play(FadeIn(npu_box), FadeIn(npu_lbl))

        op_colors = [SOFT] * 8
        ops = VGroup()
        for i, c in enumerate(op_colors):
            sq = Square(side_length=0.45, fill_color=c, fill_opacity=0.7, stroke_width=0)
            sq.move_to([-4.5 + i * 0.7, 0.0, 0])
            ops.add(sq)

        self.play(FadeIn(ops), run_time=0.5)
        self.play(ops.animate.move_to([1.2, 0.0, 0]), run_time=1.2)

        arrow = Arrow(start=[2.0, 0.0, 0], end=npu_box.get_left(), color=SOFT, stroke_width=2, buff=0.1)
        self.play(GrowArrow(arrow))

        fast_lbl = Text("Fast — milliseconds per op", font_size=16, color=SOFT)
        fast_lbl.to_edge(DOWN, buff=0.9)
        pct_lbl = Text("80% of total MACs", font_size=18, color=INK)
        pct_lbl.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(fast_lbl), FadeIn(pct_lbl))

        self.wait(1)


class B02_FallbackQueue(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("20% Fallback: CPU Bottleneck", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Slow CPU lane
        cpu_box = Rectangle(width=2.5, height=1.2, color=ACC, stroke_width=2.5, fill_opacity=0)
        cpu_box.move_to([3.0, 0.2, 0])
        cpu_lbl = Text("CPU\nfallback", font_size=18, color=ACC, weight="BOLD")
        cpu_lbl.move_to(cpu_box.get_center())
        self.play(FadeIn(cpu_box), FadeIn(cpu_lbl))

        # Fallback ops (softmax, reshape) queuing
        op_labels = ["softmax", "reshape", "gelu", "custom"]
        ops = VGroup()
        for i, lbl in enumerate(op_labels):
            sq = Square(side_length=0.55, fill_color=ACC, fill_opacity=0.7, stroke_width=0)
            sq.move_to([-4.0 + i * 0.8, 0.2, 0])
            ops.add(sq)

        self.play(FadeIn(ops))

        # Queue stacking up
        queue_ops = VGroup()
        for i in range(4):
            sq = Square(side_length=0.55, fill_color=ACC, fill_opacity=0.5, stroke_width=1, stroke_color=ACC)
            sq.move_to([0.8, 0.2 + i * 0.6, 0])
            queue_ops.add(sq)

        self.play(ops.animate.move_to([0.3, 0.2, 0]), run_time=0.8)
        self.play(FadeIn(queue_ops), run_time=0.6)

        slow_lbl = Text("Queue backing up — NPU sits idle", font_size=16, color=ACC)
        slow_lbl.to_edge(DOWN, buff=0.9)
        pct_lbl = Text("20% of MACs, but owns the timeline", font_size=18, color=INK)
        pct_lbl.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(slow_lbl), FadeIn(pct_lbl))

        self.wait(1)


class B03_SpeedupWaterfall(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("10× Potential → 3.57× Reality", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Bar chart: potential vs actual speedup
        bar_w = 1.8
        max_h = 3.5

        h_10x = max_h
        h_357 = (3.57 / 10.0) * max_h

        bar_potential = Rectangle(width=bar_w, height=h_10x, fill_color=SOFT, fill_opacity=0.5, stroke_width=0)
        bar_potential.move_to([-2.0, h_10x/2 - 2.0, 0])

        bar_actual = Rectangle(width=bar_w, height=h_357, fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        bar_actual.move_to([2.0, h_357/2 - 2.0, 0])

        lbl_pot = Text("10×\nPotential", font_size=18, color=INK)
        lbl_pot.next_to(bar_potential, DOWN, buff=0.2)
        lbl_act = Text("3.57×\nActual", font_size=18, color=ACC, weight="BOLD")
        lbl_act.next_to(bar_actual, DOWN, buff=0.2)

        self.play(GrowFromEdge(bar_potential, DOWN), run_time=0.7)
        self.play(GrowFromEdge(bar_actual, DOWN), run_time=0.7)
        self.play(FadeIn(lbl_pot))
        self.play(FadeIn(lbl_act))

        formula = Text("1 / (0.8/10 + 0.2/1) = 3.57×", font_size=18, color=SOFT)
        formula.to_edge(DOWN, buff=0.8)
        note = Text("The unaccelerated 20% owns the ceiling.", font_size=16, color=INK)
        note.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(formula))
        self.play(FadeIn(note))

        self.wait(1.2)
