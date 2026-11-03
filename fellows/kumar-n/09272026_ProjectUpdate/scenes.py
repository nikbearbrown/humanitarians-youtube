"""
scenes.py: sers-ml-4-4-update (landscape 16:9)

Body beats for the Section 4.4 revision update.
  B02_BeforeAfter       draft (2 paragraphs) -> revision (4 paragraphs)
  B03_Correction        uncited claim boxed; identical-backbone comparison
  B04_ProtocolDefault   naive vs leakage-audited split; two-model default
  B05_PhysicsConstraint negative concentrations -> non-negative (illustrative)

Safe area enforced by GATE B (landscape): x +/-6.3, y +/-3.4.
Every coordinate below was checked against that box, see the per-scene notes.
Title: .to_edge(UP, buff=0.75). Kicker: .to_edge(DOWN, buff=0.65).

GATE A: every visual element enters through a real shape Transform
(grows from a sliver or a dot) spread across the timeline, never one
Create() followed by text-only fades.
GATE B: no text sits on a Line/Arrow; call-outs use SurroundingRectangle.

Palette: approximations of the Claude tokens. Swap them for the exact
values in runtime/remotion/src/tokens/claude.ts if your other reels use them.
"""

from manim import *

PAGE = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A766A"
SPARK = "#D97757"
CARD = "#FFFFFF"
FOOTER = "Paper 2 · §4.4 Hybrid and Multi-Task Architectures"

config.background_color = PAGE


# Helpers

def fit(m, maxw):
    """Shrink a mobject to maxw if it is wider; never enlarge."""
    if m.width > maxw:
        m.scale_to_fit_width(maxw)
    return m


def make_title(s):
    t = Text(s, font_size=40, color=INK, weight="BOLD")
    fit(t, 11.5)
    return t.to_edge(UP, buff=0.75)


def make_kicker(s):
    k = Text(s, font_size=28, color=INK)
    fit(k, 11.5)
    return k.to_edge(DOWN, buff=0.65)


def make_card(w, h, center, stroke=INK):
    r = RoundedRectangle(
        corner_radius=0.12, width=w, height=h,
        stroke_color=stroke, stroke_width=2.5,
        fill_color=CARD, fill_opacity=1,
    )
    return r.move_to(center)


def label_in(card, s, size=24, color=INK):
    t = Text(s, font_size=size, color=color, line_spacing=0.8)
    fit(t, card.width - 0.4)
    return t.move_to(card.get_center())


def grow_from_left(scene, m, run_time=0.8):
    """Grow m from a thin sliver at its left edge (real shape Transform)."""
    s = m.copy()
    s.stretch_to_fit_width(0.04)
    s.move_to(m.get_left() + RIGHT * 0.02)
    scene.add(s)
    scene.play(ReplacementTransform(s, m), run_time=run_time)


def grow_from_point(scene, m, run_time=0.5):
    """Grow m from a near-zero copy of itself at its own centre."""
    s = m.copy().scale(0.04)
    scene.add(s)
    scene.play(ReplacementTransform(s, m), run_time=run_time)


# B02: Before -> After
# Coordinates: title bottom ~2.7 | column heads y=2.05 | right cards
# y 1.575 .. -1.875, x 0.3 .. 4.9 | left cards x -5.5 .. -2.1 |
# "4 paragraphs" y ~-2.3 | kicker top ~-2.95. All inside +/-6.3 / +/-3.4.
# Run time ~22.5 s vs ~25 s narration (58 words).

