"""scenes.py — Manim scenes for banking-domain-star-method-behavioral (deep-explainer).
11 Manim scenes: 4 act cards (B01, B04, B09, B13) + 7 content beats (B02, B05,
B08, B12, B14, B17, B18). The other 11 beats (B00, B03, B06, B07, B10, B11,
B15, B16, B_VERDICT, B_YOURTURN, B_OUTRO) render via Remotion.

Palette: bookends (ClaudeComposerAsk/ClaudeVerdictArtifact/ClaudeTitleOutro) render
in the claude fidelity skin with no override lever. Body Remotion cards
(QuoteCard/StateCardPair/LabelChip) hardcode the humanitarians accent set with no
override lever either. These Manim scenes match that same humanitarians set for
internal body consistency — this is not persona branding, it is the only color
wiring the shared components have (see beat_sheet.json's `component_note`).

Class names are `B0X_Name(Scene)` for run.sh's scene-detection regex. No LaTeX
(Text/Pango only). weight/slant passed as STRING literals ("BOLD"/"ITALIC"), not
the bare manim constants, since Gate A's static-check stub doesn't define them.
"""
from manim import *
import numpy as np

CREAM = "#F3EBDD"; INK = "#2F2A26"; TEAL = "#1F4E5F"
CRIMSON = "#E4572E"; SLATE = "#29335C"; GOLD = "#F3A712"

def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return "\n".join(lines)

def pad(scene, elapsed, target):
    scene.wait(max(0.4, target - elapsed - 0.2))

def checkmark(color=TEAL, size=0.32):
    """A real vector checkmark (native shape), not a Unicode glyph in Text —
    Gate A's distinctness stub excludes Text from its shape signature."""
    mark = VMobject(color=color, stroke_width=7)
    mark.set_points_as_corners([
        np.array([-0.5, 0.05, 0]) * size,
        np.array([-0.1, -0.45, 0]) * size,
        np.array([0.55, 0.5, 0]) * size,
    ])
    return mark

def act_card(scene, act_label, numeral, numeral_x, headline, mark_color, dur):
    """FILL-THE-CANVAS LAW: a large low-opacity background numeral gives the
    card real visual mass on a 4K canvas instead of a small left-clustered
    strip of text."""
    elapsed = 0.0
    big = Text(numeral, color=mark_color, weight="BOLD", font_size=280,
               fill_opacity=0.28, stroke_width=0).move_to([numeral_x, -0.3, 0])
    scene.play(FadeIn(big), run_time=0.6); elapsed += 0.6
    mark = Rectangle(width=1.2, height=0.16, color=mark_color, fill_color=mark_color,
                      fill_opacity=1, stroke_width=0).move_to([-5.4, 1.3, 0])
    eyebrow = Text(act_label, color=SLATE, weight="BOLD", font_size=32).next_to(mark, RIGHT, buff=0.35)
    scene.play(GrowFromEdge(mark, LEFT), FadeIn(eyebrow), run_time=0.6); elapsed += 0.6
    head = Text(wrap(headline, 18), color=INK, weight="BOLD", font_size=54,
                line_spacing=1.05).next_to(mark, DOWN, buff=0.6, aligned_edge=LEFT)
    scene.play(Write(head), run_time=1.3); elapsed += 1.3
    rule = Rectangle(width=2.6, height=0.07, color=mark_color, fill_color=mark_color,
                      fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.45, aligned_edge=LEFT)
    scene.play(GrowFromEdge(rule, LEFT), run_time=0.5); elapsed += 0.5
    pad(scene, elapsed, dur)


class B01_ActICard(Scene):
    DUR = 3.78
    def construct(self):
        self.camera.background_color = CREAM
        act_card(self, "ACT I", "I", 3.9, "The STAR Framework", TEAL, self.DUR)


class B04_ActIICard(Scene):
    DUR = 3.95
    def construct(self):
        self.camera.background_color = CREAM
        act_card(self, "ACT II", "II", 3.4, "What a Banking Panel Listens For", CRIMSON, self.DUR)


class B09_ActIIICard(Scene):
    DUR = 3.05
    def construct(self):
        self.camera.background_color = CREAM
        act_card(self, "ACT III", "III", 3.2, "Weak Answer, STAR Rewrite", SLATE, self.DUR)


class B13_ActIVCard(Scene):
    DUR = 3.05
    def construct(self):
        self.camera.background_color = CREAM
        act_card(self, "ACT IV", "IV", 3.5, "Daniel's Full-Loop Mock", GOLD, self.DUR)


