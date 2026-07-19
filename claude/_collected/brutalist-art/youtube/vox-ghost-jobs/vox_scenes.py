"""vox_scenes.py — Why You Can Spot a Fake Job Without Reading It
(vox-ghost-jobs, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-ghost-jobs

Color law: dusty blue #5B7B9C = live/real · terracotta #D35F43 = ghost/fake.
The liveness meter is QUALITATIVE — no probabilities or percentages printed.
Three fingerprints max on screen (card exclusion).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 10.8, "B04": 8.8, "B05": 8.4, "B06": 6.0, "B07": 6.0,
       "B08": 6.4, "B09": 10.0, "B10": 8.8, "B11": 8.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------------- builders

_METER_POS = np.array([2.8, -0.3, 0])   # meter center
_METER_H = 3.6
_METER_BOTTOM = _METER_POS + DOWN * (_METER_H / 2)


def _fill_rect(level):
    """Meter fill — blue above the midline, terracotta below (zone color)."""
    h = max(0.06, _METER_H * level)
    color = BLUE if level >= 0.5 else TERRA
    r = Rectangle(width=0.62, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    r.move_to(_METER_BOTTOM + UP * 0.02, aligned_edge=DOWN)
    return r


def _meter_frame():
    tube = Rectangle(width=0.7, height=_METER_H).set_stroke(INK, 2)
    tube.move_to(_METER_POS)
    live = SerifLabel("live", BLUE, size=22)
    live.next_to(tube, UP, buff=0.25)
    ghost = SerifLabel("ghost", TERRA, size=22)
    ghost.next_to(tube, DOWN, buff=0.25)
    return VGroup(tube, live, ghost)


def _posting_card(center=LEFT * 2.2 + UP * 0.3, w=3.0, h=3.8):
    card = Rectangle(width=w, height=h).set_fill(WHITE, 1)
    card.set_stroke("#D8D2C4", 1.5)
    card.move_to(center)
    title = Rectangle(width=w * 0.7, height=0.22)
    title.set_fill(INK, 0.85).set_stroke(width=0, opacity=0)
    title.move_to(center + UP * (h / 2 - 0.5))
    lines = VGroup(*[Line(LEFT * (w * 0.38), RIGHT * (w * 0.38 - 0.25 * k),
                          color="#C9C2B4", stroke_width=3)
                     .move_to(center + UP * (h / 2 - 1.1 - 0.38 * k)
                              + LEFT * (0.12 * k))
                     for k in range(6)])
    return VGroup(card, title, lines)


_STAMP_SPECS = (("STALE CLOCK", UP * 1.1, -0.05),
                ("FROZEN SIBLINGS", DOWN * 0.1, 0.04),
                ("CLONED TEXT", DOWN * 1.3, -0.04))


def _stamp(i):
    text, offset, ang = _STAMP_SPECS[i]
    chip = LabelChip(text, accent=TERRA, size=24)
    if chip.width > 2.9:
        chip.scale_to_fit_width(2.9)
    chip.rotate(ang * PI)
    chip.move_to(LEFT * 2.2 + UP * 0.3 + offset)
    return chip


def _chart_state(n_stamps, level):
    """Posting card + meter frame + fill + first n stamps (for scene entry)."""
    return VGroup(_posting_card(), _meter_frame(), _fill_rect(level),
                  *[_stamp(i) for i in range(n_stamps)])


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("GHOST POSTINGS", font=SERIF, color=BLUE, font_size=24)
        t1 = Text("Why you can spot a fake job", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("without reading it", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B04_SpamReads(Scene):        # the pivot — what a spam filter reads
    def construct(self):
        _quote_scene(self, "Sent at 3 a.m. Ten thousand copies. No replies.",
                     "— what a spam filter actually reads", None,
                     "reads", DUR["B04"])


class B05_SpamMeter(Scene):        # score the behavior, not the words
    def construct(self):
        total = DUR["B05"]
        env = VGroup(Rectangle(width=2.8, height=1.9).set_stroke(INK, 2)
                     .set_fill(WHITE, 1))
        c = env[0].get_center()
        flap_l = Line(env[0].get_corner(UL), c + DOWN * 0.15, color=INK,
                      stroke_width=2)
        flap_r = Line(env[0].get_corner(UR), c + DOWN * 0.15, color=INK,
                      stroke_width=2)
        env.add(flap_l, flap_r)
        env.move_to(LEFT * 2.2 + UP * 0.3)
        frame = _meter_frame()
        fill = _fill_rect(0.75)
        self.play(FadeIn(env), FadeIn(frame), FadeIn(fill), run_time=0.9)
        ticks = ("3 a.m. blast", "no replies", "identical copies")
        levels = (0.55, 0.35, 0.14)
        for i, (name, lv) in enumerate(zip(ticks, levels)):
            chip = LabelChip(name, accent=TERRA, size=22)
            if chip.width > 2.3:
                chip.scale_to_fit_width(2.3)
            # clean column in the gap between envelope (right edge ~-0.8)
            # and meter tube (left edge ~2.45)
            chip.move_to(RIGHT * 0.85 + UP * (1.6 - i * 1.0))
            chip.rotate((0.02 if i % 2 else -0.02) * PI)
            self.play(FadeIn(chip, shift=DOWN * 0.2),
                      Transform(fill, _fill_rect(lv)), run_time=0.9)
        spam = LabelChip("SPAM", accent=TERRA, size=28)
        spam.rotate(-0.04 * PI)
        # lower half of the envelope, fully inside the border, below the
        # flap lines (they converge at y≈+0.15; chip top stays under 0.05)
        spam.move_to(env[0].get_center() + DOWN * 0.55)
        self.play(FadeIn(spam, scale=0.85), run_time=0.6)
        self.wait(max(0.5, total - 0.9 - 3 * 0.9 - 0.6))


class B06_StaleClock(Scene):       # fingerprint 1/3
    def construct(self):
        total = DUR["B06"]
        chart = _chart_state(0, 0.78)
        fill = chart[2]
        self.play(FadeIn(chart), run_time=0.8)
        self.play(FadeIn(_stamp(0), shift=DOWN * 0.25),
                  Transform(fill, _fill_rect(0.60)), run_time=1.0)
        self.wait(max(0.5, total - 1.8))


class B07_FrozenSiblings(Scene):   # fingerprint 2/3 — crosses the midline
    def construct(self):
        total = DUR["B07"]
        chart = _chart_state(1, 0.60)
        fill = chart[2]
        self.add(chart)
        sibs = VGroup(*[Rectangle(width=0.72, height=0.5)
                        .set_stroke("#C9C2B4", 1.5).set_fill(WHITE, 0.5)
                        .move_to(LEFT * 3.6 + RIGHT * i * 0.86 + DOWN * 2.85)
                        for i in range(4)])
        self.play(LaggedStart(*[FadeIn(s) for s in sibs], lag_ratio=0.15,
                              run_time=0.8))
        self.play(FadeIn(_stamp(1), shift=DOWN * 0.25),
                  Transform(fill, _fill_rect(0.38)), run_time=1.0)
        self.wait(max(0.5, total - 1.8))


class B08_ClonedText(Scene):       # fingerprint 3/3 — deep in the ghost zone
    def construct(self):
        total = DUR["B08"]
        chart = _chart_state(2, 0.38)
        fill = chart[2]
        # the clone is a STROKE-FREE silhouette — a blank pale sheet sliding
        # out from behind (a generated copy has nothing of its own on it),
        # and fills carry no curve/line for the layout audit to strike
        ghost_copy = Rectangle(width=3.0, height=3.8)
        ghost_copy.set_fill("#E7E0D1", 0.9).set_stroke(width=0, opacity=0)
        ghost_copy.move_to(LEFT * 2.2 + UP * 0.3)
        self.add(ghost_copy, chart)
        ghost_target = Rectangle(width=3.0, height=3.8)
        ghost_target.set_fill("#E7E0D1", 0.9).set_stroke(width=0, opacity=0)
        ghost_target.move_to(LEFT * 3.1 + UP * 0.75)
        self.play(Transform(ghost_copy, ghost_target), run_time=0.8)
        self.play(FadeIn(_stamp(2), shift=DOWN * 0.25),
                  Transform(fill, _fill_rect(0.15)), run_time=1.0)
        self.wait(max(0.5, total - 1.8))


class B09_AccumulateRing(Scene):   # the pattern, not any single stamp
    def construct(self):
        total = DUR["B09"]
        chart = _chart_state(3, 0.15)
        self.add(chart)
        meter_zone = VGroup(chart[1], chart[2])
        ring = HandRing(meter_zone, color=TERRA)
        self.play(Create(ring), run_time=1.1)
        self.wait(max(0.5, total - 1.1))


class B10_TwoDoors(Scene):         # same employer, opposite calls
    def construct(self):
        total = DUR["B10"]
        title = SerifLabel("same employer, same title", NAVY, size=28)
        title.to_edge(UP, buff=0.6)

        def mini(xc):
            card = Rectangle(width=2.2, height=2.8).set_fill(WHITE, 1)
            card.set_stroke("#D8D2C4", 1.5).move_to(np.array([xc - 1.5, -0.4, 0]))
            tube = Rectangle(width=0.5, height=2.6).set_stroke(INK, 2)
            tube.move_to(np.array([xc + 0.9, -0.4, 0]))
            return card, tube

        def mini_fill(xc, level, color):
            h = max(0.06, 2.6 * level)
            r = Rectangle(width=0.42, height=h)
            r.set_fill(color, 1).set_stroke(width=0, opacity=0)
            r.move_to(np.array([xc + 0.9, -1.7 + 0.02, 0]), aligned_edge=DOWN)
            return r

        lcard, ltube = mini(-3.0)
        rcard, rtube = mini(3.0)
        lfill = mini_fill(-3.0, 0.45, BLUE)
        rfill = mini_fill(3.0, 0.45, BLUE)
        self.play(FadeIn(title), FadeIn(lcard), FadeIn(ltube), FadeIn(lfill),
                  FadeIn(rcard), FadeIn(rtube), FadeIn(rfill), run_time=1.0)
        self.play(Transform(lfill, mini_fill(-3.0, 0.85, BLUE)),
                  Transform(rfill, mini_fill(3.0, 0.12, TERRA)), run_time=1.3)
        live = LabelChip("LIVE", accent=BLUE, size=26)
        live.next_to(lcard, DOWN, buff=0.35)
        ghost = LabelChip("GHOST", accent=TERRA, size=26)
        ghost.next_to(rcard, DOWN, buff=0.35)
        self.play(FadeIn(live, scale=0.9), FadeIn(ghost, scale=0.9),
                  run_time=0.7)
        self.wait(max(0.5, total - 3.0))


class B11_End(Scene):              # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("A posting is a signal —", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("signals can lie.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 8", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
