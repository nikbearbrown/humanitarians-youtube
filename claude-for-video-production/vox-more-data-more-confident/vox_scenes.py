"""vox_scenes.py — Why More Data Makes the Wrong Answer More Confident
(vox-more-data-more-confident, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-more-data-more-confident

HONESTY RULES (FACTCHECK.md): B06 and B08 share the same wave schedule — the
only difference between the honest poll and the Digest is the aim-point. The
truth dot never moves. Scatter is real seeded Gaussian, not hand-placed.
Color law: blue #5B7B9C = the truth; terracotta #D35F43 = the biased cluster;
ink = unbiased darts.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene, MONO
import numpy as np

DUR = {"B01": 9.2, "B04": 10.4, "B05": 9.6, "B06": 9.2, "B07": 8.8,
       "B08": 10.4, "B09": 9.6, "B10": 9.6, "B11": 8.4}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ------------------------------------------------------------ shared geometry

TRUTH = np.array([-0.9, 0.15, 0.0])
OFFSET = np.array([2.1, -0.55, 0.0])
# ONE wave schedule for B06 and B08 (the honesty rule): (spread, count)
WAVES = [(1.5, 12), (0.9, 14), (0.5, 16)]


def _rings(center, radii=(1.0, 2.0)):
    g = VGroup(*[Circle(radius=r).set_stroke(INK, 1.5).set_fill(opacity=0)
                 .move_to(center) for r in radii])
    return g


def _truth_dot(labeled=True):
    d = Dot(TRUTH, radius=0.10, color=BLUE)
    if not labeled:
        return VGroup(d)
    lab = SerifLabel("the truth", BLUE, size=24)
    # below the whole target, clear of both rings (outer r=2.0; the label's
    # nearest edge sits ~2.45 from center) — never on a ring stroke
    lab.move_to(TRUTH + DOWN * 2.45)
    return VGroup(d, lab)


def _darts(center, spread, n, color, rng):
    pts = rng.normal(0.0, spread, size=(n, 2))
    g = VGroup()
    for dx, dy in pts:
        x = float(np.clip(center[0] + dx, -5.8, 5.8))
        y = float(np.clip(center[1] + dy * 0.75, -2.55, 3.05))
        g.add(Dot(np.array([x, y, 0.0]), radius=0.055, color=color))
    return g


def _crosshair(center, color):
    return VGroup(Line(center + LEFT * 0.28, center + RIGHT * 0.28,
                       color=color, stroke_width=3),
                  Line(center + UP * 0.28, center + DOWN * 0.28,
                       color=color, stroke_width=3))


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("BIAS IS NOT NOISE", font=SERIF, color=BLUE, font_size=24)
        t1 = Text("Why more data makes", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("the wrong answer more confident", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        if t2.width > 12.0:
            t2.scale_to_fit_width(12.0)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B04_CantLie(Scene):
    def construct(self):
        _quote_scene(self, "A sample that big can't lie.",
                     "— the instinct this story breaks", None,
                     "can't", DUR["B04"])


class B05_TheTarget(Scene):
    def construct(self):
        total = DUR["B05"]
        rings = _rings(TRUTH)
        truth = _truth_dot()
        self.play(Create(rings), run_time=1.2)
        self.play(FadeIn(truth), run_time=0.7)
        rng = np.random.default_rng(1936)
        first = _darts(TRUTH, 1.2, 3, INK, rng)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in first],
                              lag_ratio=0.35, run_time=1.5))
        self.wait(max(0.5, total - 3.4))


class B06_UnbiasedTightens(Scene):
    def construct(self):
        total = DUR["B06"]
        self.add(_rings(TRUTH), _truth_dot())
        lab = SerifLabel("unbiased: the scatter shrinks around the truth",
                         NAVY, size=26)
        if lab.width > 10.5:
            lab.scale_to_fit_width(10.5)
        lab.to_edge(UP, buff=0.55)
        self.play(FadeIn(lab), run_time=0.6)
        rng = np.random.default_rng(1936)
        for spread, n in WAVES:                # THE shared schedule
            wave = _darts(TRUTH, spread, n, INK, rng)
            self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in wave],
                                  lag_ratio=0.05, run_time=1.7))
        self.wait(max(0.5, total - 0.6 - 3 * 1.7))


class B07_BadAim(Scene):
    def construct(self):
        total = DUR["B07"]
        self.add(_rings(TRUTH), _truth_dot())
        ch = _crosshair(TRUTH, TERRA)
        self.play(FadeIn(ch), run_time=0.6)
        ch_target = _crosshair(OFFSET, TERRA)
        self.play(Transform(ch, ch_target), run_time=1.4)
        chip = LabelChip("who got ballots: car & telephone owners",
                         accent=TERRA, size=24)
        if chip.width > 5.6:
            chip.scale_to_fit_width(5.6)
        chip.to_corner(DL, buff=0.55)
        chip.shift(RIGHT * 0.3)
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 2.7))


class B08_TightenWrong(Scene):
    def construct(self):
        total = DUR["B08"]
        self.add(_rings(TRUTH), _truth_dot())
        ch = _crosshair(OFFSET, TERRA)
        ch.set_opacity(0.45)
        self.add(ch)
        counter = Text("n = 100", font=MONO, color=INK, font_size=34)
        counter.to_corner(DR, buff=0.6)
        self.play(FadeIn(counter), run_time=0.4)
        rng = np.random.default_rng(1936)
        labels = ("n = 100", "n = 10,000", "n = 2,400,000")
        for (spread, n), ntext in zip(WAVES, labels):   # SAME schedule as B06
            wave = _darts(OFFSET, spread, n, TERRA, rng)
            nxt = Text(ntext, font=MONO, color=INK, font_size=34)
            nxt.to_corner(DR, buff=0.6)
            self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in wave],
                                  lag_ratio=0.05, run_time=1.7),
                      Transform(counter, nxt))
        self.wait(max(0.5, total - 0.4 - 3 * 1.7))


class B09_TheGap(Scene):
    def construct(self):
        total = DUR["B09"]
        self.add(_rings(TRUTH), _truth_dot())
        rng = np.random.default_rng(1936)
        cluster = _darts(OFFSET, 0.42, 60, TERRA, rng)
        self.add(cluster)
        direction = (OFFSET - TRUTH) / np.linalg.norm(OFFSET - TRUTH)
        a = TRUTH + direction * 0.22
        b = OFFSET - direction * 0.22
        gap_line = Line(a, b, color=INK, stroke_width=2.5)
        gap_line.set_opacity(0.8)
        self.play(Create(gap_line), run_time=0.9)
        lab = SerifLabel("the bias", TERRA, size=34)   # the ONE label
        # up-right of the gap: clear of the inner ring (r=1.0), the outer
        # ring (r=2.0, whose arc crosses y≈1.5-2.1 in this x-range), and the
        # gap line (which stays below y=0.15)
        lab.move_to(np.array([1.35, 1.95, 0.0]))
        self.play(FadeIn(lab, shift=DOWN * 0.1), run_time=0.7)
        zone = Rectangle(width=float(np.linalg.norm(b - a)) + 0.6, height=1.1)
        zone.set_stroke(width=0).set_fill(opacity=0)
        zone.move_to((a + b) / 2)
        ring = HandRing(zone, color=TERRA)             # the ONE ring
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 2.6))


class B10_PreciselyWrong(Scene):
    def construct(self):
        total = DUR["B10"]
        L = np.array([-3.0, -0.05, 0.0])
        R = np.array([3.0, -0.05, 0.0])
        rng = np.random.default_rng(1936)
        left_rings = _rings(L, radii=(0.8, 1.6))
        right_rings = _rings(R, radii=(0.8, 1.6))
        ld = Dot(L, radius=0.09, color=BLUE)
        rd = Dot(R, radius=0.09, color=BLUE)
        self.play(Create(left_rings), Create(right_rings),
                  FadeIn(ld), FadeIn(rd), run_time=1.1)
        tight = _darts(L + np.array([0.95, 0.55, 0.0]), 0.22, 20, TERRA, rng)
        loose = _darts(R, 0.65, 20, INK, rng)
        lab_l = SerifLabel("precisely wrong", TERRA, size=28)
        lab_l.move_to(L + DOWN * 2.35)
        lab_r = SerifLabel("roughly right", BLUE, size=28)
        lab_r.move_to(R + DOWN * 2.35)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in tight],
                              lag_ratio=0.04, run_time=1.4),
                  FadeIn(lab_l))
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in loose],
                              lag_ratio=0.04, run_time=1.4),
                  FadeIn(lab_r))
        self.wait(max(0.5, total - 3.9))


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Scale buys precision —", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("never correction.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 3",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
