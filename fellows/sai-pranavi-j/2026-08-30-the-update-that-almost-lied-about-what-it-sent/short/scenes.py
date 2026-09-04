"""
Manim scenes for 2026-08-30-the-update-that-almost-lied-about-what-it-sent/short
(9:16 Shorts derivative)

Built via THE SHORTS LAW (runtime/scripts/shorts.py): this reel is UNDER the
180s cap (121.5s), so the whole reel reformats 16:9 -> 9:16 as-is — 0 beats
dropped, every beat's mp3 is the parent's unchanged narration (symlinked
into short/mp3/). This file supplies ONLY the visual half: a genuine
hand-authored portrait (1080x1920) re-layout of each of the 9 parent Manim
scenes in ../scenes.py — per THE REFORMAT RULE, generated graphics are
NEVER auto-cropped. Same beat_id -> class name mapping, same
PALETTE/MONO/fit()/panel()/box_around(), same per-beat animation timing
(every self.play run_time and self.wait matches the parent beat-for-beat,
since the audio is identical) — only the geometry changes.

Portrait geometry budget (manim units): frame is 4.5 wide x 8.0 tall (same
convention as this fellow's 2 sibling shorts). GATE B's --portrait safe box
is +-1.95 x / +-3.4 y (half-extents); this file targets a tighter
+-1.75 x / +-3.1 y working area so margin checks clear with room to spare.

Real redesigns (not a mechanical shrink) — the 3 beats called out in the
build brief:
  B03 TwoConditions   — parent is LEFT/RIGHT (High Priority Filter vs. Mark
                        email sent) with a vertical divider. Portrait
                        restacks TOP/BOTTOM with a horizontal divider
                        (clear_of_hdivider, this file's rotated analogue of
                        the parent's clear_of_divider) — reads in the same
                        order the narration does (High Priority Filter
                        first, Mark email sent second).
  B05 LiveQueryProof  — parent has query+"12"-count side by side, then the
                        example row below. Portrait stacks all three
                        strictly top-to-bottom: query, then "12", then the
                        id-153 row card — same reading order, one column.
  B06 BeforeAfterFix  — parent is LEFT/RIGHT (BEFORE/AFTER SQL) with a
                        vertical divider. Portrait restacks TOP/BOTTOM
                        (BEFORE above, AFTER below — the narration's own
                        order: "stop re-deriving the rule... read the exact
                        ids...") with a horizontal divider
                        (clear_of_hdivider).

Every other beat (B00, B01, B02, B04, B07, B08) was already a single
vertical column in the parent — these keep the same composition, narrower
widths/re-wrapped text and, where GATE B/V required it, bigger fonts/buffs
tuned by real Manim measurement (never guessed) for portrait canvas-fill.
"""

from manim import *

