"""vox_scenes.py — Why 'Improve This' Is a Wish, Not an Instruction
(vox-prompt-six-slots, slate cut, 16:9)

Color law (teardown):
  INK     = filled slot / specified component
  CRIMSON = empty slot / generic guess
  SLATE   = neutral structure

Exclusions: no chain-of-thought research, no XML syntax, no framework comparisons.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 12.0, "B05": 12.0, "B06": 11.0,
    "B07": 10.0, "B08": 9.0, "B09": 13.0, "B10": 10.0, "B11": 12.0,
    "B12": 11.0, "B13": 11.0, "B14": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

SLOTS = ["TASK", "CONTEXT", "SOURCES", "CONSTRAINTS", "FORMAT", "EVALUATION"]


def _label(text, color=INK, size=26):
    return Text(text, font=SERIF, color=color, font_size=size)


def _chip(text, accent=SLATE, size=20):
    return LabelChip(text, accent=accent, size=size)


def _slot_row(name, filled=False, fill_text="", size=22):
    """A slot label + either empty box or filled box."""
    slot_lbl = Text(name, font=DISPLAY, color=INK if filled else CRIMSON,
                    font_size=size, weight=BOLD)
    box = Rectangle(width=3.8, height=0.32)
    if filled:
        box.set_fill(INK, 0.12).set_stroke(INK, 1.5)
        content = Text(fill_text, font=SERIF, color=INK, font_size=size - 2)
        content.move_to(box.get_center())
    else:
        box.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        content = Text("?", font=SERIF, color=CRIMSON, font_size=size)
        content.move_to(box.get_center())
    row = VGroup(slot_lbl, box)
    row.arrange(RIGHT, buff=0.3)
    return row, content


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why 'Improve this'", font=SERIF, color=INK, font_size=54, weight=BOLD)
        t2 = Text("is a wish, not an instruction", font=SERIF, color=INK, font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("six missing decisions, six generic guesses", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why did a well-meaning improvement", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        q2 = Text("produce the wrong output?", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_SixSlots(Scene):
    """Six prompt slots — all empty (crimson question marks)."""
    def construct(self):
        total = DUR["B04"]
        title = _label("A prompt has six slots", INK, 30)
        title.to_edge(UP, buff=0.6)
        rows = VGroup()
        contents = VGroup()
        for name in SLOTS:
            row, content = _slot_row(name, filled=False)
            rows.add(row)
            contents.add(content)
        rows.arrange(DOWN, buff=0.22).move_to(DOWN * 0.2)
        # reposition contents inside boxes
        for row, content in zip(rows, contents):
            content.move_to(row[1].get_center())
        note = SerifLabel("'Improve this' answers none of them", CRIMSON, size=26)
        note.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.12), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c) for c in contents], lag_ratio=0.12), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.1))


class B05_GenericGuesses(Scene):
    """Six slots filled with Claude's generic defaults."""
    def construct(self):
        total = DUR["B05"]
        title = _label("Claude fills all six with plausible defaults", INK, 30)
        title.to_edge(UP, buff=0.6)
        fills = [
            ("TASK", "make it clearer"),
            ("CONTEXT", "general academic reader"),
            ("SOURCES", "the text provided"),
            ("CONSTRAINTS", "standard academic norms"),
            ("FORMAT", "prose paragraphs"),
            ("EVALUATION", "reads well"),
        ]
        rows = VGroup()
        contents = VGroup()
        for name, fill in fills:
            row, content = _slot_row(name, filled=True, fill_text=fill)
            rows.add(row)
            contents.add(content)
        rows.arrange(DOWN, buff=0.22).move_to(DOWN * 0.2)
        for row, content in zip(rows, contents):
            content.move_to(row[1].get_center())
        note = SerifLabel("plausible — not yours", CRIMSON, size=26)
        note.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.1), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(c) for c in contents], lag_ratio=0.1), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B06_ContextSlot(Scene):
    """Context slot: specialist vs general — the key mismatch."""
    def construct(self):
        total = DUR["B06"]
        title = _label("The context slot is the critical miss", INK, 30)
        title.to_edge(UP, buff=0.6)
        # Claude's guess
        guess_head = _chip("CLAUDE'S GUESS", accent=CRIMSON, size=22)
        guess_head.move_to(LEFT * 3.5 + UP * 0.8)
        guess_val = _label("general academic reader", CRIMSON, 30)
        guess_val.move_to(LEFT * 3.5 + DOWN * 0.1)
        # Actual context
        actual_head = _chip("ACTUAL CONTEXT", accent=INK, size=22)
        actual_head.move_to(RIGHT * 3.0 + UP * 0.8)
        actual_val = _label("specialist review committee\n(already know the field)", INK, 26)
        actual_val.move_to(RIGHT * 3.0 + DOWN * 0.2)
        # divider
        div = Line(UP * 2.0, DOWN * 2.0, color=SLATE, stroke_width=1.5)
        # note
        note = SerifLabel("general-audience framing is exactly wrong", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(div), run_time=0.4)
        self.play(FadeIn(guess_head), FadeIn(guess_val), run_time=0.7)
        self.play(FadeIn(actual_head), FadeIn(actual_val), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B07_TwoOutputs(Scene):
    """Same input, two different outputs depending on filled slots."""
    def construct(self):
        total = DUR["B07"]
        title = _label("Same input — two outputs", INK, 30)
        title.to_edge(UP, buff=0.6)
        # input
        input_chip = _chip("RAW TEXT", accent=SLATE, size=22)
        input_chip.move_to(LEFT * 5.0 + UP * 0.0)
        # branch arrow up → general
        arr_up = Arrow(LEFT * 3.0 + UP * 0.2, RIGHT * 0.0 + UP * 1.5,
                       color=CRIMSON, stroke_width=3, buff=0.2)
        out_general = _chip("GENERAL AUDIENCE OUTPUT", accent=CRIMSON, size=20)
        out_general.move_to(RIGHT * 2.5 + UP * 1.5)
        # branch arrow down → specialist
        arr_down = Arrow(LEFT * 3.0 + DOWN * 0.2, RIGHT * 0.0 + DOWN * 1.5,
                         color=INK, stroke_width=3, buff=0.2)
        out_specialist = _chip("SPECIALIST OUTPUT", accent=INK, size=20)
        out_specialist.move_to(RIGHT * 2.5 + DOWN * 1.5)
        # labels
        lbl_up = _label("(empty context slot)", CRIMSON, 22)
        lbl_up.next_to(out_general, DOWN, buff=0.2)
        lbl_down = _label("(context slot filled)", INK, 22)
        lbl_down.next_to(out_specialist, UP, buff=0.2)
        self.play(FadeIn(title), FadeIn(input_chip), run_time=0.6)
        self.play(GrowArrow(arr_up), GrowArrow(arr_down), run_time=0.7)
        self.play(FadeIn(out_general), FadeIn(lbl_up), run_time=0.6)
        self.play(FadeIn(out_specialist), FadeIn(lbl_down), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B08_SectionCard(Scene):
    def construct(self):
        total = DUR["B08"]
        t1 = Text("Each filled slot", font=DISPLAY, color=INK, font_size=50, weight=BOLD)
        t2 = Text("removes a generic guess", font=DISPLAY, color=CRIMSON,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B09_FilledSlots(Scene):
    """Dr. Osei fills all six slots with her actual situation."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Dr. Osei fills the slots", INK, 28)
        title.to_edge(UP, buff=0.6)
        osei_fills = [
            ("TASK", "tighten the gap statement"),
            ("CONTEXT", "specialist review committee"),
            ("SOURCES", "only evidence in the text"),
            ("CONSTRAINTS", "do not add claims"),
            ("FORMAT", "one paragraph"),
            ("EVALUATION", "gap clear in first 2 sentences"),
        ]
        rows = VGroup()
        contents = VGroup()
        for name, fill in osei_fills:
            row, content = _slot_row(name, filled=True, fill_text=fill)
            rows.add(row)
            contents.add(content)
        rows.arrange(DOWN, buff=0.18).move_to(DOWN * 0.2)
        for row, content in zip(rows, contents):
            content.move_to(row[1].get_center())
        result = SerifLabel("same raw text — correct output this time", INK, size=26)
        result.next_to(rows, DOWN, buff=0.35)
        self.play(FadeIn(title), run_time=0.5)
        for i, (row, content) in enumerate(zip(rows, contents)):
            self.play(FadeIn(row), FadeIn(content), run_time=0.35)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 0.5 - len(rows) * 0.35 - 0.6))


class B10_AnyRequest(Scene):
    """Six slots apply to any request type."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Six slots apply to every request", INK, 30)
        title.to_edge(UP, buff=0.6)
        examples = ["Summarize this.", "Analyze this.", "Write me something.", "Improve this."]
        chips = VGroup()
        for text in examples:
            c = _chip(text.upper(), accent=CRIMSON, size=20)
            chips.add(c)
        chips.arrange(RIGHT, buff=0.4).move_to(UP * 0.5)
        note1 = _label("every vague instruction leaves slots empty", CRIMSON, 28)
        note1.move_to(DOWN * 0.3)
        note2 = SerifLabel("every empty slot is a guess you did not make", INK, size=26)
        note2.move_to(DOWN * 1.1)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in chips], lag_ratio=0.2),
                  run_time=1.0)
        self.play(FadeIn(note1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(note2, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B11_JamieExample(Scene):
    """Jamie's 'analyze this dataset' → descriptive stats (not outlier report)."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Jamie: 'analyze this dataset'", INK, 28)
        title.to_edge(UP, buff=0.6)
        prompt_chip = _chip("PROMPT", accent=SLATE, size=22)
        prompt_chip.move_to(LEFT * 4.0 + UP * 0.8)
        prompt_text = _label("Analyze this dataset.", INK, 28)
        prompt_text.move_to(LEFT * 4.0 + UP * 0.1)
        arr = Arrow(LEFT * 1.8, RIGHT * 0.0, color=CRIMSON, stroke_width=4, buff=0.2)
        arr.move_to(ORIGIN + UP * 0.4)
        out_chip = _chip("OUTPUT", accent=CRIMSON, size=22)
        out_chip.move_to(RIGHT * 3.2 + UP * 0.8)
        out_text = _label("Descriptive statistics\nsummary", CRIMSON, 26)
        out_text.move_to(RIGHT * 3.2 + UP * 0.1)
        miss = _label("Jamie needed: outlier detection", CRIMSON, 26)
        miss.move_to(DOWN * 1.8)
        note = SerifLabel("task slot said 'analyze' — type was left to Claude", CRIMSON, size=24)
        note.move_to(DOWN * 2.5)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(prompt_chip), FadeIn(prompt_text), run_time=0.7)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(FadeIn(out_chip), FadeIn(out_text), run_time=0.7)
        self.play(FadeIn(miss), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


class B12_JamieFixed(Scene):
    """Jamie fills the task slot → outlier report."""
    def construct(self):
        total = DUR["B12"]
        title = _label("One slot filled — task specified", INK, 28)
        title.to_edge(UP, buff=0.6)
        prompt_chip = _chip("TASK SLOT FILLED", accent=INK, size=22)
        prompt_chip.move_to(LEFT * 3.8 + UP * 0.8)
        prompt_text = _label("Identify outliers: flag values\n> 3 std devs from mean.", INK, 26)
        prompt_text.move_to(LEFT * 3.8 + UP * 0.0)
        arr = Arrow(LEFT * 1.0, RIGHT * 0.5, color=INK, stroke_width=4, buff=0.2)
        arr.move_to(ORIGIN + UP * 0.4)
        out_chip = _chip("OUTPUT", accent=INK, size=22)
        out_chip.move_to(RIGHT * 3.5 + UP * 0.8)
        out_text = _label("Outlier detection report", INK, 26)
        out_text.move_to(RIGHT * 3.5 + UP * 0.1)
        note = SerifLabel("the one slot that mattered most — specified", INK, size=26)
        note.move_to(DOWN * 2.0)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(prompt_chip), FadeIn(prompt_text), run_time=0.7)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(FadeIn(out_chip), FadeIn(out_text), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B13_Practice(Scene):
    """Thirty-second slot check."""
    def construct(self):
        total = DUR["B13"]
        title = _label("Before submitting a vague request:", INK, 30)
        title.to_edge(UP, buff=0.6)
        questions = [
            ("TASK", "What specific verb?"),
            ("CONTEXT", "Who reads this, in what situation?"),
            ("SOURCES", "What should Claude draw from?"),
            ("CONSTRAINTS", "What must it not do?"),
            ("FORMAT", "What shape?"),
            ("EVALUATION", "How will you know it worked?"),
        ]
        rows = VGroup()
        for name, q in questions:
            chip = _chip(name, accent=SLATE, size=18)
            q_lbl = _label(q, INK, 22)
            row = VGroup(chip, q_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.22).move_to(DOWN * 0.1)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.12),
                  run_time=1.3)
        self.wait(max(0.5, total - 1.8))


class B14_End(Scene):
    def construct(self):
        total = DUR["B14"]
        t1 = Text("A prompt is a work order with six slots.", font=SERIF,
                  color=INK, font_size=42, weight=BOLD)
        t2 = Text("Empty slots become generic guesses.", font=SERIF,
                  color=INK, font_size=42, weight=BOLD)
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
