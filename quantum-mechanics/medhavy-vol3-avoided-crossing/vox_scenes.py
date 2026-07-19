"""vox_scenes.py — medhavy-vol3-avoided-crossing
Reel: Two-Level Avoided Crossing — Energy Levels That Never Touch
Palette: medhavy (Okabe-Ito)

Physics:
  Two-level Hamiltonian: E₁=0, E₂=λ, coupling V=0.1 eV
  Perturbed eigenvalues:
    E±(λ) = (E₁+E₂)/2 ± √((ΔE/2)² + V²)
    where ΔE = E₂ − E₁ = λ
  At degeneracy (λ=1): gap = 2|V| = 0.2 eV
  Unperturbed (V=0): E₁=0 (flat), E₂=λ (diagonal) — they cross at λ=1

Display:
  x_range=[0, 2] eV (λ); y_range=[-0.6, 1.6] eV
  TEAL: upper branch E+(λ)
  CRIMSON: lower branch E-(λ)
  SLATE dashed: unperturbed E₁=0 (flat) and E₂=λ (diagonal)
  DoubleArrow at λ=1 showing gap = 0.2 eV

Gate A: axes.c2p not used for arithmetic — label positions via sx/sy helpers
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]

Layout:
  Axes center: (0, -0.1); x_range=[0,2], y_range=[-0.6,1.6]
  x_length=9.0, y_length=5.0
  x_scale = 9.0/2 = 4.5 u/eV; y_scale = 5.0/2.2 ≈ 2.273 u/eV

  sx(lam) = 0 - 4.5 + lam/2 * 9.0 = -4.5 + lam*4.5
  sy(e)   = -0.1 - 2.5 + (e+0.6)/2.2 * 5.0 = -2.6 + (e+0.6)*2.273

  Key points:
    λ=1: sx = 0.0
    E+(1) = 0.5 + 0.1 = 0.6: sy = -2.6 + 1.2*2.273 = -2.6 + 2.727 = 0.127
    E-(1) = 0.5 - 0.1 = 0.4: sy = -2.6 + 1.0*2.273 = -2.6 + 2.273 = -0.327
    Gap arrow: x=0.0, from sy(0.4) to sy(0.6) → from -0.327 to 0.127
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

_DEFAULTS = {"B03": 22.0}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)

V = 0.1  # eV, coupling strength

def _Eplus(lam):
    """Upper branch E+(λ) in eV."""
    mean = lam / 2
    half = lam / 2
    return mean + np.sqrt(half**2 + V**2)

def _Eminus(lam):
    """Lower branch E-(λ) in eV."""
    mean = lam / 2
    half = lam / 2
    return mean - np.sqrt(half**2 + V**2)


class B03_AvoidedCrossingRun(Scene):
    """Avoided crossing plot: two energy branches that never touch.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, -0.1
        x_len, y_len = 9.0, 5.0
        x_min, x_max = 0.0, 2.0
        y_min, y_max = -0.6, 1.6

        def sx(lam_val):
            return cx - x_len / 2 + (lam_val - x_min) / (x_max - x_min) * x_len

        def sy(e_val):
            return cy - y_len / 2 + (e_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.6

        # Degeneracy point coordinates
        lam_deg = 1.0
        e_plus_deg = _Eplus(lam_deg)    # = 0.6 eV
        e_minus_deg = _Eminus(lam_deg)  # = 0.4 eV
        gap_x = sx(lam_deg)             # = 0.0
        gap_top_y = sy(e_plus_deg)      # ≈ 0.127
        gap_bot_y = sy(e_minus_deg)     # ≈ -0.327

        # Header
        header = _ink_text("Two-Level Avoided Crossing", font_size=22, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes
        axes = Axes(
            x_range=[x_min, x_max, 0.5],
            y_range=[y_min, y_max, 0.5],
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": SLATE, "stroke_width": 1.5, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        axes.move_to([cx, cy, 0])
        self.play(Create(axes), run_time=0.6)

        # Axis labels
        x_lbl = _ink_text("λ  (eV)", font_size=18)
        x_lbl.move_to([sx(x_max) - 0.55, x_axis_y - 0.30, 0])
        # y-label: moved to sy(0.75) to avoid overlap with the 0.5 tick at sy(0.5)=cy
        y_lbl = _ink_text("E  (eV)", font_size=16)
        y_lbl.move_to([sx(x_min) - 0.80, sy(0.75), 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels
        for lam_val in [0.5, 1.0, 1.5]:
            lbl = _ink_text(str(lam_val), font_size=14)
            lbl.move_to([sx(lam_val), x_axis_y - 0.25, 0])
            self.add(lbl)

        for e_val in [0.0, 0.5, 1.0]:
            lbl = _ink_text(f"{e_val:.1f}", font_size=14)
            lbl.move_to([sx(x_min) - 0.50, sy(e_val), 0])
            self.add(lbl)

        # --- SLATE dashed: unperturbed lines (V=0 crossing) ---
        # E₁ = 0 (horizontal) and E₂ = λ (diagonal, slope 1)
        flat_line = DashedLine(
            start=[sx(x_min), sy(0.0), 0],
            end=[sx(x_max), sy(0.0), 0],
            color=SLATE,
            stroke_width=1.5,
            dash_length=0.15
        )
        diag_line = DashedLine(
            start=[sx(x_min), sy(x_min), 0],
            end=[sx(x_max), sy(x_max), 0],
            color=SLATE,
            stroke_width=1.5,
            dash_length=0.15
        )
        v0_lbl = _ink_text("V = 0  (cross freely)", font_size=14)
        v0_lbl.move_to([-3.0, sy(0.8), 0])
        self.play(Create(flat_line), Create(diag_line), run_time=0.5)
        self.play(FadeIn(v0_lbl), run_time=0.3)

        # --- TEAL upper branch E+(λ) ---
        curve_plus = axes.plot(
            lambda lam: _Eplus(lam),
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(curve_plus), run_time=0.6)

        # E+ label: right of curve endpoint, kept within safe area ±3.4y
        # sy(_Eplus(1.85)) = sy(1.4) ≈ -2.6 + 2.0*2.273 = -2.6 + 4.546 → clipped to y_max
        # Use sx(1.65) to position label left of tip, and sy(1.15) well within safe area
        eplus_lbl = _ink_text("E₊", font_size=18)
        eplus_lbl.move_to([sx(1.65), sy(1.15), 0])
        self.play(FadeIn(eplus_lbl), run_time=0.25)

        # --- CRIMSON lower branch E-(λ) ---
        curve_minus = axes.plot(
            lambda lam: _Eminus(lam),
            x_range=[x_min, x_max],
            color=CRIMSON,
            stroke_width=2.8
        )
        self.play(Create(curve_minus), run_time=0.6)

        # E- label: lower-right, below curve tip
        eminus_lbl = _ink_text("E₋", font_size=18)
        eminus_lbl.move_to([sx(1.85), sy(_Eminus(1.85)) - 0.35, 0])
        self.play(FadeIn(eminus_lbl), run_time=0.25)

        # --- DoubleArrow: gap at degeneracy point ---
        gap_arrow = DoubleArrow(
            start=[gap_x, gap_bot_y, 0],
            end=[gap_x, gap_top_y, 0],
            color=INK,
            stroke_width=1.5,
            tip_length=0.18
        )
        self.play(Create(gap_arrow), run_time=0.4)

        gap_lbl = _ink_text("2|V| = 0.2 eV", font_size=15)
        gap_lbl.move_to([gap_x + 1.15, (gap_top_y + gap_bot_y) / 2, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # Degeneracy marker: tick at λ=1
        deg_lbl = _ink_text("λ = 1 eV", font_size=14)
        deg_lbl.move_to([gap_x, x_axis_y - 0.50, 0])
        self.play(FadeIn(deg_lbl), run_time=0.25)

        # --- Chips ---
        plus_chip = LabelChip("E₊: upper branch (TEAL)", accent=TEAL, size=18)
        plus_chip.move_to([-3.0, -3.10, 0])
        self.play(GrowFromCenter(plus_chip), run_time=0.4)

        minus_chip = LabelChip("E₋: lower branch  gap = 2|V|", accent=CRIMSON, size=18)
        minus_chip.move_to([2.2, -3.10, 0])
        self.play(GrowFromCenter(minus_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.5 + 0.3 + 0.6 + 0.25 + 0.6 + 0.25 + 0.4 + 0.3 + 0.25 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
