"""
Manim scenes for 2026-07-27-how-facial-recognition-actually-works

Restructured 2026-08-05 per a PROOF.md rubric review: the reusable framework
now comes BEFORE the examples (was previously narrated as a conclusion at
the end), the low/high-stakes examples are explicitly tagged as instances of
that framework, a worked example applies the framework live to a concrete
case, and a real scaffolded CTA was added (there was none before).

B00_EverywhereHook   — phone/airport/store/policing icons, debate framing (HOOK)
B01_FrameworkLens    — the reusable lens: 3 questions, shown before any example (FRAMEWORK)
B02_PipelineMechanism — detect -> embed -> compare -> similarity score, tagged Q3 (MECHANISM)
B03_LegitimateUses    — accessibility, unlock, missing persons, medical — tagged LOW-STAKES (BENEFITS)
B04_HarmfulUses       — mass surveillance, retail tracking, biometric risk — tagged HIGH-STAKES (HARMS)
B05_NistEvidence      — NIST FRVT: real gap for most, near-zero for the best; dissent named on screen (EVIDENCE)
B06_FluencyTrap       — a fluent paragraph and a match score both look certain (FRAMEWORK-CALLBACK)
B07_WorkedExample     — the lens applied live to a retail loss-prevention case (WORKED-EXAMPLE)
B08_YourTurn          — a real scaffolded task, not a vague pointer (CTA)
B09_BrandOutro        — @HumanitariansAI, in for Sai Pranavi Jeedigunta (SIGN-OFF)

Palette: humanitarians (runtime/remotion/src/tokens/humanitarians.ts) —
this reel uses the hai/Bella persona, not the Claude-branded palette.

Lessons carried over from the 2026-07-26 reel's build (see its BUILD-LOG.md):
- Never use Integer/DecimalNumber/MathTex/Tex — they render via LaTeX, which
  is not installed here. Animated numbers use Text + ValueTracker instead.
- Never call .to_edge(LEFT) / .to_edge(RIGHT) on a wide mobject — the
  toolkit's static WCAG/margin checker (GATE W) estimates position assuming
  a small fixed half-width, which badly misplaces wide text. Center wide
  content with .move_to() instead.
- Never draw a literal Line across a Text mobject as a "strikethrough" —
  GATE B's post-render layout audit flags any text sitting on a line.
- Every scene needs at least one non-text SHAPE whose position/size changes
  at least once — GATE A's static shape-distinctness check flags scenes
  that are all-text (or where a SurroundingRectangle's only child is Text,
  which the checker misclassifies as text-like) as "repeated animation".
- Never chain two `.animate` calls in one `self.play()` (e.g.
  `.animate.stretch_to_fit_width(w).move_to(p)`) — real Manim supports it,
  but the toolkit's static mock checker (GATE A) does not and raises
  AttributeError. Use a ValueTracker + always_redraw instead.
- Settle into the final static state comfortably before 50% of the scene's
  own native runtime — GATE V samples at 50%/85% of the (post-stretch) beat
  duration, and a mid-animation frame at those points reads as a defect.
"""

from manim import *

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool
    "crimson": "#E4572E", # bad / CVD-safe warm
    "slate":  "#29335C",  # structure
    "gold":   "#F3A712",  # fill only
    "sage":   "#A8C686",  # human / growth
}

MONO = "Courier New"


def fit(mob, max_w):
    """Scale down only if wider than max_w — never scale up short text to an
    artificial fixed width (that starves neighboring elements of room)."""
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


