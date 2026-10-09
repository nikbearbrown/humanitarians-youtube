"""scenes.py — portrait (9:16) Manim scenes for knowledge-cutoff/vertical.

Rendered by run.sh at 2160x3840 → frame is 4.5 x 8 units.
Palette: cream #FAF9F5, ink #3D3929. INK ONLY — no terracotta text or fills.
Explicit font on every Text: EB Garamond. GHOST is for shapes only.
Every label is >= size 32 (GATE T portrait floor, 1.9% of 3840 px) and all
text sits inside the title-safe box (y between -2.85 and 3.4).
B04 / B06 are ILLUSTRATIVE (labelled on screen). Same text as the 16:9 scenes.
"""
from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
SOFT  = ManimColor("#6E6A57")   # >= 4.5:1 on cream
GHOST = ManimColor("#A8A491")   # shapes only
CARD  = ManimColor("#FFFFFF")

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width
# at the 16:9 default (14.22).
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

SAFE_W = 3.9


def _label(text, size=32, color=None, weight=None, fit=True, max_w=SAFE_W):
    m = 4 if len(text) * size < 1100 else 2      # long lines at 4x wrap in Pango
    kw = {"font_size": size * m, "color": color or INK, "font": "EB Garamond"}
    if weight:
        kw["weight"] = weight
    t = Text(text, **kw).scale(1 / m)
    if fit and t.width > max_w:
        t.scale_to_fit_width(max_w)
    return t


def _stack(lines, size, weight=None, color=None, buff=0.14):
    """Several lines at ONE shared scale (so they match), centered."""
    ts = [_label(l, size=size, weight=weight, color=color, fit=False) for l in lines]
    g = VGroup(*ts).arrange(DOWN, buff=buff)
    if g.width > SAFE_W:
        g.scale_to_fit_width(SAFE_W)
    return g


def _doc(color=INK):
    page = Rectangle(width=0.36, height=0.48, color=color, stroke_width=3,
                     fill_color=CARD, fill_opacity=1)
    rules = VGroup(*[Line(LEFT * 0.1, RIGHT * 0.1, color=color, stroke_width=2.5)
                     for _ in range(3)]).arrange(DOWN, buff=0.08).move_to(page)
    return VGroup(page, rules)


