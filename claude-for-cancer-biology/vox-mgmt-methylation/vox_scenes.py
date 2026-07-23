"""vox_scenes.py — Why Silencing a Repair Gene Is Better for the Patient Than Expressing It
(vox-mgmt-methylation, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is STILL·ai — no scene.
Color law: TEAL = MGMT methylated / repair silenced / drug works (good for patient);
           CRIMSON = MGMT expressed / drug neutralized (bad for patient).
Exclusions: no DNMT1, no histone code, no IDH, no azacitidine/decitabine, no other biomarkers.
"""
import sys, json, pathlib
# Reel lives at books/cancer-biology/youtube/vox-mgmt-methylation/ —
# .parents[3] = books/, so add books/vox/aspects/explainer/vox-explainer/manim
_vox_manim = pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
sys.path.insert(0, str(_vox_manim))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ----------------------------------------------------------------- B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Silencing a Repair Gene", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("Is Better for the Patient", font=DISPLAY, color=CRIMSON,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ----------------------------------------------------------------- B03 SameTreatment

class B03_SameTreatment(Scene):
    """Temozolomide attaches methyl group to O6 position of guanine — the lesion."""
    def construct(self):
        total = DUR["B03"]

        # Drug label
        drug_label = Text("Temozolomide", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        drug_label.to_edge(UP, buff=0.7)

        # Simple guanine base as a rectangle with label
        base = Rectangle(width=1.4, height=0.9)
        base.set_fill(SLATE, 0.18).set_stroke(SLATE, 2)
        base_label = Text("Guanine (O6)", font=SERIF, color=INK, font_size=22)
        base_label.move_to(base)
        base_group = VGroup(base, base_label).move_to(LEFT * 1.5 + DOWN * 0.3)

        # Arrow from drug to base
        arrow = Arrow(drug_label.get_bottom() + DOWN * 0.1, base_group.get_top() + UP * 0.1,
                      color=INK, stroke_width=3, buff=0.1)

        # Methyl group dot landing on base
        methyl_dot = Dot(radius=0.18, color=CRIMSON)
        methyl_label = Text("CH3", font=SERIF, color=CRIMSON, font_size=20)
        methyl_group = VGroup(methyl_dot, methyl_label).arrange(RIGHT, buff=0.08)
        methyl_group.next_to(base_group, RIGHT, buff=0.6)

        # Lesion label
        lesion_label = Text("O6-methylguanine lesion", font=SERIF, color=CRIMSON, font_size=22)
        lesion_label.next_to(base_group, DOWN, buff=0.55)
        lesion_u = Line(lesion_label.get_corner(DL) + DOWN * 0.06,
                        lesion_label.get_corner(DR) + DOWN * 0.06,
                        stroke_width=1.5, color=CRIMSON)

        self.play(FadeIn(drug_label), run_time=0.7)
        self.play(Create(arrow), run_time=0.6)
        self.play(FadeIn(base_group), run_time=0.7)
        self.play(methyl_group.animate.shift(LEFT * 0.5), FadeIn(methyl_group), run_time=0.8)
        self.play(FadeIn(lesion_label), Create(lesion_u), run_time=0.7)
        self.wait(max(0.3, total - 3.5))


# ----------------------------------------------------------------- B04 TheQuestion

class B04_TheQuestion(Scene):
    """Gap-formula card: DNA repair should protect — here it doesn't — why?"""
    def construct(self):
        total = DUR["B04"]

        # Slate card background
        card = Rectangle(width=10.5, height=4.8)
        card.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        card.move_to(ORIGIN)

        premise = Text("DNA repair should protect a cell.", font=SERIF,
                       color=WHITE, font_size=30)
        premise.move_to(UP * 1.2)

        expect = Text("A tumor that fixes its DNA efficiently should survive better.",
                      font=SERIF, color=WHITE, font_size=24)
        expect.next_to(premise, DOWN, buff=0.45)

        but = Text("Here the efficiently-repairing tumor kills the patient faster.",
                   font=SERIF, color=CRIMSON, font_size=24)
        but.next_to(expect, DOWN, buff=0.45)

        question = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=40, weight=BOLD)
        question.next_to(but, DOWN, buff=0.55)

        self.play(FadeIn(card), run_time=0.5)
        self.play(FadeIn(premise), run_time=0.7)
        self.play(FadeIn(expect), run_time=0.7)
        self.wait(0.5)
        self.play(FadeIn(but), run_time=0.7)
        self.play(FadeIn(question), question.animate.scale(1.1), run_time=0.8)
        self.wait(max(0.3, total - 3.9))


