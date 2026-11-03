"""
Portrait (9:16) Manim scenes for the death-of-the-generic-resume Short.
Manim's coordinate frame for a 2160x3840 (9:16) render is ~4.5 units wide x
8 units tall (vs ~14.2 x 8 landscape) — everything here is laid out for that
narrow, tall canvas: single-column stacks instead of side-by-side rows,
smaller type, width-guarded text.

B00B_AgrimaIntro — presenter card: "Hi, I'm Agrima." + topic lead-in
B01_TheOutreach  — recruiter reaches out -> you apply, stacked vertically
B02_InstantReject— applied -> (fast) -> rejected, stacked vertically
B03_Gaslit       — the phrase, named
B04_QuoteDeny    — "no AI auto-rejects candidates"
B05_QuoteAdmit   — "we pre-screen for hard requirements" + checklist
B06_BlackBox     — application -> [ ? ] -> rejected, stacked vertically
B10_NotDying     — minimal reframe card
B12_AboutYou     — three-line closing typographic beat

(B07/B08/B09/B11 were dropped from this Short by shorts.py's auto-plan —
the parent reel is 4:00, over the 3:00 Shorts cap — so those four scenes
have no portrait counterpart here; the rewritten B14 outro points viewers
to the long for the AI-arms-race arc and the closing "negotiating AIs"
beat those four covered.)
"""

from manim import *

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


def card_bg(width, height):
    return RoundedRectangle(
        corner_radius=0.1, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=PALETTE["border"], stroke_width=1.5,
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
            "I want to talk about\nsomething that's been\nbugging me for a while —\n"
            "a pattern I keep running\ninto every single time\nI apply for a job.",
            color=PALETTE["ink"], font_size=20, line_spacing=1.35, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.6)
        grow_in(self, rule, 1.4, run_time=0.35)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.2)


