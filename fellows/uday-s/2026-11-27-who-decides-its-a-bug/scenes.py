"""Manim beats for the reel `who-decides-its-a-bug`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Commissioned topic: "Implications/Advantages of using AI as a Beta Tester for
games and other kinds of software", retitled.

THREE primary sources, each read directly and quoted verbatim (see SOURCES.md):
  * the OSS-Fuzz README -- figures carry their "as of May 2025" qualifier
  * the OSS-Fuzz-Gen README -- 30 reported bugs; the four grading metrics
  * Meta's TestGen-LLM paper, arXiv:2402.09171 (FSE'24) -- the oracle sentence

The reel is organised as three oracle regimes: FREE (a crash decides), WRITABLE
(a spec decides, with a human at the end), and ABSENT (nobody can write the
predicate -- most of what game beta testing is for).

Two things the reel refuses to do, both of which are the easy error here:
  * calling classical fuzzing "AI". B03 states the opposite on screen.
  * claiming the crash is the sole oracle in OSS-Fuzz-Gen. Its README never says
    how a bug is adjudicated, so B04 claims only the documented grading metrics.

The November 2024 Google Security Blog figures are NOT used anywhere: the page
returned only its chrome, so it could not be read at the source.

NO LaTeX anywhere (dvisvgm absent).

Layout, per the rule this series converged on. GATE V scores `cover` as the ink
BOUNDING BOX over the safe area, so:
  * the fitted body must FILL its band -- fit_src() centres the group in a
    4.2-unit band, and a group much wider than ~2.9:1 comes back height-starved
    with dead bands top and bottom. Keep panel lines short.
  * the citation strip is the lowest element on the frame, so it lands by ~45%
    of each beat or the midpoint QC frame reads as half-empty.
  * faint ink drags the contrast metric down; one accent colour, the rest INK.

Other rules that still hold:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * compose every label INTO the fitted group before fitting -- positioning a
    closing line with to_edge() lands it on top of the body
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
"""
import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, Line, RoundedRectangle, Scene, Text,
    VGroup,
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


def tick(color=INK):
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def crossmark(color=TERRA):
    """Sits BESIDE or BETWEEN. Never drawn through text."""
    return VGroup(
        Line([-0.10, 0.10, 0], [0.10, -0.10, 0], stroke_width=3.2, color=color),
        Line([-0.10, -0.10, 0], [0.10, 0.10, 0], stroke_width=3.2, color=color),
    )


def hollow(size=0.24, color=INK_SOFT, stroke=1.8):
    return RoundedRectangle(width=size, height=size, corner_radius=0.04,
                            stroke_width=stroke, stroke_color=color, fill_opacity=0)


def chip(label, color, font_size=19, pad=0.32, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(box, t)


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=20, title_fs=24):
    lines = [l for l in lines if l.strip()]
    t = Text(title, font=SANS, font_size=title_fs, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


def stat(figure, caption_lines, accent=INK, fig_fs=50, cap_fs=18, min_w=3.8):
    f = Text(figure, font=SERIF, font_size=fig_fs, color=accent)
    caps = VGroup(*[Text(c, font=MONO, font_size=cap_fs, color=INK_SOFT)
                    for c in caption_lines])
    caps.arrange(DOWN, buff=0.14)
    inner = VGroup(f, caps).arrange(DOWN, buff=0.22)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.6),
                           height=inner.height + 0.56, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)



def tickrow(text, color=INK, fs=20):
    return VGroup(tick(color), Text(text, font=MONO, font_size=fs, color=INK)).arrange(
        RIGHT, buff=0.26)


def connector(height=0.32):
    return Line([0, 0, 0], [0, -height, 0], stroke_width=1.6, color=INK_SOFT)


