"""
Portrait (9:16) Manim scenes for the weekly-recap-suffolk Short.

Parent is 2:12.5, well under the 3:00 Shorts cap, so shorts.py's auto-plan
dropped nothing -- all 11 parent beats carry over full-parity plus the
silent endcard. The 4 Manim scenes are relaid out here for a narrow, tall
canvas (~4.5 x 8 units vs ~14.2 x 8 landscape): single-column stacks
instead of side-by-side rows/columns, generous to_edge() buffs (>=0.7) per
this session's GATE B near-miss lessons.

B04/B07 also carry forward a fix made on the parent AFTER the first 16:9
render: _reveal_card grows a card's box and fades in its (already
full-size) text at the same time, which briefly shows the text overhanging
the still-narrow box mid-grow -- worse once a beat this short gets slowed
several times over to match its narration. Fixed by growing the box to
full width FIRST, then fading the text in.

B01_NotAHighlightReel — typographic card, generic framing
B04_FlatWeek          — three same-weight cards, stacked: Article / 4 Videos / Suffolk
B07_SplitWeek         — same three cards, regrouped: DONE (stacked) vs STARTING NEXT
B08_TheLesson         — closing typographic beat
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

        phrase = fit(Text("Not a highlight reel.", color=PALETTE["ink"], font_size=30,
                           line_spacing=1.2, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("A real log of the week.", color=PALETTE["dim"], font_size=18))

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.4, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


# ---------------------------------------------------------------------------
# Shared card builders — reused, differently grouped, by B04 and B07.
# ---------------------------------------------------------------------------

def _article_card(w=2.5, h=1.9, fs=12, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    dots = VGroup(*[
        Circle(radius=0.05, color=PALETTE["border"], fill_color=PALETTE["border"],
               fill_opacity=1, stroke_width=0)
        for _ in range(3)
    ]).arrange(RIGHT, buff=0.1)
    header_rule = Line(LEFT * (w * 0.32), RIGHT * (w * 0.32),
                        color=PALETTE["border"], stroke_width=1.5)
    header = VGroup(dots, header_rule).arrange(DOWN, buff=0.1)

    kicker = fit(Text("SUBSTACK · ARTICLE", color=PALETTE["accent"], font_size=fs - 4), w - 0.4)
    title = fit(Text("No Face,\nNo Problem", color=PALETTE["ink"], font_size=fs,
                      line_spacing=1.2, should_center=True, weight="BOLD"), w - 0.4)
    byline = fit(Text("faceless AI, real trust", color=PALETTE["dim"], font_size=fs - 4), w - 0.4)

    inner = VGroup(header, kicker, title, byline).arrange(DOWN, buff=0.22)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _video_card(w=2.5, h=1.9, fs=12, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    def mini_frame():
        f = RoundedRectangle(corner_radius=0.04, width=0.5, height=0.36,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["dim"], stroke_width=1.5)
        tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                        fill_opacity=1, stroke_width=0).scale(0.055).rotate(-PI / 2)
        tri.move_to(f.get_center())
        return VGroup(f, tri)

    grid = VGroup(*[mini_frame() for _ in range(4)]).arrange_in_grid(rows=2, cols=2, buff=0.1)

    badge = fit(Text("16:9 + 9:16", color=PALETTE["dim"], font_size=fs - 3), w - 0.4)
    title = fit(Text("Four videos,\nproduced", color=PALETTE["ink"], font_size=fs,
                      line_spacing=1.2, should_center=True), w - 0.4)
    inner = VGroup(grid, title, badge).arrange(DOWN, buff=0.22)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _suffolk_card(w=2.5, h=1.9, fs=12, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    slide = RoundedRectangle(corner_radius=0.05, width=0.78, height=0.5,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["accent"], stroke_width=2)
    slide_lines = VGroup(*[
        Line(LEFT * 0.29, RIGHT * (0.29 - 0.1 * i), color=PALETTE["dim"], stroke_width=1.5)
        for i in range(2)
    ]).arrange(DOWN, buff=0.08)
    slide_lines.move_to(slide.get_center())
    podium = Polygon(
        [-0.2, -0.28, 0], [0.2, -0.28, 0], [0.13, 0.0, 0], [-0.13, 0.0, 0],
        fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0,
    )
    podium.next_to(slide, DOWN, buff=0.02)
    icon = VGroup(slide, slide_lines, podium)

    title = fit(Text("Suffolk\nUniversity", color=PALETTE["ink"], font_size=fs,
                      line_spacing=1.2, should_center=True), w - 0.4)
    badge = fit(Text("lecture · with Yatra", color=PALETTE["dim"], font_size=fs - 3), w - 0.4)
    inner = VGroup(icon, title, badge).arrange(DOWN, buff=0.22)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _reveal_card(scene, card, run_time=0.7):
    # Grow the box to full width FIRST, then fade in its (already full-size)
    # content -- doing both at once briefly showed the static-sized content
    # overhanging the still-narrow box mid-grow (worse once beats this short
    # get slowed to match narration length, stretching that transient).
    box, inner = card[0], card[1]
    target_w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), run_time=run_time * 0.55)
    scene.play(FadeIn(inner), run_time=run_time * 0.45)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article_card()
        b = _video_card()
        c = _suffolk_card()
        footer = fit(Text("Same weight. No sense of\nwhat's finished.", color=PALETTE["dim"],
                           font_size=14, line_spacing=1.25, should_center=True))

        VGroup(a, b, c, footer).arrange(DOWN, buff=0.16).move_to(ORIGIN)

        _reveal_card(self, a, run_time=0.5)
        _reveal_card(self, b, run_time=0.5)
        _reveal_card(self, c, run_time=0.5)

        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.0)


class B07_SplitWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        done_head = fit(Text("DONE THIS WEEK", color=PALETTE["good"], font_size=16))
        next_head = fit(Text("STARTING NEXT WEEK", color=PALETTE["accent"], font_size=16))

        a = _article_card(w=1.8, h=2.1, fs=11)
        b = _video_card(w=1.8, h=2.1, fs=11)
        c = _suffolk_card()

        done_row = VGroup(a, b).arrange(RIGHT, buff=0.2)
        done_col = VGroup(done_head, done_row).arrange(DOWN, buff=0.22)

        divider = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["border"], stroke_width=2)

        next_col = VGroup(next_head, c).arrange(DOWN, buff=0.22)

        VGroup(done_col, divider, next_col).arrange(DOWN, buff=0.28).move_to(ORIGIN)

        self.play(FadeIn(done_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, a, run_time=0.5)
        _reveal_card(self, b, run_time=0.5)

        grow_in(self, divider, divider.get_width(), run_time=0.4)

        self.play(FadeIn(next_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, c, run_time=0.5)

        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("Done from next.", color=PALETTE["ink"], font_size=28))
        l2 = fit(Text("Not a small detail.", color=PALETTE["ink"], font_size=28))
        l3 = fit(Text("The whole difference.", color=PALETTE["accent"], font_size=28))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
