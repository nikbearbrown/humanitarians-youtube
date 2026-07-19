"""vox_scenes.py — Why Losing One Repair Gene Creates a Target the Driver Gene Never Could
(vox-synthetic-lethality, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 and B14 are STILL ai slots — no scenes.

Color law:
  TEAL = HR-intact / normal cell / survives
  CRIMSON = HR-deficient / tumor cell / dies
  GOLD = editor's-pen highlight (fill only, once: the dead corner of B08)
  SLATE = structural neutrality (NHEJ label, section cards)

Exclusions honored: no RAD51 biochemistry, no NHEJ detail, no resistance
mechanisms, no HRD scoring, no BRCA1 vs BRCA2 differences.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 11.0, "B04": 9.0, "B05": 10.0,
    "B06": 9.0, "B07": 10.0, "B08": 10.0, "B09": 9.0,
    "B10": 10.0, "B11": 10.0, "B12": 11.0, "B13": 9.0,
    "B15": 10.0, "B16": 8.0, "B17": 44.0, "B18": 12.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _strand(start, end, color=TEAL, sw=5):
    return Line(start, end, color=color, stroke_width=sw)


def _nick(pos, color=CRIMSON):
    """A small crimson notch representing a single-strand break."""
    t = Triangle().scale(0.08).set_fill(color, 1).set_stroke(width=0, opacity=0)
    t.move_to(pos)
    return t


def _dsb_gap(center, color=CRIMSON, w=0.25):
    """Two short lines with a gap — a double-strand break."""
    top = Line(center + LEFT * w + UP * 0.15, center + UP * 0.15,
               color=color, stroke_width=5)
    bot = Line(center + LEFT * w + DOWN * 0.15, center + DOWN * 0.15,
               color=color, stroke_width=5)
    return VGroup(top, bot)


def _repair_chip(text, accent, size=22):
    return LabelChip(text, accent=accent, size=size)


def _cell_outline(center, side=2.8, color=TEAL):
    r = RoundedRectangle(corner_radius=0.2, width=side, height=side)
    r.set_fill(opacity=0).set_stroke(color, 2.5)
    r.move_to(center)
    return r


def _x_mark(center, color=CRIMSON, size=0.32):
    """A simple X to indicate absence/failure."""
    a = Line(center + UP * size + LEFT * size, center + DOWN * size + RIGHT * size,
             color=color, stroke_width=5)
    b = Line(center + UP * size + RIGHT * size, center + DOWN * size + LEFT * size,
             color=color, stroke_width=5)
    return VGroup(a, b)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        t1 = Text("Why losing one repair gene", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("creates a target the driver gene", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        t3 = Text("never could", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.15).move_to(UP * 0.2)
        u = Line(t3.get_corner(DL) + DOWN * 0.14, t3.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


class B03_PARPBlock(Scene):
    def construct(self):
        total = DUR["B03"]
        # DNA strand with PARP blocked
        strand_y = UP * 1.2
        strand = Line(LEFT * 5.5 + strand_y, RIGHT * 5.5 + strand_y,
                      color=INK, stroke_width=5)
        parp_chip = LabelChip("PARP", accent=INK, size=22)
        parp_chip.move_to(LEFT * 1.5 + strand_y + UP * 0.55)
        block_x = _x_mark(LEFT * 1.5 + strand_y + UP * 0.55, color=CRIMSON, size=0.22)
        blocked_label = SerifLabel("blocked", CRIMSON, size=20)
        blocked_label.next_to(parp_chip, RIGHT, buff=0.3).shift(UP * 0.05)

        # SSB nicks accumulating on strand
        nick_positions = [LEFT * 3.2, LEFT * 0.8, RIGHT * 1.4, RIGHT * 3.6]
        nicks = VGroup(*[_nick(p + strand_y, CRIMSON) for p in nick_positions])

        # DSB label
        dsb_label = LabelChip("DSB forms during replication", accent=CRIMSON, size=20)
        dsb_label.move_to(DOWN * 0.8)

        same_label = SerifLabel("same damage, every cell", INK, size=24)
        same_label.move_to(DOWN * 2.1)

        self.play(Create(strand), FadeIn(parp_chip), run_time=0.8)
        self.play(FadeIn(block_x, scale=0.8), FadeIn(blocked_label), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(n, scale=0.6) for n in nicks],
                               lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(dsb_label, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(same_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.5))


class B04_Question(Scene):
    def construct(self):
        total = DUR["B04"]
        q1 = Text("Blocking PARP should create double-strand breaks", font=SERIF,
                  color=INK, font_size=32)
        q2 = Text("in every cell equally.", font=SERIF, color=INK, font_size=32)
        q3 = Text("Here it kills the cancer cells but spares normal cells.", font=SERIF,
                  color=INK, font_size=32)
        dek = Text("Why does the same drug kill one cell type and not another?",
                   font=DISPLAY, color=CRIMSON, font_size=36, weight="BOLD")
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.12).move_to(UP * 0.9)
        dek.next_to(block, DOWN, buff=0.5)
        u = Line(dek.get_corner(DL) + DOWN * 0.12, dek.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.5)
        self.play(FadeIn(q2), FadeIn(q3), run_time=0.8)
        self.play(FadeIn(dek, shift=UP * 0.1), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 2.3))


class B05_TwoRepairPaths(Scene):
    def construct(self):
        total = DUR["B05"]
        # DSB center point
        dsb = Text("DSB", font=DISPLAY, color=CRIMSON, font_size=32, weight="BOLD")
        dsb.move_to(ORIGIN + UP * 0.2)

        # Two branches
        left_arrow = Arrow(dsb.get_left() + LEFT * 0.1,
                            LEFT * 4.5 + DOWN * 1.2,
                            color=TEAL, buff=0.1, stroke_width=4,
                            max_tip_length_to_length_ratio=0.12)
        right_arrow = Arrow(dsb.get_right() + RIGHT * 0.1,
                             RIGHT * 4.5 + DOWN * 1.2,
                             color=SLATE, buff=0.1, stroke_width=4,
                             max_tip_length_to_length_ratio=0.12)

        # HR branch (left, teal)
        hr_chip = LabelChip("Homologous Recombination", accent=TEAL, size=20)
        hr_chip.move_to(LEFT * 4.5 + DOWN * 1.8)
        hr_detail1 = SerifLabel("high fidelity", TEAL, size=22)
        hr_detail2 = SerifLabel("uses sister chromatid as template", TEAL, size=20)
        hr_detail1.next_to(hr_chip, DOWN, buff=0.25)
        hr_detail2.next_to(hr_detail1, DOWN, buff=0.18)

        # NHEJ branch (right, slate)
        nhej_chip = LabelChip("NHEJ", accent=SLATE, size=20)
        nhej_chip.move_to(RIGHT * 4.5 + DOWN * 1.8)
        nhej_detail1 = SerifLabel("error-prone", SLATE, size=22)
        nhej_detail2 = SerifLabel("no template", SLATE, size=20)
        nhej_detail1.next_to(nhej_chip, DOWN, buff=0.25)
        nhej_detail2.next_to(nhej_detail1, DOWN, buff=0.18)

        self.play(FadeIn(dsb, scale=0.9), run_time=0.6)
        self.play(Create(left_arrow), Create(right_arrow), run_time=0.9)
        self.play(FadeIn(hr_chip), FadeIn(nhej_chip), run_time=0.7)
        self.play(FadeIn(hr_detail1), FadeIn(nhej_detail1), run_time=0.6)
        self.play(FadeIn(hr_detail2), FadeIn(nhej_detail2), run_time=0.6)
        self.wait(max(0.5, total - 3.4))


class B06_NormalCellRepair(Scene):
    def construct(self):
        total = DUR["B06"]
        # Normal cell outline
        cell = _cell_outline(ORIGIN + UP * 0.2, side=3.2, color=TEAL)
        cell_label = SerifLabel("normal cell", TEAL, size=22)
        cell_label.next_to(cell, UP, buff=0.22)

        # BRCA2 chip present
        brca2 = LabelChip("BRCA2", accent=TEAL, size=24)
        brca2.move_to(ORIGIN + UP * 1.0)

        # DSB shown as break, then repaired
        break_left = Line(LEFT * 1.0 + DOWN * 0.1, LEFT * 0.2 + DOWN * 0.1,
                          color=CRIMSON, stroke_width=6)
        break_right = Line(RIGHT * 0.2 + DOWN * 0.1, RIGHT * 1.0 + DOWN * 0.1,
                           color=CRIMSON, stroke_width=6)
        repair_line = Line(LEFT * 1.0 + DOWN * 0.1, RIGHT * 1.0 + DOWN * 0.1,
                           color=TEAL, stroke_width=6)

        result = LabelChip("HR succeeds - cell survives", accent=TEAL, size=22)
        result.next_to(cell, DOWN, buff=0.4)

        self.play(FadeIn(cell), FadeIn(cell_label), run_time=0.7)
        self.play(FadeIn(brca2, scale=0.9), run_time=0.6)
        self.play(FadeIn(break_left), FadeIn(break_right), run_time=0.5)
        self.play(ReplacementTransform(VGroup(break_left, break_right), repair_line),
                  run_time=0.9)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B07_TumorCellFails(Scene):
    def construct(self):
        total = DUR["B07"]
        # Tumor cell outline
        cell = _cell_outline(ORIGIN + UP * 0.2, side=3.2, color=CRIMSON)
        cell_label = SerifLabel("tumor cell (BRCA2 lost)", CRIMSON, size=22)
        cell_label.next_to(cell, UP, buff=0.22)

        # BRCA2 chip with X
        brca2_bg = LabelChip("BRCA2", accent=SLATE, size=24)
        brca2_bg.move_to(ORIGIN + UP * 1.0)
        brca2_x = _x_mark(ORIGIN + UP * 1.0, CRIMSON, size=0.28)

        # DSB break (remains broken)
        break_left = Line(LEFT * 1.0 + DOWN * 0.1, LEFT * 0.25 + DOWN * 0.1,
                          color=CRIMSON, stroke_width=6)
        break_right = Line(RIGHT * 0.25 + DOWN * 0.1, RIGHT * 1.0 + DOWN * 0.1,
                           color=CRIMSON, stroke_width=6)

        # Jagged NHEJ "scar" — use Line segments to avoid VMobject point-shape issues
        scar = VGroup(
            Line(LEFT * 0.25 + DOWN * 0.1, LEFT * 0.06 + UP * 0.06,
                 color=CRIMSON, stroke_width=5),
            Line(LEFT * 0.06 + UP * 0.06, RIGHT * 0.06 + DOWN * 0.16,
                 color=CRIMSON, stroke_width=5),
            Line(RIGHT * 0.06 + DOWN * 0.16, RIGHT * 0.25 + DOWN * 0.1,
                 color=CRIMSON, stroke_width=5),
        )

        nhej_chip = LabelChip("NHEJ fallback", accent=SLATE, size=20)
        nhej_chip.move_to(ORIGIN + DOWN * 0.7)
        result = LabelChip("chromosomal disaster", accent=CRIMSON, size=22)
        result.next_to(cell, DOWN, buff=0.4)

        self.play(FadeIn(cell), FadeIn(cell_label), run_time=0.7)
        self.play(FadeIn(brca2_bg, scale=0.9), run_time=0.4)
        self.play(FadeIn(brca2_x, scale=0.8), run_time=0.5)
        self.play(FadeIn(break_left), FadeIn(break_right), run_time=0.5)
        self.play(FadeIn(nhej_chip, shift=UP * 0.15), run_time=0.5)
        self.play(Create(scar), run_time=0.8)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.9))


class B08_SLGrid(Scene):
    def construct(self):
        total = DUR["B08"]
        # 2x2 grid layout
        # Columns: PARP active | PARP inhibited
        # Rows: BRCA2 intact | BRCA2 lost
        cell_w, cell_h = 3.4, 1.8
        col_xs = [-cell_w / 2 - 0.05, cell_w / 2 + 0.05]
        row_ys = [cell_h / 2 + 0.05, -cell_h / 2 - 0.05]

        def _cell_rect(cx, cy, color, fill_op=0.08, label=None):
            r = Rectangle(width=cell_w, height=cell_h)
            r.set_fill(color, fill_op).set_stroke(color, 2.0)
            r.move_to(np.array([cx, cy, 0]))
            g = VGroup(r)
            if label:
                lbl = Text(label, font=DISPLAY, color=color, font_size=22,
                           weight="BOLD")
                if lbl.width > cell_w * 0.85:
                    lbl.scale_to_fit_width(cell_w * 0.85)
                lbl.move_to(r.get_center())
                g.add(lbl)
            return g

        # Four cells
        c_tl = _cell_rect(col_xs[0], row_ys[0], TEAL, label="ALIVE")
        c_tr = _cell_rect(col_xs[1], row_ys[0], TEAL, label="ALIVE")
        c_bl = _cell_rect(col_xs[0], row_ys[1], TEAL, label="ALIVE")
        # Dead corner — crimson fill, gold highlight
        dead_rect = Rectangle(width=cell_w, height=cell_h)
        dead_rect.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 3.5)
        dead_rect.move_to(np.array([col_xs[1], row_ys[1], 0]))
        dead_label = Text("DEAD", font=DISPLAY, color=CRIMSON, font_size=32,
                          weight="BOLD")
        dead_label.move_to(dead_rect.get_center())
        gold_ring = SurroundingRectangle(dead_rect, buff=0.08)
        gold_ring.set_stroke(GOLD, 4).set_fill(GOLD, 0.0)
        c_br = VGroup(dead_rect, dead_label)

        # Column headers
        hdr_left = SerifLabel("PARP active", INK, size=22)
        hdr_left.move_to(np.array([col_xs[0], row_ys[0] + cell_h / 2 + 0.45, 0]))
        hdr_right = SerifLabel("PARP inhibited", INK, size=22)
        hdr_right.move_to(np.array([col_xs[1], row_ys[0] + cell_h / 2 + 0.45, 0]))

        # Row headers
        row_hdr_top = SerifLabel("BRCA2 intact", TEAL, size=22)
        row_hdr_top.move_to(np.array([col_xs[0] - cell_w / 2 - 0.9, row_ys[0], 0]))
        row_hdr_bot = SerifLabel("BRCA2 lost", CRIMSON, size=22)
        row_hdr_bot.move_to(np.array([col_xs[0] - cell_w / 2 - 0.9, row_ys[1], 0]))

        title = Text("Synthetic Lethality", font=DISPLAY, color=INK,
                     font_size=28, weight="BOLD")
        title.move_to(np.array([0, row_ys[1] - cell_h / 2 - 0.55, 0]))

        self.play(FadeIn(hdr_left), FadeIn(hdr_right),
                  FadeIn(row_hdr_top), FadeIn(row_hdr_bot), run_time=0.7)
        self.play(FadeIn(c_tl, scale=0.95), FadeIn(c_tr, scale=0.95),
                  FadeIn(c_bl, scale=0.95), run_time=0.9)
        self.play(FadeIn(c_br, scale=0.95), run_time=0.6)
        self.play(Create(gold_ring), run_time=0.9)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.6))


class B09_MechanismPivot(Scene):
    def construct(self):
        total = DUR["B09"]
        t1 = Text("The drug does not see cancer.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("It exploits what the cancer lost.", font=SERIF, color=TEAL,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.6))


class B10_PopulationStart(Scene):
    def construct(self):
        total = DUR["B10"]
        # Two isotype grids side by side — simplified to 25 per grid for clarity
        # (illustrative — labeled)
        n = 25  # per grid, represents 1000 (illustrative)
        tumor_grid = IsotypeGrid([n], [CRIMSON], per_row=5, size=0.18, gap=0.10)
        normal_grid = IsotypeGrid([n], [TEAL], per_row=5, size=0.18, gap=0.10)
        tumor_grid.move_to(LEFT * 3.5 + UP * 0.2)
        normal_grid.move_to(RIGHT * 3.5 + UP * 0.2)

        tumor_lbl = LabelChip("tumor (BRCA2 lost)", accent=CRIMSON, size=20)
        tumor_lbl.next_to(tumor_grid, UP, buff=0.28)
        normal_lbl = LabelChip("normal (BRCA2 intact)", accent=TEAL, size=20)
        normal_lbl.next_to(normal_grid, UP, buff=0.28)

        count_t = Text("1,000 cells", font=MONO, color=CRIMSON, font_size=26)
        count_t.next_to(tumor_grid, DOWN, buff=0.2)
        count_n = Text("1,000 cells", font=MONO, color=TEAL, font_size=26)
        count_n.next_to(normal_grid, DOWN, buff=0.2)

        drug_chip = LabelChip("olaparib added", accent=INK, size=22)
        drug_chip.move_to(DOWN * 2.4)
        illustrative = SerifLabel("illustrative numbers", INK, size=18)
        illustrative.move_to(DOWN * 3.1)

        self.play(tumor_grid.count_up(1.2), normal_grid.count_up(1.2))
        self.play(FadeIn(tumor_lbl), FadeIn(normal_lbl),
                  FadeIn(count_t), FadeIn(count_n), run_time=0.7)
        self.play(FadeIn(drug_chip, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(illustrative), run_time=0.4)
        self.wait(max(0.5, total - 2.9))


class B11_NormalSurvive(Scene):
    def construct(self):
        total = DUR["B11"]
        n = 25
        normal_grid = IsotypeGrid([n], [TEAL], per_row=5, size=0.18, gap=0.10)
        normal_grid.move_to(LEFT * 1.5 + UP * 0.3)
        normal_lbl = LabelChip("normal cells", accent=TEAL, size=22)
        normal_lbl.next_to(normal_grid, UP, buff=0.28)

        hr_chip = LabelChip("HR active", accent=TEAL, size=22)
        hr_chip.move_to(RIGHT * 3.8 + UP * 0.3)

        count_final = Text("1,000 / 1,000 survive", font=MONO, color=TEAL, font_size=28)
        count_final.next_to(normal_grid, DOWN, buff=0.35)

        self.play(normal_grid.count_up(1.0))
        self.play(FadeIn(normal_lbl), run_time=0.5)
        self.play(FadeIn(hr_chip, shift=LEFT * 0.3), run_time=0.6)
        self.play(hr_chip.animate.scale(1.05), run_time=0.3)
        self.play(FadeIn(count_final, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B12_TumorDie(Scene):
    def construct(self):
        total = DUR["B12"]
        n = 25
        tumor_grid = IsotypeGrid([n], [CRIMSON], per_row=5, size=0.18, gap=0.10)
        tumor_grid.move_to(LEFT * 1.5 + UP * 0.3)
        tumor_lbl = LabelChip("tumor cells", accent=CRIMSON, size=22)
        tumor_lbl.next_to(tumor_grid, UP, buff=0.28)

        fail_chip = LabelChip("NHEJ misfires", accent=CRIMSON, size=22)
        fail_chip.move_to(RIGHT * 3.8 + UP * 0.3)

        count_final = Text("approx 0 / 1,000 survive", font=MONO, color=CRIMSON,
                           font_size=28)
        count_final.next_to(tumor_grid, DOWN, buff=0.35)

        self.play(tumor_grid.count_up(1.0))
        self.play(FadeIn(tumor_lbl), run_time=0.5)
        self.play(FadeIn(fail_chip, shift=LEFT * 0.3), run_time=0.6)
        # Fade out cells progressively
        marks = tumor_grid.marks
        for i in range(0, len(marks), 4):
            batch = VGroup(*marks[i:i+4])
            self.play(FadeOut(batch), run_time=0.22)
        self.play(FadeIn(count_final, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.0 - 0.5 - 0.6 - 7 * 0.22 - 0.6))


class B13_FinalCount(Scene):
    def construct(self):
        total = DUR["B13"]
        # Left panel — tumor ~0
        left_panel = Rectangle(width=4.8, height=3.8)
        left_panel.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 2.0)
        left_panel.move_to(LEFT * 3.0 + UP * 0.1)
        zero = Text("~0", font=MONO, color=CRIMSON, font_size=96, weight="BOLD")
        zero.move_to(left_panel.get_center())
        tumor_lbl = SerifLabel("tumor cells", CRIMSON, size=22)
        tumor_lbl.next_to(left_panel, UP, buff=0.25)

        # Right panel — normal ~1000
        right_panel = Rectangle(width=4.8, height=3.8)
        right_panel.set_fill(TEAL, 0.06).set_stroke(TEAL, 2.0)
        right_panel.move_to(RIGHT * 3.0 + UP * 0.1)
        thousand = Text("~1,000", font=MONO, color=TEAL, font_size=72, weight="BOLD")
        thousand.move_to(right_panel.get_center())
        normal_lbl = SerifLabel("normal cells", TEAL, size=22)
        normal_lbl.next_to(right_panel, UP, buff=0.25)

        same_label = SerifLabel("same drug - same damage", INK, size=24)
        same_label.move_to(DOWN * 2.5)

        self.play(FadeIn(left_panel), FadeIn(right_panel),
                  FadeIn(tumor_lbl), FadeIn(normal_lbl), run_time=0.8)
        self.play(FadeIn(zero, scale=0.85), FadeIn(thousand, scale=0.85), run_time=0.9)
        self.play(FadeIn(same_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B15_Implication(Scene):
    def construct(self):
        total = DUR["B15"]
        # Left: BRCA2 loss = vulnerability
        left_chip = LabelChip("BRCA2 loss in tumor", accent=CRIMSON, size=22)
        left_chip.move_to(LEFT * 4.2 + UP * 0.3)
        vuln_label = SerifLabel("repair vulnerability", CRIMSON, size=20)
        vuln_label.next_to(left_chip, DOWN, buff=0.25)

        # Arrow to result
        arr = Arrow(left_chip.get_right() + RIGHT * 0.15,
                    RIGHT * 0.8 + UP * 0.3,
                    color=INK, buff=0.1, stroke_width=3,
                    max_tip_length_to_length_ratio=0.15)

        # Right: olaparib + synthetic lethality
        result_chip = LabelChip("olaparib + BRCA2 loss", accent=TEAL, size=22)
        result_chip.move_to(RIGHT * 3.4 + UP * 0.3)
        sl_label = SerifLabel("synthetic lethality", TEAL, size=22)
        sl_label.next_to(result_chip, DOWN, buff=0.25)

        # Cancer type chips
        breast = LabelChip("BRCA-mutant breast", accent=SLATE, size=19)
        ovarian = LabelChip("ovarian", accent=SLATE, size=19)
        prostate = LabelChip("prostate", accent=SLATE, size=19)
        cancers = VGroup(breast, ovarian, prostate).arrange(RIGHT, buff=0.3)
        cancers.move_to(DOWN * 2.0)
        cancers_label = SerifLabel("standard of care", INK, size=22)
        cancers_label.next_to(cancers, UP, buff=0.25)

        self.play(FadeIn(left_chip, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(vuln_label), run_time=0.4)
        self.play(Create(arr), run_time=0.6)
        self.play(FadeIn(result_chip, shift=LEFT * 0.3), run_time=0.6)
        self.play(FadeIn(sl_label), run_time=0.4)
        self.play(FadeIn(cancers_label), FadeIn(cancers, lag_ratio=0.2),
                  run_time=0.9)
        self.wait(max(0.5, total - 3.5))


class B16_GeneralizationCard(Scene):
    def construct(self):
        total = DUR["B16"]
        t1 = Text("Synthetic lethality:", font=SERIF, color=INK, font_size=44,
                  weight="BOLD")
        t2 = Text("map the repair defect,", font=SERIF, color=INK, font_size=44,
                  weight="BOLD")
        t3 = Text("find the target.", font=SERIF, color=TEAL, font_size=44,
                  weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.18).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.14, t3.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.5)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.8))


class B17_ExampleWalkthrough(Scene):
    def construct(self):
        total = DUR["B17"]
        n = 20  # illustrative per grid (represents 1000)

        # Phase 1 — both grids, drug added
        tumor_grid = IsotypeGrid([n], [CRIMSON], per_row=4, size=0.20, gap=0.12)
        normal_grid = IsotypeGrid([n], [TEAL], per_row=4, size=0.20, gap=0.12)
        tumor_grid.move_to(LEFT * 4.0 + UP * 0.5)
        normal_grid.move_to(RIGHT * 4.0 + UP * 0.5)

        tlbl = LabelChip("1,000 tumor cells", accent=CRIMSON, size=20)
        tlbl.next_to(tumor_grid, UP, buff=0.25)
        nlbl = LabelChip("1,000 normal cells", accent=TEAL, size=20)
        nlbl.next_to(normal_grid, UP, buff=0.25)

        drug = LabelChip("olaparib", accent=INK, size=22)
        drug.move_to(DOWN * 1.2)
        drug_note = SerifLabel("identical SSB -> DSB in both populations", INK, size=20)
        drug_note.next_to(drug, DOWN, buff=0.2)

        illus = SerifLabel("illustrative numbers", INK, size=18)
        illus.move_to(DOWN * 2.5)

        self.play(tumor_grid.count_up(1.2), normal_grid.count_up(1.2))
        self.play(FadeIn(tlbl), FadeIn(nlbl), run_time=0.5)
        self.play(FadeIn(drug, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(drug_note), run_time=0.4)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(4.0)

        # Phase 2 — normal cells repair
        hr_chip = LabelChip("HR active", accent=TEAL, size=20)
        hr_chip.next_to(normal_grid, DOWN, buff=0.35)
        survive_label = Text("1,000 survive", font=MONO, color=TEAL, font_size=24)
        survive_label.next_to(hr_chip, DOWN, buff=0.2)

        self.play(FadeOut(drug), FadeOut(drug_note), FadeOut(illus), run_time=0.4)
        self.play(FadeIn(hr_chip, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(survive_label), run_time=0.4)
        self.wait(4.0)

        # Phase 3 — tumor cells die
        fail_chip = LabelChip("NHEJ misfires", accent=CRIMSON, size=20)
        fail_chip.next_to(tumor_grid, DOWN, buff=0.35)
        marks = tumor_grid.marks
        self.play(FadeIn(fail_chip, shift=UP * 0.1), run_time=0.5)
        for i in range(0, len(marks), 4):
            batch = VGroup(*marks[i:min(i+4, len(marks))])
            self.play(FadeOut(batch), run_time=0.2)

        zero_label = Text("~0 survive", font=MONO, color=CRIMSON, font_size=24)
        zero_label.next_to(fail_chip, DOWN, buff=0.2)
        self.play(FadeIn(zero_label), run_time=0.5)
        self.wait(4.0)

        # Final — conclusion label
        same = SerifLabel("same drug - same damage - one missing gene", INK, size=22)
        same.move_to(DOWN * 2.8)
        self.play(FadeIn(same, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 1.2 - 1.2 - 0.5 - 0.4 - 0.3 - 4.0 - 0.4
                      - 0.5 - 0.4 - 4.0 - 0.5 - 5 * 0.2 - 0.5 - 4.0 - 0.8))


class B18_End(Scene):
    def construct(self):
        total = DUR["B18"]
        q_line = Text("Blocking PARP creates double-strand breaks in every cell equally.",
                      font=SERIF, color=INK, font_size=30)
        a_line = Text("It kills cancer cells, spares normal cells, because the cancer",
                      font=SERIF, color=INK, font_size=30)
        a_line2 = Text("lost the repair gene that could have saved it.",
                       font=SERIF, color=INK, font_size=30)
        sl_line = Text("BRCA2 loss alone: survivable.  PARP inhibition alone: survivable.",
                       font=SERIF, color=INK, font_size=26)
        punch = Text("Together: lethal — only in the cell that has both.",
                     font=DISPLAY, color=CRIMSON, font_size=32, weight="BOLD")
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                     font_size=20, weight="MEDIUM")
        block = VGroup(q_line, a_line, a_line2, sl_line, punch).arrange(DOWN, buff=0.22)
        block.move_to(UP * 0.3)
        u = Line(punch.get_corner(DL) + DOWN * 0.12,
                 punch.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        topic.next_to(block, DOWN, buff=0.45)

        self.play(FadeIn(q_line), run_time=0.7)
        self.play(FadeIn(a_line), FadeIn(a_line2), run_time=0.8)
        self.play(FadeIn(sl_line), run_time=0.6)
        self.play(FadeIn(punch, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(topic), run_time=0.5)
        self.wait(max(0.5, total - 3.5))
