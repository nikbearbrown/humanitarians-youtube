import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------------------
# B01 — Title card (CARD beat)
# ---------------------------------------------------------------------------
class B01_Title(Scene):
    def construct(self):
        duration = DUR.get("B01", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.8)
        headline = Text("Why Quantum Mechanics\nNeeds ell(ell+1), Not ell squared",
                        font=DISPLAY, font_size=36, color=INK,
                        line_spacing=1.2).move_to(DOWN * 0.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(headline), run_time=1.0)
        self.wait(max(0.1, duration - 1.5))


# ---------------------------------------------------------------------------
# B02 — Naive expectation: ell-squared vs ell(ell+1) (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_NaiveVsActual(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("L-squared eigenvalue: expected vs actual", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.2)

        # Left: naive guess (CRIMSON)
        box_wrong = Rectangle(width=5.5, height=2.8).set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 2)
        box_wrong.move_to(LEFT * 3.5 + DOWN * 0.2)
        label_wrong = Text("EXPECTED", font=DISPLAY, font_size=20,
                           color=CRIMSON).move_to(LEFT * 3.5 + UP * 1.4)
        eq_wrong = Text("L-sq = ell^2  h-bar^2", font="PT Mono", font_size=22,
                        color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 0.1)
        logic_wrong = Text("max L-z squared", font=DISPLAY, font_size=16,
                           color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 1.0)

        # Right: actual (TEAL)
        box_right = Rectangle(width=5.5, height=2.8).set_fill(TEAL, 0.07).set_stroke(TEAL, 2)
        box_right.move_to(RIGHT * 3.5 + DOWN * 0.2)
        label_right = Text("ACTUAL", font=DISPLAY, font_size=20,
                           color=TEAL).move_to(RIGHT * 3.5 + UP * 1.4)
        eq_right = Text("L-sq = ell(ell+1)  h-bar^2", font="PT Mono", font_size=22,
                        color=TEAL).move_to(RIGHT * 3.5 + DOWN * 0.1)
        logic_right = Text("measured every time", font=DISPLAY, font_size=16,
                           color=TEAL).move_to(RIGHT * 3.5 + DOWN * 1.0)

        divider = Line(UP * 2.5, DOWN * 2.0, color=INK, stroke_width=1).set_opacity(0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(box_wrong), GrowFromCenter(box_right), run_time=0.8)
        self.play(FadeIn(label_wrong), FadeIn(label_right), run_time=0.5)
        self.play(Write(eq_wrong), Write(eq_right), run_time=1.0)
        self.play(FadeIn(logic_wrong), FadeIn(logic_right), Create(divider), run_time=0.7)
        self.wait(max(0.1, duration - 3.7))


# ---------------------------------------------------------------------------
# B03 — THE QUESTION card (CARD beat)
# ---------------------------------------------------------------------------
class B03_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B03", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 2.8)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        line1 = Text("L squared should equal L-z max squared.", font=SERIF, font_size=26, color=INK).move_to(UP * 1.4)
        line2 = Text("Every measurement gives ell(ell+1), not ell squared.", font=SERIF, font_size=24, color=INK).move_to(UP * 0.5)
        line3 = Text("The plus-one cannot be dropped.", font=SERIF, font_size=24, color=INK).move_to(DOWN * 0.4)
        line4 = Text("Why does L squared give more than L-z squared?", font=SERIF, font_size=24, color=INK).move_to(DOWN * 1.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.6)
        self.play(Write(line1), run_time=0.5)
        self.play(Write(line2), run_time=0.6)
        self.play(Write(line3), Write(line4), run_time=0.7)
        self.wait(max(0.1, duration - 2.4))


