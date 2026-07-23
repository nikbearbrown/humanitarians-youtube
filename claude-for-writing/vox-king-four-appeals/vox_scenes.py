"""vox_scenes.py — Why the Most Powerful Persuasion Feels Inevitable
(vox-king-four-appeals, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. STILL beats (B01, B11)
have no scene — they compile as slates until the ai stills are filled.

Color law:
  TEAL = the analyzed appeal doing real work — the machinery of persuasion
  CRIMSON = the surface reading that misses the machinery
  GOLD = editor's pen highlight (once per graphic, fill only, never text)

Exclusions honored: NO full Letter context, NO civil rights history beyond
what the Letter itself names, NO speech-version debate.

Gate B: every zero-width stroke is also zero-opacity.
Gate A: single-method .animate chains only; every scene has real shape motion.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 9.0, "B03": 12.0, "B04": 10.0, "B05": 11.0,
    "B06": 14.0, "B07": 12.0, "B08": 13.0, "B09": 12.0,
    "B10": 14.0, "B12": 14.0, "B13": 11.0, "B14": 14.0,
    "B15": 13.0, "B16": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _chip(label, accent=TEAL, size=26):
    return LabelChip(label, accent=accent, size=size)


def _serif(text, size=32, color=INK, bold=False):
    kw = {"weight": "BOLD"} if bold else {}
    return Text(text, font=SERIF, color=color, font_size=size, **kw)


def _display(text, size=48, color=INK, bold=False):
    kw = {"weight": "BOLD"} if bold else {}
    return Text(text, font=DISPLAY, color=color, font_size=size, **kw)


def _appeal_block(label, gloss, accent=TEAL):
    """One appeal: chip + one-line serif gloss below."""
    ch = _chip(label, accent=accent, size=24)
    gl = _serif(gloss, size=22, color=INK)
    gl.next_to(ch, DOWN, buff=0.18)
    return VGroup(ch, gl)


# ---------------------------------------------------------------- scenes

class B02_Title(Scene):
    """Title card with the film's question."""
    def construct(self):
        total = DUR["B02"]
        eye = _chip("WRITING", accent=SLATE, size=22)
        q = _display("Why does powerful persuasion", size=46, bold=True)
        q2 = _display("feel inevitable?", size=46, bold=True)
        block = VGroup(q, q2).arrange(DOWN, buff=0.15).move_to(UP * 0.2)
        u = Line(q2.get_corner(DL) + DOWN * 0.14,
                 q2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_FirstSentence(Scene):
    """Cold open: sentence 1 appears, LOGOS chip drops in — mystery established."""
    def construct(self):
        total = DUR["B03"]
        # The sentence in display type — split into two lines for readability
        s1a = _serif("We know through painful experience that freedom", size=34)
        s1b = _serif("is never voluntarily given by the oppressor;", size=34)
        s1c = _serif("it must be demanded by the oppressed.", size=34)
        passage = VGroup(s1a, s1b, s1c).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        passage.move_to(UP * 0.6)
        logos_chip = _chip("LOGOS", accent=TEAL, size=26)
        logos_chip.next_to(passage, DOWN, buff=0.55)
        causal_label = SerifLabel("causal claim", accent=TEAL, size=24)
        causal_label.next_to(logos_chip, RIGHT, buff=0.4)
        self.play(FadeIn(passage, shift=UP * 0.2), run_time=1.0)
        self.wait(1.8)
        self.play(FadeIn(logos_chip, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(causal_label, shift=LEFT * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.1))


class B04_PainfulWord(Scene):
    """Cold open: 'painful' highlighted, PATHOS chip joins LOGOS."""
    def construct(self):
        total = DUR["B04"]
        # Same sentence — now with the key phrase highlighted
        s1a = _serif("We know through", size=34)
        s1b_pre = _serif("painful experience", size=34, color=INK)
        s1b_suf = _serif("that freedom", size=34)
        row1 = VGroup(s1a, s1b_pre, s1b_suf).arrange(RIGHT, buff=0.18)
        s2 = _serif("is never voluntarily given by the oppressor;", size=34)
        s3 = _serif("it must be demanded by the oppressed.", size=34)
        passage = VGroup(row1, s2, s3).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        passage.move_to(UP * 0.7)
        # Gold bar will sweep under 'painful experience'
        bar = Rectangle(width=0.1, height=s1b_pre.height + 0.16)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar.align_to(s1b_pre, LEFT).align_to(s1b_pre, DOWN).shift(DOWN * 0.04)
        logos_chip = _chip("LOGOS", accent=TEAL, size=24)
        pathos_chip = _chip("PATHOS", accent=CRIMSON, size=24)
        chips = VGroup(logos_chip, pathos_chip).arrange(RIGHT, buff=0.4)
        chips.move_to(DOWN * 2.4)
        self.add(passage)
        self.play(FadeIn(logos_chip, shift=UP * 0.1), run_time=0.6)
        self.wait(0.6)
        # Gold bar grows to full width (single-method .animate chain only)
        bar_target = Rectangle(width=s1b_pre.width + 0.2, height=s1b_pre.height + 0.16)
        bar_target.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar_target.align_to(s1b_pre, LEFT).align_to(s1b_pre, DOWN).shift(DOWN * 0.04)
        self.add(bar)
        s1b_pre.set_z_index(1)
        self.play(Transform(bar, bar_target), run_time=0.9)
        self.play(FadeIn(pathos_chip, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 2.8))


class B05_QuestionCard(Scene):
    """THE QUESTION section card."""
    def construct(self):
        total = DUR["B05"]
        kicker = _chip("THE QUESTION", accent=SLATE, size=22)
        q = _display("Why does one sentence", size=44, bold=True)
        q2 = _display("carry three things?", size=44, bold=True)
        block = VGroup(q, q2).arrange(DOWN, buff=0.15)
        kicker.next_to(block, UP, buff=0.65)
        u = Line(q2.get_corner(DL) + DOWN * 0.14,
                 q2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(kicker, shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 1.5))


class B06_FourAppeals(Scene):
    """THE PROBLEM: four appeal chips accumulate with one-line glosses."""
    def construct(self):
        total = DUR["B06"]
        appeals = [
            ("ETHOS", "projected credibility of the speaker", SLATE),
            ("LOGOS", "structure of the argument", TEAL),
            ("PATHOS", "emotional weight the language carries", CRIMSON),
            ("KAIROS", "timeliness — the right argument at the right moment", SLATE),
        ]
        blocks = VGroup(*[_appeal_block(lbl, gloss, acc)
                          for lbl, gloss, acc in appeals])
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        blocks.move_to(ORIGIN)
        # Teal accent bar grows in as shape anchor for Gate A
        accent_bar = Rectangle(width=11.0, height=0.06)
        accent_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        accent_bar.move_to(UP * 3.2)
        # Accumulate one at a time
        self.play(FadeIn(blocks[0], shift=UP * 0.2), run_time=0.8)
        self.play(GrowFromCenter(accent_bar), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(blocks[1], shift=UP * 0.2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeIn(blocks[2], shift=UP * 0.2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeIn(blocks[3], shift=UP * 0.2), run_time=0.7)
        self.wait(max(0.5, total - 4.5))


class B07_NaiveVsReal(Scene):
    """THE PROBLEM: separate (naive) vs overlapping (real) model."""
    def construct(self):
        total = DUR["B07"]
        labels = ["ETHOS", "LOGOS", "PATHOS", "KAIROS"]
        accents = [SLATE, TEAL, CRIMSON, SLATE]

        # NAIVE side: four separate chips stacked
        naive_label = SerifLabel("naive reading", accent=CRIMSON, size=28)
        naive_chips = VGroup(*[_chip(lbl, acc, 22)
                                for lbl, acc in zip(labels, accents)])
        naive_chips.arrange(DOWN, buff=0.3)
        naive_group = VGroup(naive_label, naive_chips)
        naive_group.arrange(DOWN, buff=0.45)
        naive_group.move_to(LEFT * 3.6)

        # ACTUAL side: chips arranged in a tighter cluster (overlapping feel)
        actual_label = SerifLabel("how it actually works", accent=TEAL, size=28)
        actual_chips = VGroup(*[_chip(lbl, acc, 22)
                                 for lbl, acc in zip(labels, accents)])
        # arrange in 2x2 grid — visual overlap
        actual_chips.arrange_in_grid(rows=2, cols=2, buff=(0.25, 0.25))
        actual_group = VGroup(actual_label, actual_chips)
        actual_group.arrange(DOWN, buff=0.45)
        actual_group.move_to(RIGHT * 3.4)

        divider = Line(UP * 2.8, DOWN * 2.8, color=SLATE, stroke_width=1.5)

        self.play(FadeIn(naive_label), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in naive_chips],
                              lag_ratio=0.15, run_time=1.2))
        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(actual_label), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in actual_chips],
                              lag_ratio=0.15, run_time=1.2))
        self.wait(max(0.5, total - 4.1))


