"""vox_scenes.py — medhavy-vol3-variational-floor
Reel: Helium Variational Energy E(Z*) — Every Trial Is Above the Floor
Palette: medhavy (Okabe-Ito)

Physics:
  E(Z*) = 27.2 eV × (Z*² − 3.375 Z*)  (Griffiths 7.27)
  Minimum at Z* = 27/16 = 1.6875: E_min = -77.5 eV
  True helium ground state: E₀ = -79.0 eV (NIST)
  Variational principle: E(Z*) ≥ E₀ for all Z*

Display:
  x_range=[1, 3] (Z*); y_range=[-82, -60] eV
  TEAL curve: E(Z*); TEAL dot at minimum
  CRIMSON dashed floor at E = -79.0 eV

Gate A: axes.c2p not used for arithmetic — label positions via sx/sy helpers
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]

Layout:
  Axes center: (0, -0.1); x_range=[1,3], y_range=[-82, -60]
  x_length=9.0, y_length=5.2
  x_scale = 9.0/2 = 4.5 u/Z*; y_scale = 5.2/22 = 0.2364 u/eV
  x-axis at y = -0.1 - 5.2/2 = -2.7; chips at y=-3.05

  sx(z) = 0 - 4.5 + (z-1)/2 * 9.0 = -4.5 + (z-1)*4.5
  sy(e) = -0.1 - 2.6 + (e-(-82))/22 * 5.2 = -2.7 + (e+82)*0.2364

  Key points:
    Z*=1.6875: sx = -4.5 + 0.6875*4.5 = -4.5 + 3.094 = -1.406
    E_min=-77.5: sy = -2.7 + 4.5*0.2364 = -2.7 + 1.064 = -1.636
    E_floor=-79.0: sy = -2.7 + 3.0*0.2364 = -2.7 + 0.709 = -1.991
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

def _E(zstar):
    """Helium variational energy in eV."""
    return 27.2 * (zstar ** 2 - 3.375 * zstar)


class B03_VariationalRun(Scene):
    """E(Z*) vs Z* for helium — variational floor plot.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, -0.1
        x_len, y_len = 9.0, 5.2
        x_min, x_max = 1.0, 3.0
        y_min, y_max = -82.0, -60.0

        def sx(z_val):
            return cx - x_len / 2 + (z_val - x_min) / (x_max - x_min) * x_len

        def sy(e_val):
            return cy - y_len / 2 + (e_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.7

        # Key coordinates
        z_min_val = 1.6875
        e_min_val = _E(z_min_val)    # ≈ -77.49 eV
        e_floor = -79.0
        dot_x = sx(z_min_val)        # ≈ -1.406
        dot_y = sy(e_min_val)        # ≈ -1.636
        floor_y = sy(e_floor)        # ≈ -1.991

        # Header
        header = _ink_text("Helium  ⟨ψ|Ĥ|ψ⟩ ≥ E₀", font_size=22, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes
        axes = Axes(
            x_range=[x_min, x_max, 0.5],
            y_range=[y_min, y_max, 5],
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
        # x-label: placed at right side only (not centered) — avoids overlap with "2.0" tick at center
        x_lbl = _ink_text("Z*", font_size=18)
        x_lbl.move_to([sx(x_max) - 0.35, x_axis_y - 0.30, 0])
        y_lbl = _ink_text("E  (eV)", font_size=16)
        y_lbl.move_to([sx(x_min) - 0.80, cy, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels — placed close to x-axis
        for z_val in [1.5, 2.0, 2.5]:
            lbl = _ink_text(str(z_val), font_size=14)
            lbl.move_to([sx(z_val), x_axis_y - 0.25, 0])
            self.add(lbl)

        for e_val in [-80, -75, -70, -65]:
            lbl = _ink_text(str(e_val), font_size=14)
            lbl.move_to([sx(x_min) - 0.50, sy(e_val), 0])
            self.add(lbl)

        # --- CRIMSON dashed floor at E₀ = -79.0 eV ---
        floor_line = DashedLine(
            start=[sx(x_min), floor_y, 0],
            end=[sx(x_max), floor_y, 0],
            color=CRIMSON,
            stroke_width=2.0,
            dash_length=0.18
        )
        self.play(Create(floor_line), run_time=0.4)

        # Floor label: centered on the right part of the plot, above the dashed line
        # Placed well above the dashed line (+0.55) to avoid overlap with the line stroke
        floor_lbl = _ink_text("E₀ = −79.0 eV  (NIST)", font_size=15)
        floor_lbl.move_to([sx(2.2), floor_y + 0.55, 0])
        self.play(FadeIn(floor_lbl), run_time=0.3)

        # --- TEAL variational curve ---
        curve = axes.plot(
            lambda z: _E(z),
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(curve), run_time=0.7)

        # --- TEAL dot at minimum ---
        dot = Dot(point=[dot_x, dot_y, 0], radius=0.13, color=TEAL,
                  fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot), run_time=0.35)

        # Minimum label: above and to the left of the dot
        min_lbl = _ink_text("min: Z*=1.69", font_size=16)
        min_lbl.move_to([dot_x - 1.8, dot_y + 0.55, 0])
        self.play(FadeIn(min_lbl), run_time=0.3)

        e_lbl = _ink_text("E = −77.5 eV", font_size=15)
        e_lbl.move_to([dot_x - 1.8, dot_y + 0.18, 0])
        self.play(FadeIn(e_lbl), run_time=0.25)

        # DoubleArrow between minimum and floor (to show gap)
        gap_arrow_x = dot_x + 0.70
        gap_arrow = DoubleArrow(
            start=[gap_arrow_x, floor_y, 0],
            end=[gap_arrow_x, dot_y, 0],
            color=INK,
            stroke_width=1.5,
            tip_length=0.18
        )
        self.play(Create(gap_arrow), run_time=0.4)

        gap_lbl = _ink_text("1.5 eV\nabove floor", font_size=14)
        gap_lbl.move_to([gap_arrow_x + 0.9, (dot_y + floor_y) / 2, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        # Ticks at x=-2.25, 0, +2.25; chips placed BELOW tick level (y=-3.20 vs ticks at -2.95)
        # Tick "1.5" at x=-2.25 may still overlap chip if chip extends left enough.
        # Use shorter text and place chips at y=-3.20 (below ticks at y=-2.95)
        min_chip = LabelChip("min: −77.5 eV", accent=TEAL, size=18)
        min_chip.move_to([-3.0, -3.20, 0])
        self.play(GrowFromCenter(min_chip), run_time=0.4)

        floor_chip = LabelChip("E₀ = −79.0 eV (NIST)", accent=CRIMSON, size=18)
        floor_chip.move_to([2.5, -3.20, 0])
        self.play(GrowFromCenter(floor_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.4 + 0.3 + 0.7 + 0.35 + 0.3 + 0.25 + 0.4 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
