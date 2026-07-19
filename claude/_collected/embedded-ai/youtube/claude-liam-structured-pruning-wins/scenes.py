"""scenes.py — Manim for claude-liam-structured-pruning-wins. Source: embedded-ai Ch. 12"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_UnstructuredPrune(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Unstructured Pruning: Same Matrix Size", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Full 8x8 matrix
        full_rect = Rectangle(width=4.5, height=2.8, fill_color=SOFT, fill_opacity=0.35,
                              stroke_color=INK, stroke_width=2)
        full_rect.move_to([0, 0.3, 0])
        self.play(FadeIn(full_rect))

        matrix_lbl = Text("8 x 8  (unchanged)", font_size=20, color=INK)
        matrix_lbl.move_to([0, 0.3, 0])
        self.play(FadeIn(matrix_lbl))

        # Add a "zeros overlay" as a distinct rectangle (different color)
        zeros_rect = Rectangle(width=4.5, height=2.8, fill_color=GHOST, fill_opacity=0.18,
                               stroke_width=0)
        zeros_rect.move_to([0, 0.3, 0])
        self.play(FadeIn(zeros_rect))

        dim_bar = Rectangle(width=4.5, height=0.12, fill_color=INK, fill_opacity=0.3, stroke_width=0)
        dim_bar.move_to([0, -1.25, 0])
        dim_lbl = Text("Dimensions unchanged: 8 x 8", font_size=17, color=SOFT)
        dim_lbl.move_to([0, -1.55, 0])
        self.play(FadeIn(dim_bar), FadeIn(dim_lbl))

        latency_bar = Rectangle(width=5.5, height=0.55, fill_color=ACC, fill_opacity=0.2, stroke_width=0)
        latency_bar.move_to([0, -2.5, 0])
        latency_lbl = Text("Latency: UNCHANGED", font_size=22, color=ACC, weight="BOLD")
        latency_lbl.move_to([0, -2.5, 0])
        self.play(FadeIn(latency_bar))
        self.play(FadeIn(latency_lbl))

        note = Text("GEMM kernel multiplies all 64 cells — zeros included.", font_size=15, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))

        self.wait(1.2)


class B02_StructuredPrune(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Structured Pruning: Matrix Shrinks", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Original 8x8 matrix
        orig_lbl = Text("8 x 8", font_size=20, color=INK)
        orig_lbl.move_to([-3.5, 1.8, 0])
        self.play(FadeIn(orig_lbl))

        orig_rect = Rectangle(width=2.8, height=2.8, fill_color=SOFT, fill_opacity=0.35,
                              stroke_color=INK, stroke_width=2)
        orig_rect.move_to([-3.5, 0.2, 0])
        self.play(FadeIn(orig_rect))

        # Highlight removed rows (terracotta) — bottom 3 rows
        removed_rows = Rectangle(width=2.8, height=1.0, fill_color=ACC, fill_opacity=0.65, stroke_width=0)
        removed_rows.move_to([-3.5, -0.95, 0])
        self.play(FadeIn(removed_rows))

        removed_lbl = Text("3 rows\nremoved", font_size=14, color=ACC)
        removed_lbl.next_to(removed_rows, DOWN, buff=0.15)
        self.play(FadeIn(removed_lbl))

        # Arrow
        arrow = Arrow(start=[-1.9, 0.2, 0], end=[0.3, 0.2, 0], color=SOFT, stroke_width=2)
        self.play(GrowArrow(arrow))

        # Resulting 5x5 matrix — visibly smaller
        new_lbl = Text("5 x 5", font_size=20, color=SOFT, weight="BOLD")
        new_lbl.move_to([2.0, 1.8, 0])
        self.play(FadeIn(new_lbl))

        new_rect = Rectangle(width=2.0, height=2.0, fill_color=SOFT, fill_opacity=0.6,
                             stroke_color=SOFT, stroke_width=2)
        new_rect.move_to([2.0, 0.5, 0])
        self.play(FadeIn(new_rect))

        latency_lbl = Text("Latency: 80% faster", font_size=20, color=SOFT, weight="BOLD")
        latency_lbl.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(latency_lbl))

        sram_lbl = Text("SRAM: 80% smaller    Flash: 80% smaller", font_size=16, color=SOFT)
        sram_lbl.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(sram_lbl))

        self.wait(1.2)


class B03_MetricsComparison(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("80% Pruning: What Actually Changes", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Header bar
        header_bg = Rectangle(width=11.5, height=0.6, fill_color=GHOST, fill_opacity=0.15, stroke_width=0)
        header_bg.move_to([0.0, 1.5, 0])
        self.play(FadeIn(header_bg))

        h_metric = Text("Metric", font_size=18, color=INK, weight="BOLD")
        h_metric.move_to([-3.5, 1.5, 0])
        h_unstruct = Text("Unstructured", font_size=18, color=INK, weight="BOLD")
        h_unstruct.move_to([0.0, 1.5, 0])
        h_struct = Text("Structured", font_size=18, color=INK, weight="BOLD")
        h_struct.move_to([3.5, 1.5, 0])
        self.play(FadeIn(h_metric), FadeIn(h_unstruct), FadeIn(h_struct))

        divider = Line(start=[-5.5, 1.1, 0], end=[5.5, 1.1, 0], color=GHOST, stroke_width=1)
        self.play(Create(divider))

        # Flash row background
        row1_bg = Rectangle(width=11.5, height=0.55, fill_color=SOFT, fill_opacity=0.08, stroke_width=0)
        row1_bg.move_to([0.0, 0.5, 0])
        self.play(FadeIn(row1_bg))
        r1_m = Text("Flash", font_size=17, color=INK)
        r1_m.move_to([-3.5, 0.5, 0])
        r1_u = Text("80% smaller", font_size=16, color=SOFT)
        r1_u.move_to([0.0, 0.5, 0])
        r1_s = Text("80% smaller", font_size=16, color=SOFT)
        r1_s.move_to([3.5, 0.5, 0])
        self.play(FadeIn(r1_m), FadeIn(r1_u), FadeIn(r1_s))

        # SRAM row background
        row2_bg = Rectangle(width=11.5, height=0.55, fill_color=GHOST, fill_opacity=0.08, stroke_width=0)
        row2_bg.move_to([0.0, -0.3, 0])
        self.play(FadeIn(row2_bg))
        r2_m = Text("SRAM", font_size=17, color=INK)
        r2_m.move_to([-3.5, -0.3, 0])
        r2_u = Text("Same", font_size=16, color=GHOST)
        r2_u.move_to([0.0, -0.3, 0])
        r2_s = Text("80% smaller", font_size=16, color=SOFT)
        r2_s.move_to([3.5, -0.3, 0])
        self.play(FadeIn(r2_m), FadeIn(r2_u), FadeIn(r2_s))

        # Latency row background (terracotta highlight)
        row3_bg = Rectangle(width=11.5, height=0.55, fill_color=ACC, fill_opacity=0.12, stroke_width=0)
        row3_bg.move_to([0.0, -1.1, 0])
        self.play(FadeIn(row3_bg))
        r3_m = Text("Latency", font_size=17, color=INK)
        r3_m.move_to([-3.5, -1.1, 0])
        r3_u = Text("UNCHANGED", font_size=16, color=ACC, weight="BOLD")
        r3_u.move_to([0.0, -1.1, 0])
        r3_s = Text("80% faster", font_size=16, color=SOFT)
        r3_s.move_to([3.5, -1.1, 0])
        self.play(FadeIn(r3_m), FadeIn(r3_u))
        self.play(FadeIn(r3_s))

        verdict = Text("Same pruning ratio. Completely different runtime impact.", font_size=15, color=SOFT)
        verdict.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(verdict))
        self.wait(1.2)
