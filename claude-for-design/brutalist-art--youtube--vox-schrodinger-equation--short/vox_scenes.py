"""short/vox_scenes.py — PORTRAIT (9:16) relayouts, The Schrödinger Equation.

Generated graphics re-band top-and-bottom for the 4.5 x 8 frame — never cut.
B01/B06/B10 use -916 clip overrides; B09 uses the hand -916 Fourier plate;
B11 dropped (--no-endcard: ends on the cat kicker).
Safe area ±1.95 x / ±3.4 y; fixed placements carry margin arithmetic in
comments (authoring preflight).
Render:  bash scripts/vox_run.sh reels/vox-schrodinger-equation/short
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

SAFE_W = 3.8
GRAY_IM = "#8A8A8A"


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def serif_lines(lines, size=26, color=INK, buff=0.16):
    g = VGroup(*[Text(t, font=SERIF, color=color, font_size=size)
                 for t in lines]).arrange(DOWN, buff=buff)
    return fit(g)


def anchor_card(spotlight=None):
    return EquationCard(r"i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi",
                        spotlight=spotlight, width=4.2,
                        plain="iℏ ∂Ψ/∂t = ĤΨ").to_edge(UP, buff=1.1)


class B02_Title(Scene):            # 11.18s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=22)
        eye.to_edge(UP, buff=1.4)
        title = VGroup(Text("THE SCHRÖDINGER", font=SERIF, color=INK,
                            font_size=44, weight=BOLD),
                       Text("EQUATION", font=SERIF, color=INK, font_size=44,
                            weight=BOLD)).arrange(DOWN, buff=0.18)
        fit(title)
        u = Line(title.get_corner(DL) + DOWN * 0.2,
                 title.get_corner(DR) + DOWN * 0.2, color=CRIMSON,
                 stroke_width=2)
        sub = serif_lines(["how the wave", "function moves"], size=26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(9.0)


class T01_EqSentences(Scene):      # 9.80s
    def construct(self):
        anchor = anchor_card(spotlight=r"i\hbar")
        eye = LabelChip("SCHRÖDINGER · TANGENT", accent=CRIMSON, size=16)
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        rows = VGroup()
        for tag, sentence in (("LHS", ["How the wave function", "is changing, right now."]),
                              ("RHS", ["The energy operator's", "verdict on the state."])):
            c = Text(tag, font=SERIF, color=WHITE, font_size=15)
            box = SurroundingRectangle(c, buff=0.08).set_fill(NAVY, 1).set_stroke(width=0)
            body = serif_lines(sentence, size=23, buff=0.1)
            rows.add(fit(VGroup(VGroup(box, c), body).arrange(RIGHT, buff=0.25,
                                                              aligned_edge=UP)))
        claim = serif_lines(["Energy drives", "all change."], size=25)
        cu = Line(claim.get_corner(DL) + DOWN * 0.1,
                  claim.get_corner(DR) + DOWN * 0.1, color=CRIMSON,
                  stroke_width=1.6)
        rows.add(VGroup(claim, cu))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.15)
        fit(rows)
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.7)
            self.wait(1.15)
        self.wait(1.7)


class T02_EqGlossary(Scene):       # 9.98s — glossary re-banded as blocks
    def construct(self):
        anchor = anchor_card(spotlight=r"i\hbar")
        self.add(anchor)
        data = [
            {"sym_tex": r"i\hbar", "sym": "iℏ", "role": "the rotator",
             "mean": "change becomes rotation", "dom": "1.055×10⁻³⁴ J·s", "hot": True},
            {"sym_tex": r"\partial\Psi/\partial t", "sym": "∂Ψ/∂t", "role": "the change",
             "mean": "the state's velocity in time", "dom": "per second", "hot": False},
            {"sym_tex": r"\hat{H}", "sym": "Ĥ", "role": "the operator",
             "mean": "total energy, kinetic + potential", "dom": "joules", "hot": False},
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
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.2)
        fit(blocks)
        self.play(FadeIn(blocks, shift=UP * 0.15), run_time=1.0)
        self.wait(9.0)


class T03_EqExample(Scene):        # 9.87s
    def construct(self):
        anchor = anchor_card(spotlight=r"\hat{H}")
        self.add(anchor)
        scenario = serif_lines(["separate space from time:", "each state gets a phase clock"],
                               size=21)
        lv = Text("E = 1 eV", font=MONO, color=CRIMSON, font_size=30)
        rv = Text("≈ 2.4×10¹⁴ turns/s", font=MONO, color=NAVY, font_size=26)
        pair = VGroup(fit(lv), fit(rv)).arrange(DOWN, buff=0.2)
        verdict = serif_lines(["the clock spins —", "the shadow stands still"],
                              size=22)
        vu = Line(verdict.get_corner(DL) + DOWN * 0.1,
                  verdict.get_corner(DR) + DOWN * 0.1, color=TERRA,
                  stroke_width=1.6)
        cost = serif_lines(["miss the phase, miss", "everything quantum"], size=19)
        stack = VGroup(scenario, pair, VGroup(verdict, vu), cost)
        stack.arrange(DOWN, buff=0.42).move_to(DOWN * 1.15)
        fit(stack)
        self.play(FadeIn(stack[0]), run_time=0.8)
        self.wait(1.5)
        self.play(FadeIn(stack[1], shift=UP * 0.15), run_time=0.9)
        self.wait(1.7)
        self.play(FadeIn(stack[2]), run_time=0.7)
        self.wait(1.3)
        self.play(FadeIn(stack[3]), run_time=0.7)
        self.wait(1.6)


class B04_TheFork(Scene):          # 9.56s — fork re-banded TOP AND BOTTOM
    def construct(self):
        top = EquationCard(r"i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi",
                           width=4.2, plain="iℏ ∂Ψ/∂t = ĤΨ").to_edge(UP, buff=0.7)
        ansatz = LabelChip("Ψ = ψ(x) · φ(t)", accent=NAVY, size=20)
        ansatz.next_to(top, DOWN, buff=0.3)
        e_chip = LabelChip("same constant E", accent=CRIMSON, size=18)
        e_chip.next_to(ansatz, DOWN, buff=0.3)
        self.play(FadeIn(top), run_time=0.9)
        self.play(FadeIn(ansatz, shift=UP * 0.1), run_time=0.7)
        self.wait(0.8)

        def card(y, fill, edge, l1, l1c, tex, plain):
            box = Rectangle(width=3.9, height=1.5).set_fill(fill, 0.16).set_stroke(edge, 1.6)
            t1 = Text(l1, font=SERIF, color=l1c, font_size=20)
            t2 = _math(tex, font_size=30, color=INK, plain=plain)
            g = VGroup(t1, t2).arrange(DOWN, buff=0.18)
            if g.width > 3.4:
                g.scale_to_fit_width(3.4)
            g.move_to(box)
            return VGroup(box, g).move_to([0, y, 0])

        # cards at y -0.6 (bottom -1.35) and -2.55 (bottom -3.3 ≤ 3.4 safe)
        tcard = card(-0.6, TERRA, TERRA, "time — trivial",
                     TERRA, r"\varphi(t) = e^{-iEt/\hbar}", "φ(t) = e^(−iEt/ℏ)")
        scard = card(-2.55, NAVY, NAVY, "space — the real problem",
                     NAVY, r"\hat{H}\,\psi = E\,\psi", "Ĥψ = Eψ")
        la = Arrow(e_chip.get_bottom() + DOWN * 0.1, tcard.get_top() + UP * 0.05,
                   color=TERRA, stroke_width=4, buff=0.05)
        self.play(FadeIn(e_chip, scale=1.1), run_time=0.6)
        self.play(Create(la), FadeIn(tcard, shift=UP * 0.1), run_time=0.9)
        self.wait(0.6)
        ra = Arrow(tcard.get_bottom() + DOWN * 0.05, scard.get_top() + UP * 0.05,
                   color=NAVY, stroke_width=4, buff=0.05)
        self.play(Create(ra), FadeIn(scard, shift=UP * 0.1), run_time=0.9)
        self.wait(3.2)


class B05_ClockAndShadow(Scene):   # 11.65s — clock TOP, shadow BOTTOM (the law)
    def construct(self):
        # clock: circle r=1.0 at (0, 2.0) → spans y 1.0..3.0 (top 3.0 < 3.4)
        c = [0.0, 2.0, 0]
        circle = Circle(radius=1.0, color=INK, stroke_width=2).move_to(c)
        hand = Line(c, [c[0] + 1.0, c[1], 0], color=CRIMSON, stroke_width=4.5)
        dot = Dot(c, radius=0.05, color=INK)
        chips = VGroup(LabelChip("Re ψ", accent=TERRA, size=18),
                       LabelChip("Im ψ", accent=SLATE, size=18))
        chips.arrange(RIGHT, buff=0.3)
        fit(chips).move_to([0, 0.72, 0])               # below circle (bottom 1.0)

        # shadow: hump baseline y=-1.15, peak 0.15 (clear of chips at 0.55+)
        y0 = -1.15
        xs = np.linspace(-1.8, 1.8, 60)
        top_pts = [np.array([x, y0 + 1.3 * np.exp(-x * x / 0.55), 0]) for x in xs]
        hump = Polygon(*(top_pts + [np.array([1.8, y0, 0]), np.array([-1.8, y0, 0])]))
        hump.set_fill(NAVY, 0.35).set_stroke(NAVY, 3)
        frozen = LabelChip("|ψ|² — FROZEN", accent=NAVY, size=20)
        fit(frozen).move_to([0, -1.62, 0])             # below the baseline

        bl = serif_lines(["the clock spins —", "the shadow never moves"],
                         size=22)
        bl.to_edge(DOWN, buff=0.62)                    # bottom ≥ −3.38, inside safe

        self.play(Create(circle), FadeIn(dot), run_time=0.9)
        self.play(Create(hand), FadeIn(chips), run_time=0.8)
        self.play(FadeIn(hump), run_time=1.0)
        self.play(FadeIn(frozen, scale=1.1), run_time=0.6)
        self.play(Rotate(hand, angle=2 * TAU, about_point=np.array(c)),
                  run_time=5.6, rate_func=linear)
        self.play(FadeIn(bl, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


class B07_TheMenu(Scene):          # 9.09s — well TOP, ladder BOTTOM
    def construct(self):
        # well: walls x ±1.75, floor y=0.0, tops y=3.0
        wl, wr, yf, yt = -1.75, 1.75, 0.0, 3.0
        walls = VGroup(Line([wl, yf, 0], [wl, yt, 0], color=INK, stroke_width=4.5),
                       Line([wr, yf, 0], [wr, yt, 0], color=INK, stroke_width=4.5),
                       Line([wl, yf, 0], [wr, yf, 0], color=INK, stroke_width=4.5))
        self.play(Create(walls), run_time=0.9)

        def mode(n, y_base, amp=0.35, color=NAVY):
            xs = np.linspace(wl, wr, 100)
            vm = VMobject(color=color, stroke_width=3)
            vm.set_points_smoothly(
                [np.array([x, y_base + amp * np.sin(n * PI * (x - wl) / (wr - wl)), 0])
                 for x in xs])
            return vm

        # rungs: x −1.3..0.9, chips to x ≤ 1.8 (< 1.95 safe)
        rungs = [(-0.9, "E₁"), (-1.7, "E₂"), (-2.5, "E₃")]
        for n, (ly, name) in enumerate(rungs, start=1):
            m = mode(n, 0.5 + (n - 1) * 0.8)
            rung = Line([-1.3, ly, 0], [0.9, ly, 0], color=NAVY, stroke_width=3)
            chip = Text(name, font=MONO, color=INK, font_size=22)
            chip.next_to(rung, RIGHT, buff=0.15)
            self.play(Create(m), run_time=0.7, rate_func=linear)
            self.play(Create(rung), FadeIn(chip), run_time=0.45)
        bad = mode(2.6, 2.65, amp=0.28, color=CRIMSON)   # band 2.37..2.93 < wall top
        bad_lb = serif_lines(["doesn't fit —", "doesn't exist"], size=20,
                             color=CRIMSON)
        bad_lb.to_edge(DOWN, buff=0.55)                  # below the ladder (−2.5)
        self.play(Create(bad), run_time=0.7, rate_func=linear)
        self.play(FadeIn(bad_lb), bad.animate.set_stroke(opacity=0.15),
                  run_time=0.9)
        self.wait(1.7)


class B08_TheSlosh(Scene):         # 9.01s
    def construct(self):
        wl, wr, y0 = -1.8, 1.8, -0.4
        walls = VGroup(Line([wl, y0, 0], [wl, 2.6, 0], color=INK, stroke_width=4),
                       Line([wr, y0, 0], [wr, 2.6, 0], color=INK, stroke_width=4),
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
        self.play(Create(walls), FadeIn(dens), run_time=1.2)
        eline = Line([wl, -2.1, 0], [wr, -2.1, 0], color=CRIMSON, stroke_width=4)
        echip = LabelChip("energy: constant", accent=CRIMSON, size=20)
        fit(echip).move_to([0, -2.7, 0])               # below the line, above safe edge
        self.play(Create(eline), FadeIn(echip), run_time=0.9, rate_func=linear)
        for theta in (PI, 2 * PI, 3 * PI):
            self.play(Transform(dens, density(theta)), run_time=1.7,
                      rate_func=linear)
        self.wait(1.8)
