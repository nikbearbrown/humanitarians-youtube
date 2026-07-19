"""vox_scenes.py — medhavy-vol1-pib-spectrum SHORT (9:16 portrait)
Portrait layout: x_length=2.8 (safe ±1.95), y_length=5.0 (safe ±3.4)
No tick numbers on axes (safe-area constraint for 9:16).
Header ≤19 chars at font_size=19.
"""

import sys, json, pathlib, os

os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import numpy as np

# Portrait sync: vox_graphics sets frame_width from pixel aspect
# In portrait mode with -r 1080,1920: frame_width ≈ 4.5, frame_height ≈ 8.0

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(
            b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0
        )
        for b in _BS["beats"]
    })
except Exception:
    pass


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, 22.0)


def _ink_text(copy: str, font_size: int = 19, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


# =============================================================================
# B03_PIBRun — portrait version (9:16)
# =============================================================================
class B03_PIBRun(Scene):
    """Portrait PIB energy ladder. Stacked top-to-bottom layout.
    Safe area: x ∈ [-1.95, 1.95], y ∈ [-3.4, 3.4]
    Header 'PIB  L = 2 nm' = 14 chars → fits at font_size=19 ✓
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics ──────────────────────────────────────────────────────────
        E1_eV = 0.094
        energies_eV = [E1_eV * n**2 for n in [1, 2, 3]]

        # Portrait layout: well narrower, tall
        WELL_LEFT   = -1.5
        WELL_RIGHT  =  1.5
        WELL_BOTTOM = -3.0
        Y_SCALE = 2.8  # scene units per eV; E3 at y = 0.846*2.8 - 3 ≈ -0.63

        def e_to_y(e: float) -> float:
            return WELL_BOTTOM + e * Y_SCALE

        # ── header (≤19 chars, font_size=19) ─────────────────────────────────
        # "PIB  L = 2 nm" = 14 chars ✓
        header = _ink_text("PIB  L = 2 nm", font_size=19, font=DISPLAY)
        header.move_to([0.0, 3.15, 0])  # inside ±3.4
        self.play(FadeIn(header), run_time=0.4)

        # ── well walls ────────────────────────────────────────────────────────
        wall_thickness = 0.12
        left_wall = Rectangle(width=wall_thickness, height=6.5)
        left_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        left_wall.move_to([WELL_LEFT - wall_thickness / 2, 0, 0])

        right_wall = Rectangle(width=wall_thickness, height=6.5)
        right_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        right_wall.move_to([WELL_RIGHT + wall_thickness / 2, 0, 0])

        well_floor = Line(
            start=[WELL_LEFT, WELL_BOTTOM, 0],
            end=[WELL_RIGHT, WELL_BOTTOM, 0],
            stroke_width=1.2, color=SLATE,
        )
        self.play(FadeIn(left_wall), FadeIn(right_wall), FadeIn(well_floor),
                  run_time=0.4)

        # ── energy levels + wavefunctions ─────────────────────────────────────
        PSI_AMP = 0.30  # amplitude in scene units
        label_names = ["0.094 eV", "0.376 eV", "0.846 eV"]

        for i, (e_eV, lbl_text) in enumerate(zip(energies_eV, label_names)):
            n = i + 1
            y_level = e_to_y(e_eV)

            level_line = Line(
                start=[WELL_LEFT, y_level, 0],
                end=[WELL_RIGHT, y_level, 0],
                stroke_width=1.8, color=TEAL,
            )

            def make_psi(n_val, y_base, amp):
                def _f(t):
                    frac = (t - WELL_LEFT) / (WELL_RIGHT - WELL_LEFT)
                    return np.array([t, y_base + amp * np.sin(n_val * np.pi * frac), 0])
                return _f

            psi_curve = ParametricFunction(
                make_psi(n, y_level, PSI_AMP),
                t_range=[WELL_LEFT + 0.01, WELL_RIGHT - 0.01],
                color=TEAL, stroke_width=1.8,
            )

            # Label ABOVE the wavefunction (clear of any stroke)
            lbl = _ink_text(lbl_text, font_size=16)
            lbl.move_to([0.0, y_level + PSI_AMP + 0.22, 0])

            # n= label at left, ABOVE level line (no curve passes at x<WELL_LEFT)
            n_lbl = _ink_text(f"n={n}", font_size=15)
            n_lbl.move_to([WELL_LEFT - 0.3, y_level + 0.22, 0])

            # Dot marker for Gate A
            dot = Dot(point=np.array([0.0, y_level, 0]),
                      radius=0.06, color=TEAL, fill_opacity=1
                      ).set_stroke(width=0, opacity=0)

            self.play(Create(level_line), run_time=0.3)
            self.play(Create(psi_curve), run_time=0.45)
            self.play(FadeIn(lbl), FadeIn(n_lbl), FadeIn(dot), run_time=0.25)

        # ── ratio chip ────────────────────────────────────────────────────────
        # y = -2.6, inside safe area; no stroked object there
        ratio_chip = LabelChip("E2/E1 = 4.000", accent=CRIMSON, size=18)
        ratio_chip.move_to([0.0, -2.6, 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.4 + 3*(0.3 + 0.45 + 0.25) + 0.35
        self.wait(max(0.5, dur - elapsed))
