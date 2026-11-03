"""Manim beats for the reel `hope-nested-learning`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: Behrouz, Razaviyayn, Zhong, Mirrokni -- "Nested Learning: The Illusion
of Deep Learning Architectures", NeurIPS 2025 (arXiv 2512.24695), and Google
Research's announcement of it.

Every figure was read out of the paper's own tables by extracting the PDF text
(Table 1, Table 2, Table 6). A web summary of the 1.3B row disagreed with the
paper and was discarded -- see FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over nine previous reels:
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
    DOWN, LEFT, RIGHT, UP, Create, DashedLine, FadeIn, Line, RoundedRectangle,
    Scene, Text, VGroup, Write,
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


def vbar(height, label, figure, color, width=1.15, fig_fs=34):
    """A vertical bordered bar with its figure above and its label below.
    Label and figure are composed INTO the group, never positioned after fit."""
    b = RoundedRectangle(width=width, height=max(height, 0.12), corner_radius=0.07,
                         stroke_width=2.0, stroke_color=color, fill_opacity=0)
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    l = Text(label, font=MONO, font_size=17, color=INK_SOFT)
    return VGroup(f, b, l).arrange(DOWN, buff=0.18)


def hbar(length, label, figure, color, height=0.44, fig_fs=24):
    """A horizontal bordered bar: label on the left, figure on the right."""
    l = Text(label, font=MONO, font_size=18, color=INK_SOFT)
    b = RoundedRectangle(width=max(length, 0.14), height=height, corner_radius=0.07,
                         stroke_width=2.0, stroke_color=color, fill_opacity=0)
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    return VGroup(l, b, f).arrange(RIGHT, buff=0.26)


class B01_LevelsNotLayers(Scene):
    """BLUF: not a training method; and the axis is levels, not depth."""

    def construct(self):
        page(self)
        head = kicker("WHAT IT IS, AND WHAT IT IS NOT",
                      "HOPE is an architecture \u2014 not a training technique")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        layers = VGroup(*[
            RoundedRectangle(width=2.5, height=0.30, corner_radius=0.06,
                             stroke_width=1.8, stroke_color=INK_SOFT, fill_opacity=0)
            for _ in range(5)]).arrange(DOWN, buff=0.16)
        lcap = Text("more layers", font=MONO, font_size=19, color=INK_SOFT)
        left = VGroup(layers, lcap).arrange(DOWN, buff=0.30)

        rates = [("fast", 2.6), ("", 2.1), ("", 1.6), ("slow", 1.1)]
        bands = VGroup(*[
            RoundedRectangle(width=2.5, height=0.30, corner_radius=0.06,
                             stroke_width=sw, stroke_color=TERRA if i == 0 else INK,
                             fill_opacity=0)
            for i, (_, sw) in enumerate(rates)]).arrange(DOWN, buff=0.22)
        rcap = Text("levels, each on its own clock", font=MONO, font_size=19, color=INK)
        right = VGroup(bands, rcap).arrange(DOWN, buff=0.30)

        link = Line(LEFT * 0.7, RIGHT * 0.7, stroke_width=1.8, color=INK_SOFT)
        strike = Line(DOWN * 0.34, UP * 0.34, stroke_width=5.0, color=TERRA)
        pair = VGroup(left, link, right).arrange(RIGHT, buff=0.55)
        strike.move_to(link.get_center())
        body = fit(VGroup(pair, strike))

        self.play(*[Create(b) for b in layers], run_time=1.5)
        self.play(FadeIn(lcap), run_time=0.7)
        self.wait(1.4)
        self.play(Create(link), run_time=0.7)
        self.play(Create(strike), run_time=1.0)
        self.play(*[Create(b) for b in bands], run_time=1.6)
        self.play(FadeIn(rcap), run_time=0.9)
        self.wait(2.0)

        point = spark("Depth was never the axis")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(4.0)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before any evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CONTINUAL-LEARNING CLAIM",
                      "ask these of the paper, not of the press release")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT UPDATES,\n   AND HOW OFTEN?", ["name the parts", "and their rates"],
                  accent=INK_SOFT),
            panel("2  BEATEN\n   AGAINST WHAT?", ["the comparison class", "is where the claim",
                                                   "actually lives"], accent=TERRA),
            panel("3  DID THE AUTHORS\n   SAY IT'S SOLVED?", ["the limitations section",
                                                              "usually answers this"],
                  accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.44, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.6)
            self.wait(1.0)
        self.wait(2.4)

        point = spark("Question two decides this one")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(3.4)


class B03_ContinuumMemory(Scene):
    """QUESTION 1: two memory speeds replaced by a spectrum of clocks."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 WHAT UPDATES, AND HOW OFTEN?",
                      "the continuum memory system")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        old = VGroup(
            panel("weights", ["never, after training"], accent=INK_SOFT, min_w=3.9, fs=18,
                  title_fs=21),
            panel("attention", ["this context only"], accent=INK_SOFT, min_w=3.9, fs=18,
                  title_fs=21),
        ).arrange(DOWN, buff=0.34)
        ocap = Text("two speeds", font=MONO, font_size=19, color=INK_SOFT)
        left = VGroup(old, ocap).arrange(DOWN, buff=0.32)

        levels = [("level 1", "every step", TERRA),
                  ("level 2", "every few", INK),
                  ("level 3", "rarely", INK),
                  ("level 4", "rarest", INK_SOFT)]
        rows = []
        for name, rate, colour in levels:
            n = Text(name, font=MONO, font_size=18, color=colour)
            box = RoundedRectangle(width=1.5, height=0.34, corner_radius=0.07,
                                   stroke_width=2.0, stroke_color=colour, fill_opacity=0)
            r = Text(rate, font=MONO, font_size=17, color=INK_SOFT)
            rows.append(VGroup(n, box, r).arrange(RIGHT, buff=0.26))
        stack = VGroup(*rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        rcap = Text("a spectrum, and the update rule is learned",
                    font=MONO, font_size=18, color=INK)
        right = VGroup(stack, rcap).arrange(DOWN, buff=0.32)

        # The two columns are top-aligned, but the connector must sit at the
        # VERTICAL CENTRE of the pair. Putting it inside the same arrange()
        # top-aligns it too and it reads as a stray mark floating above.
        pair = VGroup(left, right).arrange(RIGHT, buff=1.70, aligned_edge=UP)
        link = Line(LEFT * 0.55, RIGHT * 0.55, stroke_width=1.8, color=INK_SOFT)
        link.move_to([(left.get_right()[0] + right.get_left()[0]) / 2,
                      pair.get_center()[1], 0])
        body = fit_src(VGroup(pair, link))
        src = source_line("Nested Learning \u00b7 Behrouz et al. \u00b7 NeurIPS 2025 \u00b7 CMS, \u00a77")

        self.play(Create(old[0][0]), FadeIn(old[0][1]), run_time=1.3)
        self.play(Create(old[1][0]), FadeIn(old[1][1]), run_time=1.3)
        self.play(FadeIn(ocap), run_time=0.7)
        self.wait(1.6)
        self.play(Create(link), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r[0]), Create(r[1]), FadeIn(r[2]), run_time=0.95)
        self.play(FadeIn(rcap), run_time=1.1)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Fast memory and slow memory, on purpose")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(5.0)


