"""scenes.py — Manim for claude-liam-split-inference. Source: embedded-ai Ch. 09"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_FullImageBar(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("224×224×3 Image = 147 KB", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Wide bar representing image payload
        bar_w = 8.0
        bar_h = 1.5
        payload_bar = Rectangle(width=bar_w, height=bar_h, fill_color=SOFT, fill_opacity=0.6, stroke_width=1.5, stroke_color=INK)
        payload_bar.move_to([0, 0.5, 0])
        self.play(GrowFromEdge(payload_bar, LEFT), run_time=1.0)

        size_lbl = Text("147,456 bytes", font_size=22, color=INK, weight="BOLD")
        size_lbl.move_to(payload_bar.get_center())
        self.play(FadeIn(size_lbl))

        # Narrow radio pipe
        pipe = Rectangle(width=0.4, height=2.0, fill_color=GHOST, fill_opacity=0.4, stroke_width=1.5, stroke_color=GHOST)
        pipe.move_to([5.0, 0.5, 0])
        pipe_lbl = Text("radio\npipe", font_size=13, color=GHOST)
        pipe_lbl.next_to(pipe, DOWN, buff=0.2)
        self.play(FadeIn(pipe), FadeIn(pipe_lbl))

        # Clash arrow
        clash = Arrow(start=payload_bar.get_right(), end=pipe.get_left(), color=ACC, stroke_width=2.5, buff=0.05)
        self.play(GrowArrow(clash))

        note = Text("Too wide for the radio. Seconds per image at typical IoT bandwidth.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(note))

        self.wait(1)


class B02_LayerStack(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Activations Shrink Layer by Layer", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        layers = [
            ("Input", 147.0),
            ("Layer 1", 100.0),
            ("Layer 2", 64.0),
            ("Layer 3", 42.0),
            ("Layer 4", 28.0),
            ("Layer 5", 16.0),
            ("Layer 6", 24.0),
        ]

        max_w = 6.5
        max_kb = 147.0
        bar_h = 0.52
        y_start = 2.0
        y_step = 0.65

        bars = VGroup()
        labels = VGroup()
        sizes = VGroup()

        for i, (name, kb) in enumerate(layers):
            w = (kb / max_kb) * max_w
            color = ACC if i == 6 else SOFT
            opacity = 0.85 if i == 6 else 0.55
            bar = Rectangle(width=w, height=bar_h, fill_color=color, fill_opacity=opacity, stroke_width=0)
            bar.move_to([-max_w/2 + w/2 - 1.0, y_start - i * y_step, 0])
            bars.add(bar)

            lbl = Text(name, font_size=14, color=INK)
            lbl.move_to([-5.0, y_start - i * y_step, 0])
            labels.add(lbl)

            sz = Text(f"{kb:.0f} KB", font_size=14, color=SOFT if i != 6 else ACC)
            sz.next_to(bar, RIGHT, buff=0.15)
            sizes.add(sz)

        self.play(FadeIn(labels))
        for b, s in zip(bars, sizes):
            self.play(GrowFromEdge(b, LEFT), FadeIn(s), run_time=0.3)

        note = Text("6 conv-pool pairs halve spatial dims each time.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(note))
        self.wait(1)


class B03_CutLine(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Split: Device | Cloud", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title))

        # Left block: on-device layers
        dev_block = Rectangle(width=3.5, height=3.0, fill_color=SOFT, fill_opacity=0.15, stroke_color=SOFT, stroke_width=1.5)
        dev_block.move_to([-2.5, 0.0, 0])
        dev_lbl = Text("On-Device\n6 conv layers", font_size=16, color=INK)
        dev_lbl.move_to(dev_block.get_center())
        self.play(FadeIn(dev_block), FadeIn(dev_lbl))

        # Cut line (dashed, terracotta)
        cut = DashedLine(
            start=[0.5, 2.2, 0],
            end=[0.5, -2.2, 0],
            color=ACC, dash_length=0.25, stroke_width=2.5
        )
        cut_lbl = Text("split", font_size=14, color=ACC)
        cut_lbl.next_to(cut, UP, buff=0.15)
        self.play(Create(cut), FadeIn(cut_lbl))

        # Right block: server layers
        srv_block = Rectangle(width=3.5, height=3.0, fill_color=SOFT, fill_opacity=0.15, stroke_color=SOFT, stroke_width=1.5)
        srv_block.move_to([3.0, 0.0, 0])
        srv_lbl = Text("Server\nrest of network", font_size=16, color=INK)
        srv_lbl.move_to(srv_block.get_center())
        self.play(FadeIn(srv_block), FadeIn(srv_lbl))

        # Transmission arrow
        tx_arrow = Arrow(start=dev_block.get_right(), end=srv_block.get_left(), color=ACC, stroke_width=2, buff=0.05)
        self.play(GrowArrow(tx_arrow))
        tx_lbl = Text("24 KB activations sent", font_size=14, color=ACC)
        tx_lbl.move_to([-1.5, 1.6, 0])
        self.play(FadeIn(tx_lbl))

        note = Text("6x less bandwidth — image never leaves device", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note))
        self.wait(1.2)
