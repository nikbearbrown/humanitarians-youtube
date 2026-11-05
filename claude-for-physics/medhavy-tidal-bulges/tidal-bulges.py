"""tidal-bulges.py — Chapter 13.6, Tidal Forces.

The Moon pulls the near side of Earth harder than the center and the far
side less. Subtracting the center's pull (Earth as a whole falls with its
center) leaves a residual toward the Moon on the near side and away from it
on the far side: two bulges along the Earth-Moon line.

Geometry is written in a frame (u toward the Moon, w perpendicular) so the
same code lays out horizontally in 16:9 and vertically in 9:16.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh tidal-bulges.py TidalBulges
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching tidal-bulges.py TidalBulges
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

DEEP = "#0072B2"     # Okabe-Ito blue (Earth's oceans)
WATER = "#56B4E9"    # Okabe-Ito sky blue (tidal water layer)
MOON = "#BDBDBD"
EPS = 0.4            # exaggerated first-order pull difference (real: ~3%)


def cues(n, d):
    return np.cumsum([0] + list(n)) / sum(n) * d


class TidalBulges(MedhavyScene):
    def construct(self):
        self.PORTRAIT = P = PORTRAIT
        if P:
            self.u, self.w = UP, RIGHT
            self.E0, self.R = np.array([0, 0.35, 0]), 0.9
            self.MD, self.MR = 2.75, 0.26
            self.A, self.BUL = 0.6, 0.3
            self.PANEL = 0.95
        else:
            self.u, self.w = LEFT, UP
            self.E0, self.R = np.array([1.2, -0.1, 0]), 1.45
            self.MD, self.MR = 6.0, 0.42
            self.A, self.BUL = 1.3, 0.45
            self.PANEL = 1.6
        self.MATH = 32 if P else 40
        self.LBL = 16 if P else 22
        self.an = ValueTracker(0.0)    # near bulge amplitude
        self.af = ValueTracker(0.0)    # far bulge amplitude
        self.spin = 0.0

        if P:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.b00_hook()
        self.b01_far_bulge()
        self.b02_three_pulls()
        self.b03_split()
        self.b04_hold()

    # ---------------- helpers ----------------
    def at(self, a, b=0.0):
        """Point a along u (toward the Moon) and b along w from Earth's center."""
        return self.E0 + a * self.u + b * self.w

    def water_mob(self):
        pts = []
        for th in np.linspace(0, TAU, 160):
            c = np.cos(th)
            rr = self.R + 0.07 + self.an.get_value() * max(c, 0) ** 2 + self.af.get_value() * max(-c, 0) ** 2
            pts.append(self.E0 + rr * (np.cos(th) * self.u + np.sin(th) * self.w))
        return Polygon(*pts[:-1], color=DEEP, stroke_width=1.5, fill_color=WATER, fill_opacity=0.6)

    def earth_mob(self, spin=0.0):
        R = self.R
        sea = Circle(radius=R, color=INK, stroke_width=2, fill_color=DEEP, fill_opacity=1)
        lands = VGroup(
            Ellipse(width=R * 0.8, height=R * 0.55, stroke_width=0, fill_color=TEAL, fill_opacity=1)
            .move_to([-R * 0.3, R * 0.35, 0]).rotate(0.5),
            Ellipse(width=R * 0.5, height=R * 0.8, stroke_width=0, fill_color=TEAL, fill_opacity=1)
            .move_to([R * 0.4, -R * 0.25, 0]).rotate(-0.3),
            Ellipse(width=R * 0.35, height=R * 0.25, stroke_width=0, fill_color=TEAL, fill_opacity=1)
            .move_to([-R * 0.35, -R * 0.5, 0]),
        )
        lands.rotate(spin, about_point=ORIGIN)
        return VGroup(sea, lands).move_to(self.E0)

    def moon_mob(self):
        r = self.MR
        body = Circle(radius=r, color=INK, stroke_width=2, fill_color=MOON, fill_opacity=1)
        craters = VGroup(*[Circle(radius=r * s, stroke_width=0, fill_color="#9E9E9E", fill_opacity=1).move_to([r * x, r * y, 0])
                           for s, x, y in [(0.22, -0.3, 0.3), (0.15, 0.35, 0.1), (0.18, 0.0, -0.45)]])
        return VGroup(body, craters).move_to(self.at(self.MD))

    def pull_arrow(self, start, length, color, sw=6, direction=None):
        d = self.u if direction is None else direction
        return Arrow(start, start + d * length, buff=0, color=color, stroke_width=sw, tip_length=0.2,
                     max_tip_length_to_length_ratio=0.3)

    # ---------------- B00 — near bulge toward the Moon ----------------
    def b00_hook(self):
        d = DURS["B00"]
        c = cues([17, 4, 8], d)
        P = self.PORTRAIT
        self.water = always_redraw(self.water_mob)
        self.earth = self.earth_mob()
        self.moon = self.moon_mob()
        t = 0.0
        self.play(FadeIn(self.water), FadeIn(self.earth), FadeIn(self.moon), run_time=1.0); t += 1.0
        start = self.at(self.R + 0.07 + self.BUL + 0.12)
        glen = (self.MD - self.MR - 0.15) - (self.R + 0.07 + self.BUL + 0.12)
        self.g_arrow = self.pull_arrow(start, glen, INK)
        txt = "Moon's\ngravity" if P else "Moon's gravity"
        self.g_lab = crisp_text(txt, self.LBL, color=INK, font=CAPTION_STYLE, line_spacing=1.0)
        self.g_lab.move_to(self.g_arrow.get_center() + self.w * (0.75 if P else 0.4))
        self.play(GrowArrow(self.g_arrow), FadeIn(self.g_lab), run_time=0.8); t += 0.8
        self.play(self.an.animate.set_value(self.BUL), run_time=2.0); t += 2.0
        self.wait(max(c[2] - t, 0.2)); t = max(c[2], t + 0.2)
        far_pt = self.at(-(self.R + 0.07))
        self.spot = Circle(radius=0.3 if P else 0.45, color=CRIMSON, stroke_width=4).move_to(far_pt)
        self.play(Create(self.spot), run_time=0.7); t += 0.7
        self.wait(max(d - t, 0.2))

    # ---------------- B01 — the far bulge, and the question ----------------
    def b01_far_bulge(self):
        d = DURS["B01"]
        c = cues([14, 21], d)
        P = self.PORTRAIT
        t = 0.0
        self.play(FadeOut(self.spot), self.af.animate.set_value(self.BUL), run_time=2.0); t += 2.0
        self.wait(max(c[1] - t, 0.2)); t = max(c[1], t + 0.2)
        self.q = Text("?", font_size=64 if P else 80, color=CRIMSON, weight=BOLD).move_to(
            self.at(-(self.R + self.BUL + 0.2), self.R * 0.9 + 0.2))
        self.play(FadeIn(self.q, scale=1.5), run_time=0.6); t += 0.6
        self.wait(max(d - t, 0.2))

    # ---------------- B02 — three pulls along the diameter ----------------
    def b02_three_pulls(self):
        d = DURS["B02"]
        c = cues([4, 25, 10, 10], d)
        R, A = self.R, self.A
        outline = Circle(radius=R, color=SLATE, stroke_width=2.5).move_to(self.E0)
        diam = DashedLine(self.at(R + 0.3), self.at(-R - 0.3), color=SLATE, stroke_width=2, dash_length=0.1)
        pts = [self.at(R), self.at(0), self.at(-R)]
        dots = VGroup(*[Dot(p, radius=0.06, color=INK) for p in pts])
        self.near_a = self.pull_arrow(pts[0], A * (1 + EPS), INK)
        self.cent_a = self.pull_arrow(pts[1], A, SLATE)
        self.far_a = self.pull_arrow(pts[2], A * (1 - EPS), INK)
        t = 0.0
        self.play(FadeOut(self.water), FadeOut(self.earth), FadeOut(self.q), FadeOut(self.g_arrow),
                  FadeOut(self.g_lab), FadeIn(outline), run_time=1.0); t += 1.0
        self.play(Create(diam), FadeIn(dots), run_time=0.8); t += 0.8
        span = c[2] - c[1]
        self.wait(max(c[1] + span * 0.55 - t, 0.2)); t = max(c[1] + span * 0.55, t + 0.2)
        for a in (self.near_a, self.cent_a, self.far_a):
            self.play(GrowArrow(a), run_time=0.6); t += 0.6
            self.wait(span * 0.12); t += span * 0.12
        self.wait(max(c[2] - t, 0.2)); t = max(c[2], t + 0.2)
        self.play(Indicate(self.near_a, color=INK, scale_factor=1.15), run_time=1.0); t += 1.0
        self.wait(max(c[3] - t, 0.2)); t = max(c[3], t + 0.2)
        self.play(Indicate(self.cent_a, color=SLATE, scale_factor=1.15), run_time=0.8); t += 0.8
        self.play(Indicate(self.far_a, color=INK, scale_factor=1.15), run_time=0.8); t += 0.8
        self.wait(max(d - t, 0.2))
        self.outline, self.diam, self.dots = outline, diam, dots

    # ---------------- B03 — split: subtract the center's pull ----------------
    def b03_split(self):
        d = DURS["B03"]
        c = cues([22, 10, 10, 9], d)
        P = self.PORTRAIT
        A = self.A * (1.4 if P else 1.75)     # panels are a zoomed view
        L = self.LBL - 2
        if P:
            off, side = 0.22, RIGHT
            o_near, o_far = np.array([-self.PANEL, -1.4, 0]), np.array([self.PANEL, -1.4, 0])
            divider = Line([0, -2.1, 0], [0, 0.7, 0], color=SLATE, stroke_width=2)
        else:
            off, side = 0.3, UP
            o_near, o_far = np.array([2.4, 1.55, 0]), np.array([2.4, -1.75, 0])
            divider = Line([-3.6, -0.1, 0], [4.2, -0.1, 0], color=SLATE, stroke_width=2)
        n_pull = self.pull_arrow(o_near + side * off, A * (1 + EPS), INK)
        n_cent = self.pull_arrow(o_near - side * off, A, SLATE)
        f_cent = self.pull_arrow(o_far + side * off, A, SLATE)
        f_pull = self.pull_arrow(o_far - side * off, A * (1 - EPS), INK)
        n_diff = self.pull_arrow(o_near, A * EPS, TEAL, sw=8)
        f_diff = self.pull_arrow(o_far, A * EPS, TEAL, sw=8, direction=-self.u)
        n_dot, f_dot = Dot(o_near, radius=0.06, color=INK), Dot(o_far, radius=0.06, color=INK)

        def lab(text, color, size=L):
            return crisp_text(text, size, color=color, font=CAPTION_STYLE)

        l_np, l_nc = lab("near", INK), lab("center", SLATE)
        l_fc, l_fp = lab("center", SLATE), lab("far", INK)
        l_nd, l_fd = lab("difference", TEAL), lab("difference", TEAL)
        t_near, t_far = lab("near side", INK, self.LBL), lab("far side", INK, self.LBL)
        if P:
            # arrows vertical (Moon at top): labels above tips, titles above panels
            for lb, ar in ((l_np, n_pull), (l_nc, n_cent), (l_fc, f_cent), (l_fp, f_pull)):
                lb.next_to(ar.get_end(), UP, buff=0.08)
            l_nd.next_to(n_dot, DOWN, buff=0.12)
            l_fd.next_to(f_diff.get_end(), DOWN, buff=0.1)
            t_near.move_to([o_near[0], 0.45, 0])
            t_far.move_to([o_far[0], 0.45, 0])
        else:
            # arrows horizontal (Moon at left): labels above/below tips, titles at far left
            l_np.next_to(n_pull.get_end(), UP, buff=0.14)
            l_nc.next_to(n_cent.get_end(), DOWN, buff=0.14)
            l_fc.next_to(f_cent.get_end(), UP, buff=0.14)
            l_fp.next_to(f_pull.get_end(), DOWN, buff=0.14)
            l_nd.next_to(n_dot, RIGHT, buff=0.2)
            l_fd.next_to(f_diff.get_end(), RIGHT, buff=0.15)
            t_near.move_to([-3.0, o_near[1], 0])
            t_far.move_to([-3.0, o_far[1], 0])

        t = 0.0
        cent_copy = self.cent_a.copy()
        self.play(FadeOut(self.outline), FadeOut(self.diam), FadeOut(self.dots), Create(divider),
                  ReplacementTransform(self.near_a, n_pull), ReplacementTransform(self.cent_a, n_cent),
                  ReplacementTransform(cent_copy, f_cent), ReplacementTransform(self.far_a, f_pull),
                  run_time=1.5); t += 1.5
        self.play(FadeIn(n_dot), FadeIn(f_dot), FadeIn(t_near), FadeIn(t_far),
                  FadeIn(l_np), FadeIn(l_nc), FadeIn(l_fc), FadeIn(l_fp), run_time=0.8); t += 0.8
        self.wait(max(c[1] - t, 0.2)); t = max(c[1], t + 0.2)
        self.play(GrowArrow(n_diff), FadeIn(l_nd), run_time=0.8); t += 0.8
        self.wait(max(c[2] - t, 0.2)); t = max(c[2], t + 0.2)
        self.play(GrowArrow(f_diff), FadeIn(l_fd), run_time=0.8); t += 0.8
        self.wait(max(c[3] - t, 0.2)); t = max(c[3], t + 0.2)
        # recombine onto Earth: the two differences move to the near and far points
        outline = Circle(radius=self.R, color=SLATE, stroke_width=2.5).move_to(self.E0)
        tn = self.pull_arrow(self.at(self.R + 0.1), self.A * EPS, TEAL, sw=8)
        tf = self.pull_arrow(self.at(-self.R - 0.1), self.A * EPS, TEAL, sw=8, direction=-self.u)
        self.play(FadeOut(VGroup(n_pull, n_cent, f_cent, f_pull, n_dot, f_dot, t_near, t_far,
                                 l_np, l_nc, l_fc, l_fp, l_nd, l_fd, divider)),
                  FadeIn(outline), ReplacementTransform(n_diff, tn), ReplacementTransform(f_diff, tf),
                  run_time=1.5); t += 1.5
        self.wait(max(d - t, 0.2))
        self.outline, self.tn, self.tf = outline, tn, tf

    # ---------------- B04 — two bulges, Earth turns beneath them ----------------
    def b04_hold(self):
        d = DURS["B04"]
        P = self.PORTRAIT
        big = self.BUL * 1.25
        self.an.set_value(self.BUL)
        self.af.set_value(self.BUL)
        water = always_redraw(self.water_mob)
        earth = self.earth_mob()
        tn_end = self.pull_arrow(self.at(self.R + 0.07 + big + 0.08), self.A * EPS, TEAL, sw=8)
        tf_end = self.pull_arrow(self.at(-(self.R + 0.07 + big + 0.08)), self.A * EPS, TEAL, sw=8, direction=-self.u)
        label = crisp_text("tidal force = difference in pull", self.LBL + (0 if P else 2), color=TEAL, font=CAPTION_STYLE)
        label.move_to([0, -1.55, 0] if P else [self.E0[0], -2.6, 0])
        if label.width > 2 * safe_half_w():
            label.scale_to_fit_width(2 * safe_half_w())
        self.play(FadeOut(self.outline), FadeIn(water), FadeIn(earth), run_time=1.0)
        self.bring_to_front(self.tn, self.tf)
        self.play(self.an.animate.set_value(big), self.af.animate.set_value(big),
                  Transform(self.tn, tn_end), Transform(self.tf, tf_end), run_time=1.5)
        self.play(FadeIn(label), run_time=0.6)

        def spin_upd(m, dt):
            self.spin += 0.35 * dt
            m.become(self.earth_mob(self.spin))
        earth.add_updater(spin_upd)
        self.wait(max(d - 3.1, 0.3))
        earth.clear_updaters()
