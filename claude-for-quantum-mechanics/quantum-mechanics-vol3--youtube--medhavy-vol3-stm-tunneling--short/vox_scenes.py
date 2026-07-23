"""vox_scenes.py — medhavy-vol3-stm-tunneling/short (9:16 portrait)
Safe area: ±1.95x / ±3.4y

Physics: κ ≈ 1.024 Å⁻¹ (φ=4 eV); ln I = −2κd; slope = −2.048 Å⁻¹

Layout:
  Portrait width: ±1.95x → usable x span ≈ 3.9 scene units
  Axes centered at (0, 0); x_range=[1,10], y_range=[-14, 0]
  x_length=3.2, y_length=4.5
  x_scale = 3.2/9 = 0.356 u/Å; y_scale = 4.5/14 = 0.321 u/ln

  x-axis stroke at y = 0 - 4.5/2 = -2.25
  Chips at y = -2.75 and y = -3.2

  Coordinate helpers (pure float, Gate A safe):
    sx(d)    = 0 - 3.2/2 + (d-1)/9 * 3.2 = -1.6 + (d-1)*0.356
    sy(lnI)  = 0 - 4.5/2 + (lnI-(-14))/14 * 4.5 = -2.25 + (lnI+14)*0.321

    d=4: sx = -1.6 + 3*0.356 = -1.6 + 1.067 = -0.533
    d=5: sx = -1.6 + 4*0.356 = -1.6 + 1.422 = -0.178
    lnI(4) = -8.192 → sy = -2.25 + 5.808*0.321 = -2.25 + 1.865 = -0.385
    lnI(5) = -10.24 → sy = -2.25 + 3.76*0.321  = -2.25 + 1.207 = -1.043

  Labels:
    x-axis label at [sx(10)-0.3, -2.25-0.35, 0] = [1.3, -2.6, 0]
    y-axis label at [sx(1)-0.38, 0, 0] = [-1.98, 0, 0] — use fixed -1.85
    Tick labels: d=3,6,9 below x-axis; lnI=-5,-10 left of y-axis
    Slope label at fixed position above curve
    Gap arrow at arrow_x = sx(4) - 0.25 = -0.78; gap label at arrow_x - 0.55
    Chips at y=-2.75 (left) and y=-3.2 (right)

  Note: all label x-positions must stay within ±1.95
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

_DEFAULTS = {"B03": 35.0}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


class B03_STMRun(Scene):
    """Portrait semi-log plot: I ∝ exp(−2κd) vs d."""

    def construct(self):
        dur = _dur("B03")

        kappa = 1.024  # Å⁻¹

        # Axis parameters (pure floats for Gate A)
        cx, cy = 0.0, 0.0
        x_len, y_len = 3.2, 4.5
        d_min, d_max = 1, 10
        lnI_min, lnI_max = -14, 0

        def sx(d_val):
            return cx - x_len / 2 + (d_val - d_min) / (d_max - d_min) * x_len

        def sy(lnI_val):
            return cy - y_len / 2 + (lnI_val - lnI_min) / (lnI_max - lnI_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.25

        # --- Header ---
        header = _ink_text("STM Tunneling  I ∝ e^(−2κd)", font_size=14, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # --- Axes ---
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
        self.play(Create(axes), run_time=0.5)

        # Axis labels (fixed positions within ±1.95x)
        x_lbl = _ink_text("d (Å)", font_size=13)
        x_lbl.move_to([sx(d_max) - 0.2, x_axis_y - 0.30, 0])
        y_lbl = _ink_text("ln I", font_size=13)
        y_lbl.move_to([-1.85, cy, 0])   # fixed x, within ±1.95
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.25)

        # Tick labels
        for d_val in [3, 6, 9]:
            lbl = _ink_text(str(d_val), font_size=11)
            lbl.move_to([sx(d_val), x_axis_y - 0.22, 0])
            self.add(lbl)

        for lnI_val in [-5, -10]:
            lbl = _ink_text(str(lnI_val), font_size=11)
            lbl.move_to([-1.78, sy(lnI_val), 0])   # within ±1.95
            self.add(lbl)

        # --- TEAL tunneling curve ---
        curve = axes.plot(
            lambda d: -2 * kappa * d,
            x_range=[d_min, d_max],
            color=TEAL,
            stroke_width=2.5
        )
        self.play(Create(curve), run_time=0.7)

        # Slope annotation: fixed position, right of curve, above mid
        # At d=6: lnI = -12.29 → sy ≈ -2.25 + 1.71*0.321 = -1.7; sx(6) = -1.6+5*0.356 = 0.18
        # Place label at right side, above the curve at that point
        slope_lbl = _ink_text("slope=−2κ", font_size=12)
        slope_lbl.move_to([1.30, sy(-7.0) + 0.5, 0])
        self.play(FadeIn(slope_lbl), run_time=0.3)

        kappa_lbl = _ink_text("≈−2.05 Å⁻¹", font_size=12)
        kappa_lbl.move_to([1.30, sy(-7.0) + 0.18, 0])
        self.play(FadeIn(kappa_lbl), run_time=0.25)

        # --- CRIMSON marker dots at d=4 and d=5 ---
        lnI_4 = -2 * kappa * 4   # -8.192
        lnI_5 = -2 * kappa * 5   # -10.24

        dot4_x, dot4_y = sx(4), sy(lnI_4)
        dot5_x, dot5_y = sx(5), sy(lnI_5)

        dot4 = Dot(point=[dot4_x, dot4_y, 0], radius=0.10, color=CRIMSON,
                   fill_opacity=1).set_stroke(width=0, opacity=0)
        dot5 = Dot(point=[dot5_x, dot5_y, 0], radius=0.10, color=CRIMSON,
                   fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot4), FadeIn(dot5), run_time=0.35)

        # DoubleArrow left of d=4 dot (clear of curve stroke)
        arrow_x = dot4_x - 0.28
        gap_arrow = DoubleArrow(
            start=[arrow_x, dot5_y, 0],
            end=[arrow_x, dot4_y, 0],
            color=INK,
            stroke_width=1.4,
            tip_length=0.14
        )
        self.play(Create(gap_arrow), run_time=0.35)

        # Gap label to the left (but within ±1.95)
        mid_y = (dot4_y + dot5_y) / 2
        gap_lbl = _ink_text("÷7 per Å", font_size=12)
        gap_lbl.move_to([arrow_x - 0.65, mid_y, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        slope_chip = LabelChip("slope = −2κ", accent=TEAL, size=15)
        slope_chip.move_to([0, -2.75, 0])
        self.play(GrowFromCenter(slope_chip), run_time=0.4)

        factor_chip = LabelChip("×7 per Å gap", accent=CRIMSON, size=15)
        factor_chip.move_to([0, -3.2, 0])
        self.play(GrowFromCenter(factor_chip), run_time=0.35)

        elapsed = (0.4 + 0.5 + 0.25 + 0.7 + 0.3 + 0.25 + 0.35 + 0.35 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
