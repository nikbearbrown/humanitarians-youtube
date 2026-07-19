"""vox_scenes.py — Why the Tumor Genome Is a Fossil Record of What the Cell Encountered
(vox-mutational-signature, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B06 (STILL geo: AdductChain) and B11 (STILL geo: FourSignatures) have no scene
class -- they compile as slates.

Color law: TEAL=#1F6F5C = preserved pattern / correct signature
           CRIMSON=#BF3339 = DNA damage / adduct / broken/misread base

Exclusions: no full chemical mechanism for all carcinogens (only B[a]P + UV);
no COSMIC database details; no enzyme kinetics; no aflatoxin-HBV interaction;
no linear no-threshold model for radiation.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import json
import os
import sys
import pathlib

# vox_graphics.py lives in books/vox/aspects/explainer/vox-explainer/manim/
# This file is at books/cancer-biology/youtube/vox-mutational-signature/
# parents[3] = books/
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 16)}

from vox_graphics import *  # noqa: E402,F401,F403

import numpy as np


# ─────────────────────────────────────────────────────────────────────────────
# B01 — Title card (COLD OPEN)
# ─────────────────────────────────────────────────────────────────────────────
class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Tumor Genome", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        t2 = Text("Is a Fossil Record", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─────────────────────────────────────────────────────────────────────────────
# B02 — Oncologist reads the report (COLD OPEN)
# ─────────────────────────────────────────────────────────────────────────────
class B02_OncologistReads(Scene):
    def construct(self):
        total = DUR["B02"]
        # Report panel background
        panel = Rectangle(width=9.0, height=3.8)
        panel.set_fill(WHITE, 0.85).set_stroke(INK, 1.5)
        panel.move_to(UP * 0.2)

        header = Text("SEQUENCING REPORT", font=DISPLAY, color=SLATE,
                      font_size=16, weight=BOLD)
        header.next_to(panel, UP, buff=-0.55).shift(LEFT * 2.8)

        count = Text("Total mutations: 340", font=MONO, color=INK, font_size=20)
        count.move_to(panel.get_center() + UP * 0.9 + LEFT * 2.0)

        pattern_label = Text("Dominant pattern:", font=MONO, color=INK, font_size=20)
        pattern_label.next_to(count, DOWN, buff=0.35).align_to(count, LEFT)

        # The mutation string — show G>T in crimson
        g_text = Text("G", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        arrow_text = Text("->T", font=MONO, color=INK, font_size=22)
        context_text = Text("  transversions at GpC contexts", font=MONO, color=INK, font_size=20)
        mut_line = VGroup(g_text, arrow_text, context_text).arrange(RIGHT, buff=0.05)
        mut_line.next_to(pattern_label, DOWN, buff=0.2).align_to(pattern_label, LEFT).shift(RIGHT * 0.3)

        sig_chip = LabelChip("Signature 4 — Tobacco", accent=CRIMSON, size=22)
        sig_chip.next_to(mut_line, DOWN, buff=0.45)

        self.play(FadeIn(panel), FadeIn(header), run_time=0.7)
        self.play(FadeIn(count, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(pattern_label), run_time=0.4)
        self.play(FadeIn(mut_line, shift=RIGHT * 0.2), run_time=0.6)
        self.play(FadeIn(sig_chip, scale=0.9), run_time=0.7)

        # Scan line moving down the report — the "reading" motion
        scan = Line(panel.get_left() + RIGHT * 0.15, panel.get_right() + LEFT * 0.15,
                    color=TEAL, stroke_width=2)
        scan.set_opacity(0.6)
        scan.move_to(panel.get_top() + DOWN * 0.3)
        self.play(FadeIn(scan), scan.animate.move_to(panel.get_bottom() + UP * 0.3),
                  run_time=1.5)
        self.play(FadeOut(scan), run_time=0.3)
        self.wait(max(0.3, total - 4.7))


# ─────────────────────────────────────────────────────────────────────────────
# B03 — THE QUESTION
# ─────────────────────────────────────────────────────────────────────────────
class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Each carcinogen leaves a distinctive", font=DISPLAY, color=INK, font_size=24)
        q2 = Text("mutation pattern", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        q3 = Text("that persists for decades.", font=DISPLAY, color=INK, font_size=24)
        q_block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.18).move_to(UP * 0.5)

        why = Text("Why?", font=DISPLAY, color=TEAL, font_size=42, weight=BOLD)
        sub = Text("How does a chemical write a permanent fingerprint into DNA?",
                   font=SERIF, color=INK, font_size=22, slant=ITALIC)
        why.next_to(q_block, DOWN, buff=0.55)
        sub.next_to(why, DOWN, buff=0.35)

        u = Line(q2.get_corner(DL) + DOWN * 0.1, q2.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)

        self.play(FadeIn(q1), FadeIn(q3), run_time=0.8)
        self.play(FadeIn(q2), Create(u), run_time=0.7)
        self.play(FadeIn(why, scale=0.85), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.7))


# ─────────────────────────────────────────────────────────────────────────────
# B04 — What mutations are (THE PROBLEM)
# ─────────────────────────────────────────────────────────────────────────────
class B04_WhatMutationsAre(Scene):
    def construct(self):
        total = DUR["B04"]
        # Show a simple DNA letter change: G -> T, inherited
        label = Text("A mutation is a heritable change in the DNA sequence",
                     font=DISPLAY, color=INK, font_size=22)
        label.move_to(UP * 2.8)

        # Two generations of cells: parent -> daughter -> granddaughter
        def _cell(label_text, x, y, color=TEAL):
            circ = Circle(radius=0.55).set_fill(color, 0.15).set_stroke(color, 2.5)
            circ.move_to(np.array([x, y, 0]))
            lbl = Text(label_text, font=MONO, color=color, font_size=18)
            lbl.move_to(circ.get_center())
            return VGroup(circ, lbl)

        parent = _cell("G->T", -3.5, 0.3, CRIMSON)
        daughter1 = _cell("G->T", 0.0, 1.2, CRIMSON)
        daughter2 = _cell("G->T", 0.0, -0.7, CRIMSON)
        grand1 = _cell("G->T", 3.5, 1.8, CRIMSON)
        grand2 = _cell("G->T", 3.5, 0.6, CRIMSON)
        grand3 = _cell("G->T", 3.5, -0.5, CRIMSON)
        grand4 = _cell("G->T", 3.5, -1.7, CRIMSON)

        # Arrows
        arr1 = Arrow(parent.get_right(), daughter1.get_left() + LEFT * 0.05,
                     buff=0.12, color=INK, stroke_width=2, tip_length=0.18)
        arr2 = Arrow(parent.get_right(), daughter2.get_left() + LEFT * 0.05,
                     buff=0.12, color=INK, stroke_width=2, tip_length=0.18)
        arr3 = Arrow(daughter1.get_right(), grand1.get_left() + LEFT * 0.05,
                     buff=0.12, color=INK, stroke_width=2, tip_length=0.18)
        arr4 = Arrow(daughter1.get_right(), grand2.get_left() + LEFT * 0.05,
                     buff=0.12, color=INK, stroke_width=2, tip_length=0.18)
        arr5 = Arrow(daughter2.get_right(), grand3.get_left() + LEFT * 0.05,
                     buff=0.12, color=INK, stroke_width=2, tip_length=0.18)
        arr6 = Arrow(daughter2.get_right(), grand4.get_left() + LEFT * 0.05,
                     buff=0.12, color=INK, stroke_width=2, tip_length=0.18)

        inherited_chip = LabelChip("every daughter cell inherits the same letter",
                                   accent=TEAL, size=18)
        inherited_chip.move_to(DOWN * 3.0)

        self.play(FadeIn(label), run_time=0.6)
        self.play(FadeIn(parent, scale=0.85), run_time=0.5)
        self.play(GrowArrow(arr1), GrowArrow(arr2), FadeIn(daughter1), FadeIn(daughter2),
                  run_time=0.9)
        self.play(GrowArrow(arr3), GrowArrow(arr4), GrowArrow(arr5), GrowArrow(arr6),
                  FadeIn(grand1), FadeIn(grand2), FadeIn(grand3), FadeIn(grand4),
                  run_time=1.0)
        self.play(FadeIn(inherited_chip, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.6))


# ─────────────────────────────────────────────────────────────────────────────
# B05 — Naive expectation (THE PROBLEM)
# ─────────────────────────────────────────────────────────────────────────────
class B05_NaiveExpectation(Scene):
    def construct(self):
        total = DUR["B05"]
        # A single dot (chemical) hitting a field of DNA letters
        top = Text("One chemical hit. One cell. One moment.",
                   font=DISPLAY, color=INK, font_size=22)
        top.move_to(UP * 2.9)

        # A teal background rectangle grows to represent the genome
        genome_bg = Rectangle(width=8.8, height=2.6)
        genome_bg.set_fill(TEAL, 0.06).set_stroke(TEAL, 1.2)
        genome_bg.move_to(DOWN * 0.2)

        # Grid of DNA letters — mostly normal
        letters = []
        cols, rows = 12, 4
        for r in range(rows):
            for c in range(cols):
                x = (c - cols / 2 + 0.5) * 0.72
                y = (rows / 2 - r - 0.5) * 0.56 - 0.3
                ltr = Text("G", font=MONO, color=TEAL, font_size=18)
                ltr.move_to(np.array([x, y, 0]))
                letters.append(ltr)

        grid = VGroup(*letters)

        # One crimson mutation in the middle
        mut_idx = rows // 2 * cols + cols // 2 - 1
        letters[mut_idx].set_color(CRIMSON)

        expect_label = Text("expect: one random mutation, lost in the noise",
                            font=SERIF, color=INK, font_size=20, slant=ITALIC)
        expect_label.move_to(DOWN * 2.9)

        self.play(FadeIn(top), run_time=0.5)
        # Grow the background rectangle — this is the real shape motion
        self.play(GrowFromCenter(genome_bg), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(l, scale=0.8) for l in grid],
                              lag_ratio=0.015), run_time=1.1)
        self.play(FadeIn(expect_label, shift=UP * 0.1), run_time=0.5)
        # Wiggle the one mutation to show it's "lost"
        self.play(letters[mut_idx].animate.scale(1.3), run_time=0.35)
        self.play(letters[mut_idx].animate.scale(1 / 1.3), run_time=0.3)
        self.wait(max(0.3, total - 3.45))


# ─────────────────────────────────────────────────────────────────────────────
# B06 — STILL (geo): AdductChain — NO SCENE CLASS
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# B07 — Adduct misread by polymerase (THE MECHANISM)
# ─────────────────────────────────────────────────────────────────────────────
class B07_AdductMisread(Scene):
    def construct(self):
        total = DUR["B07"]
        # Show: damaged G with adduct on one strand, polymerase inserts A opposite
        title = Text("BPDE adduct at guanine", font=DISPLAY, color=INK, font_size=20)
        title.move_to(UP * 3.1)

        # DNA ladder -- two strands, 4 rungs
        rung_y = [1.2, 0.4, -0.4, -1.2]
        strand_x = [-2.2, 2.2]

        # Left strand (template) -- G in crimson (damaged), rest teal
        lbases = ["C", "G", "A", "T"]
        lcolors = [TEAL, CRIMSON, TEAL, TEAL]
        lbase_mobs = []
        for i, (b, c) in enumerate(zip(lbases, lcolors)):
            t = Text(b, font=MONO, color=c, font_size=28)
            t.move_to(np.array([strand_x[0], rung_y[i], 0]))
            lbase_mobs.append(t)

        # Right strand (new) -- only show C, T, A (not the misread slot yet)
        rbases_init = ["G", "C", "T", "A"]
        rbase_mobs = []
        for i, b in enumerate(rbases_init):
            t = Text(b, font=MONO, color=TEAL, font_size=28)
            t.move_to(np.array([strand_x[1], rung_y[i], 0]))
            rbase_mobs.append(t)

        # Rungs (horizontal bars between bases)
        rungs = []
        for y in rung_y:
            r = Line(np.array([strand_x[0] + 0.25, y, 0]),
                     np.array([strand_x[1] - 0.25, y, 0]),
                     color=SLATE, stroke_width=2)
            rungs.append(r)

        # Adduct blob on the damaged G
        adduct = Circle(radius=0.25).set_fill(CRIMSON, 0.8).set_stroke(width=0, opacity=0)
        adduct.move_to(lbase_mobs[1].get_center() + LEFT * 0.6 + UP * 0.1)
        adduct_label = SerifLabel("BPDE adduct", CRIMSON, size=18)
        adduct_label.next_to(adduct, LEFT, buff=0.15)

        # Kinked rung at damaged G position -- replace the straight rung
        kink_rung = Line(np.array([strand_x[0] + 0.25, rung_y[1] + 0.15, 0]),
                         np.array([strand_x[1] - 0.25, rung_y[1] - 0.1, 0]),
                         color=CRIMSON, stroke_width=2)

        # Wrong insertion: A instead of C opposite damaged G
        wrong_A = Text("A", font=MONO, color=CRIMSON, font_size=28)
        wrong_A.move_to(rbase_mobs[1].get_center())

        poly_label = LabelChip("polymerase inserts A not C", accent=CRIMSON, size=18)
        poly_label.move_to(DOWN * 2.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(
            *[FadeIn(m) for m in lbase_mobs],
            *[FadeIn(r) for r in rungs],
            run_time=0.7)
        # Show adduct and kink
        rungs[1].set_color(CRIMSON)   # pre-color the rung before animation
        self.play(
            GrowFromCenter(adduct),
            FadeIn(adduct_label),
            rungs[1].animate.put_start_and_end_on(
                np.array([strand_x[0] + 0.25, rung_y[1] + 0.15, 0]),
                np.array([strand_x[1] - 0.25, rung_y[1] - 0.1, 0])),
            run_time=0.8)
        # Polymerase inserts wrong base: hide C, show A in crimson
        self.play(rbase_mobs[1].animate.set_opacity(0.0), run_time=0.3)
        self.play(FadeIn(wrong_A, scale=0.85),
                  *[FadeIn(m) for m in [rbase_mobs[0], rbase_mobs[2], rbase_mobs[3]]],
                  run_time=0.7)
        self.play(FadeIn(poly_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.6))


# ─────────────────────────────────────────────────────────────────────────────
# B08 — Mutation fixed after next replication (THE MECHANISM)
# ─────────────────────────────────────────────────────────────────────────────
class B08_MutationFixed(Scene):
    def construct(self):
        total = DUR["B08"]
        title = Text("After one more replication:", font=DISPLAY, color=INK, font_size=22)
        title.move_to(UP * 3.0)

        # Show: G:A mismatch -> replication -> one G:C (normal), one T:A (fixed mutation)
        left_label = SerifLabel("G:A mismatch", CRIMSON, size=24)
        left_label.move_to(LEFT * 3.8 + UP * 0.8)

        # Two daughter cells
        cell_left = Circle(radius=1.0).set_fill(TEAL, 0.1).set_stroke(TEAL, 2.5)
        cell_left.move_to(LEFT * 3.2 + DOWN * 0.5)
        cl_text = Text("G:C", font=MONO, color=TEAL, font_size=26, weight=BOLD)
        cl_text.move_to(cell_left.get_center())
        cl_chip = LabelChip("normal", accent=TEAL, size=18)
        cl_chip.next_to(cell_left, DOWN, buff=0.2)

        cell_right = Circle(radius=1.0).set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 2.5)
        cell_right.move_to(RIGHT * 3.2 + DOWN * 0.5)
        cr_text = Text("T:A", font=MONO, color=CRIMSON, font_size=26, weight=BOLD)
        cr_text.move_to(cell_right.get_center())
        cr_chip = LabelChip("fixed mutation", accent=CRIMSON, size=18)
        cr_chip.next_to(cell_right, DOWN, buff=0.2)

        # Arrows from top center (parent) to two daughters
        parent_dot = Dot(radius=0.12, color=INK).move_to(UP * 1.6)
        arr_l = Arrow(parent_dot.get_center(), cell_left.get_top() + UP * 0.05,
                      buff=0.12, color=INK, stroke_width=2, tip_length=0.18)
        arr_r = Arrow(parent_dot.get_center(), cell_right.get_top() + UP * 0.05,
                      buff=0.12, color=INK, stroke_width=2, tip_length=0.18)

        permanent = Text("permanent, heritable — copied into every daughter cell",
                         font=SERIF, color=INK, font_size=19, slant=ITALIC)
        permanent.move_to(DOWN * 2.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(parent_dot), FadeIn(left_label), run_time=0.5)
        self.play(GrowArrow(arr_l), GrowArrow(arr_r), run_time=0.7)
        self.play(FadeIn(cell_left), FadeIn(cl_text), FadeIn(cl_chip),
                  FadeIn(cell_right), FadeIn(cr_text), FadeIn(cr_chip), run_time=0.9)

        # Scan motion: a line sweeps across the two daughters left to right
        scan = Line(np.array([-5.5, -0.5, 0]), np.array([-5.5, -0.5, 0]),
                    color=GOLD, stroke_width=2)
        self.play(FadeIn(scan), run_time=0.2)
        self.play(scan.animate.put_start_and_end_on(
            np.array([-5.5, -0.5, 0]), np.array([5.5, -0.5, 0])), run_time=0.9)
        self.play(FadeOut(scan), FadeIn(permanent, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 4.3))


# ─────────────────────────────────────────────────────────────────────────────
# B09 — UV dimer contrast (THE MECHANISM)
# ─────────────────────────────────────────────────────────────────────────────
class B09_UVContrast(Scene):
    def construct(self):
        total = DUR["B09"]
        title = Text("UV: a different mechanism", font=DISPLAY, color=INK, font_size=22)
        title.move_to(UP * 3.1)

        # Adjacent pyrimidines: C-C on a strand
        cc_label = Text("adjacent pyrimidines: C  C", font=MONO, color=TEAL, font_size=24)
        cc_label.move_to(UP * 1.6)

        # UV photon arrow
        photon_arrow = Arrow(UP * 3.0 + LEFT * 1.5, cc_label.get_top() + UP * 0.1,
                             buff=0.08, color=GOLD, stroke_width=3, tip_length=0.22)
        photon_label = Text("UV-B photon", font=DISPLAY, color=INK, font_size=16)
        photon_label.next_to(photon_arrow, LEFT, buff=0.15)

        # Dimer — C-C fused
        dimer_box = Rectangle(width=2.2, height=0.7)
        dimer_box.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        dimer_box.move_to(UP * 0.2)
        dimer_label = Text("cyclobutane dimer", font=DISPLAY, color=CRIMSON, font_size=18)
        dimer_label.next_to(dimer_box, RIGHT, buff=0.3)
        cc_fused = Text("C=C", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        cc_fused.move_to(dimer_box.get_center())

        # Mutation arrow: dimer -> C->T transition
        mut_arrow = Arrow(dimer_box.get_bottom() + DOWN * 0.05,
                          np.array([0, -1.2, 0]),
                          buff=0.1, color=INK, stroke_width=2, tip_length=0.18)
        mut_text = Text("C -> T transition at dipyrimidine site",
                        font=MONO, color=CRIMSON, font_size=20)
        mut_text.move_to(DOWN * 1.8)
        cc_tt = Text("(CC -> TT: near-diagnostic for UV)", font=SERIF, color=INK,
                     font_size=18, slant=ITALIC)
        cc_tt.next_to(mut_text, DOWN, buff=0.25)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(cc_label), run_time=0.5)
        self.play(GrowArrow(photon_arrow), FadeIn(photon_label), run_time=0.7)
        self.play(
            FadeIn(dimer_box, scale=0.85),
            FadeIn(cc_fused),
            FadeIn(dimer_label),
            run_time=0.8)
        self.play(GrowArrow(mut_arrow), FadeIn(mut_text), run_time=0.7)
        self.play(FadeIn(cc_tt, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 3.7))


# ─────────────────────────────────────────────────────────────────────────────
# B10 — Pattern accumulates over decades (THE MECHANISM)
# ─────────────────────────────────────────────────────────────────────────────
class B10_PatternAccumulates(Scene):
    def construct(self):
        total = DUR["B10"]
        title = Text("Decades of exposure:", font=DISPLAY, color=INK, font_size=22)
        title.move_to(UP * 3.1)

        # Bar chart growing — showing the G->T signature accumulating
        # 8 bars representing mutation contexts; bar 3 (GpC) grows tallest
        bar_data = [0.05, 0.06, 0.85, 0.08, 0.04, 0.06, 0.05, 0.07]
        bar_colors = [TEAL, TEAL, CRIMSON, TEAL, TEAL, TEAL, TEAL, TEAL]
        bar_width = 0.55
        gap = 0.15
        bar_max_h = 3.2
        base_y = -1.5

        bars = []
        for i, (h_frac, c) in enumerate(zip(bar_data, bar_colors)):
            x = (i - len(bar_data) / 2 + 0.5) * (bar_width + gap)
            h = max(0.05, h_frac * bar_max_h)
            bar = Rectangle(width=bar_width, height=h)
            bar.set_fill(c, 0.9).set_stroke(width=0, opacity=0)
            bar.move_to(np.array([x, base_y + h / 2, 0]))
            bars.append(bar)

        # Axis line
        axis = Line(np.array([-3.5, base_y, 0]), np.array([3.5, base_y, 0]),
                    color=INK, stroke_width=2)

        x_label = SerifLabel("trinucleotide context", SLATE, size=20)
        x_label.next_to(axis, DOWN, buff=0.3)

        y_label = Text("mutation count", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        y_label.move_to(LEFT * 4.5 + UP * 0.5).rotate(PI / 2)

        sig_chip = LabelChip("G->T at GpC contexts", accent=CRIMSON, size=22)
        sig_chip.move_to(RIGHT * 1.5 + UP * 2.0)

        # Start bars at zero height, grow them
        start_bars = []
        for bar in bars:
            s = Rectangle(width=bar_width, height=0.05)
            s.set_fill(bar.get_color(), 0.9).set_stroke(width=0, opacity=0)
            s.move_to(bar.get_bottom() + UP * 0.025)
            start_bars.append(s)

        self.play(FadeIn(title), FadeIn(axis), FadeIn(x_label), run_time=0.6)
        for s in start_bars:
            self.add(s)
        self.play(FadeIn(y_label, shift=RIGHT * 0.1), run_time=0.4)
        self.play(
            *[Transform(s, b) for s, b in zip(start_bars, bars)],
            run_time=1.8)
        self.play(FadeIn(sig_chip, scale=0.85), run_time=0.6)
        self.wait(max(0.3, total - 3.4))


# ─────────────────────────────────────────────────────────────────────────────
# B11 — STILL (geo): FourSignatures — NO SCENE CLASS
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# B12 — Reading history from the genome (THE IMPLICATION)
# ─────────────────────────────────────────────────────────────────────────────
class B12_ReadingHistory(Scene):
    def construct(self):
        total = DUR["B12"]
        # Two columns: "genome says" vs "clinical file says"
        genome_header = LabelChip("what the genome says", accent=TEAL, size=22)
        clinical_header = LabelChip("what the file says", accent=SLATE, size=22)

        genome_header.move_to(LEFT * 3.2 + UP * 2.0)
        clinical_header.move_to(RIGHT * 3.2 + UP * 2.0)

        genome_content = Text("Tobacco signature\npresent",
                              font=MONO, color=TEAL, font_size=20)
        genome_content.move_to(LEFT * 3.2 + UP * 0.5)

        file_content = Text("Never-smoker\n(no tobacco history)",
                            font=MONO, color=INK, font_size=20)
        file_content.move_to(RIGHT * 3.2 + UP * 0.5)

        divider = Line(UP * 2.8, DOWN * 1.5, color=SLATE, stroke_width=1.5)
        divider.move_to(ORIGIN)

        # Implication: secondary smoke exposure
        impl = Text("implies: secondary smoke exposure", font=SERIF, color=CRIMSON,
                    font_size=20, slant=ITALIC)
        impl.move_to(DOWN * 1.8)

        witness = Text("The genome: a more reliable witness than memory.",
                       font=DISPLAY, color=INK, font_size=20)
        witness.move_to(DOWN * 2.8)

        self.play(FadeIn(divider), FadeIn(genome_header), FadeIn(clinical_header),
                  run_time=0.7)
        self.play(FadeIn(genome_content, shift=RIGHT * 0.2),
                  FadeIn(file_content, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(impl, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(witness, scale=0.92), run_time=0.6)
        self.wait(max(0.3, total - 2.6))


# ─────────────────────────────────────────────────────────────────────────────
# B13 — Example setup (THE EXAMPLE)
# ─────────────────────────────────────────────────────────────────────────────
class B13_ExampleSetup(Scene):
    def construct(self):
        total = DUR["B13"]
        eye = Text("ILLUSTRATIVE EXAMPLE", font=DISPLAY, color=SLATE, font_size=16)
        eye.move_to(UP * 3.2)

        heading = Text("Four tumor genomes.", font=DISPLAY, color=INK,
                       font_size=30, weight=BOLD)
        heading.move_to(UP * 1.8)

        sub = Text("Four patients. Four exposure histories.",
                   font=SERIF, color=INK, font_size=24, slant=ITALIC)
        sub.next_to(heading, DOWN, buff=0.4)

        prompt = Text("The pattern names the carcinogen.", font=DISPLAY,
                      color=TEAL, font_size=22)
        prompt.move_to(DOWN * 1.0)

        # Four placeholder boxes (will fill in next beat)
        box_y = -2.3
        boxes = []
        for i in range(4):
            x = (i - 1.5) * 2.8
            b = Rectangle(width=2.2, height=0.7)
            b.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
            b.move_to(np.array([x, box_y, 0]))
            boxes.append(b)

        self.play(FadeIn(eye), run_time=0.4)
        self.play(FadeIn(heading), FadeIn(sub), run_time=0.7)
        self.play(FadeIn(prompt, scale=0.9), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, scale=0.85) for b in boxes],
                              lag_ratio=0.15), run_time=0.9)
        self.wait(max(0.3, total - 2.5))


# ─────────────────────────────────────────────────────────────────────────────
# B14 — Four genomes revealed (THE EXAMPLE)
# ─────────────────────────────────────────────────────────────────────────────
class B14_ExampleFourGenomes(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("ILLUSTRATIVE", font=DISPLAY, color=SLATE, font_size=14)
        eye.move_to(UP * 3.2)

        # Four columns: tumor type, pattern, carcinogen
        cases = [
            ("Melanoma", "C->T at CC", "UV", GOLD),
            ("Lung\nadenoca.", "G->T at GpC", "Tobacco", CRIMSON),
            ("Liver\ntumor", "spike: codon 249", "Aflatoxin", CRIMSON),
            ("Colon\ncancer", "400 uniform", "MMR deficiency", TEAL),
        ]

        card_xs = [-5.0, -1.7, 1.7, 5.0]
        # Clamp to safe area — use 4.8 for outermost
        card_xs = [-4.8, -1.6, 1.6, 4.8]
        card_top = 2.2

        all_cards = []
        for i, ((tumor, pattern, carcinogen, color), x) in enumerate(zip(cases, card_xs)):
            card_bg = Rectangle(width=2.6, height=4.8)
            card_bg.set_fill(GROUND, 0).set_stroke(color, 2)
            card_bg.move_to(np.array([x, card_top - 2.4, 0]))

            tumor_text = Text(tumor, font=DISPLAY, color=INK, font_size=16, weight=BOLD)
            tumor_text.move_to(np.array([x, card_top - 0.5, 0]))

            pattern_text = Text(pattern, font=MONO, color=color, font_size=15)
            pattern_text.move_to(np.array([x, card_top - 1.5, 0]))

            carcinogen_chip = LabelChip(carcinogen, accent=color, size=14)
            carcinogen_chip.move_to(np.array([x, card_top - 2.6, 0]))

            all_cards.append(VGroup(card_bg, tumor_text, pattern_text, carcinogen_chip))

        # A scan line moving across all four cards
        scan = Line(np.array([-6.0, 0.0, 0]), np.array([-6.0, 0.0, 0]),
                    color=TEAL, stroke_width=1.5)
        scan.set_opacity(0.7)

        self.play(FadeIn(eye), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in all_cards],
                              lag_ratio=0.2), run_time=1.5)

        # Scan across
        self.play(FadeIn(scan), run_time=0.2)
        self.play(scan.animate.put_start_and_end_on(
            np.array([6.0, 3.0, 0]), np.array([6.0, -3.0, 0])),
            run_time=1.8)
        self.play(FadeOut(scan), run_time=0.3)

        four_hist = Text("Four patterns. Four histories.",
                         font=DISPLAY, color=INK, font_size=20)
        four_hist.move_to(DOWN * 3.1)
        self.play(FadeIn(four_hist, scale=0.9), run_time=0.6)
        self.wait(max(0.3, total - 4.7))


# ─────────────────────────────────────────────────────────────────────────────
# B15 — Recap / Endcard (RECAP)
# ─────────────────────────────────────────────────────────────────────────────
class B15_Recap(Scene):
    def construct(self):
        total = DUR["B15"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)

        t1 = Text("Each carcinogen: adducts at specific contexts.", font=DISPLAY,
                  color=INK, font_size=20)
        t2 = Text("Polymerase: context-specific misread.", font=DISPLAY,
                  color=INK, font_size=20)
        t3 = Text("Pattern fixed, heritable —", font=DISPLAY,
                  color=INK, font_size=20)
        t4 = Text("a chemical fingerprint in DNA.", font=DISPLAY,
                  color=CRIMSON, font_size=22, weight=BOLD)

        block = VGroup(t1, t2, t3, t4).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        u = Line(t4.get_corner(DL) + DOWN * 0.12, t4.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.6)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), FadeIn(t4), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.2))
