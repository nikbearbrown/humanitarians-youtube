"""
Manim scenes for 2026-09-07-the-synonyms-the-classifier-never-learned/short
(9:16 Shorts derivative)

Built via THE SHORTS LAW (runtime/scripts/shorts.py): this reel is UNDER the
180s cap (131.6s), so the whole reel reformats 16:9 -> 9:16 as-is — 0 beats
dropped, every beat's mp3 is the parent's unchanged narration (symlinked
into short/mp3/). This file supplies ONLY the visual half: a genuine
hand-authored portrait (1080x1920) re-layout of each of the 9 parent Manim
scenes in ../scenes.py — per THE REFORMAT RULE, generated graphics are
NEVER auto-cropped. Same beat_id -> class name mapping, same
PALETTE/MONO/fit()/box_around(), same per-beat animation timing (every
self.play run_time and self.wait matches the parent beat-for-beat, since
the audio is identical) — only the geometry changes.

Portrait geometry budget (manim units): frame is 4.5 wide x 8.0 tall (same
convention as this fellow's sibling shorts). GATE B's --portrait safe box
is +-1.95 x / +-3.4 y (half-extents); SAFE_W below is a FULL-width cap
(3.8, just inside the ~3.9 full safe width) so fit() calls read the same
as the sibling shorts' own convention.

Real redesigns (not a mechanical shrink) — the 3 beats this build calls
out (the side-by-side/multi-row parent beats):
  B03 FieldComparison    — parent is LEFT (Federal Register dc:creator) /
                        RIGHT (Google News <source>) with a vertical
                        divider. Portrait stacks TOP / BOTTOM with a
                        horizontal divider (clear_of_hdivider) — same
                        reading order the narration walks.
  B04 TwoGroups          — parent is LEFT (recoverable title) / RIGHT
                        (not-recoverable title) with a vertical divider.
                        Portrait stacks TOP / BOTTOM with a horizontal
                        divider (clear_of_hdivider).
  B05 FixAndProofTable   — parent is a 4-column table (feed / items /
                        before / after), 5 rows + a total row. Portrait
                        restacks every row as its own vertical mini-card
                        (feed name, then items/before/after, then note),
                        one column, same changed-rows and 18->8 total
                        highlights.

Every other beat (B00, B01, B02, B06, B07, B08) was already a single
vertical column in the parent — these keep the same composition, narrower
widths/re-wrapped text and bigger fonts/buffs tuned by real Manim
measurement (never guessed) for portrait canvas-fill.
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

SAFE_W = 3.8   # working full-width inside the 4.5-wide portrait frame (safe box full-width ~3.9)


def fit(mob, max_w=SAFE_W):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


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
            "The Synonyms\nthe Classifier\nNever Learned",
            color=PALETTE["ink"], font_size=42, weight="BOLD", line_spacing=1.05,
        ))

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=30)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        self.wait(2.40)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: name/role/accent/summary, same 4-element stack as the
# parent — summary re-wrapped for the narrow column.
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text(
            "Sai Pranavi\nJeedigunta", color=PALETTE["ink"], font_size=42,
            weight="BOLD", line_spacing=1.0,
        ))
        role = Text("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=20)
        role = fit(role)
        accent = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        summary = fit(Text(
            "Eighteen items were\nfalling into 'Unknown\nSource.' An honest\n"
            "partial fix recovered\nten — eight stay open,\non purpose.",
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
        # animation sum = 2.8s; measured narration = 15.02s
        self.wait(12.22)


# --------------------------------------------------------------------------- #
# B02 — HOOK: 18-cell feed grid + red stamp. Already a single vertical
# column in the parent — grid renarrowed to 3 cols x 6 rows to fit the
# portrait safe width, stamp text wrapped to 2 lines.
# --------------------------------------------------------------------------- #
class B02_UnknownSourceHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text(
            "Google News feeds —\nlive scan, today", color=PALETTE["slate"],
            font_size=22, font=MONO, line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        cells = VGroup()
        for i in range(18):
            cell = RoundedRectangle(
                width=1.05, height=0.42, corner_radius=0.05,
                fill_color=PALETTE["ink"], fill_opacity=0.07,
                stroke_color=PALETTE["slate"], stroke_width=1.3,
            )
            tag = Text("?", color=PALETTE["crimson"], font_size=17, weight="BOLD")
            tag.move_to(cell.get_center())
            cells.add(VGroup(cell, tag))
        grid = cells.arrange_in_grid(rows=6, cols=3, buff=0.14)
        grid.next_to(header, DOWN, buff=0.3)

        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in cells], lag_ratio=0.04), run_time=1.4)

        stamp_text = fit(Text(
            "18 -> UNKNOWN\nSOURCE", color=PALETTE["crimson"], font_size=30,
            weight="BOLD", line_spacing=1.0,
        ), 3.2)
        stamp_box = Rectangle(
            width=stamp_text.width + 0.4, height=stamp_text.height + 0.3,
            stroke_color=PALETTE["crimson"], stroke_width=4, fill_opacity=0,
        )
        stamp = VGroup(stamp_box, stamp_text)
        stamp.next_to(grid, DOWN, buff=0.3)
        self.play(Write(stamp_text), Create(stamp_box), run_time=0.7)

        caption = fit(Text(
            "last week's fix\ndidn't touch these",
            color=PALETTE["slate"], font_size=18, line_spacing=1.0,
        ))
        caption.next_to(stamp, DOWN, buff=0.22)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        # animation sum = 0.5+1.4+0.7+0.5 = 3.1s; measured narration = 9.98s
        self.wait(6.88)


# --------------------------------------------------------------------------- #
# B03 — SETUP: REAL redesign. Parent is LEFT (Federal Register dc:creator) /
# RIGHT (Google News <source>) with a vertical divider. Portrait stacks
# TOP / BOTTOM with a horizontal divider (clear_of_hdivider) — same
# narration order (Federal Register first, then Google News).
# --------------------------------------------------------------------------- #
class B03_FieldComparison(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(Text(
            "Two feeds, two\ndifferent fields", color=cream,
            font_size=26, weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.6)
        self.play(Write(header), run_time=0.5)

        # TOP — Federal Register: dc:creator, populated with a real agency.
        top_label = Text("FEDERAL REGISTER", color=PALETTE["teal"], font_size=18, font=MONO, weight="BOLD")
        top_label = fit(top_label)
        top_lines = [
            "<dc:creator>",
            "  Commodity Futures",
            "  Trading Commission",
            "</dc:creator>",
        ]
        top_code = VGroup(*[
            fit(Text(l, color=cream, font_size=17, font=MONO)) for l in top_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        top_tag = fit(Text("-> real issuing agency", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD"))
        top_block = VGroup(top_label, top_code, top_tag).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        top_block.next_to(header, DOWN, buff=0.3)

        # BOTTOM — Google News: <source>, a publisher name, not a regulator.
        bottom_label = Text("GOOGLE NEWS", color=PALETTE["crimson"], font_size=18, font=MONO, weight="BOLD")
        bottom_lines = [
            "<source>",
            "  Mayer Brown",
            "</source>",
        ]
        bottom_code = VGroup(*[
            fit(Text(l, color=cream, font_size=17, font=MONO)) for l in bottom_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        bottom_tag = fit(Text(
            "-> a law firm,\nnot a regulator", color=PALETTE["crimson"], font_size=15, font=MONO,
            weight="BOLD", line_spacing=1.0,
        ))
        bottom_block = VGroup(bottom_label, bottom_code, bottom_tag).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        bottom_block.next_to(top_block, DOWN, buff=0.5)

        divider_y = (top_block.get_bottom()[1] + bottom_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=cream, stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(top_block, divider_y, side="top", margin=0.3)
        clear_of_hdivider(bottom_block, divider_y, side="bottom", margin=0.3)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(top_block, shift=DOWN * 0.1),
            FadeIn(bottom_block, shift=UP * 0.1),
            run_time=0.8,
        )

        caption = fit(Text(
            "one names who issued it;\nthe other names who\npublished about it",
            color=PALETTE["sage"], font_size=18, line_spacing=1.0,
        ))
        caption.next_to(bottom_block, DOWN, buff=0.35)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.6)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.3+0.8+0.6+0.3 = 2.5s; measured narration = 21.67s
        self.wait(19.17)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: REAL redesign. Parent is LEFT (recoverable) / RIGHT (not
# recoverable) with a vertical divider. Portrait stacks TOP / BOTTOM with a
# horizontal divider (clear_of_hdivider) — same narration order.
# --------------------------------------------------------------------------- #
class B04_TwoGroups(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text(
            "Eighteen titles split\ninto two groups", color=PALETTE["ink"],
            font_size=26, weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.6)
        self.play(Write(header), run_time=0.5)

        # TOP — recoverable: the title uses a synonym the classifier
        # didn't check for ("adviser").
        top_label = Text("RECOVERABLE", color=PALETTE["teal"], font_size=18, weight="BOLD")
        top_title = fit(Text(
            "“What Are Exempt\nReporting Advisers (ERAs)?”",
            color=PALETTE["ink"], font_size=18, line_spacing=1.05,
        ))
        top_tag = fit(Text(
            "-> contains 'adviser'", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD",
        ))
        top_block = VGroup(top_label, top_title, top_tag).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        top_block.next_to(header, DOWN, buff=0.35)

        # BOTTOM — not recoverable: a different regulator entirely (UK FCA).
        bottom_label = Text("NOT RECOVERABLE", color=PALETTE["crimson"], font_size=18, weight="BOLD")
        bottom_title = fit(Text(
            "“FCA Decision Notice...”", color=PALETTE["ink"], font_size=18,
        ))
        bottom_tag = fit(Text(
            "-> UK Financial Conduct\nAuthority — not tracked here",
            color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD", line_spacing=1.05,
        ))
        bottom_block = VGroup(bottom_label, bottom_title, bottom_tag).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        bottom_block.next_to(top_block, DOWN, buff=0.5)

        divider_y = (top_block.get_bottom()[1] + bottom_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["slate"], stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(top_block, divider_y, side="top", margin=0.3)
        clear_of_hdivider(bottom_block, divider_y, side="bottom", margin=0.3)

        self.play(Create(divider), run_time=0.3)
        self.play(
            FadeIn(top_block, shift=DOWN * 0.1),
            FadeIn(bottom_block, shift=UP * 0.1),
            run_time=0.8,
        )

        caption = fit(Text(
            "same failure mode.\nvery different reasons.",
            color=PALETTE["slate"], font_size=20, line_spacing=1.0,
        ))
        caption.next_to(bottom_block, DOWN, buff=0.4)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["crimson"], stroke_width=1.5)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.1, caption.get_corner(DR) + DOWN * 0.1
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+0.3+0.8+0.5+0.3 = 2.4s; measured narration = 25.25s
        self.wait(22.85)


# --------------------------------------------------------------------------- #
# B05 — FIX + PROOF: REAL redesign. Parent is a 4-column table (feed /
# items / before / after), 5 rows + a total row. Portrait restacks every
# row as its own vertical mini-card, one column, same changed-rows and
# 18->8 total highlights.
# --------------------------------------------------------------------------- #
class B05_FixAndProofTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        ink = PALETTE["ink"]

        header = fit(Text(
            "Live test — all 5\nreal feeds, today", color=ink, font_size=24,
            weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.6)
        self.play(Write(header), run_time=0.5)

        rows_data = [
            ("Federal Register - Securities", "146 items · 0 -> 0", PALETTE["ink"]),
            ("CFTC Regulations", "12 items · 0 -> 0", PALETTE["ink"]),
            ("SEC Press Releases", "25 items · 0 -> 0", PALETTE["ink"]),
            ("FINRA (Google News)", "100 items · 6 -> 4", PALETTE["crimson"]),
            ("Investment Advisor (News)", "100 items · 12 -> 4", PALETTE["crimson"]),
        ]

        row_groups = []
        for feed, counts, rcolor in rows_data:
            feed_t = fit(Text(feed, color=ink, font_size=16, weight="BOLD"))
            counts_t = fit(Text(counts, color=rcolor, font_size=15, font=MONO, weight="BOLD"))
            row = VGroup(feed_t, counts_t).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row_groups.append(row)

        table = VGroup(*row_groups).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        table.next_to(header, DOWN, buff=0.3)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.06) for r in row_groups], lag_ratio=0.15), run_time=1.0)

        # highlight the 2 changed rows (FINRA, Investment Advisor)
        changed_rows = VGroup(row_groups[3], row_groups[4])
        changed_top = changed_rows.get_top()[1] + 0.08
        changed_bottom = changed_rows.get_bottom()[1] - 0.08
        changed_box = Rectangle(
            width=3.7, height=changed_top - changed_bottom,
            stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0,
        )
        changed_box.move_to([table.get_x(), (changed_top + changed_bottom) / 2, 0])
        self.play(Create(changed_box), run_time=0.5)

        total_label = Text("TOTAL", color=ink, font_size=17, font=MONO, weight="BOLD")
        total_counts = Text("383 items", color=ink, font_size=16, font=MONO)
        total_change = Text("18 -> 8", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        # buff=0.3 (not 0.08) — GATE B's --curve-strict flagged
        # "383 items" as sitting on a curve: the gold box_around() padding
        # (0.14) around total_change exceeded the original 0.08 gap, so its
        # top stroke intruded into total_counts's own text box. A gap wider
        # than the box's own padding clears it.
        total_row = VGroup(total_label, total_counts, total_change).arrange(DOWN, buff=0.3)
        total_row.next_to(table, DOWN, buff=0.35)
        total_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["slate"], stroke_width=1.5)
        total_rule.next_to(total_row, UP, buff=0.12)
        self.play(Create(total_rule), FadeIn(total_row), run_time=0.5)

        total_box = box_around(total_change, PALETTE["gold"], buff=0.14)
        self.play(Create(total_box), run_time=0.4)

        caption = fit(Text(
            "10 of 18 recovered.\nzero already-correct\nitems reclassified.",
            color=PALETTE["slate"], font_size=17, line_spacing=1.0,
        ))
        caption.next_to(total_box, DOWN, buff=0.3)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        # animation sum = 0.5+1.0+0.5+0.5+0.4+0.5 = 3.4s; measured narration = 22.70s
        self.wait(19.30)


# --------------------------------------------------------------------------- #
# B06 — HONEST LIMIT: already a single vertical column in the parent —
# narrower widths/re-wrapped lines for the portrait column, same
# "LEFT OPEN -- BY DESIGN" framing (FACTCHECK.md row #5).
# --------------------------------------------------------------------------- #
class B06_HonestLimit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(Text(
            "The remaining eight —\ntwo real categories", color=cream,
            font_size=24, weight="BOLD", line_spacing=1.0,
        ))
        header.to_edge(UP, buff=0.62)
        self.play(Write(header), run_time=0.5)

        cat1_label = Text("NO NAMED REGULATOR", color=PALETTE["gold"], font_size=17, font=MONO, weight="BOLD")
        cat1_label = fit(cat1_label)
        cat1_example = fit(Text(
            "“Financial Regulators:\nWho They Are and\nWhat They Do”",
            color=cream, font_size=18, line_spacing=1.05,
        ))
        cat1_block = VGroup(cat1_label, cat1_example).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        cat2_label = Text("OUT-OF-SCOPE REGULATOR", color=PALETTE["gold"], font_size=17, font=MONO, weight="BOLD")
        cat2_label = fit(cat2_label)
        cat2_example = fit(Text(
            "“FCA Decision Notice...”", color=cream, font_size=18,
        ))
        cat2_note = fit(Text(
            "UK Financial Conduct\nAuthority — not tracked here", color=PALETTE["sage"], font_size=14,
            font=MONO, line_spacing=1.0,
        ))
        cat2_block = VGroup(cat2_label, cat2_example, cat2_note).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        categories = VGroup(cat1_block, cat2_block).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        categories.next_to(header, DOWN, buff=0.32)
        self.play(LaggedStart(
            FadeIn(cat1_block, shift=UP * 0.1),
            FadeIn(cat2_block, shift=UP * 0.1),
            lag_ratio=0.4,
        ), run_time=1.0)

        stamp_text = fit(Text(
            "LEFT OPEN --\nBY DESIGN", color=PALETTE["crimson"], font_size=32,
            weight="BOLD", line_spacing=1.0,
        ), 3.3)
        stamp_box = Rectangle(
            width=stamp_text.width + 0.4, height=stamp_text.height + 0.3,
            stroke_color=PALETTE["crimson"], stroke_width=4, fill_opacity=0,
        )
        stamp = VGroup(stamp_box, stamp_text)
        stamp.next_to(categories, DOWN, buff=0.28)
        self.play(Write(stamp_text), Create(stamp_box), run_time=0.7)

        caption = fit(Text(
            "not a bug i missed --\na real tradeoff,\nmade on purpose",
            color=cream, font_size=16, line_spacing=1.0,
        ))
        caption.next_to(stamp, DOWN, buff=0.2)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.12, caption.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(caption_underline), run_time=0.3)

        # animation sum = 0.5+1.0+0.7+0.5+0.3 = 3.0s; measured narration = 20.69s
        self.wait(17.69)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card. Already a single vertical column in the
# parent — re-wrapped to shorter lines, bigger type for the narrow column.
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = fit(Text(
            "Not every fix\nshould chase",
            color=PALETTE["ink"], font_size=44, line_spacing=1.05,
        ))
        line2 = fit(Text(
            "a hundred\npercent.",
            color=PALETTE["crimson"], font_size=48, line_spacing=1.05,
        ))
        line3 = fit(Text(
            "Know exactly where\nto stop — and say so.",
            color=PALETTE["slate"], font_size=30, line_spacing=1.05,
        ))
        VGroup(line1, line2, line3).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.6)
        # animation sum = 3.2s; measured narration = 8.02s
        self.wait(4.82)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI. Already a single vertical column in the
# parent — narrower rule, same composition.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font_size 62/34, buff 1.3 -> 70/38, buff 1.55 — GATE V measured
        # the first draft right at the 55% floor (marginal fail, 55%
        # rounded display masking a true value just under it); real
        # measurement confirmed this bigger-font/wider-buff combination
        # clears it with margin.
        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=70))
        accent = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(Text(
            "in for Sai Pranavi\nJeedigunta", color=PALETTE["ink"], font_size=38, line_spacing=1.05,
        ))
        VGroup(handle, accent, tagline).arrange(DOWN, buff=1.55).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        # animation sum = 1.8s; measured narration = 4.22s
        self.wait(2.42)
