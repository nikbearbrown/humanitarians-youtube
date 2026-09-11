"""
Manim scenes for rag-vector-search (RAG series — ANN indexes).
Claude fidelity palette. Content grounded in PRODUCTION_NOTES.md §2.
Coordinates within SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_BruteForce": 18.88, "B02_Triangle": 19.54, "B03_Flat": 17.58,
          "B04_HNSW": 22.23, "B05_IVF": 20.18, "B06_Quant": 27.86, "B08_Choose": 24.47}


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


def _table(scene, title_txt, headers, rows, highlight_row=None, note_txt=None, key=None):
    _bg(scene)
    scene.play(FadeIn(_title(title_txt, 44), shift=DOWN * 0.2), run_time=0.6)
    ncol = len(headers); span = 8.4
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
        cells = VGroup(*[Text(str(c), color=col, font_size=24,
                             weight=("BOLD" if (ri == highlight_row or j > 0) else "NORMAL"),
                             font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                        for j, c in enumerate(rowv)])
        if ri == highlight_row:
            scene.play(GrowFromCenter(sw), FadeIn(cells),
                       Create(SurroundingRectangle(cells, color=ACCENT, buff=0.14, stroke_width=2.5, corner_radius=0.06)), run_time=0.5)
        else:
            scene.play(GrowFromCenter(sw), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.6)
        y -= 0.72
    if note_txt:
        scene.play(Write(Text(note_txt, color=INK, font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
    _fill(scene, key)


class B01_BruteForce(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Brute Force — Compare Everything"), shift=DOWN * 0.2), run_time=0.6)
        q = _chip("query", w=1.9, h=0.9, fill=ACCENT, op=0.14, fs=28).move_to([-4.6, 0, 0])
        self.play(FadeIn(q, shift=RIGHT * 0.1), run_time=0.4)
        dots = VGroup(*[Dot(color=INK, radius=0.09) for _ in range(24)])
        dots.arrange_in_grid(rows=4, cols=6, buff=0.5).move_to([1.3, 0.2, 0])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.03, run_time=1.0))
        lines = VGroup(*[Line(q.get_right(), d.get_center(), color=MUTE, stroke_width=1.2) for d in dots])
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.02, run_time=1.4))
        self.play(Write(Text("O(n · d) — one query touches every vector", color=INK, font_size=28, weight="BOLD").move_to([0, -2.2, 0])), run_time=0.7)
        self.play(Write(Text("1,500 vectors → 4 ms      10M → minutes", color=MUTE, font_size=26).move_to([0, -3.0, 0])), run_time=0.6)
        _fill(self, "B01_BruteForce")


class B02_Triangle(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The ANN Trade-off"), shift=DOWN * 0.2), run_time=0.6)
        A = [0, 2.0, 0]; B = [-3.4, -1.7, 0]; C = [3.4, -1.7, 0]
        tri = Polygon(A, B, C, color=ACCENT, stroke_width=5, fill_opacity=0.05, fill_color=ACCENT)
        self.play(Create(tri), run_time=0.9)
        la = Text("recall", color=INK, font_size=32, weight="BOLD").next_to(A, UP, buff=0.25)
        lb = Text("latency", color=INK, font_size=32, weight="BOLD").next_to(B, DOWN, buff=0.25)
        lc = Text("memory", color=INK, font_size=32, weight="BOLD").next_to(C, DOWN, buff=0.25)
        for l in (la, lb, lc):
            self.play(FadeIn(l, shift=UP * 0.1), run_time=0.45); self.wait(0.5)
        self.play(Write(Text("approximate search: trade a little exactness for speed", color=ACCENT,
                             font_size=28, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B02_Triangle")


class B03_Flat(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Flat — Exact and Simple"), shift=DOWN * 0.2), run_time=0.6)
        box = RoundedRectangle(width=7.2, height=3.0, corner_radius=0.18, fill_color=INK,
                               fill_opacity=0.06, stroke_color=INK, stroke_width=3).move_to([0, 0.1, 0])
        self.play(FadeIn(box), run_time=0.5)
        rows = VGroup(
            Text("compares against every vector", color=INK, font_size=30),
            Text("recall = 1.0  ·  no approximation", color=GOOD, font_size=30, weight="BOLD"),
            Text("the right answer below ~100k vectors", color=INK, font_size=30),
        ).arrange(DOWN, buff=0.4).move_to(box.get_center())
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.5); self.wait(0.8)
        self.play(Write(Text("don't reach for a fancy index before you need one", color=MUTE,
                             font_size=26, slant="ITALIC").to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B03_Flat")


class B04_HNSW(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("HNSW — A Graph You Walk"), shift=DOWN * 0.2), run_time=0.6)
        layers = []
        specs = [(1.9, 3, MUTE), (0.5, 5, INK), (-0.9, 8, INK)]
        for y, n, col in specs:
            pts = VGroup(*[Dot(color=col, radius=0.08) for _ in range(n)])
            pts.arrange(RIGHT, buff=(8.4 / (n)) if n > 1 else 1).move_to([0, y, 0])
            edges = VGroup(*[Line(pts[i].get_center(), pts[i + 1].get_center(), color=LINE, stroke_width=1.5) for i in range(n - 1)])
            layers.append((pts, edges))
            self.play(FadeIn(pts), Create(edges), run_time=0.5)
        # greedy descent arrows top → bottom
        path = [layers[0][0][0], layers[1][0][2], layers[2][0][5]]
        arrs = VGroup(*[Arrow(path[i].get_center(), path[i + 1].get_center(), color=ACCENT, stroke_width=5, buff=0.12) for i in range(2)])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.6, run_time=1.2))
        self.play(Write(Text("big hops, then small — ~O(log n), high recall, high RAM", color=INK,
                             font_size=27, weight="BOLD").move_to([0, -2.45, 0])), run_time=0.8)
        self.play(Write(Text("knobs: M · ef_construction · ef_search", color=MUTE, font_size=24).move_to([0, -3.05, 0])), run_time=0.5)
        _fill(self, "B04_HNSW")


class B05_IVF(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("IVF — Clusters You Skip"), shift=DOWN * 0.2), run_time=0.6)
        centers = [[-3.6, 1.0, 0], [-0.2, 1.4, 0], [2.9, 0.6, 0], [-1.8, -1.6, 0], [3.4, -1.7, 0]]
        cols = [MUTE, MUTE, ACCENT, MUTE, MUTE]
        clusters = VGroup()
        for i, c in enumerate(centers):
            ring = Circle(radius=0.95, color=cols[i], stroke_width=3, fill_opacity=0.05, fill_color=cols[i]).move_to(c)
            cen = Dot(color=cols[i], radius=0.11).move_to(c)
            pts = VGroup(*[Dot(color=cols[i], radius=0.055).move_to([c[0] + 0.5 * np.cos(a), c[1] + 0.5 * np.sin(a), 0]) for a in np.linspace(0, TAU, 6, endpoint=False)])
            clusters.add(VGroup(ring, cen, pts))
        self.play(LaggedStart(*[FadeIn(cl) for cl in clusters], lag_ratio=0.2, run_time=1.4))
        q = _chip("query", w=1.7, h=0.8, fill=ACCENT, op=0.16, fs=26).move_to([-5.0, -0.4, 0])
        self.play(FadeIn(q), run_time=0.4)
        arr = Arrow(q.get_right(), np.array(centers[2]) + np.array([-0.9, 0, 0]), color=ACCENT, stroke_width=5, buff=0.1)
        self.play(GrowArrow(arr), Indicate(clusters[2], color=ACCENT, scale_factor=1.15), run_time=0.9)
        self.play(Write(Text("search only the nearest clusters — nprobe tunes recall vs speed", color=INK,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.8)
        _fill(self, "B05_IVF")


class B06_Quant(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Compression — IVF-PQ"), shift=DOWN * 0.2), run_time=0.6)
        full = _chip("float32 vector", w=4.6, h=1.1, fill=INK, op=0.09, fs=28).move_to([-3.2, 1.4, 0])
        code = _chip("compact code", w=2.6, h=1.1, fill=ACCENT, op=0.14, fs=26).move_to([3.2, 1.4, 0])
        arr = Arrow(full.get_right(), code.get_left(), color=ACCENT, stroke_width=5, buff=0.15)
        self.play(FadeIn(full), run_time=0.4)
        self.play(GrowArrow(arr), FadeIn(code), run_time=0.6)
        self.wait(0.6)
        math = VGroup(
            Text("storage  =  n_chunks × dims × 4 bytes", color=INK, font_size=30, weight="BOLD"),
            Text("1M × 768 × 4B  ≈  3 GB", color=ACCENT, font_size=30, weight="BOLD"),
            Text("smaller dims → half the storage AND half the search", color=MUTE, font_size=25),
        ).arrange(DOWN, buff=0.35).move_to([0, -1.3, 0])
        for m in math:
            self.play(FadeIn(m, shift=UP * 0.1), run_time=0.5); self.wait(0.7)
        _fill(self, "B06_Quant")


class B08_Choose(Scene):
    def construct(self):
        _table(self, "Which Index?",
               ["scale", "index", "why"],
               [["< 100k", "Flat", "exact, simple"],
                ["recall + RAM", "HNSW", "graph, high recall"],
                ["10M+, tight RAM", "IVF-PQ", "clusters + compress"]],
               highlight_row=None,
               note_txt="k-means routing (Boehringer) = IVF, hand-rolled",
               key="B08_Choose")
