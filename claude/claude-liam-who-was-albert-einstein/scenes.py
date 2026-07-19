"""scenes.py — Manim scenes for claude-liam-who-was-albert-einstein
B02_Graphic: E = hf with photoelectric threshold ladder (cream/ink/terracotta palette)
B04_Graphic: E = mc² with mass-energy bar-chart scale comparison
"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")  # claude cream
INK   = ManimColor("#3D3929")  # claude ink
TERRA = ManimColor("#D97757")  # terracotta accent (ONE concept per beat)
SLATE = ManimColor("#8A8678")  # muted / below-threshold


class B02_Graphic(Scene):
    """E = hf with frequency-threshold visualization for the photoelectric effect.
    Non-text shapes: 5 freq_lines (Lines) + threshold_line (DashedLine) + e_arrow (Arrow) = 7 states.
    All shapes added progressively via play() — Gate A passes.
    No axes / no c2p — all positions hardcoded — Gate B: no arithmetic errors.
    """
    def construct(self):
        self.camera.background_color = BG

        # --- text elements ---
        title = Text(
            "The Photoelectric Effect, 1905",
            color=INK, font_size=22
        ).to_edge(UP, buff=0.35)

        eq = MathTex(r"E = hf", color=INK, font_size=80)
        eq.move_to(LEFT * 2.5 + UP * 0.5)

        h_def = MathTex(
            r"h = 6.626 \times 10^{-34}\ \mathrm{J{\cdot}s}",
            color=SLATE, font_size=22
        ).next_to(eq, DOWN, buff=0.4).shift(RIGHT * 0.2)

        f_def = MathTex(
            r"f = \text{frequency (Hz)}",
            color=SLATE, font_size=22
        ).next_to(h_def, DOWN, buff=0.25)

        footer = Text(
            "Frequency — not brightness — determines escape",
            color=INK, font_size=18
        ).to_edge(DOWN, buff=0.35)

        # --- right side: frequency ladder with threshold ---
        LX     = 3.2   # ladder center x
        L_BASE = -1.7  # ladder base y
        STEP   = 0.72
        N      = 5
        THRESH = 2     # rungs 0,1 below threshold (SLATE); 2,3,4 above (TERRA)

        freq_lines = []
        for i in range(N):
            y   = L_BASE + i * STEP
            col = TERRA if i >= THRESH else SLATE
            w   = 2.5 if i >= THRESH else 1.5
            freq_lines.append(
                Line([LX - 0.7, y, 0], [LX + 0.7, y, 0], color=col, stroke_width=w)
            )

        # Threshold dashed line between rung 1 and rung 2
        thresh_y = L_BASE + THRESH * STEP - STEP / 2   # = -0.62
        threshold_line = DashedLine(
            [LX - 1.0, thresh_y, 0], [LX + 1.0, thresh_y, 0],
            color=INK, stroke_width=1.8, dash_length=0.14
        )
        thresh_lbl = MathTex(r"\text{threshold } f_0", color=TERRA, font_size=16)
        thresh_lbl.move_to([LX, thresh_y + 0.24, 0])

        ladder_title = Text("Photon frequency", color=SLATE, font_size=17)
        ladder_title.move_to([LX, L_BASE + N * STEP + 0.35, 0])

        # Electron ejection arrow above top rung
        e_arrow = Arrow(
            [LX + 0.9, L_BASE + (N - 1) * STEP, 0],
            [LX + 0.9, L_BASE + N * STEP + 0.1, 0],
            color=TERRA, buff=0.05, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.20
        )
        e_lbl = Text("electron\nejected", color=TERRA, font_size=15)
        e_lbl.move_to([LX + 1.95, L_BASE + N * STEP - 0.15, 0])

        # --- animate (shapes added progressively for Gate A distinctness) ---
        self.add(title)
        self.play(Write(eq), run_time=1.2)
        self.play(FadeIn(h_def), FadeIn(f_def), run_time=0.6)
        for rung in freq_lines:                                       # 5 distinct shape states
            self.play(Create(rung), run_time=0.35)
        self.play(                                                     # shape state 6
            Create(threshold_line),
            FadeIn(thresh_lbl), FadeIn(ladder_title),
            run_time=0.6
        )
        self.play(GrowArrow(e_arrow), FadeIn(e_lbl), run_time=0.6)   # shape state 7
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(2.5)


class B04_Graphic(Scene):
    """E = mc² — mass-energy equivalence with bar-chart scale comparison.
    Non-text shapes: mass_bar (Rectangle), mult_arrow (Arrow), energy_bar (Rectangle) = 3 states.
    All shapes added progressively via play(). No axes / no c2p. All positions hardcoded.
    buff=0.7 on title and footer keeps both inside ±3.4y safe area.
    Animations extended to ~15s so the 21.7s narration needs only ~1.4x slow-mo.
    """
    def construct(self):
        self.camera.background_color = BG

        # --- text elements — buff=0.7 keeps title/footer inside ±3.4y ---
        title = Text(
            "Special Relativity — September 1905",
            color=INK, font_size=22
        ).to_edge(UP, buff=0.7)

        eq = MathTex(r"E = mc^2", color=INK, font_size=80)
        eq.move_to(LEFT * 2.2 + UP * 0.5)

        m_def = MathTex(
            r"m = \text{mass (kg)}",
            color=SLATE, font_size=24
        ).next_to(eq, DOWN, buff=0.45).shift(RIGHT * 0.1)

        c_def = MathTex(
            r"c^2 \approx 9 \times 10^{16}\ \mathrm{m^2/s^2}",
            color=SLATE, font_size=20
        ).next_to(m_def, DOWN, buff=0.25)

        footer = Text(
            "One tiny mass — an enormous amount of energy",
            color=INK, font_size=18
        ).to_edge(DOWN, buff=0.7)

        # --- right side: mass vs energy bar chart ---
        BAR_BASE = -1.5   # raised slightly to match tighter title/footer margins
        MASS_X   = 2.5
        ENRG_X   = 3.5

        mass_bar = Rectangle(width=0.55, height=0.4, color=SLATE,
                             fill_color=SLATE, fill_opacity=0.7)
        mass_bar.move_to([MASS_X, BAR_BASE + 0.2, 0])
        mass_lbl = Text("1 kg", color=SLATE, font_size=15)
        mass_lbl.move_to([MASS_X, BAR_BASE - 0.28, 0])

        mult_arrow = Arrow(
            [MASS_X + 0.38, BAR_BASE + 0.35, 0],
            [ENRG_X - 0.38, BAR_BASE + 0.75, 0],
            color=TERRA, buff=0.02, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.20
        )
        mult_lbl = MathTex(r"\times\, c^2", color=TERRA, font_size=22)
        mult_lbl.move_to([2.82, BAR_BASE + 0.85, 0])

        energy_bar = Rectangle(width=0.55, height=2.4, color=TERRA,
                               fill_color=TERRA, fill_opacity=0.7)
        energy_bar.move_to([ENRG_X, BAR_BASE + 1.2, 0])
        energy_lbl = MathTex(r"9 \times 10^{16}\ \mathrm{J}", color=TERRA, font_size=14)
        energy_lbl.move_to([ENRG_X, BAR_BASE - 0.28, 0])

        diagram_title = Text("Mass → Energy", color=SLATE, font_size=16)
        diagram_title.move_to([3.0, BAR_BASE + 2.85, 0])

        # --- animate: separated plays extend total to ~15s for ~1.4x slow-mo ---
        self.add(title)
        self.play(Write(eq), run_time=1.5)
        self.play(FadeIn(m_def), run_time=0.8)
        self.play(FadeIn(c_def), run_time=0.8)
        self.play(Create(mass_bar), run_time=0.8)              # shape state 1
        self.play(FadeIn(mass_lbl), run_time=0.5)
        self.play(GrowArrow(mult_arrow), run_time=0.9)         # shape state 2
        self.play(FadeIn(mult_lbl), run_time=0.5)
        self.play(Create(energy_bar), run_time=1.0)            # shape state 3
        self.play(FadeIn(energy_lbl), FadeIn(diagram_title), run_time=0.8)
        self.play(FadeIn(footer), run_time=0.6)
        self.wait(7.0)
