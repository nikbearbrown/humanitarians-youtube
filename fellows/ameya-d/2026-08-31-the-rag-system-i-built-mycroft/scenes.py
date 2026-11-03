"""
Manim scenes for mycroft-rag-walkthrough (weekly WORK video).
Claude fidelity palette: cream #FAF9F5, ink #3D3929, one terracotta #D97757.
All numbers real, from fin-disclosure-rag (run_eval.py, compare_embeddings.py,
weight_sweep.py, benchmark.py — see SOURCES.md / FACTCHECK.md).
Coordinates kept inside SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill to audio via _fill().
"""

from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

# Filled from measured Kokoro audio durations (ground truth).
TARGET = {
    "B01_Task": 21.72, "B02_Pipeline": 20.01, "B03_Chunking": 22.49,
    "B04_Embeddings": 20.76, "B05_Hybrid": 34.5, "B06_Latency": 22.17,
    "B08_Surprises": 18.58,
}


def _bg(s):
    s.camera.background_color = BG


def _fill(s, key, tail=1.0):
    try:
        elapsed = s.renderer.time
    except Exception:
        elapsed = 0.0
    s.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _title(txt, size=44):
    return Text(txt, color=INK, font_size=size, weight="BOLD").to_edge(UP, buff=0.5)


def _chip(label, w=2.5, h=1.05, fill=INK, op=0.10, fs=30, tcol=INK):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.14, fill_color=fill,
                           fill_opacity=op, stroke_color=fill, stroke_width=3)
    t = Text(label, color=tcol, font_size=fs, weight="BOLD").move_to(box.get_center())
    return VGroup(box, t)


