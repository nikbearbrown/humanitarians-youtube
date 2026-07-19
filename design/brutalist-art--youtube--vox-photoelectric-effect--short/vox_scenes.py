"""short/vox_scenes.py — PORTRAIT (9:16) relayouts, The Photoelectric Effect.

The reformat rule: generated graphics re-band top-and-bottom for the 4.5 x 8
frame — never cut. Same content and durations as the 16:9 master.
Render:  bash scripts/vox_run.sh reels/vox-photoelectric-effect/short
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

PX0, PX1, PY0, PY1 = -1.9, 2.0, -2.3, 1.5
SAFE_W = 3.8


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def serif_lines(lines, size=26, color=INK, buff=0.16):
    g = VGroup(*[Text(t, font=SERIF, color=color, font_size=size)
                 for t in lines]).arrange(DOWN, buff=buff)
    return fit(g)


def hand_strike(m, color=TERRA):
    l, r = m.get_corner(DL), m.get_corner(UR)
    v = VMobject(color=color, stroke_width=6)
    pts = [np.array([l[0] - 0.12 + t * (r[0] - l[0] + 0.24),
                     l[1] + t * (r[1] - l[1]) + 0.05 * np.sin(9 * t), 0.0])
           for t in np.linspace(0, 1, 24)]
    v.set_points_smoothly(pts)
    v._qc_intentional = True
    return v


TANGENT = EquationTangent({
    "eyebrow": "Photoelectric law · tangent",
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
        "cost": "Sub-threshold photons never add up.",
    },
    "values_claim": "(unused)",
})


def anchor_card(spotlight=None):
    return EquationCard(r"K_{max} = h\nu - \Phi", spotlight=spotlight,
                        width=4.2, plain="Kmax = hν − Φ").to_edge(UP, buff=1.1)


class B02_Title(Scene):            # 9.61s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=22)
        eye.to_edge(UP, buff=1.4)
        title = VGroup(*[Text(w, font=SERIF, color=INK, font_size=48,
                              weight=BOLD)
                         for w in ("THE", "PHOTOELECTRIC", "EFFECT")])
        title.arrange(DOWN, buff=0.18)
        fit(title)
        u = Line(title.get_corner(DL) + DOWN * 0.2,
                 title.get_corner(DR) + DOWN * 0.2, color=CRIMSON,
                 stroke_width=2)
        sub = serif_lines(["how light came", "apart in chunks"], size=26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(7.4)


class B05_MoreNotFaster(Scene):    # 9.14s
    def construct(self):
        lb = serif_lines(["brighter light:", "more, not faster"], size=28,
                         color=NAVY)
        lb.to_edge(UP, buff=1.2)
        row1 = IsotypeGrid([8], [NAVY], per_row=8, size=0.3, gap=0.18)
        row2 = IsotypeGrid([16], [NAVY], per_row=8, size=0.3, gap=0.18)
        dim = LabelChip("dim", accent=BLUE, size=20)
        bright = LabelChip("2× bright", accent=BLUE, size=20)
        g1 = VGroup(dim, fit(row1)).arrange(DOWN, buff=0.3)
        g2 = VGroup(bright, fit(row2)).arrange(DOWN, buff=0.3)
        stack = VGroup(g1, g2).arrange(DOWN, buff=0.7).move_to(DOWN * 0.6)
        same = LabelChip("same energy, each", accent=TERRA, size=22)
        same.next_to(stack, DOWN, buff=0.5)
        self.play(FadeIn(lb), run_time=0.8)
        self.play(FadeIn(dim), run_time=0.4)
        self.play(row1.count_up(1.5, lag_ratio=0.02))
        self.play(FadeIn(bright), run_time=0.4)
        self.play(row2.count_up(2.0, lag_ratio=0.01))
        self.play(FadeIn(same, shift=UP * 0.15), run_time=0.7)
        self.wait(3.0)


class B07_WavesCant(Scene):        # 9.74s
    def construct(self):
        lb = SerifLabel("what waves would do", CRIMSON, size=26)
        fit(lb).to_edge(UP, buff=1.2)
        rows = VGroup(
            serif_lines(["any color works,", "given time"], size=26),
            serif_lines(["brighter means", "faster electrons"], size=26),
            serif_lines(["energy needs time", "to accumulate"], size=26),
        ).arrange(DOWN, buff=0.65).shift(DOWN * 0.5)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.8)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.55)
        self.wait(0.9)
        for r in rows:
            self.play(Create(hand_strike(r)), run_time=0.65)
            self.wait(0.4)
        self.wait(2.0)


class B09_LightQuanta(Scene):      # ~10.5s
    def construct(self):
        def wf(x):
            return 1.3 + 0.55 * np.sin(2.6 * x)
        wave = VMobject(color=NAVY, stroke_width=4.5)
        wave.set_points_smoothly([np.array([x, wf(x), 0.0])
                                  for x in np.linspace(-1.9, 1.9, 80)])
        self.play(Create(wave), run_time=1.6, rate_func=linear)
        self.wait(0.8)
        grey = wave.copy().set_stroke(INK, width=3, opacity=0.2)
        self.play(Transform(wave, grey), run_time=1.0)
        photons = VGroup(*[Dot([-1.6 + i * 0.65, -0.4, 0], radius=0.12,
                               color=TERRA) for i in range(6)])
        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in photons],
                              lag_ratio=0.12, run_time=2.0))
        lb = serif_lines(["Lichtquanten", "— light quanta"], size=28,
                         color=TERRA)
        lb.next_to(photons, DOWN, buff=0.6)
        self.play(FadeIn(lb), run_time=0.9)
        self.wait(3.4)


class B10_OnePhotonOneElectron(Scene):  # ~9s
    def construct(self):
        metal = Rectangle(width=3.8, height=1.6).set_fill(SLATE, 1).set_stroke(width=0)
        metal.move_to(DOWN * 2.0)
        mlabel = Text("sodium", font=SERIF, color=WHITE, font_size=22)
        mlabel.move_to(metal)
        self.add(metal, mlabel)
        photon = Dot([-0.8, 2.6, 0], radius=0.14, color=TERRA)
        plabel = Text("one photon", font=SERIF, color=TERRA, font_size=20)
        plabel.next_to(photon, UP, buff=0.2)
        self.play(FadeIn(photon), FadeIn(plabel), run_time=0.6)
        self.play(photon.animate.move_to(metal.get_top() + UP * 0.1 + LEFT * 0.8),
                  FadeOut(plabel), run_time=1.2, rate_func=linear)
        electron = Dot(metal.get_top() + UP * 0.1 + LEFT * 0.8, radius=0.11,
                       color=NAVY)
        self.play(FadeOut(photon), FadeIn(electron), run_time=0.4)
        self.play(electron.animate.move_to([-1.2, 0.3, 0]), run_time=1.0)
        elabel = Text("one electron", font=SERIF, color=NAVY, font_size=20)
        elabel.next_to(electron, UP, buff=0.2)
        self.play(FadeIn(elabel), run_time=0.5)
        weak = Dot([0.9, 2.6, 0], radius=0.09, color=TERRA).set_opacity(0.6)
        self.play(weak.animate.move_to(metal.get_top() + UP * 0.1 + RIGHT * 0.8),
                  run_time=1.0, rate_func=linear)
        nothing = serif_lines(["below the fee:", "nothing"], size=20)
        for t in nothing:
            t.set_color(INK)
        nothing.next_to(metal.get_top() + RIGHT * 0.8, UP, buff=0.3)
        self.play(FadeOut(weak), FadeIn(nothing), run_time=0.7)
        self.wait(2.4)


class T01_EqSentences(Scene):      # ~10s
    def construct(self):
        anchor = anchor_card()
        eye = LabelChip("PHOTOELECTRIC LAW · TANGENT", accent=CRIMSON, size=16)
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        rows = VGroup()
        for tag, sentence in (("LHS", ["The fastest electron's", "kinetic energy."]),
                              ("RHS", ["The photon's payment,", "minus the exit fee."])):
            chip = Text(tag, font=SERIF, color=WHITE, font_size=15)
            box = SurroundingRectangle(chip, buff=0.08).set_fill(NAVY, 1).set_stroke(width=0)
            body = serif_lines(sentence, size=23, buff=0.1)
            rows.add(fit(VGroup(VGroup(box, chip), body).arrange(RIGHT, buff=0.25,
                                                                 aligned_edge=UP)))
        claim = serif_lines(["Each photon acts alone —", "whole or not at all."],
                            size=23)
        cu = Line(claim.get_corner(DL) + DOWN * 0.1,
                  claim.get_corner(DR) + DOWN * 0.1, color=CRIMSON,
                  stroke_width=1.6)
        rows.add(VGroup(claim, cu))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(DOWN * 1.1)
        fit(rows)
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.8)
            self.wait(1.6)
        self.wait(1.4)


class T02_EqGlossary(Scene):       # ~10s
    def construct(self):
        anchor = anchor_card(spotlight=r"\Phi")
        self.add(anchor)
        blocks = VGroup()
        for r in TANGENT.d["glossary"]:
            hot = r["sym"] == "Φ"
            sym = _math(r["sym_tex"], font_size=32,
                        color=CRIMSON if hot else INK, plain=r["sym"])
            role = Text(r["role"], font=SERIF, font_size=17, slant=ITALIC,
                        color=TERRA if hot else BLUE)
            top = VGroup(sym, role).arrange(RIGHT, buff=0.28, aligned_edge=DOWN)
            mean = Text(r["mean"], font=SERIF, color=INK, font_size=19)
            dom = Text(r["dom"], font=MONO, color=INK, font_size=14)
            blocks.add(fit(VGroup(top, fit(mean), dom)
                           .arrange(DOWN, aligned_edge=LEFT, buff=0.12)))
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.2)
        fit(blocks)
        self.play(FadeIn(blocks, shift=UP * 0.15), run_time=1.0)
        self.wait(9.0)


class T03_EqExample(Scene):        # ~10.5s
    def construct(self):
        anchor = anchor_card()
        self.add(anchor)
        scenario = serif_lines(["UV at 300 nm on sodium.", "Fee: 2.28 eV."], size=22)
        lv = Text("UV pays: 4.13 eV", font=MONO, color=CRIMSON, font_size=28)
        rv = Text("green pays: 2.27 eV", font=MONO, color=NAVY, font_size=28)
        pair = VGroup(fit(lv), fit(rv)).arrange(DOWN, buff=0.2)
        verdict = serif_lines(["UV: keeps 1.85 eV", "green: 0.01 short — nothing"],
                              size=23)
        vu = Line(verdict.get_corner(DL) + DOWN * 0.1,
                  verdict.get_corner(DR) + DOWN * 0.1, color=TERRA,
                  stroke_width=1.6)
        cost = serif_lines(["Sub-threshold photons", "never add up."], size=19)
        stack = VGroup(scenario, pair, VGroup(verdict, vu), cost)
        stack.arrange(DOWN, buff=0.42).move_to(DOWN * 1.15)
        fit(stack)
        self.play(FadeIn(stack[0]), run_time=0.8)
        self.wait(1.8)
        self.play(FadeIn(stack[1], shift=UP * 0.15), run_time=0.9)
        self.wait(2.0)
        self.play(FadeIn(stack[2]), run_time=0.7)
        self.wait(1.6)
        self.play(FadeIn(stack[3]), run_time=0.7)
        self.wait(2.0)


class B11_ThreeFactsFall(Scene):   # ~10.5s
    def construct(self):
        lb = serif_lines(["the three impossible", "facts, explained"], size=26,
                         color=NAVY)
        lb.to_edge(UP, buff=1.2)
        def row(text):
            mark = Text("✓", font=SERIF, color=NAVY, font_size=28)
            t = Text(text, font=SERIF, color=INK, font_size=26)
            if t.width > 3.0:
                t.scale_to_fit_width(3.0)
            return VGroup(mark, t).arrange(RIGHT, buff=0.25)
        rows = VGroup(row("the threshold"),
                      row("energy from frequency"),
                      row("no delay"))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.8).move_to(DOWN * 0.6)
        fit(rows)
        self.play(FadeIn(lb), run_time=0.8)
        for r in rows:
            r[0].set_opacity(0)
            self.play(FadeIn(r[1], shift=UP * 0.1), run_time=0.6)
            self.play(r[0].animate.set_opacity(1), run_time=0.4)
            self.wait(0.8)
        self.wait(2.6)


class B13_MillikanSlope(Scene):    # ~10.5s
    def construct(self):
        chip = LabelChip("slope: h/e — every metal", accent=CRIMSON, size=20)
        fit(chip, 3.8).to_edge(UP, buff=1.2)
        ax = VGroup(
            Line([PX0, PY0, 0], [PX1, PY0, 0], color=INK, stroke_width=2.5),
            Line([PX0, PY0, 0], [PX0, PY1, 0], color=INK, stroke_width=2.5))
        xl = Text("frequency", font=SERIF, color=INK, font_size=18)
        xl.next_to(ax[0], DOWN, buff=0.18).align_to(ax[0], RIGHT).shift(LEFT * 0.25)
        yl = Text("stopping potential", font=SERIF, color=INK, font_size=18)
        yl.next_to([PX0, PY1, 0], UP, buff=0.15).align_to(ax[1], LEFT)
        self.play(FadeIn(chip), run_time=0.7)
        self.play(Create(ax[0]), Create(ax[1]), run_time=1.0)
        self.play(FadeIn(xl), FadeIn(yl), run_time=0.5)
        names = ["sodium", "lithium", "potassium"]
        for i, x_start in enumerate((-1.5, -0.75, 0.0)):
            ln = Line([x_start, PY0, 0], [x_start + 1.7, PY0 + 3.2, 0],
                      color=NAVY, stroke_width=4.5 - i)
            nm = Text(names[i], font=SERIF, color=NAVY, font_size=16)
            nm.next_to(ln.get_end(), UP, buff=0.12)
            self.play(Create(ln), FadeIn(nm), run_time=1.0, rate_func=linear)
        self.wait(3.8)


class B14_NobelIrony(Scene):       # ~10.4s — portrait: cards stack vertically
    def construct(self):
        c1 = StateCard("EINSTEIN", side=2.2,
                       figures=[("Nobel Prize", "1921", True)])
        s1 = serif_lines(["for the photoelectric effect", "— not relativity"],
                         size=20)
        c2 = StateCard("MILLIKAN", side=2.2,
                       figures=[("Nobel Prize", "1923", False)])
        s2 = serif_lines(["for proving the theory", "he set out to kill"],
                         size=20)
        g1 = VGroup(c1, s1).arrange(DOWN, buff=1.1)
        g2 = VGroup(c2, s2).arrange(DOWN, buff=1.1)
        stack = VGroup(g1, g2).arrange(DOWN, buff=0.75)
        if stack.height > 7.0:
            stack.scale_to_fit_height(7.0)
        fit(stack)
        self.play(FadeIn(g1, shift=UP * 0.15), run_time=0.8)
        self.wait(2.6)
        self.play(FadeIn(g2, shift=UP * 0.15), run_time=0.8)
        self.wait(4.0)
