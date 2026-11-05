"""sonic-boom.py — Chapter 17, Shock Waves.

A plane accelerates continuously from M = 0.5 through M = 1 to M = 1.5.
Drawn in the plane's frame: the plane stays put while the air (and every
wavefront centre) streams backward at v_s. Ring k, emitted at t_k, is
centred v_s-integrated distance behind the nose, radius v (t - t_k). At
M = 1 every front touches the nose (the wall); for M > 1 the fronts are
tangent to two lines at half angle theta, sin(theta) = v/v_s = 1/M — the
cone is drawn from that formula and visibly matches the rings. The cone's
ground intersection sweeps forward; each listener hears the boom only when
it reaches them, after the plane has passed overhead.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh sonic-boom.py SonicBoom
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching sonic-boom.py SonicBoom
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

DT_EMIT = 0.4
RING_SAMPLES = 160
_UNIT = np.stack([np.cos(np.linspace(0, TAU, RING_SAMPLES + 1)),
                  np.sin(np.linspace(0, TAU, RING_SAMPLES + 1))], axis=1)
PLANE_FILL = "#B9C0C8"


def smooth01(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def make_plane(s):
    """Side view, nose at the origin, pointing +x."""
    def P(pts, fill, sw=2):
        return Polygon(*[[x * s, y * s, 0] for x, y in pts], color=INK, stroke_width=sw,
                       fill_color=fill, fill_opacity=1)
    fus = P([(0, 0), (-0.28, 0.1), (-1.1, 0.1), (-1.22, 0.06), (-1.22, -0.05), (-1.1, -0.08), (-0.28, -0.08)],
            PLANE_FILL)
    fin = P([(-0.92, 0.1), (-1.12, 0.4), (-1.22, 0.4), (-1.16, 0.1)], PLANE_FILL)
    wing = P([(-0.45, -0.02), (-0.82, -0.02), (-0.98, -0.24), (-0.84, -0.24)], "#8E969F")
    canopy = P([(-0.2, 0.07), (-0.3, 0.15), (-0.46, 0.15), (-0.46, 0.09)], "#9EC9E2", sw=1.5)
    return VGroup(fin, fus, wing, canopy)


def make_person(s, color=INK):
    head = Circle(radius=0.09 * s, color=color, stroke_width=3).move_to([0, 0.74 * s, 0])
    neck, hip = np.array([0, 0.65 * s, 0]), np.array([0, 0.34 * s, 0])
    return VGroup(head, Line(neck, hip, color=color, stroke_width=3),
                  Line(hip, [-0.11 * s, 0, 0], color=color, stroke_width=3),
                  Line(hip, [0.11 * s, 0, 0], color=color, stroke_width=3),
                  Line(neck + DOWN * 0.07 * s, [-0.15 * s, 0.38 * s, 0], color=color, stroke_width=3),
                  Line(neck + DOWN * 0.07 * s, [0.15 * s, 0.38 * s, 0], color=color, stroke_width=3))


class SonicBoom(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if PORTRAIT:
            self.S = 0.55
            self.XP, self.YP, self.YG = 1.1, 0.5, -1.6
            self.CLIP = (-safe_half_w(), safe_half_w(), -2.3, 2.0)  # top kept clear for text
            self.SPACING = 2.2
        else:
            self.S = 1.0
            self.XP, self.YP, self.YG = 3.5, 0.6, -2.5
            self.CLIP = (-safe_half_w(), safe_half_w(), -safe_half_h(), 2.25)  # top kept clear for text
            self.SPACING = 4.0
        self.V = 1.0 * self.S

        self.ticker = Mobject()
        self.ticker.add_updater(lambda m, dt: None)
        self.add(self.ticker)

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.T0 = self.time
        self.build_schedule()
        self.clip_bottom = self.CLIP[2]

        self.b00_hook()
        self.b01_mach1()
        self.b02_cone()
        self.b03_ground()
        self.b04_hold()

    # ---------------- kinematics ----------------
    def build_schedule(self):
        d = [DURS[k] for k in ("B00", "B01", "B02", "B03", "B04")]
        self.b_start = np.cumsum([0] + d)  # relative to T0
        total = self.b_start[-1] + 1.0
        tg = np.arange(0, total, 1 / 240)
        M = np.empty_like(tg)
        for i, t in enumerate(tg):
            if t < self.b_start[1]:
                M[i] = 0.5 + 0.45 * smooth01(t / (0.85 * d[0]))
            elif t < self.b_start[2]:
                M[i] = 0.95 + 0.05 * np.clip((t - self.b_start[1]) / 2.5, 0, 1)
            elif t < self.b_start[3]:
                M[i] = 1.0 + 0.5 * smooth01((t - self.b_start[2]) / 5.0)
            else:
                M[i] = 1.5
        X = np.concatenate([[0], np.cumsum(0.5 * (M[1:] + M[:-1]) * np.diff(tg))]) * self.V
        self.tg, self.Mg, self.Xg = tg, M, X

    def rel(self):
        return self.time - self.T0

    def mach(self, t=None):
        return float(np.interp(self.rel() if t is None else t, self.tg, self.Mg))

    def xair(self, t):
        return np.interp(t, self.tg, self.Xg)

    # ---------------- drawing helpers ----------------
    def ring_points(self):
        t = self.rel()
        n = int(np.floor(t / DT_EMIT)) + 1
        tk = np.arange(n) * DT_EMIT
        tk = tk[t - tk < 16.0]
        cx = self.XP - (self.xair(t) - self.xair(tk))
        r = self.V * (t - tk)
        x0, x1, y0, y1 = self.CLIP[0], self.CLIP[1], self.clip_bottom, self.CLIP[3]
        segs = []
        for c, rr in zip(cx, r):
            if rr < 0.02:
                continue
            pts = np.array([c, self.YP]) + rr * _UNIT
            inside = (pts[:, 0] > x0) & (pts[:, 0] < x1) & (pts[:, 1] > y0) & (pts[:, 1] < y1)
            ok = inside[:-1] & inside[1:]
            if not ok.any():
                continue
            a = np.column_stack([pts[:-1][ok], np.zeros(ok.sum())])
            b = np.column_stack([pts[1:][ok], np.zeros(ok.sum())])
            segs.append(np.stack([a, a + (b - a) / 3, a + 2 * (b - a) / 3, b], axis=1))
        if not segs:
            return np.zeros((0, 3))
        return np.concatenate(segs).reshape(-1, 3)

    def clip_len(self, d):
        """Distance from the nose along unit direction d to the clip boundary."""
        x0, x1, y0, y1 = self.CLIP[0], self.CLIP[1], self.clip_bottom, self.CLIP[3]
        ts = []
        if d[0] < -1e-9:
            ts.append((x0 - self.XP) / d[0])
        if d[0] > 1e-9:
            ts.append((x1 - self.XP) / d[0])
        if d[1] < -1e-9:
            ts.append((y0 - self.YP) / d[1])
        if d[1] > 1e-9:
            ts.append((y1 - self.YP) / d[1])
        return min(ts) if ts else 10.0

    def backed(self, mob, buff=0.12):
        bg = SurroundingRectangle(mob, buff=buff, stroke_width=0, fill_color=CREAM, fill_opacity=0.92)
        return VGroup(bg, mob)

    # ---------------- B00 — subsonic, formula blows up ----------------
    def b00_hook(self):
        S = self.S
        self.plane = make_plane(S).shift([self.XP, self.YP, 0])
        self.op_r = ValueTracker(0.0)
        self.rings = VMobject()

        def ring_upd(m):
            m.set_points(self.ring_points())
            m.set_stroke(TEAL, width=3, opacity=self.op_r.get_value())
            m.set_fill(opacity=0)
        ring_upd(self.rings)
        self.rings.add_updater(ring_upd)

        fs = 30 if self.PORTRAIT else 40
        f = MathTex(r"f_o = f_s\,\frac{v}{v - v_s} = \frac{f_s}{1 - M}", color=INK, font_size=fs)
        if f.width > 2 * safe_half_w() - 0.3:
            f.scale_to_fit_width(2 * safe_half_w() - 0.3)
        f_pos = [0, 2.95, 0] if self.PORTRAIT else [-3.3, 2.85, 0]
        self.formula = self.backed(f.move_to(f_pos))

        # live readouts (digits cached as crisp text)
        cache = {}

        def num(sv, color=INK):
            if (sv, color) not in cache:
                cache[(sv, color)] = crisp_text(sv, 18 if self.PORTRAIT else 26, color=color, font=CAPTION_STYLE)
            return cache[(sv, color)].copy()

        rfs = 28 if self.PORTRAIT else 38
        self.m_lhs = MathTex(r"M =", color=INK, font_size=rfs)
        self.f_lhs = MathTex(r"f_o \approx", color=INK, font_size=rfs)
        self.f_rhs = MathTex(r"f_s", color=INK, font_size=rfs)
        self.inf = MathTex(r"\to \infty", color=CRIMSON, font_size=rfs + 6)
        if self.PORTRAIT:
            self.m_pos, self.f_pos = np.array([-0.85, 2.3, 0]), np.array([0.75, 2.3, 0])
        else:
            self.m_pos, self.f_pos = np.array([2.3, 2.85, 0]), np.array([4.9, 2.85, 0])

        self.m_read = VGroup()

        def m_upd(m):
            g = VGroup(self.m_lhs.copy(), num(f"{self.mach():.2f}")).arrange(RIGHT, buff=0.12)
            m.become(self.backed(g.move_to(self.m_pos), buff=0.08))
        m_upd(self.m_read)
        self.m_read.add_updater(m_upd)

        self.f_read = VGroup()

        def f_upd(m):
            M = self.mach()
            if M >= 0.985:
                g = VGroup(MathTex(r"f_o", color=INK, font_size=rfs), self.inf.copy()).arrange(RIGHT, buff=0.12)
            else:
                g = VGroup(self.f_lhs.copy(), num(f"{1 / (1 - M):.1f}"), self.f_rhs.copy()).arrange(RIGHT, buff=0.1)
            m.become(self.backed(g.move_to(self.f_pos), buff=0.08))
        f_upd(self.f_read)
        self.f_read.add_updater(f_upd)

        self.add(self.rings)
        self.play(FadeIn(self.plane), self.op_r.animate.set_value(1.0), run_time=1.0)
        self.play(FadeIn(self.formula), run_time=0.8)
        self.play(FadeIn(self.m_read), FadeIn(self.f_read), run_time=0.6)
        self.bring_to_front(self.plane)
        self.wait(max(DURS["B00"] - 2.4, 0.3))

    # ---------------- B01 — Mach 1: the wall ----------------
    def b01_mach1(self):
        self.op_c = ValueTracker(0.0)
        self.cone = VGroup(VMobject(), VMobject())
        self.lower_end = None

        def cone_upd(g):
            t = self.rel()
            M = max(self.mach(), 1.0)
            th = np.arcsin(1.0 / M)
            oldest = min(t, 16.0)
            L_want = max(1.5 * self.S, self.V * oldest * np.sqrt(M * M - 1))
            pts_all = []
            for sgn in (1, -1):
                d = np.array([-np.cos(th), sgn * np.sin(th)])
                L = min(L_want, self.clip_len(d))
                end = np.array([self.XP, self.YP]) + L * d
                a = np.array([self.XP, self.YP, 0])
                b = np.array([end[0], end[1], 0])
                pts_all.append(np.array([a, a + (b - a) / 3, a + 2 * (b - a) / 3, b]))
            pts = np.concatenate(pts_all)
            under, top = g
            op = self.op_c.get_value()
            under.set_points(pts)
            under.set_stroke(INK, width=10, opacity=op)
            top.set_points(pts)
            top.set_stroke(GOLD, width=6, opacity=op)
            under.set_fill(opacity=0)
            top.set_fill(opacity=0)
        cone_upd(self.cone)
        self.cone.add_updater(cone_upd)
        self.add(self.cone)
        self.bring_to_front(self.plane)

        # cone appears as M reaches 1 (2.5 s into the beat)
        self.wait(2.0)
        self.play(self.op_c.animate.set_value(1.0), run_time=1.0)
        self.wait(max(DURS["B01"] - 3.0, 0.3))

    # ---------------- B02 — Mach 1.5: the cone ----------------
    def b02_cone(self):
        S = self.S
        self.play(FadeOut(self.formula), FadeOut(self.f_read), run_time=0.6)
        self.f_read.clear_updaters()
        self.wait(4.6)  # M ramps 1.0 -> 1.5 over the first 5 s of this beat

        th = np.arcsin(1 / 1.5)
        r_arc = 1.5 * S  # larger than the fuselage so the arc never crosses the plane
        self.arc = Arc(radius=r_arc, start_angle=PI - th, angle=th, arc_center=[self.XP, self.YP, 0],
                       color=INK, stroke_width=3)
        self.th_lab = MathTex(r"\theta", color=INK, font_size=30 if self.PORTRAIT else 40)
        self.th_lab.move_to(np.array([self.XP, self.YP, 0]) + (r_arc + 0.28 * max(S, 0.8)) *
                            np.array([np.cos(PI - th / 2), np.sin(PI - th / 2), 0]))
        fs = 30 if self.PORTRAIT else 40
        sf = MathTex(r"\sin\theta = \frac{v}{v_s} = \frac{1}{M}", color=INK, font_size=fs)
        sub = MathTex(r"M = 1.5:\ \theta \approx 42^\circ", color=SLATE, font_size=fs - 6)
        grp = VGroup(sf, sub).arrange(DOWN, buff=0.15) if self.PORTRAIT else VGroup(sf, sub).arrange(RIGHT, buff=0.6)
        if grp.width > 2 * safe_half_w() - 0.3:
            grp.scale_to_fit_width(2 * safe_half_w() - 0.3)
        grp.move_to([0, 2.8, 0] if self.PORTRAIT else [-2.6, 2.85, 0])
        self.sin_f = self.backed(grp)
        self.play(Create(self.arc), FadeIn(self.th_lab), run_time=0.8)
        if self.PORTRAIT:
            # narrow frame: the formula block needs the readout's row; M = 1.5 is in its sub-line
            self.play(FadeIn(self.sin_f), FadeOut(self.m_read), run_time=0.8)
            self.m_read.clear_updaters()
        else:
            self.play(FadeIn(self.sin_f), run_time=0.8)
        self.wait(max(DURS["B02"] - 6.8, 0.3))

    # ---------------- B03 — the boom sweeps the ground ----------------
    def b03_ground(self):
        S = self.S
        outs = [FadeOut(self.sin_f), FadeOut(self.arc), FadeOut(self.th_lab)]
        if not self.PORTRAIT:
            outs.append(FadeOut(self.m_read))
        self.play(*outs, self.op_r.animate.set_value(0.45), run_time=0.8)
        self.m_read.clear_updaters()
        self.ground = Line([self.CLIP[0], self.YG, 0], [self.CLIP[1], self.YG, 0], color=SLATE, stroke_width=4)
        self.play(Create(self.ground), run_time=0.8)
        self.clip_bottom = self.YG

        th = np.arcsin(1 / 1.5)
        self.x_cross = self.XP - (self.YP - self.YG) / np.tan(th)
        t3 = self.rel()
        n = 4
        wrap = n * self.SPACING
        speed = 1.5 * self.V
        x_spawn = self.CLIP[1] + 0.4
        self.people = VGroup(*[make_person(S) for _ in range(n)])
        self.bursts = VGroup(*[Star(n=8, outer_radius=0.32 * S, inner_radius=0.15 * S, color=CRIMSON,
                                    fill_color=CRIMSON, fill_opacity=1, stroke_width=0) for _ in range(n)])
        self.boom_labs = VGroup(*[crisp_text("boom", 14 if self.PORTRAIT else 20, color=CRIMSON,
                                             font=CAPTION_STYLE, weight=BOLD) for _ in range(n)])
        burst_window = speed * 1.0
        self.op_p = ValueTracker(0.0)

        def people_upd(g):
            tau = self.rel() - t3
            op = self.op_p.get_value()
            for i, (p, b, lb) in enumerate(zip(g, self.bursts, self.boom_labs)):
                x = x_spawn - ((speed * tau + i * self.SPACING) % wrap)
                p.move_to([x, self.YG, 0], aligned_edge=DOWN)
                vis = self.CLIP[0] + 0.2 < x < self.CLIP[1] - 0.2
                p.set_stroke(opacity=op if vis else 0)
                past = self.x_cross - x
                if vis and 0 <= past <= burst_window:
                    k = 1 - past / burst_window
                    b.move_to([x, self.YG + 0.75 * S, 0])
                    b.set_fill(CRIMSON, opacity=op * min(1.0, 3 * k))
                    lb.next_to(b, UP, buff=0.08)
                    lb.set_opacity(op * min(1.0, 3 * k))
                else:
                    b.set_fill(opacity=0)
                    lb.set_opacity(0)
        people_upd(self.people)
        self.people.add_updater(people_upd)
        self.add(self.people, self.bursts, self.boom_labs)

        self.track = DashedLine([self.XP - 0.35 * S, self.YP - 0.15 * S, 0], [self.XP - 0.35 * S, self.YG, 0],
                                color=SLATE, stroke_width=2, dash_length=0.1)
        self.track_lab = crisp_text("below the plane", 12 if self.PORTRAIT else 16, color=SLATE, font=CAPTION_STYLE)
        self.track_lab.next_to(self.track, DOWN, buff=0.12)
        if self.track_lab.get_right()[0] > safe_half_w():
            self.track_lab.shift(LEFT * (self.track_lab.get_right()[0] - safe_half_w()))
        self.bring_to_front(self.cone, self.plane)
        self.play(self.op_p.animate.set_value(1.0), Create(self.track), FadeIn(self.track_lab), run_time=0.8)
        self.wait(max(DURS["B03"] - 2.4, 0.3))

    # ---------------- B04 — summary ----------------
    def b04_hold(self):
        fs = 22 if not self.PORTRAIT else 15
        inf = MathTex(r"\infty", color=CRIMSON, font_size=56 if not self.PORTRAIT else 40)
        strike = Line(inf.get_corner(DL) + [-0.05, -0.05, 0], inf.get_corner(UR) + [0.05, 0.05, 0],
                      color=INK, stroke_width=4)
        crossed = VGroup(inf, strike)
        txt = ("NOT AN INFINITE PITCH:\nONE SHOCK FRONT" if self.PORTRAIT
               else "NOT AN INFINITE PITCH: ONE SHOCK FRONT")
        t = crisp_text(txt, fs, color=INK, font=CAPTION_STYLE, weight=BOLD, line_spacing=1.05)
        g = VGroup(crossed, t).arrange(RIGHT, buff=0.3)
        if g.width > 2 * safe_half_w():
            g.scale_to_fit_width(2 * safe_half_w())
        g.move_to([0, 2.8 if self.PORTRAIT else 2.9, 0])
        self.summary = self.backed(g)
        self.play(FadeIn(self.summary), run_time=0.8)
        self.wait(max(DURS["B04"] - 0.8, 0.3))
