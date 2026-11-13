"""
Manim scenes for 2026-09-14-b3-the-link-that-pointed-nowhere/vertical
(full-length 9:16 companion — NOT a Shorts derivative: every beat kept,
full runtime, no drops, no endcard, per PIPELINE-SAFETY.md / THE SHORTS LAW.)

Built via `./art vertical` (runtime/scripts/shorts.py --vertical): 0 beats
dropped, every beat's mp3 is the parent's unchanged narration (copied into
vertical/mp3/). This file supplies ONLY the visual half: a genuine
hand-authored portrait (2160x3840-native, working in the same 4.5x8.0 unit
frame convention) re-layout of each of the 10 parent Manim scenes in
../scenes.py — per THE REFORMAT RULE, generated graphics are NEVER
auto-cropped. Same beat_id -> class name mapping, same
PALETTE/MONO/fit()/box_around(), same per-beat animation timing (every
self.play run_time and self.wait matches the parent beat-for-beat, since the
audio is identical) — only the geometry changes.

House style ported verbatim from this fellow's own prior portrait short,
2026-09-07-the-synonyms-the-classifier-never-learned/short/scenes.py:
frame-sync fix, SAFE_W, fit()/box_around()/clear_of_hdivider().

Real redesigns (not a mechanical shrink) — the 3 beats this build calls out
(the parent's side-by-side / multi-column beats):
  B04 ResolutionFlowDiagram — parent is a 4-box horizontal pipeline
                        (Redirect page -> id/timestamp/signature -> POST ->
                        Real article URL). Portrait restacks it as a
                        vertical pipeline, same 4 boxes/colors, downward
                        arrows instead of rightward ones — same reading
                        order the narration walks.
  B05 OrderingNearMiss  — parent is LEFT (old order, broken) / RIGHT (fixed
                        order) with a vertical divider. Portrait stacks
                        TOP / BOTTOM with a horizontal divider
                        (clear_of_hdivider).
  B07 HonestLimits      — parent is LEFT (not yet verified) / RIGHT (added
                        cost) with a vertical divider. Portrait stacks
                        TOP / BOTTOM with a horizontal divider
                        (clear_of_hdivider).

Every other beat (B00, B01, B02, B03, B06, B08, B09) was already a single
vertical column in the parent — these keep the same composition, narrower
widths/re-wrapped text and tuned fonts/buffs for portrait canvas-fill (same
law the parent's own GATE V fixes documented: grow the gaps until both axes
clear the 55% floor, verified by rendering — not guessed).
"""

from manim import *

# Portrait sync (same fix as this fellow's sibling short and the shared
# runtime/manim/animated_graphics.py fixture): Manim CE's CLI sets pixel
# dims from `-r W,H` but does NOT recompute frame_width to match — it
# leaves the 16:9 default (14.22) and stretches frame_height instead, so a
# portrait scene composed against an assumed 4.5-unit-wide frame actually
# renders at roughly a third of its intended size. Keep frame_height 8.0,
# derive frame_width from the real pixel aspect.
try:
    _pw = getattr(config, "pixel_width", None)
    _ph = getattr(config, "pixel_height", None)
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool
    "crimson": "#E4572E", # bad / CVD-safe warm
    "slate":  "#29335C",  # structure
    "gold":   "#F3A712",  # fill only — never text color
    "sage":   "#A8C686",  # human / growth
}

MONO = "Courier New"

SAFE_W = 3.8   # working full-width inside the 4.5-wide portrait frame (safe box full-width ~3.9)


