"""vox_scenes.py — The pH-Triggered Lock That Lets RNA Drugs Escape the Cell's Trash
(vox-endosomal-escape, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat whose source is 'own'.
B02 is the only STILL (ai media slot) and has no scene here.
Durations read from this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law:
  TEAL = escaped RNA / ionizable lipid working / cytosol (the good outcome)
  CRIMSON = trapped RNA / endosomal degradation (the bad outcome)
  GOLD = the pH switch (highlighter fill only, once per graphic)

Gate B convention: every zero-width stroke is also zero-opacity, or the layout
audit strikes it.
"""
import sys, pathlib as _pl
# Reel lives at books/<book>/youtube/<slug>/vox_scenes.py
# parents[3] = books/  → vox toolkit is at books/vox/
_vox_manim = _pl.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
if str(_vox_manim) not in sys.path:
    sys.path.insert(0, str(_vox_manim))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}

import numpy as np


# ---------------------------------------------------------------- B01_Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The pH-Triggered Lock That Lets", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("RNA Drugs Escape the Cell's Trash", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B03_Question

class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q = Text("How does the ionizable lipid", font=DISPLAY, color=INK,
                 font_size=34, weight=BOLD)
        q2 = Text("solve the endosomal trap?", font=DISPLAY, color=TEAL,
                  font_size=34, weight=BOLD)
        block = VGroup(q, q2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(q2.get_corner(DL) + DOWN * 0.13, q2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        sub = Text("siRNA works in a dish — silent in a mouse — why?",
                   font=SERIF, color=INK, font_size=22, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.55)
        self.play(FadeIn(q), run_time=0.7)
        self.play(FadeIn(q2), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.2))


# ---------------------------------------------------------------- B04_Endocytosis

class B04_Endocytosis(Scene):
    def construct(self):
        total = DUR["B04"]

        # LNP: small teal circle
        lnp = Circle(radius=0.28)
        lnp.set_fill(TEAL, 0.85).set_stroke(INK, 1.5)
        lnp.move_to(LEFT * 5.0 + UP * 0.2)

        # Cell membrane: a large arc (top of a circle) representing the cell surface
        cell_arc = Arc(radius=2.8, start_angle=PI * 0.15, angle=PI * 0.7,
                       color=INK, stroke_width=3)
        cell_arc.move_to(RIGHT * 1.5 + DOWN * 2.2)

        lnp_label = LabelChip("LNP", accent=TEAL, size=20)
        lnp_label.next_to(lnp, UP, buff=0.18)

        cell_label = SerifLabel("cell membrane", INK, size=22)
        cell_label.next_to(cell_arc, LEFT, buff=0.3)

        self.play(FadeIn(lnp), FadeIn(lnp_label), FadeIn(cell_arc), FadeIn(cell_label),
                  run_time=1.0)

        # Move LNP to the membrane
        self.play(lnp.animate.move_to(RIGHT * 1.5 + DOWN * 0.1),
                  lnp_label.animate.move_to(RIGHT * 1.5 + UP * 0.55),
                  run_time=1.0)

        # Endosome: a CRIMSON circle that appears around the LNP position
        endo = Circle(radius=0.55)
        endo.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2.5)
        endo.move_to(RIGHT * 1.5 + DOWN * 0.1)

        endo_label = LabelChip("endosome", accent=CRIMSON, size=20)
        endo_label.next_to(endo, RIGHT, buff=0.28)

        ph_label = Text("pH 7 -> 5.5", font=MONO, color=INK, font_size=22)
        ph_label.next_to(endo, DOWN, buff=0.32)

        self.play(Create(endo), run_time=0.9)
        self.play(FadeIn(endo_label), FadeIn(ph_label), run_time=0.7)
        self.wait(max(0.3, total - 3.6))


# ---------------------------------------------------------------- B05_pHDrop

