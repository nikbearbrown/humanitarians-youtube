"""
Manim scenes for onprem-rag-chatbot
B01_PrivacyBoundary    — PROBLEM: a question blocked from a third-party API,
                         looping instead entirely inside your own hardware.
B04_HardwareFit        — CONTEXT: model-size vs RAM/VRAM, redrawn (simplified,
                         RAM-only) from the source's Part 1 hardware table.
B05_RagPipelineBroken  — OUTPUT cycle 1: no embedding model wired → zero
                         chunks retrieved → a confident, ungrounded answer.
B08_RagPipelineGrounded — OUTPUT cycle 2: the same pipeline, embedder wired →
                         chunks retrieved → a grounded, cited answer.

Mechanics illustrated (not a screen recording): RAG cannot retrieve anything
without an embedding model producing vectors first; chunk size 500-1000
tokens is the source's own recommendation. See beat_sheet.json metadata note
and SOURCES.md for what's source-verbatim vs constructed-for-illustration.
"""

from manim import *

# nbb teardown palette (brands/nbb.md) — crimson is the ONE accent.
PALETTE = {
    "bg":      "#FFFFFF",
    "ink":     "#2A1A0E",
    "crimson": "#C8102E",
    "slate":   "#545454",
    "gold":    "#F6D8DC",
    "hair":    "#D4D4D4",
}


def title_card(text, font_size=34):
    return Text(text, color=PALETTE["ink"], font_size=font_size).to_edge(UP, buff=0.4)


def caption(text, font_size=18):
    return Text(text, color=PALETTE["slate"], font_size=font_size).to_edge(DOWN, buff=0.3)


# --------------------------------------------------------------------------- B01

class B01_PrivacyBoundary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = title_card("Where does the question actually go?")
        self.play(Write(title), run_time=0.8)

        api_box = RoundedRectangle(width=4.4, height=2.6, corner_radius=0.15,
                                    stroke_color=PALETTE["hair"], stroke_width=2
                                    ).move_to([4.0, 0.1, 0])
        api_label = Text("THIRD-PARTY API", color=PALETTE["slate"], font_size=20
                          ).next_to(api_box, UP, buff=0.2)

        hw_box = RoundedRectangle(width=4.4, height=2.6, corner_radius=0.15,
                                   stroke_color=PALETTE["ink"], stroke_width=3
                                   ).move_to([-4.0, 0.1, 0])
        hw_label = Text("YOUR HARDWARE", color=PALETTE["ink"], font_size=20
                         ).next_to(hw_box, UP, buff=0.2)

        ollama_node = Circle(radius=0.55, color=PALETTE["ink"],
                              fill_color=PALETTE["ink"], fill_opacity=0.08
                              ).move_to(hw_box.get_center())
        ollama_lbl = Text("OLLAMA", color=PALETTE["ink"], font_size=18
                           ).move_to(ollama_node.get_center())

        self.play(Create(api_box), Create(hw_box), FadeIn(api_label), FadeIn(hw_label),
                   run_time=1.1)
        self.play(Create(ollama_node), FadeIn(ollama_lbl), run_time=0.6)

        doc = RoundedRectangle(width=1.1, height=1.4, corner_radius=0.08,
                                stroke_color=PALETTE["slate"], stroke_width=2,
                                fill_color=PALETTE["bg"], fill_opacity=1).move_to(ORIGIN)
        doc_lines = VGroup(*[
            Line(LEFT * 0.34, RIGHT * 0.34, stroke_width=2, color=PALETTE["slate"])
            .move_to(doc.get_center() + UP * 0.35 + DOWN * i * 0.3)
            for i in range(3)
        ])
        doc_group = VGroup(doc, doc_lines)
        doc_label = Text("your question + a doc chunk", color=PALETTE["slate"], font_size=16
                          ).next_to(doc_group, DOWN, buff=0.25)
        self.play(FadeIn(doc_group), Write(doc_label), run_time=0.6)
        self.wait(0.3)

        # ── first path: toward the third-party API — blocked ──
        self.play(doc_group.animate.move_to(api_box.get_center()),
                   doc_label.animate.next_to(api_box, DOWN, buff=0.35),
                   run_time=1.2)
        cross = Text("✗", color=PALETTE["crimson"], font_size=72).move_to(api_box.get_center())
        blocked = Text("blocked — never sent", color=PALETTE["crimson"], font_size=20
                        ).next_to(api_box, DOWN, buff=0.7)
        self.play(FadeIn(cross, scale=1.5), Write(blocked), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(cross), FadeOut(blocked), FadeOut(doc_label), run_time=0.5)

        # ── second path: loop entirely inside your hardware ──
        p1 = hw_box.get_top() + DOWN * 0.5
        p2 = ollama_node.get_center()
        p3 = hw_box.get_bottom() + UP * 0.5
        self.play(doc_group.animate.move_to(p1), run_time=0.7)
        self.play(doc_group.animate.move_to(p2), run_time=0.7)
        self.play(doc_group.animate.move_to(p3), run_time=0.7)

        check = Text("✓", color=PALETTE["ink"], font_size=60
                      ).next_to(hw_box, DOWN, buff=0.35)
        never_leaves = Text("0 external calls", color=PALETTE["ink"], font_size=24
                             ).next_to(check, DOWN, buff=0.2)
        self.play(FadeIn(check, scale=1.3), Write(never_leaves), run_time=0.8)
        self.wait(2.2)


