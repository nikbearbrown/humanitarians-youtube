"""scenes.py — Manim for macos-computer-use-coordinate-roundtrip. Source: Claude Quickstarts (Anthropic)"""
from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_TheDrift(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Drift", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Large display rectangle — native Retina
        large_rect = Rectangle(width=5.0, height=3.0, color=INK, stroke_width=2)
        large_rect.move_to([0, 0.6, 0])
        large_label = Text("2560x1600 (native Retina)", font_size=16, color=INK)
        large_label.move_to(large_rect.get_center())

        self.play(Create(large_rect), FadeIn(large_label))

        # Arrow with label
        arrow = Arrow(
            start=large_rect.get_bottom() + np.array([0, -0.1, 0]),
            end=large_rect.get_bottom() + np.array([0, -1.0, 0]),
            color=SOFT, stroke_width=2, buff=0.0
        )
        arrow_label = Text("target_image_size()", font_size=13, color=SOFT)
        arrow_label.next_to(arrow, RIGHT, buff=0.15)

        self.play(GrowArrow(arrow), FadeIn(arrow_label))

        # Smaller rectangle — sent to API
        small_rect = Rectangle(width=3.2, height=1.8, color=SOFT, stroke_width=2)
        small_rect.move_to([0, -2.5, 0])
        small_label = Text("1456x819 (sent to API)", font_size=14, color=SOFT)
        small_label.move_to(small_rect.get_center())

        self.play(Create(small_rect), FadeIn(small_label))

        # Warning text
        warning = Text("Without pre-resize: server resizes again — click drift", font_size=14, color=ACC)
        warning.move_to([0, -3.5, 0])
        self.play(FadeIn(warning))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_Forward(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Forward", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Code lines appear one by one
        lines = [
            ("original = (2560, 1600)", INK),
            ("sent_w, sent_h = target_image_size(*original)  # 1456, 819", SOFT),
            ("img = img.resize((sent_w, sent_h))", INK),
            ("# record sent for inverse", SOFT),
        ]
        start_y = 1.2
        line_objs = []
        for i, (text, color) in enumerate(lines):
            t = Text(text, font_size=15, color=color)
            t.move_to([0, start_y - i * 0.65, 0])
            line_objs.append(t)

        for t in line_objs:
            self.play(FadeIn(t), run_time=0.5)

        # Result chip
        chip_bg = Rectangle(width=3.2, height=0.55, fill_color=ACC, fill_opacity=0.15, stroke_color=ACC, stroke_width=1.5)
        chip_bg.move_to([0, -1.4, 0])
        chip_text = Text("(1456, 819) recorded", font_size=16, color=ACC)
        chip_text.move_to(chip_bg.get_center())

        self.play(Create(chip_bg), FadeIn(chip_text))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_RoundTrip(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Round-Trip", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Left panel — Original
        left_rect = Rectangle(width=2.8, height=2.0, color=INK, stroke_width=2)
        left_rect.move_to([-2.8, 0.0, 0])
        left_label = Text("Original 1920x1080", font_size=13, color=INK)
        left_label.next_to(left_rect, UP, buff=0.15)
        left_dot = Dot(point=left_rect.get_center(), radius=0.13, color=ACC)
        left_coord = Text("Button\n(960, 540)", font_size=12, color=ACC)
        left_coord.next_to(left_dot, DOWN, buff=0.12)

        self.play(Create(left_rect), FadeIn(left_label))
        self.play(FadeIn(left_dot), FadeIn(left_coord))

        # Downward arrow "forward"
        fwd_arrow = Arrow(
            start=left_rect.get_right() + np.array([0.1, 0.2, 0]),
            end=left_rect.get_right() + np.array([1.4, 0.2, 0]),
            color=SOFT, stroke_width=2, buff=0.0
        )
        fwd_label = Text("forward", font_size=12, color=SOFT)
        fwd_label.next_to(fwd_arrow, UP, buff=0.08)
        self.play(GrowArrow(fwd_arrow), FadeIn(fwd_label))

        # Right panel — API sees
        right_rect = Rectangle(width=2.2, height=1.5, color=SOFT, stroke_width=2)
        right_rect.move_to([2.8, 0.0, 0])
        right_label = Text("API sees 1456x819", font_size=13, color=SOFT)
        right_label.next_to(right_rect, UP, buff=0.15)
        right_dot = Dot(point=right_rect.get_center(), radius=0.13, color=ACC)
        right_coord = Text("(728, 409)", font_size=12, color=SOFT)
        right_coord.next_to(right_dot, DOWN, buff=0.12)

        self.play(Create(right_rect), FadeIn(right_label))
        self.play(FadeIn(right_dot), FadeIn(right_coord))

        # Curved return arrow
        inv_arrow = CurvedArrow(
            start_point=right_rect.get_bottom() + np.array([0, -0.1, 0]),
            end_point=left_rect.get_bottom() + np.array([0, -0.1, 0]),
            angle=-TAU / 5,
            color=ACC, stroke_width=2
        )
        inv_label = Text("inverse x(1920/1456)", font_size=12, color=ACC)
        inv_label.move_to([0, -2.0, 0])
        self.play(Create(inv_arrow), FadeIn(inv_label))

        # Formula chips
        chip1 = Text("728 x 1920/1456 = 960", font_size=14, color=ACC)
        chip2 = Text("409 x 1080/819 = 540", font_size=14, color=ACC)
        chip1.move_to([-1.5, -2.9, 0])
        chip2.move_to([1.5, -2.9, 0])
        self.play(FadeIn(chip1), FadeIn(chip2))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B04_Scope(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Scope", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        header = Text("Not covered:", font_size=20, color=INK)
        header.move_to([0, 1.2, 0])
        self.play(FadeIn(header))

        items = [
            "Batched tool calls",
            "Non-macOS platforms",
            "No-op case (sent==original)",
        ]
        for i, item in enumerate(items):
            t = Text(item, font_size=18, color=SOFT)
            t.move_to([0, 0.3 - i * 0.7, 0])
            self.play(FadeIn(t))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
