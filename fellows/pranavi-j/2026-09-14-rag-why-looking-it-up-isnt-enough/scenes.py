"""
Manim scenes for 2026-09-14-rag-why-looking-it-up-isnt-enough
"RAG: Why 'Looking It Up' Doesn't Guarantee It's True"

First video built under the toolkit's NEW submission spec (effective
2026-09-07): see brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md.
B00 is a declared-silent beat (audio_policy: "silence" in beat_sheet.json,
real silent mp3 generated via ffmpeg anullsrc) per the new build_safety.py
gate that hard-fails any undeclared silent required-audio beat.

B00_TitleCard                  — silent title card (TITLE)
B01_ExecSummary                — spoken personal-intro card (EXEC-SUMMARY)
B02_StaleDocHook                — chat Q&A + stale-dated doc + confident wrong answer (HOOK)
B03_ThreeQuestionsFramework     — rubric card, Relevant/Current/Grounded shown together (FRAMEWORK)
B04_StaleDocResolved            — retrieved doc + answer, both dates legible together (WORKED-EXAMPLE)
B05_RetrievalWorksFalsifiability— no-retrieval vs with-retrieval, fair labeled comparison (FALSIFIABILITY)
B06_AuditChecklist              — 3 questions restated as a checklist card, visually distinct from B03 (SCAFFOLDED-TASK)
B07_Statement                   — takeaway statement card (TAKEAWAY)
B08_BrandOutro                  — @HumanitariansAI sign-off (SIGN-OFF)

IMPORTANT (see FACTCHECK.md / SOURCES.md): the support-bot stale-policy
scenario (B02/B04) and the internal-product-launch scenario (B05) are both
GENERIC, illustrative, hypothetical examples. Neither names a real company,
product, vendor, or RAG system — do not add real names to this file.

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), panel(), clear_of_divider()) copied from this
fellow's closest sibling reel
(2026-08-17-why-ai-generated-code-still-needs-a-human/scenes.py) for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed, and this reel has no math.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule. Wait budgets within
each beat are split proportionally to the word count of the narration
segment they hold space for, so the visual pacing tracks what's actually
being said at that moment. B00 carries no narration (silent beat) so its
4.049s target is fixed, not measured from speech.
"""

from manim import *

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
                          # (cream): measures 7.67:1 there but a genuinely
                          # broken 1.56:1 on "ink" (verified via the same
                          # contrast math as runtime/qc/wcag_margin_check.py
                          # -- this exact bug, on this exact hex pair, was
                          # already found and documented in this fellow's
                          # 2026-08-17 sibling reel's short/scenes.py; fixed
                          # here proactively rather than waiting for a real
                          # frame extraction to catch it a second time).
    "teal_on_ink": "#5FB8CC",  # same hue family, lightened for ink
                          # backgrounds specifically (6.23:1 on "ink") --
                          # use this, never "teal", for teal text/strokes in
                          # any scene whose camera.background_color is ink,
                          # or any panel/box FILLED with "ink" on a cream
                          # scene (B04, B05 here).
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
    x=divider_x, measured from the block's OWN rendered bounds
    (get_left()/get_right()), not a guessed constant or a fit()-width cap
    that was never actually checked against the divider's position. Copied
    verbatim from the 2026-08-17 sibling reel, which found and fixed exactly
    this bug (a fit()-capped code block whose longest line still landed past
    a divider at x=0) via direct frame measurement, not static analysis.
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.049s — fixed target, not measured narration
# (narration_text is "" and audio_policy is "silence" in beat_sheet.json).
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T(
            "RAG: Why \"Looking It Up\"",
            color=PALETTE["ink"], font_size=48, weight="BOLD",
        ), 12.0)
        title_line2 = fit(T(
            "Doesn't Guarantee It's True",
            color=PALETTE["ink"], font_size=48, weight="BOLD",
        ), 12.0)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=38)

        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.0
        ).move_to(ORIGIN)

        # outer bordered frame — GATE V's canvas-fill law (>=55% of the safe
        # area) is measured on the tight bbox of ALL visible content; a
        # centered rule/title/handle stack alone only reaches ~41% (found via
        # direct GATE V run + real frame extraction on the first draft). A
        # generously-sized frame around the same content reliably clears the
        # floor without changing the card's actual information.
        frame = panel(width=11.6, height=6.6, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder is a clean static hold tuned to the
        # measured 4.049s silent-track length (ffprobe on mp3/beat-B00.mp3)
        self.wait(2.45)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 18.336s (2026-10-20 name-retrofit: "Sai Pranavi J.", was 18.744s)
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 3.4, RIGHT * 3.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 3.4, RIGHT * 3.4, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.55, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=30, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=42, weight="BOLD"), 9.0)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=22), 7.0)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_row = VGroup(badge_group, name_block).arrange(RIGHT, buff=0.4)

        summary_lines = [
            "This video: Retrieval-Augmented Generation —",
            "giving an AI model a search step so it can",
            "look things up instead of guessing — and 3",
            "questions that catch a grounded answer",
            "from one that just sounds like it is.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=25), 11.0) for l in summary_lines
        ]).arrange(DOWN, buff=0.18)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(
            DOWN, buff=0.6
        ).move_to(ORIGIN)

        # outer bordered frame — same canvas-fill fix as B00 (see that
        # class's comment): a centered rule/badge/summary stack alone
        # measured only ~40% coverage of the safe area under GATE V.
        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 18.336s Kokoro
        # length for B01 (2026-10-20 name-retrofit: 18.336 - 2.1 = 16.236)
        self.wait(16.24)


