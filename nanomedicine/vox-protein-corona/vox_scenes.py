import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import json, os
_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 13)}

import numpy as np


# ---------------------------------------------------------------------------
# B01 — TITLE CARD
# ---------------------------------------------------------------------------
class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The Instant a Nanoparticle Hits Blood,", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        t2 = Text("It Vanishes Under a Coat of Protein", font=DISPLAY, color=CRIMSON, font_size=26, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------------------
# B02 — QUESTION CARD
# ---------------------------------------------------------------------------
class B02_Question(Scene):
    def construct(self):
        total = DUR["B02"]
        chip = LabelChip("The Question", accent=SLATE, size=20)
        chip.to_corner(UL, buff=0.6)
        q1 = Text("The antibodies are still attached.", font=SERIF, color=INK,
                  font_size=32, slant=ITALIC)
        q2 = Text("Why does the particle end up in the liver?", font=SERIF,
                  color=CRIMSON, font_size=32, slant=ITALIC)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        u = Line(block.get_corner(DL) + DOWN * 0.15, block.get_corner(DR) + DOWN * 0.15,
                 color=GOLD, stroke_width=2)
        self.play(FadeIn(chip, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(q1), run_time=0.8)
        self.play(FadeIn(q2), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.2))


# ---------------------------------------------------------------------------
# B04 — CORONA FORMS (the core accumulate graphic)
# ---------------------------------------------------------------------------
class B04_CoronaForms(Scene):
    def construct(self):
        total = DUR["B04"]
        particle = Circle(0.7).set_fill(TEAL, 0.75).set_stroke(INK, 2)
        particle.move_to(ORIGIN)

        # ligands as small teal dots on perimeter
        ligands = VGroup()
        for angle in np.linspace(0, 6.28, 8, endpoint=False):
            dot = Dot(radius=0.09, color=TEAL).move_to(
                particle.get_center() + np.array([np.cos(angle) * 0.78, np.sin(angle) * 0.78, 0]))
            dot.set_fill(TEAL, 1).set_stroke(width=0)
            ligands.add(dot)

        # inner corona ring — proteins settle close
        proteins_inner = VGroup()
        for angle in np.linspace(0.2, 6.5, 14, endpoint=False):
            r = 0.92 + 0.04 * np.sin(angle * 4)
            p = Dot(radius=0.12, color=CRIMSON).move_to(
                np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            p.set_fill(CRIMSON, 0.9).set_stroke(width=0)
            proteins_inner.add(p)

        # outer corona ring — more proteins pile on
        proteins_outer = VGroup()
        for angle in np.linspace(0.5, 6.8, 18, endpoint=False):
            r = 1.08 + 0.05 * np.cos(angle * 3)
            p = Dot(radius=0.10, color=CRIMSON).move_to(
                np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            p.set_fill(CRIMSON, 0.75).set_stroke(width=0)
            proteins_outer.add(p)

        title = Text("Protein corona forms within seconds", font=DISPLAY,
                     font_size=20, color=INK).move_to(UP * 3.2)
        gold_u = Line(title.get_corner(DL) + DOWN * 0.09, title.get_corner(DR) + DOWN * 0.09,
                      color=GOLD, stroke_width=2)
        masked = Text("ligands buried beneath corona", font=MONO, font_size=14,
                      color=CRIMSON).move_to(DOWN * 2.0)

        self.play(Write(title), Create(gold_u), GrowFromCenter(particle), run_time=0.8)
        self.play(AnimationGroup(*[GrowFromCenter(l) for l in ligands], lag_ratio=0.08),
                  run_time=0.6)
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in proteins_inner], lag_ratio=0.05),
                  run_time=1.2)
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in proteins_outer], lag_ratio=0.04),
                  run_time=1.0)
        self.play(FadeIn(masked, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 4.1))


