"""
Manim scenes for no-face-no-problem

A first-person, observational, slightly-wry explainer on faceless AI content
accounts, sourced from the user-supplied article "No Face, No Problem:
Inside the Rise of AI Accounts Nobody's Ever Seen — and Why We Might Trust
Them Anyway." Per the user's explicit materials note, several beats lean
into the article's OWN aesthetic — abstract stock-footage motifs (a
skyline, waves, a flame) with bold on-screen captions standing in for a
host on camera, rather than a composer/host card, since that directly
performs the piece's own point. Built in the house Claude palette.

B00B_AgrimaIntro    — presenter card: "Hi, I'm Agrima." + topic lead-in
B01_TheHook         — stock-footage-style caption card (skyline/wave/flame)
B02_TheStrategy     — flow checklist: topic -> script -> AI voice -> footage -> post
B03_TheVoiceGap     — before/after AI-voice comparison + cost + arms-race note
B04_WhereItPays     — niche icon grid + higher-ad-rate tag
B05_TrustFinding    — trust stat card with an explicit on-screen skepticism flag
B06_TheReframe      — watch-time meter, not a face
B07_ClosingQuestion — quiet typographic closing beat
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
            "I want to talk about\nsomething I keep noticing\nwhen I scroll — accounts with\n"
            "no face, no name, just a\ncalm voice and some footage,\ndoing surprisingly well.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.3, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        grow_in(self, rule, 1.8, run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.4)


def _skyline():
    bars = VGroup(*[
        Rectangle(width=0.35, height=h, fill_color=PALETTE["dim"], fill_opacity=1, stroke_width=0)
        for h in [0.8, 1.4, 1.0, 1.7, 1.1, 0.9, 1.5]
    ]).arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
    return bars


def _waves():
    lines = VGroup(*[
        FunctionGraph(lambda x, p=p: 0.18 * np.sin(x * 2 + p), x_range=[-1.6, 1.6],
                      color=PALETTE["dim"], stroke_width=3)
        for p in [0, 1.0, 2.0]
    ]).arrange(DOWN, buff=0.22)
    return lines


def _flame():
    outer = Triangle(fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0).scale(0.55)
    outer.stretch(0.6, 0)
    inner = Triangle(fill_color=PALETTE["bg"], fill_opacity=1, stroke_width=0).scale(0.28)
    inner.stretch(0.6, 0).shift(DOWN * 0.12)
    return VGroup(outer, inner)


class B01_TheHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        frame = card_bg(7.2, 3.6, stroke_color=PALETTE["border"])
        vignette = RoundedRectangle(corner_radius=0.1, width=7.0, height=3.4,
                                     fill_color=PALETTE["ink"], fill_opacity=0.04, stroke_width=0)

        motifs = VGroup(_skyline(), _waves(), _flame()).arrange(RIGHT, buff=0.7)
        motifs.scale_to_fit_width(6.0)
        motifs.move_to(frame.get_center() + UP * 0.35)

        stock_tag = Text("STOCK FOOTAGE", color=PALETTE["dim"], font_size=14)
        stock_tag.move_to(frame.get_top() + DOWN * 0.35)

        scene_group = VGroup(frame, vignette, motifs, stock_tag)
        scene_group.move_to(UP * 0.6)

        frame.stretch(0.01, 0)
        self.play(frame.animate.stretch_to_fit_width(7.2), FadeIn(vignette), run_time=0.6)
        self.play(FadeIn(stock_tag), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in motifs], lag_ratio=0.25), run_time=0.9)

        caption = Text("5 FACTS ABOUT MONEY\nNOBODY TELLS YOU", color=PALETTE["accent"],
                        font_size=26, weight="BOLD", line_spacing=1.2, should_center=True)
        caption.move_to(frame.get_bottom() + UP * 0.55)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        tag = Text("no face · no name", color=PALETTE["dim"], font_size=16)
        tag.next_to(frame, DOWN, buff=0.35)
        self.play(FadeIn(tag), run_time=0.4)
        self.wait(1.3)


def _flow_node(label, w=2.0, h=1.0, fs=14):
    box = card_bg(w, h)
    txt = Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.15, should_center=True)
    return VGroup(box, txt.move_to(box.get_center()))


class B02_TheStrategy(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        labels = ["Topic", "Script", "AI Voice", "Stock\nFootage", "Post"]
        nodes = VGroup(*[_flow_node(lbl) for lbl in labels])
        nodes.arrange(RIGHT, buff=0.45).move_to(UP * 0.3)

        for n in nodes:
            n[0].stretch(0.01, 0)
        arrows = VGroup()
        for i, n in enumerate(nodes):
            self.play(n[0].animate.stretch_to_fit_width(2.0), FadeIn(n[1]), run_time=0.4)
            if i < len(nodes) - 1:
                a = Arrow(n[0].get_right(), nodes[i + 1][0].get_left(),
                          color=PALETTE["accent"], stroke_width=3, buff=0.24,
                          max_tip_length_to_length_ratio=0.4)
                arrows.add(a)
                self.play(GrowArrow(a), run_time=0.2)

        no_camera = VGroup(
            Circle(radius=0.28, color=PALETTE["miss"], stroke_width=3),
            Line(LEFT * 0.2, RIGHT * 0.2, color=PALETTE["miss"], stroke_width=3).rotate(PI / 4),
            Text("camera", color=PALETTE["dim"], font_size=14),
        )
        no_camera[2].next_to(no_camera[0], DOWN, buff=0.15)
        no_camera.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(no_camera, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B03_TheVoiceGap(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        left = card_bg(3.0, 2.6, stroke_color=PALETTE["border"])
        left_wave = VGroup(*[
            Line(UP * 0.35, DOWN * 0.35, color=PALETTE["dim"], stroke_width=3)
            for _ in range(6)
        ]).arrange(RIGHT, buff=0.14)
        left_label = Text("\"GPS voice\"", color=PALETTE["dim"], font_size=17)
        left_cost = Text("real $ · real time", color=PALETTE["miss"], font_size=14)
        left_inner = VGroup(left_wave, left_label, left_cost).arrange(DOWN, buff=0.28)

        right = card_bg(3.0, 2.6, stroke_color=PALETTE["accent"])
        right_wave = VGroup(*[
            Line(UP * (0.15 + 0.25 * np.sin(i)), DOWN * (0.15 + 0.25 * np.sin(i)),
                 color=PALETTE["accent"], stroke_width=3)
            for i in range(6)
        ]).arrange(RIGHT, buff=0.14)
        right_label = Text("passes as human", color=PALETTE["ink"], font_size=17)
        right_cost = Text("$ per minute", color=PALETTE["good"], font_size=14)
        right_inner = VGroup(right_wave, right_label, right_cost).arrange(DOWN, buff=0.28)

        row = VGroup(left, right).arrange(RIGHT, buff=0.6).move_to(UP * 0.3)
        left_inner.move_to(left.get_center())
        right_inner.move_to(right.get_center())

        left.stretch(0.01, 0)
        right.stretch(0.01, 0)
        self.play(left.animate.stretch_to_fit_width(3.0), FadeIn(left_inner), run_time=0.6)
        self.play(right.animate.stretch_to_fit_width(3.0), FadeIn(right_inner), run_time=0.6)

        arrow = Arrow(left.get_right(), right.get_left(), color=PALETTE["dim"],
                      stroke_width=3, buff=0.1, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(arrow), run_time=0.4)

        note = Text("now: paying to beat detection", color=PALETTE["dim"], font_size=16)
        note.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


def _niche_card(label, w=1.9, h=1.6, fs=15):
    box = card_bg(w, h)
    txt = Text(label, color=PALETTE["ink"], font_size=fs, line_spacing=1.15, should_center=True)
    return VGroup(box, txt.move_to(box.get_center()))


class B04_WhereItPays(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        labels = ["Personal\nFinance", "Tech &\nAI News", "True\nCrime", "Psychology", "Self-\nImprovement"]
        cards = VGroup(*[_niche_card(lbl) for lbl in labels])
        cards.arrange(RIGHT, buff=0.28).move_to(UP * 0.3)

        for c in cards:
            c[0].stretch(0.01, 0)
        self.play(
            LaggedStart(*[c[0].animate.stretch_to_fit_width(1.9) for c in cards], lag_ratio=0.15),
            LaggedStart(*[FadeIn(c[1]) for c in cards], lag_ratio=0.15),
            run_time=1.2,
        )

        tag = Text("some of the platforms' highest ad rates", color=PALETTE["accent"], font_size=17)
        tag.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B05_TrustFinding(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        stat = Text("\"more trustworthy,\nnot less.\"", color=PALETTE["ink"], font_size=34,
                     line_spacing=1.25, should_center=True, weight="BOLD")
        rule = Line(LEFT * 1.0, RIGHT * 1.0, color=PALETTE["accent"], stroke_width=3)
        sub = Text("no personality to get distracted by —\njust the information", color=PALETTE["dim"],
                    font_size=18, line_spacing=1.3, should_center=True)

        VGroup(stat, rule, sub).arrange(DOWN, buff=0.35).move_to(UP * 0.3)

        self.play(FadeIn(stat, shift=UP * 0.15), run_time=0.8)
        grow_in(self, rule, 2.0, run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)

        flag = card_bg(6.6, 0.85, stroke_color=PALETTE["miss"])
        flag_txt = Text("sourced from AI-tool vendors — take with skepticism",
                         color=PALETTE["miss"], font_size=15)
        flag_txt.move_to(flag.get_center())
        flag_group = VGroup(flag, flag_txt).to_edge(DOWN, buff=0.6)

        flag.stretch(0.01, 0)
        self.play(flag.animate.stretch_to_fit_width(6.6), FadeIn(flag_txt), run_time=0.6)
        self.wait(1.3)


class B06_TheReframe(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("WATCH TIME", color=PALETTE["dim"], font_size=18).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.4)

        track = RoundedRectangle(corner_radius=0.15, width=6.0, height=0.55,
                                  fill_color=PALETTE["card"], fill_opacity=1,
                                  stroke_color=PALETTE["border"], stroke_width=1.5)
        fill = RoundedRectangle(corner_radius=0.15, width=6.0, height=0.55,
                                 fill_color=PALETTE["accent"], fill_opacity=1, stroke_width=0)
        fill.align_to(track, LEFT)
        meter = VGroup(track, fill).move_to(UP * 0.4)

        fill.stretch(0.01, 0)
        fill.align_to(track, LEFT)
        self.play(FadeIn(track), run_time=0.3)
        self.play(fill.animate.stretch_to_fit_width(6.0).align_to(track, LEFT), run_time=1.0)

        tags = Text("completion · saves · shares", color=PALETTE["ink"], font_size=18)
        tags.next_to(meter, DOWN, buff=0.45)
        self.play(FadeIn(tags, shift=UP * 0.1), run_time=0.5)

        no_face = VGroup(
            Circle(radius=0.26, color=PALETTE["dim"], stroke_width=2.5),
            Line(LEFT * 0.19, RIGHT * 0.19, color=PALETTE["miss"], stroke_width=3).rotate(PI / 4),
        )
        no_face_label = Text("not a face", color=PALETTE["dim"], font_size=15)
        no_face_group = VGroup(no_face, no_face_label).arrange(DOWN, buff=0.15)
        no_face_group.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(no_face_group, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


class B07_ClosingQuestion(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        l1 = Text("A voice we can't verify.", color=PALETTE["ink"], font_size=30)
        l2 = Text("Facts we haven't checked.", color=PALETTE["ink"], font_size=30)
        l3 = Text("Hasn't been wrong yet.", color=PALETTE["accent"], font_size=30)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(l3, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
