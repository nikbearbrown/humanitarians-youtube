"""vox_scenes.py — medhavy-vol2-orbital-energies
Reel: Orbital Energy Diagram — Hydrogen (degenerate) vs Sodium (l-split)
Palette: medhavy (Okabe-Ito)

Physics:
  H n=3: E(3s) = E(3p) = E(3d) = -13.6/9 = -1.511 eV  [Coulomb degeneracy]
  Na n=3: E(3s) = -5.1 eV, E(3p) = -3.0 eV, gap = 2.1 eV  [screening splits]

Gate W: INK all Text; TEAL for H lines; CRIMSON for Na lines
Gate A: Distinct line mobjects; labels placed to right of line ends (not on strokes)
Gate B: labels placed ABOVE each line (not at line y-level) to avoid overlap
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]

Layout (scene units):
  y_range: [-6, 0] eV, y_length=5.5 → scale = 5.5/6 ≈ 0.917 units/eV
  y_origin_scene: 2.5 (top of axis at 0 eV, bottom at -6 eV)
  Left column (H): x center at -2.8
  Right column (Na): x center at +2.8
  Line half-width: 1.0 scene units
  Labels: placed to RIGHT of each line (x = col_x + 1.15), vertically at line level
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

_DEFAULTS = {"B03": 25.0}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


class B03_OrbitalRun(Scene):
    """Two-column orbital energy level diagram: H (TEAL, degenerate) vs Na (CRIMSON, split).

    Layout:
      y_scale: 5.5 units / 6 eV = 0.9167 units/eV
      y_scene(E_eV) = y_top - (|E_eV| * y_scale)   where y_top = 2.3
        E = -1.511 eV → y = 2.3 - 1.511*0.9167 = 2.3 - 1.385 = 0.915
        E = -3.0 eV   → y = 2.3 - 3.0*0.9167   = 2.3 - 2.750 = -0.450
        E = -5.1 eV   → y = 2.3 - 5.1*0.9167   = 2.3 - 4.675 = -2.375

      Left column H: x ∈ [-3.7, -1.7],  labels at x = -1.55 (right side)
      Right column Na: x ∈ [1.7, 3.7],  labels at x = 3.85 (right side)
      Arrow (double-headed) in Na column between 3s and 3p: x = 1.55
      Column headers at y = 2.7
      Chips at y = -2.85 (below line at -2.375)
      y-axis: left edge at x = -4.5, tick marks at -1.5, -3.0, -5.0 eV
      y-axis label at x = -5.7
    """

    def construct(self):
        dur = _dur("B03")

        # --- Scale parameters ---
        y_top = 2.3         # scene y for 0 eV
        y_scale = 0.9167    # scene units per eV (5.5 / 6)

        def ev_to_y(e_ev):
            """Convert energy in eV (negative values) to scene y."""
            return y_top + e_ev * y_scale  # e_ev is negative, so this subtracts

        # Energy values (eV)
        E_H = -1.511      # H n=3 (all three subshells)
        E_Na_3s = -5.1
        E_Na_3p = -3.0

        # Scene y positions
        y_H = ev_to_y(E_H)           # ≈  0.916
        y_Na_3s = ev_to_y(E_Na_3s)   # ≈ -2.375
        y_Na_3p = ev_to_y(E_Na_3p)   # ≈ -0.450

        # Column x ranges
        H_x1, H_x2 = -3.7, -1.7      # H line: left to right
        Na_x1, Na_x2 = 1.7, 3.7      # Na line: left to right

        # Label x positions (to the right of each line, no overlap with stroke)
        H_lbl_x = -1.52
        Na_lbl_x = 3.87

        # --- Header ---
        header = _ink_text("Orbital Energies  n = 3", font_size=22, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # --- y-axis line (for reference scale) ---
        y_axis_x = -5.1
        y_bottom_scene = ev_to_y(-6.0)  # = 2.3 - 5.5 = -3.2  (safe: ≥ -3.4)
        y_axis = Line(start=[y_axis_x, y_bottom_scene, 0], end=[y_axis_x, y_top, 0],
                      color=SLATE, stroke_width=1.2)
        self.play(Create(y_axis), run_time=0.3)

        # y-axis tick marks and labels: at -1.5, -3.0, -5.0 eV
        tick_len = 0.18
        for e_tick, lbl_str in [(-1.5, "-1.5"), (-3.0, "-3.0"), (-5.0, "-5.0")]:
            y_t = ev_to_y(e_tick)
            tick = Line(start=[y_axis_x, y_t, 0], end=[y_axis_x + tick_len, y_t, 0],
                        color=SLATE, stroke_width=1.0)
            tick_lbl = _ink_text(lbl_str, font_size=13)
            # Label to LEFT of tick, clear of y-axis stroke
            tick_lbl.move_to([y_axis_x - 0.55, y_t, 0])
            self.add(tick, tick_lbl)

        # y-axis unit label
        y_unit_lbl = _ink_text("eV", font_size=14)
        y_unit_lbl.move_to([y_axis_x - 0.55, y_top + 0.25, 0])
        self.play(FadeIn(y_unit_lbl), run_time=0.2)

        # --- Column headers ---
        h_col_hdr = _ink_text("Hydrogen", font_size=19, font=DISPLAY)
        h_col_hdr.move_to([-2.7, 2.72, 0])
        na_col_hdr = _ink_text("Sodium", font_size=19, font=DISPLAY)
        na_col_hdr.move_to([2.7, 2.72, 0])
        self.play(FadeIn(h_col_hdr), FadeIn(na_col_hdr), run_time=0.3)

        # --- HYDROGEN column: THREE degenerate lines, all at y_H ---
        # All three at same height — Coulomb degeneracy
        h_lines = []
        for _ in range(3):
            ln = Line(start=[H_x1, y_H, 0], end=[H_x2, y_H, 0],
                      color=TEAL, stroke_width=3.0)
            h_lines.append(ln)

        # Draw as a group (they stack; visually appear as one thick teal line at y_H)
        self.play(*[Create(ln) for ln in h_lines], run_time=0.5)

        # Labels for H lines: placed to RIGHT of right endpoint, stacked vertically
        # Must NOT be at y_H (on the line); offset vertically by ±0.24 and center
        h_3s_lbl = _ink_text("3s", font_size=15)
        h_3s_lbl.move_to([H_lbl_x + 0.18, y_H + 0.30, 0])
        h_3p_lbl = _ink_text("3p", font_size=15)
        h_3p_lbl.move_to([H_lbl_x + 0.18, y_H, 0])
        h_3d_lbl = _ink_text("3d", font_size=15)
        h_3d_lbl.move_to([H_lbl_x + 0.18, y_H - 0.30, 0])
        self.play(FadeIn(h_3s_lbl), FadeIn(h_3p_lbl), FadeIn(h_3d_lbl), run_time=0.35)

        # Energy label for H (to left of column)
        h_e_lbl = _ink_text("-1.51 eV", font_size=14)
        h_e_lbl.move_to([-4.25, y_H, 0])
        self.play(FadeIn(h_e_lbl), run_time=0.25)

        # --- SODIUM column: 3s and 3p at different heights ---
        # Na 3p (higher, less bound)
        na_3p_line = Line(start=[Na_x1, y_Na_3p, 0], end=[Na_x2, y_Na_3p, 0],
                          color=CRIMSON, stroke_width=3.0)
        # Na 3s (lower, more bound)
        na_3s_line = Line(start=[Na_x1, y_Na_3s, 0], end=[Na_x2, y_Na_3s, 0],
                          color=CRIMSON, stroke_width=3.0)

        self.play(Create(na_3p_line), run_time=0.4)
        self.play(Create(na_3s_line), run_time=0.4)

        # Labels: to the RIGHT of each Na line, offset above the line stroke
        na_3p_lbl = _ink_text("3p", font_size=15)
        na_3p_lbl.move_to([Na_lbl_x + 0.15, y_Na_3p + 0.28, 0])
        na_3s_lbl = _ink_text("3s", font_size=15)
        na_3s_lbl.move_to([Na_lbl_x + 0.15, y_Na_3s + 0.28, 0])
        self.play(FadeIn(na_3p_lbl), FadeIn(na_3s_lbl), run_time=0.3)

        # Energy labels for Na lines (to left of Na column)
        na_3p_e_lbl = _ink_text("-3.0 eV", font_size=14)
        na_3p_e_lbl.move_to([0.95, y_Na_3p, 0])
        na_3s_e_lbl = _ink_text("-5.1 eV", font_size=14)
        na_3s_e_lbl.move_to([0.95, y_Na_3s, 0])
        self.play(FadeIn(na_3p_e_lbl), FadeIn(na_3s_e_lbl), run_time=0.3)

        # --- Gap arrow: double-headed arrow between Na 3s and Na 3p ---
        # Arrow x at left side of Na column
        gap_x = 1.40
        gap_arrow = DoubleArrow(
            start=[gap_x, y_Na_3s, 0],
            end=[gap_x, y_Na_3p, 0],
            color=INK,
            stroke_width=1.6,
            tip_length=0.18
        )
        self.play(Create(gap_arrow), run_time=0.4)

        # Gap label: to the left of the gap arrow, centered between 3s and 3p
        gap_mid_y = (y_Na_3s + y_Na_3p) / 2   # = (-2.375 + -0.450) / 2 = -1.4125
        gap_lbl = _ink_text("Δ = 2.1 eV", font_size=14)
        gap_lbl.move_to([gap_x - 0.90, gap_mid_y, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        # x-axis of H column: at y_Na_3s ≈ -2.375 (bottom line); chips below at y=-2.85
        h_chip = LabelChip("H: 3s=3p=3d", accent=TEAL, size=19)
        h_chip.move_to([-2.5, -2.85, 0])
        self.play(GrowFromCenter(h_chip), run_time=0.4)

        na_chip = LabelChip("Na: E(3s)<E(3p)", accent=CRIMSON, size=19)
        na_chip.move_to([2.6, -2.85, 0])
        self.play(GrowFromCenter(na_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.2 + 0.3 + 0.5 + 0.35 + 0.25 +
                   0.4 + 0.4 + 0.3 + 0.3 + 0.4 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
