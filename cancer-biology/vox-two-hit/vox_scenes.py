"""vox_scenes.py — Why Knudson's Math Solved Cancer Genetics Before Molecular
Biology Did (vox-two-hit, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 and B11 are
STILL (ai media slots) and have no scenes here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-two-hit

Color law: TEAL #1F6F5C = the pre-loaded germline hit / familial advantage /
mechanism that works. CRIMSON #BF3339 = the somatic hit / tumor event /
what must happen twice. GOLD #F5D061 = editor's-pen highlight, fill only,
once at B12 confirmation payoff. Never swapped mid-film.

Exclusions honored: NO RB1 protein biochemistry, NO Rb/E2F gate mechanism,
NO other two-hit gene mechanisms, NO PTEN haploinsufficiency, NO Knudson
career history.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 11.0, "B03": 11.0, "B04": 12.0, "B05": 11.0, "B06": 12.0,
    "B07": 13.0, "B08": 13.0, "B09": 14.0, "B10": 12.0,
    "B12": 12.0, "B13": 12.0, "B14": 12.0, "B15": 11.0, "B16": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _cell_circle(color=INK, radius=0.22, fill_opacity=0.0):
    c = Circle(radius=radius)
    c.set_fill(color, fill_opacity).set_stroke(color, 2.5)
    return c


def _allele_box(color, label_text, size=0.55):
    box = Square(size)
    box.set_fill(color, 0.85).set_stroke(color, 2.0)
    lbl = Text(label_text, font=DISPLAY, color=WHITE,
               font_size=18, weight="MEDIUM")
    lbl.move_to(box)
    return VGroup(box, lbl)


def _hit_arrow(start, end, color=CRIMSON):
    arr = Arrow(start, end, color=color, stroke_width=4,
                max_tip_length_to_length_ratio=0.25, buff=0.0)
    return arr


# ---------------------------------------------------------------- scenes


class B01_Title(Scene):
    """Title card: CANCER BIOLOGY eyebrow (TEAL), main title in INK."""
    def construct(self):
        total = DUR["B01"]
        # Eyebrow: TEAL — "good / kept / true" accent, per card spec
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=26, weight="MEDIUM")
        t1 = Text("Why Knudson's Math Solved", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("Cancer Genetics Before", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        t3 = Text("Molecular Biology Did", font=DISPLAY, color=INK,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        sub = Text("counting tumors in children", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        u = Line(sub.get_corner(DL) + DOWN * 0.1,
                 sub.get_corner(DR) + DOWN * 0.1,
                 color=TEAL, stroke_width=1.8)
        eye.next_to(block, UP, buff=0.7)
        sub_group = VGroup(sub, u)
        sub_group.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(eye, shift=DOWN * 0.2), run_time=0.7)
        self.play(FadeIn(block, shift=UP * 0.1), run_time=1.1)
        self.play(FadeIn(sub_group, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.5, total - 2.6))


class B03_OnsetPattern(Scene):
    """Familial vs sporadic onset side-by-side: early bilateral vs late unilateral."""
    def construct(self):
        total = DUR["B03"]
        # Two columns
        fam_label = LabelChip("FAMILIAL", accent=TEAL, size=24)
        spo_label = LabelChip("SPORADIC", accent=CRIMSON, size=24)
        fam_label.move_to(LEFT * 3.5 + UP * 2.8)
        spo_label.move_to(RIGHT * 3.5 + UP * 2.8)

        # Age axis labels
        age_early = Text("Year 1", font=MONO, color=INK, font_size=22)
        age_early.move_to(LEFT * 3.5 + UP * 1.2)
        age_late = Text("Year 4-5", font=MONO, color=INK, font_size=22)
        age_late.move_to(RIGHT * 3.5 + UP * 0.2)

        # Onset dots
        fam_dot = Circle(radius=0.22)
        fam_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        fam_dot.move_to(LEFT * 3.5 + UP * 1.2)
        spo_dot = Circle(radius=0.22)
        spo_dot.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        spo_dot.move_to(RIGHT * 3.5 + UP * 0.2)

        # Bilateral / unilateral labels
        fam_eye_lbl = SerifLabel("bilateral", TEAL, size=26)
        fam_eye_lbl.move_to(LEFT * 3.5 + DOWN * 0.3)
        spo_eye_lbl = SerifLabel("unilateral", CRIMSON, size=26)
        spo_eye_lbl.move_to(RIGHT * 3.5 + DOWN * 0.3)

        # Vertical divider
        divider = Line(UP * 3.2, DOWN * 1.8, color=INK, stroke_width=1.0)
        divider.move_to(ORIGIN)

        self.play(FadeIn(fam_label, shift=DOWN * 0.2),
                  FadeIn(spo_label, shift=DOWN * 0.2), run_time=0.8)
        self.play(Create(divider), run_time=0.5)
        self.play(GrowFromCenter(fam_dot), FadeIn(age_early), run_time=0.7)
        self.play(GrowFromCenter(spo_dot), FadeIn(age_late), run_time=0.7)
        self.play(FadeIn(fam_eye_lbl, shift=UP * 0.1),
                  FadeIn(spo_eye_lbl, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.5, total - 3.5))


class B04_TheQuestion(Scene):
    """THE QUESTION beat — on screen as a styled card."""
    def construct(self):
        total = DUR["B04"]
        q_eye = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                     font_size=22, weight="MEDIUM")
        q_line1 = Text("How did counting tumors in children", font=SERIF,
                       color=INK, font_size=36, weight="BOLD")
        q_line2 = Text("predict molecular biology?", font=SERIF,
                       color=INK, font_size=36, weight="BOLD")
        q_block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.15)
        q_block.move_to(ORIGIN)
        dek = Text("Knudson 1971: two events required — before any gene was sequenced.",
                   font=SERIF, color=INK, font_size=24, slant=ITALIC)
        u = Line(q_line2.get_corner(DL) + DOWN * 0.12,
                 q_line2.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=1.8)
        q_eye.next_to(q_block, UP, buff=0.7)
        dek.next_to(VGroup(q_block, u), DOWN, buff=0.5)
        self.play(FadeIn(q_eye, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(q_block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.play(FadeIn(dek, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


class B05_NaiveVsReal(Scene):
    """Naive assumption struck out; real inheritance shown as pre-loaded hit."""
    def construct(self):
        total = DUR["B05"]
        # Left panel: naive (struck tumor icon)
        naive_lbl = LabelChip("NAIVE ASSUMPTION", accent=CRIMSON, size=20)
        naive_lbl.move_to(LEFT * 3.8 + UP * 2.5)
        tumor_icon = Circle(radius=0.55)
        tumor_icon.set_fill(CRIMSON, 0.7).set_stroke(CRIMSON, 2.5)
        tumor_icon.move_to(LEFT * 3.8 + UP * 1.0)
        arrow_q = Text("inherited?", font=SERIF, color=INK,
                       font_size=26, slant=ITALIC)
        arrow_q.next_to(tumor_icon, DOWN, buff=0.3)
        strike1 = Line(tumor_icon.get_corner(UL) + LEFT * 0.1 + UP * 0.1,
                       tumor_icon.get_corner(DR) + RIGHT * 0.1 + DOWN * 0.1,
                       color=CRIMSON, stroke_width=5)
        strike1._qc_intentional = True  # deliberate strike-through

        # Right panel: real (cell with pre-loaded TEAL hit)
        real_lbl = LabelChip("WHAT ACTUALLY INHERITS", accent=TEAL, size=20)
        real_lbl.move_to(RIGHT * 3.0 + UP * 2.5)
        cell_bg = Circle(radius=0.55)
        cell_bg.set_fill(TEAL, 0.25).set_stroke(TEAL, 2.5)
        cell_bg.move_to(RIGHT * 3.0 + UP * 1.0)
        hit_dot = Circle(radius=0.18)
        hit_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        hit_dot.move_to(RIGHT * 3.0 + UP * 1.0)
        real_desc = SerifLabel("a pre-loaded change", TEAL, size=26)
        real_desc.move_to(RIGHT * 3.0 + DOWN * 0.2)

        divider = Line(UP * 3.2, DOWN * 1.5, color=INK, stroke_width=1.0)

        self.play(FadeIn(naive_lbl), FadeIn(real_lbl), Create(divider), run_time=0.8)
        self.play(GrowFromCenter(tumor_icon), FadeIn(arrow_q), run_time=0.7)
        self.play(Create(strike1), run_time=0.5)
        self.play(GrowFromCenter(cell_bg), GrowFromCenter(hit_dot), run_time=0.8)
        self.play(FadeIn(real_desc, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.4))


class B06_TwoHitConcept(Scene):
    """Two arrows must hit the same cell — the core two-hit requirement."""
    def construct(self):
        total = DUR["B06"]
        title = SerifLabel("two hits, same cell", INK, size=30)
        title.move_to(UP * 2.9)

        # Single target cell center
        cell = Circle(radius=0.6)
        cell.set_fill(INK, 0.08).set_stroke(INK, 2.5)
        cell.move_to(ORIGIN)
        cell_lbl = Text("retinal cell", font=SERIF, color=INK,
                        font_size=22, slant=ITALIC)
        cell_lbl.next_to(cell, DOWN, buff=0.35)

        # Hit 1 arrow from upper-left
        hit1_start = LEFT * 3.5 + UP * 2.0
        hit1_end = LEFT * 0.55 + UP * 0.35
        arr1 = _hit_arrow(hit1_start, hit1_end)
        lbl1 = LabelChip("HIT 1", accent=CRIMSON, size=22)
        lbl1.move_to(hit1_start + RIGHT * 0.5 + DOWN * 0.3)

        # Hit 2 arrow from upper-right
        hit2_start = RIGHT * 3.5 + UP * 2.0
        hit2_end = RIGHT * 0.55 + UP * 0.35
        arr2 = _hit_arrow(hit2_start, hit2_end)
        lbl2 = LabelChip("HIT 2", accent=CRIMSON, size=22)
        lbl2.move_to(hit2_start + LEFT * 0.5 + DOWN * 0.3)

        # Result: cell turns tumor
        tumor_cell = Circle(radius=0.6)
        tumor_cell.set_fill(CRIMSON, 0.75).set_stroke(CRIMSON, 2.5)
        tumor_cell.move_to(ORIGIN)
        tumor_lbl = LabelChip("TUMOR", accent=CRIMSON, size=26)
        tumor_lbl.next_to(tumor_cell, DOWN, buff=0.4)

        self.play(FadeIn(title), FadeIn(cell), FadeIn(cell_lbl), run_time=0.8)
        self.play(Create(arr1), FadeIn(lbl1), run_time=0.7)
        self.play(Create(arr2), FadeIn(lbl2), run_time=0.7)
        self.play(
            ReplacementTransform(cell, tumor_cell),
            FadeOut(cell_lbl),
            FadeIn(tumor_lbl, shift=UP * 0.1),
            run_time=0.9
        )
        self.wait(max(0.5, total - 3.1))


class B07_SporadicField(Scene):
    """Sporadic: grid of cells, two arrows must land on same cell — rare event squared."""
    def construct(self):
        total = DUR["B07"]
        title = LabelChip("SPORADIC", accent=CRIMSON, size=26)
        title.move_to(UP * 3.0 + LEFT * 3.5)
        subtitle = SerifLabel("two somatic hits required", CRIMSON, size=24)
        subtitle.next_to(title, RIGHT, buff=0.4)

        # Grid of cells (4x5 = 20)
        cols, rows = 5, 4
        cells = VGroup()
        for r in range(rows):
            for c in range(cols):
                cell = Circle(radius=0.25)
                cell.set_fill(INK, 0.06).set_stroke(INK, 1.8)
                cell.move_to(LEFT * 3.2 + RIGHT * c * 1.3 + UP * 1.5 + DOWN * r * 1.0)
                cells.add(cell)

        # Two arrows converging on one specific cell (cell index 11 = row 2, col 1)
        target_cell = cells[11]
        arr_a = _hit_arrow(LEFT * 5.5 + UP * 3.5, target_cell.get_center())
        arr_b = _hit_arrow(RIGHT * 5.5 + UP * 3.5, target_cell.get_center())

        # The one hit cell
        tumor_dot = Circle(radius=0.25)
        tumor_dot.set_fill(CRIMSON, 0.85).set_stroke(CRIMSON, 2.0)
        tumor_dot.move_to(target_cell.get_center())

        rare_lbl = SerifLabel("two hits, one cell — rare squared", CRIMSON, size=24)
        rare_lbl.move_to(DOWN * 2.8)

        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in cells],
                               lag_ratio=0.04), run_time=1.2)
        self.play(Create(arr_a), Create(arr_b), run_time=0.9)
        self.play(ReplacementTransform(target_cell, tumor_dot), run_time=0.6)
        self.play(FadeIn(rare_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B08_FamilialField(Scene):
    """Familial: all cells pre-loaded TEAL, multiple CRIMSON hits fall — many tumors."""
    def construct(self):
        total = DUR["B08"]
        title = LabelChip("FAMILIAL", accent=TEAL, size=26)
        title.move_to(UP * 3.0 + LEFT * 3.5)
        subtitle = SerifLabel("one hit inherited in every cell", TEAL, size=24)
        subtitle.next_to(title, RIGHT, buff=0.4)

        # Grid of cells — all TEAL-primed
        cols, rows = 5, 4
        cells = VGroup()
        for r in range(rows):
            for c in range(cols):
                cell = Circle(radius=0.25)
                cell.set_fill(TEAL, 0.28).set_stroke(TEAL, 2.0)
                cell.move_to(LEFT * 3.2 + RIGHT * c * 1.3 + UP * 1.5 + DOWN * r * 1.0)
                cells.add(cell)

        # Multiple single arrows landing on several cells
        target_indices = [2, 6, 12, 17]
        arrows = VGroup()
        for idx in target_indices:
            tc = cells[idx]
            # spread origins
            angle = np.pi * 0.5 + idx * 0.4
            origin = tc.get_center() + np.array([np.cos(angle) * 4.0,
                                                  np.sin(angle) * 3.5, 0])
            origin[0] = np.clip(origin[0], -6.5, 6.5)
            origin[1] = np.clip(origin[1], -3.5, 3.8)
            arr = _hit_arrow(origin, tc.get_center())
            arrows.add(arr)

        # Tumor dots at hit cells
        tumor_dots = VGroup()
        for idx in target_indices:
            td = Circle(radius=0.25)
            td.set_fill(CRIMSON, 0.85).set_stroke(CRIMSON, 2.0)
            td.move_to(cells[idx].get_center())
            tumor_dots.add(td)

        many_lbl = SerifLabel("multiple cells hit — bilateral, early", CRIMSON, size=24)
        many_lbl.move_to(DOWN * 2.8)

        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in cells],
                               lag_ratio=0.04), run_time=1.0)
        self.play(LaggedStart(*[Create(a) for a in arrows],
                               lag_ratio=0.15), run_time=1.0)
        hit_transforms = [ReplacementTransform(cells[i], tumor_dots[j])
                          for j, i in enumerate(target_indices)]
        self.play(*hit_transforms, run_time=0.7)
        self.play(FadeIn(many_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B09_ProbabilityCompare(Scene):
    """Probability comparison: sporadic (1 in 10^13) vs familial (1 in 10^6)."""
    def construct(self):
        total = DUR["B09"]
        # Two columns
        spo_col = LEFT * 3.5
        fam_col = RIGHT * 3.5

        spo_header = LabelChip("SPORADIC", accent=CRIMSON, size=24)
        spo_header.move_to(spo_col + UP * 3.0)
        fam_header = LabelChip("FAMILIAL", accent=TEAL, size=24)
        fam_header.move_to(fam_col + UP * 3.0)

        # Probability labels in MONO
        spo_prob = Text("1 in 10^13 / cell / year", font=MONO, color=INK, font_size=26)
        spo_prob.move_to(spo_col + UP * 1.8)
        fam_prob = Text("1 in 10^6 / cell / year", font=MONO, color=INK, font_size=26)
        fam_prob.move_to(fam_col + UP * 1.8)

        # Representative fields: sporadic = vast neutral field, tiny CRIMSON dot
        spo_field = Square(2.6).set_fill(INK, 0.05).set_stroke(INK, 1.5)
        spo_field.move_to(spo_col + UP * 0.3)
        spo_tiny = Circle(radius=0.06)
        spo_tiny.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        spo_tiny.move_to(spo_col + UP * 0.3 + RIGHT * 0.6 + DOWN * 0.4)

        # Familial = TEAL-tinted field, several CRIMSON dots
        fam_field = Square(2.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        fam_field.move_to(fam_col + UP * 0.3)
        fam_dots = VGroup()
        positions = [UP * 0.5 + LEFT * 0.5, UP * 0.1 + RIGHT * 0.6,
                     DOWN * 0.4 + LEFT * 0.2, DOWN * 0.3 + RIGHT * 0.3]
        for pos in positions:
            d = Circle(radius=0.1)
            d.set_fill(CRIMSON, 0.9).set_stroke(width=0, opacity=0)
            d.move_to(fam_col + UP * 0.3 + pos)
            fam_dots.add(d)

        # Outcome labels
        spo_out = SerifLabel("one tumor, late onset", CRIMSON, size=23)
        spo_out.move_to(spo_col + DOWN * 2.0)
        fam_out = SerifLabel("multiple tumors, year one", TEAL, size=23)
        fam_out.move_to(fam_col + DOWN * 2.0)

        # Illustrative note — within safe area y=-3.2
        illus = Text("(illustrative)", font=MONO, color=INK, font_size=18)
        illus.move_to(DOWN * 3.2)

        divider = Line(UP * 3.3, DOWN * 2.6, color=INK, stroke_width=1.0)

        self.play(FadeIn(spo_header), FadeIn(fam_header), Create(divider), run_time=0.8)
        self.play(FadeIn(spo_prob), FadeIn(fam_prob), run_time=0.7)
        self.play(FadeIn(spo_field), FadeIn(fam_field), run_time=0.7)
        self.play(GrowFromCenter(spo_tiny),
                  LaggedStart(*[GrowFromCenter(d) for d in fam_dots], lag_ratio=0.2),
                  run_time=0.9)
        self.play(FadeIn(spo_out, shift=UP * 0.1),
                  FadeIn(fam_out, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(illus), run_time=0.5)
        self.wait(max(0.5, total - 4.3))


class B10_DominantRecessive(Scene):
    """Dominant at family level (pedigree), recessive at cell level (two alleles)."""
    def construct(self):
        total = DUR["B10"]

        # Family level — top box
        fam_box = Rectangle(width=6.0, height=1.9)
        fam_box.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.8)
        fam_box.move_to(UP * 2.2)
        fam_lbl_head = LabelChip("FAMILY LEVEL", accent=TEAL, size=22)
        fam_lbl_head.next_to(fam_box, UP, buff=0.15)
        # Allele icon passed down
        allele_icon = _allele_box(TEAL, "1", size=0.5)
        allele_icon.move_to(fam_box.get_center() + LEFT * 1.6)
        dom_arr = Arrow(allele_icon.get_right(), allele_icon.get_right() + RIGHT * 2.0,
                        color=TEAL, stroke_width=3,
                        max_tip_length_to_length_ratio=0.25, buff=0.0)
        dom_lbl = SerifLabel("dominant: one copy raises risk", TEAL, size=23)
        dom_lbl.move_to(fam_box.get_center() + RIGHT * 1.0)

        # Cell level — bottom box
        cell_box = Rectangle(width=6.0, height=2.4)
        cell_box.set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.8)
        cell_box.move_to(DOWN * 1.3)
        cell_lbl_head = LabelChip("CELL LEVEL", accent=CRIMSON, size=22)
        cell_lbl_head.next_to(cell_box, UP, buff=0.15)

        # Normal cell: one TEAL, one neutral
        allele_a = _allele_box(TEAL, "1", size=0.5)
        allele_b_normal = Square(0.5)
        allele_b_normal.set_fill(INK, 0.1).set_stroke(INK, 2.0)
        b_lbl_n = Text("?", font=SERIF, color=INK, font_size=20)
        b_lbl_n.move_to(allele_b_normal)
        allele_b_normal_g = VGroup(allele_b_normal, b_lbl_n)
        normal_pair = VGroup(allele_a, allele_b_normal_g).arrange(RIGHT, buff=0.3)
        normal_pair.move_to(cell_box.get_center() + LEFT * 2.0)
        norm_label = SerifLabel("normal cell", INK, size=22)
        norm_label.next_to(normal_pair, DOWN, buff=0.25)

        # Tumor cell: both CRIMSON
        allele_c = _allele_box(CRIMSON, "X", size=0.5)
        allele_d = _allele_box(CRIMSON, "X", size=0.5)
        tumor_pair = VGroup(allele_c, allele_d).arrange(RIGHT, buff=0.3)
        tumor_pair.move_to(cell_box.get_center() + RIGHT * 1.8)
        tum_label = LabelChip("TUMOR", accent=CRIMSON, size=22)
        tum_label.next_to(tumor_pair, DOWN, buff=0.25)

        rec_arr = Arrow(normal_pair.get_right() + RIGHT * 0.1,
                        tumor_pair.get_left() + LEFT * 0.1,
                        color=CRIMSON, stroke_width=3,
                        max_tip_length_to_length_ratio=0.25, buff=0.0)
        rec_lbl = SerifLabel("both copies must go", CRIMSON, size=22)
        rec_lbl.move_to(cell_box.get_center() + UP * 0.3)

        self.play(FadeIn(fam_box), FadeIn(fam_lbl_head), run_time=0.7)
        self.play(FadeIn(allele_icon), Create(dom_arr), FadeIn(dom_lbl), run_time=0.9)
        self.play(FadeIn(cell_box), FadeIn(cell_lbl_head), run_time=0.6)
        self.play(FadeIn(normal_pair), FadeIn(norm_label), run_time=0.7)
        self.play(Create(rec_arr), FadeIn(rec_lbl), run_time=0.6)
        self.play(FadeIn(tumor_pair), FadeIn(tum_label), run_time=0.7)
        self.wait(max(0.5, total - 4.2))


class B12_Confirmation(Scene):
    """1986: allele-box glyphs showing familial vs sporadic molecular findings.
    GOLD highlight bar sweeps 'confirmed' — editor's pen, used once."""
    def construct(self):
        total = DUR["B12"]
        title = SerifLabel("1986: RB1 cloned — the molecular confirmation", INK, size=28)
        title.move_to(UP * 2.9)

        # Familial tumor: TEAL box (germline) + CRIMSON box (somatic)
        fam_head = LabelChip("FAMILIAL TUMOR", accent=TEAL, size=22)
        fam_head.move_to(LEFT * 3.8 + UP * 1.7)
        fam_a1 = _allele_box(TEAL, "G", size=0.65)   # G = germline
        fam_a1.move_to(LEFT * 4.3 + UP * 0.5)
        fam_a2 = _allele_box(CRIMSON, "S", size=0.65)  # S = somatic
        fam_a2.move_to(LEFT * 3.3 + UP * 0.5)
        fam_germ_lbl = SerifLabel("germline", TEAL, size=22)
        fam_germ_lbl.next_to(fam_a1, DOWN, buff=0.2)
        fam_som_lbl = SerifLabel("somatic", CRIMSON, size=22)
        fam_som_lbl.next_to(fam_a2, DOWN, buff=0.2)

        # Sporadic tumor: CRIMSON + CRIMSON
        spo_head = LabelChip("SPORADIC TUMOR", accent=CRIMSON, size=22)
        spo_head.move_to(RIGHT * 3.0 + UP * 1.7)
        spo_a1 = _allele_box(CRIMSON, "S", size=0.65)
        spo_a1.move_to(RIGHT * 2.5 + UP * 0.5)
        spo_a2 = _allele_box(CRIMSON, "S", size=0.65)
        spo_a2.move_to(RIGHT * 3.5 + UP * 0.5)
        spo_som1 = SerifLabel("somatic", CRIMSON, size=22)
        spo_som1.next_to(spo_a1, DOWN, buff=0.2)
        spo_som2 = SerifLabel("somatic", CRIMSON, size=22)
        spo_som2.next_to(spo_a2, DOWN, buff=0.2)

        # Bracket: both = biallelic loss
        both_lbl = SerifLabel("biallelic loss — both cases", INK, size=26)
        both_lbl.move_to(DOWN * 1.0)

        # CONFIRMED line with GOLD highlight fill bar
        confirmed_text = Text("1971 prediction: confirmed", font=SERIF,
                              color=INK, font_size=34, weight=BOLD)
        confirmed_text.move_to(DOWN * 2.2)
        # GOLD fill bar behind "confirmed" (editor's pen — fill only, never text)
        gold_bar = Rectangle(width=confirmed_text.width + 0.3,
                             height=confirmed_text.height + 0.1)
        gold_bar.set_fill(GOLD, 0.6).set_stroke(width=0, opacity=0)
        gold_bar.move_to(confirmed_text.get_center())

        divider = Line(UP * 2.2, DOWN * 0.4, color=INK, stroke_width=1.0)
        divider.move_to(UP * 0.9 + LEFT * 0.5)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(fam_head), FadeIn(spo_head), Create(divider), run_time=0.8)
        self.play(FadeIn(fam_a1), FadeIn(fam_a2),
                  FadeIn(fam_germ_lbl), FadeIn(fam_som_lbl), run_time=0.8)
        self.play(FadeIn(spo_a1), FadeIn(spo_a2),
                  FadeIn(spo_som1), FadeIn(spo_som2), run_time=0.8)
        self.play(FadeIn(both_lbl, shift=UP * 0.1), run_time=0.6)
        # GOLD bar slides in behind the text
        self.play(FadeIn(gold_bar, shift=RIGHT * 0.5),
                  FadeIn(confirmed_text), run_time=0.9)
        self.wait(max(0.5, total - 4.6))


