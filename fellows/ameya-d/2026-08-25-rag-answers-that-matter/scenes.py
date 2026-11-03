"""
Manim scenes for rag-answers-that-matter (field-guide explainer).
Claude fidelity palette: cream #FAF9F5, ink #3D3929, one terracotta #D97757.
Content is field-standard RAG knowledge from the user's reference doc (SOURCES.md).
Coordinates kept inside SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill to audio via _fill().
"""

from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {
    "B01_Pipeline": 16.45, "B02_Chunking": 18.39, "B03_Encoders": 20.82,
    "B04_VectorSearch": 22.87, "B05_Hybrid": 18.75, "B06_Advanced": 19.07,
    "B07_Eval": 18.26, "B08_Judge": 16.51, "B09_Production": 19.86, "B10_Honest": 13.7,
}


def _bg(s):
    s.camera.background_color = BG


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


class B01_Pipeline(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Shared Pipeline"), shift=DOWN * 0.2), run_time=0.6)
        r1 = ["ingest", "chunk", "embed", "index"]
        r2 = ["retrieve", "rerank", "augment", "generate"]

        def row(labels, y):
            g = VGroup(*[_chip(l, w=2.3, h=0.95, fs=28) for l in labels])
            g.arrange(RIGHT, buff=0.55).move_to([0, y, 0])
            return g
        row1 = row(r1, 1.4)
        row2 = row(r2, -0.1)
        for g in (row1, row2):
            for i, chip in enumerate(g):
                self.play(FadeIn(chip, shift=RIGHT * 0.1), run_time=0.28)
                if i < len(g) - 1:
                    self.play(GrowArrow(Arrow(g[i].get_right(), g[i + 1].get_left(),
                              color=ACCENT, stroke_width=5, buff=0.1,
                              max_tip_length_to_length_ratio=0.4)), run_time=0.18)
            self.wait(0.4)
        tiers = VGroup(
            Text("naive — stuff top matches in", color=MUTE, font_size=26),
            Text("advanced — + query rewrite, rerank", color=INK, font_size=26),
            Text("agentic — retrieval becomes a tool", color=ACCENT, font_size=26, weight="BOLD"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to([0, -2.3, 0])
        for t in tiers:
            self.play(FadeIn(t, shift=RIGHT * 0.1), run_time=0.4)
            self.wait(0.7)
        _fill(self, "B01_Pipeline")


# ---- shared table helper (with per-row swatch for distinctness) ----
def _table(scene, title_txt, headers, rows, highlight_row=None, note_txt=None, key=None):
    _bg(scene)
    scene.play(FadeIn(_title(title_txt, 44), shift=DOWN * 0.2), run_time=0.6)
    ncol = len(headers)
    span = 8.4
    xs = [-span / 2 + i * (span / (ncol - 1)) for i in range(ncol)] if ncol > 1 else [0]
    y0 = 1.6
    hdr = VGroup(*[Text(h, color=MUTE, font_size=25, weight="BOLD").move_to([xs[i], y0, 0]) for i, h in enumerate(headers)])
    scene.play(FadeIn(hdr), run_time=0.4)
    scene.play(Create(Line([xs[0] - 0.7, y0 - 0.35, 0], [xs[-1] + 0.7, y0 - 0.35, 0], color=LINE, stroke_width=2)), run_time=0.3)
    y = y0 - 0.95
    for ri, rowv in enumerate(rows):
        col = ACCENT if ri == highlight_row else INK
        sw = Square(side_length=0.28, fill_color=(ACCENT if ri == highlight_row else MUTE),
                    fill_opacity=0.9, stroke_width=0).move_to([xs[0] - 1.15, y, 0])
        cells = VGroup(*[Text(str(c), color=col, font_size=25,
                             weight=("BOLD" if (ri == highlight_row or j > 0) else "NORMAL"),
                             font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                        for j, c in enumerate(rowv)])
        if ri == highlight_row:
            scene.play(GrowFromCenter(sw), FadeIn(cells),
                       Create(SurroundingRectangle(cells, color=ACCENT, buff=0.14, stroke_width=2.5, corner_radius=0.06)), run_time=0.5)
        else:
            scene.play(GrowFromCenter(sw), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.7)
        y -= 0.72
    if note_txt:
        scene.play(Write(Text(note_txt, color=INK, font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
    _fill(scene, key)


class B02_Chunking(Scene):
    def construct(self):
        _table(self, "Chunking — Recursive Wins",
               ["strategy", "what", "when"],
               [["fixed", "N tokens", "fast, uniform"],
                ["recursive", "para→line→sent", "the default"],
                ["document", "by heading", "structured"],
                ["parent-doc", "small→big", "precision+context"]],
               highlight_row=1,
               note_txt="start 256–512 tokens · 10–20% overlap",
               key="B02_Chunking")


class B03_Encoders(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Bi-Encoder vs Cross-Encoder"), shift=DOWN * 0.2), run_time=0.6)

        def panel(x, head, lines, col):
            box = RoundedRectangle(width=5.4, height=3.1, corner_radius=0.16, fill_color=col,
                                   fill_opacity=0.10, stroke_color=col, stroke_width=3).move_to([x, 0.1, 0])
            h = Text(head, color=col, font_size=32, weight="BOLD").move_to([x, 1.15, 0])
            body = VGroup(*[Text(l, color=INK, font_size=25) for l in lines]).arrange(DOWN, buff=0.28).move_to([x, -0.25, 0])
            return VGroup(box, h, body)
        left = panel(-3.1, "bi-encoder", ["encodes separately", "vectors precompute", "fast · FIRST-STAGE"], INK)
        right = panel(3.1, "cross-encoder", ["reads both together", "cannot precompute", "accurate · RERANK ONLY"], ACCENT)
        self.play(FadeIn(left, shift=RIGHT * 0.1), run_time=0.7)
        self.wait(2.4)
        self.play(FadeIn(right, shift=LEFT * 0.1), run_time=0.7)
        self.wait(2.4)
        self.play(Write(Text("normalize once → cosine is a dot product", color=INK,
                             font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B03_Encoders")


class B04_VectorSearch(Scene):
    def construct(self):
        _table(self, "Under the Vector DB",
               ["index", "mechanism", "trade-off"],
               [["Flat", "compare all", "exact, <100k"],
                ["HNSW", "prox. graph", "fast · RAM"],
                ["IVF", "cluster route", "tune nprobe"],
                ["PQ / SQ", "compress", "memory · recall"]],
               highlight_row=1,
               note_txt="recall vs latency vs memory — the ANN triangle",
               key="B04_VectorSearch")


class B05_Hybrid(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Hybrid: Sparse + Dense"), shift=DOWN * 0.2), run_time=0.6)
        sparse = _chip("BM25 (keyword)", w=4.4, h=1.3, fill=INK, op=0.10, fs=30).move_to([-3.4, 1.3, 0])
        s_note = Text("exact terms, names, codes", color=MUTE, font_size=24).next_to(sparse, DOWN, buff=0.18)
        dense = _chip("embeddings (dense)", w=4.4, h=1.3, fill=ACCENT, op=0.12, fs=30).move_to([-3.4, -1.2, 0])
        d_note = Text("meaning, paraphrase", color=MUTE, font_size=24).next_to(dense, DOWN, buff=0.18)
        self.play(FadeIn(sparse, shift=RIGHT * 0.1), FadeIn(s_note), run_time=0.6)
        self.wait(1.8)
        self.play(FadeIn(dense, shift=RIGHT * 0.1), FadeIn(d_note), run_time=0.6)
        self.wait(1.8)
        rrf = _chip("RRF fusion", w=3.4, h=1.5, fill=GOOD, op=0.14, fs=32).move_to([3.4, 0.05, 0])
        a1 = Arrow(sparse.get_right(), rrf.get_corner(UL) + [0, -0.2, 0], color=ACCENT, stroke_width=5, buff=0.15)
        a2 = Arrow(dense.get_right(), rrf.get_corner(DL) + [0, 0.2, 0], color=ACCENT, stroke_width=5, buff=0.15)
        self.play(GrowArrow(a1), GrowArrow(a2), FadeIn(rrf), run_time=0.7)
        self.wait(1.6)
        self.play(Write(Text("merge ranked lists — no calibrated scores needed", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B05_Hybrid")


class B06_Advanced(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Retrieval Toolbox"), shift=DOWN * 0.2), run_time=0.6)
        items = [("query rewriting", "clean the question"),
                 ("HyDE", "search a hypothetical answer"),
                 ("reranking", "cross-encoder re-scores top-N"),
                 ("contextual retrieval", "prepend a parent summary")]
        cards = VGroup()
        for head, sub in items:
            box = RoundedRectangle(width=5.3, height=1.5, corner_radius=0.14, fill_color=INK,
                                   fill_opacity=0.08, stroke_color=INK, stroke_width=3)
            h = Text(head, color=ACCENT, font_size=30, weight="BOLD").move_to(box.get_center() + UP * 0.32)
            s = Text(sub, color=INK, font_size=24).move_to(box.get_center() + DOWN * 0.32)
            cards.add(VGroup(box, h, s))
        cards.arrange_in_grid(rows=2, cols=2, buff=(0.7, 0.6)).move_to([0, -0.2, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.45)
            self.wait(0.9)
        _fill(self, "B06_Advanced")


class B07_Eval(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Measure the Two Halves"), shift=DOWN * 0.2), run_time=0.6)

        def col(x, head, items, c):
            h = Text(head, color=c, font_size=30, weight="BOLD").move_to([x, 1.7, 0])
            rows = VGroup()
            for it in items:
                dot = Dot(color=c, radius=0.1)
                t = Text(it, color=INK, font_size=27)
                rows.add(VGroup(dot, t).arrange(RIGHT, buff=0.28))
            rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([x, 0.1, 0])
            return h, rows
        lh, lrows = col(-3.3, "RETRIEVAL", ["hit rate @ k", "MRR", "NDCG"], INK)
        rh, rrows = col(3.3, "GENERATION", ["faithfulness", "relevance", "correctness"], ACCENT)
        div = Line([0, 2.0, 0], [0, -1.4, 0], color=LINE, stroke_width=2)
        self.play(FadeIn(lh), FadeIn(rh), Create(div), run_time=0.7)
        for i in range(3):
            self.play(GrowFromCenter(lrows[i][0]), FadeIn(lrows[i][1], shift=RIGHT * 0.1), run_time=0.4)
            self.play(GrowFromCenter(rrows[i][0]), FadeIn(rrows[i][1], shift=RIGHT * 0.1), run_time=0.4)
            self.wait(0.7)
        self.play(Write(Text("debug retrieval first — bad context, no prompt saves you", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B07_Eval")


class B08_Judge(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Judge Has Tells"), shift=DOWN * 0.2), run_time=0.6)
        biases = [("position", "favours the first"),
                  ("verbosity", "favours the longer"),
                  ("self-preference", "favours its own family")]
        cards = VGroup()
        for head, sub in biases:
            box = RoundedRectangle(width=3.5, height=1.7, corner_radius=0.14, fill_color=BAD,
                                   fill_opacity=0.10, stroke_color=BAD, stroke_width=3)
            h = Text(head, color=BAD, font_size=28, weight="BOLD").move_to(box.get_center() + UP * 0.35)
            s = Text(sub, color=INK, font_size=23).move_to(box.get_center() + DOWN * 0.35)
            cards.add(VGroup(box, h, s))
        cards.arrange(RIGHT, buff=0.4).move_to([0, 0.9, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.45)
            self.wait(0.9)
        self.play(Write(Text("randomize order · use a rubric · check vs humans", color=MUTE,
                             font_size=26).move_to([0, -1.2, 0])), run_time=0.6)
        self.wait(1.2)
        self.play(Write(Text("validate the judge before you trust the judge", color=ACCENT,
                             font_size=34, weight="BOLD").to_edge(DOWN, buff=0.6)), run_time=0.8)
        _fill(self, "B08_Judge")


class B09_Production(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Production: Four Levers"), shift=DOWN * 0.2), run_time=0.6)
        items = [("latency", "stream first token (TTFT)"),
                 ("cost", "input tokens dominate — route, trim"),
                 ("caching", "exact + semantic"),
                 ("guardrails", "grounding + schema out")]
        cards = VGroup()
        for head, sub in items:
            box = RoundedRectangle(width=5.4, height=1.5, corner_radius=0.14, fill_color=INK,
                                   fill_opacity=0.08, stroke_color=INK, stroke_width=3)
            h = Text(head, color=ACCENT, font_size=30, weight="BOLD").move_to(box.get_center() + UP * 0.32)
            s = Text(sub, color=INK, font_size=23).move_to(box.get_center() + DOWN * 0.32)
            cards.add(VGroup(box, h, s))
        cards.arrange_in_grid(rows=2, cols=2, buff=(0.6, 0.55)).move_to([0, -0.15, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.45)
            self.wait(0.9)
        self.play(Write(Text("the cheapest token is the one you don't generate", color=MUTE,
                             font_size=26, slant="ITALIC").to_edge(DOWN, buff=0.45)), run_time=0.7)
        _fill(self, "B09_Production")


class B10_Honest(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Honest Frame"), shift=DOWN * 0.2), run_time=0.6)
        lines = [("\"I haven't built that in production.\"", MUTE),
                 ("\"My understanding is …\"", INK),
                 ("\"If I were starting, I'd …\"", ACCENT)]
        grp = VGroup()
        for txt, col in lines:
            bullet = Square(side_length=0.34, fill_color=col, fill_opacity=0.9, stroke_width=0).rotate(PI / 4)
            t = Text(txt, color=INK, font_size=36, weight="BOLD")
            grp.add(VGroup(bullet, t).arrange(RIGHT, buff=0.45))
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.7).move_to([0, 0.4, 0])
        for it in grp:
            self.play(GrowFromCenter(it[0]), FadeIn(it[1], shift=RIGHT * 0.15), run_time=0.5)
            self.wait(1.3)
        self.play(Write(Text("credible beats confident — bluffing is the only version that loses",
                             color=ACCENT, font_size=28, weight="BOLD").to_edge(DOWN, buff=0.6)), run_time=0.8)
        _fill(self, "B10_Honest")
