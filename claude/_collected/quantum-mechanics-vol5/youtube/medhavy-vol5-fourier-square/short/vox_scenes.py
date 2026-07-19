"""vox_scenes.py — medhavy-vol5-fourier-square/short (9:16 portrait)
Reel: Fourier Square Wave — Gibbs Overshoot Never Goes Away
Palette: medhavy (Okabe-Ito)

Physics:
  f(x) = (4/pi) * sum_{n=1,3,5,7,9} (1/n)*sin(n*pi*x/L)
  Gibbs overshoot: max ≈ 1.09 (9% above 1.0), always
  At x=L/2: exact convergence to 1.0

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Axes center: (0, 0.1); x_range=[0,1], y_range=[-0.3,1.4]
  x_length=3.2, y_length=4.2
  x_scale = 3.2/1.0 = 3.2 u/unit; y_scale = 4.2/1.7 ≈ 2.471 u/unit

  sx(x) = -1.6 + x * 3.2
  sy(y) = 0.1 - 2.1 + (y+0.3)/1.7 * 4.2 = -2.0 + (y+0.3)*2.471

  Key points:
    x_peak ≈ 0.056: sx = -1.6 + 0.056*3.2 = -1.421
    y_peak ≈ 1.09: sy = -2.0 + 1.39*2.471 = -2.0 + 3.435 = 1.435
    x=0.5: sx = 0.0; y=1.0: sy = -2.0 + 1.3*2.471 = -2.0 + 3.212 = 1.212
    y=0: sy = -2.0 + 0.3*2.471 = -2.0 + 0.741 = -1.259

  x-axis at y = 0.1 - 2.1 = -2.0
  Chips at y=-2.65 and y=-3.1
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

def _fourier_sq(x_arr, N_terms, L=1.0):
    result = np.zeros_like(x_arr)
    for k in range(N_terms):
        n = 2 * k + 1
        result += (4.0 / (n * np.pi)) * np.sin(n * np.pi * x_arr / L)
    return result


class B03_FourierSquareRun(Scene):
    """Portrait Fourier square wave scene.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")
        L = 1.0
        N_terms = 5  # odd harmonics 1,3,5,7,9

        # Axis parameters
        cx, cy = 0.0, 0.1
        x_len, y_len = 3.2, 4.2
        x_min, x_max = 0.0, 1.0
        y_min, y_max = -0.3, 1.4

        def sx(xv):
            return cx - x_len / 2 + (xv - x_min) / (x_max - x_min) * x_len

        def sy(yv):
            return cy - y_len / 2 + (yv - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -2.0

        # Key coordinates
        x_peak = 1.0 / (2.0 * 9.0)  # ≈ 0.056
        y_peak_val = float(_fourier_sq(np.array([x_peak]), N_terms, L)[0])
        peak_dot_x = sx(x_peak)
        peak_dot_y = sy(y_peak_val)

        # Header
        header = _ink_text("Fourier N=9  Gibbs +9%", font_size=16, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes — no tick numbers
        axes = Axes(
            x_range=[x_min, x_max, 0.25],
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
        x_lbl = _ink_text("x/L", font_size=13)
        x_lbl.move_to([sx(x_max) - 0.20, x_axis_y + 0.32, 0])
        y_lbl = _ink_text("f(x)", font_size=14)
        y_lbl.move_to([-1.72, cy + 0.3, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Sparse ticks
        for xv, xl in [(0.5, "0.5")]:
            lbl = _ink_text(xl, font_size=12)
            lbl.move_to([sx(xv), x_axis_y - 0.22, 0])
            self.add(lbl)

        for yv, yl in [(1.0, "1")]:
            lbl = _ink_text(yl, font_size=12)
            lbl.move_to([-1.75, sy(yv), 0])
            self.add(lbl)

        # SLATE dashed: true square wave target at y=1.0 from x=0 to 0.5
        sq_line = DashedLine(
            start=[sx(0), sy(1.0), 0], end=[sx(0.5), sy(1.0), 0],
            color=SLATE, stroke_width=1.2, dash_length=0.10
        )
        ref_lbl = _ink_text("true=1", font_size=12)
        ref_lbl.move_to([-1.75, sy(1.0) + 0.25, 0])
        self.play(FadeIn(sq_line), FadeIn(ref_lbl), run_time=0.3)

        # --- TEAL Fourier curve ---
        fourier_curve = axes.plot(
            lambda xv: _fourier_sq(np.array([xv]), N_terms, L)[0],
            x_range=[0.001, L - 0.001],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(fourier_curve), run_time=0.8)

        # --- CRIMSON dot at Gibbs peak ---
        peak_dot = Dot(point=[peak_dot_x, peak_dot_y, 0], radius=0.11, color=CRIMSON,
                       fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(peak_dot), run_time=0.3)

        # Gibbs label: right of dot, above it — peak is at x≈-1.42, y≈1.44
        # Move label to right side where curve is low
        gibbs_lbl = _ink_text("+9%", font_size=14)
        gibbs_lbl.move_to([peak_dot_x + 0.55, peak_dot_y + 0.05, 0])
        self.play(FadeIn(gibbs_lbl), run_time=0.25)

        # Midpoint dot at x=L/2
        mid_dot = Dot(point=[sx(0.5), sy(1.0), 0], radius=0.10, color=TEAL,
                      fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(mid_dot), run_time=0.25)

        # --- Chips ---
        gibbs_chip = LabelChip("Gibbs +9%", accent=CRIMSON, size=16)
        gibbs_chip.move_to([-0.55, -2.65, 0])
        self.play(GrowFromCenter(gibbs_chip), run_time=0.4)

        conv_chip = LabelChip("x=0.5: f=1.00", accent=TEAL, size=16)
        conv_chip.move_to([0.60, -3.08, 0])
        self.play(GrowFromCenter(conv_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.3 + 0.8 + 0.3 + 0.25 + 0.25 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