class B02_BeforeAfter(Scene):
    def construct(self):
        title = make_title("Section 4.4: Before → After")
        footer = make_kicker(FOOTER)
        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(footer), run_time=0.8)
        self.wait(0.3)

        lhead = Text("Draft", font_size=30, color=SOFT).move_to([-3.8, 2.05, 0])
        rhead = Text("Revised", font_size=30, color=SPARK, weight="BOLD").move_to([2.6, 2.05, 0])

        left_specs = ["Describes the model", "Reports a finding"]
        right_specs = [
            "Why it was designed this way",
            "Evidence against the easy claim",
            "The mechanism behind a result",
            "A rule readers can use",
        ]
        rows_y = [1.2, 0.3, -0.6, -1.5]

        self.play(FadeIn(lhead), run_time=0.5)
        for s, y in zip(left_specs, rows_y):
            c = make_card(3.4, 0.75, [-3.8, y, 0], stroke=SOFT)
            grow_from_left(self, c)
            self.play(FadeIn(label_in(c, s, color=SOFT)), run_time=0.5)

        lcount = Text("2 paragraphs", font_size=24, color=SOFT).move_to([-3.8, -0.6, 0])
        self.play(FadeIn(lcount), run_time=0.5)
        self.wait(0.8)

        arrow = Arrow([-1.9, -0.15, 0], [0.1, -0.15, 0], buff=0, color=SPARK, stroke_width=5)
        self.play(GrowArrow(arrow), run_time=0.8)
        self.play(FadeIn(rhead), run_time=0.5)

        right_cards = VGroup()
        for s, y in zip(right_specs, rows_y):
            c = make_card(4.6, 0.75, [2.6, y, 0])
            grow_from_left(self, c)
            right_cards.add(c)
            self.play(FadeIn(label_in(c, s)), run_time=0.5)
            self.wait(0.2)

        rcount = Text("4 paragraphs", font_size=24, color=SPARK).move_to([2.6, -2.3, 0])
        self.play(FadeIn(rcount), run_time=0.5)
        self.wait(0.5)

        # Late shape change: call-out frame around the revised column.
        frame = SurroundingRectangle(right_cards, color=SPARK, buff=0.12, stroke_width=3)
        grow_from_left(self, frame, run_time=1.0)

        kicker = make_kicker("From describing models to saying when to use them")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(0.7)


# B03: The correction
# Coordinates: claim y 1.95 (box ~1.6 .. 2.3) | tag ~1.3 | backbone
# x -5.5 .. -2.9 | head cards x -0.8 .. 1.6, y 1.0 .. -1.8 | results
# x ~2.9 .. 4.5 | source note x <= -2.9, y ~-1.5 | kicker top ~-2.95.
# Run time ~27.5 s vs ~31 s narration (71 words).

class B03_Correction(Scene):
    def construct(self):
        title = make_title("The Correction")
        footer = make_kicker(FOOTER)
        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(footer), run_time=0.8)

        claim = Text("“…often improving performance on both tasks…”",
                     font_size=28, color=INK, slant="ITALIC")
        fit(claim, 10.0).move_to([0, 1.95, 0])
        self.play(FadeIn(claim), run_time=0.8)
        self.wait(0.6)

        box = SurroundingRectangle(claim, color=SPARK, buff=0.15, stroke_width=3)
        grow_from_left(self, box)
        tag = Text("original draft · no citation", font_size=22, color=SPARK)
        tag.next_to(box, DOWN, buff=0.1)
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(2.0)
        self.play(claim.animate.set_opacity(0.35), box.animate.set_stroke(opacity=0.5),
                  tag.animate.set_opacity(0.5), run_time=0.5)

        backbone = make_card(2.6, 1.3, [-4.2, -0.4, 0])
        grow_from_left(self, backbone)
        self.play(FadeIn(label_in(backbone, "Leakage-audited\nsplit · C-MAPSS", size=24)), run_time=0.5)
        src = Text("Shamim et al., 2026\npreprint · non-SERS", font_size=20,
                   color=SOFT, line_spacing=0.8)
        fit(src, 2.6).move_to([-4.2, -1.5, 0])
        self.play(FadeIn(src), run_time=0.5)
        self.wait(0.5)

        a_top = Arrow([-2.8, -0.1, 0], [-0.85, 0.55, 0], buff=0, color=SOFT, stroke_width=4)
        a_bot = Arrow([-2.8, -0.7, 0], [-0.85, -1.35, 0], buff=0, color=SOFT, stroke_width=4)
        self.play(GrowArrow(a_top), GrowArrow(a_bot), run_time=0.8)

        joint = make_card(2.4, 0.8, [0.4, 0.6, 0])
        grow_from_left(self, joint)
        self.play(FadeIn(label_in(joint, "Multi-task\n(AMTLNet)", size=22)), run_time=0.5)
        sep = make_card(2.4, 0.8, [0.4, -1.4, 0])
        grow_from_left(self, sep)
        self.play(FadeIn(label_in(sep, "Single-task\n(CNN-LSTM)", size=22)), run_time=0.5)
        self.wait(1.0)

        r_top = Arrow([1.7, 0.6, 0], [2.6, 0.6, 0], buff=0, color=SOFT, stroke_width=4)
        r_bot = Arrow([1.7, -1.4, 0], [2.6, -1.4, 0], buff=0, color=SOFT, stroke_width=4)
        self.play(GrowArrow(r_top), GrowArrow(r_bot), run_time=0.6)

        res_top = Text("84.12%", font_size=34, color=INK, weight="BOLD").move_to([3.7, 0.6, 0])
        res_bot = Text("≈ same", font_size=34, color=INK, weight="BOLD").move_to([3.7, -1.4, 0])
        self.play(FadeIn(res_top), run_time=0.6)
        self.wait(1.0)
        self.play(FadeIn(res_bot), run_time=0.6)
        self.wait(1.0)

        both = SurroundingRectangle(VGroup(res_top, res_bot), color=SPARK, buff=0.2, stroke_width=3)
        grow_from_left(self, both)
        kicker = make_kicker("Tukey p = 1.0: no significant advantage for joint training")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(3.1)


