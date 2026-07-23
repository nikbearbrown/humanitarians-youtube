"""vox_scenes.py — Why the Group That Learned Less Was Sure It Learned More
(vox-fluency-trap, fresh build, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT beat. Durations read from this reel's
beat_sheet.json (actual_duration_s once audio is locked; estimates as
fallback) — the compile ladder retimes ±5% anyway. Render everything:
  bash scripts/vox_run.sh reels/vox-fluency-trap

Color law (FACTCHECK.md / beat_sheet color_semantics):
  dusty blue #5B7B9C = hand-coders / interrogation / checking
  terracotta #D35F43 = AI-delegation
  gold = the single editor's-pen voice. Never swap mid-film.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# Fallback estimates — used when this file is checked from an isolated copy
# (vox_run Gate A) where beat_sheet.json is not adjacent. At render time the
# real sheet sits next to this file and measured durations win.
DUR = {"B01": 8.3, "B03": 8.3, "B05": 7.4, "B06": 9.2, "B08": 8.8,
       "B09": 9.2, "B10": 7.3, "B11": 8.8, "B13": 10.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _pct_bar(value, color, width=1.6, scale=0.045):
    """Zero-baseline bar; height honest to the printed value."""
    bar = Rectangle(width=width, height=value * scale)
    bar.set_fill(color, 1).set_stroke(width=0)
    return bar


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):            # title card
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE FLUENCY TRAP", font=SERIF, color=BLUE, font_size=24)
        t1 = Text("Why the group that learned less", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("was sure it learned more", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Split(Scene):            # one cohort divides — no headcount printed
    def construct(self):
        total = DUR["B03"]
        left = IsotypeGrid([24], [INK], per_row=6, size=0.28, gap=0.14)
        right = IsotypeGrid([24], [INK], per_row=6, size=0.28, gap=0.14)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.14).move_to(UP * 0.4)
        self.play(AnimationGroup(left.count_up(1.4), right.count_up(1.4),
                                 lag_ratio=0.0))
        lab_ai = SerifLabel("AI assistant", TERRA)
        lab_hand = SerifLabel("hand-coding", BLUE)
        self.play(pair[0].animate.shift(LEFT * 1.4),
                  pair[1].animate.shift(RIGHT * 1.4), run_time=1.0)
        lab_ai.next_to(left, DOWN, buff=0.45)
        lab_hand.next_to(right, DOWN, buff=0.45)
        self.play(LaggedStart(*[m.animate.set_fill(TERRA, 1)
                                for m in left.marks],
                              lag_ratio=0.01, run_time=1.0),
                  FadeIn(lab_ai, shift=UP * 0.1))
        self.play(LaggedStart(*[m.animate.set_fill(BLUE, 1)
                                for m in right.marks],
                              lag_ratio=0.01, run_time=1.0),
                  FadeIn(lab_hand, shift=UP * 0.1))
        self.wait(max(0.5, total - 4.6))


class B05_Quiz(Scene):             # the twist — film's own question card
    def construct(self):
        _quote_scene(self, "Do you understand what the code does?",
                     "— 14-question comprehension quiz", None,
                     "understand", DUR["B05"])


class B06_Bars(Scene):             # 67 vs 50, zero baseline, honest bracket
    def construct(self):
        total = DUR["B06"]
        base_y = -2.2
        baseline = Line(LEFT * 4.6, RIGHT * 4.6, color=INK,
                        stroke_width=2).shift(UP * base_y)
        hand = _pct_bar(67, BLUE)
        ai = _pct_bar(50, TERRA)
        hand.move_to(LEFT * 1.6 + UP * base_y, aligned_edge=DOWN)
        ai.move_to(RIGHT * 1.6 + UP * base_y, aligned_edge=DOWN)
        lab_h = SerifLabel("hand-coding", BLUE, size=26)
        lab_a = SerifLabel("AI-assisted", TERRA, size=26)
        lab_h.next_to(hand, DOWN, buff=0.35)
        lab_a.next_to(ai, DOWN, buff=0.35)
        n_h = Text("67", font=SERIF, color=INK, font_size=44, weight=BOLD)
        n_a = Text("50", font=SERIF, color=INK, font_size=44, weight=BOLD)
        title = SerifLabel("comprehension quiz average", NAVY, size=28)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), Create(baseline), FadeIn(lab_h), FadeIn(lab_a),
                  run_time=0.8)
        self.play(GrowFromEdge(hand, DOWN), run_time=1.0)
        n_h.next_to(hand, UP, buff=0.18)
        self.play(FadeIn(n_h), run_time=0.4)
        self.play(GrowFromEdge(ai, DOWN), run_time=1.0)
        n_a.next_to(ai, UP, buff=0.18)
        self.play(FadeIn(n_a), run_time=0.4)
        # the 17-point bracket spans the ACTUAL gap between bar tops
        bx = ai.get_right()[0] + 0.85
        top = np.array([bx, hand.get_top()[1], 0])
        bot = np.array([bx, ai.get_top()[1], 0])
        brk = VGroup(Line(top, bot, color=TERRA, stroke_width=3),
                     Line(top, top + LEFT * 0.18, color=TERRA, stroke_width=3),
                     Line(bot, bot + LEFT * 0.18, color=TERRA, stroke_width=3))
        blab = Text("17 points", font=SERIF, color=TERRA, font_size=28,
                    weight=BOLD)
        blab.next_to(brk, RIGHT, buff=0.22)
        self.play(Create(brk), FadeIn(blab), run_time=0.9)
        self.wait(max(0.5, total - 4.5))


class B08_CheckLoop(Scene):        # where understanding forms
    def construct(self):
        total = DUR["B08"]
        title = SerifLabel("where understanding forms", NAVY, size=28)
        title.to_edge(UP, buff=0.6)
        stages = ["read", "test", "question", "break", "fix"]
        r = 1.9
        nodes = VGroup()
        for i, s in enumerate(stages):
            a = TAU / 4 - i * TAU / 5
            t = Text(s, font=SERIF, color=INK, font_size=34, weight=BOLD)
            t.move_to(np.array([np.cos(a), np.sin(a), 0]) * r + DOWN * 0.4)
            nodes.add(t)
        arcs = VGroup()
        for i in range(5):
            a0 = TAU / 4 - i * TAU / 5
            a1 = TAU / 4 - (i + 1) * TAU / 5
            arc = ArcBetweenPoints(
                np.array([np.cos(a0), np.sin(a0), 0]) * (r - 0.55) + DOWN * 0.4,
                np.array([np.cos(a1), np.sin(a1), 0]) * (r - 0.55) + DOWN * 0.4,
                angle=-TAU / 7, color=BLUE, stroke_width=4)
            arc.add_tip(tip_length=0.16, tip_width=0.16)
            arcs.add(arc)
        typing = Text("typing", font=SERIF, color="#9A938A", font_size=26)
        typing.to_corner(DL, buff=0.8)
        self.play(FadeIn(title), FadeIn(typing), run_time=0.7)
        for node, arc in zip(nodes, arcs):   # the loop draws itself, verb by verb
            self.play(FadeIn(node, scale=0.9), Create(arc), run_time=0.85)
        self.wait(max(0.5, total - 5.0))


# --- chapter fig 1.2 as a beat pair: the three columns share one chart.
# Hand-coding (solid 67) and AI+interrogation (band 65–86) CONVERGE — joined
# by a faint reference line; AI+delegation (band 24–39) drops off. The two
# high columns share a behavior (checking), not a typing method. That
# convergence is the film's thesis; B06's naive two-bar read gets corrected
# here exactly the way the chapter corrects it.

_FQ = dict(base_y=-2.2, scale=0.045, xs=(-3.2, 0.0, 3.2), col_w=1.6)


def _fig12_col_label(text, accent, x, base_y):
    lab = SerifLabel(text, accent, size=24)
    if lab.width > 2.9:
        lab.scale_to_fit_width(2.9)
    lab.move_to(np.array([x, base_y - 0.55, 0]))
    return lab


def _fig12_statics():
    """Everything B09 ends with, rebuilt for B10 to inherit."""
    base_y, sc, xs, w = (_FQ["base_y"], _FQ["scale"], _FQ["xs"], _FQ["col_w"])
    baseline = Line(LEFT * 5.6, RIGHT * 5.6, color=INK,
                    stroke_width=2).shift(UP * base_y)
    hand = Rectangle(width=w, height=67 * sc)
    hand.set_fill(BLUE, 1).set_stroke(width=0)
    hand.move_to(np.array([xs[0], base_y, 0]), aligned_edge=DOWN)
    n_hand = Text("67", font=SERIF, color=INK, font_size=40, weight=BOLD)
    n_hand.next_to(hand, UP, buff=0.18)
    band = Rectangle(width=w, height=(86 - 65) * sc)
    band.set_fill(BLUE, 0.9).set_stroke(width=0)
    band.move_to(np.array([xs[1], base_y + 65 * sc, 0]), aligned_edge=DOWN)
    n_band = Text("65–86", font=SERIF, color=INK, font_size=34, weight=BOLD)
    n_band.next_to(band, UP, buff=0.18)
    ref = DashedLine(np.array([xs[0] - w / 2, base_y + 67 * sc, 0]),
                     np.array([xs[1] + w / 2 + 0.4, base_y + 67 * sc, 0]),
                     color=INK, stroke_width=2, dash_length=0.14)
    ref.set_opacity(0.55)
    ref._qc_intentional = True   # the reference line crosses the band on purpose
    lab_hand = _fig12_col_label("hand-coding", BLUE, xs[0], base_y)
    lab_int = _fig12_col_label("AI + interrogation", BLUE, xs[1], base_y)
    return baseline, hand, n_hand, band, n_band, ref, lab_hand, lab_int


class B09_Converge(Scene):         # fig 1.2, columns 1–2: the convergence
    def construct(self):
        total = DUR["B09"]
        title = SerifLabel("the variable is the checking, not the typing",
                           NAVY, size=28)
        if title.width > 11.0:
            title.scale_to_fit_width(11.0)
        title.to_edge(UP, buff=0.6)
        baseline, hand, n_hand, band, n_band, ref, lab_hand, lab_int = \
            _fig12_statics()
        # hand-coding column is already on the books — it opens the scene
        self.add(baseline, hand, n_hand, lab_hand)
        self.play(FadeIn(title), run_time=0.7)
        self.play(GrowFromEdge(band, DOWN), FadeIn(lab_int), run_time=1.2)
        self.play(FadeIn(n_band), run_time=0.5)
        self.play(Create(ref), run_time=0.9)   # the faint line lands the claim
        self.wait(max(0.5, total - 3.3))


class B10_DropOff(Scene):          # fig 1.2, column 3: delegation falls away
    def construct(self):
        total = DUR["B10"]
        base_y, sc, xs, w = (_FQ["base_y"], _FQ["scale"], _FQ["xs"],
                             _FQ["col_w"])
        title = SerifLabel("the variable is the checking, not the typing",
                           NAVY, size=28)
        if title.width > 11.0:
            title.scale_to_fit_width(11.0)
        title.to_edge(UP, buff=0.6)
        self.add(title, *_fig12_statics())
        deleg = Rectangle(width=w, height=(39 - 24) * sc)
        deleg.set_fill(TERRA, 1).set_stroke(width=0)
        deleg.move_to(np.array([xs[2], base_y + 24 * sc, 0]), aligned_edge=DOWN)
        n_del = Text("24–39", font=SERIF, color=INK, font_size=34, weight=BOLD)
        n_del.next_to(deleg, UP, buff=0.18)
        lab_del = _fig12_col_label("AI + delegation", TERRA, xs[2], base_y)
        self.play(GrowFromEdge(deleg, DOWN), FadeIn(lab_del), run_time=1.1)
        self.play(FadeIn(n_del), run_time=0.5)
        # the editor's pen: gold sweeps the EMPTY band 39→65 in the
        # delegation column — the drop-off is real and it is the point
        gap = Rectangle(width=w, height=0.06)
        gap.set_fill(GOLD, 0.55).set_stroke(width=0)
        gap.move_to(np.array([xs[2], base_y + 39 * sc, 0]), aligned_edge=DOWN)
        gap._qc_intentional = True
        gap_full = Rectangle(width=w, height=(65 - 39) * sc)
        gap_full.set_fill(GOLD, 0.55).set_stroke(width=0)
        gap_full.move_to(np.array([xs[2], base_y + 39 * sc, 0]),
                         aligned_edge=DOWN)
        gap_full._qc_intentional = True
        self.add(gap)
        self.play(Transform(gap, gap_full), run_time=1.0)
        self.wait(max(0.5, total - 2.6))


class B11_Debt(Scene):             # comprehension debt — metaphor, no numbers
    def construct(self):
        total = DUR["B11"]
        title = SerifLabel("comprehension debt", TERRA, size=28)
        title.to_edge(UP, buff=0.6)
        # the ledger meter: unscaled, growth only
        tube = Rectangle(width=0.5, height=4.0).set_stroke(INK, 2)
        tube.move_to(RIGHT * 4.6 + DOWN * 0.4)
        fill = Rectangle(width=0.44, height=0.01)
        fill.set_fill(TERRA, 1).set_stroke(width=0)
        fill.move_to(tube.get_bottom() + UP * 0.02, aligned_edge=DOWN)
        self.play(FadeIn(title), Create(tube), run_time=0.8)
        rng = np.random.default_rng(7)
        pile = VGroup()
        n_cards = 6
        for i in range(n_cards):
            card = VGroup(
                Rectangle(width=2.6, height=1.5).set_fill(WHITE, 1)
                .set_stroke("#D8D2C4", 1.5),
                *[Line(LEFT * 1.0, RIGHT * (1.0 - 0.3 * k), color="#C9C2B4",
                       stroke_width=3).shift(UP * (0.35 - 0.28 * k))
                  for k in range(3)])
            card.rotate(rng.uniform(-0.09, 0.09) * PI)
            card.move_to(LEFT * 1.4 + DOWN * 1.1
                         + UP * i * 0.28 + RIGHT * rng.uniform(-0.25, 0.25))
            pile.add(card)
            new_h = 4.0 * (i + 1) / n_cards * 0.92
            fill_next = Rectangle(width=0.44, height=new_h)
            fill_next.set_fill(TERRA, 1).set_stroke(width=0)
            fill_next.move_to(tube.get_bottom() + UP * 0.02, aligned_edge=DOWN)
            self.play(FadeIn(card, shift=DOWN * 0.35),
                      Transform(fill, fill_next), run_time=0.75)
        self.wait(max(0.5, total - 0.8 - n_cards * 0.75))


class B13_End(Scene):              # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B13"]
        t1 = Text("Let it type.", font=SERIF, color=INK, font_size=54,
                  weight=BOLD)
        t2 = Text("Keep the checking.", font=SERIF, color=INK, font_size=54,
                  weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 1", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
