"""
Portrait (9:16) Manim scenes for the weekly-recap-catbot Short.

This Short is a FULL-PARITY reformat -- the parent (2:10.3) is well under the
3:00 Shorts cap, so shorts.py's auto-plan drops nothing. All 11 parent beats
+ a silent endcard are present here, just relaid out for a narrow, tall
canvas (~4.5 x 8 units vs ~14.2 x 8 landscape): single-column stacks instead
of side-by-side rows, generous to_edge() buffs (>=0.7) per this session's
GATE B near-miss lessons.

B01_NotAHighlightReel — typographic card (unchanged content, portrait layout)
B04_FlatWeek          — three same-weight cards, STACKED vertically
B07_SplitWeek         — same three cards, regrouped DONE/NEXT, stacked
B08_TheLesson         — typographic closing beat (unchanged content)
"""

from manim import *
import numpy as np

config.frame_width = 4.5
config.frame_height = 8.0

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

SAFE_W = 3.7  # stay inside the 1.95-half-width portrait safe band


def card_bg(width, height, stroke_color=None):
    return RoundedRectangle(
        corner_radius=0.1, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=stroke_color or PALETTE["border"], stroke_width=1.5,
    )


def grow_in(scene, mob, target_width, run_time=0.5, **kwargs):
    mob.stretch(0.01, 0)
    scene.play(mob.animate.stretch_to_fit_width(target_width), run_time=run_time, **kwargs)


def fit(mob, max_w=SAFE_W):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


class B01_NotAHighlightReel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(Text("Not a highlight reel.", color=PALETTE["ink"], font_size=30))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("A real log of the week.", color=PALETTE["dim"], font_size=18))

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.4, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


# ---------------------------------------------------------------------------
# Shared card builders — reused, differently grouped, by B04 and B07.
# ---------------------------------------------------------------------------