# B04: Protocol matters, then the new default
# Phase 1: sub y 2.1 | track 1 y 0.6, x -5 .. 5 (labels y 1.2, ticks y 0.1)
#          track 2 y -1.3 (labels y -0.7, ticks y -1.8) | kicker top ~-2.95
# Phase 2: question card y 0.85 .. 1.75 | answer cards y -0.45 .. -1.65,
#          x -5.8 .. -0.8 and 0.8 .. 5.8
# No text sits on either track line: labels are 0.5+ above, ticks 0.5 below.
# Run time ~29 s vs ~27 s narration (62 words).

class B04_ProtocolDefault(Scene):
    def construct(self):
        title = make_title("Protocol Matters")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        sub = Text("Same data · same model · different split", font_size=28, color=SOFT)
        fit(sub, 11).move_to([0, 2.1, 0])
        self.play(FadeIn(sub), run_time=0.6)

        def track(y, name):
            line = Line([-5, y, 0], [5, y, 0], color=SOFT, stroke_width=5)
            lab = Text(name, font_size=26, color=INK)
            lab.move_to([0, y + 0.6, 0]).align_to(line, LEFT)
            t0 = Text("0%", font_size=22, color=SOFT).move_to([-5, y - 0.5, 0])
            t1 = Text("100%", font_size=22, color=SOFT).move_to([5, y - 0.5, 0])
            return line, lab, VGroup(t0, t1)

        x_of = lambda pct: -5 + 10 * pct / 100.0

        line1, lab1, ticks1 = track(0.6, "Naive split")
        grow_from_left(self, line1)
        self.play(FadeIn(lab1), FadeIn(ticks1), run_time=0.5)
        dot1 = Dot([0, 0.6, 0], radius=0.14, color=SPARK)
        grow_from_point(self, dot1, run_time=0.4)
        for pct, rt in [(99.9, 0.6), (0, 0.6), (99.9, 0.5), (0, 0.5)]:
            self.play(dot1.animate.move_to([x_of(pct), 0.6, 0]), run_time=rt)
        read1 = Text("swings 0% ↔ 99.9%", font_size=24, color=SPARK)
        read1.move_to([0, 1.2, 0]).align_to(line1, RIGHT)
        self.play(FadeIn(read1), run_time=0.5)
        self.wait(0.5)

        line2, lab2, ticks2 = track(-1.3, "Leakage-audited split")
        grow_from_left(self, line2, run_time=0.6)
        self.play(FadeIn(lab2), FadeIn(ticks2), run_time=0.5)
        dot2 = Dot([x_of(50), -1.3, 0], radius=0.14, color=INK)
        grow_from_point(self, dot2, run_time=0.4)
        self.play(dot2.animate.move_to([x_of(30), -1.3, 0]), run_time=0.8)
        read2 = Text("≈30% (±15)", font_size=24, color=INK, weight="BOLD")
        read2.move_to([0, -0.7, 0]).align_to(line2, RIGHT)
        self.play(FadeIn(read2), run_time=0.5)
        self.wait(0.3)

        k1 = make_kicker("The protocol mattered as much as the architecture")
        self.play(FadeIn(k1, shift=UP * 0.15), run_time=0.6)
        self.wait(0.8)

        # Phase 2: the default
        phase1 = VGroup(sub, line1, lab1, ticks1, dot1, read1,
                        line2, lab2, ticks2, dot2, read2, k1)
        self.play(FadeOut(phase1), run_time=0.4)
        title2 = make_title("The New Default")
        self.play(Transform(title, title2), run_time=0.4)

        q = make_card(8.0, 0.9, [0, 1.3, 0])
        grow_from_left(self, q)
        self.play(FadeIn(label_in(q, "Are the two tasks naturally coupled?", size=28)), run_time=0.4)

        a_l = Arrow([-1.5, 0.8, 0], [-3.3, -0.4, 0], buff=0, color=SOFT, stroke_width=4)
        a_r = Arrow([1.5, 0.8, 0], [3.3, -0.4, 0], buff=0, color=SOFT, stroke_width=4)
        self.play(GrowArrow(a_l), GrowArrow(a_r), run_time=0.6)

        yes = make_card(5.0, 1.2, [-3.3, -1.05, 0])
        grow_from_left(self, yes)
        self.play(FadeIn(label_in(yes, "Yes\none joint model", size=26)), run_time=0.5)
        no = make_card(5.0, 1.2, [3.3, -1.05, 0])
        grow_from_left(self, no)
        self.play(FadeIn(label_in(no, "No\nclassifier + regressor", size=26)), run_time=0.5)
        self.play(no.animate.set_stroke(color=SPARK, width=4), run_time=0.6)

        k2 = make_kicker("Uncoupled tasks? Two models: easier to debug and interpret")
        self.play(FadeIn(k2, shift=UP * 0.15), run_time=0.6)
        self.wait(1.5)


