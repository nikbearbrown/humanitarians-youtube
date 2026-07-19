"""vox_scenes.py — Why Tumors Make the Immune Cells That Could Kill Them Run Out of Fuel
(vox-immune-starvation, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
B05 and B09 are STILL (ai media slots) — no scenes here for those.
Durations read from this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law: TEAL #1F6F5C = T cells functional / adequate nutrients / immune system winning;
CRIMSON #BF3339 = T cells exhausted / glucose depleted / cancer winning the competition.
GOLD = editor's-pen highlighter (pool fill only), NEVER text.
Exclusions honored: no PD-1/PD-L1 mechanism detail, no IDO, no arginine, no trial data.
Gate B: every zero-width stroke is also zero-opacity.
"""
import json, os, sys, pathlib

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}

sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np


# ---------------------------------------------------------------- helpers

def _rect(w, h, color, fill_opacity=1.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, fill_opacity).set_stroke(width=0, opacity=0)
    return r


def _cell_icon(center, radius=0.32, color=TEAL, label=None):
    """A simple circle representing a cell."""
    c = Circle(radius=radius)
    c.set_fill(color, 0.18).set_stroke(color, 2.5)
    c.move_to(center)
    grp = VGroup(c)
    if label:
        lbl = LabelChip(label, accent=color, size=18)
        lbl.next_to(c, DOWN, buff=0.18)
        grp.add(lbl)
    return grp


def _pool_rect(center, w=2.8, h=1.4, fill_level=1.0):
    """A nutrient pool rectangle with GOLD fill that can be partially filled."""
    border = Rectangle(width=w, height=h)
    border.set_fill(opacity=0).set_stroke(INK, 2.0)
    border.move_to(center)
    if fill_level > 0:
        filled_h = h * fill_level
        filled = _rect(w - 0.08, filled_h, GOLD, 0.55)
        filled.move_to(center + DOWN * ((h - filled_h) / 2))
    else:
        filled = VGroup()
    return VGroup(border, filled)


# ---------------------------------------------------------------- B01_Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Tumors Starve", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("the Immune Cells That Could Kill Them", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B02_GlucoseGap

class B02_GlucoseGap(Scene):
    """Two bars: serum 5 mM (TEAL) vs tumor 0.5 mM (CRIMSON).
    A dashed threshold line sits between them."""
    def construct(self):
        total = DUR["B02"]

        # parameters
        max_h = 3.2
        bar_w = 1.1
        # left center (serum), right center (tumor)
        lx = -1.4
        rx = 1.4
        base_y = -1.6

        # serum bar (full height = 5 mM)
        serum_h = max_h
        serum = _rect(bar_w, serum_h, TEAL, 0.85)
        serum.move_to(np.array([lx, base_y + serum_h / 2, 0]))

        # tumor bar (one-tenth = 0.5 mM)
        tumor_h = max_h * 0.1
        tumor = _rect(bar_w, tumor_h, CRIMSON, 0.85)
        tumor.move_to(np.array([rx, base_y + tumor_h / 2, 0]))

        # labels
        serum_lbl = LabelChip("Serum  5 mM", accent=TEAL, size=20)
        serum_lbl.next_to(serum, UP, buff=0.22)
        tumor_lbl = LabelChip("Tumor  0.5 mM", accent=CRIMSON, size=20)
        tumor_lbl.next_to(tumor, UP, buff=0.22)

        # baseline
        baseline = Line(
            np.array([lx - 0.9, base_y, 0]),
            np.array([rx + 0.9, base_y, 0]),
            color=INK, stroke_width=1.5
        )
        baseline.set_stroke(opacity=0.5)

        # threshold dashed line (at ~25% of max height above baseline)
        thresh_y_val = base_y + max_h * 0.25
        thresh = DashedLine(
            np.array([lx - 0.9, thresh_y_val, 0]),
            np.array([rx + 0.9, thresh_y_val, 0]),
            color=INK, stroke_width=1.6, dash_length=0.18
        )
        thresh_lbl = SerifLabel("T cell activation threshold", INK, size=22)
        thresh_lbl.next_to(thresh, RIGHT, buff=0.25)

        # axis label — horizontal to stay in frame
        axis_lbl = SerifLabel("Glucose (mM)", INK, size=20)
        axis_lbl.move_to(np.array([-4.8, 1.0, 0]))

        self.play(
            FadeIn(baseline),
            FadeIn(axis_lbl),
            run_time=0.6
        )
        self.play(
            GrowFromEdge(serum, DOWN),
            run_time=0.9
        )
        self.play(FadeIn(serum_lbl, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            GrowFromEdge(tumor, DOWN),
            run_time=0.7
        )
        self.play(FadeIn(tumor_lbl, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            Create(thresh),
            FadeIn(thresh_lbl, shift=LEFT * 0.3),
            run_time=0.9
        )
        self.wait(max(0.3, total - 4.1))


# ---------------------------------------------------------------- B03_Question (CARD)

class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q = Text("Checkpoint inhibitors release the T cell brakes.",
                 font=SERIF, color=INK, font_size=26)
        q2 = Text("Here the T cells still fail after the brakes are released.",
                  font=SERIF, color=INK, font_size=26)
        q3 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=38, weight=BOLD)
        block = VGroup(q, q2, q3).arrange(DOWN, buff=0.28).move_to(ORIGIN)
        u = Line(q3.get_corner(DL) + DOWN * 0.12, q3.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q), run_time=0.7)
        self.play(FadeIn(q2), run_time=0.7)
        self.play(FadeIn(q3), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.2))


