"""vox_scenes.py — embedded-ai/youtube/cli-int8-mash
Reel: INT8 Rounding Mash — weights vs activations
Palette: teardown (white ground, ink originals, crimson = mash/damage)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text  (TEAL == INK in teardown)
  CRIMSON #C8102E  quantized / error / mash
  SLATE   #545454  structure, neutral chips

Gate W colour rules (teardown on GROUND #FFFFFF):
  INK on GROUND -> contrast ~21:1  (AAA)
  CRIMSON on GROUND -> non-text shape fill only; white-on-CRIMSON chip = OK
  No GOLD text.  No chapter references.

Gate A rules (IMPORTANT):
  Each .animate uses a single chained method.
  Every scene has real shape motion (Create / Transform / GrowFromCenter).
  Coords inside +-7.1 x, +-4.0 y; safe area +-6.3 x, +-3.4 y.
"""

import sys, json, pathlib, os, numpy as np

os.environ.setdefault("VOX_PALETTE", "teardown")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

# ── duration table ─────────────────────────────────────────────────────────
DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

_DEFAULTS = {"B01": 14.0, "B04": 17.0, "B06": 12.0, "B07": 11.0, "B08": 10.0}

def _dur(bid):
    return DUR.get(bid, _DEFAULTS.get(bid, 10.0))

# ── shared coordinate helpers ───────────────────────────────────────────────
SCALE_W = 3.0 / 255.0   # weight scale: (1.5 - (-1.5)) / 255 ≈ 0.01176

# Panel x extents (scene units)
PAN_L_X0, PAN_L_X1 = -6.0, -0.4   # left panel data region
PAN_R_X0, PAN_R_X1 =  0.4,  6.0   # right panel data region

# Activation display physical range (must contain both quantised levels 0 and SCALE_W)
ACT_Y_LO, ACT_Y_HI = -0.003, 0.016

def _act_scene_y(y_phys):
    return (y_phys - ACT_Y_LO) / (ACT_Y_HI - ACT_Y_LO) * 5.0 - 2.5

def _wt_scene_y(y_w):
    return y_w * (2.5 / 1.5)

def _scene_x_left(t):
    return PAN_L_X0 + t * (PAN_L_X1 - PAN_L_X0)

def _scene_x_right(t):
    return PAN_R_X0 + t * (PAN_R_X1 - PAN_R_X0)

# ── weight curve functions (t in [0, 1]) ───────────────────────────────────
def _wt_ink_pt(t):
    y = (0.9 * np.sin(3 * np.pi * t)
         + 0.4 * np.cos(7 * np.pi * t + 0.3)
         + 0.2 * np.sin(11 * np.pi * t + 0.7))
    y = float(np.clip(y, -1.5, 1.5))
    return np.array([_scene_x_left(t), _wt_scene_y(y), 0.0])

def _wt_quant_pt(t):
    y = (0.9 * np.sin(3 * np.pi * t)
         + 0.4 * np.cos(7 * np.pi * t + 0.3)
         + 0.2 * np.sin(11 * np.pi * t + 0.7))
    y = float(np.clip(y, -1.5, 1.5))
    q = float(np.clip(np.round(y / SCALE_W), -128, 127))
    yq = SCALE_W * q
    return np.array([_scene_x_left(t), _wt_scene_y(yq), 0.0])

# ── activation curve functions (t in [0, 1]) ───────────────────────────────
def _act_ink_pt(t):
    y = 0.0055 + 0.0045 * np.sin(2 * np.pi * t)
    return np.array([_scene_x_right(t), _act_scene_y(y), 0.0])

def _act_quant_pt(t):
    # Quantised with the WEIGHT scale — the mash
    y = 0.0055 + 0.0045 * np.sin(2 * np.pi * t)
    q = float(np.clip(np.round(y / SCALE_W), -128, 127))
    yq = SCALE_W * q
    return np.array([_scene_x_right(t), _act_scene_y(yq), 0.0])