# B05: The physics constraint (ILLUSTRATIVE values, not from the paper)
# Coordinates: sub y 2.2 | bars x -3.45 .. 3.45, top <= 1.66, bottom >= -1.14
# axis y -0.3, x -4.3 .. 4.3 | "0" at x -4.6 | component labels y -1.6 |
# callout x ~4.2 .. 5.8, y ~-0.7 | "illustrative" x ~4.3 .. 5.7, y -2.2 |
# kicker top ~-2.95.
# Run time ~23 s vs ~26 s narration (60 words).

AXIS_Y = -0.3
SCALE = 1.4
XS = [-3.0, -1.0, 1.0, 3.0]
UNCONSTRAINED = [0.9, -0.6, 1.4, -0.4]
CONSTRAINED = [0.7, 0.0, 1.1, 0.25]


def make_bar(x, v):
    h = max(abs(v) * SCALE, 0.03)
    color = SPARK if v < 0 else INK
    r = Rectangle(width=0.9, height=h, stroke_width=0, fill_color=color, fill_opacity=0.9)
    cy = AXIS_Y + h / 2 if v >= 0 else AXIS_Y - h / 2
    return r.move_to([x, cy, 0])


class B05_PhysicsConstraint(Scene):
    def construct(self):
        title = make_title("The Missing Why")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        sub = Text("Unconstrained autoencoder: good reconstruction", font_size=28, color=INK)
        fit(sub, 10.5).move_to([0, 2.2, 0])
        self.play(FadeIn(sub), run_time=0.6)

        axis = Line([-4.3, AXIS_Y, 0], [4.3, AXIS_Y, 0], color=SOFT, stroke_width=3)
        grow_from_left(self, axis)
        zero = Text("0", font_size=22, color=SOFT).move_to([-4.65, AXIS_Y, 0])
        self.play(FadeIn(zero), run_time=0.3)

        bars = []
        for x, v in zip(XS, UNCONSTRAINED):
            b = make_bar(x, v)
            seed = Rectangle(width=0.9, height=0.02, stroke_width=0,
                             fill_color=b.get_fill_color(), fill_opacity=0.9).move_to([x, AXIS_Y, 0])
            self.add(seed)
            self.play(ReplacementTransform(seed, b), run_time=0.6)
            bars.append(b)

        names = VGroup(*[Text(n, font_size=24, color=INK).move_to([x, -1.6, 0])
                         for n, x in zip(["A", "B", "C", "D"], XS)])
        self.play(FadeIn(names), run_time=0.5)
        self.wait(1.0)

        callout = Text("< 0:\nimpossible", font_size=22, color=SPARK, line_spacing=0.8)
        callout.move_to([5.0, -0.7, 0])
        illus = Text("illustrative", font_size=20, color=SOFT, slant="ITALIC").move_to([5.0, -2.2, 0])
        self.play(FadeIn(callout), FadeIn(illus), run_time=0.6)
        self.wait(2.5)

        sub2 = Text("Non-negativity built in: physically valid", font_size=28, color=INK)
        fit(sub2, 10.5).move_to(sub)
        self.play(Transform(sub, sub2), run_time=0.8)
        self.play(*[Transform(b, make_bar(x, v)) for b, x, v in zip(bars, XS, CONSTRAINED)],
                  FadeOut(callout), run_time=1.5)
        self.wait(1.5)

        kicker = make_kicker("Mixtures need physically valid answers")
        self.play(FadeIn(kicker, shift=UP * 0.15), run_time=0.6)
        self.wait(6.0)
