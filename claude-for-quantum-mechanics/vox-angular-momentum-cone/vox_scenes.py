"""vox_scenes.py — Why Angular Momentum Can Never Point Straight Up
(vox-angular-momentum-cone, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. B09 is STILL·ai — no scene here.
Color law: TEAL = classical/expected alignment; CRIMSON = quantum deficit/lean.
Exclusions: no ladder-operator derivation, no Robertson algebra, no spherical harmonics.
"""
import sys, json, pathlib, numpy as np
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid, fallback=9.0):
    return DUR.get(bid, fallback)


# ── B01 — Cold open: cone precession teaser ─────────────────────────────────
class B01_ConeTeaser(Scene):
    def construct(self):
        total = _dur("B01", 9.0)
        # z-axis
        z_axis = Arrow(DOWN * 2.8, UP * 2.8, color=INK, stroke_width=3,
                       buff=0, tip_length=0.2)
        z_label = Text("z", font=SERIF, color=INK, font_size=32)
        z_label.next_to(z_axis, UP, buff=0.15)
        # cone circle (ellipse at base) - dashed
        cone_ring = Ellipse(width=3.2, height=0.7, color=SLATE, stroke_width=1.5)
        cone_ring.set_fill(opacity=0).set_stroke(opacity=0.5)
        cone_ring.shift(DOWN * 1.2)
        # angular momentum vector on the cone
        vec = Arrow(ORIGIN, RIGHT * 1.4 + UP * 2.0, color=CRIMSON, stroke_width=4,
                    buff=0, tip_length=0.25)
        vec.shift(DOWN * 1.2)
        # z-shadow (projection)
        shadow = Arrow(ORIGIN, UP * 2.0, color=TEAL, stroke_width=3,
                       buff=0, tip_length=0.2)
        shadow.shift(DOWN * 1.2)
        shadow_label = Text("max z", font=MONO, color=TEAL, font_size=26)
        shadow_label.next_to(shadow, RIGHT, buff=0.15)

        self.play(Create(z_axis), FadeIn(z_label), run_time=0.8)
        self.play(Create(cone_ring), run_time=0.7)
        self.play(GrowArrow(vec), run_time=0.9)
        self.play(GrowArrow(shadow), FadeIn(shadow_label), run_time=0.8)
        # rotate vector around z: show precession
        rot_vec = vec.copy()
        self.play(Rotate(rot_vec, angle=TAU, about_point=DOWN * 1.2,
                         run_time=total - 3.5, rate_func=linear))
        self.wait(0.5)


# ── B02 — Max alignment, still on a cone ────────────────────────────────────
class B02_MaxAlignment(Scene):
    def construct(self):
        total = _dur("B02", 9.0)
        z_axis = Arrow(DOWN * 2.5, UP * 2.8, color=INK, stroke_width=3,
                       buff=0, tip_length=0.2)
        z_label = Text("z", font=SERIF, color=INK, font_size=32)
        z_label.next_to(z_axis, UP, buff=0.12)
        # the L vector for ell=1, m=1: angle = arccos(1/sqrt(2)) = 45 deg
        angle = np.pi / 4
        lx = np.sin(angle) * 2.0
        lz = np.cos(angle) * 2.0
        vec = Arrow(ORIGIN, RIGHT * lx + UP * lz, color=CRIMSON, stroke_width=4,
                    buff=0, tip_length=0.25)
        # shadow on z
        shadow = DashedLine(ORIGIN, UP * lz, color=TEAL, stroke_width=2.5)
        shadow_label = SerifLabel("ell*hbar", accent=TEAL, size=26)
        shadow_label.next_to(shadow, LEFT, buff=0.2)
        # total length indicator
        total_label = SerifLabel("hbar sqrt(ell(ell+1))", accent=CRIMSON, size=26)
        total_label.next_to(vec, RIGHT, buff=0.2)

        self.play(Create(z_axis), FadeIn(z_label), run_time=0.7)
        self.play(GrowArrow(vec), run_time=0.8)
        self.play(Create(shadow), FadeIn(shadow_label), run_time=0.8)
        self.play(FadeIn(total_label), run_time=0.7)
        # rotate to show cone
        rot = vec.copy()
        self.play(Rotate(rot, angle=PI, about_point=ORIGIN,
                         run_time=total - 4.0, rate_func=linear))
        self.wait(0.5)


