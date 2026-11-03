"""
Manim scenes for two-threads-one-week (v2 revision — "a log, not a highlight reel")
B01_AgrimaIntro — presenter intro: who's talking, what this week covered
B04_LogV1       — weekly_log_v1.py run for real: two plain logs, every item + status
B07_LogV2       — weekly_log_v2.py run for real: SAME logs + a standout per thread
B08_Summary     — the log, restated — not a highlight reel
"""

from manim import *

PALETTE = {
    "bg":     "#FAF9F5",
    "ink":    "#3D3929",
    "accent": "#D97757",
    "good":   "#4A7C59",
    "miss":   "#C0392B",
    "card":   "#FFFFFF",
    "border": "#E8E4DA",
    "dim":    "#8B8878",
}


def card_bg(width, height):
    return RoundedRectangle(
        corner_radius=0.12, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=PALETTE["border"], stroke_width=1.5,
    )


class B01_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = Text(
            "This week split two ways — writing\nabout AI, and hands-on work for the\n"
            "Loon Project, tracking Minnesota's\ncommon loons by drone. This is the\n"
            "log, not the highlights.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.35, should_center=True)
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        group = VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        rule.stretch(0.01, 0)
        self.play(rule.animate.stretch_to_fit_width(1.8), run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.wait(1.3)


# Shared log-column renderer for B04 / B07. A plain function, not a shared
# base class — run.sh discovers Manim scenes via a regex requiring each
# scene class to inherit directly from Scene, so both real scene classes
# below call this helper from their own construct().
def _log_column(scene, items, header, x_center, top_y, show_highlight=False, font_size=15):
    head = Text(header, color=PALETTE["ink"], font_size=19)
    head.move_to([x_center, top_y, 0])
    rule = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["accent"], stroke_width=2.5)
    rule.next_to(head, DOWN, buff=0.16)

    scene.play(FadeIn(head), run_time=0.3)
    rule.stretch(0.01, 0)
    scene.play(rule.animate.stretch_to_fit_width(3.8), run_time=0.3)

    prev = rule
    if show_highlight:
        standout = next(i for i in items if i["status"] in ("done", "published"))
        hl = Text(f"* highlight: {standout['item']}", color=PALETTE["accent"], font_size=font_size + 1)
        hl.next_to(rule, DOWN, buff=0.22)
        hl.set_x(x_center)
        scene.play(FadeIn(hl, shift=RIGHT * 0.15), run_time=0.3)
        prev = hl

    rows = VGroup(*[
        Text(
            f"- {it['item']} ({it['status']})",
            color=PALETTE["ink"] if it["status"] in ("done", "published") else PALETTE["dim"],
            font_size=font_size,
        )
        for it in items
    ])
    rows.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
    rows.next_to(prev, DOWN, buff=0.26)
    rows.set_x(x_center)

    for row in rows:
        scene.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.24)

    return VGroup(head, rule, rows)


WEEK = {
    "writing": [
        {"item": "Fashion Just Got a Data Brain", "status": "published"},
        {"item": "The Open-Source AI Gap Basically Closed", "status": "published"},
    ],
    "loon_project": [
        {"item": "Drone acquired", "status": "done"},
        {"item": "FAA Part 107 requirements researched", "status": "done"},
        {"item": "Social media strategy written", "status": "done"},
        {"item": "Nina's FAA certification", "status": "in progress"},
        {"item": "First drone footage", "status": "in progress"},
        {"item": "CV model training", "status": "in progress"},
    ],
}


class B04_LogV1(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Run it — weekly_log_v1.py", color=PALETTE["ink"],
                      font_size=24).to_edge(UP, buff=0.7)
        sub = Text("this week, logged", color=PALETTE["dim"],
                    font_size=15).next_to(title, DOWN, buff=0.12)
        self.play(Write(title), FadeIn(sub), run_time=0.5)

        top_y = sub.get_bottom()[1] - 0.5
        _log_column(self, WEEK["writing"], "WRITING", -3.5, top_y)
        _log_column(self, WEEK["loon_project"], "LOON PROJECT", 3.2, top_y)

        self.wait(1.0)


class B07_LogV2(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Run it again — weekly_log_v2.py", color=PALETTE["ink"],
                      font_size=24).to_edge(UP, buff=0.7)
        sub = Text("the SAME log, now with a standout", color=PALETTE["dim"],
                    font_size=15).next_to(title, DOWN, buff=0.12)
        self.play(Write(title), FadeIn(sub), run_time=0.5)

        top_y = sub.get_bottom()[1] - 0.5
        _log_column(self, WEEK["writing"], "WRITING", -3.5, top_y, show_highlight=True)
        _log_column(self, WEEK["loon_project"], "LOON PROJECT", 3.2, top_y, show_highlight=True)

        self.wait(1.2)


class B08_Summary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Two threads, one week — the log",
                      color=PALETTE["ink"], font_size=28).to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.7)

        left_box = card_bg(5.2, 3.0)
        left_head = Text("WRITING", color=PALETTE["good"], font_size=20)
        left_body = Text(
            "Fashion's new data brain: forecasting,\ngenerative design, virtual try-on.\n"
            "The open-source gap — nearly closed.",
            color=PALETTE["ink"], font_size=15.5, line_spacing=1.3)
        left_g = VGroup(left_head, left_body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        left_card = VGroup(left_box, left_g.move_to(left_box.get_center()))

        right_box = card_bg(5.2, 3.0)
        right_head = Text("LOON PROJECT", color=PALETTE["good"], font_size=20)
        right_body = Text(
            "Drone in hand, FAA path researched,\nstrategy written. Certification,\n"
            "footage, and training: still in progress.",
            color=PALETTE["ink"], font_size=15.5, line_spacing=1.3)
        right_g = VGroup(right_head, right_body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_card = VGroup(right_box, right_g.move_to(right_box.get_center()))

        row = VGroup(left_card, right_card).arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.55)
        left_box.stretch(0.01, 0)
        right_box.stretch(0.01, 0)
        self.play(left_box.animate.stretch_to_fit_width(5.2), FadeIn(left_g), run_time=0.7)
        self.play(right_box.animate.stretch_to_fit_width(5.2), FadeIn(right_g), run_time=0.7)
        self.wait(0.4)

        tag = Text("Not a highlight reel — the actual log.",
                    color=PALETTE["accent"], font_size=20)
        tag.next_to(row, DOWN, buff=0.5)
        self.play(FadeIn(tag, shift=UP * 0.15), run_time=0.6)

        self.wait(1.3)
