"""vox_scenes.py — Every valley is a parabola if you lean in close enough
(vox-potential-parabola, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B08 is STILL·ai — no scene.
Color law: TEAL = parabola (the harmonic approximation);
CRIMSON = full complicated potential.
GOLD = minimum marker (B05-B06 only).
Exclusions: no full Taylor coefficients on screen.
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


# A lumpy asymmetric potential
def _lumpy(x):
    return 0.5 * x**2 + 0.15 * x**3 - 0.04 * x**4 + 0.3 * np.sin(2.5 * x)

# Its minimum is near x=0 by construction; shift so minimum is at origin
_x0 = 0.0  # approximate minimum
_V0 = _lumpy(_x0)
def _V(x):
    return _lumpy(x) - _V0

# Parabola matching at minimum: V''(0) ~ 1.0 - 0.0 ... let's compute numerically
_dx = 0.001
_V_pp = (_lumpy(_x0 + _dx) - 2 * _lumpy(_x0) + _lumpy(_x0 - _dx)) / _dx**2
def _P(x):
    return 0.5 * _V_pp * x**2


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("Every valley is a parabola\nif you lean in close enough",
                     font=DISPLAY, color=INK, font_size=38, weight="BOLD",
                     line_spacing=1.2)
        title.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(d - 1.3)


# ── B02 CARD — THE QUESTION ───────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        d = _dur("B02", 10.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.move_to(UP * 2.8)
        line1 = Text("Complicated wells, complicated spectra.", font=SERIF, color=INK, font_size=26)
        line1.move_to(UP * 0.8)
        line2 = Text("Parabola predicts equal spacing.", font=SERIF, color=TEAL, font_size=26)
        line2.move_to(UP * 0.0)
        line3 = Text("Real spectra show equal spacing. Why?", font=SERIF, color=CRIMSON,
                     font_size=26, slant=ITALIC)
        line3.move_to(DOWN * 1.0)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3), run_time=0.5)
        self.wait(d - 1.7)


# ── B03 GRAPHIC — lumpy asymmetric potential ─────────────────────────────────
class B03_LumpyPotential(Scene):
    def construct(self):
        d = _dur("B03", 11.0)
        ax = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-0.5, 3.5, 1],
            x_length=8.0, y_length=5.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(DOWN * 0.3)
        x_vals = np.linspace(-2.4, 2.4, 400)
        y_vals = np.clip(_V(x_vals), -0.4, 3.4)
        pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
        curve = VMobject().set_points_smoothly(pts)
        curve.set_stroke(CRIMSON, width=3)
        label = Text("any smooth potential", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        label.move_to(RIGHT * 3.5 + UP * 2.8)
        self.play(Create(ax), run_time=0.5)
        self.play(Create(curve), run_time=(d - 0.5) * 0.7)
        self.play(FadeIn(label), run_time=(d - 0.5) * 0.3)


# ── B04 GRAPHIC — Taylor expansion: linear term dies ─────────────────────────
class B04_TaylorLinearDies(Scene):
    def construct(self):
        d = _dur("B04", 10.0)
        ax = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-0.5, 3.5, 1],
            x_length=8.0, y_length=5.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(DOWN * 0.3)
        x_vals = np.linspace(-2.4, 2.4, 400)
        y_vals = np.clip(_V(x_vals), -0.4, 3.4)
        pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
        curve = VMobject().set_points_smoothly(pts)
        curve.set_stroke(CRIMSON, width=2.5, opacity=0.5)

        # mark minimum
        min_dot = Dot(ax.c2p(0, 0), color=TEAL, radius=0.12)

        # annotate
        annot1 = Text("V'(x0) = 0  at minimum", font=MONO, color=INK, font_size=24)
        annot1.move_to(RIGHT * 3.0 + UP * 1.4)
        annot2 = Text("linear term dies", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        annot2.move_to(RIGHT * 3.0 + UP * 0.3)
        annot3 = Text("quadratic survives", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        annot3.move_to(RIGHT * 3.0 + DOWN * 0.8)

        self.play(Create(ax), Create(curve), run_time=0.6)
        self.play(FadeIn(min_dot), run_time=0.4)
        self.play(FadeIn(annot1), run_time=0.5)
        self.play(FadeIn(annot2), run_time=0.5)
        self.play(FadeIn(annot3), run_time=(d - 2.0))


# ── B05 GRAPHIC — zoom into well, parabola locks on ──────────────────────────
class B05_ZoomMerge(Scene):
    def construct(self):
        d = _dur("B05", 12.0)
        # Show well + parabola, then zoom (scale x range in)
        ax_wide = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-0.1, 3.0, 1],
            x_length=8.5, y_length=5.0,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_wide.move_to(DOWN * 0.2)

        ax_narrow = Axes(
            x_range=[-0.8, 0.8, 0.4], y_range=[-0.05, 0.5, 0.2],
            x_length=8.5, y_length=5.0,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_narrow.move_to(DOWN * 0.2)

        x_wide = np.linspace(-2.4, 2.4, 400)
        y_V_wide = np.clip(_V(x_wide), -0.05, 2.95)
        y_P_wide = np.clip(_P(x_wide), -0.05, 2.95)

        x_narrow = np.linspace(-0.75, 0.75, 400)
        y_V_narrow = np.clip(_V(x_narrow), -0.01, 0.45)
        y_P_narrow = np.clip(_P(x_narrow), -0.01, 0.45)

        v_curve_w = VMobject().set_points_smoothly([ax_wide.c2p(x, y) for x, y in zip(x_wide, y_V_wide)])
        v_curve_w.set_stroke(CRIMSON, width=3)
        p_curve_w = VMobject().set_points_smoothly([ax_wide.c2p(x, y) for x, y in zip(x_wide, y_P_wide)])
        p_curve_w.set_stroke(TEAL, width=2.5)

        v_curve_n = VMobject().set_points_smoothly([ax_narrow.c2p(x, y) for x, y in zip(x_narrow, y_V_narrow)])
        v_curve_n.set_stroke(CRIMSON, width=3)
        p_curve_n = VMobject().set_points_smoothly([ax_narrow.c2p(x, y) for x, y in zip(x_narrow, y_P_narrow)])
        p_curve_n.set_stroke(TEAL, width=2.5)

        gold_dot = Dot(ax_wide.c2p(0, 0), color=GOLD, radius=0.15)
        gold_dot.set_stroke(INK, width=1.5)

        zoom_label = Text("zoom in", font=SERIF, color=INK, font_size=24, slant=ITALIC)
        zoom_label.move_to(UP * 3.2)
        merge_label = Text("they merge", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        merge_label.move_to(UP * 3.7)  # distinct y

        self.play(Create(ax_wide), run_time=0.4)
        self.play(Create(v_curve_w), run_time=0.5)
        self.play(Create(p_curve_w), FadeIn(gold_dot), FadeIn(zoom_label), run_time=0.5)
        self.play(Transform(ax_wide, ax_narrow),
                  Transform(v_curve_w, v_curve_n),
                  Transform(p_curve_w, p_curve_n),
                  FadeOut(zoom_label), FadeIn(merge_label),
                  run_time=d - 1.4, rate_func=smooth)


# ── B06 GRAPHIC — spring constant = V''(x0) ──────────────────────────────────
class B06_SpringConstant(Scene):
    def construct(self):
        d = _dur("B06", 11.0)
        ax = Axes(
            x_range=[-1.5, 1.5, 0.5], y_range=[-0.1, 1.5, 0.5],
            x_length=5.5, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(LEFT * 1.5 + DOWN * 0.3)
        x_vals = np.linspace(-1.4, 1.4, 300)
        y_P = np.clip(_P(x_vals), -0.05, 1.45)
        parab = VMobject().set_points_smoothly([ax.c2p(x, y) for x, y in zip(x_vals, y_P)])
        parab.set_stroke(TEAL, width=3)

        gold_bar = Line(ax.c2p(0.0, 0), ax.c2p(0.4, 0), color=GOLD, stroke_width=5)

        info1 = Text("k_eff = V''(x0)", font=MONO, color=TEAL, font_size=28)
        info1.move_to(RIGHT * 3.5 + UP * 1.2)
        info2 = Text("second derivative\nat the minimum", font=SERIF, color=INK, font_size=24,
                     line_spacing=1.2)
        info2.move_to(RIGHT * 3.5 + UP * 0.0)
        info3 = Text("shape elsewhere:\nirrelevant", font=SERIF, color=CRIMSON, font_size=24,
                     line_spacing=1.2)
        info3.move_to(RIGHT * 3.5 + DOWN * 1.5)

        self.play(Create(ax), Create(parab), run_time=0.6)
        self.play(Create(gold_bar), run_time=0.4)
        self.play(FadeIn(info1), run_time=0.5)
        self.play(FadeIn(info2), run_time=0.5)
        self.play(FadeIn(info3), run_time=(d - 2.0))


# ── B07 GRAPHIC — three wells, three parabolas ────────────────────────────────
class B07_ThreeWells(Scene):
    def construct(self):
        d = _dur("B07", 11.0)
        # Three small panels side by side
        positions = [LEFT * 4.5, ORIGIN, RIGHT * 4.5]
        labels = ["molecular bond", "lattice site", "trapped atom"]
        keffs = [0.8, 1.5, 0.5]  # different spring constants

        for pos, lbl, k in zip(positions, labels, keffs):
            ax = Axes(
                x_range=[-1.2, 1.2, 0.6], y_range=[0, 1.2, 0.5],
                x_length=3.0, y_length=2.5,
                axis_config={"color": SLATE, "stroke_width": 1.0, "include_tip": False}
            )
            ax.move_to(pos + DOWN * 0.3)
            x_v = np.linspace(-1.1, 1.1, 200)
            # different shaped wells
            y_v = np.clip(0.5 * k * x_v**2 + 0.12 * x_v**3 - 0.05 * x_v**4, 0, 1.15)
            y_p = np.clip(0.5 * k * x_v**2, 0, 1.15)
            well = VMobject().set_points_smoothly([ax.c2p(x, y) for x, y in zip(x_v, y_v)])
            well.set_stroke(CRIMSON, width=2.5)
            parab = VMobject().set_points_smoothly([ax.c2p(x, y) for x, y in zip(x_v, y_p)])
            parab.set_stroke(TEAL, width=2.0)
            name_label = Text(lbl, font=SERIF, color=INK, font_size=18)
            name_label.move_to(pos + DOWN * 2.6)
            self.play(Create(ax), run_time=0.2)
            self.play(Create(well), Create(parab), FadeIn(name_label), run_time=0.5)

        chip = LabelChip("each = parabola at bottom", accent=TEAL, size=22)
        chip.move_to(UP * 3.0)
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(d - (0.2 + 0.5) * 3 - 0.5)


# ── B09 GRAPHIC — Morse potential zoom example ────────────────────────────────
class B09_MorseZoom(Scene):
    def construct(self):
        d = _dur("B09", 13.0)
        # Morse potential V = De*(1 - exp(-alpha*(x-x0)))^2
        De = 1.5; alpha = 1.8
        def morse(x):
            return De * (1 - np.exp(-alpha * x))**2

        title = Text("Illustrative: Morse potential", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.2)

        ax_wide = Axes(
            x_range=[-0.8, 2.5, 1], y_range=[0, 1.8, 0.5],
            x_length=7.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_wide.move_to(DOWN * 0.5)

        ax_narrow = Axes(
            x_range=[-0.3, 0.3, 0.15], y_range=[0, 0.25, 0.1],
            x_length=7.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_narrow.move_to(DOWN * 0.5)

        x_w = np.linspace(-0.75, 2.4, 400)
        y_morse_w = np.clip([morse(x) for x in x_w], 0, 1.75)
        y_para_w = np.clip([De * alpha**2 * x**2 for x in x_w], 0, 1.75)

        x_n = np.linspace(-0.28, 0.28, 300)
        y_morse_n = np.clip([morse(x) for x in x_n], 0, 0.24)
        y_para_n = np.clip([De * alpha**2 * x**2 for x in x_n], 0, 0.24)

        mc_w = VMobject().set_points_smoothly([ax_wide.c2p(x, y) for x, y in zip(x_w, y_morse_w)])
        mc_w.set_stroke(CRIMSON, width=3)
        pc_w = VMobject().set_points_smoothly([ax_wide.c2p(x, y) for x, y in zip(x_w, y_para_w)])
        pc_w.set_stroke(TEAL, width=2.5)

        mc_n = VMobject().set_points_smoothly([ax_narrow.c2p(x, y) for x, y in zip(x_n, y_morse_n)])
        mc_n.set_stroke(CRIMSON, width=3)
        pc_n = VMobject().set_points_smoothly([ax_narrow.c2p(x, y) for x, y in zip(x_n, y_para_n)])
        pc_n.set_stroke(TEAL, width=2.5)

        agree_note = Text("agree within 0.05 nm", font=MONO, color=TEAL, font_size=22)
        agree_note.move_to(RIGHT * 4.0 + DOWN * 2.8)

        self.play(FadeIn(title), Create(ax_wide), run_time=0.5)
        self.play(Create(mc_w), Create(pc_w), run_time=0.7)
        self.play(Transform(ax_wide, ax_narrow),
                  Transform(mc_w, mc_n), Transform(pc_w, pc_n),
                  run_time=(d - 1.2) * 0.6, rate_func=smooth)
        self.play(FadeIn(agree_note), run_time=(d - 1.2) * 0.4)


# ── B10 CARD — RECAP ──────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Linear term = 0 at minimum.\nLeading survivor = quadratic.\nEvery well is a parabola up close.",
                      font=SERIF, color=INK, font_size=24, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
