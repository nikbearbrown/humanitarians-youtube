"""vox_scenes.py — Why the Tumor That Shrank in Mice Won't Shrink in Patients
(vox-epr-gap, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 and B06 are STILL·ai beats and have no scene class here — they compile as slates.

Color law:
  TEAL = mouse xenograft / open EPR / good accumulation
  CRIMSON = human desmoplastic tumor / blocked EPR / failure
  GOLD = editor's pen highlight (fill only, never text)
  Two accents max; never swapped mid-film.

Exclusions (card-level): NO BIND-014 specifics, NO IFP derivation, NO stromal
disruption strategies, NO active vs passive targeting debate. One mechanism only:
mouse model = EPR-max; patients = EPR-variable/low.

Render (on machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-nanomedicine/youtube/vox-epr-gap

Gate B convention: every zero-width stroke is also zero-opacity.
"""

import sys, json, os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}

# ---------------------------------------------------------------- helpers

NP_R = 0.08   # nanoparticle dot radius


def _np_dot(color=TEAL, r=NP_R):
    """A single nanoparticle as a small filled circle."""
    d = Circle(radius=r)
    d.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return d


def _vessel_rect(center, w=3.5, h=0.55, color=TEAL):
    """A vessel lumen as a horizontal rounded rectangle."""
    v = RoundedRectangle(width=w, height=h, corner_radius=0.22)
    v.set_fill(color, 0.15).set_stroke(color, 2.5)
    v.move_to(center)
    return v


def _fiber_line(start, end, color=CRIMSON):
    """A desmoplastic fiber as a short line segment."""
    l = Line(start, end, color=color, stroke_width=3)
    return l


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Tumor That Shrank in Mice", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("Won't Shrink in Patients", font=DISPLAY, color=CRIMSON,
                  font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_AccumComparison(Scene):
    """Cold open graphic: mouse accumulation (tall, TEAL) vs patient tumors
    (short, variable, CRIMSON). Side-by-side bars — the core contrast."""

    def construct(self):
        total = DUR["B03"]

        # Mouse bar
        mouse_bar = Rectangle(width=1.4, height=3.2)
        mouse_bar.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        mouse_bar.move_to(LEFT * 3.5 + DOWN * 0.6)

        mouse_val = Text("8% ID/g", font=DISPLAY, color=TEAL,
                         font_size=22, weight=BOLD)
        mouse_val.next_to(mouse_bar, UP, buff=0.2)

        mouse_label = LabelChip("Mouse xenograft", accent=TEAL, size=20)
        mouse_label.next_to(mouse_bar, DOWN, buff=0.25)

        # Patient bars — 5 short bars at varying heights to show variability
        heights = [0.8, 0.4, 1.1, 0.25, 0.6]
        patient_bars = VGroup()
        xs = [-0.8, 0.15, 1.1, 2.05, 3.0]
        for i, (h, x) in enumerate(zip(heights, xs)):
            bar = Rectangle(width=0.75, height=h)
            bar.set_fill(CRIMSON, 0.75).set_stroke(width=0, opacity=0)
            bar.move_to(RIGHT * x + DOWN * (3.2 / 2 - h / 2) + DOWN * 0.6 + UP * (3.2 - 3.2) / 2)
            bar.align_to(mouse_bar, DOWN)
            patient_bars.add(bar)

        patient_range = Text("0.1-2% ID/g", font=DISPLAY, color=CRIMSON,
                             font_size=20, weight=BOLD)
        patient_range.next_to(patient_bars, UP, buff=0.2)

        patient_label = LabelChip("Patient tumors", accent=CRIMSON, size=20)
        patient_label.next_to(patient_bars, DOWN, buff=0.25)

        # Shared label
        same_chip = LabelChip("same nanoparticle", accent=SLATE, size=19)
        same_chip.move_to(UP * 3.0)

        # Divider line between mouse and patients
        div = Line(LEFT * 1.8 + UP * 2.8, LEFT * 1.8 + DOWN * 2.8,
                   color=INK, stroke_width=1)
        div.set_stroke(opacity=0.3)

        self.play(FadeIn(same_chip, shift=DOWN * 0.2), run_time=0.6)
        self.play(GrowFromEdge(mouse_bar, DOWN), FadeIn(mouse_label), run_time=1.0)
        self.play(FadeIn(mouse_val, shift=UP * 0.1), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in patient_bars],
                        lag_ratio=0.15),
            run_time=1.0
        )
        self.play(FadeIn(patient_range, shift=UP * 0.1), FadeIn(patient_label), run_time=0.6)
        self.wait(max(0.3, total - 4.1))