class B05_pHDrop(Scene):
    def construct(self):
        total = DUR["B05"]

        # Endosome circle: large, centered
        endo = Circle(radius=2.0)
        endo.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 3)
        endo.move_to(ORIGIN + DOWN * 0.2)

        endo_label = LabelChip("endosome", accent=CRIMSON, size=22)
        endo_label.next_to(endo, UP, buff=0.28)

        # pH label at 7.4
        ph_74 = Text("pH 7.4", font=MONO, color=INK, font_size=38, weight=BOLD)
        ph_74.move_to(ORIGIN + UP * 0.4)

        arrow_down = Arrow(UP * 0.0, DOWN * 0.5, color=GOLD, stroke_width=4,
                           buff=0.05)
        arrow_down.next_to(ph_74, DOWN, buff=0.15)

        ph_55 = Text("pH 5.5", font=MONO, color=CRIMSON, font_size=38, weight=BOLD)
        ph_55.next_to(arrow_down, DOWN, buff=0.15)

        # H+ ions appearing inside
        ions = VGroup()
        positions = [LEFT * 0.9 + UP * 0.8, RIGHT * 0.8 + UP * 0.5,
                     LEFT * 0.3 + DOWN * 0.6, RIGHT * 1.0 + DOWN * 0.4,
                     LEFT * 1.1 + DOWN * 0.1]
        for pos in positions:
            ion = Text("H+", font=MONO, color=CRIMSON, font_size=18)
            ion.move_to(pos)
            ions.add(ion)

        note = SerifLabel("proton pumps acidify the endosome", CRIMSON, size=22)
        note.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(endo), FadeIn(endo_label), run_time=0.8)
        self.play(FadeIn(ph_74), run_time=0.6)
        self.play(Create(arrow_down), run_time=0.5)
        self.play(FadeIn(ph_55), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(ion, scale=0.8) for ion in ions],
                              lag_ratio=0.1, run_time=0.9))
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 4.0))


# ---------------------------------------------------------------- B06_ChargeFlip

class B06_ChargeFlip(Scene):
    def construct(self):
        total = DUR["B06"]

        # Left side: neutral state at pH 7.4
        ph_74_label = Text("pH 7.4", font=MONO, color=INK, font_size=26)
        ph_74_label.move_to(LEFT * 4.5 + UP * 2.0)

        head_neutral = Circle(radius=0.55)
        head_neutral.set_fill(INK, 0.75).set_stroke(INK, 2)
        head_neutral.move_to(LEFT * 4.5 + UP * 0.5)

        neutral_chip = LabelChip("neutral", accent=SLATE, size=22)
        neutral_chip.next_to(head_neutral, DOWN, buff=0.28)

        # Right side: cationic state at pH 5.5
        ph_55_label = Text("pH 5.5", font=MONO, color=CRIMSON, font_size=26)
        ph_55_label.move_to(RIGHT * 4.5 + UP * 2.0)

        head_cationic = Circle(radius=0.55)
        head_cationic.set_fill(TEAL, 0.85).set_stroke(TEAL, 2)
        head_cationic.move_to(RIGHT * 4.5 + UP * 0.5)

        # The plus sign sits on the teal circle — use LabelChip for proper accent box
        plus_chip = LabelChip("+", accent=TEAL, size=32)
        plus_chip.move_to(head_cationic.get_center() + DOWN * 0.52)

        cationic_chip = LabelChip("cationic", accent=TEAL, size=22)
        cationic_chip.next_to(head_cationic, DOWN, buff=0.28)

        # GOLD transition arrow and label — no chained animate
        ph_arrow = Arrow(LEFT * 1.2, RIGHT * 1.2, color=GOLD, stroke_width=4, buff=0.05)
        ph_arrow.move_to(ORIGIN + UP * 0.5)

        flip_label = Text("charge flip", font=DISPLAY, color=INK,
                          font_size=22, weight=BOLD)
        flip_label.next_to(ph_arrow, UP, buff=0.18)

        # Gold bar under the label — pre-sized, no animation chaining
        gold_bar = Rectangle(width=flip_label.width + 0.2, height=flip_label.height + 0.16)
        gold_bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        gold_bar.move_to(flip_label.get_center())

        # Show neutral state first
        self.play(FadeIn(ph_74_label), GrowFromCenter(head_neutral),
                  FadeIn(neutral_chip), run_time=1.0)

        # Show pH arrow, gold bar, and label
        self.play(Create(ph_arrow), FadeIn(gold_bar), FadeIn(flip_label), run_time=0.8)

        # Transform neutral head to cationic head (the charge flip — use Transform)
        head_for_transform = head_neutral.copy()
        head_for_transform.move_to(RIGHT * 4.5 + UP * 0.5)
        self.play(FadeIn(ph_55_label),
                  Transform(head_for_transform, head_cationic),
                  FadeIn(cationic_chip), run_time=1.1)
        self.play(FadeIn(plus_chip), run_time=0.5)
        self.wait(max(0.3, total - 3.4))


# ---------------------------------------------------------------- B07_MembraneCrack