# ---------------------------------------------------------------- B04_TCellNeeds

class B04_TCellNeeds(Scene):
    """T cell center; two arms: proliferate + cytokine synthesis; both point to ATP box."""
    def construct(self):
        total = DUR["B04"]

        # central T cell
        tcell = Circle(radius=0.5)
        tcell.set_fill(TEAL, 0.15).set_stroke(TEAL, 2.5)
        tcell.move_to(ORIGIN)
        tcell_lbl = LabelChip("T cell", accent=TEAL, size=20)
        tcell_lbl.move_to(tcell.get_center())

        # arm targets
        prolif_box = _rect(2.2, 0.5, TEAL, 0.12)
        prolif_box.set_stroke(TEAL, 1.5)
        prolif_box.move_to(UP * 1.8 + RIGHT * 3.0)
        prolif_txt = Text("Proliferate", font=DISPLAY, color=TEAL, font_size=20)
        prolif_txt.move_to(prolif_box.get_center())

        cyto_box = _rect(2.2, 0.5, CRIMSON, 0.05)
        cyto_box.set_stroke(CRIMSON, 1.5)
        cyto_box.move_to(DOWN * 0.8 + RIGHT * 3.0)
        cyto_txt = Text("Synthesize cytotoxins", font=DISPLAY, color=CRIMSON, font_size=18)
        cyto_txt.move_to(cyto_box.get_center())

        # ATP result box
        atp_box = _rect(2.8, 0.65, TEAL, 0.1)
        atp_box.set_stroke(TEAL, 1.5)
        atp_box.move_to(RIGHT * 5.8)
        atp_txt = Text("requires ATP", font=DISPLAY, color=INK, font_size=20)
        atp_sub = Text("from glucose", font=SERIF, color=TEAL, font_size=18)
        VGroup(atp_txt, atp_sub).arrange(DOWN, buff=0.1).move_to(atp_box.get_center())

        # arrows
        arr1 = Arrow(tcell.get_right() + UP * 0.2, prolif_box.get_left(),
                     color=TEAL, stroke_width=2.5, max_tip_length_to_length_ratio=0.18)
        arr2 = Arrow(tcell.get_right() + DOWN * 0.2, cyto_box.get_left(),
                     color=CRIMSON, stroke_width=2.5, max_tip_length_to_length_ratio=0.18)
        arr3 = Arrow(prolif_box.get_right(), atp_box.get_left() + UP * 0.15,
                     color=TEAL, stroke_width=2.0, max_tip_length_to_length_ratio=0.15)
        arr4 = Arrow(cyto_box.get_right(), atp_box.get_left() + DOWN * 0.15,
                     color=CRIMSON, stroke_width=2.0, max_tip_length_to_length_ratio=0.15)

        grp = VGroup(tcell, tcell_lbl, prolif_box, prolif_txt, cyto_box, cyto_txt,
                     atp_box, atp_txt, atp_sub, arr1, arr2, arr3, arr4)
        grp.center().scale(0.92)

        self.play(FadeIn(tcell), FadeIn(tcell_lbl), run_time=0.6)
        self.play(
            GrowArrow(arr1), FadeIn(prolif_box), FadeIn(prolif_txt), run_time=0.8
        )
        self.play(
            GrowArrow(arr2), FadeIn(cyto_box), FadeIn(cyto_txt), run_time=0.8
        )
        self.play(
            GrowArrow(arr3), GrowArrow(arr4),
            FadeIn(atp_box), FadeIn(atp_txt), FadeIn(atp_sub),
            run_time=0.9
        )
        self.wait(max(0.3, total - 3.1))