def barset(data, maxw=6.4, fs=20, bh=0.46, gap=0.26):
    """data = [(label, fraction_of_longest, value_text, colour)].

    Bars encode the stated percentages proportionally and nothing else; every
    bar carries its own r in the value text, so the bar is never the only
    evidence on screen.
    """
    labs = [Text(d[0], font=MONO, font_size=fs, color=INK) for d in data]
    vals = [Text(d[2], font=MONO, font_size=fs, color=d[3]) for d in data]
    labw = max(l.width for l in labs)
    valw = max(v.width for v in vals)

    # Build CENTRED on the origin. Laying the rows out from x=0 rightward puts
    # explicit coordinates outside the frame before fit_src() recentres the
    # group, which GATE A rejects -- correctly, since nothing guarantees the
    # recentring happens.
    total = labw + 0.40 + maxw + 0.40 + valw
    x0 = -total / 2.0
    x_bar = x0 + labw + 0.40
    x_val = x_bar + maxw + 0.40
    y0 = (len(data) - 1) * (bh + gap) / 2.0

    rows = VGroup()
    tracks = VGroup()
    for i, ((name, frac, vtext, color), lab, val) in enumerate(zip(data, labs, vals)):
        y = y0 - i * (bh + gap)
        track = RoundedRectangle(width=maxw, height=bh, corner_radius=0.08,
                                 stroke_width=1.5, stroke_color=INK_SOFT,
                                 stroke_opacity=0.70, fill_opacity=0)
        track.move_to([x_bar + maxw / 2.0, y, 0])
        tracks.add(track)
        bar = RoundedRectangle(width=max(0.34, maxw * frac), height=bh,
                               corner_radius=0.08, stroke_width=2.8,
                               stroke_color=color, fill_opacity=0.34, fill_color=color)
        lab.move_to([x0 + labw - lab.width / 2.0, y, 0])
        bar.move_to([x_bar + bar.width / 2.0, y, 0])
        val.move_to([x_val + val.width / 2.0, y, 0])
        rows.add(VGroup(lab, bar, val))
    return rows, tracks



def boxed(rows, accent=INK, pad_x=0.8, pad_y=0.7):
    box = RoundedRectangle(width=rows.width + pad_x, height=rows.height + pad_y,
                           corner_radius=0.12, stroke_width=1.8,
                           stroke_color=accent, fill_opacity=0)
    box.move_to(rows.get_center())
    return VGroup(box, rows)


class B01_FourJobs(Scene):
    """BLUF: a beta tester does four jobs, not one. 19.63s."""

    def construct(self):
        page(self)
        head = kicker("WHAT A BETA TESTER ACTUALLY DOES",
                      "four jobs · automation is not evenly good at them")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        jobs = [
            chip("1   exercise it in ways nobody designed for", INK,
                 font_size=24, pad=0.46, height=0.60),
            chip("2   notice that something is wrong", TERRA,
                 font_size=24, pad=0.46, height=0.60),
            chip("3   judge whether it matters", INK, font_size=24, pad=0.46, height=0.60),
            chip("4   write it down so someone can reproduce it", INK,
                 font_size=24, pad=0.46, height=0.60),
        ]
        mark = chip("this one has a name in the literature", TERRA,
                    font_size=21, pad=0.40, height=0.52)
        line = Text("four jobs, not one — and the argument lives in the second",
                    font=SANS, font_size=24, color=INK)
        body = fit_src(VGroup(VGroup(*jobs).arrange(DOWN, buff=0.22),
                              mark, line).arrange(DOWN, buff=0.34))
        src = source_line("the oracle problem · named in the testing literature")

        for j in jobs:
            self.play(Create(j[0]), FadeIn(j[1]), run_time=1.0)
            self.wait(0.5)
        self.play(Create(mark[0]), FadeIn(mark[1]), run_time=1.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(2.6)
        self.play(FadeIn(line), run_time=1.4)
        self.wait(2.9)

        point = spark("Automation is good at one of these")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(1.93)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before any figure. 19.65s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY TESTING TOOL",
                      "ask these before you believe a dashboard")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT IS\n   THE ORACLE?", ["what decides the", "output is WRONG,",
                                                 "not merely surprising"], accent=TERRA),
            panel("2  WHAT HAPPENS TO\n   A FAILURE IT\n   CANNOT JUDGE?", ["escalated,",
                                                                            "or quietly dropped"],
                  accent=INK_SOFT),
            panel("3  WHO PAYS FOR A\n   FALSE POSITIVE?", ["somebody always does —", "usually an engineer's",
                                                            "afternoon"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in row:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=2.2)
            self.wait(1.6)

        point = spark("The first one decides the other two")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.35)


class B03_FreeOracle(Scene):
    """EVIDENCE: the free oracle, its scale, and an honest label. 32.34s."""

    def construct(self):
        page(self)
        head = kicker("CASE 1 — THE ORACLE IS FREE",
                      "if it crashed, nobody has to judge anything")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        oracle = panel("the oracle", ["did it crash?"], accent=INK, min_w=3.8, fs=22, title_fs=23)
        figs = VGroup(
            stat("13,000+", ["vulnerabilities"], accent=TERRA, fig_fs=38, cap_fs=17, min_w=3.4),
            stat("50,000", ["bugs"], accent=INK, fig_fs=38, cap_fs=17, min_w=3.4),
            stat("1,000", ["projects"], accent=INK, fig_fs=38, cap_fs=17, min_w=3.4),
        ).arrange(DOWN, buff=0.22)
        pair = VGroup(oracle, figs).arrange(RIGHT, buff=0.46)

        notai = chip("classical fuzzing is not AI — it is a loop with a free oracle", TERRA,
                     font_size=21, pad=0.40, height=0.52)
        body = fit_src(VGroup(pair, notai).arrange(DOWN, buff=0.38))
        src = source_line("OSS-Fuzz README, \"as of May 2025\" · \"helped identify and fix\"")

        self.play(Create(oracle[0]), FadeIn(oracle[1]), run_time=2.0)
        self.wait(1.2)
        for f in figs:
            self.play(Create(f[0]), FadeIn(f[1]), run_time=1.8)
            self.wait(1.6)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(2.4)
        self.play(Create(notai[0]), FadeIn(notai[1]), run_time=2.4)
        self.wait(8.2)

        point = spark("A crash needs no judgement")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.04)