class B01_TheOutreach(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        step1_box = card_bg(3.6, 1.9)
        step1_head = Text("1", color=PALETTE["accent"], font_size=26)
        step1_body = fit(Text("A recruiter reaches out.\nPersonally. They think\nyou'd be a great fit.",
                               color=PALETTE["ink"], font_size=16, line_spacing=1.3, should_center=True), 3.2)
        step1_g = VGroup(step1_head, step1_body).arrange(DOWN, buff=0.2)
        step1_card = VGroup(step1_box, step1_g.move_to(step1_box.get_center()))

        arrow = Arrow(UP * 0.4, DOWN * 0.4, color=PALETTE["accent"], stroke_width=4, buff=0)

        step2_box = card_bg(3.6, 1.5)
        step2_head = Text("2", color=PALETTE["accent"], font_size=26)
        step2_body = Text("You apply.", color=PALETTE["ink"], font_size=16)
        step2_g = VGroup(step2_head, step2_body).arrange(DOWN, buff=0.2)
        step2_card = VGroup(step2_box, step2_g.move_to(step2_box.get_center()))

        VGroup(step1_card, arrow, step2_card).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        arrow_target = arrow.get_height()

        step1_box.stretch(0.01, 0)
        self.play(step1_box.animate.stretch_to_fit_width(3.6), FadeIn(step1_g), run_time=0.7)
        arrow.stretch(0.01, 1)
        self.play(arrow.animate.stretch_to_fit_height(arrow_target), run_time=0.4)
        step2_box.stretch(0.01, 0)
        self.play(step2_box.animate.stretch_to_fit_width(3.6), FadeIn(step2_g), run_time=0.7)
        self.wait(1.2)


class B02_InstantReject(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("Minutes later.\nSometimes seconds.", color=PALETTE["dim"],
                          font_size=18, line_spacing=1.2, should_center=True))
        title.to_edge(UP, buff=0.75)
        self.play(FadeIn(title), run_time=0.5)

        applied_box = card_bg(2.9, 1.2)
        applied_txt = Text("Applied", color=PALETTE["ink"], font_size=19)
        applied = VGroup(applied_box, applied_txt.move_to(applied_box.get_center()))

        clock = Text("00:00:47", color=PALETTE["accent"], font_size=22)

        rejected_box = card_bg(2.9, 1.2)
        rejected_box.set_stroke(PALETTE["miss"], width=2.5)
        rejected_txt = Text("Rejected", color=PALETTE["miss"], font_size=19)
        rejected = VGroup(rejected_box, rejected_txt.move_to(rejected_box.get_center()))

        footer = Text("No feedback. No reason. Just no.", color=PALETTE["dim"], font_size=15)

        VGroup(applied, clock, rejected, footer).arrange(DOWN, buff=0.35).next_to(title, DOWN, buff=0.5)

        applied_box.stretch(0.01, 0)
        self.play(applied_box.animate.stretch_to_fit_width(2.9), FadeIn(applied_txt), run_time=0.55)
        self.play(FadeIn(clock), run_time=0.35)
        self.wait(0.25)
        rejected_box.stretch(0.01, 0)
        self.play(
            FadeOut(clock),
            rejected_box.animate.stretch_to_fit_width(2.9),
            FadeIn(rejected_txt),
            run_time=0.55,
        )
        self.wait(0.2)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(1.1)


class B03_Gaslit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        phrase = fit(Text("Gaslit by\nthe process.", color=PALETTE["ink"],
                           font_size=34, line_spacing=1.2, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("No one will tell\nyou why.", color=PALETTE["dim"],
                        font_size=18, line_spacing=1.25, should_center=True))

        VGroup(phrase, rule, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(phrase, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.4, run_time=0.35)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.55)
        self.wait(1.3)


def _quote_card(text, attribution, extra=None):
    box = card_bg(3.7, 3.7 if extra is None else 4.1)
    mark = Text("“", color=PALETTE["accent"], font_size=46)
    body = fit(Text(text, color=PALETTE["ink"], font_size=19, line_spacing=1.3, should_center=True), 3.3)
    attr = fit(Text(attribution, color=PALETTE["dim"], font_size=14), 3.3)
    if extra is not None:
        inner = VGroup(mark, body, extra, attr).arrange(DOWN, buff=0.18)
    else:
        inner = VGroup(mark, body, attr).arrange(DOWN, buff=0.18)
    return VGroup(box, inner.move_to(box.get_center()))


class B04_QuoteDeny(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        card = _quote_card(
            "No AI auto-rejects\ncandidates. A person\nreads every\napplication.",
            "— some recruiters,\nwhen asked",
        )
        box, inner = card[0], card[1]
        box.stretch(0.01, 0)
        self.play(box.animate.stretch_to_fit_width(3.7), FadeIn(inner), run_time=0.85)
        self.wait(1.5)


class B05_QuoteAdmit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        checklist = fit(Text("Visa · Location ·\nYears of experience",
                              color=PALETTE["accent"], font_size=15, line_spacing=1.2, should_center=True), 3.3)
        card = _quote_card(
            "We pre-screen for\nthe hard requirements\nbefore a human\nsees it.",
            "— others, more quietly",
            extra=checklist,
        )
        box, inner = card[0], card[1]
        box.stretch(0.01, 0)
        self.play(box.animate.stretch_to_fit_width(3.7), FadeIn(inner), run_time=0.85)
        self.wait(1.5)


class B06_BlackBox(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("Which one just\nhappened to you?", color=PALETTE["ink"],
                          font_size=20, line_spacing=1.2, should_center=True))
        title.to_edge(UP, buff=0.75)
        self.play(FadeIn(title), run_time=0.5)

        app_box = card_bg(2.8, 1.1)
        app_txt = Text("Application", color=PALETTE["ink"], font_size=16)
        app = VGroup(app_box, app_txt.move_to(app_box.get_center()))

        mid_box = Rectangle(width=1.5, height=1.5, fill_color=PALETTE["ink"],
                             fill_opacity=1, stroke_width=0)
        mid_q = Text("?", color=PALETTE["bg"], font_size=46)
        mid = VGroup(mid_box, mid_q.move_to(mid_box.get_center()))

        out_box = card_bg(2.8, 1.1)
        out_box.set_stroke(PALETTE["miss"], width=2.5)
        out_txt = Text("Rejected", color=PALETTE["miss"], font_size=16)
        out = VGroup(out_box, out_txt.move_to(out_box.get_center()))

        col = VGroup(app, mid, out).arrange(DOWN, buff=0.55).next_to(title, DOWN, buff=0.5)

        app_box.stretch(0.01, 0)
        self.play(app_box.animate.stretch_to_fit_width(2.8), FadeIn(app_txt), run_time=0.55)

        a1 = Arrow(app.get_bottom() + DOWN * 0.06, mid.get_top() + UP * 0.06,
                   color=PALETTE["dim"], stroke_width=3, buff=0)
        a1_h = a1.get_height()
        a1.stretch(0.01, 1)
        self.play(a1.animate.stretch_to_fit_height(a1_h), run_time=0.35)

        mid_box.stretch(0.01, 0)
        self.play(mid_box.animate.stretch_to_fit_width(1.5), FadeIn(mid_q), run_time=0.55)

        a2 = Arrow(mid.get_bottom() + DOWN * 0.06, out.get_top() + UP * 0.06,
                   color=PALETTE["dim"], stroke_width=3, buff=0)
        a2_h = a2.get_height()
        a2.stretch(0.01, 1)
        self.play(a2.animate.stretch_to_fit_height(a2_h), run_time=0.35)

        out_box.stretch(0.01, 0)
        self.play(out_box.animate.stretch_to_fit_width(2.8), FadeIn(out_txt), run_time=0.55)
        self.wait(1.2)


class B10_NotDying(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = fit(Text("Not a story about", color=PALETTE["dim"], font_size=24))
        line2 = fit(Text("the resume dying.", color=PALETTE["ink"], font_size=28))
        VGroup(line1, line2).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(line1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)


class B12_AboutYou(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = fit(Text("Two systems.", color=PALETTE["ink"], font_size=28))
        l2 = fit(Text("Talking past you.", color=PALETTE["ink"], font_size=28))
        l3 = fit(Text("About you.", color=PALETTE["accent"], font_size=28))
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.55)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.55)
        self.wait(1.4)