# ----------------------------------------------------------------- B05 NaiveExpectation

class B05_NaiveExpectation(Scene):
    """Naive intuition: damage -> repair -> cell survives. Standard expectation."""
    def construct(self):
        total = DUR["B05"]

        title = Text("The Naive Expectation", font=DISPLAY, color=INK,
                     font_size=24, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        # Left: damage
        dmg_box = Rectangle(width=2.2, height=1.1)
        dmg_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        dmg_box.move_to(LEFT * 4.0 + DOWN * 0.2)
        dmg_label = Text("DNA Damage", font=SERIF, color=CRIMSON, font_size=22)
        dmg_label.move_to(dmg_box)

        # Arrow
        arrow1 = Arrow(dmg_box.get_right() + RIGHT * 0.05,
                       dmg_box.get_right() + RIGHT * 1.7,
                       color=INK, stroke_width=3, buff=0.05)

        # Center: repair
        rep_box = Rectangle(width=2.2, height=1.1)
        rep_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        rep_box.move_to(ORIGIN + DOWN * 0.2)
        rep_label = Text("Repair", font=SERIF, color=TEAL, font_size=22)
        rep_label.move_to(rep_box)

        # Arrow
        arrow2 = Arrow(rep_box.get_right() + RIGHT * 0.05,
                       rep_box.get_right() + RIGHT * 1.7,
                       color=INK, stroke_width=3, buff=0.05)

        # Right: cell survives
        surv_box = Rectangle(width=2.2, height=1.1)
        surv_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        surv_box.move_to(RIGHT * 4.0 + DOWN * 0.2)
        surv_label = Text("Cell survives", font=SERIF, color=TEAL, font_size=22)
        surv_label.move_to(surv_box)

        bottom = Text("More repair = better. Or so you'd think.",
                      font=SERIF, color=INK, font_size=22, slant=ITALIC)
        bottom.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(dmg_box), FadeIn(dmg_label), run_time=0.6)
        self.play(Create(arrow1), run_time=0.5)
        self.play(FadeIn(rep_box), FadeIn(rep_label), run_time=0.6)
        self.play(Create(arrow2), run_time=0.5)
        self.play(FadeIn(surv_box), FadeIn(surv_label), run_time=0.6)
        self.play(FadeIn(bottom), run_time=0.7)
        self.wait(max(0.3, total - 4.1))


# ----------------------------------------------------------------- B06 WhyItFlips

class B06_WhyItFlips(Scene):
    """The inversion: drug is trying to damage the tumor; MGMT repairs = bad for patient."""
    def construct(self):
        total = DUR["B06"]

        title = Text("When the Drug Is Doing the Damaging", font=DISPLAY,
                     color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        # Drug arrow pointing at tumor cell
        drug_label = Text("Temozolomide", font=SERIF, color=TEAL, font_size=22)
        drug_label.move_to(LEFT * 4.5 + UP * 0.4)

        tumor_box = Rectangle(width=1.8, height=1.1)
        tumor_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        tumor_box.move_to(LEFT * 1.5 + UP * 0.4)
        tumor_label = Text("Tumor cell", font=SERIF, color=CRIMSON, font_size=20)
        tumor_label.move_to(tumor_box)

        drug_arrow = Arrow(drug_label.get_right() + RIGHT * 0.1,
                           tumor_box.get_left() + LEFT * 0.1,
                           color=TEAL, stroke_width=3, buff=0.05)

        # MGMT repair arrow removes damage
        mgmt_label = Text("MGMT repairs damage", font=SERIF, color=CRIMSON, font_size=22)
        mgmt_label.move_to(RIGHT * 2.5 + UP * 0.4)

        mgmt_arrow = Arrow(tumor_box.get_right() + RIGHT * 0.1,
                           mgmt_label.get_left() + LEFT * 0.1,
                           color=CRIMSON, stroke_width=3, buff=0.05)

        # Drug wasted label
        wasted = Text("Drug wasted", font=DISPLAY, color=CRIMSON,
                      font_size=26, weight=BOLD)
        wasted.move_to(DOWN * 1.2)

        # Context note
        note = Text("MGMT protects the tumor, not the patient.",
                    font=SERIF, color=INK, font_size=22, slant=ITALIC)
        note.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(drug_label), run_time=0.5)
        self.play(Create(drug_arrow), run_time=0.5)
        self.play(FadeIn(tumor_box), FadeIn(tumor_label), run_time=0.6)
        self.play(Create(mgmt_arrow), run_time=0.5)
        self.play(FadeIn(mgmt_label), run_time=0.6)
        self.play(FadeIn(wasted), run_time=0.6)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(max(0.3, total - 4.5))


