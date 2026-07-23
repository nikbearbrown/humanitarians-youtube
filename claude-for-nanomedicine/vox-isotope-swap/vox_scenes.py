"""vox_scenes.py — One Molecule, Two Isotopes: See the Tumor, Then Treat It
(vox-isotope-swap, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat.
B02 and B09 are STILL·ai slots — no scene class (they compile as slates).

Color law: TEAL #1F6F5C = target-expressed / imaging-lit / responds;
           CRIMSON #BF3339 = PSMA-negative / dark / no response.
GOLD #F5D061 = editor's-pen highlight fill (B06 only), never text.
Never swapped mid-film.

Exclusions: NO beta-vs-alpha physics, NO dosing detail, NO DOTATATE,
NO VISION trial stats. Isotope-swap loop and scan-selects-patient only.
"""
import sys, pathlib, json, os
# Resolve toolkit manim library from this file's location:
# vox-isotope-swap/ -> youtube/ -> cancer-nanomedicine/ -> books/ -> books/vox/aspects/...
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {f"B{i:02d}": 10.0 for i in range(1, 13)}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ─────────────────────────────────────────── B01 — COLD OPEN / title card

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("One Molecule, Two Isotopes:", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("See the Tumor, Then Treat It", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        u.set_stroke(color=GOLD, width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─────────────────────────────────────────── B02 — STILL·ai (no scene)
# PET scan image — open slot, compiles as slate


# ─────────────────────────────────────────── B03 — COLD OPEN / lesion map

class B03_LesionMap(Scene):
    """Six lesion circles on a body silhouette outline: 4 teal (PSMA-positive),
    2 crimson (PSMA-negative). Labels appear after the circles."""
    def construct(self):
        total = DUR["B03"]
        # Body silhouette — a simple ellipse chain: head + torso
        head = Circle(radius=0.45).set_stroke(INK, 2).set_fill(opacity=0)
        head.move_to(UP * 3.2)
        torso = Ellipse(width=2.0, height=3.8).set_stroke(INK, 2).set_fill(opacity=0)
        torso.move_to(UP * 0.8)
        body = VGroup(head, torso)

        # Six lesion positions (x, y) on the torso
        positions = [
            LEFT * 0.5 + UP * 1.9,   # upper left — teal
            RIGHT * 0.4 + UP * 1.6,  # upper right — teal
            LEFT * 0.6 + UP * 0.6,   # mid left — teal
            RIGHT * 0.5 + UP * 0.3,  # mid right — teal
            LEFT * 0.3 + DOWN * 0.7, # lower left — crimson (PSMA-neg)
            RIGHT * 0.4 + DOWN * 0.9,# lower right — crimson (PSMA-neg, largest)
        ]
        colors = [TEAL, TEAL, TEAL, TEAL, CRIMSON, CRIMSON]
        radii  = [0.18, 0.16, 0.17, 0.15, 0.26, 0.30]

        circles = VGroup(*[
            Circle(radius=r).set_fill(c, 0.85).set_stroke(width=0)
            .move_to(p)
            for p, c, r in zip(positions, colors, radii)
        ])

        # Labels on the right side
        pos_label = LabelChip("PSMA-POSITIVE", accent=TEAL, size=20)
        pos_label.move_to(RIGHT * 4.2 + UP * 1.2)
        neg_label = LabelChip("PSMA-NEGATIVE", accent=CRIMSON, size=20)
        neg_label.move_to(RIGHT * 4.2 + DOWN * 0.8)
        pos_note = SerifLabel("4 lesions lit", TEAL, size=22)
        pos_note.next_to(pos_label, DOWN, buff=0.2)
        neg_note = SerifLabel("2 stay dark", CRIMSON, size=22)
        neg_note.next_to(neg_label, DOWN, buff=0.2)

        self.play(FadeIn(body), run_time=0.7)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in circles[:4]], lag_ratio=0.15),
            run_time=1.0
        )
        self.play(FadeIn(pos_label), FadeIn(pos_note), run_time=0.6)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in circles[4:]], lag_ratio=0.3),
            run_time=0.7
        )
        self.play(FadeIn(neg_label), FadeIn(neg_note), run_time=0.6)
        self.wait(max(0.3, total - 3.6))


# ─────────────────────────────────────────── B04 — THE QUESTION card

