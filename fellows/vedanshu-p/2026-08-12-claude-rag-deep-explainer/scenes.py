"""scenes.py — Manim scenes for claude-liam-rag-deep-explainer.

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


# ─────────────────────────────────────────────────────────────────────────────
#  B05_TrainingCutoff
#  A timeline: training-cutoff marker, then a "policy changed" marker AFTER
#  it. The gap between the two is the entire failure, drawn as a straight line.
# ─────────────────────────────────────────────────────────────────────────────
class B05_TrainingCutoff(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("The Gap", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        line = Line(LEFT * 5, RIGHT * 5, color=INK, stroke_width=2)
        self.play(Create(line), run_time=0.8)

        cutoff_x = -1.5
        policy_x = 2.5

        cutoff_tick = Line(UP * 0.18, DOWN * 0.18, color=INK, stroke_width=2).move_to([cutoff_x, 0, 0])
        cutoff_lbl = _label("training cutoff", size=16).next_to(cutoff_tick, UP, buff=0.25)
        self.play(Create(cutoff_tick), FadeIn(cutoff_lbl), run_time=0.6)

        policy_tick = Line(UP * 0.18, DOWN * 0.18, color=ACC, stroke_width=3).move_to([policy_x, 0, 0])
        policy_lbl = _label("policy changed", size=16, color=ACC).next_to(policy_tick, UP, buff=0.25)
        self.play(Create(policy_tick), FadeIn(policy_lbl), run_time=0.6)

        gap = Rectangle(width=policy_x - cutoff_x, height=0.5, color=ACC,
                         stroke_width=0, fill_color=ACC, fill_opacity=0.15
                         ).move_to([(cutoff_x + policy_x) / 2, 0, 0])
        gap_lbl = _label("the gap is the failure", size=17, color=ACC).next_to(gap, DOWN, buff=0.35)
        self.play(FadeIn(gap), FadeIn(gap_lbl), run_time=0.8)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_FrozenWeights
#  Training corpus feeds in; weights solidify (lock). Nothing after the
#  cutoff was ever written down.
# ─────────────────────────────────────────────────────────────────────────────
class B08_FrozenWeights(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Parametric Memory", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        corpus = Rectangle(width=2.6, height=1.6, color=INK, stroke_width=1.5,
                            fill_color=CARD, fill_opacity=1).shift(LEFT * 3.2)
        corpus_lbl = _label("training corpus", size=16).move_to(corpus)
        self.play(FadeIn(corpus), FadeIn(corpus_lbl), run_time=0.6)

        arrow = Arrow(corpus.get_right(), corpus.get_right() + RIGHT * 1.6,
                      color=INK, stroke_width=2, buff=0.1)
        self.play(GrowArrow(arrow), run_time=0.5)

        weights = Rectangle(width=2.6, height=1.6, color=INK, stroke_width=1.5,
                             fill_color=GHOST, fill_opacity=0.25
                             ).next_to(arrow, RIGHT, buff=0.1)
        weights_lbl = _label("the weights", size=16).move_to(weights)
        self.play(FadeIn(weights), FadeIn(weights_lbl), run_time=0.6)

        # freeze: weights solidify to ink-filled + a lock glyph
        weights_frozen = weights.copy().set_fill(INK, opacity=1)
        lock_body = Rectangle(width=0.35, height=0.28, color=BG, stroke_width=0,
                               fill_color=BG, fill_opacity=1).move_to(weights.get_center())
        lock_arc = Arc(radius=0.16, start_angle=0, angle=PI, color=BG, stroke_width=3
                        ).next_to(lock_body, UP, buff=-0.05)
        self.play(Transform(weights, weights_frozen), FadeOut(weights_lbl), run_time=0.8)
        self.play(FadeIn(lock_body), Create(lock_arc), run_time=0.5)

        stamp = _label("frozen the moment training stops", size=17, color=ACC
                        ).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(stamp), run_time=0.6)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B10_LiveStore
#  A shelf of documents; one slides in fresh, stamped "today" — contrast to
#  the frozen weights of B08.
# ─────────────────────────────────────────────────────────────────────────────
class B10_LiveStore(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Non-Parametric Memory", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        shelf = Rectangle(width=6.4, height=2.6, color=INK, stroke_width=1.5,
                           fill_color=CARD, fill_opacity=1).shift(DOWN * 0.2)
        self.play(FadeIn(shelf), run_time=0.5)

        rows = VGroup()
        for i in range(4):
            row = Rectangle(width=5.6, height=0.4, color=INK, stroke_width=0,
                             fill_color=GHOST, fill_opacity=0.35
                             ).move_to(shelf.get_center() + UP * (0.9 - i * 0.55))
            rows.add(row)
        self.play(*[FadeIn(r) for r in rows], run_time=0.6)

        new_doc = Rectangle(width=5.6, height=0.4, color=ACC, stroke_width=2,
                             fill_color=ACC, fill_opacity=0.15).move_to(rows[3])
        new_doc.shift(LEFT * 8)
        self.play(new_doc.animate.move_to(rows[3]), run_time=0.9, rate_func=rate_functions.ease_out_cubic)

        today = _label("updated today", size=15, color=ACC).next_to(new_doc, RIGHT, buff=0.25)
        self.play(FadeIn(today), run_time=0.4)

        stamp = _label("swapped, corrected, added — no retraining", size=17, color=ACC
                        ).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(stamp), run_time=0.6)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B14_RetrieverSearch
#  A query enters; a sweep passes over document icons; only the matching
#  passages light up and get pulled out.
# ─────────────────────────────────────────────────────────────────────────────
class B14_RetrieverSearch(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("The Retriever", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        query = Rectangle(width=2.2, height=0.7, color=INK, stroke_width=1.5,
                           fill_color=CARD, fill_opacity=1).shift(UP * 1.8)
        query_lbl = _label("the question", size=15).move_to(query)
        self.play(FadeIn(query), FadeIn(query_lbl), run_time=0.5)

        docs = VGroup()
        hits = [1, 3]
        for i in range(5):
            d = Rectangle(width=1.3, height=1.0, color=INK, stroke_width=1.2,
                           fill_color=CARD, fill_opacity=1
                           ).move_to([(i - 2) * 1.7, -1.0, 0])
            docs.add(d)
        self.play(*[FadeIn(d) for d in docs], run_time=0.6)

        sweep = Rectangle(width=0.15, height=2.2, color=ACC, stroke_width=0,
                           fill_color=ACC, fill_opacity=0.5).move_to([-3.6, -1.0, 0])
        self.play(FadeIn(sweep), run_time=0.2)
        self.play(sweep.animate.move_to([3.6, -1.0, 0]), run_time=1.4, rate_func=rate_functions.linear)
        self.play(FadeOut(sweep), run_time=0.2)

        highlights = VGroup()
        for i in hits:
            ring = SurroundingRectangle(docs[i], color=ACC, stroke_width=3, buff=0.06)
            highlights.add(ring)
        self.play(*[Create(h) for h in highlights], run_time=0.6)

        pulled = VGroup(*[docs[i].copy() for i in hits])
        self.play(pulled.animate.shift(DOWN * 1.6), run_time=0.7)

        stamp = _label("only the passages that matter", size=17, color=ACC).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(stamp), run_time=0.5)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B15_GeneratorCondition
#  Question + retrieved passages combine into ONE input; the answer writes
#  itself out of that combination, not from memory.
# ─────────────────────────────────────────────────────────────────────────────
class B15_GeneratorCondition(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("The Generator", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        q = Rectangle(width=2.2, height=0.8, color=INK, stroke_width=1.5,
                       fill_color=CARD, fill_opacity=1).shift(LEFT * 3 + UP * 0.8)
        q_lbl = _label("question", size=15).move_to(q)
        p = Rectangle(width=2.2, height=0.8, color=ACC, stroke_width=1.5,
                       fill_color=CARD, fill_opacity=1).shift(LEFT * 3 + DOWN * 0.8)
        p_lbl = _label("retrieved passage", size=13).move_to(p)
        self.play(FadeIn(q), FadeIn(q_lbl), FadeIn(p), FadeIn(p_lbl), run_time=0.6)

        plus = _label("+", size=26).move_to(LEFT * 3)
        self.play(FadeIn(plus), run_time=0.3)

        arrow = Arrow(LEFT * 1.6, RIGHT * 0.4, color=INK, stroke_width=2, buff=0.1)
        self.play(GrowArrow(arrow), run_time=0.5)

        gen = Rectangle(width=3.2, height=2.0, color=INK, stroke_width=1.5,
                         fill_color=CARD, fill_opacity=1).shift(RIGHT * 3)
        gen_lbl = _label("generator", size=15, color=SOFT).move_to(gen).shift(UP * 0.7)
        self.play(FadeIn(gen), FadeIn(gen_lbl), run_time=0.5)

        answer = _label("a grounded answer", size=16, color=ACC).move_to(gen).shift(DOWN * 0.2)
        self.play(Write(answer), run_time=0.9)

        stamp = _label("conditioned on both — not on memory alone", size=17, color=ACC
                        ).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(stamp), run_time=0.5)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B21_RetrievalVsFinetune
#  Qualitative bars only — NO invented numbers. "Knowledge injection
#  strength": fine-tuning shorter, retrieval taller. Citation on screen.
# ─────────────────────────────────────────────────────────────────────────────
class B21_RetrievalVsFinetune(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Injecting New Facts", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        base_y = -1.2
        ft_bar_bg = Rectangle(width=1.6, height=2.2, color=GHOST, stroke_width=0,
                               fill_color=GHOST, fill_opacity=0.25
                               ).move_to([-1.8, base_y + 1.1, 0]).align_to([0, base_y, 0], DOWN)
        rag_bar_bg = Rectangle(width=1.6, height=2.2, color=GHOST, stroke_width=0,
                                fill_color=GHOST, fill_opacity=0.25
                                ).move_to([1.8, base_y + 1.1, 0]).align_to([0, base_y, 0], DOWN)
        self.play(FadeIn(ft_bar_bg), FadeIn(rag_bar_bg), run_time=0.5)

        ft_fill = Rectangle(width=1.6, height=0.01, color=INK, stroke_width=0,
                             fill_color=INK, fill_opacity=0.7
                             ).move_to(ft_bar_bg).align_to(ft_bar_bg, DOWN)
        rag_fill = Rectangle(width=1.6, height=0.01, color=ACC, stroke_width=0,
                              fill_color=ACC, fill_opacity=1
                              ).move_to(rag_bar_bg).align_to(rag_bar_bg, DOWN)
        self.play(FadeIn(ft_fill), FadeIn(rag_fill), run_time=0.3)

        ft_full = Rectangle(width=1.6, height=1.0, color=INK, stroke_width=0,
                             fill_color=INK, fill_opacity=0.7
                             ).move_to(ft_bar_bg).align_to(ft_bar_bg, DOWN)
        rag_full = Rectangle(width=1.6, height=2.1, color=ACC, stroke_width=0,
                              fill_color=ACC, fill_opacity=1
                              ).move_to(rag_bar_bg).align_to(rag_bar_bg, DOWN)
        self.play(Transform(ft_fill, ft_full), Transform(rag_fill, rag_full),
                  run_time=1.2, rate_func=rate_functions.ease_out_cubic)

        ft_lbl = _label("Fine-tuning", size=16).next_to(ft_bar_bg, DOWN, buff=0.25)
        rag_lbl = _label("Retrieval", size=16, color=ACC).next_to(rag_bar_bg, DOWN, buff=0.25)
        self.play(FadeIn(ft_lbl), FadeIn(rag_lbl), run_time=0.4)

        cite = _cite("Direct comparisons favor retrieval for new-fact injection — Ovadia et al. 2024; Soudani et al. 2024. Schematic, not measured.")
        cite.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B26_Threshold
#  A qualitative slider: "fits in a prompt" <-> "has to be searched." No
#  fixed document count — the chapter itself declines to give one.
# ─────────────────────────────────────────────────────────────────────────────
class B26_Threshold(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Where The Line Sits", size=30, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        track = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2)
        self.play(Create(track), run_time=0.7)

        left_lbl = _label("fits in a prompt", size=17).next_to(track, UP, buff=0.3).align_to(track, LEFT)
        right_lbl = _label("has to be searched", size=17).next_to(track, UP, buff=0.3).align_to(track, RIGHT)
        self.play(FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.5)

        knob = Dot(radius=0.14, color=ACC).move_to(track.get_left())
        self.play(FadeIn(knob), run_time=0.3)
        self.play(knob.animate.move_to(track.get_right() * 0.55), run_time=1.3,
                  rate_func=rate_functions.ease_in_out_sine)

        stamp = _label("no fixed count — small & stable vs. large & changing", size=16, color=ACC
                        ).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(stamp), run_time=0.6)
        self.wait(0.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B31_SameMechanism
#  Two frames, same shape: the broken run and the fixed run, side by side.
#  Only the input arrow differs — the mechanism itself never changed.
# ─────────────────────────────────────────────────────────────────────────────
class B31_SameMechanism(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = _label("Same Model. Different Input.", size=28, weight="BOLD").to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        def frame(center, tint, tint_opacity, label_text, answer_text, answer_color):
            box = Rectangle(width=4.4, height=3.0, color=INK, stroke_width=1.5,
                             fill_color=CARD, fill_opacity=1).move_to(center)
            in_arrow = Arrow(box.get_left() + LEFT * 1.1, box.get_left(),
                              color=tint, stroke_width=2, buff=0.05)
            in_lbl = _label(label_text, size=13, color=tint).next_to(in_arrow, UP, buff=0.12)
            ans = _label(answer_text, size=15, color=answer_color).move_to(box).shift(DOWN * 0.3)
            model_lbl = _label("same model", size=13, color=SOFT).move_to(box).shift(UP * 0.9)
            return VGroup(box, in_arrow, in_lbl, ans, model_lbl)

        left = frame(LEFT * 3.2, GHOST, 0.3, "memory only", "10 sick days", INK)
        right = frame(RIGHT * 3.2, ACC, 1.0, "memory + retrieved passage", "15 sick days", ACC)

        self.play(FadeIn(left), run_time=1.6)
        self.wait(1.2)
        self.play(FadeIn(right), run_time=1.6)
        self.wait(1.0)

        # underline both answer lines together — a second beat of motion so the
        # native runtime comfortably fills a long narration window without
        # relying on post-hoc slow-mo stretching (compile.py warns past ~3x).
        left_ans = left[3]
        right_ans = right[3]
        left_rule = Underline(left_ans, color=GHOST, stroke_width=2)
        right_rule = Underline(right_ans, color=ACC, stroke_width=2.5)
        self.play(Create(left_rule), Create(right_rule), run_time=1.4)
        self.wait(1.0)

        stamp = _label("only the input changed", size=18, color=ACC).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(stamp), run_time=0.9)
        self.wait(3.5)
