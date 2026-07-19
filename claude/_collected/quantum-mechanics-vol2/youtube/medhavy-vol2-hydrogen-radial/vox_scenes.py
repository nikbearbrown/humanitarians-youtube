"""vox_scenes.py — medhavy-vol2-hydrogen-radial
Reel: Hydrogen 1s Radial Probability Density — Why Mean ≠ Mode
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — P(r) curve, r_mp marker (mode)
  CRIMSON (#D55E00) — mean marker, mean annotation

Gate A:
  Two distinct Dot markers (mode and mean); curve is shape state.
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
# B03_HydrogenRun — P(r) = (4/a₀³)r²e^(-2r/a₀) with mode and mean markers
# =============================================================================
class B03_HydrogenRun(Scene):
    """Hydrogen 1s radial probability density.
    Physics:
      P(r) = (4/a₀³) r² e^(-2r/a₀)
      r_mp = a₀   (mode: where dP/dr = 0)
      ⟨r⟩ = 3a₀/2  (mean: pulled right by tail)
      a₀ ≈ 0.0529 nm

    Layout:
      Axes: x_range=[0, 7] (in units of a₀), y_range=[0, 0.55] (in units of a₀⁻¹)
      x_length=10.0, y_length=5.0
      Axes centered at ORIGIN + LEFT*0.2 + DOWN*0.1
      x-axis stroke at scene y = -0.1 - 5.0/2 = -2.6
      Mode dashed line: x=1 data (a₀), TEAL
      Mean dashed line: x=1.5 data (3a₀/2), CRIMSON
      Labels placed ABOVE the curve top (y > peak) or at a safe x
      Chips at y=-2.8 (below x-axis at y=-2.6, within ±3.4 safe area)

    Gate B notes:
      numbers_to_include=[] on both axes
      Dashed lines at x=1 and x=1.5 are vertical; labels for them
      placed above the dashed line tops (at y=0.55 data → scene y near axes top)
      but the labels go at fixed scene y = 2.0 (above axes top ≈ -0.1+5.0/2=2.4)
      Actually place labels at scene y=2.2 (above axes top at y=2.4 data boundary)
      Chip at y=-2.8 is BELOW x-axis at -2.6 (safe).
    """

    def construct(self):
        dur = _dur("B03")

        # ── header ────────────────────────────────────────────────────────────
        header = _ink_text("Hydrogen 1s  P(r) = (4/a₀³) r² e^(−2r/a₀)",
                           font_size=20, font=DISPLAY)
        header.move_to([0.0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        # x in units of a₀ (dimensionless); y in units of a₀⁻¹ (normalized)
        # Peak of P(r) at r=a₀: P(a₀) = (4/a₀³)×a₀²×e^(-2) = (4/a₀)e^(-2) → in a₀⁻¹: 4e^(-2) ≈ 0.541
        axes = Axes(
            x_range=[0, 7.0, 1],
            y_range=[0, 0.55, 0.1],
            x_length=10.0,
            y_length=5.0,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + LEFT * 0.2 + DOWN * 0.1)

        self.play(Create(axes), run_time=0.6)

        # Axis labels
        x_lbl = _ink_text("r / a₀", font_size=16)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.22)
        y_lbl = _ink_text("P (a₀⁻¹)", font_size=15)
        y_lbl.move_to([-6.0, -0.1, 0])

        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── P(r) curve ────────────────────────────────────────────────────────
        # In units of a₀: P(ξ) = 4ξ²e^(-2ξ) where ξ = r/a₀; units are a₀⁻¹
        def P_normalized(xi: float) -> float:
            if xi <= 0:
                return 0
            return 4 * xi**2 * np.exp(-2 * xi)

        P_curve = axes.plot(P_normalized, x_range=[0.01, 6.95], color=TEAL,
                            stroke_width=2.8)
        self.play(Create(P_curve), run_time=0.9)

        # ── Mode dashed line at ξ=1 (r=a₀) ──────────────────────────────────
        # Vertical dashed line from (1, 0) to (1, 0.55)
        mode_bot = _c2p(axes, 1.0, 0.0)
        mode_top = _c2p(axes, 1.0, 0.55)
        mode_dash = DashedLine(start=mode_bot, end=mode_top, color=TEAL,
                               stroke_width=1.6, dash_length=0.12)
        self.play(Create(mode_dash), run_time=0.4)

        # Dot at peak (1, 4e^-2 ≈ 0.541)
        mode_dot_pos = _c2p(axes, 1.0, 4 * np.exp(-2))
        mode_dot = Dot(point=mode_dot_pos, radius=0.10, color=TEAL,
                       fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(mode_dot), run_time=0.3)

        # Label "r_mp = a₀" placed LEFT of the mode line, ABOVE the curve
        # Axes top in scene: -0.1 + 5.0/2 = 2.4; place label at y=2.2 (just below header area)
        # At x=1 data, scene x ≈ axes_left + 1/(7)*10 - 0.2 ... just compute from mode_dot_pos
        mode_x_scene = float(mode_dot_pos[0]) if isinstance(mode_dot_pos, np.ndarray) else -2.0
        mode_lbl = _ink_text("r_mp = a₀", font_size=16)
        mode_lbl.move_to([mode_x_scene - 0.9, 2.2, 0])
        self.play(FadeIn(mode_lbl), run_time=0.3)

        # ── Mean dashed line at ξ=1.5 (r=3a₀/2) ─────────────────────────────
        mean_bot = _c2p(axes, 1.5, 0.0)
        mean_top = _c2p(axes, 1.5, 0.55)
        mean_dash = DashedLine(start=mean_bot, end=mean_top, color=CRIMSON,
                               stroke_width=1.6, dash_length=0.12)
        self.play(Create(mean_dash), run_time=0.4)

        # Dot at mean height
        mean_dot_pos = _c2p(axes, 1.5, P_normalized(1.5))
        mean_dot = Dot(point=mean_dot_pos, radius=0.10, color=CRIMSON,
                       fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(mean_dot), run_time=0.3)

        # Label "⟨r⟩ = 3a₀/2" to the RIGHT of the mean line, above curve
        mean_x_scene = float(mean_dot_pos[0]) if isinstance(mean_dot_pos, np.ndarray) else -1.0
        mean_lbl = _ink_text("⟨r⟩ = 3a₀/2", font_size=16)
        mean_lbl.move_to([mean_x_scene + 1.1, 2.2, 0])
        self.play(FadeIn(mean_lbl), run_time=0.3)

        # ── chips ─────────────────────────────────────────────────────────────
        # x-axis stroke at scene y ≈ -2.6; chips at y=-2.8 (just below)
        rmp_chip = LabelChip("r_mp = a₀", accent=TEAL, size=19)
        rmp_chip.move_to([-2.0, -2.8, 0])
        self.play(GrowFromCenter(rmp_chip), run_time=0.4)

        mean_chip = LabelChip("⟨r⟩ = 1.5 a₀", accent=CRIMSON, size=19)
        mean_chip.move_to([2.0, -2.8, 0])
        self.play(GrowFromCenter(mean_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = (0.4 + 0.6 + 0.3 + 0.9 +
                   0.4 + 0.3 + 0.3 + 0.4 + 0.3 + 0.3 +
                   0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
