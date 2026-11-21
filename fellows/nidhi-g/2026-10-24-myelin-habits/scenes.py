"""
Manim scenes for myelin-habits (16:9). Body beats B02-B09 + @HumanitariansAI outro B11.

Evidence: trace counts re-counted from Downloads/myelin/data/historical_trajectories
(booking lookups 1,419 = 377 GPT-4o + 1,042 Sonnet; order lookups 1,029; flight searches 538;
user lookups 486). Design facts from Downloads/myelin/docs/DESIGN_SPECIFICATION.md.
B03 booking codes are illustrative, not from the traces. The B07 formula is a structured layout
(real fraction bar), per MATH-TYPESETTING.md; no LaTeX on this machine.

Claude palette: cream ground, warm ink, terracotta as the one accent (shapes only).
"""

import os

import numpy as np
from manim import *

HERE = os.path.dirname(os.path.abspath(__file__))
_HOME = os.environ.get("ART_HOME") or os.path.join(HERE, "..", "..", "brutalist")

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



def ital(s, size=40, color=INK):
    return Text(s, font=SERIF, font_size=size, color=color, slant="ITALIC")


def frac(num, den, size=48):
    """Structured fraction (MATH-TYPESETTING.md): grouped numerator, a real bar, grouped denominator."""
    n, d = ital(num, size), ital(den, size)
    w = max(n.width, d.width) + 0.3
    rule = Line(LEFT * w / 2, RIGHT * w / 2, color=INK, stroke_width=4)
    return VGroup(n.next_to(rule, UP, buff=0.14), rule, d.next_to(rule, DOWN, buff=0.14))


# ── B02 — agents repeat themselves (11.75 s) ────────────────────────────────

class B02_Repeat(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Agents repeat themselves.")), rt=0.4)
        rows = (("look up a booking", 1419), ("look up an order", 1029),
                ("search flights", 538), ("look up a user", 486))
        x0, full = -1.6, 5.6
        labels, bars, vals = VGroup(), VGroup(), VGroup()
        for i, (name, n) in enumerate(rows):
            y = 1.55 - 1.05 * i
            labels.add(serif(name, 40).move_to([0, y, 0]).align_to([-6.0, 0, 0], LEFT))
            b = Rectangle(width=full * n / 1419, height=0.55).set_fill(INK_SOFT, opacity=1).set_stroke(width=0)
            bars.add(b.move_to([x0 + b.width / 2, y, 0]))
            vals.add(mono(f"{n:,}", 34).next_to(b, RIGHT, buff=0.35))
        src = serif("public customer-service agent traces (tau-bench)", 34, INK_SOFT).move_to([0, -2.75, 0]).align_to([-6.0, 0, 0], LEFT)
        self.run(FadeIn(labels), rt=0.4)
        self.at(1.2)
        self.run(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.35), rt=2.2)
        self.run(FadeIn(vals), FadeIn(src), rt=0.5)
        self.at(9.6)   # "over fourteen hundred times"
        self.run(bars[0].animate.set_fill(INK), Indicate(vals[0], color=INK, scale_factor=1.15), rt=0.7)
        self.at(11.75)


# ── B03 — a habit, up close (10.13 s) ───────────────────────────────────────

