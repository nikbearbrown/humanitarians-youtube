"""vox_scenes.py — The Schrödinger Equation (film five, 16:9).

One Scene per GRAPHIC/CARD beat; the compile ladder retimes to measured
audio. Durations from beat_sheet.json (audio locked 2026-07-05):
B02 11.18 · T01 9.80 · T02 9.98 · T03 9.87 · B04 9.56 · B05 11.65 ·
B07 9.09 · B08 9.01 · B11 6.58.
Safe area ±6.4 x / ±3.5 y (16:9); every fixed label placed with explicit
margin arithmetic in comments — the B06-short lesson, applied at authoring.
Render:  bash scripts/vox_run.sh reels/vox-schrodinger-equation
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

GRAY_IM = "#8A8A8A"

TANGENT = EquationTangent({
    "eyebrow": "Schrödinger equation · tangent",
    "equation": "iℏ ∂Ψ/∂t = ĤΨ",
    "equation_tex": r"i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi",
    "lhs": "How the wave function is changing, right now.",
    "rhs": "The energy operator's verdict on the state.",
    "claim": "Energy is the engine of all quantum change.",
    "glossary": [
        {"sym": "iℏ", "sym_tex": r"i\hbar", "role": "the rotator",
         "mean": "turns change into rotation; ℏ sets the speed", "dom": "1.055×10⁻³⁴ J·s"},
        {"sym": "∂Ψ/∂t", "sym_tex": r"\partial\Psi/\partial t", "role": "the change",
         "mean": "the state's velocity through time", "dom": "per second"},
        {"sym": "Ĥ", "sym_tex": r"\hat{H}", "role": "the operator",
         "mean": "total energy — kinetic plus potential", "dom": "joules"},
    ],
    "example": {
        "scenario": "Separate space from time: each state gets a phase clock.",
        "lhs_val": "E = 1 eV", "rhs_val": "≈ 2.4×10¹⁴ turns/s",
        "verdict": "the clock spins — the shadow stands still",
        "cost": "Miss the phase and you miss interference — everything quantum.",
    },
    "values_claim": "(merged into the sentences claim — simple equation)",
})


class B02_Title(Scene):            # 11.18s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE SCHRÖDINGER EQUATION", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("how the wave function moves", font=SERIF, color=INK,
                 font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(9.0)


class T01_EqSentences(Scene):      # 9.80s
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"i\hbar")
        eye = TANGENT.eyebrow()
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        z = TANGENT.zone("sentences")
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in z[0]:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.7)
            self.wait(1.2)
        self.wait(3.1)


class T02_EqGlossary(Scene):       # 9.98s
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"i\hbar")
        z = TANGENT.zone("glossary", spotlight="iℏ")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(9.0)


class T03_EqExample(Scene):        # 9.87s
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"\hat{H}")
        z = TANGENT.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)
        self.wait(1.5)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)
        self.wait(1.7)
        self.play(FadeIn(rows[2]), run_time=0.7)
        self.wait(1.3)
        self.play(FadeIn(rows[3]), run_time=0.7)
        self.wait(2.4)


class B04_TheFork(Scene):          # 9.56s — fig 4.1 as motion
    def construct(self):
        # TDSE card top (EquationCard tops out at y≈+3.0; safe to ±3.5)
        top = EquationCard(r"i\hbar\,\frac{\partial \Psi}{\partial t} = \hat{H}\,\Psi",
                           width=6.5, plain="iℏ ∂Ψ/∂t = ĤΨ").to_edge(UP, buff=0.55)
        ansatz = LabelChip("the guess:  Ψ = ψ(x) · φ(t)", accent=NAVY, size=24)
        ansatz.next_to(top, DOWN, buff=0.35)
        self.play(FadeIn(top), run_time=0.9)
        self.play(FadeIn(ansatz, shift=UP * 0.1), run_time=0.7)
        self.wait(1.0)

        # fork: E chip at hinge (y≈0), branch cards at y≈-1.9 (bottom ≈ -2.6)
        hinge = ansatz.get_bottom() + DOWN * 0.35
        # chip sits AT the hinge; arrows start BELOW its bottom corners so no
        # stroke crosses the text (preflight: the B06-short failure class)
        e_chip = LabelChip("the same constant E on both sides", accent=CRIMSON,
                           size=22).move_to([0, hinge[1] - 0.15, 0])
        lcard = VGroup()
        lc = Rectangle(width=5.2, height=1.7).set_fill(TERRA, 0.16).set_stroke(TERRA, 1.6)
        lt1 = Text("time — trivial", font=SERIF, color=TERRA, font_size=24)
        lt2 = _math(r"\varphi(t) = e^{-iEt/\hbar}", font_size=34, color=INK,
                    plain="φ(t) = e^(−iEt/ℏ)")
        lg = VGroup(lt1, lt2).arrange(DOWN, buff=0.2)
        if lg.width > 4.6:
            lg.scale_to_fit_width(4.6)
        lg.move_to(lc)
        lcard.add(lc, lg)
        lcard.move_to([-3.5, -1.9, 0])
        rcard = VGroup()
        rc = Rectangle(width=5.2, height=1.7).set_fill(NAVY, 0.14).set_stroke(NAVY, 1.6)
        rt1 = Text("space — the real problem", font=SERIF, color=NAVY, font_size=24)
        rt2 = _math(r"\hat{H}\,\psi = E\,\psi", font_size=34, color=INK,
                    plain="Ĥψ = Eψ")
        rg = VGroup(rt1, rt2).arrange(DOWN, buff=0.2)
        if rg.width > 4.6:
            rg.scale_to_fit_width(4.6)
        rg.move_to(rc)
        rcard.add(rc, rg)
        rcard.move_to([3.5, -1.9, 0])
        chip_bl = e_chip.get_corner(DL) + DOWN * 0.12
        chip_br = e_chip.get_corner(DR) + DOWN * 0.12
        la = Arrow(chip_bl, lcard.get_top() + UP * 0.1, color=TERRA,
                   stroke_width=4, buff=0.1)
        ra = Arrow(chip_br, rcard.get_top() + UP * 0.1, color=NAVY,
                   stroke_width=4, buff=0.1)
        self.play(Create(la), Create(ra), run_time=0.9, rate_func=linear)
        self.play(FadeIn(lcard, shift=UP * 0.1), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(rcard, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(e_chip, scale=1.1), run_time=0.6)
        self.wait(3.2)


class B05_ClockAndShadow(Scene):   # 11.65s — THE visual
    def construct(self):
        # LEFT: the clock — phasor circle r=1.5 centered (-3.6, 0.35);
        # top of circle y=1.85, label above at y≈2.35 (safe)
        c = [-3.6, 0.35, 0]
        circle = Circle(radius=1.5, color=INK, stroke_width=2).move_to(c)
        hand = Line(c, [c[0] + 1.5, c[1], 0], color=CRIMSON, stroke_width=5)
        dot = Dot(c, radius=0.06, color=INK)
        re_chip = LabelChip("Re ψ", accent=TERRA, size=20)
        im_chip = LabelChip("Im ψ", accent=SLATE, size=20)
        re_chip.move_to([c[0] + 2.9, c[1] - 0.4, 0])   # right of circle, inside safe
        im_chip.move_to([c[0], c[1] + 2.35, 0])        # above circle, y 2.35 < 3.5
        clock_lb = Text("the clock", font=SERIF, color=INK, font_size=26)
        clock_lb.move_to([c[0], c[1] - 2.25, 0])       # below circle, y -1.9

        # RIGHT: the shadow — frozen |ψ|² hump, baseline y=-1.0
        y0 = -1.0
        xs = np.linspace(1.2, 6.0, 60)
        x_mid = 3.6
        top_pts = [np.array([x, y0 + 2.0 * np.exp(-((x - x_mid) ** 2) / 0.9), 0])
                   for x in xs]
        hump = Polygon(*(top_pts + [np.array([6.0, y0, 0]), np.array([1.2, y0, 0])]))
        hump.set_fill(NAVY, 0.35).set_stroke(NAVY, 3)
        frozen = LabelChip("|ψ|² — FROZEN", accent=NAVY, size=22)
        frozen.move_to([x_mid, y0 + 2.75, 0])          # above hump peak, y 1.75
        shadow_lb = Text("the shadow", font=SERIF, color=INK, font_size=26)
        shadow_lb.move_to([x_mid, y0 - 0.55, 0])       # y -1.55

        bl = Text("the clock spins — the shadow never moves", font=SERIF,
                  color=INK, font_size=28, slant=ITALIC)
        bl.to_edge(DOWN, buff=0.55)                    # bottom ≈ -3.45+0.3 — inside

        self.play(Create(circle), FadeIn(dot), FadeIn(clock_lb), run_time=1.0)
        self.play(Create(hand), FadeIn(re_chip), FadeIn(im_chip), run_time=0.8)
        self.play(FadeIn(hump), FadeIn(shadow_lb), run_time=1.0)
        self.play(FadeIn(frozen, scale=1.1), run_time=0.6)
        self.play(Rotate(hand, angle=2 * TAU, about_point=np.array(c)),
                  run_time=5.4, rate_func=linear)
        self.play(FadeIn(bl, shift=UP * 0.1), run_time=0.7)
        self.wait(1.6)


class B07_TheMenu(Scene):          # 9.09s — modes that fit, the energy ladder
    def construct(self):
        # well: walls x=-5.6 and x=-0.6, floor y=-2.2, walls to y=+2.6
        wl, wr, yf, yt = -5.6, -0.6, -2.2, 2.6
        walls = VGroup(Line([wl, yf, 0], [wl, yt, 0], color=INK, stroke_width=5),
                       Line([wr, yf, 0], [wr, yt, 0], color=INK, stroke_width=5),
                       Line([wl, yf, 0], [wr, yf, 0], color=INK, stroke_width=5))
        self.play(Create(walls), run_time=0.9)

        def mode(n, y_base, amp=0.55):
            xs = np.linspace(wl, wr, 120)
            vm = VMobject(color=NAVY, stroke_width=3.5)
            vm.set_points_smoothly(
                [np.array([x, y_base + amp * np.sin(n * PI * (x - wl) / (wr - wl)), 0])
                 for x in xs])
            return vm

        # modes stacked at y −1.6 / −0.25 / 1.1 (amp 0.5 → tops ≤1.6);
        # bad wave gets its own empty band 1.7..2.5 — no curve overlap
        levels = [(-1.8, "E₁"), (-0.3, "E₂"), (1.9, "E₃")]
        for n, (ly, name) in enumerate(levels, start=1):
            m = mode(n, -1.6 + (n - 1) * 1.35, amp=0.5)
            rung = Line([1.0, ly, 0], [5.0, ly, 0], color=NAVY, stroke_width=3)
            chip = Text(name, font=MONO, color=INK, font_size=26)
            chip.next_to(rung, RIGHT, buff=0.2)        # ends ≈ x 5.9 < 6.4 safe
            self.play(Create(m), run_time=0.8, rate_func=linear)
            self.play(Create(rung), FadeIn(chip), run_time=0.5)
        bad = mode(2.6, 2.1, amp=0.4)
        bad.set_color(CRIMSON)
        bad_lb = Text("doesn't fit — doesn't exist", font=SERIF, color=CRIMSON,
                      font_size=24)
        bad_lb.to_edge(DOWN, buff=0.55)
        self.play(Create(bad), run_time=0.8, rate_func=linear)
        self.play(FadeIn(bad_lb), bad.animate.set_stroke(opacity=0.15),
                  run_time=1.0)
        self.wait(2.0)


class B08_TheSlosh(Scene):         # 9.01s — the shadow moves; the energy doesn't
    def construct(self):
        # well walls x=-5.2..5.2 visual; density band baseline y=-0.6
        wl, wr, y0 = -5.2, 5.2, -0.6
        walls = VGroup(Line([wl, y0, 0], [wl, 2.8, 0], color=INK, stroke_width=4),
                       Line([wr, y0, 0], [wr, 2.8, 0], color=INK, stroke_width=4),
                       Line([wl, y0, 0], [wr, y0, 0], color=INK, stroke_width=4))

        def density(theta):
            xs = np.linspace(wl, wr, 120)
            L = wr - wl
            pts = []
            for x in xs:
                u = (x - wl) / L
                p1 = np.sin(PI * u); p2 = np.sin(2 * PI * u)
                d = 0.5 * (p1 * p1 + p2 * p2) + p1 * p2 * np.cos(theta)
                pts.append(np.array([x, y0 + 2.4 * d * 0.7, 0]))
            poly = Polygon(*(pts + [np.array([wr, y0, 0]), np.array([wl, y0, 0])]))
            poly.set_fill(NAVY, 0.35).set_stroke(NAVY, 3)
            return poly

        dens = density(0.0)
        self.play(Create(walls), FadeIn(dens), run_time=1.2)
        # ⟨E⟩ flatline beneath: y=-2.4; chip right end x≈5.9 < 6.4
        eline = Line([wl, -2.4, 0], [wr, -2.4, 0], color=CRIMSON, stroke_width=4)
        echip = LabelChip("energy: constant", accent=CRIMSON, size=22)
        echip.move_to([0, -3.0, 0])
        self.play(Create(eline), FadeIn(echip), run_time=0.9, rate_func=linear)
        for theta in (PI, 2 * PI, 3 * PI):
            self.play(Transform(dens, density(theta)), run_time=1.7,
                      rate_func=linear)
        self.wait(1.8)


class B11_Next(Scene):             # 6.58s — outro law replaces this slot
    def construct(self):
        eye = Text("NEXT", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE INFINITE SQUARE WELL", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        s = Text("quantum, vol. 1 · chapter 5", font=SERIF, color=INK,
                 font_size=28)
        eye.to_edge(UP, buff=1.4)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(4.7)
