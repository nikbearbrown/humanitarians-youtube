"""
Manim scenes — 9:16 PORTRAIT SHORT derived from
2026-08-17-why-ai-generated-code-still-needs-a-human

Built via THE SHORTS LAW (runtime/scripts/shorts.py): this reel is UNDER the
180s Shorts cap, so the short is a full reformat — all 9 parent beats kept,
no narration rewritten, every mp3 reused byte-for-byte from the parent's
mp3/ folder (see short/beat_sheet.json). Every beat here is a Manim GRAPHIC
beat, so THE REFORMAT RULE's auto center-cut never applies (generated
graphics are never cropped) — each beat below is a genuine portrait
RE-LAYOUT of the parent ../scenes.py composition, authored by hand for a
1080x1920 canvas, not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect
(so the vertical safe/hard bounds the parent file already designed against
— to_edge(UP/DOWN, buff=...) — carry over almost unchanged). What changes
is frame_width: 4.5 instead of 14.222, i.e. a hard edge of only +/-2.25 and
a safe band of +/-1.95 (vs the parent's +/-6.3) — SEE
runtime/qc/manim_layout_audit.py's --portrait constants. That is roughly a
3.2x narrower stage. Every wide composition in the parent film — the B02
hook's fix.js/server.log split screen, B04's before/after SQL columns, and
B05's rubric-chips-beside-a-code-panel — is re-composed here as a TOP/BOTTOM
stack instead of LEFT/RIGHT columns, with code re-wrapped onto more, shorter
lines (measured against real Manim Text.width at 1080x1920 — see
BUILD-LOG.md's short-cut entry for the measurement method) rather than
shrunk-to-illegibility by fit()'s safety scaling alone.

MAX_W = 3.6 is this file's general content-width budget (leaves ~0.15
margin inside the portrait safe half-width of 1.95 on each side); code
panels use a tighter ~3.2-3.4. fit() remains the same safety net as the
parent file — most lines below were pre-measured to already clear budget,
so fit() is mostly a no-op backstop, not the primary sizing tool.

clear_of_hdivider() is this file's portrait analogue of the parent's
clear_of_divider(): the same "measure the block's OWN rendered bounds and
shift the whole rigid unit" pattern that fixed the parent's B02 divider bug,
just rotated 90 degrees — every vertical divider (LEFT/RIGHT split) in the
parent becomes a horizontal divider (TOP/BOTTOM stack) here, so it is the
block's top/bottom clearance, not its left/right clearance, that has to be
verified against the divider's position.

Beat-by-beat redesign notes:
  B00 TitleCard      — title re-wrapped 2->4 lines for the narrow column.
  B01 ExecSummary    — badge+name row (side-by-side in the parent) stacked
                       badge-above-name; summary re-wrapped 3->5 short lines.
  B02 HookCrashLog   — THE hook's fix.js/server.log split screen -> fix.js
                       on top, server.log on the bottom, divided by a fixed
                       horizontal rule (clear_of_hdivider protects both
                       blocks from it, mirroring the parent's vertical case).
  B03 FrameworkRubric— each row's badge+label mini-header now sits ABOVE its
                       (full-width) explanation instead of beside a
                       width-starved one.
  B04 WorkedExampleDiff — THE worked example's before/after SQL columns ->
                       BEFORE code panel on top, AFTER panel crossfades in
                       at the exact same anchor once the WHY step needs it
                       (fits inside the existing 0.5s step-transition, so
                       total beat timing is unchanged), separated from the
                       caption zone below by a fixed horizontal divider.
  B05 FalsifiabilityCase — THE falsifiability beat's rubric-chips-beside-
                       code-panel -> chips column ABOVE the code panel.
  B06 ScaffoldedTask — same box+text-column row structure as the parent
                       (already vertical friendly); only the checklist/
                       explanation text is re-wrapped narrower.
  B07 Close          — the checkmark that sat to the RIGHT of the struck
                       old line now sits beside the NEW corrected line
                       instead (old line stacked above, both narrower).
  B08 BrandOutro     — unchanged composition; only widths/rule length trimmed.

Palette/MONO/fit()/panel() are copied verbatim from the parent ../scenes.py
for visual continuity (same humanitarians/hai persona look). See
../scenes.py for the full production history (v1-v4) of this content —
nothing about WHAT is said or WHEN changes here, only how it is laid out.
"""

