"""
Manim scenes for rag-pdf-pytorch (cli-explainer: RAG over PDFs with PyTorch).
Claude fidelity palette: cream #FAF9F5, ink #3D3929, one terracotta #D97757.

OUTPUT beats:
  B04_Embed    — PDF -> chunks -> unit vectors placed in a 2D "vector space"
  B07_Retrieve — a question vector finds its k nearest chunk vectors (top-k),
                 which ground the answer with a citation.

Coordinates kept inside SAFE (±6.3 x, ±3.4 y); type sized to fill the canvas.
Scenes auto-fill to measured narration length via _fill() (audio is the clock).
"""

from manim import *

BG = "#FAF9F5"
INK = "#3D3929"
ACCENT = "#D97757"
MUTE = "#8A8578"
GOOD = "#4A7C59"
LINE = "#B8B0A0"


def _bg(scene):
    scene.camera.background_color = BG


# Measured narration lengths (mp3/timings.json) — set after audio generation.
TARGET = {
    "B01_Problem": 20.61,
    "B04_Embed": 15.79,
    "B07_Retrieve": 20.76,
    "B08_Summary": 18.22,
}


def _fill(scene, key, tail=1.0):
    try:
        elapsed = scene.renderer.time
    except Exception:
        elapsed = 0.0
    scene.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _pdf_icon(x, y, label):
    page = Rectangle(width=1.5, height=1.9, fill_color="#FFFFFF", fill_opacity=1.0,
                     stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    lines = VGroup(*[
        Line([x - 0.5, y + 0.55 - i * 0.28, 0], [x + 0.5, y + 0.55 - i * 0.28, 0],
             color=MUTE, stroke_width=3) for i in range(5)
    ])
    tag = Text(label, color=INK, font_size=24).next_to(page, DOWN, buff=0.2)
    return VGroup(page, lines, tag)


class B04_Embed(Scene):
    """PDF -> chunks -> vectors in space."""

    def construct(self):
        _bg(self)
        title = Text("Chunk, Then Embed", color=INK, font_size=56,
                     weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.8)

        pdf = _pdf_icon(-5.0, 0.4, "paper.pdf")
        self.play(FadeIn(pdf, shift=RIGHT * 0.2), run_time=0.7)
        self.wait(1.8)

        # chunks
        a1 = Arrow([-4.1, 0.4, 0], [-3.2, 0.4, 0], color=ACCENT, stroke_width=6, buff=0.1)
        chunks = VGroup()
        for i in range(4):
            c = Rectangle(width=2.0, height=0.62, fill_color=INK, fill_opacity=0.12,
                          stroke_color=INK, stroke_width=2.5)
            lab = Text(f"chunk {i+1}", color=INK, font_size=26)
            chunks.add(VGroup(c, lab.move_to(c.get_center())))
        chunks.arrange(DOWN, buff=0.34).move_to([-2.0, 0.4, 0])
        self.play(GrowArrow(a1), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chunks],
                              lag_ratio=0.3), run_time=1.2)
        self.wait(2.2)

        # vector space
        frame = Rectangle(width=4.6, height=4.2, stroke_color=LINE, stroke_width=3,
                          fill_opacity=0).move_to([3.4, -0.15, 0])
        vs_lab = Text("vector space", color=MUTE, font_size=24).next_to(frame, UP, buff=0.12)
        a2 = Arrow([-1.15, 0.4, 0], [1.0, 0.1, 0], color=ACCENT, stroke_width=6, buff=0.1)
        self.play(Create(frame), FadeIn(vs_lab), GrowArrow(a2), run_time=0.7)

        pts = [[2.4, 1.0, 0], [4.3, 1.4, 0], [2.8, -0.9, 0], [4.6, -0.6, 0]]
        dots = VGroup(*[Dot(p, color=INK, radius=0.19) for p in pts])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.3),
                  run_time=1.2)
        self.wait(2.0)

        cap = Text("each chunk → a 384-dim vector  (shown in 2D)", color=INK,
                   font_size=36, weight="BOLD").move_to([0, -3.15, 0])
        self.play(Write(cap), run_time=0.7)
        _fill(self, "B04_Embed")