class B04_TheQuestion(Scene):
    """THE QUESTION beat — gap formula on screen."""

    def construct(self):
        total = DUR["B04"]
        lines = [
            "A cancer nanoparticle reliably",
            "delivered drug to tumors in mice.",
            "In patients with the same tumor type,",
            "it mostly ended up in the liver.",
            "The molecule was identical. Why?"
        ]
        q = Paragraph(*lines, font=SERIF, color=INK,
                      font_size=32, alignment="center", line_spacing=1.0)
        q.move_to(UP * 0.3)
        why = q[-1]   # "The molecule was identical. Why?"
        bar = Rectangle(width=0.1, height=why.height + 0.18)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar.align_to(why, LEFT).align_to(why, DOWN).shift(DOWN * 0.04)
        self.play(FadeIn(q), run_time=1.2)
        self.add(bar)
        bar.set_z_index(-1)
        why.set_z_index(1)
        bar.align_to(why, LEFT)
        self.play(bar.animate.stretch_to_fit_width(why.width + 0.2), run_time=0.9)
        self.wait(max(0.5, total - 2.1))


class B05_EPRMechanism(Scene):
    """THE PROBLEM — EPR schematic: leaky vessel, particles streaming through."""

    def construct(self):
        total = DUR["B05"]

        # Vessel wall — two horizontal bars with gaps
        top_wall = Rectangle(width=6.5, height=0.22)
        top_wall.set_fill(TEAL, 0.7).set_stroke(width=0, opacity=0)
        top_wall.move_to(UP * 1.4)

        bot_wall = Rectangle(width=6.5, height=0.22)
        bot_wall.set_fill(TEAL, 0.7).set_stroke(width=0, opacity=0)
        bot_wall.move_to(UP * 0.55)

        # Fenestration gaps — small gaps cut in the walls (shown as gaps)
        # We'll use the background color rectangles to show gaps
        gap_positions = [-2.1, -0.5, 1.3, 2.9]
        gap_covers = VGroup()
        for x in gap_positions:
            g = Rectangle(width=0.32, height=0.3)
            g.set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
            g.move_to(RIGHT * x + UP * 1.4)
            gap_covers.add(g)
        gap_covers2 = VGroup()
        for x in gap_positions:
            g = Rectangle(width=0.32, height=0.3)
            g.set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
            g.move_to(RIGHT * x + UP * 0.55)
            gap_covers2.add(g)

        # Vessel label
        vessel_label = SerifLabel("leaky tumor vessel", TEAL, size=24)
        vessel_label.move_to(LEFT * 4.0 + UP * 1.0)

        # Nanoparticles inside vessel (blood side)
        np_blood = VGroup(*[_np_dot(TEAL) for _ in range(8)])
        positions_blood = [
            LEFT * 2.8 + UP * 0.97,
            LEFT * 1.5 + UP * 0.97,
            LEFT * 0.2 + UP * 0.97,
            RIGHT * 1.1 + UP * 0.97,
            RIGHT * 2.4 + UP * 0.97,
            LEFT * 3.5 + UP * 0.97,
            RIGHT * 3.2 + UP * 0.97,
            LEFT * 0.9 + UP * 0.97,
        ]
        for dot, pos in zip(np_blood, positions_blood):
            dot.move_to(pos)

        # Nanoparticles in tissue (below vessel)
        np_tissue = VGroup(*[_np_dot(TEAL) for _ in range(12)])
        tissue_positions = [
            LEFT * 2.5 + DOWN * 0.2,
            LEFT * 1.2 + DOWN * 0.5,
            LEFT * 0.1 + DOWN * 0.3,
            RIGHT * 1.0 + DOWN * 0.6,
            RIGHT * 2.2 + DOWN * 0.2,
            LEFT * 3.0 + DOWN * 0.8,
            RIGHT * 3.0 + DOWN * 0.5,
            LEFT * 1.8 + DOWN * 1.0,
            LEFT * 0.6 + DOWN * 1.2,
            RIGHT * 0.5 + DOWN * 1.1,
            RIGHT * 1.8 + DOWN * 0.9,
            LEFT * 0.5 + DOWN * 0.7,
        ]
        for dot, pos in zip(np_tissue, tissue_positions):
            dot.move_to(pos)

        # EPR label
        epr_chip = LabelChip("EPR effect", accent=TEAL, size=26)
        epr_chip.move_to(UP * 2.6)

        # Accumulation arrow (downward from vessel)
        acc_arrow = Arrow(UP * 0.1, DOWN * 1.5, color=TEAL,
                          stroke_width=3, buff=0.0,
                          max_tip_length_to_length_ratio=0.12)
        acc_arrow.move_to(RIGHT * 4.5 + DOWN * 0.5)

        self.play(
            Create(top_wall), Create(bot_wall), run_time=0.8
        )
        self.play(FadeIn(gap_covers), FadeIn(gap_covers2), run_time=0.4)
        self.play(FadeIn(vessel_label, shift=RIGHT * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.8) for d in np_blood],
                        lag_ratio=0.05),
            run_time=0.9
        )
        self.play(FadeIn(epr_chip, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.8) for d in np_tissue],
                        lag_ratio=0.04),
            Create(acc_arrow),
            run_time=1.2
        )
        self.wait(max(0.3, total - 4.3))