# --------------------------------------------------------------------------- #
# B02 — HOOK: chat-style Q&A, a retrieved document card stamped with an old
# date, a confident answer bubble — then the stale/wrong reveal.
# [GENERIC/HYPOTHETICAL SCENARIO — see FACTCHECK.md — no real product/vendor]
# measured audio: 17.304s
# --------------------------------------------------------------------------- #
class B02_StaleDocHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # ---- question bubble (top) ----
        question = fit(T(
            "\"What's our refund policy?\"", color=PALETTE["bg"], font_size=24
        ), 9.0)
        # low fill opacity (not 1.0): a solid slate/teal bubble fill sits too
        # close in luminance to the ink background (found via GATE V's
        # low-contrast check averaging ALL non-background ink, which a large
        # solid mid-tone fill area drags down even though the TEXT inside it
        # is high-contrast) — a subtle tint + bright stroke reads as a bubble
        # without dragging the average down.
        q_panel = panel(width=question.width + 0.7, height=question.height + 0.5,
                         fill=PALETTE["slate"], stroke=PALETTE["sage"], opacity=0.3)
        q_panel.move_to(question.get_center())
        question_bubble = VGroup(q_panel, question)
        # Vertical anchors below are spread across nearly the full safe
        # height (+3.0 to -2.8) rather than clustered in the upper half.
        # An earlier draft passed GATE V's automated canvas-fill check only
        # by wrapping an invisible bordering rectangle around the real
        # content — which cleared the METRIC but left a real, visible defect
        # on direct frame inspection (question+doc+answer bunched in the top
        # ~55% of the frame, a dead empty band below). Real fix: move the
        # actual content, not the measurement trick.
        question_bubble.move_to([0, 3.15, 0])

        # ---- retrieved document card (middle) ----
        doc_header = fit(T(
            "RETRIEVED: Policy #114 — Refund Window", color=PALETTE["sage"], font_size=20, font=MONO
        ), 11.0)
        doc_stamp = fit(T(
            "Last updated: Jan 12, 2026", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD"
        ), 8.5)
        doc_body = fit(T(
            "\"Refunds accepted within 30 days of purchase.\"", color=PALETTE["bg"], font_size=18
        ), 10.5)
        doc_col = VGroup(doc_header, doc_stamp, doc_body).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        # padding bumped 0.8 -> 1.6: the T() text-rendering fix (geometric
        # scale-down from a clean font_size=48 base) removed a Pango/Cairo
        # hinting artifact that used to insert extra visual gaps INSIDE this
        # card's small-font-size words — those spurious gaps had been quietly
        # widening this panel just enough to clear GATE V's canvas-fill floor
        # (55%). With the bug fixed the panel is now its true (narrower)
        # width, and a direct re-render measured B02 at 8.5s (mid-beat, before
        # the STALE/WRONG tags reveal) at 53% — a real, reproducible MAJOR
        # underfill, not a false positive (see BUILD-LOG.md). Fixed the same
        # way this file's own B00 already established: a bit more real
        # padding around the same real content, not a bigger invisible frame.
        doc_card_bg = panel(width=doc_col.width + 1.6, height=doc_col.height + 0.6,
                             fill=PALETTE["ink"], stroke=PALETTE["sage"])
        doc_card_bg.move_to(doc_col.get_center())
        doc_card = VGroup(doc_card_bg, doc_col)
        doc_card.move_to([0, 0.8, 0])

        # ---- confident answer bubble (bottom) ----
        answer = fit(T(
            "\"Per Policy #114, refunds are available within 30 days.\"",
            color=PALETTE["bg"], font_size=22
        ), 11.0)
        a_panel = panel(width=answer.width + 1.5, height=answer.height + 0.5,
                         fill=PALETTE["teal"], stroke=PALETTE["sage"], opacity=0.3)
        a_panel.move_to(answer.get_center())
        answer_bubble = VGroup(a_panel, answer)
        answer_bubble.move_to([0, -2.55, 0])

        self.play(FadeIn(question_bubble, shift=DOWN * 0.15), run_time=0.4)
        self.wait(3.93)
        self.play(FadeIn(doc_card, shift=UP * 0.1), run_time=0.5)
        self.wait(1.72)
        self.play(FadeIn(answer_bubble, shift=UP * 0.1), run_time=0.5)
        self.wait(2.07)

        # reveal: the answer is wrong because the source is stale.
        # Centered below their targets (not next_to(..., RIGHT), which — for
        # a wide doc card/answer bubble centered at x=0 — pushed the tag's
        # own width off the right edge of the frame; caught by GATE B's
        # post-render layout audit on the real rendered bounds, not fit()'s
        # width cap alone). stale_tag sits in the gap between the doc card
        # and the (now lower) answer bubble; wrong_group sits just under the
        # answer bubble, both safely inside the y in [-3.4, 3.4] margin.
        stale_tag = fit(T("STALE — replaced 8 months ago", color=PALETTE["crimson"],
                              font_size=18, font=MONO, weight="BOLD"), 7.5)
        stale_tag.move_to([0, -0.75, 0])
        wrong_tag = fit(T("WRONG", color=PALETTE["crimson"], font_size=22, font=MONO, weight="BOLD"), 3.0)
        wrong_box = Rectangle(width=wrong_tag.width + 0.3, height=wrong_tag.height + 0.2,
                               stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        wrong_box.move_to(wrong_tag.get_center())
        wrong_group = VGroup(wrong_box, wrong_tag)
        wrong_group.move_to([0, -3.2, 0])

        self.play(FadeIn(stale_tag, shift=LEFT * 0.1), FadeIn(wrong_group, scale=1.2), run_time=0.4)
        # everything legible together well before end; clean static hold
        self.wait(7.58)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: the 3-question rubric (Relevant / Current / Grounded),
# shown in full BEFORE any example — framework-first.
# measured audio: 26.352s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T(
            "The 3 Questions Behind Every RAG Answer", color=PALETTE["ink"], font_size=42
        ), 11.8)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)

        intro = fit(T(
            "Here's the check, before any example.", color=PALETTE["slate"], font_size=22
        ), 10.5)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro, shift=UP * 0.1), run_time=0.4)
        self.wait(4.38)
        self.play(FadeOut(intro, shift=UP * 0.1), run_time=0.3)

        rows_data = [
            ("1", "RELEVANT", "Does the retrieved document actually address\nthis question — or just share some keywords with it?"),
            ("2", "CURRENT", "Is this the newest version — or a stale\ncopy the index never updated?"),
            ("3", "GROUNDED", "Is the answer actually built from what was\nretrieved — or did the model fall back on\nwhat it already \"knew\" and cite the document anyway?"),
        ]

        rows = VGroup()
        for num, label, desc in rows_data:
            badge = Circle(radius=0.42, color=PALETTE["teal"], fill_color=PALETTE["teal"], fill_opacity=0.15, stroke_width=2.5)
            badge_num = T(num, color=PALETTE["teal"], font_size=28, font=MONO).move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)

            label_txt = fit(T(label, color=PALETTE["slate"], font_size=26, font=MONO), 4.8)
            desc_txt = fit(T(desc, color=PALETTE["ink"], font_size=20, line_spacing=1.0), 9.8)

            text_col = VGroup(label_txt, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
            row = VGroup(badge_group, text_col).arrange(RIGHT, buff=0.5)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.75)
        if rows.width > 12.0:
            rows.scale_to_fit_width(12.0)
        if rows.height > 4.7:
            rows.scale_to_fit_height(4.7)
        rows.move_to(ORIGIN).shift(UP * 0.05)

        # SKELETON FIRST: all 3 badges + labels land before any one question
        # is explained — the full rubric's shape is on screen up front
        # (framework-first requirement), matching the sibling reel's pattern.
        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.15)

        # holds tuned to the measured 26.352s Kokoro audio, split proportional
        # to each question's word count (17/15/28 of 60 spoken words across
        # relevant/current/grounded) — see BUILD-LOG.md.
        row_holds = [4.96, 4.38, 8.18]
        for row, hold in zip(rows, row_holds):
            desc_txt = row[1][1]
            self.play(FadeIn(desc_txt, shift=UP * 0.1), run_time=0.3)
            self.wait(hold)

        not_two = fit(T(
            "not one, not two — all three.", color=PALETTE["crimson"], font_size=24
        ), 8.5)
        not_two.to_edge(DOWN, buff=0.6)
        self.play(Write(not_two), run_time=0.5)
        self.wait(1.40)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: the retrieved (stale-dated) document AND the model's
