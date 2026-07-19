"""vox_scenes.py — medhavy-ch1-classical-sims/short
Portrait (1080×1920) Manim scenes for the 9:16 Short cut.
Segment: UV CATASTROPHE — Planck vs Rayleigh-Jeans.

Frame: 1080×1920  →  frame_width ≈ 4.5,  frame_height = 8.0
Safe area: x ∈ [−1.85, 1.85],  y ∈ [−3.5, 3.5]

Palette: medhavy (colorblind-safe Okabe-Ito)
  INK #000000 — all Text()
  TEAL #009E73 — Planck curve + chip (shape fill)
  CRIMSON #D55E00 — RJ curve + chip (shape fill)
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

_DEFAULTS = {"B11": 20.0}


def _dur(beat_id: str) -> float:
    return DUR.get(beat_id, _DEFAULTS.get(beat_id, 10.0))


def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> Text:
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


def _c2p(ax, x, y) -> np.ndarray:
    pt = ax.c2p(x, y)
    return pt if isinstance(pt, np.ndarray) else np.zeros(3)


# =============================================================================
# B11_UVCatastropheRunPortrait — 9:16 portrait for the UV catastrophe short
# =============================================================================
class B11_UVCatastropheRunPortrait(Scene):
    """UV catastrophe (portrait 1080×1920): Planck vs Rayleigh-Jeans.

    Physics (identical to landscape):
      f_P(x) = x³/(eˣ−1) / 1.419   Planck, normalised to peak=1
      f_RJ(x) = x² / 1.419           Rayleigh-Jeans — diverges

    Layout for 9:16 (frame_width≈4.5, safe x ∈ [−1.90, 1.90], y ∈ [−3.4, 3.4]):
      • Single header at y=3.05 (within safe ±3.4)
      • Axes: x_length=2.8, y_length=4.0, centred at (0, −0.20)
          → x edges at ±1.4, y edges at −2.2 / +1.8
      • No axis tick numbers (they clip at x≈±2.0 in portrait)
      • x-label below axes
      • Curve labels at fixed scene y=2.1 (above axes top at y=1.8, below header)
      • DIVERGES chip in above-axes strip (y=2.42)
      • Legend chips at y=−2.9 (within safe area)
    """

    def construct(self):
        dur = _dur("B11")

        # ── header — single line, scaled to fit within safe x ────────────────
        h1 = _ink_text("Blackbody Radiation", font_size=19, font=DISPLAY)
        h1.move_to([0, 3.05, 0])
        self.play(FadeIn(h1), run_time=0.5)

        # ── axes — narrow and tall, no tick numbers ──────────────────────────
        # x_length=2.8: left edge x=−1.4, right edge x=+1.4 (safe ±1.9)
        # y_length=4.0: bottom y=−2.2, top y=+1.8 (safe ±3.4)
        axes = Axes(
            x_range=[0, 8, 2],
            y_range=[0, 7, 1],
            x_length=2.8,
            y_length=4.0,
            axis_config={
                "color": SLATE,
                "stroke_width": 2,
                "include_tip": True,
                "decimal_number_config": {"color": INK},
            },
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
        ).move_to(ORIGIN + DOWN * 0.20)

        self.play(Create(axes), run_time=0.7)

        # x-label below axes (y ≈ −2.2 − 0.30 = −2.5, within safe ±3.4)
        x_lbl = _ink_text("x = hν / kT", font_size=15)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.30)
        self.play(FadeIn(x_lbl), run_time=0.25)

        # ── curve functions ───────────────────────────────────────────────────
        _PEAK = 1.419

        def planck_norm(x: float) -> float:
            if x < 0.001:
                return 0.0
            ex = np.exp(min(x, 50.0))
            denom = ex - 1.0
            return 0.0 if denom < 1e-12 else (x ** 3 / denom) / _PEAK

        def rj_norm(x: float) -> float:
            return (x ** 2) / _PEAK

        def rj_plot(x: float) -> float:
            # Clip at 6.8 — keeps curve within y_range=[0,7] and off the header.
            return min(rj_norm(x), 6.8)

        # ── Planck curve ──────────────────────────────────────────────────────
        planck_curve = axes.plot(
            planck_norm, x_range=[0.01, 7.5],
            color=TEAL, stroke_width=3,
        )
        self.play(Create(planck_curve), run_time=0.9)

        # ── Rayleigh-Jeans curve ──────────────────────────────────────────────
        rj_curve = axes.plot(
            rj_plot, x_range=[0.01, 7.0],
            color=CRIMSON, stroke_width=3,
        )
        self.play(Create(rj_curve), run_time=0.7)

        # ── UV catastrophe annotation ─────────────────────────────────────────
        # DIVERGES chip: right-centre quadrant of axes.
        # At data x≈7.1 (scene x≈1.1): RJ is clipped at scene y=1.69 (far above
        # chip y=0.50). Planck(7.1)≈0.002 → scene y≈−2.19 (far below). The x-axis
        # and y-axis strokes are at y≈−2.20 and x≈−1.40 respectively — neither
        # passes through (1.10, 0.50). No stroked VMobject at this position.
        uv_chip = LabelChip("DIVERGES", accent=CRIMSON, size=18)
        uv_chip.move_to(np.array([1.10, 0.50, 0]))
        self.play(GrowFromCenter(uv_chip), run_time=0.35)

        # ── legend chips at bottom (y=−2.80, within safe ±3.4) ──────────────
        # Curve labels are omitted; the legend chips identify both curves.
        chip_p  = LabelChip("Planck", accent=TEAL, size=17)
        chip_rj = LabelChip("Rayleigh–Jeans", accent=CRIMSON, size=17)
        legend  = VGroup(chip_p, chip_rj).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        legend.move_to([0, -2.80, 0])
        self.play(GrowFromCenter(chip_p), run_time=0.30)
        self.play(GrowFromCenter(chip_rj), run_time=0.30)

        # ── hold ─────────────────────────────────────────────────────────────
        elapsed = (0.5 + 0.7 + 0.25 + 0.9 + 0.7 + 0.35 + 0.30 + 0.30)
        self.wait(max(0.5, dur - elapsed))
