"""vox_scenes.py — Why Your Examples Teach More Than Your Instructions
(vox-examples-teach-more, slate cut, 16:9)

One Scene per GRAPHIC / CARD beat whose source is 'own'.
B02 is STILL·ai — no scene. Durations come from beat_sheet.json actuals (or
estimates before audio lock).

Color law (teardown palette):
  INK     = intended features / good output (plain warm near-black)
  CRIMSON = unintended features that get copied
  SLATE   = structural scaffolding (neutral gray)

Exclusions: no few-shot benchmark research, no attention mechanism,
no in-context learning theory.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 11.0, "B05": 12.0,
    "B06": 11.0, "B07": 10.0, "B08": 10.0, "B09": 13.0,
    "B10": 10.0, "B11": 12.0, "B12": 12.0, "B13": 11.0, "B14": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _bar(w=2.5, h=0.28, color=INK, opacity=0.85):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return r


def _label(text, color=INK, size=26):
    return Text(text, font=SERIF, color=color, font_size=size)


def _chip(text, accent=SLATE, size=22):
    return LabelChip(text, accent=accent, size=size)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight=BOLD)
        t1 = Text("Why your examples", font=SERIF, color=INK,
                  font_size=54, weight=BOLD)
        t2 = Text("teach more than your instructions", font=SERIF, color=INK,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = Text("the features you never meant to copy", font=SERIF,
                   color=SLATE, font_size=28)
        sub.next_to(u, DOWN, buff=0.45)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q = Text("Why did the example", font=SERIF, color=INK,
                 font_size=50, weight=BOLD)
        q2 = Text("teach more than she intended?", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(q, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q), run_time=0.7)
        self.play(FadeIn(q2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.6))


class B04_InstructionVsExample(Scene):
    """Two-column: explicit instruction (left) vs demonstration example (right)."""
    def construct(self):
        total = DUR["B04"]
        # left column — instruction
        lcol_head = _chip("INSTRUCTION", accent=SLATE, size=22)
        lcol_body = _label("Write in paragraphs,\none topic each.", INK, 28)
        lcol = VGroup(lcol_head, lcol_body).arrange(DOWN, buff=0.4)
        lcol.move_to(LEFT * 3.2)
        # right column — example
        rcol_head = _chip("EXAMPLE", accent=CRIMSON, size=22)
        # mini "memo" representation: several bars
        memo_bars = VGroup(*[_bar(2.4, 0.22, INK, 0.55) for _ in range(4)])
        memo_bars.arrange(DOWN, buff=0.14)
        rcol = VGroup(rcol_head, memo_bars).arrange(DOWN, buff=0.4)
        rcol.move_to(RIGHT * 3.2)
        # divider
        div = Line(UP * 3.0, DOWN * 3.0, color=SLATE, stroke_width=1.5)
        div.move_to(ORIGIN)
        # labels
        lsub = _label("explicit: you name the rule", SLATE, 22)
        lsub.next_to(lcol, DOWN, buff=0.35)
        rsub = _label("implicit: teaches by demonstration", CRIMSON, 22)
        rsub.next_to(rcol, DOWN, buff=0.35)
        self.play(FadeIn(div), run_time=0.5)
        self.play(FadeIn(lcol_head), FadeIn(lcol_body), run_time=0.8)
        self.play(FadeIn(rcol_head),
                  LaggedStart(*[FadeIn(b, scale=0.9) for b in memo_bars], lag_ratio=0.1),
                  run_time=1.0)
        self.play(FadeIn(lsub, shift=UP * 0.1), FadeIn(rsub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.0))


class B05_FeatureDimensions(Scene):
    """A memo with feature labels appearing one by one."""
    def construct(self):
        total = DUR["B05"]
        # memo representation: rows of text bars
        memo_head = _chip("CASUAL MEMO", accent=SLATE, size=22)
        bars = VGroup(*[_bar(4.0, 0.22, INK, 0.45) for _ in range(5)])
        bars.arrange(DOWN, buff=0.15)
        memo = VGroup(memo_head, bars).arrange(DOWN, buff=0.3)
        memo.move_to(LEFT * 2.0)
        # feature labels on the right with arrows
        features = [
            ("structure: paragraphs", INK),
            ("register: casual", CRIMSON),
            ("sentence length: short", CRIMSON),
            ("hedging: frequent", CRIMSON),
            ("vocabulary: informal", CRIMSON),
        ]
        feature_labels = VGroup()
        for i, (text, color) in enumerate(features):
            lbl = _label(text, color, 24)
            lbl.move_to(RIGHT * 2.8 + UP * (1.0 - i * 0.55))
            feature_labels.add(lbl)
        self.play(FadeIn(memo), run_time=0.8)
        # labels appear one by one
        for lbl in feature_labels:
            self.play(FadeIn(lbl, shift=LEFT * 0.2), run_time=0.4)
        self.wait(max(0.5, total - 0.8 - len(features) * 0.4))


class B06_AllFeaturesEqual(Scene):
    """All feature bars shown with equal-weight indicators."""
    def construct(self):
        total = DUR["B06"]
        title = _label("Claude sees all features equally", INK, 30)
        title.to_edge(UP, buff=0.7)
        features = [
            ("structure", INK),
            ("register", CRIMSON),
            ("sentence length", CRIMSON),
            ("hedging density", CRIMSON),
            ("vocabulary", CRIMSON),
        ]
        bars = VGroup()
        for i, (text, color) in enumerate(features):
            bar = Rectangle(width=4.5, height=0.38)
            bar.set_fill(color, 0.75).set_stroke(width=0, opacity=0)
            lbl = Text(text, font=SERIF, color=INK, font_size=24)
            lbl.next_to(bar, LEFT, buff=0.25)
            grp = VGroup(lbl, bar)
            bars.add(grp)
        bars.arrange(DOWN, buff=0.22).move_to(DOWN * 0.2)
        # equal-weight label
        eq_label = SerifLabel("equal weight as teaching signal", CRIMSON, size=26)
        eq_label.next_to(bars, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(b, scale=0.95) for b in bars], lag_ratio=0.1),
                  run_time=1.2)
        self.play(FadeIn(eq_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B07_AllFeaturesCopied(Scene):
    """Features flowing from example into output — all of them."""
    def construct(self):
        total = DUR["B07"]
        # source: memo chip
        src = _chip("CASUAL MEMO", accent=SLATE, size=24)
        src.move_to(LEFT * 4.5 + UP * 0.5)
        # destination: board report chip (red — wrong)
        dst = _chip("BOARD REPORT?", accent=CRIMSON, size=24)
        dst.move_to(RIGHT * 4.5 + UP * 0.5)
        # arrow
        arr = Arrow(LEFT * 2.5 + UP * 0.5, RIGHT * 2.5 + UP * 0.5,
                    color=CRIMSON, stroke_width=4, buff=0.2)
        # features listed under the arrow
        feature_text = [
            "structure  +  register  +  sentence length  +  hedging  +  vocabulary"
        ]
        feat_lbl = _label(feature_text[0], CRIMSON, 22)
        feat_lbl.next_to(arr, DOWN, buff=0.3)
        # result label
        result = _label("output: sounds like the memo", CRIMSON, 28)
        result.move_to(DOWN * 2.2)
        self.play(FadeIn(src), FadeIn(dst), run_time=0.7)
        self.play(GrowArrow(arr), run_time=0.7)
        self.play(FadeIn(feat_lbl, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(result, scale=0.95), run_time=0.6)
        self.wait(max(0.5, total - 2.6))


class B08_SectionCard(Scene):
    """Section card: The fix: annotate the example."""
    def construct(self):
        total = DUR["B08"]
        t = Text("The fix:", font=DISPLAY, color=INK, font_size=52, weight=BOLD)
        t2 = Text("annotate the example", font=DISPLAY, color=CRIMSON,
                  font_size=52, weight=BOLD)
        block = VGroup(t, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B09_AnnotatedExample(Scene):
    """Memo with feature labels: COPY (ink) vs SKIP (crimson, crossed out)."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Annotated example", INK, 30)
        title.to_edge(UP, buff=0.7)
        memo_head = _chip("MEMO EXAMPLE", accent=SLATE, size=22)
        memo_head.move_to(LEFT * 3.0 + UP * 1.5)
        # features
        features = [
            ("structure: paragraphs", True),   # True = copy
            ("register: casual", False),        # False = skip
            ("sentence length: short", False),
            ("hedging: frequent", False),
            ("vocabulary: informal", False),
        ]
        labels = VGroup()
        strikes = VGroup()
        copy_chips = VGroup()
        skip_chips = VGroup()
        for i, (text, copy) in enumerate(features):
            y = 0.8 - i * 0.6
            lbl = _label(text, INK if copy else SLATE, 24)
            lbl.move_to(LEFT * 1.0 + UP * y)
            labels.add(lbl)
            if copy:
                chip = _chip("COPY", accent=INK, size=18)
                chip.next_to(lbl, RIGHT, buff=0.3)
                copy_chips.add(chip)
            else:
                chip = _chip("SKIP", accent=CRIMSON, size=18)
                chip.next_to(lbl, RIGHT, buff=0.3)
                skip_chips.add(chip)
                strike = Line(lbl.get_left() + LEFT * 0.05,
                              lbl.get_right() + RIGHT * 0.05,
                              color=CRIMSON, stroke_width=2)
                strike._qc_intentional = True
                strikes.add(strike)
        self.play(FadeIn(title), FadeIn(memo_head), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.1),
                  run_time=0.9)
        # first show the COPY chip for structure
        self.play(FadeIn(copy_chips[0]), run_time=0.4)
        # then strike through the rest and show SKIP chips
        for s, c in zip(strikes, skip_chips):
            self.play(Create(s), FadeIn(c), run_time=0.35)
        self.wait(max(0.5, total - 0.7 - 0.9 - 0.4 - len(strikes) * 0.35))


