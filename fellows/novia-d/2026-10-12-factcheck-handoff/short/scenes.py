"""
Portrait 9:16 Manim for factcheck-handoff short.

9:16 Manim frame is ~4.5×8. GATE W: never put the unit name on a slide.
GATE B: stroke_opacity=0.
"""
from manim import *

PALETTE = {
    "bg": "#FAF9F5",
    "ink": "#3D3929",
    "accent": "#D97757",
    "mute": "#8B8878",
}


def _title(text, toy):
    t = Text(text, color=PALETTE["ink"], font_size=18)
    t.to_edge(UP, buff=0.55)
    s = Text(toy, color=PALETTE["mute"], font_size=11)
    s.next_to(t, DOWN, buff=0.08)
    return t, s


class B09_ZeroNotSafe(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("Zero Is Not Safe", "AI-Only second read is required")
        self.add(title, toy)

        first = Text("0 issues", color=PALETTE["ink"], font_size=36)
        first_sub = Text("out of 1,599 sentences", color=PALETTE["mute"], font_size=14)
        top = VGroup(first, first_sub).arrange(DOWN, buff=0.10).move_to(UP * 1.55)
        self.play(FadeIn(top), run_time=0.50)

        then = Text("then a real re-check", color=PALETTE["mute"], font_size=14)
        then.next_to(top, DOWN, buff=0.40)
        self.play(FadeIn(then), run_time=0.30)

        found = Text("26 genuine problems", color=PALETTE["accent"], font_size=22)
        found.next_to(then, DOWN, buff=0.28)
        self.play(Write(found), run_time=0.50)

        foot = Text("A zero is not automatically safe.",
                    color=PALETTE["ink"], font_size=13)
        foot.to_edge(DOWN, buff=0.55)
        self.play(Write(foot), run_time=0.35)
        self.wait(10.0)


class B12_WhatIsDone(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("What Is Done", "as of 2026-10-12")
        self.add(title, toy)

        big = Text("36", color=PALETTE["accent"], font_size=64)
        sub = Text("packages · current format", color=PALETTE["ink"], font_size=16)
        mid = VGroup(big, sub).arrange(DOWN, buff=0.16).move_to(ORIGIN)
        self.play(FadeIn(big), run_time=0.40)
        self.play(FadeIn(sub), run_time=0.30)

        foot = Text("All thirty-six are on the current format.",
                    color=PALETTE["ink"], font_size=13)
        foot.to_edge(DOWN, buff=0.55)
        self.play(Write(foot), run_time=0.35)
        self.wait(10.0)
