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
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 12",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


CLASSES = ["Cat", "Dog", "Car", "Bird", "Fish", "Tree", "Hat", "Cup", "Key", "Pen"]
TEACHER_LOGITS = [2.1, 0.8, -0.5, -0.3, -0.8, -1.2, -0.9, -0.7, -1.0, -0.6]


def softmax(logits, T=1.0):
    scaled = [l / T for l in logits]
    max_l = max(scaled)
    exps = [np.exp(l - max_l) for l in scaled]
    s = sum(exps)
    return [e / s for e in exps]


class B01_OneHotLabel(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("One-Hot Label: Cat = 1, Everything Else = 0", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        one_hot = [1.0 if c == "Cat" else 0.0 for c in CLASSES]

        n = len(CLASSES)
        bar_w = 0.55
        gap = 0.15
        start_x = -(n * bar_w + (n - 1) * gap) / 2 + bar_w / 2
        max_h = 3.2

        axes_line = Line(
            LEFT * (n * bar_w + (n - 1) * gap) / 2 + LEFT * 0.3,
            RIGHT * (n * bar_w + (n - 1) * gap) / 2 + RIGHT * 0.3,
            color=INK, stroke_width=2
        ).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        for i, (cls, v) in enumerate(zip(CLASSES, one_hot)):
            x = start_x + i * (bar_w + gap)
            h = max(v * max_h, 0.02)
            col = INK if cls == "Cat" else GHOST
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1
            ).move_to([x, -1.5 + h / 2, 0])
            lbl = Text(cls, font_size=10, color=SOFT).move_to([x, -1.5 - 0.3, 0]).rotate(PI / 6)
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), run_time=0.25)

        note = Text("One-hot label discards all inter-class relationships", font_size=15, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note))
        self.wait(1.5)


class B02_TeacherT1(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Teacher Distribution at T=1", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        probs = softmax(TEACHER_LOGITS, T=1.0)

        n = len(CLASSES)
        bar_w = 0.55
        gap = 0.15
        start_x = -(n * bar_w + (n - 1) * gap) / 2 + bar_w / 2
        max_h = 3.5

        axes_line = Line(
            LEFT * (n * bar_w + (n - 1) * gap) / 2 + LEFT * 0.3,
            RIGHT * (n * bar_w + (n - 1) * gap) / 2 + RIGHT * 0.3,
            color=INK, stroke_width=2
        ).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        for i, (cls, p) in enumerate(zip(CLASSES, probs)):
            x = start_x + i * (bar_w + gap)
            h = max(p * max_h * 3, 0.02)
            col = ACC if cls == "Dog" else (INK if cls == "Cat" else GHOST)
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1
            ).move_to([x, -1.5 + h / 2, 0])
            lbl = Text(cls, font_size=10, color=SOFT).move_to([x, -1.5 - 0.3, 0]).rotate(PI / 6)
            val = Text(f"{p:.2f}", font_size=10, color=col).move_to([x, -1.5 + h + 0.2, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), FadeIn(val), run_time=0.25)

        dog_arrow = Text("5% dog → extra signal", font_size=14, color=ACC).shift(RIGHT * 1.5 + UP * 1.2)
        self.play(FadeIn(dog_arrow))
        self.wait(1.5)


class B03_TemperatureSweep(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.add(source_credit())

        title = Text("Temperature Sweep: T=1 → T=3 → T=6", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        temps = [1.0, 3.0, 6.0]
        cols = [INK, SOFT, ACC]

        # Show bar heights for first 5 classes at each temp
        show_classes = CLASSES[:5]
        show_logits = TEACHER_LOGITS[:5]

        n_cls = len(show_classes)
        n_temps = len(temps)
        group_w = n_temps * 0.45 + (n_temps - 1) * 0.05
        gap_group = 0.5
        start_x = -(n_cls * group_w + (n_cls - 1) * gap_group) / 2 + group_w / 2
        max_h = 3.0

        axes_line = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        for ci, cls in enumerate(show_classes):
            x_group = start_x + ci * (group_w + gap_group)
            for ti, (T, col) in enumerate(zip(temps, cols)):
                probs = softmax(show_logits, T=T)
                p = probs[ci]
                h = max(p * max_h * 5, 0.02)
                x = x_group + ti * (0.45 + 0.05) - group_w / 2 + 0.225
                bar = Rectangle(
                    width=0.4, height=h,
                    fill_color=col, fill_opacity=0.8,
                    stroke_color=col, stroke_width=0.5
                ).move_to([x, -1.5 + h / 2, 0])
                self.play(GrowFromEdge(bar, DOWN), run_time=0.2)

            lbl = Text(cls, font_size=13, color=INK).move_to([x_group, -1.5 - 0.4, 0])
            self.play(FadeIn(lbl), run_time=0.1)

        legend = VGroup(
            *[VGroup(
                Rectangle(width=0.3, height=0.2, fill_color=c, fill_opacity=0.8, stroke_width=0),
                Text(f"T={t}", font_size=12, color=c)
            ).arrange(RIGHT, buff=0.1)
              for t, c in zip(temps, cols)]
        ).arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(legend))

        note = Text("Higher T → flatter distribution → more inter-class signal", font_size=14, color=ACC).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.5)
