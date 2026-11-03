"""scenes.py — Manim scenes for claude-liam-context-window.

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757 (ONE accent per scene).
Illustrative token counts only — never presented as measured/real API output
(see SOURCES.md). No slant=ITALIC on multi-word text (Pango collapses spaces).
"""
from manim import *

BG    = ManimColor("#FAF9F5")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all body text
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#6E6A57")   # secondary / muted text
GHOST = ManimColor("#A8A491")   # dimmed / placeholder
CARD  = ManimColor("#FFFFFF")   # white card surface


def _label(text, size=28, color=None, weight=None):
    kw = {"font_size": size, "color": color or INK, "font": "EB Garamond"}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


class B04_TokenSplit(Scene):
    """Tokens are word-fragments, not words. 'context' -> 1 token,
    'windowing' -> 'window' + 'ing' -> 2 tokens. A running total bar
    fills the lower canvas so the beat isn't just two floating words."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Tokens, Not Words", size=34, weight="BOLD").to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.6)

        # ── running total bar, bottom of frame — fills the lower canvas ──
        bar_bg = Rectangle(width=8.4, height=0.5, color=GHOST, stroke_width=1.5,
                            fill_color=GHOST, fill_opacity=0.15).shift(DOWN * 2.5)
        bar_label = _label("Running total", size=20, color=SOFT).next_to(bar_bg, UP, buff=0.22).align_to(bar_bg, LEFT)
        bar_fill = Rectangle(width=0.01, height=0.5, color=INK, stroke_width=0,
                              fill_color=INK, fill_opacity=0.85).move_to(bar_bg).align_to(bar_bg, LEFT)
        bar_count = _label("0 tokens", size=26, color=INK, weight="BOLD").next_to(bar_bg, RIGHT, buff=0.35)
        self.play(Create(bar_bg), FadeIn(bar_label), FadeIn(bar_count), run_time=0.4)

        # ── "context" → one token ───────────────────────────────────────
        word1 = _label("context", size=64).shift(UP * 1.7 + LEFT * 3.6)
        self.play(FadeIn(word1), run_time=0.5)

        box1 = SurroundingRectangle(word1, color=INK, stroke_width=3.5, buff=0.26)
        counter1 = _label("1 token", size=24, color=INK).next_to(box1, DOWN, buff=0.32)
        new_fill1 = Rectangle(width=8.4 / 3, height=0.5, color=INK, stroke_width=0,
                               fill_color=INK, fill_opacity=0.85).move_to(bar_bg).align_to(bar_bg, LEFT)
        new_count1 = _label("1 token", size=26, color=INK, weight="BOLD").next_to(bar_bg, RIGHT, buff=0.35)
        self.play(Create(box1), FadeIn(counter1), run_time=0.7)
        self.play(Transform(bar_fill, new_fill1), Transform(bar_count, new_count1), run_time=0.4)

        # ── "windowing" → "window" + "ing" → two tokens ─────────────────
        word2 = _label("windowing", size=64).shift(UP * 1.7 + RIGHT * 3.4)
        self.play(FadeIn(word2), run_time=0.5)

        part_a = _label("window", size=64).move_to(word2).shift(LEFT * 1.4)
        part_b = _label("ing", size=64, color=INK).move_to(word2).shift(RIGHT * 1.75)
        self.remove(word2)
        self.add(part_a, part_b)

        box2a = SurroundingRectangle(part_a, color=INK, stroke_width=3, buff=0.22)
        box2b = SurroundingRectangle(part_b, color=INK, stroke_width=3, buff=0.22)
        counter2 = _label("2 tokens", size=24, color=INK).next_to(
            VGroup(box2a, box2b), DOWN, buff=0.32
        )
        new_fill2 = Rectangle(width=8.4, height=0.5, color=INK, stroke_width=0,
                               fill_color=INK, fill_opacity=0.85).move_to(bar_bg).align_to(bar_bg, LEFT)
        new_count2 = _label("3 tokens", size=26, color=INK, weight="BOLD").next_to(bar_bg, RIGHT, buff=0.35)
        self.play(Create(box2a), Create(box2b), FadeIn(counter2), run_time=0.7)
        self.play(Transform(bar_fill, new_fill2), Transform(bar_count, new_count2), run_time=0.4)
        self.wait(0.6)
