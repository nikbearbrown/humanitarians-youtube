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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_LatencyStages(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Latency Decomposed: Four Pipeline Stages", font_size=25, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        stages = ["Weight Load", "Compute\n(MACs)", "Mem Move\n(Activations)", "Overhead"]
        times = [8, 22, 5, 2]
        colors = [INK, ACC, INK, SOFT]  # Compute dominates → terracotta
        total = sum(times)

        axes_line = Line(LEFT * 4.0, RIGHT * 4.0, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        bar_w = 1.4
        gap = 0.4
        n = len(stages)
        start_x = -(n * bar_w + (n - 1) * gap) / 2 + bar_w / 2
        max_t = 25
        bar_h_scale = 3.0

        for i, (s, t, col) in enumerate(zip(stages, times, colors)):
            x = start_x + i * (bar_w + gap)
            h = t / max_t * bar_h_scale
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1
            ).move_to([x, -1.5 + h / 2, 0])
            lbl = Text(s, font_size=13, color=INK).move_to([x, -1.5 - 0.4, 0])
            val = Text(f"{t}ms", font_size=13, color=col).move_to([x, -1.5 + h + 0.25, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), FadeIn(val), run_time=0.6)

        total_label = Text(f"Total: {total}ms  |  Bottleneck: Compute (22ms)", font_size=16, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(total_label))
        self.wait(1.5)


class B02_Int8Rerun(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("INT8 Re-Run: Weight Load + Compute Shrink", font_size=25, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        stages = ["Weight Load", "Compute", "Mem Move", "Overhead"]
        fp32_times = [8, 22, 5, 2]
        int8_times = [2, 10, 5, 2]
        total_fp32 = sum(fp32_times)
        total_int8 = sum(int8_times)

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        bar_w = 0.9
        gap = 0.7
        n = len(stages)
        start_x = -(n * (bar_w * 2 + 0.15) + (n - 1) * gap) / 2 + bar_w
        max_t = 25
        bar_h_scale = 3.0

        for i, (s, ft, it) in enumerate(zip(stages, fp32_times, int8_times)):
            x_c = start_x + i * (bar_w * 2 + 0.15 + gap)
            x_fp32 = x_c - bar_w / 2 - 0.05
            x_int8 = x_c + bar_w / 2 + 0.05

            fh = ft / max_t * bar_h_scale
            ih = it / max_t * bar_h_scale

            fp32_bar = Rectangle(
                width=bar_w, height=fh,
                fill_color=SOFT, fill_opacity=0.5,
                stroke_color=SOFT, stroke_width=1
            ).move_to([x_fp32, -1.5 + fh / 2, 0])

            changed = it != ft
            int8_bar = Rectangle(
                width=bar_w, height=ih,
                fill_color=GREEN if changed else INK,
                fill_opacity=0.85, stroke_width=1
            ).move_to([x_int8, -1.5 + ih / 2, 0])

            lbl = Text(s, font_size=12, color=INK).move_to([x_c, -1.5 - 0.35, 0])
            val_fp32 = Text(f"{ft}ms", font_size=11, color=SOFT).move_to([x_fp32, -1.5 + fh + 0.2, 0])
            val_int8 = Text(f"{it}ms", font_size=11, color=GREEN if changed else INK).move_to([x_int8, -1.5 + ih + 0.2, 0])

            self.play(
                GrowFromEdge(fp32_bar, DOWN),
                GrowFromEdge(int8_bar, DOWN),
                FadeIn(lbl), FadeIn(val_fp32), FadeIn(val_int8),
                run_time=0.55
            )

        comp = Text(f"FP32: {total_fp32}ms  →  INT8: {total_int8}ms  (right optimization, right stage)", font_size=14, color=GREEN).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(comp))
        self.wait(1.5)


class B03_OptimizeRule(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Rule: Optimize the Bottleneck, Not the Others", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        rules = [
            ("Weight Load bottleneck", "Quantization (INT8/INT4)", GREEN),
            ("Compute bottleneck", "SIMD kernels / faster CPU", INK),
            ("Memory Move bottleneck", "Tiling + activation compression", INK),
            ("Overhead bottleneck", "Reduce framework calls", SOFT),
        ]

        y_start = 1.0
        for i, (problem, solution, col) in enumerate(rules):
            row = VGroup(
                Text(problem, font_size=16, color=INK),
                Text("→", font_size=16, color=ACC),
                Text(solution, font_size=16, color=col),
            ).arrange(RIGHT, buff=0.4).shift(UP * (y_start - i * 0.85))
            self.play(FadeIn(row), run_time=0.5)

        lesson = Text("Identify the stage first. Then pick the tool.", font_size=17, color=ACC).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(lesson))
        self.wait(1.5)
