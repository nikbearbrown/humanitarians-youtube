"""
Manim scenes for patent-agent-video12-baseline-results
B01_LabeledTestSet     — 1 query -> 160 patents -> 16 patents -> 50 claims, labeled by hand
B02_AccuracyVsKappa    — accuracy next to the always-same-answer baseline, then kappa
B03_LeansTheOtherWay   — 11 broad/offensive predictions, 10 labeled narrow; label caveat
B04_RefusalBug         — mid-answer refusal broke the parser; stop_reason fix; 50/50 scored

Every number on screen is from this session's real runs:
  pull: one query, $0.92 list price, 160 candidate patents; 50 claims from
  16 patents, 2 per CPC section A-H; labels 46 narrow / 4 broad, 50 defensive.
  baseline (50 claims): breadth acc 0.66, kappa 0.08, majority 0.92;
  posture acc 0.60, kappa 0.00, majority 1.00; 11 predicted broad/offensive,
  10 of them labeled narrow. Cost upper bound $0.32 (actual not recorded).
  diagnostic call: stop_reason=refusal, 155 of 1000 output tokens.
"""
from manim import *

PALETTE = {
    "bg":     "#F3EBDD",
    "ink":    "#2F2A26",
    "teal":   "#1F4E5F",
    "crimson": "#E4572E",
    "slate":  "#29335C",
    "gold":   "#F3A712",
    "sage":   "#A8C686",
}

BODY_FONT = "Menlo"


def make_title(line1, line2, font_size=22):
    t1 = Text(line1, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
    if line2:
        t2 = Text(line2, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.15)
    else:
        title = VGroup(t1)
    title.to_edge(UP, buff=0.7)
    title.move_to([0, title.get_y(), 0])
    return title


def card(text, color, width, height=0.8, font_size=15, text_color=None):
    box = RoundedRectangle(
        corner_radius=0.1, width=width, height=height,
        fill_color=PALETTE[color], fill_opacity=0.08,
        stroke_color=PALETTE[color], stroke_width=1.5
    )
    label = Text(text, color=PALETTE[text_color or color], font_size=font_size,
                 font=BODY_FONT, line_spacing=1.2).move_to(box.get_center())
    return VGroup(box, label)


def bar_row(label, value, max_value, color, width=5.0, value_text=None):
    name = Text(label, color=PALETTE["ink"], font_size=14, font=BODY_FONT)
    bar = Rectangle(width=max(width * value / max_value, 0.04), height=0.42,
                    fill_color=PALETTE[color], fill_opacity=0.7,
                    stroke_color=PALETTE[color], stroke_width=1)
    num = Text(value_text or f"{value:.2f}", color=PALETTE["ink"], font_size=14, font=BODY_FONT)
    return name, bar, num


class B01_LabeledTestSet(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Labeled", "Test Set")
        self.add(title)

        # State 1 — last week: one query narrowed to the test set
        funnel = VGroup(
            card("1 query\n$0.92", "slate", 2.0, 1.0),
            card("160\npatents", "teal", 2.0, 1.0),
            card("16\npatents", "teal", 2.0, 1.0),
            card("50\nclaims", "gold", 2.0, 1.0, text_color="ink"),
        ).arrange(RIGHT, buff=0.45).move_to([0, 1.0, 0])
        arrows = VGroup(*[
            Arrow(funnel[i].get_right(), funnel[i + 1].get_left(), buff=0.08,
                  color=PALETTE["ink"], stroke_width=2)
            for i in range(3)
        ])
        for i, f in enumerate(funnel):
            self.play(Create(f[0]), Write(f[1]), run_time=0.7)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)
        self.wait(4.0)

        # State 2 — two patents from each of the eight CPC sections
        sections = VGroup(*[
            card(f"{s}  x2", "slate", 0.95, 0.6, font_size=14) for s in "ABCDEFGH"
        ]).arrange(RIGHT, buff=0.12).move_to([0, -0.4, 0])
        self.play(LaggedStart(*[Create(s[0]) for s in sections], lag_ratio=0.1), run_time=1.2)
        self.play(LaggedStart(*[Write(s[1]) for s in sections], lag_ratio=0.1), run_time=1.0)
        self.wait(5.0)

        # State 3 — this week: every claim labeled by hand
        label = card("labeled by hand: breadth + posture + a note on each",
                     "teal", 7.8, 0.75, font_size=15).move_to([0, -1.6, 0])
        self.play(Create(label[0]), Write(label[1]), run_time=1.0)
        self.play(Indicate(funnel[3], color=PALETTE["gold"]), run_time=1.0)
        self.wait(3.9)

        bottom = Text("labels: 46 narrow / 4 broad  ·  50 defensive",
                      color=PALETTE["slate"], font_size=15, font=BODY_FONT).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)