class B01_Task(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Task"), shift=DOWN * 0.2), run_time=0.6)
        a = _chip("600 documents", w=3.3, h=1.3, fill=INK, op=0.09, fs=29).move_to([-3.9, 0.4, 0])
        b = _chip("1,500 chunks", w=3.1, h=1.3, fill=INK, op=0.09, fs=29).move_to([0.0, 0.4, 0])
        c = _chip("25 eval questions", w=3.6, h=1.3, fill=ACCENT, op=0.13, fs=29).move_to([3.8, 0.4, 0])
        self.play(FadeIn(a, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowArrow(Arrow(a.get_right(), b.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), run_time=0.3)
        self.play(FadeIn(b, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowArrow(Arrow(b.get_right(), c.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), run_time=0.3)
        self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.5)
        gold = Text("a golden set: known, exact answers", color=MUTE, font_size=25).next_to(c, DOWN, buff=0.3)
        self.play(FadeIn(gold), run_time=0.4)
        self.wait(0.6)
        self.play(Write(Text("unseen in training, too many to paste — so the job is retrieval", color=INK,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B01_Task")


class B02_Pipeline(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("What I Built, End To End"), shift=DOWN * 0.2), run_time=0.6)
        r1 = ["ingest", "chunk", "embed", "index"]
        r2 = ["retrieve", "rerank", "generate"]

        def row(labels, y):
            g = VGroup(*[_chip(l, w=2.3, h=0.95, fs=27) for l in labels])
            g.arrange(RIGHT, buff=0.55).move_to([0, y, 0])
            return g
        row1 = row(r1, 1.2)
        row2 = row(r2, -0.5)
        for g in (row1, row2):
            for i, chip in enumerate(g):
                self.play(FadeIn(chip, shift=RIGHT * 0.1), run_time=0.26)
                if i < len(g) - 1:
                    self.play(GrowArrow(Arrow(g[i].get_right(), g[i + 1].get_left(),
                              color=ACCENT, stroke_width=5, buff=0.1,
                              max_tip_length_to_length_ratio=0.4)), run_time=0.16)
            self.wait(0.3)
        tag = _chip("every stage traced — chunks, scores, latency", w=8.6, h=0.9, fill=GOOD, op=0.12, fs=26, tcol=INK).move_to([0, -2.2, 0])
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.6)
        self.wait(0.5)
        _fill(self, "B02_Pipeline")


class B03_Chunking(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Chunking Moved Quality Most"), shift=DOWN * 0.2), run_time=0.6)
        naive = _chip("naive split", w=3.6, h=1.2, fill=MUTE, op=0.12, fs=29).move_to([-3.6, 1.1, 0])
        n_m = Text("MRR 0.833", color=MUTE, font_size=30, weight="BOLD").next_to(naive, DOWN, buff=0.22)
        rec = _chip("recursive split", w=3.6, h=1.2, fill=ACCENT, op=0.14, fs=29).move_to([3.6, 1.1, 0])
        r_m = Text("MRR 1.000", color=ACCENT, font_size=34, weight="BOLD").next_to(rec, DOWN, buff=0.22)
        self.play(FadeIn(naive, shift=RIGHT * 0.1), FadeIn(n_m), run_time=0.6)
        self.play(GrowArrow(Arrow(naive.get_right(), rec.get_left(), color=ACCENT, stroke_width=6, buff=0.2)), run_time=0.5)
        self.play(FadeIn(rec, shift=RIGHT * 0.1), FadeIn(r_m), run_time=0.6)
        self.wait(0.6)
        rules = VGroup(
            Text("prose → recursive (para, line, sentence)", color=INK, font_size=25),
            Text("tables → by row, header repeated", color=INK, font_size=25),
            Text("contracts → by clause", color=INK, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1.7, 0])
        for r in rules:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.4)
            self.wait(0.5)
        _fill(self, "B03_Chunking")


class B04_Embeddings(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Surprise 1 — Smaller Won"), shift=DOWN * 0.2), run_time=0.6)
        base_y = -1.6
        # bars
        h384 = 3.0 * 0.88
        h768 = 3.0 * 0.76
        bar1 = Rectangle(width=1.7, height=h384, fill_color=ACCENT, fill_opacity=0.85, stroke_width=0)
        bar1.move_to([-2.4, base_y + h384 / 2, 0])
        bar2 = Rectangle(width=1.7, height=h768, fill_color=MUTE, fill_opacity=0.8, stroke_width=0)
        bar2.move_to([2.4, base_y + h768 / 2, 0])
        l1 = Text("384-dim", color=INK, font_size=27, weight="BOLD").next_to(bar1, DOWN, buff=0.2)
        l2 = Text("768-dim", color=INK, font_size=27, weight="BOLD").next_to(bar2, DOWN, buff=0.2)
        v1 = Text("88% hit", color=ACCENT, font_size=30, weight="BOLD").next_to(bar1, UP, buff=0.18)
        v2 = Text("76% hit", color=MUTE, font_size=30, weight="BOLD").next_to(bar2, UP, buff=0.18)
        self.play(GrowFromEdge(bar1, DOWN), FadeIn(l1), run_time=0.6)
        self.play(FadeIn(v1), run_time=0.3)
        self.play(GrowFromEdge(bar2, DOWN), FadeIn(l2), run_time=0.6)
        self.play(FadeIn(v2), run_time=0.3)
        notes = VGroup(
            Text("half the storage", color=INK, font_size=24),
            Text("~3x faster", color=INK, font_size=24),
        ).arrange(RIGHT, buff=0.8).move_to([0, 1.9, 0])
        self.play(FadeIn(notes), run_time=0.4)
        self.wait(0.6)
        self.play(Write(Text("bigger is not better — measure on your own corpus", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.45)), run_time=0.8)
        _fill(self, "B04_Embeddings")


class B05_Hybrid(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Surprise 2 — Ranking, Not Recall"), shift=DOWN * 0.2), run_time=0.6)
        # data: (dense_weight, MRR)
        pts = [(0.0, 0.750), (0.2, 0.810), (0.3, 0.810), (0.5, 0.733), (0.7, 0.683), (1.0, 0.655)]

        def X(w):
            return -4.4 + w * 8.2
        def Y(m):
            return -1.5 + (m - 0.64) / 0.19 * 3.1
        # axes
        xax = Line([X(0.0), -1.7, 0], [X(1.0), -1.7, 0], color=LINE, stroke_width=2)
        yax = Line([X(0.0), -1.7, 0], [X(0.0), 1.9, 0], color=LINE, stroke_width=2)
        xlbl = Text("dense weight →", color=MUTE, font_size=22).next_to(xax, DOWN, buff=0.2)
        ylbl = Text("MRR", color=MUTE, font_size=22).next_to(yax, LEFT, buff=0.15).shift(UP * 1.4)
        self.play(Create(xax), Create(yax), FadeIn(xlbl), FadeIn(ylbl), run_time=0.6)
        # flat hit line
        hit = DashedLine([X(0.0), 2.05, 0], [X(0.32), 2.05, 0], color=GOOD, stroke_width=4)
        hlbl = Text("hit@5 ≈ 84% (barely moves)", color=GOOD, font_size=23, weight="BOLD").next_to(hit, RIGHT, buff=0.25)
        self.play(Create(hit), FadeIn(hlbl), run_time=0.6)
        # MRR curve
        dots = VGroup()
        for w, m in pts:
            peak = w in (0.2, 0.3)
            dots.add(Dot([X(w), Y(m), 0], color=(ACCENT if peak else INK), radius=(0.13 if peak else 0.09)))
        segs = VGroup(*[Line([X(pts[i][0]), Y(pts[i][1]), 0], [X(pts[i + 1][0]), Y(pts[i + 1][1]), 0],
                             color=INK, stroke_width=4) for i in range(len(pts) - 1)])
        self.play(Create(segs), run_time=1.0)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.15), run_time=0.9)
        peak_lbl = Text("peak 0.810", color=ACCENT, font_size=24, weight="BOLD").move_to([X(0.25), Y(0.810) + 0.5, 0])
        self.play(FadeIn(peak_lbl), run_time=0.4)
        self.wait(0.6)
        self.play(Write(Text("MRR 0.655 → 0.810  (+24%) — dense reorders, it doesn't add recall", color=INK,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.4)), run_time=0.8)
        _fill(self, "B05_Hybrid")


class B06_Latency(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Surprise 3 — Where The Time Goes"), shift=DOWN * 0.2), run_time=0.6)
        x0 = -2.2                      # bars start here; labels sit to the left
        scale = 5.6 / 1288.0           # generation bar ~5.6 units wide
        rows = [("generation", 1288, "1288 ms", INK, 1.3),
                ("rerank", 301, "301 ms", ACCENT, 0.0),
                ("search", 4, "4 ms", MUTE, -1.3)]
        for name, ms, lab, col, y in rows:
            nm = Text(name, color=INK, font_size=25, weight="BOLD")
            nm.next_to([-5.7, y, 0], RIGHT, buff=0.0)   # left edge pinned inside safe
            w = max(ms * scale, 0.06)
            bar = Rectangle(width=w, height=0.6, fill_color=col, fill_opacity=0.85, stroke_width=0)
            bar.move_to([x0 + w / 2, y, 0])
            val = Text(lab, color=col, font_size=25, weight="BOLD").next_to(bar, RIGHT, buff=0.25)
            self.play(FadeIn(nm), GrowFromEdge(bar, LEFT), FadeIn(val), run_time=0.55)
            self.wait(0.5)
        self.play(Write(Text("cache hit skips all of it: 0.002 ms", color=GOOD,
                             font_size=27, weight="BOLD").move_to([0, -2.2, 0])), run_time=0.6)
        self.wait(0.4)
        self.play(Write(Text("vector search is 0.2% — optimise the cache first", color=ACCENT,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.45)), run_time=0.7)
        _fill(self, "B06_Latency")


class B08_Surprises(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Three Things I'll Carry Forward"), shift=DOWN * 0.2), run_time=0.6)
        items = [("1", "smaller model won", "384-dim beat 768-dim"),
                 ("2", "hit rate saturates", "MRR still discriminates"),
                 ("3", "vector search ≈ 0.2%", "of total latency")]
        cards = VGroup()
        for num, head, sub in items:
            box = RoundedRectangle(width=3.6, height=2.4, corner_radius=0.16, fill_color=INK,
                                   fill_opacity=0.07, stroke_color=INK, stroke_width=3)
            n = Text(num, color=ACCENT, font_size=52, weight="BOLD").move_to(box.get_center() + UP * 0.7)
            h = Text(head, color=INK, font_size=25, weight="BOLD").move_to(box.get_center() + DOWN * 0.15)
            s = Text(sub, color=MUTE, font_size=22).move_to(box.get_center() + DOWN * 0.72)
            cards.add(VGroup(box, n, h, s))
        cards.arrange(RIGHT, buff=0.5).move_to([0, 0.1, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.12), run_time=0.5)
            self.wait(0.8)
        self.play(Write(Text("measure before you optimise", color=ACCENT,
                             font_size=32, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B08_Surprises")
