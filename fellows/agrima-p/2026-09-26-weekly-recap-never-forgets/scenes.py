"""
Manim scenes for weekly-recap-never-forgets

A first-person, honest weekly-progress CLI-explainer documenting this
specific week's work. The two OUTPUT beats visualize the REAL output of
weekly_recap_v1.py / weekly_recap_v2.py -- no invented numbers, no code/CLI
content beyond what those two scripts actually print. Built in the house
Claude palette.

B01_NotAHighlightReel — typographic card: "Not a highlight reel."
B04_FlatWeek          — three same-weight cards: Article / 4 Videos / Meeting
B07_TaggedWeek        — same three cards, now tagged by category + a count
B08_TheLesson         — closing typographic beat: what actually shipped
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


class B01_NotAHighlightReel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("Not a highlight reel.", color=PALETTE["ink"], font_size=40)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = Text("A flat log of what shipped.", color=PALETTE["dim"], font_size=20)

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


# ---------------------------------------------------------------------------
# Shared card builders — reused, differently tagged, by B04 and B07.
# ---------------------------------------------------------------------------

def _article_card(w=2.6, h=3.2, fs=15, tag=None, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    dots = VGroup(*[
        Circle(radius=0.045, color=PALETTE["border"], fill_color=PALETTE["border"],
               fill_opacity=1, stroke_width=0)
        for _ in range(3)
    ]).arrange(RIGHT, buff=0.09)
    header_rule = Line(LEFT * (w * 0.32), RIGHT * (w * 0.32),
                        color=PALETTE["border"], stroke_width=1.5)
    header = VGroup(dots, header_rule).arrange(DOWN, buff=0.1)

    kicker = Text("SUBSTACK · ARTICLE", color=PALETTE["accent"], font_size=fs - 4)
    title = Text("The AI That\nNever Forgets", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True, weight="BOLD")
    byline = Text("memory, marketing, privacy", color=PALETTE["dim"], font_size=fs - 4)

    parts = [header, kicker, title, byline]
    if tag:
        chip = card_bg(1.3, 0.4, stroke_color=PALETTE["good"])
        chip_lbl = Text(tag, color=PALETTE["good"], font_size=fs - 5)
        chip_group = VGroup(chip, chip_lbl.move_to(chip.get_center()))
        parts.append(chip_group)

    inner = VGroup(*parts).arrange(DOWN, buff=0.22)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _video_card(w=2.6, h=3.2, fs=15, tag=None, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    def mini_frame():
        f = RoundedRectangle(corner_radius=0.04, width=0.55, height=0.4,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["dim"], stroke_width=1.5)
        tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                        fill_opacity=1, stroke_width=0).scale(0.06).rotate(-PI / 2)
        tri.move_to(f.get_center())
        return VGroup(f, tri)

    grid = VGroup(*[mini_frame() for _ in range(4)]).arrange_in_grid(rows=2, cols=2, buff=0.12)

    badge = Text("16:9 + 9:16", color=PALETTE["dim"], font_size=fs - 3)
    title = Text("Four videos,\nproduced", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True)

    parts = [grid, title, badge]
    if tag:
        chip = card_bg(1.3, 0.4, stroke_color=PALETTE["good"])
        chip_lbl = Text(tag, color=PALETTE["good"], font_size=fs - 5)
        chip_group = VGroup(chip, chip_lbl.move_to(chip.get_center()))
        parts.append(chip_group)

    inner = VGroup(*parts).arrange(DOWN, buff=0.22)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _meeting_card(w=2.6, h=3.2, fs=15, tag=None, scale=1.0):
    box = card_bg(w, h, stroke_color=PALETTE["border"])

    cal = RoundedRectangle(corner_radius=0.06, width=0.9, height=0.75,
                            fill_color=PALETTE["bg"], fill_opacity=1,
                            stroke_color=PALETTE["dim"], stroke_width=1.5)
    cal_top = Line(cal.get_corner(UL) + DOWN * 0.16, cal.get_corner(UR) + DOWN * 0.16,
                    color=PALETTE["dim"], stroke_width=1.5)
    tab_l = Line(UP * 0.08, DOWN * 0.06, color=PALETTE["dim"], stroke_width=2)
    tab_l.move_to(cal.get_corner(UL) + RIGHT * 0.18 + UP * 0.02)
    tab_r = tab_l.copy().move_to(cal.get_corner(UR) + LEFT * 0.18 + UP * 0.02)
    dot = Dot(radius=0.05, color=PALETTE["accent"]).move_to(cal.get_center() + DOWN * 0.08)
    icon = VGroup(cal, cal_top, tab_l, tab_r, dot)

    badge = Text("attended", color=PALETTE["dim"], font_size=fs - 3)
    title = Text("Team\nMeeting", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True)

    parts = [icon, title, badge]
    if tag:
        chip = card_bg(1.3, 0.4, stroke_color=PALETTE["good"])
        chip_lbl = Text(tag, color=PALETTE["good"], font_size=fs - 5)
        chip_group = VGroup(chip, chip_lbl.move_to(chip.get_center()))
        parts.append(chip_group)

    inner = VGroup(*parts).arrange(DOWN, buff=0.22)
    card = VGroup(box, inner.move_to(box.get_center()))
    if scale != 1.0:
        card.scale(scale)
    return card


def _reveal_card(scene, card, run_time=0.7):
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
        row = VGroup(a, b, c).arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        _reveal_card(self, a, run_time=0.6)
        _reveal_card(self, b, run_time=0.6)
        _reveal_card(self, c, run_time=0.6)

        footer = Text("no labels, no count yet — just the list", color=PALETTE["dim"],
                       font_size=17).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_TaggedWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = Text("This week: 3 things shipped", color=PALETTE["accent"],
                       font_size=22, weight="BOLD").to_edge(UP, buff=0.85)
        self.play(FadeIn(header, shift=UP * 0.1), run_time=0.5)

        a = _article_card(w=2.4, h=3.0, fs=14, tag="Writing")
        b = _video_card(w=2.4, h=3.0, fs=14, tag="Video")
        c = _meeting_card(w=2.4, h=3.0, fs=14, tag="Meetings")
        row = VGroup(a, b, c).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.3)

        _reveal_card(self, a, run_time=0.55)
        _reveal_card(self, b, run_time=0.55)
        _reveal_card(self, c, run_time=0.55)
        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("Not everything I thought about.", color=PALETTE["ink"], font_size=28)
        l2 = Text("Not everything I planned.", color=PALETTE["ink"], font_size=28)
        l3 = Text("Just what shipped.", color=PALETTE["accent"], font_size=32)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