class B13_TwoChildren(Scene):
    """Two children side-by-side: sporadic vs familial trajectories (illustrative)."""
    def construct(self):
        total = DUR["B13"]

        # Column headers
        spo_col_x = -3.8
        fam_col_x = 3.0
        spo_head = LabelChip("SPORADIC CHILD", accent=CRIMSON, size=22)
        spo_head.move_to(np.array([spo_col_x, 3.0, 0]))
        fam_head = LabelChip("FAMILIAL CHILD", accent=TEAL, size=22)
        fam_head.move_to(np.array([fam_col_x, 3.0, 0]))

        # Retina blobs (oval)
        spo_retina = Ellipse(width=2.4, height=1.6)
        spo_retina.set_fill(INK, 0.07).set_stroke(INK, 1.8)
        spo_retina.move_to(np.array([spo_col_x, 1.4, 0]))

        fam_retina = Ellipse(width=2.4, height=1.6)
        fam_retina.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.8)
        fam_retina.move_to(np.array([fam_col_x, 1.4, 0]))

        # Probability labels (MONO)
        spo_prob = Text("1 in 10^13 / cell / year", font=MONO, color=INK, font_size=22)
        spo_prob.move_to(np.array([spo_col_x, 0.2, 0]))
        fam_prob = Text("1 in 10^6 / cell / year", font=MONO, color=INK, font_size=22)
        fam_prob.move_to(np.array([fam_col_x, 0.2, 0]))

        # Outcomes
        spo_dot = Circle(radius=0.18)
        spo_dot.set_fill(CRIMSON, 0.9).set_stroke(width=0, opacity=0)
        spo_dot.move_to(np.array([spo_col_x, 1.4, 0]) + RIGHT * 0.5 + DOWN * 0.3)
        spo_out = SerifLabel("1 tumor, late onset", CRIMSON, size=23)
        spo_out.move_to(np.array([spo_col_x, -0.7, 0]))

        fam_dots = VGroup()
        fam_positions = [UP * 0.4 + LEFT * 0.5, UP * 0.2 + RIGHT * 0.5,
                         DOWN * 0.3 + LEFT * 0.2, DOWN * 0.4 + RIGHT * 0.6]
        for pos in fam_positions:
            fd = Circle(radius=0.15)
            fd.set_fill(CRIMSON, 0.9).set_stroke(width=0, opacity=0)
            fd.move_to(np.array([fam_col_x, 1.4, 0]) + pos)
            fam_dots.add(fd)
        fam_out = SerifLabel("bilateral tumors, year one", TEAL, size=23)
        fam_out.move_to(np.array([fam_col_x, -0.7, 0]))

        # Illustrative note — within safe area y=-3.2
        illus = Text("(illustrative)", font=MONO, color=INK, font_size=18)
        illus.move_to(DOWN * 3.2)

        divider = Line(UP * 3.3, DOWN * 2.6, color=INK, stroke_width=1.0)

        self.play(FadeIn(spo_head), FadeIn(fam_head), Create(divider), run_time=0.8)
        self.play(FadeIn(spo_retina), FadeIn(fam_retina), run_time=0.7)
        self.play(FadeIn(spo_prob), FadeIn(fam_prob), run_time=0.6)
        self.play(GrowFromCenter(spo_dot),
                  LaggedStart(*[GrowFromCenter(d) for d in fam_dots], lag_ratio=0.2),
                  run_time=0.9)
        self.play(FadeIn(spo_out, shift=UP * 0.1),
                  FadeIn(fam_out, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.5, total - 4.1))


