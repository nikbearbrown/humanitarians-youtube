"""vox_scenes.py — Why the 2s State Lives a Hundred Million Times Longer Than It Should
(vox-2s-forbidden, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL-ai slots.
Color law: TEAL = allowed transitions (solid arrows, fast nanosecond decays)
           CRIMSON = the forbidden 2s->1s gap (dashed, blocked by conservation law)
Exclusions: no electric-dipole matrix element derivation, no QED,
            no full Balmer/Lyman series, no antihydrogen CPT comparison.
"""
import sys, json, pathlib
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
        title = Text("Why the 2s State Lives", font=DISPLAY, color=INK, font_size=42)
        sub = Text("a Hundred Million Times Longer Than It Should",
                   font=SERIF, color=TEAL, font_size=34, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.5 + DOWN * 0.7, RIGHT * 5.5 + DOWN * 0.7,
                    color=CRIMSON, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: normal decays happen fast ───────────────────────────────
class B02_NormalDecays(Scene):
    def construct(self):
        total = _dur("B02", 14.0)
        eyebrow = LabelChip("allowed decays", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Simple energy level diagram: n=1 and n=2 with 2p
        n1_line = Line(LEFT * 2.0 + DOWN * 1.8, RIGHT * 2.0 + DOWN * 1.8,
                       color=INK, stroke_width=2.5)
        n1_label = Text("1s   (n=1)", font=MONO, color=INK, font_size=22)
        n1_label.next_to(n1_line, RIGHT, buff=0.25)

        n2p_line = Line(LEFT * 2.0 + UP * 0.6, RIGHT * 2.0 + UP * 0.6,
                        color=TEAL, stroke_width=2.5)
        n2p_label = Text("2p  (ell=1)", font=MONO, color=TEAL, font_size=22)
        n2p_label.next_to(n2p_line, RIGHT, buff=0.25)

        # Arrow: allowed 2p -> 1s
        arrow = Arrow(
            UP * 0.6 + LEFT * 0.5,
            DOWN * 1.8 + LEFT * 0.5,
            color=TEAL, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.12,
        )
        arrow_label = Text("allowed", font=MONO, color=TEAL, font_size=22)
        arrow_label.move_to(LEFT * 1.8 + DOWN * 0.6)

        ns_label = Text("nanoseconds", font=DISPLAY, color=TEAL, font_size=30)
        ns_label.move_to(DOWN * 2.9)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(n1_line), FadeIn(n1_label), run_time=0.7)
        self.play(Create(n2p_line), FadeIn(n2p_label), run_time=0.7)
        self.play(Create(arrow), FadeIn(arrow_label), run_time=0.7)
        self.play(FadeIn(ns_label), run_time=0.6)
        self.wait(total - 3.8)


# ── B03 — Cold open: 2s is different ────────────────────────────────────────
class B03_TwosIsDifferent(Scene):
    def construct(self):
        total = _dur("B03", 13.0)
        eyebrow = LabelChip("the 2s problem", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Energy diagram showing 2s and 2p at same level
        n1_line = Line(LEFT * 2.5 + DOWN * 1.8, RIGHT * 2.5 + DOWN * 1.8,
                       color=INK, stroke_width=2.5)
        n1_label = Text("1s", font=MONO, color=INK, font_size=22)
        n1_label.next_to(n1_line, RIGHT, buff=0.25)

        n2_line = Line(LEFT * 2.5 + UP * 0.6, RIGHT * 2.5 + UP * 0.6,
                       color=CRIMSON, stroke_width=2.5)
        n2_label = Text("2s  same 10.2 eV gap", font=MONO, color=CRIMSON, font_size=22)
        n2_label.next_to(n2_line, RIGHT, buff=0.25)

        # Dashed arrow blocked
        dash_line = DashedLine(
            UP * 0.6 + LEFT * 0.5,
            DOWN * 1.8 + LEFT * 0.5,
            color=CRIMSON, stroke_width=3.0, dash_length=0.18,
        )
        blocked = Text("0.12 s  (about 8x10^7 slower)", font=DISPLAY, color=CRIMSON, font_size=27)
        blocked.move_to(DOWN * 2.9)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(n1_line), FadeIn(n1_label), run_time=0.7)
        self.play(Create(n2_line), FadeIn(n2_label), run_time=0.7)
        self.play(Create(dash_line), run_time=0.7)
        self.play(FadeIn(blocked), run_time=0.6)
        self.wait(total - 3.8)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 13.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("The 2s state has 10.2 eV and a clear destination.", font=DISPLAY, color=INK, font_size=34)
        q2 = Text("Why can't it decay?", font=DISPLAY, color=CRIMSON, font_size=38)
        content = VGroup(q, q2)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 2.5)


