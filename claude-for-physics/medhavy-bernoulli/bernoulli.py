"""bernoulli.py — Chapter 14, 14.6 Bernoulli's Equation.

Level pipe narrows -> continuity forces faster flow in the neck -> a net
forward force (higher pressure behind) is needed -> neck pressure is lower.
Bernoulli's principle: p + (1/2) rho v^2 = constant along a streamline.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh bernoulli.py Bernoulli
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching bernoulli.py Bernoulli
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

WATER = "#56B4E9"
TRACER = "#0072B2"

if PORTRAIT:
    L, YC, H1, H2, NH, TR = 1.65, 1.0, 0.42, 0.19, 0.2, 0.55
    GX = [-1.1, 0.0, 1.1]
    DIAL_Y, DIAL_R = 2.0, 0.22
    V_Y, V1_LEN = 0.36, 0.3
    EQ_POS = np.array([0, 2.85, 0])
    BAR_BASE, BAR_H, BAR_W = -2.0, 1.5, 0.36
    SPACING, DOT_R, V1 = 0.22, 0.022, 0.35
    LBL, EQ, TXT = 26, 34, 18
else:
    L, YC, H1, H2, NH, TR = 6.2, 1.0, 0.85, 0.38, 0.5, 1.6
    GX = [-4.2, 0.0, 4.2]
    DIAL_Y, DIAL_R = 2.85, 0.4
    V_Y, V1_LEN = -0.2, 0.6
    EQ_POS = np.array([0, -1.0, 0])
    BAR_BASE, BAR_H, BAR_W = -3.35, 1.8, 0.55
    SPACING, DOT_R, V1 = 0.55, 0.04, 0.9
    LBL, EQ, TXT = 38, 46, 26

TOTAL = 3.0
KE1 = 0.45
KE2 = KE1 * (H1 / H2) ** 2      # v_2 / v_1 = A_1 / A_2 = H1 / H2 (2D cross-section)
P1, P2 = TOTAL - KE1, TOTAL - KE2
STREAMS = [-0.7, -0.35, 0.0, 0.35, 0.7]


def bump(x):
    ax = abs(x)
    if ax <= NH:
        return 1.0
    if ax >= NH + TR:
        return 0.0
    return 0.5 * (1 + np.cos(PI * (ax - NH) / TR))


def half_h(x, a):
    return H1 - a * (H1 - H2) * bump(x)


def needle_angle(p):
    return PI * (1 - p / TOTAL)


class Bernoulli(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        self.a = ValueTracker(0.0)
        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])
        self.b00_hook()
        self.b01_narrow()
        self.b02_pressure()
        self.b03_bernoulli()
        self.b04_hold()

    # ---- pipe geometry ----
    def xs(self):
        return np.linspace(-L, L, 161)

    def walls(self):
        a = self.a.get_value()
        top = [np.array([x, YC + half_h(x, a), 0]) for x in self.xs()]
        bot = [np.array([x, YC - half_h(x, a), 0]) for x in self.xs()]
        t = VMobject(color=INK, stroke_width=5).set_points_smoothly(top)
        b = VMobject(color=INK, stroke_width=5).set_points_smoothly(bot)
        return VGroup(t, b)

    def fill(self):
        a = self.a.get_value()
        top = [np.array([x, YC + half_h(x, a), 0]) for x in self.xs()]
        bot = [np.array([x, YC - half_h(x, a), 0]) for x in self.xs()[::-1]]
        return Polygon(*top, *bot, stroke_width=0, fill_color=WATER, fill_opacity=0.4)

    def gauge(self, i):
        x = GX[i]
        c = np.array([x, DIAL_Y, 0])
        face = Circle(radius=DIAL_R, color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=3).move_to(c)
        ticks = VGroup(*[Line(c + 0.72 * DIAL_R * np.array([np.cos(t), np.sin(t), 0]),
                              c + 0.92 * DIAL_R * np.array([np.cos(t), np.sin(t), 0]),
                              color=SLATE, stroke_width=2) for t in np.linspace(0, PI, 7)])
        hub = Dot(c, radius=DIAL_R * 0.1, color=INK)
        return VGroup(face, ticks, hub)

    def needle(self, i, tracker):
        c = np.array([GX[i], DIAL_Y, 0])
        t = tracker.get_value()
        return Line(c, c + 0.8 * DIAL_R * np.array([np.cos(t), np.sin(t), 0]), color=CRIMSON, stroke_width=4)

    def stem(self, i):
        x = GX[i]
        return Line([x, YC + half_h(x, self.a.get_value()), 0], [x, DIAL_Y - DIAL_R, 0], color=INK, stroke_width=4)

    def bar(self, x, p, ke):
        hp, hk = BAR_H * p / TOTAL, BAR_H * ke / TOTAL
        pr = Rectangle(width=BAR_W, height=hp, color=INK, fill_color=TEAL, fill_opacity=1, stroke_width=1.5)
        pr.move_to([x, BAR_BASE + hp / 2, 0])
        kr = Rectangle(width=BAR_W, height=hk, color=INK, fill_color=GOLD, fill_opacity=1, stroke_width=1.5)
        kr.move_to([x, BAR_BASE + hp + hk / 2, 0])
        return VGroup(pr, kr)

    # ---------------- B00 — uniform pipe, steady flow, equal gauges ----------------
    def b00_hook(self):
        self.pipe_fill = always_redraw(self.fill)
        self.pipe_walls = always_redraw(self.walls)
        self.play(FadeIn(self.pipe_fill), Create(self.pipe_walls), run_time=1.0)

        n = int(round(2 * L / SPACING))
        sp = 2 * L / n          # exact: no gap where dots wrap around
        state = []
        dots = VGroup()
        for j, f in enumerate(STREAMS):
            for k in range(n):
                x = -L + (k + 0.5 * (j % 2)) * sp
                state.append([x, f])
                dots.add(Dot([x, YC + f * H1, 0], radius=DOT_R, color=TRACER))
        self.dot_state = np.array(state)

        def flow(m, dt):
            a = self.a.get_value()
            st = self.dot_state
            for idx, d in enumerate(m):
                x, f = st[idx]
                # midpoint substeps: plain Euler at frame dt bunches dots unevenly
                h = dt / 6
                for _ in range(6):
                    xm = x + 0.5 * h * V1 * H1 / half_h(x, a)
                    x += h * V1 * H1 / half_h(xm, a)
                if x > L:
                    x -= 2 * L
                st[idx, 0] = x
                d.move_to([x, YC + f * half_h(x, a), 0])

        dots.add_updater(flow)
        self.dots = dots
        self.play(FadeIn(dots), run_time=0.5)

        self.p_trackers = [ValueTracker(needle_angle(P1)) for _ in GX]
        self.gauges = VGroup(*[self.gauge(i) for i in range(3)])
        self.stems = VGroup(*[always_redraw(lambda i=i: self.stem(i)) for i in range(3)])
        self.needles = VGroup(*[always_redraw(lambda i=i: self.needle(i, self.p_trackers[i])) for i in range(3)])
        self.play(FadeIn(self.stems), FadeIn(self.gauges), FadeIn(self.needles), run_time=0.8)
        self.wait(max(DURS["B00"] - 2.3, 0.1))

    # ---------------- B01 — narrow the pipe: continuity ----------------
    def b01_narrow(self):
        self.play(self.a.animate.set_value(1.0), run_time=2.5, rate_func=smooth)

        def varrow(x, length, name):
            ar = Arrow([x - length / 2, V_Y, 0], [x + length / 2, V_Y, 0], buff=0, color=INK, stroke_width=6,
                       max_tip_length_to_length_ratio=0.35 if length < 1 else 0.2,
                       max_stroke_width_to_length_ratio=40)
            lb = MathTex(name, font_size=LBL, color=INK).next_to(ar, DOWN, buff=0.08)
            return VGroup(ar, lb)

        v2_len = V1_LEN * H1 / H2
        self.varrows = VGroup(varrow(GX[0], V1_LEN, "v_1"), varrow(GX[1], v2_len, "v_2"), varrow(GX[2], V1_LEN, "v_1"))
        self.play(*[GrowArrow(v[0]) for v in self.varrows], *[FadeIn(v[1]) for v in self.varrows], run_time=0.8)

        self.eq = MathTex(r"A_1 v_1 = A_2 v_2", font_size=EQ, color=INK).move_to(EQ_POS)
        self.play(Write(self.eq), run_time=0.8)
        self.wait(max(DURS["B01"] - 4.1, 0.1))

    # ---------------- B02 — neck pressure drops ----------------
    def b02_pressure(self):
        names = ["p_1", "p_2", "p_1"]
        y_lbl = (YC + H1 + DIAL_Y - DIAL_R) / 2
        self.g_lbls = VGroup(*[MathTex(n, font_size=LBL, color=INK).move_to([GX[i], y_lbl, 0])
                               for i, n in enumerate(names)])
        for i, m in enumerate(self.g_lbls):
            m.next_to(np.array([GX[i], y_lbl, 0]), RIGHT, buff=0.08)
        self.play(FadeIn(self.g_lbls), run_time=0.6)

        w1 = max(DURS["B02"] * 0.55 - 0.6, 0.1)
        self.wait(w1)
        self.play(self.p_trackers[1].animate.set_value(needle_angle(P2)), run_time=0.8, rate_func=smooth)
        eq2 = MathTex(r"p_2 < p_1", font_size=EQ, color=CRIMSON).move_to(EQ_POS)
        self.play(ReplacementTransform(self.eq, eq2), run_time=0.8)
        self.eq = eq2
        self.wait(max(DURS["B02"] - (0.6 + w1 + 1.6), 0.1))

    # ---------------- B03 — Bernoulli: p + 1/2 rho v^2 = constant ----------------
    def b03_bernoulli(self):
        self.play(FadeOut(self.varrows), run_time=0.5)
        eq3 = MathTex(r"p + \tfrac{1}{2}\rho v^2 = \text{constant}", font_size=EQ, color=INK).move_to(EQ_POS)
        self.play(ReplacementTransform(self.eq, eq3), run_time=0.8)
        self.eq = eq3

        self.bars = [self.bar(x, P1, KE1) for x in GX]
        outlines = VGroup(*[DashedVMobject(Rectangle(width=BAR_W + 0.12, height=BAR_H + 0.08, color=SLATE,
                                                      stroke_width=2.5).move_to([x, BAR_BASE + BAR_H / 2, 0]),
                                            num_dashes=30) for x in GX])
        self.outlines = outlines
        self.play(*[FadeIn(b) for b in self.bars], Create(outlines), run_time=0.8)

        lp = MathTex("p", font_size=LBL, color=TEAL)
        lk = MathTex(r"\tfrac{1}{2}\rho v^2", font_size=LBL, color=INK)
        if self.PORTRAIT:
            # no room beside the narrow-frame bars: a swatch legend row above them
            sw_p = Square(side_length=0.16, color=INK, fill_color=TEAL, fill_opacity=1, stroke_width=1.5)
            sw_k = Square(side_length=0.16, color=INK, fill_color=GOLD, fill_opacity=1, stroke_width=1.5)
            self.legend = VGroup(VGroup(sw_p, lp).arrange(RIGHT, buff=0.1),
                                 VGroup(sw_k, lk).arrange(RIGHT, buff=0.1)).arrange(RIGHT, buff=0.5)
            self.legend.move_to([0, BAR_BASE + BAR_H + 0.4, 0])
        else:
            lp.next_to(self.bars[0][0], LEFT, buff=0.15)
            lk.next_to(self.bars[0][1], LEFT, buff=0.15)
            self.legend = VGroup(lp, lk)
        self.play(FadeIn(self.legend), run_time=0.5)

        new_mid = self.bar(GX[1], P2, KE2)
        self.play(ReplacementTransform(self.bars[1], new_mid), run_time=1.2)
        self.bars[1] = new_mid
        self.wait(max(DURS["B03"] - 3.8, 0.1))

    # ---------------- B04 — hold ----------------
    def b04_hold(self):
        neck = Rectangle(width=2 * NH + 0.6 * TR, height=2 * H2 + 0.1, stroke_width=0,
                         fill_color=GOLD, fill_opacity=0.35).move_to([0, YC, 0])
        self.neck = neck
        self.play(FadeIn(neck), run_time=0.6)
        summary = crisp_text("FASTER FLOW, LOWER PRESSURE", TXT, color=INK, font=CAPTION_STYLE).move_to(EQ_POS)
        if summary.width > 2 * safe_half_w():
            summary.scale_to_fit_width(2 * safe_half_w())
        self.play(FadeOut(self.eq), FadeIn(summary), run_time=0.8)
        self.summary = summary
        self.wait(max(DURS["B04"] - 1.4, 0.1))
