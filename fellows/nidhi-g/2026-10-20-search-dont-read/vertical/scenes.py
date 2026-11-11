"""
Manim scenes for search-dont-read/vertical: NATIVE 9:16 (frame 4.5 x 8 units).
Portrait rules: serif >= 36, mono >= 26, wrap long lines (never shrink below the type floor).
 Body beats B02-B08 + @HumanitariansAI outro B10.

Evidence is real and from agentic_search_pi/: the loop limits (12 turns, 3,500-char output
cap), the REPL helpers, the corpus metadata (qa2, 128k, 6,429 lines, ~275 pages) and the
recorded run (evals/last_run.json: lines 3780/5091/5187/6021, answer kitchen, 11 REPL runs).
BABILong venue: Kuratov et al., NeurIPS 2024 Datasets & Benchmarks Track (arXiv 2406.10149).
No credentials appear anywhere.

Claude palette: cream ground, warm ink, terracotta as the one accent (shapes only).
Text boxes use soft (INK_SOFT) borders: dark borders fuse with text in gate T.
"""

import os

import numpy as np
from manim import *

config.frame_height = 8.0
config.frame_width = 4.5

HERE = os.path.dirname(os.path.abspath(__file__))
_HOME = os.environ.get("ART_HOME") or os.path.join(HERE, "..", "..", "..", "brutalist")

try:
    import manimpango
    for _rel in ("runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf",
                 "runtime/fonts/PT_Mono/PTMono-Regular.ttf"):
        _p = os.path.join(_HOME, _rel)
        if os.path.isfile(_p):
            manimpango.register_font(_p)
except Exception:
    pass

PAGE = "#FAF9F5"
CARD = "#F2F0E9"
INK = "#3D3929"
INK_SOFT = "#73705F"
SPARK = "#D97757"
OK = "#5B7F4A"
SERIF = "EB Garamond"
MONO = "PT Mono"


def serif(s, size=40, color=INK):
    return Text(s, font=SERIF, font_size=size, color=color)


