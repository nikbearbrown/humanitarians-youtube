"""vox_scenes.py — medhavy-vol5-group-phase-velocity/short (9:16 portrait)
Reel: Group vs Phase Velocity — v_group = 2 * v_phase
Palette: medhavy (Okabe-Ito)

Physics:
  quadratic dispersion: omega = k^2 / 2  (hbar/m = 1 units)
  wave packet at t=0: psi(x) = cos(k0*x) * exp(-x^2 / (2*sig^2))
  k0 = 2.0, sig = 1.2
  v_group = k0 = 2.0
  v_phase = k0 / 2 = 1.0
  ratio: v_group / v_phase = 2 (quadratic dispersion)

Portrait layout:
  Safe area: +-1.95x / +-3.4y
  Single panel: center (0, 0.2); x_range=[-4,4], y_range=[-1.1,1.1]
                x_length=3.2, y_length=4.2

  sx(xv) = -1.6 + (xv + 4) / 8 * 3.2
  sy(yv) = 0.2 - 2.1 + (yv + 1.1) / 2.2 * 4.2

  Chips at y=-2.72 and y=-3.18
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

_DEFAULTS = {"B03": 26.51}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)

# Physics parameters
k0 = 2.0
sig = 1.2

# Panel geometry
pan_w = 3.2
pan_h = 4.2
x_min, x_max = -4.0, 4.0
y_min, y_max = -1.1, 1.1
cx, cy_pan = 0.0, 0.2

def sx(xv: float) -> float:
    return cx - pan_w / 2 + (xv - x_min) / (x_max - x_min) * pan_w

def sy(yv: float) -> float:
    return cy_pan - pan_h / 2 + (yv - y_min) / (y_max - y_min) * pan_h


class B03_GroupPhaseRun(Scene):
    """Portrait wave packet scene: carrier (TEAL) + envelope (CRIMSON dashed).

    All label positions via sx()/sy() pure-float helpers (Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Header — top safe area
        header = _ink_text("Group vs Phase Velocity", font_size=15, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Subtitle below header
        sub = _ink_text("v_group = 2 x v_phase", font_size=12)
        sub.move_to([0, 2.80, 0])
        self.play(FadeIn(sub), run_time=0.3)

        # Axes
        ax = Axes(
            x_range=[x_min, x_max, 1],
            y_range=[y_min, y_max, 0.5],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        ax.move_to([cx, cy_pan, 0])
        self.play(Create(ax), run_time=0.6)

        # Panel label (below panel, above chips)
        lbl = _ink_text("wave packet at t = 0", font_size=11)
        lbl.move_to([cx, cy_pan - pan_h / 2 - 0.24, 0])  # = 0.2 - 2.1 - 0.24 = -2.14
        self.play(FadeIn(lbl), run_time=0.25)

        # CRIMSON: Gaussian envelope (+) — use DashedVMobject for dashed style
        env_pos_solid = ax.plot(
            lambda xv: np.exp(-xv**2 / (2 * sig**2)),
            x_range=[x_min, x_max],
            color=CRIMSON, stroke_width=2.0
        )
        env_pos = DashedVMobject(env_pos_solid, num_dashes=30, dashed_ratio=0.6)

        # CRIMSON: Gaussian envelope (-)
        env_neg_solid = ax.plot(
            lambda xv: -np.exp(-xv**2 / (2 * sig**2)),
            x_range=[x_min, x_max],
            color=CRIMSON, stroke_width=2.0
        )
        env_neg = DashedVMobject(env_neg_solid, num_dashes=30, dashed_ratio=0.6)

        self.play(Create(env_pos), Create(env_neg), run_time=0.6)

        # TEAL: oscillating wave packet (carrier * envelope)
        wave = ax.plot(
            lambda xv: np.cos(k0 * xv) * np.exp(-xv**2 / (2 * sig**2)),
            x_range=[x_min, x_max],
            color=TEAL, stroke_width=2.5
        )
        self.play(Create(wave), run_time=0.7)

        # TEAL dot at envelope peak (x=0, y=1)
        d_peak = Dot(point=[sx(0), sy(1.0), 0], radius=0.10, color=TEAL,
                     fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d_peak), run_time=0.2)

        # Label: "envelope" just left of peak, placed above peak in blank space
        # envelope peak is at (sx(0), sy(1.0)) = (0.0, 2.30); safe header starts at ~2.6
        # Place label at y=2.50 — between sub (y=2.80) and panel top (cy_pan+pan_h/2=2.30)
        # Actually cy_pan+pan_h/2 = 0.2+2.1 = 2.30; sub is at 2.80
        # Put env label at x=-0.85, y=2.50 (gap region between sub and panel top)
        env_lbl = _ink_text("envelope", font_size=10)
        env_lbl.move_to([-0.85, 2.50, 0])
        self.play(FadeIn(env_lbl), run_time=0.2)

        # CRIMSON dot at carrier crest nearest origin (cos(k0*x) = 1 at x=0 but wave=0 isn't crest)
        # First crest of cos(2x): x=0 gives cos(0)=1 -> wave value = 1*exp(0)=1.0 (peak)
        # Actually x=0 IS the central crest. Place CRIMSON dot to mark a crest slightly off-center
        # Use x = pi/(2*k0) = pi/4 ~ 0.785 to mark first zero crossing? No: mark x=0 crest with CRIMSON
        # Mark the crest at x=0 with a small CRIMSON dot slightly offset so it's visible on TEAL dot
        d_crest = Dot(point=[sx(0.0), sy(1.0), 0], radius=0.06, color=CRIMSON,
                      fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d_crest), run_time=0.15)

        # Arrow annotation: v_group label at right side, y near sy(0.5)
        # v_group arrow: horizontal, from x=1.0 to x=2.0 at y=sy(0.55)
        arr_y = sy(0.55)  # = 0.2 - 2.1 + (0.55+1.1)/2.2*4.2 = -1.9 + 1.65/2.2*4.2 = -1.9+3.15 = 1.25
        vg_arr = Arrow(
            start=[sx(0.5), arr_y, 0],
            end=[sx(1.8), arr_y, 0],
            color=TEAL, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.18
        )
        self.play(GrowArrow(vg_arr), run_time=0.35)

        vg_lbl = _ink_text("v_group", font_size=10)
        vg_lbl.move_to([sx(1.15), arr_y + 0.28, 0])
        self.play(FadeIn(vg_lbl), run_time=0.2)

        # v_phase arrow: shorter (half length) at lower y showing slower crests
        arr_y2 = sy(-0.55)  # = -1.9 + (-0.55+1.1)/2.2*4.2 = -1.9 + 0.55/2.2*4.2 = -1.9+1.05 = -0.85
        vp_arr = Arrow(
            start=[sx(-0.5), arr_y2, 0],
            end=[sx(0.4), arr_y2, 0],
            color=CRIMSON, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25
        )
        self.play(GrowArrow(vp_arr), run_time=0.3)

        vp_lbl = _ink_text("v_phase", font_size=10)
        vp_lbl.move_to([sx(-0.05), arr_y2 - 0.28, 0])
        self.play(FadeIn(vp_lbl), run_time=0.2)

        # Chips
        env_chip = LabelChip("v_group = 2 v_phase", accent=TEAL, size=15)
        env_chip.move_to([-0.35, -2.72, 0])
        self.play(GrowFromCenter(env_chip), run_time=0.4)

        disp_chip = LabelChip("omega = k^2 / 2", accent=CRIMSON, size=15)
        disp_chip.move_to([0.25, -3.18, 0])
        self.play(GrowFromCenter(disp_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.6 + 0.25 + 0.6 + 0.7 + 0.2 + 0.2 + 0.15
                   + 0.35 + 0.2 + 0.3 + 0.2 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