def _act_perchan_pt(t):
    # Per-channel scale: (0.01 - 0.001) / 255
    SCALE_CH = 0.009 / 255.0
    y = 0.0055 + 0.0045 * np.sin(2 * np.pi * t)
    q = float(np.clip(np.round((y - 0.001) / SCALE_CH) - 128, -128, 127))
    yq = SCALE_CH * (q + 128) + 0.001
    return np.array([_scene_x_right(t), _act_scene_y(yq), 0.0])


# =============================================================================
# B01_Problem — INT8 as the enabling move; activation danger flagged
# =============================================================================
class B01_Problem(Scene):
    """Title card: 4x smaller / 4x faster enabling move, then the hazard."""

    def construct(self):
        dur = _dur("B01")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("INT8 QUANTIZATION", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── separator (required shape motion) ─────────────────────────────────
        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        # ── stat chips ────────────────────────────────────────────────────────
        chip_4x = LabelChip("4x SMALLER", accent=SLATE, size=22)
        chip_4x.move_to([-2.6, 1.9, 0])

        chip_fast = LabelChip("4x FASTER", accent=SLATE, size=22)
        chip_fast.move_to([2.6, 1.9, 0])

        self.play(GrowFromCenter(chip_4x), GrowFromCenter(chip_fast), run_time=0.5)

        sub = Text("float32 -> int8  ·  makes edge AI possible",
                   font=DISPLAY, color=INK, font_size=20)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        # ── second separator ──────────────────────────────────────────────────
        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        # ── hazard chips ──────────────────────────────────────────────────────
        chip_w = LabelChip("HARMLESS FOR WEIGHTS", accent=SLATE, size=22)
        chip_w.move_to([-2.5, -0.15, 0])

        chip_a = LabelChip("LETHAL FOR ACTIVATIONS", accent=CRIMSON, size=22)
        chip_a.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_w), GrowFromCenter(chip_a), run_time=0.5)

        # ── question footer ───────────────────────────────────────────────────
        q_line = Text("When does int8 mash the signal, and why?",
                      font=SERIF, color=INK, font_size=22)
        q_line.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q_line), run_time=0.5)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_QuantMash — two-panel: weight staircase (clean) vs activation mash
