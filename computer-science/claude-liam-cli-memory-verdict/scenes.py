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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 05",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_FlashOvershoot(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Flash Budget: FP32 Overshoots 2 MB Ceiling", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes_line = Line(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        flash_mb = 6.0
        ceiling_mb = 2.0
        max_bar = 3.0  # ceiling multiplier
        bar_h_scale = 3.5

        bar_h = min(flash_mb / ceiling_mb, max_bar) * bar_h_scale / max_bar
        ceil_h = bar_h_scale / max_bar

        flash_bar = Rectangle(
            width=2.0, height=bar_h,
            fill_color=ACC, fill_opacity=0.85,
            stroke_color=ACC, stroke_width=1
        ).move_to([0, -1.5 + bar_h / 2, 0])

        ceil_line = DashedLine(
            start=LEFT * 1.5,
            end=RIGHT * 1.5,
            color=INK, stroke_width=2.5, dash_length=0.12
        ).shift(UP * (-1.5 + ceil_h))

        ceil_label = Text("2 MB flash ceiling", font_size=15, color=INK).next_to(ceil_line, RIGHT, buff=0.2)
        flash_val = Text("6 MB (FP32)", font_size=15, color=ACC).shift(UP * (-1.5 + bar_h + 0.3))
        flash_lbl = Text("Flash", font_size=16, color=INK).shift(DOWN * 1.85)

        over_label = Text("FLASH FAILS", font_size=24, color=ACC, weight=BOLD).shift(RIGHT * 3.0 + UP * 0.5)

        self.play(GrowFromEdge(flash_bar, DOWN), run_time=1.5)
        self.play(Create(ceil_line), FadeIn(ceil_label))
        self.play(FadeIn(flash_val), FadeIn(flash_lbl))
        self.play(FadeIn(over_label))
        self.wait(1.5)


class B02_SRAMPass(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("SRAM Budget: 0.6 MB Passes 1 MB Ceiling", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes_line = Line(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        sram_mb = 0.6
        ceiling_mb = 1.0
        bar_h_scale = 3.5

        bar_h = sram_mb / ceiling_mb * bar_h_scale
        ceil_h = bar_h_scale

        sram_bar = Rectangle(
            width=2.0, height=bar_h,
            fill_color=GREEN, fill_opacity=0.85,
            stroke_color=GREEN, stroke_width=1
        ).move_to([0, -1.5 + bar_h / 2, 0])

        ceil_line = DashedLine(
            start=LEFT * 1.5,
            end=RIGHT * 1.5,
            color=INK, stroke_width=2.5, dash_length=0.12
        ).shift(UP * (-1.5 + ceil_h))

        ceil_label = Text("1 MB SRAM ceiling", font_size=15, color=INK).next_to(ceil_line, RIGHT, buff=0.2)
        sram_val = Text("0.6 MB (activation)", font_size=15, color=GREEN).shift(UP * (-1.5 + bar_h + 0.3))
        sram_lbl = Text("SRAM", font_size=16, color=INK).shift(DOWN * 1.85)

        pass_label = Text("SRAM PASSES", font_size=22, color=GREEN, weight=BOLD).shift(RIGHT * 3.0 + UP * 0.5)
        margin_label = Text(f"margin: {(ceiling_mb - sram_mb):.1f} MB", font_size=14, color=SOFT).shift(RIGHT * 3.0 + UP * -0.1)

        self.play(GrowFromEdge(sram_bar, DOWN), run_time=1)
        self.play(Create(ceil_line), FadeIn(ceil_label))
        self.play(FadeIn(sram_val), FadeIn(sram_lbl))
        self.play(FadeIn(pass_label), FadeIn(margin_label))
        self.wait(1.5)


class B03_Int8Toggle(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("INT8 Toggle: Flash Drops, Verdict FITS", font_size=25, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        # Flash: FP32 vs INT8
        flash_fp32 = 6.0
        flash_int8 = 1.5
        flash_ceil = 2.0
        sram_val = 0.6
        sram_ceil = 1.0
        bar_h_scale = 3.5
        bar_w = 1.1
        max_bar = 4.0

        def draw_bar(val, ceiling, x_pos, color, label, col_label):
            h = min(val / ceiling, max_bar / max_bar) * bar_h_scale * min(val / ceiling, 1.2)
            ceil_h = bar_h_scale
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=color, fill_opacity=0.85,
                stroke_color=color, stroke_width=1
            ).move_to([x_pos, -1.5 + h / 2, 0])
            c_line = DashedLine(
                start=[x_pos - bar_w / 2 - 0.15, -1.5 + ceil_h, 0],
                end=[x_pos + bar_w / 2 + 0.15, -1.5 + ceil_h, 0],
                color=INK, stroke_width=2, dash_length=0.1
            )
            lbl = Text(label, font_size=12, color=INK).move_to([x_pos, -1.5 - 0.35, 0])
            val_lbl = Text(col_label, font_size=12, color=color).move_to([x_pos, -1.5 + h + 0.2, 0])
            return bar, c_line, lbl, val_lbl

        # FP32 flash (fails — terracotta)
        bar1, cl1, l1, v1 = draw_bar(flash_fp32, flash_ceil, -3.0, ACC, "Flash\nFP32", "6MB FAIL")
        self.play(GrowFromEdge(bar1, DOWN), Create(cl1), FadeIn(l1), FadeIn(v1), run_time=0.6)

        # INT8 flash (passes — green)
        bar2, cl2, l2, v2 = draw_bar(flash_int8, flash_ceil, -1.2, GREEN, "Flash\nINT8", "1.5MB OK")
        self.play(GrowFromEdge(bar2, DOWN), Create(cl2), FadeIn(l2), FadeIn(v2), run_time=0.6)

        # SRAM (passes — green)
        bar3, cl3, l3, v3 = draw_bar(sram_val, sram_ceil, 0.9, GREEN, "SRAM", "0.6MB OK")
        self.play(GrowFromEdge(bar3, DOWN), Create(cl3), FadeIn(l3), FadeIn(v3), run_time=0.6)

        verdict = Text("VERDICT: FITS", font_size=26, color=GREEN, weight=BOLD).shift(RIGHT * 2.8 + UP * 0.8)
        fix = Text("Fix: quantize weights\nNot: get a bigger chip", font_size=14, color=SOFT).shift(RIGHT * 2.8 + UP * -0.1)
        self.play(FadeIn(verdict), FadeIn(fix))
        self.wait(1.5)
