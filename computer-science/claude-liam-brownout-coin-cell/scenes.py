"""scenes.py — Manim for claude-liam-brownout-coin-cell. Source: embedded-ai Ch. 02"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_CoinCellCharge(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("CR2032 — Looks Fine", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Battery outline
        bat_body = RoundedRectangle(width=3.5, height=1.8, corner_radius=0.2, color=INK, stroke_width=2.5)
        bat_body.move_to([-0.2, 0.2, 0])
        bat_tip = Rectangle(width=0.3, height=0.7, color=INK, stroke_width=2.5)
        bat_tip.next_to(bat_body, RIGHT, buff=0)

        # Fill level at 80%
        fill_w = 3.5 * 0.80
        bat_fill = Rectangle(width=fill_w, height=1.4, fill_color=SOFT, fill_opacity=0.6, stroke_width=0)
        bat_fill.move_to([-0.2 - (3.5 - fill_w)/2, 0.2, 0])

        self.play(Create(bat_body), Create(bat_tip))
        self.play(GrowFromEdge(bat_fill, LEFT))

        pct_label = Text("80% charge", font_size=20, color=INK)
        pct_label.next_to(bat_body, DOWN, buff=0.2)
        self.play(FadeIn(pct_label))

        # Then: RESET indicator
        reset_box = Rectangle(width=2.4, height=0.7, fill_color=ACC, fill_opacity=0.9, stroke_width=0)
        reset_box.move_to([0, -1.8, 0])
        reset_text = Text("RESET", font_size=22, color=BG, weight=BOLD)
        reset_text.move_to(reset_box)

        self.wait(0.5)
        self.play(FadeIn(reset_box), FadeIn(reset_text))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_VoltageTrace(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Voltage Sag During Inference Burst", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[2.4, 3.1, 0.1],
            x_length=7.5,
            y_length=3.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False
        )
        axes.move_to([0, -0.2, 0])
        x_lbl = Text("time →", font_size=13, color=SOFT)
        x_lbl.next_to(axes, DOWN, buff=0.1)
        y_lbl = Text("V_supply", font_size=13, color=SOFT)
        y_lbl.next_to(axes, LEFT, buff=0.1).rotate(PI/2)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl))

        # Voltage trace: flat at 3V, then dips during burst
        V_nom   = 3.0
        V_burst = 2.65   # 3 - 0.01 * 35
        burst_start = 3.5
        burst_end   = 5.5

        def v_trace(t):
            if burst_start <= t <= burst_end:
                return V_burst
            return V_nom

        pts = [axes.c2p(t, v_trace(t)) for t in np.linspace(0, 10, 1000)]
        wave = VMobject()
        wave.set_points_as_corners(pts)
        wave.set_stroke(color=INK, width=2.5)
        self.play(Create(wave), run_time=1.5)

        # Brown-out threshold line
        threshold_y = 2.7
        thresh_line = DashedLine(
            start=axes.c2p(0, threshold_y),
            end=axes.c2p(10, threshold_y),
            color=ACC, dash_length=0.18, stroke_width=2
        )
        thresh_label = Text("2.7V reset threshold", font_size=13, color=ACC)
        thresh_label.next_to(thresh_line, RIGHT, buff=0.1)
        self.play(Create(thresh_line), FadeIn(thresh_label))

        # Annotation at dip
        dip_arrow = Arrow(
            start=axes.c2p(4.5, 2.55),
            end=axes.c2p(4.5, V_burst + 0.02),
            color=ACC, stroke_width=2
        )
        dip_note = Text("2.65V — below reset", font_size=13, color=ACC)
        dip_note.next_to(dip_arrow, DOWN, buff=0.05)
        self.play(GrowArrow(dip_arrow), FadeIn(dip_note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_TwoQuestions(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Two Power Questions", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left column
        q1_box = Rectangle(width=3.2, height=2.8, color=SOFT, stroke_width=2)
        q1_box.move_to([-2.5, -0.3, 0])
        q1_label = Text("How long\nwill it run?", font_size=20, color=INK)
        q1_label.move_to(q1_box.get_center() + UP * 0.6)
        q1_answer = Text("Energy / Average current\n→ 6 months", font_size=15, color=SOFT)
        q1_answer.move_to(q1_box.get_center() - UP * 0.4)

        # Right column
        q2_box = Rectangle(width=3.2, height=2.8, color=ACC, stroke_width=2)
        q2_box.move_to([2.5, -0.3, 0])
        q2_label = Text("Will it run\nat all?", font_size=20, color=INK)
        q2_label.move_to(q2_box.get_center() + UP * 0.6)
        q2_answer = Text("Peak current vs\nV_supply sag → CRASH", font_size=15, color=ACC)
        q2_answer.move_to(q2_box.get_center() - UP * 0.4)

        self.play(FadeIn(q1_box), FadeIn(q1_label), FadeIn(q1_answer))
        self.play(FadeIn(q2_box), FadeIn(q2_label), FadeIn(q2_answer))

        note = Text("Average lied. Peak told the truth.", font_size=17, color=INK)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 02", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