def fit(mob, max_w=SAFE_W):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See BUILD-LOG.md for the empirical proof."""
    t = Text(text, font_size=SAFE_TEXT_BASE, **kwargs)
    if font_size != SAFE_TEXT_BASE:
        t.scale(font_size / SAFE_TEXT_BASE)
    return t


def panel(width, height, fill=None, stroke=None, corner_radius=0.1, opacity=1.0):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        fill_color=fill or PALETTE["ink"], fill_opacity=opacity,
        stroke_color=stroke or PALETTE["slate"], stroke_width=2,
    )


def box_around(mob, color, buff=0.1):
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color, stroke_width=3, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


def clear_of_hdivider(block, divider_y, side, margin=0.3):
    """Portrait analogue of the parent scenes.py's clear_of_divider() — same
    pattern (measure the block's OWN rendered bounds, shift the whole rigid
    unit by the real overhang, never a per-line rescale), rotated 90
    degrees: every side-by-side split in the parent (a vertical divider with
    LEFT/RIGHT panels) becomes a top/bottom stack here (a horizontal divider
    with TOP/BOTTOM panels). Ported verbatim from the sibling short's own
    scenes.py.

    side="top"    -> block sits ABOVE the divider; keeps get_bottom()[1] >=
                      divider_y + margin.
    side="bottom" -> block sits BELOW the divider; keeps get_top()[1] <=
                      divider_y - margin.
    """
    if side == "top":
        overhang = (divider_y + margin) - block.get_bottom()[1]
        if overhang > 0:
            block.shift(UP * overhang)
    else:
        overhang = block.get_top()[1] - (divider_y - margin)
        if overhang > 0:
            block.shift(DOWN * overhang)
    return block


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent title card. Already a single vertical column.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T(
            "The Link That\nPointed Nowhere", color=PALETTE["ink"], font_size=46,
            weight="BOLD", line_spacing=1.05,
        ))

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=30))

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=1.1).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # animation sum = 1.65s; measured silent track = 4.05s
        self.wait(2.40)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: name/role/accent/summary, same 4-element stack as the
# parent — summary re-wrapped for the narrow column.
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(T(
            "Sai Pranavi J.", color=PALETTE["ink"], font_size=42,
            weight="BOLD", line_spacing=1.0,
        ))
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=20))
        accent = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        summary = fit(T(
            "Every stored Google\nNews link was a\ndead-end redirect —\n"
            "the fix had to\nreverse-engineer how\nGoogle News resolves it.",
            color=PALETTE["ink"], font_size=24, line_spacing=1.08,
        ))

        VGroup(name, role, accent, summary).arrange(DOWN, buff=0.62).move_to(ORIGIN)
        summary_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(name, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        summary_underline.put_start_and_end_on(
            summary.get_corner(DL) + DOWN * 0.12, summary.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(summary_underline), run_time=0.3)
        # animation sum = 2.8s; measured narration = 17.18s
        self.wait(14.38)


# --------------------------------------------------------------------------- #
# B02 — HOOK: feed item card, click bounces back to Google News. Already a
# single vertical column in the parent — narrower card, re-wrapped text.
# --------------------------------------------------------------------------- #
class B02_DeadEndLinkHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(T(
            "A feed item, and\nits stored link", color=PALETTE["slate"],
            font_size=28, weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.7)
        self.play(Write(header), run_time=0.5)

        card = panel(3.5, 1.75, fill=PALETTE["bg"], stroke=PALETTE["slate"], opacity=1.0)
        card_title = fit(T(
            "FINRA Enforcement\nUpdate — Google News", color=ink, font_size=17,
            weight="BOLD", line_spacing=1.05,
        ), 3.2)
        card_link = fit(T(
            "link: news.google.com/\nrss/articles/CBMi...", color=PALETTE["teal"],
            font_size=14, font=MONO, line_spacing=1.05,
        ), 3.2)
        card_body = VGroup(card_title, card_link).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        card_body.move_to(card.get_center())
        feed_card = VGroup(card, card_body)
        # buffs trimmed (0.7/0.15-1.15/0.25/0.4 -> 0.55/0.1-0.9/0.15/0.3):
        # GATE B measured the first draft's caption bottom at y=-3.79, past
        # the -3.4 safe floor.
        feed_card.next_to(header, DOWN, buff=0.55)
        self.play(FadeIn(feed_card, shift=UP * 0.1), run_time=0.6)

        click_arrow = Arrow(
            start=feed_card.get_bottom() + DOWN * 0.1,
            end=feed_card.get_bottom() + DOWN * 0.9,
            color=PALETTE["gold"], stroke_width=5, buff=0,
        )
        click_label = fit(T("click", color=PALETTE["gold"], font_size=20, weight="BOLD"))
        click_label.next_to(click_arrow, RIGHT, buff=0.2)
        self.play(Create(click_arrow), Write(click_label), run_time=0.5)

        outcome = panel(3.4, 1.3, fill=PALETTE["ink"], stroke=PALETTE["crimson"], opacity=1.0)
        outcome_text = fit(T(
            "back to Google News\n— not the article", color=PALETTE["bg"],
            font_size=18, weight="BOLD", line_spacing=1.05,
        ), 3.1)
        outcome_group = VGroup(outcome, outcome_text)
        outcome_group.next_to(click_arrow, DOWN, buff=0.15)
        self.play(FadeIn(outcome_group, shift=UP * 0.1), run_time=0.6)

        caption = fit(T(
            "the link was never\nreal to begin with",
            color=PALETTE["crimson"], font_size=20, line_spacing=1.05,
        ))
        caption.next_to(outcome_group, DOWN, buff=0.3)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.6+0.5+0.6+0.5+0.3 = 3.0s; measured narration = 10.78s
        self.wait(7.78)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the failing regex next to a real modern link, missing url=
# highlighted. Already a single vertical column — re-wrapped/resized code.
# --------------------------------------------------------------------------- #
class B03_RegexVsRealLink(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(T(
            "The fix looked for a\nparameter that's gone", color=cream,
            font_size=26, weight="BOLD", line_spacing=1.05,
        ))
        header.to_edge(UP, buff=0.7)
        self.play(Write(header), run_time=0.5)

        regex_label = fit(T("THE OLD FIX", color=PALETTE["teal"], font_size=18, font=MONO, weight="BOLD"))
        regex_code = fit(T(
            "link.match(/url=\n([^&]+)/)", color=cream, font_size=24, font=MONO, line_spacing=1.1,
        ))
        regex_block = VGroup(regex_label, regex_code).arrange(DOWN, buff=0.25)
        regex_block.next_to(header, DOWN, buff=0.7)
        self.play(FadeIn(regex_block, shift=UP * 0.1), run_time=0.6)

        # "looking for: url=" placed BELOW the arrow, not beside it (portrait
        # fix): GATE B measured a beside-the-arrow placement at x up to 2.77,
        # off the +-1.95 safe width — the narrow column has no room to the
        # side of a centered arrow the way the 16:9 parent does.
        down_arrow = Arrow(
            start=regex_block.get_bottom() + DOWN * 0.2,
            end=regex_block.get_bottom() + DOWN * 0.85,
            color=PALETTE["gold"], stroke_width=5, buff=0,
        )
        looking_for = fit(T("looking for: url=", color=PALETTE["gold"], font_size=17, font=MONO))
        looking_for.next_to(down_arrow, DOWN, buff=0.15)
        self.play(Create(down_arrow), Write(looking_for), run_time=0.4)

        link_label = fit(T("A REAL MODERN LINK", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD"))
        link_code = fit(T(
            "news.google.com/rss/\narticles/<opaque-id>?oc=5", color=cream,
            font_size=17, font=MONO, line_spacing=1.15,
        ), 3.5)
        link_block = VGroup(link_label, link_code).arrange(DOWN, buff=0.25)
        link_block.next_to(looking_for, DOWN, buff=0.4)
        self.play(FadeIn(link_block, shift=UP * 0.1), run_time=0.6)

        missing_box = box_around(link_code, PALETTE["crimson"], buff=0.14)
        missing_label = fit(T(
            "no url= parameter\nanywhere in this link", color=PALETTE["crimson"],
            font_size=18, weight="BOLD", line_spacing=1.05,
        ))
        missing_label.next_to(missing_box, DOWN, buff=0.35)
        self.play(Create(missing_box), Write(missing_label), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            missing_label.get_corner(DL) + DOWN * 0.12, missing_label.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.6+0.4+0.6+0.5+0.3 = 2.9s; measured narration = 18.82s
        self.wait(15.92)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: REAL redesign. Parent is a 4-box HORIZONTAL pipeline
# (Redirect page -> id/timestamp/signature -> POST -> Real article URL).
# Portrait restacks it VERTICALLY, same 4 boxes/colors/order, downward
# arrows instead of rightward — same reading order the narration walks. The
# FACTCHECK-required caveat label stays full-size and clearly legible.
# --------------------------------------------------------------------------- #
class B04_ResolutionFlowDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(T(
            "How the page itself\ngets the real URL", color=ink,
            font_size=26, weight="BOLD", line_spacing=1.05,
        ))
        header.to_edge(UP, buff=0.68)
        self.play(Write(header), run_time=0.5)

        step_labels = [
            "Redirect page",
            "id + timestamp\n+ signature",
            "POST to internal\nendpoint",
            "Real article URL",
        ]
        step_colors = [PALETTE["slate"], PALETTE["teal"], PALETTE["teal"], PALETTE["crimson"]]
        steps = VGroup()
        for label, color in zip(step_labels, step_colors):
            box = panel(3.2, 0.72, fill=PALETTE["ink"], stroke=color, opacity=1.0)
            text = fit(T(label, color=PALETTE["bg"], font_size=17, font=MONO,
                             weight="BOLD", line_spacing=1.0), 2.9)
            text.move_to(box.get_center())
            steps.add(VGroup(box, text))
        # buffs trimmed (0.32/0.5 -> 0.22/0.3): GATE B measured the caveat
        # bottom at y=-3.53, past the -3.4 safe floor.
        steps.arrange(DOWN, buff=0.22)
        steps.next_to(header, DOWN, buff=0.45)

        arrows = VGroup(*[
            Arrow(steps[i].get_bottom(), steps[i + 1].get_top(), color=PALETTE["gold"],
                  stroke_width=4, buff=0.06)
            for i in range(len(steps) - 1)
        ])

        self.play(LaggedStart(*[FadeIn(s, scale=0.9) for s in steps], lag_ratio=0.25), run_time=1.0)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.2), run_time=0.6)

        # box sized FROM the text's real rendered bounds (not a hardcoded
        # guess): a fixed height=1.1 box clipped this 3-line caveat text
        # top and bottom (the underline cut straight through "official
        # API") — visible only by looking at an actual frame, not caught by
        # any gate. box_around()-style padding, never a fixed size.
        caveat_text = fit(T(
            "reverse-engineered —\nnot a documented/\nofficial API",
            color=PALETTE["crimson"], font_size=22, weight="BOLD", line_spacing=1.1,
        ), 3.3)
        caveat_box = Rectangle(
            width=caveat_text.width + 0.4, height=caveat_text.height + 0.3,
            stroke_color=PALETTE["crimson"], stroke_width=3,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
        )
        caveat_box.move_to(caveat_text.get_center())
        caveat = VGroup(caveat_box, caveat_text)
        caveat.next_to(steps, DOWN, buff=0.3)
        self.play(FadeIn(caveat, shift=UP * 0.1), run_time=0.6)

        underline = Line(color=PALETTE["sage"], stroke_width=1)
        underline.put_start_and_end_on(
            caveat.get_corner(DL) + DOWN * 0.15, caveat.get_corner(DR) + DOWN * 0.15
        )
        self.play(Create(underline), run_time=0.3)

        # animation sum = 0.5+1.0+0.6+0.6+0.3 = 3.0s; measured narration = 19.73s
        self.wait(16.73)


# --------------------------------------------------------------------------- #
# B05 — NEAR-MISS: REAL redesign. Parent is LEFT (old order, broken) / RIGHT
# (fixed order) with a vertical divider. Portrait stacks TOP / BOTTOM with a
# horizontal divider (clear_of_hdivider) — same reading order (old order
# first, then fixed).
# --------------------------------------------------------------------------- #
class B05_OrderingNearMiss(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(T(
            "Two call orders — only\none survives the fix", color=cream,
            font_size=24, weight="BOLD", line_spacing=1.05,
        ))
        header.to_edge(UP, buff=0.68)
        self.play(Write(header), run_time=0.5)

        # TOP — old order: extractRealUrl() THEN identifySource(). Breaks
        # silently once the fix ships.
        top_label = fit(T("OLD ORDER — BROKEN\nONCE THE FIX SHIPS", color=PALETTE["crimson"],
                              font_size=16, font=MONO, weight="BOLD", line_spacing=1.05))
        top_steps = [
            "1. extractRealUrl(link)",
            "2. identifySource(link)",
            "-> link is now",
            "   mayerbrown.com",
            "-> \"news.google.com\"",
            "   != match",
            "-> FINRA -> Unknown",
        ]
        # buffs trimmed throughout this beat (line/internal/inter-block/
        # caption): GATE B measured the first draft's caption bottom at
        # y=-4.23 — off-frame — this side-by-side-to-stack redesign has
        # more total lines (7+6) than the safe height comfortably holds at
        # the sibling short's default spacing.
        top_lines = VGroup(*[
            fit(T(l, color=cream, font_size=15, font=MONO), 3.5) for l in top_steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.07)
        top_block = VGroup(top_label, top_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        top_block.next_to(header, DOWN, buff=0.25)

        # BOTTOM — fixed order: identifySource() on the ORIGINAL link first.
        bottom_label = fit(T("FIXED ORDER —\nCLASSIFY FIRST", color=PALETTE["teal"],
                                 font_size=16, font=MONO, weight="BOLD", line_spacing=1.05))
        bottom_steps = [
            "1. identifySource(rawLink)",
            "2. extractRealUrl(link)",
            "-> classified while link",
            "   is still news.google.com",
            "-> FINRA Enforcement",
            "   News",
        ]
        bottom_lines = VGroup(*[
            fit(T(l, color=cream, font_size=15, font=MONO), 3.5) for l in bottom_steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.07)
        bottom_block = VGroup(bottom_label, bottom_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        bottom_block.next_to(top_block, DOWN, buff=0.35)

        divider_y = (top_block.get_bottom()[1] + bottom_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.6, RIGHT * 1.6, color=cream, stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(top_block, divider_y, side="top", margin=0.2)
        clear_of_hdivider(bottom_block, divider_y, side="bottom", margin=0.2)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(top_block, shift=DOWN * 0.1),
            FadeIn(bottom_block, shift=UP * 0.1),
            run_time=0.8,
        )

        caption = fit(T(
            "caught before it ever\nshipped — by classifying\non the original link first",
            color=PALETTE["sage"], font_size=18, line_spacing=1.1,
        ))
        caption.next_to(bottom_block, DOWN, buff=0.28)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.3+0.8+0.6+0.3 = 2.5s; measured narration = 28.66s
        self.wait(26.16)


# --------------------------------------------------------------------------- #
# B06 — PROOF: all 3 escalating rounds + the final round's real resolved
# URLs. Already a single vertical column — rounds restacked label-over-score
# (too wide side by side in the narrow column), URLs restacked 2x3 grid.
# --------------------------------------------------------------------------- #
class B06_ThreeRoundProof(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        # This beat carries the most total lines of any portrait redesign
        # (header + 3 rounds + 6 URLs + caption) — GATE B measured a first,
        # single-column-of-6-URLs draft with the sibling's default spacing
        # at a caption bottom of y=-4.63, badly off-frame. Fix: the URL list
        # restacks as a 2x3 grid (half the vertical run of 6 stacked lines),
        # and every buff below is compacted accordingly.
        header = fit(T(
            "Three rounds, each\ncloser to the real system", color=ink,
            font_size=24, weight="BOLD", line_spacing=1.05,
        ))
        header.to_edge(UP, buff=0.62)
        self.play(Write(header), run_time=0.5)

        rounds_data = [
            ("ROUND 1 — script prototype", "20 / 20", PALETTE["teal"]),
            ("ROUND 2 — exact code, ported", "16 / 16", PALETTE["teal"]),
            ("ROUND 3 — real node, live run", "6 / 6", PALETTE["crimson"]),
        ]
        round_cards = VGroup()
        for label, score, color in rounds_data:
            label_t = fit(T(label, color=ink, font_size=14, font=MONO, weight="BOLD"), 3.4)
            score_t = T(score, color=color, font_size=22, font=MONO, weight="BOLD")
            row = VGroup(label_t, score_t).arrange(DOWN, buff=0.05)
            round_cards.add(row)
        round_cards.arrange(DOWN, buff=0.22)
        round_cards.next_to(header, DOWN, buff=0.32)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.08) for r in round_cards], lag_ratio=0.25), run_time=1.0)

        round3_box = box_around(round_cards[2], PALETTE["crimson"], buff=0.12)
        self.play(Create(round3_box), run_time=0.4)

        url_header = fit(T(
            "round 3's 6 real\nresolved URLs:", color=PALETTE["slate"], font_size=15,
            font=MONO, line_spacing=1.05,
        ))
        urls = [
            "mcguirewoods.com", "freshfields.com", "mayerbrown.com",
            "jdsupra.com", "morganlewis.com", "ai-cio.com",
        ]
        url_cells = VGroup(*[fit(T(u, color=ink, font_size=14, font=MONO), 1.75) for u in urls])
        url_grid = url_cells.arrange_in_grid(rows=3, cols=2, buff=(0.25, 0.14))
        url_block = VGroup(url_header, url_grid).arrange(DOWN, buff=0.2)
        url_block.next_to(round_cards, DOWN, buff=0.35)
        self.play(FadeIn(url_block, shift=UP * 0.1), run_time=0.8)

        caption = fit(T(
            "all 6 still correctly\nlabeled FINRA\nEnforcement News",
            color=PALETTE["teal"], font_size=18, weight="BOLD", line_spacing=1.05,
        ))
        caption.next_to(url_block, DOWN, buff=0.28)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+1.0+0.4+0.8+0.5+0.3 = 3.5s; measured narration = 23.54s
        self.wait(20.04)


# --------------------------------------------------------------------------- #
# B07 — HONEST LIMITS: REAL redesign. Parent is LEFT (not yet verified) /
# RIGHT (added cost) with a vertical divider. Portrait stacks TOP / BOTTOM
# with a horizontal divider (clear_of_hdivider). Both limitations kept at
# full weight, neither minimized — FACTCHECK.md's explicit resolution.
# --------------------------------------------------------------------------- #
class B07_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(T(
            "Two things I'm\nnot claiming", color=cream,
            font_size=27, weight="BOLD", line_spacing=1.05,
        ))
        header.to_edge(UP, buff=0.68)
        self.play(Write(header), run_time=0.5)

        top_label = fit(T("NOT YET VERIFIED", color=PALETTE["crimson"], font_size=21, weight="BOLD"))
        top_body = VGroup(*[
            fit(T(l, color=cream, font_size=18), 3.4) for l in
            ["on the fellow's actual", "live n8n instance —", "only on the workflow file"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        top_block = VGroup(top_label, top_body).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        top_block.next_to(header, DOWN, buff=0.5)

        bottom_label = fit(T("A REAL ADDED COST", color=PALETTE["crimson"], font_size=21, weight="BOLD"))
        bottom_body = VGroup(*[
            fit(T(l, color=cream, font_size=18), 3.4) for l in
            ["~400 extra requests/run —", "sequential, by design,", "not parallelized"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        bottom_block = VGroup(bottom_label, bottom_body).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        bottom_block.next_to(top_block, DOWN, buff=0.6)

        divider_y = (top_block.get_bottom()[1] + bottom_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.6, RIGHT * 1.6, color=cream, stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(top_block, divider_y, side="top", margin=0.3)
        clear_of_hdivider(bottom_block, divider_y, side="bottom", margin=0.3)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(top_block, shift=DOWN * 0.1),
            FadeIn(bottom_block, shift=UP * 0.1),
            run_time=0.8,
        )

        # box sized FROM the text's real rendered bounds — see B04's
        # caveat_box fix note (a fixed-height panel() clipped multi-line
        # text there; never hardcode a box size against wrapped text).
        log_text = fit(T(
            "Google News links seen: N,\nunwrapped: M, fell back: N-M",
            color=PALETTE["gold"], font_size=15, font=MONO, line_spacing=1.15,
        ), 3.2)
        log_box = panel(log_text.width + 0.35, log_text.height + 0.3,
                         fill=PALETTE["ink"], stroke=PALETTE["gold"], opacity=1.0)
        log_box.move_to(log_text.get_center())
        log_group = VGroup(log_box, log_text)
        log_group.next_to(bottom_block, DOWN, buff=0.55)
        self.play(FadeIn(log_group, shift=UP * 0.1), run_time=0.6)

        underline = Line(color=PALETTE["sage"], stroke_width=1)
        underline.put_start_and_end_on(
            log_group.get_corner(DL) + DOWN * 0.15, log_group.get_corner(DR) + DOWN * 0.15
        )
        self.play(Create(underline), run_time=0.3)

        # animation sum = 0.5+0.3+0.8+0.6+0.3 = 2.5s; measured narration = 24.58s
        self.wait(22.08)


# --------------------------------------------------------------------------- #
# B08 — TAKEAWAY: statement card. Already a single vertical column — bigger
# type, re-wrapped for the narrow column.
# --------------------------------------------------------------------------- #
class B08_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = fit(T(
            "A fix that\nworks today",
            color=PALETTE["ink"], font_size=52, line_spacing=1.05,
        ))
        line2 = fit(T(
            "isn't finished.",
            color=PALETTE["crimson"], font_size=48,
        ))
        line3 = fit(T(
            "Ask what happens the\nday it stops — and\nmake sure you'll notice.",
            color=PALETTE["slate"], font_size=26, line_spacing=1.1,
        ))
        VGroup(line1, line2, line3).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.6)
        # animation sum = 3.2s; measured narration = 7.87s
        self.wait(4.67)


# --------------------------------------------------------------------------- #
# B09 — SIGN-OFF: @HumanitariansAI, fixed with Claude Code, in for Sai
# Pranavi J.. Already a single vertical column.
# --------------------------------------------------------------------------- #
class B09_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=46))
        accent = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        tagline1 = fit(T(
            "fixed with Claude Code", color=PALETTE["ink"], font_size=28, weight="BOLD",
        ))
        tagline2 = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=24, line_spacing=1.1,
        ))
        tagline = VGroup(tagline1, tagline2).arrange(DOWN, buff=0.22)
        VGroup(handle, accent, tagline).arrange(DOWN, buff=1.7).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        # animation sum = 1.8s; measured narration = 5.78s
        self.wait(3.98)
