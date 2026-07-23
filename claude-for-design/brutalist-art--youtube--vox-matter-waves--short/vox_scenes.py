"""short/vox_scenes.py — PORTRAIT (9:16) relayouts, Matter Waves.

Generated graphics re-band top-and-bottom for the 4.5 x 8 frame — never cut.
B14 needs no portrait scene: the outro law brands it from the 9:16 pool.
Render:  bash scripts/vox_run.sh reels/vox-matter-waves/short
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


TANGENT = EquationTangent({
    "eyebrow": "de Broglie relation · tangent",
    "equation": "λ = h / p",
    "equation_tex": r"\lambda = \frac{h}{p}",
    "lhs": "The wavelength of matter itself.",
    "rhs": "Planck's constant, divided by momentum.",
    "claim": "Everything that moves has a wavelength — everything.",
    "glossary": [
        {"sym": "λ", "sym_tex": r"\lambda", "role": "the prediction",
         "mean": "the matter wavelength", "dom": "meters"},
        {"sym": "p", "sym_tex": "p", "role": "variable",
         "mean": "momentum — mass times velocity", "dom": "kg·m/s"},
        {"sym": "h", "sym_tex": "h", "role": "constant of nature",
         "mean": "Planck's constant — same h, third film", "dom": "6.626×10⁻³⁴ J·s"},
    ],
    "example": {
        "scenario": "An electron accelerated through 150 volts.",
        "lhs_val": "λ ≈ 0.1 nm", "rhs_val": "atoms: ~0.1 nm apart",
        "verdict": "matter wave ≈ crystal spacing — testable",
        "cost": "Heavier things: waves too small to see.",
    },
    "values_claim": "(unused)",
})


def anchor_card(spotlight=None):
    return EquationCard(r"\lambda = \frac{h}{p}", spotlight=spotlight,
                        width=4.2, plain="λ = h / p").to_edge(UP, buff=1.1)


class B02_Title(Scene):            # 8.72s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=22)
        eye.to_edge(UP, buff=1.4)
        title = VGroup(Text("MATTER", font=SERIF, color=INK, font_size=52,
                            weight=BOLD),
                       Text("WAVES", font=SERIF, color=INK, font_size=52,
                            weight=BOLD)).arrange(DOWN, buff=0.18)
        fit(title)
        u = Line(title.get_corner(DL) + DOWN * 0.2,
                 title.get_corner(DR) + DOWN * 0.2, color=CRIMSON,
                 stroke_width=2)
        sub = serif_lines(["why electrons", "make stripes"], size=26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(6.5)


class B03_TheReversal(Scene):      # 9.43s — stacked vertically
    def construct(self):
        chip = LabelChip("Einstein — film two", accent=NAVY, size=18)
        chip.to_edge(UP, buff=1.3)
        top = serif_lines(["light waves", "→ particles  ✓"], size=32)
        bottom = serif_lines(["particles", "→ waves  ?"], size=32)
        for t in bottom:
            t.set_color(INK)
        stack = VGroup(top, bottom).arrange(DOWN, buff=1.1).move_to(DOWN * 0.4)
        lb = serif_lines(["de Broglie reverses", "the arrow"], size=26,
                         color=TERRA)
        lb.next_to(stack, DOWN, buff=0.7)
        self.play(FadeIn(chip), FadeIn(top, shift=UP * 0.1), run_time=1.0)
        self.wait(1.6)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=1.0)
        self.play(FadeIn(lb), run_time=0.9)
        self.wait(3.9)


class T01_EqSentences(Scene):      # 7.97s
    def construct(self):
        anchor = anchor_card()
        eye = LabelChip("DE BROGLIE · TANGENT", accent=CRIMSON, size=16)
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        rows = VGroup()
        for tag, sentence in (("LHS", ["The wavelength of", "matter itself."]),
                              ("RHS", ["Planck's constant,", "divided by momentum."])):
            c = Text(tag, font=SERIF, color=WHITE, font_size=15)
            box = SurroundingRectangle(c, buff=0.08).set_fill(NAVY, 1).set_stroke(width=0)
            body = serif_lines(sentence, size=23, buff=0.1)
            rows.add(fit(VGroup(VGroup(box, c), body).arrange(RIGHT, buff=0.25,
                                                              aligned_edge=UP)))
        claim = serif_lines(["Everything that moves", "has a wavelength."], size=23)
        cu = Line(claim.get_corner(DL) + DOWN * 0.1,
                  claim.get_corner(DR) + DOWN * 0.1, color=CRIMSON,
                  stroke_width=1.6)
        rows.add(VGroup(claim, cu))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.1)
        fit(rows)
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.7)
            self.wait(1.1)
        self.wait(1.0)


class T02_EqGlossary(Scene):       # 10.63s
    def construct(self):
        anchor = anchor_card(spotlight=r"\lambda")
        self.add(anchor)
        blocks = VGroup()
        for r in TANGENT.d["glossary"]:
            hot = r["sym"] == "λ"
            sym = _math(r["sym_tex"], font_size=32,
                        color=CRIMSON if hot else INK, plain=r["sym"])
            role = Text(r["role"], font=SERIF, font_size=17, slant=ITALIC,
                        color=TERRA if hot else BLUE)
            topline = VGroup(sym, role).arrange(RIGHT, buff=0.28,
                                                aligned_edge=DOWN)
            mean = Text(r["mean"], font=SERIF, color=INK, font_size=19)
            dom = Text(r["dom"], font=MONO, color=INK, font_size=14)
            blocks.add(fit(VGroup(topline, fit(mean), dom)
                           .arrange(DOWN, aligned_edge=LEFT, buff=0.12)))
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.2)
        fit(blocks)
        self.play(FadeIn(blocks, shift=UP * 0.15), run_time=1.0)
        self.wait(9.6)


class T03_EqExample(Scene):        # 10.89s
    def construct(self):
        anchor = anchor_card()
        self.add(anchor)
        scenario = serif_lines(["An electron accelerated", "through 150 volts."],
                               size=22)
        lv = Text("λ ≈ 0.1 nm", font=MONO, color=CRIMSON, font_size=30)
        rv = Text("atoms: ~0.1 nm apart", font=MONO, color=NAVY, font_size=26)
        pair = VGroup(fit(lv), fit(rv)).arrange(DOWN, buff=0.2)
        verdict = serif_lines(["matter wave ≈ crystal", "spacing — testable"],
                              size=23)
        vu = Line(verdict.get_corner(DL) + DOWN * 0.1,
                  verdict.get_corner(DR) + DOWN * 0.1, color=TERRA,
                  stroke_width=1.6)
        cost = serif_lines(["Heavier things: waves", "too small to see."],
                           size=19)
        stack = VGroup(scenario, pair, VGroup(verdict, vu), cost)
        stack.arrange(DOWN, buff=0.42).move_to(DOWN * 1.15)
        fit(stack)
        self.play(FadeIn(stack[0]), run_time=0.8)
        self.wait(1.9)
        self.play(FadeIn(stack[1], shift=UP * 0.15), run_time=0.9)
        self.wait(2.1)
        self.play(FadeIn(stack[2]), run_time=0.7)
        self.wait(1.7)
        self.play(FadeIn(stack[3]), run_time=0.7)
        self.wait(2.1)


class B05_AccidentPeaks(Scene):    # ~10s — before above, after below
    def construct(self):
        rng = np.random.default_rng(7)
        jumble = VGroup(*[Square(0.08, color=SLATE, fill_opacity=1,
                                 stroke_width=0)
                          .move_to([-1.6 + rng.uniform(0, 1.7),
                                    2.0 + rng.uniform(0, 1.3), 0])
                          .rotate(rng.uniform(0, PI))
                          for _ in range(30)])
        flat = VMobject(color=INK, stroke_width=3.5)
        flat.set_points_smoothly([np.array([0.4 + t * 1.5,
                                            2.6 + 0.1 * np.sin(5 * t), 0.0])
                                  for t in np.linspace(0, 1, 30)])
        lb1 = Text("featureless", font=SERIF, color=INK, font_size=20)
        lb1.next_to(flat, DOWN, buff=0.2)
        self.play(FadeIn(jumble), Create(flat), FadeIn(lb1), run_time=1.4)
        self.wait(1.0)
        heat = LabelChip("annealed — the accident", accent=TERRA, size=20)
        fit(heat, 3.6).move_to([0, 0.35, 0])
        self.play(FadeIn(heat, shift=UP * 0.15), run_time=0.7)
        lattice = VGroup(*[Square(0.08, color=SLATE, fill_opacity=1,
                                  stroke_width=0)
                           .move_to([-1.6 + 0.28 * i, -2.4 + 0.28 * j, 0])
                           for i in range(7) for j in range(5)])
        def peak(x):
            return -2.7 + 1.6 * np.exp(-((x - 1.3) ** 2) / 0.03)
        pk = VMobject(color=NAVY, stroke_width=4.5)
        pk.set_points_smoothly([np.array([x, peak(x), 0.0])
                                for x in np.linspace(0.4, 2.1, 60)])
        lb2 = Text("sharp peaks", font=SERIF, color=NAVY, font_size=20)
        lb2.next_to(pk, DOWN, buff=0.2)
        self.play(FadeIn(lattice), run_time=1.0)
        self.play(Create(pk), FadeIn(lb2), run_time=1.5, rate_func=linear)
        self.wait(3.4)


class B06_NumbersAgree(Scene):     # ~10s
    def construct(self):
        lb = serif_lines(["a parameter-free", "prediction"], size=28,
                         color=NAVY)
        lb.to_edge(UP, buff=1.2)
        rows = VGroup(
            Text("54 volts", font=MONO, color=INK, font_size=28),
            Text("→ λ = 0.167 nm", font=MONO, color=INK, font_size=28),
            Text("→ Bragg, d = 0.091 nm", font=MONO, color=INK, font_size=28),
            Text("→ peak ≈ 50°", font=MONO, color=CRIMSON, font_size=28),
            Text("as observed", font=SERIF, color=CRIMSON, font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 0.7)
        fit(rows)
        self.play(FadeIn(lb), run_time=0.9)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.6)
            self.wait(0.7)
        self.wait(2.4)


class B08_TheBuildup(Scene):       # ~10s — 2x2 grid
    def construct(self):
        rng = np.random.default_rng(42)
        counts = [(10, "10"), (200, "200"), (700, "6,000"), (1300, "70,000")]
        panels = VGroup()
        pos = [(-1.15, 2.0), (1.15, 2.0), (-1.15, -1.6), (1.15, -1.6)]
        for i, ((n, label), (cx, cy)) in enumerate(zip(counts, pos)):
            frame = Rectangle(width=2.0, height=2.9).set_stroke(INK, 1.5)
            frame.move_to([cx, cy, 0])
            fringe_bias = min(1.0, i / 2.5)
            dots = VGroup()
            for _ in range(min(n, 500)):
                while True:
                    y = rng.uniform(-1.3, 1.3)
                    prob = (1 - fringe_bias) + fringe_bias * np.cos(3.4 * y) ** 2
                    if rng.uniform(0, 1) < prob:
                        break
                dots.add(Dot([cx + rng.uniform(-0.92, 0.92), cy + y, 0],
                             radius=0.018, color=NAVY))
            cap = Text(label, font=MONO, color=INK, font_size=20)
            cap.next_to(frame, DOWN, buff=0.15)
            panels.add(VGroup(frame, dots, cap))
        for i, p in enumerate(panels):
            self.play(FadeIn(p[0]), FadeIn(p[2]), run_time=0.35)
            self.play(FadeIn(p[1], lag_ratio=0.002),
                      run_time=0.9 if i < 2 else 1.3)
        self.wait(2.6)


class B09_BothPaths(Scene):        # ~10s — vertical: source top, screen bottom
    def construct(self):
        src = Dot([0, 3.1, 0], radius=0.13, color=TERRA)
        wire = Dot([0, 0.9, 0], radius=0.08, color=INK)
        wl = Text("the splitter", font=SERIF, color=INK, font_size=18)
        fit(wl, 0.95)
        wl.move_to([1.42, 1.35, 0])            # clear of both bowed paths
        screen = Line([-1.9, -2.4, 0], [1.9, -2.4, 0], color=INK,
                      stroke_width=3)
        self.add(wire, wl, screen)
        self.play(FadeIn(src), run_time=0.5)
        path_l = VMobject(color=NAVY, stroke_width=4).set_stroke(opacity=0.5)
        path_l.set_points_smoothly([np.array([0, 3.1, 0]),
                                    np.array([-0.85, 0.9, 0]),
                                    np.array([-0.2, -2.4, 0])])
        path_r = VMobject(color=NAVY, stroke_width=4).set_stroke(opacity=0.5)
        path_r.set_points_smoothly([np.array([0, 3.1, 0]),
                                    np.array([0.85, 0.9, 0]),
                                    np.array([0.2, -2.4, 0])])
        self.play(Create(path_l), Create(path_r), run_time=1.8,
                  rate_func=linear)
        lb = serif_lines(["one electron —", "both paths"], size=22,
                         color=NAVY)
        lb.move_to([0, -3.02, 0])              # below the detector, off the paths
        self.play(FadeIn(lb), run_time=0.9)
        fringes = VGroup(*[Rectangle(width=0.42, height=0.14)
                           .set_fill(NAVY, 0.25 + 0.55 * (np.cos(2.4 * x) ** 2))
                           .set_stroke(width=0)
                           .move_to([x, -2.62, 0])
                           for x in np.linspace(-1.7, 1.7, 11)])
        self.play(FadeIn(fringes, lag_ratio=0.05), run_time=1.4)
        land = Dot([0.55, -2.4, 0], radius=0.09, color=TERRA)
        self.play(FadeOut(src), FadeIn(land), run_time=0.7)
        self.wait(2.6)


class B11_ScaleBar(Scene):         # ~9.5s — VERTICAL scale (portrait-native)
    def construct(self):
        lb = serif_lines(["the de Broglie", "wavelength of…"], size=26,
                         color=NAVY)
        lb.to_edge(UP, buff=1.1)
        bar = Line([-1.5, 2.0, 0], [-1.5, -3.0, 0], color=INK, stroke_width=3)
        self.play(FadeIn(lb), run_time=0.9)
        self.play(Create(bar), run_time=1.0)
        marks = [(1.5, "an electron", "10⁻¹⁰ m", NAVY),
                 (0.3, "a buckyball", "10⁻¹² m", NAVY),
                 (-0.9, "a proton's size", "10⁻¹⁵ m", INK),
                 (-2.6, "you, walking", "10⁻³⁵ m", CRIMSON)]
        ring_target = None
        for y, name, val, color in marks:
            tick = Line([-1.65, y, 0], [-1.35, y, 0], color=color,
                        stroke_width=4)
            nm = Text(name, font=SERIF, color=color, font_size=22)
            vl = Text(val, font=MONO, color=color, font_size=20)
            grp = VGroup(nm, vl).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            grp.next_to(tick, RIGHT, buff=0.3)
            fit(grp, 2.9)
            self.play(FadeIn(tick), FadeIn(grp, shift=RIGHT * 0.1),
                      run_time=0.55)
            if color == CRIMSON:
                ring_target = nm
        ring = HandRing(ring_target, color=TERRA)
        self.play(Create(ring), run_time=1.0)
        self.wait(2.4)
