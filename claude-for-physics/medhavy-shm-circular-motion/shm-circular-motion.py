"""shm-circular-motion.py — Chapter 15, 15.3 Comparing SHM and Circular Motion.

A peg on a wheel of radius A turning at constant omega, lit from above,
casts a shadow x(t) = A cos(omega t) that rides exactly on a block-spring
oscillator with omega = 2 pi f. SHM is circular motion viewed edge-on.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh shm-circular-motion.py ShmCircularMotion
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching shm-circular-motion.py ShmCircularMotion
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

PERIOD = 3.2
OMEGA = 2 * PI / PERIOD
WHEEL = "#D9D9D9"

if PORTRAIT:
    CX, A, DISK_Y = -0.1, 0.85, 1.95
    AXIS_Y, BLOCK_Y, BLOCK_S, FLOOR_Y = 0.86, 0.0, 0.44, -0.22
    TR_TOP, TR_BOT, VS = -0.42, -2.15, 0.45
    SPRING_MIN = 0.5
    LBL_OUT = 0.45   # +-A labels sit outboard of the shadow line / turning-point pulse
    PEG_R = 0.08
    LBL, EQ, TXT = 26, 34, 18
    EQ_A = np.array([0, 3.17, 0])
    EQ_B = EQ_A
    SUM_POS = EQ_A
else:
    CX, A, DISK_Y = -2.4, 1.35, 1.85
    AXIS_Y, BLOCK_Y, BLOCK_S, FLOOR_Y = 0.2, -0.75, 0.7, -1.1
    TR_TOP, TR_BOT, VS = -1.35, -3.3, 0.6
    SPRING_MIN = 1.0
    LBL_OUT = 0.6
    PEG_R = 0.13
    LBL, EQ, TXT = 44, 60, 34
    EQ_A = np.array([3.6, 1.6, 0])
    EQ_B = np.array([3.6, 0.2, 0])
    SUM_POS = np.array([3.6, -1.4, 0])

WALL_X = CX - A - BLOCK_S / 2 - SPRING_MIN
CENTER = np.array([CX, DISK_Y, 0])


class ShmCircularMotion(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])
        self.t = 0.0
        self.pulse_on = False
        self.trace_on = False
        self.history = []
        self.b00_hook()
        self.b01_shadow()
        self.b02_duplicate()
        self.b03_cosine()
        self.b04_hold()

    # ---- shared clock: everything reads self.t, so wheel and block are exactly in sync ----
    def theta(self):
        return OMEGA * self.t

    def x_now(self):
        return CX + A * np.cos(self.theta())

    def peg_pos(self):
        th = self.theta()
        return CENTER + A * np.array([np.cos(th), np.sin(th), 0])

    def start_clock(self):
        clock = Mobject()

        def tick(m, dt):
            self.t += dt
            if self.trace_on:
                self.history.append((self.t, self.x_now()))
        clock.add_updater(tick)
        self.add(clock)
        self.clock = clock

    # ---- drawables ----
    def spokes(self):
        th = self.theta()
        return VGroup(*[Line(CENTER, CENTER + 0.92 * A * np.array([np.cos(th + k * PI / 2), np.sin(th + k * PI / 2), 0]),
                             color=SLATE, stroke_width=3) for k in range(4)])

    def peg(self):
        return Circle(radius=PEG_R, color=INK, fill_color=GOLD, fill_opacity=1, stroke_width=2).move_to(self.peg_pos())

    def block(self):
        return Square(side_length=BLOCK_S, color=INK, fill_color=CRIMSON, fill_opacity=1,
                      stroke_width=2.5).move_to([self.x_now(), BLOCK_Y, 0])

    def spring(self):
        x0, x1 = WALL_X, self.x_now() - BLOCK_S / 2
        n, amp = 12, BLOCK_S * 0.22
        lead = 0.08 * (x1 - x0)
        pts = [np.array([x0, BLOCK_Y, 0]), np.array([x0 + lead, BLOCK_Y, 0])]
        for i in range(n):
            xx = x0 + lead + (i + 0.5) * (x1 - x0 - 2 * lead) / n
            pts.append(np.array([xx, BLOCK_Y + (amp if i % 2 == 0 else -amp), 0]))
        pts += [np.array([x1 - lead, BLOCK_Y, 0]), np.array([x1, BLOCK_Y, 0])]
        return VMobject(color=SLATE, stroke_width=3).set_points_as_corners(pts)

    def proj_line(self):
        p = self.peg_pos()
        # fixed dash count: a length-dependent count changes the submobject
        # count frame to frame and breaks FadeIn (zip length mismatch)
        return DashedVMobject(Line(p + DOWN * PEG_R, [p[0], self.proj_end.get_value(), 0], color=SLATE,
                                   stroke_width=2.5), num_dashes=40)

    def shadow(self, y):
        return Circle(radius=PEG_R * 0.9, color=INK, fill_color=GOLD, fill_opacity=1,
                      stroke_width=2).move_to([self.x_now(), y, 0])

    def pulse_level(self):
        if not self.pulse_on:
            return 0.0
        return float(np.clip((abs(np.cos(self.theta())) - 0.95) / 0.05, 0, 1))

    def trace(self):
        if len(self.history) < 2:
            return VMobject()
        pts = []
        for (tt, xx) in self.history:
            y = TR_TOP - (self.t - tt) * VS
            if y >= TR_BOT:
                pts.append(np.array([xx, y, 0]))
        if len(pts) < 2:
            return VMobject()
        return VMobject(color=INK, stroke_width=4).set_points_as_corners(pts)

    # ---------------- B00 — two motions ----------------
    def b00_hook(self):
        self.start_clock()
        disk = Circle(radius=A, color=INK, fill_color=WHEEL, fill_opacity=1, stroke_width=3).move_to(CENTER)
        hub = Dot(CENTER, radius=0.05, color=INK)
        self.disk, self.hub = disk, hub
        self.spokes_m = always_redraw(self.spokes)
        self.peg_m = always_redraw(self.peg)

        wall = Line([WALL_X, FLOOR_Y, 0], [WALL_X, BLOCK_Y + BLOCK_S * 0.9, 0], color=INK, stroke_width=5)
        hatch = VGroup(*[Line([WALL_X, y, 0], [WALL_X - 0.12, y - 0.12, 0], color=INK, stroke_width=2)
                         for y in np.linspace(FLOOR_Y + 0.12, BLOCK_Y + BLOCK_S * 0.9, 5)])
        floor = Line([WALL_X, FLOOR_Y, 0], [CX + A + BLOCK_S, FLOOR_Y, 0], color=INK, stroke_width=3)
        self.base = VGroup(wall, hatch, floor)
        self.spring_m = always_redraw(self.spring)
        self.block_m = always_redraw(self.block)

        self.play(FadeIn(disk), FadeIn(hub), FadeIn(self.spokes_m), FadeIn(self.peg_m),
                  FadeIn(self.base), FadeIn(self.spring_m), FadeIn(self.block_m), run_time=1.2)
        self.bring_to_front(self.peg_m)
        self.wait(max(DURS["B00"] - 1.2, 0.1))

    # ---------------- B01 — the shadow on an axis ----------------
    def b01_shadow(self):
        axis = Line([CX - A - 0.35, AXIS_Y, 0], [CX + A + 0.35, AXIS_Y, 0], color=INK, stroke_width=3)
        ticks = VGroup(*[Line([CX + s * A, AXIS_Y - 0.08, 0], [CX + s * A, AXIS_Y + 0.08, 0], color=INK, stroke_width=3)
                         for s in (-1, 0, 1)])
        tl = VGroup(*[MathTex(s, font_size=LBL, color=INK).next_to(ticks[i], DOWN, buff=0.08)
                      for i, s in enumerate(["-A", "0", "+A"])])
        # the dashed projection line and turning-point rings sit exactly at +-A:
        # move those two labels outboard so nothing crosses the text
        tl[0].shift(LEFT * LBL_OUT)
        tl[2].shift(RIGHT * LBL_OUT)
        self.axis = VGroup(axis, ticks, tl)
        self.play(Create(axis), FadeIn(ticks), FadeIn(tl), run_time=0.8)

        self.proj_end = ValueTracker(AXIS_Y)
        self.proj_m = always_redraw(self.proj_line)
        self.shadow_m = always_redraw(lambda: self.shadow(AXIS_Y))
        self.play(FadeIn(self.proj_m), FadeIn(self.shadow_m), run_time=0.6)
        self.bring_to_front(self.peg_m)
        self.wait(max(DURS["B01"] - 1.4, 0.1))

    # ---------------- B02 — the shadow rides the block ----------------
    def b02_duplicate(self):
        self.drop = ValueTracker(AXIS_Y)
        self.shadow2_m = always_redraw(lambda: self.shadow(self.drop.get_value()))
        self.add(self.shadow2_m)
        self.play(self.proj_end.animate.set_value(BLOCK_Y), self.drop.animate.set_value(BLOCK_Y), run_time=1.0)

        self.pulse_on = True
        self.ring_s = always_redraw(lambda: Circle(radius=PEG_R * 2.2, color=CRIMSON, stroke_width=4)
                                    .move_to([self.x_now(), AXIS_Y, 0]).set_stroke(opacity=self.pulse_level()))
        self.ring_b = always_redraw(lambda: Square(side_length=BLOCK_S + 0.18, color=GOLD, stroke_width=5)
                                    .move_to([self.x_now(), BLOCK_Y, 0]).set_stroke(opacity=self.pulse_level()))
        self.add(self.ring_s, self.ring_b)

        self.eq1 = MathTex(r"\omega = 2\pi f", font_size=EQ, color=INK).move_to(EQ_A)
        self.play(Write(self.eq1), run_time=0.8)
        self.wait(max(DURS["B02"] - 1.8, 0.1))

    # ---------------- B03 — theta = omega t, x = A cos(omega t), cosine trace ----------------
    def b03_cosine(self):
        self.radius_m = always_redraw(lambda: Line(CENTER, self.peg_pos(), color=INK, stroke_width=3))
        self.arc_m = always_redraw(lambda: Arc(radius=0.32 * A, start_angle=0,
                                               angle=max(self.theta() % TAU, 0.01), arc_center=CENTER,
                                               color=TEAL, stroke_width=4))
        self.th_lbl = MathTex(r"\theta", font_size=LBL, color=TEAL)
        self.th_lbl.add_updater(lambda m: m.move_to(CENTER + 0.5 * A * np.array(
            [np.cos((self.theta() % TAU) / 2), np.sin((self.theta() % TAU) / 2), 0])))
        self.play(FadeIn(self.radius_m), FadeIn(self.arc_m), FadeIn(self.th_lbl), run_time=0.6)
        self.bring_to_front(self.peg_m)

        if self.PORTRAIT:
            eq2 = MathTex(r"x(t) = A\cos(\omega t)", font_size=EQ, color=INK).move_to(EQ_B)
            self.play(ReplacementTransform(self.eq1, eq2), run_time=0.8)
        else:
            eq2 = MathTex(r"x(t) = A\cos(\omega t)", font_size=EQ, color=INK).move_to(EQ_B)
            self.play(Write(eq2), run_time=0.8)
        self.eq2 = eq2

        self.trace_on = True
        self.trace_m = always_redraw(self.trace)
        self.add(self.trace_m)
        tx = CX - A - 0.4
        t_arrow = Arrow([tx, TR_TOP, 0], [tx, TR_TOP - 0.8, 0], buff=0, color=SLATE, stroke_width=4,
                        max_tip_length_to_length_ratio=0.2)
        t_lbl = MathTex("t", font_size=LBL, color=SLATE).next_to(t_arrow, LEFT, buff=0.08)
        self.t_axis = VGroup(t_arrow, t_lbl)
        self.play(FadeIn(self.t_axis), run_time=0.5)
        self.wait(max(DURS["B03"] - 1.9, 0.1))

    # ---------------- B04 — hold ----------------
    def b04_hold(self):
        summary = crisp_text("SHM = circular motion,\nviewed edge-on", TXT, color=INK, font=CAPTION_STYLE,
                             line_spacing=1.0)
        if summary.width > 2 * safe_half_w():
            summary.scale_to_fit_width(2 * safe_half_w())
        summary.move_to(SUM_POS)
        if self.PORTRAIT:
            self.play(FadeOut(self.eq2), FadeIn(summary), run_time=0.8)
        else:
            self.play(FadeIn(summary), run_time=0.8)
        self.summary = summary
        self.wait(max(DURS["B04"] - 0.8, 0.1))
