"""Native 9:16 layouts for "Week 4 Progress" (Keya G.).

Same scene names, content, colours and go() cues as ../scenes.py, rearranged for a tall
frame (4.5 x 8 Manim units at 2160x3840). Nothing here is a crop of the landscape film.

B01_ThisWeeksVideo  title, a drawn keyboard guess (hashi -> kana -> kanji candidates), then research, script, build
B02_Watching        a video player; claims matched to sources; scenes matched to narration
B03_Gates           a scene token down four gates; a failed gate, fix and render again; the check stays on
B04_Checksum        a final video and its copy on a drive show the same drawn fingerprint
B05_WhatILearned    a folder fills with its five parts; a terminal skill bar grows; a badge helps

Simple drawn shapes only: no photos, no person icons, no company or tool logos.
Portrait rule: all text sits above 86% of the frame height (y > -2.88 in Manim units), so
nothing sits below LOW. Each scene's length comes from actual_duration_s in beat_sheet.json.
The times passed to go() are word timings measured from the beat's narration audio
(faster-whisper), so re-check them if that audio is regenerated.
"""
import json
import math
import subprocess
from pathlib import Path

import numpy as np
from manim import *

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the
# 16:9 default (14.22); make it 4.5 so the frame is 4.5 x 8 units.
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

HERE = Path(__file__).resolve().parent
# beat_sheet.json is the master clock. The fallback is its measured values, for run.sh's
# Gate A, which checks a copy of this file in a folder without the sheet.
DUR = {"B01": 10.73, "B02": 10.43, "B03": 13.27, "B04": 10.41, "B05": 15.36}
SHEET = {}
if (HERE / "beat_sheet.json").is_file():
    SHEET = json.loads((HERE / "beat_sheet.json").read_text())
    DUR = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
# Just inside the portrait safe band Gate B enforces (1.95 x 3.4). Gate T also keeps the
# bottom 14% of a phone frame clear, so nothing sits below LOW.
SAFE_X, SAFE_Y = 1.85, 3.3
LOW = -2.85
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"     # good / done / kept
CRIMSON = "#E4572E"  # problem / blocked
SLATE = "#29335C"    # structure
GOLD = "#F3A712"     # fill only, never text or fine marks
SAGE = "#A8C686"     # fill only
JP = "Hiragino Sans"


def T(text, size=48, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def JT(text, size=48, color=INK):
    """Japanese text: Hiragino Sans, set explicitly (the default font has no kana or kanji)."""
    return Text(text, font=JP, font_size=size, color=color)


def fit(mob, max_w):
    """Shrink (never grow) a label so it is at most max_w units wide."""
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    return mob


def M(text, size=30, color=INK):
    return Text(text, font="Menlo", font_size=size, color=color)


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

    def _audit(self, t):
        """Log text outside the safe area or colliding with other text."""
        if not hasattr(self, "get_mobject_family_members"):  # Gate A's stand-in for Manim
            return
        texts = [m for m in self.get_mobject_family_members()
                 if isinstance(m, Text) and m.get_fill_opacity() > 0.05]
        for m in texts:
            box = (m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1])
            if box[0] < -SAFE_X - .01 or box[1] > SAFE_X + .01 or box[2] < LOW - .01 or box[3] > SAFE_Y + .01:
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


# ---- generic drawn shapes (never a company or tool logo) ---------------------------

def box(x, y, w, h, stroke=INK, width=3, fill=CREAM, fill_opacity=1):
    return RoundedRectangle(corner_radius=.14, width=w, height=h, stroke_color=stroke,
                            stroke_width=width, fill_color=fill,
                            fill_opacity=fill_opacity).move_to([x, y, 0])


def dashed(mob, n=28):
    return DashedVMobject(mob, num_dashes=n)


def check(at, size=.5, color=TEAL):
    at = np.array(at, dtype=float)
    pts = [at + np.array([-.5, 0, 0]) * size, at + np.array([-.1, -.45, 0]) * size,
           at + np.array([.6, .55, 0]) * size]
    return VMobject(stroke_color=color, stroke_width=10).set_points_as_corners(pts)


