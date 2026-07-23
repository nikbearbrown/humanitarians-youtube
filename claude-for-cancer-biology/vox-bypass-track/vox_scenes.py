"""vox_scenes.py — Why Blocking the Accelerator Perfectly Can Still Fail
(vox-bypass-track, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B02 is a STILL (ai media slot) — no scene.

Color law: TEAL = drug / blocked target / the kept thing
           CRIMSON = bypass track / resistance / the growing tumor
           GOLD = single editor highlight fill ONLY (never text)
Gate B: every zero-width stroke is also zero-opacity.
Exclusions: NO T790M, NO full EGFR biochemistry, NO phenotypic switching,
NO pharmacokinetics. One mechanism only: bypass track selected, not created.
"""
import sys, pathlib as _pl
# Resolve vox toolkit regardless of cwd — reel is at books/<book>/youtube/<slug>/
# so parents[3] = books/, then vox/aspects/explainer/vox-explainer/manim
_VOX_MANIM = _pl.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
if str(_VOX_MANIM) not in sys.path:
    sys.path.insert(0, str(_VOX_MANIM))
from vox_graphics import *   # noqa: F401,F403
import json, os, numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


# ---------------------------------------------------------------- scene helpers

def _node(label, color, radius=0.55):
    """Filled circle node with a white serif label inside."""
    c = Circle(radius=radius)
    c.set_fill(color, 1).set_stroke(width=0, opacity=0)
    t = Text(label, font=SERIF, color=WHITE, font_size=22)
    if t.width > radius * 1.6:
        t.scale_to_fit_width(radius * 1.6)
    t.move_to(c)
    return VGroup(c, t)


def _arrow(start, end, color=INK, tip=0.22):
    return Arrow(start, end, color=color, stroke_width=3,
                 tip_length=tip, buff=0.12)


def _xbar(center, color=CRIMSON, size=0.55):
    """Bold X marker for 'blocked' — two diagonal lines."""
    d = size * 0.5
    l1 = Line(center + np.array([-d, -d, 0]), center + np.array([d, d, 0]),
               color=color, stroke_width=8)
    l2 = Line(center + np.array([-d, d, 0]), center + np.array([d, -d, 0]),
               color=color, stroke_width=8)
    return VGroup(l1, l2)


