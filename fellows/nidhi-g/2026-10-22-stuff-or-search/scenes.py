"""
Manim scenes for stuff-or-search (16:9). Body beats B02-B09 + @HumanitariansAI outro B11.

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


def cross(color=SPARK, s=0.3):
    return VGroup(Line([-s / 2, -s / 2, 0], [s / 2, s / 2, 0], color=color, stroke_width=8),
                  Line([-s / 2, s / 2, 0], [s / 2, -s / 2, 0], color=color, stroke_width=8))


def page_stack(h=4.2, w=3.0, n=5, rows=None):
    pages = VGroup(*[box(w, h).shift(RIGHT * 0.1 * i + UP * 0.1 * i) for i in range(n - 1, -1, -1)])
    front = pages[-1]
    k = rows or int((h - 0.6) / 0.3)
    lines = VGroup(*[Line(LEFT * (w / 2 - 0.3), RIGHT * (w / 2 - 0.3), color=INK_SOFT, stroke_width=3)
                     .set_opacity(0.35).move_to(front).shift(UP * (h / 2 - 0.4 - 0.3 * i)) for i in range(k)])
    return VGroup(pages, lines)


# ── B02 — NIAH, the easy case (10.79 s) ─────────────────────────────────────

class B02_Needle(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The classic test.")), rt=0.4)
        stack = page_stack().move_to([-3.6, -0.35, 0])
        self.at(0.9)
        self.run(FadeIn(stack), rt=0.6)

        title = VGroup(serif("Needle in a Haystack", 50), serif("(Kamradt, 2023)", 32, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        title.move_to([2.6, 1.7, 0])
        self.at(1.8)
        self.run(FadeIn(title), rt=0.5)

        needle = stack[1][7].copy().set_color(SPARK).set_opacity(1).set_stroke(width=8)
        step1 = VGroup(bar(0.45), serif("hide one sentence", 40)).arrange(RIGHT, buff=0.2)
        step2 = VGroup(bar(0.45), serif("ask the model to find it", 40)).arrange(RIGHT, buff=0.2)
        steps = VGroup(step1, step2).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(title, DOWN, buff=0.55).align_to(title, LEFT)
        self.at(3.2)
        self.run(Create(needle), FadeIn(step1), rt=0.6)
        self.at(5.8)
        self.run(FadeIn(step2), rt=0.5)
        found = VGroup(serif("found", 40), tick()).arrange(RIGHT, buff=0.15).next_to(stack, RIGHT, buff=0.3).set_y(needle.get_y())
        self.run(FadeIn(found), Indicate(needle, color=SPARK), rt=0.7)

        tag = VGroup(serif("one fact = the easy case", 44)).next_to(steps, DOWN, buff=0.6).align_to(title, LEFT)
        self.at(8.9)
        self.run(FadeIn(tag), rt=0.5)
        self.at(10.79)


# ── B03 — shortcut one: stuff it (10.28 s) ──────────────────────────────────

class B03_Stuff(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Shortcut one: stuff it.")), rt=0.4)
        stack = page_stack(h=3.4, w=2.4, n=4).move_to([-4.6, 0.5, 0])
        pbox = box(5.6, 3.4, fill=CARD).move_to([2.6, 0.5, 0])
        plab = mono("prompt", 30, INK_SOFT).next_to(pbox, UP, buff=0.12).align_to(pbox, LEFT)
        arrow = Arrow(stack.get_right(), pbox.get_left(), buff=0.25, color=INK, stroke_width=5)
        stack[1].set_opacity(0.7)
        self.at(0.9)
        self.run(FadeIn(stack), FadeIn(pbox), FadeIn(plab), rt=0.6)

        fill = VGroup(*[Line(LEFT * 2.5, RIGHT * 2.5, color=INK_SOFT, stroke_width=3).set_opacity(0.7)
                        .move_to(pbox).shift(UP * (1.45 - 0.2 * i)) for i in range(15)])
        rel = VGroup(*[fill[i].copy().set_color(SPARK).set_opacity(1).set_stroke(width=6) for i in (3, 9, 12)])
        self.run(GrowArrow(arrow), LaggedStart(*[Create(f) for f in fill], lag_ratio=0.05), rt=1.4)
        self.at(3.5)   # "The few lines that matter get buried"
        self.run(FadeIn(rel), rt=0.4)
        self.run(rel.animate.scale(0.25).set_opacity(1), rt=1.0)
        buried = serif("the lines that matter: buried", 36, INK_SOFT).next_to(pbox, DOWN, buff=0.2).align_to(pbox, LEFT)
        self.run(FadeIn(buried), rt=0.4)

        rows = VGroup()
        for q in ("question 1", "question 2", "question 3"):
            b = Rectangle(width=4.3, height=0.28).set_fill(SPARK, opacity=0.75).set_stroke(width=0)
            rows.add(VGroup(serif(q, 32, INK_SOFT), b).arrange(RIGHT, buff=0.3))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to([-2.4, -2.5, 0])
        lab = serif("every page, every time", 36).next_to(rows, RIGHT, buff=0.35)
        self.at(6.1)   # "every question pays again for every page"
        for r in rows:
            self.run(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), rt=0.45)
        self.at(8.6)   # "in cost and in time"
        self.run(FadeIn(lab), rt=0.5)
        self.at(10.28)


# ── B04 — accepted isn't used (12.16 s) ─────────────────────────────────────

class B04_Effective(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Accepted isn't used.")), rt=0.4)
        x0 = -2.2
        adv = Rectangle(width=8.2, height=0.42).set_fill(INK_SOFT, opacity=0.35).set_stroke(width=0)
        adv.move_to([x0 + 4.1, 1.75, 0])
        eff = Rectangle(width=5.0, height=0.42).set_fill(INK, opacity=0.9).set_stroke(width=0)
        eff.move_to([x0 + 2.5, 1.05, 0])
        la = serif("advertised context", 34, INK_SOFT).next_to(adv, LEFT, buff=0.25)
        le = serif("reliable context", 34).next_to(eff, LEFT, buff=0.25).align_to(la, RIGHT)
        src = serif("RULER (Hsieh et al., 2024): most models fall short of their claimed length", 28, INK_SOFT)
        fit(src, 11.5).move_to([0, 0.45, 0])
        self.at(2.6)   # "The RULER benchmark"
        self.run(FadeIn(la), GrowFromEdge(adv, LEFT), rt=0.6)
        self.at(4.0)   # "found most models fall short of their advertised length"
        self.run(FadeIn(le), GrowFromEdge(eff, LEFT), FadeIn(src), rt=0.8)

        ax = Line([-4.6, -2.45, 0], [4.6, -2.45, 0], color=INK_SOFT, stroke_width=3)
        curve = VMobject(color=INK, stroke_width=6).set_points_smoothly(
            [[-4.3, -0.5, 0], [-2.2, -1.6, 0], [0, -2.0, 0], [2.2, -1.6, 0], [4.3, -0.5, 0]])
        labs = VGroup(serif("start", 34).move_to([-4.3, -2.78, 0]), serif("middle", 34).move_to([0, -2.78, 0]),
                      serif("end", 34).move_to([3.6, -2.78, 0]))
        dot = Dot([0, -2.0, 0], radius=0.13, color=SPARK)
        ylab = serif("how well it's used", 30, INK_SOFT).move_to([-3.2, -0.15, 0])
        src2 = serif("Lost in the Middle (Liu et al.) · redrawn", 30, INK_SOFT).move_to([2.9, -0.15, 0])
        self.at(7.6)   # "models use the start and end of their input best"
        self.run(Create(ax), FadeIn(labs), FadeIn(ylab), Create(curve), FadeIn(src2), rt=1.2)
        self.at(10.3)  # "losing what's in the middle"
        mu = Line(LEFT * 0.5, RIGHT * 0.5, color=SPARK, stroke_width=6).next_to(labs[1], DOWN, buff=0.06)
        self.run(FadeIn(dot, scale=1.5), Create(mu), rt=0.5)
        self.at(12.16)


# ── B05 — distractors (4.89 s) ──────────────────────────────────────────────

class B05_Distractors(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Look-alikes.")), rt=0.3)
        q = VGroup(serif("question:", 34, INK_SOFT), serif("Where did Daniel go last?", 44)).arrange(RIGHT, buff=0.25)
        q.move_to([0, 1.9, 0])
        rows = VGroup(*[mono(t, 34) for t in ("Daniel went back to the garden.", "Daniel went to the kitchen.",
                                               "Mary went to the kitchen.", "Daniel journeyed to the bedroom.")])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to([-0.9, -0.55, 0])
        tickm = tick().next_to(rows[1], RIGHT, buff=0.3)
        right = serif("real answer", 34, INK_SOFT).next_to(tickm, RIGHT, buff=0.15)
        note = serif("illustration", 28, INK_SOFT).move_to([0, -2.85, 0])
        self.run(FadeIn(q), FadeIn(rows, lag_ratio=0.1), FadeIn(note), rt=0.8)
        self.run(FadeIn(right), FadeIn(tickm), rt=0.4)
        arr = Arrow([-5.9, 1.2, 0], rows[2].get_left() + LEFT * 0.12, buff=0.05, color=SPARK, stroke_width=6)
        self.at(2.6)   # "can pull the model toward the wrong answer"
        self.run(GrowArrow(arr), rt=0.7)
        self.at(4.89)


# ── B06 — shortcut two: RAG, chunking (11.95 s) ─────────────────────────────

class B06_RAG(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Shortcut two: retrieval (RAG).")), rt=0.4)
        doc = box(11.6, 0.8, fill=CARD).move_to([0, 1.8, 0])
        dl = serif("document", 34, INK_SOFT).move_to(doc)
        self.at(0.8)
        self.run(FadeIn(doc), FadeIn(dl), rt=0.5)

        chunks = VGroup(*[box(1.75, 0.8, fill=CARD) for _ in range(6)]).arrange(RIGHT, buff=0.22).move_to([0, 0.55, 0])
        nums = VGroup(*[serif(f"chunk {i + 1}", 28, INK_SOFT).move_to(c) for i, c in enumerate(chunks)])
        self.at(2.2)   # "Split the document into chunks"
        self.run(ReplacementTransform(doc.copy(), chunks), FadeOut(dl), doc.animate.set_opacity(0.25), FadeIn(nums), rt=0.9)

        self.at(4.5)   # "find the chunks most like your question"
        q = serif("your question", 34).move_to([-4.6, -0.75, 0])
        self.run(FadeIn(q), chunks[1].animate.set_stroke(INK, width=5), chunks[3].animate.set_stroke(INK, width=5), FadeIn(VGroup(*[Dot(chunks[i].get_top() + UP * 0.16, radius=0.08, color=SPARK) for i in (1, 3)])), rt=0.6)
        mdl = box(2.6, 0.9, fill=CARD).move_to([4.4, -0.75, 0])
        mt = serif("model", 36).move_to(mdl)
        a1 = Arrow(chunks[1].get_bottom(), mdl.get_left(), buff=0.12, color=INK, stroke_width=4)
        a2 = Arrow(chunks[3].get_bottom(), mdl.get_left(), buff=0.12, color=INK, stroke_width=4)
        self.at(7.0)   # "pass only those on"
        self.run(FadeIn(mdl), FadeIn(mt), GrowArrow(a1), GrowArrow(a2), rt=0.6)

        f1 = VGroup(bar(0.4), serif("Daniel took the football…", 34)).arrange(RIGHT, buff=0.15)
        f2 = VGroup(bar(0.4), serif("…Daniel went to the kitchen", 34)).arrange(RIGHT, buff=0.15)
        f1.move_to([-3.1, -2.3, 0]); f2.move_to([3.1, -2.3, 0])
        cut = DashedLine([0, -1.75, 0], [0, -2.85, 0], color=SPARK, stroke_width=5)
        cl = serif("chunk boundary", 28, INK_SOFT).next_to(cut, DOWN, buff=0.08)
        self.at(8.9)   # "chunking can split facts that belong together"
        self.run(FadeIn(f1), FadeIn(f2), rt=0.5)
        self.run(Create(cut), FadeIn(cl), rt=0.5)
        self.at(11.95)


# ── B07 — the second hop, and order (12.99 s) ───────────────────────────────

class B07_SecondHop(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The second hop.")), rt=0.4)
        q = VGroup(serif("question:", 34, INK_SOFT), serif("Where is the football?", 44)).arrange(RIGHT, buff=0.25)
        q.move_to([0, 2.15, 0]).align_to([-6.0, 0, 0], LEFT)
        self.run(FadeIn(q), rt=0.5)

        def row(text, w, y):
            t = mono(text, 30).move_to([0, y, 0]).align_to([-6.0, 0, 0], LEFT)
            b = Rectangle(width=w, height=0.32).set_fill(INK_SOFT, opacity=0.5).set_stroke(width=0)
            b.move_to([2.2 + w / 2, y, 0])
            return VGroup(t, b)

        hdr = serif("how much it looks like the question (illustration)", 28, INK_SOFT).move_to([0, 1.4, 0]).align_to([-6.0, 0, 0], LEFT)
        r1 = row("Daniel took the football there.", 3.6, 0.85)
        r2 = row("Daniel went to the kitchen.", 0.7, 0.2)
        self.at(2.1)   # "Retrieval finds Daniel taking it"
        self.run(FadeIn(hdr), FadeIn(r1[0]), GrowFromEdge(r1[1], LEFT), rt=0.7)
        self.run(r1[1].animate.set_fill(OK, opacity=0.8), rt=0.3)
        self.at(4.6)   # "the deciding fact, Daniel went to the kitchen"
        self.run(FadeIn(r2[0]), GrowFromEdge(r2[1], LEFT), rt=0.6)
        low = serif("ranks low", 34).next_to(r2[1], RIGHT, buff=0.25)
        self.at(8.3)   # "so it ranks low"
        self.run(FadeIn(low), r2[1].animate.set_fill(SPARK, opacity=0.9), rt=0.5)

        steps = ["took", "dropped", "grabbed", "went to the kitchen"]
        tl = VGroup(*[serif(s, 38) for s in steps]).arrange(RIGHT, buff=0.95).move_to([0, -1.7, 0])
        arrows = VGroup(*[Arrow(tl[i].get_right(), tl[i + 1].get_left(), buff=0.12, color=INK_SOFT, stroke_width=4)
                          for i in range(3)])
        self.at(9.7)   # "And order matters"
        self.run(FadeIn(tl, lag_ratio=0.2), FadeIn(arrows), rt=1.0)
        hl = Line(tl[3].get_left(), tl[3].get_right(), color=SPARK, stroke_width=6).next_to(tl[3], DOWN, buff=0.12)
        wins = serif("the latest fact wins", 40).move_to([0, -2.75, 0])
        self.at(11.4)  # "the latest fact wins"
        self.run(Create(hl), FadeIn(wins), rt=0.5)
        self.at(12.99)


# ── B08 — references inside documents (7.53 s) ──────────────────────────────

class B08_References(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("References inside documents.")), rt=0.4)
        pa = box(5.2, 3.6, fill=CARD).move_to([-3.2, -0.2, 0])
        pb = box(5.2, 3.6, fill=CARD).move_to([3.2, -0.2, 0])
        ta = VGroup(mono("page 12", 26, INK_SOFT), mono("Coverage applies", 30), mono("as defined in", 30),
                    mono("section 4.2.", 30)).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(pa).align_to(pa, LEFT).shift(RIGHT * 0.35)
        tb = VGroup(mono("page 87", 26, INK_SOFT), mono("4.2 Definitions", 30), mono("\"Coverage\" means…", 30)
                    ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(pb).align_to(pb, LEFT).shift(RIGHT * 0.35)
        note = serif("illustration", 28, INK_SOFT).move_to([0, -2.6, 0])
        self.at(0.5)
        self.run(FadeIn(pa), FadeIn(ta), FadeIn(pb), FadeIn(tb), FadeIn(note), rt=0.7)
        u = Line(ta[3].get_left(), ta[3].get_right(), color=SPARK, stroke_width=5).next_to(ta[3], DOWN, buff=0.06)
        self.at(2.9)   # "see section four point two"
        self.run(Create(u), rt=0.4)
        arc = CurvedArrow(ta[3].get_right() + RIGHT * 0.1, tb[1].get_left() + LEFT * 0.1, angle=-PI / 3, color=SPARK, stroke_width=6)
        lab = VGroup(serif("follow it", 36), tick()).arrange(RIGHT, buff=0.12).move_to([0, 2.05, 0])
        self.at(5.6)   # "need following, not matching"
        self.run(Create(arc), FadeIn(lab), rt=0.7)
        self.at(7.53)


# ── B09 — verdict (7.10 s) ──────────────────────────────────────────────────

class B09_Verdict(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        c = box(11.4, 5.9, fill=CARD).move_to([0, 0.2, 0])
        label = mono("Verdict", 26, INK_SOFT).move_to(c.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.4, aligned_edge=UL)
        rule = Line(c.get_left() + RIGHT * 0.3, c.get_right() + LEFT * 0.3, color=INK_SOFT, stroke_width=2)
        rule.next_to(label, DOWN, buff=0.15).set_x(0)
        cols = VGroup()
        for name in ("Stuffing", "Basic RAG"):
            h = serif(name, 52)
            r1 = VGroup(tick(), serif("finds pieces", 40)).arrange(RIGHT, buff=0.2)
            r2 = VGroup(cross(), serif("connects them", 40)).arrange(RIGHT, buff=0.2)
            cols.add(VGroup(h, r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.35))
        cols.arrange(RIGHT, buff=1.6).next_to(rule, DOWN, buff=0.45)
        foot = VGroup(bar(0.45), serif("Next: multi-hop search", 42)).arrange(RIGHT, buff=0.2).next_to(cols, DOWN, buff=0.55)
        self.run(FadeIn(c), FadeIn(label), Create(rule), FadeIn(cols[0][0]), FadeIn(cols[1][0]), rt=0.4)
        self.run(FadeIn(cols[0][1]), FadeIn(cols[1][1]), rt=0.4)
        self.at(1.9)   # "Neither connects them"
        self.run(FadeIn(cols[0][2]), FadeIn(cols[1][2]), rt=0.5)
        self.at(4.9)   # "multi-hop search, coming in the next video"
        self.run(FadeIn(foot), rt=0.5)
        self.at(7.10)


# ── B11 — @HumanitariansAI title outro (3.07 s) ─────────────────────────────

class B11_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        title = serif("Stuff It or Search It?", 100).move_to([0, 1.35, 0])
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.3)
        mark = wordmark(0.7).move_to([0, -1.55, 0])
        handle = serif("@HumanitariansAI", 56).next_to(mark, DOWN, buff=0.4)
        self.run(Write(title), rt=0.8)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(3.07)
