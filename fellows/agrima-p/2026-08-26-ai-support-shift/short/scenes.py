"""
Portrait (9:16) Manim scenes for the ai-support-shift Short.
Manim's coordinate frame for a 2160x3840 (9:16) render is ~4.5 units wide x
8 units tall (vs ~14.2 x 8 landscape) — everything here is laid out for that
narrow, tall canvas: single-column stacks instead of side-by-side columns/rows.
B00B_ExecSummary    — presenter intro + one-line video summary
B04_OldBotFails     — support_bot_v1.py run on 3 messages; 1 misses
B07_NewBotUnderstands — support_bot_v2.py run on the SAME 3 messages; all land
(B01_WhyShift and B08_Summary are NOT in this Short — auto-dropped by the
 cap-check to make room for the added B00B intro; they only exist in the long.)
"""

from manim import *

# Manim does NOT auto-derive the coordinate frame from -r's pixel resolution
# — config.frame_width stays the landscape default (~14.22) regardless of
# pixel_width/height, so a scene laid out for a "4.5 units wide" portrait
# canvas actually rendered into that wide frame, landing tiny and center-
# clustered in the portrait pixel buffer (effectively a center-crop). This
# must be set explicitly; 4.5x8.0 also matches what manim_layout_audit.py's
# own --portrait GATE B check hardcodes, so it's the house-standard value.
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


class B00B_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=30)
        summary = Text(
            "This video looks at what actually\nchanges when a company swaps an\n"
            "old rule-based support bot for a\nmodern AI chatbot — why companies\n"
            "make the switch, and where the\ntradeoffs still show up.",
            color=PALETTE["ink"], font_size=18, line_spacing=1.35, should_center=True,
        )
        if summary.width > 3.7:
            summary.scale_to_fit_width(3.7)
        rule = Line(LEFT * 0.7, RIGHT * 0.7, color=PALETTE["accent"], stroke_width=3)

        group = VGroup(name, rule, summary).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.6)
        rule.stretch(0.01, 0)
        self.play(rule.animate.stretch_to_fit_width(1.4), run_time=0.35)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.2)


def _bubble(text, text_color, border_color, font_size=13, max_w=3.0):
    txt = Text(text, color=text_color, font_size=font_size, line_spacing=1.1, should_center=True)
    if txt.width > max_w:
        txt.scale_to_fit_width(max_w)
    box = RoundedRectangle(
        corner_radius=0.1,
        width=txt.width + 0.36, height=txt.height + 0.28,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=border_color, stroke_width=2,
    )
    txt.move_to(box.get_center())
    return VGroup(box, txt)


def _construct_chat(scene, headline, subfile, script):
    scene.camera.background_color = PALETTE["bg"]

    head = Text(headline, color=PALETTE["ink"], font_size=16, line_spacing=1.2,
                should_center=True)
    if head.width > 3.6:
        head.scale_to_fit_width(3.6)
    head.to_edge(UP, buff=0.85)
    sub = Text(subfile, color=PALETTE["dim"], font_size=13).next_to(head, DOWN, buff=0.12)
    scene.play(Write(head), FadeIn(sub), run_time=0.5)

    n = len(script)
    top = sub.get_bottom()[1] - 0.35
    # bottom is conservative: the LAST row's optional tag_txt renders BELOW
    # its row's own budget (not divided into row_h), so this must leave a
    # full tag's worth of extra headroom above the real safe-area floor
    # (~y=-3.4 at 9:16) or the tag clips past it.
    bottom = -2.5
    row_h = (top - bottom) / n

    for i, (user_line, bot_line, tag, tag_color) in enumerate(script):
        row_top = top - row_h * i

        user_bub = _bubble(user_line, PALETTE["ink"], PALETTE["border"], font_size=13, max_w=2.6)
        user_bub.move_to([0.55, row_top - user_bub.height / 2 - 0.05, 0])
        user_bub[0].stretch(0.01, 0)
        scene.play(user_bub[0].animate.stretch_to_fit_width(user_bub[1].width + 0.36),
                   FadeIn(user_bub[1]), run_time=0.3)

        bot_color = tag_color if tag_color else PALETTE["border"]
        bot_y = row_top - user_bub.height - 0.22
        bot_bub = _bubble(bot_line, PALETTE["ink"], bot_color, font_size=13, max_w=2.9)
        bot_bub.move_to([-0.45, bot_y - bot_bub.height / 2, 0])
        bot_bub[0].stretch(0.01, 0)
        scene.play(bot_bub[0].animate.stretch_to_fit_width(bot_bub[1].width + 0.36),
                   FadeIn(bot_bub[1]), run_time=0.3)

        if tag:
            tag_txt = Text(tag, color=tag_color, font_size=11).scale_to_fit_width(min(2.6, 2.6))
            tag_txt.next_to(bot_bub, DOWN, buff=0.05).align_to(bot_bub, LEFT)
            scene.play(FadeIn(tag_txt), run_time=0.2)

        scene.wait(0.15)

    scene.wait(0.8)


B04_SCRIPT = [
    ("\"reset my password\"",
     "\"Go to Settings >\nSecurity > Reset.\"", None, None),
    ("\"money back for\nthis refund\"",
     "\"Refunds take\n5-7 days.\"", None, None),
    ("\"charged twice by mistake,\nI'm really upset\"",
     "\"Sorry, I didn't\nunderstand. Press 1...\"",
     "MISSED", PALETTE["miss"]),
]

B07_SCRIPT = [
    ("\"reset my password\"",
     "\"Go to Settings >\nSecurity > Reset.\"", None, None),
    ("\"money back for\nthis refund\"",
     "\"Refunds take\n5-7 days.\"", None, None),
    ("\"charged twice by mistake,\nI'm really upset\"",
     "\"Refunds take 5-7 days.\nConnecting you to a human.\"",
     "UNDERSTOOD + escalated", PALETTE["good"]),
]


class B04_OldBotFails(Scene):
    def construct(self):
        _construct_chat(self, "support_bot_v1.py\n(keyword matching)",
                         "3 real messages, tested", B04_SCRIPT)


class B07_NewBotUnderstands(Scene):
    def construct(self):
        _construct_chat(self, "support_bot_v2.py\n(intent + urgency)",
                         "the SAME 3 messages", B07_SCRIPT)