# =============================================================================
class B04_QuantMash(Scene):
    """Left panel: weights [-1.5, 1.5] quantised with SCALE_W -> 249 levels.
    Crimson staircase hugs the ink curve.
    Right panel: activations [0.001, 0.01] with the SAME weight scale -> 2 levels.
    Entire sine range narrower than one step; crimson collapses to two bars.
    """

    def construct(self):
        dur = _dur("B04")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("INT8 QUANTIZATION", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── panel divider ─────────────────────────────────────────────────────
        div = Line([0, -3.3, 0], [0, 2.9, 0], stroke_width=0.8, color=SLATE)
        div.set_stroke(color=SLATE, width=0.8, opacity=0.5)
        self.play(Create(div), run_time=0.3)

        # ── panel labels ──────────────────────────────────────────────────────
        lbl_w = Text("WEIGHTS  [-1.5, 1.5]", font=DISPLAY, color=INK, font_size=20)
        lbl_w.move_to([-3.2, 2.85, 0])

        lbl_a = Text("ACTIVATIONS  [0.001, 0.01]", font=DISPLAY, color=INK, font_size=20)
        lbl_a.move_to([3.2, 2.85, 0])

        self.play(FadeIn(lbl_w), FadeIn(lbl_a), run_time=0.3)

        # ── scale chips (same scale for both panels) ──────────────────────────
        sc_chip_l = LabelChip("SCALE 0.0118", accent=SLATE, size=20)
        sc_chip_l.move_to([-3.2, 2.45, 0])

        sc_chip_r = LabelChip("SAME SCALE 0.0118", accent=SLATE, size=20)
        sc_chip_r.move_to([3.2, 2.45, 0])

        self.play(GrowFromCenter(sc_chip_l), GrowFromCenter(sc_chip_r), run_time=0.4)

        # ── LEFT PANEL: original weight curve (ink) ───────────────────────────
        wt_curve = ParametricFunction(
            _wt_ink_pt,
            t_range=[0.0, 1.0, 0.002],
            color=INK,
            stroke_width=1.6,
        )
        self.play(Create(wt_curve), run_time=0.9)

        # crimson staircase — same function but quantised (249 tiny steps)
        wt_stair = ParametricFunction(
            _wt_quant_pt,
            t_range=[0.0, 1.0, 0.001],
            color=CRIMSON,
            stroke_width=1.4,
        )
        self.play(Create(wt_stair), run_time=1.0)

        # "249 LEVELS" chip — good result, ink accent
        ok_chip = LabelChip("249 LEVELS", accent=INK, size=20)
        ok_chip.move_to([-3.2, -2.95, 0])
        self.play(GrowFromCenter(ok_chip), run_time=0.35)

        # ── RIGHT PANEL: original activation sine (ink) ───────────────────────
        act_curve = ParametricFunction(
            _act_ink_pt,
            t_range=[0.0, 1.0, 0.002],
            color=INK,
            stroke_width=1.6,
        )
        self.play(Create(act_curve), run_time=0.9)

        # crimson step function — only 2 levels
        act_mash = ParametricFunction(
            _act_quant_pt,
            t_range=[0.0, 1.0, 0.001],
            color=CRIMSON,
            stroke_width=1.8,
        )
        self.play(Create(act_mash), run_time=0.8)

        # "2 LEVELS" chip — bad result, crimson accent
        mash_chip = LabelChip("2 LEVELS  MASH", accent=CRIMSON, size=20)
        mash_chip.move_to([3.2, -2.95, 0])
        self.play(GrowFromCenter(mash_chip), run_time=0.35)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.3 + 0.3 + 0.4 + 0.9 + 1.0 + 0.35 + 0.9 + 0.8 + 0.35
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_PerChannel — activation sine recovering with per-channel scale
# =============================================================================
class B06_PerChannel(Scene):
    """Start with the collapsed 2-bar crimson mash.
    Transform: crimson bars animate into a faithful per-channel staircase.
    The ink sine stays unchanged throughout — it's the ground truth.
    """

    def construct(self):
        dur = _dur("B06")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("PER-CHANNEL QUANTIZATION", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── panel label ───────────────────────────────────────────────────────
        lbl = Text("ACTIVATIONS  [0.001, 0.01]", font=DISPLAY, color=INK, font_size=22)
        lbl.move_to([0.0, 2.8, 0])
        self.play(FadeIn(lbl), run_time=0.3)

        # Re-centre curves: full-width panel
        def _act_ink_full(t):
            x = -5.8 + t * 11.6
            y = 0.0055 + 0.0045 * np.sin(2 * np.pi * t)
            return np.array([x, _act_scene_y(y), 0.0])

        def _act_mash_full(t):
            x = -5.8 + t * 11.6
            y = 0.0055 + 0.0045 * np.sin(2 * np.pi * t)
            q = float(np.clip(np.round(y / SCALE_W), -128, 127))
            yq = SCALE_W * q
            return np.array([x, _act_scene_y(yq), 0.0])

        def _act_ch_full(t):
            SCALE_CH = 0.009 / 255.0
            x = -5.8 + t * 11.6
            y = 0.0055 + 0.0045 * np.sin(2 * np.pi * t)
            q = float(np.clip(np.round((y - 0.001) / SCALE_CH) - 128, -128, 127))
            yq = SCALE_CH * (q + 128) + 0.001
            return np.array([x, _act_scene_y(yq), 0.0])

        # ── ink sine (ground truth, stays the whole scene) ────────────────────
        ink_sine = ParametricFunction(
            _act_ink_full,
            t_range=[0.0, 1.0, 0.002],
            color=INK,
            stroke_width=1.6,
        )
        self.play(Create(ink_sine), run_time=0.8)

        # ── start state: 2-bar mash ───────────────────────────────────────────
        mash_curve = ParametricFunction(
            _act_mash_full,
            t_range=[0.0, 1.0, 0.001],
            color=CRIMSON,
            stroke_width=1.8,
        )
        self.play(Create(mash_curve), run_time=0.6)

        mash_lbl = LabelChip("2 LEVELS  MASH", accent=CRIMSON, size=20)
        mash_lbl.move_to([0.0, -2.9, 0])
        self.play(GrowFromCenter(mash_lbl), run_time=0.3)
        self.wait(0.6)

        # ── transform: mash -> per-channel staircase ──────────────────────────
        ch_curve = ParametricFunction(
            _act_ch_full,
            t_range=[0.0, 1.0, 0.001],
            color=CRIMSON,
            stroke_width=1.6,
        )
        self.play(Transform(mash_curve, ch_curve), run_time=1.8)

        # swap label — ok_lbl at a distinct y so Gate W sees no text-on-text overlap
        ok_lbl = LabelChip("255 LEVELS  RECOVERED", accent=INK, size=20)
        ok_lbl.move_to([0.0, -1.9, 0])
        self.play(Transform(mash_lbl, ok_lbl), run_time=0.4)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.3 + 0.8 + 0.6 + 0.3 + 0.6 + 1.8 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary — one-scale mash vs per-channel preserved
# =============================================================================
class B07_Summary(Scene):
    """Recap card: one scale -> mash vs per-channel -> preserved."""

    def construct(self):
        dur = _dur("B07")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── separator (required shape motion) ─────────────────────────────────
        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        # ── row 1: mash case ──────────────────────────────────────────────────
        row1 = Text("one scale for all", font=DISPLAY, color=INK, font_size=24)
        row1.move_to([-2.0, 1.6, 0])

        chip_mash = LabelChip("MASH", accent=CRIMSON, size=22)
        chip_mash.move_to([3.2, 1.6, 0])

        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip_mash), run_time=0.4)

        # ── row 2: preserved case ─────────────────────────────────────────────
        row2 = Text("per-channel scale", font=DISPLAY, color=INK, font_size=24)
        row2.move_to([-2.0, 0.6, 0])

        chip_ok = LabelChip("PRESERVED", accent=INK, size=22)
        chip_ok.move_to([3.2, 0.6, 0])

        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip_ok), run_time=0.4)

        # ── second separator ──────────────────────────────────────────────────
        sep2 = Line([-5.5, 0.0, 0], [5.5, 0.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        # ── footer insight ────────────────────────────────────────────────────
        foot = Text("The denominator was wrong, not the bit-width.",
                    font=SERIF, color=INK, font_size=22)
        foot.move_to([0.0, -0.75, 0])
        self.play(FadeIn(foot), run_time=0.5)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps — action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps card: dump activations, verify per-channel in toolchain."""

    def construct(self):
        dur = _dur("B08")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── separator (required shape motion) ─────────────────────────────────
        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        # ── step 1 ────────────────────────────────────────────────────────────
        step1 = Text("· dump activation tensors from your model",
                     font=DISPLAY, color=INK, font_size=22)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("see which layers live near the rounding floor",
                    font=SERIF, color=INK, font_size=18)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        # ── step 2 ────────────────────────────────────────────────────────────
        step2 = Text("· verify per-channel in your deploy toolchain",
                     font=DISPLAY, color=INK, font_size=22)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("no per-channel  ·  that is where your accuracy went",
                    font=SERIF, color=INK, font_size=18)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        # ── bottom separator ──────────────────────────────────────────────────
        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        # ── hold ──────────────────────────────────────────────────────────────
        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
