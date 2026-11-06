"""Manim scenes for "How AI Draws Anime Frames" (Keya G.).

B01_WouldYouStillLove  hand-held vs smoothed motion, in-between slots, the question
B03_KeyFrames          two key poses, then the in-betweens AI is asked to draw
B04_OnesTwosThrees     one 24-frame strip recoloured into twos, threes and ones
B05_OpticalFlow        arrows between two frames; halfway along them is the new frame
B06_ThreeBreaks        flat colors, big movement, hidden parts, and the resulting errors
B07_TimingWiped        even 60 fps ticks flatten the animator's chosen holds
B08_MatchColourShapes  AnimeInterp: match flat shapes first; the animator checks every frame

Simple abstract shapes only: no frames or characters from Naruto or any real anime.
Each scene's length comes from actual_duration_s in beat_sheet.json. The times passed
to go() are word timings measured from the beat's narration audio, so re-check them if
that audio is regenerated.
"""
import json
import math
import random
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
# beat_sheet.json is the master clock. The fallback is its measured values, for run.sh's
# Gate A, which checks a copy of this file in a folder without the sheet.
DUR = {"B01": 17.66, "B03": 20.42, "B04": 20.12, "B05": 18.71, "B06": 25.3, "B07": 19.22, "B08": 23.7}
if (HERE / "beat_sheet.json").is_file():
    DUR = {b["beat_id"]: b["actual_duration_s"]
           for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"     # good / kept / true
CRIMSON = "#E4572E"  # bad / lost / broken
SLATE = "#29335C"    # structure
GOLD = "#F3A712"     # fill only, never text or fine marks
SAGE = "#A8C686"     # fill only

# Just inside the safe area run.sh's Gate B enforces (6.3 x 3.4), in Manim units.
SAFE_X, SAFE_Y = 6.25, 3.4
WIDE = SAFE_X * 2


def T(text, size=48, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def centred(lines, size, color=INK, buff=.28):
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
        self._audit(t)
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))

    def finish(self):
        self._audit(self.now)
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

    def _audit(self, t):
        """Log text outside the safe area or colliding with other text."""
        if not hasattr(self, "get_mobject_family_members"):  # Gate A's stand-in for Manim
            return
        texts = [m for m in self.get_mobject_family_members()
                 if isinstance(m, Text) and m.get_fill_opacity() > 0.05]
        for m in texts:
            box = (m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1])
            if box[0] < -SAFE_X - .01 or box[1] > SAFE_X + .01 or box[2] < -SAFE_Y - .01 or box[3] > SAFE_Y + .01:
                self._say(f"t={t}: '{m.text}' leaves the safe area {tuple(round(v, 2) for v in box)}")
        for i, a in enumerate(texts):
            for b in texts[i + 1:]:
                if (a.get_left()[0] < b.get_right()[0] and b.get_left()[0] < a.get_right()[0]
                        and a.get_bottom()[1] < b.get_top()[1] and b.get_bottom()[1] < a.get_top()[1]):
                    self._say(f"t={t}: '{a.text}' overlaps '{b.text}'")

    def _say(self, msg):
        if msg not in self._reported:
            self._reported.add(msg)
            print(f"QC {self.BEAT}: {msg}")


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because
    run.sh finds scenes by that exact text, so it would miss a Scene subclass."""
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
    return RoundedRectangle(corner_radius=.12, width=w, height=h, stroke_color=stroke,
                            stroke_width=width, fill_opacity=0).move_to([x, y, 0])


def check(at, size=.5, color=TEAL):
    pts = [at + np.array([-.5, 0, 0]) * size, at + np.array([-.1, -.45, 0]) * size,
           at + np.array([.6, .55, 0]) * size]
    return VMobject(stroke_color=color, stroke_width=10).set_points_as_corners(pts)


@timed("B01")
class B01_WouldYouStillLove(Scene):
    def construct(self):
        # Two copies of one shape cross the frame: held drawings vs a glide.
        start, end = -5.4, 5.4
        top = token(TEAL, 1.6).move_to([start, 1.15, 0])
        bot = token(CRIMSON, 1.6).move_to([start, -2.3, 0])
        top_label = left_at(T("drawn, then held", 60), -SAFE_X, 2.85)
        bot_label = left_at(T("AI-smoothed", 60), -SAFE_X, -.65)
        unnatural = T("unnatural", 76, CRIMSON)
        unnatural.move_to([SAFE_X - unnatural.width / 2, -.65, 0])
        self.add(top, bot, top_label)

        def stepped(m, a):
            m.set_x(start + (end - start) * math.floor(a * 7) / 7)

        def glide(m, a):
            m.set_x(start + (end - start) * a)
        self.driven(top, .2, 4.0, stepped)
        self.driven(bot, .2, 4.0, glide)
        self.go(1.14, FadeIn(bot_label))
        self.go(2.8, FadeIn(unnatural, scale=1.15))

        # Toei: AI for the slots between two drawings.
        lanes = VGroup(top, bot, top_label, bot_label, unnatural)
        self.go(4.18, FadeOut(lanes), rt=.5)
        head = T("AI for in-between frames", 80).move_to([0, 2.6, 0])
        source = T("Anime Corner, 2025", 50).move_to([0, -2.75, 0])
        w, gap = 1.62, .17
        xs = [(i - 3) * (w + gap) for i in range(7)]
        slots = VGroup(*[DashedVMobject(panel(x, .1, w, 2.8), num_dashes=34) for x in xs])
        keys = VGroup(token(SLATE, 1.1).move_to([xs[0], .1, 0]), token(SLATE, 1.1).move_to([xs[-1], .1, 0]))
        self.go(4.94, Create(slots), FadeIn(keys), rt=1)
        self.go(6.84, FadeIn(source))
        self.go(9.74, FadeIn(head))
        fills = VGroup(*[token(TEAL, 1.1).move_to([x, .1, 0]) for x in xs[1:-1]])
        self.go(10.66, LaggedStart(*[FadeIn(f, scale=.7) for f in fills], lag_ratio=.5), rt=1.1)

        # The question is the last thing on screen.
        self.go(12.5, FadeOut(VGroup(head, source, slots, keys, fills)), rt=.45)
        if_line = centred(["If AI drew your favourite anime", "on its own,"], 76).move_to([0, 1.6, 0])
        love = centred(["would you still love it", "the same way?"], 76, TEAL).move_to([0, -1.6, 0])
        # An empty slot holds the lower half until the second line lands in it.
        slot = DashedVMobject(panel(0, -1.6, 11.6, 3.0), num_dashes=70)
        self.go(13.04, FadeIn(if_line, shift=UP * .1), FadeIn(slot), rt=.6)
        self.go(15.94, FadeIn(love, shift=UP * .1), rt=.6)
        self.finish()


@timed("B03")
class B03_KeyFrames(Scene):
    def construct(self):
        def arc(a):
            p0, p1, p2 = np.array([-5.0, -.95, 0]), np.array([-.6, 4.3, 0]), np.array([3.9, -.85, 0])
            return (1 - a) ** 2 * p0 + 2 * a * (1 - a) * p1 + a ** 2 * p2

        def pose(a, color, opacity=1.0):
            d = arc(min(a + .01, 1)) - arc(max(a - .01, 0))
            return RoundedRectangle(corner_radius=.28, width=1.0, height=.6, fill_color=color,
                                    fill_opacity=opacity, stroke_width=0).rotate(math.atan2(d[1], d[0])).move_to(arc(a))

        title = T("Hand-drawn animation", 76).move_to([0, 2.85, 0])
        self.go(.4, FadeIn(title))
        title2 = T("Every scene starts with key frames", 70).move_to([0, 2.85, 0])
        pitch, n = WIDE / 9, 9
        cells = VGroup(*[Rectangle(width=pitch - .08, height=.95, stroke_color=INK, stroke_width=2,
                                   fill_color=CREAM, fill_opacity=1).move_to([-SAFE_X + pitch * (i + .5), -2.95, 0])
                         for i in range(n)])
        self.go(2.56, FadeOut(title), FadeIn(cells), rt=.5)
        self.go(3.1, FadeIn(title2))
        key_cells = [cells[0], cells[-1]]
        key_words = VGroup(*[T("key", 54, CREAM).move_to(c) for c in key_cells])
        self.go(3.98, *[c.animate.set_fill(SLATE) for c in key_cells], FadeIn(key_words))

        block = Rectangle(width=1.05, height=2.5, fill_color=INK, fill_opacity=1,
                          stroke_width=0).move_to([5.75, -.6, 0])
        p1 = pose(0, SLATE)
        launch = T("launch", 60).move_to([-5.0, -1.95, 0])
        self.go(9.18, FadeIn(p1, scale=1.2), FadeIn(launch))
        p2 = pose(1, SLATE)
        lands = T("lands", 60).move_to([3.9, -1.95, 0])
        self.go(11.1, FadeIn(block), FadeIn(p2, scale=1.2), FadeIn(lands))

        # The in-betweens fill the arc and the timeline, one at a time.
        title3 = T("In-betweens connect them", 80).move_to([0, 2.85, 0])
        self.go(12.68, FadeOut(title2), FadeIn(title3))
        ghosts = VGroup(*[pose((i + 1) / 8, SLATE, .42) for i in range(7)])
        self.go(13.2, LaggedStart(*[AnimationGroup(FadeIn(g), cells[i + 1].animate.set_fill(SLATE, .42))
                                    for i, g in enumerate(ghosts)], lag_ratio=.6), rt=2.3)
        # Those drawings are the ones AI is asked to make.
        title4 = T("What AI is asked to draw", 80, TEAL).move_to([0, 2.85, 0])
        self.go(16.36, FadeOut(title3), FadeIn(title4),
                *[g.animate.set_fill(TEAL, 1) for g in ghosts],
                *[c.animate.set_fill(TEAL, 1) for c in cells[1:-1]], rt=.8)
        self.finish()


@timed("B04")
class B04_OnesTwosThrees(Scene):
    def strip(self, y, h):
        cell = WIDE / 24
        return VGroup(*[Rectangle(width=cell, height=h, stroke_color=CREAM, stroke_width=2.5,
                                  fill_color=SLATE, fill_opacity=.42).move_to([-SAFE_X + cell * (i + .5), y, 0])
                        for i in range(24)])

    def holds(self, cells, n):
        """Same-coloured runs of cells are one drawing, held for n frames."""
        return [c.animate.set_fill(TEAL if (i // n) % 2 == 0 else SAGE, 1) for i, c in enumerate(cells)]

    def playhead(self, y, n, t0, seconds=2.0, sweeps=1):
        cell = WIDE / 24
        tri = Triangle(fill_color=CRIMSON, fill_opacity=1, stroke_width=0).scale(.17)
        tri.move_to([-SAFE_X + cell * n / 2, y, 0])

        def step(m, a):
            pos = (a * sweeps) % 1 if a < 1 else .999
            m.set_x(-SAFE_X + cell * (math.floor(pos * 24 / n) * n + n / 2))
        self.driven(tri, t0, t0 + seconds * sweeps, step)
        return tri

    def construct(self):
        base = self.strip(.2, 1.9)
        head = T("24 frames = one second", 88).move_to([0, 2.15, 0])
        self.add(base)
        self.go(.98, FadeIn(head))
        rarely = T("anime rarely draws all 24", 76).move_to([0, -1.75, 0])
        self.go(3.12, FadeIn(rarely))

        ys = (2.05, .35, -1.35)
        self.go(5.52, FadeOut(head), FadeOut(rarely),
                base.animate.stretch_to_fit_height(.8).move_to([0, ys[0], 0]), rt=.7)
        twos = left_at(T("on twos", 54), -SAFE_X, ys[0] + .72)
        self.go(6.7, FadeIn(twos), *self.holds(base, 2), rt=.5)

        row3 = self.strip(ys[1], .8)
        threes = left_at(T("on threes", 54), -SAFE_X, ys[1] + .72)
        # The third row waits as an empty outline until its cue.
        cell = WIDE / 24
        outline = VGroup(*[Rectangle(width=cell, height=.8, stroke_color=INK, stroke_width=2, fill_opacity=0)
                           .move_to([-SAFE_X + cell * (i + .5), ys[2], 0]) for i in range(24)])
        self.go(7.3, FadeIn(row3), FadeIn(threes), FadeIn(outline), *self.holds(row3, 3), rt=.5)
        # The same sweep on both rows: the mark hangs longer on threes.
        self.add(self.playhead(ys[0] - .54, 2, 8.3), self.playhead(ys[1] - .54, 3, 8.3))
        twos2 = left_at(T("on twos: 12 drawings", 54), -SAFE_X, ys[0] + .72)
        self.go(11.38, FadeOut(twos, run_time=.3), FadeIn(twos2, run_time=.3), rt=None)
        threes2 = left_at(T("on threes: just 8", 54), -SAFE_X, ys[1] + .72)
        self.go(11.72, FadeOut(threes, run_time=.3), FadeIn(threes2, run_time=.3), rt=None)

        row1 = self.strip(ys[2], .8)
        ones = left_at(T("on ones", 54), -SAFE_X, ys[2] + .72)
        self.go(13.56, FadeIn(row1), FadeOut(outline))
        self.go(15.8, FadeIn(ones), *self.holds(row1, 1), rt=.4)
        self.add(self.playhead(ys[2] - .54, 1, 15.8, seconds=.5, sweeps=2))
        ones2 = left_at(T("on ones: all 24", 54), -SAFE_X, ys[2] + .72)
        self.go(16.3, FadeOut(ones, run_time=.3), FadeIn(ones2, run_time=.3), rt=None)

        # One line of text, revealed in parts, so every word shares a baseline.
        line = T("a choice about budget and feel", 72).move_to([0, -3.0, 0])
        choice, budget, andword, feel = line[:12], line[12:18], line[18:21], line[21:25]
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
        w, h, cy = 3.72, 4.25, .25
        left_x, mid_x, right_x = -4.54, 0.0, 4.54
        frames = VGroup(*[panel(x, cy, w, h) for x in (left_x, right_x)])
        middle = DashedVMobject(panel(mid_x, cy, w, h), num_dashes=46)
        labels = VGroup(T("frame 1", 60).move_to([left_x, 3.0, 0]), T("frame 2", 60).move_to([right_x, 3.0, 0]))

        # p = where a pixel sits; v = how far it moves between the frames.
        points = []
        for _ in range(95):
            points.append((np.array([rng.uniform(-1.65, 1.65), rng.uniform(-1.9, 1.9), 0]),
                           np.array([.1, .03, 0]), False))
        for _ in range(46):
            a, r = rng.uniform(0, math.tau), .8 * math.sqrt(rng.random())
            points.append((np.array([-.85 + r * math.cos(a), r * math.sin(a), 0]),
                           np.array([1.55, .3, 0]), True))

        def dot(c, big):
            return Dot(c, radius=.085 if big else .05, color=SLATE if big else INK,
                       fill_opacity=1 if big else .55)

        centre = np.array([0, cy, 0])
        left_dots = VGroup(*[dot(centre + [left_x, 0, 0] + p, big) for p, v, big in points])
        right_dots = VGroup(*[dot(centre + [right_x, 0, 0] + p + v, big) for p, v, big in points])
        self.add(frames, labels, left_dots, right_dots)
        self.go(.8, Create(middle), rt=.8)

        word = T("optical flow", 92, TEAL).move_to([0, -2.75, 0])
        self.go(3.32, FadeIn(word))
        # Straight from a dot in frame 1 to the same dot in frame 2.
        chosen = list(range(95, 107)) + list(range(0, 95, 16))
        arrows = VGroup(*[Arrow(left_dots[i].get_center(), right_dots[i].get_center(), buff=0, stroke_width=3.5,
                                tip_length=.2, color=TEAL, max_stroke_width_to_length_ratio=100)
                          for i in chosen])
        sub = T("where each pixel moved", 84).move_to([0, -2.75, 0])
        self.go(4.88, LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=.12, run_time=3.4),
                FadeOut(word, run_time=.4), FadeIn(sub, run_time=.4), rt=None)

        # Halfway along each arrow is that dot's place in the new frame.
        new_label = T("new frame", 60, TEAL).move_to([mid_x, 3.0, 0])
        halfway = T("follow the arrows halfway", 84).move_to([0, -2.75, 0])
        self.go(9.3, FadeOut(sub), FadeIn(halfway), rt=.4)
        movers = VGroup(*[d.copy() for d in left_dots])
        self.add(movers)
        targets = [(np.array(left_dots[i].get_center()) + np.array(right_dots[i].get_center())) / 2
                   for i in range(len(points))]
        self.go(9.96, *[m.animate.move_to(c) for m, c in zip(movers, targets)], rt=2.3)
        self.go(12.3, FadeIn(new_label))

        # Live action has texture everywhere, so this holds up.
        live = T("live action: lots of texture", 84).move_to([0, -2.75, 0])
        self.go(13.48, FadeOut(arrows), FadeOut(halfway), rt=.45)
        self.go(14.0, FadeIn(live), rt=.45)
        works = T("works surprisingly well", 84, TEAL)
        tick = check(np.array([0, 0, 0]), .7)
        VGroup(tick, works).arrange(RIGHT, buff=.4).move_to([0, -2.75, 0])
        self.go(17.0, FadeOut(live), FadeIn(works), Create(tick), rt=.4)
        self.finish()


@timed("B06")
class B06_ThreeBreaks(Scene):
    def construct(self):
        xs = (-4.34, 0, 4.34)
        w, h, cy = 4.1, 5.05, -.75 + .72
        boxes = VGroup(*[panel(x, cy, w, h) for x in xs])
        heads = [T(s, 56).move_to([x, 3.05, 0]) for s, x in
                 zip(("flat colors", "big movement", "hidden parts"), xs)]
        for head in heads[1:]:
            head.align_to(heads[0], UP)
        self.go(.3, Create(boxes), rt=.7)
        cap_y = -2.05

        # 1. A flat sleeve: no texture, so the flow arrows have nothing to hold on to.
        x = xs[0]
        rng = random.Random(3)
        self.go(2.5, FadeIn(heads[0]), rt=.4)
        sleeve = Rectangle(width=2.6, height=1.5, fill_color=SLATE, fill_opacity=1,
                           stroke_width=0).move_to([x - .28, .75, 0])
        self.go(3.66, FadeIn(sleeve))
        cap1 = T("no texture", 50, CRIMSON).move_to([x, cap_y, 0])
        self.go(5.2, FadeIn(cap1))
        arrows = VGroup()
        for _ in range(9):
            a = np.array([x + rng.uniform(-1.4, .95), rng.uniform(.15, 1.35), 0])
            b = np.array([x + rng.uniform(-1.6, 1.6), rng.uniform(-1.2, 1.9), 0])
            arrows.add(Arrow(a, b, buff=0, stroke_width=4, tip_length=.2, color=CRIMSON,
                             max_stroke_width_to_length_ratio=100))
        self.go(6.72, LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=.15), rt=1.6)

        # 2. A long curved jump: the real path bends, the straight guess misses.
        x = xs[1]
        self.go(9.24, FadeIn(heads[1]), rt=.4)
        p0, p1, p2 = [np.array(v, float) for v in ([x - 1.55, -1.15, 0], [x - 1.6, 2.5, 0], [x + 1.45, 1.75, 0])]
        path = VMobject(stroke_color=TEAL, stroke_width=6)
        path.set_points_as_corners([(1 - a) ** 2 * p0 + 2 * a * (1 - a) * p1 + a ** 2 * p2
                                    for a in np.linspace(0, 1, 40)])
        fist = Circle(radius=.36, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to(p0)
        self.go(10.4, FadeIn(fist))
        self.go(13.7, Create(path), MoveAlongPath(fist, path), rt=3.1)
        guess_mid = (p0 + p2) / 2
        guess = DashedLine(p0, guess_mid, color=CRIMSON, stroke_width=7, dash_length=.16)
        miss = Cross(Circle(radius=.26).move_to(guess_mid), stroke_color=CRIMSON, stroke_width=9)
        cap2 = T("the guess misses", 46, CRIMSON).move_to([x, cap_y, 0]).align_to(cap1, UP)
        self.go(16.82, Create(guess), Create(miss), FadeIn(cap2), rt=.6)

        # 3. A hand slips behind the body: nothing in frame 2 to match it to.
        x = xs[2]
        self.go(17.54, FadeIn(heads[2]), rt=.4)
        hand = Circle(radius=.42, fill_color=TEAL, fill_opacity=1, stroke_width=0).move_to([x - 1.25, .5, 0])
        hand_label = T("hand", 46).move_to([x - 1.25, 1.25, 0])
        body = RoundedRectangle(corner_radius=.15, width=1.65, height=3.0, fill_color=SLATE, fill_opacity=1,
                                stroke_width=0).move_to([x + .75, .4, 0])
        body_label = T("body", 46, CREAM).move_to(body)
        self.go(17.95, FadeIn(hand), FadeIn(hand_label), FadeIn(body), FadeIn(body_label), rt=.5)
        self.bring_to_back(hand)
        outline = DashedVMobject(Circle(radius=.42, stroke_color=TEAL, stroke_width=5).move_to(hand.get_center()),
                                 num_dashes=14)
        self.add(outline)
        self.go(19.38, hand.animate.move_to(body.get_center() + UP * .95), FadeOut(hand_label), rt=.7)
        cap3 = T("no match", 50, CRIMSON).move_to([x, cap_y, 0]).align_to(cap1, UP)
        self.go(20.64, FadeIn(cap3), rt=.4)

        # The errors those breaks leave in the drawn frame.
        panel1 = VGroup(sleeve, arrows, cap1, heads[0])
        panel2 = VGroup(path, fist, guess, miss, cap2, heads[1])
        panel3 = VGroup(hand, outline, body, body_label, cap3, heads[2])
        result = T("the result", 76).move_to([0, 3.0, 0])
        self.go(21.5, FadeOut(panel1), FadeOut(panel2), FadeOut(panel3), rt=.35)
        self.go(21.9, FadeIn(result), rt=.3)

        def figure(x, color=SLATE, opacity=1.0, limbs=2):
            c = np.array([x, .55, 0])
            core = Circle(radius=.62, fill_color=color, fill_opacity=opacity, stroke_width=0).move_to(c)
            parts = VGroup(core)
            for i in range(limbs):
                ang = -PI / 2 + (i - (limbs - 1) / 2) * (1.15 if limbs == 2 else .85)
                limb = RoundedRectangle(corner_radius=.11, width=1.3, height=.26, fill_color=color,
                                        fill_opacity=opacity, stroke_width=0).rotate(ang)
                limb.move_to(c + np.array([math.cos(ang), math.sin(ang), 0]) * 1.05)
                parts.add(limb)
            return parts

        ghost = VGroup(figure(xs[0] - .55, CRIMSON, .28), figure(xs[0] + .55, CRIMSON, .28), figure(xs[0]))
        blur = VGroup(figure(xs[1]))
        for i in range(8):
            blur.add(Rectangle(width=.26, height=1.25 - i * .09, fill_color=CRIMSON,
                                fill_opacity=.72 - i * .08, stroke_width=0).move_to([xs[1] - .68 - i * .17, .55, 0]))
        extra = VGroup(figure(xs[2]))
        for ang in (-PI / 2, .55, PI - .55):
            limb = RoundedRectangle(corner_radius=.11, width=1.3, height=.26, fill_color=CRIMSON, fill_opacity=1,
                                    stroke_width=0).rotate(ang)
            limb.move_to(np.array([xs[2], .55, 0]) + np.array([math.cos(ang), math.sin(ang), 0]) * 1.05)
            extra.add(limb)
        words = [T(s, 60, CRIMSON).move_to([x, cap_y, 0]) for s, x in zip(("ghosting", "blur", "extra limbs"), xs)]
        for word in words[1:]:
            word.align_to(words[0], UP)
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
            out.add(Rectangle(width=cell * n, height=h, stroke_color=CREAM, stroke_width=3,
                              fill_color=TEAL if i % 2 == 0 else SAGE, fill_opacity=1)
                    .move_to([x + cell * n / 2, y, 0]))
            x += cell * n
        return out

    def construct(self):
        y1, y2, h = 2.0, -.35, 1.0
        top = self.blocks(y1, h)
        top_label = left_at(T("the animator\u2019s timing", 62), -SAFE_X, y1 + .92)
        self.add(top, top_label)

        bot_label = left_at(T("60 fps AI edit", 62), -SAFE_X, y2 + .92)
        bot = self.blocks(y2, h)
        self.go(2.44, FadeIn(bot_label), FadeIn(bot), rt=.5)

        # Smoothing every frame: even ticks sweep across and the holds disappear.
        tw = WIDE / 60
        ticks = VGroup(*[Rectangle(width=tw, height=h, stroke_color=CREAM, stroke_width=1.5,
                                   fill_color=CRIMSON, fill_opacity=1).move_to([-SAFE_X + tw * (i + .5), y2, 0])
                         for i in range(60)])
        self.go(5.66, LaggedStart(*[FadeIn(t, run_time=.15) for t in ticks], lag_ratio=.6), rt=2.3)
        self.remove(bot)
        self.bring_to_front(ticks)

        quote = T("“lifeless”", 112, CRIMSON, slant="ITALIC").move_to([0, -1.92, 0])
        credit = T("a critic in The A.V. Club", 56).move_to([0, -3.1, 0])
        self.go(10.0, FadeIn(quote, scale=1.05), FadeIn(credit), rt=.5)

        # A little is fine; a whole anime is not.
        little = T("A little AI here and there: fine", 72, TEAL).move_to([0, -1.65, 0])
        whole = T("A whole anime: unnatural to me", 72, CRIMSON).move_to([0, -2.95, 0])
        self.go(12.9, FadeOut(quote), FadeOut(credit), rt=.4)
        self.go(13.46, FadeIn(little), top[3].animate.set_fill(CRIMSON, 1), rt=.5)
        self.go(16.14, FadeIn(whole), rt=.5)
        self.finish()


@timed("B08")
class B08_MatchColourShapes(Scene):
    def construct(self):
        # The dataset.
        head = T("AI built for anime", 92).move_to([0, 2.85, 0])
        self.go(.5, FadeIn(head))
        name = T("AnimeInterp, 2021", 70, TEAL).move_to([0, 1.6, 0])
        self.go(4.3, FadeIn(name))
        count = T("0", 190).move_to([0, -.4, 0])

        def counter(m, a):
            m.become(T(f"{round(a * 12000):,}", 190).move_to([0, -.4, 0]))
        self.go(8.1, FadeIn(count), rt=.15)
        self.driven(count, 8.3, 9.6, counter)
        unit = T("sets of anime frames", 80).move_to([0, -2.4, 0])
        self.go(9.7, FadeIn(unit))
        self.go(11.0, FadeOut(VGroup(head, name, count, unit)), rt=.4)

        # Two drawings made of flat regions: match the regions before the motion.
        lx, rx, cy, w, h = -3.32, 3.32, -.45, 6.1, 5.1
        boxes = VGroup(panel(lx, cy, w, h), panel(rx, cy, w, h))

        def drawing(cx, shift):
            sq = RoundedRectangle(corner_radius=.15, width=1.6, height=1.25, fill_color=SLATE, fill_opacity=1,
                                  stroke_width=0).move_to([cx - 1.25 + shift[0][0], cy + 1.05 + shift[0][1], 0])
            ci = Circle(radius=.6, fill_color=TEAL, fill_opacity=1,
                        stroke_width=0).move_to([cx + 1.45 + shift[1][0], cy + .7 + shift[1][1], 0])
            tr = Triangle(fill_color=GOLD, fill_opacity=1, stroke_width=0).scale(.8).move_to(
                [cx - .95 + shift[2][0], cy - 1.25 + shift[2][1], 0])
            bl = Ellipse(width=1.6, height=.9, fill_color=SAGE, fill_opacity=1,
                         stroke_width=0).move_to([cx + 1.05 + shift[3][0], cy - 1.45 + shift[3][1], 0])
            return VGroup(sq, ci, tr, bl)

        still = ((0, 0),) * 4
        moved = ((.65, -.35), (-.2, .55), (.75, .25), (.45, .4))
        d1, d2 = drawing(lx, still), drawing(rx, moved)
        match_head = T("first, match the flat color shapes", 76).move_to([0, 2.85, 0])
        self.go(11.5, FadeIn(boxes), FadeIn(d1), FadeIn(d2), rt=.3)
        self.go(12.44, FadeIn(match_head))
        links = VGroup(*[DashedVMobject(ArcBetweenPoints(a.get_center(), b.get_center(), angle=ang,
                                                         stroke_color=INK, stroke_width=5), num_dashes=30)
                         for a, b, ang in zip(d1, d2, (-.55, .4, -.3, .5))])
        self.go(13.0, LaggedStart(*[Create(l) for l in links], lag_ratio=.45), rt=1.5)

        motion_head = T("then guess the motion", 76, TEAL).move_to([0, 2.85, 0])
        arrows = VGroup()
        before = drawing(rx, still).set_fill(opacity=.22)
        for a, b in zip(before, d2):
            arrows.add(Arrow(a.get_center(), b.get_center(), buff=0, stroke_width=8, tip_length=.26,
                             color=CRIMSON, max_stroke_width_to_length_ratio=100))
        self.go(15.3, FadeOut(match_head), FadeOut(links), rt=.3)
        self.add(before)
        self.bring_to_back(before)
        self.go(15.68, FadeIn(motion_head), *[GrowArrow(a) for a in arrows], rt=.6)

        # Off the animator's desk, but never out of the animator's sight.
        self.go(16.9, FadeOut(VGroup(boxes, d1, d2, before, motion_head, arrows)), rt=.3)
        off = T("repetitive in-betweens, off the desk", 68).move_to([0, 2.85, 0])
        desk = Rectangle(width=WIDE, height=.42, fill_color=INK, fill_opacity=1,
                         stroke_width=0).move_to([0, -3.2, 0])

        def sheet():
            s = Rectangle(width=1.9, height=2.6, fill_color=CREAM, fill_opacity=1, stroke_color=INK, stroke_width=3)
            return VGroup(s, token(SLATE, 1.15).move_to(s))
        n = 6
        sheets = VGroup(*[sheet().move_to([-4.4 + i * .1, -1.65 + i * .08, 0]) for i in range(n)])
        self.go(17.3, FadeIn(desk), FadeIn(sheets), rt=.5)
        self.go(18.24, FadeIn(off))
        pitch = WIDE / n
        xs = [-SAFE_X + pitch * (i + .5) for i in range(n)]
        self.go(19.44, *[s.animate.move_to([x, .95, 0]) for s, x in zip(sheets, xs)], rt=1.1)

        checks_head = T("the animator checks every frame", 74, TEAL).move_to([0, 2.85, 0])
        self.go(21.0, FadeOut(off), rt=.3)
        self.go(21.36, FadeIn(checks_head), rt=.4)
        pencil = VGroup(Rectangle(width=1.5, height=.3, fill_color=GOLD, fill_opacity=1, stroke_width=0),
                        Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(.17).rotate(-PI / 2)
                        .move_to([.86, 0, 0])).rotate(-.5).move_to([xs[0], -2.35, 0])
        self.add(pencil)
        marks = VGroup(*[check(np.array([x, -1.15, 0]), .8) for x in xs])
        self.driven(pencil, 21.8, 23.3, lambda m, a: m.set_x(xs[0] + a * (xs[-1] - xs[0]) - .1))
        self.go(21.8, LaggedStart(*[Create(c) for c in marks], lag_ratio=.9), rt=1.5)
        self.finish()
