"""vox_scenes.py -- embedded-ai/youtube/cli-compression-journey
Reel: The MobileNetV2-0.5 That Almost Fit
Palette: teardown (white ground, ink originals, crimson = over-ceiling/error)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  over-ceiling / order-penalty
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
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass
_DEFAULTS = {"B01": 14.0, "B04": 17.0, "B06": 12.0, "B07": 11.0, "B08": 10.0}
def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))


# =============================================================================
# B01_Problem -- MobileNetV2-0.5 misses all three ceilings on STM32H7
# =============================================================================
class B01_Problem(Scene):
    """Title card: the model passed selection but missed flash/SRAM/latency ceilings."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("COMPRESSION JOURNEY", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_target = LabelChip("STM32H7 TARGET", accent=SLATE, size=22)
        chip_target.move_to([-2.8, 1.9, 0])

        chip_miss = LabelChip("MISSED ALL 3 CEILINGS", accent=CRIMSON, size=22)
        chip_miss.move_to([2.8, 1.9, 0])

        self.play(GrowFromCenter(chip_target), GrowFromCenter(chip_miss), run_time=0.5)

        sub = Text("MobileNetV2-0.5  ·  89.8% accuracy  ·  FP32 baseline",
                   font=DISPLAY, color=INK, font_size=20)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_knob1 = LabelChip("QUANTIZE", accent=SLATE, size=22)
        chip_knob1.move_to([-3.5, -0.15, 0])

        chip_knob2 = LabelChip("PRUNE", accent=SLATE, size=22)
        chip_knob2.move_to([0.0, -0.15, 0])

        chip_knob3 = LabelChip("DISTILL", accent=INK, size=22)
        chip_knob3.move_to([3.5, -0.15, 0])

        self.play(GrowFromCenter(chip_knob1), GrowFromCenter(chip_knob2), GrowFromCenter(chip_knob3), run_time=0.5)

        q = Text("three knobs  ·  what order  ·  does the combination ship?",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_CompressionJourney -- 4 metrics x 4 states bar chart
# =============================================================================
class B04_CompressionJourney(Scene):
    """4 grouped bar columns: FLASH, SRAM, LATENCY, ACCURACY across 4 states.
    Ceiling lines shown. FP32 bars in CRIMSON (over ceiling), rest in INK.
    """

    def construct(self):
        dur = _dur("B04")

        # State data: flash_mb, sram_mb, latency_ms, accuracy_%
        STATES = [
            {"name": "FP32",     "flash": 4.0,  "sram": 1.2,  "lat": 320, "acc": 89.8},
            {"name": "INT8",     "flash": 1.0,  "sram": 0.8,  "lat": 320, "acc": 89.8},
            {"name": "+PRUNE",   "flash": 0.75, "sram": 0.6,  "lat": 240, "acc": 89.0},
            {"name": "+DISTILL", "flash": 0.75, "sram": 0.6,  "lat": 240, "acc": 90.6},
        ]
        CEILS = {"flash": 2.0, "sram": 1.0, "lat": 250, "acc": 88.0}

        # Metric columns at x = -4.5, -1.5, 1.5, 4.5
        COL_X = [-4.5, -1.5, 1.5, 4.5]
        METRICS = ["flash", "sram", "lat", "acc"]
        LABELS  = ["FLASH", "SRAM", "LATENCY", "ACCURACY"]
        # Normalization max for each metric (to scene height)
        MAXES = {"flash": 4.5, "sram": 1.5, "lat": 360, "acc": 100}

        Y_BOT = -2.2   # bottom of plot (raised to leave room for chips)
        Y_TOP =  2.5   # top of plot
        BAR_H_RANGE = Y_TOP - Y_BOT   # 4.7 units

        def metric_y(metric, val):
            return Y_BOT + (val / MAXES[metric]) * BAR_H_RANGE

        def ceil_y(metric):
            return metric_y(metric, CEILS[metric])

        # Header
        hdr = Text("COMPRESSION JOURNEY", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # Column labels
        for i, (lbl, cx) in enumerate(zip(LABELS, COL_X)):
            t = Text(lbl, font=DISPLAY, color=INK, font_size=16)
            t.move_to([cx, Y_TOP + 0.15, 0])
            self.play(FadeIn(t), run_time=0.2)

        # Ceiling lines
        for i, (metric, cx) in enumerate(zip(METRICS, COL_X)):
            cy = ceil_y(metric)
            cl = Line([cx - 0.55, cy, 0], [cx + 0.55, cy, 0],
                      stroke_width=1.5, color=CRIMSON)
            cl.set_stroke(opacity=0.7)
            self.play(Create(cl), run_time=0.3)

        # Draw bars for each state, one state at a time
        STATE_COLORS = [CRIMSON, INK, INK, INK]
        BAR_W = 0.22
        STATE_OFFSETS = [-0.33, -0.11, 0.11, 0.33]

        elapsed = 0.4 + 4 * 0.2 + 4 * 0.3

        for si, state in enumerate(STATES):
            col = STATE_COLORS[si]
            for mi, (metric, cx) in enumerate(zip(METRICS, COL_X)):
                val = state[metric]
                bar_top = metric_y(metric, val)
                bar_height = bar_top - Y_BOT
                # Check if over ceiling
                if val > CEILS[metric]:
                    bar_col = CRIMSON
                else:
                    bar_col = INK
                bar_cx = cx + STATE_OFFSETS[si]
                rect = Rectangle(
                    width=BAR_W,
                    height=max(bar_height, 0.05),
                    fill_color=bar_col,
                    fill_opacity=0.85,
                    stroke_width=0,
                )
                rect.move_to([bar_cx, Y_BOT + max(bar_height, 0.05) / 2, 0])
                self.play(Create(rect), run_time=0.25)
                elapsed += 0.25

            # State label chip after all 4 bars for that state
            chip = LabelChip(state["name"], accent=SLATE, size=16)
            chip.move_to([COL_X[0] + STATE_OFFSETS[si], Y_BOT - 0.45, 0])
            self.play(GrowFromCenter(chip), run_time=0.3)
            elapsed += 0.3

        # Ship state chip
        ship_chip = LabelChip("SHIP: 0.75MB  240ms  90.6%", accent=INK, size=18)
        ship_chip.move_to([2.0, Y_BOT - 0.85, 0])
        self.play(GrowFromCenter(ship_chip), run_time=0.4)
        elapsed += 0.4

        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_CompressionOrder -- order matters: quantize->prune vs prune->quantize
# =============================================================================
class B06_CompressionOrder(Scene):
    """Two bars: quantize-then-prune (CRIMSON, 88.1%) vs prune-then-quantize (INK, 90.6%)."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("ORDER MATTERS", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.7, 0], [5.5, 2.7, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        # Axis
        ax_y = Line([-1.0, -2.5, 0], [-1.0, 2.4, 0], stroke_width=1.5, color=INK)
        self.play(Create(ax_y), run_time=0.4)

        y_lbl = Text("accuracy %", font=DISPLAY, color=INK, font_size=18)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([-1.7, 0.0, 0])
        self.play(FadeIn(y_lbl), run_time=0.3)

        # Accuracy range: 85 -> 92 mapped to y -2.5 -> 2.4
        Y_BOT, Y_TOP = -2.5, 2.4
        ACC_MIN, ACC_MAX = 85.0, 92.0

        def acc_y(a):
            return Y_BOT + (a - ACC_MIN) / (ACC_MAX - ACC_MIN) * (Y_TOP - Y_BOT)

        # Ceiling line at 88%
        ceil_y = acc_y(88.0)
        ceil_line = Line([-1.0, ceil_y, 0], [6.0, ceil_y, 0],
                         stroke_width=1.5, color=CRIMSON)
        ceil_line.set_stroke(opacity=0.6)
        self.play(Create(ceil_line), run_time=0.3)

        ceil_lbl = Text("ceiling  88.0%", font=DISPLAY, color=CRIMSON, font_size=16)
        ceil_lbl.move_to([4.5, ceil_y + 0.25, 0])
        self.play(FadeIn(ceil_lbl), run_time=0.3)

        # Bar 1: quantize -> prune, acc=88.1% (CRIMSON, barely above ceiling)
        acc1 = 88.1
        h1 = acc_y(acc1) - Y_BOT
        bar1 = Rectangle(width=1.4, height=h1,
                         fill_color=CRIMSON, fill_opacity=0.85, stroke_width=0)
        bar1.move_to([0.7, Y_BOT + h1 / 2, 0])
        self.play(Create(bar1), run_time=0.7)

        lbl1 = LabelChip("QUANTIZE->PRUNE", accent=CRIMSON, size=18)
        lbl1.move_to([0.7, Y_BOT - 0.45, 0])
        self.play(GrowFromCenter(lbl1), run_time=0.35)

        val1 = Text("88.1%", font=DISPLAY, color=INK, font_size=20)
        val1.move_to([0.7, acc_y(acc1) + 0.35, 0])
        self.play(FadeIn(val1), run_time=0.3)

        # Bar 2: prune -> quantize, acc=90.6% (INK)
        acc2 = 90.6
        h2 = acc_y(acc2) - Y_BOT
        bar2 = Rectangle(width=1.4, height=h2,
                         fill_color=INK, fill_opacity=0.85, stroke_width=0)
        bar2.move_to([3.5, Y_BOT + h2 / 2, 0])
        self.play(Create(bar2), run_time=0.7)

        lbl2 = LabelChip("PRUNE->QUANTIZE", accent=INK, size=18)
        lbl2.move_to([3.5, Y_BOT - 0.45, 0])
        self.play(GrowFromCenter(lbl2), run_time=0.35)

        val2 = Text("90.6%", font=DISPLAY, color=INK, font_size=20)
        val2.move_to([3.5, acc_y(acc2) + 0.35, 0])
        self.play(FadeIn(val2), run_time=0.3)

        # Delta label
        delta = Text("2.5 pt spread from sequence alone", font=SERIF, color=INK, font_size=20)
        delta.move_to([2.0, -3.1, 0])
        self.play(FadeIn(delta), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.3 + 0.3 + 0.3 + 0.7 + 0.35 + 0.3 + 0.7 + 0.35 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- three-knob sequence + ship state
# =============================================================================
class B07_Summary(Scene):
    """Recap: quantize -> prune -> distill, in order. Ship state metrics."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("quantize  ->  prune  ->  distill", font=DISPLAY, color=INK, font_size=24)
        row1.move_to([0.0, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.4)

        chip_order = LabelChip("ORDER MATTERS", accent=CRIMSON, size=22)
        chip_order.move_to([0.0, 0.85, 0])
        self.play(GrowFromCenter(chip_order), run_time=0.4)

        sep2 = Line([-5.5, 0.3, 0], [5.5, 0.3, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        ship_row = Text("ship state: 0.75 MB flash  ·  0.6 MB SRAM  ·  240 ms  ·  90.6%",
                        font=DISPLAY, color=INK, font_size=20)
        ship_row.move_to([0.0, -0.3, 0])
        self.play(FadeIn(ship_row), run_time=0.4)

        chip_ship = LabelChip("SHIPS", accent=INK, size=22)
        chip_ship.move_to([0.0, -1.1, 0])
        self.play(GrowFromCenter(chip_ship), run_time=0.4)

        foot = Text("Pruning earned the fit. Distillation earned the margin.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -1.95, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps card: run your param count, add distillation if needed, mind the order."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· run your param count through the four-state table",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("compare flash / SRAM / latency / accuracy against your ceilings",
                    font=SERIF, color=INK, font_size=17)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· add distillation if pruning alone falls short",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("always prune before quantize  ·  2.5 pt is not a rounding error",
                    font=SERIF, color=INK, font_size=17)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
