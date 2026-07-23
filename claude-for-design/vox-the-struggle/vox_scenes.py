"""vox_scenes.py — Why AI Help Made Students Worse
(vox-the-struggle, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash scripts/vox_run.sh reels/vox-the-struggle

Color law: navy #3D5A80 = struggle / learning / the brain that fires and grows ·
crimson #BF3339 = the AI-assisted path / the dark brain / the exam drop. Gold =
editor's pen, once. Hero: two cartoon brains on one problem (compare). Name a
spark only — NO dopamine/BDNF/dendritic-spine naming (card exclusion).

Gate A/B conventions: zero-width strokes are also zero-opacity; deliberate
line-on-text (ring) is marked `_qc_intentional = True`; every `.animate` uses a
SINGLE method (the static checker's mock rejects chains).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 10.5, "B03": 9.5, "B04": 8.5, "B05": 10.0, "B06": 10.0,
       "B07": 10.0, "B08": 10.0, "B09": 9.5, "B10": 9.5, "B11": 7.5}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

_NODES = [(-0.7, 0.4), (0.1, 0.62), (0.72, 0.22), (-0.42, -0.42), (0.44, -0.52), (0.0, 0.02)]


# ---------------------------------------------------------------- builders

def _brain(cx, cy, color, grown=False, s=1.0):
    """A cartoon brain: rounded outline + central fissure. If grown, navy
    connective dots + lines branch inside (the wiring that IS the memory)."""
    outline = Circle(radius=1.15 * s).set_stroke(color, 4).set_fill(color, 0.05)
    outline.stretch(1.15, 0).move_to([cx, cy, 0])          # widen to a brain oval
    fissure = Line([cx, cy + 0.85 * s, 0], [cx, cy - 0.85 * s, 0], color=color, stroke_width=2)
    g = VGroup(outline, fissure)
    if grown:
        dots = VGroup(*[Dot([cx + dx * s, cy + dy * s, 0], radius=0.07)
                        .set_fill(color, 1).set_stroke(width=0, opacity=0)
                        for dx, dy in _NODES])
        lines = VGroup(*[Line([cx + _NODES[i][0] * s, cy + _NODES[i][1] * s, 0],
                              [cx + _NODES[i + 1][0] * s, cy + _NODES[i + 1][1] * s, 0],
                              color=color, stroke_width=2.5)
                         for i in range(len(_NODES) - 1)])
        g.add(lines, dots)
    return g


def _spark(cx, cy, color, r=0.5):
    return VGroup(*[Line([cx, cy, 0], [cx + np.cos(a) * r, cy + np.sin(a) * r, 0],
                         color=color, stroke_width=4)
                    for a in np.linspace(0, TAU, 8, endpoint=False)])


def _bolt(cx, cy, color=INK):
    pts = [[cx - 0.18, cy + 0.6, 0], [cx + 0.12, cy + 0.12, 0],
           [cx - 0.06, cy + 0.12, 0], [cx + 0.2, cy - 0.6, 0]]
    return VGroup(*[Line(pts[i], pts[i + 1], color=color, stroke_width=5)
                    for i in range(len(pts) - 1)])


def _worksheet(cx, cy, w=2.0, h=2.6):
    page = Rectangle(width=w, height=h).set_fill(WHITE, 1).set_stroke("#C9C2B4", 1.6)
    page.move_to([cx, cy, 0])
    qs = VGroup(*[Line([cx - w / 2 + 0.25, cy + h / 2 - 0.5 - i * 0.5, 0],
                       [cx + 0.0, cy + h / 2 - 0.5 - i * 0.5, 0],
                       color="#C9C2B4", stroke_width=3) for i in range(4)])
    return page, qs


def _answers(cx, cy, w=2.0, h=2.6, color=NAVY):
    return VGroup(*[Line([cx + 0.2, cy + h / 2 - 0.5 - i * 0.5, 0],
                         [cx + w / 2 - 0.25, cy + h / 2 - 0.5 - i * 0.5, 0],
                         color=color, stroke_width=4) for i in range(4)])


def _bars(label, left_h, right_h, tag, tag_on_right=True):
    """Two bars (navy left, crimson right) under a label + a tag on one bar."""
    y0 = -1.9
    lbar = Rectangle(width=1.1, height=max(0.05, left_h)).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
    lbar.move_to([-1.7, y0, 0], aligned_edge=DOWN)
    rbar = Rectangle(width=1.1, height=max(0.05, right_h)).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
    rbar.move_to([1.7, y0, 0], aligned_edge=DOWN)
    ll = SerifLabel("struggled", NAVY, size=20).next_to(lbar, DOWN, buff=0.2)
    rl = SerifLabel("used AI", CRIMSON, size=20).next_to(rbar, DOWN, buff=0.2)
    head = SerifLabel(label, INK, size=26).to_edge(UP, buff=0.7)
    base = Line([-3.6, y0, 0], [3.6, y0, 0], color=INK, stroke_width=2)
    tgt = rbar if tag_on_right else lbar
    tg = LabelChip(tag, accent=(CRIMSON if tag_on_right else NAVY), size=24).next_to(tgt, UP, buff=0.2)
    return VGroup(base, lbar, rbar, ll, rl, head), tg, lbar, rbar


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE STRUGGLE IS THE MECHANISM", font=SERIF, color=NAVY, font_size=22)
        t1 = Text("Why AI help", font=SERIF, color=INK, font_size=54, weight=BOLD)
        t2 = Text("made students worse", font=SERIF, color=INK, font_size=54, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_PracticeScores(Scene):    # practice: the AI group races ahead (+48%)
    def construct(self):
        total = DUR["B03"]
        grp, tag, lbar, rbar = _bars("practice", 1.4, 3.5, "+48%", tag_on_right=True)
        self.play(FadeIn(grp[0]), FadeIn(grp[3]), FadeIn(grp[4]), FadeIn(grp[5]), run_time=0.7)
        self.play(GrowFromEdge(lbar, DOWN), GrowFromEdge(rbar, DOWN), run_time=1.1)
        self.play(FadeIn(tag, shift=DOWN * 0.2), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B04_FeelingVsLearning(Scene):  # DOCUMENT — feeling fluent is not learning
    def construct(self):
        _quote_scene(self, "Feeling fluent is not learning.",
                     "— what the practice scores hid", None,
                     "learning", DUR["B04"])


class B05_SparkFires(Scene):        # struggle → spark → connections grow
    def construct(self):
        total = DUR["B05"]
        brain = _brain(-0.6, 0.4, NAVY, grown=False)
        bolt = _bolt(-3.2, 0.4, INK)
        blab = SerifLabel("something you can't yet do", INK, size=20).next_to(bolt, DOWN, buff=0.4)
        self.play(FadeIn(brain), run_time=0.7)
        self.play(FadeIn(bolt, shift=RIGHT * 0.3), FadeIn(blab), run_time=0.7)
        spark = _spark(-0.6, 0.4, NAVY, r=0.55)
        self.play(Create(spark), run_time=0.6)
        cx, cy = -0.6, 0.4                                  # grow connections inline
        conn_lines = VGroup(*[Line([cx + _NODES[i][0], cy + _NODES[i][1], 0],
                                   [cx + _NODES[i + 1][0], cy + _NODES[i + 1][1], 0],
                                   color=NAVY, stroke_width=2.5)
                              for i in range(len(_NODES) - 1)])
        conn_dots = VGroup(*[Dot([cx + dx, cy + dy, 0], radius=0.07)
                             .set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
                             for dx, dy in _NODES])
        self.play(LaggedStart(*[Create(m) for m in conn_lines],
                              *[FadeIn(m) for m in conn_dots], lag_ratio=0.12), run_time=1.6)
        lab = SerifLabel("a spark fires — connections grow", NAVY, size=24).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 4.2))


class B06_NoSpark(Scene):           # remove the struggle → no spark, nothing grows
    def construct(self):
        total = DUR["B06"]
        page, qs = _worksheet(-2.8, 0.3)
        brain = _brain(2.6, 0.4, CRIMSON, grown=False)
        self.play(FadeIn(page), FadeIn(qs), FadeIn(brain), run_time=0.9)
        ans = _answers(-2.8, 0.3, color=NAVY)              # the worksheet fills itself
        self.play(LaggedStart(*[Create(a) for a in ans], lag_ratio=0.2), run_time=1.6)
        lab = SerifLabel("no struggle, no spark", CRIMSON, size=26).to_edge(DOWN, buff=0.7)
        dark = SerifLabel("(dark)", CRIMSON, size=20).next_to(brain, DOWN, buff=0.2)
        self.play(FadeIn(lab), FadeIn(dark), run_time=0.7)
        self.wait(max(0.5, total - 3.2))


class B07_TwoBrains(Scene):         # THE COMPARE — same hour, two brains
    def construct(self):
        total = DUR["B07"]
        left = _brain(-3.3, 0.7, NAVY, grown=True, s=0.95)
        lspark = _spark(-3.3, 0.7, NAVY, r=0.45)
        right = _brain(3.3, 0.7, CRIMSON, grown=False, s=0.95)
        ll = SerifLabel("struggled: wired", NAVY, size=22).next_to(left, UP, buff=0.25)
        rl = SerifLabel("used AI: dark", CRIMSON, size=22).next_to(right, UP, buff=0.25)
        self.play(FadeIn(left), FadeIn(lspark), FadeIn(right), run_time=1.0)
        self.play(FadeIn(ll), FadeIn(rl), run_time=0.6)
        # identical homework below both
        wl = Rectangle(width=1.4, height=1.0).set_fill(WHITE, 1).set_stroke("#C9C2B4", 1.5).move_to([-3.3, -1.9, 0])
        wr = Rectangle(width=1.4, height=1.0).set_fill(WHITE, 1).set_stroke("#C9C2B4", 1.5).move_to([3.3, -1.9, 0])
        d1 = LabelChip("done", accent=INK, size=16).move_to([-3.3, -1.9, 0])
        d2 = LabelChip("done", accent=INK, size=16).move_to([3.3, -1.9, 0])
        idlab = SerifLabel("identical homework", INK, size=24).move_to([0, -1.9, 0])
        self.play(FadeIn(wl), FadeIn(wr), FadeIn(d1), FadeIn(d2), FadeIn(idlab), run_time=0.9)
        self.wait(max(0.5, total - 2.5))


class B08_ExamReversal(Scene):      # the exam flips: AI group -17 points
    def construct(self):
        total = DUR["B08"]
        grp, tag, lbar, rbar = _bars("exam  (no AI)", 3.4, 1.5, "-17 pts", tag_on_right=True)
        self.play(FadeIn(grp[0]), FadeIn(grp[3]), FadeIn(grp[4]), FadeIn(grp[5]), run_time=0.7)
        self.play(GrowFromEdge(lbar, DOWN), GrowFromEdge(rbar, DOWN), run_time=1.1)
        flip = SerifLabel("the gap flipped", NAVY, size=22).next_to(lbar, UP, buff=0.2)
        self.play(FadeIn(tag, shift=DOWN * 0.2), FadeIn(flip), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B09_ArtifactVsBrain(Scene):   # artifact fine, brain unchanged
    def construct(self):
        total = DUR["B09"]
        page, qs = _worksheet(-3.0, 0.4)
        ans = _answers(-3.0, 0.4, color=NAVY)
        aplus = LabelChip("A+", accent=NAVY, size=28).next_to(page, UP, buff=0.2)
        brain = _brain(2.8, 0.4, CRIMSON, grown=False)
        self.play(FadeIn(page), FadeIn(qs), FadeIn(ans), FadeIn(aplus), FadeIn(brain), run_time=1.0)
        pl = SerifLabel("artifact: fine", NAVY, size=22).next_to(page, DOWN, buff=0.3)
        bl = SerifLabel("brain: unchanged", CRIMSON, size=22).next_to(brain, DOWN, buff=0.3)
        self.play(FadeIn(pl), FadeIn(bl), run_time=0.6)
        ring = HandRing(brain, color=CRIMSON)              # intentional (built-in)
        self.play(Create(ring), run_time=1.1)
        self.wait(max(0.5, total - 2.7))


class B10_SharperStruggle(Scene):   # good AI makes the struggle sharper
    def construct(self):
        total = DUR["B10"]
        brain = _brain(0.6, 0.4, NAVY, grown=True)
        spark = _spark(0.6, 0.4, NAVY, r=0.5)
        self.play(FadeIn(brain), FadeIn(spark), run_time=0.8)
        chip = LabelChip("AI", accent=NAVY, size=24).move_to([-4.2, 0.4, 0])
        bolt = _bolt(-2.2, 0.4, INK)
        arrow = Arrow([-3.7, 0.4, 0], [-2.7, 0.4, 0], color=NAVY, stroke_width=5, buff=0.15)
        blab = SerifLabel("a sharper question", INK, size=20).next_to(bolt, DOWN, buff=0.4)
        self.play(FadeIn(chip), GrowArrow(arrow), FadeIn(bolt), FadeIn(blab), run_time=0.9)
        big = _spark(0.6, 0.4, NAVY, r=0.75)               # the spark brightens
        self.play(Transform(spark, big), run_time=0.7)
        lab = SerifLabel("sharper struggle, not none", NAVY, size=24).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B11_End(Scene):               # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Remove the struggle —", font=SERIF, color=INK, font_size=46, weight=BOLD)
        t2 = Text("you remove the learning.", font=SERIF, color=INK, font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        s = Text("from The Reallocation Engine — the fundamental themes", font=SERIF,
                 color=INK, font_size=24)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
