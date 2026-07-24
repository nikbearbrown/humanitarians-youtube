"""vox_scenes.py — Why Claude Invents Claims When You Ask It to Improve Your Writing
(vox-writing-claim-invention, slate cut, 16:9)

Color law (teardown):
  INK     = author's original claims (owned, traceable)
  CRIMSON = Claude-invented claims (plausible but unsourced)

Exclusions: no hallucination research formalism, no RAG as solution,
no model-version comparison on citation accuracy.
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
        t1 = Text("Why Claude invents claims", font=SERIF, color=INK, font_size=52, weight=BOLD)
        t2 = Text("when you ask it to improve your writing", font=SERIF, color=INK,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("strengthening an argument often means inventing one", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why did improvement add", font=SERIF, color=INK, font_size=50, weight=BOLD)
        q2 = Text("a claim she never wrote?", font=SERIF, color=INK, font_size=50, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_GapFilling(Scene):
    """Argument text with visible gap → Claude fills with invented claim (crimson)."""
    def construct(self):
        total = DUR["B04"]
        title = _label("'Strengthen' → logical completeness becomes the target", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Original text (INK)
        orig1 = _label('"We recruited 120 participants', INK, 23)
        orig2 = _label('from three urban high schools."', INK, 23)
        gap = _label("[apparent gap: representativeness unclear]", SLATE, 21)
        orig_block = VGroup(orig1, orig2, gap).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        orig_block.move_to(UP * 0.4)

        # Claude's fill (crimson)
        fill_chip = _chip("CLAUDE FILLS", accent=CRIMSON, size=18)
        fill_text = _label('"...demographically consistent with', CRIMSON, 23)
        fill_text2 = _label('national urban enrollment patterns."', CRIMSON, 23)
        fill_block = VGroup(fill_chip, fill_text, fill_text2).arrange(DOWN, buff=0.1,
                                                                       aligned_edge=LEFT)
        fill_block.move_to(DOWN * 0.65)

        note = SerifLabel("fill comes from priors — not from your document", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(orig_block), run_time=0.7)
        self.play(FadeIn(fill_block, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.6))


class B05_NoVisibleSeam(Scene):
    """Before/after: original claim vs invented claim — no visible difference."""
    def construct(self):
        total = DUR["B05"]
        title = _label("Invented claim looks identical to original claims", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Side by side: original row vs invented row
        orig_chip = _chip("AUTHOR WROTE", accent=INK, size=18)
        orig_txt = _label('"Recruited 120 participants from three urban high schools."', INK, 22)
        orig_row = VGroup(orig_chip, orig_txt).arrange(RIGHT, buff=0.25)
        orig_row.move_to(UP * 0.5)

        inv_chip = _chip("CLAUDE ADDED", accent=CRIMSON, size=18)
        inv_txt = _label('"Consistent with national urban enrollment patterns."', CRIMSON, 22)
        inv_row = VGroup(inv_chip, inv_txt).arrange(RIGHT, buff=0.25)
        inv_row.move_to(DOWN * 0.1)

        # After: both look identical in output (show as plain INK)
        combined_chip = _chip("IN SUBMITTED DRAFT", accent=SLATE, size=18)
        combined_txt = _label("both claims — same format, same confidence", SLATE, 22)
        combined_row = VGroup(combined_chip, combined_txt).arrange(RIGHT, buff=0.25)
        combined_row.move_to(DOWN * 0.7)

        note = SerifLabel("no visible seam between what you wrote and what it invented", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(orig_row, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(inv_row, shift=LEFT * 0.2), run_time=0.6)
        self.play(FadeIn(combined_row, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B06_InstructionPermits(Scene):
    """'Strengthen' instruction → completeness goal → gap-fill pathway."""
    def construct(self):
        total = DUR["B06"]
        title = _label("'Strengthen' opens the gap-fill pathway", INK, 28)
        title.to_edge(UP, buff=0.6)

        instr = _chip("INSTRUCTION", accent=CRIMSON, size=20)
        instr_txt = _label('"strengthen the argument"', CRIMSON, 26)
        instr_row = VGroup(instr, instr_txt).arrange(RIGHT, buff=0.3)
        instr_row.move_to(UP * 0.6)

        arrow1 = Arrow(instr_row.get_bottom(), instr_row.get_bottom() + DOWN * 0.6,
                       color=SLATE, stroke_width=3, buff=0.1)

        interp = _label("goal: make this more complete and supported", SLATE, 24)
        interp.move_to(DOWN * 0.15)

        arrow2 = Arrow(interp.get_bottom(), interp.get_bottom() + DOWN * 0.5,
                       color=CRIMSON, stroke_width=3, buff=0.1)

        result = _chip("RESULT", accent=CRIMSON, size=20)
        result_txt = _label("fill logical gaps from priors", CRIMSON, 24)
        result_row = VGroup(result, result_txt).arrange(RIGHT, buff=0.3)
        result_row.move_to(DOWN * 0.9)

        note = SerifLabel("the instruction did not say: only from what is already here", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(instr_row), run_time=0.6)
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(FadeIn(interp), run_time=0.5)
        self.play(GrowArrow(arrow2), run_time=0.5)
        self.play(FadeIn(result_row), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.8))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("The instruction permitted", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("what you did not intend", font=DISPLAY, color=CRIMSON,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_OwnershipConstraint(Scene):
    """Ownership constraints close the gap-fill pathway."""
    def construct(self):
        total = DUR["B08"]
        title = _label("State the ownership boundary before the instruction", INK, 28)
        title.to_edge(UP, buff=0.6)

        constraints = [
            ("do not add claims not present in my text", INK),
            ("do not remove or soften hedges", INK),
            ("do not add examples or facts I did not provide", INK),
            ("mark every change so I can review it", INK),
        ]
        rows = VGroup()
        for text, color in constraints:
            bullet = Text("—", font=SERIF, color=SLATE, font_size=22)
            lbl = _label(text, color, 23)
            row = VGroup(bullet, lbl).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 0.05)

        note = SerifLabel("constraint closes the gap-fill pathway", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B09_AnyImprovement(Scene):
    """Any improvement instruction can trigger gap-filling."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Any improvement instruction can trigger gap-filling", INK, 28)
        title.to_edge(UP, buff=0.6)

        examples = [
            ('"Make it stronger."', "→ fills logical gaps", CRIMSON),
            ('"Fill out the argument."', "→ adds supporting claims", CRIMSON),
            ('"Sound more confident."', "→ removes hedges, upgrades claims", CRIMSON),
        ]
        rows = VGroup()
        for instr, effect, color in examples:
            instr_lbl = _label(instr, CRIMSON, 23)
            arrow = Text("→", font=SERIF, color=SLATE, font_size=22)
            eff_lbl = _label(effect, SLATE, 22)
            row = VGroup(instr_lbl, arrow, eff_lbl).arrange(RIGHT, buff=0.25)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to(UP * 0.1)

        note = SerifLabel("smoother output = harder to spot what was added", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B10_PolicyExample(Scene):
    """Policy analyst: HUD phrase invented, survives two editing rounds."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Invented phrase survives two editing rounds", INK, 26)
        title.to_edge(UP, buff=0.6)

        steps = [
            ("DRAFT", "housing tenure trends memo", INK),
            ("STRENGTHEN", "Claude adds: 'consistent with recent HUD data'", CRIMSON),
            ("EDIT ROUND 1", "phrase sounds authoritative — approved", CRIMSON),
            ("EDIT ROUND 2", "still present — no one checks the source", CRIMSON),
        ]
        rows = VGroup()
        for step, desc, color in steps:
            chip = _chip(step, accent=color, size=18)
            desc_lbl = _label(desc, color, 22)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.32).move_to(UP * 0.1)

        note = SerifLabel("no such HUD dataset exists for that metric", CRIMSON, size=24)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B11_PolicyFixed(Scene):
    """Constrained prompt: logic flow only, mark changes, flag gaps."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Constrained: tighten flow, mark changes, flag gaps", INK, 28)
        title.to_edge(UP, buff=0.6)

        outcomes = [
            ("TIGHTENED", "transitions and sentence clarity — flow only", INK),
            ("MARKED", "every change tagged [EDIT] for review", INK),
            ("FLAGGED", "one logical gap — 'fill this with your own data'", INK),
        ]
        rows = VGroup()
        for label, desc, color in outcomes:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38).move_to(UP * 0.0)

        result = SerifLabel("no invented claims — gaps flagged for analyst to fill", INK, size=26)
        result.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B12_Practice(Scene):
    """Four ownership constraints as standard prefix."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Paste these four constraints at the top of every editing prompt:", INK, 26)
        title.to_edge(UP, buff=0.6)

        constraints = [
            ("do not add claims not present in my text", INK),
            ("do not remove or soften hedges", INK),
            ("do not add examples or facts I did not provide", INK),
            ("mark every change so I can review it", INK),
        ]
        rows = VGroup()
        for i, (text, color) in enumerate(constraints, 1):
            num = _label(f"{i}.", SLATE, 23)
            lbl = _label(text, color, 23)
            row = VGroup(num, lbl).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 0.1)

        note = SerifLabel("standard header — no overhead to write it each time", INK, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("Every claim is yours.", font=SERIF,
                  color=INK, font_size=46, weight=BOLD)
        t2 = Text("Name the boundary first.", font=SERIF,
                  color=INK, font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        sub = _label("improvement without constraints means gap-filling from priors", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        topic = Text("PROMPT ENGINEERING", font=DISPLAY, color=SLATE,
                     font_size=22, weight=BOLD)
        topic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.6))
