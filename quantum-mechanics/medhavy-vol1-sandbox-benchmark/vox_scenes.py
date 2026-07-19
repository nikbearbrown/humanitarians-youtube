"""vox_scenes.py — medhavy-vol1-sandbox-benchmark
Reel: 1D Quantum Eigensolver Benchmark — Tridiagonal H and n² Spectrum
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — numerical eigenvalue dots, diagonal entries label
  CRIMSON (#D55E00) — analytic energy lines, error annotation

Gate A:
  Dot markers at analytic/numerical level pairs; matrix cells are
  distinct filled shapes. Each .animate uses single chained method.

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
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_SandboxRun — tridiagonal matrix + energy level comparison
# =============================================================================
class B03_SandboxRun(Scene):
    """Eigensolver benchmark: analytic vs numerical ISW energies.
    Physics:
      E_n = n²π²ℏ²/2mL²;  L=2 nm, m=m_e → E₁≈0.094 eV
      E₂/E₁ = 4.000 exactly;  frac error < 10⁻⁵ for N=500

    Layout:
      LEFT panel (center: [-3.3, 0, 0]): 4×4 schematic of tridiagonal H
        Each cell: Rectangle width=1.6, height=0.8
        Diagonal cells: TEAL fill (α=0.25) with INK text "2t_k"
        Off-diagonal cells: CRIMSON fill (α=0.25) with INK text "-t_k"
        Corner/zero cells: INK text "0" on plain ground background
      RIGHT panel: energy level comparison on Axes
        Axes center [3.3, -0.1], x_range=[0,2], y_range=[0,0.95]
        x_length=3.0, y_length=4.5
        CRIMSON lines at analytic E_n; TEAL dots at numerical E_n
        Labels: n=1..4 at x=1.6, y=E_n
        numbers_to_include=[] on both axes
      Header at y=3.1
      Chips at y=-2.8 and y=-3.2

    Gate B notes:
      All labels placed away from any stroked VMobject.
      Right panel x-axis stroke at scene y = -0.1 - 4.5/2 = -2.35
      Chips placed at y=-2.8 (above -3.4 safe boundary, below x-axis stroke).
      Left panel: label text is ON the colored Rectangle fill (not on a stroke).
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics ────────────────────────────────────────────────────────────
        hbar = 1.0546e-34
        m_e  = 9.109e-31
        eV   = 1.602e-19
        L    = 2e-9
        E1_ana = (np.pi**2 * hbar**2) / (2 * m_e * L**2) / eV  # ≈0.0943 eV
        E_n_ana = [E1_ana * n**2 for n in range(1, 4)]  # n=1,2,3 (avoid n=4 exceeding y_range)
        # Numerical values (to 4 dp): same (negligible error for N=500)
        E_n_num = [e * (1 - 3e-6) for e in E_n_ana]  # show tiny offset for illustration

        # ── header ────────────────────────────────────────────────────────────
        header = _ink_text("Eigensolver Benchmark  L = 2 nm, N = 500",
                           font_size=20, font=DISPLAY)
        header.move_to([0.0, 3.1, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ─────────────────────────────────────────────────────────────────────
        # LEFT PANEL: Schematic tridiagonal matrix (4×4)
        # ─────────────────────────────────────────────────────────────────────
        cell_w = 1.55
        cell_h = 0.75
        mat_cx = -3.3
        mat_cy = 0.3

        # Labels for each cell position
        # Diagonal: (i,i) → "2t_k"; off-diag (i,i±1) → "-t_k"; else → "0"
        labels_4x4 = [
            ["2t_k", "-t_k", "0",    "0"   ],
            ["-t_k", "2t_k", "-t_k", "0"   ],
            ["0",    "-t_k", "2t_k", "-t_k"],
            ["0",    "0",    "-t_k", "2t_k"],
        ]

        cells = []
        for row in range(4):
            for col in range(4):
                cx = mat_cx + (col - 1.5) * cell_w
                cy = mat_cy - (row - 1.5) * cell_h
                lbl_str = labels_4x4[row][col]

                if row == col:
                    fill = TEAL
                    fill_op = 0.25
                elif abs(row - col) == 1:
                    fill = CRIMSON
                    fill_op = 0.25
                else:
                    fill = GROUND
                    fill_op = 1.0

                cell_rect = Rectangle(width=cell_w, height=cell_h,
                                      fill_color=fill, fill_opacity=fill_op,
                                      stroke_color=SLATE, stroke_width=0.8)
                cell_rect.move_to([cx, cy, 0])

                cell_lbl = _ink_text(lbl_str, font_size=14)
                cell_lbl.move_to([cx, cy, 0])

                cells.append((cell_rect, cell_lbl))

        for rect, lbl in cells:
            self.play(FadeIn(rect), run_time=0.08)
            self.play(FadeIn(lbl), run_time=0.06)

        # Matrix label below
        mat_lbl = _ink_text("H (4×4 excerpt)", font_size=15)
        mat_lbl.move_to([mat_cx, mat_cy - 1.75, 0])
        self.play(FadeIn(mat_lbl), run_time=0.25)

        # ─────────────────────────────────────────────────────────────────────
        # RIGHT PANEL: Energy level comparison
        # ─────────────────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[0, 2.0, 1],
            y_range=[0, 0.95, 0.2],
            x_length=3.0,
            y_length=4.5,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to([3.3, -0.1, 0])

        self.play(Create(ax), run_time=0.5)

        ylbl = _ink_text("E (eV)", font_size=15)
        ylbl.move_to([1.45, -0.1, 0])

        # x-axis label (no x label needed — x has no physical meaning here)
        self.play(FadeIn(ylbl), run_time=0.25)

        n_labels = ["n=1", "n=2", "n=3"]
        # Analytic ratios: 1, 4, 9, 16 × E1 = 0.0943 eV
        for n_idx, (e_ana, e_num, n_lbl) in enumerate(zip(E_n_ana, E_n_num, n_labels)):
            # Analytic line: CRIMSON, x from 0.1 to 1.4 data
            ana_start = _c2p(ax, 0.1, e_ana)
            ana_end   = _c2p(ax, 1.4, e_ana)
            if isinstance(ana_start, np.ndarray) and isinstance(ana_end, np.ndarray):
                ana_line = Line(start=ana_start, end=ana_end,
                                stroke_width=2.0, color=CRIMSON)
                self.play(Create(ana_line), run_time=0.25)

            # Numerical dot: TEAL, at x=0.75
            num_pos = _c2p(ax, 0.75, e_num)
            num_dot = Dot(point=num_pos, radius=0.09, color=TEAL,
                          fill_opacity=1).set_stroke(width=0, opacity=0)
            self.play(FadeIn(num_dot), run_time=0.2)

            # Label at right edge of axes; place ABOVE the line to avoid overlap
            label_pos_y = _c2p(ax, 0, e_ana)
            lbl_y = float(label_pos_y[1]) if isinstance(label_pos_y, np.ndarray) else 0
            ratio = (n_idx + 1)**2
            lbl = _ink_text(f"{n_lbl}  ×{ratio}", font_size=14)
            lbl.move_to([6.0, lbl_y, 0])
            self.play(FadeIn(lbl), run_time=0.2)

        # ── chips ─────────────────────────────────────────────────────────────
        # Right panel x-axis at scene y = -0.1 - 4.5/2 = -2.35
        # Chips at y=-2.8 and y=-3.2 (below x-axis, within safe area)
        ratio_chip = LabelChip("E₂/E₁ = 4.000", accent=TEAL, size=19)
        ratio_chip.move_to([-1.5, -2.8, 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.4)

        err_chip = LabelChip("error < 10⁻⁵", accent=CRIMSON, size=19)
        err_chip.move_to([1.5, -2.8, 0])
        self.play(GrowFromCenter(err_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        # 16 cell FadeIns (0.08+0.06 each) + mat_lbl + ax + ylbl + 4*(0.25+0.2+0.2) + chips
        elapsed = 16*(0.08+0.06) + 0.25 + 0.4 + 0.5 + 0.25 + 4*(0.25+0.2+0.2) + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
