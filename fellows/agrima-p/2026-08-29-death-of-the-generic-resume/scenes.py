"""
Manim scenes for death-of-the-generic-resume

A reflective, first-person explainer on the AI-hiring rejection pattern.
No code/CLI content — every body beat is a from-scratch typographic or
diagram visual, built in the house Claude palette.

B00B_AgrimaIntro    — presenter card: "Hi, I'm Agrima." + topic lead-in
B01_TheOutreach     — "recruiter reaches out" -> "you apply"
B02_InstantReject   — applied -> (fast) -> rejected, timestamped
B03_Gaslit          — the phrase, named
B04_QuoteDeny       — "no AI auto-rejects candidates"
B05_QuoteAdmit      — "we pre-screen for hard requirements" + checklist
B06_BlackBox        — application -> [ ? ] -> rejected
B07_TailoredStack   — one resume -> many AI-tailored versions
B08_IdenticalGrid   — grid of near-identical resume cards
B09_FilteredOut     — same grid, one card flagged
B10_NotDying        — minimal reframe card
B11_TwoAIs          — your AI <-> negotiating <-> their AI, you: waiting
B12_AboutYou         — three-line closing typographic beat
"""

from manim import *

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


def card_bg(width, height):
    return RoundedRectangle(
        corner_radius=0.12, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=PALETTE["border"], stroke_width=1.5,
    )


def grow_in(scene, mob, target_width, run_time=0.5):
    """Genuine shape-state change (GATE A) — a box/line grows into place
    rather than just fading, mirroring the pattern used across this
    project's other reels."""
    mob.stretch(0.01, 0)
    scene.play(mob.animate.stretch_to_fit_width(target_width), run_time=run_time)


class B00B_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = Text(
            "I want to talk about something\nthat's been bugging me for a while —\n"
            "a pattern I keep running into every\nsingle time I apply for a job.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.35, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.wait(1.3)


class B01_TheOutreach(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        step1_box = card_bg(4.6, 2.2)
        step1_head = Text("1", color=PALETTE["accent"], font_size=30)
        step1_body = Text("A recruiter reaches out.\nPersonally. They think\nyou'd be a great fit.",
                           color=PALETTE["ink"], font_size=18, line_spacing=1.3, should_center=True)
        step1_g = VGroup(step1_head, step1_body).arrange(DOWN, buff=0.25)
        step1_card = VGroup(step1_box, step1_g.move_to(step1_box.get_center()))

        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=PALETTE["accent"], stroke_width=4, buff=0)

        step2_box = card_bg(4.6, 2.2)
        step2_head = Text("2", color=PALETTE["accent"], font_size=30)
        step2_body = Text("You apply.",
                           color=PALETTE["ink"], font_size=18, line_spacing=1.3, should_center=True)
        step2_g = VGroup(step2_head, step2_body).arrange(DOWN, buff=0.25)
        step2_card = VGroup(step2_box, step2_g.move_to(step2_box.get_center()))

        row = VGroup(step1_card, arrow, step2_card).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        step1_box.stretch(0.01, 0)
        step2_box.stretch(0.01, 0)
        arrow_target = arrow.get_width()

        self.play(step1_box.animate.stretch_to_fit_width(4.6), FadeIn(step1_g), run_time=0.7)
        arrow.stretch(0.01, 0)
        self.play(arrow.animate.stretch_to_fit_width(arrow_target), run_time=0.4)
        self.play(step2_box.animate.stretch_to_fit_width(4.6), FadeIn(step2_g), run_time=0.7)
        self.wait(1.3)


class B02_InstantReject(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Minutes later. Sometimes seconds.", color=PALETTE["dim"],
                      font_size=22).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)

        applied_box = card_bg(3.6, 1.8)
        applied_txt = Text("Applied", color=PALETTE["ink"], font_size=22)
        applied = VGroup(applied_box, applied_txt.move_to(applied_box.get_center()))
        applied.move_to(LEFT * 3.4)

        rejected_box = card_bg(3.6, 1.8)
        rejected_box.set_stroke(PALETTE["miss"], width=2.5)
        rejected_txt = Text("Rejected", color=PALETTE["miss"], font_size=22)
        rejected = VGroup(rejected_box, rejected_txt.move_to(rejected_box.get_center()))
        rejected.move_to(RIGHT * 3.4)

        applied_box.stretch(0.01, 0)
        self.play(applied_box.animate.stretch_to_fit_width(3.6), FadeIn(applied_txt), run_time=0.6)

        clock = Text("00:00:47", color=PALETTE["accent"], font_size=26).move_to(ORIGIN)
        self.play(FadeIn(clock), run_time=0.4)
        self.wait(0.3)

        rejected_box.stretch(0.01, 0)
        self.play(
            FadeOut(clock),
            rejected_box.animate.stretch_to_fit_width(3.6),
            FadeIn(rejected_txt),
            run_time=0.6,
        )
        self.wait(0.3)

        arrow = Arrow(applied.get_right() + RIGHT * 0.15, rejected.get_left() + LEFT * 0.15,
                      color=PALETTE["dim"], stroke_width=3, buff=0)
        arrow_target_width = arrow.get_width()
        arrow.stretch(0.01, 0)
        self.play(arrow.animate.stretch_to_fit_width(arrow_target_width), run_time=0.5)

        footer = Text("No feedback. No reason. Just no.", color=PALETTE["dim"],
                       font_size=18).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


