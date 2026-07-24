"""scenes.py — Manim for feature-list-checkpoint-persistence. Source: Claude Quickstarts (Anthropic)"""
from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

# ── @HumanitariansAI corner watermark (LOGO LAW) ─────────────────────────────────
def nbb_watermark(scene):
    mark = Text('@HumanitariansAI', font_size=11, color='#73705F', weight=NORMAL)
    mark.to_corner(DR, buff=0.18)
    mark.set_opacity(0.22)
    scene.add(mark)



class B01_TheReset(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("The Reset", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Session 1 bar — filled ACC
        bar1 = Rectangle(width=3.0, height=1.0, fill_color=ACC, fill_opacity=0.9, stroke_width=0)
        bar1.move_to([-2.5, 0.4, 0])
        bar1_label = Text("50 features — context full", font_size=14, color=INK)
        bar1_label.next_to(bar1, DOWN, buff=0.15)
        sess1_label = Text("Session 1", font_size=14, color=SOFT)
        sess1_label.next_to(bar1, UP, buff=0.15)
        nbb_watermark(self)

        self.play(GrowFromEdge(bar1, LEFT), FadeIn(sess1_label))
        self.play(FadeIn(bar1_label))

        # Dashed divider
        divider = DashedLine(
            start=[0, 1.5, 0],
            end=[0, -1.5, 0],
            color=INK,
            dash_length=0.15,
            stroke_width=2
        )
        boundary_label = Text("Session boundary", font_size=12, color=INK)
        boundary_label.next_to(divider, UP, buff=0.1)
        self.play(Create(divider), FadeIn(boundary_label))

        # Session 2 bar — empty SOFT border
        bar2 = Rectangle(width=3.0, height=1.0, fill_color=GHOST, fill_opacity=0.15, stroke_color=SOFT, stroke_width=2)
        bar2.move_to([2.5, 0.4, 0])
        bar2_label = Text("blank slate", font_size=14, color=SOFT)
        bar2_label.next_to(bar2, DOWN, buff=0.15)
        sess2_label = Text("Session 2", font_size=14, color=SOFT)
        sess2_label.next_to(bar2, UP, buff=0.15)

        self.play(Create(bar2), FadeIn(sess2_label))
        self.play(FadeIn(bar2_label))

        # Two arrows from Session 2
        arrow_re_read = Arrow(
            start=bar2.get_bottom() + np.array([-0.6, 0, 0]),
            end=bar2.get_bottom() + np.array([-0.6, -0.9, 0]),
            color=SOFT, stroke_width=2, buff=0.0
        )
        re_read_label = Text("Re-read everything", font_size=12, color=SOFT)
        re_read_label.next_to(arrow_re_read, LEFT, buff=0.1)

        arrow_guess = Arrow(
            start=bar2.get_bottom() + np.array([0.6, 0, 0]),
            end=bar2.get_bottom() + np.array([0.6, -0.9, 0]),
            color=ACC, stroke_width=2, buff=0.0
        )
        guess_label = Text("Guess — wrong X", font_size=12, color=ACC)
        guess_label.next_to(arrow_guess, RIGHT, buff=0.1)

        self.play(GrowArrow(arrow_re_read), FadeIn(re_read_label))
        self.play(GrowArrow(arrow_guess), FadeIn(guess_label))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_ExternalState(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("External State", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Two rectangles
        rect_json = Rectangle(width=2.8, height=0.8, color=INK, stroke_width=2)
        rect_json.move_to([-2.2, 1.2, 0])
        label_json = Text("feature_list.json", font_size=16, color=INK)
        label_json.move_to(rect_json.get_center())

        rect_git = Rectangle(width=2.2, height=0.8, color=SOFT, stroke_width=2)
        rect_git.move_to([2.2, 1.2, 0])
        label_git = Text("git log", font_size=16, color=SOFT)
        label_git.move_to(rect_git.get_center())

        self.play(Create(rect_json), FadeIn(label_json))
        self.play(Create(rect_git), FadeIn(label_git))

        # Cycle text sequence
        steps = [
            "read list",
            "find first incomplete",
            "implement",
            "test",
            "commit",
            "mark passing",
        ]
        step_objects = []
        for i, step in enumerate(steps):
            t = Text(step, font_size=17, color=ACC if i % 2 == 0 else SOFT)
            t.move_to([0, 0.1 - i * 0.55, 0])
            step_objects.append(t)

        for t in step_objects:
            self.play(FadeIn(t), run_time=0.5)

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_Accumulate(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("Accumulate", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        rows = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]
        row_objs = []
        badge_objs = []
        hash_objs = []

        start_y = 1.4
        row_h = 0.45

        for i, row_name in enumerate(rows):
            y = start_y - i * row_h
            box = Rectangle(width=1.4, height=0.35, color=SOFT, stroke_width=1.5)
            box.move_to([-3.0, y, 0])
            lbl = Text(row_name, font_size=13, color=INK)
            lbl.move_to(box.get_center())
            badge = Text("incomplete", font_size=12, color=SOFT)
            badge.move_to([-1.0, y, 0])
            h_text = Text("", font_size=11, color=GHOST)
            h_text.move_to([2.5, y, 0])
            row_objs.append((box, lbl))
            badge_objs.append(badge)
            hash_objs.append(h_text)

        # Draw all rows
        for box, lbl in row_objs:
            self.play(Create(box), FadeIn(lbl), run_time=0.2)

        # Show incomplete badges
        for badge in badge_objs[:4]:
            self.play(FadeIn(badge), run_time=0.2)

        # Session 1: flip f1-f4 to passing
        hashes = ["a1b2c3d", "e4f5g6h", "i7j8k9l", "m0n1o2p"]
        for i in range(4):
            new_badge = Text("passing", font_size=12, color=ACC)
            new_badge.move_to(badge_objs[i].get_center())
            hash_t = Text(hashes[i], font_size=11, color=GHOST)
            hash_t.move_to([2.5, start_y - i * row_h, 0])
            self.play(Transform(badge_objs[i], new_badge), FadeIn(hash_t), run_time=0.3)

        # Session boundary
        divider = DashedLine(
            start=[-4.5, start_y - 3.5 * row_h, 0],
            end=[4.0, start_y - 3.5 * row_h, 0],
            color=ACC, dash_length=0.15, stroke_width=2
        )
        bound_lbl = Text("Session boundary", font_size=12, color=ACC)
        bound_lbl.next_to(divider, RIGHT, buff=0.1)
        self.play(Create(divider), FadeIn(bound_lbl))

        # Session 2: f5-f8 begin flipping
        for i in range(4, 8):
            self.play(FadeIn(badge_objs[i]), run_time=0.2)
        for i in range(4, 6):
            new_badge = Text("passing", font_size=12, color=ACC)
            new_badge.move_to(badge_objs[i].get_center())
            hash_t = Text("q3r4s5t6", font_size=11, color=GHOST)
            hash_t.move_to([2.5, start_y - i * row_h, 0])
            self.play(Transform(badge_objs[i], new_badge), FadeIn(hash_t), run_time=0.3)

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B04_Scope(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("Scope", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        header = Text("Not covered:", font_size=20, color=INK)
        header.move_to([0, 1.2, 0])
        self.play(FadeIn(header))

        items = [
            "How initializer generates feature list",
            "Detailed test framework",
        ]
        for i, item in enumerate(items):
            t = Text(item, font_size=18, color=SOFT)
            t.move_to([0, 0.3 - i * 0.7, 0])
            self.play(FadeIn(t))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
