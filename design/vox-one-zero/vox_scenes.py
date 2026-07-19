"""vox_scenes.py — Why One Zero Beats Four Nines
(vox-one-zero, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash scripts/vox_run.sh reels/vox-one-zero

Color law: navy #3D5A80 = the flow / healthy factor / Apply · crimson #BF3339 =
the closed valve / the zero / Skip. Gold = editor's pen, once. Hero object: a
score pipeline — votes sum into a flow that must pass two valves (collapse).
NO weight values, NO 'Bayesian', NO threshold number (card exclusions).

Gate A/B conventions: zero-width strokes are also zero-opacity; deliberate
line-on-text (strike/ring) is marked `_qc_intentional = True`; every `.animate`
uses a SINGLE method (the static checker's mock rejects chains).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 10.0, "B03": 9.5, "B04": 10.0, "B05": 10.0, "B06": 10.0,
       "B07": 9.5, "B08": 9.0, "B09": 10.0, "B10": 9.5, "B11": 8.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

FLOW_Y = 0.2


# ---------------------------------------------------------------- builders

def _flow(x0, x1, y=FLOW_Y, color=NAVY, h=0.5):
    r = Rectangle(width=abs(x1 - x0), height=h).set_fill(color, 1).set_stroke(width=0, opacity=0)
    r.move_to([(x0 + x1) / 2, y, 0])
    return r


def _valve(x, y=FLOW_Y, shut=False, label=""):
    col = CRIMSON if shut else NAVY
    ring = Circle(radius=0.55).set_stroke(col, 4).set_fill(WHITE, 1)
    ring.move_to([x, y, 0])
    parts = VGroup(ring)
    if shut:
        bar = Line([x - 0.38, y - 0.38, 0], [x + 0.38, y + 0.38, 0], color=CRIMSON, stroke_width=5)
        parts.add(bar)
    else:
        dot = Dot([x, y, 0], radius=0.09).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
        parts.add(dot)
    if label:
        lab = SerifLabel(label, col, size=20).next_to(ring, DOWN, buff=0.3)
        parts.add(lab)
    return parts


def _node(x, text, color, y=FLOW_Y):
    chip = LabelChip(text, accent=color, size=26)
    chip.move_to([x, y, 0])
    return chip


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("GATES, NOT VOTES", font=SERIF, color=NAVY, font_size=24)
        t1 = Text("Why one zero", font=SERIF, color=INK, font_size=54, weight=BOLD)
        t2 = Text("beats four nines", font=SERIF, color=INK, font_size=54, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Votes(Scene):             # votes are addends — they sum into a flow
    def construct(self):
        total = DUR["B03"]
        fit = Rectangle(width=2.4, height=0.5).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
        fit.move_to([-4.0, 0.9, 0])
        hire = Rectangle(width=2.4, height=0.5).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
        hire.move_to([-4.0, -0.5, 0])
        fl = SerifLabel("fit", NAVY, size=22).next_to(fit, UP, buff=0.15)
        hl = SerifLabel("can they hire you", NAVY, size=22).next_to(hire, DOWN, buff=0.15)
        plus = Text("+", font=SERIF, color=INK, font_size=48).move_to([-4.0, 0.2, 0])
        arrow = Arrow([-2.5, 0.2, 0], [0.2, 0.2, 0], color=INK, stroke_width=5, buff=0.2)
        flow = _flow(0.6, 3.2, y=0.2)
        flab = SerifLabel("the flow", NAVY, size=22).next_to(flow, DOWN, buff=0.3)
        self.play(GrowFromEdge(fit, LEFT), GrowFromEdge(hire, LEFT),
                  FadeIn(fl), FadeIn(hl), run_time=1.0)
        self.play(FadeIn(plus), run_time=0.4)
        self.play(GrowArrow(arrow), FadeIn(flow), FadeIn(flab), run_time=1.0)
        self.wait(max(0.5, total - 2.4))


class B04_Valves(Scene):            # the flow must pass two valves
    def construct(self):
        total = DUR["B04"]
        flow = _flow(-5.2, 4.0)
        v1 = _valve(-1.3, shut=False, label="is it real?")
        v2 = _valve(1.5, shut=False, label="can you start?")
        node = _node(4.6, "Apply", NAVY)
        self.play(FadeIn(flow), run_time=0.6)
        self.play(FadeIn(v1), run_time=0.6)
        self.play(FadeIn(v2), run_time=0.6)
        self.play(FadeIn(node, shift=LEFT * 0.2), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B05_Collapse(Scene):          # close a valve → the flow collapses to zero
    def construct(self):
        total = DUR["B05"]
        up_flow = _flow(-5.2, 1.5)                       # up to the second valve
        v1 = _valve(-1.3, shut=False)
        v2open = Circle(radius=0.55).set_stroke(NAVY, 4).set_fill(WHITE, 1).move_to([1.5, FLOW_Y, 0])
        down_flow = _flow(2.05, 4.0)                     # downstream, will collapse
        node = _node(4.6, "Apply", NAVY)
        vlab = SerifLabel("can you start?", NAVY, size=20).next_to(v2open, DOWN, buff=0.3)
        self.play(FadeIn(up_flow), FadeIn(v1), FadeIn(v2open), FadeIn(down_flow),
                  FadeIn(node), FadeIn(vlab), run_time=1.0)
        # the valve slams crimson-shut
        v2shut = VGroup(Circle(radius=0.55).set_stroke(CRIMSON, 4).set_fill(WHITE, 1).move_to([1.5, FLOW_Y, 0]),
                        Line([1.12, FLOW_Y - 0.38, 0], [1.88, FLOW_Y + 0.38, 0], color=CRIMSON, stroke_width=5))
        self.play(Transform(v2open, v2shut), run_time=0.7)
        # downstream flow collapses to a flat zero line
        flat = Line([2.05, FLOW_Y, 0], [4.0, FLOW_Y, 0], color=CRIMSON, stroke_width=4)
        x0 = LabelChip("x 0", accent=CRIMSON, size=26).move_to([3.0, FLOW_Y + 0.9, 0])
        skip = _node(4.6, "Skip", CRIMSON)
        self.play(Transform(down_flow, flat), run_time=0.9)
        self.play(FadeIn(x0, shift=DOWN * 0.2), Transform(node, skip), run_time=0.7)
        self.wait(max(0.5, total - 3.3))


class B06_AverageDilutes(Scene):    # averaging hides the zero (ILLUSTRATIVE)
    def construct(self):
        total = DUR["B06"]
        y0, sc = -1.7, 2.9
        vals = [0.9, 0.9, 0.9, 0.9, 0.0]
        cols = [NAVY, NAVY, NAVY, NAVY, CRIMSON]
        bars = VGroup()
        for i, (v, c) in enumerate(zip(vals, cols)):
            h = max(0.05, v * sc)
            b = Rectangle(width=0.6, height=h).set_fill(c, 1).set_stroke(width=0, opacity=0)
            b.move_to([-5.0 + i * 0.85, y0, 0], aligned_edge=DOWN)
            bars.add(b)
        cutoff = DashedLine([-5.6, y0 + 0.3 * sc, 0], [5.6, y0 + 0.3 * sc, 0],
                            color=INK, stroke_width=2)
        clab = SerifLabel("apply line", INK, size=18).next_to(cutoff, RIGHT, buff=0.05)
        arrow = Arrow([-0.7, y0 + 1.0, 0], [1.6, y0 + 1.0, 0], color=INK, stroke_width=4, buff=0.2)
        alab = Text("average", font=SERIF, color=INK, font_size=22).next_to(arrow, UP, buff=0.15)
        avg = Rectangle(width=0.8, height=0.68 * sc).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
        avg.move_to([3.0, y0, 0], aligned_edge=DOWN)
        note = SerifLabel("still looks like apply", NAVY, size=22)
        note.next_to(avg, UP, buff=0.2)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12),
                  run_time=1.4)
        self.play(Create(cutoff), FadeIn(clab), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(alab), run_time=0.6)
        self.play(GrowFromEdge(avg, DOWN), FadeIn(note), run_time=0.8)
        self.wait(max(0.5, total - 3.4))


class B07_TwoFates(Scene):          # averaged 'go' vs multiplied 'stop'
    def construct(self):
        total = DUR["B07"]
        y0, sc = -1.7, 2.9
        cutoff = DashedLine([-5.0, y0 + 0.3 * sc, 0], [5.0, y0 + 0.3 * sc, 0],
                            color=INK, stroke_width=2)
        avg = Rectangle(width=1.2, height=0.68 * sc).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
        avg.move_to([-3.0, y0, 0], aligned_edge=DOWN)
        al = SerifLabel("averaged: go", NAVY, size=24).next_to(avg, UP, buff=0.2)
        mul = Line([2.2, y0, 0], [3.8, y0, 0], color=CRIMSON, stroke_width=5)
        ml = SerifLabel("multiplied: stop", CRIMSON, size=24).move_to([3.0, y0 + 0.7, 0])
        self.play(Create(cutoff), run_time=0.5)
        self.play(GrowFromEdge(avg, DOWN), FadeIn(al), run_time=0.8)
        self.play(Create(mul), FadeIn(ml), run_time=0.8)
        ring = HandRing(VGroup(avg, al), color=CRIMSON)   # intentional (built-in)
        self.play(Create(ring), run_time=1.1)
        self.wait(max(0.5, total - 3.2))


class B08_WorthNothing(Scene):      # DOCUMENT — what the gate knows
    def construct(self):
        _quote_scene(self, "A job you can't start is worth nothing.",
                     "— what the gate knows and the average forgets", None,
                     "nothing", DUR["B08"])


class B09_CalendarKilled(Scene):    # jobs the calendar already killed
    def construct(self):
        total = DUR["B09"]
        # calendar
        cal = Rectangle(width=3.0, height=2.6).set_fill(WHITE, 1).set_stroke("#C9C2B4", 2)
        cal.move_to([-3.6, 0.2, 0])
        head = Rectangle(width=3.0, height=0.5).set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        head.move_to([-3.6, 1.35, 0])
        grid = VGroup()
        for r in range(3):
            for c in range(4):
                cell = Square(0.5).set_stroke("#C9C2B4", 1.2).set_fill(WHITE, 0)
                cell.move_to([-4.7 + c * 0.62, 0.7 - r * 0.62, 0])
                grid.add(cell)
        x_cell = grid[10]
        xmark = VGroup(
            Line(x_cell.get_corner(DL), x_cell.get_corner(UR), color=CRIMSON, stroke_width=5),
            Line(x_cell.get_corner(UL), x_cell.get_corner(DR), color=CRIMSON, stroke_width=5))
        xmark._qc_intentional = True
        dl = SerifLabel("deadline passed", CRIMSON, size=20).next_to(cal, DOWN, buff=0.3)
        # the shut door
        door = Rectangle(width=1.7, height=3.2).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 3)
        door.move_to([4.2, 0.0, 0])
        knob = Dot([3.7, 0.0, 0], radius=0.08).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        dlab = SerifLabel("already closed", CRIMSON, size=22).next_to(door, DOWN, buff=0.3)
        self.play(FadeIn(cal), FadeIn(head), FadeIn(grid), run_time=0.9)
        self.play(Create(xmark), FadeIn(dl), run_time=0.7)
        self.play(FadeIn(door), FadeIn(knob), FadeIn(dlab), run_time=0.7)
        envs = VGroup()
        for k in range(5):
            e = Rectangle(width=0.5, height=0.34).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
            e.move_to([2.2 + (k % 3) * 0.15, -1.4 + (k // 3) * 0.4, 0])
            envs.add(e)
        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.4) for e in envs],
                              lag_ratio=0.12), run_time=1.2)
        self.wait(max(0.5, total - 3.5))


class B10_TheRule(Scene):           # clears every valve, or it's zero
    def construct(self):
        total = DUR["B10"]
        # top pipeline — both open → Apply
        top = _flow(-5.0, 2.4, y=1.4, h=0.35)
        t1 = Circle(radius=0.32).set_stroke(NAVY, 3).set_fill(WHITE, 1).move_to([-1.6, 1.4, 0])
        t2 = Circle(radius=0.32).set_stroke(NAVY, 3).set_fill(WHITE, 1).move_to([0.4, 1.4, 0])
        tnode = _node(3.6, "Apply", NAVY, y=1.4)
        # bottom pipeline — one shut → Skip
        bot = _flow(-5.0, -0.1, y=-1.4, h=0.35)
        b1 = Circle(radius=0.32).set_stroke(NAVY, 3).set_fill(WHITE, 1).move_to([-1.6, -1.4, 0])
        b2 = VGroup(Circle(radius=0.32).set_stroke(CRIMSON, 3).set_fill(WHITE, 1).move_to([0.4, -1.4, 0]),
                    Line([0.18, -1.62, 0], [0.62, -1.18, 0], color=CRIMSON, stroke_width=4))
        bflat = Line([0.75, -1.4, 0], [2.4, -1.4, 0], color=CRIMSON, stroke_width=4)
        bnode = _node(3.6, "Skip", CRIMSON, y=-1.4)
        rule = SerifLabel("clears every valve, or it's zero", INK, size=26).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(top), FadeIn(t1), FadeIn(t2), FadeIn(tnode), run_time=0.9)
        self.play(FadeIn(bot), FadeIn(b1), FadeIn(b2), FadeIn(bflat), FadeIn(bnode), run_time=0.9)
        self.play(FadeIn(rule, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B11_End(Scene):               # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Nines and a zero —", font=SERIF, color=INK, font_size=46, weight=BOLD)
        t2 = Text("multiply, and zero wins.", font=SERIF, color=INK, font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 11", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