# ── B05 — The Problem: energy gap alone should be enough ─────────────────────
class B05_NaivePicture(Scene):
    def construct(self):
        total = _dur("B05", 15.0)
        eyebrow = LabelChip("the naive picture", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        naive = Text("naive rule:", font=MONO, color=SLATE, font_size=26)
        naive.move_to(UP * 1.8 + LEFT * 2.5)

        rule_text = Text("gap below + state above = decay happens",
                         font=DISPLAY, color=INK, font_size=30)
        rule_text.move_to(UP * 0.9)

        box = Rectangle(width=8.5, height=0.75, color=CRIMSON, stroke_width=2.0)
        box.set_fill(GROUND, opacity=0.0)
        box.move_to(UP * 0.9)

        contradiction = Text("2p decays in nanoseconds. 2s does not.",
                             font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        contradiction.move_to(DOWN * 0.3)

        question = Text("same energy. same destination. why different?",
                        font=MONO, color=SLATE, font_size=24)
        question.move_to(DOWN * 1.4)

        hint = Text("the missing ingredient is the E1 selection rule",
                    font=DISPLAY, color=TEAL, font_size=26)
        hint.move_to(DOWN * 2.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(naive), run_time=0.5)
        self.play(FadeIn(rule_text), Create(box), run_time=0.7)
        self.play(FadeIn(contradiction), run_time=0.6)
        self.play(FadeIn(question), run_time=0.5)
        self.play(FadeIn(hint), run_time=0.6)
        self.wait(total - 4.0)


# ── B06 — Mechanism: photon carries angular momentum ─────────────────────────
class B06_PhotonAngularMomentum(Scene):
    def construct(self):
        total = _dur("B06", 16.0)
        eyebrow = LabelChip("the constraint", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        fact1 = Text("a single photon carries", font=DISPLAY, color=INK, font_size=34)
        fact1.move_to(UP * 1.5)

        fact2 = Text("E1 rule: delta ell = plus or minus 1",
                     font=DISPLAY, color=TEAL, font_size=38)
        fact2.move_to(UP * 0.6)

        rule_line = Line(LEFT * 5.0 + UP * 0.0, RIGHT * 5.0 + UP * 0.0,
                         color=TEAL, stroke_width=1.5)

        consequence = Text("and the atomic parity must change",
                           font=MONO, color=TEAL, font_size=26)
        consequence.move_to(DOWN * 0.7)

        always = Text("dominant one-photon electric-dipole channel",
                      font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        always.move_to(DOWN * 1.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(fact1), run_time=0.6)
        self.play(FadeIn(fact2), run_time=0.7)
        self.play(Create(rule_line), run_time=0.5)
        self.play(FadeIn(consequence), run_time=0.6)
        self.play(FadeIn(always), run_time=0.6)
        self.wait(total - 4.0)


# ── B07 — Mechanism: delta-ell = 0 blocks the transition ─────────────────────
class B07_DeltaEllZero(Scene):
    def construct(self):
        total = _dur("B07", 17.0)
        eyebrow = LabelChip("why 2s cannot go", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        state_2s = Text("2s:   ell = 0", font=MONO, color=CRIMSON, font_size=32)
        state_2s.move_to(UP * 1.8 + LEFT * 2.0)

        state_1s = Text("1s:   ell = 0", font=MONO, color=CRIMSON, font_size=32)
        state_1s.move_to(UP * 0.9 + LEFT * 2.0)

        delta = Text("delta ell = 0 - 0 = 0", font=DISPLAY, color=CRIMSON, font_size=36)
        delta.move_to(DOWN * 0.0)

        need = Text("E1 requires delta ell = plus or minus 1", font=MONO, color=INK, font_size=26)
        need.move_to(DOWN * 0.95)

        forbidden = Text("E1 FORBIDDEN", font=DISPLAY, color=CRIMSON, font_size=34)
        forbidden.move_to(DOWN * 2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(state_2s), run_time=0.6)
        self.play(FadeIn(state_1s), run_time=0.6)
        self.play(FadeIn(delta), run_time=0.7)
        self.play(FadeIn(need), run_time=0.5)
        self.play(FadeIn(forbidden), run_time=0.7)
        self.wait(total - 4.0)


# ── B08 — Mechanism: why 2p can go but 2s cannot (compare) ───────────────────
class B08_Compare2p2s(Scene):
    def construct(self):
        total = _dur("B08", 16.0)
        eyebrow = LabelChip("allowed vs forbidden", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left column: 2p -> 1s  (allowed)
        left_title = Text("2p  ->  1s", font=DISPLAY, color=TEAL, font_size=30)
        left_title.move_to(LEFT * 3.2 + UP * 1.8)

        left_d = Text("ell: 1  ->  0", font=MONO, color=TEAL, font_size=26)
        left_d.move_to(LEFT * 3.2 + UP * 0.9)

        left_change = Text("delta ell = -1", font=DISPLAY, color=TEAL, font_size=28)
        left_change.move_to(LEFT * 3.2 + UP * 0.0)

        left_result = Text("parity changes", font=MONO, color=TEAL, font_size=24)
        left_result.move_to(LEFT * 3.2 + DOWN * 0.8)

        left_ok = Text("ALLOWED", font=DISPLAY, color=TEAL, font_size=28)
        left_ok.move_to(LEFT * 3.2 + DOWN * 1.7)

        # Divider
        divider = Line(UP * 2.5 + ORIGIN, DOWN * 2.2 + ORIGIN, color=SLATE, stroke_width=1.5)

        # Right column: 2s -> 1s (forbidden)
        right_title = Text("2s  ->  1s", font=DISPLAY, color=CRIMSON, font_size=30)
        right_title.move_to(RIGHT * 3.2 + UP * 1.8)

        right_d = Text("ell: 0  ->  0", font=MONO, color=CRIMSON, font_size=26)
        right_d.move_to(RIGHT * 3.2 + UP * 0.9)

        right_change = Text("delta ell = 0", font=DISPLAY, color=CRIMSON, font_size=28)
        right_change.move_to(RIGHT * 3.2 + UP * 0.0)

        right_result = Text("same parity", font=MONO, color=CRIMSON, font_size=24)
        right_result.move_to(RIGHT * 3.2 + DOWN * 0.8)

        right_forbidden = Text("FORBIDDEN", font=DISPLAY, color=CRIMSON, font_size=28)
        right_forbidden.move_to(RIGHT * 3.2 + DOWN * 1.7)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.6)
        self.play(FadeIn(left_d), FadeIn(right_d), run_time=0.6)
        self.play(FadeIn(left_change), FadeIn(right_change), run_time=0.6)
        self.play(FadeIn(left_result), FadeIn(right_result), run_time=0.6)
        self.play(FadeIn(left_ok), FadeIn(right_forbidden), run_time=0.7)
        self.wait(total - 4.5)


# ── B09 — Implication: the two-photon escape route ──────────────────────────
class B09_TwoPhoton(Scene):
    def construct(self):
        total = _dur("B09", 16.0)
        eyebrow = LabelChip("the escape route", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        problem = Text("one-photon E1 amplitude vanishes",
                       font=MONO, color=CRIMSON, font_size=26)
        problem.move_to(UP * 2.0)

        solution_title = Text("two photons:", font=DISPLAY, color=TEAL, font_size=34)
        solution_title.move_to(UP * 1.0)

        share = Text("combined state satisfies total J and parity",
                     font=MONO, color=TEAL, font_size=26)
        share.move_to(UP * 0.1)

        allowed = Text("allowed, but rare", font=SERIF, color=TEAL, font_size=30, slant=ITALIC)
        allowed.move_to(DOWN * 0.9)

        lifetime = Text("lifetime: 0.12 s  (not nanoseconds)", font=DISPLAY, color=TEAL, font_size=28)
        lifetime.move_to(DOWN * 2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(problem), run_time=0.7)
        self.play(FadeIn(solution_title), run_time=0.6)
        self.play(FadeIn(share), run_time=0.6)
        self.play(FadeIn(allowed), run_time=0.5)
        self.play(FadeIn(lifetime), run_time=0.6)
        self.wait(total - 4.0)


# ── B10 — Implication: metastability has uses ────────────────────────────────
class B10_Metastable(Scene):
    def construct(self):
        total = _dur("B10", 15.0)
        eyebrow = LabelChip("metastability", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        label = Text("long lifetime -> metastable state", font=DISPLAY, color=TEAL, font_size=34)
        label.move_to(UP * 1.5)

        rule = Line(LEFT * 5.0 + UP * 0.9, RIGHT * 5.0 + UP * 0.9,
                    color=TEAL, stroke_width=1.5)

        use1 = Text("stable enough to interrogate with a laser pulse",
                    font=MONO, color=TEAL, font_size=26)
        use1.move_to(UP * 0.1)

        use2 = Text("1s-2s transition measured to 15 significant figures",
                    font=MONO, color=TEAL, font_size=26)
        use2.move_to(DOWN * 0.75)

        note = Text("the forbidden rule makes the measurement possible",
                    font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        note.move_to(DOWN * 1.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(label), run_time=0.7)
        self.play(Create(rule), run_time=0.4)
        self.play(FadeIn(use1), run_time=0.6)
        self.play(FadeIn(use2), run_time=0.6)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 3.8)


# ── B11 — THE EXAMPLE (illustrative): student's beam ────────────────────────
class Legacy11_Example(Scene):
    def construct(self):
        total = _dur("B11", 20.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("A student prepares a 2s hydrogen beam",
                     font=DISPLAY, color=INK, font_size=28)
        title.move_to(UP * 2.4)

        steps = [
            "expects fast decay — energy gap, nearby destination",
            "after 0.1 s, most atoms still haven't decayed",
            "traces: ell=0 -> ell=0, delta ell = 0",
            "photon needs 1 unit — conservation fails",
            "every surviving atom explained by the rule",
        ]
        step_mobs = []
        for i, text in enumerate(steps):
            t_mob = Text(text, font=MONO, color=TEAL, font_size=22)
            t_mob.move_to(UP * (1.2 - i * 0.7))
            step_mobs.append(t_mob)

        note = Text("(illustrative)", font=MONO, color=SLATE, font_size=20)
        note.move_to(DOWN * 2.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        for mob in step_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.48)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(total - 5.5)


# ── B12 — RECAP endcard ──────────────────────────────────────────────────────
class Legacy12_Endcard(Scene):
    def construct(self):
        total = _dur("B12", 15.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: Why can't the 2s state decay in nanoseconds?",
                     font=SERIF, color=SLATE, font_size=26, slant=ITALIC)
        q_row.move_to(UP * 1.8)

        rule = Line(LEFT * 5.0 + UP * 1.15, RIGHT * 5.0 + UP * 1.15,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: The 2s->1s transition has delta ell = 0.",
                     font=DISPLAY, color=INK, font_size=28)
        a_sub = Text("Angular momentum conservation forbids it.",
                     font=SERIF, color=TEAL, font_size=32, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        a_group.move_to(DOWN * 0.3)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)

class B11_Scope(Scene):
    def construct(self):
        total=_dur("B11",13); title=LabelChip("WHAT FORBIDDEN MEANS",accent=SLATE,size=22); title.to_corner(UL,buff=.6)
        no=Text("not: impossible forever",font=MONO,font_size=34,color=CRIMSON).move_to(UP*1.3)
        yes=Text("yes: amplitude vanishes in the E1 channel",font=MONO,font_size=32,color=TEAL)
        route=Text("two-photon route remains",font=DISPLAY,font_size=36,color=TEAL).move_to(DOWN*1.4)
        self.play(FadeIn(title,no),run_time=.7); self.play(FadeIn(yes,route),run_time=.8); self.wait(max(.1,total-1.5))

class B12_YourTurn(Scene):
    def construct(self):
        total=_dur("B12",12); title=LabelChip("YOUR TURN",accent=SLATE,size=24); title.to_corner(UL,buff=.6)
        left=VGroup(Text("2p → 1s",font=DISPLAY,font_size=34,color=TEAL),Text("delta ell = -1",font=MONO,font_size=30,color=TEAL),Text("parity changes",font=MONO,font_size=27,color=TEAL),Text("E1 allowed",font=DISPLAY,font_size=30,color=TEAL)).arrange(DOWN,buff=.35).shift(LEFT*3)
        right=VGroup(Text("2s → 1s",font=DISPLAY,font_size=34,color=CRIMSON),Text("delta ell = 0",font=MONO,font_size=30,color=CRIMSON),Text("same parity",font=MONO,font_size=27,color=CRIMSON),Text("E1 forbidden",font=DISPLAY,font_size=30,color=CRIMSON)).arrange(DOWN,buff=.35).shift(RIGHT*3)
        self.play(FadeIn(title,left,right),run_time=1); self.wait(max(.1,total-1))

class B13_CorrectTitleOutro(Scene):
    def construct(self):
        total = _dur("B13", 5.0)
        self.camera.background_color = "#201F1C"
        title = Text("Why Some Atomic Light Is Forbidden", font=DISPLAY,
                     font_size=33, color="#F2EFE8")
        subtitle = Text("Hydrogen 2s and the E1 selection rule", font=SERIF,
                        font_size=21, color="#AAA49A").next_to(title, DOWN, buff=0.35)
        credit = Text("Kore, in for Humanitarians AI", font=SERIF, font_size=20,
                      color="#D97757").next_to(subtitle, DOWN, buff=0.42)
        self.play(FadeIn(title), FadeIn(subtitle), FadeIn(credit), run_time=1.0)
        self.wait(max(0.1, total - 1.0))
