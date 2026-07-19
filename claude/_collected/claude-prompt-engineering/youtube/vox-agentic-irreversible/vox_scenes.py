"""vox_scenes.py — Why 'Clean Up This Folder' Is a Dangerous Instruction
(vox-agentic-irreversible, slate cut, 16:9)

Color law (teardown):
  INK     = specified / bounded / reversible (chat lane, approval gate, safe handoff)
  CRIMSON = unspecified / unbounded / irreversible (agentic lane, missing gate, deletion)

Exclusions: no formal agentic safety taxonomy, no platform comparison,
no reversibility theory.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 12.0, "B05": 11.0, "B06": 11.0,
    "B07": 10.0, "B08": 12.0, "B09": 11.0, "B10": 12.0, "B11": 12.0,
    "B12": 11.0, "B13": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _label(text, color=INK, size=26):
    return Text(text, font=SERIF, color=color, font_size=size)


def _chip(text, accent=SLATE, size=20):
    return LabelChip(text, accent=accent, size=size)


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why 'clean up this folder'", font=SERIF, color=INK, font_size=52, weight=BOLD)
        t2 = Text("is a dangerous instruction", font=SERIF, color=INK, font_size=52, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("conversational request — agentic consequences", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why did a familiar instruction", font=SERIF, color=INK, font_size=48, weight=BOLD)
        q2 = Text("cause irreversible harm?", font=SERIF, color=INK, font_size=48, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_ChatVsAgentic(Scene):
    """Chat lane: prompt → text → human reviews → acts. Agentic lane: prompt → action directly."""
    def construct(self):
        total = DUR["B04"]
        title = _label("Chat: text you review. Agent: action — no review step.", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Chat lane (INK)
        chat_chip = _chip("CHAT", accent=INK, size=20)
        chat_step1 = _label("prompt", INK, 22)
        chat_arr1 = Text("→", font=SERIF, color=SLATE, font_size=22)
        chat_step2 = _label("text output", INK, 22)
        chat_arr2 = Text("→", font=SERIF, color=SLATE, font_size=22)
        chat_step3 = _label("you review", INK, 22)
        chat_arr3 = Text("→", font=SERIF, color=SLATE, font_size=22)
        chat_step4 = _label("act or discard", INK, 22)
        chat_row = VGroup(chat_chip, chat_step1, chat_arr1, chat_step2,
                          chat_arr2, chat_step3, chat_arr3, chat_step4).arrange(RIGHT, buff=0.18)
        chat_row.move_to(UP * 0.5)

        # Agentic lane (CRIMSON)
        agent_chip = _chip("AGENT", accent=CRIMSON, size=20)
        ag_step1 = _label("prompt", CRIMSON, 22)
        ag_arr1 = Text("→", font=SERIF, color=SLATE, font_size=22)
        ag_step2 = _label("action", CRIMSON, 22)
        ag_arr2 = Text("→", font=SERIF, color=CRIMSON, font_size=22)
        ag_step3 = _label("files changed", CRIMSON, 22)
        ag_row = VGroup(agent_chip, ag_step1, ag_arr1, ag_step2,
                        ag_arr2, ag_step3).arrange(RIGHT, buff=0.18)
        ag_row.move_to(DOWN * 0.3)

        note = SerifLabel("the human review step that protected you in chat is gone", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(chat_row, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(ag_row, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B05_GoalVsSpec(Scene):
    """Goal = 'clean up' → agent interprets freely. Spec = bounded execution."""
    def construct(self):
        total = DUR["B05"]
        title = _label("A goal lets the agent define 'clean' — specification does not", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Goal side
        goal_chip = _chip("GOAL", accent=CRIMSON, size=18)
        goal_txt = _label('"clean up this folder"', CRIMSON, 24)
        goal_row = VGroup(goal_chip, goal_txt).arrange(RIGHT, buff=0.3)
        goal_row.move_to(UP * 0.4)

        goal_result = _label("→ agent defines 'clean' from training", CRIMSON, 23)
        goal_result.move_to(UP * 0.0)

        # Spec side
        spec_chip = _chip("SPECIFICATION", accent=INK, size=18)
        spec_txt = _label('"rename files to YYYY-MM-DD format; no deletions"', INK, 22)
        spec_row = VGroup(spec_chip, spec_txt).arrange(RIGHT, buff=0.3)
        spec_row.move_to(DOWN * 0.5)

        spec_result = _label("→ agent executes your definition", INK, 23)
        spec_result.move_to(DOWN * 0.9)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(goal_row), run_time=0.6)
        self.play(FadeIn(goal_result, shift=LEFT * 0.2), run_time=0.6)
        self.play(FadeIn(spec_row), run_time=0.6)
        self.play(FadeIn(spec_result, shift=LEFT * 0.2), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B06_ThreeQuestions(Scene):
    """Three questions every agentic handoff must answer."""
    def construct(self):
        total = DUR["B06"]
        title = _label("Every agentic handoff must answer three questions:", INK, 28)
        title.to_edge(UP, buff=0.6)

        questions = [
            ("WORKSPACE", "What is the exact scope the agent may touch?", INK),
            ("AUTHORIZATION", "What actions is the agent permitted to take?", INK),
            ("PROHIBITION", "What must the agent not do?", CRIMSON),
        ]
        rows = VGroup()
        for label, desc, color in questions:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(DOWN * 0.05)

        note = SerifLabel("without prohibition: everything outside authorization is available", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Approval gates put the", font=DISPLAY, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("human review step back", font=DISPLAY, color=CRIMSON,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_SafeHandoff(Scene):
    """Safe handoff structure: five elements."""
    def construct(self):
        total = DUR["B08"]
        title = _label("The safe handoff has five required elements", INK, 28)
        title.to_edge(UP, buff=0.6)

        elements = [
            ("TASK", "standardize filenames — one sentence", INK),
            ("WORKSPACE", "this folder only — exact path", INK),
            ("AUTHORIZED", "rename files: yes", INK),
            ("PROHIBITED", "delete, move, create folders: no", CRIMSON),
            ("GATE", "list proposed renames — wait for approval", INK),
        ]
        rows = VGroup()
        for label, desc, color in elements:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 22)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.28).move_to(DOWN * 0.05)

        note = SerifLabel("gate → plan reviewed → action taken → outcome verified", INK, size=24)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.18),
                  run_time=1.3)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B09_AnyAgenticTask(Scene):
    """Any agentic task may be irreversible — scale spec to stakes."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Any agentic task can produce irreversible changes", INK, 28)
        title.to_edge(UP, buff=0.6)

        tasks = [
            ("organize a folder", "→ moves, deletes, renames", CRIMSON),
            ("generate drafts", "→ creates or overwrites files", CRIMSON),
            ("extract data from files", "→ reads, reformats, may overwrite", CRIMSON),
        ]
        rows = VGroup()
        for task, risk, color in tasks:
            task_lbl = _label(task, INK, 23)
            arrow = Text("→", font=SERIF, color=SLATE, font_size=22)
            risk_lbl = _label(risk, color, 22)
            row = VGroup(task_lbl, arrow, risk_lbl).arrange(RIGHT, buff=0.25)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to(UP * 0.1)

        note = SerifLabel("scale the specification to the stakes of the task", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B10_BiologistExample(Scene):
    """Biologist: 12 deleted as 'duplicates,' 3 had different content."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Organize sequencing folder — 12 files deleted", INK, 26)
        title.to_edge(UP, buff=0.6)

        steps = [
            ("REQUEST", '"organize my sequencing outputs folder"', INK),
            ("AGENT ACTS", "creates subfolders, moves 47 files", CRIMSON),
            ("DELETES 12", "flagged as duplicates — by filename only", CRIMSON),
            ("REALITY", "3 deleted files had different content", CRIMSON),
        ]
        rows = VGroup()
        for step, desc, color in steps:
            chip = _chip(step, accent=color, size=18)
            desc_lbl = _label(desc, color, 22)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.33).move_to(UP * 0.1)

        note = SerifLabel("log: '12 duplicates removed — no action needed'", CRIMSON, size=24)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B11_BiologistFixed(Scene):
    """Bounded handoff: create subfolders only, no delete, approval gate."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Bounded handoff — no data lost", INK, 28)
        title.to_edge(UP, buff=0.6)

        elements = [
            ("TASK", "create date-based subfolders only", INK),
            ("AUTHORIZED", "create subfolders, move files between them", INK),
            ("PROHIBITED", "do not delete any files", CRIMSON),
            ("GATE", "list proposed structure — wait for approval", INK),
            ("RESULT", "files moved, nothing deleted", INK),
        ]
        rows = VGroup()
        for label, desc, color in elements:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 22)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.28).move_to(DOWN * 0.0)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.18),
                  run_time=1.3)
        self.wait(max(0.5, total - 1.8))


class B12_Practice(Scene):
    """Practice: five elements before any agentic handoff."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Before any agentic handoff, write five things:", INK, 28)
        title.to_edge(UP, buff=0.6)

        elements = [
            ("TASK", "one sentence — what to accomplish", INK),
            ("WORKSPACE", "exact path or boundary", INK),
            ("AUTHORIZED", "list each permitted action", INK),
            ("PROHIBITED", "list each action it must not take", CRIMSON),
            ("GATE", "list proposed changes and wait before acting", INK),
        ]
        rows = VGroup()
        for label, desc, color in elements:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.3).move_to(DOWN * 0.05)

        note = SerifLabel("the agent can only protect what you define", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.18),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("The agent can only protect what you define.", font=SERIF,
                  color=INK, font_size=40, weight=BOLD)
        t2 = Text("Specify before it acts — not after.", font=SERIF,
                  color=INK, font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        topic = Text("PROMPT ENGINEERING", font=DISPLAY, color=SLATE,
                     font_size=22, weight=BOLD)
        topic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.1))
