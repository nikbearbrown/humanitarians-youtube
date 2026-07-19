"""vox_scenes.py — medhavy-vol3-variational-floor/short (9:16 portrait)
Reel: Helium Variational Energy E(Z*) — Every Trial Is Above the Floor
Palette: medhavy (Okabe-Ito)

Physics:
  E(Z*) = 27.2 eV × (Z*² − 3.375 Z*)  (Griffiths 7.27)
  Minimum at Z* = 27/16 = 1.6875: E_min = -77.5 eV
  True helium ground state: E₀ = -79.0 eV (NIST)
  Variational principle: E(Z*) ≥ E₀ for all Z*

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Axes center: (0, 0.1); x_range=[1,3], y_range=[-82,-60]
  x_length=3.2, y_length=4.5
  x_scale = 3.2/2 = 1.6 u/Z*; y_scale = 4.5/22 ≈ 0.2045 u/eV

  sx(z) = -1.6 + (z-1)*1.6
  sy(e) = 0.1 - 2.25 + (e+82)*(4.5/22) = -2.15 + (e+82)*0.2045

  Key points:
    Z*=1.6875: sx = -1.6 + 0.6875*1.6 = -1.6 + 1.1 = -0.50
    E_min=-77.5: sy = -2.15 + 4.5*0.2045 = -2.15 + 0.920 = -1.230
    E_floor=-79.0: sy = -2.15 + 3.0*0.2045 = -2.15 + 0.614 = -1.536

  x-axis at y = 0.1 - 2.25 = -2.15
  Chips at y=-2.85 and y=-3.30

Gate A: axes.c2p not used for arithmetic — label positions via sx/sy helpers
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

def _E(zstar):
    """Helium variational energy in eV."""
    return 27.2 * (zstar ** 2 - 3.375 * zstar)


class B03_VariationalRun(Scene):
    """Portrait E(Z*) vs Z* for helium — variational floor plot.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, 0.1
        x_len, y_len = 3.2, 4.5
        x_min, x_max = 1.0, 3.0
        y_min, y_max = -82.0, -60.0

        def sx(z_val):
            return cx - x_len / 2 + (z_val - x_min) / (x_max - x_min) * x_len

        def sy(e_val):
            return cy - y_len / 2 + (e_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.15

        # Key coordinates
        z_min_val = 1.6875
        e_min_val = _E(z_min_val)    # ≈ -77.49 eV
        e_floor = -79.0
        dot_x = sx(z_min_val)        # ≈ -0.50
        dot_y = sy(e_min_val)        # ≈ -1.23
        floor_y = sy(e_floor)        # ≈ -1.54

        # Header
        header = _ink_text("He  ⟨ψ|Ĥ|ψ⟩ ≥ E₀", font_size=18, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes — no tick numbers (portrait safe area ±1.95x)
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

        # Axis labels — placed in safe area
        # x-label: above x-axis at right end (avoids tick overlap and chips below)
        x_lbl = _ink_text("Z*", font_size=16)
        x_lbl.move_to([sx(x_max) - 0.20, x_axis_y + 0.35, 0])

        # y-label: to left of y-axis, within ±1.95x
        y_lbl = _ink_text("E (eV)", font_size=14)
        y_lbl.move_to([-1.70, cy, 0])

        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels — placed at safe positions
        # x-ticks: just 1.5 and 2.5 (avoid center clutter)
        for z_val, label in [(1.5, "1.5"), (2.5, "2.5")]:
            lbl = _ink_text(label, font_size=12)
            lbl.move_to([sx(z_val), x_axis_y - 0.22, 0])
            self.add(lbl)

        # y-ticks: sparse, to left of y-axis
        for e_val in [-80, -70]:
            lbl = _ink_text(str(e_val), font_size=12)
            lbl.move_to([-1.78, sy(e_val), 0])
            self.add(lbl)

        # --- CRIMSON dashed floor at E₀ = -79.0 eV ---
        floor_line = DashedLine(
            start=[sx(x_min), floor_y, 0],
            end=[sx(x_max), floor_y, 0],
            color=CRIMSON,
            stroke_width=2.0,
            dash_length=0.14
        )
        self.play(Create(floor_line), run_time=0.4)

        # Floor label: above the dashed line, right side
        floor_lbl = _ink_text("E₀ = −79.0 eV", font_size=13)
        floor_lbl.move_to([0.30, floor_y + 0.42, 0])
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
        dot = Dot(point=[dot_x, dot_y, 0], radius=0.11, color=TEAL,
                  fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot), run_time=0.35)

        # Minimum label: left of dot, above it
        min_lbl = _ink_text("Z*=1.69", font_size=13)
        min_lbl.move_to([dot_x - 0.62, dot_y + 0.42, 0])
        self.play(FadeIn(min_lbl), run_time=0.3)

        e_lbl = _ink_text("−77.5 eV", font_size=13)
        e_lbl.move_to([dot_x - 0.62, dot_y + 0.15, 0])
        self.play(FadeIn(e_lbl), run_time=0.25)

        # DoubleArrow: gap between minimum and floor
        gap_arrow_x = dot_x + 0.55
        gap_arrow = DoubleArrow(
            start=[gap_arrow_x, floor_y, 0],
            end=[gap_arrow_x, dot_y, 0],
            color=INK,
            stroke_width=1.5,
            tip_length=0.15
        )
        self.play(Create(gap_arrow), run_time=0.4)

        gap_lbl = _ink_text("1.5 eV\nabove", font_size=12)
        gap_lbl.move_to([gap_arrow_x + 0.60, (dot_y + floor_y) / 2, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        min_chip = LabelChip("min: −77.5 eV", accent=TEAL, size=16)
        min_chip.move_to([-0.55, -2.85, 0])
        self.play(GrowFromCenter(min_chip), run_time=0.4)

        floor_chip = LabelChip("E₀ = −79.0 eV", accent=CRIMSON, size=16)
        floor_chip.move_to([0.40, -3.28, 0])
        self.play(GrowFromCenter(floor_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.4 + 0.3 + 0.7 + 0.35 + 0.3 + 0.25 + 0.4 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
