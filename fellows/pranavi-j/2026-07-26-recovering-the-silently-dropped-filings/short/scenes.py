"""
Manim scenes for 2026-07-26-recovering-the-silently-dropped-filings/short
(9:16 Shorts derivative)

Built by shorts.py's "keep everything under the cap" path: 0 beats dropped,
so every beat's mp3 is the parent's unchanged narration (symlinked into
short/mp3/), and this file supplies ONLY the visual half — a portrait
(1080x1920, manim frame_width=4.5 / frame_height=8.0) re-layout of each of
the 9 parent Manim scenes in ../scenes.py. Same beat_id -> class name
mapping, same PALETTE/MONO, same per-beat animation timing (every self.play
run_time and self.wait matches the parent beat-for-beat, since the audio is
identical) — ONLY the geometry changes. THE REFORMAT RULE says generated
graphics are never auto-cropped; this file is that required hand redesign.

Portrait geometry budget (manim units): frame is 4.5 wide x 8.0 tall.
GATE B's --portrait safe box is +-1.95 x / +-3.4 y (half-extents) -> this
file targets a tighter +-1.75 x / +-3.1 y working area so W3 margin checks
clear with room to spare. Where the parent's layout was WIDE (side-by-side
columns, single long lines), this file goes TALL: multi-line Text (Pango
honors literal "\\n") replaces single long lines, and side-by-side elements
(B03's feeds-left/stages-right, B06's before/after) are restacked
top-to-bottom.

Layout pattern used repeatedly below: build a throwaway VGroup, .arrange()
it to get correct spacing automatically (no hand-guessed y-coordinates that
silently overlap), read off .get_center() for any piece that needs to become
an animated mobject (e.g. B06's always_redraw counter), then swap it in at
that same position. Safer than manually stacking narrow-frame layouts by
hand, given how little slack a 3.6-wide safe column leaves for error.
"""

from manim import *

# Portrait sync (the bn_layout fix, same one already applied in the shared
# runtime/manim/animated_graphics.py fixture): Manim CE's CLI sets pixel dims
# from `-r W,H` but does NOT recompute frame_width to match — it leaves the
# 16:9 default (14.22) and instead stretches frame_height to preserve that
# width, so a portrait scene composed against an assumed 4.5-unit-wide frame
# actually renders at roughly a third of its intended size, clustered in the
# middle of a much taller effective canvas (confirmed by a probe render: a
# point at manim (0, 4, 0) — the intended frame top — landed at ~1/3 of the
# way to the real edge). Keep frame_height 8.0, derive frame_width from the
# real pixel aspect, exactly like the shared fixture does.
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


