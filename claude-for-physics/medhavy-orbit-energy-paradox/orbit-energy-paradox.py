"""orbit-energy-paradox.py — Chapter 13.4, Satellite Orbits and Energy.

For a circular orbit K = GMm/2r, U = -GMm/r, E = -GMm/2r = -K. A forward
burn adds energy (E less negative) -> larger r -> smaller K: higher and
slower. A backward burn removes energy -> smaller r -> larger K: lower and
faster. One radius tracker drives orbit, satellite, speed arrow
(|v| ~ r^-1/2) and the energy bars (K ~ 1/r, U = -2K, E = -K).

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh orbit-energy-paradox.py OrbitEnergyParadox
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching orbit-energy-paradox.py OrbitEnergyParadox
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

OCEAN = "#56B4E9"   # Okabe-Ito sky blue


def cues(n, d):
    return np.cumsum([0] + list(n)) / sum(n) * d


def make_earth(r):
    sea = Circle(radius=r, color=INK, stroke_width=2, fill_color=OCEAN, fill_opacity=1)
    land1 = Ellipse(width=r * 0.9, height=r * 0.6, stroke_width=0, fill_color=TEAL, fill_opacity=1).move_to(
        [-r * 0.25, r * 0.3, 0]).rotate(0.5)
    land2 = Ellipse(width=r * 0.55, height=r * 0.8, stroke_width=0, fill_color=TEAL, fill_opacity=1).move_to(
        [r * 0.35, -r * 0.3, 0]).rotate(-0.3)
    return VGroup(sea, land1, land2)


def make_sat(s):
    body = Square(side_length=0.17 * s, color=INK, stroke_width=1.5, fill_color=GOLD, fill_opacity=1)
    pl = Rectangle(width=0.24 * s, height=0.09 * s, color=INK, stroke_width=1, fill_color=SLATE, fill_opacity=1)
    pr = pl.copy()
    pl.next_to(body, LEFT, buff=0.03 * s)
    pr.next_to(body, RIGHT, buff=0.03 * s)
    return VGroup(pl, pr, body)


class OrbitEnergyParadox(MedhavyScene):
    def construct(self):
        self.PORTRAIT = P = PORTRAIT
        if P:
            self.OC = np.array([0, 1.95, 0])
            self.R1, self.R2, self.R3 = 0.8, 1.15, 0.5
            self.ER, self.V1, self.SS = 0.28, 0.55, 0.8
            self.EQ = np.array([0, -0.15, 0])
            self.Z, self.KS = 0.35, 0.5
            self.ROWS = [-1.3, -1.7, -2.1]
            self.BH = 0.3
        else:
            self.OC = np.array([-3.4, -0.2, 0])
            self.R1, self.R2, self.R3 = 1.5, 2.6, 0.95
            self.ER, self.V1, self.SS = 0.55, 1.0, 1.2
            self.EQ = np.array([3.0, 2.3, 0])
            self.Z, self.KS = 3.2, 0.9
            self.ROWS = [0.5, -0.2, -0.9]
            self.BH = 0.42
        self.MATH = 32 if P else 40
        self.LBL = 17 if P else 22
        self.r = ValueTracker(self.R1)
        self.ang = ValueTracker(0.0)

        if P:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_energy()
        self.b02_forward()
        self.b03_backward()
        self.b04_hold()

    # ---------------- helpers ----------------
    def sat_pos(self):
        a = self.ang.get_value()
        return self.OC + self.r.get_value() * np.array([np.cos(a), np.sin(a), 0])

    def tangent(self):
        a = self.ang.get_value()
        return np.array([-np.sin(a), np.cos(a), 0])      # counterclockwise

    def radial(self):
        a = self.ang.get_value()
        return np.array([np.cos(a), np.sin(a), 0])

    def speed_len(self):
        return self.V1 * np.sqrt(self.R1 / self.r.get_value())

    def orbit_mob(self):
        return DashedVMobject(Circle(radius=self.r.get_value(), color=SLATE, stroke_width=2.5).move_to(self.OC),
                              num_dashes=int(30 + 18 * self.r.get_value()))

    def sat_mob(self):
        return make_sat(self.SS).rotate(self.ang.get_value() - PI / 2).move_to(self.sat_pos())

    def v_mob(self):
        t = self.tangent()
        p0 = self.sat_pos() + t * 0.45 * self.SS
        return Arrow(p0, p0 + t * self.speed_len(), buff=0, color=INK, stroke_width=6, tip_length=0.18,
                     max_tip_length_to_length_ratio=0.3)

    def v_label(self, tex):
        def f():
            t = self.tangent()
            tip = self.sat_pos() + t * (0.45 * self.SS + self.speed_len())
            m = MathTex(tex, font_size=self.MATH, color=INK)
            if self.PORTRAIT:
                # narrow frame: label above the arrow, not past its tip
                mid = self.sat_pos() + t * (0.45 * self.SS + self.speed_len() / 2)
                return m.move_to(mid + self.radial() * 0.3)
            return m.next_to(tip, t if abs(t[0]) > 0.5 else RIGHT, buff=0.12)
        return f

    def thrust(self, sign):
        t = self.tangent() * sign
        p0 = self.sat_pos() + self.radial() * (0.3 if self.PORTRAIT else 0.38) - t * 0.25
        return Arrow(p0, p0 + t * (0.6 if self.PORTRAIT else 0.85), buff=0, color=CRIMSON, stroke_width=7,
                     tip_length=0.2, max_tip_length_to_length_ratio=0.35)

    def flash(self, arrow):
        self.add(arrow)
        self.wait(0.4)
        self.remove(arrow)
        self.wait(0.3)
        self.add(arrow)
        self.wait(0.4)
        self.play(FadeOut(arrow), run_time=0.3)
        return 1.4

    def bar(self, y, val, color):
        w = max(abs(val), 0.02)
        x0 = self.Z if val >= 0 else self.Z - w
        return Rectangle(width=w, height=self.BH, color=INK, stroke_width=1.5, fill_color=color,
                         fill_opacity=1).move_to([x0 + w / 2, y, 0])

    def K_val(self):
        return self.KS * self.R1 / self.r.get_value()

    def set_label(self, tex):
        new = always_redraw(self.v_label(tex))
        self.play(FadeOut(self.vl), FadeIn(new), run_time=0.4)
        self.vl = new
        return 0.4

    # ---------------- B00 — forward burn -> higher, slower ----------------
    def b00_hook(self):
        d = DURS["B00"]
        c = cues([4, 11, 21, 9], d)
        self.earth = make_earth(self.ER).move_to(self.OC)
        self.orbit = always_redraw(self.orbit_mob)
        self.sat = always_redraw(self.sat_mob)
        t = 0.0
        self.play(FadeIn(self.earth), FadeIn(self.orbit), FadeIn(self.sat), run_time=1.0); t += 1.0
        self.play(self.ang.animate.set_value(PI / 2), run_time=2.2, rate_func=linear); t += 2.2
        self.v = always_redraw(self.v_mob)
        self.vl = always_redraw(self.v_label("v_1"))
        self.play(GrowArrow(self.v), FadeIn(self.vl), run_time=0.6); t += 0.6
        self.wait(max(c[1] - t, 0.2)); t = max(c[1], t + 0.2)
        t += self.flash(self.thrust(+1))
        self.ghost = DashedVMobject(Circle(radius=self.R1, color=SLATE, stroke_width=1.5).move_to(self.OC),
                                    num_dashes=40).set_stroke(opacity=0.35)
        self.add(self.ghost)
        self.play(self.r.animate.set_value(self.R2), run_time=3.0, rate_func=rate_functions.ease_in_out_sine); t += 3.0
        t += self.set_label(r"v_2 < v_1")
        self.wait(max(d - t, 0.2))

    # ---------------- B01 — K, U, E for a circular orbit ----------------
    def b01_energy(self):
        d = DURS["B01"]
        c = cues([25, 10, 12, 13], d)
        P = self.PORTRAIT
        t = 0.0
        self.play(FadeOut(self.ghost), self.r.animate.set_value(self.R1), FadeOut(self.vl), run_time=1.0); t += 1.0
        self.vl = always_redraw(self.v_label("v_1"))
        self.play(FadeIn(self.vl), run_time=0.3); t += 0.3

        top_y = self.ROWS[0] + self.BH / 2 + 0.12
        bot_y = self.ROWS[2] - self.BH / 2 - 0.12
        zero = Line([self.Z, top_y, 0], [self.Z, bot_y, 0], color=INK, stroke_width=2.5)
        zl = MathTex("0", font_size=self.MATH - 8, color=INK).next_to(zero, UP, buff=0.08)
        self.Kb = always_redraw(lambda: self.bar(self.ROWS[0], self.K_val(), TEAL))
        self.Ub = always_redraw(lambda: self.bar(self.ROWS[1], -2 * self.K_val(), CRIMSON))
        self.Eb = always_redraw(lambda: self.bar(self.ROWS[2], -self.K_val(), SLATE))
        lk = MathTex("K", font_size=self.MATH, color=TEAL).move_to([self.Z - 0.28, self.ROWS[0], 0])
        lu = MathTex("U", font_size=self.MATH, color=CRIMSON).move_to([self.Z + 0.28, self.ROWS[1], 0])
        le = MathTex("E", font_size=self.MATH, color=INK).move_to([self.Z + 0.28, self.ROWS[2], 0])
        maxw = 3.6 if P else 5.6

        def eq(tex):
            m = MathTex(*tex, font_size=self.MATH + 4, color=INK)
            if m.width > maxw:
                m.scale_to_fit_width(maxw)
            return m.move_to(self.EQ)

        eqK = eq(["K", "=", r"\frac{GMm}{2r}"])
        eqU = eq(["U", "=", r"-\frac{GMm}{r}"])
        eqE = eq(["E", "=", r"-\frac{GMm}{2r}", "=", "-K"])
        eqK[0].set_color(TEAL)
        eqU[0].set_color(CRIMSON)

        self.wait(max(c[1] * 0.55 - t, 0.2)); t = max(c[1] * 0.55, t + 0.2)
        self.play(Write(eqK), Create(zero), FadeIn(zl), run_time=1.0); t += 1.0
        self.play(FadeIn(self.Kb), FadeIn(lk), run_time=0.6); t += 0.6
        self.wait(max(c[1] - t, 0.2)); t = max(c[1], t + 0.2)
        self.play(ReplacementTransform(eqK, eqU), FadeIn(self.Ub), FadeIn(lu), run_time=1.0); t += 1.0
        self.wait(max(c[2] - t, 0.2)); t = max(c[2], t + 0.2)
        self.play(ReplacementTransform(eqU, eqE), FadeIn(self.Eb), FadeIn(le), run_time=1.0); t += 1.0
        self.wait(max(c[3] - t, 0.2)); t = max(c[3], t + 0.2)
        self.play(Indicate(eqE[4], color=CRIMSON), run_time=1.0); t += 1.0
        self.wait(max(d - t, 0.2))
        self.eqE, self.zero, self.zl, self.blabels = eqE, zero, zl, VGroup(lk, lu, le)

    # ---------------- B02 — forward burn: E up, r up, K down ----------------
    def b02_forward(self):
        d = DURS["B02"]
        c = cues([10, 19, 15, 7], d)
        t = 0.0
        t += self.flash(self.thrust(+1))
        self.play(self.r.animate.set_value(self.R2), run_time=4.0, rate_func=rate_functions.ease_in_out_sine); t += 4.0
        self.wait(max(c[2] - t, 0.2)); t = max(c[2], t + 0.2)
        self.play(Indicate(self.blabels[0], color=TEAL, scale_factor=1.4), run_time=1.0); t += 1.0
        self.wait(max(c[3] - t, 0.2)); t = max(c[3], t + 0.2)
        t += self.set_label(r"v_2 < v_1")
        self.wait(max(d - t, 0.2))

    # ---------------- B03 — backward burn: E down, r down, K up ----------------
    def b03_backward(self):
        d = DURS["B03"]
        c = cues([4, 17, 9], d)
        t = 0.0
        self.play(self.r.animate.set_value(self.R1), FadeOut(self.vl), run_time=1.0); t += 1.0
        self.vl = always_redraw(self.v_label("v_1"))
        self.play(FadeIn(self.vl), run_time=0.3); t += 0.3
        self.wait(max(c[1] - t, 0.2)); t = max(c[1], t + 0.2)
        t += self.flash(self.thrust(-1))
        self.play(self.r.animate.set_value(self.R3), run_time=3.5, rate_func=rate_functions.ease_in_out_sine); t += 3.5
        self.wait(max(c[2] - t, 0.2)); t = max(c[2], t + 0.2)
        t += self.set_label(r"v_3 > v_1")
        self.wait(max(d - t, 0.2))

    # ---------------- B04 — both orbits labeled, equation stays ----------------
    def b04_hold(self):
        d = DURS["B04"]
        P = self.PORTRAIT
        outer = DashedVMobject(Circle(radius=self.R2, color=SLATE, stroke_width=2).move_to(self.OC),
                               num_dashes=70).set_stroke(opacity=0.6)
        hi = crisp_text("higher: more E, slower", self.LBL, color=SLATE, font=CAPTION_STYLE)
        lo = crisp_text("lower: less E, faster", self.LBL, color=INK, font=CAPTION_STYLE)
        anims = [Create(outer), FadeOut(self.vl)]
        if P:
            hi.move_to([0, self.OC[1] + self.R2 + 0.3, 0])
            lo.move_to([0, -0.15, 0])
            anims += [FadeOut(VGroup(self.Kb, self.Ub, self.Eb, self.zero, self.zl, self.blabels)),
                      self.eqE.animate.move_to([0, -1.25, 0])]
        else:
            hi.move_to(self.OC + np.array([self.R2 + 0.2 + hi.width / 2, 1.5, 0]))
            lo.move_to(self.OC + np.array([0, -1.5, 0]))
        self.play(*anims, run_time=1.0)
        self.play(FadeIn(hi), run_time=0.5)
        self.play(FadeIn(lo), run_time=0.5)
        self.wait(max(d - 2.0, 0.3))