class B14_MathSignature(Scene):
    """Probability trees: sporadic (two branches required) vs familial (pre-loaded, multiple)."""
    def construct(self):
        total = DUR["B14"]
        # Tree nodes as circles connected by lines — compact
        spo_col_x = -3.6
        fam_col_x = 3.2

        # SPORADIC tree
        spo_head = LabelChip("SPORADIC", accent=CRIMSON, size=22)
        spo_head.move_to(np.array([spo_col_x, 3.0, 0]))

        spo_root = Circle(radius=0.22)
        spo_root.set_fill(INK, 0.1).set_stroke(INK, 2.0)
        spo_root.move_to(np.array([spo_col_x, 1.8, 0]))

        spo_b1 = Circle(radius=0.22)
        spo_b1.set_fill(INK, 0.1).set_stroke(CRIMSON, 2.0)
        spo_b1.move_to(np.array([spo_col_x, 0.5, 0]))
        spo_l1 = SerifLabel("hit 1 (rare)", CRIMSON, size=20)
        spo_l1.next_to(spo_b1, RIGHT, buff=0.3)

        spo_b2 = Circle(radius=0.22)
        spo_b2.set_fill(CRIMSON, 0.75).set_stroke(CRIMSON, 2.0)
        spo_b2.move_to(np.array([spo_col_x, -0.8, 0]))
        spo_l2 = SerifLabel("hit 2 (rare)", CRIMSON, size=20)
        spo_l2.next_to(spo_b2, RIGHT, buff=0.3)

        spo_line1 = Line(spo_root.get_bottom(), spo_b1.get_top(), color=INK, stroke_width=2.0)
        spo_line2 = Line(spo_b1.get_bottom(), spo_b2.get_top(), color=CRIMSON, stroke_width=2.0)

        spo_outcome = LabelChip("ONE LATE TUMOR", accent=CRIMSON, size=20)
        spo_outcome.move_to(np.array([spo_col_x, -2.0, 0]))

        # FAMILIAL tree — root pre-loaded TEAL
        fam_head = LabelChip("FAMILIAL", accent=TEAL, size=22)
        fam_head.move_to(np.array([fam_col_x, 3.0, 0]))

        fam_root = Circle(radius=0.28)
        fam_root.set_fill(TEAL, 0.6).set_stroke(TEAL, 2.5)
        fam_root.move_to(np.array([fam_col_x, 1.8, 0]))
        fam_root_lbl = SerifLabel("hit 1 pre-loaded", TEAL, size=19)
        fam_root_lbl.next_to(fam_root, RIGHT, buff=0.3)

        # Multiple branches from root — each needing just one more hit
        fam_branches = VGroup()
        fam_b_lbls = VGroup()
        fam_lines = VGroup()
        branch_x_offsets = [-0.9, 0.0, 0.9]
        for bx in branch_x_offsets:
            b = Circle(radius=0.22)
            b.set_fill(CRIMSON, 0.75).set_stroke(CRIMSON, 2.0)
            b.move_to(np.array([fam_col_x + bx, 0.2, 0]))
            fam_branches.add(b)
            ln = Line(fam_root.get_bottom(),
                      b.get_top(), color=CRIMSON, stroke_width=2.0)
            fam_lines.add(ln)

        fam_b_lbl = SerifLabel("hit 2 (rare, but 1M cells)", CRIMSON, size=19)
        fam_b_lbl.move_to(np.array([fam_col_x + 1.9, 0.2, 0]))

        fam_outcome = LabelChip("BILATERAL, YEAR ONE", accent=TEAL, size=20)
        fam_outcome.move_to(np.array([fam_col_x, -1.1, 0]))

        sig_lbl = SerifLabel("bilateral pattern = mathematical signature of the pre-loaded hit",
                             INK, size=22)
        sig_lbl.move_to(DOWN * 3.1)

        divider = Line(UP * 3.3, DOWN * 2.7, color=INK, stroke_width=1.0)

        self.play(FadeIn(spo_head), FadeIn(fam_head), Create(divider), run_time=0.7)
        self.play(FadeIn(spo_root), FadeIn(fam_root), FadeIn(fam_root_lbl), run_time=0.7)
        self.play(Create(spo_line1), FadeIn(spo_b1), FadeIn(spo_l1), run_time=0.7)
        self.play(Create(spo_line2), FadeIn(spo_b2), FadeIn(spo_l2), run_time=0.6)
        self.play(LaggedStart(*[Create(ln) for ln in fam_lines], lag_ratio=0.15),
                  LaggedStart(*[FadeIn(b) for b in fam_branches], lag_ratio=0.15),
                  FadeIn(fam_b_lbl), run_time=0.9)
        self.play(FadeIn(spo_outcome), FadeIn(fam_outcome), run_time=0.7)
        self.play(FadeIn(sig_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.9))