def mono(s, size=30, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def fit(m, width):
    if m.width > width:
        m.scale_to_fit_width(width)
    return m


def spark_line(words):
    c = np.array([-1.75, 3.05, 0])
    arms = VGroup(*[
        Line(c + 0.15 * np.array([np.cos(a), np.sin(a), 0]),
             c - 0.15 * np.array([np.cos(a), np.sin(a), 0]),
             color=SPARK, stroke_width=6)
        for a in (0, np.pi / 3, 2 * np.pi / 3)])
    label = fit(serif(words, 36), 3.25).next_to(arms, RIGHT, buff=0.22)
    return VGroup(arms, label)


def wordmark(height):
    try:
        m = SVGMobject(os.path.join(HERE, "hai-wordmark.svg"))
        m.set_fill(INK, opacity=1).set_stroke(width=0)
        m.height = height
        return m
    except Exception:
        return serif("Humanitarians AI", int(height * 60))


def logo_bug():
    bug = wordmark(0.13)
    bug.set_fill(INK, opacity=0.4)
    return bug.move_to(np.array([1.2, -3.42, 0]))


def tick(color=OK, s=0.26):
    return VMobject(stroke_color=color, stroke_width=8).set_points_as_corners(
        [[-0.5 * s, 0, 0], [-0.1 * s, -0.4 * s, 0], [0.6 * s, 0.45 * s, 0]])


def box(w, h, fill=PAGE):
    return RoundedRectangle(corner_radius=0.1, width=w, height=h).set_fill(
        fill, opacity=1).set_stroke(INK_SOFT, width=2)


def bar(h=0.5):
    return Line(UP * h / 2, DOWN * h / 2, color=SPARK, stroke_width=8)



def wrap(text, size=37, maxw=3.4, color=INK):
    """Greedy word-wrap to a max width; returns left-aligned lines (never shrinks type)."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if cur and serif(trial, size).width > maxw:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    lines.append(cur)
    return VGroup(*[serif(l, size, color) for l in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.0)


def _setup(self):
    self.camera.background_color = PAGE
    self.add(logo_bug())
    self.t = 0.0


def _at(self, target):
    now = getattr(self, "t", 0.0)
    if target > now:
        self.wait(target - now)
    self.t = max(now, target)


def _run(self, *anims, rt=0.6):
    self.play(*anims, run_time=rt)
    self.t = getattr(self, "t", 0.0) + rt


def kaggle_card(y):
    c = box(3.8, 1.95, fill=CARD).move_to([0, y, 0])
    lab = serif("Kaggle competition", 36, INK_SOFT)
    l1 = serif("Post-train Gemma", 44)
    l2 = serif("→ developer agent", 44)
    g = VGroup(lab, l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
    fit(g, 3.45).move_to(c).align_to(c, LEFT).shift(RIGHT * 0.16)
    return VGroup(c, g)


# ── B02 — where I started (17.24 s) ──────────────────────────────────────────

class B02_Origin(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Where I started.")), rt=0.4)
        k = kaggle_card(1.65)
        self.at(2.4)
        self.run(FadeIn(k, shift=UP * 0.15), rt=0.7)

        head = serif("literature review", 40, INK_SOFT).move_to([0, 0.25, 0]).align_to([-1.9, 0, 0], LEFT)

        def card(name):
            c = box(3.8, 0.7)
            t = fit(serif(name, 44), 3.2).move_to(c).align_to(c, LEFT).shift(RIGHT * 0.35)
            b = bar(0.42).move_to(c.get_left() + RIGHT * 0.15)
            return VGroup(c, b, t)

        cards = VGroup(card("RLVR"), card("PostTrainBench"), card("HumanEval")).arrange(DOWN, buff=0.14)
        cards.next_to(head, DOWN, buff=0.22).set_x(0)

        self.at(10.4)  # "I was in the literature review"
        self.run(FadeIn(head), rt=0.5)
        self.at(11.8)  # "reinforcement learning with verifiable rewards"
        self.run(FadeIn(cards[0], shift=LEFT * 0.15), rt=0.5)
        self.at(15.2)  # "PostTrainBench"
        self.run(FadeIn(cards[1], shift=LEFT * 0.15), rt=0.4)
        self.at(16.2)  # "HumanEval"
        self.run(FadeIn(cards[2], shift=LEFT * 0.15), rt=0.4)
        self.at(17.24)


# ── B03 — reassigned (6.78 s) ────────────────────────────────────────────────

class B03_Reassigned(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("A new question.")), rt=0.3)
        k = kaggle_card(1.65)
        self.add(k)
        tag = VGroup(serif("scoped beyond", 38, INK_SOFT), serif("the fellowship", 38, INK_SOFT)
                     ).arrange(DOWN, aligned_edge=LEFT, buff=0.02).next_to(k, DOWN, buff=0.2).align_to([-1.8, 0, 0], LEFT)
        self.at(1.3)
        self.run(k.animate.set_opacity(0.35), FadeIn(tag), rt=0.6)

        new = box(3.8, 1.5, fill=CARD).move_to([0, -2.1, 0])
        t = serif("Agentic search", 54).move_to(new)
        fit(t, 3.5)
        u = Line(LEFT * 1.5, RIGHT * 1.5, color=SPARK, stroke_width=6).next_to(t, DOWN, buff=0.1)
        arrow = Arrow([0, -0.55, 0], [0, -1.3, 0], buff=0, color=INK, stroke_width=5)
        self.at(4.4)
        self.run(GrowArrow(arrow), FadeIn(new), FadeIn(t), rt=0.6)
        self.run(Create(u), rt=0.4)
        self.at(6.78)


# ── B04 — the new problem (17.51 s) ──────────────────────────────────────────

def doc_strip(h=2.5, w=1.2):
    pages = VGroup(*[box(w, h).shift(RIGHT * 0.06 * i + UP * 0.06 * i) for i in range(4, -1, -1)])
    rule = VGroup(*[Line(LEFT * (w / 2 - 0.18), RIGHT * (w / 2 - 0.18), color=INK_SOFT, stroke_width=2)
                    .set_opacity(0.35).move_to(pages[-1]).shift(UP * (h / 2 - 0.3 - 0.24 * i))
                    for i in range(int((h - 0.5) / 0.24))])
    return VGroup(pages, rule)


class B04_Problem(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Scattered answers.")), rt=0.4)

        doc = doc_strip().move_to([-1.15, 1.3, 0])
        lab = serif("2,000+ pages", 40).next_to(doc, DOWN, buff=0.15).align_to([-1.9, 0, 0], LEFT)
        self.at(0.6)
        self.run(FadeIn(doc), FadeIn(lab), rt=0.8)

        front = doc[0][-1]
        ys = [2.15, 1.3, 0.45]
        marks = VGroup(*[Rectangle(width=0.85, height=0.16).set_fill(SPARK, opacity=0.85).set_stroke(width=0)
                         .move_to([front.get_x(), y, 0]) for y in ys])
        circ = Circle(radius=0.38).set_stroke(INK, width=3).move_to([1.15, 1.6, 0])
        atext = VGroup(serif("one", 36), serif("answer", 36)).arrange(DOWN, buff=0.0).next_to(circ, DOWN, buff=0.1)
        links = VGroup(*[Line(m.get_right(), circ.get_left(), color=SPARK, stroke_width=3) for m in marks])
        self.at(5.6)
        self.run(FadeIn(marks, lag_ratio=0.3), rt=0.7)
        self.run(Create(links), FadeIn(circ), FadeIn(atext), rt=0.6)

        people = VGroup(serif("people:", 38, INK_SOFT), serif("slowly", 38)).arrange(RIGHT, buff=0.15)
        agents = VGroup(serif("agents:", 38, INK_SOFT), mono("grep(...)", 26)).arrange(RIGHT, buff=0.15)
        rows = VGroup(people, agents).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to([0, -1.25, 0]).align_to([-1.85, 0, 0], LEFT)
        self.at(7.6)
        self.run(FadeIn(people), rt=0.5)
        self.at(9.0)
        self.run(FadeIn(agents), rt=0.5)

        chips = VGroup(serif("insurance,", 38), serif("healthcare, more", 38)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.0).move_to([0, -2.55, 0]).align_to([-1.6, 0, 0], LEFT)
        cbar = bar(0.75).next_to(chips, LEFT, buff=0.15)
        self.at(13.6)
        self.run(FadeIn(cbar), FadeIn(chips, lag_ratio=0.3), rt=0.8)
        self.at(17.51)


# ── B05 — the setup (16.47 s) ────────────────────────────────────────────────

class B05_Setup(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The setup.")), rt=0.4)

        m = box(3.8, 1.65, fill=CARD).move_to([0, 1.85, 0])
        mt = VGroup(serif("model", 52), serif("Pi-style loop", 38, INK_SOFT), serif("(for testing)", 38, INK_SOFT)
                    ).arrange(DOWN, buff=0.0).move_to(m)
        r = box(3.8, 1.75, fill=CARD).move_to([0, -0.45, 0])
        rt_ = VGroup(mono("python_repl", 32), mono("grep()", 26, INK_SOFT), mono("read_lines()", 26, INK_SOFT),
                     mono("file_info()", 26, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.06).move_to(r)
        down = Arrow([-0.7, m.get_bottom()[1], 0], [-0.7, r.get_top()[1], 0], buff=0.05, color=INK, stroke_width=5)
        up = Arrow([0.7, r.get_top()[1], 0], [0.7, m.get_bottom()[1], 0], buff=0.05, color=SPARK, stroke_width=5)
        l1 = serif("↓ writes code", 38).move_to([0, -1.8, 0]).align_to([-1.85, 0, 0], LEFT)
        l2 = serif("↑ output ≤ 3,500 chars", 38)
        fit(l2, 3.7).next_to(l1, DOWN, buff=0.1).align_to(l1, LEFT)
        turns = VGroup(bar(0.45), serif("up to 12 turns", 40)).arrange(RIGHT, buff=0.18).next_to(l2, DOWN, buff=0.2).align_to(l1, LEFT)

        self.at(2.3)
        self.run(FadeIn(m), FadeIn(mt), rt=0.6)
        self.at(6.2)
        self.run(FadeIn(r), FadeIn(rt_), rt=0.6)
        self.at(9.6)
        self.run(GrowArrow(down), FadeIn(l1), rt=0.6)
        self.at(11.3)
        self.run(GrowArrow(up), FadeIn(l2), rt=0.6)
        self.at(13.8)
        self.run(FadeIn(turns), rt=0.5)
        self.at(16.47)


# ── B06 — the benchmark (19.16 s) ────────────────────────────────────────────

class B06_Benchmark(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The benchmark.")), rt=0.4)

        c = box(3.8, 1.7, fill=CARD).move_to([0, 1.85, 0])
        title = serif("BABILong", 64)
        venue = VGroup(serif("NeurIPS 2024 ·", 36, INK_SOFT), serif("Datasets & Benchmarks", 36, INK_SOFT)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
        g = VGroup(title, venue).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
        fit(g, 3.6).move_to(c).align_to(c, LEFT).shift(RIGHT * 0.18)

        def pt(a, b):
            t = VGroup(serif(a, 38), serif(b, 38)).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
            return VGroup(bar(0.7), t).arrange(RIGHT, buff=0.18)

        p1 = pt("facts hidden", "inside long books")
        p2 = pt("multi-hop: chain", "scattered facts")
        pts = VGroup(p1, p2).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to([0, 0.05, 0]).align_to([-1.85, 0, 0], LEFT)

        self.at(1.9)
        self.run(FadeIn(c), FadeIn(title), rt=0.6)
        self.at(4.2)
        self.run(FadeIn(venue), rt=0.5)
        self.at(6.0)
        self.run(FadeIn(p1), rt=0.5)
        self.at(10.6)
        self.run(FadeIn(p2), rt=0.5)

        m = box(3.8, 2.05).move_to([0, -2.15, 0])
        mh = serif("My first test", 40)
        rows = VGroup(*[mono(t, 26) for t in ("task: qa2", "128k tokens", "6,429 lines",
                                               "~275 pages")]).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
        mg = VGroup(mh, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(m).align_to(m, LEFT).shift(RIGHT * 0.2)
        self.at(13.0)
        self.run(FadeIn(m), FadeIn(mh), rt=0.5)
        self.run(FadeIn(rows, lag_ratio=0.35), rt=1.6)
        self.at(19.16)


# ── B07 — first test question (19.22 s) ──────────────────────────────────────

ROWS = ((3780, "took the football"), (5091, "dropped the football"),
        (5187, "grabbed the football"), (6021, "went to the kitchen"))


class B07_FirstTest(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("BABILong test question.")), rt=0.4)

        q = fit(serif("Where is the football?", 44), 3.75).move_to([0, 2.4, 0]).align_to([-1.85, 0, 0], LEFT)
        self.at(2.6)
        self.run(FadeIn(q), rt=0.6)

        who = serif("Daniel…", 38, INK_SOFT).move_to([0, 1.85, 0]).align_to([-1.85, 0, 0], LEFT)
        rows = VGroup()
        for n, text in ROWS:
            r = VGroup(mono(f"line {n:,}", 26, INK_SOFT), serif(text, 38)).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
            fit(r, 3.5)
            rows.add(VGroup(bar(0.55), r).arrange(RIGHT, buff=0.15))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.04).next_to(who, DOWN, buff=0.06).align_to(who, LEFT)

        self.at(5.2)
        self.run(FadeIn(who), rt=0.4)
        for i, t in enumerate((8.3, 9.4, 10.4, 11.6)):
            self.at(t)
            self.run(FadeIn(rows[i], shift=RIGHT * 0.1), rt=0.45)

        r1 = serif("agent: kitchen", 38)
        r2 = VGroup(serif("benchmark: kitchen", 38), tick()).arrange(RIGHT, buff=0.12)
        res = VGroup(r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
        fit(res, 3.7).next_to(rows, DOWN, buff=0.1).align_to(who, LEFT)
        self.at(13.9)
        self.run(FadeIn(r1), rt=0.4)
        self.run(FadeIn(r2), rt=0.4)

        tag = VGroup(bar(0.4), serif("very early work · 1 run", 36)).arrange(RIGHT, buff=0.15)
        fit(tag, 3.7).next_to(res, DOWN, buff=0.08).align_to(who, LEFT)
        self.at(16.9)
        self.run(FadeIn(tag), rt=0.5)
        self.at(19.22)


# ── B08 — what comes next (12.80 s) ─────────────────────────────────────────

class B08_Next(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        label = mono("Next", 26, INK_SOFT).move_to([-1.85, 3.1, 0], aligned_edge=UL)
        rule = Line([-1.85, 2.62, 0], [1.85, 2.62, 0], color=INK_SOFT, stroke_width=2)
        head = fit(serif("What comes next", 44), 3.7).next_to(rule, DOWN, buff=0.15).align_to(label, LEFT)

        texts = ("Connect Earendil's Pi agent", "Longer documents, more BABILong tasks",
                 "Stricter scoring", "Sandbox the code", "Fine-tune toward 2,000-page books")
        items = VGroup(*[wrap(t, 36, 3.45) for t in texts])
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.14).next_to(head, DOWN, buff=0.22).align_to([-1.5, 0, 0], LEFT)
        marks = VGroup(*[bar(0.36).move_to([-1.75, it.get_top()[1] - 0.22, 0]) for it in items])
        for it in items:
            it.set_opacity(0)

        self.run(FadeIn(label), Create(rule), FadeIn(head), rt=0.5)
        for i, t in enumerate((0.7, 4.0, 7.6, 9.4, 11.0)):
            self.at(t)
            self.run(items[i].animate.set_opacity(1), FadeIn(marks[i]), rt=0.45)
        self.at(12.80)


# ── B10 — @HumanitariansAI title outro (2.97 s) ─────────────────────────────

class B10_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        l1, l2 = serif("Search,", 80), serif("Don't Read", 80)
        dot = Dot(radius=0.06, color=SPARK)
        line2 = VGroup(l2, dot).arrange(RIGHT, buff=0.03, aligned_edge=DOWN)
        dot.shift(UP * 0.07)
        title = VGroup(l1, line2).arrange(DOWN, buff=0.18).move_to([0, 1.55, 0])
        fit(title, 3.8)
        rule = Line(LEFT * 1.7, RIGHT * 1.7, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.2)
        mark = wordmark(0.3).move_to([0, -1.55, 0])
        handle = serif("@HumanitariansAI", 42).next_to(mark, DOWN, buff=0.35)
        fit(handle, 3.6)
        self.run(Write(l1), Write(l2), FadeIn(dot), rt=0.8)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(2.97)
