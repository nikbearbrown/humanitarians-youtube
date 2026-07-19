"""vox_scenes.py — medhavy-vol4-decoherence-t2/short (9:16 portrait)
Reel: Qubit Decoherence — T2 Exponential Decay
Palette: medhavy (Okabe-Ito)

Physics:
  rho_01(t) = e^(−t/T2); T2 = 1 us
  At t=T2: |rho_01| = 1/e ≈ 0.3679
  At t=3T2: |rho_01| ≈ 0.050

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Axes center: (0, 0.1); x_range=[0,4], y_range=[0,1.1]
  x_length=3.2, y_length=4.0
  x_scale = 3.2/4 = 0.8 u/us; y_scale = 4.0/1.1 ≈ 3.636 u/unit

  sx(t) = -1.6 + t/4 * 3.2
  sy(r) = 0.1 - 2.0 + r/1.1 * 4.0 = -1.9 + r*3.636

  Key points:
    t=1 (T2): sx = -1.6 + 0.8 = -0.8
    r=0.3679: sy = -1.9 + 0.3679*3.636 = -1.9 + 1.338 = -0.562
    r=1.0: sy = -1.9 + 3.636 = 1.736

  x-axis at y = 0.1 - 2.0 = -1.9
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

T2 = 1.0  # microseconds


class B03_DecoherenceRun(Scene):
    """Portrait T2 decay plot: rho_01(t) = e^(-t/T2).

    All label positions via sx/sy (pure float arithmetic, Gate A safe).
    """

    def construct(self):
        dur = _dur("B03")

        # Axis parameters
        cx, cy = 0.0, 0.1
        x_len, y_len = 3.2, 4.0
        x_min, x_max = 0.0, 4.0
        y_min, y_max = 0.0, 1.1

        def sx(t_val):
            return cx - x_len / 2 + (t_val - x_min) / (x_max - x_min) * x_len

        def sy(r_val):
            return cy - y_len / 2 + (r_val - y_min) / (y_max - y_min) * y_len

        x_axis_y = cy - y_len / 2   # = -1.9

        # Key coordinates
        t2_x = sx(T2)                    # = -0.8
        t2_y = sy(np.exp(-1.0))          # = -0.562
        dot0_x = sx(0.0)                 # = -1.6
        dot0_y = sy(1.0)                 # = 1.736

        # Header
        header = _ink_text("T2 Decay", font_size=18, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Axes — no tick numbers
        axes = Axes(
            x_range=[x_min, x_max, 1.0],
            y_range=[y_min, y_max, 0.25],
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": SLATE, "stroke_width": 1.5, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        )
        axes.move_to([cx, cy, 0])
        self.play(Create(axes), run_time=0.6)

        # Axis labels
        # x-label: above x-axis at right end
        x_lbl = _ink_text("t (us)", font_size=14)
        x_lbl.move_to([sx(x_max) - 0.25, x_axis_y + 0.35, 0])
        # y-label: left of y-axis at middle
        y_lbl = _ink_text("|rho|", font_size=14)
        y_lbl.move_to([-1.72, cy + 0.3, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # Sparse tick labels
        for t_val, label in [(1, "1"), (2, "2"), (3, "3")]:
            lbl = _ink_text(label, font_size=12)
            lbl.move_to([sx(float(t_val)), x_axis_y - 0.22, 0])
            self.add(lbl)

        for r_val, label in [(0.5, "0.5"), (1.0, "1")]:
            lbl = _ink_text(label, font_size=12)
            lbl.move_to([-1.78, sy(r_val), 0])
            self.add(lbl)

        # --- TEAL decay curve ---
        decay_curve = axes.plot(
            lambda t_us: np.exp(-t_us / T2),
            x_range=[x_min, x_max],
            color=TEAL,
            stroke_width=2.8
        )
        self.play(Create(decay_curve), run_time=0.7)

        # Dot at t=0
        d0 = Dot(point=[dot0_x, dot0_y, 0], radius=0.10, color=TEAL, fill_opacity=1)
        d0.set_stroke(width=0, opacity=0)
        self.play(FadeIn(d0), run_time=0.25)

        # --- CRIMSON T2 marker: vertical dashed line at t=T2 ---
        t2_line = DashedLine(
            start=[t2_x, x_axis_y, 0],
            end=[t2_x, t2_y, 0],
            color=CRIMSON, stroke_width=1.5, dash_length=0.12
        )
        self.play(Create(t2_line), run_time=0.4)

        # Dot on curve at t=T2
        t2_dot = Dot(point=[t2_x, t2_y, 0], radius=0.11, color=CRIMSON, fill_opacity=1)
        t2_dot.set_stroke(width=0, opacity=0)
        self.play(FadeIn(t2_dot), run_time=0.25)

        # Label at T2 marker — right of the dashed line, above dot
        t2_lbl = _ink_text("T2=1: 1/e", font_size=13)
        t2_lbl.move_to([t2_x + 0.75, t2_y + 0.40, 0])
        self.play(FadeIn(t2_lbl), run_time=0.3)

        # --- Chips ---
        teal_chip = LabelChip("1/e = 0.368", accent=TEAL, size=16)
        teal_chip.move_to([-0.50, -2.65, 0])
        self.play(GrowFromCenter(teal_chip), run_time=0.4)

        t2_chip = LabelChip("T2 = 1 us", accent=CRIMSON, size=16)
        t2_chip.move_to([0.60, -3.08, 0])
        self.play(GrowFromCenter(t2_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.7 + 0.25 + 0.4 + 0.25 + 0.3 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
