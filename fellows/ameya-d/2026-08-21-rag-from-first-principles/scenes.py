"""
Manim scenes for rag-from-first-principles (deep-explainer).
Claude fidelity palette: cream #FAF9F5, ink #3D3929, one terracotta #D97757.

All numbers are real, from the repo scripts (see FACTCHECK.md claims ledger).
Coordinates kept inside SAFE (|x|<=6.0, |y|<=3.3); type sized to fill the canvas.
Every scene auto-fills to its measured narration length via _fill() (audio clock).
"""

from manim import *

BG = "#FAF9F5"
INK = "#3D3929"
ACCENT = "#D97757"
MUTE = "#8A8578"
GOOD = "#4A7C59"
BAD = "#C0392B"
LINE = "#B8B0A0"

# Measured narration lengths (mp3/timings.json) — set after audio generation.
TARGET = {
    "B01_ThreeNumbers": 18.45, "B02_Problem": 19.9, "B04_Overlap": 12.59,
    "B05_Histogram": 21.18, "B06_Tokens": 23.83, "B07_Pooling": 16.92,
    "B08_Batch": 21.14, "B09_Padding": 20.95, "B10_Index": 21.99,
    "B13_Dilution": 19.84, "B14_Address": 17.51, "B15_Metrics": 18.97,
    "B16_Models": 22.31, "B17_HybridWorse": 22.36, "B18_Sweep": 22.19,
    "B19_Latency": 19.05, "B20_Cache": 17.05, "B21_Scale": 26.9,
}


def _bg(s):
    s.camera.background_color = BG


def _fill(s, key, tail=1.0):
    try:
        elapsed = s.renderer.time
    except Exception:
        elapsed = 0.0
    s.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _title(txt, size=48):
    return Text(txt, color=INK, font_size=size, weight="BOLD").to_edge(UP, buff=0.5)


def _act(txt):
    """small act kicker, top-left — inset well inside the title-safe area."""
    return Text(txt, color=MUTE, font_size=22, weight="BOLD").to_edge(
        LEFT, buff=1.0).to_edge(UP, buff=0.45)


class B01_ThreeNumbers(Scene):
    def construct(self):
        _bg(self)
        k = _act("RAG FROM FIRST PRINCIPLES")
        self.play(FadeIn(k), run_time=0.4)
        rows = [
            ("768 → 384", "a smaller model won", ACCENT),
            ("LOST", "pooling destroys information", BAD),
            ("0.655", "the default that got beaten", INK),
        ]
        items = VGroup()
        for big, small, col in rows:
            n = Text(big, color=col, font_size=76, weight="BOLD")
            l = Text(small, color=MUTE, font_size=30)
            items.add(VGroup(n, l).arrange(DOWN, buff=0.18))
        items.arrange(DOWN, buff=0.7).move_to([0, -0.1, 0])
        for it in items:
            self.play(FadeIn(it, shift=UP * 0.2), run_time=0.6)
            self.wait(1.6)
        _fill(self, "B01_ThreeNumbers")


