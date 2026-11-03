"""
Manim scenes for 2026-09-22-the-all-clear-that-wasnt-all-there
"The All-Clear That Wasn't All There"

First-ever pranavi-j-path project built fresh (not migrated) under the
toolkit's NEW submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per the new build_safety.py gate
that hard-fails any undeclared silent required-audio beat.

B00_TitleCard        — silent title card (TITLE)
B01_ExecSummary      — spoken personal-intro card (EXEC-SUMMARY)
B02_AllClearHook     — the shipped "All Clear!" email header/message (HOOK)
B03_FourCardGrid     — real shipped 4-card "Monitored Sources" grid (SETUP)
B04_FiveRealFeeds    — 4 shown vs 5 real feed nodes, missing 5th highlighted (DISCOVERY)
B05_BeforeAfterFix   — before(4)/after(5) grid, new card highlighted (FIX)
B06_StaleNoteClosed  — stale FINDINGS.md note, stamped ALREADY FIXED (ASIDE)
B07_Statement        — takeaway statement card (TAKEAWAY)
B08_BrandOutro       — @HumanitariansAI sign-off (SIGN-OFF)

EMOJI RENDERING NOTE (found this build, verified empirically before writing
a single beat): the source material's card labels are written with a
leading emoji glyph in B5-VERIFICATION.md (e.g. "\U0001F4F0 SEC Press
Releases"). A direct test — `Text("\U0001F4F0 SEC Press Releases", ...)`
rendered via this environment's Manim/Pango/Cairo pipeline — logs
"Unsupported element type: <class 'svgelements.svgelements.Image'>" and the
emoji glyph is silently DROPPED (renders as blank space, not a tofu box, not
a crash). Real color-emoji glyphs are COLR/SVG-in-font content that this
text-to-SVG-path pipeline cannot rasterize. Rather than ship an invisible
glyph (a real legibility defect no automated gate would catch, since the
text that IS there still passes), every source-card badge here uses a
small drawn circle + short mono abbreviation (SEC / FED / FIN / CFTC / IAR)
in place of the emoji — the verbatim TEXT label (e.g. "SEC Press Releases")
is kept exactly as shipped; only the decorative emoji prefix is substituted
with a rendering-safe equivalent. See BUILD-LOG.md.

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), panel(), T()) copied from this fellow's
sibling reels (2026-09-14-rag-why-looking-it-up-isnt-enough/scenes.py and
2026-09-14-b3-the-link-that-pointed-nowhere/scenes.py) for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed, and this reel has no
math.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule. B00 carries no
narration (silent beat) so its 4.049s target is fixed, not measured from
speech. compile.py retimes silently within +/-5% of the audio length, so
exact-to-the-millisecond wait sums are not required, but every scene below
sums exactly to its beat's actual_duration_s regardless.

CANVAS-FILL NOTE: every beat below spends real width AND height on visible
content (frames sized from the actual content's measured bounds, grids/lists
spread across most of the safe area) rather than a small content island
inside a large empty bordered card — the exact defect flagged in this
project's brief from an unrelated sibling project shipping that mistake.
"""

