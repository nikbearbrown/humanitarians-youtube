"""vox_scenes.py — Your Targeted Nanoparticle Doesn't Reach More Tumor.
It Just Enters More Cells. (vox-targeting-uptake, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from
beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law:
  TEAL   = particle accumulation in tumor / what is actually measured
  CRIMSON = cell uptake / the last-step-only action
  GOLD   = the binding step (editor's pen, fill only, never text)

EXCLUSIONS: protein corona, EC145 case, 0.7% figure, EPR contested status.
One claim: uptake does not equal accumulation, because the ligand acts last.

Gate B: every zero-width stroke is also zero-opacity, or the layout audit
strikes it.
"""
import sys, pathlib
# Resolve vox_graphics from this file's absolute location — works whether manim
# is invoked from the reel dir, the book root, or the vox toolkit root.
_VOX_MANIM = (pathlib.Path(__file__).resolve().parent
              .parent.parent.parent / "vox/aspects/explainer/vox-explainer/manim")
if str(_VOX_MANIM) not in sys.path:
    sys.path.insert(0, str(_VOX_MANIM))
from vox_graphics import *
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 11)}

import numpy as np

# ---------------------------------------------------------------- helpers

BAR_W = 2.0
BAR_H_UNIT = 3.0   # full height for a 100% bar


def _bar(color, frac=1.0, w=BAR_W, max_h=BAR_H_UNIT):
    h = max(0.15, frac * max_h)
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 0.85).set_stroke(width=0, opacity=0)
    return r


def _step_rect(label_text, color, w=2.2, h=0.62):
    """One step in a delivery chain."""
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 0.18).set_stroke(color, 2.2)
    lbl = Text(label_text, font=DISPLAY, color=color,
               font_size=20, weight=BOLD)
    if lbl.width > w * 0.88:
        lbl.scale_to_fit_width(w * 0.88)
    lbl.move_to(r)
    return VGroup(r, lbl)


def _arrow_right(start, end, color=TEAL):
    return Arrow(start, end, color=color, stroke_width=3,
                 tip_length=0.22, buff=0.0)


def _particle_dot(color=TEAL, radius=0.22):
    d = Dot(radius=radius)
    d.set_fill(color, 1).set_stroke(color, 1)
    return d


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Your Targeted Nanoparticle", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("Doesn't Reach More Tumor.", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        t3 = Text("It Just Enters More Cells.", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.12).move_to(UP * 0.1)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.45)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    """Gap formula card — the question on screen before the answer."""
    def construct(self):
        total = DUR["B03"]
        # Teal chip: ACCUMULATION
        chip_acc = LabelChip("ACCUMULATION", accent=TEAL, size=22)
        chip_acc.move_to(LEFT * 3.8 + UP * 1.2)
        # Crimson chip: UPTAKE
        chip_upt = LabelChip("UPTAKE", accent=CRIMSON, size=22)
        chip_upt.move_to(RIGHT * 3.8 + UP * 1.2)
        # Central question text
        q1 = Text("The ligand works.", font=SERIF, color=INK,
                  font_size=36, weight=BOLD)
        q2 = Text("Why doesn't it help?", font=SERIF, color=CRIMSON,
                  font_size=36, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.18).move_to(DOWN * 0.2)
        u = Line(block.get_corner(DL) + DOWN * 0.15,
                 block.get_corner(DR) + DOWN * 0.15,
                 color=GOLD, stroke_width=2.5)
        # Separator line between chips
        sep = Line(LEFT * 0.6 + UP * 1.2, RIGHT * 0.6 + UP * 1.2,
                   color=INK, stroke_width=1.2)
        sep.set_opacity(0.35)
        self.play(FadeIn(chip_acc, shift=RIGHT * 0.3),
                  FadeIn(chip_upt, shift=LEFT * 0.3),
                  run_time=0.8)
        self.play(FadeIn(sep), run_time=0.4)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.3, total - 2.3))


