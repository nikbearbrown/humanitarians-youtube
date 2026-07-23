"""vox_scenes.py — Why a Cancer With Intact Tumor Suppressor Genes Still
Behaves As If They Are Missing (vox-protein-level-loss, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this
reel's beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-protein-level-loss

Color law: TEAL #1F6F5C = intact/present/functional (genes, sequencing result);
CRIMSON #BF3339 = lost/absent/broken (protein degraded, absent). GOLD = single
editor's-pen fill in B12 only, never as text. Two accents max; never swapped.

Exclusions honored: NO HPV life cycle, NO vaccine, NO CIN staging, NO HPV
type taxonomy, NO insertional mutagenesis, NO HBV/HCV.

Gate B convention: every zero-width stroke is also zero-opacity, or the
layout audit strikes it.
"""
import sys
import json
import pathlib
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene

# ---------------------------------------------------------------- durations

DUR = {
    "B01": 11.0, "B03": 10.0, "B04": 12.0, "B05": 10.0, "B06": 10.0,
    "B07": 11.0, "B08": 13.0, "B09": 12.0, "B10": 11.0, "B11": 13.0,
    "B12": 11.0, "B13": 12.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS.get("beats", [])})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _gene_box(label, color=TEAL, width=2.8, height=0.9):
    """A flat rectangular box representing a gene locus."""
    box = Rectangle(width=width, height=height)
    box.set_fill(color, 0.15).set_stroke(color, 2.5)
    chip = LabelChip(label, accent=color, size=22)
    chip.move_to(box)
    return VGroup(box, chip)


def _protein_circle(label, color=TEAL, radius=0.38):
    """A circle representing a protein molecule."""
    circ = Circle(radius=radius)
    circ.set_fill(color, 0.2).set_stroke(color, 2.5)
    txt = Text(label, font=SERIF, color=color, font_size=20)
    if txt.width > radius * 1.5:
        txt.scale_to_fit_width(radius * 1.5)
    txt.move_to(circ)
    return VGroup(circ, txt)


def _x_mark(center, color=CRIMSON, size=0.22):
    """A bold X drawn as two lines — marks something absent/destroyed."""
    diag1 = Line(center + UP * size + LEFT * size,
                 center + DOWN * size + RIGHT * size,
                 color=color, stroke_width=5)
    diag2 = Line(center + UP * size + RIGHT * size,
                 center + DOWN * size + LEFT * size,
                 color=color, stroke_width=5)
    return VGroup(diag1, diag2)


