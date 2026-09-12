"""
Manim scenes for rescue-reinvented

A first-person, professional-but-optimistic explainer on how AI is helping
animal shelters, sourced from the user-supplied article "Rescue, Reinvented:
How Artificial Intelligence Is Reshaping Rescue Work." No code/CLI content —
every body beat is a from-scratch typographic or diagram visual, built in
the house Claude palette.

B00B_AgrimaIntro     — presenter card: "Hi, I'm Agrima." + topic lead-in
B01_TheBackdrop      — 2x2 grid: the four strain points shelters operate under
B02_LostPetMatch     — lost/found pet photo-match graphic + recovery stat
B03_NotesToContent   — one input card fanning into three output cards
B04_CoordinationHub  — central "Coordination" card + three fanned tags
B05_HonestNumbers    — two-stat contrast: real progress vs. real gap
B06_NotSmarterAI     — reframe: wider adoption, not smarter AI
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
    """Genuine shape-state change (GATE A) — a box/line grows into place
    rather than just fading, mirroring the pattern used across this
    project's other reels."""
    mob.stretch(0.01, 0)
    scene.play(mob.animate.stretch_to_fit_width(target_width), run_time=run_time, **kwargs)


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = Text(
            "I want to talk about something\nI looked into recently — how AI is\n"
            "actually showing up in animal rescue\nwork, and where it's making a\nreal difference.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.35, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.wait(1.3)


def _strain_card(label, w=3.0, h=1.5, fs=17):
    box = card_bg(w, h)
    txt = Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.2, should_center=True)
    return VGroup(box, txt.move_to(box.get_center()))


class B01_TheBackdrop(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("The backdrop.", color=PALETTE["dim"],
                      font_size=22).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.5)

        labels = ["Overcrowded\nkennels", "Staffing\nshortages",
                  "Hard-to-recruit\nvolunteers", "Donations that\nlag behind need"]
        cards = VGroup(*[_strain_card(lbl) for lbl in labels])
        cards.arrange_in_grid(rows=2, cols=2, buff=0.5).move_to(DOWN * 0.2)

        for c in cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(3.0) for c in cards], lag_ratio=0.15),
            LaggedStart(*[FadeIn(c[1]) for c in cards], lag_ratio=0.15),
            run_time=1.3,
        )
        self.wait(1.2)


def _photo_card(label, w=2.8, h=3.0, fs=18):
    box = card_bg(w, h)
    frame = RoundedRectangle(corner_radius=0.08, width=w - 0.6, height=h - 1.2,
                              fill_color=PALETTE["bg"], fill_opacity=1,
                              stroke_color=PALETTE["border"], stroke_width=2)
    # simple pet-silhouette: an ellipse head + two triangle ears
    head = Ellipse(width=0.9, height=0.75, fill_color=PALETTE["dim"],
                    fill_opacity=1, stroke_width=0)
    ear1 = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.22)
    ear1.move_to(head.get_center() + UP * 0.42 + LEFT * 0.28)
    ear2 = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.22)
    ear2.move_to(head.get_center() + UP * 0.42 + RIGHT * 0.28)
    silhouette = VGroup(ear1, ear2, head).move_to(frame.get_center())
    kicker = Text(label, color=PALETTE["accent"], font_size=fs - 2)
    inner = VGroup(kicker, VGroup(frame, silhouette)).arrange(DOWN, buff=0.2)
    return VGroup(box, inner.move_to(box.get_center()))


class B02_LostPetMatch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lost = _photo_card("LOST")
        found = _photo_card("FOUND")
        row = VGroup(lost, found).arrange(RIGHT, buff=1.0).move_to(UP * 0.3)

        lost[0].stretch(0.01, 0)
        self.play(lost[0].animate.stretch_to_fit_width(2.8), FadeIn(lost[1]), run_time=0.6)
        found[0].stretch(0.01, 0)
        self.play(found[0].animate.stretch_to_fit_width(2.8), FadeIn(found[1]), run_time=0.6)

        badge = Circle(radius=0.35, color=PALETTE["good"], fill_color=PALETTE["good"],
                        fill_opacity=1, stroke_width=0)
        check = Text("✓", color=PALETTE["card"], font_size=28)
        match = VGroup(badge, check.move_to(badge.get_center()))
        match.move_to((np.array(lost.get_right()) + np.array(found.get_left())) / 2)
        self.play(FadeIn(match, scale=0.5), run_time=0.4)

        stat = Text("Recovery rates: up to +25%", color=PALETTE["accent"],
                     font_size=24).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