class B07_MembraneCrack(Scene):
    def construct(self):
        total = DUR["B07"]

        # Draw the endosome as a circle with a gap
        # We'll create the full circle first, then remove a segment
        endo_full = Circle(radius=1.9)
        endo_full.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 3)
        endo_full.move_to(ORIGIN + LEFT * 1.5 + UP * 0.2)

        endo_label = LabelChip("endosome", accent=CRIMSON, size=20)
        endo_label.next_to(endo_full, UP, buff=0.28)

        # Plus charges inside the endosome (cationic lipids)
        cation_label = Text("+", font=DISPLAY, color=TEAL, font_size=32, weight=BOLD)
        cation_label.move_to(endo_full.get_center() + LEFT * 0.4 + UP * 0.3)
        cation_label2 = Text("+", font=DISPLAY, color=TEAL, font_size=32, weight=BOLD)
        cation_label2.move_to(endo_full.get_center() + RIGHT * 0.2 + DOWN * 0.4)

        self.play(Create(endo_full), FadeIn(endo_label), run_time=0.9)
        self.play(FadeIn(cation_label), FadeIn(cation_label2), run_time=0.6)

        # The crack: FadeOut the full endosome, create a broken arc
        # Arc that covers most of the circle, with a gap on the right side
        endo_cracked = Arc(radius=1.9, start_angle=PI * 0.22, angle=PI * 1.56,
                           color=CRIMSON, stroke_width=3)
        endo_cracked.move_to(endo_full.get_center())

        crack_label = SerifLabel("membrane disrupted", CRIMSON, size=22)
        crack_label.next_to(endo_full, DOWN, buff=0.35)

        self.play(FadeOut(endo_full), FadeIn(endo_cracked), run_time=0.7)
        self.play(FadeIn(crack_label), run_time=0.5)

        # RNA dots stream out through the gap (to the right)
        rna_dots = VGroup()
        escape_positions = [
            RIGHT * 0.85 + UP * 0.5,
            RIGHT * 1.4 + UP * 0.1,
            RIGHT * 1.8 + UP * 0.7,
            RIGHT * 2.3 + DOWN * 0.2,
            RIGHT * 2.7 + UP * 0.4,
            RIGHT * 3.2 + UP * 0.1,
            RIGHT * 3.6 + DOWN * 0.3,
        ]
        for pos in escape_positions:
            # Translate relative to the endosome center
            d = Dot(radius=0.13, color=TEAL)
            d.set_fill(TEAL, 0.9).set_stroke(width=0, opacity=0)
            d.move_to(endo_full.get_center() + pos)
            rna_dots.add(d)

        cytosol_label = LabelChip("cytosol", accent=TEAL, size=20)
        cytosol_label.move_to(endo_full.get_center() + RIGHT * 3.8 + UP * 1.2)

        self.play(LaggedStart(*[GrowFromCenter(d) for d in rna_dots],
                              lag_ratio=0.12, run_time=1.2))
        self.play(FadeIn(cytosol_label), run_time=0.6)
        self.wait(max(0.3, total - 4.5))


# ---------------------------------------------------------------- B08_EscapeFraction

class B08_EscapeFraction(Scene):
    def construct(self):
        total = DUR["B08"]

        # Funnel shape: wide at top (many dots), narrow at bottom (few dots)
        # Represent as two groups of dots with a label

        # Top: 20 crimson dots (trapped cargo)
        trapped_dots = VGroup()
        for i in range(20):
            d = Dot(radius=0.12, color=CRIMSON)
            d.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
            row = i // 5
            col = i % 5
            d.move_to(LEFT * 2.0 + RIGHT * col * 0.38 + UP * 2.2 + DOWN * row * 0.38)
            trapped_dots.add(d)

        trapped_label = LabelChip("internalized", accent=CRIMSON, size=20)
        trapped_label.move_to(LEFT * 4.5 + UP * 2.5)

        # Funnel lines
        funnel_left = Line(LEFT * 2.8 + UP * 1.7, LEFT * 0.5 + DOWN * 0.3,
                           color=INK, stroke_width=2.5)
        funnel_right = Line(RIGHT * 2.6 + UP * 1.7, RIGHT * 0.3 + DOWN * 0.3,
                            color=INK, stroke_width=2.5)
        funnel_bottom = Line(LEFT * 0.5 + DOWN * 0.3, RIGHT * 0.3 + DOWN * 0.3,
                             color=INK, stroke_width=2.5)

        # Rate-limiting label — placed on the right, away from funnel center
        rate_label = SerifLabel("rate-limiting step", INK, size=22)
        rate_label.move_to(RIGHT * 4.8 + UP * 0.7)

        # Escaped: 2 teal dots at the bottom
        escaped_dots = VGroup()
        for i in range(2):
            d = Dot(radius=0.15, color=TEAL)
            d.set_fill(TEAL, 0.9).set_stroke(width=0, opacity=0)
            d.move_to(LEFT * 0.1 + RIGHT * i * 0.45 + DOWN * 1.0)
            escaped_dots.add(d)

        pct_label = Text("~1-2%", font=MONO, color=TEAL, font_size=36, weight=BOLD)
        pct_label.move_to(ORIGIN + DOWN * 1.7)

        escaped_chip = LabelChip("escapes", accent=TEAL, size=20)
        escaped_chip.next_to(pct_label, DOWN, buff=0.28)

        self.play(FadeIn(trapped_label), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d, scale=0.85) for d in trapped_dots],
                              lag_ratio=0.04, run_time=1.0))
        self.play(Create(funnel_left), Create(funnel_right), Create(funnel_bottom),
                  FadeIn(rate_label), run_time=0.9)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in escaped_dots],
                              lag_ratio=0.2, run_time=0.7))
        self.play(FadeIn(pct_label), FadeIn(escaped_chip), run_time=0.7)
        self.wait(max(0.3, total - 3.8))


