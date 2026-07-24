"""vox_scenes.py — Why "Maybe We Should" Becomes "Decision: We Will"
(vox-modal-upgrade, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT beat whose source is 'own'.
B02 and B11 are STILL (ai) slots — compiled as slates.

Color law: TEAL #1F6F5C = original tentative note / faithful record
           CRIMSON #BF3339 = upgraded/decided version / wrong promotion
           GOLD #F5D061 = editor's-pen highlight fill only
Two accents max — never swapped mid-film.

Exclusions: NO column template, NO contextual-integrity theory,
NO four-operations taxonomy, NO second artifact type, NO ICMJE.
Gate B: every zero-width stroke is also zero-opacity.
"""
import json
import os
import sys
import pathlib

_bs_path = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs_path))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}

sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np


# ---------------------------------------------------------------- helpers

def _note_line(text, color=TEAL, size=32):
    """A serif note line with a left-tick accent."""
    tick = Line(ORIGIN, ORIGIN + DOWN * 0.5, color=color, stroke_width=3)
    tick.set_stroke(opacity=1)
    txt = Text(text, font=SERIF, color=color, font_size=size, slant=ITALIC)
    if txt.width > 9.0:
        txt.scale_to_fit_width(9.0)
    g = VGroup(tick, txt).arrange(RIGHT, buff=0.2)
    return g


def _label_row(left_text, right_text, left_color=TEAL, right_color=CRIMSON, size=26):
    lt = Text(left_text, font=DISPLAY, color=left_color, font_size=size)
    colon = Text(":", font=DISPLAY, color=INK, font_size=size)
    rt = Text(right_text, font=SERIF, color=right_color, font_size=size, slant=ITALIC)
    return VGroup(lt, colon, rt).arrange(RIGHT, buff=0.18)


# ============================================================ scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why “Maybe We Should”", font=SERIF, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("Becomes “Decision: We Will”", font=SERIF, color=INK,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14,
                 t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_TheQuestion(Scene):
    def construct(self):
        _quote_scene(
            self,
            "A faithful summary should preserve 'maybe we should look into this.' "
            "The summary reads 'Decision: we will.' Nothing was fabricated. Why?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_OriginalNote(Scene):
    """THE PROBLEM — original note text in TEAL."""
    def construct(self):
        total = DUR["B04"]
        source_lbl = LabelChip("ORIGINAL NOTE", accent=TEAL, size=22)
        note_text = Text(
            "silent auction — tabled, needs board input",
            font=SERIF, color=TEAL, font_size=36, slant=ITALIC,
        )
        if note_text.width > 10.0:
            note_text.scale_to_fit_width(10.0)
        under = Line(
            note_text.get_corner(DL) + DOWN * 0.1,
            note_text.get_corner(DR) + DOWN * 0.1,
            color=TEAL, stroke_width=1.5,
        )
        under.set_stroke(opacity=1)
        block = VGroup(note_text, under).move_to(ORIGIN)
        source_lbl.next_to(block, UP, buff=0.5)
        self.play(FadeIn(source_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(note_text, shift=UP * 0.1), Create(under), run_time=0.9)
        self.wait(max(0.5, total - 1.4))


class B05_SummaryPromotion(Scene):
    """THE PROBLEM — summary output in CRIMSON below original."""
    def construct(self):
        total = DUR["B05"]

        orig_lbl = LabelChip("ORIGINAL NOTE", accent=TEAL, size=20)
        orig_txt = Text(
            "silent auction — tabled, needs board input",
            font=SERIF, color=TEAL, font_size=30, slant=ITALIC,
        )
        if orig_txt.width > 10.0:
            orig_txt.scale_to_fit_width(10.0)

        arrow = Arrow(ORIGIN, DOWN * 0.8, color=CRIMSON, buff=0.0, stroke_width=3)

        summ_lbl = LabelChip("DECISIONS", accent=CRIMSON, size=20)
        summ_txt = Text(
            "DECISION: add a silent auction",
            font=DISPLAY, color=CRIMSON, font_size=34,
        )
        if summ_txt.width > 10.0:
            summ_txt.scale_to_fit_width(10.0)

        top_group = VGroup(orig_lbl, orig_txt).arrange(DOWN, buff=0.15)
        bot_group = VGroup(summ_lbl, summ_txt).arrange(DOWN, buff=0.15)
        full = VGroup(top_group, arrow, bot_group).arrange(DOWN, buff=0.3)
        full.move_to(ORIGIN)

        self.play(FadeIn(top_group, shift=UP * 0.1), run_time=0.7)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(bot_group, shift=DOWN * 0.1), run_time=0.8)
        self.wait(max(0.5, total - 2.0))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        head = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48)
        sub = Text("coherence over modality", font=SERIF, color=TEAL, font_size=28,
                   slant=ITALIC)
        block = VGroup(head, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(block, scale=0.95), run_time=0.7)
        self.wait(max(0.3, total - 0.7))


