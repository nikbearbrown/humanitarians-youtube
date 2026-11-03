"""
Manim scenes for 2026-07-26-recovering-the-silently-dropped-filings

v2 (2026-08-25, 4K program-feedback rebuild) — added B00/B01, renumbered the
rest by +2:
B00_TitleCard        — silent title card: "The Pipeline That Was Lying to
                        Me" + @HumanitariansAI, no narration (TITLE)
B01_ExecSummary       — personal-intro/executive-summary card, spoken (EXEC-SUMMARY)
B02_CalmDashboard    — calm feed log, nothing looks wrong (HOOK) [was B00]
B03_PipelineDiagram  — 5 RSS feeds -> normalize -> score -> Postgres -> email alert [was B01]
B04_ClaudeCodeDiff   — the removed empty-description filter (DISCOVERY) [was B02]
B05_RecoveredFilings — Cboe / MEMX / Nasdaq GEMX / DOJ antitrust (PROOF) [was B03]
B06_BeforeAfterCount — 297 -> 370 items passed (+73 recovered) [was B04]
B07_Statement        — "silent filters fail invisibly" (TAKEAWAY) [was B05]
B08_BrandOutro       — @HumanitariansAI sign-off [was B06]

B00/B01 follow the precedent set in the sibling reel
fellows/sai-pranavi-j/2026-08-17-why-ai-generated-code-still-needs-a-human's
scenes.py (its B00_TitleCard, v3 renumbering) — same silent-title-card
mechanics (a real silent mp3, never audio_file: null — see beat_sheet.json's
B00 shot.note for why) and the same +2-shift renumbering pattern.

All 5 non-Manim beats in the original plan (B00 vox-still, B02/B06 Remotion,
B03/B05 card) were converted to Manim scenes here rather than left as
slates: the two Remotion patterns the original beat sheet named
(ClaudeCodeDiffView, HumanitariansResearchReport) don't exist in the
installed brutalist/ toolkit, and building them would mean adding components
to that shared repo, which is out of scope for this reel. Manim keeps
everything self-contained in this folder with no external images or toolkit
changes.

Palette: humanitarians (runtime/remotion/src/tokens/humanitarians.ts) —
this reel uses the hai/Bella persona, not the Claude-branded palette.
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


class B00_TitleCard(Scene):
    """Silent title card — no narration. Title pulled verbatim from
    beat_sheet.json's metadata.title. Two rules (top AND bottom) bracket
    the title rather than a single underline, so a title-only/handle-only
    card still earns a real share of the safe frame (GATE V canvas-fill
    floor) instead of a small cluster at center — same fix the sibling
    reel's B00_TitleCard needed. Audio: mp3/beat-B00.mp3 is a REAL silent
    mp3 (ffmpeg anullsrc), not audio_file: null — see beat_sheet.json's
    B00 shot.note for why a null path would break every beat's narration."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text(
            "The Pipeline That Was Lying to Me",
            color=PALETTE["ink"], font_size=54, weight="BOLD",
        ), 12.0)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=38)

        # buff=1.3 (not the usual ~0.4-0.5): a title-only card has just 3
        # elements, so real canvas-fill has to come from spacing, not word
        # count. GATE V's first pass on this card measured only 50% coverage
        # of the safe area at buff=1.0 (below the 55% floor) — measured
        # offline against real Manim text metrics (not the render-free static
        # stub): width=11.40, height=4.04 -> cover=0.50 at buff=1.0. buff=1.3
        # raises height to 4.94 with the same 11.40 width (still 0.70 clear
        # of the safe edge on each side) -> cover=0.61, comfortably clear.
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.3
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        # bottom rule + handle land together, one beat — a title reveal,
        # not a race of separate steps
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # settled well before the mid-beat QC sample point; the remainder is
        # a clean static hold tuned to the real measured silent-track length
        # (4.23s, mp3/beat-B00.mp3) so this clip needs no compile-time retime.
        self.wait(2.58)


