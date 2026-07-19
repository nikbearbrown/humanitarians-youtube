"""vox_scenes.py — Why the Schrodinger Equation Is a Theorem, Not a Postulate
(vox-schrodinger-theorem, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = derivation steps (probability conservation -> unitarity -> Hermitian -> exponential -> Schrodinger)
           CRIMSON = the postulate framing being displaced
Exclusions: no interaction-picture detour, no path-integral derivation,
            no Stone's theorem, no Hamiltonian in curved spacetime.
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
        title = Text("Why the Schrodinger Equation", font=DISPLAY, color=INK, font_size=40)
        sub = Text("Is a Theorem, Not a Postulate", font=SERIF, color=TEAL, font_size=40, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.5 + DOWN * 0.65, RIGHT * 5.5 + DOWN * 0.65,
                    color=CRIMSON, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: probabilities sum to one ────────────────────────────────
class B02_ProbabilitiesOne(Scene):
    def construct(self):
        total = _dur("B02", 15.0)
        eyebrow = LabelChip("NORM PRESERVATION", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        fact = Text("total probability of finding", font=SERIF, color=INK, font_size=32, slant=ITALIC)
        fact2 = Text("the particle somewhere = 1", font=SERIF, color=INK, font_size=32, slant=ITALIC)
        fact_grp = VGroup(fact, fact2)
        fact_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        fact_grp.move_to(UP * 1.0)

        always = Text("at every moment in time", font=DISPLAY, color=TEAL, font_size=36)
        always.move_to(DOWN * 0.4)

        start = Text("plus linear inner-product-preserving evolution", font=MONO, color=TEAL, font_size=23)
        start.move_to(DOWN * 1.6)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(fact), FadeIn(fact2), run_time=0.8)
        self.play(FadeIn(always), run_time=0.7)
        self.play(FadeIn(start), run_time=0.6)
        self.wait(total - 3.5)


# ── B03 — Cold open: constraint forces a form ────────────────────────────────
class B03_ConstraintForcesForm(Scene):
    def construct(self):
        total = _dur("B03", 14.0)
        eyebrow = LabelChip("THE CONDITIONAL BRIDGE", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        step_a = Text("continuous unitary group", font=MONO, color=TEAL, font_size=26)
        arrow1 = Text("->", font=MONO, color=SLATE, font_size=28)
        step_b = Text("self-adjoint generator G", font=MONO, color=TEAL, font_size=26)
        arrow2 = Text("->", font=MONO, color=SLATE, font_size=28)
        step_c = Text("identify G = H/h-bar", font=DISPLAY, color=CRIMSON, font_size=30)

        chain = VGroup(step_a, arrow1, step_b, arrow2, step_c)
        chain.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        chain.move_to(ORIGIN + UP * 0.3)

        postulate = Text("then the Schrodinger form follows", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        postulate.move_to(DOWN * 2.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for mob in [step_a, arrow1, step_b, arrow2, step_c]:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.5)
        self.play(FadeIn(postulate), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 14.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("Does probability conservation", font=DISPLAY, color=INK, font_size=40)
        q2 = Text("force the Schrodinger equation?", font=DISPLAY, color=CRIMSON, font_size=40)
        ask = Text("Or is it still just a convenient postulate?", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        content = VGroup(q, q2, ask)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(ask), run_time=0.7)
        self.wait(total - 3.2)


# ── B05 — The Problem: postulate framing hides the chain ─────────────────────
class Legacy05_PostulateHides(Scene):
    def construct(self):
        total = _dur("B05", 17.0)
        eyebrow = LabelChip("the postulate trap", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        wrong = Text("textbook move:", font=MONO, color=CRIMSON, font_size=26)
        wrong.move_to(UP * 1.8)

        postulate_box = Rectangle(width=8.0, height=0.9, color=CRIMSON, stroke_width=2.0)
        postulate_box.set_fill(GROUND, opacity=0.0)
        postulate_box.move_to(UP * 0.8)
        p_text = Text("i h-bar d/dt psi = H psi  [POSTULATE]",
                      font=DISPLAY, color=CRIMSON, font_size=28)
        p_text.move_to(UP * 0.8)

        problem = Text("this hides: why THAT equation?", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        problem.move_to(DOWN * 0.3)

        note = Text("postulating the wrong equation would also 'work'",
                    font=MONO, color=SLATE, font_size=22)
        note.move_to(DOWN * 1.4)

        correct = Text("the constraint actually picks out the right one",
                       font=DISPLAY, color=TEAL, font_size=26)
        correct.move_to(DOWN * 2.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(wrong), run_time=0.5)
        self.play(FadeIn(postulate_box), FadeIn(p_text), run_time=0.7)
        self.play(FadeIn(problem), run_time=0.6)
        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(correct), run_time=0.5)
        self.wait(total - 4.0)


# ── B06 — Step 1: Unitarity ──────────────────────────────────────────────────
class B06_Unitarity(Scene):
    def construct(self):
        total = _dur("B06", 18.0)
        eyebrow = LabelChip("step 1: unitarity", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        setup = Text("norm must be preserved at all times:", font=MONO, color=SLATE, font_size=26)
        setup.move_to(UP * 2.0)

        eq = Text("<psi(t)|psi(t)> = 1 for all t", font=DISPLAY, color=TEAL, font_size=32)
        eq.move_to(UP * 0.9)

        consequence = Text("forces  U-dagger x U = I", font=DISPLAY, color=TEAL, font_size=36)
        consequence.move_to(DOWN * 0.1)

        defn = Text("= definition of a unitary operator", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        defn.move_to(DOWN * 1.2)

        note = Text("assumes linear closed-system evolution", font=MONO, color=SLATE, font_size=22)
        note.move_to(DOWN * 2.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(setup), run_time=0.6)
        self.play(FadeIn(eq), run_time=0.6)
        self.play(FadeIn(consequence), run_time=0.7)
        self.play(FadeIn(defn), run_time=0.6)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(total - 4.0)


# ── B07 — Step 2: Hermitian generator ───────────────────────────────────────
class B07_HermitianGenerator(Scene):
    def construct(self):
        total = _dur("B07", 18.0)
        eyebrow = LabelChip("step 2: self-adjoint generator", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        setup = Text("infinitesimal step: U(dt) = I - i G dt",
                     font=MONO, color=SLATE, font_size=26)
        setup.move_to(UP * 1.8)

        constraint = Text("unitarity to first order: G-dagger = G", font=DISPLAY, color=TEAL, font_size=32)
        constraint.move_to(UP * 0.7)

        mean1 = Text("generator G is self-adjoint", font=DISPLAY, color=TEAL, font_size=34)
        mean1.move_to(DOWN * 0.2)

        mean2 = Text("physical input: G = H / h-bar", font=MONO, color=TEAL, font_size=25)
        mean2.move_to(DOWN * 1.2)

        free = Text("requires continuity and unitary group structure",
                    font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        free.move_to(DOWN * 2.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(setup), run_time=0.6)
        self.play(FadeIn(constraint), run_time=0.7)
        self.play(FadeIn(mean1), run_time=0.6)
        self.play(FadeIn(mean2), run_time=0.5)
        self.play(FadeIn(free), run_time=0.5)
        self.wait(total - 4.0)


# ── B08 — Step 3: matrix exponential ────────────────────────────────────────
class B08_MatrixExponential(Scene):
    def construct(self):
        total = _dur("B08", 18.0)
        eyebrow = LabelChip("step 3: compose N infinitesimal steps", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        step1 = Text("each step: U(dt) = I - (i/h-bar) H dt",
                     font=MONO, color=SLATE, font_size=26)
        step1.move_to(UP * 2.0)

        step2 = Text("compose N steps, send N -> infinity:",
                     font=MONO, color=SLATE, font_size=26)
        step2.move_to(UP * 1.1)

        result = Text("U(t) = e^(-i H t / h-bar)", font=DISPLAY, color=TEAL, font_size=40)
        result.move_to(UP * 0.0)

        called = Text("exact when H is time independent",
                      font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        called.move_to(DOWN * 1.1)

        note = Text("time-dependent H generally requires time ordering",
                    font=MONO, color=SLATE, font_size=22)
        note.move_to(DOWN * 2.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(step1), run_time=0.6)
        self.play(FadeIn(step2), run_time=0.6)
        self.play(FadeIn(result), run_time=0.8)
        self.play(FadeIn(called), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(total - 4.0)


# ── B09 — Step 4: differentiate to get Schrodinger ───────────────────────────
class B09_Differentiate(Scene):
    def construct(self):
        total = _dur("B09", 17.0)
        eyebrow = LabelChip("step 4: differentiate", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        start = Text("start: psi(t) = e^(-iHt/h-bar) psi(0)",
                     font=MONO, color=TEAL, font_size=26)
        start.move_to(UP * 2.0)

        diff = Text("differentiate with respect to t:", font=MONO, color=SLATE, font_size=26)
        diff.move_to(UP * 1.1)

        result = Text("i h-bar d/dt |psi> = H |psi>", font=DISPLAY, color=TEAL, font_size=40)
        result.move_to(UP * 0.1)

        box = Rectangle(width=7.5, height=0.85, color=TEAL, stroke_width=2.5)
        box.set_fill(GROUND, opacity=0.0)
        box.move_to(UP * 0.1)

        tag = Text("Schrodinger form under the stated assumptions", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        tag.move_to(DOWN * 1.0)

        chain = Text("unitary group + G=H/h-bar -> exponential -> differential form",
                     font=MONO, color=SLATE, font_size=20)
        chain.move_to(DOWN * 2.2)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(start), run_time=0.6)
        self.play(FadeIn(diff), run_time=0.5)
        self.play(FadeIn(result), run_time=0.8)
        self.play(Create(box), run_time=0.5)
        self.play(FadeIn(tag), run_time=0.6)
        self.play(FadeIn(chain), run_time=0.5)
        self.wait(total - 4.5)


# ── B10 — The Implication: energies are real ─────────────────────────────────
class Legacy10_EnergiesReal(Scene):
    def construct(self):
        total = _dur("B10", 16.0)
        eyebrow = LabelChip("a free corollary", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        coro = Text("H must be Hermitian", font=DISPLAY, color=TEAL, font_size=36)
        coro.move_to(UP * 1.5)

        arrow = Text("->", font=MONO, color=SLATE, font_size=30)
        arrow.move_to(UP * 0.5)

        result1 = Text("eigenvalues of H are real", font=DISPLAY, color=TEAL, font_size=34)
        result1.move_to(DOWN * 0.3)

        result2 = Text("measured energies are always real numbers", font=MONO, color=TEAL, font_size=26)
        result2.move_to(DOWN * 1.2)

        note = Text("not assumed — forced by probability conservation",
                    font=SERIF, color=SLATE, font_size=26, slant=ITALIC)
        note.move_to(DOWN * 2.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(coro), run_time=0.7)
        self.play(FadeIn(arrow), run_time=0.4)
        self.play(FadeIn(result1), run_time=0.6)
        self.play(FadeIn(result2), run_time=0.5)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 4.0)


# ── B11 — THE EXAMPLE (illustrative): student derives from scratch ────────────
class Legacy11_Example(Scene):
    def construct(self):
        total = _dur("B11", 22.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("A student derives time evolution from scratch",
                     font=DISPLAY, color=INK, font_size=28)
        title.move_to(UP * 2.4)

        steps = [
            ("1.", "writes U-dagger U = I  (prob. must sum to 1)", TEAL),
            ("2.", "extracts Hermitian generator: H-dagger = H", TEAL),
            ("3.", "composes N steps -> U(t) = e^(-iHt/h-bar)", TEAL),
            ("4.", "differentiates -> i h-bar d/dt psi = H psi", TEAL),
        ]

        step_mobs = []
        for i, (num, text, color) in enumerate(steps):
            n_mob = Text(num, font=MONO, color=SLATE, font_size=24)
            t_mob = Text(text, font=MONO, color=color, font_size=24)
            row = VGroup(n_mob, t_mob)
            row.arrange(RIGHT, buff=0.3)
            row.move_to(UP * (0.8 - i * 0.7))
            step_mobs.append(row)

        note = Text("(illustrative)", font=MONO, color=SLATE, font_size=20)
        note.move_to(DOWN * 2.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        for mob in step_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(total - 5.0)


# ── B12 — RECAP endcard ──────────────────────────────────────────────────────
class Legacy12_Endcard(Scene):
    def construct(self):
        total = _dur("B12", 17.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: Does probability conservation force the Schrodinger equation?",
                     font=SERIF, color=SLATE, font_size=24, slant=ITALIC)
        q_row.move_to(UP * 1.7)

        rule = Line(LEFT * 5.0 + UP * 1.05, RIGHT * 5.0 + UP * 1.05,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: Yes. Unitarity -> Hermitian generator -> matrix exponential -> Schrodinger.",
                     font=DISPLAY, color=INK, font_size=26)
        a_sub = Text("Not a postulate — a theorem.",
                     font=SERIF, color=TEAL, font_size=32, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        a_group.move_to(DOWN * 0.4)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)

class B05_Assumptions(Scene):
    def construct(self):
        total=_dur("B05",13); title=LabelChip("THE HIDDEN ASSUMPTIONS",accent=SLATE,size=22); title.to_corner(UL,buff=.6)
        rows=VGroup(*[Text(s,font=MONO,font_size=30,color=c) for s,c in [("linear state evolution",TEAL),("continuous time",TEAL),("unitary composition law",TEAL),("physical H supplied separately",CRIMSON)]]).arrange(DOWN,buff=.55)
        self.play(FadeIn(title),run_time=.5); self.play(FadeIn(rows),run_time=.9); self.wait(max(.1,total-1.4))

class B10_PhysicsInput(Scene):
    def construct(self):
        total=_dur("B10",13); title=LabelChip("WHAT UNITARITY DOES NOT CHOOSE",accent=CRIMSON,size=22); title.to_corner(UL,buff=.6)
        h=Text("H = ?",font=MONO,font_size=50,color=INK).move_to(UP*1.5)
        choices=VGroup(*[Text(s,font=MONO,font_size=29,color=TEAL) for s in ["harmonic potential","Coulomb interaction","spin coupling"]]).arrange(RIGHT,buff=1)
        note=Text("the physical model supplies the Hamiltonian",font=SERIF,font_size=31,color=CRIMSON).move_to(DOWN*2)
        self.play(FadeIn(title,h),run_time=.7); self.play(FadeIn(choices,note),run_time=.8); self.wait(max(.1,total-1.5))

class B11_Audit(Scene):
    def construct(self):
        total=_dur("B11",13); title=LabelChip("THE HONEST CONDITIONAL CHAIN",accent=SLATE,size=22); title.to_corner(UL,buff=.6)
        chain=VGroup(*[Text(s,font=MONO,font_size=28,color=c) for s,c in [("unitary continuous group",TEAL),("self-adjoint generator G",TEAL),("identify G = H / h-bar",CRIMSON),("Schrodinger form follows",TEAL)]]).arrange(DOWN,buff=.45)
        arrows=VGroup(*[Text("↓",font=MONO,font_size=28,color=INK) for _ in range(3)])
        for i,a in enumerate(arrows): a.move_to((chain[i].get_bottom()+chain[i+1].get_top())/2)
        self.play(FadeIn(title,chain,arrows),run_time=1); self.wait(max(.1,total-1))

class B12_YourTurn(Scene):
    def construct(self):
        total=_dur("B12",12); title=LabelChip("YOUR TURN",accent=SLATE,size=24); title.to_corner(UL,buff=.6)
        start=Text("psi(t) = exp(-iHt/h-bar) psi(0)",font=MONO,font_size=34,color=INK).move_to(UP*1.4)
        prompt=Text("differentiate with respect to t",font=SERIF,font_size=30,color=SLATE)
        result=Text("i h-bar d psi/dt = H psi",font=MONO,font_size=40,color=TEAL).move_to(DOWN*1.6)
        self.play(FadeIn(title,start,prompt),run_time=.8); self.wait(total*.4); self.play(FadeIn(result),run_time=.7); self.wait(max(.1,total*.6-1.5))