class B07_DesmoplasiaSqueeze(Scene):
    """THE MECHANISM — desmoplastic stroma compresses vessel cross-section."""

    def construct(self):
        total = DUR["B07"]

        # Open vessel (before compression) — left side
        vessel_open = RoundedRectangle(width=2.2, height=1.6, corner_radius=0.4)
        vessel_open.set_fill(GROUND, 1).set_stroke(CRIMSON, 3)
        vessel_open.move_to(LEFT * 2.5 + UP * 0.4)

        open_label = SerifLabel("open lumen", TEAL, size=22)
        open_label.next_to(vessel_open, DOWN, buff=0.25)

        # Nanoparticles entering open vessel
        np_open = VGroup(*[_np_dot(TEAL) for _ in range(5)])
        open_positions = [
            LEFT * 2.5 + UP * 0.4,
            LEFT * 2.1 + UP * 0.7,
            LEFT * 2.9 + UP * 0.1,
            LEFT * 2.3 + UP * 0.1,
            LEFT * 2.7 + UP * 0.7,
        ]
        for dot, pos in zip(np_open, open_positions):
            dot.move_to(pos)

        # Arrow in middle
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.9, color=INK,
                      stroke_width=3, buff=0.1,
                      max_tip_length_to_length_ratio=0.18)
        arrow.move_to(UP * 0.4)

        # Compressed vessel (right side)
        vessel_compressed = RoundedRectangle(width=2.2, height=0.3, corner_radius=0.1)
        vessel_compressed.set_fill(GROUND, 1).set_stroke(CRIMSON, 3)
        vessel_compressed.move_to(RIGHT * 2.5 + UP * 0.4)

        compressed_label = SerifLabel("compressed lumen", CRIMSON, size=22)
        compressed_label.next_to(vessel_compressed, DOWN, buff=0.5)

        # Fiber lines surrounding the compressed vessel
        fiber_starts_ends = [
            (RIGHT * 1.1 + UP * 1.2, RIGHT * 1.7 + UP * 0.55),
            (RIGHT * 3.9 + UP * 1.2, RIGHT * 3.3 + UP * 0.55),
            (RIGHT * 1.3 + DOWN * 0.4, RIGHT * 1.9 + UP * 0.25),
            (RIGHT * 3.7 + DOWN * 0.4, RIGHT * 3.1 + UP * 0.25),
            (RIGHT * 2.0 + UP * 1.3, RIGHT * 2.5 + UP * 0.55),
            (RIGHT * 3.0 + UP * 1.3, RIGHT * 2.5 + UP * 0.55),
            (RIGHT * 2.0 + DOWN * 0.5, RIGHT * 2.5 + UP * 0.25),
            (RIGHT * 3.0 + DOWN * 0.5, RIGHT * 2.5 + UP * 0.25),
        ]
        fibers = VGroup(*[_fiber_line(s, e) for s, e in fiber_starts_ends])

        # Stroma label
        stroma_chip = LabelChip("desmoplastic stroma", accent=CRIMSON, size=22)
        stroma_chip.move_to(RIGHT * 2.5 + UP * 2.5)

        # Nanoparticles blocked — pile up outside compressed vessel
        np_blocked = VGroup(*[_np_dot(CRIMSON) for _ in range(5)])
        blocked_positions = [
            RIGHT * 0.8 + UP * 0.4,
            RIGHT * 0.6 + UP * 0.0,
            RIGHT * 0.6 + UP * 0.8,
            RIGHT * 0.3 + UP * 0.4,
            RIGHT * 0.4 + DOWN * 0.2,
        ]
        for dot, pos in zip(np_blocked, blocked_positions):
            dot.move_to(pos)

        self.play(FadeIn(vessel_open, shift=RIGHT * 0.3),
                  FadeIn(open_label), run_time=0.8)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.9) for d in np_open], lag_ratio=0.08),
            run_time=0.7
        )
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(stroma_chip, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[Create(f) for f in fibers], lag_ratio=0.08),
            run_time=1.0
        )
        self.play(FadeIn(vessel_compressed), FadeIn(compressed_label), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.9) for d in np_blocked], lag_ratio=0.08),
            run_time=0.6
        )
        self.wait(max(0.3, total - 4.9))


