"""
Manim scenes for rag-chunking (RAG series). Claude fidelity palette.
Grounded in VIDEO_SCRIPT.md SEGMENT 2. SAFE: |x|<=6.0, |y|<=3.3; auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_StepSize": 15.62, "B02_Overlap": 14.72, "B03_Recursive": 16.0, "B04_EightTen": 18.24, "B05_Histogram": 20.8, "B06_ByType": 16.9, "B08_IsolationTest": 18.69}


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
        cells = VGroup(*[Text(str(c), color=INK, font_size=23, weight=("BOLD" if j > 0 else "NORMAL"),
                             font=("monospace" if j > 0 else "sans-serif")).move_to([xs[j], y, 0])
                        for j, c in enumerate(rowv)])
        scene.play(GrowFromCenter(sw), FadeIn(cells, shift=RIGHT * 0.1), run_time=0.45)
        scene.wait(0.55); y -= 0.72
    if note_txt:
        scene.play(Write(Text(note_txt, color=ACCENT, font_size=26, weight="BOLD").move_to([0, -3.05, 0])), run_time=0.7)
    _fill(scene, key)


class B01_StepSize(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Step = Size − Overlap"), shift=DOWN * 0.2), run_time=0.6)
        letters = "ABCDEFGHIJ"
        row = VGroup(*[Square(side_length=0.62, fill_color=INK, fill_opacity=0.07, stroke_color=INK, stroke_width=2) for _ in letters])
        row.arrange(RIGHT, buff=0.12).move_to([0, 2.0, 0])
        labs = VGroup(*[Text(c, color=INK, font_size=26, weight="BOLD").move_to(row[i]) for i, c in enumerate(letters)])
        self.play(LaggedStart(*[FadeIn(b) for b in row], lag_ratio=0.05, run_time=0.8), FadeIn(labs))
        wins = [(0, 4, [3]), (3, 7, [3, 6]), (6, 10, [6, 9]), (9, 10, [9])]
        y = 0.9
        for a, b, reps in wins:
            box = SurroundingRectangle(VGroup(*row[a:b]), color=ACCENT, buff=0.08, stroke_width=4, corner_radius=0.08).copy()
            box.move_to([row[a:b].get_center()[0], y, 0]).stretch_to_fit_height(0.5)
            seg = VGroup(*[Text(letters[i], color=(ACCENT if i in reps else INK), font_size=24,
                               weight="BOLD").move_to([row[i].get_center()[0], y, 0]) for i in range(a, b)])
            self.play(FadeIn(seg, shift=DOWN * 0.1), run_time=0.4); self.wait(0.35)
            y -= 0.62
        self.play(Write(Text("size=4, overlap=1  →  step=3  (repeats in terracotta)", color=INK,
                             font_size=26, weight="BOLD").move_to([0, -3.0, 0])), run_time=0.7)
        _fill(self, "B01_StepSize")


class B02_Overlap(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Why Overlap"), shift=DOWN * 0.2), run_time=0.6)
        sent = Text("…revenue rose 40% | in the third quarter…", color=INK, font_size=30).move_to([0, 1.6, 0])
        cut = DashedLine([0.0, 2.1, 0], [0.0, 1.1, 0], color=BAD, stroke_width=5)
        self.play(FadeIn(sent), run_time=0.5)
        self.play(Create(cut), run_time=0.4)
        bad = _chip("no overlap: fact cut in half", w=6.6, h=1.0, fill=BAD, op=0.10, fs=27, tcol=BAD).move_to([0, 0.1, 0])
        good = _chip("overlap: the seam repeats — fact survives", w=8.0, h=1.0, fill=GOOD, op=0.12, fs=27, tcol=GOOD).move_to([0, -1.4, 0])
        self.play(FadeIn(bad, shift=UP * 0.1), run_time=0.6); self.wait(1.0)
        self.play(FadeIn(good, shift=UP * 0.1), run_time=0.6); self.wait(1.0)
        self.play(Write(Text("overlap is a small insurance policy at each seam", color=MUTE,
                             font_size=25, slant="ITALIC").move_to([0, -3.0, 0])), run_time=0.7)
        _fill(self, "B02_Overlap")


class B03_Recursive(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Fixed Is Blind — Go Recursive"), shift=DOWN * 0.2), run_time=0.6)
        fixed = Text("fixed:  cuts at 400 chars — even mid-word", color=BAD, font_size=28, weight="BOLD").move_to([0, 1.7, 0])
        self.play(FadeIn(fixed, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.8)
        seps = ['"\\n\\n"', '"\\n"', '". "', '" "', '""']
        chips = VGroup(*[_chip(s, w=1.7, h=0.9, fill=INK, op=0.10, fs=26, tcol=INK) for s in seps])
        chips.arrange(RIGHT, buff=0.4).move_to([0, 0.2, 0])
        for i, c in enumerate(chips):
            self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.35)
            if i < len(chips) - 1:
                self.play(GrowArrow(Arrow(chips[i].get_right(), chips[i + 1].get_left(), color=ACCENT, stroke_width=4, buff=0.05)), run_time=0.2)
        self.play(Write(Text("try paragraphs → lines → sentences → words → chars", color=INK,
                             font_size=26, weight="BOLD").move_to([0, -1.4, 0])), run_time=0.7)
        self.play(Write(Text("stop at the first boundary that fits", color=MUTE, font_size=25, slant="ITALIC").move_to([0, -3.0, 0])), run_time=0.6)
        _fill(self, "B03_Recursive")


class B04_EightTen(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Same Settings, Different Output"), shift=DOWN * 0.2), run_time=0.6)
        note = Text("chunk_size = 400   ·   overlap = 50", color=MUTE, font_size=28).move_to([0, 1.9, 0])
        self.play(FadeIn(note), run_time=0.5)
        a = _chip("fixed  →  8 chunks", w=5.2, h=1.3, fill=MUTE, op=0.16, fs=32).move_to([-3.0, 0.1, 0])
        b = _chip("recursive  →  10 chunks", w=5.6, h=1.3, fill=ACCENT, op=0.14, fs=32).move_to([3.0, 0.1, 0])
        self.play(FadeIn(a, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.8)
        self.play(FadeIn(b, shift=LEFT * 0.1), run_time=0.6); self.wait(0.8)
        self.play(Write(Text("recursive won't pack to the limit — size is a ceiling", color=INK,
                             font_size=27, weight="BOLD").move_to([0, -1.8, 0])), run_time=0.8)
        _fill(self, "B04_EightTen")


class B05_Histogram(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("1,500 Chunks — Bimodal"), shift=DOWN * 0.2), run_time=0.6)
        bars = [("50–99", 564), ("100–149", 336), ("300–349", 96), ("350–399", 504)]
        mx = 564
        grp = VGroup()
        for label, v in bars:
            w = 0.5 + 7.0 * v / mx
            bar = RoundedRectangle(width=w, height=0.7, corner_radius=0.08,
                                   fill_color=(ACCENT if v > 400 else INK), fill_opacity=0.8, stroke_width=0)
            bar.move_to([w / 2 - 4.2, 0, 0])
            lab = Text(label, color=INK, font_size=22, weight="BOLD").next_to(bar, LEFT, buff=0.25)
            val = Text(str(v), color=INK, font_size=22).next_to(bar, RIGHT, buff=0.2)
            grp.add(VGroup(lab, bar, val))
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to([0.4, 0.5, 0])
        for row in grp:
            self.play(GrowFromEdge(row, LEFT), run_time=0.5); self.wait(0.4)
        self.play(Write(Text("min 67 · max 388 · mean 202 · median 104", color=MUTE,
                             font_size=25).move_to([0, -2.5, 0])), run_time=0.7)
        self.play(Write(Text("chunk_size is a ceiling, not a target", color=ACCENT,
                             font_size=27, weight="BOLD").move_to([0, -3.05, 0])), run_time=0.6)
        _fill(self, "B05_Histogram")


class B06_ByType(Scene):
    def construct(self):
        _table(self, "Chunk by Data Type",
               ["data", "how"],
               [["prose", "recursive, 500–1000"],
                ["code", "function boundaries"],
                ["tables", "rows + repeat header"],
                ["contracts", "by clause"],
                ["transcripts", "by speaker turn"]],
               note_txt="one size does not fit your data",
               key="B06_ByType")


class B08_IsolationTest(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Isolation Test"), shift=DOWN * 0.2), run_time=0.6)
        card = RoundedRectangle(width=9.0, height=1.7, corner_radius=0.16, fill_color=BAD,
                                fill_opacity=0.08, stroke_color=BAD, stroke_width=3).move_to([0, 1.2, 0])
        txt = Text("\"…increased 40% due to this factor.\"", color=INK, font_size=30, weight="BOLD").move_to(card.get_center())
        self.play(FadeIn(card), Write(txt), run_time=0.9); self.wait(0.8)
        q = Text("increased — what?  no subject in the chunk.", color=BAD, font_size=28, weight="BOLD").move_to([0, -0.5, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.6); self.wait(1.0)
        self.play(Write(Text("if a chunk can't be understood alone, the chunking is wrong", color=INK,
                             font_size=26, weight="BOLD").move_to([0, -2.6, 0])), run_time=0.8)
        _fill(self, "B08_IsolationTest")
