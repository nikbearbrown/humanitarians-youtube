"""
Manim scenes for claude-liam-nearest-neighbor ("Claude, Nearest.")
B01_BLUF         — the one-breath executive summary, text only
B02_Framework    — a 2D toy embedding space; similar meaning clusters together
B03_Query        — a query point; nearest neighbors are just the closest dots
B04_BruteVsANN   — brute-force scan vs a graph hop toward the neighborhood
B05_Recall       — falsifiability: approximate search can miss the true neighbor
"""

from manim import *
import numpy as np

INK = "#3D3929"
BG = "#FAF9F5"
ACCENT = "#D97757"
BLUE = "#5B7B9C"
GREEN = "#4A7C59"
RED = "#C0392B"

config.background_color = BG


class B01_BLUF(Scene):
    def construct(self):
        l1 = Text("An embedding model turns text into a vector.",
                   font_size=38, color=INK)
        l2 = Text("Train it so similar meaning lands close together.",
                   font_size=38, color=INK)
        l3 = Text("Then 'search' becomes 'find the nearest points.'",
                   font_size=36, color=ACCENT)
        for _l in (l1, l2, l3):
            if _l.width > 12.0:
                _l.scale_to_fit_width(12.0)
        l1.move_to(UP * 1.3)
        l2.move_to(UP * 0.1)
        l3.move_to(DOWN * 1.1)
        self.play(Write(l1), run_time=1.4)
        self.play(Write(l2), run_time=1.4)
        self.play(Write(l3), run_time=1.2)
        self.wait(1.2)


class B02_Framework(Scene):
    def construct(self):
        title = Text("A 2D map of meaning", font_size=34, color=INK).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        animals = {"dog": (-3.2, 1.0), "puppy": (-2.6, 1.6), "cat": (-3.6, 0.2), "kitten": (-2.9, 0.4)}
        vehicles = {"car": (2.6, -0.8), "truck": (3.4, -0.3), "van": (2.9, -1.4)}
        dots = VGroup()
        for word, (x, y) in {**animals, **vehicles}.items():
            color = BLUE if word in animals else GREEN
            p = np.array([x, y, 0])
            dot = Dot(p, radius=0.09, color=color)
            lbl = Text(word, font_size=22, color=color).next_to(dot, UP, buff=0.12)
            dots.add(VGroup(dot, lbl))
        self.play(*[FadeIn(d, scale=0.6) for d in dots], run_time=1.4)

        near1 = Line(np.array([-3.2, 1.0, 0]), np.array([-2.6, 1.6, 0]), color=BLUE, stroke_width=3)
        near2 = Line(np.array([2.6, -0.8, 0]), np.array([3.4, -0.3, 0]), color=GREEN, stroke_width=3)
        self.play(Create(near1), Create(near2), run_time=0.9)

        cap = Text("Distance on this map IS semantic similarity.",
                    font_size=26, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.3)


