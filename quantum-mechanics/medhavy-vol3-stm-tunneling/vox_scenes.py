"""vox_scenes.py — medhavy-vol3-stm-tunneling
Reel: STM Tunneling Current I ∝ exp(−2κd) vs gap distance d
Palette: medhavy (Okabe-Ito)

Physics:
  κ = √(2mφ)/ℏ ≈ 1.024 Å⁻¹ for φ = 4 eV (typical metal work function)
  I(d) ∝ exp(−2κd)
  ln I = −2κd → linear on semi-log plot; slope = −2κ ≈ −2.048 Å⁻¹
  +1 Å increase in d → I multiplied by exp(−2κ) = exp(−2.048) ≈ 1/7.75

Gate W: INK all Text; TEAL for curve; CRIMSON for marker dots
Gate A: Axes with numbers_to_include=[]; labels placed away from axis strokes
Gate B: All labels placed via fixed coordinates; c2p used for curve only
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]

Layout:
  Axes centered at (−0.3, −0.1); x_range=[1,10], y_range=[−14, 0]
  x_length=9.5 scene units (x spans 9 Å → x_scale = 9.5/9 ≈ 1.0556 u/Å)
  y_length=5.2 scene units (y spans 14 → y_scale = 5.2/14 ≈ 0.3714 u/ln)
  x-axis stroke at y = cy - y_length/2 = -0.1 - 2.6 = -2.7
  Chips at y = -3.05

  Manual coordinate arithmetic (c2p not used outside curve):
    scene_x(d)  = cx - x_len/2 + (d - d_min)/(d_max - d_min) * x_len
    scene_y(lnI) = cy - y_len/2 + (lnI - lnI_min)/(lnI_max - lnI_min) * y_len

    d_min=1, d_max=10, x_len=9.5, cx=-0.3
    scene_x(d) = -0.3 - 4.75 + (d-1)/9 * 9.5 = -5.05 + (d-1)*1.0556

    lnI_min=-14, lnI_max=0, y_len=5.2, cy=-0.1
    scene_y(lnI) = -0.1 - 2.6 + (lnI-(-14))/14 * 5.2 = -2.7 + (lnI+14)*0.3714

    d=4: scene_x = -5.05 + 3*1.0556 = -5.05 + 3.167 = -1.883
    d=5: scene_x = -5.05 + 4*1.0556 = -5.05 + 4.222 = -0.828
    lnI(d=4) = -2*1.024*4 = -8.192  → scene_y = -2.7 + (-8.192+14)*0.3714 = -2.7 + 2.157 = -0.543
    lnI(d=5) = -2*1.024*5 = -10.24  → scene_y = -2.7 + (-10.24+14)*0.3714 = -2.7 + 1.395 = -1.305
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


class B03_STMRun(Scene):
    """Semi-log plot of STM tunneling current I(d) = exp(−2κd).

    All label positions computed via manual arithmetic (not axes.c2p) so
    the static_scene_check stub does not encounter _Mob arithmetic.
    """

    def construct(self):
        dur = _dur("B03")

        kappa = 1.024   # Å⁻¹

        # Axis parameters
        cx, cy = -0.3, -0.1
        x_len, y_len = 9.5, 5.2
        d_min, d_max = 1, 10
        lnI_min, lnI_max = -14, 0

        # Coordinate transform helpers (pure Python floats — Gate A safe)
        def sx(d_val):
            return cx - x_len / 2 + (d_val - d_min) / (d_max - d_min) * x_len

        def sy(lnI_val):
            return cy - y_len / 2 + (lnI_val - lnI_min) / (lnI_max - lnI_min) * y_len

        # x-axis stroke at y = cy - y_len/2
        x_axis_y = cy - y_len / 2   # = -0.1 - 2.6 = -2.7

        # Axes — suppress tick numbers to prevent safe-area overflow
        axes = Axes(
            x_range=[d_min, d_max, 1],
            y_range=[lnI_min, lnI_max, 2],
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": SLATE, "stroke_width": 1.5, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        axes.move_to([cx, cy, 0])
        self.play(Create(axes), run_time=0.6)

        # --- Axis labels (fixed coordinates, clear of axis strokes) ---
        x_lbl = _ink_text("d  (Å)", font_size=18)
        x_lbl.move_to([sx(d_max) - 0.6, x_axis_y - 0.45, 0])
        y_lbl = _ink_text("ln I", font_size=18)
        y_lbl.move_to([sx(d_min) - 0.65, cy, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Manual x tick labels: d = 2, 4, 6, 8 Å (placed BELOW x-axis)
        for d_val in [2, 4, 6, 8]:
            lbl = _ink_text(str(d_val), font_size=14)
            lbl.move_to([sx(d_val), x_axis_y - 0.28, 0])
            self.add(lbl)

        # Manual y tick labels: ln I = -4, -8, -12 (placed LEFT of y-axis)
        for lnI_val in [-4, -8, -12]:
            lbl = _ink_text(str(lnI_val), font_size=14)
            lbl.move_to([sx(d_min) - 0.48, sy(lnI_val), 0])
            self.add(lbl)

        # --- TEAL tunneling curve: ln I = −2κd ---
        curve = axes.plot(
            lambda d: -2 * kappa * d,
            x_range=[d_min, d_max],
            color=TEAL,
            stroke_width=2.5
        )
        self.play(Create(curve), run_time=0.7)

        # Slope annotation — placed at fixed position near mid-curve
        # At d=3: lnI = -6.144 → scene (sx(3), sy(-6.144)) = (-3.94, -0.977)
        # Place label ABOVE and to the RIGHT of that point
        slope_lbl = _ink_text("slope = −2κ", font_size=16)
        slope_lbl.move_to([sx(5.5) + 1.0, sy(-9.0) + 1.2, 0])
        self.play(FadeIn(slope_lbl), run_time=0.3)

        kappa_lbl = _ink_text("≈ −2.05 Å⁻¹", font_size=16)
        kappa_lbl.move_to([sx(5.5) + 1.0, sy(-9.0) + 0.78, 0])
        self.play(FadeIn(kappa_lbl), run_time=0.25)

        # --- CRIMSON marker dots at d=4 and d=5 ---
        lnI_4 = -2 * kappa * 4   # = -8.192
        lnI_5 = -2 * kappa * 5   # = -10.24

        # Scene positions (pure float arithmetic)
        dot4_x, dot4_y = sx(4), sy(lnI_4)
        dot5_x, dot5_y = sx(5), sy(lnI_5)

        dot4 = Dot(point=[dot4_x, dot4_y, 0], radius=0.12, color=CRIMSON,
                   fill_opacity=1).set_stroke(width=0, opacity=0)
        dot5 = Dot(point=[dot5_x, dot5_y, 0], radius=0.12, color=CRIMSON,
                   fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot4), FadeIn(dot5), run_time=0.4)

        # DoubleArrow: between dots, placed slightly to LEFT of d=4 (clear of curve)
        arrow_x = dot4_x - 0.50   # left of d=4 dot; d=4 scene x ≈ -1.88 → arrow at -2.38
        gap_arrow = DoubleArrow(
            start=[arrow_x, dot5_y, 0],
            end=[arrow_x, dot4_y, 0],
            color=INK,
            stroke_width=1.6,
            tip_length=0.18
        )
        self.play(Create(gap_arrow), run_time=0.4)

        # Gap label: to the left of the arrow, centered vertically
        mid_y = (dot4_y + dot5_y) / 2
        gap_lbl = _ink_text("÷7.4 per Å", font_size=15)
        gap_lbl.move_to([arrow_x - 1.05, mid_y, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        slope_chip = LabelChip("slope = −2κ ≈ −2.05 Å⁻¹", accent=TEAL, size=18)
        slope_chip.move_to([-2.5, -3.05, 0])
        self.play(GrowFromCenter(slope_chip), run_time=0.4)

        factor_chip = LabelChip("×7 per Å gap", accent=CRIMSON, size=18)
        factor_chip.move_to([3.0, -3.05, 0])
        self.play(GrowFromCenter(factor_chip), run_time=0.35)

        elapsed = (0.6 + 0.3 + 0.7 + 0.3 + 0.25 + 0.4 + 0.4 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
