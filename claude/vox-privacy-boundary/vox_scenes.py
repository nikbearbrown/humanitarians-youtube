"""vox_scenes.py — Why 'Claude is Private' Is Not the Privacy Question
(vox-privacy-boundary, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = scoped / intentional / appropriate access;
           CRIMSON = over-broad / unintended / outside intended boundary.
Never swap mid-film.

Exclusions: NO HIPAA/FERPA compliance detail, NO extended legal analysis
of data governance, NO enterprise-vs-personal-plan comparison beyond one
spoken aside.
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


# ---------------------------------------------------------------- B01 — folder grant

class B01_FolderGrant(Scene):
    def construct(self):
        total = DUR["B01"]

        folder_chip = LabelChip("DOCUMENTS FOLDER", accent=SLATE, size=22)
        folder_chip.move_to(UP * 1.2)

        granted_chip = LabelChip("ACCESS GRANTED", accent=TEAL, size=20)
        granted_chip.move_to(UP * 0.3)

        intended_chip = LabelChip("FUNDER REPORT", accent=TEAL, size=20)
        intended_chip.move_to(LEFT * 3.0 + DOWN * 0.9)

        client_chip = LabelChip("CLIENT INTAKE FILES", accent=CRIMSON, size=18)
        client_chip.move_to(ORIGIN + DOWN * 0.9)

        salary_chip = LabelChip("STAFF SALARY DATA", accent=CRIMSON, size=18)
        salary_chip.move_to(RIGHT * 3.0 + DOWN * 0.9)

        note = SerifLabel("all three in scope", CRIMSON, size=20)
        note.move_to(ORIGIN + DOWN * 1.9)

        self.play(FadeIn(folder_chip), run_time=0.5)
        self.play(FadeIn(granted_chip), run_time=0.4)
        self.play(FadeIn(intended_chip), run_time=0.4)
        self.play(FadeIn(client_chip), FadeIn(salary_chip), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.2))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Why didn't 'grant access'", font=SERIF,
                  color=INK, font_size=38, weight="BOLD")
        q2 = Text("mean 'grant access to the right files'?", font=SERIF,
                  color=INK, font_size=38, weight="BOLD")
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.16, q2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.6)
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

        folder_chip = LabelChip("FOLDER GRANT", accent=SLATE, size=22)
        folder_chip.move_to(LEFT * 3.3)

        arrow = Arrow(LEFT * 1.7, RIGHT * 0.3,
                      color=TEAL, stroke_width=3, buff=0.0)

        relevant_chip = LabelChip("RELEVANT FILES ONLY", accent=TEAL, size=20)
        relevant_chip.move_to(RIGHT * 2.8)

        naive_label = SerifLabel("platform filters automatically", SLATE, size=22)
        naive_label.move_to(ORIGIN + DOWN * 1.3)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(folder_chip), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(relevant_chip), run_time=0.5)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


# ---------------------------------------------------------------- B05 — configuration reframe card

class B05_ConfigCard(Scene):
    def construct(self):
        total = DUR["B05"]
        t1 = Text("Privacy is a configuration question,", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        t2 = Text("not a platform property.", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B06 — three surface boundaries

class B06_SurfaceBoundaries(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("THREE SURFACES — THREE ACCESS BOUNDARIES", font=DISPLAY,
                   color=SLATE, font_size=15, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        chat_chip = LabelChip("CHAT", accent=TEAL, size=22)
        chat_chip.move_to(LEFT * 3.5 + UP * 1.2)
        chat_ctx = SerifLabel("pasted text + uploads only", TEAL, size=20)
        chat_ctx.move_to(RIGHT * 1.3 + UP * 1.2)

        code_chip = LabelChip("CODE", accent=TEAL, size=22)
        code_chip.move_to(LEFT * 3.5)
        code_ctx = SerifLabel("repository files + commands", TEAL, size=20)
        code_ctx.move_to(RIGHT * 1.3)

        cowork_chip = LabelChip("COWORK", accent=CRIMSON, size=22)
        cowork_chip.move_to(LEFT * 3.5 + DOWN * 1.2)
        cowork_ctx = SerifLabel("files + apps + browser + tasks", CRIMSON, size=20)
        cowork_ctx.move_to(RIGHT * 1.3 + DOWN * 1.2)

        note = SerifLabel("each surface expands what Claude can reach", SLATE, size=18)
        note.move_to(ORIGIN + DOWN * 2.1)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(chat_chip), FadeIn(chat_ctx), run_time=0.5)
        self.play(FadeIn(code_chip), FadeIn(code_ctx), run_time=0.5)
        self.play(FadeIn(cowork_chip), FadeIn(cowork_ctx), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.4))


# ---------------------------------------------------------------- B07 — default inclusion card

class B07_DefaultInclusion(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Nothing is excluded by default.", font=SERIF, color=CRIMSON,
                  font_size=42, weight="BOLD")
        t2 = Text("Only what you explicitly exclude.", font=SERIF, color=TEAL,
                  font_size=42, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u1 = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                  color=CRIMSON, stroke_width=2)
        u2 = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                  color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u1), run_time=0.8)
        self.play(FadeIn(t2), Create(u2), run_time=0.8)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B08 — before vs after

class B08_BeforeAfter(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("BROAD GRANT vs SCOPED WORKING FOLDER", font=DISPLAY,
                   color=SLATE, font_size=15, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        divider = Line(UP * 1.8, DOWN * 2.2, color=SLATE, stroke_width=0.8)
        divider.move_to(ORIGIN)

        before_head = Text("BEFORE", font=DISPLAY, color=CRIMSON,
                           font_size=20, weight="MEDIUM")
        before_head.move_to(LEFT * 3.3 + UP * 1.4)

        after_head = Text("AFTER", font=DISPLAY, color=TEAL,
                          font_size=20, weight="MEDIUM")
        after_head.move_to(RIGHT * 3.3 + UP * 1.4)

        before_folder = LabelChip("DOCUMENTS FOLDER", accent=CRIMSON, size=18)
        before_folder.move_to(LEFT * 3.3 + UP * 0.6)

        after_folder = LabelChip("CLAUDE-WORKING", accent=TEAL, size=18)
        after_folder.move_to(RIGHT * 3.3 + UP * 0.6)

        before_note = SerifLabel("everything in scope", CRIMSON, size=18)
        before_note.move_to(LEFT * 3.3 + DOWN * 0.2)

        after_note = SerifLabel("grant materials only", TEAL, size=18)
        after_note.move_to(RIGHT * 3.3 + DOWN * 0.2)

        before_warn = LabelChip("CLIENT + SALARY + TRANSCRIPTS", accent=CRIMSON, size=14)
        before_warn.move_to(LEFT * 3.3 + DOWN * 1.05)

        after_ok = SerifLabel("others excluded", TEAL, size=18)
        after_ok.move_to(RIGHT * 3.3 + DOWN * 1.05)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(before_head), FadeIn(after_head), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(before_folder), FadeIn(after_folder), run_time=0.5)
        self.play(FadeIn(before_note), FadeIn(after_note), run_time=0.5)
        self.play(FadeIn(before_warn), FadeIn(after_ok), run_time=0.5)
        self.wait(max(0.5, total - 2.7))


# ---------------------------------------------------------------- B09 — practice steps

class B09_PracticeSteps(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("THREE STEPS BEFORE GRANTING ACCESS", font=DISPLAY, color=TEAL,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        labels = [
            "CREATE DEDICATED WORKING FOLDER",
            "COPY ONLY WHAT THE TASK NEEDS",
            "NAME WHAT TO EXCLUDE",
        ]
        chips = VGroup(*[LabelChip(l, accent=TEAL, size=20) for l in labels])
        chips.arrange(DOWN, buff=0.4)
        chips.move_to(ORIGIN)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips],
                              lag_ratio=0.18, run_time=1.2))
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B10 — boundary check card

class B10_BoundaryCheck(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Does everything in this boundary", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("belong in this session?", font=SERIF, color=TEAL,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B11 — configuration reframe card

class B11_ConfigReframe(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Not: is Claude private?", font=SERIF, color=CRIMSON,
                  font_size=38, weight="BOLD")
        t2 = Text("But: what did I configure?", font=SERIF, color=TEAL,
                  font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        u1 = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                  color=CRIMSON, stroke_width=2)
        u2 = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                  color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u1), run_time=0.8)
        self.play(FadeIn(t2), Create(u2), run_time=0.8)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B12 — working folder diagram

class B12_WorkingFolder(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE ACCESS GRANT IS THE PRIVACY DECISION", font=DISPLAY,
                   color=SLATE, font_size=15, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        docs_chip = LabelChip("DOCUMENTS FOLDER", accent=CRIMSON, size=22)
        docs_chip.move_to(LEFT * 3.0 + UP * 0.2)
        docs_note = SerifLabel("everything", CRIMSON, size=20)
        docs_note.move_to(LEFT * 3.0 + DOWN * 0.65)

        arrow = Arrow(LEFT * 0.8, RIGHT * 0.8,
                      color=TEAL, stroke_width=2.5, buff=0.0)
        arrow_label = SerifLabel("set before the session", TEAL, size=18)
        arrow_label.move_to(ORIGIN + DOWN * 0.6)

        work_chip = LabelChip("CLAUDE-WORKING", accent=TEAL, size=22)
        work_chip.move_to(RIGHT * 3.0 + UP * 0.2)
        work_note = SerifLabel("grant materials only", TEAL, size=20)
        work_note.move_to(RIGHT * 3.0 + DOWN * 0.65)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(docs_chip), FadeIn(docs_note), run_time=0.5)
        self.play(Create(arrow), FadeIn(arrow_label), run_time=0.5)
        self.play(FadeIn(work_chip), FadeIn(work_note), run_time=0.5)
        self.wait(max(0.5, total - 2.0))


# ---------------------------------------------------------------- B14 — folder preparation card

class B14_FolderPrep(Scene):
    def construct(self):
        total = DUR["B14"]
        t1 = Text("Trust your folder preparation,", font=SERIF, color=TEAL,
                  font_size=40, weight="BOLD")
        t2 = Text("not just the platform.", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.wait(max(0.5, total - 1.6))


# ---------------------------------------------------------------- B15 — endcard

class B15_End(Scene):
    def construct(self):
        total = DUR["B15"]

        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("Set the boundary", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("before the session begins.", font=SERIF, color=TEAL,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.8))