class B02_AccuracyVsKappa(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Accuracy vs.", "Kappa")
        self.add(title)

        # State 1 — classifier accuracy on both dimensions
        rows = VGroup()
        bars = []
        for lbl, val, color in [("breadth accuracy", 0.66, "teal"),
                                ("posture accuracy", 0.60, "teal")]:
            name, bar, num = bar_row(lbl, val, 1.0, color)
            rows.add(VGroup(name, bar, num))
            bars.append((name, bar, num))
        self._layout(rows, top=1.4)
        for name, bar, num in bars:
            self.play(Write(name), run_time=0.5)
            self.play(Create(bar), Write(num), run_time=0.8)
        self.wait(3.5)

        # State 2 — the always-same-answer baseline beats it
        base = VGroup()
        base_parts = []
        for lbl, val, txt in [("always 'narrow'", 0.92, "0.92"),
                              ("always 'defensive'", 1.00, "1.00")]:
            name, bar, num = bar_row(lbl, val, 1.0, "crimson", value_text=txt)
            base.add(VGroup(name, bar, num))
            base_parts.append((name, bar, num))
        self._layout(base, top=-0.1)
        for name, bar, num in base_parts:
            self.play(Write(name), run_time=0.5)
            self.play(Create(bar), Write(num), run_time=0.8)
        self.wait(6.0)

        # State 3 — kappa corrects for chance
        self.play(FadeOut(rows), FadeOut(base), run_time=0.6)
        kappa = VGroup(
            card("breadth   kappa 0.08", "crimson", 3.8, 0.9, font_size=16),
            card("posture   kappa 0.00", "crimson", 3.8, 0.9, font_size=16),
        ).arrange(RIGHT, buff=0.4).move_to([0, 0.7, 0])
        for k in kappa:
            self.play(Create(k[0]), Write(k[1]), run_time=0.9)
        self.play(Indicate(kappa, color=PALETTE["gold"]), run_time=1.0)
        note = card("kappa = agreement beyond chance  ·  0 = no better than chance",
                    "gold", 8.0, 0.8, font_size=14, text_color="ink").move_to([0, -0.9, 0])
        self.play(Create(note[0]), Write(note[1]), run_time=1.0)
        self.wait(5.3)

        bottom = Text("50 claims  ·  cost at most $0.32",
                      color=PALETTE["slate"], font_size=15, font=BODY_FONT).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)

    def _layout(self, rows, top):
        for i, row in enumerate(rows):
            name, bar, num = row
            y = top - i * 0.65
            name.move_to([-3.9 + name.width / 2, y, 0])
            bar.move_to([-1.2 + bar.width / 2, y, 0])
            num.next_to(bar, RIGHT, buff=0.2)