class B00_TitleCard(Scene):
    """Silent title card — no narration. Portrait: title wraps to two lines
    (one long line at any legible font blew well past the 3.6-wide safe
    column), rules shortened to match. Same bracket-the-title composition as
    the parent (top AND bottom rule) so a title+handle-only card still earns
    real canvas coverage instead of a small center cluster."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The Pipeline That\nWas Lying to Me",
            color=PALETTE["ink"], font_size=46, weight="BOLD", line_spacing=1.0,
        ))

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=32)

        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.1
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        self.wait(2.58)


class B01_ExecSummary(Scene):
    """Spoken personal-intro / executive-summary card. Portrait: name and
    summary wrap to two lines each; same 4-element name+role+accent+summary
    stack as the parent, just narrower."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text(
            "Sai Pranavi J.", color=PALETTE["ink"], font_size=62,
            weight="BOLD", line_spacing=1.0,
        ))
        role = fit(Text(
            "Humanitarians AI Fellow", color=PALETTE["slate"], font_size=30,
        ))
        accent = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        summary = fit(Text(
            "Recovering silently-dropped\nSEC and exchange filings",
            color=PALETTE["ink"], font_size=34, line_spacing=1.0,
        ))

        # buff raised 0.75->1.15 and font sizes enlarged (2026-10-20): the
        # "Sai Pranavi J." retrofit shortened `name` from two lines to one,
        # which dropped real measured canvas-fill coverage below GATE V's
        # 55% floor (measured 51%) — recovered with bigger type + spacing.
        VGroup(name, role, accent, summary).arrange(DOWN, buff=1.15).move_to(ORIGIN)
        summary_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(name, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        summary_underline.put_start_and_end_on(
            summary.get_corner(DL) + DOWN * 0.12, summary.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(summary_underline), run_time=0.3)
        # retimed 2026-10-20: narration shortened to 13.22s after the
        # "Sai Pranavi J." retrofit (was 13.87s) — 2.8s of animation above,
        # remaining hold is 10.42s.
        self.wait(10.42)


class B02_CalmDashboard(Scene):
    """Calm feed log. Portrait: rows shortened (abbreviated, not truncated —
    same 5 feeds, same verdicts) and given more vertical breathing room since
    a 9:16 frame has far more spare height than a 16:9 one."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = Text(
            "regulatory-feed.log — live", color=PALETTE["ink"],
            font_size=17, font=MONO
        )
        header.to_edge(UP, buff=0.7)
        underline = Line(
            header.get_corner(DL) + DOWN * 0.15, header.get_corner(DR) + DOWN * 0.15,
            color=PALETTE["slate"], stroke_width=1
        )
        self.play(Write(header), Create(underline), run_time=0.6)
        self.wait(0.3)

        rows = [
            "[SEC]    Form 8-K — Officer chg",
            "[FINRA]  Rule filing — routine",
            "[CFTC]   No-action — extension",
            "[FedReg] Proposed rule — open",
            "[SEC]    Prospectus supplement",
        ]
        y = 2.3
        cursor = None
        for r in rows:
            m = fit(Text(r, color=PALETTE["ink"], font_size=17, font=MONO))
            m.move_to([0, y, 0])
            target = m.get_left() + LEFT * 0.25
            if cursor is None:
                cursor = Dot(target, radius=0.06, color=PALETTE["teal"])
                self.play(FadeIn(cursor), FadeIn(m, shift=UP * 0.1), run_time=0.5)
            else:
                self.play(cursor.animate.move_to(target), FadeIn(m, shift=UP * 0.1), run_time=0.5)
            y -= 0.85

        self.play(FadeOut(cursor), run_time=0.3)
        self.wait(4.7)


class B03_PipelineDiagram(Scene):
    """5 RSS feeds -> normalize -> score -> Postgres -> email alert.

    PORTRAIT REDESIGN (the beat named explicitly as needing one): the
    parent's side-by-side layout (5 feeds stacked on the LEFT, 4 stages in a
    row on the RIGHT) does not fit a 3.6-wide column. Restacked as: 5 feed
    chips in a single horizontal row up top (they're short labels, still fit
    across), converging down through one merge point into a vertical column
    of the 4 pipeline stages below — so the diagram now reads top-to-bottom
    the way the narration walks through it (feeds -> pipeline), rather than
    left-to-right. The empty-description filter callout moves from
    below-the-first-stage (no vertical room was the old plan) to
    beside-the-first-stage, arrowed in from the right where the narrow
    column still has a little width to spare.
    """

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Project 29 — Regulatory\nIntelligence Pipeline",
            color=PALETTE["ink"], font_size=22, line_spacing=1.0,
        )).to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.6)
        self.wait(0.5)

        feeds = ["SEC", "FINRA", "CFTC", "FR-Sec", "FR-CFTC"]
        stages = ["Normalize", "Score", "Postgres", "Email"]

        feed_boxes = VGroup(*[
            RoundedRectangle(
                width=0.66, height=0.42, corner_radius=0.05,
                fill_color=PALETTE["slate"], fill_opacity=0.05,
                stroke_color=PALETTE["slate"], stroke_width=1.3
            )
            for _ in feeds
        ]).arrange(RIGHT, buff=0.08)
        feed_boxes.next_to(title, DOWN, buff=0.45)

        feed_labels = VGroup(*[
            fit(Text(name, color=PALETTE["ink"], font_size=11), max_w=0.6).move_to(box)
            for name, box in zip(feeds, feed_boxes)
        ])

        self.play(
            LaggedStart(*[Create(b) for b in feed_boxes], lag_ratio=0.15),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[Write(l) for l in feed_labels], lag_ratio=0.15),
            run_time=1.0
        )
        self.wait(2.0)

        stage_boxes = VGroup(*[
            RoundedRectangle(
                width=1.85, height=0.5, corner_radius=0.07,
                fill_color=PALETTE["teal"], fill_opacity=0.06,
                stroke_color=PALETTE["teal"], stroke_width=1.6
            )
            for _ in stages
        ]).arrange(DOWN, buff=0.42).move_to(DOWN * 0.55)

        stage_labels = VGroup(*[
            Text(name, color=PALETTE["ink"], font_size=17).move_to(box)
            for name, box in zip(stages, stage_boxes)
        ])

        merge_point = Dot(feed_boxes.get_bottom() + DOWN * 0.35, color=PALETTE["ink"], radius=0.03)
        feed_arrows = VGroup(*[
            Arrow(box.get_bottom(), merge_point.get_center(), buff=0.05,
                  color=PALETTE["ink"], stroke_width=1.4, max_tip_length_to_length_ratio=0.15)
            for box in feed_boxes
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in feed_arrows], lag_ratio=0.1), run_time=0.9)

        stage_arrows = VGroup()
        for i in range(len(stage_boxes) - 1):
            stage_arrows.add(
                Arrow(stage_boxes[i].get_bottom(), stage_boxes[i + 1].get_top(),
                      buff=0.06, color=PALETTE["ink"], stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.25)
            )
        entry_arrow = Arrow(merge_point.get_center(), stage_boxes[0].get_top(),
                             buff=0.06, color=PALETTE["ink"], stroke_width=1.5,
                             max_tip_length_to_length_ratio=0.2)

        self.play(GrowArrow(entry_arrow), run_time=0.4)
        for i, (box, label) in enumerate(zip(stage_boxes, stage_labels)):
            self.play(Create(box), Write(label), run_time=0.6)
            if i < len(stage_arrows):
                self.play(GrowArrow(stage_arrows[i]), run_time=0.35)
        self.wait(0.5)

        filter_note = fit(Text(
            "checks: has\ndescription?",
            color=PALETTE["crimson"], font_size=12, line_spacing=0.9
        ), max_w=0.75).next_to(stage_boxes[0], RIGHT, buff=0.15)
        filter_arrow = Arrow(
            filter_note.get_left(), stage_boxes[0].get_right(),
            buff=0.08, color=PALETTE["crimson"], stroke_width=2,
            max_tip_length_to_length_ratio=0.25
        )
        # FadeIn, not Write: Write() traces text via a progressive stroke
        # outline that (at this small a font) briefly renders as a pale
        # near-white sliver before the fill catches up — GATE V's mid-beat
        # sample landed exactly in that transient window and read it as
        # low-contrast. FadeIn ramps the same crimson fill's opacity instead
        # of tracing an outline, so every visible frame is on-palette.
        self.play(FadeIn(filter_note), GrowArrow(filter_arrow), run_time=0.9)
        self.wait(10.0)


class B04_ClaudeCodeDiff(Scene):
    """The removed empty-description filter — Claude Code diff view.
    Portrait: every code line wraps to 2-3 short lines instead of one long
    monospace line; the REMOVED tag moves from beside the removed line
    (no width for it in a 3.6-wide column) to directly beneath it."""

    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = fit(Text(
            "workflow.dev.json —\nNormalize Data node",
            color=cream, font_size=16, font=MONO, line_spacing=1.0,
        )).to_edge(UP, buff=0.6)
        self.play(Write(header), run_time=0.6)

        ctx1 = fit(Text(
            "const hasContent =\n  item.content &&\n  item.content.trim();",
            color=cream, font_size=14, font=MONO, line_spacing=1.0,
        ))
        removed = fit(Text(
            "- if (!hasContent)\n    return null;\n    // drop silently",
            color=PALETTE["crimson"], font_size=14, font=MONO, line_spacing=1.0,
        ))
        note = fit(Text(
            "// SEC/exchange filings\n// often arrive title-only",
            color=PALETTE["gold"], font_size=13, font=MONO, line_spacing=1.0,
        ))

        code = VGroup(ctx1, removed, note).arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(UP * 0.35)

        self.play(FadeIn(ctx1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(removed), run_time=0.7)
        self.wait(0.5)

        def box_around(text_mob, color, buff=0.12):
            r = Rectangle(width=text_mob.width + 2 * buff, height=text_mob.height + 2 * buff,
                          color=color, stroke_width=2)
            r.move_to(text_mob.get_center())
            return r

        highlight = box_around(removed, PALETTE["crimson"])
        self.play(Create(highlight), run_time=0.6)

        removed_tag = Text(
            "REMOVED", color=PALETTE["sage"], font_size=14, font=MONO
        ).next_to(highlight, DOWN, buff=0.12, aligned_edge=RIGHT)
        self.play(Write(removed_tag), run_time=0.6)
        self.wait(0.5)

        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.0)

        result = fit(Text(
            "-> title-only items\nnow pass through",
            color=PALETTE["sage"], font_size=15, line_spacing=1.0,
        )).next_to(code, DOWN, buff=0.7)
        self.play(Write(result), run_time=0.8)
        self.play(Transform(highlight, box_around(result, PALETTE["sage"])), run_time=0.6)
        self.wait(8.4)


class B05_RecoveredFilings(Scene):
    """Recovered title-only filings list. Portrait: long items wrap to two
    lines; extra vertical buff between rows absorbs the taller ones without
    hand-tuned y-coordinates."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Recovered — title-only\nfilings", color=PALETTE["ink"], font_size=22,
            line_spacing=1.0,
        )).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.6)

        items = [
            "Cboe Clear U.S.",
            "MEMX LLC",
            "Nasdaq GEMX\nSRO notice",
            "US v. Edwards\nLifeSciences (DOJ antitrust)",
        ]
        rows = []
        for it in items:
            check = Text("check:", color=PALETTE["sage"], font_size=18, font=MONO)
            label = Text(it, color=PALETTE["ink"], font_size=18, line_spacing=1.0)
            row = fit(VGroup(check, label).arrange(RIGHT, buff=0.25), max_w=3.4)
            rows.append(row)

        VGroup(*rows).arrange(DOWN, buff=0.55).move_to(DOWN * 0.3)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.6)

        self.wait(3.8)