class B07_Retrieve(Scene):
    """Query vector -> k nearest chunks -> grounded answer."""

    def construct(self):
        _bg(self)
        title = Text("Retrieve the Nearest Chunks", color=INK, font_size=52,
                     weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.8)

        frame = Rectangle(width=5.2, height=4.4, stroke_color=LINE, stroke_width=3,
                          fill_opacity=0).move_to([-3.0, -0.2, 0])
        self.play(Create(frame), run_time=0.5)

        # chunk dots (some near the query, some far)
        near = [[-3.4, 0.5, 0], [-2.2, 0.9, 0], [-3.9, -0.4, 0], [-2.4, -0.5, 0]]
        far = [[-4.6, 1.4, 0], [-1.4, -1.4, 0], [-4.4, -1.5, 0]]
        near_dots = VGroup(*[Dot(p, color=INK, radius=0.13) for p in near])
        far_dots = VGroup(*[Dot(p, color=MUTE, radius=0.12) for p in far])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in [*near_dots, *far_dots]],
                              lag_ratio=0.15), run_time=1.0)
        self.wait(1.6)

        # query vector
        q = [-3.0, 0.15, 0]
        q_dot = Dot(q, color=ACCENT, radius=0.18)
        q_lab = Text("your question", color=ACCENT, font_size=26, weight="BOLD").next_to(
            q_dot, DOWN, buff=0.15)
        self.play(GrowFromCenter(q_dot), Write(q_lab), run_time=0.7)
        self.wait(2.0)

        # connect to k nearest
        links = VGroup(*[Line(q, p, color=ACCENT, stroke_width=3) for p in near])
        rings = VGroup(*[Circle(radius=0.26, color=ACCENT, stroke_width=3).move_to(p)
                         for p in near])
        self.play(LaggedStart(*[Create(l) for l in links], lag_ratio=0.2), run_time=1.0)
        self.play(*[Create(r) for r in rings], run_time=0.6)
        k_lab = Text("top-4 by cosine similarity", color=INK, font_size=26).next_to(
            frame, DOWN, buff=0.2)
        self.play(FadeIn(k_lab), run_time=0.4)
        self.wait(2.2)

        # grounded answer card
        card = Rectangle(width=4.4, height=2.3, fill_color="#FFFFFF", fill_opacity=1.0,
                         stroke_color=ACCENT, stroke_width=3).move_to([3.2, 0.3, 0])
        ans = Text("grounded answer", color=INK, font_size=30, weight="BOLD").move_to([3.2, 0.85, 0])
        body = Text("built only from the\ntop chunks", color=MUTE, font_size=24,
                    line_spacing=0.8).move_to([3.2, 0.15, 0])
        cite = Text("— source: paper.pdf, p.7", color=ACCENT, font_size=24).move_to([3.2, -0.55, 0])
        a3 = Arrow([-0.3, 0.0, 0], [0.95, 0.2, 0], color=ACCENT, stroke_width=6, buff=0.1)
        self.play(GrowArrow(a3), FadeIn(card), run_time=0.6)
        self.play(Write(ans), FadeIn(body), run_time=0.6)
        self.play(FadeIn(cite, shift=UP * 0.1), run_time=0.5)

        cap = Text("the model answers from YOUR pdf — with a citation", color=INK,
                   font_size=30, weight="BOLD").move_to([0, -3.2, 0])
        self.play(Write(cap), run_time=0.7)
        _fill(self, "B07_Retrieve")


class B01_Problem(Scene):
    """The model never read your PDF: two failure modes -> RAG."""

    def construct(self):
        _bg(self)
        title = Text("The Model Never Read Your PDF", color=INK, font_size=42,
                     weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.6)

        ask = Text("you ask about YOUR document…", color=INK, font_size=32).move_to([0, 2.0, 0])
        self.play(FadeIn(ask), run_time=0.5)
        self.wait(1.8)

        def card(x, head, body, col):
            box = Rectangle(width=5.0, height=2.2, fill_color=col, fill_opacity=0.28,
                            stroke_color=col, stroke_width=4).move_to([x, 0.15, 0])
            h = Text(head, color=INK, font_size=34, weight="BOLD").move_to([x, 0.65, 0])
            b = Text(body, color=INK, font_size=26).move_to([x, -0.3, 0])
            return VGroup(box, h, b)

        c1 = card(-2.9, "\"I don't know.\"", "it never saw the file", MUTE)
        c2 = card(2.9, "a confident answer", "…that is simply wrong", "#C0392B")
        self.play(FadeIn(c1, shift=UP * 0.15), run_time=0.6)
        self.wait(1.8)
        self.play(FadeIn(c2, shift=UP * 0.15), run_time=0.6)
        self.wait(2.2)

        fix = Text("RAG: give it the passages.", color=ACCENT,
                   font_size=40, weight="BOLD").move_to([0, -2.9, 0])
        self.play(Write(fix), run_time=0.8)
        _fill(self, "B01_Problem")


class B08_Summary(Scene):
    """Recap chain: chunk -> embed -> retrieve -> ground."""

    def construct(self):
        _bg(self)
        title = Text("The Whole Pipeline", color=INK, font_size=56,
                     weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.6)

        stages = ["chunk", "embed", "retrieve", "ground"]
        chips = VGroup()
        for s in stages:
            box = RoundedRectangle(width=2.5, height=1.7, corner_radius=0.16,
                                   fill_color=INK, fill_opacity=0.16,
                                   stroke_color=INK, stroke_width=4)
            t = Text(s, color=INK, font_size=38, weight="BOLD").move_to(box.get_center())
            chips.add(VGroup(box, t))
        chips.arrange(RIGHT, buff=0.3).move_to([0, 0.4, 0])

        for i, chip in enumerate(chips):
            self.play(FadeIn(chip, shift=RIGHT * 0.15), run_time=0.45)
            if i < len(chips) - 1:
                arr = Arrow(chips[i].get_right(), chips[i + 1].get_left(),
                            color=ACCENT, stroke_width=7, buff=0.1,
                            max_tip_length_to_length_ratio=0.4)
                self.play(GrowArrow(arr), run_time=0.3)
            self.wait(1.4)

        punch = Text("answers from evidence — not memory", color=ACCENT,
                     font_size=40, weight="BOLD").move_to([0, -2.7, 0])
        self.play(Write(punch), run_time=0.8)
        _fill(self, "B08_Summary")
