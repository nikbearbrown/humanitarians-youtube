"""vox_scenes.py — vox-name-match-gap
Why Unknown Doesn't Mean Avoid: The Name-Match Gap
THE REALLOCATION ENGINE

Color law:
  TEAL   = matched / consolidated / Likely tier / found
  CRIMSON= name-mismatch / fragmented / Unknown-from-bad-join / artifact
  GOLD   = fill highlight only, never text
  INK    = body text, neutral labels

Exclusions: no Levenshtein/fuzzy algorithms; no entity-resolution system design;
no legal entity definition. One mechanism only: punctuation-blind join fragments
a company into buckets that never meet.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ─────────────────────────────────────────────────────── B01  Title card
class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Why Unknown Doesn't Mean Avoid", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        t2 = Text("The Name-Match Gap", font=DISPLAY, color=CRIMSON, font_size=26, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL)+DOWN*0.13, t2.get_corner(DR)+DOWN*0.13, color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─────────────────────────────────────────────────────── B03  The Question card
class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = LabelChip("The Question", accent=SLATE, size=22)
        eye.to_corner(UL, buff=0.7)
        q1 = Text("A job engine should know the difference", font=SERIF, color=INK, font_size=28)
        q2 = Text("between a company that doesn't sponsor", font=SERIF, color=INK, font_size=28)
        q3 = Text("and one it simply cannot find.", font=SERIF, color=INK, font_size=28)
        body = VGroup(q1, q2, q3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        dek = Text("Here is the case where they look identical. Why?", font=SERIF,
                   color=CRIMSON, font_size=26, slant=ITALIC)
        body.move_to(UP * 0.4)
        dek.next_to(body, DOWN, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(body, shift=UP * 0.15), run_time=1.0)
        self.play(FadeIn(dek, shift=UP * 0.1), run_time=0.9)
        self.wait(max(0.3, total - 2.4))


# ─────────────────────────────────────────────────────── B04  Two Unknowns
class B04_TwoUnknowns(Scene):
    def construct(self):
        total = DUR["B04"]

        # Left column: "True absence"
        lbl_a = LabelChip("UNKNOWN A", accent=SLATE, size=22)
        desc_a1 = Text("No filing history", font=SERIF, color=INK, font_size=26)
        desc_a2 = Text("Never sponsored, or too new", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        col_a = VGroup(lbl_a, desc_a1, desc_a2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        # Right column: "Name-match artifact"
        lbl_b = LabelChip("UNKNOWN B", accent=CRIMSON, size=22)
        desc_b1 = Text("Name-match failure", font=SERIF, color=INK, font_size=26)
        desc_b2 = Text("Filings exist — never joined", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC)
        col_b = VGroup(lbl_b, desc_b1, desc_b2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        cols = VGroup(col_a, col_b).arrange(RIGHT, buff=1.8, aligned_edge=UP)
        cols.move_to(UP * 0.2)

        divider = Line(UP * 1.8 + RIGHT * 0.0, DOWN * 1.8 + RIGHT * 0.0,
                       stroke_width=1.5, color=INK)
        divider.move_to(cols.get_center())

        self.play(FadeIn(col_a, shift=RIGHT * 0.2), run_time=0.9)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(col_b, shift=LEFT * 0.2), run_time=0.9)
        self.wait(max(0.3, total - 2.2))


# ─────────────────────────────────────────────────────── B05  Name-mismatch cause
class B05_NameMismatchCause(Scene):
    def construct(self):
        total = DUR["B05"]

        title = SerifLabel("The filing exists. It just never joined.", accent=CRIMSON, size=32)
        title.move_to(UP * 1.5)

        # Two database rows that should match but don't
        row_dol = Rectangle(width=5.5, height=0.7).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        row_dol_lbl = Text("DOL: BioTechCo LLC  (8 filings)", font=MONO, color=INK, font_size=22)
        row_dol_lbl.move_to(row_dol)

        row_usc = Rectangle(width=5.5, height=0.7).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        row_usc_lbl = Text("USCIS: BIOTECHCO LLC  (8 approvals)", font=MONO, color=INK, font_size=22)
        row_usc_lbl.move_to(row_usc)

        rows = VGroup(
            VGroup(row_dol, row_dol_lbl),
            VGroup(row_usc, row_usc_lbl)
        ).arrange(DOWN, buff=0.55)
        rows.next_to(title, DOWN, buff=0.55)

        cross = Line(rows.get_center() + LEFT * 3.0, rows.get_center() + RIGHT * 3.0,
                     stroke_width=2.5, color=CRIMSON)
        cross_lbl = Text("no match", font=DISPLAY, color=CRIMSON, font_size=20)
        cross_lbl.next_to(cross, RIGHT, buff=0.3)

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(rows[0], shift=RIGHT * 0.15), run_time=0.7)
        self.play(FadeIn(rows[1], shift=LEFT * 0.15), run_time=0.7)
        self.play(Create(cross), FadeIn(cross_lbl), run_time=0.8)
        self.wait(max(0.3, total - 2.9))


# ─────────────────────────────────────────────────────── B07  Bucket diagram
class B07_BucketDiagram(Scene):
    def construct(self):
        total = DUR["B07"]

        # Three buckets — name variants
        def make_bucket(label, count, color, w=3.8):
            chip = LabelChip(label, accent=color, size=18)
            bar = Rectangle(width=w, height=0.5 * count).set_fill(color, 0.25).set_stroke(color, 1.8)
            cnt = Text(str(count), font=MONO, color=color, font_size=28, weight=BOLD)
            cnt.move_to(bar)
            return VGroup(chip, VGroup(bar, cnt)).arrange(DOWN, buff=0.18)

        b1 = make_bucket("BioTechCo LLC", 5, CRIMSON)
        b2 = make_bucket("BIOTECHCO LLC", 4, CRIMSON)
        b3 = make_bucket("BioTechCo Inc", 3, CRIMSON)

        buckets = VGroup(b1, b2, b3).arrange(RIGHT, buff=0.9, aligned_edge=DOWN)
        buckets.move_to(UP * 0.3)

        # Dotted boundary around all three
        boundary = DashedVMobject(
            SurroundingRectangle(buckets, buff=0.35, corner_radius=0.2)
            .set_stroke(TEAL, 2),
            num_dashes=32
        )
        boundary_lbl = Text("same legal filer", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        boundary_lbl.next_to(boundary, DOWN, buff=0.2)

        self.play(FadeIn(b1, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(b2, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(b3, shift=UP * 0.2), run_time=0.6)
        self.play(Create(boundary), FadeIn(boundary_lbl), run_time=1.2)
        self.wait(max(0.3, total - 3.1))


# ─────────────────────────────────────────────────────── B08  Consolidated count
class B08_ConsolidatedCount(Scene):
    def construct(self):
        total = DUR["B08"]

        # Start with three small fragmented buckets
        def small_bucket(n, color):
            bar = Rectangle(width=1.2, height=0.35 * n).set_fill(color, 0.2).set_stroke(color, 1.5)
            cnt = Text(str(n), font=MONO, color=color, font_size=22)
            cnt.move_to(bar)
            return VGroup(bar, cnt)

        frags = VGroup(
            small_bucket(5, CRIMSON),
            small_bucket(4, CRIMSON),
            small_bucket(3, CRIMSON)
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        frags.move_to(LEFT * 3.0 + UP * 0.3)

        arrow = Arrow(frags.get_right() + RIGHT * 0.15, RIGHT * 0.5 + UP * 0.3,
                      color=TEAL, stroke_width=3, buff=0.1)
        consolidate_lbl = Text("resolve entity", font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        consolidate_lbl.next_to(arrow, UP, buff=0.12)

        # Big consolidated bucket
        bar_big = Rectangle(width=2.2, height=2.1).set_fill(TEAL, 0.25).set_stroke(TEAL, 2.5)
        cnt_big = Text("12", font=MONO, color=TEAL, font_size=52, weight=BOLD)
        cnt_big.move_to(bar_big)
        big_bucket = VGroup(bar_big, cnt_big)
        big_bucket.move_to(RIGHT * 3.0 + UP * 0.3)

        true_lbl = Text("true count", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        true_lbl.next_to(big_bucket, DOWN, buff=0.25)

        self.play(FadeIn(frags, shift=UP * 0.15), run_time=0.8)
        self.wait(0.6)
        self.play(GrowArrow(arrow), FadeIn(consolidate_lbl), run_time=0.8)
        self.play(FadeIn(big_bucket, shift=LEFT * 0.2), FadeIn(true_lbl), run_time=1.0)
        self.wait(max(0.3, total - 3.2))


# ─────────────────────────────────────────────────────── B09  Coverage audit dial
class B09_CoverageAudit(Scene):
    def construct(self):
        total = DUR["B09"]

        title = Text("Join Coverage", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        title.to_edge(UP, buff=0.8)

        # Coverage bar
        bar_bg = Rectangle(width=9.0, height=0.8).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 1.5)
        bar_bg.next_to(title, DOWN, buff=0.8)

        bar_matched = Rectangle(width=9.0 * 0.64, height=0.8).set_fill(TEAL, 0.8).set_stroke(width=0)
        bar_matched.align_to(bar_bg, LEFT)

        pct_matched = Text("64% matched", font=MONO, color=INK, font_size=22, weight=BOLD)
        pct_matched.move_to(bar_matched)

        pct_unmatched = Text("36% unmatched", font=MONO, color=INK, font_size=22)
        pct_unmatched.next_to(bar_matched, RIGHT, buff=0.3)

        note_lbl = SerifLabel("each unmatched company may be an artifact", accent=CRIMSON, size=24)
        note_lbl.next_to(bar_bg, DOWN, buff=0.6)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(bar_bg), run_time=0.5)
        self.play(FadeIn(bar_matched, shift=RIGHT * 0.2), FadeIn(pct_matched), run_time=0.9)
        self.play(FadeIn(pct_unmatched, shift=LEFT * 0.15), run_time=0.6)
        self.play(FadeIn(note_lbl), run_time=0.7)
        self.wait(max(0.3, total - 3.3))


# ─────────────────────────────────────────────────────── B10  Two actions
class B10_TwoActions(Scene):
    def construct(self):
        total = DUR["B10"]

        header = Text("Same tier. Opposite fix.", font=DISPLAY, color=INK,
                      font_size=28, weight=BOLD)
        header.to_edge(UP, buff=0.7)

        # Left: True absence
        chip_a = LabelChip("True absence", accent=SLATE, size=22)
        fix_a1 = Text("Look for direct signals:", font=SERIF, color=INK, font_size=24)
        fix_a2 = Text("careers page, recruiter, LinkedIn H-1B posts", font=SERIF,
                      color=INK, font_size=20, slant=ITALIC)
        col_a = VGroup(chip_a, fix_a1, fix_a2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        # Right: Artifact
        chip_b = LabelChip("Name-match artifact", accent=CRIMSON, size=22)
        fix_b1 = Text("Resolve the entity name,", font=SERIF, color=INK, font_size=24)
        fix_b2 = Text("re-run the join", font=SERIF, color=TEAL, font_size=24)
        col_b = VGroup(chip_b, fix_b1, fix_b2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        cols = VGroup(col_a, col_b).arrange(RIGHT, buff=1.4, aligned_edge=UP)
        cols.next_to(header, DOWN, buff=0.6)

        divider = Line(UP * 1.5, DOWN * 1.5, stroke_width=1.2, color=INK)
        divider.move_to(cols.get_center())

        audit_note = Text("Coverage audit tells them apart.", font=SERIF,
                          color=TEAL, font_size=24, slant=ITALIC)
        audit_note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(header, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(col_a, shift=RIGHT * 0.2), Create(divider), run_time=0.9)
        self.play(FadeIn(col_b, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(audit_note, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 3.0))


# ─────────────────────────────────────────────────────── B11  NovaGen setup
class B11_NovaGenExample(Scene):
    def construct(self):
        total = DUR["B11"]

        # Company card — white text on slate card (card covers the cream ground)
        card = Rectangle(width=4.5, height=2.8).set_fill(SLATE, 1).set_stroke(width=0)
        card.move_to(LEFT * 3.0)
        name = Text("NovaGen", font=SERIF, color=INK, font_size=36, weight=BOLD)
        stage = Text("Series B  |  3 yrs  |  60 employees", font=MONO, color=INK, font_size=18)
        card_grp = VGroup(name, stage).arrange(DOWN, buff=0.2).move_to(card.get_center())
        tier_chip = LabelChip("UNKNOWN", accent=CRIMSON, size=24)
        tier_chip.next_to(card, DOWN, buff=0.2)
        company_block = VGroup(card, name, stage, tier_chip)

        # Coverage stat
        cov_lbl = Text("Join coverage:", font=SERIF, color=INK, font_size=26)
        cov_num = Text("64%", font=MONO, color=TEAL, font_size=52, weight=BOLD)
        cov_sub = Text("~36% of Unknowns may be artifacts", font=SERIF,
                       color=CRIMSON, font_size=22, slant=ITALIC)
        cov_block = VGroup(cov_lbl, cov_num, cov_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        cov_block.move_to(RIGHT * 2.8 + UP * 0.1)

        self.play(FadeIn(card, shift=RIGHT * 0.2), FadeIn(name), FadeIn(stage), run_time=0.8)
        self.play(FadeIn(tier_chip, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(cov_block, shift=LEFT * 0.2), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


# ─────────────────────────────────────────────────────── B12  NovaGen fix
class B12_NovaGenFix(Scene):
    def construct(self):
        total = DUR["B12"]

        # Show the two raw name rows
        row_dol = Rectangle(width=5.8, height=0.72).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.8)
        lbl_dol_tag = Text("DOL:", font=MONO, color=CRIMSON, font_size=20)
        lbl_dol_val = Text("NovaGen Bio LLC", font=MONO, color=INK, font_size=22)
        lbl_dol_row = VGroup(lbl_dol_tag, lbl_dol_val).arrange(RIGHT, buff=0.3)
        lbl_dol_row.move_to(row_dol)

        row_usc = Rectangle(width=5.8, height=0.72).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.8)
        lbl_usc_tag = Text("USCIS:", font=MONO, color=CRIMSON, font_size=20)
        lbl_usc_val = Text("NOVAGEN BIO", font=MONO, color=INK, font_size=22)
        lbl_usc_row = VGroup(lbl_usc_tag, lbl_usc_val).arrange(RIGHT, buff=0.3)
        lbl_usc_row.move_to(row_usc)

        rows_before = VGroup(
            VGroup(row_dol, lbl_dol_row),
            VGroup(row_usc, lbl_usc_row)
        ).arrange(DOWN, buff=0.4)
        rows_before.move_to(UP * 1.2)

        fix_arrow = Arrow(rows_before.get_bottom() + DOWN * 0.1,
                          rows_before.get_bottom() + DOWN * 1.0,
                          color=TEAL, stroke_width=3, buff=0.1)
        fix_lbl = Text("strip punctuation + normalize case", font=SERIF,
                       color=TEAL, font_size=22, slant=ITALIC)
        fix_lbl.next_to(fix_arrow, RIGHT, buff=0.25)

        # After: matched, tier jumps
        matched_bar = Rectangle(width=5.8, height=0.72).set_fill(TEAL, 0.25).set_stroke(TEAL, 2.2)
        matched_txt = Text("NOVAGEN BIO  =  NOVAGEN BIO", font=MONO, color=INK, font_size=22)
        matched_txt.move_to(matched_bar)
        matched_grp = VGroup(matched_bar, matched_txt)

        count_txt = Text("8 filings surface", font=MONO, color=TEAL, font_size=26, weight=BOLD)
        tier_after = LabelChip("LIKELY", accent=TEAL, size=26)
        result_grp = VGroup(count_txt, tier_after).arrange(RIGHT, buff=0.6)
        matched_grp.next_to(fix_arrow.get_end(), DOWN, buff=0.25)
        result_grp.next_to(matched_grp, DOWN, buff=0.3)

        self.play(FadeIn(rows_before, shift=DOWN * 0.1), run_time=0.8)
        self.play(GrowArrow(fix_arrow), FadeIn(fix_lbl), run_time=0.8)
        self.play(FadeIn(matched_grp, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(result_grp, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.3, total - 3.1))


# ─────────────────────────────────────────────────────── B13  Endcard / Recap
class B13_Endcard(Scene):
    def construct(self):
        total = DUR["B13"]

        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        answer = Text("Unknown has two causes.", font=DISPLAY, color=INK,
                      font_size=30, weight=BOLD)
        detail1 = Text("The coverage audit tells you which one.", font=SERIF,
                       color=INK, font_size=26)
        detail2 = Text("Fix the join — or find the signal.", font=SERIF,
                       color=TEAL, font_size=26)
        detail3 = Text("Never skip both.", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)

        block = VGroup(answer, detail1, detail2, detail3).arrange(DOWN, buff=0.28)
        block.move_to(UP * 0.1)
        eye.next_to(block, UP, buff=0.55)

        u = Line(answer.get_corner(DL)+DOWN*0.1, answer.get_corner(DR)+DOWN*0.1,
                 color=GOLD, stroke_width=2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(answer), Create(u), run_time=0.9)
        self.play(FadeIn(detail1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(detail2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(detail3, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.2))
