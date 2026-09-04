"""
Manim scenes for claude-liam-kv-cache ("Claude, Cached.")
B01_BLUF        — the one-breath executive summary, text only
B02_Framework   — every token makes a Key + Value; the past never changes
B03_Prefill     — the whole prompt's K/V computed in one parallel pass
B04_Decode      — one new token at a time, attends to the whole cache
B05_Growth      — falsifiability: the cache grows with every token/layer/head
"""

from manim import *

INK = "#3D3929"
BG = "#FAF9F5"
ACCENT = "#D97757"
BLUE = "#5B7B9C"
GREEN = "#4A7C59"
RED = "#C0392B"

config.background_color = BG


def token_square(label, color=BLUE, size=0.55):
    sq = Square(side_length=size, color=color, fill_color=color, fill_opacity=0.15, stroke_width=2)
    txt = Text(label, font_size=20, color=INK).move_to(sq.get_center())
    return VGroup(sq, txt)


class B01_BLUF(Scene):
    def construct(self):
        l1 = Text("Attention needs every past token's Key and Value.",
                   font_size=38, color=INK)
        l2 = Text("Those never change once computed — so cache them.",
                   font_size=38, color=INK)
        l3 = Text("Each new token computes only its OWN K/V.",
                   font_size=36, color=ACCENT)
        for _l in (l1, l2, l3):
            if _l.width > 12.0:
                _l.scale_to_fit_width(12.0)
        l1.move_to(UP * 1.3)
        l2.move_to(UP * 0.1)
        l3.move_to(DOWN * 1.1)
        self.play(Write(l1), run_time=1.4)
        self.play(Write(l2), run_time=1.4)
        self.play(Write(l3), run_time=1.2)
        self.wait(1.2)


class B02_Framework(Scene):
    def construct(self):
        title = Text("Every token makes a Key + Value", font_size=34, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        labels = ["The", "cat", "sat", "down"]
        tokens = VGroup(*[token_square(t) for t in labels]).arrange(RIGHT, buff=0.6)
        tokens.move_to(UP * 0.8)
        self.play(*[FadeIn(t, shift=UP * 0.3) for t in tokens], run_time=1.0)

        kv_row = VGroup()
        for tok in tokens:
            kv = Rectangle(width=0.55, height=0.35, color=GREEN, fill_color=GREEN,
                            fill_opacity=0.25, stroke_width=2)
            kv.next_to(tok, DOWN, buff=0.5)
            kv_row.add(kv)
        kv_label = Text("K, V per token", font_size=24, color=GREEN)
        kv_label.next_to(kv_row, DOWN, buff=0.3)
        self.play(*[FadeIn(kv, shift=DOWN * 0.2) for kv in kv_row], run_time=1.0)
        self.play(FadeIn(kv_label), run_time=0.6)

        cap = Text("The future never changes the past — safe to reuse.",
                    font_size=26, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.4)


class B03_Prefill(Scene):
    def construct(self):
        title = Text("Prefill: the whole prompt, one parallel pass", font_size=30, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.9)

        labels = ["The", "cat", "sat", "down", "on", "the"]
        tokens = VGroup(*[token_square(t, color=ACCENT) for t in labels]).arrange(RIGHT, buff=0.35)
        tokens.move_to(UP * 0.6)
        self.play(*[FadeIn(t) for t in tokens], run_time=0.3)

        kv_row = VGroup()
        for tok in tokens:
            kv = Rectangle(width=0.5, height=0.3, color=GREEN, fill_color=GREEN,
                            fill_opacity=0.3, stroke_width=2)
            kv.next_to(tok, DOWN, buff=0.5)
            kv_row.add(kv)
        # all computed AT ONCE — the parallel pass
        self.play(*[FadeIn(kv, scale=1.3) for kv in kv_row], run_time=0.6)
        cache_label = Text("all Keys/Values computed simultaneously", font_size=24, color=GREEN)
        cache_label.next_to(kv_row, DOWN, buff=0.35)
        self.play(FadeIn(cache_label), run_time=0.6)

        cap = Text("This big parallel matmul is the 'thinking' pause.",
                    font_size=26, color=ACCENT).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.4)


class B04_Decode(Scene):
    def construct(self):
        title = Text("Decode: one new token, attends to the cache", font_size=30, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.9)

        labels = ["The", "cat", "sat", "down", "on", "the"]
        tokens = VGroup(*[token_square(t, color=BLUE) for t in labels]).arrange(RIGHT, buff=0.35)
        tokens.move_to(UP * 0.9)
        cache = VGroup()
        for tok in tokens:
            kv = Rectangle(width=0.5, height=0.3, color=GREEN, fill_color=GREEN,
                            fill_opacity=0.3, stroke_width=2).next_to(tok, DOWN, buff=0.4)
            cache.add(kv)
        self.add(tokens, cache)

        new_tok = token_square("mat", color=ACCENT)
        new_tok.next_to(tokens, RIGHT, buff=0.35)
        self.play(FadeIn(new_tok, shift=LEFT * 0.3), run_time=0.6)

        # query arrow sweeps across the cached K/V
        q_arrow = Arrow(new_tok.get_bottom(), cache[0].get_center(), color=ACCENT,
                         stroke_width=3, buff=0.1)
        self.play(Create(q_arrow), run_time=0.5)
        for kv in cache[1:]:
            new_arrow = Arrow(new_tok.get_bottom(), kv.get_center(), color=ACCENT,
                               stroke_width=3, buff=0.1)
            self.play(Transform(q_arrow, new_arrow), run_time=0.15)
        self.play(FadeOut(q_arrow), run_time=0.3)

        new_kv = Rectangle(width=0.5, height=0.3, color=RED, fill_color=RED,
                            fill_opacity=0.3, stroke_width=2).next_to(new_tok, DOWN, buff=0.4)
        self.play(FadeIn(new_kv, scale=1.3), run_time=0.5)
        cap = Text("One new K/V appended. Nothing else recomputed.",
                    font_size=26, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.7)
        self.wait(1.4)


class B05_Growth(Scene):
    def construct(self):
        title = Text("The cache only ever grows", font_size=32, color=INK).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        axes = Axes(x_range=[0, 10, 2], y_range=[0, 6, 2],
                    x_length=7.5, y_length=3.6,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to(DOWN * 0.4)
        x_label = Text("tokens generated", font_size=22, color=INK).next_to(axes, DOWN, buff=0.25)
        y_label = Text("cache size", font_size=22, color=INK).next_to(axes, LEFT, buff=0.2).rotate(PI / 2)
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.5)

        line = axes.plot(lambda x: 0.55 * x, x_range=[0, 9], color=RED, stroke_width=5)
        self.play(Create(line), run_time=1.2)

        ceiling = DashedLine(axes.c2p(0, 5.2), axes.c2p(9.4, 5.2), color=ACCENT, stroke_width=3)
        ceiling_label = Text("GPU memory limit", font_size=22, color=ACCENT)
        ceiling_label.next_to(ceiling, UP, buff=0.1).align_to(ceiling, RIGHT)
        self.play(Create(ceiling), FadeIn(ceiling_label), run_time=0.8)

        cap = Text("Linear in tokens x layers x heads — why long context is expensive.",
                    font_size=24, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.4)
