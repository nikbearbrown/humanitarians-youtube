"""scenes.py — Manim scenes for knowledge-cutoff (16:9).

Palette: cream #FAF9F5, ink #3D3929. INK ONLY — no terracotta text or fills
(GATE T §8.3; carried over from claude-liam-context-window/vertical).
Explicit font on every Text: EB Garamond. GHOST is for shapes only, never text.
B04 and B06 are ILLUSTRATIVE (labelled on screen) — no real dates or versions.
No slant=ITALIC on multi-word text (Pango collapses spaces).
Clip lengths are set to the measured audio (mp3/timings.json), within the
compiler's ±5% retime window so nothing is center-cut.
"""
from manim import *

BG    = ManimColor("#FAF9F5")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all text and fills
SOFT  = ManimColor("#6E6A57")   # secondary text (>= 4.5:1 on cream)
GHOST = ManimColor("#A8A491")   # shapes only — dimmed / out-of-range
CARD  = ManimColor("#FFFFFF")

SAFE_W = 12.4                   # usable width inside the 14.22-unit frame


def _label(text, size=32, color=None, weight=None, fit=True, max_w=SAFE_W):
    # Lay out at 4x then scale down: Pango kerning at small sizes collapses
    # word spaces; the big layout keeps them.
    # Long lines at 4x hit Pango's layout width and wrap, so drop to 2x there.
    m = 4 if len(text) * size < 1100 else 2
    kw = {"font_size": size * m, "color": color or INK, "font": "EB Garamond"}
    if weight:
        kw["weight"] = weight
    t = Text(text, **kw).scale(1 / m)
    if fit and t.width > max_w:
        t.scale_to_fit_width(max_w)
    return t


def _doc(color=INK):
    """A small document chip: page outline plus three text rules."""
    page = Rectangle(width=0.42, height=0.56, color=color, stroke_width=3,
                     fill_color=CARD, fill_opacity=1)
    rules = VGroup(*[Line(LEFT * 0.12, RIGHT * 0.12, color=color, stroke_width=2.5)
                     for _ in range(3)]).arrange(DOWN, buff=0.1).move_to(page)
    return VGroup(page, rules)


class B01_HesitantWriter(Scene):
    """Beat 2 BLUF, hesitant writer in Manim (BrutalistHesitantWriter is not
    on this reel's allowed list). 'Claude knows / everything up to today.'
    types in; the second line dims and backspaces out; 'what it learned
    before its cutoff.' types in its place. Ink only. ~4.6s (audio 4.56s)."""

    def construct(self):
        self.camera.background_color = BG

        line1 = _label("Claude knows", size=64, fit=False)
        wrong = _label("everything up to today.", size=64, fit=False)
        right = _label("what it learned before its cutoff.", size=64, fit=False)
        k = min(1.0, 11.6 / max(line1.width, wrong.width, right.width))
        for t in (line1, wrong, right):
            t.scale(k)
        VGroup(line1, wrong).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(UP * 0.2)
        right.move_to(wrong, aligned_edge=LEFT)
        # center the block on its widest (final) state, left-aligned like a page
        left_x = -max(line1.width, wrong.width, right.width) / 2
        for t in (line1, wrong, right):
            t.shift(RIGHT * (left_x - t.get_left()[0]))

        self.play(AddTextLetterByLetter(line1), run_time=0.5)
        self.play(AddTextLetterByLetter(wrong), run_time=0.6)
        self.wait(0.3)
        self.play(wrong.animate.set_color(SOFT), run_time=0.25)
        self.play(RemoveTextLetterByLetter(wrong), run_time=0.4)
        self.play(AddTextLetterByLetter(right), run_time=0.8)
        self.wait(1.75)


