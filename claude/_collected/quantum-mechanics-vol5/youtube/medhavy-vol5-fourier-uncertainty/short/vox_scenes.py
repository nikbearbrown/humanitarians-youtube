"""vox_scenes.py — medhavy-vol5-fourier-uncertainty/short (9:16 portrait)
Reel: Fourier Uncertainty — sigma_t * sigma_omega = 0.5
Palette: medhavy (Okabe-Ito)

Physics:
  Gaussian in time: f(t) = exp(-t²/2), sigma_t = 1
  FT: F(w) = exp(-w²/2/sigma_w²), sigma_w = 0.5
  Product: sigma_t * sigma_w = 0.5 (minimum)

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Two panels stacked:
    Upper panel (time): center at (0, 1.8); x_range=[-3,3], y_range=[0,1.1]
                        x_length=3.2, y_length=2.0
    Lower panel (freq): center at (0, -0.8); x_range=[-3,3], y_range=[0,1.1]
                        x_length=3.2, y_length=2.0

  Upper panel: sx_u(t) = -1.6 + (t+3)/6*3.2; sy_u(y) = 1.8-1.0 + y/1.1*2.0
  Lower panel: sx_l = sx_u (same width); sy_l(y) = -0.8-1.0 + y/1.1*2.0

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

sigma_t = 1.0
sigma_w = 0.5


class B03_FourierUncertaintyRun(Scene):
    """Portrait two-panel Gaussian uncertainty plot.

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Panel dimensions
        pan_w, pan_h = 3.2, 2.0
        x_rng_min, x_rng_max = -3.0, 3.0
        y_rng_min, y_rng_max = 0.0, 1.1

        # Upper panel: time; center (0, 1.8)
        ucy = 1.8
        def sx(xv):
            return -pan_w / 2 + (xv - x_rng_min) / (x_rng_max - x_rng_min) * pan_w
        def sy_u(yv):
            return ucy - pan_h / 2 + (yv - y_rng_min) / (y_rng_max - y_rng_min) * pan_h

        # Lower panel: freq; center (0, -0.8)
        lcy = -0.8
        def sy_l(yv):
            return lcy - pan_h / 2 + (yv - y_rng_min) / (y_rng_max - y_rng_min) * pan_h

        # Header: at top, safe
        header = _ink_text("Fourier Uncertainty", font_size=16, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Panel titles: place BELOW each panel axis to avoid header and product overlaps
        # Upper panel x-axis bottom: ucy - pan_h/2 = 0.8; title below at 0.60
        # Lower panel x-axis bottom: lcy - pan_h/2 = -1.8; title below at -2.0
        t_lbl = _ink_text("time: sigma=1", font_size=12)
        t_lbl.move_to([0, ucy - pan_h / 2 - 0.22, 0])  # = 0.8 - 0.22 = 0.58
        w_lbl = _ink_text("freq: sigma=0.5", font_size=12)
        w_lbl.move_to([0, lcy - pan_h / 2 - 0.22, 0])  # = -1.8 - 0.22 = -2.02
        self.play(FadeIn(t_lbl), FadeIn(w_lbl), run_time=0.3)

        # Upper axes (time domain)
        ax_u = Axes(
            x_range=[x_rng_min, x_rng_max, 1],
            y_range=[y_rng_min, y_rng_max, 0.5],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        ax_u.move_to([0, ucy, 0])

        # Lower axes (freq domain)
        ax_l = Axes(
            x_range=[x_rng_min, x_rng_max, 1],
            y_range=[y_rng_min, y_rng_max, 0.5],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        ax_l.move_to([0, lcy, 0])

        self.play(Create(ax_u), Create(ax_l), run_time=0.6)

        # TEAL: time-domain Gaussian
        gauss_t = ax_u.plot(
            lambda t: np.exp(-t**2 / (2 * sigma_t**2)),
            x_range=[x_rng_min, x_rng_max],
            color=TEAL, stroke_width=2.5
        )
        self.play(Create(gauss_t), run_time=0.6)

        # Dot at t=0 peak
        d_t = Dot(point=[sx(0), sy_u(1.0), 0], radius=0.09, color=TEAL,
                  fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d_t), run_time=0.2)

        # CRIMSON: frequency-domain Gaussian
        gauss_w = ax_l.plot(
            lambda om: np.exp(-om**2 / (2 * sigma_w**2)),
            x_range=[x_rng_min, x_rng_max],
            color=CRIMSON, stroke_width=2.5
        )
        self.play(Create(gauss_w), run_time=0.6)

        # Dot at omega=0 peak
        d_w = Dot(point=[sx(0), sy_l(1.0), 0], radius=0.09, color=CRIMSON,
                  fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d_w), run_time=0.2)

        # (product annotation handled by chips below)

        # --- Chips ---
        t_chip = LabelChip("sigma_t = 1", accent=TEAL, size=16)
        t_chip.move_to([-0.55, -2.65, 0])
        self.play(GrowFromCenter(t_chip), run_time=0.4)

        w_chip = LabelChip("product = 0.5 min", accent=CRIMSON, size=16)
        w_chip.move_to([0.60, -3.08, 0])
        self.play(GrowFromCenter(w_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.6 + 0.6 + 0.2 + 0.6 + 0.2 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
