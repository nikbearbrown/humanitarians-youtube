"""vox_scenes.py — Why the Wrong AI Surface Costs More Than the Wrong Prompt
(vox-surface-routing, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = right surface / context matches / trustworthy output;
           CRIMSON = wrong surface / context mismatch / untrustworthy output.
Never swap mid-film.

Exclusions: NO deep feature comparison of Claude products, NO technical
internals of how each surface works, NO extended automation research citations.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 10.0, "B05": 11.0,
    "B06": 11.0, "B07": 10.0, "B08": 11.0, "B09": 10.0,
    "B10": 10.0, "B11": 10.0, "B12": 10.0, "B14": 11.0,
    "B15": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- B01 — analyst scenario

class B01_AnalystScenario(Scene):
    def construct(self):
        total = DUR["B01"]

        chat_box = Rectangle(width=5.0, height=2.0)
        chat_box.set_fill(SLATE, 0.10).set_stroke(SLATE, 1.6)
        chat_box.move_to(UP * 0.5)
        chat_tag = Text("CLAUDE CHAT", font=DISPLAY, color=SLATE,
                        font_size=18, weight="MEDIUM")
        chat_tag.next_to(chat_box, UP, buff=0.1)

        output_chip = LabelChip("CONFIDENT ANALYSIS", accent=TEAL, size=24)
        output_chip.move_to(UP * 0.6)

        missing_chip = LabelChip("DATA FILES NEVER INCLUDED", accent=CRIMSON, size=20)
        missing_chip.next_to(chat_box, DOWN, buff=0.4)

        self.play(FadeIn(chat_box), FadeIn(chat_tag), run_time=0.6)
        self.play(FadeIn(output_chip), run_time=0.5)
        self.play(FadeIn(missing_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Why didn't the output reveal", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("the context was missing?", font=SERIF,
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

        missing_chip = LabelChip("MISSING CONTEXT", accent=CRIMSON, size=24)
        missing_chip.move_to(LEFT * 3.5)

        arrow = Arrow(LEFT * 1.9, RIGHT * 0.3,
                      color=CRIMSON, stroke_width=3, buff=0.0)

        weak_chip = LabelChip("WEAK OUTPUT", accent=CRIMSON, size=24)
        weak_chip.move_to(RIGHT * 2.8)

        naive_label = SerifLabel("it would be obvious", SLATE, size=24)
        naive_label.next_to(VGroup(missing_chip, weak_chip), DOWN, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(missing_chip), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(weak_chip), run_time=0.5)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


# ---------------------------------------------------------------- B05 — context window comparison

class B05_ContextWindow(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("TWO CONTEXTS — IDENTICAL-LOOKING OUTPUTS", font=DISPLAY,
                   color=SLATE, font_size=16, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.0, color=SLATE, stroke_width=0.8)
        divider.move_to(ORIGIN)

        # Left: pasted notes
        left_head = Text("PASTED NOTES", font=DISPLAY, color=CRIMSON,
                         font_size=18, weight="MEDIUM")
        left_head.move_to(LEFT * 3.3 + UP * 1.5)
        left_ctx = LabelChip("1 NOTE OF 12", accent=CRIMSON, size=20)
        left_ctx.move_to(LEFT * 3.3 + UP * 0.5)
        left_out = LabelChip("CONFIDENT ANALYSIS", accent=TEAL, size=18)
        left_out.move_to(LEFT * 3.3 + DOWN * 0.7)
        left_warn = SerifLabel("based on 1 of 12 files", CRIMSON, size=18)
        left_warn.move_to(LEFT * 3.3 + DOWN * 1.5)

        # Right: full files
        right_head = Text("FULL FILES", font=DISPLAY, color=TEAL,
                          font_size=18, weight="MEDIUM")
        right_head.move_to(RIGHT * 3.3 + UP * 1.5)
        right_ctx = LabelChip("ALL 12 NOTES", accent=TEAL, size=20)
        right_ctx.move_to(RIGHT * 3.3 + UP * 0.5)
        right_out = LabelChip("CONFIDENT ANALYSIS", accent=TEAL, size=18)
        right_out.move_to(RIGHT * 3.3 + DOWN * 0.7)
        right_good = SerifLabel("based on all files", TEAL, size=18)
        right_good.move_to(RIGHT * 3.3 + DOWN * 1.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(left_head), FadeIn(right_head), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(left_ctx), FadeIn(right_ctx), run_time=0.5)
        self.play(FadeIn(left_out), FadeIn(right_out), run_time=0.5)
        self.play(FadeIn(left_warn), FadeIn(right_good), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B06 — three surfaces

class B06_ThreeSurfaces(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("THREE SURFACES — THREE CONTEXT SOURCES", font=DISPLAY,
                   color=SLATE, font_size=16, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Three rows
        chat_chip = LabelChip("CLAUDE CHAT", accent=SLATE, size=22)
        chat_chip.move_to(LEFT * 3.0 + UP * 1.2)
        chat_ctx = SerifLabel("context: typed / pasted", SLATE, size=22)
        chat_ctx.move_to(RIGHT * 1.5 + UP * 1.2)

        code_chip = LabelChip("CLAUDE CODE", accent=SLATE, size=22)
        code_chip.move_to(LEFT * 3.0)
        code_ctx = SerifLabel("context: code repository", TEAL, size=22)
        code_ctx.move_to(RIGHT * 1.5)

        cowork_chip = LabelChip("CLAUDE COWORK", accent=SLATE, size=22)
        cowork_chip.move_to(LEFT * 3.0 + DOWN * 1.2)
        cowork_ctx = SerifLabel("context: files / apps / calendar", TEAL, size=22)
        cowork_ctx.move_to(RIGHT * 1.5 + DOWN * 1.2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(chat_chip), FadeIn(chat_ctx), run_time=0.5)
        self.play(FadeIn(code_chip), FadeIn(code_ctx), run_time=0.5)
        self.play(FadeIn(cowork_chip), FadeIn(cowork_ctx), run_time=0.5)
        self.wait(max(0.5, total - 2.0))


# ---------------------------------------------------------------- B07 — context-access card

class B07_ContextCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("The surface cannot see", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("the context it did not receive.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B08 — Alex and Sam

class B08_AlexSam(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("ALEX vs SAM: SAME TASK, DIFFERENT SURFACES", font=DISPLAY,
                   color=SLATE, font_size=15, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.2, color=SLATE, stroke_width=0.8)
        divider.move_to(ORIGIN)

        alex_head = Text("ALEX", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        alex_head.move_to(LEFT * 3.3 + UP * 1.4)

        sam_head = Text("SAM", font=DISPLAY, color=INK, font_size=22, weight="MEDIUM")
        sam_head.move_to(RIGHT * 3.3 + UP * 1.4)

        alex_method = Text("chat + paste 1 note", font=SERIF, color=CRIMSON, font_size=18)
        alex_method.move_to(LEFT * 3.3 + UP * 0.6)

        sam_method = Text("Cowork + folder", font=SERIF, color=TEAL, font_size=18)
        sam_method.move_to(RIGHT * 3.3 + UP * 0.6)

        alex_out = LabelChip("POLISHED PARAGRAPH", accent=TEAL, size=18)
        alex_out.move_to(LEFT * 3.3 + DOWN * 0.2)

        sam_out = LabelChip("SYNTHESIS + CITATIONS", accent=TEAL, size=18)
        sam_out.move_to(RIGHT * 3.3 + DOWN * 0.2)

        alex_warn = LabelChip("BASED ON 1 OF 12 NOTES", accent=CRIMSON, size=16)
        alex_warn.move_to(LEFT * 3.3 + DOWN * 1.1)

        sam_note = SerifLabel("source log verifiable", TEAL, size=18)
        sam_note.move_to(RIGHT * 3.3 + DOWN * 1.1)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(alex_head), FadeIn(sam_head), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(alex_method), FadeIn(sam_method), run_time=0.5)
        self.play(FadeIn(alex_out), FadeIn(sam_out), run_time=0.5)
        self.play(FadeIn(alex_warn), FadeIn(sam_note), run_time=0.5)
        self.wait(max(0.5, total - 2.7))


# ---------------------------------------------------------------- B09 — five routing questions

class B09_RoutingQuestions(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("FIVE ROUTING QUESTIONS", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        labels = [
            "OUTPUT TYPE",
            "CONTEXT SOURCE",
            "RISK",
            "REVERSIBILITY",
            "VERIFICATION PATH",
        ]
        chips = VGroup(*[LabelChip(l, accent=TEAL, size=20) for l in labels])
        chips.arrange(DOWN, buff=0.3)
        chips.move_to(ORIGIN)

        takes = SerifLabel("takes less than a minute", TEAL, size=22)
        takes.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips],
                              lag_ratio=0.12, run_time=1.5))
        self.play(FadeIn(takes, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B10 — routing decision

class B10_RoutingDecision(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("CONTEXT SOURCE DETERMINES SURFACE", font=DISPLAY, color=TEAL,
                   font_size=17, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Three paths
        clip_chip = LabelChip("CLIPBOARD / TYPED", accent=SLATE, size=20)
        clip_chip.move_to(LEFT * 4.5 + UP * 1.2)
        repo_chip = LabelChip("CODE REPOSITORY", accent=SLATE, size=20)
        repo_chip.move_to(LEFT * 4.5)
        files_chip = LabelChip("FILES / APPS", accent=SLATE, size=20)
        files_chip.move_to(LEFT * 4.5 + DOWN * 1.2)

        a1 = Arrow(LEFT * 2.6 + UP * 1.2, RIGHT * 0.3 + UP * 1.2,
                   color=TEAL, stroke_width=2.5, buff=0.0)
        a2 = Arrow(LEFT * 2.6, RIGHT * 0.3,
                   color=TEAL, stroke_width=2.5, buff=0.0)
        a3 = Arrow(LEFT * 2.6 + DOWN * 1.2, RIGHT * 0.3 + DOWN * 1.2,
                   color=TEAL, stroke_width=2.5, buff=0.0)

        chat_out = LabelChip("CHAT", accent=TEAL, size=22)
        chat_out.move_to(RIGHT * 2.5 + UP * 1.2)
        code_out = LabelChip("CODE", accent=TEAL, size=22)
        code_out.move_to(RIGHT * 2.5)
        cowork_out = LabelChip("COWORK", accent=TEAL, size=22)
        cowork_out.move_to(RIGHT * 2.5 + DOWN * 1.2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(clip_chip), FadeIn(repo_chip), FadeIn(files_chip), run_time=0.6)
        self.play(Create(a1), Create(a2), Create(a3), run_time=0.6)
        self.play(FadeIn(chat_out), FadeIn(code_out), FadeIn(cowork_out), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


# ---------------------------------------------------------------- B11 — the check (decision diamond)

class B11_TheCheck(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("THE ROUTING CHECK", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        diamond = Square(side_length=2.4)
        diamond.rotate(45 * DEGREES)
        diamond.set_fill(GROUND, 1).set_stroke(INK, 2.5)
        diamond.move_to(ORIGIN + UP * 0.2)

        q_line1 = Text("Surface accesses", font=SERIF, color=INK, font_size=18)
        q_line2 = Text("required context?", font=SERIF, color=INK, font_size=18)
        q_block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.1)
        q_block.move_to(diamond)

        yes_label = Text("YES", font=DISPLAY, color=TEAL,
                         font_size=22, weight="BOLD")
        yes_label.next_to(diamond, RIGHT, buff=0.5)

        proceed_chip = LabelChip("PROCEED", accent=TEAL, size=22)
        proceed_chip.next_to(yes_label, RIGHT, buff=0.5)

        no_label = Text("NO", font=DISPLAY, color=CRIMSON,
                        font_size=22, weight="BOLD")
        no_label.next_to(diamond, DOWN, buff=0.5)

        switch_chip = LabelChip("CHOOSE RIGHT SURFACE", accent=CRIMSON, size=18)
        switch_chip.next_to(no_label, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(diamond), FadeIn(q_block), run_time=0.8)
        self.play(FadeIn(yes_label), FadeIn(proceed_chip), run_time=0.6)
        self.play(FadeIn(no_label), FadeIn(switch_chip), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B12 — capability vs fit card

class B12_CapabilityFit(Scene):
    def construct(self):
        total = DUR["B12"]
        t1 = Text("Capability is not fit.", font=SERIF, color=CRIMSON,
                  font_size=46, weight="BOLD")
        t2 = Text("The routing decision is yours.", font=SERIF, color=TEAL,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u1 = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                  color=CRIMSON, stroke_width=2)
        u2 = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                  color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u1), run_time=0.8)
        self.play(FadeIn(t2), Create(u2), run_time=0.8)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B14 — surface-prompt asymmetry card

class B14_AsymmetryCard(Scene):
    def construct(self):
        total = DUR["B14"]
        t1 = Text("No prompt fixes a surface", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("that cannot see the context.", font=SERIF, color=CRIMSON,
                  font_size=42, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B15 — endcard

class B15_End(Scene):
    def construct(self):
        total = DUR["B15"]

        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("Choose the surface that can see", font=SERIF, color=INK,
                  font_size=38, weight="BOLD")
        t2 = Text("what the task requires.", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.8))
