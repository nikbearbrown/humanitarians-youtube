"""vox_scenes.py — The phasor that spins but never changes anything
(vox-phasor-stationary, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B08 is STILL·ai — no scene here.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law: TEAL = the rotating phasor (unit length, truth/kept);
CRIMSON = the naive expectation that rotation must change something.
GOLD = single highlight marker (probability bar height, B07 only).

Exclusions: no TDSE derivation, no superposition/interference, single eigenstate only.
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


def _dur(bid, fallback=8.0):
    return DUR.get(bid, fallback)


# ── B01 CARD — title card (COLD OPEN) ────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("The phasor that spins\nbut never changes anything",
                     font=DISPLAY, color=INK, font_size=44, weight="BOLD",
                     line_spacing=1.2)
        title.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.6)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(d - 1.4)


# ── B02 CARD — THE QUESTION ───────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        d = _dur("B02", 10.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.move_to(UP * 2.8)
        dek = Text("e^{-iEt/hbar} rotates without stop.\n|psi|^2 never moves. Why?",
                   font=SERIF, color=INK, font_size=36, line_spacing=1.3)
        dek.move_to(ORIGIN)
        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(dek), run_time=0.8)
        self.wait(d - 1.3)


# ── B03 GRAPHIC — complex plane with rotating arrow ───────────────────────────
class B03_ComplexPlane(Scene):
    def construct(self):
        d = _dur("B03", 11.0)
        # axes
        ax_x = Line(LEFT * 2.8, RIGHT * 2.8, color=INK, stroke_width=1.5)
        ax_y = Line(DOWN * 2.8, UP * 2.8, color=INK, stroke_width=1.5)
        ax_x.move_to(LEFT * 1.5)
        ax_y.move_to(LEFT * 1.5)
        circle = Circle(radius=1.8, color=TEAL, stroke_width=2.5)
        circle.move_to(LEFT * 1.5)
        re_label = Text("Re", font=SERIF, color=INK, font_size=24)
        re_label.next_to(ax_x, RIGHT, buff=0.15)
        im_label = Text("Im", font=SERIF, color=INK, font_size=24)
        im_label.next_to(ax_y, UP, buff=0.15)
        # phasor arrow
        angle = ValueTracker(0.0)
        phasor = always_redraw(lambda: Arrow(
            LEFT * 1.5,
            LEFT * 1.5 + RIGHT * 1.8 * np.cos(angle.get_value()) + UP * 1.8 * np.sin(angle.get_value()),
            color=TEAL, buff=0, stroke_width=4, tip_length=0.22
        ))
        psi_label = Text("psi", font=SERIF, color=TEAL, font_size=30, slant=ITALIC)
        psi_label.move_to(LEFT * 1.5 + RIGHT * 0.6 + UP * 0.5)
        # right panel: label
        panel_title = Text("The wavefunction lives\nin the complex plane",
                           font=SERIF, color=INK, font_size=28, line_spacing=1.2)
        panel_title.move_to(RIGHT * 3.2)
        self.play(Create(ax_x), Create(ax_y), run_time=0.5)
        self.play(Create(circle), run_time=0.6)
        self.play(FadeIn(re_label), FadeIn(im_label), run_time=0.4)
        self.play(GrowArrow(phasor), FadeIn(psi_label), run_time=0.7)
        self.play(FadeIn(panel_title), run_time=0.5)
        self.play(angle.animate.set_value(TAU * 1.1), run_time=d - 2.7, rate_func=linear)


# ── B04 GRAPHIC — unit-arrow: modulus = 1 always ─────────────────────────────
class B04_UnitArrow(Scene):
    def construct(self):
        d = _dur("B04", 10.0)
        circle = Circle(radius=2.0, color=TEAL, stroke_width=2.5)
        circle.move_to(LEFT * 1.8)
        dot_center = Dot(LEFT * 1.8, color=INK, radius=0.07)
        # label |e^{-iEt/hbar}| = 1
        eq_label = Text("|e^(-iEt/hbar)| = 1", font=MONO, color=INK, font_size=30)
        eq_label.move_to(RIGHT * 3.0 + UP * 1.0)
        angle = ValueTracker(0.3)
        phasor = always_redraw(lambda: Arrow(
            LEFT * 1.8,
            LEFT * 1.8 + RIGHT * 2.0 * np.cos(angle.get_value()) + UP * 2.0 * np.sin(angle.get_value()),
            color=TEAL, buff=0, stroke_width=5, tip_length=0.25
        ))
        length_label = always_redraw(lambda: Text("length = 1", font=MONO,
                                                   color=TEAL, font_size=26).move_to(RIGHT * 3.0 + DOWN * 0.4))
        note = Text("No matter the angle,\nthe arrow never shortens\nor lengthens.",
                    font=SERIF, color=INK, font_size=22, line_spacing=1.2)
        note.move_to(RIGHT * 2.5 + DOWN * 1.6)
        self.play(Create(circle), FadeIn(dot_center), run_time=0.6)
        self.play(GrowArrow(phasor), run_time=0.6)
        self.play(FadeIn(eq_label), FadeIn(length_label), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.play(angle.animate.set_value(TAU + 0.3), run_time=d - 2.2, rate_func=linear)


# ── B05 GRAPHIC — modulus squared: psi* x psi = 1 ────────────────────────────
class B05_ModulusSquared(Scene):
    def construct(self):
        d = _dur("B05", 12.0)
        # show psi and psi* arrows rotating in opposite directions
        circle = Circle(radius=1.6, color=SLATE, stroke_width=1.5)
        circle.move_to(ORIGIN)
        dot_c = Dot(ORIGIN, color=INK, radius=0.07)
        angle = ValueTracker(0.5)
        psi_arrow = always_redraw(lambda: Arrow(
            ORIGIN,
            RIGHT * 1.6 * np.cos(angle.get_value()) + UP * 1.6 * np.sin(angle.get_value()),
            color=TEAL, buff=0, stroke_width=4, tip_length=0.22
        ))
        psi_conj = always_redraw(lambda: Arrow(
            ORIGIN,
            RIGHT * 1.6 * np.cos(-angle.get_value()) + UP * 1.6 * np.sin(-angle.get_value()),
            color=CRIMSON, buff=0, stroke_width=4, tip_length=0.22
        ))
        psi_txt = Text("psi", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        psi_txt.move_to(LEFT * 2.8 + UP * 1.2)
        psistar_txt = Text("psi*", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        psistar_txt.move_to(LEFT * 2.8 + DOWN * 1.2)
        product_box = Rectangle(width=4.2, height=1.0)
        product_box.set_fill(GOLD, 0.35).set_stroke(width=0, opacity=0)
        product_box.move_to(RIGHT * 3.5)
        product_text = Text("|psi|^2 = psi* x psi = 1", font=MONO, color=INK, font_size=28)
        product_text.move_to(RIGHT * 3.5)
        self.play(Create(circle), FadeIn(dot_c), run_time=0.5)
        self.play(GrowArrow(psi_arrow), GrowArrow(psi_conj), run_time=0.7)
        self.play(FadeIn(psi_txt), FadeIn(psistar_txt), run_time=0.4)
        self.play(FadeIn(product_box), FadeIn(product_text), run_time=0.6)
        self.play(angle.animate.set_value(TAU + 0.5), run_time=d - 2.2, rate_func=linear)


# ── B06 GRAPHIC — counter-rotating pair, product stays at real=1 ──────────────
class B06_CounterRotate(Scene):
    def construct(self):
        d = _dur("B06", 11.0)
        circle = Circle(radius=1.8, color=SLATE, stroke_width=1.5)
        circle.move_to(ORIGIN)
        dot_c = Dot(ORIGIN, color=INK, radius=0.07)
        angle = ValueTracker(0.0)
        psi_a = always_redraw(lambda: Arrow(
            ORIGIN,
            RIGHT * 1.8 * np.cos(angle.get_value()) + UP * 1.8 * np.sin(angle.get_value()),
            color=TEAL, buff=0, stroke_width=5, tip_length=0.25
        ))
        psi_c = always_redraw(lambda: Arrow(
            ORIGIN,
            RIGHT * 1.8 * np.cos(-angle.get_value()) + UP * 1.8 * np.sin(-angle.get_value()),
            color=CRIMSON, buff=0, stroke_width=5, tip_length=0.25
        ))
        product_dot = Dot(RIGHT * 1.8, color=INK, radius=0.14)
        product_label = Text("product = 1\n(always real)", font=MONO, color=INK, font_size=26,
                             line_spacing=1.1)
        product_label.move_to(RIGHT * 3.8 + UP * 0.5)
        self.play(Create(circle), FadeIn(dot_c), run_time=0.5)
        self.play(GrowArrow(psi_a), GrowArrow(psi_c), run_time=0.7)
        self.play(FadeIn(product_dot), FadeIn(product_label), run_time=0.5)
        self.play(angle.animate.set_value(TAU * 1.2), run_time=d - 1.7, rate_func=linear)


# ── B07 GRAPHIC — spatial part vs time phase: compare ────────────────────────
class B07_SpatialVsPhase(Scene):
    def construct(self):
        d = _dur("B07", 11.0)
        # left panel: spatial shape (a Gaussian-like curve)
        left_title = Text("psi(x) — spatial shape", font=SERIF, color=INK,
                          font_size=26, slant=ITALIC)
        left_title.move_to(LEFT * 3.5 + UP * 2.8)
        ax_left = Axes(
            x_range=[-3, 3, 1], y_range=[0, 1.2, 0.5],
            x_length=4.5, y_length=2.5,
            axis_config={"color": INK, "stroke_width": 1.5,
                         "include_tip": False}
        )
        ax_left.move_to(LEFT * 3.2 + DOWN * 0.3)
        curve = ax_left.plot(lambda x: np.exp(-x**2), color=TEAL, stroke_width=3)
        # right panel: unit circle (the phase factor)
        right_title = Text("e^{-iEt/hbar} — pure phase", font=SERIF, color=INK,
                           font_size=26, slant=ITALIC)
        right_title.move_to(RIGHT * 3.0 + UP * 2.8)
        circle_r = Circle(radius=1.4, color=CRIMSON, stroke_width=2.5)
        circle_r.move_to(RIGHT * 3.0 + DOWN * 0.3)
        angle_r = ValueTracker(0.0)
        arrow_r = always_redraw(lambda: Arrow(
            RIGHT * 3.0 + DOWN * 0.3,
            RIGHT * 3.0 + DOWN * 0.3 + RIGHT * 1.4 * np.cos(angle_r.get_value()) + UP * 1.4 * np.sin(angle_r.get_value()),
            color=CRIMSON, buff=0, stroke_width=4, tip_length=0.2
        ))
        # highlight bar on curve (GOLD, used once)
        bar = Line(ax_left.c2p(0, 0), ax_left.c2p(0, 1.0),
                   color=GOLD, stroke_width=6)
        bar_label = Text("height fixed", font=MONO, color=INK, font_size=22)
        bar_label.next_to(bar, RIGHT, buff=0.15)
        divider = Line(UP * 3.5, DOWN * 3.5, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)
        self.play(FadeIn(left_title), FadeIn(right_title), Create(divider), run_time=0.6)
        self.play(Create(ax_left), run_time=0.5)
        self.play(Create(curve), run_time=0.6)
        self.play(Create(circle_r), GrowArrow(arrow_r), run_time=0.6)
        self.play(FadeIn(bar), FadeIn(bar_label), run_time=0.5)
        self.play(angle_r.animate.set_value(TAU * 1.3), run_time=d - 2.8, rate_func=linear)


# ── B09 GRAPHIC — hydrogen ground state example ───────────────────────────────
class B09_HydrogenExample(Scene):
    def construct(self):
        d = _dur("B09", 14.0)
        title = Text("Hydrogen ground state  (illustrative)", font=SERIF, color=INK,
                     font_size=28, slant=ITALIC)
        title.move_to(UP * 3.1)
        # left: phasor rotating fast
        circle = Circle(radius=1.6, color=TEAL, stroke_width=2.5)
        circle.move_to(LEFT * 3.2 + UP * 0.2)
        dot_c = Dot(LEFT * 3.2 + UP * 0.2, color=INK, radius=0.07)
        energy_label = Text("E = -13.6 eV", font=MONO, color=INK, font_size=24)
        energy_label.move_to(LEFT * 3.2 + DOWN * 2.1)
        rate_label = Text("~2e16 rad/s", font=MONO, color=TEAL, font_size=22)
        rate_label.move_to(LEFT * 3.2 + DOWN * 2.8)
        angle = ValueTracker(0.0)
        phasor = always_redraw(lambda: Arrow(
            LEFT * 3.2 + UP * 0.2,
            LEFT * 3.2 + UP * 0.2 + RIGHT * 1.6 * np.cos(angle.get_value()) + UP * 1.6 * np.sin(angle.get_value()),
            color=TEAL, buff=0, stroke_width=4, tip_length=0.22
        ))
        # right: probability bar that stays flat
        bar_bg = Rectangle(width=0.6, height=2.0)
        bar_bg.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.2)
        bar_bg.move_to(RIGHT * 2.5 + UP * 0.2)
        bar_fill = Rectangle(width=0.6, height=2.0)
        bar_fill.set_fill(TEAL, 0.7).set_stroke(width=0, opacity=0)
        bar_fill.move_to(RIGHT * 2.5 + UP * 0.2)
        bar_label_top = Text("|psi|^2", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        bar_label_top.move_to(RIGHT * 2.5 + UP * 2.0)
        flat_label = Text("locked still", font=MONO, color=INK, font_size=22)
        flat_label.move_to(RIGHT * 2.5 + DOWN * 2.1)
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(circle), FadeIn(dot_c), run_time=0.5)
        self.play(GrowArrow(phasor), run_time=0.6)
        self.play(FadeIn(energy_label), FadeIn(rate_label), run_time=0.5)
        self.play(FadeIn(bar_bg), FadeIn(bar_fill), FadeIn(bar_label_top), FadeIn(flat_label), run_time=0.6)
        self.play(angle.animate.set_value(TAU * 3.5), run_time=d - 2.7, rate_func=linear)


# ── B10 CARD — RECAP endcard ──────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Unit rotation — probability unchanged.\nStationary = observable frozen.",
                      font=SERIF, color=INK, font_size=30, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