class B00_EverywhereHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Facial recognition is everywhere right now",
            color=PALETTE["ink"], font_size=30
        ), 11.0)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)
        self.wait(0.3)

        contexts = [
            ("Phone", PALETTE["teal"]),
            ("Airport", PALETTE["slate"]),
            ("Store", PALETTE["gold"]),
            ("Policing", PALETTE["crimson"]),
        ]
        chips = VGroup()
        for label, color in contexts:
            chip = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15,
                                     fill_color=color, fill_opacity=0.18,
                                     stroke_color=color, stroke_width=2.5)
            txt = Text(label, color=PALETTE["ink"], font_size=24).move_to(chip)
            chips.add(VGroup(chip, txt))
        chips.arrange(RIGHT, buff=0.5).move_to(UP * 0.7)

        for c in chips:
            self.play(FadeIn(c, scale=1.1), run_time=0.5)
        self.wait(0.4)

        debate = fit(Text(
            "There's real, unresolved disagreement about whether that's okay.",
            color=PALETTE["crimson"], font_size=26
        ), 10.5)
        debate.move_to(DOWN * 2.3)
        self.play(Write(debate), run_time=1.0)
        self.wait(6.0)


class B01_FrameworkLens(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("The lens", color=PALETTE["ink"], font_size=32), 10.5)
        title.move_to(UP * 3.0)
        self.play(Write(title), run_time=0.6)
        self.wait(0.2)

        questions = [
            "What's it used for?",
            "What happens if it's wrong?",
            "How confident is the claim, really?",
        ]
        y = 1.9
        for i, q in enumerate(questions, start=1):
            badge = Circle(radius=0.28, color=PALETTE["slate"], stroke_width=2.2,
                            fill_color=PALETTE["slate"], fill_opacity=0.15)
            num = Text(str(i), color=PALETTE["ink"], font_size=22).move_to(badge)
            label = fit(Text(q, color=PALETTE["ink"], font_size=25), 8.5)
            badge.move_to(LEFT * 4.6 + UP * y)
            num.move_to(badge)
            label.next_to(badge, RIGHT, buff=0.35)
            self.play(FadeIn(badge, scale=1.2), FadeIn(num), Write(label), run_time=0.7)
            self.wait(0.2)
            y -= 0.95
        self.wait(0.3)

        track = RoundedRectangle(width=8.4, height=0.45, corner_radius=0.2,
                                  fill_color=PALETTE["ink"], fill_opacity=0.07,
                                  stroke_color=PALETTE["slate"], stroke_width=1.4)
        track.move_to(DOWN * 1.8)
        self.play(FadeIn(track), run_time=0.4)

        fill_tracker = ValueTracker(0.01)
        fill = always_redraw(lambda: Rectangle(
            width=max(0.02, 8.4 * 0.98 * fill_tracker.get_value()), height=0.45,
            fill_opacity=0.9, stroke_width=0
        ).set_fill(color=[PALETTE["sage"], PALETTE["gold"], PALETTE["crimson"]])
         .move_to(track.get_left() + RIGHT * (8.4 * 0.98 * fill_tracker.get_value()) / 2))
        self.add(fill)
        self.play(fill_tracker.animate.set_value(1.0), run_time=1.0)

        low = Text("low-stakes", color=PALETTE["sage"], font_size=16).next_to(track, DOWN, buff=0.25).align_to(track, LEFT)
        high = Text("high-stakes", color=PALETTE["crimson"], font_size=16).next_to(track, DOWN, buff=0.25).align_to(track, RIGHT)
        self.play(FadeIn(low), FadeIn(high), run_time=0.5)

        thesis = fit(Text(
            "Scrutiny should scale with those answers.",
            color=PALETTE["ink"], font_size=24
        ), 10.0)
        thesis.move_to(DOWN * 3.1)
        self.play(Write(thesis), run_time=0.8)
        self.wait(6.0)


