"""vox_scenes.py — medhavy-companion-pib
Reel: Particle in a Box — Energy Ladder (L=1 nm)
Palette: medhavy (colorblind-safe Okabe-Ito)

Gate W colour rules (medhavy on GROUND #F0EAD6):
  TEAL  #009E73 — shape fills only (energy levels, wavefunctions)
  CRIMSON #D55E00 — shape fills only (ratio chip, annotations)
  INK   #000000 — ALL Text() elements (AAA on GROUND)
  LabelChip white-on-TEAL / white-on-CRIMSON = WARN-OK

Gate B placement:
  - Header at [1.5, 3.1, 0] — right of y-axis, inside safe area
  - Energy labels at x=4.85 (outside well region x=[-4,4])
  - Ratio chip at [0, -2.6, 0] — below all energy levels
  - n-labels at x=-4.7 (outside well, no curves)
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
# B03_PIBRun — Particle in a Box L=1 nm: energy ladder n=1,2,3
# =============================================================================
class B03_PIBRun(Scene):
    """Particle in a box L=1 nm.
    Physics:
      E_n = n^2 * E_1,  E_1 = pi^2 hbar^2 / (2 m_e L^2) approx 0.376 eV
      E_1 approx 0.376 eV  (n=1, ground state)
      E_2 approx 1.504 eV  (n=2)
      E_3 approx 3.384 eV  (n=3)
      Ratio E2/E1 = 4.000 exactly

    Scene layout:
      - Well walls (SLATE rectangles), floor (SLATE line)
      - Horizontal energy levels (TEAL lines)
      - Sine eigenfunctions above each level (TEAL curves)
      - Energy labels right of well at x=4.85 (no curves there)
      - Ratio chip at [0, -2.6, 0]
      - Zero-point chip at [0, -3.1, 0]
      - n labels at x=-4.7 (outside well)
    """

    def construct(self):
        dur = _dur("B03")

        # Physics constants
        E1_eV = 0.376
        energies_eV = [E1_eV * n**2 for n in [1, 2, 3]]  # [0.376, 1.504, 3.384]

        # Layout: well x in [-4, 4]; y-scale maps energy to scene
        WELL_LEFT = -4.0
        WELL_RIGHT = 4.0
        WELL_BOTTOM = -3.1
        # Scale: E3=3.384 eV should map to about y=0.8 => scale = (0.8-(-3.1))/3.384 = 1.153
        Y_SCALE = 1.10  # scene units per eV

        def e_to_y(e_eV):
            return WELL_BOTTOM + e_eV * Y_SCALE

        # Header — placed BEFORE axes (but wells aren't axes, still safe to do first)
        # x=1.5 avoids any vertical stroke; y=3.1 inside safe area
        header = _ink_text("Particle in a Box  (L = 1 nm)", font_size=26, font=DISPLAY)
        header.move_to([1.5, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Well walls (SLATE rectangles)
        wall_thickness = 0.18
        left_wall = Rectangle(width=wall_thickness, height=7.0)
        left_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        left_wall.move_to([WELL_LEFT - wall_thickness / 2, 0, 0])

        right_wall = Rectangle(width=wall_thickness, height=7.0)
        right_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        right_wall.move_to([WELL_RIGHT + wall_thickness / 2, 0, 0])

        # Well floor (thin SLATE stroke)
        well_floor = Line(
            start=[WELL_LEFT, WELL_BOTTOM, 0],
            end=[WELL_RIGHT, WELL_BOTTOM, 0],
            stroke_width=1.5, color=SLATE,
        )

        self.play(FadeIn(left_wall), FadeIn(right_wall), FadeIn(well_floor), run_time=0.5)

        # Energy levels, sine wavefunctions, and labels
        PSI_AMP = 0.28  # wavefunction amplitude (scene units)
        label_names = ["E1 = 0.376 eV", "E2 = 1.504 eV", "E3 = 3.384 eV"]

        for i, (e_eV, lbl_text) in enumerate(zip(energies_eV, label_names)):
            n = i + 1
            y_level = e_to_y(e_eV)

            # Horizontal energy level (TEAL stroke)
            level_line = Line(
                start=[WELL_LEFT, y_level, 0],
                end=[WELL_RIGHT, y_level, 0],
                stroke_width=2.0, color=TEAL,
            )

            # Sine wavefunction
            def make_psi(n_val, y_base, amp):
                def _f(t):
                    x_phys = (t - WELL_LEFT) / (WELL_RIGHT - WELL_LEFT)
                    return np.array([t, y_base + amp * np.sin(n_val * np.pi * x_phys), 0])
                return _f

            psi_curve = ParametricFunction(
                make_psi(n, y_level, PSI_AMP),
                t_range=[WELL_LEFT + 0.01, WELL_RIGHT - 0.01],
                color=TEAL,
                stroke_width=2.0,
            )

            # Energy label — at x=4.85, well outside the well region
            # Gate B: no curve passes through x > 4.0
            lbl = _ink_text(lbl_text, font_size=18)
            lbl.move_to([5.1, y_level, 0])

            # Dot marker at mid-well (Gate A distinct shape state)
            mid_dot = Dot(
                point=np.array([0.0, y_level, 0]),
                radius=0.07, color=TEAL,
                fill_opacity=1,
            ).set_stroke(width=0, opacity=0)

            self.play(Create(level_line), run_time=0.35)
            self.play(Create(psi_curve), run_time=0.55)
            self.play(FadeIn(lbl), FadeIn(mid_dot), run_time=0.3)

        # Ratio chip E2/E1 = 4.000 (CRIMSON, WARN-OK per Gate W)
        # Position: y=-2.6, well below E1 at y=e_to_y(0.376)=-2.686
        # Floor is at y=-3.1; chip goes between -3.1 and -2.686 → y=-2.9 safe
        y_e1 = e_to_y(E1_eV)  # -3.1 + 0.376*1.10 = -2.686
        ratio_chip = LabelChip("E2/E1 = 4.000", accent=CRIMSON, size=21)
        ratio_chip.move_to([0.0, max(y_e1 - 0.35, -3.0), 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.4)

        # n labels (outside well, no curves at x < -4.0)
        for i, e_eV in enumerate(energies_eV):
            n = i + 1
            y_level = e_to_y(e_eV)
            n_lbl = _ink_text(f"n={n}", font_size=16)
            n_lbl.move_to([WELL_LEFT - 0.55, y_level + 0.22, 0])
            self.play(FadeIn(n_lbl), run_time=0.2)

        # Elapsed time estimate
        elapsed = 0.4 + 0.5 + 3*(0.35 + 0.55 + 0.3) + 0.4 + 3*0.2
        self.wait(max(0.5, dur - elapsed))