class B02_StarFourParts(Scene):
    """The universal STAR definition — four rows, badge + label + one-line detail."""
    DUR = 13.23

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("The four parts", color=INK, weight="BOLD", font_size=40).to_edge(UP + LEFT, buff=0.85)
        self.play(Write(head), run_time=0.9); elapsed += 0.9

        parts = [
            ("S", "Situation", "the scenario, briefly"),
            ("T", "Task", "your responsibility or goal"),
            ("A", "Action", "what you specifically did"),
            ("R", "Result", "the outcome, and what changed because of it"),
        ]
        rows = VGroup()
        for letter, label, detail in parts:
            badge = RoundedRectangle(corner_radius=0.14, width=0.95, height=0.95, color=TEAL,
                                      fill_color=TEAL, fill_opacity=1, stroke_width=0)
            letter_txt = Text(letter, color=CREAM, weight="BOLD", font_size=40).move_to(badge)
            label_txt = Text(label, color=INK, weight="BOLD", font_size=36)
            detail_txt = Text(wrap(detail, 34), color=SLATE, font_size=26, line_spacing=1.05)
            text_col = VGroup(label_txt, detail_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            row = VGroup(VGroup(badge, letter_txt), text_col).arrange(RIGHT, buff=0.5, aligned_edge=UP)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows.next_to(head, DOWN, buff=0.55, aligned_edge=LEFT)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rows],
                              lag_ratio=0.7, run_time=4.2)); elapsed += 4.2
        pad(self, elapsed, self.DUR)


class B05_ThreeCompetencies(Scene):
    """The three banking-specific competencies — three panels, side by side."""
    DUR = 22.14

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("What a banking panel listens for", color=INK, weight="BOLD",
                     font_size=34).to_edge(UP + LEFT, buff=0.9)
        self.play(Write(head), run_time=1.2); elapsed += 1.2

        items = [
            ("Risk awareness", "Noticed before being told."),
            ("Control judgment", "Understood why the rule existed."),
            ("Examiner comfort", "Can defend the work without sounding defensive."),
        ]
        cols = VGroup()
        xs = [-4.2, 0, 4.2]
        for (label, detail), x in zip(items, xs):
            box = Rectangle(width=3.6, height=2.6, color=SLATE, stroke_width=3,
                             fill_color=CREAM, fill_opacity=1).move_to([x, -0.5, 0])
            lbl = Text(label, color=TEAL, weight="BOLD", font_size=22).next_to(
                box.get_top(), DOWN, buff=0.4)
            det = Text(wrap(detail, 18), color=INK, font_size=19,
                       line_spacing=1.1).next_to(lbl, DOWN, buff=0.35)
            cols.add(VGroup(box, lbl, det))
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cols],
                              lag_ratio=0.8, run_time=6.5)); elapsed += 6.5
        pad(self, elapsed, self.DUR)


class B08_DeliveryRule(Scene):
    """'We fixed it' (weak) struck through, replaced by the named-control version."""
    DUR = 15.77

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("Be specific about what changed.", color=INK, weight="BOLD",
                     font_size=40).to_edge(UP + LEFT, buff=0.85)
        self.play(Write(head), run_time=1.1); elapsed += 1.1

        weak = Text('"We fixed it."', color=INK, font_size=40).next_to(
            head, DOWN, buff=0.7, aligned_edge=LEFT)
        self.play(FadeIn(weak), run_time=0.7); elapsed += 0.7
        strike = Line(weak.get_left() + LEFT * 0.1, weak.get_right() + RIGHT * 0.1,
                       color=CRIMSON, stroke_width=4)
        strike._qc_intentional = True
        self.play(Create(strike), run_time=0.5); elapsed += 0.5
        self.play(FadeOut(weak), FadeOut(strike), run_time=0.5); elapsed += 0.5

        strong = Text(wrap('"We added a validation check that catches that specific '
                            'error before it reaches the report."', 30),
                       color=TEAL, weight="BOLD", font_size=36,
                       line_spacing=1.15).next_to(head, DOWN, buff=0.7, aligned_edge=LEFT)
        self.play(FadeIn(strong, shift=UP * 0.15), run_time=1.0); elapsed += 1.0

        note = Text("Proves you understood why it mattered.", color=SLATE, font_size=28,
                     slant="ITALIC").next_to(strong, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(FadeIn(note), run_time=0.8); elapsed += 0.8

        pad(self, elapsed, self.DUR)


class B12_ScoredChecklist(Scene):
    """What's scored in the STAR rewrite — animated checklist."""
    DUR = 14.66

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("What's scored", color=INK, weight="BOLD", font_size=46).to_edge(UP + LEFT, buff=0.85)
        rule = Rectangle(width=2.0, height=0.07, color=TEAL, fill_color=TEAL,
                          fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.38, aligned_edge=LEFT)
        self.play(Write(head), run_time=0.9); elapsed += 0.9
        self.play(GrowFromEdge(rule, LEFT), run_time=0.4); elapsed += 0.4

        items = [
            "Risk awareness — is this plausible, checked as a habit",
            "Escalation — raised immediately, to the right people",
            "Outcome — the specific control now named",
        ]
        rows = VGroup()
        for it in items:
            check = checkmark(color=TEAL, size=0.44)
            txt = Text(wrap(it, 32), color=INK, font_size=30, line_spacing=1.05)
            row = VGroup(check, txt).arrange(RIGHT, buff=0.4, aligned_edge=UP)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(rule, DOWN, buff=0.55, aligned_edge=LEFT)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.25) for r in rows],
                              lag_ratio=0.6, run_time=2.6)); elapsed += 2.6

        pad(self, elapsed, self.DUR)


