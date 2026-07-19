"""vox_scenes.py — The Class-Size Paradox (Calling Bullshit, Vox style).

One Scene per GRAPHIC/CARD beat, rendered to the beat's measured duration
(read from beat_sheet.json at import — self-updating after any audio regen).
STILL beats A01 (packed hall) and A10 (brochure) carry no scene — they are
ai media slots filled from pantry; slates stand in for the review cut.

Color law: navy = the students · ink = the classrooms · golden highlighter =
the brochure number (the editor's pen, ONCE, on the 50 in A04). Terra is the
verdict accent only.

REPRESENTATIVE VALUES (FACTCHECK, the book's own worked example, VERIFIED
VERBATIM): 24 classes = 20 classes of 20 students + 4 classes of 200. Class
mean = (20*20 + 4*200)/24 = 1200/24 = 50. Students: 400 in the small classes,
800 in the giant four (two-thirds). Experienced mean = (400*20 + 800*200)/1200
= 168000/1200 = 140. Narration commits only to "fifty" and "one hundred forty"
and "two-thirds". No weighted-mean formula on screen (exclusion honored).

Desk preflight: 16:9 safe area x +/-6.4, y +/-3.5; margin arithmetic in comments.
Durations: audio not yet locked — fallbacks are the dry-run estimates and are
OVERRIDDEN by actual_duration_s the moment generate_audio.py runs.

Render: bash scripts/vox_run.sh reels/vox-class-size-paradox
"""
import json
import sys
import pathlib

import numpy as np

_HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[1] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403
from vox_graphics import (GROUND, INK, CRIMSON, NAVY, BLUE, GOLD, TERRA, SLATE,
                          SERIF, SerifLabel, LabelChip)


def dur(bid, fb=6.0):
    try:
        sheet = json.loads((_HERE / "beat_sheet.json").read_text())
        for b in sheet["beats"]:
            if b["beat_id"] == bid and b.get("actual_duration_s"):
                return float(b["actual_duration_s"])
    except Exception:
        pass
    return fb


def _card(scene, t, eyebrow, title, sub):
    eye = Text(eyebrow, font=SERIF, color=BLUE, font_size=24)
    ti = Text(title, font=SERIF, color=INK, font_size=52, weight=BOLD)
    if ti.width > 12.0:                          # 12.0 < 12.8 usable — safe
        ti.scale_to_fit_width(12.0)
    u = Line(ti.get_corner(DL) + DOWN * 0.15, ti.get_corner(DR) + DOWN * 0.15,
             color=CRIMSON, stroke_width=2)
    eye.to_edge(UP, buff=1.3)                    # top ~ 2.7 < 3.5 safe
    scene.play(FadeIn(eye), run_time=0.4)
    scene.play(FadeIn(ti), Create(u), run_time=0.8)
    used = 1.2
    if sub:
        sb = Text(sub, font=SERIF, color=INK, font_size=28)
        sb.next_to(u, DOWN, buff=0.4)
        scene.play(FadeIn(sb), run_time=0.4)
        used += 0.4
    scene.wait(max(0.1, t - used))


# ── the campus (shared by A03 / A04 / A09) ───────────────────────────────────
# 20 small ink squares (20-student classes) + 4 large ink squares (200-student
# classes). Side ratio ~sqrt(10)=3.16 encodes the 10x student count by AREA.
# small side 0.33, large side 1.04.
SMALL_S, LARGE_S = 0.33, 1.04
SMALL_COLS = [-4.9, -4.4, -3.9, -3.4, -2.9]      # pitch 0.5; leftmost 4.9 < 6.4
SMALL_ROWS = [1.35, 0.80, 0.25, -0.30]           # 4 rows -> 20 squares
LARGE_XS, LARGE_YS = [2.55, 3.95], [0.98, -0.40] # 2x2; right edge 4.47 < 6.4


