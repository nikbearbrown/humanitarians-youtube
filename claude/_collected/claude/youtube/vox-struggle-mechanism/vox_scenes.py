"""vox_scenes.py — Why Removing the Struggle Removes the Learning
(vox-struggle-mechanism, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = genuine learning / struggle / synaptic connection;
           CRIMSON = borrowed fluency / AI-assisted / no learning event.
Never swap mid-film.

Exclusions: NO detailed BDNF or synaptic biology beyond the core mechanism,
NO extended spaced-repetition or retrieval-practice theory,
NO Bastani et al. methodology deep-dive.
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


# ---------------------------------------------------------------- B01 — score reversal

class B01_ScoreGap(Scene):
    def construct(self):
        total = DUR["B01"]

        eye = Text("PRACTICE vs EXAM", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Column headers
        prac_head = Text("PRACTICE", font=DISPLAY, color=INK,
                         font_size=22, weight="MEDIUM")
        exam_head = Text("EXAM", font=DISPLAY, color=INK,
                         font_size=22, weight="MEDIUM")
        prac_head.move_to(LEFT * 2.8 + UP * 2.0)
        exam_head.move_to(RIGHT * 2.8 + UP * 2.0)

        # Practice bars: AI bar taller (teal), solo bar shorter
        ai_prac_bar = Rectangle(width=0.9, height=2.6)
        ai_prac_bar.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        ai_prac_bar.move_to(LEFT * 3.3 + DOWN * 0.3)
        ai_prac_bar.align_to(Rectangle(width=0.9, height=0.01).move_to(LEFT * 3.3 + DOWN * 1.6), DOWN)

        solo_prac_bar = Rectangle(width=0.9, height=1.6)
        solo_prac_bar.set_fill(SLATE, 0.55).set_stroke(width=0, opacity=0)
        solo_prac_bar.move_to(LEFT * 2.3 + DOWN * 0.3)
        solo_prac_bar.align_to(Rectangle(width=0.9, height=0.01).move_to(LEFT * 2.3 + DOWN * 1.6), DOWN)

        ai_prac_label = Text("+48%", font=MONO, color=TEAL, font_size=22, weight="BOLD")
        ai_prac_label.next_to(ai_prac_bar, UP, buff=0.12)

        ai_prac_tag = Text("AI", font=DISPLAY, color=INK, font_size=16)
        ai_prac_tag.next_to(ai_prac_bar, DOWN, buff=0.1)
        solo_prac_tag = Text("solo", font=DISPLAY, color=INK, font_size=16)
        solo_prac_tag.next_to(solo_prac_bar, DOWN, buff=0.1)

        # Exam bars: solo bar taller (teal), AI bar shorter (crimson) — reversal
        solo_exam_bar = Rectangle(width=0.9, height=2.0)
        solo_exam_bar.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        solo_exam_bar.move_to(RIGHT * 2.3 + DOWN * 0.3)
        solo_exam_bar.align_to(Rectangle(width=0.9, height=0.01).move_to(RIGHT * 2.3 + DOWN * 1.6), DOWN)

        ai_exam_bar = Rectangle(width=0.9, height=0.8)
        ai_exam_bar.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        ai_exam_bar.move_to(RIGHT * 3.3 + DOWN * 0.3)
        ai_exam_bar.align_to(Rectangle(width=0.9, height=0.01).move_to(RIGHT * 3.3 + DOWN * 1.6), DOWN)

        ai_exam_label = Text("-17 pts", font=MONO, color=CRIMSON, font_size=22, weight="BOLD")
        ai_exam_label.next_to(ai_exam_bar, UP, buff=0.12)

        ai_exam_tag = Text("AI", font=DISPLAY, color=INK, font_size=16)
        ai_exam_tag.next_to(ai_exam_bar, DOWN, buff=0.1)
        solo_exam_tag = Text("solo", font=DISPLAY, color=INK, font_size=16)
        solo_exam_tag.next_to(solo_exam_bar, DOWN, buff=0.1)

        # Baseline
        baseline = Line(LEFT * 5.5 + DOWN * 1.6, RIGHT * 5.5 + DOWN * 1.6,
                        color=INK, stroke_width=1.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(prac_head), FadeIn(exam_head), run_time=0.5)
        self.play(Create(baseline), run_time=0.4)
        self.play(FadeIn(ai_prac_bar), FadeIn(solo_prac_bar),
                  FadeIn(ai_prac_tag), FadeIn(solo_prac_tag), run_time=0.8)
        self.play(FadeIn(ai_prac_label), run_time=0.4)
        self.play(FadeIn(solo_exam_bar), FadeIn(ai_exam_bar),
                  FadeIn(ai_exam_tag), FadeIn(solo_exam_tag), run_time=0.8)
        self.play(FadeIn(ai_exam_label), run_time=0.4)
        self.wait(max(0.5, total - 3.8))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Why did more practice success", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("produce less learning?", font=SERIF,
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

        solved_chip = LabelChip("PROBLEMS SOLVED", accent=TEAL, size=26)
        solved_chip.move_to(LEFT * 3.2)

        arrow = Arrow(LEFT * 1.5, RIGHT * 0.8,
                      color=INK, stroke_width=3, buff=0.0)

        skill_chip = LabelChip("SKILL BUILT", accent=TEAL, size=26)
        skill_chip.move_to(RIGHT * 2.8)

        naive_label = SerifLabel("the naive expectation", SLATE, size=24)
        naive_label.next_to(VGroup(solved_chip, skill_chip), DOWN, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(solved_chip), run_time=0.6)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(skill_chip), run_time=0.6)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B05 — learning chain

class B05_LearningChain(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("THE LEARNING CHAIN", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Vertical stack to stay within safe area and avoid W5 text-on-line
        struggle_chip = LabelChip("COGNITIVE STRUGGLE", accent=TEAL, size=24)
        struggle_chip.move_to(UP * 1.2)

        a1 = Arrow(UP * 0.55, UP * 0.05,
                   color=TEAL, stroke_width=3, buff=0.0)

        error_chip = LabelChip("PREDICTION ERROR FIRES", accent=TEAL, size=24)
        error_chip.move_to(ORIGIN + DOWN * 0.35)

        a2 = Arrow(DOWN * 0.75, DOWN * 1.25,
                   color=TEAL, stroke_width=3, buff=0.0)

        synapse_chip = LabelChip("SYNAPSE STRENGTHENS", accent=TEAL, size=24)
        synapse_chip.move_to(DOWN * 1.65)

        bio_label = SerifLabel("a biological event", TEAL, size=22)
        bio_label.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(struggle_chip), run_time=0.6)
        self.play(Create(a1), run_time=0.4)
        self.play(FadeIn(error_chip), run_time=0.6)
        self.play(Create(a2), run_time=0.4)
        self.play(FadeIn(synapse_chip), run_time=0.6)
        self.play(FadeIn(bio_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.6))


# ---------------------------------------------------------------- B06 — AI intercepts

class B06_TriggerRemoved(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("AI REMOVES THE TRIGGER", font=DISPLAY, color=CRIMSON,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Vertical chain — stays in safe area, no W5 text-on-line
        struggle_chip = LabelChip("COGNITIVE STRUGGLE", accent=TEAL, size=22)
        struggle_chip.move_to(UP * 1.4)

        a1 = Arrow(UP * 0.78, UP * 0.28,
                   color=TEAL, stroke_width=3, buff=0.0)

        error_chip = LabelChip("PREDICTION ERROR", accent=TEAL, size=22)
        error_chip.move_to(ORIGIN + DOWN * 0.05)

        a2 = Arrow(DOWN * 0.42, DOWN * 0.92,
                   color=TEAL, stroke_width=3, buff=0.0)

        synapse_chip = LabelChip("SYNAPSE STRENGTHENS", accent=TEAL, size=22)
        synapse_chip.move_to(DOWN * 1.3)

        chain_group = VGroup(struggle_chip, a1, error_chip, a2, synapse_chip)

        # AI intercept chip to the left of the chain
        ai_chip = LabelChip("AI ANSWERS", accent=CRIMSON, size=26)
        ai_chip.move_to(LEFT * 4.5 + UP * 1.4)

        # Block badge — placed below synapse, not overlapping error_chip
        block_x = Text("BLOCKED", font=DISPLAY, color=CRIMSON,
                       font_size=26, weight="BOLD")
        block_x.move_to(RIGHT * 3.5 + DOWN * 0.7)

        no_trigger = SerifLabel("no trigger — no consolidation", CRIMSON, size=22)
        no_trigger.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(chain_group), run_time=0.8)
        self.play(FadeIn(ai_chip, shift=RIGHT * 0.3), run_time=0.7)
        # Chain grays out — set opacity directly before re-adding
        struggle_chip.set_opacity(0.25)
        a1.set_opacity(0.25)
        error_chip.set_opacity(0.25)
        a2.set_opacity(0.25)
        synapse_chip.set_opacity(0.25)
        self.play(FadeIn(block_x, scale=1.2), run_time=0.6)
        self.play(FadeIn(no_trigger, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.1))


# ---------------------------------------------------------------- B07 — borrowed scores card

class B07_BorrowedCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("The practice scores were", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("borrowed from the machine.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B08 — brain connectivity

class B08_BrainConnectivity(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("BRAIN CONNECTIVITY DURING WRITING", font=DISPLAY, color=SLATE,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Helper: build a node-network at center_x
        def _network(center_x, accent, n_nodes, n_edges, opacity=1.0):
            rng = np.random.default_rng(42 + int(center_x * 10))
            positions = []
            for _ in range(n_nodes):
                angle = rng.uniform(0, 2 * np.pi)
                radius = rng.uniform(0.3, 1.1)
                positions.append(np.array([center_x + np.cos(angle) * radius,
                                           np.sin(angle) * radius * 0.8, 0.0]))
            nodes = VGroup(*[Dot(radius=0.09, color=accent).move_to(p)
                             for p in positions])
            nodes.set_opacity(opacity)

            edges = VGroup()
            chosen = set()
            count = 0
            for _ in range(n_edges * 6):
                if count >= n_edges:
                    break
                i, j = int(rng.integers(0, n_nodes)), int(rng.integers(0, n_nodes))
                if i != j and (i, j) not in chosen:
                    chosen.add((i, j))
                    e = Line(positions[i], positions[j],
                             color=accent, stroke_width=1.4)
                    e.set_opacity(opacity * 0.6)
                    edges.add(e)
                    count += 1
            return VGroup(edges, nodes)

        solo_net = _network(-3.5, TEAL, n_nodes=11, n_edges=28)
        ai_net = _network(3.5, CRIMSON, n_nodes=11, n_edges=8, opacity=0.55)

        solo_label = Text("SOLO STRUGGLE", font=DISPLAY, color=TEAL,
                          font_size=20, weight="MEDIUM")
        solo_label.move_to(LEFT * 3.5 + DOWN * 1.7)

        ai_label = Text("AI-ASSISTED", font=DISPLAY, color=CRIMSON,
                        font_size=20, weight="MEDIUM")
        ai_label.move_to(RIGHT * 3.5 + DOWN * 1.7)

        reduction = Text("−55% connectivity", font=MONO, color=CRIMSON, font_size=24)
        reduction.to_edge(DOWN, buff=0.5)

        divider = Line(UP * 1.5, DOWN * 1.3, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(solo_net), FadeIn(solo_label), run_time=0.8)
        self.play(FadeIn(divider), run_time=0.3)
        self.play(FadeIn(ai_net), FadeIn(ai_label), run_time=0.8)
        self.play(FadeIn(reduction, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B09 — Alexa and Bao

class B09_AlexaBao(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("PRACTICE vs QUIZ", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Row labels
        alexa_head = Text("ALEXA", font=DISPLAY, color=INK,
                          font_size=24, weight="MEDIUM")
        bao_head = Text("BAO", font=DISPLAY, color=INK,
                        font_size=24, weight="MEDIUM")
        alexa_head.move_to(LEFT * 2.8 + UP * 1.4)
        bao_head.move_to(RIGHT * 2.8 + UP * 1.4)

        # Sub-labels
        prac_tag = Text("practice", font=SERIF, color=SLATE, font_size=20)
        quiz_tag = Text("quiz", font=SERIF, color=SLATE, font_size=20)
        prac_tag.move_to(LEFT * 5.5 + UP * 0.3)
        quiz_tag.move_to(LEFT * 5.5 + DOWN * 1.1)

        # Alexa practice = 95% (teal), Bao practice = 60% (teal)
        alexa_prac = Text("95%", font=MONO, color=TEAL, font_size=44, weight="BOLD")
        alexa_prac.move_to(LEFT * 2.8 + UP * 0.3)
        alexa_prac_sub = Text("20 problems, AI-assisted", font=SERIF,
                               color=SLATE, font_size=18)
        alexa_prac_sub.next_to(alexa_prac, DOWN, buff=0.1)

        bao_prac = Text("60%", font=MONO, color=TEAL, font_size=44, weight="BOLD")
        bao_prac.move_to(RIGHT * 2.8 + UP * 0.3)
        bao_prac_sub = Text("12 problems, by hand", font=SERIF,
                             color=SLATE, font_size=18)
        bao_prac_sub.next_to(bao_prac, DOWN, buff=0.1)

        divider = Line(LEFT * 5.8 + DOWN * 0.55, RIGHT * 5.8 + DOWN * 0.55,
                       color=SLATE, stroke_width=1.0)

        # Alexa quiz = 62% (crimson — reversal), Bao quiz = 81% (teal)
        alexa_quiz = Text("62%", font=MONO, color=CRIMSON, font_size=44, weight="BOLD")
        alexa_quiz.move_to(LEFT * 2.8 + DOWN * 1.1)
        bao_quiz = Text("81%", font=MONO, color=TEAL, font_size=44, weight="BOLD")
        bao_quiz.move_to(RIGHT * 2.8 + DOWN * 1.1)

        reversal_label = SerifLabel("the reversal", CRIMSON, size=22)
        reversal_label.move_to(LEFT * 2.8 + DOWN * 2.1)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(alexa_head), FadeIn(bao_head),
                  FadeIn(prac_tag), FadeIn(quiz_tag), run_time=0.6)
        self.play(FadeIn(alexa_prac), FadeIn(alexa_prac_sub),
                  FadeIn(bao_prac), FadeIn(bao_prac_sub), run_time=0.8)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(bao_quiz), run_time=0.6)
        self.play(FadeIn(alexa_quiz, scale=1.1), run_time=0.6)
        self.play(FadeIn(reversal_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 4.0))


# ---------------------------------------------------------------- B10 — artifact/brain card

class B10_ArtifactCard(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("The artifact was fine.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("The brain was unchanged.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B11 — two kinds of AI use

class B11_TwoKinds(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("TWO KINDS OF AI USE", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Row 1: FREES CAPACITY (teal)
        frees_chip = LabelChip("FREES CAPACITY", accent=TEAL, size=24)
        frees_chip.move_to(LEFT * 3.5 + UP * 0.8)

        frees_desc = Text("AI handles formatting / boilerplate\nhuman handles synthesis",
                          font=SERIF, color=INK, font_size=22)
        frees_desc.move_to(RIGHT * 1.5 + UP * 0.8)

        # Row 2: REMOVES STRUGGLE (crimson)
        removes_chip = LabelChip("REMOVES STRUGGLE", accent=CRIMSON, size=24)
        removes_chip.move_to(LEFT * 3.5 + DOWN * 0.9)

        removes_desc = Text("AI handles the synthesis itself",
                            font=SERIF, color=INK, font_size=22)
        removes_desc.move_to(RIGHT * 1.5 + DOWN * 0.9)

        divider = Line(LEFT * 5.8 + DOWN * 0.05, RIGHT * 5.8 + DOWN * 0.05,
                       color=SLATE, stroke_width=0.8)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(frees_chip), run_time=0.5)
        self.play(FadeIn(frees_desc), run_time=0.6)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(removes_chip), run_time=0.5)
        self.play(FadeIn(removes_desc), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


# ---------------------------------------------------------------- B12 — phase gate

class B12_TheGate(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE PHASE GATE", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Timeline
        timeline = Line(LEFT * 5.8, RIGHT * 5.8, color=SLATE, stroke_width=2.0)
        timeline.move_to(ORIGIN)

        # Gate marker
        gate_line = Line(UP * 1.5, DOWN * 1.5, color=INK, stroke_width=3.5)
        gate_line.move_to(ORIGIN)

        # Left side: AI zone
        ai_zone = Rectangle(width=4.8, height=1.4)
        ai_zone.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.6)
        ai_zone.move_to(LEFT * 2.9 + DOWN * 0.0)
        ai_text = Text("AI: scaffold / format", font=DISPLAY, color=INK,
                       font_size=22, weight="MEDIUM")
        ai_text.move_to(ai_zone)

        # Right side: human zone (teal)
        human_zone = Rectangle(width=4.8, height=1.4)
        human_zone.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.6)
        human_zone.move_to(RIGHT * 2.9)
        human_text = Text("HUMAN: reasoning / synthesis", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        human_text.move_to(human_zone)

        gate_label = SerifLabel("where learning lives", TEAL, size=22)
        gate_label.next_to(human_zone, DOWN, buff=0.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(Create(timeline), run_time=0.5)
        self.play(FadeIn(ai_zone), FadeIn(ai_text), run_time=0.6)
        self.play(Create(gate_line), run_time=0.4)
        self.play(FadeIn(human_zone), FadeIn(human_text), run_time=0.6)
        self.play(FadeIn(gate_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.1))


# ---------------------------------------------------------------- B14 — the check (decision diamond)

class B14_TheCheck(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("THE CHECK BEFORE DELEGATING", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Diamond shape using a rotated square
        diamond = Square(side_length=2.2)
        diamond.rotate(45 * DEGREES)
        diamond.set_fill(GROUND, 1).set_stroke(INK, 2.5)
        diamond.move_to(ORIGIN + UP * 0.1)

        q_line1 = Text("Is this the struggle", font=SERIF, color=INK, font_size=20)
        q_line2 = Text("that builds the skill?", font=SERIF, color=INK, font_size=20)
        q_block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.1)
        q_block.move_to(diamond)

        # YES branch: right, teal
        yes_label = Text("YES", font=DISPLAY, color=TEAL,
                         font_size=22, weight="BOLD")
        yes_label.next_to(diamond, RIGHT, buff=0.5)

        do_it_chip = LabelChip("DO IT YOURSELF", accent=TEAL, size=22)
        do_it_chip.next_to(yes_label, RIGHT, buff=0.5)

        # NO branch: down, slate
        no_label = Text("NO", font=DISPLAY, color=SLATE,
                        font_size=22, weight="BOLD")
        no_label.next_to(diamond, DOWN, buff=0.5)

        ai_it_chip = LabelChip("AI HANDLES IT", accent=SLATE, size=22)
        ai_it_chip.next_to(no_label, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(diamond), FadeIn(q_block), run_time=0.8)
        self.play(FadeIn(yes_label), FadeIn(do_it_chip), run_time=0.6)
        self.play(FadeIn(no_label), FadeIn(ai_it_chip), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B15 — principle card

class B15_PrincipleCard(Scene):
    def construct(self):
        total = DUR["B15"]
        t1 = Text("The struggle is not the price.", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("It is the mechanism.", font=SERIF, color=TEAL,
                  font_size=42, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B16 — endcard

class B16_End(Scene):
    def construct(self):
        total = DUR["B16"]

        # Kicker topic
        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("Struggle removed =", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("learning removed.", font=SERIF, color=CRIMSON,
                  font_size=40, weight="BOLD")
        t3 = Text("You cannot borrow the learning event.", font=SERIF,
                  color=INK, font_size=32)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))