# ---------------------------------------------------------------- B06_GlucoseDrain

class B06_GlucoseDrain(Scene):
    """Shared pool draining: cancer large CRIMSON arrow, T cell small TEAL arrow.
    Pool fill drops visually (accumulate move)."""
    def construct(self):
        total = DUR["B06"]

        pool_center = ORIGIN
        pool_w, pool_h = 3.0, 1.8

        # pool border
        pool_border = Rectangle(width=pool_w, height=pool_h)
        pool_border.set_fill(opacity=0).set_stroke(INK, 2.2)
        pool_border.move_to(pool_center)
        pool_lbl = SerifLabel("Shared glucose pool", INK, size=22)
        pool_lbl.next_to(pool_border, UP, buff=0.22)

        # full fill
        fill_full = _rect(pool_w - 0.1, pool_h - 0.1, GOLD, 0.55)
        fill_full.move_to(pool_center)

        # empty fill state (for replacement)
        fill_empty = _rect(pool_w - 0.1, 0.18, GOLD, 0.55)
        fill_empty.align_to(pool_border, DOWN).shift(UP * 0.05)

        # cancer cluster on left
        cancer_cells = VGroup()
        for i in range(3):
            c = Circle(radius=0.22)
            c.set_fill(CRIMSON, 0.22).set_stroke(CRIMSON, 2.0)
            c.move_to(LEFT * 5.0 + UP * (i - 1) * 0.55)
            cancer_cells.add(c)
        cancer_lbl = LabelChip("Cancer cells", accent=CRIMSON, size=18)
        cancer_lbl.next_to(cancer_cells, DOWN, buff=0.2)
        warburg_lbl = SerifLabel("Warburg: 10x rate", CRIMSON, size=19)
        warburg_lbl.next_to(cancer_cells, UP, buff=0.22)

        # T cells on right
        tcells = VGroup()
        for i in range(2):
            c = Circle(radius=0.18)
            c.set_fill(TEAL, 0.18).set_stroke(TEAL, 2.0)
            c.move_to(RIGHT * 5.0 + UP * (i - 0.5) * 0.45)
            tcells.add(c)
        tcell_lbl = LabelChip("T cells", accent=TEAL, size=18)
        tcell_lbl.next_to(tcells, DOWN, buff=0.2)

        # arrows
        cancer_arr = Arrow(pool_border.get_left(), cancer_cells.get_right(),
                           color=CRIMSON, stroke_width=5.0,
                           max_tip_length_to_length_ratio=0.14)
        tcell_arr = Arrow(pool_border.get_right(), tcells.get_left(),
                          color=TEAL, stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.14)

        self.play(
            FadeIn(pool_border), FadeIn(pool_lbl),
            FadeIn(fill_full),
            run_time=0.7
        )
        self.play(
            FadeIn(cancer_cells), FadeIn(cancer_lbl), FadeIn(warburg_lbl),
            FadeIn(tcells), FadeIn(tcell_lbl),
            run_time=0.7
        )
        self.play(GrowArrow(cancer_arr), GrowArrow(tcell_arr), run_time=0.9)
        # drain the pool (accumulate move)
        self.play(
            ReplacementTransform(fill_full, fill_empty),
            run_time=2.2
        )
        # show depleted label
        depleted = LabelChip("Depleted", accent=CRIMSON, size=22)
        depleted.move_to(pool_center)
        self.play(FadeIn(depleted, scale=0.9), run_time=0.6)
        self.wait(max(0.3, total - 5.1))


# ---------------------------------------------------------------- B07_FuelGauge

