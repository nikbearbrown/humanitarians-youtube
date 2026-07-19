"""vox_scenes.py — Why the Same Drug That Kills Cancer Cells Kills Platelets
(and How to Fix It) (vox-bcl-selectivity, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is the only STILL
(ai media slot) and has NO scene here. Durations read from beat_sheet.json
(actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-bcl-selectivity

Color law: TEAL #1F6F5C = BCL-2-dependent / survives venetoclax / therapeutic
  success; CRIMSON #BF3339 = BCL-XL-dependent / killed / on-target toxicity.
  GOLD = editor's-pen highlight fill only (never text). Two accents: TEAL + CRIMSON.
  SLATE = entity cards / structure (cell-type cards).

Gate B convention: every zero-width stroke is also zero-opacity.
Exclusions: no full intrinsic pathway, no MCL-1 inhibitors, no BH3 profiling
  assay detail, no IAP/TRAIL, no trial data tables.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 11.0, "B03": 13.0, "B04": 11.0, "B05": 12.0,
    "B06": 12.0, "B07": 13.0, "B08": 11.0, "B09": 12.0,
    "B10": 11.0, "B11": 13.0, "B12": 14.0, "B13": 14.0,
    "B14": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _card(w=8.5, h=1.2, color=SLATE, alpha=0.12):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, alpha).set_stroke(color, 1.5)
    return r


def _solid_card(w=2.8, h=2.8, color=SLATE):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return r


def _chip_row(labels, accent=TEAL, size=22):
    """Return a VGroup of LabelChips arranged in a row."""
    chips = [LabelChip(lbl, accent=accent, size=size) for lbl in labels]
    g = VGroup(*chips).arrange(RIGHT, buff=0.3)
    return g


def _bar(w, h, color, alpha=1.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """Title card — COLD OPEN. Eyebrow in TEAL, title in INK."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=26, weight="MEDIUM")
        t1 = Text("Why the Same Drug That Kills", font=DISPLAY, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("Cancer Cells Kills Platelets", font=DISPLAY, color=INK,
                  font_size=44, weight="BOLD")
        t3 = Text("and How to Fix It", font=SERIF, color=INK,
                  font_size=30, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.14)
        t3.next_to(block, DOWN, buff=0.22)
        full = VGroup(block, t3)
        full.move_to(UP * 0.2)
        eye.next_to(block, UP, buff=0.7)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.play(FadeIn(t3, shift=UP * 0.08), run_time=0.8)
        self.wait(max(0.5, total - 2.6))


class B03_TheQuestion(Scene):
    """THE QUESTION beat — question on screen with GOLD highlight fill on key phrase."""
    def construct(self):
        total = DUR["B03"]
        q1 = Text("A BCL-2/BCL-XL inhibitor", font=SERIF, color=INK,
                  font_size=36, slant=ITALIC)
        q2 = Text("releases the death program cancer cells have suppressed.", font=SERIF,
                  color=INK, font_size=36, slant=ITALIC)
        qblock = VGroup(q1, q2).arrange(DOWN, buff=0.15).move_to(UP * 0.6)
        dek = Text("Why do platelets die from the same drug?",
                   font=DISPLAY, color=INK, font_size=38, weight="BOLD")
        dek.next_to(qblock, DOWN, buff=0.5)
        # Gold highlight bar behind the dek (fill only, never text)
        gold_bar = Rectangle(width=dek.width + 0.4, height=dek.height + 0.2)
        gold_bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        gold_bar.move_to(dek)
        u = Line(dek.get_corner(DL) + DOWN * 0.12, dek.get_corner(DR) + DOWN * 0.12,
                 color=INK, stroke_width=2)
        self.play(FadeIn(qblock), run_time=1.0)
        self.play(FadeIn(gold_bar), FadeIn(dek), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 2.2))


