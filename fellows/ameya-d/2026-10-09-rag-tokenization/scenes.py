"""
Manim scenes for rag-tokenization (RAG series). Claude fidelity palette.
Grounded in VIDEO_SCRIPT.md SEGMENT 3. SAFE: |x|<=6.0, |y|<=3.3; auto-fill via _fill().
"""
from manim import *

BG = "#FAF9F5"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#8A8578"
GOOD = "#4A7C59"; BAD = "#C0392B"; LINE = "#B8B0A0"

TARGET = {"B01_Vocab": 16.6, "B02_Compare": 17.49, "B03_Shred": 17.19, "B04_Ratio": 18.62, "B05_Consequences": 19.52, "B06_Truncation": 18.09, "B08_Fix": 19.61}


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


def _tokrow(tokens, y, accent_idx=(), fs=24, buff=0.14):
    chips = VGroup()
    for i, tk in enumerate(tokens):
        col = ACCENT if i in accent_idx else INK
        c = _chip(tk, w=max(0.5, 0.28 * len(tk) + 0.42), h=0.6, fill=col, op=0.14, fs=fs, tcol=col, mono=True)
        chips.add(c)
    chips.arrange(RIGHT, buff=buff).move_to([0, y, 0])
    return chips


class B01_Vocab(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("A ~30k Subword Vocabulary"), shift=DOWN * 0.2), run_time=0.6)
        common = _chip("\"the\"  →  1 token", w=5.6, h=1.1, fill=GOOD, op=0.12, fs=30, tcol=GOOD).move_to([0, 1.3, 0])
        self.play(FadeIn(common, shift=DOWN * 0.1), run_time=0.6); self.wait(0.8)
        rare = _chip("\"EBITDA\"  →  shredded", w=6.4, h=1.1, fill=BAD, op=0.10, fs=30, tcol=BAD).move_to([0, -0.3, 0])
        self.play(FadeIn(rare, shift=UP * 0.1), run_time=0.6); self.wait(0.9)
        self.play(Write(Text("in the vocabulary → one token. outside it → pieces.", color=INK,
                             font_size=27, weight="BOLD").move_to([0, -2.2, 0])), run_time=0.8)
        _fill(self, "B01_Vocab")


class B02_Compare(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Same 20 Characters"), shift=DOWN * 0.2), run_time=0.6)
        h1 = Text("'the cat sat on a mat'   —   20 chars → 6 tokens", color=INK, font_size=27, weight="BOLD").move_to([0, 2.0, 0])
        self.play(FadeIn(h1), run_time=0.5)
        r1 = _tokrow(["the", "cat", "sat", "on", "a", "mat"], 1.15, fs=24)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in r1], lag_ratio=0.15, run_time=1.0)); self.wait(0.7)
        h2 = Text("'$4,829.17 EBITDA Q3x'   —   20 chars → 13 tokens", color=ACCENT, font_size=27, weight="BOLD").move_to([0, -0.05, 0])
        self.play(FadeIn(h2), run_time=0.5)
        r2a = _tokrow(["$", "4", ",", "82", "##9", ".", "17"], -1.0, accent_idx=range(7), fs=22, buff=0.12)
        r2b = _tokrow(["e", "##bit", "##da", "q", "##3", "##x"], -1.78, accent_idx=range(6), fs=22, buff=0.12)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in r2a], lag_ratio=0.08, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in r2b], lag_ratio=0.08, run_time=0.8)); self.wait(0.5)
        self.play(Write(Text("identical length — more than double the tokens", color=INK,
                             font_size=26, weight="BOLD").move_to([0, -3.0, 0])), run_time=0.7)
        _fill(self, "B02_Compare")


class B03_Shred(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("How It Shreds"), shift=DOWN * 0.2), run_time=0.6)
        r = _tokrow(["e", "##bit", "##da"], 1.4, accent_idx=(1, 2), fs=30, buff=0.2)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in r], lag_ratio=0.2, run_time=0.9)); self.wait(0.6)
        self.play(Write(Text("'##' = continues the previous word, no space", color=INK, font_size=27, weight="BOLD").move_to([0, 0.2, 0])), run_time=0.7)
        self.wait(0.6)
        self.play(Write(Text("$4,829.17  →  7 tokens for 9 characters", color=ACCENT, font_size=30, weight="BOLD").move_to([0, -1.2, 0])), run_time=0.7)
        self.wait(0.6)
        self.play(Write(Text("rare tokens are expensive tokens", color=MUTE, font_size=26, slant="ITALIC").move_to([0, -2.7, 0])), run_time=0.6)
        _fill(self, "B03_Shred")