class B04_Question(Scene):
    def construct(self):
        total = DUR["B04"]
        # Slate panel behind all text — white-on-slate passes WCAG contrast
        panel = Rectangle(width=13.0, height=5.0)
        panel.set_fill(SLATE, 1).set_stroke(width=0)
        panel.move_to(ORIGIN)
        # All text in INK on cream ground would fail contrast; use WHITE on slate.
        # Static checker sees the panel as the background for the white text.
        lines = VGroup(
            Text("A cancer drug and an imaging probe", font=SERIF, color=WHITE,
                 font_size=30, slant=ITALIC),
            Text("can be built from the same molecule.", font=SERIF, color=WHITE,
                 font_size=30, slant=ITALIC),
            Text("If they work by identical biology --", font=SERIF, color=WHITE,
                 font_size=30, slant=ITALIC),
            Text("why does one scan have to come before the other?", font=SERIF,
                 color=WHITE, font_size=30, slant=ITALIC, weight=BOLD),
        )
        lines.arrange(DOWN, buff=0.22).move_to(ORIGIN)
        # Teal underline on the key question line
        u = Line(lines[3].get_corner(DL) + DOWN * 0.1,
                 lines[3].get_corner(DR) + DOWN * 0.1,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(panel), run_time=0.5)
        self.play(FadeIn(lines), Create(u), run_time=1.4)
        self.wait(max(0.3, total - 1.9))


# ─────────────────────────────────────────── B05 — THE PROBLEM / naive loop

class B05_NaiveLoop(Scene):
    """Naive treat-on-diagnosis: DIAGNOSIS -> TREAT, simple direct arrow."""
    def construct(self):
        total = DUR["B05"]
        dx_box = Rectangle(width=3.6, height=1.0)
        dx_box.set_fill(SLATE, 1).set_stroke(width=0)
        dx_box.move_to(LEFT * 3.5)
        dx_label = Text("DIAGNOSIS", font=DISPLAY, color=WHITE, font_size=22)
        dx_label.move_to(dx_box)
        dx_sub = SerifLabel("prostate cancer", SLATE, size=22)
        dx_sub.next_to(dx_box, DOWN, buff=0.2)

        tx_box = Rectangle(width=3.6, height=1.0)
        tx_box.set_fill(SLATE, 1).set_stroke(width=0)
        tx_box.move_to(RIGHT * 3.5)
        tx_label = Text("TREAT", font=DISPLAY, color=WHITE, font_size=22)
        tx_label.move_to(tx_box)
        tx_sub = SerifLabel("inject the drug", SLATE, size=22)
        tx_sub.next_to(tx_box, DOWN, buff=0.2)

        arrow = Arrow(dx_box.get_right(), tx_box.get_left(),
                      color=INK, stroke_width=4, buff=0.1)
        naive_label = SerifLabel("the naive assumption", INK, size=24)
        naive_label.move_to(UP * 2.2)

        self.play(FadeIn(naive_label), run_time=0.5)
        self.play(FadeIn(dx_box), FadeIn(dx_label), FadeIn(dx_sub), run_time=0.7)
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(tx_box), FadeIn(tx_label), FadeIn(tx_sub), run_time=0.7)
        self.wait(max(0.3, total - 2.5))


# ─────────────────────────────────────────── B06 — THE PROBLEM / companion dx quote

class B06_CompanionDx(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The imaging step becomes a genuine companion diagnostic\nfor that specific therapy, not a generic staging procedure.",
            "— Cancer Nanomedicine, Ch. 7",
            None,
            "companion diagnostic",
            DUR["B06"]
        )


# ─────────────────────────────────────────── B07 — THE MECHANISM / isotope swap morph

