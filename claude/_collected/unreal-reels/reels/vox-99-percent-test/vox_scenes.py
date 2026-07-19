"""vox_scenes.py — Why a 99%-Accurate Test Is Almost Always Wrong When It
Says Yes (vox-99-percent-test, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-99-percent-test

COUNTABLE-TRUE LAW (FACTCHECK.md): exactly 10,000 marks, exactly 1 blue,
exactly 100 terracotta, exactly 101 in the pool. Freeze-frame counting must
match the narration. Fixed seed — renders are reproducible.
Color law: blue #5B7B9C = the true positive / truth; terracotta #D35F43 =
false alarms / noise.
NOTE: the crowd scenes (B04–B07, B11) build 10,000 mobjects — they render
slower than the others. That is expected.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 9.5, "B03": 8.5, "B04": 9.0, "B05": 6.5, "B06": 10.0,
       "B07": 8.5, "B08": 8.0, "B09": 9.5, "B10": 9.5, "B11": 8.5,
       "B12": 8.5}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ------------------------------------------------------------- the crowd

COLS, ROWS = 125, 80                 # 125 x 80 = 10,000 exactly
PALE = "#C9C2B4"
_X0, _X1 = -5.5, 5.5
_Y0, _Y1 = -2.55, 3.05               # keep clear of lower-third burn-in zone
BLUE_IDX = 31 * COLS + 47            # off-center, unremarkable — by design

_rng = np.random.default_rng(20260706)
_healthy = [i for i in range(COLS * ROWS) if i != BLUE_IDX]
FALSE_IDX = sorted(_rng.choice(_healthy, size=100, replace=False).tolist())


def _dot_pos(i):
    r, c = divmod(i, COLS)
    x = _X0 + c * (_X1 - _X0) / (COLS - 1)
    y = _Y1 - r * (_Y1 - _Y0) / (ROWS - 1)
    return np.array([x, y, 0.0])


def _crowd(state="plain"):
    """The 10,000. state: plain | one-blue | flagged (blue + 100 terra)."""
    dots = VGroup()
    for i in range(COLS * ROWS):
        d = Square(0.05)
        d.set_stroke(width=0)
        if state in ("one-blue", "flagged") and i == BLUE_IDX:
            d.set_fill(BLUE, 1)
        elif state == "flagged" and i in _FALSE_SET:
            d.set_fill(TERRA, 1)
        else:
            d.set_fill(PALE, 1)
        d.move_to(_dot_pos(i))
        dots.add(d)
    return dots


_FALSE_SET = set(FALSE_IDX)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("BASE RATES", font=SERIF, color=BLUE, font_size=24)
        t1 = Text("Why a 99% accurate test", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("is almost always wrong", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t3 = Text("when it says yes", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        u = Line(t3.get_corner(DL) + DOWN * 0.16, t3.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Commit(Scene):
    def construct(self):
        _quote_scene(self, "Pick a number. Lock it in.",
                     "— before the counting starts", None,
                     "Lock", DUR["B03"])


class B04_TheCrowd(Scene):
    def construct(self):
        total = DUR["B04"]
        title = SerifLabel("10,000 people — 1 is sick", NAVY, size=28)
        title.to_edge(DOWN, buff=0.35)
        dots = _crowd("plain")
        # reveal in 20 row-chunks (400 rows/chunk) — no per-dot animation
        chunks = [VGroup(*dots[k * 500:(k + 1) * 500]) for k in range(20)]
        self.play(LaggedStart(*[FadeIn(ch) for ch in chunks],
                              lag_ratio=0.06, run_time=2.4))
        self.play(FadeIn(title), run_time=0.5)
        one = dots[BLUE_IDX]
        big = Square(0.05).set_stroke(width=0).set_fill(BLUE, 1)
        big.move_to(_dot_pos(BLUE_IDX)).scale(3.0)
        small = Square(0.05).set_stroke(width=0).set_fill(BLUE, 1)
        small.move_to(_dot_pos(BLUE_IDX)).scale(1.6)
        self.play(Transform(one, big), run_time=0.6)   # the pulse
        self.play(Transform(one, small), run_time=0.5)
        self.wait(max(0.5, total - 4.0))


class B05_OneCaught(Scene):
    def construct(self):
        total = DUR["B05"]
        dots = _crowd("one-blue")
        dots[BLUE_IDX].scale(1.6)
        self.add(dots)
        scan = Line(UP * (_Y1 + 0.15), UP * (_Y0 - 0.15), color=INK,
                    stroke_width=2).move_to(np.array([_X0, 0.25, 0]),
                                            aligned_edge=UP)
        scan.set_opacity(0.6)
        self.add(scan)
        scan_end = Line(UP * (_Y1 + 0.15), UP * (_Y0 - 0.15), color=INK,
                        stroke_width=2).move_to(np.array([_X1, 0.25, 0]),
                                                aligned_edge=UP)
        scan_end.set_opacity(0.6)
        self.play(Transform(scan, scan_end), run_time=1.8)
        self.play(FadeOut(scan), run_time=0.3)
        chip = LabelChip("TRUE POSITIVE", accent=BLUE, size=22)
        chip.next_to(_dot_pos(BLUE_IDX), UR, buff=0.35)
        self.play(FadeIn(chip, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B06_FalseAlarms(Scene):
    def construct(self):
        total = DUR["B06"]
        dots = _crowd("one-blue")
        dots[BLUE_IDX].scale(1.6)
        chip = LabelChip("TRUE POSITIVE", accent=BLUE, size=22)
        chip.next_to(_dot_pos(BLUE_IDX), UR, buff=0.35)
        self.add(dots, chip)
        title = SerifLabel("~100 false alarms", TERRA, size=28)
        title.to_edge(DOWN, buff=0.35)
        wave = AnimationGroup(*[dots[i].animate.set_fill(TERRA, 1)
                                for i in FALSE_IDX],
                              lag_ratio=0.012, run_time=3.2)
        self.play(wave)
        self.play(FadeIn(title), run_time=0.5)
        self.wait(max(0.5, total - 3.7))


class B07_ThePool(Scene):
    def construct(self):
        total = DUR["B07"]
        dots = _crowd("flagged")
        dots[BLUE_IDX].scale(1.6)
        self.add(dots)
        flagged = [BLUE_IDX] + FALSE_IDX
        others = VGroup(*[dots[i] for i in range(COLS * ROWS)
                          if i not in _FALSE_SET and i != BLUE_IDX])
        self.play(others.animate.set_opacity(0.10), run_time=0.9)
        # the pool: 101 dots settle into tidy rows, blue IN-ROW (FACTCHECK:
        # nothing marks it out in real life — the color finds the eye)
        pool_targets = {}
        for k, i in enumerate(sorted(flagged)):
            r, c = divmod(k, 10)
            pool_targets[i] = np.array([3.15 + (c - 4.5) * 0.20,
                                        1.75 - r * 0.20, 0.0])
        bucket = Rectangle(width=2.5, height=2.9).set_stroke(INK, 2)
        bucket.move_to(np.array([3.15, 0.72, 0]))
        lab = SerifLabel("the positives — 101", NAVY, size=26)
        lab.next_to(bucket, DOWN, buff=0.35)
        self.play(Create(bucket), run_time=0.6)
        self.play(AnimationGroup(*[dots[i].animate.move_to(pool_targets[i])
                                   for i in sorted(flagged)],
                                 lag_ratio=0.004, run_time=2.4))
        self.play(FadeIn(lab), run_time=0.5)
        self.wait(max(0.5, total - 4.4))


class B08_OnePercent(Scene):
    def construct(self):
        total = DUR["B08"]
        num = Text("≈1%", font=SERIF, color=INK, font_size=160, weight=BOLD)
        num.move_to(UP * 0.7)
        line = Text("1 true positive among 101 positive results",
                    font=SERIF, color=INK, font_size=30)
        line.next_to(num, DOWN, buff=0.6)
        u = Line(line.get_corner(DL) + DOWN * 0.12,
                 line.get_corner(DR) + DOWN * 0.12,
                 color=TERRA, stroke_width=1.6)
        self.play(FadeIn(num, scale=0.95), run_time=0.9)
        self.play(FadeIn(line), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.8))


class B09_NothingBroken(Scene):
    def construct(self):
        total = DUR["B09"]
        left = SerifLabel("99% accurate", BLUE, size=44)
        left.move_to(LEFT * 3.1 + UP * 0.4)
        lsub = Text("what the box promised", font=SERIF, color=INK,
                    font_size=24)
        lsub.next_to(left, DOWN, buff=0.4)
        right = SerifLabel("≈1% sick", TERRA, size=44)
        right.move_to(RIGHT * 3.1 + UP * 0.4)
        rsub = Text("what the count shows", font=SERIF, color=INK,
                    font_size=24)
        rsub.next_to(right, DOWN, buff=0.4)
        self.play(FadeIn(left), FadeIn(lsub), run_time=0.8)
        self.play(FadeIn(right), FadeIn(rsub), run_time=0.8)
        # the film's single editor's-pen ring — on the GAP between them
        gap = Rectangle(width=2.1, height=1.5)
        gap.set_stroke(width=0).set_fill(opacity=0)
        gap.move_to(UP * 0.3)
        ring = HandRing(gap, color=TERRA)
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 2.6))


class B10_TwoQuestions(Scene):
    def construct(self):
        total = DUR["B10"]
        title = SerifLabel("two different questions", NAVY, size=28)
        title.to_edge(UP, buff=0.6)

        def qcard(xc, q1, q2, ans, color):
            card = Rectangle(width=4.6, height=3.4).set_fill(WHITE, 1)
            card.set_stroke("#D8D2C4", 1.5).move_to(np.array([xc, -0.3, 0]))
            l1 = Text(q1, font=SERIF, color=INK, font_size=27)
            l2 = Text(q2, font=SERIF, color=INK, font_size=27)
            for l in (l1, l2):
                if l.width > 4.0:
                    l.scale_to_fit_width(4.0)
            l1.move_to(np.array([xc, 0.75, 0]))
            l2.next_to(l1, DOWN, buff=0.12)
            n = Text(ans, font=SERIF, color=color, font_size=66, weight=BOLD)
            n.move_to(np.array([xc, -1.0, 0]))
            return card, VGroup(l1, l2), n

        lc, lq, ln = qcard(-3.0, "How often is the test", "right about the sick?",
                           "99%", BLUE)
        rc, rq, rn = qcard(3.0, "How often is a positive", "actually sick?",
                           "≈1%", TERRA)
        self.play(FadeIn(title), FadeIn(lc), FadeIn(rc), run_time=0.8)
        self.play(FadeIn(lq), run_time=0.6)
        self.play(FadeIn(ln, scale=0.9), run_time=0.6)
        self.play(FadeIn(rq), run_time=0.6)
        self.play(FadeIn(rn, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 3.2))


class B11_TheBaseRate(Scene):
    def construct(self):
        total = DUR["B11"]
        dots = _crowd("one-blue")
        for i, d in enumerate(dots):
            if i != BLUE_IDX:
                d.set_opacity(0.10)
        dots[BLUE_IDX].scale(1.6)
        self.play(FadeIn(dots), run_time=1.0)
        chip = LabelChip("1 in 10,000 — the base rate", accent=SLATE, size=32)
        if chip.width > 6.5:
            chip.scale_to_fit_width(6.5)
        chip.move_to(DOWN * 0.1)
        self.play(FadeIn(chip, scale=0.95), run_time=0.8)
        self.wait(max(0.5, total - 1.8))


class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        t1 = Text("The test is honest.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("Your intuition forgot the prior.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 2",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
