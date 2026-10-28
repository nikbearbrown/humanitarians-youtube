"""
Manim scenes for multi-hop-search (16:9). Body beats B02-B09 + @HumanitariansAI outro B11.

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


def chipbox(t, size=36, mono_=False, fill=PAGE):
    tx = mono(t, size) if mono_ else serif(t, size)
    b = box(tx.width + 0.5, tx.height + 0.4, fill=fill)
    return VGroup(b, tx.move_to(b))


def arr(a, b, color=INK):
    return Arrow(a, b, buff=0.12, color=color, stroke_width=5, max_tip_length_to_length_ratio=0.25)


# ── B02 — iterative retrieval (11.67 s) ─────────────────────────────────────

class B02_Iterative(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Retrieve, read, retrieve again.")), rt=0.4)
        s1 = chipbox('search: "football"', 32, True, CARD).move_to([-3.8, 1.6, 0])
        r1 = serif("Daniel took it", 44).move_to([1.9, 1.6, 0])
        a1 = arr([-1.5, 1.6, 0], [0.2, 1.6, 0])
        s2 = chipbox('search: "Daniel"', 32, True, CARD).move_to([-4.0, 0.15, 0])
        steps = VGroup(serif("dropped it", 42).move_to([0.1, 0.15, 0]), serif("grabbed it", 42).move_to([3.6, 0.15, 0]),
                       serif("went to the kitchen", 42).move_to([1.7, -1.25, 0]))
        a2 = arr([-1.9, 0.15, 0], [-1.0, 0.15, 0])
        a3 = arr([1.2, 0.15, 0], [2.5, 0.15, 0])
        a4 = arr([3.6, -0.25, 0], [2.9, -0.85, 0])
        link = arr([0.6, 1.2, 0], [-3.0, 0.6, 0], INK_SOFT)
        u = Line(LEFT * 2.0, RIGHT * 2.0, color=SPARK, stroke_width=6).move_to([1.7, -1.75, 0])
        cap = serif("each finding shapes the next search", 40).move_to([0, -2.6, 0]).align_to([-6.0, 0, 0], LEFT)

        self.run(FadeIn(s1), rt=0.5)
        self.at(2.9)   # "Daniel took it"
        self.run(GrowArrow(a1), FadeIn(r1), rt=0.5)
        self.at(3.9)   # "Now search Daniel"
        self.run(GrowArrow(link), FadeIn(s2), rt=0.5)
        self.at(5.0)
        self.run(GrowArrow(a2), FadeIn(steps[0]), rt=0.4)
        self.at(5.7)
        self.run(GrowArrow(a3), FadeIn(steps[1]), rt=0.4)
        self.at(6.4)
        self.run(GrowArrow(a4), FadeIn(steps[2]), rt=0.4)
        self.at(7.9)   # "Each finding shapes the next search"
        self.run(FadeIn(cap), rt=0.5)
        self.at(10.4)  # "the latest fact wins"
        self.run(Create(u), rt=0.4)
        self.at(11.67)


# ── B03 — Self-Ask (9.83 s) ─────────────────────────────────────────────────

class B03_SelfAsk(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Break it into steps.")), rt=0.4)
        q = chipbox("Where is the football?", 46, fill=CARD).move_to([0, 1.75, 0])
        q1 = chipbox("Who had the football?", 40).move_to([-3.2, 0.05, 0])
        q2 = chipbox("Where did they go last?", 40).move_to([3.2, 0.05, 0])
        a1 = arr(q.get_bottom() + LEFT * 1.0, q1.get_top())
        a2 = arr(q.get_bottom() + RIGHT * 1.0, q2.get_top())
        s1 = chipbox("search", 32, True).next_to(q1, DOWN, buff=0.7)
        s2 = chipbox("search", 32, True).next_to(q2, DOWN, buff=0.7)
        b1 = arr(q1.get_bottom(), s1.get_top())
        b2 = arr(q2.get_bottom(), s2.get_top())
        lab = serif("Self-Ask (Press et al.): the model asks and answers its own follow-ups", 34, INK_SOFT)
        fit(lab, 11.6).move_to([0, -2.75, 0])
        self.run(FadeIn(q), rt=0.5)
        self.at(1.6)   # "breaks the question into smaller ones"
        self.run(GrowArrow(a1), GrowArrow(a2), FadeIn(q1), FadeIn(q2), rt=0.7)
        self.at(3.1)   # "Self-Ask ..."
        self.run(FadeIn(lab), rt=0.5)
        self.at(8.6)   # "can each go to a search engine"
        self.run(GrowArrow(b1), GrowArrow(b2), FadeIn(s1), FadeIn(s2), rt=0.6)
        self.at(9.83)


# ── B04 — IRCoT (14.61 s) ───────────────────────────────────────────────────

class B04_IRCoT(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Reason, then search.")), rt=0.4)
        t = serif("IRCoT", 72).move_to([0, 1.95, 0]).align_to([-6.0, 0, 0], LEFT)
        full = VGroup(serif("Interleaving Retrieval", 40), serif("with Chain-of-Thought", 40)).arrange(DOWN, aligned_edge=LEFT, buff=0.02)
        full.next_to(t, RIGHT, buff=0.6)
        src = serif("Trivedi et al., ACL 2023", 32, INK_SOFT).next_to(full, DOWN, buff=0.12).align_to(full, LEFT)
        self.at(0.8)
        self.run(FadeIn(t), rt=0.5)
        self.at(1.6)
        self.run(FadeIn(full), FadeIn(src), rt=0.6)

        names = ("reason", "search", "reason", "search")
        boxes = VGroup(*[chipbox(n, 40, fill=(CARD if n == "reason" else PAGE)) for n in names]).arrange(RIGHT, buff=0.9)
        boxes.move_to([0, -0.1, 0])
        arrows = VGroup(*[arr(boxes[i].get_right(), boxes[i + 1].get_left()) for i in range(3)])
        self.at(6.2)   # "one reasoning step"
        self.run(FadeIn(boxes[0]), rt=0.4)
        self.at(7.4)   # "then a new search guided by it"
        self.run(GrowArrow(arrows[0]), FadeIn(boxes[1]), rt=0.4)
        self.run(GrowArrow(arrows[1]), FadeIn(boxes[2]), rt=0.4)
        self.run(GrowArrow(arrows[2]), FadeIn(boxes[3]), rt=0.4)
        note = VGroup(bar(0.45), serif("authors report better retrieval and answers", 40)).arrange(RIGHT, buff=0.2)
        sub = serif("on multi-hop benchmarks (HotpotQA, MuSiQue and more)", 32, INK_SOFT)
        g = VGroup(note, sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to([0, -2.2, 0]).align_to([-6.0, 0, 0], LEFT)
        self.at(10.4)  # "Its authors report..."
        self.run(FadeIn(g), rt=0.6)
        self.at(14.61)


# ── B05 — GraphRAG (10.28 s) ────────────────────────────────────────────────

class B05_Graph(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Link facts by what they mention.")), rt=0.4)
        contents = (("Daniel", "football"), ("football",), ("Daniel", "kitchen"))
        chunks = VGroup()
        ents = []
        for i, names in enumerate(contents):
            c = box(3.4, 1.9, fill=CARD)
            lab = mono(f"chunk {i + 1}", 26, INK_SOFT).move_to(c.get_top() + DOWN * 0.3)
            e = VGroup(*[serif(n, 40) for n in names]).arrange(DOWN, buff=0.12).next_to(lab, DOWN, buff=0.15)
            chunks.add(VGroup(c, lab, e))
            ents.append(e)
        chunks.arrange(RIGHT, buff=0.7).move_to([0, 1.0, 0])
        self.at(0.6)
        self.run(FadeIn(chunks[0][0]), FadeIn(chunks[1][0]), FadeIn(chunks[2][0]),
                 FadeIn(chunks[0][1]), FadeIn(chunks[1][1]), FadeIn(chunks[2][1]), rt=0.5)
        self.at(2.8)   # "a map of the people and things"
        self.run(*[FadeIn(e, lag_ratio=0.2) for e in ents], rt=0.7)

        def node(n, x):
            c = Circle(radius=0.5).set_fill(PAGE, opacity=1).set_stroke(INK, width=3).move_to([x, -1.75, 0])
            return VGroup(c, serif(n, 34).next_to(c, DOWN, buff=0.1))
        nd, nf, nk = node("Daniel", -1.2), node("football", -4.2), node("kitchen", 1.8)
        e1 = Line(nd[0].get_left(), nf[0].get_right(), color=SPARK, stroke_width=5)
        e2 = Line(nd[0].get_right(), nk[0].get_left(), color=SPARK, stroke_width=5)
        lab = VGroup(serif("GraphRAG", 40), serif("(Microsoft, 2024)", 32, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
        lab.move_to([4.6, -1.55, 0])
        self.at(7.3)   # "related facts stay linked"
        self.run(FadeIn(nd), FadeIn(nf), FadeIn(nk), FadeIn(lab), rt=0.6)
        self.at(8.9)   # "even across chunks"
        self.run(Create(e1), Create(e2), rt=0.6)
        self.at(10.28)


# ── B06 — agentic search with code (14.36 s) ────────────────────────────────

class B06_Agentic(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("My project: search with code.")), rt=0.4)
        card = box(6.0, 3.4, fill=CARD).move_to([-3.2, 0.45, 0])
        code = VGroup(mono('grep("football")', 32), mono('grep("Daniel")', 32), mono("read_lines(5180, 5190)", 28)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(card).align_to(card, LEFT).shift(RIGHT * 0.4)
        self.at(1.9)   # "writes its own searches in code"
        self.run(FadeIn(card), rt=0.3)
        self.run(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in code], lag_ratio=0.5), rt=1.4)

        trail = VGroup(serif("football", 46), serif("Daniel", 46), serif("kitchen", 46)).arrange(DOWN, buff=0.75)
        trail.move_to([2.6, 0.45, 0]).align_to([0.3, 0, 0], LEFT)
        lns = VGroup(mono("line 3,780", 28, INK_SOFT), mono("5,091 · 5,187", 28, INK_SOFT), mono("line 6,021", 28, INK_SOFT))
        for l, t in zip(lns, trail):
            l.next_to(t, RIGHT, buff=0.35)
        ar = VGroup(arr(trail[0].get_bottom(), trail[1].get_top()), arr(trail[1].get_bottom(), trail[2].get_top()))
        for t, when in zip(range(3), (8.8, 9.6, 10.5)):
            self.at(when)
            anims = [FadeIn(trail[t]), FadeIn(lns[t])]
            if t > 0:
                anims.append(GrowArrow(ar[t - 1]))
            self.run(*anims, rt=0.45)
        tag = VGroup(bar(0.45), serif("very early work · 1 question · 1 run", 38)).arrange(RIGHT, buff=0.2)
        tag.move_to([0, -2.6, 0]).align_to([-6.0, 0, 0], LEFT)
        self.at(11.5)  # "That's very early work"
        self.run(FadeIn(tag), rt=0.5)
        self.at(14.36)


# ── B07 — citations (15.04 s) ───────────────────────────────────────────────

class B07_Citations(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Answers need receipts.")), rt=0.4)
        ans = VGroup(serif("answer:", 40, INK_SOFT), serif("kitchen", 64)).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        ans.move_to([0, 1.75, 0])
        q = serif("?", 64, INK_SOFT).next_to(ans, RIGHT, buff=0.3)
        ans[1].set_opacity(0.35)
        self.at(1.3)
        self.run(FadeIn(ans), FadeIn(q), rt=0.6)
        nb = serif("no source lines → nobody can check it", 40).move_to([0, 0.6, 0])
        self.at(4.4)
        self.run(FadeIn(nb), rt=0.5)
        chips = serif("insurance · healthcare · law:", 40)
        must = serif("must be checkable", 38)
        row = VGroup(chips, must).arrange(RIGHT, buff=0.5).move_to([0, -0.55, 0])
        self.at(6.4)   # "insurance, healthcare or law"
        self.run(FadeIn(chips), FadeIn(must), rt=0.8)

        cites = VGroup(*[VGroup(mono(n, 30), tick(s=0.26)).arrange(RIGHT, buff=0.12)
                         for n in ("3,780", "5,091", "5,187", "6,021")]).arrange(RIGHT, buff=0.55).move_to([0, -1.85, 0])
        rl = serif("the receipt: every line number it used", 34, INK_SOFT).next_to(cites, DOWN, buff=0.25)
        self.at(12.9)  # "My agent cited every line it used."
        self.run(FadeOut(nb), FadeIn(cites, lag_ratio=0.15), FadeIn(rl), rt=0.8)
        self.run(ans[1].animate.set_opacity(1), FadeOut(q), rt=0.5)
        self.at(15.04)


# ── B08 — privacy (6.91 s) ──────────────────────────────────────────────────

class B08_Privacy(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Keep the document local.")), rt=0.3)
        mach = box(6.4, 4.6).move_to([-2.9, -0.2, 0])
        ml = serif("your machine", 38).move_to(mach.get_top() + DOWN * 0.4)
        stack = page_stack(h=2.6, w=2.0, n=4).move_to([-2.9, -0.45, 0])
        stack[1].set_opacity(0.7)
        mdl = VGroup(serif("model", 46), Line(LEFT * 0.8, RIGHT * 0.8, color=INK, stroke_width=4)).arrange(DOWN, buff=0.08).move_to([4.2, 0.6, 0])
        self.at(0.7)
        self.run(FadeIn(mach), FadeIn(ml), FadeIn(stack), FadeIn(mdl), rt=0.6)
        lines = VGroup(*[Line(LEFT * 0.7, RIGHT * 0.7, color=INK, stroke_width=6).move_to([-2.9, 0.1 - 0.35 * i, 0]) for i in range(3)])
        self.at(2.0)   # "only the relevant lines need to leave"
        self.run(FadeIn(lines), rt=0.3)
        self.run(lines.animate.arrange(DOWN, buff=0.15).next_to(mdl, DOWN, buff=0.35), rt=0.9)
        l1 = serif("only these lines leave", 36).next_to(lines, DOWN, buff=0.3)
        l2 = serif("the document stays", 36).next_to(mach, DOWN, buff=0.15)
        self.run(FadeIn(l1), rt=0.4)
        self.at(5.2)   # "not the whole sensitive document"
        self.run(FadeIn(l2), rt=0.4)
        self.at(6.91)


# ── B09 — trade-offs (5.38 s) ───────────────────────────────────────────────

class B09_Tradeoffs(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The catch.")), rt=0.3)
        nodes = VGroup(*[Circle(radius=0.38).set_fill(PAGE, opacity=1).set_stroke(INK, width=4) for _ in range(5)]).arrange(RIGHT, buff=1.1)
        nodes.move_to([0, 1.2, 0])
        edges = VGroup(*[Line(nodes[i].get_right(), nodes[i + 1].get_left(), color=INK, stroke_width=5) for i in range(4)])
        hl = VGroup(*[serif(f"hop {i + 1}", 30, INK_SOFT).next_to(nodes[i], UP, buff=0.15) for i in range(5)])
        meter_l = serif("time & cost", 38).move_to([0, -0.45, 0]).align_to([-6.0, 0, 0], LEFT)
        meter = Rectangle(width=0.1, height=0.18).set_fill(INK, opacity=0.9).set_stroke(width=0).next_to(meter_l, RIGHT, buff=0.4)
        self.run(FadeIn(nodes[0]), FadeIn(hl[0]), FadeIn(meter_l), FadeIn(meter), rt=0.4)
        self.at(0.8)   # "more hops cost more time and money"
        anims = []
        for i in range(4):
            anims += [Create(edges[i]), FadeIn(nodes[i + 1]), FadeIn(hl[i + 1])]
        self.run(*anims, meter.animate.stretch_to_fit_width(7.2).align_to(meter, LEFT), rt=1.6)
        x = cross(s=0.5).move_to(edges[1])
        wrong = serif("one wrong step derails the rest", 40).move_to([0, -1.9, 0]).align_to([-6.0, 0, 0], LEFT)
        self.at(3.4)   # "one wrong step can derail the rest"
        self.run(Create(x), VGroup(*nodes[2:]).animate.set_stroke(INK_SOFT, opacity=0.5), VGroup(*edges[2:]).animate.set_stroke(INK_SOFT, opacity=0.5), FadeIn(wrong), rt=0.7)
        self.at(5.38)


# ── B10 — how it's measured (6.19 s) — verdict/artifact page ────────────────

class B10_Benchmarks(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        c = box(11.4, 5.8, fill=CARD).move_to([0, 0.2, 0])
        label = mono("Measured on", 26, INK_SOFT).move_to(c.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.4, aligned_edge=UL)
        rule = Line(c.get_left() + RIGHT * 0.3, c.get_right() + LEFT * 0.3, color=INK_SOFT, stroke_width=2)
        rule.next_to(label, DOWN, buff=0.15).set_x(0)
        head = serif("Multi-hop benchmarks", 54).next_to(rule, DOWN, buff=0.3).align_to(label, LEFT)
        cards = VGroup()
        for n, y in (("HotpotQA", "2018"), ("MuSiQue", "2022"), ("BABILong", "2024")):
            b = box(3.2, 1.7)
            t = VGroup(serif(n, 46), serif(y, 34, INK_SOFT)).arrange(DOWN, buff=0.08).move_to(b)
            cards.add(VGroup(b, t))
        cards.arrange(RIGHT, buff=0.4).next_to(head, DOWN, buff=0.4).set_x(0)
        foot = VGroup(tick(), serif("each answer needs several facts", 40)).arrange(RIGHT, buff=0.2).next_to(cards, DOWN, buff=0.4)
        self.run(FadeIn(c), FadeIn(label), Create(rule), FadeIn(head), rt=0.5)
        for i, t in enumerate((2.6, 3.9, 4.5)):
            self.at(t)
            self.run(FadeIn(cards[i], shift=UP * 0.1), rt=0.35)
        self.run(FadeIn(foot), rt=0.4)
        self.at(6.19)


# ── B12 — outro (4.48 s) ────────────────────────────────────────────────────

class B12_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        t1 = serif("Multi-Hop Search", 100)
        t2 = serif("Connecting the Pieces", 64, INK_SOFT)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to([0, 1.5, 0])
        rule = Line(LEFT * 4.6, RIGHT * 4.6, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.3)
        mark = wordmark(0.7).move_to([0, -1.75, 0])
        handle = serif("@HumanitariansAI", 56).next_to(mark, DOWN, buff=0.4)
        self.run(Write(t1), FadeIn(t2), rt=0.9)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(4.48)
