"""vox_scenes.py — Why Near the Band Top an Electron Behaves Like a Positive Charge
(vox-hole-effective-mass, slate cut, 16:9)

Color law: TEAL = positive effective mass / normal electron / band bottom
           CRIMSON = negative effective mass / band top / hole behavior
EXCLUSIONS: no tight-binding derivation, no effective-mass tensor,
            no multi-band physics, no Bloch oscillation.
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


# ── B01: COLD OPEN — electron accelerates backward ───────────────────────────
class B01_BackwardAcceleration(Scene):
    def construct(self):
        dur = DUR.get("B01", 10.0)
        # Show an electron at band top with an arrow pushed by E-field going one way,
        # but accelerating the other way
        title = Text("Near the band top", font=DISPLAY, font_size=30, color=INK)
        title.move_to(UP * 3.0)
        # Electron dot
        electron = Dot(ORIGIN, radius=0.25, color=CRIMSON)
        e_lbl = LabelChip("electron", accent=CRIMSON, size=22)
        e_lbl.next_to(electron, DOWN, buff=0.3)
        # Field arrow (rightward)
        field_arr = Arrow(LEFT * 3.5, LEFT * 1.0, color=INK, stroke_width=3)
        field_lbl = SerifLabel("electric field  →", INK, size=22)
        field_lbl.next_to(field_arr, DOWN, buff=0.2)
        # Acceleration arrow (leftward — CRIMSON, "wrong" direction)
        acc_arr = Arrow(RIGHT * 1.0, RIGHT * 3.5, color=CRIMSON, stroke_width=3)
        acc_lbl = LabelChip("acceleration ← backward!", accent=CRIMSON, size=22)
        acc_lbl.next_to(acc_arr, UP, buff=0.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(electron), FadeIn(e_lbl), run_time=dur * 0.20)
        self.play(GrowArrow(field_arr), FadeIn(field_lbl), run_time=dur * 0.30)
        self.play(GrowArrow(acc_arr), FadeIn(acc_lbl), run_time=dur * 0.30)
        self.wait(dur * 0.20)


# ── B02: COLD OPEN — silicon hole, positive charge carrier ───────────────────
class B02_SiliconHole(Scene):
    def construct(self):
        dur = DUR.get("B02", 11.0)
        # Show filled band with one missing electron (hole)
        title = Text("Silicon valence band", font=DISPLAY, font_size=28, color=INK)
        title.move_to(UP * 3.0)
        # Draw a band as a filled rectangle with one gap (hole)
        band = Rectangle(width=8.0, height=1.2, color=INK, stroke_width=2)
        band.set_fill(TEAL, opacity=0.25)
        band.move_to(DOWN * 0.3)
        band_lbl = SerifLabel("valence band (nearly full)", INK, size=20)
        band_lbl.next_to(band, DOWN, buff=0.3)
        # One hole = missing spot
        hole = Dot(band.get_center() + RIGHT * 2.2, radius=0.28, color=GROUND)
        hole.set_stroke(color=CRIMSON, width=2)
        hole_lbl = LabelChip("hole: +e", accent=CRIMSON, size=22)
        hole_lbl.move_to(band.get_center() + RIGHT * 2.2 + UP * 0.9)
        # Photon knocking out electron
        photon_lbl = SerifLabel("photon ejects one electron", INK, size=20)
        photon_lbl.move_to(UP * 1.6)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(band), FadeIn(band_lbl), run_time=dur * 0.25)
        self.play(FadeIn(photon_lbl), run_time=dur * 0.20)
        self.play(FadeIn(hole), FadeIn(hole_lbl), run_time=dur * 0.30)
        self.wait(dur * 0.25)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────


# ── B04: THE PROBLEM — STILL·ai beat, no scene class ─────────────────────────


# ── B05: THE PROBLEM — tight-binding dispersion relation ─────────────────────
class B05_TightBindingDispersion(Scene):
    def construct(self):
        dur = DUR.get("B05", 12.0)
        title = Text("Tight-binding dispersion", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.1)
        # Formula display
        formula = Text("E(k) = E₀ − 2t cos(ka)", font=MONO,
                       font_size=32, color=INK).move_to(UP * 1.8)
        # Axes
        axes = Axes(x_range=[-1.2, 1.2, 0.5], y_range=[-1.5, 1.5, 0.5],
                    x_length=7.0, y_length=4.0,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 1.0)
        x_lbl = SerifLabel("k  (units of π/a)", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("E(k)", INK, size=20).next_to(axes, UP + LEFT * 3.5, buff=0.1)
        # Cosine curve: E(k) = -cos(pi*k) normalized so range is [-1,1]
        cosine_curve = axes.plot(lambda k: -np.cos(np.pi * k),
                                 x_range=[-1.0, 1.0, 0.02],
                                 color=INK, stroke_width=3)
        # Label bottom and top
        bot_lbl = LabelChip("band bottom", accent=TEAL, size=20)
        bot_lbl.move_to(LEFT * 2.5 + DOWN * 2.8)
        top_lbl = LabelChip("band top", accent=CRIMSON, size=20)
        top_lbl.move_to(LEFT * 0.5 + UP * 0.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(formula), run_time=dur * 0.25)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(cosine_curve), run_time=dur * 0.40)
        self.play(FadeIn(bot_lbl), FadeIn(top_lbl), run_time=dur * 0.20)
        self.wait(dur * 0.15)


# ── B06: THE PROBLEM — band bottom vs band top curvature ─────────────────────
class B06_CurvatureSign(Scene):
    def construct(self):
        dur = DUR.get("B06", 10.0)
        # Left panel: band bottom (positive curvature), right panel: band top (negative)
        title = Text("Same band, two different curvatures", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        divider = Line(UP * 2.3, DOWN * 3.0, color=INK, stroke_width=1.2)
        # Left: parabola opening up (band bottom)
        left_title = Text("Band bottom", font=DISPLAY, font_size=22, color=TEAL)
        left_title.move_to(LEFT * 3.5 + UP * 2.0)
        left_arc = VMobject(color=TEAL, stroke_width=3)
        left_pts = [np.array([-4.5 + i * 0.5, 0.4 * (i - 2) ** 2 - 2.5, 0]) for i in range(9)]
        left_arc.set_points_smoothly(left_pts)
        left_note = SerifLabel("curves UP: d²E/dk² > 0", TEAL, size=20)
        left_note.move_to(LEFT * 3.5 + DOWN * 2.3)
        # Right: parabola opening down (band top)
        right_title = Text("Band top", font=DISPLAY, font_size=22, color=CRIMSON)
        right_title.move_to(RIGHT * 3.0 + UP * 2.0)
        right_arc = VMobject(color=CRIMSON, stroke_width=3)
        right_pts = [np.array([0.7 + i * 0.5, -0.4 * (i - 2) ** 2 + 1.5, 0]) for i in range(9)]
        right_arc.set_points_smoothly(right_pts)
        right_note = SerifLabel("curves DOWN: d²E/dk² < 0", CRIMSON, size=20)
        right_note.move_to(RIGHT * 3.0 + DOWN * 2.3)
        self.play(FadeIn(title), Create(divider), run_time=0.5)
        self.play(FadeIn(left_title), Create(left_arc), run_time=dur * 0.35)
        self.play(FadeIn(left_note), run_time=dur * 0.15)
        self.play(FadeIn(right_title), Create(right_arc), run_time=dur * 0.35)
        self.play(FadeIn(right_note), run_time=dur * 0.15)


# ── B07: THE MECHANISM — effective mass from curvature, positive at bottom ────
class B07_EffectiveMassPositive(Scene):
    def construct(self):
        dur = DUR.get("B07", 12.0)
        title = Text("Effective mass: the curvature formula", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        formula = Text("m∗ = ħ² / (d²E/dk²)", font=MONO,
                       font_size=30, color=INK).move_to(UP * 1.8)
        # Two-row comparison
        pos_row = VGroup(
            LabelChip("band bottom", accent=TEAL, size=22),
            Text("d²E/dk² > 0", font=MONO, font_size=24, color=TEAL),
            Text("  →  m∗ > 0", font=MONO, font_size=24, color=TEAL),
            SerifLabel("normal: field pushes opposite", TEAL, size=20),
        )
        pos_row.arrange(RIGHT, buff=0.4).move_to(DOWN * 0.2)
        neg_row = VGroup(
            LabelChip("band top", accent=CRIMSON, size=22),
            Text("d²E/dk² < 0", font=MONO, font_size=24, color=CRIMSON),
            Text("  →  m∗ < 0", font=MONO, font_size=24, color=CRIMSON),
            SerifLabel("weird: accelerates same as field!", CRIMSON, size=20),
        )
        neg_row.arrange(RIGHT, buff=0.4).move_to(DOWN * 1.6)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(formula), run_time=dur * 0.25)
        self.play(FadeIn(pos_row), run_time=dur * 0.30)
        self.play(FadeIn(neg_row), run_time=dur * 0.30)
        self.wait(dur * 0.15)


# ── B08: THE MECHANISM — negative effective mass, backward acceleration ───────
class B08_NegativeMass(Scene):
    def construct(self):
        dur = DUR.get("B08", 11.0)
        title = Text("Negative mass: Newton's law flips", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Show F = ma → a = F/m, with m<0 gives a opposite to F
        f_eq = Text("F = m∗ × a", font=MONO, font_size=32, color=INK)
        f_eq.move_to(UP * 1.5)
        rearranged = Text("a = F / m∗", font=MONO, font_size=28, color=INK)
        rearranged.move_to(UP * 0.4)
        neg_case = Text("m∗ < 0  →  a and F point opposite ways",
                        font=MONO, font_size=24, color=CRIMSON)
        neg_case.move_to(DOWN * 0.8)
        # Visual: F arrow right, a arrow left
        f_vis = Arrow(LEFT * 3.5, LEFT * 1.5, color=INK, stroke_width=3)
        f_vis_lbl = SerifLabel("F  (field pushes right)", INK, size=20)
        f_vis_lbl.next_to(f_vis, UP, buff=0.2)
        a_vis = Arrow(RIGHT * 1.5, RIGHT * 3.5, color=CRIMSON, stroke_width=3)
        a_vis_lbl = SerifLabel("a  (electron goes left!)", CRIMSON, size=20)
        a_vis_lbl.next_to(a_vis, DOWN, buff=0.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(f_eq), run_time=dur * 0.20)
        self.play(FadeIn(rearranged), run_time=dur * 0.15)
        self.play(FadeIn(neg_case), run_time=dur * 0.20)
        self.play(GrowArrow(f_vis), FadeIn(f_vis_lbl), run_time=dur * 0.20)
        self.play(GrowArrow(a_vis), FadeIn(a_vis_lbl), run_time=dur * 0.25)


# ── B09: THE MECHANISM — filled band argument, hole current ──────────────────
class B09_HoleCurrent(Scene):
    def construct(self):
        dur = DUR.get("B09", 12.0)
        title = Text("The filled-band argument", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Three rows: full band, remove one, net current
        full_lbl = SerifLabel("full band: all k-states filled", INK, size=20)
        full_lbl.move_to(UP * 1.8 + LEFT * 2.5)
        full_eq = Text("net current = 0", font=MONO, font_size=22, color=INK)
        full_eq.move_to(UP * 1.8 + RIGHT * 2.8)
        sep1 = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1).move_to(UP * 1.1)
        remove_lbl = SerifLabel("remove electron at k = k₀", CRIMSON, size=20)
        remove_lbl.move_to(UP * 0.5 + LEFT * 2.5)
        remove_eq = Text("(full) − (one electron at k₀)", font=MONO,
                         font_size=20, color=CRIMSON)
        remove_eq.move_to(UP * 0.5 + RIGHT * 2.0)
        sep2 = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1).move_to(DOWN * 0.2)
        net_lbl = SerifLabel("net current:", INK, size=20)
        net_lbl.move_to(DOWN * 0.9 + LEFT * 4.0)
        net_eq = Text("− (electron at k₀)", font=MONO, font_size=22, color=TEAL)
        net_eq.move_to(DOWN * 0.9 + RIGHT * 1.2)
        conclusion = LabelChip("= hole of charge +e moving forward!", accent=TEAL, size=22)
        conclusion.move_to(DOWN * 2.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(full_lbl), FadeIn(full_eq), run_time=dur * 0.20)
        self.play(Create(sep1), run_time=0.2)
        self.play(FadeIn(remove_lbl), FadeIn(remove_eq), run_time=dur * 0.20)
        self.play(Create(sep2), run_time=0.2)
        self.play(FadeIn(net_lbl), FadeIn(net_eq), run_time=dur * 0.20)
        self.play(FadeIn(conclusion), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B10: THE MECHANISM — section CARD, no scene class ────────────────────────


# ── B11: THE IMPLICATION — p-type semiconductor ──────────────────────────────
class B11_PTypeSemiconductor(Scene):
    def construct(self):
        dur = DUR.get("B11", 11.0)
        title = Text("Holes in real semiconductors", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Two columns: n-type (electron carriers) vs p-type (hole carriers)
        n_grp = VGroup(
            LabelChip("n-type", accent=TEAL, size=24),
            Text("extra electrons donated", font=SERIF, font_size=21,
                 color=TEAL, slant=ITALIC),
            Text("negative charge carriers", font=DISPLAY, font_size=21, color=TEAL),
        )
        n_grp.arrange(DOWN, buff=0.3).move_to(LEFT * 3.2 + DOWN * 0.5)
        p_grp = VGroup(
            LabelChip("p-type", accent=CRIMSON, size=24),
            Text("electrons removed by acceptors", font=SERIF, font_size=21,
                 color=CRIMSON, slant=ITALIC),
            Text("holes as positive carriers", font=DISPLAY, font_size=21, color=CRIMSON),
        )
        p_grp.arrange(DOWN, buff=0.3).move_to(RIGHT * 3.2 + DOWN * 0.5)
        divider = Line(UP * 2.0, DOWN * 2.3, color=INK, stroke_width=1.5)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(n_grp), run_time=dur * 0.40)
        self.play(FadeIn(p_grp), run_time=dur * 0.35)
        self.wait(dur * 0.25)


# ── B12: THE IMPLICATION — p-n junction and devices ──────────────────────────
class B12_PNJunction(Scene):
    def construct(self):
        dur = DUR.get("B12", 11.0)
        title = Text("The p-n junction: two carriers meet", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Schematic: p side (CRIMSON, holes moving right) | n side (TEAL, electrons left)
        p_rect = Rectangle(width=3.5, height=2.0)
        p_rect.set_fill(CRIMSON, opacity=0.15).set_stroke(color=CRIMSON, width=2)
        p_rect.move_to(LEFT * 2.2 + DOWN * 0.2)
        p_lbl = Text("p", font=DISPLAY, font_size=36, color=CRIMSON).move_to(LEFT * 2.2 + DOWN * 0.2)
        n_rect = Rectangle(width=3.5, height=2.0)
        n_rect.set_fill(TEAL, opacity=0.15).set_stroke(color=TEAL, width=2)
        n_rect.move_to(RIGHT * 2.2 + DOWN * 0.2)
        n_lbl = Text("n", font=DISPLAY, font_size=36, color=TEAL).move_to(RIGHT * 2.2 + DOWN * 0.2)
        # Arrows showing drift — placed below the p/n labels to avoid crossing
        hole_arr = Arrow(LEFT * 3.5 + DOWN * 1.0, LEFT * 0.5 + DOWN * 1.0,
                         color=CRIMSON, stroke_width=2.5)
        hole_arr_lbl = SerifLabel("holes →", CRIMSON, size=20)
        hole_arr_lbl.move_to(LEFT * 2.2 + DOWN * 1.5)
        elec_arr = Arrow(RIGHT * 3.5 + DOWN * 1.0, RIGHT * 0.5 + DOWN * 1.0,
                         color=TEAL, stroke_width=2.5)
        elec_arr_lbl = SerifLabel("← electrons", TEAL, size=20)
        elec_arr_lbl.move_to(RIGHT * 2.2 + DOWN * 1.5)
        device_note = SerifLabel("rectifier, solar cell, LED — same physics", INK, size=20)
        device_note.move_to(DOWN * 2.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(p_rect), FadeIn(p_lbl), Create(n_rect), FadeIn(n_lbl), run_time=dur * 0.30)
        self.play(GrowArrow(hole_arr), FadeIn(hole_arr_lbl),
                  GrowArrow(elec_arr), FadeIn(elec_arr_lbl), run_time=dur * 0.35)
        self.play(FadeIn(device_note), run_time=dur * 0.25)
        self.wait(dur * 0.10)


# ── B13: THE EXAMPLE — illustrative numbers ───────────────────────────────────
class B13_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B13", 18.0)
        title = Text("Illustrative: 1D tight-binding, t = 1 eV, a = 0.3 nm", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.1)
        subtitle = Text("(invented numbers, labeled illustrative)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        rows = [
            ("E(k) = E₀ − 2×1 eV×cos(ka)", "band width = 4 eV", INK),
            ("band bottom: m∗ = +0.4 mₑ", "positive curvature → normal electron", TEAL),
            ("band top:    m∗ = −0.4 mₑ", "negative curvature → hole behavior", CRIMSON),
        ]
        row_groups = VGroup()
        for i, (expr, note, col) in enumerate(rows):
            y = 1.2 - i * 1.5
            r = VGroup(
                Text(expr, font=MONO, font_size=20, color=col).move_to(LEFT * 2.5 + UP * y),
                SerifLabel(note, col, size=18).move_to(RIGHT * 3.0 + UP * y),
            )
            row_groups.add(r)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        for rg in row_groups:
            self.play(FadeIn(rg, shift=RIGHT * 0.3), run_time=dur * 0.22)
        self.wait(dur * 0.12)


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