def cross(at, size=.5, color=CRIMSON):
    at = np.array(at, dtype=float)
    d = size * .5
    return VGroup(Line(at + [-d, -d, 0], at + [d, d, 0], stroke_color=color, stroke_width=12),
                  Line(at + [-d, d, 0], at + [d, -d, 0], stroke_color=color, stroke_width=12))


def play_icon(x, y, s=1.0, color=TEAL):
    return Triangle(fill_color=color, fill_opacity=1, stroke_width=0).rotate(-PI / 2).scale(.45 * s).move_to([x, y, 0])


def code_icon(x, y, s=1.0, color=SLATE):
    """< / > drawn as strokes."""
    w = 8 * s
    left = VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[-.25, .4, 0], [-.65, 0, 0], [-.25, -.4, 0]])
    right = VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[.25, .4, 0], [.65, 0, 0], [.25, -.4, 0]])
    slash = Line([.12, .45, 0], [-.12, -.45, 0], stroke_color=color, stroke_width=w)
    return VGroup(left, slash, right).scale(s).move_to([x, y, 0])


def cloud_icon(x, y, s=1.0, color=SLATE):
    parts = [Circle(radius=r, fill_color=color, fill_opacity=1, stroke_width=0).move_to(p)
             for r, p in ((.32, [-.38, -.05, 0]), (.42, [.05, .12, 0]), (.3, [.45, -.08, 0]))]
    base = RoundedRectangle(corner_radius=.18, width=1.3, height=.42, fill_color=color,
                            fill_opacity=1, stroke_width=0).move_to([.03, -.2, 0])
    return VGroup(*parts, base).scale(s).move_to([x, y, 0])


def magnifier_icon(x, y, s=1.0, color=SLATE):
    ring = Circle(radius=.34, stroke_color=color, stroke_width=8 * s, fill_opacity=0).move_to([-.1, .1, 0])
    handle = Line([.15, -.15, 0], [.5, -.5, 0], stroke_color=color, stroke_width=10 * s)
    return VGroup(ring, handle).scale(s).move_to([x, y, 0])


def page_icon(x, y, s=1.0, color=SLATE):
    page = RoundedRectangle(corner_radius=.06, width=.8, height=1.0, stroke_color=color,
                            stroke_width=5 * s, fill_color=CREAM, fill_opacity=1)
    rows = VGroup(*[Line([-.25, yy, 0], [.25 - .1 * i, yy, 0], stroke_color=color, stroke_width=5 * s)
                    for i, yy in enumerate((.25, 0, -.25))])
    return VGroup(page, rows).scale(s).move_to([x, y, 0])


def film_icon(x, y, w=2.6, h=1.4, color=SLATE):
    strip = Rectangle(width=w, height=h, fill_color=color, fill_opacity=1, stroke_width=0)
    holes = VGroup(*[RoundedRectangle(corner_radius=.03, width=.14, height=.12, fill_color=CREAM,
                                      fill_opacity=1, stroke_width=0).move_to([-w / 2 + .2 + i * (w - .4) / 7, yy, 0])
                     for i in range(8) for yy in (h / 2 - .14, -h / 2 + .14)])
    frames = VGroup(*[Rectangle(width=(w - .5) / 3 - .1, height=h - .65, fill_color=SAGE, fill_opacity=1,
                                stroke_width=0).move_to([-w / 2 + .25 + (w - .5) / 6 + i * (w - .5) / 3, 0, 0])
                      for i in range(3)])
    return VGroup(strip, holes, frames).move_to([x, y, 0])


def fingerprint(x, y, w, h, seed, color=SLATE):
    """A drawn 'fingerprint': a strip of bars. An illustration, never a real hash."""
    rng = np.random.default_rng(seed)
    n = 22
    bars = VGroup()
    for i in range(n):
        bh = h * (.45 + .5 * rng.random())
        bx = -w / 2 + w * (i + .5) / n
        bars.add(Line([bx, -bh / 2, 0], [bx, bh / 2, 0], stroke_color=color,
                      stroke_width=3 + 6 * rng.random()))
    return bars.move_to([x, y, 0])