class B04_TheNumbers(Scene):
    """the headline comparison, Table 2, 1.3B params / 100B tokens."""

    def construct(self):
        page(self)
        head = kicker("THE NUMBERS", "1.3B params \u00b7 100B tokens \u00b7 Table 2")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # WikiText perplexity: lower is better, so the bar is drawn SHORTER for
        # the better model and the group is labelled as inverted.
        ppl = VGroup(
            vbar(1.05, "Hope", "14.39", TERRA),
            vbar(1.30, "Titans", "15.60", INK),
            vbar(1.80, "Transformer++", "17.92", INK_SOFT),
        ).arrange(RIGHT, buff=0.34, aligned_edge=DOWN)
        ppl_t = Text("WIKITEXT PERPLEXITY", font=SANS, font_size=21, color=INK_SOFT)
        ppl_s = Text("shorter is better", font=MONO, font_size=17, color=INK_SOFT)
        gl = VGroup(ppl_t, ppl, ppl_s).arrange(DOWN, buff=0.26)

        acc = VGroup(
            vbar(1.80, "Hope", "51.0", TERRA),
            vbar(1.66, "Titans", "49.1", INK),
            vbar(1.28, "Transformer++", "42.6", INK_SOFT),
        ).arrange(RIGHT, buff=0.34, aligned_edge=DOWN)
        acc_t = Text("LAMBADA ACCURACY", font=SANS, font_size=21, color=INK_SOFT)
        acc_s = Text("taller is better", font=MONO, font_size=17, color=INK_SOFT)
        gr = VGroup(acc_t, acc, acc_s).arrange(DOWN, buff=0.26)

        body = fit_src(VGroup(gl, gr).arrange(RIGHT, buff=0.85, aligned_edge=DOWN))
        src = source_line("Behrouz et al., NeurIPS 2025 \u00b7 Table 2 \u00b7 arXiv 2512.24695")

        self.play(FadeIn(ppl_t), run_time=0.7)
        for b in ppl:
            self.play(Create(b[1]), FadeIn(b[0]), FadeIn(b[2]), run_time=0.95)
        self.play(FadeIn(ppl_s), run_time=0.6)
        self.wait(1.1)
        self.play(FadeIn(acc_t), run_time=0.7)
        for b in acc:
            self.play(Create(b[1]), FadeIn(b[0]), FadeIn(b[2]), run_time=0.95)
        self.play(FadeIn(acc_s), run_time=0.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.4)

        point = spark("Real gains. Narrow ones.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.3)


class B05_Ablation(Scene):
    """does the new part carry its weight? Table 6, remove the CMS."""

    def construct(self):
        page(self)
        head = kicker("IS THE MEMORY SPECTRUM DOING THE WORK?",
                      "the ablation \u2014 remove CMS, keep everything else")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        full = panel("Hope", ["avg perplexity   12.24",
                              "reasoning acc    58.1"], accent=INK, min_w=5.2)
        cut = panel("w/o CMS", ["avg perplexity   13.04",
                                "reasoning acc    57.3"], accent=TERRA, min_w=5.2)
        deltas = VGroup(chip("+0.80 ppl", TERRA, font_size=17),
                        chip("\u22120.8 acc", TERRA, font_size=17)).arrange(DOWN, buff=0.26)
        body = fit_src(VGroup(full, deltas, cut).arrange(RIGHT, buff=0.46))
        src = source_line("same paper \u00b7 Table 6 \u00b7 average over the LM tasks, not WikiText alone")

        self.play(Create(full[0]), FadeIn(full[1]), run_time=1.5)
        self.wait(2.0)
        self.play(Create(cut[0]), FadeIn(cut[1]), run_time=1.5)
        self.wait(1.8)
        for d in deltas:
            self.play(Create(d[0]), FadeIn(d[1]), run_time=0.9)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Load-bearing. By less than a point.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.4)