class B08_PressureFlow(Scene):
    """THE MECHANISM — high interstitial pressure pushes particles outward."""

    def construct(self):
        total = DUR["B08"]

        # Tumor boundary — crimson circle
        tumor = Circle(radius=1.8)
        tumor.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 3)
        tumor.move_to(ORIGIN)

        tumor_label = SerifLabel("human solid tumor", CRIMSON, size=22)
        tumor_label.move_to(ORIGIN)

        # Outward pressure arrows radiating from center
        angles = [0, 45, 90, 135, 180, 225, 270, 315]
        pressure_arrows = VGroup()
        for angle in angles:
            import numpy as np
            rad = angle * np.pi / 180
            start = np.array([np.cos(rad) * 0.5, np.sin(rad) * 0.5, 0])
            end = np.array([np.cos(rad) * 2.1, np.sin(rad) * 2.1, 0])
            arr = Arrow(start, end, color=CRIMSON,
                        stroke_width=2.5, buff=0.0,
                        max_tip_length_to_length_ratio=0.2)
            pressure_arrows.add(arr)

        pressure_chip = LabelChip("high interstitial pressure", accent=CRIMSON, size=22)
        pressure_chip.move_to(UP * 3.2)

        # Nanoparticles approaching from outside, deflected
        np_approach = VGroup(*[_np_dot(TEAL) for _ in range(6)])
        approach_positions = [
            RIGHT * 3.2 + UP * 0.0,
            RIGHT * 2.5 + UP * 1.8,
            LEFT * 3.2 + UP * 0.5,
            LEFT * 2.8 + DOWN * 1.5,
            RIGHT * 1.5 + DOWN * 2.5,
            RIGHT * 3.0 + DOWN * 1.2,
        ]
        for dot, pos in zip(np_approach, approach_positions):
            dot.move_to(pos)

        # X marks showing particles blocked
        blocked_marks = VGroup()
        for pos in approach_positions:
            x_line1 = Line(pos + LEFT * 0.12 + UP * 0.12,
                           pos + RIGHT * 0.12 + DOWN * 0.12,
                           color=CRIMSON, stroke_width=3)
            x_line2 = Line(pos + RIGHT * 0.12 + UP * 0.12,
                           pos + LEFT * 0.12 + DOWN * 0.12,
                           color=CRIMSON, stroke_width=3)
            blocked_marks.add(x_line1, x_line2)

        self.play(Create(tumor), run_time=0.8)
        self.play(FadeIn(tumor_label), run_time=0.5)
        self.play(FadeIn(pressure_chip, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[GrowArrow(a) for a in pressure_arrows], lag_ratio=0.06),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.9) for d in np_approach], lag_ratio=0.08),
            run_time=0.7
        )
        self.play(
            LaggedStart(*[Create(m) for m in blocked_marks], lag_ratio=0.05),
            run_time=0.7
        )
        self.wait(max(0.3, total - 4.4))