def wave(x, y, w, h, seed, color=TEAL):
    rng = np.random.default_rng(seed)
    n = 30
    bars = VGroup()
    for i in range(n):
        bh = h * (.2 + .8 * rng.random())
        bx = -w / 2 + w * (i + .5) / n
        bars.add(Line([bx, -bh / 2, 0], [bx, bh / 2, 0], stroke_color=color, stroke_width=6))
    return bars.move_to([x, y, 0])


def switch(x, y, on=True, w=1.5, h=.78):
    body = RoundedRectangle(corner_radius=h / 2, width=w, height=h, stroke_color=TEAL if on else SLATE,
                            stroke_width=5, fill_color=TEAL if on else CREAM, fill_opacity=1)
    knob = Circle(radius=h / 2 - .1, fill_color=CREAM if on else SLATE, fill_opacity=1, stroke_width=0)
    knob.move_to([(w / 2 - h / 2) * (1 if on else -1), 0, 0])
    return VGroup(body, knob).move_to([x, y, 0])


# ---- scenes -----------------------------------------------------------------------

@timed("B01")
class B01_ThisWeeksVideo(Scene):
    def construct(self):
        title = VGroup(T("How Your", 50, SLATE), T("Phone Types", 50, SLATE), T("Japanese", 50, SLATE)).arrange(DOWN, buff=.04).move_to([0, 2.35, 0])
        sub = VGroup(T("this week's", 44), T("explainer", 44)).arrange(DOWN, buff=.04).move_to([0, .76, 0])
        self.go(.1, FadeIn(title, shift=UP * .1), rt=.5)
        self.go(.55, FadeIn(sub), rt=.45)

        # Steps: three cards, each landing on its spoken words. The first waits at the bottom
        # while the keyboard guess plays, then the three stack in reading order.
        def step(icon, label, y, h=1.0):
            return VGroup(box(0, y, 3.7, h, stroke=SLATE, width=5), icon.move_to([-1.4, y, 0]),
                          label.move_to([.35, y, 0]))
        c1 = step(magnifier_icon(0, 0, .8), T("researched", 46), -2.4, .8)
        c2 = step(page_icon(0, 0, .8), VGroup(T("wrote the", 46), T("script", 46)).arrange(DOWN, buff=.02), -1.25, .9)
        c3 = step(code_icon(0, 0, .56, TEAL), VGroup(T("built with", 44), T("Claude Code", 40)).arrange(DOWN, buff=.02), -2.32, 1.06)
        self.go(3.74, FadeIn(c1, scale=.9), rt=.15)

        # A keyboard guess: hashi, typed as romaji, becomes kana, then the kanji it might mean.
        ky = -.4
        hashi = VGroup(box(-.85, ky, 1.7, .86, stroke=SLATE, width=5), M("hashi", 44, SLATE).move_to([-.85, ky, 0]))
        arrow1 = Arrow([.05, ky, 0], [.5, ky, 0], buff=0, stroke_width=6, color=INK, max_tip_length_to_length_ratio=.5)
        kana = VGroup(box(1.2, ky, 1.3, .86, stroke=SLATE, width=5), JT("はし", 52, SLATE).move_to([1.2, ky, 0]))
        self.go(3.95, FadeIn(hashi, shift=DOWN * .1), rt=.4)
        self.go(4.9, GrowArrow(arrow1), FadeIn(kana, scale=.9), rt=.35)
        cands = []
        for kj, x in zip("橋箸端", (-1.28, 0, 1.28)):
            cands.append(VGroup(box(x, -1.4, 1.12, 1.0, stroke=SLATE, width=5), JT(kj, 56, SLATE).move_to([x, -1.4, 0])))
        self.go(5.3, LaggedStart(*[FadeIn(c, shift=UP * .15) for c in cands], lag_ratio=.35), rt=.9)
        # "which kanji you mean": one candidate is chosen.
        self.go(6.76, cands[0][0].animate.set_stroke(TEAL, 8).set_fill(TEAL, .15), rt=.35)

        # The keyboard guess clears and the three steps stack in order.
        demo = VGroup(hashi, arrow1, kana, *cands)
        self.go(7.1, FadeOut(demo), c1.animate.shift(UP * 2.15), rt=.3)
        self.go(7.38, FadeIn(c2, scale=.9), rt=.3)
        self.go(8.76, FadeIn(c3, scale=.9), rt=.3)
        self.go(9.6, Indicate(c3, color=TEAL, scale_factor=1.04), rt=.6)
        self.finish()


