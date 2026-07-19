"""short/vox_scenes.py — PORTRAIT (9:16) relayouts, The Infinite Square Well.

Generated graphics re-band top-and-bottom for the 4.5 x 8 frame — never cut.
B01/B09 use portrait recreation clips (disclosed); B05 is the sequential
Bohr→Schrödinger cut (hand -916); B10 dropped (--no-endcard: ends on
'Nature obeys').
Safe area ±1.95 x / ±3.4 y; placements carry margin arithmetic (preflight).
Render:  bash scripts/vox_run.sh reels/vox-infinite-square-well/short
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

SAFE_W = 3.8


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def serif_lines(lines, size=26, color=INK, buff=0.16):
    g = VGroup(*[Text(t, font=SERIF, color=color, font_size=size)
                 for t in lines]).arrange(DOWN, buff=buff)
    return fit(g)


def anchor_card(spotlight=None):
    return EquationCard(r"E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}",
                        spotlight=spotlight, width=4.2,
                        plain="E(n) = n²π²ℏ²/2mL²").to_edge(UP, buff=0.9)


def _standing(n, wl, wr, y_base, amp, color=INK, frac=1.0, pts=100):
    xs = np.linspace(wl, wr, pts)
    L = wr - wl
    vm = VMobject(color=color, stroke_width=3)
    vm.set_points_smoothly(
        [np.array([x, y_base + amp * np.sin(n * PI * (x - wl) / (L * frac)), 0])
         for x in xs])
    return vm


class B02_Title(Scene):            # 7.24s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=22)
        eye.to_edge(UP, buff=1.4)
        title = VGroup(Text("THE INFINITE", font=SERIF, color=INK,
                            font_size=46, weight=BOLD),
                       Text("SQUARE WELL", font=SERIF, color=INK,
                            font_size=46, weight=BOLD)).arrange(DOWN, buff=0.18)
        fit(title)
        u = Line(title.get_corner(DL) + DOWN * 0.2,
                 title.get_corner(DR) + DOWN * 0.2, color=CRIMSON,
                 stroke_width=2)
        sub = serif_lines(["why boxes make", "whole numbers"], size=26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(5.0)


class B03_GuitarString(Scene):     # 11.18s — rows re-banded for the tall frame
    def construct(self):
        wl, wr = -1.7, 1.7
        y_rows = [2.3, 1.1, -0.1]                     # modes 1..3, amp 0.4
        pins = VGroup(*[Dot([x, y, 0], radius=0.055, color=INK)
                        for y in y_rows for x in (wl, wr)])
        title = serif_lines(["a string pinned", "at both ends"], size=24,
                            color=NAVY)
        title.to_edge(UP, buff=0.55)                  # y ≈ 3.0..3.45 top area
        self.play(FadeIn(title), FadeIn(pins), run_time=1.0)
        for i, y in enumerate(y_rows, start=1):
            m = _standing(i, wl, wr, y, 0.4)
            self.play(Create(m), run_time=0.85, rate_func=linear)
        bad = _standing(1.33, wl, wr, -1.55, 0.38, color=CRIMSON, frac=0.75)
        bad_lb = serif_lines(["doesn't reach the pin —", "dies"], size=20,
                             color=CRIMSON)
        bad_lb.move_to([0, -2.45, 0])                 # its own band
        self.play(Create(bad), run_time=0.85, rate_func=linear)
        self.play(FadeIn(bad_lb), bad.animate.set_stroke(opacity=0.15),
                  run_time=0.9)
        self.wait(1.2)
        swap = LabelChip("now the wave is |ψ|²", accent=NAVY, size=20)
        fit(swap).to_edge(DOWN, buff=0.6)             # bottom band, ≥ −3.3
        self.play(FadeIn(swap, shift=UP * 0.1), run_time=0.8)
        self.wait(2.8)


class B04_TheOneLine(Scene):       # 10.21s
    def construct(self):
        axis = Line([-1.85, 2.5, 0], [1.85, 2.5, 0], color=INK, stroke_width=2.5)
        alab = serif_lines(["k — any value", "allowed"], size=22)
        alab.next_to(axis, UP, buff=0.25)             # top ≈ 3.4 edge; size ok
        if alab.get_top()[1] > 3.35:
            alab.shift(DOWN * (alab.get_top()[1] - 3.35))
        band = Rectangle(width=3.7, height=0.24).set_fill(NAVY, 0.25)\
            .set_stroke(width=0).move_to([0, 2.5, 0])
        self.play(Create(axis), FadeIn(alab), run_time=0.9)
        self.play(FadeIn(band), run_time=0.8)
        self.wait(0.6)
        chips = VGroup(LabelChip("ψ(0) = 0", accent=TERRA, size=18),
                       LabelChip("ψ(L) = 0", accent=TERRA, size=18))
        chips.arrange(DOWN, buff=0.25)
        fit(chips).move_to([0, 0.9, 0])
        self.play(FadeIn(chips, shift=UP * 0.1), run_time=0.8)
        ticks = VGroup(*[Line([x, 2.36, 0], [x, 2.64, 0], color=CRIMSON,
                              stroke_width=4)
                         for x in np.linspace(-1.55, 1.55, 7)])
        self.play(FadeOut(band), FadeIn(ticks, lag_ratio=0.1), run_time=1.2)
        card = EquationCard(r"\sin(kL) = 0 \Rightarrow kL = n\pi",
                            width=4.2, plain="sin(kL) = 0 → kL = nπ")
        card.move_to([0, -1.6, 0])                    # bottom ≈ −2.4, safe
        self.play(FadeIn(card, scale=1.05), run_time=0.9)
        self.wait(3.6)


class T01_EqSentences(Scene):      # 8.72s
    def construct(self):
        anchor = anchor_card(spotlight="n")
        eye = LabelChip("PARTICLE IN A BOX · TANGENT", accent=CRIMSON, size=15)
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        rows = VGroup()
        for tag, sentence in (("LHS", ["The energy of", "note number n."]),
                              ("RHS", ["n squared, times the", "confinement floor price."])):
            c = Text(tag, font=SERIF, color=WHITE, font_size=15)
            box = SurroundingRectangle(c, buff=0.08).set_fill(NAVY, 1).set_stroke(width=0)
            body = serif_lines(sentence, size=22, buff=0.1)
            rows.add(fit(VGroup(VGroup(box, c), body).arrange(RIGHT, buff=0.25,
                                                              aligned_edge=UP)))
        claim = serif_lines(["whole numbers", "only"], size=24)
        cu = Line(claim.get_corner(DL) + DOWN * 0.1,
                  claim.get_corner(DR) + DOWN * 0.1, color=CRIMSON,
                  stroke_width=1.6)
        rows.add(VGroup(claim, cu))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to(DOWN * 1.3)
        fit(rows)
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.65)
            self.wait(0.95)
        self.wait(1.2)


class T02_EqGlossary(Scene):       # 9.87s
    def construct(self):
        anchor = anchor_card(spotlight="n")
        self.add(anchor)
        data = [
            {"sym_tex": "n", "sym": "n", "role": "the label",
             "mean": "which note — counts humps", "dom": "1, 2, 3, …", "hot": True},
            {"sym_tex": r"\hbar", "sym": "ℏ", "role": "the quantum",
             "mean": "why there's a floor at all", "dom": "1.055×10⁻³⁴ J·s", "hot": False},
            {"sym_tex": r"mL^2", "sym": "mL²", "role": "the scale",
             "mean": "heavier or roomier — lower notes", "dom": "kg·m²", "hot": False},
        ]
        blocks = VGroup()
        for r in data:
            sym = _math(r["sym_tex"], font_size=32,
                        color=CRIMSON if r["hot"] else INK, plain=r["sym"])
            role = Text(r["role"], font=SERIF, font_size=17, slant=ITALIC,
                        color=TERRA if r["hot"] else BLUE)
            topline = VGroup(sym, role).arrange(RIGHT, buff=0.28,
                                                aligned_edge=DOWN)
            mean = Text(r["mean"], font=SERIF, color=INK, font_size=19)
            dom = Text(r["dom"], font=MONO, color=INK, font_size=14)
            blocks.add(fit(VGroup(topline, fit(mean), dom)
                           .arrange(DOWN, aligned_edge=LEFT, buff=0.12)))
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.3)
        fit(blocks)
        self.play(FadeIn(blocks, shift=UP * 0.15), run_time=1.0)
        self.wait(8.9)


class T03_EqExample(Scene):        # 11.96s
    def construct(self):
        anchor = anchor_card(spotlight=r"mL^2")
        self.add(anchor)
        scenario = serif_lines(["electron in 1 nm,", "vs a 1 g marble in 1 cm"],
                               size=21)
        lv = Text("electron: E1 = 0.38 eV", font=MONO, color=CRIMSON,
                  font_size=24)
        rv = Text("marble: ~3×10⁻⁴² eV", font=MONO, color=NAVY, font_size=24)
        pair = VGroup(fit(lv), fit(rv)).arrange(DOWN, buff=0.2)
        verdict = serif_lines(["same law — loud for electrons,", "silent for marbles"],
                              size=21)
        vu = Line(verdict.get_corner(DL) + DOWN * 0.1,
                  verdict.get_corner(DR) + DOWN * 0.1, color=TERRA,
                  stroke_width=1.6)
        cost = serif_lines(["the classical world is arithmetic,", "not a different universe"],
                           size=18)
        stack = VGroup(scenario, pair, VGroup(verdict, vu), cost)
        stack.arrange(DOWN, buff=0.4).move_to(DOWN * 1.3)
        fit(stack)
        self.play(FadeIn(stack[0]), run_time=0.8)
        self.wait(1.9)
        self.play(FadeIn(stack[1], shift=UP * 0.15), run_time=0.9)
        self.wait(2.3)
        self.play(FadeIn(stack[2]), run_time=0.7)
        self.wait(1.7)
        self.play(FadeIn(stack[3]), run_time=0.7)
        self.wait(2.9)


class B06_TheLadder(Scene):        # 10.29s — well TOP, n² ladder BOTTOM (the law)
    def construct(self):
        # well: walls x ±1.75, floor y=0.4, tops y=3.2; modes rows 0.9/1.7/2.5 amp .3
        wl, wr, yf, yt = -1.75, 1.75, 0.4, 3.2
        walls = VGroup(Line([wl, yf, 0], [wl, yt, 0], color=INK, stroke_width=4.5),
                       Line([wr, yf, 0], [wr, yt, 0], color=INK, stroke_width=4.5),
                       Line([wl, yf, 0], [wr, yf, 0], color=INK, stroke_width=4.5))
        self.play(Create(walls), run_time=0.7)
        # ladder BOTTOM: rungs at y = −3.1 + 0.185·n² → −2.9, −2.4, −1.4, −0.1
        for n in (1, 2, 3, 4):
            if n <= 3:
                m = _standing(n, wl, wr, 0.55 + (n - 1) * 0.85, 0.3, color=NAVY)
                nodes = VGroup(*[Dot([wl + (wr - wl) * j / n,
                                      0.55 + (n - 1) * 0.85, 0], radius=0.045,
                                     color=CRIMSON) for j in range(1, n)])
                self.play(Create(m), FadeIn(nodes, lag_ratio=0.2),
                          run_time=0.65, rate_func=linear)
            ry = -3.1 + 0.185 * n * n
            rung = Line([-1.3, ry, 0], [0.9, ry, 0], color=NAVY, stroke_width=3)
            chip = Text(str(n * n), font=MONO, color=INK, font_size=22)
            chip.next_to(rung, RIGHT, buff=0.15)      # ends ≈ 1.5 < 1.95
            self.play(Create(rung), FadeIn(chip), run_time=0.5)
        lb = serif_lines(["the ladder climbs as n²"], size=21, color=NAVY)
        lb.move_to([0, -0.55, 0])                     # between well floor and ladder top... floor 0.4; ladder top rung −0.1: band −0.55 collides? rung 4 at −0.1, lb at −0.55 → clear of rung (−0.1) by 0.3 and of rung 3 (−1.4) by 0.7 ✓
        self.play(FadeIn(lb), run_time=0.8)
        self.wait(2.6)


class B07_NeverZero(Scene):        # 10.45s
    def construct(self):
        # levels re-banded: E=0 dashed at y −0.8, E1 at y 1.0; axis far left x −1.85
        ax = Line([-1.85, -1.6, 0], [-1.85, 1.9, 0], color=INK, stroke_width=2.5)
        e0 = DashedLine([-1.5, -0.8, 0], [1.5, -0.8, 0], color=INK,
                        stroke_width=2.2)
        e0lab = Text("E = 0", font=MONO, color=INK, font_size=22)
        e0lab.next_to(e0, DOWN, buff=0.18)            # centered x 0 — clear of axis −1.85
        self.play(Create(ax), Create(e0), FadeIn(e0lab), run_time=1.0)
        # local strike (no StrikeX in the library)
        x0, y0 = -1.6, -1.0
        x1, y1 = 1.6, -0.6
        s1 = VMobject(color=CRIMSON, stroke_width=5)
        s1.set_points_smoothly([np.array([x0, y0, 0]), np.array([0.03, (y0+y1)/2+0.04, 0]), np.array([x1, y1, 0])])
        s2 = VMobject(color=CRIMSON, stroke_width=5)
        s2.set_points_smoothly([np.array([x0, y1, 0]), np.array([-0.03, (y0+y1)/2-0.04, 0]), np.array([x1, y0, 0])])
        s1._qc_intentional = True; s2._qc_intentional = True
        self.play(Create(s1), Create(s2), run_time=0.8)
        e1 = Line([-1.5, 1.0, 0], [1.5, 1.0, 0], color=NAVY, stroke_width=3.5)
        e1lab = Text("E1 > 0", font=MONO, color=NAVY, font_size=24)
        e1lab.next_to(e1, UP, buff=0.18)
        gap = DoubleArrow([1.72, -0.8, 0], [1.72, 1.0, 0], color=TERRA,
                          buff=0, stroke_width=2.5, tip_length=0.14)
        self.play(Create(e1), FadeIn(e1lab), Create(gap), run_time=1.0)
        card = ValuesClaim("still + confined → σₓσₚ = 0 < ℏ/2", size=20,
                           width=3.9)
        card.move_to([0, 2.75, 0])                    # top band; card ≈ ±0.5 tall → ≤ 3.25
        c1 = VMobject(color=CRIMSON, stroke_width=5)
        c1.set_points_smoothly([np.array([-2.0, 2.4, 0]), np.array([0.02, 2.78, 0]), np.array([2.0, 3.1, 0])])
        c2 = VMobject(color=CRIMSON, stroke_width=5)
        c2.set_points_smoothly([np.array([-2.0, 3.1, 0]), np.array([-0.02, 2.72, 0]), np.array([2.0, 2.4, 0])])
        c1._qc_intentional = True; c2._qc_intentional = True
        self.play(FadeIn(card), run_time=0.9)
        self.play(Create(c1), Create(c2), run_time=0.8)
        bl = serif_lines(["being boxed in", "costs energy"], size=24,
                         color=TERRA)
        bl.to_edge(DOWN, buff=0.62)
        self.play(FadeIn(bl), run_time=0.9)
        self.wait(2.5)


class B08_FemtoSlosh(Scene):       # 8.49s
    def construct(self):
        wl, wr, y0 = -1.8, 1.8, -0.5
        walls = VGroup(Line([wl, y0, 0], [wl, 2.4, 0], color=INK, stroke_width=4),
                       Line([wr, y0, 0], [wr, 2.4, 0], color=INK, stroke_width=4),
                       Line([wl, y0, 0], [wr, y0, 0], color=INK, stroke_width=4))

        def density(theta):
            xs = np.linspace(wl, wr, 100)
            L = wr - wl
            pts = []
            for x in xs:
                u = (x - wl) / L
                p1 = np.sin(PI * u); p2 = np.sin(2 * PI * u)
                d = 0.5 * (p1 * p1 + p2 * p2) + p1 * p2 * np.cos(theta)
                pts.append(np.array([x, y0 + 1.9 * d * 0.7, 0]))
            poly = Polygon(*(pts + [np.array([wr, y0, 0]), np.array([wl, y0, 0])]))
            poly.set_fill(NAVY, 0.35).set_stroke(NAVY, 3)
            return poly

        dens = density(0.0)
        self.play(Create(walls), FadeIn(dens), run_time=1.0)
        chip = LabelChip("T ≈ 3.7 femtoseconds", accent=CRIMSON, size=20)
        fit(chip).move_to([0, -2.2, 0])
        for i, theta in enumerate((PI, 2 * PI, 3 * PI, 4 * PI)):
            self.play(Transform(dens, density(theta)), run_time=1.3,
                      rate_func=linear)
            if i == 1:
                self.play(FadeIn(chip, scale=1.1), run_time=0.5)
        self.wait(0.5)
