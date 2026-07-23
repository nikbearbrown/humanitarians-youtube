"""vox_scenes.py — medhavy-vol4-gate-bloch
Reel: Quantum Gates — Hadamard and S gate on the Bloch sphere
Palette: medhavy (colorblind-safe Okabe-Ito)

Physics:
  H|0> = |+>   (north pole to equator)
  S|+> = |i>   (equator, 90 degree rotation in phi)
  H*H  = I     (Hadamard is self-inverse)

Scene: 2D Bloch circle (cross-section view)
  - Circle representing the equatorial plane (top-down view for the H rotation)
  - Arrows showing state positions: |0>, |+>, |i>
  - Arc arrows showing rotations

Gate B placement:
  - Header at [1.5, 3.1, 0] (right of y-axis, inside safe area)
  - State labels offset from arrow tips, clear of arcs
  - Gate chips: placed in lower safe zone
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


# =============================================================================
# B03_GateBlochRun — Quantum gates on Bloch sphere (2D schematic)
# =============================================================================
class B03_GateBlochRun(Scene):
    """Bloch sphere gate visualization.

    Layout: Two panels side by side.
    Left panel: vertical cross-section (xz plane) showing H gate: |0> north -> |+> equator
    Right panel: horizontal cross-section (xy plane) showing S gate: |+> -> |i> (90 deg rotation)

    All labels placed at computed safe positions, not on curves.
    """

    def construct(self):
        dur = _dur("B03")
        R = 1.8   # sphere radius in scene units

        # Header first (before any circles)
        header = _ink_text("Quantum Gates: H and S", font_size=26, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── LEFT PANEL: xz plane (H gate: |0> pole -> |+> equator) ──────────
        # Center at (-3.2, 0, 0)
        lx, ly = -3.2, 0.0

        # Bloch circle (xz cross-section) — SLATE
        bloch_circle_L = Circle(radius=R, color=SLATE, stroke_width=1.5,
                                fill_opacity=0).move_to([lx, ly, 0])
        self.play(Create(bloch_circle_L), run_time=0.5)

        # Axes inside circle (SLATE thin)
        z_axis_L = Line(start=[lx, ly-R-0.2, 0], end=[lx, ly+R+0.2, 0],
                        stroke_width=1.0, color=SLATE)
        x_axis_L = Line(start=[lx-R-0.2, ly, 0], end=[lx+R+0.2, ly, 0],
                        stroke_width=1.0, color=SLATE)
        self.play(FadeIn(z_axis_L), FadeIn(x_axis_L), run_time=0.3)

        # State |0> at north pole (top of circle)
        state0 = Dot(point=[lx, ly+R, 0], radius=0.14, color=TEAL, fill_opacity=1)
        state0.set_stroke(width=0, opacity=0)
        lbl0 = _ink_text("|0>", font_size=18)
        lbl0.move_to([lx + 0.35, ly+R + 0.2, 0])
        self.play(FadeIn(state0), FadeIn(lbl0), run_time=0.3)

        # Arrow from |0> toward |+> (the H gate: pole to equator right)
        # |+> is at (R, 0) in the xz plane → (lx+R, ly, 0) in scene
        h_arrow = Arrow(
            start=[lx, ly+R, 0],
            end=[lx+R*0.85, ly+0.1, 0],  # slightly inside to avoid circle overlap
            buff=0,
            color=TEAL,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(Create(h_arrow), run_time=0.6)

        # State |+> at equator right
        state_plus = Dot(point=[lx+R, ly, 0], radius=0.14, color=TEAL, fill_opacity=1)
        state_plus.set_stroke(width=0, opacity=0)
        lbl_plus = _ink_text("|+>", font_size=18)
        lbl_plus.move_to([lx+R+0.32, ly + 0.22, 0])
        self.play(FadeIn(state_plus), FadeIn(lbl_plus), run_time=0.3)

        # H gate chip — placed below left panel, clear of all strokes
        h_chip = LabelChip("H gate", accent=TEAL, size=20)
        h_chip.move_to([lx, ly - R - 0.55, 0])
        self.play(GrowFromCenter(h_chip), run_time=0.4)

        # Label: left panel title
        left_title = _ink_text("xz plane", font_size=14)
        left_title.move_to([lx, ly - R - 0.22, 0])
        self.play(FadeIn(left_title), run_time=0.2)

        # ── RIGHT PANEL: xy plane (S gate: |+> -> |i> 90 deg rotation) ──────
        rx, ry = 3.2, 0.0

        bloch_circle_R = Circle(radius=R, color=SLATE, stroke_width=1.5,
                                fill_opacity=0).move_to([rx, ry, 0])
        self.play(Create(bloch_circle_R), run_time=0.4)

        x_axis_R = Line(start=[rx-R-0.2, ry, 0], end=[rx+R+0.2, ry, 0],
                        stroke_width=1.0, color=SLATE)
        y_axis_R = Line(start=[rx, ry-R-0.2, 0], end=[rx, ry+R+0.2, 0],
                        stroke_width=1.0, color=SLATE)
        self.play(FadeIn(x_axis_R), FadeIn(y_axis_R), run_time=0.3)

        # State |+> at x-axis (phi=0 equator)
        state_plus_R = Dot(point=[rx+R, ry, 0], radius=0.14, color=TEAL, fill_opacity=1)
        state_plus_R.set_stroke(width=0, opacity=0)
        lbl_plus_R = _ink_text("|+>", font_size=18)
        lbl_plus_R.move_to([rx+R+0.32, ry - 0.22, 0])
        self.play(FadeIn(state_plus_R), FadeIn(lbl_plus_R), run_time=0.3)

        # S gate arc: from |+> (x-axis, angle 0) to |i> (y-axis, angle 90)
        # Arc in xy plane, going counterclockwise
        s_arc = Arc(
            radius=R * 0.7,
            start_angle=0,
            angle=np.pi/2,
            arc_center=[rx, ry, 0],
            color=CRIMSON,
            stroke_width=2.5,
        )
        self.play(Create(s_arc), run_time=0.5)

        # State |i> at y-axis (phi=pi/2)
        state_i = Dot(point=[rx, ry+R, 0], radius=0.14, color=TEAL, fill_opacity=1)
        state_i.set_stroke(width=0, opacity=0)
        lbl_i = _ink_text("|i>", font_size=18)
        lbl_i.move_to([rx - 0.38, ry+R+0.22, 0])
        self.play(FadeIn(state_i), FadeIn(lbl_i), run_time=0.3)

        # S gate chip below right panel
        s_chip = LabelChip("S gate (90 deg)", accent=CRIMSON, size=20)
        s_chip.move_to([rx, ry - R - 0.55, 0])
        self.play(GrowFromCenter(s_chip), run_time=0.4)

        right_title = _ink_text("xy plane", font_size=14)
        right_title.move_to([rx, ry - R - 0.22, 0])
        self.play(FadeIn(right_title), run_time=0.2)

        # H*H = I chip in center (between panels), safe zone at y=2.3
        hh_chip = LabelChip("H*H = I", accent=TEAL, size=20)
        hh_chip.move_to([0.0, 2.4, 0])
        self.play(GrowFromCenter(hh_chip), run_time=0.4)

        elapsed = (0.4 + 0.5 + 0.3 + 0.3 + 0.3 + 0.6 + 0.3 + 0.4 + 0.2 +
                   0.4 + 0.3 + 0.3 + 0.5 + 0.3 + 0.4 + 0.2 + 0.4)
        self.wait(max(0.5, dur - elapsed))
