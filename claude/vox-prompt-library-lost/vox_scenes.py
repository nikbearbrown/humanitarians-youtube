"""vox_scenes.py — Why the Prompt That Worked Is Already Lost
(vox-prompt-library-lost, slate cut, 16:9)

Color law (teardown):
  INK     = prompt card (findable, maintained, repeatable)
  CRIMSON = lost chat history (buried, unsearchable, starts from zero)

Exclusions: no organizational knowledge management theory,
no tool comparison, no fine-tuning or model personalization.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 8.0, "B03": 9.0, "B04": 12.0, "B05": 11.0, "B06": 11.0,
    "B07": 10.0, "B08": 12.0, "B09": 10.0, "B10": 12.0, "B11": 11.0,
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
        t1 = Text("Why the prompt that worked", font=SERIF, color=INK, font_size=50, weight=BOLD)
        t2 = Text("is already lost", font=SERIF, color=INK, font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("successful prompts disappear — unless you save them", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why does a successful prompt", font=SERIF, color=INK, font_size=48, weight=BOLD)
        q2 = Text("disappear?", font=SERIF, color=INK, font_size=48, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_ChatScroll(Scene):
    """Chat scroll: prompt buried among failed attempts — no marker."""
    def construct(self):
        total = DUR["B04"]
        title = _label("Chat history: unindexed, unsearchable, mixed", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Chat messages as rows — most CRIMSON (failed), one hidden (the winning prompt)
        messages = [
            ("attempt 1", "not quite right", SLATE),
            ("attempt 2", "wrong format", SLATE),
            ("attempt 3", "added constraint...", SLATE),
            ("attempt 7 ← THIS ONE", "perfect output produced", INK),
            ("attempt 8", "overrode constraint", SLATE),
            ("other work", "unrelated task", CRIMSON),
            ("other work", "another session", CRIMSON),
        ]
        rows = VGroup()
        for label, desc, color in messages:
            lbl = _label(label, color, 20)
            dash = Text("—", font=SERIF, color=SLATE, font_size=20)
            desc_lbl = _label(desc, color, 20)
            row = VGroup(lbl, dash, desc_lbl).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(DOWN * 0.05)

        # HandRing on attempt 7 but it's buried
        ring = HandRing(rows[3], color=CRIMSON)

        note = SerifLabel("no tag marks the one that succeeded", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.1), run_time=1.2)
        self.play(Create(ring), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B05_MemoryGap(Scene):
    """Memory reconstructs 1 layer; the working prompt had 5."""
    def construct(self):
        total = DUR["B05"]
        title = _label("Memory reconstructs approximation — not the specification", INK, 28)
        title.to_edge(UP, buff=0.6)

        # The actual layers (INK) and what memory keeps (SLATE/CRIMSON)
        layers = [
            ("TASK", "initial goal — remembered", INK),
            ("CONSTRAINT", "added on iteration 3 — forgotten", CRIMSON),
            ("EXAMPLE", "added on iteration 5 — forgotten", CRIMSON),
            ("FREEZE CLAUSE", "prevents claim invention — forgotten", CRIMSON),
            ("REVIEW CRITERIA", "what made output pass — forgotten", CRIMSON),
        ]
        rows = VGroup()
        for label, desc, color in layers:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 22)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.28).move_to(DOWN * 0.05)

        note = SerifLabel("those additions were what made it work — now gone", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.18),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B06_SpecLayers(Scene):
    """5-layer spec builds up — memory produces 1."""
    def construct(self):
        total = DUR["B06"]
        title = _label("A prompt is built in layers — memory captures one", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Left: full spec (5 layers stacked)
        spec_chip = _chip("FULL SPEC", accent=INK, size=18)
        spec_chip.move_to(LEFT * 3.5 + UP * 0.5)
        layers_lbl = VGroup(
            _label("task", INK, 20),
            _label("+ constraints", INK, 20),
            _label("+ examples", INK, 20),
            _label("+ freeze clause", INK, 20),
            _label("+ review criteria", INK, 20),
        )
        layers_lbl.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        layers_lbl.move_to(LEFT * 3.5 + DOWN * 0.2)

        # Right: memory output (1 layer)
        mem_chip = _chip("MEMORY", accent=CRIMSON, size=18)
        mem_chip.move_to(RIGHT * 2.5 + UP * 0.5)
        mem_lbl = _label("task only", CRIMSON, 20)
        mem_lbl.move_to(RIGHT * 2.5 + DOWN * 0.05)

        note = SerifLabel("five layers built the output — one layer recreates the attempt", CRIMSON, size=24)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(spec_chip), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(l) for l in layers_lbl], lag_ratio=0.15), run_time=0.9)
        self.play(FadeIn(mem_chip), FadeIn(mem_lbl), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.1))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Prompt card =", font=DISPLAY, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("the specification, not just the text", font=DISPLAY, color=CRIMSON,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_PromptCard(Scene):
    """Eight-field prompt card."""
    def construct(self):
        total = DUR["B08"]
        title = _label("Eight fields — the specification, complete", INK, 28)
        title.to_edge(UP, buff=0.6)

        fields = [
            ("PURPOSE", "what task does this accomplish?", INK),
            ("INPUTS", "what does the user supply?", INK),
            ("CONSTRAINTS", "non-negotiable rules", INK),
            ("OUTPUT FORMAT", "what good output looks like", INK),
            ("REVIEW CRITERIA", "how you judge it correct", INK),
            ("EXAMPLE", "one worked use — proof of concept", INK),
            ("FAILURE MODES", "where it breaks down", SLATE),
            ("REVISION HISTORY", "what changed and why", SLATE),
        ]
        rows = VGroup()
        for label, desc, color in fields:
            chip = _chip(label, accent=color, size=14)
            desc_lbl = _label(desc, color, 19)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, buff=0.2).move_to(DOWN * 0.1)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.12),
                  run_time=1.5)
        self.wait(max(0.5, total - 2.0))


class B09_CumulativeVsRandom(Scene):
    """Without card: random quality. With card: cumulative."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Without card: start from zero. With card: cumulative.", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Without card
        no_chip = _chip("WITHOUT CARD", accent=CRIMSON, size=18)
        no_desc = _label("each task: iteration 1 quality", CRIMSON, 23)
        no_row = VGroup(no_chip, no_desc).arrange(RIGHT, buff=0.3)
        no_row.move_to(UP * 0.4)

        # With card
        yes_chip = _chip("WITH CARD", accent=INK, size=18)
        yes_desc = _label("each task: seventh-iteration quality from the start", INK, 23)
        yes_row = VGroup(yes_chip, yes_desc).arrange(RIGHT, buff=0.3)
        yes_row.move_to(DOWN * 0.1)

        note = SerifLabel("prompt quality becomes cumulative — not random", INK, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(no_row, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(yes_row, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B10_GrantExample(Scene):
    """Grant writer: seventh iteration lost; colleague retrieves card in 30s."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Seventh-iteration quality — gone. Card — 30 seconds.", INK, 26)
        title.to_edge(UP, buff=0.6)

        cases = [
            ("NO CARD", "90 minutes re-iterating — never gets back to iteration 7", CRIMSON),
            ("WITH CARD", "search 'program summary' — retrieves in 30 seconds", INK),
        ]
        rows = VGroup()
        for label, desc, color in cases:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.5).move_to(UP * 0.1)

        note = SerifLabel("the card carries what the seventh iteration cost to learn", INK, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(rows[0], shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(rows[1], shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B11_CardRetrieved(Scene):
    """The card the colleague retrieves: four key fields."""
    def construct(self):
        total = DUR["B11"]
        title = _label("The retrieved card — seventh-iteration knowledge", INK, 28)
        title.to_edge(UP, buff=0.6)

        fields = [
            ("PURPOSE", "executive summary for program funders", INK),
            ("INPUTS", "program name, audience, three measurable outcomes", INK),
            ("CONSTRAINTS", "200 words, no invented claims, plain language", INK),
            ("REVIEW", "outcomes must be specific and named", INK),
        ]
        rows = VGroup()
        for label, desc, color in fields:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38).move_to(DOWN * 0.0)

        result = SerifLabel("starts from the seventh iteration — not the first", INK, size=25)
        result.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.1)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B12_Practice(Scene):
    """Practice: four-field minimal card."""
    def construct(self):
        total = DUR["B12"]
        title = _label("When a prompt works — save it immediately. Write four things:", INK, 26)
        title.to_edge(UP, buff=0.6)

        fields = [
            ("PURPOSE", "one sentence — what task does this accomplish?", INK),
            ("INPUTS", "what does the user need to supply?", INK),
            ("CONSTRAINTS", "the rules that made it work", INK),
            ("REVIEW", "one criterion you actually checked", INK),
        ]
        rows = VGroup()
        for label, desc, color in fields:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35).move_to(DOWN * 0.1)

        note = SerifLabel("enough to start from the seventh iteration next time", INK, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("Don't start from zero next time.", font=SERIF,
                  color=INK, font_size=44, weight=BOLD)
        t2 = Text("Save the specification. Build the library.", font=SERIF,
                  color=INK, font_size=38, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.2)
        u = Line(t1.get_corner(DL) + DOWN * 0.14, t1.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        topic = Text("PROMPT ENGINEERING", font=DISPLAY, color=SLATE,
                     font_size=22, weight=BOLD)
        topic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2), run_time=0.7)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.1))