class B04_NaiveExpectation(Scene):
    """THE PROBLEM — naive model: BCL-2 overexpressed in cancer, not normal cells."""
    def construct(self):
        total = DUR["B04"]
        # Two columns: cancer cell (left) and normal cell (right)
        lc = LEFT * 3.2 + DOWN * 0.1
        rc = RIGHT * 3.2 + DOWN * 0.1

        l_card = _solid_card(2.8, 3.0, SLATE)
        r_card = _solid_card(2.8, 3.0, SLATE)
        l_card.move_to(lc); r_card.move_to(rc)

        l_label = Text("LEUKEMIA CELL", font=DISPLAY, color=WHITE,
                       font_size=20, weight="MEDIUM")
        r_label = Text("NORMAL CELL", font=DISPLAY, color=WHITE,
                       font_size=20, weight="MEDIUM")
        l_label.move_to(lc + UP * 1.1)
        r_label.move_to(rc + UP * 1.1)

        # BCL-2 bar in left column (teal), absent from right
        bcl2_bar = _bar(2.2, 0.7, TEAL)
        bcl2_bar.move_to(lc + DOWN * 0.1)
        bcl2_text = Text("BCL-2", font=DISPLAY, color=WHITE,
                         font_size=22, weight="MEDIUM")
        bcl2_text.move_to(bcl2_bar)

        # "absent" chip in right column
        absent = LabelChip("absent", accent=CRIMSON, size=22)
        absent.move_to(rc + DOWN * 0.1)

        eye = SerifLabel("the naive model", SLATE, size=24).to_edge(UP, buff=0.6)

        self.play(FadeIn(l_card), FadeIn(r_card),
                  FadeIn(l_label), FadeIn(r_label), FadeIn(eye), run_time=1.0)
        self.play(FadeIn(bcl2_bar), FadeIn(bcl2_text), run_time=0.8)
        self.play(FadeIn(absent, scale=0.9), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B05_GuardianConcept(Scene):
    """THE PROBLEM — guardian holds the death program at bay."""
    def construct(self):
        total = DUR["B05"]
        # Central guardian card
        g_card = _solid_card(3.0, 1.2, SLATE)
        g_card.move_to(ORIGIN + UP * 0.4)
        g_label = Text("GUARDIAN", font=DISPLAY, color=WHITE,
                       font_size=26, weight="MEDIUM")
        g_sub = Text("(BCL-2 family)", font=SERIF, color=WHITE,
                     font_size=20, slant=ITALIC)
        g_group = VGroup(g_label, g_sub).arrange(DOWN, buff=0.05)
        g_group.move_to(g_card)

        # Death program block (crimson), held at right boundary
        death_block = _bar(2.4, 1.0, CRIMSON)
        death_block.move_to(RIGHT * 4.5 + UP * 0.4)
        death_label = Text("death program", font=SERIF, color=WHITE,
                           font_size=22, slant=ITALIC)
        death_label.move_to(death_block)

        # Arrow from guardian pushing right (suppressing)
        suppress_arr = Arrow(g_card.get_right(), death_block.get_left(),
                             color=INK, stroke_width=4, buff=0.1)

        # Cell card context (left)
        cell_card = _solid_card(2.2, 1.0, TEAL)
        cell_card.move_to(LEFT * 4.5 + UP * 0.4)
        cell_label = Text("CANCER CELL", font=DISPLAY, color=WHITE,
                          font_size=18, weight="MEDIUM")
        cell_label.move_to(cell_card)

        cap_label = SerifLabel("guardian suppresses death", SLATE, size=24)
        cap_label.move_to(DOWN * 2.2)

        self.play(FadeIn(cell_card), FadeIn(cell_label), run_time=0.7)
        self.play(GrowFromCenter(g_card), FadeIn(g_group), run_time=0.9)
        self.play(FadeIn(death_block), FadeIn(death_label), run_time=0.7)
        self.play(GrowArrow(suppress_arr), run_time=0.8)
        self.play(FadeIn(cap_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.7))


class B06_MultipleGuardians(Scene):
    """THE MECHANISM — three guardians, different cells depend on different ones."""
    def construct(self):
        total = DUR["B06"]
        # Three guardian chips across the top
        g_names = ["BCL-2", "BCL-XL", "MCL-1"]
        g_colors = [TEAL, CRIMSON, SLATE]
        g_chips = VGroup(*[LabelChip(n, accent=c, size=26)
                           for n, c in zip(g_names, g_colors)])
        g_chips.arrange(RIGHT, buff=1.2).move_to(UP * 2.2)

        # Cell type chips below each guardian
        cell_names = ["CLL LEUKEMIA", "PLATELET", "OTHERS"]
        cell_colors = [TEAL, CRIMSON, SLATE]
        cell_chips = VGroup(*[LabelChip(n, accent=c, size=22)
                              for n, c in zip(cell_names, cell_colors)])
        # Position each below its guardian
        for i, (chip, g_chip) in enumerate(zip(cell_chips, g_chips)):
            chip.move_to(np.array([g_chip.get_center()[0], -1.2, 0]))

        # Arrows from each guardian to its cell
        arrows = VGroup()
        for g_chip, c_chip in zip(g_chips, cell_chips):
            arr = Arrow(g_chip.get_bottom(), c_chip.get_top(),
                        color=INK, stroke_width=3, buff=0.12)
            arrows.add(arr)

        # Fade the MCL-1 group (excluded from card)
        mcl1_group = VGroup(g_chips[2], cell_chips[2], arrows[2])

        title = SerifLabel("each cell type leans on a different guardian", SLATE, size=24)
        title.to_edge(UP, buff=0.3)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(g_chips[0]), FadeIn(g_chips[1]), run_time=0.8)
        self.play(FadeIn(cell_chips[0]), FadeIn(cell_chips[1]),
                  GrowArrow(arrows[0]), GrowArrow(arrows[1]), run_time=1.0)
        self.play(FadeIn(mcl1_group, scale=0.85), run_time=0.6)
        self.play(mcl1_group.animate.set_opacity(0.35), run_time=0.5)
        self.wait(max(0.5, total - 3.5))


