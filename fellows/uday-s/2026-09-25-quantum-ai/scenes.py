"""Manim beats for the reel `quantum-ai`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Every figure on screen carries a source (also in SOURCES.md):
  AlphaQubit    Google DeepMind, Nature 2024 -- 6% vs tensor network,
                30% vs correlated matching, tested 17 -> 241 qubits
  Dequantization  Ewin Tang 2018 onward -- quantum recommendation systems and
                a class of QML algorithms; topological data analysis resisted
  Willow        Google 2024 -- 105 qubits, first below-threshold error correction
  Roadmap       IBM -- 200 logical qubits 2029, 1,000 early 2030s

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over eight previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * _fit scales UP as well as down (FILL-THE-CANVAS)
  * a beat carried by text alone has no shape-state -- give it geometry
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, FadeOut, LaggedStart, Line,
    RoundedRectangle, Scene, Text, VGroup, Write,
)

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR",
    "D:/Projects/brutalist.art/.claude/worktrees/video-creation-setup-4c85fe/runtime/fonts",
)
for _ttf in glob.glob(os.path.join(_TOOLKIT_FONTS, "**", "*.ttf"), recursive=True):
    manimpango.register_font(os.path.abspath(_ttf))

_FAMS = set(manimpango.list_fonts())
SERIF = "EB Garamond" if "EB Garamond" in _FAMS else "Georgia"
SANS = "Inter 28pt" if "Inter 28pt" in _FAMS else "Segoe UI"
MONO = "Consolas" if "Consolas" in _FAMS else "Courier New"

CREAM = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#6B6559"
TERRA = "#D97757"

BODY_TOP = 2.25
BODY_BOTTOM = -2.45
BODY_W = 12.0
BODY_H = BODY_TOP - BODY_BOTTOM
SRC_BOTTOM = -1.95


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    k = Text(text, font=SANS, font_size=22, color=INK_SOFT).to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.9)
    rule = Line(k.get_left() + DOWN * 0.28, k.get_left() + RIGHT * 12.0 + DOWN * 0.28,
                stroke_width=1.4, color=INK_SOFT)
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.20).align_to(k, LEFT)
        grp.add(s)
    return grp


def spark(text):
    return Text(text, font=SERIF, font_size=37, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    return Text(text, font=MONO, font_size=16, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def _fit(group, w, h, centre_y, grow=1.9):
    if group.width <= 0 or group.height <= 0:
        return group
    k = min(w / group.width, h / group.height)
    k = min(k, grow) if k > 1 else k
    group.scale(k)
    group.move_to([0, centre_y, 0])
    return group


def fit(group, w=BODY_W, h=BODY_H):
    return _fit(group, w, h, (BODY_TOP + BODY_BOTTOM) / 2)


def fit_src(group, w=BODY_W):
    return _fit(group, w, BODY_TOP - SRC_BOTTOM, (BODY_TOP + SRC_BOTTOM) / 2)


def chip(label, color, font_size=19, pad=0.32, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(box, t)


def node(label, color=INK_SOFT, fs=26, pad_w=0.9, h=1.0):
    t = Text(label, font=SANS, font_size=fs, color=color)
    b = RoundedRectangle(width=t.width + pad_w, height=h, corner_radius=0.12,
                         stroke_width=2.0, stroke_color=color, fill_opacity=0)
    b.move_to(t.get_center())
    return VGroup(b, t)


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=20, title_fs=24):
    t = Text(title, font=SANS, font_size=title_fs, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_ArrowReversed(Scene):
    """BLUF: the expected direction, then the demonstrated one. 19.78s."""

    def construct(self):
        page(self)
        head = kicker("WHICH WAY DOES IT RUN?", "the usual story, and the measured one")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        q = node("QUANTUM", INK_SOFT)
        a = node("AI", INK_SOFT)
        pair = VGroup(q, a).arrange(RIGHT, buff=3.4)
        fit(pair)

        gap_l, gap_r = q[0].get_right(), a[0].get_left()
        fwd = Line(gap_l + RIGHT * 0.15, gap_r + LEFT * 0.15,
                   stroke_width=3.0, color=INK)
        fwd_lab = Text("the usual story", font=SANS, font_size=23, color=INK)
        fwd_lab.next_to(fwd, UP, buff=0.26)

        back = Line(gap_r + LEFT * 0.15, gap_l + RIGHT * 0.15,
                    stroke_width=3.4, color=TERRA)
        back_lab = Text("what is demonstrated", font=SANS, font_size=23, color=TERRA)
        back_lab.next_to(back, DOWN, buff=0.26)

        self.play(Create(q[0]), FadeIn(q[1]), Create(a[0]), FadeIn(a[1]), run_time=1.6)
        self.wait(0.8)
        self.play(Create(fwd), FadeIn(fwd_lab), run_time=1.6)
        self.wait(1.6)
        self.play(FadeOut(fwd), FadeOut(fwd_lab), run_time=0.9)
        self.play(Create(back), FadeIn(back_lab), run_time=1.8)
        self.wait(1.8)

        point = spark("AI is what makes quantum work today")
        self.play(Write(point), run_time=2.1)
        self.wait(6.48)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: three questions for any quantum AI claim. 19.50s."""

    QS = [
        ("1", "WHICH\nDIRECTION?", "quantum helping AI,\nor AI helping quantum?"),
        ("2", "WHERE DOES THE\nDATA LIVE?", "classical data must be\nloaded into a state"),
        ("3", "DID CLASSICAL\nTRY?", "was a good classical\nalgorithm written?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS", "ask these of any quantum AI claim")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.QS:
            n = Text(num, font=SERIF, font_size=32, color=TERRA)
            t = Text(title, font=SANS, font_size=25, color=INK, line_spacing=0.7)
            b = Text(body, font=MONO, font_size=19, color=INK_SOFT, line_spacing=0.7)
            hr = VGroup(n, t).arrange(RIGHT, buff=0.28, aligned_edge=UP)
            inner = VGroup(hr, b).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.8, height=inner.height + 0.8,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.42))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.05)
            self.wait(1.45)

        point = spark("Most of the field sorts itself on these")
        self.play(Write(point), run_time=2.0)
        self.wait(5.10)


