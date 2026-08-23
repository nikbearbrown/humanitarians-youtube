"""
Manim scenes for 2026-08-17-why-ai-generated-code-still-needs-a-human

v3 (2026-08-17): fellow watched v2 (119.03s) and requested two changes —
(1) a new SILENT title-card opening beat (no narration) before the hook,
    since v1/v2 dove straight into the crash log with no title/branding
    intro; (2) the Trace question's on-screen caption reworded
    ("not just read the diff" -> "not just read what's different") to
    match the narration fix (fellow found "diff" jargon unclear).
All 7 pre-existing beats renamed B00-B06 -> B01-B07 to make room for the
new B00 title card. Content unchanged except the Trace caption in
B02_FrameworkRubric (see that class for the exact fix).

B00_TitleCard        — silent title card: video title + @HumanitariansAI (TITLE, NEW)
B01_HookCrashLog     — split screen: escaped-quotes diff vs. crash log (HOOK)
B02_FrameworkRubric  — the 3-question rubric, Trace / Consequence / Why (FRAMEWORK)
B03_WorkedExampleDiff— hand-escaped SQL insert vs. parameterized-query fix (WORKED-EXAMPLE)
B04_FalsifiabilityCase — trivial date-formatter, "LOW STAKES" (FALSIFIABILITY)
B05_ScaffoldedTask   — the literal 3-step viewer checklist (CTA)
B06_Close            — callback to B01's crash log, now corrected (CLOSE)
B07_BrandOutro       — @HumanitariansAI sign-off (SIGN-OFF)

IMPORTANT (see FACTCHECK.md / SOURCES.md): the B03 worked example is a
GENERIC, illustrative code pattern (a hand-escaped SQL insert vs. a
parameterized-query fix). It is deliberately NOT attributed to any real
company, repo, or incident — do not add real names to this file.

All 8 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette: humanitarians (runtime/remotion/src/tokens/humanitarians.ts) — this
reel uses the hai/Bella persona, not the Claude-branded palette. Convention
copied from this fellow's sibling reel
(2026-07-26-recovering-the-silently-dropped-filings/scenes.py): plain Text
(Pango) throughout, never Integer/DecimalNumber/MathTex — this machine has
no LaTeX installed and Manim equation beats are blocked (irrelevant here,
since this reel has no math).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's
*measured* Kokoro audio duration (beat_sheet.json -> actual_duration_s),
not the pre-audio estimate — the audio-first pipeline conforms video to
audio by center-cutting or slow-fitting the rendered clip to the measured
mp3 length (runtime/scripts/compile.py). Measured durations came in well
under the pre-audio estimates (fast narration), so scenes here are built
compact rather than padded, to avoid the compiler needing to trim into
real content. B00 is the one exception: it carries no narration at all
(narration_text: "" in beat_sheet.json), so its duration is a fixed
silent-beat target (4.5s) rather than a measured Kokoro length — see
B00_TitleCard's own docstring and the beat_sheet.json shot.note for why
(compile.py's build_master_audio() needs a REAL audio file — even silent —
at every beat's audio_file path, or the entire film's narration falls back
to silence; a bare `null` breaks that all-beats-exist check).
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


def panel(width, height, fill=None, stroke=None, corner_radius=0.12, opacity=1.0):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        fill_color=fill or PALETTE["ink"], fill_opacity=opacity,
        stroke_color=stroke or PALETTE["slate"], stroke_width=2,
    )


def clear_of_divider(block, divider_x, side, margin=0.35):
    """Shift `block` (a VGroup/Mobject) so it keeps real clearance from a
    vertical divider at x=divider_x, measured from the block's OWN rendered
    bounds (get_left()/get_right()) rather than trusting whatever fixed
    coordinate + max-width cap it was built with.

    v3.1 (2026-08-17) fix: B01_HookCrashLog's left code block was positioned
    by centering its header at a fixed x and left-aligning the code lines to
    that header's left edge, capped only by a generous fit() max-width (5.6)
    that was never actually checked against the divider's position. The
    longest line ("const q = `INSERT INTO items") rendered at width 4.14,
    landing its right edge at x=+0.11 — past the divider at x=0 — so the
    divider visibly crossed through the tail of "items". A wider fit() cap
    doesn't fix this (it only shrinks a mobject that EXCEEDS the cap; it was
    already under 5.6) and per-line shrinking would mismatch that one line's
    font size against its neighbors. Shifting the whole header+code block as
    one unit — by an amount computed from its actual measured edge, not a
    guessed constant — guarantees clearance regardless of future edits to
    line content, and preserves a single consistent font size throughout.

    side="left"  -> block sits left of the divider; keeps get_right() <=
                    divider_x - margin.
    side="right" -> block sits right of the divider; keeps get_left() >=
                    divider_x + margin.
    No-op (returns unchanged) if the block already clears the margin.
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
# NEW 2026-08-17 (v3, fellow request) — v1/v2 dove straight into B01's crash
# log with zero title/branding intro. Style reuses the sibling reel's brand
# card (2026-07-26-recovering-the-silently-dropped-filings/scenes.py
# B06_BrandOutro): centered VGroup, gold accent rule, handle in slate.
# Silent-beat duration: see the file-level docstring + beat_sheet.json
# shot.note for why this is a fixed 4.5s target, not a measured Kokoro
# length (there is no narration to measure — narration_text is "").
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # Title wrapped onto two lines by hand (11 words / 64 chars — too
        # long for one legible line at a title-card size), each line fit to
        # the safe width rather than shrunk to an arbitrary font size.
        # Sized up + bracketed by a rule above AND below (not just one
        # underline) so a title-only/handle-only card still uses a real
        # share of the safe frame instead of a small cluster at center
        # (GATE V canvas-fill law caught the first draft at 25% fill).
        title_line1 = fit(Text(
            "Why AI-Generated Code Still Needs",
            color=PALETTE["ink"], font_size=50, weight="BOLD",
        ), 12.0)
        title_line2 = fit(Text(
            "a Human Who Understands the System",
            color=PALETTE["ink"], font_size=50, weight="BOLD",
        ), 12.0)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=38)

        # buff=1.0 (not the usual ~0.4-0.5) is deliberate: a title-only card
        # has just 3 elements, so real canvas-fill (GATE V's 55% floor) has
        # to come from spacing, not word count — measured offline against
        # the real manim metrics (not the render-free stub) at ~63% fill.
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.0
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        # bottom rule + handle land together, one beat — a title card reveal,
        # not a race of separate steps
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # everything settled well before the mid-beat QC sample point; the
        # remainder is a clean static hold — tuned to the real measured
        # silent-track length (4.55s, mp3/beat-B00.mp3) so the manim clip
        # needs no compile-time retime/slow-mo to conform to the beat.
        self.wait(2.9)


