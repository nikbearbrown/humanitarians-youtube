"""Native 9:16 layouts for "How AI Draws Anime Frames" (Keya G.).

Same scene names, content, colours and go() cues as ../scenes.py, rearranged for a tall
frame (4.5 x 8 Manim units at 2160x3840). Nothing here is a crop of the landscape film.

Simple abstract shapes only: no frames or characters from Naruto or any real anime.
Each scene's length comes from actual_duration_s in beat_sheet.json.
"""
import json
import math
import random
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the
# 16:9 default (14.22); make it 4.5 so the frame is 4.5 x 8 units.
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass
# beat_sheet.json is the master clock. The fallback is its measured values, for run.sh's
# Gate A, which checks a copy of this file in a folder without the sheet.
DUR = {"B01": 17.66, "B03": 20.42, "B04": 20.12, "B05": 18.71, "B06": 25.3, "B07": 19.22, "B08": 23.7}
if (HERE / "beat_sheet.json").is_file():
    DUR = {b["beat_id"]: b["actual_duration_s"]
           for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"
CRIMSON = "#E4572E"
SLATE = "#29335C"
GOLD = "#F3A712"
SAGE = "#A8C686"

# Just inside the portrait safe band Gate B enforces (1.95 x 3.4).
SAFE_X, SAFE_Y = 1.85, 3.3
WIDE = SAFE_X * 2


def T(text, size=40, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def centred(lines, size, color=INK, buff=.1):
    return VGroup(*[T(line, size, color) for line in lines]).arrange(DOWN, buff=buff)


def left_at(mob, x, y):
    return mob.move_to([x + mob.width / 2, y, 0])


class Timed:
    """Narration-clock helpers: go(t, ...) starts animations at t seconds."""

    def setup(self):
        self.camera.background_color = CREAM
        self._reported = set()

    @property
    def now(self):
        return self.renderer.time

    def go(self, t, *anims, rt=0.5):
        """rt=None lets each animation keep its own run_time."""
        gap = t - self.now
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"QC {self.BEAT}: cue {t}s is late by {-gap:.2f}s")
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))

    def finish(self):
        gap = DUR[self.BEAT] - self.now
        if gap > 1e-3:
            self.wait(gap)

    def driven(self, mob, t0, t1, fn):
        """Run fn(mob, alpha) from t0 to t1 while other cues play."""
        def update(m):
            a = min(max((self.now - t0) / (t1 - t0), 0), 1)
            fn(m, a)
            if a >= 1:
                m.remove_updater(update)
        mob.add_updater(update)
        return mob


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because
    run.sh finds scenes by that exact text."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


def token(color=SLATE, scale=1.0):
    """The film's one abstract 'drawing': a plain star, so it can never read as a person."""
    return Star(n=5, outer_radius=.62, inner_radius=.28, fill_color=color, fill_opacity=1,
                stroke_width=0).scale(scale)


def panel(x, y, w, h, stroke=INK, width=3):
    return RoundedRectangle(corner_radius=.1, width=w, height=h, stroke_color=stroke,
                            stroke_width=width, fill_opacity=0).move_to([x, y, 0])


def check(at, size=.5, color=TEAL):
    pts = [at + np.array([-.5, 0, 0]) * size, at + np.array([-.1, -.45, 0]) * size,
           at + np.array([.6, .55, 0]) * size]
    return VMobject(stroke_color=color, stroke_width=10).set_points_as_corners(pts)


