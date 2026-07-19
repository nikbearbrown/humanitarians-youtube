"""vox_scenes.py — Why the Warburg Tumor Lights Up on a PET Scan
(vox-fdg-hif1a, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 is the only STILL (ai media slot) and has no scene here.
Durations read from this reel's beat_sheet.json (actuals after audio lock;
estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-fdg-hif1a

Color law: TEAL #1F6F5C = glucose uptake / GLUT transporters / HIF-1alpha
active / accumulation (the mechanism working). CRIMSON #BF3339 = FDG trapped /
blocked pathways / PHD stalled (the obstruction). GOLD = highlighter fill
only, never text. Never swap mid-film.

Exclusions honored: NO VHL/clear cell RCC, NO Warburg carbon-allocation
argument, NO IDH/succinate PHD inhibition, NO FDG-negative tumors beyond
one sentence (B13), NO scanner physics beyond functional description.

Gate B convention: every zero-width stroke is also zero-opacity.
Single-method .animate only (no chaining).
"""
import sys
import json
import pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] /
    "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# ---------------------------------------------------------------- DUR dict

DUR = {
    "B01": 11.0, "B03": 10.0, "B04": 11.0, "B05": 11.0,
    "B06": 13.0, "B07": 12.0, "B08": 13.0, "B09": 11.0,
    "B10": 13.0, "B11": 12.0, "B12": 13.0, "B13": 12.0,
}
try:
    _BS = json.load(
        open(pathlib.Path(__file__).with_name("beat_sheet.json"))
    )
    DUR.update({
        b["beat_id"]: float(
            b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0
        )
        for b in _BS["beats"]
    })
except Exception:
    pass

# ---------------------------------------------------------------- helpers

def _bar(height_units, color, w=0.9, scale_y=1.0):
    """A filled rectangle bar rising from bottom, height proportional to
    height_units. scale_y converts units to Manim units."""
    h = height_units * scale_y
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return r


def _cascade_box(label_text, accent=TEAL, w=4.2, h=0.72):
    """A rounded cascade step box: accent fill, white Montserrat label."""
    box = RoundedRectangle(width=w, height=h, corner_radius=0.12)
    box.set_fill(accent, 1).set_stroke(width=0, opacity=0)
    lbl = Text(label_text.upper(), font=DISPLAY, color=WHITE,
               font_size=24, weight="MEDIUM")
    if lbl.width > w * 0.88:
        lbl.scale_to_fit_width(w * 0.88)
    lbl.move_to(box)
    return VGroup(box, lbl)


def _x_mark(center, color=CRIMSON, size=0.38):
    """A bold X mark for 'blocked'."""
    d = size / 2
    l1 = Line(center + UL * d, center + DR * d,
              color=color, stroke_width=6)
    l2 = Line(center + UR * d, center + DL * d,
              color=color, stroke_width=6)
    return VGroup(l1, l2)


def _arrow_down(start, length=0.5, color=INK):
    return Arrow(start, start + DOWN * length, color=color,
                 stroke_width=3, tip_length=0.18, buff=0)


def _small_chip(text, accent=TEAL, size=20):
    """Small LabelChip wrapper."""
    return LabelChip(text, accent=accent, size=size)


def _cell_outline(center, w=2.6, h=2.6, color=INK):
    """An oval cell membrane outline."""
    e = Ellipse(width=w, height=h)
    e.set_stroke(color, 2.5).set_fill(opacity=0)
    e.move_to(center)
    return e


