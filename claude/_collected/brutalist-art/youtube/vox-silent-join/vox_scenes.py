"""vox_scenes.py — Why the Missing-Values Check Ran Clean on a Broken Dataset
(vox-silent-join, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-silent-join

COUNTABLE-TRUE (FACTCHECK.md): 100 rows queue, 96 land, 4 fall (3 of the
subpopulation's 10, 1 of the majority's 90). The subpopulation is visible
from the queue onward. The fall is silent — no error marks. Fixed seed.
Color law: ink = majority rows; terracotta = the subpopulation; blue = the
model's ticks; gold = the editor's pen.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene, MONO
import numpy as np

DUR = {"B01": 8.4, "B03": 9.2, "B04": 9.2, "B05": 10.4, "B06": 10.0,
       "B07": 7.2, "B08": 9.6, "B09": 9.6, "B10": 9.2, "B11": 9.2}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------- the 100 rows

_rng = np.random.default_rng(100)
SUBPOP = sorted(_rng.choice(100, size=10, replace=False).tolist())
_sub_set = set(SUBPOP)
# 4 fall: 3 from the subpopulation, 1 from the majority (fixed choice)
FALL = sorted(SUBPOP[2:5] + [next(i for i in range(100)
                                   if i not in _sub_set)])
_fall_set = set(FALL)


def _bar(i, w=0.42, h=0.12):
    color = TERRA if i in _sub_set else INK
    b = Rectangle(width=w, height=h)
    b.set_fill(color, 0.85).set_stroke(width=0)
    return b


def _queue_pos(i):
    r, c = divmod(i, 20)
    return np.array([-5.2 + c * 0.55, 2.95 - r * 0.3, 0.0])


def _merged_pos(k):
    r, c = divmod(k, 16)
    return np.array([-4.1 + c * 0.55, -0.75 - r * 0.3, 0.0])


def _fall_pos(j):
    return np.array([4.55 + j * 0.42, -3.05 + (j % 2) * 0.12, 0.0])


def _funnel():
    return VGroup(Line([-3.2, 1.45, 0], [-0.7, 0.05, 0], color=INK,
                       stroke_width=2.5),
                  Line([3.2, 1.45, 0], [0.7, 0.05, 0], color=INK,
                       stroke_width=2.5))


def _join_end_state():
    """Everything B05 ends with: merged 96 + funnel + 4 fallen."""
    bars = VGroup()
    passers = [i for i in range(100) if i not in _fall_set]
    for k, i in enumerate(passers):
        b = _bar(i)
        b.move_to(_merged_pos(k))
        bars.add(b)
    fallen = VGroup()
    for j, i in enumerate(FALL):
        b = _bar(i)
        b.move_to(_fall_pos(j))
        fallen.add(b)
    return bars, _funnel(), fallen


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("DATA VALIDATION", font=SERIF, color=BLUE, font_size=24)
        t1 = Text("Why the missing-values check", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("ran clean on a broken dataset", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_CleanCheck(Scene):
    def construct(self):
        _quote_scene(self, "Missing values: none.",
                     "— the EDA report, technically true", None,
                     "none", DUR["B03"])


class B04_ThreeSystems(Scene):
    def construct(self):
        total = DUR["B04"]
        title = SerifLabel("assembled, not born", NAVY, size=28)
        title.to_edge(UP, buff=0.55)
        blocks = VGroup()
        for k, x in enumerate((-4.2, 0.0, 4.2)):
            tbl = VGroup(Rectangle(width=2.4, height=1.5)
                         .set_fill(WHITE, 1).set_stroke("#D8D2C4", 1.5))
            for r in range(3):
                tbl.add(Line([-0.95, 0.35 - r * 0.4, 0],
                             [0.95, 0.35 - r * 0.4, 0],
                             color="#C9C2B4", stroke_width=2.5))
            lab = SerifLabel(f"system {k + 1}", SLATE, size=22)
            lab.next_to(tbl[0], DOWN, buff=0.25)
            g = VGroup(tbl, lab)
            g.move_to(np.array([x, 1.5, 0]))
            blocks.add(g)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.15) for b in blocks],
                              lag_ratio=0.25, run_time=1.5))
        funnel = VGroup(Line([-2.6, -0.1, 0], [-0.6, -1.6, 0], color=INK,
                             stroke_width=2.5),
                        Line([2.6, -0.1, 0], [0.6, -1.6, 0], color=INK,
                             stroke_width=2.5))
        arrows = VGroup(*[Line(blocks[k].get_bottom() + DOWN * 0.15,
                               np.array([x * 0.45, -0.05, 0]),
                               color=INK, stroke_width=2)
                          for k, x in enumerate((-4.2, 0.0, 4.2))])
        self.play(Create(arrows), Create(funnel), run_time=1.1)
        chip = LabelChip("joined on a shared ID", accent=SLATE, size=24)
        chip.move_to(DOWN * 2.5)
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 3.8))


class B05_TheJoin(Scene):
    def construct(self):
        total = DUR["B05"]
        bars = VGroup(*[_bar(i) for i in range(100)])
        for i, b in enumerate(bars):
            b.move_to(_queue_pos(i))
        funnel = _funnel()
        self.play(FadeIn(bars), run_time=0.8)
        self.play(Create(funnel), run_time=0.7)
        moves = []
        k = 0
        for i in range(100):
            if i in _fall_set:
                j = FALL.index(i)
                moves.append(bars[i].animate.move_to(_fall_pos(j)))
            else:
                moves.append(bars[i].animate.move_to(_merged_pos(k)))
                k += 1
        self.play(LaggedStart(*moves, lag_ratio=0.006, run_time=3.4))
        chip = LabelChip("4% dropped — silently", accent=TERRA, size=24)
        chip.move_to(np.array([4.0, 1.9, 0]))
        self.play(FadeIn(chip, shift=DOWN * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 5.6))


class B06_NotEven(Scene):
    def construct(self):
        total = DUR["B06"]
        merged, funnel, fallen = _join_end_state()
        merged.set_opacity(0.22)
        funnel.set_opacity(0.22)
        self.add(merged, funnel, fallen)
        big = VGroup()
        for j, i in enumerate(FALL):
            b = _bar(i, w=1.5, h=0.42)
            b.move_to(np.array([-2.6 + j * 1.85, 0.5, 0.0]))
            big.add(b)
        self.play(LaggedStart(*[Transform(fallen[j], big[j])
                                for j in range(4)],
                              lag_ratio=0.15, run_time=1.6))
        chip = LabelChip("one subpopulation — 3 of its 10 rows, gone",
                         accent=TERRA, size=24)
        if chip.width > 6.4:
            chip.scale_to_fit_width(6.4)
        # below the ghosted merged grid (its lowest bar bottoms out ≈ -2.31;
        # at 0.22 opacity those thin bars read as strokes to the audit)
        chip.move_to(DOWN * 2.85)
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 2.4))


class B07_TrainedOnPresent(Scene):
    def construct(self):
        total = DUR["B07"]
        passers = [i for i in range(100) if i not in _fall_set]
        bars = VGroup()
        for k, i in enumerate(passers):
            b = _bar(i, w=0.34, h=0.12)
            r, c = divmod(k, 12)
            b.move_to(np.array([-5.1 + c * 0.46, 2.35 - r * 0.42, 0.0]))
            bars.add(b)
        box = Rectangle(width=2.4, height=1.4).set_stroke(INK, 2.5)
        box.move_to(np.array([3.4, 1.2, 0]))
        lab = Text("model", font=SERIF, color=INK, font_size=32, weight=BOLD)
        lab.move_to(box)
        title = SerifLabel("beautiful — on what it saw", BLUE, size=26)
        title.move_to(np.array([3.4, -0.6, 0]))
        if title.width > 4.6:
            title.scale_to_fit_width(4.6)
        self.add(bars, box, lab)
        self.play(FadeIn(title), run_time=0.5)
        ticks = VGroup(*[Dot(b.get_center(), radius=0.045, color=BLUE)
                         for b in bars])
        self.play(LaggedStart(*[FadeIn(t, scale=0.6) for t in ticks],
                              lag_ratio=0.008, run_time=2.6))
        self.wait(max(0.5, total - 3.1))


class B08_Deployed(Scene):
    def construct(self):
        total = DUR["B08"]
        title = SerifLabel("in production — the full population", NAVY,
                           size=26)
        title.to_edge(UP, buff=0.55)
        rows = VGroup()
        kinds = ["ink"] * 9 + ["terra"] * 3
        for k, kind in enumerate(kinds):
            b = Rectangle(width=1.5, height=0.2)
            b.set_fill(TERRA if kind == "terra" else INK, 0.85)
            b.set_stroke(width=0)
            b.move_to(np.array([-2.6, 2.25 - k * 0.44, 0.0]))
            rows.add(b)
        self.play(FadeIn(title), FadeIn(rows), run_time=0.9)
        marks = VGroup()
        anims = []
        for k in range(9):
            d = Dot(rows[k].get_center() + RIGHT * 1.35, radius=0.07,
                    color=BLUE)
            marks.add(d)
            anims.append(FadeIn(d, scale=0.6))
        self.play(LaggedStart(*anims, lag_ratio=0.1, run_time=1.6))
        strikes = VGroup()
        for k in range(9, 12):
            b = rows[k]
            s = VGroup(Line(b.get_corner(UL) + UL * 0.06,
                            b.get_corner(DR) + DR * 0.06,
                            color=TERRA, stroke_width=5),
                       Line(b.get_corner(UR) + UR * 0.06,
                            b.get_corner(DL) + DL * 0.06,
                            color=TERRA, stroke_width=5))
            for m in s:
                m._qc_intentional = True
            strikes.add(s)
        self.play(LaggedStart(*[FadeIn(s) for s in strikes],
                              lag_ratio=0.2, run_time=1.1))
        zone = Rectangle(width=3.4, height=1.7)
        zone.set_stroke(width=0).set_fill(opacity=0)
        zone.move_to(np.array([-2.6, 2.25 - 10 * 0.44, 0.0]))
        ring = HandRing(zone, color=TERRA)   # the film's single ring
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 4.6))


class B09_NeverThere(Scene):
    def construct(self):
        # no highlighter sweep: on a wrapped line this wide the gold bar's
        # edge reads as a stroke under the text and Gate B strikes it
        # (the fixture's Gossett card had the same failure)
        _quote_scene(self, "You cannot compute the missingness of rows "
                     "that never existed.",
                     "— why every check ran green", None,
                     None, DUR["B09"])


class B10_TheQuestion(Scene):
    def construct(self):
        total = DUR["B10"]
        q = Text("Why are there exactly N rows?", font=SERIF, color=INK,
                 font_size=46, weight=BOLD)
        q.move_to(UP * 1.9)
        u = Line(q.get_corner(DL) + DOWN * 0.14, q.get_corner(DR) + DOWN * 0.14,
                 color=BLUE, stroke_width=2)
        l1 = Text("expected   100", font=MONO, color=INK, font_size=36)
        l2 = Text("received    96", font=MONO, color=INK, font_size=36)
        l1.move_to(UP * 0.35)
        l2.move_to(DOWN * 0.45)
        gap = Text("4 rows — where?", font=SERIF, color=TERRA, font_size=34,
                   weight=BOLD)
        gap.move_to(DOWN * 1.7)
        self.play(FadeIn(q), Create(u), run_time=1.0)
        self.play(FadeIn(l1), run_time=0.6)
        self.play(FadeIn(l2), run_time=0.6)
        bar = Rectangle(width=0.1, height=gap.height + 0.24)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0)
        bar.align_to(gap, LEFT).align_to(gap, DOWN)
        bar.shift(DOWN * 0.04)
        bar._qc_intentional = True
        bar_full = Rectangle(width=gap.width + 0.24, height=gap.height + 0.24)
        bar_full.set_fill(GOLD, 0.55).set_stroke(width=0)
        bar_full.move_to(gap)
        bar_full._qc_intentional = True
        self.add(bar)
        gap.set_z_index(1)
        self.play(FadeIn(gap), Transform(bar, bar_full), run_time=0.9)
        self.wait(max(0.5, total - 3.1))


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Interrogate the row count", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("before the rows.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 5",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
