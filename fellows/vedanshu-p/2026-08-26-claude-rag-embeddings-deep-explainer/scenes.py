"""scenes.py — Manim scenes for claude-rag-embeddings-deep-explainer.

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
No invented numbers/units on screen — qualitative comparisons only, citations
carried as small SOFT text alongside any claim that needs one (DOUBLE-CHECK LAW).
No slant=ITALIC on multi-word text (Pango collapses spaces).
"""
from manim import *
import numpy as np

# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all body text
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#6E6A57")   # secondary / muted text
GHOST = ManimColor("#A8A491")   # dimmed / placeholder
CARD  = ManimColor("#FFFFFF")   # white card surface


def _label(text, size=22, color=None, weight=None):
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _cite(text):
    return Text(text, font_size=14, color=SOFT)


def _dot(point, color=INK, radius=0.08):
    return Dot(point=point, color=color, radius=radius)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_VocabularyToVectors
#  Words drift from a random scatter into a topic cluster; one unrelated word
#  settles far away. Rebuild of the chapter's Fig. 01 (2D teaching simplification).
# ─────────────────────────────────────────────────────────────────────────────
class B04_VocabularyToVectors(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Learned, Not Assigned", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # starting scatter (random-looking but fixed) for the four words
        starts = {
            "vacation": np.array([-3.2, 1.4, 0]),
            "PTO":      np.array([2.6, 1.8, 0]),
            "leave":    np.array([-1.0, -1.6, 0]),
            "printer":  np.array([3.4, -1.2, 0]),
        }
        # target positions: three cluster tightly, printer stays far
        targets = {
            "vacation": np.array([-1.8, 0.3, 0]),
            "PTO":      np.array([-1.1, 0.7, 0]),
            "leave":    np.array([-1.4, -0.2, 0]),
            "printer":  np.array([3.2, -0.6, 0]),
        }

        dots, labels = {}, {}
        for word, p in starts.items():
            is_printer = word == "printer"
            dots[word] = _dot(p, color=ACC if is_printer else INK)
            labels[word] = _label(word, size=18, color=ACC if is_printer else INK).next_to(dots[word], UP, buff=0.15)

        self.play(*[FadeIn(dots[w]) for w in starts], *[FadeIn(labels[w]) for w in starts], run_time=0.8)
        self.wait(0.3)

        anims = []
        for word, p in targets.items():
            anims.append(dots[word].animate.move_to(p))
            anims.append(labels[word].animate.next_to(p, UP, buff=0.15))
        self.play(*anims, run_time=1.6, rate_func=rate_functions.ease_out_cubic)

        ring = Circle(radius=0.9, color=ACC, stroke_width=2).move_to(
            (targets["vacation"] + targets["PTO"] + targets["leave"]) / 3
        )
        self.play(Create(ring), run_time=0.6)

        cite = _cite("Mikolov et al., 2013 — teaching simplification: real embeddings use hundreds of dimensions")
        cite.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(5.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_VectorArithmetic
#  king − man + woman ≈ queen, shown as an arrow translated from one base
#  point to another. Illustrative geometry, not a literal 2D embedding.
# ─────────────────────────────────────────────────────────────────────────────
class B08_VectorArithmetic(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("king − man + woman", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        man   = np.array([-2.6, -1.2, 0])
        king  = np.array([-2.0, 1.4, 0])
        woman = np.array([1.8, -1.2, 0])
        queen = np.array([2.4, 1.4, 0])

        pts = {"man": man, "king": king, "woman": woman, "queen": queen}
        dots = {w: _dot(p) for w, p in pts.items()}
        labels = {w: _label(w, size=18).next_to(p, DOWN if w in ("man", "woman") else UP, buff=0.15)
                  for w, p in pts.items()}
        self.play(*[FadeIn(dots[w]) for w in pts], *[FadeIn(labels[w]) for w in pts], run_time=0.8)

        arrow1 = Arrow(man, king, color=INK, stroke_width=3, buff=0.12)
        self.play(GrowArrow(arrow1), run_time=0.7)

        arrow2 = Arrow(woman, queen, color=ACC, stroke_width=3, buff=0.12)
        self.play(TransformFromCopy(arrow1, arrow2), run_time=1.0, rate_func=rate_functions.ease_out_cubic)

        note = _label("same arrow, redrawn from “woman”", size=16, color=ACC).next_to(arrow2, RIGHT, buff=0.3)
        self.play(FadeIn(note), run_time=0.5)

        cite = _cite("Mikolov, Yih & Zweig, 2013 — directions between vectors, not raw positions")
        cite.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(4.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_ExcludeTheQuery
#  The honest replication caveat: a naive nearest-vector search lands back on
#  "king"; excluding the query word from the search finds "queen" instead.
# ─────────────────────────────────────────────────────────────────────────────
class B09_ExcludeTheQuery(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Exclude The Query Word", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        target = np.array([-3.0, 0.3, 0])
        king = np.array([-3.0, -2.1, 0])
        queen = np.array([3.2, 0.3, 0])
        others = [np.array([-0.8, 1.9, 0]), np.array([1.0, 1.9, 0]), np.array([0.1, -2.3, 0])]

        target_dot = _dot(target, color=ACC)
        target_lbl = _label("king − man + woman", size=16, color=ACC).next_to(target_dot, UP, buff=0.25)
        king_dot = _dot(king)
        king_lbl = _label("king", size=18).next_to(king_dot, LEFT, buff=0.25)
        queen_dot = _dot(queen)
        queen_lbl = _label("queen", size=18).next_to(queen_dot, DOWN, buff=0.25)
        other_dots = [_dot(p, color=GHOST) for p in others]

        self.play(FadeIn(target_dot), FadeIn(target_lbl), FadeIn(king_dot), FadeIn(king_lbl),
                   FadeIn(queen_dot), FadeIn(queen_lbl), *[FadeIn(d) for d in other_dots], run_time=0.8)

        naive_arrow = Arrow(target, king, color=INK, stroke_width=3, buff=0.1)
        naive_lbl = _label("nearest vector: “king” again", size=16).next_to(naive_arrow, RIGHT, buff=0.25)
        self.play(GrowArrow(naive_arrow), FadeIn(naive_lbl), run_time=0.9)
        self.wait(0.6)

        self.play(FadeOut(naive_arrow), FadeOut(naive_lbl),
                   king_dot.animate.set_color(GHOST), king_lbl.animate.set_color(GHOST), run_time=0.6)
        exclude_lbl = _label("exclude the query word", size=16, color=SOFT).next_to(king_dot, DOWN, buff=0.3)
        self.play(FadeIn(exclude_lbl), run_time=0.5)

        fixed_arrow = Arrow(target, queen, color=ACC, stroke_width=3, buff=0.1)
        fixed_lbl = _label("nearest remaining vector: “queen”", size=16, color=ACC).next_to(fixed_arrow, UP, buff=0.3)
        self.play(GrowArrow(fixed_arrow), FadeIn(fixed_lbl), run_time=0.9)

        cite = _cite("the chapter's own caveat — qualitative finding only, no invented replication statistics")
        cite.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(4.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_WordToPassage
#  A single word-point, alone, contrasted with a whole sentence's scattered
#  word-points merging into one combined passage-vector.
# ─────────────────────────────────────────────────────────────────────────────
class B11_WordToPassage(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("One Word. One Passage.", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        word_dot = _dot(np.array([-3.2, 1.2, 0]))
        word_lbl = _label("word2vec: one word at a time", size=16).next_to(word_dot, DOWN, buff=0.2)
        self.play(FadeIn(word_dot), FadeIn(word_lbl), run_time=0.7)
        self.wait(0.4)

        sentence_pts = [np.array([1.4, 1.6, 0]), np.array([2.6, 0.6, 0]), np.array([1.0, -0.4, 0]),
                         np.array([2.4, -1.2, 0]), np.array([3.4, 1.0, 0])]
        sentence_dots = [_dot(p, color=SOFT) for p in sentence_pts]
        self.play(*[FadeIn(d) for d in sentence_dots], run_time=0.7)

        combined = np.array([2.2, 0.1, 0])
        anims = [d.animate.move_to(combined) for d in sentence_dots]
        self.play(*anims, run_time=1.3, rate_func=rate_functions.ease_out_cubic)
        merged = _dot(combined, color=ACC, radius=0.14)
        self.play(FadeOut(*sentence_dots), FadeIn(merged), run_time=0.5)
        merged_lbl = _label("a passage, one vector", size=18, color=ACC).next_to(merged, UP, buff=0.2)
        self.play(FadeIn(merged_lbl), run_time=0.5)

        cite = _cite("a passage's meaning is more than the sum of its words' meanings")
        cite.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(4.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_BertToSbert
#  A state-card morph: BERT's raw output compares sentences poorly; the same
#  network, restructured as Sentence-BERT, compares them well.
# ─────────────────────────────────────────────────────────────────────────────
class B13_BertToSbert(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Restructured For Comparison", size=27, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        card1 = RoundedRectangle(width=5.2, height=2.0, corner_radius=0.15, color=INK,
                                   stroke_width=1.5, fill_color=CARD, fill_opacity=1).shift(UP * 0.6)
        card1_lbl = _label("BERT", size=22, weight="BOLD").move_to(card1).shift(UP * 0.45)
        card1_sub = _label("raw output → poor sentence comparison", size=15, color=SOFT).move_to(card1).shift(DOWN * 0.35)
        self.play(FadeIn(card1), FadeIn(card1_lbl), FadeIn(card1_sub), run_time=0.8)
        self.wait(0.6)

        card2 = RoundedRectangle(width=5.2, height=2.0, corner_radius=0.15, color=ACC,
                                   stroke_width=1.5, fill_color=CARD, fill_opacity=1).shift(DOWN * 1.7)
        card2_lbl = _label("Sentence-BERT", size=22, weight="BOLD", color=ACC).move_to(card2).shift(UP * 0.45)
        card2_sub = _label("one vector per passage → direct comparison", size=15, color=SOFT).move_to(card2).shift(DOWN * 0.35)

        arrow = Arrow(card1.get_bottom(), card2.get_top(), color=ACC, stroke_width=3, buff=0.15)
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(card2), FadeIn(card2_lbl), FadeIn(card2_sub), run_time=0.8)

        cite = _cite("Devlin et al., 2019 (BERT); Reimers & Gurevych, 2019 (Sentence-BERT)")
        cite.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(4.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B19_CosineGeometry
#  The actual geometry: two vectors from the origin, the angle between them,
#  cos(theta) sweeping from near 1 (close) to near 0 (unrelated).
# ─────────────────────────────────────────────────────────────────────────────
class B19_CosineGeometry(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("The Angle Between Two Vectors", size=26, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        origin = np.array([-0.5, -0.4, 0])
        axes_hint = Dot(origin, radius=0.05, color=INK)
        v1 = Arrow(origin, origin + np.array([3.0, 1.8, 0]), color=INK, stroke_width=3, buff=0)
        self.play(FadeIn(axes_hint), GrowArrow(v1), run_time=0.7)

        angle_tracker = ValueTracker(0.3)

        def make_v2():
            a = angle_tracker.get_value()
            base_angle = np.arctan2(1.8, 3.0)
            length = 2.6
            end = origin + length * np.array([np.cos(base_angle - a), np.sin(base_angle - a), 0])
            return Arrow(origin, end, color=ACC, stroke_width=3, buff=0)

        v2 = always_redraw(make_v2)
        self.play(GrowArrow(v2), run_time=0.6)

        theta_lbl = always_redraw(
            lambda: _label(f"cos θ ≈ {np.cos(angle_tracker.get_value()):.1f}", size=20, color=ACC)
            .next_to(origin, UP + RIGHT, buff=0.9)
        )
        self.play(FadeIn(theta_lbl), run_time=0.4)

        note_close = _label("small angle → close in meaning", size=16, color=SOFT).to_edge(DOWN, buff=1.3)
        self.play(FadeIn(note_close), run_time=0.5)
        self.wait(0.4)

        # fade the "close" label out before the angle widens, and only fade the
        # "far" label in once the widening is complete — otherwise there's a
        # window where cos θ already reads near 0 while the screen still claims
        # "small angle", a real claim/visual mismatch caught in VISUAL QC.
        self.play(FadeOut(note_close), run_time=0.3)
        self.play(angle_tracker.animate.set_value(1.25), run_time=1.8, rate_func=rate_functions.ease_in_out_sine)
        note_far = _label("wide angle → unrelated", size=16, color=SOFT).to_edge(DOWN, buff=1.3)
        self.play(FadeIn(note_far), run_time=0.5)

        cite = _cite("Manning, Raghavan & Schütze, 2008 — the formula, not a computed example")
        cite.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(3.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B21_ClosenessPremise
#  Two point-pairs: one pulling close (similar meaning), one pushing apart
#  (different meaning) — independent of whether their labels share words.
# ─────────────────────────────────────────────────────────────────────────────
class B21_ClosenessPremise(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Close = Similar. Far = Different.", size=25, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        a1, a2 = np.array([-3.2, 0.8, 0]), np.array([-1.8, 1.4, 0])
        b1, b2 = np.array([1.6, 1.2, 0]), np.array([-1.2, -1.6, 0])

        dot_a1, dot_a2 = _dot(a1), _dot(a2)
        dot_b1, dot_b2 = _dot(b1, color=ACC), _dot(b2, color=ACC)
        self.play(FadeIn(dot_a1), FadeIn(dot_a2), FadeIn(dot_b1), FadeIn(dot_b2), run_time=0.7)

        target_a2 = a1 + np.array([0.6, -0.1, 0])
        target_b2 = b1 + np.array([3.2, -0.4, 0])
        self.play(dot_a2.animate.move_to(target_a2), dot_b2.animate.move_to(target_b2),
                   run_time=1.3, rate_func=rate_functions.ease_out_cubic)

        lbl_close = _label("similar meaning", size=16).next_to(dot_a1, DOWN, buff=0.6)
        lbl_far = _label("different meaning", size=16, color=ACC).next_to(dot_b1, UP, buff=0.6)
        self.play(FadeIn(lbl_close), FadeIn(lbl_far), run_time=0.6)

        cite = _cite("regardless of whether the underlying words overlap at all")
        cite.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(4.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B26_ParaphraseVsTrap
#  The combined worked-example map — rebuild of the chapter's Fig. 02. The
#  paraphrase pair sits close; the shared-phrase trap pair sits far apart.
# ─────────────────────────────────────────────────────────────────────────────
class B26_ParaphraseVsTrap(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Meaning, Not Vocabulary", size=27, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        vac = np.array([-2.6, 1.0, 0])
        pto = np.array([-1.9, 1.5, 0])
        dot_vac, dot_pto = _dot(vac), _dot(pto)
        lbl_vac = _label("“vacation”", size=14).next_to(dot_vac, LEFT, buff=0.15)
        lbl_pto = _label("“PTO policy”", size=14).next_to(dot_pto, UP, buff=0.15)
        self.play(FadeIn(dot_vac), FadeIn(dot_pto), FadeIn(lbl_vac), FadeIn(lbl_pto), run_time=0.7)
        close_tag = _label("different words, same region", size=15, color=SOFT).next_to(
            VGroup(dot_vac, dot_pto), DOWN, buff=0.35)
        self.play(FadeIn(close_tag), run_time=0.5)
        self.wait(0.4)

        timeoff = np.array([1.4, -0.6, 0])
        laptop = np.array([3.2, 1.4, 0])
        dot_t, dot_l = _dot(timeoff, color=ACC), _dot(laptop, color=ACC)
        lbl_t = _label("“time off”", size=14, color=ACC).next_to(dot_t, DOWN, buff=0.15)
        lbl_l = _label("“new laptop”", size=14, color=ACC).next_to(dot_l, UP, buff=0.15)
        self.play(FadeIn(dot_t), FadeIn(dot_l), FadeIn(lbl_t), FadeIn(lbl_l), run_time=0.7)
        far_tag = _label("shared words, different regions", size=15, color=SOFT).next_to(
            VGroup(dot_t, dot_l), DOWN, buff=0.35)
        self.play(FadeIn(far_tag), run_time=0.5)

        caption = _label("the vector captures meaning, not vocabulary", size=18, color=ACC).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(caption), run_time=0.6)

        cite = _cite("rebuild of the chapter's Fig. 02 — qualitative placement, no computed score")
        cite.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(4.5)
