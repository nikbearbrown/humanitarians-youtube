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


def accuracy_curve(x):
    """Illustrative accuracy-vs-pruning-rate curve."""
    if x <= 0.2:
        return 100 - x * 3
    elif x <= 0.4:
        return 99.4 - (x - 0.2) * 15
    elif x <= 0.6:
        return 96.4 - (x - 0.4) * 30
    elif x <= 0.7:
        return 90.4 - (x - 0.6) * 60
    else:
        return max(50, 84.4 - (x - 0.7) * 200)


class B01_FlatRegion(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Pruning Curve: Flat Through 20%", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 0.95, 0.2],
            y_range=[50, 102, 10],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = Text("% channels pruned", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("accuracy (%)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Trace only up to 20%
        curve_flat = axes.plot(
            accuracy_curve,
            x_range=[0, 0.20],
            color=GREEN, stroke_width=3
        )
        self.play(Create(curve_flat), run_time=2)

        flat_label = Text("<1% loss through 20% pruning", font_size=16, color=GREEN).shift(LEFT * 1 + UP * 1.2)
        self.play(FadeIn(flat_label))

        start_dot = Dot(axes.c2p(0, accuracy_curve(0)), color=INK, radius=0.08)
        end_dot = Dot(axes.c2p(0.2, accuracy_curve(0.2)), color=GREEN, radius=0.08)
        self.play(FadeIn(start_dot), FadeIn(end_dot))
        self.wait(1.5)


class B02_SweetSpot(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Sweet Spot: 20–40% Pruning", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 0.95, 0.2],
            y_range=[50, 102, 10],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = Text("% channels pruned", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("accuracy (%)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Full curve so far
        curve_flat = axes.plot(accuracy_curve, x_range=[0, 0.20], color=SOFT, stroke_width=2)
        curve_sweet = axes.plot(accuracy_curve, x_range=[0.20, 0.40], color=ACC, stroke_width=3)
        self.play(Create(curve_flat), run_time=0.5)
        self.play(Create(curve_sweet), run_time=1.5)

        # Sweet spot shading
        sweet_region = axes.get_area(
            axes.plot(accuracy_curve, x_range=[0.20, 0.40]),
            x_range=[0.20, 0.40],
            color=ACC, opacity=0.15
        )
        self.play(FadeIn(sweet_region))

        sweet_label = Text("Sweet spot: 20–40% → 2–4% loss", font_size=16, color=ACC).shift(RIGHT * 1.2 + UP * 0.8)
        self.play(FadeIn(sweet_label))
        self.wait(1.5)


class B03_CliffCollapse(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("The Cliff: Collapse Past 70%", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 0.95, 0.1],
            y_range=[50, 102, 10],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = Text("% channels pruned", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("accuracy (%)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Full curve
        curve_safe = axes.plot(accuracy_curve, x_range=[0, 0.40], color=SOFT, stroke_width=2)
        curve_steep = axes.plot(accuracy_curve, x_range=[0.40, 0.70], color=INK, stroke_width=2)
        curve_cliff = axes.plot(accuracy_curve, x_range=[0.70, 0.90], color=ACC, stroke_width=3)

        self.play(Create(curve_safe), run_time=0.5)
        self.play(Create(curve_steep), run_time=1)
        self.play(Create(curve_cliff), run_time=1.5)

        # Cliff zone shading
        cliff_region = axes.get_area(
            axes.plot(accuracy_curve, x_range=[0.70, 0.90]),
            x_range=[0.70, 0.90],
            color=ACC, opacity=0.2
        )
        cliff_line = axes.get_vertical_line(axes.c2p(0.70, accuracy_curve(0.70)),
                                             color=ACC, stroke_width=2,
                                             line_func=DashedLine)
        self.play(FadeIn(cliff_region), Create(cliff_line))

        cliff_label = Text(">70% → collapse", font_size=18, color=ACC).shift(RIGHT * 2.5 + DOWN * 0.3)
        self.play(FadeIn(cliff_label))
        self.wait(1.5)
