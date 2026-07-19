"""vox_scenes.py — The Ultraviolet Catastrophe (fresh build).

One Scene per GRAPHIC/CARD beat, rendered to the measured beat durations in
beat_sheet.json. Media slots (B01 B03 B05 B08 B10 B14 B15) fill from the
SHOTLIST archive links; B16 is the vox_outro composite.
Render everything:  bash scripts/vox_run.sh reels/vox-ultraviolet-catastrophe
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403 — tokens, mobjects, tangent kit
import numpy as np

# ------------------------------------------------------------- chart idiom
# Same continuous chart arc as the proven conversion reel: one framing shared
# by B04 -> B07 -> B12 so the argument stays on one set of axes.

X0, X1, Y0, Y1 = -5.2, 5.6, -2.6, 3.0

def smooth_curve(fn, x0, x1, color, width=5, n=90):
    v = VMobject(color=color, stroke_width=width)
    v.set_points_smoothly([np.array([x, fn(x), 0.0])
                           for x in np.linspace(x0, x1, n)])
    return v

def chart_axes(xlabel="frequency", ylabel="brightness"):
    ax = VGroup(
        Line([X0, Y0, 0], [X1, Y0, 0], color=INK, stroke_width=2.5),
        Line([X0, Y0, 0], [X0, Y1, 0], color=INK, stroke_width=2.5),
    )
    xl = Text(xlabel, font=SERIF, color=INK, font_size=26)
    xl.next_to(ax[0], DOWN, buff=0.25).align_to(ax[0], RIGHT)
    yl = Text(ylabel, font=SERIF, color=INK, font_size=26)
    yl.rotate(PI / 2).next_to(ax[1], LEFT, buff=0.25).align_to(ax[1], UP)
    return VGroup(ax, xl, yl)

def planck_shape(x, scale=1.0, tmax=9.0):
    t = tmax * (x - X0) / (X1 - X0) + 1e-6
    return Y0 + scale * 5.2 * (t ** 3 / (np.exp(t) - 1)) / 1.42

def rj(x):
    t = (x - X0) / (X1 - X0)
    return Y0 + 5.6 * t * t

def data_dots(scale=1.0, color=NAVY, n=9):
    xs = np.linspace(X0 + 0.7, X1 - 0.9, n)
    return VGroup(*[Dot([x, planck_shape(x, scale), 0], radius=0.055,
                        color=color) for x in xs])

# ------------------------------------------------------------- the tangent
# E = h nu, straight from beat_sheet.json viz.tangent (T01-T03).

TANGENT = EquationTangent({
    "eyebrow": "Chunk law · equation · tangent",
    "equation": "E = hν",
    "equation_tex": r"E = h\nu",
    "lhs": "The energy of one chunk of light.",
    "rhs": "Its frequency, times a new constant of nature.",
    "claim": "Exactly equal — in-between energies are banned.",
    "glossary": [
        {"sym": "E", "sym_tex": "E", "role": "quantity",
         "mean": "energy of one chunk", "dom": "joules"},
        {"sym": "ν", "sym_tex": r"\nu", "role": "variable",
         "mean": "frequency of the light", "dom": "hertz"},
        {"sym": "h", "sym_tex": "h", "role": "constant of nature",
         "mean": "Planck's constant — the exchange rate", "dom": "6.626×10⁻³⁴ J·s"},
    ],
    "example": {
        "scenario": "A forge at 3000 K. Thermal budget per mode: 0.26 eV.",
        "lhs_val": "red: 1.8 eV", "rhs_val": "UV: 12.4 eV",
        "verdict": "UV ≈ 48× the budget — unaffordable",
        "cost": "High frequencies go dark. The catastrophe is cancelled.",
    },
    "values_claim": "(unused — physics, not a contested judgment)",
})

# ---------------------------------------------------------------- scenes

class B02_Title(Scene):            # 9.8s — title card
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE ULTRAVIOLET CATASTROPHE", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:                     # margins are law
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("why physics predicted infinite light", font=SERIF, color=INK,
                 font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(7.6)


class B04_MeasuredHump(Scene):     # 9.46s — the Berlin data
    def construct(self):
        ch = chart_axes()
        lb = SerifLabel("what Berlin measured", NAVY, size=30)
        lb.to_edge(UP, buff=0.55)
        self.play(Create(ch[0]), run_time=1.0)
        self.play(FadeIn(ch[1]), FadeIn(ch[2]), run_time=0.5)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.8)
        cool = smooth_curve(lambda x: planck_shape(x, 0.62, 7.0),
                            X0 + 0.4, X1 - 0.4, NAVY, width=5)
        self.play(Create(cool), run_time=2.2, rate_func=linear)
        # hotter: taller AND peak shifted toward the blue (Wien) — tmax
        # smaller pushes the peak RIGHT in these scaled units
        hot = smooth_curve(lambda x: planck_shape(x, 1.0, 5.5),
                           X0 + 0.4, X1 - 0.4, NAVY, width=4)
        hot.set_stroke(opacity=0.45)
        hot_lb = Text("hotter", font=SERIF, color=NAVY, font_size=24)
        hot_lb.move_to([fx_pos(0.513), 1.85, 0])   # inside the hump, off both strokes
        self.play(Create(hot), FadeIn(hot_lb), run_time=1.8, rate_func=linear)
        self.wait(3.1)


def fx_pos(t):
    return X0 + t * (X1 - X0)


class B06_EqualShares(Scene):      # 9.93s — equipartition as isotype
    def construct(self):
        lb = SerifLabel("every vibration gets the same wage", TERRA, size=32)
        lb.to_edge(UP, buff=0.7)
        grid = IsotypeGrid([30], [SLATE], per_row=10, size=0.5, gap=0.28)
        grid.move_to(ORIGIN).shift(DOWN * 0.3)
        chip = LabelChip("kT each", accent=TERRA, size=26)
        chip.next_to(grid, DOWN, buff=0.55)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.play(grid.count_up(4.5, lag_ratio=0.01))
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.7)
        self.wait(3.8)


class B07_RJRunaway(Scene):        # 9.69s — fits, then runs away
    def construct(self):
        ch = chart_axes(); self.add(ch)
        dots = data_dots(0.62)
        self.add(dots)
        lb = SerifLabel("the Rayleigh–Jeans prediction", CRIMSON, size=30)
        lb.to_edge(UP, buff=0.55)              # centered — clear of the y-axis label
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        run = smooth_curve(rj, X0 + 0.4, fx_pos(0.97), CRIMSON, width=6)
        self.play(Create(run), run_time=4.6, rate_func=linear)
        self.wait(4.2)


class B09_WhichAssumption(Scene):  # 11.55s — the diagnosis
    def construct(self):
        rows = VGroup(
            SerifLabel("counting the modes", BLUE, size=34),
            SerifLabel("equal shares for each", BLUE, size=34),
            SerifLabel("energy flows continuously", INK, size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75).shift(LEFT * 1.2)
        checks = VGroup()
        for i in (0, 1):
            c = Text("✓", font=SERIF, color=NAVY, font_size=40)
            c.next_to(rows[i], RIGHT, buff=0.5)
            checks.add(c)
        self.play(FadeIn(rows[0], shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(checks[0]), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(rows[1], shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(checks[1]), run_time=0.5)
        self.wait(1.6)
        self.play(FadeIn(rows[2], shift=UP * 0.1), run_time=0.8)
        ring = HandRing(rows[2], color=TERRA)
        self.play(Create(ring), run_time=1.1)
        self.wait(4.2)


class B11_Staircase(Scene):        # 10.03s — only whole steps
    def construct(self):
        lb = SerifLabel("allowed energies", NAVY, size=32)
        lb.to_edge(UP, buff=0.7)
        steps = VGroup()
        labels = ["0", "hν", "2hν", "3hν"]
        for i in range(4):
            s = Line([-3.5 + i * 2.0, -1.8 + i * 0.95, 0],
                     [-1.9 + i * 2.0, -1.8 + i * 0.95, 0],
                     color=SLATE, stroke_width=10)
            t = Text(labels[i], font=SERIF, color=INK, font_size=30,
                     slant=ITALIC)
            t.next_to(s, UP, buff=0.18)
            steps.add(VGroup(s, t))
        marker = Dot([-2.7, -1.8 + 0.475, 0], radius=0.14, color=CRIMSON)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in steps],
                              lag_ratio=0.25, run_time=2.4))
        self.play(FadeIn(marker), run_time=0.4)
        self.wait(1.2)
        # tries to sit between steps; snaps to the nearest one
        self.play(marker.animate.move_to([-1.5, -1.33, 0]), run_time=0.7)
        self.play(marker.animate.move_to([-2.7 + 2.0, -1.8 + 0.95 + 0.14, 0]),
                  run_time=0.5)
        self.wait(3.9)


class T01_EqSentences(Scene):      # 9.98s — zone 2: sentences before symbols
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


class T02_EqGlossary(Scene):       # 10.48s — zone 3: the glossary, h spotlit
    def construct(self):
        anchor = TANGENT.anchor(spotlight="h")
        z = TANGENT.zone("glossary", spotlight="h")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(9.5)


class T03_EqExample(Scene):        # 10.87s — zone 4: holds or breaks
    def construct(self):
        anchor = TANGENT.anchor()
        z = TANGENT.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)          # scenario
        self.wait(1.8)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)  # red vs UV
        self.wait(2.0)
        self.play(FadeIn(rows[2]), run_time=0.7)          # verdict
        self.wait(1.6)
        self.play(FadeIn(rows[3]), run_time=0.7)          # the cost
        self.wait(2.4)


class B12_PlanckCurve(Scene):      # 12.56s — the fix traces the data
    def construct(self):
        ch = chart_axes(); self.add(ch)
        dots = data_dots(0.62); self.add(dots)
        ghost = smooth_curve(rj, X0 + 0.4, fx_pos(0.97), CRIMSON, width=5)
        self.add(ghost)
        self.wait(0.8)
        grey = smooth_curve(rj, X0 + 0.4, fx_pos(0.97), INK, width=3)
        grey.set_stroke(opacity=0.22)
        self.play(Transform(ghost, grey), run_time=1.2)
        pl = smooth_curve(lambda x: planck_shape(x, 0.62, 7.0),
                          X0 + 0.4, X1 - 0.4, NAVY, width=6)
        self.play(Create(pl), run_time=4.4, rate_func=linear)
        chip = LabelChip("PLANCK 1900", accent=NAVY, size=26)
        chip.move_to([fx_pos(0.72), planck_shape(fx_pos(0.30), 0.62, 7.0) + 1.6, 0])
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.7)
        self.wait(4.7)


class B13_TwentyOrders(Scene):     # 7.94s — the number beat
    def construct(self):
        n = Text("10²⁰", font=SERIF, color=CRIMSON, font_size=160, weight=BOLD)
        sub = Text("×  too bright — the classical error in the ultraviolet",
                   font=SERIF, color=INK, font_size=30)
        zeros = Text("100,000,000,000,000,000,000", font="Menlo", color=INK,
                     font_size=34)
        n.shift(UP * 0.9)
        zeros.next_to(n, DOWN, buff=0.5)
        sub.next_to(zeros, DOWN, buff=0.5)
        self.play(FadeIn(n, shift=UP * 0.2), run_time=0.8)
        self.wait(1.6)
        self.play(Write(zeros), run_time=1.6)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(3.3)
