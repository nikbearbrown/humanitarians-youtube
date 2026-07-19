"""vox_scenes.py — embedded-ai/youtube/cli-roofline
Reel: The Roofline: Is Your Model Compute- or Memory-Bound?
Palette: teardown (white ground, ink originals, crimson = damage/problem)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  operating point / problem
  SLATE   #545454  structure, neutral chips

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
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

_DEFAULTS = {"B01": 14.0, "B04": 17.0, "B06": 12.0, "B07": 11.0, "B08": 10.0}
def _dur(bid):
    return DUR.get(bid, _DEFAULTS.get(bid, 10.0))

# ── roofline parameters ────────────────────────────────────────────────────────
PEAK_GFLOPS = 1.0   # target peak compute (GFLOP/s)
BANDWIDTH   = 2.0   # memory bandwidth (GB/s)
RIDGE_AI    = PEAK_GFLOPS / BANDWIDTH  # 0.5 FLOP/byte

# ── scene coordinate mapping ───────────────────────────────────────────────────
# x axis: arithmetic intensity (FLOP/byte), range [0.05, 1.5] -> scene [-5.5, 5.5]
# y axis: attainable GFLOP/s, range [0, 1.2] -> scene [-2.8, 2.8]
AI_MIN, AI_MAX = 0.05, 1.5
PERF_MIN, PERF_MAX = 0.0, 1.2

X_ORIGIN = -5.5
Y_ORIGIN = -2.8
X_RANGE  = 11.0
Y_RANGE  = 5.6

def _ai_to_x(ai):
    return X_ORIGIN + (ai - AI_MIN) / (AI_MAX - AI_MIN) * X_RANGE

def _perf_to_y(perf):
    return Y_ORIGIN + (perf - PERF_MIN) / (PERF_MAX - PERF_MIN) * Y_RANGE

def _attainable(ai):
    return min(BANDWIDTH * ai, PEAK_GFLOPS)


# =============================================================================
# B01_Problem — title card: same FLOPs, wildly different speed; roofline intro
# =============================================================================
class B01_Problem(Scene):
    """Title card: same FLOPs, different speed; memory bus is the hidden variable."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("THE ROOFLINE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_flops = LabelChip("SAME FLOP COUNT", accent=SLATE, size=22)
        chip_flops.move_to([-2.8, 1.9, 0])

        chip_speed = LabelChip("WILDLY DIFFERENT SPEED", accent=CRIMSON, size=22)
        chip_speed.move_to([2.8, 1.9, 0])

        self.play(GrowFromCenter(chip_flops), GrowFromCenter(chip_speed), run_time=0.5)

        sub = Text("the memory bus is the hidden bottleneck",
                   font=DISPLAY, color=INK, font_size=20)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_mem = LabelChip("MEMORY-BOUND", accent=SLATE, size=22)
        chip_mem.move_to([-2.8, -0.15, 0])

        chip_comp = LabelChip("COMPUTE-BOUND", accent=INK, size=22)
        chip_comp.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_mem), GrowFromCenter(chip_comp), run_time=0.5)

        q = Text("which bottleneck are you actually fighting?",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_Roofline — roofline plot with FP32 operating point (memory-bound)
# =============================================================================
class B04_Roofline(Scene):
    """Roofline: memory-bandwidth slope, compute ceiling, ridge, FP32 point."""

    def construct(self):
        dur = _dur("B04")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("ROOFLINE PLOT", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X_ORIGIN, Y_ORIGIN, 0], [X_ORIGIN + X_RANGE + 0.3, Y_ORIGIN, 0],
                    stroke_width=1.5, color=INK)
        ax_y = Line([X_ORIGIN, Y_ORIGIN, 0], [X_ORIGIN, Y_ORIGIN + Y_RANGE + 0.3, 0],
                    stroke_width=1.5, color=INK)
        self.play(Create(ax_x), run_time=0.5)
        self.play(Create(ax_y), run_time=0.5)

        # axis labels
        x_lbl = Text("Arithmetic Intensity (FLOP/byte)", font=DISPLAY, color=INK, font_size=16)
        x_lbl.move_to([0.0, -3.25, 0])
        y_lbl = Text("GFLOP/s", font=DISPLAY, color=INK, font_size=16)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([-5.8, 0.0, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── memory-bandwidth slope (SLATE) ────────────────────────────────────
        # From AI_MIN to ridge (0.5)
        slope_start = [_ai_to_x(AI_MIN), _perf_to_y(_attainable(AI_MIN)), 0]
        slope_end   = [_ai_to_x(RIDGE_AI), _perf_to_y(_attainable(RIDGE_AI)), 0]
        mem_slope = Line(slope_start, slope_end, stroke_width=2.5, color=SLATE)
        self.play(Create(mem_slope), run_time=0.8)

        mem_lbl = Text("memory bandwidth (2 GB/s)", font=DISPLAY, color=SLATE, font_size=16)
        mem_lbl.move_to([_ai_to_x(0.2), _perf_to_y(0.55), 0])
        self.play(FadeIn(mem_lbl), run_time=0.3)

        # ── compute ceiling (INK) ─────────────────────────────────────────────
        ceil_start = [_ai_to_x(RIDGE_AI), _perf_to_y(PEAK_GFLOPS), 0]
        ceil_end   = [_ai_to_x(AI_MAX), _perf_to_y(PEAK_GFLOPS), 0]
        comp_ceil = Line(ceil_start, ceil_end, stroke_width=2.5, color=INK)
        self.play(Create(comp_ceil), run_time=0.8)

        ceil_lbl = Text("peak compute (1 GFLOP/s)", font=DISPLAY, color=INK, font_size=16)
        ceil_lbl.move_to([_ai_to_x(1.0), _perf_to_y(1.08), 0])
        self.play(FadeIn(ceil_lbl), run_time=0.3)

        # ── ridge point ───────────────────────────────────────────────────────
        ridge_x = _ai_to_x(RIDGE_AI)
        ridge_y = _perf_to_y(PEAK_GFLOPS)
        ridge_dot = Dot([ridge_x, ridge_y, 0], color=INK, radius=0.12)
        self.play(GrowFromCenter(ridge_dot), run_time=0.4)

        ridge_chip = LabelChip("RIDGE  0.5 FLOP/byte", accent=INK, size=18)
        ridge_chip.move_to([ridge_x - 1.5, ridge_y + 0.5, 0])
        self.play(GrowFromCenter(ridge_chip), run_time=0.4)

        # ── FP32 operating point (CRIMSON, memory-bound) ──────────────────────
        fp32_ai   = 0.2
        fp32_perf = _attainable(fp32_ai)
        fp32_x    = _ai_to_x(fp32_ai)
        fp32_y    = _perf_to_y(fp32_perf)
        fp32_dot  = Dot([fp32_x, fp32_y, 0], color=CRIMSON, radius=0.18)
        self.play(GrowFromCenter(fp32_dot), run_time=0.5)

        fp32_chip = LabelChip("FP32  MEMORY-BOUND", accent=CRIMSON, size=18)
        fp32_chip.move_to([fp32_x + 1.8, fp32_y - 0.55, 0])
        self.play(GrowFromCenter(fp32_chip), run_time=0.4)

        elapsed = 0.4 + 0.5 + 0.5 + 0.3 + 0.8 + 0.3 + 0.8 + 0.3 + 0.4 + 0.4 + 0.5 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_RooflineInt8 — same roofline, add INT8 point in compute-bound region
# =============================================================================
class B06_RooflineInt8(Scene):
    """Same roofline. FP32 dot (SLATE, before), then INT8 dot (INK, compute-bound)."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("ROOFLINE  --  INT8 SHIFT", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── redraw axes ───────────────────────────────────────────────────────
        ax_x = Line([X_ORIGIN, Y_ORIGIN, 0], [X_ORIGIN + X_RANGE + 0.3, Y_ORIGIN, 0],
                    stroke_width=1.5, color=INK)
        ax_y = Line([X_ORIGIN, Y_ORIGIN, 0], [X_ORIGIN, Y_ORIGIN + Y_RANGE + 0.3, 0],
                    stroke_width=1.5, color=INK)
        self.play(Create(ax_x), run_time=0.4)
        self.play(Create(ax_y), run_time=0.4)

        # ── memory slope ──────────────────────────────────────────────────────
        slope_start = [_ai_to_x(AI_MIN), _perf_to_y(_attainable(AI_MIN)), 0]
        slope_end   = [_ai_to_x(RIDGE_AI), _perf_to_y(_attainable(RIDGE_AI)), 0]
        mem_slope = Line(slope_start, slope_end, stroke_width=2.5, color=SLATE)
        self.play(Create(mem_slope), run_time=0.5)

        # ── compute ceiling ───────────────────────────────────────────────────
        ceil_start = [_ai_to_x(RIDGE_AI), _perf_to_y(PEAK_GFLOPS), 0]
        ceil_end   = [_ai_to_x(AI_MAX), _perf_to_y(PEAK_GFLOPS), 0]
        comp_ceil = Line(ceil_start, ceil_end, stroke_width=2.5, color=INK)
        self.play(Create(comp_ceil), run_time=0.5)

        # ── FP32 dot (SLATE, before) ──────────────────────────────────────────
        fp32_ai   = 0.2
        fp32_perf = _attainable(fp32_ai)
        fp32_dot  = Dot([_ai_to_x(fp32_ai), _perf_to_y(fp32_perf), 0],
                        color=SLATE, radius=0.15)
        self.play(GrowFromCenter(fp32_dot), run_time=0.4)

        fp32_chip = LabelChip("FP32  BEFORE", accent=SLATE, size=18)
        fp32_chip.move_to([_ai_to_x(fp32_ai) + 1.6, _perf_to_y(fp32_perf) - 0.5, 0])
        self.play(GrowFromCenter(fp32_chip), run_time=0.3)

        # ── INT8 dot (INK, compute-bound) ─────────────────────────────────────
        int8_ai   = 0.8
        int8_perf = _attainable(int8_ai)
        int8_dot  = Dot([_ai_to_x(int8_ai), _perf_to_y(int8_perf), 0],
                        color=INK, radius=0.18)
        self.play(GrowFromCenter(int8_dot), run_time=0.5)

        int8_chip = LabelChip("INT8  COMPUTE-BOUND", accent=INK, size=18)
        int8_chip.move_to([_ai_to_x(int8_ai) - 1.8, _perf_to_y(int8_perf) + 0.55, 0])
        self.play(GrowFromCenter(int8_chip), run_time=0.4)

        # ── region label ─────────────────────────────────────────────────────
        region_lbl = Text("int8 shifts 4x fewer bytes -> 4x higher AI",
                          font=SERIF, color=INK, font_size=18)
        region_lbl.move_to([0.5, -2.2, 0])
        self.play(FadeIn(region_lbl), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.5 + 0.5 + 0.4 + 0.3 + 0.5 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary — which knob to turn for each region
# =============================================================================
class B07_Summary(Scene):
    """Recap: memory-bound -> fix bandwidth; compute-bound -> fix MACs."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("memory-bound", font=DISPLAY, color=INK, font_size=24)
        row1.move_to([-2.5, 1.6, 0])
        chip1 = LabelChip("QUANTIZE OR FASTER BUS", accent=SLATE, size=20)
        chip1.move_to([3.0, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip1), run_time=0.4)

        row2 = Text("compute-bound", font=DISPLAY, color=INK, font_size=24)
        row2.move_to([-2.5, 0.6, 0])
        chip2 = LabelChip("PRUNE OR FASTER CHIP", accent=INK, size=20)
        chip2.move_to([3.0, 0.6, 0])
        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)

        sep2 = Line([-5.5, 0.0, 0], [5.5, 0.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        foot = Text("Optimizing the ceiling you are not under is wasted work.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -0.75, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps — action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps card: get datasheet numbers, profile model, plot the point."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· pull peak GFLOP/s + bandwidth from the datasheet",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("every MCU datasheet has both numbers",
                    font=SERIF, color=INK, font_size=18)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· profile MACs + bytes from your model",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("plot the operating point  ·  see which side of the ridge you land",
                    font=SERIF, color=INK, font_size=18)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
