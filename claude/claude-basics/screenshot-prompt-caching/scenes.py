"""scenes.py — Manim for screenshot-prompt-caching. Source: Claude Quickstarts (Anthropic)"""
from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

# ── @NikBearBrown corner watermark (LOGO LAW) ─────────────────────────────────
def nbb_watermark(scene):
    mark = Text('@NikBearBrown', font_size=11, color='#73705F', weight=NORMAL)
    mark.to_corner(DR, buff=0.18)
    mark.set_opacity(0.22)
    scene.add(mark)



class B01_Redundant(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("Redundant", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Row of ~12 small turn chips
        unique_labels = ["A", "B", "C"]
        n_chips = 12
        chip_w = 0.5
        chip_h = 0.4
        spacing = 0.62
        start_x = -(n_chips / 2) * spacing + spacing / 2

        chips = []
        for i in range(n_chips):
            is_unique = i < 3
            color = ACC if is_unique else SOFT
            label_text = unique_labels[i] if is_unique else unique_labels[i % 3]
            rect = Rectangle(
                width=chip_w, height=chip_h,
                fill_color=color, fill_opacity=0.85 if is_unique else 0.3,
                stroke_color=color, stroke_width=1.5
            )
            rect.move_to([start_x + i * spacing, 0.8, 0])
            lbl = Text(label_text, font_size=13, color=INK)
            lbl.move_to(rect.get_center())
            chips.append((rect, lbl))

        for rect, lbl in chips:
            self.play(FadeIn(rect), FadeIn(lbl), run_time=0.15)

        # Token counter
        token_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
        token_texts = []
        for i, val in enumerate(token_values):
            t = Text(f"{val}k", font_size=13, color=INK)
            t.move_to([start_x + i * spacing, 0.1, 0])
            token_texts.append(t)

        for t in token_texts:
            self.play(FadeIn(t), run_time=0.12)

        # Brace label "wasted tokens"
        brace_start = chips[3][0].get_top() + np.array([0, 0.15, 0])
        brace_end = chips[-1][0].get_top() + np.array([0, 0.15, 0])
        brace = Line(
            start=brace_start,
            end=brace_end,
            color=ACC, stroke_width=2
        )
        tick_l = Line(brace_start, brace_start + np.array([0, 0.15, 0]), color=ACC, stroke_width=2)
        tick_r = Line(brace_end, brace_end + np.array([0, 0.15, 0]), color=ACC, stroke_width=2)
        waste_label = Text("wasted tokens", font_size=15, color=ACC)
        waste_label.move_to([
            (brace_start[0] + brace_end[0]) / 2,
            brace_start[1] + 0.4,
            0
        ])

        self.play(Create(brace), Create(tick_l), Create(tick_r), FadeIn(waste_label))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B02_CacheHit(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("Cache Hit", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # cache_control flag
        flag_line = Text('"cache_control": {"type": "ephemeral"}', font_size=18, color=INK)
        flag_line.move_to([0, 1.2, 0])
        self.play(FadeIn(flag_line))

        # First send — MISS
        send1_rect = Rectangle(width=3.5, height=0.65, color=SOFT, stroke_width=1.5)
        send1_rect.move_to([-1.5, 0.1, 0])
        send1_label = Text("first send", font_size=14, color=SOFT)
        send1_label.move_to(send1_rect.get_center())
        miss_badge = Text("MISS — tokenized", font_size=13, color=ACC)
        miss_badge.next_to(send1_rect, RIGHT, buff=0.2)

        self.play(Create(send1_rect), FadeIn(send1_label))
        self.play(FadeIn(miss_badge))

        # Second send — HIT
        send2_rect = Rectangle(width=3.5, height=0.65, color=INK, stroke_width=1.5)
        send2_rect.move_to([-1.5, -0.8, 0])
        send2_label = Text("second identical send", font_size=14, color=INK)
        send2_label.move_to(send2_rect.get_center())
        hit_badge = Text("HIT — ~0 tokens", font_size=13, color=ACC)
        hit_badge.next_to(send2_rect, RIGHT, buff=0.2)

        self.play(Create(send2_rect), FadeIn(send2_label))
        self.play(FadeIn(hit_badge))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)


class B03_Filmstrip(Scene):
    def construct(self):
        self.camera.background_color = BG
        nbb_watermark(self)

        title = Text("Filmstrip", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        n_frames = 10
        first_occurrences = {0, 3, 7}  # 3 MISS frames
        frame_w = 0.55
        frame_h = 0.7
        spacing = 0.68
        start_x = -(n_frames / 2) * spacing + spacing / 2

        frames = []
        for i in range(n_frames):
            is_miss = i in first_occurrences
            color = ACC if is_miss else SOFT
            fill_op = 0.15 if is_miss else 0.4
            rect = Rectangle(
                width=frame_w, height=frame_h,
                fill_color=color, fill_opacity=fill_op,
                stroke_color=color, stroke_width=2
            )
            rect.move_to([start_x + i * spacing, 0.8, 0])
            badge_text = "MISS" if is_miss else "HIT"
            badge = Text(badge_text, font_size=10, color=color)
            badge.move_to(rect.get_center())
            frames.append((rect, badge))

        for rect, badge in frames:
            self.play(FadeIn(rect), FadeIn(badge), run_time=0.18)

        # Stats
        without_text = Text("Without: 100,000 tokens", font_size=16, color=INK)
        with_text    = Text("With:    10,000 tokens", font_size=16, color=ACC)
        without_text.move_to([-2.0, -0.4, 0])
        with_text.move_to([2.0, -0.4, 0])

        self.play(FadeIn(without_text), FadeIn(with_text))

        # Large badge "90% saved"
        saved_bg = Rectangle(width=2.8, height=0.7, fill_color=ACC, fill_opacity=0.2, stroke_color=ACC, stroke_width=2)
        saved_bg.move_to([0, -1.4, 0])
        saved_text = Text("90% saved", font_size=22, color=ACC, weight=BOLD)
        saved_text.move_to(saved_bg.get_center())

        self.play(Create(saved_bg), FadeIn(saved_text))

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
            "Minimum token thresholds",
            "Cache eviction policy",
            "Persistent cache tier",
        ]
        for i, item in enumerate(items):
            t = Text(item, font_size=18, color=SOFT)
            t.move_to([0, 0.3 - i * 0.7, 0])
            self.play(FadeIn(t))

        source = Text("Source: Claude Quickstarts (Anthropic)", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)
        self.wait(1)
