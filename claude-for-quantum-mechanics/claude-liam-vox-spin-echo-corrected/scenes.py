import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np
import math

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ── B01: Cold open — spins fan out, signal dies ──────────────────────────────

class OldSpinsFanOutColdOpen(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)

        title = Text("SPIN ECHO", font=DISPLAY, font_size=28, color=INK,
                     weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        origin = np.array([0.0, 0.0, 0.0])
        n_spins = 9

        # All arrows start pointing up
        arrows = VGroup()
        for i in range(n_spins):
            arr = Arrow(origin, origin + np.array([0.0, 1.8, 0.0]),
                        buff=0, color=TEAL, stroke_width=3)
            arrows.add(arr)

        # Sum arrow (total magnetization)
        sum_arrow = Arrow(origin, origin + np.array([0.0, 2.2, 0.0]),
                          buff=0, color=INK, stroke_width=5)
        sum_lbl = Text("M", font=SERIF, font_size=32, color=INK,
                       slant=ITALIC).next_to(sum_arrow.get_end(), RIGHT, buff=0.15)

        self.play(FadeIn(arrows), FadeIn(sum_arrow), FadeIn(sum_lbl),
                  run_time=0.6)

        # Fan out: spread arrows over a 300-degree arc
        fan_anims = []
        spread_angles = np.linspace(-math.pi * 5/6, math.pi * 5/6, n_spins)
        for arr, angle in zip(arrows, spread_angles):
            tip = origin + 1.8 * np.array([math.sin(angle), math.cos(angle), 0.0])
            fan_anims.append(arr.animate.put_start_and_end_on(origin, tip))
        # Sum shrinks toward zero
        fan_anims.append(sum_arrow.animate.put_start_and_end_on(
            origin, origin + np.array([0.0, 0.05, 0.0])))
        fan_anims.append(FadeOut(sum_lbl))

        self.play(*fan_anims, run_time=dur * 0.55)

        zero_lbl = Text("signal = 0", font=DISPLAY, font_size=26, color=CRIMSON
                        ).move_to(np.array([0.0, -2.5, 0.0]))
        self.play(FadeIn(zero_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.6 - dur * 0.55 - 0.4))


# ── B02: Cold open — echo returns at 2τ ─────────────────────────────────────

class B02_EchoReturns(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)

        title = Text("SPIN ECHO", font=DISPLAY, font_size=28, color=INK,
                     weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        origin = np.array([0.0, 0.0, 0.0])
        n_spins = 9

        # Start fanned out
        spread_angles = np.linspace(-math.pi * 5/6, math.pi * 5/6, n_spins)
        arrows = VGroup()
        for angle in spread_angles:
            tip = origin + 1.8 * np.array([math.sin(angle), math.cos(angle), 0.0])
            arr = Arrow(origin, tip, buff=0, color=TEAL, stroke_width=3)
            arrows.add(arr)

        sum_arrow = Arrow(origin, origin + np.array([0.0, 0.05, 0.0]),
                          buff=0, color=INK, stroke_width=5)
        zero_lbl = Text("signal = 0", font=DISPLAY, font_size=26, color=CRIMSON
                        ).move_to(np.array([0.0, -2.5, 0.0]))

        self.add(arrows, sum_arrow, zero_lbl)

        # Rephase: all arrows snap back to up
        rephase_anims = []
        for arr in arrows:
            tip = origin + np.array([0.0, 1.8, 0.0])
            rephase_anims.append(arr.animate.put_start_and_end_on(origin, tip))
        sum_end = origin + np.array([0.0, 2.2, 0.0])
        rephase_anims.append(sum_arrow.animate.put_start_and_end_on(origin, sum_end))
        rephase_anims.append(FadeOut(zero_lbl))

        self.play(*rephase_anims, run_time=dur * 0.55)

        echo_lbl = Text("ECHO at t = 2τ", font=DISPLAY, font_size=28,
                        color=TEAL, weight=BOLD).move_to(np.array([0.0, -2.2, 0.0]))
        self.play(FadeIn(echo_lbl), run_time=0.5)
        self.wait(max(0.1, dur - dur * 0.55 - 0.5))


# ── B04: The problem — inhomogeneous field ───────────────────────────────────

class B04_InhomogeneousField(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)

        title = Text("Inhomogeneous Field", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Show 5 spin sites spread horizontally
        x_positions = [-3.6, -1.8, 0.0, 1.8, 3.6]
        origin_y = -0.5

        spin_arrows = VGroup()
        field_labels = VGroup()
        field_deltas = [-0.02, -0.01, 0.0, 0.01, 0.02]
        field_strs = ["-2%", "-1%", "B₀", "+1%", "+2%"]

        for x, dB, fs in zip(x_positions, field_deltas, field_strs):
            orig = np.array([x, origin_y, 0.0])
            tip = orig + np.array([0.0, 1.6, 0.0])
            col = CRIMSON if dB > 0 else (TEAL if dB < 0 else INK)
            arr = Arrow(orig, tip, buff=0, color=col, stroke_width=4)
            spin_arrows.add(arr)
            lbl = Text(fs, font=DISPLAY, font_size=20, color=col
                       ).move_to(np.array([x, origin_y - 0.5, 0.0]))
            field_labels.add(lbl)

        field_title = Text("Each spin sees a different B", font=SERIF,
                           font_size=26, color=INK, slant=ITALIC
                           ).move_to(np.array([0.0, -2.0, 0.0]))

        self.play(LaggedStart(*[FadeIn(a) for a in spin_arrows],
                              lag_ratio=0.15, run_time=1.0))
        self.play(LaggedStart(*[FadeIn(l) for l in field_labels],
                              lag_ratio=0.12, run_time=0.8))
        self.play(FadeIn(field_title), run_time=0.5)

        # Show precession: faster for higher field (CRIMSON), slower for TEAL
        rate_lbl = Text("→ different precession rates", font=SERIF,
                        font_size=26, color=INK, slant=ITALIC
                        ).move_to(np.array([0.0, -2.7, 0.0]))
        self.play(FadeIn(rate_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.0 - 0.8 - 0.5 - 0.5))


# ── B05: The problem — fan spreads, signal dies ──────────────────────────────

class B05_FanSpread(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)

        title = Text("Spins Fan Out", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        origin = np.array([0.0, 0.0, 0.0])

        # Fast (CRIMSON) and slow (TEAL) representatives
        fast_start = origin + np.array([0.0, 1.8, 0.0])
        slow_start = origin + np.array([0.0, 1.8, 0.0])

        fast_arr = Arrow(origin, fast_start, buff=0, color=CRIMSON, stroke_width=5)
        slow_arr = Arrow(origin, slow_start, buff=0, color=TEAL, stroke_width=5)
        mid_arr  = Arrow(origin, origin + np.array([0.0, 1.8, 0.0]),
                         buff=0, color=INK, stroke_width=3)

        fast_lbl = Text("fast", font=DISPLAY, font_size=22, color=CRIMSON
                        ).move_to(np.array([2.5, 1.2, 0.0]))
        slow_lbl = Text("slow", font=DISPLAY, font_size=22, color=TEAL
                        ).move_to(np.array([-2.5, 1.2, 0.0]))

        tau_lbl = Text("after τ:", font=SERIF, font_size=26, color=INK,
                       slant=ITALIC).move_to(np.array([-4.0, 2.0, 0.0]))

        self.play(FadeIn(fast_arr), FadeIn(slow_arr), FadeIn(mid_arr), run_time=0.5)

        # Spread: fast goes clockwise (right), slow goes counter-clockwise (left)
        fast_angle = math.pi * 2 / 3   # 120° ahead (right/down)
        slow_angle = -math.pi * 2 / 3  # 120° behind (left/down)
        fast_tip = origin + 1.8 * np.array([math.sin(fast_angle), math.cos(fast_angle), 0.0])
        slow_tip = origin + 1.8 * np.array([math.sin(slow_angle), math.cos(slow_angle), 0.0])

        self.play(
            fast_arr.animate.put_start_and_end_on(origin, fast_tip),
            slow_arr.animate.put_start_and_end_on(origin, slow_tip),
            FadeIn(tau_lbl),
            run_time=dur * 0.45,
        )

        self.play(FadeIn(fast_lbl), FadeIn(slow_lbl), run_time=0.4)

        # Signal = 0
        sum_zero = Text("total M = 0", font=DISPLAY, font_size=28,
                        color=CRIMSON, weight=BOLD).move_to(np.array([0.0, -2.5, 0.0]))
        self.play(FadeIn(sum_zero), run_time=0.4)
        self.wait(max(0.1, dur - 0.5 - dur * 0.45 - 0.4 - 0.4))


# ── B06: The mechanism — π-pulse flips ordering ──────────────────────────────

class B06_PiPulse(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)

        title = Text("The π-Pulse", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        origin = np.array([0.0, 0.0, 0.0])

        # Before: fast ahead (right), slow behind (left)
        fast_angle_before = math.pi / 4   # 45° ahead
        slow_angle_before = -math.pi / 4  # 45° behind
        fast_tip_b = origin + 1.8 * np.array([math.sin(fast_angle_before), math.cos(fast_angle_before), 0.0])
        slow_tip_b = origin + 1.8 * np.array([math.sin(slow_angle_before), math.cos(slow_angle_before), 0.0])

        fast_arr = Arrow(origin, fast_tip_b, buff=0, color=CRIMSON, stroke_width=5)
        slow_arr = Arrow(origin, slow_tip_b, buff=0, color=TEAL, stroke_width=5)

        before_lbl = Text("before π-pulse", font=SERIF, font_size=22,
                          color=INK, slant=ITALIC).move_to(np.array([0.0, -1.6, 0.0]))
        fast_lbl_b = Text("fast: +45°", font=DISPLAY, font_size=20,
                          color=CRIMSON).move_to(np.array([2.8, 1.8, 0.0]))
        slow_lbl_b = Text("slow: −45°", font=DISPLAY, font_size=20,
                          color=TEAL).move_to(np.array([-2.8, 1.8, 0.0]))

        self.play(FadeIn(fast_arr), FadeIn(slow_arr),
                  FadeIn(before_lbl), FadeIn(fast_lbl_b), FadeIn(slow_lbl_b),
                  run_time=0.6)

        # Flash the π-pulse (horizontal bar)
        pulse_bar = Rectangle(width=10.0, height=0.25, color=GOLD,
                              fill_opacity=0.7, stroke_width=0
                              ).move_to(np.array([0.0, 0.0, 0.0]))
        pulse_lbl = Text("π-pulse", font=DISPLAY, font_size=26,
                         color=INK, weight=BOLD).move_to(np.array([0.0, -0.55, 0.0]))

        self.play(FadeIn(pulse_bar), FadeIn(pulse_lbl), run_time=0.4)
        self.play(FadeOut(pulse_bar), FadeOut(pulse_lbl),
                  FadeOut(before_lbl), FadeOut(fast_lbl_b), FadeOut(slow_lbl_b),
                  run_time=0.3)

        # After: angles negated (mirrored)
        fast_tip_a = origin + 1.8 * np.array([math.sin(-fast_angle_before),
                                               math.cos(-fast_angle_before), 0.0])
        slow_tip_a = origin + 1.8 * np.array([math.sin(-slow_angle_before),
                                               math.cos(-slow_angle_before), 0.0])

        self.play(
            fast_arr.animate.put_start_and_end_on(origin, fast_tip_a),
            slow_arr.animate.put_start_and_end_on(origin, slow_tip_a),
            run_time=dur * 0.40,
        )

        after_lbl = Text("after π-pulse", font=SERIF, font_size=22,
                         color=INK, slant=ITALIC).move_to(np.array([0.0, -2.3, 0.0]))
        fast_lbl_a = Text("fast: −45°", font=DISPLAY, font_size=20,
                          color=CRIMSON).move_to(np.array([-2.8, 1.2, 0.0]))
        slow_lbl_a = Text("slow: +45°", font=DISPLAY, font_size=20,
                          color=TEAL).move_to(np.array([2.8, 1.2, 0.0]))
        order_lbl = Text("ordering reversed", font=DISPLAY, font_size=24,
                         color=INK, weight=BOLD).move_to(np.array([0.0, -3.2, 0.0]))

        self.play(FadeIn(after_lbl), FadeIn(fast_lbl_a), FadeIn(slow_lbl_a),
                  FadeIn(order_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.6 - 0.4 - 0.3 - dur * 0.40 - 0.5))


# ── B07: The mechanism — arrows converge, echo ──────────────────────────────

class B07_EchoConverge(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)

        title = Text("Echo at 2τ", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        origin = np.array([0.0, 0.0, 0.0])

        # Start: fast behind (left), slow ahead (right) — post π-pulse
        fast_angle = -math.pi / 4
        slow_angle = math.pi / 4
        fast_tip_s = origin + 1.8 * np.array([math.sin(fast_angle), math.cos(fast_angle), 0.0])
        slow_tip_s = origin + 1.8 * np.array([math.sin(slow_angle), math.cos(slow_angle), 0.0])

        fast_arr = Arrow(origin, fast_tip_s, buff=0, color=CRIMSON, stroke_width=5)
        slow_arr = Arrow(origin, slow_tip_s, buff=0, color=TEAL, stroke_width=5)

        fast_lbl = Text("fast (still fast)", font=DISPLAY, font_size=20,
                        color=CRIMSON).move_to(np.array([-3.2, 0.8, 0.0]))
        slow_lbl = Text("slow (still slow)", font=DISPLAY, font_size=20,
                        color=TEAL).move_to(np.array([3.2, 0.8, 0.0]))

        self.play(FadeIn(fast_arr), FadeIn(slow_arr),
                  FadeIn(fast_lbl), FadeIn(slow_lbl), run_time=0.5)

        # Converge to up (0°)
        up_tip = origin + np.array([0.0, 1.8, 0.0])
        self.play(
            fast_arr.animate.put_start_and_end_on(origin, up_tip),
            slow_arr.animate.put_start_and_end_on(origin, up_tip),
            FadeOut(fast_lbl), FadeOut(slow_lbl),
            run_time=dur * 0.50,
        )

        # Full sum arrow + echo label
        sum_arrow = Arrow(origin, origin + np.array([0.0, 2.2, 0.0]),
                          buff=0, color=INK, stroke_width=6)
        echo_lbl = Text("ECHO", font=DISPLAY, font_size=36,
                        color=TEAL, weight=BOLD).move_to(np.array([0.0, -1.8, 0.0]))
        tau2_lbl = Text("t = 2τ", font=SERIF, font_size=28, color=INK,
                        slant=ITALIC).move_to(np.array([0.0, -2.5, 0.0]))

        self.play(FadeIn(sum_arrow), FadeIn(echo_lbl), FadeIn(tau2_lbl),
                  run_time=0.6)
        self.wait(max(0.1, dur - 0.5 - dur * 0.50 - 0.6))


# ── B08: Implication — T₂ decay curve ───────────────────────────────────────

class B08_T2Decay(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        title = Text("Hahn echo envelope often ~ e^(−2τ/T₂)", font=DISPLAY,
                     font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Axes
        ax = Axes(
            x_range=[0, 3.2, 1],
            y_range=[0, 1.15, 0.5],
            x_length=7.5,
            y_length=4.0,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([-0.3, -0.5, 0.0]))

        x_lbl = Text("2τ", font=SERIF, font_size=26, color=INK, slant=ITALIC
                     ).move_to(np.array([3.7, -0.5, 0.0]))
        y_lbl = Text("echo\namplitude", font=SERIF, font_size=22, color=INK,
                     slant=ITALIC).move_to(np.array([-4.2, 1.6, 0.0]))

        self.play(FadeIn(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)

        # Exponential decay curve: e^(-t/1.0) (T2=1 in normalized units)
        curve = ax.plot(lambda t: math.exp(-t), x_range=[0, 3.0], color=TEAL,
                        stroke_width=3)
        self.play(Create(curve), run_time=dur * 0.40)

        t2_lbl = Text("echo envelope: irreversible + dynamic losses", font=SERIF, font_size=22,
                      color=TEAL, slant=ITALIC).move_to(np.array([2.2, 1.8, 0.0]))
        cancel_lbl = Text("ideal static offsets refocus", font=SERIF,
                          font_size=22, color=INK, slant=ITALIC
                          ).move_to(np.array([0.0, -2.5, 0.0]))

        self.play(FadeIn(t2_lbl), FadeIn(cancel_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 0.5 - dur * 0.40 - 0.5))


# ── B09: Implication — MRI in imperfect magnet ───────────────────────────────

class B09_MRI(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)

        title = Text("Spin echoes in MRI and NMR", font=DISPLAY, font_size=28,
                     color=INK, weight=BOLD).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        # Magnet coil (imperfect) — simple ellipse outline
        coil = Ellipse(width=7.0, height=3.5, color=SLATE, stroke_width=3,
                       fill_opacity=0).move_to(np.array([0.0, 0.2, 0.0]))
        imperfect_lbl = Text("static field inhomogeneity", font=SERIF, font_size=22,
                             color=SLATE, slant=ITALIC
                             ).move_to(np.array([0.0, -1.5, 0.0]))

        # Timeline bar inside coil
        timeline = Line(np.array([-2.5, 0.2, 0.0]), np.array([2.5, 0.2, 0.0]),
                        color=INK, stroke_width=2)
        tau_mark = Dot(np.array([0.0, 0.2, 0.0]), radius=0.07, color=INK)
        tau_tick = Line(np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.4, 0.0]),
                        color=INK, stroke_width=2)
        pi_lbl = Text("π", font=SERIF, font_size=24, color=CRIMSON
                      ).move_to(np.array([0.0, 0.7, 0.0]))
        echo_dot = Dot(np.array([2.5, 0.2, 0.0]), radius=0.10, color=TEAL)
        echo_tick = Line(np.array([2.5, 0.0, 0.0]), np.array([2.5, 0.4, 0.0]),
                         color=TEAL, stroke_width=2)
        echo_lbl = Text("echo", font=DISPLAY, font_size=20, color=TEAL
                        ).move_to(np.array([2.5, 0.85, 0.0]))

        t2_result = Text("echo suppresses static inhomogeneous broadening",
                         font=SERIF, font_size=22, color=TEAL, slant=ITALIC
                         ).move_to(np.array([0.0, -2.5, 0.0]))

        self.play(FadeIn(coil), run_time=0.5)
        self.play(FadeIn(imperfect_lbl), run_time=0.4)
        self.play(FadeIn(timeline), FadeIn(tau_mark), FadeIn(tau_tick),
                  FadeIn(pi_lbl), run_time=0.4)
        self.play(FadeIn(echo_dot), FadeIn(echo_tick), FadeIn(echo_lbl),
                  run_time=0.4)
        self.play(FadeIn(t2_result), run_time=0.4)
        self.wait(max(0.1, dur - 0.5 - 0.4 - 0.4 - 0.4 - 0.4))


# ── B10: Example — data points & fit ─────────────────────────────────────────

class B10_ExampleFit(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)

        title = Text("Illustrative: T₂ Fit from Echo Amplitudes",
                     font=DISPLAY, font_size=26, color=INK, weight=BOLD
                     ).move_to(np.array([0.0, 3.0, 0.0]))
        self.add(title)

        ax = Axes(
            x_range=[0, 250, 50],
            y_range=[0, 1.15, 0.5],
            x_length=8.0,
            y_length=4.2,
            axis_config={"color": INK, "stroke_width": 2},
        ).move_to(np.array([-0.2, -0.6, 0.0]))

        x_lbl = Text("2τ (ms)", font=SERIF, font_size=24, color=INK,
                     slant=ITALIC).move_to(np.array([4.2, -0.6, 0.0]))
        y_lbl = Text("M/M₀", font=SERIF, font_size=24, color=INK,
                     slant=ITALIC).move_to(np.array([-4.5, 1.8, 0.0]))

        self.play(FadeIn(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)

        # Data points from Ch09 exercise: 2τ=50→0.85, 100→0.72, 200→0.52
        data = [(50, 0.85), (100, 0.72), (200, 0.52)]
        data_labels = ["0.85", "0.72", "0.52"]
        dots = VGroup()
        for (tx, ty), dl in zip(data, data_labels):
            dot = Dot(ax.c2p(tx, ty), radius=0.12, color=INK)
            lbl = Text(dl, font=DISPLAY, font_size=20, color=INK
                       ).next_to(dot, UP, buff=0.12)
            dots.add(dot, lbl)

        self.play(LaggedStart(*[FadeIn(m) for m in dots],
                              lag_ratio=0.3, run_time=1.0))

        # Fitted curve: T2 ≈ 305ms; e^(-2τ/305) normalized
        T2 = 305.0
        curve = ax.plot(lambda t: math.exp(-t / T2),
                        x_range=[0, 230], color=TEAL, stroke_width=3)
        self.play(Create(curve), run_time=dur * 0.35)

        t2_fit_lbl = Text("T₂ ≈ 305 ms (illustrative)", font=SERIF,
                          font_size=22, color=TEAL, slant=ITALIC
                          ).move_to(np.array([1.8, 2.0, 0.0]))
        self.play(FadeIn(t2_fit_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 0.5 - 1.0 - dur * 0.35 - 0.4))

class B03_RefocusQuestion(Scene):
    def construct(self):
        d=DUR.get("B03",9); title=Text("WHAT DOES THE π PULSE REVERSE?",font=DISPLAY,font_size=39,color=INK).to_edge(UP)
        yes=Text("REVERSES\nphase ordering",font=SERIF,font_size=30,color=TEAL,line_spacing=1.1).move_to(LEFT*3)
        no=Text("DOES NOT REVERSE\nfrequency offsets · time",font=SERIF,font_size=28,color=CRIMSON,line_spacing=1.1).move_to(RIGHT*3)
        self.play(FadeIn(title),FadeIn(yes),FadeIn(no),run_time=d*.45);self.wait(d*.55)

class B11_PhaseLedger(Scene):
    def construct(self):
        d=DUR.get("B11",11); title=Text("STATIC-OFFSET PHASE LEDGER",font=DISPLAY,font_size=38,color=INK).to_edge(UP)
        first=Text("first wait:  +Δωτ",font=MONO,font_size=32,color=CRIMSON).move_to(UP*.7)
        second=Text("second wait: -Δωτ",font=MONO,font_size=32,color=TEAL).move_to(DOWN*.2)
        net=Text("net at 2τ: 0",font=MONO,font_size=39,color=INK).move_to(DOWN*1.6)
        self.play(FadeIn(title),FadeIn(first),FadeIn(second),run_time=d*.4);self.play(FadeIn(net),run_time=d*.2);self.wait(d*.4)

class B12_QualifiedRecap(Scene):
    def construct(self):
        d=DUR.get("B12",11); title=Text("REFOCUSING IS NOT TIME REVERSAL",font=DISPLAY,font_size=37,color=INK).to_edge(UP)
        ref=Text("correlated static offsets\nrefocus",font=SERIF,font_size=29,color=TEAL,line_spacing=1.1).move_to(LEFT*3)
        loss=Text("changing noise · diffusion · pulse error\nremain",font=SERIF,font_size=27,color=CRIMSON,line_spacing=1.1).move_to(RIGHT*3)
        self.play(FadeIn(title),FadeIn(ref),FadeIn(loss),run_time=d*.45);self.wait(d*.55)

class B13_YourTurn(Scene):
    def construct(self):
        d=DUR.get("B13",12); title=Text("YOUR TURN",font=DISPLAY,font_size=42,color=INK).to_edge(UP)
        q=Text("Δω = 10 rad/s     τ = 0.05 s",font=MONO,font_size=32,color=INK).move_to(UP*.6)
        ans=Text("+0.5 rad  +  (-0.5 rad)  =  0",font=MONO,font_size=36,color=TEAL).move_to(DOWN*.8)
        self.play(FadeIn(title),FadeIn(q),run_time=d*.35);self.wait(d*.3);self.play(FadeIn(ans),run_time=d*.15);self.wait(d*.2)

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        d=DUR.get("B14",8); bg=Rectangle(width=14.4,height=8.2,stroke_width=0).set_fill("#1E1D1A",1)
        title=Text("Un-Blurring Time: The Spin Echo",font=DISPLAY,font_size=44,color="#F3EFE6").move_to(UP*.35)
        by=Text("Kore, in for Humanitarians AI",font=SERIF,font_size=25,color="#D97757").move_to(DOWN*.85)
        series=Text("QUANTUM MECHANICS · VOLUME THREE",font=MONO,font_size=19,color="#B8B1A5").move_to(DOWN*1.45)
        self.add(bg);self.play(FadeIn(title),FadeIn(by),FadeIn(series),run_time=d*.35);self.wait(d*.65)
