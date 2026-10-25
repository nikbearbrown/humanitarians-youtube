"""gyroscope-precession.py — Chapter 11.4, Precession of a Gyroscope.

Gravity's torque about the pivot of a tilted top, tau = r x Mg, is
horizontal and perpendicular to L, so (dL = tau dt) it turns L sideways
instead of tipping it: the spinning top precesses about the vertical. A
non-spinning top simply falls.

3D is drawn with a fixed oblique projection computed here (MedhavyScene is a
2D Scene). z is up, the pivot is the origin.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh gyroscope-precession.py GyroscopePrecession
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching gyroscope-precession.py GyroscopePrecession
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

WOOD = "#C8A165"
WOOD_LIGHT = "#E2C590"
G_C, L_C, T_C = CRIMSON, TEAL, GOLD     # gravity, angular momentum, torque

TILT = 25 * DEGREES
EL, AZ = 18 * DEGREES, 25 * DEGREES
U = np.array([-np.sin(AZ), np.cos(AZ), 0.0])                                   # screen right
W = np.array([-np.sin(EL) * np.cos(AZ), -np.sin(EL) * np.sin(AZ), np.cos(EL)])  # screen up
VIEW = np.array([np.cos(EL) * np.cos(AZ), np.cos(EL) * np.sin(AZ), np.sin(EL)])  # toward viewer

H_CONE, H_TOP, H_SPIN = 0.9, 1.05, 1.5   # body cone top, top face, spindle end (along axis)
R_BODY = 0.6
D_CM = 0.8
PREC = TAU / 9.0        # one precession sweep per 9 s
SPIN = 8 * PREC         # spin much faster than precession


def axis_vec(th, ph):
    return np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])


def torque_dir(ph):
    """tau = r x (-Mg z) is along (-sin ph, cos ph, 0) for axis azimuth ph."""
    return np.array([-np.sin(ph), np.cos(ph), 0.0])


def hull(pts):
    pts = sorted(map(tuple, pts))

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def outlined_arrow(p0, p1, color, sw=7, tip=0.22):
    under = Arrow(p0, p1, buff=0, color=INK, stroke_width=sw + 4, tip_length=tip + 0.05,
                  max_tip_length_to_length_ratio=0.4)
    over = Arrow(p0, p1, buff=0, color=color, stroke_width=sw, tip_length=tip,
                 max_tip_length_to_length_ratio=0.4)
    return VGroup(under, over)


class GyroscopePrecession(MedhavyScene):
    def construct(self):
        self.PORTRAIT = P = PORTRAIT
        if P:
            self.K, self.O = 1.0, np.array([0.0, -1.0, 0])
            self.FLOOR_R = 1.5
        else:
            self.K, self.O = 1.35, np.array([0.0, -2.2, 0])
            self.FLOOR_R = 2.4
        self.MATH = 34 if P else 42
        self.LBL = 18 if P else 22

        self.Uv, self.Wv = U, W
        self.th, self.ph, self.psi = TILT, AZ + PI / 2, 0.0   # unspun top falls to screen-right
        self.spinning, self.precessing = False, False

        if P:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_vectors()
        self.b02_perpendicular()
        self.b03_cone()
        self.b04_hold()

    # ---------------- projection + drawing ----------------
    def pr(self, p):
        p = np.asarray(p, dtype=float)
        return self.O + self.K * np.array([p @ self.Uv, p @ self.Wv, 0.0])

    def circle3(self, c, e1, e2, r, n=48, a0=0.0, a1=TAU):
        return [c + r * (np.cos(t) * e1 + np.sin(t) * e2) for t in np.linspace(a0, a1, n)]

    def make_top(self):
        a = axis_vec(self.th, self.ph)
        e1 = torque_dir(self.ph)
        e2 = np.cross(a, e1)
        rim1 = self.circle3(a * H_CONE, e1, e2, R_BODY)
        rim2 = self.circle3(a * H_TOP, e1, e2, R_BODY * 0.92)
        sil = hull([self.pr(p)[:2] for p in [np.zeros(3)] + rim1 + rim2])
        body = Polygon(*[[x, y, 0] for x, y in sil], color=INK, stroke_width=2.5, fill_color=WOOD, fill_opacity=1)
        g = VGroup(body)
        # spin stripes on the near side of the band (they move with psi)
        for k in range(6):
            ang = self.psi + k * TAU / 6
            dvec = np.cos(ang) * e1 + np.sin(ang) * e2
            if dvec @ VIEW > 0.05:
                p0 = a * (H_CONE * 0.55) + dvec * R_BODY * 0.55 * 0.95
                p1 = a * H_CONE + dvec * R_BODY
                p2 = a * H_TOP + dvec * R_BODY * 0.92
                g.add(VMobject(color=SLATE, stroke_width=4).set_points_as_corners([self.pr(p0), self.pr(p1), self.pr(p2)]))
        # top face, if it faces the viewer
        if a @ VIEW > 0.02:
            face = Polygon(*[self.pr(p) for p in rim2[:-1]], color=INK, stroke_width=2,
                           fill_color=WOOD_LIGHT, fill_opacity=1)
            g.add(face)
            for k in range(3):
                ang = self.psi + k * TAU / 3
                dvec = np.cos(ang) * e1 + np.sin(ang) * e2
                g.add(Line(self.pr(a * H_TOP + dvec * 0.12), self.pr(a * H_TOP + dvec * R_BODY * 0.85),
                           color=SLATE, stroke_width=3))
        g.add(Line(self.pr(a * H_TOP), self.pr(a * H_SPIN), color=INK, stroke_width=7))
        if self.spinning:
            # curled spin arrow around the spindle, counterclockwise about +a
            arc_pts = [self.pr(p) for p in self.circle3(a * 1.32, e1, e2, 0.3, n=30,
                                                         a0=self.psi * 0.5, a1=self.psi * 0.5 + 1.5 * PI)]
            curl = VMobject(color=INK, stroke_width=3).set_points_smoothly(arc_pts)
            dirv = arc_pts[-1] - arc_pts[-3]
            tipm = Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=1).scale(0.07)
            tipm.rotate(np.arctan2(dirv[1], dirv[0]) - PI / 2).move_to(arc_pts[-1])
            g.add(curl, tipm)
        return g

    def top_updater(self, m, dt):
        if self.spinning:
            self.psi += SPIN * dt
        if self.precessing:
            self.ph += PREC * dt
        m.become(self.make_top())

    def floor(self):
        pts = [self.pr(p) for p in self.circle3(np.zeros(3), np.array([1.0, 0, 0]), np.array([0, 1.0, 0]),
                                               self.FLOOR_R / self.K, n=72)]
        return Polygon(*pts[:-1], color=SLATE, stroke_width=2, fill_color="#EDEDED", fill_opacity=1)

    def g_start(self):
        """Gravity acts at the CM, but the arrow is drawn beside the body
        (offset to screen-right, clear of the silhouette) with a dashed
        leader from a CM dot, so it never pierces the top."""
        cm = axis_vec(self.th, self.ph) * D_CM
        return self.pr(cm), self.pr(cm) + RIGHT * (R_BODY + 0.22) * self.K

    def gravity_mob(self):
        cm_p, s = self.g_start()
        dz = self.pr([0, 0, 0.55]) - self.pr([0, 0, 0])
        lead = DashedLine(cm_p, s, color=G_C, stroke_width=2, dash_length=0.06)
        dot = Dot(cm_p, radius=0.045, color=G_C)
        return VGroup(lead, dot, outlined_arrow(s, s - dz, G_C, sw=6, tip=0.18))

    def gravity_label(self):
        _, s = self.g_start()
        dz = self.pr([0, 0, 0.55]) - self.pr([0, 0, 0])
        return MathTex("M", r"\vec g", font_size=self.MATH - 4, color=G_C).next_to(s - dz * 0.5, RIGHT, buff=0.15)

    def L_mob(self, ph=None, length=2.5, start=H_SPIN + 0.08):
        a = axis_vec(self.th, self.ph if ph is None else ph)
        return outlined_arrow(self.pr(a * start), self.pr(a * length), L_C, sw=7, tip=0.24)

    def L_label(self, ph=None, length=2.5):
        a = axis_vec(self.th, self.ph if ph is None else ph)
        return MathTex(r"\vec L", font_size=self.MATH, color=L_C).move_to(self.pr(a * (length + 0.25)) + UP * 0.08)

    def tau_mob(self):
        t = torque_dir(self.ph)
        return outlined_arrow(self.pr(np.zeros(3)), self.pr(t * 1.1), T_C, sw=7, tip=0.22)

    def tau_label(self):
        t = torque_dir(self.ph)
        return MathTex(r"\vec\tau", font_size=self.MATH, color=INK).move_to(self.pr(t * 1.1) + DOWN * 0.32)

    # ---------------- B00 — non-spinning top falls; spinning top circles ----------------
    def b00_hook(self):
        d = DURS["B00"]
        floor = self.floor()
        top = self.make_top()
        self.play(FadeIn(floor), FadeIn(top), run_time=0.8)
        g = always_redraw(self.gravity_mob)
        self.play(FadeIn(g), run_time=0.4)
        # not spinning: tilt grows until the body rim reaches the floor
        th_t = ValueTracker(TILT)

        def fall_upd(m):
            self.th = th_t.get_value()
            m.become(self.make_top())
        top.add_updater(fall_upd)
        self.wait(max(d * 0.22 - 1.2, 0.2))
        self.play(th_t.animate.set_value(62 * DEGREES), run_time=1.3, rate_func=rate_functions.ease_in_quad)
        self.wait(0.6)
        self.play(FadeOut(top), FadeOut(g), run_time=0.4)
        top.clear_updaters()
        # reset, spinning this time
        self.th = TILT
        # start azimuth chosen so precession ends B00 at ph = AZ + 45 deg, where
        # both the axis lean and the horizontal torque read clearly on screen
        used = 0.8 + 0.4 + max(d * 0.22 - 1.2, 0.2) + 1.3 + 0.6 + 0.4 + 0.5
        self.ph = AZ + PI / 4 - PREC * max(d - used, 0.3)
        self.spinning = True
        top2 = self.make_top()
        self.play(FadeIn(top2), FadeIn(g), run_time=0.5)
        top2.add_updater(self.top_updater)
        self.precessing = True
        used = 0.8 + 0.4 + max(d * 0.22 - 1.2, 0.2) + 1.3 + 0.6 + 0.4 + 0.5
        self.wait(max(d - used, 0.3))
        self.floor_m, self.top, self.g = floor, top2, g

    # ---------------- B01 — L along axis, torque horizontal at pivot ----------------
    def b01_vectors(self):
        d = DURS["B01"]
        n = [4, 13, 15, 6, 11]
        cue = np.cumsum([0] + n) / sum(n) * d
        self.precessing = False
        vline = DashedLine(self.pr(np.zeros(3)), self.pr([0, 0, 2.7]), color=SLATE, stroke_width=2, dash_length=0.1)
        Lm = always_redraw(self.L_mob)
        Ll = always_redraw(self.L_label)
        gl = always_redraw(self.gravity_label)
        tm = always_redraw(self.tau_mob)
        tl = always_redraw(self.tau_label)
        t = 0.0
        self.play(Create(vline), run_time=0.6); t += 0.6
        self.wait(max(cue[1] - t, 0.2)); t = max(cue[1], t + 0.2)
        self.play(GrowFromPoint(Lm, self.pr(axis_vec(self.th, self.ph) * H_SPIN)), FadeIn(Ll), run_time=0.9); t += 0.9
        self.wait(max(cue[2] - t, 0.2)); t = max(cue[2], t + 0.2)
        self.play(FadeIn(gl), run_time=0.5); t += 0.5
        self.wait(1.2); t += 1.2
        self.play(FadeIn(tm), FadeIn(tl), run_time=0.9); t += 0.9
        self.wait(max(cue[4] - t, 0.2)); t = max(cue[4], t + 0.2)
        self.play(Indicate(tl, color=T_C, scale_factor=1.3), run_time=1.0); t += 1.0
        self.wait(max(d - t, 0.2))
        self.vline, self.Lm, self.Ll, self.gl, self.tm, self.tl = vline, Lm, Ll, gl, tm, tl

    # ---------------- B02 — isolated diagram: tau dt turns L sideways ----------------
    def b02_perpendicular(self):
        d = DURS["B02"]
        P = self.PORTRAIT
        # isolate: keep only the vertical line and L; L now drawn from the pivot
        # (clear the bound-method updater first: FadeOut copies the mobject,
        # and deep-copying a bound method would try to copy the Scene)
        self.top.clear_updaters()
        self.play(FadeOut(self.top), FadeOut(self.floor_m), FadeOut(self.g), FadeOut(self.gl),
                  FadeOut(self.tm), FadeOut(self.tl), FadeOut(self.Lm), FadeOut(self.Ll), run_time=0.8)
        LEN = 2.5
        # the diagram is viewed from higher up (35 deg elevation) and zoomed,
        # so a horizontal sideways step of L reads clearly; restored after B02
        el2 = 35 * DEGREES
        self.Uv = U
        self.Wv = np.array([-np.sin(el2) * np.cos(AZ), -np.sin(el2) * np.sin(AZ), np.cos(el2)])
        K_save = self.K
        self.K = K_save * 1.2
        self.ph = AZ - PI / 6   # diagram pose: the sideways steps of L cross the screen plane
        phd = ValueTracker(self.ph)

        def tip():
            return axis_vec(self.th, phd.get_value()) * LEN

        L_full = always_redraw(lambda: self.L_mob(ph=phd.get_value(), length=LEN, start=0.0))
        def L_lab_mob():
            a = axis_vec(self.th, phd.get_value())
            p0, p1 = self.pr(np.zeros(3)), self.pr(a * LEN)
            dvec = (p1 - p0) / np.linalg.norm(p1 - p0)
            n = np.array([-dvec[1], dvec[0], 0])          # screen-left of the arrow
            return MathTex(r"\vec L", font_size=self.MATH, color=L_C).move_to(p1 + dvec * 0.38)
        L_lab = always_redraw(L_lab_mob)
        # crossed-out "falls" direction at the tip (tilt would grow)
        ph0 = self.ph
        a0 = axis_vec(self.th, ph0)
        fall_dir = np.array([np.cos(self.th) * np.cos(ph0), np.cos(self.th) * np.sin(ph0), -np.sin(self.th)])
        f0, f1 = self.pr(a0 * LEN), self.pr(a0 * LEN + fall_dir * 0.75)
        fall = Arrow(f0, f1, buff=0, color=SLATE, stroke_width=5, tip_length=0.18, stroke_opacity=0.5)
        fall.set_opacity(0.45)
        mid = (f0 + f1) / 2
        xm = VGroup(Line(mid + [-0.15, -0.15, 0], mid + [0.15, 0.15, 0], color=CRIMSON, stroke_width=5),
                    Line(mid + [-0.15, 0.15, 0], mid + [0.15, -0.15, 0], color=CRIMSON, stroke_width=5))

        def dl_mob():
            p = tip()
            return outlined_arrow(self.pr(p), self.pr(p + torque_dir(phd.get_value()) * 0.8), T_C, sw=6, tip=0.2)

        def dl_lab():
            p0 = self.pr(tip())
            p1 = self.pr(tip() + torque_dir(phd.get_value()) * 0.8)
            dvec = (p1 - p0) / max(np.linalg.norm(p1 - p0), 1e-6)
            m = MathTex(r"\vec\tau\,dt", font_size=self.MATH - 4, color=INK)
            # beyond the arrow tip along its own direction, never across the vertical line
            return m.move_to(p1 + dvec * (m.width / 2 + 0.15) + UP * 0.12)

        def right_mark():
            p = tip()
            a = axis_vec(self.th, phd.get_value())
            t = torque_dir(phd.get_value())
            s = 0.2
            return VMobject(color=INK, stroke_width=2.5).set_points_as_corners(
                [self.pr(p - a * s), self.pr(p - a * s + t * s), self.pr(p + t * s)])

        dl = always_redraw(dl_mob)
        dll = always_redraw(dl_lab)
        rm = always_redraw(right_mark)

        n = [8, 12, 21, 11]
        cue = np.cumsum([0] + n) / sum(n) * d
        t = 0.8
        self.play(FadeIn(L_full), FadeIn(L_lab), run_time=0.7); t += 0.7
        self.wait(max(cue[1] - t, 0.2)); t = max(cue[1], t + 0.2)
        self.play(FadeIn(dl), FadeIn(dll), run_time=0.7); t += 0.7
        self.wait(max(cue[2] - t, 0.2)); t = max(cue[2], t + 0.2)
        self.play(FadeIn(rm), run_time=0.5); t += 0.5
        self.play(GrowArrow(fall), run_time=0.6); t += 0.6
        self.play(Create(xm), run_time=0.5); t += 0.5
        self.wait(max(cue[3] - t - 0.4, 0.2)); t = max(cue[3] - 0.4, t + 0.2)
        self.play(FadeOut(fall), FadeOut(xm), run_time=0.4); t += 0.4
        ghosts = VGroup()
        step = 0.32
        for i in range(3):
            ghost = self.L_mob(ph=phd.get_value(), length=LEN, start=0.0).set_opacity(0.25)
            ghosts.add(ghost)
            self.add(ghost)
            self.play(phd.animate.increment_value(step), run_time=1.0); t += 1.0
            self.wait(0.3); t += 0.3
        arc = DashedVMobject(VMobject(color=L_C, stroke_width=2).set_points_smoothly(
            [self.pr(axis_vec(self.th, ph0 + s) * LEN) for s in np.linspace(0, 3 * step, 20)]), num_dashes=12)
        self.play(Create(arc), run_time=0.5); t += 0.5
        self.wait(max(d - t - 0.7, 0.2))
        self.play(FadeOut(VGroup(dl, dll, rm, ghosts, arc, L_full, L_lab)), run_time=0.7)
        self.ph = phd.get_value()
        self.Uv, self.Wv, self.K = U, W, K_save

    # ---------------- B03 — precession traces the cone ----------------
    def b03_cone(self):
        d = DURS["B03"]
        LEN = 2.5
        self.top = self.make_top()
        self.Lm = always_redraw(self.L_mob)
        self.Ll = always_redraw(self.L_label)
        self.tm = always_redraw(self.tau_mob)
        self.tl = always_redraw(self.tau_label)
        self.play(FadeIn(self.floor_m), FadeIn(self.top), FadeIn(self.g), FadeIn(self.Lm), FadeIn(self.Ll),
                  FadeIn(self.tm), FadeIn(self.tl), run_time=0.8)
        self.bring_to_front(self.vline)
        self.top.add_updater(self.top_updater)
        self.precessing = True
        # the cone: L's tip circle (revealed in step with the sweep) + two edge lines
        ph0 = self.ph
        h = LEN * np.cos(self.th)
        rr = LEN * np.sin(self.th)
        circ = DashedVMobject(VMobject(color=L_C, stroke_width=2.5).set_points_smoothly(
            [self.pr([rr * np.cos(ph0 + s), rr * np.sin(ph0 + s), h]) for s in np.linspace(0, TAU, 90)]),
            num_dashes=50)
        # silhouette edges: points of the circle at the screen-left and screen-right extremes
        ext = [self.pr([rr * np.cos(s), rr * np.sin(s), h]) for s in np.linspace(0, TAU, 360)]
        left = min(ext, key=lambda p: p[0])
        right = max(ext, key=lambda p: p[0])
        edges = VGroup(DashedLine(self.pr(np.zeros(3)), left, color=L_C, stroke_width=2, dash_length=0.1),
                       DashedLine(self.pr(np.zeros(3)), right, color=L_C, stroke_width=2, dash_length=0.1))
        edges.set_stroke(opacity=0.6)
        self.add(circ)
        self.bring_to_front(self.top, self.g, self.Lm, self.Ll, self.tm, self.tl)
        t_sweep = TAU / PREC
        self.play(Create(circ), run_time=t_sweep, rate_func=linear)
        self.play(Create(edges), run_time=0.8)
        self.bring_to_front(self.top, self.g, self.Lm, self.Ll, self.tm, self.tl)
        self.wait(max(d - 0.8 - t_sweep - 0.8, 0.2))
        self.cone = VGroup(circ, edges)

    # ---------------- B04 — summary label, precession continues ----------------
    def b04_hold(self):
        d = DURS["B04"]
        P = self.PORTRAIT
        eq = MathTex(r"\vec\tau \perp \vec L", font_size=self.MATH + 2, color=INK)
        txt = crisp_text("turns the axis, not the tilt", self.LBL + 2, color=INK, font=CAPTION_STYLE)
        if P:
            grp = VGroup(eq, txt).arrange(DOWN, buff=0.18).move_to([0, safe_half_h() - 0.5, 0])
        else:
            grp = VGroup(eq, txt).arrange(RIGHT, buff=0.35).move_to([0, safe_half_h() - 0.3, 0])
        self.play(FadeIn(grp), run_time=0.6)
        self.wait(max(d - 0.6, 0.3))
