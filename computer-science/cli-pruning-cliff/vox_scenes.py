"""vox_scenes.py -- embedded-ai/youtube/cli-pruning-cliff
Reel: Find the Pruning Cliff with Claude Code
Palette: teardown (white ground, ink originals, crimson = cliff/damage)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  cliff zone / collapse
  SLATE   #545454  structure, neutral, unstructured pruning curve

Gate W colour rules (teardown on GROUND #FFFFFF):
  INK on GROUND -> contrast ~21:1 (AAA)
  CRIMSON on GROUND -> non-text shape fill only; white-on-CRIMSON chip = OK
  No GOLD text. No chapter references.

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

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass
_DEFAULTS = {"B01": 14.0, "B04": 17.0, "B06": 12.0, "B07": 11.0, "B08": 10.0}
def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))

# ── coordinate mapping ─────────────────────────────────────────────────────────
# x axis: pruning rate 0->90% -> scene x -5.5 -> 5.5
# y axis: accuracy 0->100% -> scene y -3.0 -> 2.8

X_LEFT, X_RIGHT = -5.5, 5.5
Y_BOT, Y_TOP = -3.0, 2.8

def _prune_x(pct):
    return X_LEFT + (pct / 90.0) * (X_RIGHT - X_LEFT)

def _acc_y(acc):
    return Y_BOT + (acc / 100.0) * (Y_TOP - Y_BOT)

# Data points: pruning rate %, accuracy %
PRUNE_RATES = np.array([0,   10,  20,   30,   40,   50,   60,   70,   80,   90])
ACCURACY    = np.array([88,  88,  87.5, 86,   84,   82,   80,   73,   55,   20])

def _interp_acc(pct):
    return float(np.interp(pct, PRUNE_RATES, ACCURACY))

def _struct_pt(t):
    """t in [0,1] -> scene point along structured pruning curve."""
    pct = t * 90.0
    acc = _interp_acc(pct)
    return np.array([_prune_x(pct), _acc_y(acc), 0.0])

def _unstruct_pt(t):
    """Unstructured pruning -- same accuracy shape but slightly different."""
    pct = t * 90.0
    acc = _interp_acc(pct) + 0.5  # slightly better accuracy illusion
    acc = min(acc, 88.5)
    return np.array([_prune_x(pct), _acc_y(acc), 0.0])


# =============================================================================
# B01_Problem -- title card: pruning rate zones and accuracy cliff
# =============================================================================
class B01_Problem(Scene):
    """Title card: flat to 20%, cliff at 70%, three zones framed."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("THE PRUNING CLIFF", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_safe = LabelChip("0-40% SAFE", accent=INK, size=22)
        chip_safe.move_to([-3.0, 1.9, 0])

        chip_cliff = LabelChip(">70% CLIFF", accent=CRIMSON, size=22)
        chip_cliff.move_to([3.0, 1.9, 0])

        self.play(GrowFromCenter(chip_safe), GrowFromCenter(chip_cliff), run_time=0.5)

        sub = Text("structured channel pruning  ·  accuracy vs pruning rate",
                   font=DISPLAY, color=INK, font_size=20)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_sw = LabelChip("20-40% SWEET SPOT", accent=SLATE, size=22)
        chip_sw.move_to([-2.8, -0.15, 0])

        chip_lat = LabelChip("LATENCY DROPS", accent=INK, size=22)
        chip_lat.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_sw), GrowFromCenter(chip_lat), run_time=0.5)

        q = Text("where is the cliff on your model?",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_PruningCliff -- accuracy vs pruning rate curve with zones
# =============================================================================
class B04_PruningCliff(Scene):
    """Curve drawn via ParametricFunction. Sweet spot band and cliff zone marked."""

    def construct(self):
        dur = _dur("B04")

        hdr = Text("ACCURACY vs PRUNING RATE", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X_LEFT, Y_BOT, 0], [X_RIGHT + 0.3, Y_BOT, 0],
                    stroke_width=1.5, color=INK)
        ax_y = Line([X_LEFT, Y_BOT, 0], [X_LEFT, Y_TOP + 0.3, 0],
                    stroke_width=1.5, color=INK)
        self.play(Create(ax_x), run_time=0.5)
        self.play(Create(ax_y), run_time=0.5)

        x_lbl = Text("pruning rate (%)", font=DISPLAY, color=INK, font_size=16)
        x_lbl.move_to([0.0, Y_BOT - 0.35, 0])
        y_lbl = Text("accuracy (%)", font=DISPLAY, color=INK, font_size=16)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([X_LEFT - 0.6, 0.0, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── x-axis tick labels ──────────────────────────────────────────────
        for pct in [0, 20, 40, 60, 70, 90]:
            t = Text(str(pct), font=DISPLAY, color=INK, font_size=14)
            t.move_to([_prune_x(pct), Y_BOT - 0.22, 0])
            self.play(FadeIn(t), run_time=0.15)

        # ── sweet-spot shade band (20-40%, SLATE rectangle) ──────────────────
        sw_x0 = _prune_x(20)
        sw_x1 = _prune_x(40)
        sw_w  = sw_x1 - sw_x0
        sw_h  = Y_TOP - Y_BOT
        sw_band = Rectangle(width=sw_w, height=sw_h,
                            fill_color=SLATE, fill_opacity=0.12, stroke_width=0)
        sw_band.move_to([(sw_x0 + sw_x1) / 2, (Y_BOT + Y_TOP) / 2, 0])
        self.play(Create(sw_band), run_time=0.5)

        sweet_chip = LabelChip("SWEET SPOT", accent=SLATE, size=16)
        sweet_chip.move_to([(sw_x0 + sw_x1) / 2, Y_TOP - 0.3, 0])
        self.play(GrowFromCenter(sweet_chip), run_time=0.3)

        # ── cliff zone shade band (>70%, CRIMSON rectangle) ──────────────────
        cl_x0 = _prune_x(70)
        cl_x1 = X_RIGHT
        cl_w  = cl_x1 - cl_x0
        cl_band = Rectangle(width=cl_w, height=sw_h,
                            fill_color=CRIMSON, fill_opacity=0.10, stroke_width=0)
        cl_band.move_to([(cl_x0 + cl_x1) / 2, (Y_BOT + Y_TOP) / 2, 0])
        self.play(Create(cl_band), run_time=0.5)

        cliff_chip = LabelChip("CLIFF", accent=CRIMSON, size=16)
        cliff_chip.move_to([(cl_x0 + cl_x1) / 2, Y_TOP - 0.3, 0])
        self.play(GrowFromCenter(cliff_chip), run_time=0.3)

        # ── accuracy curve (INK) ──────────────────────────────────────────────
        curve = ParametricFunction(
            _struct_pt,
            t_range=[0.0, 1.0, 0.005],
            color=INK,
            stroke_width=2.5,
        )
        self.play(Create(curve), run_time=2.0)

        # Annotate key points
        pt70_chip = LabelChip("73% at 70%", accent=CRIMSON, size=16)
        pt70_chip.move_to([_prune_x(70) + 0.8, _acc_y(73) + 0.4, 0])
        self.play(GrowFromCenter(pt70_chip), run_time=0.35)

        elapsed = 0.4 + 0.5 + 0.5 + 0.3 + 6 * 0.15 + 0.5 + 0.3 + 0.5 + 0.3 + 2.0 + 0.35
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_PruningUnstructured -- two curves: structured (INK) + unstructured (SLATE)
# =============================================================================
class B06_PruningUnstructured(Scene):
    """Overlay unstructured pruning curve. Both curves look similar.
    Chips show STRUCTURED: latency drops vs UNSTRUCTURED: latency flat."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("STRUCTURED vs UNSTRUCTURED", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X_LEFT, Y_BOT, 0], [X_RIGHT + 0.3, Y_BOT, 0],
                    stroke_width=1.5, color=INK)
        ax_y = Line([X_LEFT, Y_BOT, 0], [X_LEFT, Y_TOP + 0.3, 0],
                    stroke_width=1.5, color=INK)
        self.play(Create(ax_x), run_time=0.4)
        self.play(Create(ax_y), run_time=0.4)

        x_lbl = Text("pruning rate (%)", font=DISPLAY, color=INK, font_size=16)
        x_lbl.move_to([0.0, Y_BOT - 0.35, 0])
        self.play(FadeIn(x_lbl), run_time=0.3)

        # ── structured pruning curve (INK) ────────────────────────────────────
        s_curve = ParametricFunction(
            _struct_pt,
            t_range=[0.0, 1.0, 0.005],
            color=INK,
            stroke_width=2.5,
        )
        self.play(Create(s_curve), run_time=1.5)

        # ── unstructured pruning curve (SLATE) ────────────────────────────────
        u_curve = ParametricFunction(
            _unstruct_pt,
            t_range=[0.0, 1.0, 0.005],
            color=SLATE,
            stroke_width=2.0,
        )
        self.play(Create(u_curve), run_time=1.5)

        # ── annotation chips ──────────────────────────────────────────────────
        chip_s = LabelChip("STRUCTURED: latency drops", accent=INK, size=18)
        chip_s.move_to([-2.5, -1.5, 0])
        self.play(GrowFromCenter(chip_s), run_time=0.4)

        chip_u = LabelChip("UNSTRUCTURED: latency flat", accent=SLATE, size=18)
        chip_u.move_to([2.5, -2.3, 0])
        self.play(GrowFromCenter(chip_u), run_time=0.4)

        foot = Text("dense GEMM ignores zeros in the weight matrix",
                    font=SERIF, color=INK, font_size=18)
        foot.move_to([0.0, -3.1, 0])
        self.play(FadeIn(foot), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.3 + 1.5 + 1.5 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- structured vs unstructured; sweet spot; cliff
# =============================================================================
class B07_Summary(Scene):
    """Recap: structured only buys latency; stay in sweet spot; cliff at 70%."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("unstructured pruning", font=DISPLAY, color=INK, font_size=22)
        row1.move_to([-2.2, 1.7, 0])
        chip1 = LabelChip("LATENCY FLAT", accent=SLATE, size=20)
        chip1.move_to([3.3, 1.7, 0])
        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip1), run_time=0.4)

        row2 = Text("structured pruning  20-40%", font=DISPLAY, color=INK, font_size=22)
        row2.move_to([-1.8, 0.7, 0])
        chip2 = LabelChip("SWEET SPOT", accent=INK, size=20)
        chip2.move_to([3.3, 0.7, 0])
        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)

        sep2 = Line([-5.5, 0.1, 0], [5.5, 0.1, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        row3 = Text("past 70%: distill to a smaller arch", font=DISPLAY, color=INK, font_size=22)
        row3.move_to([-1.5, -0.55, 0])
        chip3 = LabelChip("NOT MORE PRUNING", accent=CRIMSON, size=20)
        chip3.move_to([3.3, -0.55, 0])
        self.play(FadeIn(row3), run_time=0.4)
        self.play(GrowFromCenter(chip3), run_time=0.4)

        foot = Text("Benchmarks reward unstructured. Silicon rewards structured.",
                    font=SERIF, color=INK, font_size=20)
        foot.move_to([0.0, -1.5, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps card: sweep 20-70%, find the bend, switch to distillation at cliff."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· sweep your model 20-70% in 10% steps",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("plot accuracy at each step  ·  find where the curve bends",
                    font=SERIF, color=INK, font_size=17)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· past 60%: switch to distillation",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("distill onto a smaller arch  ·  more pruning past cliff = wasted fine-tune",
                    font=SERIF, color=INK, font_size=17)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
