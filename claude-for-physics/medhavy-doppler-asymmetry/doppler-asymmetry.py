"""doppler-asymmetry.py — Chapter 17, The Doppler Effect.

Same relative speed, two different physical mechanisms. A moving source
emits each wavefront from a new position, so the wavelength in the air is
shorter ahead of it (f_o = f_s v/(v - v_s)). A moving observer meets the
unchanged, evenly spaced wavefronts more often (f_o = f_s (v + v_o)/v).
With v = 340 m/s, f_s = 500 Hz, 30 m/s: 548 Hz vs 544 Hz.

Both panels are simulated in the air's rest frame: every ring is centred
where the siren was when it was emitted and grows at the wave speed; ring
arcs are clipped to their panel. Episodes of length P loop with a short fade.
The running-listener counter is the true number of rings that have reached
the listener's ear. Displayed speeds are exaggerated (v_s = 0.4 v); stated
on screen.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh doppler-asymmetry.py DopplerAsymmetry
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching doppler-asymmetry.py DopplerAsymmetry
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

P = 10.0          # episode length (s)
DT_EMIT = 0.5     # emission interval (s) -> 2 rings per second
FADE = 0.4
PAST_S = 9.0     # seconds of emission history before each episode
RING_SAMPLES = 160
_UNIT = np.stack([np.cos(np.linspace(0, TAU, RING_SAMPLES + 1)),
                  np.sin(np.linspace(0, TAU, RING_SAMPLES + 1))], axis=1)


def make_ambulance(s):
    """Side view, facing right: white box body, red stripe + cross, cab, light bar, wheels."""
    body = Rectangle(width=0.72 * s, height=0.42 * s, color=INK, stroke_width=2.5,
                     fill_color=WHITE, fill_opacity=1)
    cab = Polygon([0, 0, 0], [0.28 * s, 0, 0], [0.28 * s, 0.2 * s, 0], [0.12 * s, 0.32 * s, 0], [0, 0.32 * s, 0],
                  color=INK, stroke_width=2.5, fill_color=WHITE, fill_opacity=1)
    cab.next_to(body, RIGHT, buff=0).align_to(body, DOWN)
    window = Polygon([0.03 * s, 0.17 * s, 0], [0.14 * s, 0.17 * s, 0], [0.14 * s, 0.28 * s, 0], [0.03 * s, 0.28 * s, 0],
                     color=INK, stroke_width=1.2, fill_color="#9EC9E2", fill_opacity=1)
    window.move_to(cab.get_corner(UL) + np.array([0.09 * s, -0.09 * s, 0]))
    stripe = Rectangle(width=1.0 * s, height=0.06 * s, stroke_width=0, fill_color=CRIMSON, fill_opacity=1)
    stripe.move_to(VGroup(body, cab).get_bottom() + UP * 0.12 * s)
    cross_v = Rectangle(width=0.06 * s, height=0.2 * s, stroke_width=0, fill_color=CRIMSON, fill_opacity=1)
    cross_h = Rectangle(width=0.2 * s, height=0.06 * s, stroke_width=0, fill_color=CRIMSON, fill_opacity=1)
    cross = VGroup(cross_v, cross_h).move_to(body.get_center() + UP * 0.07 * s)
    light = Rectangle(width=0.16 * s, height=0.07 * s, stroke_width=1.2, color=INK,
                      fill_color=CRIMSON, fill_opacity=1).next_to(body, UP, buff=0)
    light.align_to(body, RIGHT).shift(LEFT * 0.08 * s)
    w1 = Circle(radius=0.085 * s, color=INK, fill_color=INK, fill_opacity=1, stroke_width=1)
    w2 = w1.copy()
    w1.move_to(body.get_corner(DL) + np.array([0.17 * s, 0, 0]))
    w2.move_to(cab.get_bottom())
    g = VGroup(body, cab, window, stripe, cross, light, w1, w2)
    return g


def make_person(s, color, phase=None):
    """Stick figure; feet at origin. phase=None -> standing, else running pose."""
    head = Circle(radius=0.1 * s, color=color, stroke_width=3).move_to([0, 0.82 * s, 0])
    neck = np.array([0, 0.72 * s, 0])
    hip = np.array([0, 0.38 * s, 0])
    torso = Line(neck, hip, color=color, stroke_width=3)
    if phase is None:
        legs = VGroup(Line(hip, [-0.12 * s, 0, 0], color=color, stroke_width=3),
                      Line(hip, [0.12 * s, 0, 0], color=color, stroke_width=3))
        arms = VGroup(Line(neck + DOWN * 0.08 * s, [-0.16 * s, 0.42 * s, 0], color=color, stroke_width=3),
                      Line(neck + DOWN * 0.08 * s, [0.16 * s, 0.42 * s, 0], color=color, stroke_width=3))
    else:
        a = 0.2 * s * np.sin(phase)
        legs = VGroup(Line(hip, [a, 0, 0], color=color, stroke_width=3),
                      Line(hip, [-a, 0, 0], color=color, stroke_width=3))
        arms = VGroup(Line(neck + DOWN * 0.08 * s, [-0.8 * a, 0.45 * s, 0], color=color, stroke_width=3),
                      Line(neck + DOWN * 0.08 * s, [0.8 * a, 0.45 * s, 0], color=color, stroke_width=3))
    return VGroup(head, torso, legs, arms)


class DopplerAsymmetry(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if PORTRAIT:
            S = 0.55
            self.S = S
            # panel A (moving source) on top, panel B (moving observer) below
            self.A_rect = (-1.72, 1.72, 0.75, 2.75)    # x0, x1, ground y, clip top
            self.B_rect = (-1.72, 1.72, -2.15, -0.45)
            self.A_title_y, self.B_title_y = 3.15, -0.05
            self.FS = 15
            self.SMALL = 11
        else:
            S = 1.0
            self.S = S
            self.A_rect = (-6.5, -0.25, -1.6, 2.45)
            self.B_rect = (0.25, 6.5, -1.6, 2.45)
            self.A_title_y = self.B_title_y = 3.0
            self.FS = 24
            self.SMALL = 15
        self.V = 1.0 * S          # wave speed (screen units / s)
        self.VS = 0.4 * self.V    # source / observer speed (exaggerated ratio)
        self.SIREN_H = 0.55 * S   # siren height above ground (light bar)
        self.EAR_H = 0.8 * S

        self.ticker = Mobject()
        self.ticker.add_updater(lambda m, dt: None)
        self.add(self.ticker)

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.T0 = self.time
        self.b00_hook()
        self.b01_moving_source()
        self.b02_moving_observer()
        self.b03_formulas()
        self.b04_hold()

    # ---------------- simulation helpers ----------------
    def ep(self):
        return (self.time - self.T0) % P

    def ep_fade(self):
        e = self.ep()
        return float(np.clip(e / FADE, 0, 1) * np.clip((P - e) / FADE, 0, 1))

    def a_src_x(self, e):
        x0 = self.A_rect[0] + 0.6 * self.S
        return x0 + self.VS * e

    def a_listener_x(self):
        return self.A_rect[1] - 0.45 * self.S

    def b_src_x(self):
        return self.B_rect[0] + 0.85 * self.S

    def b_runner_x(self, e):
        return self.B_rect[1] - 0.8 * self.S - self.VS * e

    def b_stander_x(self):
        return self.B_rect[1] - 0.25 * self.S

    def emitted(self, e):
        """Emission times t_k = k*DT_EMIT <= e, including PAST_S seconds before
        the episode began, so each episode opens on an established wave field."""
        k0 = -int(PAST_S / DT_EMIT)
        n = int(np.floor(e / DT_EMIT))
        return np.arange(k0, n + 1) * DT_EMIT

    def ring_points(self, centers, radii, rect):
        x0, x1, yg, ytop = rect
        segs = []
        for c, r in zip(centers, radii):
            if r < 0.02:
                continue
            pts = c[None, :2] + r * _UNIT
            inside = (pts[:, 0] > x0 + 0.03) & (pts[:, 0] < x1 - 0.03) & (pts[:, 1] > yg) & (pts[:, 1] < ytop)
            ok = inside[:-1] & inside[1:]
            if not ok.any():
                continue
            a = pts[:-1][ok]
            b = pts[1:][ok]
            a3 = np.column_stack([a, np.zeros(len(a))])
            b3 = np.column_stack([b, np.zeros(len(b))])
            segs.append(np.stack([a3, a3 + (b3 - a3) / 3, a3 + 2 * (b3 - a3) / 3, b3], axis=1))
        if not segs:
            return np.zeros((0, 3))
        return np.concatenate(segs).reshape(-1, 3)

    def rings_mobject(self, rect, centers_fn, op_tracker):
        m = VMobject()

        def upd(mob):
            e = self.ep()
            tk = self.emitted(e)
            centers = centers_fn(tk)
            radii = self.V * (e - tk)
            mob.set_points(self.ring_points(centers, radii, rect))
            mob.set_stroke(TEAL, width=3, opacity=op_tracker.get_value() * self.ep_fade())
            mob.set_fill(opacity=0)

        upd(m)
        m.add_updater(upd)
        return m

    # ---------------- B00 — split screen, matching motion ----------------
    def b00_hook(self):
        S = self.S
        ax0, ax1, ayg, _ = self.A_rect
        bx0, bx1, byg, _ = self.B_rect
        if self.PORTRAIT:
            self.divider = Line([-2.25, 0.35, 0], [2.25, 0.35, 0], color=INK, stroke_width=4)
        else:
            self.divider = Line([0, -2.6, 0], [0, 3.4, 0], color=INK, stroke_width=4)
        self.groundA = Line([ax0, ayg, 0], [ax1, ayg, 0], color=SLATE, stroke_width=2)
        self.groundB = Line([bx0, byg, 0], [bx1, byg, 0], color=SLATE, stroke_width=2)

        self.titleA = crisp_text("moving source", self.FS, color=INK, font=CAPTION_STYLE, weight=BOLD)
        self.titleA.move_to([(ax0 + ax1) / 2, self.A_title_y, 0])
        self.titleB = crisp_text("moving observer", self.FS, color=INK, font=CAPTION_STYLE, weight=BOLD)
        self.titleB.move_to([(bx0 + bx1) / 2, self.B_title_y, 0])

        # panel A: ambulance drives right toward a standing listener
        self.ambA = make_ambulance(S)
        self.ambA_dx = self.ambA[5].get_center()[0] - self.ambA.get_center()[0]  # light bar offset
        self.ambA_bottom = self.ambA.get_bottom()[1]

        def ambA_upd(m):
            e = self.ep()
            sx = self.a_src_x(e)
            m.move_to([sx - self.ambA_dx, m.get_center()[1], 0])
            m.set_opacity(self.ep_fade())
        self.ambA.move_to([self.a_src_x(0) - self.ambA_dx, ayg + self.ambA.height / 2 + 0.0, 0])
        self.ambA.add_updater(ambA_upd)
        self.listA = make_person(S, INK).move_to([self.a_listener_x(), ayg, 0], aligned_edge=DOWN)

        # panel B: parked ambulance, listener runs left toward it
        self.ambB = make_ambulance(S)
        dxB = self.ambB[5].get_center()[0] - self.ambB.get_center()[0]
        self.ambB.move_to([self.b_src_x() - dxB, byg + self.ambB.height / 2, 0])
        self.runner = make_person(S, INK, phase=0.0)

        def runner_upd(m):
            e = self.ep()
            new = make_person(S, INK, phase=2 * PI * 1.6 * (self.time - self.T0))
            new.move_to([self.b_runner_x(e), byg, 0], aligned_edge=DOWN)
            m.become(new)
            m.set_opacity(self.ep_fade())
        runner_upd(self.runner)
        self.runner.add_updater(runner_upd)

        # siren y used for ring centres: light bar centre
        self.sirenA_y = self.ambA[5].get_center()[1]
        self.sirenB_y = self.ambB[5].get_center()[1]
        self.sirenB_x = self.ambB[5].get_center()[0]

        self.play(Create(self.divider), Create(self.groundA), Create(self.groundB),
                  FadeIn(self.titleA), FadeIn(self.titleB), run_time=1.0)
        self.play(FadeIn(self.ambA), FadeIn(self.listA), FadeIn(self.ambB), FadeIn(self.runner), run_time=0.8)
        self.wait(max(DURS["B00"] - 1.8, 0.3))

    # ---------------- B01 — moving source: rings bunch ahead ----------------
    def b01_moving_source(self):
        S = self.S
        self.opA = ValueTracker(0.0)
        self.ringsA = self.rings_mobject(
            self.A_rect,
            lambda tk: np.column_stack([self.a_src_x(tk) + 0 * tk, np.full_like(tk, self.sirenA_y)]),
            self.opA)
        self.add(self.ringsA)
        self.bring_to_front(self.ambA, self.listA)

        # wavelength brackets locked to the ring pair (n-1, n-2)
        tick = 0.1 * S
        lab_fs = self.SMALL

        def bracket(x_a, x_b, y):
            return VGroup(Line([x_a, y, 0], [x_b, y, 0], color=INK, stroke_width=3),
                          Line([x_a, y - tick, 0], [x_a, y + tick, 0], color=INK, stroke_width=3),
                          Line([x_b, y - tick, 0], [x_b, y + tick, 0], color=INK, stroke_width=3))

        self.br_y = self.sirenA_y
        self.brA_front = VGroup()
        self.brA_back = VGroup()
        lfs = 20 if self.PORTRAIT else 28
        self.lab_front = MathTex(r"\text{shorter }\lambda", color=INK, font_size=lfs)
        self.lab_back = MathTex(r"\text{longer }\lambda", color=INK, font_size=lfs)
        self.lab_y = self.A_rect[2] - (0.16 if self.PORTRAIT else 0.24)  # under the ground line: never overlaps
        self.op_br = ValueTracker(0.0)

        def edges(sign):
            e = self.ep()
            tk = self.emitted(e)
            # front: rings n-5, n-4 (label clear of the cab); back: rings n-3, n-2
            if len(tk) < 6:
                return None
            pair = tk[-6:-4] if sign > 0 else tk[-4:-2]
            c = self.a_src_x(pair)
            r = self.V * (e - pair)
            # horizontal chord at height br_y above the siren
            h = self.br_y - self.sirenA_y
            if np.any(r <= h + 0.05):
                return None
            half = np.sqrt(r ** 2 - h ** 2)
            return c + sign * half

        def front_upd(m):
            x = edges(+1)
            op = self.op_br.get_value() * self.ep_fade()
            if x is None or x.max() > self.a_listener_x() - 0.4 * S:
                m.become(VGroup())
                self.lab_front.set_opacity(0)
                return
            m.become(bracket(x[0], x[1], self.br_y))
            m.set_stroke(opacity=op)
            self.lab_front.move_to([(x[0] + x[1]) / 2, self.lab_y, 0])
            self.lab_front.set_opacity(op)

        def back_upd(m):
            x = edges(-1)
            op = self.op_br.get_value() * self.ep_fade()
            if x is None or x.min() < self.A_rect[0] + 0.05:
                m.become(VGroup())
                self.lab_back.set_opacity(0)
                return
            m.become(bracket(x[0], x[1], self.br_y))
            m.set_stroke(opacity=op)
            self.lab_back.move_to([(x[0] + x[1]) / 2, self.lab_y, 0])
            self.lab_back.set_opacity(op)

        self.brA_front.add_updater(front_upd)
        self.brA_back.add_updater(back_upd)
        self.lab_front.set_opacity(0)
        self.lab_back.set_opacity(0)
        self.add(self.brA_front, self.brA_back, self.lab_front, self.lab_back)

        note = crisp_text("speeds exaggerated for visibility", self.SMALL, color=SLATE, font=CAPTION_STYLE)
        if self.PORTRAIT:
            note.move_to([0, self.A_rect[3] + 0.0, 0]).next_to(self.titleA, DOWN, buff=0.08)
        else:
            note.move_to([(self.A_rect[0] + self.A_rect[1]) / 2, self.A_rect[2] - 0.62, 0])
        self.note = note

        self.play(self.opA.animate.set_value(1.0), run_time=1.0)
        self.play(self.op_br.animate.set_value(1.0), FadeIn(note), run_time=0.8)
        self.wait(max(DURS["B01"] - 1.8, 0.3))

    # ---------------- B02 — moving observer: same rings, met faster ----------------
    def b02_moving_observer(self):
        S = self.S
        byg = self.B_rect[2]
        self.opB = ValueTracker(0.0)
        self.ringsB = self.rings_mobject(
            self.B_rect,
            lambda tk: np.column_stack([np.full_like(tk, self.sirenB_x), np.full_like(tk, self.sirenB_y)]),
            self.opB)
        self.add(self.ringsB)

        self.stander = make_person(S, SLATE).move_to([self.b_stander_x(), byg, 0], aligned_edge=DOWN)
        self.bring_to_front(self.ambB, self.runner)

        def met(e, x_ear):
            d = np.hypot(x_ear - self.sirenB_x, (byg + self.EAR_H) - self.sirenB_y)
            return int(np.floor((e - d / self.V) / DT_EMIT))

        def count(x_ear, x_ear0):
            # wavefronts that have reached this ear since the episode began
            return max(met(self.ep(), x_ear) - met(0.0, x_ear0), 0)

        cache = {}

        def num_text(n, color):
            key = (n, color)
            if key not in cache:
                t = crisp_text(str(n), self.FS, color=color, font=CAPTION_STYLE, weight=BOLD)
                bg = SurroundingRectangle(t, buff=0.05, stroke_width=0, fill_color=CREAM, fill_opacity=0.9)
                cache[key] = VGroup(bg, t)
            return cache[key].copy()

        self.op_c = ValueTracker(0.0)
        cnt_y = byg + 1.25 * S

        self.cnt_run = VGroup()
        self.cnt_std = VGroup()

        def run_upd(m):
            e = self.ep()
            x = self.b_runner_x(e)
            m.become(num_text(count(x, self.b_runner_x(0.0)), INK).move_to([x, cnt_y, 0]))
            m.set_opacity(self.op_c.get_value() * self.ep_fade())

        def std_upd(m):
            x = self.b_stander_x()
            m.become(num_text(count(x, x), SLATE).move_to([x, cnt_y, 0]))
            m.set_opacity(self.op_c.get_value() * self.ep_fade())

        self.cnt_run.add_updater(run_upd)
        self.cnt_std.add_updater(std_upd)
        run_upd(self.cnt_run)
        std_upd(self.cnt_std)
        cap_t = crisp_text("wavefronts met", self.SMALL, color=SLATE, font=CAPTION_STYLE)
        self.cnt_cap = VGroup(SurroundingRectangle(cap_t, buff=0.05, stroke_width=0, fill_color=CREAM,
                                                   fill_opacity=0.9), cap_t)
        cap_x = (self.B_rect[0] + self.B_rect[1]) / 2 + (0.9 if not self.PORTRAIT else 0.45)
        self.cnt_cap.move_to([cap_x, cnt_y + (0.65 if not self.PORTRAIT else 0.4), 0])

        self.play(self.opB.animate.set_value(1.0), FadeIn(self.stander), run_time=1.0)
        self.add(self.cnt_run, self.cnt_std)
        self.play(self.op_c.animate.set_value(1.0), FadeIn(self.cnt_cap), run_time=0.8)
        self.wait(max(DURS["B02"] - 1.8, 0.3))

    # ---------------- B03 — the two formulas ----------------
    def b03_formulas(self):
        fs = 26 if self.PORTRAIT else 40
        eqA = MathTex(r"f_o = f_s\,\frac{v}{v - v_s} \approx 548\ \text{Hz}", color=INK, font_size=fs)
        eqB = MathTex(r"f_o = f_s\,\frac{v + v_o}{v} \approx 544\ \text{Hz}", color=INK, font_size=fs)
        for eq, rect, y in ((eqA, self.A_rect, self.A_title_y), (eqB, self.B_rect, self.B_title_y)):
            maxw = (rect[1] - rect[0]) - 0.3
            if eq.width > maxw:
                eq.scale_to_fit_width(maxw)
            eq.move_to([(rect[0] + rect[1]) / 2, y, 0])
        if self.PORTRAIT:
            eqA.shift(DOWN * 0.08)
        self.eqA, self.eqB = eqA, eqB
        given = MathTex(r"v = 340\ \text{m/s},\quad f_s = 500\ \text{Hz},\quad v_s = v_o = 30\ \text{m/s}",
                        color=SLATE, font_size=22 if self.PORTRAIT else 28)
        if given.width > 2 * safe_half_w():
            given.scale_to_fit_width(2 * safe_half_w())
        self.given = given
        anims = [FadeOut(self.titleA), FadeOut(self.titleB)]
        if self.PORTRAIT:
            # no room under the formulas: the given values take the divider's slot
            given.move_to([0, 0.37, 0])
            anims += [FadeOut(self.note), FadeOut(self.divider)]
        else:
            given.move_to([(self.B_rect[0] + self.B_rect[1]) / 2, self.B_rect[2] - 0.62, 0])
        self.play(*anims, run_time=0.5)
        self.play(Write(eqA), run_time=1.5)
        self.wait(max(DURS["B03"] * 0.35 - 2.0, 0.3))
        self.play(Write(eqB), run_time=1.5)
        self.play(FadeIn(given), run_time=0.6)
        self.wait(max(DURS["B03"] - (max(DURS["B03"] * 0.35 - 2.0, 0.3) + 4.1), 0.3))

    # ---------------- B04 — summary ----------------
    def b04_hold(self):
        if self.PORTRAIT:
            summary = crisp_text("THE MEDIUM BREAKS THE SYMMETRY", 14, color=INK, font=CAPTION_STYLE, weight=BOLD)
            if summary.width > 2 * safe_half_w():
                summary.scale_to_fit_width(2 * safe_half_w())
            summary.move_to([0, 0.37, 0])
            self.summary = VGroup(summary)
            self.play(FadeOut(self.given), FadeIn(self.summary), run_time=0.8)
        else:
            summary = crisp_text("THE MEDIUM BREAKS THE SYMMETRY", 26, color=INK, font=CAPTION_STYLE, weight=BOLD)
            sub = crisp_text("moving source: shorter wavelength   ·   moving observer: faster arrival", 16,
                             color=SLATE, font=CAPTION_STYLE)
            summary.move_to([0, -2.55, 0])
            sub.next_to(summary, DOWN, buff=0.18)
            self.summary = VGroup(summary, sub)
            self.play(FadeOut(self.divider), FadeOut(self.note), FadeOut(self.given), FadeIn(self.summary),
                      run_time=0.8)
        self.wait(max(DURS["B04"] - 0.8, 0.3))
