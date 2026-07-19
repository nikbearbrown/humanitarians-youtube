import sys, json, os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ─────────────────────────────────────────────────────────────────────────────
# B01 — TITLE CARD
# ─────────────────────────────────────────────────────────────────────────────
class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Only 0.7% of a Cancer", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("Nanoparticle Reaches the Tumor", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─────────────────────────────────────────────────────────────────────────────
# B03 — QUESTION CARD
# ─────────────────────────────────────────────────────────────────────────────
class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        # Slate card — white text on SLATE is AA (6.70:1)
        card = Rectangle(width=12.8, height=5.8)
        card.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        card.move_to(ORIGIN)

        q_line1 = Text("A tumor-targeted nanoparticle is injected.", font=SERIF,
                        color=WHITE, font_size=27)
        # GOLD highlight bar behind the key line — text stays INK/WHITE (not GOLD text)
        q_line2 = Text("Only 0.7% reaches the tumor.", font=SERIF,
                        color=INK, font_size=27)
        gold_bar = Rectangle(width=q_line2.width + 0.28, height=q_line2.height + 0.18)
        gold_bar.set_fill(GOLD, 1).set_stroke(width=0, opacity=0)
        gold_bar.move_to(q_line2)
        q_line2.set_z_index(1)
        q_line3 = Text("The targeting ligand is working.", font=SERIF,
                        color=WHITE, font_size=27)
        q_line4 = Text("So why does so little arrive?", font=SERIF,
                        color=WHITE, font_size=30, weight=BOLD)

        qblock = VGroup(q_line1, q_line2, q_line3, q_line4).arrange(DOWN, buff=0.32)
        qblock.move_to(card)
        # Re-position gold bar after layout
        gold_bar.move_to(q_line2)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(q_line1, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(gold_bar), FadeIn(q_line2, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(q_line3, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(q_line4, shift=UP * 0.12), run_time=0.7)
        self.wait(max(0.3, total - 2.5 - 0.5))


# ─────────────────────────────────────────────────────────────────────────────
# B04 — FIVE STEPS CHAIN
# ─────────────────────────────────────────────────────────────────────────────
class B04_FiveSteps(Scene):
    def construct(self):
        total = DUR["B04"]

        title = Text("Five steps between the syringe and the tumor cell",
                     font=SERIF, color=INK, font_size=26)
        title.to_edge(UP, buff=0.55)

        steps = [
            "1. Survive\ncirculation",
            "2. Escape\nthe vessel",
            "3. Penetrate\ntissue",
            "4. Cell\nuptake",
            "5. Release\npayload",
        ]

        chips = VGroup()
        for label in steps:
            box = Rectangle(width=1.7, height=1.1)
            box.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            txt = Text(label, font=DISPLAY, color=WHITE, font_size=15,
                       weight="MEDIUM")
            txt.move_to(box)
            chips.add(VGroup(box, txt))

        chips.arrange(RIGHT, buff=0.28).move_to(DOWN * 0.2)

        # Dose bar on the left showing "injected dose"
        dose_bar = Rectangle(width=0.45, height=1.1)
        dose_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        dose_bar_label = Text("Injected\ndose", font=DISPLAY, color=TEAL,
                               font_size=13, weight="MEDIUM")
        dose_group = VGroup(dose_bar, dose_bar_label).arrange(DOWN, buff=0.15)
        dose_group.next_to(chips, LEFT, buff=0.45)

        # Arrow from dose to first step
        arr = Arrow(
            dose_bar.get_right(),
            chips[0].get_left(),
            buff=0.05,
            color=TEAL,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2,
        )

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.6)
        self.play(GrowFromCenter(dose_bar), FadeIn(dose_bar_label), run_time=0.7)
        self.play(GrowArrow(arr), run_time=0.4)

        for chip in chips:
            self.play(FadeIn(chip, scale=0.9), run_time=0.5)

        self.wait(max(0.3, total - 0.6 - 0.7 - 0.4 - len(chips) * 0.5))


# ─────────────────────────────────────────────────────────────────────────────
# B05 — DRAIN 1: CIRCULATION LOSS
# ─────────────────────────────────────────────────────────────────────────────
class B05_Drain1(Scene):
    def construct(self):
        total = DUR["B05"]

        title = Text("Step 1 -- Circulation loss", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.55)

        full_width = 9.0
        bar_height = 1.2
        bar_y = 0.3

        # Anchor the left edge x so we can build the remain bar beside it
        left_x = -full_width / 2.0 - 0.5

        full_bar = Rectangle(width=full_width, height=bar_height)
        full_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        full_bar.move_to([left_x + full_width / 2.0, bar_y, 0])

        dose_label = Text("Injected dose (100%)", font=DISPLAY, color=TEAL,
                           font_size=18, weight="MEDIUM")
        dose_label.next_to(full_bar, UP, buff=0.22)

        loss_chip = LabelChip("Cleared by liver / spleen", accent=CRIMSON, size=20)
        loss_chip.next_to(full_bar, DOWN, buff=0.55)

        # Remain bar — same left anchor, shorter width
        remain_fraction = 0.64
        remain_width = full_width * remain_fraction
        remain_bar = Rectangle(width=remain_width, height=bar_height)
        remain_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        remain_bar.move_to([left_x + remain_width / 2.0, bar_y, 0])

        remain_label = Text("Surviving: ~64%", font=DISPLAY, color=TEAL,
                             font_size=18, weight="MEDIUM")
        remain_label.next_to(remain_bar, UP, buff=0.22)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowFromCenter(full_bar), FadeIn(dose_label), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(loss_chip, shift=UP * 0.1), run_time=0.5)
        self.wait(0.4)
        # Drain: replace full bar with remain bar (single Transform — no chained animate)
        self.play(Transform(full_bar, remain_bar), Transform(dose_label, remain_label),
                  run_time=1.5)
        self.wait(max(0.3, total - 0.5 - 0.7 - 0.3 - 0.5 - 0.4 - 1.5))


