"""vox_scenes.py — Why One Data Point Can Beat Your Thousand-Point Average
(vox-heavy-tail-yank, slate cut, 16:9).

One Scene per GRAPHIC/DOCUMENT/COMPOSITE beat whose source is 'own'.
B01 (title CARD), B04 (question CARD), B15 (endcard CARD) are rendered by the
card renderer in vox_run.sh — no Scene class needed.
B12 is STILL·ai — no scene (compiles as slate).

Color law: teal #1F6F5C = converging distribution / CLT holds / what works;
crimson #BF3339 = heavy tail / lurching mean / catastrophic outlier (villain).
Gold #F5D061 = editor's-pen highlight, once per graphic (fill only, never text).

Exclusions honored: no Cauchy proof, no CLT full statement, no CI formulas,
no power-law taxonomy.

Gate B: every zero-width stroke is also zero-opacity; all labels clear of lines.
"""
import sys
import json
import pathlib
import numpy as np

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene

# ── duration table (actual from audio; estimates as fallback) ─────────────────
DUR = {
    "B01": 4.0,
    "B02": 9.5, "B03": 7.0, "B05": 11.0, "B06": 11.5,
    "B07": 9.5, "B08": 8.0, "B09": 8.0,  "B10": 11.5,
    "B11": 9.5, "B13": 8.5, "B14": 10.5,
    "B15": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update(
        {b["beat_id"]: float(
            b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0
        ) for b in _BS["beats"]}
    )
except Exception:
    pass

# ── pre-computed running average traces ───────────────────────────────────────

# B02/B03 — 30-point settling trace: starts volatile, converges near zero
_SETTLE_XS = [-5.5 + i * (11.0 / 29) for i in range(30)]
_SETTLE_YS = [
    2.1, -1.3, 1.5, 0.7, -0.3, 0.8, 0.1, 0.4, -0.1, 0.2,
    0.13, 0.06, 0.17, -0.04, 0.09, 0.03, 0.06, -0.02, 0.04, 0.01,
    0.02, -0.01, 0.02, 0.00, 0.01, -0.01, 0.01, 0.00, 0.01, 0.00,
]

# B08 — 40-point Gaussian trace: clearly converging (teal)
_GAUSS_XS = [-5.5 + i * (11.0 / 39) for i in range(40)]
_GAUSS_YS = [
    2.1, -1.0, 0.8, 0.4, -0.1, 0.3, 0.05, 0.2, -0.05, 0.12,
    0.08, 0.03, 0.09, -0.02, 0.05, 0.02, 0.04, -0.01, 0.02, 0.01,
    0.015, -0.008, 0.012, 0.005, 0.008, -0.005, 0.007, 0.004, 0.005, 0.003,
    0.004, -0.003, 0.003, 0.002, 0.003, -0.002, 0.002, 0.001, 0.002, 0.001,
]

# B09 — 40-point heavy-tail trace: keeps lurching at n=5,9,17,25,33,39 (crimson)
_HEAVY_XS = [-5.5 + i * (11.0 / 39) for i in range(40)]
_HEAVY_YS = [
    2.0, -0.8, 0.6, 0.3, 1.4, 0.4, 0.1, 0.3, -1.1, 0.2,
    0.15, 0.1, 0.08, 0.06, 0.07, 0.05, 2.2, 0.18, 0.14, 0.11,
    0.10, 0.09, 0.08, 0.07, -0.85, 0.06, 0.05, 0.04, 0.04, 0.04,
    0.03, 0.03, 1.75, 0.03, 0.025, 0.02, 0.02, 0.02, -0.65, 0.02,
]


# ── helper ────────────────────────────────────────────────────────────────────

def _trace(xs, ys, color, stroke_width=3.5):
    """VMobject polyline from pre-computed (xs, ys) lists."""
    pts = [np.array([xs[i], ys[i], 0]) for i in range(len(xs))]
    vm = VMobject()
    vm.set_points_as_corners(pts)
    vm.set_color(color)
    vm.set_stroke(width=stroke_width)
    vm.set_fill(opacity=0)
    return vm


# ── scenes ────────────────────────────────────────────────────────────────────

class B01_Title(Scene):
    """COLD OPEN title card — COMPUTATIONAL SKEPTICISM eyebrow + title."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why One Data Point Can", font=DISPLAY, color=INK,
                  font_size=34, weight=BOLD)
        t2 = Text("Beat Your Thousand-Point Average", font=DISPLAY, color=CRIMSON,
                  font_size=34, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B02_TraceBuild(Scene):
    """COLD OPEN pt.1 — running average builds up and appears to settle."""
    def construct(self):
        total = DUR["B02"]

        ref = Line([-5.7, 0, 0], [5.7, 0, 0])
        ref.set_stroke(color=SLATE, width=1.2, opacity=0.4)

        trace = _trace(_SETTLE_XS, _SETTLE_YS, TEAL)

        lbl = SerifLabel("running average", accent=TEAL, size=28)
        lbl.move_to([3.2, 0.65, 0])   # above the settled right end of the trace

        self.play(Create(ref), run_time=0.7)
        self.play(Create(trace), run_time=2.0)
        self.play(FadeIn(lbl), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B03_YankTrace(Scene):
    """COLD OPEN pt.2 — one extreme case yanks the running mean."""
    def construct(self):
        total = DUR["B03"]

        # Settled trace: last 15 SETTLE points, displayed x: -5.5 to 3.5
        settled_xs = [-5.5 + i * (9.0 / 14) for i in range(15)]
        settled_ys = _SETTLE_YS[15:]   # all near 0

        settled = _trace(settled_xs, settled_ys, TEAL, stroke_width=3.5)

        # The extreme observation — far above the settled line
        extreme_dot = Dot(radius=0.22)
        extreme_dot.set_fill(CRIMSON, 1.0)
        extreme_dot.set_stroke(width=0, opacity=0)
        extreme_dot.move_to([4.5, 3.0, 0])

        # The running mean lurches upward after the extreme arrives
        lurch = Line([3.5, 0.0, 0], [4.5, 1.8, 0])
        lurch.set_stroke(color=CRIMSON, width=3.5)

        # Label — upper-left of the extreme dot, clear of the lurch line
        lbl = SerifLabel("one case", accent=CRIMSON, size=28)
        lbl.move_to([3.3, 3.4, 0])

        self.play(Create(settled), run_time=0.7)
        self.play(GrowFromCenter(extreme_dot), run_time=0.6)
        self.play(Create(lurch), run_time=0.7)
        self.play(FadeIn(lbl), run_time=0.5)
        self.wait(max(0.5, total - 2.5))


class B05_BellCurve(Scene):
    """THE PROBLEM pt.1 — the Gaussian: the naive expectation."""
    def construct(self):
        total = DUR["B05"]

        baseline = Line([-6.0, 0, 0], [6.0, 0, 0])
        baseline.set_stroke(color=SLATE, width=1.5, opacity=0.45)

        gaussian = ParametricFunction(
            lambda t: np.array([t * 3.5, 2.8 * np.exp(-(t ** 2)), 0]),
            t_range=[-2.0, 2.0, 0.05],
            color=TEAL,
            stroke_width=3.5,
        )
        gaussian.set_fill(opacity=0)

        # Label to the right where the curve is near-flat (y≈0.56 at x=4.8)
        lbl = SerifLabel("well-behaved distribution", accent=TEAL, size=26)
        lbl.move_to([4.5, 2.1, 0])

        self.play(Create(baseline), run_time=0.7)
        self.play(Create(gaussian), run_time=1.5)
        self.play(FadeIn(lbl), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


class B06_HeavyTail(Scene):
    """THE PROBLEM pt.2 — the heavy-tailed distribution (the broken condition)."""
    def construct(self):
        total = DUR["B06"]

        baseline = Line([-6.0, 0, 0], [6.0, 0, 0])
        baseline.set_stroke(color=SLATE, width=1.5, opacity=0.45)

        cauchy = ParametricFunction(
            lambda t: np.array([t * 3.5, 2.8 / (1.0 + t ** 2), 0]),
            t_range=[-2.0, 2.0, 0.05],
            color=CRIMSON,
            stroke_width=3.5,
        )
        cauchy.set_fill(opacity=0)

        # Gold highlight on the extended tails — fill only, zero stroke
        tail_l = Rectangle(width=2.5, height=0.42)
        tail_l.set_fill(GOLD, 0.38)
        tail_l.set_stroke(width=0, opacity=0)
        tail_l.move_to([-5.75, 0.21, 0])

        tail_r = Rectangle(width=2.5, height=0.42)
        tail_r.set_fill(GOLD, 0.38)
        tail_r.set_stroke(width=0, opacity=0)
        tail_r.move_to([5.75, 0.21, 0])

        # Label — right side, above curve height at that x (y≈0.97 at x=4.8)
        lbl = SerifLabel("heavy-tailed distribution", accent=CRIMSON, size=26)
        lbl.move_to([4.5, 2.1, 0])

        self.play(Create(baseline), run_time=0.7)
        self.play(Create(cauchy), run_time=1.5)
        self.play(FadeIn(VGroup(tail_l, tail_r)), run_time=0.6)
        self.play(FadeIn(lbl), run_time=0.5)
        self.wait(max(0.5, total - 3.3))


class B07_QuoteNoMatter(Scene):
    """THE PROBLEM pt.3 — quote: no matter how many you have collected."""
    def construct(self):
        _quote_scene(
            self,
            "The next observation can move your average dramatically,"
            " no matter how many you have already collected.",
            "-- the heavy-tail problem, Chapter 2",
            None,
            "no matter",
            DUR["B07"],
        )


class B08_GaussianTrace(Scene):
    """MECHANISM pt.1 — Gaussian running mean: it settles."""
    def construct(self):
        total = DUR["B08"]

        ref = Line([-5.7, 0, 0], [5.7, 0, 0])
        ref.set_stroke(color=SLATE, width=1.2, opacity=0.35)

        trace = _trace(_GAUSS_XS, _GAUSS_YS, TEAL)

        # Label above the settled right end (max GAUSS_YS right-half ≈ 0.008)
        lbl = SerifLabel("settles", accent=TEAL, size=30)
        lbl.move_to([4.0, 0.55, 0])

        self.play(Create(ref), run_time=0.7)
        self.play(Create(trace), run_time=2.0)
        self.play(FadeIn(lbl), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B09_HeavyTrace(Scene):
    """MECHANISM pt.2 — heavy-tail running mean: never settles."""
    def construct(self):
        total = DUR["B09"]

        ref = Line([-5.7, 0, 0], [5.7, 0, 0])
        ref.set_stroke(color=SLATE, width=1.2, opacity=0.35)

        trace = _trace(_HEAVY_XS, _HEAVY_YS, CRIMSON)

        # Label above the trace; max HEAVY_YS = 2.2 (at index 16)
        # Place label at y=3.0 — 0.8 clear of the peak
        lbl = SerifLabel("never settles", accent=CRIMSON, size=30)
        lbl.move_to([3.8, 3.0, 0])

        self.play(Create(ref), run_time=0.7)
        self.play(Create(trace), run_time=2.0)
        self.play(FadeIn(lbl), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B10_CompareTraces(Scene):
    """MECHANISM pt.3 — THE COMPARE MOVE: left settles, right never does."""
    def construct(self):
        total = DUR["B10"]

        # Left panel: Gaussian trace (teal), x from -5.5 to -0.5
        left_xs = [-5.5 + i * (5.0 / 39) for i in range(40)]
        left_trace = _trace(left_xs, _GAUSS_YS, TEAL)

        # Right panel: heavy-tail trace (crimson), x from 0.5 to 5.5
        right_xs = [0.5 + i * (5.0 / 39) for i in range(40)]
        right_trace = _trace(right_xs, _HEAVY_YS, CRIMSON)

        # Vertical dividing line at x=0 — within safe area (±3.4 y)
        div_line = Line([0, -3.2, 0], [0, 3.2, 0])
        div_line.set_stroke(color=SLATE, width=1.5, opacity=0.5)

        # LabelChips above each panel
        # GAUSS_YS max left panel ≈ 2.1 (index 0); HEAVY_YS max right ≈ 2.2 (index 16)
        # Chips at y=3.1 — safely above both trace peaks
        chip_l = LabelChip("converges", accent=TEAL, size=24)
        chip_l.move_to([-2.5, 3.1, 0])

        chip_r = LabelChip("never settles", accent=CRIMSON, size=24)
        chip_r.move_to([2.8, 3.1, 0])

        self.play(Create(div_line), run_time=0.7)
        self.play(
            AnimationGroup(Create(left_trace), Create(right_trace), lag_ratio=0.0),
            run_time=2.0,
        )
        self.play(FadeIn(VGroup(chip_l, chip_r)), run_time=0.7)
        self.wait(max(0.5, total - 3.4))


class B11_ExtremeWeight(Scene):
    """MECHANISM pt.4 — why: tail extremes keep arriving large enough to matter."""
    def construct(self):
        total = DUR["B11"]

        number_line = Line([-5.5, -1.5, 0], [5.5, -1.5, 0])
        number_line.set_stroke(color=SLATE, width=2.0, opacity=0.6)

        # Teal dots — typical observations near center of distribution
        teal_xs = [-1.5, -0.8, -0.2, 0.3, 0.5, 0.9, 1.3, 1.6]
        teal_dots = VGroup(*[
            Dot(radius=0.13, point=[x, -1.5, 0])
            .set_fill(TEAL, 0.9)
            .set_stroke(width=0, opacity=0)
            for x in teal_xs
        ])

        # Crimson dots — tail extremes (larger = more weight on the mean)
        crimson_xs = [3.2, 4.3, 5.2]
        crimson_dots = VGroup(*[
            Dot(radius=0.22, point=[x, -1.5, 0])
            .set_fill(CRIMSON, 1.0)
            .set_stroke(width=0, opacity=0)
            for x in crimson_xs
        ])

        # Labels — above the clusters; well clear of the number_line at y=-1.5
        lbl_typ = SerifLabel("typical observations", accent=TEAL, size=26)
        lbl_typ.move_to([0.0, -0.82, 0])  # above teal cluster; bottom ≈ -1.0, line at -1.5

        lbl_tail = SerifLabel("tail extremes", accent=CRIMSON, size=26)
        lbl_tail.move_to([4.2, -0.82, 0])  # above crimson dots

        self.play(Create(number_line), run_time=0.7)
        self.play(AnimationGroup(*[GrowFromCenter(d) for d in teal_dots], lag_ratio=0.06))
        self.play(AnimationGroup(*[GrowFromCenter(d) for d in crimson_dots], lag_ratio=0.12))
        self.play(FadeIn(lbl_typ), FadeIn(lbl_tail), run_time=0.6)
        self.wait(max(0.5, total - 3.2))


class B13_BarChart(Scene):
    """IMPLICATION pt.2 — 99 cheap errors vs. one catastrophic outlier."""
    def construct(self):
        total = DUR["B13"]

        baseline = Line([-5.7, 0, 0], [2.1, 0, 0])
        baseline.set_stroke(color=SLATE, width=1.5, opacity=0.6)

        # 15 small teal bars (schematic representation of the 99 cheap errors)
        bar_w, bar_h_sm, bar_gap = 0.22, 0.4, 0.07
        step = bar_w + bar_gap
        start_cx = -5.4 + bar_w / 2

        small_bars = VGroup(*[
            Rectangle(width=bar_w, height=bar_h_sm)
            .set_fill(TEAL, 0.85)
            .set_stroke(TEAL, 1.2)
            .move_to([start_cx + i * step, bar_h_sm / 2, 0])
            for i in range(15)
        ])

        # 1 giant crimson bar — the catastrophic $3M case
        giant_bar = Rectangle(width=0.8, height=2.8)
        giant_bar.set_fill(CRIMSON, 0.9)
        giant_bar.set_stroke(CRIMSON, 1.8)
        giant_bar.move_to([0.9, 1.4, 0])  # bottom at y=0, top at y=2.8

        # PT Mono cost labels (clear of bar tops; within ±3.4 safe area)
        lbl_sm = Text("$30", font=MONO, font_size=26)
        lbl_sm.set_color(TEAL)
        lbl_sm.move_to([-3.0, 0.75, 0])   # above small bars (top at y=0.4)

        lbl_big = Text("$3,000,000", font=MONO, font_size=22)
        lbl_big.set_color(CRIMSON)
        lbl_big.move_to([0.9, 3.2, 0])    # above giant bar (top at y=2.8), within safe area

        self.play(Create(baseline), run_time=0.6)
        self.play(
            AnimationGroup(*[GrowFromEdge(b, DOWN) for b in small_bars], lag_ratio=0.02),
            run_time=0.8,
        )
        self.play(GrowFromEdge(giant_bar, DOWN), run_time=0.7)
        self.play(FadeIn(lbl_sm), FadeIn(lbl_big), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B14_QuoteTailAware(Scene):
    """IMPLICATION pt.3 — quote: the question is what happens when the extreme arrives."""
    def construct(self):
        _quote_scene(
            self,
            "You need tail-aware metrics. Worst-case analysis."
            " The question isn't what happens on average --"
            " it's what happens when the extreme arrives.",
            "-- Chapter 2, Computational Skepticism for AI",
            None,
            "extreme arrives",
            DUR["B14"],
        )


class B15_ExampleTail(Scene):
    """THE EXAMPLE — document-processing AI: 10 normal + 1 outlier yanks the running average."""
    def construct(self):
        total = DUR["B15"]
        title = Text("Document-Processing AI — run time", font=DISPLAY,
                     font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("10 normal docs", font=DISPLAY, font_size=22, color=TEAL, weight=BOLD)
        lbl_l.move_to(col_l.get_top() + DOWN * 0.45)
        val_l1 = Text("avg: 0.3 s", font=MONO, font_size=30, color=TEAL)
        val_l1.move_to(col_l.get_center() + UP * 0.2)
        val_l2 = Text("SLA: 1.0 s  ✓", font=MONO, font_size=22, color=TEAL)
        val_l2.move_to(col_l.get_center() + DOWN * 0.8)

        lbl_r = Text("+ 1 outlier", font=DISPLAY, font_size=22, color=CRIMSON, weight=BOLD)
        lbl_r.move_to(col_r.get_top() + DOWN * 0.45)
        val_r1 = Text("300 s", font=MONO, font_size=38, color=CRIMSON)
        val_r1.move_to(col_r.get_center() + UP * 0.2)
        val_r2 = Text("(full re-index)", font=SERIF, font_size=20, color=CRIMSON)
        val_r2.move_to(col_r.get_center() + DOWN * 0.6)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("new running avg: 27 s — 90× the prior average",
                        font=SERIF, font_size=20, color=CRIMSON)
        note_txt.move_to(note_rect.get_center())

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(col_l), FadeIn(lbl_l), run_time=0.7)
        self.play(FadeIn(val_l1), FadeIn(val_l2), run_time=0.6)
        self.play(FadeIn(col_r), FadeIn(lbl_r), run_time=0.7)
        self.play(FadeIn(val_r1), run_time=0.5)
        self.play(FadeIn(val_r2), run_time=0.5)
        self.play(FadeIn(note_rect), FadeIn(note_txt), run_time=0.7)
        self.wait(max(0.5, total - 4.4))
