"""scenes.py — Manim for claude-liam-latency-gap. Source: embedded-ai Ch. 04"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_InitialGap(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("The Gap", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Draw latency axis
        axis_y = -2.0
        axis = Line([-5.0, axis_y, 0], [5.0, axis_y, 0], color=INK, stroke_width=2)
        self.play(Create(axis))

        axis_label = Text("Latency (ms)", font_size=16, color=INK)
        axis_label.next_to(axis, DOWN, buff=0.2)
        self.play(FadeIn(axis_label))

        # Target line at 100 ms (normalized position)
        # Scale: 0 ms at -5, 1400 ms at 5 => scale = 10/1400
        def ms_to_x(ms):
            return -5.0 + (ms / 1400.0) * 10.0

        target_x = ms_to_x(100)
        target_line = DashedLine(
            [target_x, axis_y - 0.2, 0],
            [target_x, 2.0, 0],
            color=SOFT, dash_length=0.15, stroke_width=2
        )
        target_label = Text("100 ms\ntarget", font_size=14, color=SOFT)
        target_label.next_to(target_line, UP, buff=0.1)
        self.play(Create(target_line), FadeIn(target_label))

        # Spec bar (367 ms)
        spec_x = ms_to_x(367)
        spec_bar = Rectangle(width=spec_x - (-5.0), height=0.5,
                             fill_color=SOFT, fill_opacity=0.7, stroke_width=0)
        spec_bar.move_to([(spec_x + (-5.0)) / 2, axis_y + 0.25, 0])
        spec_label = Text("Spec: 367 ms", font_size=14, color=SOFT)
        spec_label.next_to(spec_bar, UP, buff=0.1)
        self.play(GrowFromEdge(spec_bar, LEFT), FadeIn(spec_label))

        # Measured bar (1200 ms) — in ACC
        meas_x = ms_to_x(1200)
        meas_bar = Rectangle(width=meas_x - (-5.0), height=0.5,
                              fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        meas_bar.move_to([(meas_x + (-5.0)) / 2, axis_y - 0.45, 0])
        meas_label = Text("Measured: 1,200 ms", font_size=14, color=ACC)
        meas_label.next_to(meas_bar, DOWN, buff=0.1)
        self.play(GrowFromEdge(meas_bar, LEFT), FadeIn(meas_label))

        # Gap annotation
        gap = DoubleArrow([target_x, axis_y - 1.1, 0], [meas_x, axis_y - 1.1, 0],
                          color=ACC, stroke_width=2, buff=0)
        gap_label = Text("The gap", font_size=13, color=ACC)
        gap_label.next_to(gap, DOWN, buff=0.1)
        self.play(Create(gap), FadeIn(gap_label))
        self.wait(1)


class B02_SimdFix(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Fix 1: SIMD Kernels", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axis_y = -1.8

        def ms_to_x(ms):
            return -5.0 + (ms / 1400.0) * 10.0

        target_x = ms_to_x(100)
        target_line = DashedLine(
            [target_x, axis_y - 0.2, 0],
            [target_x, 2.0, 0],
            color=SOFT, dash_length=0.15, stroke_width=2
        )
        target_label = Text("100 ms", font_size=13, color=SOFT)
        target_label.next_to(target_line, UP, buff=0.1)
        self.add(target_line, target_label)

        # Before bar: 1200 ms
        before_x = ms_to_x(1200)
        before_bar = Rectangle(width=before_x - (-5.0), height=0.5,
                               fill_color=SOFT, fill_opacity=0.4, stroke_width=1, stroke_color=INK)
        before_bar.move_to([(before_x + (-5.0)) / 2, axis_y + 0.25, 0])
        before_label = Text("Before: 1,200 ms", font_size=14, color=INK)
        before_label.next_to(before_bar, UP, buff=0.1)
        self.play(GrowFromEdge(before_bar, LEFT), FadeIn(before_label))

        # After bar: 400 ms (terracotta = progress)
        after_x = ms_to_x(400)
        after_bar = Rectangle(width=after_x - (-5.0), height=0.5,
                              fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        after_bar.move_to([(after_x + (-5.0)) / 2, axis_y - 0.45, 0])
        after_label = Text("After SIMD: ~400 ms", font_size=14, color=ACC)
        after_label.next_to(after_bar, DOWN, buff=0.1)
        self.play(GrowFromEdge(after_bar, LEFT), FadeIn(after_label))

        note = Text("4 × int8 per instruction → 3× faster compute", font_size=14, color=INK)
        note.move_to([0, -2.8, 0])
        self.play(FadeIn(note))
        self.wait(1)


class B03_MemorySpillFix(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Fix 2: Stop Memory Spill", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axis_y = -1.8

        def ms_to_x(ms):
            return -5.0 + (ms / 1400.0) * 10.0

        target_x = ms_to_x(100)
        target_line = DashedLine(
            [target_x, axis_y - 0.2, 0],
            [target_x, 2.0, 0],
            color=SOFT, dash_length=0.15, stroke_width=2
        )
        target_label = Text("100 ms", font_size=13, color=SOFT)
        target_label.next_to(target_line, UP, buff=0.1)
        self.add(target_line, target_label)

        # State after fix 1: 400 ms
        prev_x = ms_to_x(400)
        prev_bar = Rectangle(width=prev_x - (-5.0), height=0.5,
                             fill_color=SOFT, fill_opacity=0.4, stroke_width=1, stroke_color=INK)
        prev_bar.move_to([(prev_x + (-5.0)) / 2, axis_y + 0.25, 0])
        prev_label = Text("After SIMD: 400 ms", font_size=14, color=INK)
        prev_label.next_to(prev_bar, UP, buff=0.1)
        self.play(GrowFromEdge(prev_bar, LEFT), FadeIn(prev_label))

        # After fix 2: 200 ms
        after_x = ms_to_x(200)
        after_bar = Rectangle(width=after_x - (-5.0), height=0.5,
                              fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        after_bar.move_to([(after_x + (-5.0)) / 2, axis_y - 0.45, 0])
        after_label = Text("Fix mem spill: ~200 ms", font_size=14, color=ACC)
        after_label.next_to(after_bar, DOWN, buff=0.1)
        self.play(GrowFromEdge(after_bar, LEFT), FadeIn(after_label))

        note = Text("Activations in SRAM, not external flash → 2× memory bandwidth", font_size=13, color=INK)
        note.move_to([0, -2.8, 0])
        self.play(FadeIn(note))
        self.wait(1)


class B04_Int8Fix(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Fix 3: Int8 Quantization", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axis_y = -1.8

        def ms_to_x(ms):
            return -5.0 + (ms / 1400.0) * 10.0

        target_x = ms_to_x(100)
        target_line = DashedLine(
            [target_x, axis_y - 0.2, 0],
            [target_x, 2.0, 0],
            color=ACC, dash_length=0.15, stroke_width=2
        )
        target_label = Text("100 ms target", font_size=13, color=ACC)
        target_label.next_to(target_line, UP, buff=0.1)
        self.add(target_line, target_label)

        # State after fix 2: 200 ms
        prev_x = ms_to_x(200)
        prev_bar = Rectangle(width=prev_x - (-5.0), height=0.5,
                             fill_color=SOFT, fill_opacity=0.4, stroke_width=1, stroke_color=INK)
        prev_bar.move_to([(prev_x + (-5.0)) / 2, axis_y + 0.25, 0])
        prev_label = Text("After mem fix: 200 ms", font_size=14, color=INK)
        prev_label.next_to(prev_bar, UP, buff=0.1)
        self.play(GrowFromEdge(prev_bar, LEFT), FadeIn(prev_label))

        # After int8: 45 ms — under the target
        after_x = ms_to_x(45)
        after_bar = Rectangle(width=after_x - (-5.0), height=0.5,
                              fill_color=ACC, fill_opacity=0.85, stroke_width=0)
        after_bar.move_to([(after_x + (-5.0)) / 2, axis_y - 0.45, 0])
        after_label = Text("After int8: 45 ms", font_size=14, color=ACC)
        after_label.next_to(after_bar, DOWN, buff=0.1)
        self.play(GrowFromEdge(after_bar, LEFT), FadeIn(after_label))

        # Under-target celebration
        check = Text("Under target.", font_size=18, color=ACC, weight=BOLD)
        check.move_to([0, -2.8, 0])
        self.play(FadeIn(check))
        self.wait(1)