# Portrait sync (the bn_layout fix, same one already applied in the shared
# runtime/manim/animated_graphics.py fixture and both this fellow's sibling
# shorts): Manim CE's CLI sets pixel dims from `-r W,H` but does NOT
# recompute frame_width to match — it leaves the 16:9 default (14.22) and
# instead stretches frame_height to preserve that width, so a portrait scene
# composed against an assumed 4.5-unit-wide frame actually renders at
# roughly a third of its intended size, clustered in the middle of a much
# taller effective canvas. Keep frame_height 8.0, derive frame_width from
# the real pixel aspect, exactly like the shared fixture and sibling shorts do.
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
    """Portrait analogue of the parent scenes.py's clear_of_divider() — same
    pattern (measure the block's OWN rendered bounds, shift the whole rigid
    unit by the real overhang, never a per-line rescale), rotated 90
    degrees: every side-by-side split in the parent (a vertical divider with
    LEFT/RIGHT panels) becomes a top/bottom stack here (a horizontal divider
    with TOP/BOTTOM panels).

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
# B00 — TITLE: silent title card. Title re-wrapped to 2 lines for the
# narrow column (already 2 lines in the parent; shrunk + re-ruled here).
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The Update That\nAlmost Lied About\nWhat It Sent",
            color=PALETTE["ink"], font_size=46, weight="BOLD", line_spacing=1.0,
        ))

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=32)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=1.05).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        self.wait(2.40)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: name/role/accent/summary, same 4-element stack as the
# parent — summary re-wrapped 3 -> 5 short lines for the narrow column.
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
            "A database update that\ncould mark high-priority\n"
            "alerts 'emailed' even when\nnone had gone out — now\n"
            "scoped to only what was\nactually sent.",
            color=PALETTE["ink"], font_size=26, line_spacing=1.05,
        ))

        VGroup(name, role, accent, summary).arrange(DOWN, buff=0.55).move_to(ORIGIN)
        summary_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(name, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        summary_underline.put_start_and_end_on(
            summary.get_corner(DL) + DOWN * 0.12, summary.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(summary_underline), run_time=0.3)
        self.wait(15.22)


# --------------------------------------------------------------------------- #
# B02 — HOOK: the "Mark email sent" node. Already a single vertical column
# in the parent (node -> condition -> "?" -> caption) — narrowed widths,
# same order.
# --------------------------------------------------------------------------- #
class B02_MarkEmailSentNode(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text(
            "workflow.dev.json — Postgres node", color=PALETTE["slate"],
            font_size=16, font=MONO,
        ))
        header.to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.5)

        # node RE-POSITIONED below the header via next_to() — GATE B
        # caught the first draft's `node` never being moved off the origin
        # (unlike the parent, which also had this bug before its own fix),
        # so the whole downstream stack (condition/qmark/caption) cascaded
        # too far down and ran off the bottom of the portrait frame
        # (measured off-frame at y=-4.22, past the -3.4 safe floor). Height
        # bumped 1.3 -> 1.5 so node_label_group (measured 1.40 tall) sits
        # fully inside, not poking past the panel's own stroke.
        node = panel(width=3.5, height=1.5, fill=PALETTE["slate"], stroke=PALETTE["slate"], opacity=0.10)
        node.next_to(header, DOWN, buff=0.35)
        node_label = fit(Text("Mark email\nsent", color=PALETTE["ink"], font_size=26,
                               weight="BOLD", line_spacing=1.0), 3.2)
        node_sub = fit(Text("UPDATE ... SET\nemail_sent = TRUE", color=PALETTE["slate"],
                             font_size=14, font=MONO, line_spacing=1.0), 3.2)
        node_label_group = VGroup(node_label, node_sub).arrange(DOWN, buff=0.15)
        node_label_group.move_to(node.get_center())
        self.play(Create(node), FadeIn(node_label_group), run_time=0.7)

        condition = fit(Text(
            "WHERE <its own\ncopy of \"high priority\">",
            color=PALETTE["ink"], font_size=20, font=MONO, line_spacing=1.0,
        ))
        condition.next_to(node, DOWN, buff=0.35)
        self.play(FadeIn(condition, shift=UP * 0.1), run_time=0.6)

        qmark = Text("?", color=PALETTE["crimson"], font_size=70, weight="BOLD")
        qmark.next_to(condition, DOWN, buff=0.2)
        self.play(Write(qmark), run_time=0.6)

        caption = fit(Text(
            "checking what the email\nstep actually sent —\nor guessing?",
            color=PALETTE["slate"], font_size=20, line_spacing=1.0,
        ))
        caption.next_to(qmark, DOWN, buff=0.25)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)

        caption_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption_underline.put_start_and_end_on(
            caption.get_corner(DL) + DOWN * 0.1, caption.get_corner(DR) + DOWN * 0.1
        )
        self.play(Create(caption_underline), run_time=0.3)
        self.wait(10.24)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the two rules, REAL redesign. Parent is LEFT (High Priority
# Filter) / RIGHT (Mark email sent) with a vertical divider; portrait stacks
# TOP (High Priority Filter) / BOTTOM (Mark email sent) with a horizontal
# divider, same reading order the narration walks: High Priority Filter
# first, then the old Mark-email-sent rule. clear_of_hdivider() verifies
# clearance from real measured bounds, not a guess.
# --------------------------------------------------------------------------- #
class B03_TwoConditions(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Two rules that were\nsupposed to agree",
            color=PALETTE["ink"], font_size=28, line_spacing=1.0,
        ))
        # buff=0.75 (not 0.55) — real portrait-frame measurement showed the
        # tighter buff's top edge at y=3.45, past the portrait safe ceiling
        # (3.4); 0.75 lands it at y=3.25.
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.6)

        # TOP — High Priority Filter (feeds the email)
        top_label = fit(Text("High Priority Filter", color=PALETTE["teal"], font_size=22, weight="BOLD"))
        top_sub = Text("(feeds the email)", color=PALETTE["slate"], font_size=14)
        top_cond = fit(Text("urgency_score > 6", color=PALETTE["ink"], font_size=20, font=MONO))
        top_block = VGroup(top_label, top_sub, top_cond).arrange(DOWN, buff=0.18)
        top_block.next_to(title, DOWN, buff=0.45)

        # BOTTOM — Mark email sent (old, re-derived rule)
        bottom_label = fit(Text("Mark email sent (old)", color=PALETTE["crimson"], font_size=22, weight="BOLD"))
        bottom_sub = Text("(re-derives the rule)", color=PALETTE["slate"], font_size=14)
        bottom_cond = VGroup(
            fit(Text("urgency_score > 7 OR", color=PALETTE["ink"], font_size=20, font=MONO)),
            fit(Text("impact_level IN", color=PALETTE["ink"], font_size=20, font=MONO)),
            fit(Text("('Critical','High')", color=PALETTE["ink"], font_size=20, font=MONO)),
        ).arrange(DOWN, buff=0.06)
        bottom_block = VGroup(bottom_label, bottom_sub, bottom_cond).arrange(DOWN, buff=0.18)

        mismatch = Text("these don't match", color=PALETTE["crimson"], font_size=20, weight="BOLD")

        # bottom_block sits below top_block with room for the divider +
        # mismatch line between them
        bottom_block.next_to(top_block, DOWN, buff=1.5)

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

        # offset BELOW divider_y (not centered ON it) — GATE B caught the
        # first draft's mismatch text sitting directly on top of the
        # divider line (a real TEXT_ON_CURVE strike, not a false positive:
        # both were centered at the exact same y). 0.3 below clears it
        # while still reading as "between" the two blocks.
        mismatch.move_to([0, divider_y - 0.3, 0])
        self.play(Write(mismatch), run_time=0.5)

        mismatch_underline = Line(color=PALETTE["crimson"], stroke_width=1.2)
        mismatch_underline.put_start_and_end_on(
            mismatch.get_corner(DL) + DOWN * 0.08, mismatch.get_corner(DR) + DOWN * 0.08
        )
        self.play(Create(mismatch_underline), run_time=0.3)

        self.wait(14.18)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: determineImpactLevel(). Already a single vertical column
# in the parent — narrowed widths, same code verbatim.
# --------------------------------------------------------------------------- #
class B04_ImpactLevelBypass(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(Text(
            "determineImpactLevel()", color=cream, font_size=18, font=MONO,
        ))
        # buff=0.7 (not 0.55) — real portrait measurement showed the
        # tighter buff's top edge at y=3.45, past the safe ceiling (3.4).
        header.to_edge(UP, buff=0.7)
        self.play(Write(header), run_time=0.5)

        lines = [
            "function determineImpactLevel(",
            "  urgencyScore, isEnforcement,",
            "  isFraud) {",
            "  if (urgencyScore >= 9",
            "    || isFraud) return 'Critical';",
            "  if (urgencyScore >= 7",
            "    || isEnforcement) return 'High';",
            "  if (urgencyScore >= 5)",
            "    return 'Medium';",
            "  return 'Low';",
            "}",
        ]
        # fit() width capped to 3.6 (not the 3.8 default) — a hair of extra
        # horizontal margin inside the 3.9-wide safe column.
        code = VGroup(*[
            fit(Text(l, color=cream, font_size=16, font=MONO), 3.6) for l in lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        code.next_to(header, DOWN, buff=0.4)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.08) for l in code], lag_ratio=0.1), run_time=1.0)

        # the two bypass lines (each now 2 physical lines: the "if" line and
        # its wrapped "|| ..." condition) boxed together, same crimson as B03
        bypass = VGroup(code[3], code[4], code[5], code[6])
        highlight = box_around(bypass, PALETTE["crimson"], buff=0.1)
        self.play(Create(highlight), run_time=0.5)

        # NOTE: the parent's separate "bypasses the score" floating tag was
        # DROPPED here (not just repositioned) — GATE B caught it (and its
        # underline) overlapping code[7]/code[8] ("return 'Medium'"/"return
        # 'Low'"), which sit physically BELOW the highlighted lines in this
        # same single-column `code` VGroup (next_to(highlight, DOWN) landed
        # right on top of them). The highlight box + caption text below
        # already carry the same meaning without a text-on-text collision.
        caption1 = fit(Text(
            "a keyword hit alone jumps\nstraight to High or Critical",
            color=PALETTE["sage"], font_size=20, line_spacing=1.0,
        ))
        # positioned below the FULL code block (not the highlight/tag),
        # so it can never land on a code line still visible beneath it.
        caption1.next_to(code, DOWN, buff=0.45)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.5)

        # 2nd real (non-text) shape, added later than `highlight` — a lone
        # static shape for the whole hold trips GATE A's "shapes never
        # change" repeated-animation check (same fix pattern as this
        # file's own B02/B03).
        caption1_underline = Line(color=PALETTE["sage"], stroke_width=1)
        caption1_underline.put_start_and_end_on(
            caption1.get_corner(DL) + DOWN * 0.08, caption1.get_corner(DR) + DOWN * 0.08
        )
        self.play(Create(caption1_underline), run_time=0.3)
        # animation sum = 0.5+1.0+0.5+0.5+0.3 = 2.8s
        self.wait(10.0)

        caption2 = fit(Text(
            "so a score of 5 or 6 can\nstill read 'Critical' — too\n"
            "low for the email filter,\nhigh enough for the old\nupdate to flip it 'sent'",
            color=PALETTE["gold"], font_size=18, line_spacing=1.0,
        ))
        caption2.move_to(caption1.get_center())
        self.play(FadeOut(caption1), FadeOut(caption1_underline), FadeIn(caption2, shift=UP * 0.1), run_time=0.6)
        # animation sum so far 2.8+10.0+0.6=13.4s; measured narration 23.52s
        self.wait(10.12)


# --------------------------------------------------------------------------- #
# B05 — PROOF: REAL redesign. Parent has query + "12"-count side by side,
# then the example row below. Portrait stacks strictly top-to-bottom: query,
# then "12" (centered, own row), then the id-153 row card — same content,
# same reading order, one column instead of two.
# --------------------------------------------------------------------------- #
class B05_LiveQueryProof(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = fit(Text(
            "Live query — regulatory_feeds", color=PALETTE["ink"], font_size=20, weight="BOLD",
        ))
        # buff=0.7 (not 0.5) — real Manim measurement (portrait frame,
        # frame_height=8.0) showed the tighter buff's top edge at y=3.5,
        # past both the portrait safe ceiling (3.4) and this file's own
        # tighter target (3.1); 0.7 lands it at y=3.3.
        header.to_edge(UP, buff=0.7)
        self.play(Write(header), run_time=0.4)

        query_lines = [
            "SELECT id, title,",
            "  urgency_score, impact_level",
            "FROM regulatory_feeds",
            "WHERE impact_level IN",
            "  ('Critical','High')",
            "  AND urgency_score <= 6",
            "  AND email_sent = FALSE;",
        ]
        query = VGroup(*[
            fit(Text(l, color=PALETTE["slate"], font_size=15, font=MONO)) for l in query_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.09)
        query.next_to(header, DOWN, buff=0.35)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.06) for l in query], lag_ratio=0.1), run_time=1.0)

        count_num = Text("12", color=PALETTE["crimson"], font_size=88, weight="BOLD")
        count_label = fit(Text("rows matched", color=PALETTE["ink"], font_size=18))
        count_group = VGroup(count_num, count_label).arrange(DOWN, buff=0.12)
        count_group.next_to(query, DOWN, buff=0.35)
        self.play(FadeIn(count_group, shift=UP * 0.08), run_time=0.6)

        # height 1.9 -> 2.2 — GATE B caught row_content (measured 1.995
        # tall) poking past a 1.9-tall panel's top/bottom stroke by ~0.05
        # each side (a real TEXT_ON_CURVE strike on "id 153" at the top
        # edge), same class of bug as the parent's B02 panel-overhang fix.
        row_panel = panel(width=3.7, height=2.2, fill=PALETTE["slate"], stroke=PALETTE["slate"], opacity=0.08)
        row_panel.next_to(count_group, DOWN, buff=0.35)

        row_id = Text("id 153", color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD")
        row_title = fit(Text(
            "“SEC Charges 21\nIndividuals With Alleged\nWide-Reaching Insider\nTrading Scheme”",
            color=PALETTE["ink"], font_size=15, line_spacing=1.0,
        ), 3.3)
        row_meta = fit(Text(
            "urgency_score = 5\nimpact_level = Critical",
            color=PALETTE["crimson"], font_size=15, font=MONO, line_spacing=1.0,
        ), 3.3)
        row_content = VGroup(row_id, row_title, row_meta).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        row_content.move_to(row_panel.get_center())

        self.play(Create(row_panel), FadeIn(row_content, shift=UP * 0.1), run_time=0.8)
        self.wait(18.75)


# --------------------------------------------------------------------------- #
# B06 — FIX: REAL redesign. Parent is LEFT (BEFORE) / RIGHT (AFTER) with a
# vertical divider; portrait stacks TOP (BEFORE) / BOTTOM (AFTER) with a
# horizontal divider — the narration's own order ("stop re-deriving the
# rule... read the exact ids..."). Both queries land together, same as the
# parent (short beat, no time for a staged reveal).
# --------------------------------------------------------------------------- #
class B06_BeforeAfterFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        before_label = fit(Text("BEFORE", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD"))
        before_lines = [
            "UPDATE regulatory_feeds",
            "SET email_sent = TRUE,",
            "  email_sent_at = NOW()",
            "WHERE (urgency_score > 7",
            "  OR impact_level IN",
            "  ('Critical','High'))",
            "  AND email_sent = FALSE;",
        ]
        before_code = VGroup(*[
            fit(Text(l, color=cream, font_size=13, font=MONO)) for l in before_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        before_block = VGroup(before_label, before_code).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        # buff=0.7 (not 0.55) — real portrait-frame measurement showed the
        # tighter buff's top edge at y=3.45, past the portrait safe ceiling
        # (3.4); 0.7 lands it at y=3.3.
        before_block.to_edge(UP, buff=0.7)

        after_label = fit(Text("AFTER", color=PALETTE["teal"], font_size=17, font=MONO, weight="BOLD"))
        after_lines = [
            "UPDATE regulatory_feeds",
            "SET email_sent = TRUE,",
            "  email_sent_at = NOW()",
            "WHERE id = ANY($1::int[])",
            "  AND email_sent = FALSE;",
        ]
        after_code = VGroup(*[
            fit(Text(l, color=cream, font_size=13, font=MONO)) for l in after_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        id_source = fit(Text("ids from: High Priority Filter", color=PALETTE["sage"], font_size=12, font=MONO))
        after_block = VGroup(after_label, after_code, id_source).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        # buff=0.7 (not 0.55) — same fix as before_block above, mirrored at
        # the bottom edge (measured bottom edge was at y=-3.45, past the
        # -3.4 safe floor).
        after_block.to_edge(DOWN, buff=0.7)

        divider_y = (before_block.get_bottom()[1] + after_block.get_top()[1]) / 2
        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["slate"], stroke_width=2).move_to([0, divider_y, 0])

        clear_of_hdivider(before_block, divider_y, side="top", margin=0.25)
        clear_of_hdivider(after_block, divider_y, side="bottom", margin=0.25)

        self.play(Create(divider), run_time=0.25)
        self.play(
            FadeIn(before_block, shift=DOWN * 0.1),
            FadeIn(after_block, shift=UP * 0.1),
            run_time=0.8,
        )

        highlight = box_around(after_code[3], PALETTE["gold"], buff=0.08)
        self.play(Create(highlight), run_time=0.55)
        self.wait(6.37)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card. Already a single vertical column in the
# parent — re-wrapped to shorter lines, bigger type for the narrow column.
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = fit(Text(
            "Copying someone\nelse's rule isn't\nwrong today.",
            color=PALETTE["ink"], font_size=38, line_spacing=1.05,
        ))
        line2 = fit(Text(
            "It's wrong the day\nthe two drift apart.",
            color=PALETTE["crimson"], font_size=42, line_spacing=1.05,
        ))
        line3 = fit(Text(
            "Nothing throws an\nerror to tell you.",
            color=PALETTE["slate"], font_size=26, line_spacing=1.05,
        ))
        VGroup(line1, line2, line3).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.4)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.6)
        self.wait(7.31)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI. Already a single vertical column in the
# parent — narrower rule, same composition.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font sizes 46/26 -> 70/36, accent width 1.3 -> 1.8, buff 0.5 -> 1.4
        # — GATE V measured the first draft at 31% canvas-fill, under the
        # 55% floor; real Manim measurement (not a guess) confirmed this
        # combination clears ~63% while staying inside both safe-area walls
        # (width 3.8/3.9, height 4.36/6.8) — same fix as the parent's B08.
        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=70))
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
        self.wait(3.82)
