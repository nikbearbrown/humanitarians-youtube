"""
Portrait 9:16 Manim for chapter14-second-read short.

B04_FirstPass only — B07 (editorial/reread) is dropped with the revision cycle.
9:16 frame is ~4.5×8; landscape bar_w=7.2 will not fit.
Hardcoded positions so GATE A (16:9 stub frame ±7.1×±4.0) stays in bounds.
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

        title = Text("The Split — Who Went Where", color=PALETTE["ink"], font_size=22)
        title.to_edge(UP, buff=0.65)
        toy = Text("STEP 2  ·  web-flagged vs AI-only", color=PALETTE["mute"], font_size=12)
        toy.next_to(title, DOWN, buff=0.10)
        self.add(title, toy)

        left_n = Text("92", color=PALETTE["accent"], font_size=42)
        left_l = Text("AI-only", color=PALETTE["ink"], font_size=15)
        left = VGroup(left_n, left_l).arrange(DOWN, buff=0.06)

        right_n = Text("46", color=PALETTE["ink"], font_size=42)
        right_l = Text("web-flagged", color=PALETTE["ink"], font_size=15)
        right = VGroup(right_n, right_l).arrange(DOWN, buff=0.06)

        heads = VGroup(left, right).arrange(RIGHT, buff=0.70)
        heads.move_to([0, 2.15, 0])
        self.play(FadeIn(heads), run_time=0.6)

        max_n = 33
        bar_w = 2.28
        bar_h = 0.30
        start_y = 1.45
        spacing = 0.58
        left_x = -0.72

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
                width=max(w, 0.08), height=bar_h,
                fill_color=PALETTE["accent"], fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0,
            )
            bar.align_to(track, LEFT).align_to(track, UP)
            row = Text(label, color=PALETTE["ink"], font_size=13)
            row.next_to(track, LEFT, buff=0.12)
            count = Text(str(n), color=PALETTE["ink"], font_size=13)
            count.next_to(track, RIGHT, buff=0.12)
            self.add(track, row)
            self.play(FadeIn(bar), run_time=0.28)
            self.play(FadeIn(count), run_time=0.12)

        note = VGroup(
            Text("Sheet B is this pile.", color=PALETTE["ink"], font_size=15),
            Text("Drop it and the split is invisible.", color=PALETTE["ink"], font_size=14),
        ).arrange(DOWN, buff=0.08)
        note.move_to([0, -2.55, 0])
        self.play(Write(note), run_time=0.5)
        self.wait(12.4)
