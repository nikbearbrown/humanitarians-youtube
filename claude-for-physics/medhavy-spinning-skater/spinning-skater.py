"""spinning-skater.py — Chapter 11.3, Conservation of Angular Momentum.

A skater with negligible external torque conserves L = I omega. Pulling her
arms in lowers I, so omega rises by I/I'; her kinetic energy K = L^2 / 2I
rises by the same factor, paid for by the work her muscles do pulling her
hands inward.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh spinning-skater.py SpinningSkater
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching spinning-skater.py SpinningSkater
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

SKIN = "#E0AC69"
HAIR = "#3B2416"
R_OUT, R_IN = 1.5, 0.5          # hand distance from the axis (model units)
L_CONST = 0.785 * (1 + R_OUT ** 2)   # omega_out = 0.785 rad/s (0.5 rev per 4 s)


def inertia(r):
    """I = I_body + 2 m r^2 with I_body = 1, 2m = 1 (model units)."""
    return 1.0 + r ** 2


def make_skater(th, r, S, ax):
    """Top-down skater: arms along local x, facing local +y; rotated by th
    about the axis point ax. r = hand distance from the axis (model units)."""
    sh = 0.32
    hx = max(r, sh + 0.08)
    arms = VGroup()
    for sgn in (1, -1):
        p0, p1 = np.array([sgn * sh, 0.02, 0]), np.array([sgn * hx, 0.02, 0])
        arms.add(Line(p0, p1, color=INK, stroke_width=13))
        arms.add(Line(p0, p1, color=SKIN, stroke_width=8))
    hands = VGroup(*[Circle(radius=0.085, color=INK, stroke_width=2, fill_color=SKIN, fill_opacity=1)
                     .move_to([sgn * hx, 0.02, 0]) for sgn in (1, -1)])
    dress = Ellipse(width=0.8, height=0.46, color=INK, stroke_width=2.5, fill_color=TEAL, fill_opacity=1)
    head = Circle(radius=0.19, color=INK, stroke_width=2, fill_color=SKIN, fill_opacity=1).move_to([0, 0.03, 0])
    hair = Circle(radius=0.165, stroke_width=0, fill_color=HAIR, fill_opacity=1).move_to([0, -0.02, 0])
    bun = Circle(radius=0.08, color=INK, stroke_width=1.5, fill_color=HAIR, fill_opacity=1).move_to([0, -0.2, 0])
    g = VGroup(arms, dress, hands, head, hair, bun)
    g.scale(S, about_point=ORIGIN).rotate(th, about_point=ORIGIN).shift(ax)
    return g


class SpinningSkater(MedhavyScene):
    def construct(self):
        self.PORTRAIT = P = PORTRAIT
        if P:
            self.AX = np.array([0, 0.9, 0])
            self.S = 0.8
            self.CARD = np.array([0, 3.0, 0])
            self.BASE = -1.85
            self.BAR_X = [-0.9, 0.0, 0.9]
            self.BAR_H = 1.4
            self.KE_X, self.KE_H0 = 1.35, 0.45
            self.FORM = np.array([-0.25, -1.25, 0])
            self.SUM_Y = [-0.75, -1.3, -1.85]
            self.SUM_X = -0.4
        else:
            self.AX = np.array([-3.2, -0.2, 0])
            self.S = 1.5
            self.CARD = np.array([2.2, 2.6, 0])
            self.BASE = -2.2
            self.BAR_X = [1.2, 2.2, 3.2]
            self.BAR_H = 2.4
            self.KE_X, self.KE_H0 = 5.3, 0.7
            self.FORM = np.array([2.2, 1.0, 0])
            self.SUM_Y = [0.6, -0.3, -1.2]
            self.SUM_X = 2.2
        self.MATH = 34 if P else 42
        self.LBL = 18 if P else 22

        self.th = PI / 2 - 0.3
        self.r = ValueTracker(R_OUT)

        if P:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_rule()
        self.b02_collapse()
        self.b03_energy()
        self.b04_hold()

    # helpers ----------------------------------------------------------
    def omega(self):
        return L_CONST / inertia(self.r.get_value())

    def hand_dir(self):
        return np.array([np.cos(self.th), np.sin(self.th), 0])

    def spin_updater(self, m, dt):
        self.th += self.omega() * dt
        m.become(make_skater(self.th, self.r.get_value(), self.S, self.AX))

    def bar(self, x, h, color, w=None):
        w = w or (0.32 if self.PORTRAIT else 0.5)
        h = max(h, 0.02)
        return Rectangle(width=w, height=h, color=INK, stroke_width=2, fill_color=color,
                         fill_opacity=1).move_to([x, self.BASE + h / 2, 0])

    # ---------------- B00 — slow spin, arms out ----------------
    def b00_hook(self):
        skater = make_skater(self.th, R_OUT, self.S, self.AX)
        circ = always_redraw(lambda: DashedVMobject(
            Circle(radius=self.r.get_value() * self.S, color=SLATE, stroke_width=2, stroke_opacity=0.6)
            .move_to(self.AX), num_dashes=40))
        label = crisp_text("no external torque", self.LBL + 4, color=SLATE, font=CAPTION_STYLE).move_to(
            [0, 3.0, 0] if self.PORTRAIT else [0, 3.2, 0])
        self.play(FadeIn(skater), FadeIn(circ), run_time=0.8)
        skater.add_updater(self.spin_updater)
        self.play(FadeIn(label), run_time=0.6)
        self.wait(max(DURS["B00"] - 1.4, 0.3))
        self.skater, self.circ, self.top_label = skater, circ, label

    # ---------------- B01 — radius arrow, L = I omega card ----------------
    def b01_rule(self):
        P = self.PORTRAIT

        def r_arrow_mob():
            d = self.hand_dir()
            n = np.array([-d[1], d[0], 0])
            off = n * (0.2 if P else 0.28)
            end = self.AX + d * self.r.get_value() * self.S + off
            return Arrow(self.AX + off, end, buff=0, color=CRIMSON, stroke_width=5, tip_length=0.16,
                         max_tip_length_to_length_ratio=0.3)

        def r_label_mob():
            d = self.hand_dir()
            n = np.array([-d[1], d[0], 0])
            p = self.AX + d * self.r.get_value() * self.S * 0.55 + n * (0.42 if P else 0.55)
            return MathTex("r", font_size=self.MATH, color=CRIMSON).move_to(p)

        r_arrow = always_redraw(r_arrow_mob)
        r_label = always_redraw(r_label_mob)
        card = MathTex("L", "=", "I", r"\omega", font_size=self.MATH + 8, color=INK).move_to(self.CARD)
        note = crisp_text("L points out of the page", self.LBL, color=SLATE, font=CAPTION_STYLE).next_to(card, DOWN, buff=0.2)

        d = DURS["B01"]
        self.play(FadeOut(self.top_label), run_time=0.5)
        self.play(Write(card), run_time=1.5)
        self.wait(max(d * 0.3 - 2.0, 0.2))
        self.play(FadeIn(r_arrow), FadeIn(r_label), run_time=0.8)
        self.wait(max(d * 0.62 - (max(d * 0.3 - 2.0, 0.2) + 2.8), 0.2))
        self.play(FadeIn(note), run_time=0.6)
        used = 0.5 + 1.5 + max(d * 0.3 - 2.0, 0.2) + 0.8 + max(d * 0.62 - (max(d * 0.3 - 2.0, 0.2) + 2.8), 0.2) + 0.6
        self.wait(max(d - used, 0.2))
        self.card, self.note, self.r_arrow, self.r_label = card, note, r_arrow, r_label

    # ---------------- B02 — collapse: I down, omega up, L constant ----------------
    def b02_collapse(self):
        H = self.BAR_H
        I_out = inertia(R_OUT)

        def bars_mob():
            I = inertia(self.r.get_value())
            return VGroup(
                self.bar(self.BAR_X[0], H * I / I_out, SLATE),
                self.bar(self.BAR_X[1], H * inertia(R_IN) / I, TEAL),
                self.bar(self.BAR_X[2], H * 0.75, INK),
            )

        bars = always_redraw(bars_mob)
        labs = VGroup(
            MathTex("I", font_size=self.MATH, color=SLATE),
            MathTex(r"\omega", font_size=self.MATH, color=TEAL),
            MathTex(r"L", font_size=self.MATH, color=INK),
        )
        for lab, x in zip(labs, self.BAR_X):
            lab.move_to([x, self.BASE - 0.22, 0])
        check = MathTex(r"\checkmark", font_size=self.MATH, color=TEAL).move_to(
            [self.BAR_X[2], self.BASE + H * 0.75 + 0.3, 0])

        d = DURS["B02"]
        self.play(FadeIn(bars), FadeIn(labs), run_time=0.7)
        self.wait(0.6)
        t_col = 3.5
        self.play(self.r.animate.set_value(R_IN), run_time=t_col, rate_func=rate_functions.ease_in_out_sine)
        self.play(FadeIn(check, scale=1.5), run_time=0.5)
        self.wait(max(d - (0.7 + 0.6 + t_col + 0.5) - 0.6, 0.2))
        self.play(FadeOut(bars), FadeOut(labs), FadeOut(check), run_time=0.6)

    # ---------------- B03 — energy: K = L^2 / 2I, muscle work ----------------
    def b03_energy(self):
        P = self.PORTRAIT
        I_out = inertia(R_OUT)

        def ke_mob():
            return self.bar(self.KE_X, self.KE_H0 * I_out / inertia(self.r.get_value()), GOLD)

        ke = always_redraw(ke_mob)
        ke_lab = MathTex("K", font_size=self.MATH, color=INK).move_to([self.KE_X, self.BASE - 0.22, 0])
        form = MathTex(r"K", "=", r"\tfrac{1}{2} I\omega^2", "=", r"\frac{L^2}{2I}",
                       font_size=self.MATH, color=INK).move_to(self.FORM)
        if form.width > (2.7 if P else 4.0):
            form.scale_to_fit_width(2.7 if P else 4.0)

        def work_mob():
            d = self.hand_dir()
            rr = self.r.get_value() * self.S
            g = VGroup()
            for sgn in (1, -1):
                hand = self.AX + sgn * d * rr
                g.add(Arrow(hand + sgn * d * (0.62 if P else 0.85), hand + sgn * d * 0.14, buff=0,
                            color=INK, stroke_width=5, tip_length=0.15, max_tip_length_to_length_ratio=0.35))
            return g

        work = always_redraw(work_mob)
        work_lab = crisp_text("muscle work", self.LBL, color=INK, font=CAPTION_STYLE)
        work_lab.move_to(self.AX + (DOWN * 1.55 if P else DOWN * 2.75))

        n = [4, 16, 14, 5, 17, 13]
        d = DURS["B03"]
        cue = np.cumsum([0] + n) / sum(n) * d
        t = 0.0
        # arms back out (energy falls with them), KE bar tied to the same r
        self.play(FadeIn(ke), FadeIn(ke_lab), run_time=0.5)
        self.play(self.r.animate.set_value(R_OUT), run_time=1.6, rate_func=rate_functions.ease_in_out_sine)
        t += 2.1
        self.wait(max(cue[1] - t, 0.2)); t = max(cue[1], t + 0.2)
        self.play(Write(form), run_time=1.8)
        t += 1.8
        self.wait(max(cue[2] - t, 0.2)); t = max(cue[2], t + 0.2)
        self.play(Indicate(form[4], color=CRIMSON), run_time=1.2)
        t += 1.2
        self.wait(max(cue[4] - t, 0.2)); t = max(cue[4], t + 0.2)
        # pull in again: work arrows on the hands, KE grows on the same interpolator
        self.play(FadeIn(work), FadeIn(work_lab), run_time=0.6)
        self.play(self.r.animate.set_value(R_IN), run_time=4.0, rate_func=rate_functions.ease_in_out_sine)
        t += 4.6
        self.wait(max(d - t, 0.2))
        self.ke, self.ke_lab, self.form, self.work, self.work_lab = ke, ke_lab, form, work, work_lab

    # ---------------- B04 — summary, labels snap in ----------------
    def b04_hold(self):
        self.play(FadeOut(self.form), FadeOut(self.work), FadeOut(self.work_lab), FadeOut(self.note),
                  FadeOut(self.r_arrow), FadeOut(self.r_label), run_time=0.6)
        labels = [
            MathTex(r"L", r"\text{ stays constant}", font_size=self.MATH, color=INK),
            MathTex(r"I \downarrow \quad \omega \uparrow", font_size=self.MATH, color=TEAL),
            MathTex(r"\text{extra } K = \text{muscle work}", font_size=self.MATH, color=INK),
        ]
        maxw = 2.3 if self.PORTRAIT else 4.6
        for lab, y in zip(labels, self.SUM_Y):
            if lab.width > maxw:
                lab.scale_to_fit_width(maxw)
            lab.move_to([self.SUM_X, y, 0])
        d = DURS["B04"]
        # snap in (no fade), one per clause of the narration
        gaps = [d * 0.08, d * 0.25, d * 0.25]
        for lab, g in zip(labels, gaps):
            self.wait(g)
            self.add(lab)
        self.wait(max(d - 0.6 - sum(gaps), 0.3))
