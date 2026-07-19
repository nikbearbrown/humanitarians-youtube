"""vox_scenes.py — medhavy-companion-tunneling
Reel: Quantum Tunneling — log(T) vs barrier width d
Palette: medhavy (colorblind-safe Okabe-Ito)

Physics: T = e^(-2*kappa*d), kappa = sqrt(2*m*(V0-E))/hbar
V0=1 eV, E=0.5 eV => kappa = 1.146 nm^-1
d range: 0 to 2 nm

Gate B placement:
  - Header at [1.5, 3.1, 0] (right of y-axis region, inside safe area)
  - Curve label at [2.8, 2.3, 0] (well above the curve at d=1.4 nm which is near y=-1)
  - Slope chip at [3.5, -2.2, 0] (below axes, no curves there)
  - Axis labels: x below axis, y at far left fixed coords
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
# B03_TunnelingRun — log(T) vs d for quantum tunneling
# =============================================================================
class B03_TunnelingRun(Scene):
    """Quantum tunneling: T = e^(-2*kappa*d)
    V0=1 eV, E=0.5 eV => kappa = 1.146 nm^-1
    Plot ln(T) vs d (nm), d in [0, 2]

    Linear on log scale: slope = -2*kappa = -2.292 per nm
    At d=0: ln(T) = 0 (T=1)
    At d=1: ln(T) = -2.292 (T=0.101)
    At d=2: ln(T) = -4.584 (T=0.010)

    Gate B: header before axes; curve label placed at fixed safe position;
    slope chip placed below axes in clear zone.
    """

    def construct(self):
        dur = _dur("B03")

        # Physics
        kappa = 1.146  # nm^-1
        # log(T) = -2*kappa*d; at d=2: log(T) = -4.584
        d_max = 2.0  # nm

        # Header FIRST (before axes) — safe at [1.5, 3.1, 0]
        header = _ink_text("Quantum Tunneling  T = e^(-2kd)", font_size=24, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes: x = d (nm) in [0, 2], y = ln(T) in [-5, 0.5]
        axes = Axes(
            x_range=[0, 2.0, 0.5],
            y_range=[-5.0, 0.5, 1.0],
            x_length=9.0,
            y_length=5.5,
            axis_config={
                "color": SLATE,
                "stroke_width": 1.5,
                "include_tip": False,
                "numbers_to_include": [],
            },
        ).move_to(ORIGIN + DOWN * 0.3)

        self.play(Create(axes), run_time=0.7)

        # Axis labels — placed AWAY from strokes
        # x-label below x-axis
        x_lbl = _ink_text("d  (nm)", font_size=20)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.35)
        # y-label at far left (fixed coord, no curves pass through x=-5.5)
        y_lbl = _ink_text("ln(T)", font_size=20)
        y_lbl.move_to([-5.4, 0.0, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)

        # Manual tick labels (to avoid numbers_to_include issues)
        # x-axis ticks at 0.5, 1.0, 1.5, 2.0
        x_ticks = [(0.5, "0.5"), (1.0, "1"), (1.5, "1.5"), (2.0, "2")]
        for xv, xl in x_ticks:
            pt = _c2p(axes, xv, 0)
            t = _ink_text(xl, font_size=14)
            t.move_to(pt + DOWN * 0.3)
            self.play(FadeIn(t), run_time=0.1)

        # y-axis ticks at -1,-2,-3,-4
        for yv in [-1, -2, -3, -4]:
            pt = _c2p(axes, 0, float(yv))
            t = _ink_text(str(yv), font_size=14)
            t.move_to(pt + LEFT * 0.4)
            self.play(FadeIn(t), run_time=0.1)

        # ln(T) = -2*kappa*d line (TEAL)
        log_T_curve = axes.plot(
            lambda d: -2 * kappa * d,
            x_range=[0, d_max],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(log_T_curve), run_time=1.0)

        # Dot at d=0 (T=1, ln(T)=0) — Gate A shape state
        d0_dot = Dot(
            point=_c2p(axes, 0, 0),
            radius=0.1, color=TEAL, fill_opacity=1,
        ).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d0_dot), run_time=0.3)

        # Annotation: T=1 at d=0
        # Place label at x OUTSIDE axes (to left of axis), NOT on the curve
        # The curve at d=0 is at ln(T)=0 which is at the x-axis level
        # Safe position: above and right of origin, where no curve passes
        t1_chip = LabelChip("T=1 at d=0", accent=TEAL, size=20)
        # Put it at scene coords left of y-axis, above x-axis
        t1_chip.move_to([-4.5, 1.5, 0])
        self.play(GrowFromCenter(t1_chip), run_time=0.4)

        # Dot at d=1 nm to mark it
        d1_dot = Dot(
            point=_c2p(axes, 1.0, -2 * kappa * 1.0),
            radius=0.1, color=CRIMSON, fill_opacity=1,
        ).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d1_dot), run_time=0.3)

        # Slope chip: slope = -2*kappa = -2.29/nm
        # Place at fixed scene coords inside safe area, right of center
        # The curve at d=2 is at ln(T)=-4.584 which maps to a low y in scene.
        # At x=3.5 (scene coord) no curve passes since axes end at d=2 nm
        # Use a position safely inside ±3.4 y: y=0.8 is in the upper-right clear zone
        slope_chip = LabelChip("slope = -2.29 /nm", accent=CRIMSON, size=20)
        slope_chip.move_to([3.5, 0.8, 0])
        self.play(GrowFromCenter(slope_chip), run_time=0.4)

        # Dot at d=2 for Gate A
        d2_dot = Dot(
            point=_c2p(axes, 2.0, -2 * kappa * 2.0),
            radius=0.1, color=TEAL, fill_opacity=1,
        ).set_stroke(width=0, opacity=0)
        self.play(FadeIn(d2_dot), run_time=0.3)

        # Elapsed
        elapsed = (0.4 + 0.7 + 0.4 + 4*0.1 + 4*0.1 + 1.0 + 0.3 + 0.4 + 0.3 + 0.4 + 0.3)
        self.wait(max(0.5, dur - elapsed))
