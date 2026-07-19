"""vox_scenes.py — Why the Turkey's Model Was Perfect Until Thanksgiving
(vox-turkey-problem, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-turkey-problem

Device: one curve. Terracotta = confidence, the model's picture built from its
data; dusty blue = the world's actual risk. The confidence curve is monotone
by construction (never one bad day is the claim), zero-baseline axes, the
cliff is DRAWN as an event (never a fade). Labels float clear of every stroke
(Gate B rule). One ring: B05, on the confidence peak. No gold sweeps this
film — both quotes wrap (Gate B lesson).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 8.0, "B03": 10.0, "B04": 10.0, "B05": 9.5, "B06": 9.5,
       "B07": 9.0, "B08": 10.0, "B09": 10.0, "B10": 9.0, "B11": 8.4}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# --------------------------------------------------------------- the curve

_OX, _OY = -5.4, -2.4          # axes origin (zero baseline)
_XMAX, _YMAX = 5.3, 2.4        # axes extents
_PEAK_X = 3.9                  # day 1,000 lands here; 1,001 lives past it


def _conf_y(t, top=1.9):
    """Monotone, saturating confidence height for t in [0,1]."""
    frac = 0.25 * t + 0.75 * (1.0 - np.exp(-3.0 * t))
    return _OY + (top - _OY) * frac


def _axes():
    x = Line([_OX, _OY, 0], [_XMAX, _OY, 0], color=INK, stroke_width=2.5)
    y = Line([_OX, _OY, 0], [_OX, _YMAX, 0], color=INK, stroke_width=2.5)
    d1 = Text("day 1", font=SERIF, color=INK, font_size=22)
    d1.move_to(np.array([-5.0, _OY - 0.42, 0]))
    d1000 = Text("day 1,000", font=SERIF, color=INK, font_size=22)
    d1000.move_to(np.array([_PEAK_X, _OY - 0.42, 0]))
    return VGroup(x, y, d1, d1000)


def _conf_curve(x_end=_PEAK_X, top=1.9):
    c = VMobject(color=TERRA, stroke_width=5)
    ts = np.linspace(0.0, 1.0, 48)
    c.set_points_smoothly([np.array([_OX + (x_end - _OX) * t,
                                     _conf_y(t, top), 0]) for t in ts])
    return c


def _peak_point(top=1.9):
    return np.array([_PEAK_X, _conf_y(1.0, top), 0])


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE LIMITS OF AI", font=SERIF, color=BLUE, font_size=24)
        t1 = Text("The turkey's model was perfect —", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("until Thanksgiving", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        if t1.width > 12.0:
            t1.scale_to_fit_width(12.0)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_FeedingDays(Scene):
    def construct(self):
        total = DUR["B03"]
        model = LabelChip("the model: the human cares about my welfare",
                          accent=TERRA, size=26)
        if model.width > 9.5:
            model.scale_to_fit_width(9.5)
        model.to_edge(UP, buff=0.55)
        grid = IsotypeGrid([100], [TERRA], per_row=10, size=0.22, gap=0.12)
        grid.move_to(np.array([-2.6, -0.55, 0]))
        unit = Text("■ = 10 mornings", font=SERIF, color=INK,
                    font_size=24)
        unit.move_to(np.array([2.9, 0.75, 0]))
        count = Text("1,000 mornings", font=MONO, color=TERRA,
                     font_size=44, weight=BOLD)
        count.move_to(np.array([2.9, -0.65, 0]))
        sub = Text("no exceptions on record", font=SERIF, color=INK,
                   font_size=24, slant=ITALIC)
        sub.move_to(np.array([2.9, -1.5, 0]))
        self.play(FadeIn(model, shift=DOWN * 0.12), run_time=0.8)
        self.play(FadeIn(unit), run_time=0.5)
        self.play(grid.count_up(run_time=min(4.5, total * 0.45)))
        self.play(FadeIn(count, scale=0.92), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(max(0.5, total - 2.5 - min(4.5, total * 0.45)))


class B04_ConfidenceCurve(Scene):
    def construct(self):
        total = DUR["B04"]
        title = SerifLabel("confidence, day 1 to day 1,000", TERRA, size=28)
        title.to_edge(UP, buff=0.55)
        ax = _axes()
        curve = _conf_curve()
        lab = SerifLabel("more evidence, more confidence", TERRA, size=24)
        lab.move_to(np.array([1.6, -1.2, 0]))     # clear below the curve
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(ax[0]), Create(ax[1]), FadeIn(ax[2]), FadeIn(ax[3]),
                  run_time=1.2)
        self.play(Create(curve), run_time=min(3.8, total * 0.4),
                  rate_func=linear)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 2.3 - min(3.8, total * 0.4)))


class B05_DayThousand(Scene):
    def construct(self):
        total = DUR["B05"]
        title = SerifLabel("confidence, day 1 to day 1,000", TERRA, size=28)
        title.to_edge(UP, buff=0.55)
        self.add(title, _axes(), _conf_curve())
        zone = Square(0.95).set_stroke(width=0).set_fill(opacity=0)
        zone.move_to(_peak_point())
        ring = HandRing(zone, color=TERRA)      # the film's single ring
        chip = LabelChip("day 1,000 — the day before Thanksgiving",
                         accent=TERRA, size=26)
        if chip.width > 6.4:
            chip.scale_to_fit_width(6.4)
        chip.move_to(np.array([0.9, -1.3, 0]))  # clear below the curve
        self.play(Create(ring), run_time=1.2)
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 2.0))


class B06_TheCliff(Scene):
    def construct(self):
        total = DUR["B06"]
        title = SerifLabel("confidence, day 1 to day 1,000", TERRA, size=28)
        title.to_edge(UP, buff=0.55)
        peak = _peak_point()
        self.add(title, _axes(), _conf_curve())
        ext = Line(peak, np.array([4.35, peak[1] + 0.05, 0]),
                   color=TERRA, stroke_width=5)
        drop = Line(np.array([4.35, peak[1] + 0.05, 0]),
                    np.array([4.35, _OY + 0.04, 0]),
                    color=TERRA, stroke_width=6)
        box = Rectangle(width=1.55, height=0.62).set_fill(WHITE, 1)
        box.set_stroke("#D8D2C4", 1.5)
        box.move_to(np.array([5.7, 0.35, 0]))
        lab = Text("day 1,001", font=SERIF, color=INK, font_size=24)
        lab.move_to(box)
        tick = Line(np.array([4.43, 0.35, 0]),
                    np.array([box.get_left()[0], 0.35, 0]),
                    color=INK, stroke_width=2)
        self.play(Create(ext), run_time=0.8)
        self.play(Create(drop), run_time=0.5)     # drawn fast — an event
        self.play(Create(tick), FadeIn(box), FadeIn(lab), run_time=0.8)
        self.wait(max(0.5, total - 2.1))


class B07_SafetyQuote(Scene):
    def construct(self):
        _quote_scene(self,
                     "the feeling of safety reached its maximum "
                     "when the risk was at the highest",
                     "— Nassim Nicholas Taleb, The Black Swan (2007)",
                     None, None, DUR["B07"])


class B08_RoutineCases(Scene):
    def construct(self):
        total = DUR["B08"]
        title = SerifLabel("ten thousand routine cases", BLUE, size=28)
        title.to_edge(UP, buff=0.55)
        grid = IsotypeGrid([100], [BLUE], per_row=10, size=0.22, gap=0.12)
        grid.move_to(np.array([-2.6, -0.55, 0]))
        frame = SurroundingRectangle(grid, buff=0.28)
        frame.set_stroke(INK, 2).set_fill(opacity=0)
        dlab = Text("the data", font=SERIF, color=INK, font_size=22)
        dlab.next_to(frame, UP, buff=0.18).align_to(frame, LEFT)
        unit = Text("■ = 100 cases", font=SERIF, color=INK, font_size=24)
        unit.move_to(np.array([3.0, 1.15, 0]))
        chip = LabelChip("99.7% accurate", accent=BLUE, size=28)
        chip.move_to(np.array([3.0, 0.25, 0]))
        slot = DashedVMobject(Square(0.55).set_stroke(TERRA, 3),
                              num_dashes=16)
        slot.move_to(np.array([3.0, -1.05, 0]))
        s1 = Text("the case that ends the regime", font=SERIF, color=TERRA,
                  font_size=22)
        s2 = Text("— not in the data", font=SERIF, color=TERRA, font_size=22)
        slab = VGroup(s1, s2).arrange(DOWN, buff=0.1)
        slab.move_to(np.array([3.0, -2.15, 0]))
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(frame), FadeIn(dlab), FadeIn(unit), run_time=1.0)
        self.play(grid.count_up(run_time=min(3.2, total * 0.32)))
        self.play(FadeIn(chip, scale=0.92), run_time=0.7)
        self.play(Create(slot), FadeIn(slab), run_time=1.0)
        self.wait(max(0.5, total - 3.2 - min(3.2, total * 0.32)))


class B09_TheGap(Scene):
    def construct(self):
        total = DUR["B09"]
        ax = _axes()
        risk = Line([_OX, 2.0, 0], [_XMAX, 2.0, 0], color=BLUE,
                    stroke_width=5)
        rlab = SerifLabel("the world's risk — never moved", BLUE, size=24)
        rlab.move_to(np.array([0.0, 2.65, 0]))    # clear above the line
        curve = _conf_curve(x_end=_XMAX, top=1.45)
        clab = SerifLabel("confidence — climbing", TERRA, size=24)
        clab.move_to(np.array([2.4, -0.9, 0]))    # clear below the curve
        self.play(Create(ax[0]), Create(ax[1]), FadeIn(ax[2]), run_time=1.0)
        self.play(Create(risk), FadeIn(rlab), run_time=1.2)
        self.play(Create(curve), run_time=min(3.4, total * 0.35),
                  rate_func=linear)
        self.play(FadeIn(clab), run_time=0.6)
        self.wait(max(0.5, total - 2.8 - min(3.4, total * 0.35)))


class B10_CompetenceQuote(Scene):
    def construct(self):
        _quote_scene(self,
                     "The system's competence is over the data, "
                     "not the world.",
                     "— Computational Skepticism for AI, chapter 14",
                     None, None, DUR["B10"])


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("The data is always less", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("than the world.", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 14",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