class B07_FuelGauge(Scene):
    """Fuel gauge on the left at near-empty; two-state comparison on the right."""
    def construct(self):
        total = DUR["B07"]

        # gauge body
        gauge_w, gauge_h = 1.0, 2.6
        gauge = Rectangle(width=gauge_w, height=gauge_h)
        gauge.set_fill(WHITE, 0.3).set_stroke(INK, 2.0)
        gauge.move_to(LEFT * 4.5)

        # filled portion (tiny — near empty)
        fill_h = gauge_h * 0.08
        gauge_fill = _rect(gauge_w - 0.1, fill_h, CRIMSON, 0.85)
        gauge_fill.align_to(gauge, DOWN).shift(UP * 0.05 + RIGHT * 0)
        gauge_fill.set_x(gauge.get_center()[0])

        # gauge label
        gauge_title = SerifLabel("T cell glucose supply", INK, size=20)
        gauge_title.next_to(gauge, UP, buff=0.22)
        empty_lbl = LabelChip("EMPTY", accent=CRIMSON, size=20)
        empty_lbl.next_to(gauge, DOWN, buff=0.22)

        # dividing line
        divider = Line(LEFT * 2.8 + UP * 1.8, LEFT * 2.8 + DOWN * 1.8,
                       color=INK, stroke_width=1.2)
        divider.set_stroke(opacity=0.35)

        # right panel: two states
        # top state (TEAL - adequate)
        ok_box = _rect(4.6, 0.9, TEAL, 0.08)
        ok_box.set_stroke(TEAL, 1.5)
        ok_box.move_to(RIGHT * 1.8 + UP * 1.2)
        ok_txt = Text("Glucose adequate:", font=DISPLAY, color=TEAL, font_size=19)
        ok_sub = Text("proliferates, kills", font=SERIF, color=TEAL, font_size=18)
        VGroup(ok_txt, ok_sub).arrange(RIGHT, buff=0.25).move_to(ok_box.get_center())

        # bottom state (CRIMSON - depleted)
        bad_box = _rect(4.6, 0.9, CRIMSON, 0.08)
        bad_box.set_stroke(CRIMSON, 1.5)
        bad_box.move_to(RIGHT * 1.8 + DOWN * 0.5)
        bad_txt = Text("Glucose < 0.5 mM:", font=DISPLAY, color=CRIMSON, font_size=19)
        bad_sub = Text("ATP falls, exhausted", font=SERIF, color=CRIMSON, font_size=18)
        VGroup(bad_txt, bad_sub).arrange(RIGHT, buff=0.25).move_to(bad_box.get_center())

        # arrow from gauge to bad state
        gauge_arr = Arrow(gauge.get_right(), bad_box.get_left() + LEFT * 0.1,
                          color=CRIMSON, stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.18)

        self.play(
            FadeIn(gauge), FadeIn(gauge_fill), FadeIn(gauge_title),
            run_time=0.7
        )
        self.play(FadeIn(empty_lbl, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(divider), run_time=0.4)
        self.play(
            FadeIn(ok_box), FadeIn(ok_txt), FadeIn(ok_sub), run_time=0.7
        )
        self.play(
            FadeIn(bad_box), FadeIn(bad_txt), FadeIn(bad_sub), run_time=0.7
        )
        self.play(GrowArrow(gauge_arr), run_time=0.7)
        self.wait(max(0.3, total - 3.7))


# ---------------------------------------------------------------- B08_LactateCard (CARD)

class B08_LactateCard(Scene):
    def construct(self):
        total = DUR["B08"]
        t1 = Text("The cancer's waste product", font=SERIF, color=INK,
                  font_size=30, weight=BOLD)
        t2 = Text("is also an immune suppressant.", font=SERIF, color=CRIMSON,
                  font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 1.5))


# ---------------------------------------------------------------- B10_TwoMechanisms