class B02_PipelineMechanism(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "What it actually does", color=PALETTE["ink"], font_size=28
        ), 10.5)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.6)

        tag = Text("Q3: how confident?", color=PALETTE["slate"], font_size=16, font=MONO)
        tag.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(tag), run_time=0.3)
        self.wait(0.2)

        face = Circle(radius=0.55, color=PALETTE["slate"], stroke_width=2.5,
                      fill_color=PALETTE["slate"], fill_opacity=0.08)
        eye_l = Dot(face.get_center() + LEFT * 0.2 + UP * 0.12, radius=0.05, color=PALETTE["ink"])
        eye_r = Dot(face.get_center() + RIGHT * 0.2 + UP * 0.12, radius=0.05, color=PALETTE["ink"])
        smile = Arc(radius=0.22, start_angle=-2.6, angle=1.2, color=PALETTE["ink"], stroke_width=2.5)
        smile.move_to(face.get_center() + DOWN * 0.12)
        face_icon = VGroup(face, eye_l, eye_r, smile).move_to(LEFT * 5.6 + DOWN * 0.5)
        self.play(Create(face), FadeIn(eye_l), FadeIn(eye_r), Create(smile), run_time=0.8)

        stages = ["Detect", "Embedding", "Compare\nto DB", "Score"]
        boxes = VGroup(*[
            RoundedRectangle(width=2.15, height=1.15, corner_radius=0.1,
                              fill_color=PALETTE["teal"], fill_opacity=0.15,
                              stroke_color=PALETTE["teal"], stroke_width=2)
            for _ in stages
        ]).arrange(RIGHT, buff=0.5).move_to(RIGHT * 0.4 + DOWN * 0.5)
        labels = VGroup(*[
            Text(s, color=PALETTE["ink"], font_size=19, line_spacing=0.9).move_to(b)
            for s, b in zip(stages, boxes)
        ])

        entry_arrow = Arrow(face_icon.get_right(), boxes[0].get_left(), buff=0.15,
                             color=PALETTE["ink"], stroke_width=2, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(entry_arrow), run_time=0.4)

        arrows = VGroup()
        for i in range(len(boxes) - 1):
            arrows.add(Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.1,
                              color=PALETTE["ink"], stroke_width=2, max_tip_length_to_length_ratio=0.18))

        for i, (box, label) in enumerate(zip(boxes, labels)):
            self.play(Create(box), Write(label), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)
        self.wait(0.4)

        gauge_bg = RoundedRectangle(width=4.6, height=0.55, corner_radius=0.25,
                                     fill_color=PALETTE["ink"], fill_opacity=0.08,
                                     stroke_color=PALETTE["slate"], stroke_width=1.5)
        gauge_bg.move_to(DOWN * 2.3)
        self.play(FadeIn(gauge_bg), run_time=0.4)

        gauge_tracker = ValueTracker(0.01)
        gauge_fill = always_redraw(lambda: Rectangle(
            width=max(0.02, 4.6 * 0.98 * gauge_tracker.get_value()), height=0.55,
            fill_color=PALETTE["crimson"], fill_opacity=0.9, stroke_width=0
        ).move_to(gauge_bg.get_left() + RIGHT * (4.6 * 0.98 * gauge_tracker.get_value()) / 2))
        self.add(gauge_fill)
        self.play(gauge_tracker.animate.set_value(1.0), run_time=1.0)

        pct = Text("98%", color=PALETTE["bg"], font_size=22).move_to(gauge_bg.get_left() + RIGHT * 0.7)
        self.play(FadeIn(pct), run_time=0.4)

        caption = fit(Text(
            "A 98% match is a probability, not a certainty.",
            color=PALETTE["crimson"], font_size=22
        ), 9.5)
        caption.next_to(gauge_bg, DOWN, buff=0.35)
        self.play(Write(caption), run_time=0.8)
        self.wait(7.0)


class B03_LegitimateUses(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The low-stakes side", color=PALETTE["ink"], font_size=27
        ), 10.5)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.6)

        badge_bg = RoundedRectangle(width=2.6, height=0.55, corner_radius=0.15,
                                     fill_color=PALETTE["sage"], fill_opacity=0.25,
                                     stroke_color=PALETTE["sage"], stroke_width=2)
        badge_bg.next_to(title, DOWN, buff=0.3)
        badge_txt = Text("LOW-STAKES", color=PALETTE["ink"], font_size=17).move_to(badge_bg)
        self.play(FadeIn(badge_bg), Write(badge_txt), run_time=0.5)
        self.wait(0.2)

        items = [
            "Assistive tools for visually impaired users",
            "Unlocking your own phone",
            "Reuniting missing people with family",
            "Supporting medical diagnosis",
        ]
        y = 0.95
        for it in items:
            dot = Dot(radius=0.12, color=PALETTE["sage"])
            check = Text("✓", color=PALETTE["bg"], font_size=16).move_to(dot)
            label = fit(Text(it, color=PALETTE["ink"], font_size=24), 8.8)
            dot.move_to(LEFT * 4.5 + UP * y)
            check.move_to(dot)
            label.next_to(dot, RIGHT, buff=0.35)
            self.play(FadeIn(dot, scale=1.3), FadeIn(check), Write(label), run_time=0.7)
            y -= 0.85

        self.wait(4.5)