class B09_SectionCard(Scene):
    """THE MECHANISM section card — core contrast stated."""

    def construct(self):
        total = DUR["B09"]
        line1 = Text("The mouse model runs EPR", font=DISPLAY, color=TEAL,
                     font_size=30, weight=BOLD)
        line2 = Text("at maximum.", font=DISPLAY, color=TEAL,
                     font_size=30, weight=BOLD)
        line3 = Text("Patients run EPR at variable —", font=DISPLAY, color=CRIMSON,
                     font_size=30, weight=BOLD)
        line4 = Text("and often low.", font=DISPLAY, color=CRIMSON,
                     font_size=30, weight=BOLD)
        block = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.22)
        block.move_to(ORIGIN)
        div = Line(LEFT * 5.5, RIGHT * 5.5, color=SLATE, stroke_width=1.5)
        div.move_to(UP * 0.0)
        self.play(FadeIn(VGroup(line1, line2)), Create(div), run_time=1.0)
        self.play(FadeIn(VGroup(line3, line4)), run_time=0.8)
        self.wait(max(0.3, total - 1.8))


class B10_ModelVsPatient(Scene):
    """THE IMPLICATION — EPR spectrum: mouse at maximum, patients scattered."""

    def construct(self):
        total = DUR["B10"]
        import numpy as np

        # Spectrum bar
        bar = Rectangle(width=11.0, height=0.5)
        bar.set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        bar.move_to(UP * 0.5)

        # End labels
        left_label = LabelChip("EPR maximum", accent=TEAL, size=22)
        left_label.move_to(LEFT * 5.1 + UP * 1.5)
        right_label = LabelChip("EPR near-zero", accent=CRIMSON, size=22)
        right_label.move_to(RIGHT * 5.1 + UP * 1.5)

        # Mouse dot — far left
        mouse_dot = Circle(radius=0.18)
        mouse_dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        mouse_dot.move_to(LEFT * 4.8 + UP * 0.5)
        mouse_label = SerifLabel("mouse model", TEAL, size=22)
        mouse_label.next_to(mouse_dot, DOWN, buff=0.35)

        # Patient dots — scattered in middle and right
        patient_xs = [-1.5, 0.3, 1.8, 3.2, -0.5, 2.6, -2.0, 1.0, 4.0, 0.8]
        patient_dots = VGroup()
        for x in patient_xs:
            d = Circle(radius=0.13)
            d.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * x + UP * 0.5)
            patient_dots.add(d)

        patient_label = SerifLabel("patient tumors", CRIMSON, size=22)
        patient_label.move_to(RIGHT * 1.5 + DOWN * 0.7)

        # Gap annotation
        gap_brace = Brace(VGroup(mouse_dot, patient_dots), DOWN, color=INK)
        gap_text = SerifLabel("EPR gap", INK, size=24)
        gap_text.next_to(gap_brace, DOWN, buff=0.15)

        self.play(FadeIn(bar, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.6)
        self.play(FadeIn(mouse_dot, scale=1.2), FadeIn(mouse_label), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.85) for d in patient_dots],
                        lag_ratio=0.07),
            FadeIn(patient_label),
            run_time=1.1
        )
        self.play(FadeIn(gap_brace), FadeIn(gap_text), run_time=0.7)
        self.wait(max(0.3, total - 3.8))


