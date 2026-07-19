"""vox_scenes.py — embedded-ai/youtube/cli-memory-verdict
Reel: Build a Memory Verdict Module with Claude Code
Palette: teardown (white ground, ink originals, crimson = fail/over budget)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  fail / over-budget bar
  SLATE   #545454  structure, neutral chips, ceiling lines

Gate W colour rules (teardown on GROUND #FFFFFF):
  INK on GROUND -> contrast ~21:1 (AAA)
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

# ── memory numbers (MobileNetV2-0.5) ──────────────────────────────────────────
# FP32: weight_kb = 2.1M params * 4 bytes / 1024 = 8192 KB -- scaled to ~5600KB with firmware
# Actually: MobileNetV2-0.5 has ~1.4M params
# FP32: 1.4M * 4 = 5.6MB; INT8: 1.4M * 1 = 1.4MB
PARAMS_M     = 1.4    # million params
FIRMWARE_KB  = 200.0  # firmware overhead
FLASH_BUDGET = 4096.0 # 4MB ceiling
SRAM_BUDGET  = 1024.0 # 1MB ceiling
LARGEST_ACT_FP32 = 500.0   # KB (FP32 activations)
LARGEST_ACT_INT8 = 250.0   # KB (INT8 slightly smaller)

def _flash_used(dtype):
    bpp = 4 if dtype == "fp32" else 1
    return PARAMS_M * 1e6 * bpp / 1024 + FIRMWARE_KB  # KB

FLASH_FP32 = _flash_used("fp32")   # ~5660 KB
FLASH_INT8 = _flash_used("int8")   # ~1565 KB

# ── waterfall bar parameters ───────────────────────────────────────────────────
BAR_X_FLASH = -2.5
BAR_X_SRAM  =  2.5
BAR_W       =  1.6

# Map KB values to scene y coordinates
# Budget scale: budget is the "ceiling"; bars grow from bottom
# y range: bar bottom at y=-2.5, ceiling mapped proportionally
BAR_Y_BOTTOM = -2.5
BAR_Y_SCALE  =  4.5  # scene height for the max value displayed

# Use a common display scale: max KB shown = 6000KB (for FP32 flash)
DISPLAY_MAX = 6200.0  # KB

def _kb_to_h(kb_value):
    return max(0.05, kb_value / DISPLAY_MAX * BAR_Y_SCALE)

def _budget_y(budget_kb):
    return BAR_Y_BOTTOM + budget_kb / DISPLAY_MAX * BAR_Y_SCALE


# =============================================================================
# B01_Problem — title card: FLASH vs SRAM, two different failures
# =============================================================================
class B01_Problem(Scene):
    """Title card: out of memory is two bugs -- flash (weights) vs SRAM (activations)."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("MEMORY VERDICT", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_flash = LabelChip("FLASH: weights + firmware", accent=SLATE, size=22)
        chip_flash.move_to([-2.8, 1.9, 0])

        chip_sram = LabelChip("SRAM: largest activation", accent=SLATE, size=22)
        chip_sram.move_to([2.8, 1.9, 0])

        self.play(GrowFromCenter(chip_flash), GrowFromCenter(chip_sram), run_time=0.5)

        sub = Text("both say 'out of memory' -- they have different fixes",
                   font=DISPLAY, color=INK, font_size=19)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_fix1 = LabelChip("FLASH FAIL -> compress weights", accent=CRIMSON, size=20)
        chip_fix1.move_to([-2.5, -0.15, 0])

        chip_fix2 = LabelChip("SRAM FAIL -> tile activations", accent=INK, size=20)
        chip_fix2.move_to([3.0, -0.15, 0])

        self.play(GrowFromCenter(chip_fix1), GrowFromCenter(chip_fix2), run_time=0.5)

        q = Text("a typed verdict names which -- naming which tells you the fix",
                 font=SERIF, color=INK, font_size=20)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_MemoryVerdict — FLASH (FP32, 5.6MB, FAIL) and SRAM (0.5MB, PASS)
