"""vox_scenes.py — medhavy-companion-pib/short (9:16 portrait)
Reel: Particle in a Box — Energy Ladder (L=1 nm)
Palette: medhavy (Okabe-Ito)

Physics:
  E_n = n^2 * E1,  E1 = pi^2 hbar^2 / (2 m_e L^2) ~ 0.376 eV  (L=1 nm)
  E1=0.376 eV, E2=1.504 eV, E3=3.384 eV
  Ratio E2/E1 = 4.000 exactly (n-squared law)

Portrait layout:
  Safe area: +-1.95x / +-3.4y
  Well walls at x = +-1.05 (wall thickness 0.15)
  Well interior: x in [-1.05, 1.05], width = 2.10
  Floor at y = -2.10
  Energy scale: Y_SCALE = 1.00 scene-units/eV
  e_to_y(e) = -2.10 + e * Y_SCALE
    E1 at y = -1.724; E2 at y = -0.596; E3 at y = 1.284

  Energy labels at x = 1.35 (just right of well wall)
  n labels at x = -1.38 (just left of well wall)
  Chips at y = -2.72 and y = -3.15
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

_DEFAULTS = {"B03": 23.54}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)

# Physics
E1_eV = 0.376
energies_eV = [E1_eV * n**2 for n in [1, 2, 3]]  # [0.376, 1.504, 3.384]

# Well geometry
WELL_LEFT = -1.05
WELL_RIGHT = 1.05
WELL_BOTTOM = -2.10
Y_SCALE = 1.00  # scene units per eV (E3=3.384 -> y=1.284, inside safe area)

def e_to_y(e_eV: float) -> float:
    return WELL_BOTTOM + e_eV * Y_SCALE

LABEL_NAMES = ["E1 = 0.376 eV", "E2 = 1.504 eV", "E3 = 3.384 eV"]


class B03_PIBRun(Scene):
    """Portrait particle-in-a-box: well + 3 energy levels + sine wavefunctions.

    All label positions via pure-float arithmetic (Gate A safe).
    No c2p() arithmetic.
    """

    def construct(self):
        dur = _dur("B03")

        # Header
        header = _ink_text("Particle in a Box  L=1 nm", font_size=14, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Subtitle
        sub = _ink_text("E_n = n^2 * E1", font_size=12)
        sub.move_to([0, 2.82, 0])
        self.play(FadeIn(sub), run_time=0.3)

        # Well walls (SLATE rectangles)
        wall_thickness = 0.13
        wall_height = 5.5  # tall enough to fill safe area
        left_wall = Rectangle(width=wall_thickness, height=wall_height)
        left_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        left_wall.move_to([WELL_LEFT - wall_thickness / 2, 0.5, 0])

        right_wall = Rectangle(width=wall_thickness, height=wall_height)
        right_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        right_wall.move_to([WELL_RIGHT + wall_thickness / 2, 0.5, 0])

        # Well floor
        well_floor = Line(
            start=[WELL_LEFT, WELL_BOTTOM, 0],
            end=[WELL_RIGHT, WELL_BOTTOM, 0],
            stroke_width=2.0, color=SLATE,
        )

        self.play(FadeIn(left_wall), FadeIn(right_wall), FadeIn(well_floor), run_time=0.5)

        # Energy levels + wavefunctions + labels
        PSI_AMP = 0.16  # wavefunction amplitude (scene units, compact for portrait)

        for i, (e_eV, lbl_text) in enumerate(zip(energies_eV, LABEL_NAMES)):
            n = i + 1
            y_level = e_to_y(e_eV)

            # Horizontal energy level (TEAL)
            level_line = Line(
                start=[WELL_LEFT, y_level, 0],
                end=[WELL_RIGHT, y_level, 0],
                stroke_width=2.0, color=TEAL,
            )

            # Sine wavefunction (parametric, pure Python — no c2p)
            well_width = WELL_RIGHT - WELL_LEFT  # = 2.10
            def make_psi(n_val, y_base, amp, wl=WELL_LEFT, wr=WELL_RIGHT):
                def _f(t):
                    x_phys = (t - wl) / (wr - wl)
                    return np.array([t, y_base + amp * np.sin(n_val * np.pi * x_phys), 0])
                return _f

            psi_curve = ParametricFunction(
                make_psi(n, y_level, PSI_AMP),
                t_range=[WELL_LEFT + 0.01, WELL_RIGHT - 0.01],
                color=TEAL,
                stroke_width=2.0,
            )

            # Energy label — at x=1.35, just right of well wall (x=1.115)
            # No curve passes outside the well walls
            lbl = _ink_text(lbl_text, font_size=10)
            lbl.move_to([1.35, y_level, 0])  # x=1.35 < safe-area edge 1.95

            # n label — at x=-1.38, just left of well wall
            n_lbl = _ink_text(f"n={n}", font_size=10)
            n_lbl.move_to([-1.40, y_level + 0.22, 0])

            # Mid-well dot
            mid_dot = Dot(
                point=np.array([0.0, y_level, 0]),
                radius=0.06, color=TEAL, fill_opacity=1,
            ).set_stroke(width=0, opacity=0)

            self.play(Create(level_line), run_time=0.30)
            self.play(Create(psi_curve), run_time=0.45)
            self.play(FadeIn(lbl), FadeIn(n_lbl), FadeIn(mid_dot), run_time=0.25)

        # Ratio chip: E2/E1 = 4.000 (CRIMSON)
        # Place in lower zone: y=-2.72 (between floor at -2.10 and chip zone at -2.72)
        ratio_chip = LabelChip("E2/E1 = 4.000", accent=CRIMSON, size=14)
        ratio_chip.move_to([0.15, -2.72, 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.4)

        # Zero-point chip (TEAL)
        zp_chip = LabelChip("E1 > 0  zero-point", accent=TEAL, size=14)
        zp_chip.move_to([-0.10, -3.15, 0])
        self.play(GrowFromCenter(zp_chip), run_time=0.35)

        elapsed = (0.4 + 0.3 + 0.5
                   + 3 * (0.30 + 0.45 + 0.25)
                   + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