# ─────────────────────────────────────────────────────────────────────────────
# B06 — DRAIN 2: EXTRAVASATION LOSS (COMPOSITE)
# ─────────────────────────────────────────────────────────────────────────────
class B06_Drain2(Scene):
    def construct(self):
        total = DUR["B06"]

        title = Text("Step 2 -- Escape the vessel", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.55)

        full_width = 9.0
        bar_height = 1.2
        bar_y = 0.3
        left_x = -full_width / 2.0 - 0.5

        step1_fraction = 0.64
        step2_fraction = 0.50
        step1_width = full_width * step1_fraction
        step2_width = full_width * step2_fraction

        carry_bar = Rectangle(width=step1_width, height=bar_height)
        carry_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        carry_bar.move_to([left_x + step1_width / 2.0, bar_y, 0])

        carry_label = Text("Surviving circulation: ~64%", font=DISPLAY, color=TEAL,
                            font_size=18, weight="MEDIUM")
        carry_label.next_to(carry_bar, UP, buff=0.22)

        loss_chip = LabelChip("Fails to extravasate", accent=CRIMSON, size=20)
        loss_chip.next_to(carry_bar, DOWN, buff=0.55)

        # Remain bar — same left anchor, shorter
        remain_bar = Rectangle(width=step2_width, height=bar_height)
        remain_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        remain_bar.move_to([left_x + step2_width / 2.0, bar_y, 0])

        remain_label = Text("Still in play: ~50%", font=DISPLAY, color=TEAL,
                             font_size=18, weight="MEDIUM")
        remain_label.next_to(remain_bar, UP, buff=0.22)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowFromCenter(carry_bar), FadeIn(carry_label), run_time=0.7)
        self.play(FadeIn(loss_chip, shift=UP * 0.1), run_time=0.5)
        self.wait(0.4)
        # Drain: Transform to remain bar (single method, no chained animate)
        self.play(Transform(carry_bar, remain_bar), Transform(carry_label, remain_label),
                  run_time=1.5)
        self.wait(max(0.3, total - 0.5 - 0.7 - 0.5 - 0.4 - 1.5))


