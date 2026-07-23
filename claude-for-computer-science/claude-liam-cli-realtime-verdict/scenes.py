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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 10",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_HistogramBuild(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Latency Histogram — Mean Looks Fine", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 140, 20],
            y_range=[0, 35, 5],
            x_length=8,
            y_length=4,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.4)
        x_label = Text("latency (ms)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("count", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Histogram bins: centered around 38ms mean
        bins = [
            (20, 5), (25, 10), (30, 18), (35, 30), (40, 28),
            (45, 18), (50, 10), (55, 6), (60, 3), (65, 2),
        ]

        for (center, count) in bins:
            bar_h = count
            bar = axes.get_riemann_rectangles(
                axes.plot(lambda x: count if abs(x - center) < 2.5 else 0,
                          x_range=[center - 2.5, center + 2.5]),
                x_range=[center - 2.5, center + 2.5],
                color=INK, fill_opacity=0.7, stroke_width=0
            )
            self.play(FadeIn(bar), run_time=0.25)

        mean_line = axes.get_vertical_line(
            axes.c2p(38, 30), color=GREEN, stroke_width=2.5, line_func=DashedLine
        )
        mean_lbl = Text("mean: 38ms", font_size=14, color=GREEN).shift(LEFT * 0.5 + UP * 1.5)
        self.play(Create(mean_line), FadeIn(mean_lbl))

        note = Text("Mean is fine — but what about the tail?", font_size=15, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note))
        self.wait(1.5)


class B02_WCETTail(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("WCET: The Tail Misses the Deadline", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 140, 20],
            y_range=[0, 35, 5],
            x_length=8,
            y_length=4,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.4)
        x_label = Text("latency (ms)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("count", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Normal region bars
        normal_bins = [(20, 5), (25, 10), (30, 18), (35, 30), (40, 28), (45, 18)]
        tail_bins = [(50, 10), (55, 6), (60, 3), (65, 2), (70, 1.5), (80, 1)]

        for center, count in normal_bins:
            rect = Rectangle(
                width=axes.x_length * 5.0 / 140,
                height=axes.y_length * count / 35,
                fill_color=INK, fill_opacity=0.7, stroke_width=0
            ).move_to(axes.c2p(center, count / 2))
            self.add(rect)

        for center, count in tail_bins:
            rect = Rectangle(
                width=axes.x_length * 5.0 / 140,
                height=axes.y_length * count / 35,
                fill_color=ACC, fill_opacity=0.8, stroke_width=0
            ).move_to(axes.c2p(center, count / 2))
            self.play(GrowFromEdge(rect, DOWN), run_time=0.3)

        # Deadline line at 50ms
        deadline_line = axes.get_vertical_line(
            axes.c2p(50, 35), color=ACC, stroke_width=2.5, line_func=DashedLine
        )
        deadline_lbl = Text("50ms deadline", font_size=14, color=ACC).shift(RIGHT * 1.5 + UP * 1.8)

        # P99 marker
        p99_line = axes.get_vertical_line(
            axes.c2p(80, 10), color=ACC, stroke_width=2, line_func=DashedLine
        )
        p99_lbl = Text("99th pct: 80ms\n(FAILS deadline)", font_size=13, color=ACC).shift(RIGHT * 3.0 + UP * 0.5)

        self.play(Create(deadline_line), FadeIn(deadline_lbl))
        self.play(Create(p99_line), FadeIn(p99_lbl))
        self.wait(1.5)


class B03_JitterStall(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Jitter: GC/DMA Stall Pushes Tail to 120ms", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 140, 20],
            y_range=[0, 35, 5],
            x_length=8,
            y_length=4,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.4)
        x_label = Text("latency (ms)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("count", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Normal histogram
        normal_bins = [(20, 5), (25, 10), (30, 18), (35, 30), (40, 28), (45, 18), (50, 10), (55, 6), (60, 3), (65, 2), (80, 1)]
        for center, count in normal_bins:
            rect = Rectangle(
                width=axes.x_length * 5.0 / 140,
                height=axes.y_length * count / 35,
                fill_color=SOFT if center <= 50 else ACC,
                fill_opacity=0.6, stroke_width=0
            ).move_to(axes.c2p(center, count / 2))
            self.add(rect)

        # Jitter tail beyond 80ms
        jitter_bins = [(85, 0.8), (90, 0.6), (100, 0.5), (110, 0.4), (120, 0.3)]
        for center, count in jitter_bins:
            rect = Rectangle(
                width=axes.x_length * 5.0 / 140,
                height=axes.y_length * count / 35,
                fill_color=ACC, fill_opacity=0.9, stroke_width=0
            ).move_to(axes.c2p(center, count / 2))
            self.play(GrowFromEdge(rect, DOWN), run_time=0.4)

        # Deadline line
        deadline_line = axes.get_vertical_line(
            axes.c2p(50, 35), color=ACC, stroke_width=2, line_func=DashedLine
        )
        deadline_lbl = Text("50ms deadline", font_size=13, color=ACC).shift(LEFT * 0.5 + UP * 1.8)

        # WCET with jitter at 120ms
        wcet_arrow = Arrow(
            axes.c2p(80, 5), axes.c2p(120, 2),
            color=ACC, stroke_width=2, buff=0.1
        )
        wcet_lbl = Text("WCET+jitter: 120ms\n70ms over deadline!", font_size=13, color=ACC).shift(RIGHT * 3.0 + UP * 0.2)

        self.play(Create(deadline_line), FadeIn(deadline_lbl))
        self.play(Create(wcet_arrow), FadeIn(wcet_lbl))

        safety_note = Text("Safety case fails — the nominal distribution hid this", font_size=14, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(safety_note))
        self.wait(1.5)