# ---------------------------------------------------------------------------
# B05 — LIGAND MASKED
# ---------------------------------------------------------------------------
class B05_LigandMasked(Scene):
    def construct(self):
        total = DUR["B05"]

        # particle
        particle = Circle(0.65).set_fill(TEAL, 0.7).set_stroke(INK, 2)
        particle.move_to(LEFT * 2.8)

        # one prominent ligand arm extending right
        ligand_base = particle.get_right()
        ligand_line = Line(ligand_base, ligand_base + RIGHT * 0.7,
                           color=TEAL, stroke_width=4)
        ligand_tip = Dot(radius=0.12, color=TEAL).move_to(ligand_base + RIGHT * 0.7)
        ligand_tip.set_fill(TEAL, 1).set_stroke(width=0)
        ligand_group = VGroup(ligand_line, ligand_tip)

        # receptor on right side
        receptor_body = Rectangle(width=0.25, height=0.6).set_fill(TEAL, 0.4)
        receptor_body.set_stroke(TEAL, 2)
        receptor_body.move_to(RIGHT * 2.5)
        receptor_label = Text("receptor", font=MONO, font_size=12, color=TEAL)
        receptor_label.next_to(receptor_body, DOWN, buff=0.12)
        receptor = VGroup(receptor_body, receptor_label)

        # blocking protein (crimson rectangle slides in from above)
        blocker = Rectangle(width=0.55, height=0.45).set_fill(CRIMSON, 0.85)
        blocker.set_stroke(CRIMSON, 2)
        blocker.move_to(ligand_base + RIGHT * 0.5 + UP * 1.5)

        chip = LabelChip("Consequence 1 -- Masking", accent=CRIMSON, size=18)
        chip.to_corner(UL, buff=0.6)

        masked_label = SerifLabel("ligand masked -- cannot bind", accent=CRIMSON, size=20)
        masked_label.move_to(DOWN * 2.8)

        self.play(FadeIn(chip, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowFromCenter(particle), run_time=0.6)
        self.play(Create(ligand_line), GrowFromCenter(ligand_tip), run_time=0.5)
        self.play(FadeIn(receptor, shift=LEFT * 0.2), run_time=0.6)
        self.wait(0.5)
        # blocker slides down and covers the ligand
        self.play(blocker.animate.move_to(ligand_base + RIGHT * 0.5), run_time=1.0)
        self.play(FadeIn(masked_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 4.2))


# ---------------------------------------------------------------------------
# B06 — OPSONIN CLEARANCE
# ---------------------------------------------------------------------------
class B06_OpsominClearance(Scene):
    def construct(self):
        total = DUR["B06"]

        # coated particle (full corona)
        particle = Circle(0.65).set_fill(TEAL, 0.6).set_stroke(INK, 2)
        particle.move_to(LEFT * 2.5)

        corona_dots = VGroup()
        for angle in np.linspace(0, 6.28, 16, endpoint=False):
            r = 0.88
            p = Dot(radius=0.11, color=CRIMSON).move_to(
                particle.get_center() + np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            p.set_fill(CRIMSON, 0.9).set_stroke(width=0)
            corona_dots.add(p)

        chip_opsonin = LabelChip("OPSONIN", accent=CRIMSON, size=18)
        chip_opsonin.next_to(particle, UP, buff=0.7)

        # arrow to liver
        arrow_start = particle.get_right() + RIGHT * 0.2
        arrow_end = RIGHT * 2.5
        clearance_arrow = Arrow(arrow_start, arrow_end, color=CRIMSON, buff=0.1,
                                stroke_width=4, max_tip_length_to_length_ratio=0.18)

        # liver box
        liver_box = Rectangle(width=1.8, height=1.0).set_fill(CRIMSON, 0.2)
        liver_box.set_stroke(CRIMSON, 2)
        liver_box.move_to(RIGHT * 3.6)
        liver_label = Text("liver", font=DISPLAY, font_size=22, color=CRIMSON, weight=BOLD)
        liver_label.move_to(liver_box)
        liver = VGroup(liver_box, liver_label)

        chip_head = LabelChip("Consequence 2 -- Clearance", accent=CRIMSON, size=18)
        chip_head.to_corner(UL, buff=0.6)

        flagged_label = SerifLabel("flagged for clearance", accent=CRIMSON, size=22)
        flagged_label.move_to(DOWN * 2.8)

        self.play(FadeIn(chip_head, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowFromCenter(particle), run_time=0.5)
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in corona_dots], lag_ratio=0.04),
                  run_time=0.9)
        self.play(FadeIn(chip_opsonin, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowArrow(clearance_arrow), run_time=0.7)
        self.play(FadeIn(liver, shift=LEFT * 0.15), run_time=0.5)
        self.play(FadeIn(flagged_label, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 4.0))


# ---------------------------------------------------------------------------
# B07 — TWO ENVIRONMENTS (culture vs blood)
# ---------------------------------------------------------------------------
class B07_TwoEnvironments(Scene):
    def construct(self):
        total = DUR["B07"]

        # gold dividing line
        divider = Line(UP * 3.5, DOWN * 3.5, color=GOLD, stroke_width=2.5)
        divider.move_to(ORIGIN)

        # LEFT PANEL: culture medium — clean particle binding receptor
        culture_label = Text("CULTURE MEDIUM", font=DISPLAY, font_size=18,
                             color=TEAL, weight=BOLD)
        culture_label.move_to(LEFT * 3.5 + UP * 3.0)

        left_particle = Circle(0.5).set_fill(TEAL, 0.75).set_stroke(INK, 2)
        left_particle.move_to(LEFT * 4.2 + UP * 0.3)
        left_ligand = Line(left_particle.get_right(),
                           left_particle.get_right() + RIGHT * 0.55,
                           color=TEAL, stroke_width=4)
        left_tip = Dot(radius=0.1, color=TEAL).move_to(left_particle.get_right() + RIGHT * 0.55)
        left_tip.set_fill(TEAL, 1).set_stroke(width=0)

        left_receptor = Rectangle(width=0.2, height=0.55).set_fill(TEAL, 0.4)
        left_receptor.set_stroke(TEAL, 2)
        left_receptor.move_to(LEFT * 3.3 + UP * 0.3)

        bound_label = Text("binds", font=MONO, font_size=14, color=TEAL)
        bound_label.move_to(LEFT * 3.7 + DOWN * 1.2)

        # RIGHT PANEL: blood — coated particle, arrow to liver
        blood_label = Text("BLOOD", font=DISPLAY, font_size=18,
                           color=CRIMSON, weight=BOLD)
        blood_label.move_to(RIGHT * 3.5 + UP * 3.0)

        right_particle = Circle(0.5).set_fill(TEAL, 0.6).set_stroke(INK, 2)
        right_particle.move_to(RIGHT * 2.0 + UP * 0.3)

        right_corona = VGroup()
        for angle in np.linspace(0, 6.28, 14, endpoint=False):
            r = 0.7
            p = Dot(radius=0.1, color=CRIMSON).move_to(
                right_particle.get_center() + np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            p.set_fill(CRIMSON, 0.9).set_stroke(width=0)
            right_corona.add(p)

        buried_label = Text("ligands buried", font=MONO, font_size=13, color=CRIMSON)
        buried_label.next_to(right_particle, DOWN, buff=0.85)

        right_arrow = Arrow(right_particle.get_right() + RIGHT * 0.15,
                            RIGHT * 4.8 + UP * 0.3,
                            color=CRIMSON, stroke_width=3,
                            max_tip_length_to_length_ratio=0.2)
        liver_txt = Text("liver", font=DISPLAY, font_size=20, color=CRIMSON, weight=BOLD)
        liver_txt.move_to(RIGHT * 5.6 + UP * 0.3)

        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(culture_label), FadeIn(blood_label), run_time=0.5)
        # left panel
        self.play(GrowFromCenter(left_particle), run_time=0.5)
        self.play(Create(left_ligand), GrowFromCenter(left_tip), run_time=0.4)
        self.play(FadeIn(left_receptor, shift=LEFT * 0.15), run_time=0.4)
        self.play(FadeIn(bound_label, shift=UP * 0.1), run_time=0.3)
        # right panel
        self.play(GrowFromCenter(right_particle), run_time=0.5)
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in right_corona], lag_ratio=0.05),
                  run_time=0.8)
        self.play(FadeIn(buried_label, shift=UP * 0.1), run_time=0.3)
        self.play(GrowArrow(right_arrow), FadeIn(liver_txt, shift=LEFT * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.8))


