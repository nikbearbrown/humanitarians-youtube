"""vox_scenes.py — Why a Deleted Passenger Gene Creates a Target the Driver Gene Never Could
(vox-mtap-passenger, slate cut, 16:9)

One Scene per GRAPHIC beat. All 14 beats are own-Manim.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law:
  TEAL   = intact/normal/full-margin (MTAP intact, PRMT5 at 100%, survival)
  CRIMSON = deleted/depleted/below-threshold (MTAP deleted, MTA accumulation, throttled, death)
  GOLD   = single editor's-pen highlight (survival threshold line)

Exclusions: no SAM/MTA biochemistry, no PRMT5 substrate biology, no CDK4/6 inhibitor
clinical comparison, no cancer-type breakdown, no other 9p21 targets.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import json, os, numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


# ---------------------------------------------------------------- B01 — chromosome locus map

class B01_LocusMap(Scene):
    """Cold open: 9p21 locus with CDKN2A and MTAP both being deleted."""
    def construct(self):
        total = DUR["B01"]
        # Chromosome arm bar
        arm = Rectangle(width=10.0, height=0.5)
        arm.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        arm.move_to(UP * 0.5)

        # Gene blocks on the chromosome
        cdkn2a_block = Rectangle(width=1.6, height=0.5)
        cdkn2a_block.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        cdkn2a_block.move_to(LEFT * 1.5 + UP * 0.5)

        mtap_block = Rectangle(width=1.2, height=0.5)
        mtap_block.set_fill(CRIMSON, 0.7).set_stroke(width=0, opacity=0)
        mtap_block.move_to(RIGHT * 0.5 + UP * 0.5)

        # Labels below the blocks
        cdkn2a_label = Text("CDKN2A", font=DISPLAY, color=CRIMSON,
                            font_size=22, weight=BOLD)
        cdkn2a_label.next_to(cdkn2a_block, DOWN, buff=0.35)

        mtap_label = Text("MTAP", font=DISPLAY, color=CRIMSON,
                          font_size=22, weight=BOLD)
        mtap_label.next_to(mtap_block, DOWN, buff=0.35)

        # 9p21 label
        locus_label = Text("chromosome 9p21", font=SERIF, color=INK,
                           font_size=24, slant=ITALIC)
        locus_label.next_to(arm, UP, buff=0.4)

        # Deletion bracket
        del_start = LEFT * 2.5 + UP * 0.5
        del_end = RIGHT * 1.3 + UP * 0.5

        self.play(FadeIn(arm), FadeIn(locus_label), run_time=0.8)
        self.play(FadeIn(cdkn2a_block), FadeIn(mtap_block),
                  FadeIn(cdkn2a_label), FadeIn(mtap_label), run_time=1.0)

        # Deletion sweep: brace below blocks
        del_brace = Brace(VGroup(cdkn2a_block, mtap_block), DOWN, color=CRIMSON)
        del_text = Text("deleted", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC)
        del_text.next_to(del_brace, DOWN, buff=0.15)

        self.play(FadeIn(del_brace), FadeIn(del_text), run_time=0.9)
        self.wait(max(0.3, total - 2.7))


# ---------------------------------------------------------------- B02 — driver gene chip

class B02_DriverChip(Scene):
    """CDKN2A named as the famous driver tumor suppressor."""
    def construct(self):
        total = DUR["B02"]

        eyebrow = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        eyebrow.move_to(UP * 2.8)

        # Backing rectangle gives Gate A a trackable shape
        backing = Rectangle(width=5.0, height=1.2)
        backing.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2)
        backing.move_to(UP * 0.5)

        gene_chip = LabelChip("CDKN2A", accent=CRIMSON, size=42)
        gene_chip.move_to(UP * 0.5)

        driver_chip = LabelChip("DRIVER", accent=SLATE, size=26)
        driver_chip.move_to(LEFT * 3.8 + UP * 0.5)

        ts_chip = LabelChip("TUMOR SUPPRESSOR", accent=SLATE, size=26)
        ts_chip.move_to(RIGHT * 3.8 + UP * 0.5)

        note = Text("p16 / INK4a — brakes CDK4 and CDK6", font=SERIF,
                    color=INK, font_size=24, slant=ITALIC)
        note.next_to(gene_chip, DOWN, buff=0.55)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(backing, scale=0.8), FadeIn(gene_chip, scale=0.9), run_time=0.8)
        self.play(FadeIn(driver_chip, shift=RIGHT * 0.2),
                  FadeIn(ts_chip, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.7))


# ---------------------------------------------------------------- B03 — question card

class B03_QuestionCard(Scene):
    """THE QUESTION beat — gap formula on screen."""
    def construct(self):
        total = DUR["B03"]

        # Question card panel
        panel = Rectangle(width=11.0, height=4.5)
        panel.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        panel.move_to(ORIGIN)

        q_line1 = Text("CDKN2A is the driver.", font=DISPLAY, color=WHITE,
                       font_size=30, weight=BOLD)
        q_line2 = Text("MTAP is the bystander.", font=DISPLAY, color=WHITE,
                       font_size=30, weight=BOLD)
        # GOLD is fill-only, not text: use INK (on SLATE panel INK reads fine)
        q_line3 = Text("Why does the bystander create", font=DISPLAY, color=INK,
                       font_size=30, weight=BOLD)
        q_line4 = Text("the better drug target?", font=DISPLAY, color=INK,
                       font_size=30, weight=BOLD)
        # GOLD underline accent on the question lines (fill, not text)
        u = Line(q_line4.get_corner(DL) + DOWN * 0.12,
                 q_line4.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=3)

        block = VGroup(q_line1, q_line2, q_line3, q_line4).arrange(DOWN, buff=0.22)
        block.move_to(ORIGIN)

        self.play(FadeIn(panel), run_time=0.6)
        self.play(FadeIn(q_line1), FadeIn(q_line2), run_time=0.8)
        self.play(FadeIn(q_line3), FadeIn(q_line4), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.2))


# ---------------------------------------------------------------- B04 — pathway arrow (naive target)

class B04_NaiveTarget(Scene):
    """The Problem: naive target via p16 -> CDK4/6 -> brake."""
    def construct(self):
        total = DUR["B04"]

        # Chain: p16 -> CDK4/6 -> division brake
        p16_chip = LabelChip("p16 (CDKN2A)", accent=TEAL, size=26)
        p16_chip.move_to(LEFT * 4.5 + UP * 0.5)

        arrow1 = Arrow(LEFT * 3.0 + UP * 0.5, LEFT * 1.8 + UP * 0.5,
                       color=INK, stroke_width=3, buff=0.1)

        cdk_chip = LabelChip("CDK4 / CDK6", accent=SLATE, size=26)
        cdk_chip.move_to(LEFT * 0.5 + UP * 0.5)

        arrow2 = Arrow(RIGHT * 0.9 + UP * 0.5, RIGHT * 2.1 + UP * 0.5,
                       color=TEAL, stroke_width=3, buff=0.1)

        brake_label = SerifLabel("division brake", TEAL, size=28)
        brake_label.move_to(RIGHT * 3.8 + UP * 0.5)

        # Deletion: CDKN2A crossed out
        del_line = Line(p16_chip.get_left() + LEFT * 0.1,
                        p16_chip.get_right() + RIGHT * 0.1,
                        color=CRIMSON, stroke_width=5)
        del_line._qc_intentional = True   # deliberate strike-through
        del_chip = LabelChip("DELETED", accent=CRIMSON, size=22)
        del_chip.next_to(p16_chip, DOWN, buff=0.45)

        brake_gone = Text("brake gone", font=SERIF, color=CRIMSON,
                          font_size=22, slant=ITALIC)
        brake_gone.next_to(brake_label, DOWN, buff=0.3)

        self.play(FadeIn(p16_chip), run_time=0.6)
        self.play(Create(arrow1), FadeIn(cdk_chip), run_time=0.7)
        self.play(Create(arrow2), FadeIn(brake_label), run_time=0.7)
        self.play(Create(del_line), FadeIn(del_chip), run_time=0.7)
        self.play(FadeIn(brake_gone, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


# ---------------------------------------------------------------- B05 — selectivity problem

class B05_SelectivityProblem(Scene):
    """CDK4/6 deregulated in many cancers — too broad a target."""
    def construct(self):
        total = DUR["B05"]

        title = Text("CDK4/6 is deregulated across many cancers", font=SERIF,
                     color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.0)

        # Broad-target circle gives Gate A a trackable shape
        broad_circle = Circle(radius=2.2)
        broad_circle.set_fill(SLATE, 0.07).set_stroke(SLATE, 2.5)
        broad_circle.move_to(UP * 0.2)

        # Multiple tumor type chips showing CDK4/6 deregulation
        tumor_types = ["BREAST", "LUNG", "COLON", "PROSTATE", "MELANOMA",
                       "BLADDER", "OVARIAN", "PANCREATIC"]
        chips = VGroup()
        for name in tumor_types:
            c = LabelChip(name, accent=SLATE, size=20)
            chips.add(c)

        chips.arrange_in_grid(rows=2, buff=(0.35, 0.4))
        chips.move_to(UP * 0.2)

        # CDK4/6 in the center
        cdk_big = LabelChip("CDK4 / CDK6", accent=SLATE, size=32)
        cdk_big.move_to(DOWN * 2.2)

        no_select = Text("no selectivity for 9p21-deleted cells", font=SERIF,
                         color=CRIMSON, font_size=24, slant=ITALIC)
        no_select.next_to(cdk_big, DOWN, buff=0.4)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(broad_circle, scale=0.5), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips],
                              lag_ratio=0.08), run_time=1.2)
        self.play(FadeIn(cdk_big, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(no_select, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.6))


# ---------------------------------------------------------------- B06 — locus deletion map

class B06_LocusDeletion(Scene):
    """Mechanism: CDKN2A and MTAP are adjacent on 9p21 — passenger concept."""
    def construct(self):
        total = DUR["B06"]

        # Chromosome band
        arm = Rectangle(width=11.0, height=0.55)
        arm.set_fill(SLATE, 0.5).set_stroke(width=0, opacity=0)
        arm.move_to(UP * 0.8)

        # Gene blocks
        cdkn2a_b = Rectangle(width=2.0, height=0.55)
        cdkn2a_b.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        cdkn2a_b.move_to(LEFT * 1.8 + UP * 0.8)

        mtap_b = Rectangle(width=1.4, height=0.55)
        mtap_b.set_fill(CRIMSON, 0.75).set_stroke(width=0, opacity=0)
        mtap_b.move_to(RIGHT * 0.8 + UP * 0.8)

        # Labels
        cdkn2a_lbl = Text("CDKN2A", font=DISPLAY, color=CRIMSON,
                           font_size=22, weight=BOLD)
        cdkn2a_lbl.next_to(cdkn2a_b, DOWN, buff=0.3)

        mtap_lbl = Text("MTAP", font=DISPLAY, color=CRIMSON,
                        font_size=22, weight=BOLD)
        mtap_lbl.next_to(mtap_b, DOWN, buff=0.3)

        driver_sub = Text("DRIVER", font=DISPLAY, color=INK, font_size=17)
        driver_sub.next_to(cdkn2a_lbl, DOWN, buff=0.1)

        passenger_sub = Text("PASSENGER", font=DISPLAY, color=INK, font_size=17)
        passenger_sub.next_to(mtap_lbl, DOWN, buff=0.1)

        # Deletion brace
        del_brace = Brace(VGroup(cdkn2a_b, mtap_b), UP, color=CRIMSON)
        del_lbl = Text("9p21 deletion", font=SERIF, color=CRIMSON,
                       font_size=22, slant=ITALIC)
        del_lbl.next_to(del_brace, UP, buff=0.15)

        no_pressure = Text("no selective pressure for or against MTAP loss",
                           font=SERIF, color=INK, font_size=20, slant=ITALIC)
        no_pressure.move_to(DOWN * 2.5)

        self.play(FadeIn(arm), run_time=0.5)
        self.play(FadeIn(cdkn2a_b), FadeIn(cdkn2a_lbl), FadeIn(driver_sub), run_time=0.7)
        self.play(FadeIn(mtap_b), FadeIn(mtap_lbl), FadeIn(passenger_sub), run_time=0.7)
        self.play(FadeIn(del_brace), FadeIn(del_lbl), run_time=0.8)
        self.play(FadeIn(no_pressure, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.3))


# ---------------------------------------------------------------- B07 — MTA accumulation chain

class B07_MTAChain(Scene):
    """MTAP deleted -> MTA accumulates -> PRMT5 throttled."""
    def construct(self):
        total = DUR["B07"]

        # Three-node chain
        node1 = LabelChip("MTAP DELETED", accent=CRIMSON, size=26)
        node1.move_to(LEFT * 4.2 + UP * 0.5)

        arr1 = Arrow(LEFT * 2.6 + UP * 0.5, LEFT * 1.2 + UP * 0.5,
                     color=CRIMSON, stroke_width=3, buff=0.1)

        node2_bg = Rectangle(width=2.4, height=0.75)
        node2_bg.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        node2_bg.move_to(UP * 0.5)
        node2_text = Text("MTA accumulates", font=DISPLAY, color=CRIMSON,
                          font_size=22, weight=BOLD)
        node2_text.move_to(node2_bg.get_center())
        node2 = VGroup(node2_bg, node2_text)

        arr2 = Arrow(RIGHT * 1.2 + UP * 0.5, RIGHT * 2.6 + UP * 0.5,
                     color=CRIMSON, stroke_width=3, buff=0.1)

        node3_bg = Rectangle(width=2.8, height=0.75)
        node3_bg.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        node3_bg.move_to(RIGHT * 4.1 + UP * 0.5)
        node3_text = Text("PRMT5 throttled", font=DISPLAY, color=CRIMSON,
                          font_size=22, weight=BOLD)
        node3_text.move_to(node3_bg.get_center())
        node3 = VGroup(node3_bg, node3_text)

        # What is PRMT5
        prmt5_note = Text("arginine methyltransferase", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC)
        prmt5_note.next_to(node3, DOWN, buff=0.4)

        # MTA similar to SAM (brief note — not the full biochemistry)
        mta_note = Text("MTA competes with the methyl donor at PRMT5", font=SERIF,
                        color=INK, font_size=20, slant=ITALIC)
        mta_note.move_to(DOWN * 2.3)

        self.play(FadeIn(node1, scale=0.9), run_time=0.6)
        self.play(Create(arr1), FadeIn(node2, shift=RIGHT * 0.3), run_time=0.8)
        self.play(Create(arr2), FadeIn(node3, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(prmt5_note, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(mta_note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


# ---------------------------------------------------------------- B08 — single bar: 60% (PRMT5 in tumor)

class B08_SingleBar(Scene):
    """Tumor cell PRMT5 at 60% — single bar approaching threshold."""
    def construct(self):
        total = DUR["B08"]

        # Bar chart: single crimson bar
        bar_height = 2.4   # 60% of a 4.0 total
        bar = Rectangle(width=1.6, height=bar_height)
        bar.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        bar.move_to(LEFT * 1.5 + DOWN * (2.0 - bar_height / 2))

        # Axis
        axis = Line(LEFT * 2.8 + DOWN * 2.0, LEFT * 2.8 + UP * 2.2,
                    color=INK, stroke_width=2)
        base = Line(LEFT * 2.8 + DOWN * 2.0, RIGHT * 0.5 + DOWN * 2.0,
                    color=INK, stroke_width=2)

        # Survival threshold line
        threshold_y = UP * 0.4
        thresh_line = Line(LEFT * 2.9 + threshold_y, RIGHT * 0.6 + threshold_y,
                           color=GOLD, stroke_width=3)
        thresh_label = Text("survival threshold", font=SERIF, color=INK,
                            font_size=20, slant=ITALIC)
        thresh_label.next_to(thresh_line, RIGHT, buff=0.25)

        # 60% label on bar
        pct_label = Text("60%", font=DISPLAY, color=WHITE, font_size=32, weight=BOLD)
        pct_label.move_to(bar.get_center())

        # Bar title
        bar_title = Text("PRMT5 activity", font=SERIF, color=INK,
                         font_size=22, slant=ITALIC)
        bar_title.move_to(LEFT * 1.5 + DOWN * 2.6)

        cell_label = LabelChip("MTAP-DELETED TUMOR CELL", accent=CRIMSON, size=22)
        cell_label.move_to(LEFT * 1.5 + DOWN * 3.2)

        close_note = Text("pre-throttled by MTA accumulation", font=SERIF,
                          color=CRIMSON, font_size=20, slant=ITALIC)
        close_note.move_to(RIGHT * 3.0 + DOWN * 1.2)

        self.play(FadeIn(axis), FadeIn(base), run_time=0.5)
        self.play(FadeIn(bar, shift=UP * 0.4), FadeIn(pct_label), run_time=0.8)
        self.play(Create(thresh_line), FadeIn(thresh_label), run_time=0.7)
        self.play(FadeIn(bar_title), FadeIn(cell_label), run_time=0.6)
        self.play(FadeIn(close_note, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.3, total - 3.1))


# ---------------------------------------------------------------- B09 — two bars: tumor vs normal

class B09_TwoBars(Scene):
    """Tumor (60%, CRIMSON) vs Normal (100%, TEAL) — threshold between them."""
    def construct(self):
        total = DUR["B09"]

        full_h = 4.0   # 100% height reference
        bar_scale = 3.2 / full_h

        tumor_h = full_h * 0.60 * bar_scale   # 60%
        normal_h = full_h * 1.00 * bar_scale  # 100%
        base_y = DOWN * 2.0

        # Tumor bar (CRIMSON)
        tumor_bar = Rectangle(width=1.5, height=tumor_h)
        tumor_bar.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        tumor_bar.move_to(LEFT * 2.8 + base_y + UP * tumor_h / 2)

        # Normal bar (TEAL)
        normal_bar = Rectangle(width=1.5, height=normal_h)
        normal_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        normal_bar.move_to(RIGHT * 2.8 + base_y + UP * normal_h / 2)

        # Axes
        laxis = Line(LEFT * 4.0 + base_y, LEFT * 4.0 + UP * 2.4,
                     color=INK, stroke_width=2)
        base_line = Line(LEFT * 4.0 + base_y, RIGHT * 4.6 + base_y,
                         color=INK, stroke_width=2)

        # Survival threshold (between bars)
        threshold_y = base_y + UP * (full_h * 0.75 * bar_scale)
        thresh_line = Line(LEFT * 4.1 + threshold_y, RIGHT * 4.7 + threshold_y,
                           color=GOLD, stroke_width=3)
        thresh_label = SerifLabel("survival threshold", GOLD, size=20)
        thresh_label.next_to(thresh_line, RIGHT, buff=0.2)

        # Percentage labels on bars
        t_pct = Text("60%", font=DISPLAY, color=WHITE, font_size=28, weight=BOLD)
        t_pct.move_to(tumor_bar.get_center())
        n_pct = Text("100%", font=DISPLAY, color=WHITE, font_size=28, weight=BOLD)
        n_pct.move_to(normal_bar.get_center())

        # Chip labels
        t_chip = LabelChip("TUMOR CELL", accent=CRIMSON, size=22)
        t_chip.next_to(tumor_bar, DOWN, buff=0.3)
        n_chip = LabelChip("NORMAL CELL", accent=TEAL, size=22)
        n_chip.next_to(normal_bar, DOWN, buff=0.3)

        # Subtitle
        sub = Text("PRMT5 activity — before any inhibitor", font=SERIF,
                   color=INK, font_size=21, slant=ITALIC)
        sub.move_to(UP * 2.9)

        self.play(FadeIn(laxis), FadeIn(base_line), FadeIn(sub), run_time=0.5)
        self.play(FadeIn(tumor_bar, shift=UP * 0.3), FadeIn(t_pct),
                  FadeIn(t_chip), run_time=0.8)
        self.play(FadeIn(normal_bar, shift=UP * 0.3), FadeIn(n_pct),
                  FadeIn(n_chip), run_time=0.8)
        self.play(Create(thresh_line), FadeIn(thresh_label), run_time=0.7)
        self.wait(max(0.3, total - 2.8))


# ---------------------------------------------------------------- B10 — threshold diagram (core visual)

class B10_ThresholdDiagram(Scene):
    """THE KEY VISUAL: inhibitor drops both bars; only tumor crosses threshold."""
    def construct(self):
        total = DUR["B10"]

        full_h = 4.0
        bar_scale = 3.2 / full_h
        base_y = DOWN * 2.0

        # Initial bars (before inhibitor)
        tumor_h0 = full_h * 0.60 * bar_scale
        normal_h0 = full_h * 1.00 * bar_scale

        # After inhibitor: drop ~35% of full height
        tumor_h1 = max(0.05, tumor_h0 - full_h * 0.38 * bar_scale)
        normal_h1 = normal_h0 - full_h * 0.38 * bar_scale

        threshold_y_offset = full_h * 0.75 * bar_scale

        def make_bar(h, color, x_center):
            b = Rectangle(width=1.6, height=h)
            b.set_fill(color, 1).set_stroke(width=0, opacity=0)
            b.move_to(np.array([x_center, 0, 0]) + base_y + UP * h / 2)
            return b

        tumor_bar0 = make_bar(tumor_h0, CRIMSON, -2.8)
        normal_bar0 = make_bar(normal_h0, TEAL, 2.8)

        # Axes
        laxis = Line(LEFT * 4.2 + base_y, LEFT * 4.2 + UP * 2.6,
                     color=INK, stroke_width=2)
        base_line = Line(LEFT * 4.2 + base_y, RIGHT * 5.0 + base_y,
                         color=INK, stroke_width=2)

        # Survival threshold line
        threshold_y = base_y + UP * threshold_y_offset
        thresh_line = Line(LEFT * 4.3 + threshold_y, RIGHT * 5.1 + threshold_y,
                           color=GOLD, stroke_width=3)
        thresh_label = SerifLabel("survival threshold", GOLD, size=20)
        thresh_label.next_to(thresh_line, RIGHT, buff=0.2)

        # Chips
        t_chip = LabelChip("TUMOR", accent=CRIMSON, size=22)
        t_chip.next_to(base_y + LEFT * 2.8, DOWN, buff=0.3)
        n_chip = LabelChip("NORMAL", accent=TEAL, size=22)
        n_chip.next_to(base_y + RIGHT * 2.8, DOWN, buff=0.3)

        # Title
        title = Text("PRMT5 activity + PRMT5 inhibitor added", font=SERIF,
                     color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 2.9)

        self.play(FadeIn(laxis), FadeIn(base_line), FadeIn(title), run_time=0.5)
        self.play(FadeIn(tumor_bar0), FadeIn(normal_bar0),
                  FadeIn(t_chip), FadeIn(n_chip), run_time=0.8)
        self.play(Create(thresh_line), FadeIn(thresh_label), run_time=0.7)

        # Drop both bars under the inhibitor
        tumor_bar1 = make_bar(tumor_h1, CRIMSON, -2.8)
        normal_bar1 = make_bar(normal_h1, TEAL, 2.8)

        inhibitor_chip = LabelChip("PRMT5 INHIBITOR ADDED", accent=SLATE, size=24)
        inhibitor_chip.move_to(UP * 1.8)

        self.play(FadeIn(inhibitor_chip, scale=0.9), run_time=0.5)
        self.play(ReplacementTransform(tumor_bar0, tumor_bar1),
                  ReplacementTransform(normal_bar0, normal_bar1), run_time=1.1)

        # Outcome labels
        death_label = LabelChip("DEATH", accent=CRIMSON, size=28)
        death_label.move_to(LEFT * 2.8 + DOWN * 1.5)
        survive_label = LabelChip("SURVIVAL", accent=TEAL, size=28)
        survive_label.move_to(RIGHT * 2.8 + DOWN * 1.5)

        self.play(FadeIn(death_label, scale=0.9), FadeIn(survive_label, scale=0.9),
                  run_time=0.8)
        self.wait(max(0.3, total - 4.4))


# ---------------------------------------------------------------- B11 — synthetic lethality grid

class B11_SyntheticLethalityGrid(Scene):
    """2x2 grid: synthetic lethality defined."""
    def construct(self):
        total = DUR["B11"]

        # Grid coordinates
        cx = [-2.5, 2.5]
        cy = [1.0, -1.3]
        cell_w, cell_h = 4.5, 2.0

        # Header labels
        col_header1 = Text("MTAP intact", font=DISPLAY, color=TEAL,
                           font_size=22, weight=BOLD)
        col_header1.move_to(LEFT * 2.5 + UP * 2.7)
        col_header2 = Text("MTAP deleted", font=DISPLAY, color=CRIMSON,
                           font_size=22, weight=BOLD)
        col_header2.move_to(RIGHT * 2.5 + UP * 2.7)

        row_header1 = Text("no inhibitor", font=DISPLAY, color=INK,
                           font_size=20, weight=BOLD)
        row_header1.move_to(LEFT * 5.4 + UP * 1.0)
        row_header2 = Text("+ inhibitor", font=DISPLAY, color=INK,
                           font_size=20, weight=BOLD)
        row_header2.move_to(LEFT * 5.4 + DOWN * 1.3)

        # Cells: intact/no-inh = survive, deleted/no-inh = survive,
        #        intact/+ inh = survive, deleted/+ inh = DEAD
        def make_cell(x, y, label, color):
            bg = Rectangle(width=cell_w, height=cell_h)
            bg.set_fill(color, 0.12).set_stroke(color, 2)
            bg.move_to(np.array([x, y, 0]))
            txt = Text(label, font=DISPLAY, color=color,
                       font_size=26, weight=BOLD)
            txt.move_to(bg.get_center())
            return VGroup(bg, txt)

        c_intact_no = make_cell(-2.5, 1.0, "SURVIVE", TEAL)
        c_deleted_no = make_cell(2.5, 1.0, "SURVIVE", TEAL)
        c_intact_inh = make_cell(-2.5, -1.3, "SURVIVE", TEAL)
        c_deleted_inh = make_cell(2.5, -1.3, "DEAD", CRIMSON)

        self.play(FadeIn(col_header1), FadeIn(col_header2),
                  FadeIn(row_header1), FadeIn(row_header2), run_time=0.7)
        self.play(FadeIn(c_intact_no), FadeIn(c_deleted_no), run_time=0.7)
        self.play(FadeIn(c_intact_inh), run_time=0.5)
        self.play(FadeIn(c_deleted_inh, scale=0.9), run_time=0.8)

        # Label: synthetic lethality
        sl_label = Text("synthetic lethality", font=SERIF, color=CRIMSON,
                        font_size=26, slant=ITALIC)
        sl_label.move_to(DOWN * 3.0)
        self.play(FadeIn(sl_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.3))


# ---------------------------------------------------------------- B12 — trial criteria

class B12_TrialCriteria(Scene):
    """Clinical trial criteria: MTAP deletion by sequencing."""
    def construct(self):
        total = DUR["B12"]

        title = Text("Clinical Trials — PRMT5 Inhibitors", font=SERIF,
                     color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 2.8)

        drug_chip = LabelChip("PRMT5 INHIBITOR", accent=SLATE, size=32)
        drug_chip.move_to(UP * 1.2)

        criteria_label = SerifLabel("Enrollment criteria", TEAL, size=26)
        criteria_label.move_to(UP * 0.0)

        crit_chip = LabelChip("MTAP DELETION BY SEQUENCING", accent=TEAL, size=26)
        crit_chip.next_to(criteria_label, DOWN, buff=0.45)

        # Trial examples (no brand names — just "in trials")
        trial_note = Text("MRTX1719 and AMG-193 in active trials", font=SERIF,
                          color=INK, font_size=21, slant=ITALIC)
        trial_note.move_to(DOWN * 1.5)

        precision_chip = LabelChip("PRECISION ONCOLOGY", accent=TEAL, size=24)
        precision_chip.move_to(DOWN * 2.8)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(drug_chip, scale=0.9), run_time=0.7)
        self.play(FadeIn(criteria_label), run_time=0.5)
        self.play(FadeIn(crit_chip, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(trial_note), FadeIn(precision_chip), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ---------------------------------------------------------------- B13 — trial bars (ILLUSTRATIVE)

class B13_TrialBars(Scene):
    """ILLUSTRATIVE example: 40% vs 5% response rate."""
    def construct(self):
        total = DUR["B13"]

        # Illustrative label
        ill_chip = LabelChip("ILLUSTRATIVE", accent=SLATE, size=22)
        ill_chip.move_to(UP * 3.0)

        full_h = 4.0
        bar_scale = 3.0 / full_h
        base_y = DOWN * 1.8

        deleted_h = full_h * 0.40 * bar_scale  # 40%
        intact_h = full_h * 0.05 * bar_scale   # 5%

        def make_bar(h, color, x_center):
            b = Rectangle(width=1.8, height=max(0.12, h))
            b.set_fill(color, 1).set_stroke(width=0, opacity=0)
            b.move_to(np.array([x_center, 0, 0]) + base_y + UP * max(0.12, h) / 2)
            return b

        deleted_bar = make_bar(deleted_h, CRIMSON, -2.5)
        intact_bar = make_bar(intact_h, TEAL, 2.5)

        # Axis
        laxis = Line(LEFT * 4.0 + base_y, LEFT * 4.0 + UP * 1.8,
                     color=INK, stroke_width=2)
        base_line = Line(LEFT * 4.0 + base_y, RIGHT * 4.5 + base_y,
                         color=INK, stroke_width=2)

        # Pct labels
        del_pct = Text("40%", font=DISPLAY, color=WHITE, font_size=30, weight=BOLD)
        del_pct.move_to(deleted_bar.get_center())
        intact_pct = Text("5%", font=DISPLAY, color=WHITE, font_size=24, weight=BOLD)
        intact_pct.move_to(intact_bar.get_center() + UP * 0.3)

        # Chip labels
        del_chip = LabelChip("MTAP DELETED", accent=CRIMSON, size=22)
        del_chip.next_to(base_y + LEFT * 2.5, DOWN, buff=0.3)
        intact_chip = LabelChip("MTAP INTACT", accent=TEAL, size=22)
        intact_chip.next_to(base_y + RIGHT * 2.5, DOWN, buff=0.3)

        # Axis label (within safe area)
        axis_label = SerifLabel("response rate", INK, size=22)
        axis_label.move_to(LEFT * 5.0 + UP * 0.0).rotate(PI / 2)

        title = Text("PRMT5 inhibitor trial — response by MTAP status",
                     font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 2.0)

        self.play(FadeIn(ill_chip), run_time=0.5)
        self.play(FadeIn(laxis), FadeIn(base_line), FadeIn(title),
                  FadeIn(axis_label), run_time=0.6)
        self.play(FadeIn(deleted_bar, shift=UP * 0.3), FadeIn(del_pct),
                  FadeIn(del_chip), run_time=0.8)
        self.play(FadeIn(intact_bar, shift=UP * 0.2), FadeIn(intact_pct),
                  FadeIn(intact_chip), run_time=0.7)
        self.wait(max(0.3, total - 2.6))


# ---------------------------------------------------------------- B14 — endcard

class B14_Endcard(Scene):
    """RECAP endcard: Q -> A, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B14"]

        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=18)
        eye.move_to(UP * 3.0)

        q_label = Text("Q:", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        q_label.move_to(LEFT * 5.5 + UP * 1.5)
        q_text = Text("Why does the passenger deletion create the better target?",
                      font=SERIF, color=INK, font_size=24, slant=ITALIC)
        q_text.move_to(RIGHT * 0.5 + UP * 1.5)

        a_label = Text("A:", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        a_label.move_to(LEFT * 5.5 + DOWN * 0.3)

        a1 = Text("The passenger deletion pre-throttles PRMT5.", font=SERIF,
                  color=INK, font_size=24, slant=ITALIC)
        a1.move_to(RIGHT * 0.5 + DOWN * 0.1)
        a2 = Text("Only the deleted cell cannot absorb an inhibitor.", font=SERIF,
                  color=INK, font_size=24, slant=ITALIC)
        a2.move_to(RIGHT * 0.5 + DOWN * 0.7)

        # Underline accent
        u = Line(a2.get_corner(DL) + DOWN * 0.13,
                 a2.get_corner(DR) + DOWN * 0.13,
                 color=TEAL, stroke_width=2)

        kicker = Text("Passenger bystander, precision target.", font=SERIF,
                      color=CRIMSON, font_size=22, weight=BOLD)
        kicker.move_to(DOWN * 2.2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(q_label), FadeIn(q_text), run_time=0.8)
        self.play(FadeIn(a_label), FadeIn(a1), run_time=0.7)
        self.play(FadeIn(a2), Create(u), run_time=0.7)
        self.play(FadeIn(kicker, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.3))
