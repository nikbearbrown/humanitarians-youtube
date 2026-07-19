"""scenes.py — Manim for claude-liam-doorbell-power-budget. Source: embedded-ai Ch. 01"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_PowerCascade(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Three Budgets", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        labels = ["Memory", "Latency", "Power"]
        values = [0.6, 0.7, 1.0]   # normalized heights (power overshoots)
        target = 0.8               # target line normalized

        bar_width = 1.2
        spacing = 2.0
        bar_colors = [SOFT, SOFT, ACC]
        max_h = 3.0

        bars = []
        bar_labels = []
        for i, (label, val, color) in enumerate(zip(labels, values, bar_colors)):
            x = (i - 1) * spacing
            h = val * max_h
            bar = Rectangle(width=bar_width, height=h, fill_color=color, fill_opacity=0.85, stroke_width=0)
            bar.set_color(color)
            bar.move_to([x, h / 2 - 1.8, 0])
            bars.append(bar)
            lbl = Text(label, font_size=18, color=INK)
            lbl.move_to([x, -2.2, 0])
            bar_labels.append(lbl)

        # Target line
        target_y = target * max_h - 1.8
        target_line = DashedLine(
            start=[-2.5, target_y, 0],
            end=[2.5, target_y, 0],
            color=INK,
            dash_length=0.15,
            stroke_width=2
        )
        target_text = Text("target", font_size=14, color=INK)
        target_text.next_to(target_line, RIGHT, buff=0.1)

        # Animate bars one by one
        for bar, lbl in zip(bars, bar_labels):
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), run_time=0.6)
        self.play(Create(target_line), FadeIn(target_text))

        # Overshoot annotation on power bar
        overshoot = Text("1.7 mA — overshoots", font_size=14, color=ACC)
        overshoot.next_to(bars[2], UP, buff=0.1)
        self.play(FadeIn(overshoot))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 01", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_DutyCycle(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Duty Cycle", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Formula display
        formula = MathTex(
            r"\text{duty cycle} = \frac{t_{\text{inference}}}{T_{\text{period}}}",
            color=INK,
            font_size=36
        )
        formula.move_to([0, 1.0, 0])
        self.play(Write(formula))

        # Two cases: design vs broken
        case1_label = Text("Design: 3.4 s / 30 s", font_size=20, color=SOFT)
        case1_val   = Text("= 11% duty cycle", font_size=20, color=SOFT)
        case2_label = Text("After update: continuous", font_size=20, color=ACC)
        case2_val   = Text("= 100% duty cycle", font_size=20, color=ACC)

        case1_label.move_to([-2.5, -0.3, 0])
        case1_val.move_to([1.8, -0.3, 0])
        case2_label.move_to([-2.5, -1.0, 0])
        case2_val.move_to([1.8, -1.0, 0])

        self.play(FadeIn(case1_label), FadeIn(case1_val))
        self.play(FadeIn(case2_label), FadeIn(case2_val))

        # Timeline strip showing pulses at 11% vs 100%
        strip_y = -2.2
        strip_w = 6.0
        strip_h = 0.4

        strip_bg1 = Rectangle(width=strip_w, height=strip_h, fill_color=GHOST, fill_opacity=0.3, stroke_width=0)
        strip_bg1.move_to([0, strip_y, 0])
        self.add(strip_bg1)

        # 11% pulses (design)
        pulse_w = strip_w * 0.11
        pulse1 = Rectangle(width=pulse_w, height=strip_h, fill_color=SOFT, fill_opacity=0.9, stroke_width=0)
        pulse1.move_to([-strip_w/2 + pulse_w/2, strip_y, 0])

        pulse2 = pulse1.copy()
        pulse2.move_to([-strip_w/2 + pulse_w/2 + strip_w/3, strip_y, 0])

        self.play(GrowFromEdge(pulse1, LEFT), GrowFromEdge(pulse2, LEFT))

        label_strip = Text("11% — design", font_size=13, color=SOFT)
        label_strip.next_to(strip_bg1, RIGHT, buff=0.15)
        self.play(FadeIn(label_strip))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 01", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_BatteryLife(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Battery Life", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        formula = MathTex(
            r"t = \frac{C}{I_{\text{avg}}} = \frac{220\,\text{mAh}}{1.7\,\text{mA}} = 130\,\text{h}",
            color=INK,
            font_size=32
        )
        formula.move_to([0, 1.2, 0])
        self.play(Write(formula))

        # Bar chart: actual vs required
        bar_w = 1.4
        spacing = 2.5

        max_h = 3.0
        actual_h = (130 / 336) * max_h
        target_h = max_h

        bar_actual = Rectangle(width=bar_w, height=actual_h, fill_color=ACC, fill_opacity=0.9, stroke_width=0)
        bar_actual.move_to([-spacing/2, actual_h/2 - 2.0, 0])

        bar_target = Rectangle(width=bar_w, height=target_h, fill_color=SOFT, fill_opacity=0.5, stroke_width=1, stroke_color=INK)
        bar_target.move_to([spacing/2, target_h/2 - 2.0, 0])

        lbl_actual = Text("130 h\n(actual)", font_size=16, color=INK)
        lbl_actual.next_to(bar_actual, DOWN, buff=0.15)

        lbl_target = Text("336 h\n(14-day spec)", font_size=16, color=INK)
        lbl_target.next_to(bar_target, DOWN, buff=0.15)

        self.play(GrowFromEdge(bar_actual, DOWN), GrowFromEdge(bar_target, DOWN), run_time=0.9)
        self.play(FadeIn(lbl_actual), FadeIn(lbl_target))

        shortfall = Text("falls short", font_size=14, color=ACC)
        shortfall.next_to(bar_actual, UP, buff=0.1)
        self.play(FadeIn(shortfall))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 01", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B04_TheFix(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Fix: Periodic Inference", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Before / After arrows
        before = Text("Continuous inference\nDuty = 100%\nI_avg = 15 mA\nLife = 14 hours", font_size=18, color=ACC)
        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=3)
        after  = Text("Periodic: 1/30 s\nDuty = 11%\nI_avg = 0.17 mA\nLife > 336 hours", font_size=18, color=SOFT)

        before.move_to([-3.5, 0, 0])
        arrow.move_to([0, 0, 0])
        after.move_to([3.5, 0, 0])

        self.play(FadeIn(before))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(after))

        note = Text("One firmware line — duty_cycle = inference_time / period", font_size=14, color=INK)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 01", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
