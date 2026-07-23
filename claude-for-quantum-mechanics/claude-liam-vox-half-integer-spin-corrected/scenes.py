"""vox_scenes.py — Why Spin-½ Exists: The Algebra Is More General Than the Sphere
(vox-half-integer-spin, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = orbital angular momentum (integer, sphere constraint);
           CRIMSON = spin (abstract space, half-integer allowed).
Exclusions: no full ladder derivation, no SU(2)/SO(3), no Dirac, no Pauli matrices.
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
        title = Text("Why Spin-½ Exists:", font=DISPLAY, color=INK, font_size=50)
        sub = Text("The Algebra Is More General Than the Sphere", font=SERIF, color=CRIMSON,
                   font_size=34, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=CRIMSON, stroke_width=2.5)
        rule.next_to(content, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Ladder algebra: all half-integers valid ────────────────────────────
class B02_LadderSpectrum(Scene):
    def construct(self):
        total = _dur("B02", 11.0)
        eyebrow = LabelChip("ANGULAR MOMENTUM ALGEBRA", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Ladder of ℓ values
        labels = ["0", "½", "1", "3⁄2", "2", "5⁄2", "…"]
        colors = [TEAL, CRIMSON, TEAL, CRIMSON, TEAL, CRIMSON, INK]
        rung_group = VGroup()
        for i, (lbl, col) in enumerate(zip(labels, colors)):
            rung = Rectangle(width=1.2, height=0.38).set_fill(col, 0.2).set_stroke(col, 1.5)
            txt = Text(lbl, font=MONO, color=col, font_size=30)
            txt.move_to(rung)
            pair = VGroup(rung, txt)
            rung_group.add(pair)
        rung_group.arrange(RIGHT, buff=0.25)
        rung_group.move_to(UP * 0.3)

        desc = Text("All multiples of ½ are algebraically valid", font=SERIF,
                    color=INK, font_size=28, slant=ITALIC)
        desc.to_edge(DOWN, buff=0.8)

        lbl_int = LabelChip("integer", accent=TEAL, size=22)
        lbl_int.move_to(DOWN * 1.0 + LEFT * 3.5)
        lbl_half = LabelChip("half-integer", accent=CRIMSON, size=22)
        lbl_half.move_to(DOWN * 1.0 + RIGHT * 0.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        for p in rung_group:
            self.play(GrowFromCenter(p[0]), FadeIn(p[1]), run_time=0.25)
        self.play(FadeIn(lbl_int), FadeIn(lbl_half), run_time=0.7)
        self.play(FadeIn(desc, shift=UP * 0.1), run_time=0.7)
        self.wait(total - (0.5 + 7 * 0.25 + 0.7 + 0.7 + 0.3))


# ── B03 — Orbitals vs spin: integer vs half-integer ──────────────────────────
class B03_OrbitalVsSpin(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("THE PUZZLE", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_orb = VGroup(
            LabelChip("atomic orbitals", accent=TEAL, size=22),
            Text("s: ℓ=0", font=MONO, color=TEAL, font_size=30),
            Text("p: ℓ=1", font=MONO, color=TEAL, font_size=30),
            Text("d: ℓ=2", font=MONO, color=TEAL, font_size=30),
            Text("f: ℓ=3", font=MONO, color=TEAL, font_size=30),
            SerifLabel("integers only", accent=TEAL, size=26),
        )
        col_orb.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col_orb.move_to(LEFT * 3.0)

        col_spin = VGroup(
            LabelChip("electron spin", accent=CRIMSON, size=22),
            Text("spin-½", font=MONO, color=CRIMSON, font_size=36),
            Text("half-integer", font=DISPLAY, color=CRIMSON, font_size=30),
            Text("every electron", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC),
        )
        col_spin.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        col_spin.move_to(RIGHT * 2.8)

        div = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_orb[0]), FadeIn(col_spin[0]), run_time=0.6)
        self.play(FadeIn(col_orb[1]), FadeIn(col_orb[2]), FadeIn(col_orb[3]), FadeIn(col_orb[4]),
                  FadeIn(col_spin[1]), run_time=0.8)
        self.play(FadeIn(col_orb[5]), FadeIn(col_spin[2]), FadeIn(col_spin[3]), run_time=0.7)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("Same algebra.", font=DISPLAY, color=INK, font_size=40)
        q2 = Text("Orbitals:  integer only.", font=DISPLAY, color=TEAL, font_size=36)
        q3 = Text("Spin:  half-integer.", font=DISPLAY, color=CRIMSON, font_size=36)
        q4 = Text("Why?", font=SERIF, color=INK, font_size=44, slant=ITALIC)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=2.0)
        rule.next_to(q3, DOWN, buff=0.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q3, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B05 — THE PROBLEM: naive reading of the algebra ──────────────────────────
class B05_NaiveAlgebra(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        naive = VGroup(
            Text("Ladder derivation is complete.", font=SERIF, color=INK, font_size=30),
            Text("Half-integers are algebraically valid.", font=SERIF, color=TEAL, font_size=28),
            Text("Half-integer orbitals should exist.", font=SERIF, color=TEAL, font_size=28),
        )
        naive.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        naive.move_to(UP * 0.5)

        strike = Rectangle(width=7.0, height=0.18).set_fill(CRIMSON, 0.6).set_stroke(width=0, opacity=0)
        strike.move_to(naive[2].get_center())

        conclusion = Text("BUT: no half-integer orbitals in any atom", font=DISPLAY,
                          color=CRIMSON, font_size=30)
        conclusion.to_edge(DOWN, buff=1.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(naive[0]), run_time=0.7)
        self.play(FadeIn(naive[1]), run_time=0.7)
        self.play(FadeIn(naive[2]), run_time=0.7)
        self.play(Create(strike), run_time=0.5)
        self.play(FadeIn(conclusion, shift=UP * 0.15), run_time=0.7)
        self.wait(total - 5.0)


# ── B06 — MECHANISM: e^{imφ} single-valuedness ───────────────────────────────
class B06_SingleValuedness(Scene):
    def construct(self):
        total=_dur("B06",12); title=LabelChip("SCALAR ORBITAL BOUNDARY CONDITION",accent=TEAL,size=22); title.to_corner(UL,buff=.6)
        circle=Circle(radius=1.5,color=TEAL).shift(LEFT*3); arrow=Arrow(LEFT*3,LEFT*1.5,color=TEAL,buff=0)
        step=Text("phi  →  phi + 2 pi",font=MONO,font_size=34,color=INK).move_to(RIGHT*2+UP*1.3)
        req=Text("exp(2 pi i m) = 1",font=MONO,font_size=38,color=TEAL).move_to(RIGHT*2)
        ans=Text("therefore m is an integer",font=MONO,font_size=32,color=INK).move_to(RIGHT*2+DOWN*1.3)
        self.play(FadeIn(title),Create(circle),GrowArrow(arrow),run_time=1); self.play(Rotate(arrow,angle=TAU,about_point=LEFT*3),run_time=1.4); self.play(FadeIn(step,req,ans),run_time=.8); self.wait(max(.1,total-3.2))


# ── B07 — MECHANISM: m=½ flips sign after 2π ─────────────────────────────────
class B07_HalfIntegerFlip(Scene):
    def construct(self):
        total=_dur("B07",11); title=LabelChip("TRY m = 1/2",accent=CRIMSON,size=22); title.to_corner(UL,buff=.6)
        start=Text("exp(i phi / 2)",font=MONO,font_size=40,color=INK).move_to(UP*1.4+LEFT*3)
        arrow=Arrow(LEFT*.7+UP*1.4,RIGHT*.25+UP*1.4,color=CRIMSON,buff=0)
        after=Text("- exp(i phi / 2)",font=MONO,font_size=38,color=CRIMSON).move_to(UP*1.4+RIGHT*3.5)
        factor=Text("exp(i pi) = -1",font=MONO,font_size=38,color=CRIMSON).move_to(DOWN*.2)
        result=Text("fails scalar orbital single-valuedness",font=MONO,font_size=31,color=INK).move_to(DOWN*2)
        self.play(FadeIn(title,start),GrowArrow(arrow),run_time=1); self.play(FadeIn(after,factor,result),run_time=.8); self.wait(max(.1,total-1.8))


# ── B08 — MECHANISM: spin has no φ ───────────────────────────────────────────
class B08_SpinNoAngle(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        eyebrow = LabelChip("SPINOR REPRESENTATION", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_orb = VGroup(
            LabelChip("orbital", accent=TEAL, size=22),
            Text("position space", font=SERIF, color=TEAL, font_size=26),
            Text("azimuthal angle φ", font=MONO, color=TEAL, font_size=28),
            Text("e^{2πim}=1 required", font=MONO, color=TEAL, font_size=26),
            Text("→ integer m only", font=DISPLAY, color=TEAL, font_size=28),
        )
        col_orb.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        col_orb.move_to(LEFT * 3.0)

        col_spin = VGroup(
            LabelChip("spin", accent=CRIMSON, size=22),
            Text("internal spinor space", font=SERIF, color=CRIMSON, font_size=26),
            Text("not orbital φ dependence", font=MONO, color=CRIMSON, font_size=25),
            Text("2π sign flip allowed", font=MONO, color=CRIMSON, font_size=26),
            Text("→ half-integer allowed", font=DISPLAY, color=CRIMSON, font_size=28),
        )
        col_spin.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        col_spin.move_to(RIGHT * 2.8)

        div = Line(UP * 2.2, DOWN * 2.2, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_orb[0]), FadeIn(col_spin[0]), run_time=0.6)
        self.play(FadeIn(col_orb[1]), FadeIn(col_spin[1]), run_time=0.6)
        self.play(FadeIn(col_orb[2]), FadeIn(col_spin[2]), run_time=0.6)
        self.play(FadeIn(col_orb[3]), FadeIn(col_spin[3]), run_time=0.6)
        self.play(FadeIn(col_orb[4]), FadeIn(col_spin[4]), run_time=0.7)
        self.wait(total - 5.0)


# ── B09 — Implication: integer restriction is a sphere property ───────────────
class B09_Implication(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        lines = VGroup(
            Text("The integer restriction is a sphere property.", font=SERIF, color=TEAL, font_size=30),
            Text("Not an algebra property.", font=DISPLAY, color=INK, font_size=34),
            Text("Angular momentum eigenstates exist for", font=SERIF, color=INK, font_size=28),
            Text("every half-integer.", font=DISPLAY, color=CRIMSON, font_size=36),
            Text("Orbital angular momentum adds a constraint", font=SERIF, color=INK, font_size=26),
            Text("that the algebra never required.", font=SERIF, color=INK, font_size=26, slant=ITALIC),
        )
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        lines.move_to(ORIGIN).shift(DOWN * 0.2)

        rule_top = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.5)
        rule_top.next_to(lines, UP, buff=0.3)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(rule_top), run_time=0.5)
        self.play(FadeIn(lines[0]), run_time=0.6)
        self.play(FadeIn(lines[1], shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(lines[2]), FadeIn(lines[3], shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(lines[4]), FadeIn(lines[5]), run_time=0.7)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE ─────────────────────────────────────────────────────────
class Legacy10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_fail = VGroup(
            LabelChip("orbital attempt", accent=TEAL, size=22),
            Text("write e^{iφ/2}", font=MONO, color=TEAL, font_size=30),
            Text("φ → φ+2π:", font=MONO, color=INK, font_size=28),
            Text("e^{iφ/2} → −e^{iφ/2}", font=MONO, color=CRIMSON, font_size=30),
            Text("✗  sign flip", font=DISPLAY, color=CRIMSON, font_size=28),
            SerifLabel("ℓ=½ forbidden in position space", accent=TEAL, size=22),
        )
        col_fail.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        col_fail.move_to(LEFT * 2.8)

        col_spin = VGroup(
            LabelChip("spin", accent=CRIMSON, size=22),
            Text("spinor-valued ψ(x)", font=MONO, color=CRIMSON, font_size=30),
            Text("internal, not orbital motion", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
            Text("2π sign flip allowed", font=DISPLAY, color=CRIMSON, font_size=27),
        )
        col_spin.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        col_spin.move_to(RIGHT * 2.8 + DOWN * 0.3)

        div = Line(UP * 2.2, DOWN * 2.4, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_fail[0]), FadeIn(col_spin[0]), run_time=0.6)
        self.play(FadeIn(col_fail[1]), FadeIn(col_spin[1]), run_time=0.6)
        self.play(FadeIn(col_fail[2]), FadeIn(col_spin[2]), run_time=0.6)
        self.play(FadeIn(col_fail[3]), FadeIn(col_spin[3]), run_time=0.7)
        self.play(FadeIn(col_fail[4]), run_time=0.5)
        self.play(FadeIn(col_fail[5]), run_time=0.6)
        self.wait(total - 5.5)

class B10_Caveat(Scene):
    def construct(self):
        total=_dur("B10",13); title=LabelChip("IMPORTANT CAVEAT",accent=SLATE,size=22); title.to_corner(UL,buff=.6)
        left=VGroup(Text("particle with spin",font=DISPLAY,font_size=34,color=INK),Text("can have psi(x)",font=MONO,font_size=36,color=TEAL),Text("with spinor components",font=SERIF,font_size=29,color=TEAL)).arrange(DOWN,buff=.45).shift(LEFT*3)
        right=VGroup(Text("intrinsic spin",font=DISPLAY,font_size=34,color=INK),Text("is an internal degree",font=MONO,font_size=31,color=CRIMSON),Text("not orbital motion in phi",font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.45).shift(RIGHT*3)
        div=Line(UP*2,DOWN*2,color=INK); self.play(FadeIn(title),Create(div),FadeIn(left,right),run_time=1.2); self.wait(max(.1,total-1.2))


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("Algebra: all half-integers allowed.", font=MONO, color=INK, font_size=30)
        line1.move_to(UP * 0.9)
        line2 = Text("Orbital: e^{2πim}=1  →  integers only.", font=MONO, color=TEAL, font_size=30)
        line2.move_to(UP * 0.2)
        line3 = Text("Spinor: 2π sign flip allowed.", font=MONO, color=CRIMSON, font_size=30)
        line3.move_to(DOWN * 0.5)
        sub = Text("The representation adds conditions beyond the algebra.", font=SERIF,
                   color=INK, font_size=24, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.7)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.5)

class B12_YourTurn(Scene):
    def construct(self):
        total=_dur("B12",12); title=LabelChip("YOUR TURN",accent=SLATE,size=24); title.to_corner(UL,buff=.6)
        q=Text("e^(2π i m)",font=MONO,font_size=44,color=INK).move_to(UP*1.5)
        one=Text("m = 1  →  +1",font=MONO,font_size=38,color=TEAL).move_to(LEFT*2.6)
        half=Text("m = 1/2  →  -1",font=MONO,font_size=38,color=CRIMSON).move_to(RIGHT*2.6)
        ans=Text("scalar orbital condition: integer",font=MONO,font_size=32,color=INK).move_to(DOWN*2)
        self.play(FadeIn(title,q),run_time=.8); self.wait(total*.35); self.play(FadeIn(one,half,ans),run_time=.8); self.wait(max(.1,total*.65-1.6))