class B10_AnyExample(Scene):
    """Any example contains feature dimensions — three different source types."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Any example teaches all its features", INK, 30)
        title.to_edge(UP, buff=0.7)
        sources = [
            ("competitor's post", CRIMSON),
            ("a paper abstract", CRIMSON),
            ("a quote you liked", CRIMSON),
        ]
        cards = VGroup()
        for text, color in sources:
            card = Rectangle(width=3.2, height=1.4)
            card.set_fill(color, 0.08).set_stroke(color, 1.8)
            lbl = _label(text, color, 26)
            lbl.move_to(card.get_center())
            sub = _label("dozens of features", SLATE, 20)
            sub.next_to(lbl, DOWN, buff=0.2)
            cards.add(VGroup(card, lbl, sub))
        cards.arrange(RIGHT, buff=0.5).move_to(DOWN * 0.3)
        note = SerifLabel("without annotation, all of them teach", CRIMSON, size=26)
        note.next_to(cards, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.95) for c in cards], lag_ratio=0.15),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B11_MarcoExample(Scene):
    """Marco pastes competitor post; exclamation points come through."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Marco: competitor post -> product blog", INK, 28)
        title.to_edge(UP, buff=0.7)
        # competitor post box
        comp_head = _chip("COMPETITOR POST", accent=SLATE, size=20)
        comp_head.move_to(LEFT * 3.8 + UP * 1.0)
        comp_features = VGroup(
            _label("short sentences", INK, 22),
            _label("punchy tone", INK, 22),
            _label("exclamation points!!!", CRIMSON, 22),
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 3.8 + DOWN * 0.1)
        # output box
        out_head = _chip("OUTPUT", accent=CRIMSON, size=20)
        out_head.move_to(RIGHT * 3.8 + UP * 1.0)
        out_features = VGroup(
            _label("short sentences", INK, 22),
            _label("punchy tone", INK, 22),
            _label("exclamation points!!!", CRIMSON, 22),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 3.8 + DOWN * 0.1)
        arr = Arrow(LEFT * 1.5 + UP * 0.0, RIGHT * 1.5 + UP * 0.0,
                    color=CRIMSON, stroke_width=4, buff=0.2)
        note = _label("he never labeled them as features to exclude", CRIMSON, 24)
        note.move_to(DOWN * 2.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(comp_head),
                  LaggedStart(*[FadeIn(f) for f in comp_features], lag_ratio=0.15),
                  run_time=0.9)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(FadeIn(out_head),
                  LaggedStart(*[FadeIn(f) for f in out_features], lag_ratio=0.15),
                  run_time=0.9)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.4))


