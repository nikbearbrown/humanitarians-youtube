"""
Manim scenes for ai-that-never-forgets

A neutral, observational explainer on AI persistent memory and what it means
for marketing personalization, sourced from the user-supplied article "The AI
That Never Forgets: How Marketing Is Learning to Read Your Mind, One
Conversation at a Time." Built in the house Claude palette. No dedicated
footage exists for this topic (per the user's own materials note) -- every
visual below is a generated Manim graphic, not stock footage or a screen
recording.

B00B_AgrimaIntro     -- presenter card: "Hi, I'm Agrima." + topic lead-in
B01_TheOldSystem     -- cookie/retargeting mechanic: click -> cookie -> follows you
B02_WhatsChanging    -- old-vs-new split card + Gemini/ChatGPT + market stat
B03_WhyItMatters     -- conversation fragments assembling into a profile + stat
B04_TheOtherSide     -- personalization model vs identity model + open questions
B05_ResponsibleTools -- memory settings panel: View / Edit / Clear
B06_ClosingFraming   -- quiet typographic closing beat: the real tradeoff
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


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = Text(
            "For years, marketing worked\nby watching where you clicked\n"
            "and guessing from there. That's\nstarting to change -- now an AI\n"
            "assistant can actually remember\nwhat you tell it.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.3, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


def _person_dot(r=0.16):
    return Circle(radius=r, color=PALETTE["ink"], fill_color=PALETTE["ink"],
                  fill_opacity=1, stroke_width=0)


def _site_card(label, w=1.7, h=1.3, fs=14):
    box = card_bg(w, h)
    shoe = RoundedRectangle(corner_radius=0.06, width=0.7, height=0.3,
                             fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
    lbl = Text(label, color=PALETTE["dim"], font_size=fs)
    inner = VGroup(shoe, lbl).arrange(DOWN, buff=0.18)
    return VGroup(box, inner.move_to(box.get_center()))


class B01_TheOldSystem(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        you = _person_dot()
        you_lbl = Text("you", color=PALETTE["dim"], font_size=15).next_to(you, DOWN, buff=0.15)
        you_group = VGroup(you, you_lbl).move_to(LEFT * 5.0 + UP * 0.5)

        cookie = card_bg(1.3, 0.7, stroke_color=PALETTE["accent"])
        cookie_lbl = Text("cookie", color=PALETTE["accent"], font_size=15)
        cookie_group = VGroup(cookie, cookie_lbl.move_to(cookie.get_center()))
        cookie_group.move_to(LEFT * 2.3 + UP * 0.5)

        sites = VGroup(*[_site_card(lbl) for lbl in ["Instagram", "YouTube", "News Site"]])
        sites.arrange(RIGHT, buff=0.35).move_to(RIGHT * 2.3 + UP * 0.5)

        self.play(FadeIn(you_group, shift=RIGHT * 0.1), run_time=0.5)

        arrow1 = Arrow(you_group.get_right(), cookie_group.get_left(), color=PALETTE["dim"],
                       stroke_width=3, buff=0.15, max_tip_length_to_length_ratio=0.2)
        cookie_group[0].stretch(0.01, 0)
        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(cookie_group[0].animate.stretch_to_fit_width(1.3), FadeIn(cookie_group[1]), run_time=0.5)

        arrow2 = Arrow(cookie_group.get_right(), sites.get_left(), color=PALETTE["dim"],
                       stroke_width=3, buff=0.15, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(arrow2), run_time=0.4)

        for s in sites:
            s[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[s[0].animate.stretch_to_fit_width(1.7) for s in sites], lag_ratio=0.2),
            LaggedStart(*[FadeIn(s[1]) for s in sites], lag_ratio=0.2),
            run_time=1.0,
        )

        caption = Text("the same shoes, everywhere you go", color=PALETTE["dim"], font_size=17)
        caption.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


def _mini_card(icon_mob, label, w=2.6, h=1.9, fs=16, border=None):
    box = card_bg(w, h, stroke_color=border)
    lbl = Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.2, should_center=True)
    inner = VGroup(icon_mob, lbl).arrange(DOWN, buff=0.28)
    return VGroup(box, inner.move_to(box.get_center()))


class B02_WhatsChanging(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        cursor = Triangle(fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0).scale(0.22).rotate(-PI / 6)
        old_card = _mini_card(cursor, "guesses from\nwhat you clicked", border=PALETTE["border"])

        bubble = RoundedRectangle(corner_radius=0.15, width=0.7, height=0.45,
                                   fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        tail = Triangle(fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        tail.scale(0.09).rotate(PI).next_to(bubble, DOWN, buff=-0.03).shift(LEFT * 0.22)
        bubble_icon = VGroup(bubble, tail)
        new_card = _mini_card(bubble_icon, "remembers what\nyou actually said", border=PALETTE["accent"])

        row = VGroup(old_card, new_card).arrange(RIGHT, buff=0.6).move_to(UP * 0.9)

        old_card[0].stretch(0.01, 0)
        new_card[0].stretch(0.01, 0)
        self.play(old_card[0].animate.stretch_to_fit_width(2.6), FadeIn(old_card[1]), run_time=0.6)
        self.play(new_card[0].animate.stretch_to_fit_width(2.6), FadeIn(new_card[1]), run_time=0.6)

        arrow = Arrow(old_card.get_right(), new_card.get_left(), color=PALETTE["dim"],
                      stroke_width=3, buff=0.1, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(arrow), run_time=0.4)

        chip1 = card_bg(1.7, 0.55, stroke_color=PALETTE["border"])
        chip1_lbl = Text("Gemini", color=PALETTE["ink"], font_size=16)
        chip1_group = VGroup(chip1, chip1_lbl.move_to(chip1.get_center()))

        chip2 = card_bg(1.9, 0.55, stroke_color=PALETTE["border"])
        chip2_lbl = Text("ChatGPT", color=PALETTE["ink"], font_size=16)
        chip2_group = VGroup(chip2, chip2_lbl.move_to(chip2.get_center()))

        chips = VGroup(chip1_group, chip2_group).arrange(RIGHT, buff=0.4)
        chips.next_to(row, DOWN, buff=0.5)

        for c in (chip1_group, chip2_group):
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(
                chip1_group[0].animate.stretch_to_fit_width(1.7),
                chip2_group[0].animate.stretch_to_fit_width(1.9),
                lag_ratio=0.25,
            ),
            LaggedStart(FadeIn(chip1_group[1]), FadeIn(chip2_group[1]), lag_ratio=0.25),
            run_time=0.8,
        )

        stat = Text("~$5B now -> nearly 4x by 2030", color=PALETTE["accent"], font_size=18, weight="BOLD")
        stat.next_to(chips, DOWN, buff=0.5)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B03_WhyItMatters(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        frags = ["training for a\nhalf marathon", "has flat feet", "tight budget"]
        frag_cards = VGroup()
        for f in frags:
            box = card_bg(2.1, 1.15, stroke_color=PALETTE["border"])
            dot = Dot(radius=0.05, color=PALETTE["accent"])
            lbl = Text(f, color=PALETTE["dim"], font_size=14, line_spacing=1.15, should_center=True)
            tag = VGroup(dot, lbl).arrange(DOWN, buff=0.12)
            frag_cards.add(VGroup(box, tag.move_to(box.get_center())))
        frag_cards.arrange(RIGHT, buff=0.3).move_to(UP * 1.1)

        for c in frag_cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(2.1) for c in frag_cards], lag_ratio=0.2),
            LaggedStart(*[FadeIn(c[1]) for c in frag_cards], lag_ratio=0.2),
            run_time=1.0,
        )

        arrow = Arrow(UP * 0.35, DOWN * 0.15, color=PALETTE["dim"], stroke_width=3,
                      buff=0.05, max_tip_length_to_length_ratio=0.35)
        arrow.move_to(DOWN * 0.15)
        self.play(GrowArrow(arrow), run_time=0.4)

        profile = card_bg(4.6, 1.1, stroke_color=PALETTE["accent"])
        profile_dot = Dot(radius=0.06, color=PALETTE["accent"])
        profile_lbl = Text("one assistant, one real picture", color=PALETTE["ink"], font_size=18)
        profile_inner = VGroup(profile_dot, profile_lbl).arrange(RIGHT, buff=0.2)
        profile_group = VGroup(profile, profile_inner.move_to(profile.get_center()))
        profile_group.move_to(DOWN * 0.9)

        profile.stretch(0.01, 0)
        self.play(profile.animate.stretch_to_fit_width(4.6), FadeIn(profile_inner), run_time=0.6)

        stat = Text("~47 min/day saved vs. starting over each time", color=PALETTE["good"], font_size=16)
        stat.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


def _model_card(title, sub, w=2.9, h=2.3, border=None):
    box = card_bg(w, h, stroke_color=border)
    title_txt = Text(title, color=PALETTE["ink"], font_size=18, weight="BOLD")
    sub_txt = Text(sub, color=PALETTE["dim"], font_size=14, line_spacing=1.2, should_center=True)
    inner = VGroup(title_txt, sub_txt).arrange(DOWN, buff=0.3)
    return VGroup(box, inner.move_to(box.get_center()))


class B04_TheOtherSide(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        left = _model_card("PERSONALIZATION", "based on\nwhat you clicked", border=PALETTE["border"])
        right = _model_card("IDENTITY MODEL", "based on\nwho you are", border=PALETTE["miss"])
        row = VGroup(left, right).arrange(RIGHT, buff=0.55).move_to(UP * 0.7)

        left[0].stretch(0.01, 0)
        right[0].stretch(0.01, 0)
        self.play(left[0].animate.stretch_to_fit_width(2.9), FadeIn(left[1]), run_time=0.6)
        self.play(right[0].animate.stretch_to_fit_width(2.9), FadeIn(right[1]), run_time=0.6)

        questions = ["Who sees it?", "Can it be corrected?", "Can it be deleted?"]
        q_chips = VGroup()
        for q in questions:
            chip = card_bg(2.35, 0.6, stroke_color=PALETTE["border"])
            lbl = Text(q, color=PALETTE["dim"], font_size=15)
            q_chips.add(VGroup(chip, lbl.move_to(chip.get_center())))
        q_chips.arrange(RIGHT, buff=0.25)
        q_chips.next_to(row, DOWN, buff=0.6)

        for c in q_chips:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(2.35) for c in q_chips], lag_ratio=0.2),
            LaggedStart(*[FadeIn(c[1]) for c in q_chips], lag_ratio=0.2),
            run_time=1.0,
        )
        self.wait(1.3)


class B05_ResponsibleTools(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Memory", color=PALETTE["ink"], font_size=22, weight="BOLD")

        rows = ["View", "Edit", "Clear"]
        row_group = VGroup()
        for r in rows:
            btn = RoundedRectangle(corner_radius=0.1, width=3.6, height=0.55,
                                    fill_color=PALETTE["bg"], fill_opacity=1,
                                    stroke_color=PALETTE["accent"], stroke_width=1.5)
            lbl = Text(r, color=PALETTE["ink"], font_size=16)
            row_group.add(VGroup(btn, lbl.move_to(btn.get_center())))
        row_group.arrange(DOWN, buff=0.22)

        content = VGroup(title, row_group).arrange(DOWN, buff=0.4)
        panel = card_bg(4.6, content.height + 0.8, stroke_color=PALETTE["border"])
        content.move_to(panel.get_center())

        panel.stretch(0.01, 0)
        self.play(panel.animate.stretch_to_fit_width(4.6), FadeIn(title), run_time=0.6)

        for r in row_group:
            self.play(FadeIn(r, shift=UP * 0.08), run_time=0.3)

        caption = Text("not a setting buried in menus", color=PALETTE["dim"], font_size=16)
        caption.next_to(panel, DOWN, buff=0.5)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(1.3)


class B06_ClosingFraming(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("A better recommendation.", color=PALETTE["ink"], font_size=30)
        l2 = Text("A longer record of you.", color=PALETTE["ink"], font_size=30)
        l3 = Text("The difference is control.", color=PALETTE["accent"], font_size=30)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