def _content_card(label, w=2.0, h=2.6, fs=15):
    box = card_bg(w, h)
    txt = Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.2, should_center=True)
    return VGroup(box, txt.move_to(box.get_center()))


class B03_NotesToContent(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        base = card_bg(2.6, 3.2)
        base_txt = Text("Rushed\nnotes", color=PALETTE["ink"], font_size=20,
                         line_spacing=1.2, should_center=True)
        base_card = VGroup(base, base_txt.move_to(base.get_center()))
        base_card.move_to(LEFT * 3.6)
        base.stretch(0.01, 0)
        self.play(base.animate.stretch_to_fit_width(2.6), FadeIn(base_txt), run_time=0.6)

        outs = ["Adoption\npost", "Social\ncaption", "Donor\nupdate"]
        cards = VGroup(*[_content_card(lbl) for lbl in outs])
        positions = [RIGHT * 1.6 + UP * 1.5, RIGHT * 2.5, RIGHT * 1.6 + DOWN * 1.5]
        for c, pos in zip(cards, positions):
            c.move_to(pos)

        for c in cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(2.0) for c in cards], lag_ratio=0.2),
            LaggedStart(*[FadeIn(c[1]) for c in cards], lag_ratio=0.2),
            run_time=1.2,
        )

        footer = Text("One set of notes. Three finished pieces.", color=PALETTE["dim"],
                       font_size=17).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.1)


class B04_CoordinationHub(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        center = card_bg(3.2, 1.6)
        center_txt = Text("Coordination", color=PALETTE["ink"], font_size=22)
        center_g = VGroup(center, center_txt.move_to(center.get_center()))
        center.stretch(0.01, 0)
        self.play(center.animate.stretch_to_fit_width(3.2), FadeIn(center_txt), run_time=0.6)

        tags_labels = ["Foster\nplacements", "Volunteer\nschedules", "Transport\nrelays"]
        positions = [UP * 2.2 + LEFT * 3.6, UP * 2.2 + RIGHT * 3.6, DOWN * 2.2]
        center_pt = np.array(center_g.get_center())
        CENTER_CLEAR = 1.9
        TAG_CLEAR = 1.2

        tags = VGroup()
        lines = VGroup()
        for lbl, pos in zip(tags_labels, positions):
            tag_box = card_bg(2.4, 1.0)
            tag_txt = Text(lbl, color=PALETTE["accent"], font_size=16,
                            line_spacing=1.15, should_center=True)
            tag = VGroup(tag_box, tag_txt.move_to(tag_box.get_center())).move_to(pos)
            tags.add(tag)

            direction = (np.array(pos) - center_pt)
            direction = direction / np.linalg.norm(direction)
            start_pt = center_pt + direction * CENTER_CLEAR
            end_pt = np.array(pos) - direction * TAG_CLEAR
            ln = Line(start_pt, end_pt, color=PALETTE["border"], stroke_width=2)
            lines.add(ln)

        for ln, tag in zip(lines, tags):
            ln_target = ln.copy()
            ln.scale(0.01)
            box = tag[0]
            box.stretch(0.01, 0)
            self.play(Transform(ln, ln_target), run_time=0.25)
            self.play(box.animate.stretch_to_fit_width(2.4), FadeIn(tag[1]), run_time=0.35)

        footer = Text("Small teams, genuinely manageable.", color=PALETTE["dim"],
                       font_size=17).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B05_HonestNumbers(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        s1_num = Text("4.2M", color=PALETTE["good"], font_size=52)
        s1_lbl = Text("shelter animals adopted in 2025", color=PALETTE["ink"], font_size=20)
        s1 = VGroup(s1_num, s1_lbl).arrange(DOWN, buff=0.2)

        s2_num = Text("Still stretched thin", color=PALETTE["miss"], font_size=34)
        s2_lbl = Text("shelter capacity, nationally", color=PALETTE["ink"], font_size=20)
        s2 = VGroup(s2_num, s2_lbl).arrange(DOWN, buff=0.2)

        VGroup(s1, s2).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        self.play(FadeIn(s1, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(s2, shift=UP * 0.15), run_time=0.7)
        self.wait(1.3)


class B06_NotSmarterAI(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("Not smarter AI.", color=PALETTE["ink"], font_size=38)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = Text("Wider adoption of what already works.", color=PALETTE["dim"], font_size=19)

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)