# ---------------------------------------------------------------------------
# B04 — Ladder of m-values (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_MValueLadder(Scene):
    def construct(self):
        duration = DUR.get("B04", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Ladder of m-values for ell = 2", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Draw 5 rungs: m = -2, -1, 0, +1, +2
        rung_y = [-2.0, -1.0, 0.0, 1.0, 2.0]
        rung_labels = ["-2", "-1", "0", "+1", "+2"]
        rungs = VGroup()
        labels = VGroup()
        for y, lab in zip(rung_y, rung_labels):
            r = Line(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=2).move_to(UP * y)
            rungs.add(r)
            t = Text(lab, font="PT Mono", font_size=22, color=INK).move_to(RIGHT * 2.2 + UP * y)
            labels.add(t)

        # Side rails
        rail_left = Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=1.5).move_to(LEFT * 1.5)
        rail_right = Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=1.5).move_to(RIGHT * 1.5)

        top_label = Text("top rung: m = +ell", font=DISPLAY, font_size=18,
                         color=TEAL).move_to(LEFT * 4.0 + UP * 2.0)
        top_arrow = Arrow(LEFT * 2.8 + UP * 2.0, LEFT * 1.8 + UP * 2.0, color=TEAL,
                          buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2)

        naive_label = Text("naive: L-sq = (ell h-bar)^2 = 4 h-bar^2", font="PT Mono",
                           font_size=18, color=CRIMSON).move_to(DOWN * 3.2)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(rail_left), Create(rail_right), run_time=0.5)
        self.play(Create(rungs), run_time=1.0)
        self.play(FadeIn(labels), run_time=0.6)
        self.play(FadeIn(top_label), GrowArrow(top_arrow), run_time=0.7)
        self.play(FadeIn(naive_label), run_time=0.5)
        self.wait(max(0.1, duration - 4.0))


# ---------------------------------------------------------------------------
# B05 — L-squared includes x and y components (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_LsqComponents(Scene):
    def construct(self):
        duration = DUR.get("B05", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("L-squared = L-x^2 + L-y^2 + L-z^2", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Three component boxes
        box_lx = Rectangle(width=3.0, height=1.5).set_fill(SLATE, 0.15).set_stroke(INK, 2)
        box_lx.move_to(LEFT * 4.5 + UP * 0.3)
        label_lx = Text("L-x squared", font=DISPLAY, font_size=20, color=INK).move_to(LEFT * 4.5 + UP * 0.3)

        box_ly = Rectangle(width=3.0, height=1.5).set_fill(SLATE, 0.15).set_stroke(INK, 2)
        box_ly.move_to(ORIGIN + UP * 0.3)
        label_ly = Text("L-y squared", font=DISPLAY, font_size=20, color=INK).move_to(ORIGIN + UP * 0.3)

        box_lz = Rectangle(width=3.0, height=1.5).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        box_lz.move_to(RIGHT * 4.5 + UP * 0.3)
        label_lz = Text("L-z squared", font=DISPLAY, font_size=20, color=TEAL).move_to(RIGHT * 4.5 + UP * 0.3)

        plus1 = Text("+", font=DISPLAY, font_size=30, color=INK).move_to(LEFT * 2.25 + UP * 0.3)
        plus2 = Text("+", font=DISPLAY, font_size=30, color=INK).move_to(RIGHT * 2.25 + UP * 0.3)

        note = Text("L-x and L-y are never exactly zero — they contribute too.", font=DISPLAY,
                    font_size=20, color=INK).move_to(DOWN * 1.8)

        highlight = Text("The missing piece: L-x^2 + L-y^2", font=DISPLAY, font_size=20,
                         color=CRIMSON).move_to(DOWN * 2.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(box_lx), GrowFromCenter(box_ly), GrowFromCenter(box_lz),
                  run_time=0.8)
        self.play(FadeIn(label_lx), FadeIn(label_ly), FadeIn(label_lz),
                  FadeIn(plus1), FadeIn(plus2), run_time=0.7)
        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(highlight), run_time=0.5)
        self.wait(max(0.1, duration - 3.2))


# ---------------------------------------------------------------------------
# B06 — THE MECHANISM section card (CARD beat)
# ---------------------------------------------------------------------------
class B06_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B06", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("The commutator\ncreates the extra term", font=DISPLAY, font_size=44,
                        color=INK, line_spacing=1.2).move_to(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.9)
        self.wait(max(0.1, duration - 1.4))


