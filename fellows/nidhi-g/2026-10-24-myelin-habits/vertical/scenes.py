"""
Manim scenes for myelin-habits/vertical: NATIVE 9:16 (frame 4.5 x 8 units).
Portrait rules: serif >= 36, mono >= 26, wrap long lines (never shrink below the type floor).
Body beats B02-B09 + @HumanitariansAI outro B11.

Evidence: trace counts re-counted from Downloads/myelin/data/historical_trajectories.
Design facts from Downloads/myelin/docs/DESIGN_SPECIFICATION.md. B03 codes are illustrative.
The B07 formula is a structured layout (real fraction bar, aligned relations); no LaTeX here.

Claude palette: cream ground, warm ink, terracotta as the one accent (shapes only).
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
                 "runtime/fonts/EB_Garamond/static/EBGaramond-Italic.ttf",
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
    # portrait: borderless card fill. At 9:16 a border sits too close to its text and gate T
    # reads the pair as one fused run (§8.6b), so grouping comes from the CARD tint instead.
    return RoundedRectangle(corner_radius=0.1, width=w, height=h).set_fill(
        CARD, opacity=1).set_stroke(width=0)


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




def ital(s, size=40, color=INK):
    return Text(s, font=SERIF, font_size=size, color=color, slant="ITALIC")


def frac(num, den, size=44):
    """Structured fraction (MATH-TYPESETTING.md): grouped numerator, a real bar, grouped denominator."""
    n, d = ital(num, size), ital(den, size)
    w = max(n.width, d.width) + 0.2
    rule = Line(LEFT * w / 2, RIGHT * w / 2, color=INK, stroke_width=4)
    return VGroup(n.next_to(rule, UP, buff=0.1), rule, d.next_to(rule, DOWN, buff=0.1))


# ── B02 — agents repeat themselves (11.75 s) ────────────────────────────────

class B02_Repeat(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Agents repeat.")), rt=0.4)
        rows = (("look up a booking", 1419), ("look up an order", 1029),
                ("search flights", 538), ("look up a user", 486))
        full = 2.15
        labels, bars, vals = VGroup(), VGroup(), VGroup()
        for i, (name, n) in enumerate(rows):
            y = 2.4 - 1.12 * i
            labels.add(left(serif(name, 38), y))
            b = Rectangle(width=full * n / 1419, height=0.4).set_fill(INK_SOFT, opacity=1).set_stroke(width=0)
            bars.add(b.move_to([L + b.width / 2, y - 0.52, 0]))
            vals.add(mono(f"{n:,}", 28).next_to(b, RIGHT, buff=0.2))
        src = left(serif("public traces\n(tau-bench)", 36, INK_SOFT), -2.55)
        self.run(FadeIn(labels), rt=0.4)
        self.at(1.2)
        self.run(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.35), rt=2.2)
        self.run(FadeIn(vals), FadeIn(src), rt=0.5)
        self.at(9.6)   # "over fourteen hundred times"
        self.run(bars[0].animate.set_fill(INK), rt=0.6)
        self.at(11.75)


# ── B03 — a habit, up close (10.13 s) ───────────────────────────────────────

class B03_Habit(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("A habit, up close.")), rt=0.4)
        codes = ("K7PL2Q", "M3XR8T", "B9WD4N", "Q2HV6C", "T5JF1Z", "R8NC3Y")
        head = serif("6 bookings", 38)
        grid = VGroup(*[mono(c, 28) for c in codes]).arrange_in_grid(3, 2, buff=(0.45, 0.12))
        inner = VGroup(head, grid).arrange(DOWN, buff=0.15)
        card = box(3.7, inner.height + 0.35, fill=CARD)
        cardg = VGroup(card, inner.move_to(card)).move_to([0, 0, 0]).align_to([0, 2.72, 0], UP)
        turns = VGroup()
        for i in range(6):
            b = box(0.52, 0.52)
            turns.add(VGroup(b, serif(f"{i + 1}", 38).move_to(b)))
        turns.arrange(RIGHT, buff=0.12).move_to([0, 0.05, 0]).align_to([L, 0, 0], LEFT)
        dots = VGroup(*[Dot(radius=0.07, color=SPARK).next_to(t, DOWN, buff=0.1) for t in turns])
        tlab = left(serif("6 model turns", 38, INK_SOFT), -0.78)
        llab = left(serif("or one loop:", 38), -1.3)
        loop = VGroup(mono("for c in codes:", 26), mono("d = lookup(c)", 26), mono("keep(d)", 26)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        loop[1].shift(RIGHT * 0.35)
        loop[2].shift(RIGHT * 0.35)
        lc = box(loop.width + 0.4, loop.height + 0.3, fill=CARD)
        loopg = VGroup(lc, loop.move_to(lc))
        loopg.move_to([0, 0, 0]).align_to([0, -1.6, 0], UP).align_to([L, 0, 0], LEFT)
        self.at(2.6)   # "A customer has six bookings"
        self.run(FadeIn(cardg), FadeIn(VGroup(*[t[0] for t in turns])), FadeIn(lc), rt=0.6)
        self.at(4.9)   # "six separate model turns"
        for i in range(6):
            self.run(FadeIn(turns[i][1]), FadeIn(dots[i], scale=0.5), rt=0.25)
        self.run(FadeIn(tlab), rt=0.3)
        self.at(7.6)   # "A three-line loop could walk that list"
        self.run(FadeIn(llab), FadeIn(loop, shift=UP * 0.1), rt=0.6)
        self.at(10.13)


# ── B04 — patterns, not puzzles (5.76 s) ────────────────────────────────────

class B04_Patterns(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Not puzzles.")), rt=0.3)
        rows = VGroup()
        for i, (k, p) in enumerate((("an ID", "name_name_1234"), ("a code", "AB12CD"), ("a date", "YYYY-MM-DD"))):
            y = 2.25 - 1.45 * i
            lab = left(serif(k, 42), y)
            chip = chipbox(p, 26, True)
            chip.move_to([0, y - 0.65, 0]).align_to([L + 0.1, 0, 0], LEFT)
            rows.add(VGroup(lab, chip))
        tag = left(serif("a pattern,\nnot a puzzle", 46), -2.5)
        self.at(1.6)   # "IDs, codes, dates"
        self.run(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows], lag_ratio=0.3), rt=1.4)
        self.at(4.0)   # "a pattern, not a puzzle"
        self.run(FadeIn(tag), rt=0.5)
        self.at(5.76)


# ── B05 — why "Myelin" (9.51 s) ─────────────────────────────────────────────

class B05_Myelin(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Why “Myelin”.")), rt=0.4)
        xa, xb = -1.7, 1.7
        top_y, bot_y = 1.0, -1.8
        top = Line([xa, top_y, 0], [xb, top_y, 0], color=INK, stroke_width=7)
        bot = Line([xa, bot_y, 0], [xb, bot_y, 0], color=INK, stroke_width=7)
        sheath = VGroup(*[RoundedRectangle(corner_radius=0.18, width=0.95, height=0.5).set_fill(CARD, opacity=1)
                          .set_stroke(INK_SOFT, width=3).move_to([xa + 0.62 + 1.23 * i, top_y, 0]) for i in range(3)])
        lt = left(wrap("busy pathway: wrapped", 40, 3.7), top_y + 0.95)
        lb = left(wrap("quiet pathway: bare", 40, 3.7, INK_SOFT), bot_y + 0.95)
        p1 = Dot([xa, top_y, 0], radius=0.14, color=SPARK).set_z_index(5)
        p2 = Dot([xa, bot_y, 0], radius=0.14, color=SPARK).set_z_index(5)
        self.run(Create(top), Create(bot), FadeIn(lt), FadeIn(lb), rt=0.6)
        self.at(1.2)   # "myelin wraps the brain's busiest nerve pathways"
        self.run(LaggedStart(*[GrowFromCenter(s) for s in sheath], lag_ratio=0.25), rt=1.4)
        self.at(4.8)   # "so their signals travel faster"
        self.add(p1, p2)
        # one 3.3 s play: the wrapped pathway's pulse arrives in a third of the time
        self.play(p1.animate.move_to([xb, top_y, 0]).set_rate_func(lambda t: min(1.0, 3 * t)),
                  p2.animate.move_to([xb, bot_y, 0]).set_rate_func(linear), run_time=3.3)
        self.t += 3.3
        fast = serif("faster", 40).move_to([0, top_y - 0.65, 0]).align_to([xb, 0, 0], RIGHT)
        self.run(FadeIn(fast), rt=0.3)
        self.at(9.51)


# ── B06 — the planned pipeline (13.03 s) ────────────────────────────────────

class B06_Pipeline(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The planned pipeline.")), rt=0.4)

        def station(t, y):
            b = box(3.5, 0.66)
            return VGroup(b, serif(t, 38).move_to(b)).move_to([0, y, 0])
        ys = (2.4, 1.43, 0.46, -0.51, -1.48)
        st = [station(t, y) for t, y in zip(("mine past logs", "keep ≥ 50 repeats", "write Python",
                                             "sandbox test", "registry"), ys)]
        a = [arr(st[i].get_bottom(), st[i + 1].get_top()) for i in range(4)]
        badge = left(serif("sandbox:\nno network,\nno model", 36, INK_SOFT), -2.65)
        self.run(FadeIn(VGroup(*[x[0] for x in st])), rt=0.3)
        self.at(0.6)   # "mine an agent's past logs"
        self.run(FadeIn(st[0][1]), rt=0.4)
        self.at(2.3)   # "keep decisions that repeat at least fifty times"
        self.run(GrowArrow(a[0]), FadeIn(st[1][1]), rt=0.5)
        self.at(5.4)   # "have a strong model write a small Python function"
        self.run(GrowArrow(a[1]), FadeIn(st[2][1]), rt=0.5)
        self.at(9.6)   # "and test it in a sandbox"
        self.run(GrowArrow(a[2]), FadeIn(st[3][1]), rt=0.5)
        self.at(11.2)  # "with no network and no model"
        self.run(FadeIn(badge), GrowArrow(a[3]), FadeIn(st[4][1]), rt=0.6)
        self.at(13.03)


# ── B07 — the abstention rule (13.01 s) ─────────────────────────────────────

class B07_Abstain(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The abstention rule.")), rt=0.4)
        when = left(serif("when not sure:", 38), 2.45)
        code = mono('return "unsure"', 26)
        cc = box(code.width + 0.4, code.height + 0.35, fill=CARD)
        codeg = VGroup(cc, code.move_to(cc)).move_to([0, 1.8, 0]).align_to([L, 0, 0], LEFT)
        model = serif("model takes over", 40)
        model.move_to([0, 0.75, 0]).align_to([L, 0, 0], LEFT)
        ax = L + 0.5
        a1 = arr([ax, codeg.get_bottom()[1], 0], [ax, model.get_top()[1], 0])
        # aligned relations: each line starts with its relation
        lhs = left(ital("agreement", 46), -0.2)
        eq = serif("=", 46)
        fr = frac("correct", "total − unsure", 42)
        row2 = VGroup(eq, fr).arrange(RIGHT, buff=0.25)
        left(row2, -1.25)
        rhs = left(serif("≥ 0.98", 46), -2.25)
        sub = left(wrap("on later sessions it never saw", 36, 3.7, INK_SOFT), -2.95)
        self.at(0.8)
        self.run(FadeIn(when), FadeIn(codeg), rt=0.5)
        self.at(3.1)   # "it says so, and the model takes over"
        self.run(GrowArrow(a1), FadeIn(model), rt=0.6)
        self.at(6.0)   # "Where it does answer"
        self.run(FadeIn(lhs), FadeIn(row2), rt=0.7)
        self.at(8.8)   # "at least ninety-eight percent"
        self.run(FadeIn(rhs), rt=0.5)
        self.at(10.9)  # "on later sessions it never saw"
        self.run(FadeIn(sub), rt=0.5)
        self.at(13.01)


# ── B08 — a fair test (10.50 s) ─────────────────────────────────────────────

class B08_Baselines(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("A fair test.")), rt=0.4)
        W, y = 3.7, 2.3
        old = Rectangle(width=W * 0.7, height=0.5).set_fill(CARD, opacity=1).set_stroke(INK_SOFT, width=2)
        new = Rectangle(width=W * 0.3, height=0.5).set_fill(PAGE, opacity=1).set_stroke(INK, width=3)
        old.move_to([L + old.width / 2, y, 0])
        new.next_to(old, RIGHT, buff=0)
        lo = left(serif("oldest 70%: build", 38), 1.6)
        ln = left(serif("newest 30%: test", 38), 1.05)
        cards = VGroup()
        for head, sub in (("semantic cache", "reuses the closest past answer"),
                          ("small classifier", None), ("small local model", None)):
            t = serif(head, 36)
            g = VGroup(t, wrap(sub, 36, 3.2, INK_SOFT)).arrange(DOWN, aligned_edge=LEFT, buff=0.12) if sub else t
            b = box(3.7, g.height + 0.4)
            cards.add(VGroup(b, g.move_to(b).align_to(b, LEFT).shift(RIGHT * 0.18)))
        cards.arrange(DOWN, buff=0.15)
        cards.move_to([0, 0, 0]).align_to([0, 0.5, 0], UP).align_to([L, 0, 0], LEFT)
        self.at(0.6)   # "tested against simpler options"
        self.run(FadeIn(old), FadeIn(new), FadeIn(lo), FadeIn(ln), rt=0.7)
        self.at(2.8)   # "a semantic cache"
        self.run(FadeIn(cards[0], shift=UP * 0.1), rt=0.5)
        self.at(7.6)   # "a small classifier"
        self.run(FadeIn(cards[1], shift=UP * 0.1), rt=0.4)
        self.at(8.9)   # "and a small local model"
        self.run(FadeIn(cards[2], shift=UP * 0.1), rt=0.4)
        self.at(10.5)


# ── B09 — what the plan delivers (14.49 s) — verdict/artifact page ──────────

class B09_Delivers(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("What it delivers.")), rt=0.4)
        tag = left(mono("initial plan", 26, INK_SOFT), 2.5)
        pk = box(1.25, 0.9, fill=CARD)
        lid = Line(pk.get_left() + UP * 0.2, pk.get_right() + UP * 0.2, color=INK_SOFT, stroke_width=3)
        pkg = VGroup(pk, lid, mono(".py", 28).move_to(pk).shift(DOWN * 0.12))
        pl = VGroup(serif("habit\ncompiler", 38), mono("package", 26, INK_SOFT)).arrange(DOWN, buff=0.12)
        col1 = VGroup(pkg, pl).arrange(DOWN, buff=0.2).move_to([-0.95, 1.05, 0])
        sc = box(1.25, 0.9, fill=PAGE)
        cells = VGroup(*[Square(0.17).set_stroke(INK_SOFT, width=2) for _ in range(12)]).arrange_in_grid(3, 4, buff=0.07).move_to(sc)
        for k in (0, 5, 6, 11):
            cells[k].set_fill(SPARK, opacity=1).set_stroke(SPARK)
        dash = VGroup(sc, cells)
        dl = VGroup(serif("dashboard", 38), mono("habit map", 26, INK_SOFT)).arrange(DOWN, buff=0.12)
        col2 = VGroup(dash, dl).arrange(DOWN, buff=0.2)
        col2.move_to([0.95, 0, 0]).align_to(col1, UP)
        pl.align_to(dl, UP)
        h1 = left(serif("measured:", 38), -0.95)
        v1 = VGroup(tick(), serif("call counts", 38)).arrange(RIGHT, buff=0.15)
        v1.move_to([0, -1.5, 0]).align_to([L + 0.2, 0, 0], LEFT)
        h2 = left(serif("not yet:", 38, INK_SOFT), -2.15)
        v2 = serif("speed, savings", 38, INK_SOFT).move_to([0, -2.7, 0]).align_to([L + 0.2, 0, 0], LEFT)
        self.run(FadeIn(tag), rt=0.3)
        self.at(1.9)   # "a habit compiler"
        self.run(FadeIn(col1), rt=0.6)
        self.at(6.0)   # "and a dashboard"
        self.run(FadeIn(col2), FadeIn(h1), FadeIn(h2), rt=0.7)
        self.at(9.5)   # "So far, only the call counts are measured"
        self.run(FadeIn(v1), rt=0.5)
        self.at(11.9)  # "Any savings are still targets"
        self.run(FadeIn(v2), rt=0.5)
        self.at(14.49)


# ── B11 — outro (3.95 s) ────────────────────────────────────────────────────

class B11_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        t1 = serif("Myelin", 96)
        t2 = serif("Teaching Agents\nHabits", 50, INK_SOFT)
        t3 = serif("an initial plan", 40, INK_SOFT)
        title = VGroup(t1, t2, t3).arrange(DOWN, buff=0.25).move_to([0, 1.5, 0])
        fit(title, 3.6)
        rule = Line(LEFT * 1.7, RIGHT * 1.7, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.25)
        mark = wordmark(0.3).move_to([0, -1.85, 0])
        handle = fit(serif("@HumanitariansAI", 42), 3.6).next_to(mark, DOWN, buff=0.35)
        self.run(FadeIn(t1), FadeIn(t2), FadeIn(t3), rt=0.9)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(3.95)