from manim import *

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the
# pixel aspect ratio ONCE, inside ManimConfig.digest_parser() at startup —
# BEFORE the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait — every
# coordinate in this file was designed against a 4.5-wide frame, so without
# this fix everything renders ~3.2x too small and clustered dead-center
# (the actual root cause of this short's first GATE V pass: 5-19%
# canvas-fill on nearly every beat). This mirrors what
# runtime/qc/manim_layout_audit.py's --portrait mode already does by hand
# for its own dry-run stub — just applied here at real-render time, after
# -r has set config.pixel_width/pixel_height (module import happens after
# manim's CLI arg-parsing, so this always sees the real portrait pixels).
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
                          # (cream): measures 7.67:1 there but a genuinely
                          # broken 1.56:1 on "ink" (verified via the same
                          # contrast() math as runtime/qc/wcag_margin_check.py
                          # -- both colors are dark, so a dark-on-dark beat
                          # using "teal" text reads as nearly invisible; a
                          # real GATE V frame extraction on this short's
                          # B07_Close caught it, see BUILD-LOG.md).
    "teal_on_ink": "#5FB8CC",  # same hue family, lightened for ink
                          # backgrounds specifically (6.23:1 on "ink") --
                          # use this, never "teal", for teal text/labels in
                          # any scene whose camera.background_color is ink
                          # (B04, B07 here).
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


def panel(width, height, fill=None, stroke=None, corner_radius=0.12, opacity=1.0):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        fill_color=fill or PALETTE["ink"], fill_opacity=opacity,
        stroke_color=stroke or PALETTE["slate"], stroke_width=2,
    )


