"""scenes.py — portrait (9:16) Manim scenes for claude-liam-context-window/vertical.

Rendered by run.sh at 2160x3840 (aspect_ratio 9:16) → frame is 4.5 x 8 units.
Palette: cream #FAF9F5, ink #3D3929. INK ONLY in every scene here — no
terracotta text or fills (sidesteps GATE T §8.3 on structural accent fills).
Illustrative token counts only — never presented as measured/real API output
(see SOURCES.md). No slant=ITALIC on multi-word text (Pango collapses spaces).
"""
from manim import *

BG    = ManimColor("#FAF9F5")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all text and fills
SOFT  = ManimColor("#6E6A57")   # secondary / muted text
GHOST = ManimColor("#A8A491")   # dimmed / placeholder

# Portrait sync (same fix as runtime/manim/animated_graphics.py): Manim CE takes
# pixel dims from -r W,H but leaves frame_width at the 16:9 default (14.22).
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

SAFE_W = 3.9                    # usable width inside the 4.5-unit portrait frame


def _label(text, size=28, color=None, weight=None, fit=True):
    # Lay out at 4x then scale down: Pango kerning at small font sizes
    # collapses word spaces ("Fixedceiling"), the big layout keeps them.
    kw = {"font_size": size * 4, "color": color or INK, "font": "EB Garamond"}
    if weight:
        kw["weight"] = weight
    t = Text(text, **kw).scale(0.25)
    if fit and t.width > SAFE_W:
        t.scale_to_fit_width(SAFE_W)
    return t


class B01_HesitantWriter(Scene):
    """Portrait stand-in for the landscape BrutalistHesitantWriter beat (the
    Remotion writer can't reach GATE T's portrait size floor on one line, and a
    second line adds a fixed 400ms pause that overruns the 3.2s beat). Same
    text and sequence: the naive line types in, 'Claude's memory.' dims and
    backspaces out, 'a fixed budget.' types in its place. Ink only. ~3.3s."""

    def construct(self):
        self.camera.background_color = BG

        line1 = _label("A context window is", size=44, fit=False)
        wrong = _label("Claude's memory.", size=44, fit=False)
        right = _label("a fixed budget.", size=44, fit=False)
        k = min(1.0, 3.7 / max(line1.width, wrong.width, right.width))  # clear of the ±1.95 edge
        for t in (line1, wrong, right):  # one shared scale so the lines match
            t.scale(k)
        lines = VGroup(line1, wrong).arrange(DOWN, buff=0.32).move_to(UP * 0.2)
        right.move_to(wrong)

        self.play(AddTextLetterByLetter(line1), run_time=0.6)
        self.play(AddTextLetterByLetter(wrong), run_time=0.5)
        self.wait(0.3)
        # reconsider: dim the wrong phrase, then backspace it out (as the
        # landscape writer does) — no strike line laid over the text
        self.play(wrong.animate.set_color(SOFT), run_time=0.25)   # SOFT keeps >= 4.5:1 on cream
        self.play(RemoveTextLetterByLetter(wrong), run_time=0.35)
        self.play(AddTextLetterByLetter(right), run_time=0.5)
        self.wait(0.75)   # clip >= the 3.2s slot, so the compiler never has to stretch it


