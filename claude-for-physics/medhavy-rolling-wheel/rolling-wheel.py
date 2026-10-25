"""rolling-wheel.py — Chapter 11.1, Rolling Motion.

Rolling without slipping = translation (every point moves with v) plus
rotation about the center (rim points move tangent with speed R omega), with
R omega = v. The velocities add to 2v at the top and cancel at the contact
point, which is instantaneously at rest.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh rolling-wheel.py RollingWheel
  Portrait  (9:16): manim -r 1080,1920 --fps 60 --disable_caching rolling-wheel.py RollingWheel
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

TRANS_C = TEAL      # translation velocity
ROT_C = CRIMSON     # rotation velocity
RES_C = INK         # resultant velocity


def make_wheel(R):
    """Bicycle-style wheel centered at ORIGIN: black tire, slate rim and
    spokes, hub. Spokes make the rotation visible."""
    disc = Circle(radius=R, stroke_width=0, fill_color=CREAM, fill_opacity=1)
    tire = Annulus(inner_radius=R * 0.86, outer_radius=R, fill_color=INK, fill_opacity=1, stroke_width=0)
    rim = Circle(radius=R * 0.86, color=SLATE, stroke_width=2)
    spokes = VGroup(*[
        Line(ORIGIN, R * 0.86 * np.array([np.cos(a), np.sin(a), 0]), color=SLATE, stroke_width=2)
        for a in np.arange(8) * TAU / 8 + PI / 8
    ])
    hub = Circle(radius=R * 0.1, color=INK, stroke_width=2, fill_color=SLATE, fill_opacity=1)
    return VGroup(disc, tire, rim, spokes, hub)


def vel_arrow(start, vec, color, sw=6, tip=0.2):
    start = np.array(start, dtype=float)
    vec = np.array(vec, dtype=float)
    n = np.linalg.norm(vec)
    if n < 0.05:
        a = Arrow(start, start + RIGHT * 0.05, buff=0, color=color, stroke_width=sw, tip_length=tip)
        a.set_opacity(0)
        return a
    return Arrow(start, start + vec, buff=0, color=color, stroke_width=sw, tip_length=tip,
                 max_tip_length_to_length_ratio=0.35)


def rot_vel(phi, L):
    """Clockwise rotation (rolling to the right), rim speed R omega -> length L."""
    return L * np.array([np.sin(phi), -np.cos(phi), 0])


def res_vel(phi, L):
    return L * np.array([1 + np.sin(phi), -np.cos(phi), 0])


class RollingWheel(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        P = self.PORTRAIT
        self.GY = -1.6 if P else -2.0          # ground line y
        self.MATH = 34 if P else 40
        self.LBL = 20 if P else 24

        if P:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_two_motions()
        self.b02_superpose()
        self.b03_sweep()
        self.b04_hold()

    def ground(self, x0, x1):
        return Line([x0, self.GY, 0], [x1, self.GY, 0], color=SLATE, stroke_width=3)

    # ---------------- B00 — wheel rolls, rim point traces a cycloid ----------------
    def b00_hook(self):
        P = self.PORTRAIT
        R = 0.4 if P else 1.0
        x0 = -PI * R                       # one revolution, cusp at x = 0
        cy = self.GY + R
        s = ValueTracker(0.0)

        def center():
            return np.array([x0 + s.get_value(), cy, 0])

        def dot_pos(sv):
            th = sv / R
            return np.array([x0 + sv + R * np.sin(th), cy + R * np.cos(th), 0])

        ground = self.ground(-safe_half_w(), safe_half_w())
        wheel = make_wheel(R).move_to(center())
        wheel.add_updater(lambda m: m.become(make_wheel(R).rotate(-s.get_value() / R).shift(center())))
        dot = Dot(dot_pos(0), radius=0.07 if P else 0.11, color=GOLD, stroke_color=INK, stroke_width=2)
        dot.add_updater(lambda m: m.move_to(dot_pos(s.get_value())))

        def trail_mob():
            sv = s.get_value()
            if sv < 0.02:
                return VMobject()
            curve = ParametricFunction(dot_pos, t_range=[0, sv, 0.01], color=SLATE, stroke_width=3)
            return DashedVMobject(curve, num_dashes=max(int(sv * (14 if P else 9)), 2), dashed_ratio=0.5)

        trail = always_redraw(trail_mob)

        self.play(Create(ground), FadeIn(wheel), run_time=0.8)
        self.play(FadeIn(dot, scale=1.5), run_time=0.4)
        self.add(trail)
        self.bring_to_front(wheel, dot)
        t_roll = 12.5
        self.play(s.animate.set_value(TAU * R), run_time=t_roll, rate_func=linear)
        trail.clear_updaters()
        wheel.clear_updaters()
        dot.clear_updaters()

        cusp = Circle(radius=0.14 if P else 0.22, color=CRIMSON, stroke_width=4).move_to([0, self.GY, 0])
        self.play(Create(cusp), run_time=0.6)
        self.play(Indicate(cusp, color=CRIMSON, scale_factor=1.4), run_time=0.8)
        self.wait(max(DURS["B00"] - (0.8 + 0.4 + t_roll + 0.6 + 0.8) - 0.6, 0.2))
        self.play(FadeOut(VGroup(ground, wheel, dot, trail, cusp)), run_time=0.6)

    # ---------------- B01 — translation panel + rotation panel ----------------
    def b01_two_motions(self):
        P = self.PORTRAIT
        if P:
            R, L = 0.6, 0.4
            c1, c2 = np.array([0, 1.55, 0]), np.array([0, -0.8, 0])
            divider = Line([-safe_half_w(), 0.33, 0], [safe_half_w(), 0.33, 0], color=SLATE, stroke_width=2)
        else:
            R, L = 1.1, 0.72
            c1, c2 = np.array([-3.3, 0.3, 0]), np.array([3.3, 0.3, 0])
            divider = Line([0, 2.6, 0], [0, -2.4, 0], color=SLATE, stroke_width=2)

        w1 = make_wheel(R).move_to(c1)
        w2 = make_wheel(R).move_to(c2)
        lab1 = crisp_text("translation", self.LBL, color=TRANS_C, font=CAPTION_STYLE).next_to(w1, DOWN, buff=0.3)
        lab2 = crisp_text("rotation", self.LBL, color=ROT_C, font=CAPTION_STYLE).next_to(w2, DOWN, buff=0.3)

        # translation: identical arrows at center, top, bottom, front
        t_pts = [c1, c1 + UP * R, c1 + DOWN * R, c1 + RIGHT * R]
        t_arrows = VGroup(*[vel_arrow(p, RIGHT * L, TRANS_C) for p in t_pts])
        t_lab = MathTex("v", font_size=self.MATH, color=TRANS_C).next_to(t_arrows[1], UP, buff=0.1)

        # rotation: tangent arrows at four rim points (clockwise), center at rest
        phis = [PI / 2, 0, -PI / 2, PI]
        r_pts = [c2 + R * np.array([np.cos(f), np.sin(f), 0]) for f in phis]
        r_arrows = VGroup(*[vel_arrow(p, rot_vel(f, L), ROT_C) for p, f in zip(r_pts, phis)])
        r_center = Dot(c2, radius=0.06, color=ROT_C)
        r_lab = MathTex(r"R\omega", font_size=self.MATH, color=ROT_C).next_to(r_arrows[0], UP, buff=0.1)

        d = DURS["B01"]
        self.play(FadeIn(w1), FadeIn(w2), Create(divider), run_time=0.8)
        self.play(FadeIn(lab1), run_time=0.4)
        self.play(LaggedStart(*[GrowArrow(a) for a in t_arrows], lag_ratio=0.3), run_time=2.0)
        self.play(Write(t_lab), run_time=0.5)
        # second sentence of narration ("Second, rotation") lands ~ halfway
        self.wait(max(d * 0.5 - 3.7, 0.2))
        self.play(FadeIn(lab2), run_time=0.4)
        self.play(Rotate(w2, angle=-PI / 4, about_point=c2), run_time=1.2)
        self.play(LaggedStart(*[GrowArrow(a) for a in r_arrows], lag_ratio=0.3), FadeIn(r_center), run_time=2.0)
        self.play(Write(r_lab), run_time=0.5)
        used = 0.8 + 0.4 + 2.0 + 0.5 + max(d * 0.5 - 3.7, 0.2) + 0.4 + 1.2 + 2.0 + 0.5
        self.wait(max(d - used - 0.6, 0.2))
        self.play(FadeOut(VGroup(w1, w2, divider, lab1, lab2, t_arrows, t_lab, r_arrows, r_center, r_lab)),
                  run_time=0.6)

    # ---------------- B02 — R omega = v; add at top, front, bottom ----------------
    def b02_superpose(self):
        P = self.PORTRAIT
        if P:
            R, cx = 0.75, -0.5
        else:
            R, cx = 1.3, -1.5
        L = 0.8 * R
        c = np.array([cx, self.GY + R, 0])
        self.R2, self.C2, self.L2 = R, c, L

        ground = self.ground(-safe_half_w(), safe_half_w())
        wheel = make_wheel(R).move_to(c)
        header = MathTex(r"R\omega", "=", "v", font_size=self.MATH + 6, color=INK)
        header[0].set_color(ROT_C)
        header[2].set_color(TRANS_C)
        header.move_to([0, safe_half_h() - 0.4, 0])

        top, front, bottom = c + UP * R, c + RIGHT * R, c + DOWN * R
        marks = VGroup(*[Dot(p, radius=0.06, color=GOLD, stroke_color=INK, stroke_width=1.5) for p in (top, front, bottom)])

        # word-proportional cue times inside this beat's narration
        n = [15, 9, 14, 13, 13]
        tot = sum(n)
        d = DURS["B02"]
        cue = np.cumsum([0] + n) / tot * d     # sentence start times

        t = 0.0
        self.play(Create(ground), FadeIn(wheel), run_time=0.8)
        self.play(Write(header), run_time=1.2)
        t += 2.0
        self.wait(max(cue[1] - t, 0.2)); t = max(cue[1], t + 0.2)
        self.play(LaggedStart(*[FadeIn(m, scale=2) for m in marks], lag_ratio=0.3), run_time=0.8)
        t += 0.8
        self.wait(max(cue[2] - t, 0.2)); t = max(cue[2], t + 0.2)

        # top: v + R omega -> 2v
        ta = vel_arrow(top, RIGHT * L, TRANS_C)
        ra = vel_arrow(top + RIGHT * L, rot_vel(PI / 2, L), ROT_C)
        tl = MathTex("v", font_size=self.MATH, color=TRANS_C).next_to(ta, UP, buff=0.1)
        rl = MathTex(r"R\omega", font_size=self.MATH, color=ROT_C).next_to(ra, UP, buff=0.1)
        self.play(GrowArrow(ta), FadeIn(tl), run_time=0.6)
        self.play(GrowArrow(ra), FadeIn(rl), run_time=0.6)
        top_res = vel_arrow(top, res_vel(PI / 2, L), RES_C, sw=7)
        top_lab = MathTex("2v", font_size=self.MATH, color=RES_C).next_to(top_res, UP, buff=0.1)
        self.wait(0.4)
        self.play(FadeOut(tl), FadeOut(rl), run_time=0.3)
        self.play(FadeOut(ta), FadeOut(ra), GrowArrow(top_res), run_time=0.5)
        self.play(FadeIn(top_lab), run_time=0.2)
        t += 2.6
        self.wait(max(cue[3] - t, 0.2)); t = max(cue[3], t + 0.2)

        # front: v (right) + R omega (down) -> diagonal
        ta = vel_arrow(front, RIGHT * L, TRANS_C)
        ra = vel_arrow(front + RIGHT * L, rot_vel(0, L), ROT_C)
        self.play(GrowArrow(ta), run_time=0.6)
        self.play(GrowArrow(ra), run_time=0.6)
        front_res = vel_arrow(front, res_vel(0, L), RES_C, sw=7)
        self.wait(0.6)
        self.play(FadeOut(ta), FadeOut(ra), GrowArrow(front_res), run_time=0.8)
        t += 2.6
        self.wait(max(cue[4] - t, 0.2)); t = max(cue[4], t + 0.2)

        # bottom: v (right) and R omega (left) from the same point -> cancel
        ta = vel_arrow(bottom + UP * 0.06, RIGHT * L, TRANS_C)
        ra = vel_arrow(bottom + UP * 0.06, rot_vel(-PI / 2, L), ROT_C)
        self.play(GrowArrow(ta), GrowArrow(ra), run_time=0.8)
        self.wait(0.8)
        ta_small = vel_arrow(bottom + UP * 0.06, RIGHT * 0.06, TRANS_C)
        ra_small = vel_arrow(bottom + UP * 0.06, LEFT * 0.06, ROT_C)
        self.play(Transform(ta, ta_small), Transform(ra, ra_small), run_time=1.0)
        ring = Circle(radius=0.14 if P else 0.2, color=CRIMSON, stroke_width=5).move_to(bottom)
        zero = MathTex("0", font_size=self.MATH, color=INK).next_to(ring, DOWN, buff=0.12)
        self.play(FadeOut(ta), FadeOut(ra), FadeOut(marks[2]), FadeIn(ring), FadeIn(zero), run_time=0.6)
        t += 3.2
        self.wait(max(d - t - 0.8, 0.2))
        self.play(FadeOut(VGroup(header, marks[0], marks[1], top_res, top_lab, front_res, ring, zero)), run_time=0.8)
        self.ground_line, self.wheel = ground, wheel

    # ---------------- B03 — rolling with live resultant field ----------------
    def b03_sweep(self):
        P = self.PORTRAIT
        R = self.R2
        L = 0.55 if P else 0.8
        cy = self.GY + R
        if P:
            x_start, k = -0.25, 0.0         # camera tracks the wheel; ground ticks scroll
        else:
            x_start, k = -4.6, 1.0
        dist = (5.08 * R)                    # same rotation angle in both orientations
        s = ValueTracker(0.0)
        phi0 = [PI / 2 - i * TAU / 8 for i in range(8)]

        def center():
            return np.array([x_start + k * s.get_value(), cy, 0])

        def phis():
            th = s.get_value() / R
            return [f - th for f in phi0]

        def ticks_mob():
            sp = 0.5
            off = (-(1 - k) * s.get_value()) % sp
            xs = np.arange(-safe_half_w() - sp, safe_half_w() + sp, sp) + off
            xs = xs[(xs > -safe_half_w()) & (xs < safe_half_w())]
            return VGroup(*[Line([x, self.GY, 0], [x - 0.15, self.GY - 0.18, 0], color=SLATE, stroke_width=2) for x in xs])

        def field_mob():
            c = center()
            return VGroup(*[vel_arrow(c + R * np.array([np.cos(f), np.sin(f), 0]), res_vel(f, L), RES_C, sw=5, tip=0.16)
                            for f in phis()])

        def dots_mob():
            c = center()
            return VGroup(*[Dot(c + R * np.array([np.cos(f), np.sin(f), 0]), radius=0.05, color=GOLD,
                                stroke_color=INK, stroke_width=1.2) for f in phis()])

        def ring_mob():
            c = center()
            dmin = min(abs(((f + PI / 2 + PI) % TAU) - PI) for f in phis())
            glow = max(0.0, 1 - dmin / 0.3)
            base = 0.17 if P else 0.24
            r = Circle(radius=base * (1 + 0.3 * glow), color=CRIMSON, stroke_width=2 + 4 * glow,
                       stroke_opacity=0.35 + 0.65 * glow).move_to([c[0], self.GY, 0])
            return r

        # move the B02 wheel to the start position
        self.play(self.wheel.animate.move_to(center()), run_time=0.8)
        wheel = self.wheel
        wheel.add_updater(lambda m: m.become(make_wheel(R).rotate(-s.get_value() / R).shift(center())))
        ticks = always_redraw(ticks_mob)
        field = always_redraw(field_mob)
        dots = always_redraw(dots_mob)
        ring = always_redraw(ring_mob)
        self.play(FadeIn(ticks), FadeIn(ring), FadeIn(dots), FadeIn(field), run_time=0.8)
        t_roll = DURS["B03"] - 1.6
        self.play(s.animate.set_value(dist), run_time=t_roll, rate_func=linear)
        for m in (wheel, ticks, field, dots, ring):
            m.clear_updaters()
        self.ticks, self.field, self.dots, self.ring = ticks, field, dots, ring
        self.C3 = center()
        self.L3 = L

    # ---------------- B04 — stop, dim, keep 2v and v = 0 ----------------
    def b04_hold(self):
        P = self.PORTRAIT
        R, c, L = self.R2, self.C3, self.L3
        top = c + UP * R
        bottom = c + DOWN * R
        top_res = vel_arrow(top, res_vel(PI / 2, L), RES_C, sw=7)
        top_lab = MathTex("2v", font_size=self.MATH, color=RES_C).next_to(top_res, UP, buff=0.1)
        ring = Circle(radius=0.16 if P else 0.22, color=INK, stroke_width=5, fill_color=GOLD, fill_opacity=0.8).move_to(bottom)
        v0 = MathTex("v", "=", "0", font_size=self.MATH, color=INK).next_to(ring, DOWN, buff=0.15)
        self.play(
            FadeOut(self.field), FadeOut(self.dots), FadeOut(self.ring),
            self.wheel.animate.set_opacity(0.22), self.ticks.animate.set_opacity(0.3),
            self.ground_line.animate.set_opacity(0.4),
            run_time=1.0,
        )
        self.play(GrowArrow(top_res), FadeIn(top_lab), run_time=0.7)
        self.play(FadeIn(ring, scale=1.5), Write(v0), run_time=0.8)
        self.wait(max(DURS["B04"] - 2.5, 0.3))
