"""vox_scenes.py — Why a MicroRNA Deletion Can Do the Same Damage As Deleting a Tumor Suppressor
(vox-mir-deletion, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is the only STILL
(ai media slot) and has NO scene here. Durations read from beat_sheet.json
(actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-mir-deletion

Color law: TEAL #1F6F5C = miR-15/16 present / BCL2 silenced / apoptosis normal;
  CRIMSON #BF3339 = miR-15/16 deleted / BCL2 elevated / apoptosis blocked.
  GOLD = editor's-pen highlight fill only (never text). Two accents: TEAL + CRIMSON.
  SLATE = entity cards / structure.

Gate B convention: every zero-width stroke is also zero-opacity.
Exclusions: no Drosha/Dicer processing pathway, no oncomiR examples (miR-21),
  no lncRNA biology, no Polycomb/Trithorax, no microRNA therapeutics beyond
  one sentence on venetoclax.
"""
import sys, json, os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


# ---------------------------------------------------------------- helpers

def _solid_card(w=2.8, h=2.8, color=SLATE):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return r


def _bar(w, h, color, alpha=1.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


def _chip(text, accent=TEAL, size=22):
    return LabelChip(text, accent=accent, size=size)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """COLD OPEN — title card."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why a MicroRNA Deletion", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Can Cause Leukemia", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_TheQuestion(Scene):
    """THE QUESTION — gap formula on screen."""
    def construct(self):
        total = DUR["B03"]
        q1 = Text("A deletion should remove a tumor suppressor protein.", font=SERIF,
                  color=INK, font_size=34, slant=ITALIC)
        q2 = Text("This one removes only RNA molecules.", font=SERIF,
                  color=INK, font_size=34, slant=ITALIC)
        qblock = VGroup(q1, q2).arrange(DOWN, buff=0.18).move_to(UP * 0.7)
        dek = Text("Why does leukemia still follow?", font=DISPLAY, color=INK,
                   font_size=36, weight=BOLD)
        dek.next_to(qblock, DOWN, buff=0.5)
        gold_bar = Rectangle(width=dek.width + 0.4, height=dek.height + 0.18)
        gold_bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        gold_bar.move_to(dek)
        u = Line(dek.get_corner(DL) + DOWN * 0.12, dek.get_corner(DR) + DOWN * 0.12,
                 color=INK, stroke_width=2)
        self.play(FadeIn(qblock), run_time=1.0)
        self.play(FadeIn(gold_bar), FadeIn(dek), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 2.2))


class B04_NaiveModel(Scene):
    """THE PROBLEM — classical gene-to-protein-to-brake model."""
    def construct(self):
        total = DUR["B04"]
        # Two columns: normal (left, teal) and deleted (right, crimson)
        lx, rx = -3.0, 3.0

        # Left column: intact model
        l_gene = _chip("GENE", accent=TEAL, size=22)
        l_prot = _chip("PROTEIN", accent=TEAL, size=22)
        l_brake = _chip("BRAKE", accent=TEAL, size=22)
        l_col = VGroup(l_gene, l_prot, l_brake).arrange(DOWN, buff=0.55)
        l_col.move_to(LEFT * 3.0 + DOWN * 0.3)
        l_outcome = Text("apoptosis normal", font=SERIF, color=TEAL,
                         font_size=20, slant=ITALIC)
        l_outcome.next_to(l_col, DOWN, buff=0.28)

        l_arr1 = Arrow(l_gene.get_bottom(), l_prot.get_top(),
                       color=TEAL, stroke_width=3, buff=0.08)
        l_arr2 = Arrow(l_prot.get_bottom(), l_brake.get_top(),
                       color=TEAL, stroke_width=3, buff=0.08)

        # Right column: deleted
        r_gene = _chip("GENE DELETED", accent=CRIMSON, size=20)
        r_prot = Text("no protein", font=DISPLAY, color=CRIMSON, font_size=20)
        r_brake = Text("no brake", font=DISPLAY, color=CRIMSON, font_size=20)
        r_col = VGroup(r_gene, r_prot, r_brake).arrange(DOWN, buff=0.55)
        r_col.move_to(RIGHT * 3.0 + DOWN * 0.3)
        r_outcome = Text("apoptosis blocked", font=SERIF, color=CRIMSON,
                         font_size=20, slant=ITALIC)
        r_outcome.next_to(r_col, DOWN, buff=0.28)

        r_arr1 = Arrow(r_gene.get_bottom(), r_prot.get_top(),
                       color=CRIMSON, stroke_width=3, buff=0.08)
        r_arr2 = Arrow(r_prot.get_bottom(), r_brake.get_top(),
                       color=CRIMSON, stroke_width=3, buff=0.08)

        # Divider
        div = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=1.5)

        # Header labels
        hl = Text("INTACT", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        hr = Text("DELETED", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        hl.move_to(LEFT * 3.0 + UP * 2.2)
        hr.move_to(RIGHT * 3.0 + UP * 2.2)

        title = SerifLabel("the classical model", SLATE, size=24)
        title.to_edge(UP, buff=0.3)

        self.play(FadeIn(title), Create(div), run_time=0.8)
        self.play(FadeIn(hl), FadeIn(hr), run_time=0.6)
        self.play(FadeIn(l_col), FadeIn(r_col), run_time=0.8)
        self.play(GrowArrow(l_arr1), GrowArrow(l_arr2),
                  GrowArrow(r_arr1), GrowArrow(r_arr2), run_time=0.9)
        self.play(FadeIn(l_outcome), FadeIn(r_outcome), run_time=0.6)
        self.wait(max(0.5, total - 3.7))


class B05_WhatWasFound(Scene):
    """THE PROBLEM — chromosome deletion reveals only miR-15 and miR-16."""
    def construct(self):
        total = DUR["B05"]
        # Chromosome bar
        chr_bar = _bar(10.0, 0.8, SLATE, alpha=0.85)
        chr_bar.move_to(UP * 1.2)
        chr_label = Text("chromosome 13", font=DISPLAY, color=INK,
                         font_size=22, weight=BOLD)
        chr_label.next_to(chr_bar, UP, buff=0.18)

        # Deletion notch (crimson rectangle with white gap inside)
        notch = _bar(1.8, 0.85, CRIMSON, alpha=1.0)
        notch.move_to(UP * 1.2 + RIGHT * 0.5)

        notch_label = Text("13q14 deletion", font=DISPLAY, color=CRIMSON,
                           font_size=20, weight=BOLD)
        notch_label.next_to(notch, UP, buff=0.28)

        # What was found: two microRNA chips
        mir15 = _chip("miR-15", accent=CRIMSON, size=22)
        mir16 = _chip("miR-16", accent=CRIMSON, size=22)
        found_group = VGroup(mir15, mir16).arrange(RIGHT, buff=0.4)
        found_group.next_to(notch, DOWN, buff=0.5)

        found_label = SerifLabel("no protein-coding gene", CRIMSON, size=22)
        found_label.next_to(found_group, DOWN, buff=0.3)

        size_label = Text("22 nucleotides each", font="PT Mono", color=CRIMSON,
                          font_size=18)
        size_label.next_to(found_label, DOWN, buff=0.2)

        # Arrow from deletion to found
        arr = Arrow(notch.get_bottom(), found_group.get_top(),
                    color=CRIMSON, stroke_width=3, buff=0.12)

        title = SerifLabel("what the deletion removed", SLATE, size=24)
        title.to_edge(UP, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromEdge(chr_bar, LEFT), FadeIn(chr_label), run_time=0.9)
        self.play(FadeIn(notch), FadeIn(notch_label), run_time=0.7)
        self.play(GrowArrow(arr), run_time=0.6)
        self.play(FadeIn(found_group), run_time=0.7)
        self.play(FadeIn(found_label), FadeIn(size_label), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B06_MicroRNAMechanism(Scene):
    """THE MECHANISM — RISC complex, partial complementarity, fan of targets."""
    def construct(self):
        total = DUR["B06"]
        # Center: miR-15/16 chip inside RISC oval
        risc_oval = Ellipse(width=3.2, height=1.6)
        risc_oval.set_fill(SLATE, 0.18).set_stroke(SLATE, 2.5)
        risc_oval.move_to(LEFT * 1.5 + UP * 0.2)

        risc_lbl = Text("RISC", font=DISPLAY, color=SLATE,
                        font_size=18, weight=BOLD)
        risc_lbl.move_to(risc_oval.get_left() + RIGHT * 0.55)

        mir_chip = _chip("miR-15/16", accent=TEAL, size=20)
        mir_chip.move_to(risc_oval.get_center() + RIGHT * 0.3)

        # Three target mRNA chips to the right
        targets = ["BCL2 mRNA", "target 2", "target 3"]
        t_chips = [_chip(t, accent=TEAL, size=18) for t in targets]
        t_y_positions = [UP * 1.3, ORIGIN, DOWN * 1.3]
        for tc, ty in zip(t_chips, t_y_positions):
            tc.move_to(RIGHT * 3.8 + ty)

        # Fan arrows from risc_oval right edge to each target
        arrows = VGroup()
        src_pt = risc_oval.get_right()
        for tc in t_chips:
            arr = Arrow(src_pt, tc.get_left(),
                        color=TEAL, stroke_width=2.5, buff=0.12)
            arrows.add(arr)

        # "partial complementarity" label
        pc_label = SerifLabel("partial complementarity", TEAL, size=22)
        pc_label.move_to(DOWN * 2.6)

        # "silences many targets" label
        sm_label = SerifLabel("silences many targets simultaneously", TEAL, size=20)
        sm_label.move_to(DOWN * 3.2)

        title = SerifLabel("microRNA silencing: one miRNA, many targets", SLATE, size=24)
        title.to_edge(UP, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(risc_oval), FadeIn(risc_lbl), run_time=0.8)
        self.play(FadeIn(mir_chip, scale=0.9), run_time=0.6)
        self.play(
            AnimationGroup(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.25
            ),
            run_time=1.0
        )
        self.play(
            AnimationGroup(
                *[FadeIn(tc, scale=0.9) for tc in t_chips],
                lag_ratio=0.2
            ),
            run_time=0.8
        )
        self.play(FadeIn(pc_label, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(sm_label, shift=UP * 0.06), run_time=0.5)
        self.wait(max(0.5, total - 4.8))


class B07_NormalState(Scene):
    """THE MECHANISM — normal B cell: miR-15/16 suppress BCL2, apoptosis normal."""
    def construct(self):
        total = DUR["B07"]
        # Banner
        banner = _bar(12.0, 0.7, TEAL, alpha=0.15)
        banner.to_edge(UP, buff=0.0)
        banner_text = Text("miR-15/16 PRESENT", font=DISPLAY, color=TEAL,
                           font_size=22, weight=BOLD)
        banner_text.move_to(banner)

        # Row 1: miR chip -> suppression -> BCL2 mRNA chip
        mir_chip = _chip("miR-15/16", accent=TEAL, size=22)
        mir_chip.move_to(LEFT * 3.8 + UP * 0.9)

        sup_bar = _bar(1.6, 0.45, TEAL, alpha=0.7)
        sup_bar.move_to(ORIGIN + UP * 0.9)
        sup_lbl = Text("suppresses", font=SERIF, color=INK,
                       font_size=16, slant=ITALIC)
        sup_lbl.move_to(sup_bar)

        bcl2_mrna = _chip("BCL2 mRNA", accent=SLATE, size=20)
        bcl2_mrna.move_to(RIGHT * 3.6 + UP * 0.9)

        arr_sup = Arrow(mir_chip.get_right(), sup_bar.get_left(),
                        color=TEAL, stroke_width=3, buff=0.1)
        arr_mrna = Arrow(sup_bar.get_right(), bcl2_mrna.get_left(),
                         color=SLATE, stroke_width=3, buff=0.1)

        # Row 2: BCL2 protein bar (short = low)
        prot_label = SerifLabel("BCL2 protein", TEAL, size=22)
        prot_label.move_to(LEFT * 3.8 + DOWN * 0.5)

        bcl2_bar_low = _bar(0.9, 1.2, TEAL, alpha=0.85)
        bcl2_bar_low.move_to(LEFT * 0.5 + DOWN * 0.3)
        low_lbl = Text("LOW", font=DISPLAY, color=TEAL, font_size=18, weight=BOLD)
        low_lbl.next_to(bcl2_bar_low, UP, buff=0.12)

        # Row 3: outcome
        outcome = _chip("APOPTOSIS NORMAL", accent=TEAL, size=22)
        outcome.move_to(DOWN * 2.0)

        arr_out = Arrow(bcl2_bar_low.get_bottom(), outcome.get_top(),
                        color=TEAL, stroke_width=3, buff=0.12)

        self.play(FadeIn(banner), FadeIn(banner_text), run_time=0.6)
        self.play(FadeIn(mir_chip), FadeIn(sup_bar), FadeIn(sup_lbl),
                  FadeIn(bcl2_mrna), run_time=0.8)
        self.play(GrowArrow(arr_sup), GrowArrow(arr_mrna), run_time=0.7)
        self.play(FadeIn(prot_label), GrowFromEdge(bcl2_bar_low, DOWN), run_time=0.7)
        self.play(FadeIn(low_lbl), run_time=0.4)
        self.play(GrowArrow(arr_out), FadeIn(outcome), run_time=0.7)
        self.wait(max(0.5, total - 3.9))


class B08_DeletedState(Scene):
    """THE MECHANISM — CLL: miR-15/16 deleted, BCL2 rises, apoptosis blocked."""
    def construct(self):
        total = DUR["B08"]
        # Banner
        banner = _bar(12.0, 0.7, CRIMSON, alpha=0.15)
        banner.to_edge(UP, buff=0.0)
        banner_text = Text("miR-15/16 DELETED", font=DISPLAY, color=CRIMSON,
                           font_size=22, weight=BOLD)
        banner_text.move_to(banner)

        # Row 1: empty RISC -> BCL2 mRNA unrestrained
        risc_oval = Ellipse(width=2.4, height=1.0)
        risc_oval.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.8)
        risc_oval.set_stroke(opacity=0.5)
        risc_oval.move_to(LEFT * 3.8 + UP * 0.9)

        empty_lbl = Text("RISC empty", font=DISPLAY, color=CRIMSON,
                         font_size=16, weight=BOLD)
        empty_lbl.move_to(risc_oval)

        bcl2_mrna = _chip("BCL2 mRNA", accent=CRIMSON, size=20)
        bcl2_mrna.move_to(RIGHT * 3.2 + UP * 0.9)

        unrest_lbl = SerifLabel("unrestrained", CRIMSON, size=20)
        unrest_lbl.move_to(ORIGIN + UP * 0.9)

        arr_unrest = Arrow(risc_oval.get_right(), bcl2_mrna.get_left(),
                           color=CRIMSON, stroke_width=3, buff=0.12)

        # Row 2: BCL2 protein bar (tall = high)
        prot_label = SerifLabel("BCL2 protein", CRIMSON, size=22)
        prot_label.move_to(LEFT * 3.8 + DOWN * 0.5)

        bcl2_bar_high = _bar(0.9, 2.4, CRIMSON, alpha=0.85)
        bcl2_bar_high.move_to(LEFT * 0.5 + DOWN * 0.6)
        high_lbl = Text("HIGH", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        high_lbl.next_to(bcl2_bar_high, UP, buff=0.12)

        # Row 3: outcome
        outcome = _chip("APOPTOSIS BLOCKED", accent=CRIMSON, size=22)
        outcome.move_to(DOWN * 2.5)

        arr_out = Arrow(bcl2_bar_high.get_bottom(), outcome.get_top(),
                        color=CRIMSON, stroke_width=3, buff=0.12)

        self.play(FadeIn(banner), FadeIn(banner_text), run_time=0.6)
        self.play(Create(risc_oval), FadeIn(empty_lbl), run_time=0.7)
        self.play(FadeIn(bcl2_mrna), FadeIn(unrest_lbl),
                  GrowArrow(arr_unrest), run_time=0.8)
        self.play(FadeIn(prot_label), GrowFromEdge(bcl2_bar_high, DOWN), run_time=0.8)
        self.play(FadeIn(high_lbl), run_time=0.4)
        self.play(GrowArrow(arr_out), FadeIn(outcome), run_time=0.7)
        self.wait(max(0.5, total - 4.0))


class B09_TwoLaneCompare(Scene):
    """THE MECHANISM — full two-lane comparison (the visual object)."""
    def construct(self):
        total = DUR["B09"]
        lx, rx = -3.2, 3.2

        # --- LEFT LANE (TEAL) ---
        l_banner = _bar(5.8, 0.65, TEAL, alpha=0.2)
        l_banner.move_to(LEFT * 3.2 + UP * 3.1)
        l_btxt = Text("miR-15/16 PRESENT", font=DISPLAY, color=TEAL,
                      font_size=18, weight=BOLD)
        l_btxt.move_to(l_banner)

        # miRNA loaded chip
        l_mir = _chip("miR-15/16 loaded", accent=TEAL, size=17)
        l_mir.move_to(LEFT * 3.2 + UP * 2.0)

        # BCL2 mRNA suppressed
        l_mrna = Text("BCL2 mRNA suppressed", font=SERIF, color=TEAL,
                      font_size=17, slant=ITALIC)
        l_mrna.move_to(LEFT * 3.2 + UP * 0.9)

        # BCL2 bar (low)
        l_bcl2_bar = _bar(0.7, 0.85, TEAL, alpha=0.85)
        l_bcl2_bar.move_to(LEFT * 3.2 + DOWN * 0.3)
        l_bcl2_lbl = Text("BCL2 low", font="PT Mono", color=TEAL, font_size=15)
        l_bcl2_lbl.next_to(l_bcl2_bar, RIGHT, buff=0.2)

        # Outcome
        l_out = _chip("APOPTOSIS NORMAL", accent=TEAL, size=17)
        l_out.move_to(LEFT * 3.2 + DOWN * 1.6)

        l_arrows = VGroup(
            Arrow(l_mir.get_bottom(), l_mrna.get_top(), color=TEAL, stroke_width=2, buff=0.08),
            Arrow(l_mrna.get_bottom(), l_bcl2_bar.get_top(), color=TEAL, stroke_width=2, buff=0.08),
            Arrow(l_bcl2_bar.get_bottom(), l_out.get_top(), color=TEAL, stroke_width=2, buff=0.08),
        )

        # --- RIGHT LANE (CRIMSON) ---
        r_banner = _bar(5.8, 0.65, CRIMSON, alpha=0.2)
        r_banner.move_to(RIGHT * 3.2 + UP * 3.1)
        r_btxt = Text("miR-15/16 DELETED", font=DISPLAY, color=CRIMSON,
                      font_size=18, weight=BOLD)
        r_btxt.move_to(r_banner)

        # RISC empty
        r_mir = Text("RISC empty", font=SERIF, color=CRIMSON,
                     font_size=17, slant=ITALIC)
        r_mir.move_to(RIGHT * 3.2 + UP * 2.0)

        # BCL2 mRNA unrestrained
        r_mrna = Text("BCL2 mRNA unrestrained", font=SERIF, color=CRIMSON,
                      font_size=17, slant=ITALIC)
        r_mrna.move_to(RIGHT * 3.2 + UP * 0.9)

        # BCL2 bar (high)
        r_bcl2_bar = _bar(0.7, 2.1, CRIMSON, alpha=0.85)
        r_bcl2_bar.move_to(RIGHT * 3.2 + DOWN * 0.75)
        r_bcl2_lbl = Text("BCL2 high", font="PT Mono", color=CRIMSON, font_size=15)
        r_bcl2_lbl.next_to(r_bcl2_bar, RIGHT, buff=0.2)

        # Outcome
        r_out = _chip("APOPTOSIS BLOCKED", accent=CRIMSON, size=17)
        r_out.move_to(RIGHT * 3.2 + DOWN * 2.2)

        r_arrows = VGroup(
            Arrow(r_mir.get_bottom(), r_mrna.get_top(), color=CRIMSON, stroke_width=2, buff=0.08),
            Arrow(r_mrna.get_bottom(), r_bcl2_bar.get_top(), color=CRIMSON, stroke_width=2, buff=0.08),
            Arrow(r_bcl2_bar.get_bottom(), r_out.get_top(), color=CRIMSON, stroke_width=2, buff=0.08),
        )

        # Divider
        div = Line(UP * 3.6, DOWN * 2.8, color=INK, stroke_width=1.5)

        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(l_banner), FadeIn(l_btxt), FadeIn(r_banner), FadeIn(r_btxt), run_time=0.7)
        self.play(FadeIn(l_mir), FadeIn(r_mir), run_time=0.6)
        self.play(GrowArrow(l_arrows[0]), GrowArrow(r_arrows[0]), run_time=0.6)
        self.play(FadeIn(l_mrna), FadeIn(r_mrna), run_time=0.6)
        self.play(GrowArrow(l_arrows[1]), GrowArrow(r_arrows[1]), run_time=0.6)
        self.play(
            GrowFromEdge(l_bcl2_bar, DOWN), FadeIn(l_bcl2_lbl),
            GrowFromEdge(r_bcl2_bar, DOWN), FadeIn(r_bcl2_lbl),
            run_time=0.8
        )
        self.play(GrowArrow(l_arrows[2]), GrowArrow(r_arrows[2]), run_time=0.6)
        self.play(FadeIn(l_out), FadeIn(r_out), run_time=0.6)
        self.wait(max(0.5, total - 5.0))


class B10_NonCodingTumorSuppressor(Scene):
    """THE IMPLICATION — section card: non-coding sequence as tumor suppressor."""
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Non-coding sequence", font=DISPLAY, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("can act as a tumor suppressor.", font=SERIF, color=INK,
                  font_size=38, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.28).move_to(UP * 0.3)
        sub = Text("the brake made of RNA works as reliably as the brake made of protein",
                   font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.45)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=2.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.08), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


class B11_VenetoclaxLink(Scene):
    """THE IMPLICATION — venetoclax targets BCL2 that miRNA loss released."""
    def construct(self):
        total = DUR["B11"]
        # Vertical causal chain: deletion -> BCL2 elevated -> CLL
        del_chip = _chip("miR-15/16 DELETED", accent=CRIMSON, size=20)
        del_chip.move_to(UP * 2.2 + LEFT * 1.5)

        bcl2_chip = _chip("BCL2 ELEVATED", accent=CRIMSON, size=20)
        bcl2_chip.move_to(UP * 0.5 + LEFT * 1.5)

        cll_chip = _chip("CLL", accent=CRIMSON, size=20)
        cll_chip.move_to(DOWN * 1.2 + LEFT * 1.5)

        arr1 = Arrow(del_chip.get_bottom(), bcl2_chip.get_top(),
                     color=CRIMSON, stroke_width=3, buff=0.1)
        arr2 = Arrow(bcl2_chip.get_bottom(), cll_chip.get_top(),
                     color=CRIMSON, stroke_width=3, buff=0.1)

        # Venetoclax branch from BCL2 node (right)
        ven_chip = _chip("VENETOCLAX", accent=TEAL, size=20)
        ven_chip.move_to(RIGHT * 3.2 + UP * 0.5)

        block_arr = Arrow(ven_chip.get_left(), bcl2_chip.get_right(),
                          color=TEAL, stroke_width=4, buff=0.1)

        direct_lbl = SerifLabel("direct target", TEAL, size=22)
        direct_lbl.next_to(ven_chip, DOWN, buff=0.28)

        title = SerifLabel("venetoclax: the RNA deletion revealed the drug target", SLATE, size=22)
        title.to_edge(UP, buff=0.4)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(del_chip), run_time=0.6)
        self.play(GrowArrow(arr1), FadeIn(bcl2_chip), run_time=0.7)
        self.play(GrowArrow(arr2), FadeIn(cll_chip), run_time=0.6)
        self.play(FadeIn(ven_chip), GrowArrow(block_arr), run_time=0.8)
        self.play(FadeIn(direct_lbl), run_time=0.5)
        self.wait(max(0.5, total - 3.7))


class B12_ExampleNormal(Scene):
    """THE EXAMPLE — illustrative: 100 normal B cells, BCL2=1, BAX wins."""
    def construct(self):
        total = DUR["B12"]
        title = SerifLabel("100 normal B cells — miR-15/16 active", TEAL, size=24)
        title.to_edge(UP, buff=0.4)

        # Row 1: miRNA chip -> RISC -> BCL2 mRNA suppressed
        mir_chip = _chip("miR-15/16", accent=TEAL, size=20)
        mir_chip.move_to(LEFT * 4.5 + UP * 1.4)

        risc_chip = _chip("RISC", accent=SLATE, size=20)
        risc_chip.move_to(LEFT * 1.8 + UP * 1.4)

        mrna_chip = _chip("BCL2 mRNA suppressed", accent=TEAL, size=18)
        mrna_chip.move_to(RIGHT * 2.0 + UP * 1.4)

        arr_r1a = Arrow(mir_chip.get_right(), risc_chip.get_left(),
                        color=TEAL, stroke_width=2.5, buff=0.1)
        arr_r1b = Arrow(risc_chip.get_right(), mrna_chip.get_left(),
                        color=TEAL, stroke_width=2.5, buff=0.1)

        # Row 2: BCL2 bar + BAX comparison
        bcl2_lbl = Text("BCL2 = 1 unit", font="PT Mono", color=TEAL, font_size=20)
        bcl2_lbl.move_to(LEFT * 3.8 + DOWN * 0.1)

        bax_chip = _chip("BAX WINS", accent=TEAL, size=20)
        bax_chip.move_to(ORIGIN + DOWN * 0.1)

        momp_chip = _chip("MOMP", accent=SLATE, size=20)
        momp_chip.move_to(RIGHT * 2.8 + DOWN * 0.1)

        die_chip = _chip("CELL DIES", accent=TEAL, size=20)
        die_chip.move_to(RIGHT * 5.2 + DOWN * 0.1)

        arr_r2a = Arrow(bcl2_lbl.get_right(), bax_chip.get_left(),
                        color=TEAL, stroke_width=2.5, buff=0.1)
        arr_r2b = Arrow(bax_chip.get_right(), momp_chip.get_left(),
                        color=TEAL, stroke_width=2.5, buff=0.1)
        arr_r2c = Arrow(momp_chip.get_right(), die_chip.get_left(),
                        color=TEAL, stroke_width=2.5, buff=0.1)

        illus = Text("ILLUSTRATIVE", font="PT Mono", color=SLATE, font_size=15)
        illus.move_to(DOWN * 3.2 + RIGHT * 4.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(mir_chip), FadeIn(risc_chip), FadeIn(mrna_chip), run_time=0.7)
        self.play(GrowArrow(arr_r1a), GrowArrow(arr_r1b), run_time=0.7)
        self.play(FadeIn(bcl2_lbl), FadeIn(bax_chip), run_time=0.6)
        self.play(GrowArrow(arr_r2a), run_time=0.5)
        self.play(FadeIn(momp_chip), GrowArrow(arr_r2b), run_time=0.6)
        self.play(FadeIn(die_chip), GrowArrow(arr_r2c), run_time=0.6)
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.5, total - 4.6))


class B13_ExampleCLL(Scene):
    """THE EXAMPLE — illustrative: CLL B cells, BCL2=4 units, BAX fails."""
    def construct(self):
        total = DUR["B13"]
        title = SerifLabel("CLL B cells -- miR-15/16 deleted", CRIMSON, size=24)
        title.to_edge(UP, buff=0.4)

        # Row 1: deletion -> RISC empty -> BCL2 mRNA unrestrained
        del_chip = _chip("miR-15/16 DELETED", accent=CRIMSON, size=18)
        del_chip.move_to(LEFT * 4.5 + UP * 1.4)

        risc_empty = Text("RISC empty", font=DISPLAY, color=CRIMSON,
                          font_size=18, weight=BOLD)
        risc_empty.move_to(LEFT * 1.6 + UP * 1.4)

        mrna_chip = _chip("BCL2 mRNA unrestrained", accent=CRIMSON, size=17)
        mrna_chip.move_to(RIGHT * 2.2 + UP * 1.4)

        arr_r1a = Arrow(del_chip.get_right(), risc_empty.get_left(),
                        color=CRIMSON, stroke_width=2.5, buff=0.1)
        arr_r1b = Arrow(risc_empty.get_right(), mrna_chip.get_left(),
                        color=CRIMSON, stroke_width=2.5, buff=0.1)

        # Row 2: BCL2 bar + BAX fails
        bcl2_lbl = Text("BCL2 = 4 units", font="PT Mono", color=CRIMSON, font_size=20)
        bcl2_lbl.move_to(LEFT * 3.8 + DOWN * 0.1)

        bax_chip = _chip("BAX LOSES", accent=CRIMSON, size=20)
        bax_chip.move_to(ORIGIN + DOWN * 0.1)

        nomopm_chip = _chip("NO MOMP", accent=CRIMSON, size=20)
        nomopm_chip.move_to(RIGHT * 2.8 + DOWN * 0.1)

        accum_chip = _chip("CELLS ACCUMULATE", accent=CRIMSON, size=18)
        accum_chip.move_to(RIGHT * 5.4 + DOWN * 0.1)

        arr_r2a = Arrow(bcl2_lbl.get_right(), bax_chip.get_left(),
                        color=CRIMSON, stroke_width=2.5, buff=0.1)
        arr_r2b = Arrow(bax_chip.get_right(), nomopm_chip.get_left(),
                        color=CRIMSON, stroke_width=2.5, buff=0.1)
        arr_r2c = Arrow(nomopm_chip.get_right(), accum_chip.get_left(),
                        color=CRIMSON, stroke_width=2.5, buff=0.1)

        illus = Text("ILLUSTRATIVE", font="PT Mono", color=SLATE, font_size=15)
        illus.move_to(DOWN * 3.2 + RIGHT * 4.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(del_chip), FadeIn(risc_empty), FadeIn(mrna_chip), run_time=0.7)
        self.play(GrowArrow(arr_r1a), GrowArrow(arr_r1b), run_time=0.7)
        self.play(FadeIn(bcl2_lbl), FadeIn(bax_chip), run_time=0.6)
        self.play(GrowArrow(arr_r2a), run_time=0.5)
        self.play(FadeIn(nomopm_chip), GrowArrow(arr_r2b), run_time=0.6)
        self.play(FadeIn(accum_chip), GrowArrow(arr_r2c), run_time=0.6)
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.5, total - 4.6))


class B14_Recap(Scene):
    """RECAP — endcard: question answered in one line."""
    def construct(self):
        total = DUR["B14"]
        t1 = Text("Deleting non-protein-coding sequence", font=SERIF, color=INK,
                  font_size=32, slant=ITALIC)
        t2 = Text("caused leukemia by releasing BCL2 from its RNA brake.", font=SERIF,
                  color=INK, font_size=32, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.5)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=2.5)
        kicker = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=22, weight=BOLD)
        kicker.next_to(block, DOWN, buff=0.55)
        self.play(FadeIn(block), run_time=1.0)
        self.play(Create(u), run_time=0.7)
        self.play(FadeIn(kicker, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
