"""
Portrait (9:16) Manim scenes for weekly-recap-tutor-short

Ports of the four graphic beats (B01, B04, B07, B08) -- full parity with the
16:9 cut, no beats dropped. Stacked horizontal cards for a 4.5 x 8.0 frame;
same palette and copy as the 16:9 scenes.
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


def _reveal_card(scene, card, run_time=0.7):
    # Box grows first, then its contents fade in (no content hanging past a growing box).
    box, inner = card[0], card[1]
    target_w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), run_time=run_time * 0.55)
    scene.play(FadeIn(inner), run_time=run_time * 0.45)


# --- icons ------------------------------------------------------------------

def _article_icon():
    page = RoundedRectangle(corner_radius=0.05, width=0.62, height=0.8,
                             fill_color=PALETTE["bg"], fill_opacity=1,
                             stroke_color=PALETTE["dim"], stroke_width=1.5)
    lines = VGroup(*[
        Line(LEFT * 0.2, RIGHT * (0.2 - 0.07 * i), color=PALETTE["border"], stroke_width=2)
        for i in range(4)
    ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    lines.move_to(page.get_center())
    return VGroup(page, lines)


def _video_icon():
    def mini_frame():
        f = RoundedRectangle(corner_radius=0.04, width=0.42, height=0.3,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["dim"], stroke_width=1.5)
        tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                        fill_opacity=1, stroke_width=0).scale(0.05).rotate(-PI / 2)
        tri.move_to(f.get_center())
        return VGroup(f, tri)
    return VGroup(*[mini_frame() for _ in range(4)]).arrange_in_grid(rows=2, cols=2, buff=0.08)


def _slides_icon():
    slide = RoundedRectangle(corner_radius=0.05, width=0.85, height=0.55,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["accent"], stroke_width=2)
    slide_lines = VGroup(*[
        Line(LEFT * 0.32, RIGHT * (0.32 - 0.12 * i), color=PALETTE["dim"], stroke_width=1.5)
        for i in range(2)
    ]).arrange(DOWN, buff=0.09)
    slide_lines.move_to(slide.get_center())
    podium = Polygon(
        [-0.22, -0.32, 0], [0.22, -0.32, 0], [0.14, 0.0, 0], [-0.14, 0.0, 0],
        fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0,
    )
    podium.next_to(slide, DOWN, buff=0.02)
    return VGroup(slide, slide_lines, podium)


def _calendar_icon():
    page = RoundedRectangle(corner_radius=0.06, width=0.95, height=0.85,
                             fill_color=PALETTE["bg"], fill_opacity=1,
                             stroke_color=PALETTE["accent"], stroke_width=2)
    band = Rectangle(width=0.95, height=0.2, fill_color=PALETTE["accent"], fill_opacity=1,
                      stroke_width=0)
    band.align_to(page, UP)
    day = Text("TUE", color=PALETTE["ink"], font_size=18, weight="BOLD")
    day.move_to(page.get_center() + DOWN * 0.1)
    return VGroup(page, band, day)


def hcard(icon, lines, w=3.6, h=1.6, border=None, icon_h=None):
    """Horizontal card: icon on the left, text lines on the right."""
    box = card_bg(w, h, stroke_color=border or PALETTE["border"])
    icon = icon.copy()
    icon.scale_to_fit_height(icon_h or (h - 0.55))
    if icon.width > 1.0:
        icon.scale_to_fit_width(1.0)
    texts = VGroup(*[
        Text(t, color=c, font_size=fs, weight=wt, line_spacing=1.15)
        for (t, fs, c, wt) in lines
    ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    inner = VGroup(icon, texts).arrange(RIGHT, buff=0.3)
    fit(inner, w - 0.4)
    return VGroup(box, inner.move_to(box.get_center()))


def _article(w=3.6, h=1.6, icon_h=None):
    return hcard(_article_icon(), [
        ("SUBSTACK · ARTICLE", 10, PALETTE["accent"], "NORMAL"),
        ("The Tutor\nThey Never Had", 15, PALETTE["ink"], "BOLD"),
    ], w, h, icon_h=icon_h)


def _videos(w=3.6, h=1.6, icon_h=None):
    return hcard(_video_icon(), [
        ("Four videos,\nproduced", 15, PALETTE["ink"], "NORMAL"),
        ("16:9 + 9:16", 11, PALETTE["dim"], "NORMAL"),
    ], w, h, icon_h=icon_h)


def _slides(badge, w=3.6, h=1.6, icon_h=None):
    return hcard(_slides_icon(), [
        ("Lecture\npresentation", 15, PALETTE["ink"], "NORMAL"),
        (badge, 11, PALETTE["dim"], "NORMAL"),
    ], w, h, icon_h=icon_h)


def _tuesday(w=3.6, h=1.5, icon_h=None):
    return hcard(_calendar_icon(), [
        ("Guest lecture", 16, PALETTE["ink"], "BOLD"),
        ("this Tuesday", 12, PALETTE["dim"], "NORMAL"),
        ("with Yatra", 12, PALETTE["dim"], "NORMAL"),
    ], w, h, border=PALETTE["accent"], icon_h=icon_h)


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

        a = _article(h=1.65, icon_h=1.0)
        b = _videos(h=1.65, icon_h=0.8)
        c = _slides("with Yatra", h=1.65, icon_h=0.95)
        col = VGroup(a, b, c).arrange(DOWN, buff=0.2).move_to(UP * 0.35)

        _reveal_card(self, a, run_time=0.6)
        _reveal_card(self, b, run_time=0.6)
        _reveal_card(self, c, run_time=0.6)

        footer = fit(Text("Same weight. No sense\nof what's finished.", color=PALETTE["dim"],
                           font_size=15, line_spacing=1.2, should_center=True), 3.6)
        footer.move_to(DOWN * 2.95)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_SplitWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        done_head = Text("DONE THIS WEEK", color=PALETTE["good"], font_size=17)
        next_head = Text("NEXT", color=PALETTE["accent"], font_size=17)

        a = _article(h=1.05, icon_h=0.6)
        b = _videos(h=1.05, icon_h=0.55)
        c = _slides("finished", h=1.05, icon_h=0.6)
        d = _tuesday(h=1.5, icon_h=0.9)

        done_cards = VGroup(a, b, c).arrange(DOWN, buff=0.14)
        done_col = VGroup(done_head, done_cards).arrange(DOWN, buff=0.22)
        done_col.move_to(UP * 1.25)

        divider = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["border"], stroke_width=2)
        divider.move_to(DOWN * 1.1)

        next_col = VGroup(next_head, d).arrange(DOWN, buff=0.22)
        next_col.move_to(DOWN * 2.3)

        self.play(FadeIn(done_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, a, run_time=0.5)
        _reveal_card(self, b, run_time=0.5)
        _reveal_card(self, c, run_time=0.5)

        grow_in(self, divider, divider.get_width(), run_time=0.4)

        self.play(FadeIn(next_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, d, run_time=0.5)

        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("Done from next.", color=PALETTE["ink"], font_size=32)
        l2 = VGroup(*[Text(t, color=PALETTE["ink"], font_size=32)
                      for t in ("Not a small", "detail.")]).arrange(DOWN, buff=0.15)
        l3 = VGroup(*[Text(t, color=PALETTE["accent"], font_size=32)
                      for t in ("The whole", "difference.")]).arrange(DOWN, buff=0.15)
        g = VGroup(l1, l2, l3).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        fit(g, 3.4)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
