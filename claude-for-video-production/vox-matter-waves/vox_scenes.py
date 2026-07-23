"""vox_scenes.py — Matter Waves (fresh build, 16:9).

One Scene per GRAPHIC/CARD beat; the compile ladder retimes to measured
audio. Render:  bash scripts/vox_run.sh reels/vox-matter-waves
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

TANGENT = EquationTangent({
    "eyebrow": "de Broglie relation · equation · tangent",
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
        "cost": "Heavier things: waves too small for any instrument.",
    },
    "values_claim": "(unused)",
})


class B02_Title(Scene):            # ~9.5s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=24)
        t = Text("MATTER WAVES", font=SERIF, color=INK, font_size=54,
                 weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("why electrons make stripes", font=SERIF, color=INK,
                 font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(7.3)


class B03_TheReversal(Scene):      # ~9.5s
    def construct(self):
        top = VGroup(Text("light waves", font=SERIF, color=INK, font_size=36),
                     Text("→", font=SERIF, color=NAVY, font_size=44),
                     Text("particles", font=SERIF, color=INK, font_size=36),
                     Text("✓", font=SERIF, color=NAVY, font_size=38))
        top.arrange(RIGHT, buff=0.45).shift(UP * 1.2)
        chip = LabelChip("Einstein, 1905 — film two", accent=NAVY, size=22)
        chip.next_to(top, UP, buff=0.5)
        bottom = VGroup(Text("particles", font=SERIF, color=INK, font_size=36),
                        Text("→", font=SERIF, color=TERRA, font_size=44),
                        Text("waves", font=SERIF, color=INK, font_size=36),
                        Text("?", font=SERIF, color=TERRA, font_size=44,
                             weight=BOLD))
        bottom.arrange(RIGHT, buff=0.45).shift(DOWN * 1.0)
        lb = SerifLabel("de Broglie reverses the arrow", TERRA, size=30)
        lb.next_to(bottom, DOWN, buff=0.7)
        self.play(FadeIn(chip), FadeIn(top, shift=UP * 0.1), run_time=1.0)
        self.wait(1.6)
        self.play(FadeIn(bottom[0]), FadeIn(bottom[1]), FadeIn(bottom[2]),
                  run_time=1.0)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.play(FadeIn(bottom[3], scale=1.4), run_time=0.6)
        self.wait(3.6)


class T01_EqSentences(Scene):      # ~8.5s
    def construct(self):
        anchor = TANGENT.anchor()
        eye = TANGENT.eyebrow()
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        z = TANGENT.zone("sentences")
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in z[0]:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.7)
            self.wait(1.3)
        self.wait(1.4)


class T02_EqGlossary(Scene):       # ~10s
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"\lambda")
        z = TANGENT.zone("glossary", spotlight="λ")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(9.0)


class T03_EqExample(Scene):        # ~10s
    def construct(self):
        anchor = TANGENT.anchor()
        z = TANGENT.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)
        self.wait(1.6)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)
        self.wait(1.8)
        self.play(FadeIn(rows[2]), run_time=0.7)
        self.wait(1.4)
        self.play(FadeIn(rows[3]), run_time=0.7)
        self.wait(2.1)


class B05_AccidentPeaks(Scene):    # ~10s
    def construct(self):
        # before: jumble + flat scatter
        rng = np.random.default_rng(7)
        jumble = VGroup(*[Square(0.09, color=SLATE, fill_opacity=1,
                                 stroke_width=0)
                          .move_to([-4.6 + rng.uniform(0, 2.6),
                                    0.2 + rng.uniform(0, 2.0), 0])
                          .rotate(rng.uniform(0, PI))
                          for _ in range(40)])
        flat = VMobject(color=INK, stroke_width=4)
        flat.set_points_smoothly([np.array([-4.9 + t * 3.0,
                                            -1.9 + 0.12 * np.sin(5 * t), 0.0])
                                  for t in np.linspace(0, 1, 40)])
        lb1 = Text("polycrystal: featureless", font=SERIF, color=INK,
                   font_size=24)
        lb1.next_to(flat, DOWN, buff=0.3)
        self.play(FadeIn(jumble), Create(flat), FadeIn(lb1), run_time=1.4)
        self.wait(1.2)
        heat = LabelChip("annealed — the accident", accent=TERRA, size=24)
        heat.move_to([0.2, 3.0, 0])
        self.play(FadeIn(heat, shift=UP * 0.15), run_time=0.7)
        # after: ordered lattice + sharp peak
        lattice = VGroup(*[Square(0.09, color=SLATE, fill_opacity=1,
                                  stroke_width=0)
                           .move_to([2.0 + 0.34 * i, 0.4 + 0.34 * j, 0])
                           for i in range(8) for j in range(6)])
        def peak(x):
            return -1.9 + 2.2 * np.exp(-((x - 3.6) ** 2) / 0.045)
        pk = VMobject(color=NAVY, stroke_width=5)
        pk.set_points_smoothly([np.array([x, peak(x), 0.0])
                                for x in np.linspace(2.0, 5.2, 80)])
        lb2 = Text("single crystal: sharp peaks", font=SERIF, color=NAVY,
                   font_size=24)
        lb2.next_to(pk, DOWN, buff=0.3)
        self.play(FadeIn(lattice), run_time=1.0)
        self.play(Create(pk), FadeIn(lb2), run_time=1.6, rate_func=linear)
        self.wait(3.5)


class B06_NumbersAgree(Scene):     # ~10s
    def construct(self):
        lb = SerifLabel("a parameter-free prediction", NAVY, size=30)
        lb.to_edge(UP, buff=0.75)
        rows = VGroup(
            Text("54 volts", font=MONO, color=INK, font_size=34),
            Text("→   λ = 0.167 nm", font=MONO, color=INK, font_size=34),
            Text("→   Bragg, d = 0.091 nm", font=MONO, color=INK, font_size=34),
            Text("→   peak at ≈ 50°  — as observed", font=MONO, color=CRIMSON,
                 font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).shift(DOWN * 0.4)
        if rows.width > 11.5:
            rows.scale_to_fit_width(11.5)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.7)
            self.wait(0.9)
        self.wait(2.7)


class B08_TheBuildup(Scene):       # ~10s — THE visual
    def construct(self):
        rng = np.random.default_rng(42)
        counts = [(10, "10"), (200, "200"), (900, "6,000"), (1600, "70,000")]
        panels = VGroup()
        for i, (n, label) in enumerate(counts):
            x0 = -6.1 + i * 3.15
            frame = Rectangle(width=2.85, height=4.4).set_stroke(INK, 1.5)
            frame.move_to([x0 + 1.42, 0.3, 0])
            fringe_bias = min(1.0, i / 2.5)      # randomness -> fringes
            dots = VGroup()
            for _ in range(min(n, 700)):
                while True:
                    y = rng.uniform(-2.0, 2.0)
                    prob = (1 - fringe_bias) + fringe_bias * np.cos(2.6 * y) ** 2
                    if rng.uniform(0, 1) < prob:
                        break
                dots.add(Dot([x0 + rng.uniform(0.12, 2.72), 0.3 + y * 1.05, 0],
                             radius=0.022, color=NAVY))
            cap = Text(label, font=MONO, color=INK, font_size=26)
            cap.next_to(frame, DOWN, buff=0.25)
            panels.add(VGroup(frame, dots, cap))
        for i, p in enumerate(panels):
            self.play(FadeIn(p[0]), FadeIn(p[2]), run_time=0.4)
            self.play(FadeIn(p[1], lag_ratio=0.002),
                      run_time=1.0 if i < 2 else 1.4)
        self.wait(2.4)


class B09_BothPaths(Scene):        # ~10s
    def construct(self):
        src = Dot([-5.5, 0, 0], radius=0.15, color=TERRA)
        wire = Dot([-1.0, 0, 0], radius=0.09, color=INK)
        wl = Text("the splitter", font=SERIF, color=INK, font_size=22)
        wl.next_to(wire, DOWN, buff=0.3)
        screen = Line([4.2, -2.2, 0], [4.2, 2.2, 0], color=INK, stroke_width=3)
        self.add(wire, wl, screen)
        self.play(FadeIn(src), run_time=0.5)
        # two ghost paths that bow around the splitter wire
        path_u = VMobject(color=NAVY, stroke_width=4).set_stroke(opacity=0.5)
        path_u.set_points_smoothly([np.array([-5.5, 0, 0]),
                                    np.array([-1.0, 0.9, 0]),
                                    np.array([4.2, 0.2, 0])])
        path_d = VMobject(color=NAVY, stroke_width=4).set_stroke(opacity=0.5)
        path_d.set_points_smoothly([np.array([-5.5, 0, 0]),
                                    np.array([-1.0, -0.9, 0]),
                                    np.array([4.2, -0.2, 0])])
        self.play(Create(path_u), Create(path_d), run_time=1.8,
                  rate_func=linear)
        lb = SerifLabel("one electron — both paths", NAVY, size=30)
        lb.to_edge(UP, buff=0.75)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        fringes = VGroup(*[Rectangle(width=0.16, height=0.5)
                           .set_fill(NAVY, 0.25 + 0.55 * (np.cos(1.9 * y) ** 2))
                           .set_stroke(width=0)
                           .move_to([4.45, y, 0])
                           for y in np.linspace(-1.9, 1.9, 13)])
        self.play(FadeIn(fringes, lag_ratio=0.05), run_time=1.4)
        land = Dot([4.2, 0.65, 0], radius=0.1, color=TERRA)
        ll = Text("one dot", font=SERIF, color=TERRA, font_size=22)
        ll.next_to(land, RIGHT, buff=0.25)
        if ll.get_right()[0] > 6.6:
            ll.next_to(land, LEFT, buff=0.25)
        self.play(FadeOut(src), FadeIn(land), FadeIn(ll), run_time=0.7)
        self.wait(2.7)


class B11_ScaleBar(Scene):         # ~9.5s
    def construct(self):
        lb = SerifLabel("the de Broglie wavelength of…", NAVY, size=30)
        lb.to_edge(UP, buff=0.75)
        bar = Line([-5.8, -0.6, 0], [5.8, -0.6, 0], color=INK, stroke_width=3)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.play(Create(bar), run_time=1.0)
        marks = [(-4.6, "an electron", "10⁻¹⁰ m", NAVY),
                 (-2.2, "a buckyball", "10⁻¹² m", NAVY),
                 (0.6, "a proton's size", "10⁻¹⁵ m", INK),
                 (4.6, "you, walking", "10⁻³⁵ m", CRIMSON)]
        ring_target = None
        for x, name, val, color in marks:
            tick = Line([x, -0.75, 0], [x, -0.45, 0], color=color,
                        stroke_width=4)
            nm = Text(name, font=SERIF, color=color, font_size=24)
            vl = Text(val, font=MONO, color=color, font_size=24)
            nm.next_to(tick, UP, buff=0.3)
            vl.next_to(tick, DOWN, buff=0.3)
            grp = VGroup(tick, nm, vl)
            self.play(FadeIn(grp, shift=UP * 0.1), run_time=0.6)
            if color == CRIMSON:
                ring_target = nm
        ring = HandRing(ring_target, color=TERRA)
        self.play(Create(ring), run_time=1.0)
        self.wait(2.6)


class B14_Next(Scene):             # ~5s — outro law replaces this slot
    def construct(self):
        eye = Text("NEXT", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE WAVE FUNCTION", font=SERIF, color=INK, font_size=54,
                 weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        s = Text("quantum, vol. 1 · chapter 3", font=SERIF, color=INK,
                 font_size=28)
        eye.to_edge(UP, buff=1.4)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(3.1)