def clear_of_hdivider(block, divider_y, side, margin=0.35):
    """Portrait analogue of the parent scenes.py's clear_of_divider() — same
    pattern (measure the block's OWN rendered bounds, shift the whole rigid
    unit by the real overhang, never a per-line rescale), rotated 90
    degrees: every side-by-side split in the parent (a vertical divider with
    LEFT/RIGHT panels) becomes a top/bottom stack in this narrow 1080x1920
    frame (a horizontal divider with TOP/BOTTOM panels), because portrait
    has ~3.2x less width to spend on columns.

    side="top"    -> block sits ABOVE the divider; keeps get_bottom()[1] >=
                      divider_y + margin.
    side="bottom" -> block sits BELOW the divider; keeps get_top()[1] <=
                      divider_y - margin.
    No-op (returns unchanged) if the block already clears the margin.
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
# B00 — TITLE: silent opening card. Same idiom as the parent (top rule /
# title / bottom rule / handle, gold accent, centered) — title re-wrapped
# from 2 wide lines to 4 narrow ones for the portrait column; timing
# unchanged (still a fixed 4.5s silent target, see parent docstring).
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = [
            "Why AI-Generated Code",
            "Still Needs a Human",
            "Who Understands",
            "the System",
        ]
        title = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
            for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        # buff=0.85 (not the ~0.5 that would look "normal") is deliberate —
        # same GATE V canvas-fill lesson as the parent B00_TitleCard's own
        # buff=1.0 fix, but portrait needs it doubly: this card's few
        # elements have to spend the tall safe area (6.8 units) on spacing
        # since there's no width left to spend it on (title is already ~92%
        # of safe width). Measured via real Manim metrics before rendering
        # at ~61% canvas coverage (was 47% at buff=0.6 — a real GATE V MAJOR
        # underfill on the first render of this beat, see BUILD-LOG.md).
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=0.85
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        self.wait(2.9)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card. Parent's badge+name ROW
# (side by side) becomes a badge-ABOVE-name COLUMN here — a 3.3-wide name
# next to a 0.9-wide badge would have squeezed the name well past budget;
# stacking gives the name its own full-width line. Summary re-wrapped from
# 3 long lines to 5 short ones. Timing identical to the parent (measured
# 11.04s Kokoro track).
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.42, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = Text("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(Text("Sai Pranavi J.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        role = fit(Text("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)

        # NEW v-short layout: badge stacked ABOVE the name/role block (the
        # parent's badge+name arranged RIGHT would have starved the 3.3-wide
        # name of width next to a 0.9-wide badge).
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: why a fix that",
            "looks right isn't always a",
            "fix that's actually right",
            "-- and the 3 questions to",
            "ask before you trust one.",
        ]
        summary = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=22), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.15)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(
            DOWN, buff=0.5
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # retimed 2026-10-20: narration shortened to 10.61s ("Sai Pranavi J."
        # retrofit, was 11.04s) — shifted this hold by the same -0.43s delta.
        self.wait(8.81)


# --------------------------------------------------------------------------- #
# B02 — HOOK: THE split-screen redesign. Parent: fix.js (left) vs.
# server.log (right), divided by a VERTICAL rule at x=0. Here: fix.js on
# TOP, server.log on the BOTTOM, divided by a HORIZONTAL rule at y=0 —
# clear_of_hdivider() protects both blocks exactly as the parent's
# clear_of_divider() protected the left/right code blocks (same real-bounds-
# measured shift, just on the y axis). Code re-wrapped from 4/5 wide lines
# to 6/7 narrow ones (measured against real Text.width at 1080x1920 — see
# BUILD-LOG.md). Timing identical to the parent (4.66s).
# --------------------------------------------------------------------------- #
class B02_HookCrashLog(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        top_header = fit(Text("fix.js", color=PALETTE["sage"], font_size=18, font=MONO), 2.4)
        top_lines = [
            "const q = `INSERT",
            "  INTO items",
            "  VALUES ('${title",
            "    .replace(/'/g,",
            "      \"''\")}')`;",
            "db.query(q);",
        ]
        top_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=15, font=MONO), 3.2)
            for l in top_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        top_block = VGroup(top_header, top_code).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        top_block.to_edge(UP, buff=0.68)
        top_block.to_edge(LEFT, buff=0.45)

        bottom_header = fit(Text("server.log", color=PALETTE["sage"], font_size=18, font=MONO), 2.4)
        bottom_data = [
            ("ERROR: syntax error", PALETTE["crimson"]),
            ("  at or near \"s\"", PALETTE["crimson"]),
            ("LINE 1: INSERT INTO", PALETTE["crimson"]),
            ("  items", PALETTE["crimson"]),
            ("  VALUES ('O'Brien''s", PALETTE["crimson"]),
            ("  Deli')", PALETTE["crimson"]),
            ("FATAL: insert aborted", PALETTE["crimson"]),
        ]
        bottom_code = VGroup(*[
            fit(Text(l, color=c, font_size=14, font=MONO), 3.2) for l, c in bottom_data
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        bottom_block = VGroup(bottom_header, bottom_code).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        bottom_block.to_edge(DOWN, buff=0.68)
        bottom_block.to_edge(LEFT, buff=0.45)

        divider_y = 0.0
        divider = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["slate"], stroke_width=2).move_to([0, divider_y, 0])

        # the protection: measured against each block's OWN rendered bounds,
        # not a guessed constant (the exact lesson of the parent's v3.1 fix)
        clear_of_hdivider(top_block, divider_y, side="top", margin=0.3)
        clear_of_hdivider(bottom_block, divider_y, side="bottom", margin=0.3)

        self.play(
            Create(divider), FadeIn(top_header, shift=UP * 0.1), FadeIn(bottom_header, shift=UP * 0.1),
            run_time=0.35,
        )
        self.play(
            LaggedStart(
                *[FadeIn(l, shift=RIGHT * 0.1) for l in top_code],
                *[FadeIn(l, shift=RIGHT * 0.1) for l in bottom_code],
                lag_ratio=0.08,
            ),
            run_time=0.85,
        )
        self.wait(1.5)

        # highlighter box on the actual crash line (bottom_code[0] =
        # "ERROR: syntax error" — the same line the parent boxes)
        err_box = Rectangle(
            width=bottom_code[0].width + 0.2, height=bottom_code[0].height + 0.12,
            stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
        ).move_to(bottom_code[0].get_center())
        self.play(Create(err_box), run_time=0.3)
        self.wait(1.66)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: the 3-question rubric. Parent's badge+label sat beside a
# width-starved description; here each row's badge+label mini-header sits
# ABOVE its (now full-width) explanation, so the actual sentences get the
# whole 3.6-wide column instead of ~2.2 beside a badge. Timing identical to
# the parent (measured 21.74s Kokoro track, split proportionally per row).
# --------------------------------------------------------------------------- #
class B03_FrameworkRubric(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The 3 Questions", "Before You Trust a Fix"]
        title = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=26), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.15)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)

        intro_lines = ["Before you trust it,", "ask yourself all three."]
        intro = VGroup(*[
            fit(Text(l, color=PALETTE["slate"], font_size=20), MAX_W) for l in intro_lines
        ]).arrange(DOWN, buff=0.1)
        intro.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(intro, shift=UP * 0.1), run_time=0.4)
        self.wait(2.71)
        self.play(FadeOut(intro, shift=UP * 0.1), run_time=0.3)

        rows_data = [
            ("1", "TRACE",
             ["Point to the exact execution", "path this change touches --", "not just read what's different."]),
            ("2", "CONSEQUENCE",
             ["Know what breaks -- silently --", "if this turns out to be wrong."]),
            ("3", "WHY, NOT JUST WHAT",
             ["Explain why this is the fix in", "terms of what the system does --", "not that it looks right."]),
        ]

        rows = VGroup()
        for num, label, desc_lines in rows_data:
            badge = Circle(radius=0.3, color=PALETTE["teal"], fill_color=PALETTE["teal"], fill_opacity=0.15, stroke_width=2.5)
            badge_num = Text(num, color=PALETTE["teal"], font_size=20, font=MONO).move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)

            label_txt = fit(Text(label, color=PALETTE["slate"], font_size=18, font=MONO), 3.0)
            top_row = VGroup(badge_group, label_txt).arrange(RIGHT, buff=0.25)

            desc_txt = VGroup(*[
                fit(Text(l, color=PALETTE["ink"], font_size=17, line_spacing=1.0), MAX_W) for l in desc_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

            # NEW: badge+label sits ABOVE the full-width description
            # (parent arranged badge/label BESIDE the description).
            row = VGroup(top_row, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        if rows.width > MAX_W:
            rows.scale_to_fit_width(MAX_W)
        if rows.height > 5.2:
            rows.scale_to_fit_height(5.2)
        rows.move_to(ORIGIN).shift(UP * 0.05)

        # SKELETON FIRST — same law as the parent: all 3 mini-headers land
        # before any explanation streams in.
        for r in rows:
            self.play(FadeIn(r[0], shift=UP * 0.12), run_time=0.15)

        row_holds = [5.05, 2.92, 6.38]
        for row, hold in zip(rows, row_holds):
            desc_txt = row[1]
            self.play(FadeIn(desc_txt, shift=UP * 0.1), run_time=0.3)
            self.wait(hold)

        not_two = fit(Text(
            "not two, not one -- all three.", color=PALETTE["crimson"], font_size=20
        ), MAX_W)
        not_two.to_edge(DOWN, buff=0.68)
        self.play(Write(not_two), run_time=0.5)
        self.wait(1.63)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: THE big redesign. Parent shows BEFORE (left column)
# and AFTER (right column) simultaneously for the whole 44s beat. Portrait
# has no width for two simultaneous columns of 8+ code lines each, so this
# beat is genuinely re-composed as a SEQUENTIAL single-panel reveal: the
# BEFORE panel occupies the (single) code slot for SETUP/TRACE/CONSEQUENCE
# (all three narrate the before_code), then crossfades to the AFTER panel
# for the WHY step (which narrates the after_code) — landing at the exact
# same anchor, so the swap reads as a clean substitution, not a jump cut.
# The crossfade is folded into the WHY step's existing 0.5s caption
# transition, so total beat timing is UNCHANGED from the parent (43.99s).
# A fixed horizontal divider still separates the code area from the
# caption zone below it — clear_of_hdivider() protects the code panels
# from it (the portrait analogue of the parent's vertical-divider fix).
#       [GENERIC EXAMPLE — see FACTCHECK.md — never attribute to a real repo]
# --------------------------------------------------------------------------- #
class B04_WorkedExampleDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        header_lines = ["illustrative example --", "a generic before/after pattern"]
        header = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=15, font=MONO), MAX_W) for l in header_lines
        ]).arrange(DOWN, buff=0.08)
        header.to_edge(UP, buff=0.68)
        self.play(Write(header), run_time=0.4)

        # ---- BEFORE panel (shown first) ----
        before_label = fit(Text("BEFORE -- hand-escaped", color=PALETTE["crimson"], font_size=15, font=MONO), MAX_W)
        before_lines = [
            "const q = `INSERT",       # [0]
            "  INTO items",            # [1]
            "  VALUES ('${title",      # [2]
            "    .replace(/'/g,",      # [3]
            "      \"''\")}',",        # [4]
            "  '${desc}',",            # [5]
            "  ${price})`;",           # [6]
            "db.query(q);",            # [7]
        ]
        before_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=14, font=MONO), 3.2) for l in before_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        before_col = VGroup(before_label, before_code).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        before_col.next_to(header, DOWN, buff=0.4)
        before_col.to_edge(LEFT, buff=0.5)

        # ---- AFTER panel (crossfades in at the SAME anchor for the WHY step) ----
        after_label = fit(Text("AFTER -- parameterized", color=PALETTE["teal_on_ink"], font_size=15, font=MONO), MAX_W)
        after_lines = [
            "const q = `INSERT",              # [0]
            "  INTO items",                    # [1]
            "  VALUES ($1, $2, $3)`;",         # [2]
            "db.query(q, [title,",             # [3]
            "  desc, price]);",                # [4]
        ]
        after_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=14, font=MONO), 3.2) for l in after_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        after_col = VGroup(after_label, after_code).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        after_col.next_to(header, DOWN, buff=0.4)
        after_col.to_edge(LEFT, buff=0.5)

        divider_y = -1.1
        divider = Line([-1.8, divider_y, 0], [1.8, divider_y, 0], color=PALETTE["slate"], stroke_width=2)

        # protection: keep whichever code panel is on screen clear of the
        # divider above the caption zone (mirrors the parent's v3.1 fix,
        # rotated onto the y axis — see clear_of_hdivider()'s docstring)
        clear_of_hdivider(before_col, divider_y, side="top", margin=0.3)
        clear_of_hdivider(after_col, divider_y, side="top", margin=0.3)

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(before_col, shift=UP * 0.1), run_time=0.8)
        self.wait(0.3)

        def box_around(mob, buff=0.1):
            r = Rectangle(
                width=mob.width + 2 * buff, height=mob.height + 2 * buff,
                stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
            )
            r.move_to(mob.get_center())
            return r

        highlight = box_around(VGroup(before_code[0], before_code[1]))
        self.play(Create(highlight), run_time=0.3)

        caption_zone = VGroup()

        def show_step(tag, body_lines, color, t_hold, focus, swap_to=None):
            """body_lines: pre-wrapped short lines (measured <=3.25 wide at
            font_size 15, well inside MAX_W). swap_to: if given (WHY step
            only), the before_col->after_col crossfade is folded into this
            same 0.5s transition so total beat timing stays unchanged."""
            nonlocal caption_zone
            tag_txt = Text(tag, color=color, font_size=16, font=MONO)
            body_col = VGroup(*[
                fit(Text(l, color=PALETTE["sage"], font_size=15), MAX_W) for l in body_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            step = VGroup(tag_txt, body_col).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            if step.width > MAX_W:
                step.scale_to_fit_width(MAX_W)
            step.to_edge(DOWN, buff=0.68)
            step.to_edge(LEFT, buff=0.45)   # pin the LEFT edge too — arrange's
            # aligned_edge only matched tag/body to EACH OTHER, not to a safe
            # x; without this the (short) tag anchors near x=0 and the wider
            # body text runs off the right edge — the exact class of bug the
            # parent's clear_of_divider() exists to catch, just on this axis.

            new_highlight = box_around(focus)
            anims = [Transform(highlight, new_highlight)]
            if swap_to is not None:
                anims += [FadeOut(before_col), FadeIn(swap_to)]
            if len(caption_zone) == 0:
                self.play(FadeIn(step, shift=UP * 0.15), *anims, run_time=0.5)
            else:
                self.play(FadeOut(caption_zone), FadeIn(step, shift=UP * 0.15), *anims, run_time=0.5)
            caption_zone = step
            self.wait(t_hold)

        # holds tuned to the measured 43.99s Kokoro audio — identical values
        # to the parent (see BUILD-LOG.md); only the on-screen composition
        # changed, not the pacing.
        show_step(
            "SETUP:",
            ["this insert escapes single quotes by",
             "hand before the value ever reaches the",
             "database"],
            PALETTE["gold"], 6.28,
            VGroup(before_code[0], before_code[1]),
        )
        show_step(
            "TRACE:",
            ["every value gets wrapped in quotes and",
             "dropped straight into the SQL string --",
             "that's the exact line that runs"],
            PALETTE["teal_on_ink"], 6.94,
            VGroup(before_code[3], before_code[4]),
        )
        show_step(
            "CONSEQUENCE:",
            ["escaping only handles apostrophes -- a",
             "backslash, a null byte, an unexpected",
             "encoding all slip through, and one bad",
             "row aborts the entire batch, not just",
             "itself"],
            PALETTE["crimson"], 9.92,
            VGroup(before_code[3], before_code[4]),
        )
        show_step(
            "WHY:",
            ["parameterized values are bound",
             "separately from the query -- there's no",
             "string for a stray character to break",
             "out of. Not a patch on the symptom --",
             "the failure mode itself is gone."],
            PALETTE["teal_on_ink"], 16.85,
            VGroup(after_code[2], after_code[3], after_code[4]),
            swap_to=after_col,
        )


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: trivial date-formatter, "LOW STAKES". Parent puts
# the rubric-chips column BESIDE the code panel; here the (already-vertical)
# chips column sits ABOVE the code panel instead — direct top/bottom
# restack of the same two elements, no new composition needed. fn code
# re-wrapped 3->4 lines (the return statement was too wide for one line).
# Timing identical to the parent (measured 9.91s Kokoro track).
# --------------------------------------------------------------------------- #
class B05_FalsifiabilityCase(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Does this need the", "same scrutiny?"]
        title = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=24), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.12)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.4)

        chip_labels = ["TRACE", "CONSEQUENCE", "WHY"]
        chips = VGroup(*[
            VGroup(
                RoundedRectangle(width=1.9, height=0.4, corner_radius=0.08,
                                 fill_color=PALETTE["slate"], fill_opacity=0.12,
                                 stroke_color=PALETTE["slate"], stroke_width=1.5),
                Text(lbl, color=PALETTE["slate"], font_size=14, font=MONO),
            )
            for lbl in chip_labels
        ])
        for grp in chips:
            grp[1].move_to(grp[0].get_center())
        chips.arrange(DOWN, buff=0.18)

        rubric_caption = fit(Text("the rubric", color=PALETTE["ink"], font_size=16), 1.8)
        rubric_caption.next_to(chips, UP, buff=0.15)
        top_group = VGroup(rubric_caption, chips)

        # NEW: the chips column sits ABOVE the code panel (parent placed it
        # to the LEFT of the panel) — same two elements, top/bottom restack.
        code_panel = panel(width=3.3, height=1.55, fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fn_lines = [
            "function formatDate(d) {",
            "  return d.toISOString()",
            "    .slice(0, 10);",
            "}",
        ]
        fn_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=14, font=MONO), 3.0) for l in fn_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        fn_code.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, fn_code)

        low_stakes = fit(Text("LOW STAKES", color=PALETTE["teal"], font_size=18, font=MONO), 2.2)
        check = Text("check", color=PALETTE["teal"], font_size=18, font=MONO)
        stakes_row = VGroup(check, low_stakes).arrange(RIGHT, buff=0.2)

        body = VGroup(top_group, code_group, stakes_row).arrange(DOWN, buff=0.35)
        body.move_to(ORIGIN).shift(UP * 0.25)

        self.play(
            FadeIn(rubric_caption), LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.15),
            run_time=0.6,
        )
        self.play(Create(code_panel), FadeIn(fn_code), run_time=0.6)
        self.wait(0.3)

        self.play(FadeIn(check), Write(low_stakes), run_time=0.5)
        self.wait(0.4)

        closing_lines = ["quick trust is fine here --", "the rubric scales with", "what breaks"]
        closing = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=16), MAX_W) for l in closing_lines
        ]).arrange(DOWN, buff=0.1)
        closing.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.5)
        self.wait(6.41)


# --------------------------------------------------------------------------- #
# B06 — CTA: the literal 3-step checklist. This composition (a checkbox
# beside a text column, rows stacked DOWN) was already portrait-friendly —
# no split-screen to redesign — so only the checklist/explanation text is
# re-wrapped for the narrower column (3 wide lines -> 4-5 short ones per
# step). Timing identical to the parent (measured 26.38s Kokoro track).
# --------------------------------------------------------------------------- #
class B06_ScaffoldedTask(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Before you merge that fix:", color=PALETTE["ink"], font_size=22
        ), MAX_W)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.3)
        self.wait(1.62)

        steps_data = [
            (['1. Ask: "what', "specifically breaks", "if this is wrong,", "and how would I", 'know?"'],
             ["don't accept a vague answer"]),
            (["2. Trace the one", "function/file it", "touches, by hand,", "for 60 seconds."],
             ["a quick check, not a full", "audit"]),
            (["3. Write one", "sentence explaining", "why this fixes the", "root cause -- not", "just what changed."],
             ["can't write it? you don't", "understand the fix yet"]),
        ]

        rows = VGroup()
        for main_lines, explain_lines in steps_data:
            box = Square(side_length=0.26, color=PALETTE["slate"], stroke_width=2.5)
            main_txt = VGroup(*[
                fit(Text(l, color=PALETTE["ink"], font_size=16, font=MONO), 3.0) for l in main_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            explain_txt = VGroup(*[
                fit(Text(l, color=PALETTE["slate"], font_size=14), 3.0) for l in explain_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
            text_col = VGroup(main_txt, explain_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            row = VGroup(box, text_col).arrange(RIGHT, buff=0.28, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        if rows.width > MAX_W:
            rows.scale_to_fit_width(MAX_W)
        if rows.height > 5.0:
            rows.scale_to_fit_height(5.0)
        rows.move_to(ORIGIN).shift(UP * 0.1)

        # SKELETON FIRST — identical law to the parent: box+main text lands
        # per step before that step's explanation streams in.
        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.2)

        step_holds = [6.22, 5.96, 4.33]
        for row, hold in zip(rows, step_holds):
            explain_txt = row[1][1]
            self.play(FadeIn(explain_txt, shift=UP * 0.08), run_time=0.3)
            self.wait(hold)

        zinger_lines = ["can't write that sentence?", "neither did the tool."]
        zinger = VGroup(*[
            fit(Text(l, color=PALETTE["crimson"], font_size=17), MAX_W) for l in zinger_lines
        ]).arrange(DOWN, buff=0.08)
        zinger.to_edge(DOWN, buff=0.68)
        self.play(Write(zinger), run_time=0.5)
        self.wait(5.96)


# --------------------------------------------------------------------------- #
# B07 — CLOSE: callback to B02's crash log, now corrected. Parent puts the
# "check" mark to the RIGHT of the (single-line) old_line; here old_line is
# itself 2 lines, so check now sits beside the NEW corrected line instead —
# same beat, same callback, narrower single-column flow. Timing identical
# to the parent (measured 7.49s Kokoro track).
# --------------------------------------------------------------------------- #
class B07_Close(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        header_lines = ["server.log --", "production"]
        header = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=16, font=MONO), MAX_W) for l in header_lines
        ]).arrange(DOWN, buff=0.08)
        header.move_to([0, 3.0, 0])
        self.play(FadeIn(header), run_time=0.3)

        old_lines = ["ERROR: syntax error at", 'or near "s"']
        old_block = VGroup(*[
            fit(Text(l, color=PALETTE["crimson"], font_size=14, font=MONO), MAX_W) for l in old_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        old_block.next_to(header, DOWN, buff=0.45)
        strike = Line(old_block.get_left(), old_block.get_right(),
                      color=PALETTE["crimson"], stroke_width=2).move_to(old_block.get_center())
        strike._qc_intentional = True  # deliberate strike-through over corrected text

        self.play(FadeIn(old_block), run_time=0.25)
        self.play(Create(strike), run_time=0.25)

        # teal_on_ink, not "teal" — this scene's background is ink, and
        # plain "teal" measures an unreadable 1.56:1 there (see PALETTE's
        # own comment; caught by a real GATE V frame extraction on this
        # exact beat, see BUILD-LOG.md).
        new_lines = ["OK: parameterized insert --", "1 row committed"]
        new_block = VGroup(*[
            fit(Text(l, color=PALETTE["teal_on_ink"], font_size=14, font=MONO), MAX_W) for l in new_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        check = Text("check", color=PALETTE["teal_on_ink"], font_size=16, font=MONO)
        fix_row = VGroup(check, new_block).arrange(RIGHT, buff=0.25, aligned_edge=UP)
        fix_row.next_to(old_block, DOWN, buff=0.45)

        self.play(FadeIn(check, scale=1.3), run_time=0.25)
        self.play(FadeIn(new_block, shift=UP * 0.1), run_time=0.3)
        self.wait(0.2)

        statement_lines = ["The code that looks right", "and the code that is right",
                           "aren't always the same thing."]
        statement = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=20), MAX_W) for l in statement_lines
        ]).arrange(DOWN, buff=0.14)
        statement.next_to(fix_row, DOWN, buff=0.6)
        self.play(FadeIn(statement), run_time=0.5)
        self.wait(0.2)

        gap_lines = ["that gap is where you're", "still the one doing the job."]
        gap_line = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=18), MAX_W) for l in gap_lines
        ]).arrange(DOWN, buff=0.1)
        gap_line.next_to(statement, DOWN, buff=0.5)
        highlight = Rectangle(
            width=gap_line.width + 0.3, height=gap_line.height + 0.2,
            fill_color=PALETTE["gold"], fill_opacity=0.15, stroke_width=0,
        ).move_to(gap_line.get_center())
        self.play(FadeIn(highlight), FadeIn(gap_line), run_time=0.5)
        self.wait(4.74)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, in for Sai Pranavi J.. Same
# centered composition as the parent; only the rule length and the tagline
# wrap (1 line -> 2) change for the narrower column. Timing identical to
# the parent (measured 4.92s Kokoro track).
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=36), MAX_W)
        accent = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        tagline_lines = ["in for Sai Pranavi J."]
        tagline = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=24), MAX_W) for l in tagline_lines
        ]).arrange(DOWN, buff=0.18)
        # buff 1.8->2.3 (2026-10-20): the "Sai Pranavi J." retrofit shortened
        # the tagline from 2 lines to 1, dropping real measured canvas-fill
        # to 53% (just under the 55% floor) — raised buff for real coverage,
        # not just to appease the checker.
        VGroup(handle, accent, tagline).arrange(DOWN, buff=2.3).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.1, tagline.get_corner(DR) + DOWN * 0.1
        )
        self.play(Create(tagline_underline), run_time=0.3)
        # retimed 2026-10-20: narration shortened to 4.46s ("Sai Pranavi J."
        # retrofit, was 4.92s) — shifted this hold by the same -0.46s delta.
        self.wait(2.66)
