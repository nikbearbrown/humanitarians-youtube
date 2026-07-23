"""vox_scenes.py — Why One Extra Neutron Makes You 1000x Harder to Superflow
(vox-helium-superfluidity, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. B02 is STILL·ai — no scene here.
Color law: TEAL = bosons/He-4/pile-up; CRIMSON = fermions/He-3/Pauli-blocked.
Exclusions: no BEC formula, no Cooper-pair math, no spin-statistics theorem.
"""
import sys, json, pathlib, numpy as np
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid, fallback=9.0):
    return DUR.get(bid, fallback)


# ── B01 — Title card ─────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        total = _dur("B01", 10.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        title = Text("One Extra Neutron.", font=DISPLAY, color=INK, font_size=52)
        sub = Text("1000x harder to superflow.", font=SERIF, color=CRIMSON, font_size=38, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.move_to(ORIGIN).shift(DOWN * 0.2)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=CRIMSON, stroke_width=2.5)
        rule.next_to(content, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B03 — Cold open: He-3 temperature journey ────────────────────────────────
class B03_TempJourney(Scene):
    def construct(self):
        total = _dur("B03", 12.0)
        # Temperature axis from 2K down to 0.001K (log scale represented)
        eyebrow = LabelChip("He-3 cooling", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Two side-by-side temperature comparisons
        col_he4 = VGroup(
            LabelChip("He-4", accent=TEAL, size=26),
            Text("2.17 K", font=MONO, color=TEAL, font_size=44),
            SerifLabel("SUPERFLUID", accent=TEAL, size=28),
        )
        col_he4.arrange(DOWN, buff=0.45)
        col_he3 = VGroup(
            LabelChip("He-3", accent=CRIMSON, size=26),
            Text("0.0025 K", font=MONO, color=CRIMSON, font_size=44),
            SerifLabel("finally superfluid", accent=CRIMSON, size=28),
        )
        col_he3.arrange(DOWN, buff=0.45)
        cols = VGroup(col_he4, col_he3)
        cols.arrange(RIGHT, buff=2.4)
        cols.move_to(ORIGIN)
        div = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=1.5)
        div.move_to(cols)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(col_he4[0]), FadeIn(col_he3[0]), Create(div), run_time=0.8)
        self.play(FadeIn(col_he4[1]), FadeIn(col_he3[1]), run_time=0.9)
        self.wait(0.5)
        self.play(FadeIn(col_he4[2]), FadeIn(col_he3[2]), run_time=0.8)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("He-4 superflows at 2 K.", font=DISPLAY, color=TEAL, font_size=36)
        q2 = Text("He-3 needs 0.0025 K.", font=DISPLAY, color=CRIMSON, font_size=36)
        q3 = Text("One neutron apart.", font=DISPLAY, color=INK, font_size=36)
        q4 = Text("Why 870 times colder?", font=SERIF, color=INK, font_size=38, slant=ITALIC)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=2.0)
        rule.next_to(q3, DOWN, buff=0.18)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1), run_time=0.7)
        self.play(FadeIn(q2), run_time=0.7)
        self.play(FadeIn(q3), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.12), run_time=0.8)
        self.wait(total - 4.5)


# ── B05 — THE PROBLEM: naive mass argument ────────────────────────────────────
class B05_NaiveMass(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE EXPECTATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        naive = VGroup(
            Text("He-3 is lighter", font=SERIF, color=INK, font_size=34),
            Text("lighter = easier to cool", font=SERIF, color=TEAL, font_size=32),
            Text("should transition SOONER", font=SERIF, color=TEAL, font_size=32),
        )
        naive.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        naive.move_to(UP * 0.5 + LEFT * 0.5)
        # X mark on the naive prediction
        x_label = Text("BUT: He-3 transitions 870x LATER", font=DISPLAY, color=CRIMSON, font_size=32)
        x_label.to_edge(DOWN, buff=1.2)

        strike_box = Rectangle(width=7.0, height=0.18).set_fill(CRIMSON, 0.6).set_stroke(width=0, opacity=0)
        strike_box.move_to(naive[2].get_center())
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(naive[0]), run_time=0.7)
        self.play(FadeIn(naive[1]), run_time=0.7)
        self.play(FadeIn(naive[2]), run_time=0.7)
        self.play(Create(strike_box), run_time=0.5)
        self.play(FadeIn(x_label, shift=UP * 0.15), run_time=0.8)
        self.wait(total - 5.0)


