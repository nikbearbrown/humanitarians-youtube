"""vox_scenes.py -- embedded-ai/youtube/cli-deploy-runner
Reel: Deploy a Keyword Spotter: Find the Layer That Leaked Accuracy
Palette: teardown (white ground, ink originals, crimson = spike/error)

teardown token mapping:
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  divergence spike / fallback op
  SLATE   #545454  normal divergence bars / structure

Gate A: every scene needs Create/GrowFromCenter/Transform.
Gate W: no Unicode arrows/checkmarks in Text(). x in [-6.3, 6.3], y in [-3.4, 3.4].
No Manim Axes class -- draw axes manually with Line().
Use Rectangle for bars.
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


# Layer layout constants
# 10 layers, x from -5.0 to 4.5 (step 1.05 apart)
N_LAYERS = 10
X_START = -5.0
X_STEP = 1.05
Y_BOT = -2.5
Y_TOP = 2.3

# Illustrative divergence values (MSE between float and int8 per layer)
# Layer 7 is the spike: 0.15 (vs 0.001-0.004 for normal layers)
DIVERGENCES = [0.001, 0.002, 0.001, 0.003, 0.002, 0.001, 0.004, 0.15, 0.003, 0.002]
MAX_DIV = 0.15

BAR_W = 0.7

def layer_x(i):
    return X_START + i * X_STEP

def div_to_h(div):
    return (div / MAX_DIV) * (Y_TOP - Y_BOT)


# =============================================================================
# B01_Problem -- 94% in Python, 91% after toolchain; bisection as the fix
# =============================================================================
class B01_Problem(Scene):
    """Title card: toolchain-induced accuracy loss; bisection as diagnostic."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("DEPLOY RUNNER", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_py = LabelChip("KERAS: 94% ACC", accent=INK, size=22)
        chip_py.move_to([-2.5, 1.6, 0])
        self.play(GrowFromCenter(chip_py), run_time=0.4)

        chip_tfl = LabelChip("TFLITE INT8: 91% ACC", accent=CRIMSON, size=22)
        chip_tfl.move_to([2.8, 1.6, 0])
        self.play(GrowFromCenter(chip_tfl), run_time=0.4)

        sep2 = Line([-5.5, 1.05, 0], [5.5, 1.05, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        row1 = Text("toolchain loss  !=  quantization loss",
                    font=DISPLAY, color=INK, font_size=20)
        row1.move_to([0.0, 0.45, 0])
        self.play(FadeIn(row1), run_time=0.4)

        chip_bis = LabelChip("BISECT LAYER BY LAYER", accent=INK, size=22)
        chip_bis.move_to([0.0, -0.35, 0])
        self.play(GrowFromCenter(chip_bis), run_time=0.4)

        foot = Text("A diff at every hop is the only defense.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -1.3, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.5+0.4+0.4+0.3+0.4+0.4+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_Deploy -- per-layer divergence bars, layer 7 is the crimson spike
# =============================================================================
class B04_Deploy(Scene):
    """10 layer bars left to right. Layers 0-6 and 8-9 in SLATE (low divergence).
    Layer 7 in CRIMSON (spike: MSE 0.15 vs 0.001-0.004 for others).
    Chip: LAYER 7: DIVERGENCE SPIKE. Illustrative data.
    """

    def construct(self):
        dur = _dur("B04")

        hdr = Text("LAYER DIVERGENCE (FLOAT vs INT8)", font=DISPLAY, color=INK, font_size=24)
        hdr.move_to([0.0, 3.1, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X_START - 0.5, Y_BOT, 0],
                    [layer_x(N_LAYERS - 1) + 0.5, Y_BOT, 0],
                    stroke_width=1.2, color=SLATE)
        ax_y = Line([X_START - 0.5, Y_BOT, 0],
                    [X_START - 0.5, Y_TOP, 0],
                    stroke_width=1.2, color=SLATE)
        ax_x.set_stroke(opacity=0.7)
        ax_y.set_stroke(opacity=0.7)
        self.play(Create(ax_x), Create(ax_y), run_time=0.4)

        lbl_y = Text("MSE", font=DISPLAY, color=SLATE, font_size=16)
        lbl_y.rotate(PI / 2)
        lbl_y.move_to([-5.5, 0.0, 0])
        self.play(FadeIn(lbl_y), run_time=0.25)

        # ── bars animate left to right ─────────────────────────────────────────
        for i, div in enumerate(DIVERGENCES):
            h = div_to_h(div)
            bx = layer_x(i)
            color = CRIMSON if i == 7 else INK

            rect = Rectangle(width=BAR_W, height=max(h, 0.04),
                              color=color, fill_color=color,
                              fill_opacity=0.85, stroke_width=0)
            rect.move_to([bx, Y_BOT + h / 2, 0])
            self.play(Create(rect), run_time=0.35)

            # Layer number label below bar
            lbl = Text(str(i), font=DISPLAY, color=INK, font_size=15)
            lbl.move_to([bx, Y_BOT - 0.25, 0])
            self.play(FadeIn(lbl), run_time=0.15)

        # ── spike annotation ──────────────────────────────────────────────────
        spike_chip = LabelChip("LAYER 7: DIVERGENCE SPIKE", accent=CRIMSON, size=19)
        spike_chip.move_to([2.5, 1.5, 0])
        self.play(GrowFromCenter(spike_chip), run_time=0.4)

        # Arrow-free annotation: a line from chip to bar
        spike_x = layer_x(7)
        ptr = Line([1.2, 1.5, 0], [spike_x + 0.2, Y_BOT + div_to_h(0.15) + 0.15, 0],
                   stroke_width=1.5, color=CRIMSON)
        ptr.set_stroke(opacity=0.6)
        self.play(Create(ptr), run_time=0.4)

        elapsed = 0.4+0.4+0.25+N_LAYERS*(0.35+0.15)+0.4+0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_DeployOp -- same bars + OK/FALLBACK chips per layer
# =============================================================================
class B06_DeployOp(Scene):
    """Same 10 bars. Above each: OK chip (INK) for layers 0-6, 8-9.
    Above layer 7: FALLBACK chip (CRIMSON).
    Final chip: CMSIS-NN FALLBACK  ACCURACY LEAK.
    Illustrative data.
    """

    def construct(self):
        dur = _dur("B06")

        hdr = Text("PER-OP SUPPORT CHECK", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.1, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X_START - 0.5, Y_BOT, 0],
                    [layer_x(N_LAYERS - 1) + 0.5, Y_BOT, 0],
                    stroke_width=1.2, color=SLATE)
        ax_y = Line([X_START - 0.5, Y_BOT, 0],
                    [X_START - 0.5, Y_TOP, 0],
                    stroke_width=1.2, color=SLATE)
        ax_x.set_stroke(opacity=0.7)
        ax_y.set_stroke(opacity=0.7)
        self.play(Create(ax_x), Create(ax_y), run_time=0.4)

        # ── draw all bars ──────────────────────────────────────────────────────
        bar_tops = []
        for i, div in enumerate(DIVERGENCES):
            h = div_to_h(div)
            bx = layer_x(i)
            color = CRIMSON if i == 7 else INK

            rect = Rectangle(width=BAR_W, height=max(h, 0.04),
                              color=color, fill_color=color,
                              fill_opacity=0.85, stroke_width=0)
            rect.move_to([bx, Y_BOT + h / 2, 0])
            self.play(Create(rect), run_time=0.25)
            bar_tops.append(Y_BOT + h)

        # ── per-op chips above each bar ────────────────────────────────────────
        for i in range(N_LAYERS):
            bx = layer_x(i)
            bar_top_y = bar_tops[i]
            chip_y = min(bar_top_y + 0.35, 2.0)  # stay in safe area

            if i == 7:
                lbl = Text("FALLBACK", font=DISPLAY, color=CRIMSON, font_size=13)
            else:
                lbl = Text("OK", font=DISPLAY, color=INK, font_size=13)
            lbl.move_to([bx, chip_y, 0])
            self.play(GrowFromCenter(lbl), run_time=0.25)

        # ── final chip ────────────────────────────────────────────────────────
        final_chip = LabelChip("CMSIS-NN FALLBACK  ACCURACY LEAK", accent=CRIMSON, size=18)
        final_chip.move_to([1.5, 2.7, 0])
        self.play(GrowFromCenter(final_chip), run_time=0.4)

        elapsed = 0.4+0.4+N_LAYERS*0.25+N_LAYERS*0.25+0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- the lesson
# =============================================================================
class B07_Summary(Scene):
    """Recap: quantization error vs toolchain error; bisection separates them."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("Quantization error:", font=DISPLAY, color=INK, font_size=23)
        row1.move_to([-2.2, 1.6, 0])
        chip1 = LabelChip("SPREAD ACROSS LAYERS", accent=SLATE, size=22)
        chip1.move_to([3.0, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.35)
        self.play(GrowFromCenter(chip1), run_time=0.35)

        sep2 = Line([-5.5, 1.0, 0], [5.5, 1.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.35)
        self.play(Create(sep2), run_time=0.3)

        row2 = Text("Toolchain error:", font=DISPLAY, color=INK, font_size=23)
        row2.move_to([-2.5, 0.4, 0])
        chip2 = LabelChip("SPIKE AT ONE OP", accent=CRIMSON, size=22)
        chip2.move_to([3.0, 0.4, 0])
        self.play(FadeIn(row2), run_time=0.35)
        self.play(GrowFromCenter(chip2), run_time=0.35)

        sep3 = Line([-5.5, -0.2, 0], [5.5, -0.2, 0], stroke_width=0.8, color=SLATE)
        sep3.set_stroke(opacity=0.35)
        self.play(Create(sep3), run_time=0.3)

        foot = Text("Bisect layer by layer. Fix the op. The accuracy comes back.",
                    font=SERIF, color=INK, font_size=20)
        foot.move_to([0.0, -0.9, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4+0.4+0.35+0.35+0.3+0.35+0.35+0.3+0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items
# =============================================================================
class B08_NextSteps(Scene):
    """Next steps: bring trained model + val set, run deploy_runner.py."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· bring a trained Keras or TFLite model",
                     font=DISPLAY, color=INK, font_size=21)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("Claude does conversion + bisection in pure Python -- no hardware needed",
                    font=SERIF, color=INK, font_size=17)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· bring a validation set for your keyword-spotter",
                     font=DISPLAY, color=INK, font_size=21)
        step2.move_to([0.0, 0.15, 0])
        self.play(FadeIn(step2), run_time=0.4)

        step3 = Text("· run deploy_runner.py and check bisection output",
                     font=DISPLAY, color=INK, font_size=21)
        step3.move_to([0.0, -0.6, 0])
        self.play(FadeIn(step3), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.35)

        note = Text("Output beats use illustrative divergence values -- swap in real model output.",
                    font=SERIF, color=INK, font_size=17)
        note.move_to([0.0, -1.8, 0])
        self.play(FadeIn(note), run_time=0.4)

        elapsed = 0.4+0.4+0.4+0.4+0.4+0.4+0.35+0.4
        self.wait(max(0.5, dur - elapsed))
