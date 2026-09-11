"""
Manim scenes for llm-inference (RAG series — how generation runs).
Claude fidelity palette. Grounded in PRODUCTION_NOTES.md §4 (model dominates latency).
Coordinates within SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_Autoregress": 19.14, "B02_PrefillDecode": 18.47, "B03_KVCache": 22.91,
          "B04_Batching": 19.33, "B05_Quantize": 17.86, "B06_Speculative": 20.74, "B08_Levers": 19.95}


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
    for ri, rowv in enumerate(rows):
        sw = Square(side_length=0.28, fill_color=MUTE, fill_opacity=0.9, stroke_width=0).move_to([xs[0] - 1.15, y, 0])
        cells = VGroup(*[Text(str(c), color=INK, font_size=24, weight=("BOLD" if j > 0 else "NORMAL"),
                             font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                        for j, c in enumerate(rowv)])
        scene.play(GrowFromCenter(sw), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.6); y -= 0.72
    if note_txt:
        scene.play(Write(Text(note_txt, color=ACCENT, font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
    _fill(scene, key)


class B01_Autoregress(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("One Token at a Time"), shift=DOWN * 0.2), run_time=0.6)
        box = _chip("the model", w=2.8, h=1.3, fill=INK, op=0.09, fs=30).move_to([0, 0.6, 0])
        self.play(FadeIn(box), run_time=0.5)
        toks = VGroup(*[_chip(t, w=1.35, h=0.7, fill=ACCENT, op=0.13, fs=24) for t in ["The", "cat", "sat", "…"]])
        toks.arrange(RIGHT, buff=0.3).move_to([0, -1.4, 0])
        for i, t in enumerate(toks):
            a_out = CurvedArrow(box.get_bottom(), t.get_top(), color=ACCENT, stroke_width=4, angle=-0.6)
            self.play(GrowArrow(a_out) if False else Create(a_out), FadeIn(t), run_time=0.4)
            if i < len(toks) - 1:
                a_back = CurvedArrow(t.get_top(), box.get_bottom(), color=MUTE, stroke_width=3, angle=0.6)
                self.play(Create(a_back), run_time=0.3)
            self.wait(0.3)
        self.play(Write(Text("100 tokens = 100 forward passes, in strict sequence", color=INK,
                             font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B01_Autoregress")


class B02_PrefillDecode(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Prefill vs Decode"), shift=DOWN * 0.2), run_time=0.6)

        def panel(x, head, lines, col):
            box = RoundedRectangle(width=5.4, height=3.0, corner_radius=0.16, fill_color=col,
                                   fill_opacity=0.10, stroke_color=col, stroke_width=3).move_to([x, 0.1, 0])
            h = Text(head, color=col, font_size=32, weight="BOLD").move_to([x, 1.15, 0])
            body = VGroup(*[Text(l, color=INK, font_size=24) for l in lines]).arrange(DOWN, buff=0.28).move_to([x, -0.35, 0])
            return VGroup(box, h, body)
        left = panel(-3.1, "PREFILL", ["reads the whole prompt", "one parallel pass", "sets time-to-first-token"], INK)
        right = panel(3.1, "DECODE", ["one token at a time", "strictly serial", "the slow part"], ACCENT)
        self.play(FadeIn(left, shift=RIGHT * 0.1), run_time=0.7); self.wait(2.4)
        self.play(FadeIn(right, shift=LEFT * 0.1), run_time=0.7); self.wait(2.4)
        self.play(Write(Text("a sprint, then a long walk", color=MUTE, font_size=27, slant="ITALIC").to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B02_PrefillDecode")


class B03_KVCache(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The KV Cache"), shift=DOWN * 0.2), run_time=0.6)
        cached = VGroup(*[Square(side_length=0.7, fill_color=INK, fill_opacity=0.12, stroke_color=INK, stroke_width=2) for _ in range(6)])
        cached.arrange(RIGHT, buff=0.22).move_to([-1.3, 1.2, 0])
        lbl = Text("stored keys + values (reused)", color=MUTE, font_size=24).next_to(cached, UP, buff=0.3)
        self.play(LaggedStart(*[FadeIn(c) for c in cached], lag_ratio=0.15, run_time=1.2), FadeIn(lbl))
        newt = Square(side_length=0.7, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0).next_to(cached, RIGHT, buff=0.22)
        nl = Text("only the new token is computed", color=ACCENT, font_size=24, weight="BOLD").move_to([0, 0.05, 0])
        self.play(GrowFromCenter(newt), FadeIn(nl, shift=UP * 0.1), run_time=0.7)
        self.wait(1.0)
        comp = VGroup(
            Text("without cache:  O(n²) — re-read everything", color=BAD, font_size=27),
            Text("with cache:     O(n) — reuse the past", color=GOOD, font_size=27, weight="BOLD"),
            Text("the price: memory grows with every token", color=MUTE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1.8, 0])
        for c in comp:
            self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.5); self.wait(0.6)
        _fill(self, "B03_KVCache")


class B04_Batching(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Batching — Throughput vs Latency"), shift=DOWN * 0.2), run_time=0.6)
        reqs = VGroup(*[_chip(f"req {i+1}", w=1.9, h=0.7, fill=INK, op=0.10, fs=22) for i in range(4)])
        reqs.arrange(DOWN, buff=0.28).move_to([-4.2, 0.1, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in reqs], lag_ratio=0.2, run_time=1.0))
        gpu = _chip("one forward pass", w=3.4, h=2.6, fill=ACCENT, op=0.12, fs=28).move_to([0.4, 0.1, 0])
        arrs = VGroup(*[Arrow(r.get_right(), gpu.get_left() + [0, r.get_center()[1] - gpu.get_center()[1], 0], color=ACCENT, stroke_width=4, buff=0.15) for r in reqs])
        self.play(FadeIn(gpu), LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.15, run_time=1.0))
        out = VGroup(Text("tokens/sec ↑↑", color=GOOD, font_size=26, weight="BOLD"),
                     Text("per-user wait ↑", color=BAD, font_size=26)).arrange(DOWN, buff=0.3).move_to([4.4, 0.1, 0])
        self.play(FadeIn(out, shift=LEFT * 0.1), run_time=0.7); self.wait(1.0)
        self.play(Write(Text("throughput for the fleet vs latency for the one", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B04_Batching")


class B05_Quantize(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Quantize the Weights"), shift=DOWN * 0.2), run_time=0.6)
        bars = [("fp16", 5.4, MUTE), ("int8", 2.7, INK), ("int4", 1.35, ACCENT)]
        grp = VGroup()
        for name, w, col in bars:
            bar = RoundedRectangle(width=w, height=0.9, corner_radius=0.1, fill_color=col, fill_opacity=0.85, stroke_width=0)
            t = Text(name, color=BG, font_size=28, weight="BOLD").move_to(bar.get_left() + RIGHT * 0.7)
            grp.add(VGroup(bar, t).move_to([w / 2 - 2.7, 0, 0]))
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to([-0.4, 0.3, 0])
        for row in grp:
            self.play(GrowFromEdge(row, LEFT), run_time=0.6); self.wait(0.6)
        self.play(Write(Text("smaller · faster · cheaper hardware — small quality loss", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B05_Quantize")


class B06_Speculative(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Speculative Decoding"), shift=DOWN * 0.2), run_time=0.6)
        draft = _chip("draft model — guesses k tokens", w=7.2, h=1.0, fill=INK, op=0.09, fs=27).move_to([0, 1.5, 0])
        self.play(FadeIn(draft, shift=DOWN * 0.1), run_time=0.5)
        guesses = VGroup(*[_chip(t, w=1.3, h=0.7, fill=ACCENT, op=0.13, fs=24) for t in ["is", "a", "fast", "small"]])
        guesses.arrange(RIGHT, buff=0.3).move_to([0, 0.15, 0])
        self.play(LaggedStart(*[FadeIn(g, shift=DOWN * 0.1) for g in guesses], lag_ratio=0.2, run_time=1.0))
        target = _chip("target model — verifies all in ONE pass", w=7.2, h=1.0, fill=ACCENT, op=0.12, fs=27).move_to([0, -1.2, 0])
        arrs = VGroup(*[Arrow(g.get_bottom(), target.get_top() + [g.get_center()[0], 0, 0], color=MUTE, stroke_width=3, buff=0.12) for g in guesses])
        self.play(FadeIn(target, shift=UP * 0.1), LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.1, run_time=0.9))
        self.wait(0.8)
        self.play(Write(Text("same output — fewer expensive steps", color=GOOD,
                             font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B06_Speculative")


class B08_Levers(Scene):
    def construct(self):
        _table(self, "Levers, In Order",
               ["lever", "what it buys"],
               [["stream", "felt speed (TTFT)"],
                ["route", "cheaper model, easy Qs"],
                ["batch", "server throughput"],
                ["quantize", "cheaper hardware"],
                ["prompt cache", "~90% off input"]],
               note_txt="the model is the clock — fix the big number first",
               key="B08_Levers")
