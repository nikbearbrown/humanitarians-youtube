"""
Portrait (9:16) Manim scenes for the weekly-recap-never-forgets Short.

shorts.py's auto-plan confirmed full parity -- the parent (1:30) is well
under the 3:00 Shorts cap, so no beats were dropped. The 4 Manim scenes are
relaid out here for a narrow, tall canvas (~4.5 x 8 units vs ~14.2 x 8
landscape): a single-column card stack instead of the parent's
side-by-side row, generous to_edge() buffs (>=0.7) per this session's GATE B
near-miss lessons.

B01_NotAHighlightReel — typographic card, generic framing
B04_FlatWeek          — three same-weight cards, stacked: Article / 4 Videos / Meeting
B07_TaggedWeek        — same three cards, stacked, now tagged + a count header
B08_TheLesson         — typographic closing beat
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

        phrase = fit(Text("Not a highlight reel.", color=PALETTE["ink"], font_size=32))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("A flat log of what shipped.", color=PALETTE["dim"], font_size=17))

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.4, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


# ---------------------------------------------------------------------------
# Shared card builders — stacked vertically (portrait), reused by B04/B07.
# ---------------------------------------------------------------------------

def _article_card(w=3.4, h=1.9, fs=15, tag=None):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    dots = VGroup(*[
        Circle(radius=0.04, color=PALETTE["border"], fill_color=PALETTE["border"],
               fill_opacity=1, stroke_width=0)
        for _ in range(3)
    ]).arrange(RIGHT, buff=0.08)
    kicker = Text("SUBSTACK · ARTICLE", color=PALETTE["accent"], font_size=fs - 5)
    title = fit(Text("The AI That Never Forgets", color=PALETTE["ink"], font_size=fs,
                      weight="BOLD"), w - 0.35)

    parts = [dots, kicker, title]
    if tag:
        chip = card_bg(1.15, 0.38, stroke_color=PALETTE["good"])
        chip_lbl = Text(tag, color=PALETTE["good"], font_size=fs - 6)
        parts.append(VGroup(chip, chip_lbl.move_to(chip.get_center())))

    inner = VGroup(*parts).arrange(DOWN, buff=0.16)
    return VGroup(box, inner.move_to(box.get_center()))


def _video_card(w=3.4, h=1.9, fs=15, tag=None):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    def mini_frame():
        f = RoundedRectangle(corner_radius=0.035, width=0.42, height=0.3,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["dim"], stroke_width=1.3)
        tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                        fill_opacity=1, stroke_width=0).scale(0.045).rotate(-PI / 2)
        tri.move_to(f.get_center())
        return VGroup(f, tri)

    grid = VGroup(*[mini_frame() for _ in range(4)]).arrange_in_grid(rows=2, cols=2, buff=0.09)
    title = Text("Four videos, produced", color=PALETTE["ink"], font_size=fs)
    badge = Text("16:9 + 9:16", color=PALETTE["dim"], font_size=fs - 4)

    parts = [grid, fit(title, w - 0.3), badge]
    if tag:
        chip = card_bg(1.15, 0.38, stroke_color=PALETTE["good"])
        chip_lbl = Text(tag, color=PALETTE["good"], font_size=fs - 6)
        parts.append(VGroup(chip, chip_lbl.move_to(chip.get_center())))

    inner = VGroup(*parts).arrange(DOWN, buff=0.14)
    return VGroup(box, inner.move_to(box.get_center()))


def _meeting_card(w=3.4, h=1.9, fs=15, tag=None):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    cal = RoundedRectangle(corner_radius=0.05, width=0.7, height=0.58,
                            fill_color=PALETTE["bg"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=1.3)
    cal_top = Line(cal.get_corner(UL) + DOWN * 0.13, cal.get_corner(UR) + DOWN * 0.13,
                    color=PALETTE["dim"], stroke_width=1.3)
    dot = Dot(radius=0.04, color=PALETTE["accent"]).move_to(cal.get_center() + DOWN * 0.06)
    icon = VGroup(cal, cal_top, dot)

    title = Text("Team Meeting", color=PALETTE["ink"], font_size=fs)
    badge = Text("attended", color=PALETTE["dim"], font_size=fs - 4)

    parts = [icon, fit(title, w - 0.3), badge]
    if tag:
        chip = card_bg(1.15, 0.38, stroke_color=PALETTE["good"])
        chip_lbl = Text(tag, color=PALETTE["good"], font_size=fs - 6)
        parts.append(VGroup(chip, chip_lbl.move_to(chip.get_center())))

    inner = VGroup(*parts).arrange(DOWN, buff=0.14)
    return VGroup(box, inner.move_to(box.get_center()))


def _reveal_card(scene, card, run_time=0.55):
    box, inner = card[0], card[1]
    target_w = box.width
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), FadeIn(inner), run_time=run_time)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article_card()
        b = _video_card()
        c = _meeting_card()
        VGroup(a, b, c).arrange(DOWN, buff=0.28).move_to(UP * 0.1)

        _reveal_card(self, a)
        _reveal_card(self, b)
        _reveal_card(self, c)

        footer = fit(Text("no labels, no count yet", color=PALETTE["dim"], font_size=15))
        footer.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_TaggedWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text("This week: 3 things shipped", color=PALETTE["accent"],
                           font_size=19, weight="BOLD"))
        header.to_edge(UP, buff=0.75)
        self.play(FadeIn(header, shift=UP * 0.1), run_time=0.5)

        a = _article_card(w=3.2, h=1.75, fs=14, tag="Writing")
        b = _video_card(w=3.2, h=1.75, fs=14, tag="Video")
        c = _meeting_card(w=3.2, h=1.75, fs=14, tag="Meetings")
        VGroup(a, b, c).arrange(DOWN, buff=0.2).move_to(DOWN * 0.25)

        _reveal_card(self, a)
        _reveal_card(self, b)
        _reveal_card(self, c)
        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("Not everything I thought about.", color=PALETTE["ink"], font_size=22))
        l2 = fit(Text("Not everything I planned.", color=PALETTE["ink"], font_size=22))
        l3 = fit(Text("Just what shipped.", color=PALETTE["accent"], font_size=26))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.32).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