# ---------------------------------------------------------------------------
# B08 — SECTION CARD (validation requirement)
# ---------------------------------------------------------------------------
class B08_ValidationCard(Scene):
    def construct(self):
        total = DUR["B08"]
        main = Text("Testing in culture medium", font=DISPLAY, color=INK,
                    font_size=30, weight=BOLD)
        main2 = Text("is not testing in blood.", font=DISPLAY, color=CRIMSON,
                     font_size=30, weight=BOLD)
        block = VGroup(main, main2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        sub = Text("the corona is not optional -- it is the experimental condition",
                   font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.55)
        u = Line(block.get_corner(DL) + DOWN * 0.12, block.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 1.6))


# ---------------------------------------------------------------------------
# B09 — FOLATE EXAMPLE (bar chart)
# ---------------------------------------------------------------------------
class B09_FolateExample(Scene):
    def construct(self):
        total = DUR["B09"]

        title = Text("Folate-targeted nanoparticle -- illustrative numbers",
                     font=DISPLAY, font_size=17, color=INK)
        title.move_to(UP * 3.3)

        # column headings
        col_culture = Text("IN CULTURE", font=DISPLAY, font_size=19,
                           color=TEAL, weight=BOLD)
        col_blood = Text("IN BLOOD", font=DISPLAY, font_size=19,
                         color=CRIMSON, weight=BOLD)
        col_culture.move_to(LEFT * 3.5 + UP * 2.3)
        col_blood.move_to(RIGHT * 2.0 + UP * 2.3)

        # scale: 1 unit height = 10% of injected dose / binding
        scale = 4.0 / 100.0   # 4 units = 100%

        # culture bar: 87% binding
        bar_culture = Rectangle(width=1.2, height=87 * scale).set_fill(TEAL, 0.8)
        bar_culture.set_stroke(width=0)
        bar_culture.align_to(DOWN * 1.8, DOWN).move_to(LEFT * 3.5 + DOWN * 1.8 + UP * (87 * scale / 2))

        label_87 = Text("87%", font=MONO, font_size=20, color=TEAL)
        label_87.next_to(bar_culture, UP, buff=0.12)
        sub_culture = Text("binding", font=SERIF, font_size=14, color=INK, slant=ITALIC)
        sub_culture.next_to(bar_culture, DOWN, buff=0.12)

        # blood bars: 72% liver (crimson), 3% tumor (teal)
        bar_liver = Rectangle(width=1.2, height=72 * scale).set_fill(CRIMSON, 0.8)
        bar_liver.set_stroke(width=0)
        bar_liver.align_to(DOWN * 1.8, DOWN).move_to(RIGHT * 1.2 + DOWN * 1.8 + UP * (72 * scale / 2))

        bar_tumor = Rectangle(width=1.2, height=3 * scale).set_fill(TEAL, 0.7)
        bar_tumor.set_stroke(width=0)
        bar_tumor.align_to(DOWN * 1.8, DOWN).move_to(RIGHT * 3.0 + DOWN * 1.8 + UP * (3 * scale / 2))

        label_72 = Text("72%", font=MONO, font_size=20, color=CRIMSON)
        label_72.next_to(bar_liver, UP, buff=0.12)
        sub_liver = Text("liver", font=SERIF, font_size=14, color=INK, slant=ITALIC)
        sub_liver.next_to(bar_liver, DOWN, buff=0.12)

        label_3 = Text("3%", font=MONO, font_size=20, color=TEAL)
        label_3.next_to(bar_tumor, UP, buff=0.12)
        sub_tumor = Text("tumor", font=SERIF, font_size=14, color=INK, slant=ITALIC)
        sub_tumor.next_to(bar_tumor, DOWN, buff=0.12)

        # annotation
        buried_ann = SerifLabel("ligands buried under corona", accent=CRIMSON, size=16)
        buried_ann.move_to(RIGHT * 2.1 + DOWN * 2.8)

        illus = Text("(illustrative numbers)", font=MONO, font_size=12, color=SLATE)
        illus.to_corner(DL, buff=0.5)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(col_culture), FadeIn(col_blood), run_time=0.5)
        self.play(GrowFromEdge(bar_culture, DOWN), run_time=0.7)
        self.play(FadeIn(label_87, shift=DOWN * 0.1), FadeIn(sub_culture), run_time=0.4)
        self.play(GrowFromEdge(bar_liver, DOWN), run_time=0.7)
        self.play(GrowFromEdge(bar_tumor, DOWN), run_time=0.5)
        self.play(FadeIn(label_72, shift=DOWN * 0.1), FadeIn(sub_liver),
                  FadeIn(label_3, shift=DOWN * 0.1), FadeIn(sub_tumor), run_time=0.4)
        self.play(FadeIn(buried_ann, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - 5.4))


