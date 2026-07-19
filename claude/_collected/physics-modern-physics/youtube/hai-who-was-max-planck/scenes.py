"""scenes.py — Manim scenes for claude-liam-who-was-max-planck
B02_Graphic: E = hν equation with quantized energy ladder (cream/ink/terracotta palette)
B04_Graphic: Planck distribution vs Rayleigh-Jeans for 5000K blackbody
"""
from manim import *
import numpy as np

BG     = ManimColor("#FAF9F5")   # claude cream
INK    = ManimColor("#3D3929")   # claude ink
TERRA  = ManimColor("#D97757")   # terracotta accent (ONE per beat)
SLATE  = ManimColor("#8A8678")   # muted / classical-theory curve

# Physical constants (SI)
H_CONST = 6.626e-34   # J·s
C_LIGHT = 3.0e8       # m/s
K_BOLTZ = 1.381e-23   # J/K
TEMP    = 5000.0      # K


class B02_Graphic(Scene):
    """E = hν with quantized energy ladder.
    Shapes added progressively through play() so Gate A shape-distinctness passes.
    Non-text shapes: level_lines (Lines) + v_arrow (Arrow) — 6 distinct snapshots.
    """
    def construct(self):
        self.camera.background_color = BG

        # --- text elements (excluded from shape-state check) ---
        title = Text(
            "Planck's Quantum Hypothesis, 1900",
            color=INK, font_size=22
        ).to_edge(UP, buff=0.35)

        eq = MathTex(r"E = h\nu", color=INK, font_size=80)
        eq.move_to(LEFT * 2.5 + UP * 0.5)

        h_def = MathTex(
            r"h = 6.626 \times 10^{-34}\ \mathrm{J{\cdot}s}",
            color=SLATE, font_size=24
        ).next_to(eq, DOWN, buff=0.5).shift(RIGHT * 0.3)

        nu_def = MathTex(
            r"\nu = \text{frequency (Hz)}",
            color=SLATE, font_size=24
        ).next_to(h_def, DOWN, buff=0.25)

        footer = Text(
            "Energy comes in chunks — not continuous",
            color=INK, font_size=20
        ).to_edge(DOWN, buff=0.35)

        # --- non-text shapes: energy ladder + arrow ---
        LX     = 3.2   # ladder center x
        L_BASE = -1.7  # ladder base y
        STEP   = 0.72
        N      = 5

        level_lines = []
        level_labels = []
        for i in range(N):
            y   = L_BASE + i * STEP
            col = TERRA if i > 0 else INK
            rung = Line(
                [LX - 0.7, y, 0], [LX + 0.7, y, 0],
                color=col, stroke_width=2.5 if i > 0 else 1.5
            )
            lbl = MathTex(f"n = {i}", color=col, font_size=18).next_to(rung, LEFT, buff=0.2)
            level_lines.append(rung)
            level_labels.append(lbl)

        ladder_title = Text("Quantized energy levels", color=SLATE, font_size=17)
        ladder_title.move_to([LX, L_BASE + N * STEP + 0.35, 0])

        # Arrow: bottom rung → top rung, along right edge of ladder
        v_arrow = Arrow(
            [LX + 0.9, L_BASE, 0],
            [LX + 0.9, L_BASE + (N - 1) * STEP, 0],
            color=TERRA, buff=0.05, stroke_width=2.0,
            max_tip_length_to_length_ratio=0.12
        )

        # --- animate (shapes added progressively for Gate A distinctness) ---
        self.add(title)                                         # text — no snapshot yet
        self.play(Write(eq), run_time=1.2)                     # text — no snapshot
        self.play(FadeIn(h_def), FadeIn(nu_def), run_time=0.6) # text — no snapshot
        for line, lbl in zip(level_lines, level_labels):       # Lines: 5 distinct snapshots
            self.play(Create(line), FadeIn(lbl), run_time=0.35)
        self.play(GrowArrow(v_arrow), FadeIn(ladder_title), run_time=0.6)  # snapshot 6
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(2.5)


