"""
Manim scenes for ai-nonprofit-marketing

A first-person, professional explainer on how AI is helping small nonprofit
marketing teams, sourced from Articles/ai-nonprofit-marketing-article.md.
No code/CLI content — every body beat is a from-scratch typographic or
diagram visual, built in the house Claude palette.

B00B_AgrimaIntro       — presenter card: "Hi, I'm Agrima." + topic lead-in
B01_OneTeamManyHats    — one person, four roles stacked on them
B02_LoonBudget         — full team vs. one person, budget bar, Loon Project
B03_AdoptionStats      — 50%+ piloting/using AI, ~30% revenue increase
B04_UnglamorousTasks   — 2x2 grid: the four automated task types
B05_EmailPersonalization — generic vs personalized email, ~2x open/CTR
B06_DonationFormLift   — $115 vs $161 donation-form bar comparison
B07_HonestLimit        — "AI can draft fast." / "It can't decide what to say."
B08_NotTopDown         — reframe: not big tech, top-down
B09_LoonClose           — closing typographic beat, Loon Project named
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
            "I want to talk about something\nI've seen firsthand, working on\n"
            "the Loon Project — how AI is\nquietly helping small nonprofit\nteams keep up.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.35, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.wait(1.3)


class B01_OneTeamManyHats(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        center = card_bg(3.0, 1.6)
        center_txt = Text("One person.", color=PALETTE["ink"], font_size=24)
        center_g = VGroup(center, center_txt.move_to(center.get_center()))
        center.stretch(0.01, 0)
        self.play(center.animate.stretch_to_fit_width(3.0), FadeIn(center_txt), run_time=0.6)

        roles = ["Outreach", "Storytelling", "Campaigns", "Fundraising"]
        positions = [UP * 2.1 + LEFT * 3.4, UP * 2.1 + RIGHT * 3.4,
                     DOWN * 2.1 + LEFT * 3.4, DOWN * 2.1 + RIGHT * 3.4]
        # Lines run edge-to-edge, not center-to-center, so they never enter
        # either box's bounding area (avoids a text/label-on-line GATE B
        # false-positive — the audit flags spatial overlap regardless of
        # z-order, so the gap has to be real, not just visually occluded).
        center_pt = np.array(center_g.get_center())
        CENTER_CLEAR = 1.8   # just outside the 3.0x1.6 center card's half-diagonal
        TAG_CLEAR = 1.35     # just outside the 2.3x0.9 tag card's half-diagonal

        tags = VGroup()
        lines = VGroup()
        for role, pos in zip(roles, positions):
            tag_box = card_bg(2.3, 0.9)
            tag_txt = Text(role, color=PALETTE["accent"], font_size=17)
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
            self.play(box.animate.stretch_to_fit_width(2.3), FadeIn(tag[1]), run_time=0.35)

        footer = Text("Same work. One person.", color=PALETTE["dim"],
                       font_size=18).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B02_LoonBudget(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        big_box = card_bg(4.6, 2.6)
        big_txt = Text("A full marketing\nteam.", color=PALETTE["ink"], font_size=22,
                        line_spacing=1.3, should_center=True)
        big = VGroup(big_box, big_txt.move_to(big_box.get_center())).move_to(LEFT * 3.4)

        small_box = card_bg(3.2, 1.8)
        small_txt = Text("One person.", color=PALETTE["ink"], font_size=20)
        small = VGroup(small_box, small_txt.move_to(small_box.get_center())).move_to(RIGHT * 3.4)

        big_box.stretch(0.01, 0)
        self.play(big_box.animate.stretch_to_fit_width(4.6), FadeIn(big_txt), run_time=0.6)
        small_box.stretch(0.01, 0)
        self.play(small_box.animate.stretch_to_fit_width(3.2), FadeIn(small_txt), run_time=0.6)

        bar_label = Text("BUDGET", color=PALETTE["dim"], font_size=14).move_to(DOWN * 1.0)
        big_bar = Rectangle(width=4.6, height=0.3, fill_color=PALETTE["good"],
                             fill_opacity=1, stroke_width=0).next_to(bar_label, DOWN, buff=0.25)
        big_bar.align_to(big, LEFT)
        small_bar = Rectangle(width=1.0, height=0.3, fill_color=PALETTE["miss"],
                               fill_opacity=1, stroke_width=0)
        small_bar.next_to(big_bar, RIGHT, buff=1.0)

        self.play(FadeIn(bar_label), run_time=0.3)
        grow_in(self, big_bar, 4.6, run_time=0.5)
        grow_in(self, small_bar, 1.0, run_time=0.5)

        footer = Text("— like the Loon Project", color=PALETTE["dim"],
                       font_size=17).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B03_AdoptionStats(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        s1_num = Text("50%+", color=PALETTE["accent"], font_size=52)
        s1_lbl = Text("of nonprofits piloting or using AI", color=PALETTE["ink"], font_size=20)
        s1 = VGroup(s1_num, s1_lbl).arrange(DOWN, buff=0.2)

        s2_num = Text("~30%", color=PALETTE["accent"], font_size=52)
        s2_lbl = Text("report a direct revenue increase", color=PALETTE["ink"], font_size=20)
        s2 = VGroup(s2_num, s2_lbl).arrange(DOWN, buff=0.2)

        VGroup(s1, s2).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        self.play(FadeIn(s1, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(s2, shift=UP * 0.15), run_time=0.7)
        self.wait(1.3)


def _task_card(label, w=3.0, h=1.5, fs=17):
    box = card_bg(w, h)
    txt = Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.2, should_center=True)
    return VGroup(box, txt.move_to(box.get_center()))


class B04_UnglamorousTasks(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("The unglamorous work.", color=PALETTE["dim"],
                      font_size=22).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.5)

        labels = ["Donor\nemails", "Impact reports\n→ social posts",
                  "Meeting notes\n→ summaries", "Long content\n→ short posts"]
        cards = VGroup(*[_task_card(lbl) for lbl in labels])
        cards.arrange_in_grid(rows=2, cols=2, buff=0.5).move_to(DOWN * 0.2)

        for c in cards:
            box = c[0]
            box.stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(3.0) for c in cards], lag_ratio=0.15),
            LaggedStart(*[FadeIn(c[1]) for c in cards], lag_ratio=0.15),
            run_time=1.3,
        )
        self.wait(1.2)


class B05_EmailPersonalization(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        gen_box = card_bg(3.4, 3.0)
        gen_head = Text("GENERIC", color=PALETTE["dim"], font_size=16)
        gen_lines = VGroup(*[
            Line(LEFT * 1.2, RIGHT * 1.2, color=PALETTE["border"], stroke_width=2)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.22)
        gen_inner = VGroup(gen_head, gen_lines).arrange(DOWN, buff=0.3)
        gen = VGroup(gen_box, gen_inner.move_to(gen_box.get_center())).move_to(LEFT * 3.0)

        per_box = card_bg(3.4, 3.0, stroke_color=PALETTE["accent"])
        per_head = Text("PERSONALIZED", color=PALETTE["accent"], font_size=16)
        per_lines = VGroup(*[
            Line(LEFT * 1.2, RIGHT * 1.2, color=PALETTE["accent"], stroke_width=2)
            for _ in range(3)
        ]).arrange(DOWN, buff=0.22)
        per_inner = VGroup(per_head, per_lines).arrange(DOWN, buff=0.3)
        per = VGroup(per_box, per_inner.move_to(per_box.get_center())).move_to(RIGHT * 3.0)

        gen_box.stretch(0.01, 0)
        self.play(gen_box.animate.stretch_to_fit_width(3.4), FadeIn(gen_inner), run_time=0.7)
        per_box.stretch(0.01, 0)
        self.play(per_box.animate.stretch_to_fit_width(3.4), FadeIn(per_inner), run_time=0.7)

        stat = Text("~2x open + click-through", color=PALETTE["accent"],
                     font_size=22).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(stat, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B06_DonationFormLift(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Average donation size.", color=PALETTE["dim"],
                      font_size=22).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.5)

        base_y = DOWN * 1.6
        bar1 = Rectangle(width=1.6, height=1.6, fill_color=PALETTE["dim"],
                          fill_opacity=1, stroke_width=0)
        bar1.move_to(LEFT * 2.2 + base_y + UP * 0.8)
        bar1.align_to(base_y, DOWN)
        lbl1 = Text("$115", color=PALETTE["ink"], font_size=26).next_to(bar1, UP, buff=0.15)
        sub1 = Text("industry-wide", color=PALETTE["dim"], font_size=15).next_to(bar1, DOWN, buff=0.2)

        bar2 = Rectangle(width=1.6, height=2.25, fill_color=PALETTE["accent"],
                          fill_opacity=1, stroke_width=0)
        bar2.move_to(RIGHT * 2.2 + base_y + UP * 1.125)
        bar2.align_to(base_y, DOWN)
        lbl2 = Text("$161", color=PALETTE["ink"], font_size=26).next_to(bar2, UP, buff=0.15)
        sub2 = Text("AI-optimized form", color=PALETTE["accent"], font_size=15).next_to(bar2, DOWN, buff=0.2)

        bar1_h = bar1.get_height()
        bar1.stretch(0.01, 1)
        bar1.align_to(base_y, DOWN)
        bar2_h = bar2.get_height()
        bar2.stretch(0.01, 1)
        bar2.align_to(base_y, DOWN)

        self.play(bar1.animate.stretch_to_fit_height(bar1_h), FadeIn(lbl1), FadeIn(sub1), run_time=0.6)
        self.play(bar2.animate.stretch_to_fit_height(bar2_h), FadeIn(lbl2), FadeIn(sub2), run_time=0.6)
        self.wait(1.3)


class B07_HonestLimit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("AI can draft fast.", color=PALETTE["ink"], font_size=32)
        l2 = Text("It can't decide what to say.", color=PALETTE["accent"], font_size=32)
        l3 = Text("That part stays human.", color=PALETTE["dim"], font_size=20)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B08_NotTopDown(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("Not big tech,\ntop-down.", color=PALETTE["ink"], font_size=38,
                       line_spacing=1.2, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = Text("Free tools, reaching the smallest teams.", color=PALETTE["dim"], font_size=19)

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B09_LoonClose(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("A public presence.", color=PALETTE["ink"], font_size=32)
        l2 = Text("Or not having one.", color=PALETTE["ink"], font_size=32)
        l3 = Text("That's the difference.", color=PALETTE["accent"], font_size=32)
        cap = Text("— the Loon Project", color=PALETTE["dim"], font_size=18)
        VGroup(l1, l2, l3, cap).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(cap, shift=UP * 0.1), run_time=0.5)
        self.wait(1.4)