@timed("B02")
class B02_Watching(Scene):
    def construct(self):
        # The stage: a video player, with a timeline that runs the length of the beat.
        head = VGroup(T("watching", 46, SLATE), T("Brutalist videos", 46, SLATE)).arrange(DOWN, buff=.06).move_to([0, 2.7, 0])
        stage = box(0, -.1, 3.7, 4.0, stroke=SLATE, width=5)  # y 1.9 .. -2.1
        ty = -2.5
        track = Line([-1.8, ty, 0], [1.8, ty, 0], stroke_color=INK, stroke_width=6)
        dot = Dot(radius=.14, color=TEAL).move_to([-1.8, ty, 0])
        dot.add_updater(lambda m: m.move_to([-1.8 + 3.6 * min(1.0, self.now / DUR["B02"]), ty, 0]))
        self.add(stage, track, dot)
        ring = VGroup(Circle(radius=.75, stroke_color=TEAL, stroke_width=8, fill_color=CREAM, fill_opacity=1),
                      play_icon(.07, 0, 1.4)).move_to([0, -.1, 0])
        films = VGroup(film_icon(0, 1.3, 3.2, .9), film_icon(0, -1.5, 3.2, .9))
        self.go(.1, FadeIn(ring, scale=.8), FadeIn(films), rt=.5)
        self.go(1.0, FadeIn(head, shift=UP * .1), rt=.5)

        # Review 1: each claim is checked against its source.
        ys = [.7, -.35, -1.4]
        lx, rx = -1.05, 1.05
        claims = VGroup(*[VGroup(box(lx, y, 1.5, .8, stroke=SLATE, width=4),
                                 Line([lx - .5, y + .11, 0], [lx + .5, y + .11, 0], stroke_color=INK, stroke_width=5),
                                 Line([lx - .5, y - .13, 0], [lx + .15, y - .13, 0], stroke_color=INK, stroke_width=5))
                          for y in ys])
        sources = VGroup(*[VGroup(box(rx, y, 1.5, .8, stroke=TEAL, width=4), page_icon(rx - .42, y, .5, TEAL),
                                  Line([rx - .1, y, 0], [rx + .55, y, 0], stroke_color=TEAL, stroke_width=5))
                           for y in ys])
        claim_h = T("claims", 44, SLATE).move_to([lx - .05, 1.5, 0])
        src_h = T("sources", 42, TEAL).move_to([rx - .05, 1.5, 0])
        self.go(4.55, FadeOut(ring), FadeOut(films), FadeIn(claim_h), FadeIn(src_h),
                LaggedStart(*[FadeIn(c) for c in claims], lag_ratio=.2),
                LaggedStart(*[FadeIn(s) for s in sources], lag_ratio=.2), rt=.45)
        links = [Arrow([lx + .8, y, 0], [rx - .8, y, 0], buff=0, stroke_width=5, color=INK,
                       max_tip_length_to_length_ratio=.4) for y in ys]
        ticks = [check([0, y + .38, 0], .36) for y in ys]
        for t, a in zip((5.9, 6.3, 6.7), links):
            self.go(t, GrowArrow(a), rt=.3)
        for t, c in zip((7.05, 7.3, 7.55), ticks):
            self.go(t, Create(c), rt=.2)

        # Review 2: every scene is watched with its narration.
        cy = [.65, -.4, -1.45]
        fcx, wcx = -1.2, .75
        h1 = T("scene", 44, SLATE).move_to([fcx, 1.5, 0])
        h2 = T("narration", 44, TEAL).move_to([wcx, 1.5, 0])
        frames = VGroup(*[VGroup(box(fcx, y, 1.3, .9, stroke=SLATE, width=5), play_icon(fcx + .04, y, .9)) for y in cy])
        waves = VGroup(*[VGroup(box(wcx, y, 2.2, .9, stroke=TEAL, width=4), wave(wcx - .1, y, 1.6, .55, 3 + i)) for i, y in enumerate(cy)])
        vticks = [check([1.5, y, 0], .34, TEAL) for y in cy]
        self.go(8.06, FadeOut(claims), FadeOut(sources), FadeOut(claim_h), FadeOut(src_h),
                *[FadeOut(a) for a in links], *[FadeOut(c) for c in ticks], rt=.35)
        self.go(8.45, FadeIn(h1), FadeIn(h2), LaggedStart(*[FadeIn(f) for f in frames], lag_ratio=.15), rt=.4)
        self.go(8.9, LaggedStart(*[FadeIn(w) for w in waves], lag_ratio=.2), rt=.5)
        for t, c in zip((9.5, 9.8, 10.1), vticks):
            self.go(t, Create(c), rt=.2)
        self.finish()


