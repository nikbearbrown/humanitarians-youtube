"""short/vox_scenes.py — PORTRAIT (9:16) relayouts, The Ultraviolet Catastrophe.

THE REFORMAT RULE: generated graphics are never cut — they are re-laid-out.
One portrait Scene per GRAPHIC/CARD beat, same content and durations as the
16:9 master, recomposed for a 4.5 x 8 unit frame (1080x1920).
Render:  bash scripts/vox_run.sh reels/vox-ultraviolet-catastrophe/short
(the runner picks this file up, renders at 1080x1920, audits --portrait).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403 — tokens, mobjects, tangent kit
from vox_graphics import _math  # underscore name — import * skips it
import numpy as np

# ------------------------------------------------------- portrait chart idiom
PX0, PX1, PY0, PY1 = -1.9, 2.0, -2.3, 1.5      # chart region, portrait units
SAFE_W = 3.8                                     # max content width (safe ±1.95)


def smooth_curve(fn, x0, x1, color, width=5, n=90):
    v = VMobject(color=color, stroke_width=width)
    v.set_points_smoothly([np.array([x, fn(x), 0.0])
                           for x in np.linspace(x0, x1, n)])
    return v


def chart_axes(xlabel="frequency", ylabel="brightness"):
    ax = VGroup(
        Line([PX0, PY0, 0], [PX1, PY0, 0], color=INK, stroke_width=2.5),
        Line([PX0, PY0, 0], [PX0, PY1, 0], color=INK, stroke_width=2.5),
    )
    # portrait: labels sit INSIDE the safe area — x-label under the axis
    # pulled off the right edge, y-label horizontal above the axis top
    xl = Text(xlabel, font=SERIF, color=INK, font_size=18)
    xl.next_to(ax[0], DOWN, buff=0.18).align_to(ax[0], RIGHT).shift(LEFT * 0.25)
    yl = Text(ylabel, font=SERIF, color=INK, font_size=18)
    yl.next_to([PX0, PY1, 0], UP, buff=0.15).align_to(ax[1], LEFT)
    return VGroup(ax, xl, yl)


def fxp(t):
    return PX0 + t * (PX1 - PX0)


def planck_shape(x, scale=1.0, tmax=9.0):
    t = tmax * (x - PX0) / (PX1 - PX0) + 1e-6
    return PY0 + scale * 3.4 * (t ** 3 / (np.exp(t) - 1)) / 1.42


def rj(x):
    t = (x - PX0) / (PX1 - PX0)
    return PY0 + 3.7 * t * t


def data_dots(scale=1.0, color=NAVY, n=8):
    xs = np.linspace(PX0 + 0.3, PX1 - 0.35, n)
    return VGroup(*[Dot([x, planck_shape(x, scale, 7.0), 0], radius=0.045,
                        color=color) for x in xs])


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def serif_lines(lines, size=26, color=INK, buff=0.16):
    g = VGroup(*[Text(t, font=SERIF, color=color, font_size=size)
                 for t in lines])
    g.arrange(DOWN, buff=buff)
    return fit(g)


# --------------------------------------------------------------- the tangent
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
    "values_claim": "(unused)",
})


def anchor_card(spotlight=None):
    card = EquationCard(r"E = h\nu", spotlight=spotlight, width=4.2,
                        plain="E = hν")
    return card.to_edge(UP, buff=1.1)


# ------------------------------------------------------------------- scenes

class B02_Title(Scene):            # 9.8s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=22)
        eye.to_edge(UP, buff=1.4)
        title = VGroup(*[Text(w, font=SERIF, color=INK, font_size=48,
                              weight=BOLD)
                         for w in ("THE", "ULTRAVIOLET", "CATASTROPHE")])
        title.arrange(DOWN, buff=0.18)
        fit(title)
        u = Line(title.get_corner(DL) + DOWN * 0.2,
                 title.get_corner(DR) + DOWN * 0.2, color=CRIMSON,
                 stroke_width=2)
        sub = serif_lines(["why physics predicted", "infinite light"], size=26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(7.6)


class B04_MeasuredHump(Scene):     # 9.46s
    def construct(self):
        lb = SerifLabel("what Berlin measured", NAVY, size=24)
        fit(lb).to_edge(UP, buff=1.2)
        ch = chart_axes()
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.8)
        self.play(Create(ch[0]), run_time=1.0)
        self.play(FadeIn(ch[1]), FadeIn(ch[2]), run_time=0.5)
        cool = smooth_curve(lambda x: planck_shape(x, 0.62, 7.0),
                            PX0 + 0.15, PX1 - 0.15, NAVY, width=4.5)
        self.play(Create(cool), run_time=2.2, rate_func=linear)
        hot = smooth_curve(lambda x: planck_shape(x, 1.0, 5.5),
                           PX0 + 0.15, PX1 - 0.15, NAVY, width=3.5)
        hot.set_stroke(opacity=0.45)
        hot_lb = Text("hotter", font=SERIF, color=NAVY, font_size=18)
        hot_lb.move_to([fxp(0.513), PY0 + 1.1, 0])
        self.play(Create(hot), FadeIn(hot_lb), run_time=1.8, rate_func=linear)
        self.wait(2.7)


class B06_EqualShares(Scene):      # 9.93s
    def construct(self):
        lb = serif_lines(["every vibration gets", "the same wage"], size=28,
                         color=INK)
        lb.to_edge(UP, buff=1.2)
        u = Line(lb.get_corner(DL) + DOWN * 0.12, lb.get_corner(DR) + DOWN * 0.12,
                 color=TERRA, stroke_width=1.6)
        grid = IsotypeGrid([30], [SLATE], per_row=5, size=0.42, gap=0.22)
        grid.move_to(DOWN * 0.5)
        fit(grid)
        chip = LabelChip("kT each", accent=TERRA, size=22)
        chip.next_to(grid, DOWN, buff=0.5)
        self.play(FadeIn(lb), Create(u), run_time=0.9)
        self.play(grid.count_up(4.5, lag_ratio=0.01))
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.7)
        self.wait(3.8)


class B07_RJRunaway(Scene):        # 9.69s
    def construct(self):
        lb = serif_lines(["the Rayleigh–Jeans", "prediction"], size=26,
                         color=CRIMSON)
        lb.to_edge(UP, buff=1.2)
        ch = chart_axes(); self.add(ch)
        self.add(data_dots(0.62))
        self.play(FadeIn(lb), run_time=0.9)
        run = smooth_curve(rj, PX0 + 0.15, fxp(0.97), CRIMSON, width=5)
        self.play(Create(run), run_time=4.6, rate_func=linear)
        self.wait(4.2)


class B09_WhichAssumption(Scene):  # 11.55s — checklist: marks INSIDE, left
    def construct(self):
        def row(text, color, checked):
            mark = Text("✓" if checked else " ", font=SERIF, color=NAVY,
                        font_size=28)
            lb = SerifLabel(text, color, size=26)
            if lb.width > 3.1:
                lb.scale_to_fit_width(3.1)
            r = VGroup(mark, lb).arrange(RIGHT, buff=0.25)
            return r, mark, lb
        r1, c1, _ = row("counting the modes", BLUE, True)
        r2, c2, _ = row("equal shares for each", BLUE, True)
        r3, _, l3 = row("energy flows continuously", INK, False)
        rows = VGroup(r1, r2, r3).arrange(DOWN, aligned_edge=LEFT, buff=0.85)
        fit(rows)
        c1.set_opacity(0); c2.set_opacity(0)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.8)
        self.play(c1.animate.set_opacity(1), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.8)
        self.play(c2.animate.set_opacity(1), run_time=0.5)
        self.wait(1.6)
        self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.8)
        ring = HandRing(l3, color=TERRA)
        self.play(Create(ring), run_time=1.1)
        self.wait(4.2)


class B11_Staircase(Scene):        # 10.03s
    def construct(self):
        lb = SerifLabel("allowed energies", NAVY, size=26)
        fit(lb).to_edge(UP, buff=1.2)
        steps, labels = VGroup(), ["0", "hν", "2hν", "3hν"]
        for i in range(4):
            s = Line([-1.7 + i * 0.95, -2.2 + i * 1.05, 0],
                     [-0.8 + i * 0.95, -2.2 + i * 1.05, 0],
                     color=SLATE, stroke_width=9)
            t = Text(labels[i], font=SERIF, color=INK, font_size=24,
                     slant=ITALIC)
            t.next_to(s, UP, buff=0.15)
            steps.add(VGroup(s, t))
        marker = Dot([-1.25, -2.2 + 0.525, 0], radius=0.12, color=CRIMSON)
        self.play(Write(lb[0]), Create(lb[1]), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in steps],
                              lag_ratio=0.25, run_time=2.4))
        self.play(FadeIn(marker), run_time=0.4)
        self.wait(1.2)
        self.play(marker.animate.move_to([-0.6, -1.65, 0]), run_time=0.7)
        self.play(marker.animate.move_to([0.02, -2.2 + 1.05 + 0.12, 0]),
                  run_time=0.5)               # right half of the step — clear of the hν label
        self.wait(3.9)


class T01_EqSentences(Scene):      # 9.98s
    def construct(self):
        anchor = anchor_card()
        eye = LabelChip("CHUNK LAW · TANGENT", accent=CRIMSON, size=18)
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        d = TANGENT.d
        rows = VGroup()
        for tag, sentence in (("LHS", ["The energy of one", "chunk of light."]),
                              ("RHS", ["Its frequency, times a new",
                                       "constant of nature."])):
            chip = Text(tag, font=SERIF, color=WHITE, font_size=16)
            box = SurroundingRectangle(chip, buff=0.08).set_fill(NAVY, 1).set_stroke(width=0)
            body = serif_lines(sentence, size=24, buff=0.1)
            row = VGroup(VGroup(box, chip), body).arrange(RIGHT, buff=0.25,
                                                          aligned_edge=UP)
            rows.add(fit(row))
        claim = serif_lines(["Exactly equal — in-between", "energies are banned."],
                            size=24)
        cu = Line(claim.get_corner(DL) + DOWN * 0.1,
                  claim.get_corner(DR) + DOWN * 0.1, color=CRIMSON,
                  stroke_width=1.6)
        rows.add(VGroup(claim, cu))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        rows.move_to(DOWN * 1.1)
        fit(rows)
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.8)
            self.wait(1.6)
        self.wait(1.5)


class T02_EqGlossary(Scene):       # 10.48s — portrait glossary: stacked blocks
    def construct(self):
        anchor = anchor_card(spotlight="h")
        self.add(anchor)
        blocks = VGroup()
        for r in TANGENT.d["glossary"]:
            hot = r["sym"] == "h"
            sym = _math(r["sym_tex"], font_size=34,
                        color=CRIMSON if hot else INK, plain=r["sym"])
            role = Text(r["role"], font=SERIF, font_size=18, slant=ITALIC,
                        color=TERRA if hot else BLUE)
            top = VGroup(sym, role).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
            mean = Text(r["mean"], font=SERIF, color=INK, font_size=20)
            dom = Text(r["dom"], font=MONO, color=INK, font_size=15)
            blk = VGroup(top, fit(mean), dom).arrange(DOWN, aligned_edge=LEFT,
                                                      buff=0.12)
            blocks.add(fit(blk))
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        blocks.move_to(DOWN * 1.2)
        fit(blocks)
        self.play(FadeIn(blocks, shift=UP * 0.15), run_time=1.0)
        self.wait(9.5)


class T03_EqExample(Scene):        # 10.87s
    def construct(self):
        anchor = anchor_card()
        self.add(anchor)
        ex = TANGENT.d["example"]
        scenario = serif_lines(["A forge at 3000 K.",
                                "Thermal budget per mode: 0.26 eV."], size=22)
        lv = Text(ex["lhs_val"], font=MONO, color=CRIMSON, font_size=34)
        rv = Text(ex["rhs_val"], font=MONO, color=NAVY, font_size=34)
        vs = Text("vs", font=SERIF, color=BLUE, font_size=20)
        pair = VGroup(lv, vs, rv).arrange(DOWN, buff=0.18)
        verdict = serif_lines(["UV ≈ 48× the budget", "— unaffordable"],
                              size=24)
        vu = Line(verdict.get_corner(DL) + DOWN * 0.1,
                  verdict.get_corner(DR) + DOWN * 0.1, color=TERRA,
                  stroke_width=1.6)
        cost = serif_lines(["High frequencies go dark.",
                            "The catastrophe is cancelled."], size=19)
        for t in cost:
            t.set_slant = None
        stack = VGroup(scenario, pair, VGroup(verdict, vu), cost)
        stack.arrange(DOWN, buff=0.45).move_to(DOWN * 1.15)
        fit(stack)
        self.play(FadeIn(stack[0]), run_time=0.8)
        self.wait(1.8)
        self.play(FadeIn(stack[1], shift=UP * 0.15), run_time=0.9)
        self.wait(2.0)
        self.play(FadeIn(stack[2]), run_time=0.7)
        self.wait(1.6)
        self.play(FadeIn(stack[3]), run_time=0.7)
        self.wait(2.4)


class B12_PlanckCurve(Scene):      # 12.56s
    def construct(self):
        ch = chart_axes(); self.add(ch)
        self.add(data_dots(0.62))
        ghost = smooth_curve(rj, PX0 + 0.15, fxp(0.97), CRIMSON, width=4)
        self.add(ghost)
        self.wait(0.8)
        grey = smooth_curve(rj, PX0 + 0.15, fxp(0.97), INK, width=2.5)
        grey.set_stroke(opacity=0.22)
        self.play(Transform(ghost, grey), run_time=1.2)
        pl = smooth_curve(lambda x: planck_shape(x, 0.62, 7.0),
                          PX0 + 0.15, PX1 - 0.15, NAVY, width=5)
        self.play(Create(pl), run_time=4.4, rate_func=linear)
        chip = LabelChip("PLANCK 1900", accent=NAVY, size=22)
        chip.to_edge(UP, buff=1.3)
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.7)
        self.wait(4.7)


class B13_TwentyOrders(Scene):     # 7.94s
    def construct(self):
        n = Text("10²⁰", font=SERIF, color=CRIMSON, font_size=130, weight=BOLD)
        fit(n)
        zeros = serif_lines(["100,000,000,000,", "000,000,000 ×"], size=26)
        for z in zeros:
            z.font = MONO
        sub = serif_lines(["too bright — the classical", "error in the ultraviolet"],
                          size=22)
        stack = VGroup(n, zeros, sub).arrange(DOWN, buff=0.5)
        fit(stack)
        self.play(FadeIn(n, shift=UP * 0.2), run_time=0.8)
        self.wait(1.6)
        self.play(Write(zeros), run_time=1.6)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(3.3)
