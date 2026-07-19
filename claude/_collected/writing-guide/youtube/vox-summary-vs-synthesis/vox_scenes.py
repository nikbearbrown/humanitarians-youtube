"""vox_scenes.py — Summary vs. Synthesis: The Move No Source Can Make For You
(vox-summary-vs-synthesis, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is own.
B02 and B10 are STILL (ai media slots) — no scenes here for those.

Color law (teardown palette):
  CRIMSON (#C8102E) = summary / isolated / absent argument
  INK    (#2A1A0E) = synthesis / connected / the argument that emerges
  GOLD wash (#F6D8DC) = editor's-pen highlight, once, in B12 only

Gate B: every zero-width stroke also has zero opacity.
Anchor-not-transcript: on-screen text is never a copy of the narration sentence.
"""
import sys
import json
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# ---- duration table (estimates; overridden by actuals after audio lock) ----
DUR = {
    "B01": 11.0, "B03": 12.0, "B04": 12.0, "B05": 12.0, "B06": 12.0,
    "B07": 13.0, "B08": 14.0, "B09": 13.0, "B11": 14.0, "B12": 14.0,
    "B13": 16.0, "B14": 14.0, "B15": 13.0, "B16": 13.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _source_block(label, color, w=3.8, h=0.7):
    """A labeled source block — a filled rectangle with a LabelChip."""
    rect = Rectangle(width=w, height=h)
    rect.set_fill(color, 0.12).set_stroke(color, 2.0)
    chip = LabelChip(label, accent=color, size=20)
    chip.next_to(rect, RIGHT, buff=0.2)
    return VGroup(rect, chip)


def _claim_block(label, w=5.0, h=0.75):
    """The writer's synthesis claim — a bold INK box."""
    rect = Rectangle(width=w, height=h)
    rect.set_fill(INK, 0.10).set_stroke(INK, 2.5)
    t = Text(label, font=SERIF, color=INK, font_size=24)
    if t.width > w * 0.88:
        t.scale_to_fit_width(w * 0.88)
    t.move_to(rect)
    return VGroup(rect, t)


def _arrow(start_mob, end_mob, color=INK):
    """A simple arrow from the right edge of start to the left edge of end."""
    start = start_mob.get_right()
    end = end_mob.get_left()
    arr = Arrow(start, end, color=color, stroke_width=2.5,
                buff=0.1, tip_length=0.18)
    return arr


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("WRITING", font=DISPLAY, color=INK, font_size=22)
        t1 = Text("Ten sources.", font=DISPLAY, color=INK,
                  font_size=54, weight="BOLD")
        t2 = Text("Zero arguments.", font=DISPLAY, color=CRIMSON,
                  font_size=54, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.18,
                 t2.get_corner(DR) + DOWN * 0.18,
                 color=CRIMSON, stroke_width=2.5)
        sub = Text("the problem is not the sources", font=SERIF, color=INK,
                   font_size=26, slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.5)
        eye.next_to(block, UP, buff=0.9)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(t1, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(t2, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=22)
        chip.to_corner(UL, buff=0.6)
        q_main = Text("Summary vs. Synthesis:", font=DISPLAY, color=INK,
                      font_size=40, weight="BOLD")
        q_sub = Text("what is the move no source can make for you?",
                     font=SERIF, color=INK, font_size=30, slant=ITALIC)
        q_group = VGroup(q_main, q_sub).arrange(DOWN, buff=0.35).move_to(UP * 0.1)
        u = Line(q_sub.get_corner(DL) + DOWN * 0.12,
                 q_sub.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=1.8)
        self.play(FadeIn(chip, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(q_main, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(q_sub, shift=UP * 0.1), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 2.2))


class B04_SummaryParagraph(Scene):
    """Three summary sentences — isolated CRIMSON blocks, one per source."""
    def construct(self):
        total = DUR["B04"]
        eye = SerifLabel("the summary pattern", CRIMSON, size=26)
        eye.to_edge(UP, buff=0.7)

        b1 = _source_block("Berners-Lee 2018", CRIMSON)
        b2 = _source_block("Willett 2019", CRIMSON)
        b3 = _source_block("Poore 2018", CRIMSON)
        stack = VGroup(b1, b2, b3).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        stack.move_to(DOWN * 0.2 + LEFT * 1.5)

        self.play(Write(eye[0]), Create(eye[1]), run_time=0.7)
        self.play(FadeIn(b1, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(b2, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(b3, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B05_SummaryThree(Scene):
    """The summary paragraph rendered as three isolated source blocks."""
    def construct(self):
        total = DUR["B05"]

        labels = [
            ("Berners-Lee 2018", "food production is sufficient"),
            ("Willett 2019",      "shift to plant-based diets"),
            ("Poore 2018",        "documents environmental footprints"),
        ]
        blocks = []
        for cit, claim in labels:
            rect = Rectangle(width=5.5, height=0.9)
            rect.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.8)
            chip = LabelChip(cit, accent=CRIMSON, size=18)
            claim_t = Text(claim, font=SERIF, color=INK, font_size=24)
            inner = VGroup(chip, claim_t).arrange(RIGHT, buff=0.3)
            if inner.width > 5.2:
                inner.scale_to_fit_width(5.2)
            inner.move_to(rect)
            blocks.append(VGroup(rect, inner))

        col = VGroup(*blocks).arrange(DOWN, buff=0.5).move_to(DOWN * 0.1)

        self.play(FadeIn(col[0], shift=LEFT * 0.4), run_time=0.7)
        self.play(FadeIn(col[1], shift=LEFT * 0.4), run_time=0.7)
        self.play(FadeIn(col[2], shift=LEFT * 0.4), run_time=0.7)
        self.wait(max(0.5, total - 2.1))


class B06_SourcesAlone(Scene):
    """Three isolated blocks — ghost of missing argument arrow."""
    def construct(self):
        total = DUR["B06"]

        labels = ["Berners-Lee 2018", "Willett 2019", "Poore 2018"]
        blocks = []
        for lab in labels:
            rect = Rectangle(width=4.2, height=0.75)
            rect.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.8)
            chip = LabelChip(lab, accent=CRIMSON, size=18)
            chip.move_to(rect)
            blocks.append(VGroup(rect, chip))

        col = VGroup(*blocks).arrange(DOWN, buff=0.45).move_to(LEFT * 2.0 + DOWN * 0.1)

        # ghost placeholder: a dashed arc showing where an argument would go
        ghost_box = Rectangle(width=3.2, height=2.0)
        ghost_box.set_stroke(CRIMSON, 1.5, opacity=0.35)
        ghost_box.set_fill(opacity=0)
        ghost_box.move_to(RIGHT * 2.8 + DOWN * 0.1)
        ghost_text = Text("argument?", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        ghost_text.set_opacity(0.35).move_to(ghost_box)

        self.add(col)
        self.play(
            FadeIn(ghost_box, scale=0.9),
            FadeIn(ghost_text, scale=0.9),
            run_time=0.9
        )
        # ghost fades to show the absence
        self.play(ghost_text.animate.set_opacity(0.12),
                  ghost_box.animate.set_stroke(opacity=0.12),
                  run_time=1.0)
        self.wait(max(0.5, total - 1.9))


class B07_MechanismCard(Scene):
    """Section card — THE MECHANISM."""
    def construct(self):
        total = DUR["B07"]
        chip = LabelChip("THE MECHANISM", accent=INK, size=22)
        chip.to_corner(UL, buff=0.6)
        h = Text("Reading sources in relation", font=DISPLAY, color=INK,
                 font_size=40, weight="BOLD")
        sub = Text("not what each says — what they say together",
                   font=SERIF, color=INK, font_size=28, slant=ITALIC)
        group = VGroup(h, sub).arrange(DOWN, buff=0.4).move_to(UP * 0.1)
        u = Line(sub.get_corner(DL) + DOWN * 0.12,
                 sub.get_corner(DR) + DOWN * 0.12,
                 color=INK, stroke_width=1.8)
        self.play(FadeIn(chip, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(h, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 2.2))


class B08_SynthesisArrow(Scene):
    """Berners-Lee block becomes a premise; arrow grows toward distribution claim."""
    def construct(self):
        total = DUR["B08"]

        src_block = Rectangle(width=4.0, height=0.9)
        src_block.set_fill(INK, 0.08).set_stroke(INK, 2.0)
        chip = LabelChip("Berners-Lee 2018", accent=INK, size=20)
        premise = Text("production is sufficient", font=SERIF, color=INK, font_size=22)
        inner = VGroup(chip, premise).arrange(RIGHT, buff=0.25)
        if inner.width > 3.7:
            inner.scale_to_fit_width(3.7)
        inner.move_to(src_block)
        src = VGroup(src_block, inner).move_to(LEFT * 3.5 + UP * 0.1)

        claim_rect = Rectangle(width=4.2, height=0.9)
        claim_rect.set_fill(INK, 0.14).set_stroke(INK, 2.8)
        claim_t = Text("distribution problem", font=DISPLAY, color=INK,
                       font_size=26, weight="BOLD")
        if claim_t.width > 3.9:
            claim_t.scale_to_fit_width(3.9)
        claim_t.move_to(claim_rect)
        claim = VGroup(claim_rect, claim_t).move_to(RIGHT * 3.0 + UP * 0.1)

        arr = Arrow(src.get_right(), claim.get_left(), color=INK,
                    stroke_width=3.0, buff=0.1, tip_length=0.22)

        premise_label = SerifLabel("if production is sufficient...", INK, size=22)
        premise_label.next_to(src, DOWN, buff=0.4)

        self.play(FadeIn(src, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(premise_label, shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(arr), run_time=0.8)
        self.play(FadeIn(claim, shift=LEFT * 0.3), run_time=0.7)
        self.wait(max(0.5, total - 2.9))


class B09_ThreeArrows(Scene):
    """All three sources converge on the synthesis claim at center."""
    def construct(self):
        total = DUR["B09"]

        sources = [
            ("Berners-Lee 2018", "production sufficient"),
            ("Willett 2019",     "EAT-Lancet: consumption"),
            ("Poore 2018",       "highest-impact: richest consumers"),
        ]
        positions = [LEFT * 4.5 + UP * 1.4,
                     LEFT * 4.5 + UP * 0.0,
                     LEFT * 4.5 + DOWN * 1.4]

        src_mobs = []
        for (cit, desc), pos in zip(sources, positions):
            rect = Rectangle(width=4.0, height=0.8)
            rect.set_fill(INK, 0.08).set_stroke(INK, 1.8)
            chip = LabelChip(cit, accent=INK, size=17)
            desc_t = Text(desc, font=SERIF, color=INK, font_size=18)
            inner = VGroup(chip, desc_t).arrange(DOWN, buff=0.08)
            if inner.width > 3.7:
                inner.scale_to_fit_width(3.7)
            if inner.height > 0.72:
                inner.scale_to_fit_height(0.72)
            inner.move_to(rect)
            mob = VGroup(rect, inner).move_to(pos)
            src_mobs.append(mob)

        claim_rect = Rectangle(width=4.0, height=1.1)
        claim_rect.set_fill(INK, 0.18).set_stroke(INK, 3.0)
        claim_t = Text("distribution\nunderstated", font=DISPLAY, color=INK,
                       font_size=26, weight="BOLD")
        if claim_t.width > 3.7:
            claim_t.scale_to_fit_width(3.7)
        claim_t.move_to(claim_rect)
        claim = VGroup(claim_rect, claim_t).move_to(RIGHT * 2.8 + UP * 0.0)

        label_fourth = SerifLabel("the writer's claim", CRIMSON, size=22)
        label_fourth.next_to(claim, DOWN, buff=0.3)

        arrows = [Arrow(s.get_right(), claim.get_left(), color=INK,
                        stroke_width=2.5, buff=0.1, tip_length=0.18)
                  for s in src_mobs]

        for s in src_mobs:
            self.play(FadeIn(s, shift=RIGHT * 0.25), run_time=0.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.3, run_time=1.2))
        self.play(FadeIn(claim, scale=0.92), run_time=0.7)
        self.play(FadeIn(label_fourth, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.9))


class B11_MorphComparison(Scene):
    """Side-by-side: SUMMARY (crimson, isolated) vs SYNTHESIS (ink, connected)."""
    def construct(self):
        total = DUR["B11"]

        # dividing line
        divider = Line(UP * 3.5, DOWN * 3.5, color=SLATE, stroke_width=1.5)
        divider.move_to(ORIGIN)

        # LEFT: SUMMARY side
        s_chip = LabelChip("SUMMARY", accent=CRIMSON, size=22)
        s_chip.move_to(LEFT * 4.5 + UP * 3.0)

        s_blocks = VGroup(*[
            Rectangle(width=3.2, height=0.55).set_fill(CRIMSON, 0.09)
            .set_stroke(CRIMSON, 1.6)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.35).move_to(LEFT * 4.5 + UP * 0.2)

        # RIGHT: SYNTHESIS side
        sy_chip = LabelChip("SYNTHESIS", accent=INK, size=22)
        sy_chip.move_to(RIGHT * 4.5 + UP * 3.0)

        sy_blocks = VGroup(*[
            Rectangle(width=3.0, height=0.50).set_fill(INK, 0.08)
            .set_stroke(INK, 1.6)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.35).move_to(RIGHT * 4.5 + DOWN * 0.5)

        sy_claim = Rectangle(width=3.0, height=0.6)
        sy_claim.set_fill(INK, 0.18).set_stroke(INK, 2.5)
        sy_claim_t = Text("writer's claim", font=DISPLAY, color=INK, font_size=20,
                          weight="BOLD")
        sy_claim_t.move_to(sy_claim)
        sy_claim_grp = VGroup(sy_claim, sy_claim_t)
        sy_claim_grp.next_to(sy_blocks, UP, buff=0.3)
        sy_claim_grp.move_to(RIGHT * 4.5 + UP * 2.1)

        sy_arrows = VGroup(*[
            Arrow(b.get_top(), sy_claim_grp.get_bottom(),
                  color=INK, stroke_width=2.0, buff=0.05, tip_length=0.15)
            for b in sy_blocks
        ])

        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(s_chip, shift=DOWN * 0.1),
                  FadeIn(sy_chip, shift=DOWN * 0.1), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.2) for b in s_blocks],
                              lag_ratio=0.2, run_time=1.0))
        self.play(LaggedStart(*[FadeIn(b, shift=LEFT * 0.2) for b in sy_blocks],
                              lag_ratio=0.2, run_time=1.0))
        self.play(LaggedStart(*[GrowArrow(a) for a in sy_arrows],
                              lag_ratio=0.2, run_time=0.9))
        self.play(FadeIn(sy_claim_grp, scale=0.9), run_time=0.7)
        self.wait(max(0.5, total - 4.7))


class B12_SummaryQuote(Scene):
    """The summary paragraph — DOCUMENT beat (source: illustrative example)."""
    def construct(self):
        _quote_scene(
            self,
            "Berners-Lee et al. (2018) argue that global food production is "
            "currently sufficient. Willett et al. (2019) propose dietary shifts. "
            "Poore and Nemecek (2018) document environmental footprints.",
            "summary version — each sentence reports one source",
            None,
            "reports one source",
            DUR["B12"],
            qsize=34
        )


class B13_SynthesisMorph(Scene):
    """The morph: three source blocks rearrange, argument claim rises above."""
    def construct(self):
        total = DUR["B13"]

        src_data = [
            ("Berners-Lee 2018", "production sufficient"),
            ("Willett 2019",     "consumption: plant-based"),
            ("Poore 2018",       "highest-impact: richest consumers"),
        ]

        # Initial state: three blocks in a column (summary arrangement)
        init_positions = [UP * 1.4, UP * 0.0, DOWN * 1.4]
        blocks = []
        for (cit, desc), pos in zip(src_data, init_positions):
            rect = Rectangle(width=4.5, height=0.8)
            rect.set_fill(CRIMSON, 0.09).set_stroke(CRIMSON, 1.8)
            chip = LabelChip(cit, accent=CRIMSON, size=18)
            desc_t = Text(desc, font=SERIF, color=INK, font_size=20)
            inner = VGroup(chip, desc_t).arrange(RIGHT, buff=0.2)
            if inner.width > 4.2:
                inner.scale_to_fit_width(4.2)
            inner.move_to(rect)
            b = VGroup(rect, inner).move_to(pos + LEFT * 0.5)
            blocks.append(b)

        # Show summary state
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in blocks],
                              lag_ratio=0.25, run_time=1.2))
        self.wait(0.7)

        # Rearrange into synthesis positions (three columns converging)
        synth_positions = [LEFT * 4.2 + DOWN * 0.3,
                           DOWN * 0.3,
                           RIGHT * 4.2 + DOWN * 0.3]
        # Recolor to INK as they move
        for b in blocks:
            b[0].set_fill(INK, 0.08)
            b[0].set_stroke(INK, 1.8)

        self.play(
            blocks[0].animate.move_to(synth_positions[0]),
            blocks[1].animate.move_to(synth_positions[1]),
            blocks[2].animate.move_to(synth_positions[2]),
            run_time=1.2
        )

        # Claim rises above
        claim_rect = Rectangle(width=7.0, height=0.9)
        claim_rect.set_fill(INK, 0.18).set_stroke(INK, 3.0)
        claim_t = Text("distribution is under-addressed", font=DISPLAY,
                       color=INK, font_size=28, weight="BOLD")
        if claim_t.width > 6.6:
            claim_t.scale_to_fit_width(6.6)
        claim_t.move_to(claim_rect)
        claim = VGroup(claim_rect, claim_t).move_to(UP * 1.9)

        label = SerifLabel("the argument no source made alone", CRIMSON, size=22)
        label.next_to(claim, UP, buff=0.3)

        arrows = [
            Arrow(b.get_top(), claim.get_bottom(),
                  color=INK, stroke_width=2.5, buff=0.08, tip_length=0.18)
            for b in blocks
        ]

        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.2, run_time=1.0))
        self.play(FadeIn(claim, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(label, shift=DOWN * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 5.4))


class B14_DiagnosticOne(Scene):
    """Diagnostic 1: remove citations, does the argument hold?"""
    def construct(self):
        total = DUR["B14"]

        chip = LabelChip("DIAGNOSTIC 1", accent=CRIMSON, size=22)
        chip.to_corner(UL, buff=0.6)

        q = Text("Remove all citations.", font=DISPLAY, color=INK,
                 font_size=34, weight="BOLD")
        q2 = Text("Is there still an argument?", font=SERIF, color=INK,
                  font_size=28, slant=ITALIC)
        q_group = VGroup(q, q2).arrange(DOWN, buff=0.3).move_to(UP * 1.5)

        # Two outcome blocks side by side
        yes_rect = Rectangle(width=3.5, height=1.0)
        yes_rect.set_fill(INK, 0.12).set_stroke(INK, 2.2)
        yes_t = Text("argument holds", font=SERIF, color=INK, font_size=22)
        yes_t.move_to(yes_rect)
        yes_label = LabelChip("citations = evidence", accent=INK, size=18)
        yes_label.next_to(yes_rect, DOWN, buff=0.2)
        yes_grp = VGroup(yes_rect, yes_t, yes_label).move_to(LEFT * 2.8 + DOWN * 0.7)

        no_rect = Rectangle(width=3.5, height=1.0)
        no_rect.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2.2)
        no_t = Text("nothing remains", font=SERIF, color=CRIMSON, font_size=22)
        no_t.move_to(no_rect)
        no_label = LabelChip("summary, not argument", accent=CRIMSON, size=18)
        no_label.next_to(no_rect, DOWN, buff=0.2)
        no_grp = VGroup(no_rect, no_t, no_label).move_to(RIGHT * 2.8 + DOWN * 0.7)

        self.play(FadeIn(chip, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(q, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(yes_grp, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(no_grp, shift=UP * 0.2), run_time=0.7)
        self.wait(max(0.5, total - 3.2))


class B15_DiagnosticTwo(Scene):
    """Diagnostic 2: does the paragraph say something no single source says?"""
    def construct(self):
        total = DUR["B15"]

        chip = LabelChip("DIAGNOSTIC 2", accent=CRIMSON, size=22)
        chip.to_corner(UL, buff=0.6)

        # Three source blocks at bottom
        src_pos = [LEFT * 4.2 + DOWN * 1.8,
                   DOWN * 1.8,
                   RIGHT * 4.2 + DOWN * 1.8]
        src_labs = ["Berners-Lee", "Willett", "Poore"]
        src_mobs = []
        for lab, pos in zip(src_labs, src_pos):
            rect = Rectangle(width=3.0, height=0.7)
            rect.set_fill(INK, 0.08).set_stroke(INK, 1.6)
            t = Text(lab, font=SERIF, color=INK, font_size=22)
            t.move_to(rect)
            src_mobs.append(VGroup(rect, t).move_to(pos))

        # The fourth element — rises above
        claim_rect = Rectangle(width=5.5, height=0.8)
        claim_rect.set_fill(INK, 0.18).set_stroke(INK, 3.0)
        claim_t = Text("the fourth element", font=DISPLAY, color=INK,
                       font_size=26, weight="BOLD")
        claim_t.move_to(claim_rect)
        claim = VGroup(claim_rect, claim_t).move_to(UP * 0.8)

        label = SerifLabel("only synthesis produces this", CRIMSON, size=22)
        label.next_to(claim, UP, buff=0.3)

        arrows = [Arrow(s.get_top(), claim.get_bottom(), color=INK,
                        stroke_width=2.5, buff=0.08, tip_length=0.18)
                  for s in src_mobs]

        self.play(FadeIn(chip, shift=RIGHT * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.2) for s in src_mobs],
                              lag_ratio=0.2, run_time=1.0))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.2, run_time=0.9))
        self.play(FadeIn(claim, shift=DOWN * 0.3), run_time=0.7)
        self.play(FadeIn(label, shift=DOWN * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.6))


class B16_Endcard(Scene):
    """Recap endcard — question restated, answer given, WRITING kicker."""
    def construct(self):
        total = DUR["B16"]
        eye = Text("WRITING", font=DISPLAY, color=INK, font_size=22)
        t1 = Text("Synthesis is the argument", font=DISPLAY, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("no source makes for you.", font=DISPLAY, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2.5)
        sub = Text("does your paragraph say something no single source also says?",
                   font=SERIF, color=INK, font_size=22, slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.45)
        eye.next_to(block, UP, buff=0.85)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(t1, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(t2, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))