# ── B03 — THE QUESTION card ──────────────────────────────────────────────────
class B03_QuestionCard(Scene):
    def construct(self):
        total = _dur("B03", 10.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q_top = Text("Total magnitude:", font=DISPLAY, color=INK, font_size=38)
        q_val1 = Text("hbar sqrt(ell(ell+1))", font=MONO, color=CRIMSON, font_size=44)
        q_mid = Text("Maximum z-projection:", font=DISPLAY, color=INK, font_size=38)
        q_val2 = Text("ell * hbar", font=MONO, color=TEAL, font_size=44)
        q_ask = Text("Why are these never equal?", font=SERIF, color=INK,
                     font_size=36, slant=ITALIC)
        content = VGroup(q_top, q_val1, q_mid, q_val2, q_ask)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.move_to(ORIGIN).shift(DOWN * 0.2)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q_top), FadeIn(q_val1), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(q_mid), FadeIn(q_val2), run_time=0.9)
        self.wait(0.5)
        self.play(FadeIn(q_ask, shift=UP * 0.15), run_time=0.8)
        self.wait(total - 4.0)


# ── B04 — THE PROBLEM: classical arrow intuition ─────────────────────────────
class B04_ClassicalArrow(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        label_cl = LabelChip("CLASSICAL", accent=TEAL, size=24)
        label_cl.to_corner(UL, buff=0.6)
        # classical arrow pointing straight up
        z_axis = Arrow(DOWN * 2.5, UP * 2.8, color=INK, stroke_width=2,
                       buff=0, tip_length=0.18)
        z_label = Text("z", font=SERIF, color=INK, font_size=28)
        z_label.next_to(z_axis, UP, buff=0.1)
        cl_vec = Arrow(ORIGIN, UP * 2.4, color=TEAL, stroke_width=5,
                       buff=0, tip_length=0.28)
        cl_label = Text("L", font=SERIF, color=TEAL, font_size=34, slant=ITALIC)
        cl_label.next_to(cl_vec, RIGHT, buff=0.2)
        aligned_chip = LabelChip("PERFECTLY ALIGNED", accent=TEAL, size=22)
        aligned_chip.to_corner(DR, buff=0.5)

        self.play(FadeIn(label_cl), Create(z_axis), FadeIn(z_label), run_time=0.8)
        self.play(GrowArrow(cl_vec), FadeIn(cl_label), run_time=0.9)
        self.wait(1.0)
        self.play(cl_vec.animate.scale(1.1), run_time=0.5)
        self.play(cl_vec.animate.scale(1.0 / 1.1), run_time=0.4)
        self.play(FadeIn(aligned_chip, shift=UP * 0.15), run_time=0.7)
        self.wait(total - 5.0)


# ── B05 — THE PROBLEM: Lz eigenstate seems sharp ────────────────────────────
class B05_LzEigenstate(Scene):
    def construct(self):
        total = _dur("B05", 10.0)
        label = LabelChip("QUANTUM", accent=CRIMSON, size=24)
        label.to_corner(UL, buff=0.6)
        # Text block on left side, arrow diagram on right side — separated
        lz_row = Text("Lz eigenstate:", font=SERIF, color=INK, font_size=34)
        lz_row.move_to(LEFT * 2.8 + UP * 1.5)
        lz_val = Text("Lz = m * hbar", font=MONO, color=TEAL, font_size=36)
        lz_val.move_to(LEFT * 2.8 + UP * 0.8)
        sharp_label = SerifLabel("Sharp z-component", accent=TEAL, size=28)
        sharp_label.move_to(LEFT * 2.8 + DOWN * 0.1)
        seems_label = Text("Seems to point along z?", font=SERIF, color=INK,
                           font_size=28, slant=ITALIC)
        seems_label.move_to(LEFT * 2.8 + DOWN * 1.0)
        # Arrow diagram on right side — well clear of text
        z_axis = Arrow(DOWN * 1.8, UP * 1.8, color=INK, stroke_width=2,
                       buff=0, tip_length=0.16)
        z_axis.shift(RIGHT * 3.5)
        vec_q = Arrow(RIGHT * 3.5 + DOWN * 0.2, RIGHT * 3.5 + UP * 1.7,
                      color=TEAL, stroke_width=4, buff=0, tip_length=0.22)

        self.play(FadeIn(label), run_time=0.5)
        self.play(FadeIn(lz_row), FadeIn(lz_val), run_time=0.9)
        self.play(FadeIn(sharp_label), run_time=0.7)
        self.play(Create(z_axis), GrowArrow(vec_q), run_time=0.8)
        self.play(FadeIn(seems_label, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: L^2 = sum of squares ────────────────────────────────────
class B06_SumOfSquares(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE CONSTRAINT", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Three squares, each labeled
        sq_x = Square(1.2).set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.5)
        lbl_x = Text("Lx^2", font=MONO, color=CRIMSON, font_size=32)
        lbl_x.move_to(sq_x)
        sq_y = Square(1.2).set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.5)
        lbl_y = Text("Ly^2", font=MONO, color=CRIMSON, font_size=32)
        lbl_y.move_to(sq_y)
        sq_z = Square(1.2).set_fill(TEAL, 0.25).set_stroke(TEAL, 2.5)
        lbl_z = Text("Lz^2", font=MONO, color=TEAL, font_size=32)
        lbl_z.move_to(sq_z)
        plus1 = Text("+", font=DISPLAY, color=INK, font_size=36)
        plus2 = Text("+", font=DISPLAY, color=INK, font_size=36)
        eq_sign = Text("=", font=DISPLAY, color=INK, font_size=36)
        l2_box = Square(1.2).set_fill(SLATE, 0.35).set_stroke(SLATE, 2.5)
        lbl_l2 = Text("L^2", font=MONO, color=INK, font_size=32)
        lbl_l2.move_to(l2_box)
        row = VGroup(sq_x, VGroup(lbl_x), plus1, sq_y, VGroup(lbl_y), plus2, sq_z, VGroup(lbl_z), eq_sign,
                     VGroup(l2_box, lbl_l2))
        # arrange manually
        sq_x_g = VGroup(sq_x, lbl_x)
        sq_y_g = VGroup(sq_y, lbl_y)
        sq_z_g = VGroup(sq_z, lbl_z)
        l2_g = VGroup(l2_box, lbl_l2)
        pieces = VGroup(sq_x_g, plus1, sq_y_g, plus2, sq_z_g, eq_sign, l2_g)
        pieces.arrange(RIGHT, buff=0.35)
        pieces.move_to(ORIGIN)
        nonneg = SerifLabel("each term is non-negative", accent=CRIMSON, size=28)
        nonneg.next_to(pieces, DOWN, buff=0.6)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(sq_x_g), FadeIn(plus1), FadeIn(sq_y_g), FadeIn(plus2),
                  FadeIn(sq_z_g), run_time=1.0)
        self.wait(0.6)
        self.play(FadeIn(eq_sign), FadeIn(l2_g), run_time=0.8)
        self.play(sq_x_g.animate.shift(UP * 0.2), sq_y_g.animate.shift(UP * 0.2),
                  run_time=0.5)
        self.play(sq_x_g.animate.shift(DOWN * 0.2), sq_y_g.animate.shift(DOWN * 0.2),
                  run_time=0.4)
        self.play(FadeIn(nonneg, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 5.5)


# ── B07 — MECHANISM: sideways spread unavoidable ─────────────────────────────
class B07_SidewaysSpread(Scene):
    def construct(self):
        total = _dur("B07", 12.0)
        eyebrow = LabelChip("THE QUANTUM CONSTRAINT", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Two columns: classical (Lx=Ly=0 ok) vs quantum (Lx,Ly nonzero)
        col_cl = VGroup(
            LabelChip("CLASSICAL", accent=TEAL, size=22),
            Text("Lx = 0  Ly = 0", font=MONO, color=TEAL, font_size=32),
            Text("allowed", font=SERIF, color=TEAL, font_size=28, slant=ITALIC),
        )
        col_cl.arrange(DOWN, buff=0.4)
        col_q = VGroup(
            LabelChip("QUANTUM", accent=CRIMSON, size=22),
            Text("Lx has spread  Ly has spread", font=MONO, color=CRIMSON, font_size=28),
            Text("unavoidable", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC),
        )
        col_q.arrange(DOWN, buff=0.4)
        cols = VGroup(col_cl, col_q)
        cols.arrange(RIGHT, buff=2.0)
        cols.move_to(ORIGIN).shift(DOWN * 0.3)
        # divider
        divider = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=1.5)
        divider.move_to(cols)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(col_cl[0]), FadeIn(col_q[0]), run_time=0.7)
        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(col_cl[1]), FadeIn(col_q[1]), run_time=0.9)
        self.wait(0.5)
        self.play(FadeIn(col_cl[2]), FadeIn(col_q[2]), run_time=0.8)
        self.wait(total - 4.5)


