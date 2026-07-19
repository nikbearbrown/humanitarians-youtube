"""vox_scenes.py — Why the Born Rule Is Just Measuring the Length of a Shadow
(vox-born-rule-projection, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = eigenstate directions; CRIMSON = amplitude (complex, before squaring);
           GOLD = probability squares (fill only, never text).
Exclusions: no polarization-identity proof, no density matrix, no no-go theorems.
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
        title = Text("Why the Born Rule Is Just", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Measuring the Length of a Shadow", font=SERIF, color=TEAL, font_size=40, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=2.5)
        rule.next_to(content, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: spin-x measured along z ─────────────────────────────────
class B02_SpinXMeasuredZ(Scene):
    def construct(self):
        total = _dur("B02", 12.0)
        eyebrow = LabelChip("BORN RULE", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Equation
        eq = Text("P(+z) = |⟨+z|+x⟩|²  = ½", font=MONO, color=INK, font_size=44)
        eq.move_to(UP * 1.2)

        rule_eq = Line(LEFT * 4.0, RIGHT * 4.0, color=SLATE, stroke_width=1.5)
        rule_eq.next_to(eq, DOWN, buff=0.3)

        label_amp = Text("inner product = 1/√2 (complex amplitude)", font=SERIF,
                         color=CRIMSON, font_size=28, slant=ITALIC)
        label_amp.next_to(rule_eq, DOWN, buff=0.3)
        label_prob = Text("square it → probability = ½", font=SERIF,
                          color=TEAL, font_size=28, slant=ITALIC)
        label_prob.next_to(label_amp, DOWN, buff=0.25)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(eq, shift=UP * 0.15), run_time=1.0)
        self.play(Create(rule_eq), run_time=0.5)
        self.play(FadeIn(label_amp, shift=RIGHT * 0.1), run_time=0.7)
        self.play(FadeIn(label_prob, shift=RIGHT * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B03 — Geometric picture: 45° projection ───────────────────────────────────
class B03_ProjectionGeometry(Scene):
    def construct(self):
        total = _dur("B03", 10.0)
        eyebrow = LabelChip("z-BASIS COEFFICIENT PLANE", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        origin = ORIGIN + LEFT * 1.5
        # z-eigenstate axis (vertical)
        z_ax = Arrow(origin, origin + UP * 2.4, color=TEAL, stroke_width=4, buff=0)
        z_lbl = Text("|-z⟩ component", font=MONO, color=TEAL, font_size=26)
        z_lbl.next_to(z_ax.get_end(), UR, buff=0.1)
        plus_ax = Arrow(origin, origin + RIGHT * 2.4, color=TEAL, stroke_width=4, buff=0)
        plus_lbl = Text("|+z⟩ component", font=MONO, color=TEAL, font_size=26)
        plus_lbl.next_to(plus_ax.get_end(), DOWN, buff=0.12)

        # x-eigenstate axis at 45°
        angle_45 = 45 * DEGREES
        x_tip = origin + (UP * np.cos(angle_45) + RIGHT * np.sin(angle_45)) * 2.4
        x_ax = Arrow(origin, x_tip, color=CRIMSON, stroke_width=4, buff=0)
        x_lbl = Text("|+x⟩ coefficients", font=MONO, color=CRIMSON, font_size=28)
        x_lbl.next_to(x_ax.get_end(), UR, buff=0.1)

        # Shadow (projection) — dashed vertical from x_tip down to z axis
        x_tip_arr = origin + (UP * np.cos(angle_45) + RIGHT * np.sin(angle_45)) * 2.4
        proj_foot = origin + UP * (2.4 * np.cos(angle_45))
        shadow_line = DashedLine(x_tip_arr, proj_foot,
                                 color=GOLD, stroke_width=2.5, dash_length=0.12)

        shadow_label = Text("each component = 1/√2", font=MONO, color=INK, font_size=24)
        shadow_label.move_to(RIGHT * 2.8 + UP * 1.0)

        sq_label = Text("Bloch x vs z angle = 90°", font=MONO, color=TEAL, font_size=25)
        sq_label.move_to(RIGHT * 3.0 + DOWN * 1.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(GrowArrow(z_ax), GrowArrow(plus_ax), FadeIn(z_lbl), FadeIn(plus_lbl), run_time=0.8)
        self.play(GrowArrow(x_ax), FadeIn(x_lbl), run_time=0.8)
        self.play(Create(shadow_line), run_time=0.7)
        self.play(FadeIn(shadow_label), run_time=0.6)
        self.play(FadeIn(sq_label, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("P  =  |⟨a|ψ⟩|²", font=MONO, color=INK, font_size=46)
        q2 = Text("squared projection.", font=DISPLAY, color=TEAL, font_size=36)
        q3 = Text("Why squared,", font=SERIF, color=INK, font_size=34, slant=ITALIC)
        q4 = Text("and why does that sum to 1?", font=SERIF, color=INK, font_size=34, slant=ITALIC)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=2.0)
        rule.next_to(q2, DOWN, buff=0.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q3), FadeIn(q4), run_time=0.8)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: inner product is complex ───────────────────────────────
class B05_ComplexAmplitude(Scene):
    def construct(self):
        total = _dur("B05", 11.0)
        eyebrow = LabelChip("NAIVE ATTEMPT", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_naive = VGroup(
            Text("use ⟨a|ψ⟩ directly", font=SERIF, color=INK, font_size=30),
            Text("= complex number", font=MONO, color=CRIMSON, font_size=32),
            Text("NOT a probability", font=DISPLAY, color=CRIMSON, font_size=30),
        )
        col_naive.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        col_naive.move_to(LEFT * 3.0)

        col_fix = VGroup(
            Text("use |⟨a|ψ⟩|²", font=SERIF, color=INK, font_size=30),
            Text("= real, ≥ 0", font=MONO, color=TEAL, font_size=32),
            Text("a probability", font=DISPLAY, color=TEAL, font_size=30),
        )
        col_fix.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        col_fix.move_to(RIGHT * 3.0)

        div = Line(UP * 1.8, DOWN * 1.8, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_naive[0]), FadeIn(col_fix[0]), run_time=0.6)
        self.play(FadeIn(col_naive[1]), FadeIn(col_fix[1]), run_time=0.7)
        self.play(FadeIn(col_naive[2]), FadeIn(col_fix[2]), run_time=0.7)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: expand in eigenbasis ────────────────────────────────────
class B06_EigenbasisExpansion(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        expand = Text("|ψ⟩  =  c₁|a₁⟩ + c₂|a₂⟩", font=MONO, color=INK, font_size=42)
        expand.move_to(UP * 1.2)

        rule_mid = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=1.5)
        rule_mid.next_to(expand, DOWN, buff=0.3)

        prob1 = Text("P(a₁) = |c₁|²", font=MONO, color=TEAL, font_size=30)
        prob1.move_to(DOWN * 0.5 + LEFT * 2.7)
        prob2 = Text("P(a₂) = |c₂|²", font=MONO, color=TEAL, font_size=30)
        prob2.move_to(DOWN * 0.5 + RIGHT * 2.7)

        sum_eq = Text("|c₁|²  +  |c₂|²  =  1", font=MONO, color=TEAL, font_size=36)
        sum_eq.move_to(DOWN * 1.5)

        conclusion = SerifLabel("squared shadow lengths always tile to 1", accent=TEAL, size=26)
        conclusion.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(expand, shift=UP * 0.1), run_time=0.9)
        self.play(Create(rule_mid), run_time=0.5)
        self.play(FadeIn(prob1), FadeIn(prob2), run_time=0.7)
        self.play(FadeIn(sum_eq, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B07 — MECHANISM: probability squares on the unit circle ──────────────────
class B07_ProbabilitySquares(Scene):
    def construct(self):
        total = _dur("B07", 11.0)
        eyebrow = LabelChip("unit circle in Hilbert space", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        origin = LEFT * 2.5
        # Two eigenstate axes
        ax1 = Arrow(origin, origin + RIGHT * 2.0, color=TEAL, stroke_width=3, buff=0)
        lbl1 = Text("|a₁⟩", font=MONO, color=TEAL, font_size=28)
        lbl1.next_to(ax1.get_end(), RIGHT, buff=0.1)

        ax2 = Arrow(origin, origin + UP * 2.0, color=TEAL, stroke_width=3, buff=0)
        lbl2 = Text("|a₂⟩", font=MONO, color=TEAL, font_size=28)
        lbl2.next_to(ax2.get_end(), UP, buff=0.1)

        # State vector at 30° from axis 1
        state_angle = 30 * DEGREES
        state_tip = origin + (RIGHT * np.cos(state_angle) + UP * np.sin(state_angle)) * 2.0
        state_arr = Arrow(origin, state_tip, color=CRIMSON, stroke_width=4, buff=0)
        state_lbl = Text("|ψ⟩", font=MONO, color=CRIMSON, font_size=28)
        state_lbl.next_to(state_arr.get_end(), UR, buff=0.1)

        # Probability squares (as filled rectangles next to axes)
        sq1 = Rectangle(width=1.2, height=0.4).set_fill(TEAL, 0.4).set_stroke(TEAL, 2.0)
        sq1.move_to(RIGHT * 2.0 + DOWN * 1.0)
        sq1_lbl = Text("|c₁|² = 0.75", font=MONO, color=TEAL, font_size=24)
        sq1_lbl.next_to(sq1, RIGHT, buff=0.2)

        sq2 = Rectangle(width=0.4, height=0.4).set_fill(TEAL, 0.4).set_stroke(TEAL, 2.0)
        sq2.move_to(RIGHT * 2.0 + DOWN * 1.7)
        sq2_lbl = Text("|c₂|² = 0.25", font=MONO, color=TEAL, font_size=24)
        sq2_lbl.next_to(sq2, RIGHT, buff=0.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(GrowArrow(ax1), GrowArrow(ax2), FadeIn(lbl1), FadeIn(lbl2), run_time=0.8)
        self.play(GrowArrow(state_arr), FadeIn(state_lbl), run_time=0.8)
        self.play(GrowFromCenter(sq1), FadeIn(sq1_lbl), run_time=0.7)
        self.play(GrowFromCenter(sq2), FadeIn(sq2_lbl), run_time=0.7)
        self.wait(total - 4.5)


# ── B08 — MECHANISM: phase disappears under |·|² ─────────────────────────────
class B08_PhaseDisappears(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        eyebrow = LabelChip("AMPLITUDE vs PROBABILITY", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left: amplitude has phase
        col_amp = VGroup(
            LabelChip("amplitude", accent=CRIMSON, size=22),
            Text("c₁ = |c₁| · e^{iθ}", font=MONO, color=CRIMSON, font_size=34),
            Text("complex, has phase θ", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC),
        )
        col_amp.arrange(DOWN, buff=0.4)
        col_amp.move_to(LEFT * 3.0)

        # Right: probability loses phase
        col_prob = VGroup(
            LabelChip("probability", accent=TEAL, size=22),
            Text("|c₁|²  =  |c₁|²", font=MONO, color=TEAL, font_size=34),
            Text("real, phase gone", font=SERIF, color=TEAL, font_size=26, slant=ITALIC),
        )
        col_prob.arrange(DOWN, buff=0.4)
        col_prob.move_to(RIGHT * 3.0)

        div = Line(UP * 1.8, DOWN * 1.8, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = Text("phase survives in interference — not single outcomes", font=SERIF,
                    color=INK, font_size=24, slant=ITALIC)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_amp[0]), FadeIn(col_prob[0]), run_time=0.6)
        self.play(FadeIn(col_amp[1]), FadeIn(col_prob[1]), run_time=0.7)
        self.play(FadeIn(col_amp[2]), FadeIn(col_prob[2]), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B09 — Implication: geometry forces the Born rule ─────────────────────────
class B09_GeometryForces(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("SCOPE OF THE METAPHOR", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        lines = VGroup(
            Text("Geometry explains the calculation.", font=SERIF, color=INK, font_size=32),
            Text("It does not derive the probability law", font=SERIF, color=INK, font_size=30),
            Text("from vector spaces alone.", font=SERIF, color=INK, font_size=30),
            Text("Born probability remains a postulate.", font=DISPLAY, color=TEAL, font_size=34),
        )
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        lines.move_to(ORIGIN).shift(DOWN * 0.1)

        rule_top = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=2.0)
        rule_top.next_to(lines, UP, buff=0.3)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(rule_top), run_time=0.5)
        self.play(FadeIn(lines[0]), run_time=0.6)
        self.play(FadeIn(lines[1]), run_time=0.6)
        self.play(FadeIn(lines[2]), run_time=0.6)
        self.play(FadeIn(lines[3], shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE: 30° student ───────────────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        setup = VGroup(
            Text("state at 30° from |E₁⟩", font=MONO, color=INK, font_size=28),
            Text("2-level system", font=MONO, color=INK, font_size=28),
        )
        setup.arrange(RIGHT, buff=0.9)
        setup.move_to(UP * 1.6)

        rule_setup = Line(LEFT * 5.0, RIGHT * 5.0, color=SLATE, stroke_width=1.5)
        rule_setup.next_to(setup, DOWN, buff=0.25)

        col_theory = VGroup(
            LabelChip("predicted", accent=TEAL, size=22),
            Text("P(E₁) = cos²(30°) = 0.75", font=MONO, color=TEAL, font_size=28),
            Text("P(E₂) = sin²(30°) = 0.25", font=MONO, color=TEAL, font_size=28),
        )
        col_theory.arrange(DOWN, buff=0.32)
        col_theory.move_to(LEFT * 2.8 + DOWN * 0.3)

        col_exp = VGroup(
            LabelChip("1000 copies", accent=SLATE, size=22),
            Text("~750 in E₁", font=MONO, color=TEAL, font_size=28),
            Text("~250 in E₂", font=MONO, color=TEAL, font_size=28),
        )
        col_exp.arrange(DOWN, buff=0.32)
        col_exp.move_to(RIGHT * 2.8 + DOWN * 0.3)

        div = Line(UP * 0.8, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN + DOWN * 0.6)

        match_lbl = SerifLabel("shadow lengths predicted the histogram", accent=TEAL, size=26)
        match_lbl.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(setup), run_time=0.6)
        self.play(Create(rule_setup), run_time=0.4)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_theory[0]), FadeIn(col_exp[0]), run_time=0.6)
        self.play(FadeIn(col_theory[1]), FadeIn(col_exp[1]), run_time=0.7)
        self.play(FadeIn(col_theory[2]), FadeIn(col_exp[2]), run_time=0.7)
        self.play(FadeIn(match_lbl, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 5.5)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("P  =  |⟨a|ψ⟩|²", font=MONO, color=INK, font_size=48)
        line1.move_to(UP * 0.8)
        line2 = Text("=  squared shadow length.", font=MONO, color=TEAL, font_size=38)
        line2.move_to(UP * 0.05)
        line3 = Text("Sums to 1 because |ψ⟩ is a unit vector.", font=MONO, color=TEAL, font_size=28)
        line3.move_to(DOWN * 0.7)
        sub = Text("Geometry illustrates the Born postulate.", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.7)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.5)

class B12_YourTurn(Scene):
    def construct(self):
        total=_dur("B12",12)
        title=LabelChip("YOUR TURN",accent=SLATE,size=24); title.to_corner(UL,buff=.6)
        q=Text("theta = 60°",font=MONO,font_size=42,color=INK).move_to(UP*1.4)
        p1=Text("cos²(60°) = 1/4",font=MONO,font_size=38,color=TEAL).move_to(LEFT*2.5)
        p2=Text("sin²(60°) = 3/4",font=MONO,font_size=38,color=CRIMSON).move_to(RIGHT*2.5)
        check=Text("1/4 + 3/4 = 1",font=MONO,font_size=36,color=INK).move_to(DOWN*2)
        self.play(FadeIn(title,q),run_time=.8); self.wait(total*.35); self.play(FadeIn(p1,p2,check),run_time=.8); self.wait(max(.1,total*.65-1.6))
