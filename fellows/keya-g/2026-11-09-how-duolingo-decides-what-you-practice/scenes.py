"""Manim scenes for "How Duolingo Decides What You Practice Next" (Keya G.).

Scenes, one per Manim beat in beat_sheet.json:
B02_Hook                 します "do" and みます "look" come back again and again; "when?"
B04_ForgettingCurve      axes, a notebook, the forgetting curve draws itself
B05_SpacedRepetition     cramming vs spaced practice on two lanes; the dip before the next practice
B06_LeitnerBoxes         three boxes; a right answer moves a card on, a wrong one moves it back
B07_HalfLife             a half-life on a decay curve; a skill's strength meter at half-full
B08_HalfLifeRegression   a word's history goes into the model and a predicted half-life comes out
B09_DidItWork            two error bars, then "mixed": a flat line and a down arrow
B10_Birdbrain            a ladder of exercises, a guess for each, and the just-right rungs
B11_FallsShort           what the model sees (inside the app) and what it does not

Simple drawn shapes only: no Duolingo logo, owl, app screenshots or other branding. Every bar, meter
and gauge is an illustration, not data: no numbers, no percentages. Japanese text is set in
Hiragino Sans on purpose: the default font has no kana glyphs.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings
measured from each beat's narration audio (faster-whisper), so re-check them if that audio is
regenerated.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
DUR = {"B02": 16.02, "B04": 12.31, "B05": 17.39, "B06": 15.96, "B07": 19.18, "B08": 19.61,
       "B09": 8.55, "B10": 16.73, "B11": 11.09}
if (HERE / "beat_sheet.json").is_file():
    DUR = {b["beat_id"]: b["actual_duration_s"]
           for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # right / kept / the model
CRIMSON = "#E4572E"   # the one accent per beat
SLATE = "#29335C"
GOLD = "#F3A712"      # fill only, never text
MUTED = "#6B6458"     # secondary text
PALE = "#BDB3A2"      # thin structure lines
PAPER = "#EADFCB"     # card fill

SAFE_X, SAFE_Y = 6.25, 3.4
MIN_FS = 30           # smallest text allowed in a scene (at 8 units tall)
JP = "Hiragino Sans"
PORTRAIT = False
HEAD_Y = 2.9          # header centre; a 56 pt line then spans 2.5-3.3, inside the safe band


def T(text, size=40, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def J(text, size=48, color=INK, **kw):
    return Text(text, font=JP, font_size=size, color=color, weight="BOLD", **kw)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    return mob


def check_mark(x, y, s=.3, color=TEAL, w=9):
    return VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[x - s, y, 0], [x - s * .35, y - s * .75, 0], [x + s, y + s * .8, 0]])


def cross_mark(x, y, s=.28, color=INK, w=9):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], stroke_color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], stroke_color=color, stroke_width=w))


def poly(pts, color=INK, w=7):
    return VMobject(stroke_color=color, stroke_width=w, fill_opacity=0).set_points_as_corners(
        [[x, y, 0] for x, y in pts])


def card_shape(w, h, fill=PAPER, color=INK, sw=5, r=.18):
    return RoundedRectangle(width=w, height=h, corner_radius=r, stroke_color=color, stroke_width=sw,
                            fill_color=fill, fill_opacity=1)


class Timed:
    _min_fs = 999

    def setup(self):
        self.camera.background_color = CREAM
        self._min_fs = 999

    @property
    def now(self):
        return self.renderer.time

    def _scan(self):
        """Smallest visible text so far; a QC line is printed for anything under MIN_FS."""
        try:
            for m in self.mobjects:
                for s in m.get_family():
                    if isinstance(s, Text) and float(s.get_fill_opacity()) > .05 and float(s.width) > 0:
                        self._min_fs = min(self._min_fs, float(s.font_size))
                        if float(s.font_size) < MIN_FS:
                            print(f"QC {self.BEAT}: text '{s.text[:24]}' is {float(s.font_size):.0f} (< {MIN_FS})")
        except (TypeError, AttributeError):
            pass

    def go(self, t, *anims, rt=0.5):
        gap = t - self.now
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"QC {self.BEAT}: cue {t}s is late by {-gap:.2f}s")
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))
        self._scan()

    def sched(self, t, items):
        """items: [(offset_s, animation)] -> one play that starts each animation `offset_s` after t.
        Lets several cues inside one phrase land on their own words without go() running late."""
        group = AnimationGroup(*[Succession(Wait(o), a) if o > 1e-3 else a for o, a in items])
        self.go(t, group, rt=None)

    def finish(self):
        self._scan()
        gap = DUR[self.BEAT] - self.now
        if gap > 1e-3:
            self.wait(gap)
        else:
            print(f"QC {self.BEAT}: scene ends {-gap:.2f}s after its audio")
        print(f"QC {self.BEAT}: smallest text {self._min_fs:.0f}")


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because the
    runner finds scenes by that exact text, so a Scene subclass would be missed."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


# ------------------------------------------------------------------------------------------
@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        # 0-6s: a year of learning; the first days are where the mix-up starts
        axis = Arrow([-6.0, 0.2, 0], [6.1, 0.2, 0], buff=0, color=INK, stroke_width=6,
                     max_tip_length_to_length_ratio=.04)
        brace = poly([(-6.0, 1.0), (-6.0, 1.3), (6.0, 1.3), (6.0, 1.0)], MUTED, 5)
        year = T("over a year of Japanese", 52).move_to([0, 2.0, 0])
        first_tick = Line([-6.0, -.15, 0], [-6.0, .55, 0], stroke_color=CRIMSON, stroke_width=9)
        first = T("my first days", 44).move_to([-4.3, -.75, 0])
        first_band = Rectangle(width=2.6, height=.3, stroke_width=0, fill_color=GOLD, fill_opacity=.85
                               ).move_to([-4.75, .2, 0])
        now_t = T("now", 44, MUTED).move_to([5.5, -.75, 0])
        self.go(.2, Create(axis), Create(brace), FadeIn(year), rt=1.3)
        self.go(3.3, FadeIn(first_band), Create(first_tick), FadeIn(first), FadeIn(now_t), rt=.8)

        # 6.4-10.4: the two words
        stage1 = Group(axis, brace, year, first_tick, first, first_band, now_t)
        cap1 = T("two words I kept mixing up", 52).move_to([0, HEAD_Y, 0])
        cardA = card_shape(5.5, 4.4).move_to([-3.2, .1, 0])
        kA = J("します", 112).move_to([-3.2, .95, 0])
        rA = T("shimasu", 48, MUTED).move_to([-3.2, -.3, 0])
        gA = T("do", 68).move_to([-3.2, -1.3, 0])
        cardB = card_shape(5.5, 4.4).move_to([3.2, .1, 0])
        kB = J("みます", 112).move_to([3.2, .95, 0])
        rB = T("mimasu", 48, MUTED).move_to([3.2, -.3, 0])
        gB = T("look", 68).move_to([3.2, -1.3, 0])
        self.go(4.5, FadeOut(stage1), FadeIn(cap1), rt=.6)
        self.go(6.4, FadeIn(cardA), FadeIn(kA), FadeIn(rA), rt=.6)
        self.go(7.6, FadeIn(gA), rt=.4)
        self.go(8.3, FadeIn(cardB), FadeIn(kB), FadeIn(rB), rt=.6)
        self.go(9.4, FadeIn(gB), rt=.4)

        # 10.4-14.6: they come back; early visits are mistakes, later ones are right
        cap2 = T("Duolingo kept bringing them back", 52).move_to([0, HEAD_Y, 0])
        chA = J("します", 64).move_to([-5.0, 1.0, 0])
        chB = J("みます", 64).move_to([-5.0, -.6, 0])
        laneA = Line([-3.5, 1.0, 0], [6.1, 1.0, 0], stroke_color=PALE, stroke_width=5)
        laneB = Line([-3.5, -.6, 0], [6.1, -.6, 0], stroke_color=PALE, stroke_width=5)
        xsA = [-2.7, -1.5, -.1, 1.9, 4.5]
        xsB = [-3.0, -1.9, -.5, 1.5, 4.9]
        dotsA = [Dot([x, 1.0, 0], radius=.14, color=INK) for x in xsA]
        dotsB = [Dot([x, -.6, 0], radius=.14, color=INK) for x in xsB]
        leg_x = cross_mark(-4.9, -2.55, .2, INK, 8)
        leg_xt = T("still mixed up", 40).next_to(leg_x, RIGHT, buff=.3)
        leg_c = check_mark(.7, -2.55, .24, TEAL, 9)
        leg_ct = T("got it right", 40).next_to(leg_c, RIGHT, buff=.3)
        self.go(10.4, FadeOut(Group(cardA, kA, rA, gA, cardB, kB, rB, gB)), Transform(cap1, cap2), rt=.4)
        self.go(10.8, FadeIn(chA), FadeIn(chB), Create(laneA), Create(laneB), FadeIn(leg_x), FadeIn(leg_xt),
                FadeIn(leg_c), FadeIn(leg_ct), rt=.4)
        self.sched(11.2, [(i * .28, AnimationGroup(FadeIn(dotsA[i], scale=1.6, run_time=.2),
                                                   FadeIn(dotsB[i], scale=1.6, run_time=.2))) for i in range(5)])
        # the first three become crosses, the last two checks, on "until I finally got them right"
        crossesA = [cross_mark(x, 1.0, .22) for x in xsA[:3]]
        crossesB = [cross_mark(x, -.6, .22) for x in xsB[:3]]
        checksA = [check_mark(x, 1.0, .26) for x in xsA[3:]]
        checksB = [check_mark(x, -.6, .26) for x in xsB[3:]]
        self.go(12.55, *[ReplacementTransform(dotsA[i], crossesA[i]) for i in range(3)],
                *[ReplacementTransform(dotsB[i], crossesB[i]) for i in range(3)], rt=.4)
        self.go(13.6, *[ReplacementTransform(dotsA[3 + i], checksA[i]) for i in range(2)],
                *[ReplacementTransform(dotsB[3 + i], checksB[i]) for i in range(2)], rt=.5)

        # 14.66: How did it decide when?
        q = T("?", 190, CRIMSON, weight="BOLD").move_to([2.7, 0.2, 0])
        cap3 = T("How did it decide when?", 52).move_to([0, HEAD_Y, 0])
        self.go(14.66, Transform(cap1, cap3), FadeIn(q, scale=.5), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B04")
class B04_ForgettingCurve(Scene):
    def construct(self):
        title = T("How do we forget?", 56).move_to([0, HEAD_Y, 0])
        ax_y = Arrow([-5.2, -2.6, 0], [-5.2, 2.45, 0], buff=0, color=INK, stroke_width=6,
                     max_tip_length_to_length_ratio=.05)
        ax_x = Arrow([-5.2, -2.6, 0], [6.0, -2.6, 0], buff=0, color=INK, stroke_width=6,
                     max_tip_length_to_length_ratio=.035)
        ylab = T("what you remember", 44).rotate(PI / 2).move_to([-5.8, -.1, 0])
        xlab = T("time", 44).move_to([5.3, -3.15, 0])
        self.go(.1, FadeIn(title, shift=DOWN * .1), Create(ax_y), Create(ax_x), FadeIn(ylab), FadeIn(xlab), rt=1.2)

        # Ebbinghaus studied his own memory (spoken "1885" is not shown)
        nb_page = card_shape(1.7, 2.2, PAPER, INK, 5, .1).move_to([1.95, 1.35, 0])
        nb_lines = VGroup(*[Line([1.35, 1.95 - i * .35, 0], [2.55, 1.95 - i * .35, 0], stroke_color=MUTED,
                                 stroke_width=3) for i in range(5)])
        nb_rings = VGroup(*[Dot([1.22, 2.1 - i * .6, 0], radius=.07, color=INK) for i in range(3)])
        name = VGroup(T("Hermann", 48), T("Ebbinghaus", 48)).arrange(DOWN, buff=.08, aligned_edge=LEFT
                                                                    ).move_to([4.5, 1.85, 0])
        own = VGroup(T("studied his", 44), T("own memory", 44)).arrange(DOWN, buff=.08, aligned_edge=LEFT
                                                                         ).move_to([4.6, .55, 0])
        self.go(4.2, FadeIn(nb_page), Create(nb_lines), FadeIn(nb_rings), FadeIn(name), rt=.8)
        self.go(5.2, FadeIn(own, shift=UP * .1), rt=.6)

        # the curve draws itself on "described the forgetting curve ... fades away over time"
        def f(u):
            return -2.5 + 4.6 * np.exp(-3.1 * u)
        pts = [(-5.0 + 10.8 * u, f(u)) for u in np.linspace(0, 1, 90)]
        curve = poly(pts, CRIMSON, 9)
        lab = T("the forgetting curve", 42).move_to([-1.8, 1.6, 0])
        note = T("no effort to keep it", 44, MUTED).move_to([-2.7, -2.05, 0])
        self.sched(6.5, [(0, Create(curve, run_time=5.0, rate_func=linear)),
                         (.5, FadeIn(lab, shift=UP * .1, run_time=.5)),
                         (2.1, FadeIn(note, shift=UP * .1, run_time=.5))])
        self.finish()


# ------------------------------------------------------------------------------------------
def _lane_curve(xs, hs, x_end, base, height, x_start, cram=False):
    """Memory curve: starts full at each practice and decays with half-life-like constant h."""
    pts = []
    for k, x0 in enumerate(xs):
        x1 = xs[k + 1] if k + 1 < len(xs) else x_end
        for x in np.linspace(x0, x1, 28):
            pts.append((x, base + height * np.exp(-(x - x0) / hs[k])))
    return pts


@timed("B05")
class B05_SpacedRepetition(Scene):
    def construct(self):
        head = T("review slows the fade", 52).move_to([0, HEAD_Y, 0])
        baseA, HA = .3, 2.0
        baseB, HB = -2.7, 2.0
        lineA = Line([-5.5, baseA, 0], [6.1, baseA, 0], stroke_color=INK, stroke_width=5)
        lineB = Line([-5.5, baseB, 0], [6.1, baseB, 0], stroke_color=INK, stroke_width=5)
        labA = T("cramming", 44).rotate(PI / 2).move_to([-5.95, baseA + 1.0, 0])
        labB = T("spaced", 44).rotate(PI / 2).move_to([-5.95, baseB + 1.0, 0])

        # 0.3: the plain fade
        fade = poly([(x, baseA + HA * np.exp(-(x + 5.4) / 2.1)) for x in np.linspace(-5.4, 6.0, 60)], MUTED, 7)
        self.go(.1, FadeIn(head), Create(lineA), Create(lineB), rt=.4)
        self.go(.5, Create(fade, run_time=1.7), rt=None)

        # 3.3: short practices spread out (lane B)
        xsB = [-5.2, -3.9, -2.2, -.1, 2.4, 5.4]
        gaps = [xsB[i + 1] - xsB[i] for i in range(len(xsB) - 1)]
        hsB = [g / .9 for g in gaps] + [4.0]
        blocksB = [Rectangle(width=.5, height=.4, stroke_color=INK, stroke_width=3, fill_color=TEAL,
                             fill_opacity=1).move_to([x, baseB + .24, 0]) for x in xsB]
        curveB = []
        for k, x0 in enumerate(xsB[:-1]):
            seg = poly([(x, baseB + .35 + (HB - .35) * np.exp(-(x - x0) / hsB[k]))
                        for x in np.linspace(x0, xsB[k + 1], 24)], TEAL, 8)
            curveB.append(seg)
        self.go(3.2, FadeIn(labB), FadeOut(fade), rt=.2)
        self.sched(3.4, [(k * .45, AnimationGroup(FadeIn(blocksB[k], scale=1.4, run_time=.4),
                                                  Create(curveB[k], run_time=.45))) for k in range(5)]
                   + [(2.2, FadeIn(blocksB[5], scale=1.4, run_time=.35))])
        # 6.2: cramming (lane A): one long session, then a long slide down
        blockA = Rectangle(width=1.5, height=.5, stroke_color=INK, stroke_width=3, fill_color=TEAL,
                           fill_opacity=1).move_to([-4.75, baseA + .3, 0])
        curveA = poly([(x, baseA + .45 + (HA - .45) * np.exp(-(x + 4.0) / 2.0)) for x in np.linspace(-4.0, 6.0, 60)],
                      TEAL, 8)
        self.go(6.1, FadeIn(labA, run_time=.5), FadeIn(blockA, run_time=.5), Create(curveA, run_time=.9), rt=None)

        # 7.3: the gaps between practices grow
        arrows = []
        for i in range(5):
            a = DoubleArrow([xsB[i] + .3, baseB - .3, 0], [xsB[i + 1] - .3, baseB - .3, 0], buff=0, color=MUTED,
                            stroke_width=5, max_tip_length_to_length_ratio=.18, max_stroke_width_to_length_ratio=9)
            arrows.append(a)
        gap_t = T("gaps grow", 44).move_to([0, baseB - .65, 0])
        self.sched(7.3, [(0, Transform(head, T("longer gaps work even better", 52).move_to([0, HEAD_Y, 0]),
                                       run_time=.5))]
                   + [(.3 + i * .5, GrowFromCenter(arrows[i], run_time=.4)) for i in range(5)])

        # 13.3: just before you forget -> the dip before the next practice
        dip_x = xsB[3]
        dip_y = baseB + .35 + (HB - .35) * np.exp(-gaps[2] / hsB[2])
        dot = Dot([dip_x - .02, dip_y, 0], radius=.19, color=CRIMSON)
        drop = DashedLine([dip_x - .02, dip_y, 0], [dip_x - .02, baseB + .5, 0], color=CRIMSON, stroke_width=6,
                          dash_length=.12)
        self.go(11.62, Transform(head, T("just before you forget", 52).move_to([0, HEAD_Y, 0])), rt=.5)
        self.go(13.3, FadeIn(dot, scale=2.5), Create(drop), rt=.5)
        self.go(15.3, Transform(head, T("spaced repetition", 60).move_to([0, HEAD_Y, 0])), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
def box_shape(w, h, color=INK, sw=6):
    """An open-topped box: three sides and a rim."""
    body = poly([(-w / 2, h / 2), (-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2)], color, sw)
    rim = Line([-w / 2 - .12, h / 2, 0], [w / 2 + .12, h / 2, 0], stroke_color=color, stroke_width=sw)
    fillr = Rectangle(width=w, height=h, stroke_width=0, fill_color=PAPER, fill_opacity=.55)
    return VGroup(fillr, body, rim)


def flashcard(w=1.35, h=.9):
    c = card_shape(w, h, CREAM, INK, 4, .1)
    ln = VGroup(Line([-w * .3, h * .12, 0], [w * .3, h * .12, 0], stroke_color=MUTED, stroke_width=3),
                Line([-w * .3, -h * .15, 0], [w * .12, -h * .15, 0], stroke_color=MUTED, stroke_width=3))
    return VGroup(c, ln)


@timed("B06")
class B06_LeitnerBoxes(Scene):
    def construct(self):
        title = T("flashcards in boxes", 56).move_to([0, HEAD_Y, 0])
        xs = [-4.2, 0, 4.2]
        boxes = [box_shape(3.7, 3.2).move_to([x, -.55, 0]) for x in xs]
        labels = [T("review often", 44).move_to([xs[0], 1.4, 0]),
                  T("review less often", 44).move_to([xs[1], 1.4, 0]),
                  T("review rarely", 44).move_to([xs[2], 1.4, 0])]
        card = flashcard(1.7, 1.15).move_to([xs[0], -.95, 0])
        self.go(.1, FadeIn(title), *[FadeIn(b) for b in boxes], rt=.7)
        self.go(.9, *[FadeIn(l) for l in labels], rt=.6)
        self.go(1.6, FadeIn(card, shift=DOWN * .3), rt=.6)

        self.go(3.2, Transform(title, T("the Leitner system", 60).move_to([0, HEAD_Y, 0])), rt=.5)
        # right answer: check, card moves to a box reviewed less often
        ok = check_mark(xs[0], .45, .36, TEAL, 12)
        self.go(5.2, Create(ok), rt=.5)
        self.go(6.4, FadeOut(ok), card.animate.move_to([xs[1], -.95, 0]), rt=1.2)
        # wrong answer: cross, card moves back to a box reviewed more often
        bad = cross_mark(xs[1], .45, .32, CRIMSON, 12)
        self.go(9.3, Create(bad), rt=.5)
        self.go(10.3, FadeOut(bad), card.animate.move_to([xs[0], -.95, 0]), rt=1.2)
        # every card follows the same fixed rules
        card2 = flashcard(1.7, 1.15).move_to([xs[1], -.95, 0])
        card3 = flashcard(1.7, 1.15).move_to([xs[2], -.95, 0])
        badge = T("every card, the same fixed rules", 50).move_to([0, -3.0, 0])
        self.go(13.1, FadeIn(card2, shift=DOWN * .3), FadeIn(card3, shift=DOWN * .3), rt=.5)
        self.go(13.6, FadeIn(badge, shift=UP * .1), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B07")
class B07_HalfLife(Scene):
    def construct(self):
        # chart frame, left part of a wide stage
        ox, oy = -5.0, -2.35          # origin
        W, H = 10.8, 4.5
        h_len = 3.2                   # the half-life, in x units
        def curve_y(u):               # u in x units from origin
            return oy + H * (2.0 ** (-u / h_len))
        head = T("every word has its own half-life", 50).move_to([0, HEAD_Y, 0])
        ax_y = Arrow([ox, oy, 0], [ox, oy + H + .35, 0], buff=0, color=INK, stroke_width=6,
                     max_tip_length_to_length_ratio=.05)
        ax_x = Arrow([ox, oy, 0], [ox + W, oy, 0], buff=0, color=INK, stroke_width=6,
                     max_tip_length_to_length_ratio=.035)
        ylab = T("chance of remembering", 36).rotate(PI / 2).move_to([ox - .6, oy + H / 2, 0])
        xlab = T("time", 40).move_to([ox + W - .4, oy - .5, 0])
        curve = poly([(ox + u, curve_y(u)) for u in np.linspace(0, W - .4, 90)], TEAL, 9)
        self.go(.1, FadeIn(head), Create(ax_y), Create(ax_x), FadeIn(ylab), FadeIn(xlab), rt=.9)
        self.go(1.9, Create(curve, run_time=1.0), rt=None)

        # 3.1: the half-life is the time it takes for memory strength to fall by half
        half_y = oy + H / 2
        half_line = DashedLine([ox, half_y, 0], [ox + h_len, half_y, 0], color=MUTED, stroke_width=5, dash_length=.12)
        half_tag = T("half", 40, MUTED).move_to([ox + .9, half_y - .4, 0])
        drop_line = DashedLine([ox + h_len, half_y, 0], [ox + h_len, oy, 0], color=MUTED, stroke_width=5,
                               dash_length=.12)
        span = DoubleArrow([ox, oy - .25, 0], [ox + h_len, oy - .25, 0], buff=0, color=TEAL, stroke_width=7,
                           max_tip_length_to_length_ratio=.1, max_stroke_width_to_length_ratio=9)
        span_t = T("half-life", 46, TEAL).move_to([ox + h_len / 2, oy - .75, 0])
        caption1 = T("memory strength falls by half", 42).move_to([ox + 6.3, oy + 3.55, 0])
        self.go(3.1, Create(span), FadeIn(span_t), rt=.6)
        self.sched(5.3, [(0, Create(half_line, run_time=.5)), (0, FadeIn(half_tag, run_time=.5)),
                         (.1, FadeIn(caption1, shift=UP * .1, run_time=.5)), (1.1, Create(drop_line, run_time=.5))])

        # 7.9: time since you last practiced slides until it meets the half-life
        mark = Dot([ox + .15, oy, 0], radius=.17, color=CRIMSON)
        since = T("time since you last practiced", 40).move_to([1.0, oy - .75, 0])
        self.go(7.9, FadeIn(mark, scale=2), FadeIn(since), rt=.4)
        self.go(8.5, mark.animate.move_to([ox + h_len, oy, 0]), rt=2.6)
        pt = Dot([ox + h_len, half_y, 0], radius=.17, color=CRIMSON)
        fifty = T("about fifty-fifty", 52, CRIMSON, weight="BOLD").move_to([ox + h_len + 3.0, half_y + .5, 0])
        self.go(11.6, FadeIn(pt, scale=2.5), FadeIn(fifty, shift=UP * .1), rt=.6)

        # 14.6: a skill's strength meter slips to half-full, and it's time to practice.
        # The chart steps back to a ghost of its shapes; its labels leave so no text is shrunk below the floor.
        words = Group(head, ylab, xlab, half_tag, span_t, caption1, since, fifty)
        ghost = VGroup(ax_y, ax_x, curve, half_line, drop_line, span, mark, pt)
        sk_head = T("a skill's strength meter", 48).move_to([3.2, 2.9, 0])
        track = RoundedRectangle(width=5.6, height=1.5, corner_radius=.3, stroke_color=INK, stroke_width=8,
                                 fill_opacity=0).move_to([3.3, 1.0, 0])
        fillm = Rectangle(width=5.3, height=1.2, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        fillm.align_to(track, LEFT).shift(RIGHT * .15).set_y(1.0)
        half_mark = Line([3.3, .15, 0], [3.3, 1.85, 0], stroke_color=INK, stroke_width=5)
        half_t = T("half-full", 50).move_to([3.3, -.3, 0])
        todo = T("time to practice", 60, CRIMSON, weight="BOLD").move_to([3.3, -1.7, 0])
        illus = T("illustrative meter", 34, MUTED).move_to([3.3, -2.75, 0])
        self.go(14.6, FadeOut(words), ghost.animate.scale(.5).move_to([-3.3, 0, 0]).set_stroke(opacity=.45), rt=.45)
        self.go(15.1, FadeIn(sk_head), FadeIn(track), FadeIn(fillm), rt=.6)
        self.go(16.5, fillm.animate.stretch_to_fit_width(2.65, about_edge=LEFT), FadeIn(half_mark), FadeIn(half_t),
                rt=1.0)
        self.go(18.2, FadeIn(todo, shift=UP * .1), FadeIn(illus), rt=.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B08")
class B08_HalfLifeRegression(Scene):
    def construct(self):
        head = T("predicting each word's half-life", 52).move_to([0, HEAD_Y, 0])
        card = card_shape(3.1, 2.1).move_to([-4.6, .35, 0])
        kana = J("みます", 70).move_to([-4.6, .75, 0])
        gl = T("a word", 42, MUTED).move_to([-4.6, -.05, 0])
        model = card_shape(4.3, 2.0, CREAM, TEAL, 8, .25).move_to([-.1, .2, 0])
        model_t = VGroup(T("half-life", 54, TEAL, weight="BOLD"), T("regression", 54, TEAL, weight="BOLD")
                         ).arrange(DOWN, buff=.1).move_to(model)
        chip1 = card_shape(4.0, .8, PAPER, PALE, 4, .2)
        chip1_t = T("machine learning", 38)
        chip2 = card_shape(3.0, .8, PAPER, PALE, 4, .2)
        chip2_t = T("data science", 38)
        c1 = VGroup(chip1, chip1_t.move_to(chip1)).move_to([-2.1, 1.95, 0])
        c2 = VGroup(chip2, chip2_t.move_to(chip2)).move_to([1.7, 1.95, 0])
        track = RoundedRectangle(width=2.6, height=.9, corner_radius=.2, stroke_color=PALE, stroke_width=5,
                                 fill_opacity=0).move_to([4.7, .2, 0])
        out_lab = VGroup(T("predicted", 40), T("half-life", 40)).arrange(DOWN, buff=.05).move_to([4.7, 1.55, 0])
        self.go(.1, FadeIn(head), FadeIn(card), FadeIn(kana), FadeIn(gl), FadeIn(model), FadeIn(track),
                FadeIn(out_lab), rt=.8)
        self.go(2.3, FadeIn(c1, shift=DOWN * .2), rt=.5)
        self.go(3.3, FadeIn(c2, shift=DOWN * .2), rt=.5)
        self.go(5.2, Transform(head, T("a new statistical model", 52).move_to([0, HEAD_Y, 0])), rt=.4)
        self.go(5.7, FadeIn(model_t, scale=.9), rt=.6)

        # 9.3: history with each word: seen, right, wrong
        arrow_in = Arrow([-2.95, .35, 0], [-2.4, .3, 0], buff=0, color=INK, stroke_width=6, max_tip_length_to_length_ratio=.4)
        row_labs = [T(n, 40).move_to([-5.9, -1.0 - k * .75, 0], aligned_edge=LEFT) for k, n in enumerate(("seen", "right", "wrong"))]
        self.go(9.3, Transform(head, T("its history with each word", 52).move_to([0, HEAD_Y, 0])),
                FadeIn(arrow_in), *[FadeIn(l) for l in row_labs], rt=.5)
        for k, (name, col, n, t0) in enumerate([("seen", INK, 5, 11.6), ("right", TEAL, 4, 13.4), ("wrong", CRIMSON, 2, 14.5)]):
            y = -1.0 - k * .75
            tallies = []
            for j in range(n):
                if k == 1:
                    m = check_mark(-3.6 + j * .55, y, .17, col, 7)
                elif k == 2:
                    m = cross_mark(-3.6 + j * .55, y, .15, col, 7)
                else:
                    m = Line([-3.6 + j * .55, y - .25, 0], [-3.6 + j * .55, y + .25, 0], stroke_color=col, stroke_width=8)
                tallies.append(m)
            self.sched(t0, [(j * .13, FadeIn(m, scale=1.4, run_time=.3)) for j, m in enumerate(tallies)])
        flow = VGroup(Line([-1.35, -1.85, 0], [0.0, -1.85, 0], stroke_color=INK, stroke_width=6),
                      Arrow([0.0, -1.85, 0], [0.0, -.9, 0], buff=0, color=INK, stroke_width=6,
                            max_tip_length_to_length_ratio=.3))
        self.go(15.5, FadeIn(flow), rt=.4)

        # 16.1: it predicts how long each word will last
        out_arrow = Arrow([2.15, .2, 0], [3.3, .2, 0], buff=0, color=TEAL, stroke_width=7, max_tip_length_to_length_ratio=.35)
        bar = Rectangle(width=2.4, height=.7, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        bar.align_to(track, LEFT).shift(RIGHT * .1).set_y(.2)
        lasts = VGroup(T("how long this word", 36), T("lasts in your memory", 36)).arrange(DOWN, buff=.06
                                                                                         ).move_to([3.9, -1.2, 0])
        lasts.set_x(3.9)
        bar.stretch_to_fit_width(.1, about_edge=LEFT)
        self.go(16.1, Transform(head, T("how long each word will last", 52).move_to([0, HEAD_Y, 0])),
                GrowArrow(out_arrow), rt=.5)
        self.go(16.6, FadeIn(bar), rt=.2)
        self.go(17.0, bar.animate.stretch_to_fit_width(2.4, about_edge=LEFT), FadeIn(lasts), rt=1.6)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B09")
class B09_DidItWork(Scene):
    def construct(self):
        head = T("Did it work?", 64).move_to([0, HEAD_Y, 0])
        sub = T("prediction error", 54).move_to([0, 2.0, 0])
        labL = T("Leitner", 54).move_to([-6.0, 1.3, 0], aligned_edge=LEFT)
        labH = T("half-life regression", 54).move_to([-6.0, -.45, 0], aligned_edge=LEFT)
        trackL = Rectangle(width=11.8, height=.8, stroke_color=PALE, stroke_width=3, fill_opacity=0
                           ).move_to([-.1, .55, 0]).align_to([-6.0, 0, 0], LEFT)
        trackH = trackL.copy().set_y(-1.3)
        barL = Rectangle(width=11.8, height=.8, stroke_width=0, fill_color=GOLD, fill_opacity=1)
        barL.align_to(trackL, LEFT).set_y(.55)
        barH = Rectangle(width=11.8 * .545, height=.8, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        barH.align_to(trackL, LEFT).set_y(-1.3)
        cap = T("as reported by Duolingo", 42, MUTED).move_to([0, -2.55, 0])
        self.go(.05, FadeIn(head), rt=.4)
        self.go(1.0, FadeIn(sub), FadeIn(labL), FadeIn(labH), Create(trackL), Create(trackH), rt=.6)
        barL.stretch_to_fit_width(.1, about_edge=LEFT)
        barH.stretch_to_fit_width(.1, about_edge=LEFT)
        self.go(2.3, FadeIn(barL), FadeIn(barH), FadeIn(cap), rt=.1)
        self.go(2.4, barL.animate.stretch_to_fit_width(11.8, about_edge=LEFT),
                barH.animate.stretch_to_fit_width(11.8 * .545, about_edge=LEFT), rt=1.8)

        # 6.0: tests with real learners were more mixed
        stage1 = Group(head, sub, labL, labH, trackL, trackH, barL, barH, cap)
        h2 = T("tests with real learners", 60).move_to([0, HEAD_Y, 0])
        mixed = T("mixed", 150, CRIMSON, weight="BOLD").move_to([0, 1.3, 0])
        rowA = T("overall activity", 50).move_to([-3.2, -.7, 0])
        flat = Line([-5.8, -1.65, 0], [-.6, -1.65, 0], stroke_color=INK, stroke_width=11)
        rowB = T("practice sessions", 50).move_to([3.2, -.7, 0])
        down = Arrow([3.2, -1.15, 0], [3.2, -2.9, 0], buff=0, color=INK, stroke_width=14, max_tip_length_to_length_ratio=.3)
        axisA = Line([-5.8, -1.65, 0], [-.6, -1.65, 0], stroke_color=PALE, stroke_width=4)
        self.go(6.0, FadeOut(stage1), FadeIn(h2), rt=.4)
        self.go(6.5, FadeIn(rowA), FadeIn(rowB), Create(flat), GrowArrow(down), rt=.7)
        self.go(7.85, FadeIn(mixed, scale=.8), rt=.4)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B10")
class B10_Birdbrain(Scene):
    def construct(self):
        N = 7
        x0, w = -.6, 5.4
        ys = [-2.95 + i * .7 for i in range(N)]           # easiest at the bottom
        gauge_fill = [.95, .88, .78, .62, .45, .28, .14]    # illustrative guesses
        blocks = [RoundedRectangle(width=w, height=.58, corner_radius=.14, stroke_color=INK, stroke_width=4,
                                   fill_color=PAPER, fill_opacity=1).move_to([x0, y, 0]) for y in ys]
        ups = Arrow([-3.55, ys[0], 0], [-3.55, ys[-1], 0], buff=0, color=MUTED, stroke_width=5,
                    max_tip_length_to_length_ratio=.06)
        easy = T("easy", 40, MUTED).move_to([-3.95, ys[0], 0], aligned_edge=RIGHT)
        hard = T("hard", 40, MUTED).move_to([-3.95, ys[-1], 0], aligned_edge=RIGHT)
        head = T("Birdbrain", 56, TEAL, weight="BOLD").move_to([-4.5, 2.85, 0])
        later = T("another model", 40, MUTED).move_to([-4.5, 2.2, 0])
        model = card_shape(2.3, 1.45, CREAM, TEAL, 7, .22).move_to([-4.85, -.5, 0])
        model_t = VGroup(T("will you get", 36), T("it right?", 36)).arrange(DOWN, buff=.05).move_to(model)
        self.go(.1, FadeIn(head), rt=.5)
        self.go(1.4, FadeIn(later), rt=.5)
        self.go(2.7, FadeIn(model), FadeIn(model_t), rt=.6)

        # 4.0: an educated guess about each exercise
        self.go(4.0, LaggedStart(*[FadeIn(b, shift=RIGHT * .2) for b in blocks], lag_ratio=.12), FadeIn(ups),
                FadeIn(easy), FadeIn(hard), rt=1.2)
        gauges = []
        for i, y in enumerate(ys):
            ring = Circle(radius=.22, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([x0 + w / 2 - .4, y, 0])
            sec = Sector(radius=.22, angle=TAU * gauge_fill[i], start_angle=PI / 2, stroke_width=0, fill_color=TEAL,
                         fill_opacity=1, arc_center=ring.get_center())
            gauges.append(VGroup(ring, sec))
        key = VGroup(T("fuller dial:", 42), T("more likely right", 42)).arrange(DOWN, buff=.06).move_to([4.35, -.65, 0])
        self.go(5.2, LaggedStart(*[FadeIn(g, scale=1.5) for g in gauges], lag_ratio=.18), FadeIn(key), rt=1.6)

        # 10.1: the middle rungs are just right
        tag_x = 4.35
        mid = SurroundingRectangle(VGroup(*blocks[2:5]), color=CRIMSON, buff=.1, stroke_width=8, corner_radius=.18)
        mid_t = VGroup(T("just the right", 44, CRIMSON, weight="BOLD"), T("difficulty", 44, CRIMSON, weight="BOLD")
                       ).arrange(DOWN, buff=.05).move_to([tag_x, (ys[2] + ys[4]) / 2, 0])
        self.go(10.1, Create(mid), FadeOut(key), FadeIn(mid_t, shift=LEFT * .2), rt=.8)
        # 11.9: too hard -> frustrated (top rungs)
        hard_t = VGroup(T("too hard:", 42), T("frustrated", 42)).arrange(DOWN, buff=.05, aligned_edge=LEFT
                                                                           ).move_to([tag_x, (ys[5] + ys[6]) / 2, 0])
        hard_t.set_x(tag_x)
        easy_t = VGroup(T("too easy:", 42), T("already mastered", 42)).arrange(DOWN, buff=.05, aligned_edge=LEFT
                                                                            ).move_to([tag_x, (ys[0] + ys[1]) / 2, 0])
        easy_t.set_x(tag_x)
        self.go(11.9, FadeIn(hard_t, shift=LEFT * .2), *[b.animate.set_opacity(.55) for b in blocks[5:]], rt=.7)
        self.go(13.9, FadeIn(easy_t, shift=LEFT * .2), *[b.animate.set_opacity(.55) for b in blocks[:2]], rt=.7)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B11")
class B11_FallsShort(Scene):
    def construct(self):
        view = T("In my view", 62, MUTED, slant="ITALIC").move_to([-3.3, HEAD_Y, 0])
        app = card_shape(5.6, 4.6, PAPER, INK, 7, .3).move_to([-3.3, -.2, 0])
        app_t = VGroup(T("inside the app:", 50), T("what I do", 50)).arrange(DOWN, buff=.1).move_to([-3.3, 1.2, 0])
        ticks = VGroup(*[check_mark(-5.1 + (i % 4) * 1.15, -.3 - (i // 4) * .9, .22, TEAL, 8) for i in range(8)])
        wall = DashedLine([.15, 2.4, 0], [.15, -2.6, 0], color=PALE, stroke_width=6, dash_length=.18)
        limits = T("it has limits", 62, MUTED).move_to([-3.3, HEAD_Y, 0])
        self.go(.2, FadeIn(limits), rt=.5)
        self.go(1.4, ReplacementTransform(limits, view), rt=.5)
        self.go(2.1, FadeIn(app), FadeIn(app_t), rt=.7)
        self.go(2.9, LaggedStart(*[FadeIn(t, scale=1.4) for t in ticks], lag_ratio=.15), rt=1.4)

        # what it does not see
        items = ["my interests", "Japanese I use somewhere else", "a mistake while speaking"]
        cues = [5.16, 6.42, 9.12]
        ys = [1.7, -.2, -2.1]
        outs = []
        notseen = T("not seen", 44, MUTED)
        for text, y in zip(items, ys):
            box = RoundedRectangle(width=5.7, height=1.55, corner_radius=.25, stroke_color=INK, stroke_width=6,
                                   fill_opacity=0).move_to([3.3, y, 0])
            dash = DashedVMobject(box, num_dashes=40, dashed_ratio=.55)
            parts = text.split(" I use ")
            two = {"Japanese I use somewhere else": ("Japanese I use", "somewhere else"),
                   "a mistake while speaking": ("a mistake", "while speaking")}
            label = (VGroup(T(two[text][0], 44), T(two[text][1], 44)).arrange(DOWN, buff=.05)
                     if text in two else T(text, 48)).move_to(box)
            cross = cross_mark(5.75, y + .45, .17, CRIMSON, 7)
            outs.append(VGroup(dash, label, cross))
        self.go(4.5, Create(wall), FadeIn(notseen.move_to([3.3, HEAD_Y, 0])), rt=.5)
        for o, c in zip(outs, cues):
            self.go(c, FadeIn(o, shift=LEFT * .2), rt=.6)
        self.finish()