class B07_CoherenceBias(Scene):
    """THE MECHANISM — model pulls toward resolved prose."""
    def construct(self):
        total = DUR["B07"]

        hedged = Text(
            '"maybe we should look into this"',
            font=SERIF, color=TEAL, font_size=30, slant=ITALIC,
        )
        resolved = Text(
            '"agreed: we will"',
            font=SERIF, color=CRIMSON, font_size=36, slant=ITALIC,
        )
        hedged_lbl = LabelChip("HEDGED", accent=TEAL, size=20)
        resolved_lbl = LabelChip("RESOLVED", accent=CRIMSON, size=20)

        left_g = VGroup(hedged_lbl, hedged).arrange(DOWN, buff=0.18)
        right_g = VGroup(resolved_lbl, resolved).arrange(DOWN, buff=0.18)
        pair = VGroup(left_g, right_g).arrange(RIGHT, buff=1.5).move_to(UP * 0.3)

        arrow = Arrow(
            left_g.get_right() + RIGHT * 0.1,
            right_g.get_left() + LEFT * 0.1,
            color=CRIMSON, buff=0.0, stroke_width=4,
        )
        model_lbl = SerifLabel("model pull", accent=CRIMSON, size=24)
        model_lbl.next_to(arrow, UP, buff=0.2)

        self.play(FadeIn(left_g, shift=RIGHT * 0.3), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(model_lbl), run_time=0.7)
        self.play(FadeIn(right_g, shift=LEFT * 0.3), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B08_ModalSpectrum(Scene):
    """THE MECHANISM — modality spectrum with CRIMSON upgrade arrow."""
    def construct(self):
        total = DUR["B08"]

        labels = ["discussed", "maybe", "agreed", "decided"]
        colors = [TEAL, TEAL, CRIMSON, CRIMSON]
        nodes = VGroup()
        for lab, col in zip(labels, colors):
            dot = Circle(radius=0.18).set_fill(col, 1).set_stroke(width=0, opacity=0)
            txt = Text(lab, font=SERIF, color=col, font_size=26)
            g = VGroup(dot, txt).arrange(DOWN, buff=0.18)
            nodes.add(g)
        nodes.arrange(RIGHT, buff=1.1).move_to(UP * 0.3)

        # Connecting line
        line = Line(
            nodes[0].get_right() + RIGHT * 0.0,
            nodes[-1].get_left() + LEFT * 0.0,
            color=INK, stroke_width=1.5,
        )
        line.set_stroke(opacity=0.35)

        # Upgrade arrow spanning discussed -> agreed
        upg_arrow = Arrow(
            nodes[0][0].get_center(),
            nodes[2][0].get_center(),
            color=CRIMSON, buff=0.25, stroke_width=3,
        )
        upg_arrow.shift(UP * 0.7)
        upg_lbl = SerifLabel("model upgrade", accent=CRIMSON, size=22)
        upg_lbl.next_to(upg_arrow, UP, buff=0.12)

        self.play(FadeIn(nodes[0], shift=UP * 0.1), FadeIn(nodes[1], shift=UP * 0.1),
                  run_time=0.6)
        self.play(Create(line), run_time=0.4)
        self.play(FadeIn(nodes[2], shift=UP * 0.1), FadeIn(nodes[3], shift=UP * 0.1),
                  run_time=0.6)
        self.play(GrowArrow(upg_arrow), FadeIn(upg_lbl), run_time=0.8)
        self.wait(max(0.5, total - 2.4))


class B09_KeyClaim(Scene):
    """THE MECHANISM — key claim quote."""
    def construct(self):
        _quote_scene(
            self,
            "The model produces what prose looks like when decisions were made.",
            "— the mechanism",
            None,
            "decisions",
            DUR["B09"],
        )


class B10_QuestionOwner(Scene):
    """THE MECHANISM — question becomes action item."""
    def construct(self):
        total = DUR["B10"]

        q_lbl = LabelChip("QUESTION ASKED", accent=TEAL, size=20)
        q_txt = Text(
            "“who owns the venue contract?”",
            font=SERIF, color=TEAL, font_size=30, slant=ITALIC,
        )
        if q_txt.width > 10.0:
            q_txt.scale_to_fit_width(10.0)

        arrow = Arrow(ORIGIN, DOWN * 0.8, color=CRIMSON, buff=0.0, stroke_width=3)

        a_lbl = LabelChip("ACTION ITEMS", accent=CRIMSON, size=20)
        a_txt = Text(
            "Owner: [Attendee] — follow-up on venue contract",
            font=SERIF, color=CRIMSON, font_size=28,
        )
        if a_txt.width > 10.0:
            a_txt.scale_to_fit_width(10.0)

        top = VGroup(q_lbl, q_txt).arrange(DOWN, buff=0.15)
        bot = VGroup(a_lbl, a_txt).arrange(DOWN, buff=0.15)
        full = VGroup(top, arrow, bot).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(top, shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(bot, shift=DOWN * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 1.8))


class B12_Example(Scene):
    """THE EXAMPLE — source note vs Decisions row (illustrative)."""
    def construct(self):
        total = DUR["B12"]

        src_lbl = LabelChip("SOURCE NOTE", accent=TEAL, size=20)
        src_txt = Text(
            "silent auction — tabled, needs board input",
            font=SERIF, color=TEAL, font_size=30, slant=ITALIC,
        )
        if src_txt.width > 9.5:
            src_txt.scale_to_fit_width(9.5)
        src_g = VGroup(src_lbl, src_txt).arrange(DOWN, buff=0.18)

        vs_arrow = Arrow(ORIGIN, DOWN * 0.7, color=CRIMSON, buff=0.0, stroke_width=3)

        sum_lbl = LabelChip("DECISIONS", accent=CRIMSON, size=20)
        sum_txt = Text(
            "Agreed: add a silent auction",
            font=SERIF, color=CRIMSON, font_size=34,
        )
        if sum_txt.width > 9.5:
            sum_txt.scale_to_fit_width(9.5)
        sum_g = VGroup(sum_lbl, sum_txt).arrange(DOWN, buff=0.18)

        full = VGroup(src_g, vs_arrow, sum_g).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        illus = SerifLabel("illustrative", accent=INK, size=20)
        illus.to_corner(DL, buff=0.55)

        self.play(FadeIn(src_g, shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(vs_arrow), run_time=0.4)
        self.play(FadeIn(sum_g, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - 2.0))


class B13_ExampleTwo(Scene):
    """THE EXAMPLE — question → action item owner (illustrative)."""
    def construct(self):
        total = DUR["B13"]

        q_txt = Text(
            "“who owns the venue contract?”",
            font=SERIF, color=TEAL, font_size=30, slant=ITALIC,
        )
        if q_txt.width > 10.5:
            q_txt.scale_to_fit_width(10.5)
        q_lbl = LabelChip("SAID BY ATTENDEE", accent=TEAL, size=18)
        q_g = VGroup(q_lbl, q_txt).arrange(DOWN, buff=0.15)

        arrow = Arrow(ORIGIN, DOWN * 0.7, color=CRIMSON, buff=0.0, stroke_width=3)

        a_txt = Text(
            "Owner: Attendee — follow-up on venue contract",
            font=SERIF, color=CRIMSON, font_size=28,
        )
        if a_txt.width > 10.5:
            a_txt.scale_to_fit_width(10.5)
        a_lbl = LabelChip("LISTED IN ACTION ITEMS", accent=CRIMSON, size=18)
        a_g = VGroup(a_lbl, a_txt).arrange(DOWN, buff=0.15)

        full = VGroup(q_g, arrow, a_g).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        illus = SerifLabel("illustrative", accent=INK, size=20)
        illus.to_corner(DL, buff=0.55)

        self.play(FadeIn(q_g, shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(a_g, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - 2.0))


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        topic = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        main = Text("Discussed is not agreed.",
                    font=SERIF, color=INK, font_size=52, weight=BOLD)
        if main.width > 11.0:
            main.scale_to_fit_width(11.0)
        u = Line(main.get_corner(DL) + DOWN * 0.14,
                 main.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(main, u).move_to(ORIGIN)
        topic.next_to(block, UP, buff=0.6)
        self.play(FadeIn(topic, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(main, shift=UP * 0.1), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 1.5))