class B07_NavitoclaxBothHit(Scene):
    """THE MECHANISM — navitoclax hits both BCL-2 and BCL-XL; both cells die."""
    def construct(self):
        total = DUR["B07"]
        # Drug label at top
        drug_bar = _bar(5.0, 0.65, SLATE)
        drug_bar.move_to(UP * 3.0)
        drug_label = Text("NAVITOCLAX", font=DISPLAY, color=WHITE,
                          font_size=24, weight="MEDIUM")
        drug_label.move_to(drug_bar)

        # Two guardian chips
        bcl2_chip = LabelChip("BCL-2", accent=TEAL, size=26)
        bclxl_chip = LabelChip("BCL-XL", accent=CRIMSON, size=26)
        bcl2_chip.move_to(LEFT * 2.8 + UP * 1.2)
        bclxl_chip.move_to(RIGHT * 2.8 + UP * 1.2)

        # Lines from drug to guardians
        arr_bcl2 = Arrow(drug_bar.get_bottom() + LEFT * 1.4,
                         bcl2_chip.get_top(), color=TEAL, stroke_width=4, buff=0.1)
        arr_bclxl = Arrow(drug_bar.get_bottom() + RIGHT * 1.4,
                          bclxl_chip.get_top(), color=CRIMSON, stroke_width=4, buff=0.1)

        # Outcome chips
        cll_die = LabelChip("CLL DIES", accent=TEAL, size=24)
        plt_die = LabelChip("PLATELET DIES", accent=CRIMSON, size=24)
        cll_die.move_to(LEFT * 2.8 + DOWN * 0.3)
        plt_die.move_to(RIGHT * 2.8 + DOWN * 0.3)

        cll_lbl = SerifLabel("therapeutic", TEAL, size=22)
        plt_lbl = SerifLabel("on-target toxicity", CRIMSON, size=22)
        cll_lbl.next_to(cll_die, DOWN, buff=0.2)
        plt_lbl.next_to(plt_die, DOWN, buff=0.2)

        arr_cll = Arrow(bcl2_chip.get_bottom(), cll_die.get_top(),
                        color=TEAL, stroke_width=3, buff=0.1)
        arr_plt = Arrow(bclxl_chip.get_bottom(), plt_die.get_top(),
                        color=CRIMSON, stroke_width=3, buff=0.1)

        self.play(FadeIn(drug_bar), FadeIn(drug_label), run_time=0.7)
        self.play(FadeIn(bcl2_chip), FadeIn(bclxl_chip),
                  GrowArrow(arr_bcl2), GrowArrow(arr_bclxl), run_time=1.0)
        self.play(FadeIn(cll_die), FadeIn(plt_die),
                  GrowArrow(arr_cll), GrowArrow(arr_plt), run_time=1.0)
        self.play(FadeIn(cll_lbl), FadeIn(plt_lbl), run_time=0.7)
        self.wait(max(0.5, total - 3.4))