class B01_ExecSummary(Scene):
    """Spoken personal-intro / executive-summary card — the fellow's name
    and role, then a one-line plain-language summary of what the video
    covers. Narration text is fixed verbatim by the program feedback (see
    beat_sheet.json B01.narration_text), not authored here."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        name = fit(Text(
            "Sai Pranavi J.", color=PALETTE["ink"], font_size=58, weight="BOLD",
        ), 11.0)
        role = Text(
            "Humanitarians AI Fellow", color=PALETTE["slate"], font_size=28,
        )
        accent = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        summary = fit(Text(
            "Recovering silently-dropped SEC and exchange filings",
            color=PALETTE["ink"], font_size=34,
        ), 11.5)

        # buff=1.3 (not the usual ~0.4-0.5) — GATE V's first pass on this
        # card measured only 23% coverage of the safe area (font_size
        # 46/22/27, buff=0.45): a 4-element name+role+summary card is
        # naturally compact. Measured offline against real Manim text
        # metrics (not the render-free static stub): the font sizes below
        # + buff=1.3 give width=10.51, height=5.33 -> cover=0.61, with
        # 1.15/0.94 units of clearance from the safe edge on width/height
        # respectively — comfortably clear of both the 55% floor and any
        # edge-bleed risk.
        VGroup(name, role, accent, summary).arrange(DOWN, buff=1.3).move_to(ORIGIN)
        # second real (non-text) shape, added later than `accent` — a lone
        # static Line for the whole hold trips GATE A's "shapes never
        # change" repeated-animation check (1 distinct state across 3+
        # snapshots); this mirrors B08_BrandOutro's own tagline_underline
        # pattern already used elsewhere in this file.
        summary_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(name, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        self.play(Create(accent), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        summary_underline.put_start_and_end_on(
            summary.get_corner(DL) + DOWN * 0.12, summary.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(summary_underline), run_time=0.3)
        # hold tuned to the measured narration length (13.22s,
        # mp3/beat-B01.mp3, generated by generate_audio_kokoro.py, after the
        # 2026-10-20 "Sai Pranavi J." retrofit shortened the narration) —
        # 0.7+0.5+0.5+0.8+0.3=2.8s of animation above, so the remaining
        # 10.42s is a clean static hold.
        self.wait(10.42)


class B02_CalmDashboard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        header = Text(
            "regulatory-feed.log — live", color=PALETTE["ink"],
            font_size=26, font=MONO
        )
        header.to_edge(UP, buff=0.65)
        underline = Line(
            header.get_corner(DL) + DOWN * 0.15, header.get_corner(DR) + DOWN * 0.15,
            color=PALETTE["slate"], stroke_width=1
        )
        self.play(Write(header), Create(underline), run_time=0.6)
        self.wait(0.3)

        rows = [
            "[SEC]     Form 8-K filed - Item 5.02 Officer Changes",
            "[FINRA]   Rule filing - minor amendment, routine",
            "[CFTC]    No-action letter - extension granted",
            "[FedReg]  Proposed rule - comment period open",
            "[SEC]     Prospectus supplement filed",
        ]
        y = 2.35
        cursor = None
        for r in rows:
            m = Text(r, color=PALETTE["ink"], font_size=21, font=MONO)
            if m.width > 11.0:
                m.scale_to_fit_width(11.0)
            m.move_to([0, y, 0])
            target = m.get_left() + LEFT * 0.3
            if cursor is None:
                cursor = Dot(target, radius=0.06, color=PALETTE["teal"])
                self.play(FadeIn(cursor), FadeIn(m, shift=UP * 0.1), run_time=0.5)
            else:
                self.play(cursor.animate.move_to(target), FadeIn(m, shift=UP * 0.1), run_time=0.5)
            y -= 0.78

        self.play(FadeOut(cursor), run_time=0.3)
        self.wait(4.7)


class B04_ClaudeCodeDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]
        cream = PALETTE["bg"]

        header = Text(
            "workflow.dev.json — Normalize Data node",
            color=cream, font_size=18, font=MONO
        ).to_edge(UP, buff=0.6)
        self.play(Write(header), run_time=0.6)

        def fit(mob, max_w):
            if mob.width > max_w:
                mob.scale_to_fit_width(max_w)
            return mob

        ctx1 = fit(Text(
            "const hasContent = item.content && item.content.trim();",
            color=cream, font_size=16, font=MONO
        ), 10.5)
        removed = fit(Text(
            "- if (!hasContent) return null;  // drop silently",
            color=PALETTE["crimson"], font_size=16, font=MONO
        ), 10.5)
        note = fit(Text(
            "// SEC / exchange filings often arrive title-only",
            color=PALETTE["gold"], font_size=15, font=MONO
        ), 10.5)

        code = VGroup(ctx1, removed, note).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(UP * 0.6)

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
            "REMOVED", color=PALETTE["sage"], font_size=16, font=MONO
        ).next_to(removed, RIGHT, buff=0.3)
        self.play(Write(removed_tag), run_time=0.6)
        self.wait(0.5)

        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.0)

        result = Text(
            "-> title-only items now pass through",
            color=PALETTE["sage"], font_size=18, font=MONO
        ).scale_to_fit_width(10.5).next_to(code, DOWN, buff=1.0)
        self.play(Write(result), run_time=0.8)
        self.play(Transform(highlight, box_around(result, PALETTE["sage"])), run_time=0.6)
        self.wait(8.4)


class B05_RecoveredFilings(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Recovered — title-only filings", color=PALETTE["ink"], font_size=24
        ).scale_to_fit_width(10.5).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.6)

        items = [
            "Cboe Clear U.S.",
            "MEMX LLC",
            "Nasdaq GEMX SRO notice",
            "US v. Edwards LifeSciences (DOJ antitrust)",
        ]
        y = 1.5
        for it in items:
            check = Text("check:", color=PALETTE["sage"], font_size=20, font=MONO)
            label = Text(it, color=PALETTE["ink"], font_size=20)
            row = VGroup(check, label).arrange(RIGHT, buff=0.3)
            if row.width > 10.0:
                row.scale_to_fit_width(10.0)
            row.move_to([0, y, 0])
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.6)
            y -= 0.8

        self.wait(3.8)


class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        line1 = Text(
            "Silent filters don't fail loudly.", color=PALETTE["ink"], font_size=30
        ).scale_to_fit_width(10.5)
        line2 = Text(
            "They fail invisibly.", color=PALETTE["crimson"], font_size=34
        ).scale_to_fit_width(9.0)
        VGroup(line1, line2).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.4)
        self.play(Write(line2), run_time=1.0)
        self.wait(5.0)


class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=66)
        accent = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=4)
        tagline = Text("Fixed with Claude Code", color=PALETTE["ink"], font_size=40)
        VGroup(handle, accent, tagline).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)

        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.play(Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.5)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.12, tagline.get_corner(DR) + DOWN * 0.12
        )
        self.play(Create(tagline_underline), run_time=0.3)
        self.wait(2.7)


class B03_PipelineDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Project 29 — Regulatory Intelligence Pipeline",
            color=PALETTE["ink"], font_size=24
        ).scale_to_fit_width(11.5).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.6)
        self.wait(0.5)

        feeds = ["SEC", "FINRA", "CFTC", "FedReg (Sec.)", "FedReg (CFTC)"]
        stages = ["Normalize", "Score", "Postgres", "Email"]

        feed_boxes = VGroup(*[
            RoundedRectangle(
                width=2.0, height=0.5, corner_radius=0.07,
                fill_color=PALETTE["slate"], fill_opacity=0.05,
                stroke_color=PALETTE["slate"], stroke_width=1.5
            )
            for _ in feeds
        ]).arrange(DOWN, buff=0.2).to_edge(LEFT, buff=0.7).shift(UP * 0.1)

        feed_labels = VGroup(*[
            Text(name, color=PALETTE["ink"], font_size=14).move_to(box)
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
                width=1.9, height=0.65, corner_radius=0.07,
                fill_color=PALETTE["teal"], fill_opacity=0.06,
                stroke_color=PALETTE["teal"], stroke_width=1.6
            )
            for _ in stages
        ]).arrange(RIGHT, buff=0.25).to_edge(RIGHT, buff=0.9).shift(DOWN * 0.2)

        stage_labels = VGroup(*[
            Text(name, color=PALETTE["ink"], font_size=15).move_to(box)
            for name, box in zip(stages, stage_boxes)
        ])

        merge_point = Dot(feed_boxes.get_right() + RIGHT * 0.5, color=PALETTE["ink"], radius=0.03)
        feed_arrows = VGroup(*[
            Arrow(box.get_right(), merge_point.get_center(), buff=0.05,
                  color=PALETTE["ink"], stroke_width=1.5, max_tip_length_to_length_ratio=0.08)
            for box in feed_boxes
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in feed_arrows], lag_ratio=0.1), run_time=0.9)

        stage_arrows = VGroup()
        for i in range(len(stage_boxes) - 1):
            stage_arrows.add(
                Arrow(stage_boxes[i].get_right(), stage_boxes[i + 1].get_left(),
                      buff=0.06, color=PALETTE["ink"], stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.15)
            )
        entry_arrow = Arrow(merge_point.get_center(), stage_boxes[0].get_left(),
                             buff=0.06, color=PALETTE["ink"], stroke_width=1.5,
                             max_tip_length_to_length_ratio=0.1)

        self.play(GrowArrow(entry_arrow), run_time=0.4)
        for i, (box, label) in enumerate(zip(stage_boxes, stage_labels)):
            self.play(Create(box), Write(label), run_time=0.6)
            if i < len(stage_arrows):
                self.play(GrowArrow(stage_arrows[i]), run_time=0.35)
        self.wait(0.5)

        filter_note = Text(
            "checks: does this item\nhave a description?",
            color=PALETTE["crimson"], font_size=15, line_spacing=0.9
        ).next_to(stage_boxes[0], DOWN, buff=0.55)
        filter_arrow = Arrow(
            filter_note.get_top(), stage_boxes[0].get_bottom(),
            buff=0.1, color=PALETTE["crimson"], stroke_width=2,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(Write(filter_note), GrowArrow(filter_arrow), run_time=0.9)
        self.wait(10.0)


class B06_BeforeAfterCount(Scene):
    """Uses Text (Pango) instead of Integer/DecimalNumber for the animated
    count — Integer renders digits via LaTeX, which this machine doesn't have
    installed (Manim equation beats are the one blocked toolkit feature)."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Live feed run — items passed the filter",
            color=PALETTE["ink"], font_size=24
        ).scale_to_fit_width(11.5).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.6)

        before_pos = LEFT * 2.8 + UP * 0.4
        after_pos = RIGHT * 2.8 + UP * 0.4

        before_label = Text("BEFORE", color=PALETTE["ink"], font_size=18).move_to(before_pos + UP * 1.1)
        after_label = Text("AFTER", color=PALETTE["ink"], font_size=18).move_to(after_pos + UP * 1.1)

        before_num = Text("297", color=PALETTE["crimson"], font_size=80).move_to(before_pos)

        after_tracker = ValueTracker(297)
        after_num = always_redraw(lambda: Text(
            str(int(round(after_tracker.get_value()))),
            color=PALETTE["teal"], font_size=80
        ).move_to(after_pos))

        self.play(FadeIn(before_label), FadeIn(before_num), run_time=0.5)
        self.play(FadeIn(after_label), FadeIn(after_num), run_time=0.5)
        self.wait(0.3)

        self.play(after_tracker.animate.set_value(370), run_time=1.4, rate_func=smooth)

        delta = Text("+73 recovered", color=PALETTE["sage"], font_size=26).move_to(DOWN * 1.3)
        self.play(Write(delta), run_time=0.6)

        caveat = Text(
            "title-only filings the empty-description filter had dropped",
            color=PALETTE["ink"], font_size=15
        ).scale_to_fit_width(9.5).next_to(delta, DOWN, buff=0.35)
        self.play(FadeIn(caveat), run_time=0.5)
        self.wait(1.5)
