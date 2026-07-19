"""scenes.py — Manim for claude-liam-radio-eats-battery. Source: embedded-ai Ch. 07"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_SleepFloor(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("The Sleep Floor", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 45, 15],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]},
            y_axis_config={"numbers_to_include": [0, 15, 30, 45]},
        )
        ax.move_to([0, -0.5, 0])
        x_label = ax.get_x_axis_label("time (s)", direction=DOWN)
        y_label = ax.get_y_axis_label("current (mA)", direction=LEFT)
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label))

        # Sleep floor: ~0.005 mA = ~5 µA — draw as flat line near bottom
        sleep_pts = [ax.c2p(0, 0.05), ax.c2p(10, 0.05)]
        sleep_line = Line(sleep_pts[0], sleep_pts[1], color=SOFT, stroke_width=3)
        self.play(Create(sleep_line))

        sleep_label = Text("Deep sleep: ~5 µA", font_size=14, color=SOFT)
        sleep_label.move_to(ax.c2p(7, 2.5))
        self.play(FadeIn(sleep_label))

        note = Text("Every event spikes above this line.\nThis is what the battery sees at rest.", font_size=14, color=INK)
        note.move_to([0, -3.2, 0])
        self.play(FadeIn(note))
        self.wait(1)


class B02_InferenceBurst(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Inference Burst", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # X axis in ms (0–200 ms), Y in mA (0–45)
        ax = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 45, 15],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, 50, 100, 150, 200]},
            y_axis_config={"numbers_to_include": [0, 15, 30, 45]},
        )
        ax.move_to([0, -0.5, 0])
        x_label = ax.get_x_axis_label("time (ms)", direction=DOWN)
        y_label = ax.get_y_axis_label("current (mA)", direction=LEFT)
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label))

        # Sleep floor
        sleep_line = Line(ax.c2p(0, 0.05), ax.c2p(200, 0.05), color=GHOST, stroke_width=2)
        self.add(sleep_line)

        # Inference burst: 15 mA from t=30 to t=52 (22 ms)
        inf_pts = [
            ax.c2p(0, 0.05), ax.c2p(30, 0.05), ax.c2p(30, 15),
            ax.c2p(52, 15), ax.c2p(52, 0.05), ax.c2p(200, 0.05),
        ]
        inf_shade = Polygon(*inf_pts, fill_color=SOFT, fill_opacity=0.5, stroke_width=0)
        inf_line = VMobject(color=SOFT, stroke_width=3)
        inf_line.set_points_as_corners(inf_pts)
        self.play(Create(inf_line), FadeIn(inf_shade))

        inf_label = Text("15 mA × 22 ms\n= 0.33 mA·s", font_size=13, color=INK)
        inf_label.move_to(ax.c2p(80, 22))
        self.play(FadeIn(inf_label))

        note = Text("Small spike. Narrow pulse. 0.33 mA·s per inference.", font_size=14, color=INK)
        note.move_to([0, -3.2, 0])
        self.play(FadeIn(note))
        self.wait(1)


class B03_RadioEnvelope(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Radio Dominates", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        ax = Axes(
            x_range=[0, 400, 100],
            y_range=[0, 45, 15],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, 100, 200, 300, 400]},
            y_axis_config={"numbers_to_include": [0, 15, 30, 45]},
        )
        ax.move_to([0, -0.5, 0])
        x_label = ax.get_x_axis_label("time (ms)", direction=DOWN)
        y_label = ax.get_y_axis_label("current (mA)", direction=LEFT)
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label))

        # Sleep floor
        sleep_line = Line(ax.c2p(0, 0.05), ax.c2p(400, 0.05), color=GHOST, stroke_width=2)
        self.add(sleep_line)

        # Inference burst (small, already rendered — ghost)
        inf_pts = [
            ax.c2p(0, 0.05), ax.c2p(20, 0.05), ax.c2p(20, 15),
            ax.c2p(42, 15), ax.c2p(42, 0.05), ax.c2p(400, 0.05),
        ]
        inf_shade = Polygon(*inf_pts, fill_color=GHOST, fill_opacity=0.3, stroke_width=0)
        inf_line = VMobject(color=GHOST, stroke_width=2)
        inf_line.set_points_as_corners(inf_pts)
        self.add(inf_line, inf_shade)

        inf_label = Text("Inference\n0.33 mA·s", font_size=11, color=GHOST)
        inf_label.move_to(ax.c2p(31, 20))
        self.add(inf_label)

        # Radio burst: 38 mA from t=150 to t=250 (100 ms) — ACC dominant
        radio_pts = [
            ax.c2p(150, 0.05), ax.c2p(150, 38),
            ax.c2p(250, 38), ax.c2p(250, 0.05),
        ]
        radio_shade = Polygon(
            ax.c2p(150, 0.05), ax.c2p(150, 38),
            ax.c2p(250, 38), ax.c2p(250, 0.05),
            fill_color=ACC, fill_opacity=0.5, stroke_width=0
        )
        radio_line = VMobject(color=ACC, stroke_width=3)
        radio_line.set_points_as_corners([
            ax.c2p(0, 0.05), ax.c2p(150, 0.05), ax.c2p(150, 38),
            ax.c2p(250, 38), ax.c2p(250, 0.05), ax.c2p(400, 0.05)
        ])
        self.play(Create(radio_line), FadeIn(radio_shade))

        radio_label = Text("LoRa TX\n38 mA × 100 ms\n= 3.5 mA·s", font_size=13, color=ACC, weight=BOLD)
        radio_label.move_to(ax.c2p(200, 42))
        self.play(FadeIn(radio_label))

        compare = Text("Radio = 10× inference energy per event", font_size=14, color=ACC, weight=BOLD)
        compare.move_to([0, -3.2, 0])
        self.play(FadeIn(compare))
        self.wait(1)


class B04_EnergyComparison(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Energy Budget: Inference vs Radio", font_size=24, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Vertical bar chart comparing daily energy budgets
        bar_w = 2.0
        spacing = 4.0
        bottom_y = -2.0

        # Inference: 1000 × 0.33 = 330 mA·s
        # Radio: 10 × 3.5 = 35 mA·s (low), 100 × 3.5 = 350 mA·s (medium)
        # Show three bars: Inference (1000/day), Radio (10/day), Radio (100/day)
        max_val = 380
        max_h = 3.5

        def val_to_h(v):
            return (v / max_val) * max_h

        bars_data = [
            (-spacing, val_to_h(330), SOFT, "Inference\n1,000/day\n330 mA·s"),
            (0, val_to_h(35), GHOST, "Radio\n10/day\n35 mA·s"),
            (spacing, val_to_h(350), ACC, "Radio\n100/day\n350 mA·s"),
        ]

        for x, h, color, lbl in bars_data:
            bar = Rectangle(width=bar_w, height=h,
                           fill_color=color, fill_opacity=0.85, stroke_width=0)
            bar.move_to([x, bottom_y + h / 2, 0])
            label = Text(lbl, font_size=13, color=INK)
            label.next_to(bar, DOWN, buff=0.15)
            self.play(GrowFromEdge(bar, DOWN), FadeIn(label), run_time=0.6)

        rule = Text("Optimize the transmit schedule, not the model.", font_size=15, color=ACC, weight=BOLD)
        rule.move_to([0, -3.3, 0])
        self.play(FadeIn(rule))
        self.wait(1)
