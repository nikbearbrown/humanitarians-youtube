"""
Portrait (9:16) Manim scenes for the no-face-no-problem Short.

shorts.py's auto-plan dropped 3 beats (B02 the strategy, B03 the voice gap,
B07 the closing reflection) since the parent (4:11) is over the 3:00 Shorts
cap. The 5 Manim scenes that survive are relaid out here for a narrow, tall
canvas (~4.5 x 8 units vs ~14.2 x 8 landscape): single-column stacks
instead of side-by-side rows, generous to_edge() buffs (>=0.7) per this
session's GATE B near-miss lessons. B01 and B05 carry forward the same
fixes applied to the parent (motifs scaled to fit their frame; a plain-text
skepticism flag, no unicode glyph).

B00B_AgrimaIntro — presenter card: "Hi, I'm Agrima." + lead-in
B01_TheHook      — stock-footage-style caption card (skyline/wave/flame)
B04_WhereItPays  — niche card grid (2 columns)
B05_TrustFinding — trust-stat card with an explicit on-screen skepticism flag
B06_TheReframe   — watch-time meter, not a face
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
            "I want to talk about\nsomething I keep noticing\nwhen I scroll — accounts with\n"
            "no face, no name, just a\ncalm voice and some footage.",
            color=PALETTE["ink"], font_size=20, line_spacing=1.3, should_center=True))
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.4, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


def _skyline():
    bars = VGroup(*[
        Rectangle(width=0.28, height=h, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        for h in [0.65, 1.1, 0.8, 1.35, 0.9, 0.7, 1.2]
    ]).arrange(RIGHT, buff=0.06, aligned_edge=DOWN)
    return bars


def _waves():
    lines = VGroup(*[
        FunctionGraph(lambda x, p=p: 0.15 * np.sin(x * 2 + p), x_range=[-1.3, 1.3],
                      color=PALETTE["dim"], stroke_width=3)
        for p in [0, 1.0, 2.0]
    ]).arrange(DOWN, buff=0.18)
    return lines


def _flame():
    outer = Triangle(fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0).scale(0.45)
    outer.stretch(0.6, 0)
    inner = Triangle(fill_color=PALETTE["bg"], fill_opacity=1, stroke_width=0).scale(0.23)
    inner.stretch(0.6, 0).shift(DOWN * 0.1)
    return VGroup(outer, inner)


class B01_TheHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        frame = card_bg(3.6, 3.3, stroke_color=PALETTE["border"])
        vignette = RoundedRectangle(corner_radius=0.08, width=3.4, height=3.1,
                                     fill_color=PALETTE["ink"], fill_opacity=0.04, stroke_width=0)

        motifs = VGroup(_skyline(), _waves(), _flame()).arrange(RIGHT, buff=0.35)
        motifs.scale_to_fit_width(2.9)
        motifs.move_to(frame.get_center() + UP * 0.35)

        stock_tag = Text("STOCK FOOTAGE", color=PALETTE["dim"], font_size=13)
        stock_tag.move_to(frame.get_top() + DOWN * 0.32)

        scene_group = VGroup(frame, vignette, motifs, stock_tag)
        scene_group.move_to(UP * 0.9)

        frame.stretch(0.01, 0)
        self.play(frame.animate.stretch_to_fit_width(3.6), FadeIn(vignette), run_time=0.6)
        self.play(FadeIn(stock_tag), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in motifs], lag_ratio=0.25), run_time=0.9)

        caption = fit(Text("5 FACTS ABOUT MONEY\nNOBODY TELLS YOU", color=PALETTE["accent"],
                            font_size=20, weight="BOLD", line_spacing=1.2, should_center=True), 3.2)
        caption.move_to(frame.get_bottom() + UP * 0.5)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        tag = Text("no face · no name", color=PALETTE["dim"], font_size=15)
        tag.next_to(frame, DOWN, buff=0.5)
        self.play(FadeIn(tag), run_time=0.4)
        self.wait(1.3)


def _niche_card(label, w=1.65, h=1.3, fs=13):
    box = card_bg(w, h)
    txt = fit(Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.15,
                    should_center=True), w - 0.25)
    return VGroup(box, txt.move_to(box.get_center()))


class B04_WhereItPays(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        labels = ["Personal\nFinance", "Tech &\nAI News", "True\nCrime", "Psychology", "Self-\nImprovement"]
        cards = VGroup(*[_niche_card(lbl) for lbl in labels])
        cards.arrange_in_grid(rows=3, cols=2, buff=0.22).move_to(UP * 0.2)

        for c in cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(1.65) for c in cards], lag_ratio=0.15),
            LaggedStart(*[FadeIn(c[1]) for c in cards], lag_ratio=0.15),
            run_time=1.2,
        )

        tag = fit(Text("some of the highest ad rates", color=PALETTE["accent"], font_size=16))
        tag.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B05_TrustFinding(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        stat = fit(Text("\"more trustworthy,\nnot less.\"", color=PALETTE["ink"], font_size=28,
                         line_spacing=1.25, should_center=True, weight="BOLD"))
        rule = Line(LEFT * 0.8, RIGHT * 0.8, color=PALETTE["accent"], stroke_width=3)
        sub = fit(Text("no personality to get\ndistracted by — just the\ninformation", color=PALETTE["dim"],
                        font_size=16, line_spacing=1.3, should_center=True))

        VGroup(stat, rule, sub).arrange(DOWN, buff=0.35).move_to(UP * 0.4)

        self.play(FadeIn(stat, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 1.6, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)

        flag = card_bg(3.5, 1.05, stroke_color=PALETTE["miss"])
        flag_txt = fit(Text("sourced from AI-tool vendors —\ntake with skepticism",
                             color=PALETTE["miss"], font_size=14, line_spacing=1.25,
                             should_center=True), 3.1)
        flag_txt.move_to(flag.get_center())
        flag_group = VGroup(flag, flag_txt).to_edge(DOWN, buff=0.7)

        flag.stretch(0.01, 0)
        self.play(flag.animate.stretch_to_fit_width(3.5), FadeIn(flag_txt), run_time=0.6)
        self.wait(1.3)


class B06_TheReframe(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("WATCH TIME", color=PALETTE["dim"], font_size=17).to_edge(UP, buff=0.75)
        self.play(FadeIn(title), run_time=0.4)

        track = RoundedRectangle(corner_radius=0.12, width=3.2, height=0.5,
                                  fill_color=PALETTE["card"], fill_opacity=1,
                                  stroke_color=PALETTE["border"], stroke_width=1.5)
        fill = RoundedRectangle(corner_radius=0.12, width=3.2, height=0.5,
                                 fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        fill.align_to(track, LEFT)
        meter = VGroup(track, fill).move_to(UP * 0.5)

        fill.stretch(0.01, 0)
        fill.align_to(track, LEFT)
        self.play(FadeIn(track), run_time=0.3)
        self.play(fill.animate.stretch_to_fit_width(3.2).align_to(track, LEFT), run_time=1.0)

        tags = fit(Text("completion · saves · shares", color=PALETTE["ink"], font_size=16))
        tags.next_to(meter, DOWN, buff=0.5)
        self.play(FadeIn(tags, shift=UP * 0.1), run_time=0.5)

        no_face = VGroup(
            Circle(radius=0.24, color=PALETTE["dim"], stroke_width=2.5),
            Line(LEFT * 0.17, RIGHT * 0.17, color=PALETTE["miss"], stroke_width=3).rotate(PI / 4),
        )
        no_face_label = Text("not a face", color=PALETTE["dim"], font_size=14)
        no_face_group = VGroup(no_face, no_face_label).arrange(DOWN, buff=0.15)
        no_face_group.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(no_face_group, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)