# --------------------------------------------------------------------------- #
# B01 — HOOK: split screen, escaped-quotes diff (left) vs. crash log (right)
# measured audio: 4.66s (unchanged from v2's B00 — renamed only)
# --------------------------------------------------------------------------- #
class B01_HookCrashLog(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        divider = Line(UP * 3.4, DOWN * 3.4, color=PALETTE["slate"], stroke_width=2)

        left_header = fit(Text("fix.js", color=PALETTE["sage"], font_size=20, font=MONO), 5.6)
        left_header.move_to([-3.6, 3.2, 0])

        left_lines = [
            "const q = `INSERT INTO items",
            "  VALUES ('${title",
            "    .replace(/'/g, \"''\")}')`;",
            "db.query(q);",
        ]
        left_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=16, font=MONO), 5.6)
            for l in left_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        left_code.next_to(left_header, DOWN, buff=0.35).align_to(left_header, LEFT)

        right_header = fit(Text("server.log", color=PALETTE["sage"], font_size=20, font=MONO), 4.4)
        right_header.move_to([2.9, 3.2, 0])

        right_lines = [
            ("ERROR: syntax error", PALETTE["crimson"]),
            ("  at or near \"s\"", PALETTE["crimson"]),
            ("LINE 1: INSERT INTO items", PALETTE["crimson"]),
            ("  VALUES ('O'Brien''s Deli')", PALETTE["crimson"]),
            ("FATAL: insert aborted", PALETTE["crimson"]),
        ]
        right_code = VGroup(*[
            fit(Text(l, color=c, font_size=15, font=MONO), 4.4) for l, c in right_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        right_code.next_to(right_header, DOWN, buff=0.35).align_to(right_header, LEFT)

        # v3.1 fix: the divider sits at x=0, but left_code/right_code were only
        # ever width-capped by fit() (5.6 / 4.4) — never actually checked
        # against the divider's position. A real frame extraction caught the
        # bug this produced: left_code's longest line ("const q = `INSERT INTO
        # items") rendered at width 4.14 with its left edge anchored at
        # left_header's left edge (~-4.03), landing its right edge at x=+0.11
        # — past the divider, visibly crossing through "items". Shifting each
        # header+code block as one rigid unit (not per-line rescaling, which
        # would mismatch that one line's font size against its neighbors) by
        # an amount measured from its own rendered bounds guarantees real
        # clearance regardless of future edits to line content. Right side
        # measured clear already (left edge ~2.16, comfortably past the
        # divider) so this is a no-op there — kept for symmetry/future-proofing.
        clear_of_divider(VGroup(left_header, left_code), divider_x=0, side="left")
        clear_of_divider(VGroup(right_header, right_code), divider_x=0, side="right")

        # both panels appear together, fast — the hold is what has to earn its keep
        self.play(
            Create(divider), FadeIn(left_header, shift=UP * 0.1), FadeIn(right_header, shift=UP * 0.1),
            run_time=0.35,
        )
        self.play(
            LaggedStart(
                *[FadeIn(l, shift=RIGHT * 0.1) for l in left_code],
                *[FadeIn(l, shift=RIGHT * 0.1) for l in right_code],
                lag_ratio=0.08,
            ),
            run_time=0.85,
        )
        self.wait(1.5)

        # a highlighter box (built from the target's own bounds, not passed the
        # mobject itself) points at the actual crash line, once both sides have
        # had a moment to register as legible together
        err_box = Rectangle(
            width=right_code[0].width + 0.24, height=right_code[0].height + 0.14,
            stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
        ).move_to(right_code[0].get_center())
        self.play(Create(err_box), run_time=0.3)

        # both sides legible simultaneously, held well past the 2s legibility floor
        self.wait(1.66)


# --------------------------------------------------------------------------- #
# B02 — FRAMEWORK: the 3-question rubric, shown in full before any example.
# v2 (2026-08-17): narration expanded from bare labels to a real explanatory
# sentence per question, opening with the fellow's requested line ("before
# you trust it, ask yourself all three"). On-screen content now carries that
# same opening line plus a two-line explanation per question (was one line),
# each row held on its own beat instead of all three landing at once.
# v3 (2026-08-17): Trace row's caption reworded — "not just read the diff"
# -> "not just read what's different" (fellow found "diff" jargon unclear;
# matches the narration_text fix in beat_sheet.json). Renamed from B01.
# measured audio: see actual_duration_s in beat_sheet.json (retuned below)
# --------------------------------------------------------------------------- #
class B02_FrameworkRubric(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The 3 Questions Before You Trust a Fix",
            color=PALETTE["ink"], font_size=44
        ), 11.5)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)

        intro = fit(Text(
            "Before you trust it, ask yourself all three.",
            color=PALETTE["slate"], font_size=22
        ), 10.5)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro, shift=UP * 0.1), run_time=0.4)
        self.wait(2.71)
        self.play(FadeOut(intro, shift=UP * 0.1), run_time=0.3)

        rows_data = [
            ("1", "TRACE", "Point to the exact execution path this change\ntouches — not just read what's different."),
            ("2", "CONSEQUENCE", "Know what breaks — silently — if this\nturns out to be wrong."),
            ("3", "WHY, NOT JUST WHAT", "Explain why this is the fix in terms of what\nthe system does — not that it looks right."),
        ]

        rows = VGroup()
        for num, label, desc in rows_data:
            badge = Circle(radius=0.42, color=PALETTE["teal"], fill_color=PALETTE["teal"], fill_opacity=0.15, stroke_width=2.5)
            badge_num = Text(num, color=PALETTE["teal"], font_size=28, font=MONO).move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)

            label_txt = fit(Text(label, color=PALETTE["slate"], font_size=26, font=MONO), 4.8)
            desc_txt = fit(Text(desc, color=PALETTE["ink"], font_size=22, line_spacing=1.0), 9.5)

            text_col = VGroup(label_txt, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
            row = VGroup(badge_group, text_col).arrange(RIGHT, buff=0.5)
            rows.add(row)

        # generous inter-row spacing (not just bigger text) — the reveal is
        # only 1-2 rows visible at a time for most of the beat's duration
        # (staged, in step with narration), and the closing "not two, not
        # one" line lands too late to be sampled by GATE V, so the row block
        # itself has to use most of the safe height on its own to pass the
        # canvas-fill law.
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.85)
        if rows.width > 12.0:
            rows.scale_to_fit_width(12.0)
        if rows.height > 4.6:
            rows.scale_to_fit_height(4.6)
        # centered between the title (top-anchored) and the closing line
        # (bottom-anchored, well clear of both), so the block's own
        # vertical span carries the canvas-fill without colliding with
        # either neighbor.
        rows.move_to(ORIGIN).shift(UP * 0.05)

        # SKELETON FIRST: all 3 badges + labels (TRACE/CONSEQUENCE/WHY) land
        # right away, one badge at a time in quick succession (not bundled
        # into a single LaggedStart — each is its own real steady state, not
        # just a repeated static frame) — the full rubric's shape is on
        # screen before any one question is explained (framework-first
        # requirement) and keeps real content spread across the frame
        # instead of an empty lower half while questions build one at a
        # time. Each row's *explanatory* sentence then streams in on its own
        # beat, in step with the narration actually explaining that question.
        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.15)

        # holds tuned to the measured 21.70s Kokoro audio, split proportional
        # to each question's word count (19/11/24 of 70 total spoken words
        # across trace/consequence/why) — see BUILD-LOG.md.
        row_holds = [5.05, 2.92, 6.38]
        for row, hold in zip(rows, row_holds):
            desc_txt = row[1][1]
            self.play(FadeIn(desc_txt, shift=UP * 0.1), run_time=0.3)
            self.wait(hold)

        not_two = fit(Text(
            "not two, not one — all three.", color=PALETTE["crimson"], font_size=24
        ), 8.5)
        # bottom-anchored (not next_to rows) so the closing line reaches
        # toward the safe-area floor — content spans title-to-floor instead
        # of clustering in the frame's top half
        not_two.to_edge(DOWN, buff=0.6)
        self.play(Write(not_two), run_time=0.5)
        # v3: +0.04s vs v2's 1.59 — the reworded Trace line measured 21.74s
        # (was 21.70s), a rounding-level difference from dropping "diff" for
        # "what's different"; absorbed into this closing hold.
        self.wait(1.63)