# ---------------------------------------------------------------- B09_LNPComparison

class B09_LNPComparison(Scene):
    def construct(self):
        total = DUR["B09"]

        # Two columns: LNP-A (neutral, crimson, 8%) and LNP-B (ionizable, teal, 84%)
        # Left column: LNP-A
        lnpa_label = LabelChip("LNP-A  neutral lipid", accent=CRIMSON, size=22)
        lnpa_label.move_to(LEFT * 3.5 + UP * 2.8)

        # Small bar for 8%
        bar_a = Rectangle(width=0.9, height=0.6)
        bar_a.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        bar_a.move_to(LEFT * 3.5 + UP * 0.4)

        pct_a = Text("8%", font=MONO, color=CRIMSON, font_size=34, weight=BOLD)
        pct_a.next_to(bar_a, UP, buff=0.18)

        fate_a = SerifLabel("most RNA digested in lysosomes", CRIMSON, size=20)
        fate_a.next_to(bar_a, DOWN, buff=0.38)

        # Right column: LNP-B
        lnpb_label = LabelChip("LNP-B  ionizable lipid", accent=TEAL, size=22)
        lnpb_label.move_to(RIGHT * 3.5 + UP * 2.8)

        # Tall bar for 84%
        bar_b = Rectangle(width=0.9, height=4.5)
        bar_b.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        bar_b.move_to(RIGHT * 3.5 + DOWN * 0.4)

        pct_b = Text("84%", font=MONO, color=TEAL, font_size=34, weight=BOLD)
        pct_b.next_to(bar_b, UP, buff=0.18)

        fate_b = SerifLabel("RNA escaped, silencing achieved", TEAL, size=20)
        fate_b.next_to(bar_b, DOWN, buff=0.28)

        # Shared label
        shared = Text("same siRNA  |  same cell  |  48 hours", font=SERIF,
                      color=INK, font_size=22, slant=ITALIC)
        shared.to_edge(UP, buff=0.4)

        illustrative = Text("illustrative", font=MONO, color=INK,
                            font_size=18, slant=ITALIC)
        illustrative.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(shared), run_time=0.6)
        self.play(FadeIn(lnpa_label), FadeIn(lnpb_label), run_time=0.7)
        self.play(GrowFromEdge(bar_a, DOWN), FadeIn(pct_a), run_time=0.8)
        self.play(GrowFromEdge(bar_b, DOWN), FadeIn(pct_b), run_time=1.0)
        self.play(FadeIn(fate_a), FadeIn(fate_b), FadeIn(illustrative), run_time=0.7)
        self.wait(max(0.3, total - 3.8))


# ---------------------------------------------------------------- B10_QuoteLock

class B10_QuoteLock(Scene):
    def construct(self):
        _quote_scene(
            self,
            "A vehicle with a pH-sensitive lock that only opens inside the trash bag.",
            "— the mechanism, stated plainly",
            None,
            "pH-sensitive lock",
            DUR["B10"]
        )


# ---------------------------------------------------------------- B11_End

class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Neutral in blood.", font=DISPLAY, color=INK,
                  font_size=36, weight=BOLD)
        t2 = Text("Cationic in the endosome.", font=DISPLAY, color=INK,
                  font_size=36, weight=BOLD)
        t3 = Text("That charge flip is the drug.", font=DISPLAY, color=TEAL,
                  font_size=36, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.22).move_to(UP * 0.25)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        topic = Text("CANCER NANOMEDICINE", font=DISPLAY, color=SLATE,
                     font_size=18)
        topic.next_to(block, DOWN, buff=0.6)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), run_time=0.6)
        self.play(FadeIn(t3), Create(u), run_time=0.9)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.7))
