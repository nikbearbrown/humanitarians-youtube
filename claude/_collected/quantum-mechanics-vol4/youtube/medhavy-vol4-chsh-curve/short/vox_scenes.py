"""vox_scenes.py — medhavy-vol4-chsh-curve/short (9:16 portrait)
Reel: CHSH Correlation Curve — Quantum Beats the Classical Bound
Palette: medhavy (Okabe-Ito)

Physics:
  E(θ) = −cos(θ); S_QM = 2√2 ≈ 2.828; S_classical ≤ 2
  Optimal angle: θ = 45°; gap = 0.828

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Axes center: (0, 0.1); x_range=[0,180], y_range=[-1.3,1.3]
  x_length=3.2, y_length=4.5
  x_scale = 3.2/180 u/deg; y_scale = 4.5/2.6 ≈ 1.731 u/unit

  sx(deg) = -1.6 + deg/180 * 3.2
  sy(e)   = 0.1 - 2.25 + (e+1.3)/2.6 * 4.5 = -2.15 + (e+1.3)*1.731

  Key points:
    θ=45°: sx = -1.6 + 0.25*3.2 = -1.6 + 0.8 = -0.8
    θ=90°: sx = -1.6 + 0.5*3.2 = 0.0
    θ=135°: sx = 0.8
    E=−0.707: sy = -2.15 + 0.593*1.731 = -2.15 + 1.026 = -1.124
    E=0: sy = -2.15 + 1.3*1.731 = -2.15 + 2.250 = 0.100
    E=+1: sy = -2.15 + 2.3*1.731 = -2.15 + 3.981 = 1.831 (above 3.4 — ok, not labeled)

  x-axis at y = 0.1 - 2.25 = -2.15
  Chips at y=-2.85 and y=-3.28
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

def _E(deg):
    return -np.cos(np.radians(deg))


class B03_CHSHRun(Scene):
    """Portrait E(θ) = −cos(θ) CHSH correlation plot.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, 0.1
        x_len, y_len = 3.2, 4.5
        x_min, x_max = 0.0, 180.0
        y_min, y_max = -1.3, 1.3

        def sx(deg_val):
            return cx - x_len / 2 + (deg_val - x_min) / (x_max - x_min) * x_len

        def sy(e_val):
            return cy - y_len / 2 + (e_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.15

        # Key coordinates
        dot45_x = sx(45.0)           # = -0.8
        dot45_y = sy(_E(45.0))       # sy(−0.707) ≈ -1.124
        dot90_x = sx(90.0)           # = 0.0
        dot90_y = sy(_E(90.0))       # sy(0) = 0.1

        # Header
        header = _ink_text("CHSH: −cos θ", font_size=18, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes — no tick numbers
        axes = Axes(
            x_range=[x_min, x_max, 45],
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
        # x-label: above x-axis at center (no ticks at center = 90°)
        x_lbl = _ink_text("theta", font_size=14)
        x_lbl.move_to([sx(90), x_axis_y + 0.35, 0])
        # y-label: left of y-axis, short
        y_lbl = _ink_text("E", font_size=16)
        y_lbl.move_to([-1.72, cy + 0.6, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Sparse tick labels
        for deg_val, label in [(45, "45"), (135, "135")]:
            lbl = _ink_text(label, font_size=11)
            lbl.move_to([sx(deg_val), x_axis_y - 0.22, 0])
            self.add(lbl)

        for e_val in [-1.0, 1.0]:
            lbl = _ink_text(f"{e_val:+.0f}", font_size=12)
            lbl.move_to([-1.78, sy(e_val), 0])
            self.add(lbl)

        # --- TEAL curve: E(θ) = −cos(θ) ---
        curve = axes.plot(
            lambda deg: _E(deg),
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(curve), run_time=0.7)

        # Curve label: near θ=150°, E=−cos150°=+cos30°≈0.866; sy≈1.64 (close to safe limit)
        # Place at (sx(140), sy(0.7)+0.25) → (0.40, 0.85)
        curve_lbl = _ink_text("-cos", font_size=13)
        curve_lbl.move_to([sx(140), sy(0.7) + 0.25, 0])
        self.play(FadeIn(curve_lbl), run_time=0.3)

        # --- TEAL dot at θ=45° ---
        dot45 = Dot(point=[dot45_x, dot45_y, 0], radius=0.11, color=TEAL,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot45), run_time=0.3)

        lbl45 = _ink_text("45°: −0.707", font_size=12)
        lbl45.move_to([dot45_x - 0.65, dot45_y - 0.38, 0])
        self.play(FadeIn(lbl45), run_time=0.25)

        # --- CRIMSON dot at θ=90° ---
        dot90 = Dot(point=[dot90_x, dot90_y, 0], radius=0.11, color=CRIMSON,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot90), run_time=0.3)

        lbl90 = _ink_text("90°: E=0", font_size=12)
        lbl90.move_to([dot90_x, dot90_y - 0.50, 0])
        self.play(FadeIn(lbl90), run_time=0.25)

        # CHSH score annotation
        s_lbl = _ink_text("S_QM = 2sqrt2\ngap = 0.828", font_size=13)
        s_lbl.move_to([0.60, sy(-0.5), 0])
        self.play(FadeIn(s_lbl), run_time=0.35)

        # --- Chips ---
        qm_chip = LabelChip("S_QM = 2sqrt2", accent=TEAL, size=16)
        qm_chip.move_to([-0.60, -2.85, 0])
        self.play(GrowFromCenter(qm_chip), run_time=0.4)

        bell_chip = LabelChip("S_class <= 2", accent=CRIMSON, size=16)
        bell_chip.move_to([0.55, -3.28, 0])
        self.play(GrowFromCenter(bell_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.7 + 0.3 + 0.3 + 0.25 + 0.3 + 0.25 + 0.35 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
