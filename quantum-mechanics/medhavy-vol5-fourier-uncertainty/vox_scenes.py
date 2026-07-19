"""vox_scenes.py — medhavy-vol5-fourier-uncertainty
Reel: Fourier Uncertainty — sigma_t*sigma_omega = 0.5 (minimum for Gaussian)
Palette: medhavy

Physics: Gaussian in time has Gaussian FT; product = 0.5 (minimum)
sigma_t=1 => sigma_omega=0.5 (normalized units)

Gate B: header before axes; chips in safe zones.
Two-panel layout: left = time domain, right = frequency domain.
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


class B03_FourierUncertaintyRun(Scene):
    """Two-panel: Gaussian pulse (time) and its FT (frequency).
    Normalized: sigma_t=1 => sigma_omega=0.5; product=0.5

    Left panel: Axes x in [-3,3] (multiples of sigma_t), y in [0,1.1]
    Right panel: Axes x in [-3,3] (multiples of sigma_omega), y in [0,1.1]
    Panels: left center at (-3.2, -0.2), right center at (3.2, -0.2)
    """

    def construct(self):
        dur = _dur("B03")
        sigma_t = 1.0   # normalized
        sigma_w = 0.5   # = 1/(2*sigma_t)

        # Panel dimensions
        pan_w, pan_h = 5.5, 4.0
        lx, rx = -3.2, 3.2
        cy = -0.2

        # Header FIRST
        header = _ink_text("Fourier Uncertainty: product=0.5", font_size=22, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # LEFT axes: time domain
        ax_L = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.1, 0.5],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([lx, cy, 0])

        # RIGHT axes: frequency domain
        ax_R = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.1, 0.5],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "numbers_to_include": []},
        ).move_to([rx, cy, 0])

        self.play(Create(ax_L), Create(ax_R), run_time=0.7)

        # Panel labels (axis titles) — placed ABOVE the axes, no curves
        x_axis_y = cy - pan_h/2  # = -2.2
        y_axis_x_L = lx - pan_w/2  # = -5.95 -- outside safe area!
        # Better: use fixed positions
        lbl_L = _ink_text("time  (sigma_t=1)", font_size=16)
        lbl_L.move_to([lx, cy + pan_h/2 + 0.22, 0])  # above left panel
        lbl_R = _ink_text("frequency  (sigma_w=0.5)", font_size=16)
        lbl_R.move_to([rx, cy + pan_h/2 + 0.22, 0])   # above right panel
        self.play(FadeIn(lbl_L), FadeIn(lbl_R), run_time=0.3)

        # Time-domain Gaussian (TEAL)
        gauss_t = ax_L.plot(
            lambda t: np.exp(-t**2 / (2 * sigma_t**2)),
            x_range=[-3, 3],
            color=TEAL, stroke_width=2.5
        )
        self.play(Create(gauss_t), run_time=0.7)

        # Dot at t=0 (peak) — Gate A shape state
        peak_L = Dot(point=_c2p(ax_L, 0, 1.0), radius=0.1, color=TEAL, fill_opacity=1)
        peak_L.set_stroke(width=0, opacity=0)
        self.play(FadeIn(peak_L), run_time=0.25)

        # sigma_t marker: dashed vertical line at t=sigma_t=1
        t_axis_y_bottom = cy - pan_h/2
        t1_pt_top = _c2p(ax_L, sigma_t, np.exp(-0.5))
        t1_pt_bot = _c2p(ax_L, sigma_t, 0)
        t1_line = DashedLine(start=t1_pt_bot, end=t1_pt_top,
                             color=TEAL, stroke_width=1.5, dash_length=0.1)
        self.play(Create(t1_line), run_time=0.3)

        # FT Gaussian (CRIMSON) on right panel
        # F(omega) = exp(-omega^2/(2*sigma_w^2)) -- normalized so sigma_w=0.5
        # x_range for ax_R is [-3,3] but these are in units of sigma_w
        # So physical omega = x * sigma_w; F(omega) = exp(-omega^2/(2*sigma_w^2)) = exp(-x^2/2)
        # But we want to show the width IS sigma_w; plot vs omega (not normalized)
        # ax_R x-range is [-3,3] in "omega/sigma_w" units... let's just plot
        gauss_w = ax_R.plot(
            lambda om: np.exp(-om**2 / (2 * sigma_w**2)),
            x_range=[-3, 3],
            color=CRIMSON, stroke_width=2.5
        )
        self.play(Create(gauss_w), run_time=0.7)

        # Dot at omega=0 (peak of FT) — Gate A shape state
        peak_R = Dot(point=_c2p(ax_R, 0, 1.0), radius=0.1, color=CRIMSON, fill_opacity=1)
        peak_R.set_stroke(width=0, opacity=0)
        self.play(FadeIn(peak_R), run_time=0.25)

        # Product chip — center bottom, safe zone
        prod_chip = LabelChip("product = 0.5 (minimum)", accent=TEAL, size=20)
        prod_chip.move_to([0.0, -3.1, 0])
        self.play(GrowFromCenter(prod_chip), run_time=0.4)

        # Dot at t=-1 for Gate A
        dot_t1 = Dot(point=_c2p(ax_L, -sigma_t, np.exp(-0.5)), radius=0.09, color=TEAL, fill_opacity=1)
        dot_t1.set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_t1), run_time=0.2)

        elapsed = (0.4 + 0.7 + 0.3 + 0.7 + 0.25 + 0.3 + 0.7 + 0.25 + 0.4 + 0.2)
        self.wait(max(0.5, dur - elapsed))
