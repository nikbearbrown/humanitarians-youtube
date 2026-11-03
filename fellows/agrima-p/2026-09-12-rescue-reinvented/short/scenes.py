"""
Portrait (9:16) Manim scenes for the rescue-reinvented Short.
Manim's coordinate frame for a 2160x3840 (9:16) render is ~4.5 units wide x
8 units tall (vs ~14.2 x 8 landscape) — everything here is laid out for that
narrow, tall canvas: single-column stacks instead of side-by-side rows,
generous to_edge() buffs (>=0.7) learned from GATE B near-misses on prior
builds this session.

B00B_AgrimaIntro    — presenter card: "Hi, I'm Agrima." + lead-in
B01_TheBackdrop     — 2x2 grid of strain-point cards, narrower
B02_LostPetMatch    — lost/found photo-match graphic, stacked vertically
B04_CoordinationHub — central card + three tags, stacked as a single flow
B06_NotSmarterAI    — reframe card, vertical stack

(B03/B05 were dropped from this Short by shorts.py's auto-plan — the
parent reel is 3:57, over the 3:00 Shorts cap — so those two scenes have
no portrait counterpart here; the rewritten B08 outro points viewers to
the long for the material those two beats covered.)
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


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=32)
        summary = fit(Text(
            "I want to talk about\nsomething I looked into\nrecently — how AI is\n"
            "actually showing up in\nanimal rescue work.",
            color=PALETTE["ink"], font_size=20, line_spacing=1.35, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.6)
        grow_in(self, rule, 1.4, run_time=0.35)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.2)


def _strain_card(label, w=1.6, h=1.5, fs=12):
    box = card_bg(w, h)
    txt = fit(Text(label, color=PALETTE["ink"], font_size=fs,
                    line_spacing=1.2, should_center=True), w - 0.3)
    return VGroup(box, txt.move_to(box.get_center()))


class B01_TheBackdrop(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("The backdrop.", color=PALETTE["dim"],
                      font_size=20).to_edge(UP, buff=0.75)
        self.play(FadeIn(title), run_time=0.5)

        labels = ["Overcrowded\nkennels", "Staffing\nshortages",
                  "Hard-to-recruit\nvolunteers", "Donations that\nlag behind need"]
        cards = VGroup(*[_strain_card(lbl) for lbl in labels])
        cards.arrange_in_grid(rows=2, cols=2, buff=0.35).move_to(ORIGIN)

        for c in cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(1.6) for c in cards], lag_ratio=0.15),
            LaggedStart(*[FadeIn(c[1]) for c in cards], lag_ratio=0.15),
            run_time=1.2,
        )
        self.wait(1.2)


def _photo_card(label, w=2.6, h=2.0, fs=15):
    box = card_bg(w, h)
    frame = RoundedRectangle(corner_radius=0.08, width=w - 0.7, height=h - 0.8,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["border"], stroke_width=2)
    head = Ellipse(width=0.7, height=0.58, fill_color=PALETTE["dim"],
                    fill_opacity=1, stroke_width=0)
    ear1 = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.17)
    ear1.move_to(head.get_center() + UP * 0.33 + LEFT * 0.22)
    ear2 = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.17)
    ear2.move_to(head.get_center() + UP * 0.33 + RIGHT * 0.22)
    silhouette = VGroup(ear1, ear2, head).move_to(frame.get_center())
    kicker = Text(label, color=PALETTE["accent"], font_size=fs - 1)
    inner = VGroup(kicker, VGroup(frame, silhouette)).arrange(DOWN, buff=0.16)
    return VGroup(box, inner.move_to(box.get_center()))


class B02_LostPetMatch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lost = _photo_card("LOST")
        found = _photo_card("FOUND")
        col = VGroup(lost, found).arrange(DOWN, buff=0.45).move_to(UP * 0.15)

        lost[0].stretch(0.01, 0)
        self.play(lost[0].animate.stretch_to_fit_width(2.6), FadeIn(lost[1]), run_time=0.55)
        found[0].stretch(0.01, 0)
        self.play(found[0].animate.stretch_to_fit_width(2.6), FadeIn(found[1]), run_time=0.55)

        badge = Circle(radius=0.3, color=PALETTE["good"], fill_color=PALETTE["good"],
                        fill_opacity=1, stroke_width=0)
        check = Text("✓", color=PALETTE["card"], font_size=24)
        match = VGroup(badge, check.move_to(badge.get_center()))
        match.move_to((np.array(lost.get_bottom()) + np.array(found.get_top())) / 2)
        self.play(FadeIn(match, scale=0.5), run_time=0.4)

        stat = fit(Text("Recovery rates: up to +25%", color=PALETTE["accent"], font_size=19))
        stat.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.55)
        self.wait(1.2)


class B04_CoordinationHub(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        center = card_bg(2.8, 1.2)
        center_txt = Text("Coordination", color=PALETTE["ink"], font_size=19)
        center_g = VGroup(center, center_txt.move_to(center.get_center()))

        tags_labels = ["Foster placements", "Volunteer schedules", "Transport relays"]
        tags = VGroup()
        for lbl in tags_labels:
            box = card_bg(2.8, 0.9)
            txt = fit(Text(lbl, color=PALETTE["accent"], font_size=15), 2.4)
            tags.add(VGroup(box, txt.move_to(box.get_center())))

        flow = VGroup(center_g, *tags).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        center.stretch(0.01, 0)
        self.play(center.animate.stretch_to_fit_width(2.8), FadeIn(center_txt), run_time=0.55)

        prev = center_g
        for tag in tags:
            ln = Line(prev.get_bottom() + DOWN * 0.04, tag.get_top() + UP * 0.04,
                      color=PALETTE["border"], stroke_width=2)
            ln_h = ln.get_height()
            ln.stretch(0.01, 1)
            self.play(ln.animate.stretch_to_fit_height(ln_h), run_time=0.25)
            box = tag[0]
            box.stretch(0.01, 0)
            self.play(box.animate.stretch_to_fit_width(2.8), FadeIn(tag[1]), run_time=0.35)
            prev = tag

        footer = fit(Text("Small teams, genuinely manageable.", color=PALETTE["dim"], font_size=15))
        footer.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.1)


class B06_NotSmarterAI(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(Text("Not smarter AI.", color=PALETTE["ink"], font_size=30))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("Wider adoption of what\nalready works.", color=PALETTE["dim"],
                        font_size=18, line_spacing=1.25, should_center=True))

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.4, run_time=0.35)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.55)
        self.wait(1.3)