# --------------------------------------------------------------------------- #
# B03 — WORKED-EXAMPLE: generic hand-escaped SQL insert vs. parameterized fix
#       [GENERIC EXAMPLE — see FACTCHECK.md — never attribute to a real repo]
# v2 (2026-08-17): narration expanded from terse one-line-per-question labels
# ("what line, what table, what executes") to the actual SQL-injection
# mechanics — why quote-only escaping misses backslashes/null bytes/encoding,
# and why parameter binding removes the failure mode rather than patching a
# symptom. Captions below now carry that same explanatory depth (2-3 lines
# each, not a single tag line), plus a scene-setting intro caption before the
# rubric steps start.
# v3 (2026-08-17): renamed from B02 — narration/captions unchanged.
# measured audio: see actual_duration_s in beat_sheet.json (retuned below)
# --------------------------------------------------------------------------- #
class B03_WorkedExampleDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        header = fit(Text(
            "illustrative example — a generic before/after pattern",
            color=PALETTE["sage"], font_size=18, font=MONO
        ), 12.0)
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.4)

        # ---- BEFORE (left) ----
        before_label = fit(Text("BEFORE — hand-escaped", color=PALETTE["crimson"], font_size=18, font=MONO), 5.8)
        before_lines = [
            "const q = `INSERT INTO items",
            "  VALUES ('${title",
            "    .replace(/'/g, \"''\")}',",
            "  '${desc}', ${price})`;",
            "db.query(q);",
        ]
        before_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=15, font=MONO), 5.8) for l in before_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        before_col = VGroup(before_label, before_code).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        before_col.move_to([-3.55, 1.0, 0])

        # ---- AFTER (right) ----
        after_label = fit(Text("AFTER — parameterized", color=PALETTE["teal"], font_size=18, font=MONO), 5.8)
        after_lines = [
            "const q = `INSERT INTO items",
            "  VALUES ($1, $2, $3)`;",
            "db.query(q, [title, desc, price]);",
        ]
        after_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=15, font=MONO), 5.8) for l in after_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        after_col = VGroup(after_label, after_code).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        after_col.move_to([3.55, 1.0, 0])

        divider = Line([0, 2.6, 0], [0, -1.6, 0], color=PALETTE["slate"], stroke_width=2)

        self.play(Create(divider), run_time=0.2)
        # both versions appear together — legible simultaneously from the start
        self.play(FadeIn(before_col, shift=UP * 0.1), FadeIn(after_col, shift=UP * 0.1), run_time=0.8)
        self.wait(0.3)

        # a highlighter box (built from the target's own bounds, not passed the
        # mobject itself, so it reads as a real shape and not a text label) that
        # tracks the rubric step onto the relevant code line(s)
        def box_around(mob, buff=0.12):
            r = Rectangle(
                width=mob.width + 2 * buff, height=mob.height + 2 * buff,
                stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
            )
            r.move_to(mob.get_center())
            return r

        highlight = box_around(before_code[0])
        self.play(Create(highlight), run_time=0.3)

        caption_zone = VGroup()

        def show_step(tag, body_lines, color, t_hold, focus):
            """body_lines: list of short lines (multi-line caption), so the
            expanded v2 explanation fits without shrinking past legibility."""
            nonlocal caption_zone
            tag_txt = Text(tag, color=color, font_size=20, font=MONO)
            body_col = VGroup(*[
                fit(Text(l, color=PALETTE["sage"], font_size=17), 11.5) for l in body_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            step = VGroup(tag_txt, body_col).arrange(RIGHT, buff=0.35, aligned_edge=UP)
            if step.width > 12.0:
                step.scale_to_fit_width(12.0)
            step.to_edge(DOWN, buff=0.75)
            new_highlight = box_around(focus)
            if len(caption_zone) == 0:
                self.play(FadeIn(step, shift=UP * 0.15), Transform(highlight, new_highlight), run_time=0.5)
            else:
                self.play(FadeOut(caption_zone), FadeIn(step, shift=UP * 0.15),
                          Transform(highlight, new_highlight), run_time=0.5)
            caption_zone = step
            self.wait(t_hold)

        # narration now walks the actual mechanics per step, not a one-line
        # label. Hold times tuned to the measured 43.99s Kokoro audio, split
        # proportional to each step's word count (19/21/30/51 of 121 total
        # spoken words across setup/trace/consequence/why) — see BUILD-LOG.md.
        show_step(
            "SETUP:",
            ["this insert escapes single quotes by hand",
             "before the value ever reaches the database"],
            PALETTE["gold"], 6.28,
            before_code[0],
        )
        show_step(
            "TRACE:",
            ["every value gets wrapped in quotes and dropped",
             "straight into the SQL string — that's the exact",
             "line that runs"],
            PALETTE["teal"], 6.94,
            before_code[2],
        )
        show_step(
            "CONSEQUENCE:",
            ["escaping only handles apostrophes — a backslash,",
             "a null byte, an unexpected encoding all slip through,",
             "and one bad row aborts the entire batch, not just itself"],
            PALETTE["crimson"], 9.92,
            before_code[2],
        )
        show_step(
            "WHY:",
            ["parameterized values are bound separately from the",
             "query — there's no string for a stray character to",
             "break out of. Not a patch on the symptom — the",
             "failure mode itself is gone."],
            PALETTE["teal"], 16.85,
            VGroup(after_code[1], after_code[2]),
        )


# --------------------------------------------------------------------------- #
# B04 — FALSIFIABILITY: trivial date-formatter, "LOW STAKES", rubric alongside
# measured audio: 9.91s (unchanged from v2's B03 — renamed only)
# --------------------------------------------------------------------------- #
class B04_FalsifiabilityCase(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Does this need the same scrutiny?", color=PALETTE["ink"], font_size=28
        ), 11.0)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.4)

        # left: compact rubric recap
        chip_labels = ["TRACE", "CONSEQUENCE", "WHY"]
        chips = VGroup(*[
            VGroup(
                RoundedRectangle(width=2.3, height=0.55, corner_radius=0.08,
                                 fill_color=PALETTE["slate"], fill_opacity=0.12,
                                 stroke_color=PALETTE["slate"], stroke_width=1.5),
                Text(lbl, color=PALETTE["slate"], font_size=15, font=MONO),
            )
            for lbl in chip_labels
        ])
        for grp in chips:
            grp[1].move_to(grp[0].get_center())
        chips.arrange(DOWN, buff=0.3)
        chips.move_to([-4.0, -0.2, 0])

        rubric_caption = fit(Text("the rubric", color=PALETTE["ink"], font_size=16), 2.6)
        rubric_caption.next_to(chips, UP, buff=0.3)

        # right: the trivial function, in its own dark panel
        code_panel = panel(width=6.6, height=2.0, fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_panel.move_to([2.6, 0.4, 0])

        fn_lines = [
            "function formatDate(d) {",
            "  return d.toISOString().slice(0, 10);",
            "}",
        ]
        fn_code = VGroup(*[
            fit(Text(l, color=PALETTE["sage"], font_size=17, font=MONO), 5.9) for l in fn_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        fn_code.move_to(code_panel.get_center())

        self.play(
            FadeIn(rubric_caption), LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.15),
            run_time=0.6,
        )
        self.play(Create(code_panel), FadeIn(fn_code), run_time=0.6)
        self.wait(0.3)

        low_stakes = fit(Text("LOW STAKES", color=PALETTE["teal"], font_size=22, font=MONO), 3.4)
        low_stakes.next_to(code_panel, DOWN, buff=0.35)
        check = Text("check", color=PALETTE["teal"], font_size=22, font=MONO).next_to(low_stakes, LEFT, buff=0.25)
        self.play(FadeIn(check), Write(low_stakes), run_time=0.5)
        self.wait(0.4)

        line = fit(Text(
            "quick trust is fine here — the rubric scales with what breaks",
            color=PALETTE["ink"], font_size=18
        ), 11.5)
        line.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(line, shift=UP * 0.1), run_time=0.5)
        self.wait(6.41)


# --------------------------------------------------------------------------- #
# B05 — CTA: the literal 3-step checklist, copyable text, held >= 3s.
# v2 (2026-08-17): narration expanded from naming the 3 steps to explaining
# why each matters ("don't accept a vague answer" / "not a full audit" /
# "if you can't write that sentence, you don't understand the fix yet — and
# neither did the tool"). On-screen content now adds a one-line explanation
# under each step and the closing zinger line, and steps build one at a time
# (in step with the narration reaching each) instead of landing all at once.
# v3 (2026-08-17): renamed from B04 — narration/captions unchanged.
# measured audio: see actual_duration_s in beat_sheet.json (retuned below)
# --------------------------------------------------------------------------- #
class B05_ScaffoldedTask(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Before you merge that fix:", color=PALETTE["ink"], font_size=27
        ), 10.5)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.3)
        # holds the title beat for the "so here's what to actually do" lead-in
        # before step one lands (see hold-tuning note below)
        self.wait(1.62)

        steps_data = [
            (["1. Ask: \"what specifically breaks if this is wrong,",
              "     and how would I know?\""],
             "don't accept a vague answer"),
            (["2. Trace the one function/file it touches,",
              "     by hand, for 60 seconds."],
             "a quick check, not a full audit"),
            (["3. Write one sentence explaining why this fixes",
              "     the root cause — not just what changed."],
             "can't write it? you don't understand the fix yet"),
        ]

        rows = VGroup()
        for main_lines, explain in steps_data:
            box = Square(side_length=0.32, color=PALETTE["slate"], stroke_width=2.5)
            main_txt = VGroup(*[
                fit(Text(l, color=PALETTE["ink"], font_size=22, font=MONO), 11.2) for l in main_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            explain_txt = fit(Text(explain, color=PALETTE["slate"], font_size=17), 11.0)
            text_col = VGroup(main_txt, explain_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            row = VGroup(box, text_col).arrange(RIGHT, buff=0.4, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        if rows.width > 12.0:
            rows.scale_to_fit_width(12.0)
        if rows.height > 4.2:
            rows.scale_to_fit_height(4.2)
        # centered between the title (top-anchored) and the closing zinger
        # (bottom-anchored, see below) — spreads real content across the
        # full safe height instead of clustering under the title with a
        # dead lower half (GATE V canvas-fill law: bbox coverage of SAFE).
        rows.move_to(ORIGIN).shift(UP * 0.1)

        # SKELETON FIRST: the literal 3-step checklist (box + main text) lands
        # one step at a time in quick succession (not bundled into a single
        # LaggedStart — each is its own real steady state) — copyable text,
        # on screen before any step is explained, and keeps real content
        # spread down the frame instead of an empty lower half while steps
        # build one at a time. Each step's *explanation* then streams in on
        # its own beat, in step with the narration actually explaining it.
        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.2)

        # holds tuned to the measured 26.38s Kokoro audio, split proportional
        # to each segment's word count (23/22/16 of 89 total spoken words for
        # steps 1/2/3, title lead-in counted above, zinger below) — see
        # BUILD-LOG.md.
        step_holds = [6.22, 5.96, 4.33]
        for row, hold in zip(rows, step_holds):
            explain_txt = row[1][1]
            self.play(FadeIn(explain_txt, shift=UP * 0.08), run_time=0.3)
            self.wait(hold)

        zinger = fit(Text(
            "can't write that sentence? neither did the tool.",
            color=PALETTE["crimson"], font_size=20
        ), 10.5)
        # bottom-anchored (not next_to rows) so the zinger reaches toward
        # the safe-area floor instead of clustering under the checklist
        zinger.to_edge(DOWN, buff=0.7)
        self.play(Write(zinger), run_time=0.5)
        self.wait(5.96)


# --------------------------------------------------------------------------- #
# B06 — CLOSE: callback to B01's crash log, now corrected
# measured audio: 7.49s (unchanged from v2's B05 — renamed only)
# --------------------------------------------------------------------------- #
class B06_Close(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        header = fit(Text("server.log — production", color=PALETTE["sage"], font_size=18, font=MONO), 8.0)
        header.move_to([0, 2.6, 0])
        self.play(FadeIn(header), run_time=0.3)

        old_line = fit(Text(
            "ERROR: syntax error at or near \"s\"", color=PALETTE["crimson"], font_size=16, font=MONO
        ), 8.0)
        old_line.next_to(header, DOWN, buff=0.35)
        strike = Line(old_line.get_left(), old_line.get_right(), color=PALETTE["crimson"], stroke_width=2)
        strike._qc_intentional = True  # deliberate strike-through over corrected text

        new_line = fit(Text(
            "OK: parameterized insert — 1 row committed", color=PALETTE["teal"], font_size=16, font=MONO
        ), 8.0)
        new_line.next_to(old_line, DOWN, buff=0.3)

        self.play(FadeIn(old_line), run_time=0.25)
        self.play(Create(strike), run_time=0.25)

        check = Text("check", color=PALETTE["teal"], font_size=20, font=MONO)
        check.next_to(old_line, RIGHT, buff=0.3)
        self.play(FadeIn(check, scale=1.3), run_time=0.25)
        self.play(FadeIn(new_line, shift=UP * 0.1), run_time=0.3)
        self.wait(0.2)

        statement1 = fit(Text(
            "The code that looks right and the code that is right",
            color=PALETTE["sage"], font_size=20
        ), 10.5)
        statement2 = fit(Text(
            "aren't always the same thing.", color=PALETTE["sage"], font_size=20
        ), 10.5)
        statement = VGroup(statement1, statement2).arrange(DOWN, buff=0.2)
        statement.move_to([0, -1.3, 0])
        # FadeIn (not Write) — a mid-animation sample must still show fully
        # formed glyphs, not a partial stroke-by-stroke draw
        self.play(FadeIn(statement), run_time=0.5)
        self.wait(0.2)

        gap_line = fit(Text(
            "that gap is where you're still the one doing the job.",
            color=PALETTE["gold"], font_size=18
        ), 10.5)
        gap_line.next_to(statement, DOWN, buff=0.4)
        highlight = Rectangle(
            width=gap_line.width + 0.4, height=gap_line.height + 0.25,
            fill_color=PALETTE["gold"], fill_opacity=0.15, stroke_width=0,
        ).move_to(gap_line.get_center())
        gap_line.set_color(PALETTE["sage"])
        self.play(FadeIn(highlight), FadeIn(gap_line), run_time=0.5)
        # everything settled well before the 50%/85% QC sample points — the
        # remainder of the beat is a clean static hold
        self.wait(4.74)


# --------------------------------------------------------------------------- #
# B07 — SIGN-OFF: @HumanitariansAI, in for Sai Pranavi Jeedigunta
# measured audio: 4.92s (unchanged from v2's B06 — renamed only)
# --------------------------------------------------------------------------- #
class B07_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=34)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(Text(
            "in for Sai Pranavi Jeedigunta", color=PALETTE["ink"], font_size=20
        ), 8.0)
        VGroup(handle, accent, tagline).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        self.wait(3.12)
