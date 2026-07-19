"""vox_scenes.py — Why a Dataset With Zero Missing Values Can Still Be
Missing Your Data (vox-comma-orphan, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash scripts/vox_run.sh reels/vox-comma-orphan

Color law: dusty navy #3D5A80 = matched/joined/counted · crimson #BF3339 =
orphaned/dropped/uncounted (the comma is crimson — the villain). Gold = the
editor's pen, once. NO base-rate / Bayes / verb-taxonomy content (card
exclusions): one mechanism only — a punctuation-blind join fragments one filer.

Gate B convention: every zero-width stroke is also zero-opacity, or the layout
audit strikes it.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

GREEN = "#4E7A51"          # muted editorial green — the honest "0 missing" check

DUR = {"B01": 10.5, "B03": 8.0, "B04": 9.5, "B05": 8.0, "B06": 10.0,
       "B07": 9.0, "B08": 8.5, "B09": 9.5, "B10": 9.0, "B11": 9.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------------- builders

ROW_W, ROW_H = 1.7, 0.24


def _row(color, w=ROW_W, h=ROW_H):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return r


def _row_block(n, color, cols=1, w=ROW_W, h=ROW_H, gap=0.12):
    """A stacked block of n filing-rows in one color."""
    g = VGroup(*[_row(color, w, h) for _ in range(n)])
    if cols == 1:
        g.arrange(DOWN, buff=gap)
    else:
        g.arrange_in_grid(cols=cols, buff=(gap, gap))
    return g


def _panel(center, w, h):
    p = Rectangle(width=w, height=h)
    p.set_fill(WHITE, 0.30).set_stroke("#C9C2B4", 1.6)
    p.move_to(center)
    return p


def _bucket(center, w=2.4, h=2.4, color=NAVY):
    b = Rectangle(width=w, height=h)
    b.set_fill(color, 0.08).set_stroke(color, 2.5)
    b.move_to(center)
    return b


def _gate(center):
    """A doorway: two ink posts + a lintel — the name-matching join."""
    h = 2.4
    lp = Line(center + LEFT * 0.55 + DOWN * h / 2, center + LEFT * 0.55 + UP * h / 2,
              color=INK, stroke_width=4)
    rp = Line(center + RIGHT * 0.55 + DOWN * h / 2, center + RIGHT * 0.55 + UP * h / 2,
              color=INK, stroke_width=4)
    lintel = Line(center + LEFT * 0.75 + UP * h / 2, center + RIGHT * 0.75 + UP * h / 2,
                  color=INK, stroke_width=4)
    return VGroup(lp, rp, lintel)


def _giant_comma(center, color=CRIMSON):
    c = Text(",", font=SERIF, color=color, font_size=320, weight=BOLD)
    c.move_to(center)
    return c


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("VERIFYING THE DATA", font=SERIF, color=NAVY, font_size=24)
        t1 = Text("Zero missing values —", font=SERIF, color=INK,
                  font_size=52, weight=BOLD)
        t2 = Text("still missing your data.", font=SERIF, color=INK,
                  font_size=52, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_EveryCellFull(Scene):     # DOCUMENT — the checker's whole definition
    def construct(self):
        _quote_scene(self, "Every cell is full.",
                     "— all the missingness check actually verifies", None,
                     "full", DUR["B03"])


class B04_TwoTables(Scene):         # two datasets, joined on name
    def construct(self):
        total = DUR["B04"]
        lc, rc = LEFT * 4.1 + DOWN * 0.2, RIGHT * 4.1 + DOWN * 0.2
        lpanel = _panel(lc, 3.1, 3.0)
        rpanel = _panel(rc, 3.1, 3.0)
        lrows = _row_block(4, NAVY).move_to(lc + UP * 0.25)
        rrows = _row_block(4, NAVY).move_to(rc + UP * 0.25)
        lhead = LabelChip("DOL · filings", accent=NAVY, size=22)
        lhead.next_to(lpanel, UP, buff=0.2)
        rhead = LabelChip("USCIS · approvals", accent=NAVY, size=22)
        rhead.next_to(rpanel, UP, buff=0.2)
        ltab = VGroup(lpanel, lrows, lhead)
        rtab = VGroup(rpanel, rrows, rhead)
        seam = SerifLabel("join on name", NAVY, size=28).move_to(ORIGIN + DOWN * 0.1)
        self.play(ltab.animate.shift(RIGHT * 0.0), FadeIn(ltab, shift=RIGHT * 0.6),
                  FadeIn(rtab, shift=LEFT * 0.6), run_time=1.1)
        self.play(FadeIn(seam, scale=0.9), run_time=0.7)
        self.wait(max(0.5, total - 1.8))


class B05_JoinGate(Scene):          # matched rows flow through the gate and join
    def construct(self):
        total = DUR["B05"]
        gate = _gate(ORIGIN + UP * 0.1)
        glabel = SerifLabel("match names", INK, size=24).next_to(gate, UP, buff=0.25)
        lrows = _row_block(3, NAVY).move_to(LEFT * 4.4 + UP * 0.1)
        rrows = _row_block(3, NAVY).move_to(RIGHT * 4.4 + UP * 0.1)
        joined = _bucket(RIGHT * 4.4 + DOWN * 0.1, 2.4, 2.4, NAVY)
        jlabel = LabelChip("joined", accent=NAVY, size=24).next_to(joined, DOWN, buff=0.2)
        self.play(FadeIn(gate), FadeIn(glabel),
                  FadeIn(lrows, shift=RIGHT * 0.4), FadeIn(rrows, shift=LEFT * 0.4),
                  run_time=1.0)
        merged = _row_block(3, NAVY).move_to(joined.get_center())
        self.play(lrows.animate.move_to(ORIGIN + LEFT * 0.1 + UP * 0.1),
                  rrows.animate.move_to(ORIGIN + RIGHT * 0.1 + UP * 0.1),
                  run_time=0.9)
        self.play(FadeIn(joined), ReplacementTransform(VGroup(lrows, rrows), merged),
                  FadeIn(jlabel), run_time=1.0)
        self.wait(max(0.5, total - 2.9))


class B06_OneCompany(Scene):        # 12 filings · one filer · two spellings
    def construct(self):
        total = DUR["B06"]
        eye = Text("one company · twelve filings", font=SERIF, color=NAVY,
                   font_size=28).to_edge(UP, buff=0.7)
        good = _row_block(10, NAVY, cols=2, w=1.5).move_to(LEFT * 3.0 + DOWN * 0.3)
        bad = _row_block(2, CRIMSON, cols=1, w=1.5).move_to(RIGHT * 3.2 + DOWN * 0.3)
        gchip = LabelChip("BioTechCo LLC", accent=NAVY, size=22)
        gchip.next_to(good, DOWN, buff=0.3)
        bchip = LabelChip("BioTechCo, LLC", accent=CRIMSON, size=22)
        bchip.next_to(bad, DOWN, buff=0.3)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(r, scale=0.9) for r in good], lag_ratio=0.05),
                  FadeIn(gchip), run_time=1.2)
        self.play(FadeIn(bad, shift=LEFT * 0.3), FadeIn(bchip), run_time=0.9)
        span = VGroup(good, gchip, bad, bchip)
        brace = Brace(span, DOWN, color=INK)
        blabel = SerifLabel("same legal filer", CRIMSON, size=26)
        blabel.next_to(brace, DOWN, buff=0.15)
        self.play(FadeIn(brace), FadeIn(blabel), run_time=0.8)
        self.wait(max(0.5, total - 3.5))


class B07_CommaSplit(Scene):        # THE SPLIT — one comma orphans two rows
    def construct(self):
        total = DUR["B07"]
        gate = _gate(ORIGIN + UP * 0.3)
        glabel = SerifLabel("case-folded, not punctuation", INK, size=22)
        glabel.next_to(gate, UP, buff=0.2)
        good = _row_block(10, NAVY, cols=2, w=1.4).move_to(LEFT * 4.6 + UP * 0.3)
        bad = _row_block(2, CRIMSON, cols=1, w=1.4).next_to(good, DOWN, buff=0.35)
        joined = _bucket(RIGHT * 4.6 + UP * 0.5, 2.3, 2.0, NAVY)
        jlabel = LabelChip("joined", accent=NAVY, size=22).next_to(joined, UP, buff=0.18)
        orphan = _bucket(RIGHT * 4.6 + DOWN * 2.1, 2.3, 1.4, CRIMSON)
        olabel = LabelChip("never joins", accent=CRIMSON, size=22)
        olabel.next_to(orphan, DOWN, buff=0.18)
        self.play(FadeIn(good), FadeIn(bad), FadeIn(gate), FadeIn(glabel),
                  run_time=1.0)
        comma = _giant_comma(ORIGIN + UP * 0.1)
        self.play(FadeIn(comma, shift=DOWN * 0.6, scale=0.7), run_time=0.7)
        good_moved = _row_block(10, NAVY, cols=2, w=1.4).move_to(joined.get_center())
        bad_moved = _row_block(2, CRIMSON, cols=1, w=1.4).move_to(orphan.get_center())
        self.play(FadeIn(joined), FadeIn(jlabel),
                  ReplacementTransform(good, good_moved), run_time=0.9)
        self.play(FadeIn(orphan), FadeIn(olabel),
                  ReplacementTransform(bad, bad_moved),
                  comma.animate.scale(1.08), run_time=1.0)
        self.wait(max(0.5, total - 3.6))


class B08_WrongCount(Scene):        # count = 10, not 12 — wrong denominator
    def construct(self):
        total = DUR["B08"]
        joined = _bucket(LEFT * 3.2 + UP * 0.2, 3.0, 3.0, NAVY)
        ten = Text("10", font=SERIF, color=NAVY, font_size=110, weight=BOLD)
        ten.move_to(joined.get_center())
        twelve = Text("12", font=SERIF, color=INK, font_size=64)
        twelve.set_opacity(0.35).next_to(joined, UP, buff=0.25)
        strike = Line(twelve.get_left() + LEFT * 0.05, twelve.get_right() + RIGHT * 0.05,
                      color=CRIMSON, stroke_width=4)
        strike._qc_intentional = True   # deliberate strike-through: exempt from
        #                                 Gate B's TEXT_ON_CURVE (12 struck to 10)
        denom = SerifLabel("wrong denominator", CRIMSON, size=26)
        denom.next_to(joined, DOWN, buff=0.3)
        orphan = _bucket(RIGHT * 3.6 + DOWN * 0.1, 2.2, 1.8, CRIMSON)
        two = Text("2", font=SERIF, color=CRIMSON, font_size=72, weight=BOLD)
        two.move_to(orphan.get_center())
        ochip = LabelChip("orphaned", accent=CRIMSON, size=22).next_to(orphan, DOWN, buff=0.2)
        self.play(FadeIn(joined), FadeIn(twelve), run_time=0.8)
        self.play(FadeIn(ten, scale=0.9), Create(strike), run_time=0.9)
        self.play(FadeIn(orphan), FadeIn(two), FadeIn(ochip), run_time=0.8)
        self.play(FadeIn(denom, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.1))


class B09_CheckSeesNothing(Scene):  # the magnifier scans WITHIN — misses the orphan
    def construct(self):
        total = DUR["B09"]

        def _cells(center):
            col = VGroup(*[Square(0.34).set_fill(WHITE, 0.4)
                           .set_stroke("#C9C2B4", 1.4) for _ in range(4)])
            col.arrange(DOWN, buff=0.14).move_to(center)
            return col

        lcol = _cells(LEFT * 3.4 + UP * 0.4)
        rcol = _cells(LEFT * 0.4 + UP * 0.4)
        lh = SerifLabel("DOL", NAVY, size=22).next_to(lcol, UP, buff=0.2)
        rh = SerifLabel("USCIS", NAVY, size=22).next_to(rcol, UP, buff=0.2)
        orphan = _bucket(RIGHT * 3.7 + DOWN * 0.3, 2.2, 1.6, CRIMSON)
        obad = _row_block(2, CRIMSON, cols=1, w=1.3).move_to(orphan.get_center())
        olabel = LabelChip("orphan · unscanned", accent=CRIMSON, size=20)
        olabel.next_to(orphan, DOWN, buff=0.18)
        self.play(FadeIn(lcol), FadeIn(rcol), FadeIn(lh), FadeIn(rh),
                  FadeIn(orphan), FadeIn(obad), FadeIn(olabel), run_time=1.0)
        lens = VGroup(Circle(radius=0.42).set_stroke(INK, 4).set_fill(BLUE, 0.05))
        handle = Line(ORIGIN, DR * 0.5, color=INK, stroke_width=5)
        handle.next_to(lens, DR, buff=-0.05)
        lens.add(handle)
        lens._qc_intentional = True   # the magnifier deliberately sweeps over
        #                               cells/headers: exempt from TEXT_ON_CURVE
        lens.move_to(lcol[0].get_center())
        self.play(FadeIn(lens), run_time=0.4)
        for col in (lcol, rcol):
            for cell in col:
                tick = Square(0.34).set_fill(NAVY, 0.55).set_stroke(width=0, opacity=0)
                tick.move_to(cell.get_center())
                self.play(lens.animate.move_to(cell.get_center()),
                          FadeIn(tick), run_time=0.28)
        chip = LabelChip("MISSING: 0", accent=GREEN, size=30)
        chip.move_to(DOWN * 2.6 + LEFT * 1.9)
        self.play(FadeIn(chip, scale=0.9), run_time=0.6)
        self.wait(max(0.4, total - 1.0 - 0.4 - 8 * 0.28 - 0.6))


class B10_BetweenRing(Scene):       # the gap lives between the tables
    def construct(self):
        total = DUR["B10"]
        lc, rc = LEFT * 3.4 + UP * 0.3, RIGHT * 3.4 + UP * 0.3
        lpanel = _panel(lc, 2.6, 2.6)
        rpanel = _panel(rc, 2.6, 2.6)
        lrows = _row_block(3, NAVY, w=1.5).move_to(lc)
        rrows = _row_block(3, NAVY, w=1.5).move_to(rc)
        lh = SerifLabel("DOL", NAVY, size=22).next_to(lpanel, UP, buff=0.18)
        rh = SerifLabel("USCIS", NAVY, size=22).next_to(rpanel, UP, buff=0.18)
        orphan = _bucket(DOWN * 2.4, 2.4, 1.3, CRIMSON)
        obad = _row_block(2, CRIMSON, cols=2, w=0.7, h=0.2).move_to(orphan.get_center())
        olabel = LabelChip("the orphaned rows", accent=CRIMSON, size=20)
        olabel.next_to(orphan, RIGHT, buff=0.3)
        self.play(FadeIn(lpanel), FadeIn(rpanel), FadeIn(lrows), FadeIn(rrows),
                  FadeIn(lh), FadeIn(rh), FadeIn(orphan), FadeIn(obad), FadeIn(olabel),
                  run_time=1.0)
        # the seam: an invisible placeholder in the empty space BETWEEN the tables
        seam = Rectangle(width=1.6, height=2.4).set_stroke(width=0, opacity=0)
        seam.set_fill(opacity=0).move_to(UP * 0.3)
        ring = HandRing(seam, color=CRIMSON)
        gap = SerifLabel("the gap is here", CRIMSON, size=24).move_to(UP * 0.3)
        self.play(FadeIn(gap), run_time=0.5)
        self.play(Create(ring), run_time=1.2)
        self.wait(max(0.5, total - 2.7))


class B11_End(Scene):               # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Zero missing doesn't mean", font=SERIF, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("nothing is missing.", font=SERIF, color=INK,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 5", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
