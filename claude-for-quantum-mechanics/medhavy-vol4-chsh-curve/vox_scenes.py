"""vox_scenes.py — medhavy-vol4-chsh-curve
Reel: CHSH Correlation Curve — Quantum Beats the Classical Bound
Palette: medhavy (Okabe-Ito)

Physics:
  Singlet correlation: E(θ) = −cos(θ)
  CHSH score at optimal angles (0°,45°,90°,135°): S_QM = 2√2 ≈ 2.828
  Classical bound: |S| ≤ 2
  Cirel'son bound: |S| ≤ 2√2 ≈ 2.828 (quantum ceiling)
  Gap = 2√2 − 2 ≈ 0.828

Display:
  x_range=[0°, 180°]; y_range=[-1.3, 1.3] for E(θ) = −cos(θ)
  TEAL curve: E(θ) = −cos(θ)
  TEAL dot at θ=45°: E = −cos(45°) = −√2/2 ≈ −0.707
  CRIMSON dot at θ=90°: E = 0 (zero correlation)
  Text annotations: S_QM and S_classical as chip labels
  DoubleArrow: from E(45°) up to 0, showing |E| = √2/2

Gate A: axes.c2p not used for arithmetic — label positions via sx/sy helpers
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]

Layout:
  Axes center: (0, -0.1); x_range=[0,180], y_range=[-1.3,1.3]
  x_length=9.0, y_length=5.0
  x_scale = 9.0/180 = 0.05 u/deg; y_scale = 5.0/2.6 ≈ 1.923 u/unit

  sx(deg) = -4.5 + deg/180 * 9.0
  sy(e)   = -0.1 - 2.5 + (e+1.3)/2.6 * 5.0 = -2.6 + (e+1.3)*1.923

  Key points:
    θ=45°: sx = -4.5 + 0.25*9.0 = -4.5 + 2.25 = -2.25
    θ=90°: sx = -4.5 + 0.5*9.0 = 0.0
    θ=135°: sx = 2.25
    E=−0.707: sy = -2.6 + 0.593*1.923 = -2.6 + 1.140 = -1.460
    E=0: sy = -2.6 + 1.3*1.923 = -2.6 + 2.5 = -0.1
    E=+0.707: sy = -2.6 + 2.007*1.923 = -2.6 + 3.860 = 1.260
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

def _E(deg):
    """CHSH singlet correlation: E(θ) = −cos(θ) in radians."""
    return -np.cos(np.radians(deg))


class B03_CHSHRun(Scene):
    """E(θ) = −cos(θ) correlation curve with CHSH bound annotations.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, -0.1
        x_len, y_len = 9.0, 5.0
        x_min, x_max = 0.0, 180.0
        y_min, y_max = -1.3, 1.3

        def sx(deg_val):
            return cx - x_len / 2 + (deg_val - x_min) / (x_max - x_min) * x_len

        def sy(e_val):
            return cy - y_len / 2 + (e_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.6

        # Key coordinates
        deg45, deg90, deg135 = 45.0, 90.0, 135.0
        E45 = _E(deg45)    # ≈ −0.707
        E90 = _E(deg90)    # = 0.0
        E135 = _E(deg135)  # ≈ +0.707
        dot45_x = sx(deg45)   # = -2.25
        dot45_y = sy(E45)     # ≈ -1.460
        dot90_x = sx(deg90)   # = 0.0
        dot90_y = sy(E90)     # ≈ -0.1

        # Header
        header = _ink_text("CHSH: Quantum Beats the Classical Bound", font_size=20, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes
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
        # x-label: past axis right end, vertically on the axis line
        x_lbl = _ink_text("theta (deg)", font_size=18)
        x_lbl.move_to([sx(180) + 0.8, x_axis_y, 0])
        # y-label: moved up to sy(0.5) to avoid overlap with "0" tick at sy(0)=cy
        y_lbl = _ink_text("E(th)", font_size=16)
        y_lbl.move_to([sx(x_min) - 0.70, sy(0.5), 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels
        for deg_val in [45, 90, 135]:
            lbl = _ink_text(f"{deg_val}°", font_size=14)
            lbl.move_to([sx(deg_val), x_axis_y - 0.25, 0])
            self.add(lbl)

        for e_val in [-1.0, 0.0, 1.0]:
            lbl = _ink_text(f"{e_val:+.0f}" if e_val != 0 else "0", font_size=14)
            lbl.move_to([sx(x_min) - 0.45, sy(e_val), 0])
            self.add(lbl)

        # --- TEAL curve: E(θ) = −cos(θ) ---
        curve = axes.plot(
            lambda deg: _E(deg),
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(curve), run_time=0.7)

        # Curve label: upper-right end of curve (E→+1 at 180°)
        # sy(+1) = -2.6 + 2.3*1.923 = -2.6 + 4.42 → above safe area
        # Place at θ=160°, E=−cos160°≈+0.94: sy ≈ -2.6 + 2.24*1.923 ≈ 1.71
        curve_lbl = _ink_text("−cos θ", font_size=16)
        curve_lbl.move_to([sx(155), sy(0.90) + 0.30, 0])
        self.play(FadeIn(curve_lbl), run_time=0.3)

        # --- TEAL dot at θ=45° (optimal angle) ---
        dot45 = Dot(point=[dot45_x, dot45_y, 0], radius=0.13, color=TEAL,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot45), run_time=0.3)

        # Label: left of dot, below it
        lbl45 = _ink_text("45°: E=−0.707", font_size=15)
        lbl45.move_to([dot45_x - 1.40, dot45_y - 0.38, 0])
        self.play(FadeIn(lbl45), run_time=0.25)

        # --- CRIMSON dot at θ=90° (zero correlation) ---
        dot90 = Dot(point=[dot90_x, dot90_y, 0], radius=0.13, color=CRIMSON,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot90), run_time=0.3)

        # Label: below dot; curve at x=dot90_x is at E=0; below = below the x-axis crossing
        lbl90 = _ink_text("90°: E=0", font_size=15)
        lbl90.move_to([dot90_x, dot90_y - 0.65, 0])
        self.play(FadeIn(lbl90), run_time=0.25)

        # --- CHSH score annotation box ---
        # S_QM = 2√2 from 4 optimal correlations
        s_lbl = _ink_text("S_QM = 2√2 ≈ 2.828\nS_class ≤ 2\ngap = 0.828", font_size=15)
        s_lbl.move_to([2.80, sy(-0.5), 0])
        self.play(FadeIn(s_lbl), run_time=0.35)

        # --- Chips ---
        qm_chip = LabelChip("S_QM = 2√2 (Cirelson)", accent=TEAL, size=18)
        qm_chip.move_to([-3.0, -3.10, 0])
        self.play(GrowFromCenter(qm_chip), run_time=0.4)

        bell_chip = LabelChip("S_classical ≤ 2 (Bell)", accent=CRIMSON, size=18)
        bell_chip.move_to([2.5, -3.10, 0])
        self.play(GrowFromCenter(bell_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.7 + 0.3 + 0.3 + 0.25 + 0.3 + 0.25 + 0.35 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