class B03_Gaslit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = Text("Gaslit by the process.", color=PALETTE["ink"], font_size=40)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)
        sub = Text("No one will tell you why.", color=PALETTE["dim"], font_size=20)

        group = VGroup(phrase, rule, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.8)
        rule.stretch(0.01, 0)
        self.play(rule.animate.stretch_to_fit_width(1.8), run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


def _quote_card(text, attribution, extra=None):
    box = card_bg(7.6, 3.2 if extra is None else 3.8)
    mark = Text("“", color=PALETTE["accent"], font_size=60)
    body = Text(text, color=PALETTE["ink"], font_size=24, line_spacing=1.3, should_center=True)
    attr = Text(attribution, color=PALETTE["dim"], font_size=17)
    inner = VGroup(mark, body, attr).arrange(DOWN, buff=0.2)
    if extra is not None:
        inner = VGroup(mark, body, extra, attr).arrange(DOWN, buff=0.2)
    return VGroup(box, inner.move_to(box.get_center()))


class B04_QuoteDeny(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        card = _quote_card(
            "No AI auto-rejects\ncandidates. A person\nreads every application.",
            "— some recruiters, when asked",
        )
        box = card[0]
        inner = card[1]
        box.stretch(0.01, 0)
        self.play(box.animate.stretch_to_fit_width(7.6), FadeIn(inner), run_time=0.9)
        self.wait(1.6)


class B05_QuoteAdmit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        checklist = Text("Visa  ·  Location  ·  Years of experience",
                          color=PALETTE["accent"], font_size=17)
        card = _quote_card(
            "We pre-screen for\nthe hard requirements\nbefore a human sees it.",
            "— others, more quietly",
            extra=checklist,
        )
        box = card[0]
        inner = card[1]
        box.stretch(0.01, 0)
        self.play(box.animate.stretch_to_fit_width(7.6), FadeIn(inner), run_time=0.9)
        self.wait(1.6)


class B06_BlackBox(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Which one just happened to you?", color=PALETTE["ink"],
                      font_size=24).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)

        app_box = card_bg(3.2, 1.6)
        app_txt = Text("Application", color=PALETTE["ink"], font_size=18)
        app = VGroup(app_box, app_txt.move_to(app_box.get_center())).move_to(LEFT * 4.0)

        mid_box = Rectangle(width=2.0, height=2.0, fill_color=PALETTE["ink"],
                             fill_opacity=1, stroke_width=0)
        mid_q = Text("?", color=PALETTE["bg"], font_size=60)
        mid = VGroup(mid_box, mid_q.move_to(mid_box.get_center())).move_to(ORIGIN)

        out_box = card_bg(3.2, 1.6)
        out_box.set_stroke(PALETTE["miss"], width=2.5)
        out_txt = Text("Rejected", color=PALETTE["miss"], font_size=18)
        out = VGroup(out_box, out_txt.move_to(out_box.get_center())).move_to(RIGHT * 4.0)

        app_box.stretch(0.01, 0)
        self.play(app_box.animate.stretch_to_fit_width(3.2), FadeIn(app_txt), run_time=0.6)

        a1 = Arrow(app.get_right() + RIGHT * 0.1, mid.get_left() + LEFT * 0.1,
                   color=PALETTE["dim"], stroke_width=3, buff=0)
        self.play(Create(a1), run_time=0.4)

        mid_box.stretch(0.01, 0)
        self.play(mid_box.animate.stretch_to_fit_width(2.0), FadeIn(mid_q), run_time=0.6)

        a2 = Arrow(mid.get_right() + RIGHT * 0.1, out.get_left() + LEFT * 0.1,
                   color=PALETTE["dim"], stroke_width=3, buff=0)
        self.play(Create(a2), run_time=0.4)

        out_box.stretch(0.01, 0)
        self.play(out_box.animate.stretch_to_fit_width(3.2), FadeIn(out_txt), run_time=0.6)
        self.wait(1.3)


class B07_TailoredStack(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("One resume. Fifty tailored versions.", color=PALETTE["ink"],
                      font_size=24).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)

        base = card_bg(2.6, 3.4)
        base_txt = Text("Resume", color=PALETTE["ink"], font_size=18)
        base_card = VGroup(base, base_txt.move_to(base.get_center()))
        base_card.move_to(LEFT * 3.5)
        base.stretch(0.01, 0)
        self.play(base.animate.stretch_to_fit_width(2.6), FadeIn(base_txt), run_time=0.6)

        fan = VGroup()
        offsets = [(-0.35, 0.25), (0.0, 0.15), (0.35, 0.05), (0.7, -0.05), (1.05, -0.15)]
        for i, (dx, dy) in enumerate(offsets):
            c = card_bg(2.0, 2.7)
            c.move_to(RIGHT * (1.6 + dx * 1.4) + UP * (dy * 1.4))
            fan.add(c)

        for c in fan:
            c.stretch(0.01, 0)
        self.play(
            LaggedStart(*[c.animate.stretch_to_fit_width(2.0) for c in fan], lag_ratio=0.15),
            run_time=1.2,
        )

        footer = Text("AI-tailored, one per posting.", color=PALETTE["dim"],
                       font_size=18).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)


