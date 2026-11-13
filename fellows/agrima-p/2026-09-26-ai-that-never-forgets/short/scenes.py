"""
Portrait (9:16) Manim scenes for the ai-that-never-forgets Short.

shorts.py's auto-plan dropped 2 beats (B02 what's changing, B04 the other
side) since the parent (3:49) is over the 3:00 Shorts cap. The 5 Manim
scenes that survive are relaid out here for a narrow, tall canvas
(~4.5 x 8 units vs ~14.2 x 8 landscape): single-column stacks and
scaled-down rows instead of the parent's wider side-by-side layouts,
generous to_edge() buffs (>=0.7) per this session's GATE B near-miss
lessons. B03 and B05 carry forward the same fixes applied to the parent
(dot-accented fragment cards so they register as real shapes; the Memory
panel's content sized via VGroup.arrange + derived panel height, not
manually-guessed offsets, to avoid the title/border collision bug found and
fixed in the parent build).

B00B_AgrimaIntro     — presenter card: "Hi, I'm Agrima." + topic lead-in
B01_TheOldSystem     — you -> cookie -> three site cards (retargeting)
B03_WhyItMatters     — three conversation fragments -> profile card + stat
B05_ResponsibleTools — Memory settings panel: View / Edit / Clear
B06_ClosingFraming   — quiet typographic closing beat: the tradeoff
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
            "For years, marketing\nworked by watching where\nyou clicked and guessing\n"
            "from there. That's starting\nto change -- now an AI\nassistant can actually\n"
            "remember what you tell it.",
            color=PALETTE["ink"], font_size=19, line_spacing=1.3, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.4, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


def _person_dot(r=0.14):
    return Circle(radius=r, color=PALETTE["ink"], fill_color=PALETTE["ink"],
                  fill_opacity=1, stroke_width=0)


def _site_card(label, w=1.05, h=1.0, fs=11):
    box = card_bg(w, h)
    shoe = RoundedRectangle(corner_radius=0.05, width=0.5, height=0.22,
                             fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    lbl = Text(label, color=PALETTE["dim"], font_size=fs)
    inner = VGroup(shoe, lbl).arrange(DOWN, buff=0.14)
    return VGroup(box, inner.move_to(box.get_center()))


class B01_TheOldSystem(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        you = _person_dot()
        you_lbl = Text("you", color=PALETTE["dim"], font_size=13).next_to(you, DOWN, buff=0.12)
        you_group = VGroup(you, you_lbl)

        cookie = card_bg(1.05, 0.6, stroke_color=PALETTE["accent"])
        cookie_lbl = Text("cookie", color=PALETTE["accent"], font_size=13)
        cookie_group = VGroup(cookie, cookie_lbl.move_to(cookie.get_center()))

        top_row = VGroup(you_group, cookie_group).arrange(RIGHT, buff=0.9)
        top_row.move_to(UP * 2.2)
        you_group.move_to(top_row[0].get_center())
        cookie_group.move_to(top_row[1].get_center())

        sites = VGroup(*[_site_card(lbl) for lbl in ["Instagram", "YouTube", "News Site"]])
        sites.arrange(RIGHT, buff=0.18).move_to(UP * 0.3)

        self.play(FadeIn(you_group, shift=RIGHT * 0.1), run_time=0.5)

        arrow1 = Arrow(you_group.get_right(), cookie_group.get_left(), color=PALETTE["dim"],
                       stroke_width=3, buff=0.12, max_tip_length_to_length_ratio=0.25)
        cookie_group[0].stretch(0.01, 0)
        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(cookie_group[0].animate.stretch_to_fit_width(1.05), FadeIn(cookie_group[1]), run_time=0.5)

        arrow2 = Arrow(cookie_group.get_bottom(), sites.get_top(), color=PALETTE["dim"],
                       stroke_width=3, buff=0.15, max_tip_length_to_length_ratio=0.2)
        self.play(GrowArrow(arrow2), run_time=0.4)

        for s in sites:
            s[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[s[0].animate.stretch_to_fit_width(1.05) for s in sites], lag_ratio=0.2),
            LaggedStart(*[FadeIn(s[1]) for s in sites], lag_ratio=0.2),
            run_time=1.0,
        )

        caption = fit(Text("the same shoes,\neverywhere you go", color=PALETTE["dim"],
                            font_size=15, line_spacing=1.25, should_center=True))
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B03_WhyItMatters(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        frags = ["training for a\nhalf marathon", "has flat feet", "tight budget"]
        frag_cards = VGroup()
        for f in frags:
            box = card_bg(1.05, 1.15, stroke_color=PALETTE["border"])
            dot = Dot(radius=0.045, color=PALETTE["accent"])
            lbl = fit(Text(f, color=PALETTE["dim"], font_size=11, line_spacing=1.15,
                            should_center=True), 0.95)
            tag = VGroup(dot, lbl).arrange(DOWN, buff=0.1)
            frag_cards.add(VGroup(box, tag.move_to(box.get_center())))
        frag_cards.arrange(RIGHT, buff=0.18).move_to(UP * 2.3)

        for c in frag_cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(1.05) for c in frag_cards], lag_ratio=0.2),
            LaggedStart(*[FadeIn(c[1]) for c in frag_cards], lag_ratio=0.2),
            run_time=1.0,
        )

        arrow = Arrow(UP * 1.55, UP * 1.05, color=PALETTE["dim"], stroke_width=3,
                      buff=0.05, max_tip_length_to_length_ratio=0.35)
        self.play(GrowArrow(arrow), run_time=0.4)

        profile = card_bg(3.4, 1.3, stroke_color=PALETTE["accent"])
        profile_dot = Dot(radius=0.05, color=PALETTE["accent"])
        profile_lbl = fit(Text("one assistant,\none real picture", color=PALETTE["ink"],
                                font_size=17, line_spacing=1.25, should_center=True), 2.9)
        profile_inner = VGroup(profile_dot, profile_lbl).arrange(DOWN, buff=0.18)
        profile_group = VGroup(profile, profile_inner.move_to(profile.get_center()))
        profile_group.move_to(UP * 0.35)

        profile.stretch(0.01, 0)
        self.play(profile.animate.stretch_to_fit_width(3.4), FadeIn(profile_inner), run_time=0.6)

        stat = fit(Text("~47 min/day saved vs.\nstarting over each time",
                         color=PALETTE["good"], font_size=15, line_spacing=1.25, should_center=True))
        stat.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B05_ResponsibleTools(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Memory", color=PALETTE["ink"], font_size=22, weight="BOLD")

        rows = ["View", "Edit", "Clear"]
        row_group = VGroup()
        for r in rows:
            btn = RoundedRectangle(corner_radius=0.09, width=2.9, height=0.5,
                                    fill_color=PALETTE["bg"], fill_opacity=1,
                                    stroke_color=PALETTE["accent"], stroke_width=1.5)
            lbl = Text(r, color=PALETTE["ink"], font_size=15)
            row_group.add(VGroup(btn, lbl.move_to(btn.get_center())))
        row_group.arrange(DOWN, buff=0.2)

        content = VGroup(title, row_group).arrange(DOWN, buff=0.4)
        panel = card_bg(3.5, content.height + 0.75, stroke_color=PALETTE["border"])
        content.move_to(panel.get_center())

        panel.stretch(0.01, 0)
        self.play(panel.animate.stretch_to_fit_width(3.5), FadeIn(title), run_time=0.6)

        for r in row_group:
            self.play(FadeIn(r, shift=UP * 0.08), run_time=0.3)

        caption = fit(Text("not a setting\nburied in menus", color=PALETTE["dim"],
                            font_size=15, line_spacing=1.25, should_center=True))
        caption.next_to(panel, DOWN, buff=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B06_ClosingFraming(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("A better\nrecommendation.", color=PALETTE["ink"], font_size=26,
                       line_spacing=1.2, should_center=True))
        l2 = fit(Text("A longer\nrecord of you.", color=PALETTE["ink"], font_size=26,
                       line_spacing=1.2, should_center=True))
        l3 = fit(Text("The difference\nis control.", color=PALETTE["accent"], font_size=26,
                       line_spacing=1.2, should_center=True))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
