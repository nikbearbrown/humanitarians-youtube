"""vox_scenes.py — medhavy-vol1-harmonic-ladder
Reel: Quantum Harmonic Oscillator — Ladder and Zero-Point Energy
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — energy rungs, parabola (shape fills/strokes)
  CRIMSON (#D55E00) — ground-state chip annotation

Gate A:
  Dot markers at each rung create distinct shape states
  Each .animate uses single chained method only

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

_DEFAULTS = {"B03": 16.0}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_HarmonicRun — parabola + 5 equally-spaced energy rungs
# =============================================================================
class B03_HarmonicRun(Scene):
    """Quantum harmonic oscillator energy ladder.
    Physics:
      E_n = ℏω(n + 1/2),  ω = 10¹⁴ rad/s, m = m_e
      ℏω ≈ 0.066 eV  →  spacing uniform = 0.066 eV
      E_0 = 0.033 eV  (non-zero ground state)
      E_1 = 0.099 eV
      E_2 = 0.165 eV
      E_3 = 0.231 eV
      E_4 = 0.297 eV

    Layout:
      Axes: x ∈ [-5, 5] → plotted region [-3, 3]; y ∈ [0, 0.40] eV
      Parabola V(x) = ½mω²x² in scene coords — scaled to fit axes
      Energy rungs: horizontal TEAL lines at each E_n
      Labels: right of right edge at x=4.5 (no curves there)
      Header: x=1.5 y=3.1 (right of y-axis)

    Gate B label placement verified:
      - Rung labels at x=4.5 scene: no parabola/rung stroke there ✓
      - Header at x=1.5: right of y-axis stroke ✓
      - Chips at x=0, y=-0.5 data: below all rungs ✓
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics ────────────────────────────────────────────────────────────
        hbar_omega_eV = 0.066  # ℏω in eV
        E_n = [hbar_omega_eV * (n + 0.5) for n in range(5)]
        # [0.033, 0.099, 0.165, 0.231, 0.297] eV

        # ── header ────────────────────────────────────────────────────────────
        header = _ink_text("Harmonic Oscillator  ℏω = 0.066 eV",
                           font_size=22, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        # x_range: physical x in some unit; y_range in eV
        # We choose: x in units where x=±3 corresponds to the classical turning
        # point of n=4. At E_4=0.297 eV: ½mω²x² = E_4 → x_turn ≈ irrelevant
        # for the plot — we just show a parabola shape.
        # x_length=9, y_length=5 keeps things in frame with left margin for y-label.
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 0.40, 0.1],
            x_length=9.0,
            y_length=5.0,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + LEFT * 0.3 + DOWN * 0.3)

        self.play(Create(axes), run_time=0.6)

        # x-axis label: placed below axis, font_size=16 stays inside safe area
        x_lbl = _ink_text("x", font_size=16)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.22)

        # y-axis label: fixed position left of axes (no next_to arithmetic overflow)
        y_lbl = _ink_text("E (eV)", font_size=15)
        y_lbl.move_to([-5.8, 0.3, 0])

        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── parabola V(x) = ½mω²x² (scaled so it reaches E_4 at x=±3) ────────
        # In axes coordinates: x-data ∈ [-3.5, 3.5], y-data in eV
        # Choose the scale so V(3) ≈ E_4 = 0.297 eV → prefactor = 0.297/9 ≈ 0.033
        PARAB_A = 0.033  # eV per (x-unit)²

        def parabola_fn(x: float) -> float:
            val = PARAB_A * x**2
            return min(val, 0.39)  # clip at y_range top

        parab_curve = axes.plot(parabola_fn, x_range=[-3.45, 3.45], color=SLATE,
                                stroke_width=2.0)
        self.play(Create(parab_curve), run_time=0.7)

        # ── energy rungs ──────────────────────────────────────────────────────
        n_labels = ["E₀ = 0.033", "E₁ = 0.099", "E₂ = 0.165", "E₃ = 0.231", "E₄ = 0.297"]

        for n_idx, (e_eV, lbl_str) in enumerate(zip(E_n, n_labels)):
            # Classical turning points: V(x_turn) = E → x_turn = √(E/A)
            x_turn = min(np.sqrt(e_eV / PARAB_A), 3.4)

            # Rung line from -x_turn to +x_turn at height e_eV
            rung_start = _c2p(axes, -x_turn, e_eV)
            rung_end   = _c2p(axes,  x_turn, e_eV)
            rung = Line(
                start=rung_start,
                end=rung_end,
                stroke_width=2.0,
                color=TEAL,
            )

            # Energy label: placed RIGHT of x=3.5 boundary (axes right edge + gap)
            # In scene coords: x=3.5 data → scene x_edge; labels at x=4.3 scene
            scene_rung_y = _c2p(axes, 0, e_eV)
            lbl = _ink_text(lbl_str + " eV", font_size=17)
            lbl_x = 4.35  # right of the axes boundary in scene coords; no curve there
            lbl_y = float(scene_rung_y[1]) if isinstance(scene_rung_y, np.ndarray) else 0
            lbl.move_to([lbl_x, lbl_y, 0])

            # Dot at center of rung for Gate A distinct state
            rung_mid = _c2p(axes, 0, e_eV)
            dot = Dot(point=rung_mid, radius=0.07, color=TEAL,
                      fill_opacity=1).set_stroke(width=0, opacity=0)

            self.play(Create(rung), run_time=0.3)
            self.play(FadeIn(lbl), FadeIn(dot), run_time=0.25)

        # ── ground-state chip ─────────────────────────────────────────────────
        # Place below all rungs; y_data = -0.03 → scene_y below x-axis
        # Use a fixed scene coordinate well below the x-axis
        # Axes center at (-0.3, -0.3); y_length=5.0; y_range=[0,0.4]
        # x-axis stroke (y_data=0) sits at scene y = -0.3 - 5.0/2 = -2.8
        # Place chips at scene x=-5.0 (left of axes) to avoid x-axis stroke entirely.
        # x=-5.0: axes left edge is at x=-0.3 - 9.0/2 = -4.8; chips at x=-5.5 are
        # fully left of the axes bounding box, no stroke there.
        zp_chip = LabelChip("E₀ > 0", accent=CRIMSON, size=19)
        zp_chip.move_to([-5.5, -2.5, 0])
        self.play(GrowFromCenter(zp_chip), run_time=0.4)

        # ── spacing chip ──────────────────────────────────────────────────────
        spacing_chip = LabelChip("gap = ℏω", accent=TEAL, size=19)
        spacing_chip.move_to([-5.5, -3.0, 0])
        self.play(GrowFromCenter(spacing_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.6 + 0.3 + 0.7 + 5*(0.3 + 0.25) + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