class B08_Sentence1Full(Scene):
    """THE MECHANISM: sentence 1 — LOGOS (spine) + ETHOS/PATHOS on 'painful experience'."""
    def construct(self):
        total = DUR["B08"]
        s1a = _serif("We know through", size=30)
        s1b = _serif("painful experience", size=30, color=INK)
        s1c = _serif("that freedom", size=30)
        row1 = VGroup(s1a, s1b, s1c).arrange(RIGHT, buff=0.14)
        s2 = _serif("is never voluntarily given by the oppressor;", size=30)
        s3 = _serif("it must be demanded by the oppressed.", size=30)
        passage = VGroup(row1, s2, s3).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        passage.move_to(UP * 1.1)

        # Gold bar for 'painful experience'
        bar = Rectangle(width=0.1, height=s1b.height + 0.16)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar.align_to(s1b, LEFT).align_to(s1b, DOWN).shift(DOWN * 0.04)
        bar_target = Rectangle(width=s1b.width + 0.2, height=s1b.height + 0.16)
        bar_target.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar_target.align_to(s1b, LEFT).align_to(s1b, DOWN).shift(DOWN * 0.04)

        logos_chip = _chip("LOGOS", accent=TEAL, size=24)
        logos_label = SerifLabel("the argument's spine", accent=TEAL, size=22)
        logos_row = VGroup(logos_chip, logos_label).arrange(RIGHT, buff=0.35)
        logos_row.move_to(DOWN * 1.5 + LEFT * 1.2)

        ethos_chip = _chip("ETHOS", accent=SLATE, size=24)
        pathos_chip = _chip("PATHOS", accent=CRIMSON, size=24)
        overlap_chips = VGroup(ethos_chip, pathos_chip).arrange(RIGHT, buff=0.3)
        overlap_label = SerifLabel("two words, two appeals", accent=SLATE, size=22)
        overlap_row = VGroup(overlap_chips, overlap_label).arrange(RIGHT, buff=0.35)
        overlap_row.move_to(DOWN * 2.45 + LEFT * 0.4)

        self.play(FadeIn(passage, shift=UP * 0.2), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(logos_row, shift=UP * 0.15), run_time=0.8)
        self.wait(1.0)
        # Gold bar grows to full width (single-method .animate via Transform)
        self.add(bar)
        s1b.set_z_index(1)
        self.play(Transform(bar, bar_target), run_time=0.9)
        self.play(FadeIn(overlap_row, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 5.3))


