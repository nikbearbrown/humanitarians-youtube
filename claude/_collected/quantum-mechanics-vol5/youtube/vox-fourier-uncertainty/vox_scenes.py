"""vox_scenes.py — Squeeze the position, the momentum spreads (uncertainty is just Fourier)
(vox-fourier-uncertainty, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B08 is STILL·ai — no scene here.
Durations read from beat_sheet.json.

Color law: TEAL = narrow/squeezed Gaussian (position);
CRIMSON = wide/spread Gaussian (momentum).
GOLD = single highlight (saturation marker, B06 only).

Exclusions: no Robertson/commutator derivation; Fourier bandwidth route only.
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
        title = Text("Squeeze the position,\nthe momentum spreads",
                     font=DISPLAY, color=INK, font_size=42, weight="BOLD",
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
        line1 = Text("delta-x * delta-k >= 1/2  (pure math).", font=MONO,
                     color=INK, font_size=28)
        line1.move_to(UP * 0.6)
        line2 = Text("Multiply by h-bar: delta-x * delta-p >= h-bar/2.", font=MONO,
                     color=INK, font_size=26)
        line2.move_to(DOWN * 0.4)
        line3 = Text("Why is this called quantum?", font=SERIF,
                     color=CRIMSON, font_size=30, slant=ITALIC)
        line3.move_to(DOWN * 1.5)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.5)
        self.play(FadeIn(line2), run_time=0.5)
        self.play(FadeIn(line3), run_time=0.5)
        self.wait(d - 1.9)


# ── B03 GRAPHIC — wave packet = sum of sinusoids ─────────────────────────────
class B03_WavePacketBuildup(Scene):
    def construct(self):
        d = _dur("B03", 11.0)
        ax = Axes(
            x_range=[-5, 5, 1], y_range=[-2.5, 2.5, 1],
            x_length=9.0, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(ORIGIN)
        # Build a narrow Gaussian by accumulating harmonics
        def gaussian_approx(x, n_terms):
            result = np.zeros_like(x)
            for k in range(1, n_terms + 1):
                sigma_k = 0.5
                result += np.exp(-0.5 * (k * 0.3 / sigma_k) ** 2) * np.cos(k * 0.3 * x)
            return result / (n_terms * 0.3)

        x_vals = np.linspace(-5, 5, 300)
        colors = [SLATE, TEAL, TEAL, TEAL]
        n_list = [1, 3, 6, 12]
        curves = []
        for i, n in enumerate(n_list):
            y_vals = gaussian_approx(x_vals, n)
            pts = [ax.c2p(x, min(max(y, -2.4), 2.4)) for x, y in zip(x_vals, y_vals)]
            c = VMobject().set_points_smoothly(pts)
            c.set_stroke(colors[min(i, 3)], width=2.5)
            curves.append(c)

        label = Text("few waves — spread out  /  many waves — narrow spike",
                     font=SERIF, color=TEAL, font_size=22)
        label.move_to(UP * 2.8)

        self.play(Create(ax), run_time=0.5)
        self.play(Create(curves[0]), run_time=0.7)
        self.play(Transform(curves[0], curves[1]), run_time=(d - 1.2) * 0.3)
        self.play(Transform(curves[0], curves[2]), run_time=(d - 1.2) * 0.35)
        self.play(Transform(curves[0], curves[3]),
                  FadeIn(label), run_time=(d - 1.2) * 0.35)


# ── B04 GRAPHIC — wide packet needs few frequencies ──────────────────────────
class B04_WideFewFrequencies(Scene):
    def _gauss_curve(self, ax, sigma, color, x_range=(-5, 5)):
        pts = [ax.c2p(x, np.exp(-x**2 / (2 * sigma**2)))
               for x in np.linspace(x_range[0], x_range[1], 200)]
        c = VMobject().set_points_smoothly(pts)
        c.set_stroke(color, width=3)
        return c

    def construct(self):
        d = _dur("B04", 10.0)
        ax_x = Axes(
            x_range=[-5, 5, 2], y_range=[0, 1.3, 0.5],
            x_length=4.5, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_x.move_to(LEFT * 2.8 + DOWN * 0.2)

        ax_k = Axes(
            x_range=[-4, 4, 2], y_range=[0, 1.3, 0.5],
            x_length=4.5, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_k.move_to(RIGHT * 2.8 + DOWN * 0.2)

        x_label = Text("position  x", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        x_label.move_to(LEFT * 2.8 + DOWN * 2.2)
        k_label = Text("wavenumber  k", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        k_label.move_to(RIGHT * 2.8 + DOWN * 2.2)

        # wide x, narrow k
        xc_wide = self._gauss_curve(ax_x, 2.0, TEAL)
        kc_narrow = self._gauss_curve(ax_k, 0.5, CRIMSON, x_range=(-4, 4))

        # narrow x, wide k
        xc_narrow = self._gauss_curve(ax_x, 0.5, TEAL)
        kc_wide = self._gauss_curve(ax_k, 2.0, CRIMSON, x_range=(-4, 4))

        label_cur = Text("wide in x = narrow in k", font=SERIF, color=INK, font_size=22)
        label_cur.move_to(UP * 2.8)
        label_next = Text("narrow in x = wide in k", font=SERIF, color=INK, font_size=22)
        label_next.move_to(UP * 3.5)  # distinct y — no overlap

        self.play(Create(ax_x), Create(ax_k), run_time=0.5)
        self.play(Create(xc_wide), Create(kc_narrow), FadeIn(x_label), FadeIn(k_label),
                  FadeIn(label_cur), run_time=0.7)
        self.play(Transform(xc_wide, xc_narrow), Transform(kc_narrow, kc_wide),
                  FadeOut(label_cur), FadeIn(label_next),
                  run_time=d - 1.2, rate_func=smooth)


# ── B05 GRAPHIC — Gaussian paired Gaussians, reciprocal widths ───────────────
class B05_PairedGaussians(Scene):
    def _gauss(self, ax, sigma, color):
        pts = [ax.c2p(x, np.exp(-x**2 / (2 * sigma**2)))
               for x in np.linspace(-5, 5, 200)]
        c = VMobject().set_points_smoothly(pts)
        c.set_stroke(color, width=3)
        return c

    def construct(self):
        d = _dur("B05", 12.0)
        ax_x = Axes(
            x_range=[-5, 5, 2], y_range=[0, 1.3, 0.5],
            x_length=4.5, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_x.move_to(LEFT * 2.8 + DOWN * 0.2)

        ax_k = Axes(
            x_range=[-5, 5, 2], y_range=[0, 1.3, 0.5],
            x_length=4.5, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_k.move_to(RIGHT * 2.8 + DOWN * 0.2)

        title_x = Text("psi(x)", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        title_x.move_to(LEFT * 2.8 + UP * 2.5)
        title_k = Text("phi(k)", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        title_k.move_to(RIGHT * 2.8 + UP * 2.5)

        arrow = Arrow(LEFT * 0.3, RIGHT * 0.3, color=INK, buff=0.1, stroke_width=2)
        arrow.move_to(ORIGIN + DOWN * 0.2)
        ft_label = Text("Fourier\ntransform", font=SERIF, color=INK, font_size=20, line_spacing=1.1)
        ft_label.move_to(ORIGIN + UP * 0.6)

        # start: medium width
        xg1 = self._gauss(ax_x, 1.0, TEAL)
        kg1 = self._gauss(ax_k, 1.0, CRIMSON)
        # narrow x, wide k
        xg_narrow = self._gauss(ax_x, 0.4, TEAL)
        kg_wide = self._gauss(ax_k, 2.5, CRIMSON)
        # wide x, narrow k
        xg_wide = self._gauss(ax_x, 2.5, TEAL)
        kg_narrow = self._gauss(ax_k, 0.4, CRIMSON)

        self.play(Create(ax_x), Create(ax_k), run_time=0.5)
        self.play(FadeIn(title_x), FadeIn(title_k), run_time=0.4)
        self.play(Create(xg1), Create(kg1), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(ft_label), run_time=0.5)
        self.play(Transform(xg1, xg_narrow), Transform(kg1, kg_wide),
                  run_time=(d - 2.0) * 0.4, rate_func=smooth)
        self.play(Transform(xg1, xg_wide), Transform(kg1, kg_narrow),
                  run_time=(d - 2.0) * 0.6, rate_func=smooth)


# ── B06 GRAPHIC — bandwidth bound with saturation highlight ──────────────────
class B06_BandwidthBound(Scene):
    def construct(self):
        d = _dur("B06", 11.0)
        # Show the inequality and saturation at Gaussian
        bound_text = Text("delta-x  *  delta-k  >=  1/2", font=MONO, color=INK, font_size=34)
        bound_text.move_to(UP * 1.8)

        sat_box = Rectangle(width=6.0, height=0.9)
        sat_box.set_fill(GOLD, 0.35).set_stroke(width=0, opacity=0)
        sat_box.move_to(UP * 0.2)
        sat_label = Text("Gaussian: delta-x * delta-k = 1/2  (equality — minimum)", font=MONO,
                         color=INK, font_size=22)
        sat_label.move_to(UP * 0.2)

        other_text = Text("All other wave shapes: strictly greater than 1/2",
                          font=SERIF, color=SLATE, font_size=26)
        other_text.move_to(DOWN * 1.2)

        meaning = Text("Gaussian is the most tightly packed shape possible.",
                       font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        meaning.move_to(DOWN * 2.5)

        self.play(FadeIn(bound_text), run_time=0.6)
        self.play(FadeIn(sat_box), FadeIn(sat_label), run_time=0.7)
        self.play(FadeIn(other_text), run_time=0.5)
        self.play(FadeIn(meaning), run_time=0.5)
        # add motion: scale bound_text slightly
        self.play(bound_text.animate.scale(1.08), run_time=(d - 2.3) * 0.5, rate_func=there_and_back)
        self.play(bound_text.animate.scale(1.0), run_time=(d - 2.3) * 0.5)


# ── B07 GRAPHIC — substitution p = hbar*k ────────────────────────────────────
class B07_Substitution(Scene):
    def construct(self):
        d = _dur("B07", 12.0)
        math_line = Text("delta-x * delta-k >= 1/2", font=MONO, color=SLATE, font_size=32)
        math_line.move_to(UP * 2.0)

        arrow_down = Arrow(UP * 1.2, UP * 0.2, color=INK, buff=0, stroke_width=2.5, tip_length=0.2)
        sub_label = Text("p = h-bar * k", font=MONO, color=TEAL, font_size=28)
        sub_label.move_to(RIGHT * 2.8 + UP * 0.7)

        result_line = Text("delta-x * delta-p >= h-bar/2", font=MONO, color=TEAL, font_size=34)
        result_line.move_to(DOWN * 0.5)

        heis_label = Text("Heisenberg's uncertainty principle", font=SERIF,
                          color=CRIMSON, font_size=28, slant=ITALIC)
        heis_label.move_to(DOWN * 1.8)

        note = Text("No new physics — only de Broglie's p = h-bar * k.",
                    font=SERIF, color=INK, font_size=24)
        note.move_to(DOWN * 3.0)

        self.play(FadeIn(math_line), run_time=0.5)
        self.play(GrowArrow(arrow_down), FadeIn(sub_label), run_time=0.6)
        self.play(FadeIn(result_line), run_time=0.6)
        self.play(FadeIn(heis_label), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.play(result_line.animate.scale(1.06), run_time=(d - 2.7) * 0.5, rate_func=there_and_back)
        self.play(result_line.animate.scale(1.0), run_time=(d - 2.7) * 0.5)


# ── B09 GRAPHIC — illustrative example: halving the width ────────────────────
class B09_ExampleHalveWidth(Scene):
    def _gauss(self, ax, sigma, color):
        pts = [ax.c2p(x, np.exp(-x**2 / (2 * sigma**2)))
               for x in np.linspace(-4, 4, 200)]
        c = VMobject().set_points_smoothly(pts)
        c.set_stroke(color, width=3)
        return c

    def construct(self):
        d = _dur("B09", 14.0)
        title = Text("Illustrative example", font=SERIF, color=INK,
                     font_size=24, slant=ITALIC)
        title.move_to(UP * 3.2)

        ax_x = Axes(
            x_range=[-4, 4, 2], y_range=[0, 1.3, 0.5],
            x_length=4.0, y_length=2.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_x.move_to(LEFT * 2.5 + DOWN * 0.3)

        ax_p = Axes(
            x_range=[-4, 4, 2], y_range=[0, 1.3, 0.5],
            x_length=4.0, y_length=2.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax_p.move_to(RIGHT * 2.5 + DOWN * 0.3)

        xl = Text("delta-x = 0.5 nm", font=MONO, color=TEAL, font_size=22)
        xl.move_to(LEFT * 2.5 + DOWN * 2.2)
        pl = Text("delta-p >= h-bar/nm", font=MONO, color=CRIMSON, font_size=22)
        pl.move_to(RIGHT * 2.5 + DOWN * 2.2)

        # start: sigma = 1 (0.5 nm baseline)
        xg1 = self._gauss(ax_x, 1.0, TEAL)
        pg1 = self._gauss(ax_p, 1.0, CRIMSON)

        # halved: sigma = 0.5 (0.25 nm), momentum doubles
        xg_half = self._gauss(ax_x, 0.5, TEAL)
        pg_double = self._gauss(ax_p, 2.0, CRIMSON)

        half_note = Text("Halve delta-x -> delta-p doubles", font=MONO,
                         color=INK, font_size=22)
        half_note.move_to(DOWN * 3.4)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(ax_x), Create(ax_p), run_time=0.5)
        self.play(FadeIn(xl), FadeIn(pl), run_time=0.4)
        self.play(Create(xg1), Create(pg1), run_time=0.6)
        self.play(Transform(xg1, xg_half), Transform(pg1, pg_double),
                  run_time=(d - 1.9) * 0.5, rate_func=smooth)
        self.play(FadeIn(half_note), run_time=0.5)
        self.play(Transform(xg1, self._gauss(ax_x, 1.0, TEAL)),
                  Transform(pg1, self._gauss(ax_p, 1.0, CRIMSON)),
                  run_time=(d - 1.9) * 0.5, rate_func=smooth)


# ── B10 CARD — RECAP endcard ──────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Fourier bandwidth: dx * dk >= 1/2.\nMultiply by h-bar: uncertainty principle.",
                      font=SERIF, color=INK, font_size=30, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