# =============================================================================
class B04_MemoryVerdict(Scene):
    """Flash bar over budget (CRIMSON), SRAM bar under budget (INK)."""

    def construct(self):
        dur = _dur("B04")

        hdr = Text("MEMORY VERDICT  --  FP32", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── baseline axis ──────────────────────────────────────────────────────
        ax = Line([-5.5, BAR_Y_BOTTOM, 0], [5.5, BAR_Y_BOTTOM, 0],
                  stroke_width=1.5, color=INK)
        self.play(Create(ax), run_time=0.4)

        # ── column labels ──────────────────────────────────────────────────────
        lbl_flash = Text("FLASH", font=DISPLAY, color=INK, font_size=20)
        lbl_flash.move_to([BAR_X_FLASH, BAR_Y_BOTTOM - 0.45, 0])
        lbl_sram = Text("SRAM", font=DISPLAY, color=INK, font_size=20)
        lbl_sram.move_to([BAR_X_SRAM, BAR_Y_BOTTOM - 0.45, 0])
        self.play(FadeIn(lbl_flash), FadeIn(lbl_sram), run_time=0.3)

        # ── FLASH ceiling line (SLATE, at 4MB = 4096KB) ────────────────────────
        flash_ceil_y = _budget_y(FLASH_BUDGET)
        flash_ceil = Line([BAR_X_FLASH - 1.2, flash_ceil_y, 0],
                          [BAR_X_FLASH + 1.2, flash_ceil_y, 0],
                          stroke_width=2.0, color=SLATE)
        self.play(Create(flash_ceil), run_time=0.4)
        flash_ceil_lbl = Text("4MB budget", font=DISPLAY, color=SLATE, font_size=14)
        flash_ceil_lbl.move_to([BAR_X_FLASH + 2.0, flash_ceil_y + 0.25, 0])
        self.play(FadeIn(flash_ceil_lbl), run_time=0.3)

        # ── SRAM ceiling line (SLATE, at 1MB = 1024KB) ────────────────────────
        sram_ceil_y = _budget_y(SRAM_BUDGET)
        sram_ceil = Line([BAR_X_SRAM - 1.2, sram_ceil_y, 0],
                         [BAR_X_SRAM + 1.2, sram_ceil_y, 0],
                         stroke_width=2.0, color=SLATE)
        self.play(Create(sram_ceil), run_time=0.4)
        sram_ceil_lbl = Text("1MB budget", font=DISPLAY, color=SLATE, font_size=14)
        sram_ceil_lbl.move_to([BAR_X_SRAM + 2.0, sram_ceil_y + 0.25, 0])
        self.play(FadeIn(sram_ceil_lbl), run_time=0.3)

        # ── FLASH bar (FP32, 5.6MB, CRIMSON = over budget) ────────────────────
        flash_h = _kb_to_h(FLASH_FP32)
        flash_bar = Rectangle(width=BAR_W, height=flash_h,
                              color=CRIMSON, fill_opacity=0.85)
        flash_bar.move_to([BAR_X_FLASH, BAR_Y_BOTTOM + flash_h / 2, 0])
        self.play(GrowFromCenter(flash_bar), run_time=0.8)

        flash_val_lbl = Text("5.6 MB", font=MONO, color=CRIMSON, font_size=16)
        flash_val_lbl.move_to([BAR_X_FLASH, BAR_Y_BOTTOM + flash_h + 0.35, 0])
        self.play(FadeIn(flash_val_lbl), run_time=0.3)

        # ── SRAM bar (FP32, 0.5MB, INK = under budget) ────────────────────────
        sram_h = _kb_to_h(LARGEST_ACT_FP32)
        sram_bar = Rectangle(width=BAR_W, height=sram_h,
                             color=INK, fill_opacity=0.85)
        sram_bar.move_to([BAR_X_SRAM, BAR_Y_BOTTOM + sram_h / 2, 0])
        self.play(GrowFromCenter(sram_bar), run_time=0.6)

        sram_val_lbl = Text("0.5 MB", font=MONO, color=INK, font_size=16)
        sram_val_lbl.move_to([BAR_X_SRAM, BAR_Y_BOTTOM + sram_h + 0.35, 0])
        self.play(FadeIn(sram_val_lbl), run_time=0.3)

        # ── verdict chip ──────────────────────────────────────────────────────
        verdict = LabelChip("FLASH: FAIL  SRAM: OK", accent=CRIMSON, size=20)
        verdict.move_to([0.0, -3.15, 0])
        self.play(GrowFromCenter(verdict), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.3 + 0.4 + 0.3 + 0.4 + 0.3 + 0.8 + 0.3 + 0.6 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_MemoryVerdictInt8 — INT8 toggle: flash passes, SRAM barely changes
# =============================================================================
class B06_MemoryVerdictInt8(Scene):
    """INT8: flash bar drops to 1.4MB (INK), SRAM to 0.25MB (INK). Both pass."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("MEMORY VERDICT  --  INT8 TOGGLE", font=DISPLAY, color=INK, font_size=24)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        ax = Line([-5.5, BAR_Y_BOTTOM, 0], [5.5, BAR_Y_BOTTOM, 0],
                  stroke_width=1.5, color=INK)
        self.play(Create(ax), run_time=0.4)

        lbl_flash = Text("FLASH", font=DISPLAY, color=INK, font_size=20)
        lbl_flash.move_to([BAR_X_FLASH, BAR_Y_BOTTOM - 0.45, 0])
        lbl_sram = Text("SRAM", font=DISPLAY, color=INK, font_size=20)
        lbl_sram.move_to([BAR_X_SRAM, BAR_Y_BOTTOM - 0.45, 0])
        self.play(FadeIn(lbl_flash), FadeIn(lbl_sram), run_time=0.3)

        # ── ceiling lines ──────────────────────────────────────────────────────
        flash_ceil_y = _budget_y(FLASH_BUDGET)
        flash_ceil = Line([BAR_X_FLASH - 1.2, flash_ceil_y, 0],
                          [BAR_X_FLASH + 1.2, flash_ceil_y, 0],
                          stroke_width=2.0, color=SLATE)
        self.play(Create(flash_ceil), run_time=0.3)

        sram_ceil_y = _budget_y(SRAM_BUDGET)
        sram_ceil = Line([BAR_X_SRAM - 1.2, sram_ceil_y, 0],
                         [BAR_X_SRAM + 1.2, sram_ceil_y, 0],
                         stroke_width=2.0, color=SLATE)
        self.play(Create(sram_ceil), run_time=0.3)

        # ── FLASH bar (INT8, 1.4MB, INK = under budget) ────────────────────────
        flash_h = _kb_to_h(FLASH_INT8)
        flash_bar = Rectangle(width=BAR_W, height=flash_h,
                              color=INK, fill_opacity=0.85)
        flash_bar.move_to([BAR_X_FLASH, BAR_Y_BOTTOM + flash_h / 2, 0])
        self.play(GrowFromCenter(flash_bar), run_time=0.7)

        flash_val_lbl = Text("1.4 MB", font=MONO, color=INK, font_size=16)
        flash_val_lbl.move_to([BAR_X_FLASH, BAR_Y_BOTTOM + flash_h + 0.35, 0])
        self.play(FadeIn(flash_val_lbl), run_time=0.3)

        # ── SRAM bar (INT8, 0.25MB, INK = under budget) ────────────────────────
        sram_h = _kb_to_h(LARGEST_ACT_INT8)
        sram_bar = Rectangle(width=BAR_W, height=sram_h,
                             color=INK, fill_opacity=0.85)
        sram_bar.move_to([BAR_X_SRAM, BAR_Y_BOTTOM + sram_h / 2, 0])
        self.play(GrowFromCenter(sram_bar), run_time=0.5)

        sram_val_lbl = Text("0.25 MB", font=MONO, color=INK, font_size=16)
        sram_val_lbl.move_to([BAR_X_SRAM, BAR_Y_BOTTOM + sram_h + 0.35, 0])
        self.play(FadeIn(sram_val_lbl), run_time=0.3)

        # ── verdict chip ──────────────────────────────────────────────────────
        verdict = LabelChip("FLASH: PASS  SRAM: PASS", accent=INK, size=20)
        verdict.move_to([0.0, -3.15, 0])
        self.play(GrowFromCenter(verdict), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.3 + 0.3 + 0.3 + 0.7 + 0.3 + 0.5 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary — out of memory is two bugs; typed verdict names which
# =============================================================================
class B07_Summary(Scene):
    """Recap: FLASH fail -> compress weights; SRAM fail -> tile activations."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("flash fail", font=DISPLAY, color=INK, font_size=24)
        row1.move_to([-3.0, 1.6, 0])
        chip1 = LabelChip("COMPRESS WEIGHTS", accent=CRIMSON, size=22)
        chip1.move_to([2.5, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip1), run_time=0.4)

        row2 = Text("SRAM fail", font=DISPLAY, color=INK, font_size=24)
        row2.move_to([-3.0, 0.6, 0])
        chip2 = LabelChip("TILE ACTIVATIONS", accent=INK, size=22)
        chip2.move_to([2.5, 0.6, 0])
        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)

        sep2 = Line([-5.5, 0.0, 0], [5.5, 0.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        foot = Text("Naming which bug it is forces you to the right fix.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -0.75, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps — action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps: get param count, largest activation, flash/SRAM, run verdict."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· get param count + largest activation from model loader",
                     font=DISPLAY, color=INK, font_size=19)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("and flash / SRAM budget from the target datasheet",
                    font=SERIF, color=INK, font_size=18)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· run the verdict: if flash fails, int8 is the first lever",
                     font=DISPLAY, color=INK, font_size=19)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("if SRAM fails, layer-by-layer tiling is the next question",
                    font=SERIF, color=INK, font_size=18)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