# ─────────────────────────────────────────────────────────────────────────────
# B07 — DRAIN 3-4-5: RESOLVE TO 0.7%
# ─────────────────────────────────────────────────────────────────────────────
class B07_Drain345(Scene):
    def construct(self):
        total = DUR["B07"]

        title = Text("Steps 3 - 4 - 5: penetrate, uptake, release",
                     font=SERIF, color=INK, font_size=26)
        title.to_edge(UP, buff=0.55)

        full_width = 9.0
        bar_height = 1.1
        bar_y = 0.7

        # Start from step 2 remainder
        carry_width = full_width * 0.50
        carry_bar = Rectangle(width=carry_width, height=bar_height)
        carry_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        carry_bar.to_edge(LEFT, buff=0.7).shift(UP * bar_y)

        step_labels = [
            ("3. Tissue penetration", 0.22),
            ("4. Cell uptake", 0.08),
            ("5. Payload release", 0.014),
        ]
        fractions = [s[1] for s in step_labels]

        loss_chips = VGroup()
        for step_text, _ in step_labels:
            chip = LabelChip(step_text, accent=CRIMSON, size=18)
            loss_chips.add(chip)
        loss_chips.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        loss_chips.next_to(carry_bar, DOWN, buff=0.45)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowFromCenter(carry_bar), run_time=0.6)

        left_x = -full_width / 2.0 - 0.5

        for i, fraction in enumerate(fractions):
            new_width = max(full_width * fraction, 0.07)
            next_bar = Rectangle(width=new_width, height=bar_height)
            next_bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            next_bar.move_to([left_x + new_width / 2.0, bar_y, 0])
            self.play(FadeIn(loss_chips[i], shift=UP * 0.1), run_time=0.4)
            # Single Transform — no chained .animate
            self.play(Transform(carry_bar, next_bar), run_time=0.9)

        # Gold label on the 0.7% sliver
        gold_label = Text("0.7%", font=MONO, color=INK, font_size=32, weight=BOLD)
        gold_box = SurroundingRectangle(gold_label, buff=0.18)
        gold_box.set_fill(GOLD, 1).set_stroke(width=0, opacity=0)
        gold_group = VGroup(gold_box, gold_label)
        gold_group.next_to(carry_bar, UP, buff=0.25)

        self.play(FadeIn(gold_box), FadeIn(gold_label), run_time=0.7)
        self.wait(max(0.3, total - 0.5 - 0.6 - len(step_labels) * 1.3 - 0.7))