@timed("B03")
class B03_Gates(Scene):
    def construct(self):
        head = T("quality gates", 54, SLATE).move_to([0, 3.0, 0])
        self.go(1.7, FadeIn(head, shift=UP * .1), rt=.5)

        # Phase 1: a scene token travels down a track past four gates, then reaches final.
        tx = -1.55
        ys = [2.05, 1.05, .05, -.95]
        names = ["layout", "text size", "contrast", "facts"]
        track = Line([tx, 2.45, 0], [tx, -1.95, 0], stroke_color=INK, stroke_width=6)
        rows = [VGroup(box(.4, y, 2.9, .8, stroke=SLATE, width=5), T(n, 48).move_to([.4, y, 0])) for n, y in zip(names, ys)]
        stubs = [Dot([tx, y, 0], radius=.09, color=INK) for y in ys]
        final = VGroup(box(0, -2.35, 3.7, .8, stroke=TEAL, width=0, fill=TEAL), T("final", 50, CREAM).move_to([0, -2.35, 0]))
        token = Square(side_length=.5, fill_color=GOLD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([tx, 2.45, 0])
        self.add(track, token)
        self.go(2.7, LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=.12), *[FadeIn(s) for s in stubs], FadeIn(final), rt=.9)
        for i, t in enumerate((4.46, 5.32, 6.36, 7.06)):
            self.go(t, token.animate.move_to([tx, ys[i], 0]), rows[i][0].animate.set_stroke(TEAL, 6),
                    rows[i][1].animate.set_color(TEAL), rt=.4)

        # Phase 2: a gate fails; fix the scene; render it again; it passes.
        def card(lines, y, color, h):
            lab = VGroup(*[T(s, 48, color) for s in lines]).arrange(DOWN, buff=.04)
            return VGroup(box(-.15, y, 3.2, h, stroke=color, width=5), lab.move_to([-.15, y, 0]))
        c_fail = card(["a gate fails"], 1.85, CRIMSON, .9)
        c_fix = card(["fix the scene"], .55, TEAL, .9)
        c_again = card(["render it", "again"], -.8, TEAL, 1.3)
        self.go(8.2, *[FadeOut(r) for r in rows], *[FadeOut(s) for s in stubs], FadeOut(track),
                FadeIn(c_fail, scale=.95), token.animate.move_to([1.55, 1.85, 0]), rt=.3)
        self.go(8.95, c_fail[0].animate.set_stroke(CRIMSON, 8), rt=.2)
        a1 = Arrow([-.15, 1.4, 0], [-.15, 1.02, 0], buff=0, stroke_width=6, color=INK, max_tip_length_to_length_ratio=.5)
        a2 = Arrow([-.15, .1, 0], [-.15, -.1, 0], buff=0, stroke_width=6, color=INK, max_tip_length_to_length_ratio=.9)
        loop = VMobject(stroke_color=TEAL, stroke_width=7).set_points_as_corners(
            [[1.45, -.8, 0], [1.7, -.8, 0], [1.7, 1.85, 0], [1.45, 1.85, 0]])
        tip = Triangle(fill_color=TEAL, fill_opacity=1, stroke_width=0).scale(.12).rotate(PI / 2).move_to([1.46, 1.85, 0])
        self.go(9.2, FadeIn(a1), Create(loop), FadeIn(tip), rt=.22)
        self.go(9.44, FadeIn(c_fix, scale=.95), rt=.3)
        self.go(10.4, FadeIn(a2), FadeIn(c_again, scale=.95), rt=.35)
        self.go(10.85, c_fail[0].animate.set_stroke(TEAL, 8), c_fail[1].animate.set_color(TEAL),
                token.animate.move_to([1.55, -2.35, 0]), rt=.8)

        # Phase 3: you never switch the check off.
        cap = T("check stays on", 46, TEAL).move_to([0, -1.9, 0])
        on = switch(-.9, -2.55, True, 1.5, .72)
        off = VGroup(switch(.9, -2.55, False, 1.5, .72), cross([.9, -2.55, 0], .9))
        self.go(11.7, FadeOut(final), FadeIn(cap), FadeIn(on), FadeIn(off, scale=.9), token.animate.set_opacity(0), rt=.5)
        self.finish()