class B04_DeliveryChain(Scene):
    """Four delivery steps — ligand acts only at the last."""
    def construct(self):
        total = DUR["B04"]
        steps_data = [
            ("BLOOD", TEAL),
            ("VESSEL WALL", TEAL),
            ("TUMOR TISSUE", TEAL),
            ("CELL SURFACE", CRIMSON),
        ]
        steps = [_step_rect(lbl, col) for lbl, col in steps_data]
        chain = VGroup(*steps).arrange(RIGHT, buff=0.55).move_to(UP * 0.4)
        arrows = VGroup()
        for i in range(len(steps) - 1):
            a = _arrow_right(
                steps[i].get_right() + RIGHT * 0.05,
                steps[i + 1].get_left() + LEFT * 0.05,
                color=INK
            )
            arrows.add(a)
        # annotation under last step
        ann = SerifLabel("ligand acts only here", CRIMSON, size=22)
        ann.next_to(steps[-1], DOWN, buff=0.45)
        # animate: chain draws on step by step
        self.play(FadeIn(steps[0], shift=RIGHT * 0.3), run_time=0.5)
        for i, step in enumerate(steps[1:]):
            self.play(GrowArrow(arrows[i]),
                      FadeIn(step, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(ann, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.3, total - (0.5 + 3 * 0.5 + 0.7)))


class B05_CultureVsBody(Scene):
    """What cell culture measures vs what the body requires."""
    def construct(self):
        total = DUR["B05"]
        # Left column: cell culture
        lhdr = LabelChip("CELL CULTURE", accent=TEAL, size=22)
        # Steps visible in culture (only step 4)
        s_blood_l   = _step_rect("BLOOD", INK)
        s_vessel_l  = _step_rect("VESSEL WALL", INK)
        s_tissue_l  = _step_rect("TUMOR TISSUE", INK)
        s_cell_l    = _step_rect("CELL SURFACE", CRIMSON)
        for s in (s_blood_l, s_vessel_l, s_tissue_l):
            s.set_opacity(0.22)
        lcol_steps = VGroup(s_blood_l, s_vessel_l, s_tissue_l, s_cell_l)
        lcol_steps.arrange(DOWN, buff=0.18)
        lcol = VGroup(lhdr, lcol_steps).arrange(DOWN, buff=0.28)
        lcol.move_to(LEFT * 3.4 + DOWN * 0.2)
        lhdr.next_to(lcol_steps, UP, buff=0.28)

        # Right column: in the animal
        rhdr = LabelChip("IN THE ANIMAL", accent=TEAL, size=22)
        s_blood_r  = _step_rect("BLOOD", TEAL)
        s_vessel_r = _step_rect("VESSEL WALL", TEAL)
        s_tissue_r = _step_rect("TUMOR TISSUE", TEAL)
        s_cell_r   = _step_rect("CELL SURFACE", CRIMSON)
        rcol_steps = VGroup(s_blood_r, s_vessel_r, s_tissue_r, s_cell_r)
        rcol_steps.arrange(DOWN, buff=0.18)
        rcol = VGroup(rhdr, rcol_steps).arrange(DOWN, buff=0.28)
        rcol.move_to(RIGHT * 3.4 + DOWN * 0.2)
        rhdr.next_to(rcol_steps, UP, buff=0.28)

        # Bring in columns
        self.play(FadeIn(lcol, shift=RIGHT * 0.4),
                  FadeIn(rcol, shift=LEFT * 0.4), run_time=1.0)
        # ring around top 3 steps of right column
        bracket_target = VGroup(s_blood_r, s_vessel_r, s_tissue_r)
        ring = HandRing(bracket_target, color=TEAL)
        ann = SerifLabel("steps 1-3 unmeasured in culture", TEAL, size=20)
        ann.next_to(bracket_target, RIGHT, buff=0.3)
        self.play(Create(ring), FadeIn(ann, shift=LEFT * 0.2), run_time=1.1)
        self.wait(max(0.3, total - 2.1))


class B06_AccumulationDrivers(Scene):
    """What sets tumor accumulation — two upstream drivers."""
    def construct(self):
        total = DUR["B06"]
        # Tumor bucket in center-right
        tumor_box = Rectangle(width=2.4, height=2.2)
        tumor_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2.5)
        tumor_box.move_to(RIGHT * 3.0)
        tumor_lbl = LabelChip("TUMOR", accent=TEAL, size=24)
        tumor_lbl.next_to(tumor_box, DOWN, buff=0.25)

        # Teal arrows: circulation half-life (top) and vessel permeability (bottom)
        circ_start = LEFT * 3.5 + UP * 1.2
        circ_end   = tumor_box.get_left() + UP * 0.5
        vessel_start = LEFT * 3.5 + DOWN * 1.2
        vessel_end   = tumor_box.get_left() + DOWN * 0.5

        arr_circ   = Arrow(circ_start, circ_end, color=TEAL,
                           stroke_width=3, tip_length=0.22, buff=0.0)
        arr_vessel = Arrow(vessel_start, vessel_end, color=TEAL,
                           stroke_width=3, tip_length=0.22, buff=0.0)

        lbl_circ   = SerifLabel("circulation half-life", TEAL, size=22)
        lbl_circ.next_to(arr_circ, UP, buff=0.12)
        lbl_vessel = SerifLabel("vessel permeability", TEAL, size=22)
        lbl_vessel.next_to(arr_vessel, DOWN, buff=0.12)

        # Crimson arrow from ligand — barred
        lig_start = LEFT * 3.5 + ORIGIN
        lig_end   = LEFT * 1.3 + ORIGIN
        arr_lig = Arrow(lig_start, lig_end, color=CRIMSON,
                        stroke_width=3, tip_length=0.22, buff=0.0)
        lbl_lig = SerifLabel("targeting ligand", CRIMSON, size=22)
        lbl_lig.next_to(arr_lig, UP, buff=0.12)
        # cross-bar to show "barred"
        bar_x = (lig_start[0] + lig_end[0]) / 2
        bar_center = np.array([bar_x, 0, 0])
        cross = Line(bar_center + UP * 0.35, bar_center + DOWN * 0.35,
                     color=CRIMSON, stroke_width=5)
        lbl_no = SerifLabel("no effect on accumulation", CRIMSON, size=20)
        lbl_no.next_to(arr_lig, DOWN, buff=0.14)

        self.play(FadeIn(tumor_box), FadeIn(tumor_lbl), run_time=0.6)
        self.play(GrowArrow(arr_circ), FadeIn(lbl_circ), run_time=0.7)
        self.play(GrowArrow(arr_vessel), FadeIn(lbl_vessel), run_time=0.7)
        self.play(GrowArrow(arr_lig), FadeIn(lbl_lig), run_time=0.6)
        self.play(Create(cross), FadeIn(lbl_no), run_time=0.7)
        self.wait(max(0.3, total - 3.3))


