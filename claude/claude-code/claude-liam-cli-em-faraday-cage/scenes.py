from manim import *
import numpy as np

# Teardown palette
BG   = ManimColor("#FFFFFF")
INK  = ManimColor("#2A1A0E")
ACC  = ManimColor("#C8102E")   # copper curve (red)
BLUE = ManimColor("#1A5276")   # aluminum curve
GRN  = ManimColor("#1E8449")   # steel curve
ORG  = ManimColor("#D97757")   # MRI marker (terracotta)
GRAY = ManimColor("#7F8C8D")

MU0 = 4e-7 * np.pi   # H/m — permeability of free space


def log_sd(log_f: float, rho: float) -> float:
    """log10 of skin depth given log10(frequency) and resistivity rho (Ω·m)."""
    f = 10.0 ** log_f
    return 0.5 * np.log10(2.0 * rho / (2.0 * np.pi * f * MU0))


class B04_SkinDepth(Scene):
    """
    Two-panel log-log plot for copper at d=1 mm:
      Left  — δ(f): skin depth sweeps down from ~0.3 mm at 1 kHz to 8.4 μm at 64 MHz
      Right — A_dB(f): attenuation climbs to >1000 dB at 64 MHz
    MRI markers animate in at 64 MHz (1.5 T) on both panels.
    """

    def construct(self):
        self.camera.background_color = BG
        RHO_CU = 1.68e-8   # copper Ω·m
        D      = 1e-3       # 1 mm sheet

        # Title
        title = Text(
            "Faraday Cage — Copper Skin Depth",
            font_size=26, color=INK, weight=BOLD,
        ).to_edge(UP, buff=0.22)
        self.play(Write(title), run_time=0.6)

        # ── Left panel: δ(f) log-log ─────────────────────────────────────────
        ax_l = Axes(
            x_range=[5, 10, 1],    # log10(f): 100 kHz → 10 GHz
            y_range=[-7, -4, 1],   # log10(δ/m): ~100 nm → 0.1 mm
            x_length=5.2,
            y_length=3.6,
            axis_config={"color": INK, "stroke_width": 1.3, "include_tip": False},
            tips=False,
        ).shift(LEFT * 2.9 + DOWN * 0.5)

        xtl_l = VGroup(*[
            Text(t, font_size=11, color=GRAY)
            .next_to(ax_l.c2p(v, -7), DOWN, buff=0.13)
            for v, t in [(5, "100k"), (7, "10M"), (9, "1G"), (10, "10G")]
        ])
        ytl_l = VGroup(*[
            Text(t, font_size=11, color=GRAY)
            .next_to(ax_l.c2p(5, v), LEFT, buff=0.11)
            for v, t in [(-4, "0.1mm"), (-5, "10μm"), (-6, "1μm"), (-7, "0.1μm")]
        ])
        xl_l = Text("f  (log)", font_size=14, color=INK).next_to(ax_l, DOWN, buff=0.48)
        yl_l = (Text("δ  (log)", font_size=14, color=INK)
                .rotate(PI / 2).next_to(ax_l, LEFT, buff=0.52))

        self.play(
            Create(ax_l),
            FadeIn(xtl_l), FadeIn(ytl_l), FadeIn(xl_l), FadeIn(yl_l),
            run_time=0.7,
        )

        curve_l = ax_l.plot(
            lambda x: log_sd(x, RHO_CU),
            x_range=[5.0, 10.0],
            color=ACC, stroke_width=3.2,
        )
        self.play(Create(curve_l), run_time=1.8)

        # 64 MHz marker (log10 ≈ 7.806)
        x_mri   = np.log10(64e6)
        y_mri_l = log_sd(x_mri, RHO_CU)   # ≈ -5.09 → 8.1 μm

        vl_l = DashedLine(
            ax_l.c2p(x_mri, -7), ax_l.c2p(x_mri, y_mri_l),
            color=ORG, stroke_width=1.6, dash_length=0.12,
        )
        dot_l = Dot(ax_l.c2p(x_mri, y_mri_l), color=ORG, radius=0.09)
        ann_l = VGroup(
            Text("1.5T  64 MHz", font_size=12, color=ORG),
            Text("δ = 8.4 μm", font_size=13, color=INK, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.04).next_to(dot_l, UL, buff=0.06)

        self.play(Create(vl_l), FadeIn(dot_l), run_time=0.4)
        self.play(Write(ann_l), run_time=0.6)

        # ── Right panel: A_dB(f) log-log ─────────────────────────────────────
        ax_r = Axes(
            x_range=[5, 10, 1],    # same x
            y_range=[0, 3, 1],     # log10(A_dB): 1 → 1000 dB
            x_length=5.2,
            y_length=3.6,
            axis_config={"color": INK, "stroke_width": 1.3, "include_tip": False},
            tips=False,
        ).shift(RIGHT * 2.7 + DOWN * 0.5)

        xtl_r = VGroup(*[
            Text(t, font_size=11, color=GRAY)
            .next_to(ax_r.c2p(v, 0), DOWN, buff=0.13)
            for v, t in [(5, "100k"), (7, "10M"), (9, "1G"), (10, "10G")]
        ])
        ytl_r = VGroup(*[
            Text(t, font_size=11, color=GRAY)
            .next_to(ax_r.c2p(5, v), LEFT, buff=0.11)
            for v, t in [(1, "10 dB"), (2, "100 dB"), (3, "1000 dB")]
        ])
        xl_r = Text("f  (log)", font_size=14, color=INK).next_to(ax_r, DOWN, buff=0.48)
        yl_r = (Text("A  (dB, log)", font_size=14, color=INK)
                .rotate(PI / 2).next_to(ax_r, LEFT, buff=0.52))

        self.play(
            Create(ax_r),
            FadeIn(xtl_r), FadeIn(ytl_r), FadeIn(xl_r), FadeIn(yl_r),
            run_time=0.7,
        )

        # log10(A_dB) = log10(20*D/ln10) - log10(δ)
        #             = log10(20*D/ln10) - log_sd(log_f, rho)
        log_K = np.log10(20.0 * D / np.log(10.0))   # ≈ -2.061

        curve_r = ax_r.plot(
            lambda x: log_K - log_sd(x, RHO_CU),
            x_range=[5.0, 10.0],
            color=BLUE, stroke_width=3.2,
        )
        self.play(Create(curve_r), run_time=1.8)

        # 64 MHz marker (right panel)
        A_mri   = 20.0 / np.log(10.0) * D / (10.0 ** y_mri_l)   # ≈ 1033 dB
        y_mri_r = min(np.log10(A_mri), 3.0)                       # clamp to axes top

        vl_r = DashedLine(
            ax_r.c2p(x_mri, 0), ax_r.c2p(x_mri, y_mri_r),
            color=ORG, stroke_width=1.6, dash_length=0.12,
        )
        dot_r = Dot(ax_r.c2p(x_mri, y_mri_r), color=ORG, radius=0.09)
        ann_r = VGroup(
            Text("64 MHz →", font_size=12, color=ORG),
            Text("1033 dB/mm", font_size=13, color=INK, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.04).next_to(dot_r, UL, buff=0.06)

        self.play(Create(vl_r), FadeIn(dot_r), run_time=0.4)
        self.play(Write(ann_r), run_time=0.6)
        self.wait(0.8)


class B06_Materials(Scene):
    """
    Material comparison: copper vs aluminum vs stainless steel 304.
    Single log-log panel; 64 MHz vertical marker; legend with δ values.
    """

    MATS = [
        ("Copper",    1.68e-8, ACC,  3.5),
        ("Aluminum",  2.82e-8, BLUE, 2.8),
        ("SS 304",    7.40e-7, GRN,  2.8),
    ]

    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "Skin Depth: Copper vs Aluminum vs Steel",
            font_size=22, color=INK, weight=BOLD,
        ).to_edge(UP, buff=0.22)
        self.play(Write(title), run_time=0.6)

        ax = Axes(
            x_range=[5, 10, 1],
            y_range=[-7, -2, 1],
            x_length=9.2,
            y_length=4.4,
            axis_config={"color": INK, "stroke_width": 1.3, "include_tip": False},
            tips=False,
        ).shift(DOWN * 0.4)

        xtl = VGroup(*[
            Text(t, font_size=12, color=GRAY)
            .next_to(ax.c2p(v, -7), DOWN, buff=0.13)
            for v, t in [(5, "100 kHz"), (7, "10 MHz"), (9, "1 GHz"), (10, "10 GHz")]
        ])
        ytl = VGroup(*[
            Text(t, font_size=12, color=GRAY)
            .next_to(ax.c2p(5, v), LEFT, buff=0.13)
            for v, t in [
                (-2, "10 mm"), (-3, "1 mm"), (-4, "0.1 mm"),
                (-5, "10 μm"), (-6, "1 μm"), (-7, "0.1 μm"),
            ]
        ])
        xl = Text("Frequency", font_size=15, color=INK).next_to(ax, DOWN, buff=0.52)
        yl = (Text("Skin depth", font_size=15, color=INK)
              .rotate(PI / 2).next_to(ax, LEFT, buff=0.58))

        self.play(
            Create(ax), FadeIn(xtl), FadeIn(ytl), FadeIn(xl), FadeIn(yl),
            run_time=0.8,
        )

        # 64 MHz dashed vertical marker
        x_mri = np.log10(64e6)   # ≈ 7.806
        vl_mri = DashedLine(
            ax.c2p(x_mri, -7), ax.c2p(x_mri, -2),
            color=ORG, stroke_width=1.4, dash_length=0.12,
        )
        mri_lbl = (Text("64 MHz  (1.5T MRI)", font_size=12, color=ORG)
                   .next_to(ax.c2p(x_mri, -2), UP, buff=0.08))
        self.play(Create(vl_mri), Write(mri_lbl), run_time=0.5)

        # Plot each material + dot at 64 MHz
        legend_items = VGroup()
        for name, rho, col, sw in self.MATS:
            curve = ax.plot(
                lambda x, r=rho: log_sd(x, r),
                x_range=[5.0, 10.0],
                color=col, stroke_width=sw,
            )
            self.play(Create(curve), run_time=1.1)

            y64      = log_sd(x_mri, rho)
            delta_um = (10.0 ** y64) * 1e6   # μm

            dot = Dot(ax.c2p(x_mri, y64), color=col, radius=0.10)
            self.play(FadeIn(dot), run_time=0.2)

            swatch = Line(ORIGIN, RIGHT * 0.45, color=col, stroke_width=sw)
            lbl    = Text(
                f"{name}   {delta_um:.1f} μm @ 64 MHz",
                font_size=14, color=col,
            )
            legend_items.add(VGroup(swatch, lbl).arrange(RIGHT, buff=0.14))

        legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        legend_items.to_corner(UR, buff=0.35)
        self.play(FadeIn(legend_items), run_time=0.8)
        self.wait(0.8)
