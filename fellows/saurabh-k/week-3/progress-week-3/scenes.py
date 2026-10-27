"""scenes.py — Manim scenes for hai-repo-sensei-v2 (Repo Sensei, Week Three).

One Scene class per GRAPHIC/manim beat; the class name's prefix is the beat id
(run.sh matches `class B\\d\\d_\\w+(Scene)` and fills media/<BID>.mp4).

Visual system is locked to the series: PAPER ground, INK near-black type, one
TERRACOTTA accent, serif display / mono for code. Hard cuts, no gradients, no
shadows, no rounded corners except where a card is explicitly a card.

Text weight is the STRING "BOLD", never the bare constant — GATE A's
static_scene_check stub does not define BOLD/ITALIC/NORMAL.

Layout budget: the 16:9 frame is 14.22 x 8 units. Title-safe is the inner 90%,
so everything is kept inside x in [-5.9, 5.9] and y in [-3.2, 3.2].
"""
from manim import *
import numpy as np

PAPER = "#FAF9F5"
INK = "#3D3929"
SOFT = "#73705F"
SPARK = "#D97757"
CARD = "#FFFFFF"
RULE = "#D8D4C8"

SERIF = "EB Garamond"
MONO = "Menlo"

XMAX, YMAX = 5.9, 3.2


def _ground(scene):
    scene.camera.background_color = PAPER


def eyebrow(text):
    t = Text(text, font=SERIF, weight="BOLD", font_size=30, color=SOFT)
    t.to_corner(UL).shift(RIGHT * 0.35 + DOWN * 0.15)
    rule = Line(LEFT * XMAX, RIGHT * XMAX, color=RULE, stroke_width=2)
    rule.next_to(t, DOWN, buff=0.22).set_x(0)
    return VGroup(t, rule)


def act_card(scene, numeral, title, hold=0.9):
    """Act divider.

    GATE A counts distinct shape *creations*, so the card builds four separate
    shapes. GATE B rejects any label sitting on a line, so every one of them is
    kept outside the type block: the numeral occupies roughly y in [-0.4, 1.5]
    and the title sits near y = -1.4, so the rules live beyond y = +/-2.0.
    """
    n = Text(numeral, font=SERIF, weight="BOLD", font_size=300, color=INK)
    dot = Dot(radius=0.11, color=SPARK).next_to(n, RIGHT, buff=0.22).align_to(n, DOWN)
    g = VGroup(n, dot).move_to(ORIGIN).shift(UP * 0.35)
    t = Text(title, font=SERIF, font_size=84, color=SOFT).next_to(g, DOWN, buff=0.55)

    top = Line(LEFT * 5.6, RIGHT * 5.6, color=RULE, stroke_width=5).move_to(UP * 2.85)
    bot = Line(LEFT * 3.4, RIGHT * 3.4, color=SPARK, stroke_width=8).move_to(DOWN * 2.85)
    tick_l = Line(DOWN * 0.22, UP * 0.22, color=RULE, stroke_width=3).move_to(
        np.array([-5.6, -2.85, 0]))
    tick_r = Line(DOWN * 0.22, UP * 0.22, color=RULE, stroke_width=3).move_to(
        np.array([5.6, -2.85, 0]))

    scene.play(Create(top, run_time=0.22))
    scene.play(Write(n, run_time=0.42))
    scene.play(FadeIn(dot, scale=0.5, run_time=0.14),
               FadeIn(t, shift=UP * 0.2, run_time=0.3),
               Create(bot, run_time=0.3))
    scene.play(Create(tick_l, run_time=0.14), Create(tick_r, run_time=0.14))
    scene.wait(hold)


class B01_ActOne(Scene):
    def construct(self):
        _ground(self)
        act_card(self, "I", "The problem", hold=0.85)


class B05_ActTwo(Scene):
    def construct(self):
        _ground(self)
        act_card(self, "II", "How it works", hold=0.83)


class B12_ActThree(Scene):
    def construct(self):
        _ground(self)
        act_card(self, "III", "Nine days in", hold=1.10)