class B06_BaselineRow(Scene):
    """FALSIFIABILITY: question 2. On the hardest retrieval test, attention wins."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 BEATEN AGAINST WHAT?",
                      "S-NIAH-3 \u00b7 find a UUID in 16K tokens \u00b7 Table 1")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = [
            hbar(0.18, "DLA", "4.0", INK_SOFT),
            hbar(0.26, "RWKV-7", "5.8", INK_SOFT),
            hbar(0.95, "Titans", "21.2", INK),
            hbar(1.11, "Hope", "24.8", TERRA),
            hbar(1.83, "Transformer", "40.8", INK),
        ]
        stack = VGroup(*rows).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        quote = Text("\u201ccomparing with other attention-free models, Hope achieves "
                     "the best performance\u201d",
                     font=SANS, font_size=21, color=INK)
        attrib = Text("\u2014 the paper, \u00a79.2", font=MONO, font_size=17, color=INK_SOFT)
        body = fit_src(VGroup(stack, quote, attrib).arrange(DOWN, buff=0.30))
        src = source_line("Behrouz et al., NeurIPS 2025 \u00b7 Table 1, S-NIAH-3 at 16K context")

        for r in rows[:4]:
            self.play(Create(r[1]), FadeIn(r[0]), FadeIn(r[2]), run_time=1.15)
            self.wait(0.25)
        self.wait(2.2)
        self.play(Create(rows[4][1]), FadeIn(rows[4][0]), FadeIn(rows[4][2]), run_time=1.9)
        self.wait(2.6)
        self.play(Write(quote), run_time=3.2)
        self.play(FadeIn(attrib), FadeIn(src), run_time=1.0)
        self.wait(3.0)

        point = spark("It wins its class. Attention wins the task.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.6)


class B07_MoreLevelsLessForgetting(Scene):
    """the result that is the point: CTNL, and the dose-response on levels."""

    def construct(self):
        page(self)
        head = kicker("WHAT IT IS ACTUALLY FOR",
                      "learn one new language, then a second, then translate the first")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # Stage one: the task itself, so the bars below mean something when
        # they land. Three steps, then the question.
        task = [chip("learn language A", INK_SOFT, font_size=18, height=0.44, pad=0.40),
                chip("then language B", INK_SOFT, font_size=18, height=0.44, pad=0.40),
                chip("now translate A", TERRA, font_size=18, height=0.44, pad=0.40)]
        arrows = [Line(LEFT * 0.16, RIGHT * 0.16, stroke_width=1.6, color=INK_SOFT)
                  for _ in range(2)]
        trow = VGroup(task[0], arrows[0], task[1], arrows[1], task[2]).arrange(RIGHT, buff=0.18)

        bars = VGroup(
            vbar(0.70, "ICL", "collapses", INK_SOFT, fig_fs=21),
            vbar(1.25, "Hope-1", "+1 level", INK, fig_fs=21),
            vbar(1.70, "Hope-2", "+2 levels", INK, fig_fs=21),
            vbar(2.20, "Hope-3", "+3 levels", TERRA, fig_fs=21),
        ).arrange(RIGHT, buff=0.46, aligned_edge=DOWN)

        base = DashedLine(LEFT * 4.1, RIGHT * 4.1, stroke_width=2.0,
                          color=INK_SOFT, dash_length=0.12)
        bcap = Text("score with no second language to forget",
                    font=MONO, font_size=18, color=INK_SOFT)
        head_pair = VGroup(bcap, base).arrange(DOWN, buff=0.14)

        # The paper reports CTNL as a two-axis ChRF scatter, not one score per
        # model. These bars show the ORDERING the paper states and carry no
        # numbers -- the caption says so, on screen, rather than in a footnote.
        scale_note = Text("ordering as reported \u2014 axis not to scale",
                          font=MONO, font_size=17, color=INK_SOFT)
        body = fit_src(VGroup(trow, head_pair, bars, scale_note).arrange(DOWN, buff=0.30))
        src = source_line("same paper \u00b7 Continual Translation of a Novel Language \u00b7 Table 8")

        for t in task:
            self.play(Create(t[0]), FadeIn(t[1]), run_time=1.0)
        self.play(*[Create(a) for a in arrows], run_time=0.7)
        self.wait(1.4)
        self.play(Create(base), FadeIn(bcap), run_time=1.5)
        self.wait(1.1)
        for b in bars:
            self.play(Create(b[1]), FadeIn(b[2]), FadeIn(b[0]), run_time=1.35)
            self.wait(0.7)
        self.play(FadeIn(scale_note), FadeIn(src), run_time=1.1)
        self.wait(2.4)

        point = spark("More levels, less forgetting")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.2)


class B08_Verdict(Scene):
    """QUESTION 3: the authors' own limitation, then the two-sided verdict."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 DID THE AUTHORS SAY IT'S SOLVED?",
                      "page 40, in their words: no")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("WHAT UPDATES", "a spectrum of blocks, own clocks", INK),
              ("AGAINST WHAT", "attention-free models only", TERRA),
              ("SOLVED?", "the authors say no", TERRA)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=22, color=INK_SOFT)
            ch = chip(answer, colour, font_size=18)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.34))
        scored = VGroup(*qrows).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  levels and update rates as a design axis",
                 font=SANS, font_size=23, color=INK),
            Text("BE SCEPTICAL OF:  \u201cthis fixes AI memory\u201d",
                 font=SANS, font_size=23, color=TERRA),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        body = fit_src(VGroup(scored, verdict).arrange(DOWN, buff=0.52, aligned_edge=LEFT))
        src = source_line("\u201ccatastrophic forgetting is not \u2018solved\u2019 in general\u201d "
                          "\u00b7 a roadmap rather than a destination")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.3)
            self.wait(0.6)
        self.wait(1.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.0)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=1.5)
            self.wait(0.8)

        point = spark("The people who built it wrote the opposite")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(5.2)
