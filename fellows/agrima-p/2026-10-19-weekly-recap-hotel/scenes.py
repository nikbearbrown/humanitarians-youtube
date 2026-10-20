"""
Manim scenes for weekly-recap-hotel

A first-person, honest weekly-progress CLI-explainer. The two OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py. Every
visual here is a generated graphic: no photos, no people shapes. The Homes of
Hope card is abstract (a calendar and a house outline); the strategy-draft
card uses blank placeholder bars and describes nothing beyond "first draft".
Built in the house Claude palette.

B01_NotAHighlightReel — typographic card: "Not a highlight reel."
B04_FlatWeek          — four same-weight cards: article / meetings / draft / videos
B07_StatusWeek        — the same four with status chips + the finished/draft count
B08_TheLesson         — closing typographic beat
"""

from manim import *
import numpy as np

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


def lines(txt, fs, color, max_w=None, buff=0.12, weight=None):
    kw = {"weight": weight} if weight else {}
    g = VGroup(*[Text(t, color=color, font_size=fs, **kw) for t in txt.split("\n")]).arrange(DOWN, buff=buff)
    return fit(g, max_w) if max_w else g


def chip(label, w=2.6, h=0.6, border=None, color=None, fs=16):
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    txt = fit(Text(label, color=color or PALETTE["ink"], font_size=fs), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


def reveal_card(scene, card, run_time=0.8):
    # Grow the box first, then fade in its content (no content hanging past a growing box).
    box, inner = card[0], card[1]
    target_w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), run_time=run_time * 0.55)
    scene.play(FadeIn(inner), run_time=run_time * 0.45)


class B01_NotAHighlightReel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("Not a highlight reel.", color=PALETTE["ink"], font_size=40)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = Text("A real log of the week.", color=PALETTE["dim"], font_size=20)

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


# --- icons ------------------------------------------------------------------

def article_icon_block(w):
    dots = VGroup(*[Circle(radius=0.045, color=PALETTE["border"], fill_color=PALETTE["border"],
                           fill_opacity=1, stroke_width=0) for _ in range(3)]).arrange(RIGHT, buff=0.09)
    rule = Line(LEFT * (w * 0.32), RIGHT * (w * 0.32), color=PALETTE["border"], stroke_width=1.5)
    return VGroup(dots, rule).arrange(DOWN, buff=0.1)


def calendar_icon():
    page = RoundedRectangle(corner_radius=0.06, width=1.5, height=1.2, fill_color=PALETTE["bg"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=2)
    band = Rectangle(width=1.5, height=0.26, fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    band.align_to(page, UP)
    cells = VGroup(*[Square(side_length=0.15, fill_color=PALETTE["accent"] if i in (2, 6, 9) else PALETTE["border"],
                            fill_opacity=1, stroke_width=0) for i in range(12)]
                   ).arrange_in_grid(rows=3, cols=4, buff=0.1).move_to(page.get_center() + DOWN * 0.15)
    return VGroup(page, band, cells)


def house_outline():
    roof = Triangle(color=PALETTE["dim"], fill_opacity=0, stroke_width=2.5).scale(0.34).stretch(1.4, 0)
    body = Rectangle(width=0.62, height=0.4, color=PALETTE["dim"], fill_opacity=0, stroke_width=2.5)
    door = Rectangle(width=0.14, height=0.22, color=PALETTE["dim"], fill_opacity=0, stroke_width=2)
    g = VGroup(roof, body).arrange(DOWN, buff=0)
    door.move_to(body.get_bottom() + UP * 0.11)
    return VGroup(g, door)


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
    def vid(label):
        land = RoundedRectangle(corner_radius=0.04, width=0.9, height=0.5, fill_color=PALETTE["bg"], fill_opacity=1,
                                stroke_color=PALETTE["good"], stroke_width=2)
        port = RoundedRectangle(corner_radius=0.04, width=0.3, height=0.5, fill_color=PALETTE["bg"], fill_opacity=1,
                                stroke_color=PALETTE["good"], stroke_width=2)
        tl = Text("16:9", color=PALETTE["dim"], font_size=9).move_to(land.get_center())
        tp = Text("9:16", color=PALETTE["dim"], font_size=8).move_to(port.get_center())
        tick = VMobject(color=PALETTE["good"], stroke_width=3.5)
        tick.set_points_as_corners([[-0.08, 0, 0], [-0.02, -0.07, 0], [0.1, 0.08, 0]])
        tick.next_to(port, RIGHT, buff=0.12)
        frames = VGroup(VGroup(land, tl), VGroup(port, tp), tick).arrange(RIGHT, buff=0.12)
        lab = Text(label, color=PALETTE["ink"], font_size=11)
        return VGroup(lab, frames).arrange(DOWN, buff=0.08)
    return VGroup(vid("the hotel video"), vid("this recap")).arrange(DOWN, buff=0.2)


def _card_article(w=2.8, h=3.7, tag=None, border=None):
    box = card_bg(w, h, stroke_color=border)
    kicker = Text("SUBSTACK · ARTICLE", color=PALETTE["accent"], font_size=10)
    title = lines("The Hotel Phone\nGets a Helper", 17, PALETTE["ink"], weight="BOLD", buff=0.08, max_w=w - 0.4)
    by = fit(Text("AI voice assistants, front desks", color=PALETTE["dim"], font_size=10), w - 0.3)
    parts = [article_icon_block(w), kicker, title, by]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.2)
    return VGroup(box, inner.move_to(box.get_center()))


def _card_meetings(w=2.8, h=3.7, tag=None, border=None):
    box = card_bg(w, h, stroke_color=border)
    cal = calendar_icon()
    hs = house_outline()
    row = fit(VGroup(cal, hs).arrange(RIGHT, buff=0.2), w - 0.7)
    title = Text("Homes of Hope", color=PALETTE["ink"], font_size=16, weight="BOLD")
    sub = Text("meetings", color=PALETTE["dim"], font_size=13)
    parts = [row, title, sub]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.22)
    return VGroup(box, fit(inner, w - 0.3).move_to(box.get_center()))


