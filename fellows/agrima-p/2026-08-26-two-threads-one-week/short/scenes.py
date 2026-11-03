"""
Portrait (9:16) Manim scenes for the two-threads-one-week Short.
Manim's coordinate frame for a 2160x3840 (9:16) render is ~4.5 units wide x
8 units tall (vs ~14.2 x 8 landscape) — everything here is laid out for that
narrow, tall canvas: single-column stacks instead of side-by-side columns.

B01_AgrimaIntro — presenter intro + one-line week summary
B04_LogV1       — weekly_log_v1.py run for real: two stacked plain logs
B07_LogV2       — weekly_log_v2.py run for real: SAME logs + a standout per thread
B08_Summary     — the log, restated — not a highlight reel

(No beats were dropped from this Short — the parent reel is only 2:05,
already under the 3:00 Shorts cap — so all 11 beats + endcard carry over.)
"""

from manim import *

# Manim does NOT auto-derive the coordinate frame from -r's pixel resolution
# — this must be set explicitly; 4.5x8.0 matches manim_layout_audit.py's own
# --portrait GATE B check, so it's the house-standard portrait value.
config.frame_width = 4.5
config.frame_height = 8.0

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
        corner_radius=0.1, width=width, height=height,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=PALETTE["border"], stroke_width=1.5,
    )


class B01_AgrimaIntro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=30)
        summary = Text(
            "This week split two ways —\nwriting about AI, and hands-on\n"
            "work for the Loon Project,\ntracking Minnesota's common\n"
            "loons by drone. This is the\nlog, not the highlights.",
            color=PALETTE["ink"], font_size=18, line_spacing=1.35, should_center=True,
        )
        if summary.width > 3.7:
            summary.scale_to_fit_width(3.7)
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.6)
        rule.stretch(0.01, 0)
        self.play(rule.animate.stretch_to_fit_width(1.4), run_time=0.35)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.2)


# Shared single-column log-block renderer for B04 / B07. A plain function,
# not a shared base class — run.sh discovers Manim scenes via a regex
# requiring each scene class to inherit directly from Scene, so both real
# scene classes below call this helper from their own construct().
def _log_block(scene, items, header, top_y, show_highlight=False, font_size=13):
    head = Text(header, color=PALETTE["ink"], font_size=15)
    head.move_to([0, top_y, 0])
    rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["accent"], stroke_width=2)
    rule.next_to(head, DOWN, buff=0.1)

    scene.play(FadeIn(head), run_time=0.22)
    rule.stretch(0.01, 0)
    scene.play(rule.animate.stretch_to_fit_width(3.0), run_time=0.22)

    prev = rule
    if show_highlight:
        standout = next(i for i in items if i["status"] in ("done", "published"))
        hl = Text(f"* highlight: {standout['item']}", color=PALETTE["accent"], font_size=font_size)
        if hl.width > 3.9:
            hl.scale_to_fit_width(3.9)
        hl.next_to(rule, DOWN, buff=0.12)
        hl.set_x(0)
        scene.play(FadeIn(hl, shift=RIGHT * 0.1), run_time=0.22)
        prev = hl

    rows = VGroup()
    for it in items:
        done = it["status"] in ("done", "published")
        row = Text(
            f"- {it['item']} ({it['status']})",
            color=PALETTE["ink"] if done else PALETTE["dim"], font_size=font_size,
        )
        if row.width > 3.9:
            row.scale_to_fit_width(3.9)
        rows.add(row)
    rows.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
    rows.next_to(prev, DOWN, buff=0.16)
    rows.set_x(0)

    for row in rows:
        scene.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.18)

    block = VGroup(head, rule, rows)
    if show_highlight:
        block.add(hl)
    return block, block.get_bottom()[1]


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
                      font_size=19).to_edge(UP, buff=0.7)
        if title.width > 3.9:
            title.scale_to_fit_width(3.9)
        sub = Text("this week, logged", color=PALETTE["dim"],
                    font_size=13).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), FadeIn(sub), run_time=0.4)

        top_y = sub.get_bottom()[1] - 0.3
        _, bottom1 = _log_block(self, WEEK["writing"], "WRITING", top_y)
        _, bottom2 = _log_block(self, WEEK["loon_project"], "LOON PROJECT", bottom1 - 0.3)

        self.wait(0.9)


class B07_LogV2(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Run it again — weekly_log_v2.py", color=PALETTE["ink"],
                      font_size=19).to_edge(UP, buff=0.7)
        if title.width > 3.9:
            title.scale_to_fit_width(3.9)
        sub = Text("the SAME log, now with a standout", color=PALETTE["dim"],
                    font_size=12).next_to(title, DOWN, buff=0.1)
        if sub.width > 3.9:
            sub.scale_to_fit_width(3.9)
        self.play(Write(title), FadeIn(sub), run_time=0.4)

        top_y = sub.get_bottom()[1] - 0.3
        _, bottom1 = _log_block(self, WEEK["writing"], "WRITING", top_y, show_highlight=True)
        _log_block(self, WEEK["loon_project"], "LOON PROJECT", bottom1 - 0.3, show_highlight=True)

        self.wait(1.0)


class B08_Summary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Two threads, one week — the log", color=PALETTE["ink"],
                      font_size=20).to_edge(UP, buff=0.7)
        if title.width > 3.9:
            title.scale_to_fit_width(3.9)
        self.play(Write(title), run_time=0.6)

        top_card = card_bg(3.9, 1.9)
        top_head = Text("WRITING", color=PALETTE["good"], font_size=16)
        top_body = Text(
            "Fashion's new data brain:\nforecasting, generative design,\n"
            "virtual try-on. Open-source\ngap — nearly closed.",
            color=PALETTE["ink"], font_size=12.5, line_spacing=1.25)
        top_g = VGroup(top_head, top_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        top = VGroup(top_card, top_g.move_to(top_card.get_center()))

        bot_card = card_bg(3.9, 1.9)
        bot_head = Text("LOON PROJECT", color=PALETTE["good"], font_size=16)
        bot_body = Text(
            "Drone in hand, FAA path\nresearched, strategy written.\n"
            "Certification, footage, training:\nstill in progress.",
            color=PALETTE["ink"], font_size=12.5, line_spacing=1.25)
        bot_g = VGroup(bot_head, bot_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        bot = VGroup(bot_card, bot_g.move_to(bot_card.get_center()))

        col = VGroup(top, bot).arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=0.4)
        top_card.stretch(0.01, 0)
        bot_card.stretch(0.01, 0)
        self.play(top_card.animate.stretch_to_fit_width(3.9), FadeIn(top_g), run_time=0.6)
        self.play(bot_card.animate.stretch_to_fit_width(3.9), FadeIn(bot_g), run_time=0.6)
        self.wait(0.3)

        tag = Text("Not a highlight reel — the actual log.",
                    color=PALETTE["accent"], font_size=14)
        if tag.width > 3.9:
            tag.scale_to_fit_width(3.9)
        tag.next_to(col, DOWN, buff=0.35)
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.5)
        self.wait(1.0)