class B06_BeforeAfterCount(Scene):
    """297 -> 370 items passed the filter.

    PORTRAIT REDESIGN (the other beat named explicitly): the parent's
    BEFORE/AFTER counters sit side by side; stacked side by side at a big
    font_size=80 they'd collide well before reaching a 3.6-wide safe column.
    Restacked top-to-bottom instead — BEFORE above, AFTER below, same order
    the narration already implies ('the result: seventy-three additional
    items') — with the delta and caveat beneath. A throwaway VGroup does the
    spacing so nothing overlaps, then the AFTER counter is swapped for an
    always_redraw ValueTracker at the same resolved position."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "Live feed run — items\npassed the filter",
            color=PALETTE["ink"], font_size=25, line_spacing=1.0,
        )).to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.6)

        # layout pass: stack every element to get correct spacing, then read
        # off the AFTER-number slot's resolved position before swapping in
        # the animated always_redraw counter there.
        before_label = Text("BEFORE", color=PALETTE["ink"], font_size=24)
        before_num = Text("297", color=PALETTE["crimson"], font_size=168)
        after_label = Text("AFTER", color=PALETTE["ink"], font_size=24)
        after_num_slot = Text("370", color=PALETTE["teal"], font_size=168)  # placeholder for layout only
        delta = Text("+73 recovered", color=PALETTE["sage"], font_size=28)
        caveat = fit(Text(
            "title-only filings the empty-\ndescription filter had dropped",
            color=PALETTE["ink"], font_size=17, line_spacing=1.0,
        ), max_w=3.4)

        layout = VGroup(
            VGroup(before_label, before_num).arrange(DOWN, buff=0.2),
            VGroup(after_label, after_num_slot).arrange(DOWN, buff=0.2),
            delta, caveat,
        ).arrange(DOWN, buff=0.3)
        layout.next_to(title, DOWN, buff=0.02)

        after_pos = after_num_slot.get_center()
        after_num_slot.set_opacity(0)  # keep it for layout math; never shown

        after_tracker = ValueTracker(297)
        after_num = always_redraw(lambda: Text(
            str(int(round(after_tracker.get_value()))),
            color=PALETTE["teal"], font_size=168
        ).move_to(after_pos))

        self.play(FadeIn(before_label), FadeIn(before_num), run_time=0.5)
        self.play(FadeIn(after_label), FadeIn(after_num), run_time=0.5)
        self.wait(0.3)

        self.play(after_tracker.animate.set_value(370), run_time=1.4, rate_func=smooth)

        self.play(Write(delta), run_time=0.6)
        self.play(FadeIn(caveat), run_time=0.5)
        self.wait(1.5)


class B07_Statement(Scene):
    """Silent filters don't fail loudly. They fail invisibly. Portrait:
    line 1 wraps to two lines; both lines narrowed to the safe column."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # Bigger, poster-style type (not just wider spacing) — a 2-element
        # statement card needs its TEXT to carry the canvas-fill floor, not
        # an artificially huge gap between two short lines.
        line1 = fit(Text(
            "Silent filters\ndon't fail loudly.", color=PALETTE["ink"], font_size=58,
            line_spacing=1.05,
        ))
        line2 = fit(Text(
            "They fail\ninvisibly.", color=PALETTE["crimson"], font_size=62,
            line_spacing=1.05,
        ))
        VGroup(line1, line2).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.4)
        self.play(Write(line2), run_time=1.0)
        self.wait(5.0)


class B08_BrandOutro(Scene):
    """@HumanitariansAI — fixed with Claude Code. Already compact in the
    parent; portrait only needs a slightly shorter accent rule and a touch
    less font size to sit comfortably inside the narrower safe column."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=66))
        accent = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(Text("Fixed with Claude Code", color=PALETTE["ink"], font_size=42))
        VGroup(handle, accent, tagline).arrange(DOWN, buff=1.95).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        self.wait(2.7)
