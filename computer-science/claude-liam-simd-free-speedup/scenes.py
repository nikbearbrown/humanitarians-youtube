"""scenes.py — Manim for claude-liam-simd-free-speedup. Source: embedded-ai Ch. 06"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_ScalarLane(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Scalar: 4 Values, 4 Clocks", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Show four sequential operations, one per clock tick
        box_w = 1.4
        box_h = 1.0
        spacing = 1.8
        start_x = -3.6
        y = 0.3

        clock_labels = ["Clock 1", "Clock 2", "Clock 3", "Clock 4"]
        value_labels = ["a₁×b₁", "a₂×b₂", "a₃×b₃", "a₄×b₄"]

        for i, (clk, val) in enumerate(zip(clock_labels, value_labels)):
            x = start_x + i * spacing
            box = Rectangle(width=box_w, height=box_h,
                           fill_color=SOFT, fill_opacity=0.4,
                           stroke_width=2, stroke_color=INK)
            box.move_to([x, y, 0])
            val_t = Text(val, font_size=14, color=INK)
            val_t.move_to(box.get_center())
            clk_t = Text(clk, font_size=11, color=GHOST)
            clk_t.next_to(box, DOWN, buff=0.1)
            self.play(FadeIn(box), FadeIn(val_t), FadeIn(clk_t), run_time=0.4)

        # Timeline arrow
        timeline = Arrow([-4.5, -0.8, 0], [4.5, -0.8, 0], color=INK, stroke_width=2)
        time_label = Text("time →", font_size=13, color=INK)
        time_label.next_to(timeline, RIGHT, buff=0.1)
        self.play(GrowArrow(timeline), FadeIn(time_label))

        summary = Text("4 multiply-accumulates = 4 clocks", font_size=15, color=INK)
        summary.move_to([0, -2.2, 0])
        self.play(FadeIn(summary))
        self.wait(1)


class B02_SimdLane(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("SIMD: 4 Values, 1 Clock", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Show four values packed into one 32-bit register
        reg_y = 0.8
        total_w = 5.6
        lane_w = total_w / 4
        lane_h = 1.0
        lane_colors = [SOFT, SOFT, SOFT, SOFT]
        lane_labels = ["int8\na₁", "int8\na₂", "int8\na₃", "int8\na₄"]

        reg_frame = Rectangle(width=total_w, height=lane_h,
                             fill_color=GHOST, fill_opacity=0.15,
                             stroke_width=2, stroke_color=INK)
        reg_frame.move_to([0, reg_y, 0])
        reg_title = Text("32-bit register", font_size=13, color=INK)
        reg_title.next_to(reg_frame, UP, buff=0.1)
        self.play(FadeIn(reg_frame), FadeIn(reg_title))

        lanes = []
        for i, (color, lbl) in enumerate(zip(lane_colors, lane_labels)):
            x = -total_w / 2 + lane_w / 2 + i * lane_w
            lane = Rectangle(width=lane_w - 0.05, height=lane_h - 0.05,
                            fill_color=color, fill_opacity=0.6, stroke_width=1, stroke_color=INK)
            lane.move_to([x, reg_y, 0])
            lane_t = Text(lbl, font_size=11, color=INK)
            lane_t.move_to(lane.get_center())
            lanes.append(lane)
            self.play(FadeIn(lane), FadeIn(lane_t), run_time=0.3)

        # Single instruction arrow
        instr_arrow = Arrow([0, 0.1, 0], [0, -0.9, 0], color=ACC, stroke_width=3)
        instr_label = Text("SIMD multiply-accumulate\n1 instruction", font_size=13, color=ACC)
        instr_label.next_to(instr_arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(instr_arrow), FadeIn(instr_label))

        # Result lane
        result_frame = Rectangle(width=total_w, height=lane_h,
                                fill_color=ACC, fill_opacity=0.25,
                                stroke_width=2, stroke_color=ACC)
        result_frame.move_to([0, -1.5, 0])
        result_label = Text("4 results  —  1 clock", font_size=14, color=ACC, weight=BOLD)
        result_label.move_to(result_frame.get_center())
        self.play(FadeIn(result_frame), FadeIn(result_label))

        summary = Text("Same arithmetic. One quarter the time.", font_size=15, color=INK)
        summary.move_to([0, -2.8, 0])
        self.play(FadeIn(summary))
        self.wait(1)


class B03_SpeedupBar(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("4× Free Speedup", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Two horizontal bars: scalar (4 clocks) and SIMD (1 clock)
        bar_h = 0.8
        max_w = 5.0
        y_scalar = 0.5
        y_simd = -0.5

        scalar_bar = Rectangle(width=max_w, height=bar_h,
                              fill_color=SOFT, fill_opacity=0.6,
                              stroke_width=1, stroke_color=INK)
        scalar_bar.move_to([-0.5, y_scalar, 0])
        scalar_label = Text("Scalar: 4 clocks", font_size=14, color=INK)
        scalar_label.next_to(scalar_bar, LEFT, buff=0.15)

        simd_bar = Rectangle(width=max_w / 4, height=bar_h,
                            fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        simd_bar.move_to([-0.5 - (max_w - max_w / 4) / 2, y_simd, 0])
        simd_label = Text("SIMD: 1 clock", font_size=14, color=ACC, weight=BOLD)
        simd_label.next_to(scalar_bar, LEFT, buff=0.15)
        simd_label.move_to([-4.0, y_simd, 0])

        self.play(GrowFromEdge(scalar_bar, LEFT), FadeIn(scalar_label))
        self.play(GrowFromEdge(simd_bar, LEFT), FadeIn(simd_label))

        # 4× bracket
        brace = BraceBetweenPoints(
            [simd_bar.get_right()[0], y_simd, 0],
            [scalar_bar.get_right()[0], y_scalar, 0],
            direction=RIGHT
        )
        brace_label = Text("4×", font_size=22, color=ACC, weight=BOLD)
        brace_label.next_to(brace, RIGHT, buff=0.15)
        self.play(Create(brace), FadeIn(brace_label))

        note = Text("Same chip. Same clock. One compile flag.", font_size=15, color=INK)
        note.move_to([0, -2.2, 0])
        self.play(FadeIn(note))
        self.wait(1)
