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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 01 + Ch. 07",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_CurrentStrip(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Current vs Time: Inference Pulse + Sleep", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[0, 12, 2],
            x_length=8,
            y_length=4,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.4)
        x_label = Text("time (s)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("current (mA)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Slow rate: one pulse per 30 s (simulated at 0.5s scale)
        pulse_w = 0.022 * 5  # 22ms scaled
        period = 0.5
        active_mA = 10
        sleep_uA = 0.01

        pulses = VGroup()
        t = 0
        while t < 2.0:
            pulse = Rectangle(
                width=axes.x_length * pulse_w / 2.2,
                height=axes.y_length * active_mA / 12,
                fill_color=ACC, fill_opacity=0.8, stroke_width=0
            ).move_to(axes.c2p(t + pulse_w / 2, active_mA / 2))
            pulses.add(pulse)
            t += period

        days_label = Text("@ 0.033 Hz → 916 days", font_size=18, color=GREEN).shift(RIGHT * 2.5 + UP * 1.0)
        self.play(LaggedStart(*[GrowFromEdge(p, DOWN) for p in pulses], lag_ratio=0.2))
        self.play(FadeIn(days_label))

        # Show crossover arrow
        crossover = Text("↑ more frequent pulses → fewer days", font_size=14, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(crossover))
        self.wait(1.5)


class B02_DutyCycleFormula(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("The Formula: Duty Cycle → Battery Life", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        formulas = [
            ("duty_cycle", "= inference_ms × freq_hz / 1000"),
            ("avg_current", "= duty_cycle × active_mA\n       + (1 − duty_cycle) × sleep_uA/1000"),
            ("days", "= battery_mAh / (avg_current × 24)"),
        ]

        y_pos = 1.0
        for label, formula in formulas:
            lhs = Text(label, font_size=20, color=ACC)
            rhs = Text(formula, font_size=18, color=INK)
            eq = VGroup(lhs, rhs).arrange(RIGHT, buff=0.2).shift(UP * y_pos)
            self.play(FadeIn(eq), run_time=0.8)
            y_pos -= 1.1

        example = Text(
            "Example: 22ms × 0.033Hz = 0.07% duty → avg 0.01mA → 916 days",
            font_size=14, color=SOFT
        ).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(example))
        self.wait(1.5)


class B03_FrequencySweep(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Frequency Sweep: Find the 7-Day Crossover", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 950, 200],
            x_length=8,
            y_length=4.2,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = Text("frequency (Hz)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("battery life (days)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        inference_ms = 22
        active_mA = 10
        sleep_uA = 10
        battery_mAh = 220

        def days_fn(freq):
            if freq < 0.001:
                return 950
            duty = inference_ms * freq / 1000
            avg_mA = duty * active_mA + (1 - duty) * sleep_uA / 1000
            return battery_mAh / (avg_mA * 24)

        curve = axes.plot(days_fn, x_range=[0.01, 12], color=INK, stroke_width=2.5)
        self.play(Create(curve), run_time=2)

        # 7-day crossover line
        crossover_line = axes.plot(lambda x: 7, x_range=[0, 12], color=ACC, stroke_width=2,
                                    stroke_opacity=0.9)
        crossover_label = Text("7-day design constraint", font_size=14, color=ACC).shift(RIGHT * 2.0 + DOWN * 0.8)

        # Mark approximate crossover frequency (~3 Hz based on formula)
        approx_crossover_x = 2.8
        crossover_dot = Dot(axes.c2p(approx_crossover_x, 7), color=ACC, radius=0.1)
        freq_label = Text(f"~{approx_crossover_x} Hz", font_size=14, color=ACC).next_to(crossover_dot, UP, buff=0.15)

        self.play(Create(crossover_line), FadeIn(crossover_label))
        self.play(FadeIn(crossover_dot), FadeIn(freq_label))

        note = Text("Run the predictor before writing firmware", font_size=15, color=SOFT).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note))
        self.wait(1.5)
