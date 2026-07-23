from manim import *
import numpy as np

BG = ManimColor("#FAF9F5")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")
GREEN = ManimColor("#4A7C59")


def source_credit():
    return Text(
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 11",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


MODELS = [
    {"name": "A", "acc": 94, "lat": 80, "flash": 4000},
    {"name": "B", "acc": 92, "lat": 40, "flash": 1500},
    {"name": "C", "acc": 91, "lat": 20, "flash": 800},
    {"name": "D", "acc": 90, "lat": 60, "flash": 1200},
    {"name": "E", "acc": 89, "lat": 15, "flash": 600},
]


class B01_ScatterPlot(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Model Field: Accuracy vs Latency", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[85, 97, 2],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)
        x_label = Text("latency (ms) — lower is better →", font_size=13, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("accuracy (%)", font_size=13, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        for m in MODELS:
            dot = Dot(axes.c2p(m["lat"], m["acc"]), color=INK, radius=0.1)
            lbl = Text(f"Model {m['name']}", font_size=13, color=INK).next_to(dot, UR, buff=0.12)
            self.play(FadeIn(dot), FadeIn(lbl), run_time=0.5)

        subtitle = Text("All models on the board — now find who wins", font_size=15, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(subtitle))
        self.wait(1.5)


class B02_DominatedFade(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Dominated Models Grey Out", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[85, 97, 2],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)
        x_label = Text("latency (ms)", font_size=13, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("accuracy (%)", font_size=13, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        dots = {}
        labels = {}
        for m in MODELS:
            dot = Dot(axes.c2p(m["lat"], m["acc"]), color=INK, radius=0.1)
            lbl = Text(f"Model {m['name']}", font_size=13, color=INK).next_to(dot, UR, buff=0.12)
            self.add(dot, lbl)
            dots[m["name"]] = dot
            labels[m["name"]] = lbl

        # Model A is dominated: B has lower latency (40 < 80) at nearly the same accuracy (92 vs 94)
        # Model D is dominated: B has lower latency AND higher accuracy
        dominated = ["A", "D"]
        for name in dominated:
            self.play(
                dots[name].animate.set_color(GHOST).set_opacity(0.3),
                labels[name].animate.set_color(GHOST).set_opacity(0.3),
                run_time=0.8
            )

        dom_note = Text("Model A: dominated by B (lower latency, similar accuracy)", font_size=13, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(dom_note))
        self.wait(1.5)


class B03_ParetoFrontier(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Pareto Frontier — Honest Shortlist", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[85, 97, 2],
            x_length=8,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.3)
        x_label = Text("latency (ms)", font_size=13, color=SOFT).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("accuracy (%)", font_size=13, color=SOFT).next_to(axes.y_axis, LEFT, buff=0.1).rotate(PI / 2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # All models, dominated ones greyed
        for m in MODELS:
            dominated = m["name"] in ["A", "D"]
            col = GHOST if dominated else INK
            opacity = 0.3 if dominated else 1.0
            dot = Dot(axes.c2p(m["lat"], m["acc"]), color=col, radius=0.1, fill_opacity=opacity)
            lbl = Text(f"{m['name']}", font_size=12, color=col).next_to(dot, UR, buff=0.1)
            lbl.set_opacity(opacity)
            self.add(dot, lbl)

        # Pareto frontier: B(40, 92), C(20, 91), E(15, 89) — sorted by latency
        pareto = [m for m in MODELS if m["name"] in ["B", "C", "E"]]
        pareto_sorted = sorted(pareto, key=lambda m: m["lat"])

        frontier_pts = [axes.c2p(m["lat"], m["acc"]) for m in pareto_sorted]
        frontier_line = VMobject()
        frontier_line.set_points_as_corners(frontier_pts)
        frontier_line.set_stroke(color=ACC, width=3)

        for m in pareto_sorted:
            dot = Dot(axes.c2p(m["lat"], m["acc"]), color=ACC, radius=0.12)
            lbl = Text(f"Model {m['name']}", font_size=13, color=ACC).next_to(dot, UR, buff=0.12)
            self.add(dot, lbl)

        self.play(Create(frontier_line), run_time=1.5)

        frontier_label = Text("Pareto frontier — nothing beats these on all axes", font_size=14, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(frontier_label))
        self.wait(1.5)
