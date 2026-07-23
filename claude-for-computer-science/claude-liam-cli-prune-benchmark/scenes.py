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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 12",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


def make_metric_bar(label, value, max_val, x_pos, color, bar_w=1.4, bar_h_scale=3.0):
    h = value / max_val * bar_h_scale
    bar = Rectangle(
        width=bar_w, height=h,
        fill_color=color, fill_opacity=0.85,
        stroke_color=color, stroke_width=1
    ).move_to([x_pos, -1.5 + h / 2, 0])
    lbl = Text(label, font_size=14, color=INK).move_to([x_pos, -1.5 - 0.35, 0])
    val_lbl = Text(f"{value}%", font_size=13, color=color).move_to([x_pos, -1.5 + h + 0.25, 0])
    return bar, lbl, val_lbl


class B01_DenseBaseline(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Dense Baseline — All Metrics at 100%", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes_line = Line(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        metrics = ["Storage", "SRAM", "Latency"]
        x_pos = [-2.5, 0, 2.5]
        for m, x in zip(metrics, x_pos):
            bar, lbl, val = make_metric_bar(m, 100, 100, x, INK)
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), FadeIn(val), run_time=0.6)

        sub = Text("Baseline: all three metrics at 100%", font_size=16, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub))
        self.wait(1.5)


class B02_UnstructuredPrune(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Unstructured 50%: Storage Drops, Latency Unchanged", font_size=22, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        # Dense baseline (grey)
        metrics = ["Storage", "SRAM", "Latency"]
        dense_vals = [100, 100, 100]
        unstruct_vals = [50, 100, 100]
        x_centers = [-2.8, 0, 2.8]
        bar_w = 0.9

        for m, dv, uv, xc in zip(metrics, dense_vals, unstruct_vals, x_centers):
            x_dense = xc - bar_w / 2 - 0.05
            x_unstruct = xc + bar_w / 2 + 0.05

            dense_bar, _, _ = make_metric_bar("", dv, 100, x_dense, SOFT, bar_w=bar_w)
            col = ACC if uv == dv else GREEN
            unstruct_bar, _, _ = make_metric_bar("", uv, 100, x_unstruct, col, bar_w=bar_w)

            lbl = Text(m, font_size=14, color=INK).move_to([xc, -1.5 - 0.35, 0])
            val_lbl = Text(f"{uv}%", font_size=13, color=col).move_to([x_unstruct, -1.5 + uv / 100 * 3.0 + 0.25, 0])

            self.play(
                GrowFromEdge(dense_bar, DOWN),
                GrowFromEdge(unstruct_bar, DOWN),
                FadeIn(lbl), FadeIn(val_lbl),
                run_time=0.6
            )

        unchanged = Text("SRAM and Latency UNCHANGED — hardware executes dense kernels on zeros", font_size=13, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(unchanged))
        self.wait(1.5)


class B03_StructuredPrune(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Structured 50%: All Three Bars Drop", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        metrics = ["Storage", "SRAM", "Latency"]
        vals = [50, 50, 50]
        x_pos = [-2.8, 0, 2.8]
        bar_w = 0.9

        for m, v, x in zip(metrics, vals, x_pos):
            x_dense = x - bar_w / 2 - 0.05
            x_struct = x + bar_w / 2 + 0.05

            dense_bar, _, _ = make_metric_bar("", 100, 100, x_dense, SOFT, bar_w=bar_w)
            struct_bar, _, _ = make_metric_bar("", v, 100, x_struct, GREEN, bar_w=bar_w)
            lbl = Text(m, font_size=14, color=INK).move_to([x, -1.5 - 0.35, 0])
            val_lbl = Text(f"{v}%", font_size=13, color=GREEN).move_to([x_struct, -1.5 + v / 100 * 3.0 + 0.25, 0])

            self.play(
                GrowFromEdge(dense_bar, DOWN),
                GrowFromEdge(struct_bar, DOWN),
                FadeIn(lbl), FadeIn(val_lbl),
                run_time=0.6
            )

        lesson = Text("Channels removed → smaller kernel → real latency reduction", font_size=14, color=GREEN).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(lesson))
        self.wait(1.5)