def _article_card(w=2.6, h=2.2, fs=13, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    dots = VGroup(*[
        Circle(radius=0.04, color=PALETTE["border"], fill_color=PALETTE["border"],
               fill_opacity=1, stroke_width=0)
        for _ in range(3)
    ]).arrange(RIGHT, buff=0.08)
    header_rule = Line(LEFT * (w * 0.32), RIGHT * (w * 0.32),
                        color=PALETTE["border"], stroke_width=1.5)
    header = VGroup(dots, header_rule).arrange(DOWN, buff=0.09)

    kicker = Text("SUBSTACK · ARTICLE", color=PALETTE["accent"], font_size=fs - 4)
    title = Text("Rescue,\nReinvented", color=PALETTE["ink"], font_size=fs + 2,
                  line_spacing=1.15, should_center=True, weight="BOLD")
    byline = fit(Text("AI in animal shelters", color=PALETTE["dim"], font_size=fs - 4), w - 0.3)

    inner = VGroup(header, kicker, title, byline).arrange(DOWN, buff=0.16)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _video_card(w=2.6, h=2.2, fs=13, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    wide = RoundedRectangle(corner_radius=0.05, width=1.0, height=0.6,
                             fill_color=PALETTE["bg"], fill_opacity=1,
                             stroke_color=PALETTE["dim"], stroke_width=2)
    tall = RoundedRectangle(corner_radius=0.05, width=0.38, height=0.72,
                             fill_color=PALETTE["card"], fill_opacity=1,
                             stroke_color=PALETTE["accent"], stroke_width=2.2)
    tall.move_to(wide.get_center() + RIGHT * 0.28 + DOWN * 0.02)
    tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                    fill_opacity=1, stroke_width=0).scale(0.08).rotate(-PI / 2)
    tri.move_to(wide.get_center() + LEFT * 0.24)
    icon = VGroup(wide, tall, tri)

    badge = Text("16:9 + 9:16", color=PALETTE["dim"], font_size=fs - 3)
    title = Text("Two videos,\nproduced", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True)
    inner = VGroup(icon, title, badge).arrange(DOWN, buff=0.18)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _catbot_card(w=2.6, h=2.2, fs=13, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    head = Circle(radius=0.22, color=PALETTE["dim"], fill_color=PALETTE["dim"],
                   fill_opacity=1, stroke_width=0)
    ear1 = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.09)
    ear1.move_to(head.get_center() + UP * 0.19 + LEFT * 0.14)
    ear2 = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.09)
    ear2.move_to(head.get_center() + UP * 0.19 + RIGHT * 0.14)
    eye1 = Dot(radius=0.017, color=PALETTE["card"]).move_to(head.get_center() + LEFT * 0.065 + UP * 0.015)
    eye2 = Dot(radius=0.017, color=PALETTE["card"]).move_to(head.get_center() + RIGHT * 0.065 + UP * 0.015)
    whisk_l = VGroup(*[
        Line(head.get_center() + LEFT * 0.13 + DOWN * 0.015 * i,
             head.get_center() + LEFT * 0.33 + DOWN * 0.04 * i,
             color=PALETTE["dim"], stroke_width=1.3)
        for i in range(2)
    ])
    whisk_r = VGroup(*[
        Line(head.get_center() + RIGHT * 0.13 + DOWN * 0.015 * i,
             head.get_center() + RIGHT * 0.33 + DOWN * 0.04 * i,
             color=PALETTE["dim"], stroke_width=1.3)
        for i in range(2)
    ])
    cat = VGroup(ear1, ear2, head, eye1, eye2, whisk_l, whisk_r)

    bubble = RoundedRectangle(corner_radius=0.07, width=0.46, height=0.33,
                               fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    tail = Triangle(fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    tail.scale(0.06).rotate(PI).move_to(bubble.get_bottom() + DOWN * 0.02 + LEFT * 0.1)
    ai_txt = Text("AI", color=PALETTE["card"], font_size=fs - 2).move_to(bubble.get_center())
    chat = VGroup(bubble, tail, ai_txt)
    chat.move_to(cat.get_center() + RIGHT * 0.46 + UP * 0.23)

    icon = VGroup(cat, chat)
    title = Text("New idea:\na 'cat bot'", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True)
    badge = fit(Text("shelter research starting", color=PALETTE["dim"], font_size=fs - 4), w - 0.3)
    inner = VGroup(icon, title, badge).arrange(DOWN, buff=0.18)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _reveal_card(scene, card, run_time=0.6):
    box, inner = card[0], card[1]
    target_w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), FadeIn(inner), run_time=run_time)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("This week.", color=PALETTE["dim"],
                      font_size=18).to_edge(UP, buff=0.75)
        self.play(FadeIn(title), run_time=0.4)

        footer = fit(Text("Same weight. No sense of what's finished.",
                           color=PALETTE["dim"], font_size=14))
        footer.to_edge(DOWN, buff=0.75)

        # cards built at a comfortable base size, then uniformly scaled down
        # so 3 stacked cards + title + footer all fit the portrait safe band
        a = _article_card(scale=0.62)
        b = _video_card(scale=0.62)
        c = _catbot_card(scale=0.62)
        VGroup(a, b, c).arrange(DOWN, buff=0.16).move_to(ORIGIN)

        _reveal_card(self, a, run_time=0.5)
        _reveal_card(self, b, run_time=0.5)
        _reveal_card(self, c, run_time=0.5)

        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.45)
        self.wait(1.2)


class B07_SplitWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        done_head = Text("DONE THIS WEEK", color=PALETTE["good"], font_size=15)
        next_head = Text("STARTING NEXT WEEK", color=PALETTE["accent"], font_size=15)

        a = _article_card(scale=0.55)
        b = _video_card(scale=0.55)
        c = _catbot_card(scale=0.62)

        done_row = VGroup(a, b).arrange(RIGHT, buff=0.2)
        done_col = VGroup(done_head, done_row).arrange(DOWN, buff=0.18)

        next_col = VGroup(next_head, c).arrange(DOWN, buff=0.18)

        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["border"], stroke_width=2)

        VGroup(done_col, divider, next_col).arrange(DOWN, buff=0.28).move_to(ORIGIN)

        self.play(FadeIn(done_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, a, run_time=0.5)
        _reveal_card(self, b, run_time=0.5)

        grow_in(self, divider, divider.get_width(), run_time=0.4)

        self.play(FadeIn(next_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, c, run_time=0.5)

        self.wait(1.2)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("Done from next.", color=PALETTE["ink"], font_size=26))
        l2 = fit(Text("Not a small detail.", color=PALETTE["ink"], font_size=26))
        l3 = fit(Text("The whole difference.", color=PALETTE["accent"], font_size=26))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
