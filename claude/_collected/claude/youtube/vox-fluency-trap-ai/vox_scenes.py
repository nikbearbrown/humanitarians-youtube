"""vox_scenes.py — Why AI Output That Sounds Right Can Be Completely Wrong
(vox-fluency-trap-ai, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
STILL beats B01 and B11 are ai-media slots — no scene here.

Color law: TEAL = real/verified/grounded; CRIMSON = hallucinated/fabricated/empty.
Never swap mid-film.

Exclusions: NO transformer architecture, NO Bayesian formalism, NO RAG solution,
NO semantic entropy math.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 9.0, "B03": 10.0, "B04": 9.0, "B05": 11.0,
    "B06": 12.0, "B07": 11.0, "B08": 11.0, "B09": 13.0,
    "B10": 11.0, "B12": 12.0, "B13": 12.0, "B14": 14.0,
    "B15": 10.0, "B16": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _citation_card(label, accent, width=4.8, height=1.8):
    """A formatted citation-like card in the accent color."""
    box = Rectangle(width=width, height=height)
    box.set_fill(accent, 0.12).set_stroke(accent, 2.0)
    title = Text("Author et al. (2024)", font=SERIF, color=INK, font_size=24)
    journal = Text("Journal of Research, vol. 12, pp. 45-67", font=SERIF,
                   color=INK, font_size=18)
    doi = Text("doi:10.xxxx/xxxxxx", font=MONO, color=INK, font_size=16)
    content = VGroup(title, journal, doi).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    content.move_to(box).shift(RIGHT * 0.1)
    chip = LabelChip(label, accent=accent, size=18)
    chip.next_to(box, UP, buff=0.15)
    return VGroup(box, content), chip


class B02_CitationClick(Scene):
    def construct(self):
        total = DUR["B02"]
        # citation card center
        cite_box = Rectangle(width=6.0, height=2.0)
        cite_box.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        title = Text("Housing Market Stability, 2023", font=SERIF, color=INK, font_size=26)
        journal = Text("Urban Studies Quarterly, vol. 18, p. 112-134", font=SERIF,
                       color=INK, font_size=20)
        doi_text = Text("doi:10.1234/usq.2023.18.112", font=MONO, color=TEAL, font_size=18)
        content = VGroup(title, journal, doi_text).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        content.move_to(cite_box).shift(RIGHT * 0.2)
        cite_group = VGroup(cite_box, content)
        cite_group.move_to(ORIGIN + UP * 0.2)

        # not found chip
        not_found = LabelChip("NOT FOUND", accent=CRIMSON, size=36)
        not_found.move_to(ORIGIN + UP * 0.2)

        self.play(FadeIn(cite_group), run_time=0.9)
        # cursor appears (simulated with a dot)
        cursor = Dot(radius=0.08, color=INK).move_to(doi_text.get_center())
        self.play(FadeIn(cursor, scale=0.5), run_time=0.3)
        self.play(cursor.animate.scale(1.4), run_time=0.2)
        self.play(cursor.animate.scale(1.0 / 1.4), run_time=0.2)
        # citation fades to crimson blur, then NOT FOUND pops in
        self.play(cite_group.animate.set_opacity(0.18), run_time=0.5)
        self.play(FadeOut(cursor), FadeOut(cite_group),
                  FadeIn(not_found, scale=0.7), run_time=0.7)
        self.wait(max(0.5, total - 2.8))


class B03_TwoCitations(Scene):
    def construct(self):
        total = DUR["B03"]
        # two citation cards side by side — look identical
        lbox = Rectangle(width=5.2, height=2.4)
        lbox.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8).move_to(LEFT * 3.0)
        rbox = Rectangle(width=5.2, height=2.4)
        rbox.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.8).move_to(RIGHT * 3.0)

        def _cite_content(center):
            t = Text("Research on AI Confidence, 2023", font=SERIF,
                     color=INK, font_size=22)
            j = Text("Artificial Intelligence Review, vol. 5", font=SERIF,
                     color=INK, font_size=18)
            d = Text("doi:10.xxxx/air.2023.5", font=MONO, color=INK, font_size=16)
            g = VGroup(t, j, d).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            g.move_to(center).shift(RIGHT * 0.15)
            return g

        lc = _cite_content(LEFT * 3.0)
        rc = _cite_content(RIGHT * 3.0)

        question = Text("Which is real?", font=SERIF, color=INK, font_size=30)
        question.to_edge(UP, buff=0.7)

        self.play(FadeIn(lbox), FadeIn(lc), run_time=0.8)
        self.play(FadeIn(rbox), FadeIn(rc), run_time=0.8)
        self.play(FadeIn(question, shift=DOWN * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 2.3))


class B04_TheQuestion(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("How does an AI produce a fake citation", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("with the same confidence as a real one?", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.16, q2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


class B05_NaiveExpect(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("THE NAIVE EXPECTATION", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.7)

        speaker = LabelChip("confident text", accent=TEAL, size=26)
        speaker.move_to(LEFT * 3.0 + UP * 0.1)

        arrow = Arrow(LEFT * 1.2 + UP * 0.1, RIGHT * 0.8 + UP * 0.1,
                      color=INK, stroke_width=3, buff=0.0)

        source = LabelChip("real source", accent=TEAL, size=26)
        source.move_to(RIGHT * 2.8 + UP * 0.1)

        label = SerifLabel("what we expect from human writing", SLATE, size=24)
        label.next_to(VGroup(speaker, source), DOWN, buff=0.6)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(speaker), run_time=0.6)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(source), run_time=0.6)
        self.play(FadeIn(label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


class B06_PlausibilityEngine(Scene):
    def construct(self):
        total = DUR["B06"]
        # model box
        model_box = Rectangle(width=3.2, height=1.8)
        model_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2.0).move_to(LEFT * 2.0)
        model_label = Text("language model", font=DISPLAY, color=INK,
                           font_size=24, weight="MEDIUM")
        model_label.move_to(model_box)
        model_group = VGroup(model_box, model_label)

        # two output arrows
        plaus_arrow = Arrow(LEFT * 0.35, RIGHT * 1.5 + UP * 0.9,
                            color=TEAL, stroke_width=5, buff=0.0)
        ground_arrow = Arrow(LEFT * 0.35, RIGHT * 1.5 + DOWN * 0.9,
                             color=CRIMSON, stroke_width=3, buff=0.0)

        plaus_chip = LabelChip("plausible text", accent=TEAL, size=24)
        plaus_chip.move_to(RIGHT * 3.5 + UP * 0.9)

        ground_chip = LabelChip("grounded text", accent=SLATE, size=24)
        ground_chip.move_to(RIGHT * 3.5 + DOWN * 0.9)
        ground_chip.set_opacity(0.35)

        # X through the grounded arrow
        cross = Text("x", font=SERIF, color=CRIMSON, font_size=32, weight="BOLD")
        cross.move_to(ground_arrow.get_center())

        optim_label = SerifLabel("optimizes for:", SLATE, size=22)
        optim_label.next_to(model_group, LEFT, buff=0.5)
        optim_label.shift(DOWN * 0.5)

        self.play(FadeIn(model_group), run_time=0.7)
        self.play(FadeIn(optim_label), run_time=0.5)
        self.play(Create(plaus_arrow), FadeIn(plaus_chip), run_time=0.8)
        self.play(Create(ground_arrow), FadeIn(ground_chip), run_time=0.7)
        self.play(FadeIn(cross, scale=1.2), run_time=0.5)
        self.wait(max(0.5, total - 3.2))


class B07_SameProcess(Scene):
    def construct(self):
        total = DUR["B07"]
        # generate box
        gen_box = Rectangle(width=2.8, height=1.6)
        gen_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2.0).move_to(LEFT * 3.0)
        gen_label = Text("generate", font=DISPLAY, color=INK,
                         font_size=26, weight="MEDIUM")
        gen_label.move_to(gen_box)
        gen_group = VGroup(gen_box, gen_label)

        # two arrows to real and hallucinated chips
        real_arrow = Arrow(LEFT * 1.55, RIGHT * 0.6 + UP * 1.1,
                           color=TEAL, stroke_width=4, buff=0.0)
        hall_arrow = Arrow(LEFT * 1.55, RIGHT * 0.6 + DOWN * 1.1,
                           color=CRIMSON, stroke_width=4, buff=0.0)

        real_chip = LabelChip("REAL citation", accent=TEAL, size=26)
        real_chip.move_to(RIGHT * 3.2 + UP * 1.1)
        hall_chip = LabelChip("HALLUCINATED citation", accent=CRIMSON, size=26)
        hall_chip.move_to(RIGHT * 3.2 + DOWN * 1.1)

        conf_label = SerifLabel("identical confidence", SLATE, size=22)
        conf_label.move_to(RIGHT * 3.2)

        self.play(FadeIn(gen_group), run_time=0.7)
        self.play(Create(real_arrow), FadeIn(real_chip), run_time=0.7)
        self.play(Create(hall_arrow), FadeIn(hall_chip), run_time=0.7)
        self.play(FadeIn(conf_label, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B08_FluencyCard(Scene):
    def construct(self):
        total = DUR["B08"]
        t1 = Text("Fluency is not", font=SERIF, color=INK,
                  font_size=54, weight="BOLD")
        t2 = Text("a verification signal.", font=SERIF, color=CRIMSON,
                  font_size=54, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


class B09_SixCitations(Scene):
    def construct(self):
        total = DUR["B09"]
        chips = []
        labels = ["C1", "C2", "C3", "C4", "C5", "C6"]
        for i, lbl in enumerate(labels):
            chip = Rectangle(width=1.5, height=1.0)
            chip.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.8)
            t = Text(lbl, font=MONO, color=INK, font_size=28, weight="BOLD")
            t.move_to(chip)
            chips.append(VGroup(chip, t))

        row1 = VGroup(*chips[:3]).arrange(RIGHT, buff=0.5).move_to(UP * 0.7)
        row2 = VGroup(*chips[3:]).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.7)
        all_chips = VGroup(row1, row2)

        eye = Text("six citations, identical confidence", font=SERIF,
                   color=INK, font_size=26)
        eye.to_edge(UP, buff=0.6)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.85) for c in chips],
                              lag_ratio=0.07, run_time=1.4))
        self.wait(0.5)

        # C2 flips crimson — reversed
        c2 = chips[1]
        rev_chip = LabelChip("REVERSED", accent=CRIMSON, size=18)
        rev_chip.move_to(c2.get_center() + DOWN * 0.85)
        c2[0].set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 1.8)
        c2[1].set_color(CRIMSON)
        self.play(FadeIn(c2), FadeIn(rev_chip), run_time=0.7)

        # C4 flips crimson — 404
        c4 = chips[3]
        gone_chip = LabelChip("404", accent=CRIMSON, size=18)
        gone_chip.move_to(c4.get_center() + DOWN * 0.85)
        c4[0].set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 1.8)
        c4[1].set_color(CRIMSON)
        self.play(FadeIn(c4), FadeIn(gone_chip), run_time=0.7)

        self.wait(max(0.5, total - 3.8))


class B10_StyleCard(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Style is not signal.", font=SERIF, color=INK,
                  font_size=58, weight="BOLD")
        t1.move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        sub = Text("The appearance of a citation is not evidence that the source exists.",
                   font=SERIF, color=INK, font_size=26)
        sub.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), Create(u), run_time=1.1)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 1.8))


class B12_VerifyGate(Scene):
    def construct(self):
        total = DUR["B12"]
        # gate posts
        gate_center = ORIGIN + DOWN * 0.1
        gh = 2.6
        lp = Line(gate_center + LEFT * 0.6 + DOWN * gh / 2,
                  gate_center + LEFT * 0.6 + UP * gh / 2,
                  color=INK, stroke_width=5)
        rp = Line(gate_center + RIGHT * 0.6 + DOWN * gh / 2,
                  gate_center + RIGHT * 0.6 + UP * gh / 2,
                  color=INK, stroke_width=5)
        lintel = Line(gate_center + LEFT * 0.8 + UP * gh / 2,
                      gate_center + RIGHT * 0.8 + UP * gh / 2,
                      color=INK, stroke_width=5)
        gate = VGroup(lp, rp, lintel)
        gate_lbl = LabelChip("OPEN IT", accent=TEAL, size=22)
        gate_lbl.next_to(lintel, UP, buff=0.18)

        # incoming citation chips (neutral)
        incoming = []
        for i in range(4):
            b = Rectangle(width=1.0, height=0.55)
            b.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.5)
            b.move_to(LEFT * 4.8 + UP * (1.1 - i * 0.75))
            incoming.append(b)

        # output buckets
        real_bkt = Rectangle(width=2.0, height=1.8)
        real_bkt.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8).move_to(RIGHT * 3.5 + UP * 0.7)
        real_lbl = LabelChip("REAL", accent=TEAL, size=22).next_to(real_bkt, UP, buff=0.15)

        fake_bkt = Rectangle(width=2.0, height=1.0)
        fake_bkt.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.8).move_to(RIGHT * 3.5 + DOWN * 1.4)
        fake_lbl = LabelChip("FABRICATED", accent=CRIMSON, size=22).next_to(fake_bkt, DOWN, buff=0.15)

        self.play(FadeIn(gate), FadeIn(gate_lbl), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(c) for c in incoming], lag_ratio=0.1, run_time=0.8))
        self.play(FadeIn(real_bkt), FadeIn(real_lbl), run_time=0.6)
        self.play(FadeIn(fake_bkt), FadeIn(fake_lbl), run_time=0.5)
        # animate three chips to real, one to fake — single-method animate only
        for i, chip in enumerate(incoming[:3]):
            chip.set_fill(TEAL, 0.5).set_stroke(TEAL, 1.5)
            self.play(chip.animate.move_to(real_bkt.get_center() + UP * (0.3 - i * 0.3)),
                      run_time=0.3)
        incoming[3].set_fill(CRIMSON, 0.5).set_stroke(CRIMSON, 1.5)
        self.play(incoming[3].animate.move_to(fake_bkt.get_center()), run_time=0.4)
        self.wait(max(0.5, total - 3.4))


class B13_CheckList(Scene):
    def construct(self):
        total = DUR["B13"]
        eye = Text("THE CITATION CHECK", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        eye.to_edge(UP, buff=0.7)

        items = ["author", "title", "journal + year", "claim matches"]
        rows = []
        for item in items:
            lbl = SerifLabel(item, TEAL, size=32)
            rows.append(lbl)

        col = VGroup(*rows).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        col.move_to(ORIGIN + LEFT * 0.5)

        self.play(FadeIn(eye), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        self.wait(max(0.5, total - len(rows) * 0.8 - 0.5))


class B14_Example(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("Mia checks six citations", font=SERIF, color=INK, font_size=26)
        eye.to_edge(UP, buff=0.7)

        # six chips
        chips = []
        labels = ["C1", "C2", "C3", "C4", "C5", "C6"]
        for lbl in labels:
            b = Rectangle(width=1.3, height=0.9)
            b.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.8)
            t = Text(lbl, font=MONO, color=INK, font_size=24, weight="BOLD")
            t.move_to(b)
            chips.append(VGroup(b, t))

        row = VGroup(*chips).arrange(RIGHT, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.85) for c in chips],
                              lag_ratio=0.06, run_time=1.2))
        self.wait(0.4)

        # chips 0,2,4,5 get ticks (teal); chip 1 gets REVERSED; chip 3 gets FABRICATED
        tick_ids = [0, 2, 4, 5]
        for idx in tick_ids:
            chips[idx][0].set_fill(TEAL, 0.55).set_stroke(TEAL, 1.8)

        rev_lbl = LabelChip("REVERSED", accent=CRIMSON, size=16)
        rev_lbl.next_to(chips[1], DOWN, buff=0.2)
        fab_lbl = LabelChip("FABRICATED", accent=CRIMSON, size=16)
        fab_lbl.next_to(chips[3], DOWN, buff=0.2)

        # set colors directly, then fade in to show the change — single-method animate
        for i in tick_ids:
            chips[i][0].set_fill(TEAL, 0.55)
        chips[1][0].set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 1.8)
        chips[1][1].set_color(CRIMSON)
        chips[3][0].set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 1.8)
        chips[3][1].set_color(CRIMSON)
        self.play(AnimationGroup(*[chips[i][0].animate.scale(1.05) for i in tick_ids],
                                 lag_ratio=0.05, run_time=0.6),
                  chips[1].animate.shift(UP * 0.0),
                  chips[3].animate.shift(UP * 0.0))
        self.play(FadeIn(rev_lbl), FadeIn(fab_lbl), run_time=0.7)

        result = LabelChip("defensible presentation", accent=TEAL, size=24)
        result.next_to(row, DOWN, buff=0.9)
        self.play(FadeIn(result, scale=0.9), run_time=0.7)
        self.wait(max(0.5, total - 3.8))


class B15_OneRule(Scene):
    def construct(self):
        total = DUR["B15"]
        t1 = Text("No verification path,", font=SERIF, color=INK,
                  font_size=52, weight="BOLD")
        t2 = Text("no delegation.", font=SERIF, color=CRIMSON,
                  font_size=52, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


class B16_End(Scene):
    def construct(self):
        total = DUR["B16"]
        eye = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        t1 = Text("Fluency is not accuracy.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("Open every citation.", font=SERIF, color=TEAL,
                  font_size=50, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 2.2))
