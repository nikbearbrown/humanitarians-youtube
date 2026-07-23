"""vox_scenes.py — medhavy-vol2-uncertainty-squeeze/short (9:16 portrait)
Safe area: ±1.95x / ±3.4y
Layout: hyperbola on portrait axes.
  Axes: x_range=[0, 3.0], y_range=[0, 15.0], x_length=3.5, y_length=4.5
  Centered at ORIGIN + UP*0.3
  x-axis at scene y = 0.3 - 4.5/2 = -1.95
  Chips at y=-2.8 and y=-3.25
  Labels for A and B placed away from the hyperbola curve
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

_DEFAULTS = {"B03": 24.37}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))

def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)

def _c2p(ax, x, y):
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


class B03_UncertaintyRun(Scene):
    def construct(self):
        dur = _dur("B03")
        HALF_HBAR = 5.273  # display units

        def sp_disp(sx): return HALF_HBAR / sx

        header = _ink_text("Uncertainty  σ_x σ_p = ℏ/2", font_size=15, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        axes = Axes(
            x_range=[0, 3.0, 0.5],
            y_range=[0, 15.0, 5.0],
            x_length=3.5,
            y_length=4.5,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + UP * 0.3)

        self.play(Create(axes), run_time=0.6)

        xlbl = _ink_text("σ_x (nm)", font_size=12)
        xlbl.next_to(axes.x_axis, DOWN, buff=0.18)
        ylbl = _ink_text("σ_p", font_size=12)
        ylbl.move_to([-1.82, 0.3, 0])
        self.play(FadeIn(xlbl), FadeIn(ylbl), run_time=0.3)

        hyp_curve = axes.plot(lambda x: sp_disp(x), x_range=[0.36, 2.85],
                              color=TEAL, stroke_width=2.5)
        self.play(Create(hyp_curve), run_time=0.9)

        # State A at (1.0, 5.273) — TEAL
        A_pos = _c2p(axes, 1.0, sp_disp(1.0))
        dot_A = Dot(point=A_pos, radius=0.1, color=TEAL,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_A), run_time=0.3)

        A_x = float(A_pos[0]) if isinstance(A_pos, np.ndarray) else 0
        A_y = float(A_pos[1]) if isinstance(A_pos, np.ndarray) else 0
        # Place label to the right and above the dot, below the curve (curve goes up-left)
        lbl_A = _ink_text("A", font_size=13)
        lbl_A.move_to([A_x + 0.35, A_y + 0.3, 0])
        self.play(FadeIn(lbl_A), run_time=0.25)

        # State B at (0.5, 10.546) — CRIMSON
        B_pos = _c2p(axes, 0.5, sp_disp(0.5))
        dot_B = Dot(point=B_pos, radius=0.1, color=CRIMSON,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_B), run_time=0.3)

        B_x = float(B_pos[0]) if isinstance(B_pos, np.ndarray) else -0.5
        B_y = float(B_pos[1]) if isinstance(B_pos, np.ndarray) else 1
        lbl_B = _ink_text("B ×2", font_size=13)
        lbl_B.move_to([B_x + 0.4, B_y + 0.3, 0])
        self.play(FadeIn(lbl_B), run_time=0.25)

        # chips: x-axis at y≈-1.95; chips at y=-2.8 and y=-3.25
        hb_chip = LabelChip("σ_x σ_p=ℏ/2", accent=TEAL, size=16)
        hb_chip.move_to([0, -2.8, 0])
        self.play(GrowFromCenter(hb_chip), run_time=0.4)

        sq_chip = LabelChip("halve→double", accent=CRIMSON, size=16)
        sq_chip.move_to([0, -3.25, 0])
        self.play(GrowFromCenter(sq_chip), run_time=0.35)

        elapsed = 0.4 + 0.6 + 0.3 + 0.9 + 0.3 + 0.25 + 0.3 + 0.25 + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