def _glut_chip(center, color=TEAL, size=18):
    chip = LabelChip("GLUT1", accent=color, size=size)
    chip.move_to(center)
    return chip


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """CARD — title beat. TEAL eyebrow 'CANCER BIOLOGY', GOLD fill only."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=26, weight="MEDIUM")
        t1 = Text("Why the Warburg Tumor", font=DISPLAY, color=INK,
                  font_size=48, weight="BOLD")
        t2 = Text("Lights Up on a PET Scan", font=DISPLAY, color=INK,
                  font_size=48, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        eye.next_to(block, UP, buff=0.65)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_QuestionCard(Scene):
    """CARD — THE QUESTION beat, on screen."""
    def construct(self):
        total = DUR["B03"]
        q_label = Text("THE QUESTION", font=DISPLAY, color=CRIMSON,
                       font_size=22, weight="MEDIUM")
        q1 = Text("Why do cancer cells consume", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        q2 = Text("so much more glucose", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        q3 = Text("than their neighbors?", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.14).move_to(UP * 0.1)
        u = Line(q3.get_corner(DL) + DOWN * 0.16,
                 q3.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        q_label.next_to(block, UP, buff=0.6)
        sub = Text("normal and tumor lymph nodes look identical on CT",
                   font=SERIF, color=INK, font_size=24, slant=ITALIC)
        sub.set_opacity(0.7).next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(q_label), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


class B04_ATPComparison(Scene):
    """GRAPHIC — 2 ATP vs 30 ATP bar comparison. The naive expectation fails."""
    def construct(self):
        total = DUR["B04"]
        # scale: 30 units -> 5.0 Manim units; 2 units -> 0.33 Manim units
        SCALE = 5.0 / 30.0

        cancer_h = 2 * SCALE
        full_h = 30 * SCALE

        cancer_bar = _bar(2, TEAL, w=1.2, scale_y=SCALE)
        full_bar = _bar(30, INK, w=1.2, scale_y=SCALE)

        # place bars on a baseline at y = -2.0
        base_y = -2.0
        cancer_bar.move_to(
            LEFT * 2.5 + UP * (base_y + cancer_h / 2)
        )
        full_bar.move_to(
            RIGHT * 2.5 + UP * (base_y + full_h / 2)
        )

        baseline = Line(LEFT * 4.5 + UP * base_y,
                        RIGHT * 4.5 + UP * base_y,
                        color=INK, stroke_width=2)

        # labels above bars
        cancer_val = Text("2", font=DISPLAY, color=TEAL,
                          font_size=56, weight="BOLD")
        cancer_val.next_to(cancer_bar, UP, buff=0.18)

        full_val = Text("30", font=DISPLAY, color=INK,
                        font_size=56, weight="BOLD")
        full_val.next_to(full_bar, UP, buff=0.18)

        cancer_lbl = SerifLabel("cancer cell glycolysis", TEAL, size=22)
        cancer_lbl.next_to(cancer_bar, DOWN, buff=0.22)

        full_lbl = SerifLabel("complete oxidation", SLATE, size=22)
        full_lbl.next_to(full_bar, DOWN, buff=0.22)

        unit_lbl = Text("ATP per glucose", font=SERIF, color=INK,
                        font_size=22, slant=ITALIC).set_opacity(0.6)
        unit_lbl.move_to(UP * 3.2)

        self.play(Create(baseline), run_time=0.4)
        self.play(
            GrowFromEdge(cancer_bar, DOWN),
            FadeIn(cancer_lbl),
            run_time=0.8
        )
        self.play(FadeIn(cancer_val, scale=0.85), run_time=0.5)
        self.play(
            GrowFromEdge(full_bar, DOWN),
            FadeIn(full_lbl),
            run_time=1.0
        )
        self.play(FadeIn(full_val, scale=0.85), run_time=0.5)
        self.play(FadeIn(unit_lbl), run_time=0.4)
        self.wait(max(0.5, total - 3.6))


class B05_MechanismCard(Scene):
    """CARD — section card introducing THE MECHANISM."""
    def construct(self):
        total = DUR["B05"]
        sec = Text("THE MECHANISM", font=DISPLAY, color=TEAL,
                   font_size=28, weight="MEDIUM")
        sub = Text("HIF-1α: the oxygen sensor", font=SERIF, color=INK,
                   font_size=40, weight=BOLD)
        u = Line(sub.get_corner(DL) + DOWN * 0.16,
                 sub.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        block = VGroup(sub, u).arrange(DOWN, buff=0.0).move_to(UP * 0.05)
        sec.next_to(block, UP, buff=0.65)
        self.play(FadeIn(sec), run_time=0.5)
        self.play(FadeIn(block), run_time=0.9)
        self.wait(max(0.5, total - 1.4))


class B06_NormoxiaCascade(Scene):
    """GRAPHIC — normoxia: PHD -> VHL -> proteasome -> HIF-1alpha gone."""
    def construct(self):
        total = DUR["B06"]
        # Four cascade boxes, top to bottom, with arrows
        steps = [
            ("PHD active (O2 present)", TEAL),
            ("HIF-1α hydroxylated", TEAL),
            ("VHL recognizes tag", TEAL),
            ("proteasome destroys HIF-1α", TEAL),
        ]
        boxes = VGroup(*[_cascade_box(s, color) for s, color in steps])
        boxes.arrange(DOWN, buff=0.38).move_to(LEFT * 1.8 + DOWN * 0.1)

        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a = _arrow_down(
                boxes[i].get_bottom() + DOWN * 0.05,
                length=0.25, color=INK
            )
            arrows.add(a)

        absent_label = LabelChip("HIF-1α: absent", accent=SLATE, size=24)
        absent_label.next_to(boxes[-1], RIGHT, buff=0.8)

        half_life = Text("half-life ~5 min", font=SERIF, color=INK,
                         font_size=22, slant=ITALIC).set_opacity(0.65)
        half_life.next_to(absent_label, DOWN, buff=0.25)

        title = Text("Normoxia", font=DISPLAY, color=INK,
                     font_size=28, weight="MEDIUM")
        title.next_to(boxes, UP, buff=0.4)

        self.play(FadeIn(title), run_time=0.4)
        for i, (box, _) in enumerate(zip(boxes, steps)):
            self.play(GrowFromEdge(box, UP), run_time=0.55)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.25)
        self.play(FadeIn(absent_label, scale=0.9),
                  FadeIn(half_life), run_time=0.7)
        self.wait(max(0.5, total - 0.4 - 4 * 0.55 - 3 * 0.25 - 0.7))


class B07_HypoxiaCascade(Scene):
    """GRAPHIC — hypoxia: PHD stalls, HIF-1alpha escapes, enters nucleus."""
    def construct(self):
        total = DUR["B07"]
        # Step 1: PHD stalled (CRIMSON)
        phd_box = _cascade_box("PHD stalled — no O2", CRIMSON)
        # Step 2: HIF-1alpha NOT tagged (shown struck)
        escape_box = _cascade_box("HIF-1α escapes VHL", TEAL)
        # Step 3: accumulation
        accum_box = _cascade_box("HIF-1α accumulates", TEAL)
        # Step 4: nucleus
        nucleus_box = _cascade_box("enters nucleus", TEAL)

        boxes = VGroup(phd_box, escape_box, accum_box, nucleus_box)
        boxes.arrange(DOWN, buff=0.38).move_to(LEFT * 1.8 + DOWN * 0.1)

        arrows = VGroup()
        for i in range(len(boxes) - 1):
            a = _arrow_down(
                boxes[i].get_bottom() + DOWN * 0.05,
                length=0.25, color=INK
            )
            arrows.add(a)

        title = Text("Hypoxia", font=DISPLAY, color=CRIMSON,
                     font_size=28, weight="MEDIUM")
        title.next_to(boxes, UP, buff=0.4)

        # "drives transcription" label beside nucleus box
        drives_lbl = LabelChip("drives transcription", accent=TEAL, size=22)
        drives_lbl.next_to(nucleus_box, RIGHT, buff=0.7)

        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromEdge(phd_box, UP), run_time=0.55)
        self.play(Create(arrows[0]), run_time=0.25)
        self.play(GrowFromEdge(escape_box, UP), run_time=0.55)
        self.play(Create(arrows[1]), run_time=0.25)
        self.play(GrowFromEdge(accum_box, UP), run_time=0.55)
        self.play(Create(arrows[2]), run_time=0.25)
        self.play(GrowFromEdge(nucleus_box, UP), run_time=0.55)
        self.play(FadeIn(drives_lbl, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 0.4 - 4 * 0.55 - 3 * 0.25 - 0.6))


class B08_HIF1aTargets(Scene):
    """GRAPHIC — HIF-1alpha in nucleus fans to GLUT1, GLUT3, HK2 targets."""
    def construct(self):
        total = DUR["B08"]
        # Central HIF-1alpha box
        hif_box = _cascade_box("HIF-1α (nucleus)", TEAL, w=3.8, h=0.8)
        hif_box.move_to(LEFT * 2.8 + UP * 0.0)

        # Three target chips to the right
        g1_chip = LabelChip("GLUT1", accent=TEAL, size=26)
        g3_chip = LabelChip("GLUT3", accent=TEAL, size=26)
        hk2_chip = LabelChip("HK2", accent=TEAL, size=26)

        targets = VGroup(g1_chip, g3_chip, hk2_chip)
        targets.arrange(DOWN, buff=0.6).move_to(RIGHT * 2.8)

        # Density annotation under GLUT chips
        density_lbl = Text("5x normal density", font=SERIF, color=INK,
                           font_size=20, slant=ITALIC).set_opacity(0.65)
        density_lbl.next_to(VGroup(g1_chip, g3_chip), DOWN, buff=0.18)

        # Arrows from HIF box to each target
        arrows = VGroup()
        for chip in targets:
            a = Arrow(hif_box.get_right(),
                      chip.get_left() + LEFT * 0.05,
                      color=INK, stroke_width=2.5,
                      tip_length=0.15, buff=0.1)
            arrows.add(a)

        self.play(GrowFromEdge(hif_box, LEFT), run_time=0.7)
        self.play(
            Create(arrows[0]),
            FadeIn(g1_chip, shift=LEFT * 0.3),
            run_time=0.6
        )
        self.play(
            Create(arrows[1]),
            FadeIn(g3_chip, shift=LEFT * 0.3),
            run_time=0.6
        )
        self.play(
            Create(arrows[2]),
            FadeIn(hk2_chip, shift=LEFT * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(density_lbl), run_time=0.5)
        self.wait(max(0.5, total - 0.7 - 3 * 0.6 - 0.5))


class B09_FDGEntry(Scene):
    """GRAPHIC — FDG passing through GLUT1 transporters into cancer cell."""
    def construct(self):
        total = DUR["B09"]
        # Cell membrane as a thick horizontal band
        mem_y = 0.3
        membrane = Rectangle(width=12.0, height=0.55)
        membrane.set_fill(SLATE, 0.18).set_stroke(SLATE, 2)
        membrane.move_to(UP * mem_y)

        mem_lbl = SerifLabel("cell membrane", SLATE, size=22)
        mem_lbl.move_to(LEFT * 5.5 + UP * (mem_y + 0.6))

        # GLUT1 transporter chips along the membrane
        glut_positions = [LEFT * 3.5, LEFT * 0.5, RIGHT * 2.5]
        gluts = VGroup(*[_glut_chip(UP * mem_y + p) for p in glut_positions])

        # "outside" and "inside" labels
        outside_lbl = Text("outside", font=SERIF, color=INK,
                           font_size=22, slant=ITALIC).set_opacity(0.5)
        outside_lbl.move_to(UP * 2.5 + LEFT * 5.5)
        inside_lbl = Text("inside cell", font=SERIF, color=INK,
                          font_size=22, slant=ITALIC).set_opacity(0.5)
        inside_lbl.move_to(DOWN * 1.8 + LEFT * 5.5)

        # FDG molecules arriving from outside (above membrane)
        fdg_color = TEAL
        fdg_start_y = 2.2
        fdg_end_y = -1.5

        fdg1_grp = LabelChip("FDG", accent=fdg_color, size=20)
        fdg1_grp.move_to(LEFT * 3.5 + UP * fdg_start_y)

        fdg2_grp = LabelChip("FDG", accent=fdg_color, size=20)
        fdg2_grp.move_to(LEFT * 0.5 + UP * fdg_start_y)

        # Inside accumulation points (re-positioned below, so declare as chips)
        inside_fdg_pos = LEFT * 3.5 + DOWN * 1.5
        inside_fdg2_pos = LEFT * 0.5 + DOWN * 1.5

        self.play(FadeIn(membrane), FadeIn(mem_lbl),
                  FadeIn(outside_lbl), FadeIn(inside_lbl), run_time=0.7)
        self.play(FadeIn(gluts), run_time=0.6)
        self.play(FadeIn(fdg1_grp), FadeIn(fdg2_grp), run_time=0.5)
        # Move FDG through membrane
        self.play(
            fdg1_grp.animate.move_to(inside_fdg_pos),
            fdg2_grp.animate.move_to(inside_fdg2_pos),
            run_time=1.0
        )
        accum_chip = LabelChip("flooding in", accent=TEAL, size=24)
        accum_chip.move_to(RIGHT * 3.8 + DOWN * 1.5)
        self.play(FadeIn(accum_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.5, total - 0.7 - 0.6 - 0.5 - 1.0 - 0.5))


class B10_HexokinaseTrap(Scene):
    """GRAPHIC — HK2 phosphorylates FDG; two CRIMSON blocked exit paths."""
    def construct(self):
        total = DUR["B10"]
        # Central: FDG + HK2 -> FDG-6-P
        fdg_grp = LabelChip("FDG", accent=TEAL, size=22)
        fdg_grp.move_to(LEFT * 3.2 + UP * 0.5)

        hk2_chip = LabelChip("HK2 phosphorylates", accent=TEAL, size=22)
        hk2_chip.move_to(UP * 0.5)

        fdgp_grp = LabelChip("FDG-6-P", accent=SLATE, size=22)
        fdgp_grp.move_to(RIGHT * 3.2 + UP * 0.5)

        arrow_hk = Arrow(fdg_grp.get_right(),
                         fdgp_grp.get_left() + LEFT * 0.05,
                         color=INK, stroke_width=3, tip_length=0.18, buff=0.12)

        # Blocked exits below FDG-6-P
        exit1_start = fdgp_grp.get_bottom() + DOWN * 0.1
        exit1_arr = Arrow(exit1_start, exit1_start + DOWN * 0.9 + LEFT * 1.2,
                          color=CRIMSON, stroke_width=2.5,
                          tip_length=0.15, buff=0)
        exit1_lbl = Text("glycolysis", font=SERIF, color=CRIMSON,
                         font_size=20, slant=ITALIC)
        exit1_lbl.move_to(exit1_start + DOWN * 1.2 + LEFT * 2.0)

        exit2_arr = Arrow(exit1_start, exit1_start + DOWN * 0.9 + RIGHT * 1.2,
                          color=CRIMSON, stroke_width=2.5,
                          tip_length=0.15, buff=0)
        exit2_lbl = Text("export", font=SERIF, color=CRIMSON,
                         font_size=20, slant=ITALIC)
        exit2_lbl.move_to(exit1_start + DOWN * 1.2 + RIGHT * 2.2)

        x1 = _x_mark(exit1_start + DOWN * 0.55 + LEFT * 0.65, CRIMSON, 0.28)
        x2 = _x_mark(exit1_start + DOWN * 0.55 + RIGHT * 0.65, CRIMSON, 0.28)

        trapped_chip = LabelChip("TRAPPED", accent=CRIMSON, size=28)
        trapped_chip.move_to(RIGHT * 3.2 + DOWN * 2.5)

        self.play(FadeIn(fdg_grp), FadeIn(hk2_chip), run_time=0.6)
        self.play(Create(arrow_hk), run_time=0.5)
        self.play(FadeIn(fdgp_grp), run_time=0.5)
        self.play(
            Create(exit1_arr), FadeIn(exit1_lbl),
            Create(exit2_arr), FadeIn(exit2_lbl),
            run_time=0.8
        )
        self.play(FadeIn(x1), FadeIn(x2), run_time=0.5)
        self.play(FadeIn(trapped_chip, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 0.6 - 0.5 - 0.5 - 0.8 - 0.5 - 0.6))


class B11_Accumulation(Scene):
    """GRAPHIC — FDG-6-P isotype accumulates inside cell; signal ring."""
    def construct(self):
        total = DUR["B11"]
        # Cell outline
        cell = _cell_outline(LEFT * 1.5 + DOWN * 0.2, w=4.5, h=3.8)

        cell_lbl = SerifLabel("cancer cell", TEAL, size=22)
        cell_lbl.next_to(cell, UP, buff=0.22)

        # Grid of small TEAL squares = FDG-6-P molecules accumulating
        n_marks = 20
        marks = VGroup()
        np.random.seed(42)
        for _ in range(n_marks):
            sq = Square(0.22).set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
            # distribute inside the ellipse rough zone
            angle = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(0, 0.72)
            x = np.cos(angle) * r * 1.6
            y = np.sin(angle) * r * 1.2
            sq.move_to(LEFT * 1.5 + DOWN * 0.2 + np.array([x, y, 0]))
            marks.add(sq)

        fdgp_lbl = Text("FDG-6-P", font=DISPLAY, color=TEAL,
                        font_size=20, weight="MEDIUM")
        fdgp_lbl.move_to(LEFT * 1.5 + DOWN * 0.2 + DOWN * 1.4)

        # Signal ring
        signal_ring = Circle(radius=2.6).set_stroke(CRIMSON, 3).set_fill(opacity=0)
        signal_ring.move_to(LEFT * 1.5 + DOWN * 0.2)

        signal_chip = LabelChip("tumor signal", accent=CRIMSON, size=24)
        signal_chip.move_to(RIGHT * 3.5 + DOWN * 0.2)

        self.play(Create(cell), FadeIn(cell_lbl), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(m, scale=0.7) for m in marks],
                        lag_ratio=0.06),
            run_time=2.5
        )
        self.play(FadeIn(fdgp_lbl), run_time=0.4)
        self.play(Create(signal_ring), run_time=0.9)
        self.play(FadeIn(signal_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.5, total - 0.7 - 2.5 - 0.4 - 0.9 - 0.5))


class B12_TwoNodes(Scene):
    """GRAPHIC — EXAMPLE: cancer node vs normal node, FDG accumulation."""
    def construct(self):
        total = DUR["B12"]
        # Two cell outlines
        left_cell = _cell_outline(LEFT * 3.5 + DOWN * 0.1, w=3.8, h=3.2)
        right_cell = _cell_outline(RIGHT * 3.5 + DOWN * 0.1, w=3.8, h=3.2)

        # Headers
        cancer_hdr = LabelChip("cancer node", accent=TEAL, size=22)
        cancer_hdr.next_to(left_cell, UP, buff=0.2)

        normal_hdr = LabelChip("normal node", accent=SLATE, size=22)
        normal_hdr.next_to(right_cell, UP, buff=0.2)

        # GLUT1 chips on cancer cell membrane (many = 5x density)
        glut_cancer = VGroup(*[
            _glut_chip(LEFT * 3.5 + np.array([np.cos(a) * 1.8, np.sin(a) * 1.5, 0]),
                       color=TEAL, size=16)
            for a in np.linspace(0.2, 2 * np.pi - 0.2, 6)
        ])

        # GLUT1 chips on normal cell (fewer)
        glut_normal = VGroup(*[
            _glut_chip(RIGHT * 3.5 + np.array([np.cos(a) * 1.8, np.sin(a) * 1.5, 0]),
                       color=SLATE, size=16)
            for a in np.linspace(0.8, 2 * np.pi - 0.5, 2)
        ])

        # Cancer cell: FDG-6-P accumulating (many teal marks)
        np.random.seed(7)
        cancer_marks = VGroup()
        for _ in range(15):
            sq = Square(0.20).set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
            angle = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(0, 0.65)
            x = np.cos(angle) * r * 1.2
            y = np.sin(angle) * r * 1.0
            sq.move_to(LEFT * 3.5 + DOWN * 0.1 + np.array([x, y, 0]))
            cancer_marks.add(sq)

        # Normal cell: minimal marks
        normal_marks = VGroup()
        for i in range(2):
            sq = Square(0.20).set_fill(SLATE, 0.35).set_stroke(width=0, opacity=0)
            sq.move_to(RIGHT * 3.5 + DOWN * 0.1 + np.array([0.3 * (i - 0.5), 0.2, 0]))
            normal_marks.add(sq)

        # Signal on cancer, quiet on normal
        cancer_signal = Circle(radius=2.2).set_stroke(CRIMSON, 3.5).set_fill(opacity=0)
        cancer_signal.move_to(LEFT * 3.5 + DOWN * 0.1)

        lit_chip = LabelChip("lights up", accent=CRIMSON, size=20)
        lit_chip.next_to(left_cell, DOWN, buff=0.3)

        quiet_chip = LabelChip("stays quiet", accent=SLATE, size=20)
        quiet_chip.next_to(right_cell, DOWN, buff=0.3)

        # Density annotation
        density_lbl = Text("5x GLUT1 density (illustrative)",
                           font=SERIF, color=INK, font_size=19,
                           slant=ITALIC).set_opacity(0.6)
        density_lbl.next_to(cancer_hdr, DOWN, buff=0.05)

        self.play(
            Create(left_cell), Create(right_cell),
            FadeIn(cancer_hdr), FadeIn(normal_hdr),
            run_time=0.8
        )
        self.play(FadeIn(glut_cancer), FadeIn(glut_normal), run_time=0.6)
        self.play(FadeIn(density_lbl), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(m, scale=0.7) for m in cancer_marks],
                        lag_ratio=0.07),
            FadeIn(normal_marks),
            run_time=1.8
        )
        self.play(Create(cancer_signal), run_time=0.8)
        self.play(FadeIn(lit_chip), FadeIn(quiet_chip), run_time=0.6)
        self.wait(max(0.5, total - 0.8 - 0.6 - 0.4 - 1.8 - 0.8 - 0.6))


class B13_End(Scene):
    """CARD — endcard RECAP. Question -> answer. CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B13"]
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                     font_size=24, weight="MEDIUM")
        t1 = Text("HIF-1α — GLUT1 + HK2 — FDG trapped", font=DISPLAY,
                  color=INK, font_size=38, weight="BOLD")
        t2 = Text("tumor lights up.", font=DISPLAY,
                  color=INK, font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=TEAL, stroke_width=2)
        topic.next_to(block, UP, buff=0.65)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))