class B10_TwoMechanisms(Scene):
    """Two panels: signaling model (old) vs metabolic model (new)."""
    def construct(self):
        total = DUR["B10"]

        # panel divider
        divider = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=1.2)
        divider.set_stroke(opacity=0.3)

        # --- left panel: signaling model ---
        l_title = LabelChip("Signaling model", accent=SLATE, size=20)
        l_title.move_to(LEFT * 3.5 + UP * 2.0)

        l_tcell = Circle(radius=0.32)
        l_tcell.set_fill(TEAL, 0.15).set_stroke(TEAL, 2.0)
        l_tcell.move_to(LEFT * 4.8 + UP * 0.3)
        l_tl = LabelChip("T cell", accent=TEAL, size=16)
        l_tl.next_to(l_tcell, DOWN, buff=0.15)

        # inhibitory bar (the brake)
        l_brake = _rect(1.0, 0.18, CRIMSON, 0.9)
        l_brake.move_to(LEFT * 3.5 + UP * 0.3)
        l_brake_lbl = SerifLabel("molecular stop signal", CRIMSON, size=18)
        l_brake_lbl.next_to(l_brake, DOWN, buff=0.2)

        # arrow blocked
        l_arr = Arrow(l_tcell.get_right(), l_brake.get_left(),
                      color=TEAL, stroke_width=2.0,
                      max_tip_length_to_length_ratio=0.2)
        l_blocked = Text("BLOCKED", font=DISPLAY, color=CRIMSON, font_size=18)
        l_blocked.next_to(l_arr, UP, buff=0.12)

        # --- right panel: metabolic model ---
        r_title = LabelChip("Metabolic model", accent=CRIMSON, size=20)
        r_title.move_to(RIGHT * 3.5 + UP * 2.0)

        r_tcell = Circle(radius=0.32)
        r_tcell.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2.0)
        r_tcell.move_to(RIGHT * 1.8 + UP * 0.3)
        r_tl = LabelChip("T cell", accent=CRIMSON, size=16)
        r_tl.next_to(r_tcell, DOWN, buff=0.15)

        # empty gauge
        gauge_mini = Rectangle(width=0.28, height=0.7)
        gauge_mini.set_fill(WHITE, 0.3).set_stroke(INK, 1.5)
        gauge_mini.next_to(r_tcell, RIGHT, buff=0.3).shift(UP * 0.05)
        gauge_dot = _rect(0.22, 0.07, CRIMSON, 0.9)
        gauge_dot.align_to(gauge_mini, DOWN).shift(UP * 0.04)
        gauge_dot.set_x(gauge_mini.get_center()[0])

        r_lbl = SerifLabel("nutrients consumed", CRIMSON, size=18)
        r_lbl.next_to(r_tcell, DOWN, buff=0.4)

        no_fuel = LabelChip("no fuel to go", accent=CRIMSON, size=20)
        no_fuel.next_to(r_tcell, RIGHT, buff=1.1).shift(DOWN * 0.2)

        self.play(FadeIn(divider), run_time=0.4)
        self.play(
            FadeIn(l_title), FadeIn(r_title), run_time=0.6
        )
        # left panel
        self.play(
            FadeIn(l_tcell), FadeIn(l_tl), run_time=0.6
        )
        self.play(
            GrowArrow(l_arr), FadeIn(l_brake), FadeIn(l_brake_lbl),
            FadeIn(l_blocked), run_time=0.9
        )
        # right panel
        self.play(
            FadeIn(r_tcell), FadeIn(r_tl), run_time=0.6
        )
        self.play(
            FadeIn(gauge_mini), FadeIn(gauge_dot),
            FadeIn(r_lbl), FadeIn(no_fuel),
            run_time=0.9
        )
        self.wait(max(0.3, total - 4.0))


# ---------------------------------------------------------------- B11_CheckpointCard (CARD)

class B11_CheckpointCard(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Checkpoint removes the brake.", font=SERIF, color=TEAL,
                  font_size=30, weight=BOLD)
        t2 = Text("It cannot restore the fuel.", font=SERIF, color=CRIMSON,
                  font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 1.5))


# ---------------------------------------------------------------- B12_ExampleTimeline

