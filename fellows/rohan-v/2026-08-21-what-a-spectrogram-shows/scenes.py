"""Manim scenes for claude-hai-spectrogram. Cream / ink / one terracotta accent."""
from manim import *
import numpy as np

BG = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A7468"
ACCENT = "#D97757"


def hold():
    # Longer than narration; compile.py trims to the audio clock.
    return 18.0


class B01_Bluf(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("A map of energy.", color=INK, font_size=56, weight=BOLD)
        title.move_to(UP * 1.55)
        sub = Text(
            "Use it to see structure.\nNot to prove what the sound is.",
            color=SOFT,
            font_size=28,
            line_spacing=0.95,
        )
        sub.move_to(DOWN * 1.85)

        x_ax = Arrow(LEFT * 4.4 + DOWN * 0.05, RIGHT * 4.4 + DOWN * 0.05, color=INK, stroke_width=3, buff=0)
        y_ax = Arrow(LEFT * 4.4 + DOWN * 0.05, LEFT * 4.4 + UP * 2.55, color=INK, stroke_width=3, buff=0)

        self.play(FadeIn(title), run_time=0.7)
        self.play(Create(x_ax), Create(y_ax), run_time=0.9)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(hold())


class B02_Waveform(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("A waveform is not enough.", color=INK, font_size=44, weight=BOLD)
        title.to_edge(UP, buff=0.42)

        ax = Axes(
            x_range=[0, 8, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=10.4,
            y_length=3.4,
            axis_config={"color": INK, "stroke_width": 3, "include_ticks": False, "include_tip": True},
        ).move_to(DOWN * 0.15)
        wave = ax.plot(lambda t: 0.72 * np.sin(1.6 * t) * np.exp(-0.04 * t), color=ACCENT, stroke_width=6)
        xlab = Text("time", color=INK, font_size=26).next_to(ax, DOWN, buff=0.28)
        ylab = Text("air pressure", color=INK, font_size=26).rotate(PI / 2).next_to(ax, LEFT, buff=0.22)
        note = Text("loud and quiet  —  not which pitches", color=SOFT, font_size=26)
        note.to_edge(DOWN, buff=0.38)

        self.play(FadeIn(title), run_time=0.45)
        self.play(Create(ax), FadeIn(xlab), FadeIn(ylab), run_time=0.8)
        self.play(Create(wave), run_time=1.2)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(hold())


class B04_Result(Scene):
    def construct(self):
        self.camera.background_color = BG
        cols, rows = 18, 10
        w, h = 0.42, 0.32
        origin = LEFT * 3.6 + DOWN * 2.1

        x_ax = Arrow(origin + LEFT * 0.15, origin + RIGHT * (cols * w + 0.8), color=INK, stroke_width=3, buff=0)
        y_ax = Arrow(origin + DOWN * 0.15, origin + UP * (rows * h + 0.7), color=INK, stroke_width=3, buff=0)
        xlab = Text("time", color=INK, font_size=26).next_to(x_ax, DOWN, buff=0.28)
        ylab = Text("frequency", color=INK, font_size=26).rotate(PI / 2).next_to(y_ax, LEFT, buff=0.28)

        self.play(Create(x_ax), FadeIn(xlab), run_time=0.6)
        self.play(Create(y_ax), FadeIn(ylab), run_time=0.6)

        cells = VGroup()
        band_row = 6
        for i in range(cols):
            for j in range(rows):
                if j == band_row:
                    op, col = 0.92, ACCENT
                elif abs(j - band_row) == 1:
                    op, col = 0.28, INK
                else:
                    op = 0.08 + 0.07 * ((i * 3 + j * 5) % 4 == 0)
                    col = INK
                sq = Square(side_length=min(w, h) * 0.88, stroke_width=0)
                sq.set_fill(col, opacity=max(0.06, op))
                sq.move_to(origin + RIGHT * ((i + 0.5) * w) + UP * ((j + 0.5) * h))
                cells.add(sq)

        self.play(FadeIn(cells), run_time=1.1)
        note = Text("sung ah  —  a band", color=ACCENT, font_size=28)
        note.to_edge(UP, buff=0.45)
        noise = Text("noise  —  speckle, no pitch to hold", color=SOFT, font_size=24)
        noise.next_to(note, DOWN, buff=0.22)
        self.play(FadeIn(note), run_time=0.5)
        self.play(FadeIn(noise), run_time=0.4)
        self.wait(hold())


class B05_Harmonics(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("A sung ah is a stack.", color=INK, font_size=44, weight=BOLD)
        title.to_edge(UP, buff=0.4)

        cols, rows = 16, 11
        w, h = 0.46, 0.28
        origin = LEFT * 3.7 + DOWN * 2.35
        x_ax = Arrow(origin, origin + RIGHT * (cols * w + 0.5), color=INK, stroke_width=3, buff=0)
        y_ax = Arrow(origin, origin + UP * (rows * h + 0.45), color=INK, stroke_width=3, buff=0)
        self.play(FadeIn(title), Create(x_ax), Create(y_ax), run_time=0.7)

        harmonics = {2: 0.95, 4: 0.55, 6: 0.32, 8: 0.18}
        cells = VGroup()
        for i in range(cols):
            for j in range(rows):
                op = 0.06
                col = INK
                if j in harmonics:
                    op = harmonics[j]
                    col = ACCENT if j == 2 else INK
                sq = Square(side_length=min(w, h) * 0.86, stroke_width=0)
                sq.set_fill(col, opacity=op)
                sq.move_to(origin + RIGHT * ((i + 0.5) * w) + UP * ((j + 0.5) * h))
                cells.add(sq)
        self.play(FadeIn(cells), run_time=0.9)

        labels = VGroup(
            Text("lowest band", color=ACCENT, font_size=24).move_to(RIGHT * 4.55 + DOWN * 1.35),
            Text("harmonics", color=SOFT, font_size=24).move_to(RIGHT * 4.45 + UP * 0.35),
            Text("Brightness is energy, not correctness.", color=SOFT, font_size=26).to_edge(DOWN, buff=0.36),
        )
        self.play(FadeIn(labels), run_time=0.5)
        self.wait(hold())


class B06_Window(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("The window is a trade.", color=INK, font_size=44, weight=BOLD)
        title.to_edge(UP, buff=0.38)

        def grid(sharp_time, label, origin):
            cols, rows = 9, 8
            w, h = 0.38, 0.30
            cells = VGroup()
            for i in range(cols):
                for j in range(rows):
                    if sharp_time:
                        on = (i in (2, 3)) and (4 <= j <= 6)
                        op = 0.85 if on else 0.08
                    else:
                        on = (j == 5)
                        op = 0.85 if on else 0.08
                    sq = Square(side_length=min(w, h) * 0.84, stroke_width=0)
                    sq.set_fill(ACCENT if on else INK, opacity=op)
                    sq.move_to(origin + RIGHT * ((i + 0.5) * w) + UP * ((j + 0.5) * h))
                    cells.add(sq)
            cap = Text(label, color=INK, font_size=24)
            cap.next_to(cells, DOWN, buff=0.28)
            return VGroup(cells, cap)

        left = grid(True, "short window  —  sharp in time", LEFT * 3.4 + DOWN * 1.2)
        right = grid(False, "long window  —  sharp in pitch", RIGHT * 0.55 + DOWN * 1.2)
        foot = Text("You cannot have both at once.", color=SOFT, font_size=26)
        foot.to_edge(DOWN, buff=0.32)

        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(left), run_time=0.7)
        self.play(FadeIn(right), run_time=0.7)
        self.play(FadeIn(foot), run_time=0.4)
        self.wait(hold())


class B07_Hides(Scene):
    def construct(self):
        self.camera.background_color = BG
        header = Text("What it hides.", color=INK, font_size=44, weight=BOLD)
        header.to_edge(UP, buff=0.42)

        def card(title, sub, accent=False):
            box = RoundedRectangle(
                corner_radius=0.12, width=10.8, height=1.32,
                fill_color=WHITE, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
            )
            rail = Rectangle(width=0.12, height=1.32, stroke_width=0)
            rail.set_fill(ACCENT if accent else INK, 1)
            rail.align_to(box, LEFT)
            t = Text(title, color=INK, font_size=32, weight=BOLD)
            s = Text(sub, color=SOFT, font_size=22)
            t.move_to(box.get_center() + UP * 0.22 + RIGHT * 0.18)
            s.move_to(box.get_center() + DOWN * 0.28 + RIGHT * 0.18)
            return VGroup(box, rail, t, s)

        c1 = card("Phase", "Same picture. Air can still cancel.", accent=True)
        c2 = card("Overlap", "Two voices smear into one stain.", accent=False)
        c3 = card("Floor", "Quiet consonants drop out.", accent=False)
        stack = VGroup(c1, c2, c3).arrange(DOWN, buff=0.26)
        stack.move_to(DOWN * 0.12)
        foot = Text("Find a note. Do not certify the mix.", color=SOFT, font_size=24)
        foot.to_edge(DOWN, buff=0.34)

        self.play(FadeIn(header), run_time=0.4)
        self.play(FadeIn(c1), run_time=0.45)
        self.play(FadeIn(c2), run_time=0.4)
        self.play(FadeIn(c3), run_time=0.4)
        self.play(FadeIn(foot), run_time=0.4)
        self.wait(hold())


class B08_Use(Scene):
    def construct(self):
        self.camera.background_color = BG
        header = Text("The split.", color=INK, font_size=48, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        def col(title, lines, accent=False):
            box = RoundedRectangle(
                corner_radius=0.14, width=6.3, height=5.1,
                fill_color=WHITE, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
            )
            rail = Rectangle(width=6.3, height=0.12, stroke_width=0)
            rail.set_fill(ACCENT if accent else INK, 1)
            rail.align_to(box, UP)
            t = Text(title, color=INK, font_size=32, weight=BOLD)
            t.next_to(rail, DOWN, buff=0.32)
            body = VGroup(*[Text(ln, color=SOFT, font_size=22) for ln in lines])
            body.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
            body.next_to(t, DOWN, buff=0.4, aligned_edge=LEFT)
            g = VGroup(box, rail, t, body)
            t.align_to(box, LEFT).shift(RIGHT * 0.4)
            body.align_to(t, LEFT)
            return g

        left = col("Use it to find", ["a note", "a breath", "a cut", "a buzz", "a dropout"], accent=True)
        right = col("Do not hand it", ["a clean mix", "isolated stems", "understood lyrics"], accent=False)
        row = VGroup(left, right).arrange(RIGHT, buff=0.45)
        row.move_to(DOWN * 0.25)

        self.play(FadeIn(header), run_time=0.4)
        self.play(FadeIn(left), run_time=0.6)
        self.play(FadeIn(right), run_time=0.6)
        self.wait(hold())