@timed("B01")
class B01_WouldYouStillLove(Scene):
    def construct(self):
        # Two copies of one shape cross the frame: held drawings vs a glide.
        start, end = -1.15, 1.15
        top = token(TEAL).move_to([start, 1.55, 0])
        bot = token(CRIMSON).move_to([start, -1.1, 0])
        top_label = left_at(T("drawn, then held", 40), -SAFE_X, 2.85)
        bot_label = left_at(T("AI-smoothed", 40), -SAFE_X, .2)
        unnatural = T("unnatural", 60, CRIMSON).move_to([0, -2.6, 0])
        self.add(top, bot, top_label)

        def stepped(m, a):
            m.set_x(start + (end - start) * math.floor(a * 7) / 7)

        def glide(m, a):
            m.set_x(start + (end - start) * a)
        self.driven(top, .2, 4.0, stepped)
        self.driven(bot, .2, 4.0, glide)
        self.go(1.14, FadeIn(bot_label))
        self.go(2.8, FadeIn(unnatural, scale=1.15))

        # Toei: AI for the slots between two drawings. The strip of slots stands upright.
        lanes = VGroup(top, bot, top_label, bot_label, unnatural)
        self.go(4.18, FadeOut(lanes), rt=.5)
        head = centred(["AI for in-between", "frames"], 40).move_to([0, 2.65, 0])
        # Above Gate T's 9:16 text floor (bottom 14% stays clear for phone players).
        source = T("Anime Corner, 2025", 34).move_to([0, -2.55, 0])
        ys = [1.62 - i * .6 for i in range(7)]
        slots = VGroup(*[DashedVMobject(panel(0, y, 2.6, .54), num_dashes=30) for y in ys])
        keys = VGroup(token(SLATE, .36).move_to([0, ys[0], 0]), token(SLATE, .36).move_to([0, ys[-1], 0]))
        self.go(4.94, Create(slots), FadeIn(keys), rt=1)
        self.go(6.84, FadeIn(source))
        self.go(9.74, FadeIn(head))
        fills = VGroup(*[token(TEAL, .36).move_to([0, y, 0]) for y in ys[1:-1]])
        self.go(10.66, LaggedStart(*[FadeIn(f, scale=.7) for f in fills], lag_ratio=.5), rt=1.1)

        # The question is the last thing on screen.
        self.go(12.5, FadeOut(VGroup(head, source, slots, keys, fills)), rt=.45)
        if_line = centred(["If AI drew your", "favourite anime", "on its own,"], 44).move_to([0, 1.95, 0])
        # An empty slot holds the lower half until the second line lands in it.
        slot = DashedVMobject(panel(0, -1.4, 3.65, 3.2), num_dashes=50)
        love = centred(["would you", "still love it", "the same way?"], 44, TEAL).move_to([0, -1.4, 0])
        self.go(13.04, FadeIn(if_line, shift=UP * .1), FadeIn(slot), rt=.6)
        self.go(15.94, FadeIn(love, shift=UP * .1), rt=.6)
        self.finish()


