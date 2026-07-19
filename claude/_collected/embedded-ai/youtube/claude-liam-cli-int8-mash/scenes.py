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


class B01_WideRange(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Case A: Wide Range [-1.5, 1.5] — Clean Staircase", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[-1.6, 1.6, 0.5],
            y_range=[-1.6, 1.6, 0.5],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = Text("weight value", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("quantized", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI / 2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Continuous sine-like curve (original)
        orig_curve = axes.plot(lambda x: x, x_range=[-1.5, 1.5], color=SOFT, stroke_width=2)

        # Quantized staircase
        scale = 3.0 / 255.0  # (-1.5 to 1.5) / 255 steps
        def quantize_wide(x):
            q = round(x / scale) * scale
            return max(-1.5, min(1.5, q))

        steps = [axes.plot(lambda x, a=a: quantize_wide(a),
                           x_range=[a - scale / 2, a + scale / 2],
                           color=INK, stroke_width=2)
                 for a in np.arange(-1.5, 1.5, scale * 10)]

        error_label = Text("scale = 0.0118/step  error ≈ 0.005  →  harmless", font_size=16, color=GREEN).to_edge(DOWN, buff=0.8)

        self.play(Create(orig_curve))
        self.play(LaggedStart(*[Create(s) for s in steps[:15]], lag_ratio=0.05))
        self.play(FadeIn(error_label))
        self.wait(1.5)


class B02_NarrowMash(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Case B: Narrow Range [0.001, 0.01] — Mash Zone", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Show the narrow range mapping
        axes = Axes(
            x_range=[0, 0.011, 0.002],
            y_range=[-0.5, 10.5, 2],
            x_length=8,
            y_length=4,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.4)
        x_label = Text("activation value", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("int8 bin", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI / 2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # The narrow range maps to very few bins
        narrow_scale = (0.01 - 0.001) / 255.0  # tiny scale
        bin_size = narrow_scale

        # Show mash: many x values → same bin
        mash_rects = VGroup()
        for bin_i in range(5):
            bin_val = 0.001 + bin_i * bin_size * 10
            rect = Rectangle(
                width=axes.x_length * bin_size * 10 / 0.011,
                height=0.6,
                fill_color=ACC, fill_opacity=0.7,
                stroke_color=ACC, stroke_width=1
            ).move_to(axes.c2p(bin_val + bin_size * 5, bin_i * 2 + 1))
            mash_rects.add(rect)

        mash_label = Text("Many activations → same bin (mash zone)", font_size=16, color=ACC).to_edge(DOWN, buff=0.9)
        scale_label = Text("scale = 0.000039/step  range spans ~9 bins only", font_size=15, color=SOFT).to_edge(DOWN, buff=0.5)

        self.play(LaggedStart(*[GrowFromCenter(r) for r in mash_rects], lag_ratio=0.15))
        self.play(FadeIn(mash_label), FadeIn(scale_label))
        self.wait(1.5)


class B03_SideBySide(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Side by Side: Wide vs Narrow Range Quantization", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left panel: Case A
        label_a = Text("Case A: Weights [-1.5, 1.5]", font_size=16, color=INK).shift(LEFT * 3.2 + UP * 1.2)
        result_a = Text("error ≈ 0.005", font_size=18, color=GREEN).shift(LEFT * 3.2 + UP * 0.6)
        desc_a = Text("Staircase tracks the curve", font_size=14, color=SOFT).shift(LEFT * 3.2 + UP * 0.1)

        bars_a = VGroup()
        for i in range(8):
            h = 0.3 + i * 0.08
            b = Rectangle(width=0.25, height=h, fill_color=INK, fill_opacity=0.7, stroke_width=0)
            b.shift(LEFT * (3.2 + (i - 3.5) * 0.3) + DOWN * (1.5 - h / 2))
            bars_a.add(b)

        # Right panel: Case B
        label_b = Text("Case B: Activations [0.001, 0.01]", font_size=16, color=INK).shift(RIGHT * 2.5 + UP * 1.2)
        result_b = Text("MASH — signal lost", font_size=18, color=ACC).shift(RIGHT * 2.5 + UP * 0.6)
        desc_b = Text("Collapsed to 2-3 bins", font_size=14, color=SOFT).shift(RIGHT * 2.5 + UP * 0.1)

        bars_b = VGroup()
        for i in range(8):
            h = 1.8 if i < 2 else 0.05
            b = Rectangle(width=0.25, height=h, fill_color=ACC if i < 2 else GHOST,
                          fill_opacity=0.8, stroke_width=0)
            b.shift(RIGHT * (2.5 + (i - 3.5) * 0.3) + DOWN * (1.5 - h / 2))
            bars_b.add(b)

        divider = Line(UP * 2, DOWN * 2.5, color=GHOST, stroke_width=1).shift(LEFT * 0.3)

        solution = Text("Per-channel quantization rescues Case B", font_size=15, color=ACC).to_edge(DOWN, buff=0.6)

        self.play(FadeIn(label_a), FadeIn(label_b), Create(divider))
        self.play(FadeIn(result_a), FadeIn(result_b))
        self.play(FadeIn(desc_a), FadeIn(desc_b))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars_a], lag_ratio=0.05))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars_b], lag_ratio=0.05))
        self.play(FadeIn(solution))
        self.wait(1.5)