class B04_Ratio(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Characters per Token"), shift=DOWN * 0.2), run_time=0.6)
        rows = [("Meridian Financial Corp reported", 8.00, GOOD),
                ("the cat sat on the mat today", 4.00, INK),
                ("$482,391.57 EBITDA Q4 YoY", 1.67, BAD)]
        grp = VGroup()
        for label, val, col in rows:
            w = 0.5 + 6.6 * val / 8.0
            bar = RoundedRectangle(width=w, height=0.66, corner_radius=0.08, fill_color=col, fill_opacity=0.8, stroke_width=0)
            bar.move_to([w / 2 - 3.2, 0, 0])
            v = Text(f"{val:.2f}", color=BG, font_size=24, weight="BOLD").move_to(bar.get_center())
            lab = Text(label, color=INK, font_size=21).next_to(bar, UP, buff=0.12, aligned_edge=LEFT)
            grp.add(VGroup(lab, bar, v))
        grp.arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to([0.2, 0.2, 0])
        for row in grp:
            self.play(FadeIn(row[0]), GrowFromEdge(row[1], LEFT), FadeIn(row[2]), run_time=0.6); self.wait(0.5)
        self.play(Write(Text("higher = more efficient — dense finance drops to 1.67", color=INK,
                             font_size=25, weight="BOLD").move_to([0, -3.0, 0])), run_time=0.8)
        _fill(self, "B04_Ratio")


class B05_Consequences(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("2–3× Worse: Three Costs"), shift=DOWN * 0.2), run_time=0.6)
        cards = VGroup()
        for head, sub, col in [("cost", "APIs bill per token", INK),
                               ("context", "window is in tokens", INK),
                               ("truncation", "the sneaky one", ACCENT)]:
            box = RoundedRectangle(width=3.6, height=2.0, corner_radius=0.14, fill_color=col,
                                   fill_opacity=0.10, stroke_color=col, stroke_width=3)
            h = Text(head, color=col, font_size=30, weight="BOLD").move_to(box.get_center() + UP * 0.45)
            s = Text(sub, color=INK, font_size=22).move_to(box.get_center() + DOWN * 0.4)
            cards.add(VGroup(box, h, s))
        cards.arrange(RIGHT, buff=0.4).move_to([0, 0.1, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.5); self.wait(0.7)
        self.play(Write(Text("same document, 2–3× more tokens", color=MUTE, font_size=26, slant="ITALIC").move_to([0, -2.6, 0])), run_time=0.7)
        _fill(self, "B05_Consequences")


class B06_Truncation(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Silent Truncation"), shift=DOWN * 0.2), run_time=0.6)
        kept = RoundedRectangle(width=5.2, height=1.0, corner_radius=0.1, fill_color=GOOD, fill_opacity=0.14, stroke_color=GOOD, stroke_width=3).move_to([-1.6, 1.2, 0])
        kt = Text("first 384 tokens — embedded", color=GOOD, font_size=24, weight="BOLD").move_to(kept.get_center())
        lost = RoundedRectangle(width=3.4, height=1.0, corner_radius=0.1, fill_color=BAD, fill_opacity=0.10, stroke_color=BAD, stroke_width=3).move_to([3.4, 1.2, 0])
        ltx = Text("the rest — discarded", color=BAD, font_size=22, weight="BOLD").move_to(lost.get_center())
        self.play(FadeIn(kept), FadeIn(kt), run_time=0.6); self.wait(0.5)
        self.play(FadeIn(lost), FadeIn(ltx), run_time=0.6); self.wait(0.7)
        self.play(Write(Text("all-mpnet-base-v2: no error, no warning", color=BAD, font_size=28, weight="BOLD").move_to([0, -0.6, 0])), run_time=0.7)
        self.wait(0.6)
        self.play(Write(Text("token-heavy chunks hit the wall sooner than chars suggest", color=INK,
                             font_size=25, weight="BOLD").move_to([0, -2.6, 0])), run_time=0.8)
        _fill(self, "B06_Truncation")


class B08_Fix(Scene):
    def construct(self):
        _bg(self)
        self.play(FadeIn(_title("Chunk by Tokens"), shift=DOWN * 0.2), run_time=0.6)
        steps = VGroup(
            Text("count tokens with the model's own tokenizer", color=INK, font_size=28),
            Text("set chunk limits in tokens, not characters", color=INK, font_size=28, weight="BOLD"),
            Text("then a 400-char / 600-token chunk can't ambush you", color=ACCENT, font_size=27, weight="BOLD"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to([0, 0.3, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.1), run_time=0.6); self.wait(0.8)
        _fill(self, "B08_Fix")
