"""vox_scenes.py — medhavy-vol3-golden-rule
Reel: Fermi's Golden Rule Γ ∝ V² — Rate vs Coupling Strength
Palette: medhavy (Okabe-Ito)

Physics:
  Γ = (2π/ℏ) |⟨f|V̂|i⟩|² ρ(E_f)
  Rate ∝ V² (quadratic in coupling)
  Reference: H 2p→1s, A = 6.27×10⁸ s⁻¹ (NIST Lyman-alpha)

Display units: V in eV (x), Γ in 10⁸ s⁻¹ (y)
  Scale k = 6.27 (so Γ(V=1 eV) = 6.27 × 10⁸ s⁻¹ = A_H)
  y_range = [0, 26]; at V=2: Γ = 6.27×4 = 25.08 ≈ 25
  Reference dot: (V=1, Γ=6.27)

Gate A: axes.c2p not used outside plot(); label positions via sx/sy helpers
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]

Layout:
  Axes center: (0.2, -0.1); x_range=[0,2], y_range=[0,26]
  x_length=9.0, y_length=5.2
  x_scale = 9.0/2 = 4.5 u/eV; y_scale = 5.2/26 = 0.2 u/(10⁸ s⁻¹)
  x-axis at y = -0.1 - 5.2/2 = -2.7; chips at y = -3.05
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


class B03_GoldenRuleRun(Scene):
    """Quadratic Γ(V) = k·V² curve with H reference point.

    All label coordinates computed via sx/sy (pure float) — no axes.c2p.
    """

    def construct(self):
        dur = _dur("B03")

        # Display parameters
        k = 6.27   # 10⁸ s⁻¹ / eV²  (so Γ(1 eV) = 6.27 = A_H in display units)

        # Axis parameters
        cx, cy = 0.2, -0.1
        x_len, y_len = 9.0, 5.2
        x_min, x_max = 0.0, 2.0
        y_min, y_max = 0.0, 26.0

        def sx(v_val):
            return cx - x_len / 2 + (v_val - x_min) / (x_max - x_min) * x_len

        def sy(gamma_val):
            return cy - y_len / 2 + (gamma_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.7

        # Reference point: V=1 eV, Γ=6.27
        v_ref = 1.0
        g_ref = k * v_ref ** 2   # = 6.27
        dot_x = sx(v_ref)         # sx(1.0)
        dot_y = sy(g_ref)         # sy(6.27)

        # Header
        header = _ink_text("Fermi's Golden Rule:  Γ ∝ V²", font_size=22, font=DISPLAY)
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
        # x-label: ABOVE the x-axis at right end (y slightly above x-axis stroke)
        # x-axis at y=-2.7; place label at y=-2.45 (above x-axis, clear of chips below)
        x_lbl = _ink_text("V  (eV)", font_size=18)
        x_lbl.move_to([sx(x_max) - 0.5, x_axis_y + 0.30, 0])
        y_lbl = _ink_text("Γ  (10⁸ s⁻¹)", font_size=16)
        y_lbl.move_to([sx(x_min) - 1.05, cy, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Manual tick labels — placed close to x-axis, NOT overlapping chip area
        for v_val in [0.5, 1.0, 1.5, 2.0]:
            lbl = _ink_text(str(v_val), font_size=14)
            lbl.move_to([sx(v_val), x_axis_y - 0.22, 0])
            self.add(lbl)

        for g_val in [5, 10, 15, 20, 25]:
            lbl = _ink_text(str(g_val), font_size=14)
            lbl.move_to([sx(x_min) - 0.42, sy(g_val), 0])
            self.add(lbl)

        # --- TEAL parabolic rate curve: Γ = k·V² ---
        curve = axes.plot(
            lambda v: k * v ** 2,
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(curve), run_time=0.7)

        # "Γ ∝ V²" label: placed in the UPPER LEFT of the plot (clear of curve)
        # At V=0.4: Γ = 6.27*0.16 = 1.003 → sy(1.0) ≈ -2.5
        # Place label high up at (sx(0.3), sy(22)) — above the curve at that x
        # sy(22) = -0.1 - 2.6 + (22-0)/26 * 5.2 = -2.7 + 4.4 = 1.7
        scaling_lbl = _ink_text("Γ ∝ V²", font_size=20)
        scaling_lbl.move_to([sx(0.35), sy(22.0), 0])
        self.play(FadeIn(scaling_lbl), run_time=0.3)

        loglog_lbl = _ink_text("log-log slope = 2", font_size=16)
        loglog_lbl.move_to([sx(0.35), sy(19.5), 0])
        self.play(FadeIn(loglog_lbl), run_time=0.25)

        # --- CRIMSON reference dot at V=1 eV, Γ=6.27×10⁸ s⁻¹ ---
        dot = Dot(point=[dot_x, dot_y, 0], radius=0.13, color=CRIMSON,
                  fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot), run_time=0.35)

        # Reference label: above and to the right of the dot
        ref_lbl = _ink_text("H 2p→1s", font_size=15)
        ref_lbl.move_to([dot_x + 1.2, dot_y + 0.45, 0])
        self.play(FadeIn(ref_lbl), run_time=0.3)

        rate_lbl = _ink_text("6.27×10⁸ s⁻¹", font_size=14)
        rate_lbl.move_to([dot_x + 1.2, dot_y + 0.10, 0])
        self.play(FadeIn(rate_lbl), run_time=0.25)

        # Dashed v-line and h-line to dot (for reference)
        v_tick_line = DashedLine(start=[dot_x, x_axis_y, 0], end=[dot_x, dot_y, 0],
                                 color=SLATE, stroke_width=1.0, dash_length=0.12)
        h_tick_line = DashedLine(start=[sx(x_min), dot_y, 0], end=[dot_x, dot_y, 0],
                                 color=SLATE, stroke_width=1.0, dash_length=0.12)
        self.play(Create(v_tick_line), Create(h_tick_line), run_time=0.4)

        # --- Chips ---
        # x-label now above x-axis at y=-2.40 (no conflict); chips at y=-3.10
        quad_chip = LabelChip("Γ ∝ V²  (slope=2)", accent=TEAL, size=18)
        quad_chip.move_to([-2.5, -3.10, 0])
        self.play(GrowFromCenter(quad_chip), run_time=0.4)

        ref_chip = LabelChip("H 2p:  6.27×10⁸ s⁻¹", accent=CRIMSON, size=18)
        ref_chip.move_to([3.5, -3.10, 0])
        self.play(GrowFromCenter(ref_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.7 + 0.3 + 0.25 + 0.35 + 0.3 + 0.25 + 0.4 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
