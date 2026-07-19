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


# ── B01: COLD OPEN — two isotopes, wildly different half-lives ───────────────
class B01_TwoIsotopes(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        po_lbl = Text("Po-212", font=DISPLAY, font_size=32, color=TEAL).move_to(LEFT * 3.5 + UP * 1.0)
        po_hl = Text("half-life: 3 x 10^-7 s", font=MONO, font_size=24, color=TEAL).move_to(LEFT * 3.5 + UP * 0.2)
        th_lbl = Text("Th-232", font=DISPLAY, font_size=32, color=CRIMSON).move_to(RIGHT * 3.0 + UP * 1.0)
        th_hl = Text("half-life: 1.4 x 10^10 yr", font=MONO, font_size=24, color=CRIMSON).move_to(RIGHT * 3.0 + UP * 0.2)
        divider = Line(UP * 2.0, DOWN * 1.5, color=INK, stroke_width=1.5).move_to(ORIGIN)
        same_lbl = Text("Same mechanism: alpha tunneling", font=SERIF, font_size=22,
                        color=INK, slant=ITALIC).move_to(DOWN * 2.5)
        ratio_lbl = Text("ratio: ~ 10^24", font=MONO, font_size=28, color=INK).move_to(LEFT * 3.5 + DOWN * 1.5)
        self.play(FadeIn(po_lbl), FadeIn(th_lbl), Create(divider), run_time=0.5)
        self.play(FadeIn(po_hl), FadeIn(th_hl), run_time=dur * 0.35)
        self.play(FadeIn(ratio_lbl), run_time=dur * 0.25)
        self.play(FadeIn(same_lbl), divider.animate.scale(0.95), run_time=dur * 0.40)


# ── B02: STILL · ai — four domains (no scene needed) ─────────────────────────


# ── B03: CARD — THE QUESTION (no scene needed) ────────────────────────────────


# ── B04: THE PROBLEM — classical barrier vs quantum tunneling ────────────────
class B04_ClassicalBarrier(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        axes = Axes(x_range=[0, 8, 2], y_range=[-0.5, 3.5, 1],
                    x_length=8.5, y_length=4.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # Barrier: centered around x=4 (mid of range 0-8), height fills most of plot
        # Use fixed coords: barrier spans roughly x=-1.6 to +1.6, y=-1.0 to +2.0
        barrier = Rectangle(width=3.2, height=3.0,
                            fill_color=CRIMSON, fill_opacity=0.25, stroke_width=0)
        barrier.move_to(np.array([0.0, 0.5, 0.0]))
        energy = 1.5
        energy_line = DashedLine(np.array([-4.25, -0.7, 0.0]), np.array([4.25, -0.7, 0.0]),
                                 color=TEAL, stroke_width=2, dash_length=0.2)
        e_lbl = Text("particle energy", font=SERIF, font_size=18, color=TEAL,
                     slant=ITALIC).move_to(np.array([-2.5, -0.35, 0]))
        barrier_lbl = Text("barrier\n30 MeV", font=SERIF, font_size=18, color=CRIMSON,
                           slant=ITALIC).move_to(np.array([0.0, 1.3, 0]))
        classical_lbl = Text("classically: bounce back", font=DISPLAY, font_size=22,
                             color=CRIMSON).move_to(DOWN * 2.8)
        self.play(Create(axes), run_time=0.4)
        self.play(FadeIn(barrier), FadeIn(barrier_lbl), run_time=dur * 0.35)
        self.play(Create(energy_line), FadeIn(e_lbl), run_time=dur * 0.30)
        self.play(FadeIn(classical_lbl), barrier.animate.scale(1.02), run_time=dur * 0.35)


# ── B05: THE PROBLEM — wave function decays exponentially ────────────────────
class B05_WaveDecay(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        axes = Axes(x_range=[0, 8, 2], y_range=[-1.5, 1.5, 0.5],
                    x_length=8.5, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # Oscillating incoming wave, decaying inside, small outgoing wave
        psi_in = axes.plot(lambda x: 0.9 * np.sin(3.5 * x) if x < 2.5 else 0,
                           x_range=[0, 2.5], color=TEAL, stroke_width=3)
        psi_decay = axes.plot(lambda x: 0.85 * np.exp(-0.8 * (x - 2.5)) * np.cos(0.5 * x)
                              if 2.5 <= x <= 5.5 else 0,
                              x_range=[2.5, 5.5], color=CRIMSON, stroke_width=3)
        psi_out = axes.plot(lambda x: 0.12 * np.sin(3.5 * x) if x > 5.5 else 0,
                            x_range=[5.5, 8], color=TEAL, stroke_width=3)
        in_lbl = Text("incoming wave", font=SERIF, font_size=18, color=TEAL,
                      slant=ITALIC).move_to(np.array([-2.5, 1.2, 0]))
        decay_lbl = Text("decays in barrier", font=SERIF, font_size=18, color=CRIMSON,
                         slant=ITALIC).move_to(np.array([0.0, 1.2, 0]))
        out_lbl = Text("tunneled fraction", font=SERIF, font_size=18, color=TEAL,
                       slant=ITALIC).move_to(np.array([3.2, 1.2, 0]))
        self.play(Create(axes), run_time=0.4)
        self.play(Create(psi_in), FadeIn(in_lbl), run_time=dur * 0.30)
        self.play(Create(psi_decay), FadeIn(decay_lbl), run_time=dur * 0.35)
        self.play(Create(psi_out), FadeIn(out_lbl), run_time=dur * 0.35)


# ── B06: THE MECHANISM — Gamow factor formula ────────────────────────────────
class B06_GamowFactor(Scene):
    def construct(self):
        dur = DUR.get("B06", 11.0)
        title = Text("Tunneling probability", font=DISPLAY, font_size=30, color=INK).move_to(UP * 3.0)
        formula_lbl = Text("T ~ exp( -2 * Gamow integral )", font=MONO,
                           font_size=30, color=TEAL).move_to(UP * 1.5)
        gamow_desc = Text("Gamow integral = integral of |p(x)| / h-bar through barrier",
                          font=SERIF, font_size=20, color=INK, slant=ITALIC).move_to(UP * 0.5)
        insight_lbl = Text("small barrier => big T", font=SERIF, font_size=22,
                           color=TEAL, slant=ITALIC).move_to(DOWN * 0.8)
        big_lbl = Text("big barrier => T ~ 0", font=SERIF, font_size=22,
                       color=CRIMSON, slant=ITALIC).move_to(DOWN * 1.8)
        box = Rectangle(width=9.0, height=1.1, stroke_width=2, color=TEAL)
        box.set_fill(TEAL, opacity=0.08).move_to(UP * 1.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(box), FadeIn(formula_lbl), run_time=dur * 0.30)
        self.play(FadeIn(gamow_desc), run_time=dur * 0.25)
        self.play(FadeIn(insight_lbl), box.animate.scale(1.01), run_time=dur * 0.25)
        self.play(FadeIn(big_lbl), run_time=dur * 0.20)


# ── B07: THE MECHANISM — exponential sensitivity ─────────────────────────────
class B07_ExponentialSensitivity(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        axes = Axes(x_range=[0, 5, 1], y_range=[-6, 1, 1],
                    x_length=7.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        log_curve = axes.plot(lambda x: -2 * x, x_range=[0, 4.8], color=TEAL, stroke_width=3.5)
        x_lbl = Text("barrier width L", font=SERIF, font_size=20, color=INK,
                     slant=ITALIC).next_to(axes, RIGHT, buff=0.1)
        y_lbl = Text("log(T)", font=SERIF, font_size=20, color=INK,
                     slant=ITALIC).next_to(axes, UP + LEFT * 3.5, buff=0.1)
        steep_lbl = Text("steep: double L => T^2", font=SERIF, font_size=20,
                         color=TEAL, slant=ITALIC).move_to(np.array([1.5, 2.8, 0]))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(log_curve), run_time=dur * 0.55)
        self.play(FadeIn(steep_lbl), log_curve.animate.set_stroke(width=4.0), run_time=dur * 0.45)


# ── B08: THE MECHANISM — energy sensitivity in alpha decay ───────────────────
class B08_EnergySensitivity(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("Coulomb barrier width depends on energy", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        axes = Axes(x_range=[0, 8, 2], y_range=[0, 4, 1],
                    x_length=8.0, y_length=3.8,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.4)
        # Coulomb potential
        coulomb = axes.plot(lambda x: 3.5 / max(x, 0.3) if x > 0.4 else 4,
                            x_range=[0.5, 7.5], color=INK, stroke_width=2)
        # Two energy levels: high E (thin barrier), low E (thick barrier)
        e_high = DashedLine(axes.c2p(0, 2.2), axes.c2p(7.5, 2.2),
                            color=TEAL, stroke_width=2, dash_length=0.2)
        e_low = DashedLine(axes.c2p(0, 1.1), axes.c2p(7.5, 1.1),
                           color=CRIMSON, stroke_width=2, dash_length=0.2)
        e_high_lbl = Text("higher E: thin barrier", font=SERIF, font_size=18,
                          color=TEAL, slant=ITALIC).move_to(np.array([3.0, 2.5, 0]))
        e_low_lbl = Text("lower E: thick barrier", font=SERIF, font_size=18,
                         color=CRIMSON, slant=ITALIC).move_to(np.array([3.5, 0.3, 0]))
        self.play(FadeIn(title), Create(axes), run_time=0.4)
        self.play(Create(coulomb), run_time=dur * 0.30)
        self.play(Create(e_high), FadeIn(e_high_lbl), run_time=dur * 0.30)
        self.play(Create(e_low), FadeIn(e_low_lbl), run_time=dur * 0.30)
        self.wait(dur * 0.10)


# ── B09: THE IMPLICATION — four applications ─────────────────────────────────
class B09_FourApplications(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Same Gamow factor, four worlds", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.0)
        apps = [
            ("Alpha decay", "nucleus", TEAL),
            ("STM tip", "surface", TEAL),
            ("Stellar fusion", "Sun", TEAL),
            ("Flash memory", "oxide", TEAL),
        ]
        boxes = VGroup()
        for i, (name, sub, col) in enumerate(apps):
            x = -4.5 + (i % 2) * 4.8
            y = 0.6 - (i // 2) * 2.2
            box = Rectangle(width=4.0, height=1.6, stroke_width=0)
            box.set_fill(col, opacity=0.12).move_to(np.array([x, y, 0]))
            lbl = Text(name, font=DISPLAY, font_size=22, color=col).move_to(np.array([x, y + 0.35, 0]))
            sub_lbl = Text(sub, font=SERIF, font_size=18, color=INK,
                           slant=ITALIC).move_to(np.array([x, y - 0.28, 0]))
            boxes.add(box, lbl, sub_lbl)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(boxes), run_time=dur * 0.60)
        self.play(boxes.animate.scale(1.01), run_time=dur * 0.40)


# ── B10: THE EXAMPLE — illustrative electron tunneling ───────────────────────
class B10_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 13.0)
        title = Text("Illustrative: electron tunneling through oxide", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        subtitle = Text("(invented numbers, labeled illustrative)", font=SERIF,
                        font_size=18, color=INK, slant=ITALIC).move_to(UP * 2.45)
        params = [
            ("electron energy", "1 eV"),
            ("barrier height", "5 eV"),
            ("barrier width", "5 angstroms"),
        ]
        param_group = VGroup()
        for i, (k, v) in enumerate(params):
            k_lbl = Text(k + ":", font=SERIF, font_size=22, color=INK,
                         slant=ITALIC).move_to(LEFT * 3.5 + UP * (0.8 - i * 0.7))
            v_lbl = Text(v, font=MONO, font_size=22, color=TEAL).move_to(
                RIGHT * 1.0 + UP * (0.8 - i * 0.7))
            param_group.add(k_lbl, v_lbl)
        result = Text("T ~ e^(-10) ~ 1 in 20,000", font=MONO, font_size=28, color=TEAL)
        result.move_to(DOWN * 1.8)
        highlight = Rectangle(width=7.0, height=0.70, stroke_width=0)
        highlight.set_fill(GOLD, opacity=0.35).move_to(DOWN * 1.8)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(param_group), run_time=dur * 0.35)
        self.play(FadeIn(highlight), FadeIn(result), run_time=dur * 0.35)
        self.wait(dur * 0.30)


# ── B11: RECAP — CARD beat — no scene needed ─────────────────────────────────