class B02_Problem(Scene):
    def construct(self):
        _bg(self)
        t = _title("600 Documents, One Question", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        counter = Text("600", color=ACCENT, font_size=90, weight="BOLD").move_to([0, 1.2, 0])
        cap = Text("financial disclosures", color=MUTE, font_size=30).next_to(counter, DOWN, buff=0.2)
        self.play(FadeIn(counter, scale=1.2), FadeIn(cap), run_time=0.7)
        self.wait(2.2)
        q = Text("\"What are Bluewater's merger cost synergies?\"", color=INK,
                 font_size=32, slant="ITALIC").move_to([0, -0.6, 0])
        self.play(Write(q), run_time=0.8)
        self.wait(2.6)
        # overflow vs fit
        bad = VGroup(Text("paste all 600", color=BAD, font_size=28, weight="BOLD"),
                     Text("context overflow — 128k blown", color=MUTE, font_size=24)).arrange(DOWN, buff=0.12).move_to([-3.4, -2.4, 0])
        good = VGroup(Text("retrieve 3", color=GOOD, font_size=28, weight="BOLD"),
                      Text("only what's relevant", color=MUTE, font_size=24)).arrange(DOWN, buff=0.12).move_to([3.4, -2.4, 0])
        self.play(FadeIn(bad, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)
        self.play(FadeIn(good, shift=UP * 0.1), run_time=0.6)
        _fill(self, "B02_Problem")


class B04_Overlap(Scene):
    def construct(self):
        _bg(self)
        t = _title("Overlap = Step Below Size", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        sub = Text("\"ABCDEFGHIJ\"   size = 4,   overlap = 1", color=MUTE, font_size=30).next_to(t, DOWN, buff=0.3)
        self.play(Write(sub), run_time=0.6)
        self.wait(1.6)
        windows = [("i=0", "ABCD", 0), ("i=3", "DEFG", 3), ("i=6", "GHIJ", 6), ("i=9", "J", 9)]
        rows = VGroup()
        for idx, chars, start in windows:
            lab = Text(idx, color=MUTE, font_size=34, font="monospace")
            chs = VGroup()
            for j, c in enumerate(chars):
                # first char of a non-initial window repeats the previous boundary
                col = ACCENT if (start > 0 and j == 0) else INK
                box = Square(side_length=0.9, fill_color=(ACCENT if (start > 0 and j == 0) else INK),
                             fill_opacity=(0.16 if (start > 0 and j == 0) else 0.06),
                             stroke_color=col, stroke_width=2)
                ch = Text(c, color=col, font_size=44, weight="BOLD", font="monospace").move_to(box.get_center())
                chs.add(VGroup(box, ch))
            chs.arrange(RIGHT, buff=0.2)
            row = VGroup(lab, chs).arrange(RIGHT, buff=0.7)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([-0.3, -0.3, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.5)
            self.wait(1.0)
        note = Text("the repeated letter keeps a boundary fact whole", color=INK,
                    font_size=30, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B04_Overlap")


class B05_Histogram(Scene):
    def construct(self):
        _bg(self)
        t = _title("chunk_size Is a Ceiling", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        cmp = Text("same settings:   fixed → 8 chunks      recursive → 10 chunks",
                   color=INK, font_size=30, weight="BOLD").next_to(t, DOWN, buff=0.3)
        self.play(Write(cmp), run_time=0.7)
        self.wait(2.4)
        # bimodal histogram
        bars = [("50–99", 564), ("100–149", 336), ("300–349", 96), ("350–399", 504)]
        maxv = 564.0
        grp = VGroup()
        for lab, v in bars:
            l = Text(lab, color=INK, font_size=24, font="monospace")
            bar = Rectangle(width=6.2 * v / maxv, height=0.5, fill_color=ACCENT,
                            fill_opacity=0.85, stroke_width=0)
            val = Text(str(v), color=MUTE, font_size=24)
            row = VGroup(l, bar, val)
            l.move_to([-4.6, 0, 0])
            bar.next_to(l, RIGHT, buff=0.3).align_to(l, LEFT).shift(RIGHT * 1.6)
            bar.align_to([-2.8, 0, 0], LEFT)
            val.next_to(bar, RIGHT, buff=0.2)
            grp.add(VGroup(l, bar, val))
        grp.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([0, -0.7, 0])
        for row in grp:
            self.play(GrowFromEdge(row[1], LEFT), FadeIn(row[0]), FadeIn(row[2]), run_time=0.5)
            self.wait(0.7)
        stat = Text("min 67   max 388   mean 202   median 104", color=INK,
                    font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(stat), run_time=0.7)
        _fill(self, "B05_Histogram")


class B06_Tokens(Scene):
    def construct(self):
        _bg(self)
        t = _title("Financial Text Costs More Tokens", 42)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)

        def strip(label, toks, col, y):
            head = Text(label, color=MUTE, font_size=26).move_to([-4.7, y + 0.55, 0]).align_to([-5.2, 0, 0], LEFT)
            chips = VGroup()
            for tk in toks:
                box = Rectangle(width=0.28 + 0.16 * len(tk), height=0.55, fill_color=col,
                                fill_opacity=0.16, stroke_color=col, stroke_width=2)
                tt = Text(tk, color=INK, font_size=22, font="monospace").move_to(box.get_center())
                chips.add(VGroup(box, tt))
            chips.arrange(RIGHT, buff=0.14).move_to([0.3, y, 0])
            cnt = Text(f"{len(toks)} tok", color=col, font_size=26, weight="BOLD")
            return head, chips, cnt

        h1, c1, n1 = strip("'the cat sat on a mat'  (20 chars)", ["the", "cat", "sat", "on", "a", "mat"], GOOD, 1.4)
        n1.next_to(c1, DOWN, buff=0.2)
        self.play(FadeIn(h1), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c) for c in c1], lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(n1), run_time=0.3)
        self.wait(2.0)
        h2, c2, n2 = strip("'$4,829.17 EBITDA Q3x'  (20 chars)",
                           ["$", "4", ",", "82", "##9", ".", "17", "e", "##bit", "##da", "q", "##3", "##x"], BAD, -0.6)
        n2.next_to(c2, DOWN, buff=0.2)
        self.play(FadeIn(h2), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c) for c in c2], lag_ratio=0.1), run_time=1.2)
        self.play(FadeIn(n2), run_time=0.3)
        self.wait(2.0)
        note = Text("2–3× less efficient  →  cost, context limits, silent truncation @ 384",
                    color=INK, font_size=26, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B06_Tokens")


class B07_Pooling(Scene):
    def construct(self):
        _bg(self)
        t = _title("One Vector Per Token", 48)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        stages = [("tokens", "(7,)"), ("per-token vecs", "(7, 384)"), ("chunk vector", "(384,)")]
        boxes = VGroup()
        for name, shape in stages:
            n = Text(name, color=MUTE, font_size=26)
            sh = Text(shape, color=INK, font_size=40, weight="BOLD", font="monospace")
            boxes.add(VGroup(sh, n).arrange(DOWN, buff=0.18))
        boxes.arrange(RIGHT, buff=1.6).move_to([0, 0.6, 0])
        self.play(FadeIn(boxes[0], shift=RIGHT * 0.2), run_time=0.6)
        self.wait(1.6)
        a1 = Text("forward pass", color=ACCENT, font_size=22, slant="ITALIC")
        arr1 = Arrow(boxes[0].get_right(), boxes[1].get_left(), color=ACCENT, stroke_width=5, buff=0.2)
        a1.next_to(arr1, UP, buff=0.1)
        self.play(GrowArrow(arr1), FadeIn(a1), FadeIn(boxes[1], shift=RIGHT * 0.2), run_time=0.7)
        self.wait(1.8)
        a2 = Text("mean pooling", color=ACCENT, font_size=22, slant="ITALIC")
        arr2 = Arrow(boxes[1].get_right(), boxes[2].get_left(), color=ACCENT, stroke_width=5, buff=0.2)
        a2.next_to(arr2, UP, buff=0.1)
        self.play(GrowArrow(arr2), FadeIn(a2), FadeIn(boxes[2], shift=RIGHT * 0.2), run_time=0.7)
        self.wait(1.8)
        note = Text("seven token vectors, averaged into one", color=INK,
                    font_size=30, weight="BOLD").to_edge(DOWN, buff=0.6)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B07_Pooling")


class B08_Batch(Scene):
    def construct(self):
        _bg(self)
        t = _title("Batching: 12.6× Free Speed", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        rows = [("64 separate matmuls", "14.924 ms", BAD),
                ("1 batched matmul", "1.181 ms", GOOD)]
        grp = VGroup()
        for lab, val, col in rows:
            l = Text(lab, color=INK, font_size=32)
            v = Text(val, color=col, font_size=36, weight="BOLD", font="monospace")
            grp.add(VGroup(l, v).arrange(RIGHT, buff=0.8))
        grp.arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to([0, 1.1, 0])
        for r in grp:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.5)
            self.wait(1.4)
        sp = Text("speedup: 12.6×", color=ACCENT, font_size=44, weight="BOLD").move_to([0, -0.7, 0])
        self.play(Write(sp), run_time=0.7)
        self.wait(1.8)
        same = Text("arithmetic ops: 75,497,472  —  IDENTICAL either way", color=INK,
                    font_size=28, weight="BOLD").to_edge(DOWN, buff=0.6)
        self.play(Write(same), run_time=0.7)
        _fill(self, "B08_Batch")


class B09_Padding(Scene):
    def construct(self):
        _bg(self)
        t = _title("But Padding Caps the Gain", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        rows = [("batch 1", "9.9", MUTE), ("batch 8", "14.2  best", GOOD),
                ("batch 32", "13.7", MUTE), ("batch 128", "11.0  worse", BAD)]
        grp = VGroup()
        for lab, val, col in rows:
            l = Text(lab, color=INK, font_size=28, font="monospace")
            v = Text(val, color=col, font_size=30, weight="BOLD", font="monospace")
            grp.add(VGroup(l, v).arrange(RIGHT, buff=0.7))
        grp.arrange(DOWN, buff=0.34, aligned_edge=LEFT).move_to([-3.0, 0.4, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in grp], lag_ratio=0.3), run_time=1.4)
        self.wait(1.6)
        # attention mask
        m1 = Text("[1,1,1,1,0,0,0,0,0,0,0]", color=INK, font_size=26, font="monospace").move_to([3.0, 1.0, 0])
        m1c = Text("4 real · 7 padding", color=BAD, font_size=22).next_to(m1, DOWN, buff=0.1)
        m2 = Text("[1,1,1,1,1,1,1,1,1,1,1]", color=INK, font_size=26, font="monospace").move_to([3.0, -0.3, 0])
        m2c = Text("11 real · 0 padding", color=GOOD, font_size=22).next_to(m2, DOWN, buff=0.1)
        self.play(FadeIn(m1), FadeIn(m1c), run_time=0.5)
        self.play(FadeIn(m2), FadeIn(m2c), run_time=0.5)
        self.wait(1.6)
        note = Text("64% of a short row's compute is padding — then thrown away", color=INK,
                    font_size=28, weight="BOLD").to_edge(DOWN, buff=0.55)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B09_Padding")


class B10_Index(Scene):
    def construct(self):
        _bg(self)
        t = _title("The Link Is Only Position", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        left = VGroup(*[Text(f"chunks[{i}]", color=INK, font_size=26, font="monospace") for i in range(5, 9)])
        right = VGroup(*[Text(f"emb[{i}]", color=INK, font_size=26, font="monospace") for i in range(5, 9)])
        left.arrange(DOWN, buff=0.45).move_to([-3.4, 0.1, 0])
        right.arrange(DOWN, buff=0.45).move_to([3.4, 0.1, 0])
        lh = Text("text + source", color=MUTE, font_size=24).next_to(left, UP, buff=0.3)
        rh = Text("(1500, 768) · 4.4 MB", color=MUTE, font_size=24).next_to(right, UP, buff=0.3)
        self.play(FadeIn(left), FadeIn(right), FadeIn(lh), FadeIn(rh), run_time=0.8)
        for i in range(4):
            ln = Line(left[i].get_right(), right[i].get_left(), color=LINE, stroke_width=2)
            dot = Dot(ln.get_center(), color=MUTE, radius=0.07)
            self.play(Create(ln), FadeIn(dot), run_time=0.4)
        self.wait(1.4)
        hl = SurroundingRectangle(VGroup(left[2], right[2]), color=ACCENT, buff=0.15, stroke_width=3)
        hlt = Text("chunks[7] ↔ emb[7]", color=ACCENT, font_size=26, weight="BOLD").move_to([0, 1.7, 0])
        self.play(Create(hl), Write(hlt), run_time=0.7)
        self.wait(2.0)
        note = Text("no shared id — order breaks → right vector, wrong citation, silently", color=INK,
                    font_size=26, weight="BOLD").to_edge(DOWN, buff=0.55)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B10_Index")


class B13_Dilution(Scene):
    def construct(self):
        _bg(self)
        t = _title("Bigger Chunks Dilute the Vector", 42)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        sub = Text("same fact, same query — only the filler grows", color=MUTE, font_size=28).next_to(t, DOWN, buff=0.25)
        self.play(Write(sub), run_time=0.6)
        rows = [("53", "0.7254", "—", MUTE), ("217", "0.7421", "−2.3%", MUTE),
                ("381", "0.6927", "+4.5%", INK), ("709", "0.5980", "+17.6%", ACCENT),
                ("1365", "0.4681", "+35.5%", BAD)]
        xs = [-3.6, 0.2, 3.6]
        hdr = VGroup(Text("chars", color=MUTE, font_size=26).move_to([xs[0], 1.7, 0]),
                     Text("cosine", color=MUTE, font_size=26).move_to([xs[1], 1.7, 0]),
                     Text("dilution", color=MUTE, font_size=26).move_to([xs[2], 1.7, 0]))
        self.play(FadeIn(hdr), run_time=0.4)
        y = 1.0
        for chars, cos, dil, col in rows:
            r = VGroup(Text(chars, color=INK, font_size=30, font="monospace").move_to([xs[0], y, 0]),
                       Text(cos, color=col, font_size=30, weight="BOLD", font="monospace").move_to([xs[1], y, 0]),
                       Text(dil, color=col, font_size=30, weight="BOLD", font="monospace").move_to([xs[2], y, 0]))
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.45)
            self.wait(0.7)
            y -= 0.62
        note = Text("the fact is present word-for-word — it's averaged away", color=INK,
                    font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B13_Dilution")


class B14_Address(Scene):
    def construct(self):
        _bg(self)
        t = _title("The Vector Is an Address", 48)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        card = RoundedRectangle(width=3.6, height=2.2, corner_radius=0.14, fill_color=INK,
                                fill_opacity=0.08, stroke_color=INK, stroke_width=3).move_to([-3.4, 0.2, 0])
        ctxt = VGroup(Text("[0.12, -0.44, …]", color=MUTE, font_size=24, font="monospace"),
                      Text("catalog entry", color=ACCENT, font_size=26, weight="BOLD")).arrange(DOWN, buff=0.2).move_to(card.get_center())
        book = RoundedRectangle(width=3.6, height=2.2, corner_radius=0.14, fill_color="#FFFFFF",
                                fill_opacity=1.0, stroke_color=INK, stroke_width=3).move_to([3.4, 0.2, 0])
        btxt = VGroup(Text("the raw text", color=INK, font_size=28, weight="BOLD"),
                      Text("what the model reads", color=MUTE, font_size=24)).arrange(DOWN, buff=0.2).move_to(book.get_center())
        arr = Arrow(card.get_right(), book.get_left(), color=ACCENT, stroke_width=6, buff=0.15)
        self.play(FadeIn(card), FadeIn(ctxt), run_time=0.6)
        self.wait(1.6)
        self.play(GrowArrow(arr), run_time=0.4)
        self.play(FadeIn(book), FadeIn(btxt), run_time=0.6)
        self.wait(2.0)
        note = Text("dilution hurts retrieval, not the answer", color=INK,
                    font_size=30, weight="BOLD").to_edge(DOWN, buff=0.6)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B14_Address")


class B15_Metrics(Scene):
    def construct(self):
        _bg(self)
        t = _title("Hit Rate Hides, MRR Tells", 46)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        defs = VGroup(
            Text("hit rate @ k — in the top k?  (binary)", color=INK, font_size=30),
            Text("MRR — how high?  rank 1 = 1.0,  rank 2 = 0.5", color=INK, font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, 1.3, 0])
        self.play(LaggedStart(*[FadeIn(d, shift=RIGHT * 0.1) for d in defs], lag_ratio=0.3), run_time=1.2)
        self.wait(2.0)
        xs = [-3.2, 1.0, 3.6]
        hdr = VGroup(Text("chunking", color=MUTE, font_size=26).move_to([xs[0], -0.3, 0]),
                     Text("hit@3", color=MUTE, font_size=26).move_to([xs[1], -0.3, 0]),
                     Text("MRR", color=MUTE, font_size=26).move_to([xs[2], -0.3, 0]))
        r1 = VGroup(Text("fixed-size", color=INK, font_size=30).move_to([xs[0], -1.0, 0]),
                    Text("100%", color=INK, font_size=30, weight="BOLD").move_to([xs[1], -1.0, 0]),
                    Text("0.833", color=MUTE, font_size=30, weight="BOLD").move_to([xs[2], -1.0, 0]))
        r2 = VGroup(Text("recursive", color=INK, font_size=30).move_to([xs[0], -1.7, 0]),
                    Text("100%", color=INK, font_size=30, weight="BOLD").move_to([xs[1], -1.7, 0]),
                    Text("1.000", color=ACCENT, font_size=30, weight="BOLD").move_to([xs[2], -1.7, 0]))
        self.play(FadeIn(hdr), run_time=0.4)
        self.play(FadeIn(r1), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(r2), run_time=0.5)
        self.wait(1.4)
        note = Text("same hit rate — recursive ranks #1 every time", color=INK,
                    font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B15_Metrics")


def _table(scene, title_txt, headers, rows, highlight_row=None, note_txt=None, key=None):
    """Shared 3-4 col table helper for the surprise/latency scenes."""
    _bg(scene)
    t = _title(title_txt, 44)
    scene.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
    ncol = len(headers)
    span = 8.4  # total column spread, kept well inside SAFE (|x|<=6.0)
    xs = [-span / 2 + i * (span / (ncol - 1)) for i in range(ncol)] if ncol > 1 else [0]
    y0 = 1.5
    hdr = VGroup(*[Text(h, color=MUTE, font_size=25, weight="BOLD").move_to([xs[i], y0, 0]) for i, h in enumerate(headers)])
    scene.play(FadeIn(hdr), run_time=0.4)
    line = Line([xs[0] - 0.6, y0 - 0.35, 0], [xs[-1] + 0.6, y0 - 0.35, 0], color=LINE, stroke_width=2)
    scene.play(Create(line), run_time=0.3)
    y = y0 - 0.95
    for ri, row in enumerate(rows):
        col = ACCENT if ri == highlight_row else INK
        # per-row swatch (a non-text shape) — distinct state per row, plus visual weight
        swatch = Square(side_length=0.28, fill_color=(ACCENT if ri == highlight_row else MUTE),
                        fill_opacity=0.9, stroke_width=0).move_to([xs[0] - 1.05, y, 0])
        cells = VGroup(*[Text(str(c), color=(col if j == 0 else col), font_size=25,
                              weight=("BOLD" if (ri == highlight_row or j > 0) else "NORMAL"),
                              font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                         for j, c in enumerate(row)])
        if ri == highlight_row:
            box = SurroundingRectangle(cells, color=ACCENT, buff=0.14, stroke_width=2.5, corner_radius=0.06)
            scene.play(GrowFromCenter(swatch), FadeIn(cells), Create(box), run_time=0.5)
        else:
            scene.play(GrowFromCenter(swatch), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.8)
        y -= 0.78
    if note_txt:
        note = Text(note_txt, color=INK, font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)
        scene.play(Write(note), run_time=0.7)
    _fill(scene, key)


class B16_Models(Scene):
    def construct(self):
        _table(self, "Surprise 1 — Smaller Won",
               ["model", "dim", "hit@5", "MRR"],
               [["mpnet", "768", "76%", "0.655"],
                ["MiniLM", "384", "76%", "0.637"],
                ["bge-small", "384", "88%", "0.683"]],
               highlight_row=2,
               note_txt="training objective beats raw dimension count",
               key="B16_Models")


class B17_HybridWorse(Scene):
    def construct(self):
        _table(self, "Surprise 2 — Hybrid Lost",
               ["retriever", "hit@5", "MRR"],
               [["dense only", "76%", "0.655"],
                ["BM25 only", "84%", "0.750"],
                ["hybrid (equal)", "80%", "0.733"]],
               highlight_row=2,
               note_txt="equal-weight fusion drags the stronger signal down",
               key="B17_HybridWorse")


class B18_Sweep(Scene):
    def construct(self):
        _bg(self)
        t = _title("Surprise 3 — Weighted, It Wins", 44)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        # axes
        ax_l, ax_r, base, top = -4.8, 4.8, -2.2, 1.8
        xaxis = Line([ax_l, base, 0], [ax_r, base, 0], color=LINE, stroke_width=2.5)
        yaxis = Line([ax_l, base, 0], [ax_l, top + 0.2, 0], color=LINE, stroke_width=2.5)
        self.play(Create(xaxis), Create(yaxis), run_time=0.5)
        xl = Text("dense weight  0 → 1", color=MUTE, font_size=24).next_to(xaxis, DOWN, buff=0.2)
        yl = Text("MRR", color=MUTE, font_size=24).next_to(yaxis, UP, buff=0.1)
        self.play(FadeIn(xl), FadeIn(yl), run_time=0.4)
        # MRR curve: 0.750 -> peak 0.810 @0.2-0.3 -> down to 0.655
        pts_data = [(0.0, 0.750), (0.2, 0.810), (0.3, 0.810), (0.5, 0.733), (0.7, 0.683), (1.0, 0.655)]

        def px(w):
            return ax_l + (ax_r - ax_l) * w
        def py(m):
            return base + (top - base) * (m - 0.64) / (0.82 - 0.64)
        pts = [[px(w), py(m), 0] for w, m in pts_data]
        curve = VMobject(color=ACCENT, stroke_width=5).set_points_as_corners(pts)
        self.play(Create(curve), run_time=1.6)
        peak = Dot(pts[1], color=ACCENT, radius=0.13)
        pk = Text("0.810 — best in the project", color=ACCENT, font_size=28, weight="BOLD").move_to([0.6, top - 0.1, 0])
        self.play(FadeIn(peak, scale=1.4), Write(pk), run_time=0.7)
        self.wait(1.8)
        flat = Text("hit rate flat at 84% — dense reorders, it doesn't recall", color=INK,
                    font_size=28, weight="BOLD").to_edge(DOWN, buff=0.5)
        self.play(Write(flat), run_time=0.7)
        _fill(self, "B18_Sweep")


class B19_Latency(Scene):
    def construct(self):
        _bg(self)
        t = _title("Where the Time Goes", 48)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        stages = [("embed", 40.9, MUTE), ("retrieve", 4.0, GOOD), ("rerank", 301.5, INK), ("generate", 1287.9, BAD)]
        total = sum(s[1] for s in stages)
        barY, h, left = 0.8, 1.0, -5.4
        x = left
        segs = VGroup()
        labels = VGroup()
        for name, ms, col in stages:
            w = 10.8 * ms / total
            seg = Rectangle(width=max(w, 0.04), height=h, fill_color=col, fill_opacity=0.85,
                            stroke_color=BG, stroke_width=2).move_to([x + w / 2, barY, 0])
            segs.add(seg)
            lab = Text(f"{name}\n{ms:.0f}ms", color=INK, font_size=22, line_spacing=0.7).move_to([x + w / 2, barY - 1.2, 0])
            labels.add(lab)
            x += w
        for i in range(len(segs)):
            self.play(GrowFromEdge(segs[i], LEFT), FadeIn(labels[i]), run_time=0.5)
            self.wait(0.7)
        self.wait(1.0)
        note = Text("vector search = 0.2%.  generation = 320× the search.", color=INK,
                    font_size=32, weight="BOLD").to_edge(DOWN, buff=0.7)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B19_Latency")


class B20_Cache(Scene):
    def construct(self):
        _bg(self)
        t = _title("Cache Beats Everything", 48)
        self.play(FadeIn(t, shift=DOWN * 0.2), run_time=0.6)
        rows = [("retrieve only", "45.0 ms", MUTE), ("+ rerank", "346.4 ms", INK),
                ("+ generation", "1634.4 ms", BAD), ("cache hit", "0.002 ms", GOOD)]
        grp = VGroup()
        for lab, val, col in rows:
            l = Text(lab, color=INK, font_size=32, font="monospace")
            v = Text(val, color=col, font_size=34, weight="BOLD", font="monospace")
            grp.add(VGroup(l, v).arrange(RIGHT, buff=0.8))
        grp.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to([0, 0.4, 0])
        for r in grp:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.5)
            self.wait(1.0)
        note = Text("a cache hit is 800,000× faster — it skips everything", color=ACCENT,
                    font_size=32, weight="BOLD").to_edge(DOWN, buff=0.6)
        self.play(Write(note), run_time=0.7)
        _fill(self, "B20_Cache")


class B21_Scale(Scene):
    def construct(self):
        _table(self, "At Scale: Approximate Search",
               ["index", "mechanism", "trade-off"],
               [["Flat", "compare all", "exact"],
                ["HNSW", "prox. graph", "log n · RAM"],
                ["IVF", "cluster route", "tune nprobe"],
                ["IVF-PQ", "IVF+compress", "huge · lossy"]],
               highlight_row=1,
               note_txt="storage = chunks × dims × 4 bytes — halving dims pays twice",
               key="B21_Scale")
