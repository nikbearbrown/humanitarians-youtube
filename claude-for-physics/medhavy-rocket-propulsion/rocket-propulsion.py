"""rocket-propulsion.py — Chapter 9, Rocket Propulsion.

Rocket + fuel is one system with zero total momentum; ejecting exhaust
backward at speed u gives the rocket m Δv = Δm u forward. With a steady burn
the remaining mass falls, so the same exhaust momentum gives ever larger Δv:
v(t) = v0 + u ln(m0/m(t)).

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh rocket-propulsion.py RocketPropulsion
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching rocket-propulsion.py RocketPropulsion
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

HULL = "#E8E8E8"
EXHAUST = CRIMSON
M_END = 0.4          # burn from m0 down to 0.4 m0
DM_PUFF = 0.08       # single puff in B02: Δm / m


def make_rocket(L, fuel):
    """Rocket pointing right, centered at origin. fuel in [0,1] = gauge fill."""
    bw, bh = 0.62 * L, 0.22 * L
    body = Rectangle(width=bw, height=bh, color=INK, stroke_width=3, fill_color=HULL, fill_opacity=1)
    nose = Polygon([bw / 2, bh / 2, 0], [bw / 2 + 0.24 * L, 0, 0], [bw / 2, -bh / 2, 0],
                   color=INK, stroke_width=3, fill_color=CRIMSON, fill_opacity=1)
    fin_t = Polygon([-bw / 2, bh / 2, 0], [-bw / 2 + 0.16 * L, bh / 2, 0], [-bw / 2 - 0.06 * L, bh / 2 + 0.13 * L, 0],
                    color=INK, stroke_width=2.5, fill_color=CRIMSON, fill_opacity=1)
    fin_b = fin_t.copy().flip(RIGHT, about_point=ORIGIN)
    nozzle = Polygon([-bw / 2, 0.06 * L, 0], [-bw / 2 - 0.08 * L, 0.09 * L, 0], [-bw / 2 - 0.08 * L, -0.09 * L, 0],
                     [-bw / 2, -0.06 * L, 0], color=INK, stroke_width=2.5, fill_color=SLATE, fill_opacity=1)
    window = Circle(radius=0.05 * L, color=INK, stroke_width=2.5, fill_color=CREAM, fill_opacity=1).move_to(
        [bw / 2 - 0.1 * L, 0, 0])
    tw, th = 0.36 * L, 0.11 * L
    tank = Rectangle(width=tw, height=th, color=INK, stroke_width=1.5).move_to([-0.07 * L, 0, 0])
    level = Rectangle(width=max(tw * fuel, 0.001), height=th, stroke_width=0, fill_color=GOLD, fill_opacity=1)
    level.move_to(tank.get_left(), aligned_edge=LEFT)
    return VGroup(body, fin_t, fin_b, nozzle, nose, window, level, tank)


class RocketPropulsion(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.L, self.C, self.FS, self.LFS = 1.5, np.array([0.1, 0.5, 0]), 32, 16
            self.U, self.EQ_Y, self.FINAL_Y, self.VMAXLEN = 2.4, 2.75, -1.4, 1.3
        else:
            self.L, self.C, self.FS, self.LFS = 2.6, np.array([-0.5, 0.2, 0]), 46, 24
            self.U, self.EQ_Y, self.FINAL_Y, self.VMAXLEN = 4.0, 2.85, -2.7, 2.6
        self.dv0 = DM_PUFF * self.U

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_nothing()
        self.b01_system()
        self.b02_puff()
        self.b03_burn()
        self.b04_exit()

    def nozzle_x(self, rocket_x):
        return rocket_x - 0.31 * self.L - 0.08 * self.L

    # ---------------- stars ----------------
    def make_stars(self, scroll):
        rng = np.random.default_rng(7)
        W = 2 * (safe_half_w() + 0.6)
        n = 14 if self.PORTRAIT else 26
        xs = rng.uniform(-W / 2, W / 2, n)
        ys = rng.uniform(-safe_half_h() + (1.4 if self.PORTRAIT else 0.3), safe_half_h() - 0.9, n)
        big = rng.uniform(0, 1, n) > 0.75
        g = VGroup()
        for x, y, b in zip(xs, ys, big):
            xx = ((x - scroll + W / 2) % W) - W / 2
            if b:
                s = Star(n=4, outer_radius=0.07, inner_radius=0.025, stroke_width=0, fill_color=SLATE, fill_opacity=0.8)
            else:
                s = Dot(radius=0.022, color=SLATE, fill_opacity=0.7)
            g.add(s.move_to([xx, y, 0]))
        return g

    # ---------------- B00 — pushing off something vs. the void ----------------
    def b00_nothing(self):
        L = self.L
        y = self.C[1] - 0.9
        road = Rectangle(width=2 * safe_half_w() + 1.2, height=0.35, stroke_width=0, fill_color=SLATE, fill_opacity=0.35)
        road.move_to([0, y - 0.175, 0])
        cw = 0.7 * L
        car_body = RoundedRectangle(width=cw, height=0.2 * L, corner_radius=0.04 * L, color=INK, stroke_width=3,
                                    fill_color=TEAL, fill_opacity=1)
        cab = RoundedRectangle(width=0.36 * L, height=0.14 * L, corner_radius=0.03 * L, color=INK, stroke_width=3,
                               fill_color=TEAL, fill_opacity=1)
        wheels = VGroup(*[Circle(radius=0.06 * L, color=INK, fill_color=INK, fill_opacity=1) for _ in range(2)])
        car = VGroup(cab, car_body, wheels)
        car_body.move_to([self.C[0], y + 0.12 * L + 0.1 * L, 0])
        cab.next_to(car_body, UP, buff=0).shift(LEFT * 0.04 * L)
        wheels[0].move_to([self.C[0] - 0.22 * L, y + 0.06 * L, 0])
        wheels[1].move_to([self.C[0] + 0.22 * L, y + 0.06 * L, 0])
        push = Arrow([wheels[0].get_x() + 0.05, y - 0.55, 0], [wheels[0].get_x() - 0.75 * L * 0.6, y - 0.55, 0], buff=0,
                     color=CRIMSON, stroke_width=6, max_tip_length_to_length_ratio=0.25)
        push_lab = crisp_text("tire pushes back on the road", self.LFS, color=CRIMSON, font=CAPTION_STYLE).next_to(
            push, DOWN, buff=0.12)
        if push_lab.get_left()[0] < -safe_half_w():
            push_lab.shift(RIGHT * (-safe_half_w() - push_lab.get_left()[0]))
        self.play(FadeIn(road), FadeIn(car), run_time=0.8)
        self.play(GrowArrow(push), FadeIn(push_lab), run_time=0.6)
        self.wait(5.0)
        self.stars = self.make_stars(0.0)
        self.play(FadeOut(VGroup(road, car, push, push_lab)), FadeIn(self.stars), run_time=1.2)
        self.rocket_x = self.C[0]
        rocket = make_rocket(L, 1.0).move_to(self.C)
        self.play(FadeIn(rocket), run_time=0.8)
        self.rocket = rocket
        self.wait(DURS["B00"] - 8.4)

    # ---------------- B01 — the system: rocket + fuel, p = 0 ----------------
    def b01_system(self):
        tank = VGroup(self.rocket[6], self.rocket[7])
        box = DashedVMobject(SurroundingRectangle(self.rocket, buff=0.3, corner_radius=0.15), num_dashes=50)
        box.set_color(TEAL).set_stroke(width=3)
        lab = crisp_text("system: rocket + fuel", self.LFS, color=TEAL, font=CAPTION_STYLE).next_to(box, UP, buff=0.12)
        p0 = MathTex(r"p_{\text{total}} = 0", font_size=self.FS, color=INK).next_to(box, DOWN, buff=0.25)
        self.wait(1.0)
        # highlight with a separate ring: animating a sub-group would add it to the scene
        # as a top-level copy that outlives the rocket
        ring = SurroundingRectangle(tank, color=GOLD, stroke_width=6, buff=0.08, corner_radius=0.05)
        self.play(Create(ring), run_time=0.5)
        self.play(FadeOut(ring), run_time=0.5)
        self.wait(2.0)
        self.play(Create(box), FadeIn(lab), run_time=1.0)
        self.wait(4.0)
        self.play(Write(p0), run_time=1.0)
        self.box, self.box_lab, self.p0 = box, lab, p0
        self.wait(DURS["B01"] - 10.0)

    # ---------------- B02 — one puff: m Δv = Δm u ----------------
    def b02_puff(self):
        L = self.L
        eq1 = MathTex(r"p_{\text{before}} = p_{\text{after}}", font_size=self.FS, color=INK).move_to([0, self.EQ_Y, 0])
        eq2 = MathTex(r"m\,\Delta v", "=", r"\Delta m\,u", font_size=self.FS + 4, color=INK).move_to([0, self.EQ_Y, 0])
        eq2[0].set_color(TEAL)
        eq2[2].set_color(EXHAUST)
        self.play(FadeOut(self.box), FadeOut(self.box_lab), FadeOut(self.p0), run_time=0.6)
        self.play(Write(eq1), run_time=1.0)
        self.wait(1.4)

        nz = np.array([self.nozzle_x(self.rocket_x), self.C[1], 0])
        puff = Circle(radius=0.11 * L, color=INK, stroke_width=2, fill_color=EXHAUST, fill_opacity=1).move_to(nz)
        t = ValueTracker(0.0)
        T = 3.0
        # this single puff is shown slowed down so it stays in frame; same u : dv ratio
        u = 0.2 if self.PORTRAIT else 1.0
        dv = DM_PUFF * u
        x_r0 = self.rocket_x
        puff.add_updater(lambda m: m.move_to(nz + LEFT * u * t.get_value()))
        self.rocket.add_updater(lambda m: m.move_to([x_r0 + dv * t.get_value(), self.C[1], 0]))
        alen_u = 0.6 if self.PORTRAIT else 1.6
        alen_v = alen_u * DM_PUFF * 3  # dv arrow drawn 3x for legibility (true ratio is dm/m)
        u_arrow = always_redraw(lambda: Arrow(puff.get_center() + RIGHT * alen_u / 2 + UP * 0.2 * L,
                                              puff.get_center() + LEFT * alen_u / 2 + UP * 0.2 * L, buff=0,
                                              color=EXHAUST, stroke_width=6, max_tip_length_to_length_ratio=0.25))
        u_lab = always_redraw(lambda: MathTex("u", font_size=self.FS - 4, color=EXHAUST).next_to(u_arrow, UP, buff=0.08))
        dm_lab = always_redraw(lambda: MathTex(r"\Delta m", font_size=self.FS - 6, color=EXHAUST).next_to(
            puff, DOWN, buff=0.1))
        v_arrow = always_redraw(lambda: Arrow(self.rocket.get_right() + RIGHT * 0.12 + DOWN * 0.0,
                                              self.rocket.get_right() + RIGHT * (0.12 + max(alen_v, 0.25)), buff=0,
                                              color=TEAL, stroke_width=6, max_tip_length_to_length_ratio=0.4))
        v_lab = always_redraw(lambda: MathTex(r"\Delta v", font_size=self.FS - 4, color=TEAL).next_to(v_arrow, UP, buff=0.08))
        self.play(FadeIn(puff, scale=0.3), run_time=0.3)
        self.add(u_arrow, u_lab, dm_lab, v_arrow, v_lab)
        self.play(t.animate.set_value(T * 0.999), run_time=T, rate_func=linear)
        for m in (puff, self.rocket, u_arrow, u_lab, dm_lab, v_arrow, v_lab):
            m.clear_updaters()
        self.rocket_x = x_r0 + dv * T
        self.wait(9.7)
        self.play(ReplacementTransform(eq1, eq2), run_time=1.2)
        self.eq = eq2
        self.puff_group = VGroup(puff, u_arrow, u_lab, dm_lab, v_arrow, v_lab)
        self.wait(DURS["B02"] - 17.2)

    # ---------------- continuous burn kinematics (ground frame) ----------------
    def kin(self, t):
        """mass, velocity, position (relative to burn start) at burn time t."""
        k = (1 - M_END) / self.T_BURN
        w = 1 - k * min(t, self.T_BURN)
        v = self.dv0 + self.U * np.log(1 / w)
        X = self.dv0 * min(t, self.T_BURN) + (self.U / k) * (w * np.log(w) - w + 1)
        if t > self.T_BURN:
            X += v * (t - self.T_BURN)
        return w, v, X

    def exhaust(self, t, cam_X, screen_x0):
        """Dots emitted every DT from the nozzle; each keeps its ground velocity v(te) - u."""
        g = VGroup()
        DT = 0.1
        ne = int(min(t, self.T_BURN) / DT)
        r = 0.045 * self.L
        lim = safe_half_w() + 0.6
        for i in range(ne + 1):
            te = i * DT
            if te > t:
                break
            _, ve, Xe = self.kin(te)
            gx = Xe + self.noz_off + (ve - self.U) * (t - te)
            sx = screen_x0 + (gx - cam_X)
            if sx < -lim or sx > lim:
                continue
            age = t - te
            jitter = 0.06 * self.L * (2 * ((np.sin(12.9898 * i) * 43758.5453) % 1.0) - 1)
            op = max(0.15, 1.0 - age / 6.0)
            g.add(Dot([sx, self.C[1] + jitter, 0], radius=r, color=EXHAUST, fill_opacity=op))
        return g

    # ---------------- B03 — steady burn: mass falls, speed builds ----------------
    def b03_burn(self):
        L = self.L
        self.noz_off = -0.31 * L - 0.08 * L - 0.05
        hold = 1.0
        self.T_BURN = DURS["B03"] - 1.0 - hold
        self.vmax = self.kin(self.T_BURN)[1]
        tb = ValueTracker(0.0)
        x0 = self.rocket_x
        self.burn_t = tb
        # camera rides with the rocket during the burn: rocket fixed on screen, stars scroll, exhaust streams
        rocket = always_redraw(lambda: make_rocket(L, (self.kin(tb.get_value())[0] - M_END) / (1 - M_END)).move_to(
            [x0, self.C[1], 0]))
        stars = always_redraw(lambda: self.make_stars(0.35 * self.kin(tb.get_value())[2]))
        trail = always_redraw(lambda: self.exhaust(tb.get_value(), self.kin(tb.get_value())[2], x0))
        y_v = self.C[1] - 0.42 * L

        def v_arrow():
            v = self.kin(tb.get_value())[1]
            ln = max(self.VMAXLEN * v / self.vmax, 0.2)
            return Arrow([x0 - ln / 2, y_v, 0], [x0 + ln / 2, y_v, 0], buff=0, color=TEAL, stroke_width=6,
                         max_tip_length_to_length_ratio=min(0.3, 0.12 / ln * 2))

        va = always_redraw(v_arrow)
        vl = always_redraw(lambda: MathTex("v", font_size=self.FS - 4, color=TEAL).next_to(va, RIGHT, buff=0.1))
        ml = always_redraw(lambda: MathTex(r"m = %.1f\,m_0" % self.kin(tb.get_value())[0], font_size=self.FS - 4,
                                           color=INK).next_to(rocket, UP, buff=0.3))
        self.play(FadeOut(self.puff_group), run_time=0.5)
        self.remove(self.rocket, self.stars)
        self.add(stars, trail, rocket)
        self.play(FadeIn(va), FadeIn(vl), FadeIn(ml), run_time=0.5)
        self.play(tb.animate.set_value(self.T_BURN), run_time=self.T_BURN, rate_func=linear)
        self.wait(hold)
        for m in (rocket, stars, trail, va, vl, ml):
            m.clear_updaters()
        self.rocket, self.stars, self.trail, self.va, self.vl, self.ml = rocket, stars, trail, va, vl, ml
        self.x0 = x0

    # ---------------- B04 — coast out of frame; trail and equation remain ----------------
    def b04_exit(self):
        L = self.L
        cam = self.kin(self.T_BURN + 1.0)[2]   # camera stops at the end of the hold
        t = ValueTracker(self.T_BURN + 1.0)
        x0 = self.x0
        rocket = always_redraw(lambda: make_rocket(L, 0.0).move_to(
            [x0 + self.kin(t.get_value())[2] - cam, self.C[1], 0]))
        trail = always_redraw(lambda: self.exhaust(t.get_value(), cam, x0))
        stars = self.make_stars(0.35 * cam)
        self.remove(self.rocket, self.trail, self.stars)
        self.add(stars, trail, rocket)
        txt = ("no road, no air:" + chr(10) + "just momentum, conserved") if self.PORTRAIT else "no road, no air: just momentum, conserved"
        label = crisp_text(txt, 22 if self.PORTRAIT else 34, color=INK, weight=BOLD, font=CAPTION_STYLE,
                           line_spacing=1.1).move_to([0, self.FINAL_Y, 0])
        if label.width > 2 * safe_half_w():
            label.scale_to_fit_width(2 * safe_half_w())
        # opaque backing so no star dot ever sits behind or through the text
        backing = SurroundingRectangle(label, buff=0.18, stroke_width=0, fill_color=CREAM, fill_opacity=1)
        final = VGroup(backing, label).set_z_index(10)
        t_exit = 3.0
        self.play(t.animate.set_value(self.T_BURN + 1.0 + t_exit), FadeOut(self.va), FadeOut(self.vl), FadeOut(self.ml),
                  run_time=t_exit, rate_func=linear)
        self.play(FadeIn(final, shift=UP * 0.15), t.animate.set_value(self.T_BURN + 1.0 + t_exit + 0.8),
                  run_time=0.8, rate_func=linear)
        rest = DURS["B04"] - t_exit - 0.8
        self.play(t.animate.set_value(self.T_BURN + 1.0 + t_exit + 0.8 + rest), run_time=rest, rate_func=linear)
