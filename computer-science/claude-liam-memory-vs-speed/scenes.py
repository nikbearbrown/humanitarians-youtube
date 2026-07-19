"""scenes.py — Manim for claude-liam-memory-vs-speed. Source: embedded-ai Ch. 04"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_NaiveStream(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Naive: Streaming from DRAM", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # DRAM box (far left)
        dram_box = Rectangle(width=1.8, height=2.5, fill_color=GHOST, fill_opacity=0.4,
                            color=INK, stroke_width=2)
        dram_box.move_to([-4.5, -0.2, 0])
        dram_label = Text("DRAM\n~200 cycles", font_size=14, color=INK)
        dram_label.move_to(dram_box.get_center())

        # ALU box (right)
        alu_box = Rectangle(width=1.6, height=1.6, fill_color=SOFT, fill_opacity=0.3,
                           color=INK, stroke_width=2)
        alu_box.move_to([2.0, -0.2, 0])
        alu_label = Text("ALU\nidle…", font_size=14, color=ACC)
        alu_label.move_to(alu_box.get_center())

        self.play(FadeIn(dram_box), FadeIn(dram_label))
        self.play(FadeIn(alu_box), FadeIn(alu_label))

        # Streaming arrows
        for _ in range(3):
            arr = Arrow(
                dram_box.get_right(),
                alu_box.get_left(),
                color=ACC, stroke_width=2, buff=0.1
            )
            self.play(GrowArrow(arr), run_time=0.5)
            self.remove(arr)

        # Slow counter
        slow_text = Text("SLOW  ×10", font_size=22, color=ACC, weight=BOLD)
        slow_text.move_to([0, -2.5, 0])
        self.play(FadeIn(slow_text))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_TiledCache(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Tiled: Resident in Cache", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Matrix grid (small)
        grid_n = 6
        cell = 0.45
        grid = VGroup()
        for r in range(grid_n):
            for c in range(grid_n):
                sq = Square(side_length=cell, color=GHOST, stroke_width=0.8, fill_opacity=0)
                sq.move_to([-2.0 + c * cell, 0.8 - r * cell, 0])
                grid.add(sq)
        self.play(Create(grid), run_time=0.5)

        # Tile highlight (2×2 block)
        tile_size = 2 * cell + 0.04
        tile = Rectangle(width=tile_size, height=tile_size, color=ACC, stroke_width=3, fill_opacity=0)
        tile.move_to([-2.0 + cell * 0.5, 0.8 - cell * 0.5, 0])
        self.play(FadeIn(tile))

        # Cache box (near)
        cache_box = Rectangle(width=2.0, height=1.6, fill_color=ACC, fill_opacity=0.15,
                             color=ACC, stroke_width=2)
        cache_box.move_to([2.5, 0.2, 0])
        cache_label = Text("L1 Cache\n~4 cycles", font_size=14, color=INK)
        cache_label.move_to(cache_box.get_center())
        self.play(FadeIn(cache_box), FadeIn(cache_label))

        # Arrow tile → cache
        arr = Arrow(tile.get_right(), cache_box.get_left(), color=INK, stroke_width=2, buff=0.1)
        self.play(GrowArrow(arr))

        # Reuse annotation
        reuse = Text("reused K times", font_size=14, color=SOFT)
        reuse.next_to(cache_box, UP, buff=0.15)
        self.play(FadeIn(reuse))

        fast_text = Text("FAST", font_size=22, color=SOFT, weight=BOLD)
        fast_text.move_to([0, -2.5, 0])
        self.play(FadeIn(fast_text))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_TimingGap(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("The 10× Memory Wall", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        max_h = 4.0
        bar_w = 1.4
        spacing = 3.0

        naive_h = max_h
        tiled_h = max_h / 10.0

        bar_naive = Rectangle(width=bar_w, height=naive_h, fill_color=SOFT, fill_opacity=0.6, stroke_width=0)
        bar_naive.move_to([-spacing/2, naive_h/2 - 2.3, 0])

        bar_tiled = Rectangle(width=bar_w, height=tiled_h, fill_color=ACC, fill_opacity=0.9, stroke_width=0)
        bar_tiled.move_to([spacing/2, tiled_h/2 - 2.3, 0])

        lbl_naive = Text("Naive\n(DRAM streams)", font_size=15, color=INK)
        lbl_naive.next_to(bar_naive, DOWN, buff=0.15)

        lbl_tiled = Text("Tiled\n(cache resident)", font_size=15, color=INK)
        lbl_tiled.next_to(bar_tiled, DOWN, buff=0.15)

        self.play(GrowFromEdge(bar_naive, DOWN), run_time=0.8)
        self.play(GrowFromEdge(bar_tiled, DOWN), run_time=0.4)
        self.play(FadeIn(lbl_naive), FadeIn(lbl_tiled))

        gap_brace = BraceBetweenPoints(
            bar_tiled.get_top(),
            bar_naive.get_top(),
            direction=RIGHT
        )
        gap_label = Text("10×", font_size=22, color=ACC, weight=BOLD)
        gap_label.next_to(gap_brace, RIGHT, buff=0.15)
        self.play(FadeIn(gap_brace), FadeIn(gap_label))

        note = Text("Zero extra arithmetic. Pure memory access.", font_size=16, color=INK)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 04", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
