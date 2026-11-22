"""Native 9:16 layouts for "How Google Docs Lets Two People Type in the Same Sentence" (Keya G.).

Same scene names, colours, words and go() cues as ../scenes.py, redrawn for a tall frame
(4.5 x 8 Manim units at 2160x3840). Nothing here is a crop or a squeeze of the landscape film:
one idea at a time, stacked top to bottom, bigger type, short lines.

B02_Hook             two windows stacked; overlapping typing; Ctrl+Z undoes only my words
B04_TheProblem       a, b, c in a row; me, then the teammate; the delete lands on the wrong letter
B05_TwoCopies        the browser on top, the server below; small changes travel down and back up
B06_Transformation   two operations stacked; a diamond between; the delete moves from slot 3 to slot 4
B07_Protocol         big words first, then me / server / teammate in a column; numbering, acks, log
B08_CursorsDelay     one window, who made each change (my guess), a cursor; then the round trip
B09_Crdts            two copies stacked, changed on their own, ending up the same
B10_Messy            first a slow connection, then (one idea at a time) two rewrites of one sentence

Simple drawn shapes only: no Google logo, no Docs interface or screenshots, no Google colours used as
branding. Every example is an illustration, not data.
Portrait rules kept here: all text sits above the 86% line (y > FLOOR), inside the side margins, and no
text is smaller than MIN_FS. Text is never scaled: the font size itself is reduced if a line is too wide,
so the size a scene reports is the size on screen. At 2160 px wide one unit is 480 px, and a 32 pt
EB Garamond line has an x-height of about 87 px, above the 72 px floor.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings measured
from each beat's narration audio (faster-whisper), so re-check them if that audio is regenerated.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the 16:9
# default; make the frame 4.5 x 8 units.
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

HERE = Path(__file__).resolve().parent
DUR = {"B02": 18.07, "B04": 19.80, "B05": 15.13, "B06": 21.76, "B07": 23.47, "B08": 16.17,
       "B09": 15.83, "B10": 17.45}
for _p in (HERE / "beat_sheet.json", HERE.parent / "beat_sheet.json"):
    if _p.is_file():
        DUR = {b["beat_id"]: b["actual_duration_s"] for b in json.loads(_p.read_text())["beats"]}
        break

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"      # my teammate / the kept result
CRIMSON = "#E4572E"   # me / the one accent per beat
MUTED = "#5C5448"     # secondary text
PALE = "#9C927F"      # thin structure lines
PAPER = "#EADFCB"     # card fill
BORDER = "#A89E8C"    # outline of cards/windows that enclose text

# Portrait safe band: nothing sits below FLOOR (the bottom 14% of the frame stays empty).
SAFE_X = 1.95
FLOOR = -2.85
MIN_FS = 32
PORTRAIT = True
HEAD_Y = 3.1


def T(text, size=40, color=INK, max_w=3.8, **kw):
    """Text that is never scaled: if a line is too wide the font size itself is reduced (not below
    MIN_FS), so the size a scene reports is the size on screen."""
    m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    while max_w and m.width > max_w and size > MIN_FS:
        size -= 2
        m = Text(text, font="EB Garamond", font_size=size, color=color, **kw)
    return m


def check_mark(x, y, s=.26, color=TEAL, w=9):
    return VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[x - s, y, 0], [x - s * .35, y - s * .75, 0], [x + s, y + s * .8, 0]])


def cross_mark(x, y, s=.28, color=INK, w=9):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], stroke_color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], stroke_color=color, stroke_width=w))


def win(w, h, title=None):
    """A plain window: rounded rectangle, a thin bar with three pale dots, an optional small title."""
    body = RoundedRectangle(width=w, height=h, corner_radius=.2, stroke_color=BORDER, stroke_width=5,
                            fill_color=PAPER, fill_opacity=1)
    bar = Line([-w / 2, h / 2 - .62, 0], [w / 2, h / 2 - .62, 0], stroke_color=PALE, stroke_width=4)
    dots = VGroup(*[Dot(radius=.06, color=PALE) for _ in range(3)]).arrange(RIGHT, buff=.12
                                                                          ).move_to([-w / 2 + .45, h / 2 - .31, 0])
    g = VGroup(body, bar, dots)
    if title:
        g.add(T(title, 32, MUTED).move_to([.35, h / 2 - .31, 0]))
    return g


def tile(ch, s=.85, color=INK, fs=56):
    box = RoundedRectangle(width=s, height=s, corner_radius=.12, stroke_color=BORDER, stroke_width=5,
                           fill_color=PAPER, fill_opacity=1)
    t = T(ch, fs, color).move_to(box)
    return VGroup(box, t)


def chip(text, color, fs=34, pad=.24, max_w=3.4):
    t = T(text, fs, color, max_w=max_w)
    box = RoundedRectangle(width=t.width + pad * 2, height=t.height + pad * 1.1, corner_radius=.16,
                           stroke_color=color, stroke_width=5, fill_color=CREAM, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


def packet(text, color, fs=32):
    t = T(text, fs, color)
    box = RoundedRectangle(width=t.width + .36, height=t.height + .34, corner_radius=.12, stroke_color=color,
                           stroke_width=4, fill_color=CREAM, fill_opacity=1)
    t.move_to(box)
    return VGroup(box, t)


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


# ------------------------------------------------------------------------------------------
@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        head = T("one shared document", 38, MUTED).move_to([0, HEAD_Y, 0])
        wl = win(3.8, 1.5, "me").move_to([0, 2.0, 0])
        wr = win(3.8, 1.5, "my teammate").move_to([0, .3, 0])
        yl, yr = 2.0 - .31, .3 - .31
        baseL = T("Plan:", 38).move_to([-1.2, yl, 0])
        baseR = T("Plan:", 38).move_to([-1.2, yr, 0])
        self.go(.2, FadeIn(head), FadeIn(wl), FadeIn(wr), FadeIn(baseL), FadeIn(baseR), rt=.7)

        # 2.1: two people type in the same line
        callL = T("call", 38, CRIMSON).next_to(baseL, RIGHT, buff=.2)
        sendR = T("send", 38, TEAL).next_to(baseR, RIGHT, buff=.2)
        self.go(2.08, AddTextLetterByLetter(callL, time_per_char=.12), AddTextLetterByLetter(sendR, time_per_char=.12),
                rt=None)

        # 4.8: the text overlaps for a moment, each window gets the other's words jammed against its own
        sendL = T("send", 38, TEAL).next_to(callL, RIGHT, buff=.02)
        callR = T("call", 38, CRIMSON).next_to(sendR, RIGHT, buff=.02)
        ov = T("text overlaps", 40, MUTED).move_to([0, -1.0, 0])
        self.go(4.8, FadeIn(sendL, shift=LEFT * .4), FadeIn(callR, shift=RIGHT * .4), FadeIn(ov), rt=.7)
        self.go(6.18, sendL.animate.next_to(callL, RIGHT, buff=.2), callR.animate.next_to(sendR, RIGHT, buff=.2),
                FadeOut(ov), rt=.6)

        # 8.1: press Ctrl+Z in my window
        key = chip("Ctrl+Z", INK, 42).move_to([0, -.95, 0])
        cap1 = T("press Ctrl+Z\nin my window", 42, line_spacing=.9).move_to([0, -2.2, 0])
        self.go(8.14, FadeIn(key, scale=1.3), FadeIn(cap1), rt=.4)
        # 10.0: will it undo my teammate's work too?
        cap2 = T("will it undo\nmy teammate's\nwork too?", 40, line_spacing=.9).move_to([0, -2.0, 0])
        self.go(10.0, Transform(cap1, cap2), FadeOut(key), rt=.5)
        # 12.0: tested in two windows
        cap3 = T("I tested it\nin two windows", 44, line_spacing=.9).move_to([0, -2.1, 0])
        self.go(12.04, Transform(cap1, cap3), rt=.5)
        # 14.0: it only undid mine
        self.go(14.15, FadeOut(callL, scale=.6), FadeOut(callR, scale=.6), rt=.6)
        cap4 = T("it only\nundid mine", 50, CRIMSON, line_spacing=.9).move_to([0, -2.1, 0])
        self.go(14.4, Transform(cap1, cap4), rt=.4)
        # 15.7: how does it keep track?
        cap5 = T("How does it\nkeep track?", 52, line_spacing=.9).move_to([0, -2.1, 0])
        self.go(15.75, Transform(cap1, cap5), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
P4 = [-1.4, -.47, .47, 1.4]    # four slots, left to right
ROW4 = -.45


@timed("B04")
class B04_TheProblem(Scene):
    def construct(self):
        head = T("why this is hard", 42).move_to([0, 3.1, 0])
        a, b, c = tile("a"), tile("b"), tile("c")
        for t, x in zip((a, b, c), P4[:3]):
            t.move_to([x, ROW4, 0])
        slots = [T(str(i + 1), 34, MUTED).move_to([P4[i], ROW4 - .75, 0]) for i in range(4)]
        ex = T("an illustrative example", 32, MUTED).move_to([0, 2.62, 0])
        self.go(.1, FadeIn(head), rt=.5)
        # 1.76: the document says a, b, c
        self.go(1.76, *[FadeIn(t, shift=DOWN * .15) for t in (a, b, c)], *[FadeIn(s) for s in slots[:3]], FadeIn(ex),
                rt=.8)

        # 4.2: at the same moment, two people act (one after the other on screen, both held)
        me = chip("me: add x\nat the start", CRIMSON, 36).move_to([0, 1.9, 0])
        xt = tile("x", color=CRIMSON).move_to([P4[0], .55, 0])
        tm = chip("teammate: delete\nthe third letter", TEAL, 36).move_to([0, 1.9, 0])
        del_arrow = Arrow([P4[2], 1.35, 0], [P4[2], ROW4 + .6, 0], buff=0, color=TEAL, stroke_width=9,
                          max_tip_length_to_length_ratio=.35)
        self.go(4.4, FadeIn(me, shift=DOWN * .1), rt=.4)
        self.go(5.5, FadeIn(xt, scale=.6), rt=.4)
        self.go(6.9, Transform(me, tm), rt=.5)
        self.go(8.1, Create(del_arrow), rt=.4)

        # 9.72: x pushes everything one place to the right; slot numbers stay put
        self.go(9.9, xt.animate.move_to([P4[0], ROW4, 0]), a.animate.move_to([P4[1], ROW4, 0]),
                b.animate.move_to([P4[2], ROW4, 0]), c.animate.move_to([P4[3], ROW4, 0]), FadeIn(slots[3]), rt=1.4)
        # 12.5: so the third letter is now b
        ring = SurroundingRectangle(b, color=TEAL, buff=.1, stroke_width=7, corner_radius=.15)
        third = T("slot 3 is\nnow b", 44, line_spacing=.9).move_to([0, -2.1, 0])
        self.go(12.6, Create(ring), FadeIn(third), rt=.6)
        # 14.56: applied exactly as it was sent; 18.1: the wrong letter gets deleted
        self.go(14.9, FadeOut(third), FadeOut(ring), rt=.3)
        x_b = cross_mark(P4[2], ROW4 + .9, .22, CRIMSON, 11)
        ring2 = SurroundingRectangle(b, color=CRIMSON, buff=.1, stroke_width=7, corner_radius=.15)
        wrong = T("wrong\nletter", 50, CRIMSON, line_spacing=.9).move_to([0, -2.1, 0])
        self.go(18.1, Create(x_b), Create(ring2), FadeIn(wrong, shift=UP * .1), rt=.7)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B05")
class B05_TwoCopies(Scene):
    def construct(self):
        # 1.66: it runs in two places: the browser on top, the server below, a gap for the packets
        bw = win(3.8, 2.0, "your browser").move_to([0, 2.4, 0])
        page = RoundedRectangle(width=.9, height=.8, corner_radius=.08, stroke_color=BORDER, stroke_width=4,
                                fill_color=CREAM, fill_opacity=1).move_to([0, 1.9, 0])
        rb = RoundedRectangle(width=3.4, height=.62, corner_radius=.1, stroke_color=BORDER, stroke_width=4,
                              fill_color=CREAM, fill_opacity=1).move_to([0, 1.9, 0])
        srv = win(3.8, 2.9, "the server").move_to([0, -1.35, 0])
        rs = [RoundedRectangle(width=3.4, height=.62, corner_radius=.1, stroke_color=BORDER, stroke_width=4,
                               fill_color=CREAM, fill_opacity=1).move_to([0, y, 0]) for y in (-.95, -1.65, -2.35)]
        self.go(1.66, FadeIn(bw), FadeIn(page), FadeIn(srv), *[FadeIn(r) for r in rs], rt=.8)

        # 7.58: not the whole document: a page would travel down, crossed out
        ghost = page.copy().set_stroke(color=MUTED).move_to([0, .8, 0])
        gx = cross_mark(0, .8, .42, CRIMSON, 11)
        self.go(8.0, FadeIn(ghost, scale=.8), rt=.3)
        self.go(8.9, Create(gx), rt=.4)
        self.go(9.8, FadeOut(ghost), FadeOut(gx), rt=.4)

        # 10.02: it sends only your changes to the server
        p1 = packet("insert x", CRIMSON, 34).move_to([-.6, 1.0, 0])
        self.go(10.2, FadeIn(p1, shift=DOWN * .2), rt=.3)
        self.go(10.7, p1.animate.move_to([-.6, .5, 0]), rt=1.1)
        self.go(11.9, FadeOut(p1, scale=.5), rt=.3)
        # 12.72: and receives everyone else's changes back
        p2 = packet("delete c", TEAL, 34).move_to([.6, .5, 0])
        self.go(12.4, FadeIn(p2, shift=UP * .2), rt=.3)
        self.go(12.8, p2.animate.move_to([.6, 1.0, 0]), rt=1.2)
        self.go(14.1, FadeOut(p2, scale=.5), rt=.3)

        # what each side keeps (small, inside each box: the page becomes two lines)
        lb = T("not yet sent", 32, MUTED).move_to(rb)
        ls = [T("changes received", 32, MUTED).move_to(rs[0]), T("revision log", 32, MUTED).move_to(rs[1]),
              T("current document", 32, MUTED).move_to(rs[2])]
        self.go(14.4, FadeOut(page), FadeIn(rb), FadeIn(lb), *[FadeIn(t) for t in ls], rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B06")
class B06_Transformation(Scene):
    def construct(self):
        a, b, c = tile("a"), tile("b"), tile("c")
        for t, x in zip((a, b, c), P4[:3]):
            t.move_to([x, -.75, 0])
        slots = [T(str(i + 1), 34, MUTED).move_to([P4[i], -1.5, 0]) for i in range(4)]
        self.go(.1, FadeIn(a), FadeIn(b), FadeIn(c), *[FadeIn(s) for s in slots[:3]], rt=.5)
        # 3.62: operational transformation (a title moment, then it makes room)
        title = T("operational\ntransformation", 52, line_spacing=.9).move_to([0, 1.2, 0])
        self.go(3.62, FadeIn(title, shift=DOWN * .1), rt=.5)
        self.go(5.7, FadeOut(title), rt=.4)

        # 5.72: each edit is an operation
        op1 = chip("insert x\nat the start", CRIMSON, 42).move_to([0, 2.9, 0])
        op2 = chip("delete the\nthird letter", TEAL, 42).move_to([0, .95, 0])
        self.go(7.7, FadeIn(op1, shift=DOWN * .1), rt=.4)
        self.go(9.7, FadeIn(op2, shift=DOWN * .1), rt=.4)
        arrow = Arrow([P4[2], .4, 0], [P4[2], -.28, 0], buff=0, color=TEAL, stroke_width=9,
                      max_tip_length_to_length_ratio=.4)
        self.go(10.3, Create(arrow), rt=.3)
        # 11.32: when two operations clash: the x goes in, the row shifts, the arrow still points at slot 3
        diamond = Square(side_length=.64, color=INK, stroke_width=6, fill_color=CREAM, fill_opacity=1
                         ).rotate(PI / 4).move_to([0, 1.95, 0])
        x = tile("x", color=CRIMSON).move_to([P4[0], .1, 0])
        self.go(11.5, FadeIn(x, scale=.6), rt=.4)
        self.go(12.1, x.animate.move_to([P4[0], -.75, 0]), a.animate.move_to([P4[1], -.75, 0]),
                b.animate.move_to([P4[2], -.75, 0]), c.animate.move_to([P4[3], -.75, 0]), FadeIn(slots[3]), rt=1.0)
        clash = T("clash", 48, CRIMSON).move_to([0, -2.3, 0])
        self.go(12.5, FadeIn(clash), rt=.3)
        # 13.34: one is transformed to fit the other
        op2b = chip("delete the\nfourth letter", TEAL, 42).move_to([0, .95, 0])
        self.go(13.4, FadeOut(clash), FadeIn(diamond), rt=.4)
        self.go(14.2, Transform(op2, op2b), rt=.7)
        # 15.76: shifted from the third letter to the fourth
        self.go(17.6, arrow.animate.shift(RIGHT * .93), rt=.9)
        ring = SurroundingRectangle(c, color=TEAL, buff=.1, stroke_width=7, corner_radius=.15)
        self.go(18.6, Create(ring), rt=.3)
        # 19.12: so the c is deleted, just as they meant
        done = T("just as they meant", 38).move_to([0, -2.35, 0])
        self.go(19.4, FadeOut(c, scale=.4), FadeOut(ring), FadeOut(arrow), rt=.6)
        self.go(20.9, FadeIn(done, shift=UP * .1), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B07")
class B07_Protocol(Scene):
    def construct(self):
        # 0.1 - 9.3: one idea at a time, in big words
        w1 = T("transforming\nisn't enough", 54, line_spacing=.9).move_to([0, .8, 0])
        self.go(.1, FadeIn(w1), rt=.4)
        w2 = T("same changes,\nsame order", 54, line_spacing=.9).move_to([0, .8, 0])
        self.go(2.1, Transform(w1, w2), rt=.5)
        w3 = T("the collaboration\nprotocol", 50, TEAL, line_spacing=.9).move_to([0, .8, 0])
        self.go(6.1, Transform(w1, w3), rt=.5)

        # 9.36: the diagram builds: me on top, server in the middle, teammate below
        me_l = chip("me", CRIMSON, 40).move_to([0, 3.0, 0])
        tm_l = chip("teammate", TEAL, 40).move_to([0, -2.5, 0])
        srv = win(3.4, 2.6, "server").move_to([0, 0, 0])
        lg = T("revision log", 32, MUTED).move_to([0, .35, 0])
        row1 = chip("1  insert x", CRIMSON, 30, .16).move_to([0, -.2, 0])
        row2 = chip("2  delete c", TEAL, 30, .16).move_to([0, -.9, 0])
        self.go(9.0, FadeOut(w1), FadeIn(srv), FadeIn(lg), FadeIn(me_l), FadeIn(tm_l), rt=.4)
        c1 = packet("insert x", CRIMSON, 32).move_to([0, 2.3, 0])
        c2 = packet("delete c", TEAL, 32).move_to([0, -1.78, 0])
        self.go(9.6, FadeIn(c1), rt=.3)
        self.go(9.9, c1.animate.move_to([0, 1.8, 0]), rt=.7)
        self.go(10.7, FadeOut(c1, scale=.5), FadeIn(row1, scale=.8), rt=.3)
        self.go(10.8, FadeIn(c2, shift=UP * .2), rt=.25)
        self.go(11.2, FadeOut(c2, scale=.5), FadeIn(row2, scale=.8), rt=.3)

        # 12.96: an acknowledgement goes back to the person who made the change
        ck1 = check_mark(-1.3, 2.0, .2, CRIMSON, 9)
        ak1 = T("acknowledged", 32, CRIMSON).move_to([.3, 2.0, 0])
        ck2 = check_mark(-1.3, -1.78, .2, TEAL, 9)
        ak2 = T("acknowledged", 32, TEAL).move_to([.3, -1.78, 0])
        self.go(13.5, FadeIn(ck1, shift=UP * .3), FadeIn(ak1), rt=.5)
        self.go(14.9, FadeIn(ck2, shift=DOWN * .3), FadeIn(ak2), rt=.5)
        # 16.5: it passes the change on to everyone else
        p1 = packet("insert x", CRIMSON, 32).move_to([0, -1.78, 0])
        p2 = packet("delete c", TEAL, 32).move_to([0, 2.0, 0])
        self.go(16.4, FadeOut(ck1), FadeOut(ak1), FadeOut(ck2), FadeOut(ak2), rt=.4)
        self.go(16.9, FadeIn(p1, shift=UP * .25), rt=.4)
        self.go(17.7, FadeOut(p1, scale=.5), Indicate(tm_l, color=CRIMSON, scale_factor=1.1), rt=.5)
        self.go(18.3, FadeIn(p2, shift=DOWN * .25), rt=.4)
        self.go(19.1, FadeOut(p2, scale=.5), Indicate(me_l, color=TEAL, scale_factor=1.1), rt=.5)
        # 18.74: and keeps every change in a revision log: the complete history of the document
        box = SurroundingRectangle(VGroup(row1, row2), color=CRIMSON, buff=.18, stroke_width=6, corner_radius=.2)
        hist = T("the complete history\nof the document", 44, line_spacing=.9).move_to([0, -2.0, 0])
        self.go(19.7, Create(box), lg.animate.set_color(INK), rt=.5)
        self.go(21.28, FadeOut(tm_l), FadeOut(me_l), FadeIn(hist), rt=.5)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B08")
class B08_CursorsDelay(Scene):
    def construct(self):
        # 0: in my test
        test = T("in my test", 42, MUTED).move_to([0, HEAD_Y, 0])
        w = win(3.8, 1.7).move_to([0, 1.85, 0])
        yl = 1.85 - .31 - .0
        base = T("Plan:", 40).move_to([-1.15, yl, 0])
        call = T("call", 40, CRIMSON).next_to(base, RIGHT, buff=.18)
        send = T("send", 40, TEAL).next_to(call, RIGHT, buff=.18)
        self.go(.1, FadeIn(test), FadeIn(w), FadeIn(base), FadeIn(call), FadeIn(send), rt=.6)
        # 0.96: Ctrl+Z
        key = chip("Ctrl+Z", INK, 42).move_to([0, .35, 0])
        self.go(1.0, FadeIn(key, scale=1.3), rt=.3)
        self.go(1.9, FadeOut(call, scale=.6), rt=.5)
        ghost = DashedVMobject(RoundedRectangle(width=1.0, height=.6, corner_radius=.08, stroke_color=CRIMSON,
                                                stroke_width=5), num_dashes=20).move_to(call)
        cap = T("only my own\ntyping", 50, CRIMSON, line_spacing=.9).move_to([0, -1.1, 0])
        self.go(2.2, FadeIn(ghost), FadeIn(cap), FadeOut(key), rt=.4)
        # 3.84: the document must keep track of who made each change (my guess)
        tag_m = chip("mine,\nundone", CRIMSON, 32, .12, max_w=1.4).move_to([-1.0, .35, 0])
        tag_t = chip("made by\nteammate", TEAL, 32, .1, max_w=1.55).move_to([1.0, .35, 0])
        guess = T("who made each\nchange? my guess", 40, MUTED, line_spacing=.9).move_to([0, -1.5, 0])
        self.go(4.3, FadeOut(cap), FadeIn(tag_t), FadeIn(tag_m), rt=.5)
        self.go(5.7, FadeIn(guess), rt=.4)
        # 7.34: I can also see where my teammate's cursor is
        self.go(7.3, FadeOut(tag_t), FadeOut(tag_m), FadeOut(guess), FadeOut(ghost), rt=.4)
        cx = send.get_right()[0] + .25
        cur = Line([cx, yl - .35, 0], [cx, yl + .35, 0], stroke_color=TEAL, stroke_width=9)
        cur_tag = chip("teammate", TEAL, 32, .14).move_to([.8, .35, 0])
        see = T("I can see my\nteammate's cursor", 44, line_spacing=.9).move_to([0, -1.2, 0])
        self.go(7.7, FadeIn(cur), FadeIn(cur_tag), FadeIn(see), rt=.4)
        # 10.32: sometimes their text shows up a moment late: the server round trip
        self.go(9.9, FadeOut(see), FadeOut(cur_tag), rt=.3)
        tm = chip("teammate", TEAL, 34).move_to([.6, .55, 0])
        sv = RoundedRectangle(width=1.9, height=1.0, corner_radius=.2, stroke_color=BORDER, stroke_width=5,
                              fill_color=PAPER, fill_opacity=1).move_to([.6, -.85, 0])
        sv_l = T("server", 34).move_to([.6, -.85, 0])
        l1 = Line([.6, .2, 0], [.6, -.35, 0], stroke_color=PALE, stroke_width=5)
        l2 = Line([-.05, -.85, 0], [-1.4, -.85, 0], stroke_color=PALE, stroke_width=5)
        l3 = Line([-1.4, -.85, 0], [-1.4, 1.0, 0], stroke_color=PALE, stroke_width=5)
        self.go(10.1, FadeIn(tm), FadeIn(sv), FadeIn(sv_l), FadeIn(l1), FadeIn(l2), FadeIn(l3), rt=.4)
        late = T("a moment late", 50, line_spacing=.9).move_to([0, -2.1, 0])
        self.go(10.5, FadeIn(late), rt=.4)
        dot = Dot([.6, .2, 0], radius=.16, color=TEAL)
        self.go(12.7, FadeIn(dot), rt=.2)
        self.go(13.0, dot.animate.move_to([.6, -.35, 0]), rt=.5)
        dot2 = Dot([-.05, -.85, 0], radius=.16, color=TEAL)
        self.go(13.6, FadeOut(dot), FadeIn(dot2), rt=.2)
        self.go(13.9, dot2.animate.move_to([-1.4, -.85, 0]), rt=.7)
        self.go(14.7, dot2.animate.move_to([-1.4, 1.0, 0]), rt=.5)
        ok = T("ok", 40, TEAL).move_to(call.get_center())
        self.go(15.3, FadeOut(dot2), FadeIn(ok, scale=.6), rt=.4)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B09")
class B09_Crdts(Scene):
    def construct(self):
        small = T("I'm just starting\nto learn", 36, MUTED, line_spacing=.9).move_to([0, 2.85, 0])
        wl = win(3.8, 1.4, "copy 1").move_to([0, .95, 0])
        wr = win(3.8, 1.4, "copy 2").move_to([0, -.8, 0])
        yl, yr = .95 - .26, -.8 - .26
        baseL = T("Plan:", 40).move_to([-1.15, yl, 0])
        baseR = T("Plan:", 40).move_to([-1.15, yr, 0])
        self.go(.2, FadeIn(wl), FadeIn(wr), FadeIn(baseL), FadeIn(baseR), FadeIn(small), rt=.7)
        # 2.92: called CRDT
        crdt = T("CRDT", 60, INK, weight="BOLD").move_to([0, 3.1, 0])
        self.go(3.1, FadeOut(small), FadeIn(crdt, shift=DOWN * .1), rt=.4)
        long = T("conflict-free\nreplicated data type", 34, MUTED, line_spacing=.9).move_to([0, 2.25, 0])
        self.go(5.16, FadeIn(long), rt=.5)
        # 8.0: each copy can be changed on its own, at the same time
        callL = T("call", 40, CRIMSON).next_to(baseL, RIGHT, buff=.2)
        sendR = T("send", 40, TEAL).next_to(baseR, RIGHT, buff=.2)
        self.go(8.9, AddTextLetterByLetter(callL, time_per_char=.12), AddTextLetterByLetter(sendR, time_per_char=.12),
                rt=None)
        same_t = T("on its own,\nat the same time", 44, line_spacing=.9).move_to([0, -2.2, 0])
        self.go(9.7, FadeIn(same_t, shift=UP * .1), rt=.4)
        # 11.68: without coordinating with the others
        gap = DashedLine([-1.9, .075, 0], [1.9, .075, 0], color=MUTED, stroke_width=6, dash_length=.18)
        crx = cross_mark(0, .075, .16, CRIMSON, 8)
        nocap = T("without coordinating\nwith the others", 40, line_spacing=.9).move_to([0, -2.2, 0])
        self.go(11.7, Transform(same_t, nocap), Create(gap), rt=.5)
        self.go(12.3, Create(crx), rt=.4)
        # 13.68: the copies still end up the same
        sendL = T("send", 40, TEAL).next_to(callL, RIGHT, buff=.2)
        callR = T("call", 40, CRIMSON).next_to(sendR, RIGHT, buff=.2)
        same = T("the copies still\nend up the same", 42, TEAL, line_spacing=.9).move_to([0, -2.2, 0])
        eq = T("=", 60, TEAL, weight="BOLD").move_to([0, .075, 0])
        self.go(13.7, FadeOut(crx), FadeOut(gap), Transform(same_t, same),
                FadeIn(sendL, shift=LEFT * .3), FadeIn(callR, shift=RIGHT * .3), rt=.8)
        self.go(14.6, FadeIn(eq, scale=.5), rt=.4)
        self.go(14.9, FadeOut(long), FadeIn(T("simplified", 34, MUTED).move_to([0, 2.25, 0])), rt=.3)
        self.finish()


# ------------------------------------------------------------------------------------------
@timed("B10")
class B10_Messy(Scene):
    def construct(self):
        # stage 1: a slow connection
        exp = T("in my experience", 42, MUTED).move_to([0, HEAD_Y, 0])
        wl = win(3.8, 1.5).move_to([0, 1.7, 0])
        base = T("Plan: call", 40, CRIMSON).move_to([-.9, 1.7 - .31, 0])
        sv = win(2.2, 1.3).move_to([0, -.8, 0])
        sv.set_stroke(color="#A89E8C")   # lighter outline: keeps the small server box from fusing with its label
        sv_l = T("server", 34).move_to([0, -.95, 0])
        c_out = CubicBezier([-1.0, .95, 0], [-2.2, .3, 0], [-2.2, -.7, 0], [-1.15, -.8, 0])
        c_back = CubicBezier([1.15, -.8, 0], [2.2, -.7, 0], [2.2, .3, 0], [1.0, .95, 0])
        path = DashedVMobject(CubicBezier([-1.0, .95, 0], [-2.2, .3, 0], [-2.2, -.7, 0], [-1.15, -.8, 0]
                                          ).set_stroke(MUTED, 6), num_dashes=16)
        path2 = DashedVMobject(CubicBezier([1.15, -.8, 0], [2.2, -.7, 0], [2.2, .3, 0], [1.0, .95, 0]
                                           ).set_stroke(MUTED, 6), num_dashes=16)
        slow = T("a slow\nconnection", 50, line_spacing=.9).move_to([0, -2.1, 0])
        stage1 = VGroup(wl, base, sv, sv_l, path, path2)
        self.go(.1, FadeIn(exp), FadeIn(stage1), FadeIn(slow), rt=.7)
        # 4.14: text can appear late
        dot = Dot([-1.0, .95, 0], radius=.16, color=TEAL)
        self.go(3.9, FadeIn(dot), rt=.3)
        self.go(4.2, MoveAlongPath(dot, c_out), rt=1.2)
        self.go(5.5, dot.animate.move_to([1.15, -.8, 0]), rt=.6)
        self.go(6.1, MoveAlongPath(dot, c_back), rt=.9)
        # 5.74: overlap for a moment before it settles
        late = T("send", 40, TEAL).next_to(base, RIGHT, buff=.02)
        self.go(7.0, FadeOut(dot), FadeIn(late), rt=.3)
        self.go(7.4, late.animate.next_to(base, RIGHT, buff=.22), rt=.4)
        # 8.0: one idea at a time: stage 1 leaves, stage 2 arrives
        self.go(7.6, FadeOut(exp), FadeOut(stage1), FadeOut(late), FadeOut(slow), rt=.3)
        fr = T("framing, not a\nmeasurement", 32, MUTED, line_spacing=.9).move_to([0, 2.9, 0])
        wr = win(3.8, 3.9).move_to([0, .3, 0])
        a = T("Send draft today", 38, CRIMSON).move_to([0, 1.2, 0])
        b = T("Share plan Monday", 38, TEAL).move_to([0, .6, 0])
        self.go(7.95, FadeIn(wr), FadeIn(fr), rt=.2)
        self.go(8.2, FadeIn(a, shift=RIGHT * .3), rt=.3)
        self.go(9.2, FadeIn(b, shift=LEFT * .3), rt=.3)
        # 12.1: the system can merge both edits; 14.2: it can't decide which wording was wanted
        keep = T("both kept", 48, TEAL).move_to([0, 0, 0])
        self.go(12.6, FadeIn(keep), rt=.4)
        q = T("which wording did\nthe team want?", 40, CRIMSON, line_spacing=.9).move_to([0, -.95, 0])
        self.go(14.6, FadeIn(q, shift=UP * .1), rt=.5)
        self.finish()
