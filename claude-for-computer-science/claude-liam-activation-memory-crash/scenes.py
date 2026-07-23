"""scenes.py — Manim for claude-liam-activation-memory-crash. Source: embedded-ai Ch. 05"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_NaiveCount(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 05", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("The Naive Count", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # SRAM bar: total 256 KB
        sram_label = Text("SRAM: 256 KB", font_size=16, color=INK)
        sram_label.move_to([-3.5, 1.2, 0])

        sram_bar_bg = Rectangle(width=6.0, height=0.7,
                                fill_color=GHOST, fill_opacity=0.3,
                                stroke_width=1, stroke_color=INK)
        sram_bar_bg.move_to([0.5, 0.3, 0])
        self.play(FadeIn(sram_label), FadeIn(sram_bar_bg))

        # Weights annotation (in flash — separate)
        flash_label = Text("Weights: 180 KB → FLASH (not SRAM)", font_size=14, color=SOFT)
        flash_label.move_to([0, -0.5, 0])
        self.play(FadeIn(flash_label))

        # Activations in SRAM: 60 KB
        act_w = 6.0 * (60.0 / 256.0)
        act_bar = Rectangle(width=act_w, height=0.7,
                            fill_color=SOFT, fill_opacity=0.8, stroke_width=0)
        act_bar.move_to([-3.5 + act_w / 2, 0.3, 0])
        act_label = Text("Activations: 60 KB", font_size=13, color=INK)
        act_label.next_to(act_bar, UP, buff=0.15)
        self.play(GrowFromEdge(act_bar, LEFT), FadeIn(act_label))

        # Remaining
        remaining_label = Text("Remaining: 196 KB (firmware, stack…)", font_size=13, color=SOFT)
        remaining_label.move_to([0, -1.5, 0])
        self.play(FadeIn(remaining_label))

        check = Text("Simple math: fits. Reality: crashes.", font_size=15, color=ACC)
        check.move_to([0, -2.5, 0])
        self.play(FadeIn(check))
        self.wait(1)


class B02_NaiveAllocation(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 05", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Naive Allocation: Buffers Pile Up", font_size=24, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # SRAM boundary line
        sram_limit_y = 1.8
        sram_line = DashedLine([-5.5, sram_limit_y, 0], [5.5, sram_limit_y, 0],
                               color=ACC, dash_length=0.15, stroke_width=2)
        sram_label = Text("256 KB SRAM limit", font_size=13, color=ACC)
        sram_label.next_to(sram_line, RIGHT, buff=0.1)
        self.play(Create(sram_line), FadeIn(sram_label))

        # Scale: 256 KB = 3.6 units height
        def kb_to_h(kb):
            return (kb / 256.0) * 3.6

        # Layer activation sizes: 30, 40, 50, 30 KB
        layer_kbs = [30, 40, 50, 30]
        layer_labels = ["L1: 30 KB", "L2: 40 KB", "L3: 50 KB", "L4: 30 KB"]
        bar_w = 1.0
        spacing = 1.3
        start_x = -2.4
        bottom_y = -2.0

        cumulative_h = 0
        bars = []
        for i, (kb, lbl) in enumerate(zip(layer_kbs, layer_labels)):
            h = kb_to_h(kb)
            bar = Rectangle(width=bar_w, height=h,
                           fill_color=SOFT, fill_opacity=0.7, stroke_width=1, stroke_color=INK)
            bar.move_to([start_x + i * spacing, bottom_y + cumulative_h + h / 2, 0])
            cumulative_h += h
            text = Text(lbl, font_size=11, color=INK)
            text.move_to(bar.get_center())
            bars.append((bar, text))

        total_h = cumulative_h

        for bar, text in bars:
            self.play(GrowFromEdge(bar, DOWN), run_time=0.5)
            self.play(FadeIn(text), run_time=0.3)

        # Peak annotation
        peak_y = bottom_y + total_h
        peak_arrow = Arrow([start_x + 1.5, peak_y + 0.3, 0],
                           [start_x + 0.5, peak_y, 0],
                           color=ACC, stroke_width=2)
        peak_label = Text("Peak: 150 KB", font_size=14, color=ACC)
        peak_label.move_to([start_x + 2.5, peak_y + 0.5, 0])
        self.play(GrowArrow(peak_arrow), FadeIn(peak_label))

        crash_text = Text("Crash.", font_size=20, color=ACC, weight=BOLD)
        crash_text.move_to([3.0, 0, 0])
        self.play(FadeIn(crash_text))
        self.wait(1)


class B03_BufferReuse(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 05", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Buffer Reuse: Peak Shrinks", font_size=24, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Timeline: show each layer reusing the same buffer slot
        # Layer sequence: L1 in → L1 out (= L2 in), L1 freed → L2 out (= L3 in) etc.

        row_y_positions = [1.0, 0.0, -1.0, -2.0]
        layer_names = ["Layer 1", "Layer 2", "Layer 3", "Layer 4"]
        phases = ["in", "compute", "out/recycle"]

        # Simplified: show two slots used simultaneously at most
        slot_colors = [SOFT, ACC]

        note1 = Text("Naive: all 4 buffers alive at once → 150 KB peak", font_size=14, color=INK)
        note1.move_to([0, 1.5, 0])
        self.play(FadeIn(note1))

        # Draw reuse diagram
        # Slot A and Slot B alternate
        bar_w = 1.6
        gap = 0.3
        x_positions = [-3.5, -1.5, 0.5, 2.5]

        for i, (x, name) in enumerate(zip(x_positions, layer_names)):
            # Input buffer
            in_bar = Rectangle(width=bar_w, height=0.5,
                              fill_color=SOFT, fill_opacity=0.8, stroke_width=0)
            in_bar.move_to([x, -0.2, 0])
            in_label = Text(f"{name}\nin", font_size=10, color=INK)
            in_label.move_to(in_bar.get_center())

            # Output buffer (reuses previous)
            out_bar = Rectangle(width=bar_w, height=0.5,
                               fill_color=ACC, fill_opacity=0.8, stroke_width=0)
            out_bar.move_to([x, -0.9, 0])
            out_label = Text(f"{name}\nout", font_size=10, color=INK)
            out_label.move_to(out_bar.get_center())

            self.play(FadeIn(in_bar), FadeIn(in_label), run_time=0.4)
            self.play(FadeIn(out_bar), FadeIn(out_label), run_time=0.4)

            if i < 3:
                recycle = Text("recycled", font_size=9, color=GHOST)
                recycle.next_to(in_bar, DOWN, buff=1.2)
                self.play(FadeIn(recycle), FadeOut(in_bar), FadeOut(in_label), run_time=0.4)

        peak_text = Text("Peak: 60 KB  (only 2 buffers live at once)", font_size=15, color=ACC, weight=BOLD)
        peak_text.move_to([0, -2.5, 0])
        self.play(FadeIn(peak_text))
        self.wait(1)


class B04_FlashSramSplit(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 05", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Flash vs SRAM", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Two columns: Flash and SRAM
        flash_box = Rectangle(width=3.5, height=4.0,
                             fill_color=SOFT, fill_opacity=0.2,
                             stroke_width=2, stroke_color=INK)
        flash_box.move_to([-2.5, -0.5, 0])
        flash_title = Text("FLASH", font_size=18, color=INK, weight=BOLD)
        flash_title.next_to(flash_box, UP, buff=0.1)

        sram_box = Rectangle(width=3.5, height=4.0,
                            fill_color=ACC, fill_opacity=0.1,
                            stroke_width=2, stroke_color=ACC)
        sram_box.move_to([2.5, -0.5, 0])
        sram_title = Text("SRAM", font_size=18, color=ACC, weight=BOLD)
        sram_title.next_to(sram_box, UP, buff=0.1)

        self.play(FadeIn(flash_box), FadeIn(flash_title), FadeIn(sram_box), FadeIn(sram_title))

        # Flash contents
        flash_weights = Text("Weights: 180 KB\n(read-only)", font_size=14, color=INK)
        flash_weights.move_to(flash_box.get_center())
        flash_note = Text("Safe: larger than SRAM", font_size=12, color=SOFT)
        flash_note.next_to(flash_box, DOWN, buff=0.15)
        self.play(FadeIn(flash_weights), FadeIn(flash_note))

        # SRAM contents
        sram_act = Text("Activations: 60 KB peak\n(writable, runtime)", font_size=14, color=INK)
        sram_act.move_to(sram_box.get_center())
        sram_note = Text("Constraint: peak, not params", font_size=12, color=ACC)
        sram_note.next_to(sram_box, DOWN, buff=0.15)
        self.play(FadeIn(sram_act), FadeIn(sram_note))

        rule = Text("Arena allocator = automatic buffer reuse", font_size=14, color=INK)
        rule.move_to([0, -2.8, 0])
        self.play(FadeIn(rule))
        self.wait(1)
