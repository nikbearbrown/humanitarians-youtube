from manim import *
import numpy as np

BG = ManimColor("#FAF9F5")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")
GREEN = ManimColor("#4A7C59")


def source_credit():
    return Text(
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_RooflineAxes(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("The Roofline Model", font_size=28, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 110, 20],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=True,
        ).shift(DOWN * 0.3)

        x_label = Text("arithmetic intensity (FLOP/byte)", font_size=13, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("attainable GFLOP/s", font_size=13, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Memory bandwidth slope: bandwidth = 8 GB/s → slope = 8 GFLOP/s per FLOP/byte
        bandwidth = 8.0  # GB/s
        peak_gflops = 80.0
        ridge_x = peak_gflops / bandwidth  # = 10

        mem_slope = axes.plot(
            lambda x: min(bandwidth * x, peak_gflops),
            x_range=[0, 25], color=INK, stroke_width=2.5
        )

        # Ceiling line
        ceil_line = axes.plot(
            lambda x: peak_gflops,
            x_range=[ridge_x, 25], color=SOFT, stroke_width=2, stroke_opacity=0.6
        )

        ridge_dot = Dot(axes.c2p(ridge_x, peak_gflops), color=ACC, radius=0.1)
        ridge_label = Text(f"ridge @ {ridge_x:.0f} FLOP/byte", font_size=14, color=ACC).next_to(ridge_dot, UR, buff=0.15)

        mem_label = Text("memory-bound", font_size=13, color=SOFT).shift(LEFT * 1.8 + DOWN * 0.3)
        compute_label = Text("compute-bound", font_size=13, color=SOFT).shift(RIGHT * 2.0 + UP * 1.2)

        self.play(Create(mem_slope), run_time=1.5)
        self.play(Create(ceil_line))
        self.play(FadeIn(ridge_dot), FadeIn(ridge_label))
        self.play(FadeIn(mem_label), FadeIn(compute_label))
        self.wait(1.5)


class B02_MemoryBound(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Model Operating Point — Memory-Bound", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 110, 20],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=True,
        ).shift(DOWN * 0.3)

        x_label = Text("arithmetic intensity (FLOP/byte)", font_size=13, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("attainable GFLOP/s", font_size=13, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)

        bandwidth = 8.0
        peak_gflops = 80.0
        ridge_x = peak_gflops / bandwidth

        roofline = axes.plot(
            lambda x: min(bandwidth * x, peak_gflops),
            x_range=[0, 25], color=SOFT, stroke_width=2
        )

        # FP32 model: 0.8 FLOP/byte (memory-bound, left of ridge)
        model_x = 0.8
        model_y = bandwidth * model_x  # 6.4 GFLOP/s

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))
        self.play(Create(roofline))

        model_dot = Dot(axes.c2p(model_x, model_y), color=ACC, radius=0.12)
        model_label = Text("FP32 model\n0.8 FLOP/byte", font_size=14, color=ACC).next_to(model_dot, RIGHT, buff=0.2)

        # Memory-bound region shading
        mem_region = Polygon(
            axes.c2p(0, 0),
            axes.c2p(ridge_x, peak_gflops),
            axes.c2p(0, peak_gflops),
            fill_color=ACC, fill_opacity=0.08,
            stroke_width=0
        )

        mem_label = Text("MEMORY-BOUND", font_size=16, color=ACC).shift(LEFT * 2.5 + UP * 0.5)
        note = Text("More compute won't help — optimize memory access", font_size=14, color=SOFT).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(mem_region))
        self.play(FadeIn(model_dot), FadeIn(model_label))
        self.play(FadeIn(mem_label), FadeIn(note))
        self.wait(1.5)


class B03_Int8Shift(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("INT8 Shifts the Operating Point Right", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 110, 20],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=True,
        ).shift(DOWN * 0.3)

        x_label = Text("arithmetic intensity (FLOP/byte)", font_size=13, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("attainable GFLOP/s", font_size=13, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)

        bandwidth = 8.0
        peak_gflops = 80.0

        roofline = axes.plot(
            lambda x: min(bandwidth * x, peak_gflops),
            x_range=[0, 25], color=SOFT, stroke_width=2
        )

        fp32_x = 0.8
        fp32_y = bandwidth * fp32_x
        int8_x = 3.2  # 4x more FLOP/byte (weights 4x smaller)
        int8_y = min(bandwidth * int8_x, peak_gflops)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))
        self.play(Create(roofline))

        fp32_dot = Dot(axes.c2p(fp32_x, fp32_y), color=SOFT, radius=0.1)
        fp32_label = Text("FP32", font_size=13, color=SOFT).next_to(fp32_dot, DOWN, buff=0.15)
        self.play(FadeIn(fp32_dot), FadeIn(fp32_label))

        int8_dot = Dot(axes.c2p(int8_x, int8_y), color=ACC, radius=0.12)
        int8_label = Text("INT8\n(4x fewer bytes)", font_size=13, color=ACC).next_to(int8_dot, UR, buff=0.15)

        arrow = Arrow(
            axes.c2p(fp32_x, fp32_y),
            axes.c2p(int8_x, int8_y),
            color=ACC, buff=0.12, stroke_width=2
        )
        self.play(Create(arrow), FadeIn(int8_dot), FadeIn(int8_label))

        note = Text("Quantization → fewer bytes moved → higher arithmetic intensity", font_size=14, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note))
        self.wait(1.5)