class B14_FiveStageLoop(Scene):
    """The five-stage banking loop, Stage 4 (Behavioral) highlighted."""
    DUR = 18.09

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("A realistic banking loop", color=INK, weight="BOLD",
                     font_size=32).to_edge(UP + LEFT, buff=0.9)
        self.play(Write(head), run_time=1.0); elapsed += 1.0

        stages = ["Domain\nVocabulary", "SQL", "Case", "Behavioral", "Systems\nDesign"]
        xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
        boxes = VGroup()
        for i, (label, x) in enumerate(zip(stages, xs)):
            color = CRIMSON if i == 3 else SLATE
            box = Rectangle(width=2.3, height=1.5, color=color, stroke_width=3,
                             fill_color=CREAM, fill_opacity=1).move_to([x, -0.2, 0])
            txt = Text(label, color=INK, font_size=22, weight="BOLD" if i == 3 else "NORMAL",
                       line_spacing=1.0).move_to(box.get_center())
            boxes.add(VGroup(box, txt))
        for b in boxes:
            self.play(FadeIn(b, shift=DOWN * 0.2), run_time=0.4); elapsed += 0.4
        self.play(Indicate(boxes[3], color=CRIMSON, scale_factor=1.08), run_time=0.8); elapsed += 0.8

        tag = Text("stage four", color=INK, weight="BOLD", font_size=24,
                    slant="ITALIC").next_to(boxes[3], DOWN, buff=0.4)
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.6); elapsed += 0.6

        pad(self, elapsed, self.DUR)


class B17_ScoreAndChart(Scene):
    """Daniel's score on Behavioral (1/3) plus the pattern across the other four stages."""
    DUR = 14.81

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("Daniel's self-scoring sheet", color=INK, weight="BOLD",
                     font_size=32).to_edge(UP + LEFT, buff=0.9)
        self.play(Write(head), run_time=1.0); elapsed += 1.0

        stages = [("Domain vocabulary", 2), ("SQL", 2), ("Case", 2),
                  ("Behavioral", 1), ("Systems design", 2)]
        ys = [1.6, 0.8, 0.0, -0.8, -1.6]
        max_w = 5.0
        rows = VGroup()
        for (label, score), y in zip(stages, ys):
            lbl = Text(label, color=INK, font_size=20).move_to([-4.0, y, 0], aligned_edge=RIGHT)
            bar_color = CRIMSON if score == 1 else SLATE
            bar = Rectangle(height=0.45, width=max_w * (score / 3), color=bar_color,
                             fill_color=bar_color, fill_opacity=1, stroke_width=0)
            bar.move_to([-3.2 + bar.width / 2, y, 0], aligned_edge=LEFT)
            score_txt = Text(f"{score}/3", color=bar_color, weight="BOLD",
                              font_size=20).next_to(bar, RIGHT, buff=0.25)
            rows.add(VGroup(lbl, bar, score_txt))
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6); elapsed += 0.6
        self.play(Indicate(rows[3], color=CRIMSON, scale_factor=1.05), run_time=0.7); elapsed += 0.7

        note = Text("Four correct answers, one repeating gap.", color=SLATE, font_size=22,
                     slant="ITALIC").to_edge(DOWN + LEFT, buff=0.9)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.8); elapsed += 0.8

        pad(self, elapsed, self.DUR)


class B18_TheLesson(Scene):
    """The final-week allocation — most hours on Behavioral, one light rep elsewhere."""
    DUR = 13.97

    def construct(self):
        self.camera.background_color = CREAM
        elapsed = 0.0
        head = Text("The final-week plan", color=INK, weight="BOLD",
                     font_size=34).to_edge(UP + LEFT, buff=0.85)
        rule = Rectangle(width=1.8, height=0.06, color=GOLD, fill_color=GOLD,
                          fill_opacity=1, stroke_width=0).next_to(head, DOWN, buff=0.32, aligned_edge=LEFT)
        self.play(Write(head), run_time=0.9); elapsed += 0.9
        self.play(GrowFromEdge(rule, LEFT), run_time=0.4); elapsed += 0.4

        stages = [("Behavioral", 5.2, CRIMSON), ("Domain vocabulary", 1.2, SLATE),
                  ("SQL", 1.2, SLATE), ("Case", 1.2, SLATE), ("Systems design", 1.2, SLATE)]
        ys = [1.1, 0.35, -0.4, -1.15, -1.9]
        rows = VGroup()
        for (label, width, color), y in zip(stages, ys):
            lbl = Text(label, color=INK, font_size=20).move_to([-4.0, y, 0], aligned_edge=RIGHT)
            bar = Rectangle(height=0.4, width=width, color=color, fill_color=color,
                             fill_opacity=1, stroke_width=0)
            bar.move_to([-3.2 + bar.width / 2, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(lbl, bar))
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rows],
                              lag_ratio=0.5, run_time=2.6)); elapsed += 2.6

        closer = Text("Finish the thought out loud.", color=INK, weight="BOLD",
                       font_size=30).to_edge(DOWN + LEFT, buff=0.9)
        self.play(Write(closer), run_time=1.1); elapsed += 1.1

        pad(self, elapsed, self.DUR)