@timed("B04")
class B04_Checksum(Scene):
    def construct(self):
        # The finished video file; below it a fingerprint; below that the copy on a drive.
        vlbl = T("final video", 50, SLATE).move_to([0, 3.0, 0])
        vid = VGroup(box(0, 2.1, 3.7, 1.0, stroke=SLATE, width=5), play_icon(0, 2.1, 1.1),
                     film_icon(-1.2, 2.1, .9, .7), film_icon(1.2, 2.1, .9, .7))
        slot = box(0, -2.2, 3.7, 1.1, stroke=INK, width=3, fill_opacity=0).set_stroke(opacity=.55)
        self.go(.1, FadeIn(vid, scale=.9), FadeIn(vlbl), Create(slot), rt=.5)

        # A fingerprint of the file: a drawn pattern, not a real hash.
        fp1 = fingerprint(0, 1.0, 3.3, .6, 7)
        fbox1 = box(0, 1.0, 3.7, .8, stroke=SLATE, width=4)
        clbl = T("checksum", 48, SLATE).move_to([0, .35, 0])
        self.go(2.1, FadeIn(fbox1), Create(fp1, lag_ratio=.05), FadeIn(clbl, shift=UP * .1), rt=1.0)

        # The copy on a drive carries the same fingerprint.
        drive = VGroup(box(0, -2.2, 3.7, 1.1, stroke=TEAL, width=5), cloud_icon(-1.0, -2.2, 1.0, TEAL),
                       T("Drive", 52, TEAL).move_to([.7, -2.2, 0]))
        fp2 = fingerprint(0, -1.2, 3.3, .6, 7, TEAL)
        fbox2 = box(0, -1.2, 3.7, .8, stroke=TEAL, width=4)
        self.go(6.9, FadeOut(slot), FadeIn(drive, scale=.9), rt=.5)
        self.go(7.5, FadeIn(fbox2), Create(fp2, lag_ratio=.05), rt=.9)

        # Same file, and it passed the gates.
        eq = VGroup(Line([-1.6, -.2, 0], [-.8, -.2, 0], stroke_color=INK, stroke_width=9),
                    Line([-1.6, -.5, 0], [-.8, -.5, 0], stroke_color=INK, stroke_width=9))
        same = T("same file", 52, TEAL).move_to([.5, -.35, 0])
        self.go(8.5, FadeIn(eq, scale=.8), FadeIn(same, shift=UP * .1), rt=.4)
        gate = check([1.45, 2.1, 0], .5)
        self.go(9.3, Create(gate), rt=.4)
        self.go(9.9, Indicate(eq, color=TEAL, scale_factor=1.15), rt=.5)
        self.finish()