# ── B08 — MECHANISM: the gap = hbar sqrt(ell) ────────────────────────────────
class B08_TheGap(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        # Number line: show |L| vs Lz_max
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2)
        # Total L marker
        total_dot = Dot(RIGHT * 2.8, color=CRIMSON, radius=0.12)
        total_lbl = Text("|L| = hbar sqrt(ell(ell+1))", font=MONO, color=CRIMSON, font_size=28)
        total_lbl.next_to(total_dot, UP, buff=0.25)
        # Lz max marker
        lz_dot = Dot(RIGHT * 1.8, color=TEAL, radius=0.12)
        lz_lbl = Text("Lz max = ell*hbar", font=MONO, color=TEAL, font_size=28)
        lz_lbl.next_to(lz_dot, DOWN, buff=0.25)
        # gap brace
        gap_line = Line(RIGHT * 1.8, RIGHT * 2.8, color=GOLD, stroke_width=5)
        gap_label = SerifLabel("gap = hbar sqrt(ell)", accent=GOLD, size=26)
        gap_label.next_to(gap_line, DOWN, buff=0.5)
        gap_label[0].set_color(INK)  # text stays ink, underline is gold
        # zero marker
        zero_dot = Dot(ORIGIN, color=INK, radius=0.08)
        zero_lbl = Text("0", font=MONO, color=INK, font_size=24)
        zero_lbl.next_to(zero_dot, DOWN, buff=0.2)

        self.play(Create(axis), FadeIn(zero_dot), FadeIn(zero_lbl), run_time=0.7)
        self.play(FadeIn(lz_dot), FadeIn(lz_lbl), run_time=0.8)
        self.play(FadeIn(total_dot), FadeIn(total_lbl), run_time=0.8)
        self.play(Create(gap_line), run_time=0.5)
        self.play(FadeIn(gap_label, shift=UP * 0.1), run_time=0.7)
        # emphasize gap
        self.play(gap_line.animate.scale(1.05), run_time=0.4)
        self.play(gap_line.animate.scale(1.0 / 1.05), run_time=0.3)
        self.wait(total - 5.5)