def _resume_grid(scene, flag_index=None):
    grid = VGroup()
    for r in range(2):
        for c in range(3):
            box = card_bg(2.1, 1.7)
            box.move_to(RIGHT * (c - 1) * 2.4 + UP * (0.5 - r) * 2.0)
            grid.add(box)

    for box in grid:
        box.stretch(0.01, 0)
    scene.play(
        LaggedStart(*[b.animate.stretch_to_fit_width(2.1) for b in grid], lag_ratio=0.08),
        run_time=1.1,
    )
    return grid


class B08_IdenticalGrid(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Starting to sound identical.", color=PALETTE["ink"],
                      font_size=24).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)

        _resume_grid(self)
        self.wait(1.4)


class B09_FilteredOut(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Its own reason to get filtered out.", color=PALETTE["ink"],
                      font_size=24).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)

        grid = _resume_grid(self)

        flagged = grid[2]
        self.play(flagged.animate.set_stroke(PALETTE["miss"], width=3), run_time=0.4)
        tag = Text("FILTERED", color=PALETTE["miss"], font_size=14)
        tag.next_to(flagged, DOWN, buff=0.12)
        self.play(FadeIn(tag), run_time=0.4)
        self.wait(1.3)


class B10_NotDying(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = Text("Not a story about", color=PALETTE["dim"], font_size=28)
        line2 = Text("the resume dying.", color=PALETTE["ink"], font_size=34)
        group = VGroup(line1, line2).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(line1, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.7)
        self.wait(1.5)


class B11_TwoAIs(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        your_box = card_bg(3.4, 2.0)
        your_txt = Text("Your AI", color=PALETTE["ink"], font_size=22)
        your_card = VGroup(your_box, your_txt.move_to(your_box.get_center())).move_to(LEFT * 3.0 + UP * 0.6)

        their_box = card_bg(3.4, 2.0)
        their_txt = Text("Their AI", color=PALETTE["ink"], font_size=22)
        their_card = VGroup(their_box, their_txt.move_to(their_box.get_center())).move_to(RIGHT * 3.0 + UP * 0.6)

        your_box.stretch(0.01, 0)
        their_box.stretch(0.01, 0)
        self.play(your_box.animate.stretch_to_fit_width(3.4), FadeIn(your_txt), run_time=0.6)
        self.play(their_box.animate.stretch_to_fit_width(3.4), FadeIn(their_txt), run_time=0.6)

        arrow = DoubleArrow(your_card.get_right() + RIGHT * 0.15, their_card.get_left() + LEFT * 0.15,
                             color=PALETTE["accent"], stroke_width=3, buff=0)
        label = Text("negotiating", color=PALETTE["accent"], font_size=16)
        label.next_to(arrow, UP, buff=0.1)
        arrow_target_width = arrow.get_width()
        arrow.stretch(0.01, 0)
        self.play(arrow.animate.stretch_to_fit_width(arrow_target_width), FadeIn(label), run_time=0.6)

        you_box = card_bg(2.6, 1.1)
        you_box.set_stroke(PALETTE["border"], width=1.5)
        you_txt = Text("you: waiting", color=PALETTE["dim"], font_size=16)
        you_card = VGroup(you_box, you_txt.move_to(you_box.get_center())).to_edge(DOWN, buff=0.7)
        you_box.stretch(0.01, 0)
        self.play(you_box.animate.stretch_to_fit_width(2.6), FadeIn(you_txt), run_time=0.6)
        self.wait(1.3)


class B12_AboutYou(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("Two systems.", color=PALETTE["ink"], font_size=32)
        l2 = Text("Talking past you.", color=PALETTE["ink"], font_size=32)
        l3 = Text("About you.", color=PALETTE["accent"], font_size=32)
        group = VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
