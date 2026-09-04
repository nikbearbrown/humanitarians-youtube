"""
Manim scenes for 2026-08-30-the-check-that-never-once-fired/short
(9:16 Shorts derivative)

Built via THE SHORTS LAW (runtime/scripts/shorts.py): this reel is UNDER the
180s cap (133.6s), so the whole reel reformats 16:9 -> 9:16 as-is — 0 beats
dropped, every beat's mp3 is the parent's unchanged narration (symlinked
into short/mp3/). This file supplies ONLY the visual half: a genuine
hand-authored portrait (1080x1920) re-layout of each of the 9 parent Manim
scenes in ../scenes.py — per THE REFORMAT RULE, generated graphics are
NEVER auto-cropped. Same beat_id -> class name mapping, same
PALETTE/MONO/fit()/panel()/box_around(), same per-beat animation timing
(every self.play run_time and self.wait matches the parent beat-for-beat,
since the audio is identical) — only the geometry changes.

Portrait geometry budget (manim units): frame is 4.5 wide x 8.0 tall (same
convention as this fellow's sibling shorts). GATE B's --portrait safe box
is +-1.95 x / +-3.4 y (half-extents); this file targets a tighter
+-1.75 x / +-3.1 y working area so margin checks clear with room to spare.

Real redesigns (not a mechanical shrink) — the 3 beats the build brief
specifically calls out:
  B04 RealFilingVsCondition — parent is LEFT (real filing) / RIGHT (what
                        the rule looks for) with a vertical divider.
                        Portrait stacks TOP (real filing) / BOTTOM (what
                        the rule looks for) with a horizontal divider
                        (clear_of_hdivider) — same reading order the
                        narration walks.
  B05 FiveFeedResultsTable — parent is a 4-column table (feed / tested /
                        reclass / result), 5 rows wide. Portrait restacks
                        every row as its own vertical mini-card (feed name,
                        then tested->reclass, then result), one column,
                        same CFTC-row and zero-regression highlights.
  B06 BeforeAfterClassifier — parent is LEFT (BEFORE) / RIGHT (AFTER) with
                        a vertical divider. Portrait restacks TOP (BEFORE)
                        / BOTTOM (AFTER) with a horizontal divider
                        (clear_of_hdivider) — the narration's own order.

Every other beat (B00, B01, B02, B03, B07, B08) was already a single
vertical column in the parent — these keep the same composition, narrower
widths/re-wrapped text and, where GATE B/V required it, bigger fonts/buffs
tuned by real Manim measurement (never guessed) for portrait canvas-fill.
"""

from manim import *

# Portrait sync (same fix as this fellow's sibling shorts and the shared
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

SAFE_W = 3.8   # working width inside the 4.5-wide portrait frame (safe box is 3.9)