class B04_HarmfulUses(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The high-stakes side", color=PALETTE["ink"], font_size=28
        ), 10.5)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.6)

        badge_bg = RoundedRectangle(width=2.9, height=0.55, corner_radius=0.15,
                                     fill_color=PALETTE["crimson"], fill_opacity=0.2,
                                     stroke_color=PALETTE["crimson"], stroke_width=2)
        badge_bg.next_to(title, DOWN, buff=0.3)
        badge_txt = Text("HIGH-STAKES", color=PALETTE["ink"], font_size=17).move_to(badge_bg)
        self.play(FadeIn(badge_bg), Write(badge_txt), run_time=0.5)
        self.wait(0.2)

        items = [
            "Mass surveillance without consent",
            "Tracking shoppers who never agreed to it",
            "Biometric data can't be reset like a password",
        ]
        y = 0.7
        for it in items:
            dot = Dot(radius=0.12, color=PALETTE["crimson"])
            cross = Text("✗", color=PALETTE["bg"], font_size=16).move_to(dot)
            label = fit(Text(it, color=PALETTE["ink"], font_size=24), 8.8)
            dot.move_to(LEFT * 4.5 + UP * y)
            cross.move_to(dot)
            label.next_to(dot, RIGHT, buff=0.35)
            self.play(FadeIn(dot, scale=1.3), FadeIn(cross), Write(label), run_time=0.7)
            y -= 0.95

        self.wait(5.0)


class B05_NistEvidence(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "NIST FRVT — Demographic Effects (2019)", color=PALETTE["ink"], font_size=25
        ), 11.0)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.6)

        cite = fit(Text(
            "189 algorithms - 18.27 million images", color=PALETTE["ink"], font_size=17, font=MONO
        ), 9.0)
        cite.next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(0.3)

        floor = Line(LEFT * 5.0, RIGHT * 5.0, color=PALETTE["ink"], stroke_width=1.5)
        floor.move_to([0, -1.4, 0])
        self.play(Create(floor), run_time=0.4)

        max_h = 2.6
        bar1_bg = Rectangle(width=2.0, height=max_h, stroke_color=PALETTE["ink"], stroke_width=1.2,
                             fill_opacity=0.0).move_to(LEFT * 2.3 + UP * (max_h / 2 - 1.4))
        bar2_bg = Rectangle(width=2.0, height=max_h, stroke_color=PALETTE["ink"], stroke_width=1.2,
                             fill_opacity=0.0).move_to(RIGHT * 2.3 + UP * (max_h / 2 - 1.4))

        lbl1 = fit(Text("Most\nalgorithms", color=PALETTE["ink"], font_size=18, line_spacing=0.9), 2.4)
        lbl1.next_to(bar1_bg, DOWN, buff=0.3)
        lbl2 = fit(Text("Best-performing\nalgorithms", color=PALETTE["ink"], font_size=18, line_spacing=0.9), 2.4)
        lbl2.next_to(bar2_bg, DOWN, buff=0.3)

        self.play(FadeIn(bar1_bg), FadeIn(bar2_bg), Write(lbl1), Write(lbl2), run_time=0.6)

        bar1_tracker = ValueTracker(0.01)
        bar1 = always_redraw(lambda: Rectangle(
            width=2.0, height=max(0.02, max_h * 0.88 * bar1_tracker.get_value()),
            fill_color=PALETTE["crimson"], fill_opacity=0.85, stroke_width=0
        ).move_to(bar1_bg.get_bottom(), aligned_edge=DOWN))
        self.add(bar1)
        self.play(bar1_tracker.animate.set_value(1.0), run_time=1.1)
        gap1 = fit(Text("real gap", color=PALETTE["crimson"], font_size=17), 1.8)
        gap1.next_to(bar1_bg, UP, buff=0.2)
        self.play(FadeIn(gap1), run_time=0.4)

        bar2_tracker = ValueTracker(0.01)
        bar2 = always_redraw(lambda: Rectangle(
            width=2.0, height=max(0.02, max_h * 0.08 * bar2_tracker.get_value()),
            fill_color=PALETTE["sage"], fill_opacity=0.85, stroke_width=0
        ).move_to(bar2_bg.get_bottom(), aligned_edge=DOWN))
        self.add(bar2)
        self.play(bar2_tracker.animate.set_value(1.0), run_time=1.1)
        gap2 = fit(Text("~near zero", color=PALETTE["sage"], font_size=17), 1.8)
        gap2.next_to(bar2_bg, UP, buff=0.2)
        self.play(FadeIn(gap2), run_time=0.4)
        self.wait(0.5)

        dissent = fit(Text(
            "Security Industry Association: this is overstated.",
            color=PALETTE["gold"], font_size=19
        ), 9.5)
        dissent.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(dissent), run_time=0.6)
        self.wait(9.0)


