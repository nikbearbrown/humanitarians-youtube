"""vox_scenes.py — medhavy-vol2-hydrogen-radial/short (9:16 portrait)
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — P(r) curve, r_mp marker
  CRIMSON (#D55E00) — mean marker

Safe area: 9:16 portrait ±1.95x / ±3.4y

Layout: P(r) curve on portrait axes.
  Axes: x_range=[0, 7], y_range=[0, 0.55], x_length=3.5, y_length=4.5
  Centered at ORIGIN + UP*0.3
  x-axis stroke at scene y = 0.3 - 4.5/2 = -1.95
  Labels: placed above the dashed lines, at scene y=2.1 (within safe area)
  Chips at y=-2.7 and y=-3.15
  y-axis label moved to fixed position within ±1.95x safe area
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

_DEFAULTS = {"B03": 26.04}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_HydrogenRun — portrait P(r) with mode and mean markers
# =============================================================================
class B03_HydrogenRun(Scene):
    """Portrait hydrogen 1s radial probability density."""

    def construct(self):
        dur = _dur("B03")

        # ── header ─────────────────────────────────────────────────────────────
        header = _ink_text("Hydrogen 1s  P(r)", font_size=17, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── axes ───────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 7.0, 1],
            y_range=[0, 0.55, 0.1],
            x_length=3.5,
            y_length=4.5,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + UP * 0.3)

        self.play(Create(axes), run_time=0.6)

        xlbl = _ink_text("r / a₀", font_size=13)
        xlbl.next_to(axes.x_axis, DOWN, buff=0.18)
        ylbl = _ink_text("P(r)", font_size=13)
        ylbl.move_to([-1.82, 0.3, 0])
        self.play(FadeIn(xlbl), FadeIn(ylbl), run_time=0.3)

        # ── P(r) curve ─────────────────────────────────────────────────────────
        def P_norm(xi):
            return 0 if xi <= 0 else 4 * xi**2 * np.exp(-2 * xi)

        P_curve = axes.plot(P_norm, x_range=[0.01, 6.95], color=TEAL, stroke_width=2.5)
        self.play(Create(P_curve), run_time=0.9)

        # ── Mode dashed line ξ=1 ─────────────────────────────────────────────
        mode_bot = _c2p(axes, 1.0, 0.0)
        mode_top = _c2p(axes, 1.0, 0.55)
        mode_dash = DashedLine(start=mode_bot, end=mode_top, color=TEAL,
                               stroke_width=1.5, dash_length=0.1)
        self.play(Create(mode_dash), run_time=0.4)

        mode_dot_pos = _c2p(axes, 1.0, 4 * np.exp(-2))
        mode_dot = Dot(point=mode_dot_pos, radius=0.09, color=TEAL,
                       fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(mode_dot), run_time=0.3)

        # Label above dashed line tops (axes top at scene y = 0.3 + 4.5/2 = 2.55)
        # Place at y=2.1 to stay inside frame
        mode_x_scene = float(mode_dot_pos[0]) if isinstance(mode_dot_pos, np.ndarray) else -0.5
        mode_lbl = _ink_text("r_mp=a₀", font_size=12)
        mode_lbl.move_to([mode_x_scene - 0.55, 2.1, 0])
        self.play(FadeIn(mode_lbl), run_time=0.3)

        # ── Mean dashed line ξ=1.5 ────────────────────────────────────────────
        mean_bot = _c2p(axes, 1.5, 0.0)
        mean_top = _c2p(axes, 1.5, 0.55)
        mean_dash = DashedLine(start=mean_bot, end=mean_top, color=CRIMSON,
                               stroke_width=1.5, dash_length=0.1)
        self.play(Create(mean_dash), run_time=0.4)

        mean_dot_pos = _c2p(axes, 1.5, P_norm(1.5))
        mean_dot = Dot(point=mean_dot_pos, radius=0.09, color=CRIMSON,
                       fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(mean_dot), run_time=0.3)

        mean_x_scene = float(mean_dot_pos[0]) if isinstance(mean_dot_pos, np.ndarray) else 0.0
        mean_lbl = _ink_text("⟨r⟩=3a₀/2", font_size=12)
        mean_lbl.move_to([mean_x_scene + 0.62, 2.1, 0])
        self.play(FadeIn(mean_lbl), run_time=0.3)

        # ── chips ──────────────────────────────────────────────────────────────
        # x-axis at y ≈ -1.95; chips at y=-2.7 and y=-3.15
        rmp_chip = LabelChip("r_mp = a₀", accent=TEAL, size=16)
        rmp_chip.move_to([0, -2.7, 0])
        self.play(GrowFromCenter(rmp_chip), run_time=0.4)

        mean_chip = LabelChip("⟨r⟩ = 1.5 a₀", accent=CRIMSON, size=16)
        mean_chip.move_to([0, -3.15, 0])
        self.play(GrowFromCenter(mean_chip), run_time=0.35)

        # ── hold ───────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.6 + 0.3 + 0.9 + 0.4 + 0.3 + 0.3 + 0.4 + 0.3 + 0.3 + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
