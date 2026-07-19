"""vox_scenes.py — medhavy-vol4-decoherence-t2
Reel: Qubit Decoherence — T2 exponential decay of off-diagonal rho
Palette: medhavy (colorblind-safe Okabe-Ito)

Physics: rho_01(t) = e^(-t/T2); T2=1 us
At t=T2: |rho_01|=0.3679

Gate B placement:
  - Header at [1.5, 3.1, 0] (right of y-axis, inside safe area)
  - T2 marker: vertical dashed line at t=1 us; chip placed right of the line
  - 1/e chip placed at safe position: [3.5, 1.5, 0]
  - Axis labels: x past axis end; y at fixed far-left coord
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


# =============================================================================
# B03_DecoherenceRun — |rho_01(t)| exponential decay
# =============================================================================
class B03_DecoherenceRun(Scene):
    """Qubit dephasing: rho_01(t) = e^(-t/T2)
    T2=1 us; plot t in [0, 4 us], rho_01 in [0, 1.1]

    Gate B: header before axes; T2 marker and chips in clear zones.
    All label positions computed as scene floats (no c2p on math paths).
    """

    def construct(self):
        dur = _dur("B03")

        T2_us = 1.0  # microseconds
        t_max = 4.0  # microseconds
        one_over_e = np.exp(-1.0)  # 0.3679

        # Axis layout parameters
        cx, cy = 0.0, -0.2
        x_len, y_len = 10.0, 5.0
        x_min, x_max = 0.0, t_max
        y_min, y_max = 0.0, 1.1

        def sx(t_us): return cx - x_len/2 + (t_us - x_min)/(x_max - x_min) * x_len
        def sy(rho):  return cy - y_len/2 + (rho - y_min)/(y_max - y_min) * y_len

        x_axis_y = cy - y_len/2  # = -2.7
        y_axis_x = cx - x_len/2  # = -5.0

        # Header FIRST (before axes)
        header = _ink_text("Qubit Decoherence  T2 = 1 us", font_size=24, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes
        axes = Axes(
            x_range=[x_min, x_max, 1.0],
            y_range=[y_min, y_max, 0.25],
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": SLATE, "stroke_width": 1.5, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([cx, cy, 0])

        self.play(Create(axes), run_time=0.7)

        # Axis labels at fixed safe positions
        x_lbl = _ink_text("t (us)", font_size=19)
        x_lbl.move_to([sx(t_max) + 0.55, x_axis_y, 0])
        y_lbl = _ink_text("|rho_01|", font_size=17)
        y_lbl.move_to([y_axis_x - 0.65, sy(0.55), 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Tick labels: x at 1,2,3,4; y at 0.5, 1.0
        for tv in [1, 2, 3, 4]:
            t = _ink_text(str(tv), font_size=14)
            t.move_to([sx(float(tv)), x_axis_y - 0.28, 0])
            self.add(t)
        for yv, yl in [(0.5, "0.5"), (1.0, "1.0")]:
            t = _ink_text(yl, font_size=14)
            t.move_to([y_axis_x - 0.38, sy(yv), 0])
            self.add(t)

        # Decay curve (TEAL): rho_01(t) = e^(-t/T2)
        decay_curve = axes.plot(
            lambda t_us: np.exp(-t_us / T2_us),
            x_range=[0, t_max],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(decay_curve), run_time=0.9)

        # Dot at t=0 (rho=1) — Gate A shape state
        d0 = Dot(point=[sx(0), sy(1.0), 0], radius=0.10, color=TEAL, fill_opacity=1)
        d0.set_stroke(width=0, opacity=0)
        self.play(FadeIn(d0), run_time=0.25)

        # T2 marker: CRIMSON vertical dashed line at t=T2
        t2_x = sx(T2_us)
        t2_y_top = sy(one_over_e)
        t2_line = DashedLine(
            start=[t2_x, x_axis_y, 0],
            end=[t2_x, t2_y_top, 0],
            color=CRIMSON, stroke_width=1.5, dash_length=0.12,
        )
        self.play(Create(t2_line), run_time=0.4)

        # Dot on curve at t=T2
        t2_dot = Dot(point=[t2_x, sy(one_over_e), 0], radius=0.12, color=CRIMSON, fill_opacity=1)
        t2_dot.set_stroke(width=0, opacity=0)
        self.play(FadeIn(t2_dot), run_time=0.25)

        # T2 chip — placed right of T2 marker, in clear upper-right zone
        # sx(T2_us)=sx(1.0)=-5+1/4*10=-2.5; so chip at x=-1.5, y=2.0 (well above curve)
        t2_chip = LabelChip("T2 = 1 us", accent=CRIMSON, size=20)
        t2_chip.move_to([t2_x + 1.2, sy(one_over_e) + 0.6, 0])
        self.play(GrowFromCenter(t2_chip), run_time=0.4)

        # 1/e annotation chip in clear zone
        one_e_chip = LabelChip("1/e = 0.368", accent=TEAL, size=20)
        one_e_chip.move_to([3.5, sy(one_over_e), 0])
        self.play(GrowFromCenter(one_e_chip), run_time=0.4)

        # Dot at t=3 us for Gate A
        d3 = Dot(point=[sx(3.0), sy(np.exp(-3.0)), 0], radius=0.09, color=TEAL, fill_opacity=1)
        d3.set_stroke(width=0, opacity=0)
        self.play(FadeIn(d3), run_time=0.2)

        elapsed = (0.4 + 0.7 + 0.3 + 0.9 + 0.25 + 0.4 + 0.25 + 0.4 + 0.4 + 0.2)
        self.wait(max(0.5, dur - elapsed))