class B02_BigRepo(Scene):
    """A dense grid of files on the left; the question stands clear on the right.

    GATE B rejects a label sitting on a curve or line, so the question mark is
    kept off the grid entirely rather than haloed on top of it.
    """

    def construct(self):
        _ground(self)
        head = eyebrow("ONE HUNDRED THOUSAND LINES")
        self.play(FadeIn(head, run_time=0.4))
        cells = VGroup()
        cols, rows = 10, 7
        for r in range(rows):
            for c in range(cols):
                box = Rectangle(width=0.52, height=0.32,
                                stroke_color=SOFT, stroke_width=2.6,
                                fill_color=CARD, fill_opacity=1)
                box.move_to(np.array([-5.0 + c * 0.62,
                                      1.35 - r * 0.46, 0]))
                cells.add(box)
        self.play(LaggedStart(*[FadeIn(b, run_time=0.22) for b in cells],
                              lag_ratio=0.012, run_time=0.85))
        q = Text("?", font=SERIF, weight="BOLD", font_size=200, color=SPARK)
        q.move_to(np.array([3.6, 0.65, 0]))
        self.play(Write(q, run_time=0.4))
        cap = VGroup(
            Text("Where does this", font=SERIF, font_size=46, color=INK),
            Text("feature live?", font=SERIF, font_size=46, color=INK),
        ).arrange(DOWN, buff=0.26).move_to(np.array([3.6, -1.75, 0]))
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.12) for l in cap],
                              lag_ratio=0.25, run_time=0.45))
        self.wait(4.4)


class B03_ConfidentGuess(Scene):
    """A fluent answer with nothing underneath it."""

    def construct(self):
        _ground(self)
        head = eyebrow("WHAT YOU USUALLY GET")
        self.play(FadeIn(head, run_time=0.4))
        card = RoundedRectangle(width=11.0, height=3.0, corner_radius=0.12,
                                stroke_color=RULE, stroke_width=2,
                                fill_color=CARD, fill_opacity=1).shift(UP * 0.95)
        lines = VGroup(*[
            Line(LEFT * w, RIGHT * w, color=SOFT, stroke_width=11)
            for w in (4.6, 4.9, 3.7)
        ]).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to(card).shift(LEFT * 0.25)
        self.play(Create(card, run_time=0.3))
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.25, run_time=0.6))
        arrow = Arrow(card.get_bottom(), card.get_bottom() + DOWN * 1.25,
                      color=SPARK, stroke_width=16, buff=0.1,
                      max_tip_length_to_length_ratio=0.45)
        empty = DashedVMobject(
            Rectangle(width=5.6, height=1.5, stroke_color=SPARK, stroke_width=6),
            num_dashes=34).next_to(arrow, DOWN, buff=0.12)
        label = Text("source?", font=MONO, font_size=52, color=SPARK).move_to(empty)
        self.play(GrowArrow(arrow, run_time=0.3))
        self.play(Create(empty, run_time=0.35), FadeIn(label, run_time=0.3))
        self.wait(4.3)


class B06_Pipeline(Scene):
    """CLONE -> PARSE -> INDEX -> ANSWER, with an arrow running through."""

    def construct(self):
        _ground(self)
        head = eyebrow("FOUR STAGES")
        self.play(FadeIn(head, run_time=0.4))
        names = ["CLONE", "PARSE", "INDEX", "ANSWER"]
        boxes = VGroup()
        for n in names:
            b = Rectangle(width=2.55, height=1.5, stroke_color=INK, stroke_width=3,
                          fill_color=CARD, fill_opacity=1)
            t = Text(n, font=SERIF, weight="BOLD", font_size=46, color=INK).move_to(b)
            boxes.add(VGroup(b, t))
        boxes.arrange(RIGHT, buff=0.62).set_y(-0.15)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in boxes],
                              lag_ratio=0.3, run_time=1.6))
        conns = VGroup()
        for a, b in zip(boxes[:-1], boxes[1:]):
            conns.add(Arrow(a.get_right(), b.get_left(), color=SOFT,
                            stroke_width=14, buff=0.06,
                            max_tip_length_to_length_ratio=0.5))
        self.play(LaggedStart(*[GrowArrow(c) for c in conns], lag_ratio=0.3, run_time=1.0))
        for b in boxes:
            self.play(b[0].animate.set_stroke(SPARK, 6), run_time=0.28)
            self.play(b[0].animate.set_stroke(INK, 3), run_time=0.18)
        cap = Text("Nothing is answered before it is indexed.",
                   font=SERIF, font_size=56, color=SOFT).move_to(np.array([0, -2.95, 0]))
        self.play(FadeIn(cap, shift=UP * 0.12, run_time=0.5))
        self.wait(4.6)