class B12_ExampleTimeline(Scene):
    """48-hour dual time-series: glucose falls (CRIMSON), T cell function follows (TEAL).
    Threshold dashed line. Annotated with illustrative chip."""
    def construct(self):
        total = DUR["B12"]

        # axes setup
        ax_origin = LEFT * 5.5 + DOWN * 1.8
        ax_w = 9.0
        ax_h = 3.6

        x_axis = Arrow(ax_origin, ax_origin + RIGHT * ax_w,
                       color=INK, stroke_width=2.0,
                       max_tip_length_to_length_ratio=0.04)
        y_axis = Arrow(ax_origin, ax_origin + UP * ax_h,
                       color=INK, stroke_width=2.0,
                       max_tip_length_to_length_ratio=0.04)

        # time labels
        t_labels = []
        for i, t in enumerate(["0h", "24h", "48h"]):
            lbl = Text(t, font=MONO, color=INK, font_size=20)
            lbl.move_to(ax_origin + RIGHT * (i * ax_w / 2) + DOWN * 0.32)
            t_labels.append(lbl)

        y_lbl = SerifLabel("Function / Glucose level", INK, size=19)
        y_lbl.rotate(PI / 2)
        y_lbl.next_to(y_axis, LEFT, buff=0.15)

        # threshold line
        thresh_y = ax_h * 0.2  # at 0.5/5 = 10% of max, but make visible: 20%
        thresh_line = DashedLine(
            ax_origin + RIGHT * 0.15 + UP * thresh_y,
            ax_origin + RIGHT * (ax_w - 0.3) + UP * thresh_y,
            color=INK, stroke_width=1.5, dash_length=0.2
        )
        thresh_lbl = SerifLabel("Activation threshold (0.5 mM)", INK, size=18)
        thresh_lbl.next_to(thresh_line, RIGHT, buff=0.15)

        # glucose trace: starts at top-left, drops steeply to 10% by 24h, stays flat
        def gpt(time_frac, val_frac):
            return ax_origin + RIGHT * time_frac * ax_w + UP * val_frac * ax_h

        glucose_points = [gpt(0, 0.9), gpt(0.5, 0.06), gpt(1.0, 0.06)]
        glucose_line = VMobject(color=CRIMSON, stroke_width=3.5)
        glucose_line.set_points_smoothly([np.array([p[0], p[1], 0]) for p in glucose_points])
        gluc_lbl = LabelChip("Interstitial glucose", accent=CRIMSON, size=18)
        gluc_lbl.next_to(gpt(0.1, 0.9), UP, buff=0.12)

        # T cell function trace: holds high until 24h, then drops to near 0 by 48h
        tcell_points = [gpt(0, 0.85), gpt(0.45, 0.82), gpt(0.55, 0.82), gpt(1.0, 0.04)]
        tcell_line = VMobject(color=TEAL, stroke_width=3.5)
        tcell_line.set_points_smoothly([np.array([p[0], p[1], 0]) for p in tcell_points])
        tcell_lbl = LabelChip("T cell function", accent=TEAL, size=18)
        tcell_lbl.next_to(gpt(0.15, 0.85), DOWN, buff=0.22)

        # annotations
        count_note = SerifLabel("10M cancer cells · 50K T cells · 1 cm3", SLATE, size=17)
        count_note.to_corner(UR, buff=0.5)

        # illustrative chip
        illus = LabelChip("ILLUSTRATIVE", accent=SLATE, size=17)
        illus.to_corner(DR, buff=0.5)

        self.play(
            Create(x_axis), Create(y_axis),
            *[FadeIn(l) for l in t_labels],
            FadeIn(y_lbl),
            run_time=0.9
        )
        self.play(Create(thresh_line), FadeIn(thresh_lbl), run_time=0.7)
        self.play(
            Create(glucose_line), FadeIn(gluc_lbl), run_time=1.4
        )
        self.play(
            Create(tcell_line), FadeIn(tcell_lbl), run_time=1.4
        )
        self.play(FadeIn(count_note), FadeIn(illus), run_time=0.6)
        self.wait(max(0.3, total - 5.0))


# ---------------------------------------------------------------- B13_ReverseWarburg