# ----------------------------------------------------------------- B07 DecisionTree

class B07_DecisionTree(Scene):
    """Two-branch decision tree: MGMT methylated (TEAL/good) vs unmethylated (CRIMSON/bad)."""
    def construct(self):
        total = DUR["B07"]

        # Root node
        root_box = Rectangle(width=3.0, height=0.8)
        root_box.set_fill(SLATE, 0.18).set_stroke(SLATE, 2)
        root_box.move_to(UP * 3.0)
        root_label = Text("MGMT Promoter Status", font=DISPLAY, color=INK,
                          font_size=20, weight=BOLD)
        root_label.move_to(root_box)

        # Branch stems from root
        left_top = root_box.get_bottom() + DOWN * 0.1
        branch_left = Line(left_top, left_top + DOWN * 0.7 + LEFT * 3.5,
                           color=TEAL, stroke_width=2.5)
        branch_right = Line(left_top, left_top + DOWN * 0.7 + RIGHT * 3.5,
                            color=CRIMSON, stroke_width=2.5)

        # Left branch label
        lbl_left = Text("Methylated", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        lbl_left.next_to(branch_left.get_end(), DOWN, buff=0.05)

        # Right branch label
        lbl_right = Text("Unmethylated", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        lbl_right.next_to(branch_right.get_end(), DOWN, buff=0.05)

        # Left chain (TEAL)
        left_nodes = [
            ("No MGMT protein made", TEAL),
            ("Lesions accumulate", TEAL),
            ("Tumor cells die", TEAL),
        ]
        left_group = VGroup()
        prev_bottom = lbl_left.get_bottom() + DOWN * 0.15
        left_boxes = []
        left_arrows = []
        for text, color in left_nodes:
            box = Rectangle(width=2.5, height=0.65)
            box.set_fill(color, 0.12).set_stroke(color, 1.8)
            txt = Text(text, font=SERIF, color=INK, font_size=18)
            txt.move_to(box)
            vg = VGroup(box, txt)
            vg.move_to(prev_bottom + DOWN * 0.42)
            arr = Arrow(prev_bottom, vg.get_top() + UP * 0.05,
                        color=color, stroke_width=2, buff=0.05)
            left_boxes.append(vg)
            left_arrows.append(arr)
            left_group.add(arr, vg)
            prev_bottom = vg.get_bottom()

        # Shift entire left chain to left
        left_group.shift(LEFT * 3.5)
        lbl_left.shift(LEFT * 3.5)
        branch_left_shift = branch_left.copy().shift(ORIGIN)

        # Right chain (CRIMSON)
        right_nodes = [
            ("MGMT expressed", CRIMSON),
            ("Damage repaired", CRIMSON),
            ("Drug wasted", CRIMSON),
        ]
        right_group = VGroup()
        prev_bottom_r = lbl_right.get_bottom() + DOWN * 0.15
        right_boxes = []
        right_arrows_list = []
        for text, color in right_nodes:
            box = Rectangle(width=2.5, height=0.65)
            box.set_fill(color, 0.12).set_stroke(color, 1.8)
            txt = Text(text, font=SERIF, color=INK, font_size=18)
            txt.move_to(box)
            vg = VGroup(box, txt)
            vg.move_to(prev_bottom_r + DOWN * 0.42)
            arr = Arrow(prev_bottom_r, vg.get_top() + UP * 0.05,
                        color=color, stroke_width=2, buff=0.05)
            right_boxes.append(vg)
            right_arrows_list.append(arr)
            right_group.add(arr, vg)
            prev_bottom_r = vg.get_bottom()

        right_group.shift(RIGHT * 3.5)
        lbl_right.shift(RIGHT * 3.5)

        # Outcome badges on terminal nodes
        good_badge = Text("GOOD OUTCOME", font=DISPLAY, color=TEAL,
                          font_size=14, weight=BOLD)
        good_badge.next_to(left_boxes[-1], DOWN, buff=0.1)

        bad_badge = Text("DRUG WASTED", font=DISPLAY, color=CRIMSON,
                         font_size=14, weight=BOLD)
        bad_badge.next_to(right_boxes[-1], DOWN, buff=0.1)

        # Build animation
        self.play(FadeIn(root_box), FadeIn(root_label), run_time=0.7)
        self.play(Create(branch_left), Create(branch_right), run_time=0.6)
        self.play(FadeIn(lbl_left), FadeIn(lbl_right), run_time=0.6)

        # Animate left chain
        for arr, box in zip(left_arrows, left_boxes):
            self.play(Create(arr), FadeIn(box), run_time=0.5)

        # Animate right chain
        for arr, box in zip(right_arrows_list, right_boxes):
            self.play(Create(arr), FadeIn(box), run_time=0.5)

        self.play(FadeIn(good_badge), FadeIn(bad_badge), run_time=0.7)
        self.wait(max(0.3, total - 7.5))


# ----------------------------------------------------------------- B08 SuicideMechanism

class B08_SuicideMechanism(Scene):
    """MGMT suicide: one methyl transfer per enzyme molecule, then protein self-destructs."""
    def construct(self):
        total = DUR["B08"]

        title = Text("MGMT: The Suicide Enzyme", font=DISPLAY, color=INK,
                     font_size=24, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        # DNA strand with lesion
        dna_rect = Rectangle(width=5.0, height=0.5)
        dna_rect.set_fill(SLATE, 0.2).set_stroke(SLATE, 2)
        dna_rect.move_to(LEFT * 1.5 + UP * 0.6)
        dna_label = Text("DNA strand", font=SERIF, color=INK, font_size=18)
        dna_label.next_to(dna_rect, UP, buff=0.12)

        # Lesion dot on DNA
        lesion_dot = Dot(radius=0.2, color=CRIMSON)
        lesion_dot.move_to(dna_rect.get_center() + LEFT * 0.5)
        lesion_label = Text("O6-methylguanine", font=SERIF, color=CRIMSON, font_size=16)
        lesion_label.next_to(lesion_dot, DOWN, buff=0.15)

        # MGMT protein box
        mgmt_box = Rectangle(width=2.0, height=1.0)
        mgmt_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        mgmt_box.move_to(RIGHT * 2.5 + UP * 0.6)
        mgmt_label = Text("MGMT", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        mgmt_label.move_to(mgmt_box)

        # Transfer arrow from lesion to MGMT cysteine
        cys_label = Text("Cys", font=MONO, color=TEAL, font_size=18)
        cys_label.next_to(mgmt_box, LEFT, buff=0.15)

        transfer_arrow = Arrow(lesion_dot.get_right() + RIGHT * 0.05,
                               cys_label.get_left() + LEFT * 0.05,
                               color=INK, stroke_width=2.5, buff=0.05)

        methyl_moved = Dot(radius=0.15, color=CRIMSON)
        methyl_moved.move_to(cys_label.get_center() + RIGHT * 0.3)

        # Step 2: MGMT self-destructs
        cross1 = Line(mgmt_box.get_corner(UL), mgmt_box.get_corner(DR),
                      color=CRIMSON, stroke_width=3)
        cross2 = Line(mgmt_box.get_corner(UR), mgmt_box.get_corner(DL),
                      color=CRIMSON, stroke_width=3)

        destroyed_label = Text("Protein destroyed", font=SERIF, color=CRIMSON, font_size=20)
        destroyed_label.next_to(mgmt_box, DOWN, buff=0.3)

        one_repair = Text("One repair event per molecule.", font=SERIF,
                          color=INK, font_size=22, slant=ITALIC)
        one_repair.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(dna_rect), FadeIn(dna_label), run_time=0.6)
        self.play(FadeIn(lesion_dot), FadeIn(lesion_label), run_time=0.6)
        self.play(FadeIn(mgmt_box), FadeIn(mgmt_label), FadeIn(cys_label), run_time=0.6)
        self.play(Create(transfer_arrow), run_time=0.6)
        self.play(FadeIn(methyl_moved), run_time=0.4)
        self.wait(0.4)
        self.play(Create(cross1), Create(cross2), run_time=0.6)
        self.play(FadeIn(destroyed_label), run_time=0.5)
        self.play(FadeIn(one_repair), run_time=0.6)
        self.wait(max(0.3, total - 5.5))


# ----------------------------------------------------------------- B09 MethylSilences

class B09_MethylSilences(Scene):
    """Methylated CpG dots block transcription machinery — MGMT promoter silenced."""
    def construct(self):
        total = DUR["B09"]

        title = Text("Methylated Promoter = Silenced Gene", font=DISPLAY,
                     color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        # Promoter label
        prom_label = Text("MGMT promoter (CpG region)", font=SERIF, color=INK, font_size=20)
        prom_label.move_to(UP * 1.8)

        # DNA strand
        dna_line = Line(LEFT * 5.0 + UP * 0.9, RIGHT * 5.0 + UP * 0.9,
                        color=SLATE, stroke_width=4)

        # CpG methylation dots (filled = methylated)
        n_cpg = 8
        dots = VGroup()
        x_positions = [i * 1.1 - 3.85 for i in range(n_cpg)]
        for x in x_positions:
            d = Dot(radius=0.18, color=TEAL)
            d.move_to(RIGHT * x + UP * 1.25)
            dots.add(d)

        methyl_note = Text("Methyl marks on cytosine", font=SERIF, color=TEAL, font_size=18)
        methyl_note.next_to(dots, UP, buff=0.18)

        # RNA polymerase blocked (simple box with X)
        pol_box = Rectangle(width=1.8, height=1.0)
        pol_box.set_fill(SLATE, 0.2).set_stroke(SLATE, 2)
        pol_box.move_to(LEFT * 0.5 + DOWN * 0.5)
        pol_label = Text("RNA pol", font=SERIF, color=INK, font_size=18)
        pol_label.move_to(pol_box)

        block_bar = Rectangle(width=0.12, height=1.4)
        block_bar.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        block_bar.next_to(pol_box, LEFT, buff=0.05)

        blocked_label = Text("Blocked", font=SERIF, color=CRIMSON, font_size=20)
        blocked_label.next_to(block_bar, LEFT, buff=0.15)

        # Result
        result = Text("No MGMT mRNA. No MGMT protein.", font=SERIF,
                      color=CRIMSON, font_size=22)
        result.to_edge(DOWN, buff=0.8)
        result_u = Line(result.get_corner(DL) + DOWN * 0.07,
                        result.get_corner(DR) + DOWN * 0.07,
                        stroke_width=1.5, color=CRIMSON)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(prom_label), Create(dna_line), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(d, scale=0.7) for d in dots],
                              lag_ratio=0.08, run_time=1.2))
        self.play(FadeIn(methyl_note), run_time=0.5)
        self.play(FadeIn(pol_box), FadeIn(pol_label), run_time=0.6)
        self.play(FadeIn(block_bar), FadeIn(blocked_label), run_time=0.6)
        self.play(FadeIn(result), Create(result_u), run_time=0.7)
        self.wait(max(0.3, total - 5.9))


# ----------------------------------------------------------------- B10 Biomarker

class B10_Biomarker(Scene):
    """Predictive vs prognostic biomarker distinction."""
    def construct(self):
        total = DUR["B10"]

        title = Text("MGMT Methylation: A Predictive Biomarker", font=DISPLAY,
                     color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.6)

        # Two chips side by side
        chip_prog = LabelChip("Prognostic", accent=SLATE, size=24)
        chip_pred = LabelChip("Predictive", accent=TEAL, size=24)
        chips = VGroup(chip_prog, chip_pred).arrange(RIGHT, buff=2.2)
        chips.move_to(UP * 0.8)

        # Descriptions
        prog_desc = Text("Predicts survival\nregardless of treatment",
                         font=SERIF, color=INK, font_size=20)
        prog_desc.next_to(chip_prog, DOWN, buff=0.35)

        pred_desc = Text("Predicts benefit\nfrom this specific drug",
                         font=SERIF, color=TEAL, font_size=20)
        pred_desc.next_to(chip_pred, DOWN, buff=0.35)

        # MGMT is predictive note
        verdict = Text("MGMT methylation status = predictive.", font=SERIF,
                       color=TEAL, font_size=22, slant=ITALIC)
        verdict.to_edge(DOWN, buff=0.9)
        verdict_u = Line(verdict.get_corner(DL) + DOWN * 0.07,
                         verdict.get_corner(DR) + DOWN * 0.07,
                         stroke_width=1.5, color=TEAL)

        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(chip_prog), FadeIn(chip_pred), run_time=0.7)
        self.play(FadeIn(prog_desc), FadeIn(pred_desc), run_time=0.8)
        self.play(FadeIn(verdict), Create(verdict_u), run_time=0.7)
        self.wait(max(0.3, total - 2.8))


