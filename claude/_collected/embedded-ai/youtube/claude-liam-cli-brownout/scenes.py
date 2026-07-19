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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_VoltageSag(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("CR2032: Voltage Sag During Inference", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 0.1, 0.02],
            y_range=[2.4, 3.1, 0.1],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)
        x_label = Text("time (s)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("terminal voltage (V)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        V_oc = 3.0
        R_int = 35.0  # ohms
        I_peak = 0.010  # 10 mA
        V_reset = 2.7
        V_terminal_peak = V_oc - I_peak * R_int  # 2.65V

        def voltage_trace(t):
            if 0.02 <= t <= 0.04:
                return V_terminal_peak
            return V_oc - 0.005  # slight sag even at rest

        trace = axes.plot(voltage_trace, x_range=[0, 0.10], color=INK, stroke_width=2.5)

        reset_line = axes.plot(lambda x: V_reset, x_range=[0, 0.10],
                                color=ACC, stroke_width=2, stroke_opacity=0.9)
        reset_label = Text("2.7V brownout reset", font_size=14, color=ACC).shift(LEFT * 2.5 + DOWN * 0.8)

        sag_label = Text("V_term = 3V − 10mA×35Ω = 2.65V → BELOW RESET", font_size=14, color=ACC).to_edge(DOWN, buff=0.8)

        self.play(Create(trace), run_time=1.5)
        self.play(Create(reset_line), FadeIn(reset_label))
        self.play(FadeIn(sag_label))
        self.wait(1.5)


class B02_BulkCap(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Add 100 µF Cap — Sag Flattens", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 0.1, 0.02],
            y_range=[2.4, 3.1, 0.1],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)
        x_label = Text("time (s)", font_size=14, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("terminal voltage (V)", font_size=14, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        V_oc = 3.0
        V_reset = 2.7
        # With cap, sag is dV = I*dt/C = 10mA*20ms/100uF = 2V absorbed → stays above 2.7V
        V_with_cap = 2.85  # stays above reset

        def trace_no_cap(t):
            if 0.02 <= t <= 0.04:
                return 2.65
            return 2.95

        def trace_with_cap(t):
            if 0.02 <= t <= 0.04:
                return V_with_cap
            return V_oc - 0.005

        trace_old = axes.plot(trace_no_cap, x_range=[0, 0.10], color=SOFT, stroke_width=2,
                               stroke_opacity=0.5)
        trace_new = axes.plot(trace_with_cap, x_range=[0, 0.10], color=GREEN, stroke_width=2.5)

        reset_line = axes.plot(lambda x: V_reset, x_range=[0, 0.10],
                                color=ACC, stroke_width=2, stroke_opacity=0.9)
        reset_label = Text("2.7V brownout reset", font_size=14, color=ACC).shift(LEFT * 2.5 + DOWN * 0.6)

        old_label = Text("without cap (2.65V)", font_size=13, color=SOFT).shift(RIGHT * 1.5 + DOWN * 1.2)
        new_label = Text("with 100µF cap (2.85V)", font_size=13, color=GREEN).shift(RIGHT * 1.5 + DOWN * 0.6)

        self.play(Create(trace_old), run_time=1)
        self.play(Create(trace_new), Create(reset_line), run_time=1.5)
        self.play(FadeIn(reset_label), FadeIn(old_label), FadeIn(new_label))

        fix_label = Text("Cap absorbs spike — no brownout reset", font_size=15, color=GREEN).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(fix_label))
        self.wait(1.5)


class B03_EnergyVsPeak(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Two Questions, Two Failure Modes", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        q1_title = Text("How long will it run?", font_size=20, color=INK).shift(LEFT * 3.0 + UP * 1.3)
        q1_type = Text("ENERGY question", font_size=16, color=GREEN).shift(LEFT * 3.0 + UP * 0.7)
        q1_formula = Text("capacity × voltage × efficiency", font_size=14, color=SOFT).shift(LEFT * 3.0 + UP * 0.2)
        q1_fail = Text("→ measured in mAh", font_size=13, color=SOFT).shift(LEFT * 3.0 + DOWN * 0.3)

        q2_title = Text("Will it run at all?", font_size=20, color=INK).shift(RIGHT * 2.5 + UP * 1.3)
        q2_type = Text("PEAK question", font_size=16, color=ACC).shift(RIGHT * 2.5 + UP * 0.7)
        q2_formula = Text("I_peak × R_int vs. V_reset", font_size=14, color=SOFT).shift(RIGHT * 2.5 + UP * 0.2)
        q2_fail = Text("→ full battery can still fail", font_size=13, color=ACC).shift(RIGHT * 2.5 + DOWN * 0.3)

        divider = Line(UP * 2.0, DOWN * 1.5, color=GHOST, stroke_width=1).shift(LEFT * 0.3)

        lesson = Text(
            "Check both before selecting a power source",
            font_size=16, color=INK
        ).to_edge(DOWN, buff=0.9)

        self.play(FadeIn(q1_title), FadeIn(q2_title), Create(divider))
        self.play(FadeIn(q1_type), FadeIn(q2_type))
        self.play(FadeIn(q1_formula), FadeIn(q2_formula))
        self.play(FadeIn(q1_fail), FadeIn(q2_fail))
        self.play(FadeIn(lesson))
        self.wait(1.5)