class B03_AlphaQubit(Scene):
    """EVIDENCE: question 1 — the demonstrated result. 28.60s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 — WHICH DIRECTION",
                      "a transformer that decodes errors inside a quantum processor")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def result(big, against):
            n = Text(big, font=SERIF, font_size=64, color=TERRA)
            a = Text(against, font=MONO, font_size=20, color=INK, line_spacing=0.7)
            inner = VGroup(n, a).arrange(DOWN, buff=0.22)
            box = RoundedRectangle(width=inner.width + 1.0, height=inner.height + 0.8,
                                   corner_radius=0.13, stroke_width=1.9,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            return VGroup(box, inner)

        r1 = result("6%", "better than\ntensor network decoding")
        r2 = result("30%", "better than\ncorrelated matching")
        pair = VGroup(r1, r2).arrange(RIGHT, buff=0.9, aligned_edge=UP)

        rng = Text("held from 17 qubits to 241", font=SANS, font_size=24, color=INK)
        direction = Text("AI  →  QUANTUM", font=SANS, font_size=27, color=TERRA)
        body = fit_src(VGroup(pair, rng, direction).arrange(DOWN, buff=0.42))
        src = source_line("AlphaQubit · Google DeepMind · Nature, 2024")

        self.play(Create(r1[0]), FadeIn(r1[1]), run_time=1.9)
        self.wait(1.4)
        self.play(Create(r2[0]), FadeIn(r2[1]), run_time=1.9)
        self.wait(1.6)
        self.play(FadeIn(rng, shift=UP * 0.15), run_time=1.4)
        self.wait(1.2)
        self.play(Write(direction), run_time=1.9)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.4)

        point = spark("The network is helping the machine")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(8.47)


class B04_LoadingBottleneck(Scene):
    """EVIDENCE: question 2 — the load step is the bottleneck. 20.10s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 — WHERE THE DATA LIVES",
                      "the step the headline never mentions")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = node("CLASSICAL\nDATA", INK_SOFT, fs=23, pad_w=0.9, h=1.3)
        b = node("ENCODE INTO A\nQUANTUM STATE", TERRA, fs=23, pad_w=1.5, h=1.8)
        c = node("QUANTUM\nALGORITHM", INK_SOFT, fs=23, pad_w=0.9, h=1.3)
        chain = VGroup(a, b, c).arrange(RIGHT, buff=0.75, aligned_edge=DOWN)
        links = VGroup(
            Line(a[0].get_right(), b[0].get_left(), stroke_width=2.2, color=INK_SOFT),
            Line(b[0].get_right(), c[0].get_left(), stroke_width=2.2, color=INK_SOFT),
        )
        note = Text("this step can cost as much as the algorithm saves",
                    font=SANS, font_size=24, color=TERRA)
        fit(VGroup(VGroup(chain, links), note).arrange(DOWN, buff=0.6))

        self.play(Create(a[0]), FadeIn(a[1]), run_time=1.3)
        self.play(Create(links[0]), run_time=0.5)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=1.6)
        self.play(Create(links[1]), run_time=0.5)
        self.play(Create(c[0]), FadeIn(c[1]), run_time=1.3)
        self.wait(1.4)
        self.play(Write(note), run_time=2.2)
        self.wait(1.4)

        point = spark("Fast once it is in. Getting it in is the problem.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(5.27)


class B05_Dequantized(Scene):
    """EVIDENCE: question 3 — the gap that vanished. 32.23s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 — DID CLASSICAL TRY?",
                      "2018 · an undergraduate was asked to prove the speedup")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def bar(label, width, color):
            b = RoundedRectangle(width=width, height=0.66, corner_radius=0.08,
                                 stroke_width=2.0, stroke_color=color, fill_opacity=0)
            t = Text(label, font=MONO, font_size=21, color=color)
            t.next_to(b, LEFT, buff=0.45)
            return VGroup(t, b)

        qb = bar("quantum", 1.9, INK)
        cb = bar("classical", 7.4, INK_SOFT)
        for r in (qb, cb):
            r[1].align_to(qb[1], LEFT)
        bars = VGroup(qb, cb).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        claim = Text("the claimed exponential gap", font=SANS, font_size=23, color=INK_SOFT)
        # Both later labels are composed INTO the fitted group. Positioning them
        # relative to `bars` after fit_src() puts them on the citation strip.
        deq = Text("dequantized — the advantage was in the input assumptions",
                   font=SANS, font_size=24, color=TERRA)
        survived = Text("not all of them — topological data analysis resisted",
                        font=MONO, font_size=20, color=INK_SOFT)
        body = fit_src(VGroup(claim, bars, deq, survived).arrange(DOWN, buff=0.40))
        src = source_line("Ewin Tang, 2018 onward · quantum recommendation systems, then a class of QML")

        self.play(FadeIn(claim), run_time=0.9)
        self.play(FadeIn(qb[0]), Create(qb[1]), run_time=1.3)
        self.play(FadeIn(cb[0]), Create(cb[1]), run_time=1.6)
        self.wait(1.8)

        # the classical bar contracts to match — the speedup was in the assumptions
        self.play(cb[1].animate.stretch_to_fit_width(1.9).align_to(qb[1], LEFT)
                  .set_stroke(TERRA), cb[0].animate.set_color(TERRA), run_time=2.6)
        self.play(Write(deq), run_time=2.4)
        self.wait(1.4)

        self.play(FadeIn(survived), FadeIn(src), run_time=1.5)
        self.wait(1.4)

        point = spark("A speedup nobody tried to beat is not a speedup")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(9.43)


class B06_WhatSurvives(Scene):
    """EVIDENCE: which promised industries survive the three questions. 23.08s."""

    ROWS = [("drug discovery", True), ("material science", True),
            ("financial forecasting", False), ("supply-chain forecasting", False)]

    def construct(self):
        page(self)
        head = kicker("WHAT SURVIVES THE THREE QUESTIONS",
                      "the four industries usually promised")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for name, ok in self.ROWS:
            c = INK if ok else TERRA
            box = RoundedRectangle(width=0.32, height=0.32, corner_radius=0.06,
                                   stroke_width=2.0, stroke_color=c, fill_opacity=0)
            t = Text(name, font=MONO, font_size=24, color=c)
            t.next_to(box, RIGHT, buff=0.38)
            reason = Text("the simulated system is itself quantum" if ok
                          else "classical data — see question 2",
                          font=SANS, font_size=20, color=INK_SOFT)
            rows.add(VGroup(box, t, reason))
        lw = max(r[1].width for r in rows)
        for r in rows:
            r[2].next_to(r[1], RIGHT, buff=0.8 + (lw - r[1].width))
        rows.arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        fit(rows)

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1], shift=RIGHT * 0.2), FadeIn(r[2]),
                      run_time=1.4)
            self.wait(0.7)
        self.wait(1.2)

        point = spark("Two of four — and for a reason, not a hope")
        self.play(Write(point), run_time=2.1)
        self.wait(6.48)


class B07_Roadmap(Scene):
    """EVIDENCE: the timeline, and the caveat on the famous benchmark. 34.21s."""

    STOPS = [("2024", "Willow · 105 qubits", "first below-threshold\nerror correction"),
             ("2029", "IBM roadmap", "200 logical qubits"),
             ("early 2030s", "IBM roadmap", "1,000 logical qubits")]

    def construct(self):
        page(self)
        head = kicker("AND WHEN?", "a milestone, not an arrival")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        stops = VGroup()
        for when, what, detail in self.STOPS:
            w = Text(when, font=MONO, font_size=23, color=INK)
            a = Text(what, font=SANS, font_size=20, color=INK_SOFT)
            d = Text(detail, font=SANS, font_size=19, color=INK_SOFT, line_spacing=0.7)
            stops.add(VGroup(w, a, d).arrange(DOWN, buff=0.16))
        stops.arrange(RIGHT, buff=0.85)
        axis = Line(stops.get_left() + LEFT * 0.25, stops.get_right() + RIGHT * 0.25,
                    stroke_width=2.0, color=INK_SOFT)
        axis.next_to(stops, DOWN, buff=0.26)
        timeline = VGroup(stops, axis)

        caveat = panel("THE FAMOUS BENCHMARK", [
            "5 minutes vs 10^25 years",
            "is random circuit sampling —",
            "chosen to be hard for classical",
            "machines, not because it is useful",
        ], TERRA, min_w=5.6, fs=20)

        body = fit_src(VGroup(timeline, caveat).arrange(DOWN, buff=0.55))
        src = source_line("Google Willow (2024) · published IBM roadmap")

        self.play(Create(axis), run_time=1.2)
        for s in stops:
            self.play(FadeIn(s, shift=UP * 0.15), run_time=1.3)
            self.wait(0.8)
        self.wait(1.2)
        self.play(Create(caveat[0]), FadeIn(caveat[1][0]), run_time=1.5)
        for line in caveat[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.85)
        self.wait(1.4)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.2)

        point = spark("Google says real problems need a million qubits")
        self.play(Write(point), run_time=2.2)
        self.wait(10.34)


class B08_Verdict(Scene):
    """VERDICT: all three scored, plus what to believe and what to doubt. 22.78s."""

    SCORES = [
        ("DIRECTION", "the wins today run AI → quantum", TERRA),
        ("THE DATA", "loading classical data is the bottleneck", INK),
        ("CLASSICAL", "assume dequantization until someone tried", INK),
    ]

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three questions, after the evidence")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for axis, answer, color in self.SCORES:
            a = Text(axis, font=SANS, font_size=25, color=INK_SOFT)
            v = Text(answer, font=MONO, font_size=21, color=color)
            cell = RoundedRectangle(width=v.width + 0.6, height=0.7, corner_radius=0.09,
                                    stroke_width=1.7, stroke_color=color, fill_opacity=0)
            cell.move_to(v.get_center())
            rows.add(VGroup(a, VGroup(cell, v)))
        lw = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.6 + (lw - r[0].width))
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT)

        yes = Text("BE EXCITED ABOUT:  simulating matter — chemistry, materials",
                   font=SANS, font_size=22, color=INK)
        no = Text("BE SCEPTICAL OF:  pattern-finding on your spreadsheet",
                  font=SANS, font_size=22, color=TERRA)
        tail = VGroup(yes, no).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        fit(VGroup(rows, tail).arrange(DOWN, buff=0.55))

        self.play(LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.18) for r in rows],
                              lag_ratio=0.2), run_time=1.0)
        for r in rows:
            self.play(Create(r[1][0]), FadeIn(r[1][1], shift=RIGHT * 0.18), run_time=1.15)
        self.wait(1.2)
        self.play(FadeIn(yes, shift=UP * 0.15), run_time=1.2)
        self.play(FadeIn(no, shift=UP * 0.15), run_time=1.2)
        self.wait(1.4)

        point = spark("Excited about the right thing")
        self.play(Write(point), run_time=1.9)
        self.wait(8.47)