class B12_MarcoFixed(Scene):
    """Marco adds annotation; exclamation points excluded from output."""
    def construct(self):
        total = DUR["B12"]
        title = _label("One annotation line — excluded feature disappears", INK, 28)
        title.to_edge(UP, buff=0.7)
        # annotation chip
        annotation = _chip("ANNOTATION ADDED", accent=INK, size=20)
        annotation.move_to(LEFT * 3.8 + UP * 1.2)
        ann_text = _label("copy the punchy short sentences.\nNot the exclamation points.", INK, 22)
        ann_text.next_to(annotation, DOWN, buff=0.3)
        # output box
        out_head = _chip("OUTPUT", accent=INK, size=20)
        out_head.move_to(RIGHT * 3.8 + UP * 1.2)
        out_features = VGroup(
            _label("short sentences", INK, 22),
            _label("punchy tone", INK, 22),
            _label("zero exclamation points", INK, 22),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 3.8 + DOWN * 0.1)
        arr = Arrow(LEFT * 1.0 + UP * 0.0, RIGHT * 1.0 + UP * 0.0,
                    color=INK, stroke_width=4, buff=0.2)
        result = SerifLabel("the example stayed; the annotation narrowed it", INK, size=26)
        result.move_to(DOWN * 2.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(annotation), FadeIn(ann_text), run_time=0.8)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(FadeIn(out_head),
                  LaggedStart(*[FadeIn(f) for f in out_features], lag_ratio=0.15),
                  run_time=0.9)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B13_Practice(Scene):
    """Two-sentence annotation practice template."""
    def construct(self):
        total = DUR["B13"]
        title = _label("Before pasting any example:", INK, 30)
        title.to_edge(UP, buff=0.7)
        q1_label = _chip("SENTENCE 1", accent=INK, size=22)
        q1_text = _label("Which features should Claude copy?", INK, 32)
        q1 = VGroup(q1_label, q1_text).arrange(DOWN, buff=0.25)
        q1.move_to(UP * 0.5)
        q2_label = _chip("SENTENCE 2", accent=CRIMSON, size=22)
        q2_text = _label("Which features should it ignore?", CRIMSON, 32)
        q2 = VGroup(q2_label, q2_text).arrange(DOWN, buff=0.25)
        q2.move_to(DOWN * 1.1)
        note = SerifLabel("two sentences = the actual specification", INK, size=26)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(q1_label), FadeIn(q1_text), run_time=0.7)
        self.play(FadeIn(q2_label), FadeIn(q2_text), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B14_End(Scene):
    """Endcard — recap."""
    def construct(self):
        total = DUR["B14"]
        t1 = Text("Unannotated examples teach everything.", font=SERIF,
                  color=INK, font_size=44, weight=BOLD)
        t2 = Text("Annotation makes them precise.", font=SERIF,
                  color=INK, font_size=44, weight=BOLD)
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
