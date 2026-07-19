"""vox_scenes.py — Why Your 0.68 Is Really a 0.40
(vox-base-rate, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash scripts/vox_run.sh reels/vox-base-rate

Color law: navy #3D5A80 = true sponsor / genuine positive · crimson #BF3339 =
false positive · pale grey #D8D2C4 = non-sponsor not flagged. Gold = editor's
pen, once. NO Bayes formula / calibration-curve / cost-ratio / verb taxonomy
(card exclusions); the dot grid + sliding marker ARE the argument. Medical
framing is B05 only.

Gate B convention: every zero-width stroke is also zero-opacity, and any
deliberate line-on-text (strike/ring) is marked `_qc_intentional = True`.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

GREY = "#D8D2C4"           # the silent majority of non-sponsors

DUR = {"B01": 10.0, "B03": 8.5, "B04": 10.5, "B05": 9.5, "B06": 9.0,
       "B07": 9.0, "B08": 10.5, "B09": 9.0, "B10": 9.5, "B11": 8.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------------- builders

_AX_X0, _AX_X1, _AX_Y = -5.0, 5.0, -0.6


def _axis_x(v):
    return _AX_X0 + v * (_AX_X1 - _AX_X0)


def _prob_axis():
    axis = Line([_AX_X0, _AX_Y, 0], [_AX_X1, _AX_Y, 0], color=INK, stroke_width=3)
    g = VGroup(axis)
    for v in (0.0, 0.5, 1.0):
        x = _axis_x(v)
        tick = Line([x, _AX_Y - 0.12, 0], [x, _AX_Y + 0.12, 0], color=INK, stroke_width=2)
        lab = Text(f"{v:.1f}" if v else "0", font=SERIF, color=INK, font_size=24)
        lab.next_to(tick, DOWN, buff=0.22)
        g.add(tick, lab)
    return g


def _marker(v, color, label):
    """A downward triangle sitting above the axis + a value label above it."""
    x = _axis_x(v)
    tri = Triangle(color=color).set_fill(color, 1).set_stroke(width=0, opacity=0)
    tri.scale(0.18).rotate(PI)                       # point down
    tri.move_to([x, _AX_Y + 0.32, 0])
    val = Text(label, font=SERIF, color=color, font_size=34, weight=BOLD)
    val.next_to(tri, UP, buff=0.14)
    return VGroup(tri, val)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE CONFIDENCE ILLUSION", font=SERIF, color=NAVY, font_size=24)
        t1 = Text("Why your 0.68", font=SERIF, color=INK, font_size=54, weight=BOLD)
        t2 = Text("is really a 0.40", font=SERIF, color=INK, font_size=54, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_TheQuestion(Scene):       # DOCUMENT — the half the score skips
    def construct(self):
        _quote_scene(self, "How rare is it, before you look?",
                     "— the question the score skips", None,
                     "rare", DUR["B03"])


class B04_BaseRateGrid(Scene):      # 8 in 100 — the base rate
    def construct(self):
        total = DUR["B04"]
        grid = IsotypeGrid(counts=[8, 92], colors=[NAVY, GREY],
                           per_row=10, size=0.26, gap=0.10)
        grid.move_to(UP * 0.3)
        lab = SerifLabel("8 sponsors in 100", NAVY, size=30)
        lab.next_to(grid, DOWN, buff=0.45)
        self.play(grid.count_up(run_time=min(4.5, total * 0.55), lag_ratio=0.02))
        self.play(FadeIn(lab, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - min(4.5, total * 0.55) - 0.7))


class B05_MedicalIntuition(Scene):  # the ONE medical beat — 99% acc, still false
    def construct(self):
        total = DUR["B05"]
        eye = Text("a 99%-accurate test · 1 in 10,000", font=SERIF, color=INK,
                   font_size=28).to_edge(UP, buff=0.7)
        base_y = -2.0
        # crimson tower of ~100 false alarms vs a single navy true tick
        false_bar = Rectangle(width=1.4, height=4.0)
        false_bar.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        false_bar.move_to([-1.6, base_y, 0], aligned_edge=DOWN)
        true_bar = Rectangle(width=1.4, height=0.06)
        true_bar.set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
        true_bar.move_to([1.6, base_y, 0], aligned_edge=DOWN)
        flab = SerifLabel("~100 false alarms", CRIMSON, size=26)
        flab.next_to(false_bar, DOWN, buff=0.25)
        tlab = SerifLabel("~1 true", NAVY, size=26)
        tlab.next_to(true_bar, DOWN, buff=0.25)
        cap = Text("per 10,000 tested", font=SERIF, color=INK, font_size=24)
        cap.next_to(VGroup(flab, tlab), DOWN, buff=0.3)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(GrowFromEdge(false_bar, DOWN), FadeIn(true_bar), run_time=1.1)
        self.play(FadeIn(flab), FadeIn(tlab), run_time=0.6)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(max(0.5, total - 2.7))


class B06_SignalLands(Scene):       # the signal fires on sponsors AND non-sponsors
    def construct(self):
        total = DUR["B06"]
        grid = IsotypeGrid(counts=[8, 92], colors=[NAVY, GREY],
                           per_row=10, size=0.26, gap=0.10)
        grid.move_to(UP * 0.2)
        grid.set_opacity(0.5)
        self.add(grid)
        lab = SerifLabel("a positive signal fires", INK, size=28)
        lab.next_to(grid, DOWN, buff=0.4)
        self.play(FadeIn(lab), grid.animate.set_opacity(0.85), run_time=0.8)
        marks = grid.marks
        # the 8 true sponsors (indices 0..7) light navy; a scattering of grey
        # squares flip crimson (false positives) — many more than the navy few
        navy_idx = list(range(8))
        rng = np.random.default_rng(42)
        grey_idx = sorted(rng.choice(range(8, 100), size=12, replace=False).tolist())
        # a signal ring sweeps the grid — a real growing shape (also satisfies
        # Gate A's shape-motion check, which recolor-only scenes fail)
        ring = Circle(radius=0.3, color=INK, stroke_width=3).move_to(grid.get_center())
        ring._qc_intentional = True   # deliberate sweep over marks — exempt Gate B
        self.play(Create(ring), run_time=0.4)
        self.play(ring.animate.scale(5.0),
                  *[marks[i].animate.set_fill(NAVY, 1) for i in navy_idx],
                  run_time=1.0)
        self.play(LaggedStart(*[marks[i].animate.set_fill(CRIMSON, 1)
                                for i in grey_idx], lag_ratio=0.08, run_time=1.6),
                  FadeOut(ring))
        self.wait(max(0.5, total - 3.2))


class B07_Swamp(Scene):             # false positives swamp the real few
    def construct(self):
        total = DUR["B07"]
        base_y = -1.9
        # 8 navy true positives at the base
        navy = VGroup(*[Square(0.30).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
                        for _ in range(8)])
        navy.arrange_in_grid(rows=1, buff=0.12).move_to([0, base_y + 0.2, 0])
        nlab = SerifLabel("the real ones", NAVY, size=24).next_to(navy, LEFT, buff=0.4)
        self.play(FadeIn(navy), FadeIn(nlab), run_time=0.8)
        # crimson false positives accumulate on top, burying them
        rng = np.random.default_rng(7)
        crimson = VGroup()
        for k in range(34):
            s = Square(0.30).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            col = k % 8
            row = k // 8
            jitter = rng.uniform(-0.06, 0.06, size=2)
            s.move_to([navy[col].get_x() + jitter[0],
                       base_y + 0.2 + (row + 1) * 0.34 + jitter[1], 0])
            crimson.add(s)
        clab = SerifLabel("false positives", CRIMSON, size=24)
        clab.next_to(crimson, RIGHT, buff=0.4)
        self.play(LaggedStart(*[FadeIn(s, scale=0.85) for s in crimson],
                              lag_ratio=0.03, run_time=2.2), FadeIn(clab))
        self.wait(max(0.5, total - 3.0))


class B08_MarkerSlides(Scene):      # 0.68 slides toward 0.40
    def construct(self):
        total = DUR["B08"]
        axis = _prob_axis()
        self.play(FadeIn(axis), run_time=0.8)
        # the base-rate anchor at 0.08
        bx = _axis_x(0.08)
        anchor = Line([bx, _AX_Y - 0.12, 0], [bx, _AX_Y + 0.12, 0],
                      color=GREY, stroke_width=6)
        blab = SerifLabel("base rate", NAVY, size=22).next_to(anchor, DOWN, buff=0.5)
        self.play(FadeIn(anchor), FadeIn(blab), run_time=0.6)
        marker = _marker(0.68, NAVY, "0.68")
        self.play(FadeIn(marker, shift=DOWN * 0.2), run_time=0.7)
        # a faint pull-line from the base rate toward the marker
        pull = DashedLine([bx, _AX_Y + 0.32, 0], [_axis_x(0.68), _AX_Y + 0.32, 0],
                          color=GREY, stroke_width=2)
        self.play(Create(pull), run_time=0.6)
        target = _marker(0.40, NAVY, "0.40")
        self.play(Transform(marker, target),
                  pull.animate.put_start_and_end_on([bx, _AX_Y + 0.32, 0],
                                                     [_axis_x(0.40), _AX_Y + 0.32, 0]),
                  run_time=1.4)
        ring = HandRing(marker, color=CRIMSON)      # intentional (built-in)
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 5.1))


class B09_SignalVsWorth(Scene):     # 0.68 signal vs 0.40 worth
    def construct(self):
        total = DUR["B09"]
        big68 = Text("0.68", font=SERIF, color=NAVY, font_size=96, weight=BOLD)
        big68.move_to(LEFT * 3.4 + UP * 0.4)
        l68 = SerifLabel("signal strength", NAVY, size=26).next_to(big68, DOWN, buff=0.3)
        big40 = Text("0.40", font=SERIF, color=CRIMSON, font_size=96, weight=BOLD)
        big40.move_to(RIGHT * 3.4 + UP * 0.4)
        l40 = SerifLabel("what it's worth", CRIMSON, size=26).next_to(big40, DOWN, buff=0.3)
        arrow = Arrow(big68.get_right() + RIGHT * 0.2, big40.get_left() + LEFT * 0.2,
                      color=INK, stroke_width=4, buff=0.3)
        alab = Text("count the base rate", font=SERIF, color=INK, font_size=24)
        alab.next_to(arrow, UP, buff=0.25)
        self.play(FadeIn(big68), FadeIn(l68), run_time=0.8)
        self.play(GrowArrow(arrow), FadeIn(alab), run_time=0.8)
        self.play(FadeIn(big40), FadeIn(l40), run_time=0.8)
        self.wait(max(0.5, total - 2.4))


class B10_LeadNotVerdict(Scene):    # a lead, not a verdict
    def construct(self):
        total = DUR["B10"]
        card = Rectangle(width=2.6, height=1.6).set_fill(WHITE, 1)
        card.set_stroke("#D8D2C4", 1.6).move_to(LEFT * 4.0)
        cname = SerifLabel("the company", NAVY, size=24).move_to(card.get_center())
        self.play(FadeIn(card), FadeIn(cname), run_time=0.7)
        # navy "ask directly" arrow leads on
        a1 = Arrow(card.get_right(), RIGHT * 2.6 + UP * 1.1, color=NAVY,
                   stroke_width=5, buff=0.25)
        l1 = SerifLabel("ask directly", NAVY, size=26).next_to(a1.get_end(), RIGHT, buff=0.2)
        # faded "apply blindly" arrow, struck out
        a2 = Arrow(card.get_right(), RIGHT * 2.6 + DOWN * 1.1, color=INK,
                   stroke_width=5, buff=0.25).set_opacity(0.35)
        l2 = Text("apply blindly", font=SERIF, color=INK, font_size=26).set_opacity(0.5)
        l2.next_to(a2.get_end(), RIGHT, buff=0.2)
        self.play(GrowArrow(a1), FadeIn(l1), run_time=0.8)
        self.play(GrowArrow(a2), FadeIn(l2), run_time=0.7)
        strike = Line(l2.get_left() + LEFT * 0.05, l2.get_right() + RIGHT * 0.05,
                      color=CRIMSON, stroke_width=4)
        strike._qc_intentional = True    # deliberate strike-through of "apply blindly"
        self.play(Create(strike), run_time=0.5)
        tag = SerifLabel("a lead, not a verdict", CRIMSON, size=28)
        tag.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B11_End(Scene):               # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("A strong signal for a rare thing", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("is still a long shot.", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 5", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