# ---------------------------------------------------------------------------
# B07 — L-minus L-plus expansion shows cross-term (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_CommutatorTerm(Scene):
    def construct(self):
        duration = DUR.get("B07", 14.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Expand L-minus times L-plus:", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Step 1: L^2 in terms of ladder ops
        step1 = Text("L-sq = L-minus times L-plus + L-z-sq + h-bar times L-z", font="PT Mono",
                     font_size=20, color=INK).move_to(UP * 2.0)

        # Step 2: the extra term highlighted
        step2a = Text("Compare to naive: L-sq = L-z-sq   <-- MISSING:", font="PT Mono",
                      font_size=18, color=CRIMSON).move_to(UP * 0.8)
        step2b = Text("L-minus times L-plus  PLUS  h-bar times L-z", font="PT Mono",
                      font_size=20, color=TEAL).move_to(DOWN * 0.2)

        # Arrow pointing to cross-term
        bracket = Rectangle(width=5.2, height=0.7).set_fill(TEAL, 0.1).set_stroke(TEAL, 2)
        bracket.move_to(DOWN * 0.2)

        origin_label = Text("this cross-term comes from non-commutativity", font=DISPLAY,
                            font_size=20, color=TEAL).move_to(DOWN * 1.4)

        result = Text("Result at top rung: L-sq = ell(ell+1) h-bar-sq", font="PT Mono",
                      font_size=20, color=TEAL).move_to(DOWN * 2.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Write(step1), run_time=1.0)
        self.play(Write(step2a), run_time=0.8)
        self.play(Write(step2b), run_time=0.9)
        self.play(GrowFromCenter(bracket), run_time=0.5)
        self.play(FadeIn(origin_label), run_time=0.5)
        self.play(FadeIn(result), run_time=0.6)
        self.wait(max(0.1, duration - 5.1))


# ---------------------------------------------------------------------------
# B08 — Top rung section card (CARD beat)
# ---------------------------------------------------------------------------
class B08_TopRungCard(Scene):
    def construct(self):
        duration = DUR.get("B08", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("The top rung condition\nforces the plus-one", font=DISPLAY, font_size=42,
                        color=INK, line_spacing=1.2).move_to(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.9)
        self.wait(max(0.1, duration - 1.4))


# ---------------------------------------------------------------------------
# B09 — Top rung kills state, eigenvalue fixed (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B09_TopRungCondition(Scene):
    def construct(self):
        duration = DUR.get("B09", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("At the top rung: L-plus kills the state", font=DISPLAY, font_size=24,
                     color=TEAL).move_to(UP * 3.2)

        # Ladder with token at top
        rung_y = [-2.0, -1.0, 0.0, 1.0, 2.0]
        rungs = VGroup(*[
            Line(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=2).move_to(UP * y)
            for y in rung_y
        ])
        rails = VGroup(
            Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=1.5).move_to(LEFT * 1.5),
            Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=1.5).move_to(RIGHT * 1.5)
        )
        token = Dot(radius=0.3, color=TEAL).move_to(UP * 2.0)
        token_label = Text("m = +ell", font=DISPLAY, font_size=18, color=TEAL).move_to(RIGHT * 3.2 + UP * 2.0)

        # L-plus arrow above top rung -> annihilates
        up_arrow = Arrow(UP * 2.0, UP * 3.2, color=CRIMSON, buff=0.35,
                         stroke_width=3, max_tip_length_to_length_ratio=0.2)
        cancel = Text("L-plus kills this state -- 0", font=DISPLAY, font_size=18,
                      color=CRIMSON).move_to(RIGHT * 4.0 + UP * 3.2)

        # Result
        result = Text("Solving: lambda = ell(ell+1) h-bar^2", font="PT Mono",
                      font_size=22, color=TEAL).move_to(DOWN * 3.2)

        self.play(FadeIn(title), Create(rails), Create(rungs), run_time=0.8)
        self.play(GrowFromCenter(token), FadeIn(token_label), run_time=0.6)
        self.play(GrowArrow(up_arrow), FadeIn(cancel), run_time=0.8)
        self.play(FadeIn(result), run_time=0.6)
        self.wait(max(0.1, duration - 3.3))


# ---------------------------------------------------------------------------
# B11 — Spectral lines trace to plus-one (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_SpectralLines(Scene):
    def construct(self):
        duration = DUR.get("B11", 8.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Every spectral line traces back to this extra term", font=DISPLAY,
                     font_size=24, color=TEAL).move_to(UP * 3.2)

        # Three energy levels, with ell(ell+1) spacing
        levels_y = [-1.5, 0.0, 2.0]
        level_labels = ["ell = 0: L-sq = 0", "ell = 1: L-sq = 2", "ell = 2: L-sq = 6"]
        for y, lab in zip(levels_y, level_labels):
            lv = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).move_to(UP * y)
            lv_label = Text(lab, font="PT Mono", font_size=18, color=TEAL).move_to(RIGHT * 5.5 + UP * y)
            self.add(lv, lv_label)

        # Transition arrows
        arr1 = Arrow(UP * 2.0, UP * 0.0, color=TEAL, buff=0.1,
                     stroke_width=2, max_tip_length_to_length_ratio=0.2)
        arr1.move_to(LEFT * 3.5 + UP * 1.0)
        arr2 = Arrow(UP * 0.0, DOWN * 1.5, color=TEAL, buff=0.1,
                     stroke_width=2, max_tip_length_to_length_ratio=0.2)
        arr2.move_to(LEFT * 3.5 + DOWN * 0.75)

        # Grow in levels already added (create a visible motion)
        highlight_box = Rectangle(width=13.5, height=0.6).set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
        highlight_box.move_to(UP * 2.0)

        conclusion = Text("Plus-one is not a correction. It is the structure.", font=DISPLAY,
                          font_size=22, color=TEAL).move_to(DOWN * 3.0)

        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(highlight_box), run_time=0.6)
        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.8)
        self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(max(0.1, duration - 2.8))