class B09_Sentence2(Scene):
    """THE MECHANISM: sentence 2 — ETHOS (first-person witness) + LOGOS (standing)."""
    def construct(self):
        total = DUR["B09"]
        s2a = _serif("Frankly, I have yet to engage in a", size=29)
        s2b = _serif("direct-action campaign that was", size=29)
        s2c = _serif('"well timed"', size=29)
        s2d = _serif("in the view of", size=29)
        s2e = _serif("those who have not suffered unduly", size=29, color=INK)
        s2f = _serif("from the disease of segregation.", size=29)
        line1 = VGroup(s2a, s2b).arrange(RIGHT, buff=0.14)
        line2 = VGroup(s2c, s2d).arrange(RIGHT, buff=0.14)
        line3 = VGroup(s2e, s2f).arrange(RIGHT, buff=0.14)
        passage = VGroup(line1, line2, line3).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        passage.move_to(UP * 1.0)

        ethos_chip = _chip("ETHOS", accent=SLATE, size=24)
        ethos_label = SerifLabel("first-person witness", accent=SLATE, size=22)
        ethos_row = VGroup(ethos_chip, ethos_label).arrange(RIGHT, buff=0.35)
        ethos_row.move_to(DOWN * 1.5 + LEFT * 1.5)

        logos_chip = _chip("LOGOS", accent=TEAL, size=24)
        logos_label = SerifLabel("who has standing to judge timeliness?", accent=TEAL, size=22)
        logos_row = VGroup(logos_chip, logos_label).arrange(RIGHT, buff=0.35)
        logos_row.move_to(DOWN * 2.4 + LEFT * 0.7)

        # Underline 'those who have not suffered unduly' to anchor LOGOS label
        underline = Line(s2e.get_corner(DL) + DOWN * 0.06,
                         s2e.get_corner(DR) + DOWN * 0.06,
                         color=TEAL, stroke_width=2)

        self.play(FadeIn(passage, shift=UP * 0.2), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(ethos_row, shift=UP * 0.15), run_time=0.8)
        self.wait(0.8)
        self.play(Create(underline), run_time=0.6)
        self.play(FadeIn(logos_row, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 4.7))


