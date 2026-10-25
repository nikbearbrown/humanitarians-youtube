"""resonance.py — Chapter 15, 15.6 Forced Oscillations.

A lightly damped spring-mass oscillator (Eq. 15.27, simulated) is driven by
moving the top of its spring with a small amplitude: off resonance the
response stays small; at the natural frequency it grows cycle by cycle.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh resonance.py Resonance
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching resonance.py Resonance
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

MASS_BLUE = "#0072B2"
RIVER = "#56B4E9"
BANK = "#7FC8A9"
DECK = "#BFBFBF"

W0 = 2 * PI / 1.6      # natural angular frequency (on-screen time)
GAMMA = 0.25           # b/m, light damping

if PORTRAIT:
    RIG_X, SUP_Y, REST_Y, MASS_S = -1.05, 2.7, 0.6, 0.4
    DRIVE_D, X_INIT = 0.055, 0.4
    CH_X0, CH_X1, VS = -0.5, 1.6, 0.35
    LBL_POS = np.array([0.72, 3.15, 0])
    LBL, TXT = 30, 18
    DECK_W, DECK_H, DECK_Y = 3.3, 0.45, 0.6
    SUM_POS = np.array([0, -1.0, 0])
else:
    RIG_X, SUP_Y, REST_Y, MASS_S = -4.6, 2.75, -0.2, 0.8
    DRIVE_D, X_INIT = 0.08, 0.6
    CH_X0, CH_X1, VS = -3.2, 6.2, 0.9
    LBL_POS = np.array([1.5, 3.05, 0])
    LBL, TXT = 48, 34
    DECK_W, DECK_H, DECK_Y = 10.5, 0.8, 0.4
    SUM_POS = np.array([1.5, -2.6, 0])


class Resonance(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])
        self.t = 0.0
        # oscillator state
        self.x, self.v = 0.0, 0.0
        self.sim_on = False
        self.drive_w = 0.0      # 0 = no drive
        self.phase = 0.0
        self.history = []
        self.sway_amp = 0.0
        self.start_clock()
        self.b00_bridge()
        self.b01_natural()
        self.b02_offres()
        self.b03_resonance()
        self.b04_hold()

    def support_s(self):
        return DRIVE_D * np.sin(self.phase) if self.drive_w > 0 else 0.0

    def start_clock(self):
        clock = Mobject()

        def tick(m, dt):
            self.t += dt
            if not self.sim_on or dt == 0:
                return
            n = 20
            h = dt / n
            for _ in range(n):
                if self.drive_w > 0:
                    self.phase += self.drive_w * h
                s = self.support_s()
                acc = -W0 * W0 * (self.x - s) - GAMMA * self.v
                self.v += acc * h
                self.x += self.v * h
            self.history.append((self.t, self.x))
            if len(self.history) > 2000:
                self.history = self.history[-2000:]
        clock.add_updater(tick)
        self.add(clock)
        self.clock = clock

    # ---- rig drawables ----
    def support(self):
        y = SUP_Y + self.support_s()
        col = CRIMSON if self.drive_w > 0 else INK
        bar = Rectangle(width=MASS_S * 2.2, height=0.12, color=INK, fill_color=col, fill_opacity=1,
                        stroke_width=2).move_to([RIG_X, y, 0])
        return bar

    def mass(self):
        return Square(side_length=MASS_S, color=INK, fill_color=MASS_BLUE, fill_opacity=1,
                      stroke_width=2.5).move_to([RIG_X, REST_Y + self.x, 0])

    def spring(self):
        y0 = SUP_Y + self.support_s() - 0.06
        y1 = REST_Y + self.x + MASS_S / 2
        n, amp = 14, MASS_S * 0.32
        lead = 0.06 * (y0 - y1)
        pts = [np.array([RIG_X, y0, 0]), np.array([RIG_X, y0 - lead, 0])]
        for i in range(n):
            yy = y0 - lead - (i + 0.5) * (y0 - y1 - 2 * lead) / n
            pts.append(np.array([RIG_X + (amp if i % 2 == 0 else -amp), yy, 0]))
        pts += [np.array([RIG_X, y1 + lead, 0]), np.array([RIG_X, y1, 0])]
        return VMobject(color=SLATE, stroke_width=3).set_points_as_corners(pts)

    def trace(self):
        pts = []
        for tt, xx in self.history:
            px = CH_X1 - (self.t - tt) * VS
            if px >= CH_X0:
                pts.append(np.array([px, REST_Y + xx, 0]))
        if len(pts) < 2:
            return VMobject()
        return VMobject(color=INK, stroke_width=3.5).set_points_as_corners(pts)

    # ---------------- B00 — footbridge sways ----------------
    def b00_bridge(self):
        river = Rectangle(width=DECK_W + 0.3, height=DECK_H * 3.4, stroke_width=0, fill_color=RIVER,
                          fill_opacity=0.35).move_to([0, DECK_Y, 0])
        bank_w = 0.5 if self.PORTRAIT else 1.0
        banks = VGroup(*[Rectangle(width=bank_w, height=DECK_H * 3.4, stroke_width=0, fill_color=BANK,
                                   fill_opacity=1).move_to([s * (DECK_W / 2 - bank_w / 2 + 0.15), DECK_Y, 0])
                         for s in (-1, 1)])
        span0, span1 = -DECK_W / 2 + bank_w, DECK_W / 2 - bank_w

        def sway(x):
            # lateral deflection: zero at the banks, largest mid-span
            u = (x - span0) / (span1 - span0)
            return self.sway_amp * np.sin(PI * np.clip(u, 0, 1)) * np.sin(W0 * self.t)

        def deck():
            xs = np.linspace(-DECK_W / 2 + 0.15, DECK_W / 2 - 0.15, 60)
            top = [np.array([x, DECK_Y + DECK_H / 2 + sway(x), 0]) for x in xs]
            bot = [np.array([x, DECK_Y - DECK_H / 2 + sway(x), 0]) for x in xs[::-1]]
            return Polygon(*top, *bot, color=INK, fill_color=DECK, fill_opacity=1, stroke_width=2.5)

        self.deck_m = always_redraw(deck)
        rng = np.random.default_rng(3)
        walkers = []
        for k in range(10 if not self.PORTRAIT else 6):
            walkers.append([rng.uniform(span0, span1), rng.choice([-1, 1]) * rng.uniform(0.25, 0.4) * DECK_H,
                            (1 if k % 2 == 0 else -1) * (0.45 if not self.PORTRAIT else 0.18)])
        self.walkers = walkers
        cols = [INK, CRIMSON, TEAL, SLATE]

        def people():
            g = VGroup()
            for i, (x, dy, _v) in enumerate(self.walkers):
                g.add(Dot([x, DECK_Y + dy + sway(x), 0], radius=0.07 if not self.PORTRAIT else 0.045,
                          color=cols[i % 4]))
            return g

        def walk(m, dt):
            for w in self.walkers:
                w[0] += w[2] * dt
                if w[0] > span1:
                    w[0] = span0
                if w[0] < span0:
                    w[0] = span1
            self.sway_amp = min(self.sway_amp + dt * (0.03 if not self.PORTRAIT else 0.014),
                                0.35 if not self.PORTRAIT else 0.16)
        self.people_m = always_redraw(people)
        self.people_m.add_updater(walk)
        lbl = crisp_text("footbridge, top view", TXT - 4, color=SLATE, font=CAPTION_STYLE)
        lbl.next_to(river, UP, buff=0.2)
        self.bridge = VGroup(river, banks, lbl)
        self.play(FadeIn(river), FadeIn(banks), FadeIn(self.deck_m), FadeIn(self.people_m), FadeIn(lbl), run_time=1.0)
        self.wait(max(DURS["B00"] - 1.0, 0.1))

    # ---------------- B01 — natural frequency, free oscillation ----------------
    def b01_natural(self):
        self.people_m.clear_updaters()
        self.deck_m.clear_updaters()
        self.play(FadeOut(self.bridge), FadeOut(self.deck_m), FadeOut(self.people_m), run_time=0.6)

        ceiling = Line([RIG_X - MASS_S * 1.6, SUP_Y + 0.3, 0], [RIG_X + MASS_S * 1.6, SUP_Y + 0.3, 0],
                       color=INK, stroke_width=4)
        self.ceiling = ceiling
        self.x = X_INIT
        self.support_m = always_redraw(self.support)
        self.spring_m = always_redraw(self.spring)
        self.mass_m = always_redraw(self.mass)
        axis = DashedLine([CH_X0, REST_Y, 0], [CH_X1, REST_Y, 0], color=SLATE, stroke_width=2, dash_length=0.1)
        # landscape: t label right of the axis; portrait has no room clear of the trace
        if self.PORTRAIT:
            self.chart = VGroup(axis)
        else:
            t_lbl = MathTex("t", font_size=LBL - 6, color=SLATE).next_to(axis, RIGHT, buff=0.1)
            self.chart = VGroup(axis, t_lbl)
        self.trace_m = always_redraw(self.trace)
        self.play(FadeIn(ceiling), FadeIn(self.support_m), FadeIn(self.spring_m), FadeIn(self.mass_m),
                  FadeIn(self.chart), run_time=0.8)
        self.add(self.trace_m)
        self.sim_on = True

        self.f_lbl = MathTex(r"\text{natural frequency } f_0", font_size=LBL, color=TEAL).move_to(LBL_POS)
        if self.PORTRAIT:
            self.f_lbl = MathTex(r"f_0", font_size=LBL, color=TEAL).move_to(LBL_POS)
        self.play(FadeIn(self.f_lbl), run_time=0.6)
        self.wait(max(DURS["B01"] - 2.0, 0.1))

    # ---------------- B02 — off-resonance drive ----------------
    def b02_offres(self):
        self.drive_w = 1.7 * W0
        lbl = MathTex(r"f_{\text{drive}} = 1.7\,f_0", font_size=LBL, color=CRIMSON).move_to(LBL_POS)
        self.play(ReplacementTransform(self.f_lbl, lbl), run_time=0.8)
        self.f_lbl = lbl
        self.wait(max(DURS["B02"] - 0.8, 0.1))

    # ---------------- B03 — resonance ----------------
    def b03_resonance(self):
        self.drive_w = W0
        lbl = MathTex(r"f_{\text{drive}} = f_0", font_size=LBL, color=INK).move_to(LBL_POS)
        self.play(ReplacementTransform(self.f_lbl, lbl), run_time=0.8)
        self.f_lbl = lbl
        self.wait(max(DURS["B03"] - 0.8, 0.1))

    # ---------------- B04 — hold ----------------
    def b04_hold(self):
        summary = crisp_text("SAME PUSH, RIGHT TIMING", TXT, color=INK, font=CAPTION_STYLE).move_to(SUM_POS)
        if summary.width > 2 * safe_half_w():
            summary.scale_to_fit_width(2 * safe_half_w())
        self.play(FadeIn(summary), run_time=0.8)
        self.summary = summary
        self.wait(max(DURS["B04"] - 0.8, 0.1))