class B11_LiverDefault(Scene):
    """THE IMPLICATION — nanoparticles routing to liver instead of tumor."""

    def construct(self):
        total = DUR["B11"]

        # Body silhouette — simple oval for torso
        body = Ellipse(width=3.2, height=5.5)
        body.set_fill(GROUND, 0.0).set_stroke(INK, 1.5)
        body.set_stroke(opacity=0.4)
        body.move_to(ORIGIN)

        # Liver — large rectangle on right side of body
        liver = RoundedRectangle(width=2.4, height=1.4, corner_radius=0.35)
        liver.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.5)
        liver.move_to(RIGHT * 0.5 + UP * 0.6)

        liver_chip = LabelChip("liver", accent=CRIMSON, size=24)
        liver_chip.next_to(liver, RIGHT, buff=0.2)

        # Tumor — small circle off to upper left
        tumor = Circle(radius=0.4)
        tumor.set_fill(TEAL, 0.2).set_stroke(TEAL, 2)
        tumor.move_to(LEFT * 2.8 + UP * 1.2)

        tumor_chip = LabelChip("tumor", accent=TEAL, size=22)
        tumor_chip.next_to(tumor, UP, buff=0.15)

        # Injection point — entry from right
        entry_point = UP * 2.8 + RIGHT * 5.5

        # Many arrows flowing to liver
        liver_flows = VGroup()
        liver_targets = [
            liver.get_right() + UP * 0.3 + RIGHT * 0.3,
            liver.get_right() + DOWN * 0.1 + RIGHT * 0.5,
            liver.get_top() + UP * 0.4,
        ]
        for tgt in liver_targets:
            arr = Arrow(entry_point, tgt, color=CRIMSON,
                        stroke_width=2.5, buff=0.1,
                        max_tip_length_to_length_ratio=0.12)
            liver_flows.add(arr)

        # One thin trickle to tumor
        tumor_flow = Arrow(entry_point, tumor.get_right() + RIGHT * 0.15,
                           color=TEAL, stroke_width=1.5, buff=0.1,
                           max_tip_length_to_length_ratio=0.18)

        # Labels
        most_label = SerifLabel("most particles", CRIMSON, size=22)
        most_label.move_to(RIGHT * 5.2 + UP * 1.4)
        few_label = SerifLabel("few particles", TEAL, size=20)
        few_label.move_to(RIGHT * 4.8 + DOWN * 0.5)

        self.play(FadeIn(body, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(liver), FadeIn(liver_chip), run_time=0.5)
        self.play(FadeIn(tumor), FadeIn(tumor_chip), run_time=0.5)
        self.play(
            LaggedStart(*[GrowArrow(a) for a in liver_flows], lag_ratio=0.12),
            FadeIn(most_label),
            run_time=1.0
        )
        self.play(GrowArrow(tumor_flow), FadeIn(few_label), run_time=0.8)
        self.wait(max(0.3, total - 3.4))


class B12_TwoTumors_Left(Scene):
    """THE EXAMPLE — left panel: mouse xenograft cross-section.
    Wide fenestrations (200 nm illustrative), particles streaming in, 8% ID/g."""

    def construct(self):
        total = DUR["B12"]

        # Title
        title = LabelChip("Mouse xenograft", accent=TEAL, size=24)
        title.move_to(UP * 3.2)

        # Tumor boundary
        boundary = Rectangle(width=6.0, height=5.2)
        boundary.set_fill(GROUND, 0.0).set_stroke(TEAL, 2.5)
        boundary.move_to(DOWN * 0.2)

        # Blood vessels — open circles with visible lumens
        v1 = Circle(radius=0.55)
        v1.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        v1.move_to(LEFT * 1.6 + UP * 1.2)

        v2 = Circle(radius=0.45)
        v2.set_fill(GROUND, 1).set_stroke(TEAL, 2.5)
        v2.move_to(RIGHT * 1.5 + UP * 0.5)

        # Fenestration gaps (small open notches on vessel walls)
        # Show as small dots on the rim of the circles
        fen_label = SerifLabel("200 nm gaps", TEAL, size=19)
        fen_label.next_to(v1, LEFT, buff=0.2)

        # Nanoparticle dots streaming from vessels into tissue
        tissue_np = VGroup(*[_np_dot(TEAL) for _ in range(18)])
        tissue_positions = [
            LEFT * 0.5 + UP * 0.8,
            LEFT * 1.0 + UP * 0.3,
            LEFT * 2.0 + UP * 0.7,
            RIGHT * 0.3 + UP * 0.2,
            RIGHT * 0.8 + DOWN * 0.3,
            LEFT * 0.2 + DOWN * 0.5,
            LEFT * 1.8 + DOWN * 0.3,
            RIGHT * 1.8 + UP * 1.0,
            RIGHT * 2.3 + DOWN * 0.5,
            LEFT * 2.4 + UP * 0.1,
            RIGHT * 0.5 + DOWN * 1.2,
            LEFT * 0.9 + DOWN * 1.4,
            RIGHT * 2.0 + DOWN * 1.5,
            LEFT * 2.2 + DOWN * 1.6,
            RIGHT * 1.1 + DOWN * 1.8,
            LEFT * 0.3 + DOWN * 1.9,
            LEFT * 1.5 + DOWN * 2.1,
            RIGHT * 0.7 + DOWN * 2.3,
        ]
        for dot, pos in zip(tissue_np, tissue_positions):
            dot.move_to(pos)

        # Accumulation chip
        accum_chip = LabelChip("8% ID/g", accent=TEAL, size=26)
        accum_chip.move_to(DOWN * 2.8)

        illus_note = Text("(illustrative)", font=SERIF, color=INK,
                          font_size=18, slant=ITALIC)
        illus_note.next_to(accum_chip, RIGHT, buff=0.2)

        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        self.play(Create(boundary), run_time=0.8)
        self.play(FadeIn(v1), FadeIn(v2), run_time=0.6)
        self.play(FadeIn(fen_label, shift=RIGHT * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.85) for d in tissue_np],
                        lag_ratio=0.04),
            run_time=1.2
        )
        self.play(FadeIn(accum_chip, scale=1.1), FadeIn(illus_note), run_time=0.6)
        self.wait(max(0.3, total - 4.2))


