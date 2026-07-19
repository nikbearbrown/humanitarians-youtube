"""vox_scenes.py — medhavy-vol1-pib-spectrum
Reel: Infinite Square Well — Energy Ladder and n² Spectrum
Palette: medhavy (colorblind-safe Okabe-Ito)

Gate W colour rules (medhavy on GROUND #F0EAD6):
  TEAL  #009E73 — shape fills only (energy levels, wavefunctions)
  CRIMSON #D55E00 — shape fills only (ratio chip, annotations)
  INK   #000000 — ALL Text() elements (AAA on GROUND)
  LabelChip white-on-TEAL / white-on-CRIMSON = WARN-OK

Gate A rules:
  - Each .animate uses a single chained method
  - Dot markers at annotation beats create new distinct shape states
  - set_stroke(width=0, opacity=0) on all zero-width shapes

Safe area: x ∈ [-6.3, 6.3], y ∈ [-3.4, 3.4]
"""

import sys, json, pathlib, os

os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene
import numpy as np

# ── duration table ─────────────────────────────────────────────────────────────
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

_DEFAULTS = {"B03": 18.0}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    """Always renders in INK — enforces Gate W text-colour constraint."""
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    """axes.c2p wrapper safe in both real Manim and Gate-A stub context."""
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_PIBRun — Infinite Square Well: energy ladder n=1,2,3
# =============================================================================
class B03_PIBRun(Scene):
    """Infinite square well L=2 nm.
    Physics:
      E_n = n² × E_1,  E_1 = π²ℏ²/(2 m_e L²) ≈ 0.094 eV
      E_1 ≈ 0.094 eV   (n=1, ground state — never zero)
      E_2 ≈ 0.376 eV   (n=2)
      E_3 ≈ 0.846 eV   (n=3)
      Ratio E₂/E₁ = 4.000 exactly  (n² law)

    Scene layout:
      - Well walls at left and right edges (SLATE rectangles)
      - Horizontal energy levels at scaled y-positions (TEAL lines)
      - Sine-wave eigenfunctions drawn above each level (TEAL curves)
      - Energy labels right of each level (INK text)
      - Ratio chip E₂/E₁ = 4.000 in CRIMSON (WARN-OK)
      - Zero-point annotation: "E₁ > 0" chip in TEAL

    Gate B label placement:
      - All text labels placed at fixed positions well clear of curves/lines
      - Energy labels at x=4.5 (right of curve region)
      - Ratio chip at x=0, y=-2.5 (below all curves)
      - Header at x=1.5, y=3.1 (right of y-axis, above all content)
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics constants ──────────────────────────────────────────────────
        # E_1 = 0.094 eV for L=2 nm, m=m_e
        E1_eV = 0.094
        energies_eV = [E1_eV * n**2 for n in [1, 2, 3]]  # [0.094, 0.376, 0.846]

        # ── layout constants ───────────────────────────────────────────────────
        # Well occupies x ∈ [-4.0, 4.0]; y-scale: 1 eV → 5.0 units
        WELL_LEFT  = -4.0
        WELL_RIGHT =  4.0
        WELL_BOTTOM = -2.6  # leaves 0.8 units below floor for annotation chips
        Y_SCALE = 5.0  # scene units per eV — E1≈-2.13, E2≈-0.72, E3≈1.63

        def e_to_y(e_eV: float) -> float:
            """Map energy in eV to scene y-coordinate."""
            return WELL_BOTTOM + e_eV * Y_SCALE

        # ── header ────────────────────────────────────────────────────────────
        # x=0 centers text; y=3.1 is inside ±3.4 safe area, above E3 at ≈1.63
        header = _ink_text("Infinite Square Well  (L = 2 nm)", font_size=26, font=DISPLAY)
        header.move_to([0.0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)   # state S1: header

        # ── well walls (SLATE fills, no text) ─────────────────────────────────
        wall_thickness = 0.18
        left_wall = Rectangle(width=wall_thickness, height=6.4)
        left_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        left_wall.move_to([WELL_LEFT - wall_thickness / 2, 0, 0])

        right_wall = Rectangle(width=wall_thickness, height=6.4)
        right_wall.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        right_wall.move_to([WELL_RIGHT + wall_thickness / 2, 0, 0])

        # Well floor (SLATE line — stroke only, very thin)
        well_floor = Line(
            start=[WELL_LEFT, WELL_BOTTOM, 0],
            end=[WELL_RIGHT, WELL_BOTTOM, 0],
            stroke_width=1.5, color=SLATE,
        )

        self.play(FadeIn(left_wall), FadeIn(right_wall), FadeIn(well_floor),
                  run_time=0.5)   # state S1 (walls = same structural shapes)

        # ── energy levels and wavefunctions ───────────────────────────────────
        # Sine wavefunction amplitude in scene coords: 0.35 units max (won't overlap)
        PSI_AMP = 0.35
        label_names = ["E₁ = 0.094 eV", "E₂ = 0.376 eV", "E₃ = 0.846 eV"]

        for i, (e_eV, lbl_text) in enumerate(zip(energies_eV, label_names)):
            n = i + 1
            y_level = e_to_y(e_eV)

            # Energy level line (TEAL horizontal line, SHAPE fill not text)
            level_line = Line(
                start=[WELL_LEFT, y_level, 0],
                end=[WELL_RIGHT, y_level, 0],
                stroke_width=2.0, color=TEAL,
            )

            # Sine wavefunction as a Manim ParametricFunction
            # ψ_n(x) = A sin(nπx/L); plot over [-4, 4] scene units
            # scene x maps to physical x via: x_phys = (x_scene - WELL_LEFT) / (WELL_RIGHT - WELL_LEFT) * L
            def make_psi(n_val, y_base, amp):
                def _f(t):
                    # t ∈ [WELL_LEFT, WELL_RIGHT] → physical x ∈ [0, L]
                    x_phys = (t - WELL_LEFT) / (WELL_RIGHT - WELL_LEFT)
                    return np.array([t, y_base + amp * np.sin(n_val * np.pi * x_phys), 0])
                return _f

            psi_curve = ParametricFunction(
                make_psi(n, y_level, PSI_AMP),
                t_range=[WELL_LEFT + 0.01, WELL_RIGHT - 0.01],
                color=TEAL,
                stroke_width=2.0,
            )

            # Energy label — placed at x=4.6 (right of right wall), exactly at y_level
            # Gate B: no curve passes through x=4.6 (well ends at x=4.0) → safe
            lbl = _ink_text(lbl_text, font_size=18)
            lbl.move_to([4.85, y_level, 0])

            # Dot marker at mid-well for Gate A distinct shape state
            mid_dot = Dot(
                point=np.array([0.0, y_level, 0]),
                radius=0.07, color=TEAL,
                fill_opacity=1,
            ).set_stroke(width=0, opacity=0)

            self.play(Create(level_line), run_time=0.35)
            self.play(Create(psi_curve), run_time=0.55)
            self.play(FadeIn(lbl), FadeIn(mid_dot), run_time=0.3)
            # → each triplet (level + curve + label + dot) creates new distinct state

        # ── ratio chip: E₂/E₁ = 4.000 ────────────────────────────────────────
        # CRIMSON chip — placed below floor (y=-2.6), left of centre.
        # Floor-to-safe-area gap is 0.8 units; side-by-side with zp_chip avoids stack.
        ratio_chip = LabelChip("E₂/E₁ = 4.000", accent=CRIMSON, size=22)
        ratio_chip.move_to([-1.8, -3.05, 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.4)

        # ── zero-point annotation ─────────────────────────────────────────────
        # TEAL chip for "E₁ > 0" — beside ratio chip, below floor, right of centre.
        # E₁ is at y ≈ -2.13 (WELL_BOTTOM + 0.094*Y_SCALE = -2.6 + 0.47)
        zp_chip = LabelChip("E₁ > 0", accent=TEAL, size=22)
        zp_chip.move_to([2.0, -3.05, 0])
        self.play(GrowFromCenter(zp_chip), run_time=0.35)

        # ── n label at left wall ──────────────────────────────────────────────
        # Small "n" labels at left edge of each level, positioned ABOVE the level line
        # to avoid being on the horizontal stroke; x = WELL_LEFT - 0.5 (in wall gap)
        for i, e_eV in enumerate(energies_eV):
            n = i + 1
            y_level = e_to_y(e_eV)
            n_lbl = _ink_text(f"n={n}", font_size=16)
            # x = WELL_LEFT - 0.6 is OUTSIDE the well, no curve passes through
            n_lbl.move_to([WELL_LEFT - 0.6, y_level + 0.25, 0])
            self.play(FadeIn(n_lbl), run_time=0.2)

        # ── hold ──────────────────────────────────────────────────────────────
        # Approximate elapsed animation time:
        # header(0.4) + walls(0.5) + 3×(0.35+0.55+0.3) + ratio(0.4) + zp(0.35) + 3×n_lbl(0.2)
        elapsed = 0.4 + 0.5 + 3*(0.35 + 0.55 + 0.3) + 0.4 + 0.35 + 3*0.2
        self.wait(max(0.5, dur - elapsed))