def _card_draft(w=2.8, h=3.7, tag=None, border=None):
    box = card_bg(w, h, stroke_color=border)
    ic = draft_icon()
    title = lines("Draft: documentary\npromotion strategies\n(with Yatra)", 12, PALETTE["ink"], buff=0.05,
                  max_w=w - 0.3)
    parts = [ic, title]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.2)
    return VGroup(box, inner.move_to(box.get_center()))


def _card_videos(w=2.8, h=3.7, tag=None, border=None):
    box = card_bg(w, h, stroke_color=border)
    ic = videos_icon()
    t = lines("two videos,\nfour files", 14, PALETTE["ink"], buff=0.06)
    parts = [ic, t]
    if tag:
        parts.insert(0, tag)
    inner = VGroup(*parts).arrange(DOWN, buff=0.22)
    return VGroup(box, fit(inner, w - 0.3).move_to(box.get_center()))


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cards = [_card_article(), _card_meetings(), _card_draft(), _card_videos()]
        VGroup(*cards).arrange(RIGHT, buff=0.3).move_to(UP * 0.15)

        for c in cards:
            reveal_card(self, c, run_time=0.9)

        footer = Text("Same weight. No sense of what's unfinished.", color=PALETTE["dim"],
                      font_size=17).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_StatusWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        def tag(label, color):
            return chip(label, w=2.0, h=0.4, border=color, color=color, fs=12)

        cards = [
            _card_article(h=3.5, tag=tag("PUBLISHED", PALETTE["good"])),
            _card_meetings(h=3.5, tag=tag("ATTENDED", PALETTE["good"])),
            _card_draft(h=3.5, tag=tag("FIRST DRAFT", PALETTE["accent"]), border=PALETTE["accent"]),
            _card_videos(h=3.5, tag=tag("PRODUCED", PALETTE["good"])),
        ]
        VGroup(*cards).arrange(RIGHT, buff=0.3).move_to(UP * 0.55)

        for c in cards:
            reveal_card(self, c, run_time=0.8)

        count = chip("3 finished  ·  1 first draft", w=5.2, h=0.8, border=PALETTE["accent"],
                     color=PALETTE["accent"], fs=22)
        count.move_to(DOWN * 2.45)
        self.play(FadeIn(count, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("Done is done.", color=PALETTE["ink"], font_size=32)
        l2 = Text("A draft is a draft.", color=PALETTE["ink"], font_size=32)
        l3 = Text("Said plainly.", color=PALETTE["accent"], font_size=32)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