class B04_TokenSplit(Scene):
    """Portrait restack of the landscape B04: 'context' -> 1 token on top,
    'windowing' -> 'window' + 'ing' -> 2 tokens beneath it, running-total
    bar across the bottom third. Same sequence and counts as the 16:9 scene."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Tokens, Not Words", size=40, weight="BOLD").move_to(UP * 3.0)
        self.play(Write(title), run_time=0.6)

        # ── running total bar, bottom third ─────────────────────────────
        BAR_W = 3.6
        bar_bg = Rectangle(width=BAR_W, height=0.42, color=GHOST, stroke_width=1.5,
                           fill_color=GHOST, fill_opacity=0.15).move_to(DOWN * 2.4)
        bar_label = _label("Running total", size=26, color=SOFT).next_to(bar_bg, UP, buff=0.2)
        bar_fill = Rectangle(width=0.01, height=0.42, color=INK, stroke_width=0,
                             fill_color=INK, fill_opacity=0.85).move_to(bar_bg).align_to(bar_bg, LEFT)
        bar_count = _label("0 tokens", size=32, weight="BOLD").next_to(bar_bg, DOWN, buff=0.28)
        self.play(Create(bar_bg), FadeIn(bar_label), FadeIn(bar_count), run_time=0.4)

        # ── "context" → one token ───────────────────────────────────────
        word1 = _label("context", size=60).move_to(UP * 1.9)
        self.play(FadeIn(word1), run_time=0.5)

        box1 = SurroundingRectangle(word1, color=INK, stroke_width=3.5, buff=0.2)
        counter1 = _label("1 token", size=30).next_to(box1, DOWN, buff=0.25)
        new_fill1 = Rectangle(width=BAR_W / 3, height=0.42, color=INK, stroke_width=0,
                              fill_color=INK, fill_opacity=0.85).move_to(bar_bg).align_to(bar_bg, LEFT)
        new_count1 = _label("1 token", size=32, weight="BOLD").move_to(bar_count)
        self.play(Create(box1), FadeIn(counter1), run_time=0.7)
        self.play(Transform(bar_fill, new_fill1), Transform(bar_count, new_count1), run_time=0.4)
        self.wait(0.3)

        # ── "windowing" → "window" + "ing" → two tokens ─────────────────
        word2 = _label("windowing", size=60).move_to(DOWN * 0.15)
        word2.scale_to_fit_width(3.2)   # boxes + split gap stay inside the ±1.95 safe width
        self.play(FadeIn(word2), run_time=0.5)

        # slice the one word so both pieces keep the same baseline
        part_a, part_b = word2[:6], word2[6:]
        self.play(part_a.animate.shift(LEFT * 0.2), part_b.animate.shift(RIGHT * 0.2),
                  run_time=0.4)

        bh = word2.height + 0.32
        box2a = Rectangle(width=part_a.width + 0.3, height=bh, color=INK,
                          stroke_width=3).move_to([part_a.get_center()[0], word2.get_center()[1], 0])
        box2b = Rectangle(width=part_b.width + 0.3, height=bh, color=INK,
                          stroke_width=3).move_to([part_b.get_center()[0], word2.get_center()[1], 0])
        counter2 = _label("2 tokens", size=30).next_to(VGroup(box2a, box2b), DOWN, buff=0.25)
        new_fill2 = Rectangle(width=BAR_W, height=0.42, color=INK, stroke_width=0,
                              fill_color=INK, fill_opacity=0.85).move_to(bar_bg).align_to(bar_bg, LEFT)
        new_count2 = _label("3 tokens", size=32, weight="BOLD").move_to(bar_count)
        self.play(Create(box2a), Create(box2b), FadeIn(counter2), run_time=0.7)
        self.play(Transform(bar_fill, new_fill2), Transform(bar_count, new_count2), run_time=0.4)
        self.wait(0.8)


class B06_CeilingClimb(Scene):
    """Portrait stand-in for the landscape AttritionChain (no AttritionChain916
    exists). Same data and labels: total 100; Turn 1 → Turn 8 (70 left) →
    Turn 15 (35 left) → Turn 22 — ceiling (0 left). The used total climbs a
    tall bar toward a dashed fixed-ceiling line while turn chips stack up
    beside it. ILLUSTRATIVE meta label stays on screen throughout. Ink only.
    Every label is >= size 30 so it clears GATE T's portrait floor (1.9% of
    3840px), and all text sits inside its title-safe box (above y = -2.85)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Room Remaining As\nTurns Accumulate", size=32, weight="BOLD")
        title.move_to([0, 2.97, 0]).to_edge(LEFT, buff=0.35)
        meta = _label("ILLUSTRATIVE —\nroom remaining,\nnot a measured trace", size=32, color=SOFT)
        meta.next_to(title, DOWN, buff=0.14).align_to(title, LEFT)
        self.play(Write(title), FadeIn(meta), run_time=0.6)

        # ── tall budget bar (right) with the fixed ceiling at its top ───
        BOT, TOP = -2.55, 0.9
        H = TOP - BOT
        BX, BW = 1.55, 0.6
        LX = BX - BW / 2 - 0.2          # right edge of the turn labels
        bar_bg = Rectangle(width=BW, height=H, color=GHOST, stroke_width=1.5,
                           fill_color=GHOST, fill_opacity=0.15).move_to([BX, (BOT + TOP) / 2, 0])
        ceiling = DashedLine([BX - 0.45, TOP, 0], [BX + 0.4, TOP, 0], color=INK,
                             stroke_width=4, dash_length=0.12)

        def fill_to(frac):
            h = max(H * frac, 0.01)
            return Rectangle(width=BW, height=h, color=INK, stroke_width=0,
                             fill_color=INK, fill_opacity=0.85).move_to(
                [BX, BOT + h / 2, 0])

        fill = fill_to(0.0)
        self.play(Create(bar_bg), Create(ceiling), run_time=0.5)
        self.add(fill)

        # ── turn labels (left), each pinned to the height the total reaches ──
        def one_line(name, sub):
            return VGroup(_label(name, size=32, weight="BOLD"),
                          _label(sub, size=32, color=SOFT)).arrange(RIGHT, buff=0.14,
                                                                    aligned_edge=DOWN)

        stages = [(one_line("Turn 1", "· 100 left"), 1.0),
                  (one_line("Turn 8", "· 70 left"), 0.7),
                  (one_line("Turn 15", "· 35 left"), 0.35),
                  (VGroup(_label("Turn 22 —", size=32, weight="BOLD"),
                          _label("ceiling · 0 left", size=32, color=SOFT)).arrange(DOWN, buff=0.08,
                                                                         aligned_edge=RIGHT), 0.0)]
        for i, (lbl, survival) in enumerate(stages):
            used = 1.0 - survival
            y = BOT + H * used
            lbl.move_to([0, y, 0]).align_to([LX, 0, 0], RIGHT)
            if i == len(stages) - 1:     # "Turn 22 —" sits on the ceiling, the rest beneath
                lbl.shift(DOWN * (lbl[0].get_center()[1] - y))
            tick = Line([LX + 0.06, y, 0], [BX - BW / 2, y, 0], color=GHOST, stroke_width=2)
            anims = [FadeIn(lbl, shift=UP * 0.15), Create(tick)]
            if i > 0:
                anims.append(Transform(fill, fill_to(used)))
            self.play(*anims, run_time=0.8)
            self.wait(0.3)

        self.play(Indicate(ceiling, color=INK, scale_factor=1.06), run_time=0.6)
        self.wait(0.6)


class B11_OutroCard(Scene):
    """Portrait title card standing in for the landscape OutroSeries (no
    OutroSeries916; LogoOutro916 has no title slot). Same text as the 16:9
    outro: eyebrow '@HumanitariansAI', line 'The Context Window Isn't Memory.',
    underline drawing in beneath. Ink only."""

    def construct(self):
        self.camera.background_color = BG

        eyebrow = _label("@HumanitariansAI", size=30, color=SOFT, weight="BOLD")
        line = VGroup(_label("The Context Window", size=46, fit=False),
                      _label("Isn't Memory.", size=46, fit=False)).arrange(DOWN, buff=0.18)
        if line.width > SAFE_W:      # scale both lines together so they match
            line.scale_to_fit_width(SAFE_W)
        group = VGroup(eyebrow, line).arrange(DOWN, buff=0.55).move_to(UP * 0.25)
        underline = Line(LEFT * 0.75, RIGHT * 0.75, color=INK, stroke_width=5)
        underline.next_to(line, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow, shift=UP * 0.1), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(line, shift=UP * 0.1), run_time=0.7)
        self.wait(0.5)
        self.play(Create(underline), run_time=0.7)
        self.wait(2.6)
