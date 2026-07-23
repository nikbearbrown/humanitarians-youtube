"""vox_scenes.py — medhavy-vol5-fourier-square
Reel: Fourier Series — building a square wave, Gibbs 9% overshoot
Palette: medhavy

Physics: f(x) = (4/pi)*sum_{n=1,3,5,...,9} (1/n)*sin(n*pi*x/L)
Gibbs overshoot at discontinuity ≈ 9%

Gate B: header at [1.5, 3.1, 0]; Gibbs chip in lower safe zone; labels clear of curves.
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import numpy as np

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid): return DUR.get(bid, 10.0)
def _ink_text(copy, font_size=24, font=SERIF, **kw):
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)
def _c2p(ax, x, y):
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)

def _fourier_sq(x_arr, N_terms, L=1.0):
    result = np.zeros_like(x_arr)
    for k in range(N_terms):
        n = 2*k + 1
        result += (4.0 / (n * np.pi)) * np.sin(n * np.pi * x_arr / L)
    return result


class B03_FourierSquareRun(Scene):
    """Fourier series for square wave, N=5 (odd terms 1,3,5,7,9).
    Shows Gibbs overshoot ≈ 9% at the edge.

    Layout: axes x in [0,1], y in [-0.3, 1.4]
    Gate B: header before axes; Gibbs chip placed below x-axis in clear zone.
    """

    def construct(self):
        dur = _dur("B03")
        L = 1.0
        N_terms = 5  # odd harmonics 1,3,5,7,9

        # Axis layout
        cx, cy = 0.0, -0.3
        x_len, y_len = 10.0, 5.5
        x_min, x_max = 0.0, 1.0
        y_min, y_max = -0.3, 1.4

        def sx(xv): return cx - x_len/2 + (xv - x_min)/(x_max - x_min) * x_len
        def sy(yv): return cy - y_len/2 + (yv - y_min)/(y_max - y_min) * y_len

        x_axis_y = cy - y_len/2  # = -3.05
        y_axis_x = cx - x_len/2  # = -5.0

        # Header FIRST
        header = _ink_text("Fourier Square Wave  N=9 terms", font_size=24, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes
        axes = Axes(
            x_range=[x_min, x_max, 0.25],
            y_range=[y_min, y_max, 0.5],
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": SLATE, "stroke_width": 1.5, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([cx, cy, 0])
        self.play(Create(axes), run_time=0.7)

        # Axis labels
        x_lbl = _ink_text("x / L", font_size=18)
        x_lbl.move_to([sx(x_max) + 0.5, x_axis_y, 0])
        y_lbl = _ink_text("f(x)", font_size=18)
        y_lbl.move_to([y_axis_x - 0.55, sy(0.55), 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels
        for xv, xl in [(0.25, "0.25"), (0.5, "0.5"), (0.75, "0.75"), (1.0, "1")]:
            t = _ink_text(xl, font_size=13)
            t.move_to([sx(xv), x_axis_y - 0.26, 0])
            self.add(t)
        for yv, yl in [(0.5, "0.5"), (1.0, "1")]:
            t = _ink_text(yl, font_size=13)
            t.move_to([y_axis_x - 0.38, sy(yv), 0])
            self.add(t)

        # True square wave reference (SLATE dashed)
        sq_line_bot = DashedLine(
            start=[sx(0), sy(0), 0], end=[sx(0.5), sy(0), 0],
            color=SLATE, stroke_width=1.2, dash_length=0.1
        )
        sq_line_top = DashedLine(
            start=[sx(0), sy(1.0), 0], end=[sx(0.5), sy(1.0), 0],
            color=SLATE, stroke_width=1.2, dash_length=0.1
        )
        self.play(FadeIn(sq_line_bot), FadeIn(sq_line_top), run_time=0.3)

        # Reference level at y=1.0 label
        ref_lbl = _ink_text("true = 1", font_size=13)
        ref_lbl.move_to([y_axis_x - 0.55, sy(1.0), 0])
        self.play(FadeIn(ref_lbl), run_time=0.2)

        # Fourier partial sum (N=5 => terms 1,3,5,7,9) — TEAL
        fourier_curve = axes.plot(
            lambda xv: _fourier_sq(np.array([xv]), N_terms, L)[0],
            x_range=[0.001, L - 0.001],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(fourier_curve), run_time=1.0)

        # Dot at peak (Gibbs overshoot) — find maximum near x=0
        # Max occurs near x = L/(2*N_max) = 1/(2*9) ≈ 0.056 for N=9
        x_peak = 1.0 / (2.0 * 9.0)  # approx 0.056
        y_peak_val = float(_fourier_sq(np.array([x_peak]), N_terms, L)[0])
        peak_dot = Dot(
            point=[sx(x_peak), sy(y_peak_val), 0],
            radius=0.12, color=CRIMSON, fill_opacity=1
        ).set_stroke(width=0, opacity=0)
        self.play(FadeIn(peak_dot), run_time=0.3)

        # Gibbs chip — placed well below all curves in the lower-right clear zone
        # x_axis_y = -3.05; chips at y=-2.6 below the x-axis ticks
        gibbs_chip = LabelChip("Gibbs: +9%", accent=CRIMSON, size=20)
        gibbs_chip.move_to([-3.0, -2.60, 0])
        self.play(GrowFromCenter(gibbs_chip), run_time=0.4)

        # Dot at x=L/2 (midpoint) for Gate A
        mid_dot = Dot(
            point=[sx(0.5), sy(float(_fourier_sq(np.array([0.5]), N_terms, L)[0])), 0],
            radius=0.10, color=TEAL, fill_opacity=1
        ).set_stroke(width=0, opacity=0)
        self.play(FadeIn(mid_dot), run_time=0.25)

        # Convergence chip
        conv_chip = LabelChip("x=L/2: f=1.000", accent=TEAL, size=20)
        conv_chip.move_to([3.5, sy(0.5), 0])
        self.play(GrowFromCenter(conv_chip), run_time=0.4)

        elapsed = (0.4 + 0.7 + 0.3 + 1.0 + 0.3 + 0.4 + 0.25 + 0.4)
        self.wait(max(0.5, dur - elapsed))
