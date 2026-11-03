"""centripetal-friction.py — Chapter 6, Centripetal Force.

A car rounding a curve at constant speed needs an inward force even though
its speed never changes. That force is static friction between tires and
road, acting perpendicular to velocity, toward the arc's center. Remove it
and the car goes straight (Newton's first law).

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh centripetal-friction.py CentripetalFriction
  Portrait  (9:16): manim -r 1080,1920 --fps 60 --disable_caching centripetal-friction.py CentripetalFriction
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

CAR_COLOR = SLATE

# is_portrait() must run at module level (sets config.background_color
# before the camera is constructed) — calling it inside construct() is too
# late and leaves the background black (confirmed bug).
PORTRAIT = is_portrait()


def make_car(scale=1.0):
    s = scale
    body = RoundedRectangle(
        width=0.9 * s, height=0.42 * s, corner_radius=0.08 * s,
        color=INK, fill_color=CAR_COLOR, fill_opacity=1, stroke_width=2.5,
    )
    windshield = Rectangle(
        width=0.32 * s, height=0.2 * s, color=INK, fill_color=CREAM, fill_opacity=0.9, stroke_width=1.5,
    ).move_to(body.get_center() + UP * 0.02 * s)
    wheel_fl = Rectangle(width=0.14 * s, height=0.1 * s, color=INK, fill_color=INK, fill_opacity=1).move_to(
        body.get_center() + [-0.28 * s, -0.24 * s, 0]
    )
    wheel_fr = wheel_fl.copy().move_to(body.get_center() + [0.28 * s, -0.24 * s, 0])
    return VGroup(body, windshield, wheel_fl, wheel_fr)


class CentripetalFriction(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            # R sized so the car (and its v arrow) at the arc's right end
            # stays inside the 4.5-wide portrait frame (was 2.1: car clipped)
            self.CENTER = np.array([-0.25, -0.3, 0])  # shifted left: v label + skid stay inside the right edge
            self.R = 1.5
            self.CAR_SCALE = 0.7
            self.F0, self.F1 = 0.3, 0.85
        else:
            self.CENTER = np.array([0.0, -0.5, 0])
            self.R = 2.6
            self.CAR_SCALE = 1.0
            self.F0, self.F1 = 0.35, 1.1

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_curve()
        self.b02_missing_force()
        self.b03_reveal_friction()
        self.b04_trace_arc()
        self.b05_break_and_restore()
        self.b06_outro()

    # ---------------- B00 — straight road, forward velocity ----------------
    def b00_hook(self):
        y = -1.6 if not self.PORTRAIT else -1.9
        road = DashedLine(
            [-safe_half_w() + 0.3, y, 0], [safe_half_w() - 0.3, y, 0], color=SLATE, stroke_width=3,
        )
        car = make_car(self.CAR_SCALE).move_to([-safe_half_w() + 1.4, y + 0.3, 0])
        v_arrow = Arrow(
            car.get_center() + [0.5, 0, 0], car.get_center() + [1.5, 0, 0],
            color=INK, buff=0, stroke_width=6,
        )
        v_label = crisp_text("v", font_size=22, color=INK)
        v_label.move_to(v_arrow.get_end() + v_arrow.get_unit_vector() * 0.25)

        self.play(Create(road), FadeIn(car), run_time=0.8)
        self.play(GrowArrow(v_arrow), FadeIn(v_label), run_time=0.6)

        self.road, self.car, self.v_arrow, self.v_label = road, car, v_arrow, v_label
        self.wait(max(DURS["B00"] - 1.4, 0.3))

    # ---------------- B01 — road bends into an arc, v stays tangent ----------------
    def b01_curve(self):
        # Arc from angle a0 (car's current heading, pointing "outward" i.e.
        # tangent-left) sweeping clockwise toward the top of the circle.
        self.theta = ValueTracker(PI)  # start: car at angle PI (left side), heading +x (tangent)
        start_theta = PI

        def car_point(theta):
            return self.CENTER + self.R * np.array([np.cos(theta), np.sin(theta), 0])

        def tangent_dir(theta):
            # clockwise motion: d/dt (cos, sin) with theta decreasing -> tangent = (sin, -cos)
            return np.array([np.sin(theta), -np.cos(theta), 0])

        arc = Arc(
            radius=self.R, start_angle=PI, angle=-PI * 0.85, arc_center=self.CENTER,
            color=SLATE, stroke_width=3,
        )
        arc_dashed = DashedVMobject(arc, num_dashes=40)

        # fade the straight road into the arc
        self.play(FadeOut(self.road), Create(arc_dashed), run_time=1.0)
        self.arc_dashed = arc_dashed

        def car_updater(m):
            th = self.theta.get_value()
            p = car_point(th)
            d = tangent_dir(th)
            ang = np.arctan2(d[1], d[0])
            m.become(make_car(self.CAR_SCALE))
            m.rotate(ang)
            m.move_to(p)

        def v_updater(m):
            th = self.theta.get_value()
            p = car_point(th)
            d = tangent_dir(th)
            start = p + 0.55 * d
            end = p + 1.3 * d
            m.become(Arrow(start, end, color=INK, buff=0, stroke_width=6))

        def vlabel_updater(m):
            m.next_to(self.v_arrow, self.v_arrow.get_unit_vector() * 0 + UP, buff=0.1)

        self.car.add_updater(car_updater)
        self.v_arrow.add_updater(v_updater)
        self.v_label.add_updater(lambda m: m.move_to(self.v_arrow.get_end() + self.v_arrow.get_unit_vector() * 0.25))

        self.play(self.theta.animate.set_value(start_theta - PI * 0.55), run_time=DURS["B01"] - 1.3, rate_func=linear)
        self.wait(0.3)

    # ---------------- B02 — freeze, show the missing inward force ----------------
    def b02_missing_force(self):
        self.car.clear_updaters()
        self.v_arrow.clear_updaters()
        self.v_label.clear_updaters()

        guide = DashedLine(self.car.get_center(), self.CENTER, color=CRIMSON, stroke_width=2)
        qmark = crisp_text("???", font_size=28, color=CRIMSON).move_to(
            self.car.get_center() + (self.CENTER - self.car.get_center()) * 0.5 + UP * 0.3
        )
        center_dot = Dot(self.CENTER, color=SLATE, radius=0.04)

        self.play(Create(guide), FadeIn(center_dot), FadeIn(qmark), run_time=0.8)
        self.guide, self.qmark, self.center_dot = guide, qmark, center_dot
        self.wait(max(DURS["B02"] - 0.8, 0.3))

    # ---------------- B03 — reveal: static friction, inward ----------------
    def b03_reveal_friction(self):
        self.play(FadeOut(self.qmark), FadeOut(self.guide), run_time=0.4)

        inward_dir = (self.CENTER - self.car.get_center())
        inward_dir = inward_dir / np.linalg.norm(inward_dir)
        f_start = self.car.get_center() + self.F0 * inward_dir
        f_end = self.car.get_center() + self.F1 * inward_dir
        f_arrow = Arrow(f_start, f_end, color=TEAL, buff=0, stroke_width=7)
        f_label = crisp_text("static friction", font_size=18, color=TEAL, font=CAPTION_STYLE).next_to(f_arrow, DOWN, buff=0.15)

        self.play(GrowArrow(f_arrow), FadeIn(f_label), run_time=0.8)
        self.f_arrow, self.f_label = f_arrow, f_label
        self.wait(max(DURS["B03"] - 1.2, 0.3))

    # ---------------- B04 — trace the arc, friction stays pinned inward ----------------
    def b04_trace_arc(self):
        self.f_label.clear_updaters()
        self.f_label.add_updater(lambda m: m.next_to(self.f_arrow, DOWN, buff=0.15))

        def car_point(theta):
            return self.CENTER + self.R * np.array([np.cos(theta), np.sin(theta), 0])

        def tangent_dir(theta):
            return np.array([np.sin(theta), -np.cos(theta), 0])

        def car_updater(m):
            th = self.theta.get_value()
            p = car_point(th)
            d = tangent_dir(th)
            ang = np.arctan2(d[1], d[0])
            m.become(make_car(self.CAR_SCALE))
            m.rotate(ang)
            m.move_to(p)

        def v_updater(m):
            th = self.theta.get_value()
            p = car_point(th)
            d = tangent_dir(th)
            m.become(Arrow(p + 0.55 * d, p + 1.3 * d, color=INK, buff=0, stroke_width=6))

        def f_updater(m):
            th = self.theta.get_value()
            p = car_point(th)
            inward = (self.CENTER - p) / self.R
            m.become(Arrow(p + self.F0 * inward, p + self.F1 * inward, color=TEAL, buff=0, stroke_width=7))

        self.car.add_updater(car_updater)
        self.v_arrow.add_updater(v_updater)
        self.f_arrow.add_updater(f_updater)
        self.v_label.add_updater(lambda m: m.move_to(self.v_arrow.get_end() + self.v_arrow.get_unit_vector() * 0.25))

        trace = TracedPath(self.car.get_center, stroke_color=GOLD, stroke_width=4, dissipating_time=None)
        self.add(trace)
        # trace under the car/arrows, not drawn across the car body
        self.bring_to_front(self.car, self.v_arrow, self.v_label, self.f_arrow, self.f_label)
        self.trace = trace

        end_theta = PI - PI * 0.55 - PI * 0.35
        self.play(self.theta.animate.set_value(end_theta), run_time=DURS["B04"], rate_func=linear)

    # ---------------- B05 — remove friction, car skids straight; restore ----------------
    def b05_break_and_restore(self):
        self.car.clear_updaters()
        self.v_arrow.clear_updaters()
        self.f_arrow.clear_updaters()
        self.v_label.clear_updaters()

        th = self.theta.get_value()
        p = self.CENTER + self.R * np.array([np.cos(th), np.sin(th), 0])
        d = np.array([np.sin(th), -np.cos(th), 0])

        self.play(FadeOut(self.f_arrow), FadeOut(self.f_label), run_time=0.3)

        skid = (0.9 if self.PORTRAIT else 1.8) * d
        # the gold trail "snaps straight": pause the TracedPath and draw the
        # straight excursion as its own gold segment, faded on restore, so it
        # never lingers on top of the v arrow afterwards
        self.trace.clear_updaters()
        skid_line = Line(p, p + skid, color=GOLD, stroke_width=4)
        self.add(skid_line)
        self.bring_to_front(self.car, self.v_arrow, self.v_label)
        t_skid = max(DURS["B05"] * 0.25, 0.5)
        # car, v arrow and v label travel together (v must not be left behind)
        self.play(
            Create(skid_line), self.car.animate.shift(skid),
            self.v_arrow.animate.shift(skid), self.v_label.animate.shift(skid),
            run_time=t_skid,
        )
        self.wait(0.2)

        # restore: snap back onto the arc, friction reappears
        self.play(
            FadeOut(skid_line), self.car.animate.shift(-skid),
            self.v_arrow.animate.shift(-skid), self.v_label.animate.shift(-skid),
            run_time=0.4,
        )
        inward = (self.CENTER - p) / self.R
        f_arrow2 = Arrow(p + self.F0 * inward, p + self.F1 * inward, color=TEAL, buff=0, stroke_width=7)
        f_label2 = crisp_text("static friction", font_size=18, color=TEAL, font=CAPTION_STYLE).next_to(f_arrow2, DOWN, buff=0.15)
        self.play(GrowArrow(f_arrow2), FadeIn(f_label2), run_time=0.5)
        self.f_arrow, self.f_label = f_arrow2, f_label2
        # beat total == DURS["B05"]: 0.3 + t_skid + 0.2 + 0.4 + 0.5 + wait
        self.wait(max(DURS["B05"] - (1.4 + t_skid), 0.3))

    # ---------------- B06 — outro: hold, labeled ----------------
    def b06_outro(self):
        # Positioned near the top of the frame, not the caption band at the
        # bottom (confirmed bug: sharing the caption's y collided with the
        # burned-in caption text).
        summary = crisp_text("NOT FORWARD. INWARD.", font_size=22, color=INK, font=CAPTION_STYLE).move_to(
            [0, safe_half_h() - 0.6, 0]
        )
        # Inside the arc, just below its center: the only region no car,
        # arrow, arc or trace ever occupies (was placed right of the arrow,
        # on top of the car and off-frame in portrait).
        label_txt = ("centripetal force\n= static friction" if self.PORTRAIT
                     else "centripetal force = static friction")
        final_label = crisp_text(label_txt, font_size=18, color=TEAL, line_spacing=1.0, font=CAPTION_STYLE).move_to(
            self.CENTER + DOWN * (0.75 if self.PORTRAIT else 0.6)
        )
        self.play(FadeOut(self.f_label), FadeIn(final_label), FadeIn(summary), run_time=0.6)
        self.wait(max(DURS["B06"] - 0.6, 0.3))
