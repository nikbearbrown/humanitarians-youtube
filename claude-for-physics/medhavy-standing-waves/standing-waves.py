"""standing-waves.py — Chapter 16, Standing Waves and Resonance.

Two identical waves traveling in opposite directions superpose into a
standing wave y = [2A sin(kx)] cos(wt): nodes at n*lambda/2 never move,
antinodes at odd multiples of lambda/4 swing through +-2A, while both
components keep traveling underneath. The sum curve is the literal
point-by-point sum y1 + y2, recomputed every frame.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh standing-waves.py StandingWaves
  Portrait  (9:16): manim -r 1080,1920 --fps 60 --disable_caching standing-waves.py StandingWaves
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


class StandingWaves(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if PORTRAIT:
            self.HW, self.LAM, self.A = 1.6, 1.6, 0.36
            self.Y_TOP, self.Y_BOT, self.Y_AX = 1.4, -1.0, -0.2
            self.N = 200
            self.GUIDE_X = [-1.6, 0.0, 1.6]
            self.NODE_LABEL_X, self.ANTI_LABEL_X = 0.8, -0.4
            self.LABEL_FS = 16
        else:
            self.HW, self.LAM, self.A = 6.0, 4.0, 0.6
            self.Y_TOP, self.Y_BOT, self.Y_AX = 1.4, -1.9, -0.4
            self.N = 400
            self.GUIDE_X = [-4.0, 0.0, 4.0]
            self.NODE_LABEL_X, self.ANTI_LABEL_X = 2.0, -3.0
            self.LABEL_FS = 22
        self.K = 2 * PI / self.LAM
        self.OMEGA = 2 * PI / 2.4  # period 2.4 s on screen

        # Wave phase reads scene time (self.time) so every updater sees the
        # same instant regardless of mobject order. The dt-updater "ticker"
        # only exists so landscape waits are never frozen frames.
        self.ticker = Mobject()
        self.ticker.add_updater(lambda m, dt: None)
        self.add(self.ticker)

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_superpose()
        self.b02_nodes()
        self.b03_antinodes()
        self.b04_equation()
        self.b05_hold()

    # ---------------- wave helpers ----------------
    def xs(self):
        return np.linspace(-self.HW, self.HW, self.N)

    def y1(self, x):  # rightward: A sin(kx - wt)
        return self.A * np.sin(self.K * x - self.OMEGA * self.time)

    def y2(self, x):  # leftward: A sin(kx + wt)
        return self.A * np.sin(self.K * x + self.OMEGA * self.time)

    def curve(self, fn, y_tracker, op_tracker, color, width):
        m = VMobject()

        def upd(mob):
            x = self.xs()
            pts = np.column_stack([x, y_tracker.get_value() + fn(x), np.zeros_like(x)])
            mob.set_points_as_corners(pts)
            mob.set_stroke(color=color, width=width, opacity=op_tracker.get_value())
            mob.set_fill(opacity=0)

        upd(m)
        m.add_updater(upd)
        return m

    # ---------------- B00 — two traveling waves, stacked ----------------
    def b00_hook(self):
        self.yt1 = ValueTracker(self.Y_TOP)
        self.yt2 = ValueTracker(self.Y_BOT)
        self.op_c = ValueTracker(1.0)
        self.axis1 = Line([-self.HW, self.Y_TOP, 0], [self.HW, self.Y_TOP, 0], color=SLATE, stroke_width=1.5)
        self.axis2 = Line([-self.HW, self.Y_BOT, 0], [self.HW, self.Y_BOT, 0], color=SLATE, stroke_width=1.5)
        self.w1 = self.curve(self.y1, self.yt1, self.op_c, TEAL, 5)
        self.w2 = self.curve(self.y2, self.yt2, self.op_c, CRIMSON, 5)

        def dir_label(text, color, direction, y):
            t = crisp_text(text, self.LABEL_FS, color=color, font=CAPTION_STYLE)
            arr_len = 0.6 if self.PORTRAIT else 0.9
            arr = Arrow(ORIGIN, direction * arr_len, buff=0, color=color, stroke_width=4,
                        max_tip_length_to_length_ratio=0.35)
            g = VGroup(t, arr).arrange(direction, buff=0.15) if np.allclose(direction, RIGHT) \
                else VGroup(arr, t).arrange(RIGHT, buff=0.15)
            g.move_to([0, y, 0])
            return g

        self.lab1 = dir_label("traveling right", TEAL, RIGHT, self.Y_TOP + self.A + 0.4)
        self.lab2 = dir_label("traveling left", CRIMSON, LEFT, self.Y_BOT + self.A + 0.4)

        self.play(Create(self.axis1), Create(self.axis2), FadeIn(self.w1), FadeIn(self.w2), run_time=1.0)
        self.play(FadeIn(self.lab1), FadeIn(self.lab2), run_time=0.6)
        self.wait(max(DURS["B00"] - 1.6, 0.3))

    # ---------------- B01 — merge onto one axis, live sum ----------------
    def b01_superpose(self):
        self.play(FadeOut(self.lab1), FadeOut(self.lab2), run_time=0.5)
        self.play(
            self.yt1.animate.set_value(self.Y_AX), self.yt2.animate.set_value(self.Y_AX),
            self.axis1.animate.move_to([0, self.Y_AX, 0]), FadeOut(self.axis2),
            self.op_c.animate.set_value(0.3),
            run_time=2.2,
        )
        self.op_s = ValueTracker(0.0)
        self.ys = ValueTracker(self.Y_AX)
        self.wsum = self.curve(lambda x: self.y1(x) + self.y2(x), self.ys, self.op_s, INK, 7)
        self.add(self.wsum)
        self.play(self.op_s.animate.set_value(1.0), run_time=1.2)
        self.wait(max(DURS["B01"] - 3.9, 0.3))

    # ---------------- B02 — nodes ----------------
    def b02_nodes(self):
        r = 0.055 if self.PORTRAIT else 0.08
        step = self.LAM / 2
        n_max = int(round(self.HW / step))
        self.node_x = [n * step for n in range(-n_max, n_max + 1)]
        self.dots = VGroup(*[
            Circle(radius=r).set_fill(CREAM, 1).set_stroke(SLATE, 3).move_to([x, self.Y_AX, 0])
            for x in self.node_x
        ])
        span = 2 * self.A
        self.guides = VGroup(*[
            DashedLine([x, self.Y_AX - span, 0], [x, self.Y_AX + span, 0], color=SLATE,
                       stroke_width=1.5, dash_length=0.08)
            for x in self.GUIDE_X
        ])
        nd = self.dots[self.node_x.index(min(self.node_x, key=lambda v: abs(v - self.NODE_LABEL_X)))]
        self.node_label = crisp_text("node", self.LABEL_FS, color=SLATE, font=CAPTION_STYLE)
        self.node_label.next_to(nd, DOWN, buff=span + 0.15)

        self.play(Create(self.guides), run_time=0.8)
        self.bring_to_front(self.wsum)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in self.dots], lag_ratio=0.15), run_time=1.2)
        self.play(FadeIn(self.node_label), run_time=0.5)
        self.wait(max(DURS["B02"] - 2.5, 0.3))

    # ---------------- B03 — antinodes, envelope-synced bands ----------------
    def b03_antinodes(self):
        q = self.LAM / 4
        self.anti_x = [x for x in np.arange(-self.HW + q, self.HW, 2 * q)]
        self.op_b = ValueTracker(0.0)
        bw = q * 0.9

        def band_upd(g):
            env = 2 * self.A * abs(np.cos(self.OMEGA * self.time))
            h = max(2 * env, 0.02)
            for rect, x in zip(g, self.anti_x):
                rect.stretch_to_fit_height(h)
                rect.move_to([x, self.Y_AX, 0])
                rect.set_fill(GOLD, opacity=0.55 * self.op_b.get_value())

        self.bands = VGroup(*[
            Rectangle(width=bw, height=1.0, stroke_width=0).set_fill(GOLD, 0) for _ in self.anti_x
        ])
        band_upd(self.bands)
        self.bands.add_updater(band_upd)
        self.add(self.bands)
        self.bring_to_back(self.bands)

        ax = min(self.anti_x, key=lambda v: abs(v - self.ANTI_LABEL_X))
        self.anti_label = crisp_text("antinode", self.LABEL_FS, color=INK, font=CAPTION_STYLE)
        self.anti_label.move_to([ax, self.Y_AX + 2 * self.A + 0.35, 0])

        self.play(self.op_b.animate.set_value(1.0), run_time=1.2)
        self.play(FadeIn(self.anti_label), run_time=0.5)
        self.wait(max(DURS["B03"] - 1.7, 0.3))

    # ---------------- B04 — the algebra ----------------
    def b04_equation(self):
        eq = MathTex(r"y(x,t) =", r"\left[\,2A\sin(kx)\,\right]", r"\cos(\omega t)", color=INK,
                     font_size=48 if not self.PORTRAIT else 40)
        eq[2].set_color(TEAL)
        if eq.width > 2 * safe_half_w():
            eq.scale_to_fit_width(2 * safe_half_w())
        eq_y = 2.0 if self.PORTRAIT else 2.5
        eq.move_to([0, eq_y, 0])
        self.eq = eq
        self.play(FadeOut(self.node_label), FadeOut(self.anti_label), run_time=0.5)
        self.play(Write(eq), run_time=1.5)
        self.wait(max(DURS["B04"] - 2.0, 0.3))

    # ---------------- B05 — summary hold ----------------
    def b05_hold(self):
        txt = ("STANDING WAVE =\nTWO TRAVELING WAVES,\nOPPOSITE DIRECTIONS" if self.PORTRAIT
               else "STANDING WAVE = TWO TRAVELING WAVES, OPPOSITE DIRECTIONS")
        summary = crisp_text(txt, 16 if self.PORTRAIT else 24, color=INK, font=CAPTION_STYLE,
                             line_spacing=1.1, weight=BOLD)
        if summary.width > 2 * safe_half_w():
            summary.scale_to_fit_width(2 * safe_half_w())
        summary.move_to(self.eq.get_center())
        self.summary = summary
        self.play(FadeOut(self.eq), FadeIn(summary), run_time=0.8)
        self.wait(max(DURS["B05"] - 0.8, 0.3))
