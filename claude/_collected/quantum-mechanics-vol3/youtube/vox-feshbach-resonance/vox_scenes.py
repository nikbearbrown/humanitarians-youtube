"""vox_scenes.py — The Cross-Section That Explodes When a Bound State Is Born
(vox-feshbach-resonance, slate cut, 16:9)

Color law: TEAL = bound / resonance / large scattering length
           CRIMSON = unbound / off-resonance / small scattering length
EXCLUSIONS: no partial-wave expansion, no Levinson theorem, no Efimov states,
            no Feshbach Hamiltonian formalism.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ── B01: COLD OPEN — cesium cross-section spike ───────────────────────────────
class B01_CesiumSpike(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        # Spike graph: cross-section vs magnetic field
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 8, 2],
                    x_length=8.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        x_lbl = SerifLabel("magnetic field", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("cross-section", INK, size=20).next_to(axes, UP + LEFT * 4.5, buff=0.1)
        # Low baseline, then sharp spike at x=5
        import math as _math
        def sigma_low(x):
            return 0.15
        def sigma_spike(x):
            return min(7.5, 2.0 / (abs(x - 5.0) + 0.05))
        baseline_left = axes.plot(sigma_low, x_range=[0, 4.6, 0.1],
                                  color=CRIMSON, stroke_width=2.5)
        baseline_right = axes.plot(sigma_low, x_range=[5.4, 10, 0.1],
                                   color=CRIMSON, stroke_width=2.5)
        spike = axes.plot(sigma_spike, x_range=[4.6, 5.4, 0.02],
                          color=TEAL, stroke_width=3)
        baseline = VGroup(baseline_left, baseline_right)
        spike_lbl = LabelChip("x 10,000 spike", accent=TEAL, size=22)
        spike_lbl.move_to(UP * 2.8)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(baseline), run_time=dur * 0.35)
        self.play(Create(spike), FadeIn(spike_lbl), run_time=dur * 0.40)
        self.wait(dur * 0.25)


# ── B02: COLD OPEN — new bound state appears at zero energy ───────────────────
class B02_BoundStateAppears(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        # Potential well, energy level approaching threshold
        axes = Axes(x_range=[-3, 3, 1], y_range=[-4, 2, 1],
                    x_length=6.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.2},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # Square well potential
        well_pts = [(-2.5, 0), (-1, 0), (-1, -3.5), (1, -3.5), (1, 0), (2.5, 0)]
        well = VMobject(color=INK, stroke_width=3)
        well.set_points_as_corners([axes.c2p(x, y) for x, y in well_pts])
        threshold = DashedLine(axes.c2p(-2.5, 0), axes.c2p(2.5, 0),
                               color=INK, stroke_width=1.5, dash_length=0.18)
        thresh_lbl = SerifLabel("threshold  E = 0", INK, size=20)
        thresh_lbl.next_to(threshold, RIGHT, buff=0.2)
        # Bound state energy level: moves UP to threshold
        level = Line(axes.c2p(-0.8, -2.0), axes.c2p(0.8, -2.0),
                     color=CRIMSON, stroke_width=3)
        level_lbl = SerifLabel("bound state", CRIMSON, size=20)
        level_lbl.next_to(level, RIGHT, buff=0.2)
        appear_lbl = LabelChip("just born at threshold", accent=TEAL, size=22)
        appear_lbl.move_to(DOWN * 2.9)
        self.play(Create(axes), Create(well), Create(threshold),
                  FadeIn(thresh_lbl), run_time=0.6)
        self.play(FadeIn(level), FadeIn(level_lbl), run_time=dur * 0.30)
        self.play(level.animate.put_start_and_end_on(axes.c2p(-0.8, -0.05),
                                                      axes.c2p(0.8, -0.05)),
                  level_lbl.animate.move_to(axes.c2p(0.9, 0.4)),
                  run_time=dur * 0.40)
        self.play(FadeIn(appear_lbl, shift=UP * 0.1), run_time=dur * 0.20)
        self.wait(dur * 0.10)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────


# ── B04: THE PROBLEM — scattering length sets cross-section ──────────────────
class B04_ScatteringLength(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        title = Text("Low-energy scattering", font=DISPLAY,
                     font_size=30, color=INK).move_to(UP * 3.0)
        # sigma = 4*pi*a^2
        formula_parts = [
            ("sigma  =  ", INK), ("4 pi ", INK), ("a", TEAL), ("^2", INK)
        ]
        line = VGroup()
        x = -3.0
        for txt, col in formula_parts:
            t = Text(txt, font=MONO, font_size=30, color=col)
            t.move_to(RIGHT * x + t.width / 2 * RIGHT)
            x += t.width + 0.05
            line.add(t)
        line.center()
        a_lbl = SerifLabel("scattering length", TEAL, size=24)
        a_lbl.move_to(DOWN * 1.8)
        a_arr = Arrow(a_lbl.get_top(), ORIGIN + RIGHT * 0.5,
                      color=TEAL, stroke_width=2, buff=0.1)
        note = Text("Bigger scattering length = bigger effective target.",
                    font=SERIF, font_size=22, color=INK,
                    slant=ITALIC).move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(line), run_time=dur * 0.35)
        self.play(FadeIn(a_lbl), GrowArrow(a_arr), run_time=dur * 0.30)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B05: THE PROBLEM — normally scattering length is finite ──────────────────
class B05_NormalLength(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        # A ruler showing "a few nm"
        axes = Axes(x_range=[0, 12, 3], y_range=[0, 3, 1],
                    x_length=8.0, y_length=2.5,
                    axis_config={"color": INK, "stroke_width": 1.2},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        a_marker = Dot(axes.c2p(2.0, 0), radius=0.18, color=CRIMSON)
        a_lbl = LabelChip("a = 2 nm", accent=CRIMSON, size=22)
        a_lbl.next_to(a_marker, UP, buff=0.3)
        sigma_bar = Rectangle(width=1.2, height=1.5)
        sigma_bar.set_fill(CRIMSON, 0.5).set_stroke(width=0, opacity=0)
        sigma_bar.move_to(axes.c2p(2.0, 0.75))
        sigma_lbl = SerifLabel("sigma = 4pi(2nm)^2 = 50 nm^2", CRIMSON, size=20)
        sigma_lbl.move_to(DOWN * 2.2)
        note = Text("A reasonable size.", font=SERIF, font_size=22,
                    color=INK, slant=ITALIC).move_to(DOWN * 3.0)
        self.play(Create(axes), run_time=0.4)
        self.play(FadeIn(a_marker), FadeIn(a_lbl), run_time=dur * 0.30)
        self.play(GrowFromEdge(sigma_bar, DOWN), run_time=dur * 0.30)
        self.play(FadeIn(sigma_lbl), run_time=dur * 0.20)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=dur * 0.20)


# ── B06: STILL·ai — wave function barely decaying at threshold ───────────────
# STILL beat — no scene class


# ── B07: THE MECHANISM — wave function extending as binding energy shrinks ────
class B07_WaveFunctionLeak(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Potential well + wave function for deep and shallow bound states
        well_left = -2.0
        well_right = 2.0
        well_bot = -3.5
        # Well outline
        well_pts = [(well_left - 1.5, 0), (well_left, 0),
                    (well_left, well_bot), (well_right, well_bot),
                    (well_right, 0), (well_right + 1.5, 0)]
        well = VMobject(color=INK, stroke_width=2.5)
        well.set_points_as_corners([np.array([x, y, 0]) for x, y in well_pts])
        threshold = DashedLine(LEFT * 5.5, RIGHT * 5.5, color=INK,
                               stroke_width=1.2, dash_length=0.15)
        # Deep bound state (stays inside)
        deep_pts = [(well_left + 0.05, 0)]
        for x in np.linspace(well_left, well_right, 30):
            deep_pts.append((x, -1.8 + 0.8 * np.sin(np.pi * (x - well_left) / (well_right - well_left))))
        deep_pts.append((well_right - 0.05, 0))
        # Add decaying tail outside
        for x in np.linspace(well_right, well_right + 1.5, 10):
            deep_pts.append((x, -0.6 * np.exp(-2 * (x - well_right))))
        deep_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        deep_wave.set_points_smoothly([np.array([x, y, 0]) for x, y in deep_pts])
        deep_lbl = LabelChip("deep bound: fast decay", accent=CRIMSON, size=20)
        deep_lbl.move_to(RIGHT * 4.5 + DOWN * 1.5)
        # Shallow bound state (leaks further)
        shallow_pts = []
        for x in np.linspace(well_left, well_right, 30):
            shallow_pts.append((x, -0.3 + 0.35 * np.sin(np.pi * (x - well_left) / (well_right - well_left))))
        # Long tail
        for x in np.linspace(well_right, well_right + 3.0, 20):
            shallow_pts.append((x, 0.28 * np.exp(-0.4 * (x - well_right))))
        shallow_wave = VMobject(color=TEAL, stroke_width=2.5)
        shallow_wave.set_points_smoothly([np.array([x, y, 0]) for x, y in shallow_pts])
        shallow_lbl = LabelChip("shallow bound: long tail", accent=TEAL, size=20)
        shallow_lbl.move_to(RIGHT * 4.5 + UP * 0.8)
        self.play(Create(well), Create(threshold), run_time=0.5)
        self.play(Create(deep_wave), FadeIn(deep_lbl), run_time=dur * 0.35)
        self.play(Create(shallow_wave), FadeIn(shallow_lbl), run_time=dur * 0.35)
        self.wait(dur * 0.30)


# ── B08: THE MECHANISM — at threshold, wave function never decays ─────────────
class B08_ThresholdDivergence(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        # Binding energy vs decay length (inverse relation)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 7, 1],
                    x_length=6.0, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(LEFT * 0.5 + DOWN * 0.3)
        # decay length ~ 1/sqrt(binding energy)
        import math as _math2
        def decay_len(x):
            return min(6.5, 1.5 / _math2.sqrt(x + 0.01))
        curve = axes.plot(decay_len, x_range=[0.0, 5.0, 0.05],
                          color=TEAL, stroke_width=3)
        x_lbl = SerifLabel("binding energy", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("decay length", INK, size=20).next_to(axes, UP + LEFT * 3.5, buff=0.1)
        thresh_x = axes.c2p(0.1, 0)
        diverge_lbl = LabelChip("diverges at threshold", accent=TEAL, size=22)
        diverge_lbl.move_to(LEFT * 3.5 + UP * 2.8)
        arrow_to = Arrow(diverge_lbl.get_bottom(), axes.c2p(0.15, 6.2),
                         color=TEAL, stroke_width=2, buff=0.05)
        equals_label = Text("decay length = scattering length",
                            font=SERIF, font_size=20, color=INK,
                            slant=ITALIC).move_to(RIGHT * 4.0 + DOWN * 0.8)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(curve), run_time=dur * 0.40)
        self.play(FadeIn(diverge_lbl), GrowArrow(arrow_to), run_time=dur * 0.25)
        self.play(FadeIn(equals_label, shift=UP * 0.1), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B09: THE MECHANISM — scattering length vs well depth ─────────────────────
class B09_ScatteringLengthPlot(Scene):
    def construct(self):
        dur = DUR.get("B09", 11.0)
        axes = Axes(x_range=[0, 10, 2], y_range=[-5, 5, 2],
                    x_length=8.0, y_length=5.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # Scattering length: diverges at each threshold crossing
        # Simulate one divergence at x=3 and x=7
        import math
        def scatt_len(x):
            # Diverge at x=3
            if 2.5 < x < 3.5:
                val = -3.0 / (x - 3.0) if x != 3.0 else 99
                return max(-4.8, min(4.8, val))
            elif x < 3:
                return -0.5 + 0.3 * x
            elif x < 7:
                return 0.4 * (x - 3.0) - 1.5
            else:
                return 0.3
        def scatt_left(x):
            if x < 2.5:
                return -0.5 + 0.3 * x
            else:
                val = -3.0 / (x - 3.0)
                return max(-4.8, min(4.8, val))
        def scatt_right(x):
            if x > 3.5:
                if x < 7:
                    return 0.4 * (x - 3.0) - 1.5
                return 0.3
            else:
                val = -3.0 / (x - 3.0)
                return max(-4.8, min(4.8, val))
        left_curve = axes.plot(scatt_left, x_range=[0, 2.7, 0.05],
                               color=CRIMSON, stroke_width=2.5)
        right_curve = axes.plot(scatt_right, x_range=[3.3, 10, 0.05],
                                color=TEAL, stroke_width=2.5)
        # Vertical dashed line at threshold x=3
        thresh_line = DashedLine(axes.c2p(3.0, -4.8), axes.c2p(3.0, 4.8),
                                  color=INK, stroke_width=1.5, dash_length=0.15)
        thresh_lbl = SerifLabel("new bound state", INK, size=20)
        thresh_lbl.move_to(axes.c2p(3.0, -5.3))
        x_lbl = SerifLabel("well depth", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("scattering length", INK, size=20).next_to(axes, UP + LEFT * 4.5, buff=0.1)
        inf_pos = LabelChip("+inf", accent=TEAL, size=22).move_to(axes.c2p(2.8, 4.5))
        inf_neg = LabelChip("-inf", accent=CRIMSON, size=22).move_to(axes.c2p(3.3, -4.5))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(left_curve), run_time=dur * 0.25)
        self.play(Create(thresh_line), FadeIn(thresh_lbl), run_time=dur * 0.15)
        self.play(FadeIn(inf_pos), FadeIn(inf_neg), run_time=dur * 0.15)
        self.play(Create(right_curve), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B10: THE MECHANISM — section CARD, no scene class ────────────────────────


# ── B11: THE IMPLICATION — Feshbach resonance as a dial ──────────────────────
class B11_FeshbachDial(Scene):
    def construct(self):
        dur = DUR.get("B11", 10.0)
        title = Text("Feshbach resonance: magnetic field as a dial", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Horizontal dial: field B on x axis, scattering length on y
        axes = Axes(x_range=[0, 10, 2], y_range=[-3, 3, 1],
                    x_length=8.0, y_length=3.5,
                    axis_config={"color": INK, "stroke_width": 1.2},
                    tips=False)
        axes.move_to(DOWN * 0.5)
        def a_of_B_left(B):
            if B < 4.2:
                return -0.3 + 0.1 * B
            val = -2.0 / (B - 5.0)
            return max(-2.9, min(2.9, val))
        def a_of_B_right(B):
            if B > 5.8:
                return 0.3
            val = -2.0 / (B - 5.0)
            return max(-2.9, min(2.9, val))
        lc = axes.plot(a_of_B_left, x_range=[0, 4.3, 0.05],
                       color=CRIMSON, stroke_width=2.5)
        rc = axes.plot(a_of_B_right, x_range=[5.7, 10, 0.05],
                       color=TEAL, stroke_width=2.5)
        res_line = DashedLine(axes.c2p(5.0, -2.9), axes.c2p(5.0, 2.9),
                               color=INK, stroke_width=1.5, dash_length=0.15)
        res_lbl = LabelChip("resonance", accent=TEAL, size=20)
        res_lbl.next_to(res_line, UP, buff=0.2)
        x_lbl = SerifLabel("magnetic field B", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("scattering length a", INK, size=20).next_to(axes, UP + LEFT * 4.5, buff=0.1)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(lc), Create(rc), run_time=dur * 0.40)
        self.play(Create(res_line), FadeIn(res_lbl), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B12: THE IMPLICATION — BEC and ideal gas ──────────────────────────────────
class B12_BECDial(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        title = Text("Setting interactions with the magnetic dial", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Two end states
        inf_state = VGroup(
            LabelChip("a = infinity", accent=TEAL, size=24),
            Text("maximum interactions", font=SERIF, font_size=22,
                 color=TEAL, slant=ITALIC),
            Text("strongly-correlated BEC", font=DISPLAY, font_size=22,
                 color=TEAL),
        )
        inf_state.arrange(DOWN, buff=0.3).move_to(LEFT * 3.2 + DOWN * 0.5)
        zero_state = VGroup(
            LabelChip("a = 0", accent=CRIMSON, size=24),
            Text("nearly zero interactions", font=SERIF, font_size=22,
                 color=CRIMSON, slant=ITALIC),
            Text("nearly ideal gas", font=DISPLAY, font_size=22,
                 color=CRIMSON),
        )
        zero_state.arrange(DOWN, buff=0.3).move_to(RIGHT * 3.2 + DOWN * 0.5)
        divider = Line(UP * 2.0, DOWN * 2.5, color=INK, stroke_width=1.5)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(inf_state), run_time=dur * 0.40)
        self.play(FadeIn(zero_state), run_time=dur * 0.35)
        self.wait(dur * 0.25)


# ── B13: THE EXAMPLE — illustrative numbers ───────────────────────────────────
class B13_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B13", 18.0)
        title = Text("Illustrative: spherical well, radius 1 nm", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.1)
        subtitle = Text("(invented numbers, labeled illustrative)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        rows = [
            ("V0 = 0.3 eV", "no bound state", "sigma = 0.08 nm^2", CRIMSON),
            ("V0 = 0.38 eV", "1st bound state AT threshold", "sigma = 10^7 nm^2 (!)", TEAL),
            ("V0 = 0.42 eV", "bound 0.01 eV below threshold", "sigma = 1800 nm^2", INK),
        ]
        row_groups = VGroup()
        for i, (v0, note, sig, col) in enumerate(rows):
            y = 1.2 - i * 1.5
            r = VGroup(
                Text(v0, font=MONO, font_size=20, color=col).move_to(LEFT * 4.5 + UP * y),
                SerifLabel(note, col, size=18).move_to(LEFT * 0.5 + UP * y),
                Text(sig, font=MONO, font_size=20, color=col).move_to(RIGHT * 4.0 + UP * y),
            )
            row_groups.add(r)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        for rg in row_groups:
            self.play(FadeIn(rg, shift=RIGHT * 0.3), run_time=dur * 0.22)
        self.wait(dur * 0.12)


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