@timed("B03")
class B03_KeyFrames(Scene):
    def construct(self):
        def arc(a):
            # The whole lower assembly sits .65 higher so the timeline's last row clears
            # Gate T's 9:16 text floor.
            p0, p1, p2 = np.array([-1.35, .2, 0]), np.array([-.35, 3.6, 0]), np.array([.85, .2, 0])
            return (1 - a) ** 2 * p0 + 2 * a * (1 - a) * p1 + a ** 2 * p2

        def pose(a, color, opacity=1.0):
            d = arc(min(a + .01, 1)) - arc(max(a - .01, 0))
            return RoundedRectangle(corner_radius=.15, width=.56, height=.32, fill_color=color,
                                    fill_opacity=opacity, stroke_width=0).rotate(math.atan2(d[1], d[0])).move_to(arc(a))

        tp = [0, 2.72, 0]
        title = centred(["Hand-drawn", "animation"], 50).move_to(tp)
        self.go(.4, FadeIn(title))
        title2 = centred(["Every scene starts", "with key frames"], 38).move_to(tp)
        # The nine-frame timeline wraps onto three rows, read left to right.
        cw, ch = WIDE / 3, .58
        cells = VGroup(*[Rectangle(width=cw - .06, height=ch - .06, stroke_color=INK, stroke_width=2,
                                   fill_color=CREAM, fill_opacity=1)
                         .move_to([-SAFE_X + cw * (i % 3 + .5), -1.3 - (i // 3) * ch, 0])
                         for i in range(9)])
        self.go(2.56, FadeOut(title), FadeIn(cells), rt=.5)
        self.go(3.1, FadeIn(title2))
        key_cells = [cells[0], cells[-1]]
        key_words = VGroup(*[T("key", 34, CREAM).move_to(c) for c in key_cells])
        self.go(3.98, *[c.animate.set_fill(SLATE) for c in key_cells], FadeIn(key_words))

        block = Rectangle(width=.5, height=1.5, fill_color=INK, fill_opacity=1,
                          stroke_width=0).move_to([1.55, .7, 0])
        p1 = pose(0, SLATE)
        launch = T("launch", 38).move_to([-1.2, -.5, 0])
        self.go(9.18, FadeIn(p1, scale=1.2), FadeIn(launch))
        p2 = pose(1, SLATE)
        lands = T("lands", 38).move_to([.85, -.5, 0])
        self.go(11.1, FadeIn(block), FadeIn(p2, scale=1.2), FadeIn(lands))

        # The in-betweens fill the arc and the timeline, one at a time.
        title3 = centred(["In-betweens", "connect them"], 46).move_to(tp)
        self.go(12.68, FadeOut(title2), FadeIn(title3))
        ghosts = VGroup(*[pose((i + 1) / 8, SLATE, .42) for i in range(7)])
        self.go(13.2, LaggedStart(*[AnimationGroup(FadeIn(g), cells[i + 1].animate.set_fill(SLATE, .42))
                                    for i, g in enumerate(ghosts)], lag_ratio=.6), rt=2.3)
        # Those drawings are the ones AI is asked to make.
        title4 = centred(["What AI is asked", "to draw"], 44, TEAL).move_to(tp)
        self.go(16.36, FadeOut(title3), FadeIn(title4),
                *[g.animate.set_fill(TEAL, 1) for g in ghosts],
                *[c.animate.set_fill(TEAL, 1) for c in cells[1:-1]], rt=.8)
        self.finish()


@timed("B04")
class B04_OnesTwosThrees(Scene):
    def strip(self, y, h):
        cell = WIDE / 24
        return VGroup(*[Rectangle(width=cell, height=h, stroke_color=CREAM, stroke_width=2,
                                  fill_color=SLATE, fill_opacity=.42).move_to([-SAFE_X + cell * (i + .5), y, 0])
                        for i in range(24)])

    def holds(self, cells, n):
        """Same-coloured runs of cells are one drawing, held for n frames."""
        return [c.animate.set_fill(TEAL if (i // n) % 2 == 0 else SAGE, 1) for i, c in enumerate(cells)]

    def playhead(self, y, n, t0, seconds=2.0, sweeps=1):
        cell = WIDE / 24
        tri = Triangle(fill_color=CRIMSON, fill_opacity=1, stroke_width=0).scale(.11)
        tri.move_to([-SAFE_X + cell * n / 2, y, 0])

        def step(m, a):
            pos = (a * sweeps) % 1 if a < 1 else .999
            m.set_x(-SAFE_X + cell * (math.floor(pos * 24 / n) * n + n / 2))
        self.driven(tri, t0, t0 + seconds * sweeps, step)
        return tri

    def construct(self):
        base = self.strip(.35, 1.5)
        head = centred(["24 frames =", "one second"], 56).move_to([0, 2.2, 0])
        self.add(base)
        self.go(.98, FadeIn(head))
        rarely = centred(["anime rarely", "draws all 24"], 50).move_to([0, -1.6, 0])
        self.go(3.12, FadeIn(rarely))

        ys = (2.3, .6, -1.3)
        size, up = 32, .5
        self.go(5.52, FadeOut(head), FadeOut(rarely),
                base.animate.stretch_to_fit_height(.5).move_to([0, ys[0], 0]), rt=.7)
        twos = left_at(T("on twos", size), -SAFE_X, ys[0] + up)
        self.go(6.7, FadeIn(twos), *self.holds(base, 2), rt=.5)

        row3 = self.strip(ys[1], .5)
        threes = left_at(T("on threes", size), -SAFE_X, ys[1] + up)
        # The third row waits as an empty outline until its cue.
        cell = WIDE / 24
        outline = VGroup(*[Rectangle(width=cell, height=.5, stroke_color=INK, stroke_width=2, fill_opacity=0)
                           .move_to([-SAFE_X + cell * (i + .5), ys[2], 0]) for i in range(24)])
        self.go(7.3, FadeIn(row3), FadeIn(threes), FadeIn(outline), *self.holds(row3, 3), rt=.5)
        # The same sweep on both rows: the mark hangs longer on threes.
        self.add(self.playhead(ys[0] - .36, 2, 8.3), self.playhead(ys[1] - .36, 3, 8.3))
        twos2 = left_at(T("on twos: 12 drawings", size), -SAFE_X, ys[0] + up)
        self.go(11.38, FadeOut(twos, run_time=.3), FadeIn(twos2, run_time=.3), rt=None)
        threes2 = left_at(T("on threes: just 8", size), -SAFE_X, ys[1] + up)
        self.go(11.72, FadeOut(threes, run_time=.3), FadeIn(threes2, run_time=.3), rt=None)

        row1 = self.strip(ys[2], .5)
        ones = left_at(T("on ones", size), -SAFE_X, ys[2] + up)
        self.go(13.56, FadeIn(row1), FadeOut(outline))
        self.go(15.8, FadeIn(ones), *self.holds(row1, 1), rt=.4)
        self.add(self.playhead(ys[2] - .36, 1, 15.8, seconds=.5, sweeps=2))
        ones2 = left_at(T("on ones: all 24", size), -SAFE_X, ys[2] + up)
        self.go(16.3, FadeOut(ones, run_time=.3), FadeIn(ones2, run_time=.3), rt=None)

        # Two lines, revealed in parts.
        choice = T("a choice about", 46).move_to([0, -2.25, 0])
        line = T("budget and feel", 46).move_to([0, -2.9, 0])
        budget, andword, feel = line[:6], line[6:9], line[9:13]
        budget.set_color(TEAL)
        feel.set_color(TEAL)
        self.go(17.9, FadeIn(choice))
        self.go(18.86, FadeIn(budget), rt=.4)
        self.go(19.44, FadeIn(andword), FadeIn(feel), rt=.4)
        self.finish()


@timed("B05")
class B05_OpticalFlow(Scene):
    def construct(self):
        rng = random.Random(7)
        # The three frames stack top to bottom; the arrows run downward.
        # Tighter than before so the caption below clears Gate T's 9:16 text floor.
        w, h = 3.7, 1.2
        top_y, mid_y, bot_y = 2.15, .5, -1.15
        frames = VGroup(*[panel(0, y, w, h) for y in (top_y, bot_y)])
        middle = DashedVMobject(panel(0, mid_y, w, h), num_dashes=40)
        # Labels sit in the left of the gaps; arrows only use the right, so never cross them.
        labels = VGroup(left_at(T("frame 1", 36), -SAFE_X, 3.08), left_at(T("frame 2", 36), -SAFE_X, -.33))

        # p = where a pixel sits; v = how far it moves between the frames.
        points = []
        for _ in range(70):
            points.append((np.array([rng.uniform(-1.7, 1.6), rng.uniform(-.5, .5), 0]),
                           np.array([.06, .02, 0]), False))
        for _ in range(30):
            a, r = rng.uniform(0, math.tau), .36 * math.sqrt(rng.random())
            points.append((np.array([.15 + r * math.cos(a), r * math.sin(a), 0]),
                           np.array([.95, .12, 0]), True))

        def dot(c, big):
            return Dot(c, radius=.05 if big else .03, color=SLATE if big else INK,
                       fill_opacity=1 if big else .55)

        top_c, bot_c = np.array([0, top_y, 0]), np.array([0, bot_y, 0])
        top_dots = VGroup(*[dot(top_c + p, big) for p, v, big in points])
        bot_dots = VGroup(*[dot(bot_c + p + v, big) for p, v, big in points])
        self.add(frames, labels, top_dots, bot_dots)
        self.go(.8, Create(middle), rt=.8)

        cap_y = -2.32
        word = T("optical flow", 56, TEAL).move_to([0, cap_y, 0])
        self.go(3.32, FadeIn(word))
        # Straight from a dot in frame 1 to the same dot in frame 2.
        chosen = list(range(70, 82)) + [i for i, (p, v, big) in enumerate(points) if not big and p[0] > .1][:6]
        arrows = VGroup(*[Arrow(top_dots[i].get_center(), bot_dots[i].get_center(), buff=0, stroke_width=3,
                                tip_length=.13, color=TEAL, max_stroke_width_to_length_ratio=100)
                          for i in chosen])
        sub = centred(["where each", "pixel moved"], 38).move_to([0, cap_y, 0])
        self.go(4.88, LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=.12, run_time=3.4),
                FadeOut(word, run_time=.4), FadeIn(sub, run_time=.4), rt=None)

        # Halfway along each arrow is that dot's place in the new frame.
        new_label = left_at(T("new frame", 36, TEAL), -SAFE_X, 1.33)
        halfway = centred(["follow the arrows", "halfway"], 38).move_to([0, cap_y, 0])
        self.go(9.3, FadeOut(sub), FadeIn(halfway), rt=.4)
        movers = VGroup(*[d.copy() for d in top_dots])
        self.add(movers)
        targets = [(np.array(top_dots[i].get_center()) + np.array(bot_dots[i].get_center())) / 2
                   for i in range(len(points))]
        self.go(9.96, *[m.animate.move_to(c) for m, c in zip(movers, targets)], rt=2.3)
        self.go(12.3, FadeIn(new_label))

        # Live action has texture everywhere, so this holds up.
        live = centred(["live action:", "lots of texture"], 38).move_to([0, cap_y, 0])
        self.go(13.48, FadeOut(arrows), FadeOut(halfway), rt=.45)
        self.go(14.0, FadeIn(live), rt=.45)
        works = centred(["works", "surprisingly well"], 34, TEAL)
        tick = check(np.array([0, 0, 0]), .45)
        VGroup(tick, works).arrange(RIGHT, buff=.15).move_to([0, cap_y, 0])
        self.go(17.0, FadeOut(live), FadeIn(works), Create(tick), rt=.4)
        self.finish()


@timed("B06")
class B06_ThreeBreaks(Scene):
    def construct(self):
        # Three panels stacked; the band above them waits for "the result".
        # Shorter panels so the last one ends above Gate T's 9:16 text floor.
        ys = (1.8, -.05, -1.9)
        w, h = 3.7, 1.7
        boxes = VGroup(*[panel(0, y, w, h) for y in ys])
        heads = [left_at(T(s, 36), -1.72, y + .6) for s, y in
                 zip(("flat colors", "big movement", "hidden parts"), ys)]
        self.go(.3, Create(boxes), rt=.7)

        # 1. A flat sleeve: no texture, so the flow arrows have nothing to hold on to.
        y = ys[0]
        rng = random.Random(3)
        self.go(2.5, FadeIn(heads[0]), rt=.4)
        sleeve = Rectangle(width=1.3, height=.95, fill_color=SLATE, fill_opacity=1,
                           stroke_width=0).move_to([-1.05, y - .22, 0])
        self.go(3.66, FadeIn(sleeve))
        cap1 = T("no texture", 32, CRIMSON).move_to([.8, y - .22, 0])
        self.go(5.2, FadeIn(cap1))
        arrows = VGroup()
        for _ in range(9):
            a = np.array([rng.uniform(-1.6, -.5), y + rng.uniform(-.62, .15), 0])
            b = np.array([rng.uniform(-1.75, -.3), y + rng.uniform(-.78, .38), 0])
            arrows.add(Arrow(a, b, buff=0, stroke_width=3, tip_length=.12, color=CRIMSON,
                             max_stroke_width_to_length_ratio=100))
        self.go(6.72, LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=.15), rt=1.6)

        # 2. A long curved jump: the real path bends, the straight guess misses.
        y = ys[1]
        self.go(9.24, FadeIn(heads[1]), rt=.4)
        p0, p1, p2 = [np.array(v, float) for v in ([-1.6, y - .62, 0], [-1.6, y + .35, 0], [-.15, y + .15, 0])]
        path = VMobject(stroke_color=TEAL, stroke_width=5)
        path.set_points_as_corners([(1 - a) ** 2 * p0 + 2 * a * (1 - a) * p1 + a ** 2 * p2
                                    for a in np.linspace(0, 1, 40)])
        fist = Circle(radius=.18, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to(p0)
        self.go(10.4, FadeIn(fist))
        self.go(13.7, Create(path), MoveAlongPath(fist, path), rt=3.1)
        guess_mid = (p0 + p2) / 2
        guess = DashedLine(p0, guess_mid, color=CRIMSON, stroke_width=5, dash_length=.1)
        miss = Cross(Circle(radius=.13).move_to(guess_mid), stroke_color=CRIMSON, stroke_width=7)
        cap2 = centred(["the guess", "misses"], 32, CRIMSON).move_to([.9, y - .22, 0])
        self.go(16.82, Create(guess), Create(miss), FadeIn(cap2), rt=.6)

        # 3. A hand slips behind the body: nothing to match it to.
        y = ys[2]
        self.go(17.54, FadeIn(heads[2]), rt=.4)
        hand = Circle(radius=.2, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to([-1.4, y - .5, 0])
        hand_label = T("hand", 32).move_to([-1.4, y - .08, 0])
        body = RoundedRectangle(corner_radius=.1, width=.95, height=1.1, fill_color=SLATE, fill_opacity=1,
                                stroke_width=0).move_to([-.45, y - .25, 0])
        body_label = T("body", 32, CREAM).move_to([-.45, y + .08, 0])
        self.go(17.95, FadeIn(hand), FadeIn(hand_label), FadeIn(body), FadeIn(body_label), rt=.5)
        self.bring_to_back(hand)
        outline = DashedVMobject(Circle(radius=.2, stroke_color=TEAL, stroke_width=4).move_to(hand.get_center()),
                                 num_dashes=12)
        self.add(outline)
        self.go(19.38, hand.animate.move_to([-.45, y - .55, 0]), FadeOut(hand_label), rt=.7)
        cap3 = centred(["no", "match"], 32, CRIMSON).move_to([1.05, y - .22, 0])
        self.go(20.64, FadeIn(cap3), rt=.4)

        # The errors those breaks leave in the drawn frame.
        panel1 = VGroup(sleeve, arrows, cap1, heads[0])
        panel2 = VGroup(path, fist, guess, miss, cap2, heads[1])
        panel3 = VGroup(hand, outline, body, body_label, cap3, heads[2])
        result = T("the result", 46).move_to([0, 3.02, 0])
        self.go(21.5, FadeOut(panel1), FadeOut(panel2), FadeOut(panel3), rt=.35)
        self.go(21.9, FadeIn(result), rt=.3)

        def figure(x, y, color=SLATE, opacity=1.0, limbs=2):
            c = np.array([x, y, 0])
            core = Circle(radius=.33, fill_color=color, fill_opacity=opacity, stroke_width=0).move_to(c)
            parts = VGroup(core)
            for i in range(limbs):
                ang = -PI / 2 + (i - (limbs - 1) / 2) * 1.15
                limb = RoundedRectangle(corner_radius=.06, width=.7, height=.14, fill_color=color,
                                        fill_opacity=opacity, stroke_width=0).rotate(ang)
                limb.move_to(c + np.array([math.cos(ang), math.sin(ang), 0]) * .56)
                parts.add(limb)
            return parts

        fx, wx = -.95, .95
        fy = [y + .18 for y in ys]
        ghost = VGroup(figure(fx - .3, fy[0], CRIMSON, .28), figure(fx + .3, fy[0], CRIMSON, .28), figure(fx, fy[0]))
        blur = VGroup(figure(fx + .15, fy[1]))
        for i in range(8):
            blur.add(Rectangle(width=.13, height=.66 - i * .05, fill_color=CRIMSON,
                               fill_opacity=.72 - i * .08, stroke_width=0)
                     .move_to([fx + .15 - .36 - i * .09, fy[1], 0]))
        extra = VGroup(figure(fx, fy[2]))
        for ang in (-PI / 2, .55, PI - .55):
            limb = RoundedRectangle(corner_radius=.06, width=.7, height=.14, fill_color=CRIMSON, fill_opacity=1,
                                    stroke_width=0).rotate(ang)
            limb.move_to(np.array([fx, fy[2], 0]) + np.array([math.cos(ang), math.sin(ang), 0]) * .56)
            extra.add(limb)
        words = [centred(s, 34, CRIMSON).move_to([wx, y, 0]) for s, y in zip((["ghosting"], ["blur"], ["extra", "limbs"]), ys)]
        self.go(22.84, FadeIn(ghost), FadeIn(words[0]), rt=.35)
        self.go(23.68, FadeIn(blur), FadeIn(words[1]), rt=.35)
        self.go(24.5, FadeIn(extra), FadeIn(words[2]), rt=.35)
        self.finish()


@timed("B07")
class B07_TimingWiped(Scene):
    def blocks(self, y, h):
        holds = [2, 2, 3, 1, 1, 1, 4, 2, 2, 3, 3]
        cell, x, out = WIDE / 24, -SAFE_X, VGroup()
        for i, n in enumerate(holds):
            out.add(Rectangle(width=cell * n, height=h, stroke_color=CREAM, stroke_width=2.5,
                              fill_color=TEAL if i % 2 == 0 else SAGE, fill_opacity=1)
                    .move_to([x + cell * n / 2, y, 0]))
            x += cell * n
        return out

    def construct(self):
        y1, y2, h = 2.1, -.85, .85
        top = self.blocks(y1, h)
        top_label = left_at(T("the animator’s timing", 32), -SAFE_X, y1 + .72)
        self.add(top, top_label)

        bot_label = left_at(T("60 fps AI edit", 34), -SAFE_X, y2 + .72)
        bot = self.blocks(y2, h)
        self.go(2.44, FadeIn(bot_label), FadeIn(bot), rt=.5)

        # Smoothing every frame: even ticks sweep across and the holds disappear.
        tw = WIDE / 60
        ticks = VGroup(*[Rectangle(width=tw, height=h, stroke_color=CREAM, stroke_width=1,
                                   fill_color=CRIMSON, fill_opacity=1).move_to([-SAFE_X + tw * (i + .5), y2, 0])
                         for i in range(60)])
        self.go(5.66, LaggedStart(*[FadeIn(t, run_time=.15) for t in ticks], lag_ratio=.6), rt=2.3)
        self.remove(bot)
        self.bring_to_front(ticks)

        quote = T("“lifeless”", 68, CRIMSON, slant="ITALIC").move_to([0, -1.92, 0])
        credit = centred(["a critic in", "The A.V. Club"], 36).move_to([0, -2.92, 0])
        self.go(10.0, FadeIn(quote, scale=1.05), FadeIn(credit), rt=.5)

        # A little is fine; a whole anime is not.
        little = centred(["A little AI here", "and there: fine"], 36, TEAL).move_to([0, -1.92, 0])
        whole = centred(["A whole anime:", "unnatural to me"], 36, CRIMSON).move_to([0, -2.92, 0])
        self.go(12.9, FadeOut(quote), FadeOut(credit), rt=.4)
        self.go(13.46, FadeIn(little), top[3].animate.set_fill(CRIMSON, 1), rt=.5)
        self.go(16.14, FadeIn(whole), rt=.5)
        self.finish()


@timed("B08")
class B08_MatchColourShapes(Scene):
    def construct(self):
        # The dataset.
        head = centred(["AI built", "for anime"], 60).move_to([0, 2.5, 0])
        self.go(.5, FadeIn(head))
        name = T("AnimeInterp, 2021", 38, TEAL).move_to([0, 1.2, 0])
        self.go(4.3, FadeIn(name))
        count = T("0", 104).move_to([0, -.25, 0])

        def counter(m, a):
            m.become(T(f"{round(a * 12000):,}", 104).move_to([0, -.25, 0]))
        self.go(8.1, FadeIn(count), rt=.15)
        self.driven(count, 8.3, 9.6, counter)
        unit = centred(["sets of", "anime frames"], 50).move_to([0, -2.1, 0])
        self.go(9.7, FadeIn(unit))
        # The project name rises to the heading spot and stays until the matching heading
        # replaces it, so the beat never goes text-free between the two sections.
        self.go(11.0, FadeOut(VGroup(head, count, unit)), name.animate.move_to([0, 2.8, 0]), rt=.4)

        # Two drawings, one above the other: match the regions before the motion.
        top_y, bot_y, w, h = .9, -1.95, 3.7, 2.7
        boxes = VGroup(panel(0, top_y, w, h), panel(0, bot_y, w, h))

        def drawing(cy, shift):
            sq = RoundedRectangle(corner_radius=.1, width=1.0, height=.8, fill_color=SLATE, fill_opacity=1,
                                  stroke_width=0).move_to([-1.05 + shift[0][0], cy + .65 + shift[0][1], 0])
            ci = Circle(radius=.38, fill_color=TEAL, fill_opacity=1,
                        stroke_width=0).move_to([1.05 + shift[1][0], cy + .55 + shift[1][1], 0])
            tr = Triangle(fill_color=GOLD, fill_opacity=1, stroke_width=0).scale(.5).move_to(
                [-1.0 + shift[2][0], cy - .7 + shift[2][1], 0])
            bl = Ellipse(width=1.0, height=.58, fill_color=SAGE, fill_opacity=1,
                         stroke_width=0).move_to([.95 + shift[3][0], cy - .75 + shift[3][1], 0])
            return VGroup(sq, ci, tr, bl)

        still = ((0, 0),) * 4
        moved = ((.45, -.2), (-.25, .15), (.5, .2), (-.2, .25))
        d1, d2 = drawing(top_y, still), drawing(bot_y, moved)
        match_head = centred(["first, match the", "flat color shapes"], 38).move_to([0, 2.8, 0])
        self.go(11.5, FadeIn(boxes), FadeIn(d1), FadeIn(d2), rt=.3)
        self.go(12.44, FadeOut(name), FadeIn(match_head))
        links = VGroup(*[DashedVMobject(ArcBetweenPoints(a.get_center(), b.get_center(), angle=ang,
                                                         stroke_color=INK, stroke_width=4), num_dashes=26)
                         for a, b, ang in zip(d1, d2, (-.35, .35, .3, -.3))])
        self.go(13.0, LaggedStart(*[Create(l) for l in links], lag_ratio=.45), rt=1.5)

        motion_head = centred(["then guess", "the motion"], 42, TEAL).move_to([0, 2.8, 0])
        arrows = VGroup()
        before = drawing(bot_y, still).set_fill(opacity=.22)
        for a, b in zip(before, d2):
            arrows.add(Arrow(a.get_center(), b.get_center(), buff=0, stroke_width=6, tip_length=.16,
                             color=CRIMSON, max_stroke_width_to_length_ratio=100))
        self.go(15.3, FadeOut(match_head), FadeOut(links), rt=.3)
        self.add(before)
        self.bring_to_back(before)
        self.go(15.68, FadeIn(motion_head), *[GrowArrow(a) for a in arrows], rt=.6)

        # Off the animator's desk, but never out of the animator's sight.
        self.go(16.9, FadeOut(VGroup(boxes, d1, d2, before, motion_head, arrows)), rt=.3)
        off = centred(["repetitive", "in-betweens,", "off the desk"], 34).move_to([0, 2.6, 0])
        desk = Rectangle(width=WIDE, height=.26, fill_color=INK, fill_opacity=1,
                         stroke_width=0).move_to([0, -3.15, 0])

        def sheet():
            s = Rectangle(width=1.08, height=1.25, fill_color=CREAM, fill_opacity=1, stroke_color=INK, stroke_width=3)
            return VGroup(s, token(SLATE, .62).move_to(s))
        n = 6
        sheets = VGroup(*[sheet().move_to([-1.3 + i * .05, -2.3 + i * .04, 0]) for i in range(n)])
        self.go(17.3, FadeIn(desk), FadeIn(sheets), rt=.5)
        self.go(18.24, FadeIn(off))
        # Two rows of three replace the landscape's single row of six.
        spots = [(-1.25 + 1.25 * (i % 3), 1.2 - (i // 3) * 2.05) for i in range(n)]
        self.go(19.44, *[s.animate.move_to([x, y, 0]) for s, (x, y) in zip(sheets, spots)], rt=1.1)

        checks_head = centred(["the animator", "checks every frame"], 38, TEAL).move_to([0, 2.8, 0])
        self.go(21.0, FadeOut(off), rt=.3)
        self.go(21.36, FadeIn(checks_head), rt=.4)
        pencil = VGroup(Rectangle(width=.8, height=.16, fill_color=GOLD, fill_opacity=1, stroke_width=0),
                        Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(.09).rotate(-PI / 2)
                        .move_to([.46, 0, 0])).rotate(-.5).move_to([spots[0][0], -2.45, 0])
        self.add(pencil)
        marks = VGroup(*[check(np.array([x, y - .88, 0]), .5) for x, y in spots])

        def write(m, a):
            pos = a * (n - 1)
            i = min(int(pos), n - 2)
            f = pos - i
            m.move_to([spots[i][0] + f * (spots[i + 1][0] - spots[i][0]) + .4,
                       spots[i][1] + f * (spots[i + 1][1] - spots[i][1]) - 1.1, 0])
        self.driven(pencil, 21.8, 23.3, write)
        self.go(21.8, LaggedStart(*[Create(c) for c in marks], lag_ratio=.9), rt=1.5)
        self.finish()
