"""Native 9:16 layouts for "How Your Phone Types Japanese" (Keya G.).

Same scene name, colours, words and go() cues as ../scenes.py, rearranged for a tall frame
(4.5 x 8 Manim units at 2160x3840). Nothing here is a crop of the landscape film.

Scenes, one per Manim beat in beat_sheet.json (all written):
B02_Hook            a year of learning, はな to 花 / 鼻, then "hashi" typed and three candidates
B04_AboutJapanese   120 million+ speakers, then an unbroken line of Japanese with no spaces
B05_ThreeScripts    one sentence in three scripts; two kanji share one sound
B06_Typing          H-A-S-H-I to はし; a kana-only keyboard stops; the IME chooses the kanji
B07_Homophones      はし, はな, あめ, しろ, each with its kanji
B08_HowImeChooses   splits, kanji paths and two illustrative score bars; the best path wins
B09_NoSpaces        ここではきものをぬぐ split two ways; You versus the IME
B10_OldVsNew        dictionary and rules, counted text, Transformer networks
B11_WhereItFails    a name and a new word miss the dictionary; wrong cut, wrong kanji

Simple drawn shapes only: no photos, no person icons, no company or tool logos.
Japanese text is set in Hiragino Sans on purpose: the default font has no kana or kanji glyphs.
Scene length comes from actual_duration_s in beat_sheet.json. The go() times are word timings
measured from the beat's narration audio (faster-whisper), so re-check them if that audio is
regenerated.
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
DUR = {"B02": 13.27, "B04": 8.38, "B05": 17.43, "B06": 16.92, "B07": 13.01, "B08": 17.05, "B09": 16.49, "B10": 26.28, "B11": 8.73}
for _p in (HERE / "beat_sheet.json", HERE.parent / "beat_sheet.json"):
    if _p.is_file():
        DUR = {b["beat_id"]: b["actual_duration_s"] for b in json.loads(_p.read_text())["beats"]}
        break

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"     # kept / the favoured reading
CRIMSON = "#E4572E"  # the one accent: where は moves
SLATE = "#29335C"
GOLD = "#F3A712"     # fill only

# Portrait safe band; the bottom 14% of the frame stays empty, so nothing sits below FLOOR
# (text stays above 86% of the height).
SAFE_X, SAFE_Y = 1.85, 3.3
FLOOR = -2.85
JP = "Hiragino Sans"
PORTRAIT = True


# Gate T type floor: no text run under 1.9% of the frame height. On the portrait master that
# is 72 px at 3840, so portrait type is never set below these sizes.
MIN_T, MIN_J = 36, 46


def T(text, size=40, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=max(size, MIN_T), color=color, **kw)


def J(text, size=48, color=INK, **kw):
    return Text(text, font=JP, font_size=max(size, MIN_J), color=color, weight="BOLD", **kw)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    return mob


def shoe(s=1.0, color=INK):
    body = Polygon([-.8, -.3, 0], [.85, -.3, 0], [.95, -.1, 0], [.7, .05, 0], [.15, .1, 0],
                   [-.05, .45, 0], [-.7, .45, 0], [-.8, .3, 0],
                   stroke_color=color, stroke_width=5, fill_opacity=0).round_corners(.1)
    sole = Line([-.8, -.3, 0], [.9, -.3, 0], stroke_color=color, stroke_width=9)
    laces = VGroup(*[Line([.12 - i * .17, .09 + i * .1, 0], [.26 - i * .17, -.06 + i * .1, 0],
                          stroke_color=color, stroke_width=4) for i in range(2)])
    return VGroup(body, sole, laces).scale(s)


def kimono(s=1.0, color=INK):
    body = Polygon([-.5, .75, 0], [.5, .75, 0], [.58, -.78, 0], [-.58, -.78, 0],
                   stroke_color=color, stroke_width=5, fill_opacity=0)
    sl = Polygon([-.5, .75, 0], [-1.3, .6, 0], [-1.3, -.55, 0], [-.54, -.45, 0],
                 stroke_color=color, stroke_width=5, fill_opacity=0)
    sr = sl.copy().flip(UP, about_point=ORIGIN)   # mirror across the vertical axis
    collar = VMobject(stroke_color=color, stroke_width=5).set_points_as_corners(
        [[-.28, .75, 0], [.08, .15, 0], [.28, .75, 0]])
    obi = Rectangle(width=1.16, height=.3, stroke_color=color, stroke_width=5, fill_color=GOLD,
                    fill_opacity=1).move_to([0, -.15, 0])
    return VGroup(body, sl, sr, collar, obi).scale(s)


def door(s=1.0, color=INK):
    frame = Rectangle(width=1.3, height=2.2, stroke_color=color, stroke_width=5, fill_opacity=0)
    panel = Rectangle(width=.8, height=1.5, stroke_color=color, stroke_width=3, fill_opacity=0).shift(UP * .15)
    knob = Dot([.45, -.2, 0], radius=.07, color=color)
    mat = Line([-.9, -1.15, 0], [.9, -1.15, 0], stroke_color=color, stroke_width=6)
    return VGroup(frame, panel, knob, mat).scale(s)


def word_row(groups, size, hot):
    """groups: list of word strings; hot: (word_index, char_index) of the は to colour."""
    items = []
    for wi, word in enumerate(groups):
        if wi == hot[0]:
            pieces = [word[:hot[1]], word[hot[1]], word[hot[1] + 1:]]
            sub = VGroup(*[J(p, size, CRIMSON if k == 1 else INK) for k, p in enumerate(pieces) if p])
            sub.arrange(RIGHT, buff=.02)
            items.append(sub)
        else:
            items.append(J(word, size))
    row = VGroup()
    for i, it in enumerate(items):
        if i:
            row.add(T("/", size * .8, "#8C8478"))
        row.add(it)
    row.arrange(RIGHT, buff=.14)
    return row


class Timed:
    def setup(self):
        self.camera.background_color = CREAM

    @property
    def now(self):
        return self.renderer.time

    def go(self, t, *anims, rt=0.5):
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
        else:
            print(f"QC {self.BEAT}: scene ends {-gap:.2f}s after its audio")


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


@timed("B09")
class B09_NoSpaces(Scene):
    def construct(self):
        W = SAFE_X * 2 - .1
        # 1. the sentence, large, kana with romaji beneath
        kana = fit(J("ここではきものをぬぐ", 80), W).move_to([0, .6, 0])
        romaji = fit(Text("kokodehakimonowonugu", font="Menlo", font_size=40, color=INK), W).next_to(kana, DOWN, buff=.35)
        self.go(.15, Write(kana, run_time=1.4), FadeIn(romaji, shift=UP * .1, run_time=1.0), rt=None)

        # 2. split two ways, one above the other
        top_kana = fit(J("ここではきものをぬぐ", 30, "#6B6458"), W).move_to([0, 3.0, 0])
        self.go(2.3, Transform(kana, top_kana), FadeOut(romaji), rt=.6)

        yA, yB = 2.2, -.3        # chips line of each block; kanji .62 below, icon + gloss 1.45 below
        a_split = fit(word_row(["ここで", "はきもの", "を", "ぬぐ"], 38, (1, 0)), W).move_to([0, yA, 0])
        a_kanji = fit(J("ここで履物を脱ぐ", 44), W).move_to([0, yA - .68, 0])
        a_arrow = Arrow(a_split.get_bottom() + DOWN * .02, a_kanji.get_top() + UP * .02, buff=.04,
                        color=INK, stroke_width=4, max_tip_length_to_length_ratio=.45)
        a_shoe = shoe(.5).move_to([-1.5, yA - 1.5, 0])
        a_gloss = VGroup(T("Take off your", 30), T("footwear here", 30)).arrange(DOWN, buff=.04, aligned_edge=LEFT)
        a_gloss.next_to(a_shoe, RIGHT, buff=.3)
        self.go(3.0, FadeIn(a_split, shift=UP * .1), rt=.6)
        self.go(4.1, GrowArrow(a_arrow), FadeIn(a_kanji), rt=.4)
        self.go(4.6, Create(a_shoe), FadeIn(a_gloss), rt=.7)

        b_split = fit(word_row(["ここでは", "きもの", "を", "ぬぐ"], 38, (0, 3)), W).move_to([0, yB, 0])
        b_kanji = fit(J("ここでは着物を脱ぐ", 44), W).move_to([0, yB - .68, 0])
        b_arrow = Arrow(b_split.get_bottom() + DOWN * .02, b_kanji.get_top() + UP * .02, buff=.04,
                        color=INK, stroke_width=4, max_tip_length_to_length_ratio=.45)
        b_kim = kimono(.42).move_to([-1.5, yB - 1.5, 0])
        b_gloss = VGroup(T("Take off your", 30), T("kimono here", 30)).arrange(DOWN, buff=.04, aligned_edge=LEFT)
        b_gloss.next_to(b_kim, RIGHT, buff=.3)
        self.go(5.5, FadeIn(b_split, shift=UP * .1), rt=.4)
        self.go(6.0, GrowArrow(b_arrow), FadeIn(b_kanji), rt=.3)
        self.go(6.35, Create(b_kim), FadeIn(b_gloss), rt=.5)

        # 3. you vs the IME, stacked for the tall frame
        stage2 = Group(kana, a_split, a_kanji, a_arrow, a_shoe, a_gloss, b_split, b_kanji, b_arrow, b_kim, b_gloss)
        self.go(7.45, FadeOut(stage2), rt=.3)

        you_t = T("You: where you are", 38).move_to([0, 3.05, 0])
        d = door(.55).move_to([-1.2, 1.95, 0])
        arrow = Arrow([-.6, 1.95, 0], [.1, 1.95, 0], buff=0, color=TEAL, stroke_width=6, max_tip_length_to_length_ratio=.3)
        sh = shoe(.55).move_to([1.05, 1.95, 0])
        you_lab = VGroup(T("front door", 36).move_to([-.95, 1.15, 0]), T("footwear", 36).move_to([1.05, 1.15, 0]))
        divider = Line([-SAFE_X, .85, 0], [SAFE_X, .85, 0], stroke_color="#BDB3A2", stroke_width=3)
        ime_t = VGroup(T("IME: which split is", 40), T("more common in text", 40)).arrange(DOWN, buff=.05).move_to([0, .3, 0])
        fit(ime_t, SAFE_X * 2 - .1)
        ya, yb = -.75, -1.8
        mini_shoe = shoe(.3).move_to([-1.65, ya, 0])
        mini_kim = kimono(.24).move_to([-1.65, yb, 0])
        trk_a = Rectangle(width=1.4, height=.3, stroke_color="#BDB3A2", stroke_width=2, fill_opacity=0).move_to([1.1, ya, 0])
        trk_b = Rectangle(width=1.4, height=.3, stroke_color="#BDB3A2", stroke_width=2, fill_opacity=0).move_to([1.1, yb, 0])
        bar_a = Rectangle(width=1.4, height=.3, stroke_color=INK, stroke_width=3, fill_color=TEAL, fill_opacity=1)
        bar_b = Rectangle(width=.7, height=.3, stroke_color=INK, stroke_width=3, fill_color=GOLD, fill_opacity=1)
        bar_a.align_to(trk_a, LEFT).align_to(trk_a, DOWN)
        bar_b.align_to(trk_b, LEFT).align_to(trk_b, DOWN)
        lab_a = VGroup(J("ここで", 46), J("はきもの", 46)).arrange(DOWN, buff=0).move_to([-.45, ya, 0])
        lab_b = VGroup(J("ここでは", 46), J("きもの", 46)).arrange(DOWN, buff=0).move_to([-.45, yb, 0])
        illus = T("illustrative only", 36, "#6B6458").move_to([0, -2.6, 0])
        self.go(7.8, FadeIn(you_t), FadeIn(ime_t), FadeIn(divider), FadeIn(mini_shoe), FadeIn(mini_kim),
                FadeIn(trk_a), FadeIn(trk_b), FadeIn(lab_a), FadeIn(lab_b), rt=.3)
        self.go(9.2, Create(d), rt=.7)
        self.go(10.4, GrowArrow(arrow), Create(sh), FadeIn(you_lab), rt=.8)
        self.go(12.1, Indicate(ime_t, color=TEAL, scale_factor=1.0), rt=.8)
        self.go(14.2, GrowFromEdge(bar_a, LEFT), GrowFromEdge(bar_b, LEFT), rt=1.1)
        self.go(15.3, FadeIn(illus), rt=.5)
        self.finish()


# =====================================================================================
# B02, B04 to B08, B10, B11. One source for both aspect ratios: L(landscape, portrait)
# picks the native value for the file it is in (PORTRAIT is set at the top of the file).
# Every scene is laid out to use the whole safe area: content reaches the top and bottom
# of the frame and spans most of its width at every point of the beat.
# =====================================================================================

WIDTH = SAFE_X * 2 - .1
GREY = "#6B6458"
FAINT = "#BDB3A2"


def L(land, port):
    return port if PORTRAIT else land


def card(content, w, h, stroke=SLATE, width=3, fill=CREAM):
    r = RoundedRectangle(corner_radius=.14, width=w, height=h, stroke_color=stroke,
                         stroke_width=width, fill_color=fill, fill_opacity=1)
    content.move_to(r.get_center())
    return VGroup(r, content)


def slot(w, h):
    """An empty placeholder card: the place a result will land."""
    return RoundedRectangle(corner_radius=.14, width=w, height=h, stroke_color=FAINT, stroke_width=2,
                            fill_opacity=0)


def keycap(label, size, w):
    r = RoundedRectangle(corner_radius=.1, width=w, height=w, stroke_color=SLATE, stroke_width=4,
                         fill_color=CREAM, fill_opacity=1)
    t = Text(label, font="Menlo", font_size=size, color=INK).move_to(r.get_center())
    return VGroup(r, t)


def keyboard(kw, gap, size, y_top):
    """A plain three-row keyboard (no brand). Returns the group and {letter: keycap}."""
    keys, g = {}, VGroup()
    for ri, row in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
        caps = []
        for ch in row:
            k = keycap(ch, size, kw)
            keys[ch] = k
            caps.append(k)
        rg = VGroup(*caps).arrange(RIGHT, buff=gap)
        rg.move_to([0, y_top - ri * (kw + gap), 0])
        g.add(rg)
    return g, keys


def book(s=1.0, color=INK):
    cover = Rectangle(width=1.1, height=1.4, stroke_color=color, stroke_width=5, fill_opacity=0)
    spine = Line([-.38, .7, 0], [-.38, -.7, 0], stroke_color=color, stroke_width=4)
    lines = VGroup(*[Line([-.2, .35 - i * .3, 0], [.4, .35 - i * .3, 0], stroke_color=color, stroke_width=3)
                     for i in range(3)])
    return VGroup(cover, spine, lines).scale(s)


def machine(s=1.0, color=INK):
    screen = Rectangle(width=1.5, height=1.0, stroke_color=color, stroke_width=5, fill_opacity=0).shift(UP * .5)
    lines = VGroup(*[Line([-.55, .72 - i * .25, 0], [.55 - i * .2, .72 - i * .25, 0], stroke_color=color, stroke_width=3)
                     for i in range(3)])
    base = Rectangle(width=2.0, height=.45, stroke_color=color, stroke_width=5, fill_opacity=0).shift(DOWN * .4)
    keys = VGroup(*[Line([-.8 + i * .4, -.4, 0], [-.6 + i * .4, -.4, 0], stroke_color=color, stroke_width=4)
                    for i in range(4)])
    return VGroup(screen, lines, base, keys).scale(s)


def pill(text, size, color=INK, fill=CREAM, stroke=SLATE, pad=.28, jp=False):
    t = (J if jp else T)(text, size, color)
    r = RoundedRectangle(corner_radius=.2, width=t.width + pad * 2, height=t.height + pad,
                         stroke_color=stroke, stroke_width=3, fill_color=fill, fill_opacity=1)
    t.move_to(r.get_center())
    return VGroup(r, t)


def label(text, size, color=INK, w=None):
    w = w or WIDTH
    t = T(text, size, color)
    if t.width <= w or " " not in text:
        return fit(t, w)
    words = text.split(" ")
    best = None
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        m = max(len(a), len(b))
        if best is None or m < best[0]:
            best = (m, a, b)
    g = VGroup(T(best[1], size, color), T(best[2], size, color)).arrange(DOWN, buff=.06)
    return fit(g, w)


# -------------------------------------------------------------------------------------


@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        # 0 to 3 s: a year of learning, twelve steps that climb the frame
        n = 12
        steps = VGroup(*[Rectangle(width=.27, height=.4 + i * .38, stroke_color=INK, stroke_width=3,
                                   fill_color=TEAL, fill_opacity=.9) for i in range(n)])
        steps.arrange(RIGHT, buff=.04, aligned_edge=DOWN).move_to([0, 0, 0])
        steps.align_to([0, -1.75, 0], DOWN)
        yr = label("over a year of learning", 40, INK, WIDTH).move_to([0, -2.25, 0])
        self.go(.3, LaggedStart(*[GrowFromEdge(s_, DOWN) for s_ in steps], lag_ratio=.12, run_time=1.4), rt=None)
        self.go(1.8, FadeIn(yr), rt=.5)
        self.go(2.6, FadeOut(steps), FadeOut(yr), rt=.3)

        # 3 to 6 s: はな splits into flower and nose
        hana = J("はな", 130).move_to([0, 2.3, 0])
        hr = Text("hana", font="Menlo", font_size=40, color=GREY).next_to(hana, DOWN, buff=.1)
        self.go(3.0, Write(hana), FadeIn(hr), rt=.7)
        k1 = J("花", 130).move_to([-.95, -.05, 0])
        k2 = J("鼻", 130).move_to([.95, -.05, 0])
        g1 = T("flower", 48).next_to(k1, DOWN, buff=.2)
        g2 = T("nose", 48).next_to(k2, DOWN, buff=.2)
        l1 = Line(hr.get_bottom() + DOWN * .1, k1.get_top() + UP * .1, stroke_color=INK, stroke_width=4)
        l2 = Line(hr.get_bottom() + DOWN * .1, k2.get_top() + UP * .1, stroke_color=INK, stroke_width=4)
        self.go(4.6, Create(l1), Create(l2), FadeIn(k1), FadeIn(k2), FadeIn(g1), FadeIn(g2), rt=.6)
        self.go(5.7, FadeOut(Group(hana, hr, k1, k2, g1, g2, l1, l2)), rt=.3)

        # 6 to 9 s: the keyboard has the same problem (a plain keyboard, drawn in full)
        bar = RoundedRectangle(corner_radius=.2, width=3.7, height=.7, stroke_color=SLATE,
                               stroke_width=5, fill_color=CREAM, fill_opacity=1).move_to([0, 3.0, 0])
        kb, keys = keyboard(.34, .05, 16, -1.3)
        kb_cap = T("my keyboard", 40, GREY).move_to([0, -2.58, 0])
        self.go(6.1, Create(bar), FadeIn(kb), FadeIn(kb_cap), rt=.3)
        letters = [Text(c, font="Menlo", font_size=40, color=INK) for c in "hashi"]
        VGroup(*letters).arrange(RIGHT, buff=.2).move_to(bar.get_center())
        self.go(8.9, LaggedStart(*[FadeIn(x) for x in letters], lag_ratio=.25),
                *[keys[c][0].animate.set_fill(GOLD, opacity=1) for c in "hasi"], rt=.7)
        hashi = J("はし", 100).move_to([-.6, 2.15, 0])
        self.go(9.6, FadeIn(hashi, shift=DOWN * .2), rt=.4)

        # 10 to 12 s: three candidates, stacked so every word stays readable
        cards = []
        for y, k, g in zip([1.1, .25, -.6], "橋箸端", ["bridge", "chopsticks", "edge"]):
            c = card(VGroup(J(k, 60), T(g, 40)).arrange(RIGHT, buff=.3), 3.2, .78)
            c.move_to([0, y, 0])
            cards.append(c)
        self.go(10.1, FadeIn(cards[0], shift=DOWN * .15), rt=.5)
        self.go(10.9, FadeIn(cards[1], shift=DOWN * .15), rt=.5)
        self.go(11.5, FadeIn(cards[2], shift=DOWN * .15), rt=.5)
        q = T("?", 100, CRIMSON).move_to([1.0, 2.15, 0])
        self.go(12.4, FadeIn(q, scale=1.4), rt=.5)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B04")
class B04_AboutJapanese(Scene):
    def construct(self):
        title = T("Japanese", 84).move_to([0, 2.7, 0])
        self.go(.2, Write(title), rt=.8)
        # a counter that climbs to 120 on the spoken "one hundred and twenty"
        num = DecimalNumber(0, num_decimal_places=0, font_size=230, color=INK)
        num.move_to([0, .75, 0])
        num.add_updater(lambda m: m.move_to([0, .75, 0]))
        plus = T("million +", 80, INK).move_to([0, -.85, 0])
        self.add(num, plus)
        self.go(1.4, num.animate.set_value(120), rt=1.7)
        sub = label("speakers, mostly in Japan", 48, INK, WIDTH).move_to([0, -2.1, 0])
        self.go(3.2, FadeIn(sub, shift=UP * .1), rt=.4)
        self.go(5.3, FadeOut(Group(title, num, plus, sub)), rt=.3)

        # no spaces: English words have gaps, Japanese runs together
        lens = [1.5, 2.4, 1.1, 2.9, 1.8]
        scl, gap = .32, .16
        eng_t = T("English", 40, GREY).move_to([-1.0, 3.1, 0])
        eng = VGroup(*[Rectangle(width=w * scl, height=.3, stroke_color=INK, stroke_width=2, fill_color=TEAL, fill_opacity=.9) for w in lens])
        eng.arrange(RIGHT, buff=gap).move_to([0, 2.6, 0])
        line1 = J("日本語を話す人は多い", 54)
        fit(line1, WIDTH)
        line1.move_to([0, 1.3, 0])
        jp_t = T("Japanese", 40, GREY).move_to([-.95, -.05, 0])
        jp_bar = Rectangle(width=sum(lens) * scl + (len(lens) - 1) * gap, height=.3, stroke_color=INK,
                           stroke_width=2, fill_color=SLATE, fill_opacity=.9).move_to([0, -.55, 0])
        self.go(5.6, FadeIn(eng_t), FadeIn(eng), FadeIn(jp_t), FadeIn(jp_bar), rt=.3)
        gaps = VGroup()
        for i in (3, 4, 6, 7, 8):
            x = line1.get_left()[0] + line1.width * i / 10
            gaps.add(Line([x, line1.get_bottom()[1] - .08, 0], [x, line1.get_bottom()[1] - .45, 0],
                          stroke_color=CRIMSON, stroke_width=6))
        cap = label("no spaces between words", 48, CRIMSON, WIDTH).move_to([0, -1.9, 0])
        self.go(6.0, Write(line1), FadeIn(cap), rt=1.0)
        self.go(7.2, LaggedStart(*[Create(g_) for g_ in gaps], lag_ratio=.15), rt=.8)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B05")
class B05_ThreeScripts(Scene):
    def construct(self):
        # one mixed sentence: 私 (kanji) は (hiragana) ケヤ (katakana) です (hiragana)
        parts = [J("私", 110), J("は", 110), J("ケヤ", 110), J("です", 110)]
        sent = VGroup(*parts).arrange(RIGHT, buff=.08).move_to([0, 1.85, 0])
        fit(sent, WIDTH)
        self.go(.3, LaggedStart(*[FadeIn(p) for p in parts], lag_ratio=.2, run_time=1.6), rt=None)
        three = label("three ways of writing, in one sentence", 38, GREY, WIDTH).move_to([0, 3.0, 0])
        self.go(2.2, FadeIn(three), rt=.5)

        def row(color, jp_text, en_text, y):
            dot = Dot(radius=.12, color=color)
            a = VGroup(dot, J(jp_text, 56, color)).arrange(RIGHT, buff=.2)
            b = T(en_text, 40, INK)
            g = VGroup(a, b).arrange(DOWN, buff=.05)
            return g.move_to([0, y, 0])
        r1 = row(TEAL, "ひらがな", "the grammar", .55)
        r2 = row(CRIMSON, "カタカナ", "foreign words", -.75)
        r3 = row(SLATE, "漢字", "meaning", -2.05)
        for r_ in (r1, r2, r3):
            r_.set_opacity(.4)
        self.go(4.6, FadeIn(r1), FadeIn(r2), FadeIn(r3), rt=.2)
        self.go(4.8, parts[1].animate.set_color(TEAL), parts[3].animate.set_color(TEAL), r1.animate.set_opacity(1), rt=.4)
        self.go(7.0, parts[2].animate.set_color(CRIMSON), r2.animate.set_opacity(1), rt=.4)
        self.go(9.9, Indicate(parts[2], color=CRIMSON, scale_factor=1.15), rt=.8)
        self.go(11.1, parts[0].animate.set_color(SLATE), r3.animate.set_opacity(1), rt=.4)

        # two kanji, one sound
        two = label("two kanji, one sound", 40, GREY, WIDTH).move_to([0, 2.85, 0])
        self.go(12.3, FadeOut(Group(sent, three, r1, r2, r3)), FadeIn(two), rt=.5)
        k1 = J("花", 130).move_to([-.95, 1.25, 0])
        k2 = J("鼻", 130).move_to([.95, 1.25, 0])
        g1 = T("flower", 48).next_to(k1, DOWN, buff=.15)
        g2 = T("nose", 48).next_to(k2, DOWN, buff=.15)
        q = T("?", 130, CRIMSON).move_to([0, -1.0, 0])
        self.go(12.9, FadeIn(k1), FadeIn(k2), FadeIn(q), rt=.5)
        self.go(15.0, FadeIn(g1), rt=.4)
        self.go(15.6, FadeIn(g2), rt=.4)
        snd = J("はな", 110, TEAL).move_to([0, -1.1, 0])
        sr = Text("hana", font="Menlo", font_size=40, color=GREY).next_to(snd, DOWN, buff=.12)
        a1 = Arrow(g1.get_bottom() + DOWN * .15, snd.get_top() + LEFT * .25 + UP * .1, buff=.05, color=INK, stroke_width=4, max_tip_length_to_length_ratio=.25)
        a2 = Arrow(g2.get_bottom() + DOWN * .15, snd.get_top() + RIGHT * .25 + UP * .1, buff=.05, color=INK, stroke_width=4, max_tip_length_to_length_ratio=.25)
        self.go(16.3, FadeOut(q), GrowArrow(a1), GrowArrow(a2), rt=.35)
        self.go(16.7, Write(snd), FadeIn(sr), rt=.5)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B06")
class B06_Typing(Scene):
    def construct(self):
        keys = VGroup(*[keycap(c, 28, .56) for c in "HASHI"]).arrange(RIGHT, buff=.1)
        board = RoundedRectangle(corner_radius=.2, width=keys.width + .4, height=.86, stroke_color=SLATE,
                                 stroke_width=5, fill_color=CREAM, fill_opacity=1)
        kb = VGroup(board, keys).move_to([0, 2.85, 0])
        keys.move_to(board.get_center())
        self.go(.7, Create(board), FadeIn(keys), rt=.6)
        for t, i in [(2.5, 0), (2.6, 1), (2.9, 2), (3.1, 3), (3.3, 4)]:
            self.go(t, keys[i][0].animate.set_fill(GOLD, opacity=1), rt=.1)
        hashi = J("はし", 140).move_to([0, 1.35, 0])
        arr = Arrow(kb.get_bottom() + DOWN * .05, hashi.get_top() + UP * .15, buff=.05, color=INK, stroke_width=5)
        self.go(3.6, GrowArrow(arr), rt=.4)
        self.go(4.0, Write(hashi), rt=.6)
        hira = T("hiragana", 44, GREY).next_to(hashi, DOWN, buff=.08)
        self.go(4.7, FadeIn(hira), rt=.4)

        # a kana-only keyboard stops here
        stop = Line([-1.6, -.2, 0], [1.6, -.2, 0], stroke_color=CRIMSON, stroke_width=10)
        stop_t = label("a kana keyboard stops here", 44, CRIMSON, WIDTH).move_to([0, -.95, 0])
        self.go(6.1, FadeIn(stop_t), rt=.5)
        self.go(8.1, Create(stop), rt=.4)

        # three different words
        qs = VGroup(*[card(T("?", 56, CRIMSON), 1.0, 1.0) for _ in range(3)]).arrange(RIGHT, buff=.3)
        self.go(8.6, FadeOut(Group(stop, stop_t)), rt=.3)
        qs.move_to([0, -.8, 0])
        self.go(9.0, LaggedStart(*[FadeIn(q_, shift=UP * .1) for q_ in qs], lag_ratio=.3, run_time=1.0), rt=None)
        tw = label("three different words", 44, INK, WIDTH).move_to([0, -1.75, 0])
        self.go(10.0, FadeIn(tw), rt=.4)

        # the IME has one more job: choosing the kanji
        self.go(10.9, FadeOut(Group(qs, tw, hira)), rt=.4)
        ime = card(T("IME", 60, TEAL), 2.0, 1.0, stroke=TEAL, width=5).move_to([0, -.3, 0])
        cands = VGroup(*[card(J(k, 56), .95, .85) for k in "橋箸端"]).arrange(RIGHT, buff=.3).move_to([0, -2.35, 0])
        job = label("one more job: choosing the kanji", 44, INK, WIDTH).move_to([0, -1.3, 0])
        self.go(13.3, FadeIn(ime, scale=.9), FadeIn(job), rt=.5)
        self.go(15.4, LaggedStart(*[FadeIn(c_, shift=UP * .1) for c_ in cands], lag_ratio=.25, run_time=.9), rt=None)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B07")
class B07_Homophones(Scene):
    def construct(self):
        # one sound at a time, large; the thesis stays on screen along the bottom
        data = [
            (2.3, "はし", "hashi", [("橋", "bridge", 2.8), ("箸", "chopsticks", 3.4), ("端", "edge", 4.2)], 5.0),
            (5.3, "はな", "hana", [("花", "flower", 5.6), ("鼻", "nose", 6.2)], 7.0),
            (7.2, "あめ", "ame", [("雨", "rain", 7.6), ("飴", "candy", 8.2)], 9.1),
            (9.3, "しろ", "shiro", [("白", "white", 9.7), ("城", "castle", 10.2)], 11.1),
        ]
        prev = None
        for t, kana, rom, items, t_out in data:
            head = VGroup(J(kana, 120), Text(rom, font="Menlo", font_size=44, color=GREY)).arrange(DOWN, buff=.08).move_to([0, 2.35, 0])
            cards = []
            for k, (kj, gl, tt) in enumerate(items):
                c = card(VGroup(J(kj, 80), T(gl, 44)).arrange(RIGHT, buff=.35), 3.6, 1.25).move_to([0, .45 - k * 1.3, 0])
                cards.append((c, tt))
            if prev is not None:
                self.go(t - .2, FadeOut(prev), rt=.2)
            self.go(t, FadeIn(head, shift=RIGHT * .1), rt=.25)
            for c, tt in cards:
                self.go(tt, FadeIn(c, shift=UP * .1), rt=.2)
            prev = Group(head, *[c for c, _ in cards])
        self.go(11.5, FadeOut(prev), rt=.2)
        # all four sounds, as the voice sums up
        sums = VGroup(*[J(k, 80) for k in ("はし", "はな", "あめ", "しろ")]).arrange(DOWN, buff=.12).move_to([0, .85, 0])
        thesis = label("same sound, different kanji", 38, TEAL, WIDTH).move_to([0, -2.3, 0])
        self.go(11.7, LaggedStart(*[FadeIn(x) for x in sums], lag_ratio=.05), FadeIn(thesis), rt=.6)
        self.go(12.3, *[Indicate(x, color=TEAL) for x in sums], rt=.4)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B08")
class B08_HowImeChooses(Scene):
    def construct(self):
        kana = VGroup(VGroup(J("はし", 88), J("を", 88)).arrange(RIGHT, buff=.05), J("わたる", 88)).arrange(DOWN, buff=.05).move_to([0, 1.6, 0])
        self.go(.4, Write(kana), rt=1.0)
        # every way to split: the pieces are tinted apart (はし | を | わたる)
        cap1 = label("every way to split", 48, CRIMSON, WIDTH).move_to([0, -.6, 0])
        self.go(3.2, kana[0][1].animate.set_color(CRIMSON), kana[1].animate.set_color(TEAL), FadeIn(cap1), rt=.5)
        # every kanji for each piece: three paths, each with two empty score tracks and a legend
        paths = [("橋を渡る", .95, .92), ("箸を渡る", .62, .14), ("端を渡る", .5, .05)]
        ys = [2.3, .9, -.5]
        tw = 3.4
        rows = []
        for (txt, a, b), y in zip(paths, ys):
            p = J(txt, 70).move_to([0, y, 0])
            tracks = VGroup(Rectangle(width=tw, height=.16, stroke_color=FAINT, stroke_width=2, fill_opacity=0),
                            Rectangle(width=tw, height=.16, stroke_color=FAINT, stroke_width=2, fill_opacity=0)).arrange(DOWN, buff=.07)
            tracks.move_to([0, y - .82, 0])
            ba = Rectangle(width=max(.05, tw * a), height=.16, stroke_color=INK, stroke_width=2, fill_color=TEAL, fill_opacity=1)
            bb = Rectangle(width=max(.05, tw * b), height=.16, stroke_color=INK, stroke_width=2, fill_color=GOLD, fill_opacity=1)
            ba.align_to(tracks[0], LEFT).align_to(tracks[0], UP)
            bb.align_to(tracks[1], LEFT).align_to(tracks[1], UP)
            rows.append((p, tracks, ba, bb))
        leg_a = VGroup(Square(.22, stroke_opacity=0, fill_color=TEAL, fill_opacity=1), T("common word", 36, INK)).arrange(RIGHT, buff=.15)
        leg_b = VGroup(Square(.22, stroke_opacity=0, fill_color=GOLD, fill_opacity=1), T("used together", 36, INK)).arrange(RIGHT, buff=.15)
        note = T("illustrative only", 36, GREY)
        legend = VGroup(leg_a, leg_b, note).arrange(DOWN, buff=.04, aligned_edge=LEFT).move_to([0, -2.15, 0])
        self.go(5.1, FadeOut(Group(kana, cap1)), rt=.3)
        for i, (p, tracks, ba, bb) in enumerate(rows):
            self.go(5.4 + i * .5, FadeIn(p, shift=RIGHT * .1), FadeIn(tracks), rt=.4)
        self.go(7.0, FadeIn(legend), rt=.4)
        self.go(9.0, LaggedStart(*[GrowFromEdge(r[2], LEFT) for r in rows], lag_ratio=.2, run_time=1.4), rt=None)
        self.go(10.7, LaggedStart(*[GrowFromEdge(r[3], LEFT) for r in rows], lag_ratio=.2, run_time=1.4), rt=None)
        # the highest-scoring path wins; the others fade (never below 40%)
        win = SurroundingRectangle(rows[0][0], color=TEAL, buff=.1, stroke_width=6)
        self.go(15.4, Create(win), rows[1][0].animate.set_opacity(.4), rows[2][0].animate.set_opacity(.4),
                rows[1][2].animate.set_opacity(.4), rows[2][2].animate.set_opacity(.4),
                rows[1][3].animate.set_opacity(.4), rows[2][3].animate.set_opacity(.4), rt=.7)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B10")
class B10_OldVsNew(Scene):
    def construct(self):
        # a three-stop timeline across the top; the active stop is named once, beneath it
        xs = [-1.2, 0, 1.2]
        ty = 3.15
        line = Line([xs[0], ty, 0], [xs[2], ty, 0], stroke_color=FAINT, stroke_width=5)
        dots = VGroup(*[Dot([x, ty, 0], radius=.16, color=FAINT) for x in xs])
        self.add(line, dots)

        def light(i):
            return [dots[j].animate.set_color(TEAL if j == i else FAINT) for j in range(3)]

        def title(text):
            return label(text, 38, TEAL).move_to([0, 2.6, 0])
        t1, t2, t3 = title("dictionary and rules"), title("counted text"), title("neural networks")

        # stop 1: the first Japanese word processor
        mc = machine(.85).move_to([0, 1.45, 0])
        cap = label("the first Japanese word processor", 40, INK, WIDTH).move_to([0, .3, 0])
        self.go(1.3, *light(0), FadeIn(t1), FadeIn(mc), rt=.6)
        self.go(3.7, FadeIn(cap), rt=.5)
        bk = book(.7).move_to([-.85, -1.0, 0])
        bk_t = T("dictionary", 36, INK).next_to(bk, DOWN, buff=.12)
        ru = card(VGroup(T("grammar", 40, INK), T("rules", 40, INK)).arrange(DOWN, buff=.02), 1.7, 1.1)
        ru.move_to([.95, -1.0, 0])
        self.go(6.2, FadeIn(bk), FadeIn(bk_t), rt=.5)
        self.go(8.2, FadeIn(ru), rt=.5)
        # homophones weighed by context and use
        self.go(9.4, FadeOut(Group(bk, bk_t, ru)), rt=.3)
        c1 = card(J("橋", 56), 1.1, 1.0).move_to([-.95, -1.4, 0])
        c2 = card(J("箸", 56), 1.1, 1.0).move_to([.95, -1.4, 0])
        hl = T("homophones", 40, GREY).move_to([0, -.6, 0])
        self.go(9.7, FadeIn(c1), FadeIn(c2), FadeIn(hl), rt=.5)
        w1 = label("sentence context", 38, TEAL, 1.75).next_to(c1, DOWN, buff=.15)
        w2 = label("how often used", 38, TEAL, 1.75).next_to(c2, DOWN, buff=.15)
        self.go(11.1, FadeIn(w1), rt=.4)
        self.go(12.6, FadeIn(w2), rt=.4)
        ck = VMobject(stroke_color=TEAL, stroke_width=10).set_points_as_corners([[-.3, 0, 0], [-.05, -.28, 0], [.38, .3, 0]]).scale(.7).move_to(c1.get_corner(UL) + np.array([-.15, .1, 0]))
        self.go(13.7, FadeIn(ck), rt=.3)

        # stop 2: later keyboards counted words
        self.go(14.5, FadeOut(Group(mc, cap, c1, c2, hl, w1, w2, ck, t1)), *light(1), FadeIn(t2), rt=.4)
        pages = VGroup(*[Rectangle(width=.75, height=1.05, stroke_color=INK, stroke_width=4, fill_color=CREAM, fill_opacity=1).shift(RIGHT * .18 * i + DOWN * .13 * i) for i in range(4)])
        pages.move_to([-1.2, 1.0, 0])
        hs = [1.0, 2.3, 1.7, 3.1]
        words = VGroup(*[Rectangle(width=.36, height=h * .6, stroke_color=INK, stroke_width=3, fill_color=TEAL, fill_opacity=1) for h in hs])
        words.arrange(RIGHT, buff=.12, aligned_edge=DOWN).move_to([.95, .5, 0])
        tally = T("counted words", 44, INK).move_to([0, -1.1, 0])
        big = label("in huge amounts of text", 44, GREY).move_to([0, -2.1, 0])
        self.go(14.9, FadeIn(pages, shift=RIGHT * .1), rt=.3)
        self.go(15.2, LaggedStart(*[GrowFromEdge(w_, DOWN) for w_ in words], lag_ratio=.25, run_time=1.1), FadeIn(tally), rt=None)
        self.go(16.4, FadeIn(big), rt=.5)

        # stop 3: neural networks called Transformers
        self.go(18.0, FadeOut(Group(pages, words, tally, big, t2)), *light(2), FadeIn(t3), rt=.4)
        cols = [2, 4, 4, 2]
        layers = [VGroup(*[Dot(radius=.1, color=SLATE) for _ in range(n_)]).arrange(DOWN, buff=.3) for n_ in cols]
        net = VGroup(*layers).arrange(RIGHT, buff=.75).move_to([0, 1.5, 0])
        edges = VGroup()
        for a_, b_ in zip(layers[:-1], layers[1:]):
            for u in a_:
                for v in b_:
                    edges.add(Line(u.get_center(), v.get_center(), stroke_color=FAINT, stroke_width=1.5))
        self.go(18.5, Create(edges), FadeIn(net), rt=.9)
        tf = pill("Transformers", 46, TEAL, stroke=TEAL).move_to([0, -.05, 0])
        self.go(19.8, FadeIn(tf, shift=UP * .1), rt=.5)
        same = label("the same design family as ChatGPT", 38, GREY, WIDTH).move_to([0, -.85, 0])
        self.go(21.2, FadeIn(same), rt=.5)
        # convert as you type
        typed = [Text(c, font="Menlo", font_size=34, color=INK) for c in "hashi"]
        trow = VGroup(*typed).arrange(RIGHT, buff=.15)
        out = J("橋", 46, TEAL)
        arrow = Text("→", font=JP, font_size=34, color=INK)
        pair = VGroup(trow, arrow, out).arrange(RIGHT, buff=.25)
        field = RoundedRectangle(corner_radius=.2, width=3.7, height=.95, stroke_color=SLATE, stroke_width=4,
                                 fill_color=CREAM, fill_opacity=1).move_to([0, -1.75, 0])
        pair.move_to(field.get_center())
        cap2 = T("convert as you type", 36, INK).move_to([0, -2.5, 0])
        self.go(21.9, FadeIn(field), rt=.4)
        self.go(23.9, FadeIn(arrow), rt=.2)
        self.go(24.1, LaggedStart(*[FadeIn(x) for x in typed], lag_ratio=.3, run_time=1.2), rt=None)
        self.go(25.4, FadeIn(out, scale=1.2), FadeIn(cap2), rt=.5)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B11")
class B11_WhereItFails(Scene):
    def construct(self):
        ime = card(T("IME", 60, TEAL), 2.0, 1.0, stroke=TEAL, width=5).move_to([0, .15, 0])
        nm = J("けや", 130).move_to([0, 2.5, 0])
        nw = pill("a brand-new word", 36, INK, pad=.2).move_to([0, 1.35, 0])
        self.go(.4, FadeIn(ime), rt=.5)
        self.go(1.9, FadeIn(nm, shift=DOWN * .2), rt=.4)
        self.go(2.4, FadeIn(nw, shift=DOWN * .2), rt=.4)
        # a dictionary lookup comes back empty
        bk = book(.8).move_to([0, -.95, 0])
        bkt = T("dictionary", 40, INK).next_to(bk, DOWN, buff=.1)
        mg = VGroup(Circle(radius=.36, stroke_color=INK, stroke_width=5), Line([.26, -.26, 0], [.66, -.66, 0], stroke_color=INK, stroke_width=6))
        mg.scale(.8).move_to(bk.get_center() + UP * .15 + RIGHT * .1)
        empty = T("no entry", 48, CRIMSON).next_to(bkt, DOWN, buff=.1)
        self.go(3.6, FadeIn(bk), FadeIn(bkt), rt=.4)
        self.go(4.0, Create(mg), rt=.3)
        self.go(4.4, FadeIn(empty), rt=.4)
        # then the kana is cut in the wrong place, and the wrong kanji is picked
        ny = 2.45
        self.go(5.0, FadeOut(Group(bk, bkt, mg, empty, nw, ime)), nm.animate.move_to([0, ny, 0]), rt=.5)
        cut = Line([0, nm.get_bottom()[1] - .35, 0], [0, nm.get_bottom()[1] - .05, 0], stroke_color=CRIMSON, stroke_width=7)
        wr = label("cut in the wrong place", 44, CRIMSON, WIDTH).move_to([0, .85, 0])
        self.go(5.5, Create(cut), FadeIn(wr), rt=.5)
        w1 = card(J("毛", 96), 1.55, 1.4).move_to([-.9, -.85, 0])
        w2 = card(J("矢", 96), 1.55, 1.4).move_to([.9, -.85, 0])
        self.go(6.9, FadeIn(w1), FadeIn(w2), rt=.5)
        wk = T("the wrong kanji", 44, CRIMSON).move_to([0, -1.95, 0])
        x1 = Cross(Square(.4), stroke_color=CRIMSON, stroke_width=7).next_to(w1, UP, buff=.12)
        x2 = Cross(Square(.4), stroke_color=CRIMSON, stroke_width=7).next_to(w2, UP, buff=.12)
        self.go(7.7, Create(x1), Create(x2), w1[0].animate.set_stroke(CRIMSON), w2[0].animate.set_stroke(CRIMSON), FadeIn(wk), rt=.5)
        self.finish()