class B08_OnTargetToxicity(Scene):
    """THE MECHANISM — on-target toxicity concept card."""
    def construct(self):
        total = DUR["B08"]
        t1 = Text("On-target toxicity:", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("not a side effect, not an accident.", font=SERIF, color=INK,
                  font_size=38, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.28).move_to(UP * 0.3)
        sub = Text("the mechanism working as designed, in a cell that shares the dependency",
                   font=SERIF, color=INK, font_size=26, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.5)
        u = Line(t1.get_corner(DL) + DOWN * 0.12, t1.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=1.0)
        self.play(FadeIn(t2), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B09_WindowConcept(Scene):
    """THE IMPLICATION — therapeutic window set by dependency gap, not potency."""
    def construct(self):
        total = DUR["B09"]
        # Two dependency rectangles side by side, slightly overlapping for navitoclax
        cancer_rect = Rectangle(width=4.5, height=2.0)
        cancer_rect.set_fill(TEAL, 0.22).set_stroke(TEAL, 2)
        cancer_rect.move_to(LEFT * 1.8 + DOWN * 0.3)

        platelet_rect = Rectangle(width=4.5, height=2.0)
        platelet_rect.set_fill(CRIMSON, 0.22).set_stroke(CRIMSON, 2)
        platelet_rect.move_to(RIGHT * 1.8 + DOWN * 0.3)

        cancer_lbl = LabelChip("BCL-2 dependency", accent=TEAL, size=22)
        cancer_lbl.move_to(cancer_rect.get_center() + LEFT * 0.3)

        platelet_lbl = LabelChip("BCL-XL dependency", accent=CRIMSON, size=22)
        platelet_lbl.move_to(platelet_rect.get_center() + RIGHT * 0.3)

        # Label the overlap zone
        overlap_lbl = SerifLabel("navitoclax kills both", CRIMSON, size=22)
        overlap_lbl.move_to(DOWN * 1.8)

        # Window arrow (the gap between them)
        window_lbl = SerifLabel("venetoclax targets only this", TEAL, size=22)
        window_lbl.move_to(LEFT * 3.8 + UP * 1.5)
        arr_w = Arrow(window_lbl.get_right() + RIGHT * 0.1,
                      cancer_rect.get_top() + LEFT * 1.2 + DOWN * 0.1,
                      color=TEAL, stroke_width=3, buff=0.1)

        title = SerifLabel("therapeutic window = dependency gap, not potency", SLATE, size=22)
        title.to_edge(UP, buff=0.45)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(cancer_rect), FadeIn(cancer_lbl), run_time=0.8)
        self.play(FadeIn(platelet_rect), FadeIn(platelet_lbl), run_time=0.8)
        self.play(FadeIn(overlap_lbl, scale=0.9), run_time=0.6)
        self.play(FadeIn(window_lbl), GrowArrow(arr_w), run_time=0.8)
        self.wait(max(0.5, total - 3.6))


class B10_VenetoclaxFix(Scene):
    """THE IMPLICATION — venetoclax: BCL-2 selective, 500x over BCL-XL."""
    def construct(self):
        total = DUR["B10"]
        # Drug label
        drug_bar = _bar(5.0, 0.65, TEAL)
        drug_bar.move_to(UP * 3.0)
        drug_label = Text("VENETOCLAX", font=DISPLAY, color=WHITE,
                          font_size=24, weight="MEDIUM")
        drug_label.move_to(drug_bar)

        # Two guardian targets
        bcl2_chip = LabelChip("BCL-2", accent=TEAL, size=26)
        bclxl_chip = LabelChip("BCL-XL", accent=SLATE, size=26)
        bcl2_chip.move_to(LEFT * 2.8 + UP * 1.2)
        bclxl_chip.move_to(RIGHT * 2.8 + UP * 1.2)

        # Strong line to BCL-2, weak dashed line to BCL-XL
        arr_bcl2 = Arrow(drug_bar.get_bottom() + LEFT * 1.4,
                         bcl2_chip.get_top(), color=TEAL, stroke_width=5, buff=0.1)
        # Dashed weak line to BCL-XL
        line_bclxl = DashedLine(drug_bar.get_bottom() + RIGHT * 1.4,
                                bclxl_chip.get_top(), color=SLATE, stroke_width=2,
                                dash_length=0.12)

        # Selectivity label
        sel_lbl = SerifLabel("500x selectivity for BCL-2", TEAL, size=24)
        sel_lbl.move_to(ORIGIN + UP * 0.0)

        # Outcome chips
        cll_die = LabelChip("CLL DIES", accent=TEAL, size=24)
        plt_safe = LabelChip("PLATELET SURVIVES", accent=TEAL, size=24)
        cll_die.move_to(LEFT * 2.8 + DOWN * 0.4)
        plt_safe.move_to(RIGHT * 2.8 + DOWN * 0.4)

        arr_cll = Arrow(bcl2_chip.get_bottom(), cll_die.get_top(),
                        color=TEAL, stroke_width=3, buff=0.1)
        arr_plt = Arrow(bclxl_chip.get_bottom(), plt_safe.get_top(),
                        color=SLATE, stroke_width=2, buff=0.1)

        self.play(FadeIn(drug_bar), FadeIn(drug_label), run_time=0.7)
        self.play(FadeIn(bcl2_chip), FadeIn(bclxl_chip),
                  GrowArrow(arr_bcl2), Create(line_bclxl), run_time=1.0)
        self.play(FadeIn(sel_lbl, scale=0.9), run_time=0.7)
        self.play(FadeIn(cll_die), FadeIn(plt_safe),
                  GrowArrow(arr_cll), GrowArrow(arr_plt), run_time=1.0)
        self.wait(max(0.5, total - 3.4))


class B11_ThreeCells(Scene):
    """THE EXAMPLE — three cell types and their guardian dependencies."""
    def construct(self):
        total = DUR["B11"]
        # Three columns
        xs = [-4.2, 0.0, 4.2]
        names = ["CLL LEUKEMIA", "PLATELET", "NEUTROPHIL"]
        colors = [TEAL, CRIMSON, SLATE]
        dep_chips = ["BCL-2", "BCL-XL", "NEITHER"]
        dep_colors = [TEAL, CRIMSON, SLATE]

        col_cards = VGroup()
        dep_chip_group = VGroup()
        col_labels = VGroup()

        for i, (x, name, col, dep, dcol) in enumerate(
                zip(xs, names, colors, dep_chips, dep_colors)):
            c = _solid_card(2.6, 1.0, col)
            c.move_to(np.array([x, 1.8, 0]))
            lbl = Text(name, font=DISPLAY, color=WHITE,
                       font_size=17, weight="MEDIUM")
            lbl.move_to(c)
            col_cards.add(VGroup(c, lbl))
            chip = LabelChip(dep, accent=dcol, size=22)
            chip.move_to(np.array([x, 0.3, 0]))
            dep_chip_group.add(chip)
            dep_lbl = SerifLabel("dependent on", col, size=20)
            dep_lbl.next_to(chip, UP, buff=0.18)
            col_labels.add(dep_lbl)

        title = SerifLabel("same dose, three different cell types", SLATE, size=24)
        title.to_edge(UP, buff=0.45)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(col_cards[0]), FadeIn(col_cards[1]), FadeIn(col_cards[2]),
                  run_time=1.0)
        self.play(LaggedStart(
            FadeIn(col_labels[0]), FadeIn(dep_chip_group[0]),
            FadeIn(col_labels[1]), FadeIn(dep_chip_group[1]),
            FadeIn(col_labels[2]), FadeIn(dep_chip_group[2]),
            lag_ratio=0.15), run_time=1.5)
        self.wait(max(0.5, total - 3.1))


