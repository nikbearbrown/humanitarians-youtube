"""vox_scenes.py — The Seam Where Fluency Sneaks Back In
(vox-fluency-seam, slate cut, 16:9)

One Scene per GRAPHIC/CARD/COMPOSITE beat whose source is own.
B04 is the only STILL (ai media slot) and has no scene here.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law:
  TEAL #1F6F5C = verified data claim / traceable / counting
  CRIMSON #BF3339 = model judgment / unsourced / fluent fabrication
  GOLD = editor's pen, once (B07 only — fill only, never text)
  Never swap mid-film.

Exclusions honored: no pipeline architecture, no caching, no three-pipeline detail.
Only the seam at the reading layer.
"""
import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)

_bs = str(pathlib.Path(__file__).with_name("beat_sheet.json"))
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- B01_Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The Seam Where Fluency", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Sneaks Back In", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL)+DOWN*0.13, t2.get_corner(DR)+DOWN*0.13, color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B02_ModelOutput

class B02_ModelOutput(Scene):
    """Five sentences appear in sequence, all ink — no color yet.
    The seam is invisible before the reveal. Real shape motion: a
    bracket bar on the left slides downward as each sentence lands."""
    def construct(self):
        total = DUR["B02"]
        sentences = [
            "Acme Bio filed 15 LCAs over the past three years.",
            "Their H-1B approval rate is 85% (source: DOL/USCIS).",
            "This is a strong sponsorship signal for a company of this size.",
            "They are very likely to sponsor your visa for a research role.",
            "Given their funding, they would be a great culture fit.",
        ]
        items = VGroup()
        for s in sentences:
            t = Text(s, font=SERIF, color=INK, font_size=22)
            if t.width > 11.0:
                t.scale_to_fit_width(11.0)
            items.add(t)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        items.move_to(DOWN * 0.1)

        # left bracket bar — real shape that shifts downward (shape motion)
        bar = Line(items[0].get_top() + LEFT * 0.35,
                   items[0].get_bottom() + LEFT * 0.35,
                   color=SLATE, stroke_width=3)

        eye = Text("model output", font=DISPLAY, color=SLATE, font_size=16)
        eye.to_corner(UL, buff=0.6)
        self.play(FadeIn(eye), FadeIn(bar), run_time=0.4)

        reveal_time = (total - 0.4 - 0.5) / len(sentences)
        for i, item in enumerate(items):
            new_bottom = item.get_bottom() + LEFT * 0.35
            self.play(
                FadeIn(item, shift=UP * 0.18),
                bar.animate.put_start_and_end_on(bar.get_start(), new_bottom),
                run_time=max(0.5, reveal_time)
            )
        self.wait(0.5)


# ---------------------------------------------------------------- B03_QuestionCard

class B03_QuestionCard(Scene):
    """THE QUESTION beat — the film's one question, on screen."""
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Where does a real number end", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        q2 = Text("and a fabricated conclusion begin?", font=DISPLAY, color=CRIMSON,
                  font_size=28, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(UP * 0.1)
        u = Line(q2.get_corner(DL)+DOWN*0.12, q2.get_corner(DR)+DOWN*0.12,
                 color=CRIMSON, stroke_width=2)
        chip = LabelChip("The Question", accent=SLATE, size=22)
        chip.next_to(block, UP, buff=0.55)
        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.7))


# ---------------------------------------------------------------- B05_SeamInvisible