class B13_ReverseWarburg(Scene):
    """Three-cell triangle: cancer (top), fibroblast (lower-left), T cell (lower-right).
    Shared pool below center. Arrows showing metabolic flows."""
    def construct(self):
        total = DUR["B13"]

        # positions
        cancer_pos = UP * 1.8
        fibro_pos = LEFT * 3.2 + DOWN * 1.0
        tcell_pos = RIGHT * 3.2 + DOWN * 1.0
        pool_pos = DOWN * 0.2

        # pool
        pool_border = Rectangle(width=2.2, height=0.9)
        pool_border.set_fill(opacity=0).set_stroke(INK, 2.0)
        pool_border.move_to(pool_pos)
        pool_fill = _rect(2.1, 0.4, GOLD, 0.45)
        pool_fill.align_to(pool_border, DOWN).shift(UP * 0.08)
        pool_fill.set_x(pool_pos[0])
        pool_lbl = SerifLabel("Shared nutrient pool", INK, size=19)
        pool_lbl.next_to(pool_border, DOWN, buff=0.18)

        # cancer cell
        cancer = Circle(radius=0.48)
        cancer.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.5)
        cancer.move_to(cancer_pos)
        cancer_lbl = LabelChip("Cancer", accent=CRIMSON, size=18)
        cancer_lbl.next_to(cancer, UP, buff=0.15)

        # fibroblast
        fibro = Circle(radius=0.35)
        fibro.set_fill(SLATE, 0.15).set_stroke(SLATE, 2.0)
        fibro.move_to(fibro_pos)
        fibro_lbl = LabelChip("Fibroblast", accent=SLATE, size=17)
        fibro_lbl.next_to(fibro, LEFT, buff=0.15)

        # T cell (dim)
        tcell = Circle(radius=0.32)
        tcell.set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 1.8)
        tcell.move_to(tcell_pos)
        tcell_lbl = LabelChip("T cell", accent=CRIMSON, size=17)
        tcell_lbl.next_to(tcell, RIGHT, buff=0.15)

        # arrows
        # fibroblast exports lactate to cancer (reverse Warburg)
        fibro_to_cancer = CurvedArrow(fibro.get_top(), cancer.get_left() + DOWN * 0.1,
                                      color=CRIMSON, stroke_width=2.5,
                                      angle=-TAU / 6)
        rw_lbl = SerifLabel("lactate (reverse Warburg)", CRIMSON, size=16)
        rw_lbl.move_to(LEFT * 2.0 + UP * 0.8)

        # cancer drains pool
        cancer_to_pool = Arrow(cancer.get_bottom(), pool_border.get_top() + LEFT * 0.3,
                               color=CRIMSON, stroke_width=3.5,
                               max_tip_length_to_length_ratio=0.18)

        # fibroblast drains pool
        fibro_to_pool = Arrow(fibro.get_right(), pool_border.get_left() + DOWN * 0.1,
                              color=SLATE, stroke_width=2.0,
                              max_tip_length_to_length_ratio=0.18)

        # T cell blocked from pool
        tcell_to_pool = Arrow(tcell.get_left(), pool_border.get_right() + DOWN * 0.1,
                              color=TEAL, stroke_width=1.5,
                              max_tip_length_to_length_ratio=0.18)
        # blocking bar on the T cell arrow
        block_bar = _rect(0.18, 0.5, CRIMSON, 0.9)
        block_bar.move_to(tcell.get_left() + LEFT * 0.6 + DOWN * 0.05)
        block_bar.set_stroke(CRIMSON, 1.0)

        # shut out label
        shut_lbl = LabelChip("T cell shut out", accent=CRIMSON, size=18)
        shut_lbl.next_to(tcell, DOWN, buff=0.4)

        self.play(
            FadeIn(pool_border), FadeIn(pool_fill), FadeIn(pool_lbl),
            run_time=0.6
        )
        self.play(
            FadeIn(cancer), FadeIn(cancer_lbl),
            FadeIn(fibro), FadeIn(fibro_lbl),
            FadeIn(tcell), FadeIn(tcell_lbl),
            run_time=0.8
        )
        self.play(
            GrowArrow(cancer_to_pool),
            GrowArrow(fibro_to_pool),
            run_time=0.9
        )
        self.play(
            Create(fibro_to_cancer), FadeIn(rw_lbl), run_time=0.9
        )
        self.play(
            GrowArrow(tcell_to_pool), FadeIn(block_bar),
            FadeIn(shut_lbl),
            run_time=0.9
        )
        self.wait(max(0.3, total - 4.1))


# ---------------------------------------------------------------- B14_Endcard (CARD)

class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The brake is released —", font=DISPLAY, color=TEAL,
                  font_size=26, weight=BOLD)
        t2 = Text("but the tank is empty.", font=DISPLAY, color=CRIMSON,
                  font_size=26, weight=BOLD)
        t3 = Text("Cancer starves the immune cells that could kill it.",
                  font=SERIF, color=INK, font_size=22)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        sub = SerifLabel("metabolic competition as immune evasion", SLATE, size=20)
        sub.next_to(block, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.0))