class B07_LastStep(Scene):
    """Equal arrival; targeted particle enters the cell — the compare."""
    def construct(self):
        total = DUR["B07"]
        # Tumor tissue box
        tissue = Rectangle(width=5.5, height=3.2)
        tissue.set_fill(TEAL, 0.07).set_stroke(TEAL, 2.0)
        tissue.move_to(RIGHT * 1.5 + DOWN * 0.2)
        tissue_lbl = LabelChip("TUMOR TISSUE", accent=TEAL, size=20)
        tissue_lbl.next_to(tissue, UP, buff=0.2)

        # Two particle dots arriving
        p_target   = _particle_dot(TEAL, radius=0.26)
        p_bare     = _particle_dot(TEAL, radius=0.26)
        p_target.move_to(LEFT * 5.5 + UP * 0.6)
        p_bare.move_to(LEFT * 5.5 + DOWN * 0.6)

        lbl_target = LabelChip("TARGETED", accent=TEAL, size=18)
        lbl_target.next_to(p_target, LEFT, buff=0.15)
        lbl_bare   = LabelChip("UNTARGETED", accent=TEAL, size=18)
        lbl_bare.next_to(p_bare, LEFT, buff=0.15)

        # Arrival positions inside tumor tissue
        arr_pos_t = tissue.get_left() + RIGHT * 1.2 + UP * 0.6
        arr_pos_b = tissue.get_left() + RIGHT * 1.2 + DOWN * 0.6

        self.play(FadeIn(tissue), FadeIn(tissue_lbl), run_time=0.6)
        self.play(FadeIn(p_target), FadeIn(lbl_target),
                  FadeIn(p_bare), FadeIn(lbl_bare), run_time=0.6)
        # Both arrive equally
        lbl_t_dest = arr_pos_t + UP * 0.35
        lbl_b_dest = arr_pos_b + DOWN * 0.35
        self.play(p_target.animate.move_to(arr_pos_t),
                  lbl_target.animate.move_to(lbl_t_dest),
                  p_bare.animate.move_to(arr_pos_b),
                  lbl_bare.animate.move_to(lbl_b_dest),
                  run_time=1.0)
        same_ann = SerifLabel("same arrival", TEAL, size=22)
        same_ann.move_to(tissue.get_left() + RIGHT * 1.2 + ORIGIN)
        self.play(FadeIn(same_ann, scale=0.9), run_time=0.5)

        # Cell receptor on the right side of tissue
        cell_pos = tissue.get_right() + LEFT * 0.6 + UP * 0.6
        cell_r = Circle(radius=0.38)
        cell_r.set_fill(SLATE, 0.85).set_stroke(SLATE, 2)
        cell_r.move_to(cell_pos)
        receptor = Dot(radius=0.12)
        receptor.set_fill(GOLD, 1).set_stroke(width=0, opacity=0)
        receptor.move_to(cell_pos + LEFT * 0.38)

        self.play(FadeIn(cell_r), FadeIn(receptor), run_time=0.5)

        # Targeted particle moves to dock the receptor (gold flash)
        dock_pos = cell_pos + LEFT * 0.6
        lbl_t_dock = cell_pos + UP * 0.55
        gold_flash = Circle(radius=0.28)
        gold_flash.set_fill(GOLD, 0.55).set_stroke(GOLD, 2.5)
        gold_flash.set_opacity(0)
        gold_flash.move_to(cell_pos + LEFT * 0.38)

        self.play(p_target.animate.move_to(dock_pos),
                  lbl_target.animate.move_to(lbl_t_dock),
                  run_time=0.7)
        gold_flash.set_opacity(1)
        self.play(gold_flash.animate.scale(1.22), run_time=0.4)
        self.play(gold_flash.animate.scale(0.01), run_time=0.3)

        # Untargeted stays in interstitium
        interst = SerifLabel("stays in interstitium", CRIMSON, size=20)
        interst.next_to(p_bare, DOWN, buff=0.2)
        self.play(FadeIn(interst, shift=UP * 0.1), run_time=0.5)

        ann = SerifLabel("same amount arrives, different cell entry", INK, size=22)
        ann.move_to(DOWN * 2.8)
        self.play(FadeIn(ann), run_time=0.6)
        self.wait(max(0.3, total - 5.7))


