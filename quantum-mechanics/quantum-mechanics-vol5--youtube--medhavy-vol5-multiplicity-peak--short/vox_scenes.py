"""vox_scenes.py — medhavy-vol5-multiplicity-peak/short (9:16 portrait)
Reel: Multiplicity Omega = C(N,n) — peak at n=N/2
Palette: medhavy (Okabe-Ito)

Physics:
  Omega(N,n) = C(N,n) = N! / (n!(N-n)!)
  N=10: C(10,5)=252 (peak); C(10,4)=210 (adjacent)
  Peak at exactly n=N/2=5 by Pascal symmetry.

Portrait layout:
  Safe area: +-1.95x / +-3.4y
  Single panel: center (0, 0.1); x_range=[-0.5,10.5], y_range=[0,280]
                x_length=3.2, y_length=4.5

  sx(nv) = -1.6 + (nv + 0.5) / 11 * 3.2
  sy(ov) = 0.1 - 2.25 + ov / 280 * 4.5

  Chips at y=-2.85 and y=-3.28
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
from math import comb

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

_DEFAULTS = {"B03": 24.27}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)

# Physics
N = 10
n_vals = list(range(N + 1))
omega_vals = [comb(N, n) for n in n_vals]
omega_max = max(omega_vals)  # 252

# Panel geometry
pan_w = 3.2
pan_h = 4.5
cx, cy_pan = 0.0, 0.1
n_min_ax, n_max_ax = -0.5, 10.5
o_min_ax, o_max_ax = 0.0, 280.0

def sx(nv: float) -> float:
    return cx - pan_w / 2 + (nv - n_min_ax) / (n_max_ax - n_min_ax) * pan_w

def sy(ov: float) -> float:
    return cy_pan - pan_h / 2 + (ov - o_min_ax) / (o_max_ax - o_min_ax) * pan_h

x_axis_y = cy_pan - pan_h / 2   # = 0.1 - 2.25 = -2.15
y_axis_x = cx - pan_w / 2       # = -1.6


class B03_MultiplicityRun(Scene):
    """Portrait bar chart: Omega(10,n) = C(10,n) for n=0..10.

    All label positions via sx()/sy() pure-float helpers (Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Header
        header = _ink_text("Multiplicity  N=10", font_size=15, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Subtitle
        sub = _ink_text("Omega(N,n) = C(N,n)", font_size=11)
        sub.move_to([0, 2.82, 0])
        self.play(FadeIn(sub), run_time=0.3)

        # Axes
        ax = Axes(
            x_range=[n_min_ax, n_max_ax, 1],
            y_range=[o_min_ax, o_max_ax, 50],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        ax.move_to([cx, cy_pan, 0])
        self.play(Create(ax), run_time=0.5)

        # Axis labels — placed below x-axis and left of y-axis, in clear zones
        x_lbl = _ink_text("n (up spins)", font_size=10)
        x_lbl.move_to([cx, x_axis_y - 0.30, 0])   # y = -2.45 (above chips at -2.85)
        y_lbl = _ink_text("C(10,n)", font_size=10)
        y_lbl.move_to([y_axis_x - 0.28, cy_pan + 0.5, 0])  # x=-1.88, y=0.6 (left of bars)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.25)

        # y-tick labels: 100, 200 (sparse to avoid crowding)
        for ov in [100, 200]:
            t = _ink_text(str(ov), font_size=9)
            t.move_to([y_axis_x - 0.28, sy(ov), 0])
            self.add(t)

        # Bar width — fit 11 bars in 3.2 units
        bar_spacing = pan_w / 11   # = 0.2909 per bar slot
        bar_w = bar_spacing * 0.72  # = 0.209

        # Draw bars
        for n, omega in zip(n_vals, omega_vals):
            x_center = sx(n)
            bar_height = sy(omega) - sy(0)
            bar = Rectangle(
                width=bar_w,
                height=max(bar_height, 0.04),
                fill_color=TEAL if n != N // 2 else CRIMSON,
                fill_opacity=1,
                stroke_width=0,
            )
            bar.set_stroke(width=0, opacity=0)
            bar.move_to([x_center, sy(0) + bar_height / 2, 0])

            # n label below x-axis (only for n=0,5,10 to avoid crowding)
            if n in (0, 5, 10):
                n_lbl = _ink_text(str(n), font_size=9)
                n_lbl.move_to([x_center, x_axis_y - 0.14, 0])
                self.play(GrowFromPoint(bar, point=[x_center, sy(0), 0]),
                          FadeIn(n_lbl), run_time=0.15)
            else:
                self.play(GrowFromPoint(bar, point=[x_center, sy(0), 0]), run_time=0.12)

        # Peak chip ABOVE peak bar (n=5, omega=252)
        # Peak bar top: sy(252). Pan top: cy_pan+pan_h/2=2.35. Sub at y=2.82.
        # sy(252) = 0.1-2.25 + 252/280*4.5 = -2.15 + 4.05 = 1.90
        # Place chip at y = sy(252)+0.38 = 2.28 — between panel top (2.35) and sub (2.82)
        # That is tight; use y=2.18 to be safe
        peak_top_y = sy(omega_max)  # 1.90
        peak_chip = LabelChip("C(10,5) = 252", accent=CRIMSON, size=14)
        peak_chip.move_to([sx(5), peak_top_y + 0.34, 0])  # y = 2.24
        self.play(GrowFromCenter(peak_chip), run_time=0.4)

        # Symmetry chip at bottom safe zone
        sym_chip = LabelChip("peak at n = N/2", accent=TEAL, size=14)
        sym_chip.move_to([0.20, -2.85, 0])
        self.play(GrowFromCenter(sym_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.5 + 0.25
                   + 3 * 0.15 + 8 * 0.12   # bar animation
                   + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
