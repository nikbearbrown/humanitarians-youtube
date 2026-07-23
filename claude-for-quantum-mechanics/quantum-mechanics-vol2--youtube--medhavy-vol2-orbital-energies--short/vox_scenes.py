"""vox_scenes.py — medhavy-vol2-orbital-energies/short (9:16 portrait)
Safe area: ±1.95x / ±3.4y

Layout: two-column energy level diagram
  Portrait width is ±1.95x scene units.
  H column: x ∈ [-1.75, -0.15]   center at -0.95
  Na column: x ∈ [0.15, 1.75]    center at  0.95
  Line half-width: 0.80 scene units
  Column headers at y = 3.0
  Header at y = 3.3

  y_scale: 4.5 units / 6 eV = 0.75 units/eV
  y_top = 2.5 (= 0 eV)
  y_bottom = 2.5 - 6*0.75 = 2.5 - 4.5 = -2.0  (safely above -3.4)

  y_scene(E_eV) = y_top + E_eV * y_scale   (E_eV < 0 → y decreases)
    E_H = -1.511 eV  → y = 2.5 - 1.133 = 1.367
    E_Na_3p = -3.0 eV → y = 2.5 - 2.25  = 0.25
    E_Na_3s = -5.1 eV → y = 2.5 - 3.825 = -1.325

  Labels: placed ABOVE each line (+0.28 y offset) to avoid overlapping strokes
  Na column gap arrow: at x = -0.02 (between the two columns)
  Gap label: at x = -0.02 - 0.55 = -0.57, mid y
  Chips at y = -2.15 (H chip left, Na chip right)
  eV tick labels placed to left side at x = -1.9 (within ±1.95)
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

_DEFAULTS = {"B03": 25.0}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


class B03_OrbitalRun(Scene):
    """Portrait two-column orbital energy level diagram.

    H (TEAL): 3s, 3p, 3d all degenerate at -1.511 eV
    Na (CRIMSON): 3s at -5.1 eV, 3p at -3.0 eV, gap = 2.1 eV
    """

    def construct(self):
        dur = _dur("B03")

        # --- Scale parameters ---
        y_top = 2.5          # scene y for 0 eV
        y_scale = 0.75       # scene units per eV  (4.5 / 6)

        def ev_to_y(e_ev):
            return y_top + e_ev * y_scale  # e_ev < 0 → subtract

        # Energy values
        E_H = -1.511
        E_Na_3s = -5.1
        E_Na_3p = -3.0

        y_H = ev_to_y(E_H)           # ≈  1.367
        y_Na_3s = ev_to_y(E_Na_3s)   # ≈ -1.325
        y_Na_3p = ev_to_y(E_Na_3p)   # ≈  0.250

        # Column x extents
        # H column starts AFTER y-axis at x = -1.60 (with 0.05 gap)
        H_x1, H_x2 = -1.55, -0.15
        Na_x1, Na_x2 = 0.15, 1.75

        # --- Header ---
        header = _ink_text("Orbital Energies  n=3", font_size=15, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # --- Column headers ---
        # H center = (-1.55 + -0.15)/2 = -0.85; Na center = (0.15 + 1.75)/2 = 0.95
        h_hdr = _ink_text("Hydrogen", font_size=13, font=DISPLAY)
        h_hdr.move_to([-0.85, 3.0, 0])
        na_hdr = _ink_text("Sodium", font_size=13, font=DISPLAY)
        na_hdr.move_to([0.95, 3.0, 0])
        self.play(FadeIn(h_hdr), FadeIn(na_hdr), run_time=0.3)

        # --- y-axis reference line ---
        # y_axis_x = -1.60: tick labels at -1.60 - 0.28 = -1.88 → within ±1.95
        y_bottom_scene = ev_to_y(-6.0)   # = 2.5 - 4.5 = -2.0
        y_axis_x = -1.60
        y_axis = Line(start=[y_axis_x, y_bottom_scene, 0], end=[y_axis_x, y_top, 0],
                      color=SLATE, stroke_width=1.0)
        self.play(Create(y_axis), run_time=0.25)

        # eV tick marks and labels at -1.5, -3.0, -5.0 eV
        # Tick labels to the LEFT of y_axis at x = y_axis_x - 0.18 (center)
        # y_axis_x = -1.60; label center at -1.78; font_size=10 → width≈0.20 → left edge≈-1.88 (within ±1.95)
        tick_len = 0.10
        for e_tick, lbl_str in [(-1.5, "-1.5"), (-3.0, "-3.0"), (-5.0, "-5.0")]:
            y_t = ev_to_y(e_tick)
            tick = Line(start=[y_axis_x - tick_len, y_t, 0], end=[y_axis_x, y_t, 0],
                        color=SLATE, stroke_width=0.8)
            t_lbl = _ink_text(lbl_str, font_size=10)
            t_lbl.move_to([y_axis_x - 0.28, y_t, 0])
            self.add(tick, t_lbl)

        # eV unit label above y-axis, also to left
        unit_lbl = _ink_text("eV", font_size=11)
        unit_lbl.move_to([y_axis_x - 0.22, y_top + 0.20, 0])
        self.play(FadeIn(unit_lbl), run_time=0.2)

        # --- HYDROGEN: three degenerate lines at y_H ---
        h_lines = [
            Line(start=[H_x1, y_H, 0], end=[H_x2, y_H, 0],
                 color=TEAL, stroke_width=2.5)
            for _ in range(3)
        ]
        self.play(*[Create(ln) for ln in h_lines], run_time=0.5)

        # Labels ABOVE line strokes (offset +0.28 to clear stroke)
        h_3s_lbl = _ink_text("3s", font_size=13)
        h_3s_lbl.move_to([-1.4, y_H + 0.28, 0])
        h_3p_lbl = _ink_text("3p", font_size=13)
        h_3p_lbl.move_to([-0.95, y_H + 0.28, 0])
        h_3d_lbl = _ink_text("3d", font_size=13)
        h_3d_lbl.move_to([-0.5, y_H + 0.28, 0])
        self.play(FadeIn(h_3s_lbl), FadeIn(h_3p_lbl), FadeIn(h_3d_lbl), run_time=0.3)

        # H energy value label: ABOVE the labels, placed at left
        h_e_lbl = _ink_text("-1.51 eV", font_size=11)
        h_e_lbl.move_to([-0.95, y_H + 0.55, 0])
        self.play(FadeIn(h_e_lbl), run_time=0.25)

        # --- SODIUM: 3p (higher) and 3s (lower) ---
        na_3p_line = Line(start=[Na_x1, y_Na_3p, 0], end=[Na_x2, y_Na_3p, 0],
                          color=CRIMSON, stroke_width=2.5)
        na_3s_line = Line(start=[Na_x1, y_Na_3s, 0], end=[Na_x2, y_Na_3s, 0],
                          color=CRIMSON, stroke_width=2.5)
        self.play(Create(na_3p_line), run_time=0.4)
        self.play(Create(na_3s_line), run_time=0.4)

        # Labels ABOVE each Na line stroke
        na_3p_lbl = _ink_text("3p", font_size=13)
        na_3p_lbl.move_to([0.95, y_Na_3p + 0.28, 0])
        na_3s_lbl = _ink_text("3s", font_size=13)
        na_3s_lbl.move_to([0.95, y_Na_3s + 0.28, 0])
        self.play(FadeIn(na_3p_lbl), FadeIn(na_3s_lbl), run_time=0.3)

        # Na energy values: placed ABOVE each label (further up)
        na_3p_e_lbl = _ink_text("-3.0 eV", font_size=11)
        na_3p_e_lbl.move_to([0.95, y_Na_3p + 0.55, 0])
        na_3s_e_lbl = _ink_text("-5.1 eV", font_size=11)
        na_3s_e_lbl.move_to([0.95, y_Na_3s + 0.55, 0])
        self.play(FadeIn(na_3p_e_lbl), FadeIn(na_3s_e_lbl), run_time=0.3)

        # --- Gap double-headed arrow between Na 3s and 3p ---
        # Place between columns, clear of both line strokes
        # x = 0.02 is in the gap between H (ends at -0.15) and Na (starts at 0.15)
        # But that's very narrow; use x = 0.13 (just at left edge of Na column, no H line there)
        gap_x = 0.10
        gap_arrow = DoubleArrow(
            start=[gap_x, y_Na_3s, 0],
            end=[gap_x, y_Na_3p, 0],
            color=INK,
            stroke_width=1.4,
            tip_length=0.14
        )
        self.play(Create(gap_arrow), run_time=0.4)

        # Gap label: to the left of the arrow, centered vertically
        gap_mid_y = (y_Na_3s + y_Na_3p) / 2   # ≈ (-1.325 + 0.250) / 2 = -0.5375
        gap_lbl = _ink_text("Δ=2.1 eV", font_size=12)
        gap_lbl.move_to([gap_x - 0.68, gap_mid_y, 0])
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # --- Chips ---
        # Lowest line is Na 3s at y ≈ -1.325; chips at y = -2.15
        h_chip = LabelChip("H: 3s=3p=3d", accent=TEAL, size=15)
        h_chip.move_to([-0.55, -2.15, 0])
        self.play(GrowFromCenter(h_chip), run_time=0.4)

        na_chip = LabelChip("Na: E(3s)<E(3p)", accent=CRIMSON, size=15)
        na_chip.move_to([0.65, -2.65, 0])
        self.play(GrowFromCenter(na_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.25 + 0.2 + 0.5 + 0.3 + 0.25 +
                   0.4 + 0.4 + 0.3 + 0.3 + 0.4 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
