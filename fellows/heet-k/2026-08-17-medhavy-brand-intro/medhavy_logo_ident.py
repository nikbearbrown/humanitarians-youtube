from __future__ import annotations

from pathlib import Path

import numpy as np
from manim import *
from manimpango import register_font


ROOT = Path("/Users/nik/Documents/Cowork/Manim/medhavy-logo-ident")
SVG_DIR = Path("/Users/nik/Documents/Cowork/medhavy/svg")
VOICE = ROOT / "mp3" / "medhavy_voice.mp3"
FONT = Path("/Users/nik/Documents/Cowork/Manim/fonts/Montserrat/static/Montserrat-Bold.ttf")

register_font(str(FONT))


class MedhavyLogoIdent(Scene):
    def construct(self):
        self.camera.background_color = "#F7F8F5"

        ink = "#111111"
        graphite = "#4B5563"
        teal = "#00A7A5"
        blue = "#355CFF"
        gold = "#E0A526"

        def icon(num: int) -> SVGMobject:
            m = SVGMobject(str(SVG_DIR / f"medhavy-{num:02d}.svg"))
            m.set_fill(ink, opacity=1)
            m.set_stroke(ink, width=0.7, opacity=0.95)
            return m

        def wordmark() -> VGroup:
            letters = VGroup()
            for ch in "MEDHAVY":
                t = Text(ch, font="Montserrat", weight=BOLD, color=ink, font_size=44)
                letters.add(t)
            letters.arrange(RIGHT, buff=0.23)
            return letters

        def label(text: str, size=20, color=graphite):
            return Text(text.upper(), font="Montserrat", weight=BOLD, color=color, font_size=size)

        # 1. A clean field with faint learning-grid geometry.
        grid = VGroup()
        for x in np.linspace(-6.5, 6.5, 14):
            grid.add(Line([x, -3.7, 0], [x, 3.7, 0], stroke_width=0.45, color="#DDE3E1"))
        for y in np.linspace(-3.4, 3.4, 8):
            grid.add(Line([-6.9, y, 0], [6.9, y, 0], stroke_width=0.45, color="#DDE3E1"))
        grid.set_opacity(0.35)
        self.play(FadeIn(grid), run_time=0.8)

        # 2. Logo variants arrive as raw visual vocabulary.
        nums = [1, 4, 7, 12, 16, 19, 22, 25, 29, 31, 37, 40, 44, 49, 51, 55]
        swarm = VGroup()
        for i, n in enumerate(nums):
            m = icon(n)
            m.scale_to_fit_height(0.6)
            angle = i * TAU / len(nums)
            m.move_to([5.2 * np.cos(angle), 2.5 * np.sin(angle), 0])
            m.set_opacity(0.18 + 0.03 * (i % 3))
            swarm.add(m)
        self.play(LaggedStart(*[FadeIn(m, scale=0.25) for m in swarm], lag_ratio=0.04), run_time=1.7)
        self.play(Rotate(swarm, angle=PI / 3), swarm.animate.set_opacity(0.28), run_time=1.2)

        # 3. Data pulses converge from the variants.
        pulse_lines = VGroup()
        for m in swarm:
            line = Line(m.get_center(), ORIGIN, color=teal, stroke_width=2.0).set_opacity(0.38)
            pulse_lines.add(line)
        self.play(LaggedStart(*[Create(line) for line in pulse_lines], lag_ratio=0.018), run_time=1.1)
        self.play(pulse_lines.animate.set_opacity(0.08), swarm.animate.scale(0.72), run_time=0.8)

        # 4. A central mark flickers through several candidates before resolving.
        preview_nums = [8, 18, 24, 32, 41, 46, 50]
        preview = icon(preview_nums[0]).scale_to_fit_height(2.25).move_to(UP * 0.35)
        preview.set_fill(teal, opacity=0.95).set_stroke(teal, width=1.0)
        self.play(TransformFromCopy(swarm[3], preview), run_time=0.7)
        for n, col in zip(preview_nums[1:], [blue, ink, teal, gold, ink, teal]):
            nxt = icon(n).scale_to_fit_height(2.25).move_to(preview)
            nxt.set_fill(col, opacity=0.95).set_stroke(col, width=1.0)
            self.play(Transform(preview, nxt), run_time=0.22)
        self.play(preview.animate.set_fill(ink).set_stroke(ink, width=0.8), run_time=0.35)

        # 5. Break the preview into parts, then rebuild as the final icon.
        shards = VGroup()
        for k, sub in enumerate(preview.copy().submobjects[:42]):
            sub.generate_target()
            angle = k * 0.55
            sub.target.shift([0.9 * np.cos(angle), 0.55 * np.sin(angle), 0])
            sub.target.set_opacity(0.25)
            shards.add(sub)
        if shards:
            self.play(LaggedStart(*[MoveToTarget(s) for s in shards], lag_ratio=0.004), preview.animate.set_opacity(0), run_time=1.0)
            self.play(FadeOut(shards), run_time=0.4)
        else:
            self.play(FadeOut(preview), run_time=0.4)

        final_icon = icon(12).scale_to_fit_height(2.55).move_to(UP * 0.85)
        halo = Circle(radius=1.62, color=teal, stroke_width=2.0).move_to(final_icon)
        halo.set_opacity(0.0)
        nodes = VGroup()
        for a in np.linspace(0, TAU, 18, endpoint=False):
            dot = Dot(final_icon.get_center() + [1.72 * np.cos(a), 1.72 * np.sin(a), 0], radius=0.025, color=teal)
            nodes.add(dot)

        self.play(Create(halo), halo.animate.set_opacity(0.35), run_time=0.55)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in nodes], lag_ratio=0.018), run_time=0.65)
        self.play(DrawBorderThenFill(final_icon), run_time=1.35)
        self.play(halo.animate.scale(1.12).set_opacity(0), nodes.animate.set_opacity(0.25), run_time=0.65)
        self.play(
            FadeOut(swarm),
            FadeOut(pulse_lines),
            FadeOut(grid),
            FadeOut(nodes),
            run_time=0.55,
        )

        # 6. Voice begins on the final brand reveal.
        self.add_sound(str(VOICE), gain=1.0)
        name = wordmark().next_to(final_icon, DOWN, buff=0.35)
        tagline = label("Intelligent Textbooks", size=20, color=graphite).next_to(name, DOWN, buff=0.26)
        url = label("www.medhavy.com", size=17, color=teal).next_to(tagline, DOWN, buff=0.19)

        self.play(LaggedStart(*[FadeIn(ch, shift=DOWN * 0.08) for ch in name], lag_ratio=0.055), run_time=1.0)
        self.play(FadeIn(tagline, shift=DOWN * 0.12), run_time=0.8)

        # 7. Make the logo feel constructed: circuit paths lock into a book-like base.
        left_trace = VMobject(color=teal, stroke_width=4)
        left_trace.set_points_as_corners([[-2.55, -1.45, 0], [-1.8, -1.45, 0], [-1.45, -1.18, 0], [-0.95, -1.18, 0]])
        right_trace = VMobject(color=teal, stroke_width=4)
        right_trace.set_points_as_corners([[2.55, -1.45, 0], [1.8, -1.45, 0], [1.45, -1.18, 0], [0.95, -1.18, 0]])
        self.play(Create(left_trace), Create(right_trace), run_time=0.55)
        self.play(FadeIn(url, shift=DOWN * 0.08), run_time=0.65)

        # 8. Final polish: a soft pulse, then hold.
        brand = VGroup(final_icon, name, tagline, url, left_trace, right_trace)
        self.play(brand.animate.scale(1.035), run_time=0.45, rate_func=there_and_back)
        sparkle = VGroup(
            *[Dot(final_icon.get_center() + [np.cos(a) * 1.35, np.sin(a) * 1.25, 0], radius=0.018, color=gold)
              for a in np.linspace(0.25, TAU + 0.25, 10, endpoint=False)]
        )
        self.play(LaggedStart(*[Flash(d, color=gold, line_length=0.12, num_lines=6) for d in sparkle], lag_ratio=0.05), run_time=0.9)
        self.play(FadeOut(VGroup()), run_time=0.2)
        self.wait(2.2)
