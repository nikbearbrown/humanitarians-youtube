"""beats.py — Chapter 17, Beats.

Two steady tones of nearly equal frequency, recorded as pressure versus time
at the listener, drift in and out of step. Their live point-by-point sum
swells and pinches inside an envelope whose loudness maxima repeat at the
beat frequency f_beat = |f2 - f1| (444 Hz - 440 Hz = 4 Hz).

Strip charts scroll continuously (newest instant at the right edge). The
displayed frequencies are 3.0 and 3.5 cycles per second of screen time, an
exaggerated ratio so the drift is visible; this is stated on screen.

Orientation-aware, one file renders either aspect:
  Landscape (16:9): manim -qh beats.py Beats
  Portrait  (9:16): manim -r 1080,1920 --fps 30 --disable_caching beats.py Beats
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

F1, F2 = 3.0, 3.5          # displayed cycles per second of screen time
DF = F2 - F1               # displayed beat frequency (0.5 Hz -> a pulse every 2 s)


class Beats(MedhavyScene):
    def construct(self):
        self.PORTRAIT = PORTRAIT
        if PORTRAIT:
            self.X0, self.X1, self.XM = -1.65, 1.15, 1.45
            self.T = 3.0
            self.Y1, self.Y2, self.YS = 2.4, 1.3, -0.05
            self.A = 0.28
            self.N = 320
            self.FS = 15
            self.GUIDE_LAB_Y = 0.77
            self.NOTE_Y = -0.97
        else:
            self.X0, self.X1, self.XM = -5.0, 5.0, 5.75
            self.T = 4.0
            self.Y1, self.Y2, self.YS = 2.3, 1.1, -1.0
            self.A = 0.4
            self.N = 560
            self.FS = 20
            self.GUIDE_LAB_Y = 0.45
            self.NOTE_Y = -2.3

        # frozen-frame guard for landscape waits (portrait handled by MedhavyScene)
        self.ticker = Mobject()
        self.ticker.add_updater(lambda m, dt: None)
        self.add(self.ticker)

        if self.PORTRAIT:
            self.init_captions(build_caption_schedule(SHEET, DURS, NARR), -safe_half_h() + 0.5)
            self.question_card(NARR["B00Q"], DURS["B00Q"])

        self.t0 = self.time
        self.b00_hook()
        self.b01_drift()
        self.b02_sum()
        self.b03_envelope()
        self.b04_hold()

    # ---------------- helpers ----------------
    def tau(self):
        """Signal time at the right (newest) edge of the chart."""
        return self.time - self.t0 + self.T

    def t_to_x(self, t):
        return self.X0 + (t - (self.tau() - self.T)) / self.T * (self.X1 - self.X0)

    def ts(self):
        tau = self.tau()
        return np.linspace(tau - self.T, tau, self.N)

    def s1(self, t):
        return self.A * np.cos(2 * PI * F1 * t)

    def s2(self, t):
        return self.A * np.cos(2 * PI * F2 * t)

    def env(self, t):
        return 2 * self.A * np.abs(np.cos(PI * DF * t))

    def curve(self, fn, y_tracker, op_tracker, color, width):
        m = VMobject()

        def upd(mob):
            t = self.ts()
            x = np.linspace(self.X0, self.X1, self.N)
            pts = np.column_stack([x, y_tracker.get_value() + fn(t), np.zeros_like(x)])
            mob.set_points_as_corners(pts)
            mob.set_stroke(color=color, width=width, opacity=op_tracker.get_value())
            mob.set_fill(opacity=0)

        upd(m)
        m.add_updater(upd)
        return m

    def visible_times(self, phase):
        """Times k/DF + phase/DF currently inside the chart window."""
        tau = self.tau()
        lo, hi = tau - self.T, tau
        k0 = int(np.floor(lo * DF - phase)) - 1
        out = []
        for k in range(k0, k0 + int(self.T * DF) + 4):
            t = (k + phase) / DF
            if lo + 0.02 <= t <= hi - 0.02:
                out.append(t)
        return out

    def baseline(self, y):
        return Line([self.X0, y, 0], [self.X1, y, 0], color=SLATE, stroke_width=1.2)

    # ---------------- B00 — two scrolling tones ----------------
    def b00_hook(self):
        self.op1 = ValueTracker(1.0)
        self.yt1, self.yt2 = ValueTracker(self.Y1), ValueTracker(self.Y2)
        self.base1, self.base2 = self.baseline(self.Y1), self.baseline(self.Y2)
        self.w1 = self.curve(self.s1, self.yt1, self.op1, TEAL, 4)
        self.w2 = self.curve(self.s2, self.yt2, self.op1, CRIMSON, 4)

        self.lab1 = crisp_text("440 Hz", self.FS, color=TEAL, font=CAPTION_STYLE, weight=BOLD)
        self.lab2 = crisp_text("444 Hz", self.FS, color=CRIMSON, font=CAPTION_STYLE, weight=BOLD)
        if self.PORTRAIT:
            self.lab1.next_to(self.base1, UP, buff=self.A + 0.12).align_to(self.base1, LEFT)
            self.lab2.next_to(self.base2, UP, buff=self.A + 0.12).align_to(self.base2, LEFT)
        else:
            self.lab1.next_to(self.base1, LEFT, buff=0.3)
            self.lab2.next_to(self.base2, LEFT, buff=0.3)

        self.play(Create(self.base1), Create(self.base2), FadeIn(self.w1), FadeIn(self.w2), run_time=1.0)
        self.play(FadeIn(self.lab1), FadeIn(self.lab2), run_time=0.6)
        self.wait(max(DURS["B00"] - 1.6, 0.3))

    # ---------------- B01 — in step / out of step guides ----------------
    def b01_drift(self):
        self.op_g = ValueTracker(0.0)
        top, bot = self.Y1 + self.A + 0.08, self.Y2 - self.A - 0.08
        pool = 5
        self.g_in = VGroup(*[DashedLine([0, bot, 0], [0, top, 0], color=INK, stroke_width=3.5,
                                        dash_length=0.1) for _ in range(pool)])
        self.g_out = VGroup(*[DashedLine([0, bot, 0], [0, top, 0], color=SLATE, stroke_width=2.5,
                                         dash_length=0.1) for _ in range(pool)])
        lab_fs = 12 if self.PORTRAIT else 16
        self.gl_in = VGroup(*[crisp_text("in step", lab_fs, color=INK, font=CAPTION_STYLE) for _ in range(pool)])
        self.gl_out = VGroup(*[crisp_text("out of step", lab_fs, color=SLATE, font=CAPTION_STYLE) for _ in range(pool)])
        mid = (top + bot) / 2

        def place(lines, labels, phase):
            def upd(_m):
                times = self.visible_times(phase)
                op = self.op_g.get_value()
                for i, (ln, lb) in enumerate(zip(lines, labels)):
                    if i < len(times):
                        x = self.t_to_x(times[i])
                        ln.move_to([x, mid, 0])
                        lb.move_to([x, self.GUIDE_LAB_Y, 0])
                        ln.set_stroke(opacity=op)
                        lb.set_opacity(op)
                    else:
                        ln.set_stroke(opacity=0)
                        lb.set_opacity(0)
            return upd

        self.g_in.add_updater(place(self.g_in, self.gl_in, 0.0))
        self.g_out.add_updater(place(self.g_out, self.gl_out, 0.5))
        self.add(self.g_in, self.g_out, self.gl_in, self.gl_out)
        self.g_in.update(); self.g_out.update()

        note_txt = "frequency difference exaggerated\nso the drift is visible" if self.PORTRAIT \
            else "frequency difference exaggerated so the drift is visible"
        self.note = crisp_text(note_txt, 11 if self.PORTRAIT else 14, color=SLATE, font=CAPTION_STYLE,
                               line_spacing=1.0)
        self.note.move_to([0, self.NOTE_Y, 0])

        self.play(self.op_g.animate.set_value(1.0), run_time=1.0)
        self.play(FadeIn(self.note), run_time=0.5)
        self.wait(max(DURS["B01"] - 1.5, 0.3))

    # ---------------- B02 — the live sum ----------------
    def b02_sum(self):
        # ghost copies of the two tones descend onto the sum axis and merge
        self.op_ghost = ValueTracker(0.0)
        self.yg1, self.yg2 = ValueTracker(self.Y1), ValueTracker(self.Y2)
        self.g1 = self.curve(self.s1, self.yg1, self.op_ghost, TEAL, 3)
        self.g2 = self.curve(self.s2, self.yg2, self.op_ghost, CRIMSON, 3)
        self.op_s = ValueTracker(0.0)
        self.ys = ValueTracker(self.YS)
        self.wsum = self.curve(lambda t: self.s1(t) + self.s2(t), self.ys, self.op_s, INK, 5)
        self.base_s = self.baseline(self.YS)
        self.add(self.g1, self.g2, self.wsum)

        self.play(self.op_g.animate.set_value(0.0), self.op1.animate.set_value(0.45),
                  self.op_ghost.animate.set_value(0.8), run_time=0.8)
        self.play(self.yg1.animate.set_value(self.YS), self.yg2.animate.set_value(self.YS),
                  Create(self.base_s), run_time=1.6)
        self.play(self.op_s.animate.set_value(1.0), self.op_ghost.animate.set_value(0.0), run_time=1.0)
        for m in (self.g_in, self.g_out, self.g1, self.g2):
            m.clear_updaters()
        self.remove(self.g_in, self.g_out, self.gl_in, self.gl_out, self.g1, self.g2)

        # grey silence bands around each crest-on-trough instant
        self.op_b = ValueTracker(0.0)
        bw = 0.28 / DF / self.T * (self.X1 - self.X0)
        self.bands = VGroup(*[Rectangle(width=bw, height=2.2 * 2 * self.A, stroke_width=0)
                              .set_fill(SLATE, 0) for _ in range(4)])

        def band_upd(g):
            times = self.visible_times(0.5)
            for i, r in enumerate(g):
                if i < len(times):
                    r.move_to([self.t_to_x(times[i]), self.YS, 0])
                    r.set_fill(SLATE, 0.16 * self.op_b.get_value())
                else:
                    r.set_fill(SLATE, 0)

        band_upd(self.bands)
        self.bands.add_updater(band_upd)
        self.add(self.bands)
        self.bring_to_back(self.bands)
        self.play(self.op_b.animate.set_value(1.0), run_time=0.6)
        self.wait(max(DURS["B02"] - 4.0, 0.3))

    # ---------------- B03 — envelope, amplitude bar, beat frequency ----------------
    def b03_envelope(self):
        self.frac = ValueTracker(0.0)
        dash_dt = 0.035 * self.T  # dash period in signal time

        def env_upd(m):
            tau = self.tau()
            lo = tau - self.T
            hi = lo + self.frac.get_value() * self.T
            # dashes anchored to signal time so they scroll with the curve
            k0 = np.ceil(lo / dash_dt)
            ks = np.arange(k0, np.floor((hi - 0.55 * dash_dt) / dash_dt) + 1)
            if len(ks) == 0:
                for sub in m:
                    sub.set_points(np.zeros((0, 3)))
                return
            ta, tb = ks * dash_dt, ks * dash_dt + 0.55 * dash_dt
            xa, xb = self.t_to_x(ta), self.t_to_x(tb)
            segs = []
            for sgn in (1, -1):
                a = np.column_stack([xa, self.YS + sgn * self.env(ta), np.zeros_like(xa)])
                b = np.column_stack([xb, self.YS + sgn * self.env(tb), np.zeros_like(xb)])
                segs.append(np.stack([a, a + (b - a) / 3, a + 2 * (b - a) / 3, b], axis=1))
            pts = np.concatenate(segs).reshape(-1, 3)
            # gold dash on a slate underlay: bare GOLD is too faint on white
            under, top = m
            under.set_points(pts)
            under.set_stroke(SLATE, width=8, opacity=1)
            top.set_points(pts)
            top.set_stroke(GOLD, width=5, opacity=1)
            under.set_fill(opacity=0)
            top.set_fill(opacity=0)

        self.envelope = VGroup(VMobject(), VMobject())
        env_upd(self.envelope)
        self.envelope.add_updater(env_upd)
        self.add(self.envelope)

        # amplitude bar at the present instant (right edge)
        bar_w = 0.16 if self.PORTRAIT else 0.3
        full = 2 * 2 * self.A
        self.op_m = ValueTracker(0.0)
        self.meter_frame = Rectangle(width=bar_w, height=full, stroke_width=1.5, color=SLATE) \
            .move_to([self.XM, self.YS, 0])
        self.meter_bar = Rectangle(width=bar_w, height=full, stroke_width=0).set_fill(GOLD, 0) \
            .move_to([self.XM, self.YS, 0])

        def bar_upd(m):
            h = max(2 * self.env(self.tau()), 0.01)
            m.stretch_to_fit_height(h)
            m.move_to([self.XM, self.YS, 0])
            m.set_fill(GOLD, 0.9 * self.op_m.get_value())

        bar_upd(self.meter_bar)
        self.meter_bar.add_updater(bar_upd)
        self.meter_lab = crisp_text("now", 12 if self.PORTRAIT else 16, color=SLATE, font=CAPTION_STYLE)
        self.meter_lab.next_to(self.meter_frame, DOWN, buff=0.12)

        if self.PORTRAIT:
            eq = MathTex(r"f_{\text{beat}} = |f_2 - f_1| = 4\,\text{Hz}", color=INK, font_size=34)
            eq.move_to([0, -1.95, 0])
        else:
            eq = MathTex(r"f_{\text{beat}} = |f_2 - f_1|", r"= 444\,\text{Hz} - 440\,\text{Hz} = 4\,\text{Hz}",
                         color=INK, font_size=44)
            eq.move_to([0, -2.95, 0])
        if eq.width > 2 * safe_half_w():
            eq.scale_to_fit_width(2 * safe_half_w())
        self.eq = eq

        self.play(self.frac.animate.set_value(1.0), run_time=2.0, rate_func=linear)
        self.add(self.meter_bar)
        self.play(FadeIn(self.meter_frame), FadeIn(self.meter_lab), self.op_m.animate.set_value(1.0), run_time=0.6)
        self.play(Write(eq), run_time=1.5)
        self.wait(max(DURS["B03"] - 4.1, 0.3))

    # ---------------- B04 — summary hold ----------------
    def b04_hold(self):
        if self.PORTRAIT:
            summary = crisp_text("BEAT FREQUENCY =\nDIFFERENCE OF FREQUENCIES", 15, color=INK,
                                 font=CAPTION_STYLE, weight=BOLD, line_spacing=1.05)
            summary.move_to([0, -1.2, 0])
            extra = [FadeOut(self.note)]
        else:
            summary = crisp_text("BEAT FREQUENCY = DIFFERENCE OF THE TWO FREQUENCIES", 22, color=INK,
                                 font=CAPTION_STYLE, weight=BOLD)
            summary.move_to([0, 3.15, 0])
            extra = [FadeOut(self.note)]
        if summary.width > 2 * safe_half_w():
            summary.scale_to_fit_width(2 * safe_half_w())
        self.summary = summary
        self.play(FadeIn(summary), self.op_b.animate.set_value(0.0), *extra, run_time=0.8)
        self.wait(max(DURS["B04"] - 0.8, 0.3))
