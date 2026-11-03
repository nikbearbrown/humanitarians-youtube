"""
Manim scenes for 2026-09-14-b3-the-link-that-pointed-nowhere

v1 (2026-09-17): first build under the toolkit's NEW submission spec
(brutalist/docs/FELLOWS-SUBMISSION.md, effective 2026-09-07). 10 beats, all
self-contained Manim (no pantry stills, no Remotion) — same house pattern as
this fellow's prior reels in the "Layer 1 hardening" series. Closest sibling:
2026-09-07-the-synonyms-the-classifier-never-learned/scenes.py (same fellow,
same voice, same genre) — PALETTE/MONO/fit()/panel()/clear_of_divider()/
box_around() copied verbatim from there for house-style consistency.

B00_TitleCard            — silent title card: video title + @HumanitariansAI (TITLE)
B01_ExecSummary          — spoken personal-intro card: name + one-line summary (EXEC-SUMMARY)
B02_DeadEndLinkHook      — feed item card, link click bouncing back to Google News, not an article (HOOK)
B03_RegexVsRealLink      — the failing url=([^&]+) regex next to a real modern link with no url= param (SETUP)
B04_ResolutionFlowDiagram — redirect page -> id/timestamp/signature -> POST -> real URL, with a required legible caveat label (DISCOVERY)
B05_OrderingNearMiss     — two call-order diagrams side by side: broken-if-shipped vs. fixed (NEAR-MISS)
B06_ThreeRoundProof      — all 3 verification rounds (20/20, 16/16, 6/6) + the final round's real resolved URLs (PROOF)
B07_HonestLimits         — both honest limitations at full weight + the visibility log line (HONEST-LIMITS)
B08_Statement            — takeaway card (TAKEAWAY)
B09_BrandOutro           — @HumanitariansAI sign-off (SIGN-OFF)

Every quoted string on screen (B03's regex/link, B04's flow + caveat, B05's
call orders, B06's round counts and 6 resolved domains, B07's two
limitations and the log-line format) is verbatim from
/Users/pranavijs/mycroft/scripts/regulatory-intel/B3-VERIFICATION.md — see
SOURCES.md's claim -> source mapping. Nothing paraphrased.

B04's caveat label ("reverse-engineered — not a documented/official API") is
a FACTCHECK-required element (FACTCHECK.md item #1, resolved) — sized and
placed to be clearly legible, not a tiny afterthought.

B05 and B07 are this reel's side-by-side beats. Both use clear_of_divider(),
ported verbatim from the sibling reel's own helper (itself ported from
2026-08-17-why-ai-generated-code-still-needs-a-human/scenes.py, which hit and
fixed a real divider-crosses-glyph bug), and verified by measuring real Manim
object bounds (get_left()/get_right()) against the divider before calling
each beat done.

B06 shows all 3 rounds (20/20, 16/16, 6/6), not just the strongest — a
FACTCHECK-required element (SOURCES.md row 4). B07's two limitations are kept
at full weight, side by side, neither minimized — FACTCHECK.md's explicit
resolution for this beat.

TIMING NOTE (audio-first rule): self.play()/self.wait() values below are
tuned to each beat's *measured* Kokoro audio duration (beat_sheet.json ->
actual_duration_s):
  B00 4.05s (silent)  B01 17.18s  B02 10.78s  B03 18.82s  B04 19.73s
  B05 28.66s  B06 23.54s  B07 24.58s  B08 7.87s  B09 5.78s
Each construct() below documents its own animation-time sum and the
resulting self.wait() so the beat lands on its measured length without the
compiler needing to slow-fit or freeze-pad into real content.
"""

from manim import *

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


def fit(mob, max_w):
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


def panel(width, height, fill=None, stroke=None, corner_radius=0.12, opacity=1.0):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        fill_color=fill or PALETTE["ink"], fill_opacity=opacity,
        stroke_color=stroke or PALETTE["slate"], stroke_width=2,
    )


def clear_of_divider(block, divider_x, side, margin=0.35):
    """Shift `block` so it keeps real clearance from a vertical divider at
    x=divider_x, measured from the block's OWN rendered bounds. Ported
    verbatim from the sibling reel's scenes.py.
    """
    if side == "left":
        overhang = block.get_right()[0] - (divider_x - margin)
        if overhang > 0:
            block.shift(LEFT * overhang)
    else:
        overhang = (divider_x + margin) - block.get_left()[0]
        if overhang > 0:
            block.shift(RIGHT * overhang)
    return block