# ---------------------------------------------------------------------------
# B12 — THE EXAMPLE card (CARD beat)
# ---------------------------------------------------------------------------
class B12_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B12", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 2.0)
        headline = Text("The d-orbital: ell = 2", font=DISPLAY, font_size=48,
                        color=INK).move_to(UP * 0.5)
        sub = Text("(illustrative)", font=SERIF, font_size=24,
                   color=SLATE).move_to(DOWN * 0.8)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.1, duration - 1.7))


# ---------------------------------------------------------------------------
# B13 — d-orbital ell=2 example (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_DorbitalExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 18.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("For ell = 2 (d-orbital)", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Ladder of 5 rungs
        rung_y = [-2.0, -1.0, 0.0, 1.0, 2.0]
        rung_labels = ["m=-2", "m=-1", "m=0", "m=+1", "m=+2"]
        rungs_grp = VGroup()
        rlabels_grp = VGroup()
        for y, lab in zip(rung_y, rung_labels):
            r = Line(LEFT * 1.5, RIGHT * 1.5, color=INK, stroke_width=2).move_to(LEFT * 4.5 + UP * y)
            rungs_grp.add(r)
            t = Text(lab, font="PT Mono", font_size=18, color=INK).move_to(LEFT * 2.5 + UP * y)
            rlabels_grp.add(t)

        rails_grp = VGroup(
            Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=1.5).move_to(LEFT * 6.0),
            Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=1.5).move_to(LEFT * 3.0)
        )

        # Right side: two eigenvalue values
        box_naive = Rectangle(width=4.5, height=1.5).set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 2)
        box_naive.move_to(RIGHT * 3.5 + UP * 1.5)
        label_naive = Text("Naive: ell^2 = 4 h-bar^2", font="PT Mono", font_size=20,
                           color=CRIMSON).move_to(RIGHT * 3.5 + UP * 1.5)

        box_actual = Rectangle(width=4.5, height=1.5).set_fill(TEAL, 0.1).set_stroke(TEAL, 2)
        box_actual.move_to(RIGHT * 3.5 + DOWN * 0.3)
        label_actual = Text("Actual: ell(ell+1) = 6 h-bar^2", font="PT Mono", font_size=20,
                            color=TEAL).move_to(RIGHT * 3.5 + DOWN * 0.3)

        extra = Text("Extra: 2 h-bar^2", font="PT Mono", font_size=20,
                     color=TEAL).move_to(RIGHT * 3.5 + DOWN * 1.8)
        extra_label = Text("= commutator cross-term", font=DISPLAY, font_size=18,
                           color=TEAL).move_to(RIGHT * 3.5 + DOWN * 2.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(rails_grp), Create(rungs_grp), run_time=0.8)
        self.play(FadeIn(rlabels_grp), run_time=0.6)
        self.play(GrowFromCenter(box_naive), FadeIn(label_naive), run_time=0.7)
        self.play(GrowFromCenter(box_actual), FadeIn(label_actual), run_time=0.7)
        self.play(FadeIn(extra), FadeIn(extra_label), run_time=0.6)
        self.wait(max(0.1, duration - 4.3))


# ---------------------------------------------------------------------------
# B14 — RECAP endcard (CARD beat)
# ---------------------------------------------------------------------------
class B14_Recap(Scene):
    def construct(self):
        duration = DUR.get("B14", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        line1 = Text("L squared = ell(ell+1),", font=DISPLAY, font_size=34,
                     color=TEAL).move_to(UP * 1.3)
        line2 = Text("not ell squared.", font=SERIF, font_size=32,
                     color=CRIMSON).move_to(UP * 0.5)
        line3 = Text("The extra term is the commutator made visible.", font=SERIF, font_size=28,
                     color=INK).move_to(DOWN * 0.7)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(line1), Write(line2), run_time=1.0)
        self.play(Write(line3), run_time=0.8)
        self.wait(max(0.1, duration - 2.3))