class B12_NavitoclaxFates(Scene):
    """THE EXAMPLE — navitoclax: CLL dies, platelet dies, neutrophil survives."""
    def construct(self):
        total = DUR["B12"]
        xs = [-4.2, 0.0, 4.2]

        # Drug bar at top
        drug_bar = _bar(10.5, 0.65, SLATE)
        drug_bar.move_to(UP * 3.3)
        drug_label = Text("NAVITOCLAX", font=DISPLAY, color=WHITE,
                          font_size=22, weight="MEDIUM")
        drug_label.move_to(drug_bar)

        # Cell headers
        cell_names = ["CLL LEUKEMIA", "PLATELET", "NEUTROPHIL"]
        cell_colors = [TEAL, CRIMSON, SLATE]
        headers = VGroup()
        for x, name, col in zip(xs, cell_names, cell_colors):
            c = _solid_card(2.6, 0.8, col)
            c.move_to(np.array([x, 1.8, 0]))
            lbl = Text(name, font=DISPLAY, color=WHITE,
                       font_size=17, weight="MEDIUM")
            lbl.move_to(c)
            headers.add(VGroup(c, lbl))

        # Fate chips
        fate_labels = ["CLL DIES", "PLATELET DIES", "SURVIVES"]
        fate_colors = [CRIMSON, CRIMSON, TEAL]
        fate_subs = ["therapeutic", "on-target toxicity", "neither dependency hit"]
        fate_chips = VGroup()
        fate_sub_lbls = VGroup()
        for x, lbl, col, sub in zip(xs, fate_labels, fate_colors, fate_subs):
            chip = LabelChip(lbl, accent=col, size=24)
            chip.move_to(np.array([x, 0.2, 0]))
            fate_chips.add(chip)
            sub_lbl = SerifLabel(sub, col, size=19)
            sub_lbl.next_to(chip, DOWN, buff=0.2)
            fate_sub_lbls.add(sub_lbl)

        self.play(FadeIn(drug_bar), FadeIn(drug_label), run_time=0.7)
        self.play(FadeIn(headers), run_time=0.8)
        self.play(LaggedStart(
            FadeIn(fate_chips[0]), FadeIn(fate_chips[1]), FadeIn(fate_chips[2]),
            lag_ratio=0.25), run_time=1.2)
        self.play(LaggedStart(
            FadeIn(fate_sub_lbls[0]), FadeIn(fate_sub_lbls[1]), FadeIn(fate_sub_lbls[2]),
            lag_ratio=0.2), run_time=1.0)
        self.wait(max(0.5, total - 3.7))