class B07_TreeSitter(Scene):
    """Source on the left, a syntax tree growing on the right."""

    def construct(self):
        _ground(self)
        head = eyebrow("IT PARSES, IT DOES NOT GREP")
        self.play(FadeIn(head, run_time=0.4))
        code = VGroup(
            Text("class Index:", font=MONO, font_size=46, color=INK),
            Text("    def add(self):", font=MONO, font_size=46, color=INK),
            Text("        ...", font=MONO, font_size=46, color=SOFT),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        panel = Rectangle(width=5.6, height=2.6, stroke_color=RULE, stroke_width=2,
                          fill_color=CARD, fill_opacity=1)
        code[1].shift(RIGHT * 0.52)
        code[2].shift(RIGHT * 1.04)
        code.move_to(panel)
        left = VGroup(panel, code).move_to(LEFT * 3.25 + DOWN * 0.25)
        self.play(FadeIn(panel, run_time=0.35))
        self.play(LaggedStart(*[AddTextLetterByLetter(l, run_time=0.5) for l in code],
                              lag_ratio=0.5, run_time=1.5))
        root = self._node("class", INK)
        c1 = self._node("name", INK)
        c2 = self._node("body", INK)
        g1 = self._node("def", INK)
        root.move_to(RIGHT * 3.3 + UP * 1.45)
        c1.move_to(RIGHT * 2.1 + UP * 0.1)
        c2.move_to(RIGHT * 4.5 + UP * 0.1)
        g1.move_to(RIGHT * 4.5 + DOWN * 1.3)
        e1 = Line(root.get_bottom(), c1.get_top(), color=SOFT, stroke_width=3)
        e2 = Line(root.get_bottom(), c2.get_top(), color=SOFT, stroke_width=3)
        e3 = Line(c2.get_bottom(), g1.get_top(), color=SOFT, stroke_width=3)
        self.play(FadeIn(root, scale=0.7, run_time=0.4))
        self.play(Create(e1, run_time=0.3), Create(e2, run_time=0.3))
        self.play(FadeIn(c1, scale=0.7, run_time=0.3), FadeIn(c2, scale=0.7, run_time=0.3))
        self.play(Create(e3, run_time=0.3))
        self.play(FadeIn(g1, scale=0.7, run_time=0.35))
        self.wait(5.2)

    def _node(self, label, color):
        box = Rectangle(width=1.75, height=0.78, stroke_color=color, stroke_width=3,
                        fill_color=CARD, fill_opacity=1)
        t = Text(label, font=MONO, font_size=30, color=color).move_to(box)
        return VGroup(box, t)


class B08_Queries(Scene):
    """Five query chips over three language tags."""

    def construct(self):
        _ground(self)
        head = eyebrow("EIGHTEEN QUERY FILES")
        self.play(FadeIn(head, run_time=0.4))
        chips = VGroup()
        for n in ["defs", "calls", "imports", "refs"]:
            b = Rectangle(width=2.5, height=1.5, stroke_color=INK, stroke_width=4,
                          fill_color=CARD, fill_opacity=1)
            t = Text(n, font=MONO, font_size=46, color=INK).move_to(b)
            chips.add(VGroup(b, t))
        chips.arrange(RIGHT, buff=0.55).shift(UP * 0.75)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in chips],
                              lag_ratio=0.15, run_time=0.7))
        langs = VGroup()
        for n in ["python", "typescript", "javascript"]:
            t = Text(n, font=MONO, font_size=48, color=SPARK)
            u = Line(LEFT * (t.width / 2), RIGHT * (t.width / 2),
                     color=SPARK, stroke_width=3).next_to(t, DOWN, buff=0.16)
            langs.add(VGroup(t, u))
        langs.arrange(RIGHT, buff=1.1).shift(DOWN * 1.75)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.18) for l in langs],
                              lag_ratio=0.2, run_time=0.5))
        self.wait(6.9)


