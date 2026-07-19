"""vox_scenes.py — Why Deleting the Cheapest Job Destroys the Most Expensive One
(vox-bottom-rung, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash scripts/vox_run.sh reels/vox-bottom-rung

Color law: navy #3D5A80 = the pipeline / climbers / judgment being built ·
crimson #BF3339 = the cut rung / the drain / the empty platform. Gold = editor's
pen, once. Hero: a career ladder losing its bottom rung while the senior platform
drains. NO wage-premium stats, NO 90%-musician inversion, NO extra IBM detail,
NO policy (card exclusions).

Gate A/B conventions: zero-width strokes are also zero-opacity; deliberate
line-on-text (ring, break-X) is marked `_qc_intentional = True`; every `.animate`
uses a SINGLE method (the static checker's mock rejects chains).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 11.0, "B03": 10.0, "B04": 8.5, "B05": 10.0, "B06": 10.5,
       "B07": 10.5, "B08": 10.0, "B09": 10.5, "B10": 10.0, "B11": 7.5}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

LX, RX = -0.7, 0.7
RUNG_YS = list(np.linspace(-2.0, 1.2, 5))
PLAT_Y = 1.7


# ---------------------------------------------------------------- builders

def _rails(color=NAVY):
    return VGroup(Line([LX, -2.4, 0], [LX, 1.4, 0], color=color, stroke_width=4),
                  Line([RX, -2.4, 0], [RX, 1.4, 0], color=color, stroke_width=4))


def _rung(y, color=NAVY):
    return Line([LX, y, 0], [RX, y, 0], color=color, stroke_width=4)


def _rungs(include_bottom=True, color=NAVY):
    g = VGroup()
    for i, y in enumerate(RUNG_YS):
        if i == 0 and not include_bottom:
            continue
        g.add(_rung(y, color))
    return g


def _platform(color=NAVY):
    return Line([-1.6, PLAT_Y, 0], [1.6, PLAT_Y, 0], color=color, stroke_width=6)


def _stick(cx, cy, color):
    head = Circle(radius=0.13).set_stroke(color, 3).set_fill(WHITE, 0).move_to([cx, cy + 0.4, 0])
    body = Line([cx, cy + 0.27, 0], [cx, cy - 0.1, 0], color=color, stroke_width=3)
    arms = Line([cx - 0.17, cy + 0.12, 0], [cx + 0.17, cy + 0.12, 0], color=color, stroke_width=3)
    legL = Line([cx, cy - 0.1, 0], [cx - 0.14, cy - 0.4, 0], color=color, stroke_width=3)
    legR = Line([cx, cy - 0.1, 0], [cx + 0.14, cy - 0.4, 0], color=color, stroke_width=3)
    return VGroup(head, body, arms, legL, legR)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE RUNG THAT GOT REMOVED", font=SERIF, color=NAVY, font_size=22)
        t1 = Text("Delete the cheapest job,", font=SERIF, color=INK, font_size=48, weight=BOLD)
        t2 = Text("destroy the most expensive one", font=SERIF, color=INK, font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_TheLadder(Scene):         # the ladder to judgment
    def construct(self):
        total = DUR["B03"]
        rails, rungs, plat = _rails(), _rungs(True), _platform()
        seniors = VGroup(_stick(-0.6, 2.1, NAVY), _stick(0.6, 2.1, NAVY))
        toplab = SerifLabel("senior judgment", NAVY, size=24).move_to([0, 3.05, 0])
        botlab = SerifLabel("junior work", NAVY, size=22).move_to([0, -2.75, 0])
        climbers = VGroup(_stick(0.0, RUNG_YS[0] + 0.42, NAVY),
                          _stick(0.0, RUNG_YS[1] + 0.42, NAVY))
        self.play(Create(rails), run_time=0.7)
        self.play(LaggedStart(*[Create(r) for r in rungs], lag_ratio=0.15), run_time=1.2)
        self.play(Create(plat), FadeIn(seniors), FadeIn(toplab), run_time=0.9)
        self.play(FadeIn(climbers), FadeIn(botlab), run_time=0.8)
        self.wait(max(0.5, total - 3.6))


class B04_Apprenticeship(Scene):    # DOCUMENT — the grunt work was the apprenticeship
    def construct(self):
        _quote_scene(self, "The grunt work was the apprenticeship.",
                     "— how senior judgment got made", None,
                     "apprenticeship", DUR["B04"])


class B05_SameRung(Scene):          # AI-does-best rung == learning rung
    def construct(self):
        total = DUR["B05"]
        rails, rungs, plat = _rails(), _rungs(True), _platform()
        rails.set_opacity(0.4)
        rungs.set_opacity(0.4)
        plat.set_opacity(0.4)
        bottom = _rung(RUNG_YS[0], NAVY)                    # keep the bottom rung bright
        self.play(FadeIn(rails), FadeIn(rungs), FadeIn(plat), Create(bottom), run_time=1.0)
        left = SerifLabel("where judgment is learned", NAVY, size=22).move_to([-3.6, RUNG_YS[0] + 0.5, 0])
        right = SerifLabel("what AI does best", CRIMSON, size=22).move_to([3.4, RUNG_YS[0] - 0.5, 0])
        aL = Arrow(left.get_bottom(), [LX - 0.1, RUNG_YS[0], 0], color=NAVY, stroke_width=4, buff=0.15)
        aR = Arrow(right.get_top(), [RX + 0.1, RUNG_YS[0], 0], color=CRIMSON, stroke_width=4, buff=0.15)
        self.play(FadeIn(left), GrowArrow(aL), run_time=0.8)
        self.play(FadeIn(right), GrowArrow(aR), run_time=0.8)
        ring = HandRing(bottom, color=CRIMSON)              # intentional (built-in)
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 3.6))


class B06_CutAndDrain(Scene):       # cut the rung → the platform drains
    def construct(self):
        total = DUR["B06"]
        rails, rungs, plat = _rails(), _rungs(False), _platform()
        seniors = VGroup(_stick(-0.7, 2.1, NAVY), _stick(0.0, 2.1, NAVY), _stick(0.7, 2.1, NAVY))
        gap = DashedLine([LX, RUNG_YS[0], 0], [RX, RUNG_YS[0], 0], color=CRIMSON, stroke_width=4)
        gap._qc_intentional = True
        climber = _stick(-1.7, -1.9, NAVY)                 # stalled beside the gap
        stall = LabelChip("can't board", accent=CRIMSON, size=18).next_to(climber, DOWN, buff=0.15)
        self.play(FadeIn(rails), FadeIn(rungs), FadeIn(plat), FadeIn(seniors), run_time=0.9)
        self.play(Create(gap), FadeIn(climber), FadeIn(stall), run_time=0.9)
        drain = Arrow([2.0, 1.9, 0], [2.0, 0.6, 0], color=CRIMSON, stroke_width=5, buff=0.1)
        dlab = SerifLabel("draining", CRIMSON, size=22).next_to(drain, RIGHT, buff=0.2)
        self.play(GrowArrow(drain), FadeIn(dlab), run_time=0.6)
        self.play(LaggedStart(*[FadeOut(s) for s in seniors], lag_ratio=0.35), run_time=1.6)
        self.wait(max(0.5, total - 4.0))


class B07_TheDelay(Scene):          # the cut is fast, the gap is slow
    def construct(self):
        total = DUR["B07"]
        axis = Line([-5.2, -0.4, 0], [5.2, -0.4, 0], color=INK, stroke_width=3)
        t1 = Line([-3.4, -0.55, 0], [-3.4, -0.25, 0], color=INK, stroke_width=2)
        t2 = Line([3.6, -0.55, 0], [3.6, -0.25, 0], color=INK, stroke_width=2)
        l1 = SerifLabel("this quarter", INK, size=22).next_to(t1, DOWN, buff=0.25)
        l2 = SerifLabel("3-5 years", INK, size=22).next_to(t2, DOWN, buff=0.25)
        save = LabelChip("savings", accent=CRIMSON, size=22).move_to([-3.4, 0.7, 0])
        gone = LabelChip("no seniors", accent=CRIMSON, size=22).move_to([3.6, 0.7, 0])
        self.play(Create(axis), FadeIn(t1), FadeIn(t2), FadeIn(l1), FadeIn(l2), run_time=0.9)
        self.play(FadeIn(save, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(gone, shift=DOWN * 0.2), run_time=0.6)
        link = DashedLine([-2.6, 0.7, 0], [2.8, 0.7, 0], color=INK, stroke_width=2)
        self.play(Create(link), run_time=0.7)
        breakx = VGroup(Line([-0.25, 0.5, 0], [0.25, 0.9, 0], color=CRIMSON, stroke_width=5),
                        Line([-0.25, 0.9, 0], [0.25, 0.5, 0], color=CRIMSON, stroke_width=5))
        breakx._qc_intentional = True
        nolab = SerifLabel("no dashboard connects them", CRIMSON, size=22).to_edge(DOWN, buff=0.6)
        self.play(FadeOut(link), Create(breakx), FadeIn(nolab), run_time=0.8)
        self.wait(max(0.5, total - 4.3))


class B08_NoSeniors(Scene):         # not cheaper seniors — no seniors
    def construct(self):
        total = DUR["B08"]
        rails, rungs, plat = _rails(), _rungs(False), _platform()
        gap = DashedLine([LX, RUNG_YS[0], 0], [RX, RUNG_YS[0], 0], color=CRIMSON, stroke_width=4)
        gap._qc_intentional = True
        self.play(FadeIn(rails), FadeIn(rungs), FadeIn(plat), FadeIn(gap), run_time=1.0)
        arrow = Arrow([3.6, -1.6, 0], [1.7, PLAT_Y - 0.1, 0], color=NAVY, stroke_width=5, buff=0.15)
        alab = SerifLabel("hire a senior?", NAVY, size=22).move_to([3.6, -2.0, 0])
        self.play(GrowArrow(arrow), FadeIn(alab), run_time=0.9)
        none = LabelChip("none", accent=CRIMSON, size=26).move_to([0.0, 2.15, 0])
        self.play(FadeIn(none, scale=0.85), run_time=0.7)
        self.wait(max(0.5, total - 2.6))


class B09_IBMTriples(Scene):        # IBM triples the bottom rung (the one announcement)
    def construct(self):
        total = DUR["B09"]
        rails, rungs, plat = _rails(), _rungs(False), _platform()
        self.play(FadeIn(rails), FadeIn(rungs), FadeIn(plat), run_time=0.8)
        # rebuild + triple the bottom rung
        y0 = RUNG_YS[0]
        r1 = _rung(y0, NAVY)
        r2 = Line([LX, y0 - 0.32, 0], [RX, y0 - 0.32, 0], color=NAVY, stroke_width=4)
        r3 = Line([LX, y0 + 0.32, 0], [RX, y0 + 0.32, 0], color=NAVY, stroke_width=4)
        self.play(Create(r1), run_time=0.5)
        self.play(Create(r2), Create(r3), run_time=0.7)
        boarders = VGroup(_stick(0.0, y0 + 0.4, NAVY), _stick(-0.02, y0 - 0.5, NAVY))
        card = StateCard("IBM", side=1.5, accent=NAVY)
        card.move_to([-3.8, 0.6, 0])
        clab = SerifLabel("triple entry-level hiring · 2026", NAVY, size=20).next_to(card, DOWN, buff=0.25)
        struct = SerifLabel("not sentiment — structure", INK, size=22).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(boarders), FadeIn(card), FadeIn(clab), run_time=0.9)
        self.play(FadeIn(struct, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B10_TheRule(Scene):           # the cheapest rung feeds the priciest
    def construct(self):
        total = DUR["B10"]
        rails, rungs, plat = _rails(), _rungs(True), _platform()
        seniors = VGroup(_stick(-0.6, 2.1, NAVY), _stick(0.6, 2.1, NAVY))
        self.play(FadeIn(rails), FadeIn(rungs), FadeIn(plat), FadeIn(seniors), run_time=1.0)
        flow = Arrow([1.15, RUNG_YS[0], 0], [1.15, PLAT_Y - 0.1, 0], color=NAVY, stroke_width=5, buff=0.1)
        flab = SerifLabel("the pipeline", NAVY, size=20).next_to(flow, RIGHT, buff=0.2)
        self.play(GrowArrow(flow), FadeIn(flab), run_time=1.0)
        ring = HandRing(_rung(RUNG_YS[0]), color=CRIMSON)   # intentional (built-in)
        self.play(Create(ring), run_time=1.0)
        lab = SerifLabel("cut here, lose the top", CRIMSON, size=24).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 3.6))


class B11_End(Scene):               # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("The cheapest rung —", font=SERIF, color=INK, font_size=46, weight=BOLD)
        t2 = Text("where the expensive one is made.", font=SERIF, color=INK, font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 1", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