class B07_IsotopeSwap(Scene):
    """Central molecule stays fixed; isotope chip MORPHS from Ga-68 (teal)
    to Lu-177 (crimson) while function label swaps below."""
    def construct(self):
        total = DUR["B07"]

        # The molecule — a central hexagon to represent a small molecule
        mol = RegularPolygon(n=6, radius=0.9)
        mol.set_fill(INK, 0.12).set_stroke(INK, 2.5)
        mol.move_to(ORIGIN)
        mol_label = Text("PSMA ligand", font=SERIF, color=INK,
                         font_size=22, slant=ITALIC)
        mol_label.next_to(mol, DOWN, buff=0.4)

        # Eyebrow
        eye = SerifLabel("same molecule", INK, size=26)
        eye.move_to(UP * 2.8)

        # BEFORE state: Ga-68 chip (teal) + PET SCANNER label
        ga_chip = LabelChip("Ga-68", accent=TEAL, size=28)
        ga_chip.next_to(mol, UP, buff=0.55)
        scan_label = Text("PET SCANNER", font=DISPLAY, color=TEAL,
                          font_size=24, weight=BOLD)
        scan_label.move_to(LEFT * 3.5 + UP * 1.0)

        # AFTER state: Lu-177 chip (crimson) + THERAPY label
        lu_chip = LabelChip("Lu-177", accent=CRIMSON, size=28)
        lu_chip.next_to(mol, UP, buff=0.55)
        tx_label = Text("THERAPY", font=DISPLAY, color=CRIMSON,
                        font_size=24, weight=BOLD)
        tx_label.move_to(RIGHT * 3.8 + UP * 1.0)

        # Arrow between function labels
        swap_arrow = Arrow(LEFT * 1.6 + UP * 1.0, RIGHT * 2.5 + UP * 1.0,
                           color=INK, stroke_width=3, buff=0.1)
        swap_label = SerifLabel("swap isotope", INK, size=22)
        swap_label.next_to(swap_arrow, DOWN, buff=0.15)

        # Build: molecule appears, then Ga-68 side, then morph
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(mol), FadeIn(mol_label), run_time=0.7)
        self.play(FadeIn(ga_chip), FadeIn(scan_label), run_time=0.7)

        # The morph: Ga-68 chip transforms to Lu-177 chip
        self.play(
            GrowArrow(swap_arrow),
            FadeIn(swap_label),
            run_time=0.7
        )
        self.play(
            ReplacementTransform(ga_chip, lu_chip),
            FadeIn(tx_label),
            run_time=1.2
        )
        # Hold showing both labels and the morphed chip
        self.wait(max(0.3, total - 3.8))


# ─────────────────────────────────────────── B08 — THE MECHANISM / binding logic

class B08_BindingLogic(Scene):
    """Two tumor cells: left has PSMA receptors (teal) and drug binds;
    right has no receptors (crimson X) and drug passes through."""
    def construct(self):
        total = DUR["B08"]

        # Left cell — PSMA-positive
        left_cell = Circle(radius=1.2)
        left_cell.set_fill(TEAL, 0.15).set_stroke(TEAL, 2.5)
        left_cell.move_to(LEFT * 3.5)
        left_title = LabelChip("PSMA PRESENT", accent=TEAL, size=20)
        left_title.next_to(left_cell, UP, buff=0.3)

        # Receptors on left cell (small ticks on circumference)
        import numpy as np
        cell_center = np.array([-3.5, 0.0, 0.0])
        rec_positions = [
            np.array([-3.5,  1.2, 0.0]),
            np.array([-2.65, 0.85, 0.0]),
            np.array([-2.3,  0.0, 0.0]),
            np.array([-2.65,-0.85, 0.0]),
        ]
        def _norm(v):
            mag = np.linalg.norm(v)
            return v / mag if mag > 0 else v
        receptors = VGroup(*[
            Line(p, p + _norm(p - cell_center) * 0.3,
                 color=TEAL, stroke_width=4)
            for p in rec_positions
        ])

        # Drug molecule (small circle) docking on left cell
        drug_l = Dot(radius=0.18).set_fill(INK, 0.9)
        drug_l.move_to(LEFT * 1.5)
        bound_label = SerifLabel("binds", TEAL, size=22)
        bound_label.next_to(left_cell, DOWN, buff=0.3)

        # Right cell — PSMA-negative
        right_cell = Circle(radius=1.2)
        right_cell.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2.5)
        right_cell.move_to(RIGHT * 3.5)
        right_title = LabelChip("PSMA ABSENT", accent=CRIMSON, size=20)
        right_title.next_to(right_cell, UP, buff=0.3)

        # Drug molecule (small circle) passing right cell — no binding
        drug_r = Dot(radius=0.18).set_fill(INK, 0.9)
        drug_r.move_to(RIGHT * 2.0)
        miss_label = SerifLabel("cannot bind", CRIMSON, size=22)
        miss_label.next_to(right_cell, DOWN, buff=0.3)

        # Divider
        div = Line(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=1.5)
        div.move_to(ORIGIN)

        self.play(FadeIn(left_cell), FadeIn(left_title),
                  FadeIn(right_cell), FadeIn(right_title),
                  FadeIn(div), run_time=0.8)
        self.play(FadeIn(receptors), run_time=0.5)
        self.play(FadeIn(drug_l), drug_l.animate.move_to(LEFT * 2.3),
                  run_time=0.8)
        self.play(FadeIn(bound_label), run_time=0.4)
        self.play(FadeIn(drug_r), drug_r.animate.move_to(RIGHT * 5.2),
                  run_time=1.0)
        self.play(FadeIn(miss_label), run_time=0.4)
        self.wait(max(0.3, total - 3.9))