class B03_LeansTheOtherWay(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("It Leaned", "the Other Way")
        self.add(title)

        # State 1 — expected vs measured
        expected = card("expected\nnarrow / defensive", "slate", 3.6, 1.1).move_to([-2.1, 1.1, 0])
        measured = card("measured\n11 broad / offensive", "crimson", 3.6, 1.1).move_to([2.1, 1.1, 0])
        self.play(Create(expected[0]), Write(expected[1]), run_time=0.9)
        self.wait(1.5)
        self.play(Create(measured[0]), Write(measured[1]), run_time=0.9)
        self.wait(2.0)

        # State 2 — 10 of those 11 were labeled narrow
        dots = VGroup(*[
            Circle(radius=0.17, stroke_width=1.5,
                   stroke_color=PALETTE["crimson" if i < 10 else "sage"],
                   fill_color=PALETTE["crimson" if i < 10 else "sage"], fill_opacity=0.6)
            for i in range(11)
        ]).arrange(RIGHT, buff=0.18).move_to([0, -0.15, 0])
        self.play(LaggedStart(*[Create(d) for d in dots], lag_ratio=0.12), run_time=1.6)
        tally = Text("10 of the 11: I labeled narrow",
                     color=PALETTE["crimson"], font_size=15, font=BODY_FONT).next_to(dots, DOWN, buff=0.25)
        self.play(Write(tally), run_time=0.9)
        self.wait(3.5)

        # State 3 — why: functional wording vs named parts
        self.play(FadeOut(dots), FadeOut(tally), run_time=0.5)
        why = VGroup(
            card('model: "configured to", "a protrusion"\n-> broad', "crimson", 4.0, 1.1, font_size=14),
            card("me: named parts, specific limits\n-> narrow", "teal", 4.0, 1.1, font_size=14),
        ).arrange(RIGHT, buff=0.3).move_to([0, -0.3, 0])
        for w in why:
            self.play(Create(w[0]), Write(w[1]), run_time=0.9)
            self.wait(2.5)
        self.wait(2.5)

        # State 4 — the caveat
        caveat = card("caveat: all 50 labels are defensive\nposture needs offensive + broad examples",
                      "gold", 7.6, 1.0, font_size=14, text_color="ink").move_to([0, -1.85, 0])
        self.play(Create(caveat[0]), Write(caveat[1]), run_time=1.1)
        self.wait(2.2)
        self.play(Indicate(caveat, color=PALETTE["gold"]), run_time=1.0)
        self.wait(1.0)


class B04_RefusalBug(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Refusal", "Bug")
        self.add(title)

        # State 1 — three failing claims on one patent
        patent = card("US-11766760-B2 · cryogenic grinding", "slate", 6.4, 0.7).move_to([0, 1.5, 0])
        claims = VGroup(*[
            card(f"claim {n}  failed", "crimson", 2.2, 0.6, font_size=14) for n in (1, 5, 7)
        ]).arrange(RIGHT, buff=0.3).move_to([0, 0.6, 0])
        self.play(Create(patent[0]), Write(patent[1]), run_time=0.9)
        self.play(LaggedStart(*[Create(c[0]) for c in claims], lag_ratio=0.2), run_time=0.9)
        self.play(LaggedStart(*[Write(c[1]) for c in claims], lag_ratio=0.2), run_time=0.8)
        tokens = Text("max_tokens 500 -> 1000: still failed",
                      color=PALETTE["ink"], font_size=14, font=BODY_FONT).move_to([0, -0.2, 0])
        self.play(Write(tokens), run_time=0.9)
        self.wait(3.5)

        # State 2 — the diagnostic call
        diag = card('stop_reason: "refusal"  ·  155 of 1000 tokens\n{"breadth": "broad", "posture": ... (cut off)',
                    "crimson", 7.8, 1.1, font_size=14).move_to([0, -1.2, 0])
        self.play(Create(diag[0]), Write(diag[1]), run_time=1.2)
        self.play(Indicate(diag, color=PALETTE["gold"]), run_time=1.0)
        self.wait(4.5)

        # State 3 — the fix
        self.play(FadeOut(claims), FadeOut(tokens), FadeOut(diag), run_time=0.6)
        before = card("before:  if not message.content", "slate", 7.8, 0.7, font_size=14).move_to([0, 0.5, 0])
        after = card('after:   ... or stop_reason == "refusal"  ->  declined',
                     "teal", 7.8, 0.7, font_size=14).move_to([0, -0.4, 0])
        self.play(Create(before[0]), Write(before[1]), run_time=0.9)
        self.wait(2.5)
        self.play(Create(after[0]), Write(after[1]), run_time=0.9)
        self.wait(4.7)

        result = card("50 / 50 claims scored  ·  next: the prompt fix",
                      "sage", 7.8, 0.7, font_size=15, text_color="ink").move_to([0, -1.4, 0])
        self.play(Create(result[0]), Write(result[1]), run_time=1.0)
        self.wait(1.0)