class B08_WrongFix(Scene):
    """Fixing step 4 when the bottleneck is steps 1–2."""
    def construct(self):
        total = DUR["B08"]
        steps_data = [
            ("BLOOD", TEAL),
            ("VESSEL WALL", TEAL),
            ("TUMOR TISSUE", TEAL),
            ("CELL SURFACE", CRIMSON),
        ]
        steps = [_step_rect(lbl, col) for lbl, col in steps_data]
        chain = VGroup(*steps).arrange(RIGHT, buff=0.55).move_to(UP * 0.6)
        arrows = VGroup()
        for i in range(len(steps) - 1):
            a = _arrow_right(
                steps[i].get_right() + RIGHT * 0.05,
                steps[i + 1].get_left() + LEFT * 0.05,
                color=INK
            )
            arrows.add(a)
        self.play(FadeIn(chain), FadeIn(arrows), run_time=0.8)

        # Crimson bracket on step 4: "you improved this"
        brace_fix = Brace(steps[-1], DOWN, color=CRIMSON)
        lbl_fix = SerifLabel("you improved this", CRIMSON, size=22)
        lbl_fix.next_to(brace_fix, DOWN, buff=0.18)
        self.play(FadeIn(brace_fix), FadeIn(lbl_fix), run_time=0.7)

        # Teal bracket on steps 1–2: "the actual bottleneck"
        brace_btl = Brace(VGroup(steps[0], steps[1]), UP, color=TEAL)
        lbl_btl = SerifLabel("the actual bottleneck", TEAL, size=22)
        lbl_btl.next_to(brace_btl, UP, buff=0.18)
        self.play(FadeIn(brace_btl), FadeIn(lbl_btl), run_time=0.7)

        # "wrong fix" annotation
        wrong = LabelChip("wrong fix", accent=CRIMSON, size=24)
        wrong.move_to(DOWN * 2.9)
        self.play(FadeIn(wrong, scale=0.9), run_time=0.5)
        self.wait(max(0.3, total - 2.7))