# ─────────────────────────────────────────── B09 — STILL·ai (no scene)
# Physician reading scan — open slot, compiles as slate


# ─────────────────────────────────────────── B10 — THE IMPLICATION / scan decides

class B10_ScanPredicts(Scene):
    """Two-column decision split: bright on PET -> treats; dark -> cannot bind."""
    def construct(self):
        total = DUR["B10"]

        header = Text("THE SCAN DECIDES", font=DISPLAY, color=INK,
                      font_size=28, weight=BOLD)
        header.move_to(UP * 3.0)

        # Left column — bright
        left_col = Rectangle(width=5.5, height=5.0)
        left_col.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        left_col.move_to(LEFT * 3.2 + DOWN * 0.3)

        bright_chip = LabelChip("BRIGHT ON PET", accent=TEAL, size=22)
        bright_chip.move_to(LEFT * 3.2 + UP * 1.6)

        bright_dot = Circle(radius=0.4).set_fill(TEAL, 0.9).set_stroke(width=0)
        bright_dot.move_to(LEFT * 3.2 + UP * 0.5)

        bright_arrow = Arrow(LEFT * 3.2 + DOWN * 0.1,
                             LEFT * 3.2 + DOWN * 0.9,
                             color=TEAL, stroke_width=4, buff=0.05)
        bright_result = LabelChip("TREATS TARGET", accent=TEAL, size=22)
        bright_result.move_to(LEFT * 3.2 + DOWN * 1.4)

        bright_note = SerifLabel("PSMA present", TEAL, size=20)
        bright_note.move_to(LEFT * 3.2 + DOWN * 2.0)

        # Right column — dark
        right_col = Rectangle(width=5.5, height=5.0)
        right_col.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        right_col.move_to(RIGHT * 3.2 + DOWN * 0.3)

        dark_chip = LabelChip("DARK ON PET", accent=CRIMSON, size=22)
        dark_chip.move_to(RIGHT * 3.2 + UP * 1.6)

        dark_dot = Circle(radius=0.4).set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.5)
        dark_dot.move_to(RIGHT * 3.2 + UP * 0.5)

        dark_arrow = Arrow(RIGHT * 3.2 + DOWN * 0.1,
                           RIGHT * 3.2 + DOWN * 0.9,
                           color=CRIMSON, stroke_width=4, buff=0.05)
        dark_result = LabelChip("CANNOT BIND", accent=CRIMSON, size=22)
        dark_result.move_to(RIGHT * 3.2 + DOWN * 1.4)

        dark_note = SerifLabel("PSMA absent", CRIMSON, size=20)
        dark_note.move_to(RIGHT * 3.2 + DOWN * 2.0)

        self.play(FadeIn(header), run_time=0.5)
        self.play(FadeIn(left_col), FadeIn(right_col), run_time=0.6)
        self.play(FadeIn(bright_chip), FadeIn(dark_chip), run_time=0.5)
        self.play(FadeIn(bright_dot), FadeIn(dark_dot), run_time=0.5)
        self.play(GrowArrow(bright_arrow), GrowArrow(dark_arrow), run_time=0.7)
        self.play(FadeIn(bright_result), FadeIn(dark_result), run_time=0.5)
        self.play(FadeIn(bright_note), FadeIn(dark_note), run_time=0.5)
        self.wait(max(0.3, total - 3.8))


# ─────────────────────────────────────────── B11 — THE EXAMPLE