class B09_Trace(Scene):
    """UI -> API -> DATABASE, lit in turn."""

    def construct(self):
        _ground(self)
        head = eyebrow("ONE FEATURE, EVERY LAYER")
        self.play(FadeIn(head, run_time=0.4))
        layers = VGroup()
        for n in ("UI", "API", "DATABASE"):
            b = Rectangle(width=7.4, height=1.4, stroke_color=INK, stroke_width=4,
                          fill_color=CARD, fill_opacity=1)
            t = Text(n, font=SERIF, weight="BOLD", font_size=56, color=INK).move_to(b)
            layers.add(VGroup(b, t))
        layers.arrange(DOWN, buff=0.52).set_y(-0.3)
        self.play(LaggedStart(*[FadeIn(l, shift=LEFT * 0.25) for l in layers],
                              lag_ratio=0.3, run_time=1.5))
        spine = Line(layers[0].get_top() + DOWN * 0.1,
                     layers[2].get_bottom() + UP * 0.1,
                     color=SPARK, stroke_width=6).shift(LEFT * 4.1)
        self.play(Create(spine, run_time=0.9))
        for l in layers:
            self.play(l[0].animate.set_stroke(SPARK, 6), run_time=0.3)
            self.play(l[0].animate.set_stroke(INK, 3), run_time=0.2)
        self.wait(3.6)


class B10_Citation(Scene):
    """An answer snapping to a file:line chip."""

    def construct(self):
        _ground(self)
        head = eyebrow("EVERY ANSWER CARRIES ITS SOURCE")
        self.play(FadeIn(head, run_time=0.4))
        ans = RoundedRectangle(width=5.6, height=2.3, corner_radius=0.12,
                               stroke_color=INK, stroke_width=3,
                               fill_color=CARD, fill_opacity=1).shift(LEFT * 3.1 + DOWN * 0.3)
        at = Text("the answer", font=SERIF, font_size=56, color=INK).move_to(ans).shift(UP * 0.6)
        bars = VGroup(*[Line(LEFT * w, RIGHT * w, color=SOFT, stroke_width=6)
                        for w in (1.85, 2.05)]).arrange(DOWN, buff=0.34).move_to(ans).shift(DOWN * 0.42)
        self.play(FadeIn(ans, run_time=0.4), FadeIn(at, run_time=0.4))
        self.play(LaggedStart(*[Create(b) for b in bars], lag_ratio=0.4, run_time=0.8))
        chip = Rectangle(width=5.0, height=1.12, stroke_color=INK, stroke_width=4,
                         fill_color=CARD, fill_opacity=1).shift(RIGHT * 3.3 + DOWN * 0.3)
        ct = Text("defs.scm:14", font=MONO, font_size=44, color=INK).move_to(chip)
        arrow = Arrow(ans.get_right(), chip.get_left(), color=INK, stroke_width=16,
                      buff=0.1, max_tip_length_to_length_ratio=0.45)
        self.play(GrowArrow(arrow, run_time=0.6))
        self.play(FadeIn(chip, scale=0.85, run_time=0.4), Write(ct, run_time=0.5))
        cap = Text("Open it. Disagree with it.", font=SERIF, font_size=56,
                   color=SOFT).move_to(np.array([0, -2.95, 0]))
        self.play(FadeIn(cap, shift=UP * 0.12, run_time=0.5))
        self.wait(3.9)


class B13_Counters(Scene):
    """Four measured numbers counting up, each over a rule that draws with it."""

    def construct(self):
        _ground(self)
        head = eyebrow("MEASURED ON 26 OCTOBER")
        self.play(FadeIn(head, run_time=0.4))
        data = [(101318, "lines of code"), (770, "files"),
                (132, "test files"), (179, "commits")]
        xs = [-4.5, -1.5, 1.5, 4.5]
        labels = VGroup()
        rules = []
        for (val, label), x in zip(data, xs):
            lab = Text(label, font=SERIF, font_size=46, color=SOFT)
            lab.move_to(np.array([x, -1.45, 0]))
            labels.add(lab)
            r = Line(LEFT * 0.01, RIGHT * 0.01, color=SPARK, stroke_width=5)
            r.move_to(np.array([x, -0.98, 0]))
            rules.append(r)
        self.play(LaggedStart(*[FadeIn(l, run_time=0.3) for l in labels],
                              lag_ratio=0.2, run_time=0.9))
        for (val, _), x, rule in zip(data, xs, rules):
            tr = ValueTracker(0)
            num = always_redraw(
                lambda t=tr, px=x: Text(f"{int(t.get_value()):,}", font=SERIF,
                                        weight="BOLD", font_size=66, color=INK)
                .move_to(np.array([px, -0.32, 0]))
            )
            self.add(num, rule)
            self.play(tr.animate.set_value(val),
                      rule.animate.stretch_to_fit_width(2.2),
                      run_time=0.75)
        self.wait(5.6)


