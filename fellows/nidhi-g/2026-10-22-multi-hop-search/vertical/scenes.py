"""
Manim scenes for multi-hop-search/vertical: NATIVE 9:16 (frame 4.5 x 8 units).
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
    # one multi-line Text: a fixed baseline pitch, so lines without descenders are not crammed
    return Text("\n".join(lines), font=SERIF, font_size=size, color=color)


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


L = -1.85   # left text edge


def chipbox(t, size=38, mono_=False, fill=PAGE):
    tx = mono(t, size) if mono_ else serif(t, size)
    b = box(tx.width + 0.4, tx.height + 0.3, fill=fill)
    return VGroup(b, tx.move_to(b))


def arr(a, b, color=INK):
    return Arrow(a, b, buff=0.08, color=color, stroke_width=5, max_tip_length_to_length_ratio=0.3)


def left(m, y):
    return m.move_to([0, y, 0]).align_to([L, 0, 0], LEFT)


# ── B02 — iterative retrieval (11.67 s) ─────────────────────────────────────

class B02_Iterative(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Retrieve, read, again.")), rt=0.4)
        s1 = chipbox("search: football", 26, True, CARD)
        r1 = serif("Daniel took it", 42)
        s2 = chipbox("search: Daniel", 26, True, CARD)
        st = wrap("dropped → grabbed", 40, 3.2)
        fin = wrap("went to the kitchen", 40, 3.2)
        col = VGroup(s1, r1, s2, st, fin).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        col.move_to([0, 0.5, 0]).align_to([L, 0, 0], LEFT)
        for m in (r1, st, fin):
            m.shift(RIGHT * 0.4)
        ax = L + 0.2
        a1, a2, a3, a4 = [arr([ax, float(col[i].get_bottom()[1]), 0], [ax, float(col[i + 1].get_top()[1]), 0]) for i in range(4)]
        u = Line(LEFT * 1.4, RIGHT * 1.4, color=SPARK, stroke_width=6).next_to(fin, DOWN, buff=0.06).align_to(fin, LEFT)
        cap = wrap("each finding shapes the next search", 38, 3.6).next_to(u, DOWN, buff=0.12).align_to([L, 0, 0], LEFT)
        self.run(FadeIn(s1), rt=0.5)
        self.at(2.9)
        self.run(GrowArrow(a1), FadeIn(r1), rt=0.5)
        self.at(3.9)
        self.run(GrowArrow(a2), FadeIn(s2), rt=0.5)
        self.at(5.0)
        self.run(GrowArrow(a3), FadeIn(st), rt=0.5)
        self.at(6.4)
        self.run(GrowArrow(a4), FadeIn(fin), rt=0.4)
        self.at(7.9)
        self.run(FadeIn(cap), rt=0.5)
        self.at(10.4)
        self.run(Create(u), rt=0.4)
        self.at(11.67)


# ── B03 — Self-Ask (9.83 s) ─────────────────────────────────────────────────

class B03_SelfAsk(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Break it into steps.")), rt=0.4)
        q = left(fit(serif("Where is the football?", 42), 3.75), 2.4)
        def qbox(t, y):
            w = wrap(t, 38, 3.2)
            b = box(3.75, w.height + 0.3)
            return VGroup(b, w.move_to(b).align_to(b, LEFT).shift(RIGHT * 0.2)).move_to([0, y, 0])
        q1 = qbox("Who had the football?", 1.3)
        q2 = qbox("Where did they go last?", 0.0)
        a1 = arr([0, 2.12, 0], [0, q1.get_top()[1], 0])
        a2 = arr([0, q1.get_bottom()[1], 0], [0, q2.get_top()[1], 0])
        ch = VGroup(chipbox("search", 26, True), chipbox("search", 26, True)).arrange(RIGHT, buff=0.5).move_to([0, -1.25, 0])
        b1 = arr([-0.9, q2.get_bottom()[1], 0], ch[0].get_top())
        b2 = arr([0.9, q2.get_bottom()[1], 0], ch[1].get_top())
        lab = left(VGroup(serif("Self-Ask", 44), serif("(Press et al.)", 38, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.12), -2.45)
        self.run(FadeIn(q), rt=0.5)
        self.at(1.6)
        self.run(GrowArrow(a1), FadeIn(q1), GrowArrow(a2), FadeIn(q2), rt=0.7)
        self.at(3.1)
        self.run(FadeIn(lab), rt=0.5)
        self.at(8.6)
        self.run(GrowArrow(b1), GrowArrow(b2), FadeIn(ch), rt=0.6)
        self.at(9.83)


# ── B04 — IRCoT (14.61 s) ───────────────────────────────────────────────────

class B04_IRCoT(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Reason, then search.")), rt=0.4)
        t = left(serif("IRCoT", 72), 2.3)
        full = left(serif("Interleaving Retrieval\nwith Chain-of-Thought", 38), 1.35)
        fit(full, 3.75).align_to([L, 0, 0], LEFT)
        src = left(serif("Trivedi et al., ACL 2023", 36, INK_SOFT), 0.65)
        fit(src, 3.75).align_to([L, 0, 0], LEFT)
        self.at(0.8)
        self.run(FadeIn(t), rt=0.5)
        self.at(1.6)
        self.run(FadeIn(full), FadeIn(src), rt=0.6)
        c = [chipbox(n, 38, fill=(CARD if n == "reason" else PAGE)) for n in ("reason", "search", "reason", "search")]
        r1 = VGroup(c[0], c[1]).arrange(RIGHT, buff=0.6).move_to([0, -0.3, 0])
        r2 = VGroup(c[2], c[3]).arrange(RIGHT, buff=0.6).move_to([0, -1.25, 0])
        h1 = arr(c[0].get_right(), c[1].get_left()); h2 = arr(c[2].get_right(), c[3].get_left())
        d = arr(c[1].get_bottom(), c[2].get_top())
        self.at(6.2)
        self.run(FadeIn(c[0]), rt=0.4)
        self.at(7.4)
        self.run(GrowArrow(h1), FadeIn(c[1]), rt=0.4)
        self.run(GrowArrow(d), FadeIn(c[2]), rt=0.4)
        self.run(GrowArrow(h2), FadeIn(c[3]), rt=0.4)
        note = VGroup(bar(0.75), wrap("authors report better retrieval and answers", 38, 3.3)).arrange(RIGHT, buff=0.15)
        left(note, -2.5)
        self.at(10.4)
        self.run(FadeIn(note), rt=0.6)
        self.at(14.61)


# ── B05 — GraphRAG (10.28 s) ────────────────────────────────────────────────

class B05_Graph(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("GraphRAG.")), rt=0.4)
        contents = ("Daniel & football", "football", "Daniel & kitchen")
        chunks = VGroup()
        for i, n in enumerate(contents):
            b = box(3.8, 1.0, fill=CARD)
            lab = mono(f"chunk {i + 1}", 26, INK_SOFT)
            tx = serif(n, 38)
            g = VGroup(lab, tx).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(b).align_to(b, LEFT).shift(RIGHT * 0.2)
            chunks.add(VGroup(b, g))
        chunks.arrange(DOWN, buff=0.12).move_to([0, 1.1, 0])
        self.at(0.6)
        self.run(*[FadeIn(ch[0]) for ch in chunks], *[FadeIn(ch[1][0]) for ch in chunks], rt=0.5)
        self.at(2.8)
        self.run(*[FadeIn(ch[1][1]) for ch in chunks], rt=0.7)

        def node(x, y):
            return Circle(radius=0.28).set_fill(PAGE, opacity=1).set_stroke(INK, width=3).move_to([x, y, 0])
        nd, nf, nk = node(-0.2, -1.0), node(-1.05, -1.9), node(1.0, -1.9)
        ld = serif("Daniel", 40).next_to(nd, RIGHT, buff=0.15)
        lf = serif("football", 40).next_to(nf, DOWN, buff=0.06)
        lk = serif("kitchen", 40).next_to(nk, DOWN, buff=0.06)
        e1 = Line(nd.get_center(), nf.get_center(), color=SPARK, stroke_width=5).set_z_index(-1)
        e2 = Line(nd.get_center(), nk.get_center(), color=SPARK, stroke_width=5).set_z_index(-1)
        src = left(serif("(Microsoft, 2024)", 36, INK_SOFT), -3.05)
        self.at(7.3)
        self.run(FadeIn(nd), FadeIn(nf), FadeIn(nk), FadeIn(ld), FadeIn(lf), FadeIn(lk), FadeIn(src), rt=0.6)
        self.at(8.9)
        self.run(Create(e1), Create(e2), rt=0.6)
        self.at(10.28)


# ── B06 — agentic search with code (14.36 s) ────────────────────────────────

class B06_Agentic(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("My project: code search.")), rt=0.4)
        card = box(3.8, 1.6, fill=CARD).move_to([0, 1.95, 0])
        code = VGroup(mono('grep("football")', 26), mono('grep("Daniel")', 26), mono("read_lines(...)", 26)
                      ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(card).align_to(card, LEFT).shift(RIGHT * 0.2)
        self.at(1.9)
        self.run(FadeIn(card), rt=0.3)
        self.run(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in code], lag_ratio=0.5), rt=1.4)
        rows = VGroup()
        for w, n in (("football", "3,780"), ("Daniel", "5,091|5,187"), ("kitchen", "6,021")):
            nums = VGroup(*[mono(x, 26, INK_SOFT) for x in n.split("|")]).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
            r = VGroup(serif(w, 44), nums).arrange(RIGHT, buff=0.25)
            rows.add(r)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -0.5, 0]).align_to([-1.45, 0, 0], LEFT)
        downs = VGroup(arr([-1.75, rows[0].get_center()[1], 0], [-1.75, rows[1].get_center()[1], 0]),
                       arr([-1.75, rows[1].get_center()[1], 0], [-1.75, rows[2].get_center()[1], 0]))
        for i, when in enumerate((8.8, 9.6, 10.5)):
            self.at(when)
            anims = [FadeIn(rows[i])]
            if i > 0:
                anims.append(GrowArrow(downs[i - 1]))
            self.run(*anims, rt=0.45)
        tag = left(VGroup(bar(0.75), serif("very early work ·\n1 question · 1 run", 38)
                          ).arrange(RIGHT, buff=0.15), -2.6)
        self.at(11.5)
        self.run(FadeIn(tag), rt=0.5)
        self.at(14.36)


# ── B07 — citations (15.04 s) ───────────────────────────────────────────────

class B07_Citations(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Answers need receipts.")), rt=0.4)
        lab = left(serif("answer:", 38, INK_SOFT), 2.45)
        ans = left(serif("kitchen", 60), 1.85)
        q = serif("?", 60, INK_SOFT).next_to(ans, RIGHT, buff=0.25)
        ans.set_opacity(0.35)
        self.at(1.3)
        self.run(FadeIn(lab), FadeIn(ans), FadeIn(q), rt=0.6)
        nb = left(wrap("no source lines → nobody can check it", 38, 3.7), 0.75)
        self.at(4.4)
        self.run(FadeIn(nb), rt=0.5)
        fields = left(VGroup(bar(1.15), serif("insurance,\nhealthcare, law:\nmust be checkable", 38)).arrange(RIGHT, buff=0.15), -1.55)
        self.at(6.4)
        self.run(FadeIn(fields), rt=0.7)
        cites = VGroup(*[VGroup(mono(n, 28), tick(s=0.24)).arrange(RIGHT, buff=0.1) for n in ("3,780", "5,091", "5,187", "6,021")])
        cites.arrange_in_grid(rows=2, cols=2, buff=(0.6, 0.15)).move_to([0, 0.85, 0]).align_to([L, 0, 0], LEFT)
        rl = left(wrap("the receipt: every line it used", 36, 3.7, INK_SOFT), -0.1)
        self.at(12.9)
        self.run(FadeOut(nb), FadeIn(cites, lag_ratio=0.15), FadeIn(rl), rt=0.8)
        self.run(ans.animate.set_opacity(1), FadeOut(q), rt=0.5)
        self.at(15.04)


# ── B08 — privacy (6.91 s) ──────────────────────────────────────────────────

class B08_Privacy(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Keep it local.")), rt=0.3)
        mach = box(3.8, 3.2).move_to([0, 1.05, 0])
        ml = serif("your machine", 38).move_to(mach.get_top() + DOWN * 0.35)
        stack = page_stack(h=1.5, w=1.3, n=4).move_to([0, 1.0, 0])
        stack[1].set_opacity(0.7)
        stays = serif("the document stays", 36).move_to(mach.get_bottom() + UP * 0.32)
        mdl = VGroup(serif("model", 44), Line(LEFT * 0.75, RIGHT * 0.75, color=INK, stroke_width=4)).arrange(DOWN, buff=0.08).move_to([0, -1.2, 0])
        self.at(0.7)
        self.run(FadeIn(mach), FadeIn(ml), FadeIn(stack), FadeIn(mdl), rt=0.6)
        lines = VGroup(*[Line(LEFT * 0.5, RIGHT * 0.5, color=INK, stroke_width=6).move_to([0, 1.2 - 0.25 * i, 0]) for i in range(3)])
        self.at(2.0)
        self.run(FadeIn(lines), rt=0.3)
        self.run(lines.animate.arrange(DOWN, buff=0.12).next_to(mdl, DOWN, buff=0.25), rt=0.9)
        l1 = left(wrap("only these lines leave", 38, 3.7), -2.65)
        self.run(FadeIn(l1), rt=0.4)
        self.at(5.2)
        self.run(FadeIn(stays), rt=0.4)
        self.at(6.91)


# ── B09 — trade-offs (5.38 s) ───────────────────────────────────────────────

class B09_Tradeoffs(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The catch.")), rt=0.3)
        hl = left(serif("hops", 40, INK_SOFT), 2.35)
        nodes = VGroup(*[Circle(radius=0.22).set_fill(PAGE, opacity=1).set_stroke(INK, width=4) for _ in range(5)]).arrange(RIGHT, buff=0.38)
        nodes.move_to([0, 1.55, 0])
        edges = VGroup(*[Line(nodes[i].get_right(), nodes[i + 1].get_left(), color=INK, stroke_width=5) for i in range(4)])
        ml = left(serif("time & cost", 40), 0.55)
        meter = Rectangle(width=0.1, height=0.2).set_fill(INK, opacity=0.9).set_stroke(width=0).move_to([0, -0.05, 0]).align_to([L, 0, 0], LEFT)
        self.run(FadeIn(hl), FadeIn(nodes[0]), FadeIn(ml), FadeIn(meter), rt=0.4)
        self.at(0.8)
        anims = []
        for i in range(4):
            anims += [Create(edges[i]), FadeIn(nodes[i + 1])]
        self.run(*anims, meter.animate.stretch_to_fit_width(3.6).align_to([L, 0, 0], LEFT), rt=1.6)
        x = cross(s=0.34).move_to(edges[1])
        wrong = left(wrap("one wrong step derails the rest", 40, 3.6), -1.3)
        self.at(3.4)
        self.run(Create(x), VGroup(*nodes[2:]).animate.set_stroke(INK_SOFT, opacity=0.5),
                 VGroup(*edges[2:]).animate.set_stroke(INK_SOFT, opacity=0.5), FadeIn(wrong), rt=0.7)
        self.at(5.38)


# ── B10 — how it's measured (6.19 s) ────────────────────────────────────────

class B10_Benchmarks(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        label = mono("Measured on", 26, INK_SOFT).move_to([L, 3.1, 0], aligned_edge=UL)
        rule = Line([L, 2.62, 0], [1.85, 2.62, 0], color=INK_SOFT, stroke_width=2)
        head = left(serif("Multi-hop", 46), 2.25)
        cards = VGroup()
        for n, y in (("HotpotQA", "2018"), ("MuSiQue", "2022"), ("BABILong", "2024")):
            b = box(3.75, 1.12)
            t = VGroup(serif(n, 42), serif(y, 36, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(b).align_to(b, LEFT).shift(RIGHT * 0.25)
            cards.add(VGroup(b, t))
        cards.arrange(DOWN, buff=0.1).move_to([0, -0.02, 0])
        foot = left(VGroup(tick(), serif("each answer"+chr(10)+"needs several facts", 36)).arrange(RIGHT, buff=0.15), -2.75)
        self.run(FadeIn(label), Create(rule), FadeIn(head), rt=0.5)
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
        ma, mb = serif("Multi", 80), serif("Hop", 80)
        mb.next_to(ma, RIGHT, buff=0.22)
        # baseline-align on the capitals (the "p" descender would lift "Hop" under a bottom-align)
        mb.shift(UP * (float(ma[0].get_bottom()[1]) - float(mb[0].get_bottom()[1])))
        hy_y = float(ma[0].get_bottom()[1]) + 0.3 * float(ma[0].height)
        hy = Line([float(ma.get_right()[0]) - 0.08, hy_y, 0], [float(mb.get_left()[0]) + 0.08, hy_y, 0],
                  color=INK, stroke_width=9)
        t1 = VGroup(VGroup(ma, hy, mb), serif("Search", 80)).arrange(DOWN, buff=0.1)
        t2 = VGroup(serif("Connecting", 52, INK_SOFT), serif("the Pieces", 52, INK_SOFT)).arrange(DOWN, buff=0.02)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.3).move_to([0, 1.35, 0])
        fit(title, 3.8)
        rule = Line(LEFT * 1.7, RIGHT * 1.7, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.22)
        mark = wordmark(0.3).move_to([0, -1.85, 0])
        handle = serif("@HumanitariansAI", 42).next_to(mark, DOWN, buff=0.35)
        fit(handle, 3.6)
        self.run(FadeIn(t1), FadeIn(t2), rt=0.9)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(4.48)