class B10_WaitWord(Scene):
    """THE MECHANISM: WAIT isolated, then sentences 3-4 with accumulating PATHOS."""
    def construct(self):
        total = DUR["B10"]
        # WAIT large, isolated
        wait_big = _display("Wait", size=110, color=TEAL, bold=True)
        wait_big.move_to(UP * 0.5)

        # Then sentences 3 and 4
        s3 = _serif("For years now I have heard the word", size=28)
        wait3 = _serif('"Wait!"', size=28, color=TEAL)
        line3 = VGroup(s3, wait3).arrange(RIGHT, buff=0.14)
        s4a = _serif("It rings in the ear of every Negro with", size=28)
        s4b = _serif("piercing familiarity.", size=28, color=INK)
        line4 = VGroup(s4a, s4b).arrange(RIGHT, buff=0.14)
        small_passage = VGroup(line3, line4).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        small_passage.move_to(UP * 0.6)

        pathos_chip = _chip("PATHOS", accent=CRIMSON, size=24)
        pathos_label = SerifLabel("sensory phrase — the word enters the body", accent=CRIMSON, size=22)
        pathos_row = VGroup(pathos_chip, pathos_label).arrange(RIGHT, buff=0.35)
        pathos_row.move_to(DOWN * 1.9 + LEFT * 0.9)

        underline4b = Line(s4b.get_corner(DL) + DOWN * 0.06,
                           s4b.get_corner(DR) + DOWN * 0.06,
                           color=CRIMSON, stroke_width=2)

        self.play(FadeIn(wait_big, scale=0.7), run_time=0.9)
        self.wait(0.8)
        self.play(wait_big.animate.scale(0.0), run_time=0.5)
        self.play(FadeIn(small_passage, shift=UP * 0.15), run_time=0.9)
        self.wait(0.8)
        self.play(Create(underline4b), run_time=0.6)
        self.play(FadeIn(pathos_row, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 5.2))


