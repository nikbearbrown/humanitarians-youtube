"""vox_scenes.py — medhavy-vol1-packet-spread
Reel: Wave Packet Spreading — Dispersion and Doubling Time
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — sigma(t) curve, t=0 Gaussian
  CRIMSON (#D55E00) — tau marker, t=tau Gaussian, doubling annotation

Gate A:
  Dot at tau on sigma curve; two Gaussian peaks are distinct shape states.
  Each .animate uses single chained method only.

Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]
"""

import sys, json, pathlib, os

os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import numpy as np

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(
            b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0
        )
        for b in _BS["beats"]
    })
except Exception:
    pass

_DEFAULTS = {"B03": 18.0}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_PacketRun — sigma(t) curve + Gaussian comparison
# =============================================================================
class B03_PacketRun(Scene):
    """Wave packet spreading: σ(t) vs t and Gaussian shape at t=0 and t=τ.
    Physics:
      σ(t) = σ₀ √(1 + (ℏt/2mσ₀²)²)
      τ = 2mσ₀²/ℏ ≈ 17.3 fs   (doubling time for √2×σ₀)
      σ₀ = 1 nm, m = m_e

    Layout (16:9):
      LEFT panel  (x ∈ [-6.1, -0.4]): σ(t) curve on Axes
        x_range=[0, 50 fs], y_range=[0, 2.5 nm]
        TEAL curve; CRIMSON dot at (τ, √2·σ₀); dashed horizontal at √2·σ₀
        Left panel center: [-3.4, -0.1, 0], x_length=5.2, y_length=4.0
      RIGHT panel (x ∈ [0.5, 6.3]): |Ψ(x)|² at t=0 and t=τ
        x_range=[-5, 5 nm], y_range=[0, 0.65 nm⁻¹] (peak of t=0 Gaussian)
        TEAL = t=0, CRIMSON = t=τ
        Right panel center: [3.5, -0.1, 0], x_length=5.2, y_length=4.0
      Header at y=3.15

    Gate B notes:
      numbers_to_include=[] on both axes of both panels (no tick number labels)
      Dot marker and chips placed clear of all axis strokes.
      Left panel x-axis stroke: y = -0.1 - 4.0/2 = -2.1 scene y
      Right panel x-axis stroke: y = -0.1 - 4.0/2 = -2.1 scene y
      Chips placed at y=-2.8 (below both x-axes, well clear)
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics constants ─────────────────────────────────────────────────
        hbar = 1.0546e-34  # J·s
        m_e  = 9.109e-31   # kg
        sigma0_nm = 1.0    # nm
        sigma0 = sigma0_nm * 1e-9  # m

        tau_s = 2 * m_e * sigma0**2 / hbar  # s
        tau_fs = tau_s * 1e15               # ~17.3 fs

        def sigma_nm(t_fs: float) -> float:
            t = t_fs * 1e-15
            return sigma0_nm * np.sqrt(1 + (hbar * t / (2 * m_e * sigma0**2))**2)

        sigma_tau_nm = sigma_nm(tau_fs)  # = sqrt(2) * sigma0_nm ≈ 1.414 nm

        def gauss_nm(x_nm: float, sig_nm: float) -> float:
            """Normalized |Ψ|² in nm⁻¹."""
            norm = 1.0 / (sig_nm * np.sqrt(np.pi))
            return norm * np.exp(-x_nm**2 / sig_nm**2)

        peak0 = gauss_nm(0, sigma0_nm)   # peak at t=0 (higher)
        peak_tau = gauss_nm(0, sigma_tau_nm)  # peak at t=τ (lower)

        t_max_fs = 3.0 * tau_fs  # show out to 3τ

        # ── header ────────────────────────────────────────────────────────────
        header = _ink_text("Wave Packet Spreading  τ = 17.3 fs",
                           font_size=21, font=DISPLAY)
        header.move_to([0.0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ─────────────────────────────────────────────────────────────────────
        # LEFT PANEL: σ(t) curve
        # ─────────────────────────────────────────────────────────────────────
        ax_left = Axes(
            x_range=[0, t_max_fs, tau_fs],
            y_range=[0, 2.5, 0.5],
            x_length=5.2,
            y_length=4.0,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to([-3.4, -0.1, 0])

        self.play(Create(ax_left), run_time=0.6)

        # axis labels
        xlbl_left = _ink_text("t (fs)", font_size=15)
        xlbl_left.next_to(ax_left.x_axis, DOWN, buff=0.22)
        ylbl_left = _ink_text("σ (nm)", font_size=15)
        ylbl_left.move_to([-6.0, -0.1, 0])

        self.play(FadeIn(xlbl_left), FadeIn(ylbl_left), run_time=0.3)

        # σ(t) curve (TEAL)
        sigma_curve = ax_left.plot(
            lambda t: sigma_nm(t),
            x_range=[0, t_max_fs - 0.1],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(sigma_curve), run_time=0.9)

        # Horizontal dashed line at σ₀√2
        dash_y_scene = _c2p(ax_left, 0, sigma_tau_nm)
        dash_x_left  = _c2p(ax_left, 0, sigma_tau_nm)
        dash_x_right = _c2p(ax_left, t_max_fs * 0.95, sigma_tau_nm)
        dashed_line = DashedLine(
            start=dash_x_left,
            end=dash_x_right,
            color=CRIMSON,
            stroke_width=1.4,
            dash_length=0.12,
        )
        self.play(Create(dashed_line), run_time=0.4)

        # CRIMSON dot at (τ, √2·σ₀)
        tau_dot_pos = _c2p(ax_left, tau_fs, sigma_tau_nm)
        tau_dot = Dot(point=tau_dot_pos, radius=0.1, color=CRIMSON,
                      fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(tau_dot), run_time=0.3)

        # Label: "√2·σ₀" placed well ABOVE the dashed line, centered left panel.
        # The dashed line is at data y=1.414 nm; the label goes 0.55 scene units
        # above so it clears the dashed stroke entirely.
        sqrt2_lbl = _ink_text("√2·σ₀ = 1.414 nm", font_size=15)
        sqrt2_lbl_y = float(dash_y_scene[1]) if isinstance(dash_y_scene, np.ndarray) else 0
        sqrt2_lbl.move_to([-4.0, sqrt2_lbl_y + 0.55, 0])
        self.play(FadeIn(sqrt2_lbl), run_time=0.3)

        # Label: "τ" on x-axis — placed below x-axis, at tau x position
        tau_x_scene = _c2p(ax_left, tau_fs, 0)
        tau_xlbl = _ink_text("τ", font_size=16)
        tau_xlbl_x = float(tau_x_scene[0]) if isinstance(tau_x_scene, np.ndarray) else 0
        # Place below x-axis (which is at scene y ≈ -2.1)
        tau_xlbl.move_to([tau_xlbl_x, -2.4, 0])
        self.play(FadeIn(tau_xlbl), run_time=0.25)

        # ─────────────────────────────────────────────────────────────────────
        # RIGHT PANEL: Gaussian shapes at t=0 and t=τ
        # ─────────────────────────────────────────────────────────────────────
        ax_right = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 0.70, 0.2],
            x_length=5.2,
            y_length=4.0,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to([3.5, -0.1, 0])

        self.play(Create(ax_right), run_time=0.6)

        xlbl_right = _ink_text("x (nm)", font_size=15)
        xlbl_right.next_to(ax_right.x_axis, DOWN, buff=0.22)
        ylbl_right = _ink_text("|Ψ|² (nm⁻¹)", font_size=14)
        ylbl_right.move_to([0.65, -0.1, 0])

        self.play(FadeIn(xlbl_right), FadeIn(ylbl_right), run_time=0.3)

        # t=0 Gaussian: TEAL (taller, narrower)
        gauss0_curve = ax_right.plot(
            lambda x: gauss_nm(x, sigma0_nm),
            x_range=[-3.45, 3.45],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(gauss0_curve), run_time=0.6)

        # t=τ Gaussian: CRIMSON (shorter, broader)
        gauss_tau_curve = ax_right.plot(
            lambda x: gauss_nm(x, sigma_tau_nm),
            x_range=[-3.45, 3.45],
            color=CRIMSON,
            stroke_width=2.5,
        )
        self.play(Create(gauss_tau_curve), run_time=0.6)

        # Label the two curves with small dots at their peaks for Gate A states
        peak0_pos = _c2p(ax_right, 0, peak0)
        dot0 = Dot(point=peak0_pos, radius=0.08, color=TEAL,
                   fill_opacity=1).set_stroke(width=0, opacity=0)
        peak_tau_pos = _c2p(ax_right, 0, peak_tau)
        dot_tau = Dot(point=peak_tau_pos, radius=0.08, color=CRIMSON,
                      fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot0), FadeIn(dot_tau), run_time=0.3)

        # Legend labels — placed right of the right panel, no strokes there
        lbl_t0   = _ink_text("t = 0", font_size=15)
        lbl_ttau = _ink_text("t = τ", font_size=15)
        peak0_scene_y = float(peak0_pos[1]) if isinstance(peak0_pos, np.ndarray) else 0
        peak_tau_scene_y = float(peak_tau_pos[1]) if isinstance(peak_tau_pos, np.ndarray) else 0
        lbl_t0.move_to([6.05, peak0_scene_y, 0])
        lbl_ttau.move_to([6.05, peak_tau_scene_y, 0])
        self.play(FadeIn(lbl_t0), FadeIn(lbl_ttau), run_time=0.3)

        # ── chips ─────────────────────────────────────────────────────────────
        # x-axis strokes at scene y ≈ -2.1 (both panels)
        # Place chips at y=-2.8 (below both axes), centered
        vg_chip = LabelChip("v_g = ℏk₀/m", accent=TEAL, size=19)
        vg_chip.move_to([-1.5, -2.8, 0])
        self.play(GrowFromCenter(vg_chip), run_time=0.4)

        sigma_chip = LabelChip("σ(τ) = √2·σ₀", accent=CRIMSON, size=19)
        sigma_chip.move_to([1.5, -2.8, 0])
        self.play(GrowFromCenter(sigma_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = (0.4 + 0.6 + 0.3 + 0.9 + 0.4 + 0.3 + 0.3 + 0.25 +
                   0.6 + 0.3 + 0.6 + 0.6 + 0.3 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
