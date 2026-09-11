"""
Manim scenes for rag-embeddings (RAG series). Claude fidelity palette.
Grounded in VIDEO_SCRIPT.md SEGMENT 4. SAFE: |x|<=6.0, |y|<=3.3; auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_PerToken": 14.49, "B02_MeanPool": 17.64, "B03_Shapes": 17.49, "B04_Speedup": 15.17, "B05_SameOps": 17.3, "B06_Oven": 20.35, "B08_AtScale": 16.02}


def _bg(s): s.camera.background_color = BG


def _fill(s, key, tail=1.0):
    try:
        elapsed = s.renderer.time
    except Exception:
        elapsed = 0.0
    s.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _title(txt, size=46):
    return Text(txt, color=INK, font_size=size, weight="BOLD").to_edge(UP, buff=0.5)


def _chip(label, w=2.5, h=1.05, fill=INK, op=0.10, fs=30, tcol=INK, mono=False):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill,
                           fill_opacity=op, stroke_color=fill, stroke_width=2.5)
    t = Text(label, color=tcol, font_size=fs, weight="BOLD",
             font=("monospace" if mono else "sans-serif")).move_to(box.get_center())
    return VGroup(box, t)


def _table(scene, title_txt, headers, rows, note_txt=None, key=None):
    _bg(scene)
    scene.play(FadeIn(_title(title_txt, 44), shift=DOWN * 0.2), run_time=0.6)
    ncol = len(headers); span = 8.4 if ncol >= 3 else 6.4
    xs = [-span / 2 + i * (span / (ncol - 1)) for i in range(ncol)] if ncol > 1 else [0]
    y0 = 1.6
    hdr = VGroup(*[Text(h, color=MUTE, font_size=25, weight="BOLD").move_to([xs[i], y0, 0]) for i, h in enumerate(headers)])
    scene.play(FadeIn(hdr), run_time=0.4)
    scene.play(Create(Line([xs[0] - 0.7, y0 - 0.35, 0], [xs[-1] + 0.7, y0 - 0.35, 0], color=LINE, stroke_width=2)), run_time=0.3)
    y = y0 - 0.95
    for rowv in rows:
        sw = Square(side_length=0.28, fill_color=MUTE, fill_opacity=0.9, stroke_width=0).move_to([xs[0] - 1.15, y, 0])
        cells = VGroup(*[Text(str(c), color=INK, font_size=23, weight=("BOLD" if j > 0 else "NORMAL"),
                             font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                        for j, c in enumerate(rowv)])
        scene.play(GrowFromCenter(sw), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.55); y -= 0.72
    if note_txt:
        scene.play(Write(Text(note_txt, color=ACCENT, font_size=26, weight="BOLD").move_to([0, -3.05, 0])), run_time=0.7)
    _fill(scene, key)


class B01_PerToken(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("One Vector per Token"), shift=DOWN * 0.2), run_time=0.6)
        toks = VGroup(*[_chip(f"t{i+1}", w=0.8, h=0.7, fill=INK, op=0.12, fs=24, mono=True) for i in range(7)])
        toks.arrange(RIGHT, buff=0.22).move_to([0, 1.8, 0])
        self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.1) for t in toks], lag_ratio=0.1, run_time=0.9))
        self.play(Write(Text("tokens (7,)  →  forward pass", color=MUTE, font_size=26).move_to([0, 0.9, 0])), run_time=0.5)
        vecs = VGroup(*[RoundedRectangle(width=0.7, height=1.3, corner_radius=0.08, fill_color=ACCENT, fill_opacity=0.14, stroke_color=ACCENT, stroke_width=2) for _ in range(7)])
        vecs.arrange(RIGHT, buff=0.22).move_to([0, -0.5, 0])
        self.play(LaggedStart(*[GrowFromEdge(v, DOWN) for v in vecs], lag_ratio=0.1, run_time=1.0))
        self.play(Write(Text("per-token vectors  (7, 384)  —  NOT one per chunk", color=INK,
                             font_size=27, weight="BOLD").move_to([0, -2.4, 0])), run_time=0.8)
        _fill(self, "B01_PerToken")


class B02_MeanPool(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Mean Pooling → One Vector"), shift=DOWN * 0.2), run_time=0.6)
        vecs = VGroup(*[RoundedRectangle(width=0.6, height=1.2, corner_radius=0.08, fill_color=ACCENT, fill_opacity=0.14, stroke_color=ACCENT, stroke_width=2) for _ in range(7)])
        vecs.arrange(RIGHT, buff=0.25).move_to([-2.4, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(v) for v in vecs], lag_ratio=0.08, run_time=0.8))
        one = RoundedRectangle(width=0.7, height=1.5, corner_radius=0.08, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0).move_to([3.4, 1.2, 0])
        arrs = VGroup(*[Arrow(v.get_right(), one.get_left(), color=MUTE, stroke_width=2.5, buff=0.1) for v in vecs])
        self.play(LaggedStart(*[Create(a) for a in arrs], lag_ratio=0.05, run_time=0.9), GrowFromEdge(one, DOWN))
        self.play(Write(Text("average all 7 → (384,)  the chunk vector", color=INK, font_size=28, weight="BOLD").move_to([0, -0.8, 0])), run_time=0.8)
        self.play(Write(Text("this single vector goes into your index", color=MUTE, font_size=25, slant="ITALIC").move_to([0, -2.6, 0])), run_time=0.6)
        _fill(self, "B02_MeanPool")


class B03_Shapes(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Batch the Matrix Multiply"), shift=DOWN * 0.2), run_time=0.6)
        a = _chip("(1, 768) @ (768, 768)", w=6.2, h=1.1, fill=MUTE, op=0.16, fs=28, mono=True).move_to([0, 1.5, 0])
        al = Text("batch = 1   —   skinny", color=MUTE, font_size=24).next_to(a, DOWN, buff=0.2)
        self.play(FadeIn(a, shift=DOWN * 0.1), FadeIn(al), run_time=0.7); self.wait(0.8)
        b = _chip("(64, 768) @ (768, 768)", w=6.2, h=1.4, fill=ACCENT, op=0.14, fs=28, mono=True).move_to([0, -0.9, 0])
        bl = Text("batch = 64   —   fat, one weight matrix for all", color=ACCENT, font_size=24, weight="BOLD").next_to(b, DOWN, buff=0.2)
        self.play(FadeIn(b, shift=UP * 0.1), FadeIn(bl), run_time=0.7); self.wait(0.9)
        _fill(self, "B03_Shapes")


class B04_Speedup(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Measurement"), shift=DOWN * 0.2), run_time=0.6)
        slow = RoundedRectangle(width=8.0, height=0.9, corner_radius=0.1, fill_color=BAD, fill_opacity=0.75, stroke_width=0).move_to([0.0, 1.3, 0])
        st = Text("64 separate matmuls   —   14.924 ms", color=BG, font_size=26, weight="BOLD").move_to(slow.get_center())
        self.play(GrowFromEdge(slow, LEFT), FadeIn(st), run_time=0.8); self.wait(0.7)
        fast = RoundedRectangle(width=0.9, height=0.9, corner_radius=0.1, fill_color=GOOD, fill_opacity=0.85, stroke_width=0).move_to([-3.55, -0.2, 0])
        ft = Text("1 batched matmul   —   1.181 ms", color=INK, font_size=26, weight="BOLD").next_to(fast, RIGHT, buff=0.3)
        self.play(GrowFromEdge(fast, LEFT), FadeIn(ft, shift=RIGHT * 0.1), run_time=0.8); self.wait(0.7)
        self.play(Write(Text("12.6× faster", color=ACCENT, font_size=44, weight="BOLD").move_to([0, -1.7, 0])), run_time=0.8)
        _fill(self, "B04_Speedup")


class B05_SameOps(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Identical Arithmetic"), shift=DOWN * 0.2), run_time=0.6)
        a = _chip("looped:   75,497,472 ops", w=7.2, h=1.1, fill=INK, op=0.09, fs=28, mono=True).move_to([0, 1.3, 0])
        b = _chip("batched:  75,497,472 ops", w=7.2, h=1.1, fill=ACCENT, op=0.13, fs=28, mono=True).move_to([0, -0.2, 0])
        self.play(FadeIn(a, shift=DOWN * 0.1), run_time=0.6); self.wait(0.6)
        self.play(FadeIn(b, shift=UP * 0.1), run_time=0.6); self.wait(0.6)
        eq = Text("IDENTICAL", color=GOOD, font_size=32, weight="BOLD").move_to([0, -1.4, 0])
        self.play(FadeIn(eq, scale=1.2), run_time=0.5); self.wait(0.6)
        self.play(Write(Text("the speedup is not less math — so where did the time go?", color=INK,
                             font_size=26, weight="BOLD").move_to([0, -2.7, 0])), run_time=0.8)
        _fill(self, "B05_SameOps")


class B06_Oven(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Memory Bandwidth, Not Math"), shift=DOWN * 0.2), run_time=0.6)
        reasons = VGroup(
            Text("fixed overhead paid once, not 64 times", color=INK, font_size=28),
            Text("weight matrix loaded once, reused for all 64", color=INK, font_size=28, weight="BOLD"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, 1.4, 0])
        for r in reasons:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.7)
        oven = _chip("one oven — 1 cookie or 64, still 12 min", w=8.4, h=1.2, fill=ACCENT, op=0.13, fs=28).move_to([0, -0.7, 0])
        self.play(FadeIn(oven, shift=UP * 0.1), run_time=0.7); self.wait(0.8)
        self.play(Write(Text("the bottleneck was never the arithmetic", color=MUTE, font_size=26, slant="ITALIC").move_to([0, -2.7, 0])), run_time=0.7)
        _fill(self, "B06_Oven")


class B08_AtScale(Scene):
    def construct(self):
        _table(self, "At Index Scale",
               ["lever", "why"],
               [["batch", "biggest single win"],
                ["stream in shards", "bounded memory"],
                ["content-hash", "re-embed only changes"]],
               note_txt="batch first — it's one argument",
               key="B08_AtScale")
