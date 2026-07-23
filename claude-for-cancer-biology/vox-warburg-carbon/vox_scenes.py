"""vox_scenes.py — Why Cancer Cells Run an Inefficient Engine on Purpose
(vox-warburg-carbon, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'. B05 and B10 are
STILL (ai) slots — no scene class here; vox_run compiles them as slates.

Color law: TEAL #1F6F5C = carbon that becomes structure (kept/built);
CRIMSON #BF3339 = carbon wasted or the naive expectation (lost/excreted);
GOLD = editor's-pen highlighter fill only, never text.
Two accents max — TEAL + CRIMSON — never swapped mid-film.

Exclusions honored: NO HIF-1alpha/VHL, NO TCA cycle chemistry, NO enzyme
kinetics, NO isotope tracing, NO Warburg history beyond one sentence (B08).
"""
import json
import os

# ------------- beat-sheet duration table (populated after audio lock) ----------
_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}

import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np


# ------------------------------------------------------------------ B01 Title

class B01_Title(Scene):
    """COLD OPEN — title card with TEAL eyebrow 'CANCER BIOLOGY'."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why Cancer Cells Run", font=DISPLAY, color=INK,
                  font_size=48, weight="BOLD")
        t2 = Text("an Inefficient Engine", font=DISPLAY, color=INK,
                  font_size=48, weight="BOLD")
        t3 = Text("on Purpose", font=DISPLAY, color=INK,
                  font_size=48, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.15).move_to(UP * 0.2)
        u = Line(t3.get_corner(DL) + DOWN * 0.14, t3.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2.0, color=TEAL)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.3)
        self.wait(max(0.5, total - 1.9))


# --------------------------------------------------------------- B02 Two bars

class B02_TwoBar(Scene):
    """COLD OPEN — 2 ATP vs 30 ATP bar chart. The puzzle established."""
    def construct(self):
        total = DUR["B02"]
        BAR_W = 1.6
        # CRIMSON bar — 2 ATP (short)
        bar_h_lo = 0.5
        bar_lo = Rectangle(width=BAR_W, height=bar_h_lo)
        bar_lo.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        bar_lo.move_to(LEFT * 2.4 + DOWN * 1.5 + UP * bar_h_lo / 2)

        # TEAL bar — 30 ATP (tall), proportional: 30/2 * bar_h_lo = 7.5 — clamp to 5.5
        bar_h_hi = min(5.5, bar_h_lo * 15)
        bar_hi = Rectangle(width=BAR_W, height=bar_h_hi)
        bar_hi.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        bar_hi.move_to(RIGHT * 2.4 + DOWN * 1.5 + UP * bar_h_hi / 2)

        # baseline
        baseline = Line(LEFT * 4.5 + DOWN * 1.5, RIGHT * 4.5 + DOWN * 1.5,
                        stroke_width=1.5, color=INK)

        # labels — INK on colored bars for contrast (white fails W6 AST check)
        lbl_lo = Text("2 ATP", font=DISPLAY, color=INK, font_size=30, weight="BOLD")
        lbl_lo.move_to(bar_lo.get_center())
        lbl_hi = Text("30 ATP", font=DISPLAY, color=INK, font_size=30, weight="BOLD")
        lbl_hi.move_to(bar_hi.get_center())

        cap_lo = SerifLabel("glycolysis to lactate", CRIMSON, size=22)
        cap_lo.next_to(bar_lo, DOWN, buff=0.18)
        cap_hi = SerifLabel("complete oxidation", TEAL, size=22)
        cap_hi.next_to(bar_hi, DOWN, buff=0.18)

        self.play(FadeIn(baseline), run_time=0.4)
        # Grow bars from baseline (real shape motion)
        bar_lo_start = bar_lo.copy().scale(np.array([1, 0.01, 1]))
        bar_lo_start.move_to(bar_lo.get_bottom() + UP * 0.01)
        bar_hi_start = bar_hi.copy().scale(np.array([1, 0.01, 1]))
        bar_hi_start.move_to(bar_hi.get_bottom() + UP * 0.01)
        self.add(bar_lo_start, bar_hi_start)
        self.play(
            Transform(bar_lo_start, bar_lo),
            Transform(bar_hi_start, bar_hi),
            run_time=1.2
        )
        self.play(FadeIn(lbl_lo), FadeIn(lbl_hi), run_time=0.6)
        self.play(FadeIn(cap_lo), FadeIn(cap_hi), run_time=0.7)
        self.wait(max(0.5, total - 2.9))


# -------------------------------------------------------------- B03 Question

class B03_Question(Scene):
    """THE QUESTION — gap formula on screen."""
    def construct(self):
        total = DUR["B03"]
        q1 = Text("A cancer cell should maximize ATP from glucose.", font=SERIF,
                  color=INK, font_size=34, weight="BOLD")
        q2 = Text("Here is a tumor extracting only two —", font=SERIF,
                  color=INK, font_size=34)
        q3 = Text("and excreting the rest as lactate.", font=SERIF,
                  color=INK, font_size=34)
        q4 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=52, weight="BOLD")
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.18).move_to(UP * 0.6)
        q4.next_to(block, DOWN, buff=0.45)
        chip = LabelChip("THE QUESTION", accent=TEAL, size=20)
        chip.next_to(block, UP, buff=0.5)
        self.play(FadeIn(chip, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(q1), run_time=0.7)
        self.play(FadeIn(q2), FadeIn(q3), run_time=0.8)
        self.play(FadeIn(q4, scale=0.85), run_time=0.7)
        self.wait(max(0.5, total - 2.7))


# --------------------------------------------------------- B04 Quiescent cell

class B04_QuiescentCell(Scene):
    """THE PROBLEM — quiescent cell: glucose flows entirely to CO2, 30 ATP."""
    def construct(self):
        total = DUR["B04"]
        # glucose node
        g_box = Rectangle(width=1.6, height=0.8)
        g_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        g_box.move_to(LEFT * 5.0 + UP * 0.3)
        g_lbl = Text("Glucose", font=SERIF, color=INK, font_size=28)
        g_lbl.move_to(g_box)

        # arrow pointing right
        arr = Arrow(LEFT * 3.9 + UP * 0.3, RIGHT * 1.4 + UP * 0.3,
                    buff=0.1, color=INK, stroke_width=3)

        # pathway label
        path_lbl = SerifLabel("complete oxidation", INK, size=24)
        path_lbl.move_to(ORIGIN + UP * 0.9)

        # CO2 cloud (circle group)
        co2_box = Rectangle(width=2.0, height=0.8)
        co2_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        co2_box.move_to(RIGHT * 3.5 + UP * 0.3)
        co2_lbl = Text("CO2", font=DISPLAY, color=INK, font_size=28, weight="BOLD")
        co2_lbl.move_to(co2_box)

        # ATP chip
        atp = LabelChip("30 ATP", accent=TEAL, size=26)
        atp.next_to(co2_box, DOWN, buff=0.35)

        caption = SerifLabel("maximum yield · all carbon discarded", INK, size=22)
        caption.move_to(DOWN * 2.0)

        self.play(FadeIn(g_box), FadeIn(g_lbl), run_time=0.6)
        self.play(Create(arr), FadeIn(path_lbl), run_time=0.9)
        self.play(FadeIn(co2_box), FadeIn(co2_lbl), run_time=0.7)
        self.play(FadeIn(atp, scale=0.9), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(max(0.5, total - 3.4))


# ------------------------------------------------------------- B06 CarbonLoss

class B06_CarbonLoss(Scene):
    """THE MECHANISM — complete oxidation = all 6 carbons lost as CO2."""
    def construct(self):
        total = DUR["B06"]
        SQ = 0.32
        GAP = 0.10
        # 6 carbon squares — start bunched on the left
        squares = VGroup(*[Square(SQ).set_fill(INK, 0.85).set_stroke(width=0, opacity=0)
                           for _ in range(6)])
        squares.arrange(RIGHT, buff=GAP).move_to(LEFT * 4.0 + UP * 0.3)

        g_lbl = Text("6 carbons (glucose)", font=SERIF, color=INK, font_size=26)
        g_lbl.next_to(squares, UP, buff=0.25)

        arr = Arrow(LEFT * 2.2 + UP * 0.3, RIGHT * 0.5 + UP * 0.3,
                    buff=0.1, color=CRIMSON, stroke_width=3)
        arr_lbl = SerifLabel("complete oxidation", CRIMSON, size=22)
        arr_lbl.move_to(ORIGIN + UP * 0.9)

        # CO2 destination — CRIMSON, carbon lost
        co2_grp = VGroup(*[Square(SQ).set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
                           for _ in range(6)])
        co2_grp.arrange(RIGHT, buff=GAP).move_to(RIGHT * 3.8 + UP * 0.3)
        co2_lbl = Text("CO2", font=DISPLAY, color=CRIMSON, font_size=36, weight="BOLD")
        co2_lbl.next_to(co2_grp, UP, buff=0.22)

        nothing = SerifLabel("nothing left to build with", CRIMSON, size=28)
        nothing.move_to(DOWN * 1.7)

        self.play(FadeIn(squares), FadeIn(g_lbl), run_time=0.7)
        self.play(Create(arr), FadeIn(arr_lbl), run_time=0.8)
        # squares move to become CO2 squares (real shape motion — Transform)
        self.play(
            ReplacementTransform(squares, co2_grp),
            FadeIn(co2_lbl),
            run_time=1.1
        )
        self.play(FadeIn(nothing, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.3))


# -------------------------------------------------------------- B07 CarbonSplit

class B07_CarbonSplit(Scene):
    """THE MECHANISM — the SPLIT: glucose carbon fans into four destinations."""
    def construct(self):
        total = DUR["B07"]
        SQ = 0.26
        GAP = 0.08

        # Glucose source on the left
        g_box = Rectangle(width=1.5, height=0.7)
        g_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        g_box.move_to(LEFT * 5.5 + UP * 0.0)
        g_lbl = Text("Glucose", font=SERIF, color=INK, font_size=26)
        g_lbl.move_to(g_box)

        # Glycolytic trunk — horizontal bar
        trunk = Rectangle(width=2.2, height=0.28)
        trunk.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
        trunk.move_to(LEFT * 3.4 + UP * 0.0)

        # Branch endpoints (4 destinations)
        dest_y = [1.9, 0.7, -0.6, -1.9]
        dest_x = 1.8
        dest_labels = [
            ("nucleotides (DNA)", TEAL),
            ("serine / one-carbon", TEAL),
            ("membrane lipids", TEAL),
            ("lactate excreted", CRIMSON),
        ]

        branch_origin_x = -2.2  # right edge of trunk

        branches = VGroup()
        chips = VGroup()
        for y, (lbl_txt, col) in zip(dest_y, dest_labels):
            # branch line from trunk to destination
            bline = Line(
                np.array([branch_origin_x, 0.0, 0]),
                np.array([dest_x - 0.8, y, 0]),
                stroke_width=3, color=col
            )
            # destination square cluster
            dsq = VGroup(*[Square(SQ).set_fill(col, 0.85).set_stroke(width=0, opacity=0)
                           for _ in range(2)])
            dsq.arrange(RIGHT, buff=GAP).move_to(np.array([dest_x, y, 0]))
            chip = LabelChip(lbl_txt, accent=col, size=18)
            chip.next_to(dsq, RIGHT, buff=0.18)
            branches.add(VGroup(bline, dsq))
            chips.add(chip)

        self.play(FadeIn(g_box), FadeIn(g_lbl), run_time=0.6)
        self.play(GrowFromEdge(trunk, LEFT), run_time=0.7)
        # fan out branches in succession
        for br, ch in zip(branches, chips):
            self.play(Create(br[0]), FadeIn(br[1]), FadeIn(ch), run_time=0.55)
        self.wait(max(0.5, total - 0.6 - 0.7 - 4 * 0.55))


# --------------------------------------------------------------- B08 Pivot card

class B08_Pivot(Scene):
    """THE MECHANISM — pivot section card: the lactate is not a failure."""
    def construct(self):
        total = DUR["B08"]
        t1 = Text("The lactate is not a failure.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("It is a choice.", font=SERIF, color=TEAL,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2.0, color=TEAL)
        att = SerifLabel("Warburg, 1920s — the observation was right; the explanation was not",
                         INK, size=20)
        att.next_to(block, DOWN, buff=0.6)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(att, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


# --------------------------------------------------------------- B09 TwoStreams

class B09_TwoStreams(Scene):
    """THE MECHANISM — two parallel metabolic streams."""
    def construct(self):
        total = DUR["B09"]
        # Top track: glucose -> biosynthetic branches
        top_y = 1.2
        bot_y = -1.2

        top_src = Rectangle(width=1.6, height=0.65)
        top_src.set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        top_src.move_to(LEFT * 5.0 + UP * top_y)
        top_src_lbl = Text("Glucose", font=SERIF, color=INK, font_size=24)
        top_src_lbl.move_to(top_src)

        top_arr = Arrow(LEFT * 4.0 + UP * top_y, RIGHT * 0.0 + UP * top_y,
                        buff=0.1, color=TEAL, stroke_width=3)
        top_mid = LabelChip("carbon for building", accent=TEAL, size=20)
        top_mid.move_to(LEFT * 2.0 + UP * (top_y + 0.55))

        top_dest = Rectangle(width=2.0, height=0.65)
        top_dest.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        top_dest.move_to(RIGHT * 1.5 + UP * top_y)
        top_dest_lbl = Text("biomass", font=DISPLAY, color=INK, font_size=22, weight="BOLD")
        top_dest_lbl.move_to(top_dest)

        # Bottom track: other fuels -> mitochondria -> ATP
        bot_src = Rectangle(width=2.0, height=0.65)
        bot_src.set_fill(SLATE, 0.12).set_stroke(SLATE, 2)
        bot_src.move_to(LEFT * 4.7 + UP * bot_y)
        bot_src_lbl = Text("glutamine · fats", font=SERIF, color=INK, font_size=22)
        bot_src_lbl.move_to(bot_src)

        bot_arr = Arrow(LEFT * 3.5 + UP * bot_y, RIGHT * 0.0 + UP * bot_y,
                        buff=0.1, color=TEAL, stroke_width=3)
        bot_mid = LabelChip("energy from other fuels", accent=TEAL, size=20)
        bot_mid.move_to(LEFT * 1.7 + UP * (bot_y - 0.55))

        bot_dest = Rectangle(width=1.8, height=0.65)
        bot_dest.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        bot_dest.move_to(RIGHT * 1.5 + UP * bot_y)
        bot_dest_lbl = Text("ATP", font=DISPLAY, color=INK, font_size=22, weight="BOLD")
        bot_dest_lbl.move_to(bot_dest)

        caption = SerifLabel("parallel streams · neither replaces the other", INK, size=22)
        caption.move_to(DOWN * 2.5)

        self.play(
            FadeIn(top_src), FadeIn(top_src_lbl),
            FadeIn(bot_src), FadeIn(bot_src_lbl),
            run_time=0.8
        )
        self.play(
            Create(top_arr), FadeIn(top_mid),
            Create(bot_arr), FadeIn(bot_mid),
            run_time=1.0
        )
        self.play(
            FadeIn(top_dest), FadeIn(top_dest_lbl),
            FadeIn(bot_dest), FadeIn(bot_dest_lbl),
            run_time=0.8
        )
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(max(0.5, total - 3.2))


# -------------------------------------------------------------- B11 PETSignal

class B11_PETSignal(Scene):
    """THE IMPLICATION — FDG trap mechanism: glucose in, building + lactate out."""
    def construct(self):
        total = DUR["B11"]
        # Cell box
        cell = Rectangle(width=5.0, height=3.5)
        cell.set_fill(TEAL, 0.06).set_stroke(TEAL, 2.5)
        cell.move_to(LEFT * 1.2 + UP * 0.2)
        cell_lbl = Text("cancer cell", font=SERIF, color=TEAL, font_size=22)
        cell_lbl.next_to(cell, UP, buff=0.15)

        # Glucose entering (arrow from left)
        glc_arr = Arrow(LEFT * 6.0 + UP * 0.5, LEFT * 3.7 + UP * 0.5,
                        buff=0.05, color=INK, stroke_width=3)
        glc_lbl = Text("glucose", font=SERIF, color=INK, font_size=22)
        glc_lbl.next_to(glc_arr, UP, buff=0.1)

        # Inside the cell: building branch (up-right) and lactate branch (down)
        build_arr = Arrow(LEFT * 2.2 + UP * 0.5, LEFT * 0.5 + UP * 1.6,
                          buff=0.05, color=TEAL, stroke_width=2.5)
        build_chip = LabelChip("building", accent=TEAL, size=20)
        build_chip.move_to(LEFT * 0.2 + UP * 1.9)

        lac_arr = Arrow(LEFT * 2.2 + UP * 0.2, LEFT * 0.5 + DOWN * 0.8,
                        buff=0.05, color=CRIMSON, stroke_width=2.5)
        lac_lbl = SerifLabel("lactate", CRIMSON, size=22)
        lac_lbl.move_to(LEFT * 0.2 + DOWN * 1.1)

        # FDG trapped dot
        fdg_dot = Dot(radius=0.28, color=TEAL)
        fdg_dot.move_to(RIGHT * 0.5 + UP * 0.3)
        fdg_dot.set_opacity(0.9)
        fdg_lbl = SerifLabel("FDG trapped", TEAL, size=20)
        fdg_lbl.next_to(fdg_dot, DOWN, buff=0.14)

        # Scanner icon (concentric arcs) on the right
        scanner_arcs = VGroup()
        for r in [0.35, 0.6, 0.85]:
            arc = Arc(radius=r, start_angle=-PI / 4, angle=PI / 2,
                      color=TEAL, stroke_width=2.5 - r * 0.5)
            arc.move_to(RIGHT * 4.5 + UP * 0.3)
            scanner_arcs.add(arc)
        scan_lbl = LabelChip("PET signal", accent=TEAL, size=20)
        scan_lbl.next_to(scanner_arcs, DOWN, buff=0.18)

        self.play(FadeIn(cell), FadeIn(cell_lbl), run_time=0.6)
        self.play(Create(glc_arr), FadeIn(glc_lbl), run_time=0.7)
        self.play(Create(build_arr), FadeIn(build_chip), run_time=0.6)
        self.play(Create(lac_arr), FadeIn(lac_lbl), run_time=0.6)
        self.play(FadeIn(fdg_dot, scale=0.5), FadeIn(fdg_lbl), run_time=0.7)
        self.play(
            Create(scanner_arcs[0]),
            Create(scanner_arcs[1]),
            Create(scanner_arcs[2]),
            FadeIn(scan_lbl),
            run_time=0.9
        )
        self.wait(max(0.5, total - 4.1))


# ------------------------------------------------------------ B12 ExampleTrace

class B12_ExampleTrace(Scene):
    """THE EXAMPLE — one glucose traced into four destinations (illustrative)."""
    def construct(self):
        total = DUR["B12"]
        SQ = 0.28
        GAP = 0.08

        # 6 carbon squares entering from left
        entry = VGroup(*[Square(SQ).set_fill(INK, 0.80).set_stroke(width=0, opacity=0)
                         for _ in range(6)])
        entry.arrange(RIGHT, buff=GAP).move_to(LEFT * 5.0 + UP * 0.0)
        entry_lbl = Text("1 glucose · 6 carbons", font=SERIF, color=INK, font_size=24)
        entry_lbl.next_to(entry, UP, buff=0.22)

        # Trunk arrow
        trunk_arr = Arrow(LEFT * 3.8 + UP * 0.0, LEFT * 2.4 + UP * 0.0,
                          buff=0.05, color=INK, stroke_width=2)

        # Destinations (illustrative)
        dests = [
            (2, "2 to ribose (DNA)", TEAL,  1.9),
            (2, "2 to serine (one-carbon)", TEAL, 0.6),
            (2, "2 to acetyl-CoA (membranes)", TEAL, -0.7),
            (2, "rest exits as lactate", CRIMSON, -1.9),
        ]

        dest_origin_x = -1.8
        dest_label_x = 1.4

        dest_groups = VGroup()
        for n, lbl_txt, col, y in dests:
            bline = Line(np.array([dest_origin_x, 0.0, 0]),
                         np.array([dest_label_x - 1.2, y, 0]),
                         stroke_width=2.5, color=col)
            dsq = VGroup(*[Square(SQ).set_fill(col, 0.85).set_stroke(width=0, opacity=0)
                           for _ in range(n)])
            dsq.arrange(RIGHT, buff=GAP).move_to(np.array([dest_label_x, y, 0]))
            chip = LabelChip(lbl_txt, accent=col, size=17)
            chip.next_to(dsq, RIGHT, buff=0.15)
            dest_groups.add(VGroup(bline, dsq, chip))

        # illustrative chip — kept well inside safe area (±6.3/±3.4)
        illus_chip = LabelChip("illustrative", accent=SLATE, size=16)
        illus_chip.move_to(RIGHT * 4.5 + DOWN * 2.8)

        self.play(FadeIn(entry), FadeIn(entry_lbl), run_time=0.7)
        self.play(Create(trunk_arr), run_time=0.5)
        for dg in dest_groups:
            self.play(Create(dg[0]), FadeIn(dg[1]), FadeIn(dg[2]), run_time=0.6)
        self.play(FadeIn(illus_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.5, total - 0.7 - 0.5 - 4 * 0.6 - 0.5))


# --------------------------------------------------------- B13 CompareOutcomes

class B13_CompareOutcomes(Scene):
    """THE EXAMPLE — side-by-side: carbon allocation vs complete oxidation."""
    def construct(self):
        total = DUR["B13"]
        SQ = 0.24
        GAP = 0.07

        # --- Left panel: dividing cell (carbon allocation) ---
        left_x = -3.4
        lp_box = Rectangle(width=5.2, height=5.5)
        lp_box.set_fill(TEAL, 0.05).set_stroke(TEAL, 2)
        lp_box.move_to(LEFT * 3.4 + DOWN * 0.15)
        lp_title = LabelChip("dividing cell", accent=TEAL, size=20)
        lp_title.next_to(lp_box, UP, buff=0.15)

        # 6 entry squares
        entry_l = VGroup(*[Square(SQ).set_fill(INK, 0.7).set_stroke(width=0, opacity=0)
                           for _ in range(6)])
        entry_l.arrange(RIGHT, buff=GAP).move_to(LEFT * 4.8 + UP * 1.6)

        # branch lines + outcome squares
        branch_data_l = [
            ("DNA", TEAL, 1.0),
            ("lipids", TEAL, -0.1),
            ("amino acids", TEAL, -1.2),
        ]
        branch_grp_l = VGroup()
        for lbl, col, y in branch_data_l:
            bl = Line(np.array([-3.9, 1.6, 0]), np.array([-2.2, y, 0]),
                      stroke_width=2, color=col)
            bsq = VGroup(*[Square(SQ).set_fill(col, 0.85).set_stroke(width=0, opacity=0)
                           for _ in range(2)])
            bsq.arrange(RIGHT, buff=GAP).move_to(np.array([-1.9, y, 0]))
            bc = SerifLabel(lbl, col, size=18)
            bc.next_to(bsq, RIGHT, buff=0.12)
            branch_grp_l.add(VGroup(bl, bsq, bc))

        lat_l = SerifLabel("lactate out", CRIMSON, size=18)
        lat_l.move_to(LEFT * 2.5 + DOWN * 2.1)

        outcome_l = LabelChip("cell doubles", accent=TEAL, size=20)
        outcome_l.move_to(LEFT * 3.4 + DOWN * 2.9)

        # --- Right panel: complete oxidation ---
        rp_box = Rectangle(width=5.2, height=5.5)
        rp_box.set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 2)
        rp_box.move_to(RIGHT * 3.4 + DOWN * 0.15)
        rp_title = LabelChip("complete oxidation", accent=CRIMSON, size=20)
        rp_title.next_to(rp_box, UP, buff=0.15)

        entry_r = VGroup(*[Square(SQ).set_fill(INK, 0.7).set_stroke(width=0, opacity=0)
                           for _ in range(6)])
        entry_r.arrange(RIGHT, buff=GAP).move_to(RIGHT * 1.8 + UP * 1.6)

        arr_r = Arrow(RIGHT * 2.8 + UP * 1.6, RIGHT * 4.0 + UP * 0.4,
                      buff=0.05, color=CRIMSON, stroke_width=2.5)

        co2_sq = VGroup(*[Square(SQ).set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
                          for _ in range(6)])
        co2_sq.arrange(RIGHT, buff=GAP).move_to(RIGHT * 4.5 + UP * 0.0)

        co2_lbl = Text("CO2", font=DISPLAY, color=CRIMSON, font_size=28, weight="BOLD")
        co2_lbl.next_to(co2_sq, UP, buff=0.2)

        atp_lbl = LabelChip("30 ATP", accent=TEAL, size=20)
        atp_lbl.move_to(RIGHT * 4.5 + DOWN * 0.8)

        nothing_r = SerifLabel("nothing to build with", CRIMSON, size=20)
        nothing_r.move_to(RIGHT * 3.4 + DOWN * 2.1)

        outcome_r = LabelChip("maintains · does not divide", accent=CRIMSON, size=18)
        outcome_r.move_to(RIGHT * 3.4 + DOWN * 2.9)

        # Animate
        self.play(
            FadeIn(lp_box), FadeIn(lp_title),
            FadeIn(rp_box), FadeIn(rp_title),
            run_time=0.8
        )
        self.play(FadeIn(entry_l), FadeIn(entry_r), run_time=0.7)
        for bg in branch_grp_l:
            self.play(Create(bg[0]), FadeIn(bg[1]), FadeIn(bg[2]), run_time=0.45)
        self.play(FadeIn(lat_l), run_time=0.4)
        self.play(Create(arr_r), ReplacementTransform(entry_r.copy(), co2_sq),
                  FadeIn(co2_lbl), run_time=0.9)
        self.play(FadeIn(atp_lbl), FadeIn(nothing_r), run_time=0.6)
        self.play(FadeIn(outcome_l, scale=0.9), FadeIn(outcome_r, scale=0.9), run_time=0.7)
        self.wait(max(0.5, total - 0.8 - 0.7 - 3 * 0.45 - 0.4 - 0.9 - 0.6 - 0.7))


# -------------------------------------------------------------- B14 Endcard

class B14_End(Scene):
    """RECAP — endcard: question restated + answer in one line."""
    def construct(self):
        total = DUR["B14"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=20)
        t1 = Text("2 ATP, not 30 —", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("because cancer cells optimize for carbon,", font=SERIF,
                  color=INK, font_size=38)
        t3 = Text("not energy.", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.20).move_to(UP * 0.25)
        u = Line(t3.get_corner(DL) + DOWN * 0.14, t3.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2.0, color=TEAL)
        sub = SerifLabel("the Warburg effect is a carbon-allocation strategy", INK, size=22)
        sub.next_to(block, DOWN, buff=0.55)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), FadeIn(t3), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.9))