class B05_SeamInvisible(Scene):
    """The paragraph reappears; a vertical dashed seam is drawn between
    sentence 2 and 3. Left labeled DATA, right labeled JUDGMENT.
    Real shape motion: the seam line is Created, labels fade in."""
    def construct(self):
        total = DUR["B05"]
        sentences = [
            "Acme Bio filed 15 LCAs over the past three years.",
            "Their H-1B approval rate is 85% (source: DOL/USCIS).",
            "This is a strong sponsorship signal for a company of this size.",
            "They are very likely to sponsor your visa.",
            "They would be a great culture fit.",
        ]
        items = VGroup()
        for s in sentences:
            t = Text(s, font=SERIF, color=INK, font_size=20)
            if t.width > 11.4:
                t.scale_to_fit_width(11.4)
            items.add(t)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        items.move_to(LEFT * 0.3 + DOWN * 0.1)

        self.play(FadeIn(items), run_time=0.8)

        # seam: vertical dashed line between sentence 2 and 3
        seam_y = (items[1].get_bottom()[1] + items[2].get_top()[1]) / 2
        seam_x_left = items.get_left()[0] - 0.3
        seam_x_right = items.get_right()[0] + 0.3
        seam = DashedLine(
            start=[seam_x_left, seam_y, 0],
            end=[seam_x_right, seam_y, 0],
            color=SLATE, stroke_width=2.5, dash_length=0.18
        )
        self.play(Create(seam), run_time=0.9)

        data_label = LabelChip("DATA", accent=TEAL, size=20)
        data_label.next_to(seam, LEFT, buff=0.3).shift(UP * 0.22)
        judg_label = LabelChip("JUDGMENT", accent=CRIMSON, size=20)
        judg_label.next_to(seam, RIGHT, buff=0.3).shift(DOWN * 0.22)

        seam_note = SerifLabel("the seam is invisible", SLATE, size=22)
        seam_note.next_to(seam, DOWN, buff=0.35)

        self.play(FadeIn(data_label), FadeIn(judg_label), run_time=0.7)
        self.play(FadeIn(seam_note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ---------------------------------------------------------------- B06_DecisionTree

class B06_DecisionTree(Scene):
    """The one-question decision tree — SPLIT move.
    Question node at top splits into TEAL (data claim) and CRIMSON (model judgment)
    branches, both converging at a label-visibility check at bottom."""
    def construct(self):
        total = DUR["B06"]

        # --- question node at top
        q_text = Text("Could this sentence have been", font=SERIF, color=INK, font_size=22)
        q_text2 = Text("produced by counting records?", font=SERIF, color=INK, font_size=22)
        q_block = VGroup(q_text, q_text2).arrange(DOWN, buff=0.1)
        q_box = SurroundingRectangle(q_block, buff=0.22, color=SLATE, stroke_width=2.5)
        q_box.set_fill(SLATE, 0.12)
        q_group = VGroup(q_box, q_block).move_to(UP * 2.8)

        # --- YES branch (left, TEAL)
        yes_chip = LabelChip("YES", accent=TEAL, size=24)
        yes_chip.move_to(LEFT * 3.2 + UP * 0.9)

        yes_label = Text("Data claim:", font=SERIF, color=TEAL, font_size=20, weight=BOLD)
        yes_sub = Text("trace to script or audit", font=SERIF, color=TEAL, font_size=18)
        yes_block = VGroup(yes_label, yes_sub).arrange(DOWN, buff=0.1)
        yes_box = SurroundingRectangle(yes_block, buff=0.18, color=TEAL, stroke_width=2)
        yes_box.set_fill(TEAL, 0.08)
        yes_group = VGroup(yes_box, yes_block).move_to(LEFT * 3.4 + DOWN * 0.2)

        # --- NO branch (right, CRIMSON)
        no_chip = LabelChip("NO", accent=CRIMSON, size=24)
        no_chip.move_to(RIGHT * 3.2 + UP * 0.9)

        no_label = Text("Model judgment:", font=SERIF, color=CRIMSON, font_size=20, weight=BOLD)
        no_sub = Text("allowed, but must be labeled", font=SERIF, color=CRIMSON, font_size=18)
        no_block = VGroup(no_label, no_sub).arrange(DOWN, buff=0.1)
        no_box = SurroundingRectangle(no_block, buff=0.18, color=CRIMSON, stroke_width=2)
        no_box.set_fill(CRIMSON, 0.08)
        no_group = VGroup(no_box, no_block).move_to(RIGHT * 3.4 + DOWN * 0.2)

        # --- convergence node at bottom
        conv_text = Text("Is the label visible in the output?", font=SERIF, color=INK, font_size=20)
        conv_box = SurroundingRectangle(conv_text, buff=0.18, color=SLATE, stroke_width=2)
        conv_box.set_fill(SLATE, 0.12)
        conv_group = VGroup(conv_box, conv_text).move_to(DOWN * 2.4)

        # --- lines
        line_q_yes = Line(q_group.get_bottom(), yes_chip.get_top(), color=TEAL, stroke_width=2)
        line_q_no = Line(q_group.get_bottom(), no_chip.get_top(), color=CRIMSON, stroke_width=2)
        line_yes_down = Line(yes_group.get_bottom(), conv_group.get_top()+LEFT*1.5, color=TEAL, stroke_width=2)
        line_no_down = Line(no_group.get_bottom(), conv_group.get_top()+RIGHT*1.5, color=CRIMSON, stroke_width=2)

        # animate: question first, then split
        self.play(FadeIn(q_group), run_time=0.8)
        self.play(
            Create(line_q_yes), FadeIn(yes_chip),
            Create(line_q_no), FadeIn(no_chip),
            run_time=0.9
        )
        self.play(
            FadeIn(yes_group, shift=DOWN * 0.2),
            FadeIn(no_group, shift=DOWN * 0.2),
            run_time=0.9
        )
        self.play(
            Create(line_yes_down), Create(line_no_down),
            run_time=0.7
        )
        self.play(FadeIn(conv_group, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.3, total - 4.0))


# ---------------------------------------------------------------- B07_AuthorityBorrow

class B07_AuthorityBorrow(Scene):
    """TEAL verified-number block -> gold highlight -> crimson judgment chain.
    The editor's pen (gold highlight bar) appears under the verified number,
    then the judgment chain grows to the right."""
    def construct(self):
        total = DUR["B07"]

        # verified block
        verified_label = Text("15 filings", font=MONO, color=TEAL, font_size=36, weight=BOLD)
        verified_sub = Text("source: DOL records", font=SERIF, color=TEAL, font_size=18)
        verified_block = VGroup(verified_label, verified_sub).arrange(DOWN, buff=0.1)
        v_box = SurroundingRectangle(verified_block, buff=0.2, color=TEAL, stroke_width=2.5)
        v_box.set_fill(TEAL, 0.1)
        v_group = VGroup(v_box, verified_block).move_to(LEFT * 4.4 + UP * 0.1)

        # gold highlight bar (editor's pen — fill only, once)
        gold_bar = Rectangle(width=0.1, height=verified_label.height + 0.16)
        gold_bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        gold_bar.align_to(verified_label, LEFT).align_to(verified_label, DOWN).shift(DOWN * 0.04)

        # judgment chain (3 crimson LabelChips — white text inside accent box)
        judgments = ["strong signal", "very likely", "great fit"]
        j_boxes = VGroup()
        for j in judgments:
            j_boxes.add(LabelChip(j, accent=CRIMSON, size=20))
        j_boxes.arrange(RIGHT, buff=0.25).move_to(RIGHT * 2.0 + UP * 0.1)

        # arrow from verified to chain
        arrow = Arrow(
            v_group.get_right() + RIGHT * 0.1,
            j_boxes.get_left() + LEFT * 0.1,
            color=INK, stroke_width=2.5, buff=0.1
        )

        # source label below
        src_note = SerifLabel("trust earned here", TEAL, size=20)
        src_note.next_to(v_group, DOWN, buff=0.35)
        spent_note = SerifLabel("spent on estimation", CRIMSON, size=20)
        spent_note.next_to(j_boxes, DOWN, buff=0.35)

        self.play(FadeIn(v_group), run_time=0.7)
        # gold bar sweeps (single-method .animate — stretch only; bar starts left-aligned)
        gold_bar.align_to(verified_label, LEFT).shift(DOWN * 0.04)
        self.add(gold_bar)
        verified_label.set_z_index(1)
        self.play(gold_bar.animate.stretch_to_fit_width(verified_label.width + 0.18),
                  run_time=0.8)
        self.play(FadeIn(src_note, shift=UP * 0.1), run_time=0.5)
        self.play(Create(arrow), run_time=0.6)
        self.play(
            LaggedStart(*[FadeIn(jb, shift=RIGHT * 0.15) for jb in j_boxes], lag_ratio=0.2),
            run_time=1.0
        )
        self.play(FadeIn(spent_note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 4.1))


# ---------------------------------------------------------------- B08_ColorCodedParagraph

class B08_ColorCodedParagraph(Scene):
    """Color-coded paragraph: 2 teal (data claims) + 3 crimson (model judgments).
    Sentences appear in ink; each is colored and annotated. A tally bar grows
    on the right side as sentences are labeled (real shape motion)."""
    def construct(self):
        total = DUR["B08"]

        display_sentences = [
            "Acme Bio filed 15 LCAs.",
            "An 85% approval rate (source: DOL/USCIS).",
            "This is a strong signal for a company of this size.",
            "Very likely to sponsor.",
            "Great culture fit.",
        ]
        colors = [TEAL, TEAL, CRIMSON, CRIMSON, CRIMSON]
        labels = ["DATA CLAIM", "DATA CLAIM", "MODEL JUDGMENT", "UNSOURCED CLAIM", "FABRICATED"]
        accents = [TEAL, TEAL, CRIMSON, CRIMSON, CRIMSON]

        items = VGroup()
        for s in display_sentences:
            t = Text(s, font=SERIF, color=INK, font_size=21)
            if t.width > 9.2:
                t.scale_to_fit_width(9.2)
            items.add(t)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.31)
        items.move_to(LEFT * 1.5 + DOWN * 0.1)

        # tally bar (real shape — grows rightward as labels land)
        tally_bar = Rectangle(width=0.12, height=0.36)
        tally_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        tally_bar.move_to(RIGHT * 6.0 + UP * 2.5)

        eye = Text("model output", font=DISPLAY, color=SLATE, font_size=15)
        eye.to_corner(UL, buff=0.5)
        self.play(FadeIn(eye), FadeIn(items), FadeIn(tally_bar), run_time=0.8)
        self.wait(0.4)

        for i, (item, color, label, accent) in enumerate(zip(items, colors, labels, accents)):
            chip = LabelChip(label, accent=accent, size=17)
            chip.next_to(item, RIGHT, buff=0.22)
            if chip.get_right()[0] > 6.8:
                chip.shift(LEFT * (chip.get_right()[0] - 6.8))
            new_w = 0.12 + (i + 1) * 0.5
            new_color = TEAL if accent == TEAL else CRIMSON
            self.play(
                item.animate.set_color(color),
                FadeIn(chip, shift=LEFT * 0.1),
                tally_bar.animate.stretch_to_fit_width(new_w),
                run_time=0.75
            )
            tally_bar.set_fill(new_color, 1)
            self.wait(0.25)

        # final summary
        count_teal = Text("2 data claims", font=SERIF, color=TEAL, font_size=20, weight=BOLD)
        count_crimson = Text("3 model judgments", font=SERIF, color=CRIMSON, font_size=20, weight=BOLD)
        count_note = Text("same paragraph", font=SERIF, color=SLATE, font_size=18)
        summary = VGroup(count_teal, count_crimson, count_note).arrange(DOWN, buff=0.15)
        summary.to_corner(DR, buff=0.6).shift(UP * 0.4)
        self.play(FadeIn(summary, shift=LEFT * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 0.8 - 0.4 - len(items) * 1.0 - 0.7))


# ---------------------------------------------------------------- B09_End

class B09_End(Scene):
    """RECAP endcard — question answered in one line."""
    def construct(self):
        total = DUR["B09"]
        t1 = Text("A real number can launch", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("a fabricated conclusion.", font=DISPLAY, color=CRIMSON,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.4)
        u = Line(t2.get_corner(DL)+DOWN*0.12, t2.get_corner(DR)+DOWN*0.12,
                 color=CRIMSON, stroke_width=2)
        sub = Text("Apply the one-question test to every sentence.", font=SERIF,
                   color=INK, font_size=22)
        sub.next_to(u, DOWN, buff=0.45)
        topic = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        topic.next_to(sub, DOWN, buff=0.55)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(topic), run_time=0.5)
        self.wait(max(0.3, total - 2.6))