class B06_FluencyTrap(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The same trap as a fluent AI paragraph", color=PALETTE["ink"], font_size=27
        ), 10.8)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.6)
        self.wait(0.3)

        left_box = RoundedRectangle(width=4.4, height=2.6, corner_radius=0.15,
                                     fill_color=PALETTE["slate"], fill_opacity=0.08,
                                     stroke_color=PALETTE["slate"], stroke_width=2)
        left_box.move_to(LEFT * 3.0 + DOWN * 0.2)
        lines = VGroup(*[
            Line(LEFT * (1.7 - 0.15 * i), RIGHT * 1.7, color=PALETTE["ink"], stroke_width=3)
            for i in range(5)
        ]).arrange(DOWN, buff=0.28).move_to(left_box)
        left_label = Text("A fluent paragraph", color=PALETTE["ink"], font_size=18).next_to(left_box, DOWN, buff=0.25)

        right_box = RoundedRectangle(width=4.4, height=2.6, corner_radius=0.15,
                                      fill_color=PALETTE["teal"], fill_opacity=0.08,
                                      stroke_color=PALETTE["teal"], stroke_width=2)
        right_box.move_to(RIGHT * 3.0 + DOWN * 0.2)
        score = Text("98%\nmatch", color=PALETTE["teal"], font_size=46, line_spacing=0.9).move_to(right_box)
        right_label = Text("A match score", color=PALETTE["ink"], font_size=18).next_to(right_box, DOWN, buff=0.25)

        self.play(FadeIn(left_box), Create(lines), Write(left_label), run_time=0.8)
        self.play(FadeIn(right_box), Write(score), Write(right_label), run_time=0.8)
        self.wait(0.3)

        tag1 = Text("looks certain", color=PALETTE["crimson"], font_size=17).next_to(left_box, UP, buff=0.2)
        tag2 = Text("looks certain", color=PALETTE["crimson"], font_size=17).next_to(right_box, UP, buff=0.2)
        self.play(FadeIn(tag1), FadeIn(tag2), run_time=0.5)
        self.wait(0.5)

        banner = RoundedRectangle(width=10.8, height=0.85, corner_radius=0.12,
                                   fill_color=PALETTE["crimson"], fill_opacity=0.92, stroke_width=0)
        banner.move_to(DOWN * 3.0)
        banner_txt = Text("Both are a probability — not a fact.", color=PALETTE["bg"], font_size=24)
        banner_txt.move_to(banner)
        self.play(FadeIn(banner), Write(banner_txt), run_time=0.9)
        self.wait(6.0)


