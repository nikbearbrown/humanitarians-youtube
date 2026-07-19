"""vox_scenes.py — Why a Glowing PET Scan Doesn't Actually Show Cancer
(vox-fdg-proxy, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
B02 and B09 are STILL·ai beats — no scene here (they compile as slates).
Durations read from this reel's beat_sheet.json (actuals after audio lock;
estimates as fallback).

Color law: TEAL #1F6F5C = true signal / correct finding;
           CRIMSON #BF3339 = false interpretation / proxy gap.
           GOLD = editor's-pen highlight (fill only, never text — once per quote).
Card exclusions: NO five-modality tour, NO biodistribution decision tree,
NO activatable probes, NO anatomical/molecular hierarchy.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import json, os

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why a Glowing PET Scan", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("Doesn't Actually Show Cancer", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B03 The Question

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("A PET scan is used to detect cancer.", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        q2 = Text("The tracer isn't looking for cancer cells.", font=DISPLAY, color=INK,
                  font_size=26)
        q3 = Text("What is it actually measuring —", font=DISPLAY, color=TEAL,
                  font_size=26, weight=BOLD)
        q4 = Text("and when does that difference matter?", font=DISPLAY, color=TEAL,
                  font_size=26, weight=BOLD)
        block = VGroup(q1, q2, q3, q4).arrange(DOWN, buff=0.28).move_to(UP * 0.1)
        u = Line(q4.get_corner(DL) + DOWN * 0.12, q4.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.8)
        self.play(FadeIn(q2), run_time=0.7)
        self.play(FadeIn(q3), FadeIn(q4), Create(u), run_time=1.0)
        self.wait(max(0.3, total - 2.5))


# ---------------------------------------------------------------- B04 FDG Uptake

class B04_FDGUptake(Scene):
    def construct(self):
        total = DUR["B04"]

        # Cell outline — simple circle
        cell = Circle(radius=1.6).set_stroke(INK, 3).set_fill(GROUND, 0)
        cell.move_to(LEFT * 2.8 + DOWN * 0.2)
        cell_label = Text("cell", font=SERIF, color=INK, font_size=24, slant=ITALIC)
        cell_label.next_to(cell, DOWN, buff=0.25)

        # Transporter slot on the cell wall (right side)
        slot = Rectangle(width=0.28, height=0.55)
        slot.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        slot.move_to(cell.get_right() + LEFT * 0.05)

        # Glucose molecule (small teal square) approaching from outside
        glc_in = Square(0.25).set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        glc_in.move_to(RIGHT * 0.6 + DOWN * 0.2)

        glc_label = Text("FDG", font=MONO, color=TEAL, font_size=20)
        glc_label.next_to(glc_in, UP, buff=0.12)

        # Trapped molecule inside cell
        trapped = Square(0.28).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        trapped.move_to(cell.get_center() + RIGHT * 0.4)
        trapped_label = Text("trapped", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        trapped_label.next_to(trapped, DOWN, buff=0.12)

        # Signal chip
        signal_chip = LabelChip("PET signal", accent=CRIMSON, size=22)
        signal_chip.move_to(RIGHT * 4.0 + DOWN * 0.2)

        # Transport arrow label
        transport_label = SerifLabel("glucose transporter", TEAL, size=22)
        transport_label.move_to(RIGHT * 0.6 + UP * 1.2)

        self.play(FadeIn(cell), FadeIn(slot), FadeIn(cell_label), run_time=0.8)
        self.play(FadeIn(glc_in), FadeIn(glc_label), FadeIn(transport_label), run_time=0.6)
        self.play(
            glc_in.animate.move_to(trapped.get_center()),
            glc_label.animate.move_to(trapped_label.get_center() + UP * 0.3),
            run_time=0.8
        )
        self.play(
            FadeIn(trapped),
            FadeIn(trapped_label),
            run_time=0.6
        )
        self.play(FadeIn(signal_chip, shift=LEFT * 0.4), run_time=0.6)
        self.wait(max(0.3, total - 3.4))


# ---------------------------------------------------------------- B05 What PET Sees

class B05_WhatPETSees(Scene):
    def construct(self):
        total = DUR["B05"]

        # Left column: "what you think you see"
        left_header = LabelChip("what you think", accent=SLATE, size=22)
        left_header.move_to(LEFT * 3.8 + UP * 2.2)

        tumor_circle = Circle(radius=0.9).set_stroke(CRIMSON, 4).set_fill(CRIMSON, 0.12)
        tumor_circle.move_to(LEFT * 3.8 + UP * 0.4)
        tumor_label = Text("cancer cells", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        tumor_label.next_to(tumor_circle, DOWN, buff=0.2)

        # Right column: "what PET actually reads"
        right_header = LabelChip("what PET reads", accent=TEAL, size=22)
        right_header.move_to(RIGHT * 3.4 + UP * 2.2)

        metab_label = SerifLabel("glucose metabolism", TEAL, size=26)
        metab_label.move_to(RIGHT * 3.4 + UP * 0.6)
        hexo_label = Text("hexokinase activity", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        hexo_label.next_to(metab_label, DOWN, buff=0.3)

        # Wrong arrow: crossed out
        wrong_arrow = Arrow(LEFT * 1.8 + UP * 0.4, RIGHT * 1.8 + UP * 0.4,
                            color=CRIMSON, buff=0.1, stroke_width=3)
        strike_wrong = Line(wrong_arrow.get_start() + UP * 0.22,
                            wrong_arrow.get_end() + DOWN * 0.22,
                            color=CRIMSON, stroke_width=3)
        strike_wrong._qc_intentional = True  # deliberate strike-through

        # Correct path label
        correct_note = Text("not identity — proxy", font=SERIF, color=TEAL,
                            font_size=22, slant=ITALIC)
        correct_note.move_to(DOWN * 1.6)

        self.play(FadeIn(left_header), FadeIn(tumor_circle), FadeIn(tumor_label), run_time=0.8)
        self.play(FadeIn(right_header), FadeIn(metab_label), FadeIn(hexo_label), run_time=0.8)
        self.play(Create(wrong_arrow), Create(strike_wrong), run_time=0.7)
        self.play(FadeIn(correct_note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.9))


# ---------------------------------------------------------------- B06 Section Card (false positives)
# CARD beat — no scene class needed; compiled directly from beat_sheet.json as a text card.
# vox_run.sh handles CARD beats natively.


# ---------------------------------------------------------------- B07 Dark Scan Quote

class B07_DarkScan(Scene):
    def construct(self):
        _quote_scene(self,
                     "A dark scan is not an empty scan.",
                     "— the FDG-negative lesion is metabolically quiet, not absent",
                     None,
                     "dark",
                     DUR["B07"])


# ---------------------------------------------------------------- B08 Imaging Suggests

class B08_ImagingSuggests(Scene):
    def construct(self):
        total = DUR["B08"]

        # Chain: SIGNAL -> PROXY -> BIOLOGY
        signal_chip = LabelChip("SIGNAL", accent=TEAL, size=24)
        signal_chip.move_to(LEFT * 4.8 + UP * 1.0)

        proxy_chip = LabelChip("PROXY", accent=SLATE, size=24)
        proxy_chip.move_to(ORIGIN + UP * 1.0)

        biology_chip = LabelChip("BIOLOGY", accent=CRIMSON, size=24)
        biology_chip.move_to(RIGHT * 4.8 + UP * 1.0)

        # Arrow from signal to proxy
        arr1 = Arrow(signal_chip.get_right() + RIGHT * 0.1,
                     proxy_chip.get_left() + LEFT * 0.1,
                     color=INK, buff=0.0, stroke_width=2.5)

        # Arrow from proxy to biology with question mark
        arr2 = Arrow(proxy_chip.get_right() + RIGHT * 0.1,
                     biology_chip.get_left() + LEFT * 0.1,
                     color=CRIMSON, buff=0.0, stroke_width=2.5)
        qmark = Text("?", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        qmark.next_to(arr2, UP, buff=0.15)

        # Lower chips: the clinical language contrast
        imaging_chip = LabelChip("imaging: consistent with", accent=SLATE, size=20)
        imaging_chip.move_to(LEFT * 2.6 + DOWN * 1.2)

        biopsy_chip = LabelChip("biopsy: confirms", accent=TEAL, size=20)
        biopsy_chip.move_to(RIGHT * 2.6 + DOWN * 1.2)

        # Dividing rule
        rule = Line(LEFT * 6.0 + DOWN * 0.55, RIGHT * 6.0 + DOWN * 0.55,
                    color=INK, stroke_width=1.2)

        self.play(FadeIn(signal_chip), Create(arr1), FadeIn(proxy_chip), run_time=0.9)
        self.play(Create(arr2), FadeIn(qmark), FadeIn(biology_chip), run_time=0.8)
        self.play(Create(rule), run_time=0.4)
        self.play(FadeIn(imaging_chip, shift=UP * 0.15),
                  FadeIn(biopsy_chip, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.3, total - 2.8))


# ---------------------------------------------------------------- B10 Example Result

class B10_ExampleResult(Scene):
    def construct(self):
        total = DUR["B10"]

        # Three node symbols in a row
        node_y = UP * 1.0
        positions = [LEFT * 3.8, ORIGIN, RIGHT * 3.8]
        nodes = VGroup()
        for pos in positions:
            n = Circle(radius=0.55)
            n.set_stroke(CRIMSON, 3).set_fill(CRIMSON, 0.15)
            n.move_to(pos + node_y)
            nodes.add(n)

        # Uptake label above each node
        uptake_labels = VGroup()
        for n in nodes:
            lbl = LabelChip("high uptake", accent=CRIMSON, size=18)
            lbl.next_to(n, UP, buff=0.2)
            uptake_labels.add(lbl)

        # Biopsy result reveals below each node in teal
        biopsy_labels = VGroup()
        for n in nodes:
            lbl = LabelChip("REACTIVE · URI", accent=TEAL, size=18)
            lbl.next_to(n, DOWN, buff=0.25)
            biopsy_labels.add(lbl)

        # Summary serif label
        summary = SerifLabel("all three — no malignant cells found", TEAL, size=24)
        summary.move_to(DOWN * 2.5)

        # Illustrative note
        note = Text("(illustrative case)", font=MONO, color=INK, font_size=18)
        note.to_corner(DR, buff=0.6)

        # Animate: nodes + uptake first, then biopsy reveals
        self.play(LaggedStart(*[FadeIn(n, scale=0.85) for n in nodes], lag_ratio=0.15),
                  LaggedStart(*[FadeIn(lbl) for lbl in uptake_labels], lag_ratio=0.15),
                  run_time=0.9)
        self.play(LaggedStart(*[FadeIn(lbl, shift=UP * 0.15) for lbl in biopsy_labels],
                              lag_ratio=0.2), run_time=0.8)
        self.play(FadeIn(summary, shift=UP * 0.1), FadeIn(note), run_time=0.7)
        self.wait(max(0.3, total - 2.4))


# ---------------------------------------------------------------- B11 Scanner Quote

class B11_ScannerRight(Scene):
    def construct(self):
        _quote_scene(self,
                     "The scanner was right. The assumption was wrong.",
                     "— high metabolism is not cancer; it is what cancer tends to do",
                     None,
                     "assumption",
                     DUR["B11"])


# ---------------------------------------------------------------- B12 Endcard

class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("A PET scan measures metabolism,", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("not malignancy.", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        t3 = Text("Imaging suggests. Biopsy confirms.", font=DISPLAY, color=INK,
                  font_size=24)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.22).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.6))
