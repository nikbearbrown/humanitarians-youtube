"""
Manim scenes for examples/ecis (ECIS — The Honest Scorecard)
B03_ArchitectureFlow — transcript -> four parallel readers -> triangulator -> signal
B04_RoutingTree      — chunks -> orchestrator -> A/B/C/D branches, D dissolves, counter ticks
Claude fidelity palette (cream ground) per PEDAGOGY.md — only B01/B02/B05/B06
(Remotion beats) carry the approved dark-stage deviation; these two Manim
beats stay on-brand.
"""

from manim import *

PALETTE = {
    "bg":     "#FAF9F5",
    "ink":    "#3D3929",
    "line":   "#9B8EAA",
    "accent": "#D97757",
    "keyword": "#3E7CB1",
    "finbert": "#2E9E8F",
    "ner":     "#D98E3E",
    "llm":     "#7A5FB5",
    "green":   "#4A7C59",
    "amber":   "#D9A757",
    "red":     "#C0392B",
    "grey":    "#8A8578",
}


class B03_ArchitectureFlow(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Four-Reader Triangulation", color=PALETTE["ink"], font_size=30).to_edge(UP, buff=0.4)
        self.add(title)

        # -- transcript -> chunks (0.0) --
        doc = RoundedRectangle(corner_radius=0.08, width=1.0, height=1.3,
                                fill_color=PALETTE["ink"], fill_opacity=0.08,
                                stroke_color=PALETTE["ink"], stroke_width=2).move_to([-6.2, 0, 0])
        doc_label = Text("Transcript", color=PALETTE["ink"], font_size=16).next_to(doc, DOWN, buff=0.15)
        self.play(Create(doc), Write(doc_label), run_time=2.01)

        chunks = VGroup(*[
            Rectangle(width=0.5, height=0.35, fill_color=PALETTE["ink"], fill_opacity=0.12,
                      stroke_color=PALETTE["ink"], stroke_width=1.5)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.12).move_to([-4.5, 0, 0])
        self.play(*[TransformFromCopy(doc, c) for c in chunks], run_time=2.01)

        # -- four reader nodes draw in on their narration cue (0.15 / 0.30 / 0.42 / 0.55) --
        readers = [
            ("Keyword\nscanner", PALETTE["keyword"], 2.4),
            ("FinBERT", PALETTE["finbert"], 0.8),
            ("Named-entity\nmodel", PALETTE["ner"], -0.8),
            ("Language\nmodel", PALETTE["llm"], -2.4),
        ]
        nodes = VGroup()
        arrows_in = VGroup()
        for label, color, y in readers:
            node = RoundedRectangle(corner_radius=0.08, width=2.0, height=0.9,
                                     fill_color=color, fill_opacity=0.15,
                                     stroke_color=color, stroke_width=2.5).move_to([-1.2, y, 0])
            node_label = Text(label, color=PALETTE["ink"], font_size=16, line_spacing=0.9).move_to(node)
            arrow = Arrow(chunks.get_right(), [-1.2, y, 0] + LEFT * 1.0,
                          buff=0.15, color=PALETTE["line"], stroke_width=2)
            nodes.add(VGroup(node, node_label))
            arrows_in.add(arrow)

        for i, ((label, color, y), grp, arrow) in enumerate(zip(readers, nodes, arrows_in)):
            self.play(GrowArrow(arrow), FadeIn(grp, shift=RIGHT * 0.2), run_time=2.15)
            if label == "Language\nmodel":
                subs = VGroup(*[
                    Text(t, color=PALETTE["llm"], font_size=13)
                    for t in ["Chain-of-thought", "Self-consistency (3 passes)", "Verification"]
                ]).arrange(DOWN, buff=0.08).next_to(grp, DOWN, buff=0.15)
                self.play(FadeIn(subs, shift=DOWN * 0.1), run_time=1.44)
                self.play(FadeOut(subs), run_time=1.00)

        # -- triangulator + weighted convergence (0.86) --
        tri = RegularPolygon(n=4, color=PALETTE["accent"], fill_color=PALETTE["accent"],
                              fill_opacity=0.18, stroke_width=3).scale(0.9).rotate(PI / 4).move_to([2.2, 0, 0])
        tri_label = Text("Triangulator", color=PALETTE["ink"], font_size=17).move_to(tri)
        self.play(Create(tri), Write(tri_label), run_time=1.44)

        # weight order matches `readers`: keyword, FinBERT, NER, LLM
        weights = [0.15, 0.20, 0.15, 0.50]
        conv_arrows = VGroup()
        for i, ((label, color, y), w) in enumerate(zip(readers, weights)):
            a = Arrow(nodes[i].get_right(), tri.get_left() + UP * (y * 0.15),
                      buff=0.1, color=color, stroke_width=1 + 6 * w)
            conv_arrows.add(a)
        self.play(*[GrowArrow(a) for a in conv_arrows], run_time=2.30)

        out = RoundedRectangle(corner_radius=0.08, width=2.6, height=1.1,
                                fill_color=PALETTE["green"], fill_opacity=0.15,
                                stroke_color=PALETTE["green"], stroke_width=2.5).move_to([5.5, 0, 0])
        out_label = Text("direction: raised\nconfidence: 0.87", color=PALETTE["ink"],
                          font_size=16, line_spacing=1.0).move_to(out)
        out_arrow = Arrow(tri.get_right(), out.get_left(), buff=0.1, color=PALETTE["accent"], stroke_width=3)
        self.play(GrowArrow(out_arrow), FadeIn(out, shift=RIGHT * 0.2), Write(out_label), run_time=2.58)

        self.wait(2.87)


class B04_RoutingTree(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Four-Way Routing", color=PALETTE["ink"], font_size=30).to_edge(UP, buff=0.4)
        self.add(title)

        orch = RoundedRectangle(corner_radius=0.1, width=2.6, height=1.0,
                                 fill_color=PALETTE["ink"], fill_opacity=0.1,
                                 stroke_color=PALETTE["ink"], stroke_width=2.5).move_to([0, 2.3, 0])
        orch_label = Text("Orchestrator", color=PALETTE["ink"], font_size=18).move_to(orch)
        self.play(Create(orch), Write(orch_label), run_time=2.23)

        chunk_row = VGroup(*[
            Rectangle(width=0.4, height=0.3, fill_color=PALETTE["ink"], fill_opacity=0.15,
                      stroke_color=PALETTE["ink"], stroke_width=1.2)
            for _ in range(6)
        ]).arrange(RIGHT, buff=0.15).next_to(orch, UP, buff=0.4)
        self.play(FadeIn(chunk_row, shift=DOWN * 0.3), run_time=2.23)
        self.play(chunk_row.animate.next_to(orch, UP, buff=0.05).set_opacity(0), run_time=1.86)

        branches = [
            ("A", "LLM\nconfirm", PALETTE["green"], -4.8),
            ("B", "Full\npipeline", PALETTE["amber"], -1.6),
            ("C", "Conflict\nresolution", PALETTE["red"], 1.6),
            ("D", "skipped", PALETTE["grey"], 4.8),
        ]
        boxes = VGroup()
        labels = VGroup()
        lines = VGroup()
        for tag, dest, color, x in branches:
            box = RoundedRectangle(corner_radius=0.08, width=2.4, height=1.0,
                                    fill_color=color, fill_opacity=0.15,
                                    stroke_color=color, stroke_width=2.5).move_to([x, -1.2, 0])
            lab = Text(dest, color=PALETTE["ink"], font_size=16, line_spacing=0.9).move_to(box)
            tag_lab = Text(tag, color=color, font_size=22, weight=BOLD).next_to(box, UP, buff=0.12)
            line = Line(orch.get_bottom(), box.get_top(), color=color, stroke_width=2)
            boxes.add(box); labels.add(lab); lines.add(tag_lab)
            self.play(Create(line), FadeIn(box, shift=DOWN * 0.2), Write(lab), Write(tag_lab), run_time=2.60)

        d_box, d_lab = boxes[3], labels[3]
        d_tag = lines[3]
        self.play(FadeOut(d_box), FadeOut(d_lab), d_tag.animate.set_opacity(0.35), run_time=2.23)

        counter_bg = RoundedRectangle(corner_radius=0.1, width=4.6, height=0.9,
                                       fill_color=PALETTE["accent"], fill_opacity=0.12,
                                       stroke_color=PALETTE["accent"], stroke_width=2).move_to([4.8, -3.0, 0])
        counter = Text("LLM calls saved: 0%", color=PALETTE["accent"], font_size=20).move_to(counter_bg)
        self.play(FadeIn(counter_bg), Write(counter), run_time=1.48)
        for pct in (20, 40, 60, 80):
            new_counter = Text(f"LLM calls saved: {pct}%", color=PALETTE["accent"], font_size=20).move_to(counter_bg)
            self.play(Transform(counter, new_counter), run_time=0.65)

        self.wait(3.71)