class B07_WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "One real case: retail loss prevention", color=PALETTE["ink"], font_size=26
        ), 11.0)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.6)
        self.wait(0.2)

        rows = [
            ("Used for?", "Catching theft - scanning every shopper, no consent"),
            ("If wrong?", "Innocent shopper flagged, maybe banned, never told why"),
            ("How confident?", "Vendor claims '99% accurate' - the same fluency trap"),
        ]
        y = 1.7
        q_col_right = -3.2   # question column is right-aligned to this x
        a_col_left = -2.85   # answer column is left-aligned to this x — keeps
                              # every row's answer starting in the same place
                              # regardless of how long its question label is
        tags = VGroup()
        for q, a in rows:
            q_txt = fit(Text(q, color=PALETTE["slate"], font_size=19, font=MONO), 2.6)
            a_txt = fit(Text(a, color=PALETTE["ink"], font_size=19), 7.4)
            q_txt.move_to([q_col_right - q_txt.width / 2, y, 0])
            a_txt.move_to([a_col_left + a_txt.width / 2, y, 0])
            tag_bg = RoundedRectangle(width=1.7, height=0.4, corner_radius=0.1,
                                       fill_color=PALETTE["crimson"], fill_opacity=0.2,
                                       stroke_color=PALETTE["crimson"], stroke_width=1.5)
            tag_bg.next_to(a_txt, DOWN, buff=0.14).align_to(a_txt, LEFT)
            tag_txt = Text("high-stakes", color=PALETTE["crimson"], font_size=14).move_to(tag_bg)
            self.play(Write(q_txt), Write(a_txt), run_time=0.7)
            self.play(FadeIn(tag_bg), FadeIn(tag_txt), run_time=0.3)
            self.wait(0.3)
            tags.add(tag_bg)
            y -= 1.35

        verdict = RoundedRectangle(width=7.4, height=0.75, corner_radius=0.12,
                                    fill_color=PALETTE["crimson"], fill_opacity=0.92, stroke_width=0)
        verdict.move_to(DOWN * 2.85)
        verdict_txt = fit(Text(
            "Three high-stakes answers - needs real scrutiny.",
            color=PALETTE["bg"], font_size=19
        ), 7.0)
        verdict_txt.move_to(verdict)
        self.play(FadeIn(verdict), Write(verdict_txt), run_time=0.8)
        self.wait(9.0)


class B08_YourTurn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("YOUR TURN", color=PALETTE["slate"], font_size=34), 10.0)
        title.move_to(UP * 2.9)
        self.play(Write(title), run_time=0.6)

        sub = fit(Text("Pick one AI system you used this week.", color=PALETTE["ink"], font_size=22), 10.0)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(0.3)

        questions = [
            "What's it used for?",
            "What happens if it's wrong?",
            "How confident is the claim, really?",
        ]
        y = 1.0
        for q in questions:
            box = Square(side_length=0.35, color=PALETTE["slate"], stroke_width=2.2,
                         fill_color=PALETTE["bg"], fill_opacity=1.0)
            label = fit(Text(q, color=PALETTE["ink"], font_size=23), 8.6)
            box.move_to(LEFT * 4.6 + UP * y)
            label.next_to(box, RIGHT, buff=0.35)
            self.play(Create(box), Write(label), run_time=0.6)
            self.wait(0.2)
            y -= 0.85

        self.wait(0.3)
        verdict = fit(Text(
            "Low-stakes on all three? Let it go. High-stakes on any? Scrutinize it.",
            color=PALETTE["crimson"], font_size=21
        ), 10.5)
        verdict.move_to(DOWN * 2.7)
        self.play(Write(verdict), run_time=0.9)
        self.wait(7.0)


class B09_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=36)
        accent = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        tagline = Text("In for Sai Pranavi Jeedigunta", color=PALETTE["ink"], font_size=22)
        VGroup(handle, accent, tagline).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        self.wait(2.7)
