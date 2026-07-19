"""
scenes.py — claude-liam-cli-em-maxwell-light
Manim scenes for Maxwell's Equations: Light Falls Out

B04_WavePacket  — Gaussian pulse propagating at c
B06_Superposition — two pulses passing through each other unchanged
"""

from manim import *
import numpy as np

# Teardown palette
BG  = "#FFFFFF"
INK = "#2A1A0E"
ACC = "#C8102E"   # terracotta / red — primary wave
BLU = "#1A5276"   # blue — left-going pulse
GRN = "#1E8449"   # green — confirmation annotation
ORG = "#D97757"   # orange — tracking dot / spark

SIGMA2 = 0.1   # Gaussian variance (width)


class B04_WavePacket(Scene):
    """
    Gaussian EM wave packet starts at x=2, travels rightward.
    Tracking dot follows the peak.
    After traversal: annotation 'v_measured = 2.998×10⁸ m/s = c ✓'
    Equation c = 1/√(μ₀ε₀) shown at top throughout.
    """

    def construct(self):
        self.camera.background_color = BG

        # — top equation
        eq = MathTex(
            r"c = \frac{1}{\sqrt{\mu_0 \,\varepsilon_0}}",
            color=INK,
        ).scale(0.8).to_edge(UP, buff=0.25)
        self.add(eq)

        # — axes
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[-0.15, 1.2, 0.5],
            x_length=9.5,
            y_length=3.5,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.6)

        x_label = ax.get_x_axis_label(
            MathTex("x\\ (\\mathrm{m})", color=INK).scale(0.65),
            edge=RIGHT, direction=DOWN
        )
        y_label = ax.get_y_axis_label(
            MathTex("E", color=INK).scale(0.65),
            edge=UP, direction=LEFT
        )
        self.add(ax, x_label, y_label)

        # — value tracker: how far the packet has shifted
        t_track = ValueTracker(0.0)

        def gaussian(shift):
            return lambda x: np.exp(-(x - 2.0 - shift) ** 2 / SIGMA2)

        # pulse curve — redrawn every frame
        pulse = always_redraw(
            lambda: ax.plot(
                gaussian(t_track.get_value()),
                x_range=[max(0, 2.0 + t_track.get_value() - 1.5),
                         min(10, 2.0 + t_track.get_value() + 1.5)],
                color=ACC,
                stroke_width=3,
            )
        )

        # peak tracking dot
        dot = always_redraw(
            lambda: Dot(
                ax.c2p(2.0 + t_track.get_value(), 1.0),
                color=ORG,
                radius=0.12,
            )
        )

        # dashed vertical line at peak
        vline = always_redraw(
            lambda: DashedLine(
                ax.c2p(2.0 + t_track.get_value(), -0.1),
                ax.c2p(2.0 + t_track.get_value(), 1.05),
                color=ORG,
                stroke_width=1.5,
                dash_length=0.07,
            )
        )

        self.add(pulse, dot, vline)

        # — animate: packet travels from x=2 to x=8.5 (shift of 6.5 m)
        self.play(
            t_track.animate.set_value(6.5),
            run_time=3.5,
            rate_func=linear,
        )
        self.wait(0.3)

        # — result annotation
        result_lines = VGroup(
            Text("v_measured  =  2.998 × 10⁸ m/s", font_size=26, color=INK),
            Text("=  c  ✓", font_size=26, color=GRN),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        box = SurroundingRectangle(
            result_lines, color=ORG, buff=0.2, stroke_width=2
        )
        result_group = VGroup(result_lines, box).next_to(ax, DOWN, buff=0.25)

        self.play(FadeIn(result_group), run_time=0.6)
        self.wait(1.5)


class B06_Superposition(Scene):
    """
    Two Gaussian pulses travel toward each other.
    Right-going from x=1.5, left-going from x=8.5.
    They overlap at x≈5, then emerge unchanged.
    """

    def construct(self):
        self.camera.background_color = BG

        # — title
        title = Text(
            "Superposition — Two Pulses, No Scattering",
            font_size=26,
            color=INK,
        ).to_edge(UP, buff=0.25)
        self.add(title)

        # — axes
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[-0.2, 2.3, 0.5],
            x_length=9.5,
            y_length=3.8,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.5)

        x_label = ax.get_x_axis_label(
            MathTex("x\\ (\\mathrm{m})", color=INK).scale(0.65),
            edge=RIGHT, direction=DOWN
        )
        y_label = ax.get_y_axis_label(
            MathTex("E", color=INK).scale(0.65),
            edge=UP, direction=LEFT
        )
        self.add(ax, x_label, y_label)

        # — value tracker: time units where 1 unit ≈ 1 m of travel
        t_track = ValueTracker(0.0)

        def g_right(t):
            """right-going pulse, starts at x=1.5"""
            cx = 1.5 + t
            return lambda x: np.exp(-(x - cx) ** 2 / SIGMA2)

        def g_left(t):
            """left-going pulse, starts at x=8.5"""
            cx = 8.5 - t
            return lambda x: np.exp(-(x - cx) ** 2 / SIGMA2)

        def safe_x_range(center, half=1.8):
            return [max(0.05, center - half), min(9.95, center + half)]

        # component curves (faint)
        curve_r = always_redraw(
            lambda: ax.plot(
                g_right(t_track.get_value()),
                x_range=safe_x_range(1.5 + t_track.get_value()),
                color=ACC,
                stroke_width=2,
                stroke_opacity=0.45,
            )
        )

        curve_l = always_redraw(
            lambda: ax.plot(
                g_left(t_track.get_value()),
                x_range=safe_x_range(8.5 - t_track.get_value()),
                color=BLU,
                stroke_width=2,
                stroke_opacity=0.45,
            )
        )

        # sum curve (solid)
        def sum_fn(x):
            t = t_track.get_value()
            return g_right(t)(x) + g_left(t)(x)

        curve_sum = always_redraw(
            lambda: ax.plot(
                sum_fn,
                x_range=[0.05, 9.95],
                color=INK,
                stroke_width=2.5,
            )
        )

        self.add(curve_r, curve_l, curve_sum)

        # — legend
        legend = VGroup(
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=ACC, stroke_width=2),
                Text(" right-going (E₁)", font_size=18, color=INK),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=BLU, stroke_width=2),
                Text(" left-going (E₂)", font_size=18, color=INK),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=INK, stroke_width=2.5),
                Text(" total E = E₁ + E₂", font_size=18, color=INK),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).to_corner(UR, buff=0.35)
        self.add(legend)

        # — phase 1: pulses approach (t: 0 → 3.5)
        self.play(
            t_track.animate.set_value(3.5),
            run_time=3.0,
            rate_func=linear,
        )

        # overlap annotation
        overlap_txt = Text(
            "E = E₁ + E₂  (amplitudes add)",
            font_size=22,
            color=ORG,
        ).next_to(ax, DOWN, buff=0.2)
        self.play(FadeIn(overlap_txt), run_time=0.4)

        # — phase 2: pulses cross and separate (t: 3.5 → 7.0)
        self.play(
            t_track.animate.set_value(7.0),
            run_time=3.5,
            rate_func=linear,
        )

        self.play(FadeOut(overlap_txt), run_time=0.3)

        # final annotation
        final_txt = Text(
            "Each pulse unchanged after crossing",
            font_size=22,
            color=GRN,
        ).next_to(ax, DOWN, buff=0.2)
        self.play(FadeIn(final_txt), run_time=0.5)
        self.wait(1.5)
