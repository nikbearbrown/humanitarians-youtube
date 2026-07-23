"""scenes.py — Manim for claude-liam-depthwise-split. Source: embedded-ai Ch. 03"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_StandardConv(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Standard Conv: 18,432 MACs/pixel", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # One 3D block representing the conv operation
        box = Rectangle(
            width=3.5, height=2.5,
            fill_color=SOFT, fill_opacity=0.3,
            color=INK, stroke_width=2.5
        )
        box.move_to([0, 0, 0])

        label = Text("3×3 Conv\n32 in → 64 out", font_size=18, color=INK)
        label.move_to(box.get_center())

        self.play(FadeIn(box), FadeIn(label))

        formula = MathTex(
            r"3 \times 3 \times 32 \times 64 = 18{,}432 \text{ MACs/px}",
            color=INK, font_size=28
        )
        formula.next_to(box, DOWN, buff=0.4)
        self.play(Write(formula))

        counter = Text("18,432", font_size=36, color=ACC, weight=BOLD)
        counter.move_to([0, -3.0, 0])
        self.play(FadeIn(counter))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 03", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_SplitConv(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Split: Depthwise + Pointwise", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Original block
        orig_box = Rectangle(width=3.0, height=2.0, fill_color=SOFT, fill_opacity=0.3,
                             color=INK, stroke_width=2.5)
        orig_box.move_to([0, 1.0, 0])
        orig_label = Text("Standard Conv\n18,432 MACs/px", font_size=16, color=INK)
        orig_label.move_to(orig_box.get_center())
        self.play(FadeIn(orig_box), FadeIn(orig_label))

        # Split arrow
        arrow = Arrow(UP * 0.2, DOWN * 0.6, color=INK, stroke_width=2)
        arrow.move_to([0, -0.1, 0])
        self.play(GrowArrow(arrow))

        # Depthwise block (left)
        dw_box = Rectangle(width=2.6, height=1.6, fill_color=SOFT, fill_opacity=0.25,
                           color=SOFT, stroke_width=2)
        dw_box.move_to([-2.2, -1.5, 0])
        dw_label = Text("Depthwise\n3×3×32\n= 288 MACs/px", font_size=14, color=INK)
        dw_label.move_to(dw_box.get_center())

        # Pointwise block (right)
        pw_box = Rectangle(width=2.6, height=1.6, fill_color=ACC, fill_opacity=0.18,
                           color=ACC, stroke_width=2)
        pw_box.move_to([2.2, -1.5, 0])
        pw_label = Text("Pointwise\n1×1×32×64\n= 2,048 MACs/px", font_size=14, color=INK)
        pw_label.move_to(pw_box.get_center())

        # Arrows from center to each
        arr_l = Arrow(arrow.get_end(), dw_box.get_top(), color=INK, stroke_width=1.5)
        arr_r = Arrow(arrow.get_end(), pw_box.get_top(), color=INK, stroke_width=1.5)

        self.play(
            GrowArrow(arr_l), FadeIn(dw_box), FadeIn(dw_label),
            GrowArrow(arr_r), FadeIn(pw_box), FadeIn(pw_label),
        )

        total = Text("Total: 288 + 2,048 = 2,336 MACs/px", font_size=18, color=ACC, weight=BOLD)
        total.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(total))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 03", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_CostComparison(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Cost Reduction: 7.9×", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        max_h = 4.0
        bar_w = 1.4
        spacing = 3.0

        std_h = max_h
        dws_h = (2336 / 18432) * max_h

        bar_std = Rectangle(width=bar_w, height=std_h, fill_color=SOFT, fill_opacity=0.6, stroke_width=0)
        bar_std.move_to([-spacing/2, std_h/2 - 2.3, 0])

        bar_dws = Rectangle(width=bar_w, height=dws_h, fill_color=ACC, fill_opacity=0.9, stroke_width=0)
        bar_dws.move_to([spacing/2, dws_h/2 - 2.3, 0])

        lbl_std = Text("18,432\nstandard conv", font_size=15, color=INK)
        lbl_std.next_to(bar_std, DOWN, buff=0.15)

        lbl_dws = Text("2,336\ndepthwise sep.", font_size=15, color=INK)
        lbl_dws.next_to(bar_dws, DOWN, buff=0.15)

        self.play(GrowFromEdge(bar_std, DOWN), run_time=0.8)
        self.play(GrowFromEdge(bar_dws, DOWN), run_time=0.5)
        self.play(FadeIn(lbl_std), FadeIn(lbl_dws))

        savings = Text("7.9× savings", font_size=20, color=ACC, weight=BOLD)
        savings.move_to([0, 1.8, 0])
        self.play(FadeIn(savings))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 03", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