# confident answer shown together — both the document's date and the current
# date legible at once. Side-by-side layout: uses clear_of_divider() to
# guarantee real clearance from the vertical divider, same discipline as the
# sibling reel's v3.1 fix (never trust a fit()-width cap alone).
# [GENERIC/HYPOTHETICAL SCENARIO — see FACTCHECK.md]
# measured audio: 17.136s
# --------------------------------------------------------------------------- #
class B04_StaleDocResolved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        today_banner = fit(T(
            "TODAY: September 14, 2026", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD"
        ), 9.0)
        today_banner.move_to([0, 3.1, 0])

        # ---- LEFT: the retrieved document, in a real bordered panel ----
        # An earlier draft used plain text columns (no panel) plus a thin
        # divider line — GATE V's automated canvas-fill check passed only
        # after wrapping an INVISIBLE oversized rectangle around everything,
        # which real frame extraction then showed as the exact defect this
        # build's process warns about: two small text blocks clustered in
        # the upper half of the frame, a big dead band below down to a
        # single status line at the very bottom. Real fix: give each side a
        # correctly-sized bordered panel (matching B05's proven layout) so
        # the panel's own visible bounds and its content are proportionate
        # to each other, and space the banner/panels/status zone across the
        # full safe height instead of clustering near the top.
        left_header = fit(T("RETRIEVED DOCUMENT", color=PALETTE["sage"], font_size=19, font=MONO), 4.9)
        left_title = fit(T("Policy #114 —\nRefund Window", color=PALETTE["bg"], font_size=19, font=MONO, line_spacing=1.1), 4.9)
        left_stamp = fit(T("Last updated:\nJan 12, 2026", color=PALETTE["crimson"], font_size=19, font=MONO, weight="BOLD", line_spacing=1.1), 4.9)
        left_body = fit(T("\"Refunds accepted\nwithin 30 days\nof purchase.\"", color=PALETTE["bg"], font_size=17, line_spacing=1.1), 4.9)
        left_content = VGroup(left_header, left_title, left_stamp, left_body).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        left_panel = panel(width=5.6, height=4.4, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        left_panel.move_to([-3.3, -0.15, 0])
        left_content.move_to(left_panel.get_center())

        # ---- RIGHT: the model's confident answer, matching panel style ----
        right_header = fit(T("MODEL'S ANSWER", color=PALETTE["sage"], font_size=19, font=MONO), 4.9)
        right_quote = fit(T(
            "\"Per Policy #114,\nrefunds are available\nwithin 30 days.\"",
            color=PALETTE["bg"], font_size=18, line_spacing=1.2
        ), 4.9)
        right_content = VGroup(right_header, right_quote).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        right_panel = panel(width=5.6, height=4.4, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        right_panel.move_to([3.3, -0.15, 0])
        right_content.move_to(right_panel.get_center())

        self.play(FadeIn(today_banner), run_time=0.3)
        self.play(Create(left_panel), Create(right_panel), run_time=0.4)
        self.play(FadeIn(left_content, shift=UP * 0.1), FadeIn(right_content, shift=UP * 0.1), run_time=0.6)
        self.wait(1.54)

        # a highlighter box (built from the target's own bounds, not passed
        # the mobject itself) that tracks the rubric step onto the relevant
        # claim — same idiom as the sibling reel's box_around()/show_step().
        # This also gives GATE A's static pre-flight a real non-text shape
        # that actually changes state across the beat (a Line divider alone
        # never changes, which the checker correctly flags as "shapes never
        # change — repeated animation").
        def box_around(mob, buff=0.12):
            r = Rectangle(
                width=mob.width + 2 * buff, height=mob.height + 2 * buff,
                stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
            )
            r.move_to(mob.get_center())
            return r

        highlight = box_around(left_title)
        self.play(Create(highlight), run_time=0.3)

        # single status line that gets replaced as the rubric walks through
        # each question — keeps the two panels above stable and legible
        # throughout, avoids stacking a permanent 3rd row of chips below them
        status_zone = VGroup()

        def show_status(text, color, hold, focus):
            nonlocal status_zone
            new_status = fit(T(text, color=color, font_size=22, font=MONO, weight="BOLD"), 12.0)
            new_status.to_edge(DOWN, buff=0.6)
            new_highlight = box_around(focus)
            if len(status_zone) == 0:
                self.play(FadeIn(new_status, shift=UP * 0.1), Transform(highlight, new_highlight), run_time=0.3)
            else:
                self.play(FadeOut(status_zone), FadeIn(new_status, shift=UP * 0.1),
                          Transform(highlight, new_highlight), run_time=0.3)
            status_zone = new_status
            self.wait(hold)

        show_status("RELEVANT — yes, it's the right document", PALETTE["teal_on_ink"], 2.46, left_title)
        show_status("CURRENT — no, it's 8 months stale", PALETTE["crimson"], 2.15, left_stamp)
        show_status("GROUNDED — doesn't matter, the source is wrong", PALETTE["crimson"], 6.15, right_quote)

        self.play(FadeOut(status_zone), FadeOut(highlight), run_time=0.2)
        closing = fit(T(
            "Retrieval didn't fail here. Freshness did.", color=PALETTE["gold"], font_size=24
        ), 11.5)
        closing.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.3)
        self.wait(1.84)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: a fair, clearly-labeled comparison of a "no
# retrieval" attempt (invented, wrong) and a "with retrieval" attempt
# (correct, grounded) — same mechanism, different source quality, not a
# strawman. Uses two separated bordered panels with a visible gap (no
# divider line drawn through the frame), so there is no divider to cross;
# each panel's text is sized well under the panel's own interior width.
# [GENERIC/HYPOTHETICAL SCENARIO — see FACTCHECK.md]
# measured audio: 25.392s
# --------------------------------------------------------------------------- #
class B05_RetrievalWorksFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T(
            "Now retrieval is exactly the fix:", color=PALETTE["ink"], font_size=30
        ), 11.5)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(3.11)

        question = fit(T("\"What is Project Nighthawk?\"", color=PALETTE["slate"], font_size=20, font=MONO), 10.0)
        question.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(question), run_time=0.3)

        # Panel width/x reduced from the first draft (6.0 wide at x=+-3.7,
        # i.e. edges at +-6.7) after GATE V's frame-level QC caught a REAL
        # edge-bleed BLOCKER on the true candidate export — the panels'
        # outer edges landed past the ~+-6.4 safe-area half-width. Centers
        # moved closer + width trimmed so both edges land at +-6.0, safely
        # inside the safe margin, confirmed by re-running GATE V.
        # ---- LEFT panel: no retrieval ----
        left_panel = panel(width=5.4, height=4.2, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        left_panel.move_to([-3.3, -0.6, 0])
        left_label = fit(T("NO RETRIEVAL", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD"), 4.6)
        left_answer = fit(T(
            "\"Project Nighthawk is a cloud\nsecurity monitoring suite...\"",
            color=PALETTE["bg"], font_size=16, line_spacing=1.1
        ), 4.6)
        left_tag = fit(T("INVENTED", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD"), 3.2)
        left_content = VGroup(left_label, left_answer, left_tag).arrange(DOWN, buff=0.35)
        left_content.move_to(left_panel.get_center())

        # ---- RIGHT panel: with retrieval ----
        right_panel = panel(width=5.4, height=4.2, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        right_panel.move_to([3.3, -0.6, 0])
        right_label = fit(T("WITH RETRIEVAL", color=PALETTE["teal_on_ink"], font_size=20, font=MONO, weight="BOLD"), 4.6)
        right_source = fit(T(
            "Launch doc: internal analytics\ndashboard, launched Sep 8, 2026",
            color=PALETTE["sage"], font_size=15, line_spacing=1.1
        ), 4.6)
        right_answer = fit(T(
            "\"...an internal analytics\ndashboard, launched last week.\"",
            color=PALETTE["bg"], font_size=16, line_spacing=1.1
        ), 4.6)
        right_tag = fit(T("GROUNDED", color=PALETTE["teal_on_ink"], font_size=17, font=MONO, weight="BOLD"), 3.2)
        right_content = VGroup(right_label, right_source, right_answer, right_tag).arrange(DOWN, buff=0.28)
        right_content.move_to(right_panel.get_center())

        # both panel frames + labels land together — a fair comparison is
        # visible as a shape before either side's detail fills in
        self.play(
            Create(left_panel), Create(right_panel),
            FadeIn(left_label), FadeIn(right_label),
            run_time=0.6,
        )

        # verdict-marker boxes (real Shape objects, not text) drawn around
        # each side's tag as it lands — also gives GATE A's static pre-flight
        # a shape-state that actually changes over time (two static bordered
        # panels alone never change signature once created, which the
        # checker correctly flags as "shapes never change").
        left_marker = Rectangle(
            width=left_tag.width + 0.3, height=left_tag.height + 0.2,
            stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0,
        )
        right_marker = Rectangle(
            width=right_tag.width + 0.3, height=right_tag.height + 0.2,
            stroke_color=PALETTE["teal_on_ink"], stroke_width=3, fill_opacity=0,
        )

        self.play(FadeIn(VGroup(left_answer, left_tag), shift=UP * 0.1), run_time=0.4)
        left_marker.move_to(left_tag.get_center())
        self.play(Create(left_marker), run_time=0.2)
        self.wait(9.74)
        self.play(FadeIn(VGroup(right_source, right_answer, right_tag), shift=UP * 0.1), run_time=0.4)
        right_marker.move_to(right_tag.get_center())
        self.play(Create(right_marker), run_time=0.2)
        self.wait(5.71)

        same_mech = fit(T("Same mechanism.", color=PALETTE["slate"], font_size=20), 6.0)
        same_mech.next_to(VGroup(left_panel, right_panel), DOWN, buff=0.35)
        self.play(FadeIn(same_mech), run_time=0.2)
        self.wait(0.62)

        closing = fit(T(
            "Different source. Different outcome.", color=PALETTE["ink"], font_size=20
        ), 9.0)
        closing.next_to(same_mech, RIGHT, buff=0.3)
        self.play(FadeIn(closing, shift=UP * 0.05), run_time=0.3)
        self.wait(3.42)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: the 3 questions restated as an audit CHECKLIST card
# — visually distinct from B03's numbered rubric (literal checkbox squares,
# action framing, matching the sibling reel's B06_ScaffoldedTask idiom).
# measured audio: 18.864s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # An earlier draft held the title alone for ~4s before revealing the
        # checklist, then wrapped everything in an invisible oversized
        # frame to satisfy GATE V's automated canvas-fill check. Real frame
        # extraction showed exactly what that hid: a lone title sentence in
        # a big empty bordered box for the beat's first several seconds —
        # a real defect, not just a metric miss. Real fix: bring the
        # checklist's SKELETON (checkboxes + questions) on screen almost
        # immediately, matching this project's established framework-first
        # "skeleton first" idiom (see B03) — the full shape of the task is
        # visible right away; only each row's one-line explanation streams
        # in afterward, in step with the narration actually reaching it.
        title = fit(T(
            "Audit one RAG answer today:", color=PALETTE["ink"], font_size=28
        ), 10.5)
        title.to_edge(UP, buff=0.7)

        # Frame sized to this beat's own eventual full extent (title at the
        # top edge down to the zinger at the bottom edge, once everything
        # has landed) — not an arbitrary oversized box (that was the earlier
        # draft's mistake). Present from t=0 alongside the title, the same
        # legitimate "card boundary that fills in over time" pattern already
        # confirmed fine on direct frame inspection in B00/B01.
        frame = panel(width=12.0, height=7.0, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), Write(title), run_time=0.3)
        self.wait(0.9)

        steps_data = [
            (["Was the source actually relevant?"], "not just keyword overlap"),
            (["Was it actually current?"], "not a stale copy the index missed"),
            (["Can you point to the exact sentence", "the answer came from?"], "if you can't, you don't know it's grounded"),
        ]

        rows = VGroup()
        for main_lines, explain in steps_data:
            box = Square(side_length=0.32, color=PALETTE["slate"], stroke_width=2.5)
            main_txt = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=22, font=MONO), 11.2) for l in main_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            explain_txt = fit(T(explain, color=PALETTE["slate"], font_size=17), 11.0)
            text_col = VGroup(main_txt, explain_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            row = VGroup(box, text_col).arrange(RIGHT, buff=0.4, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        if rows.width > 12.0:
            rows.scale_to_fit_width(12.0)
        if rows.height > 4.2:
            rows.scale_to_fit_height(4.2)
        rows.move_to(ORIGIN).shift(UP * 0.1)

        # SKELETON FIRST: checkbox + question land one at a time, before any
        # explanation streams in — copyable checklist visible up front.
        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.2)

        # holds tuned to the measured 18.864s Kokoro audio, split proportional
        # to each row's word count (9/4/12 of the 3-question span).
        row_holds = [2.76, 1.23, 3.68]
        for row, hold in zip(rows, row_holds):
            explain_txt = row[1][1]
            self.play(FadeIn(explain_txt, shift=UP * 0.08), run_time=0.3)
            self.wait(hold)

        zinger = fit(T(
            "can't point to it? you're not grounded — you're hoping.",
            color=PALETTE["crimson"], font_size=20
        ), 11.0)
        zinger.to_edge(DOWN, buff=0.7)
        self.play(Write(zinger), run_time=0.5)
        self.wait(7.75)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 9.480s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # An earlier draft kept these lines at their original (smaller) font
        # sizes and wrapped an oversized INVISIBLE rectangle around them to
        # satisfy GATE V's automated canvas-fill check. Real frame
        # extraction showed the actual defect that hid: a short statement
        # adrift in a big empty bordered box. Real fix: make the statement
        # itself genuinely bigger (font sizes up, line spacing opened out),
        # then size the visible frame from the CONTENT's own measured
        # bounds plus a modest, proportionate margin — so the border always
        # hugs what's actually on screen instead of a fixed oversized box.
        # fit() caps kept a bit under the ~6.4 safe half-width (12.8 safe
        # width) — the first pass here (11.8 cap + a padded frame) actually
        # rendered wide enough to cross the safe edge, a real edge-bleed
        # BLOCKER caught by GATE V on the true candidate export, not just
        # the earlier low-fill warning.
        line1 = fit(T(
            "Giving a model a search step doesn't make it honest.",
            color=PALETTE["bg"], font_size=36
        ), 10.6)
        line2 = fit(T(
            "It makes it capable of being honest —", color=PALETTE["sage"], font_size=31
        ), 9.8)
        line3 = fit(T(
            "only if what it finds is actually right,\nand it actually uses it.",
            color=PALETTE["gold"], font_size=28, line_spacing=1.2
        ), 10.8)

        content = VGroup(line1, line2, line3).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        # frame padding clamped so it can never push past the ~+-6.4 safe
        # half-width regardless of how wide the longest line measures.
        frame_w = min(content.width + 1.4, 12.2)
        frame = panel(width=frame_w, height=content.height + 1.2,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)
        self.play(Create(frame), run_time=0.25)

        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.5)
        self.wait(2.36)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.09)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.4)
        # underline accent under the closing qualifier — a second real Shape
        # (not text) that appears partway through the beat, giving GATE A's
        # static pre-flight a genuine shape-state change (the outer frame
        # alone is static for the whole beat, which the checker correctly
        # flags as "shapes never change").
        underline = Line(
            line3.get_corner(DL) + DOWN * 0.15, line3.get_corner(DR) + DOWN * 0.15,
            color=PALETTE["gold"], stroke_width=2,
        )
        self.play(Create(underline), run_time=0.1)
        self.wait(3.39)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, in for Sai Pranavi J.
# measured audio: 1.512s — a very short beat; all elements land together.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # An earlier draft kept these 3 elements at their original (smaller)
        # sizes and wrapped an oversized INVISIBLE rectangle around them to
        # satisfy GATE V's automated canvas-fill check — real frame
        # extraction showed the actual defect: a small sign-off adrift in a
        # big empty bordered box. Real fix: make the card's own elements
        # genuinely bigger, then size the visible frame from the content's
        # own measured bounds plus a modest, proportionate margin.
        # v2: 9.6/9.2-wide fit caps still only measured 35% real canvas-fill
        # on the true candidate export (the crude pre-render size estimate
        # undershot actual Pango metrics) — pushed noticeably larger again
        # and re-verified against the real GATE V run, not just calculation.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=70), 10.8)
        accent = Line(LEFT * 3.0, RIGHT * 3.0, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=42
        ), 10.4)
        content = VGroup(handle, accent, tagline).arrange(DOWN, buff=1.85).move_to(ORIGIN)

        # frame padding clamped so it can never push past the safe margin.
        frame_w = min(content.width + 1.6, 12.2)
        frame_h = min(content.height + 0.9, 7.0)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        # single combined reveal — the beat is only 1.512s (an "Explained
        # with Claude Code" narration line), so there is no room for a
        # sibling-style multi-step build; everything lands as one clean beat
        # and the remainder is a static hold.
        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        self.wait(1.06)