def _campus():
    small = VGroup()
    for y in SMALL_ROWS:
        for x in SMALL_COLS:
            sq = Square(SMALL_S).set_fill(INK, 0.9).set_stroke(INK, 1.5)
            sq.move_to([x, y, 0])
            small.add(sq)
    large = VGroup()
    for y in LARGE_YS:
        for x in LARGE_XS:
            sq = Square(LARGE_S).set_fill(INK, 0.9).set_stroke(INK, 2)
            sq.move_to([x, y, 0])
            large.add(sq)
    lb_small = Text("20 classes of 20", font=SERIF, color=INK, font_size=22)
    lb_small.move_to([-3.9, -1.05, 0])           # bottom ~ -1.2 < 3.5 safe
    lb_large = Text("4 classes of 200", font=SERIF, color=INK, font_size=22)
    lb_large.move_to([3.25, -1.35, 0])
    return small, large, lb_small, lb_large


def _big_number(tracker, color, x=0.0, y=0.15, size=132):
    """A serif tally that counts as the narration lands. Text (no LaTeX)."""
    return always_redraw(
        lambda: Text(str(int(round(tracker.get_value()))), font=SERIF,
                     color=color, font_size=size, weight=BOLD).move_to([x, y, 0]))


# ── beats ────────────────────────────────────────────────────────────────────

class A02_Card(Scene):             # eyebrow / title / sub
    def construct(self):
        _card(self, dur("A02", 9.13), "CALLING BULLSHIT",
              "THE CLASS-SIZE PARADOX", "two true averages, one impression")


class A03_Campus(Scene):           # draw the 24 classrooms on
    def construct(self):
        t = dur("A03", 9.13)
        small, large, lb_small, lb_large = _campus()
        title = SerifLabel("one small college — 24 classes", accent=NAVY, size=26)
        title.move_to([0, 2.95, 0])              # top ~ 3.1 < 3.5 safe
        self.play(FadeIn(title), run_time=t * 0.12)
        self.play(AnimationGroup(*[GrowFromCenter(s) for s in small],
                                 lag_ratio=0.04), FadeIn(lb_small),
                  run_time=t * 0.40)
        self.play(AnimationGroup(*[GrowFromCenter(s) for s in large],
                                 lag_ratio=0.10), FadeIn(lb_large),
                  run_time=t * 0.33)
        self.wait(max(0.1, t * 0.15))


class A04_ClassMean(Scene):        # counter over classrooms -> 50; the pen, once
    def construct(self):
        t = dur("A04", 8.70)
        cap = SerifLabel("average over the 24 classes", accent=INK, size=28)
        cap.move_to([0, 2.4, 0])                 # top ~ 2.6 < 3.4 safe
        tr = ValueTracker(0)
        num = _big_number(tr, INK, x=0.0, y=-0.2)
        self.play(FadeIn(cap), run_time=t * 0.15)
        self.add(num)
        self.play(tr.animate.set_value(50), run_time=t * 0.35, rate_func=linear)
        # the editor's pen: golden highlighter behind the 50 — ONCE in the film.
        # intentional annotation touching the number -> exempt from TEXT_ON_CURVE.
        hi = Rectangle(width=2.2, height=1.9).set_fill(GOLD, 0.45).set_stroke(width=0, opacity=0)
        hi.move_to([0.0, -0.2, 0])
        hi._qc_intentional = True
        self.add(hi); self.bring_to_back(hi)
        hi.set_opacity(0)
        brochure = Text("the brochure number", font=SERIF, color=TERRA,
                        font_size=26, slant=ITALIC).move_to([0, -2.5, 0])
        self.play(hi.animate.set_fill(GOLD, 0.45), FadeIn(brochure), run_time=t * 0.25)
        self.wait(max(0.1, t * 0.25))


class A05_Card(Scene):
    def construct(self):
        _card(self, dur("A05", 5.65), "THE OTHER QUESTION",
              "AVERAGE THE STUDENTS, NOT THE CLASSES", "")