def _viral_protein_node(label, color=CRIMSON, radius=0.3):
    """A diamond-shaped node for a viral protein (E6 or E7)."""
    d = Polygon(UP * radius, RIGHT * radius * 1.3, DOWN * radius,
                LEFT * radius * 1.3)
    d.set_fill(color, 0.9).set_stroke(color, 0)
    txt = Text(label, font=DISPLAY, color=WHITE, font_size=20, weight="MEDIUM")
    if txt.width > radius * 2.2:
        txt.scale_to_fit_width(radius * 2.2)
    txt.move_to(d)
    return VGroup(d, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """Title card: CANCER BIOLOGY eyebrow, TEAL, INK fill for text."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=26, weight="MEDIUM")
        t1 = Text("Intact genes,", font=SERIF, color=INK,
                  font_size=52, weight=BOLD)
        t2 = Text("absent proteins.", font=SERIF, color=INK,
                  font_size=52, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        sub = Text("the gap between DNA and protein",
                   font=SERIF, color=INK, font_size=28)
        sub.next_to(block, DOWN, buff=0.5)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B03_DiscordanceSummary(Scene):
    """Two-row table: gene (TEAL INTACT) vs protein (CRIMSON ABSENT).
    The core discordance revealed before the explanation."""
    def construct(self):
        total = DUR["B03"]
        # column headers
        h_gene = SerifLabel("gene", TEAL, size=28).move_to(LEFT * 2.8 + UP * 2.2)
        h_prot = SerifLabel("protein", CRIMSON, size=28).move_to(RIGHT * 2.4 + UP * 2.2)
        header_rule = Line(LEFT * 5.5 + UP * 1.85, RIGHT * 5.5 + UP * 1.85,
                           color=INK, stroke_width=1.2)

        # row 1: TP53 / p53
        row1_gene = LabelChip("TP53 gene", accent=TEAL, size=24).move_to(LEFT * 2.8 + UP * 0.9)
        row1_arr = Arrow(LEFT * 1.2 + UP * 0.9, RIGHT * 0.8 + UP * 0.9,
                         color=INK, stroke_width=2, buff=0.05)
        row1_prot = LabelChip("p53 protein  ABSENT", accent=CRIMSON, size=24).move_to(RIGHT * 2.8 + UP * 0.9)

        # row 2: RB1 / Rb
        row2_gene = LabelChip("RB1 gene", accent=TEAL, size=24).move_to(LEFT * 2.8 + DOWN * 0.5)
        row2_arr = Arrow(LEFT * 1.2 + DOWN * 0.5, RIGHT * 0.8 + DOWN * 0.5,
                         color=INK, stroke_width=2, buff=0.05)
        row2_prot = LabelChip("Rb protein  ABSENT", accent=CRIMSON, size=24).move_to(RIGHT * 2.8 + DOWN * 0.5)

        # INTACT labels under gene chips
        intact1 = SerifLabel("intact", TEAL, size=22).next_to(row1_gene, DOWN, buff=0.18)
        intact2 = SerifLabel("intact", TEAL, size=22).next_to(row2_gene, DOWN, buff=0.18)

        self.play(FadeIn(h_gene), FadeIn(h_prot), Create(header_rule), run_time=0.8)
        self.play(FadeIn(row1_gene), FadeIn(intact1), run_time=0.6)
        self.play(GrowArrow(row1_arr), FadeIn(row1_prot), run_time=0.8)
        self.play(FadeIn(row2_gene), FadeIn(intact2), run_time=0.6)
        self.play(GrowArrow(row2_arr), FadeIn(row2_prot), run_time=0.8)
        self.wait(max(0.5, total - 3.6))


class B04_QuestionCard(Scene):
    """THE QUESTION — on screen and in narration."""
    def construct(self):
        total = DUR["B04"]
        _quote_scene(
            self,
            "Both genes intact. Neither protein functional.",
            "Why does a clean sequencing report mask the actual loss of both tumor suppressors?",
            None,
            "mask",
            total,
        )


class B05_NaiveModel(Scene):
    """The naive model: mutation -> protein loss -> function loss.
    Standard tumor suppressor loss — sequencing catches it."""
    def construct(self):
        total = DUR["B05"]
        label = SerifLabel("standard tumor suppressor loss", SLATE, size=26)
        label.to_edge(UP, buff=0.9)

        # chain: DNA node → MUTATION → protein node → function node
        dna_box = _gene_box("DNA", TEAL, width=2.0, height=0.8).move_to(LEFT * 4.8 + DOWN * 0.3)
        mutation = LabelChip("MUTATION", accent=CRIMSON, size=22)
        mutation.move_to(LEFT * 1.6 + DOWN * 0.3)

        prot_circ = _protein_circle("protein", CRIMSON, 0.42)
        prot_circ.move_to(RIGHT * 1.6 + DOWN * 0.3)

        # X over the protein circle
        prot_x = _x_mark(prot_circ.get_center(), CRIMSON, 0.3)

        function = LabelChip("FUNCTION LOST", accent=CRIMSON, size=20)
        function.move_to(RIGHT * 4.6 + DOWN * 0.3)

        arr1 = Arrow(dna_box.get_right(), mutation.get_left(), color=INK,
                     stroke_width=2.5, buff=0.1)
        arr2 = Arrow(mutation.get_right(), prot_circ.get_left(), color=INK,
                     stroke_width=2.5, buff=0.1)
        arr3 = Arrow(prot_circ.get_right(), function.get_left(), color=INK,
                     stroke_width=2.5, buff=0.1)

        seq_label = SerifLabel("sequencing detects this", TEAL, size=24)
        seq_label.next_to(mutation, DOWN, buff=0.6)
        tick_line = Line(mutation.get_bottom() + DOWN * 0.1,
                         seq_label.get_top() + UP * 0.08,
                         color=TEAL, stroke_width=1.5)

        self.play(FadeIn(label), run_time=0.5)
        self.play(FadeIn(dna_box), run_time=0.5)
        self.play(GrowArrow(arr1), FadeIn(mutation), run_time=0.7)
        self.play(GrowArrow(arr2), FadeIn(prot_circ), run_time=0.7)
        self.play(FadeIn(prot_x), run_time=0.4)
        self.play(GrowArrow(arr3), FadeIn(function), run_time=0.7)
        self.play(Create(tick_line), FadeIn(seq_label), run_time=0.7)
        self.wait(max(0.5, total - 4.2))


class B06_StandardCase(Scene):
    """Standard case: mutation present in gene, protein absent, sequencing
    catches it. Gene column vs protein column, one row each."""
    def construct(self):
        total = DUR["B06"]
        h_gene = SerifLabel("gene", CRIMSON, size=28).move_to(LEFT * 2.8 + UP * 1.8)
        h_prot = SerifLabel("protein", CRIMSON, size=28).move_to(RIGHT * 2.4 + UP * 1.8)
        rule = Line(LEFT * 5.5 + UP * 1.5, RIGHT * 5.5 + UP * 1.5,
                    color=INK, stroke_width=1.2)

        gene_chip = LabelChip("TP53  MUTATED", accent=CRIMSON, size=26).move_to(LEFT * 2.8 + UP * 0.4)
        prot_chip = LabelChip("p53  ABSENT", accent=CRIMSON, size=26).move_to(RIGHT * 2.6 + UP * 0.4)
        arr = Arrow(LEFT * 0.8 + UP * 0.4, RIGHT * 0.8 + UP * 0.4,
                    color=INK, stroke_width=2.5, buff=0.1)

        brace_line = Line(LEFT * 4.5 + DOWN * 0.5, LEFT * 1.3 + DOWN * 0.5,
                          color=TEAL, stroke_width=2)
        tick_down = Line(LEFT * 2.9 + UP * 0.0, LEFT * 2.9 + DOWN * 0.5,
                         color=TEAL, stroke_width=2)
        seq_label = SerifLabel("sequencing detects this", TEAL, size=26)
        seq_label.move_to(LEFT * 2.9 + DOWN * 1.1)

        self.play(FadeIn(h_gene), FadeIn(h_prot), Create(rule), run_time=0.7)
        self.play(FadeIn(gene_chip), GrowArrow(arr), FadeIn(prot_chip), run_time=1.0)
        self.play(Create(brace_line), Create(tick_down), run_time=0.5)
        self.play(FadeIn(seq_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


class B07_SectionMechanism(Scene):
    """Section card: THE MECHANISM — E6 and E7, protein-level sabotage."""
    def construct(self):
        total = DUR["B07"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=SLATE,
                       font_size=48, weight="MEDIUM")
        sub = SerifLabel("E6 and E7 — protein-level sabotage", CRIMSON, size=30)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.5).move_to(UP * 0.1)
        rule_top = Line(LEFT * 5.0 + UP * 1.2, RIGHT * 5.0 + UP * 1.2,
                        color=SLATE, stroke_width=1.5)
        rule_bot = Line(LEFT * 5.0 + DOWN * 0.6, RIGHT * 5.0 + DOWN * 0.6,
                        color=SLATE, stroke_width=1.5)
        self.play(FadeIn(heading, shift=DOWN * 0.2), Create(rule_top), run_time=0.8)
        self.play(FadeIn(sub), Create(rule_bot), run_time=0.7)
        # grow the section card
        card_bg = Rectangle(width=11.0, height=2.8)
        card_bg.set_fill(SLATE, 0.07).set_stroke(width=0, opacity=0)
        card_bg.move_to(block.get_center())
        self.play(card_bg.animate.scale(1.04), run_time=0.5)
        self.wait(max(0.5, total - 2.0))


class B08_E6Degrades(Scene):
    """E6 hijacks ubiquitin machinery to destroy p53 protein.
    Gene stays teal/intact throughout. Transform: protein -> destroyed."""
    def construct(self):
        total = DUR["B08"]

        # Left: gene box producing protein circles
        gene = _gene_box("TP53 gene", TEAL, width=2.4, height=0.85)
        gene.move_to(LEFT * 5.2 + UP * 1.0)
        gene_label = SerifLabel("intact", TEAL, size=22).next_to(gene, DOWN, buff=0.2)

        # p53 protein being produced
        p53_a = _protein_circle("p53", TEAL, 0.35).move_to(LEFT * 2.8 + UP * 1.0)
        prod_arr = Arrow(gene.get_right(), p53_a.get_left(),
                         color=TEAL, stroke_width=2, buff=0.08)

        # E6 viral protein node — center stage
        e6 = _viral_protein_node("E6", CRIMSON, 0.38).move_to(ORIGIN + UP * 0.0)
        e6_label = SerifLabel("viral protein", CRIMSON, size=22).next_to(e6, DOWN, buff=0.22)

        # Ubiquitin ligase node
        ub_box = Rectangle(width=2.4, height=0.75)
        ub_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        ub_label = Text("ubiquitin\nligase E6AP", font=SERIF, color=CRIMSON,
                        font_size=20, line_spacing=1.1)
        ub_label.move_to(ub_box)
        ubiquitin = VGroup(ub_box, ub_label).move_to(ORIGIN + DOWN * 1.6)

        # Proteasome (destruction)
        proteasome = LabelChip("PROTEASOME", accent=CRIMSON, size=22)
        proteasome.move_to(RIGHT * 4.4 + DOWN * 0.2)
        dest_label = SerifLabel("p53 destroyed", CRIMSON, size=22)
        dest_label.next_to(proteasome, DOWN, buff=0.2)

        # p53 copy that gets destroyed
        p53_b = _protein_circle("p53", TEAL, 0.35).move_to(RIGHT * 1.8 + UP * 0.4)

        # arrows
        arr_e6_ub = Arrow(e6.get_bottom(), ubiquitin.get_top(),
                          color=CRIMSON, stroke_width=2, buff=0.08)
        arr_ub_p53 = Arrow(ubiquitin.get_right(), p53_b.get_bottom(),
                           color=CRIMSON, stroke_width=2, buff=0.08)
        arr_p53_dest = Arrow(p53_b.get_right(), proteasome.get_left(),
                             color=CRIMSON, stroke_width=2, buff=0.08)

        self.play(FadeIn(gene), FadeIn(gene_label), run_time=0.6)
        self.play(GrowArrow(prod_arr), FadeIn(p53_a), run_time=0.7)
        self.play(FadeIn(e6), FadeIn(e6_label), run_time=0.7)
        self.play(GrowArrow(arr_e6_ub), FadeIn(ubiquitin), run_time=0.7)
        self.play(FadeIn(p53_b), GrowArrow(arr_ub_p53), run_time=0.6)
        self.play(GrowArrow(arr_p53_dest), run_time=0.5)
        # Transform: protein circle becomes destroyed (scale to 0, then show proteasome result)
        self.play(Transform(p53_b, proteasome), FadeIn(dest_label), run_time=0.9)
        self.play(gene.animate.scale(1.06), run_time=0.4)
        self.wait(max(0.5, total - 5.1))


class B09_E7FreesE2F(Scene):
    """E7 binds Rb, forces E2F loose, unlocks S-phase entry.
    RB1 gene stays teal/intact throughout. Transform animation."""
    def construct(self):
        total = DUR["B09"]

        # Left: RB1 gene box
        rb1_gene = _gene_box("RB1 gene", TEAL, width=2.4, height=0.85)
        rb1_gene.move_to(LEFT * 5.2 + UP * 0.6)
        rb1_label = SerifLabel("intact", TEAL, size=22).next_to(rb1_gene, DOWN, buff=0.2)

        # Rb protein node holding E2F
        rb_node = _protein_circle("Rb", TEAL, 0.42).move_to(LEFT * 1.2 + UP * 0.6)
        e2f_node = _protein_circle("E2F", TEAL, 0.32).move_to(RIGHT * 0.3 + UP * 0.6)
        hold_label = SerifLabel("sequestered", TEAL, size=20).next_to(e2f_node, DOWN, buff=0.15)

        gene_arr = Arrow(rb1_gene.get_right(), rb_node.get_left(),
                         color=TEAL, stroke_width=2, buff=0.08)

        # E7 viral protein
        e7 = _viral_protein_node("E7", CRIMSON, 0.38).move_to(LEFT * 1.2 + DOWN * 1.4)
        e7_label = SerifLabel("viral protein", CRIMSON, size=22).next_to(e7, DOWN, buff=0.22)
        arr_e7_rb = Arrow(e7.get_top(), rb_node.get_bottom(),
                          color=CRIMSON, stroke_width=2, buff=0.08)

        # After E7 binds: Rb disabled (crimson), E2F freed
        rb_disabled = _protein_circle("Rb", CRIMSON, 0.42).move_to(LEFT * 1.2 + UP * 0.6)
        e2f_freed = _protein_circle("E2F", TEAL, 0.38).move_to(RIGHT * 2.4 + UP * 0.6)
        freed_label = SerifLabel("released", TEAL, size=20).next_to(e2f_freed, DOWN, buff=0.15)

        # S-phase box
        sphase = LabelChip("S PHASE", accent=CRIMSON, size=26)
        sphase.move_to(RIGHT * 5.0 + UP * 0.6)
        sphase_note = SerifLabel("uncontrolled", CRIMSON, size=20).next_to(sphase, DOWN, buff=0.2)
        arr_e2f_s = Arrow(e2f_freed.get_right(), sphase.get_left(),
                          color=CRIMSON, stroke_width=2.5, buff=0.08)

        self.play(FadeIn(rb1_gene), FadeIn(rb1_label), run_time=0.6)
        self.play(GrowArrow(gene_arr), FadeIn(rb_node), FadeIn(e2f_node),
                  FadeIn(hold_label), run_time=0.8)
        self.play(FadeIn(e7), FadeIn(e7_label), GrowArrow(arr_e7_rb), run_time=0.8)
        # Transform: Rb becomes disabled, E2F becomes free
        self.play(Transform(rb_node, rb_disabled),
                  Transform(e2f_node, e2f_freed),
                  FadeOut(hold_label),
                  run_time=0.9)
        self.play(FadeIn(freed_label), GrowArrow(arr_e2f_s), FadeIn(sphase),
                  FadeIn(sphase_note), run_time=0.9)
        self.play(rb1_gene.animate.scale(1.06), run_time=0.4)
        self.wait(max(0.5, total - 4.4))


class B10_AssayBlind(Scene):
    """Two-layer diagram: DNA layer (teal) with intact genes on top;
    protein layer (crimson) with absent proteins below.
    Sequencing arrow stops at the layer boundary."""
    def construct(self):
        total = DUR["B10"]

        # DNA layer
        dna_bg = Rectangle(width=12.0, height=1.9)
        dna_bg.set_fill(TEAL, 0.08).set_stroke(TEAL, 2.0)
        dna_bg.move_to(UP * 1.5)
        dna_layer_label = SerifLabel("DNA layer", TEAL, size=24).move_to(LEFT * 4.8 + UP * 1.5)
        tp53_box = LabelChip("TP53 intact", accent=TEAL, size=22).move_to(UP * 1.5 + LEFT * 0.8)
        rb1_box = LabelChip("RB1 intact", accent=TEAL, size=22).move_to(UP * 1.5 + RIGHT * 2.4)

        # Protein layer
        prot_bg = Rectangle(width=12.0, height=1.9)
        prot_bg.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 2.0)
        prot_bg.move_to(DOWN * 1.5)
        prot_layer_label = SerifLabel("protein layer", CRIMSON, size=24).move_to(LEFT * 4.5 + DOWN * 1.5)

        p53_absent_chip = LabelChip("p53  ABSENT", accent=CRIMSON, size=22).move_to(DOWN * 1.5 + LEFT * 0.8)
        rb_absent_chip = LabelChip("Rb  ABSENT", accent=CRIMSON, size=22).move_to(DOWN * 1.5 + RIGHT * 2.4)

        # Sequencing assay arrow — stops at boundary
        assay_label = SerifLabel("sequencing reads here only", TEAL, size=22)
        assay_label.move_to(RIGHT * 4.5 + UP * 2.4)
        assay_arr = Arrow(RIGHT * 4.5 + UP * 2.1, RIGHT * 4.5 + UP * 0.55,
                          color=TEAL, stroke_width=3, buff=0.05)

        # Block symbol where the arrow stops — cannot cross
        stop_rect = Rectangle(width=0.5, height=0.15)
        stop_rect.set_fill(INK, 1).set_stroke(width=0, opacity=0)
        stop_rect.move_to(RIGHT * 4.5 + UP * 0.55)
        cannot_see = SerifLabel("cannot see below", INK, size=20)
        cannot_see.next_to(stop_rect, RIGHT, buff=0.2)

        self.play(FadeIn(dna_bg), FadeIn(dna_layer_label), run_time=0.6)
        self.play(FadeIn(tp53_box), FadeIn(rb1_box), run_time=0.7)
        self.play(FadeIn(prot_bg), FadeIn(prot_layer_label), run_time=0.6)
        self.play(FadeIn(p53_absent_chip), FadeIn(rb_absent_chip), run_time=0.7)
        self.play(FadeIn(assay_label), GrowArrow(assay_arr), run_time=0.8)
        self.play(FadeIn(stop_rect), FadeIn(cannot_see), run_time=0.6)
        # grow the DNA layer gently to reinforce "sequencing reads here"
        self.play(dna_bg.animate.scale(1.03), run_time=0.5)
        self.wait(max(0.5, total - 4.5))


class B11_IsotypeExample(Scene):
    """Isotype grid of 100 cervical cancers.
    Step 1: 10 crimson (TP53 mutated), 90 teal (WT by sequencing).
    Step 2: of the 90 teal, 70 flip to crimson (p53 absent by IHC).
    All numbers labeled illustrative."""
    def construct(self):
        total = DUR["B11"]

        header = SerifLabel("100 cervical cancers  (illustrative)", SLATE, size=26)
        header.to_edge(UP, buff=0.7)

        # Build grid manually: 10 crimson then 90 teal
        size = 0.26
        gap = 0.08
        per_row = 10
        marks = VGroup()
        colors_step1 = [CRIMSON] * 10 + [TEAL] * 90
        for i, c in enumerate(colors_step1):
            sq = Square(size).set_fill(c, 1).set_stroke(width=0, opacity=0)
            sq.move_to(RIGHT * (i % per_row) * (size + gap)
                       + DOWN * (i // per_row) * (size + gap))
            marks.add(sq)
        marks.move_to(UP * 0.3)

        # Legend step 1
        leg1a = LabelChip("TP53 mutated (10)", accent=CRIMSON, size=20)
        leg1b = LabelChip("TP53 wild-type (90)", accent=TEAL, size=20)
        legend1 = VGroup(leg1a, leg1b).arrange(RIGHT, buff=0.5)
        legend1.next_to(marks, DOWN, buff=0.55)

        seq_label = SerifLabel("by sequencing", SLATE, size=22)
        seq_label.next_to(legend1, DOWN, buff=0.28)

        self.play(FadeIn(header), run_time=0.5)
        self.play(AnimationGroup(
            *[FadeIn(m, scale=0.85) for m in marks],
            lag_ratio=0.006, run_time=2.5
        ))
        self.play(FadeIn(legend1), FadeIn(seq_label), run_time=0.7)
        self.wait(0.6)

        # Step 2: flip 70 of the 90 teal marks to crimson (indices 10..79)
        flip_targets = marks[10:80]   # the 70 that will show absent protein
        self.play(AnimationGroup(
            *[m.animate.set_fill(CRIMSON, 1) for m in flip_targets],
            lag_ratio=0.008, run_time=2.0
        ))

        # Updated legend
        leg2a = LabelChip("p53 absent by IHC (70 of 90 WT)", accent=CRIMSON, size=20)
        leg2b = LabelChip("p53 present (20)", accent=TEAL, size=20)
        legend2 = VGroup(leg2a, leg2b).arrange(RIGHT, buff=0.5)
        legend2.move_to(legend1.get_center())
        ihc_label = SerifLabel("by immunohistochemistry (IHC)", SLATE, size=22)
        ihc_label.next_to(legend2, DOWN, buff=0.28)

        self.play(FadeOut(legend1), FadeOut(seq_label), run_time=0.4)
        self.play(FadeIn(legend2), FadeIn(ihc_label), run_time=0.7)
        self.wait(max(0.5, total - 7.4))


class B12_Blueprint(Scene):
    """Blueprint metaphor: gene is the blueprint, E6/E7 destroy the product.
    Gold highlighter fill under the word 'blueprints'. Single gold use."""
    def construct(self):
        total = DUR["B12"]

        # Gene / blueprint node
        gene_box = Rectangle(width=3.0, height=1.1)
        gene_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2.5)
        gene_chip = LabelChip("gene\n(blueprint)", accent=TEAL, size=24)
        gene_chip.move_to(gene_box)
        blueprint = VGroup(gene_box, gene_chip).move_to(LEFT * 4.0 + UP * 0.5)

        # Product / protein node
        prod_circ = Circle(radius=0.5)
        prod_circ.set_fill(TEAL, 0.2).set_stroke(TEAL, 2.5)
        prod_text = Text("protein", font=SERIF, color=TEAL, font_size=22)
        prod_text.move_to(prod_circ)
        product_node = VGroup(prod_circ, prod_text).move_to(ORIGIN + UP * 0.5)

        # E6/E7 crimson arrow destroying product
        e6e7_node = _viral_protein_node("E6 / E7", CRIMSON, 0.38).move_to(ORIGIN + DOWN * 1.5)
        destroy_arr = Arrow(e6e7_node.get_right(),
                            product_node.get_bottom() + RIGHT * 0.2,
                            color=CRIMSON, stroke_width=3, buff=0.08)
        x_mark = _x_mark(product_node.get_center(), CRIMSON, 0.38)

        # Production arrow (gene -> protein)
        prod_arr = Arrow(blueprint.get_right(), product_node.get_left(),
                         color=TEAL, stroke_width=2.5, buff=0.1)
        prod_ann = SerifLabel("transcription / translation", SLATE, size=20)
        prod_ann.next_to(prod_arr, UP, buff=0.15)

        # Gold highlighter bar under 'blueprints' — the one gold use
        gold_bar = Rectangle(width=3.4, height=0.38)
        gold_bar.set_fill(GOLD, 0.65).set_stroke(width=0, opacity=0)
        seq_text = Text("sequencing reads blueprints",
                        font=SERIF, color=INK, font_size=28)
        seq_text.move_to(DOWN * 2.5)
        gold_bar.move_to(seq_text.get_center())

        # Product gone on the right
        gone_chip = LabelChip("product destroyed", accent=CRIMSON, size=22)
        gone_chip.next_to(product_node, RIGHT, buff=0.5)

        self.play(FadeIn(blueprint), run_time=0.6)
        self.play(GrowArrow(prod_arr), FadeIn(prod_ann), FadeIn(product_node), run_time=0.8)
        self.play(FadeIn(e6e7_node), GrowArrow(destroy_arr), run_time=0.7)
        self.play(FadeIn(x_mark), FadeIn(gone_chip), run_time=0.6)
        # Gold bar + label
        self.play(FadeIn(gold_bar), FadeIn(seq_text), run_time=0.7)
        # Scale blueprint gently (shape motion for Gate A)
        self.play(blueprint.animate.scale(1.05), run_time=0.5)
        self.wait(max(0.5, total - 3.9))


class B13_Endcard(Scene):
    """Endcard: question restated -> answer, CANCER BIOLOGY kicker.
    INK fill for all text, never GOLD as text color."""
    def construct(self):
        total = DUR["B13"]
        kicker = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=26, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.8)

        t1 = Text("Intact genes. Absent proteins.", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("E6 and E7 inactivate tumor suppressors", font=SERIF,
                  color=INK, font_size=36)
        t3 = Text("at the protein level — invisible to sequencing.",
                  font=SERIF, color=INK, font_size=36)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.22).move_to(UP * 0.1)
        u = Line(t1.get_corner(DL) + DOWN * 0.14,
                 t1.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.play(FadeIn(t3), run_time=0.7)
        self.wait(max(0.5, total - 2.8))