class B12_FullPassage(Scene):
    """THE IMPLICATION: full five-sentence passage color-coded, all four chips accumulate."""
    def construct(self):
        total = DUR["B12"]
        # Five sentences in smaller text — color by dominant appeal
        sent1 = _serif("We know through painful experience that freedom", size=24, color=TEAL)
        sent1b = _serif("is never voluntarily given by the oppressor;", size=24, color=TEAL)
        sent1c = _serif("it must be demanded by the oppressed.", size=24, color=TEAL)
        sent2 = _serif("Frankly, I have yet to engage in a direct-action", size=24, color=SLATE)
        sent2b = _serif("campaign that was well timed in the view of those", size=24, color=SLATE)
        sent2c = _serif("who have not suffered unduly from segregation.", size=24, color=SLATE)
        sent3 = _serif("For years now I have heard the word", size=24, color=CRIMSON)
        wait3 = _serif('"Wait!"', size=24, color=TEAL)
        line3 = VGroup(sent3, wait3).arrange(RIGHT, buff=0.1)
        sent4 = _serif("It rings in the ear of every Negro with piercing familiarity.", size=24, color=CRIMSON)
        sent5 = _serif('This "Wait" has almost always meant "Never."', size=24, color=INK)

        para = VGroup(
            VGroup(sent1, sent1b, sent1c).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            VGroup(sent2, sent2b, sent2c).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            line3,
            sent4,
            sent5,
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        para.move_to(UP * 0.8)

        # Four chips accumulate at the bottom
        chip_ethos = _chip("ETHOS", accent=SLATE, size=22)
        chip_logos = _chip("LOGOS", accent=TEAL, size=22)
        chip_pathos = _chip("PATHOS", accent=CRIMSON, size=22)
        chip_kairos = _chip("KAIROS", accent=SLATE, size=22)
        all_chips = VGroup(chip_ethos, chip_logos, chip_pathos, chip_kairos)
        all_chips.arrange(RIGHT, buff=0.3).move_to(DOWN * 3.1)

        # Accent bar grows in above chip row — real shape motion for Gate A
        accent_bar = Rectangle(width=11.0, height=0.06)
        accent_bar.set_fill(SLATE, 0.3).set_stroke(width=0, opacity=0)
        accent_bar.move_to(DOWN * 2.6)
        self.play(FadeIn(para, shift=UP * 0.2), run_time=1.2)
        self.wait(1.0)
        self.play(GrowFromCenter(accent_bar), run_time=0.4)
        self.play(FadeIn(chip_logos, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(chip_ethos, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(chip_pathos, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(chip_kairos, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 4.6))


class B13_ImplicationCard(Scene):
    """THE IMPLICATION section card: the machinery does not break the spell."""
    def construct(self):
        total = DUR["B13"]
        kicker = _chip("THE IMPLICATION", accent=SLATE, size=22)
        line1 = _display("The machinery does not", size=44, bold=True)
        line2 = _display("break the spell.", size=44, bold=True)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.15)
        sub = _serif("it shows why the spell is earned", size=28, color=SLATE)
        kicker.next_to(block, UP, buff=0.65)
        sub.next_to(block, DOWN, buff=0.45)
        u = Line(block.get_corner(DL) + DOWN * 0.14,
                 block.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(kicker, shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.1))


class B14_Example(Scene):
    """THE EXAMPLE: made-up 'Maria' sentence, four appeals labeled as they accumulate."""
    def construct(self):
        total = DUR["B14"]
        # Eyebrow
        eye = _chip("ILLUSTRATIVE EXAMPLE", accent=SLATE, size=20)
        eye.to_corner(UL, buff=0.6)

        # The made-up sentence — split across lines
        line1 = _serif("After twenty years of working the same shift,", size=28)
        line2 = _serif("Maria knows —", size=28)
        line3 = _serif("the safety board's definition of acceptable risk", size=28)
        line4 = _serif("has never been written by someone who breathes this air.", size=28)
        sentence = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        sentence.move_to(UP * 0.6)

        # Four appeal chips appear clause by clause
        logos_chip = _chip("LOGOS", accent=TEAL, size=22)
        logos_lbl = _serif("who writes policy", size=20, color=INK)
        logos_row = VGroup(logos_chip, logos_lbl).arrange(RIGHT, buff=0.25)

        ethos_chip = _chip("ETHOS", accent=SLATE, size=22)
        ethos_lbl = _serif("twenty years — the witness", size=20, color=INK)
        ethos_row = VGroup(ethos_chip, ethos_lbl).arrange(RIGHT, buff=0.25)

        pathos_chip = _chip("PATHOS", accent=CRIMSON, size=22)
        pathos_lbl = _serif("breathes this air", size=20, color=INK)
        pathos_row = VGroup(pathos_chip, pathos_lbl).arrange(RIGHT, buff=0.25)

        kairos_chip = _chip("KAIROS", accent=SLATE, size=22)
        kairos_lbl = _serif("implied — the rule is still in force", size=20, color=INK)
        kairos_row = VGroup(kairos_chip, kairos_lbl).arrange(RIGHT, buff=0.25)

        chip_col = VGroup(logos_row, ethos_row, pathos_row, kairos_row)
        chip_col.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        chip_col.move_to(DOWN * 2.4 + LEFT * 0.5)

        # Accent bar grows in below sentence — real shape motion for Gate A
        accent_bar = Rectangle(width=11.0, height=0.06)
        accent_bar.set_fill(SLATE, 0.3).set_stroke(width=0, opacity=0)
        accent_bar.move_to(DOWN * 0.6)
        self.play(FadeIn(eye), run_time=0.4)
        self.play(FadeIn(sentence, shift=UP * 0.15), run_time=1.0)
        self.play(GrowFromCenter(accent_bar), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(logos_row, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(ethos_row, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(pathos_row, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(kairos_row, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.9))


class B15_Practice(Scene):
    """THE PRACTICE: four questions accumulate as the heuristic."""
    def construct(self):
        total = DUR["B15"]
        kicker = _chip("THE PRACTICE", accent=TEAL, size=22)
        kicker.to_corner(UL, buff=0.6)

        prompt = _serif("When a persuasive sentence lands — stop. Ask:", size=30)
        prompt.move_to(UP * 2.0)

        q1 = _serif("1. What is the logical claim?", size=28)
        lbl1 = _chip("LOGOS", accent=TEAL, size=20)
        row1 = VGroup(q1, lbl1).arrange(RIGHT, buff=0.4)

        q2 = _serif("2. Who is claiming standing to make it?", size=28)
        lbl2 = _chip("ETHOS", accent=SLATE, size=20)
        row2 = VGroup(q2, lbl2).arrange(RIGHT, buff=0.4)

        q3 = _serif("3. What does the word choice make you feel?", size=28)
        lbl3 = _chip("PATHOS", accent=CRIMSON, size=20)
        row3 = VGroup(q3, lbl3).arrange(RIGHT, buff=0.4)

        q4 = _serif("4. Why does this argument exist right now, for this audience?", size=28)
        lbl4 = _chip("KAIROS", accent=SLATE, size=20)
        row4 = VGroup(q4, lbl4).arrange(RIGHT, buff=0.4)

        questions = VGroup(row1, row2, row3, row4)
        questions.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        questions.move_to(DOWN * 0.4)

        # Accent bar grows in below prompt — real shape motion for Gate A
        accent_bar = Rectangle(width=11.0, height=0.06)
        accent_bar.set_fill(TEAL, 0.5).set_stroke(width=0, opacity=0)
        accent_bar.move_to(UP * 1.45)
        self.play(FadeIn(kicker), run_time=0.4)
        self.play(FadeIn(prompt, shift=DOWN * 0.1), run_time=0.7)
        self.play(GrowFromCenter(accent_bar), run_time=0.4)
        self.play(FadeIn(row1, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(row2, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(row3, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(row4, shift=UP * 0.12), run_time=0.6)
        self.wait(max(0.5, total - 3.9))


class B16_End(Scene):
    """RECAP endcard — question answered, topic kicker."""
    def construct(self):
        total = DUR["B16"]
        eye = _chip("WRITING", accent=SLATE, size=22)
        q = _display("Why does powerful persuasion", size=40, bold=True)
        q2 = _display("feel inevitable?", size=40, bold=True)
        div = Line(LEFT * 4.5, RIGHT * 4.5, color=TEAL, stroke_width=1.5)
        ans = _serif("Every word is doing more than one thing.", size=32)
        eye.to_corner(UL, buff=0.6)
        block_q = VGroup(q, q2).arrange(DOWN, buff=0.12).move_to(UP * 0.8)
        div.next_to(block_q, DOWN, buff=0.4)
        ans.next_to(div, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.4)
        self.play(FadeIn(block_q, shift=DOWN * 0.1), run_time=0.8)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(ans, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.4))
