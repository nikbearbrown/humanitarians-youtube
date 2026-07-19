"""vox_scenes.py — Why Code That Looks Correct Can Still Be Wrong
(vox-code-oracle, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = verified / oracle-passed / correct;
           CRIMSON = unverified / appearance-only / wrong.
Never swap mid-film.

Exclusions: NO formal verification or proof-based methods, NO extended test
coverage metrics, NO fuzzing or property-based testing.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 10.0, "B03": 10.0, "B04": 11.0, "B05": 12.0,
    "B06": 12.0, "B07": 11.0, "B08": 12.0, "B09": 13.0,
    "B10": 11.0, "B11": 12.0, "B12": 12.0, "B14": 12.0,
    "B15": 10.0, "B16": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- B01 — code fails

class B01_CodeFails(Scene):
    def construct(self):
        total = DUR["B01"]

        code_box = Rectangle(width=3.2, height=1.8)
        code_box.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        code_box.move_to(LEFT * 3.5)
        code_label = Text("AI-FIXED CODE", font=DISPLAY, color=INK,
                          font_size=20, weight="MEDIUM")
        code_label.move_to(LEFT * 3.5 + UP * 0.3)
        looks_ok = Text("looks correct", font=SERIF, color=TEAL, font_size=18)
        looks_ok.move_to(LEFT * 3.5 + DOWN * 0.3)

        arrow = Arrow(LEFT * 1.8, RIGHT * 0.0,
                      color=INK, stroke_width=3, buff=0.0)

        fail_box = Rectangle(width=3.2, height=1.8)
        fail_box.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.8)
        fail_box.move_to(RIGHT * 3.5)
        fail_label = Text("TESTS FAIL", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        fail_label.move_to(RIGHT * 3.5 + UP * 0.3)
        new_way = Text("in a new way", font=SERIF, color=CRIMSON, font_size=18)
        new_way.move_to(RIGHT * 3.5 + DOWN * 0.3)

        self.play(FadeIn(code_box), FadeIn(code_label), FadeIn(looks_ok), run_time=0.7)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(fail_box), FadeIn(fail_label), FadeIn(new_way), run_time=0.7)
        self.wait(max(0.5, total - 1.9))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Why can't the appearance of code", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("tell you if it's right?", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.16, q2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B04 — naive model

class B04_NaiveModel(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = Text("THE NAIVE EXPECTATION", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.7)

        looks_chip = LabelChip("LOOKS CORRECT", accent=TEAL, size=26)
        looks_chip.move_to(LEFT * 3.2)

        arrow = Arrow(LEFT * 1.5, RIGHT * 0.6,
                      color=TEAL, stroke_width=3, buff=0.0)

        is_chip = LabelChip("IS CORRECT", accent=TEAL, size=26)
        is_chip.move_to(RIGHT * 2.8)

        naive_label = SerifLabel("the naive expectation", SLATE, size=24)
        naive_label.next_to(VGroup(looks_chip, is_chip), DOWN, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(looks_chip), run_time=0.6)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(is_chip), run_time=0.6)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B05 — oracle chain

class B05_OracleChain(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("THE ORACLE CHAIN", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Vertical chain to stay safe
        code_chip = LabelChip("CODE", accent=SLATE, size=26)
        code_chip.move_to(UP * 1.3)

        a1 = Arrow(UP * 0.72, UP * 0.22,
                   color=TEAL, stroke_width=3, buff=0.0)
        run_label = Text("run oracle", font=SERIF, color=TEAL, font_size=18)
        run_label.next_to(a1, RIGHT, buff=0.15)

        oracle_chip = LabelChip("RUN ORACLE", accent=TEAL, size=26)
        oracle_chip.move_to(ORIGIN + DOWN * 0.12)

        a2 = Arrow(DOWN * 0.58, DOWN * 1.08,
                   color=TEAL, stroke_width=3, buff=0.0)

        verdict_chip = LabelChip("VERDICT", accent=TEAL, size=26)
        verdict_chip.move_to(DOWN * 1.48)

        verdict_note = SerifLabel("tests pass or fail — not looks plausible", TEAL, size=22)
        verdict_note.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(code_chip), run_time=0.5)
        self.play(Create(a1), FadeIn(run_label), run_time=0.5)
        self.play(FadeIn(oracle_chip), run_time=0.5)
        self.play(Create(a2), run_time=0.4)
        self.play(FadeIn(verdict_chip), run_time=0.5)
        self.play(FadeIn(verdict_note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


# ---------------------------------------------------------------- B06 — fluency vs verification

class B06_FluencyVsVerify(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("FLUENCY vs VERIFICATION", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Left column: FLUENCY
        fluency_head = Text("FLUENCY", font=DISPLAY, color=SLATE,
                            font_size=22, weight="MEDIUM")
        fluency_head.move_to(LEFT * 3.5 + UP * 1.5)

        ai_box = Rectangle(width=3.0, height=1.2)
        ai_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.8)
        ai_box.move_to(LEFT * 3.5 + UP * 0.4)
        ai_text = Text("AI generates code", font=SERIF, color=INK, font_size=20)
        ai_text.move_to(ai_box)

        fluency_out = LabelChip("LOOKS CORRECT", accent=TEAL, size=20)
        fluency_out.move_to(LEFT * 3.5 + DOWN * 0.9)

        no_oracle = SerifLabel("no internal oracle", CRIMSON, size=20)
        no_oracle.move_to(LEFT * 3.5 + DOWN * 1.7)

        # Divider
        divider = Line(UP * 2.0, DOWN * 2.0, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        # Right column: VERIFICATION
        verify_head = Text("VERIFICATION", font=DISPLAY, color=TEAL,
                           font_size=22, weight="MEDIUM")
        verify_head.move_to(RIGHT * 3.5 + UP * 1.5)

        run_box = Rectangle(width=3.0, height=1.2)
        run_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.8)
        run_box.move_to(RIGHT * 3.5 + UP * 0.4)
        run_text = Text("oracle runs tests", font=SERIF, color=INK, font_size=20)
        run_text.move_to(run_box)

        verify_out = LabelChip("PASS / FAIL", accent=TEAL, size=20)
        verify_out.move_to(RIGHT * 3.5 + DOWN * 0.9)

        verdict_note = SerifLabel("external, deterministic", TEAL, size=20)
        verdict_note.move_to(RIGHT * 3.5 + DOWN * 1.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(fluency_head), FadeIn(verify_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(ai_box), FadeIn(ai_text), FadeIn(run_box), FadeIn(run_text), run_time=0.7)
        self.play(FadeIn(fluency_out), FadeIn(verify_out), run_time=0.5)
        self.play(FadeIn(no_oracle), FadeIn(verdict_note), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B07 — practitioner rule card

class B07_PractitionerRule(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Trust the oracle,", font=SERIF, color=TEAL,
                  font_size=52, weight="BOLD")
        t2 = Text("not the output.", font=SERIF, color=INK,
                  font_size=52, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B08 — oracle effect comparison

class B08_OracleEffect(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("ORACLE PRESENT vs ABSENT", font=DISPLAY, color=SLATE,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.0, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        # Left: WITH ORACLE
        with_head = Text("WITH ORACLE", font=DISPLAY, color=TEAL,
                         font_size=20, weight="MEDIUM")
        with_head.move_to(LEFT * 3.3 + UP * 1.4)

        w_steps = VGroup(
            LabelChip("CODE", accent=SLATE, size=18),
            LabelChip("TESTS RUN", accent=TEAL, size=18),
            LabelChip("PASS", accent=TEAL, size=18),
        ).arrange(DOWN, buff=0.4)
        w_steps.move_to(LEFT * 3.3 + DOWN * 0.2)

        speedup = SerifLabel("bounded gain, known risk", TEAL, size=20)
        speedup.move_to(LEFT * 3.3 + DOWN * 1.8)

        # Right: NO ORACLE
        no_head = Text("NO ORACLE", font=DISPLAY, color=CRIMSON,
                       font_size=20, weight="MEDIUM")
        no_head.move_to(RIGHT * 3.3 + UP * 1.4)

        n_steps = VGroup(
            LabelChip("CODE", accent=SLATE, size=18),
            LabelChip("LOOKS PLAUSIBLE", accent=SLATE, size=18),
            LabelChip("UNKNOWN", accent=CRIMSON, size=18),
        ).arrange(DOWN, buff=0.4)
        n_steps.move_to(RIGHT * 3.3 + DOWN * 0.2)

        risk = SerifLabel("review burden grows", CRIMSON, size=20)
        risk.move_to(RIGHT * 3.3 + DOWN * 1.8)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(with_head), FadeIn(no_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(w_steps), FadeIn(n_steps), run_time=0.8)
        self.play(FadeIn(speedup), FadeIn(risk), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


# ---------------------------------------------------------------- B09 — off-by-one example

class B09_OffByOne(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("THE SILENT FAILURE", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Two function boxes
        orig_box = Rectangle(width=3.6, height=1.8)
        orig_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.8)
        orig_box.move_to(LEFT * 3.3 + UP * 0.4)
        orig_label = Text("ORIGINAL", font=DISPLAY, color=INK,
                          font_size=18, weight="MEDIUM")
        orig_label.move_to(LEFT * 3.3 + UP * 0.8)
        orig_err = LabelChip("KeyError", accent=CRIMSON, size=18)
        orig_err.move_to(LEFT * 3.3 + DOWN * 0.2)

        fix_box = Rectangle(width=3.6, height=1.8)
        fix_box.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        fix_box.move_to(RIGHT * 3.3 + UP * 0.4)
        fix_label = Text("AI FIX", font=DISPLAY, color=INK,
                         font_size=18, weight="MEDIUM")
        fix_label.move_to(RIGHT * 3.3 + UP * 0.8)
        fix_ok = Text("looks clean", font=SERIF, color=TEAL, font_size=18)
        fix_ok.move_to(RIGHT * 3.3 + DOWN * 0.2)

        # Hidden edge case badge
        edge_chip = LabelChip("EMPTY INPUT: wrong output", accent=CRIMSON, size=18)
        edge_chip.move_to(RIGHT * 3.3 + DOWN * 1.1)

        shipped = Text("shipped to 40 clients", font=MONO, color=CRIMSON,
                       font_size=22, weight="BOLD")
        shipped.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(orig_box), FadeIn(orig_label), FadeIn(orig_err), run_time=0.6)
        self.play(FadeIn(fix_box), FadeIn(fix_label), FadeIn(fix_ok), run_time=0.6)
        self.play(FadeIn(edge_chip, scale=0.9), run_time=0.6)
        self.play(FadeIn(shipped, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B10 — appearance card

class B10_AppearanceCard(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Appearance is not evidence.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        t2 = Text("The oracle is the arbiter.", font=SERIF, color=TEAL,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u1 = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                  color=CRIMSON, stroke_width=2)
        u2 = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                  color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u1), run_time=0.8)
        self.play(FadeIn(t2), Create(u2), run_time=0.8)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B11 — two workflows

class B11_TwoWorkflows(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("CHAT vs AGENT — ORACLE PRESENCE", font=DISPLAY, color=SLATE,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.0, color=SLATE, stroke_width=0.8)
        divider.move_to(ORIGIN)

        # Top row: CHAT (no oracle)
        chat_head = Text("CHAT", font=DISPLAY, color=CRIMSON,
                         font_size=20, weight="MEDIUM")
        chat_head.move_to(LEFT * 3.5 + UP * 1.4)

        chat_chips = VGroup(
            LabelChip("PASTE CODE", accent=SLATE, size=18),
            LabelChip("AI OUTPUT", accent=SLATE, size=18),
            LabelChip("NO ORACLE", accent=CRIMSON, size=18),
        ).arrange(DOWN, buff=0.38)
        chat_chips.move_to(LEFT * 3.5 + DOWN * 0.0)

        # Bottom row: AGENT (oracle)
        agent_head = Text("AGENT", font=DISPLAY, color=TEAL,
                          font_size=20, weight="MEDIUM")
        agent_head.move_to(RIGHT * 3.5 + UP * 1.4)

        agent_chips = VGroup(
            LabelChip("REPO CONTEXT", accent=SLATE, size=18),
            LabelChip("AI EDITS + RUNS", accent=TEAL, size=18),
            LabelChip("ORACLE VERDICT", accent=TEAL, size=18),
        ).arrange(DOWN, buff=0.38)
        agent_chips.move_to(RIGHT * 3.5 + DOWN * 0.0)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(chat_head), FadeIn(agent_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(chat_chips), run_time=0.6)
        self.play(FadeIn(agent_chips), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B12 — oracle gate

class B12_TheGate(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE ORACLE GATE", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        code_chip = LabelChip("AI CODE", accent=SLATE, size=24)
        code_chip.move_to(LEFT * 4.5)

        a1 = Arrow(LEFT * 3.2, LEFT * 1.8,
                   color=SLATE, stroke_width=3, buff=0.0)

        gate_box = Rectangle(width=2.2, height=1.6)
        gate_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2.2)
        gate_box.move_to(LEFT * 0.5)
        gate_text = Text("ORACLE\nGATE", font=DISPLAY, color=INK,
                         font_size=18, weight="MEDIUM")
        gate_text.move_to(gate_box)

        a2 = Arrow(RIGHT * 0.7, RIGHT * 2.3,
                   color=TEAL, stroke_width=3, buff=0.0)

        accept_chip = LabelChip("ACCEPT", accent=TEAL, size=24)
        accept_chip.move_to(RIGHT * 4.0)

        gate_q = SerifLabel("what test or build verifies this?", TEAL, size=22)
        gate_q.next_to(gate_box, DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(code_chip), run_time=0.4)
        self.play(Create(a1), run_time=0.4)
        self.play(FadeIn(gate_box), FadeIn(gate_text), run_time=0.5)
        self.play(FadeIn(gate_q, shift=UP * 0.1), run_time=0.5)
        self.play(Create(a2), FadeIn(accept_chip), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B14 — the check

class B14_TheCheck(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("THE ORACLE CHECK", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        diamond = Square(side_length=2.2)
        diamond.rotate(45 * DEGREES)
        diamond.set_fill(GROUND, 1).set_stroke(INK, 2.5)
        diamond.move_to(ORIGIN + UP * 0.1)

        q_line1 = Text("Can you name", font=SERIF, color=INK, font_size=20)
        q_line2 = Text("the oracle?", font=SERIF, color=INK, font_size=20)
        q_block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.1)
        q_block.move_to(diamond)

        yes_label = Text("YES", font=DISPLAY, color=TEAL,
                         font_size=22, weight="BOLD")
        yes_label.next_to(diamond, RIGHT, buff=0.5)

        run_chip = LabelChip("RUN IT", accent=TEAL, size=22)
        run_chip.next_to(yes_label, RIGHT, buff=0.5)

        no_label = Text("NO", font=DISPLAY, color=CRIMSON,
                        font_size=22, weight="BOLD")
        no_label.next_to(diamond, DOWN, buff=0.5)

        stop_chip = LabelChip("APPEARANCE JUDGMENT — STOP", accent=CRIMSON, size=18)
        stop_chip.next_to(no_label, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(diamond), FadeIn(q_block), run_time=0.8)
        self.play(FadeIn(yes_label), FadeIn(run_chip), run_time=0.6)
        self.play(FadeIn(no_label), FadeIn(stop_chip), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B15 — principle card

class B15_PrincipleCard(Scene):
    def construct(self):
        total = DUR["B15"]
        t1 = Text("Trust the oracle,", font=SERIF, color=TEAL,
                  font_size=46, weight="BOLD")
        t2 = Text("not the surface.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B16 — endcard

class B16_End(Scene):
    def construct(self):
        total = DUR["B16"]

        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("Appearance is not evidence.", font=SERIF, color=CRIMSON,
                  font_size=38, weight="BOLD")
        t2 = Text("Run the oracle.", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u1 = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                  color=CRIMSON, stroke_width=2)
        u2 = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                  color=TEAL, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), Create(u1), run_time=0.7)
        self.play(FadeIn(t2), Create(u2), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