class B11_Example(Scene):
    """Before/after comparison: 6 lesions (4 teal, 2 crimson).
    Day 90: 4 teal shrink 60%, 2 crimson grow 40%. All numbers illustrative."""
    def construct(self):
        total = DUR["B11"]

        # Column headers
        before_hdr = Text("BEFORE TREATMENT", font=DISPLAY, color=INK,
                          font_size=22, weight=BOLD)
        before_hdr.move_to(LEFT * 3.5 + UP * 3.2)
        after_hdr = Text("DAY 90", font=DISPLAY, color=INK,
                         font_size=22, weight=BOLD)
        after_hdr.move_to(RIGHT * 3.5 + UP * 3.2)

        # Divider line
        div = Line(UP * 3.5, DOWN * 3.0, color=INK, stroke_width=1.5)
        div.move_to(ORIGIN)

        # BEFORE: 4 teal + 2 crimson circles
        # Teal lesions (4)
        t_r = [0.28, 0.24, 0.26, 0.22]
        t_pos = [LEFT * 3.8 + UP * 1.8,
                 LEFT * 3.2 + UP * 0.7,
                 LEFT * 4.0 + DOWN * 0.3,
                 LEFT * 3.3 + DOWN * 1.4]
        teal_before = VGroup(*[
            Circle(radius=r).set_fill(TEAL, 0.85).set_stroke(width=0).move_to(p)
            for r, p in zip(t_r, t_pos)
        ])
        # Crimson lesions (2) — larger
        c_r = [0.40, 0.48]
        c_pos = [LEFT * 3.7 + DOWN * 2.5,
                 LEFT * 3.1 + DOWN * 3.3]
        crim_before = VGroup(*[
            Circle(radius=r).set_fill(CRIMSON, 0.75).set_stroke(width=0).move_to(p)
            for r, p in zip(c_r, c_pos)
        ])

        # AFTER: 4 teal (smaller — 60% shrink) + 2 crimson (larger — 40% grow)
        # Shrunk to ~63% of original radius (linear; volume would be cube-root)
        t_r2 = [r * 0.63 for r in t_r]
        t_pos2 = [RIGHT * 3.2 + UP * 1.8,
                  RIGHT * 3.8 + UP * 0.7,
                  RIGHT * 3.1 + DOWN * 0.3,
                  RIGHT * 3.7 + DOWN * 1.4]
        teal_after = VGroup(*[
            Circle(radius=r).set_fill(TEAL, 0.85).set_stroke(width=0).move_to(p)
            for r, p in zip(t_r2, t_pos2)
        ])
        # Grown to ~119% of original radius
        c_r2 = [r * 1.19 for r in c_r]
        c_pos2 = [RIGHT * 3.6 + DOWN * 2.5,
                  RIGHT * 3.0 + DOWN * 3.4]
        crim_after = VGroup(*[
            Circle(radius=r).set_fill(CRIMSON, 0.75).set_stroke(width=0).move_to(p)
            for r, p in zip(c_r2, c_pos2)
        ])

        # Percentage chips
        teal_pct = LabelChip("-60%", accent=TEAL, size=26)
        teal_pct.move_to(RIGHT * 3.5 + UP * 2.8)
        crim_pct = LabelChip("+40%", accent=CRIMSON, size=26)
        crim_pct.move_to(RIGHT * 3.5 + DOWN * 2.0)

        # Illustrative label (inside safe area: +-6.3/+-3.4)
        illus = SerifLabel("illustrative", INK, size=20)
        illus.move_to(RIGHT * 5.5 + DOWN * 3.0)

        self.play(FadeIn(before_hdr), FadeIn(after_hdr), FadeIn(div), run_time=0.7)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in teal_before], lag_ratio=0.15),
            LaggedStart(*[GrowFromCenter(c) for c in crim_before], lag_ratio=0.3),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in teal_after], lag_ratio=0.15),
            LaggedStart(*[GrowFromCenter(c) for c in crim_after], lag_ratio=0.3),
            run_time=1.2
        )
        self.play(FadeIn(teal_pct), FadeIn(crim_pct), run_time=0.7)
        self.play(FadeIn(illus, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 4.2))


# ─────────────────────────────────────────── B12 — RECAP / endcard

class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The scan that finds the target", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("IS the treatment decision.", font=DISPLAY, color=TEAL,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.4)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=TEAL, stroke_width=2)
        sub = Text("One molecule, two isotopes — the imaging step selects the patient.",
                   font=SERIF, color=INK, font_size=22, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.55)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.3))
