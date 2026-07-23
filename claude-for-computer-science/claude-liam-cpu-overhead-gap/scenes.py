"""scenes.py — Manim for claude-liam-cpu-overhead-gap. Source: embedded-ai Ch. 08"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_CpuBar(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("CPU on Matrix Multiply", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        bar_w = 7.0
        bar_h = 1.4
        y_cpu = 0.5

        # Full bar background
        bg_bar = Rectangle(width=bar_w, height=bar_h, fill_color=SOFT, fill_opacity=0.2, stroke_width=0)
        bg_bar.move_to([0, y_cpu, 0])
        self.play(FadeIn(bg_bar))

        # Arithmetic portion: 30%
        arith_w = bar_w * 0.30
        arith_bar = Rectangle(width=arith_w, height=bar_h, fill_color=SOFT, fill_opacity=0.85, stroke_width=0)
        arith_bar.move_to([-bar_w/2 + arith_w/2, y_cpu, 0])

        # Overhead portion: 70%
        over_w = bar_w * 0.70
        over_bar = Rectangle(width=over_w, height=bar_h, fill_color=GHOST, fill_opacity=0.5, stroke_width=0)
        over_bar.move_to([-bar_w/2 + arith_w + over_w/2, y_cpu, 0])

        self.play(GrowFromEdge(arith_bar, LEFT), run_time=0.7)
        self.play(GrowFromEdge(over_bar, LEFT), run_time=1.0)

        lbl_arith = Text("30%\nArithmetic", font_size=18, color=INK)
        lbl_arith.move_to(arith_bar.get_center())
        lbl_over = Text("70%\nOverhead", font_size=18, color=INK)
        lbl_over.move_to(over_bar.get_center())
        self.play(FadeIn(lbl_arith), FadeIn(lbl_over))

        note = Text("fetch · cache · pipeline · branch prediction", font_size=15, color=SOFT)
        note.next_to(bg_bar, DOWN, buff=0.35)
        self.play(FadeIn(note))

        util_lbl = Text("Arithmetic utilization: 30%", font_size=20, color=SOFT)
        util_lbl.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(util_lbl))

        self.wait(1)


class B02_NpuBar(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("NPU on Same Operation", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        bar_w = 7.0
        bar_h = 1.4
        y_npu = 0.5

        bg_bar = Rectangle(width=bar_w, height=bar_h, fill_color=SOFT, fill_opacity=0.2, stroke_width=0)
        bg_bar.move_to([0, y_npu, 0])
        self.play(FadeIn(bg_bar))

        # Arithmetic portion: 90% — terracotta (useful work)
        arith_w = bar_w * 0.90
        arith_bar = Rectangle(width=arith_w, height=bar_h, fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        arith_bar.move_to([-bar_w/2 + arith_w/2, y_npu, 0])

        # Overhead: 10%
        over_w = bar_w * 0.10
        over_bar = Rectangle(width=over_w, height=bar_h, fill_color=GHOST, fill_opacity=0.5, stroke_width=0)
        over_bar.move_to([-bar_w/2 + arith_w + over_w/2, y_npu, 0])

        self.play(GrowFromEdge(arith_bar, LEFT), run_time=1.0)
        self.play(GrowFromEdge(over_bar, LEFT), run_time=0.4)

        lbl_arith = Text("90%\nArithmetic", font_size=18, color=BG, weight="BOLD")
        lbl_arith.move_to(arith_bar.get_center())
        lbl_over = Text("10%", font_size=14, color=INK)
        lbl_over.move_to(over_bar.get_center())
        self.play(FadeIn(lbl_arith), FadeIn(lbl_over))

        note = Text("MAC array · fixed datapath · no branch prediction", font_size=15, color=SOFT)
        note.next_to(bg_bar, DOWN, buff=0.35)
        self.play(FadeIn(note))

        util_lbl = Text("Arithmetic utilization: 90%", font_size=20, color=ACC)
        util_lbl.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(util_lbl))

        self.wait(1)


class B03_Comparison(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Same MACs — 3× Higher Utilization", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        bar_w = 5.5
        bar_h = 1.1
        spacing = 1.5

        y_cpu = 0.8
        y_npu = -0.8

        # CPU bar
        cpu_arith = Rectangle(width=bar_w * 0.30, height=bar_h, fill_color=SOFT, fill_opacity=0.85, stroke_width=0)
        cpu_arith.move_to([-bar_w/2 + bar_w*0.30/2, y_cpu, 0])
        cpu_over = Rectangle(width=bar_w * 0.70, height=bar_h, fill_color=GHOST, fill_opacity=0.4, stroke_width=0)
        cpu_over.move_to([-bar_w/2 + bar_w*0.30 + bar_w*0.70/2, y_cpu, 0])
        cpu_lbl = Text("CPU  30% arithmetic", font_size=18, color=INK)
        cpu_lbl.next_to(cpu_arith.get_left(), LEFT, buff=0.15).shift(RIGHT * 0.5)
        cpu_lbl.move_to([-4.2, y_cpu, 0])

        # NPU bar
        npu_arith = Rectangle(width=bar_w * 0.90, height=bar_h, fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        npu_arith.move_to([-bar_w/2 + bar_w*0.90/2, y_npu, 0])
        npu_over = Rectangle(width=bar_w * 0.10, height=bar_h, fill_color=GHOST, fill_opacity=0.4, stroke_width=0)
        npu_over.move_to([-bar_w/2 + bar_w*0.90 + bar_w*0.10/2, y_npu, 0])
        npu_lbl = Text("NPU  90% arithmetic", font_size=18, color=ACC)
        npu_lbl.move_to([-4.2, y_npu, 0])

        self.play(
            GrowFromEdge(cpu_arith, LEFT), GrowFromEdge(cpu_over, LEFT),
            GrowFromEdge(npu_arith, LEFT), GrowFromEdge(npu_over, LEFT),
            run_time=1.0
        )
        self.play(FadeIn(cpu_lbl), FadeIn(npu_lbl))

        # Annotation
        arrow = Arrow(start=[2.5, y_cpu, 0], end=[2.5, y_npu, 0], color=ACC, stroke_width=2)
        ratio = Text("3× utilization", font_size=20, color=ACC, weight="BOLD")
        ratio.next_to(arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow), FadeIn(ratio))

        caption = Text("The NPU doesn't compute faster — it wastes less.", font_size=16, color=SOFT)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption))

        self.wait(1.2)
