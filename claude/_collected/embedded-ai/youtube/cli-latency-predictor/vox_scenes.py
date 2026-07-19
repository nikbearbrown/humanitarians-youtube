"""vox_scenes.py -- embedded-ai/youtube/cli-latency-predictor
Reel: Build a Latency Predictor with Claude Code
Palette: teardown (white ground, ink originals, crimson = dominant stage/bottleneck)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  dominant bottleneck stage
  SLATE   #545454  non-dominant stages, neutral chips

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


# =============================================================================
# B01_Problem -- title card: four pipeline stages, one dominates
# =============================================================================
class B01_Problem(Scene):
    """Title card: four stages; the bottleneck varies; wasted week framed."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("LATENCY PREDICTOR", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_q = LabelChip("HOW FAST IS MY MODEL?", accent=SLATE, size=22)
        chip_q.move_to([-2.5, 1.9, 0])

        chip_4 = LabelChip("4 ANSWERS", accent=INK, size=22)
        chip_4.move_to([3.0, 1.9, 0])

        self.play(GrowFromCenter(chip_q), GrowFromCenter(chip_4), run_time=0.5)

        sub = Text("weight load  ·  compute  ·  mem movement  ·  overhead",
                   font=DISPLAY, color=INK, font_size=20)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_mem = LabelChip("MEMORY-BOUND", accent=CRIMSON, size=22)
        chip_mem.move_to([-2.8, -0.15, 0])

        chip_comp = LabelChip("COMPUTE-BOUND", accent=SLATE, size=22)
        chip_comp.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_mem), GrowFromCenter(chip_comp), run_time=0.5)

        q = Text("which stage is your bottleneck?",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_Latency -- Gantt chart of FP32 pipeline stages
# =============================================================================
class B04_Latency(Scene):
    """4 horizontal bars (Gantt) filling left to right.
    FP32 memory-bound model: weight_load=45ms dominant (CRIMSON), others SLATE.
    """

    def construct(self):
        dur = _dur("B04")

        # Stage data: name, ms, is_dominant
        FP32_STAGES = [
            ("WEIGHT LOAD", 45, True),
            ("COMPUTE",     12, False),
            ("MEM MOVE",    38, False),
            ("OVERHEAD",     5, False),
        ]
        TOTAL_MS = sum(s[1] for s in FP32_STAGES)  # 100ms

        hdr = Text("FP32  PIPELINE  BREAKDOWN", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # Gantt layout
        # X: time axis, 0->100ms mapped to -5.5->5.5
        # Y: 4 rows at y = 1.5, 0.5, -0.5, -1.5
        X_L, X_R = -5.5, 5.5
        ROW_Y = [1.5, 0.5, -0.5, -1.5]
        BAR_H = 0.7

        def ms_to_x(ms):
            return X_L + (ms / TOTAL_MS) * (X_R - X_L)

        # X axis
        ax = Line([X_L, -2.3, 0], [X_R, -2.3, 0], stroke_width=1.5, color=INK)
        self.play(Create(ax), run_time=0.4)

        x_lbl = Text("time (ms)", font=DISPLAY, color=INK, font_size=16)
        x_lbl.move_to([0.0, -2.6, 0])
        self.play(FadeIn(x_lbl), run_time=0.25)

        elapsed = 0.4 + 0.25 + 0.4

        # Draw stages
        t_offset = 0
        for (name, ms, dom), ry in zip(FP32_STAGES, ROW_Y):
            col = CRIMSON if dom else SLATE

            # Row label
            lbl = Text(name, font=DISPLAY, color=INK, font_size=16)
            lbl.move_to([X_L - 0.6, ry, 0])
            # Place it just to the left of the bar area -- adjust x to be inside safe area
            lbl2 = Text(name, font=DISPLAY, color=INK, font_size=14)
            lbl2.move_to([-6.0, ry, 0])
            self.play(FadeIn(lbl2), run_time=0.2)
            elapsed += 0.2

            # Bar
            x0 = ms_to_x(t_offset)
            x1 = ms_to_x(t_offset + ms)
            bw = x1 - x0
            bar = Rectangle(width=bw, height=BAR_H,
                             fill_color=col, fill_opacity=0.8, stroke_width=0)
            bar.move_to([(x0 + x1) / 2, ry, 0])
            self.play(Create(bar), run_time=0.5)
            elapsed += 0.5

            # ms label inside or next to bar
            ms_t = Text(f"{ms}ms", font=DISPLAY, color=INK, font_size=14)
            ms_t.move_to([(x0 + x1) / 2, ry + BAR_H / 2 + 0.2, 0])
            self.play(FadeIn(ms_t), run_time=0.2)
            elapsed += 0.2

            t_offset += ms

        # Total chip
        total_chip = LabelChip(f"TOTAL: {TOTAL_MS}ms", accent=INK, size=20)
        total_chip.move_to([0.0, -2.9, 0])
        self.play(GrowFromCenter(total_chip), run_time=0.4)
        elapsed += 0.4

        # Dominant annotation
        dom_chip = LabelChip("WEIGHT LOAD DOMINATES", accent=CRIMSON, size=18)
        dom_chip.move_to([3.0, 1.5, 0])
        self.play(GrowFromCenter(dom_chip), run_time=0.35)
        elapsed += 0.35

        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_LatencyInt8 -- same Gantt for INT8 version; weight load shrinks 4x
# =============================================================================
class B06_LatencyInt8(Scene):
    """INT8 Gantt: weight load 11ms, compute 12ms (now dominant), mem 10ms, oh 5ms.
    Total 38ms. Chip: INT8: 38ms vs FP32: 100ms.
    """

    def construct(self):
        dur = _dur("B06")

        INT8_STAGES = [
            ("WEIGHT LOAD", 11, False),
            ("COMPUTE",     12, True),   # now dominant
            ("MEM MOVE",    10, False),
            ("OVERHEAD",     5, False),
        ]
        TOTAL_MS = sum(s[1] for s in INT8_STAGES)  # 38ms

        hdr = Text("INT8  PIPELINE  BREAKDOWN", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # Same Gantt layout as B04
        X_L, X_R = -5.5, 5.5
        ROW_Y = [1.5, 0.5, -0.5, -1.5]
        BAR_H = 0.7
        TOTAL_NORM = 38.0  # normalize x axis to INT8 total

        def ms_to_x(ms):
            return X_L + (ms / TOTAL_NORM) * (X_R - X_L)

        ax = Line([X_L, -2.3, 0], [X_R, -2.3, 0], stroke_width=1.5, color=INK)
        self.play(Create(ax), run_time=0.4)

        x_lbl = Text("time (ms)", font=DISPLAY, color=INK, font_size=16)
        x_lbl.move_to([0.0, -2.6, 0])
        self.play(FadeIn(x_lbl), run_time=0.25)

        elapsed = 0.4 + 0.25 + 0.4

        t_offset = 0
        for (name, ms, dom), ry in zip(INT8_STAGES, ROW_Y):
            col = CRIMSON if dom else SLATE

            lbl2 = Text(name, font=DISPLAY, color=INK, font_size=14)
            lbl2.move_to([-6.0, ry, 0])
            self.play(FadeIn(lbl2), run_time=0.2)
            elapsed += 0.2

            x0 = ms_to_x(t_offset)
            x1 = ms_to_x(t_offset + ms)
            bw = x1 - x0
            bar = Rectangle(width=bw, height=BAR_H,
                             fill_color=col, fill_opacity=0.8, stroke_width=0)
            bar.move_to([(x0 + x1) / 2, ry, 0])
            self.play(Create(bar), run_time=0.5)
            elapsed += 0.5

            ms_t = Text(f"{ms}ms", font=DISPLAY, color=INK, font_size=14)
            ms_t.move_to([(x0 + x1) / 2, ry + BAR_H / 2 + 0.2, 0])
            self.play(FadeIn(ms_t), run_time=0.2)
            elapsed += 0.2

            t_offset += ms

        # Total chip
        total_chip = LabelChip(f"INT8: {TOTAL_MS}ms vs FP32: 100ms", accent=INK, size=18)
        total_chip.move_to([0.0, -2.9, 0])
        self.play(GrowFromCenter(total_chip), run_time=0.4)
        elapsed += 0.4

        # New dominant annotation
        dom_chip = LabelChip("COMPUTE NOW DOMINANT", accent=CRIMSON, size=18)
        dom_chip.move_to([3.0, 0.5, 0])
        self.play(GrowFromCenter(dom_chip), run_time=0.35)
        elapsed += 0.35

        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- memory-bound vs compute-bound: which knob to turn
# =============================================================================
class B07_Summary(Scene):
    """Recap: memory-bound -> quantize; compute-bound -> prune; wasted week warning."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("memory-bound dominant stage", font=DISPLAY, color=INK, font_size=22)
        row1.move_to([-1.8, 1.7, 0])
        chip1 = LabelChip("QUANTIZE", accent=INK, size=20)
        chip1.move_to([3.8, 1.7, 0])
        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip1), run_time=0.4)

        row2 = Text("compute-bound dominant stage", font=DISPLAY, color=INK, font_size=22)
        row2.move_to([-1.8, 0.7, 0])
        chip2 = LabelChip("PRUNE OR FASTER CHIP", accent=SLATE, size=20)
        chip2.move_to([3.5, 0.7, 0])
        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)

        sep2 = Line([-5.5, 0.1, 0], [5.5, 0.1, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_warn = LabelChip("WRONG STAGE = WASTED WEEK", accent=CRIMSON, size=20)
        chip_warn.move_to([0.0, -0.55, 0])
        self.play(GrowFromCenter(chip_warn), run_time=0.4)

        foot = Text("The stage breakdown tells you. The total latency doesn't.",
                    font=SERIF, color=INK, font_size=20)
        foot.move_to([0.0, -1.45, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps card: profiler for MACs+bytes, datasheet for GFLOP/s+bw, read dominant stage."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· get MACs + weight bytes from a model profiler",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("get GFLOP/s + memory bandwidth from the target datasheet",
                    font=SERIF, color=INK, font_size=17)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· read the dominant stage, not the total",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("dominant stage names the knob  ·  total latency doesn't",
                    font=SERIF, color=INK, font_size=17)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
