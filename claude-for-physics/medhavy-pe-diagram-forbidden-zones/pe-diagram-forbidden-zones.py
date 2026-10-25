"""pe-diagram-forbidden-zones.py — Chapter 8, Potential Energy Diagrams.

A particle on a frictionless valley track: U(x) has the track's shape, E is a
flat line, K = E - U(x) can't be negative, so the regions where U(x) > E are
forbidden and the crossing points are turning points.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh pe-diagram-forbidden-zones.py PEDiagramForbiddenZones
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching pe-diagram-forbidden-zones.py PEDiagramForbiddenZones
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

K_U = 0.35          # U(x) = K_U x^2  (graph units)
E_LEVEL = 2.2
XT = np.sqrt(E_LEVEL / K_U)   # turning points at ±XT
XMAX = 3.2          # curve drawn on [-XMAX, XMAX]
PARTICLE = GOLD


def U(x):
    return K_U * x * x


class PEDiagramForbiddenZones(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.O, self.SX, self.SY = np.array([0, -1.5, 0]), 0.45, 0.78
            self.PR, self.FS, self.CARD_Y, self.LAB_Y = 0.12, 32, 2.85, -2.0
        else:
            self.O, self.SX, self.SY = np.array([0, -2.6, 0]), 1.25, 1.1
            self.PR, self.FS, self.CARD_Y, self.LAB_Y = 0.18, 44, 2.75, -3.15

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_track()
        self.b01_graph()
        self.b02_energy_line()
        self.b03_forbidden()
        self.b04_turning_points()
        self.b05_hold()

    def g(self, x, u):
        return self.O + np.array([x * self.SX, u * self.SY, 0])

    def curve(self, **kw):
        return ParametricFunction(lambda t: self.g(t, U(t)), t_range=[-XMAX, XMAX], **kw)

    def make_particle(self):
        return Circle(radius=self.PR, color=INK, stroke_width=2.5, fill_color=PARTICLE, fill_opacity=1)

    def on_track(self, x):
        p = self.g(x, U(x))
        n = np.array([-self.SY * 2 * K_U * x, self.SX, 0])
        return p + n / np.linalg.norm(n) * (self.PR + 0.03)

    # ---------------- B00 — particle sloshing on a valley track ----------------
    def b00_track(self):
        track = self.curve(color=SLATE, stroke_width=7)
        base_y = self.O[1] - 0.35
        pts = [self.g(t, U(t)) for t in np.linspace(-XMAX, XMAX, 80)]
        ground = Polygon(*pts, [pts[-1][0], base_y, 0], [pts[0][0], base_y, 0],
                         stroke_width=0, fill_color=SLATE, fill_opacity=0.15)
        self.tau = ValueTracker(0.0)
        particle = always_redraw(lambda: self.make_particle().move_to(
            self.on_track(XT * np.sin(2 * PI * self.tau.get_value()))))
        self.play(Create(track), FadeIn(ground), FadeIn(particle), run_time=0.8)
        T = DURS["B00"] - 0.8
        n = max(1, round(T / 5.0))
        self.play(self.tau.animate.set_value(n), run_time=T, rate_func=linear)
        self.track, self.ground, self.particle = track, ground, particle

    # ---------------- B01 — the track becomes U(x) ----------------
    def b01_graph(self):
        self.particle.clear_updaters()
        x0, x1 = -3.6, 3.6
        corner = self.g(x0, 0)
        x_axis = Arrow(corner, self.g(x1, 0) + RIGHT * 0.25, buff=0, color=INK, stroke_width=3,
                       max_tip_length_to_length_ratio=0.03)
        y_axis = Arrow(corner, self.g(x0, 4.1) + UP * 0.2, buff=0, color=INK, stroke_width=3,
                       max_tip_length_to_length_ratio=0.05)
        x_lab = MathTex("x", font_size=self.FS, color=INK).next_to(x_axis, DOWN, buff=0.1).align_to(x_axis, RIGHT)
        e_lab = crisp_text("energy", 18 if self.PORTRAIT else 24, color=INK, font=CAPTION_STYLE).next_to(
            y_axis, RIGHT, buff=0.1).align_to(y_axis, UP)
        ucurve = self.curve(color=INK, stroke_width=5)
        ucurve.set_z_index(2)
        u_lab = MathTex("U(x)", font_size=self.FS, color=INK)
        if self.PORTRAIT:
            u_lab.next_to(Dot(self.g(3.2, U(3.2)), radius=0.01), LEFT, buff=0.12)
        else:
            u_lab.next_to(Dot(self.g(XMAX, U(XMAX)), radius=0.01), RIGHT, buff=0.15)
        self.play(FadeOut(self.particle), run_time=0.5)
        self.play(ReplacementTransform(self.track, ucurve), FadeOut(self.ground),
                  Create(x_axis), Create(y_axis), run_time=2.0)
        self.play(FadeIn(x_lab), FadeIn(e_lab), FadeIn(u_lab), run_time=0.8)
        self.axes = VGroup(x_axis, y_axis, x_lab, e_lab)
        self.ucurve, self.u_lab = ucurve, u_lab
        self.wait(DURS["B01"] - 3.3)

    # ---------------- B02 — constant E line, two crossings ----------------
    def b02_energy_line(self):
        eline = DashedLine(self.g(-3.6, E_LEVEL), self.g(3.6, E_LEVEL), color=TEAL, stroke_width=5,
                           dash_length=0.14)
        eline.set_z_index(1)
        if self.PORTRAIT:
            elab = MathTex("E", font_size=self.FS, color=TEAL).move_to(self.g(-3.3, E_LEVEL) + DOWN * 0.24)
        else:
            elab = MathTex(r"E\ \text{(constant)}", font_size=self.FS - 6, color=TEAL).next_to(eline, RIGHT, buff=0.15)
        dots = VGroup(*[Dot(self.g(s * XT, E_LEVEL), radius=0.08, color=INK) for s in (-1, 1)])
        dots.set_z_index(3)
        self.wait(1.5)
        self.play(Create(eline), FadeIn(elab), run_time=1.5)
        self.wait(DURS["B02"] - 5.0)
        self.play(FadeIn(dots, scale=1.6), run_time=0.6)
        self.wait(1.4)
        self.eline, self.elab, self.dots = eline, elab, dots

    # ---------------- B03 — K = E - U, forbidden zones ----------------
    def b03_forbidden(self):
        l1 = MathTex("K", "=", "E", "-", "U(x)", font_size=self.FS, color=INK)
        l1[0].set_color(TEAL)
        l1[2].set_color(TEAL)
        l2 = MathTex(r"U(x) > E", r"\;\Rightarrow\;", r"K < 0", font_size=self.FS, color=INK)
        l2[2].set_color(CRIMSON)
        lines = VGroup(l1, l2).arrange(DOWN, buff=0.22).move_to([0, self.CARD_Y, 0])
        frame = SurroundingRectangle(lines, color=SLATE, stroke_width=2.5, buff=0.2, corner_radius=0.1,
                                     fill_color=CREAM, fill_opacity=1)

        xa, xf = 1.2, -3.0
        bar_ok = Line(self.g(xa, U(xa)), self.g(xa, E_LEVEL), color=TEAL, stroke_width=8)
        lab_ok = MathTex("K", font_size=self.FS, color=TEAL).next_to(bar_ok, LEFT, buff=0.12)
        bar_bad = Line(self.g(xf, E_LEVEL), self.g(xf, U(xf)), color=CRIMSON, stroke_width=8)
        lab_bad = MathTex("K < 0", font_size=self.FS - 4, color=CRIMSON).next_to(bar_bad, UR, buff=0.08).shift(RIGHT * 0.15)
        for m in (bar_ok, bar_bad):
            m.set_z_index(4)

        zones = VGroup(
            Polygon(self.g(-3.6, 0), self.g(-XT, 0), self.g(-XT, 4.1), self.g(-3.6, 4.1)),
            Polygon(self.g(XT, 0), self.g(3.6, 0), self.g(3.6, 4.1), self.g(XT, 4.1)),
        )
        zones.set_stroke(width=0).set_fill(CRIMSON, opacity=0.22)
        zones.set_z_index(-1)
        crosses = VGroup(*[
            Cross(Square(side_length=0.5 if not self.PORTRAIT else 0.3), stroke_color=CRIMSON, stroke_width=8)
            .move_to(self.g(s * 3.05, 1.0)) for s in (-1, 1)])

        T = DURS["B03"]
        self.play(FadeIn(frame), Write(l1), run_time=1.2)
        self.play(Create(bar_ok), FadeIn(lab_ok), run_time=0.8)
        self.wait(T * 0.18)
        self.play(Create(bar_bad), FadeIn(lab_bad), run_time=0.8)
        self.wait(T * 0.12)
        self.play(Write(l2), run_time=1.2)
        self.wait(T * 0.25)
        self.play(FadeIn(zones), FadeIn(crosses, scale=1.4), run_time=0.8)
        self.play(FadeOut(crosses), run_time=0.6)
        self.wait(T - (5.4 + T * 0.55))
        self.card = VGroup(frame, lines)
        self.bars = VGroup(bar_ok, lab_ok, bar_bad, lab_bad)
        self.zones = zones

    # ---------------- B04 — oscillation between turning points ----------------
    def b04_turning_points(self):
        self.tau.set_value(0.0)

        def x_now():
            return XT * np.sin(2 * PI * self.tau.get_value())

        particle = always_redraw(lambda: self.make_particle().move_to(self.g(x_now(), U(x_now()))))
        particle.set_z_index(6)

        def kbar():
            x = x_now()
            if E_LEVEL - U(x) < 0.03:
                return VMobject()
            return Line(self.g(x, U(x)), self.g(x, E_LEVEL), color=TEAL, stroke_width=7)

        bar = always_redraw(kbar)
        bar.set_z_index(5)
        fs = 16 if self.PORTRAIT else 24
        if self.PORTRAIT:
            # one centered label with pointers: two labels collide in the narrow frame
            tl = crisp_text("turning points", fs, color=INK, font=CAPTION_STYLE).move_to(
                self.g(0, E_LEVEL) + UP * 0.32)
            tr = VGroup(*[Arrow(tl.get_corner(s * RIGHT + DOWN) + np.array([-s * 0.1, -0.03, 0]),
                                d.get_center() + np.array([-s * 0.07, 0.07, 0]), buff=0.02, color=INK,
                                stroke_width=2.5, max_tip_length_to_length_ratio=0.18)
                          for s, d in ((-1, self.dots[0]), (1, self.dots[1]))])
        else:
            tl = crisp_text("turning point", fs, color=INK, font=CAPTION_STYLE).next_to(self.dots[0], UR, buff=0.1)
            tr = crisp_text("turning point", fs, color=INK, font=CAPTION_STYLE).next_to(self.dots[1], UL, buff=0.1)

        self.play(FadeOut(self.card), FadeOut(self.bars), run_time=0.6)
        self.play(FadeIn(particle), FadeIn(bar), run_time=0.5)
        hold = 1.0
        T1 = (DURS["B04"] - 1.1 - hold) / 1.375
        self.play(self.tau.animate.set_value(2.0), run_time=T1, rate_func=linear)
        self.play(self.tau.animate.set_value(2.75), FadeIn(tl), FadeIn(tr), run_time=0.375 * T1, rate_func=linear)
        self.wait(hold)
        particle.clear_updaters()
        bar.clear_updaters()
        self.particle, self.kbar, self.tlabels = particle, bar, VGroup(tl, tr)

    # ---------------- B05 — hold with summary label ----------------
    def b05_hold(self):
        label = Tex(r"Classically forbidden: $U(x) > E$", font_size=self.FS - 2, color=CRIMSON).move_to(
            [0, self.LAB_Y, 0])
        if label.width > 2 * safe_half_w():
            label.scale_to_fit_width(2 * safe_half_w())
        self.wait(0.8)
        self.play(FadeIn(label, shift=UP * 0.15), run_time=0.8)
        self.wait(DURS["B05"] - 1.6)
