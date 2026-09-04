"""
Portrait (9:16) Manim scenes for the ai-nonprofit-marketing Short.
Manim's coordinate frame for a 2160x3840 (9:16) render is ~4.5 units wide x
8 units tall (vs ~14.2 x 8 landscape) — everything here is laid out for that
narrow, tall canvas: single-column stacks instead of side-by-side rows,
generous to_edge() buffs (>=0.7) learned from two GATE B near-misses on the
parent 16:9 build this session.

B00B_AgrimaIntro         — presenter card: "Hi, I'm Agrima." + lead-in
B01_OneTeamManyHats      — one-person card + four role tags, stacked 2x2
B03_AdoptionStats        — 50%+ / ~30% stat lines, stacked
B05_EmailPersonalization — generic vs personalized email, stacked vertically
B07_HonestLimit          — three-line contrast, stacked
B09_LoonClose            — closing typographic beat + Loon Project caption

(B02/B04/B06/B08 were dropped from this Short by shorts.py's auto-plan —
the parent reel is 3:59, over the 3:00 Shorts cap — so those four scenes
have no portrait counterpart here; the rewritten B11 outro points viewers
to the long for the material those four beats covered.)
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
            "I want to talk about\nsomething I've seen firsthand,\n"
            "working on the Loon Project —\nhow AI is quietly helping\n"
            "small nonprofit teams keep up.",
            color=PALETTE["ink"], font_size=20, line_spacing=1.35, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.6)
        grow_in(self, rule, 1.4, run_time=0.35)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.2)


class B01_OneTeamManyHats(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        center = card_bg(2.6, 1.2)
        center_txt = Text("One person.", color=PALETTE["ink"], font_size=20)
        center_g = VGroup(center, center_txt.move_to(center.get_center()))
        center.stretch(0.01, 0)
        self.play(center.animate.stretch_to_fit_width(2.6), FadeIn(center_txt), run_time=0.55)

        rule = Line(UP * 0.2, DOWN * 0.2, color=PALETTE["border"], stroke_width=2)

        roles = ["Outreach", "Storytelling", "Campaigns", "Fundraising"]
        tag_boxes = []
        for role in roles:
            box = card_bg(1.6, 0.85)
            txt = Text(role, color=PALETTE["accent"], font_size=13)
            tag_boxes.append(VGroup(box, txt.move_to(box.get_center())))
        grid = VGroup(*tag_boxes).arrange_in_grid(rows=2, cols=2, buff=0.3)

        VGroup(center_g, rule, grid).arrange(DOWN, buff=0.3).move_to(ORIGIN + UP * 0.3)

        grow_in(self, rule, rule.get_height(), run_time=0.3)
        for t in tag_boxes:
            t[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[t[0].animate.stretch_to_fit_width(1.6) for t in tag_boxes], lag_ratio=0.2),
            LaggedStart(*[FadeIn(t[1]) for t in tag_boxes], lag_ratio=0.2),
            run_time=1.1,
        )

        footer = Text("Same work. One person.", color=PALETTE["dim"],
                       font_size=15).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B03_AdoptionStats(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        s1_num = Text("50%+", color=PALETTE["accent"], font_size=42)
        s1_lbl = fit(Text("of nonprofits piloting\nor using AI", color=PALETTE["ink"],
                           font_size=17, line_spacing=1.2, should_center=True))
        s1 = VGroup(s1_num, s1_lbl).arrange(DOWN, buff=0.18)

        s2_num = Text("~30%", color=PALETTE["accent"], font_size=42)
        s2_lbl = fit(Text("report a direct\nrevenue increase", color=PALETTE["ink"],
                           font_size=17, line_spacing=1.2, should_center=True))
        s2 = VGroup(s2_num, s2_lbl).arrange(DOWN, buff=0.18)

        VGroup(s1, s2).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(FadeIn(s1, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(s2, shift=UP * 0.15), run_time=0.6)
        self.wait(1.2)


class B05_EmailPersonalization(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        gen_box = card_bg(3.2, 1.6)
        gen_head = Text("GENERIC", color=PALETTE["dim"], font_size=14)
        gen_lines = VGroup(*[
            Line(LEFT * 1.1, RIGHT * 1.1, color=PALETTE["border"], stroke_width=2)
            for _ in range(2)
        ]).arrange(DOWN, buff=0.16)
        gen_inner = VGroup(gen_head, gen_lines).arrange(DOWN, buff=0.2)
        gen = VGroup(gen_box, gen_inner.move_to(gen_box.get_center()))

        per_box = card_bg(3.2, 1.6, stroke_color=PALETTE["accent"])
        per_head = Text("PERSONALIZED", color=PALETTE["accent"], font_size=14)
        per_lines = VGroup(*[
            Line(LEFT * 1.1, RIGHT * 1.1, color=PALETTE["accent"], stroke_width=2)
            for _ in range(2)
        ]).arrange(DOWN, buff=0.16)
        per_inner = VGroup(per_head, per_lines).arrange(DOWN, buff=0.2)
        per = VGroup(per_box, per_inner.move_to(per_box.get_center()))

        VGroup(gen, per).arrange(DOWN, buff=0.35).move_to(ORIGIN + UP * 0.2)

        gen_box.stretch(0.01, 0)
        self.play(gen_box.animate.stretch_to_fit_width(3.2), FadeIn(gen_inner), run_time=0.6)
        per_box.stretch(0.01, 0)
        self.play(per_box.animate.stretch_to_fit_width(3.2), FadeIn(per_inner), run_time=0.6)

        stat = fit(Text("~2x open + click-through", color=PALETTE["accent"], font_size=18))
        stat.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_HonestLimit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("AI can draft fast.", color=PALETTE["ink"], font_size=26))
        l2 = fit(Text("It can't decide\nwhat to say.", color=PALETTE["accent"],
                       font_size=26, line_spacing=1.2, should_center=True))
        l3 = fit(Text("That part stays human.", color=PALETTE["dim"], font_size=17))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.55)
        self.wait(1.3)


class B09_LoonClose(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("A public presence.", color=PALETTE["ink"], font_size=26))
        l2 = fit(Text("Or not having one.", color=PALETTE["ink"], font_size=26))
        l3 = fit(Text("That's the difference.", color=PALETTE["accent"], font_size=26))
        cap = fit(Text("— the Loon Project", color=PALETTE["dim"], font_size=15))
        VGroup(l1, l2, l3, cap).arrange(DOWN, buff=0.28).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(cap, shift=UP * 0.1), run_time=0.45)
        self.wait(1.3)
