"""
Manim scenes for rag-reranking (RAG-series episode on reranking).
Claude fidelity palette: cream #FAF9F5, ink #3D3929, one terracotta #D97757.
Numbers are real, from fin-disclosure-rag (rerank.py, benchmark.py — see SOURCES.md).
Coordinates kept inside SAFE (|x|<=6.0, |y|<=3.3); scenes auto-fill to audio via _fill().
"""

from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

# Filled from measured Kokoro audio durations (ground truth).
TARGET = {
    "B01_Problem": 20.33, "B02_Encoders": 22.46, "B03_Mechanism": 18.73,
    "B04_TwoStage": 20.71, "B06_Cost": 21.29, "B07_When": 21.57,
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


class B01_Problem(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Good Context, Wrong Order"), shift=DOWN * 0.2), run_time=0.6)
        # the top-3 window the model actually reads
        window = RoundedRectangle(width=5.2, height=2.5, corner_radius=0.16, fill_color=INK,
                                  fill_opacity=0.05, stroke_color=INK, stroke_width=3).move_to([-2.6, 0.4, 0])
        wlabel = Text("the model reads top 3", color=MUTE, font_size=24).next_to(window, UP, buff=0.18)
        rows = VGroup()
        for r in (1, 2, 3):
            rows.add(_chip(f"#{r}  near-miss chunk", w=4.6, h=0.6, fill=MUTE, op=0.12, fs=24, tcol=INK))
        rows.arrange(DOWN, buff=0.22).move_to(window.get_center())
        self.play(FadeIn(window), FadeIn(wlabel), run_time=0.5)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.3)
        self.wait(0.6)
        # the actual best match, stuck at rank 7
        best = _chip("best match · rank 7", w=4.6, h=0.9, fill=ACCENT, op=0.14, fs=27, tcol=INK).move_to([2.9, -1.1, 0])
        self.play(FadeIn(best, shift=UP * 0.1), run_time=0.5)
        arr = Arrow(best.get_top(), window.get_corner(DR) + [-0.3, 0.1, 0], color=ACCENT, stroke_width=5, buff=0.15)
        self.play(GrowArrow(arr), run_time=0.5)
        self.wait(0.6)
        self.play(Write(Text("the right passage is found — just ranked too low", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B01_Problem")


class B02_Encoders(Scene):
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
        self.play(Write(Text("separate = fast to retrieve · together = accurate to rank", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B02_Encoders")


class B03_Mechanism(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("The Second Pass"), shift=DOWN * 0.2), run_time=0.6)
        query = _chip("query", w=2.2, h=0.9, fill=ACCENT, op=0.14, fs=28).move_to([-4.4, 0, 0])
        self.play(FadeIn(query, shift=RIGHT * 0.1), run_time=0.4)
        cands = VGroup()
        for i in range(3):
            cands.add(_chip(f"candidate {i+1}", w=2.5, h=0.7, fill=MUTE, op=0.12, fs=24, tcol=INK))
        cands.arrange(DOWN, buff=0.4).move_to([-1.4, 0, 0])
        ce = RoundedRectangle(width=2.5, height=2.4, corner_radius=0.16, fill_color=INK,
                              fill_opacity=0.08, stroke_color=INK, stroke_width=3).move_to([1.5, 0, 0])
        ce_t = Text("cross-\nencoder", color=INK, font_size=26, weight="BOLD", line_spacing=0.7).move_to(ce.get_center())
        self.play(FadeIn(cands, shift=RIGHT * 0.1), run_time=0.5)
        self.play(FadeIn(ce), FadeIn(ce_t), run_time=0.5)
        for c in cands:
            self.play(GrowArrow(Arrow(query.get_right(), c.get_left(), color=ACCENT, stroke_width=3, buff=0.12)),
                      GrowArrow(Arrow(c.get_right(), ce.get_left(), color=LINE, stroke_width=3, buff=0.12)), run_time=0.22)
        scores = VGroup(
            _chip("score 0.9", w=2.3, h=0.66, fill=ACCENT, op=0.16, fs=24, tcol=INK),
            _chip("score 0.6", w=2.3, h=0.66, fill=MUTE, op=0.12, fs=24, tcol=INK),
            _chip("score 0.2", w=2.3, h=0.66, fill=MUTE, op=0.10, fs=24, tcol=INK),
        ).arrange(DOWN, buff=0.34).move_to([4.4, 0, 0])
        self.play(GrowArrow(Arrow(ce.get_right(), scores.get_left(), color=ACCENT, stroke_width=4, buff=0.12)), run_time=0.3)
        for s in scores:
            self.play(FadeIn(s, shift=RIGHT * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(Write(Text("the retriever finds · the reranker decides", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B03_Mechanism")


class B04_TwoStage(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Retrieve Wide, Rerank Narrow"), shift=DOWN * 0.2), run_time=0.6)
        # stage 1: wide net of candidates
        wide = VGroup(*[Dot(color=MUTE, radius=0.16) for _ in range(10)])
        wide.arrange_in_grid(rows=2, cols=5, buff=(0.5, 0.5)).move_to([-3.4, 0.3, 0])
        w_lbl = Text("retrieve 20 · fast · wide", color=INK, font_size=26, weight="BOLD").next_to(wide, DOWN, buff=0.4)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in wide], lag_ratio=0.06), run_time=1.0)
        self.play(FadeIn(w_lbl), run_time=0.4)
        self.wait(0.8)
        rr = _chip("rerank", w=2.0, h=1.1, fill=INK, op=0.10, fs=28).move_to([0.4, 0.3, 0])
        self.play(GrowArrow(Arrow(wide.get_right(), rr.get_left(), color=ACCENT, stroke_width=5, buff=0.2)),
                  FadeIn(rr), run_time=0.6)
        # stage 2: narrow, precise
        narrow = VGroup(*[Dot(color=ACCENT, radius=0.2) for _ in range(3)])
        narrow.arrange(DOWN, buff=0.45).move_to([3.6, 0.3, 0])
        n_lbl = Text("keep 3 · precise · narrow", color=ACCENT, font_size=26, weight="BOLD").next_to(narrow, DOWN, buff=0.4)
        self.play(GrowArrow(Arrow(rr.get_right(), narrow.get_left(), color=ACCENT, stroke_width=5, buff=0.2)), run_time=0.4)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in narrow], lag_ratio=0.2), FadeIn(n_lbl), run_time=0.7)
        self.wait(0.6)
        self.play(Write(Text("recall of a big search · precision of a slow model", color=INK,
                             font_size=27, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B04_TwoStage")


class B06_Cost(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Where The Time Goes"), shift=DOWN * 0.2), run_time=0.6)
        x0 = -2.2                      # bars start here; labels sit to the left
        scale = 5.6 / 1288.0           # generation bar ~5.6 units wide
        rows = [("generation", 1288, "1288 ms", INK, 1.3),
                ("rerank", 301, "301 ms", ACCENT, 0.0),
                ("search", 4, "4 ms", MUTE, -1.3)]
        for name, ms, lab, col, y in rows:
            nm = Text(name, color=INK, font_size=26, weight="BOLD")
            nm.next_to([-5.7, y, 0], RIGHT, buff=0.0)   # left edge pinned at -5.7 (inside safe)
            w = max(ms * scale, 0.07)
            bar = Rectangle(width=w, height=0.6, fill_color=col, fill_opacity=0.85, stroke_width=0)
            bar.move_to([x0 + w / 2, y, 0])
            val = Text(lab, color=col, font_size=25, weight="BOLD").next_to(bar, RIGHT, buff=0.25)
            self.play(FadeIn(nm), GrowFromEdge(bar, LEFT), FadeIn(val), run_time=0.6)
            self.wait(0.6)
        self.play(Write(Text("a shortlist tax, not a search tax", color=ACCENT,
                             font_size=30, weight="BOLD").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B06_Cost")


class B07_When(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("When To Reach For It"), shift=DOWN * 0.2), run_time=0.6)

        def col(left_edge_x, head, items, c):
            rows = VGroup()
            for it in items:
                dot = Square(side_length=0.24, fill_color=c, fill_opacity=0.9, stroke_width=0)
                t = Text(it, color=INK, font_size=24)
                rows.add(VGroup(dot, t).arrange(RIGHT, buff=0.26))
            rows.arrange(DOWN, aligned_edge=LEFT, buff=0.44)
            h = Text(head, color=c, font_size=27, weight="BOLD")
            grp = VGroup(h, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            grp.next_to([left_edge_x, 0.3, 0], RIGHT, buff=0.0)   # pin left edge inside safe
            return h, rows
        lh, lrows = col(-5.9, "rerank when it matters",
                        ["support answers", "financial disclosures", "answers you stand behind"], ACCENT)
        rh, rrows = col(0.5, "it also trims context",
                        ["10 mediocre chunks", "→ 3 strong chunks", "fewer tokens, cleaner"], INK)
        div = Line([0, 2.0, 0], [0, -1.6, 0], color=LINE, stroke_width=2)
        self.play(FadeIn(lh), FadeIn(rh), Create(div), run_time=0.7)
        for i in range(3):
            self.play(GrowFromCenter(lrows[i][0]), FadeIn(lrows[i][1], shift=RIGHT * 0.1), run_time=0.4)
            self.play(GrowFromCenter(rrows[i][0]), FadeIn(rrows[i][1], shift=RIGHT * 0.1), run_time=0.4)
            self.wait(0.55)
        self.play(Write(Text("low-stakes chatbot? perfectly fine to skip it", color=MUTE,
                             font_size=26, slant="ITALIC").to_edge(DOWN, buff=0.5)), run_time=0.7)
        _fill(self, "B07_When")