class B09_FolateExample(Scene):
    """Folate-targeted vs bare: equal accumulation, different internalization.
    All numbers are illustrative per the card's Example Seed."""
    def construct(self):
        total = DUR["B09"]
        # Layout: row labels on left (x~-3.5), bars centered at x~-0.6 and x~+2.0
        # Column headers
        h1 = LabelChip("TARGETED",   accent=TEAL,    size=22)
        h2 = LabelChip("UNTARGETED", accent=CRIMSON, size=22)
        h1.move_to(LEFT * 0.6 + UP * 2.9)
        h2.move_to(RIGHT * 2.2 + UP * 2.9)

        # Row label: tumor accumulation  (x=-3.5 stays well inside +-6.3)
        row_acc_lbl = SerifLabel("tumor accumulation", TEAL, size=20)
        row_acc_lbl.move_to(LEFT * 3.5 + UP * 1.4)

        # Accumulation bars (teal, near-equal heights)
        bar_acc1 = _bar(TEAL, 1.0,                  w=1.5, max_h=1.8)
        bar_acc2 = _bar(TEAL, 0.019 / 0.021,        w=1.5, max_h=1.8)
        bar_acc1.move_to(LEFT * 0.6 + UP * 0.7)
        bar_acc2.move_to(RIGHT * 2.2 + UP * 0.7)
        n_acc1 = Text("2.1%", font=MONO, color=TEAL, font_size=24, weight=BOLD)
        n_acc2 = Text("1.9%", font=MONO, color=TEAL, font_size=24, weight=BOLD)
        n_acc1.next_to(bar_acc1, UP, buff=0.1)
        n_acc2.next_to(bar_acc2, UP, buff=0.1)

        # Separator line
        sep = Line(LEFT * 5.8 + UP * 0.0, RIGHT * 5.8 + UP * 0.0,
                   color=INK, stroke_width=1.0)
        sep.set_opacity(0.28)

        # Row label: cell internalization
        row_int_lbl = SerifLabel("cell internalization", CRIMSON, size=20)
        row_int_lbl.move_to(LEFT * 3.5 + DOWN * 1.2)

        # Internalization bars (crimson, very different heights)
        bar_int1 = _bar(CRIMSON, 0.68, w=1.5, max_h=2.0)
        bar_int2 = _bar(CRIMSON, 0.12, w=1.5, max_h=2.0)
        # anchor bottom of bars at y=-2.2
        bar_int1.move_to(LEFT * 0.6 + DOWN * 2.2 + UP * bar_int1.height / 2)
        bar_int2.move_to(RIGHT * 2.2 + DOWN * 2.2 + UP * bar_int2.height / 2)
        n_int1 = Text("68%", font=MONO, color=CRIMSON, font_size=24, weight=BOLD)
        n_int2 = Text("12%", font=MONO, color=CRIMSON, font_size=24, weight=BOLD)
        n_int1.next_to(bar_int1, UP, buff=0.1)
        n_int2.next_to(bar_int2, UP, buff=0.1)

        # Illustrative note — place at bottom center, within safe area
        ilnote = SerifLabel("illustrative numbers", INK, size=18)
        ilnote.move_to(RIGHT * 3.8 + DOWN * 3.3)

        self.play(FadeIn(h1), FadeIn(h2), run_time=0.6)
        self.play(FadeIn(row_acc_lbl),
                  FadeIn(bar_acc1, shift=UP * 0.3),
                  FadeIn(bar_acc2, shift=UP * 0.3),
                  run_time=0.9)
        self.play(FadeIn(n_acc1), FadeIn(n_acc2), run_time=0.5)
        self.play(Create(sep), run_time=0.4)
        self.play(FadeIn(row_int_lbl),
                  FadeIn(bar_int1, shift=UP * 0.3),
                  FadeIn(bar_int2, shift=UP * 0.3),
                  run_time=0.9)
        self.play(FadeIn(n_int1), FadeIn(n_int2), run_time=0.5)
        self.play(FadeIn(ilnote, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 4.3))


class B10_End(Scene):
    """Endcard — uptake does not equal accumulation."""
    def construct(self):
        total = DUR["B10"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Uptake does not equal accumulation.", font=DISPLAY,
                  color=INK, font_size=30, weight=BOLD)
        t2 = Text("The ligand acts last. Fix the early steps.", font=DISPLAY,
                  color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(DOWN * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.2))
