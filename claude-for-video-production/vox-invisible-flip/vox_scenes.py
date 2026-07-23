"""vox_scenes.py — Why an Invisible Change Can Flip a Million-Pixel Answer
(vox-invisible-flip, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-invisible-flip

HONESTY RULES (FACTCHECK.md): B06-B08 are ONE persistent machine — same
cells, same bar, same decision line; the fill climbs, never teleports. B07's
slivers are identical in size and direction (alignment IS the argument).
Numbers on screen: 57.7 and 99.3 only (both verified).
Color law: blue = panda side / human-visible truth; terracotta = the
perturbation and the flipped label.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene, MONO
import numpy as np

DUR = {"B01": 8.8, "B04": 9.6, "B05": 10.0, "B06": 9.6, "B07": 10.8,
       "B08": 9.6, "B09": 9.6, "B10": 9.6, "B11": 8.8}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------- the machine

N_CELLS = 12
_VALUES = [".62", ".13", ".88", ".41", ".07", ".95", ".33", ".76",
           ".22", ".58", ".49", ".84"]          # dressing, not data
_CELL_Y = 1.6
_TUBE = dict(x=4.6, yc=-0.5, h=3.2, w=0.7)
_LINE_FRAC = 0.62                                # decision line height


def _cell_x(i):
    return -5.7 + i * 0.66


def _cells():
    g = VGroup()
    for i in range(N_CELLS):
        box = Rectangle(width=0.58, height=0.5).set_fill(WHITE, 1)
        box.set_stroke("#D8D2C4", 1.5)
        box.move_to(np.array([_cell_x(i), _CELL_Y, 0]))
        t = Text(_VALUES[i], font=MONO, color=INK, font_size=20)
        t.move_to(box)
        g.add(VGroup(box, t))
    return g


def _weights():
    g = VGroup()
    for i in range(N_CELLS):
        box = Rectangle(width=0.44, height=0.32)
        box.set_fill(SLATE, 1).set_stroke(width=0)
        box.move_to(np.array([_cell_x(i), _CELL_Y - 0.62, 0]))
        t = Text("w", font=SERIF, color=WHITE, font_size=18, slant=ITALIC)
        t.move_to(box)
        g.add(VGroup(box, t))
    return g


def _tube():
    tube = Rectangle(width=_TUBE["w"], height=_TUBE["h"]).set_stroke(INK, 2)
    tube.move_to(np.array([_TUBE["x"], _TUBE["yc"], 0]))
    y_line = _TUBE["yc"] - _TUBE["h"] / 2 + _LINE_FRAC * _TUBE["h"]
    line = Line([_TUBE["x"] - 0.55, y_line, 0], [_TUBE["x"] + 0.55, y_line, 0],
                color=INK, stroke_width=2.5)
    lab = Text("decision line", font=SERIF, color=INK, font_size=22)
    lab.move_to(np.array([_TUBE["x"] - 2.0, y_line + 0.02, 0]))
    lab.align_to(np.array([_TUBE["x"] - 0.85, 0, 0]), RIGHT)
    title = SerifLabel("the sum", NAVY, size=24)
    title.next_to(tube, UP, buff=0.3)
    return VGroup(tube, line, lab, title)


def _fill(frac, color):
    h = max(0.05, _TUBE["h"] * frac)
    r = Rectangle(width=_TUBE["w"] - 0.1, height=h)
    r.set_fill(color, 1).set_stroke(width=0)
    r.move_to(np.array([_TUBE["x"], _TUBE["yc"] - _TUBE["h"] / 2 + 0.02, 0]),
              aligned_edge=DOWN)
    return r


def _label_chip(text, accent):
    c = LabelChip(text, accent=accent, size=26)
    c.move_to(np.array([_TUBE["x"], _TUBE["yc"] - _TUBE["h"] / 2 - 0.55, 0]))
    return c


def _arrows():
    g = VGroup()
    for i in range(N_CELLS):
        a = Line(np.array([_cell_x(i), _CELL_Y + 0.42, 0]),
                 np.array([_cell_x(i), _CELL_Y + 0.72, 0]),
                 color=TERRA, stroke_width=4)
        a.add_tip(tip_length=0.12, tip_width=0.12)
        g.add(a)
    return g


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("ADVERSARIAL EXAMPLES", font=SERIF, color=BLUE,
                   font_size=24)
        t1 = Text("Why an invisible change can flip", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("a million-pixel answer", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B04_Gibbon(Scene):
    def construct(self):
        _quote_scene(self, "gibbon — 99.3%",
                     "— the model, on the same panda (Goodfellow et al., 2014)",
                     None, "gibbon", DUR["B04"])


class B05_JustNumbers(Scene):
    def construct(self):
        total = DUR["B05"]
        title = SerifLabel("the image, as the model sees it", NAVY, size=28)
        title.to_edge(UP, buff=0.55)
        grid = VGroup()
        rng = np.random.default_rng(7)
        for r in range(6):
            for c in range(6):
                s = Square(0.34)
                s.set_fill(PALE_GREY := "#B9B2A4", float(rng.uniform(0.25, 0.9)))
                s.set_stroke(width=0)
                s.move_to(np.array([-4.3 + c * 0.38, -0.4 - r * 0.38, 0]))
                grid.add(s)
        cells = _cells()
        arrow = Line(np.array([-2.9, -1.3, 0]), np.array([-1.4, 0.9, 0]),
                     color=INK, stroke_width=2.5)
        arrow.add_tip(tip_length=0.16, tip_width=0.16)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(grid), run_time=1.0)
        self.play(Create(arrow), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in cells],
                              lag_ratio=0.06, run_time=1.9))
        self.wait(max(0.5, total - 4.1))


class B06_WeightedSum(Scene):
    def construct(self):
        total = DUR["B06"]
        cells = _cells()
        self.add(cells)
        weights = _weights()
        self.play(LaggedStart(*[FadeIn(w, shift=DOWN * 0.12) for w in weights],
                              lag_ratio=0.05, run_time=1.6))
        machine = _tube()
        self.play(Create(machine[0]), Create(machine[1]),
                  FadeIn(machine[2]), FadeIn(machine[3]), run_time=1.2)
        fill = _fill(0.35, BLUE)
        chip = _label_chip("panda", BLUE)
        self.play(FadeIn(fill), FadeIn(chip), run_time=0.8)
        self.wait(max(0.5, total - 3.6))


class B07_Slivers(Scene):
    def construct(self):
        total = DUR["B07"]
        cells = _cells()
        weights = _weights()
        machine = _tube()
        fill = _fill(0.35, BLUE)
        chip = _label_chip("panda", BLUE)
        self.add(cells, weights, machine, fill, chip)
        arrows = _arrows()
        # three waves of aligned slivers; the fill climbs with each —
        # continuous, never teleporting (honesty rule)
        levels = (0.43, 0.51, 0.58)
        chunks = (arrows[0:4], arrows[4:8], arrows[8:12])
        for chunk, lv in zip(chunks, levels):
            self.play(LaggedStart(*[FadeIn(a, shift=UP * 0.08) for a in chunk],
                                  lag_ratio=0.12, run_time=1.1),
                      Transform(fill, _fill(lv, TERRA)))
        self.wait(max(0.5, total - 3.3))


class B08_TheFlip(Scene):
    def construct(self):
        total = DUR["B08"]
        cells = _cells()
        weights = _weights()
        machine = _tube()
        fill = _fill(0.58, TERRA)
        chip = _label_chip("panda", BLUE)
        self.add(cells, weights, machine, fill, _arrows(), chip)
        self.play(Transform(fill, _fill(0.80, TERRA)), run_time=1.4)
        self.play(Transform(chip, _label_chip("gibbon", TERRA)), run_time=0.8)
        y_line = _TUBE["yc"] - _TUBE["h"] / 2 + _LINE_FRAC * _TUBE["h"]
        zone = Rectangle(width=1.7, height=1.0)
        zone.set_stroke(width=0).set_fill(opacity=0)
        zone.move_to(np.array([_TUBE["x"], y_line, 0]))
        ring = HandRing(zone, color=TERRA)   # the film's single ring
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 3.2))


class B09_NothingEverything(Scene):
    def construct(self):
        total = DUR["B09"]
        # left: one magnified cell with its single sliver
        box = Rectangle(width=1.7, height=1.4).set_fill(WHITE, 1)
        box.set_stroke("#D8D2C4", 2)
        box.move_to(np.array([-3.2, 0.5, 0]))
        val = Text(".62", font=MONO, color=INK, font_size=44)
        val.move_to(box)
        arr = Line(np.array([-3.2, 1.35, 0]), np.array([-3.2, 1.85, 0]),
                   color=TERRA, stroke_width=5)
        arr.add_tip(tip_length=0.15, tip_width=0.15)
        lab_l = SerifLabel("one pixel — nothing", INK, size=26)
        lab_l.move_to(np.array([-3.2, -1.5, 0]))
        # right: the climbed bar
        tube = Rectangle(width=0.7, height=3.0).set_stroke(INK, 2)
        tube.move_to(np.array([3.2, 0.3, 0]))
        fl = Rectangle(width=0.6, height=2.4)
        fl.set_fill(TERRA, 1).set_stroke(width=0)
        fl.move_to(np.array([3.2, 0.3 - 1.5 + 0.02, 0]), aligned_edge=DOWN)
        lab_r = SerifLabel("the sum — everything", TERRA, size=26)
        lab_r.move_to(np.array([3.2, -1.9, 0]))
        self.play(FadeIn(box), FadeIn(val), FadeIn(arr), FadeIn(lab_l),
                  run_time=1.2)
        self.play(Create(tube), FadeIn(fl), FadeIn(lab_r), run_time=1.2)
        self.wait(max(0.5, total - 2.4))


class B10_Flashlight(Scene):
    def construct(self):
        _quote_scene(self, "Not a bug — a flashlight.",
                     "— what adversarial examples reveal", None,
                     "flashlight", DUR["B10"])


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Right answer, wrong reasons —", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("until someone checks.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 8",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