# ── B10 — IMPLICATION: classical limit ───────────────────────────────────────
class B10_ClassicalLimit(Scene):
    def construct(self):
        total = _dur("B10", 11.0)
        # Show cone half-angle shrinking as ell increases
        eyebrow = LabelChip("CLASSICAL LIMIT", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # Three cones at ell=1, ell=5, ell=large
        def make_cone_diagram(ell_val, label_str, x_pos):
            angle_rad = np.arccos(ell_val / np.sqrt(ell_val * (ell_val + 1)))
            lx = np.sin(angle_rad) * 1.6
            lz = np.cos(angle_rad) * 1.6
            z_ax = Line(DOWN * 1.4, UP * 1.6, color=INK, stroke_width=1.5)
            vec = Arrow(ORIGIN, RIGHT * lx + UP * lz, color=CRIMSON, stroke_width=3,
                        buff=0, tip_length=0.18)
            lbl = Text(label_str, font=MONO, color=INK, font_size=24)
            lbl.next_to(z_ax, DOWN, buff=0.2)
            grp = VGroup(z_ax, vec, lbl)
            grp.move_to(RIGHT * x_pos)
            return grp

        c1 = make_cone_diagram(1, "ell=1", -4.2)
        c5 = make_cone_diagram(5, "ell=5", -1.0)
        c20 = make_cone_diagram(20, "ell=20", 2.2)
        arrow_right = Text("classical ->", font=SERIF, color=INK, font_size=24, slant=ITALIC)
        arrow_right.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(c1), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(c5), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(c20), run_time=0.8)
        self.play(FadeIn(arrow_right, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B11 — IMPLICATION: not measurement disturbance ───────────────────────────
class B11_NotDisturbance(Scene):
    def construct(self):
        total = _dur("B11", 11.0)
        wrong = VGroup(
            LabelChip("NOT THIS", accent=CRIMSON, size=22),
            Text("measurement disturbs Lx, Ly", font=SERIF, color=CRIMSON, font_size=30),
        )
        wrong.arrange(DOWN, buff=0.4)
        right = VGroup(
            LabelChip("THIS", accent=TEAL, size=22),
            Text("Lx, Ly simply have no definite value", font=SERIF, color=INK, font_size=30),
        )
        right.arrange(DOWN, buff=0.4)
        cols = VGroup(wrong, right)
        cols.arrange(RIGHT, buff=2.2)
        cols.move_to(ORIGIN).shift(DOWN * 0.2)
        div = Line(UP * 1.6, DOWN * 1.6, color=INK, stroke_width=1.2)
        div.move_to(cols)

        self.play(FadeIn(wrong[0]), FadeIn(right[0]), Create(div), run_time=0.8)
        self.play(FadeIn(wrong[1]), FadeIn(right[1]), run_time=0.9)
        self.play(wrong.animate.shift(DOWN * 0.1), run_time=0.4)
        self.play(wrong.animate.shift(UP * 0.1), run_time=0.3)
        self.wait(total - 3.5)


# ── B12 — EXAMPLE: ell=2 worked ──────────────────────────────────────────────
class B12_Example_Ell2(Scene):
    def construct(self):
        total = _dur("B12", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # ell=2 top state
        lbl_ell = Text("ell = 2   (m = 2, maximum)", font=SERIF, color=INK, font_size=32)
        lbl_total = Text("|L| = hbar sqrt(6)  ~  2.45 hbar", font=MONO, color=CRIMSON, font_size=34)
        lbl_lz = Text("Lz max = 2 hbar", font=MONO, color=TEAL, font_size=34)
        lbl_angle = Text("cone half-angle = arccos(2/sqrt(6)) ~ 35 degrees", font=SERIF,
                         color=INK, font_size=28)
        # mini diagram
        angle_rad = np.arccos(2.0 / np.sqrt(6.0))
        z_ax = Arrow(DOWN * 1.6, UP * 1.8, color=INK, stroke_width=2,
                     buff=0, tip_length=0.16)
        vec2 = Arrow(ORIGIN, RIGHT * np.sin(angle_rad) * 1.8 + UP * np.cos(angle_rad) * 1.8,
                     color=CRIMSON, stroke_width=4, buff=0, tip_length=0.2)
        shadow2 = DashedLine(ORIGIN, UP * np.cos(angle_rad) * 1.8, color=TEAL, stroke_width=2)
        diagram = VGroup(z_ax, vec2, shadow2)
        diagram.shift(RIGHT * 4.5)
        content = VGroup(lbl_ell, lbl_total, lbl_lz, lbl_angle)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.to_edge(LEFT, buff=0.8).shift(DOWN * 0.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(lbl_ell), run_time=0.7)
        self.play(Create(z_ax), GrowArrow(vec2), run_time=0.8)
        self.play(FadeIn(lbl_total), Create(shadow2), run_time=0.8)
        self.play(FadeIn(lbl_lz), run_time=0.6)
        self.play(FadeIn(lbl_angle), run_time=0.7)
        self.wait(total - 5.5)


# ── B13 — EXAMPLE: ell=10 ────────────────────────────────────────────────────
class B13_Example_Ell10(Scene):
    def construct(self):
        total = _dur("B13", 11.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        # ell=10
        angle_10 = np.arccos(10.0 / np.sqrt(110.0))
        lbl_ell10 = Text("ell = 10: cone half-angle ~ 18 degrees", font=MONO,
                          color=CRIMSON, font_size=32)
        lbl_inf = Text("ell -> infinity: angle -> 0   (classical arrow)", font=SERIF,
                        color=TEAL, font_size=30)
        content = VGroup(lbl_ell10, lbl_inf)
        content.arrange(DOWN, buff=0.6)
        content.move_to(ORIGIN).shift(LEFT * 1.0)
        # mini diagrams side by side
        z10 = Arrow(DOWN * 1.5, UP * 1.7, color=INK, stroke_width=2, buff=0, tip_length=0.15)
        v10 = Arrow(ORIGIN, RIGHT * np.sin(angle_10) * 1.6 + UP * np.cos(angle_10) * 1.6,
                    color=CRIMSON, stroke_width=3, buff=0, tip_length=0.18)
        d10 = VGroup(z10, v10).shift(RIGHT * 4.0 + UP * 0.5)
        # classical (ell=inf represented as straight up)
        z_cl = Arrow(DOWN * 1.5, UP * 1.7, color=INK, stroke_width=2, buff=0, tip_length=0.15)
        v_cl = Arrow(ORIGIN, UP * 1.6, color=TEAL, stroke_width=4, buff=0, tip_length=0.2)
        d_cl = VGroup(z_cl, v_cl).shift(RIGHT * 5.8 + UP * 0.5)
        lbl_cl = Text("ell=inf", font=MONO, color=TEAL, font_size=22)
        lbl_cl.next_to(d_cl, DOWN, buff=0.15)
        lbl_10 = Text("ell=10", font=MONO, color=CRIMSON, font_size=22)
        lbl_10.next_to(d10, DOWN, buff=0.15)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(lbl_ell10), FadeIn(d10), FadeIn(lbl_10), run_time=0.9)
        self.wait(0.6)
        self.play(FadeIn(lbl_inf), FadeIn(d_cl), FadeIn(lbl_cl), run_time=0.9)
        self.wait(total - 3.5)


# ── B14 — RECAP endcard ──────────────────────────────────────────────────────
class B14_Endcard(Scene):
    def construct(self):
        total = _dur("B14", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        answer = Text("hbar sqrt(ell(ell+1)) > ell * hbar", font=MONO, color=CRIMSON, font_size=44)
        answer.move_to(UP * 0.8)
        sub = Text("The sideways spread is unavoidable. The cone never closes.",
                   font=SERIF, color=INK, font_size=30)
        sub.next_to(answer, DOWN, buff=0.6)
        rule = Line(answer.get_corner(DL) + DOWN * 0.1,
                    answer.get_corner(DR) + DOWN * 0.1,
                    color=CRIMSON, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(answer), Create(rule), run_time=0.9)
        self.play(answer.animate.shift(UP * 0.1), run_time=0.3)
        self.play(answer.animate.shift(DOWN * 0.1), run_time=0.3)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.8)
        self.wait(total - 3.5)