class B13_TwoTumors_Right(Scene):
    """THE EXAMPLE — right panel: human desmoplastic tumor cross-section.
    Compressed vessels, particles blocked, 0.3% ID/g. Bracket: same chemistry."""

    def construct(self):
        total = DUR["B13"]

        # Title
        title = LabelChip("Human desmoplastic tumor", accent=CRIMSON, size=22)
        title.move_to(UP * 3.2)

        # Tumor boundary
        boundary = Rectangle(width=6.0, height=5.2)
        boundary.set_fill(GROUND, 0.0).set_stroke(CRIMSON, 2.5)
        boundary.move_to(DOWN * 0.2)

        # Compressed vessels — very flat ellipses
        v1 = Ellipse(width=1.6, height=0.22)
        v1.set_fill(GROUND, 1).set_stroke(CRIMSON, 2)
        v1.move_to(LEFT * 1.6 + UP * 1.2)

        v2 = Ellipse(width=1.2, height=0.18)
        v2.set_fill(GROUND, 1).set_stroke(CRIMSON, 2)
        v2.move_to(RIGHT * 1.5 + UP * 0.5)

        # Fibrous stroma lines across the tumor
        fiber_coords = [
            (LEFT * 2.8 + UP * 0.2, RIGHT * 0.5 + UP * 0.9),
            (LEFT * 3.0 + DOWN * 0.5, RIGHT * 1.2 + UP * 0.2),
            (LEFT * 1.0 + UP * 2.0, RIGHT * 2.5 + DOWN * 0.8),
            (LEFT * 2.5 + DOWN * 1.5, RIGHT * 2.8 + DOWN * 0.2),
            (LEFT * 0.5 + DOWN * 0.8, RIGHT * 2.8 + DOWN * 1.8),
            (LEFT * 2.8 + DOWN * 2.5, RIGHT * 1.5 + DOWN * 1.0),
        ]
        fibers = VGroup(*[
            Line(s, e, color=CRIMSON, stroke_width=2.5)
            for s, e in fiber_coords
        ])

        stroma_label = SerifLabel("dense stromal fibers", CRIMSON, size=20)
        stroma_label.move_to(LEFT * 0.3 + DOWN * 1.5)

        # Nanoparticles piling up OUTSIDE tumor boundary
        blocked_np = VGroup(*[_np_dot(CRIMSON, r=0.07) for _ in range(8)])
        blocked_positions = [
            LEFT * 3.6 + UP * 0.5,
            LEFT * 3.6 + UP * 0.0,
            LEFT * 3.6 + UP * 1.0,
            LEFT * 3.6 + DOWN * 0.5,
            LEFT * 3.8 + UP * 0.25,
            LEFT * 3.8 + DOWN * 0.25,
            LEFT * 3.4 + UP * 0.7,
            LEFT * 3.4 + DOWN * 0.2,
        ]
        for dot, pos in zip(blocked_np, blocked_positions):
            dot.move_to(pos)

        blocked_label = SerifLabel("particles blocked", CRIMSON, size=20)
        blocked_label.move_to(LEFT * 4.5 + DOWN * 1.0)

        # Accumulation chip — very small
        accum_chip = LabelChip("0.3% ID/g", accent=CRIMSON, size=26)
        accum_chip.move_to(DOWN * 2.8)

        illus_note = Text("(illustrative)", font=SERIF, color=INK,
                          font_size=18, slant=ITALIC)
        illus_note.next_to(accum_chip, RIGHT, buff=0.2)

        # Same chemistry annotation at bottom — inside safe area (±3.4 y)
        same_chip = LabelChip("same chemistry -- interpatient EPR variability",
                              accent=SLATE, size=18)
        same_chip.move_to(DOWN * 3.1)

        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        self.play(Create(boundary), run_time=0.8)
        self.play(FadeIn(v1), FadeIn(v2), run_time=0.5)
        self.play(
            LaggedStart(*[Create(f) for f in fibers], lag_ratio=0.08),
            run_time=1.0
        )
        self.play(FadeIn(stroma_label, shift=RIGHT * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.85) for d in blocked_np], lag_ratio=0.06),
            FadeIn(blocked_label),
            run_time=0.9
        )
        self.play(FadeIn(accum_chip, scale=1.1), FadeIn(illus_note), run_time=0.6)
        self.play(FadeIn(same_chip, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 4.9))


class B14_End(Scene):
    """RECAP endcard — question answered, topic named (outro law owns the tail)."""

    def construct(self):
        total = DUR["B14"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The mouse model runs EPR at maximum.", font=DISPLAY, color=TEAL,
                  font_size=26, weight=BOLD)
        t2 = Text("The patient runs EPR at real —", font=DISPLAY, color=CRIMSON,
                  font_size=26, weight=BOLD)
        t3 = Text("compressed, fibrous, variable.", font=DISPLAY, color=CRIMSON,
                  font_size=26, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        sub = Text("Same nanoparticle. Different biological world.", font=SERIF,
                   color=INK, font_size=24)
        sub.next_to(u, DOWN, buff=0.45)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(VGroup(t2, t3)), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.7))