class B01_HesitantWriter(Scene):
    """'Claude knows' / 'everything up to today.' types in; the second line
    dims and backspaces out; 'what it learned' / 'before its cutoff.' types
    in its place. Ink only. ~4.6s (audio 4.56s)."""

    def construct(self):
        self.camera.background_color = BG

        size = 44
        line1 = _label("Claude knows", size=size, fit=False)
        wrong = VGroup(_label("everything", size=size, fit=False),
                       _label("up to today.", size=size, fit=False))
        right = VGroup(_label("what it learned", size=size, fit=False),
                       _label("before its cutoff.", size=size, fit=False))
        allw = max(line1.width, *[t.width for t in [*wrong, *right]])
        k = min(1.0, 3.7 / allw)
        for t in (line1, *wrong, *right):
            t.scale(k)
        gap = 0.3
        line1.move_to(UP * 0.9)
        for grp in (wrong, right):
            grp.arrange(DOWN, buff=gap, aligned_edge=LEFT)
            grp.next_to(line1, DOWN, buff=gap, aligned_edge=LEFT)
        left_x = -allw * k / 2
        for t in (line1, wrong, right):
            t.shift(RIGHT * (left_x - t.get_left()[0]))

        self.play(AddTextLetterByLetter(line1), run_time=0.45)
        self.play(AddTextLetterByLetter(wrong[0]), run_time=0.3)
        self.play(AddTextLetterByLetter(wrong[1]), run_time=0.3)
        self.wait(0.25)
        self.play(wrong.animate.set_color(SOFT), run_time=0.25)
        self.play(RemoveTextLetterByLetter(wrong[1]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(wrong[0]), run_time=0.2)
        self.play(AddTextLetterByLetter(right[0]), run_time=0.4)
        self.play(AddTextLetterByLetter(right[1]), run_time=0.45)
        self.wait(1.8)


class B02_Snapshot(Scene):
    """Portrait restack: time runs DOWN a vertical axis. Chips above the
    dashed cutoff line rise into the Training box at the top; chips below it
    push up to the line, bounce back, and dim. ~4.5s (audio 4.42s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _stack(["Training Is", "a Snapshot"], size=40, weight="BOLD").move_to(UP * 2.6)
        box = RoundedRectangle(width=3.7, height=0.95, corner_radius=0.12, color=INK,
                               stroke_width=4).move_to(UP * 1.3)
        box_lbl = _label("Training", size=36, weight="BOLD").next_to(box, DOWN, buff=0.15).align_to(box, RIGHT)

        AX_X, TOP, BOT, CUT_Y = -1.45, 0.45, -2.55, -1.35
        axis = Arrow([AX_X, TOP, 0], [AX_X, BOT, 0], color=INK, stroke_width=4, buff=0,
                     max_tip_length_to_length_ratio=0.05)
        time_lbl = _label("time", size=34, color=SOFT).next_to(axis.get_end(), RIGHT, buff=0.15)
        cut = DashedLine([AX_X - 0.35, CUT_Y, 0], [1.9, CUT_Y, 0], color=INK,
                         stroke_width=5, dash_length=0.14)
        cut_lbl = _label("cutoff", size=36, weight="BOLD").next_to(cut, UP, buff=0.1).align_to(cut, RIGHT)

        self.play(Write(title), run_time=0.5)
        self.play(Create(box), FadeIn(box_lbl), Create(axis), FadeIn(time_lbl),
                  Create(cut), FadeIn(cut_lbl), run_time=0.6)

        # chips sit to the right of the axis, two columns before the cutoff
        before_pos = [(-0.9, -0.3), (-0.3, -0.3), (0.3, -0.3), (0.9, -0.3),
                      (-0.9, -0.85), (-0.3, -0.85), (0.3, -0.85)]   # 4 + 3: clear of the 'cutoff' label
        after_pos = [(-0.9, -1.9), (-0.3, -1.9), (0.3, -1.9)]
        before = VGroup(*[_doc().move_to([x, y, 0]) for x, y in before_pos])
        after = VGroup(*[_doc().move_to([x, y, 0]) for x, y in after_pos])
        self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 0.15) for d in [*before, *after]],
                              lag_ratio=0.08), run_time=0.6)

        slots = [box.get_left() + RIGHT * (0.35 + 0.5 * i) for i in range(len(before))]
        self.play(*[d.animate.move_to(s) for d, s in zip(before, slots)], run_time=1.0)

        push = (CUT_Y - 0.32) - after[0].get_center()[1]
        self.play(*[d.animate.shift(UP * push) for d in after], run_time=0.35, rate_func=rush_into)
        self.play(*[d.animate.shift(DOWN * 0.3).set_stroke(GHOST) for d in after],
                  run_time=0.35, rate_func=rush_from)
        self.wait(1.1)


class B04_EdgeThins(Scene):
    """ILLUSTRATIVE vertical band, time running down: solid ink 'Most
    reliable' to the 'Reliable cutoff', lighter 'Thins' to the 'Training
    cutoff', empty 'Nothing seen' beyond. ~5.1s (audio 5.04s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _stack(["Between the Dates,", "Knowledge Thins"], size=40, weight="BOLD").move_to(UP * 2.6)
        meta = _label("ILLUSTRATIVE", size=34, color=SOFT).next_to(title, DOWN, buff=0.18)

        X, W = -1.25, 1.1
        T, A, B, Bot = 1.4, -0.5, -1.65, -2.75
        outline = Rectangle(width=W, height=T - Bot, color=INK, stroke_width=3).move_to([X, (T + Bot) / 2, 0])

        def zone(y0, y1, op):
            return Rectangle(width=W, height=y0 - y1, stroke_width=0, fill_color=INK,
                             fill_opacity=op).move_to([X, (y0 + y1) / 2, 0])

        z1, z2 = zone(T, A, 0.85), zone(A, B, 0.28)
        LX = X + W / 2 + 0.2

        def zlabel(text, y):
            return _label(text, size=36, weight="BOLD", max_w=1.95 - LX).move_to([0, y, 0]).align_to([LX, 0, 0], LEFT)

        def marker(y, text):
            tick = Line([X + W / 2, y, 0], [LX + 0.0, y, 0], color=INK, stroke_width=3)
            lbl = _label(text, size=34, max_w=1.95 - LX - 0.18).next_to(tick, RIGHT, buff=0.08)
            return VGroup(tick, lbl)

        l1, l2, l3 = zlabel("Most reliable", (T + A) / 2 + 0.2), zlabel("Thins", (A + B) / 2), zlabel("Nothing seen", (B + Bot) / 2)
        m1, m2 = marker(A, "Reliable cutoff"), marker(B, "Training cutoff")
        # markers sit on the boundary; nudge zone labels clear of them
        l2.shift(UP * 0.0)

        self.play(Write(title), FadeIn(meta), run_time=0.6)
        self.play(Create(outline), run_time=0.4)
        self.play(FadeIn(z1), FadeIn(l1), FadeIn(m1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(z2), FadeIn(l2), FadeIn(m2), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(l3), run_time=0.6)
        self.wait(1.2)


class B06_StaleAnswer(Scene):
    """ILLUSTRATIVE worked example, stacked: question card on top, the
    snapshot answer (v2) above today's (v3) with a drawn ≠ between.
    ~3.4s (audio 3.36s)."""

    def construct(self):
        self.camera.background_color = BG

        q = _stack(["Latest version", "of the tool?"], size=38, weight="BOLD")
        q_box = SurroundingRectangle(q, color=INK, stroke_width=3.5, buff=0.25, corner_radius=0.12)
        qg = VGroup(q_box, q).move_to(UP * 2.5)
        meta = _label("ILLUSTRATIVE", size=34, color=SOFT).next_to(qg, DOWN, buff=0.18)

        def card(head, val, y):
            h = _label(head, size=36, color=SOFT, max_w=3.5)
            v = _label(val, size=80, weight="BOLD")
            body = VGroup(h, v).arrange(DOWN, buff=0.1)
            frame = RoundedRectangle(width=3.9, height=1.45, corner_radius=0.14, color=INK,
                                     stroke_width=3.5)
            return VGroup(frame, body.move_to(frame)).move_to([0, y, 0])

        top = card("Claude's snapshot", "v2", 0.3)
        bot = card("Today", "v3", -2.1)
        bars = VGroup(*[Line(LEFT * 0.4, RIGHT * 0.4, color=INK, stroke_width=9).shift(UP * dy)
                        for dy in (0.14, -0.14)])
        slash = Line([0.16, 0.32, 0], [-0.16, -0.32, 0], color=INK, stroke_width=9)
        neq = VGroup(bars, slash).move_to([0, -0.9, 0])

        self.play(FadeIn(qg), FadeIn(meta), run_time=0.5)
        self.play(FadeIn(top, shift=DOWN * 0.15), run_time=0.55)
        self.play(FadeIn(bot, shift=UP * 0.15), run_time=0.55)
        self.play(Write(neq), run_time=0.4)
        self.wait(1.4)


class B11_OutroCard(Scene):
    """Portrait title card standing in for the landscape OutroSeries (no
    OutroSeries916). Same text: eyebrow '@HumanitariansAI', line 'What Is a
    Knowledge Cutoff?', ink underline drawing in. ~5.1s (audio 5.02s)."""

    def construct(self):
        self.camera.background_color = BG

        eyebrow = _label("@HumanitariansAI", size=34, color=SOFT, weight="BOLD")
        line = _stack(["What Is a", "Knowledge Cutoff?"], size=50, buff=0.18)
        group = VGroup(eyebrow, line).arrange(DOWN, buff=0.55).move_to(UP * 0.25)
        underline = Line(LEFT * 0.75, RIGHT * 0.75, color=INK, stroke_width=5)
        underline.next_to(line, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow, shift=UP * 0.1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(line, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)
        self.play(Create(underline), run_time=0.7)
        self.wait(2.3)