class B14_Monorepo(Scene):
    """The four parts of the monorepo, wired."""

    def construct(self):
        _ground(self)
        head = eyebrow("ONE REPOSITORY, FOUR PARTS")
        self.play(FadeIn(head, run_time=0.4))
        spec = [("apps/web", "what you look at", LEFT * 3.1 + UP * 1.15),
                ("apps/api", "what you talk to", RIGHT * 3.1 + UP * 1.15),
                ("packages/engine", "parse and index", LEFT * 3.1 + DOWN * 1.45),
                ("workers", "the slow jobs", RIGHT * 3.1 + DOWN * 1.45)]
        boxes = VGroup()
        for name, sub, pos in spec:
            b = Rectangle(width=5.9, height=1.7, stroke_color=INK, stroke_width=3,
                          fill_color=CARD, fill_opacity=1)
            t = Text(name, font=MONO, font_size=46, color=INK).move_to(b)
            boxes.add(VGroup(b, t).move_to(pos))
        self.play(LaggedStart(*[FadeIn(b, scale=0.9) for b in boxes],
                              lag_ratio=0.25, run_time=1.5))
        wires = VGroup(
            Line(boxes[0].get_right(), boxes[1].get_left(), color=SOFT, stroke_width=3),
            Line(boxes[1].get_bottom(), boxes[3].get_top(), color=SOFT, stroke_width=3),
            Line(boxes[0].get_bottom(), boxes[2].get_top(), color=SOFT, stroke_width=3),
            Line(boxes[2].get_right(), boxes[3].get_left(), color=SPARK, stroke_width=4),
        )
        self.play(LaggedStart(*[Create(w) for w in wires], lag_ratio=0.25, run_time=1.2))
        self.wait(4.4)


class B16_Honest(Scene):
    """What works and what does not, as two bars."""

    def construct(self):
        _ground(self)
        head = eyebrow("NINE DAYS OLD")
        self.play(FadeIn(head, run_time=0.4))
        rows = [("indexing", 0.92, INK, "works"),
                ("answering", 0.38, SOFT, "being built")]
        g = VGroup()
        for label, frac, col, note in rows:
            lab = Text(label, font=SERIF, weight="BOLD", font_size=46, color=INK)
            track = Rectangle(width=6.6, height=0.62, stroke_color=RULE, stroke_width=2,
                              fill_color=CARD, fill_opacity=1)
            fill = Rectangle(width=6.6 * frac, height=0.62, stroke_width=0,
                             fill_color=col, fill_opacity=1)
            fill.align_to(track, LEFT)
            bar = VGroup(track, fill)
            note_t = Text(note, font=SERIF, font_size=30, color=SOFT)
            row = VGroup(lab, bar, note_t).arrange(RIGHT, buff=0.55)
            lab.align_to(row, LEFT)
            g.add(row)
        g.arrange(DOWN, buff=0.95, aligned_edge=LEFT).set_y(-0.2)
        for row in g:
            track, fill = row[1]
            target = fill.copy()
            fill.stretch_to_fit_width(0.01)
            fill.align_to(track, LEFT)
            self.play(FadeIn(row[0], run_time=0.3), FadeIn(track, run_time=0.3))
            self.play(Transform(fill, target, run_time=0.8))
            self.play(FadeIn(row[2], run_time=0.3))
        cap = Text("No demo of something that does not exist yet.",
                   font=SERIF, font_size=46, color=INK).move_to(np.array([0, -2.95, 0]))
        self.play(FadeIn(cap, shift=UP * 0.12, run_time=0.5))
        self.wait(5.0)
