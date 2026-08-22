"""Manim scenes for claude-hai-nyquist. Cream / ink / one terracotta accent."""
from manim import *
import numpy as np

BG = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A7468"
ACCENT = "#D97757"


def hold():
    return 18.0


class B01_Bluf(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Two numbers, one trap.", color=INK, font_size=52, weight=BOLD)
        title.move_to(UP * 1.7)
        line = Text(
            "Sample rate is how often you measure.\nNyquist is the highest pitch those\nmeasurements can uniquely catch.",
            color=SOFT,
            font_size=28,
            line_spacing=0.95,
        )
        line.move_to(DOWN * 0.55)
        foot = Text("Go faster than twice the highest cycle  —  or the picture lies.", color=INK, font_size=24)
        foot.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(title), run_time=0.55)
        self.play(FadeIn(line), run_time=0.7)
        self.play(FadeIn(foot), run_time=0.45)
        self.wait(hold())


class B02_Snapshots(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Sampling is snapshots.", color=INK, font_size=44, weight=BOLD)
        title.to_edge(UP, buff=0.4)

        ax = Axes(
            x_range=[0, 8.2, 1],
            y_range=[-1.35, 1.35, 1],
            x_length=10.6,
            y_length=3.5,
            axis_config={"color": INK, "stroke_width": 3, "include_ticks": False, "include_tip": True},
        ).move_to(DOWN * 0.05)
        wave = ax.plot(lambda t: np.sin(1.35 * t), color=INK, stroke_width=4)
        xs = np.arange(0.4, 8.0, 0.85)
        dots = VGroup(*[
            Dot(ax.c2p(x, np.sin(1.35 * x)), color=ACCENT, radius=0.11)
            for x in xs
        ])
        xlab = Text("time", color=INK, font_size=26).next_to(ax, DOWN, buff=0.22)
        note = Text("Each dot is one measurement of air pressure.", color=SOFT, font_size=26)
        note.to_edge(DOWN, buff=0.34)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(ax), FadeIn(xlab), Create(wave), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.12), run_time=1.2)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(hold())


class B04_Enough(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Enough dots reconstruct the wiggle.", color=INK, font_size=40, weight=BOLD)
        title.to_edge(UP, buff=0.38)

        ax = Axes(
            x_range=[0, 8.2, 1],
            y_range=[-1.35, 1.35, 1],
            x_length=10.6,
            y_length=3.4,
            axis_config={"color": INK, "stroke_width": 3, "include_ticks": False, "include_tip": True},
        ).move_to(DOWN * 0.1)
        true = ax.plot(lambda t: np.sin(1.7 * t), color=INK, stroke_width=3)
        xs = np.arange(0.25, 8.0, 0.42)
        dots = VGroup(*[
            Dot(ax.c2p(x, np.sin(1.7 * x)), color=ACCENT, radius=0.09)
            for x in xs
        ])
        recon = ax.plot(lambda t: np.sin(1.7 * t), color=ACCENT, stroke_width=6)
        note = Text("More than two samples per cycle  —  the sine comes back.", color=SOFT, font_size=24)
        note.to_edge(DOWN, buff=0.34)

        self.play(FadeIn(title), Create(ax), Create(true), run_time=0.9)
        self.play(FadeIn(dots), run_time=0.7)
        self.play(Create(recon), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(hold())


class B05_Limit(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Nyquist = sample rate / 2", color=INK, font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.45)

        def card(big, sub, accent=False):
            box = RoundedRectangle(
                corner_radius=0.14, width=5.9, height=3.6,
                fill_color=WHITE, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
            )
            rail = Rectangle(width=5.9, height=0.12, stroke_width=0)
            rail.set_fill(ACCENT if accent else INK, 1)
            rail.align_to(box, UP)
            t = Text(big, color=INK, font_size=40, weight=BOLD)
            s = Text(sub, color=SOFT, font_size=24)
            t.move_to(box.get_center() + UP * 0.35)
            s.move_to(box.get_center() + DOWN * 0.55)
            return VGroup(box, rail, t, s)

        left = card("44,100 Hz", "a CD sample rate", accent=True)
        right = card("22,050 Hz", "highest unique pitch", accent=False)
        row = VGroup(left, right).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.15)
        foot = Text("Need more than two samples per cycle of the highest pitch you care about.", color=SOFT, font_size=22)
        foot.to_edge(DOWN, buff=0.36)

        self.play(FadeIn(title), run_time=0.45)
        self.play(FadeIn(left), run_time=0.55)
        self.play(FadeIn(right), run_time=0.55)
        self.play(FadeIn(foot), run_time=0.4)
        self.wait(hold())


class B06_Alias(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Too few dots  —  a high pitch pretends to be low.", color=INK, font_size=36, weight=BOLD)
        title.to_edge(UP, buff=0.36)

        ax = Axes(
            x_range=[0, 8.2, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=10.6,
            y_length=3.45,
            axis_config={"color": INK, "stroke_width": 3, "include_ticks": False, "include_tip": True},
        ).move_to(DOWN * 0.05)
        high = ax.plot(lambda t: np.sin(5.4 * t), color=SOFT, stroke_width=3)
        xs = np.arange(0.35, 8.0, 1.15)
        ys = [np.sin(5.4 * x) for x in xs]
        dots = VGroup(*[Dot(ax.c2p(x, y), color=ACCENT, radius=0.11) for x, y in zip(xs, ys)])
        fake = ax.plot(lambda t: np.sin(0.85 * t), color=ACCENT, stroke_width=6)
        note = Text("That slow terracotta curve is the alias. The high pitch was never stored.", color=SOFT, font_size=22)
        note.to_edge(DOWN, buff=0.32)

        self.play(FadeIn(title), Create(ax), Create(high), run_time=0.9)
        self.play(FadeIn(dots), run_time=0.6)
        self.play(Create(fake), run_time=0.9)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(hold())


class B07_Use(Scene):
    def construct(self):
        self.camera.background_color = BG
        header = Text("The split.", color=INK, font_size=48, weight=BOLD)
        header.to_edge(UP, buff=0.4)

        def col(title, lines, accent=False):
            box = RoundedRectangle(
                corner_radius=0.14, width=6.3, height=5.15,
                fill_color=WHITE, fill_opacity=1, stroke_color=INK, stroke_width=1.5,
            )
            rail = Rectangle(width=6.3, height=0.12, stroke_width=0)
            rail.set_fill(ACCENT if accent else INK, 1)
            rail.align_to(box, UP)
            t = Text(title, color=INK, font_size=30, weight=BOLD)
            body = VGroup(*[Text(ln, color=SOFT, font_size=22) for ln in lines])
            body.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
            g = VGroup(box, rail, t, body)
            t.next_to(rail, DOWN, buff=0.32).align_to(box, LEFT).shift(RIGHT * 0.38)
            body.next_to(t, DOWN, buff=0.38).align_to(t, LEFT)
            return g

        left = col("Use the limit to", ["choose a sample rate", "read a spectrogram ceiling", "catch a fake high"], accent=True)
        right = col("Do not", ["upsample to invent highs", "treat 192 kHz as magic", "blame a singer for folding"], accent=False)
        row = VGroup(left, right).arrange(RIGHT, buff=0.45).move_to(DOWN * 0.22)

        self.play(FadeIn(header), run_time=0.4)
        self.play(FadeIn(left), run_time=0.6)
        self.play(FadeIn(right), run_time=0.6)
        self.wait(hold())
