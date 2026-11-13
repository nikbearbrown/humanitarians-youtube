"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-09-22-the-all-clear-that-wasnt-all-there

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command — NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard (see
brutalist/docs/PIPELINE-SAFETY.md, "Isolated portrait companions and
Shorts"). All 9 parent beats are kept; every mp3 is reused byte-for-byte
from the parent's mp3/ folder (see vertical/beat_sheet.json, written by
shorts.py). Every beat here is a Manim GRAPHIC beat, so THE REFORMAT RULE's
auto center-cut never applies (generated graphics are never cropped) — each
class below is a genuine portrait RE-LAYOUT of the parent ../scenes.py
composition, authored by hand for a 1080x1920 canvas (rendered at
2160x3840 for the true 4K vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the parent file's vertical safe/hard bounds (to_edge(UP/DOWN, buff=...))
carry over almost unchanged. What changes is frame_width: 4.5 instead of
14.222 — a hard edge of only +/-2.25 and a safe half-width of ~1.95 (vs the
parent's +/-6.3). MAX_W = 3.6 is this file's general content-width budget
(leaves ~0.15 margin on each side).

Beat-by-beat redesign notes:
  B00 TitleCard        — title re-wrapped 2->4 narrow lines.
  B01 ExecSummary      — badge+name row (side-by-side in the parent)
                         stacked badge-above-name; summary re-wrapped to
                         narrow lines.
  B02 AllClearHook     — already a single vertical column in the parent;
                         narrowed widths + re-wrapped text.
  B03 FourCardGrid     — 2x2 card grid (same shape as parent) + ghost slot
                         BELOW the grid (not beside it — no horizontal
                         room in portrait), narrower cards.
  B04 FiveRealFeeds    — THE big redesign: parent's LEFT/RIGHT columns ->
                         TOP (shown-on-card) / BOTTOM (real workflow nodes)
                         stack, both simultaneously visible.
  B05 BeforeAfterFix   — parent's horizontal BEFORE/AFTER card rows -> each
                         row wraps 2x2 (BEFORE) / 2x3 (AFTER, last cell
                         the new highlighted card) instead of a single wide
                         row, so nothing needs portrait-row compression.
  B06 StaleNoteClosed  — already vertical-friendly; narrowed + re-wrapped.
  B07 Statement        — already vertical-friendly; narrowed + re-wrapped.
  B08 BrandOutro       — unchanged composition; only widths trimmed.

Palette/MONO/fit()/T()/panel()/checkmark()/source_card() are copied
verbatim from ../scenes.py for visual continuity, including the emoji ->
mono-badge substitution (see that file's module docstring for the
empirical finding) and the slate-vs-ink contrast fix (B02/B04).
"""

from manim import *
import numpy as np

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup — BEFORE
# the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait — every
# coordinate in this file is designed against a 4.5-wide frame, so without
# this fix everything would render ~3.2x too small and clustered dead-center.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

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
MAX_W = 3.6   # general portrait content-width budget (safe half-width 1.95)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See ../scenes.py for the empirical proof."""
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
                 font_size=16, badge_font_size=14, radius=0.24, label_max_w=1.5):
    """One 'Monitored Sources' card — portrait-scaled version of the parent's
    helper (smaller default sizes/width budget, same mono-badge pattern)."""
    badge_color = badge_color or stroke_color
    circ = Circle(radius=radius, color=badge_color, fill_color=badge_color,
                   fill_opacity=0.18, stroke_width=2.5)
    badge_txt = T(badge, font_size=badge_font_size, font=MONO, weight="BOLD", color=badge_color)
    badge_txt.move_to(circ.get_center())
    badge_group = VGroup(circ, badge_txt)
    label_txt = fit(T(label, font_size=font_size, color=text_color), label_max_w)
    content = VGroup(badge_group, label_txt).arrange(DOWN, buff=0.14)
    bg = panel(width=content.width + 0.4, height=content.height + 0.4,
               fill=card_bg, stroke=stroke_color, corner_radius=0.1)
    bg.move_to(content.get_center())
    return VGroup(bg, content)


SHOWN_4 = [
    ("SEC Press Releases", "SEC"),
    ("Federal Register", "FED"),
    ("FINRA Enforcement", "FIN"),
    ("CFTC Regulations", "CFTC"),
]
MISSING_5TH = ("Investment Advisor Rules", "IAR")

REAL_NODES_5 = [
    "Federal Register - Securities",
    "SEC Press Releases",
    "FINRA Enforcement News",
    "CFTC Regulations",
    "Investment Advisor Rules",
]


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Title re-wrapped 2 -> 4 narrow lines.
# measured (silent) duration: 4.049s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The All-Clear", "That Wasn't", "All There"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W)
            for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame = panel(width=3.9, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.449)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name/role (parent's side-by-side
# row would starve the name of width next to a badge in this narrow frame).
# measured audio: 13.608s (2026-10-20 name-retrofit: "Sai Pranavi J.", was 14.232s)
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.42, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video is about",
            "the pipeline's own",
            "\"all clear\" email —",
            "the one it sends when",
            "nothing needs your",
            "attention — and a",
            "small, real gap where",
            "it was quietly under-",
            "reporting what it",
            "actually watches.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.1)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge, run_time=0.2), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 13.608s Kokoro length
        # (2026-10-20 name-retrofit: 13.608 - 1.8 = 11.808)
        self.wait(11.81)


# --------------------------------------------------------------------------- #
# B02 — HOOK: already a single vertical column in the parent; narrowed
# widths + re-wrapped text. Email mockup, question folded into the same
# layout group as the parent (not independently positioned below the card).
# measured audio: 9.744s
# --------------------------------------------------------------------------- #
class B02_AllClearHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        mail_header = fit(T(
            "regulatory-intel-pipeline", color=PALETTE["sage"], font_size=14, font=MONO,
        ), MAX_W)

        badge_circle = Circle(radius=0.45, color=PALETTE["sage"], fill_color=PALETTE["sage"],
                               fill_opacity=0.15, stroke_width=3)
        tick = checkmark(color=PALETTE["sage"], size=0.5, stroke_width=7)
        tick.move_to(badge_circle.get_center())
        badge = VGroup(badge_circle, tick)

        header = fit(T("All Clear!", color=PALETTE["sage"], font_size=40, weight="BOLD"), MAX_W)
        subtitle = fit(T(
            "No new high-priority\nregulatory items detected",
            color=PALETTE["bg"], font_size=19, line_spacing=1.2,
        ), MAX_W)

        content = VGroup(badge, header, subtitle).arrange(DOWN, buff=0.4)

        footer = fit(T(
            "Run completed 06:00 UTC\nscheduled daily scan",
            color=PALETTE["sage"], font_size=14, font=MONO, line_spacing=1.2,
        ), MAX_W)

        question = fit(T("...but is it?", color=PALETTE["crimson"], font_size=20, weight="BOLD"), MAX_W)

        full_stack = VGroup(mail_header, content, footer, question).arrange(DOWN, buff=0.4)
        full_stack.move_to(ORIGIN)
        question.set_opacity(0)

        card = panel(width=full_stack.width + 0.7, height=full_stack.height + 0.6,
                     fill=PALETTE["ink"], stroke=PALETTE["sage"], corner_radius=0.2)
        card.move_to(full_stack.get_center())

        self.play(Create(card), run_time=0.3)
        self.play(FadeIn(mail_header, shift=DOWN * 0.1), run_time=0.3)
        self.play(Create(badge_circle), Create(tick), run_time=0.4)
        self.play(FadeIn(header, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(subtitle, shift=UP * 0.1), FadeIn(footer, shift=UP * 0.1), run_time=0.4)
        self.wait(3.5)

        highlight = Rectangle(width=subtitle.width + 0.35, height=subtitle.height + 0.3,
                               stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        highlight.move_to(subtitle.get_center())
        self.play(Create(highlight), question.animate.set_opacity(1).shift(UP * 0.1), run_time=0.3)
        self.wait(4.044)


# --------------------------------------------------------------------------- #
# B03 — SETUP: 2x2 grid (same shape as parent) + ghost slot BELOW the grid
# (not beside it — no horizontal room in portrait for a 3rd column).
# measured audio: 14.016s
# --------------------------------------------------------------------------- #
class B03_FourCardGrid(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Monitored Sources", color=PALETTE["ink"], font_size=28, weight="BOLD"), MAX_W)
        title.to_edge(UP, buff=0.68)

        # label_max_w 1.5 -> 1.1: the 2x2 grid at the wider cap measured
        # ~4.1 units wide on the actual candidate export — safe width here
        # is only ~3.9 units, a real left/right edge-bleed BLOCKER, not a
        # guess.
        cards = VGroup(*[
            source_card(label, badge, PALETTE["ink"], PALETTE["teal"], PALETTE["bg"],
                        font_size=15, badge_font_size=13, radius=0.24, label_max_w=1.1)
            for label, badge in SHOWN_4
        ])
        cards.arrange_in_grid(rows=2, cols=2, buff=(0.3, 0.22))

        ghost_box = RoundedRectangle(width=1.4, height=0.9, corner_radius=0.1,
                                      stroke_color=PALETTE["crimson"], stroke_width=2.5, fill_opacity=0)
        ghost_slot = DashedVMobject(ghost_box, num_dashes=12)

        stack = VGroup(cards, ghost_slot).arrange(DOWN, buff=0.4)
        stack.move_to(ORIGIN).shift(DOWN * 0.1)

        closing = fit(T(
            "Four boxes. Clean,\nreassuring — and short one source.",
            color=PALETTE["slate"], font_size=17, line_spacing=1.2,
        ), MAX_W)
        closing.to_edge(DOWN, buff=0.68)

        self.play(Write(title), run_time=0.5)
        self.wait(0.5)
        self.play(*[Create(c[0]) for c in cards], *[FadeIn(c[1]) for c in cards], run_time=0.5)
        self.play(Create(ghost_slot), run_time=0.2)
        self.wait(0.5)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        self.wait(11.416)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: THE redesign. Parent's LEFT (shown)/RIGHT (real nodes)
# columns -> TOP/BOTTOM stack, both simultaneously visible.
# measured audio: 11.664s
# --------------------------------------------------------------------------- #
class B04_FiveRealFeeds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        top_header = fit(T("SHOWN ON CARD (4)", color=PALETTE["sage"], font_size=17, font=MONO, weight="BOLD"), MAX_W)
        top_rows = VGroup(*[
            fit(T(name, color=PALETTE["bg"], font_size=16), MAX_W) for name, _ in SHOWN_4
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        top_col = VGroup(top_header, top_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        bot_header = fit(T("REAL WORKFLOW NODES (5)", color=PALETTE["teal_on_ink"], font_size=17, font=MONO, weight="BOLD"), MAX_W)
        bot_rows = VGroup(*[
            fit(T(name, color=PALETTE["bg"] if name != "Investment Advisor Rules" else PALETTE["gold"],
                   font_size=16, weight="BOLD" if name == "Investment Advisor Rules" else "NORMAL"), MAX_W)
            for name in REAL_NODES_5
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        bot_col = VGroup(bot_header, bot_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        # buff 0.5->0.7: a bit more real vertical spacing between the two
        # columns (not a bigger empty margin) — the first pass measured 51%
        # canvas-fill on the actual candidate export, just under the 55%
        # floor, with everything already timed to land well before the
        # beat's 50% sample point (see the reveal-early timing below).
        both = VGroup(top_col, bot_col).arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        both.move_to(ORIGIN)

        divider = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["teal_on_ink"], stroke_width=2)
        divider.move_to([0, (top_col.get_bottom()[1] + bot_col.get_top()[1]) / 2, 0])

        missing_row = bot_rows[4]
        highlight = Rectangle(width=missing_row.width + 0.3, height=missing_row.height + 0.2,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        highlight.move_to(missing_row.get_center())

        missing_tag = fit(T("MISSING FROM\nTHE CARD", color=PALETTE["gold"], font_size=15, font=MONO,
                             weight="BOLD", line_spacing=1.2), MAX_W)
        missing_tag.next_to(both, DOWN, buff=0.35)

        # Everything real lands within the first ~2s and holds for the rest
        # of the beat — an earlier draft revealed missing_row/highlight/tag
        # only in the back half, so the sampled steady-state frame at 50%
        # of this beat showed top_col+bot_col[:4] alone (the real ~51%
        # underfill above).
        self.play(FadeIn(top_header), Create(divider), run_time=0.4)
        self.play(FadeIn(top_rows, shift=UP * 0.08), run_time=0.3)
        self.play(FadeIn(bot_header), FadeIn(bot_rows[:4], shift=UP * 0.08), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(missing_row, shift=UP * 0.08), Create(highlight), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(missing_tag, shift=UP * 0.1), run_time=0.3)
        self.wait(8.964)


# --------------------------------------------------------------------------- #
# B05 — FIX: BEFORE (2x2) / AFTER (2x3 with 1 empty cell) card grids
# stacked, instead of the parent's single wide horizontal rows — wrapping
# into a grid (not compressing into one over-narrow row) is what keeps each
# card legible in the portrait width.
# measured audio: 16.512s
# --------------------------------------------------------------------------- #
class B05_BeforeAfterFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("The fix:", color=PALETTE["ink"], font_size=30, weight="BOLD"), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.4)

        # Bordered card grids (2x2 / 2x3) measured OFF-FRAME at this
        # portrait width on the actual render — a real BLOCKER, not a
        # guess (3-across cards bled past +/-1.95 safe x; even a 2x2+1
        # stack ran ~1.1 units too tall for the safe height budget once
        # title/conformance were included). Simple colored TEXT ROWS (the
        # same proven-safe pattern as this file's own B04) carry the same
        # information — 4 vs 5 sources, the 5th highlighted — without
        # either failure mode.
        before_label = fit(T("BEFORE — 4 sources", color=PALETTE["slate"], font_size=18, font=MONO), MAX_W)
        before_rows = VGroup(*[
            fit(T(label, color=PALETTE["ink"], font_size=17), MAX_W) for label, _ in SHOWN_4
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        before_group = VGroup(before_label, before_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        after_label = fit(T("AFTER — 5 sources", color=PALETTE["teal"], font_size=18, font=MONO), MAX_W)
        after_rows = VGroup(*[
            fit(T(label, color=PALETTE["ink"], font_size=17), MAX_W) for label, _ in SHOWN_4
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        new_row = fit(T(MISSING_5TH[0], color=PALETTE["gold"], font_size=17, weight="BOLD"), MAX_W)
        after_all_rows = VGroup(*after_rows, new_row).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        after_group = VGroup(after_label, after_all_rows).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        both = VGroup(before_group, after_group).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        both.move_to(ORIGIN).shift(DOWN * 0.1)

        # a real Shape divider between BEFORE and AFTER (not just text) —
        # gives GATE A's static pre-flight a genuine non-text shape that
        # changes state over the beat (created partway through), alongside
        # new_highlight below.
        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["slate"], stroke_width=2)
        divider.move_to([0, (before_group.get_bottom()[1] + after_group.get_top()[1]) / 2, 0])

        new_highlight = Rectangle(width=new_row.width + 0.3, height=new_row.height + 0.18,
                                   stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        new_highlight.move_to(new_row.get_center())
        added_tag = fit(T("ADDED", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), 1.6)
        added_tag.next_to(new_row, DOWN, buff=0.12)

        conformance = fit(T(
            "conformance.mjs\nVALID", color=PALETTE["teal"], font_size=17, font=MONO, weight="BOLD",
            line_spacing=1.2,
        ), MAX_W)
        conformance.to_edge(DOWN, buff=0.6)

        # Everything real lands within the first ~2.6s and holds for the
        # rest of the beat — an earlier draft revealed new_row/conformance
        # only in the back half, so the sampled steady-state frame at 50%
        # of this (16.5s) beat showed just title+before+after+divider (a
        # real ~52% underfill MAJOR on the actual candidate export).
        self.play(FadeIn(before_rows, shift=UP * 0.08), FadeIn(before_label), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(after_rows, shift=UP * 0.08), FadeIn(after_label), Create(divider), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(new_row, shift=UP * 0.08), Create(new_highlight),
                   FadeIn(added_tag, scale=1.2), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(conformance, shift=UP * 0.1), run_time=0.4)
        self.wait(13.012)


# --------------------------------------------------------------------------- #
# B06 — ASIDE: already vertical-friendly; narrowed + re-wrapped.
# measured audio: 20.256s
# --------------------------------------------------------------------------- #
class B06_StaleNoteClosed(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        note_header = fit(T("FINDINGS.md\nopen item", color=PALETTE["slate"], font_size=17, font=MONO,
                             weight="BOLD", line_spacing=1.2), MAX_W)
        note_body = fit(T("\"apply A4/B4 to\nGenerate Email\"", color=PALETTE["ink"], font_size=18,
                           line_spacing=1.2), MAX_W)
        note_col = VGroup(note_header, note_body).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        note_card = panel(width=note_col.width + 0.5, height=note_col.height + 0.4,
                           fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15)
        note_card.move_to(note_col.get_center())
        note_group = VGroup(note_card, note_col)
        note_group.to_edge(UP, buff=0.6)

        item1_box = Square(side_length=0.24, color=PALETTE["slate"], stroke_width=2.5)
        item1_txt = fit(T("HTML escaping", color=PALETTE["ink"], font_size=17, font=MONO), 2.6)
        item1 = VGroup(item1_box, item1_txt).arrange(RIGHT, buff=0.25)

        item2_box = Square(side_length=0.24, color=PALETTE["slate"], stroke_width=2.5)
        item2_txt = fit(T("Alert threshold", color=PALETTE["ink"], font_size=17, font=MONO), 2.6)
        item2 = VGroup(item2_box, item2_txt).arrange(RIGHT, buff=0.25)

        checklist = VGroup(item1, item2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        checklist.next_to(note_group, DOWN, buff=0.7)

        commit_tag = fit(T(
            "already present in fa88e05\nfirst hardening commit",
            color=PALETTE["slate"], font_size=15, line_spacing=1.2,
        ), MAX_W)
        commit_tag.next_to(checklist, DOWN, buff=0.55)

        stamp = fit(T("ALREADY FIXED\nconfirmed 2026-09-29", color=PALETTE["ink"], font_size=18,
                       weight="BOLD", line_spacing=1.2), MAX_W)
        stamp_bg = panel(width=stamp.width + 0.6, height=stamp.height + 0.4,
                          fill=PALETTE["sage"], stroke=PALETTE["sage"], corner_radius=0.15)
        stamp_bg.move_to(stamp.get_center())
        stamp_group = VGroup(stamp_bg, stamp).rotate(0.05)
        stamp_group.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(note_group, shift=DOWN * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(item1, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(item2, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)

        check1 = checkmark(color=PALETTE["sage"], size=0.3, stroke_width=6)
        check1.move_to(item1_box.get_center())
        check2 = checkmark(color=PALETTE["sage"], size=0.3, stroke_width=6)
        check2.move_to(item2_box.get_center())
        self.play(Create(check1), Create(check2), run_time=0.4)
        self.wait(0.5)

        self.play(FadeIn(commit_tag, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(stamp_group, scale=1.15), run_time=0.5)
        self.wait(15.056)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: already vertical-friendly; narrowed + re-wrapped.
# measured audio: 12.000s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T(
            "A status email is\nsupposed to be the\nboring, trustworthy\npart of a system.",
            color=PALETTE["bg"], font_size=22, line_spacing=1.25,
        ), MAX_W)

        line2 = fit(T(
            "If it can't accurately\ndescribe what it's\nwatching,",
            color=PALETTE["sage"], font_size=19, line_spacing=1.25,
        ), MAX_W)

        line3 = fit(T(
            "its silence isn't\nreassurance — it's just\nan unchecked assumption.",
            color=PALETTE["gold"], font_size=17, line_spacing=1.25,
        ), MAX_W)

        content = VGroup(line1, line2, line3).arrange(DOWN, buff=0.65).move_to(ORIGIN)

        frame_w = min(content.width + 0.8, 3.9)
        frame = panel(width=frame_w, height=content.height + 1.3,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)
        self.play(Create(frame), run_time=0.25)

        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.5)
        self.wait(2.5)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.4)
        underline = Line(
            line3.get_corner(DL) + DOWN * 0.12, line3.get_corner(DR) + DOWN * 0.12,
            color=PALETTE["gold"], stroke_width=2,
        )
        self.play(Create(underline), run_time=0.1)
        self.wait(5.85)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 5.064s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=36), MAX_W)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=24, line_spacing=1.25,
        ), MAX_W)
        content = VGroup(handle, accent, tagline).arrange(DOWN, buff=1.85).move_to(ORIGIN)

        frame_w = min(content.width + 1.0, 3.9)
        frame_h = min(content.height + 0.9, 7.0)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        self.wait(4.614)
