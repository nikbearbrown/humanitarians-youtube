"""vox_scenes.py -- embedded-ai/youtube/cli-prune-benchmark
Reel: Structured vs Unstructured Pruning: Measure the Lie
Palette: teardown (white ground, ink originals, crimson = error/mash)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text  (TEAL == INK in teardown)
  CRIMSON #C8102E  quantized / error / mash
  SLATE   #545454  structure, neutral chips

Gate W colour rules (teardown on GROUND #FFFFFF):
  INK on GROUND -> contrast ~21:1  (AAA)
  CRIMSON on GROUND -> non-text shape fill only; white-on-CRIMSON chip = OK
  No GOLD text.  No chapter references.

Gate A rules:
  Each .animate uses a single chained method.
  Every scene has real shape motion (Create / Transform / GrowFromCenter).
  Coords inside +-7.1 x, +-4.0 y; safe area +-6.3 x, +-3.4 y.
  No Manim Axes class -- draw axes manually with Line().
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
_DEFAULTS = {"B01":14.0,"B04":17.0,"B06":12.0,"B07":11.0,"B08":10.0}
def _dur(bid): return DUR.get(bid,_DEFAULTS.get(bid,10.0))


# =============================================================================
# B01_Problem -- the unstructured pruning lie
# =============================================================================
class B01_Problem(Scene):
    """Title card: storage drops but SRAM + latency stay for unstructured;
    structured pruning drops all three."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("PRUNING BENCHMARK", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        # Unstructured row
        chip_u = LabelChip("UNSTRUCTURED 50%", accent=CRIMSON, size=22)
        chip_u.move_to([-2.5, 1.6, 0])
        self.play(GrowFromCenter(chip_u), run_time=0.4)

        row_u = Text("storage -50%   SRAM: same   latency: same",
                     font=DISPLAY, color=INK, font_size=19)
        row_u.move_to([1.8, 1.6, 0])
        self.play(FadeIn(row_u), run_time=0.4)

        sep2 = Line([-5.5, 1.1, 0], [5.5, 1.1, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        # Structured row
        chip_s = LabelChip("STRUCTURED 50%", accent=INK, size=22)
        chip_s.move_to([-2.5, 0.5, 0])
        self.play(GrowFromCenter(chip_s), run_time=0.4)

        row_s = Text("storage -75%   SRAM -50%   latency -48%",
                     font=DISPLAY, color=INK, font_size=19)
        row_s.move_to([1.8, 0.5, 0])
        self.play(FadeIn(row_s), run_time=0.4)

        sep3 = Line([-5.5, -0.15, 0], [5.5, -0.15, 0], stroke_width=0.8, color=SLATE)
        sep3.set_stroke(opacity=0.35)
        self.play(Create(sep3), run_time=0.3)

        foot = Text("Embedded kernels run dense GEMM -- zeros don't skip.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -0.9, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.5+0.4+0.4+0.3+0.4+0.4+0.3+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_PruneBenchmark -- 3 metric columns x 3 method bars
# =============================================================================
class B04_PruneBenchmark(Scene):
    """3 columns: STORAGE, SRAM, LATENCY.
    3 bars per column: Dense (SLATE), Unstructured (CRIMSON), Structured (INK).
    Key punchline: LATENCY column -- Unstructured bar same height as Dense.
    Illustrative data:
      Dense:        storage=5.6MB, SRAM=0.5MB, latency=100ms
      Unstructured: storage=2.8MB, SRAM=0.5MB, latency=100ms
      Structured:   storage=1.4MB, SRAM=0.25MB, latency=52ms
    """

    def construct(self):
        dur = _dur("B04")

        # ── header ────────────────────────────────────────────────────────────
        hdr = Text("PRUNE BENCHMARK", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── column setup ──────────────────────────────────────────────────────
        # Columns at x = -4.0, 0.0, 4.0
        col_labels = ["STORAGE", "SRAM", "LATENCY"]
        col_xs = [-4.0, 0.0, 4.0]
        col_max_vals = [5.6, 0.5, 100.0]

        # Data: [Dense, Unstructured, Structured]
        data = {
            "STORAGE":  [5.6, 2.8, 1.4],
            "SRAM":     [0.5, 0.5, 0.25],
            "LATENCY":  [100.0, 100.0, 52.0],
        }
        bar_colors = [SLATE, CRIMSON, INK]
        bar_width = 0.55
        bar_offsets = [-0.7, 0.0, 0.7]  # x offset within column

        # y mapping: 0 -> y=-2.5, max -> y=2.0
        Y_BOT = -2.5
        Y_TOP = 2.0
        bar_base_y = Y_BOT  # bars grow up from here

        def val_to_h(val, max_val):
            return (val / max_val) * (Y_TOP - Y_BOT)

        # ── column headers ────────────────────────────────────────────────────
        for lbl, cx in zip(col_labels, col_xs):
            t = Text(lbl, font=DISPLAY, color=INK, font_size=20)
            t.move_to([cx, 2.85, 0])
            self.play(FadeIn(t), run_time=0.25)

        # ── draw axis baselines ────────────────────────────────────────────────
        for cx in col_xs:
            ax = Line([cx - 1.2, Y_BOT, 0], [cx + 1.2, Y_BOT, 0],
                      stroke_width=1.0, color=SLATE)
            ax.set_stroke(opacity=0.5)
            self.play(Create(ax), run_time=0.2)

        # ── draw bars column by column ────────────────────────────────────────
        for col_idx, (lbl, cx) in enumerate(zip(col_labels, col_xs)):
            col_data = data[lbl]
            max_val = col_max_vals[col_idx]
            for bar_idx, (val, color, x_off) in enumerate(zip(col_data, bar_colors, bar_offsets)):
                h = val_to_h(val, max_val)
                bx = cx + x_off
                # Rectangle bottom-left corner, then center it
                rect = Rectangle(width=bar_width, height=h, color=color,
                                  fill_color=color, fill_opacity=0.85,
                                  stroke_width=0)
                rect.move_to([bx, bar_base_y + h / 2, 0])
                self.play(Create(rect), run_time=0.35)

        # ── method legend chips (below bars) ─────────────────────────────────
        chip_d = LabelChip("DENSE", accent=SLATE, size=18)
        chip_d.move_to([-5.5, -3.1, 0])

        chip_u = LabelChip("UNSTRUCTURED", accent=CRIMSON, size=18)
        chip_u.move_to([0.0, -3.1, 0])

        chip_s = LabelChip("STRUCTURED", accent=INK, size=18)
        chip_s.move_to([5.3, -3.1, 0])

        self.play(GrowFromCenter(chip_d), GrowFromCenter(chip_u), GrowFromCenter(chip_s), run_time=0.5)

        # ── punchline chip on LATENCY column ─────────────────────────────────
        punch = LabelChip("LATENCY: NO CHANGE", accent=CRIMSON, size=19)
        punch.move_to([4.0, 1.0, 0])
        self.play(GrowFromCenter(punch), run_time=0.4)

        elapsed = 0.4 + 3*0.25 + 3*0.2 + 9*0.35 + 0.5 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_PruneSparse -- 4 bars per column, hypothetical sparse kernel added
# =============================================================================
class B06_PruneSparse(Scene):
    """Same 3-column layout. 4th bar: hypothetical sparse kernel.
    Storage and SRAM match Structured. Latency matches Structured.
    Chip: IF SPARSE KERNEL EXISTED.
    Illustrative data -- 4th bar same as Structured for all metrics.
    """

    def construct(self):
        dur = _dur("B06")

        hdr = Text("HYPOTHETICAL SPARSE KERNEL", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        col_labels = ["STORAGE", "SRAM", "LATENCY"]
        col_xs = [-4.0, 0.0, 4.0]
        col_max_vals = [5.6, 0.5, 100.0]

        # 4 bars: Dense, Unstructured, Structured, Hypothetical Sparse
        data = {
            "STORAGE":  [5.6, 2.8, 1.4, 1.4],
            "SRAM":     [0.5, 0.5, 0.25, 0.25],
            "LATENCY":  [100.0, 100.0, 52.0, 52.0],
        }
        bar_colors = [SLATE, CRIMSON, INK, SLATE]
        bar_width = 0.42
        bar_offsets = [-1.0, -0.35, 0.3, 0.95]

        Y_BOT = -2.5
        Y_TOP = 2.0

        def val_to_h(val, max_val):
            return (val / max_val) * (Y_TOP - Y_BOT)

        # Column headers
        for lbl, cx in zip(col_labels, col_xs):
            t = Text(lbl, font=DISPLAY, color=INK, font_size=20)
            t.move_to([cx, 2.85, 0])
            self.play(FadeIn(t), run_time=0.2)

        # Axis baselines
        for cx in col_xs:
            ax = Line([cx - 1.5, Y_BOT, 0], [cx + 1.5, Y_BOT, 0],
                      stroke_width=1.0, color=SLATE)
            ax.set_stroke(opacity=0.5)
            self.play(Create(ax), run_time=0.2)

        # Draw first 3 bars per column (existing)
        for col_idx, (lbl, cx) in enumerate(zip(col_labels, col_xs)):
            col_data = data[lbl]
            max_val = col_max_vals[col_idx]
            for bar_idx in range(3):
                val = col_data[bar_idx]
                color = bar_colors[bar_idx]
                x_off = bar_offsets[bar_idx]
                h = val_to_h(val, max_val)
                bx = cx + x_off
                rect = Rectangle(width=bar_width, height=max(h, 0.05),
                                  color=color, fill_color=color,
                                  fill_opacity=0.85, stroke_width=0)
                rect.move_to([bx, Y_BOT + h / 2, 0])
                self.play(Create(rect), run_time=0.25)

        # Draw 4th bar (hypothetical sparse) per column -- dashed border style
        for col_idx, (lbl, cx) in enumerate(zip(col_labels, col_xs)):
            col_data = data[lbl]
            max_val = col_max_vals[col_idx]
            val = col_data[3]
            h = val_to_h(val, max_val)
            bx = cx + bar_offsets[3]
            # Fill with light slate, dashed border to signal "hypothetical"
            rect_fill = Rectangle(width=bar_width, height=max(h, 0.05),
                                   color=SLATE, fill_color=SLATE,
                                   fill_opacity=0.35, stroke_width=1.5,
                                   stroke_color=INK)
            rect_fill.move_to([bx, Y_BOT + h / 2, 0])
            self.play(Create(rect_fill), run_time=0.4)

        # Hypothetical chip label
        sparse_chip = LabelChip("IF SPARSE KERNEL EXISTED", accent=INK, size=18)
        sparse_chip.move_to([0.0, -3.05, 0])
        self.play(GrowFromCenter(sparse_chip), run_time=0.4)

        # Punchline on latency
        lat_chip = LabelChip("LATENCY WOULD DROP", accent=INK, size=19)
        lat_chip.move_to([4.0, 1.0, 0])
        self.play(GrowFromCenter(lat_chip), run_time=0.4)

        elapsed = 0.4 + 3*0.2 + 3*0.2 + 9*0.25 + 3*0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- the lesson
# =============================================================================
class B07_Summary(Scene):
    """Recap: optimize for the kernel you ship."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("Unstructured:", font=DISPLAY, color=INK, font_size=23)
        row1.move_to([-2.8, 1.6, 0])
        chip1 = LabelChip("STORAGE ONLY", accent=CRIMSON, size=22)
        chip1.move_to([2.8, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.35)
        self.play(GrowFromCenter(chip1), run_time=0.35)

        sep2 = Line([-5.5, 1.0, 0], [5.5, 1.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        row2 = Text("Structured:", font=DISPLAY, color=INK, font_size=23)
        row2.move_to([-2.8, 0.4, 0])
        chip2 = LabelChip("STORAGE + SRAM + LATENCY", accent=INK, size=22)
        chip2.move_to([2.8, 0.4, 0])
        self.play(FadeIn(row2), run_time=0.35)
        self.play(GrowFromCenter(chip2), run_time=0.35)

        sep3 = Line([-5.5, -0.2, 0], [5.5, -0.2, 0], stroke_width=0.8, color=SLATE)
        sep3.set_stroke(opacity=0.35)
        self.play(Create(sep3), run_time=0.3)

        foot = Text("Optimize for the kernel you ship, not the benchmark you read.",
                    font=SERIF, color=INK, font_size=20)
        foot.move_to([0.0, -0.9, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.4+0.35+0.35+0.3+0.35+0.35+0.3+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps: run on real shapes, measure on-target latency."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· run prune_benchmark.py on your real layer shapes",
                     font=DISPLAY, color=INK, font_size=21)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("verify which of the three metrics actually move",
                    font=SERIF, color=INK, font_size=18)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· measure on-target latency on the MCU",
                     font=DISPLAY, color=INK, font_size=21)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("output beats here use illustrative data -- swap in real captures",
                    font=SERIF, color=INK, font_size=18)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        step3 = Text("· watch for sparse kernel support in your toolchain",
                     font=DISPLAY, color=INK, font_size=21)
        step3.move_to([0.0, -1.3, 0])
        self.play(FadeIn(step3), run_time=0.4)

        sep2 = Line([-5.5, -1.9, 0], [5.5, -1.9, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.35)

        elapsed = 0.4+0.4+0.4+0.4+0.4+0.4+0.4+0.35
        self.wait(max(0.5, dur - elapsed))
