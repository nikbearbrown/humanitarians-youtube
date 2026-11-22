"""Manim scenes for "How Google Docs Lets Two People Type in the Same Sentence" (Keya G.).

Scenes, one per Manim beat in beat_sheet.json:
B02_Hook             two plain windows, overlapping typing, Ctrl+Z undoes only my words
B04_TheProblem       a, b, c; an x goes in at the start; the delete, applied as sent, hits the wrong letter
B05_TwoCopies        your browser and the server; only small changes travel, never the whole page
B06_Transformation   two operations clash; the delete is rewritten from the third letter to the fourth
B07_Protocol         the server numbers changes as they arrive, acknowledges, passes on, keeps a log
B08_CursorsDelay     who made each change (my guess), a teammate's cursor, a letter that arrives late
B09_Crdts            two copies change on their own, with no coordination, and end up the same
B10_Messy            a slow connection and two different rewrites of one sentence

Simple drawn shapes only: no Google logo, no Docs interface or screenshots, no Google colours used as
branding. The windows are plain rounded rectangles with a text line. Every example is an illustration,
not data. The only numbers are slot numbers under the a-b-c tiles and 1, 2 in the revision log.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings measured
from each beat's narration audio (faster-whisper), so re-check them if that audio is regenerated.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
DUR = {"B02": 18.07, "B04": 19.80, "B05": 15.13, "B06": 21.76, "B07": 23.47, "B08": 16.17,
       "B09": 15.83, "B10": 17.45}
if (HERE / "beat_sheet.json").is_file():
    DUR = {b["beat_id"]: b["actual_duration_s"]
           for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # my teammate / the kept result
CRIMSON = "#E4572E"   # me / the one accent per beat
MUTED = "#5C5448"     # secondary text
PALE = "#9C927F"      # thin structure lines
PAPER = "#EADFCB"     # card fill
BORDER = "#6A604F"    # outline of cards/windows that enclose text (kept off the ink mask)

SAFE_X, SAFE_Y = 6.25, 3.4
MIN_FS = 30           # smallest text allowed in a scene (at 8 units tall)
PORTRAIT = False
HEAD_Y = 2.9


def T(text, size=40, color=INK, max_w=None, **kw):
    """Text that is never scaled: if it is too wide the font size itself is reduced, so the size a
    scene reports is the size on screen."""
    m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    while max_w and m.width > max_w and size > MIN_FS:
        size -= 2
        m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    return m


def check_mark(x, y, s=.3, color=TEAL, w=9):
    return VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[x - s, y, 0], [x - s * .35, y - s * .75, 0], [x + s, y + s * .8, 0]])


def cross_mark(x, y, s=.28, color=INK, w=9):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], stroke_color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], stroke_color=color, stroke_width=w))


def poly(pts, color=INK, w=7):
    return VMobject(stroke_color=color, stroke_width=w, fill_opacity=0).set_points_as_corners(
        [[x, y, 0] for x, y in pts])


def win(w, h, title=None):
    """A plain window: rounded rectangle, a thin bar with three pale dots, an optional small title."""
    body = RoundedRectangle(width=w, height=h, corner_radius=.2, stroke_color=BORDER, stroke_width=5,
                            fill_color=PAPER, fill_opacity=1)
    bar = Line([-w / 2, h / 2 - .62, 0], [w / 2, h / 2 - .62, 0], stroke_color=PALE, stroke_width=4)
    dots = VGroup(*[Dot(radius=.07, color=PALE) for _ in range(3)]).arrange(RIGHT, buff=.15
                                                                          ).move_to([-w / 2 + .55, h / 2 - .31, 0])
    g = VGroup(body, bar, dots)
    if title:
        g.add(T(title, 32, MUTED).move_to([0, h / 2 - .31, 0]))
    return g


def tile(ch, s=1.5, color=INK, fs=84):
    box = RoundedRectangle(width=s, height=s, corner_radius=.15, stroke_color=BORDER, stroke_width=6,
                           fill_color=PAPER, fill_opacity=1)
    t = T(ch, fs, color).move_to(box)
    return VGroup(box, t)


def chip(text, color, fs=34, pad=.3):
    t = T(text, fs, color)
    box = RoundedRectangle(width=t.width + pad * 2, height=t.height + pad * 1.1, corner_radius=.18,
                           stroke_color=color, stroke_width=5, fill_color=CREAM, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def packet(text, color, fs=32):
    t = T(text, fs, color)
    box = RoundedRectangle(width=t.width + .4, height=t.height + .38, corner_radius=.14, stroke_color=color,
                           stroke_width=4, fill_color=CREAM, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def server_shape(w, h, label=None):
    body = RoundedRectangle(width=w, height=h, corner_radius=.2, stroke_color=BORDER, stroke_width=5,
                            fill_color=PAPER, fill_opacity=1)
    g = VGroup(body)
    if label:
        g.add(T(label, 36, INK).move_to([0, h / 2 - .4, 0]))
    return g


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
        """items: [(offset_s, animation)] -> one play that starts each animation `offset_s` after t."""
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
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because the runner finds
    scenes by that exact text, so a Scene subclass would be missed."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


def typed(text, color, size=44):
    return T(text, size, color)


# ------------------------------------------------------------------------------------------
@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        # 0.3: a shared document, seen from two windows
        head = T("one shared document", 52, MUTED).move_to([0, HEAD_Y, 0])
        wl = win(5.9, 3.5, "me").move_to([-3.2, .65, 0])
        wr = win(5.9, 3.5, "my teammate").move_to([3.2, .65, 0])
        wl.set_stroke(color="#A89E8C"); wr.set_stroke(color="#A89E8C")   # lighter outline, as in the portrait cut (keeps the ring from reading as a text run)
        baseL = typed("Plan:", INK).move_to([-5.0, .45, 0])
        baseR = typed("Plan:", INK).move_to([1.4, .45, 0])
        self.go(.2, FadeIn(head), FadeIn(wl), FadeIn(wr), FadeIn(baseL), FadeIn(baseR), rt=.7)

        # 2.1: two people type in the same line
        callL = typed("call", CRIMSON).next_to(baseL, RIGHT, buff=.25)
        sendR = typed("send", TEAL).next_to(baseR, RIGHT, buff=.25)
        self.go(2.08, AddTextLetterByLetter(callL, time_per_char=.12), AddTextLetterByLetter(sendR, time_per_char=.12),
                rt=None)

        # 4.8: the text overlaps for a moment: each window gets the other's words, jammed against its own
        sendL = typed("send", TEAL).next_to(callL, RIGHT, buff=.02)
        callR = typed("call", CRIMSON).next_to(sendR, RIGHT, buff=.02)
        zigL = poly([(sendL.get_left()[0] - .02, .1), (sendL.get_left()[0] + .08, .85), (sendL.get_left()[0] - .06, .45),
                     (sendL.get_left()[0] + .06, 0.0)], CRIMSON, 5)
        zigR = poly([(callR.get_left()[0] - .02, .1), (callR.get_left()[0] + .08, .85), (callR.get_left()[0] - .06, .45),
                     (callR.get_left()[0] + .06, 0.0)], CRIMSON, 5)
        ov = T("text overlaps", 40, MUTED).move_to([0, -1.55, 0])
        self.go(4.8, FadeIn(sendL, shift=LEFT * .5), FadeIn(callR, shift=RIGHT * .5), FadeIn(ov), rt=.7)
        # 6.1: it settles, spaced apart
        self.go(6.18, sendL.animate.next_to(callL, RIGHT, buff=.28), callR.animate.next_to(sendR, RIGHT, buff=.28),
                FadeOut(ov), rt=.6)

        # 8.1: press Ctrl+Z in the left window
        key = chip("Ctrl+Z", INK, 38).move_to([-4.85, -.45, 0])
        cap1 = T("press Ctrl+Z in my window", 46).move_to([0, -2.7, 0])
        self.go(8.14, FadeIn(key, scale=1.3), FadeIn(cap1), rt=.4)
        # 10.0: will it undo my teammate's work too?
        q = T("?", 90, CRIMSON, weight="BOLD").move_to([5.4, -.35, 0])
        cap2 = T("will it undo my teammate's work too?", 46).move_to([0, -2.7, 0])
        self.go(10.0, Transform(cap1, cap2), FadeIn(q, scale=.6), rt=.5)
        # 12.0: tested in two windows
        cap3 = T("I tested it in two windows", 46).move_to([0, -2.7, 0])
        self.go(12.04, Transform(cap1, cap3), FadeOut(q), rt=.5)
        # 14.0: it only undid mine
        self.go(14.15, FadeOut(callL, scale=.6), FadeOut(callR, scale=.6), FadeOut(key), rt=.6)
        cap4 = T("it only undid mine", 52, CRIMSON).move_to([0, -2.7, 0])
        self.go(14.55, Transform(cap1, cap4), rt=.4)
        # 15.7: how does it keep track?
        cap5 = T("How does it keep track?", 56).move_to([0, -2.7, 0])
        self.go(15.75, Transform(cap1, cap5), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
P4 = [-3.0, -1.0, 1.0, 3.0]    # four slots, left to right
ROW4 = -.25


@timed("B04")
class B04_TheProblem(Scene):
    def construct(self):
        head = T("why this is hard", 56).move_to([0, HEAD_Y, 0])
        a, b, c = tile("a", 1.6), tile("b", 1.6), tile("c", 1.6)
        for t, x in zip((a, b, c), P4[:3]):
            t.move_to([x, ROW4, 0])
        slots = [T(str(i + 1), 40, MUTED).move_to([P4[i], ROW4 - 1.35, 0]) for i in range(4)]
        ex = T("an illustrative example", 34, MUTED).move_to([0, -3.1, 0])
        self.go(.1, FadeIn(head), rt=.5)
        # 1.76: the document says a, b, c
        self.go(1.76, *[FadeIn(t, shift=DOWN * .15) for t in (a, b, c)], *[FadeIn(s) for s in slots[:3]], FadeIn(ex),
                rt=.8)

        # 4.2: at the same moment, two people act
        me = chip("me: add x at the start", CRIMSON, 36).move_to([-3.3, 2.15, 0])
        tm = chip("teammate: delete the third letter", TEAL, 36).move_to([3.0, 2.15, 0])
        xt = tile("x", 1.6, CRIMSON).move_to([P4[0], 1.0, 0])
        del_arrow = Arrow([P4[2], 1.45, 0], [P4[2], ROW4 + .95, 0], buff=0, color=TEAL, stroke_width=9,
                          max_tip_length_to_length_ratio=.35)
        self.go(4.4, FadeIn(me, shift=DOWN * .1), rt=.4)
        self.go(5.5, FadeIn(xt, scale=.6), rt=.4)
        self.go(7.0, FadeIn(tm, shift=DOWN * .1), rt=.4)
        self.go(8.1, Create(del_arrow), rt=.4)

        # 9.72: x pushes everything one place to the right; slot numbers stay put
        s4 = slots[3]
        self.go(9.9, xt.animate.move_to([P4[0], ROW4, 0]), a.animate.move_to([P4[1], ROW4, 0]),
                b.animate.move_to([P4[2], ROW4, 0]), c.animate.move_to([P4[3], ROW4, 0]), FadeIn(s4), rt=1.4)
        # 12.5: so the third letter is now b
        ring = SurroundingRectangle(b, color=TEAL, buff=.12, stroke_width=7, corner_radius=.2)
        third = T("slot 3 is now b", 44).move_to([0, -2.45, 0])
        self.go(12.6, Create(ring), FadeIn(third), rt=.6)
        # 14.56: applied exactly as it was sent: the delete lands on b; 18.1: the wrong letter gets deleted
        self.go(14.9, FadeOut(third), FadeOut(ring), rt=.3)
        x_b = cross_mark(P4[2], ROW4 + 1.3, .3, CRIMSON, 12)
        ring2 = SurroundingRectangle(b, color=CRIMSON, buff=.12, stroke_width=7, corner_radius=.2)
        wrong = T("wrong letter", 52, CRIMSON).move_to([0, -2.45, 0])
        self.go(18.1, Create(x_b), Create(ring2), FadeIn(wrong, shift=UP * .1), rt=.7)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B05")
class B05_TwoCopies(Scene):
    def construct(self):
        # 1.66: it runs in two places
        bw = win(5.0, 4.4, None).move_to([-3.8, -.1, 0])
        page = RoundedRectangle(width=2.4, height=1.7, corner_radius=.12, stroke_color=BORDER, stroke_width=4,
                                fill_color=CREAM, fill_opacity=1).move_to([-3.8, .75, 0])
        lines = VGroup(*[Line([-5.1, 1.35 - i * .38, 0], [-3.1 - (.5 if i == 3 else 0), 1.35 - i * .38, 0],
                              stroke_color=PALE, stroke_width=5) for i in range(4)])
        rb = [RoundedRectangle(width=4.5, height=.62, corner_radius=.1, stroke_color=BORDER, stroke_width=4,
                               fill_color=CREAM, fill_opacity=1).move_to([-3.8, y, 0]) for y in (-.7, -1.5)]
        srv = win(3.9, 4.4, None).move_to([4.3, -.1, 0])
        rs = [RoundedRectangle(width=3.5, height=.72, corner_radius=.1, stroke_color=BORDER, stroke_width=4,
                               fill_color=CREAM, fill_opacity=1).move_to([4.3, y, 0]) for y in (.75, -.15, -1.05)]
        lab_b = T("your browser", 48).move_to([-3.8, 2.65, 0])
        lab_s = T("the server", 48).move_to([4.3, 2.65, 0])
        self.go(1.66, FadeIn(bw), FadeIn(page), FadeIn(lines), *[FadeIn(r) for r in rb], FadeIn(srv),
                *[FadeIn(r) for r in rs], rt=.8)
        self.go(3.68, FadeIn(lab_b, shift=DOWN * .1), rt=.4)
        self.go(4.86, FadeIn(lab_s, shift=DOWN * .1), rt=.4)

        # 7.58: your browser doesn't send the whole document: the big page would go, crossed out
        ghost = page.copy().set_stroke(color=MUTED)
        gx = cross_mark(0, .75, .6, CRIMSON, 11)
        no = T("not the whole document", 42, MUTED).move_to([0, -2.95, 0])
        self.go(8.0, FadeIn(no), FadeIn(ghost, scale=1.0), rt=.3)
        self.go(8.3, ghost.animate.move_to([0, .75, 0]), rt=.9)
        self.go(9.3, Create(gx), rt=.4)
        self.go(9.9, FadeOut(ghost), FadeOut(gx), FadeOut(no), rt=.4)

        # 10.02: it sends only your changes to the server
        p1 = packet("insert x", CRIMSON).move_to([-.7, .75, 0])
        only = T("only your changes", 44, CRIMSON).move_to([0, -2.95, 0])
        self.go(10.2, FadeIn(p1, shift=RIGHT * .3), FadeIn(only), rt=.4)
        self.go(10.7, p1.animate.move_to([1.5, .75, 0]), rt=1.1)
        self.go(11.9, FadeOut(p1, scale=.5), rt=.3)

        # 12.72: and receives everyone else's changes back
        p2 = packet("delete c", TEAL).move_to([1.5, -.1, 0])
        back = T("everyone else's changes", 40, TEAL).move_to([0, -2.95, 0])
        self.go(12.5, Transform(only, back), FadeIn(p2, shift=LEFT * .3), rt=.4)
        self.go(13.1, p2.animate.move_to([-.7, -.1, 0]), rt=1.0)
        self.go(14.1, FadeOut(p2, scale=.5), rt=.3)

        # what each side keeps (small, inside the boxes)
        lb = [T("changes not yet sent", 30, MUTED).move_to(rb[0]), T("sent, not yet acknowledged", 30, MUTED).move_to(rb[1])]
        ls = [T("changes received", 32, MUTED).move_to(rs[0]), T("revision log", 32, MUTED).move_to(rs[1]),
              T("current document", 32, MUTED).move_to(rs[2])]
        self.go(14.4, FadeOut(only), *[FadeIn(t) for t in lb + ls], rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B06")
class B06_Transformation(Scene):
    def construct(self):
        head = T("operational transformation", 60).move_to([0, HEAD_Y, 0])
        a, b, c = tile("a", 1.5), tile("b", 1.5), tile("c", 1.5)
        for t, x in zip((a, b, c), P4[:3]):
            t.move_to([x, -1.0, 0])
        slots = [T(str(i + 1), 40, MUTED).move_to([P4[i], -2.2, 0]) for i in range(4)]
        self.go(.1, FadeIn(a), FadeIn(b), FadeIn(c), *[FadeIn(s) for s in slots[:3]], rt=.5)
        self.go(3.62, FadeIn(head, shift=DOWN * .1), rt=.5)

        # 5.72: each edit is an operation
        op1 = chip("insert x at the start", CRIMSON, 34).move_to([-3.9, 1.65, 0])
        op2 = chip("delete the third letter", TEAL, 34).move_to([3.9, 1.65, 0])
        self.go(7.7, FadeIn(op1, shift=DOWN * .1), rt=.4)
        self.go(9.7, FadeIn(op2, shift=DOWN * .1), rt=.4)
        arrow = Arrow([P4[2], .1, 0], [P4[2], -.1 + .0, 0], buff=0, color=TEAL, stroke_width=1)
        arrow = Arrow([P4[2], .55, 0], [P4[2], -.1, 0], buff=0, color=TEAL, stroke_width=9,
                      max_tip_length_to_length_ratio=.4)
        self.go(10.3, Create(arrow), rt=.3)

        # 11.32: when two operations clash: the x goes in, the row shifts, the arrow still points at slot 3
        diamond = Square(side_length=1.3, color=INK, stroke_width=6, fill_color=CREAM, fill_opacity=1
                         ).rotate(PI / 4).move_to([0, 1.65, 0])
        dl = T("transform", 32, INK).move_to([0, 1.65, 0])
        x = tile("x", 1.5, CRIMSON).move_to([P4[0], 0.8, 0])
        self.go(11.5, FadeIn(x, scale=.6), rt=.4)
        self.go(12.1, x.animate.move_to([P4[0], -1.0, 0]), a.animate.move_to([P4[1], -1.0, 0]),
                b.animate.move_to([P4[2], -1.0, 0]), c.animate.move_to([P4[3], -1.0, 0]), FadeIn(slots[3]), rt=1.0)
        clash = T("clash", 44, CRIMSON).move_to([0, -3.0, 0])
        self.go(13.1, FadeIn(clash), rt=.3)
        # 13.34: one is transformed to fit the other
        op2b = chip("delete the fourth letter", TEAL, 34).move_to([3.9, 1.65, 0])
        self.go(13.6, FadeOut(clash), FadeIn(diamond), FadeIn(dl), rt=.4)
        self.go(14.3, Transform(op2, op2b), rt=.7)
        # 15.76: shifted from the third letter to the fourth
        self.go(17.6, arrow.animate.shift(RIGHT * 2.0), rt=.9)
        ring = SurroundingRectangle(c, color=TEAL, buff=.12, stroke_width=7, corner_radius=.2)
        self.go(18.6, Create(ring), rt=.3)
        # 19.12: so the c is deleted, just as they meant
        done = T("just as they meant", 52).move_to([0, -2.95, 0])
        self.go(19.4, FadeOut(c, scale=.4), FadeOut(ring), FadeOut(arrow), rt=.6)
        self.go(20.9, FadeIn(done, shift=UP * .1), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B07")
class B07_Protocol(Scene):
    def construct(self):
        srv = server_shape(2.8, 5.2).move_to([0, 0, 0])
        lab_s = T("server", 44).move_to([0, 2.1, 0])
        lg = T("revision log", 32, MUTED).move_to([0, 1.45, 0])
        me_w = win(2.2, 2.6, None).move_to([-5.1, .3, 0])
        tm_w = win(2.2, 2.6, None).move_to([5.1, .3, 0])
        me_l = T("me", 44, CRIMSON).move_to([-5.1, 2.0, 0])
        tm_l = T("teammate", 44, TEAL).move_to([5.1, 2.0, 0])
        self.go(.1, FadeIn(srv), FadeIn(lab_s), FadeIn(lg), FadeIn(me_w), FadeIn(tm_w), FadeIn(me_l), FadeIn(tm_l),
                rt=.6)
        # 2.1: every copy needs the same changes in the same order
        same = T("same changes, same order", 48).move_to([0, -3.05, 0])
        self.go(2.1, FadeIn(same), rt=.4)
        part2 = T("the collaboration protocol", 48, INK).move_to([0, -3.05, 0])
        self.go(7.5, Transform(same, part2), rt=.5)

        # 9.36: the server processes changes in the order they arrive
        c1 = packet("insert x", CRIMSON).move_to([-3.1, .65, 0])
        c2 = packet("delete c", TEAL).move_to([3.1, -.4, 0])
        row1 = chip("1  insert x", CRIMSON, 30, .18).move_to([0, .6, 0])
        row2 = chip("2  delete c", TEAL, 30, .18).move_to([0, -.4, 0])
        self.go(9.4, FadeIn(c1, shift=RIGHT * .3), rt=.3)
        self.go(9.8, c1.animate.move_to([-2.2, .65, 0]), rt=.7)
        self.go(10.6, FadeOut(c1, scale=.5), FadeIn(row1, scale=.8), rt=.3)
        self.go(11.0, FadeIn(c2, shift=LEFT * .3), rt=.3)
        self.go(11.4, c2.animate.move_to([2.2, -.4, 0]), rt=.6)
        self.go(12.0, FadeOut(c2, scale=.5), FadeIn(row2, scale=.8), rt=.3)

        # 12.96: an acknowledgement goes back to the person who made the change
        ck1 = check_mark(-5.1, -1.5, .26, CRIMSON, 10)
        ak1 = T("acknowledged", 32, CRIMSON).move_to([-5.1, -2.15, 0])
        ck2 = check_mark(5.1, -1.5, .26, TEAL, 10)
        ak2 = T("acknowledged", 32, TEAL).move_to([5.1, -2.15, 0])
        self.go(13.5, FadeIn(ck1, shift=LEFT * .4), FadeIn(ak1), rt=.5)
        self.go(14.9, FadeIn(ck2, shift=RIGHT * .4), FadeIn(ak2), rt=.5)
        # 16.5: it passes the change on to everyone else
        p1 = packet("insert x", CRIMSON).move_to([2.2, .65, 0])
        p2 = packet("delete c", TEAL).move_to([-2.2, -.4, 0])
        p1s = T("passed on", 34, MUTED).move_to([3.0, 1.6, 0])
        self.go(16.4, FadeOut(ck1), FadeOut(ak1), FadeOut(ck2), FadeOut(ak2), FadeIn(p1, shift=RIGHT * .3), rt=.4)
        self.go(16.9, p1.animate.move_to([3.1, .65, 0]), FadeIn(p1s), rt=.6)
        self.go(17.6, FadeOut(p1, scale=.5), Indicate(tm_w, color=CRIMSON, scale_factor=1.04), rt=.5)
        self.go(18.2, FadeOut(p1s), FadeIn(p2, shift=LEFT * .3), rt=.3)
        self.go(18.5, p2.animate.move_to([-3.1, -.4, 0]), rt=.5)
        self.go(19.1, FadeOut(p2, scale=.5), Indicate(me_w, color=TEAL, scale_factor=1.04), rt=.5)
        # 18.74: and keeps every change in a revision log: the complete history of the document
        box = SurroundingRectangle(VGroup(row1, row2), color=CRIMSON, buff=.25, stroke_width=6, corner_radius=.2)
        hist = T("the complete history of the document", 46).move_to([0, -3.05, 0])
        self.go(19.7, Create(box), lg.animate.set_color(INK), rt=.5)
        self.go(21.28, Transform(same, hist), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B08")
class B08_CursorsDelay(Scene):
    def construct(self):
        # 0: in my test
        test = T("in my test", 44, MUTED).move_to([-2.4, HEAD_Y, 0])
        w = win(7.8, 3.4, None).move_to([-2.4, .75, 0])
        base = T("Plan:", 52, INK).move_to([-5.3, .5, 0])
        call = T("call", 52, CRIMSON).next_to(base, RIGHT, buff=.28)
        send = T("send", 52, TEAL).next_to(call, RIGHT, buff=.28)
        tm = win(2.5, 1.5, None).move_to([5.0, 2.2, 0])
        tm_l = T("teammate", 36, TEAL).move_to([5.0, 2.0, 0])
        sv = server_shape(2.5, 1.6).move_to([5.0, -.7, 0])
        sv_l = T("server", 36, INK).move_to([5.0, -.7, 0])
        self.go(.1, FadeIn(test), FadeIn(w), FadeIn(base), FadeIn(call), FadeIn(send), FadeIn(tm), FadeIn(tm_l),
                FadeIn(sv), FadeIn(sv_l), rt=.6)
        # 0.96: Ctrl+Z
        key = chip("Ctrl+Z", INK, 38).move_to([-.2, 1.95, 0])
        self.go(1.0, FadeIn(key, scale=1.3), rt=.3)
        self.go(1.9, FadeOut(call, scale=.6), rt=.5)
        ghost = DashedVMobject(RoundedRectangle(width=1.5, height=.8, corner_radius=.1, stroke_color=CRIMSON,
                                                stroke_width=5), num_dashes=24).move_to(call)
        cap = T("only my own typing", 46, CRIMSON).move_to([-2.4, -1.75, 0])
        self.go(2.45, FadeIn(ghost), FadeIn(cap), FadeOut(key), rt=.4)
        # 3.84: the document must keep track of who made each change (my guess)
        tag_t = chip("made by my teammate", TEAL, 32, .22).move_to([-2.1, 1.7, 0])
        tag_m = chip("made by me, undone", CRIMSON, 32, .22).move_to([-3.4, -.4, 0])
        guess = T("who made each change? my guess", 40, MUTED).move_to([-2.4, -2.65, 0])
        self.go(4.3, FadeOut(cap), FadeIn(tag_t), FadeIn(tag_m), rt=.5)
        self.go(5.7, FadeIn(guess), rt=.4)
        # 7.34: I can also see where my teammate's cursor is
        self.go(8.2, FadeOut(tag_t), FadeOut(tag_m), FadeOut(guess), FadeOut(ghost), rt=.3)
        cx = send.get_right()[0] + .35
        cur = Line([cx, .1, 0], [cx, .95, 0], stroke_color=TEAL, stroke_width=9)
        cur_tag = chip("teammate", TEAL, 32, .2).next_to(cur, UP, buff=.12)
        self.go(8.5, FadeIn(cur), FadeIn(cur_tag), rt=.4)
        self.go(9.0, cur.animate.shift(RIGHT * 1.2), cur_tag.animate.shift(RIGHT * 1.2), rt=.6)
        # 10.32: sometimes their text shows up a moment late: the server round trip
        l1 = Line([5.0, 1.4, 0], [5.0, .1, 0], stroke_color=PALE, stroke_width=5)
        l2 = Line([3.75, -.7, 0], [3.0, -.7, 0], stroke_color=PALE, stroke_width=5)
        l3 = Line([3.0, -.7, 0], [3.0, -1.4, 0], stroke_color=PALE, stroke_width=5)
        self.go(10.0, FadeIn(l1), FadeIn(l2), FadeIn(l3), rt=.5)
        late = T("a moment late", 46).move_to([-2.4, -1.75, 0])
        self.go(10.6, FadeIn(late), rt=.4)
        dot = Dot([5.0, 1.4, 0], radius=.2, color=TEAL)
        self.go(12.7, FadeIn(dot), rt=.2)
        self.go(13.0, dot.animate.move_to([5.0, .1, 0]), rt=.7)
        self.go(13.8, dot.animate.move_to([3.0, -.7, 0]), rt=.6)
        self.go(14.5, dot.animate.move_to([3.0, -1.4, 0]), rt=.4)
        ok = T("ok", 52, TEAL).next_to(cur, LEFT, buff=.2).shift(DOWN * .0)
        self.go(15.0, FadeOut(dot), FadeIn(ok, scale=.6), rt=.4)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B09")
class B09_Crdts(Scene):
    def construct(self):
        wl = win(5.8, 3.0, "copy 1").move_to([-3.5, .2, 0])
        wr = win(5.8, 3.0, "copy 2").move_to([3.5, .2, 0])
        baseL = T("Plan:", 48, INK).move_to([-5.0, -.05, 0])
        baseR = T("Plan:", 48, INK).move_to([2.0, -.05, 0])
        small = T("I'm just starting to learn", 34, MUTED).move_to([-3.4, -3.1, 0])
        self.go(.2, FadeIn(wl), FadeIn(wr), FadeIn(baseL), FadeIn(baseR), FadeIn(small), rt=.7)
        # 2.92: called CRDT
        crdt = T("CRDT", 84, INK, weight="BOLD").move_to([0, 2.95, 0])
        self.go(3.1, FadeIn(crdt, shift=DOWN * .1), rt=.4)
        long = T("conflict-free replicated data type", 44, MUTED).move_to([0, 2.4, 0])
        crdt2 = T("CRDT", 72, INK, weight="BOLD").move_to([0, 3.0, 0])
        self.go(5.16, Transform(crdt, crdt2), FadeIn(long), rt=.5)
        # 8.0: each copy can be changed on its own, at the same time
        callL = T("call", 48, CRIMSON).next_to(baseL, RIGHT, buff=.28)
        sendR = T("send", 48, TEAL).next_to(baseR, RIGHT, buff=.28)
        self.go(8.9, AddTextLetterByLetter(callL, time_per_char=.12), AddTextLetterByLetter(sendR, time_per_char=.12),
                rt=None)
        same_t = T("on its own, at the same time", 46).move_to([0, -2.3, 0])
        self.go(9.7, FadeIn(same_t, shift=UP * .1), rt=.4)
        # 11.68: without coordinating with the others
        gap = DashedLine([0, 1.5, 0], [0, -1.4, 0], color=MUTED, stroke_width=6, dash_length=.18)
        noc = T("no coordination", 38, MUTED).move_to([0, 1.95, 0])
        crx = cross_mark(0, .1, .3, CRIMSON, 9)
        nocap = T("without coordinating with the others", 44).move_to([0, -2.3, 0])
        self.go(11.7, Transform(same_t, nocap), Create(gap), FadeIn(noc), rt=.5)
        self.go(12.3, Create(crx), rt=.4)
        # 13.68: the copies still end up the same
        sendL = T("send", 48, TEAL).next_to(callL, RIGHT, buff=.28)
        callR = T("call", 48, CRIMSON).next_to(sendR, RIGHT, buff=.28)
        same = T("the copies still end up the same", 46, TEAL).move_to([0, -2.3, 0])
        eq = T("=", 100, TEAL, weight="BOLD").move_to([0, .1, 0])
        self.go(13.7, FadeOut(crx), FadeOut(gap), FadeOut(noc), Transform(same_t, same),
                FadeIn(sendL, shift=LEFT * .4), FadeIn(callR, shift=RIGHT * .4), rt=.8)
        self.go(14.6, FadeIn(eq, scale=.5), rt=.4)
        self.go(15.0, FadeIn(T("simplified", 34, MUTED).move_to([5.0, -3.1, 0])), rt=.3)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B10")
class B10_Messy(Scene):
    def construct(self):
        # left panel, built centred and moved left when the right panel opens
        exp = T("in my experience", 44, MUTED).move_to([0, HEAD_Y, 0])
        wl = win(5.4, 2.1, None).move_to([0, 1.25, 0])
        base = T("Plan: call", 46, CRIMSON).move_to([-1.2, .95, 0])
        sv = server_shape(2.4, 1.3).move_to([0, -2.0, 0])
        sv.set_stroke(color="#A89E8C")   # lighter outline: keeps the small server box from fusing with its label
        sv_l = T("server", 36, INK).move_to([0, -2.0, 0])
        path = DashedVMobject(CubicBezier([-2.0, .2, 0], [-3.4, -.6, 0], [-3.4, -2.0, 0], [-1.3, -2.0, 0]
                                          ).set_stroke(MUTED, 6), num_dashes=22)
        path2 = DashedVMobject(CubicBezier([1.3, -2.0, 0], [3.4, -2.0, 0], [3.4, -.6, 0], [2.0, .2, 0]
                                           ).set_stroke(MUTED, 6), num_dashes=22)
        slow = T("a slow connection", 44).move_to([0, -3.05, 0])
        left = VGroup(wl, base, sv, sv_l, path, path2, slow)
        self.go(.1, FadeIn(exp), FadeIn(left), rt=.7)
        # 4.14: text can appear late
        dot = Dot([-2.0, .2, 0], radius=.2, color=TEAL)
        self.go(3.9, FadeIn(dot), rt=.3)
        self.go(4.2, MoveAlongPath(dot, CubicBezier([-2.0, .2, 0], [-3.4, -.6, 0], [-3.4, -2.0, 0], [-1.3, -2.0, 0])),
                rt=1.2)
        self.go(5.5, dot.animate.move_to([1.3, -2.0, 0]), rt=.6)
        self.go(6.1, MoveAlongPath(dot, CubicBezier([1.3, -2.0, 0], [3.4, -2.0, 0], [3.4, -.6, 0], [2.0, .2, 0])),
                rt=.9)
        # 5.74: overlap for a moment before it settles
        late = T("send", 46, TEAL).next_to(base, RIGHT, buff=.02)
        self.go(7.05, FadeOut(dot), FadeIn(late), rt=.3)
        self.go(7.4, late.animate.next_to(base, RIGHT, buff=.3), rt=.4)
        # 8.2: two people rewrite the same sentence in different ways
        group = VGroup(left, late, exp)
        self.go(7.6, group.animate.shift(LEFT * 3.0), rt=.4)
        wr = win(5.2, 3.7, None).move_to([3.7, .8, 0])
        a = T("Send draft today", 44, CRIMSON).move_to([3.7, 1.2, 0])
        b = T("Share plan Monday", 44, TEAL).move_to([3.7, .2, 0])
        fr = T("framing, not a measurement", 34, MUTED).move_to([3.7, -3.0, 0])
        self.go(8.0, FadeIn(wr), rt=.25)
        self.go(8.2, FadeIn(a, shift=RIGHT * .3), rt=.3)
        self.go(10.4, FadeIn(b, shift=LEFT * .3), rt=.4)
        # 12.1: the system can merge both edits; 14.2: it can't decide which wording was wanted
        keep = T("both kept", 44, TEAL).move_to([3.7, -.55, 0])
        self.go(12.6, FadeIn(keep), FadeIn(fr), rt=.4)
        q = T("which wording did\nthe team want?", 42, CRIMSON, line_spacing=.9).move_to([3.7, -2.0, 0])
        self.go(14.6, FadeIn(q, shift=UP * .1), rt=.5)
        self.finish()