@timed("B05")
class B05_WhatILearned(Scene):
    def construct(self):
        # A folder with five parts.
        body = box(0, -.1, 3.7, 5.2, stroke=SLATE, width=5)
        tab = Polygon([-1.75, 2.5, 0], [-.5, 2.5, 0], [-.3, 2.72, 0], [-1.75, 2.72, 0],
                      stroke_color=SLATE, stroke_width=5, fill_color=SLATE, fill_opacity=1)
        head = T("complete folder", 46, SLATE).move_to([0, 3.0, 0])
        names = ["script", "beat sheet", "fact check", "scenes", "write-up"]
        ry = [1.75, .77, -.21, -1.19, -2.17]
        slots = VGroup(*[dashed(box(0, y, 3.3, .8, stroke=INK, width=2, fill_opacity=0), 22) for y in ry])
        rows = [VGroup(box(0, y, 3.3, .8, stroke=TEAL, width=4), T(n, 48).move_to([0, y, 0])) for n, y in zip(names, ry)]
        self.go(.1, FadeIn(body), FadeIn(tab), Create(slots), rt=.5)
        self.go(1.76, FadeIn(head, shift=UP * .1), rt=.45)
        for t, r in zip((3.28, 4.16, 5.14, 6.26, 7.14), rows):
            self.go(t, FadeIn(r, shift=RIGHT * .2), rt=.3)
        done = check([1.5, 2.2, 0], .5)
        self.go(7.5, Create(done), rt=.35)

        # Better at the terminal with Claude Code: the folder clears, the skill bar grows.
        folder = VGroup(body, tab, head, slots, *rows, done)
        term = VGroup(box(0, 1.65, 3.7, 2.5, stroke=SLATE, width=5),
                      Rectangle(width=3.7, height=.6, fill_color=SLATE, fill_opacity=1, stroke_width=0).move_to([0, 2.6, 0]),
                      M(">_ claude", 40, CREAM).move_to([-.2, 2.6, 0]),
                      M("> better", 40, INK).move_to([-.75, 1.8, 0]).align_to([-1.6, 0, 0], LEFT))
        track = RoundedRectangle(corner_radius=.17, width=3.2, height=.36, stroke_color=SLATE, stroke_width=4,
                                 fill_opacity=0).move_to([0, .95, 0])
        fill = RoundedRectangle(corner_radius=.17, width=.8, height=.36, fill_color=TEAL, fill_opacity=1,
                               stroke_width=0).move_to(track.get_left() + RIGHT * .4)
        full = RoundedRectangle(corner_radius=.17, width=3.2, height=.36, fill_color=TEAL, fill_opacity=1,
                                stroke_width=0).move_to(track.get_center())
        self.go(8.45, FadeOut(folder), FadeIn(term), Create(track), FadeIn(fill), rt=.4)
        self.go(10.2, Transform(fill, full), rt=1.3)

        # Humanitarians AI helped: a plain badge sends a helped-arrow to the terminal.
        badge = VGroup(box(0, -2.15, 3.7, 1.3, stroke=SLATE, width=5, fill=SLATE),
                       VGroup(T("Humanitarians", 46, CREAM), T("AI", 46, CREAM)).arrange(DOWN, buff=.04).move_to([0, -2.15, 0]))
        up = Arrow([-.9, -1.45, 0], [-.9, -.1, 0], buff=0, stroke_width=7, color=TEAL)
        helped = T("helped", 50, TEAL).move_to([.6, -.8, 0])
        self.go(11.88, FadeIn(badge, shift=UP * .15), rt=.5)
        self.go(13.06, GrowArrow(up), FadeIn(helped), rt=.5)
        self.finish()
