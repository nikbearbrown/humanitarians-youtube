"""
Manim scenes for stuff-or-search/vertical: NATIVE 9:16 (frame 4.5 x 8 units).
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


def cross(color=SPARK, s=0.24):
    return VGroup(Line([-s / 2, -s / 2, 0], [s / 2, s / 2, 0], color=color, stroke_width=7),
                  Line([-s / 2, s / 2, 0], [s / 2, -s / 2, 0], color=color, stroke_width=7))


def page_stack(h=2.6, w=2.0, n=4):
    pages = VGroup(*[box(w, h).shift(RIGHT * 0.07 * i + UP * 0.07 * i) for i in range(n - 1, -1, -1)])
    front = pages[-1]
    k = int((h - 0.4) / 0.2)
    lines = VGroup(*[Line(LEFT * (w / 2 - 0.2), RIGHT * (w / 2 - 0.2), color=INK_SOFT, stroke_width=2)
                     .set_opacity(0.35).move_to(front).shift(UP * (h / 2 - 0.28 - 0.2 * i)) for i in range(k)])
    return VGroup(pages, lines)


L = -1.85   # left text edge


# ── B02 — NIAH (10.79 s) ────────────────────────────────────────────────────

class B02_Needle(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The classic test.")), rt=0.4)
        stack = page_stack(w=1.8).move_to([-0.95, 1.35, 0])
        self.at(0.9)
        self.run(FadeIn(stack), rt=0.6)
        title = VGroup(serif("Needle in", 46), serif("a Haystack", 46), serif("(Kamradt, 2023)", 36, INK_SOFT)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.0).move_to([0, -0.75, 0]).align_to([L, 0, 0], LEFT)
        self.at(1.8)
        self.run(FadeIn(title), rt=0.5)
        needle = stack[1][5].copy().set_color(SPARK).set_opacity(1).set_stroke(width=7)
        self.at(3.2)
        self.run(Create(needle), rt=0.5)
        found = VGroup(serif("found", 36), tick()).arrange(RIGHT, buff=0.1).next_to(stack, RIGHT, buff=0.12).set_y(needle.get_y())
        self.at(5.8)
        self.run(FadeIn(found), Indicate(needle, color=SPARK), rt=0.7)
        tag = VGroup(bar(0.8), VGroup(serif("one fact =", 40), serif("the easy case", 40)).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
                     ).arrange(RIGHT, buff=0.18).next_to(title, DOWN, buff=0.35).align_to([L, 0, 0], LEFT)
        self.at(8.9)
        self.run(FadeIn(tag), rt=0.5)
        self.at(10.79)


# ── B03 — stuff it (10.28 s) ────────────────────────────────────────────────

class B03_Stuff(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Shortcut one: stuff it.")), rt=0.4)
        stack = page_stack(h=1.25, w=1.3, n=4).move_to([-1.15, 1.95, 0])
        pbox = box(3.8, 1.4, fill=CARD).move_to([0, 0.45, 0])
        plab = mono("prompt", 26, INK_SOFT).next_to(stack, RIGHT, buff=0.4).set_y(1.95)
        arrow = Arrow([0.3, 1.6, 0], [0.3, 1.18, 0], buff=0, color=INK, stroke_width=5)
        stack[1].set_opacity(0.7)
        self.at(0.9)
        self.run(FadeIn(stack), FadeIn(pbox), FadeIn(plab), rt=0.6)
        fill = VGroup(*[Line(LEFT * 1.65, RIGHT * 1.65, color=INK_SOFT, stroke_width=2).set_opacity(0.7)
                        .move_to(pbox).shift(UP * (0.5 - 0.11 * i)) for i in range(10)])
        rel = VGroup(*[fill[i].copy().set_color(SPARK).set_opacity(1).set_stroke(width=5) for i in (2, 6, 8)])
        self.run(GrowArrow(arrow), LaggedStart(*[Create(f) for f in fill], lag_ratio=0.05), rt=1.4)
        self.at(3.5)
        self.run(FadeIn(rel), rt=0.4)
        self.run(rel.animate.scale(0.25).set_opacity(1), rt=1.0)
        buried = wrap("what matters: buried", 38, 3.6, INK_SOFT).next_to(pbox, DOWN, buff=0.12).align_to([L, 0, 0], LEFT)
        self.run(FadeIn(buried), rt=0.4)
        rows = VGroup()
        for q in ("Q1", "Q2", "Q3"):
            b = Rectangle(width=2.9, height=0.22).set_fill(SPARK, opacity=0.75).set_stroke(width=0)
            rows.add(VGroup(mono(q, 26, INK_SOFT), b).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(buried, DOWN, buff=0.15).align_to([L, 0, 0], LEFT)
        lab = wrap("every page, every time", 38, 3.6).next_to(rows, DOWN, buff=0.08).align_to([L, 0, 0], LEFT)
        self.at(6.1)
        for r in rows:
            self.run(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), rt=0.45)
        self.at(8.6)
        self.run(FadeIn(lab), rt=0.5)
        self.at(10.28)


# ── B04 — accepted isn't used (12.16 s) ─────────────────────────────────────

class B04_Effective(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Accepted isn't used.")), rt=0.4)
        la = serif("advertised context", 38, INK_SOFT).move_to([0, 2.5, 0]).align_to([L, 0, 0], LEFT)
        adv = Rectangle(width=3.7, height=0.3).set_fill(INK_SOFT, opacity=0.35).set_stroke(width=0)
        adv.next_to(la, DOWN, buff=0.08).align_to([L, 0, 0], LEFT)
        le = serif("reliable context", 38).next_to(adv, DOWN, buff=0.15).align_to([L, 0, 0], LEFT)
        eff = Rectangle(width=2.2, height=0.3).set_fill(INK, opacity=0.9).set_stroke(width=0)
        eff.next_to(le, DOWN, buff=0.08).align_to([L, 0, 0], LEFT)
        src = VGroup(serif("RULER", 36, INK_SOFT), serif("(Hsieh et al., 2024)", 36, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.0).next_to(eff, DOWN, buff=0.12).align_to([L, 0, 0], LEFT)
        self.at(2.6)
        self.run(FadeIn(la), GrowFromEdge(adv, LEFT), rt=0.6)
        self.at(4.0)
        self.run(FadeIn(le), GrowFromEdge(eff, LEFT), FadeIn(src), rt=0.8)

        src2 = VGroup(serif("Lost in the Middle", 36, INK_SOFT), serif("(Liu et al.), redrawn", 36, INK_SOFT)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.0).next_to(src, DOWN, buff=0.22).align_to([L, 0, 0], LEFT)
        ax = Line([-1.8, -2.6, 0], [1.8, -2.6, 0], color=INK_SOFT, stroke_width=3)
        curve = VMobject(color=INK, stroke_width=6).set_points_smoothly(
            [[-1.7, -1.3, 0], [-0.9, -2.05, 0], [0, -2.35, 0], [0.9, -2.05, 0], [1.7, -1.3, 0]])
        labs = VGroup(serif("start", 36).move_to([-1.45, -2.92, 0]), serif("middle", 36).move_to([0, -2.92, 0]),
                      serif("end", 36).move_to([1.5, -2.92, 0]))
        dot = Dot([0, -2.35, 0], radius=0.09, color=SPARK)
        self.at(7.6)
        self.run(FadeIn(src2), Create(ax), FadeIn(labs), Create(curve), rt=1.2)
        self.at(10.3)
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
        q = wrap("Where did Daniel go last?", 42, 3.6)
        q.shift(DOWN * 0.15)
        q.move_to([0, 2.15, 0]).align_to([L, 0, 0], LEFT)
        sents = ("Daniel went back to the garden.", "Daniel went to the kitchen.", "Mary went to the kitchen.",
                 "Daniel journeyed to the bedroom.")
        rows = VGroup(*[wrap(t, 36, 3.25) for t in sents]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        rows.next_to(q, DOWN, buff=0.3).align_to([-1.45, 0, 0], LEFT)
        tickm = tick().next_to(rows[1][-1], RIGHT, buff=0.12)
        note = serif("illustration", 36, INK_SOFT).next_to(rows, DOWN, buff=0.2).align_to([L, 0, 0], LEFT)
        self.run(FadeIn(q), FadeIn(rows, lag_ratio=0.1), FadeIn(note), rt=0.8)
        self.run(FadeIn(tickm), rt=0.3)
        ry = float(rows[2].get_center()[1])
        arr = Arrow([-1.95, ry + 0.45, 0], [-1.55, ry, 0], buff=0, color=SPARK, stroke_width=6,
                    max_tip_length_to_length_ratio=0.5)
        self.at(2.6)
        self.run(GrowArrow(arr), rt=0.7)
        self.at(4.89)


# ── B06 — RAG, chunking (11.95 s) ───────────────────────────────────────────

class B06_RAG(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Shortcut two: RAG.")), rt=0.4)
        doc = box(3.8, 0.55, fill=CARD).move_to([0, 2.45, 0])
        dl = serif("document", 36, INK_SOFT).move_to(doc)
        self.at(0.8)
        self.run(FadeIn(doc), FadeIn(dl), rt=0.5)
        chunks = VGroup(*[box(1.8, 0.5, fill=CARD) for _ in range(6)]).arrange_in_grid(rows=3, cols=2, buff=(0.2, 0.12))
        chunks.move_to([0, 1.1, 0])
        nums = VGroup(*[mono(f"chunk {i + 1}", 26, INK_SOFT).move_to(c) for i, c in enumerate(chunks)])
        self.at(2.2)
        self.run(ReplacementTransform(doc.copy(), chunks), FadeOut(dl), doc.animate.set_opacity(0.25), FadeIn(nums), rt=0.9)
        q = serif("your question", 38).move_to([0, -0.3, 0]).align_to([L, 0, 0], LEFT)
        self.at(4.5)
        self.run(FadeIn(q), chunks[3].animate.set_stroke(INK, width=5), chunks[5].animate.set_stroke(INK, width=5), FadeIn(VGroup(*[Dot(chunks[i].get_right() + RIGHT * 0.0 + LEFT * 0.12 + UP * 0.12, radius=0.06, color=SPARK) for i in (3, 5)])), rt=0.6)
        mdl = box(1.5, 0.55, fill=CARD).move_to([1.15, -1.0, 0])
        mt = serif("model", 36).move_to(mdl)
        a = Arrow(chunks[5].get_bottom(), mdl.get_top(), buff=0.08, color=INK, stroke_width=4)
        self.at(7.0)
        self.run(FadeIn(mdl), FadeIn(mt), GrowArrow(a), rt=0.6)
        f1 = VGroup(bar(0.4), serif("took the football", 38)).arrange(RIGHT, buff=0.12).move_to([0, -1.75, 0]).align_to([L, 0, 0], LEFT)
        cl = mono("chunk boundary", 26, INK_SOFT).move_to([0, -2.2, 0]).align_to([L, 0, 0], LEFT)
        cut = DashedLine([float(cl.get_right()[0]) + 0.12, -2.2, 0], [1.9, -2.2, 0], color=SPARK, stroke_width=5)
        f2 = VGroup(bar(0.75), wrap("went to the kitchen", 38, 3.2)).arrange(RIGHT, buff=0.12).move_to([0, -2.85, 0]).align_to([L, 0, 0], LEFT)
        self.at(8.9)
        self.run(FadeIn(f1), FadeIn(f2), rt=0.5)
        self.run(FadeIn(cl), Create(cut), rt=0.5)
        self.at(11.95)


# ── B07 — second hop, order (12.99 s) ───────────────────────────────────────

class B07_SecondHop(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The second hop.")), rt=0.4)
        q = fit(serif("Where is the football?", 42), 3.75).move_to([0, 2.45, 0]).align_to([L, 0, 0], LEFT)
        self.run(FadeIn(q), rt=0.5)
        hdr = wrap("match to the question (illustration)", 36, 3.6, INK_SOFT).next_to(q, DOWN, buff=0.12).align_to([L, 0, 0], LEFT)
        t1 = serif("took the football", 38).next_to(hdr, DOWN, buff=0.18).align_to([L, 0, 0], LEFT)
        b1 = Rectangle(width=3.3, height=0.22).set_fill(INK_SOFT, opacity=0.5).set_stroke(width=0).next_to(t1, DOWN, buff=0.06).align_to([L, 0, 0], LEFT)
        t2 = serif("went to the kitchen", 38).next_to(b1, DOWN, buff=0.15).align_to([L, 0, 0], LEFT)
        b2 = Rectangle(width=0.6, height=0.22).set_fill(INK_SOFT, opacity=0.5).set_stroke(width=0).next_to(t2, DOWN, buff=0.06).align_to([L, 0, 0], LEFT)
        self.at(2.1)
        self.run(FadeIn(hdr), FadeIn(t1), GrowFromEdge(b1, LEFT), rt=0.7)
        self.run(b1.animate.set_fill(OK, opacity=0.8), rt=0.3)
        self.at(4.6)
        self.run(FadeIn(t2), GrowFromEdge(b2, LEFT), rt=0.6)
        low = serif("ranks low", 36).next_to(b2, RIGHT, buff=0.2)
        self.at(8.3)
        self.run(FadeIn(low), b2.animate.set_fill(SPARK, opacity=0.9), rt=0.5)
        tl = VGroup(serif("took → dropped", 38), serif("→ grabbed", 38), serif("→ kitchen", 38)).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
        tl.next_to(b2, DOWN, buff=0.3).align_to([L, 0, 0], LEFT)
        self.at(9.7)
        self.run(FadeIn(tl, lag_ratio=0.3), rt=1.0)
        last = tl[2]
        hl = Line(LEFT * 0.65, RIGHT * 0.65, color=SPARK, stroke_width=6).move_to([float(last.get_right()[0]) - 0.65, float(last.get_bottom()[1]) - 0.06, 0])
        wins = wrap("the latest fact wins", 40, 3.6).next_to(tl, DOWN, buff=0.15).align_to([L, 0, 0], LEFT)
        self.at(11.4)
        self.run(Create(hl), FadeIn(wins), rt=0.5)
        self.at(12.99)


# ── B08 — references (7.53 s) ───────────────────────────────────────────────

class B08_References(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("References.")), rt=0.4)
        pa = box(3.8, 2.0, fill=CARD).move_to([0, 1.45, 0])
        ta = VGroup(mono("page 12 (example)", 26, INK_SOFT), mono("Coverage applies", 26), mono("as defined in", 26),
                    mono("section 4.2.", 26)).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(pa).align_to(pa, LEFT).shift(RIGHT * 0.2)
        pb = box(3.8, 1.5, fill=CARD).move_to([0, -1.25, 0])
        tb = VGroup(mono("page 87", 26, INK_SOFT), mono("4.2 Definitions", 26), mono("Coverage means…", 26)
                    ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(pb).align_to(pb, LEFT).shift(RIGHT * 0.2)
        self.at(0.5)
        self.run(FadeIn(pa), FadeIn(ta), FadeIn(pb), FadeIn(tb), rt=0.7)
        u = Line(ta[3].get_left(), ta[3].get_right(), color=SPARK, stroke_width=5).next_to(ta[3], DOWN, buff=0.05)
        self.at(2.9)
        self.run(Create(u), rt=0.4)
        arr = Arrow([1.3, pa.get_bottom()[1] + 0.05, 0], [1.3, pb.get_top()[1] - 0.05, 0], buff=0, color=SPARK, stroke_width=6)
        lab = VGroup(serif("follow it", 40), tick()).arrange(RIGHT, buff=0.12).move_to([0, -2.6, 0]).align_to([L, 0, 0], LEFT)
        self.at(5.6)
        self.run(GrowArrow(arr), FadeIn(lab), rt=0.7)
        self.at(7.53)


# ── B09 — verdict (7.10 s) ──────────────────────────────────────────────────

class B09_Verdict(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        label = mono("Verdict", 26, INK_SOFT).move_to([L, 3.1, 0], aligned_edge=UL)
        rule = Line([L, 2.62, 0], [1.85, 2.62, 0], color=INK_SOFT, stroke_width=2)
        secs = VGroup()
        for name in ("Stuffing", "Basic RAG"):
            h = serif(name, 48)
            r1 = VGroup(tick(), serif("finds pieces", 40)).arrange(RIGHT, buff=0.18)
            r2 = VGroup(cross(), serif("connects them", 40)).arrange(RIGHT, buff=0.18)
            secs.add(VGroup(h, r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.12))
        secs.arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(rule, DOWN, buff=0.3).align_to([L, 0, 0], LEFT)
        foot = VGroup(bar(0.8), VGroup(serif("Next: multi-hop", 40), serif("search", 40)).arrange(DOWN, aligned_edge=LEFT, buff=0.0)
                      ).arrange(RIGHT, buff=0.18).next_to(secs, DOWN, buff=0.45).align_to([L, 0, 0], LEFT)
        self.run(FadeIn(label), Create(rule), FadeIn(secs[0][0]), FadeIn(secs[1][0]), rt=0.4)
        self.run(FadeIn(secs[0][1]), FadeIn(secs[1][1]), rt=0.4)
        self.at(1.9)
        self.run(FadeIn(secs[0][2]), FadeIn(secs[1][2]), rt=0.5)
        self.at(4.9)
        self.run(FadeIn(foot), rt=0.5)
        self.at(7.10)


# ── B11 — outro (3.07 s) ────────────────────────────────────────────────────

class B11_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        title = VGroup(serif("Stuff It or", 80), serif("Search It?", 80)).arrange(DOWN, buff=0.18).move_to([0, 1.55, 0])
        fit(title, 3.8)
        rule = Line(LEFT * 1.7, RIGHT * 1.7, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.2)
        mark = wordmark(0.3).move_to([0, -1.55, 0])
        handle = serif("@HumanitariansAI", 42).next_to(mark, DOWN, buff=0.35)
        fit(handle, 3.6)
        self.run(Write(title), rt=0.8)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(3.07)
