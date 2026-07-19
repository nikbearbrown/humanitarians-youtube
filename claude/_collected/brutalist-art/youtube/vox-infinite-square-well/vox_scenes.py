"""vox_scenes.py — The Infinite Square Well (film six, 16:9).

One Scene per GRAPHIC/CARD beat; the compile ladder retimes to measured
audio. Durations from beat_sheet.json (audio locked 2026-07-06):
B02 7.24 · B03 11.18 · B04 10.21 · T01 8.72 · T02 9.87 · T03 12.54 ·
B06 10.29 · B07 10.45 · B08 8.49 · B10 6.58.
Safe area ±6.4 x / ±3.5 y; fixed placements carry margin arithmetic in
comments (desk preflight — film-five practice).
Render:  bash scripts/vox_run.sh reels/vox-infinite-square-well
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

TANGENT = EquationTangent({
    "eyebrow": "particle in a box · tangent",
    "equation": "E(n) = n²π²ℏ²/2mL²",
    "equation_tex": r"E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}",
    "lhs": "The energy of note number n.",
    "rhs": "n squared, times the confinement floor price.",
    "claim": "Confinement writes the menu — whole numbers only.",
    "glossary": [
        {"sym": "n", "sym_tex": "n", "role": "the label",
         "mean": "which note — counts the humps", "dom": "1, 2, 3, …"},
        {"sym": "ℏ", "sym_tex": r"\hbar", "role": "the quantum",
         "mean": "why there's a floor at all", "dom": "1.055×10⁻³⁴ J·s"},
        {"sym": "mL²", "sym_tex": r"mL^2", "role": "the scale",
         "mean": "heavier or roomier — lower notes", "dom": "kg·m²"},
    ],
    "example": {
        "scenario": "Electron in L = 1 nm, versus a 1 g marble in L = 1 cm.",
        "lhs_val": "electron: E1 = 0.38 eV", "rhs_val": "marble: ~3×10⁻⁴² eV",
        "verdict": "same law — loud for electrons, silent for marbles",
        "cost": "The classical world is arithmetic, not a different universe.",
    },
    "values_claim": "(merged into the sentences claim — simple equation)",
})


def _strike(around, color=CRIMSON, pad=0.15):
    """Hand-drawn X across a mobject (vox_graphics has HandRing but no
    StrikeX — SKILL.md prose notwithstanding; the library wins). Declares
    itself intentional so Gate B exempts the overlap."""
    x0, y0, _ = np.asarray(around.get_corner(DL)) - np.array([pad, pad, 0.0])
    x1, y1, _ = np.asarray(around.get_corner(UR)) + np.array([pad, pad, 0.0])
    rng = np.random.default_rng(11)
    def stroke(a, b):
        vm = VMobject(color=color, stroke_width=6)
        mid = [(a[0]+b[0])/2 + rng.uniform(-0.06, 0.06),
               (a[1]+b[1])/2 + rng.uniform(-0.06, 0.06), 0]
        vm.set_points_smoothly([np.array(a), np.array(mid), np.array(b)])
        vm._qc_intentional = True
        return vm
    g = VGroup(stroke([x0, y0, 0], [x1, y1, 0]),
               stroke([x0, y1, 0], [x1, y0, 0]))
    g._qc_intentional = True
    return g


def _standing(n, wl, wr, y_base, amp, color=INK, frac=1.0, pts=120):
    """Standing-wave mode n between pins; frac<1 draws a wave that misses
    the right pin (the wrong-fit wave)."""
    xs = np.linspace(wl, wr, pts)
    L = wr - wl
    vm = VMobject(color=color, stroke_width=3.5)
    vm.set_points_smoothly(
        [np.array([x, y_base + amp * np.sin(n * PI * (x - wl) / (L * frac)), 0])
         for x in xs])
    return vm


class B02_Title(Scene):            # 7.24s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE INFINITE SQUARE WELL", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("why boxes make whole numbers", font=SERIF, color=INK,
                 font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(5.0)


class B03_GuitarString(Scene):     # 11.18s — the analogy, then its break
    def construct(self):
        wl, wr = -4.6, 4.6
        y_rows = [1.7, 0.2, -1.3]                     # modes 1..3, amp 0.55 → rows clear
        pins = VGroup(*[Dot([x, y, 0], radius=0.07, color=INK)
                        for y in y_rows for x in (wl, wr)])
        title = SerifLabel("a string pinned at both ends", NAVY, size=30)
        title.to_edge(UP, buff=0.7)                   # y ≈ 2.9..3.3, clear of row 1.7+0.55
        self.play(Write(title[0]), Create(title[1]), FadeIn(pins), run_time=1.0)
        for i, y in enumerate(y_rows, start=1):
            m = _standing(i, wl, wr, y, 0.55)
            self.play(Create(m), run_time=0.9, rate_func=linear)
        # the wrong-fit wave: misses the right pin — its own row at y=-2.8
        bad = _standing(1.33, wl, wr, -2.8, 0.5, color=CRIMSON, frac=0.75)
        bad_lb = Text("doesn't reach the pin — dies", font=SERIF, color=CRIMSON,
                      font_size=24)
        bad_lb.next_to(bad, DOWN, buff=0.18)          # bottom ≈ −3.45+... ≈ −3.4 edge
        if bad_lb.get_bottom()[1] < -3.4:
            bad_lb.shift(UP * (-3.4 - bad_lb.get_bottom()[1]))
        self.play(Create(bad), run_time=0.9, rate_func=linear)
        self.play(FadeIn(bad_lb), bad.animate.set_stroke(opacity=0.15),
                  run_time=0.9)
        self.wait(1.4)
        # the swap: same walls, different thing waving
        swap = LabelChip("now the wave is |ψ|² — probability itself",
                         accent=NAVY, size=24)
        swap.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(swap, shift=UP * 0.1), run_time=0.8)
        self.wait(2.9)


class B04_TheOneLine(Scene):       # 10.21s — the continuum collapses to ticks
    def construct(self):
        # k-axis: continuous band, y = 1.6
        axis = Line([-5.6, 1.6, 0], [5.6, 1.6, 0], color=INK, stroke_width=3)
        alab = Text("k — any value allowed", font=SERIF, color=INK, font_size=26)
        alab.next_to(axis, UP, buff=0.3)
        band = Rectangle(width=11.2, height=0.28).set_fill(NAVY, 0.25)\
            .set_stroke(width=0).move_to([0, 1.6, 0])
        self.play(Create(axis), FadeIn(alab), run_time=0.9)
        self.play(FadeIn(band), run_time=0.8)
        self.wait(0.6)
        chips = VGroup(LabelChip("ψ(0) = 0", accent=TERRA, size=22),
                       LabelChip("ψ(L) = 0", accent=TERRA, size=22))
        chips.arrange(RIGHT, buff=0.5).move_to([0, 0.1, 0])
        self.play(FadeIn(chips, shift=UP * 0.1), run_time=0.8)
        # collapse: band out, discrete ticks in (kL = nπ)
        ticks = VGroup(*[Line([x, 1.42, 0], [x, 1.78, 0], color=CRIMSON,
                              stroke_width=5)
                         for x in np.linspace(-4.8, 4.8, 7)])
        self.play(FadeOut(band), FadeIn(ticks, lag_ratio=0.1), run_time=1.2)
        card = EquationCard(r"\sin(kL) = 0 \;\Rightarrow\; kL = n\pi",
                            width=7.0, plain="sin(kL) = 0 → kL = nπ")
        card.move_to([0, -2.0, 0])                    # card ±3.5 wide, y −1.0..−3.0
        self.play(FadeIn(card, scale=1.05), run_time=0.9)
        self.wait(3.6)


class T01_EqSentences(Scene):      # 8.72s
    def construct(self):
        anchor = TANGENT.anchor(spotlight="n")
        eye = TANGENT.eyebrow()
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        z = TANGENT.zone("sentences")
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in z[0]:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.65)
            self.wait(1.0)
        self.wait(2.4)


class T02_EqGlossary(Scene):       # 9.87s
    def construct(self):
        anchor = TANGENT.anchor(spotlight="n")
        z = TANGENT.zone("glossary", spotlight="n")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(8.9)


class T03_EqExample(Scene):        # 12.54s
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"mL^2")
        z = TANGENT.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)
        self.wait(2.0)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)
        self.wait(2.4)
        self.play(FadeIn(rows[2]), run_time=0.7)
        self.wait(1.8)
        self.play(FadeIn(rows[3]), run_time=0.7)
        self.wait(3.2)


class B06_TheLadder(Scene):        # 10.29s — modes + nodes LEFT, n² rungs RIGHT
    def construct(self):
        # well: walls x −5.9/−0.9, floor −2.5, top 2.7
        wl, wr, yf, yt = -5.9, -0.9, -2.5, 2.7
        walls = VGroup(Line([wl, yf, 0], [wl, yt, 0], color=INK, stroke_width=5),
                       Line([wr, yf, 0], [wr, yt, 0], color=INK, stroke_width=5),
                       Line([wl, yf, 0], [wr, yf, 0], color=INK, stroke_width=5))
        self.play(Create(walls), run_time=0.8)
        # rungs at heights ∝ n² (scaled): E1..E4 → y = −2.6 + 0.3·n²·(4.9/16)
        rungs = [(1, "1"), (2, "4"), (3, "9"), (4, "16")]
        for n, lab in rungs:
            yb = yf + 0.55 + (n - 1) * 1.25            # mode rows: −1.95, −0.7, 0.55, 1.8; amp .45 → max 2.25 < 2.7
            m = _standing(n, wl, wr, yb, 0.45, color=NAVY)
            nodes = VGroup(*[Dot([wl + (wr - wl) * j / n, yb, 0], radius=0.055,
                                 color=CRIMSON) for j in range(1, n)])
            ry = -2.6 + (n * n) * 0.3                  # rung y: −2.3, −1.4, +0.1, +2.2 < 3.5
            rung = Line([1.0, ry, 0], [5.0, ry, 0], color=NAVY, stroke_width=3.5)
            chip = Text(lab, font=MONO, color=INK, font_size=26)
            chip.next_to(rung, RIGHT, buff=0.2)        # ends ≈ 5.6 < 6.4
            self.play(Create(m), run_time=0.55, rate_func=linear)
            self.play(FadeIn(nodes, lag_ratio=0.2), Create(rung), FadeIn(chip),
                      run_time=0.55)
        lb = SerifLabel("nodes: 0, 1, 2, 3 — the ladder climbs as n²", NAVY,
                        size=28)
        lb.to_edge(UP, buff=0.55)                      # y ≈ 3.1..3.45... size 28 ≈ 0.38 tall → 3.07..3.45 edge
        lb.shift(DOWN * 0.1)                           # clear of ±3.5 with margin
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.wait(3.0)


class B07_NeverZero(Scene):        # 10.45s — the crimson X on E = 0
    def construct(self):
        # energy axis at FAR left x = −6.05 so level labels (centered ≈ −4.3)
        # never straddle it — Gate B text-on-line fix
        ax = Line([-6.05, -2.6, 0], [-6.05, 2.6, 0], color=INK, stroke_width=3)
        e0 = DashedLine([-5.8, -2.2, 0], [-2.8, -2.2, 0], color=INK,
                        stroke_width=2.5)
        e0lab = Text("E = 0", font=MONO, color=INK, font_size=26)
        e0lab.next_to(e0, DOWN, buff=0.2)
        self.play(Create(ax), Create(e0), FadeIn(e0lab), run_time=1.0)
        x_mark = _strike(e0, color=CRIMSON)
        self.play(Create(x_mark), run_time=0.8)
        e1 = Line([-5.8, -0.6, 0], [-2.8, -0.6, 0], color=NAVY, stroke_width=4)
        e1lab = Text("E1 > 0", font=MONO, color=NAVY, font_size=28)
        e1lab.next_to(e1, UP, buff=0.2)
        gap = DoubleArrow([-2.5, -2.2, 0], [-2.5, -0.6, 0], color=TERRA,
                          buff=0, stroke_width=3, tip_length=0.18)
        gaplab = Text("the floor", font=SERIF, color=TERRA, font_size=24,
                      slant=ITALIC)
        gaplab.next_to(gap, RIGHT, buff=0.15)          # ends ≈ −0.9, safe
        self.play(Create(e1), FadeIn(e1lab), run_time=0.9)
        self.play(Create(gap), FadeIn(gaplab), run_time=0.8)
        # RIGHT: the contradiction card (terracotta tint), struck through
        card = ValuesClaim("still + confined  →  σₓ·σₚ = 0  <  ℏ/2",
                           size=28, width=6.2)
        card.move_to([2.9, 0.3, 0])                    # spans x −0.2..6.0, safe
        strike = _strike(card, color=CRIMSON)
        self.play(FadeIn(card), run_time=0.9)
        self.play(Create(strike), run_time=0.8)
        bl = SerifLabel("being boxed in costs energy", TERRA, size=30)
        bl.to_edge(DOWN, buff=0.6)
        self.play(Write(bl[0]), Create(bl[1]), run_time=0.9)
        self.wait(2.4)


class B08_FemtoSlosh(Scene):       # 8.49s — the film-five rhyme
    def construct(self):
        wl, wr, y0 = -5.2, 5.2, -0.9
        walls = VGroup(Line([wl, y0, 0], [wl, 2.5, 0], color=INK, stroke_width=4),
                       Line([wr, y0, 0], [wr, 2.5, 0], color=INK, stroke_width=4),
                       Line([wl, y0, 0], [wr, y0, 0], color=INK, stroke_width=4))

        def density(theta):
            xs = np.linspace(wl, wr, 120)
            L = wr - wl
            pts = []
            for x in xs:
                u = (x - wl) / L
                p1 = np.sin(PI * u); p2 = np.sin(2 * PI * u)
                d = 0.5 * (p1 * p1 + p2 * p2) + p1 * p2 * np.cos(theta)
                pts.append(np.array([x, y0 + 2.2 * d * 0.7, 0]))
            poly = Polygon(*(pts + [np.array([wr, y0, 0]), np.array([wl, y0, 0])]))
            poly.set_fill(NAVY, 0.35).set_stroke(NAVY, 3)
            return poly

        dens = density(0.0)
        self.play(Create(walls), FadeIn(dens), run_time=1.1)
        chip = LabelChip("T ≈ 3.7 femtoseconds", accent=CRIMSON, size=24)
        chip.move_to([0, -2.6, 0])
        for i, theta in enumerate((PI, 2 * PI, 3 * PI, 4 * PI)):
            self.play(Transform(dens, density(theta)), run_time=1.35,
                      rate_func=linear)
            if i == 1:                                 # chip lands on the first full return
                self.play(FadeIn(chip, scale=1.1), run_time=0.5)
        self.wait(0.5)


class B10_Next(Scene):             # 6.58s — outro law replaces this slot
    def construct(self):
        eye = Text("NEXT", font=SERIF, color=BLUE, font_size=24)
        t = Text("FINITE WELLS & BARRIERS", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        s = Text("quantum, vol. 1 · chapter 6", font=SERIF, color=INK,
                 font_size=28)
        eye.to_edge(UP, buff=1.4)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(4.7)