# ---------------------------------------------------------------------------
# B10 — CORONA SUMMARY (with HandRing)
# ---------------------------------------------------------------------------
class B10_CoronaSummary(Scene):
    def construct(self):
        total = DUR["B10"]

        particle = Circle(0.7).set_fill(TEAL, 0.65).set_stroke(INK, 2)
        particle.move_to(ORIGIN)

        # ligands (barely visible, buried)
        ligands = VGroup()
        for angle in np.linspace(0, 6.28, 8, endpoint=False):
            dot = Dot(radius=0.07, color=TEAL).move_to(
                particle.get_center() + np.array([np.cos(angle) * 0.76, np.sin(angle) * 0.76, 0]))
            dot.set_fill(TEAL, 0.5).set_stroke(width=0)
            ligands.add(dot)

        # full corona
        corona = VGroup()
        for angle in np.linspace(0.2, 6.5, 20, endpoint=False):
            r = 0.95 + 0.04 * np.sin(angle * 5)
            p = Dot(radius=0.11, color=CRIMSON).move_to(
                particle.get_center() + np.array([np.cos(angle) * r, np.sin(angle) * r, 0]))
            p.set_fill(CRIMSON, 0.88).set_stroke(width=0)
            corona.add(p)

        # dummy group for the ring to surround
        ring_target = Circle(0.98).set_stroke(width=0).set_fill(opacity=0)
        ring_target.move_to(particle.get_center())

        label_ligands = SerifLabel("targeting ligands -- buried", accent=TEAL, size=20)
        label_ligands.move_to(LEFT * 4.2 + UP * 1.0)
        label_corona = SerifLabel("protein corona -- seconds", accent=CRIMSON, size=20)
        label_corona.move_to(RIGHT * 3.8 + DOWN * 1.2)

        self.play(GrowFromCenter(particle), run_time=0.5)
        self.play(AnimationGroup(*[GrowFromCenter(l) for l in ligands], lag_ratio=0.06),
                  run_time=0.5)
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in corona], lag_ratio=0.04),
                  run_time=1.0)
        self.play(FadeIn(label_ligands, shift=RIGHT * 0.1), run_time=0.5)
        self.play(FadeIn(label_corona, shift=LEFT * 0.1), run_time=0.5)
        ring = HandRing(ring_target, color=CRIMSON)
        self.play(Create(ring), run_time=1.1)
        self.wait(max(0.5, total - 4.1))


# ---------------------------------------------------------------------------
# B11 — ENDCARD
# ---------------------------------------------------------------------------
class B11_Endcard(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        ans1 = Text("The protein corona buries the targeting ligand.", font=SERIF,
                    color=INK, font_size=28, slant=ITALIC)
        ans2 = Text("The body sees the corona,", font=SERIF, color=INK,
                    font_size=28, slant=ITALIC)
        ans3 = Text("not the particle you designed.", font=SERIF, color=CRIMSON,
                    font_size=28, slant=ITALIC)
        block = VGroup(ans1, ans2, ans3).arrange(DOWN, buff=0.22).move_to(UP * 0.1)
        u = Line(block.get_corner(DL) + DOWN * 0.15, block.get_corner(DR) + DOWN * 0.15,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.6)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.7))
