"""crumple-zones.py — Chapter 9, Impulse and Collisions.

Same change in momentum for both passengers; the crumpling car stretches the
stop over a longer time, so the average force F = Δp/Δt is smaller.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh crumple-zones.py CrumpleZones
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching crumple-zones.py CrumpleZones
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

RIGID_C = CRIMSON
CRUMPLE_C = TEAL
FRONT = 0.24      # crumple section, fraction of car length
CRUSH_MAX = 0.13  # how much the crumple section folds, fraction of car length


def make_car(x_rear, yg, L, color, crumple=False, crush=0.0):
    """Side-view car facing right, rear at x_rear, wheels on ground y=yg.
    Index layout: 0 body | 1 cabin | 2 window | 3 passenger | 4 front section | 5 wheels."""
    h = 0.26 * L
    yb = yg + 0.09 * L
    main_w = (1 - FRONT) * L
    body = Rectangle(width=main_w, height=h, color=INK, stroke_width=3, fill_color=color, fill_opacity=1)
    body.move_to([x_rear + main_w / 2, yb + h / 2, 0])
    cab_l, cab_r = x_rear + 0.18 * L, x_rear + 0.62 * L
    cabin = Polygon([cab_l, yb + h, 0], [cab_l + 0.08 * L, yb + h + 0.2 * L, 0],
                    [cab_r - 0.1 * L, yb + h + 0.2 * L, 0], [cab_r, yb + h, 0],
                    color=INK, stroke_width=3, fill_color=color, fill_opacity=1)
    win = Polygon([cab_l + 0.05 * L, yb + h + 0.02 * L, 0], [cab_l + 0.1 * L, yb + h + 0.17 * L, 0],
                  [cab_r - 0.12 * L, yb + h + 0.17 * L, 0], [cab_r - 0.05 * L, yb + h + 0.02 * L, 0],
                  color=INK, stroke_width=2, fill_color=CREAM, fill_opacity=1)
    head_c = np.array([cab_l + 0.2 * L, yb + h + 0.105 * L, 0])
    head = Circle(radius=0.045 * L, color=INK, stroke_width=2.5, fill_color=CREAM, fill_opacity=1).move_to(head_c)
    torso = Line(head_c + DOWN * 0.045 * L, head_c + DOWN * 0.12 * L, color=INK, stroke_width=3)
    passenger = VGroup(torso, head)
    fx0 = x_rear + main_w
    fw = FRONT * L - (crush * L if crumple else 0.0)
    fh = h * 0.85
    front_box = Rectangle(width=fw, height=fh, color=INK, stroke_width=3, fill_color=color,
                          fill_opacity=1 if not crumple else 0.55).move_to([fx0 + fw / 2, yb + fh / 2, 0])
    front = VGroup(front_box)
    if crumple:
        n = 6
        pts = []
        for i in range(n + 1):
            x = fx0 + fw * i / n
            pts.append([x, yb + (0.08 * h if i % 2 == 0 else fh - 0.08 * h), 0])
        front.add(VMobject(color=INK, stroke_width=2.5).set_points_as_corners(pts))
    wheels = VGroup(*[
        Circle(radius=0.075 * L, color=INK, stroke_width=2, fill_color=INK, fill_opacity=1).move_to(
            [x_rear + f * L, yg + 0.075 * L, 0]) for f in (0.17, 0.62)])
    return VGroup(body, cabin, win, passenger, front, wheels)


def car_length(crumple, crush):
    return 1 - (crush if crumple else 0.0)


def make_clock(center, r, frac, color):
    face = Circle(radius=r, color=INK, stroke_width=3, fill_color=CREAM, fill_opacity=1).move_to(center)
    sector = Sector(radius=r * 0.92, angle=-frac * TAU, start_angle=PI / 2, stroke_width=0,
                    fill_color=color, fill_opacity=0.85, arc_center=center)
    hand = Line(center, center + UP * r * 0.8, color=INK, stroke_width=3)
    return VGroup(face, sector, hand)


class CrumpleZones(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.L, self.WALL_X, self.YS = 1.5, 1.42, [1.15, -1.35]
            self.X0, self.FS, self.LFS = -1.62, 30, 16
            self.ARROW_R, self.ARROW_C = 1.75, 0.35
        else:
            self.L, self.WALL_X, self.YS = 2.6, 5.0, [0.9, -2.4]
            self.X0, self.FS, self.LFS = -6.0, 46, 28
            self.ARROW_R, self.ARROW_C = 3.0, 0.6

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_setup()
        self.b01_rigid()
        self.b02_crumple()
        self.b03_graphs()
        self.b04_hold()

    # ---------------- B00 — two cars, same speed ----------------
    def b00_setup(self):
        L = self.L
        top = self.YS[0] + 0.75 * L
        wall = Rectangle(width=0.22 if self.PORTRAIT else 0.35, height=(self.YS[0] + 0.75 * L) - (self.YS[1] - 0.15),
                         color=INK, stroke_width=3, fill_color=INK, fill_opacity=1)
        wall.move_to([self.WALL_X + wall.width / 2, (top + self.YS[1] - 0.15) / 2, 0])
        grounds = VGroup(*[Line([-safe_half_w() - 0.4, y, 0], [self.WALL_X, y, 0], color=SLATE, stroke_width=3)
                           for y in self.YS])
        self.x_r = ValueTracker(self.X0)
        self.x_c = ValueTracker(self.X0)
        self.crush = ValueTracker(0.0)
        rigid = always_redraw(lambda: make_car(self.x_r.get_value(), self.YS[0], L, RIGID_C))
        crump = always_redraw(lambda: make_car(self.x_c.get_value(), self.YS[1], L, CRUMPLE_C,
                                               crumple=True, crush=self.crush.get_value()))
        lab_r = crisp_text("RIGID", self.LFS, color=RIGID_C, weight=BOLD, font=CAPTION_STYLE)
        lab_c = crisp_text("CRUMPLE ZONE", self.LFS, color=CRUMPLE_C, weight=BOLD, font=CAPTION_STYLE)
        lab_r.move_to([self.X0 + 0.0, self.YS[0] + 0.8 * L, 0], aligned_edge=LEFT)
        lab_c.move_to([self.X0 + 0.0, self.YS[1] + 0.8 * L, 0], aligned_edge=LEFT)
        lab_r.set_x(max(lab_r.get_x(), -safe_half_w() + lab_r.width / 2))
        lab_c.set_x(max(lab_c.get_x(), -safe_half_w() + lab_c.width / 2))
        # velocity arrows below each car's body, inside the lane (equal length = same speed)
        vlen = 0.55 * L
        def v_arrow(tracker, y):
            x = tracker.get_value() + L * 0.5
            return Arrow([x - vlen / 2, y - 0.17 * L, 0], [x + vlen / 2, y - 0.17 * L, 0], buff=0,
                         color=INK, stroke_width=5, max_tip_length_to_length_ratio=0.25)
        v_r = always_redraw(lambda: v_arrow(self.x_r, self.YS[0]))
        v_c = always_redraw(lambda: v_arrow(self.x_c, self.YS[1]))
        v_lr = always_redraw(lambda: MathTex("v", font_size=self.FS - 6, color=INK).next_to(v_r, DOWN, buff=0.06))
        v_lc = always_redraw(lambda: MathTex("v", font_size=self.FS - 6, color=INK).next_to(v_c, DOWN, buff=0.06))

        self.play(FadeIn(wall), Create(grounds), run_time=0.8)
        self.play(FadeIn(rigid), FadeIn(crump), FadeIn(lab_r), FadeIn(lab_c), run_time=0.8)
        self.play(GrowArrow(v_r), GrowArrow(v_c), FadeIn(v_lr), FadeIn(v_lc), run_time=0.7)
        self.wait(DURS["B00"] - 2.3)
        self.wall, self.grounds, self.rigid, self.crump = wall, grounds, rigid, crump
        self.lab_r, self.lab_c, self.v_r, self.v_c, self.v_lr, self.v_lc = lab_r, lab_c, v_r, v_c, v_lr, v_lc

    def speed(self):
        return 2.4 * self.L  # scene units per second, same for both cars

    # ---------------- B01 — rigid car: dead stop, huge force ----------------
    def b01_rigid(self):
        L = self.L
        x_stop = self.WALL_X - L
        t_drive = (x_stop - self.X0) / self.speed()
        self.play(FadeOut(self.lab_r), run_time=0.3)
        self.play(self.x_r.animate.set_value(x_stop), run_time=t_drive, rate_func=linear)
        # dead stop: velocity arrow gone in the same instant
        self.rigid.clear_updaters()
        self.v_r.clear_updaters()
        self.v_lr.clear_updaters()
        self.remove(self.v_r, self.v_lr)
        head = self.rigid[3][1]
        y_arr = self.YS[0] + 0.75 * L
        f_arrow = Arrow([head.get_x(), y_arr, 0], [head.get_x() - self.ARROW_R, y_arr, 0], buff=0,
                        color=RIGID_C, stroke_width=7, max_tip_length_to_length_ratio=0.12)
        f_lab = crisp_text("large force", self.LFS, color=RIGID_C, font=CAPTION_STYLE).next_to(f_arrow, UP, buff=0.1)
        clock = make_clock(np.array([x_stop - 0.42 * L if not self.PORTRAIT else x_stop - 0.3, self.YS[0] + 0.45 * L, 0]),
                           0.17 * L, 0.08, RIGID_C)
        c_lab = Tex(r"short $\Delta t$", font_size=self.FS - 10, color=INK).next_to(clock, DOWN, buff=0.08)
        cg = VGroup(clock, c_lab)
        cg.shift(RIGHT * ((x_stop - 0.12) - cg.get_right()[0]))
        self.play(GrowArrow(f_arrow), run_time=0.15, rate_func=linear)
        self.play(FadeIn(f_lab), FadeIn(clock), FadeIn(c_lab), run_time=0.6)
        self.f_r, self.f_lr, self.clock_r, self.clab_r = f_arrow, f_lab, clock, c_lab
        self.wait(DURS["B01"] - 1.05 - t_drive)

    # ---------------- B02 — crumple car: gradual stop, small force ----------------
    def b02_crumple(self):
        L = self.L
        x_touch = self.WALL_X - L
        t_drive = (x_touch - self.X0) / self.speed()
        self.play(FadeOut(self.lab_c), run_time=0.3)
        self.play(self.x_c.animate.set_value(x_touch), run_time=t_drive, rate_func=linear)
        head_x = lambda: self.crump[3][1].get_x()
        y_arr = self.YS[1] + 0.75 * L
        flen = ValueTracker(0.001)
        f_arrow = always_redraw(lambda: Arrow([head_x(), y_arr, 0], [head_x() - max(flen.get_value(), 0.02), y_arr, 0],
                                              buff=0, color=CRUMPLE_C, stroke_width=7,
                                              max_tip_length_to_length_ratio=0.5))
        self.add(f_arrow)
        # uniform deceleration over the crush distance, shown in 4 discrete fold steps:
        # equal crush increments take times proportional to sqrt-differences of a decelerating approach
        steps = 4
        D = CRUSH_MAX * L
        t_total = 3.0   # stop shown slowed for legibility; 4 discrete fold steps
        times = []
        for k in range(steps):
            # remaining distance after k steps: D*(1 - k/steps); time-to-stop ~ sqrt(remaining)
            t0 = 1 - np.sqrt(1 - k / steps)
            t1 = 1 - np.sqrt(1 - (k + 1) / steps)
            times.append((t1 - t0) * t_total)
        for k in range(steps):
            c = CRUSH_MAX * (k + 1) / steps
            self.play(self.crush.animate.set_value(c), self.x_c.animate.set_value(x_touch + c * L),
                      flen.animate.set_value(self.ARROW_C * (k + 1) / steps),
                      run_time=times[k], rate_func=linear)
        for m in (self.crump, self.v_c, self.v_lc, f_arrow):
            m.clear_updaters()
        self.play(FadeOut(self.v_c), FadeOut(self.v_lc), run_time=0.3)
        f_lab = crisp_text("small force", self.LFS, color=CRUMPLE_C, font=CAPTION_STYLE).next_to(f_arrow, UP, buff=0.1)
        x_stop = x_touch + CRUSH_MAX * L
        clock = make_clock(np.array([x_stop - 0.42 * L if not self.PORTRAIT else x_stop - 0.3, self.YS[1] + 0.45 * L, 0]),
                           0.17 * L, 0.4, CRUMPLE_C)
        c_lab = Tex(r"long $\Delta t$", font_size=self.FS - 10, color=INK).next_to(clock, DOWN, buff=0.08)
        cg = VGroup(clock, c_lab)
        cg.shift(RIGHT * ((x_stop - 0.12) - cg.get_right()[0]))
        self.play(FadeIn(f_lab), FadeIn(clock), FadeIn(c_lab), run_time=0.6)
        self.f_c, self.f_lc, self.clock_c, self.clab_c = f_arrow, f_lab, clock, c_lab
        self.wait(DURS["B02"] - 1.2 - t_drive - sum(times))

    # ---------------- B03 — two F-t graphs, equal areas ----------------
    def graph(self, origin, sx, sy, dt, F, color, title):
        ax_t = Arrow(origin, origin + RIGHT * (3.2 * sx), buff=0, color=INK, stroke_width=3,
                     max_tip_length_to_length_ratio=0.04)
        ax_f = Arrow(origin, origin + UP * (4.6 * sy), buff=0, color=INK, stroke_width=3,
                     max_tip_length_to_length_ratio=0.06)
        t_lab = MathTex("t", font_size=self.FS - 6, color=INK).next_to(ax_t, RIGHT, buff=0.08)
        f_lab = MathTex(r"F", font_size=self.FS - 6, color=INK).next_to(ax_f, UP, buff=0.06)
        rect = Rectangle(width=dt * sx, height=F * sy, stroke_color=INK, stroke_width=2.5,
                         fill_color=color, fill_opacity=0.75)
        rect.move_to(origin, aligned_edge=DL)
        ttl = crisp_text(title, self.LFS, color=color, weight=BOLD, font=CAPTION_STYLE)
        return VGroup(ax_t, ax_f, t_lab, f_lab), rect, ttl

    def b03_graphs(self):
        lanes = VGroup(self.wall, self.grounds, self.rigid, self.crump, self.f_r, self.f_lr, self.clock_r,
                       self.clab_r, self.f_c, self.f_lc, self.clock_c, self.clab_c)
        self.lanes_saved = VGroup(self.wall, self.grounds, self.rigid, self.crump).copy()
        if self.PORTRAIT:
            o1, o2, sx, sy = np.array([-1.45, 0.75, 0]), np.array([-1.45, -1.75, 0]), 0.9, 0.36
            eq_pos = np.array([0, 3.0, 0])
        else:
            o1, o2, sx, sy = np.array([-6.0, -1.7, 0]), np.array([0.6, -1.7, 0]), 1.65, 0.95
            eq_pos = np.array([0, -2.85, 0])
        ax1, r1, t1 = self.graph(o1, sx, sy, 0.5, 4.0, RIGID_C, "rigid")
        ax2, r2, t2 = self.graph(o2, sx, sy, 2.5, 0.8, CRUMPLE_C, "crumple zone")
        t1.next_to(r1, RIGHT, buff=0.25).align_to(r1, UP)
        t2.next_to(r2, UP, buff=0.2).align_to(r2, LEFT).shift(RIGHT * 0.1)
        eq = MathTex(r"J", "=", r"\bar F\,\Delta t", "=", r"\Delta p", font_size=self.FS, color=INK).move_to(eq_pos)
        same = crisp_text("same for both", self.LFS, color=SLATE, font=CAPTION_STYLE).next_to(eq, DOWN if self.PORTRAIT else RIGHT, buff=0.2)
        if self.PORTRAIT:
            same.next_to(eq, DOWN, buff=0.12)

        T = DURS["B03"]
        self.play(FadeOut(lanes), run_time=0.8)
        self.play(Create(ax1), Create(ax2), FadeIn(t1), FadeIn(t2), run_time=1.0)
        self.wait(0.6)
        self.play(GrowFromEdge(r1, LEFT), run_time=1.6, rate_func=linear)
        self.play(GrowFromEdge(r2, LEFT), run_time=3.2, rate_func=linear)
        self.wait(T * 0.2)
        self.play(Write(eq), run_time=1.2)
        self.play(FadeIn(same), run_time=0.5)
        self.wait(T * 0.25)
        self.play(Indicate(r1, color=GOLD, scale_factor=1.06), Indicate(r2, color=GOLD, scale_factor=1.06), run_time=1.2)
        self.wait(T - (10.1 + T * 0.45))
        self.graphs = VGroup(ax1, ax2, r1, r2, t1, t2, eq, same)

    # ---------------- B04 — back to the cars ----------------
    def b04_hold(self):
        lanes = self.lanes_saved
        rigid, crump = lanes[2], lanes[3]
        h_r, h_c = rigid[3][1], crump[3][1]
        star = Star(n=9, outer_radius=0.12 * self.L, inner_radius=0.07 * self.L, color=RIGID_C, stroke_width=5).move_to(h_r)
        calm = Circle(radius=0.09 * self.L, color=CRUMPLE_C, stroke_width=6).move_to(h_c)
        if self.PORTRAIT:
            tpos, txt = np.array([0, 2.85, 0]), "crumple zone:\nmore time, less force"
        else:
            tpos, txt = np.array([0, 3.0, 0]), "crumple zone: more time, less force"
        text = crisp_text(txt, 24 if self.PORTRAIT else 34, color=INK, weight=BOLD, font=CAPTION_STYLE,
                          line_spacing=1.1).move_to(tpos)
        self.play(FadeOut(self.graphs), run_time=0.8)
        self.play(FadeIn(lanes), run_time=0.8)
        self.play(Create(star), Create(calm), run_time=0.8)
        self.play(FadeIn(text, shift=DOWN * 0.15), run_time=0.8)
        self.wait(DURS["B04"] - 3.2)
