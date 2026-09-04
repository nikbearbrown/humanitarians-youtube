"""
Portrait (9:16) Manim scenes for the weekly-recap Short.
Manim's coordinate frame for a 2160x3840 (9:16) render is ~4.5 units wide x
8 units tall (vs ~14.2 x 8 landscape) — everything here is laid out for that
narrow, tall canvas: single-column stacks instead of side-by-side rows.

B01_NotAHighlightReel — typographic reveal, single column
B04_FlatWeek           — three cards stacked in ONE column
B07_SplitWeek           — DONE / STARTING NEXT groups stacked vertically
B08_TheLesson           — three-line closing typographic beat

(No beats were dropped from this Short — the parent reel is only 1:59,
already under the 3:00 Shorts cap — so all 11 beats + endcard carry over.)
"""

from manim import *
import numpy as np

# Manim does NOT auto-derive the coordinate frame from -r's pixel resolution
# — this must be set explicitly; 4.5x8.0 matches manim_layout_audit.py's own
# --portrait GATE B check, so it's the house-standard portrait value.
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

        phrase = fit(Text("Not a highlight\nreel.", color=PALETTE["ink"],
                           font_size=32, line_spacing=1.2, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("A real log of\nthe week.", color=PALETTE["dim"],
                        font_size=18, line_spacing=1.25, should_center=True))

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.4, run_time=0.35)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.55)
        self.wait(1.3)


# ---------------------------------------------------------------------------
# Shared card builders — same three cards as the parent's scenes.py, resized
# for a narrow portrait column. Plain functions, not a shared base class.
# ---------------------------------------------------------------------------

def _article_card(w=3.2, h=2.0, fs=14):
    box = card_bg(w, h)
    kicker = Text("ARTICLE + RESEARCH", color=PALETTE["accent"], font_size=fs - 5)
    title = fit(Text("AI in nonprofit\nmarketing", color=PALETTE["ink"],
                      font_size=fs - 1, line_spacing=1.15, should_center=True), w - 0.5)
    inner = VGroup(kicker, title).arrange(DOWN, buff=0.16)
    return VGroup(box, inner.move_to(box.get_center()))


def _video_card(w=3.2, h=2.0, fs=14):
    box = card_bg(w, h)
    tri = Triangle(color=PALETTE["accent"], fill_color=PALETTE["accent"],
                    fill_opacity=1, stroke_width=0).scale(0.2).rotate(-PI / 2)
    ring = Circle(radius=0.3, color=PALETTE["accent"], stroke_width=2)
    icon = VGroup(ring, tri)
    title = Text("The video, produced", color=PALETTE["ink"], font_size=fs - 1)
    badge = Text("16:9 + 9:16", color=PALETTE["dim"], font_size=fs - 4)
    inner = VGroup(icon, title, badge).arrange(DOWN, buff=0.14)
    return VGroup(box, inner.move_to(box.get_center()))


def _suffolk_card(w=3.2, h=2.0, fs=14):
    box = card_bg(w, h)
    cal_body = RoundedRectangle(corner_radius=0.05, width=0.8, height=0.65,
                                 fill_color=PALETTE["bg"], fill_opacity=1,
                                 stroke_color=PALETTE["dim"], stroke_width=1.5)
    cal_head = RoundedRectangle(corner_radius=0.05, width=0.8, height=0.2,
                                 fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
    cal_head.next_to(cal_body, UP, buff=-0.1)
    cal = VGroup(cal_body, cal_head)
    title = Text("Suffolk University talk", color=PALETTE["ink"], font_size=fs - 1)
    badge = Text("Wed, with Yatra", color=PALETTE["dim"], font_size=fs - 4)
    inner = VGroup(cal, title, badge).arrange(DOWN, buff=0.14)
    return VGroup(box, inner.move_to(box.get_center()))


def _reveal_card(scene, card, target_w, run_time=0.6):
    box, inner = card[0], card[1]
    box.stretch(0.01, 0)
    scene.play(box.animate.stretch_to_fit_width(target_w), FadeIn(inner), run_time=run_time)


class B04_FlatWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        a = _article_card(h=1.7)
        b = _video_card(h=1.7)
        c = _suffolk_card(h=1.7)
        VGroup(a, b, c).arrange(DOWN, buff=0.16).move_to(ORIGIN + UP * 0.25)

        _reveal_card(self, a, 3.2, run_time=0.55)
        _reveal_card(self, b, 3.2, run_time=0.55)
        _reveal_card(self, c, 3.2, run_time=0.55)

        footer = fit(Text("Same weight. No sense of\nwhat's finished.", color=PALETTE["dim"],
                           font_size=15, line_spacing=1.2, should_center=True))
        footer.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.1)


class B07_SplitWeek(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        done_head = Text("DONE THIS WEEK", color=PALETTE["good"], font_size=17)
        next_head = Text("STARTING NEXT WEEK", color=PALETTE["accent"], font_size=17)

        a = _article_card(w=3.2, h=1.55, fs=12)
        b = _video_card(w=3.2, h=1.55, fs=12)
        c = _suffolk_card(w=3.2, h=1.75, fs=13)

        done_stack = VGroup(a, b).arrange(DOWN, buff=0.16)
        done_group = VGroup(done_head, done_stack).arrange(DOWN, buff=0.22)
        done_group.to_edge(UP, buff=0.75)

        next_group = VGroup(next_head, c).arrange(DOWN, buff=0.22)
        next_group.next_to(done_group, DOWN, buff=0.35)

        divider = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["border"], stroke_width=2)
        divider.move_to((np.array(done_group.get_bottom()) + np.array(next_group.get_top())) / 2)

        self.play(FadeIn(done_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, a, 3.2, run_time=0.5)
        _reveal_card(self, b, 3.2, run_time=0.5)

        grow_in(self, divider, divider.get_width(), run_time=0.4)

        self.play(FadeIn(next_head, shift=UP * 0.1), run_time=0.4)
        _reveal_card(self, c, 3.2, run_time=0.5)

        self.wait(1.2)


class B08_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("Done from next.", color=PALETTE["ink"], font_size=26))
        l2 = fit(Text("Not a small detail.", color=PALETTE["ink"], font_size=26))
        l3 = fit(Text("The whole difference.", color=PALETTE["accent"], font_size=26))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.55)
        self.wait(1.4)