class B03_Query(Scene):
    def construct(self):
        title = Text("Nearest neighbors: just the closest dots", font_size=30, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        points = {"dog": (-2.4, 0.8), "cat": (-1.9, -0.2), "car": (2.8, 0.3), "truck": (3.3, -0.6)}
        dots = VGroup()
        for word, (x, y) in points.items():
            p = np.array([x, y, 0])
            dot = Dot(p, radius=0.09, color=BLUE)
            lbl = Text(word, font_size=22, color=BLUE).next_to(dot, UP, buff=0.1)
            dots.add(VGroup(dot, lbl))
        self.play(*[FadeIn(d) for d in dots], run_time=0.8)

        q = np.array([-2.1, 0.2, 0])
        q_dot = Dot(q, radius=0.13, color=ACCENT)
        q_lbl = Text("query: 'puppy'", font_size=24, color=ACCENT).next_to(q_dot, RIGHT, buff=0.3)
        self.play(FadeIn(q_dot, scale=0.5), FadeIn(q_lbl), run_time=0.8)

        for word, (x, y) in list(points.items())[:2]:
            p = np.array([x, y, 0])
            line = Line(q, p, color=ACCENT, stroke_width=3)
            self.play(Create(line), run_time=0.5)

        cap = Text("No shared letters with 'dog' or 'cat' — just proximity.",
                    font_size=24, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.3)


class B04_BruteVsANN(Scene):
    def construct(self):
        title = Text("Brute-force vs. a graph hop", font_size=32, color=INK).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        left_label = Text("brute-force: check everything", font_size=22, color=RED)
        left_label.move_to(LEFT * 3.3 + UP * 1.6)
        right_label = Text("ANN: hop through a few edges", font_size=22, color=GREEN)
        right_label.move_to(RIGHT * 3.3 + UP * 1.6)
        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.6)

        rng_pts = [LEFT * 3.3 + np.array([np.cos(a), np.sin(a), 0]) * 1.3
                   for a in np.linspace(0, 2 * PI, 10, endpoint=False)]
        query_l = LEFT * 3.3
        dots_l = VGroup(*[Dot(p, radius=0.07, color=RED) for p in rng_pts])
        q_l = Dot(query_l, radius=0.1, color=ACCENT)
        self.play(FadeIn(dots_l), FadeIn(q_l), run_time=0.5)
        lines_l = VGroup(*[Line(query_l, p, color=RED, stroke_width=1.5) for p in rng_pts])
        self.play(Create(lines_l), run_time=1.0)

        rng_pts_r = [RIGHT * 3.3 + np.array([np.cos(a), np.sin(a), 0]) * 1.3
                     for a in np.linspace(0, 2 * PI, 10, endpoint=False)]
        query_r = RIGHT * 3.3
        dots_r = VGroup(*[Dot(p, radius=0.07, color=GREEN) for p in rng_pts_r])
        q_r = Dot(query_r, radius=0.1, color=ACCENT)
        self.play(FadeIn(dots_r), FadeIn(q_r), run_time=0.5)
        hop_path = [query_r, rng_pts_r[0], rng_pts_r[1], rng_pts_r[2]]
        hop_lines = VGroup(*[Line(hop_path[i], hop_path[i + 1], color=GREEN, stroke_width=4)
                              for i in range(len(hop_path) - 1)])
        self.play(Create(hop_lines), run_time=1.0)

        cap = Text("A few hops toward the neighborhood — skip almost everything.",
                    font_size=24, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.3)


class B05_Recall(Scene):
    def construct(self):
        title = Text("Approximate means it can miss", font_size=32, color=INK).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        q = LEFT * 0.0 + UP * 0.6
        true_nn = q + LEFT * 1.6 + DOWN * 0.3
        approx_nn = q + RIGHT * 1.9 + DOWN * 0.6

        q_dot = Dot(q, radius=0.11, color=ACCENT)
        q_lbl = Text("query", font_size=22, color=ACCENT).next_to(q_dot, UP, buff=0.1)
        true_dot = Dot(true_nn, radius=0.09, color=GREEN)
        true_lbl = Text("true nearest", font_size=20, color=GREEN).next_to(true_dot, DOWN, buff=0.1)
        approx_dot = Dot(approx_nn, radius=0.09, color=RED)
        approx_lbl = Text("what the index returned", font_size=20, color=RED).next_to(approx_dot, DOWN, buff=0.1)

        self.play(FadeIn(VGroup(q_dot, q_lbl)), run_time=0.5)
        self.play(FadeIn(VGroup(true_dot, true_lbl)), run_time=0.5)
        true_line = DashedLine(q, true_nn, color=GREEN, stroke_width=2)
        self.play(Create(true_line), run_time=0.5)

        self.play(FadeIn(VGroup(approx_dot, approx_lbl)), run_time=0.5)
        approx_line = Line(q, approx_nn, color=RED, stroke_width=3)
        self.play(Create(approx_line), run_time=0.5)

        cap = Text("Faster search costs recall — tune how much graph you explore.",
                    font_size=24, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.4)
