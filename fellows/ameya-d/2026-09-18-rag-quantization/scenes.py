"""
Manim scenes for rag-quantization (RAG series — vector quantization & storage).
Claude fidelity palette. Grounded in PRODUCTION_NOTES.md §1 and the 384-vs-768 result.
Coordinates within SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_StorageMath": 19.54, "B02_Dimensions": 17.62, "B03_Scalar": 18.05,
          "B04_Binary": 16.3, "B05_Rescore": 19.05, "B06_Result": 18.13, "B08_When": 16.13}


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


class B01_StorageMath(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Storage Formula"), shift=DOWN * 0.2), run_time=0.6)
        formula = Text("storage  =  n_chunks  ×  dims  ×  bytes", color=INK, font_size=38, weight="BOLD").move_to([0, 1.4, 0])
        self.play(Write(formula), run_time=1.0); self.wait(0.8)
        rows = VGroup(
            Text("1M × 768  × 4B   ≈   3 GB", color=INK, font_size=32),
            Text("1M × 1536 × 4B   ≈   6 GB", color=ACCENT, font_size=32, weight="BOLD"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to([0, -0.6, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.9)
        self.play(Write(Text("this is your RAM bill — it grows with every document", color=MUTE,
                             font_size=26, slant="ITALIC").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B01_StorageMath")


class B02_Dimensions(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Dimensions Cost Twice"), shift=DOWN * 0.2), run_time=0.6)
        big = _chip("768 dims", w=6.0, h=1.1, fill=MUTE, op=0.16, fs=30).move_to([0, 1.4, 0])
        small = _chip("384 dims", w=3.0, h=1.1, fill=ACCENT, op=0.14, fs=30).move_to([-1.5, -0.1, 0])
        self.play(GrowFromEdge(big, LEFT), run_time=0.6); self.wait(0.6)
        self.play(TransformFromCopy(big, small), run_time=0.9); self.wait(0.6)
        gains = VGroup(Text("½ the storage", color=GOOD, font_size=28, weight="BOLD"),
                       Text("~½ the search time", color=GOOD, font_size=28, weight="BOLD")).arrange(DOWN, buff=0.3).move_to([3.6, -0.1, 0])
        self.play(FadeIn(gains, shift=LEFT * 0.1), run_time=0.7); self.wait(0.9)
        self.play(Write(Text("optimise quality per byte — bigger isn't automatically better", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.8)
        _fill(self, "B02_Dimensions")


class B03_Scalar(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Scalar Quantization"), shift=DOWN * 0.2), run_time=0.6)
        a = _chip("float32", w=4.4, h=1.2, fill=INK, op=0.09, fs=30).move_to([-3.0, 0.6, 0])
        b = _chip("int8", w=1.6, h=1.2, fill=ACCENT, op=0.14, fs=30).move_to([2.8, 0.6, 0])
        arr = Arrow(a.get_right(), b.get_left(), color=ACCENT, stroke_width=5, buff=0.2)
        self.play(FadeIn(a), run_time=0.5)
        self.play(GrowArrow(arr), FadeIn(b), run_time=0.7); self.wait(0.8)
        note = VGroup(Text("4× smaller", color=GOOD, font_size=30, weight="BOLD"),
                      Text("small recall loss", color=MUTE, font_size=27)).arrange(DOWN, buff=0.3).move_to([0, -1.4, 0])
        for n in note:
            self.play(FadeIn(n, shift=UP * 0.1), run_time=0.5); self.wait(0.7)
        self.play(Write(Text("the default first move when the index gets heavy", color=INK,
                             font_size=26, weight="BOLD").to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B03_Scalar")


class B04_Binary(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Binary Quantization"), shift=DOWN * 0.2), run_time=0.6)
        bits = VGroup(*[Text(b, color=(ACCENT if b == "1" else MUTE), font_size=40, weight="BOLD", font="monospace") for b in "1011001010"])
        bits.arrange(RIGHT, buff=0.28).move_to([0, 1.1, 0])
        self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.1) for b in bits], lag_ratio=0.1, run_time=1.2))
        self.play(Write(Text("1 bit per dimension — keep only the sign", color=INK, font_size=28).move_to([0, 0.0, 0])), run_time=0.7)
        big = Text("32× smaller", color=GOOD, font_size=34, weight="BOLD").move_to([-2.6, -1.4, 0])
        cost = Text("but the loss is real", color=BAD, font_size=30, weight="BOLD").move_to([2.6, -1.4, 0])
        self.play(FadeIn(big, shift=UP * 0.1), run_time=0.5); self.wait(0.6)
        self.play(FadeIn(cost, shift=UP * 0.1), run_time=0.5); self.wait(0.6)
        self.play(Write(Text("a coarse first filter — never trusted alone", color=MUTE,
                             font_size=26, slant="ITALIC").to_edge(DOWN, buff=0.55)), run_time=0.7)
        _fill(self, "B04_Binary")


class B05_Rescore(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Search Cheap, Then Rescore"), shift=DOWN * 0.2), run_time=0.6)
        a = _chip("compressed\nsearch", w=3.0, h=1.4, fill=INK, op=0.09, fs=26).move_to([-4.0, 0.2, 0])
        b = _chip("shortlist", w=2.4, h=1.4, fill=MUTE, op=0.16, fs=26).move_to([-0.3, 0.2, 0])
        c = _chip("rescore w/\nfull vectors", w=3.0, h=1.4, fill=ACCENT, op=0.13, fs=26).move_to([3.9, 0.2, 0])
        self.play(FadeIn(a), run_time=0.5)
        self.play(GrowArrow(Arrow(a.get_right(), b.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), FadeIn(b), run_time=0.6)
        self.play(GrowArrow(Arrow(b.get_right(), c.get_left(), color=ACCENT, stroke_width=5, buff=0.15)), FadeIn(c), run_time=0.6)
        self.wait(0.8)
        self.play(Write(Text("compression's speed + memory, almost full accuracy", color=GOOD,
                             font_size=27, weight="BOLD").move_to([0, -2.45, 0])), run_time=0.8)
        self.play(Write(Text("coarse first, precise last — same idea as reranking", color=MUTE,
                             font_size=24).move_to([0, -3.05, 0])), run_time=0.6)
        _fill(self, "B05_Rescore")


class B06_Result(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Project Result"), shift=DOWN * 0.2), run_time=0.6)

        def bar(x, label, pct, w, col):
            rect = RoundedRectangle(width=w, height=0.95, corner_radius=0.1, fill_color=col, fill_opacity=0.85, stroke_width=0)
            rect.move_to([x + w / 2 - 3.0, 0, 0])
            lab = Text(label, color=INK, font_size=26, weight="BOLD").next_to(rect, LEFT, buff=0.3)
            val = Text(pct, color=BG, font_size=28, weight="BOLD").move_to(rect.get_center())
            return VGroup(rect, lab, val)
        b1 = bar(0, "384-dim", "88%", 4.6, ACCENT).move_to([0.6, 0.9, 0])
        b2 = bar(0, "768-dim", "76%", 3.95, MUTE).move_to([0.35, -0.5, 0])
        self.play(GrowFromEdge(b1, LEFT), run_time=0.7); self.wait(0.6)
        self.play(GrowFromEdge(b2, LEFT), run_time=0.7); self.wait(0.8)
        self.play(Write(Text("half the storage · 3× faster · better retrieval", color=GOOD,
                             font_size=28, weight="BOLD").move_to([0, -2.45, 0])), run_time=0.8)
        self.play(Write(Text("dimension and precision = quality AND cost, one knob", color=MUTE,
                             font_size=24).move_to([0, -3.05, 0])), run_time=0.6)
        _fill(self, "B06_Result")


class B08_When(Scene):
    def construct(self):
        _table(self, "When to Compress",
               ["situation", "do"],
               [["small + RAM to spare", "stay full precision"],
                ["large / memory-bound", "quantize + rescore"],
                ["always", "measure recall + bytes"]],
               note_txt="add loss deliberately — never by accident",
               key="B08_When")
