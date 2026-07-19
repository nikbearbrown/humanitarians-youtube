"""vox_scenes.py — medhavy-vol5-multiplicity-peak
Reel: Multiplicity Omega = C(N,n) — peak at n=N/2
Palette: medhavy

Physics: Omega(N,n) = C(N,n) = N!/(n!(N-n)!)
N=10: C(10,5)=252 at peak; C(10,4)=210

Scene: Bar chart of Omega(10,n) for n=0..10
Gate B: header before axes; peak chip above peak bar; labels clear of bars.
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import numpy as np
from math import comb

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


class B03_MultiplicityRun(Scene):
    """Bar chart: Omega(10,n) = C(10,n) for n=0..10.
    Peak at n=5, Omega=252.

    Layout: axes with bars; n on x-axis (0..10), Omega on y-axis (0..280).
    Gate B: header before axes; peak chip ABOVE the peak bar, in clear zone.
    """

    def construct(self):
        dur = _dur("B03")
        N = 10
        n_vals = list(range(N+1))  # 0..10
        omega_vals = [comb(N, n) for n in n_vals]
        omega_max = max(omega_vals)  # 252

        # Layout parameters
        cx, cy = 0.0, -0.3
        x_len, y_len = 10.0, 5.0
        n_min, n_max = 0, N
        o_min, o_max = 0, 280

        def sx(nv): return cx - x_len/2 + (nv - n_min)/(n_max - n_min) * x_len
        def sy(ov): return cy - y_len/2 + (ov - o_min)/(o_max - o_min) * y_len

        x_axis_y = cy - y_len/2  # = -2.8
        y_axis_x = cx - x_len/2  # = -5.0

        # Header FIRST (before axes)
        header = _ink_text("Multiplicity  N=10 spins", font_size=26, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes
        axes = Axes(
            x_range=[n_min - 0.5, n_max + 0.5, 1],
            y_range=[o_min, o_max, 50],
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": SLATE, "stroke_width": 1.5, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([cx, cy, 0])
        self.play(Create(axes), run_time=0.6)

        # Axis labels
        x_lbl = _ink_text("n (up spins)", font_size=18)
        x_lbl.move_to([cx, x_axis_y - 0.42, 0])
        y_lbl = _ink_text("C(10,n)", font_size=18)
        y_lbl.move_to([y_axis_x - 0.6, cy, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # y-axis tick labels: 50, 100, 150, 200, 250
        for ov in [50, 100, 150, 200, 250]:
            t = _ink_text(str(ov), font_size=13)
            t.move_to([y_axis_x - 0.42, sy(ov), 0])
            self.add(t)

        # Bar width
        bar_w = x_len / (n_max - n_min + 1) * 0.7  # 70% of spacing

        # Draw bars one by one — each is a Gate A distinct shape state
        for i, (n, omega) in enumerate(zip(n_vals, omega_vals)):
            x_center = sx(n)
            bar_height = sy(omega) - sy(0)
            bar = Rectangle(
                width=bar_w,
                height=max(bar_height, 0.05),
                fill_color=TEAL if n != N//2 else CRIMSON,
                fill_opacity=1,
                stroke_width=0,
            )
            bar.set_stroke(width=0, opacity=0)
            bar.move_to([x_center, sy(0) + bar_height/2, 0])

            # n label below x-axis
            n_lbl = _ink_text(str(n), font_size=13)
            n_lbl.move_to([x_center, x_axis_y - 0.22, 0])

            self.play(GrowFromPoint(bar, point=[x_center, sy(0), 0]),
                      FadeIn(n_lbl), run_time=0.15)

        # Peak chip ABOVE peak bar — peak is at n=5, omega=252
        # sy(252) is the top of the peak bar; place chip ABOVE it
        peak_top_y = sy(omega_max)
        peak_chip = LabelChip("C(10,5)=252", accent=CRIMSON, size=21)
        peak_chip.move_to([sx(5), peak_top_y + 0.45, 0])
        self.play(GrowFromCenter(peak_chip), run_time=0.4)

        # Peak at n=N/2 chip in clear zone right of chart
        sym_chip = LabelChip("peak at n=N/2", accent=TEAL, size=19)
        sym_chip.move_to([4.5, 2.5, 0])
        self.play(GrowFromCenter(sym_chip), run_time=0.4)

        elapsed = (0.4 + 0.6 + 0.3 + 11*0.15 + 0.4 + 0.4)
        self.wait(max(0.5, dur - elapsed))
