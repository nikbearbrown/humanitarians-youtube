"""scenes.py — Manim for claude-liam-race-to-sleep. Source: embedded-ai Ch. 07"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_SlowClockTrace(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Slow Clock: Wide Pulse", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Axes
        ax = Axes(
            x_range=[0, 40, 10],
            y_range=[0, 12, 4],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, 10, 20, 30, 40]},
            y_axis_config={"numbers_to_include": [0, 4, 8, 12]},
        )
        ax.move_to([0, -0.5, 0])
        x_label = ax.get_x_axis_label("time (ms)", direction=DOWN)
        y_label = ax.get_y_axis_label("current (mA)", direction=LEFT)
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label))

        # Slow clock trace: 8 mA active from t=5 to t=27 (22 ms), then sleep ~0
        # Use step function shape
        slow_color = SOFT

        # Build trace as polygon for shading
        # Points: sleep → rise → active → fall → sleep
        trace_points = [
            ax.c2p(0, 0),
            ax.c2p(5, 0),
            ax.c2p(5, 8),
            ax.c2p(27, 8),
            ax.c2p(27, 0),
            ax.c2p(40, 0),
        ]
        trace_line = VMobject(color=slow_color, stroke_width=3)
        trace_line.set_points_as_corners(trace_points)

        # Shaded area
        shaded = Polygon(*trace_points, fill_color=slow_color, fill_opacity=0.35, stroke_width=0)

        self.play(Create(trace_line), FadeIn(shaded))

        # Annotations
        active_label = Text("8 mA", font_size=13, color=INK)
        active_label.move_to(ax.c2p(16, 9.5))
        duration_label = Text("22 ms active", font_size=13, color=INK)
        duration_label.move_to(ax.c2p(16, 7.0))

        energy_label = Text("Energy = 8 mA × 22 ms = 0.176 mA·s", font_size=14, color=INK)
        energy_label.move_to([0, -3.2, 0])

        self.play(FadeIn(active_label), FadeIn(duration_label))
        self.play(FadeIn(energy_label))
        self.wait(1)


class B02_FastClockTrace(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Fast Clock: Narrower Area", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        ax = Axes(
            x_range=[0, 40, 10],
            y_range=[0, 18, 6],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, 10, 20, 30, 40]},
            y_axis_config={"numbers_to_include": [0, 6, 12, 18]},
        )
        ax.move_to([0, -0.5, 0])
        x_label = ax.get_x_axis_label("time (ms)", direction=DOWN)
        y_label = ax.get_y_axis_label("current (mA)", direction=LEFT)
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label))

        # Slow trace ghost (reference)
        slow_points = [
            ax.c2p(0, 0), ax.c2p(5, 0), ax.c2p(5, 8),
            ax.c2p(27, 8), ax.c2p(27, 0), ax.c2p(40, 0),
        ]
        slow_line = VMobject(color=GHOST, stroke_width=2)
        slow_line.set_points_as_corners(slow_points)
        slow_shade = Polygon(*slow_points, fill_color=GHOST, fill_opacity=0.15, stroke_width=0)
        self.add(slow_line, slow_shade)

        # Fast trace: 14 mA from t=5 to t=16 (11 ms)
        fast_points = [
            ax.c2p(0, 0), ax.c2p(5, 0), ax.c2p(5, 14),
            ax.c2p(16, 14), ax.c2p(16, 0), ax.c2p(40, 0),
        ]
        fast_line = VMobject(color=ACC, stroke_width=3)
        fast_line.set_points_as_corners(fast_points)
        fast_shade = Polygon(*fast_points, fill_color=ACC, fill_opacity=0.35, stroke_width=0)
        self.play(Create(fast_line), FadeIn(fast_shade))

        active_label = Text("14 mA (+75%)", font_size=13, color=ACC)
        active_label.move_to(ax.c2p(10.5, 16.0))
        duration_label = Text("11 ms\n(half the time)", font_size=12, color=ACC)
        duration_label.move_to(ax.c2p(10.5, 12.5))

        energy_label = Text("Energy = 14 × 11 = 0.154 mA·s  (12% less than slow)", font_size=14, color=ACC, weight=BOLD)
        energy_label.move_to([0, -3.2, 0])

        self.play(FadeIn(active_label), FadeIn(duration_label))
        self.play(FadeIn(energy_label))
        self.wait(1)


class B03_RaceToSleep(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 07", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Race to Sleep", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        ax = Axes(
            x_range=[0, 35, 5],
            y_range=[0, 18, 6],
            x_length=9,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": [0, 5, 10, 15, 20, 25, 30, 35]},
            y_axis_config={"numbers_to_include": [0, 6, 12, 18]},
        )
        ax.move_to([0, -0.5, 0])
        x_label = ax.get_x_axis_label("time (ms)", direction=DOWN)
        y_label = ax.get_y_axis_label("current (mA)", direction=LEFT)
        self.play(Create(ax), FadeIn(x_label), FadeIn(y_label))

        # Slow trace (ghost): active 0–22 ms at 8 mA
        slow_pts = [
            ax.c2p(0, 8), ax.c2p(22, 8), ax.c2p(22, 0), ax.c2p(35, 0)
        ]
        slow_line = VMobject(color=GHOST, stroke_width=2)
        slow_line.set_points_as_corners([ax.c2p(0, 8)] + slow_pts)
        slow_label = Text("Slow: still active at t=11", font_size=12, color=GHOST)
        slow_label.move_to(ax.c2p(15, 9.5))
        self.play(Create(slow_line), FadeIn(slow_label))

        # Fast trace: active 0–11 ms at 14 mA, then drops to ~0 (sleep)
        fast_pts = [
            ax.c2p(0, 14), ax.c2p(11, 14), ax.c2p(11, 0.1), ax.c2p(35, 0.1)
        ]
        fast_line = VMobject(color=ACC, stroke_width=3)
        fast_line.set_points_as_corners([ax.c2p(0, 14)] + fast_pts)
        self.play(Create(fast_line))

        # Sleep label
        sleep_label = Text("SLEEP\n~5 µA", font_size=12, color=ACC)
        sleep_label.move_to(ax.c2p(25, 2.0))
        self.play(FadeIn(sleep_label))

        # Annotation at t=11
        vert = DashedLine(ax.c2p(11, 0), ax.c2p(11, 16), color=ACC, dash_length=0.12, stroke_width=1.5)
        vert_label = Text("t = 11 ms\nfast: sleeping\nslow: still active", font_size=11, color=ACC)
        vert_label.move_to(ax.c2p(11, 17.0))
        self.play(Create(vert), FadeIn(vert_label))

        rule = Text("Finish fast. Go deep. Save the area.", font_size=15, color=INK, weight=BOLD)
        rule.move_to([0, -3.2, 0])
        self.play(FadeIn(rule))
        self.wait(1)
