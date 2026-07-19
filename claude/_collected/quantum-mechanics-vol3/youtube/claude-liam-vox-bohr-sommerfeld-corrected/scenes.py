"""vox_scenes.py — Zero-Point Energy Is a Patch of Phase Space
(vox-bohr-sommerfeld, slate cut, 16:9)

Color law: TEAL = allowed/quantized orbits/nonzero area
           CRIMSON = classical prediction/zero zero-point energy
EXCLUSIONS: no Airy-function connection formulas, no action-integral
            evaluation, no Langer correction.
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


# ── B01: COLD OPEN — oscillator traces an ellipse in phase space ──────────────
class LegacyPhaseSpaceEllipseOpening(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        # Phase space axes: x horizontal, p vertical
        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-3.5, 3.5, 1],
                    x_length=5.5, y_length=5.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(ORIGIN)
        x_lbl = SerifLabel("position x", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("momentum p", INK, size=20).next_to(axes, UP + LEFT * 2.5, buff=0.1)
        # Draw one ellipse (classical orbit)
        ellipse = Ellipse(width=4.0, height=3.0, color=CRIMSON, stroke_width=2.5)
        ellipse.move_to(ORIGIN)
        classical_lbl = SerifLabel("classical: any size", CRIMSON, size=20)
        classical_lbl.move_to(DOWN * 3.2 + LEFT * 1.5)
        dot = Dot(ORIGIN + UP * 1.0, radius=0.15, color=CRIMSON)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(ellipse), run_time=dur * 0.40)
        self.play(FadeIn(dot), FadeIn(classical_lbl), run_time=dur * 0.35)
        self.wait(dur * 0.25)


# ── B02: COLD OPEN — quantum requires nonzero minimum area ────────────────────
class B02_QuantumNested(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        axes = Axes(x_range=[-4, 4, 1], y_range=[-4, 4, 1],
                    x_length=5.5, y_length=5.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(ORIGIN)
        x_lbl = SerifLabel("x", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("p", INK, size=20).next_to(axes, UP + LEFT * 2.5, buff=0.1)
        # Three nested ellipses: n=0 (smallest), n=1, n=2
        e0 = Ellipse(width=1.6, height=1.2, color=TEAL, stroke_width=2.5).move_to(ORIGIN)
        e0_lbl = Text("n=0", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 3.0 + DOWN * 0.5)
        e1 = Ellipse(width=2.8, height=2.1, color=TEAL, stroke_width=2.0).move_to(ORIGIN)
        e1_lbl = Text("n=1", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 3.0 + UP * 0.8)
        e2 = Ellipse(width=3.8, height=2.9, color=TEAL, stroke_width=1.5).move_to(ORIGIN)
        e2_lbl = Text("n=2", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 3.0 + UP * 2.0)
        no_point = LabelChip("semiclassical energy shells — not particle paths", accent=TEAL, size=20)
        no_point.move_to(DOWN * 3.2)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(e0), FadeIn(e0_lbl), run_time=dur * 0.20)
        self.play(Create(e1), FadeIn(e1_lbl), run_time=dur * 0.15)
        self.play(Create(e2), FadeIn(e2_lbl), run_time=dur * 0.15)
        self.play(FadeIn(no_point), run_time=dur * 0.30)
        self.wait(dur * 0.20)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────

class B03_HalfUnitQuestion(Scene):
    def construct(self):
        dur = DUR.get("B03", 8.0)
        title = Text("THE QUESTION", font=MONO, font_size=18, color=CRIMSON).to_edge(UP)
        q1 = Text("Why does the smallest WKB ellipse", font=DISPLAY, font_size=31, color=INK)
        q2 = Text("retain half a quantum of action?", font=DISPLAY, font_size=31, color=TEAL)
        group = VGroup(q1, q2).arrange(DOWN, buff=0.55).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(group), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B04: THE PROBLEM — original Bohr-Sommerfeld rule ─────────────────────────
class B04_OldRule(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        title = Text("Bohr-Sommerfeld (1913-1916)", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Original rule
        old_formula = Text("∮ p dx = n·h,    n = 0, 1, 2, ...",
                           font=MONO, font_size=28, color=CRIMSON).move_to(UP * 1.4)
        old_lbl = SerifLabel("integer multiples of h — classical orbits", CRIMSON, size=20)
        old_lbl.move_to(UP * 0.3)
        # n=0 case
        n0_case = Text("n = 0  →  orbit area = 0  →  zero energy",
                       font=MONO, font_size=24, color=CRIMSON).move_to(DOWN * 0.9)
        n0_note = SerifLabel("particle at rest — classically fine", CRIMSON, size=20)
        n0_note.move_to(DOWN * 1.9)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(old_formula), run_time=dur * 0.30)
        self.play(FadeIn(old_lbl), run_time=dur * 0.20)
        self.play(FadeIn(n0_case), run_time=dur * 0.25)
        self.play(FadeIn(n0_note), run_time=dur * 0.25)


# ── B05: THE PROBLEM — actual QM gives (n+½) ─────────────────────────────────
class B05_ActualSpectrum(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        title = Text("Actual quantum spectrum", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        correct = Text("E_n = (n + ½) ℏω", font=MONO, font_size=32, color=TEAL)
        correct.move_to(UP * 1.4)
        wrong = Text("NOT n · ℏω", font=MONO, font_size=28, color=CRIMSON)
        wrong.move_to(UP * 0.2)
        half_lbl = SerifLabel("the ½ is real — and it's missing from the original rule", INK, size=20)
        half_lbl.move_to(DOWN * 1.0)
        n0_e = Text("n = 0:  E₀ = ½ ℏω  (not zero)", font=MONO, font_size=24, color=TEAL)
        n0_e.move_to(DOWN * 2.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(correct), run_time=dur * 0.30)
        self.play(FadeIn(wrong), run_time=dur * 0.25)
        self.play(FadeIn(half_lbl), run_time=dur * 0.20)
        self.play(FadeIn(n0_e), run_time=dur * 0.25)


# ── B06: THE PROBLEM — STILL·ai beat, no scene class ─────────────────────────

class B06_SoftTurningPoints(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)
        title = Text("Two soft turning points", font=DISPLAY, font_size=28, color=INK).to_edge(UP)
        axes = Axes(x_range=[-3, 3, 1], y_range=[0, 4, 1], x_length=7.0, y_length=3.5,
                    axis_config={"color": INK, "stroke_width": 1.2}, tips=False).shift(DOWN * 0.5)
        potential = axes.plot(lambda x: x ** 2, x_range=[-2, 2], color=INK, stroke_width=2.5)
        level = axes.plot(lambda x: 1.5, x_range=[-1.22, 1.22], color=TEAL, stroke_width=2.5)
        dots = VGroup(Dot(axes.c2p(-1.22, 1.5), color=CRIMSON), Dot(axes.c2p(1.22, 1.5), color=CRIMSON))
        note = Text("oscillatory inside · decaying outside", font=SERIF, font_size=23, color=SLATE).to_edge(DOWN)
        self.play(FadeIn(title), FadeIn(axes), Create(potential), Create(level), FadeIn(dots), run_time=1.0)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(max(0.1, dur - 1.5))


# ── B07: THE MECHANISM — Maslov index at each turning point ──────────────────
class B07_MaslovIndex(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)
        title = Text("Two soft turning points → Maslov index 2", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        # Schematic of potential with turning points
        axes = Axes(x_range=[-3, 3, 1], y_range=[0, 4, 1],
                    x_length=6.0, y_length=3.0,
                    axis_config={"color": INK, "stroke_width": 1.2},
                    tips=False)
        axes.move_to(DOWN * 0.8)
        potential = axes.plot(lambda x: x ** 2, x_range=[-2.0, 2.0, 0.05],
                              color=INK, stroke_width=2.5)
        # Energy level
        e_line = axes.plot(lambda x: 1.5, x_range=[-1.22, 1.22, 0.05],
                           color=TEAL, stroke_width=2.5)
        # Turning points
        tp_left = Dot(axes.c2p(-1.22, 1.5), radius=0.18, color=CRIMSON)
        tp_right = Dot(axes.c2p(1.22, 1.5), radius=0.18, color=CRIMSON)
        tp_lbl = LabelChip("closed-orbit correction: μ = 2", accent=CRIMSON, size=20)
        tp_lbl.move_to(DOWN * 3.0)
        x_lbl = SerifLabel("x", INK, size=18).next_to(axes, RIGHT, buff=0.1)
        v_lbl = SerifLabel("V(x)", INK, size=18).next_to(axes, UP + LEFT * 3.0, buff=0.1)
        self.play(FadeIn(title), Create(axes), FadeIn(x_lbl), FadeIn(v_lbl), run_time=0.5)
        self.play(Create(potential), run_time=dur * 0.25)
        self.play(Create(e_line), run_time=dur * 0.20)
        self.play(FadeIn(tp_left), FadeIn(tp_right), run_time=dur * 0.20)
        self.play(FadeIn(tp_lbl), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B08: THE MECHANISM — two turning points give h/2 ─────────────────────────
class B08_TwoTurningPoints(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("Invariant result: the half-unit correction", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        step1 = Text("closed-orbit Maslov index:  mu = 2",
                     font=MONO, font_size=22, color=CRIMSON).move_to(UP * 1.6)
        step2 = Text("action shift:  mu/4 = 1/2",
                     font=MONO, font_size=22, color=CRIMSON).move_to(UP * 0.7)
        divline = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=1.2).move_to(ORIGIN)
        total = Text("J = (n + mu/4)h = (n + 1/2)h",
                     font=MONO, font_size=24, color=TEAL).move_to(DOWN * 0.8)
        new_rule = LabelChip("∮ p dx = (n + ½)h", accent=TEAL, size=24)
        new_rule.move_to(DOWN * 2.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(step1), run_time=dur * 0.20)
        self.play(FadeIn(step2), run_time=dur * 0.20)
        self.play(Create(divline), run_time=0.2)
        self.play(FadeIn(total), run_time=dur * 0.20)
        self.play(FadeIn(new_rule), run_time=dur * 0.25)
        self.wait(dur * 0.15)


# ── B09: THE MECHANISM — n=0: orbit area = h/2, not zero ──────────────────────
class B09_GroundStateArea(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Ground state: the half is everything", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # n=0 case
        n0 = Text("n = 0:   (0 + ½)·h  =  h/2", font=MONO, font_size=28, color=TEAL)
        n0.move_to(UP * 1.5)
        not_zero = LabelChip("orbit area ≠ 0", accent=TEAL, size=24)
        not_zero.move_to(UP * 0.3)
        energy_eq = Text("E₀  =  ½ ℏω  =  ½ · (h/2π) · ω",
                         font=MONO, font_size=24, color=TEAL).move_to(DOWN * 0.7)
        zpe_note = SerifLabel("zero-point energy: the mandatory half-unit of action", TEAL, size=20)
        zpe_note.move_to(DOWN * 2.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(n0), run_time=dur * 0.30)
        self.play(FadeIn(not_zero), run_time=dur * 0.20)
        self.play(FadeIn(energy_eq), run_time=dur * 0.25)
        self.play(FadeIn(zpe_note), run_time=dur * 0.25)


# ── B10: THE MECHANISM — section CARD, no scene class ────────────────────────

class B10_SemiclassicalScope(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)
        title = Text("SEMICLASSICAL PICTURE ≠ EXACT STATE", font=DISPLAY, font_size=28, color=INK).to_edge(UP)
        left = VGroup(Text("ellipse", font=DISPLAY, font_size=28, color=TEAL),
                      Text("classical energy shell\nused by WKB", font=SERIF, font_size=23, color=INK, line_spacing=1.3)).arrange(DOWN, buff=0.5).move_to(LEFT * 3)
        right = VGroup(Text("ground state", font=DISPLAY, font_size=28, color=CRIMSON),
                       Text("quantum wavefunction\nnot a definite orbit", font=SERIF, font_size=23, color=INK, line_spacing=1.3)).arrange(DOWN, buff=0.5).move_to(RIGHT * 3)
        divider = Line(UP * 2, DOWN * 2, color=SLATE)
        self.play(FadeIn(title), FadeIn(left), FadeIn(right), Create(divider), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B11: THE IMPLICATION — uncertainty principle ─────────────────────────────
class B11_UncertaintyPrinciple(Scene):
    def construct(self):
        dur = DUR.get("B11", 10.0)
        title = Text("Exact cross-check: no zero-spread phase-space point", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        # Phase space picture: can't shrink orbit to point
        classic_pt = VGroup(
            LabelChip("classical", accent=CRIMSON, size=22),
            SerifLabel("point in phase space: Δx = 0, Δp = 0", CRIMSON, size=20),
            Text("both zero: allowed classically", font=SERIF, font_size=20,
                 color=CRIMSON, slant=ITALIC),
        )
        classic_pt.arrange(DOWN, buff=0.25).move_to(LEFT * 3.0 + DOWN * 0.5)
        quantum_pt = VGroup(
            LabelChip("quantum", accent=TEAL, size=22),
            SerifLabel("state must obey Δx Δp ≥ ℏ/2", TEAL, size=20),
            Text("both zero: forbidden", font=SERIF, font_size=20,
                 color=TEAL, slant=ITALIC),
        )
        quantum_pt.arrange(DOWN, buff=0.25).move_to(RIGHT * 3.0 + DOWN * 0.5)
        divider = Line(UP * 2.0, DOWN * 2.2, color=INK, stroke_width=1.5)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(classic_pt), run_time=dur * 0.40)
        self.play(FadeIn(quantum_pt), run_time=dur * 0.35)
        self.wait(dur * 0.25)


# ── B12: THE IMPLICATION — liquid helium, Casimir ───────────────────────────
class B12_YourTurn(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        title = Text("YOUR TURN", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        items = [("omega", "10^14 rad/s", INK),
                 ("h-bar", "6.58 × 10^-16 eV s", TEAL),
                 ("calculate", "E0 = (1/2) h-bar omega", CRIMSON)]
        row_group = VGroup()
        for i, (item, desc, col) in enumerate(items):
            y = 1.2 - i * 1.4
            r = VGroup(
                LabelChip(item, accent=col, size=20).move_to(LEFT * 3.5 + UP * y),
                SerifLabel(desc, col, size=18).move_to(RIGHT * 1.5 + UP * y),
            )
            row_group.add(r)
        self.play(FadeIn(title), run_time=0.4)
        for rg in row_group:
            self.play(FadeIn(rg, shift=RIGHT * 0.2), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B13: THE EXAMPLE — illustrative numbers ───────────────────────────────────
class B13_YourTurnAnswer(Scene):
    def construct(self):
        dur = DUR.get("B13", 16.0)
        title = Text("ANSWER: ABOUT 33 meV", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.1)
        subtitle = Text("one-half h-bar omega", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        rows = [("0.5 × 6.58 × 10^-16", "× 10^14 eV", INK),
                ("= 0.0329 eV", "", CRIMSON),
                ("= 32.9 meV", "approximately 33 meV", TEAL)]
        row_groups = VGroup()
        for i, (expr, note, col) in enumerate(rows):
            y = 1.0 - i * 1.5
            r = VGroup(
                Text(expr, font=MONO, font_size=20, color=col).move_to(LEFT * 2.5 + UP * y),
                SerifLabel(note, col, size=18).move_to(RIGHT * 2.8 + UP * y),
            )
            row_groups.add(r)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        for rg in row_groups:
            self.play(FadeIn(rg, shift=RIGHT * 0.3), run_time=dur * 0.25)
        self.wait(dur * 0.10)


class B14_CorrectTitleOutro(Scene):
    def construct(self):
        dur = DUR.get("B14", 5.0)
        self.camera.background_color = "#201F1C"
        title = Text("Zero-Point Energy as a Phase-Space Patch", font=DISPLAY,
                     font_size=31, color="#F2EFE8")
        credit = Text("Liam, in for Bear", font=SERIF, font_size=20,
                      color="#D97757").next_to(title, DOWN, buff=0.45)
        series = Text("QUANTUM MECHANICS  ·  VOLUME THREE", font=MONO,
                      font_size=14, color="#AAA49A").next_to(credit, DOWN, buff=0.35)
        self.play(FadeIn(title), FadeIn(credit), FadeIn(series), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
