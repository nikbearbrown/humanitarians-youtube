"""vox_scenes.py — medhavy-vol1-packet-spread/short (9:16 portrait)
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — sigma(t) curve
  CRIMSON (#D55E00) — tau marker and broadened Gaussian

Safe area: 9:16 portrait ±1.95x / ±3.4y

Layout: single panel σ(t) curve only (portrait width too narrow for dual panel).
  Axes: x_range=[0, 52 fs], y_range=[0, 2.5 nm]
  x_length=3.5, y_length=4.5
  Centered at ORIGIN + UP*0.3
  x-axis stroke at scene y = 0.3 - 4.5/2 = -1.95
  Chips placed at y=-2.8 and y=-3.2 (below x-axis stroke)
  Labels placed ABOVE their reference lines (not at the same y)
"""

import sys, json, pathlib, os

os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4]
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

_DEFAULTS = {"B03": 28.79}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_PacketRun — portrait σ(t) curve
# =============================================================================
class B03_PacketRun(Scene):
    """Portrait wave packet spreading: σ(t) vs t.
    Physics: σ(t) = σ₀√(1+(ℏt/2mσ₀²)²); τ=17.3 fs; σ(τ)=√2·σ₀
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics ────────────────────────────────────────────────────────────
        hbar = 1.0546e-34
        m_e  = 9.109e-31
        sigma0_nm = 1.0
        sigma0 = sigma0_nm * 1e-9
        tau_s = 2 * m_e * sigma0**2 / hbar
        tau_fs = tau_s * 1e15  # ≈ 17.27 fs
        t_max_fs = 3.0 * tau_fs

        def sigma_nm(t_fs: float) -> float:
            t = t_fs * 1e-15
            return sigma0_nm * np.sqrt(1 + (hbar * t / (2 * m_e * sigma0**2))**2)

        sigma_tau_nm = sigma_nm(tau_fs)  # ≈ 1.414 nm

        # ── header ─────────────────────────────────────────────────────────────
        header = _ink_text("Wave Packet  τ = 17.3 fs",
                            font_size=16, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── axes ───────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, t_max_fs, tau_fs],
            y_range=[0, 2.5, 0.5],
            x_length=3.5,
            y_length=4.5,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + UP * 0.3)

        self.play(Create(axes), run_time=0.6)

        xlbl = _ink_text("t (fs)", font_size=14)
        xlbl.next_to(axes.x_axis, DOWN, buff=0.2)
        ylbl = _ink_text("σ (nm)", font_size=12)
        ylbl.move_to([-1.78, 0.3, 0])
        self.play(FadeIn(xlbl), FadeIn(ylbl), run_time=0.3)

        # ── σ(t) curve ─────────────────────────────────────────────────────────
        sigma_curve = axes.plot(
            lambda t: sigma_nm(t),
            x_range=[0, t_max_fs - 0.1],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(sigma_curve), run_time=0.9)

        # Dashed horizontal at σ₀√2
        dash_y_scene = _c2p(axes, 0, sigma_tau_nm)
        dash_end = _c2p(axes, t_max_fs * 0.92, sigma_tau_nm)
        dashed_line = DashedLine(
            start=dash_y_scene,
            end=dash_end,
            color=CRIMSON,
            stroke_width=1.4,
            dash_length=0.10,
        )
        self.play(Create(dashed_line), run_time=0.4)

        # CRIMSON dot at (τ, √2·σ₀)
        tau_dot_pos = _c2p(axes, tau_fs, sigma_tau_nm)
        tau_dot = Dot(point=tau_dot_pos, radius=0.1, color=CRIMSON,
                      fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(tau_dot), run_time=0.3)

        # Label "√2·σ₀" — place at the right end of the dashed line,
        # ABOVE the dashed line, where no sigma curve stroke passes.
        # At t=t_max_fs*0.92, sigma(t) is much higher than 1.414 nm, so no overlap.
        # We place the label at the very right end of the dashed line + offset above.
        dash_y_val = float(dash_y_scene[1]) if isinstance(dash_y_scene, np.ndarray) else 0
        dash_right = _c2p(axes, t_max_fs * 0.70, sigma_tau_nm)
        dash_right_x = float(dash_right[0]) if isinstance(dash_right, np.ndarray) else 1.0
        sqrt2_lbl = _ink_text("√2·σ₀", font_size=12)
        # Place above the dashed line by 0.3 scene units at the right side of label area
        # At t=0.7*t_max, sigma >> 1.414, so the curve is above the label, no overlap.
        sqrt2_lbl.move_to([dash_right_x, dash_y_val + 0.28, 0])
        self.play(FadeIn(sqrt2_lbl), run_time=0.3)

        # Label "τ" below x-axis, at tau x position
        # x-axis stroke at scene y = 0.3 - 4.5/2 = -1.95
        tau_x_scene = _c2p(axes, tau_fs, 0)
        tau_xlbl = _ink_text("τ", font_size=15)
        tau_xlbl_x = float(tau_x_scene[0]) if isinstance(tau_x_scene, np.ndarray) else 0
        tau_xlbl.move_to([tau_xlbl_x, -2.2, 0])
        self.play(FadeIn(tau_xlbl), run_time=0.25)

        # ── chips ──────────────────────────────────────────────────────────────
        # x-axis stroke at y ≈ -1.95; chips at y=-2.8 and y=-3.2 (below, centered)
        vg_chip = LabelChip("v_g = ℏk₀/m", accent=TEAL, size=16)
        vg_chip.move_to([0, -2.8, 0])
        self.play(GrowFromCenter(vg_chip), run_time=0.4)

        sigma_chip = LabelChip("σ(τ)=√2·σ₀", accent=CRIMSON, size=16)
        sigma_chip.move_to([0, -3.2, 0])
        self.play(GrowFromCenter(sigma_chip), run_time=0.35)

        # ── hold ───────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.6 + 0.3 + 0.9 + 0.4 + 0.3 + 0.3 + 0.25 + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
