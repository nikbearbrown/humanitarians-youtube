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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 13",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_PipelineAccuracy(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Deployment Pipeline: Accuracy at Each Stage", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        stages = [
            ("Keras Float", 94.0, GREEN),
            ("SavedModel", 94.0, GREEN),
            ("TFLite Float", 93.5, GREEN),
            ("TFLite INT8", 91.0, ACC),
        ]

        n = len(stages)
        bar_w = 1.4
        gap = 0.6
        start_x = -(n * bar_w + (n - 1) * gap) / 2 + bar_w / 2
        acc_min = 88
        acc_max = 95
        bar_h_scale = 3.0

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        for i, (s, acc, col) in enumerate(stages):
            x = start_x + i * (bar_w + gap)
            norm = (acc - acc_min) / (acc_max - acc_min)
            h = norm * bar_h_scale

            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1
            ).move_to([x, -1.5 + h / 2, 0])
            lbl = Text(s, font_size=12, color=INK).move_to([x, -1.5 - 0.4, 0])
            val = Text(f"{acc}%", font_size=13, color=col).move_to([x, -1.5 + h + 0.25, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), FadeIn(val), run_time=0.6)

        gap_label = Text("3% gap introduced during INT8 conversion — nobody checked", font_size=14, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(gap_label))
        self.wait(1.5)


class B02_DivergenceBisect(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Bisection: Per-Layer Output Divergence", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Layer divergence (L2 distance float vs int8)
        layer_names = ["conv2d_0", "conv2d_1", "conv2d_2", "conv2d_3", "dense_0"]
        divergence = [0.02, 0.03, 0.04, 0.45, 0.05]  # spike at conv2d_3
        colors = [INK, INK, INK, ACC, INK]

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        n = len(layer_names)
        bar_w = 1.1
        gap = 0.4
        start_x = -(n * bar_w + (n - 1) * gap) / 2 + bar_w / 2
        max_div = 0.5

        for i, (name, div, col) in enumerate(zip(layer_names, divergence, colors)):
            x = start_x + i * (bar_w + gap)
            h = div / max_div * 3.5

            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1
            ).move_to([x, -1.5 + h / 2, 0])
            lbl = Text(name, font_size=11, color=INK).move_to([x, -1.5 - 0.35, 0])
            val = Text(f"{div:.2f}", font_size=12, color=col).move_to([x, -1.5 + h + 0.2, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), FadeIn(val), run_time=0.5)

        spike_label = Text("conv2d_3: spike → unsupported op fusion → CPU fallback", font_size=13, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(spike_label))
        self.wait(1.5)


class B03_CheckEveryHop(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Check at Every Hop — Not Just End-to-End", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        points = [
            ("End-to-end green test", "Hides silent precision failures", ACC),
            ("Per-stage accuracy check", "Shows where the drop occurs", GREEN),
            ("Per-op bisection", "Identifies the exact leaking op", GREEN),
            ("CMSIS-NN support check", "Flags CPU fallback candidates", GREEN),
        ]

        y_start = 0.9
        for i, (check, result, col) in enumerate(points):
            row = VGroup(
                Text(check, font_size=15, color=INK),
                Text("→", font_size=15, color=SOFT),
                Text(result, font_size=15, color=col),
            ).arrange(RIGHT, buff=0.4).shift(UP * (y_start - i * 0.85))
            self.play(FadeIn(row), run_time=0.5)

        lesson = Text("Don't trust end-to-end green — bisect every conversion step", font_size=15, color=ACC).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(lesson))
        self.wait(1.5)
