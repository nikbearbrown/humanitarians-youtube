"""scenes.py — Manim for claude-liam-duty-cycle-battery. Source: embedded-ai Ch. 02"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_SlowPulse(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("1 inference / hour — 104 days", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Current-vs-time strip
        strip_y = 0.0
        strip_w = 8.0
        strip_h = 2.5
        t_total = 10.0  # seconds of "time" shown

        axes = Axes(
            x_range=[0, t_total, 1],
            y_range=[0, 20, 5],
            x_length=strip_w,
            y_length=strip_h,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False
        )
        axes.move_to([0, strip_y, 0])
        x_label = Text("time →", font_size=14, color=SOFT)
        x_label.next_to(axes, DOWN, buff=0.1)
        y_label = Text("current (mA)", font_size=14, color=SOFT)
        y_label.next_to(axes, LEFT, buff=0.1).rotate(PI/2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # One narrow pulse at 10% of timeline (slow period)
        pulse_x_start = 0.1
        pulse_x_end   = 0.3
        I_active = 15.0
        I_sleep  = 0.005

        def current_wave(t):
            if pulse_x_start <= t <= pulse_x_end:
                return I_active
            return I_sleep

        wave_points = [axes.c2p(t, current_wave(t)) for t in np.linspace(0, t_total, 500)]
        wave = VMobject()
        wave.set_points_as_corners(wave_points)
        wave.set_stroke(color=SOFT, width=2.5)
        self.play(Create(wave), run_time=1.2)

        annotation = Text("104 days", font_size=18, color=SOFT)
        annotation.move_to(axes.c2p(5, 17))
        self.play(FadeIn(annotation))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_PeriodShrinks(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("9 inferences / hour — period shrinks", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        strip_w = 8.0
        strip_h = 2.5
        t_total = 10.0

        axes = Axes(
            x_range=[0, t_total, 1],
            y_range=[0, 20, 5],
            x_length=strip_w,
            y_length=strip_h,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False
        )
        axes.move_to([0, 0.3, 0])
        self.play(Create(axes))

        # Multiple pulses, crowded (9x frequency)
        period = t_total / 9.0
        pulse_dur = 0.2

        I_active = 15.0
        I_sleep  = 0.005

        def crowded_wave(t):
            phase = t % period
            if phase < pulse_dur:
                return I_active
            return I_sleep

        wave_points = [axes.c2p(t, crowded_wave(t)) for t in np.linspace(0, t_total, 2000)]
        wave = VMobject()
        wave.set_points_as_corners(wave_points)
        wave.set_stroke(color=ACC, width=2.5)
        self.play(Create(wave), run_time=1.5)

        # Rising average current line
        avg_y = I_active * (pulse_dur / period) + I_sleep * (1 - pulse_dur / period)
        avg_line = DashedLine(
            start=axes.c2p(0, avg_y),
            end=axes.c2p(t_total, avg_y),
            color=ACC, dash_length=0.2, stroke_width=2
        )
        avg_label = Text(f"avg ≈ {avg_y:.1f} mA", font_size=14, color=ACC)
        avg_label.next_to(avg_line, RIGHT, buff=0.1)
        self.play(Create(avg_line), FadeIn(avg_label))

        annotation = Text("11 days", font_size=18, color=ACC)
        annotation.move_to(axes.c2p(5, 18))
        self.play(FadeIn(annotation))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_BarChart(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Frequency Changed Everything", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        bar_w = 1.6
        spacing = 3.0
        max_h = 3.5

        h_104 = max_h
        h_11  = (11 / 104) * max_h

        bar_104 = Rectangle(width=bar_w, height=h_104, fill_color=SOFT, fill_opacity=0.7, stroke_width=0)
        bar_104.move_to([-spacing/2, h_104/2 - 1.8, 0])

        bar_11 = Rectangle(width=bar_w, height=h_11, fill_color=ACC, fill_opacity=0.9, stroke_width=0)
        bar_11.move_to([spacing/2, h_11/2 - 1.8, 0])

        lbl_104 = Text("104 days\n1/hour", font_size=16, color=INK)
        lbl_104.next_to(bar_104, DOWN, buff=0.2)

        lbl_11 = Text("11 days\n9/hour", font_size=16, color=INK)
        lbl_11.next_to(bar_11, DOWN, buff=0.2)

        self.play(GrowFromEdge(bar_104, DOWN), GrowFromEdge(bar_11, DOWN), run_time=0.9)
        self.play(FadeIn(lbl_104), FadeIn(lbl_11))

        note = Text("Model unchanged. Frequency is the variable.", font_size=16, color=INK)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