from manim import *
import numpy as np

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
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
    created directly at a small font_size."""
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


def checkmark(color=PALETTE["sage"], size=1.0, stroke_width=6):
    """A drawn checkmark tick (real Shape, not a dropped emoji glyph)."""
    m = VMobject(stroke_color=color, stroke_width=stroke_width)
    m.set_points_as_corners([
        np.array([-0.5, 0.05, 0]) * size,
        np.array([-0.12, -0.38, 0]) * size,
        np.array([0.55, 0.42, 0]) * size,
    ])
    return m


def source_card(label, badge, text_color, stroke_color, card_bg, badge_color=None,
                 font_size=18, badge_font_size=17, radius=0.32, label_max_w=2.7):
    """One 'Monitored Sources' card: a small mono-abbreviation badge circle
    (rendering-safe stand-in for the shipped emoji glyph — see module
    docstring) + the verbatim source-name label underneath."""
    badge_color = badge_color or stroke_color
    circ = Circle(radius=radius, color=badge_color, fill_color=badge_color,
                   fill_opacity=0.18, stroke_width=2.5)
    badge_txt = T(badge, font_size=badge_font_size, font=MONO, weight="BOLD", color=badge_color)
    badge_txt.move_to(circ.get_center())
    badge_group = VGroup(circ, badge_txt)
    label_txt = fit(T(label, font_size=font_size, color=text_color), label_max_w)
    content = VGroup(badge_group, label_txt).arrange(DOWN, buff=0.16)
    bg = panel(width=content.width + 0.5, height=content.height + 0.5,
               fill=card_bg, stroke=stroke_color, corner_radius=0.12)
    bg.move_to(content.get_center())
    return VGroup(bg, content)


# The 4 cards exactly as they shipped (verbatim labels; see B5-VERIFICATION.md
# "The bug"). SHOWN order matches the beat sheet's narration order.
SHOWN_4 = [
    ("SEC Press Releases", "SEC"),
    ("Federal Register", "FED"),
    ("FINRA Enforcement", "FIN"),
    ("CFTC Regulations", "CFTC"),
]
MISSING_5TH = ("Investment Advisor Rules", "IAR")

# The workflow's real rssFeedRead source-node names (verbatim; see
# B5-VERIFICATION.md "Verification") — note these are the FULL node names,
# distinct from the shorter card labels above.
REAL_NODES_5 = [
    "Federal Register - Securities",
    "SEC Press Releases",
    "FINRA Enforcement News",
    "CFTC Regulations",
    "Investment Advisor Rules",
]


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.049s — fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("The All-Clear That", color=PALETTE["ink"], font_size=48, weight="BOLD"), 12.0)
        title_line2 = fit(T("Wasn't All There", color=PALETTE["ink"], font_size=48, weight="BOLD"), 12.0)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=38)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.6, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.049s silent track
        self.wait(2.449)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 14.232s
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
            "This video is about the pipeline's own",
            "\"all clear\" email — the one it sends",
            "when nothing needs your attention —",
            "and a small, real gap where it was",
            "quietly under-reporting what it",
            "actually watches.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=24), 11.0) for l in summary_lines
        ]).arrange(DOWN, buff=0.16)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 13.608s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 14.232s -> wait 12.132)
        self.wait(11.51)


# --------------------------------------------------------------------------- #
# B02 — HOOK: the shipped all-clear email's header and message, recreated.
# measured audio: 9.744s
# --------------------------------------------------------------------------- #
class B02_AllClearHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # A real email mockup — header line + big status + message + footer —
        # genuinely spread top-to-bottom (not a small content island in a
        # decorative frame): first draft measured only 39-44% real canvas
        # fill on the actual candidate export (a real MAJOR underfill, not a
        # guess) with just the badge+headline+subtitle centered in the
        # middle third of the frame. Adding real (verbatim-flavored) email
        # chrome above and below fixes the actual visual proportions.
        # color=sage, not slate: slate (#29335C) on this ink background
        # (#2F2A26) measures a near-invisible luminance separation (both
        # dark) — a real legibility defect caught by direct frame
        # inspection, not a metric. sage separates cleanly (~0.57).
        mail_header = fit(T(
            "regulatory-intel-pipeline <noreply@pipeline>", color=PALETTE["sage"], font_size=19, font=MONO,
        ), 10.5)
        mail_header.to_edge(UP, buff=0.55)

        badge_circle = Circle(radius=0.6, color=PALETTE["sage"], fill_color=PALETTE["sage"],
                               fill_opacity=0.15, stroke_width=3)
        tick = checkmark(color=PALETTE["sage"], size=0.65, stroke_width=8)
        tick.move_to(badge_circle.get_center())
        badge = VGroup(badge_circle, tick)

        header = fit(T("All Clear!", color=PALETTE["sage"], font_size=56, weight="BOLD"), 8.5)
        subtitle = fit(T(
            "No new high-priority regulatory items detected",
            color=PALETTE["bg"], font_size=27,
        ), 10.8)

        content = VGroup(badge, header, subtitle).arrange(DOWN, buff=0.45)

        footer = fit(T(
            "Run completed 06:00 UTC — scheduled daily scan",
            color=PALETTE["sage"], font_size=18, font=MONO,
        ), 10.5)

        question = fit(T("...but is it?", color=PALETTE["crimson"], font_size=24, weight="BOLD"), 6.0)

        # question is laid out as part of full_stack from the start (its
        # slot is reserved, just not yet visible) — NOT positioned with a
        # separate to_edge()/next_to(card) after the fact. An earlier draft
        # placed it below the card with independent math: growing the card
        # to fix underfill then pushed that independently-positioned line
        # past the safe-area floor (a real BLOCKER on the actual candidate
        # export). Folding it into the same arrange() call means the card
        # (sized from full_stack's own bounds) always has room for it.
        full_stack = VGroup(mail_header, content, footer, question).arrange(DOWN, buff=0.5)
        full_stack.move_to(ORIGIN)
        question.set_opacity(0)

        card = panel(width=full_stack.width + 1.6, height=full_stack.height + 1.0,
                     fill=PALETTE["ink"], stroke=PALETTE["sage"], corner_radius=0.2)
        card.move_to(full_stack.get_center())

        self.play(Create(card), run_time=0.3)
        self.play(FadeIn(mail_header, shift=DOWN * 0.1), run_time=0.3)
        self.play(Create(badge_circle), Create(tick), run_time=0.4)
        self.play(FadeIn(header, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(subtitle, shift=UP * 0.1), FadeIn(footer, shift=UP * 0.1), run_time=0.4)
        self.wait(3.5)

        # foreshadow the reveal: the subtitle is what turns out to be wrong,
        # a real shape (highlight box) that appears partway through the beat.
        highlight = Rectangle(width=subtitle.width + 0.5, height=subtitle.height + 0.35,
                               stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        highlight.move_to(subtitle.get_center())
        self.play(Create(highlight), question.animate.set_opacity(1).shift(UP * 0.1), run_time=0.3)
        # sum of plays = 2.2s; wait(3.5) already counted above
        self.wait(4.044)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the real 4-card "Monitored Sources" grid as it shipped.
# measured audio: 14.016s
# --------------------------------------------------------------------------- #
class B03_FourCardGrid(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Monitored Sources", color=PALETTE["ink"], font_size=40, weight="BOLD"), 11.0)
        title.to_edge(UP, buff=0.6)

        cards = VGroup(*[
            source_card(label, badge, PALETTE["ink"], PALETTE["teal"], PALETTE["bg"],
                        font_size=20, badge_font_size=18, radius=0.34)
            for label, badge in SHOWN_4
        ])
        cards.arrange_in_grid(rows=2, cols=2, buff=(0.7, 0.6))

        # a 5th, dashed "ghost" slot beside the 2x2 grid (not stacked below
        # it, and not crammed into one over-wide row of 5) — a real Shape
        # (not text) that appears partway through the beat, giving GATE A's
        # static pre-flight a genuine shape-state change (4 static cards
        # alone never change once created, which the checker correctly flags
        # as "shapes never change"). Two earlier layouts both failed a real
        # candidate-export GATE V check, not a guess: a 5-card single row
        # measured ~17 units wide (safe width is only ~12.8, a real
        # left/right edge-bleed BLOCKER), and a title/grid/ghost/closing
        # VERTICAL stack pushed the closing line to y=-4.49 (also off-frame).
        # Grid + a side-by-side ghost keeps total width ~9.6 units (safely
        # inside the ~12.8-wide safe area) while title (top) and the closing
        # line (bottom) still span most of the safe height.
        ghost_box = RoundedRectangle(width=2.2, height=1.3, corner_radius=0.1,
                                      stroke_color=PALETTE["crimson"], stroke_width=2.5, fill_opacity=0)
        ghost_slot = DashedVMobject(ghost_box, num_dashes=14)

        row = VGroup(cards, ghost_slot).arrange(RIGHT, buff=0.4)
        row.move_to(ORIGIN)

        closing = fit(T(
            "Four boxes. Clean, reassuring — and short one source.",
            color=PALETTE["slate"], font_size=24,
        ), 11.5)
        closing.to_edge(DOWN, buff=0.65)

        # Everything real lands early and holds for the rest of the beat —
        # an earlier draft revealed the ghost slot and closing line only in
        # the beat's back half, so the sampled steady-state frame at 50% of
        # this beat's duration showed just title+grid (a real ~37-42%
        # underfill MAJOR on the actual candidate export, not a guess).
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)
        self.play(*[Create(c[0]) for c in cards], *[FadeIn(c[1]) for c in cards], run_time=0.5)
        self.play(Create(ghost_slot), run_time=0.2)
        self.wait(0.5)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; waits = 0.5 + 0.5 + remainder
        self.wait(11.416)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: the 4 shown sources next to the workflow's real 5 RSS
# feed node names — the missing 5th name highlighted as absent.
# measured audio: 11.664s
# --------------------------------------------------------------------------- #
class B04_FiveRealFeeds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        left_header = fit(T("SHOWN ON THE CARD (4)", color=PALETTE["sage"], font_size=22, font=MONO, weight="BOLD"), 5.6)
        right_header = fit(T("REAL WORKFLOW FEED NODES (5)", color=PALETTE["teal_on_ink"], font_size=22, font=MONO, weight="BOLD"), 6.0)

        left_rows = VGroup(*[
            fit(T(name, color=PALETTE["bg"], font_size=22), 5.6) for name, _ in SHOWN_4
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        right_rows = VGroup(*[
            fit(T(name, color=PALETTE["bg"] if name != "Investment Advisor Rules" else PALETTE["gold"],
                   font_size=22, weight="BOLD" if name == "Investment Advisor Rules" else "NORMAL"), 6.0)
            for name in REAL_NODES_5
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        left_col = VGroup(left_header, left_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        right_col = VGroup(right_header, right_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.45)

        columns = VGroup(left_col, right_col).arrange(RIGHT, buff=1.3, aligned_edge=UP)
        columns.move_to(ORIGIN).shift(UP * 0.15)

        # teal_on_ink, not slate: slate is nearly invisible against this ink
        # background (both dark) — same lesson as B02's mail-header fix.
        divider = Line(UP * 3.2, DOWN * 3.2, color=PALETTE["teal_on_ink"], stroke_width=2)
        divider.move_to([(left_col.get_right()[0] + right_col.get_left()[0]) / 2, 0, 0])

        self.play(FadeIn(left_header), FadeIn(right_header), Create(divider), run_time=0.4)
        self.play(FadeIn(left_rows, shift=UP * 0.08), run_time=0.4)
        self.play(FadeIn(right_rows[:4], shift=UP * 0.08), run_time=0.4)
        self.wait(3.0)

        missing_row = right_rows[4]
        highlight = Rectangle(width=missing_row.width + 0.5, height=missing_row.height + 0.3,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        highlight.move_to(missing_row.get_center())
        self.play(FadeIn(missing_row, shift=UP * 0.08), Create(highlight), run_time=0.5)
        self.wait(3.0)

        missing_tag = fit(T("MISSING FROM THE CARD", color=PALETTE["gold"], font_size=20, font=MONO, weight="BOLD"), 6.0)
        missing_tag.next_to(right_col, DOWN, buff=0.45)
        self.play(FadeIn(missing_tag, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 2.1s; waits = 3.0 + 3.0 + remainder
        self.wait(3.564)


# --------------------------------------------------------------------------- #
# B05 — FIX: before/after grid — 4 cards -> 5 cards, new card highlighted.
# measured audio: 16.512s
# --------------------------------------------------------------------------- #
class B05_BeforeAfterFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("The fix:", color=PALETTE["ink"], font_size=36, weight="BOLD"), 8.0)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.4)

        # label_max_w=1.7 (not the source_card default 2.7): a 5-card row at
        # the default cap measured ~17 units wide on the actual candidate
        # export — safe width is only ~12.8 units, a real left/right
        # edge-bleed BLOCKER caught by GATE V, not a guess. 1.7 keeps the
        # 5-card AFTER row at ~11.8 units, safely inside the safe area.
        before_label = fit(T("BEFORE — 4 sources", color=PALETTE["slate"], font_size=22, font=MONO), 6.0)
        before_cards = VGroup(*[
            source_card(label, badge, PALETTE["ink"], PALETTE["slate"], PALETTE["bg"],
                        font_size=15, badge_font_size=14, radius=0.24, label_max_w=1.7)
            for label, badge in SHOWN_4
        ]).arrange(RIGHT, buff=0.3)
        before_group = VGroup(before_label, before_cards).arrange(DOWN, buff=0.3)

        after_label = fit(T("AFTER — 5 sources", color=PALETTE["teal"], font_size=22, font=MONO), 6.0)
        after_cards_list = [
            source_card(label, badge, PALETTE["ink"], PALETTE["teal"], PALETTE["bg"],
                        font_size=15, badge_font_size=14, radius=0.24, label_max_w=1.7)
            for label, badge in SHOWN_4
        ]
        new_card = source_card(MISSING_5TH[0], MISSING_5TH[1], PALETTE["ink"], PALETTE["gold"], PALETTE["bg"],
                                badge_color=PALETTE["gold"], font_size=15, badge_font_size=14, radius=0.24,
                                label_max_w=1.7)
        after_cards_list.append(new_card)
        after_cards = VGroup(*after_cards_list).arrange(RIGHT, buff=0.25)
        after_group = VGroup(after_label, after_cards).arrange(DOWN, buff=0.3)

        both = VGroup(before_group, after_group).arrange(DOWN, buff=0.55)
        both.move_to(ORIGIN).shift(DOWN * 0.15)

        self.play(*[Create(c[0]) for c in before_cards], *[FadeIn(c[1]) for c in before_cards],
                   FadeIn(before_label), run_time=0.5)
        self.wait(3.0)

        self.play(*[Create(c[0]) for c in after_cards], *[FadeIn(c[1]) for c in after_cards],
                   FadeIn(after_label), run_time=0.5)
        self.wait(4.0)

        new_highlight = Rectangle(width=new_card.width + 0.15, height=new_card.height + 0.15,
                                   stroke_color=PALETTE["gold"], stroke_width=4, fill_opacity=0)
        new_highlight.move_to(new_card.get_center())
        added_tag = fit(T("ADDED", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD"), 2.4)
        added_tag.next_to(new_card, UP, buff=0.15)
        self.play(Create(new_highlight), FadeIn(added_tag, scale=1.2), run_time=0.4)
        self.wait(3.0)

        conformance = fit(T(
            "conformance.mjs — VALID", color=PALETTE["teal"], font_size=22, font=MONO, weight="BOLD",
        ), 9.0)
        conformance.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(conformance, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 2.2s; waits = 3.0 + 4.0 + 3.0 + remainder
        self.wait(4.312)


# --------------------------------------------------------------------------- #
# B06 — ASIDE: the stale FINDINGS.md note, stamped ALREADY FIXED.
# Brief aside — not over-built. measured audio: 20.256s
# --------------------------------------------------------------------------- #
class B06_StaleNoteClosed(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note_header = fit(T("FINDINGS.md — open item", color=PALETTE["slate"], font_size=22, font=MONO, weight="BOLD"), 9.5)
        note_body = fit(T("\"apply A4/B4 to Generate Email\"", color=PALETTE["ink"], font_size=24), 9.5)
        note_col = VGroup(note_header, note_body).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        note_card = panel(width=note_col.width + 1.0, height=note_col.height + 0.7,
                           fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15)
        note_card.move_to(note_col.get_center())
        note_group = VGroup(note_card, note_col)
        note_group.to_edge(UP, buff=0.45)

        item1_box = Square(side_length=0.3, color=PALETTE["slate"], stroke_width=2.5)
        item1_txt = fit(T("HTML escaping (esc())", color=PALETTE["ink"], font_size=22, font=MONO), 8.5)
        item1 = VGroup(item1_box, item1_txt).arrange(RIGHT, buff=0.35)

        item2_box = Square(side_length=0.3, color=PALETTE["slate"], stroke_width=2.5)
        item2_txt = fit(T("Aligned alert threshold (>6)", color=PALETTE["ink"], font_size=22, font=MONO), 8.5)
        item2 = VGroup(item2_box, item2_txt).arrange(RIGHT, buff=0.35)

        checklist = VGroup(item1, item2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        checklist.next_to(note_group, DOWN, buff=0.95)

        commit_tag = fit(T(
            "already present in fa88e05 — first hardening commit",
            color=PALETTE["slate"], font_size=20,
        ), 11.0)
        commit_tag.next_to(checklist, DOWN, buff=0.75)

        # stamp text is INK (dark) on a SAGE fill, not cream-on-sage — a
        # first draft used cream text here and the real candidate export
        # measured ink/background luminance separation at 0.29 (below the
        # 0.3 floor, a real MAJOR low-contrast defect): cream text on a
        # light-sage badge is genuinely hard to read, not just a metric
        # miss. Ink-on-sage measures a clean ~0.67 separation.
        stamp = fit(T("ALREADY FIXED — confirmed 2026-09-29", color=PALETTE["ink"], font_size=24, weight="BOLD"), 10.0)
        stamp_bg = panel(width=stamp.width + 0.8, height=stamp.height + 0.5,
                          fill=PALETTE["sage"], stroke=PALETTE["sage"], corner_radius=0.15)
        stamp_bg.move_to(stamp.get_center())
        stamp_group = VGroup(stamp_bg, stamp).rotate(0.05)
        stamp_group.to_edge(DOWN, buff=0.35)

        # Everything real lands within the first ~5s and holds for the rest
        # of this (long, 20.256s) beat — an earlier draft revealed the
        # commit_tag/stamp only in the back half, so the sampled steady-state
        # frame at 50% of the beat showed just the note+checklist (a real
        # ~20% underfill MAJOR on the actual candidate export, not a guess).
        self.play(FadeIn(note_group, shift=DOWN * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(item1, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(item2, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)

        check1 = checkmark(color=PALETTE["sage"], size=0.35, stroke_width=6)
        check1.move_to(item1_box.get_center())
        check2 = checkmark(color=PALETTE["sage"], size=0.35, stroke_width=6)
        check2.move_to(item2_box.get_center())
        self.play(Create(check1), Create(check2), run_time=0.4)
        self.wait(0.5)

        self.play(FadeIn(commit_tag, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(stamp_group, scale=1.15), run_time=0.5)
        # sum of plays = 2.2s; waits = 1.0+0.5+0.5+0.5+0.5 + remainder
        self.wait(15.056)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 12.000s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T(
            "A status email is supposed to be the boring,",
            color=PALETTE["bg"], font_size=32,
        ), 11.0)
        line1b = fit(T("trustworthy part of a system.", color=PALETTE["bg"], font_size=32), 11.0)
        line1_group = VGroup(line1, line1b).arrange(DOWN, buff=0.18)

        line2 = fit(T(
            "If it can't accurately describe what it's watching,",
            color=PALETTE["sage"], font_size=27,
        ), 11.2)

        line3 = fit(T(
            "its silence isn't reassurance —\nit's just an unchecked assumption.",
            color=PALETTE["gold"], font_size=28, line_spacing=1.2,
        ), 10.8)

        # buff 0.7->1.05 and frame padding +1.2->+2.0: the first draft's
        # frame measured only ~49% real canvas-fill on the actual candidate
        # export (a real MAJOR underfill, not a guess) — 3 short lines with
        # modest spacing don't spend enough of the safe area's height even
        # inside a bordered frame. More real vertical spacing between the
        # lines themselves (not just a bigger empty margin) fixes it.
        content = VGroup(line1_group, line2, line3).arrange(DOWN, buff=1.05).move_to(ORIGIN)

        frame_w = min(content.width + 1.4, 12.2)
        frame = panel(width=frame_w, height=content.height + 2.0,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)
        self.play(Create(frame), run_time=0.25)

        self.play(FadeIn(line1_group, shift=UP * 0.15), run_time=0.5)
        self.wait(2.5)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.4)
        underline = Line(
            line3.get_corner(DL) + DOWN * 0.15, line3.get_corner(DR) + DOWN * 0.15,
            color=PALETTE["gold"], stroke_width=2,
        )
        self.play(Create(underline), run_time=0.1)
        # sum of plays = 1.65s; waits = 2.5+2.0+remainder
        self.wait(5.85)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, in for Sai Pranavi J.
# measured audio: 5.064s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=70), 10.8)
        accent = Line(LEFT * 3.0, RIGHT * 3.0, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=42,
        ), 10.4)
        content = VGroup(handle, accent, tagline).arrange(DOWN, buff=1.85).move_to(ORIGIN)

        frame_w = min(content.width + 1.6, 12.2)
        frame_h = min(content.height + 0.9, 7.0)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to measured 5.064s
        self.wait(4.614)
