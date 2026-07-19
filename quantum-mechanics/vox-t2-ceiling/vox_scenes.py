"""vox_scenes.py — Why Coherence Is Always Shorter Than Twice the Lifetime
(vox-t2-ceiling, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B09 is STILL·ai — no scene (compiles as slate).
B01, B04, B05, B08, B11, B14 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = T2 / coherence / ceiling / best case;
crimson #BF3339 = pure dephasing / gap / T_phi.
Never swap mid-film.

Exclusions: NO Lindblad derivation, NO jump-operator algebra, NO Bloch equations, NO spin-echo.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 11.0, "B03": 11.0, "B04": 10.0,
    "B05": 5.0,  "B06": 13.0, "B07": 12.0, "B08": 5.0,
    "B09": 12.0, "B10": 13.0, "B11": 5.0,  "B12": 12.0,
    "B13": 14.0, "B14": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- helpers ---------------------------------------------------------------

def _bloch_circle_2d(radius=2.0, accent=TEAL, cx=0.0, cy=0.0):
    """A 2D Bloch sphere cross-section centered at (cx, cy)."""
    circ = Circle(radius=radius)
    circ.set_stroke(accent, 2.5).set_fill(GROUND, 0)
    circ.move_to([cx, cy, 0])
    north = Dot(radius=0.08, color=INK).move_to([cx, cy + radius, 0])
    south = Dot(radius=0.08, color=INK).move_to([cx, cy - radius, 0])
    north_lbl = Text("|0>", font=MONO, color=INK, font_size=20)
    north_lbl.move_to([cx + 0.5, cy + radius + 0.18, 0])
    south_lbl = Text("|1>", font=MONO, color=INK, font_size=20)
    south_lbl.move_to([cx + 0.5, cy - radius - 0.18, 0])
    return VGroup(circ, north, south, north_lbl, south_lbl)


# ---- scenes ----------------------------------------------------------------

class B02_T1Definition(Scene):
    def construct(self):
        total = DUR["B02"]

        bloch = _bloch_circle_2d(radius=1.9, accent=SLATE, cx=-2.5, cy=0.0)

        # T1 arrow from north to south
        north_pos = [-2.5, 1.9, 0]
        south_pos = [-2.5, -1.9, 0]

        # Arc sweeping from north to south
        arc_pts = []
        for i in range(50):
            angle = PI / 2 - (i / 49) * PI  # from 90 to -90 deg
            r = 1.9
            arc_pts.append([-2.5 + r * np.cos(angle), r * np.sin(angle), 0])
        t1_arc = VMobject(color=CRIMSON, stroke_width=3)
        t1_arc.set_points_smoothly(arc_pts)

        # Arrow tip at south
        arr = Arrow([-0.6, -0.8, 0], [-2.4, -1.6, 0], color=CRIMSON, stroke_width=3,
                    tip_length=0.18, buff=0.05)

        t1_chip = LabelChip("T1 ENERGY LIFETIME", accent=CRIMSON, size=22)
        t1_chip.move_to([2.5, 0.5, 0])

        t1_lbl = SerifLabel("excited state decays to ground", accent=CRIMSON, size=22)
        t1_lbl.move_to([2.5, -0.6, 0])

        north_label = Text("excited |1>", font=MONO, color=TEAL, font_size=22)
        north_label.move_to([-4.5, 1.7, 0])
        south_label = Text("ground |0>", font=MONO, color=INK, font_size=22)
        south_label.move_to([-4.5, -1.7, 0])

        self.play(Create(bloch), run_time=0.6)
        self.play(FadeIn(north_label), FadeIn(south_label), run_time=0.4)
        self.play(Create(t1_arc), run_time=0.9)
        self.play(FadeIn(t1_chip, scale=0.88), run_time=0.4)
        self.play(FadeIn(t1_lbl, shift=LEFT * 0.2), run_time=0.4)
        self.wait(max(0.5, total - 2.7))


class B03_T2Definition(Scene):
    def construct(self):
        total = DUR["B03"]

        bloch = _bloch_circle_2d(radius=1.9, accent=TEAL, cx=-2.5, cy=0.0)

        # Arrow pointing to equator (right)
        arr = Arrow([-2.5, 0, 0], [-2.5 + 1.9, 0, 0], color=TEAL,
                    stroke_width=4, buff=0, tip_length=0.22)

        # Inward spiral arc
        spiral_pts = []
        for i in range(55):
            t = i / 54
            r = 1.9 * (1 - t * 0.92)
            angle = t * TAU * 0.7
            spiral_pts.append([-2.5 + r * np.cos(angle), r * np.sin(angle), 0])
        spiral = VMobject(color=TEAL, stroke_width=2.5, stroke_opacity=0.7)
        spiral.set_points_smoothly(spiral_pts)

        t2_chip = LabelChip("T2 COHERENCE TIME", accent=TEAL, size=22)
        t2_chip.move_to([2.5, 0.5, 0])

        t2_lbl = SerifLabel("superposition decays inward", accent=TEAL, size=22)
        t2_lbl.move_to([2.5, -0.6, 0])

        eq_label = Text("superposition", font=MONO, color=TEAL, font_size=20)
        eq_label.move_to([-2.5, 2.3, 0])

        center_lbl = Text("classical", font=MONO, color=SLATE, font_size=20)
        center_lbl.move_to([-2.5, -0.4, 0])

        self.play(Create(bloch), run_time=0.6)
        self.play(GrowArrow(arr), FadeIn(eq_label), run_time=0.6)
        self.play(Create(spiral), run_time=0.8)
        self.play(arr.animate.scale(0.08, about_point=[-2.5, 0, 0]), run_time=0.7)
        self.play(FadeIn(center_lbl), run_time=0.3)
        self.play(FadeIn(t2_chip, scale=0.88), run_time=0.4)
        self.play(FadeIn(t2_lbl, shift=LEFT * 0.2), run_time=0.4)
        self.wait(max(0.5, total - 3.8))


class B06_TwoDecays(Scene):
    def construct(self):
        total = DUR["B06"]

        title = Text("Inside the Density Matrix", font=SERIF, color=INK,
                     font_size=26, slant=ITALIC)
        title.move_to(UP * 3.2)

        # 2x2 matrix schematic (just boxes)
        cell_size = 1.4
        # 4 cells at positions (i, j)
        cells = {}
        labels = {(0,0): "rho_00", (0,1): "rho_01", (1,0): "rho_10", (1,1): "rho_11"}
        colors = {(0,0): SLATE, (0,1): TEAL, (1,0): TEAL, (1,1): CRIMSON}
        for r in range(2):
            for c in range(2):
                cx = -1.5 + c * 1.8
                cy = 0.8 - r * 1.8
                box = Rectangle(width=1.5, height=1.3)
                box.set_fill(colors[(r, c)], 0.15).set_stroke(colors[(r, c)], 1.5)
                box.move_to([cx, cy, 0])
                lbl = Text(labels[(r, c)], font=MONO, color=colors[(r, c)], font_size=22)
                lbl.move_to([cx, cy, 0])
                cells[(r, c)] = VGroup(box, lbl)

        # Labels for diagonal/off-diagonal
        pop_lbl = Text("populations", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        pop_lbl.move_to(RIGHT * 3.5 + UP * 0.8)
        coh_lbl = Text("coherences", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        coh_lbl.move_to(RIGHT * 3.5 + DOWN * 0.4)

        # T1 decay arrow on rho_11
        t1_arr = Arrow([0.3, -0.9, 0], [0.3, -2.0, 0], color=CRIMSON,
                       stroke_width=3, tip_length=0.18, buff=0.05)
        t1_arr_lbl = Text("T1 decay", font=SERIF, color=CRIMSON,
                          font_size=20, slant=ITALIC)
        t1_arr_lbl.move_to([0.3, -2.5, 0])

        # Branching from T1 to off-diagonal
        branch = CurvedArrow([-1.5, -0.5, 0], [-1.5, 0.8, 0],
                             color=CRIMSON, stroke_width=2,
                             tip_length=0.15, angle=-TAU / 6)

        ratio_chip = LabelChip("2:1 RATIO", accent=CRIMSON, size=24)
        ratio_chip.move_to(LEFT * 4.0 + UP * 0.2)

        half_lbl = SerifLabel("half the rate", accent=CRIMSON, size=22)
        half_lbl.move_to(LEFT * 4.0 + DOWN * 0.8)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.4)
        for (r, c), cell in cells.items():
            self.play(FadeIn(cell, scale=0.9), run_time=0.25)
        self.play(FadeIn(pop_lbl), FadeIn(coh_lbl), run_time=0.4)
        self.play(GrowArrow(t1_arr), FadeIn(t1_arr_lbl), run_time=0.5)
        self.play(Create(branch), run_time=0.6)
        self.play(FadeIn(ratio_chip, scale=0.88), run_time=0.4)
        self.play(FadeIn(half_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 4.4))


class B07_Ceiling(Scene):
    def construct(self):
        total = DUR["B07"]

        # Horizontal axis
        ax = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2)
        ax.move_to(DOWN * 0.2)
        ax_lbl = Text("T2", font=MONO, color=INK, font_size=28)
        ax_lbl.next_to(ax.get_right(), RIGHT, buff=0.2)

        # Ceiling line
        ceiling_y = 1.5
        ceiling = Line(LEFT * 5.5 + UP * ceiling_y, RIGHT * 5.5 + UP * ceiling_y,
                       color=TEAL, stroke_width=3)
        ceiling_chip = LabelChip("T2 = 2T1 CEILING", accent=TEAL, size=24)
        ceiling_chip.move_to(UP * (ceiling_y + 0.65))

        # Allowed zone below ceiling
        zone = Rectangle(width=11.0, height=ceiling_y + 0.2)
        zone.set_fill(TEAL, 0.07).set_stroke(width=0, opacity=0)
        zone.move_to(DOWN * 0.2 + UP * ceiling_y / 2 - UP * 0.1)

        zone_lbl = Text("allowed zone", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        zone_lbl.move_to(UP * 0.5)

        cannot_lbl = SerifLabel("T2 can never reach above this line", accent=TEAL, size=22)
        cannot_lbl.move_to(DOWN * 1.8)

        # T1 marker
        t1_mark = Line(LEFT * 5.5 + DOWN * 0.3, LEFT * 5.5 + UP * ceiling_y + UP * 0.1,
                       color=SLATE, stroke_width=1.5)
        t1_mark.move_to([0, (ceiling_y / 2 - 0.1), 0])
        t1_chip = LabelChip("T1", accent=SLATE, size=20)
        t1_chip.move_to([0, -0.7, 0])

        self.play(Create(ax), FadeIn(ax_lbl), run_time=0.5)
        self.play(FadeIn(zone), run_time=0.4)
        self.play(Create(ceiling), run_time=0.6)
        self.play(FadeIn(ceiling_chip, scale=0.88), run_time=0.4)
        self.play(FadeIn(zone_lbl, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(cannot_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.7))


class B10_Formula(Scene):
    def construct(self):
        total = DUR["B10"]

        title = Text("Two additive decay rates", font=SERIF, color=INK,
                     font_size=26, slant=ITALIC)
        title.move_to(UP * 3.2)

        # Stacked bar diagram showing 1/T2 = 1/(2T1) + 1/T_phi
        # Total bar width = 8.0 at position y = 0

        bar_h = 0.9
        bar_y = 0.2
        bar_x0 = -5.0

        # 1/(2T1) segment — teal, width 3.5
        w_t1 = 4.2
        bar_t1 = Rectangle(width=w_t1, height=bar_h)
        bar_t1.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        bar_t1.move_to([bar_x0 + w_t1 / 2, bar_y, 0])

        lbl_t1 = Text("1/(2T1)", font=MONO, color=INK, font_size=24)
        lbl_t1.move_to([bar_x0 + w_t1 / 2, bar_y + bar_h + 0.45, 0])

        # 1/T_phi segment — crimson, width 2.0
        w_phi = 2.8
        bar_phi = Rectangle(width=w_phi, height=bar_h)
        bar_phi.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        bar_phi.move_to([bar_x0 + w_t1 + w_phi / 2, bar_y, 0])

        lbl_phi = Text("1/T-phi", font=MONO, color=CRIMSON, font_size=24)
        lbl_phi.move_to([bar_x0 + w_t1 + w_phi / 2, bar_y + bar_h + 0.45, 0])

        # Bracket showing total
        brace_start = [bar_x0, bar_y - 0.55, 0]
        brace_end = [bar_x0 + w_t1 + w_phi, bar_y - 0.55, 0]
        brace = Line(brace_start, brace_end, color=INK, stroke_width=2)
        total_lbl_bar = Text("= 1/T2  (total)", font=MONO, color=INK, font_size=24)
        total_lbl_bar.move_to([(brace_start[0] + brace_end[0]) / 2, bar_y - 1.1, 0])

        # Labels below
        note_t1 = SerifLabel("energy relaxation — always present", accent=TEAL, size=22)
        note_t1.move_to(LEFT * 2.0 + DOWN * 2.2)

        note_phi = SerifLabel("pure dephasing — adds on top", accent=CRIMSON, size=22)
        note_phi.move_to(RIGHT * 2.8 + DOWN * 2.8)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(bar_t1, scale=0.3), FadeIn(lbl_t1), run_time=0.6)
        self.play(FadeIn(bar_phi, scale=0.3), FadeIn(lbl_phi), run_time=0.5)
        self.play(Create(brace), FadeIn(total_lbl_bar), run_time=0.5)
        self.play(FadeIn(note_t1, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(note_phi, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.8))


class B12_Diagnostic(Scene):
    def construct(self):
        total = DUR["B12"]

        # Axes
        ax_x = Line(LEFT * 5.5 + DOWN * 2.8, RIGHT * 5.5 + DOWN * 2.8,
                    color=INK, stroke_width=2)
        ax_y = Line(LEFT * 5.5 + DOWN * 2.8, LEFT * 5.5 + UP * 2.8,
                    color=INK, stroke_width=2)

        x_lbl = Text("T1", font=MONO, color=INK, font_size=26)
        x_lbl.next_to(ax_x.get_right(), DOWN + RIGHT, buff=0.1)
        y_lbl = Text("T2", font=MONO, color=INK, font_size=26)
        y_lbl.rotate(PI / 2)
        y_lbl.next_to(ax_y.get_top(), LEFT, buff=0.15)

        # Ceiling line: T2 = 2T1, from origin to upper right
        ceiling = Line(LEFT * 5.5 + DOWN * 2.8, RIGHT * 4.0 + UP * 2.0,
                       color=TEAL, stroke_width=2.5)
        ceiling_lbl = Text("2T1 ceiling", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        ceiling_lbl.move_to(RIGHT * 3.8 + UP * 2.5)

        # Near-ceiling point
        pt_near = Dot(radius=0.16, color=TEAL).move_to(RIGHT * 1.2 + UP * 0.8)
        lbl_near = Text("low dephasing", font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        lbl_near.next_to(pt_near, RIGHT, buff=0.2)

        # Far-below point
        pt_far = Dot(radius=0.16, color=CRIMSON).move_to(RIGHT * 2.8 + DOWN * 1.0)
        lbl_far = Text("high dephasing", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        lbl_far.next_to(pt_far, RIGHT, buff=0.2)

        # Vertical bracket from pt_far up to ceiling
        gap_line = DashedLine([2.8, -1.0, 0], [2.8, 1.04, 0],
                              color=CRIMSON, stroke_width=2, dash_length=0.12)
        gap_lbl = Text("T_phi gap", font=MONO, color=CRIMSON, font_size=20)
        gap_lbl.move_to([5.2, -0.5, 0])

        self.play(Create(ax_x), Create(ax_y), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.6)
        self.play(Create(ceiling), FadeIn(ceiling_lbl), run_time=0.5)
        self.play(FadeIn(pt_near, scale=1.3), FadeIn(lbl_near), run_time=0.4)
        self.play(FadeIn(pt_far, scale=1.3), FadeIn(lbl_far), run_time=0.4)
        self.play(Create(gap_line), FadeIn(gap_lbl), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


class B13_Example(Scene):
    def construct(self):
        total = DUR["B13"]

        title = Text("Worked example: T1 = 400 us", font=SERIF, color=INK,
                     font_size=26, slant=ITALIC)
        title.move_to(UP * 3.2)

        # Horizontal axis for T2 values
        ax = Line(LEFT * 6.0 + DOWN * 0.5, RIGHT * 6.0 + DOWN * 0.5,
                  color=INK, stroke_width=2)
        ax_lbl = Text("T2", font=MONO, color=INK, font_size=24)
        ax_lbl.next_to(ax.get_right(), RIGHT, buff=0.15)

        # Scale: 800 µs = 5.5 units wide, so scale = 5.5/800
        scale = 5.5 / 800

        def t_pos(us):
            return -6.0 + us * scale

        # Ceiling at 800 µs
        t_ceiling = t_pos(800)
        ceiling_tick = Line([t_ceiling, -0.5, 0], [t_ceiling, 0.4, 0],
                            color=TEAL, stroke_width=3)
        ceiling_chip = LabelChip("2T1 = 800 us", accent=TEAL, size=22)
        ceiling_chip.move_to([t_ceiling, 0.9, 0])

        # T2 at 267 µs
        t_t2 = t_pos(267)
        t2_tick = Line([t_t2, -0.5, 0], [t_t2, 0.4, 0], color=CRIMSON, stroke_width=3)
        t2_chip = LabelChip("T2 = 267 us", accent=CRIMSON, size=22)
        t2_chip.move_to([t_t2, 0.9, 0])

        # Bracket for gap
        gap_brace = Line([t_t2, -0.9, 0], [t_ceiling, -0.9, 0],
                         color=CRIMSON, stroke_width=2.5)
        gap_tick_l = Line([t_t2, -0.75, 0], [t_t2, -1.05, 0], color=CRIMSON, stroke_width=2)
        gap_tick_r = Line([t_ceiling, -0.75, 0], [t_ceiling, -1.05, 0], color=CRIMSON, stroke_width=2)
        gap_lbl = Text("T-phi gap", font=MONO, color=CRIMSON, font_size=22)
        gap_lbl.move_to([(t_t2 + t_ceiling) / 2, -1.45, 0])

        # Values table
        values_title = Text("Published numbers reveal:", font=SERIF, color=INK,
                            font_size=22, slant=ITALIC)
        values_title.move_to(LEFT * 2.0 + DOWN * 2.2)

        val_t1 = Text("T1  = 400 us", font=MONO, color=SLATE, font_size=22)
        val_t1.move_to(LEFT * 2.0 + DOWN * 2.7)
        val_t2 = Text("T2  = 267 us", font=MONO, color=CRIMSON, font_size=22)
        val_t2.move_to(RIGHT * 0.5 + DOWN * 2.7)
        val_tphi = Text("T-phi ~ 450 us", font=MONO, color=CRIMSON, font_size=22)
        val_tphi.move_to(RIGHT * 3.5 + DOWN * 2.7)

        illustrative = SerifLabel("all numbers illustrative", accent=SLATE, size=20)
        illustrative.move_to(DOWN * 3.2)

        self.play(FadeIn(title, shift=DOWN * 0.1), Create(ax), FadeIn(ax_lbl), run_time=0.6)
        self.play(Create(ceiling_tick), FadeIn(ceiling_chip), run_time=0.4)
        self.play(Create(t2_tick), FadeIn(t2_chip), run_time=0.4)
        self.play(Create(gap_brace), Create(gap_tick_l), Create(gap_tick_r),
                  FadeIn(gap_lbl), run_time=0.5)
        self.play(FadeIn(values_title), run_time=0.3)
        self.play(FadeIn(val_t1), run_time=0.25)
        self.play(FadeIn(val_t2), run_time=0.25)
        self.play(FadeIn(val_tphi), run_time=0.25)
        self.play(FadeIn(illustrative, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 3.3))
