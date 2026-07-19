"""vox_scenes.py — Why Vague Revision Requests Change the Wrong Things
(vox-vague-revision-spreads, slate cut, 16:9)

Color law (teardown):
  INK     = named / frozen elements (preserved correctly)
  CRIMSON = unintended changes spreading from vague instruction

Exclusions: no AI alignment research on instruction following,
no chain-of-thought or scratchpad techniques,
no model-comparison benchmarks on instruction compliance.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 12.0, "B05": 11.0, "B06": 11.0,
    "B07": 10.0, "B08": 12.0, "B09": 11.0, "B10": 13.0, "B11": 12.0,
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


def _doc_row(label, color=INK, size=24):
    bar = Rectangle(width=0.18, height=0.4)
    bar.set_fill(color, 0.7).set_stroke(color, 1.5)
    txt = _label(label, color, size)
    return VGroup(bar, txt).arrange(RIGHT, buff=0.2)


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why vague revision requests", font=SERIF, color=INK, font_size=50, weight=BOLD)
        t2 = Text("change the wrong things", font=SERIF, color=INK, font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("one instruction — four unintended changes", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why does one revision request", font=SERIF, color=INK, font_size=48, weight=BOLD)
        q2 = Text("change four things?", font=SERIF, color=INK, font_size=48, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_RevisionSpread(Scene):
    """One vague instruction → spread arrows to four document elements."""
    def construct(self):
        total = DUR["B04"]
        title = _label("No target = entire output is revision-eligible", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Instruction box
        instr = _chip("more concise", accent=CRIMSON, size=22)
        instr.move_to(LEFT * 4.0 + UP * 0.0)

        # Four document elements on the right
        elements = [
            ("opening hook", CRIMSON),
            ("impact paragraph", CRIMSON),
            ("CEO quote", CRIMSON),
            ("methodology section", CRIMSON),
        ]
        elem_group = VGroup()
        for label, color in elements:
            e = _label(label, color, 22)
            elem_group.add(e)
        elem_group.arrange(DOWN, buff=0.35).move_to(RIGHT * 2.2)

        # Arrows from instruction to each element
        arrows = VGroup()
        for elem in elem_group:
            a = Arrow(instr.get_right(), elem.get_left(), color=CRIMSON,
                      stroke_width=2, buff=0.15, max_tip_length_to_length_ratio=0.15)
            arrows.add(a)

        note = SerifLabel("'more concise' is a goal — not a target", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(instr), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(e) for e in elem_group], lag_ratio=0.15), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.4))


class B05_CascadeEffect(Scene):
    """One unnamed change cascades into three others."""
    def construct(self):
        total = DUR["B05"]
        title = _label("One change cascades: elements are interdependent", INK, 28)
        title.to_edge(UP, buff=0.6)

        items = [
            ("impact paragraph removed", "for conciseness", CRIMSON),
            ("CEO quote loses its referent", "→ gets flattened", CRIMSON),
            ("opening hook rewritten", "→ now weaker", CRIMSON),
            ("structure shifts throughout", "→ unintended", CRIMSON),
        ]
        rows = VGroup()
        for label, consequence, color in items:
            lbl = _label(label, color, 22)
            con = _label(consequence, SLATE, 21)
            row = VGroup(lbl, con).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to(DOWN * 0.1)

        note = SerifLabel("one unnamed change → three cascading changes", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B06_TargetAndFreeze(Scene):
    """Revision = target + freeze list."""
    def construct(self):
        total = DUR["B06"]
        title = _label("A revision prompt has two parts", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Target (INK — what changes)
        target_chip = _chip("CHANGE TARGET", accent=INK, size=20)
        target_desc = _label("the specific element to revise", INK, 24)
        target_row = VGroup(target_chip, target_desc).arrange(RIGHT, buff=0.3)
        target_row.move_to(UP * 0.5)

        # Freeze list (SLATE — what doesn't change)
        freeze_chip = _chip("FREEZE LIST", accent=SLATE, size=20)
        freeze_desc = _label("elements that must not change", SLATE, 24)
        freeze_row = VGroup(freeze_chip, freeze_desc).arrange(RIGHT, buff=0.3)
        freeze_row.move_to(DOWN * 0.1)

        # Wall visualization: freeze list has a border
        wall = Rectangle(width=freeze_row.width + 0.6, height=freeze_row.height + 0.3)
        wall.set_fill(SLATE, 0.04).set_stroke(SLATE, 1.5)
        wall.move_to(freeze_row.get_center())

        note = SerifLabel("without the freeze list, everything is implicitly available", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(target_row, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(freeze_row), Create(wall), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.6))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Revision drift =", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("specification failure", font=DISPLAY, color=CRIMSON,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_NamedTargetPrompt(Scene):
    """Named target vs. vague: scope comparison."""
    def construct(self):
        total = DUR["B08"]
        title = _label("Name the target — freeze the rest", INK, 28)
        title.to_edge(UP, buff=0.6)

        # Vague prompt
        vague_chip = _chip("VAGUE", accent=CRIMSON, size=18)
        vague_text = _label('"Make it more concise."', CRIMSON, 24)
        vague_row = VGroup(vague_chip, vague_text).arrange(RIGHT, buff=0.3)
        vague_row.move_to(UP * 0.6)

        cross = Line(vague_text.get_corner(UL), vague_text.get_corner(DR),
                     color=CRIMSON, stroke_width=2)
        cross._qc_intentional = True

        # Named prompt
        named_chip = _chip("TARGETED", accent=INK, size=18)
        named_t1 = _label('"Shorten the methodology section only.', INK, 22)
        named_t2 = _label('Freeze: CEO quote, impact paragraph, opening hook."', INK, 22)
        named_block = VGroup(named_t1, named_t2).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        named_row = VGroup(named_chip, named_block).arrange(RIGHT, buff=0.3)
        named_row.move_to(DOWN * 0.35)

        note = SerifLabel("Claude cannot spread to what is frozen", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(vague_row), run_time=0.6)
        self.play(Create(cross), run_time=0.5)
        self.play(FadeIn(named_row, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B09_AnyRevision(Scene):
    """Any property-based revision applies globally."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Any property request applies to the whole document", INK, 28)
        title.to_edge(UP, buff=0.6)

        examples = [
            ("make it clearer", "→ every sentence that could be clearer", CRIMSON),
            ("make it warmer", "→ every sentence that sounds formal", CRIMSON),
            ("make it shorter", "→ every paragraph that seems expandable", CRIMSON),
        ]
        rows = VGroup()
        for instr, effect, color in examples:
            instr_lbl = _label(f'"{instr}"', CRIMSON, 23)
            arrow = Text("→", font=SERIF, color=SLATE, font_size=22)
            effect_lbl = _label(effect, SLATE, 22)
            row = VGroup(instr_lbl, arrow, effect_lbl).arrange(RIGHT, buff=0.25)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to(UP * 0.1)

        note = SerifLabel("property → optimization target across every eligible element", CRIMSON, size=25)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B10_GrantExample(Scene):
    """Nonprofit: engaging revision removes required measurable outcomes."""
    def construct(self):
        total = DUR["B10"]
        title = _label("'More engaging' — funder requirement removed", INK, 26)
        title.to_edge(UP, buff=0.6)

        elements = [
            ("opening paragraph", "rewritten — narrative hook added", CRIMSON),
            ("data section", "softened — reads as 'dry'", CRIMSON),
            ("measurable outcomes list", "REMOVED — read as dry", CRIMSON),
        ]
        rows = VGroup()
        for elem, change, color in elements:
            elem_lbl = _label(elem, INK, 22)
            arrow = Text("→", font=SERIF, color=SLATE, font_size=22)
            change_lbl = _label(change, color, 22)
            row = VGroup(elem_lbl, arrow, change_lbl).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to(UP * 0.1)

        # Ring on the removed item
        ring = HandRing(rows[2], color=CRIMSON)

        note = SerifLabel("funder required measurable outcomes — now gone", CRIMSON, size=24)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.15) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B11_GrantFixed(Scene):
    """Named-target revision preserves required sections."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Targeted revision — required sections preserved", INK, 28)
        title.to_edge(UP, buff=0.6)

        items = [
            ("CHANGE", "opening paragraph — engage the reader", INK),
            ("FREEZE", "measurable outcomes section — unchanged", SLATE),
            ("FREEZE", "data in section two — unchanged", SLATE),
            ("FREEZE", "logic model structure — unchanged", SLATE),
        ]
        rows = VGroup()
        for label, desc, color in items:
            chip = _chip(label, accent=color, size=18)
            desc_lbl = _label(desc, color, 23)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35).move_to(UP * 0.0)

        result = SerifLabel("funder requirement survives — one element changed", INK, size=26)
        result.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.1)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B12_Practice(Scene):
    """Practice: name target, freeze list, change log."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Before every revision request:", INK, 28)
        title.to_edge(UP, buff=0.6)

        steps = [
            ("CHANGE TARGET", "the specific element to revise", INK),
            ("FREEZE LIST", "elements that must not change", SLATE),
            ("CHANGE LOG", "what moved · what changed · what was kept", INK),
        ]
        rows = VGroup()
        for label, desc, color in steps:
            chip = _chip(label, accent=color, size=20)
            desc_lbl = _label(desc, color, 24)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.42).move_to(DOWN * 0.1)

        note = SerifLabel("the loop only works if you own the scope", INK, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.1)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B13_End(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("Name the target. Freeze the rest.", font=SERIF,
                  color=INK, font_size=42, weight=BOLD)
        t2 = Text("The revision loop only works if you own the scope.", font=SERIF,
                  color=INK, font_size=36, weight=BOLD)
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
