"""vox_scenes.py — embedded-ai/youtube/cli-distill
Reel: Distillation: See the Soft Label's Extra Signal
Palette: teardown (white ground, ink originals, crimson = target class / problem)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  target class (cat) / baseline
  SLATE   #545454  wrong classes / neutral

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

# ── distillation parameters ────────────────────────────────────────────────────
LOGITS = np.array([5.0, 0.3, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
N_CLASSES = 10
CLASS_NAMES = ["cat", "dog", "bird", "fish", "frog",
               "ship", "car", "truck", "deer", "horse"]

def _softmax(z, T=1.0):
    z = np.asarray(z, dtype=float) / T
    e = np.exp(z - z.max())
    return e / e.sum()

# Bar x positions: 10 bars spanning [-5.0, 4.9] with spacing 1.1
BAR_XS = [-5.0 + 1.1 * i for i in range(N_CLASSES)]
BAR_W  = 0.7
BAR_ORIGIN_Y = -2.8
BAR_MAX_H    = 5.0  # scene units for 100% probability


def _bar_h(prob):
    return max(0.02, prob * BAR_MAX_H)

def _bar_center_y(prob):
    return BAR_ORIGIN_Y + _bar_h(prob) / 2


# =============================================================================
# B01_Problem — title card: one-hot vs teacher soft distribution
# =============================================================================
class B01_Problem(Scene):
    """Title card: one-hot discards signal; teacher soft distribution carries it."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("KNOWLEDGE DISTILLATION", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_hard = LabelChip("HARD LABEL: cat", accent=SLATE, size=22)
        chip_hard.move_to([-2.8, 1.9, 0])

        chip_soft = LabelChip("SOFT: 85% cat  5% dog", accent=CRIMSON, size=22)
        chip_soft.move_to([2.8, 1.9, 0])

        self.play(GrowFromCenter(chip_hard), GrowFromCenter(chip_soft), run_time=0.5)

        sub = Text("the 5% dog is the signal the hard label throws away",
                   font=DISPLAY, color=INK, font_size=19)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_dark = LabelChip("DARK KNOWLEDGE", accent=INK, size=22)
        chip_dark.move_to([-2.8, -0.15, 0])

        chip_temp = LabelChip("TEMPERATURE EXPOSES IT", accent=SLATE, size=22)
        chip_temp.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_dark), GrowFromCenter(chip_temp), run_time=0.5)

        q = Text("the teacher's reasonable mistakes are the signal",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_DistillTemp — 10 class bars, temperature sweep T=1 -> T=3 -> T=6
# =============================================================================
class B04_DistillTemp(Scene):
    """10 bars: cat=CRIMSON, others=SLATE. Morph through T=1, T=3, T=6."""

    def construct(self):
        dur = _dur("B04")

        hdr = Text("TEMPERATURE SWEEP", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── baseline axis ─────────────────────────────────────────────────────
        ax = Line([-5.5, BAR_ORIGIN_Y, 0], [5.5, BAR_ORIGIN_Y, 0],
                  stroke_width=1.5, color=INK)
        self.play(Create(ax), run_time=0.4)

        # ── initial bars at T=1 ───────────────────────────────────────────────
        probs_t1 = _softmax(LOGITS, T=1)
        bars = []
        for i in range(N_CLASSES):
            h = _bar_h(probs_t1[i])
            cy = BAR_ORIGIN_Y + h / 2
            col = CRIMSON if i == 0 else SLATE
            bar = Rectangle(width=BAR_W, height=h, color=col, fill_opacity=0.85)
            bar.move_to([BAR_XS[i], cy, 0])
            bars.append(bar)
            self.play(GrowFromCenter(bar), run_time=0.15)

        # T=1 chip — placed high right
        t_chip = LabelChip("T = 1", accent=SLATE, size=22)
        t_chip.move_to([4.5, 2.5, 0])
        self.play(GrowFromCenter(t_chip), run_time=0.35)
        self.wait(0.5)

        # ── transform to T=3 ──────────────────────────────────────────────────
        probs_t3 = _softmax(LOGITS, T=3)
        new_bars_t3 = []
        for i in range(N_CLASSES):
            h = _bar_h(probs_t3[i])
            cy = BAR_ORIGIN_Y + h / 2
            col = CRIMSON if i == 0 else SLATE
            nb = Rectangle(width=BAR_W, height=h, color=col, fill_opacity=0.85)
            nb.move_to([BAR_XS[i], cy, 0])
            new_bars_t3.append(nb)

        anims_t3 = [Transform(bars[i], new_bars_t3[i]) for i in range(N_CLASSES)]
        self.play(*anims_t3, run_time=1.2)
        # T=3 chip — at different y position so Gate W sees no overlap
        t_chip2 = LabelChip("T = 3", accent=SLATE, size=22)
        t_chip2.move_to([4.5, 1.6, 0])
        self.play(GrowFromCenter(t_chip2), run_time=0.3)
        self.wait(0.3)

        # ── transform to T=6 ──────────────────────────────────────────────────
        probs_t6 = _softmax(LOGITS, T=6)
        new_bars_t6 = []
        for i in range(N_CLASSES):
            h = _bar_h(probs_t6[i])
            cy = BAR_ORIGIN_Y + h / 2
            col = CRIMSON if i == 0 else SLATE
            nb = Rectangle(width=BAR_W, height=h, color=col, fill_opacity=0.85)
            nb.move_to([BAR_XS[i], cy, 0])
            new_bars_t6.append(nb)

        anims_t6 = [Transform(bars[i], new_bars_t6[i]) for i in range(N_CLASSES)]
        self.play(*anims_t6, run_time=1.2)
        # T=6 chip — at yet another y position
        t_chip3 = LabelChip("T = 6", accent=CRIMSON, size=22)
        t_chip3.move_to([4.5, 0.7, 0])
        self.play(GrowFromCenter(t_chip3), run_time=0.3)
        self.wait(0.3)

        # ── class label for bar 0 (cat) ───────────────────────────────────────
        cat_lbl = Text("cat", font=DISPLAY, color=CRIMSON, font_size=18)
        cat_lbl.move_to([BAR_XS[0], BAR_ORIGIN_Y - 0.4, 0])
        self.play(FadeIn(cat_lbl), run_time=0.3)

        # ── signal chip ───────────────────────────────────────────────────────
        sig_chip = LabelChip("wrong-class signal now visible", accent=INK, size=18)
        sig_chip.move_to([0.0, -3.3, 0])
        self.play(GrowFromCenter(sig_chip), run_time=0.4)

        elapsed = 0.4 + 0.4 + N_CLASSES * 0.15 + 0.35 + 0.5 + 1.2 + 0.4 + 1.2 + 0.4 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_DistillPruned — two accuracy bars: hard label vs distilled student
# =============================================================================
class B06_DistillPruned(Scene):
    """Hard label bar (shorter, CRIMSON) vs Distilled bar (taller, INK)."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("PRUNED STUDENT  --  ACCURACY RECOVERY", font=DISPLAY, color=INK, font_size=24)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axis ──────────────────────────────────────────────────────────────
        ax_y = Line([-4.0, -2.5, 0], [-4.0, 2.5, 0], stroke_width=1.5, color=INK)
        ax_x = Line([-4.0, -2.5, 0], [4.0, -2.5, 0], stroke_width=1.5, color=INK)
        self.play(Create(ax_y), run_time=0.4)
        self.play(Create(ax_x), run_time=0.4)

        y_lbl = Text("accuracy (%)", font=DISPLAY, color=INK, font_size=16)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([-5.5, 0.0, 0])
        self.play(FadeIn(y_lbl), run_time=0.3)

        # Bar parameters: accuracy scale 80-95% -> height in scene units
        ACC_LO, ACC_HI = 80.0, 95.0
        BAR_Y_LO, BAR_Y_HI = -2.5, 2.5
        BAR_RANGE = BAR_Y_HI - BAR_Y_LO

        def acc_y(acc):
            return BAR_Y_LO + (acc - ACC_LO) / (ACC_HI - ACC_LO) * BAR_RANGE

        # Tick marks at 80, 85, 90, 95
        for acc_val in [80, 85, 90, 95]:
            ty = acc_y(acc_val)
            tick = Line([-4.1, ty, 0], [-3.9, ty, 0], stroke_width=1.0, color=SLATE)
            lbl = Text(str(acc_val), font=MONO, color=SLATE, font_size=14)
            lbl.move_to([-4.5, ty, 0])
            self.play(Create(tick), FadeIn(lbl), run_time=0.2)

        # ── hard label bar (CRIMSON, 85%) ─────────────────────────────────────
        HL_ACC = 85.0
        hl_top = acc_y(HL_ACC)
        hl_h   = hl_top - BAR_Y_LO
        hl_bar = Rectangle(width=1.2, height=hl_h, color=CRIMSON, fill_opacity=0.85)
        hl_bar.move_to([-1.5, BAR_Y_LO + hl_h / 2, 0])
        self.play(GrowFromCenter(hl_bar), run_time=0.7)

        hl_lbl = Text("HARD LABEL", font=DISPLAY, color=CRIMSON, font_size=18)
        hl_lbl.move_to([-1.5, hl_top + 0.35, 0])
        self.play(FadeIn(hl_lbl), run_time=0.3)

        # ── distilled bar (INK, 88%) ───────────────────────────────────────────
        DT_ACC = 88.0
        dt_top = acc_y(DT_ACC)
        dt_h   = dt_top - BAR_Y_LO
        dt_bar = Rectangle(width=1.2, height=dt_h, color=INK, fill_opacity=0.85)
        dt_bar.move_to([1.5, BAR_Y_LO + dt_h / 2, 0])
        self.play(GrowFromCenter(dt_bar), run_time=0.7)

        dt_lbl = Text("DISTILLED", font=DISPLAY, color=INK, font_size=18)
        dt_lbl.move_to([1.5, dt_top + 0.35, 0])
        self.play(FadeIn(dt_lbl), run_time=0.3)

        # ── verdict chip ──────────────────────────────────────────────────────
        verdict = LabelChip("DISTILLED STUDENT +3%", accent=INK, size=20)
        verdict.move_to([0.0, -3.1, 0])
        self.play(GrowFromCenter(verdict), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.3 + 4 * 0.2 + 0.7 + 0.3 + 0.7 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary — teacher's mistakes are the signal
# =============================================================================
class B07_Summary(Scene):
    """Recap: hard labels discard dark knowledge; soft labels transfer it."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("hard label", font=DISPLAY, color=INK, font_size=24)
        row1.move_to([-3.0, 1.6, 0])
        chip1 = LabelChip("DISCARDS DARK KNOWLEDGE", accent=CRIMSON, size=20)
        chip1.move_to([2.5, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip1), run_time=0.4)

        row2 = Text("soft label", font=DISPLAY, color=INK, font_size=24)
        row2.move_to([-3.0, 0.6, 0])
        chip2 = LabelChip("TRANSFERS IT", accent=INK, size=20)
        chip2.move_to([2.5, 0.6, 0])
        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)

        sep2 = Line([-5.5, 0.0, 0], [5.5, 0.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        foot = Text("The teacher's reasonable mistakes are exactly what the student needs.",
                    font=SERIF, color=INK, font_size=19)
        foot.move_to([0.0, -0.75, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps — action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps: sweep T on your logits; run real distillation training."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· sweep temperature on your teacher's logits",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("find the T where wrong-class signal becomes visible",
                    font=SERIF, color=INK, font_size=18)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· run distillation against the float teacher",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("2-5% gain is real  ·  but only if you train on your data",
                    font=SERIF, color=INK, font_size=18)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