# --------------------------------------------------------------------------- B04

HW_ROWS = [
    ("8B model (Llama 3.1)", 16, "8–16GB RAM · CPU-OK (slow)", PALETTE["ink"]),
    ("Qwen3-30B-A3B (MoE, ~3B active)", 24, "16–24GB · GPU recommended", PALETTE["slate"]),
    ("70B-class", 48, "40–48GB+ · GPU required", PALETTE["crimson"]),
]
HW_MAX_GB = 50


class B04_HardwareFit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = title_card("Size the hardware before you pull a model")
        self.play(Write(title), run_time=0.8)

        axis_left, axis_right = -5.3, 5.3
        axis_w = axis_right - axis_left

        def x_of(gb):
            return axis_left + axis_w * (min(gb, HW_MAX_GB) / HW_MAX_GB)

        row_ys = [1.7, 0.3, -1.1]
        axis_y = -1.9

        axis = Line([axis_left, axis_y, 0], [axis_right, axis_y, 0],
                    color=PALETTE["hair"], stroke_width=2)
        self.play(Create(axis), run_time=0.4)

        ticks = VGroup()
        for t in (0, 10, 20, 30, 40, 50):
            x = x_of(t)
            tick = Line([x, axis_y - 0.1, 0], [x, axis_y + 0.1, 0],
                        color=PALETTE["slate"], stroke_width=2)
            lbl = Text(f"{t}GB", color=PALETTE["slate"], font_size=16
                       ).next_to(tick, DOWN, buff=0.12)
            ticks.add(tick, lbl)
        self.play(FadeIn(ticks), run_time=0.5)

        for (name, gb, spec, color), y in zip(HW_ROWS, row_ys):
            label = Text(name, color=color, font_size=22).move_to([axis_left + 0.1, y + 0.35, 0])
            label.align_to([axis_left, 0, 0], LEFT)
            bar = Line([x_of(0), y, 0], [x_of(gb), y, 0], color=color, stroke_width=18)
            spec_lbl = Text(spec, color=color, font_size=18
                             ).next_to(bar, RIGHT, buff=0.25)
            self.play(FadeIn(label), run_time=0.35)
            self.play(Create(bar), run_time=1.0)
            self.play(FadeIn(spec_lbl, shift=RIGHT * 0.1), run_time=0.4)

        note = Text("embedding models: ~100–600M params — CPU always fine, whatever you pick",
                     color=PALETTE["ink"], font_size=18).next_to(axis, DOWN, buff=0.85)
        self.play(Write(note), run_time=1.0)

        cap = caption("Redrawn (simplified) from the source's Part 1 hardware table.")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(2.0)


