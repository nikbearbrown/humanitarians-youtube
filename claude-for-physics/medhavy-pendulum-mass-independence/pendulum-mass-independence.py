"""pendulum-mass-independence.py — Chapter 15, 15.4 Pendulums.

Two equal-length pendulums, 10 kg and 1 kg, swing in lockstep. Mass
multiplies both the restoring force (-mg sin theta) and the inertia (ma), so
it cancels: a = -g sin theta, and T = 2 pi sqrt(L/g).

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh pendulum-mass-independence.py PendulumMassIndependence
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching pendulum-mass-independence.py PendulumMassIndependence
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

HEAVY = "#4D4D4D"
LIGHT = "#E69F00"      # Okabe-Ito orange
THETA0 = 12 * DEGREES  # small angle (< 15 degrees, 15.4)
PERIOD = 2.6           # on-screen period, identical for both (same L)
OMEGA = 2 * PI / PERIOD

if PORTRAIT:
    BEAM_Y, PIV_X, L = 2.8, [-0.8, 0.8], 2.0
    R_HEAVY, R_LIGHT = 0.26, 0.11
    W_HEAVY = 1.1
    LBL, EQ, TXT = 26, 32, 18
    EQ_Y = [0.1, -0.6, -1.6]
    EQ_X = 0.0
    Q_POS = np.array([0, -1.5, 0])
else:
    BEAM_Y, PIV_X, L = 2.8, [-5.0, -2.2], 3.9
    R_HEAVY, R_LIGHT = 0.45, 0.21
    W_HEAVY = 1.7
    LBL, EQ, TXT = 44, 60, 34
    EQ_Y = [1.9, 0.3, -1.4]
    EQ_X = 3.4
    Q_POS = np.array([3.4, 0.3, 0])


class PendulumMassIndependence(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])
        self.t = 0.0
        self.b00_hook()
        self.b01_naive()
        self.b02_cancel()
        self.b03_period()
        self.b04_hold()

    # ---- one shared angle for both pendulums: exact lockstep ----
    def theta(self):
        return THETA0 * np.cos(OMEGA * self.t)

    def bob_pos(self, i):
        th = self.theta()
        return np.array([PIV_X[i] + L * np.sin(th), BEAM_Y - L * np.cos(th), 0])

    def pendulum(self, i):
        r = R_HEAVY if i == 0 else R_LIGHT
        col = HEAVY if i == 0 else LIGHT
        p = self.bob_pos(i)
        piv = np.array([PIV_X[i], BEAM_Y, 0])
        d = (p - piv) / np.linalg.norm(p - piv)
        string = Line(piv, p - d * r, color=INK, stroke_width=2.5)
        bob = Circle(radius=r, color=INK, fill_color=col, fill_opacity=1, stroke_width=2.5).move_to(p)
        return VGroup(string, bob)

    def weight_arrow(self, i):
        r = R_HEAVY if i == 0 else R_LIGHT
        length = W_HEAVY if i == 0 else W_HEAVY / 10
        p = self.bob_pos(i) + DOWN * (r + 0.03)
        return Arrow(p, p + DOWN * length, buff=0, color=CRIMSON, stroke_width=7 if i == 0 else 5,
                     max_tip_length_to_length_ratio=0.18 if i == 0 else 0.9,
                     max_stroke_width_to_length_ratio=60)

    # ---------------- B00 — lockstep ----------------
    def b00_hook(self):
        clock = Mobject()

        def tick(m, dt):
            self.t += dt
        clock.add_updater(tick)
        self.add(clock)
        self.clock = clock

        beam = Line([PIV_X[0] - 0.9, BEAM_Y, 0], [PIV_X[1] + 0.9, BEAM_Y, 0], color=INK, stroke_width=6)
        hatch = VGroup(*[Line([x, BEAM_Y, 0], [x + 0.15, BEAM_Y + 0.15, 0], color=INK, stroke_width=2)
                         for x in np.linspace(PIV_X[0] - 0.8, PIV_X[1] + 0.65, 10)])
        self.beam = VGroup(beam, hatch)
        self.pends = VGroup(always_redraw(lambda: self.pendulum(0)), always_redraw(lambda: self.pendulum(1)))
        lh = crisp_text("10 kg", TXT, color=INK, font=CAPTION_STYLE)
        ll = crisp_text("1 kg", TXT, color=INK, font=CAPTION_STYLE)
        lh.next_to(np.array([PIV_X[0], BEAM_Y, 0]), UP, buff=0.25)
        ll.next_to(np.array([PIV_X[1], BEAM_Y, 0]), UP, buff=0.25)
        self.mass_lbls = VGroup(lh, ll)
        self.play(Create(self.beam), FadeIn(self.pends), FadeIn(self.mass_lbls), run_time=1.0)
        self.wait(max(DURS["B00"] - 1.0, 0.1))

    # ---------------- B01 — naive guess ----------------
    def b01_naive(self):
        self.w_arrows = VGroup(always_redraw(lambda: self.weight_arrow(0)), always_redraw(lambda: self.weight_arrow(1)))
        self.w_lbl = MathTex("mg", font_size=LBL, color=CRIMSON)
        self.w_lbl.add_updater(lambda m: m.next_to(self.w_arrows[0], LEFT, buff=0.12))
        self.play(FadeIn(self.w_arrows), FadeIn(self.w_lbl), run_time=0.6)
        self.q = crisp_text("heavier = faster?", TXT, color=CRIMSON, font=CAPTION_STYLE).move_to(Q_POS)
        self.play(FadeIn(self.q), run_time=0.5)
        self.wait(max(DURS["B01"] - 1.1, 0.1))

    # ---------------- B02 — m appears twice and cancels ----------------
    def b02_cancel(self):
        self.play(FadeOut(self.w_arrows), FadeOut(self.w_lbl), FadeOut(self.q), run_time=0.5)
        self.w_lbl.clear_updaters()

        def row(tex_parts, label, y):
            eq = MathTex(*tex_parts, font_size=EQ, color=INK)
            tag = crisp_text(label, TXT - 4, color=SLATE, font=CAPTION_STYLE)
            g = VGroup(eq, tag).arrange(DOWN, buff=0.1) if self.PORTRAIT else VGroup(eq, tag).arrange(DOWN, buff=0.12)
            return g.move_to([EQ_X, y, 0])

        self.r1 = row([r"F = -", "m", r"g\sin\theta"], "restoring force", EQ_Y[0])
        self.r2 = row([r"F = ", "m", "a"], "inertia", EQ_Y[1])
        self.r1[0][1].set_color(CRIMSON)
        self.r2[0][1].set_color(CRIMSON)
        self.play(Write(self.r1), run_time=0.9)
        w1 = max(DURS["B02"] * 0.35 - 1.4, 0.1)
        self.wait(w1)
        self.play(Write(self.r2), run_time=0.9)

        self.r3 = MathTex("m", "a", "= -", "m", r"g\sin\theta", font_size=EQ, color=INK).move_to([EQ_X, EQ_Y[2], 0])
        self.r3[0].set_color(CRIMSON)
        self.r3[3].set_color(CRIMSON)
        w2 = max(DURS["B02"] * 0.7 - (1.4 + w1 + 0.9), 0.1)
        self.wait(w2)
        self.play(Write(self.r3), run_time=0.9)
        self.wait(0.6)
        crosses = VGroup(*[Line(self.r3[k].get_corner(DL), self.r3[k].get_corner(UR),
                                color=CRIMSON, stroke_width=5) for k in (0, 3)])
        self.crosses = crosses
        self.play(Create(crosses), run_time=0.7)
        self.wait(max(DURS["B02"] - (0.5 + 0.9 + w1 + 0.9 + w2 + 0.9 + 0.6 + 0.7), 0.1))

    # ---------------- B03 — what remains: T = 2 pi sqrt(L/g) ----------------
    def b03_period(self):
        a_eq = MathTex(r"a = -g\sin\theta", font_size=EQ, color=INK).move_to([EQ_X, EQ_Y[0], 0])
        self.play(FadeOut(self.r1), FadeOut(self.r2), FadeOut(self.crosses),
                  ReplacementTransform(self.r3, a_eq), run_time=1.0)
        self.a_eq = a_eq
        w1 = max(DURS["B03"] * 0.3 - 1.0, 0.1)
        self.wait(w1)
        small = MathTex(r"\sin\theta \approx \theta", font_size=EQ - 6, color=SLATE).move_to([EQ_X, EQ_Y[1], 0])
        self.play(FadeIn(small), run_time=0.6)
        self.small = small
        w2 = max(DURS["B03"] * 0.55 - (1.0 + w1 + 0.6), 0.1)
        self.wait(w2)
        T_eq = MathTex(r"T = 2\pi\sqrt{\frac{L}{g}}", font_size=EQ if self.PORTRAIT else EQ + 4, color=INK).move_to([EQ_X, EQ_Y[2], 0])
        box = SurroundingRectangle(T_eq, color=TEAL, buff=0.15, stroke_width=4)
        no_m = crisp_text("no m", TXT, color=TEAL, font=CAPTION_STYLE).next_to(box, RIGHT, buff=0.2)
        self.play(Write(T_eq), Create(box), run_time=1.0)
        self.play(FadeIn(no_m), run_time=0.5)
        self.T_group = VGroup(T_eq, box, no_m)
        self.wait(max(DURS["B03"] - (1.0 + w1 + 0.6 + w2 + 1.5), 0.1))

    # ---------------- B04 — hold ----------------
    def b04_hold(self):
        summary = crisp_text("SAME LENGTH, SAME PERIOD", TXT, color=INK, font=CAPTION_STYLE)
        summary.move_to([EQ_X, EQ_Y[0], 0])
        self.play(FadeOut(self.a_eq), FadeOut(self.small), run_time=0.5)
        self.play(FadeIn(summary), run_time=0.6)
        self.summary = summary
        self.wait(max(DURS["B04"] - 1.1, 0.1))