def fit(mob, max_w=SAFE_W):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


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
    """Portrait analogue of the parent scenes.py's clear_of_divider() —
    same pattern (measure the block's OWN rendered bounds, shift the whole
    rigid unit by the real overhang, never a per-line rescale), rotated 90
    degrees: every side-by-side split in the parent (a vertical divider
    with LEFT/RIGHT panels) becomes a top/bottom stack here (a horizontal
    divider with TOP/BOTTOM panels).

    side="top"    -> block sits ABOVE the divider; keeps get_bottom()[1] >=
                      divider_y + margin.
    side="bottom" -> block sits BELOW the divider; keeps get_top()[1] <=
                      divider_y - margin.
    No-op if the block already clears the margin.
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

        title = fit(Text(
            "The Check That\nNever Once Fired",
            color=PALETTE["ink"], font_size=48, weight="BOLD", line_spacing=1.05,
        ))

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=32)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=1.1).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        self.wait(2.40)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: name/role/accent/summary, same 4-element stack as the
# parent — summary re-wrapped 3 -> 7 short lines for the narrow column.
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text(
            "Sai Pranavi\nJeedigunta", color=PALETTE["ink"], font_size=44,
            weight="BOLD", line_spacing=1.0,
        ))
        role = Text("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=22)
        accent = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        summary = fit(Text(
            "A classifier written\nto catch CFTC filings\nthat, tested against\n"
            "real data, never once\nmatched — now reads\nthe actual source\ninstead of guessing.",
            color=PALETTE["ink"], font_size=25, line_spacing=1.05,
        ))

        VGroup(name, role, accent, summary).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        summary_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(name, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        summary_underline.put_start_and_end_on(
            summary.get_corner(DL) + DOWN * 0.12, summary.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(summary_underline), run_time=0.3)
        # animation sum = 2.8s; measured narration = 18.74s
        self.wait(15.94)


# --------------------------------------------------------------------------- #
# B02 — HOOK: CFTC heuristic condition + "0 MATCHES" stamp. Already a
# single vertical column in the parent — narrowed widths, same order.
# --------------------------------------------------------------------------- #
class B02_ZeroMatchesHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text(
            "identifySource() —\nthe CFTC heuristic", color=PALETTE["slate"],
            font_size=18, font=MONO, line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        cond_lines = [
            "if (link.includes(",
            "  'commodity-futures')",
            "  || title.includes(",
            "    'cftc')) {",
            "  return 'CFTC",
            "    Regulations';",
            "}",
        ]
        cond = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=18, font=MONO)) for l in cond_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        cond.next_to(header, DOWN, buff=0.4)
        box = box_around(cond, PALETTE["teal"], buff=0.2)
        self.play(Create(box), FadeIn(cond), run_time=0.7)

        # capped narrower than SAFE_W: the stamp box below adds +0.4 width
        # padding, so the TEXT alone must leave room for that padding to
        # keep the outer box inside the safe x-extent.
        stamp_text = fit(Text("0 MATCHES", color=PALETTE["crimson"], font_size=48, weight="BOLD"), 3.2)
        stamp_box = Rectangle(
            width=stamp_text.width + 0.4, height=stamp_text.height + 0.25,
            stroke_color=PALETTE["crimson"], stroke_width=5, fill_opacity=0,
        )
        stamp = VGroup(stamp_box, stamp_text)
        stamp.next_to(box, DOWN, buff=0.4)
        self.play(Write(stamp_text), Create(stamp_box), run_time=0.65)

        caption = fit(Text(
            "tested against every live\nCFTC item pulled today",
            color=PALETTE["slate"], font_size=20, line_spacing=1.0,
        ))
        caption.next_to(stamp, DOWN, buff=0.35)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.1, caption.get_corner(DR) + DOWN * 0.1
        )
        self.play(Create(caption_underline), run_time=0.3)
        self.wait(8.73)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the full federalregister.gov branch. Already a single
# vertical column in the parent — code lines individually fit()-capped to
# the narrow safe width (they were already fit()-capped in the parent too;
# the cap just bites harder here), tags moved BELOW the whole code block
# instead of beside each highlight (no room to the side in portrait).
# --------------------------------------------------------------------------- #
class B03_ClassifierCondition(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(Text(
            "identifySource() —\nthe Federal Register branch", color=cream,
            font_size=16, font=MONO, line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.7)
        self.play(Write(header), run_time=0.5)

        lines = [
            "if (lowerLink.includes(",
            "  'federalregister.gov'",
            ")) {",
            "  if (lowerLink.includes(",
            "    'commodity-futures')",
            "    || lowerTitle",
            "      .includes('cftc')) {",
            "    return 'CFTC Regulations';",
            "  }",
            "  return 'Federal Register -",
            "    Securities';",
            "}",
        ]
        code = VGroup(*[
            fit(Text(l, color=cream, font_size=15, font=MONO)) for l in lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.09)
        code.next_to(header, DOWN, buff=0.4)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.08) for l in code], lag_ratio=0.1), run_time=1.0)

        # the two checks — link contains 'commodity-futures' OR title
        # contains 'cftc' — now spans lines 3-6 (wrapped across more
        # physical lines than the parent's 2, since each line is much
        # narrower in portrait).
        checks = VGroup(code[3], code[4], code[5], code[6])
        checks_box = box_around(checks, PALETTE["teal"], buff=0.12)
        self.play(Create(checks_box), run_time=0.5)

        # the default — now spans lines 9-10 (wrapped).
        default_box = box_around(VGroup(code[9], code[10]), PALETTE["crimson"], buff=0.12)
        self.play(Create(default_box), run_time=0.5)

        # ONE shared caption pair below the FULL code block (not beside
        # each highlight — no horizontal room in a ~3.8-wide column, and a
        # floating side tag is exactly the collision class the parent's
        # own B03 build note documents fixing).
        tag1 = Text("↑ the two checks", color=PALETTE["teal"], font_size=17, font=MONO, weight="BOLD")
        tag2 = Text("↑ the default", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD")
        tags = VGroup(tag1, tag2).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        tags.next_to(code, DOWN, buff=0.3)
        self.play(Write(tag1), run_time=0.5)
        self.play(Write(tag2), run_time=0.5)

        self.wait(11.82)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: REAL redesign. Parent has REAL FILING (left) / WHAT THE
# RULE LOOKS FOR (right) with a vertical divider. Portrait stacks TOP (real
# filing) / BOTTOM (what the rule looks for) with a horizontal divider —
# same reading order the narration walks (the real filing first, then the
# two absent checks). clear_of_hdivider() verifies clearance from real
# measured bounds, not a guess.
# --------------------------------------------------------------------------- #
class B04_RealFilingVsCondition(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text(
            "A real CFTC filing,\npulled live today", color=PALETTE["ink"],
            font_size=26, weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.75)
        self.play(Write(header), run_time=0.5)

        # TOP — the real filing
        top_label = Text("REAL FILING", color=PALETTE["teal"], font_size=18, weight="BOLD")
        top_title = fit(Text(
            "“Swap Execution Facility\nOrder Book Requirement\nfor Permitted Transactions”",
            color=PALETTE["ink"], font_size=16, line_spacing=1.05,
        ))
        top_link = fit(Text(
            "federalregister.gov/\ndocuments/2026/08/26/\n2026-17416/swap-execution-\nfacility-...",
            color=PALETTE["slate"], font_size=13, font=MONO, line_spacing=1.0,
        ))
        top_block = VGroup(top_label, top_title, top_link).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        top_block.next_to(header, DOWN, buff=0.3)

        # BOTTOM — what the rule looks for, both absent
        bottom_label = Text("WHAT THE RULE LOOKS FOR", color=PALETTE["crimson"], font_size=16, weight="BOLD")
        bottom_label = fit(bottom_label)
        check1 = fit(Text("'cftc' in title", color=PALETTE["ink"], font_size=17, font=MONO))
        absent1 = Text("→ ABSENT", color=PALETTE["crimson"], font_size=16, weight="BOLD")
        row1 = VGroup(check1, absent1).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        check2 = fit(Text("'commodity-futures'\nin link", color=PALETTE["ink"], font_size=17, font=MONO, line_spacing=1.0))
        absent2 = Text("→ ABSENT", color=PALETTE["crimson"], font_size=16, weight="BOLD")
        row2 = VGroup(check2, absent2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        bottom_block = VGroup(bottom_label, row1, row2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        # bottom_block sits below top_block with room for the divider
        bottom_block.next_to(top_block, DOWN, buff=0.4)

        divider_y = (top_block.get_bottom()[1] + bottom_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["slate"], stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(top_block, divider_y, side="top", margin=0.3)
        clear_of_hdivider(bottom_block, divider_y, side="bottom", margin=0.3)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(top_block, shift=DOWN * 0.1),
            FadeIn(bottom_block, shift=UP * 0.1),
            run_time=0.7,
        )
        self.play(Write(absent1), run_time=0.4)
        self.play(Write(absent2), run_time=0.4)

        caption = fit(Text(
            "checking for something\nthat structurally can't appear",
            color=PALETTE["slate"], font_size=18, line_spacing=1.0,
        ))
        caption.next_to(bottom_block, DOWN, buff=0.25)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["crimson"], stroke_width=1.5)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.1, caption.get_corner(DR) + DOWN * 0.1
        )
        self.play(Create(caption_underline), run_time=0.3)

        self.wait(16.56)


# --------------------------------------------------------------------------- #
# B05 — PROOF: REAL redesign. Parent has a 4-column table, 5 rows wide.
# Portrait restacks every row as its own vertical mini-card (feed name,
# then tested->reclass, then result) — one column, same reading order,
# same CFTC-row and zero-regression highlights.
# --------------------------------------------------------------------------- #
class B05_FiveFeedResultsTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(Text(
            "Live test — all 5\nreal feeds, today", color=ink, font_size=24,
            weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.7)
        self.play(Write(header), run_time=0.5)

        rows_data = [
            ("Federal Register - Securities", "146 → 83", PALETTE["crimson"],
             "→ real agency (FCC, EEOC, DOT)"),
            ("CFTC Regulations", "12 → 12", PALETTE["crimson"],
             "→ was 0/12 caught before"),
            ("SEC Press Releases", "25 → 0", PALETTE["teal"],
             "unchanged — already correct"),
            ("FINRA (Google News)", "100 → 0", PALETTE["teal"],
             "unchanged — already correct"),
            ("Investment Advisor Rules", "100 → 0", PALETTE["teal"],
             "unchanged — already correct"),
        ]

        row_groups = []
        for feed, counts, rcolor, result in rows_data:
            feed_t = fit(Text(feed, color=ink, font_size=17, weight="BOLD"))
            counts_t = Text(counts, color=rcolor, font_size=18, font=MONO, weight="BOLD")
            result_t = fit(Text(result, color=PALETTE["slate"], font_size=14))
            row = VGroup(feed_t, counts_t, result_t).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row_groups.append(row)

        table = VGroup(*row_groups).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        table.next_to(header, DOWN, buff=0.35)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.06) for r in row_groups], lag_ratio=0.15), run_time=1.1)

        # highlight the CFTC row (index 1) — the hero proof: 0 -> 12/12
        cftc_row = row_groups[1]
        cftc_box = Rectangle(
            width=3.7, height=cftc_row.height + 0.16,
            stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
        )
        # x from the table's own (symmetric) center, not the row's own
        # center — rows are left-aligned with varying widths, so a fixed-
        # width box centered on a narrower row's center would overhang the
        # opposite safe edge (same class of bug as the zero_box below,
        # which already centers on x=0 for this reason).
        cftc_box.move_to([table.get_x(), cftc_row.get_center()[1], 0])
        self.play(Create(cftc_box), run_time=0.5)

        # highlight the 3 zero-regression rows (SEC, FINRA, Investment Advisor)
        zero_rows = VGroup(row_groups[2], row_groups[3], row_groups[4])
        zero_top = zero_rows.get_top()[1] + 0.1
        zero_bottom = zero_rows.get_bottom()[1] - 0.1
        zero_box = Rectangle(
            width=3.7, height=zero_top - zero_bottom,
            stroke_color=PALETTE["teal"], stroke_width=3, fill_opacity=0,
        )
        zero_box.move_to([0.0, (zero_top + zero_bottom) / 2, 0])
        self.play(Create(zero_box), run_time=0.5)

        caption = fit(Text(
            "CFTC: every one now\ncaught. Zero regressions\non what already worked.",
            color=PALETTE["slate"], font_size=17, line_spacing=1.0,
        ))
        caption.next_to(zero_box, DOWN, buff=0.25)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.1, caption.get_corner(DR) + DOWN * 0.1
        )
        self.play(Create(caption_underline), run_time=0.3)

        self.wait(25.32)


# --------------------------------------------------------------------------- #
# B06 — FIX: REAL redesign. Parent is LEFT (BEFORE) / RIGHT (AFTER) with a
# vertical divider; portrait stacks TOP (BEFORE) / BOTTOM (AFTER) with a
# horizontal divider — the narration's own order ("stop guessing... now
# reads the actual source..."). ONE shared caption below both (not
# per-line floating tags — same collision class the parent's own B06 build
# note documents fixing).
# --------------------------------------------------------------------------- #
class B06_BeforeAfterClassifier(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        before_label = Text("BEFORE", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD")
        before_lines = [
            "if (link.includes(",
            "  'federalregister.gov'",
            ")) {",
            "  if (link.includes(",
            "    'commodity-futures')",
            "    || title.includes(",
            "      'cftc')) {",
            "    return 'CFTC Regulations';",
            "  }",
            "  return 'Federal Register -",
            "    Securities';",
            "}",
        ]
        before_code = VGroup(*[
            fit(Text(l, color=cream, font_size=14, font=MONO)) for l in before_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
        before_block = VGroup(before_label, before_code).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        before_block.to_edge(UP, buff=0.8)

        after_label = Text("AFTER", color=PALETTE["teal"], font_size=17, font=MONO, weight="BOLD")
        after_lines = [
            "if (link.includes(",
            "  'federalregister.gov'",
            ")) {",
            "  const c = (creator ||",
            "    '').toLowerCase();",
            "  if (c.includes('commodity",
            "    futures ...')",
            "    || link.includes(",
            "      'commodity-futures')) {",
            "    return 'CFTC Regulations';",
            "  }",
            "  return `Federal Register -",
            "    ${creator}`;",
            "}",
        ]
        after_code = VGroup(*[
            fit(Text(l, color=cream, font_size=14, font=MONO)) for l in after_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
        after_block = VGroup(after_label, after_code).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        after_block.to_edge(DOWN, buff=0.7)

        divider_y = (before_block.get_bottom()[1] + after_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["slate"], stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(before_block, divider_y, side="top", margin=0.2)
        clear_of_hdivider(after_block, divider_y, side="bottom", margin=0.2)

        self.play(Create(divider), run_time=0.25)
        self.play(
            FadeIn(before_block, shift=DOWN * 0.1),
            FadeIn(after_block, shift=UP * 0.1),
            run_time=0.75,
        )

        # highlight 1 — reads dc:creator instead of guessing
        hl1 = box_around(after_code[3], PALETTE["gold"], buff=0.08)
        self.play(Create(hl1), run_time=0.45)

        # highlight 2 — the real-agency fallback, never a blanket "Securities"
        hl2 = box_around(VGroup(after_code[11], after_code[12]), PALETTE["gold"], buff=0.08)
        self.play(Create(hl2), run_time=0.45)

        self.wait(11.54)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card. Already a single vertical column in the
# parent — re-wrapped to shorter lines, bigger type for the narrow column.
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font sizes + buff bumped up from the first pass (GATE V flagged
        # 53% canvas-fill, under the 55% floor) — real Manim measurement
        # confirmed this puts the group's height at ~4.7 (was ~4.1),
        # comfortably clearing 55% coverage while still bottoming out at
        # y=+-2.36, well inside the +-3.4 safe floor.
        line1 = fit(Text(
            "A safeguard that's\nnever once tested",
            color=PALETTE["ink"], font_size=44, line_spacing=1.05,
        ))
        line2 = fit(Text(
            "against real input isn't\nprotecting anything.",
            color=PALETTE["crimson"], font_size=42, line_spacing=1.05,
        ))
        line3 = fit(Text(
            "It's just code that\nlooks like protection.",
            color=PALETTE["slate"], font_size=30, line_spacing=1.05,
        ))
        VGroup(line1, line2, line3).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.4)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.6)
        self.wait(7.26)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI. Already a single vertical column in the
# parent — narrower rule, same composition.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=68))
        accent = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(Text("in for Sai Pranavi\nJeedigunta", color=PALETTE["ink"], font_size=36, line_spacing=1.05))
        VGroup(handle, accent, tagline).arrange(DOWN, buff=1.4).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        self.wait(4.46)
