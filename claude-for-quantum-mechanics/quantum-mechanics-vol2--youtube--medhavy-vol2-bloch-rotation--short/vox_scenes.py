"""vox_scenes.py — medhavy-vol2-bloch-rotation/short (9:16 portrait)
Safe area: ±1.95x / ±3.4y
Layout: Bloch sphere circle, radius R=1.6, centered at ORIGIN+UP*0.2
  Circle bottom at y = 0.2 - 1.6 = -1.4 (well within safe area)
  Chips at y=-2.7 and y=-3.15
  Labels for states placed at safe positions clear of circle strokes
  Arrow labels placed near origin area (no circle stroke there)
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

_DEFAULTS = {"B03": 27.35}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


class B03_BlochRun(Scene):
    """Portrait Bloch sphere cross-section."""

    def construct(self):
        dur = _dur("B03")
        R = 1.6  # sphere radius

        # header
        header = _ink_text("Bloch Sphere", font_size=17, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Circle centered at (0, 0.2)
        cx, cy = 0, 0.2
        bloch_circle = Circle(radius=R, color=SLATE, stroke_width=2.0)
        bloch_circle.move_to([cx, cy, 0])
        self.play(Create(bloch_circle), run_time=0.6)

        # axes
        z_axis = Arrow(start=[cx, cy - 1.9, 0], end=[cx, cy + 2.1, 0],
                       color=SLATE, stroke_width=1.2, tip_length=0.18)
        x_axis = Arrow(start=[cx - 1.9, cy, 0], end=[cx + 2.1, cy, 0],
                       color=SLATE, stroke_width=1.2, tip_length=0.18)
        zlbl = _ink_text("z", font_size=13)
        zlbl.move_to([cx + 0.22, cy + 2.25, 0])
        xlbl = _ink_text("x", font_size=13)
        xlbl.move_to([cx + 2.25, cy + 0.2, 0])
        self.play(Create(z_axis), Create(x_axis), run_time=0.4)
        self.play(FadeIn(zlbl), FadeIn(xlbl), run_time=0.2)

        # State labels (placed just outside circle radius)
        north_lbl = _ink_text("|↑⟩", font_size=15)
        north_lbl.move_to([cx + 0.4, cy + R + 0.22, 0])
        south_lbl = _ink_text("|↓⟩", font_size=15)
        south_lbl.move_to([cx + 0.4, cy - R - 0.22, 0])
        plus_lbl = _ink_text("|+⟩", font_size=14)
        plus_lbl.move_to([cx + R + 0.25, cy + 0.28, 0])
        self.play(FadeIn(north_lbl), FadeIn(south_lbl), FadeIn(plus_lbl), run_time=0.3)

        # TEAL arrow: |↑⟩ (north)
        up_arrow = Arrow(start=[cx, cy, 0], end=[cx, cy + R * 0.9, 0],
                         color=TEAL, stroke_width=2.5, tip_length=0.22)
        self.play(Create(up_arrow), run_time=0.4)
        north_dot = Dot(point=[cx, cy + R, 0], radius=0.09, color=TEAL,
                        fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(north_dot), run_time=0.22)

        # Label for |↑⟩ placed well inside circle, lower (clear of circle stroke)
        # Circle at x=-0.7 has y = cy + √(R²-0.7²) = 0.2+√(2.56-0.49) = 0.2+1.44 = 1.64
        # Place at y=0.9 (well below circle boundary at that x, inside the sphere)
        up_lbl = _ink_text("θ=0: P=1", font_size=12)
        up_lbl.move_to([cx - 0.7, cy + 0.7, 0])
        self.play(FadeIn(up_lbl), run_time=0.25)

        # CRIMSON arrow: |+⟩ (equator)
        plus_arrow = Arrow(start=[cx, cy, 0], end=[cx + R * 0.9, cy, 0],
                           color=CRIMSON, stroke_width=2.5, tip_length=0.22)
        self.play(Create(plus_arrow), run_time=0.4)
        equator_dot = Dot(point=[cx + R, cy, 0], radius=0.09, color=CRIMSON,
                          fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(equator_dot), run_time=0.22)

        # Label for |+⟩: placed BELOW the arrow, well below circle boundary
        # Circle bottom at y = cy - R = 0.2 - 1.6 = -1.4
        # Place label at y = -1.95 (below circle, within safe area, no circle stroke there)
        eq_lbl = _ink_text("θ=π/2: ⟨Z⟩=0", font_size=12)
        eq_lbl.move_to([cx + 0.5, -2.05, 0])
        self.play(FadeIn(eq_lbl), run_time=0.25)

        # chips at y=-2.7 and y=-3.15
        up_chip = LabelChip("θ=0→P(+)=1", accent=TEAL, size=16)
        up_chip.move_to([0, -2.7, 0])
        self.play(GrowFromCenter(up_chip), run_time=0.4)

        eq_chip = LabelChip("θ=π/2→⟨Z⟩=0", accent=CRIMSON, size=16)
        eq_chip.move_to([0, -3.15, 0])
        self.play(GrowFromCenter(eq_chip), run_time=0.35)

        elapsed = 0.4 + 0.6 + 0.4 + 0.2 + 0.3 + 0.4 + 0.22 + 0.25 + 0.4 + 0.22 + 0.25 + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