def _blocker_bar(center_y=0.0, center_x=0.0, color=TEAL):
    """A thick vertical bar — the drug blockade marker. Placed manually."""
    perp_len = 0.7
    bar = Line(np.array([center_x, center_y - perp_len / 2, 0]),
               np.array([center_x, center_y + perp_len / 2, 0]),
               color=color, stroke_width=14)
    return bar


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = LabelChip("CANCER BIOLOGY", accent=TEAL, size=24)
        t1 = Text("Why Blocking the Accelerator", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("Perfectly Can Still Fail", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        sub = Text("when perfect target blockade is not enough",
                   font=SERIF, color=INK, font_size=28, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.45)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(block, shift=UP * 0.1), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


class B03_TumorShrink(Scene):
    def construct(self):
        total = DUR["B03"]
        before_c = LEFT * 3.0
        after_c = RIGHT * 3.0
        big = Circle(radius=1.5).set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        big.move_to(before_c)
        small = Circle(radius=0.3).set_fill(GROUND, 0).set_stroke(TEAL, 5)
        small.move_to(after_c)
        drug = LabelChip("osimertinib", accent=TEAL, size=22)
        drug.move_to(ORIGIN + UP * 2.6)
        arr = _arrow(drug.get_right() + RIGHT * 0.05, drug.get_right() + RIGHT * 1.0,
                     color=TEAL)
        lbl_before = Text("before", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        lbl_before.next_to(big, DOWN, buff=0.35)
        lbl_after = Text("3 months", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        lbl_after.next_to(small, DOWN, buff=0.35)
        self.play(FadeIn(drug), run_time=0.5)
        self.play(GrowFromCenter(big), FadeIn(lbl_before), run_time=0.8)
        self.wait(0.4)
        self.play(ReplacementTransform(big, small), FadeIn(lbl_after), run_time=1.2)
        self.wait(max(0.5, total - 2.9))


class B04_TheQuestion(Scene):
    def construct(self):
        total = DUR["B04"]
        # EGFR blocked label (TEAL block + X)
        egfr_node = _node("EGFR", TEAL, radius=0.65)
        egfr_node.move_to(LEFT * 3.5 + UP * 1.5)
        block_chip = LabelChip("BLOCKED", accent=TEAL, size=22)
        block_chip.next_to(egfr_node, RIGHT, buff=0.35)
        x_bar = _xbar(egfr_node.get_center(), TEAL, size=0.65)
        # tumor re-growing circle
        tumor = Circle(radius=0.9).set_fill(CRIMSON, 0.80).set_stroke(width=0, opacity=0)
        tumor.move_to(RIGHT * 3.2 + UP * 1.5)
        tumor_lbl = LabelChip("tumor re-growing", accent=CRIMSON, size=20)
        tumor_lbl.next_to(tumor, DOWN, buff=0.3)
        # question card
        q1 = Text("EGFR is still present and still blocked.", font=SERIF, color=INK,
                  font_size=30)
        q2 = Text("Why is this tumor growing?", font=SERIF, color=CRIMSON,
                  font_size=34, weight="BOLD")
        qblock = VGroup(q1, q2).arrange(DOWN, buff=0.25).move_to(DOWN * 1.9)
        self.play(FadeIn(egfr_node), FadeIn(block_chip), run_time=0.7)
        self.play(FadeIn(x_bar), run_time=0.5)
        self.play(GrowFromCenter(tumor), FadeIn(tumor_lbl), run_time=0.8)
        self.play(FadeIn(qblock, shift=UP * 0.15), run_time=0.9)
        self.wait(max(0.5, total - 2.9))


class B05_AddictionLogic(Scene):
    def construct(self):
        total = DUR["B05"]
        egfr = _node("EGFR", TEAL, radius=0.6)
        survival = _node("SURVIVAL", TEAL, radius=0.6)
        egfr.move_to(UP * 2.2)
        survival.move_to(DOWN * 2.2)
        arr_down = _arrow(egfr.get_bottom(), survival.get_top(), TEAL)
        drug_bar = _blocker_bar(center_y=0.0, center_x=0.0, color=TEAL)
        blocked_lbl = LabelChip("drug blocks here", accent=TEAL, size=20)
        blocked_lbl.next_to(drug_bar, RIGHT, buff=0.35)
        dead_lbl = SerifLabel("no alternative path", INK, size=26)
        dead_lbl.next_to(survival, DOWN, buff=0.4)
        self.play(FadeIn(egfr), run_time=0.5)
        self.play(GrowArrow(arr_down), run_time=0.7)
        self.play(FadeIn(survival), run_time=0.5)
        self.play(FadeIn(drug_bar), FadeIn(blocked_lbl), run_time=0.7)
        self.play(FadeIn(dead_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B06_BetEverything(Scene):
    def construct(self):
        total = DUR["B06"]
        egfr = _node("EGFR", TEAL, radius=0.6)
        egfr.move_to(ORIGIN)
        survival = _node("SURVIVAL", TEAL, radius=0.6)
        survival.move_to(DOWN * 3.0)
        # multiple inputs converging on EGFR
        starts = [UP * 2.5 + LEFT * 3.0, UP * 2.5 + LEFT * 1.0,
                  UP * 2.5 + RIGHT * 1.0, UP * 2.5 + RIGHT * 3.0]
        input_labels = ["GF1", "GF2", "GF3", "GF4"]
        inputs = VGroup()
        arrs_in = VGroup()
        for s, lbl in zip(starts, input_labels):
            n = _node(lbl, SLATE, radius=0.35)
            n.move_to(s)
            inputs.add(n)
            a = _arrow(s + DOWN * 0.35, egfr.get_top() + UP * 0.05, SLATE, tip=0.16)
            arrs_in.add(a)
        arr_out = _arrow(egfr.get_bottom(), survival.get_top(), TEAL)
        drug_bar = _blocker_bar(center_y=-1.5, center_x=0.0, color=TEAL)
        no_backup = SerifLabel("no backup plan", CRIMSON, size=26)
        no_backup.next_to(survival, RIGHT, buff=0.5)
        self.play(LaggedStart(*[FadeIn(n) for n in inputs], lag_ratio=0.15),
                  run_time=0.9)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrs_in], lag_ratio=0.1),
                  run_time=0.8)
        self.play(FadeIn(egfr), run_time=0.4)
        self.play(GrowArrow(arr_out), FadeIn(survival), run_time=0.6)
        self.play(FadeIn(drug_bar), run_time=0.5)
        self.play(FadeIn(no_backup, shift=LEFT * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.8))


class B07_TumorPopulation(Scene):
    def construct(self):
        total = DUR["B07"]
        # A grid of squares representing the tumor population
        # Most TEAL, a few CRIMSON scattered among them
        per_row = 22
        n_total = 44  # reduced for render speed; label explains scale
        n_crimson = 1
        counts = [n_total - n_crimson, n_crimson]
        colors = [TEAL, CRIMSON]
        grid = IsotypeGrid(counts, colors, per_row=per_row, size=0.18, gap=0.08)
        grid.move_to(UP * 0.4)
        pop_lbl = Text("10,000,000,000 cells", font=SERIF, color=INK, font_size=30)
        pop_lbl.next_to(grid, UP, buff=0.4)
        met_chip = LabelChip("MET-amplified (1 in 1,000,000)", accent=CRIMSON, size=20)
        met_chip.next_to(grid, DOWN, buff=0.4)
        self.play(FadeIn(pop_lbl, shift=DOWN * 0.1), run_time=0.6)
        self.play(grid.count_up(run_time=2.5))
        self.play(FadeIn(met_chip, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.8))


class B08_BypassRoute(Scene):
    def construct(self):
        total = DUR["B08"]
        # Main road: EGFR (blocked) -> RAS/PI3K -> SURVIVAL
        # Bypass: MET (CRIMSON) -> RAS/PI3K -> SURVIVAL
        egfr = _node("EGFR", TEAL, radius=0.52)
        met = _node("MET", CRIMSON, radius=0.52)
        ras = _node("RAS/PI3K", SLATE, radius=0.55)
        survival = _node("SURVIVAL", TEAL, radius=0.55)
        egfr.move_to(LEFT * 4.0 + UP * 1.2)
        met.move_to(LEFT * 4.0 + DOWN * 1.2)
        ras.move_to(ORIGIN)
        survival.move_to(RIGHT * 3.8)
        arr_egfr = _arrow(egfr.get_right(), ras.get_left() + LEFT * 0.1, TEAL)
        arr_met = _arrow(met.get_right(), ras.get_left() + LEFT * 0.1, CRIMSON)
        arr_surv = _arrow(ras.get_right(), survival.get_left(), TEAL)
        drug_bar = _blocker_bar(center_y=1.2, center_x=-2.0, color=TEAL)
        bypass_lbl = SerifLabel("bypass track", CRIMSON, size=24)
        bypass_lbl.next_to(arr_met, DOWN, buff=0.25)
        self.play(FadeIn(egfr), FadeIn(ras), FadeIn(survival), run_time=0.7)
        self.play(GrowArrow(arr_egfr), GrowArrow(arr_surv), run_time=0.7)
        self.play(FadeIn(drug_bar), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(met), run_time=0.5)
        self.play(GrowArrow(arr_met), run_time=0.7)
        self.play(FadeIn(bypass_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.1))


class B09_SelectionSweep(Scene):
    def construct(self):
        total = DUR["B09"]
        # Before: large teal grid with a few crimson; After: teal fades, crimson expands
        per_row = 20
        n_teal = 38
        n_crim = 2
        big_grid = IsotypeGrid([n_teal, n_crim], [TEAL, CRIMSON],
                               per_row=per_row, size=0.20, gap=0.08)
        big_grid.move_to(UP * 0.4)
        before_lbl = Text("tumor at treatment start", font=SERIF, color=INK,
                          font_size=26, slant=ITALIC)
        before_lbl.next_to(big_grid, UP, buff=0.4)
        self.play(FadeIn(before_lbl), run_time=0.4)
        self.play(big_grid.count_up(run_time=1.6))
        self.wait(0.5)
        # fade out teal marks, keep crimson, then grow crimson
        teal_marks = VGroup(*list(big_grid.marks)[: n_teal])
        crim_marks = VGroup(*list(big_grid.marks)[n_teal:])
        self.play(FadeOut(teal_marks), run_time=1.2)
        after_lbl = LabelChip("drug cannot touch MET bypass", accent=CRIMSON, size=22)
        after_lbl.next_to(big_grid, DOWN, buff=0.4)
        self.play(crim_marks.animate.scale(2.5), FadeIn(after_lbl), run_time=0.9)
        self.wait(max(0.5, total - 4.6))


class B10_ResistanceSelected(Scene):
    def construct(self):
        total = DUR["B10"]
        chip = LabelChip("RESISTANCE", accent=CRIMSON, size=36)
        chip.move_to(UP * 0.6)
        line1 = Text("selected, not created.", font=DISPLAY, color=INK,
                     font_size=52, weight="BOLD")
        line1.next_to(chip, DOWN, buff=0.45)
        sub = SerifLabel("the pre-existing minority survives", CRIMSON, size=26)
        sub.next_to(line1, DOWN, buff=0.4)
        self.play(FadeIn(chip, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(line1, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B11_ClonalSelection(Scene):
    def construct(self):
        total = DUR["B11"]
        stages = ["pre-treatment", "3 months", "relapse"]
        stage_xs = [-4.2, 0.0, 4.2]
        # teal bar heights: before=3.0, during=0.5, after=0
        # crimson bar heights: before=0.05, during=0.05, after=3.0
        teal_h = [3.0, 0.5, 0.0]
        crim_h = [0.15, 0.15, 3.0]
        bar_w = 1.6
        y_base = -1.8
        bars = VGroup()
        for i, (x, th, ch, lbl) in enumerate(zip(stage_xs, teal_h, crim_h, stages)):
            if th > 0:
                tb = Rectangle(width=bar_w, height=th)
                tb.set_fill(TEAL, 0.80).set_stroke(width=0, opacity=0)
                tb.move_to(np.array([x, y_base + th / 2, 0]))
                bars.add(tb)
            if ch > 0:
                cb = Rectangle(width=bar_w, height=ch)
                cb.set_fill(CRIMSON, 0.80).set_stroke(width=0, opacity=0)
                cb.move_to(np.array([x, y_base + (th if th > 0 else 0) + ch / 2, 0]))
                bars.add(cb)
            stage_text = Text(lbl, font=SERIF, color=INK, font_size=24, slant=ITALIC)
            stage_text.move_to(np.array([x, y_base - 0.5, 0]))
            bars.add(stage_text)
        teal_legend = LabelChip("EGFR-addicted cells", accent=TEAL, size=20)
        crim_legend = LabelChip("MET-amplified clone", accent=CRIMSON, size=20)
        teal_legend.move_to(UP * 2.8 + LEFT * 2.5)
        crim_legend.next_to(teal_legend, RIGHT, buff=0.6)
        baseline = Line(np.array([-5.5, y_base, 0]), np.array([5.5, y_base, 0]),
                        color=INK, stroke_width=2)
        self.play(FadeIn(teal_legend), FadeIn(crim_legend), run_time=0.6)
        self.play(Create(baseline), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in bars],
                               lag_ratio=0.07), run_time=1.8)
        self.wait(max(0.5, total - 2.9))


class B12_ExampleNumbers(Scene):
    def construct(self):
        total = DUR["B12"]
        total_n = Text("10,000,000,000", font=SERIF, color=INK, font_size=54, weight="BOLD")
        total_n.move_to(UP * 2.0)
        total_lbl = Text("cells in tumor at treatment start  (illustrative)",
                         font=SERIF, color=INK, font_size=24, slant=ITALIC)
        total_lbl.next_to(total_n, DOWN, buff=0.22)
        freq_line = Text("1 in 1,000,000 = MET-amplified",
                         font=SERIF, color=INK, font_size=28)
        freq_line.move_to(UP * 0.4)
        calc_line = Text("10,000,000,000 / 1,000,000 =", font=SERIF, color=INK,
                         font_size=28)
        result = Text("10,000", font=SERIF, color=CRIMSON, font_size=54, weight="BOLD")
        calc_block = VGroup(calc_line, result).arrange(RIGHT, buff=0.35)
        calc_block.move_to(DOWN * 1.0)
        met_lbl = SerifLabel("MET-amplified cells before pill 1  (illustrative)",
                             CRIMSON, size=22)
        met_lbl.next_to(calc_block, DOWN, buff=0.4)
        self.play(FadeIn(total_n, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(total_lbl), run_time=0.5)
        self.play(FadeIn(freq_line, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(calc_line), run_time=0.4)
        self.play(FadeIn(result, scale=0.9), run_time=0.6)
        self.play(FadeIn(met_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.2))


class B13_KillCount(Scene):
    def construct(self):
        total = DUR["B13"]
        # Three columns: BEFORE, AFTER DRUG, OUTCOME
        col_xs = [-4.5, 0.0, 4.5]
        bar_w = 1.8
        y_base = -0.8
        # before: large teal bar + tiny crimson
        tb_before = Rectangle(width=bar_w, height=3.8)
        tb_before.set_fill(TEAL, 0.80).set_stroke(width=0, opacity=0)
        tb_before.move_to(np.array([col_xs[0], y_base + 1.9, 0]))
        cb_before = Rectangle(width=bar_w, height=0.08)
        cb_before.set_fill(CRIMSON, 0.90).set_stroke(width=0, opacity=0)
        cb_before.move_to(np.array([col_xs[0], y_base + 3.84, 0]))
        # after drug: very small teal, same tiny crimson
        tb_after = Rectangle(width=bar_w, height=0.4)
        tb_after.set_fill(TEAL, 0.30).set_stroke(width=0, opacity=0)
        tb_after.move_to(np.array([col_xs[1], y_base + 0.2, 0]))
        cb_after = Rectangle(width=bar_w, height=0.08)
        cb_after.set_fill(CRIMSON, 0.90).set_stroke(width=0, opacity=0)
        cb_after.move_to(np.array([col_xs[1], y_base + 0.44, 0]))
        # outcome: only crimson, grown
        cb_outcome = Rectangle(width=bar_w, height=3.8)
        cb_outcome.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        cb_outcome.move_to(np.array([col_xs[2], y_base + 1.9, 0]))
        lbl_before = Text("before", font=SERIF, color=INK, font_size=24, slant=ITALIC)
        lbl_before.move_to(np.array([col_xs[0], y_base - 0.45, 0]))
        lbl_after = Text("3 months", font=SERIF, color=INK, font_size=24, slant=ITALIC)
        lbl_after.move_to(np.array([col_xs[1], y_base - 0.45, 0]))
        lbl_out = Text("relapse", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        lbl_out.move_to(np.array([col_xs[2], y_base - 0.45, 0]))
        no_effect = SerifLabel("drug: no effect on MET", CRIMSON, size=22)
        no_effect.move_to(UP * 2.8)
        baseline = Line(np.array([-5.8, y_base, 0]), np.array([5.8, y_base, 0]),
                        color=INK, stroke_width=2)
        self.play(Create(baseline), run_time=0.4)
        self.play(FadeIn(tb_before), FadeIn(cb_before), FadeIn(lbl_before), run_time=0.7)
        self.play(FadeIn(tb_after), FadeIn(cb_after), FadeIn(lbl_after), run_time=0.7)
        self.play(FadeIn(no_effect, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(cb_outcome), FadeIn(lbl_out), run_time=0.9)
        self.wait(max(0.5, total - 3.2))


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = LabelChip("CANCER BIOLOGY", accent=TEAL, size=24)
        eye.move_to(UP * 2.6)
        line1 = Text("Perfect blockade of one entry", font=DISPLAY, color=INK,
                     font_size=40, weight="BOLD")
        line2 = Text("cannot close a bypass that already exists.", font=DISPLAY,
                     color=INK, font_size=40, weight="BOLD")
        answer = VGroup(line1, line2).arrange(DOWN, buff=0.18).move_to(UP * 0.5)
        u = Line(line2.get_corner(DL) + DOWN * 0.16,
                 line2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2.5)
        sub = Text("resistance is selected, not created",
                   font=SERIF, color=INK, font_size=26, slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(answer, shift=UP * 0.1), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
