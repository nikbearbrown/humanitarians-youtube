"""
Manim scenes for search-dont-read (16:9). Body beats B02-B08 + @HumanitariansAI outro B10.

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

HERE = os.path.dirname(os.path.abspath(__file__))
_HOME = os.environ.get("ART_HOME") or os.path.join(HERE, "..", "..", "brutalist")

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
    c = np.array([-5.85, 2.95, 0])
    arms = VGroup(*[
        Line(c + 0.2 * np.array([np.cos(a), np.sin(a), 0]),
             c - 0.2 * np.array([np.cos(a), np.sin(a), 0]),
             color=SPARK, stroke_width=6)
        for a in (0, np.pi / 3, 2 * np.pi / 3)])
    label = serif(words, 44).next_to(arms, RIGHT, buff=0.3)
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
    bug = wordmark(0.22)
    bug.set_fill(INK, opacity=0.4)
    return bug.move_to(np.array([4.95, -3.2, 0]))


def tick(color=OK, s=0.32):
    return VMobject(stroke_color=color, stroke_width=8).set_points_as_corners(
        [[-0.5 * s, 0, 0], [-0.1 * s, -0.4 * s, 0], [0.6 * s, 0.45 * s, 0]])


def box(w, h, fill=PAGE):
    return RoundedRectangle(corner_radius=0.14, width=w, height=h).set_fill(
        fill, opacity=1).set_stroke(INK_SOFT, width=2)


def bar(h=0.5):
    return Line(UP * h / 2, DOWN * h / 2, color=SPARK, stroke_width=8)


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


def kaggle_card():
    c = box(5.6, 2.5, fill=CARD)
    lab = serif("Kaggle competition", 32, INK_SOFT)
    l1 = serif("Post-train Gemma", 48)
    l2 = serif("→ developer agent", 48)
    g = VGroup(lab, l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
    g.move_to(c).align_to(c, LEFT).shift(RIGHT * 0.35)
    return VGroup(c, g)


# ── B02 — where I started (17.24 s) ──────────────────────────────────────────

class B02_Origin(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Where I started.")), rt=0.4)
        k = kaggle_card().move_to([-3.2, 0.3, 0])
        self.at(2.4)   # "a Kaggle competition on post-training..."
        self.run(FadeIn(k, shift=UP * 0.2), rt=0.7)

        head = serif("literature review", 40, INK_SOFT).move_to([3.0, 2.15, 0])

        def card(name, kind):
            c = box(5.2, 1.0)
            t = serif(name, 46)
            t.move_to(c).align_to(c, LEFT).shift(RIGHT * 0.45)
            b = bar(0.55).move_to(c.get_left() + RIGHT * 0.2)
            return VGroup(c, b, t)

        cards = VGroup(card("RLVR", "method"), card("PostTrainBench", "benchmark"),
                       card("HumanEval", "benchmark")).arrange(DOWN, buff=0.25).move_to([3.0, 0.1, 0])
        rl = VGroup(serif("RLVR = reinforcement learning", 32, INK_SOFT), serif("with verifiable rewards", 32, INK_SOFT)
                    ).arrange(DOWN, aligned_edge=LEFT, buff=0.04).next_to(cards, DOWN, buff=0.3).align_to(cards, LEFT)

        self.at(10.4)  # "I was in the literature review"
        self.run(FadeIn(head), rt=0.5)
        self.at(11.8)  # "reinforcement learning with verifiable rewards"
        self.run(FadeIn(cards[0], shift=LEFT * 0.2), FadeIn(rl), rt=0.5)
        self.at(15.2)  # "PostTrainBench"
        self.run(FadeIn(cards[1], shift=LEFT * 0.2), rt=0.4)
        self.at(16.2)  # "HumanEval"
        self.run(FadeIn(cards[2], shift=LEFT * 0.2), rt=0.4)
        self.at(17.24)


# ── B03 — reassigned (6.78 s) ────────────────────────────────────────────────

class B03_Reassigned(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("A new question.")), rt=0.3)
        k = kaggle_card().move_to([-3.2, 0.3, 0])
        self.add(k)
        tag = serif("scoped beyond the fellowship", 36, INK_SOFT).next_to(k, DOWN, buff=0.35)
        self.at(1.3)   # "scoped beyond what the fellowship could take on"
        self.run(k.animate.set_opacity(0.35), FadeIn(tag), rt=0.6)

        new = box(5.0, 2.0, fill=CARD).move_to([3.5, 0.3, 0])
        t = serif("Agentic search", 60).move_to(new)
        u = Line(LEFT * 1.9, RIGHT * 1.9, color=SPARK, stroke_width=6).next_to(t, DOWN, buff=0.12)
        arrow = Arrow(k.get_right(), new.get_left(), buff=0.2, color=INK, stroke_width=5)
        self.at(4.4)   # "reassigned to a new research question"
        self.run(GrowArrow(arrow), FadeIn(new), FadeIn(t), rt=0.6)
        self.run(Create(u), rt=0.4)
        self.at(6.78)


# ── B04 — the new problem (17.51 s) ──────────────────────────────────────────

def doc_strip(h=4.5, w=1.7):
    pages = VGroup(*[box(w, h).shift(RIGHT * 0.09 * i + UP * 0.09 * i) for i in range(4, -1, -1)])
    rule = VGroup(*[Line(LEFT * (w / 2 - 0.25), RIGHT * (w / 2 - 0.25), color=INK_SOFT, stroke_width=2)
                    .set_opacity(0.35).move_to(pages[-1]).shift(UP * (h / 2 - 0.4 - 0.32 * i))
                    for i in range(int((h - 0.6) / 0.32))])
    return VGroup(pages, rule)


class B04_Problem(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Scattered answers.")), rt=0.4)

        doc = doc_strip().move_to([-4.7, -0.7, 0])
        lab = serif("2,000+ pages", 40).next_to(doc, UP, buff=0.2)
        self.at(0.6)   # "a text of two thousand pages or more"
        self.run(FadeIn(doc), FadeIn(lab), rt=0.8)

        front = doc[0][-1]
        ys = [1.1, -0.5, -2.1]
        marks = VGroup(*[Rectangle(width=1.2, height=0.2).set_fill(SPARK, opacity=0.85).set_stroke(width=0)
                         .move_to([front.get_x(), y - 0.35, 0]) for y in ys])
        ans = VGroup(Circle(radius=0.55).set_stroke(INK, width=3), serif("one answer", 34))
        ans[1].next_to(ans[0], DOWN, buff=0.12)
        ans.move_to([-1.3, -0.6, 0])
        links = VGroup(*[Line(m.get_right(), ans[0].get_left(), color=SPARK, stroke_width=3) for m in marks])
        self.at(5.6)   # "where the reasoning behind one answer is scattered across it"
        self.run(FadeIn(marks, lag_ratio=0.3), rt=0.7)
        self.run(Create(links), FadeIn(ans), rt=0.6)

        people = VGroup(serif("people:", 36, INK_SOFT), serif("page by page, slowly", 40)).arrange(RIGHT, buff=0.2)
        agents = VGroup(serif("agents:", 36, INK_SOFT), mono("grep(pattern)", 36)).arrange(RIGHT, buff=0.2)
        rows = VGroup(people, agents).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to([3.4, 0.9, 0])
        self.at(7.6)   # "People are bad at searching like that."
        self.run(FadeIn(people), rt=0.5)
        self.at(9.0)   # "Agents search by writing code"
        self.run(FadeIn(agents), rt=0.5)

        def chip(s):
            t = serif(s, 36)
            b = box(t.width + 0.5, t.height + 0.35)
            return VGroup(b, t.move_to(b))

        chips = VGroup(chip("insurance"), chip("healthcare"), chip("& more")).arrange(RIGHT, buff=0.25)
        fit(chips, 6.2).move_to([2.95, -1.3, 0])
        self.at(13.6)  # "insurance, healthcare and any field buried in documents"
        self.run(FadeIn(chips, lag_ratio=0.3), rt=1.0)
        self.at(17.51)


# ── B05 — the setup (16.47 s) ────────────────────────────────────────────────

class B05_Setup(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The setup.")), rt=0.4)

        m = box(4.0, 2.2, fill=CARD).move_to([-3.6, 0.45, 0])
        mt = VGroup(serif("model", 56), serif("Pi-style loop", 32, INK_SOFT), serif("(for testing)", 32, INK_SOFT)
                    ).arrange(DOWN, buff=0.06).move_to(m)
        r = box(4.6, 2.6, fill=CARD).move_to([3.4, 0.45, 0])
        rt_ = VGroup(mono("python_repl", 40), mono("grep()", 30, INK_SOFT), mono("read_lines()", 30, INK_SOFT),
                     mono("file_info()", 30, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(r)

        top = CurvedArrow(m.get_top() + RIGHT * 0.6, r.get_top() + LEFT * 0.6, angle=-PI / 4, color=INK, stroke_width=5)
        bot = CurvedArrow(r.get_bottom() + LEFT * 0.6, m.get_bottom() + RIGHT * 0.6, angle=-PI / 4, color=INK, stroke_width=5)
        tl = serif("writes code", 34).next_to(top, UP, buff=0.08)
        bl = serif("output, ≤ 3,500 chars", 34).next_to(bot, DOWN, buff=0.08)

        self.at(2.3)   # "A Pi-style agent loop, for testing"
        self.run(FadeIn(m), FadeIn(mt), rt=0.6)
        self.at(6.2)   # "a Python REPL with search helpers like grep and read lines"
        self.run(FadeIn(r), FadeIn(rt_), rt=0.6)
        self.at(9.6)   # "The model writes code"
        self.run(Create(top), FadeIn(tl), rt=0.6)
        self.at(11.3)  # "sees the output"
        self.run(Create(bot), FadeIn(bl), rt=0.6)

        dots = VGroup(*[Circle(radius=0.11).set_stroke(INK, width=2) for _ in range(12)]).arrange(RIGHT, buff=0.16)
        dl = serif("up to 12 turns", 36)
        turns = VGroup(dl, dots).arrange(RIGHT, buff=0.35).move_to([0, -2.75, 0])
        self.at(13.8)  # "for up to twelve turns"
        self.run(FadeIn(turns), rt=0.4)
        self.run(LaggedStart(*[d.animate.set_fill(SPARK, opacity=1) for d in dots], lag_ratio=0.15), rt=1.4)
        self.at(16.47)


# ── B06 — the benchmark (19.16 s) ────────────────────────────────────────────

class B06_Benchmark(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The benchmark.")), rt=0.4)

        c = box(6.6, 4.8, fill=CARD).move_to([-2.85, -0.15, 0])
        title = serif("BABILong", 72)
        venue = serif("NeurIPS 2024 · Datasets & Benchmarks", 32, INK_SOFT)
        p1 = VGroup(bar(0.45), serif("facts hidden inside long books", 38)).arrange(RIGHT, buff=0.2)
        p2 = VGroup(bar(0.45), serif("multi-hop: chain scattered facts", 38)).arrange(RIGHT, buff=0.2)
        g = VGroup(title, venue, p1, p2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        fit(g, 6.0).move_to(c).align_to(c, LEFT).shift(RIGHT * 0.35)

        self.at(1.9)   # "I used BABILong"
        self.run(FadeIn(c), FadeIn(title), rt=0.6)
        self.at(4.2)   # "published at NeurIPS twenty twenty-four"
        self.run(FadeIn(venue), rt=0.5)
        self.at(6.0)   # "It hides simple facts inside long books"
        self.run(FadeIn(p1), rt=0.5)
        self.at(10.6)  # "finding scattered facts and chaining them together"
        self.run(FadeIn(p2), rt=0.5)

        m = box(4.6, 4.8).move_to([3.95, -0.15, 0])
        mh = serif("My first test", 44)
        rows = VGroup(*[VGroup(mono(a, 32, INK_SOFT), mono(b, 32)).arrange(RIGHT, buff=0.3)
                        for a, b in (("task  ", "qa2"), ("length", "128k tokens"),
                                     ("lines ", "6,429"), ("pages ", "~275"))]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        mg = VGroup(mh, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        fit(mg, 4.1).move_to(m)
        self.at(13.0)  # "My first test"
        self.run(FadeIn(m), FadeIn(mh), rt=0.5)
        self.run(FadeIn(rows, lag_ratio=0.35), rt=1.6)
        self.at(19.16)


# ── B07 — first test question (19.22 s) ──────────────────────────────────────

LINES = ((3780, "Daniel took the football there."),
         (5091, "Daniel dropped the football."),
         (5187, "Daniel grabbed the football there."),
         (6021, "Daniel went to the kitchen."))
TOTAL_LINES = 6429


class B07_FirstTest(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("First test question.")), rt=0.4)

        q = VGroup(serif("BABILong test question:", 34, INK_SOFT), serif("Where is the football?", 52)
                   ).arrange(RIGHT, buff=0.3, aligned_edge=DOWN).move_to([0, 2.05, 0]).align_to([-6.0, 0, 0], LEFT)
        self.at(2.6)   # "I gave it one BABILong question: where is the football?"
        self.run(FadeIn(q), rt=0.6)

        top, bottom = 1.2, -1.6
        doc = Line([-5.55, top, 0], [-5.55, bottom, 0], color=INK_SOFT, stroke_width=8)
        dl = VGroup(mono("line 1", 22, INK_SOFT).next_to(doc, UP, buff=0.08),
                    mono("6,429", 22, INK_SOFT).next_to(doc, DOWN, buff=0.08))
        rows = VGroup()
        ticks = VGroup()
        links = VGroup()
        for i, (n, text) in enumerate(LINES):
            y = top - (top - bottom) * n / TOTAL_LINES
            tk = Line([-5.75, y, 0], [-5.35, y, 0], color=SPARK, stroke_width=8)
            row = VGroup(mono(str(n), 28, INK_SOFT), mono(text, 28)).arrange(RIGHT, buff=0.3)
            row.move_to([0, 0.95 - i * 0.78, 0]).align_to([-4.6, 0, 0], LEFT)
            ticks.add(tk)
            rows.add(row)
            links.add(Line(tk.get_right(), row.get_left() + LEFT * 0.1, color=SPARK, stroke_width=2).set_opacity(0.6))

        self.at(5.2)   # "The facts that answer it are scattered across the document."
        self.run(Create(doc), FadeIn(dl), rt=0.6)
        for i, t in enumerate((8.3, 9.4, 10.4, 11.6)):  # "taking... dropping... picking it up... walking to the kitchen"
            self.at(t)
            self.run(FadeIn(ticks[i]), Create(links[i]), FadeIn(rows[i], shift=RIGHT * 0.15), rt=0.5)

        res = VGroup(
            VGroup(serif("agent:", 36, INK_SOFT), serif("kitchen", 44)).arrange(RIGHT, buff=0.15, aligned_edge=DOWN),
            VGroup(serif("benchmark:", 36, INK_SOFT), serif("kitchen", 44), tick()).arrange(RIGHT, buff=0.15, aligned_edge=DOWN),
        ).arrange(RIGHT, buff=0.9).move_to([0, -2.3, 0]).align_to([-4.6, 0, 0], LEFT)
        self.at(13.9)  # "Its answer, kitchen, matched the benchmark."
        self.run(FadeIn(res[0]), rt=0.4)
        self.run(FadeIn(res[1]), rt=0.4)

        tag = VGroup(bar(0.45), serif("very early work · 1 question · 1 run", 36)).arrange(RIGHT, buff=0.2)
        fit(tag, 8.6).move_to([0, -3.0, 0]).align_to([-4.6, 0, 0], LEFT)
        self.at(16.9)  # "One question, one run: very early work."
        self.run(FadeIn(tag), rt=0.5)
        self.at(19.22)


# ── B08 — what comes next (12.80 s) — verdict/artifact page ─────────────────

class B08_Next(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        c = box(10.6, 5.9, fill=CARD).move_to([0, 0.2, 0])
        label = mono("Next", 26, INK_SOFT).move_to(c.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.4, aligned_edge=UL)
        rule = Line(c.get_left() + RIGHT * 0.3, c.get_right() + LEFT * 0.3, color=INK_SOFT, stroke_width=2)
        rule.next_to(label, DOWN, buff=0.15).set_x(0)
        head = serif("What comes next", 54).next_to(rule, DOWN, buff=0.3).align_to(label, LEFT)

        texts = ("Connect Earendil's Pi agent", "Longer documents, more BABILong tasks",
                 "Stricter scoring", "Sandbox the code", "Fine-tune toward 2,000-page books")
        items = VGroup(*[VGroup(serif(f"{i + 1}.", 40), serif(t, 40)).arrange(RIGHT, buff=0.25)
                         for i, t in enumerate(texts)]).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        items.next_to(head, DOWN, buff=0.35).align_to(head, LEFT).shift(RIGHT * 0.3)
        marks = VGroup(*[bar(0.4).next_to(it, LEFT, buff=0.15) for it in items])
        for it in items:
            it.set_opacity(0)

        self.run(FadeIn(c), FadeIn(label), Create(rule), FadeIn(head), rt=0.5)
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
        title = serif("Search, Don't Read", 104)
        dot = Dot(radius=0.11, color=SPARK)
        grp = VGroup(title, dot).arrange(RIGHT, buff=0.06, aligned_edge=DOWN).move_to([0, 1.35, 0])
        dot.shift(UP * 0.12)
        rule = Line(LEFT * 5.2, RIGHT * 5.2, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.3)
        mark = wordmark(0.7).move_to([0, -1.55, 0])
        handle = serif("@HumanitariansAI", 56).next_to(mark, DOWN, buff=0.4)
        self.run(Write(title), FadeIn(dot), rt=0.8)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(2.97)
