"""vox_scenes.py — medhavy-vol2-bloch-rotation
Reel: Bloch Sphere — Qubit States on the x-z Cross-Section
Palette: medhavy (Okabe-Ito)

Gate W: INK all Text; TEAL sphere circle + |↑⟩ arrow; CRIMSON |+⟩ arrow
Gate A: Two distinct arrow mobjects; Circle is distinct shape state
Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]
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

_DEFAULTS = {"B03": 18.0}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


class B03_BlochRun(Scene):
    """Bloch sphere cross-section (x-z plane) with |↑⟩, |+⟩, |↓⟩.
    Layout:
      Circle of radius R=2.2 centered at ORIGIN
      z-axis: vertical arrow from [-2.5] to [2.5]
      x-axis: horizontal arrow from [-2.5] to [2.5]
      State arrows: TEAL for |↑⟩ (north), CRIMSON for |+⟩ (equator)
      Labels at pole/equator positions
      Header at y=3.1
      Chips at y=-2.9 (well inside safe area, far from Circle boundary at y=-2.2)
    """

    def construct(self):
        dur = _dur("B03")

        R = 2.2  # sphere radius in scene units

        # header
        header = _ink_text("Bloch Sphere  x-z Cross-Section",
                           font_size=21, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Bloch sphere circle (SLATE stroke)
        bloch_circle = Circle(radius=R, color=SLATE, stroke_width=2.0)
        bloch_circle.move_to(ORIGIN)
        self.play(Create(bloch_circle), run_time=0.7)

        # z-axis (vertical)
        z_axis = Arrow(start=[0, -2.6, 0], end=[0, 2.8, 0],
                       color=SLATE, stroke_width=1.4, tip_length=0.2)
        x_axis = Arrow(start=[-2.6, 0, 0], end=[2.8, 0, 0],
                       color=SLATE, stroke_width=1.4, tip_length=0.2)
        zlbl = _ink_text("z", font_size=16)
        zlbl.move_to([0.25, 2.95, 0])
        xlbl = _ink_text("x", font_size=16)
        xlbl.move_to([2.95, 0.25, 0])
        self.play(Create(z_axis), Create(x_axis), run_time=0.5)
        self.play(FadeIn(zlbl), FadeIn(xlbl), run_time=0.25)

        # Pole and equator labels
        # North pole (0, R, 0) = |↑⟩
        north_lbl = _ink_text("|↑⟩", font_size=18)
        north_lbl.move_to([0.5, R + 0.25, 0])
        # South pole (0, -R, 0) = |↓⟩
        south_lbl = _ink_text("|↓⟩", font_size=18)
        south_lbl.move_to([0.5, -R - 0.25, 0])
        # Equator right (R, 0, 0) = |+⟩
        plus_lbl = _ink_text("|+⟩", font_size=18)
        plus_lbl.move_to([R + 0.4, 0.35, 0])
        # Equator left (-R, 0, 0) = |−⟩
        minus_lbl = _ink_text("|−⟩", font_size=18)
        minus_lbl.move_to([-R - 0.4, 0.35, 0])

        self.play(FadeIn(north_lbl), FadeIn(south_lbl), run_time=0.3)
        self.play(FadeIn(plus_lbl), FadeIn(minus_lbl), run_time=0.25)

        # TEAL arrow: |↑⟩ state — Bloch vector pointing to north pole
        up_arrow = Arrow(start=ORIGIN, end=[0, R * 0.92, 0],
                         color=TEAL, stroke_width=3.0, tip_length=0.25)
        self.play(Create(up_arrow), run_time=0.4)

        # Dot at north pole for Gate A shape state
        north_dot = Dot(point=[0, R, 0], radius=0.1, color=TEAL,
                        fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(north_dot), run_time=0.25)

        # Label for TEAL arrow: "θ=0, P(+)=1" — placed to the LEFT of the arrow, well above axes
        up_lbl = _ink_text("θ=0: P(+)=1", font_size=16)
        up_lbl.move_to([-2.0, 1.5, 0])
        self.play(FadeIn(up_lbl), run_time=0.3)

        # CRIMSON arrow: |+⟩ state — Bloch vector pointing to equator (right)
        plus_arrow = Arrow(start=ORIGIN, end=[R * 0.92, 0, 0],
                           color=CRIMSON, stroke_width=3.0, tip_length=0.25)
        self.play(Create(plus_arrow), run_time=0.4)

        # Dot at equator for Gate A
        equator_dot = Dot(point=[R, 0, 0], radius=0.1, color=CRIMSON,
                          fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(equator_dot), run_time=0.25)

        # Label for CRIMSON arrow: "θ=π/2, ⟨Z⟩=0"
        # Place below and left of equator, well below the circle boundary at y≈-1.5
        # and clear of the arrow stroke at y=0
        eq_lbl = _ink_text("θ=π/2: ⟨Z⟩=0", font_size=16)
        eq_lbl.move_to([1.6, -2.3, 0])
        self.play(FadeIn(eq_lbl), run_time=0.3)

        # chips — placed below y=-2.5 (well below circle boundary at y=-2.2)
        up_chip = LabelChip("θ=0 → P(+)=1", accent=TEAL, size=19)
        up_chip.move_to([-2.0, -2.9, 0])
        self.play(GrowFromCenter(up_chip), run_time=0.4)

        eq_chip = LabelChip("θ=π/2 → ⟨Z⟩=0", accent=CRIMSON, size=19)
        eq_chip.move_to([2.3, -2.9, 0])
        self.play(GrowFromCenter(eq_chip), run_time=0.35)

        elapsed = (0.4 + 0.7 + 0.5 + 0.25 + 0.3 + 0.25 +
                   0.4 + 0.25 + 0.3 + 0.4 + 0.25 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
