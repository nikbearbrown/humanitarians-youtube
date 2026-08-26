"""
Manim scenes for chapter14-second-read (fact-check CLI reel).

B04_FirstPass     — 92 AI-only by file; 46 web-flagged as the other pile.
B07_SecondRead    — 8 editorial + 5 hallucination flags; IL-23 inversion accent.

Counts from ch14_ledger.py (inlined so GATE A can run scenes.py alone).
Claude palette: cream #FAF9F5 / ink #3D3929 / terracotta #D97757.
"""
from manim import *

PALETTE = {
    "bg": "#FAF9F5",
    "ink": "#3D3929",
    "accent": "#D97757",
    "mute": "#8B8878",
}

BY_FILE = [
    ("Intro", 8),
    ("Components", 33),
    ("Stroma", 13),
    ("Inflammation", 17),
    ("ECM", 16),
    ("Summary", 5),
]


class B04_FirstPass(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("The Split — Who Went Where", color=PALETTE["ink"], font_size=28)
        title.to_edge(UP, buff=0.68)
        toy = Text("STEP 2  ·  web-flagged vs AI-only, by file", color=PALETTE["mute"], font_size=15)
        toy.next_to(title, DOWN, buff=0.10)
        self.add(title, toy)

        # two headline numbers
        left_n = Text("92", color=PALETTE["accent"], font_size=64)
        left_l = Text("AI-only", color=PALETTE["ink"], font_size=20)
        left = VGroup(left_n, left_l).arrange(DOWN, buff=0.08)

        right_n = Text("46", color=PALETTE["ink"], font_size=64)
        right_l = Text("web-flagged", color=PALETTE["ink"], font_size=20)
        right = VGroup(right_n, right_l).arrange(DOWN, buff=0.08)

        heads = VGroup(left, right).arrange(RIGHT, buff=2.4).move_to(UP * 1.15)
        self.play(FadeIn(heads), run_time=0.6)

        # AI-only by file — horizontal bars
        max_n = 33
        bar_w = 7.2
        bar_h = 0.32
        start_y = 0.15
        spacing = 0.48
        left_x = -2.1

        for i, (label, n) in enumerate(BY_FILE):
            y = start_y - i * spacing
            w = bar_w * (n / max_n)
            track = Rectangle(
                width=bar_w, height=bar_h,
                fill_color=PALETTE["ink"], fill_opacity=0.08,
                stroke_width=0, stroke_opacity=0,
            )
            track.move_to([left_x + bar_w / 2, y, 0])
            bar = Rectangle(
                width=w, height=bar_h,
                fill_color=PALETTE["accent"], fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0,
            )
            bar.align_to(track, LEFT).align_to(track, UP)
            row = Text(label, color=PALETTE["ink"], font_size=16).next_to(track, LEFT, buff=0.18)
            count = Text(str(n), color=PALETTE["ink"], font_size=16).next_to(track, RIGHT, buff=0.16)
            self.add(track, row)
            self.play(FadeIn(bar), run_time=0.28)
            self.play(FadeIn(count), run_time=0.12)

        note = Text("Sheet B is this pile. Drop it and the split is invisible.", color=PALETTE["ink"], font_size=20)
        note.to_edge(DOWN, buff=0.62)
        self.play(Write(note), run_time=0.5)
        self.wait(12.4)


class B07_SecondRead(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Editorial and Reread", color=PALETTE["ink"], font_size=28)
        title.to_edge(UP, buff=0.68)
        toy = Text("STEPS 3–4  ·  editorial sheet, then the 92", color=PALETTE["mute"], font_size=15)
        toy.next_to(title, DOWN, buff=0.10)
        self.add(title, toy)

        def card(kicker, number, lines, accent=False):
            plate = RoundedRectangle(
                width=5.6,
                height=4.15,
                corner_radius=0.10,
                fill_color=PALETTE["ink"],
                fill_opacity=0.07,
                stroke_width=0,
                stroke_opacity=0,
            )
            rail = Rectangle(
                width=0.10,
                height=4.15,
                fill_color=PALETTE["accent"] if accent else PALETTE["ink"],
                fill_opacity=0.95 if accent else 0.35,
                stroke_width=0,
                stroke_opacity=0,
            )
            rail.align_to(plate, LEFT)
            k = Text(kicker, color=PALETTE["mute"], font_size=14)
            n = Text(number, color=PALETTE["accent"] if accent else PALETTE["ink"], font_size=52)
            body = VGroup(*[Text(s, color=PALETTE["ink"], font_size=16) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            inner = VGroup(k, n, body).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            inner.move_to(plate.get_center() + RIGHT * 0.12 + UP * 0.08)
            return VGroup(plate, rail, inner)

        left = card(
            "Sheet C  ·  editorial",
            "8",
            [
                "redundant CAF definitions",
                "failed drugs as current",
                "90% unique vs lung desmoplasia",
                "IL-23 on two pathways",
            ],
            accent=False,
        )
        right = card(
            "Part 3  ·  of the 92",
            "5",
            [
                "DCs are not killers",
                "checkpoint blockade backwards",
                "IL-17 → IL-23 reversed",
                "that last one is the error",
            ],
            accent=True,
        )
        pair = VGroup(left, right).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        pair.move_to(DOWN * 0.12)
        self.play(FadeIn(left), run_time=0.7)
        self.play(FadeIn(right), run_time=0.7)

        foot = Text("These two moves catch what the web never saw.", color=PALETTE["ink"], font_size=20)
        foot.to_edge(DOWN, buff=0.62)
        self.play(Write(foot), run_time=0.5)
        self.wait(17.5)