# ─────────────────────────────────────────────────────────────────────────────
# B08 — TARGETING FIX ANNOTATION
# ─────────────────────────────────────────────────────────────────────────────
class B08_TargetingFix(Scene):
    def construct(self):
        total = DUR["B08"]

        title = Text("Targeting only helps at one step", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.55)

        steps = ["1", "2", "3", "4", "5"]
        step_boxes = VGroup()
        for s in steps:
            box = Square(0.85)
            box.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            num = Text(s, font=DISPLAY, color=WHITE, font_size=22, weight=BOLD)
            num.move_to(box)
            step_boxes.add(VGroup(box, num))

        step_boxes.arrange(RIGHT, buff=0.35).move_to(UP * 0.35)

        # Step 4 highlighted teal (targeting helps here)
        step4_box = Square(0.85)
        step4_box.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        step4_num = Text("4", font=DISPLAY, color=WHITE, font_size=22, weight=BOLD)
        step4_num.move_to(step4_box)
        step4_group = VGroup(step4_box, step4_num)
        step4_group.move_to(step_boxes[3])

        # Targeting label under step 4
        targeting_label = SerifLabel("targeting ligand helps here", accent=TEAL, size=22)
        targeting_label.next_to(step4_group, DOWN, buff=0.38)

        # "Still lost" label under steps 1-3
        lost_label = SerifLabel("still lost at earlier steps", accent=CRIMSON, size=22)
        lost_label.next_to(step_boxes[1], DOWN, buff=0.38)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in step_boxes],
                              lag_ratio=0.12, run_time=1.2))
        self.wait(0.4)
        # Highlight step 4 as TEAL
        self.play(Transform(step_boxes[3], step4_group), run_time=0.7)
        self.play(FadeIn(targeting_label, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(lost_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 0.5 - 1.2 - 0.4 - 0.7 - 0.5 - 0.5))


# ─────────────────────────────────────────────────────────────────────────────
# B09 — QUOTE CARD
# ─────────────────────────────────────────────────────────────────────────────
class B09_Quote(Scene):
    def construct(self):
        total = DUR["B09"]
        q1 = Text("Most of what is injected does not arrive.", font=SERIF,
                   color=INK, font_size=32)
        q2 = Text("Adding a targeting ligand to a particle that", font=SERIF,
                   color=INK, font_size=32)
        q3 = Text("fails at step one does not solve the problem.", font=SERIF,
                   color=INK, font_size=32)
        att = Text("-- Cancer Nanomedicine, Chapter 1", font=SERIF,
                   color=INK, font_size=24)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.22)
        block.move_to(UP * 0.5)
        att.next_to(block, DOWN, buff=0.55)
        # Gold bar highlight behind "does not arrive"
        bar = Rectangle(width=q1.width + 0.2, height=q1.height + 0.14)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar.align_to(q1, LEFT).align_to(q1, DOWN).shift(DOWN * 0.05)
        q1.set_z_index(1)
        self.play(FadeIn(q1), FadeIn(q2), FadeIn(q3), run_time=1.0)
        self.play(FadeIn(att, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(bar), run_time=0.6)
        self.wait(max(0.3, total - 1.0 - 0.6 - 0.6))


# ─────────────────────────────────────────────────────────────────────────────
# B10 — EXAMPLE: 100-UNIT TRACKING
# ─────────────────────────────────────────────────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = DUR["B10"]

        # Left column — lost dose
        left_header = LabelChip("99.3% lost across 5 steps", accent=CRIMSON, size=21)

        loss_rows = [
            ("18 units", "cleared by spleen / liver (hour 1)"),
            ("14 units", "degrade in circulation"),
            ("12 units", "exit vessel, fail to penetrate"),
            ("55 units", "reach non-tumor tissue"),
        ]

        left_items = VGroup()
        for num_text, desc_text in loss_rows:
            num = Text(num_text, font=MONO, color=CRIMSON, font_size=24)
            desc = Text(desc_text, font=SERIF, color=INK, font_size=20)
            row = VGroup(num, desc).arrange(RIGHT, buff=0.28, aligned_edge=LEFT)
            left_items.add(row)
        left_items.arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        left_col = VGroup(left_header, left_items).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        left_col.move_to(LEFT * 3.0 + UP * 0.2)

        # Vertical divider
        divider = Line(UP * 2.8, DOWN * 2.8, stroke_width=1.5, color=INK)
        divider.move_to(ORIGIN)

        # Right column — arriving dose
        right_header = LabelChip("0.7% reaches tumor", accent=TEAL, size=21)

        arrive_num = Text("0.7 units", font=MONO, color=TEAL, font_size=34, weight=BOLD)
        arrive_desc = Text("reach tumor cells and\nrelease payload", font=SERIF,
                           color=INK, font_size=22)
        right_items = VGroup(arrive_num, arrive_desc).arrange(DOWN, buff=0.2)
        right_col = VGroup(right_header, right_items).arrange(DOWN, buff=0.35)
        right_col.move_to(RIGHT * 3.0 + UP * 0.2)

        # Note bar — "numbers illustrative"
        note = Text("numbers illustrative", font=MONO, color=SLATE, font_size=16)
        note.to_edge(DOWN, buff=0.38)

        self.play(FadeIn(left_header, shift=DOWN * 0.1),
                  FadeIn(right_header, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(divider), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(row, shift=RIGHT * 0.1) for row in left_items],
                              lag_ratio=0.18, run_time=1.6))
        self.play(GrowFromCenter(arrive_num), FadeIn(arrive_desc), run_time=0.9)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.3, total - 0.6 - 0.4 - 1.6 - 0.9 - 0.4))


# ─────────────────────────────────────────────────────────────────────────────
# B11 — ENDCARD
# ─────────────────────────────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]

        topic = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL,
                     font_size=18, weight="MEDIUM")

        q = Text("Why only 0.7%?", font=SERIF, color=INK, font_size=36, weight=BOLD)
        a = Text("Five steps lose dose before the ligand has a chance.",
                 font=SERIF, color=INK, font_size=28)

        u = Line(q.get_corner(DL) + DOWN * 0.1, q.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)

        block = VGroup(q, u, a).arrange(DOWN, buff=0.28)
        topic.next_to(block, UP, buff=0.55)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q), Create(u), run_time=0.9)
        self.play(FadeIn(a, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 0.5 - 0.9 - 0.7))