class B15_Implication(Scene):
    """Cell with one TEAL hit, one CRIMSON arrow poised — one event away. SLATE chip list."""
    def construct(self):
        total = DUR["B15"]
        title = SerifLabel("every carrier cell: one hit away", CRIMSON, size=30)
        title.move_to(UP * 3.0)

        # Cell with one TEAL allele
        cell = Circle(radius=0.85)
        cell.set_fill(TEAL, 0.15).set_stroke(TEAL, 2.5)
        cell.move_to(LEFT * 2.8 + UP * 0.8)
        teal_allele = _allele_box(TEAL, "1", size=0.5)
        teal_allele.move_to(LEFT * 2.8 + UP * 0.8 + LEFT * 0.3)
        neutral_allele = Square(0.5)
        neutral_allele.set_fill(INK, 0.08).set_stroke(INK, 1.8)
        neutral_allele.move_to(LEFT * 2.8 + UP * 0.8 + RIGHT * 0.35)

        cell_lbl = SerifLabel("carrier cell", TEAL, size=24)
        cell_lbl.next_to(cell, DOWN, buff=0.3)

        # Single CRIMSON arrow hovering
        arrow_start = LEFT * 2.8 + UP * 3.2
        arrow_end = LEFT * 2.8 + UP * 1.7
        hover_arrow = _hit_arrow(arrow_start, arrow_end)
        one_lbl = SerifLabel("one more event", CRIMSON, size=24)
        one_lbl.next_to(hover_arrow, RIGHT, buff=0.3)

        # SLATE chip list of other tumor suppressors
        chip_title = SerifLabel("same logic:", SLATE, size=26)
        chip_title.move_to(RIGHT * 2.5 + UP * 2.0)
        genes = ["BRCA1", "BRCA2", "APC", "TP53"]
        gene_chips = VGroup()
        for i, g in enumerate(genes):
            chip = LabelChip(g, accent=SLATE, size=22)
            chip.move_to(RIGHT * 2.5 + UP * 1.0 + DOWN * i * 0.75)
            gene_chips.add(chip)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(cell), FadeIn(teal_allele), FadeIn(neutral_allele),
                  FadeIn(cell_lbl), run_time=0.8)
        self.play(Create(hover_arrow), FadeIn(one_lbl), run_time=0.7)
        self.play(FadeIn(chip_title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in gene_chips],
                               lag_ratio=0.15), run_time=0.9)
        self.wait(max(0.5, total - 3.6))


class B16_End(Scene):
    """Endcard: CANCER BIOLOGY eyebrow, question-to-answer recap."""
    def construct(self):
        total = DUR["B16"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=24, weight="MEDIUM")
        line1 = Text("Counting tumors predicted the two-hit rule.", font=SERIF,
                     color=INK, font_size=38, weight=BOLD)
        line2 = Text("The molecule confirmed it, sixteen years later.", font=SERIF,
                     color=INK, font_size=38, weight=BOLD)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(line2.get_corner(DL) + DOWN * 0.14,
                 line2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2.0)
        sub = Text("The bilateral, early-onset pattern is the signature of the pre-loaded hit.",
                   font=SERIF, color=INK, font_size=24, slant=ITALIC)
        sub.next_to(VGroup(block, u), DOWN, buff=0.5)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(line1, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(line2, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.0))