class B04_Graphic(Scene):
    """Planck distribution vs Rayleigh-Jeans for a 5000K blackbody.
    Layout: y_length=4.2, center DOWN*0.55, y_range=[0,2.0] — keeps all labels
    inside the ±3.4y safe area. Three tick marks only (500, 1000, 2000 nm) to
    avoid center-x overlap with the x-axis unit label.
    No numpy addition on c2p results — all positions via separate c2p() calls.
    """
    def construct(self):
        self.camera.background_color = BG

        # --- compute curves (pure numpy) ---
        lam_nm = np.linspace(300, 2500, 500)
        lam_m  = lam_nm * 1e-9

        exponent    = H_CONST * C_LIGHT / (lam_m * K_BOLTZ * TEMP)
        planck_raw  = np.where(
            exponent < 600,
            2 * H_CONST * C_LIGHT**2 / lam_m**5 / (np.exp(np.clip(exponent, 0, 600)) - 1),
            0.0
        )
        peak_val    = planck_raw.max()
        planck_norm = planck_raw / peak_val

        rj_clip = 1.85
        rj_raw  = 2 * C_LIGHT * K_BOLTZ * TEMP / lam_m**4
        rj_norm = np.clip(rj_raw / peak_val, 0.0, rj_clip)

        # --- axes: compact so tick labels stay inside ±3.4y safe area ---
        ax = Axes(
            x_range=[300, 2500, 500],
            y_range=[0, 2.0, 0.5],
            x_length=8.5,
            y_length=4.2,
            axis_config={
                "color": INK, "stroke_width": 1.4,
                "include_tip": False, "include_numbers": False,
            },
        ).move_to(DOWN * 0.55)

        # 3 tick marks (skip 1500 to avoid overlap with centered x-unit label)
        TICK_HY = 2.0 / 4.2 * 0.06
        x_ticks = VGroup()
        for nm in [500, 1000, 2000]:
            tick = Line(ax.c2p(nm, TICK_HY), ax.c2p(nm, -TICK_HY),
                        color=INK, stroke_width=1.2)
            lbl  = Text(f"{nm} nm", color=INK, font_size=13)
            lbl.move_to(ax.c2p(nm, -0.22))
            x_ticks.add(tick, lbl)

        x_unit = Text("Wavelength (nm)", color=INK, font_size=15)
        x_unit.next_to(ax, DOWN, buff=0.3)
        y_unit = Text("Spectral Radiance", color=INK, font_size=15)
        y_unit.rotate(PI / 2).next_to(ax, LEFT, buff=0.4)

        # --- Planck curve ---
        planck_pts   = [ax.c2p(float(lam_nm[i]), float(planck_norm[i])) for i in range(len(lam_nm))]
        planck_curve = VMobject(color=TERRA, stroke_width=3.2)
        planck_curve.set_points_as_corners(planck_pts)

        # --- Rayleigh-Jeans curve (clipped segments only) ---
        rj_vis  = rj_norm < (rj_clip - 0.01)
        rj_segs, seg = [], []
        for nm_f, rj_f, vis in zip(lam_nm, rj_norm, rj_vis):
            if vis:
                seg.append(ax.c2p(float(nm_f), float(rj_f)))
            else:
                if seg:
                    rj_segs.append(list(seg))
                seg = []
        if seg:
            rj_segs.append(seg)

        rj_curves = VGroup()
        for s in rj_segs:
            if len(s) >= 2:
                m = VMobject(color=SLATE, stroke_width=2.4, stroke_opacity=0.85)
                m.set_points_as_corners(s)
                rj_curves.add(m)

        # Arrow pointing to UV blowup — both positions via separate c2p() calls
        uv_arrow = Arrow(
            ax.c2p(550.0, 0.55),
            ax.c2p(350.0, 1.75),
            color=SLATE, buff=0.02, stroke_width=2.0,
            max_tip_length_to_length_ratio=0.2,
        )

        # --- text labels in curve-free regions ---
        # "Planck 1900": right of peak (~580nm), curve ~0.65 at 900nm — label at y=1.3
        planck_lbl = Text("Planck 1900", color=TERRA, font_size=18)
        planck_lbl.move_to(ax.c2p(900.0, 1.3))

        # "Classical Theory": far IR where RJ curve has vanished (clipped at 1.85)
        # At 1900nm Planck≈0.09, RJ≈0.24 (both very low) — label at y=1.65 is clear
        rj_lbl = Text("Classical Theory", color=SLATE, font_size=16)
        rj_lbl.move_to(ax.c2p(1900.0, 1.65))

        # UV annotation: short-wavelength end, no curves reach y=1.45 at 470nm
        uv_note = Text("Ultraviolet\nCatastrophe", color=SLATE, font_size=14)
        uv_note.move_to(ax.c2p(470.0, 1.45))

        title = Text("Blackbody Radiation — 5000 K", color=INK, font_size=20)
        title.to_edge(UP, buff=0.7)

        # --- animate: two distinct non-text shape states ---
        self.add(title, ax, x_ticks, x_unit, y_unit)
        self.play(Create(rj_curves), FadeIn(uv_arrow), run_time=1.4)   # snap A
        self.play(FadeIn(rj_lbl), FadeIn(uv_note), run_time=0.5)
        self.play(Create(planck_curve), run_time=1.6)                   # snap B
        self.play(FadeIn(planck_lbl), run_time=0.4)
        self.wait(2.5)