def box_around(mob, color, buff=0.12):
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color, stroke_width=3, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# Title (30 chars) splits into 2 lines. Audio: mp3/beat-B00.mp3 is a REAL
# silent mp3 (ffmpeg anullsrc, 4.05s measured), never audio_file: null.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T(
            "The Link That", color=PALETTE["ink"], font_size=84, weight="BOLD",
        ), 12.0)
        title_line2 = fit(T(
            "Pointed Nowhere", color=PALETTE["ink"], font_size=84, weight="BOLD",
        ), 12.0)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 4.2, RIGHT * 4.2, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 4.2, RIGHT * 4.2, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=52)

        # buff 0.95->1.35: GATE V measured 0.95 at 49% canvas-fill (a 2-line
        # title has less inherent height than the sibling reel's 3-line
        # title, which needed 1.5 to clear the 55% floor) — see the sibling
        # reel's own B00_TitleCard comment for the underlying law (grow the
        # gaps between rule/title/handle groups until both axes clear it).
        # 1.8 overshot GATE B's safe-area bottom edge (measured handle bottom
        # at y=-3.94 vs the -3.4 floor); 1.35 clears the fill floor with
        # margin to spare (~60% projected) while staying inside safe area.
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.35
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # animation sum = 1.65s; measured silent track = 4.05s
        self.wait(2.40)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card, name + role + 3-line
# plain-language summary matching the narration's own second sentence.
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(T(
            "Sai Pranavi J.", color=PALETTE["ink"], font_size=56, weight="BOLD",
        ), 11.0)
        role = T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=26)
        accent = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)

        summary_l1 = fit(T(
            "Every stored Google News link",
            color=PALETTE["ink"], font_size=30,
        ), 11.5)
        summary_l2 = fit(T(
            "was a dead-end redirect — the fix had to",
            color=PALETTE["ink"], font_size=30,
        ), 11.5)
        summary_l3 = fit(T(
            "reverse-engineer how Google News resolves it.",
            color=PALETTE["ink"], font_size=30,
        ), 11.5)
        summary = VGroup(summary_l1, summary_l2, summary_l3).arrange(DOWN, buff=0.18)

        VGroup(name, role, accent, summary).arrange(DOWN, buff=1.4).move_to(ORIGIN)
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
# B02 — HOOK: a feed item card with a stored link; a click animation lands
# back on a Google News icon instead of an article. Generic feed visual, no
# real product named (per shot.note).
# --------------------------------------------------------------------------- #
class B02_DeadEndLinkHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(T(
            "A feed item, and its stored link", color=PALETTE["slate"],
            font_size=30, weight="BOLD",
        ), 12.0)
        header.to_edge(UP, buff=0.6)
        self.play(Write(header), run_time=0.5)

        card = panel(7.5, 1.9, fill=PALETTE["bg"], stroke=PALETTE["slate"], opacity=1.0)
        card_title = fit(T(
            "FINRA Enforcement Update — Google News", color=ink, font_size=22, weight="BOLD",
        ), 6.9)
        card_link = fit(T(
            "link: news.google.com/rss/articles/CBMi...", color=PALETTE["teal"],
            font_size=19, font=MONO,
        ), 6.9)
        card_body = VGroup(card_title, card_link).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        card_body.move_to(card.get_center())
        feed_card = VGroup(card, card_body)
        # buffs widened (0.55/1.15/0.2/0.35 -> 0.75/1.55/0.25/0.45): GATE V
        # measured the tight-stack draft at 49% canvas-fill. A first, more
        # aggressive widening (0.85/1.85/0.45/0.65) pushed the caption to
        # y=-4.09 — off-frame (GATE B off-frame ERROR) — so this is a
        # smaller, safe-margin-checked increase.
        feed_card.next_to(header, DOWN, buff=0.75)
        self.play(FadeIn(feed_card, shift=UP * 0.1), run_time=0.6)

        click_arrow = Arrow(
            start=feed_card.get_bottom() + DOWN * 0.15,
            end=feed_card.get_bottom() + DOWN * 1.55,
            color=PALETTE["gold"], stroke_width=5, buff=0,
        )
        click_label = T("click", color=PALETTE["gold"], font_size=20, weight="BOLD")
        click_label.next_to(click_arrow, RIGHT, buff=0.25)
        self.play(Create(click_arrow), Write(click_label), run_time=0.5)

        outcome = panel(5.6, 1.15, fill=PALETTE["ink"], stroke=PALETTE["crimson"], opacity=1.0)
        outcome_text = fit(T(
            "back to Google News — not the article", color=PALETTE["bg"],
            font_size=22, weight="BOLD",
        ), 5.1)
        outcome_group = VGroup(outcome, outcome_text)
        outcome_group.next_to(click_arrow, DOWN, buff=0.25)
        self.play(FadeIn(outcome_group, shift=UP * 0.1), run_time=0.6)

        caption = fit(T(
            "the link was never real to begin with",
            color=PALETTE["crimson"], font_size=22,
        ), 11.0)
        caption.next_to(outcome_group, DOWN, buff=0.45)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.6+0.5+0.6+0.5+0.3 = 3.0s; measured narration = 10.78s
        self.wait(7.78)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the failing regex verbatim next to a real modern Google News
