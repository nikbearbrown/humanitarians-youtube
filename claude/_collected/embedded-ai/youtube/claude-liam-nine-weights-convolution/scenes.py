"""scenes.py — Manim for claude-liam-nine-weights-convolution. Source: embedded-ai Ch. 03"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_DenseGrid(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Fully Connected: 19.3M Weights", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Represent image as a tall rectangle
        img_box = Rectangle(width=1.4, height=3.5, color=SOFT, fill_color=SOFT, fill_opacity=0.25, stroke_width=2)
        img_box.move_to([-4.0, -0.2, 0])
        img_label = Text("224×224×3\n150,528 inputs", font_size=14, color=INK)
        img_label.next_to(img_box, DOWN, buff=0.2)

        # Represent 128 neurons as small circles
        neuron_x = 2.5
        n_shown = 8
        neurons = VGroup(*[
            Circle(radius=0.18, color=INK, stroke_width=1.5)
            for _ in range(n_shown)
        ]).arrange(DOWN, buff=0.22)
        neurons.move_to([neuron_x, -0.2, 0])
        neuron_label = Text("128 neurons", font_size=14, color=INK)
        neuron_label.next_to(neurons, DOWN, buff=0.2)

        self.play(FadeIn(img_box), FadeIn(img_label))
        self.play(FadeIn(neurons), FadeIn(neuron_label))

        # Draw a few representative connections
        lines = VGroup()
        for i in range(0, n_shown, 2):
            for j_offset in [-0.5, 0, 0.5]:
                start = img_box.get_right() + UP * j_offset
                end   = neurons[i].get_left()
                line  = Line(start, end, stroke_width=0.4, color=GHOST)
                lines.add(line)
        self.play(Create(lines), run_time=0.8)

        # Counter
        counter = Text("19,267,584 weights", font_size=20, color=ACC)
        counter.move_to([0, -2.8, 0])
        self.play(FadeIn(counter))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 03", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_FilterSlide(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Convolution: 9 Shared Weights", font_size=26, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Small 6×6 image grid
        grid_size = 6
        cell_size = 0.55
        grid = VGroup()
        cells = {}
        for r in range(grid_size):
            for c in range(grid_size):
                sq = Square(side_length=cell_size, color=GHOST, stroke_width=1, fill_opacity=0)
                sq.move_to([-1.5 + c * cell_size, 1.0 - r * cell_size, 0])
                grid.add(sq)
                cells[(r, c)] = sq
        self.play(Create(grid), run_time=0.5)

        # 3×3 filter highlight box
        def filter_highlight(r0, c0):
            box = Rectangle(
                width=3 * cell_size + 0.04,
                height=3 * cell_size + 0.04,
                color=ACC, stroke_width=3, fill_opacity=0
            )
            box.move_to(cells[(r0, c0)].get_center() + RIGHT * cell_size + DOWN * cell_size)
            return box

        fh = filter_highlight(0, 0)
        self.play(FadeIn(fh))

        # Weight labels inside filter
        weight_labels = VGroup(*[
            Text(f"w{i+1}", font_size=12, color=ACC)
            for i in range(9)
        ])
        for idx, (dr, dc) in enumerate([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]):
            weight_labels[idx].move_to(cells[(dr, dc)].get_center())
        self.play(FadeIn(weight_labels))

        # Slide filter across — 3 positions
        positions = [(0, 0), (0, 2), (1, 1), (2, 2)]
        for r0, c0 in positions[1:]:
            new_fh = filter_highlight(r0, c0)
            new_wl = VGroup(*[
                Text(f"w{i+1}", font_size=12, color=ACC)
                for i in range(9)
            ])
            for idx, (dr, dc) in enumerate([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]):
                new_wl[idx].move_to(cells[(r0+dr, c0+dc)].get_center())
            self.play(
                Transform(fh, new_fh),
                Transform(weight_labels, new_wl),
                run_time=0.6
            )

        note = Text("Same 9 weights — every position", font_size=17, color=INK)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 03", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_Comparison(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Parameter Count", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        max_h = 4.0
        bar_w = 1.4
        spacing = 3.0

        # Dense bar — full height
        bar_dense = Rectangle(width=bar_w, height=max_h, fill_color=SOFT, fill_opacity=0.6, stroke_width=0)
        bar_dense.move_to([-spacing/2, max_h/2 - 2.2, 0])

        # Conv bar — tiny
        conv_h = max_h * (9 / 19_267_584)  # essentially 0, clamp to visible
        conv_h_visible = max(conv_h * 1000, 0.05)  # make visible
        bar_conv = Rectangle(width=bar_w, height=conv_h_visible, fill_color=ACC, fill_opacity=0.95, stroke_width=0)
        bar_conv.move_to([spacing/2, conv_h_visible/2 - 2.2, 0])

        lbl_dense = Text("19.3M\n(fully connected)", font_size=15, color=INK)
        lbl_dense.next_to(bar_dense, DOWN, buff=0.15)

        lbl_conv = Text("9\n(3×3 conv)", font_size=15, color=INK)
        lbl_conv.next_to(bar_conv, DOWN, buff=0.15)

        self.play(GrowFromEdge(bar_dense, DOWN), run_time=0.7)
        self.play(GrowFromEdge(bar_conv, DOWN), run_time=0.4)
        self.play(FadeIn(lbl_dense), FadeIn(lbl_conv))

        note = Text("6 orders of magnitude", font_size=18, color=ACC)
        note.move_to([0, 2.0, 0])
        self.play(FadeIn(note))

        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 03", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
