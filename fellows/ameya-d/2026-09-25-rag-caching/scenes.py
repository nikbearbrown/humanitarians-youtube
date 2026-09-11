"""
Manim scenes for rag-caching (RAG series — caching layers + invalidation).
Claude fidelity palette. Grounded in PRODUCTION_NOTES.md §3 & §5 (cache hit 0.002ms).
Coordinates within SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_Waste": 20.35, "B02_Exact": 18.88, "B03_Semantic": 17.73,
          "B04_Layers": 18.84, "B05_Danger": 18.77, "B06_Invalidate": 21.18, "B08_CostOrder": 19.05}


def _bg(s): s.camera.background_color = BG


def _fill(s, key, tail=1.0):
    try:
        elapsed = s.renderer.time
    except Exception:
        elapsed = 0.0
    s.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _title(txt, size=46):
    return Text(txt, color=INK, font_size=size, weight="BOLD").to_edge(UP, buff=0.5)


def _chip(label, w=2.5, h=1.05, fill=INK, op=0.10, fs=30, tcol=INK):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.14, fill_color=fill,
                           fill_opacity=op, stroke_color=fill, stroke_width=3)
    t = Text(label, color=tcol, font_size=fs, weight="BOLD").move_to(box.get_center())
    return VGroup(box, t)


def _pipeline(scene, y=0.2, dim_from=None, scale=1.0):
    stages = ["embed", "search", "rerank", "generate"]
    chips = VGroup(*[_chip(s, w=2.2 * scale, h=0.9 * scale, fill=INK, op=0.10, fs=int(26 * scale)) for s in stages])
    chips.arrange(RIGHT, buff=0.5).move_to([0, y, 0])
    arrs = VGroup(*[Arrow(chips[i].get_right(), chips[i + 1].get_left(), color=ACCENT, stroke_width=4, buff=0.1) for i in range(3)])
    return chips, arrs


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
        cells = VGroup(*[Text(str(c), color=INK, font_size=24, weight=("BOLD" if j > 0 else "NORMAL"),
                             font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                        for j, c in enumerate(rowv)])
        scene.play(GrowFromCenter(sw), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.6); y -= 0.72
    if note_txt:
        scene.play(Write(Text(note_txt, color=ACCENT, font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
    _fill(scene, key)


class B01_Waste(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Every Query Pays Full Price"), shift=DOWN * 0.2), run_time=0.6)
        chips, arrs = _pipeline(self, y=0.6)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in chips], lag_ratio=0.3, run_time=1.2), LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.3, run_time=1.0))
        self.play(Write(Text("~1.3 s — generation is the expensive second", color=INK, font_size=27, weight="BOLD").move_to([0, -0.8, 0])), run_time=0.7)
        self.wait(0.6)
        self.play(Write(Text("but real traffic repeats — and paraphrases too", color=ACCENT,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.6)), run_time=0.8)
        _fill(self, "B01_Waste")


class B02_Exact(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Exact Cache"), shift=DOWN * 0.2), run_time=0.6)
        q = _chip("normalized question", w=5.4, h=1.0, fill=INK, op=0.09, fs=28).move_to([0, 1.6, 0])
        ans = _chip("stored answer", w=4.2, h=1.0, fill=GOOD, op=0.14, fs=28).move_to([0, -0.2, 0])
        arr = Arrow(q.get_bottom(), ans.get_top(), color=GOOD, stroke_width=6, buff=0.15)
        self.play(FadeIn(q, shift=DOWN * 0.1), run_time=0.5)
        self.play(GrowArrow(arr), FadeIn(ans, shift=UP * 0.1), run_time=0.7)
        skip = Text("skips the ENTIRE pipeline", color=ACCENT, font_size=30, weight="BOLD").move_to([0, -1.5, 0])
        self.play(Write(skip), run_time=0.7); self.wait(0.8)
        self.play(Write(Text("~0.002 ms · fires on identical repeats", color=MUTE,
                             font_size=26).to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B02_Exact")


class B03_Semantic(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Semantic Cache"), shift=DOWN * 0.2), run_time=0.6)
        newq = _chip("\"how do margins work?\"", w=5.6, h=0.95, fill=ACCENT, op=0.13, fs=26).move_to([0, 1.7, 0])
        past = _chip("\"explain buying on margin\"  (answered)", w=7.0, h=0.95, fill=INK, op=0.09, fs=24).move_to([0, 0.2, 0])
        self.play(FadeIn(newq, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(past, shift=UP * 0.1), run_time=0.5)
        link = DoubleArrow(newq.get_bottom(), past.get_top(), color=GOOD, stroke_width=4, buff=0.12)
        sim = Text("similarity ≥ threshold → serve it", color=GOOD, font_size=26, weight="BOLD").move_to([0, -1.2, 0])
        self.play(GrowFromCenter(link), FadeIn(sim), run_time=0.7); self.wait(0.9)
        self.play(Write(Text("catches paraphrases · saves everything after embedding", color=INK,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B03_Semantic")


class B04_Layers(Scene):
    def construct(self):
        _table(self, "Four Cache Layers",
               ["layer", "keyed on", "saves"],
               [["exact", "question string", "everything"],
                ["semantic", "query embedding", "all-after-embed"],
                ["embedding", "text hash", "one embed call"],
                ["prompt / KV", "stable prefix", "~90% of input"]],
               note_txt="each layer catches a different kind of repeat",
               key="B04_Layers")


class B05_Danger(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Semantic Trap"), shift=DOWN * 0.2), run_time=0.6)
        q1 = _chip("\"is margin safe?\"", w=5.0, h=0.9, fill=INK, op=0.09, fs=26).move_to([-2.9, 1.4, 0])
        q2 = _chip("\"is margin ever safe?\"", w=5.4, h=0.9, fill=INK, op=0.09, fs=25).move_to([-2.6, 0.0, 0])
        ans = _chip("same cached answer", w=4.6, h=1.2, fill=BAD, op=0.12, fs=26, tcol=BAD).move_to([3.4, 0.7, 0])
        self.play(FadeIn(q1, shift=RIGHT * 0.1), run_time=0.45)
        self.play(FadeIn(q2, shift=RIGHT * 0.1), run_time=0.45)
        self.play(GrowArrow(Arrow(q1.get_right(), ans.get_left() + [0, 0.3, 0], color=BAD, stroke_width=4, buff=0.15)),
                  GrowArrow(Arrow(q2.get_right(), ans.get_left() + [0, -0.3, 0], color=BAD, stroke_width=4, buff=0.15)),
                  FadeIn(ans), run_time=0.8)
        self.play(Write(Text("threshold too loose → the wrong answer, confidently", color=BAD,
                             font_size=27, weight="BOLD").move_to([0, -1.5, 0])), run_time=0.8)
        self.wait(0.6)
        self.play(Write(Text("evaluate it with the same rigor as retrieval", color=MUTE,
                             font_size=25, slant="ITALIC").to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B05_Danger")


class B06_Invalidate(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Invalidation — The Hard Part"), shift=DOWN * 0.2), run_time=0.6)
        doc = _chip("doc_014  amended", w=4.4, h=1.0, fill=ACCENT, op=0.14, fs=28).move_to([0, 1.7, 0])
        self.play(FadeIn(doc, shift=DOWN * 0.1), run_time=0.5)
        cached = VGroup(*[_chip(f"answer {i+1}", w=2.4, h=0.8, fill=BAD, op=0.10, fs=22, tcol=BAD) for i in range(3)])
        cached.arrange(RIGHT, buff=0.5).move_to([0, 0.2, 0])
        arrs = VGroup(*[Arrow(doc.get_bottom(), c.get_top(), color=BAD, stroke_width=3, buff=0.12) for c in cached])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.2, run_time=0.8), LaggedStart(*[FadeIn(c) for c in cached], lag_ratio=0.2, run_time=0.8))
        self.play(Write(Text("all now stale — and served with confidence", color=BAD, font_size=26, weight="BOLD").move_to([0, -1.1, 0])), run_time=0.7)
        self.wait(0.5)
        self.play(Write(Text("defend with TTL, or tag by source-id and purge on update", color=INK,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B06_Invalidate")


class B08_CostOrder(Scene):
    def construct(self):
        _table(self, "Cost Levers, In Order",
               ["#", "lever"],
               [["1", "cache (exact + semantic)"],
                ["2", "route to a cheaper model"],
                ["3", "trim retrieved context"],
                ["4", "prompt-cache the prefix"]],
               note_txt="cache is first — nothing beats work you don't do",
               key="B08_CostOrder")
