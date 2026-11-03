"""
Portrait (9:16) Manim scenes for weekly-recap-hotel-short

Ports of the four graphic beats (B01, B04, B07, B08) -- full parity with the
16:9 cut, no beats dropped. Stacked horizontal cards for a 4.5 x 8.0 frame;
same palette and copy as the 16:9 scenes. All visuals are generated: no
photos, no people shapes; the strategy-draft card uses blank placeholder bars.
"""

from manim import *
import numpy as np

config.frame_width = 4.5
config.frame_height = 8.0

SAFE_W = 3.7

PALETTE = {
    "bg":     "#FAF9F5",
    "ink":    "#3D3929",
    "accent": "#D97757",
    "good":   "#4A7C59",
    "miss":   "#C0392B",
    "card":   "#FFFFFF",
    "border": "#E8E4DA",
    "dim":    "#8B8878",
}


def card_bg(width, height, stroke_color=None):
    return RoundedRectangle(
        corner_radius=0.12, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=stroke_color or PALETTE["border"], stroke_width=1.5,
    )


def grow_in(scene, mob, target_width, run_time=0.5, **kwargs):
    mob.stretch(0.01, 0)
    scene.play(mob.animate.stretch_to_fit_width(target_width), run_time=run_time, **kwargs)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def lines(txt, fs, color, max_w=None, buff=0.1, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def chip(label, w=2.6, h=0.5, border=None, color=None, fs=14):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.2)
    return VGroup(box, txt.move_to(box.get_center()))


def reveal_card(scene, card, run_time=0.8):
    box, inner = card[0], card[1]
    target_w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), run_time=run_time * 0.55)
    scene.play(FadeIn(inner), run_time=run_time * 0.45)


# --- icons ------------------------------------------------------------------

