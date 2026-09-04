"""
Manim scenes for weekly-recap

A first-person, honest weekly-progress CLI-explainer. The two OUTPUT beats
visualize the REAL output of weekly_recap_v1.py / weekly_recap_v2.py — no
invented numbers, no code/CLI content beyond what those two scripts actually
print. Built in the house Claude palette.

B01_NotAHighlightReel — typographic card: "Not a highlight reel."
B04_FlatWeek          — three same-weight cards: Article / Video / Suffolk talk
B07_SplitWeek         — same three cards, regrouped: DONE vs STARTING NEXT
B08_TheLesson         — closing typographic beat: the real lesson
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
        sub = Text("A real log of the week.", color=PALETTE["dim"], font_size=20)

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


# ---------------------------------------------------------------------------
# Shared card builders — reused, differently grouped, by B04 and B07.
# Plain functions, not a shared base class — run.sh discovers Manim scenes
# via a regex requiring each scene class to inherit directly from Scene.
# ---------------------------------------------------------------------------

def _article_card(w=2.6, h=3.2, fs=15):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    kicker = Text("ARTICLE + RESEARCH", color=PALETTE["accent"], font_size=fs - 4)
    lines = VGroup(*[
        Line(LEFT * (w * 0.32), RIGHT * (w * 0.32), color=PALETTE["border"], stroke_width=2)
        for _ in range(3)
    ]).arrange(DOWN, buff=0.14)
    title = Text("AI in nonprofit\nmarketing", color=PALETTE["ink"],
                  font_size=fs, line_spacing=1.2, should_center=True)
    inner = VGroup(kicker, title, lines).arrange(DOWN, buff=0.22)
    return VGroup(box, inner.move_to(box.get_center()))


def _video_card(w=2.6, h=3.2, fs=15):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                    fill_opacity=1, stroke_width=0).scale(0.28).rotate(-PI / 2)
    ring = Circle(radius=0.42, color=PALETTE["accent"], stroke_width=2.5)
    icon = VGroup(ring, tri)
    badge = Text("16:9 + 9:16", color=PALETTE["dim"], font_size=fs - 3)
    title = Text("The video,\nproduced", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True)
    inner = VGroup(icon, title, badge).arrange(DOWN, buff=0.22)
    return VGroup(box, inner.move_to(box.get_center()))


def _suffolk_card(w=2.6, h=3.2, fs=15):
    box = card_bg(w, h, stroke_color=PALETTE["border"])
    cal_body = RoundedRectangle(corner_radius=0.06, width=1.1, height=0.9,
                                 fill_color=PALETTE["bg"], fill_opacity=1,
                                 stroke_color=PALETTE["dim"], stroke_width=2)
    cal_head = RoundedRectangle(corner_radius=0.06, width=1.1, height=0.28,
                                 fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
    cal_head.next_to(cal_body, UP, buff=-0.14)
    cal = VGroup(cal_body, cal_head)
    title = Text("Suffolk\nUniversity talk", color=PALETTE["ink"], font_size=fs,
                  line_spacing=1.2, should_center=True)
    badge = Text("Wed, with Yatra", color=PALETTE["dim"], font_size=fs - 3)
    inner = VGroup(cal, title, badge).arrange(DOWN, buff=0.22)
    return VGroup(box, inner.move_to(box.get_center()))


def _reveal_card(scene, card, target_w, run_time=0.7):
    box, inner = card[0], card[1]
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), FadeIn(inner), run_time=run_time)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article_card()
        b = _video_card()
        c = _suffolk_card()
        row = VGroup(a, b, c).arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        _reveal_card(self, a, 2.6, run_time=0.6)
        _reveal_card(self, b, 2.6, run_time=0.6)
        _reveal_card(self, c, 2.6, run_time=0.6)

        footer = Text("Same weight. No sense of what's finished.", color=PALETTE["dim"],
                       font_size=17).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_SplitWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        done_head = Text("DONE THIS WEEK", color=PALETTE["good"], font_size=20)
        next_head = Text("STARTING NEXT WEEK", color=PALETTE["accent"], font_size=20)

        a = _article_card(w=2.2, h=2.7, fs=13)
        b = _video_card(w=2.2, h=2.7, fs=13)
        c = _suffolk_card(w=2.4, h=3.0, fs=14)

        done_row = VGroup(a, b).arrange(RIGHT, buff=0.35)
        done_col = VGroup(done_head, done_row).arrange(DOWN, buff=0.35)
        done_col.move_to(LEFT * 3.2)

        next_col = VGroup(next_head, c).arrange(DOWN, buff=0.35)
        next_col.move_to(RIGHT * 3.6)

        divider = Line(UP * 2.2, DOWN * 2.2, color=PALETTE["border"], stroke_width=2)
        divider.move_to((np.array(done_col.get_right()) + np.array(next_col.get_left())) / 2)

        self.play(FadeIn(done_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, a, 2.2, run_time=0.5)
        _reveal_card(self, b, 2.2, run_time=0.5)

        grow_in(self, divider, divider.get_height(), run_time=0.4)

        self.play(FadeIn(next_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, c, 2.4, run_time=0.5)

        self.wait(1.3)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("Done from next.", color=PALETTE["ink"], font_size=32)
        l2 = Text("Not a small detail.", color=PALETTE["ink"], font_size=32)
        l3 = Text("The whole difference.", color=PALETTE["accent"], font_size=32)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
