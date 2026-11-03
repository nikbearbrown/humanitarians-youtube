"""
Manim scenes for ai-support-shift
B01_WhyShift       — why companies are making the shift (cost, 24/7, instant)
B04_OldBotFails     — support_bot_v1.py run on 3 messages; 1 misses
B07_NewBotUnderstands — support_bot_v2.py run on the SAME 3 messages; all land
B08_Summary         — old vs new recap + the tradeoffs that still remain
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


class B00B_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = Text("Hi, I'm Agrima.", color=PALETTE["ink"], font_size=40)
        summary = Text(
            "This video looks at what actually changes when a company\n"
            "swaps an old rule-based support bot for a modern AI chatbot —\n"
            "why companies make the switch, and where the tradeoffs still show up.",
            color=PALETTE["ink"], font_size=22, line_spacing=1.35, should_center=True,
        )
        rule = Line(LEFT * 0.9, RIGHT * 0.9, color=PALETTE["accent"], stroke_width=3)

        group = VGroup(name, rule, summary).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.7)
        rule.stretch(0.01, 0)
        self.play(rule.animate.stretch_to_fit_width(1.8), run_time=0.4)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.wait(1.3)


class B01_WhyShift(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Why companies are making the shift",
                      color=PALETTE["ink"], font_size=34).to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.8)

        points = [
            ("Cost", "Thousands of chats\nfor a fraction\nof the price"),
            ("24/7 Availability", "No nights,\nweekends,\nor holidays"),
            ("Instant Response", "No hold music —\nreplies in\nseconds"),
        ]

        cols = VGroup()
        for label, sub in points:
            box = card_bg(3.6, 3.2)
            head = Text(label, color=PALETTE["accent"], font_size=24)
            body = Text(sub, color=PALETTE["ink"], font_size=16, line_spacing=1.25).next_to(head, DOWN, buff=0.35)
            group = VGroup(box, VGroup(head, body).move_to(box.get_center()))
            cols.add(group)
        cols.arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.7)

        for c in cols:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.7)
            self.wait(0.3)

        self.wait(1.2)


# Shared chat-bubble renderer for B04 / B07. A plain function, not a shared
# base class — run.sh discovers Manim scenes via a regex that requires each
# scene class to inherit directly from Scene, so both real scene classes
# below do that and just CALL this helper from their own construct().
def _bubble(text, text_color, border_color, font_size=14):
    txt = Text(text, color=text_color, font_size=font_size, line_spacing=1.1, should_center=True)
    box = RoundedRectangle(
        corner_radius=0.12,
        width=txt.width + 0.4, height=txt.height + 0.32,
        fill_color=PALETTE["card"], fill_opacity=1,
        stroke_color=border_color, stroke_width=2.2,
    )
    txt.move_to(box.get_center())
    return VGroup(box, txt)


def _construct_chat(scene, headline, subfile, script):
    scene.camera.background_color = PALETTE["bg"]

    head = Text(headline, color=PALETTE["ink"], font_size=21).to_edge(UP, buff=0.65)
    sub = Text(subfile, color=PALETTE["dim"], font_size=14).next_to(head, DOWN, buff=0.12)
    scene.play(Write(head), FadeIn(sub), run_time=0.5)

    n = len(script)
    top = sub.get_bottom()[1] - 0.45
    bottom = -3.5
    row_h = (top - bottom) / n

    for i, (user_line, bot_line, tag, tag_color) in enumerate(script):
        row_y = top - row_h * (i + 0.5)

        user_bub = _bubble(user_line, PALETTE["ink"], PALETTE["border"], font_size=14)
        user_bub.move_to([-3.3, row_y, 0])
        # the box GROWS into place (genuine shape change, not just a fade)
        user_bub[0].stretch(0.01, 0)
        scene.play(user_bub[0].animate.stretch_to_fit_width(user_bub[1].width + 0.4),
                   FadeIn(user_bub[1]), run_time=0.35)

        bot_color = tag_color if tag_color else PALETTE["border"]
        bot_bub = _bubble(bot_line, PALETTE["ink"], bot_color, font_size=14)
        bot_bub.move_to([3.1, row_y, 0])
        bot_bub[0].stretch(0.01, 0)
        scene.play(bot_bub[0].animate.stretch_to_fit_width(bot_bub[1].width + 0.4),
                   FadeIn(bot_bub[1]), run_time=0.35)

        if tag:
            tag_txt = Text(tag, color=tag_color, font_size=13)
            tag_txt.next_to(bot_bub, DOWN, buff=0.06).align_to(bot_bub, RIGHT)
            scene.play(FadeIn(tag_txt), run_time=0.25)

        scene.wait(0.2)

    scene.wait(1.0)


B04_SCRIPT = [
    ("\"how do I reset my password\"",
     "\"Go to Settings > Security\n> Reset Password.\"", None, None),
    ("\"I want my money back\nfor this refund\"",
     "\"Refunds take 5-7\nbusiness days.\"", None, None),
    ("\"my card was charged twice by\nmistake and I'm really upset\"",
     "\"Sorry, I didn't understand.\nPress 1 for billing...\"",
     "MISSED — no keyword matched", PALETTE["miss"]),
]

B07_SCRIPT = [
    ("\"how do I reset my password\"",
     "\"Go to Settings > Security\n> Reset Password.\"", None, None),
    ("\"I want my money back\nfor this refund\"",
     "\"Refunds take 5-7\nbusiness days.\"", None, None),
    ("\"my card was charged twice by\nmistake and I'm really upset\"",
     "\"Refunds take 5-7 days. This\nsounds frustrating — connecting\nyou to a human now.\"",
     "UNDERSTOOD + escalated to a human", PALETTE["good"]),
]


class B04_OldBotFails(Scene):
    def construct(self):
        _construct_chat(self, "Run it — support_bot_v1.py (keyword matching)",
                         "3 real messages, tested", B04_SCRIPT)


class B07_NewBotUnderstands(Scene):
    def construct(self):
        _construct_chat(self, "Run it again — support_bot_v2.py (intent + urgency)",
                         "the SAME 3 messages", B07_SCRIPT)


class B08_Summary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("Same 3 messages. Different bot.",
                      color=PALETTE["ink"], font_size=28).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        old_box = card_bg(4.6, 2.6)
        old_head = Text("OLD — keyword rules", color=PALETTE["miss"], font_size=20)
        old_body = Text("Matches exact words only.\nAnything phrased differently\nfalls through.",
                         color=PALETTE["ink"], font_size=16, line_spacing=1.3)
        old_g = VGroup(old_head, old_body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        old_card = VGroup(old_box, old_g.move_to(old_box.get_center()))

        new_box = card_bg(4.6, 2.6)
        new_head = Text("NEW — intent + urgency", color=PALETTE["good"], font_size=20)
        new_body = Text("Understands meaning, not just\nwords — and knows when to\nhand off to a person.",
                         color=PALETTE["ink"], font_size=16, line_spacing=1.3)
        new_g = VGroup(new_head, new_body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        new_card = VGroup(new_box, new_g.move_to(new_box.get_center()))

        row = VGroup(old_card, new_card).arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.5)
        old_box.stretch(0.01, 0)
        new_box.stretch(0.01, 0)
        self.play(old_box.animate.stretch_to_fit_width(4.6), FadeIn(old_g), run_time=0.7)
        self.play(new_box.animate.stretch_to_fit_width(4.6), FadeIn(new_g), run_time=0.7)
        self.wait(0.4)

        still_head = Text("Still true either way:", color=PALETTE["accent"], font_size=20)
        still_body = Text(
            "Complex or emotionally-loaded issues • edge cases no one wrote a rule for • trust is earned, not assumed",
            color=PALETTE["ink"], font_size=16, line_spacing=1.3,
        )
        still = VGroup(still_head, still_body).arrange(DOWN, buff=0.2).next_to(row, DOWN, buff=0.55)
        self.play(FadeIn(still, shift=UP * 0.15), run_time=0.6)

        self.wait(1.3)