# --------------------------------------------------------------------------- shared RAG-pipeline layout

def _rag_stage_labels():
    return ["DOCUMENT", "CHUNKS", "VECTORS (ChromaDB)", "RETRIEVED", "ANSWER"]


class _RagPipelineBase(Scene):
    """Shared stage layout for the broken/grounded pipeline pair."""

    def build_stage(self):
        self.camera.background_color = PALETTE["bg"]
        col_xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
        labels = _rag_stage_labels()
        header = VGroup()
        for x, lbl in zip(col_xs, labels):
            t = Text(lbl, color=PALETTE["slate"], font_size=17).move_to([x, 3.15, 0])
            header.add(t)
        self.play(FadeIn(header), run_time=0.6)
        return col_xs


# --------------------------------------------------------------------------- B05

class B05_RagPipelineBroken(_RagPipelineBase):
    def construct(self):
        col_xs = self.build_stage()
        title = title_card("First run — no embedding model wired")
        self.play(Write(title), run_time=0.8)

        doc = RoundedRectangle(width=1.3, height=1.7, corner_radius=0.08,
                                stroke_color=PALETTE["hair"], stroke_width=2,
                                fill_color=PALETTE["bg"]).move_to([col_xs[0], 0.6, 0])
        doc_lbl = Text("HR-handbook.pdf", color=PALETTE["slate"], font_size=16
                        ).next_to(doc, DOWN, buff=0.2)
        not_embedded = Text("NOT EMBEDDED", color=PALETTE["crimson"], font_size=16
                             ).next_to(doc_lbl, DOWN, buff=0.15)
        self.play(FadeIn(doc), Write(doc_lbl), run_time=0.7)
        self.play(Write(not_embedded), run_time=0.5)
        self.wait(0.4)

        gap = Text("no chunker · no vectors ·\nnothing here to search",
                    color=PALETTE["slate"], font_size=19).move_to([(col_xs[1] + col_xs[2]) / 2, 0.6, 0])
        self.play(FadeIn(gap, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)

        question = Circle(radius=0.5, color=PALETTE["ink"], fill_color=PALETTE["ink"],
                           fill_opacity=0.06).move_to([col_xs[3], 0.6, 0])
        q_mark = Text("?", color=PALETTE["ink"], font_size=40, weight=BOLD
                       ).move_to(question.get_center())
        q_text = Text("“what's the remote-work policy?”", color=PALETTE["ink"], font_size=17
                       ).next_to(question, DOWN, buff=0.3)
        self.play(FadeIn(question), FadeIn(q_mark), Write(q_text), run_time=0.7)

        badge = RoundedRectangle(width=2.6, height=0.7, corner_radius=0.1,
                                  color=PALETTE["crimson"], fill_color=PALETTE["crimson"],
                                  fill_opacity=0.08).move_to([col_xs[3], -0.9, 0])
        badge_txt = Text("0 chunks retrieved", color=PALETTE["crimson"], font_size=20
                          ).move_to(badge.get_center())
        self.play(Create(badge), Write(badge_txt), run_time=0.8)
        self.wait(0.5)

        answer = RoundedRectangle(width=3.0, height=1.6, corner_radius=0.12,
                                   stroke_color=PALETTE["ink"], stroke_width=2
                                   ).move_to([col_xs[4], 0.5, 0])
        answer_txt = Text("“Employees may\nwork remotely up\nto 3 days.”",
                           color=PALETTE["ink"], font_size=17).move_to(answer.get_center())
        warn = Text("fabricated —\nnot in source", color=PALETTE["crimson"], font_size=17
                     ).next_to(answer, DOWN, buff=0.25)
        self.play(FadeIn(answer), Write(answer_txt), run_time=0.8)
        self.play(Write(warn), run_time=0.6)
        self.wait(2.0)


# --------------------------------------------------------------------------- B08

class B08_RagPipelineGrounded(_RagPipelineBase):
    def construct(self):
        col_xs = self.build_stage()
        title = title_card("Same question, re-run — the embedder is wired")
        self.play(Write(title), run_time=0.8)

        doc = RoundedRectangle(width=1.3, height=1.7, corner_radius=0.08,
                                stroke_color=PALETTE["ink"], stroke_width=2,
                                fill_color=PALETTE["bg"]).move_to([col_xs[0], 0.6, 0])
        doc_lbl = Text("HR-handbook.pdf", color=PALETTE["ink"], font_size=16
                        ).next_to(doc, DOWN, buff=0.2)
        self.play(FadeIn(doc), Write(doc_lbl), run_time=0.6)

        chunk_starts = [doc.get_center() + UP * 0.35, doc.get_center(), doc.get_center() + DOWN * 0.35]
        chunks = VGroup(*[
            Rectangle(width=0.5, height=0.28, stroke_color=PALETTE["slate"], stroke_width=1.5,
                      fill_color=PALETTE["bg"]).move_to(p) for p in chunk_starts
        ])
        self.play(FadeIn(chunks), run_time=0.5)

        cluster_center = np.array([col_xs[2], 0.5, 0])
        vector_targets = [
            cluster_center + np.array([-0.5, 0.4, 0]),
            cluster_center + np.array([0.5, 0.5, 0]),
            cluster_center + np.array([0.0, -0.3, 0]),
        ]
        dots = VGroup(*[Dot(point=t, radius=0.09, color=PALETTE["ink"]) for t in vector_targets])
        cloud_lbl = Text("ChromaDB", color=PALETTE["slate"], font_size=16
                          ).move_to(cluster_center + UP * 1.0)
        self.play(
            *[Transform(c, d) for c, d in zip(chunks, dots)],
            FadeIn(cloud_lbl), run_time=1.1,
        )
        self.wait(0.3)

        question = Dot(point=[col_xs[3], 0.6, 0], radius=0.11, color=PALETTE["crimson"])
        q_text = Text("“what's the remote-work policy?”", color=PALETTE["ink"], font_size=17
                       ).next_to(question, UP, buff=0.35)
        self.play(FadeIn(question), Write(q_text), run_time=0.6)

        lines = VGroup(*[
            Line(question.get_center(), t, stroke_color=PALETTE["crimson"], stroke_width=2)
            for t in vector_targets
        ])
        self.play(*[Create(l) for l in lines], run_time=0.8)

        badge = RoundedRectangle(width=2.6, height=0.7, corner_radius=0.1,
                                  color=PALETTE["ink"], fill_color=PALETTE["ink"],
                                  fill_opacity=0.06).move_to([col_xs[3], -0.9, 0])
        badge_txt = Text("3 chunks retrieved", color=PALETTE["ink"], font_size=20
                          ).move_to(badge.get_center())
        self.play(Create(badge), Write(badge_txt), run_time=0.7)
        self.wait(0.4)

        answer = RoundedRectangle(width=3.0, height=1.8, corner_radius=0.12,
                                   stroke_color=PALETTE["ink"], stroke_width=2
                                   ).move_to([col_xs[4], 0.5, 0])
        answer_txt = Text("“Per §4.2: remote\nwork is approved\ncase-by-case with\nmanager sign-off.”",
                           color=PALETTE["ink"], font_size=15).move_to(answer.get_center())
        cite = Text("Source: HR Handbook §4.2", color=PALETTE["slate"], font_size=15
                     ).next_to(answer, DOWN, buff=0.25)
        self.play(FadeIn(answer), Write(answer_txt), run_time=0.9)
        self.play(Write(cite), run_time=0.6)
        self.wait(2.0)
