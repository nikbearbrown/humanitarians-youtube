"""vox_scenes.py — Why AI Can't Fix Its Own Mistakes
(vox-self-review-sieve, slate cut, 16:9)

Color law (teardown):
  INK     = external check / human review / correctly surfaced issues
  CRIMSON = the reasoning error that passes through both sieves

Exclusions: no Huang et al. methodology, no formal verification,
no external critic models, no RLHF critique pipelines.
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


def _sieve_rect(width=5.5, height=0.55, color=INK):
    """A sieve as a horizontal rectangle with a dashed border."""
    r = Rectangle(width=width, height=height)
    r.set_fill(color, 0.08).set_stroke(color, 2.0)
    return r


def _particle(color=CRIMSON, radius=0.1):
    c = Circle(radius=radius)
    c.set_fill(color, 0.85).set_stroke(color, 1.5)
    return c


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why AI can't fix", font=SERIF, color=INK, font_size=58, weight=BOLD)
        t2 = Text("its own mistakes", font=SERIF, color=INK, font_size=58, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("the sieve that generates also reviews", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why didn't self-review", font=SERIF, color=INK, font_size=52, weight=BOLD)
        q2 = Text("fix the error?", font=SERIF, color=INK, font_size=52, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_OneSieve(Scene):
    """Single sieve: particles fall through holes — reasoning gaps let errors pass."""
    def construct(self):
        total = DUR["B04"]
        title = _label("A reasoning model is a sieve", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Sieve bar
        sieve = _sieve_rect(5.5, 0.55, INK)
        sieve.move_to(ORIGIN)

        # Hole labels on the sieve (gaps = inference steps it cannot reliably make)
        hole1 = _label("gap", CRIMSON, 20)
        hole1.move_to(sieve.get_center() + LEFT * 1.4)
        hole2 = _label("gap", CRIMSON, 20)
        hole2.move_to(sieve.get_center() + RIGHT * 1.1)

        # Label above sieve
        lbl_above = _label("output", INK, 24)
        lbl_above.next_to(sieve, UP, buff=0.45)

        # Error particle — shown above sieve, then moves through
        error = _particle(CRIMSON, 0.13)
        error.move_to(sieve.get_top() + UP * 0.5 + LEFT * 1.4)

        # Bottom note
        note = SerifLabel("errors the sieve cannot catch fall through", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(sieve), run_time=0.7)
        self.play(FadeIn(hole1), FadeIn(hole2), run_time=0.5)
        self.play(FadeIn(lbl_above), FadeIn(error), run_time=0.5)
        # error passes through the gap
        self.play(error.animate.move_to(sieve.get_bottom() + DOWN * 0.5 + LEFT * 1.4),
                  run_time=0.9)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.7))


class B05_TwoSieves(Scene):
    """Two sieves stacked — same holes in same places. Error passes both."""
    def construct(self):
        total = DUR["B05"]
        title = _label("Same sieve, run twice — same holes", INK, 28)
        title.to_edge(UP, buff=0.6)

        # First sieve (generation)
        sieve1 = _sieve_rect(5.5, 0.55, INK)
        sieve1.move_to(UP * 0.7)
        lbl1 = _chip("GENERATE", accent=INK, size=18)
        lbl1.next_to(sieve1, LEFT, buff=0.25)

        # Second sieve (self-review)
        sieve2 = _sieve_rect(5.5, 0.55, INK)
        sieve2.move_to(DOWN * 0.5)
        lbl2 = _chip("SELF-REVIEW", accent=INK, size=18)
        lbl2.next_to(sieve2, LEFT, buff=0.25)

        # Gap markers on both sieves in same position
        gap1a = _label("gap", CRIMSON, 20)
        gap1a.move_to(sieve1.get_center() + LEFT * 1.2)
        gap1b = _label("gap", CRIMSON, 20)
        gap1b.move_to(sieve1.get_center() + RIGHT * 1.0)
        gap2a = _label("gap", CRIMSON, 20)
        gap2a.move_to(sieve2.get_center() + LEFT * 1.2)
        gap2b = _label("gap", CRIMSON, 20)
        gap2b.move_to(sieve2.get_center() + RIGHT * 1.0)

        # Error particle moving through both
        error = _particle(CRIMSON, 0.13)
        error.move_to(sieve1.get_top() + UP * 0.45 + LEFT * 1.2)

        note = SerifLabel("same weights — holes in the same places", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(sieve1), FadeIn(lbl1), run_time=0.7)
        self.play(FadeIn(gap1a), FadeIn(gap1b), run_time=0.4)
        self.play(FadeIn(error), run_time=0.3)
        # through sieve 1
        self.play(error.animate.move_to(sieve1.get_bottom() + DOWN * 0.15 + LEFT * 1.2),
                  run_time=0.7)
        self.play(Create(sieve2), FadeIn(lbl2), run_time=0.6)
        self.play(FadeIn(gap2a), FadeIn(gap2b), run_time=0.4)
        # through sieve 2
        self.play(error.animate.move_to(sieve2.get_bottom() + DOWN * 0.5 + LEFT * 1.2),
                  run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.9))


class B06_SurfaceVsLogic(Scene):
    """Surface items (grammar) pass sieve cleanly; logic gap falls through."""
    def construct(self):
        total = DUR["B06"]
        title = _label("Surface issues caught — logic gaps fall through", INK, 28)
        title.to_edge(UP, buff=0.6)

        sieve = _sieve_rect(5.5, 0.55, INK)
        sieve.move_to(UP * 0.1)

        gap = _label("logic gap", CRIMSON, 20)
        gap.move_to(sieve.get_center() + RIGHT * 0.8)

        # Surface item: grammar — stays above sieve (caught)
        surface_dot = _particle(INK, 0.13)
        surface_dot.move_to(sieve.get_top() + UP * 0.5 + LEFT * 1.5)
        surface_lbl = _label("grammar", INK, 21)
        surface_lbl.next_to(surface_dot, RIGHT, buff=0.15)

        # Error particle: reasoning gap — falls through
        error_dot = _particle(CRIMSON, 0.13)
        error_dot.move_to(sieve.get_top() + UP * 0.5 + RIGHT * 0.8)
        error_lbl = _label("reasoning gap", CRIMSON, 21)
        error_lbl.next_to(error_dot, RIGHT, buff=0.15)

        # Bottom: "stated more confidently"
        note = SerifLabel("revision sounds more confident — error still inside", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(sieve), FadeIn(gap), run_time=0.7)
        self.play(FadeIn(surface_dot), FadeIn(surface_lbl), run_time=0.4)
        self.play(FadeIn(error_dot), FadeIn(error_lbl), run_time=0.4)
        # surface stops at sieve top
        self.play(
            surface_dot.animate.move_to(sieve.get_top() + DOWN * 0.05 + LEFT * 1.5),
            run_time=0.6,
        )
        # error passes through
        self.play(
            error_dot.animate.move_to(sieve.get_bottom() + DOWN * 0.5 + RIGHT * 0.8),
            run_time=0.7,
        )
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.9))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Self-critique = surfacing for you,", font=DISPLAY, color=INK,
                  font_size=40, weight=BOLD)
        t2 = Text("not repairing for the model", font=DISPLAY, color=CRIMSON,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_BetterPrompt(Scene):
    """Better prompt: ask to flag assumptions, not fix reasoning."""
    def construct(self):
        total = DUR["B08"]
        title = _label("Ask Claude to flag assumptions — not fix reasoning", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Old prompt (bad)
        old_chip = _chip("OLD PROMPT", accent=CRIMSON, size=18)
        old_text = _label('"Review this reasoning and fix any errors."', CRIMSON, 24)
        old_row = VGroup(old_chip, old_text).arrange(RIGHT, buff=0.3)
        old_row.move_to(UP * 0.6)

        cross = Line(old_text.get_corner(UL), old_text.get_corner(DR),
                     color=CRIMSON, stroke_width=2)
        cross._qc_intentional = True

        # New prompt (good)
        new_chip = _chip("BETTER PROMPT", accent=INK, size=18)
        new_t1 = _label('"List any inference steps where you assumed', INK, 24)
        new_t2 = _label('something rather than derived it."', INK, 24)
        new_block = VGroup(new_t1, new_t2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        new_row = VGroup(new_chip, new_block).arrange(RIGHT, buff=0.3)
        new_row.move_to(DOWN * 0.3)

        note = SerifLabel("output: a checklist for you — not another generated fix", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(old_row), run_time=0.6)
        self.play(Create(cross), run_time=0.5)
        self.play(FadeIn(new_row, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B09_FalseConfidence(Scene):
    """Self-check gives false confidence — error still inside after both passes."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Self-check creates false confidence", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Two-step: generate → check → same error
        steps = [
            ("GENERATE", "error present", CRIMSON),
            ("SELF-CHECK", "error still present", CRIMSON),
            ("RESULT", "output accepted — flaw intact", CRIMSON),
        ]
        rows = VGroup()
        for step, desc, color in steps:
            chip = _chip(step, accent=color, size=18)
            desc_lbl = _label(desc, color, 24)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38).move_to(UP * 0.1)

        note = SerifLabel("the check gives you confidence — not correctness", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B10_AnalystExample(Scene):
    """Investment analyst: DCF rationale, self-check returns 'no logical errors found'."""
    def construct(self):
        total = DUR["B10"]
        title = _label("DCF rationale: self-check misses the hidden assumption", INK, 26)
        title.to_edge(UP, buff=0.6)

        steps = [
            ("REQUEST", "build a DCF model rationale", INK),
            ("SELF-CHECK", '"checked — no logical errors found"', CRIMSON),
            ("SUBMITTED", "senior partner: constant discount rate assumed", CRIMSON),
        ]
        rows = VGroup()
        for step, desc, color in steps:
            chip = _chip(step, accent=color, size=18)
            desc_lbl = _label(desc, color, 24)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(UP * 0.1)

        note = SerifLabel("model never questioned what it did not know to question", CRIMSON, size=24)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.3),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B11_AnalystFixed(Scene):
    """Assumption list: seven items, constant discount rate is #4. Human catches it."""
    def construct(self):
        total = DUR["B11"]
        title = _label("List every assumption — human reads the list", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Seven assumption chips, #4 highlighted
        assumptions = [
            ("1. revenue growth rate held constant", INK),
            ("2. terminal value multiple derived from comparables", INK),
            ("3. tax rate based on current statutory rate", INK),
            ("4. discount rate constant across all periods", CRIMSON),
            ("5. no additional capital expenditure assumed", INK),
            ("6. working capital ratios from prior year", INK),
            ("7. no currency adjustment for foreign revenues", INK),
        ]
        rows = VGroup()
        for text, color in assumptions:
            row = _label(text, color, 21)
            rows.add(row)
        rows.arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(DOWN * 0.05)

        ring = HandRing(rows[3], color=CRIMSON)

        note = SerifLabel("assumption 4 — caught before submission", INK, size=26)
        note.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.08), run_time=1.2)
        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.1))


class B12_Practice(Scene):
    """Practice: make reasoning visible — list assumptions, flag inference steps."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Expose reasoning — do not ask Claude to fix it", INK, 28)
        title.to_edge(UP, buff=0.6)

        practices = [
            ("LIST ASSUMPTIONS", "what was assumed vs. derived from data", INK),
            ("FLAG INFERENCES", "mark where it filled a gap you did not specify", INK),
            ("MARK DERIVATIONS", "what is derived vs. what is stated", INK),
        ]
        rows = VGroup()
        for label, desc, color in practices:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 24)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38).move_to(UP * 0.1)

        note = SerifLabel("you review those — not another generated output", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("The sieve that generates also reviews.", font=SERIF,
                  color=INK, font_size=40, weight=BOLD)
        t2 = Text("Expose the reasoning. Apply your judgment.", font=SERIF,
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
