"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-09-29-tokenization-why-ai-cant-count-its-own-letters

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

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect
(so the parent file's y-axis safe/hard bounds — to_edge(UP/DOWN, buff=...)
— carry over UNCHANGED; only frame_width shrinks). What changes is
frame_width: ~4.5 instead of 14.222 — a hard edge of only +/-2.25 and a
safe half-width of ~1.95 (vs the parent's +/-6.3). MAX_W = 3.6 is this
file's general content-width budget (leaves ~0.15 margin on each side).
Every side-by-side layout in the parent (B02's two task cards, B04's
model/true count boxes) is re-composed here as a TOP/BOTTOM stack instead
of LEFT/RIGHT columns, and B05's 10-letter token row is re-wrapped into two
rows of 5 — matching this fellow's sibling reels' own portrait-redesign
convention.

Beat-by-beat redesign notes:
  B00 TitleCard            — title re-wrapped 3->4 narrow lines.
  B01 ExecSummary          — badge stacked ABOVE name/role; summary re-wrapped
                             to narrower lines.
  B02 TwoTasksHook         — parent's LEFT/RIGHT task cards -> TOP/BOTTOM stack.
  B03 TokenSplitDiagram    — already single-column; chunk row narrowed to fit MAX_W.
  B04 MiscountedTally      — parent's side-by-side model/true count boxes ->
                             TOP/BOTTOM stack with the mismatch sign between them.
  B05 SpelledOutFix        — parent's single 10-letter row -> two rows of 5
                             letters (STRAW / BERRY split) to fit MAX_W.
  B06 AuditChecklist       — already single-column; card narrowed, same checklist.
  B07 Statement            — already single-column; lines re-wrapped narrower.
  B08 BrandOutro           — unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around()/token_chunk() are copied
verbatim from ../scenes.py for visual continuity. See ../scenes.py for the
full beat-by-beat build history (timing derivations, GATE V findings,
illustrative-word rationale) — nothing about WHAT is said or WHEN changes
here, only how it is laid out for the narrow canvas.
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
# Copied verbatim from this fellow's sibling reels' vertical/scenes.py, which
# found and documented this exact bug.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm -- avoid as TEXT on ink
    "slate":  "#29335C",  # structure -- low-contrast on ink; use "sage" instead
    "gold":   "#F3A712",  # fill/stroke/accent; safe as TEXT on ink too.
    "sage":   "#A8C686",  # human / growth; safe secondary text color on ink.
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


def box_around(mob, buff=0.12, color=None):
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color or PALETTE["gold"], stroke_width=3, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


def token_chunk(label, color, font_size=34):
    """One colored token-chunk pill — see ../scenes.py's docstring."""
    txt = T(label, color=PALETTE["bg"], font_size=font_size, font=MONO, weight="BOLD")
    pad_w, pad_h = 0.5, 0.35
    bg = panel(width=txt.width + pad_w, height=txt.height + pad_h,
               fill=color, stroke=PALETTE["bg"], corner_radius=0.12, opacity=1.0)
    txt.move_to(bg.get_center())
    return VGroup(bg, txt)


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Title re-wrapped 3 -> 4 narrow lines.
# measured (silent) duration: 4.056s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Tokenization:", "Why AI Can't", "Count the Letters", "in Its Own Words"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W)
            for l in title_lines
        ]).arrange(DOWN, buff=0.2)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        frame = panel(width=3.9, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.056s silent track
        self.wait(2.456)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name/role (parent's side-by-side
# row would starve the name of width next to a badge in this narrow frame).
# measured audio: 14.09s
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

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: why AI",
            "models mess up tasks",
            "like counting letters",
            "or finding rhymes —",
            "even though they can",
            "write whole essays",
            "correctly — and the",
            "one mechanism that",
            "explains it.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.1)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 13.56s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 14.09s -> wait 12.29)
        self.wait(11.76)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's LEFT/RIGHT task cards -> TOP/BOTTOM stack.
# measured audio: 13.70s
# --------------------------------------------------------------------------- #
class B02_TwoTasksHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same model.\nTwo tasks.", color=PALETTE["bg"],
                          font_size=24, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # ---- TOP: counting letters ----
        top_panel = panel(width=3.7, height=2.5, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        top_header = fit(T("COUNT LETTERS", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD"), 3.3)
        top_example = fit(T('"How many R\'s in\nstrawberry?"', color=PALETTE["bg"],
                                font_size=14, line_spacing=1.2), 3.3)
        top_stamp = fit(T("OFTEN WRONG", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD"), 3.2)
        top_content = VGroup(top_header, top_example, top_stamp).arrange(DOWN, buff=0.22)

        # ---- BOTTOM: writing an essay ----
        bot_panel = panel(width=3.7, height=2.5, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        bot_header = fit(T("WRITE AN ESSAY", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD"), 3.3)
        bot_example = fit(T('"Explain photosynthesis\nin 3 paragraphs."', color=PALETTE["bg"],
                                font_size=14, line_spacing=1.2), 3.3)
        bot_stamp = fit(T("RELIABLE", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD"), 3.2)
        bot_content = VGroup(bot_header, bot_example, bot_stamp).arrange(DOWN, buff=0.22)

        top_content.move_to(top_panel.get_center())
        bot_content.move_to(bot_panel.get_center())

        top_group = VGroup(top_panel, top_content)
        bot_group = VGroup(bot_panel, bot_content)
        panels = VGroup(top_group, bot_group).arrange(DOWN, buff=0.3)
        # cap 5.4 -> 4.6: GATE B's post-render layout audit caught the
        # zinger line below (to_edge(DOWN, buff=0.68)) landing directly on
        # the bottom panel's own rounded corner curve (a real TEXT_ON_CURVE,
        # not a guessed margin) — the uncapped natural height (5.3) was
        # under the old 5.4 ceiling and so never actually got scaled down.
        if panels.height > 4.6:
            panels.scale_to_fit_height(4.6)
        panels.next_to(title, DOWN, buff=0.3)

        self.play(Create(top_panel), Create(bot_panel), run_time=0.5)
        self.play(FadeIn(top_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(bot_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        top_stamp_box = box_around(top_stamp, buff=0.1, color=PALETTE["gold"])
        bot_stamp_box = box_around(bot_stamp, buff=0.1, color=PALETTE["sage"])
        self.play(Create(top_stamp_box), Create(bot_stamp_box), run_time=0.3)
        self.wait(0.5)

        zinger = fit(T("Wildly different\nreliability.", color=PALETTE["gold"],
                           font_size=20, line_spacing=1.2), MAX_W)
        zinger.to_edge(DOWN, buff=0.68)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 2.8s, waits above = 5.5s; remainder tuned to the
        # measured 13.70s Kokoro length (13.70 - 2.8 - 5.5 = 5.4)
        self.wait(5.4)


# --------------------------------------------------------------------------- #
# B03 — MECHANISM: already single-column; word + chunk row narrowed to fit
# MAX_W. Same 3-chunk split as the parent (STRAW / BER / RY).
# measured audio: 21.46s
# --------------------------------------------------------------------------- #
class B03_TokenSplitDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        frame = panel(width=3.9, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        title = fit(T("Here's why:", color=PALETTE["ink"], font_size=26), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), Create(frame), run_time=0.5)
        self.wait(1.2)

        whole_word = T("strawberry", color=PALETTE["ink"], font_size=36, font=MONO, weight="BOLD")
        whole_word = fit(whole_word, MAX_W)
        whole_word.move_to(UP * 1.3)
        self.play(FadeIn(whole_word, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)

        chunk1 = token_chunk("STRAW", PALETTE["teal"], font_size=22)
        chunk2 = token_chunk("BER", PALETTE["crimson"], font_size=22)
        chunk3 = token_chunk("RY", PALETTE["slate"], font_size=22)
        chunks = VGroup(chunk1, chunk2, chunk3).arrange(RIGHT, buff=0.18)
        if chunks.width > MAX_W:
            chunks.scale_to_fit_width(MAX_W)
        chunks.move_to(UP * 1.3)

        self.play(FadeOut(whole_word), FadeIn(chunks, shift=UP * 0.1), run_time=0.8)
        self.wait(1.0)

        label1 = fit(T("TOKEN 1", color=PALETTE["teal"], font_size=13, font=MONO), 1.1)
        label2 = fit(T("TOKEN 2", color=PALETTE["crimson"], font_size=13, font=MONO), 1.1)
        label3 = fit(T("TOKEN 3", color=PALETTE["slate"], font_size=13, font=MONO), 1.1)
        label1.next_to(chunk1, DOWN, buff=0.18)
        label2.next_to(chunk2, DOWN, buff=0.18)
        label3.next_to(chunk3, DOWN, buff=0.18)
        labels = VGroup(label1, label2, label3)
        self.play(FadeIn(labels), run_time=0.5)
        self.wait(1.0)

        box1 = box_around(chunk1, buff=0.06, color=PALETTE["gold"])
        box2 = box_around(chunk2, buff=0.06, color=PALETTE["gold"])
        box3 = box_around(chunk3, buff=0.06, color=PALETTE["gold"])
        self.play(Create(VGroup(box1, box2, box3)), run_time=0.4)
        self.wait(1.0)

        caption1 = fit(T("model sees these\nchunks —", color=PALETTE["crimson"],
                             font_size=18, line_spacing=1.2), MAX_W)
        caption2 = fit(T("not the letters inside", color=PALETTE["crimson"], font_size=18), MAX_W)
        caption = VGroup(caption1, caption2).arrange(DOWN, buff=0.18)
        caption.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        # sum of plays = 3.2s, waits above = 6.0s; remainder tuned to the
        # measured 21.46s Kokoro length (21.46 - 3.2 - 6.0 = 12.26)
        self.wait(12.26)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: parent's side-by-side model/true count boxes ->
# TOP/BOTTOM stack, mismatch sign between them.
# measured audio: 18.05s
# --------------------------------------------------------------------------- #
class B04_MiscountedTally(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T('Count the R\'s in\n"strawberry":', color=PALETTE["bg"],
                          font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        chunk1 = token_chunk("STRAW", PALETTE["teal"], font_size=18)
        chunk2 = token_chunk("BER", PALETTE["crimson"], font_size=18)
        chunk3 = token_chunk("RY", PALETTE["slate"], font_size=18)
        chunks = VGroup(chunk1, chunk2, chunk3).arrange(RIGHT, buff=0.16)
        if chunks.width > MAX_W:
            chunks.scale_to_fit_width(MAX_W)
        chunks.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(chunks, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)

        tally1 = fit(T("sees 1 R", color=PALETTE["sage"], font_size=12, font=MONO), 1.1)
        tally2 = fit(T("sees 1 R", color=PALETTE["sage"], font_size=12, font=MONO), 1.1)
        tally3 = fit(T("sees 0 R", color=PALETTE["crimson"], font_size=12, font=MONO, weight="BOLD"), 1.1)
        tally1.next_to(chunk1, DOWN, buff=0.15)
        tally2.next_to(chunk2, DOWN, buff=0.15)
        tally3.next_to(chunk3, DOWN, buff=0.15)
        tallies = VGroup(tally1, tally2, tally3)
        self.play(FadeIn(tallies), run_time=0.5)
        self.wait(1.5)

        # TOP/BOTTOM stack (not side-by-side — too narrow at MAX_W=3.6 for
        # two readable boxes side by side), the mismatch sign between them.
        model_box = panel(width=3.3, height=1.5, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        model_label = fit(T("MODEL'S COUNT", color=PALETTE["sage"], font_size=13, font=MONO), 2.9)
        model_number = T("2", color=PALETTE["crimson"], font_size=34, font=MONO, weight="BOLD")
        model_content = VGroup(model_label, model_number).arrange(DOWN, buff=0.15)
        model_content.move_to(model_box.get_center())

        true_box = panel(width=3.3, height=1.5, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        true_label = fit(T("TRUE COUNT", color=PALETTE["sage"], font_size=13, font=MONO), 2.9)
        true_number = T("3", color=PALETTE["sage"], font_size=34, font=MONO, weight="BOLD")
        true_content = VGroup(true_label, true_number).arrange(DOWN, buff=0.15)
        true_content.move_to(true_box.get_center())

        model_group = VGroup(model_box, model_content)
        true_group = VGroup(true_box, true_content)
        mismatch = T("≠", color=PALETTE["gold"], font_size=36, weight="BOLD")

        boxes = VGroup(model_group, mismatch, true_group).arrange(DOWN, buff=0.12)
        boxes.next_to(tallies, DOWN, buff=0.35)

        self.play(Create(model_box), Create(true_box), run_time=0.5)
        self.play(FadeIn(model_content), FadeIn(true_content), run_time=0.5)
        self.wait(1.5)

        self.play(Write(mismatch), run_time=0.4)
        self.wait(1.5)

        closing = fit(T("Working from the\nwrong unit entirely.", color=PALETTE["gold"],
                            font_size=16, line_spacing=1.2), MAX_W)
        closing.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.3s, waits above = 6.7s; remainder tuned to the
        # measured 18.05s Kokoro length (18.05 - 3.3 - 6.7 = 8.05)
        self.wait(8.05)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: parent's single 10-letter row -> two rows of 5
# letters (STRAW / BERRY split) to fit MAX_W, same word, same R highlight.
# measured audio: 17.88s
# --------------------------------------------------------------------------- #
class B05_SpelledOutFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        frame = panel(width=3.9, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        title = fit(T("Spell it out first:", color=PALETTE["ink"], font_size=24), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), Create(frame), run_time=0.5)
        self.wait(1.0)

        letters = list("STRAWBERRY")
        row1_letters = letters[:5]   # S T R A W
        row2_letters = letters[5:]  # B E R R Y

        def letter_row(chs):
            row = VGroup(*[
                token_chunk(ch, PALETTE["slate"] if ch != "R" else PALETTE["crimson"], font_size=18)
                for ch in chs
            ]).arrange(RIGHT, buff=0.1)
            if row.width > MAX_W:
                row.scale_to_fit_width(MAX_W)
            return row

        row1 = letter_row(row1_letters)
        row2 = letter_row(row2_letters)
        letter_rows = VGroup(row1, row2).arrange(DOWN, buff=0.18)

        caption = fit(T("every letter is now\nits own token", color=PALETTE["slate"],
                            font_size=16, line_spacing=1.2), MAX_W)

        count_box = panel(width=3.3, height=1.5, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        count_label = fit(T("MODEL'S COUNT", color=PALETTE["sage"], font_size=13, font=MONO), 2.9)
        count_number = T("3", color=PALETTE["sage"], font_size=34, font=MONO, weight="BOLD")
        count_content = VGroup(count_label, count_number).arrange(DOWN, buff=0.15)
        count_content.move_to(count_box.get_center())
        count_group = VGroup(count_box, count_content)

        checkmark = fit(T("✓ MATCHES TRUE\nCOUNT", color=PALETTE["sage"],
                             font_size=16, weight="BOLD", line_spacing=1.2), MAX_W)

        # The first draft chained 5 next_to() calls (title -> letter_rows ->
        # caption -> count_box -> checkmark) — a static pre-flight run found
        # an explicit resulting coordinate at y=-4.6, off the HARD bottom
        # edge (+/-4.0), not just outside the safe margin. Building every
        # piece first, THEN arranging the whole chain as one VGroup and
        # capping its total height via scale_to_fit_height (same proven
        # pattern as this file's B02/B04) guarantees it fits regardless of
        # any single element's assumed height.
        content_block = VGroup(letter_rows, caption, count_group, checkmark).arrange(DOWN, buff=0.35)
        if content_block.height > 5.5:
            content_block.scale_to_fit_height(5.5)
        content_block.next_to(title, DOWN, buff=0.35)

        self.play(FadeIn(letter_rows, shift=UP * 0.1), run_time=0.8)
        self.wait(1.5)

        self.play(FadeIn(caption), run_time=0.5)
        self.wait(1.5)

        # highlight the 3 R tokens across both rows — row1 has 1 R (index 2),
        # row2 has 2 R's (indices 2,3 of "BERRY") — built only AFTER the
        # final layout above, from each token's own true rendered position.
        r_boxes = VGroup(
            box_around(row1[2], buff=0.05, color=PALETTE["gold"]),
            box_around(row2[2], buff=0.05, color=PALETTE["gold"]),
            box_around(row2[3], buff=0.05, color=PALETTE["gold"]),
        )
        self.play(Create(r_boxes), run_time=0.5)
        self.wait(1.0)

        self.play(Create(count_box), FadeIn(count_content), run_time=0.5)
        self.wait(1.0)

        self.play(FadeIn(checkmark, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.2s, waits above = 6.0s; remainder tuned to the
        # measured 17.88s Kokoro length (17.88 - 3.2 - 6.0 = 8.68)
        self.wait(8.68)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: already single-column; card narrowed to fit MAX_W.
# measured audio: 18.55s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=24), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        questions = [
            "Is it a whole-word\ntask?",
            "Does it need\ncharacter-level detail?",
            "Would spelling it\nout help?",
        ]
        rows = VGroup()
        for q in questions:
            box = Square(side_length=0.35, stroke_color=PALETTE["slate"], stroke_width=3, fill_opacity=0)
            qtxt = fit(T(q, color=PALETTE["ink"], font_size=17, line_spacing=1.2), 2.9)
            row = VGroup(box, qtxt).arrange(RIGHT, buff=0.25, aligned_edge=UP)
            rows.add(row)
        rows.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        rows.move_to(ORIGIN)

        card = panel(width=3.9, height=5.6,
                     fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.18, opacity=0.0)
        card.set_stroke(width=2.5)
        card.move_to(rows.get_center())
        self.play(Create(card), run_time=0.4)
        self.wait(0.5)

        checks = []
        for row in rows:
            box = row[0]
            check = T("✓", color=PALETTE["sage"], font_size=22, weight="BOLD")
            check.move_to(box.get_center())
            checks.append(check)

        self.play(FadeIn(rows[0]), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(rows[1]), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(rows[2]), run_time=0.5)
        self.wait(2.0)
        self.play(*[Write(c) for c in checks], run_time=0.5)
        self.wait(1.0)

        closing = fit(T("That's tokenization\nin action.", color=PALETTE["slate"],
                            font_size=18, line_spacing=1.2), MAX_W)
        closing.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.3s (0.5+0.4+0.5+0.5+0.5+0.5+0.4), waits above = 8.5s
        # (1.0 + 0.5 + 2.0 + 2.0 + 2.0 + 1.0); remainder tuned to the measured
        # 18.55s Kokoro length (18.55 - 3.3 - 8.5 = 6.75)
        self.wait(6.75)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: already single-column; lines re-wrapped narrower.
# measured audio: 11.74s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("A model that writes\nfluent paragraphs and", color=PALETTE["bg"],
                          font_size=22, line_spacing=1.2), MAX_W)
        line2 = fit(T("a model that can't\ncount letters aren't\ncontradicting each other.",
                          color=PALETTE["sage"], font_size=20, line_spacing=1.2), MAX_W)
        line3 = fit(T("They're the same\nsystem, working at the\nwrong resolution for\nthe task you gave it.",
                          color=PALETTE["gold"], font_size=20, line_spacing=1.2), MAX_W)

        content = VGroup(line1, line2, line3).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame_w = min(content.width + 0.9, 3.95)
        frame = panel(width=frame_w, height=content.height + 1.3,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.25)
        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.5)
        self.wait(1.8)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.4)
        underline = Line(
            line3.get_corner(DL) + DOWN * 0.15, line3.get_corner(DR) + DOWN * 0.15,
            color=PALETTE["gold"], stroke_width=2,
        )
        self.play(Create(underline), run_time=0.1)
        # sum of plays = 1.65s, waits above = 3.3s; remainder tuned to the
        # measured 11.74s Kokoro length (11.74 - 1.65 - 3.3 = 6.79)
        self.wait(6.79)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s — a very short beat; kept deliberately simple.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=46), MAX_W)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with\nClaude Code", color=PALETTE["ink"],
                               font_size=26, line_spacing=1.2), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"],
                            font_size=22, line_spacing=1.25), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        frame_w = min(content.width + 1.0, 3.95)
        frame_h = min(content.height + 1.1, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.06)
