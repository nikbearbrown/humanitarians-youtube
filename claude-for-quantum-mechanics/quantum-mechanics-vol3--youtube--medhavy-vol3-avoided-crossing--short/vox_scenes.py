"""vox_scenes.py — medhavy-vol3-avoided-crossing/short (9:16 portrait)
Reel: Two-Level Avoided Crossing — Energy Levels That Never Touch
Palette: medhavy (Okabe-Ito)

Physics:
  Two-level Hamiltonian: E₁=0, E₂=λ, coupling V=0.1 eV
  E±(λ) = λ/2 ± √((λ/2)² + V²)
  At λ=1: gap = 2V = 0.2 eV
  Unperturbed (V=0): E₁=0 flat, E₂=λ diagonal — cross at λ=1

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Axes center: (0, 0.1); x_range=[0,2], y_range=[-0.6,1.6]
  x_length=3.2, y_length=4.5
  x_scale = 3.2/2 = 1.6 u/eV; y_scale = 4.5/2.2 ≈ 2.045 u/eV

  sx(lam) = -1.6 + lam * 1.6
  sy(e)   = 0.1 - 2.25 + (e+0.6)/2.2 * 4.5 = -2.15 + (e+0.6)*2.045

  Key points:
    λ=1: sx = 0.0
    E+(1) = 0.6: sy = -2.15 + 1.2*2.045 = -2.15 + 2.454 = 0.304
    E-(1) = 0.4: sy = -2.15 + 1.0*2.045 = -2.15 + 2.045 = -0.105
    Gap arrow: x=0.0, from -0.105 to 0.304

  x-axis at y = 0.1 - 2.25 = -2.15
  Chips at y=-2.85 and y=-3.28

Gate A: axes.c2p not used — sx/sy helpers only
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4]
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

V = 0.1  # eV

def _Eplus(lam):
    mean = lam / 2
    half = lam / 2
    return mean + np.sqrt(half**2 + V**2)

def _Eminus(lam):
    mean = lam / 2
    half = lam / 2
    return mean - np.sqrt(half**2 + V**2)


class B03_AvoidedCrossingRun(Scene):
    """Portrait avoided crossing plot.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, 0.1
        x_len, y_len = 3.2, 4.5
        x_min, x_max = 0.0, 2.0
        y_min, y_max = -0.6, 1.6

        def sx(lam_val):
            return cx - x_len / 2 + (lam_val - x_min) / (x_max - x_min) * x_len

        def sy(e_val):
            return cy - y_len / 2 + (e_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.15

        # Degeneracy coordinates
        lam_deg = 1.0
        e_plus_deg = _Eplus(lam_deg)    # 0.6 eV
        e_minus_deg = _Eminus(lam_deg)  # 0.4 eV
        gap_x = sx(lam_deg)             # 0.0
        gap_top_y = sy(e_plus_deg)      # ≈ 0.304
        gap_bot_y = sy(e_minus_deg)     # ≈ -0.105

        # Header
        header = _ink_text("Avoided Crossing", font_size=18, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes — no tick numbers (portrait safe area ±1.95x)
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

        # Axis labels — within ±1.95x
        # x-label: above x-axis at right end
        x_lbl = _ink_text("λ (eV)", font_size=14)
        x_lbl.move_to([sx(x_max) - 0.30, x_axis_y + 0.35, 0])
        # y-label: left of axis, short string
        y_lbl = _ink_text("E", font_size=16)
        y_lbl.move_to([-1.72, cy + 0.5, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels — sparse for portrait
        for lam_val, label in [(1.0, "1")]:
            lbl = _ink_text(label, font_size=12)
            lbl.move_to([sx(lam_val), x_axis_y - 0.22, 0])
            self.add(lbl)

        for e_val in [0.0, 1.0]:
            lbl = _ink_text(f"{e_val:.0f}", font_size=12)
            lbl.move_to([-1.75, sy(e_val), 0])
            self.add(lbl)

        # --- SLATE dashed: unperturbed (V=0) crossing lines ---
        flat_line = DashedLine(
            start=[sx(x_min), sy(0.0), 0],
            end=[sx(x_max), sy(0.0), 0],
            color=SLATE, stroke_width=1.5, dash_length=0.12
        )
        diag_line = DashedLine(
            start=[sx(x_min), sy(x_min), 0],
            end=[sx(x_max), sy(x_max), 0],
            color=SLATE, stroke_width=1.5, dash_length=0.12
        )
        v0_lbl = _ink_text("V=0: cross", font_size=12)
        v0_lbl.move_to([-0.90, sy(0.85), 0])
        self.play(Create(flat_line), Create(diag_line), run_time=0.5)
        self.play(FadeIn(v0_lbl), run_time=0.3)

        # --- TEAL upper branch ---
        curve_plus = axes.plot(
            lambda lam: _Eplus(lam),
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(curve_plus), run_time=0.6)

        # E+ label: right side, offset above curve so it stays in safe area
        eplus_lbl = _ink_text("E₊", font_size=15)
        eplus_lbl.move_to([sx(1.65), sy(1.1), 0])
        self.play(FadeIn(eplus_lbl), run_time=0.25)

        # --- CRIMSON lower branch ---
        curve_minus = axes.plot(
            lambda lam: _Eminus(lam),
            x_range=[x_min, x_max],
            color=CRIMSON,
            stroke_width=2.8
        )
        self.play(Create(curve_minus), run_time=0.6)

        eminus_lbl = _ink_text("E₋", font_size=15)
        eminus_lbl.move_to([sx(1.65), sy(-0.35), 0])
        self.play(FadeIn(eminus_lbl), run_time=0.25)

        # --- DoubleArrow: gap at degeneracy ---
        gap_arrow = DoubleArrow(
            start=[gap_x, gap_bot_y, 0],
            end=[gap_x, gap_top_y, 0],
            color=INK,
            stroke_width=1.5,
            tip_length=0.13
        )
        self.play(Create(gap_arrow), run_time=0.4)

        gap_lbl = _ink_text("2|V|=0.2 eV", font_size=12)
        gap_lbl.move_to([gap_x + 0.75, (gap_top_y + gap_bot_y) / 2, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        plus_chip = LabelChip("E₊ upper", accent=TEAL, size=16)
        plus_chip.move_to([-0.70, -2.85, 0])
        self.play(GrowFromCenter(plus_chip), run_time=0.4)

        minus_chip = LabelChip("gap = 2|V|", accent=CRIMSON, size=16)
        minus_chip.move_to([0.55, -3.28, 0])
        self.play(GrowFromCenter(minus_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.5 + 0.3 + 0.6 + 0.25 + 0.6 + 0.25 + 0.4 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
