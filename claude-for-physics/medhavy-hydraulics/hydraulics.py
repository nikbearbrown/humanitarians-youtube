"""hydraulics.py — Chapter 14, 14.3 Pascal's Principle and Hydraulics.

A small force F_1 on a narrow piston raises the fluid pressure by F_1/A_1;
Pascal's principle transmits that change undiminished to the wide piston,
which feels F_2 = (A_2/A_1) F_1. Work is not multiplied: F_1 d_1 = F_2 d_2.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh hydraulics.py Hydraulics
  Portrait  (9:16): manim -r 1080,1920 --fps 60 --disable_caching hydraulics.py Hydraulics
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from medhavy_common import *

HERE = Path(__file__).parent
SHEET = json.loads((HERE / "beat_sheet.json").read_text())
DURS = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}
NARR = {b["beat_id"]: b["narration_text"] for b in SHEET["beats"]}

PORTRAIT = is_portrait()

FLUID = "#56B4E9"      # Okabe-Ito sky blue (hydraulic fluid)
CAR_BLUE = "#0072B2"   # Okabe-Ito blue (car body)
PISTON = "#A6A6A6"

# ---- design-space geometry (landscape units); mapped to screen by P() ----
XL0, XL1 = -4.5, -4.0      # narrow cylinder (width 0.5)
XR0, XR1 = -1.5, 1.0       # wide cylinder (width 2.5): 5x the narrow one
YB, YC = -3.0, -2.4        # channel bottom / channel inner top
Y0 = 0.3                   # starting fluid level, both pistons level
YTOP_L, YTOP_R = 0.6, 0.8  # wall tops
D1, D2 = 1.5, 0.3          # strokes: D1 * 0.5 == D2 * 2.5 (incompressible)
TP_L, TP_R = 0.22, 0.7     # piston thicknesses
ROD = 1.8                  # rod top stays above the wall even at full stroke
XM_L = (XL0 + XL1) / 2
XM_R = (XR0 + XR1) / 2

if PORTRAIT:
    K = 0.58
    OFF = np.array([1.015, -0.2, 0])
    LBL, EQ = 34, 36
    SLOTS = [np.array([0, 2.95, 0]), np.array([0, 1.95, 0])]
    EQ_MAXW = 2 * safe_half_w()
else:
    K = 1.0
    OFF = np.array([-0.6, -0.3, 0])
    LBL, EQ = 48, 56
    SLOTS = [np.array([3.7, 1.6, 0]), np.array([3.7, 0.0, 0])]
    EQ_MAXW = 4.6


def P(x, y):
    return OFF + K * np.array([x, y, 0.0])


def fit(m, maxw=None):
    maxw = maxw or EQ_MAXW
    if m.width > maxw:
        m.scale_to_fit_width(maxw)
    return m


def two_lines(a, b, font_size, color):
    """Two centered MathTex lines (one align* MathTex right-aligns them)."""
    return VGroup(MathTex(a, font_size=font_size, color=color),
                  MathTex(b, font_size=font_size, color=color)).arrange(DOWN, buff=0.18)


def make_car():
    """Side-view car in design units, wheel bottoms at y=0, centered on x=0."""
    body = RoundedRectangle(width=2.0, height=0.4, corner_radius=0.12, color=INK,
                            fill_color=CAR_BLUE, fill_opacity=1, stroke_width=2.5).move_to([0, 0.38, 0])
    cabin = Polygon([-0.65, 0.58, 0], [0.75, 0.58, 0], [0.45, 0.95, 0], [-0.4, 0.95, 0],
                    color=INK, fill_color=CAR_BLUE, fill_opacity=1, stroke_width=2.5)
    win1 = Polygon([-0.52, 0.63, 0], [0.0, 0.63, 0], [0.0, 0.88, 0], [-0.33, 0.88, 0],
                   color=INK, fill_color=WHITE, fill_opacity=0.95, stroke_width=1.5)
    win2 = Polygon([0.08, 0.63, 0], [0.6, 0.63, 0], [0.4, 0.88, 0], [0.08, 0.88, 0],
                   color=INK, fill_color=WHITE, fill_opacity=0.95, stroke_width=1.5)
    wheels = VGroup()
    for x in (-0.6, 0.6):
        tyre = Circle(radius=0.2, color=INK, fill_color=INK, fill_opacity=1, stroke_width=2).move_to([x, 0.2, 0])
        hub = Circle(radius=0.08, color=SLATE, fill_color=PISTON, fill_opacity=1, stroke_width=1).move_to([x, 0.2, 0])
        wheels.add(tyre, hub)
    return VGroup(body, cabin, win1, win2, wheels)


class Hydraulics(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        self.s = ValueTracker(0.0)    # stroke progress 0 -> 1
        self.g = ValueTracker(0.3)    # gap between F_1 arrow tip and rod top

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_push()
        self.b02_pascal()
        self.b03_lift()
        self.b04_tradeoff()
        self.b05_hold()

    # ---- geometry as a function of the stroke tracker ----
    def yL(self):
        return Y0 - self.s.get_value() * D1

    def yR(self):
        return Y0 + self.s.get_value() * D2

    def fluid(self):
        yl, yr = self.yL(), self.yR()
        pts = [P(XL0, yl), P(XL0, YB), P(XR1, YB), P(XR1, yr), P(XR0, yr), P(XR0, YC), P(XL1, YC), P(XL1, yl)]
        return Polygon(*pts, stroke_width=0, fill_color=FLUID, fill_opacity=0.45)

    def left_piston(self):
        yl = self.yL()
        disk = Rectangle(width=K * (XL1 - XL0 - 0.04), height=K * TP_L, color=INK,
                         fill_color=PISTON, fill_opacity=1, stroke_width=2).move_to(P(XM_L, yl + TP_L / 2))
        rod = Line(P(XM_L, yl + TP_L), P(XM_L, yl + TP_L + ROD), color=INK, stroke_width=6)
        cap = Rectangle(width=K * 0.4, height=K * 0.08, color=INK, fill_color=SLATE, fill_opacity=1,
                        stroke_width=1.5).move_to(P(XM_L, yl + TP_L + ROD))
        return VGroup(rod, disk, cap)

    def rod_top(self):
        return P(XM_L, self.yL() + TP_L + ROD + 0.04)

    def right_piston(self):
        yr = self.yR()
        return Rectangle(width=K * (XR1 - XR0 - 0.04), height=K * TP_R, color=INK, fill_color=PISTON,
                         fill_opacity=1, stroke_width=2).move_to(P(XM_R, yr + TP_R / 2))

    def f1_arrow(self):
        top = self.rod_top()
        tip = top + UP * K * self.g.get_value()
        return Arrow(tip + UP * K * 0.9, tip, buff=0, color=CRIMSON, stroke_width=8,
                     max_tip_length_to_length_ratio=0.28)

    def f2_arrow(self):
        return Arrow(P(XM_R, -2.3), P(XM_R, self.yR() - 0.04), buff=0, color=TEAL, stroke_width=14,
                     max_tip_length_to_length_ratio=0.18, max_stroke_width_to_length_ratio=12)

    def marker(self, x0, x1, y):
        return Line(P(x0 + 0.03, y), P(x1 - 0.03, y), color=GOLD, stroke_width=8)

    # ---------------- B00 — the jack at rest ----------------
    def b00_hook(self):
        outer = VMobject(color=INK, stroke_width=5).set_points_as_corners(
            [P(XL0, YTOP_L), P(XL0, YB), P(XR1, YB), P(XR1, YTOP_R)])
        inner = VMobject(color=INK, stroke_width=5).set_points_as_corners(
            [P(XL1, YTOP_L), P(XL1, YC), P(XR0, YC), P(XR0, YTOP_R)])
        self.walls = VGroup(outer, inner)
        self.fluid_m = always_redraw(self.fluid)
        self.lp = always_redraw(self.left_piston)
        self.rp = always_redraw(self.right_piston)

        car = make_car().scale(K)
        car.move_to(P(XM_R, Y0 + TP_R) + UP * car.height / 2)
        car.add_updater(lambda m: m.shift(UP * (P(XM_R, self.yR() + TP_R)[1] - m.get_bottom()[1])))
        self.car = car

        self.play(FadeIn(self.fluid_m), Create(self.walls), run_time=1.0)
        self.play(FadeIn(self.lp), FadeIn(self.rp), FadeIn(self.car, shift=DOWN * 0.2), run_time=0.8)
        self.wait(max(DURS["B00"] - 1.8, 0.1))

    # ---------------- B01 — F_1 on A_1, delta p = F_1/A_1 ----------------
    def b01_push(self):
        self.f1 = always_redraw(self.f1_arrow)
        self.f1_lbl = MathTex("F_1", font_size=LBL, color=CRIMSON)
        self.f1_lbl.add_updater(lambda m: m.next_to(self.f1, RIGHT, buff=0.12))
        self.play(FadeIn(self.f1), FadeIn(self.f1_lbl), run_time=0.5)
        self.play(self.g.animate.set_value(0.0), run_time=0.8)

        self.a1 = always_redraw(lambda: self.marker(XL0, XL1, self.yL()))
        self.a1_lbl = MathTex("A_1", font_size=LBL, color=INK)
        self.a1_lbl.add_updater(lambda m: m.next_to(P(XL1, self.yL()), RIGHT, buff=0.15))
        self.play(Create(self.a1), FadeIn(self.a1_lbl), run_time=0.6)

        self.eq1 = fit(MathTex(r"\Delta p = \frac{F_1}{A_1}", font_size=EQ, color=INK)).move_to(SLOTS[0])
        self.play(Write(self.eq1), run_time=0.8)
        self.wait(max(DURS["B01"] - 2.7, 0.1))

    # ---------------- B02 — Pascal: same delta p everywhere ----------------
    def b02_pascal(self):
        y0 = Y0
        specs_other = [
            ((XM_L, -1.6), (XL0 + 0.03, -1.6)), ((XM_L, -0.8), (XL1 - 0.03, -0.8)),
            ((XM_L, y0 - 0.5), (XM_L, y0 - 0.03)),
            ((-3.5, -2.7), (-3.5, -2.97)), ((-2.2, -2.7), (-2.2, -2.97)), ((-2.85, -2.68), (-2.85, -2.43)),
            ((-0.9, -1.2), (XR0 + 0.03, -1.2)), ((0.4, -1.2), (XR1 - 0.03, -1.2)),
            ((XM_R, -2.55), (XM_R, -2.97)),
        ]
        specs_piston = [((x, y0 - 0.55), (x, y0 - 0.03)) for x in (-1.0, XM_R, 0.5)]

        def arr(a, b):
            return Arrow(P(*a), P(*b), buff=0, color=TEAL, stroke_width=5,
                         max_tip_length_to_length_ratio=0.45, max_stroke_width_to_length_ratio=20)

        self.p_other = VGroup(*[arr(a, b) for a, b in specs_other])
        self.p_piston = VGroup(*[arr(a, b) for a, b in specs_piston])
        self.play(*[GrowArrow(a) for a in [*self.p_other, *self.p_piston]], run_time=1.0)

        self.eq2 = fit(two_lines(r"\text{same } \Delta p \text{ everywhere}", r"\text{in the fluid}",
                                 EQ - 8, TEAL)).move_to(SLOTS[1])
        self.play(FadeIn(self.eq2), run_time=0.8)
        self.wait(max(DURS["B02"] - 1.8, 0.1))

    # ---------------- B03 — F_2 = (A_2/A_1) F_1, the car rises ----------------
    def b03_lift(self):
        self.play(FadeOut(self.eq1), FadeOut(self.eq2), run_time=0.4)

        self.a2 = always_redraw(lambda: self.marker(XR0, XR1, self.yR()))
        self.a2_lbl = MathTex("A_2", font_size=LBL, color=INK)
        self.a2_lbl.add_updater(lambda m: m.next_to(P(XR0, self.yR()), LEFT, buff=0.15))
        self.play(Create(self.a2), FadeIn(self.a2_lbl), run_time=0.6)

        f2_static = self.f2_arrow()
        self.play(ReplacementTransform(self.p_piston, f2_static), FadeOut(self.p_other), run_time=1.0)
        self.remove(f2_static)
        self.f2 = always_redraw(self.f2_arrow)
        self.add(self.f2)
        self.bring_to_front(self.rp, self.car)
        self.f2_lbl = MathTex("F_2", font_size=LBL, color=TEAL)
        self.f2_lbl.add_updater(lambda m: m.next_to(self.f2, RIGHT, buff=0.12))

        self.eq3 = fit(MathTex(r"F_2 = \frac{A_2}{A_1}\,F_1", font_size=EQ, color=INK)).move_to(SLOTS[0])
        self.play(Write(self.eq3), FadeIn(self.f2_lbl), run_time=0.8)

        self.play(self.s.animate.set_value(1.0), run_time=2.5, rate_func=smooth)

        self.eq4 = fit(two_lines(r"A_2 = 5A_1", r"100\ \text{N} \rightarrow 500\ \text{N}",
                                 EQ - 8, TEAL)).move_to(SLOTS[1])
        self.play(FadeIn(self.eq4), run_time=0.6)
        self.wait(max(DURS["B03"] - 5.9, 0.1))

    # ---------------- B04 — distance for force: F_1 d_1 = F_2 d_2 ----------------
    def b04_tradeoff(self):
        self.play(*[FadeOut(m) for m in (self.a1, self.a1_lbl, self.a2, self.a2_lbl, self.eq3, self.eq4)],
                  run_time=0.5)
        for m in (self.a1_lbl, self.a2_lbl):
            m.clear_updaters()

        lvl1 = DashedLine(P(XL0 - 0.15, Y0), P(XL1 + 0.15, Y0), color=SLATE, stroke_width=3, dash_length=0.08)
        lvl2 = DashedLine(P(XR0 - 0.15, Y0), P(XR1 + 0.15, Y0), color=SLATE, stroke_width=3, dash_length=0.08)
        self.play(Create(lvl1), Create(lvl2), run_time=0.5)
        self.lvl = VGroup(lvl1, lvl2)
        # reference level goes behind the rod and the F_2 arrow, not across them
        self.bring_to_front(self.lp, self.f2, self.f1)

        x1, x2 = XL1 + 0.35, XR0 - 0.35

        def dim(y_from, y_to, x):
            # dimension marker (|-| bar): reads clearly even for the short d_2,
            # where an arrowhead would be bigger than the stroke itself.
            # Gold reads weakly on white, so an ink copy underneath outlines it.
            tw = 0.16 / max(K, 0.6)
            parts = VGroup()
            for col, sw in ((INK, 11), (GOLD, 6)):
                parts.add(Line(P(x, y_from), P(x, y_to), color=col, stroke_width=sw))
                for y in (y_from, y_to):
                    parts.add(Line(P(x - tw / 2, y), P(x + tw / 2, y), color=col, stroke_width=sw))
            return parts

        d1 = dim(Y0, Y0 - D1, x1)
        d2 = dim(Y0, Y0 + D2, x2)
        d1_lbl = MathTex("d_1", font_size=LBL, color=INK).next_to(d1, RIGHT, buff=0.1)
        d2_lbl = MathTex("d_2", font_size=LBL, color=INK).next_to(d2, LEFT, buff=0.1)
        self.play(Create(d1), Create(d2), run_time=1.2)
        self.play(FadeIn(d1_lbl), FadeIn(d2_lbl), run_time=0.4)
        self.d = VGroup(d1, d2, d1_lbl, d2_lbl)

        self.eq5 = fit(MathTex(r"A_1 d_1 = A_2 d_2", font_size=EQ, color=INK)).move_to(SLOTS[0])
        self.eq6 = fit(MathTex(r"F_1 d_1 = F_2 d_2", font_size=EQ, color=CRIMSON)).move_to(SLOTS[1])
        self.play(Write(self.eq5), run_time=0.8)
        self.play(Write(self.eq6), run_time=0.8)
        self.wait(max(DURS["B04"] - 4.2, 0.1))

    # ---------------- B05 — hold ----------------
    def b05_hold(self):
        summary = crisp_text("MORE FORCE, NOT MORE WORK", font_size=20 if self.PORTRAIT else 26,
                             color=INK, font=CAPTION_STYLE).move_to(SLOTS[1])
        self.play(FadeOut(self.eq5), self.eq6.animate.move_to(SLOTS[0]), run_time=0.8)
        self.play(FadeIn(summary), run_time=0.6)
        self.summary = summary
        self.wait(max(DURS["B05"] - 1.4, 0.1))