class A06_StudentDrop(Scene):      # a random student lands in a monster
    def construct(self):
        t = dur("A06", 11.74)
        r = np.random.default_rng(3)
        # two zones. each navy mark = 20 students. 20 marks small, 40 big.
        left = Rectangle(width=4.3, height=3.5).set_stroke(INK, 2).set_fill(opacity=0)
        left.move_to([-3.15, 0.15, 0])           # x -5.3..-1.0 ; safe
        right = Rectangle(width=4.7, height=3.5).set_stroke(INK, 2).set_fill(opacity=0)
        right.move_to([3.05, 0.15, 0])           # x 0.7..5.4 ; safe
        lz = Text("20 small classes", font=SERIF, color=INK, font_size=22).move_to([-3.15, 2.25, 0])
        rz = Text("4 giant lectures", font=SERIF, color=INK, font_size=22).move_to([3.05, 2.25, 0])

        def marks(cx, cols, rows, n):
            g = VGroup()
            x0 = cx - (cols - 1) * 0.42 / 2
            y0 = 1.15
            for i in range(n):
                x = x0 + (i % cols) * 0.42
                y = y0 - (i // cols) * 0.42
                g.add(Square(0.16).set_fill(NAVY, 1).set_stroke(width=0).move_to([x, y, 0]))
            return g
        small_m = marks(-3.15, 5, 4, 20)         # 20 marks = 400 students
        big_m = marks(3.05, 8, 5, 40)            # 40 marks = 800 students
        self.play(Create(left), Create(right), FadeIn(lz), FadeIn(rz),
                  run_time=t * 0.18)
        self.play(AnimationGroup(*[FadeIn(m, shift=DOWN * 0.2) for m in small_m],
                                 lag_ratio=0.02), run_time=t * 0.22)
        self.play(AnimationGroup(*[FadeIn(m, shift=DOWN * 0.2) for m in big_m],
                                 lag_ratio=0.02), run_time=t * 0.28)
        verdict = SerifLabel("two-thirds land here", accent=TERRA, size=28)
        verdict.move_to([3.05, -2.6, 0])         # under the big zone; box within +/-6.3/3.4
        arrow = Arrow([3.05, -2.2, 0], [3.05, -1.8, 0], color=TERRA, buff=0.05,
                      stroke_width=6)             # points UP into the giant-lecture zone
        self.play(FadeIn(verdict), GrowArrow(arrow), run_time=t * 0.14)
        self.wait(max(0.1, t * 0.18))


class A07_ExperiencedMean(Scene):  # counter recomputes over students -> 140
    def construct(self):
        t = dur("A07", 6.52)
        cap = SerifLabel("average over the students", accent=NAVY, size=28)
        cap.move_to([0, 2.4, 0])
        ghost = Text("50", font=SERIF, color=INK, font_size=90).move_to([-3.9, -0.2, 0])
        ghost.set_opacity(0.28)
        gx = Line(ghost.get_corner(DL), ghost.get_corner(UR), color=CRIMSON,
                  stroke_width=5)
        gx._qc_intentional = True                # deliberate strike-through -> exempt
        tr = ValueTracker(0)
        num = _big_number(tr, NAVY, x=0.6, y=-0.2)
        self.play(FadeIn(cap), run_time=t * 0.16)
        self.play(FadeIn(ghost), Create(gx), run_time=t * 0.18)
        self.add(num)
        self.play(tr.animate.set_value(140), run_time=t * 0.42, rate_func=linear)
        self.wait(max(0.1, t * 0.24))


class A08_Card(Scene):
    def construct(self):
        _card(self, dur("A08", 9.57), "THE MECHANISM",
              "SIZE-WEIGHTED SAMPLING", "big classes hold more witnesses")


class A09_TwoAverages(Scene):      # both numbers, same school, no lies
    def construct(self):
        t = dur("A09", 10.87)
        cap = SerifLabel("same school — the same 24 classes", accent=INK, size=26)
        cap.move_to([0, 2.75, 0])                # top ~ 2.9 < 3.4 safe
        # left result: over classes = 50 (ink) ; right: over students = 140 (navy)
        l_cap = Text("averaged over classes", font=SERIF, color=INK, font_size=26).move_to([-3.5, 1.35, 0])
        l_num = Text("50", font=SERIF, color=INK, font_size=112, weight=BOLD).move_to([-3.5, -0.25, 0])
        l_u = Line([-4.7, -1.45, 0], [-2.3, -1.45, 0], color=INK, stroke_width=3)
        r_cap = Text("averaged over students", font=SERIF, color=NAVY, font_size=26).move_to([3.5, 1.35, 0])
        r_num = Text("140", font=SERIF, color=NAVY, font_size=112, weight=BOLD).move_to([3.5, -0.25, 0])
        r_u = Line([4.9, -1.45, 0], [2.1, -1.45, 0], color=NAVY, stroke_width=3)
        self.play(FadeIn(cap), run_time=t * 0.14)
        self.play(FadeIn(l_cap), FadeIn(l_num), Create(l_u), run_time=t * 0.26)
        self.play(FadeIn(r_cap), FadeIn(r_num), Create(r_u), run_time=t * 0.26)
        verdict = SerifLabel("the choice of average is the message",
                             accent=TERRA, size=27)
        verdict.move_to([0, -2.6, 0])            # bottom ~ -2.8 < 3.4 safe
        self.play(FadeIn(verdict, shift=UP * 0.1), run_time=t * 0.18)
        self.wait(max(0.1, t * 0.16))


class A11_Everywhere(Scene):       # flights fuller, gyms busier
    def construct(self):
        t = dur("A11", 10.43)
        r = np.random.default_rng(11)
        l_lb = SerifLabel("your flight feels full", accent=NAVY, size=24)
        l_lb.move_to([-3.3, 2.6, 0])             # top ~ 2.8 < 3.5 safe
        r_lb = SerifLabel("your gym feels busy", accent=NAVY, size=24)
        r_lb.move_to([3.3, 2.6, 0])
        # plane: 6 rows x 4 seats, mostly occupied (navy) — the crowded flight
        plane = VGroup()
        for row in range(6):
            for seat in range(4):
                x = -4.6 + seat * 0.55 + (0.35 if seat >= 2 else 0)  # aisle gap
                y = 1.4 - row * 0.5
                filled = r.uniform() < 0.85
                plane.add(Square(0.28).set_fill(NAVY if filled else GROUND, 1)
                          .set_stroke(INK, 1.2).move_to([x, y, 0]))
        # gym: dense scatter of navy people-marks
        gym = VGroup(*[Square(0.15).set_fill(NAVY, 1).set_stroke(width=0)
                       .move_to([1.4 + r.uniform(0, 3.8), -1.6 + r.uniform(0, 3.0), 0])
                       for _ in range(46)])
        divider = Line([0, -2.3, 0], [0, 2.3, 0], color=INK, stroke_width=2).set_opacity(0.35)
        self.play(FadeIn(l_lb), Create(divider), run_time=t * 0.14)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.8) for m in plane],
                                 lag_ratio=0.02), run_time=t * 0.30)
        self.play(FadeIn(r_lb), run_time=t * 0.08)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.8) for m in gym],
                                 lag_ratio=0.01), run_time=t * 0.26)
        note = Text("big groups hold more witnesses", font=SERIF, color=INK,
                    font_size=24, slant=ITALIC).move_to([0, -2.85, 0])
        self.play(FadeIn(note), run_time=t * 0.10)
        self.wait(max(0.1, t * 0.12))


class A12_Card(Scene):             # closer (outro law pads this beat)
    def construct(self):
        _card(self, dur("A12", 7.83), "THE RULE",
              "ASK: AVERAGED OVER WHAT?", "the units chosen decide the story")
