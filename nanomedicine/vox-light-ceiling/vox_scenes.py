"""vox_scenes.py — Why a Better Cancer Drug Can't Fix a Tumor Two Centimeters Deep
(vox-light-ceiling, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B02 is the only STILL (ai media slot) and has no scene here.
Durations read from this reel's beat_sheet.json (actuals after audio lock;
estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-nanomedicine/youtube/vox-light-ceiling

Color law:
  TEAL  = light reaching / cleared surface tumor (the positive outcome)
  CRIMSON = unreached tumor / physics ceiling (the problem)
  GOLD  = the physics ceiling line — fill/stroke only, NEVER text color

EXCLUSIONS honored: oxygen dependence, PDT triad Venn, photothermal therapy,
photoimmunotherapy, 5-ALA surgery. ONE mechanism only: light stops at
millimeters, formulation cannot beat physics.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, pathlib
# vox toolkit is at books/vox/ — locate it relative to this file's absolute path.
# This file lives at: books/<book>/youtube/<slug>/vox_scenes.py
# so: parents[0]=<slug>/, parents[1]=youtube/, parents[2]=<book>/, parents[3]=books/
_HERE = pathlib.Path(__file__).resolve()
_VOX_MANIM = _HERE.parents[3] / "vox" / "aspects" / "explainer" / "vox-explainer" / "manim"
if str(_VOX_MANIM) not in sys.path:
    sys.path.insert(0, str(_VOX_MANIM))
from vox_graphics import *  # noqa: F401,F403
import json, os, numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 13)}


# ---------------------------------------------------------------- B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why a Better Cancer Drug", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("Can't Fix a Tumor Two Centimeters Deep", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B03 Question Card

class B03_QuestionCard(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = LabelChip("THE QUESTION", accent=SLATE, size=20)
        q1 = Text("A PDT drug accumulates at 10x normal concentration.", font=SERIF,
                  color=INK, font_size=26, slant=ITALIC)
        q2 = Text("Surface tumor at 2mm: cleared.", font=SERIF,
                  color=TEAL, font_size=26, weight=BOLD)
        q3 = Text("Tumor at 15mm: untouched.", font=SERIF,
                  color=CRIMSON, font_size=26, weight=BOLD)
        q4 = Text("Why can't better drug delivery fix this?", font=DISPLAY,
                  color=INK, font_size=28, weight=BOLD)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.22).move_to(UP * 0.5)
        u = Line(q4.get_corner(DL) + DOWN * 0.1, q4.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        q4.next_to(block, DOWN, buff=0.45)
        u.next_to(q4, DOWN, buff=0.05)
        eye.next_to(block, UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(q3, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(q4), Create(u), run_time=0.7)
        self.wait(max(0.3, total - 2.8))


# ---------------------------------------------------------------- B04 PDT Mechanism

class B04_PDTMechanism(Scene):
    def construct(self):
        total = DUR["B04"]

        # Drug chip on left, light chip on right, cell in center
        drug_chip = LabelChip("DRUG", accent=TEAL, size=26)
        drug_chip.move_to(LEFT * 4.5 + UP * 0.5)

        light_chip = LabelChip("LIGHT", accent=SLATE, size=26)
        light_chip.move_to(LEFT * 4.5 + DOWN * 0.8)

        cell = Circle(radius=0.8).set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        cell.move_to(RIGHT * 1.5 + UP * 0.0)
        cell_label = Text("tumor cell", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        cell_label.next_to(cell, DOWN, buff=0.2)

        # Arrows from drug and light to cell
        arr_drug = Arrow(drug_chip.get_right() + RIGHT * 0.15,
                         cell.get_left() + LEFT * 0.1,
                         buff=0.1, color=TEAL, stroke_width=3,
                         tip_length=0.22, max_tip_length_to_length_ratio=0.3)
        arr_light = Arrow(light_chip.get_right() + RIGHT * 0.15,
                          cell.get_left() + LEFT * 0.1,
                          buff=0.1, color=GOLD, stroke_width=3,
                          tip_length=0.22, max_tip_length_to_length_ratio=0.3)

        # Activated state
        cell_active = Circle(radius=0.8).set_fill(TEAL, 0.55).set_stroke(TEAL, 3)
        cell_active.move_to(cell.get_center())
        activated_label = Text("activated", font=SERIF, color=TEAL,
                               font_size=22, weight=BOLD)
        activated_label.next_to(cell_active, DOWN, buff=0.2)

        # Dark/inert label for drug alone
        inert_note = Text("inert without light", font=MONO, color=INK, font_size=18)
        inert_note.move_to(LEFT * 1.5 + DOWN * 2.3)

        self.play(FadeIn(drug_chip, shift=RIGHT * 0.3),
                  FadeIn(light_chip, shift=RIGHT * 0.3),
                  FadeIn(cell), FadeIn(cell_label), run_time=0.8)
        self.play(GrowArrow(arr_drug), GrowArrow(arr_light), run_time=0.9)
        self.play(FadeIn(inert_note, scale=0.9), run_time=0.5)
        self.play(ReplacementTransform(cell, cell_active),
                  FadeOut(cell_label),
                  FadeIn(activated_label), run_time=0.9)
        self.wait(max(0.3, total - 3.1))


# ---------------------------------------------------------------- B05 Light Question

class B05_LightQuestion(Scene):
    def construct(self):
        total = DUR["B05"]

        # Tissue block on the right
        tissue = Rectangle(width=4.5, height=4.5)
        tissue.set_fill(SLATE, 0.18).set_stroke(SLATE, 2)
        tissue.move_to(RIGHT * 2.8)
        tissue_label = Text("tissue", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        tissue_label.next_to(tissue, DOWN, buff=0.25)

        # Light beam from left
        beam = Rectangle(width=3.5, height=0.55)
        beam.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
        beam.move_to(LEFT * 2.0 + UP * 0.1)

        beam_label = Text("light", font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        beam_label.next_to(beam, UP, buff=0.2)

        # Fading effect — three progressively dimmer rectangles inside tissue
        fade1 = Rectangle(width=1.0, height=0.55).set_fill(TEAL, 0.5).set_stroke(width=0, opacity=0)
        fade1.move_to(RIGHT * 0.85 + UP * 0.1)
        fade2 = Rectangle(width=1.0, height=0.55).set_fill(TEAL, 0.2).set_stroke(width=0, opacity=0)
        fade2.move_to(RIGHT * 2.1 + UP * 0.1)
        fade3 = Rectangle(width=1.0, height=0.55).set_fill(TEAL, 0.05).set_stroke(width=0, opacity=0)
        fade3.move_to(RIGHT * 3.35 + UP * 0.1)

        # Question mark at depth
        qmark = Text("?", font=DISPLAY, color=CRIMSON, font_size=64, weight=BOLD)
        qmark.move_to(RIGHT * 4.5 + UP * 0.1)

        question = Text("how far does light go?", font=DISPLAY, color=INK, font_size=24)
        question.move_to(DOWN * 2.6)

        self.play(FadeIn(tissue), FadeIn(tissue_label), run_time=0.6)
        self.play(GrowFromEdge(beam, LEFT), FadeIn(beam_label), run_time=0.9)
        self.play(FadeIn(fade1), FadeIn(fade2), FadeIn(fade3), run_time=0.8)
        self.play(FadeIn(qmark, scale=0.8), run_time=0.5)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.4))


# ---------------------------------------------------------------- B06 Light Depth Ruler

class B06_LightDepth(Scene):
    def construct(self):
        total = DUR["B06"]

        # Depth ruler (vertical, 0mm at top, 20mm at bottom)
        ruler = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=2).move_to(LEFT * 4.5)
        ruler_label = Text("tissue depth", font=DISPLAY, font_size=13, color=INK
                           ).next_to(ruler, LEFT, buff=0.22).rotate(90 * DEGREES)

        # Tick marks and mm labels
        depths_mm = [0, 2, 5, 10, 15, 20]
        tick_grp = VGroup()
        lbl_grp = VGroup()
        ruler_top_y = 3.0
        ruler_span = 6.0
        for d in depths_mm:
            frac = d / 20.0
            y = ruler_top_y - frac * ruler_span
            tick = Line(LEFT * 4.5 + LEFT * 0.12, LEFT * 4.5 + RIGHT * 0.12,
                        color=INK, stroke_width=1.5)
            tick.move_to(LEFT * 4.5 + UP * y)
            lbl = Text(f"{d}mm", font=MONO, font_size=12, color=INK
                       ).move_to(LEFT * 3.55 + UP * y)
            tick_grp.add(tick)
            lbl_grp.add(lbl)

        # Light attenuation bars (teal, decreasing opacity)
        # bar positions: depth 0-2mm zone teal strong, 2-5mm fading, 5-10mm dim, 10+ gone
        bar_data = [
            (0.0,  1.0,   TEAL,    1.0),   # 0mm: full intensity
            (0.5,  0.72,  TEAL,    0.80),  # 1mm
            (1.0,  0.45,  TEAL,    0.58),  # 2mm boundary
            (1.5,  0.25,  GOLD,    0.38),  # 3mm — crossing into uncertainty
            (2.0,  0.12,  CRIMSON, 0.22),  # 4mm — barely there
            (2.5,  0.04,  CRIMSON, 0.1),   # 5mm — essentially zero
        ]
        bars = VGroup()
        for frac, width_mult, color, opacity in bar_data:
            y = ruler_top_y - frac * 1.2 * ruler_span / 5.0
            bar = Rectangle(width=2.8 * width_mult, height=0.52,
                            fill_color=color, fill_opacity=opacity)
            bar.set_stroke(width=0, opacity=0)
            bar.move_to(RIGHT * 0.0 + UP * y)
            bars.add(bar)

        # Surface cleared tumor marker (TEAL, at 2mm depth)
        y_2mm = ruler_top_y - (2.0 / 20.0) * ruler_span
        surface_dot = Circle(radius=0.28).set_fill(TEAL, 0.9).set_stroke(TEAL, 2)
        surface_dot.move_to(RIGHT * 3.2 + UP * y_2mm)
        surface_lbl = Text("2mm: cleared", font=SERIF, color=TEAL,
                           font_size=18, weight=BOLD)
        surface_lbl.next_to(surface_dot, RIGHT, buff=0.2)

        # Deep tumor marker (CRIMSON, at 15mm depth)
        y_15mm = ruler_top_y - (15.0 / 20.0) * ruler_span
        deep_dot = Circle(radius=0.35).set_fill(CRIMSON, 0.9).set_stroke(CRIMSON, 2)
        deep_dot.move_to(RIGHT * 3.2 + UP * y_15mm)
        deep_lbl = Text("15mm: untouched", font=SERIF, color=CRIMSON,
                        font_size=18, weight=BOLD)
        deep_lbl.next_to(deep_dot, RIGHT, buff=0.2)

        # Physics ceiling dashed line at ~5mm zone
        y_ceil = ruler_top_y - (5.0 / 20.0) * ruler_span
        ceiling_line = DashedLine(LEFT * 4.2, RIGHT * 3.0, color=GOLD, stroke_width=2)
        ceiling_line.move_to(LEFT * 0.6 + UP * y_ceil)
        ceiling_txt = Text("light ceiling", font=MONO, font_size=14, color=INK)
        ceiling_txt.next_to(ceiling_line, RIGHT, buff=0.2)

        # Build
        self.play(Create(ruler), Write(ruler_label), run_time=0.6)
        self.play(FadeIn(tick_grp), FadeIn(lbl_grp), run_time=0.5)
        self.play(
            AnimationGroup(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.18),
            run_time=1.6
        )
        self.play(FadeIn(surface_dot, scale=0.8), FadeIn(surface_lbl), run_time=0.6)
        self.play(FadeIn(deep_dot, scale=0.8), FadeIn(deep_lbl), run_time=0.6)
        self.play(Create(ceiling_line), FadeIn(ceiling_txt), run_time=0.7)
        self.wait(max(0.3, total - 4.6))


# ---------------------------------------------------------------- B07 Optical Window Bar Chart

class B07_OpticalWindow(Scene):
    def construct(self):
        total = DUR["B07"]

        # Horizontal bar chart: red light 3mm, NIR 6mm, deep tumor 15mm
        # Bars grow from left baseline
        baseline_x = LEFT * 4.8
        unit = 0.38  # pixels per mm

        labels = ["red light\n(630 nm)", "near-infrared\nlight", "deep tumor\ntarget"]
        values = [3, 6, 15]
        colors = [TEAL, TEAL, CRIMSON]
        opacities = [1.0, 0.65, 0.85]
        y_positions = [UP * 1.3, UP * 0.0, DOWN * 1.3]
        bar_h = 0.7

        bars = []
        bar_labels_r = []
        name_labels = []
        for i, (lbl, val, col, opa, yp) in enumerate(
                zip(labels, values, colors, opacities, y_positions)):
            bar_w = val * unit
            bar = Rectangle(width=bar_w, height=bar_h)
            bar.set_fill(col, opa).set_stroke(width=0, opacity=0)
            bar.move_to(baseline_x + RIGHT * (bar_w / 2) + yp)
            bars.append(bar)

            val_lbl = Text(f"{val}mm", font=MONO, color=INK, font_size=22, weight=BOLD)
            val_lbl.next_to(bar, RIGHT, buff=0.18)
            bar_labels_r.append(val_lbl)

            name_lbl = Text(lbl, font=SERIF, color=INK, font_size=18, slant=ITALIC)
            name_lbl.next_to(bar, LEFT, buff=0.22)
            name_labels.append(name_lbl)

        # Gold ceiling line at 6mm
        # baseline_x is LEFT*4.8 = numpy array with x=-4.8
        base_x_val = -4.8
        ceil_x = base_x_val + 6 * unit          # plain float
        y_vals = [1.3, 0.0, -1.3]               # from y_positions above
        ceil_top_y = y_vals[0] + bar_h / 2 + 0.3
        ceil_bot_y = y_vals[2] - bar_h / 2 - 0.3
        ceiling = DashedLine(
            np.array([ceil_x, ceil_top_y, 0]),
            np.array([ceil_x, ceil_bot_y, 0]),
            color=GOLD, stroke_width=2.5
        )
        ceiling_lbl = Text("optical ceiling", font=MONO, font_size=14, color=INK)
        ceiling_lbl.move_to(np.array([ceil_x + 0.9, ceil_top_y + 0.3, 0]))

        # Gap annotation for the deep tumor bar
        gap_arrow = Arrow(
            np.array([ceil_x + 0.15, y_vals[2], 0]),
            np.array([base_x_val + 15 * unit - 0.1, y_vals[2], 0]),
            buff=0.0, color=CRIMSON, stroke_width=2.5,
            tip_length=0.2, max_tip_length_to_length_ratio=0.25
        )
        gap_lbl = Text("light cannot reach", font=SERIF, color=CRIMSON,
                       font_size=17, slant=ITALIC)
        gap_lbl.next_to(gap_arrow, DOWN, buff=0.18)

        # Build
        self.play(FadeIn(name_labels[0]), FadeIn(name_labels[1]), FadeIn(name_labels[2]),
                  run_time=0.6)
        self.play(GrowFromEdge(bars[0], LEFT), GrowFromEdge(bars[1], LEFT),
                  run_time=1.0)
        self.play(FadeIn(bar_labels_r[0]), FadeIn(bar_labels_r[1]), run_time=0.4)
        self.play(GrowFromEdge(bars[2], LEFT), run_time=0.8)
        self.play(FadeIn(bar_labels_r[2]), run_time=0.3)
        self.play(Create(ceiling), FadeIn(ceiling_lbl), run_time=0.7)
        self.play(GrowArrow(gap_arrow), FadeIn(gap_lbl), run_time=0.7)
        self.wait(max(0.3, total - 4.5))


# ---------------------------------------------------------------- B08 Formulation Ceiling

class B08_FormulationCeiling(Scene):
    def construct(self):
        total = DUR["B08"]

        # Two columns: standard delivery (left) and 10x nanoparticle (right)
        # Each column has a drug accumulation bar and a light-reach zone below a ceiling line

        col_positions = [LEFT * 3.0, RIGHT * 1.5]
        labels_top = ["standard\ndelivery", "nanoparticle\n10x accumulation"]
        # drug bars: drug accumulates inside tumor — above ceiling zone
        drug_heights = [1.0, 2.5]   # 10x is taller
        light_zone_h = 1.4          # what light can actually reach — same for both

        col_grp = VGroup()

        ceiling_y = 0.0  # gold ceiling line at y=0

        for pos, lbl_txt, drug_h in zip(col_positions, labels_top, drug_heights):
            col_w = 2.0

            # Header label
            hdr = Text(lbl_txt, font=DISPLAY, color=INK, font_size=20, weight=BOLD)
            hdr.move_to(pos + UP * 3.2)

            # Drug accumulation zone (above ceiling — drug is there, but light isn't)
            drug_bar = Rectangle(width=col_w, height=drug_h)
            drug_bar.set_fill(TEAL, 0.45).set_stroke(TEAL, 1.5)
            drug_bar.move_to(pos + UP * (ceiling_y + drug_h / 2))
            drug_note = Text("drug", font=MONO, color=TEAL, font_size=16)
            drug_note.move_to(drug_bar.get_center())

            # Light reach zone (below ceiling)
            light_bar = Rectangle(width=col_w, height=light_zone_h)
            light_bar.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.0)
            light_bar.move_to(pos + UP * (ceiling_y - light_zone_h / 2))
            light_note = Text("light\nreaches", font=MONO, color=INK, font_size=14)
            light_note.move_to(light_bar.get_center())

            # Below light zone — no activation
            dark_bar = Rectangle(width=col_w, height=1.4)
            dark_bar.set_fill(SLATE, 0.12).set_stroke(SLATE, 0.8)
            dark_bar.move_to(pos + DOWN * (light_zone_h + 0.7))

            col_grp.add(hdr, drug_bar, drug_note, light_bar, light_note, dark_bar)

        # Gold ceiling line spanning both columns
        ceiling_line = DashedLine(
            col_positions[0] + LEFT * 1.2,
            col_positions[1] + RIGHT * 1.2,
            color=GOLD, stroke_width=3
        ).move_to(UP * ceiling_y + RIGHT * (-0.75))
        ceiling_lbl = Text("physics ceiling", font=MONO, font_size=16, color=INK)
        ceiling_lbl.next_to(ceiling_line, RIGHT, buff=0.2)

        # "Same ceiling" callout
        same_txt = Text("same ceiling — tissue optics unchanged", font=SERIF,
                        color=INK, font_size=19, slant=ITALIC)
        same_txt.move_to(DOWN * 3.1)

        self.play(FadeIn(col_grp), run_time=1.0)
        self.play(Create(ceiling_line), FadeIn(ceiling_lbl), run_time=0.8)
        self.play(FadeIn(same_txt, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.4))


# ---------------------------------------------------------------- B09 Two Patients

class B09_TwoPatients(Scene):
    def construct(self):
        total = DUR["B09"]

        # Two tissue cross-sections side by side
        section_w, section_h = 4.5, 5.0
        positions = [LEFT * 2.9, RIGHT * 2.9]
        titles = ["Barrett's esophagus\n1mm depth", "Submucosal lesion\n12mm depth"]
        tumor_depths_frac = [0.1, 0.72]   # fraction down the section
        tumor_colors = [TEAL, CRIMSON]
        clear_pcts = ["94%\ncleared", "3%\ncleared"]
        light_pcts = ["100%\nlight", "< 2%\nlight"]
        light_opacities = [0.85, 0.06]

        for i, (pos, title, depth_frac, t_color, clear, lpct, lopa) in enumerate(
                zip(positions, titles, tumor_depths_frac, tumor_colors,
                    clear_pcts, light_pcts, light_opacities)):

            # Tissue background block
            section = Rectangle(width=section_w, height=section_h)
            section.set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
            section.move_to(pos + DOWN * 0.2)

            # Title above
            t = Text(title, font=DISPLAY, color=INK, font_size=19, weight=BOLD)
            t.next_to(section, UP, buff=0.3)

            # Light intensity band at the top of the tissue
            light_band = Rectangle(width=section_w, height=0.6)
            light_band.set_fill(TEAL, lopa).set_stroke(width=0, opacity=0)
            light_band.move_to(pos + UP * (section_h / 2 - 0.3 - 0.2))
            light_lbl = Text(lpct, font=MONO, color=INK, font_size=14)
            light_lbl.next_to(light_band, RIGHT, buff=0.18)

            # Tumor circle at depth
            tumor_y = pos[1] + section_h / 2 - depth_frac * section_h - 0.2
            tumor = Circle(radius=0.52).set_fill(t_color, 0.85).set_stroke(t_color, 2)
            tumor.move_to(np.array([pos[0], tumor_y, 0]))

            # Outcome label
            outcome = Text(clear, font=MONO, color=t_color, font_size=20, weight=BOLD)
            outcome.next_to(tumor, RIGHT, buff=0.25)

            self.play(FadeIn(section), FadeIn(t), run_time=0.5)
            self.play(GrowFromEdge(light_band, UP), FadeIn(light_lbl), run_time=0.5)
            self.play(FadeIn(tumor, scale=0.8), FadeIn(outcome), run_time=0.6)

        # Illustrative note at bottom
        note = Text("illustrative numbers", font=SERIF, color=INK,
                    font_size=17, slant=ITALIC)
        note.move_to(DOWN * 3.2)
        self.play(FadeIn(note), run_time=0.5)

        # Same carrier callout
        carrier_note = Text("same nanoparticle carrier  same accumulation",
                            font=MONO, color=SLATE, font_size=15)
        carrier_note.move_to(UP * 3.1)
        self.play(FadeIn(carrier_note), run_time=0.5)

        self.wait(max(0.3, total - 4.1))


# ---------------------------------------------------------------- B10 Endcard

class B10_End(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The ceiling isn't chemistry.", font=DISPLAY, color=INK,
                  font_size=34, weight=BOLD)
        t2 = Text("It's the millimeters tissue allows.", font=DISPLAY, color=CRIMSON,
                  font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.6)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.0))
