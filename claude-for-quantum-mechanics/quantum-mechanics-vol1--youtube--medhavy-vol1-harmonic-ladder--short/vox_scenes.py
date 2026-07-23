"""vox_scenes.py — medhavy-vol1-harmonic-ladder/short (9:16 portrait)
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — energy rungs, parabola
  CRIMSON (#D55E00) — zero-point chip

Safe area: 9:16 portrait ±1.95x / ±3.4y
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

_DEFAULTS = {"B03": 22.18}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_HarmonicRun — portrait (9:16) parabola + 5 equally-spaced energy rungs
# =============================================================================
class B03_HarmonicRun(Scene):
    """Portrait quantum harmonic oscillator energy ladder.
    Physics:
      E_n = ℏω(n + 1/2),  ω = 10¹⁴ rad/s, m = m_e
      ℏω ≈ 0.066 eV  →  spacing uniform = 0.066 eV
      E_0 = 0.033 eV  (non-zero ground state)
    Layout (portrait ±1.95x / ±3.4y):
      Axes: x_range=[-2, 2]; y_range=[0, 0.40]; x_length=3.6; y_length=4.5
      Axes centered at ORIGIN + UP*0.2
      x-axis stroke at scene y = 0.2 - 4.5/2 = -2.05
      Header at y=3.2 (above axes, fits ±1.95x safe area)
      Labels: at x=1.45 (right edge, within ±1.95 safe area)
      Chips: at x=-1.5, y=-3.0 and y=-3.35 (below axes, left of center)
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics ────────────────────────────────────────────────────────────
        hbar_omega_eV = 0.066  # ℏω in eV
        E_n = [hbar_omega_eV * (n + 0.5) for n in range(5)]
        # [0.033, 0.099, 0.165, 0.231, 0.297] eV

        # ── header (≤19 chars for portrait safe area) ─────────────────────────
        # "Harmonic Osc" = 13 chars (with space), font_size=19
        header = _ink_text("Harmonic Osc  ℏω=0.066 eV",
                            font_size=16, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 0.40, 0.1],
            x_length=3.6,
            y_length=4.5,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + UP * 0.2)

        self.play(Create(axes), run_time=0.6)

        # axis labels
        x_lbl = _ink_text("x", font_size=14)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.18)

        y_lbl = _ink_text("E (eV)", font_size=13)
        y_lbl.next_to(axes.y_axis, LEFT, buff=0.12)

        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── parabola V(x) ─────────────────────────────────────────────────────
        # V(x) = A*x²; choose A so V(2) ≈ E_4 = 0.297 → A = 0.297/4 ≈ 0.074
        PARAB_A = 0.074

        def parabola_fn(x: float) -> float:
            val = PARAB_A * x**2
            return min(val, 0.39)

        parab_curve = axes.plot(parabola_fn, x_range=[-1.98, 1.98], color=SLATE,
                                stroke_width=2.0)
        self.play(Create(parab_curve), run_time=0.7)

        # ── energy rungs ──────────────────────────────────────────────────────
        n_labels = ["E₀=0.033", "E₁=0.099", "E₂=0.165", "E₃=0.231", "E₄=0.297"]

        for n_idx, (e_eV, lbl_str) in enumerate(zip(E_n, n_labels)):
            # Classical turning points clipped to axes range
            x_turn = min(np.sqrt(e_eV / PARAB_A), 1.95)

            rung_start = _c2p(axes, -x_turn, e_eV)
            rung_end   = _c2p(axes,  x_turn, e_eV)
            rung = Line(
                start=rung_start,
                end=rung_end,
                stroke_width=2.0,
                color=TEAL,
            )

            # Label centered ABOVE each rung to avoid overlapping the rung stroke.
            # Rungs span full width in portrait, so side placement overlaps.
            # Offset +0.20 scene units above the rung y position.
            scene_rung_y = _c2p(axes, 0, e_eV)
            lbl = _ink_text(lbl_str, font_size=12)
            lbl_y = float(scene_rung_y[1]) if isinstance(scene_rung_y, np.ndarray) else 0
            # Place label at x=0, y = rung_y + 0.20 (centered above rung)
            lbl.move_to([0.0, lbl_y + 0.20, 0])

            # Dot at rung center for Gate A shape state
            rung_mid = _c2p(axes, 0, e_eV)
            dot = Dot(point=rung_mid, radius=0.07, color=TEAL,
                      fill_opacity=1).set_stroke(width=0, opacity=0)

            self.play(Create(rung), run_time=0.3)
            self.play(FadeIn(lbl), FadeIn(dot), run_time=0.25)

        # ── chips ─────────────────────────────────────────────────────────────
        # x-axis stroke at scene y = 0.2 - 4.5/2 = -2.05
        # Place chips at y=-3.0 and y=-3.35 (below x-axis, well away from stroke)
        # x=-1.5: left of center, no axes strokes there
        zp_chip = LabelChip("E₀ > 0", accent=CRIMSON, size=17)
        zp_chip.move_to([-0.5, -3.0, 0])
        self.play(GrowFromCenter(zp_chip), run_time=0.4)

        spacing_chip = LabelChip("gap = ℏω", accent=TEAL, size=17)
        spacing_chip.move_to([-0.5, -3.2, 0])
        self.play(GrowFromCenter(spacing_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.6 + 0.3 + 0.7 + 5*(0.3 + 0.25) + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
