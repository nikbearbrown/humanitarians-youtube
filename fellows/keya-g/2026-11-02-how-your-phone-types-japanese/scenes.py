"""Manim scenes for "How Your Phone Types Japanese" (Keya G.).

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

HERE = Path(__file__).resolve().parent
DUR = {"B02": 13.27, "B04": 8.38, "B05": 17.43, "B06": 16.92, "B07": 13.01, "B08": 17.05, "B09": 16.49, "B10": 26.28, "B11": 8.73}
if (HERE / "beat_sheet.json").is_file():
    DUR = {b["beat_id"]: b["actual_duration_s"]
           for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"     # kept / the favoured reading
CRIMSON = "#E4572E"  # the one accent: where は moves
SLATE = "#29335C"
GOLD = "#F3A712"     # fill only

SAFE_X, SAFE_Y = 6.25, 3.4
FLOOR = -SAFE_Y
JP = "Hiragino Sans"
PORTRAIT = False


def T(text, size=40, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def J(text, size=48, color=INK, **kw):
    return Text(text, font=JP, font_size=size, color=color, weight="BOLD", **kw)


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
        # 1. the sentence, large, kana with romaji beneath
        kana = fit(J("ここではきものをぬぐ", 120), 11.5).move_to([0, .55, 0])
        romaji = fit(Text("kokodehakimonowonugu", font="Menlo", font_size=48, color=INK), 9.0).next_to(kana, DOWN, buff=.45)
        self.go(.15, Write(kana, run_time=1.4), FadeIn(romaji, shift=UP * .1, run_time=1.0), rt=None)

        # 2. split two ways, one above the other (cues from the narration)
        top_kana = fit(J("ここではきものをぬぐ", 38, "#6B6458"), 5.0).move_to([0, 3.0, 0])
        self.go(2.3, Transform(kana, top_kana), FadeOut(romaji), rt=.6)

        ROW_A, ROW_B = 1.35, -1.55
        LX = -3.2    # centre of the left column
        # row A: ここで / はきもの / を / ぬぐ  ->  ここで履物を脱ぐ  ->  footwear
        a_split = fit(word_row(["ここで", "はきもの", "を", "ぬぐ"], 46, (1, 0)), 5.9).move_to([LX, ROW_A + .6, 0])
        a_kanji = fit(J("ここで履物を脱ぐ", 50), 5.9).move_to([LX, ROW_A - .6, 0])
        a_arrow = Arrow(a_split.get_bottom() + DOWN * .02, a_kanji.get_top() + UP * .02, buff=.05,
                        color=INK, stroke_width=4, max_tip_length_to_length_ratio=.4)
        a_shoe = shoe(.9).move_to([3.6, ROW_A + .55, 0])
        a_gloss = fit(T("Take off your footwear here", 36), 4.9).move_to([3.6, ROW_A - .5, 0])
        self.go(3.0, FadeIn(a_split, shift=UP * .1), rt=.6)
        self.go(4.1, GrowArrow(a_arrow), FadeIn(a_kanji), rt=.4)
        self.go(4.6, Create(a_shoe), FadeIn(a_gloss), rt=.7)

        # row B: ここでは / きもの / を / ぬぐ  ->  ここでは着物を脱ぐ  ->  kimono
        b_split = fit(word_row(["ここでは", "きもの", "を", "ぬぐ"], 46, (0, 3)), 5.9).move_to([LX, ROW_B + .6, 0])
        b_kanji = fit(J("ここでは着物を脱ぐ", 50), 5.9).move_to([LX, ROW_B - .6, 0])
        b_arrow = Arrow(b_split.get_bottom() + DOWN * .02, b_kanji.get_top() + UP * .02, buff=.05,
                        color=INK, stroke_width=4, max_tip_length_to_length_ratio=.4)
        b_kim = kimono(.8).move_to([3.6, ROW_B + .5, 0])
        b_gloss = fit(T("Take off your kimono here", 36), 4.9).move_to([3.6, ROW_B - .65, 0])
        self.go(5.5, FadeIn(b_split, shift=UP * .1), rt=.4)
        self.go(6.0, GrowArrow(b_arrow), FadeIn(b_kanji), rt=.3)
        self.go(6.35, Create(b_kim), FadeIn(b_gloss), rt=.5)

        # 3. side by side: you vs the IME (cues: "A person uses the situation", "The IME only has statistics")
        stage2 = Group(kana, a_split, a_kanji, a_arrow, a_shoe, a_gloss, b_split, b_kanji, b_arrow, b_kim, b_gloss)
        self.go(7.45, FadeOut(stage2), rt=.3)

        divider = Line([0, -3.0, 0], [0, 2.9, 0], stroke_color="#BDB3A2", stroke_width=3)
        you_t = T("You: where you are", 40).move_to([-3.25, 2.5, 0])
        d = door(1.0).move_to([-5.0, -.2, 0])
        sh = shoe(1.0).move_to([-1.55, -.2, 0])
        arrow = Arrow([-3.9, -.2, 0], [-2.7, -.2, 0], buff=0, color=TEAL, stroke_width=7)
        you_lab = T("front door: footwear", 34).move_to([-3.25, -1.9, 0])
        ime_t = VGroup(T("IME: which split is", 40), T("more common in text", 40)).arrange(DOWN, buff=.12).move_to([3.25, 2.5, 0])
        ya, yb = .6, -.85
        mini_shoe = shoe(.42).move_to([.95, ya, 0])
        mini_kim = kimono(.36).move_to([.95, yb, 0])
        trk_a = Rectangle(width=4.4, height=.5, stroke_color="#BDB3A2", stroke_width=2, fill_opacity=0).move_to([1.65 + 2.2, ya, 0])
        trk_b = Rectangle(width=4.4, height=.5, stroke_color="#BDB3A2", stroke_width=2, fill_opacity=0).move_to([1.65 + 2.2, yb, 0])
        bar_a = Rectangle(width=4.2, height=.5, stroke_color=INK, stroke_width=3, fill_color=TEAL, fill_opacity=1)
        bar_b = Rectangle(width=2.0, height=.5, stroke_color=INK, stroke_width=3, fill_color=GOLD, fill_opacity=1)
        bar_a.move_to([1.65 + 2.1, ya, 0])
        bar_b.move_to([1.65 + 1.0, yb, 0])
        lab_a = J("ここで/はきもの", 28).move_to([1.65, ya + .5, 0], aligned_edge=LEFT)
        lab_b = J("ここでは/きもの", 28).move_to([1.65, yb + .5, 0], aligned_edge=LEFT)
        lab_a.align_to(bar_a, LEFT)
        lab_b.align_to(bar_b, LEFT)
        illus = T("illustrative bars, not real numbers", 30, "#6B6458").move_to([3.25, -1.9, 0])
        self.go(7.8, FadeIn(divider), FadeIn(you_t), FadeIn(ime_t), FadeIn(mini_shoe), FadeIn(mini_kim),
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
    t = T(text, size, color)
    return fit(t, w or WIDTH)


# -------------------------------------------------------------------------------------
@timed("B02")
class B02_Hook(Scene):
    def construct(self):
        # 0 to 3 s: a year of learning, drawn as twelve steps that climb the whole frame
        n = 12
        base = L(-2.7, -2.3)
        steps = VGroup(*[Rectangle(width=L(.9, .27), height=L(.5, .5) + i * L(.47, .43), stroke_color=INK, stroke_width=3,
                                   fill_color=TEAL, fill_opacity=.9) for i in range(n)])
        steps.arrange(RIGHT, buff=L(.08, .04), aligned_edge=DOWN).move_to([0, 0, 0])
        steps.align_to([0, base, 0], DOWN)
        yr = label("over a year of learning", L(48, 30), INK, WIDTH).move_to([0, L(-3.05, -2.65), 0])
        self.go(.3, LaggedStart(*[GrowFromEdge(s_, DOWN) for s_ in steps], lag_ratio=.12, run_time=1.4), rt=None)
        self.go(1.8, FadeIn(yr), rt=.5)
        self.go(2.6, FadeOut(steps), FadeOut(yr), rt=.3)

        # 3 to 6 s: はな splits into flower and nose
        hana = J("はな", L(220, 120)).move_to([0, L(2.0, 2.35), 0])
        hr = Text("hana", font="Menlo", font_size=L(44, 28), color=GREY).next_to(hana, DOWN, buff=.1)
        self.go(3.0, Write(hana), FadeIn(hr), rt=.7)
        kx = L(3.8, .95)
        ky = L(-.4, .35)
        k1 = J("花", L(230, 120)).move_to([-kx, ky, 0])
        k2 = J("鼻", L(230, 120)).move_to([kx, ky, 0])
        g1 = T("flower", L(64, 38)).next_to(k1, DOWN, buff=.2)
        g2 = T("nose", L(64, 38)).next_to(k2, DOWN, buff=.2)
        l1 = Line(hr.get_bottom() + DOWN * .1, k1.get_top() + UP * .1, stroke_color=INK, stroke_width=4)
        l2 = Line(hr.get_bottom() + DOWN * .1, k2.get_top() + UP * .1, stroke_color=INK, stroke_width=4)
        self.go(4.6, Create(l1), Create(l2), FadeIn(k1), FadeIn(k2), FadeIn(g1), FadeIn(g2), rt=.6)
        self.go(5.7, FadeOut(Group(hana, hr, k1, k2, g1, g2, l1, l2)), rt=.3)

        # 6 to 9 s: the keyboard has the same problem (a plain keyboard, drawn in full)
        bar = RoundedRectangle(corner_radius=.2, width=L(11.6, 3.7), height=L(.95, .65), stroke_color=SLATE,
                               stroke_width=5, fill_color=CREAM, fill_opacity=1).move_to([0, L(2.85, 3.0), 0])
        kb, keys = keyboard(L(.9, .34), L(.12, .05), L(40, 16), L(-.75, -.75))
        kb_cap = label("my keyboard", L(30, 24), GREY).move_to([L(-4.6, 0), L(2.85, -1.95), 0])
        self.go(6.1, Create(bar), FadeIn(kb), FadeIn(kb_cap), rt=.3)
        letters = [Text(c, font="Menlo", font_size=L(64, 34), color=INK) for c in "hashi"]
        row = VGroup(*letters).arrange(RIGHT, buff=.2).move_to(bar.get_center())
        self.go(8.9, LaggedStart(*[FadeIn(x) for x in letters], lag_ratio=.25),
                *[keys[c][0].animate.set_fill(GOLD, opacity=1) for c in "hasi"], rt=.7)
        hashi = J("はし", L(110, 80)).move_to([-L(4.7, 0), L(.95, 1.95), 0])
        self.go(9.6, FadeIn(hashi, shift=DOWN * .2), rt=.4)

        # 10 to 12 s: three candidates fan out
        cw, ch = L(2.7, 1.12), L(2.0, 1.5)
        xs = [-L(1.2, 1.2), L(1.55, 0), L(4.3, 1.2)]
        cy = L(.95, .65)
        cards = []
        for x, k, g in zip(xs, "橋箸端", ["bridge", "chopsticks", "edge"]):
            c = card(VGroup(J(k, L(100, 56)), fit(T(g, L(46, 22)), cw - .14)).arrange(DOWN, buff=.12), cw, ch)
            c.move_to([x, cy, 0])
            cards.append(c)
        self.go(10.1, FadeIn(cards[0], shift=DOWN * .15), rt=.5)
        self.go(10.9, FadeIn(cards[1], shift=DOWN * .15), rt=.5)
        self.go(11.5, FadeIn(cards[2], shift=DOWN * .15), rt=.5)
        q = T("?", L(110, 100), CRIMSON).move_to([-L(3.0, -1.5), L(.95, 1.95), 0])
        self.go(12.4, FadeIn(q, scale=1.4), rt=.5)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B04")
class B04_AboutJapanese(Scene):
    def construct(self):
        nihongo = J("日本語", L(230, 130))
        fit(nihongo, WIDTH)
        nihongo.move_to([0, L(1.7, 2.45), 0])
        self.go(.2, Write(nihongo), rt=.8)
        # a counter that climbs to 120 on the spoken "one hundred and twenty"
        num = DecimalNumber(0, num_decimal_places=0, font_size=L(250, 88), color=TEAL)
        plus = T("million +", L(130, 42), INK)
        probe = DecimalNumber(120, num_decimal_places=0, font_size=L(250, 88))
        total = probe.width + .3 + plus.width
        plus.move_to([total / 2 - plus.width / 2, L(-1.05, .6), 0])
        num.next_to(plus, LEFT, buff=.3, aligned_edge=DOWN)
        num.add_updater(lambda m: m.next_to(plus, LEFT, buff=.3, aligned_edge=DOWN))
        grp = VGroup(num, plus)
        self.add(grp)
        self.go(1.4, num.animate.set_value(120), rt=1.7)
        sub = label("speakers, mostly in Japan", L(64, 34), INK, WIDTH).move_to([0, L(-2.95, -1.9), 0])
        self.go(3.2, FadeIn(sub, shift=UP * .1), rt=.4)
        self.go(5.3, FadeOut(Group(nihongo, grp, sub)), rt=.3)

        # no spaces: English words have gaps, Japanese runs together
        lens = [1.5, 2.4, 1.1, 2.9, 1.8]
        scl = L(1.0, .32)
        gap = L(.45, .16)
        eng_t = label("English", L(40, 26), GREY).move_to([-L(5.2, 1.3), L(3.05, 3.2), 0])
        eng = VGroup(*[Rectangle(width=w * scl, height=L(.5, .3), stroke_color=INK, stroke_width=2, fill_color=TEAL, fill_opacity=.9) for w in lens])
        eng.arrange(RIGHT, buff=gap).move_to([0, L(2.3, 2.65), 0])
        line1 = J("日本語を話す人は多い", L(130, 54))
        fit(line1, WIDTH)
        line1.move_to([0, L(.85, 1.15), 0])
        jp_t = label("Japanese", L(40, 26), GREY).move_to([-L(5.1, 1.25), L(-.85, -.4), 0])
        jp_bar = Rectangle(width=sum(lens) * scl + (len(lens) - 1) * gap, height=L(.5, .3), stroke_color=INK,
                           stroke_width=2, fill_color=SLATE, fill_opacity=.9).move_to([0, L(-1.5, -.95), 0])
        self.go(5.6, FadeIn(eng_t), FadeIn(eng), FadeIn(jp_t), FadeIn(jp_bar), rt=.3)
        self.go(6.0, Write(line1), rt=1.0)
        gaps = VGroup()
        for i in (3, 4, 6, 7, 8):
            x = line1.get_left()[0] + line1.width * i / 10
            gaps.add(Line([x, line1.get_bottom()[1] - .08, 0], [x, line1.get_bottom()[1] - .45, 0],
                          stroke_color=CRIMSON, stroke_width=6))
        cap = label("no spaces between words", L(76, 40), CRIMSON, WIDTH).move_to([0, L(-2.6, -2.2), 0])
        self.go(7.2, LaggedStart(*[Create(g_) for g_ in gaps], lag_ratio=.15), FadeIn(cap), rt=.8)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B05")
class B05_ThreeScripts(Scene):
    def construct(self):
        # one mixed sentence: 私 (kanji) は (hiragana) ケヤ (katakana) です (hiragana)
        parts = [J("私", L(170, 110)), J("は", L(170, 110)), J("ケヤ", L(170, 110)), J("です", L(170, 110))]
        sent = VGroup(*parts).arrange(RIGHT, buff=.08).move_to([0, L(1.5, 2.0), 0])
        fit(sent, WIDTH)
        self.go(.3, LaggedStart(*[FadeIn(p) for p in parts], lag_ratio=.2, run_time=1.6), rt=None)
        three = label("three ways of writing, in one sentence", L(50, 28), GREY, WIDTH).move_to([0, L(3.05, 3.1), 0])
        self.go(2.2, FadeIn(three), rt=.5)

        def row(color, jp_text, en_text, y):
            dot = Dot(radius=.16, color=color)
            a = J(jp_text, L(64, 44), color)
            b = T(en_text, L(60, 40), INK)
            g = VGroup(dot, a, b).arrange(RIGHT, buff=.25)
            fit(g, WIDTH)
            g.move_to([0, y, 0])
            return g
        r1 = row(TEAL, "ひらがな", "the grammar", L(-.35, .5))
        r2 = row(CRIMSON, "カタカナ", "foreign words", L(-1.5, -.7))
        r3 = row(SLATE, "漢字", "meaning", L(-2.65, -1.9))
        for r_ in (r1, r2, r3):
            r_.set_opacity(.4)
        self.go(4.6, FadeIn(r1), FadeIn(r2), FadeIn(r3), rt=.2)
        self.go(4.8, parts[1].animate.set_color(TEAL), parts[3].animate.set_color(TEAL), r1.animate.set_opacity(1), rt=.4)
        self.go(7.0, parts[2].animate.set_color(CRIMSON), r2.animate.set_opacity(1), rt=.4)
        self.go(9.9, Indicate(parts[2], color=CRIMSON, scale_factor=1.15), rt=.8)
        self.go(11.1, parts[0].animate.set_color(SLATE), r3.animate.set_opacity(1), rt=.4)

        # two kanji, one sound
        two = label("two kanji, one sound", L(50, 28), GREY, WIDTH).move_to([0, L(3.05, 3.1), 0])
        self.go(12.3, FadeOut(Group(sent, three, r1, r2, r3)), FadeIn(two), rt=.5)
        k1 = J("花", L(250, 120)).move_to([-L(3.6, .95), L(.85, 1.6), 0])
        k2 = J("鼻", L(250, 120)).move_to([L(3.6, .95), L(.85, 1.6), 0])
        g1 = T("flower", L(70, 40)).next_to(k1, DOWN, buff=.15)
        g2 = T("nose", L(70, 40)).next_to(k2, DOWN, buff=.15)
        q = T("?", L(150, 90), CRIMSON).move_to([0, L(-2.4, -1.5), 0])
        self.go(12.9, FadeIn(k1), FadeIn(k2), FadeIn(q), rt=.5)
        self.go(15.0, FadeIn(g1), rt=.4)
        self.go(15.6, FadeIn(g2), rt=.4)
        snd = J("はな", L(130, 90), TEAL).move_to([0, L(-2.4, -1.5), 0])
        sr = Text("hana", font="Menlo", font_size=L(44, 30), color=GREY).next_to(snd, L(RIGHT, DOWN), buff=L(.3, .12))
        a1 = Arrow(g1.get_bottom() + DOWN * .15, snd.get_top() + LEFT * L(.5, .25) + UP * .1, buff=.05, color=INK, stroke_width=4, max_tip_length_to_length_ratio=.25)
        a2 = Arrow(g2.get_bottom() + DOWN * .15, snd.get_top() + RIGHT * L(.5, .25) + UP * .1, buff=.05, color=INK, stroke_width=4, max_tip_length_to_length_ratio=.25)
        self.go(16.3, FadeOut(q), GrowArrow(a1), GrowArrow(a2), rt=.35)
        self.go(16.7, Write(snd), FadeIn(sr), rt=.5)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B06")
class B06_Typing(Scene):
    def construct(self):
        kw = L(1.7, .56)
        keys = VGroup(*[keycap(c, L(64, 28), kw) for c in "HASHI"]).arrange(RIGHT, buff=L(.15, .1))
        board = RoundedRectangle(corner_radius=.2, width=keys.width + L(.7, .4), height=kw + L(.5, .3), stroke_color=INK,
                                 stroke_width=5, fill_color=CREAM, fill_opacity=1)
        kb = VGroup(board, keys).move_to([0, L(2.15, 2.85), 0])
        keys.move_to(board.get_center())
        self.go(.7, Create(board), FadeIn(keys), rt=.6)
        for t, i in [(2.5, 0), (2.6, 1), (2.9, 2), (3.1, 3), (3.3, 4)]:
            self.go(t, keys[i][0].animate.set_fill(GOLD, opacity=1), rt=.1)
        hashi = J("はし", L(150, 130)).move_to([0, L(0.0, .75), 0])
        arr = Arrow(kb.get_bottom() + DOWN * .05, hashi.get_top() + UP * .1, buff=.05, color=INK, stroke_width=5)
        self.go(3.6, GrowArrow(arr), rt=.4)
        self.go(4.0, Write(hashi), rt=.6)
        hira = label("hiragana", L(48, 28), GREY).next_to(hashi, DOWN, buff=.1)
        self.go(4.7, FadeIn(hira), rt=.4)

        # a kana-only keyboard stops here
        stop_y = L(-1.75, -.8)
        stop = Line([-L(2.4, 1.6), stop_y, 0], [L(2.4, 1.6), stop_y, 0], stroke_color=CRIMSON, stroke_width=10)
        stop_t = label("a kana keyboard stops here", L(56, 32), CRIMSON).move_to([0, L(-2.45, -1.3), 0])
        self.go(6.1, FadeIn(stop_t), rt=.5)
        self.go(8.1, Create(stop), rt=.4)

        # three different words
        qs = VGroup(*[card(T("?", L(90, 50), CRIMSON), L(2.2, 1.0), L(1.2, 1.0)) for _ in range(3)]).arrange(RIGHT, buff=L(.5, .3))
        self.go(8.6, FadeOut(Group(stop, stop_t)), rt=.3)
        qs.move_to([0, L(-2.35, -1.7), 0])
        self.go(9.0, LaggedStart(*[FadeIn(q_, shift=UP * .1) for q_ in qs], lag_ratio=.3, run_time=1.0), rt=None)
        tw = label("three different words", L(44, 32), INK).move_to([0, L(-3.1, -2.55), 0])
        self.go(10.0, FadeIn(tw), rt=.4)

        # the IME has one more job: choosing the kanji
        self.go(10.9, FadeOut(Group(qs, tw, hira)), rt=.4)
        ime = card(T("IME", L(90, 50), TEAL), L(3.4, 2.0), L(1.9, 1.0), stroke=TEAL, width=5)
        cands = VGroup(*[card(J(k, L(80, 46)), L(1.55, .85), L(1.55, .85)) for k in "橋箸端"]).arrange(RIGHT, buff=.3)
        if PORTRAIT:
            ime.move_to([0, -.7, 0])
            cands.move_to([0, -2.3, 0])
        else:
            ime.move_to([-3.6, -1.8, 0])
            cands.move_to([3.3, -1.8, 0])
        self.go(13.3, FadeIn(ime, scale=.9), rt=.5)
        job = label("one more job: choosing the kanji", L(46, 28), INK).move_to([0, L(-3.0, -1.55), 0])
        self.go(14.3, FadeIn(job), rt=.5)
        self.go(15.4, LaggedStart(*[FadeIn(c_, shift=UP * .1) for c_ in cands], lag_ratio=.25, run_time=.9), rt=None)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B07")
class B07_Homophones(Scene):
    def construct(self):
        data = [
            (2.3, "はし", "hashi", [("橋", "bridge", 2.8), ("箸", "chopsticks", 3.4), ("端", "edge", 4.2)]),
            (5.3, "はな", "hana", [("花", "flower", 5.6), ("鼻", "nose", 6.2)]),
            (7.2, "あめ", "ame", [("雨", "rain", 7.6), ("飴", "candy", 8.2)]),
            (9.3, "しろ", "shiro", [("白", "white", 9.7), ("城", "castle", 10.2)]),
        ]
        ys = [L(2.05, 2.45), L(.6, .95), L(-.85, -.5), L(-2.3, -1.95)]
        cw, ch = L(2.7, 1.1), L(1.35, .85)
        rows = []
        for (t, kana, rom, items), y in zip(data, ys):
            k = J(kana, L(84, 46))
            r = Text(rom, font="Menlo", font_size=L(40, 24), color=GREY)
            head = VGroup(k, r).arrange(RIGHT, buff=.3)
            fit(head, L(3.2, 3.6))
            cards, slots = [], []
            for kj, gl, tt in items:
                c = card(VGroup(J(kj, L(66, 40)), fit(T(gl, L(36, 22)), cw - .14)).arrange(DOWN, buff=.05), cw, ch)
                cards.append((c, tt))
            row_cards = VGroup(*[c for c, _ in cards]).arrange(RIGHT, buff=.2)
            if PORTRAIT:
                head.move_to([0, y + .5, 0])
                row_cards.move_to([0, y - .2, 0])
            else:
                head.move_to([-4.5, y, 0])
                row_cards.move_to([0, y, 0]).align_to([-2.6, y, 0], LEFT)
            for c, tt in cards:
                slots.append(slot(cw, ch).move_to(c.get_center()))
            rows.append((t, head, cards, slots))
        title = label("same sound, different kanji", L(44, 22), TEAL).move_to([0, 3.0, 0])
        # the table's frame is on screen from the start: four sounds, empty slots to fill
        self.go(.3, *[FadeIn(h_) for _, h_, _, _ in rows], *[FadeIn(s_) for _, _, _, ss in rows for s_ in ss], rt=.6)
        for t, head, cards, slots in rows:
            for c, tt in cards:
                self.go(tt, FadeIn(c, shift=UP * .1), rt=.4)
        if not PORTRAIT:
            self.go(11.3, FadeIn(title), rt=.5)
        self.go(12.3, *[Indicate(h_, color=TEAL) for _, h_, _, _ in rows], rt=.7)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B08")
class B08_HowImeChooses(Scene):
    def construct(self):
        kana = J("はしをわたる", L(130, 62)).move_to([0, L(2.55, 2.8), 0])
        fit(kana, WIDTH)
        self.go(.4, Write(kana), rt=1.0)
        # every way to split: tick marks
        def tick(ch):
            x = ch.get_left()[0] - .02
            return Line([x, kana.get_bottom()[1] - .42, 0], [x, kana.get_bottom()[1] - .08, 0], stroke_color=CRIMSON, stroke_width=6)
        cut1, cut2 = tick(kana[2]), tick(kana[3])
        cap1 = label("every way to split", L(44, 26), CRIMSON).next_to(kana, DOWN, buff=.5)
        self.go(3.2, Create(cut1), Create(cut2), FadeIn(cap1), rt=.5)
        # every kanji for each piece, as three paths with empty score tracks
        paths = [("橋を渡る", TEAL, .95, .92), ("箸を渡る", INK, .62, .14), ("端を渡る", INK, .5, .05)]
        ys = [L(.75, 1.5), L(-.6, .15), L(-1.95, -1.2)]
        tw = L(6.6, 3.2)
        rows = []
        for (txt, col, a, b), y in zip(paths, ys):
            p = J(txt, L(76, 40))
            if PORTRAIT:
                p.move_to([0, y + .32, 0])
            else:
                p.move_to([-4.1, y, 0])
            tracks = VGroup(Rectangle(width=tw, height=L(.4, .18), stroke_color=FAINT, stroke_width=2, fill_opacity=0),
                            Rectangle(width=tw, height=L(.4, .18), stroke_color=FAINT, stroke_width=2, fill_opacity=0)).arrange(DOWN, buff=.1, aligned_edge=LEFT)
            ba = Rectangle(width=max(.05, tw * a), height=L(.4, .18), stroke_color=INK, stroke_width=2, fill_color=TEAL, fill_opacity=1)
            bb = Rectangle(width=max(.05, tw * b), height=L(.4, .18), stroke_color=INK, stroke_width=2, fill_color=GOLD, fill_opacity=1)
            if PORTRAIT:
                tracks.move_to([0, y - .5, 0]).align_to([-tw / 2, 0, 0], LEFT)
            else:
                tracks.move_to([0, y, 0]).align_to([-1.0, 0, 0], LEFT)
            ba.align_to(tracks[0], LEFT).align_to(tracks[0], UP)
            bb.align_to(tracks[1], LEFT).align_to(tracks[1], UP)
            rows.append((p, tracks, ba, bb))
        self.go(5.1, FadeOut(cap1), rt=.3)
        for i, (p, tracks, ba, bb) in enumerate(rows):
            self.go(5.4 + i * .5, FadeIn(p, shift=RIGHT * .1), FadeIn(tracks), rt=.4)
        leg_a = VGroup(Square(.22, stroke_opacity=0, fill_color=TEAL, fill_opacity=1), label("how common the word is", L(26, 20), INK, L(3.3, 2.6))).arrange(RIGHT, buff=.15)
        leg_b = VGroup(Square(.22, stroke_opacity=0, fill_color=GOLD, fill_opacity=1), label("how often they appear together", L(26, 20), INK, L(4.2, 3.2))).arrange(RIGHT, buff=.15)
        note = label("illustrative bars, not real numbers", L(24, 20), GREY, L(3.3, 3.2))
        if PORTRAIT:
            legend = VGroup(leg_a, leg_b, note).arrange(DOWN, buff=.08, aligned_edge=LEFT).move_to([0, -2.4, 0])
        else:
            leg_a.move_to([0, -3.05, 0]).align_to([-6.2, 0, 0], LEFT)
            leg_b.move_to([0, -3.05, 0]).align_to([-2.6, 0, 0], LEFT)
            note.move_to([0, -3.05, 0]).align_to([2.8, 0, 0], LEFT)
            legend = VGroup(leg_a, leg_b)
        self.go(9.0, LaggedStart(*[GrowFromEdge(r[2], LEFT) for r in rows], lag_ratio=.2, run_time=1.4), FadeIn(leg_a), rt=None)
        self.go(10.7, LaggedStart(*[GrowFromEdge(r[3], LEFT) for r in rows], lag_ratio=.2, run_time=1.4), FadeIn(leg_b), rt=None)
        self.go(13.6, FadeIn(note), rt=.4)
        # the highest-scoring path wins; the others fade (never below 40%)
        win = SurroundingRectangle(rows[0][0], color=TEAL, buff=.15, stroke_width=6)
        self.go(15.4, Create(win), rows[1][0].animate.set_opacity(.4), rows[2][0].animate.set_opacity(.4),
                rows[1][2].animate.set_opacity(.4), rows[2][2].animate.set_opacity(.4),
                rows[1][3].animate.set_opacity(.4), rows[2][3].animate.set_opacity(.4), rt=.7)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B10")
class B10_OldVsNew(Scene):
    def construct(self):
        # a three-stop timeline across the top; the active stop is named once, beneath it
        xs = [-L(4.6, 1.2), 0, L(4.6, 1.2)]
        ty = L(3.05, 3.15)
        line = Line([xs[0], ty, 0], [xs[2], ty, 0], stroke_color=FAINT, stroke_width=5)
        dots = VGroup(*[Dot([x, ty, 0], radius=.16, color=FAINT) for x in xs])
        self.add(line, dots)

        def light(i):
            return [dots[j].animate.set_color(TEAL if j == i else FAINT) for j in range(3)]

        def title(text):
            return label(text, L(50, 32), TEAL).move_to([0, L(2.5, 2.65), 0])
        t1, t2, t3 = title("dictionary and rules"), title("counted text"), title("neural networks")

        # stop 1: the first Japanese word processor
        mc = machine(L(1.75, .95)).move_to([-L(3.6, 0), L(-.15, 1.45), 0])
        cap = label("the first Japanese word processor", L(46, 28), INK, L(5.2, WIDTH)).move_to([-L(3.5, 0), L(-1.95, .45), 0])
        self.go(1.3, *light(0), FadeIn(t1), FadeIn(mc), rt=.6)
        self.go(3.7, FadeIn(cap), rt=.5)
        rx = L(3.0, 0)
        ry = L(-.25, -.75)
        bk = book(L(1.5, .75)).move_to([rx - L(1.5, 1.0), ry, 0])
        bk_t = label("dictionary", L(40, 24), INK, 2.2).next_to(bk, DOWN, buff=.15)
        ru = card(T("grammar rules", L(40, 24), INK), L(3.0, 1.7), L(1.2, .7))
        ru.move_to([rx + L(1.2, 1.0), ry, 0])
        self.go(6.2, FadeIn(bk), FadeIn(bk_t), rt=.5)
        self.go(8.2, FadeIn(ru), rt=.5)
        # homophones weighed by context and use
        self.go(9.4, FadeOut(Group(bk, bk_t, ru)), rt=.3)
        c1 = card(J("橋", L(100, 46)), L(1.9, 1.0), L(1.9, 1.0)).move_to([rx - L(1.8, .95), L(-.45, -1.0), 0])
        c2 = card(J("箸", L(100, 46)), L(1.9, 1.0), L(1.9, 1.0)).move_to([rx + L(1.8, .95), L(-.45, -1.0), 0])
        hl = label("homophones", L(40, 24), GREY).move_to([rx, L(1.0, -.1), 0])
        self.go(9.7, FadeIn(c1), FadeIn(c2), FadeIn(hl), rt=.5)
        w1 = label("sentence context", L(40, 22), TEAL, L(3.0, 1.7)).next_to(c1, DOWN, buff=.25)
        w2 = label("how often used", L(40, 22), TEAL, L(3.0, 1.7)).next_to(c2, DOWN, buff=.25)
        self.go(11.1, FadeIn(w1), rt=.4)
        self.go(12.6, FadeIn(w2), rt=.4)
        ck = VMobject(stroke_color=TEAL, stroke_width=10).set_points_as_corners([[-.3, 0, 0], [-.05, -.28, 0], [.38, .3, 0]]).scale(L(1.2, .7)).move_to(c1.get_corner(UL) + np.array([-.15, .1, 0]))
        self.go(13.7, FadeIn(ck), rt=.3)

        # stop 2: later keyboards counted words
        self.go(14.5, FadeOut(Group(mc, cap, c1, c2, hl, w1, w2, ck, t1)), *light(1), FadeIn(t2), rt=.4)
        pages = VGroup(*[Rectangle(width=L(2.0, .75), height=L(2.6, 1.05), stroke_color=INK, stroke_width=4, fill_color=CREAM, fill_opacity=1).shift(RIGHT * L(.3, .18) * i + DOWN * .13 * i) for i in range(4)])
        pages.move_to([-L(4.4, 1.2), L(.55, 1.0), 0])
        hs = [1.0, 2.3, 1.7, 3.1]
        words = VGroup(*[Rectangle(width=L(1.2, .36), height=L(h, h * .6), stroke_color=INK, stroke_width=3, fill_color=TEAL, fill_opacity=1) for h in hs])
        words.arrange(RIGHT, buff=L(.35, .12), aligned_edge=DOWN).move_to([L(3.2, .95), L(.2, .5), 0])
        tally = label("counted words", L(60, 32), INK).move_to([0, L(-2.0, -1.35), 0])
        big = label("in huge amounts of text", L(52, 28), GREY).move_to([0, L(-2.9, -2.0), 0])
        self.go(14.9, FadeIn(pages, shift=RIGHT * .1), rt=.3)
        self.go(15.2, LaggedStart(*[GrowFromEdge(w_, DOWN) for w_ in words], lag_ratio=.25, run_time=1.1), FadeIn(tally), rt=None)
        self.go(16.4, FadeIn(big), rt=.5)

        # stop 3: neural networks called Transformers
        self.go(18.0, FadeOut(Group(pages, words, tally, big, t2)), *light(2), FadeIn(t3), rt=.4)
        cols = [2, 4, 4, 2]
        layers = [VGroup(*[Dot(radius=L(.16, .1), color=SLATE) for _ in range(n_)]).arrange(DOWN, buff=L(.5, .3)) for n_ in cols]
        net = VGroup(*layers).arrange(RIGHT, buff=L(2.8, .75)).move_to([0, L(.95, 1.25), 0])
        edges = VGroup()
        for a_, b_ in zip(layers[:-1], layers[1:]):
            for u in a_:
                for v in b_:
                    edges.add(Line(u.get_center(), v.get_center(), stroke_color=FAINT, stroke_width=1.5))
        self.go(18.5, Create(edges), FadeIn(net), rt=.9)
        tf = pill("Transformers", L(70, 36), TEAL, stroke=TEAL).move_to([L(-3.3, 0), L(-.8, -.3), 0])
        self.go(19.8, FadeIn(tf, shift=UP * .1), rt=.5)
        same = label("the same design family as ChatGPT", L(44, 22), GREY, L(5.2, WIDTH))
        same.next_to(tf, L(RIGHT, DOWN), buff=L(.5, .2))
        self.go(21.2, FadeIn(same), rt=.5)
        # convert as you type
        typed = [Text(c, font="Menlo", font_size=L(76, 32), color=INK) for c in "hashi"]
        trow = VGroup(*typed).arrange(RIGHT, buff=.15)
        out = J("橋", L(104, 44), TEAL)
        arrow = Text("→", font=JP, font_size=L(76, 32), color=INK)
        pair = VGroup(trow, arrow, out).arrange(RIGHT, buff=L(.4, .25))
        field = RoundedRectangle(corner_radius=.2, width=L(8.6, 3.7), height=L(1.3, .95), stroke_color=SLATE, stroke_width=4,
                                 fill_color=CREAM, fill_opacity=1).move_to([0, L(-2.1, -1.85), 0])
        pair.move_to(field.get_center())
        cap2 = label("convert as you type", L(40, 28), INK).move_to([0, L(-3.1, -2.6), 0])
        self.go(21.9, FadeIn(field), rt=.4)
        self.go(23.9, FadeIn(arrow), rt=.2)
        self.go(24.1, LaggedStart(*[FadeIn(x) for x in typed], lag_ratio=.3, run_time=1.2), rt=None)
        self.go(25.4, FadeIn(out, scale=1.2), FadeIn(cap2), rt=.5)
        self.finish()


# -------------------------------------------------------------------------------------
@timed("B11")
class B11_WhereItFails(Scene):
    def construct(self):
        ime = card(T("IME", L(90, 50), TEAL), L(4.0, 2.4), L(1.8, 1.0), stroke=TEAL, width=5).move_to([-L(2.9, 0), L(-.9, .3), 0])
        nm = J("けや", L(170, 120)).move_to([-L(3.5, 0), L(1.9, 2.55), 0])
        nw = pill("a brand-new word", L(44, 28), INK, pad=.3).move_to([L(3.5, 0), L(1.9, 1.4), 0])
        self.go(.4, FadeIn(ime), rt=.5)
        self.go(1.9, FadeIn(nm, shift=DOWN * .2), rt=.4)
        self.go(2.4, FadeIn(nw, shift=DOWN * .2), rt=.4)
        # a dictionary lookup comes back empty
        bk = book(L(1.1, .85)).move_to([L(3.0, 0), L(-.9, -1.0), 0])
        bkt = label("dictionary", L(44, 28), INK, 2.6).next_to(bk, DOWN, buff=.12)
        mg = VGroup(Circle(radius=.36, stroke_color=INK, stroke_width=5), Line([.26, -.26, 0], [.66, -.66, 0], stroke_color=INK, stroke_width=6))
        mg.scale(L(1.3, .8)).move_to(bk.get_center() + UP * .15 + RIGHT * .1)
        empty = label("no entry", L(54, 32), CRIMSON).next_to(bkt, DOWN, buff=.15)
        self.go(3.6, FadeIn(bk), FadeIn(bkt), rt=.4)
        self.go(4.0, Create(mg), rt=.3)
        self.go(4.4, FadeIn(empty), rt=.4)
        # then the kana is cut in the wrong place, and the wrong kanji is picked
        ny = L(1.85, 2.4)
        self.go(5.0, FadeOut(Group(bk, bkt, mg, empty, nw, ime)), nm.animate.move_to([0, ny, 0]), rt=.5)
        cut = Line([0, nm.get_bottom()[1] - L(.5, .35), 0], [0, nm.get_bottom()[1] - .05, 0], stroke_color=CRIMSON, stroke_width=7)
        wr = label("cut in the wrong place", L(66, 34), CRIMSON).move_to([0, L(-.15, .95), 0])
        self.go(5.5, Create(cut), FadeIn(wr), rt=.5)
        w1 = card(J("毛", L(160, 90)), L(2.7, 1.5), L(2.4, 1.4)).move_to([-L(3.1, .85), L(-2.2, -.9), 0])
        w2 = card(J("矢", L(160, 90)), L(2.7, 1.5), L(2.4, 1.4)).move_to([L(3.1, .85), L(-2.2, -.9), 0])
        self.go(6.9, FadeIn(w1), FadeIn(w2), rt=.5)
        wk = label("the wrong kanji", L(52, 28), CRIMSON, L(3.2, 3.0)).move_to([0, L(-2.2, -2.0), 0])
        x1 = Cross(Square(.4), stroke_color=CRIMSON, stroke_width=7).next_to(w1, UP, buff=.15)
        x2 = Cross(Square(.4), stroke_color=CRIMSON, stroke_width=7).next_to(w2, UP, buff=.15)
        self.go(7.7, Create(x1), Create(x2), w1[0].animate.set_stroke(CRIMSON), w2[0].animate.set_stroke(CRIMSON), FadeIn(wk), rt=.5)
        self.finish()
