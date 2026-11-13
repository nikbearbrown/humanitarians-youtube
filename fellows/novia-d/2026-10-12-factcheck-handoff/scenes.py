"""
Manim scenes for factcheck-handoff.

Counts from SOURCE.md. GATE W: never put the unit name on a slide.
GATE B: stroke_opacity=0; counts sit next_to(track, RIGHT).
"""
from manim import *

PALETTE = {
    "bg": "#FAF9F5",
    "ink": "#3D3929",
    "accent": "#D97757",
    "mute": "#8B8878",
}


def _title(text, toy):
    t = Text(text, color=PALETTE["ink"], font_size=28)
    t.to_edge(UP, buff=0.62)
    s = Text(toy, color=PALETTE["mute"], font_size=15)
    s.next_to(t, DOWN, buff=0.10)
    return t, s


class B09_ZeroNotSafe(Scene):
    """AI-Only second read is required — 0 of 1599, then 26."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("Zero Is Not Safe", "AI-Only second read is required")
        self.add(title, toy)

        first = Text("0 issues", color=PALETTE["ink"], font_size=52)
        first_sub = Text("out of 1,599 sentences", color=PALETTE["mute"], font_size=22)
        top = VGroup(first, first_sub).arrange(DOWN, buff=0.12).move_to(UP * 0.85)
        self.play(FadeIn(top), run_time=0.55)

        then = Text("then a real re-check", color=PALETTE["mute"], font_size=20)
        then.next_to(top, DOWN, buff=0.55)
        self.play(FadeIn(then), run_time=0.35)

        found = Text("26 genuine problems", color=PALETTE["accent"], font_size=40)
        found.next_to(then, DOWN, buff=0.35)
        self.play(Write(found), run_time=0.55)

        foot = Text("A zero is not automatically safe to trust.", color=PALETTE["ink"], font_size=20)
        foot.to_edge(DOWN, buff=0.52)
        self.play(Write(foot), run_time=0.4)
        self.wait(10.0)


class B12_WhatIsDone(Scene):
    """Package status. Name the topic, not the file number."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("What Is Done", "as of 2026-10-12")
        self.add(title, toy)

        big = Text("36", color=PALETTE["accent"], font_size=96)
        sub = Text("packages · current format", color=PALETTE["ink"], font_size=28)
        mid = VGroup(big, sub).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        self.play(FadeIn(big), run_time=0.45)
        self.play(FadeIn(sub), run_time=0.35)

        foot = Text("All thirty-six are on the current format.",
                    color=PALETTE["ink"], font_size=20)
        foot.to_edge(DOWN, buff=0.52)
        self.play(Write(foot), run_time=0.4)
        self.wait(10.0)