# link, the missing url= param highlighted as absent. Both shown together —
# the mismatch is the point. [Source: B3-VERIFICATION.md "The bug"]
# --------------------------------------------------------------------------- #
class B03_RegexVsRealLink(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(T(
            "The fix looked for a parameter that's gone", color=cream,
            font_size=30, weight="BOLD",
        ), 12.5)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        regex_label = T("THE OLD FIX", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        regex_code = fit(T(
            "link.match(/url=([^&]+)/)", color=cream, font_size=30, font=MONO,
        ), 11.0)
        regex_block = VGroup(regex_label, regex_code).arrange(DOWN, buff=0.22)
        # buffs widened (0.5/0.15-1.0/0.35/0.3 -> 0.8/0.3-1.7/0.65/0.6): GATE V
        # measured the tight-stack draft at only 45% canvas-fill, the worst
        # underfill in this reel — content confined to the top half, a large
        # empty panel below (same defect class the sibling reel's B00 comment
        # documents; the fix is the same, grow the vertical gaps).
        regex_block.next_to(header, DOWN, buff=0.8)
        self.play(FadeIn(regex_block, shift=UP * 0.1), run_time=0.6)

        down_arrow = Arrow(
            start=regex_block.get_bottom() + DOWN * 0.3,
            end=regex_block.get_bottom() + DOWN * 1.7,
            color=PALETTE["gold"], stroke_width=5, buff=0,
        )
        looking_for = T("looking for: url=", color=PALETTE["gold"], font_size=18, font=MONO)
        looking_for.next_to(down_arrow, RIGHT, buff=0.3)
        self.play(Create(down_arrow), Write(looking_for), run_time=0.4)

        link_label = T("A REAL MODERN LINK", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD")
        link_code = fit(T(
            "news.google.com/rss/articles/<opaque-id>?oc=5", color=cream,
            font_size=26, font=MONO,
        ), 11.5)
        link_block = VGroup(link_label, link_code).arrange(DOWN, buff=0.22)
        link_block.next_to(down_arrow, DOWN, buff=0.65)
        self.play(FadeIn(link_block, shift=UP * 0.1), run_time=0.6)

        missing_box = box_around(link_code, PALETTE["crimson"], buff=0.14)
        missing_label = fit(T(
            "no url= parameter anywhere in this link", color=PALETTE["crimson"],
            font_size=20, weight="BOLD",
        ), 11.0)
        missing_label.next_to(missing_box, DOWN, buff=0.6)
        self.play(Create(missing_box), Write(missing_label), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            missing_label.get_corner(DL) + DOWN * 0.12, missing_label.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.6+0.4+0.6+0.5+0.3 = 2.9s; measured narration = 18.82s
        self.wait(15.92)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: the real resolution flow — redirect page -> extract
# id/timestamp/signature -> POST to internal endpoint -> real URL — with a
# required, clearly legible on-screen caveat label. [Source: B3-VERIFICATION.md
# "Why it's not a simple regex/302 fix" and "The fix". Caveat added per
# FACTCHECK.md item #1 — resolved.]
# --------------------------------------------------------------------------- #
class B04_ResolutionFlowDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(T(
            "How the page itself gets the real URL", color=ink,
            font_size=30, weight="BOLD",
        ), 12.5)
        header.to_edge(UP, buff=0.65)
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
            box = panel(2.55, 1.3, fill=PALETTE["ink"], stroke=color, opacity=1.0)
            text = fit(T(label, color=PALETTE["bg"], font_size=19, font=MONO, weight="BOLD", line_spacing=1.05), 2.2)
            text.move_to(box.get_center())
            steps.add(VGroup(box, text))
        steps.arrange(RIGHT, buff=0.55)
        # buff widened 0.65->1.0: GATE V measured the tighter draft at 51%
        # canvas-fill (just under the 55% floor).
        steps.next_to(header, DOWN, buff=1.0)

        arrows = VGroup(*[
            Arrow(steps[i].get_right(), steps[i + 1].get_left(), color=PALETTE["gold"],
                  stroke_width=4, buff=0.08)
            for i in range(len(steps) - 1)
        ])

        self.play(LaggedStart(*[FadeIn(s, scale=0.9) for s in steps], lag_ratio=0.25), run_time=1.0)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.2), run_time=0.6)

        caveat_box = Rectangle(
            width=10.6, height=0.85, stroke_color=PALETTE["crimson"], stroke_width=3,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
        )
        caveat_text = fit(T(
            "reverse-engineered — not a documented/official API",
            color=PALETTE["crimson"], font_size=26, weight="BOLD",
        ), 10.0)
        caveat_text.move_to(caveat_box.get_center())
        caveat = VGroup(caveat_box, caveat_text)
        caveat.next_to(steps, DOWN, buff=1.3)
        self.play(FadeIn(caveat, shift=UP * 0.1), run_time=0.6)

        underline = Line(color=PALETTE["sage"], stroke_width=1)
        underline.put_start_and_end_on(
            caveat.get_corner(DL) + DOWN * 0.15, caveat.get_corner(DR) + DOWN * 0.15
        )
        self.play(Create(underline), run_time=0.3)

        # animation sum = 0.5+1.0+0.6+0.6+0.3 = 3.0s; measured narration = 19.73s
        self.wait(16.73)


# --------------------------------------------------------------------------- #
# B05 — NEAR-MISS: two call-order diagrams side by side — old (classify AFTER
# unwrap, now broken) vs. fixed (classify BEFORE unwrap). Uses
# clear_of_divider(), verified by measured bounds.
# [Source: B3-VERIFICATION.md "Critical ordering fix, caught before deploying"]
# --------------------------------------------------------------------------- #
class B05_OrderingNearMiss(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(T(
            "Two call orders — only one survives the fix", color=cream,
            font_size=28, weight="BOLD",
        ), 12.5)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        # LEFT — old order: extractRealUrl() THEN identifySource(). Harmless
        # before (regex never matched); breaks silently once unwrap works.
        left_label = T("OLD ORDER — BROKEN ONCE THE FIX SHIPS", color=PALETTE["crimson"],
                           font_size=17, font=MONO, weight="BOLD")
        left_label = fit(left_label, 5.6)
        left_steps = [
            "1. extractRealUrl(link)",
            "2. identifySource(link)",
            "-> link is now mayerbrown.com",
            "-> \"news.google.com\" != match",
            "-> FINRA -> Unknown Source",
        ]
        left_lines = VGroup(*[
            fit(T(l, color=cream, font_size=17, font=MONO), 5.6) for l in left_steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        left_block = VGroup(left_label, left_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        left_block.move_to([-3.4, -0.2, 0])

        # RIGHT — fixed order: identifySource() on the ORIGINAL link, THEN
        # extractRealUrl() only for the stored/displayed link.
        right_label = T("FIXED ORDER — CLASSIFY FIRST", color=PALETTE["teal"],
                            font_size=17, font=MONO, weight="BOLD")
        right_label = fit(right_label, 5.6)
        right_steps = [
            "1. identifySource(rawLink)",
            "2. extractRealUrl(link)",
            "-> classified while link is",
            "   still news.google.com",
            "-> FINRA Enforcement News",
        ]
        right_lines = VGroup(*[
            fit(T(l, color=cream, font_size=17, font=MONO), 5.6) for l in right_steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        right_block = VGroup(right_label, right_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        right_block.move_to([3.2, -0.2, 0])

        clear_of_divider(left_block, divider_x=0, side="left")
        clear_of_divider(right_block, divider_x=0, side="right")

        blocks_top = max(left_block.get_top()[1], right_block.get_top()[1]) + 0.3
        blocks_bottom = min(left_block.get_bottom()[1], right_block.get_bottom()[1]) - 0.3
        divider = Line([0, blocks_top, 0], [0, blocks_bottom, 0], color=cream, stroke_width=2)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(left_block, shift=RIGHT * 0.1),
            FadeIn(right_block, shift=LEFT * 0.1),
            run_time=0.8,
        )

        caption = fit(T(
            "caught before it ever shipped — by classifying on the original link first",
            color=PALETTE["sage"], font_size=22,
        ), 12.5)
        caption.next_to(VGroup(left_block, right_block), DOWN, buff=0.5)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.3+0.8+0.6+0.3 = 2.5s; measured narration = 28.66s
        self.wait(26.16)


# --------------------------------------------------------------------------- #
# B06 — PROOF: all 3 escalating verification rounds (20/20, 16/16, 6/6), plus
# the final round's real resolved URLs. All 3 rounds visible, not just the
# best. [Source: B3-VERIFICATION.md "Live verification"]
# --------------------------------------------------------------------------- #
class B06_ThreeRoundProof(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(T(
            "Three rounds, each closer to the real system", color=ink,
            font_size=28, weight="BOLD",
        ), 12.5)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        rounds_data = [
            ("ROUND 1 — script prototype", "20 / 20", PALETTE["teal"]),
            ("ROUND 2 — exact code, ported", "16 / 16", PALETTE["teal"]),
            ("ROUND 3 — real node, live run", "6 / 6", PALETTE["crimson"]),
        ]
        round_cards = VGroup()
        for label, score, color in rounds_data:
            label_t = fit(T(label, color=ink, font_size=20, font=MONO, weight="BOLD"), 6.0)
            score_t = T(score, color=color, font_size=30, font=MONO, weight="BOLD")
            row = VGroup(label_t, score_t).arrange(RIGHT, buff=0.9)
            round_cards.add(row)
        # buffs widened (0.32/0.5 -> 0.46/1.15): GATE V measured the tighter
        # draft at only 39% canvas-fill, the worst underfill in this reel;
        # the first widening pass (0.42/1.0) landed at 54% — one point under
        # the 55% floor — so this is a small additional nudge.
        round_cards.arrange(DOWN, buff=0.46, aligned_edge=LEFT)
        round_cards.next_to(header, DOWN, buff=1.15)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in round_cards], lag_ratio=0.25), run_time=1.0)

        round3_box = box_around(round_cards[2], PALETTE["crimson"], buff=0.14)
        self.play(Create(round3_box), run_time=0.4)

        url_header = fit(T(
            "round 3's 6 real resolved URLs:", color=PALETTE["slate"], font_size=18, font=MONO,
        ), 11.5)
        urls = [
            "mcguirewoods.com", "freshfields.com", "mayerbrown.com",
            "jdsupra.com", "morganlewis.com", "ai-cio.com",
        ]
        url_row1 = VGroup(*[
            fit(T(u, color=ink, font_size=17, font=MONO), 3.2) for u in urls[:3]
        ]).arrange(RIGHT, buff=0.5)
        url_row2 = VGroup(*[
            fit(T(u, color=ink, font_size=17, font=MONO), 3.2) for u in urls[3:]
        ]).arrange(RIGHT, buff=0.5)
        url_block = VGroup(url_header, url_row1, url_row2).arrange(DOWN, buff=0.3)
        url_block.next_to(round_cards, DOWN, buff=1.1)
        self.play(FadeIn(url_block, shift=UP * 0.1), run_time=0.8)

        caption = fit(T(
            "all 6 still correctly labeled FINRA Enforcement News",
            color=PALETTE["teal"], font_size=20, weight="BOLD",
        ), 12.5)
        caption.next_to(url_block, DOWN, buff=0.75)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+1.0+0.4+0.8+0.5+0.3 = 3.5s; measured narration = 23.54s
        self.wait(20.04)


# --------------------------------------------------------------------------- #
# B07 — HONEST LIMITS: both limitation cards at full weight, side by side,
# plus the visibility log line. Neither limitation minimized or omitted —
# FACTCHECK.md's explicit resolution for this beat. Uses clear_of_divider().
# [Source: B3-VERIFICATION.md "Visibility, not silent degradation" and
# "What's NOT verified"]
# --------------------------------------------------------------------------- #
class B07_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(T(
            "Two things I'm not claiming", color=cream,
            font_size=30, weight="BOLD",
        ), 12.5)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        left_label = T("NOT YET VERIFIED", color=PALETTE["crimson"], font_size=22, weight="BOLD")
        left_body = VGroup(*[
            fit(T(l, color=cream, font_size=20), 5.6) for l in
            ["on the fellow's actual", "live n8n instance —", "only on the workflow file"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        left_block = VGroup(left_label, left_body).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        left_block.move_to([-3.3, 0.1, 0])

        right_label = T("A REAL ADDED COST", color=PALETTE["crimson"], font_size=22, weight="BOLD")
        right_body = VGroup(*[
            fit(T(l, color=cream, font_size=20), 5.6) for l in
            ["~400 extra requests/run —", "sequential, by design,", "not parallelized"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        right_block = VGroup(right_label, right_body).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        right_block.move_to([3.3, 0.1, 0])

        clear_of_divider(left_block, divider_x=0, side="left")
        clear_of_divider(right_block, divider_x=0, side="right")

        blocks_top = max(left_block.get_top()[1], right_block.get_top()[1]) + 0.3
        blocks_bottom = min(left_block.get_bottom()[1], right_block.get_bottom()[1]) - 0.3
        divider = Line([0, blocks_top, 0], [0, blocks_bottom, 0], color=cream, stroke_width=2)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(left_block, shift=RIGHT * 0.1),
            FadeIn(right_block, shift=LEFT * 0.1),
            run_time=0.8,
        )

        log_box = panel(10.4, 0.85, fill=PALETTE["ink"], stroke=PALETTE["gold"], opacity=1.0)
        log_text = fit(T(
            "Google News links seen: N, unwrapped: M, fell back: N-M",
            color=PALETTE["gold"], font_size=20, font=MONO,
        ), 9.8)
        log_text.move_to(log_box.get_center())
        log_group = VGroup(log_box, log_text)
        log_group.next_to(VGroup(left_block, right_block), DOWN, buff=0.55)
        self.play(FadeIn(log_group, shift=UP * 0.1), run_time=0.6)

        underline = Line(color=PALETTE["sage"], stroke_width=1)
        underline.put_start_and_end_on(
            log_group.get_corner(DL) + DOWN * 0.15, log_group.get_corner(DR) + DOWN * 0.15
        )
        self.play(Create(underline), run_time=0.3)

        # animation sum = 0.5+0.3+0.8+0.6+0.3 = 2.5s; measured narration = 24.58s
        self.wait(22.08)


# --------------------------------------------------------------------------- #
# B08 — TAKEAWAY: statement card.
# --------------------------------------------------------------------------- #
class B08_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = fit(T(
            "A fix that works today",
            color=PALETTE["ink"], font_size=58,
        ), 11.9)
        line2 = fit(T(
            "isn't finished.",
            color=PALETTE["crimson"], font_size=62,
        ), 11.9)
        line3 = fit(T(
            "Ask what happens the day it stops — and make sure you'll notice.",
            color=PALETTE["slate"], font_size=34,
        ), 11.8)
        VGroup(line1, line2, line3).arrange(DOWN, buff=1.8).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.6)
        # animation sum = 3.2s; measured narration = 7.87s
        self.wait(4.67)


# --------------------------------------------------------------------------- #
# B09 — SIGN-OFF: @HumanitariansAI, fixed with Claude Code, in for Sai
# Pranavi J..
# --------------------------------------------------------------------------- #
class B09_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=80)
        accent = Line(LEFT * 3.0, RIGHT * 3.0, color=PALETTE["gold"], stroke_width=3)
        tagline1 = fit(T(
            "fixed with Claude Code", color=PALETTE["ink"], font_size=40, weight="BOLD",
        ), 9.5)
        tagline2 = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=32,
        ), 9.5)
        tagline = VGroup(tagline1, tagline2).arrange(DOWN, buff=0.22)
        # buff 1.5->2.3: matches the proven value from the sibling reel's own
        # B08_BrandOutro (same handle/accent/tagline structure), which GATE V
        # measured clean at 0 MAJOR. This draft's tighter buff measured 46%
        # canvas-fill.
        VGroup(handle, accent, tagline).arrange(DOWN, buff=2.3).move_to(ORIGIN)

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
