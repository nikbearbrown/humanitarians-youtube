"""zero-work-carrying.py — Chapter 7, Work.

Carrying a box horizontally at constant speed: the upward force on the box is
perpendicular to its horizontal displacement, so W = F d cos 90° = 0.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh zero-work-carrying.py ZeroWorkCarrying
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching zero-work-carrying.py ZeroWorkCarrying
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

BOX_COLOR = "#C8A06E"   # cardboard
BOX_TAPE = "#E3C99F"
F_COLOR = TEAL
D_COLOR = CRIMSON


def make_figure(x, G, S, phase, tremble=0.0):
    """Napkin-doodle stick figure carrying a cardboard box, facing right.
    Index layout: 0,1 legs | 2 torso | 3 head | 4,5 arms | 6 box group."""
    sw = 4
    hip = np.array([x, G + 0.95 * S, 0])
    a = 0.38 * np.sin(2 * PI * phase)
    legs = []
    for ang in (a, -a):
        foot = np.array([x + np.tan(ang) * 0.95 * S, G, 0])
        legs.append(Line(hip, foot, color=INK, stroke_width=sw))
    shoulder = np.array([x, G + 1.95 * S, 0])
    torso = Line(hip, shoulder + UP * 0.08 * S, color=INK, stroke_width=sw)
    head = Circle(radius=0.25 * S, color=INK, stroke_width=sw).move_to([x, G + 2.3 * S, 0])
    dy = UP * tremble
    bx = x + 0.22 * S
    arm1 = VMobject(color=INK, stroke_width=sw).set_points_as_corners([
        shoulder, np.array([x + 0.1 * S, G + 1.45 * S, 0]) + dy, np.array([bx, G + 1.5 * S, 0]) + dy])
    arm2 = VMobject(color=INK, stroke_width=sw).set_points_as_corners([
        shoulder, np.array([x + 0.16 * S, G + 1.62 * S, 0]) + dy, np.array([bx, G + 1.75 * S, 0]) + dy])
    c = np.array([x + 0.62 * S, G + 1.6 * S, 0]) + dy
    body = Rectangle(width=0.8 * S, height=0.65 * S, color=INK, stroke_width=3,
                     fill_color=BOX_COLOR, fill_opacity=1).move_to(c)
    tape = Rectangle(width=0.12 * S, height=0.65 * S, stroke_width=0, fill_color=BOX_TAPE,
                     fill_opacity=1).move_to(c)
    flap = Line(c + np.array([-0.4 * S, 0.2 * S, 0]), c + np.array([0.4 * S, 0.2 * S, 0]),
                color=INK, stroke_width=1.5)
    box = VGroup(body, tape, flap, body.copy().set_fill(opacity=0))
    return VGroup(legs[0], legs[1], torso, head, arm1, arm2, box)


def box_corner(x, G, S):
    """Top-right corner of the box (where F and d start)."""
    return np.array([x + 1.02 * S, G + 1.925 * S, 0])


def make_drop(S):
    d = Dot(radius=0.06 * S, color=TEAL)
    t = Triangle(color=TEAL, fill_color=TEAL, fill_opacity=1, stroke_width=0).scale(0.075 * S)
    t.move_to(d.get_top() + UP * 0.03 * S)
    return VGroup(d, t)


class ZeroWorkCarrying(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if self.PORTRAIT:
            self.S, self.G, self.XF = 0.75, -0.6, -0.95
            self.FS = 34
        else:
            self.S, self.G, self.XF = 1.6, -2.8, -2.2
            self.FS = 46
        # walked distance; landscape translates the figure, portrait scrolls the floor
        self.WALK = 0.0 if self.PORTRAIT else 3.6
        self.w = ValueTracker(0.0)

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_walk()
        self.b01_vectors()
        self.b02_split()
        self.b03_zero()
        self.b04_hold()

    def fig_x(self):
        if self.PORTRAIT:
            return self.XF
        return self.XF - self.WALK + self.w.get_value()

    def floor(self):
        G = self.G
        xl, xr = -safe_half_w(), safe_half_w()
        line = Line([xl, G, 0], [xr, G, 0], color=SLATE, stroke_width=3)
        off = (self.w.get_value() % 0.45) if self.PORTRAIT else 0.0
        hatch = VGroup()
        xk = xl + 0.15 + 0.45 - off
        while xk < xr:
            hatch.add(Line([xk, G, 0], [xk - 0.15, G - 0.15, 0], color=SLATE, stroke_width=2))
            xk += 0.45
        return VGroup(line, hatch)

    # ---------------- B00 — walking with the box ----------------
    def b00_walk(self):
        S = self.S
        stride = 0.7 * S
        floor = always_redraw(self.floor)
        fig = always_redraw(lambda: make_figure(
            self.fig_x(), self.G, S, self.w.get_value() / stride,
            tremble=0.018 * S * np.sin(45 * self.time)))
        self.play(FadeIn(floor), FadeIn(fig), run_time=0.8)
        # portrait walks in place: floor scrolls by the same distance
        total = 3.6 if not self.PORTRAIT else 3.0
        T = DURS["B00"] - 0.8
        drops = []
        for k in range(2):
            d = make_drop(S)
            dx = (-0.45 + 0.25 * k) * S
            dy = (2.75 + 0.15 * k) * S
            d.add_updater(lambda m, dx=dx, dy=dy: m.move_to([self.fig_x() + dx, self.G + dy, 0]))
            drops.append(d)
        segs = [T * 0.3, T * 0.3, T * 0.4]
        acc = 0.0
        for i, seg in enumerate(segs):
            acc += seg
            anims = [self.w.animate.set_value(total * acc / T)]
            if i >= 1:
                anims.append(FadeIn(drops[i - 1], scale=0.5))
            self.play(*anims, run_time=seg, rate_func=linear)
        self.floor_m, self.fig, self.drops = floor, fig, drops

    # ---------------- B01 — freeze; F up, d right, 90° ----------------
    def b01_vectors(self):
        S = self.S
        self.fig.clear_updaters()
        self.floor_m.clear_updaters()
        for d in self.drops:
            d.clear_updaters()
        x = self.fig_x()
        P = box_corner(x, self.G, S)
        F = Arrow(P, P + UP * 1.3 * S, buff=0, color=F_COLOR, stroke_width=8,
                  max_tip_length_to_length_ratio=0.22)
        F_lab = MathTex(r"\vec F", font_size=self.FS, color=F_COLOR).next_to(F, LEFT, buff=0.12)
        d = Arrow(P, P + RIGHT * 1.5 * S, buff=0, color=D_COLOR, stroke_width=8,
                  max_tip_length_to_length_ratio=0.2)
        d_lab = MathTex(r"\vec d", font_size=self.FS, color=D_COLOR).next_to(d, DOWN, buff=0.12)
        sq = Square(side_length=0.26 * S, color=SLATE, stroke_width=3).move_to(P + np.array([0.13 * S, 0.13 * S, 0]))
        deg = MathTex(r"90^\circ", font_size=self.FS - 8, color=INK).move_to(P + np.array([0.62 * S, 0.55 * S, 0]))

        self.play(*[FadeOut(dr) for dr in self.drops], run_time=0.4)
        self.wait(3.0)
        self.play(GrowArrow(F), FadeIn(F_lab), run_time=0.8)
        self.wait(3.8)
        self.play(GrowArrow(d), FadeIn(d_lab), run_time=0.8)
        self.wait(3.8)
        self.play(Create(sq), FadeIn(deg), run_time=0.6)
        self.F, self.F_lab, self.d, self.d_lab, self.sq, self.deg = F, F_lab, d, d_lab, sq, deg
        self.diagram_copy = VGroup(F, F_lab, d, d_lab, sq, deg).copy()
        self.fig.save_state()
        self.wait(DURS["B01"] - 13.2)

    # ---------------- B02 — split: drawing | W = F d cos θ ----------------
    def b02_split(self):
        group = VGroup(self.fig, self.F, self.F_lab, self.d, self.d_lab, self.sq, self.deg)
        if self.PORTRAIT:
            divider = DashedLine([-safe_half_w(), 0.3, 0], [safe_half_w(), 0.3, 0], color=SLATE, stroke_width=2)
            target = dict(scale=0.9, pos=[0, 1.75, 0])
            ex, ys, efs = 0.0, [-0.25, -1.0, -1.8], 40
        else:
            divider = Line([0.2, -3.0, 0], [0.2, 3.0, 0], color=SLATE, stroke_width=2)
            target = dict(scale=0.85, pos=[-3.4, 0, 0])
            ex, ys, efs = 3.6, [1.3, 0.0, -1.3], 62
        L1 = MathTex("W", "=", "F", "d", r"\cos", r"\theta", font_size=efs, color=INK).move_to([ex, ys[0], 0])
        L1[2].set_color(F_COLOR)
        L1[3].set_color(D_COLOR)
        L2 = MathTex(r"\cos 90^\circ = 0", font_size=efs, color=INK).move_to([ex, ys[1], 0])
        self.play(FadeOut(self.floor_m), group.animate.scale(target["scale"]).move_to(target["pos"]),
                  Create(divider), run_time=1.2)
        self.wait(5.8)
        self.play(Write(L1), run_time=2.0)
        self.wait(5.0)
        ring = Circle(radius=0.36 * efs / 62 + 0.05, color=CRIMSON, stroke_width=5).move_to(L1[5])
        link = DashedLine(ring.get_center(), self.sq.get_center(), color=CRIMSON, stroke_width=3,
                          dash_length=0.1)
        # trim the link so it starts on the ring's edge and stops short of the label
        u = link.get_unit_vector()
        link = DashedLine(ring.get_center() + u * (ring.width / 2 + 0.05),
                          self.sq.get_center() - u * (self.sq.width * 0.75 + 0.06),
                          color=CRIMSON, stroke_width=3, dash_length=0.1)
        self.play(Create(ring), Create(link), Indicate(VGroup(self.sq, self.deg), color=CRIMSON), run_time=1.0)
        self.wait(3.0)
        self.play(Write(L2), run_time=1.2)
        self.divider, self.L1, self.L2, self.ring, self.link = divider, L1, L2, ring, link
        self.eq_y3, self.eq_x, self.efs = ys[2], ex, efs
        self.wait(DURS["B02"] - 19.2)

    # ---------------- B03 — W = 0; muscles vs work ----------------
    def b03_zero(self):
        S = self.S
        L3 = MathTex("W = 0", font_size=self.efs + 6, color=CRIMSON).move_to([self.eq_x, self.eq_y3, 0])
        u1 = Line(L3.get_corner(DL) + DOWN * 0.12, L3.get_corner(DR) + DOWN * 0.12, color=CRIMSON, stroke_width=4)
        u2 = u1.copy().shift(DOWN * 0.1)
        self.play(Write(L3), run_time=0.8)
        self.play(Create(u1), Create(u2), run_time=0.5)
        self.wait(1.7)

        x = self.XF
        P = box_corner(x, self.G, S)
        if self.PORTRAIT:
            spos = np.array([1.0, 1.4, 0])
            bpos, btxt, bfs = np.array([0.1, 2.55, 0]), "muscle effort\n≠ work on the box", 20
        else:
            spos = P + np.array([1.5, 0.85, 0])
            bpos, btxt, bfs = np.array([-3.6, 2.2, 0]), "muscle effort\n≠ work on the box", 28
        stamp_txt = MathTex("W = 0", font_size=self.FS + 6, color=CRIMSON)
        stamp_box = SurroundingRectangle(stamp_txt, color=CRIMSON, stroke_width=5, buff=0.15, corner_radius=0.08)
        stamp = VGroup(stamp_box, stamp_txt).rotate(8 * DEGREES).move_to(spos)

        floor = self.floor()
        zero = VGroup(L3, u1, u2)
        self.remove(L3, u1, u2)
        self.add(zero)
        self.play(
            FadeOut(self.L1), FadeOut(self.L2), FadeOut(self.ring), FadeOut(self.link), FadeOut(self.divider),
            FadeOut(self.F), FadeOut(self.F_lab), FadeOut(self.d), FadeOut(self.d_lab), FadeOut(self.sq), FadeOut(self.deg),
            Restore(self.fig), FadeIn(floor),
            ReplacementTransform(zero, stamp),
            run_time=1.2,
        )
        self.floor_m = floor
        arms = VGroup(self.fig[4], self.fig[5])
        self.play(arms.animate.set_stroke(CRIMSON, width=8), run_time=0.6)
        self.play(Wiggle(arms, scale_value=1.05, rotation_angle=0.03 * TAU), run_time=1.2)
        self.wait(3.0)

        text = crisp_text(btxt, bfs, color=INK, font=CAPTION_STYLE, line_spacing=1.1).move_to(bpos)
        cloud = Ellipse(width=text.width + 0.6, height=text.height + 0.45, color=SLATE, stroke_width=3,
                        fill_color=CREAM, fill_opacity=1).move_to(text)
        head_top = self.fig[3].get_top()
        p0 = cloud.get_bottom() + (head_top - cloud.get_bottom()) * 0.35
        p1 = cloud.get_bottom() + (head_top - cloud.get_bottom()) * 0.7
        puffs = VGroup(Circle(radius=0.09 * S + 0.03, color=SLATE, stroke_width=3).move_to(p0),
                       Circle(radius=0.05 * S + 0.02, color=SLATE, stroke_width=3).move_to(p1))
        bubble = VGroup(puffs, cloud, text)
        self.play(FadeIn(bubble), run_time=0.8)
        self.stamp, self.bubble, self.arms = stamp, bubble, arms
        self.wait(DURS["B03"] - 9.8)

    # ---------------- B04 — the same diagram, W = F d cos 90° = 0 ----------------
    def b04_hold(self):
        S = self.S
        diagram = self.diagram_copy
        if self.PORTRAIT:
            ey, efs = -1.55, 38
        else:
            ey, efs = -3.3, 56
        eq = MathTex("W", "=", "F", "d", r"\cos 90^\circ", "=", "0", font_size=efs, color=INK).move_to([0, ey, 0])
        eq[2].set_color(F_COLOR)
        eq[3].set_color(D_COLOR)
        eq[6].set_color(CRIMSON)
        if eq.width > 2 * safe_half_w():
            eq.scale_to_fit_width(2 * safe_half_w())
        self.play(FadeOut(self.stamp), FadeOut(self.bubble),
                  self.arms.animate.set_stroke(INK, width=4), FadeIn(diagram), run_time=1.0)
        self.wait(1.5)
        self.play(Write(eq), run_time=1.5)
        box = self.fig[6]
        ring = Circle(radius=max(box.width, box.height) * 0.75, color=GOLD, stroke_width=7).move_to(box)
        self.play(Create(ring), run_time=0.8)
        self.wait(DURS["B04"] - 4.8)
