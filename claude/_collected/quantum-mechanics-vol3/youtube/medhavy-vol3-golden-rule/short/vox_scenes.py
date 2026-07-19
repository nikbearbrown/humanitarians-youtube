"""vox_scenes.py — medhavy-vol3-golden-rule/short (9:16 portrait)
Safe area: ±1.95x / ±3.4y

Physics: Γ = (2π/ℏ)|V|²ρ, k=6.27 (Γ(1eV)=6.27×10⁸ s⁻¹ = A_H)

Layout:
  Axes centered at (0, 0.1); x_range=[0,2], y_range=[0,26]
  x_length=3.2, y_length=4.5
  x_scale = 3.2/2 = 1.6 u/eV
  y_scale = 4.5/26 = 0.173 u/(10⁸ s⁻¹)
  x-axis at y = 0.1 - 4.5/2 = 0.1 - 2.25 = -2.15
  Chips at y = -2.65 and y = -3.1

  sx(v) = 0 - 3.2/2 + v/2 * 3.2 = -1.6 + v*1.6
  sy(g) = 0.1 - 2.25 + g/26 * 4.5 = -2.15 + g*0.173

  Dot at V=1: sx(1)=-1.6+1.6=0; sy(6.27)=-2.15+6.27*0.173=-2.15+1.085=-1.065

  Labels:
    x-label: above x-axis at [sx(2)-0.3, -2.15+0.25, 0] = [1.3, -1.9, 0]
    y-label: at [-1.85, 0.1, 0]
    tick x: v=1,2 at y=-2.38 (below x-axis stroke)
    tick y: g=10,20 at x=-1.82

  All label x-positions within ±1.95 ✓
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


class B03_GoldenRuleRun(Scene):
    """Portrait Fermi Golden Rule rate curve Γ ∝ V²."""

    def construct(self):
        dur = _dur("B03")

        k = 6.27  # display prefactor

        cx, cy = 0.0, 0.1
        x_len, y_len = 3.2, 4.5
        x_min, x_max = 0.0, 2.0
        y_min, y_max = 0.0, 26.0

        def sx(v_val):
            return cx - x_len / 2 + (v_val - x_min) / (x_max - x_min) * x_len

        def sy(g_val):
            return cy - y_len / 2 + (g_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2  # = -2.15

        # --- Header ---
        header = _ink_text("Fermi's Golden Rule  Γ ∝ V²", font_size=14, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # --- Axes ---
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
        self.play(Create(axes), run_time=0.5)

        # Axis labels
        # x-label: at center-bottom, ABOVE x-axis stroke (y = x_axis_y + 0.55 = -1.60)
        # Place at x=0 (center of plot), not near any axis stroke (y-axis at x=-1.6, not x=0)
        x_lbl = _ink_text("V (eV)", font_size=13)
        x_lbl.move_to([0.0, x_axis_y + 0.55, 0])
        # y-label: short "Γ" at top of y-axis, to the RIGHT of the y-axis stroke
        # y-axis stroke at x=-1.6; label at x=-1.35 (clear): width of "Γ"≈0.15, right edge=-1.28 (fine)
        y_lbl = _ink_text("Γ", font_size=13)
        y_lbl.move_to([-1.35, cy + y_len / 2 + 0.10, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.25)

        # Tick labels
        for v_val in [1.0, 2.0]:
            lbl = _ink_text(str(int(v_val)), font_size=11)
            lbl.move_to([sx(v_val), x_axis_y - 0.22, 0])
            self.add(lbl)

        for g_val in [10, 20]:
            lbl = _ink_text(str(g_val), font_size=11)
            lbl.move_to([-1.82, sy(g_val), 0])
            self.add(lbl)

        # --- TEAL parabola ---
        curve = axes.plot(
            lambda v: k * v ** 2,
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.5
        )
        self.play(Create(curve), run_time=0.7)

        # Scaling label: UPPER LEFT of plot, clear of curve
        # At V=0.2: Γ = 6.27*0.04 = 0.25 → sy(0.25) ≈ -2.107 (near bottom)
        # Place label at (sx(0.2), sy(22)) → (-1.28, 1.656)
        scaling_lbl = _ink_text("Γ ∝ V²", font_size=14)
        scaling_lbl.move_to([sx(0.3), sy(22.0), 0])
        self.play(FadeIn(scaling_lbl), run_time=0.3)

        # --- CRIMSON dot at V=1 eV, Γ=6.27 ---
        dot_x = sx(1.0)    # = 0.0
        dot_y = sy(6.27)   # ≈ -1.065

        dot = Dot(point=[dot_x, dot_y, 0], radius=0.10, color=CRIMSON,
                  fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot), run_time=0.35)

        # Ref label: to the right and above dot
        ref_lbl = _ink_text("H 2p→1s", font_size=12)
        ref_lbl.move_to([dot_x + 0.75, dot_y + 0.38, 0])
        self.play(FadeIn(ref_lbl), run_time=0.3)

        rate_lbl = _ink_text("6.27×10⁸ s⁻¹", font_size=11)
        rate_lbl.move_to([dot_x + 0.80, dot_y + 0.08, 0])
        self.play(FadeIn(rate_lbl), run_time=0.25)

        # Dashed cross-hairs to dot
        v_tick = DashedLine(start=[dot_x, x_axis_y, 0], end=[dot_x, dot_y, 0],
                            color=SLATE, stroke_width=0.9, dash_length=0.10)
        h_tick = DashedLine(start=[sx(x_min), dot_y, 0], end=[dot_x, dot_y, 0],
                            color=SLATE, stroke_width=0.9, dash_length=0.10)
        self.play(Create(v_tick), Create(h_tick), run_time=0.35)

        # --- Chips ---
        # x-label at y = -2.15+0.28 = -1.87; chips at y=-2.65 and -3.1
        slope_chip = LabelChip("Γ ∝ V²", accent=TEAL, size=15)
        slope_chip.move_to([0, -2.65, 0])
        self.play(GrowFromCenter(slope_chip), run_time=0.4)

        ref_chip = LabelChip("H 2p: 6.27×10⁸ s⁻¹", accent=CRIMSON, size=15)
        ref_chip.move_to([0, -3.1, 0])
        self.play(GrowFromCenter(ref_chip), run_time=0.35)

        elapsed = (0.4 + 0.5 + 0.25 + 0.7 + 0.3 + 0.35 + 0.3 + 0.25 + 0.35 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