class B03_Habit(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("A habit, up close.")), rt=0.4)
        codes = ("K7PL2Q", "M3XR8T", "B9WD4N", "Q2HV6C", "T5JF1Z", "R8NC3Y")
        card = box(4.9, 3.2, fill=CARD).move_to([-3.55, 0.75, 0])
        head = serif("customer: 6 bookings", 38).move_to(card.get_top() + DOWN * 0.5)
        grid = VGroup(*[mono(c, 32) for c in codes]).arrange_in_grid(3, 2, buff=(0.5, 0.28)).next_to(head, DOWN, buff=0.35)
        turns = VGroup()
        for i in range(6):
            b = box(1.75, 0.9)
            turns.add(VGroup(b, serif(f"turn {i + 1}", 36).move_to(b)))
        turns.arrange_in_grid(2, 3, buff=(0.3, 0.35)).move_to([3.2, 1.05, 0])
        dots = VGroup(*[Dot(radius=0.09, color=SPARK).next_to(t, DOWN, buff=0.12) for t in turns])
        tlab = serif("6 separate model turns", 38, INK_SOFT).next_to(turns, DOWN, buff=0.45)
        loop = VGroup(mono("for code in bookings:", 32), mono("details = lookup(code)", 32),
                      mono("keep(details)", 32)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        loop[1].shift(RIGHT * 0.6)
        loop[2].shift(RIGHT * 0.6)
        lc = box(loop.width + 0.8, loop.height + 0.6, fill=CARD)
        loopg = VGroup(lc, loop.move_to(lc)).move_to([-0.1, -2.15, 0])
        llab = serif("or one loop:", 38).next_to(loopg, LEFT, buff=0.35)
        self.at(2.6)   # "A customer has six bookings"
        self.run(FadeIn(card), FadeIn(head), FadeIn(grid), rt=0.6)
        self.at(4.9)   # "six separate model turns"
        for i in range(6):
            self.run(FadeIn(turns[i]), FadeIn(dots[i], scale=0.5), rt=0.25)
        self.run(FadeIn(tlab), rt=0.3)
        self.at(7.6)   # "A three-line loop could walk that list"
        self.run(FadeIn(llab), FadeIn(loopg, shift=UP * 0.1), rt=0.6)
        self.at(10.13)


# ── B04 — patterns, not puzzles (5.76 s) ────────────────────────────────────

class B04_Patterns(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Patterns, not puzzles.")), rt=0.3)
        rows = VGroup()
        for i, (k, p) in enumerate((("an ID", "name_name_1234"), ("a code", "AB12CD"), ("a date", "YYYY-MM-DD"))):
            y = 1.5 - 1.25 * i
            lab = serif(k, 48).move_to([-3.6, y, 0])
            chip = chipbox(p, 42, True).move_to([2.0, y, 0])
            rows.add(VGroup(lab, arr(lab.get_right() + RIGHT * 0.2, chip.get_left()), chip))
        tag = serif("a pattern, not a puzzle", 52).move_to([0, -2.45, 0])
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
        xa, xb = -5.6, 5.6
        top_y, bot_y = 0.9, -1.5
        top = Line([xa, top_y, 0], [xb, top_y, 0], color=INK, stroke_width=7)
        bot = Line([xa, bot_y, 0], [xb, bot_y, 0], color=INK, stroke_width=7)
        sheath = VGroup(*[RoundedRectangle(corner_radius=0.22, width=1.55, height=0.62).set_fill(CARD, opacity=1)
                          .set_stroke(INK_SOFT, width=3).move_to([xa + 0.95 + 1.85 * i, top_y, 0]) for i in range(6)])
        lt = serif("busy pathway: wrapped", 42).next_to(sheath, UP, buff=0.3).align_to([xa, 0, 0], LEFT)
        lb = serif("quiet pathway: bare", 42, INK_SOFT).next_to(bot, UP, buff=0.3).align_to([xa, 0, 0], LEFT)
        p1 = Dot([xa, top_y, 0], radius=0.17, color=SPARK).set_z_index(5)
        p2 = Dot([xa, bot_y, 0], radius=0.17, color=SPARK).set_z_index(5)
        self.run(Create(top), Create(bot), FadeIn(lt), FadeIn(lb), rt=0.6)
        self.at(1.2)   # "myelin wraps the brain's busiest nerve pathways"
        self.run(LaggedStart(*[GrowFromCenter(s) for s in sheath], lag_ratio=0.2), rt=1.6)
        self.at(4.8)   # "so their signals travel faster"
        self.add(p1, p2)
        # one 3.3 s play: the wrapped pathway's pulse arrives in a third of the time
        self.play(p1.animate.move_to([xb, top_y, 0]).set_rate_func(lambda t: min(1.0, 3 * t)),
                  p2.animate.move_to([xb, bot_y, 0]).set_rate_func(linear), run_time=3.3)
        self.t += 3.3
        fast = serif("faster", 40).next_to(p1, DOWN, buff=0.45)
        self.run(FadeIn(fast), rt=0.3)
        self.at(9.51)


# ── B06 — the planned pipeline (13.03 s) ────────────────────────────────────

class B06_Pipeline(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The planned pipeline.")), rt=0.4)

        def station(t, x, y):
            b = box(3.5, 1.05)
            return VGroup(b, serif(t, 36).move_to(b)).move_to([x, y, 0])
        s1 = station("mine past logs", -4.15, 1.3)
        s2 = station("keep ≥ 50 repeats", 0.0, 1.3)
        s3 = station("write Python", 4.15, 1.3)
        s4 = station("sandbox test", 4.15, -0.9)
        s5 = station("registry", 0.0, -0.9)
        a = [arr(s1.get_right(), s2.get_left()), arr(s2.get_right(), s3.get_left()),
             arr(s3.get_bottom(), s4.get_top()), arr(s4.get_left(), s5.get_right())]
        badge = serif("no network, no model", 34, INK_SOFT).next_to(s4, DOWN, buff=0.35)
        self.at(0.6)   # "mine an agent's past logs"
        self.run(FadeIn(s1), rt=0.4)
        self.at(2.3)   # "keep decisions that repeat at least fifty times"
        self.run(GrowArrow(a[0]), FadeIn(s2), rt=0.5)
        self.at(5.4)   # "have a strong model write a small Python function"
        self.run(GrowArrow(a[1]), FadeIn(s3), rt=0.5)
        self.at(9.6)   # "and test it in a sandbox"
        self.run(GrowArrow(a[2]), FadeIn(s4), rt=0.5)
        self.at(11.2)  # "with no network and no model"
        self.run(FadeIn(badge), GrowArrow(a[3]), FadeIn(s5), rt=0.6)
        self.at(13.03)


# ── B07 — the abstention rule (13.01 s) ─────────────────────────────────────

class B07_Abstain(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The abstention rule.")), rt=0.4)
        code = VGroup(mono("if not sure:", 36), mono('return "unsure"', 36)).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        code[1].shift(RIGHT * 0.65)
        cc = box(code.width + 0.8, code.height + 0.6, fill=CARD)
        codeg = VGroup(cc, code.move_to(cc)).move_to([-3.1, 1.5, 0])
        model = serif("the model takes over", 42).move_to([3.4, 1.5, 0])
        a1 = arr(codeg.get_right(), model.get_left())
        lhs = ital("agreement", 52)
        eq = serif("=", 52)
        fr = frac("correct", "total − unsure", 50)
        rhs = serif("≥ 0.98", 52)
        formula = VGroup(lhs, eq, fr, rhs).arrange(RIGHT, buff=0.35).move_to([0, -1.05, 0])
        sub = serif("on later sessions it never saw", 40, INK_SOFT).next_to(formula, DOWN, buff=0.45)
        self.at(0.8)
        self.run(FadeIn(codeg), rt=0.5)
        self.at(3.1)   # "it says so, and the model takes over"
        self.run(GrowArrow(a1), FadeIn(model), rt=0.6)
        self.at(6.0)   # "Where it does answer"
        self.run(FadeIn(lhs), FadeIn(eq), FadeIn(fr), rt=0.7)
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
        x0, W, y = -5.9, 11.8, 1.15
        old = Rectangle(width=W * 0.7, height=0.55).set_fill(CARD, opacity=1).set_stroke(INK_SOFT, width=2)
        new = Rectangle(width=W * 0.3, height=0.55).set_fill(PAGE, opacity=1).set_stroke(INK, width=3)
        old.move_to([x0 + old.width / 2, y, 0])
        new.next_to(old, RIGHT, buff=0)
        lo = serif("oldest 70% · build", 40).next_to(old, DOWN, buff=0.22)
        ln = serif("newest 30% · test", 40).next_to(new, DOWN, buff=0.22)
        tl = serif("past sessions, in time order", 34, INK_SOFT).next_to(old, UP, buff=0.2).align_to(old, LEFT)
        cards = VGroup()
        for head, sub in (("semantic cache", "reuses the answer to the\nmost similar past input"),
                          ("small classifier", None), ("small local model", None)):
            b = box(4.2 if sub else 3.65, 1.9)
            t = serif(head, 38)
            g = VGroup(t, serif(sub, 32, INK_SOFT)).arrange(DOWN, buff=0.15) if sub else t
            cards.add(VGroup(b, g.move_to(b)))
        cards.arrange(RIGHT, buff=0.25).move_to([0, -1.5, 0])
        self.at(0.6)   # "tested against simpler options"
        self.run(FadeIn(tl), FadeIn(old), FadeIn(new), FadeIn(lo), FadeIn(ln), rt=0.7)
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
        self.run(FadeIn(spark_line("What the plan delivers.")), rt=0.4)
        tag = mono("initial plan", 30, INK_SOFT).move_to([4.6, 2.95, 0])
        # package: a box with a lid band
        pk = box(2.6, 1.9, fill=CARD)
        lid = Line(pk.get_left() + UP * 0.45, pk.get_right() + UP * 0.45, color=INK_SOFT, stroke_width=3)
        ptxt = mono(".py", 40).move_to(pk).shift(DOWN * 0.25)
        pkg = VGroup(pk, lid, ptxt).move_to([-3.2, 0.85, 0])
        pl = VGroup(serif("habit compiler", 46), serif("a Python package", 36, INK_SOFT)).arrange(DOWN, buff=0.1).next_to(pkg, DOWN, buff=0.3)
        # dashboard: a screen with a grid; compiled habits filled
        sc = box(3.4, 1.9, fill=PAGE)
        cells = VGroup(*[Square(0.32).set_stroke(INK_SOFT, width=2) for _ in range(18)]).arrange_in_grid(3, 6, buff=0.14).move_to(sc)
        for k in (0, 3, 7, 8, 13):
            cells[k].set_fill(SPARK, opacity=1).set_stroke(SPARK)
        dash = VGroup(sc, cells).move_to([3.2, 0.85, 0])
        dl = VGroup(serif("dashboard", 46), serif("a map of compiled habits", 36, INK_SOFT)).arrange(DOWN, buff=0.1).next_to(dash, DOWN, buff=0.3)
        m1 = VGroup(tick(), serif("measured: call counts", 38)).arrange(RIGHT, buff=0.2)
        m2 = serif("not yet: speed · cost · savings", 38, INK_SOFT)
        meas = VGroup(m1, m2).arrange(RIGHT, buff=1.0).move_to([0, -2.6, 0])
        self.run(FadeIn(tag), rt=0.3)
        self.at(1.9)   # "a habit compiler"
        self.run(FadeIn(pkg), FadeIn(pl), rt=0.6)
        self.at(6.0)   # "and a dashboard"
        self.run(FadeIn(sc), LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.05), FadeIn(dl), rt=0.9)
        self.at(9.5)   # "So far, only the call counts are measured"
        self.run(FadeIn(m1), rt=0.5)
        self.at(11.9)  # "Any savings are still targets"
        self.run(FadeIn(m2), rt=0.5)
        self.at(14.49)


# ── B11 — outro (3.95 s) ────────────────────────────────────────────────────

class B11_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        t1 = serif("Myelin", 110)
        t2 = serif("Teaching Agents Habits", 62, INK_SOFT)
        t3 = serif("an initial plan", 44, INK_SOFT)
        title = VGroup(t1, t2, t3).arrange(DOWN, buff=0.2).move_to([0, 1.55, 0])
        rule = Line(LEFT * 4.6, RIGHT * 4.6, color=SPARK, stroke_width=4).next_to(title, DOWN, buff=0.3)
        mark = wordmark(0.7).move_to([0, -1.85, 0])
        handle = serif("@HumanitariansAI", 56).next_to(mark, DOWN, buff=0.4)
        self.run(Write(t1), FadeIn(t2), FadeIn(t3), rt=0.9)
        self.run(Create(rule), FadeIn(mark), FadeIn(handle), rt=0.5)
        self.at(3.95)
