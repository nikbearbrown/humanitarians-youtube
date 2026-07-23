"""vox_scenes.py — Same Average Size, Different Product
(vox-batch-distribution, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT beat whose source is 'own'.
B02 is the only STILL (ai media slot) and has no scene here.
Durations read from this reel's beat_sheet.json (actuals after audio lock;
estimates as fallback).

Render:
  bash vox/scripts/vox_run.sh cancer-nanomedicine/youtube/vox-batch-distribution

Color law: TEAL #1F6F5C = narrow / controlled / monodisperse / low PDI (good);
           CRIMSON #BF3339 = wide / heterogeneous / high PDI (the problem).
           GOLD = editor's pen (mean tick, quote highlight) — NEVER text color.
Exclusions: NO TEM artifacts, NO GMP tour, NO olaratumab, NO cascade,
            NO encapsulation efficiency. One concept: mean != distribution.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import json, os
import numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Same Average Size, Different Product", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        t2 = Text("Why Batches Can't Be Proved Identical Like Pills", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ---------------------------------------------------------------- B03 The Question

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text(
            "Two batches of the same cancer nanoparticle",
            font=DISPLAY, color=INK, font_size=22, weight=BOLD
        )
        q2 = Text(
            "measure the same average particle size.",
            font=DISPLAY, color=INK, font_size=22, weight=BOLD
        )
        q3 = Text(
            "Regulators say they are not the same product.",
            font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD
        )
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.22).move_to(UP * 0.5)
        sub = Text("Why isn't the average enough?", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        u = Line(sub.get_corner(DL) + DOWN * 0.1, sub.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=1.8)
        sub.next_to(block, DOWN, buff=0.55)
        self.play(FadeIn(q1), FadeIn(q2), run_time=1.0)
        self.play(FadeIn(q3), run_time=0.7)
        self.play(FadeIn(sub), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.6))


# ---------------------------------------------------------------- B04 Small Molecule — binary identity

class B04_SmallMolecule(Scene):
    def construct(self):
        total = DUR["B04"]
        # One teal dot = one defined structure
        dot = Dot(radius=0.28).set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        dot.move_to(UP * 0.6)
        struct_label = SerifLabel("one defined structure", TEAL, size=26)
        struct_label.next_to(dot, DOWN, buff=0.35)
        # Binary bracket
        bracket_line = Line(LEFT * 2.8 + DOWN * 0.7, RIGHT * 2.8 + DOWN * 0.7,
                            color=INK, stroke_width=2)
        tick_l = Line(LEFT * 2.8 + DOWN * 0.55, LEFT * 2.8 + DOWN * 0.85,
                      color=INK, stroke_width=2)
        tick_r = Line(RIGHT * 2.8 + DOWN * 0.55, RIGHT * 2.8 + DOWN * 0.85,
                      color=INK, stroke_width=2)
        yes_label = Text("identical", font=DISPLAY, color=TEAL, font_size=20)
        yes_label.next_to(tick_l, DOWN, buff=0.18)
        no_label = Text("not identical", font=DISPLAY, color=CRIMSON, font_size=20)
        no_label.next_to(tick_r, DOWN, buff=0.18)
        or_label = Text("or", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        or_label.move_to(DOWN * 0.7)
        self.play(FadeIn(dot, scale=0.7), run_time=0.6)
        self.play(FadeIn(struct_label), run_time=0.6)
        self.play(Create(bracket_line), Create(tick_l), Create(tick_r), run_time=0.8)
        self.play(FadeIn(yes_label), FadeIn(no_label), FadeIn(or_label), run_time=0.7)
        self.wait(max(0.3, total - 2.7))


# ---------------------------------------------------------------- B05 Nano Cloud — population

class B05_NanoCloud(Scene):
    def construct(self):
        total = DUR["B05"]
        # Create dots of varying sizes in a bell-shaped spread
        rng = np.random.default_rng(42)
        # sizes sampled from a narrow normal for illustration
        sizes = rng.normal(0, 1.6, 30)
        # Create dots
        dots = VGroup()
        for i, x_val in enumerate(sizes):
            y_val = rng.uniform(-0.6, 0.6)
            r = 0.08 + abs(x_val) * 0.01  # vary radius slightly
            d = Dot(radius=max(0.06, min(0.18, r)))
            d.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * x_val * 0.5 + UP * y_val)
            dots.add(d)
        # Mean tick (gold vertical line)
        mean_tick = Line(DOWN * 0.9, UP * 0.9, color=GOLD, stroke_width=3)
        mean_tick.move_to(ORIGIN)
        mean_label = Text("mean", font=MONO, color=INK, font_size=20)
        mean_label.next_to(mean_tick, UP, buff=0.2)
        # Labels
        pop_label = SerifLabel("population", TEAL, size=28)
        pop_label.move_to(DOWN * 1.8)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots],
                              lag_ratio=0.04, run_time=1.6))
        self.play(Create(mean_tick), FadeIn(mean_label), run_time=0.7)
        self.play(FadeIn(pop_label), run_time=0.6)
        self.wait(max(0.3, total - 2.9))


# ---------------------------------------------------------------- B06 Two Histograms — the core compare

def _histogram_bars(x_center, bar_heights, bar_width=0.22, bar_gap=0.04,
                    color=TEAL, baseline_y=-1.8):
    """Build a VGroup of Rectangle bars for a histogram.
    bar_heights: list of relative heights (0-1 scale, will be multiplied by 3.2).
    Returns VGroup of bars positioned around x_center."""
    bars = VGroup()
    n = len(bar_heights)
    total_width = n * bar_width + (n - 1) * bar_gap
    x_start = x_center - total_width / 2
    max_h = 3.2
    for i, h in enumerate(bar_heights):
        bar_h = max(0.04, h * max_h)
        bar = Rectangle(width=bar_width, height=bar_h)
        bar.set_fill(color, 0.85).set_stroke(width=0, opacity=0)
        bar.align_to(np.array([0, baseline_y, 0]), DOWN)
        bar.move_to(np.array([x_start + i * (bar_width + bar_gap) + bar_width / 2,
                               baseline_y + bar_h / 2, 0]))
        bars.add(bar)
    return bars


class B06_TwoHistograms(Scene):
    def construct(self):
        total = DUR["B06"]
        baseline_y = -1.5
        # Narrow distribution (PDI 0.07) — tight spike, TEAL
        narrow_heights = [0.02, 0.05, 0.12, 0.28, 0.72, 1.0, 0.72, 0.28, 0.12, 0.05, 0.02]
        # Wide distribution (PDI 0.31) — broad bell, CRIMSON
        wide_heights   = [0.08, 0.14, 0.22, 0.34, 0.52, 0.65, 0.52, 0.34, 0.22, 0.14, 0.08]
        left_x  = -3.2
        right_x =  3.2
        narrow_bars = _histogram_bars(left_x,  narrow_heights, color=TEAL,    baseline_y=baseline_y)
        wide_bars   = _histogram_bars(right_x, wide_heights,   color=CRIMSON, baseline_y=baseline_y)
        # Axis baselines
        left_axis  = Line(np.array([left_x  - 1.4, baseline_y, 0]),
                          np.array([left_x  + 1.4, baseline_y, 0]),
                          color=INK, stroke_width=2)
        right_axis = Line(np.array([right_x - 1.4, baseline_y, 0]),
                          np.array([right_x + 1.4, baseline_y, 0]),
                          color=INK, stroke_width=2)
        # Shared mean tick (GOLD) — same x-offset from center of each histogram
        # The mean sits at bar index 5 (center) in both
        n_bars = len(narrow_heights)
        bar_w, bar_gap = 0.22, 0.04
        total_w = n_bars * bar_w + (n_bars - 1) * bar_gap
        mean_offset = 0.0  # center of histogram = center bar
        left_mean_x  = left_x  + mean_offset
        right_mean_x = right_x + mean_offset
        left_mean_tick  = Line(np.array([left_mean_x,  baseline_y - 0.15, 0]),
                               np.array([left_mean_x,  baseline_y + 0.5, 0]),
                               color=GOLD, stroke_width=3)
        right_mean_tick = Line(np.array([right_mean_x, baseline_y - 0.15, 0]),
                               np.array([right_mean_x, baseline_y + 0.5, 0]),
                               color=GOLD, stroke_width=3)
        # Labels
        left_header  = LabelChip("Batch A  PDI 0.07", accent=TEAL,    size=22)
        right_header = LabelChip("Batch B  PDI 0.31", accent=CRIMSON, size=22)
        left_header.move_to(np.array([left_x,  1.9, 0]))
        right_header.move_to(np.array([right_x, 1.9, 0]))
        mean_label_l = Text("98 nm mean", font=MONO, color=INK, font_size=18)
        mean_label_r = Text("98 nm mean", font=MONO, color=INK, font_size=18)
        mean_label_l.next_to(left_mean_tick,  UP, buff=0.12)
        mean_label_r.next_to(right_mean_tick, UP, buff=0.12)
        narrow_label = SerifLabel("monodisperse", TEAL,    size=22)
        wide_label   = SerifLabel("heterogeneous", CRIMSON, size=22)
        narrow_label.move_to(np.array([left_x,  -2.3, 0]))
        wide_label.move_to(np.array([right_x,   -2.3, 0]))
        # Animate: headers first, then bars grow, then mean ticks, then labels
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.7)
        self.play(Create(left_axis), Create(right_axis), run_time=0.4)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in narrow_bars], lag_ratio=0.06, run_time=1.2),
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in wide_bars],   lag_ratio=0.06, run_time=1.2),
        )
        self.play(Create(left_mean_tick), Create(right_mean_tick), run_time=0.6)
        self.play(FadeIn(mean_label_l), FadeIn(mean_label_r), run_time=0.5)
        self.play(FadeIn(narrow_label), FadeIn(wide_label), run_time=0.6)
        self.wait(max(0.3, total - 4.0))


# ---------------------------------------------------------------- B07 PDI Scale

class B07_PDIScale(Scene):
    def construct(self):
        total = DUR["B07"]
        # Horizontal PDI axis
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2.5)
        axis.move_to(ORIGIN)
        axis_label = Text("Polydispersity Index (PDI)", font=DISPLAY, color=INK, font_size=20)
        axis_label.next_to(axis, DOWN, buff=0.5)
        # 0 tick
        t0 = Line(DOWN * 0.15, UP * 0.15, color=INK, stroke_width=2).move_to(LEFT * 5.3)
        l0 = Text("0", font=MONO, color=INK, font_size=20).next_to(t0, DOWN, buff=0.18)
        # 0.07 tick — teal (low PDI, good)
        x_007 = LEFT * 5.3 + RIGHT * (0.07 / 0.45) * 10.6
        t007 = Line(DOWN * 0.22, UP * 0.22, color=TEAL, stroke_width=3).move_to(x_007)
        chip_007 = LabelChip("0.07  monodisperse", accent=TEAL, size=20)
        chip_007.next_to(t007, UP, buff=0.35)
        # 0.2 threshold — dashed
        x_02 = LEFT * 5.3 + RIGHT * (0.2 / 0.45) * 10.6
        threshold = DashedLine(DOWN * 0.5, UP * 2.0, color=INK, stroke_width=1.5, dash_length=0.12)
        threshold.move_to(x_02)
        thresh_label = Text("~0.2 threshold", font=MONO, color=INK, font_size=18)
        thresh_label.next_to(threshold, UP, buff=0.15)
        # 0.31 tick — crimson (high PDI, problem)
        x_031 = LEFT * 5.3 + RIGHT * (0.31 / 0.45) * 10.6
        t031 = Line(DOWN * 0.22, UP * 0.22, color=CRIMSON, stroke_width=3).move_to(x_031)
        chip_031 = LabelChip("0.31  heterogeneous", accent=CRIMSON, size=20)
        chip_031.next_to(t031, UP, buff=0.35)
        # Animate
        self.play(Create(axis), FadeIn(axis_label), FadeIn(t0), FadeIn(l0), run_time=0.8)
        self.play(Create(t007), FadeIn(chip_007), run_time=0.7)
        self.play(Create(threshold), FadeIn(thresh_label), run_time=0.7)
        self.play(Create(t031), FadeIn(chip_031), run_time=0.7)
        self.wait(max(0.3, total - 2.9))


# ---------------------------------------------------------------- B08 Three Populations

class B08_ThreePopulations(Scene):
    def construct(self):
        total = DUR["B08"]
        baseline_y = -1.3
        # Recreate the wide crimson histogram from B06
        wide_heights = [0.08, 0.14, 0.22, 0.34, 0.52, 0.65, 0.52, 0.34, 0.22, 0.14, 0.08]
        wide_bars = _histogram_bars(0.0, wide_heights, color=CRIMSON, baseline_y=baseline_y)
        axis = Line(np.array([-1.6, baseline_y, 0]), np.array([1.6, baseline_y, 0]),
                    color=INK, stroke_width=2)
        header = LabelChip("Batch B  PDI 0.31", accent=CRIMSON, size=22)
        header.move_to(UP * 2.0)
        # Three bracket regions
        bar_w, bar_gap = 0.22, 0.04
        n = len(wide_heights)
        total_bw = n * bar_w + (n - 1) * bar_gap
        x_left = -total_bw / 2
        # Left tail: bars 0-2 (small particles)
        small_x_l = x_left + 0 * (bar_w + bar_gap)
        small_x_r = x_left + 2 * (bar_w + bar_gap) + bar_w
        small_brace_center = (small_x_l + small_x_r) / 2
        small_brace = Brace(VGroup(wide_bars[0], wide_bars[2]), DOWN, color=INK)
        small_label = Text("small:", font=DISPLAY, color=INK, font_size=17)
        small_sub   = Text("rapid clearance", font=SERIF, color=CRIMSON, font_size=17, slant=ITALIC)
        small_group = VGroup(small_label, small_sub).arrange(DOWN, buff=0.06)
        small_group.next_to(small_brace, DOWN, buff=0.15)
        # Center: bars 3-7 (mid-range)
        mid_brace = Brace(VGroup(wide_bars[3], wide_bars[7]), DOWN, color=INK)
        mid_label = Text("mid-range:", font=DISPLAY, color=INK, font_size=17)
        mid_sub   = Text("designed behavior", font=SERIF, color=TEAL, font_size=17, slant=ITALIC)
        mid_group = VGroup(mid_label, mid_sub).arrange(DOWN, buff=0.06)
        mid_group.next_to(mid_brace, DOWN, buff=0.15)
        # Right tail: bars 8-10 (large particles)
        large_brace = Brace(VGroup(wide_bars[8], wide_bars[10]), DOWN, color=INK)
        large_label = Text("large:", font=DISPLAY, color=INK, font_size=17)
        large_sub   = Text("liver / spleen", font=SERIF, color=CRIMSON, font_size=17, slant=ITALIC)
        large_group = VGroup(large_label, large_sub).arrange(DOWN, buff=0.06)
        large_group.next_to(large_brace, DOWN, buff=0.15)
        # Animate
        self.play(FadeIn(header), Create(axis), run_time=0.5)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in wide_bars],
                              lag_ratio=0.06, run_time=1.0))
        self.play(FadeIn(small_brace), FadeIn(small_group), run_time=0.7)
        self.play(FadeIn(mid_brace),   FadeIn(mid_group),   run_time=0.7)
        self.play(FadeIn(large_brace), FadeIn(large_group), run_time=0.7)
        self.wait(max(0.3, total - 3.6))


# ---------------------------------------------------------------- B09 Quote Card

class B09_QuoteCard(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Two batches with identical mean size and different PDIs are not the same product.",
            "-- NCI Nanotechnology Characterization Laboratory framework",
            None,
            "not the same product",
            DUR["B09"]
        )


# ---------------------------------------------------------------- B10 Match Mean vs Distribution

class B10_MatchMeanVsDistribution(Scene):
    def construct(self):
        total = DUR["B10"]
        # Left column: "match the mean" — two overlapping single ticks
        left_x = -3.2
        right_x = 3.2
        baseline_y = -0.5
        # Left: two overlapping mean ticks (same point)
        tick_a = Line(np.array([left_x, baseline_y - 0.8, 0]),
                      np.array([left_x, baseline_y + 0.8, 0]),
                      color=TEAL, stroke_width=4)
        tick_b = Line(np.array([left_x + 0.08, baseline_y - 0.8, 0]),
                      np.array([left_x + 0.08, baseline_y + 0.8, 0]),
                      color=CRIMSON, stroke_width=4)
        left_header = LabelChip("match the mean", accent=SLATE, size=22)
        left_header.move_to(np.array([left_x, 1.6, 0]))
        left_sub = SerifLabel("same center point", SLATE, size=22)
        left_sub.move_to(np.array([left_x, baseline_y - 1.4, 0]))
        left_verdict = Text("NOT sufficient", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        left_verdict.move_to(np.array([left_x, baseline_y - 2.0, 0]))
        # Right: two overlapping histogram outlines (same shape = match)
        narrow_h = [0.02, 0.08, 0.22, 0.55, 1.0, 0.55, 0.22, 0.08, 0.02]
        # Batch A and Batch B distributions shown as overlapping outlines
        bars_a = _histogram_bars(right_x, narrow_h, color=TEAL,    baseline_y=baseline_y)
        bars_b = _histogram_bars(right_x, narrow_h, color=CRIMSON, baseline_y=baseline_y)
        # Make B slightly transparent to show overlap
        for b in bars_b:
            b.set_fill(CRIMSON, 0.45)
        right_header = LabelChip("match the distribution", accent=SLATE, size=22)
        right_header.move_to(np.array([right_x, 1.6, 0]))
        right_sub = SerifLabel("same whole population", TEAL, size=22)
        right_sub.move_to(np.array([right_x, baseline_y - 1.4, 0]))
        right_verdict = Text("the full product", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        right_verdict.move_to(np.array([right_x, baseline_y - 2.0, 0]))
        # Animate
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.6)
        self.play(Create(tick_a), Create(tick_b), run_time=0.7)
        self.play(FadeIn(left_sub), run_time=0.5)
        self.play(FadeIn(left_verdict), run_time=0.5)
        axis_r = Line(np.array([right_x - 1.4, baseline_y, 0]),
                      np.array([right_x + 1.4, baseline_y, 0]),
                      color=INK, stroke_width=2)
        self.play(Create(axis_r), run_time=0.3)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars_a], lag_ratio=0.05, run_time=0.8),
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars_b], lag_ratio=0.05, run_time=0.8),
        )
        self.play(FadeIn(right_sub), run_time=0.5)
        self.play(FadeIn(right_verdict), run_time=0.5)
        self.wait(max(0.3, total - 4.4))


# ---------------------------------------------------------------- B11 Example Comparison (illustrative)

class B11_ExampleComparison(Scene):
    def construct(self):
        total = DUR["B11"]
        baseline_y = -1.2
        left_x  = -3.2
        right_x =  3.2
        # Narrow (Batch A) — TEAL
        narrow_h = [0.02, 0.05, 0.12, 0.30, 0.75, 1.0, 0.75, 0.30, 0.12, 0.05, 0.02]
        # Wide (Batch B) — CRIMSON
        wide_h   = [0.08, 0.15, 0.24, 0.36, 0.54, 0.68, 0.54, 0.36, 0.24, 0.15, 0.08]
        narrow_bars = _histogram_bars(left_x,  narrow_h, color=TEAL,    baseline_y=baseline_y)
        wide_bars   = _histogram_bars(right_x, wide_h,   color=CRIMSON, baseline_y=baseline_y)
        left_axis  = Line(np.array([left_x  - 1.5, baseline_y, 0]),
                          np.array([left_x  + 1.5, baseline_y, 0]),
                          color=INK, stroke_width=2)
        right_axis = Line(np.array([right_x - 1.5, baseline_y, 0]),
                          np.array([right_x + 1.5, baseline_y, 0]),
                          color=INK, stroke_width=2)
        # Shared mean tick (GOLD)
        left_mean  = Line(np.array([left_x,  baseline_y - 0.15, 0]),
                          np.array([left_x,  baseline_y + 0.55, 0]),
                          color=GOLD, stroke_width=3)
        right_mean = Line(np.array([right_x, baseline_y - 0.15, 0]),
                          np.array([right_x, baseline_y + 0.55, 0]),
                          color=GOLD, stroke_width=3)
        mean_l_lbl = Text("98 nm", font=MONO, color=INK, font_size=17)
        mean_r_lbl = Text("98 nm", font=MONO, color=INK, font_size=17)
        mean_l_lbl.next_to(left_mean,  UP, buff=0.1)
        mean_r_lbl.next_to(right_mean, UP, buff=0.1)
        # Headers
        left_hdr  = LabelChip("Batch A  PDI 0.07", accent=TEAL,    size=22)
        right_hdr = LabelChip("Batch B  PDI 0.31", accent=CRIMSON, size=22)
        left_hdr.move_to(np.array([left_x,  2.1, 0]))
        right_hdr.move_to(np.array([right_x, 2.1, 0]))
        # Delivery labels
        left_delivery  = SerifLabel("tumor delivery: 100%", TEAL,    size=22)
        right_delivery = SerifLabel("tumor delivery: ~60%", CRIMSON, size=22)
        left_delivery.move_to(np.array([left_x,  -2.2, 0]))
        right_delivery.move_to(np.array([right_x, -2.2, 0]))
        # ILLUSTRATIVE chip at bottom center
        illustrative = LabelChip("ILLUSTRATIVE", accent=SLATE, size=20)
        illustrative.move_to(DOWN * 2.9)
        # Animate
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.6)
        self.play(Create(left_axis), Create(right_axis), run_time=0.4)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in narrow_bars], lag_ratio=0.06, run_time=1.2),
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in wide_bars],   lag_ratio=0.06, run_time=1.2),
        )
        self.play(Create(left_mean), Create(right_mean), run_time=0.5)
        self.play(FadeIn(mean_l_lbl), FadeIn(mean_r_lbl), run_time=0.5)
        self.play(FadeIn(left_delivery), FadeIn(right_delivery), run_time=0.7)
        self.play(FadeIn(illustrative), run_time=0.5)
        self.wait(max(0.3, total - 4.4))


# ---------------------------------------------------------------- B12 Endcard

class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("A nanoparticle is a distribution,", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("not a molecule.", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.1))
