"""scenes.py — Manim for claude-liam-soft-label-lesson. Source: embedded-ai Ch. 12"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_OneHotBar(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("One-Hot Labels: Information-Poor", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        classes = ["cat", "dog", "bird", "fish", "frog"]
        probs_onehot = [1.0, 0.0, 0.0, 0.0, 0.0]

        bar_w = 1.1
        spacing = 1.5
        max_h = 2.8
        x_start = -3.5

        # Cat bar (tall) — play separately for state change
        cat_bar = Rectangle(width=bar_w, height=max_h, fill_color=SOFT, fill_opacity=0.8, stroke_width=0)
        cat_bar.move_to([x_start, max_h / 2 - 1.7, 0])
        cat_lbl = Text("cat", font_size=16, color=INK)
        cat_lbl.move_to([x_start, -1.9, 0])
        cat_p = Text("1", font_size=16, color=SOFT)
        cat_p.next_to(cat_bar, UP, buff=0.1)
        self.play(GrowFromEdge(cat_bar, DOWN), FadeIn(cat_lbl))
        self.play(FadeIn(cat_p))

        # Remaining bars (flat) — play as group for contrast
        flat_bars = VGroup()
        flat_lbls = VGroup()
        for i in range(1, len(classes)):
            bar = Rectangle(width=bar_w, height=0.08, fill_color=GHOST, fill_opacity=0.5, stroke_width=0)
            bar.move_to([x_start + i * spacing, -1.66, 0])
            lbl = Text(classes[i], font_size=16, color=GHOST)
            lbl.move_to([x_start + i * spacing, -1.9, 0])
            flat_bars.add(bar)
            flat_lbls.add(lbl)
        self.play(FadeIn(flat_bars), FadeIn(flat_lbls))

        p_zero = Text("0   0   0   0", font_size=16, color=GHOST)
        p_zero.move_to([x_start + 2.5 * spacing, -1.9, 0])
        self.play(FadeIn(p_zero))

        note = Text("cat=1, everything else=0. No similarity. No structure.", font_size=16, color=SOFT)
        note.to_edge(DOWN, buff=0.7)
        missing = Text("What resembles a cat? Label doesn't say.", font_size=15, color=GHOST)
        missing.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note))
        self.play(FadeIn(missing))

        self.wait(1.2)


class B02_TeacherDist(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Teacher's Soft Labels: Information-Rich", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        classes = ["cat", "dog", "bird", "fish", "frog"]
        probs_soft = [0.85, 0.05, 0.04, 0.03, 0.03]

        bar_w = 1.1
        spacing = 1.5
        max_h = 3.0
        x_start = -3.5

        bars = VGroup()
        labels = VGroup()
        prob_lbls = VGroup()

        for i, (cls, prob) in enumerate(zip(classes, probs_soft)):
            h = prob * max_h
            # Dog bar is terracotta — the interesting signal
            if cls == "dog":
                color = ACC
            elif cls == "cat":
                color = SOFT
            else:
                color = GHOST
            bar = Rectangle(width=bar_w, height=max(h, 0.08),
                            fill_color=color, fill_opacity=0.85, stroke_width=0)
            bar.move_to([x_start + i * spacing, h / 2 - 1.8, 0])
            bars.add(bar)

            cls_lbl = Text(cls, font_size=16, color=color if cls == "dog" else INK)
            cls_lbl.move_to([x_start + i * spacing, -2.1, 0])
            labels.add(cls_lbl)

            p_str = f"{prob:.2f}"
            p_lbl = Text(p_str, font_size=15, color=color if cls in ("cat", "dog") else GHOST)
            p_lbl.next_to(bar, UP, buff=0.1)
            prob_lbls.add(p_lbl)

        self.play(FadeIn(labels))
        self.play(*[GrowFromEdge(b, DOWN) for b in bars], run_time=0.9)
        self.play(FadeIn(prob_lbls))

        dog_bar = bars[1]
        dog_insight = Text("5% dog — encodes visual similarity to cat", font_size=15, color=ACC)
        dog_insight.next_to(dog_bar, RIGHT, buff=0.4).shift(UP * 0.5)
        arrow = Arrow(start=dog_insight.get_left(), end=dog_bar.get_right() + UP * 0.2,
                      color=ACC, stroke_width=1.5, buff=0.05)
        self.play(FadeIn(dog_insight), GrowArrow(arrow))

        note = Text("The teacher learned this from millions of examples.", font_size=15, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)


class B03_MixedLoss(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Student Trains on Mixed Loss", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Teacher box
        teacher = Rectangle(width=2.8, height=1.2, fill_color=SOFT, fill_opacity=0.15, stroke_color=SOFT, stroke_width=1.5)
        teacher.move_to([-4.0, 1.2, 0])
        t_lbl = Text("Teacher\n(large)", font_size=16, color=SOFT)
        t_lbl.move_to(teacher.get_center())
        self.play(FadeIn(teacher), FadeIn(t_lbl))

        # Ground truth box
        gt = Rectangle(width=2.8, height=1.2, fill_color=GHOST, fill_opacity=0.15, stroke_color=GHOST, stroke_width=1.5)
        gt.move_to([-4.0, -1.2, 0])
        gt_lbl = Text("Ground truth\n(one-hot)", font_size=16, color=INK)
        gt_lbl.move_to(gt.get_center())
        self.play(FadeIn(gt), FadeIn(gt_lbl))

        # Student box
        student = Rectangle(width=2.8, height=1.6, fill_color=ACC, fill_opacity=0.12, stroke_color=ACC, stroke_width=1.5)
        student.move_to([3.5, 0.0, 0])
        s_lbl = Text("Student\n(small)\n+2-5% accuracy", font_size=16, color=ACC)
        s_lbl.move_to(student.get_center())
        self.play(FadeIn(student), FadeIn(s_lbl))

        # Arrows to student
        soft_arrow = Arrow(start=teacher.get_right(), end=student.get_left() + UP * 0.4,
                           color=ACC, stroke_width=2, buff=0.1)
        soft_lbl = Text("soft labels (T=3)", font_size=14, color=ACC)
        soft_lbl.move_to([0.0, 0.9, 0])
        self.play(GrowArrow(soft_arrow), FadeIn(soft_lbl))

        hard_arrow = Arrow(start=gt.get_right(), end=student.get_left() + DOWN * 0.4,
                           color=GHOST, stroke_width=2, buff=0.1)
        hard_lbl = Text("hard labels (alpha)", font_size=14, color=GHOST)
        hard_lbl.move_to([0.0, -0.9, 0])
        self.play(GrowArrow(hard_arrow), FadeIn(hard_lbl))

        # Mixed loss
        loss_box = Rectangle(width=2.6, height=0.8, fill_color=SOFT, fill_opacity=0.15, stroke_color=SOFT, stroke_width=1.2)
        loss_box.move_to([0.0, 0.0, 0])
        loss_lbl = Text("mixed loss", font_size=15, color=INK)
        loss_lbl.move_to(loss_box.get_center())
        self.play(FadeIn(loss_box), FadeIn(loss_lbl))

        note = Text("Richer signal — no extra training data needed.", font_size=15, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)
