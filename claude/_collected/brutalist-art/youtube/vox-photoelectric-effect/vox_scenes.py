"""vox_scenes.py — The Photoelectric Effect (fresh build, 16:9).

One Scene per GRAPHIC/CARD beat. Scene lengths are near the plan estimates;
the compile ladder retimes each fragment to the measured audio (±5% exact,
short clips slow to fit). Render everything:
  bash scripts/vox_run.sh reels/vox-photoelectric-effect
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

X0, X1, Y0, Y1 = -5.2, 5.6, -2.6, 3.0


def smooth_curve(fn, x0, x1, color, width=5, n=90):
    v = VMobject(color=color, stroke_width=width)
    v.set_points_smoothly([np.array([x, fn(x), 0.0])
                           for x in np.linspace(x0, x1, n)])
    return v


def hand_strike(m, color=TERRA):
    """The editor's pen: a slightly wobbly strike through a mobject.
    Declared _qc_intentional — striking text is the point, not a collision."""
    l, r = m.get_corner(DL), m.get_corner(UR)
    v = VMobject(color=color, stroke_width=6)
    pts = [np.array([l[0] - 0.15 + t * (r[0] - l[0] + 0.3),
                     l[1] + t * (r[1] - l[1]) + 0.06 * np.sin(9 * t), 0.0])
           for t in np.linspace(0, 1, 24)]
    v.set_points_smoothly(pts)
    v._qc_intentional = True
    return v


TANGENT = EquationTangent({
    "eyebrow": "Photoelectric law · equation · tangent",
    "equation": "Kmax = hν − Φ",
    "equation_tex": r"K_{max} = h\nu - \Phi",
    "lhs": "The fastest electron's kinetic energy.",
    "rhs": "The photon's payment, minus the metal's exit fee.",
    "claim": "Exactly this — each photon acts alone, whole or not at all.",
    "glossary": [
        {"sym": "Kmax", "sym_tex": r"K_{max}", "role": "quantity",
         "mean": "fastest electron's energy", "dom": "eV"},
        {"sym": "hν", "sym_tex": r"h\nu", "role": "the payment",
         "mean": "one photon's energy", "dom": "eV"},
        {"sym": "Φ", "sym_tex": r"\Phi", "role": "constant of the metal",
         "mean": "work function — the exit fee", "dom": "sodium: 2.28 eV"},
    ],
    "example": {
        "scenario": "UV at 300 nm on sodium. Fee: 2.28 eV.",
        "lhs_val": "UV pays: 4.13 eV", "rhs_val": "green pays: 2.27 eV",
        "verdict": "UV: keeps 1.85 eV · green: 0.01 short — nothing",
        "cost": "Sub-threshold photons never add up. Each acts alone.",
    },
    "values_claim": "(unused)",
})


class B02_Title(Scene):            # ~10s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE PHOTOELECTRIC EFFECT", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("how light came apart in chunks", font=SERIF, color=INK,
                 font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(7.8)


class B05_MoreNotFaster(Scene):    # ~9.5s — more electrons, same energy
    def construct(self):
        lb = SerifLabel("brighter light: more, not faster", NAVY, size=30)
        lb.to_edge(UP, buff=0.55)
        row1 = IsotypeGrid([8], [NAVY], per_row=8, size=0.42, gap=0.3)
        row1.move_to(UP * 0.6)
        row2 = IsotypeGrid([16], [NAVY], per_row=8, size=0.42, gap=0.3)
        row2.next_to(row1, DOWN, buff=0.8)
        dim = LabelChip("dim", accent=BLUE, size=22)
        dim.next_to(row1, LEFT, buff=0.5)
        bright = LabelChip("2× bright", accent=BLUE, size=22)
        bright.next_to(row2, LEFT, buff=0.5)
        same = LabelChip("same energy, each", accent=TERRA, size=24)
        same.next_to(row2, DOWN, buff=0.55)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.8)
        self.play(FadeIn(dim), run_time=0.4)
        self.play(row1.count_up(1.6, lag_ratio=0.02))
        self.play(FadeIn(bright), run_time=0.4)
        self.play(row2.count_up(2.2, lag_ratio=0.01))
        self.play(FadeIn(same, shift=UP * 0.15), run_time=0.7)
        self.wait(3.4)


class B07_WavesCant(Scene):        # ~10s — classical expectations, struck
    def construct(self):
        lb = SerifLabel("what waves would do", CRIMSON, size=30)
        lb.to_edge(UP, buff=0.75)             # inside the ±3.4 safe area
        rows = VGroup(
            Text("any color works, given time", font=SERIF, color=INK, font_size=32),
            Text("brighter means faster electrons", font=SERIF, color=INK, font_size=32),
            Text("energy needs time to accumulate", font=SERIF, color=INK, font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7).shift(DOWN * 0.4)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.8)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.6)
        self.wait(1.0)
        for r in rows:
            self.play(Create(hand_strike(r)), run_time=0.7)
            self.wait(0.5)
        self.wait(2.2)


class B09_LightQuanta(Scene):      # ~10.5s — the wave becomes packets
    def construct(self):
        wave = smooth_curve(lambda x: 0.9 * np.sin(1.7 * x) + 0.4,
                            X0 + 0.4, X1 - 0.4, NAVY, width=5)
        self.play(Create(wave), run_time=1.6, rate_func=linear)
        self.wait(0.8)
        grey = wave.copy().set_stroke(INK, width=3, opacity=0.2)
        self.play(Transform(wave, grey), run_time=1.0)
        photons = VGroup(*[Dot([X0 + 0.9 + i * 1.15, -1.1, 0], radius=0.14,
                               color=TERRA) for i in range(9)])
        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.4) for p in photons],
                              lag_ratio=0.12, run_time=2.2))
        lb = SerifLabel("Lichtquanten — light quanta", TERRA, size=32)
        lb.next_to(photons, DOWN, buff=0.6)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.wait(3.5)


class B10_OnePhotonOneElectron(Scene):  # ~9s
    def construct(self):
        metal = Rectangle(width=3.2, height=4.4).set_fill(SLATE, 1).set_stroke(width=0)
        metal.to_edge(RIGHT, buff=1.6)
        mlabel = Text("sodium", font=SERIF, color=WHITE, font_size=26)
        mlabel.move_to(metal)
        self.add(metal, mlabel)
        photon = Dot([-4.5, 1.0, 0], radius=0.16, color=TERRA)
        plabel = Text("one photon", font=SERIF, color=TERRA, font_size=24)
        plabel.next_to(photon, UP, buff=0.25)
        self.play(FadeIn(photon), FadeIn(plabel), run_time=0.6)
        self.play(photon.animate.move_to(metal.get_left() + LEFT * 0.1 + UP * 1.0),
                  FadeOut(plabel), run_time=1.2, rate_func=linear)
        electron = Dot(metal.get_left() + LEFT * 0.1 + UP * 1.0, radius=0.12,
                       color=NAVY)
        elabel = Text("one electron", font=SERIF, color=NAVY, font_size=24)
        self.play(FadeOut(photon), FadeIn(electron), run_time=0.4)
        self.play(electron.animate.move_to([-3.6, 0.2, 0]), run_time=1.0)
        elabel.next_to(electron, DOWN, buff=0.25)
        self.play(FadeIn(elabel), run_time=0.5)
        weak = Dot([-4.5, -1.6, 0], radius=0.10, color=TERRA).set_opacity(0.6)
        self.play(weak.animate.move_to(metal.get_left() + LEFT * 0.1 + DOWN * 1.6),
                  run_time=1.0, rate_func=linear)
        nothing = Text("below the fee: nothing", font=SERIF, color=INK,
                       font_size=24, slant=ITALIC)
        nothing.next_to(metal.get_left() + DOWN * 1.6, LEFT, buff=0.5)
        self.play(FadeOut(weak), FadeIn(nothing), run_time=0.7)
        self.wait(2.6)


class T01_EqSentences(Scene):      # ~10s — zone 2
    def construct(self):
        anchor = TANGENT.anchor()
        eye = TANGENT.eyebrow()
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        z = TANGENT.zone("sentences")
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in z[0]:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.8)
            self.wait(1.7)
        self.wait(1.6)


class T02_EqGlossary(Scene):       # ~10s — zone 3, Φ spotlit
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"\Phi")
        z = TANGENT.zone("glossary", spotlight="Φ")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(9.0)


class T03_EqExample(Scene):        # ~10.5s — zone 4
    def construct(self):
        anchor = TANGENT.anchor()
        z = TANGENT.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)
        self.wait(1.8)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)
        self.wait(2.0)
        self.play(FadeIn(rows[2]), run_time=0.7)
        self.wait(1.6)
        self.play(FadeIn(rows[3]), run_time=0.7)
        self.wait(2.0)


class B11_ThreeFactsFall(Scene):   # ~10s — the mirror of B07
    def construct(self):
        lb = SerifLabel("the three impossible facts, explained", NAVY, size=30)
        lb.to_edge(UP, buff=0.55)
        rows = VGroup(
            Text("the threshold", font=SERIF, color=INK, font_size=32),
            Text("energy from frequency alone", font=SERIF, color=INK, font_size=32),
            Text("no delay", font=SERIF, color=INK, font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7).shift(DOWN * 0.4 + LEFT * 1.0)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.8)
        for r in rows:
            c = Text("✓", font=SERIF, color=NAVY, font_size=36)
            c.next_to(r, RIGHT, buff=0.4)
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.6)
            self.play(FadeIn(c), run_time=0.4)
            self.wait(0.8)
        self.wait(2.4)


class B13_MillikanSlope(Scene):    # ~10s — three metals, one slope
    def construct(self):
        ax = VGroup(
            Line([X0, Y0, 0], [X1, Y0, 0], color=INK, stroke_width=2.5),
            Line([X0, Y0, 0], [X0, Y1, 0], color=INK, stroke_width=2.5))
        xl = Text("frequency", font=SERIF, color=INK, font_size=26)
        xl.next_to(ax[0], DOWN, buff=0.25).align_to(ax[0], RIGHT)
        yl = Text("stopping potential", font=SERIF, color=INK, font_size=26)
        yl.rotate(PI / 2).next_to(ax[1], LEFT, buff=0.25).align_to(ax[1], UP)
        self.play(Create(ax[0]), Create(ax[1]), run_time=1.0)
        self.play(FadeIn(xl), FadeIn(yl), run_time=0.5)
        lines, names = VGroup(), ["sodium", "lithium", "potassium"]
        for i, x_start in enumerate((-3.4, -1.9, -0.4)):
            ln = Line([x_start, Y0, 0], [x_start + 4.6, Y0 + 3.9, 0],
                      color=NAVY, stroke_width=5 - i)
            nm = Text(names[i], font=SERIF, color=NAVY, font_size=22)
            nm.next_to(ln.get_end(), UP, buff=0.15)
            lines.add(VGroup(ln, nm))
        for pair in lines:
            self.play(Create(pair[0]), FadeIn(pair[1]), run_time=1.1,
                      rate_func=linear)
        chip = LabelChip("slope: h/e — the same for every metal",
                         accent=CRIMSON, size=26)
        if chip.width > 6.0:
            chip.scale_to_fit_width(6.0)
        chip.move_to([-2.1, 2.3, 0])           # empty upper-left, clear of axis labels
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.8)
        self.wait(2.6)


class B14_NobelIrony(Scene):       # ~10s
    def construct(self):
        c1 = StateCard("EINSTEIN", side=3.0,
                       figures=[("Nobel Prize", "1921", True)])
        c2 = StateCard("MILLIKAN", side=3.0,
                       figures=[("Nobel Prize", "1923", False)])
        pair = VGroup(c1, c2).arrange(RIGHT, buff=2.2).shift(UP * 0.6)
        def caption(lines, under):
            g = VGroup(*[Text(t, font=SERIF, color=INK, font_size=26)
                         for t in lines]).arrange(DOWN, buff=0.12)
            for t in g:
                if t.width > 4.4:              # stay inside the card's column
                    t.scale_to_fit_width(4.4)
            return g.next_to(under, DOWN, buff=1.5)
        sub1 = caption(["for the photoelectric effect", "— not relativity"], c1)
        sub2 = caption(["for proving the theory", "he set out to kill"], c2)
        self.play(FadeIn(c1, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(sub1), run_time=0.6)
        self.wait(2.0)
        self.play(FadeIn(c2, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(4.0)


class B16_Next(Scene):             # ~5s — next tease (outro law replaces this
    def construct(self):           # slot with the branded card at vox_run)
        eye = Text("NEXT", font=SERIF, color=BLUE, font_size=24)
        t = Text("MATTER WAVES", font=SERIF, color=INK, font_size=54,
                 weight=BOLD)
        s = Text("quantum, vol. 1 · chapter 2", font=SERIF, color=INK,
                 font_size=28)
        eye.to_edge(UP, buff=1.4)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(3.1)
