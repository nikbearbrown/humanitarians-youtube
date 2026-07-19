"""vox_scenes.py — medhavy-companion-tunneling/short (9:16 portrait)
Reel: Quantum Tunneling — log(T) vs barrier width d
Palette: medhavy (Okabe-Ito)

Physics:
  T = exp(-2*kappa*d),  kappa = sqrt(2*m*(V0-E))/hbar
  V0=1 eV, E=0.5 eV => kappa = 1.146 nm^-1
  d in [0, 2] nm
  ln(T) = -2*kappa*d: linear in d, slope = -2.292 per nm
  At d=0: T=1, ln(T)=0; At d=1: ln(T)=-2.292; At d=2: ln(T)=-4.584

Portrait layout:
  Safe area: +-1.95x / +-3.4y
  Single panel: center (0, 0.0); x_range=[0,2] (d in nm), y_range=[-5,0.5]
                x_length=3.0, y_length=4.8

  sx(dv) = -1.5 + dv / 2 * 3.0
  sy(lv) = 0.0 - 2.4 + (lv + 5) / 5.5 * 4.8

  Header at y=3.15; subtitle at y=2.80
  x-label below panel at y=-2.72 (above chips)
  Chips at y=-3.00 and y=-3.38
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

_DEFAULTS = {"B03": 24.84}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)

# Physics
kappa = 1.146  # nm^-1
d_max = 2.0    # nm
def log_T(d_nm: float) -> float:
    return -2 * kappa * d_nm

# Panel geometry
pan_w = 3.0
pan_h = 4.8
cx, cy_pan = 0.0, 0.0
d_min_ax, d_max_ax = 0.0, 2.0
lT_min, lT_max = -5.0, 0.5

def sx(dv: float) -> float:
    return cx - pan_w / 2 + (dv - d_min_ax) / (d_max_ax - d_min_ax) * pan_w

def sy(lv: float) -> float:
    return cy_pan - pan_h / 2 + (lv - lT_min) / (lT_max - lT_min) * pan_h

x_axis_y = sy(0)       # where ln(T)=0 maps in scene
y_axis_x = sx(0)       # left edge = cx - pan_w/2 = -1.5


class B03_TunnelingRun(Scene):
    """Portrait log(T) vs d plot for quantum tunneling.

    All label positions via sx()/sy() pure-float helpers (Gate A safe).
    No c2p() arithmetic.
    """

    def construct(self):
        dur = _dur("B03")

        # Header
        header = _ink_text("Quantum Tunneling", font_size=14, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Subtitle
        sub = _ink_text("T = exp(-2 kappa d)", font_size=11)
        sub.move_to([0, 2.82, 0])
        self.play(FadeIn(sub), run_time=0.3)

        # Axes
        ax = Axes(
            x_range=[d_min_ax, d_max_ax, 0.5],
            y_range=[lT_min, lT_max, 1.0],
            x_length=pan_w,
            y_length=pan_h,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        ax.move_to([cx, cy_pan, 0])
        self.play(Create(ax), run_time=0.6)

        # x-axis label: placed below panel, above chips zone
        # Panel bottom: cy_pan - pan_h/2 = -2.4; label below at -2.57
        x_lbl = _ink_text("d  (nm)", font_size=11)
        x_lbl.move_to([cx, cy_pan - pan_h / 2 - 0.20, 0])  # = -2.60
        self.play(FadeIn(x_lbl), run_time=0.25)

        # y-axis label: rotated text risks overlap; use short fixed text left of axis
        # y_axis_x = -1.5; safe area edge is -1.95; use x=-1.82
        y_lbl = _ink_text("ln(T)", font_size=11)
        y_lbl.move_to([-1.82, cy_pan + 0.5, 0])  # y=0.5 well above x-axis at sy(0)
        self.play(FadeIn(y_lbl), run_time=0.2)

        # y-tick labels at ln(T) = -1, -2, -3, -4
        # Place at x = y_axis_x - 0.22 = -1.72
        for lv in [-1.0, -2.0, -3.0, -4.0]:
            t = _ink_text(str(int(lv)), font_size=9)
            t.move_to([y_axis_x - 0.22, sy(lv), 0])
            self.add(t)

        # x-tick labels at d = 1.0, 2.0
        for dv, dl in [(1.0, "1"), (2.0, "2")]:
            t = _ink_text(dl, font_size=9)
            t.move_to([sx(dv), x_axis_y - 0.20, 0])
            self.add(t)

        # TEAL: ln(T) = -2*kappa*d line
        log_T_curve = ax.plot(
            lambda dv: -2 * kappa * dv,
            x_range=[d_min_ax, d_max_ax],
            color=TEAL, stroke_width=2.5
        )
        self.play(Create(log_T_curve), run_time=0.9)

        # Dot at d=0, ln(T)=0 (T=1)
        d0_dot = Dot(point=[sx(0), sy(0), 0], radius=0.09, color=TEAL,
                     fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d0_dot), run_time=0.25)

        # Label "T=1 at d=0" — place RIGHT of d=0 dot in blank space
        # The curve goes down-right from (sx(0), sy(0)) = (-1.5, x_axis_y)
        # Upper-right of d=0 is blank; x=-0.9, y=sy(0)+0.35 (above x-axis)
        t1_lbl = _ink_text("T=1 at d=0", font_size=10)
        t1_lbl.move_to([-0.65, sy(0) + 0.38, 0])
        self.play(FadeIn(t1_lbl), run_time=0.2)

        # CRIMSON dot at d=1 nm
        d1_dot = Dot(point=[sx(1.0), sy(log_T(1.0)), 0], radius=0.09, color=CRIMSON,
                     fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d1_dot), run_time=0.25)

        # Chips
        # sy(0) = 0.0 - 2.4 + (0+5)/5.5*4.8 = -2.4 + 4.3636 = 1.9636
        # x_axis_y = sy(0) = 1.9636
        # chips at y=-3.00 and y=-3.38 (in absolute scene coordinates)
        slope_chip = LabelChip("slope = -2.29 /nm", accent=CRIMSON, size=14)
        slope_chip.move_to([0.10, -2.78, 0])
        self.play(GrowFromCenter(slope_chip), run_time=0.4)

        t0_chip = LabelChip("T=1 at d=0  (no barrier)", accent=TEAL, size=13)
        t0_chip.move_to([-0.05, -3.20, 0])
        self.play(GrowFromCenter(t0_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.6 + 0.25 + 0.2
                   + 0.9 + 0.25 + 0.2 + 0.25
                   + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
