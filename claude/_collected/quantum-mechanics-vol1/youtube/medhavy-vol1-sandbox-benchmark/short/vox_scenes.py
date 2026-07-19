"""vox_scenes.py — medhavy-vol1-sandbox-benchmark/short (9:16 portrait)
Palette: medhavy (Okabe-Ito)

Gate W:
  INK (#000000) — all Text()
  TEAL (#009E73) — numerical eigenvalue dots, diagonal entries
  CRIMSON (#D55E00) — analytic energy lines, error annotation

Safe area: 9:16 portrait ±1.95x / ±3.4y

Layout: energy level comparison only (portrait too narrow for dual panel).
  Axes: x_range=[0, 2], y_range=[0, 1.0], x_length=3.0, y_length=4.5
  Centered at ORIGIN + UP*0.25
  x-axis stroke at scene y = 0.25 - 4.5/2 = -2.0
  Labels placed RIGHT of axes at x=1.82 (within ±1.95 safe area)
  Chips at y=-2.7 and y=-3.15 (below x-axis stroke, within ±3.4 safe area)
"""

import sys, json, pathlib, os

os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4]
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

_DEFAULTS = {"B03": 28.79}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B03_SandboxRun — portrait energy level comparison
# =============================================================================
class B03_SandboxRun(Scene):
    """Portrait benchmark: analytic (CRIMSON lines) vs numerical (TEAL dots).
    Physics: E_n = n²×E₁; E₁≈0.094 eV; E₂/E₁=4.000; error<10⁻⁵
    """

    def construct(self):
        dur = _dur("B03")

        # ── physics ────────────────────────────────────────────────────────────
        hbar = 1.0546e-34
        m_e  = 9.109e-31
        eV   = 1.602e-19
        L    = 2e-9
        E1_ana = (np.pi**2 * hbar**2) / (2 * m_e * L**2) / eV  # ≈0.0943 eV
        # n=1,2,3 only (n=4 would be 16×E₁ ≈ 1.51 eV, outside y_range)
        E_n_ana = [E1_ana * n**2 for n in range(1, 4)]
        E_n_num = [e * (1 - 3e-6) for e in E_n_ana]

        # ── header ─────────────────────────────────────────────────────────────
        header = _ink_text("Eigensolver  L=2nm N=500",
                            font_size=15, font=DISPLAY)
        header.move_to([0, 3.2, 0])
        self.play(FadeIn(header), run_time=0.4)

        # ── axes ───────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 2.0, 1],
            y_range=[0, 1.0, 0.2],
            x_length=3.0,
            y_length=4.5,
            axis_config={"color": SLATE, "stroke_width": 1.8, "include_tip": True,
                         "decimal_number_config": {"color": INK}},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + UP * 0.25)

        self.play(Create(axes), run_time=0.5)

        ylbl = _ink_text("E (eV)", font_size=13)
        ylbl.next_to(axes.y_axis, LEFT, buff=0.1)
        self.play(FadeIn(ylbl), run_time=0.25)

        n_labels = ["n=1", "n=2", "n=3"]
        ratios = [1, 4, 9]

        for n_idx, (e_ana, e_num, n_lbl, ratio) in enumerate(
                zip(E_n_ana, E_n_num, n_labels, ratios)):

            # Analytic line: CRIMSON
            ana_start = _c2p(axes, 0.1, e_ana)
            ana_end   = _c2p(axes, 1.5, e_ana)
            if isinstance(ana_start, np.ndarray) and isinstance(ana_end, np.ndarray):
                ana_line = Line(start=ana_start, end=ana_end,
                                stroke_width=2.0, color=CRIMSON)
                self.play(Create(ana_line), run_time=0.25)

            # Numerical dot: TEAL at x=0.8
            num_pos = _c2p(axes, 0.8, e_num)
            num_dot = Dot(point=num_pos, radius=0.09, color=TEAL,
                          fill_opacity=1).set_stroke(width=0, opacity=0)
            self.play(FadeIn(num_dot), run_time=0.2)

            # Label placed to RIGHT of the axes (within ±1.95 portrait safe area)
            # Axes: x_length=3.0, centered at (0,0.25) → right edge at x ≈ 1.5
            # Place labels at x=1.82 (right of axes, well within 1.95)
            label_pos_y = _c2p(axes, 0, e_ana)
            lbl_y = float(label_pos_y[1]) if isinstance(label_pos_y, np.ndarray) else 0
            lbl = _ink_text(f"{n_lbl} ×{ratio}", font_size=13)
            lbl.move_to([1.82, lbl_y, 0])
            self.play(FadeIn(lbl), run_time=0.2)

        # ── chips ──────────────────────────────────────────────────────────────
        # x-axis stroke at y ≈ -2.0; chips at y=-2.7 and y=-3.15
        ratio_chip = LabelChip("E₂/E₁=4.000", accent=TEAL, size=16)
        ratio_chip.move_to([0, -2.7, 0])
        self.play(GrowFromCenter(ratio_chip), run_time=0.4)

        err_chip = LabelChip("error<10⁻⁵", accent=CRIMSON, size=16)
        err_chip.move_to([0, -3.15, 0])
        self.play(GrowFromCenter(err_chip), run_time=0.35)

        # ── hold ───────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.5 + 0.25 + 3*(0.25+0.2+0.2) + 0.4 + 0.35
        self.wait(max(0.5, dur - elapsed))
