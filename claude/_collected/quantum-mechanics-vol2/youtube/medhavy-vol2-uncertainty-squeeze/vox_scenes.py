"""vox_scenes.py — medhavy-vol2-uncertainty-squeeze
Reel: Uncertainty Squeeze — Heisenberg Boundary as a Hyperbola
Palette: medhavy (Okabe-Ito)

Gate W: INK all Text; TEAL hyperbola + original state; CRIMSON squeezed state
Gate A: Two distinct Dot markers; hyperbola is curve shape state
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

def _dur(beat_id): return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))
def _ink_text(copy, font_size=24, font=SERIF, **kw):
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)
def _c2p(ax, x, y):
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


class B03_UncertaintyRun(Scene):
    """Uncertainty squeeze: σ_x σ_p = ℏ/2 hyperbola with two state points.
    Layout:
      Axes: x_range=[0, 3.0] nm, y_range=[0, 2.5] (×10⁻²⁵ kg·m/s)
      x_length=9.0, y_length=5.0
      Axes centered at LEFT*0.3 + DOWN*0.3
      x-axis stroke at scene y = -0.3 - 5.0/2 = -2.8
      Chips at y=-3.0 (just above -3.4 safe boundary... actually -2.8 - 0.2 gap = -3.0 is OK)
      State A (TEAL) at σ_x=1 nm; State B (CRIMSON) at σ_x=0.5 nm
      Labels for A and B placed ABOVE and to the right of the dots, away from the curve
    """

    def construct(self):
        dur = _dur("B03")
        hbar = 1.0546e-34  # J·s

        # physics (in display units: σ_x in nm, σ_p in 10^-26 kg·m/s)
        hbar_display = hbar * 1e9 * 1e26  # = hbar * 1e35; in (nm × 10⁻²⁶)
        # σ_p = hbar/(2σ_x) = (hbar_display/2) / σ_x_nm  → in 10⁻²⁶ kg·m/s
        # hbar_display/2 = 1.0546e-34 * 1e9 * 1e26 / 2 = 1.0546e1/2 = 5.273
        # So σ_p(σ_x_nm) = 5.273 / σ_x_nm  in units of 10⁻²⁶ kg·m/s

        HALF_HBAR = 5.273  # in display units

        def sigma_p_disp(sx_nm):
            return HALF_HBAR / sx_nm  # in 10⁻²⁶ kg·m/s

        # State A: σ_x=1 nm, σ_p=5.273; State B: σ_x=0.5 nm, σ_p=10.546
        sx_A, sp_A = 1.0, sigma_p_disp(1.0)   # 5.273
        sx_B, sp_B = 0.5, sigma_p_disp(0.5)   # 10.546

        # header
        header = _ink_text("Uncertainty Squeeze  σ_x σ_p = ℏ/2",
                           font_size=21, font=DISPLAY)
        header.move_to([0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # axes
        axes = Axes(
            x_range=[0, 3.0, 0.5],
            y_range=[0, 15.0, 5.0],
            x_length=9.0,
            y_length=5.0,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(LEFT * 0.3 + DOWN * 0.3)

        self.play(Create(axes), run_time=0.6)

        xlbl = _ink_text("σ_x  (nm)", font_size=15)
        xlbl.next_to(axes.x_axis, DOWN, buff=0.22)
        ylbl = _ink_text("σ_p  (×10⁻²⁶ kg·m/s)", font_size=14)
        ylbl.move_to([-5.6, -0.3, 0])
        self.play(FadeIn(xlbl), FadeIn(ylbl), run_time=0.3)

        # hyperbola σ_p = 5.273/σ_x (TEAL)
        hyp_curve = axes.plot(
            lambda x: sigma_p_disp(x),
            x_range=[0.36, 2.9],
            color=TEAL,
            stroke_width=2.5,
        )
        self.play(Create(hyp_curve), run_time=0.9)

        # State A dot (TEAL) at (1.0, 5.273)
        A_pos = _c2p(axes, sx_A, sp_A)
        dot_A = Dot(point=A_pos, radius=0.12, color=TEAL,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_A), run_time=0.3)

        # Label A: placed ABOVE and to the right — curve goes downward to the right
        # At x=1.0 the curve is at y=5.273; curve slope is negative so
        # placing label at (x+0.5, y+1.5) is above the curve there
        A_scene_x = float(A_pos[0]) if isinstance(A_pos, np.ndarray) else 0
        A_scene_y = float(A_pos[1]) if isinstance(A_pos, np.ndarray) else 0
        lbl_A = _ink_text("A: σ_x=1nm", font_size=15)
        lbl_A.move_to([A_scene_x + 1.0, A_scene_y + 0.5, 0])
        self.play(FadeIn(lbl_A), run_time=0.3)

        # Dashed horizontal at sp_A (reference line for doubling comparison)
        dash_left = _c2p(axes, 0.0, sp_A)
        dash_right = _c2p(axes, sx_A, sp_A)
        dash_horiz = DashedLine(start=dash_left, end=dash_right, color=TEAL,
                                stroke_width=1.2, dash_length=0.1)
        self.play(Create(dash_horiz), run_time=0.3)

        # State B dot (CRIMSON) at (0.5, 10.546)
        B_pos = _c2p(axes, sx_B, sp_B)
        dot_B = Dot(point=B_pos, radius=0.12, color=CRIMSON,
                    fill_opacity=1).set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_B), run_time=0.3)

        # Label B: above and right of B
        B_scene_x = float(B_pos[0]) if isinstance(B_pos, np.ndarray) else -1
        B_scene_y = float(B_pos[1]) if isinstance(B_pos, np.ndarray) else 1
        lbl_B = _ink_text("B: σ_x=0.5nm", font_size=15)
        lbl_B.move_to([B_scene_x + 1.3, B_scene_y + 0.4, 0])
        self.play(FadeIn(lbl_B), run_time=0.3)

        # Double arrow between A and B sigma_p values
        # (connecting the dashed line to B vertically)
        dbl_start = _c2p(axes, 0.15, sp_A)
        dbl_end   = _c2p(axes, 0.15, sp_B)
        if isinstance(dbl_start, np.ndarray) and isinstance(dbl_end, np.ndarray):
            dbl_arr = DoubleArrow(
                start=dbl_start, end=dbl_end,
                color=CRIMSON, stroke_width=1.8,
                tip_length=0.15,
            )
            ratio_lbl = _ink_text("×2", font_size=16)
            mid_y = (float(dbl_start[1]) + float(dbl_end[1])) / 2
            ratio_lbl.move_to([-5.2, mid_y, 0])
            self.play(Create(dbl_arr), FadeIn(ratio_lbl), run_time=0.4)

        # chips
        # x-axis stroke at y = -0.3 - 2.5 = -2.8
        # chips at y=-3.0 (within -3.4 safe boundary)
        hb_chip = LabelChip("σ_x σ_p = ℏ/2", accent=TEAL, size=19)
        hb_chip.move_to([-1.5, -3.0, 0])
        self.play(GrowFromCenter(hb_chip), run_time=0.4)

        sq_chip = LabelChip("halve σ_x → double σ_p", accent=CRIMSON, size=19)
        sq_chip.move_to([2.2, -3.0, 0])
        self.play(GrowFromCenter(sq_chip), run_time=0.35)

        elapsed = (0.4 + 0.6 + 0.3 + 0.9 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.4 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