class B04_WhereAIEnters(Scene):
    """EVIDENCE: the LLM writes the probe, not the verdict. 32.76s."""

    def construct(self):
        page(self)
        head = kicker("CASE 2 — WHERE THE MODEL ACTUALLY GOES",
                      "it writes the probe · the crash still returns the verdict")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        s1 = chip("the LLM writes the fuzz target", TERRA, font_size=22, pad=0.44, height=0.58)
        a1 = Text("→", font=SERIF, font_size=34, color=INK_SOFT)
        s2 = chip("the target runs", INK, font_size=22, pad=0.44, height=0.58)
        a2 = Text("→", font=SERIF, font_size=34, color=INK_SOFT)
        s3 = chip("the crash decides", INK, font_size=22, pad=0.44, height=0.58)
        flow = VGroup(s1, a1, s2, a2, s3).arrange(RIGHT, buff=0.26)

        metrics = panel("how the framework grades a generated target", [
            "compilability",
            "runtime crashes",
            "runtime coverage, and the line-coverage diff",
            "against the existing human-written targets",
        ], accent=INK, min_w=8.0, fs=19, title_fs=22)

        count = chip("30 new bugs/vulnerabilities reported · 2 still pending triage", TERRA,
                     font_size=21, pad=0.40, height=0.52)

        body = fit_src(VGroup(flow, metrics, count).arrange(DOWN, buff=0.34))
        src = source_line("OSS-Fuzz-Gen README · repository archived 10 Nov 2026")

        self.play(Create(s1[0]), FadeIn(s1[1]), run_time=1.4)
        self.play(FadeIn(a1), run_time=0.5)
        self.play(Create(s2[0]), FadeIn(s2[1]), run_time=1.4)
        self.play(FadeIn(a2), run_time=0.5)
        self.play(Create(s3[0]), FadeIn(s3[1]), run_time=1.6)
        self.wait(1.6)
        self.play(Create(metrics[0]), FadeIn(metrics[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(3.0)
        self.play(Create(count[0]), FadeIn(count[1]), run_time=2.0)
        self.wait(12.0)

        point = spark("Reach, not judgement")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.46)


class B05_TheOracleProblem(Scene):
    """HERO: the paper's own sentence, and what it implies. 32.85s."""

    def construct(self):
        page(self)
        head = kicker("CASE 3 — THE ORACLE HAS TO BE WRITTEN",
                      "Meta shipped this, published it, and said so plainly")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        quote = panel("from the paper, verbatim", [
            "\"Without an automatable test oracle,",
            "TestGen-LLM cannot automatically determine",
            "whether a failing test has found a bug,",
            "or whether it merely contains an",
            "incorrect test assertion.\"",
        ], accent=INK, min_w=8.6, fs=20, title_fs=22)
        attrib = Text("— Automated Unit Test Improvement using LLMs at Meta, §2",
                      font=MONO, font_size=18, color=INK_SOFT)

        f1 = chip("a test fails", INK, font_size=21, pad=0.40, height=0.52)
        fa = Text("→", font=SERIF, font_size=30, color=INK_SOFT)
        f2 = chip("bug, or bad assertion?", INK, font_size=21, pad=0.40, height=0.52)
        fb = Text("→", font=SERIF, font_size=30, color=INK_SOFT)
        f3 = chip("cannot tell — discarded", TERRA, font_size=21, pad=0.40, height=0.52)
        flow = VGroup(f1, fa, f2, fb, f3).arrange(RIGHT, buff=0.24)

        body = fit_src(VGroup(quote, attrib, flow).arrange(DOWN, buff=0.32))
        src = source_line("arXiv:2402.09171 · FSE 2024 industry track")

        self.play(Create(quote[0]), run_time=1.4)
        self.play(FadeIn(quote[1]), run_time=3.4)
        self.play(FadeIn(attrib), run_time=1.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(4.0)
        for f in (f1, fa, f2, fb, f3):
            self.play(FadeIn(f), run_time=0.8)
        self.wait(12.2)

        point = spark("It throws the failures away")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.55)


class B06_TheFunnel(Scene):
    """EVIDENCE: what it does deliver, and who stands at the end. 32.14s."""

    def construct(self):
        page(self)
        head = kicker("WHAT IT DOES DELIVER",
                      "Meta's offline evaluation on Instagram Reels and Stories")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        data = [
            ("built correctly", 75 / 75.0, "75%", INK),
            ("passed reliably", 57 / 75.0, "57%", INK),
            ("increased coverage", 25 / 75.0, "25%", TERRA),
        ]
        bars, tracks = barset(data, maxw=5.6)

        deployed = panel("deployed across Instagram and Facebook", [
            "196 of 1,979 test classes improved  (about 10%)",
            "73% of its improvements accepted by engineers",
        ], accent=INK, min_w=8.4, fs=19, title_fs=22)

        last = chip("the final gate is a person", TERRA, font_size=21, pad=0.40, height=0.52)

        body = fit_src(VGroup(VGroup(tracks, bars), deployed, last).arrange(DOWN, buff=0.32))
        src = source_line("arXiv:2402.09171 · abstract and §4")

        self.play(Create(tracks), run_time=0.8)
        for r in bars:
            self.play(FadeIn(r[0]), Create(r[1]), FadeIn(r[2]), run_time=1.5)
            self.wait(1.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(2.0)
        self.play(Create(deployed[0]), FadeIn(deployed[1]), run_time=2.4)
        self.wait(2.0)
        self.play(Create(last[0]), FadeIn(last[1]), run_time=2.0)
        self.wait(9.1)

        point = spark("It narrows at every step")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(1.84)


class B07_SourceProblems(Scene):
    """FALSIFIABILITY: three problems in my own sources. 41.89s."""

    def construct(self):
        page(self)
        head = kicker("CHECKING MY OWN SOURCES",
                      "all three had a problem · one cuts the headline figure")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        p1 = panel("1  the abstract and the body disagree", [
            "abstract: 11.5% of classes improved",
            "body §4: 196 of 1,979  =  9.9%, \"approximately 10%\"",
        ], accent=TERRA, min_w=9.0, fs=19, title_fs=22)
        p2 = panel("2  the denominator moves", [
            "abstract: 75% of test CASES built",
            "§3.3: 75% of test CLASSES had at least one that built",
        ], accent=TERRA, min_w=9.0, fs=19, title_fs=22)
        p3 = panel("3  two official pages, two totals", [
            "README:    13,000 / 50,000   as of May 2025",
            "docs site: 10,000 / 36,000   as of August 2023",
        ], accent=TERRA, min_w=9.0, fs=19, title_fs=22)

        body = fit_src(VGroup(p1, p2, p3).arrange(DOWN, buff=0.30))
        src = source_line("I used 10%, the measured denominator, and the dated figure")

        self.play(Create(p1[0]), FadeIn(p1[1]), run_time=2.6)
        self.wait(2.4)
        self.play(FadeIn(src), run_time=1.0)
        self.play(Create(p2[0]), FadeIn(p2[1]), run_time=2.6)
        self.wait(2.6)
        self.play(Create(p3[0]), FadeIn(p3[1]), run_time=2.8)
        self.wait(17.0)

        point = spark("The quoted figure is the abstract's")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.99)


class B08_Verdict(Scene):
    """VERDICT: the rubric scored, the games case, then both sides. 35.43s."""

    def construct(self):
        page(self)
        head = kicker("SCORED",
                      "three oracles, three different answers")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup(
            tickrow("a crash — free, and it scales enormously"),
            tickrow("a specification — writable, with a human at the end"),
            tickrow("nothing — is this level fun? is this curve cruel?"),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        good = panel("BE EXCITED", ["the crash-hunting half is",
                                    "being industrialised — and a",
                                    "model writing probes found",
                                    "bugs in hard-fuzzed code"],
                     accent=INK, min_w=5.4, fs=19, title_fs=23)
        bad = panel("BE SCEPTICAL", ["of anyone selling AI beta",
                                     "testing who will not tell you",
                                     "what their oracle is — that",
                                     "answer decides everything"],
                    accent=TERRA, min_w=5.4, fs=19, title_fs=23)
        pair = VGroup(good, bad).arrange(RIGHT, buff=0.44, aligned_edge=UP)

        body = fit_src(VGroup(rows, pair).arrange(DOWN, buff=0.38))
        src = source_line("for games, the third row is most of the question")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.4)
            self.wait(1.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(3.0)
        self.play(Create(good[0]), FadeIn(good[1]), run_time=2.6)
        self.wait(2.4)
        self.play(Create(bad[0]), FadeIn(bad[1]), run_time=2.6)
        self.wait(11.1)

        point = spark("Ask what the oracle is")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.03)