class B13_VenetoclaxFates(Scene):
    """THE EXAMPLE — venetoclax: CLL dies, platelet survives, neutrophil survives."""
    def construct(self):
        total = DUR["B13"]
        xs = [-4.2, 0.0, 4.2]

        # Drug bar (teal = BCL-2 selective)
        drug_bar = _bar(10.5, 0.65, TEAL)
        drug_bar.move_to(UP * 3.3)
        drug_label = Text("VENETOCLAX  (BCL-2 selective)", font=DISPLAY, color=WHITE,
                          font_size=20, weight="MEDIUM")
        drug_label.move_to(drug_bar)

        # Cell headers
        cell_names = ["CLL LEUKEMIA", "PLATELET", "NEUTROPHIL"]
        cell_colors = [TEAL, CRIMSON, SLATE]
        headers = VGroup()
        for x, name, col in zip(xs, cell_names, cell_colors):
            c = _solid_card(2.6, 0.8, col)
            c.move_to(np.array([x, 1.8, 0]))
            lbl = Text(name, font=DISPLAY, color=WHITE,
                       font_size=17, weight="MEDIUM")
            lbl.move_to(c)
            headers.add(VGroup(c, lbl))

        # Fate chips — all teal (two good, one therapeutic)
        fate_labels = ["CLL DIES", "SURVIVES", "SURVIVES"]
        fate_colors = [TEAL, TEAL, TEAL]
        fate_subs = ["BCL-2 dependency hit", "BCL-XL spared", "neither hit"]
        fate_chips = VGroup()
        fate_sub_lbls = VGroup()
        for x, lbl, col, sub in zip(xs, fate_labels, fate_colors, fate_subs):
            chip = LabelChip(lbl, accent=col, size=24)
            chip.move_to(np.array([x, 0.2, 0]))
            fate_chips.add(chip)
            sub_lbl = SerifLabel(sub, col, size=19)
            sub_lbl.next_to(chip, DOWN, buff=0.2)
            fate_sub_lbls.add(sub_lbl)

        self.play(FadeIn(drug_bar), FadeIn(drug_label), run_time=0.7)
        self.play(FadeIn(headers), run_time=0.8)
        self.play(LaggedStart(
            FadeIn(fate_chips[0]), FadeIn(fate_chips[1]), FadeIn(fate_chips[2]),
            lag_ratio=0.25), run_time=1.2)
        self.play(LaggedStart(
            FadeIn(fate_sub_lbls[0]), FadeIn(fate_sub_lbls[1]), FadeIn(fate_sub_lbls[2]),
            lag_ratio=0.2), run_time=1.0)
        self.wait(max(0.5, total - 3.7))


class B14_End(Scene):
    """RECAP endcard — question restated, answer, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B14"]
        kicker = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=24, weight="MEDIUM")
        t1 = Text("The window is set by which normal cell", font=SERIF, color=INK,
                  font_size=40, weight=BOLD)
        t2 = Text("shares the cancer's guardian dependency.", font=SERIF, color=INK,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.16).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        kicker.next_to(block, UP, buff=0.7)
        self.play(FadeIn(kicker), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 2.4))