class B02_Snapshot(Scene):
    """Training is a snapshot: document chips before the dashed cutoff line
    flow up into the Training box; chips after it arrive, stop at the line,
    and stay out (dimmed). ~4.5s (audio 4.42s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Training Is a Snapshot", size=44, weight="BOLD").move_to(UP * 2.9)
        AX_Y, CUT_X = -1.6, 2.0
        axis = Arrow([-6.0, AX_Y, 0], [6.1, AX_Y, 0], color=INK, stroke_width=4,
                     buff=0, max_tip_length_to_length_ratio=0.03)
        time_lbl = _label("time", size=30, color=SOFT).next_to(axis.get_end(), DOWN, buff=0.25).shift(LEFT * 0.3)
        cut = DashedLine([CUT_X, AX_Y - 0.9, 0], [CUT_X, 1.9, 0], color=INK,
                         stroke_width=5, dash_length=0.16)
        cut_lbl = _label("cutoff", size=34, weight="BOLD").next_to(cut, DOWN, buff=0.15)
        box = RoundedRectangle(width=5.6, height=1.6, corner_radius=0.15, color=INK,
                               stroke_width=4).move_to([-2.4, 0.85, 0])
        box_lbl = _label("Training", size=40, weight="BOLD").next_to(box, LEFT, buff=0.3)
        if box_lbl.get_left()[0] < -6.6:
            box_lbl.next_to(box, UP, buff=0.2).align_to(box, LEFT)

        self.play(Write(title), run_time=0.5)
        self.play(Create(axis), Create(cut), FadeIn(cut_lbl), FadeIn(time_lbl),
                  Create(box), FadeIn(box_lbl), run_time=0.6)

        before_x = [-5.2, -4.2, -3.2, -2.2, -1.2, -0.2, 0.9]
        after_x = [3.1, 4.1, 5.1]
        before = VGroup(*[_doc().move_to([x, AX_Y + 0.55, 0]) for x in before_x])
        after = VGroup(*[_doc().move_to([x, AX_Y + 0.55, 0]) for x in after_x])
        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.2) for d in [*before, *after]],
                              lag_ratio=0.08), run_time=0.6)

        # before-cutoff chips go into the box, packed in one row
        slots = [box.get_left() + RIGHT * (0.5 + 0.75 * i) for i in range(len(before))]
        self.play(*[d.animate.move_to(s) for d, s in zip(before, slots)], run_time=1.0)

        # after-cutoff chips push at the line, bounce back, and dim
        push = after[0].get_center()[0] - CUT_X - 0.4      # same shift for all: no pile-up
        self.play(*[d.animate.shift(LEFT * push) for d in after],
                  run_time=0.35, rate_func=rush_into)
        self.play(*[d.animate.shift(RIGHT * 0.35).set_stroke(GHOST) for d in after],
                  run_time=0.35, rate_func=rush_from)
        self.wait(1.1)


class B04_EdgeThins(Scene):
    """ILLUSTRATIVE band along a timeline: solid ink up to the reliable
    knowledge cutoff ('Most reliable'), lighter between the two dates
    ('Thins'), empty past the training data cutoff ('Nothing seen').
    No real dates. ~5.1s (audio 5.04s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Between the Dates, Knowledge Thins", size=44, weight="BOLD").move_to(UP * 2.9)
        meta = _label("ILLUSTRATIVE — not a measured trace", size=30, color=SOFT).next_to(title, DOWN, buff=0.2)

        L, A, B, R = -6.0, 0.0, 3.0, 6.0
        H, Y = 1.5, 0.15
        outline = Rectangle(width=R - L, height=H, color=INK, stroke_width=3).move_to([(L + R) / 2, Y, 0])

        def zone(x0, x1, op):
            return Rectangle(width=x1 - x0, height=H, stroke_width=0, fill_color=INK,
                             fill_opacity=op).move_to([(x0 + x1) / 2, Y, 0])

        z1, z2 = zone(L, A, 0.85), zone(A, B, 0.28)
        lbl_top = Y + H / 2 + 0.4
        l1 = _label("Most reliable", size=38, weight="BOLD").move_to([(L + A) / 2, lbl_top, 0])
        l2 = _label("Thins", size=38, weight="BOLD").move_to([(A + B) / 2, lbl_top, 0])
        l3 = _label("Nothing seen", size=38, weight="BOLD").move_to([(B + R) / 2, lbl_top, 0])

        def marker(x, text, drop):
            tick = Line([x, Y - H / 2 - 0.05, 0], [x, Y - H / 2 - drop, 0], color=INK, stroke_width=3)
            lbl = _label(text, size=34).next_to(tick.get_end(), DOWN, buff=0.12)
            return VGroup(tick, lbl)

        m1 = marker(A, "Reliable cutoff", 0.35)
        m2 = marker(B, "Training cutoff", 1.15)

        self.play(Write(title), FadeIn(meta), run_time=0.6)
        self.play(Create(outline), run_time=0.4)
        self.play(FadeIn(z1), FadeIn(l1), FadeIn(m1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(z2), FadeIn(l2), FadeIn(m2), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(l3), Indicate(outline.copy(), color=INK, scale_factor=1.0), run_time=0.6)
        self.wait(1.2)


class B06_StaleAnswer(Scene):
    """ILLUSTRATIVE worked example: 'Latest version of the tool?' — the
    snapshot answer (v2) beside today's (v3), a ≠ between them. No real tool
    or version. ~3.4s (audio 3.36s)."""

    def construct(self):
        self.camera.background_color = BG

        q = _label("Latest version of the tool?", size=48, weight="BOLD")
        q_box = SurroundingRectangle(q, color=INK, stroke_width=3.5, buff=0.35, corner_radius=0.15)
        qg = VGroup(q_box, q).move_to(UP * 2.4)
        meta = _label("ILLUSTRATIVE", size=30, color=SOFT).next_to(qg, DOWN, buff=0.25)

        def card(head, val, x):
            h = _label(head, size=38, color=SOFT)
            v = _label(val, size=120, weight="BOLD")
            body = VGroup(h, v).arrange(DOWN, buff=0.3)
            frame = RoundedRectangle(width=4.6, height=3.1, corner_radius=0.18, color=INK,
                                     stroke_width=3.5)
            return VGroup(frame, body.move_to(frame)).move_to([x, -1.25, 0])

        left = card("Claude's snapshot", "v2", -3.4)
        right = card("Today", "v3", 3.4)
        # drawn ≠ (no LaTeX dependency): two bars and a slash
        bars = VGroup(*[Line(LEFT * 0.55, RIGHT * 0.55, color=INK, stroke_width=10).shift(UP * dy)
                        for dy in (0.2, -0.2)])
        slash = Line([0.28, 0.6, 0], [-0.28, -0.6, 0], color=INK, stroke_width=10)
        neq = VGroup(bars, slash).move_to([0, -1.25, 0])

        self.play(FadeIn(qg), FadeIn(meta), run_time=0.5)
        self.play(FadeIn(left, shift=UP * 0.15), run_time=0.55)
        self.play(FadeIn(right, shift=UP * 0.15), run_time=0.55)
        self.play(Write(neq), run_time=0.4)
        self.wait(1.4)
