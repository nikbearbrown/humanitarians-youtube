"""scenes.py — Manim for claude-liam-architecture-physics. Source: embedded-ai Ch. 14"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_ImageBlocked(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("160,000 bits Through a 250 bps Pipe", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Large payload bar (terracotta — blocked)
        payload = Rectangle(width=8.5, height=1.3, fill_color=ACC, fill_opacity=0.65, stroke_width=0)
        payload.move_to([0.0, 0.8, 0])
        size_lbl = Text("20 KB image = 160,000 bits", font_size=18, color=BG, weight="BOLD")
        size_lbl.move_to(payload.get_center())
        self.play(GrowFromEdge(payload, LEFT), run_time=0.9)
        self.play(FadeIn(size_lbl))

        # Narrow LoRaWAN pipe
        pipe = Rectangle(width=0.25, height=2.8, fill_color=SOFT, fill_opacity=0.4, stroke_color=SOFT, stroke_width=1.5)
        pipe.move_to([5.5, 0.0, 0])
        pipe_lbl = Text("LoRaWAN\n250 bps", font_size=13, color=SOFT)
        pipe_lbl.next_to(pipe, DOWN, buff=0.2)
        self.play(FadeIn(pipe), FadeIn(pipe_lbl))

        # Block arrow
        block_arrow = Arrow(
            start=[payload.get_right()[0] - 0.1, 0.8, 0],
            end=[pipe.get_left()[0] + 0.05, 0.8, 0],
            color=ACC, stroke_width=2.5, buff=0.05
        )
        self.play(GrowArrow(block_arrow))

        # Calculation
        calc = Text("640 seconds per image", font_size=20, color=ACC, weight="BOLD")
        calc.move_to([0.0, -0.5, 0])
        self.play(FadeIn(calc))

        note = Text("= 10.7 minutes per image. LoRaWAN DR0: ~250 bps.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.7)
        physics = Text("Physics: not a configuration problem.", font_size=14, color=INK)
        physics.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note), FadeIn(physics))
        self.wait(1.2)


class B02_AirtimeCeiling(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Airtime Budget: 36 s/hour", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Manual bar chart — y axis: max = 640s mapped to 3.5 manim units
        ax_line = Line(start=[-3.5, -2.0, 0], end=[3.5, -2.0, 0], color=INK, stroke_width=1.5)
        ay_line = Line(start=[-1.0, -2.2, 0], end=[-1.0, 2.0, 0], color=INK, stroke_width=1.5)
        y_lbl = Text("seconds", font_size=14, color=SOFT).rotate(PI/2)
        y_lbl.move_to([-2.0, 0.0, 0])
        self.play(Create(ax_line), Create(ay_line), FadeIn(y_lbl))

        max_h = 3.5
        max_s = 640.0

        def s_to_h(s):
            return (s / max_s) * max_h

        # Budget bar (36s) — very short
        bh = s_to_h(36)
        budget_bar = Rectangle(width=1.2, height=bh, fill_color=SOFT, fill_opacity=0.7, stroke_width=0)
        budget_bar.move_to([-0.2, -2.0 + bh / 2, 0])
        budget_lbl = Text("Budget\n36 s", font_size=14, color=INK)
        budget_lbl.next_to(budget_bar, DOWN, buff=0.15)
        self.play(GrowFromEdge(budget_bar, DOWN), FadeIn(budget_lbl))

        # Ceiling line at 36s
        ceiling_y = -2.0 + bh
        ceiling = DashedLine(
            start=[-3.0, ceiling_y, 0],
            end=[3.0, ceiling_y, 0],
            color=ACC, dash_length=0.2, stroke_width=2
        )
        ceiling_lbl = Text("1% duty cycle ceiling (36 s)", font_size=13, color=ACC)
        ceiling_lbl.move_to([0.0, ceiling_y + 0.25, 0])
        self.play(Create(ceiling))
        self.play(FadeIn(ceiling_lbl))

        # Needed bar (640s) — full height, slams into ceiling
        nh = max_h
        needed_bar = Rectangle(width=1.2, height=nh, fill_color=ACC, fill_opacity=0.7, stroke_width=0)
        needed_bar.move_to([1.8, -2.0 + nh / 2, 0])
        needed_lbl = Text("Needed\n640 s", font_size=14, color=ACC)
        needed_lbl.next_to(needed_bar, DOWN, buff=0.15)
        self.play(GrowFromEdge(needed_bar, DOWN), run_time=0.9)
        self.play(FadeIn(needed_lbl))

        note = Text("One image needs 640s. Budget allows 36s/hour.", font_size=15, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)


class B03_ResultZips(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("10 Bytes Zips Through in 0.32 s", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Two comparisons side by side
        # Left: image blocked
        left_box = Rectangle(width=3.8, height=4.0, fill_color=ACC, fill_opacity=0.08, stroke_color=ACC, stroke_width=1.5)
        left_box.move_to([-3.0, -0.2, 0])
        left_title = Text("Image payload", font_size=17, color=ACC, weight="BOLD")
        left_title.next_to(left_box, UP, buff=0.15)
        self.play(FadeIn(left_box), FadeIn(left_title))

        left_items = [
            ("Size:", "20 KB = 160,000 bits"),
            ("At 250 bps:", "640 seconds"),
            ("Budget/hour:", "36 seconds"),
            ("Images/hour:", "0.056 — impossible"),
        ]
        for i, (k, v) in enumerate(left_items):
            k_lbl = Text(k, font_size=14, color=SOFT)
            v_lbl = Text(v, font_size=14, color=ACC if "impossible" in v or "640" in v else INK)
            k_lbl.move_to([-4.5, 0.8 - i * 0.65, 0])
            v_lbl.move_to([-2.2, 0.8 - i * 0.65, 0])
            self.play(FadeIn(k_lbl), FadeIn(v_lbl), run_time=0.25)

        # Right: result zips through
        right_box = Rectangle(width=3.8, height=4.0, fill_color=SOFT, fill_opacity=0.08, stroke_color=SOFT, stroke_width=1.5)
        right_box.move_to([3.0, -0.2, 0])
        right_title = Text("Classifier result", font_size=17, color=SOFT, weight="BOLD")
        right_title.next_to(right_box, UP, buff=0.15)
        self.play(FadeIn(right_box), FadeIn(right_title))

        right_items = [
            ("Size:", "10 bytes = 80 bits"),
            ("At 250 bps:", "0.32 seconds"),
            ("Budget/hour:", "36 seconds"),
            ("Results/hour:", "112 — easy"),
        ]
        for i, (k, v) in enumerate(right_items):
            k_lbl = Text(k, font_size=14, color=SOFT)
            v_lbl = Text(v, font_size=14, color=SOFT if "easy" in v else INK)
            k_lbl.move_to([1.5, 0.8 - i * 0.65, 0])
            v_lbl.move_to([3.5, 0.8 - i * 0.65, 0])
            self.play(FadeIn(k_lbl), FadeIn(v_lbl), run_time=0.25)

        verdict = Text("Physics chose the architecture.", font_size=18, color=INK, weight="BOLD")
        verdict.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(verdict))
        self.wait(1.2)
