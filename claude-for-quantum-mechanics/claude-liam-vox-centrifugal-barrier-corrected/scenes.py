"""vox_scenes.py — Why the Centrifugal Barrier Is Kinetic Energy Pretending to Be a Force
(vox-centrifugal-kinetic, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = kinetic energy (true origin); CRIMSON = centrifugal term on potential side.
Exclusions: no spherical Laplacian derivation, no Laguerre polynomials.
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
        title = Text("Why the Centrifugal Barrier", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Is Kinetic Energy Pretending to Be a Force", font=SERIF,
                   color=CRIMSON, font_size=34, slant=ITALIC)
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


# ── B02 — Cold open: centrifugal term in p-orbital equation ──────────────────
class B02_CentrifugalInEquation(Scene):
    def construct(self):
        total = _dur("B02", 11.0)
        eyebrow = LabelChip("hydrogen p-orbital", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Effective potential equation
        eq = Text("V_eff = V(r)  +  ℏ²ℓ(ℓ+1) / 2mr²", font=MONO, color=INK, font_size=36)
        eq.move_to(UP * 1.0)

        arrow_coulomb = Arrow(eq.get_left() + DOWN * 0.6, eq.get_left() + DOWN * 0.6 + DOWN * 0.5,
                              color=TEAL, stroke_width=2.5, buff=0)
        lbl_coulomb = Text("Coulomb attraction", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        lbl_coulomb.next_to(arrow_coulomb.get_end(), DOWN, buff=0.1)

        # Highlight centrifugal term
        cent_box = Rectangle(width=3.6, height=0.55).set_stroke(CRIMSON, 2.5).set_fill(CRIMSON, 0.08)
        cent_box.move_to(eq.get_right() + LEFT * 2.0)

        cent_lbl = Text("centrifugal barrier", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        cent_lbl.next_to(cent_box, DOWN, buff=0.3)

        s_note = Text("for ℓ=0 (s-orbital): barrier = 0", font=MONO, color=TEAL, font_size=26)
        s_note.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(eq, shift=DOWN * 0.1), run_time=0.9)
        self.play(Create(cent_box), run_time=0.6)
        self.play(FadeIn(cent_lbl), run_time=0.6)
        self.play(FadeIn(s_note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B03 — Cold open: effective potential shape ────────────────────────────────
class B03_EffectivePotential(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("effective potential", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two energy rungs showing the potential floor difference
        col_s = VGroup(
            LabelChip("s-orbital  ℓ=0", accent=TEAL, size=22),
            Text("no barrier", font=MONO, color=TEAL, font_size=28),
            Text("no 1/r² exclusion", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        col_s.arrange(DOWN, buff=0.4)
        col_s.move_to(LEFT * 3.0)

        col_p = VGroup(
            LabelChip("p-orbital  ℓ=1", accent=CRIMSON, size=22),
            Text("centrifugal barrier", font=MONO, color=CRIMSON, font_size=28),
            Text("suppressed near r=0", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        col_p.arrange(DOWN, buff=0.4)
        col_p.move_to(RIGHT * 3.0)

        div = Line(UP * 1.8, DOWN * 1.8, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = SerifLabel("mean radius also depends on n and V(r)", accent=CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_s[0]), FadeIn(col_p[0]), run_time=0.6)
        self.play(FadeIn(col_s[1]), FadeIn(col_p[1]), run_time=0.6)
        self.play(FadeIn(col_s[2]), FadeIn(col_p[2]), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("The centrifugal term repels", font=DISPLAY, color=CRIMSON, font_size=36)
        q2 = Text("like a potential.", font=DISPLAY, color=CRIMSON, font_size=36)
        q3 = Text("But it came from L²/2mr².", font=MONO, color=INK, font_size=34)
        q4 = Text("Kinetic energy — or a force?", font=SERIF, color=INK, font_size=36, slant=ITALIC)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=2.0)
        rule.next_to(q3, DOWN, buff=0.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q3, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: naive reading ─────────────────────────────────────────
class B05_NaiveReading(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        eq_layout = VGroup(
            Text("V_eff  =  V(r)  +  [centrifugal]", font=MONO, color=INK, font_size=36),
        )
        eq_layout.move_to(UP * 0.9)

        arrow_rhs = Arrow(UP * 0.3, DOWN * 0.0, color=CRIMSON, stroke_width=2.5, buff=0)
        arrow_rhs.move_to(RIGHT * 1.8 + UP * 0.5)

        rhs_lbl = Text("sits on V(r) side", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        rhs_lbl.move_to(RIGHT * 1.8 + DOWN * 0.1)

        repel = Text("repels electron from nucleus", font=SERIF, color=CRIMSON, font_size=26)
        repel.move_to(DOWN * 0.8)

        conclusion_naive = Text("must be a force →", font=DISPLAY, color=CRIMSON, font_size=30)
        conclusion_naive.to_edge(DOWN, buff=1.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(eq_layout), run_time=0.8)
        self.play(GrowArrow(arrow_rhs), FadeIn(rhs_lbl), run_time=0.7)
        self.play(FadeIn(repel), run_time=0.6)
        self.play(FadeIn(conclusion_naive, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 5.0)


# ── B06 — MECHANISM: 3D KE splits into radial + angular ──────────────────────
class B06_KineticEnergySplit(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        ke_full = Text("T = T_radial  +  L²/2mr²", font=MONO, color=INK, font_size=40)
        ke_full.move_to(UP * 0.9)

        rule_ke = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.5)
        rule_ke.next_to(ke_full, DOWN, buff=0.3)

        lbl_rad = LabelChip("radial KE", accent=SLATE, size=22)
        lbl_rad.move_to(DOWN * 0.2 + LEFT * 2.5)

        lbl_ang = LabelChip("angular KE", accent=TEAL, size=22)
        lbl_ang.move_to(DOWN * 0.2 + RIGHT * 2.5)

        note = VGroup(
            Text("Both are kinetic energy.", font=SERIF, color=TEAL, font_size=28),
            Text("It may later serve as an effective potential.", font=SERIF, color=TEAL, font_size=28),
        )
        note.arrange(DOWN, buff=0.3)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(ke_full, shift=UP * 0.1), run_time=0.9)
        self.play(Create(rule_ke), run_time=0.5)
        self.play(FadeIn(lbl_rad), FadeIn(lbl_ang), run_time=0.7)
        self.play(FadeIn(note[0]), run_time=0.6)
        self.play(FadeIn(note[1]), run_time=0.6)
        self.wait(total - 5.0)


# ── B07 — MECHANISM: project onto ℓ eigenstate ───────────────────────────────
class B07_ProjectOntoEigenstate(Scene):
    def construct(self):
        total = _dur("B07", 11.0)
        eyebrow = LabelChip("project onto ℓ eigenstate", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        step1 = Text("L²  acts on  |ℓ,m⟩:", font=MONO, color=INK, font_size=34)
        step1.move_to(UP * 1.3)

        arrow_down = Arrow(LEFT * 0.0 + UP * 0.7, LEFT * 0.0 + UP * 0.1,
                           color=TEAL, stroke_width=2.5, buff=0)

        step2 = Text("L²  →  ℏ²ℓ(ℓ+1)", font=MONO, color=TEAL, font_size=36)
        step2.move_to(DOWN * 0.4)

        rule_res = Line(LEFT * 4.0, RIGHT * 4.0, color=TEAL, stroke_width=1.5)
        rule_res.move_to(DOWN * 1.1)

        result = Text("angular KE  =  ℏ²ℓ(ℓ+1) / 2mr²", font=MONO, color=TEAL, font_size=32)
        result.move_to(DOWN * 1.7)

        still_ke = SerifLabel("still kinetic energy — just a number now", accent=TEAL, size=26)
        still_ke.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(step1), run_time=0.7)
        self.play(GrowArrow(arrow_down), run_time=0.5)
        self.play(FadeIn(step2, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule_res), run_time=0.4)
        self.play(FadeIn(result), run_time=0.6)
        self.play(FadeIn(still_ke, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B08 — MECHANISM: migration to potential side ──────────────────────────────
class B08_Migration(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        eyebrow = LabelChip("GROUPED INTO V-effective", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Before: KE side
        before = VGroup(
            LabelChip("KINETIC side", accent=TEAL, size=22),
            Text("T_radial  +  ℏ²ℓ(ℓ+1)/2mr²", font=MONO, color=TEAL, font_size=28),
        )
        before.arrange(DOWN, buff=0.35)
        before.move_to(UP * 0.8 + LEFT * 0.5)

        arrow_migr = Arrow(before.get_bottom() + DOWN * 0.1, before.get_bottom() + DOWN * 1.0,
                           color=INK, stroke_width=2.5, buff=0)

        # After: V side
        after = VGroup(
            LabelChip("V(r) side (rearranged)", accent=CRIMSON, size=22),
            Text("V_eff  =  V(r)  +  ℏ²ℓ(ℓ+1)/2mr²", font=MONO, color=CRIMSON, font_size=28),
        )
        after.arrange(DOWN, buff=0.35)
        after.move_to(DOWN * 1.2 + LEFT * 0.5)

        note = Text("effective-potential role · angular-kinetic origin", font=SERIF,
                    color=INK, font_size=26, slant=ITALIC)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(before), run_time=0.8)
        self.play(GrowArrow(arrow_migr), run_time=0.5)
        self.play(FadeIn(after, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B09 — Implication: ℓ controls barrier ────────────────────────────────────
class B09_Implication(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        rungs = VGroup()
        for i, (ell, col) in enumerate([(0, TEAL), (1, CRIMSON), (2, CRIMSON)]):
            lbl = f"ℓ={ell}"
            bar = Rectangle(width=3.0 + i * 1.0, height=0.4).set_fill(col, 0.25).set_stroke(col, 1.5)
            txt = Text(lbl, font=MONO, color=col, font_size=26)
            txt.move_to(bar.get_left() + RIGHT * 0.4)
            barrier_txt = Text(f"barrier = ℏ²·{ell}·{ell+1}/2mr²", font=MONO,
                               color=col, font_size=22)
            barrier_txt.next_to(bar, RIGHT, buff=0.3)
            pair = VGroup(bar, txt, barrier_txt)
            rungs.add(pair)
        rungs.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rungs.move_to(ORIGIN + UP * 0.2)

        note = Text("higher ell means stronger small-r suppression", font=SERIF,
                    color=TEAL, font_size=24, slant=ITALIC)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        for rung in rungs:
            self.play(GrowFromCenter(rung[0]), FadeIn(rung[1]), FadeIn(rung[2]), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - (0.5 + 3 * 0.6 + 0.7 + 0.3))


# ── B10 — THE EXAMPLE ─────────────────────────────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_wrong = VGroup(
            LabelChip("student's first label", accent=CRIMSON, size=22),
            Text("ℏ²ℓ(ℓ+1)/2mr²", font=MONO, color=CRIMSON, font_size=28),
            Text("= new repulsive force?", font=DISPLAY, color=CRIMSON, font_size=26),
        )
        col_wrong.arrange(DOWN, buff=0.38)
        col_wrong.move_to(LEFT * 2.8 + DOWN * 0.2)

        col_right = VGroup(
            LabelChip("traced back to origin", accent=TEAL, size=22),
            Text("L² / 2mr²  (eigenstate)", font=MONO, color=TEAL, font_size=28),
            Text("= effective barrier, kinetic origin", font=DISPLAY, color=TEAL, font_size=23),
        )
        col_right.arrange(DOWN, buff=0.38)
        col_right.move_to(RIGHT * 2.8 + DOWN * 0.2)

        div = Line(UP * 0.8, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN + DOWN * 0.6)

        rule_top = Line(LEFT * 5.0, RIGHT * 5.0, color=SLATE, stroke_width=1.5)
        rule_top.move_to(UP * 1.4)
        setup = Text("V_eff for ℓ=1 in hydrogen", font=MONO, color=INK, font_size=28)
        setup.move_to(UP * 1.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(setup), Create(rule_top), run_time=0.6)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_wrong[0]), FadeIn(col_right[0]), run_time=0.6)
        self.play(FadeIn(col_wrong[1]), FadeIn(col_right[1]), run_time=0.7)
        self.play(FadeIn(col_wrong[2]), FadeIn(col_right[2]), run_time=0.7)
        self.wait(total - 5.0)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("L²/2mr²  =  angular kinetic energy.", font=MONO, color=TEAL, font_size=28)
        line1.move_to(UP * 0.9)
        line2 = Text("Projected onto eigenstate:", font=MONO, color=INK, font_size=26)
        line2.move_to(UP * 0.2)
        line3 = Text("ℏ²ℓ(ℓ+1)/2mr²  joins V-effective.", font=MONO, color=CRIMSON, font_size=28)
        line3.move_to(DOWN * 0.5)
        line4 = Text("Effective role. Kinetic origin.", font=DISPLAY, color=TEAL, font_size=30)
        line4.move_to(DOWN * 1.2)
        sub = Text("No new fundamental interaction is introduced.", font=SERIF,
                   color=INK, font_size=24, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line2), run_time=0.5)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line4, shift=DOWN * 0.1), run_time=0.6)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.8)

class B12_YourTurn(Scene):
    def construct(self):
        total=_dur("B12",12); title=LabelChip("YOUR TURN",accent=SLATE,size=24); title.to_corner(UL,buff=.6)
        eq=Text("ell(ell + 1)",font=MONO,font_size=44,color=INK).move_to(UP*1.4)
        zero=Text("ell = 0  →  0",font=MONO,font_size=38,color=TEAL).move_to(LEFT*2.5)
        two=Text("ell = 2  →  6",font=MONO,font_size=38,color=CRIMSON).move_to(RIGHT*2.5)
        ans=Text("ell = 2: stronger suppression near r = 0",font=MONO,font_size=30,color=INK).move_to(DOWN*2)
        self.play(FadeIn(title,eq),run_time=.8); self.wait(total*.35); self.play(FadeIn(zero,two,ans),run_time=.8); self.wait(max(.1,total*.65-1.6))
