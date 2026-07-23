"""vox_scenes.py -- embedded-ai/youtube/cli-realtime-verdict
Reel: Build a Real-Time Verdict Module with Claude Code
Palette: teardown (white ground, ink originals, crimson = tail / deadline miss)

teardown token mapping:
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  tail bins / deadline miss
  SLATE   #545454  structure, neutral chips

Gate A: every scene needs Create/GrowFromCenter/Transform.
Gate W: no Unicode arrows/checkmarks in Text(). x in [-6.3, 6.3], y in [-3.4, 3.4].
No Manim Axes class -- draw axes manually with Line().
Use Rectangle for histogram bars.
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


# Histogram layout constants
# X: latency 30ms-150ms across 15 bins (step 8ms), scene x=-5.5 to 5.5
# Y: count 0-30, scene y=-2.5 to 2.5
X_LEFT = -5.5
X_RIGHT = 5.5
Y_BOT = -2.5
Y_TOP = 2.5
BAR_W = (X_RIGHT - X_LEFT) / 15 * 0.85  # slight gap

# Illustrative counts for 15 bins (30, 38, 46, 54, 62, 70, 78, 86, 94, 102, 110, 118, 126, 134, 142ms)
# Bell peak at 62-70ms (bins 4-5), small tail at 102+ ms (bins 9-14)
BASE_COUNTS = [2, 5, 10, 18, 28, 30, 24, 15, 8, 4, 3, 2, 1, 0, 0]
# Bins 9-14 are past the 100ms deadline (bin centers: 102, 110, 118, 126, 134, 142ms)
DEADLINE_MS = 100.0
# Bin edges: 30 + i*8 for i in 0..15; bin i is past deadline when 30+i*8 >= 100 -> i >= 8.75 -> i >= 9
DEADLINE_BIN = 9  # first bin fully past deadline

JITTER_EXTRA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 6, 4, 2]  # GC jitter adds to tail bins 10-14 and extends to new bins

MAX_COUNT = 30
# X scene for bin i: X_LEFT + (i + 0.5) * (X_RIGHT - X_LEFT) / 15
def bin_x(i):
    return X_LEFT + (i + 0.5) * (X_RIGHT - X_LEFT) / 15

# Y scale: count -> scene y
def count_to_h(count):
    return (count / MAX_COUNT) * (Y_TOP - Y_BOT)

# Deadline x position: 100ms in [30ms, 150ms] -> fraction (100-30)/(150-30) = 70/120
DEADLINE_X = X_LEFT + (DEADLINE_MS - 30) / 120 * (X_RIGHT - X_LEFT)


# =============================================================================
# B01_Problem -- mean vs WCET
# =============================================================================
class B01_Problem(Scene):
    """Title card: mean latency passes, WCET misses the deadline."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("REAL-TIME VERDICT", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_mean = LabelChip("MEAN: 65ms  -- PASSES", accent=INK, size=22)
        chip_mean.move_to([-1.8, 1.6, 0])
        self.play(GrowFromCenter(chip_mean), run_time=0.4)

        chip_wcet = LabelChip("WCET: 125ms -- MISSES", accent=CRIMSON, size=22)
        chip_wcet.move_to([3.2, 1.6, 0])
        self.play(GrowFromCenter(chip_wcet), run_time=0.4)

        sep2 = Line([-5.5, 1.05, 0], [5.5, 1.05, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        chip_dl = LabelChip("DEADLINE: 100ms", accent=SLATE, size=22)
        chip_dl.move_to([0.0, 0.4, 0])
        self.play(GrowFromCenter(chip_dl), run_time=0.4)

        foot = Text("Real-time isn't fast -- it's bounded.",
                    font=SERIF, color=INK, font_size=22)
        foot.move_to([0.0, -0.7, 0])
        self.play(FadeIn(foot), run_time=0.5)

        q = Text("WCET: the guarantee, not the average.",
                 font=DISPLAY, color=INK, font_size=20)
        q.move_to([0.0, -1.5, 0])
        self.play(FadeIn(q), run_time=0.4)

        elapsed = 0.4+0.5+0.4+0.4+0.3+0.4+0.5+0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_Realtime -- latency histogram, tail in crimson, deadline line
# =============================================================================
class B04_Realtime(Scene):
    """Latency histogram builds bar by bar.
    Bins past 100ms deadline appear in CRIMSON.
    Deadline line added after all bars. Chip: WCET: 125ms DEADLINE MISSED.
    Illustrative data -- bell peak at 62-70ms, tail at 102-126ms.
    """

    def construct(self):
        dur = _dur("B04")

        hdr = Text("LATENCY DISTRIBUTION", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.1, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X_LEFT, Y_BOT, 0], [X_RIGHT, Y_BOT, 0],
                    stroke_width=1.2, color=SLATE)
        ax_y = Line([X_LEFT, Y_BOT, 0], [X_LEFT, Y_TOP, 0],
                    stroke_width=1.2, color=SLATE)
        ax_x.set_stroke(opacity=0.7)
        ax_y.set_stroke(opacity=0.7)
        self.play(Create(ax_x), Create(ax_y), run_time=0.4)

        lbl_x = Text("LATENCY (ms)", font=DISPLAY, color=SLATE, font_size=16)
        lbl_x.move_to([0.0, -3.2, 0])
        lbl_y = Text("COUNT", font=DISPLAY, color=SLATE, font_size=16)
        lbl_y.rotate(PI / 2)
        lbl_y.move_to([-5.0, 0.0, 0])
        self.play(FadeIn(lbl_x), FadeIn(lbl_y), run_time=0.25)

        # ── bins animate left to right ─────────────────────────────────────────
        for i, count in enumerate(BASE_COUNTS):
            if count == 0:
                continue
            h = count_to_h(count)
            bx = bin_x(i)
            color = CRIMSON if i >= DEADLINE_BIN else INK
            rect = Rectangle(width=BAR_W, height=max(h, 0.02),
                              color=color, fill_color=color,
                              fill_opacity=0.85, stroke_width=0)
            rect.move_to([bx, Y_BOT + h / 2, 0])
            self.play(Create(rect), run_time=0.35)

        # ── deadline vertical line ────────────────────────────────────────────
        dl_line = Line([DEADLINE_X, Y_BOT, 0], [DEADLINE_X, Y_TOP, 0],
                       stroke_width=2.5, color=CRIMSON)
        dl_line.set_stroke(opacity=0.9)
        self.play(Create(dl_line), run_time=0.5)

        dl_lbl = Text("100ms", font=DISPLAY, color=CRIMSON, font_size=17)
        dl_lbl.move_to([DEADLINE_X + 0.6, Y_TOP - 0.25, 0])
        self.play(FadeIn(dl_lbl), run_time=0.3)

        # ── WCET chip ─────────────────────────────────────────────────────────
        wcet_chip = LabelChip("WCET: 125ms  DEADLINE MISSED", accent=CRIMSON, size=19)
        wcet_chip.move_to([2.5, 1.8, 0])
        self.play(GrowFromCenter(wcet_chip), run_time=0.4)

        n_bars = sum(1 for c in BASE_COUNTS if c > 0)
        elapsed = 0.4 + 0.4 + 0.25 + n_bars*0.35 + 0.5 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_RealtimeJitter -- GC jitter extends tail further
# =============================================================================
class B06_RealtimeJitter(Scene):
    """Same histogram + GC jitter bars at 130-180ms.
    Mean stays 65ms; WCET extends to 180ms.
    Chip: GC JITTER  TAIL EXTENDS. New chip: WCET: 180ms.
    Illustrative data.
    """

    def construct(self):
        dur = _dur("B06")

        hdr = Text("GC JITTER -- TAIL EXTENDS", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.1, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        # Extended X range to 190ms: scene x=-5.5 to 5.5 maps 30ms to 190ms
        X_EXT_RIGHT = 5.5
        X_EXT_RANGE = 160  # 30 to 190ms

        def bin_x_ext(ms_center):
            return X_LEFT + (ms_center - 30) / X_EXT_RANGE * (X_EXT_RIGHT - X_LEFT)

        ax_x = Line([X_LEFT, Y_BOT, 0], [X_EXT_RIGHT, Y_BOT, 0],
                    stroke_width=1.2, color=SLATE)
        ax_y = Line([X_LEFT, Y_BOT, 0], [X_LEFT, Y_TOP, 0],
                    stroke_width=1.2, color=SLATE)
        ax_x.set_stroke(opacity=0.7)
        ax_y.set_stroke(opacity=0.7)
        self.play(Create(ax_x), Create(ax_y), run_time=0.4)

        lbl_x = Text("LATENCY (ms)", font=DISPLAY, color=SLATE, font_size=16)
        lbl_x.move_to([0.0, -3.05, 0])
        self.play(FadeIn(lbl_x), run_time=0.25)

        # ── base bins (original distribution) ────────────────────────────────
        # Rescale bin positions for extended x range
        bin_centers_ms = [30 + i*8 + 4 for i in range(15)]  # center of each bin
        bar_w_ext = 0.55

        for i, (ms, count) in enumerate(zip(bin_centers_ms, BASE_COUNTS)):
            if count == 0:
                continue
            h = count_to_h(count)
            bx = bin_x_ext(ms)
            color = CRIMSON if ms >= DEADLINE_MS else INK
            rect = Rectangle(width=bar_w_ext, height=max(h, 0.02),
                              color=color, fill_color=color,
                              fill_opacity=0.85, stroke_width=0)
            rect.move_to([bx, Y_BOT + h / 2, 0])
            self.play(Create(rect), run_time=0.25)

        # ── deadline line ──────────────────────────────────────────────────────
        dl_x = bin_x_ext(DEADLINE_MS)
        dl_line = Line([dl_x, Y_BOT, 0], [dl_x, Y_TOP * 0.8, 0],
                       stroke_width=2.0, color=CRIMSON)
        dl_line.set_stroke(opacity=0.7)
        self.play(Create(dl_line), run_time=0.4)

        # ── GC jitter bars: 5 new bins at 130, 146, 162, 178 ms ──────────────
        jitter_bins = [(134, 6), (146, 8), (158, 7), (170, 4), (182, 2)]
        for ms, count in jitter_bins:
            h = count_to_h(count)
            bx = bin_x_ext(ms)
            rect = Rectangle(width=bar_w_ext, height=h,
                              color=CRIMSON, fill_color=CRIMSON,
                              fill_opacity=0.85, stroke_width=0)
            rect.move_to([bx, Y_BOT + h / 2, 0])
            self.play(Create(rect), run_time=0.4)

        # ── chips ──────────────────────────────────────────────────────────────
        jitter_chip = LabelChip("GC JITTER  TAIL EXTENDS", accent=CRIMSON, size=19)
        jitter_chip.move_to([-1.5, 2.0, 0])
        self.play(GrowFromCenter(jitter_chip), run_time=0.4)

        wcet_chip = LabelChip("WCET: 180ms  DEADLINE: 100ms", accent=CRIMSON, size=18)
        wcet_chip.move_to([3.2, 2.0, 0])
        self.play(GrowFromCenter(wcet_chip), run_time=0.4)

        mean_note = Text("mean still 65ms -- average is useless here",
                         font=SERIF, color=INK, font_size=17)
        mean_note.move_to([0.0, -3.3, 0])
        self.play(FadeIn(mean_note), run_time=0.4)

        n_base = sum(1 for c in BASE_COUNTS if c > 0)
        elapsed = 0.4+0.4+0.25+n_base*0.25+0.4+len(jitter_bins)*0.4+0.4+0.4+0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- the lesson
# =============================================================================
class B07_Summary(Scene):
    """Recap: average latency vs WCET."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("Average latency:", font=DISPLAY, color=INK, font_size=23)
        row1.move_to([-2.2, 1.6, 0])
        chip1 = LabelChip("NORMAL CASE", accent=SLATE, size=22)
        chip1.move_to([3.2, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.35)
        self.play(GrowFromCenter(chip1), run_time=0.35)

        sep2 = Line([-5.5, 1.0, 0], [5.5, 1.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        row2 = Text("WCET:", font=DISPLAY, color=INK, font_size=23)
        row2.move_to([-3.8, 0.4, 0])
        chip2 = LabelChip("GUARANTEE UNDER LOAD", accent=INK, size=22)
        chip2.move_to([2.6, 0.4, 0])
        self.play(FadeIn(row2), run_time=0.35)
        self.play(GrowFromCenter(chip2), run_time=0.35)

        sep3 = Line([-5.5, -0.2, 0], [5.5, -0.2, 0], stroke_width=0.8, color=SLATE)
        sep3.set_stroke(opacity=0.35)
        self.play(Create(sep3), run_time=0.3)

        foot = Text("Optimizing the average while ignoring the tail is the classic safety failure.",
                    font=SERIF, color=INK, font_size=18)
        foot.move_to([0.0, -0.9, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.4+0.35+0.35+0.3+0.35+0.35+0.3+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items
# =============================================================================
class B08_NextSteps(Scene):
    """Next steps: collect real latency distribution, run realtime.py."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· collect latency distribution under production load",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("not a benchmark -- actual inference times during operation",
                    font=SERIF, color=INK, font_size=17)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· run realtime.py and check WCET vs your deadline class",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.15, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("soft / firm / hard -- each demands a different design",
                    font=SERIF, color=INK, font_size=17)
        sub2.move_to([0.0, -0.5, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.1, 0], [5.5, -1.1, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.35)

        note = Text("Output beats use illustrative data -- swap in your measured latency array.",
                    font=SERIF, color=INK, font_size=17)
        note.move_to([0.0, -1.7, 0])
        self.play(FadeIn(note), run_time=0.4)

        elapsed = 0.4+0.4+0.4+0.4+0.4+0.4+0.35+0.4
        self.wait(max(0.5, dur - elapsed))