def article_icon():
    page = RoundedRectangle(corner_radius=0.05, width=0.7, height=0.9, fill_color=PALETTE["bg"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=1.5)
    ln = VGroup(*[Line(LEFT * 0.22, RIGHT * (0.22 - 0.08 * i), color=PALETTE["border"], stroke_width=2)
                  for i in range(4)]).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(page.get_center())
    return VGroup(page, ln)


def calendar_house_icon():
    page = RoundedRectangle(corner_radius=0.06, width=1.5, height=1.2, fill_color=PALETTE["bg"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=2)
    band = Rectangle(width=1.5, height=0.26, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    band.align_to(page, UP)
    cells = VGroup(*[Square(side_length=0.15, fill_color=PALETTE["accent"] if i in (2, 6, 9) else PALETTE["border"],
                            fill_opacity=1, stroke_width=0) for i in range(12)]
                   ).arrange_in_grid(rows=3, cols=4, buff=0.1).move_to(page.get_center() + DOWN * 0.15)
    return VGroup(page, band, cells)


def draft_icon():
    page = RoundedRectangle(corner_radius=0.06, width=1.1, height=1.4, fill_color=PALETTE["bg"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=2)
    rows = VGroup()
    for i in range(4):
        box = Square(side_length=0.12, color=PALETTE["dim"], fill_opacity=0, stroke_width=1.8)
        bar = Line(ORIGIN, RIGHT * (0.5 - 0.06 * (i % 2)), color=PALETTE["border"], stroke_width=4)
        rows.add(VGroup(box, bar).arrange(RIGHT, buff=0.1))
    rows.arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(page.get_center())
    return VGroup(page, rows)


def videos_icon():
    def vid():
        land = RoundedRectangle(corner_radius=0.04, width=0.9, height=0.5, fill_color=PALETTE["bg"], fill_opacity=1,
                                stroke_color=PALETTE["good"], stroke_width=2)
        port = RoundedRectangle(corner_radius=0.04, width=0.3, height=0.5, fill_color=PALETTE["bg"], fill_opacity=1,
                                stroke_color=PALETTE["good"], stroke_width=2)
        tl = Text("16:9", color=PALETTE["dim"], font_size=9).move_to(land.get_center())
        tp = Text("9:16", color=PALETTE["dim"], font_size=8).move_to(port.get_center())
        tick = VMobject(color=PALETTE["good"], stroke_width=3.5)
        tick.set_points_as_corners([[-0.08, 0, 0], [-0.02, -0.07, 0], [0.1, 0.08, 0]])
        tick.next_to(port, RIGHT, buff=0.12)
        return VGroup(VGroup(land, tl), VGroup(port, tp), tick).arrange(RIGHT, buff=0.12)
    return VGroup(vid(), vid()).arrange(DOWN, buff=0.18)


def hcard(icon, parts, w=3.7, h=1.3, border=None, icon_h=None):
    box = card_bg(w, h, stroke_color=border)
    icon = icon.copy()
    icon.scale_to_fit_height(icon_h or (h - 0.4))
    if icon.width > 1.15:
        icon.scale_to_fit_width(1.15)
    texts = VGroup(*[lines(t, fs, c, buff=0.04, weight=wt) for (t, fs, c, wt) in parts]).arrange(
        DOWN, buff=0.07, aligned_edge=LEFT)
    inner = VGroup(icon, texts).arrange(RIGHT, buff=0.28)
    fit(inner, w - 0.4)
    return VGroup(box, inner.move_to(box.get_center()))


def _article(h=1.3, tag=None):
    parts = ([tag] if tag else []) + [("SUBSTACK · ARTICLE", 9, PALETTE["accent"], None),
                                      ("The Hotel Phone\nGets a Helper", 14, PALETTE["ink"], "BOLD"),
                                      ("AI voice assistants,\nfront desks", 9, PALETTE["dim"], None)]
    return hcard(article_icon(), parts, h=h, icon_h=0.8 if tag else 0.9)


def _meetings(h=1.3, tag=None):
    parts = ([tag] if tag else []) + [("Homes of Hope", 15, PALETTE["ink"], "BOLD"),
                                      ("meetings", 12, PALETTE["dim"], None)]
    return hcard(calendar_house_icon(), parts, h=h, icon_h=0.7)


def _draft(h=1.3, tag=None, border=None):
    parts = ([tag] if tag else []) + [("Draft: documentary\npromotion strategies\n(with Yatra)", 11, PALETTE["ink"],
                                       None)]
    return hcard(draft_icon(), parts, h=h, icon_h=0.85 if tag else 0.95, border=border)


def _videos(h=1.3, tag=None):
    parts = ([tag] if tag else []) + [("two videos,\nfour files", 14, PALETTE["ink"], None),
                                      ("16:9 + 9:16 each", 10, PALETTE["dim"], None)]
    return hcard(videos_icon(), parts, h=h, icon_h=0.95)


# --- scenes -----------------------------------------------------------------

class B01_NotAHighlightReel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(VGroup(*[Text(t, color=PALETTE["ink"], font_size=40)
                              for t in ("Not a", "highlight", "reel.")]).arrange(DOWN, buff=0.22), 3.4)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = fit(VGroup(*[Text(t, color=PALETTE["dim"], font_size=22)
                           for t in ("A real log", "of the week.")]).arrange(DOWN, buff=0.15), 3.4)
        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [_article(), _meetings(), _draft(), _videos()]
        VGroup(*cards).arrange(DOWN, buff=0.15).move_to(UP * 0.55)

        for c in cards:
            reveal_card(self, c, run_time=0.9)

        footer = lines("Same weight. No sense of\nwhat's unfinished.", 15, PALETTE["dim"], max_w=3.6, buff=0.08)
        footer.move_to(DOWN * 2.95)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [
            _article(h=1.35, tag=("PUBLISHED", 10, PALETTE["good"], "BOLD")),
            _meetings(h=1.35, tag=("ATTENDED", 10, PALETTE["good"], "BOLD")),
            _draft(h=1.35, tag=("FIRST DRAFT", 10, PALETTE["accent"], "BOLD"), border=PALETTE["accent"]),
            _videos(h=1.35, tag=("PRODUCED", 10, PALETTE["good"], "BOLD")),
        ]
        VGroup(*cards).arrange(DOWN, buff=0.13).move_to(UP * 0.55)

        for c in cards:
            reveal_card(self, c, run_time=0.8)

        count = chip("3 finished · 1 first draft", w=3.6, h=0.65, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=17)
        count.move_to(DOWN * 2.95)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=32)
        l2 = VGroup(*[Text(t, color=PALETTE["ink"], font_size=32) for t in ("A draft is", "a draft.")]
                    ).arrange(DOWN, buff=0.15)
        l3 = Text("Said plainly.", color=PALETTE["accent"], font_size=32)
        g = VGroup(l1, l2, l3).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        fit(g, 3.4)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
