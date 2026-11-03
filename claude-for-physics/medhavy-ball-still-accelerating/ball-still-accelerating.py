"""ball-still-accelerating.py — Chapter 3, Average and Instantaneous Acceleration.

A ball thrown straight up has zero velocity at the top of its path, yet its
acceleration there is still 9.8 m/s² downward: acceleration is the rate of
change of velocity, and at the peak velocity is changing from up to down.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh ball-still-accelerating.py BallStillAccelerating
  Portrait  (9:16): manim -r 1080,1920 --fps 60 --disable_caching ball-still-accelerating.py BallStillAccelerating
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

BALL_COLOR = CRIMSON   # red ball (storyboard)
V_COLOR = TEAL         # velocity
A_COLOR = INK          # acceleration (black, storyboard)


def make_ball(r):
    body = Circle(radius=r, color=INK, stroke_width=2.5, fill_color=BALL_COLOR, fill_opacity=1)
    sheen = Circle(radius=r * 0.28, stroke_width=0, fill_color=CREAM, fill_opacity=0.55).move_to(
        body.get_center() + np.array([-0.4 * r, 0.4 * r, 0])
    )
    return VGroup(body, sheen)


def v_mark(origin, length, stroke=6):
    """Velocity arrow from origin, signed length (+ up). A dot when ~zero."""
    if abs(length) < 0.06:
        return Dot(origin, radius=0.08, color=V_COLOR)
    return Arrow(origin, origin + UP * length, buff=0, color=V_COLOR, stroke_width=stroke,
                 max_tip_length_to_length_ratio=0.3)


def a_mark(center, length, stroke=8):
    """Acceleration arrow, fixed downward, centered on `center`."""
    return Arrow(center + UP * length / 2, center + DOWN * length / 2, buff=0, color=A_COLOR,
                 stroke_width=stroke, max_tip_length_to_length_ratio=0.25)


def a_label(fs):
    return MathTex(r"a = 9.8\ \mathrm{m/s^2}", font_size=fs, color=A_COLOR)


class BallStillAccelerating(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.X, self.YB, self.H = 0.6, -2.0, 4.0
            self.R, self.LV, self.LA, self.OFF = 0.26, 1.3, 1.2, 0.5
            self.FS = 28
        else:
            self.X, self.YB, self.H = 0.0, -2.8, 5.0
            self.R, self.LV, self.LA, self.OFF = 0.45, 2.2, 1.8, 0.8
            self.FS = 46

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_rise()
        self.b01_zero_velocity()
        self.b02_reveal_acceleration()
        self.b03_compare()
        self.b04_hold()

    # s = time in units of the rise time; s=1 is the peak.
    def ball_y(self, s):
        return self.YB + self.H * (1 - (1 - s) ** 2)

    def ball_pos(self):
        return np.array([self.X, self.ball_y(self.s.get_value()), 0])

    # ---------------- B00 — ball rises, v shrinks to a dot ----------------
    def b00_rise(self):
        self.s = ValueTracker(0.0)
        track = DashedLine(
            [self.X, self.YB - self.R - 0.1, 0], [self.X, self.ball_y(1) + self.R + 0.5, 0],
            color=SLATE, stroke_width=2.5, dash_length=0.12,
        )
        ball = always_redraw(lambda: make_ball(self.R).move_to(self.ball_pos()))
        v = always_redraw(lambda: v_mark(
            self.ball_pos() + RIGHT * self.OFF, self.LV * (1 - self.s.get_value())))
        v_lab = always_redraw(lambda: MathTex("v", font_size=self.FS + 4, color=V_COLOR).next_to(
            v, RIGHT, buff=0.12))

        self.play(Create(track), FadeIn(ball), FadeIn(v), FadeIn(v_lab), run_time=0.8)
        hold = 3.0
        self.play(self.s.animate.set_value(1.0), run_time=DURS["B00"] - 0.8 - hold, rate_func=linear)
        self.wait(hold)
        self.track, self.ball, self.v, self.v_lab = track, ball, v, v_lab

    # ---------------- B01 — ZERO VELOCITY stamp, stillness ----------------
    def b01_zero_velocity(self):
        stamp = crisp_text("ZERO VELOCITY", 30 if self.PORTRAIT else 44, color=CRIMSON, weight=BOLD, font=CAPTION_STYLE)
        if self.PORTRAIT:
            stamp.move_to([0, safe_half_h() - 0.15, 0])
        else:
            stamp.next_to(self.v_lab, RIGHT, buff=0.8)
        if stamp.width > 2 * safe_half_w():
            stamp.scale_to_fit_width(2 * safe_half_w())
        self.wait(1.0)
        self.play(FadeIn(stamp, scale=1.4), run_time=0.5)
        self.stamp = stamp
        self.wait(DURS["B01"] - 1.5)

    # ---------------- B02 — fixed acceleration arrow; ball falls ----------------
    def b02_reveal_acceleration(self):
        a = a_mark(self.ball_pos() + LEFT * self.OFF, self.LA)
        a_lab = a_label(self.FS).next_to(a, LEFT, buff=0.15)
        self.play(FadeOut(self.stamp), run_time=0.5)
        self.play(GrowArrow(a), FadeIn(a_lab), run_time=1.0)
        # translate only (length and direction never change)
        a.add_updater(lambda m: m.move_to(
            [self.X - self.OFF, self.ball_y(self.s.get_value()), 0]))
        a_lab.add_updater(lambda m: m.next_to(a, LEFT, buff=0.15))
        self.a, self.a_lab = a, a_lab
        self.wait(4.0)
        hold = 1.0
        self.play(self.s.animate.set_value(1.7), run_time=DURS["B02"] - 0.5 - 1.0 - 4.0 - hold,
                  rate_func=linear)
        self.wait(hold)

    # ---------------- B03 — three snapshots, identical a ----------------
    def build_rows(self):
        if self.PORTRAIT:
            ys, bx, r, lv, la, off, fs_l, hy = [1.8, 0.3, -1.2], 0.55, 0.2, 0.7, 0.7, 0.5, 18, 2.95
        else:
            ys, bx, r, lv, la, off, fs_l, hy = [1.7, -0.3, -2.3], 1.0, 0.38, 1.05, 1.1, 0.85, 32, 3.2
        names = ["rising", "at the peak", "falling"]
        signs = [1, 0, -1]
        rows, v_list, a_list = VGroup(), VGroup(), VGroup()
        for y, name, sg in zip(ys, names, signs):
            c = np.array([bx, y, 0])
            ball = make_ball(r).move_to(c)
            v = v_mark(c + RIGHT * off, lv * sg, stroke=5)
            a = a_mark(c + LEFT * off, la, stroke=7)
            lab = crisp_text(name, fs_l, color=SLATE, font=CAPTION_STYLE)
            lab.next_to(a, LEFT, buff=0.35).set_y(y)
            rows.add(VGroup(lab, a, ball, v))
            v_list.add(v)
            a_list.add(a)
        h_v = MathTex("v", font_size=self.FS + 6, color=V_COLOR).move_to([bx + off, hy, 0])
        h_a = MathTex("a", font_size=self.FS + 6, color=A_COLOR).move_to([bx - off, hy, 0])
        heads = VGroup(h_v, h_a)
        whole = VGroup(rows, heads)
        dx = -whole.get_center()[0]
        whole.shift(RIGHT * dx)
        return rows, heads, v_list, a_list

    def b03_compare(self):
        for m in (self.ball, self.v, self.v_lab, self.a, self.a_lab):
            m.clear_updaters()
        old = VGroup(self.track, self.ball, self.v, self.v_lab, self.a, self.a_lab)
        self.remove(*old)
        self.add(old)
        rows, heads, v_list, a_list = self.build_rows()
        new = VGroup(rows, heads)
        self.play(ReplacementTransform(old, new), run_time=1.5)
        self.wait(3.0)
        for v in v_list:
            self.play(Indicate(v, color=V_COLOR, scale_factor=1.3), run_time=1.0)
        self.wait(3.0)
        box = SurroundingRectangle(a_list, color=GOLD, stroke_width=7, buff=0.12, corner_radius=0.1)
        self.play(Create(box), run_time=0.8)
        self.rows_group = VGroup(new, box)
        self.wait(DURS["B03"] - 1.5 - 3.0 - 3.0 - 3.0 - 0.8)

    # ---------------- B04 — back to the peak, statement ----------------
    def b04_hold(self):
        if self.PORTRAIT:
            c, r, la, off = np.array([0.55, 1.1, 0]), 0.3, 1.3, 0.5
            text = "ZERO VELOCITY\n≠ ZERO ACCELERATION"
            ty = -1.3
        else:
            c, r, la, off = np.array([0.0, 1.0, 0]), 0.5, 2.0, 0.85
            text = "ZERO VELOCITY ≠ ZERO ACCELERATION"
            ty = -1.9
        ball = make_ball(r).move_to(c)
        v = v_mark(c + RIGHT * off, 0.0)
        v_lab = MathTex("v = 0", font_size=self.FS, color=V_COLOR).next_to(v, RIGHT, buff=0.15)
        a = a_mark(c + LEFT * off, la)
        a_lab = a_label(self.FS).next_to(a, LEFT, buff=0.15)
        peak = VGroup(ball, v, v_lab, a, a_lab)
        peak.shift(RIGHT * (-peak.get_center()[0]))
        statement = crisp_text(text, 28 if self.PORTRAIT else 40, color=INK, weight=BOLD, font=CAPTION_STYLE,
                               line_spacing=1.1).move_to([0, ty, 0])
        if statement.width > 2 * safe_half_w():
            statement.scale_to_fit_width(2 * safe_half_w())
        underline = Line(statement.get_corner(DL) + DOWN * 0.18, statement.get_corner(DR) + DOWN * 0.18,
                         color=CRIMSON, stroke_width=5)
        self.play(ReplacementTransform(self.rows_group, peak), run_time=1.5)
        self.wait(1.0)
        self.play(FadeIn(statement, shift=UP * 0.2), Create(underline), run_time=0.8)
        self.wait(DURS["B04"] - 3.3)