# ----------------------------------------------------------------- B11 ExampleTrace

class B11_ExampleTrace(Scene):
    """Follow one O6-methylguanine lesion in each patient through to fate."""
    def construct(self):
        total = DUR["B11"]

        title = Text("One Lesion, Two Fates (illustrative)", font=DISPLAY,
                     color=INK, font_size=22, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # --- Patient A (TEAL - good outcome) ---
        pa_header = Text("Patient A — MGMT methylated", font=DISPLAY,
                         color=TEAL, font_size=20, weight=BOLD)
        pa_header.move_to(LEFT * 3.3 + UP * 2.1)

        pa_steps = [
            "O6-methylguanine forms",
            "MGMT absent",
            "Lesion persists",
            "Mismatch detected",
            "Apoptosis triggered",
        ]
        pa_step_colors = [CRIMSON, TEAL, CRIMSON, INK, TEAL]
        pa_step_group = VGroup()
        prev_y = 1.35
        pa_dots = []
        pa_labels = []
        for i, (step, col) in enumerate(zip(pa_steps, pa_step_colors)):
            dot = Dot(radius=0.1, color=col)
            dot.move_to(LEFT * 4.2 + UP * prev_y)
            lbl = Text(step, font=SERIF, color=INK, font_size=16)
            lbl.next_to(dot, RIGHT, buff=0.15)
            pa_step_group.add(dot, lbl)
            pa_dots.append(dot)
            pa_labels.append(lbl)
            prev_y -= 0.62

        # Arrow connecting steps in Patient A
        pa_final = Text("Tumor cell dies", font=DISPLAY, color=TEAL,
                        font_size=18, weight=BOLD)
        pa_final.move_to(LEFT * 3.3 + DOWN * 2.15)

        # --- Patient B (CRIMSON - bad outcome) ---
        pb_header = Text("Patient B — MGMT unmethylated", font=DISPLAY,
                         color=CRIMSON, font_size=20, weight=BOLD)
        pb_header.move_to(RIGHT * 3.0 + UP * 2.1)

        pb_steps = [
            "O6-methylguanine forms",
            "MGMT present",
            "Methyl transfer (~2 min)",
            "MGMT destroys itself",
            "Lesion gone",
        ]
        pb_step_colors = [CRIMSON, CRIMSON, INK, CRIMSON, TEAL]
        pb_step_group = VGroup()
        prev_y2 = 1.35
        pb_dots = []
        pb_labels = []
        for i, (step, col) in enumerate(zip(pb_steps, pb_step_colors)):
            dot = Dot(radius=0.1, color=col)
            dot.move_to(RIGHT * 1.5 + UP * prev_y2)
            lbl = Text(step, font=SERIF, color=INK, font_size=16)
            lbl.next_to(dot, RIGHT, buff=0.15)
            pb_step_group.add(dot, lbl)
            pb_dots.append(dot)
            pb_labels.append(lbl)
            prev_y2 -= 0.62

        pb_final = Text("Tumor cell survives", font=DISPLAY, color=CRIMSON,
                        font_size=18, weight=BOLD)
        pb_final.move_to(RIGHT * 3.0 + DOWN * 2.15)

        # Divider
        divider = Line(UP * 2.5, DOWN * 2.5, color=SLATE, stroke_width=1.5)
        divider.move_to(LEFT * 0.5)

        # Build scene
        self.play(FadeIn(title), run_time=0.6)
        self.play(FadeIn(pa_header), FadeIn(pb_header), Create(divider), run_time=0.7)

        # Animate steps for both patients simultaneously
        for (da, la), (db, lb) in zip(zip(pa_dots, pa_labels), zip(pb_dots, pb_labels)):
            self.play(FadeIn(da), FadeIn(la), FadeIn(db), FadeIn(lb), run_time=0.55)

        self.play(FadeIn(pa_final), FadeIn(pb_final), run_time=0.7)
        self.wait(max(0.3, total - 8.5))


# ----------------------------------------------------------------- B12 Endcard

class B12_Endcard(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        line1 = Text("Repair protects the wrong side.", font=SERIF,
                     color=INK, font_size=34, weight=BOLD)
        line2 = Text("Silenced MGMT = the drug works.", font=SERIF,
                     color=TEAL, font_size=28)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        u = Line(block.get_corner(DL) + DOWN * 0.18, block.get_corner(DR) + DOWN * 0.18,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.3, total - 1.6))