# ── B06 — MECHANISM section card ─────────────────────────────────────────────
class B06_MechanismCard(Scene):
    def construct(self):
        total = _dur("B06", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        heading = Text("The Mechanism:", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Count the fermions inside.", font=SERIF, color=INK, font_size=36, slant=ITALIC)
        content = VGroup(heading, sub)
        content.arrange(DOWN, buff=0.5)
        content.move_to(ORIGIN)

        rule = Line(LEFT * 4.0, RIGHT * 4.0, color=SLATE, stroke_width=2.5)
        rule.next_to(heading, DOWN, buff=0.3)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.wait(total - 3.5)


# ── B07 — He-4: even count, boson ────────────────────────────────────────────
class B07_He4Boson(Scene):
    def construct(self):
        total = _dur("B07", 13.0)
        eyebrow = LabelChip("He-4", accent=TEAL, size=24)
        eyebrow.to_corner(UL, buff=0.6)
        # Count display
        count_row = VGroup(
            Text("2p + 2n + 2e", font=MONO, color=INK, font_size=36),
            Text("=", font=DISPLAY, color=INK, font_size=36),
            Text("6", font=MONO, color=TEAL, font_size=56),
            Text("fermions", font=SERIF, color=INK, font_size=32),
        )
        count_row.arrange(RIGHT, buff=0.4)
        count_row.move_to(UP * 0.8)
        even_label = LabelChip("EVEN", accent=TEAL, size=26)
        even_label.move_to(UP * 0.0)
        boson_label = Text("BOSON", font=DISPLAY, color=TEAL, font_size=48)
        boson_label.move_to(DOWN * 0.9)
        pileup = SerifLabel("Bosons can all pile into one state", accent=TEAL, size=28)
        pileup.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(count_row[0]), FadeIn(count_row[1]), run_time=0.7)
        self.play(FadeIn(count_row[2]), FadeIn(count_row[3]), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(even_label, shift=DOWN * 0.1), run_time=0.6)
        self.play(count_row[2].animate.scale(1.1), run_time=0.3)
        self.play(count_row[2].animate.scale(1.0 / 1.1), run_time=0.3)
        self.play(FadeIn(boson_label, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(pileup, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.5)


# ── B08 — He-3: odd count, fermion ───────────────────────────────────────────
class B08_He3Fermion(Scene):
    def construct(self):
        total = _dur("B08", 13.0)
        eyebrow = LabelChip("He-3", accent=CRIMSON, size=24)
        eyebrow.to_corner(UL, buff=0.6)
        count_row = VGroup(
            Text("2p + 1n + 2e", font=MONO, color=INK, font_size=36),
            Text("=", font=DISPLAY, color=INK, font_size=36),
            Text("5", font=MONO, color=CRIMSON, font_size=56),
            Text("fermions", font=SERIF, color=INK, font_size=32),
        )
        count_row.arrange(RIGHT, buff=0.4)
        count_row.move_to(UP * 0.8)
        odd_label = LabelChip("ODD", accent=CRIMSON, size=26)
        odd_label.move_to(UP * 0.0)
        fermion_label = Text("FERMION", font=DISPLAY, color=CRIMSON, font_size=48)
        fermion_label.move_to(DOWN * 0.9)
        pauli = SerifLabel("One per state — Pauli exclusion", accent=CRIMSON, size=28)
        pauli.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(count_row[0]), FadeIn(count_row[1]), run_time=0.7)
        self.play(FadeIn(count_row[2]), FadeIn(count_row[3]), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(odd_label, shift=DOWN * 0.1), run_time=0.6)
        self.play(count_row[2].animate.scale(1.1), run_time=0.3)
        self.play(count_row[2].animate.scale(1.0 / 1.1), run_time=0.3)
        self.play(FadeIn(fermion_label, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(pauli, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.5)


# ── B09 — Boson pile-up into ground state ────────────────────────────────────
class B09_BosonPileup(Scene):
    def construct(self):
        total = _dur("B09", 12.0)
        eyebrow = LabelChip("He-4 BOSONS", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Energy rungs
        ground = Rectangle(width=4.0, height=0.3).set_fill(TEAL, 0.4).set_stroke(TEAL, 2.5)
        ground.move_to(DOWN * 1.8)
        ground_lbl = Text("ground state", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        ground_lbl.next_to(ground, RIGHT, buff=0.3)
        e1 = Rectangle(width=4.0, height=0.3).set_fill(SLATE, 0.2).set_stroke(SLATE, 1.5)
        e1.move_to(DOWN * 0.6)
        e2 = Rectangle(width=4.0, height=0.3).set_fill(SLATE, 0.2).set_stroke(SLATE, 1.5)
        e2.move_to(UP * 0.6)
        e3 = Rectangle(width=4.0, height=0.3).set_fill(SLATE, 0.2).set_stroke(SLATE, 1.5)
        e3.move_to(UP * 1.8)
        # Dots piling into ground state
        dots = VGroup(*[Dot(radius=0.13, color=TEAL).move_to(ground.get_center() + RIGHT * (-1.4 + i * 0.45))
                        for i in range(7)])
        pile_label = LabelChip("ALL IN GROUND STATE", accent=TEAL, size=22)
        pile_label.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(ground), FadeIn(ground_lbl), Create(e1), Create(e2), Create(e3), run_time=0.9)
        for d in dots:
            self.play(FadeIn(d, shift=DOWN * 0.3), run_time=0.25)
        self.play(FadeIn(pile_label, shift=UP * 0.1), run_time=0.7)
        self.wait(total - (0.5 + 0.9 + 7 * 0.25 + 0.7 + 0.5))


# ── B10 — Fermion stack: one per rung ─────────────────────────────────────────
class B10_FermionStack(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("He-3 FERMIONS", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Stack of energy rungs each holding one dot
        rungs = []
        rung_dots = []
        for i in range(6):
            y = -2.0 + i * 0.75
            r = Rectangle(width=3.0, height=0.25).set_fill(SLATE, 0.2).set_stroke(SLATE, 1.5)
            r.move_to(LEFT * 1.5 + UP * y)
            rungs.append(r)
            d = Dot(radius=0.13, color=CRIMSON).move_to(LEFT * 1.5 + UP * y)
            rung_dots.append(d)
        pauli_lbl = SerifLabel("one per rung — Pauli excluded", accent=CRIMSON, size=28)
        pauli_lbl.move_to(RIGHT * 3.0)
        no_bec = Text("No ground-state crowd.", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        no_bec.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(eyebrow), run_time=0.5)
        for r in rungs:
            self.play(Create(r), run_time=0.3)
        for d in rung_dots:
            self.play(FadeIn(d, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(pauli_lbl), run_time=0.7)
        self.play(FadeIn(no_bec, shift=UP * 0.1), run_time=0.6)
        self.wait(total - (0.5 + 6 * 0.3 + 6 * 0.3 + 0.7 + 0.6 + 0.3))


# ── B11 — Implication: Cooper pairs needed ────────────────────────────────────
class B11_CooperPairs(Scene):
    def construct(self):
        total = _dur("B11", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # He-3 path: pair up to make composite boson
        pair_label = VGroup(
            Text("He-3 fermions", font=SERIF, color=CRIMSON, font_size=32),
            Text("pair at millikelvin", font=SERIF, color=INK, font_size=30),
            Text("Cooper pair = composite boson", font=MONO, color=TEAL, font_size=28),
            Text("THEN can superflow", font=DISPLAY, color=TEAL, font_size=32),
        )
        pair_label.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        pair_label.move_to(ORIGIN).shift(DOWN * 0.2)

        rule_top = Line(LEFT * 4.5, RIGHT * 4.5, color=CRIMSON, stroke_width=1.5)
        rule_top.next_to(pair_label, UP, buff=0.25)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(rule_top), run_time=0.5)
        self.play(FadeIn(pair_label[0]), run_time=0.7)
        self.play(FadeIn(pair_label[1]), run_time=0.7)
        self.play(FadeIn(pair_label[2], shift=RIGHT * 0.1), run_time=0.7)
        self.play(FadeIn(pair_label[3], shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B12 — THE EXAMPLE ─────────────────────────────────────────────────────────
class B12_Example(Scene):
    def construct(self):
        total = _dur("B12", 15.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Two columns: He-4 vs He-3 lab scenario
        col_he4 = VGroup(
            LabelChip("He-4", accent=TEAL, size=24),
            Text("2 K cryostat", font=MONO, color=TEAL, font_size=28),
            Text("superfluid in minutes", font=SERIF, color=TEAL, font_size=26, slant=ITALIC),
        )
        col_he4.arrange(DOWN, buff=0.42)
        col_he3 = VGroup(
            LabelChip("He-3", accent=CRIMSON, size=24),
            Text("dilution refrigerator", font=MONO, color=CRIMSON, font_size=28),
            Text("3 months to commission", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC),
        )
        col_he3.arrange(DOWN, buff=0.42)
        cols = VGroup(col_he4, col_he3)
        cols.arrange(RIGHT, buff=2.5)
        cols.move_to(ORIGIN)
        div = Line(UP * 1.8, DOWN * 1.8, color=INK, stroke_width=1.5)
        div.move_to(cols)
        same_label = SerifLabel("same element, one neutron", accent=GOLD, size=28)
        same_label.to_edge(DOWN, buff=0.7)
        same_label[0].set_color(INK)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(col_he4[0]), FadeIn(col_he3[0]), Create(div), run_time=0.8)
        self.play(FadeIn(col_he4[1]), FadeIn(col_he3[1]), run_time=0.8)
        self.play(FadeIn(col_he4[2]), FadeIn(col_he3[2]), run_time=0.8)
        self.play(FadeIn(same_label, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B13 — RECAP endcard ──────────────────────────────────────────────────────
class B13_Endcard(Scene):
    def construct(self):
        total = _dur("B13", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("Even count  =  boson  =  pile up.", font=MONO, color=TEAL, font_size=36)
        line1.move_to(UP * 0.7)
        line2 = Text("Odd count  =  fermion  =  one per rung.", font=MONO, color=CRIMSON, font_size=36)
        line2.move_to(DOWN * 0.1)
        sub = Text("One neutron decides which machine you need.", font=SERIF,
                   color=INK, font_size=28, slant=ITALIC)
        sub.to_edge(DOWN, buff=1.0)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)
        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.8)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.7)
        self.wait(total - 4.0)
