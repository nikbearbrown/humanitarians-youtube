"""
Manim scenes — 9:16 PORTRAIT SHORT derived from
2026-09-07-embeddings-how-ai-tells-similar-from-different

Built via THE SHORTS LAW (runtime/scripts/shorts.py): this reel (143.8s) is
UNDER the 180s Shorts cap, so the short is a FULL REFORMAT — all 9 parent
beats kept, no narration rewritten, every mp3 reused byte-for-byte from the
parent's mp3/ folder (see short/beat_sheet.json). Every beat in the parent is
a Manim GRAPHIC beat, so THE REFORMAT RULE's auto center-cut never applies
(generated graphics are never cropped) — each beat below is a genuine
portrait RE-LAYOUT of the parent ../scenes.py composition, hand-authored for
a 1080x1920 canvas, not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the vertical safe/hard bounds the parent file already designed against
carry over almost unchanged (hard y +/-4.0, safe y +/-3.4). What changes is
frame_width: 4.5 instead of 14.222 (hard x +/-2.25, safe x +/-1.95) — roughly
a 3.2x narrower stage. See the CRITICAL PORTRAIT FIX guard below.

Beat-by-beat redesign notes:
  B00 TitleCard          — title re-wrapped 3->5 narrow lines.
  B01 ExecSummary        — badge stacked ABOVE name (was beside it); summary
                           re-wrapped 3->6 short lines.
  B02 KeywordMissHook    — rule box and document card, side by side in the
                           parent, now stack TOP (rule) / BOTTOM (document) —
                           a single vertical column, no divider needed since
                           the parent never had a divider line either.
  B03 ThreeQuestionsFramework — each row's badge sits ABOVE its (now
                           full-width, more-wrapped) explanation instead of
                           beside a width-starved one.
  B04 MeaningSpaceDiagram — THE meaning-space diagram, redesigned as a
                           TALL/NARROW vertical scatter (was wide/short):
                           the cluster near the top of a portrait panel, the
                           unrelated far term near the bottom — using the
                           portrait frame's abundant HEIGHT instead of the
                           width it no longer has.
  B05 ExactnessFalsifiability — same tall vertical panel style as B04, with
                           Section 4.12/4.13 stacked near the panel's upper
                           half and the warning badge below.
  B06 AuditChecklist      — same checkbox+text row shape as the parent
                           (already narrow-friendly); text re-wrapped
                           narrower, decision line stacked into 3 short lines.
  B07 Statement           — 2 lines -> 4 shorter lines.
  B08 BrandOutro          — unchanged composition, narrower widths.

Palette/MONO/fit()/panel() copied from the parent ../scenes.py (including the
teal_on_ink fix for text sitting on an ink panel/background) for visual
continuity. See ../scenes.py and ../BUILD-LOG.md for full production history.
"""

from manim import *

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup — BEFORE
# the -r/--resolution CLI flag is applied. So a bare `manim -r 2160,3840` (as
# run.sh invokes) leaves frame_width at the 16:9 default even on a portrait
# render, making every coordinate in this file ~3.2x too small. This module-
# level guard (copied from the sibling reel's own short/scenes.py fix) runs
# at import time, AFTER manim's CLI arg-parsing has already set the real
# portrait pixel dimensions.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool — only legible on "bg" (cream)
    "teal_on_ink": "#5FB8CC",  # same hue, lightened for ink backgrounds/panels
    "crimson": "#E4572E", # bad / CVD-safe warm
    "slate":  "#29335C",  # structure — on the CREAM bg only (10.3:1 there)
    "slate_on_ink": "#9AA3D6",  # 2026-09-11 fix: plain "slate" measured only 1.16:1 on
                          # "ink" (near-invisible) — this tint hits 5.80:1. Use this,
                          # never plain "slate", on an ink background or panel.
    "gold":   "#F3A712",  # fill/stroke accent only — never text color
    "sage":   "#A8C686",  # human / growth / code-on-dark
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


def box_around(mob, buff=0.14, color=None, stroke_width=3):
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color or PALETTE["gold"], stroke_width=stroke_width, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


# --------------------------------------------------------------------------- #
# Tall/narrow "meaning space" panel for B04/B05 — the portrait redesign of
# the parent's wide/short panel. Portrait has abundant HEIGHT and little
# WIDTH, so the cluster is spread mostly vertically instead of horizontally.
#
# GATE V fix (2026-09-07 patch): direct visual inspection of a real rendered
# frame (not just the GATE V number, which already passed on raw bbox
# coverage since the whole panel is ink-colored) confirmed the exact defect
# described in the fix brief — the cluster sat in the panel's top quarter
# with a totally empty band across the panel's middle-to-bottom half before
# the far point appeared. Panel height enlarged 5.0->5.6, and a new
# distance_connector() below fills that middle band with a real, meaningful
# element (a dashed "distance in meaning space" line + label) instead of
# just moving points around and leaving the void.
# --------------------------------------------------------------------------- #
# 2026-09-11 fix: PANEL_H trimmed 5.0->4.5 — same reason as the 16:9 sibling's
# identical fix (see that file's PANEL_H comment): not enough gap below the panel to
# give warn_label a real frame-edge safe margin without overlapping the panel border.
# No point coordinate is re-scaled here (unlike 16:9's PANEL_SCALE_Y) since this
# file's plot points use absolute coordinates that already sit safely inside a
# smaller panel (checked: lowest point, p_far at y=-1.9+anchor, stays >=0.3 inside
# the new smaller bottom edge).
PANEL_W, PANEL_H = 3.5, 4.5


def meaning_space_frame(stroke=None):
    """Built centered at ORIGIN — same fixed-anchor discipline as the parent
    (never next_to a title). stroke: border color override — B05 (ink
    background) passes teal_on_ink for the same real-measured low-contrast
    fix as the 16:9 master's B05 (plain slate-on-ink border pixels average
    too close to the ink background's own luminance)."""
    return VGroup(panel(PANEL_W, PANEL_H, fill=PALETTE["ink"], stroke=stroke or PALETTE["slate"], opacity=1.0))


def plot_point(pos, label_text, color, label_dir=DOWN, font_size=16):
    dot = Dot(point=[pos[0], pos[1], 0], radius=0.11, color=color, fill_opacity=1.0)
    label = fit(Text(label_text, color=color, font_size=font_size, font=MONO), 2.9)
    label.next_to(dot, label_dir, buff=0.14)
    return VGroup(dot, label)


def grouping_ellipse(center, color, w=1.8, h=2.2):
    ell = Ellipse(width=w, height=h, color=color, stroke_width=3, fill_opacity=0.06,
                   fill_color=color)
    ell.move_to([center[0], center[1], 0])
    return DashedVMobject(ell, num_dashes=24)


def distance_connector(top_y, bottom_y, color, label_text):
    """Fills the tall panel's otherwise-empty middle band with a real
    element: a dashed vertical line running from just below the cluster to
    just above the far/distinct point, with a small label at its midpoint —
    "the same space, just far apart in it", not blank padding. The label
    sits directly on the line by design (same deliberate-annotation escape
    hatch as the cluster ellipse elsewhere in this file), so the caller
    marks the returned line `_qc_intentional`."""
    line = DashedLine([0, top_y, 0], [0, bottom_y, 0], color=color, stroke_width=2, dash_length=0.12)
    # GATE V/B fix (2026-09-07 patch): a half-width-based shift (this
    # function's first draft) pushed the label's right edge to x≈2.1-2.8 on
    # a portrait canvas whose safe half-width is only ~1.95-2.0 — a real
    # measured off-safe-area + label-on-curve (crossing the panel's own
    # border on its way out) defect, not just a numeric nit. Capped the fit
    # width narrower (1.5, was 2.7) and shifted by a small FIXED amount
    # (0.22, not proportional to the label's own width) so the label's
    # right edge never leaves the panel regardless of text length.
    label = fit(Text(label_text, color=color, font_size=13, font=MONO), 1.5)
    label.move_to([0, (top_y + bottom_y) / 2, 0])
    label.shift(RIGHT * 0.22)
    return VGroup(line, label)


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Title re-wrapped 3->5 narrow lines.
# Fixed silent-beat duration (4.05s).
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~53% safe-area coverage (real GATE V number) — sized up
        # (30/22 -> 36/26 fonts, rule width 1.5->1.9) and buff widened
        # 0.7->1.15 — portrait has abundant safe HEIGHT (7.2 units) to spend
        # on spacing, same lesson as the 16:9 master's own B00 fix.
        title_lines = [
            "Embeddings:",
            "How AI Tells",
            "Similar From",
            "Different",
            "(When Keyword",
            "Matching Can't)",
        ]
        title = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=36, weight="BOLD"), MAX_W)
            for l in title_lines[:4]
        ] + [fit(Text(l, color=PALETTE["slate"], font_size=26), MAX_W) for l in title_lines[4:]]
        ).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=28), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.02
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.7)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        self.wait(2.55)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name (was beside it in the
# parent); summary re-wrapped 3->6 short lines. Timing unchanged (12.34s).
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~61% at best (and much lower during animate-in) — sized up
        # across the board and buff widened 0.45->0.65, same lesson as the
        # 16:9 master's own B01 fix (a card with few elements needs its OWN
        # spacing/size to clear the canvas-fill floor).
        top_rule = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.5, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = Text("SPJ", color=PALETTE["teal"], font_size=28, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(Text("Sai Pranavi Jeedigunta", color=PALETTE["ink"], font_size=28, weight="BOLD"), MAX_W)
        role = fit(Text("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=21), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.18)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.3)

        summary_lines = [
            "This video: why keyword-",
            "matching rules quietly",
            "break over time —",
            "and what embeddings",
            "actually do",
            "differently.",
        ]
        summary = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=26), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.17)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(
            DOWN, buff=0.65
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(10.54)


# --------------------------------------------------------------------------- #
# B02 — HOOK: rule box (top) / document card (bottom) — a vertical stack
# instead of the parent's side-by-side layout. No divider needed (the parent
# never had one either — its two panels were just spaced apart). Timing
# unchanged (18.53s).
# --------------------------------------------------------------------------- #
class B02_KeywordMissHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~52% (real GATE V number) and dipped to ~25% for a multi-
        # second window before the doc card landed — same late-arriving-
        # anchor bug as the 16:9 master's own B02 fix. A floor rule now
        # draws with the header at t=0 (present the whole beat); "closing"
        # lands above it later. Cards enlarged too.
        header = fit(Text("document tagging rule", color=PALETTE["sage"], font_size=18, font=MONO), MAX_W)
        header.to_edge(UP, buff=0.65)
        floor_rule = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["slate"], stroke_width=2)
        floor_rule.to_edge(DOWN, buff=0.9)

        def doc_card(title_text, w=2.9, h=2.05):
            body = RoundedRectangle(width=w, height=h, corner_radius=0.08,
                                     fill_color=PALETTE["bg"], fill_opacity=1.0,
                                     stroke_color=PALETTE["slate"], stroke_width=2)
            fold = Polygon(
                [w / 2 - 0.4, h / 2, 0], [w / 2, h / 2, 0], [w / 2, h / 2 - 0.4, 0],
                fill_color=PALETTE["slate"], fill_opacity=0.3, stroke_width=0,
            )
            title = fit(Text(title_text, color=PALETTE["ink"], font_size=18, weight="BOLD"), w - 0.4)
            title.move_to([0, h / 2 - 0.42, 0])
            lines = VGroup(*[
                Line([-w / 2 + 0.28, y, 0], [w / 2 - 0.28, y, 0],
                     color=PALETTE["slate"], stroke_width=1.2, stroke_opacity=0.5)
                for y in (h / 2 - 0.88, h / 2 - 1.2, h / 2 - 1.52)
            ])
            return VGroup(body, fold, title, lines)

        def rule_box(w=3.3, h=1.75):
            box = panel(w, h, fill=PALETTE["slate"], stroke=PALETTE["gold"], opacity=0.35)
            rule_hdr = Text("RULE", color=PALETTE["gold"], font_size=19, font=MONO, weight="BOLD")
            rule_hdr.move_to([0, h / 2 - 0.34, 0])
            phrase = fit(Text('contains exact phrase:', color=PALETTE["sage"], font_size=15, font=MONO), w - 0.3)
            phrase.move_to([0, 0.05, 0])
            phrase2 = fit(Text('"investment adviser"?', color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD"), w - 0.3)
            phrase2.next_to(phrase, DOWN, buff=0.14)
            return VGroup(box, rule_hdr, phrase, phrase2)

        rule = rule_box()
        rule.next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(header, shift=UP * 0.1), Create(floor_rule), run_time=0.4)
        self.play(Create(rule[0]), FadeIn(rule[1:]), run_time=0.6)

        # CASE 1 — the rule works.
        doc1 = doc_card("Investment Adviser\nDisclosure")
        doc1.next_to(rule, DOWN, buff=0.45)
        self.play(FadeIn(doc1, shift=UP * 0.15), run_time=0.5)

        check1 = Text("✓ FLAGGED", color=PALETTE["teal_on_ink"], font_size=20, font=MONO, weight="BOLD")
        check1.next_to(doc1, DOWN, buff=0.22)
        self.play(FadeIn(check1, scale=1.2), run_time=0.4)
        self.wait(1.5)

        # CASE 2 — swap in the doc titled with the industry's own acronym.
        self.play(FadeOut(doc1, shift=LEFT * 0.3), FadeOut(check1), run_time=0.3)

        doc2 = doc_card("RIA\nAnnual Update")
        doc2.next_to(rule, DOWN, buff=0.45)
        self.play(FadeIn(doc2, shift=UP * 0.15), run_time=0.8)
        self.wait(1.0)

        scan_box = box_around(rule[3], color=PALETTE["gold"], stroke_width=2)
        self.play(Create(scan_box), run_time=0.5)
        self.wait(1.2)

        miss = Text("✗ NOT FLAGGED", color=PALETTE["crimson"], font_size=21, font=MONO, weight="BOLD")
        miss.next_to(doc2, DOWN, buff=0.22)
        self.play(FadeIn(miss, scale=1.2), run_time=0.5)
        self.wait(3.0)

        closing = VGroup(
            fit(Text("nothing crashed —", color=PALETTE["sage"], font_size=18), MAX_W),
            fit(Text("it just quietly stopped working", color=PALETTE["sage"], font_size=18), MAX_W),
        ).arrange(DOWN, buff=0.12)
        closing.next_to(floor_rule, UP, buff=0.25)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.6)
        self.wait(6.23)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: each row's badge sits ABOVE its (now full-width)
# explanation instead of beside a width-starved one. Timing unchanged
# (24.07s).
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # a flat ~54% (real GATE V number) for most of the beat's runtime —
        # rows sized up, height cap widened 4.8->5.7, and a bottom-anchored
        # closer line added (same fix as the 16:9 master's own B03), plus
        # the intro hold shortened 1.3->0.6 to trim the sparsest opening
        # moment.
        title = VGroup(
            fit(Text("Three Questions,", color=PALETTE["ink"], font_size=32), MAX_W),
            fit(Text("Before Any Example", color=PALETTE["ink"], font_size=32), MAX_W),
        ).arrange(DOWN, buff=0.12)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)

        intro = fit(Text("Ask all three, in order:", color=PALETTE["slate"], font_size=22), MAX_W)
        intro.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(intro, shift=UP * 0.1), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(intro, shift=UP * 0.1), run_time=0.3)

        rows_data = [
            ("1", "WORDING VARIES", "Does the wording actually\nvary in the real world —\nor is there only one way\nto say this?"),
            ("2", "CONTEXT FLIPS\nMEANING", "Does context change what a\nphrase means, so a fixed\nkeyword could be right in\none place, wrong in another?"),
            ("3", "EXACTNESS IS\nTHE POINT", "Is exactness itself the\npoint — like matching an\nID or code — where a\nclose match is wrong?"),
        ]

        rows = VGroup()
        for num, label, desc in rows_data:
            badge = Circle(radius=0.34, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                            fill_opacity=0.15, stroke_width=2.3)
            badge_num = Text(num, color=PALETTE["teal"], font_size=23, font=MONO).move_to(badge.get_center())
            label_txt = fit(Text(label, color=PALETTE["slate"], font_size=19, font=MONO, weight="BOLD", line_spacing=0.9), MAX_W)
            header_row = VGroup(badge, badge_num, label_txt).arrange(RIGHT, buff=0.22)
            desc_txt = fit(Text(desc, color=PALETTE["ink"], font_size=17, line_spacing=1.05), MAX_W)
            row = VGroup(header_row, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        if rows.width > MAX_W:
            rows.scale_to_fit_width(MAX_W)
        if rows.height > 5.2:
            rows.scale_to_fit_height(5.2)
        rows.move_to(ORIGIN).shift(DOWN * 0.35)

        for r in rows:
            self.play(FadeIn(r[0], shift=UP * 0.1), run_time=0.15)

        row_holds = [5.29, 6.46, 6.46]
        for row, hold in zip(rows, row_holds):
            desc_txt = row[1]
            self.play(FadeIn(desc_txt, shift=UP * 0.08), run_time=0.3)
            self.wait(hold)

        closer = fit(Text("all three, every time.", color=PALETTE["crimson"], font_size=20), MAX_W)
        closer.to_edge(DOWN, buff=0.95)
        self.play(FadeIn(closer, shift=UP * 0.1), run_time=0.3)
        self.wait(2.41)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: THE meaning-space diagram, redesigned as a TALL/
# NARROW vertical scatter — the cluster near the top of a portrait panel,
# the unrelated far term near the bottom. Uses the abundant portrait HEIGHT
# instead of the width the parent spent on a wide layout. Timing unchanged
# (25.9s).
# --------------------------------------------------------------------------- #
class B04_MeaningSpaceDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(Text("Meaning Space", color=PALETTE["ink"], font_size=28), MAX_W)
        title.move_to([0, 3.1, 0])

        frame = meaning_space_frame()
        frame.move_to([0, -0.2, 0])
        anchor = frame.get_center()

        self.play(Write(title), run_time=0.4)
        self.play(FadeIn(frame), run_time=0.5)
        self.wait(2.6)

        # cluster near the TOP of the tall panel — vertical spread, not
        # horizontal (portrait's abundant height, not width)
        p_ria = plot_point([-0.5, 1.9], "RIA", PALETTE["teal_on_ink"], label_dir=LEFT)
        p_ia = plot_point([0.3, 1.5], "investment\nadviser", PALETTE["teal_on_ink"], label_dir=RIGHT, font_size=14)
        p_adv = plot_point([-0.3, 1.0], "advisor", PALETTE["teal_on_ink"], label_dir=LEFT)
        for p in (p_ria, p_ia, p_adv):
            p.shift(anchor)

        self.play(FadeIn(p_ria), run_time=0.3)
        self.play(FadeIn(p_ia), run_time=0.3)
        self.play(FadeIn(p_adv), run_time=0.3)

        # GATE V fix (2026-09-10 patch): the connector + far point used to
        # be created only after ellipse/close_tag/checkmark, ~85% of the way
        # through this 25.9s beat — confirmed by direct frame extraction at
        # 68s into the 9:16 short that the bottom two-thirds of the tall
        # panel was still empty at that point. Moved here, right after the
        # 3-point cluster fades in (same reordering pattern already applied
        # to the parent ../scenes.py B04), with NO run_time/wait value
        # changed anywhere in this scene — just reordered — so the connector
        # + far point are now visible for ~83% of the beat instead of ~15%.
        # The connector's own y-coordinates are untouched: its top_y (0.4)
        # already sits below the lowest cluster point (p_adv at y=1.0, a
        # 0.6-unit gap) independent of whether the ellipse has been drawn
        # yet, so no coordinate change was needed to move it earlier.
        connector = distance_connector(
            0.4 + anchor[1], -1.3 + anchor[1], PALETTE["slate_on_ink"], "far apart in meaning",
        )
        connector[0]._qc_intentional = True
        self.play(Create(connector), run_time=0.5)

        # the unrelated far term — near the BOTTOM of the tall panel
        p_far = plot_point([0.0, -1.9], "quarterly\nearnings", PALETTE["slate_on_ink"], label_dir=UP, font_size=14)
        p_far.shift(anchor)
        self.play(FadeIn(p_far), run_time=0.4)
        self.wait(4.1)

        ellipse = grouping_ellipse([0.0, 1.45], PALETTE["teal_on_ink"], w=2.1, h=1.5)
        ellipse.shift(anchor)
        ellipse._qc_intentional = True
        close_tag = fit(Text("close together", color=PALETTE["teal_on_ink"], font_size=15, font=MONO), 2.6)
        close_tag.next_to(ellipse, DOWN, buff=0.1)

        self.play(Create(ellipse), run_time=0.6)
        self.play(FadeIn(close_tag), run_time=0.5)
        self.wait(6.9)

        checkmark = fit(Text("✓ same real-world thing", color=PALETTE["teal_on_ink"], font_size=15, font=MONO, weight="BOLD"), MAX_W)
        checkmark.next_to(title, DOWN, buff=0.15)
        pulse_box = box_around(VGroup(p_ria, p_ia, p_adv), color=PALETTE["teal_on_ink"], stroke_width=2, buff=0.35)
        pulse_box._qc_intentional = True
        self.play(FadeIn(checkmark, scale=1.1), Create(pulse_box), run_time=0.8)
        self.wait(4.7)

        caption = VGroup(
            fit(Text("catches every synonym —", color=PALETTE["ink"], font_size=15), MAX_W),
            fit(Text("even ones nobody listed", color=PALETTE["ink"], font_size=15), MAX_W),
        ).arrange(DOWN, buff=0.08)
        caption.next_to(frame, DOWN, buff=0.1)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        self.wait(2.6)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: same tall vertical panel style as B04, "Section
# 4.12"/"Section 4.13" (fictional placeholders) stacked near the panel's
# upper half, warning badge below. Timing unchanged (26.83s).
# --------------------------------------------------------------------------- #
class B05_ExactnessFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # GATE V fix (2026-09-07 patch): same panel enlargement + empty-
        # middle-band fix as B04 above (see that class's comment), plus the
        # real-measured low-contrast dilution fix (border stroke ->
        # teal_on_ink, dimmed far-point opacity 0.5->0.65) carried over from
        # the 16:9 master's own B05 patch.
        title = VGroup(
            fit(Text("Meaning Space —", color=PALETTE["bg"], font_size=24), MAX_W),
            fit(Text("the Exactness Case", color=PALETTE["bg"], font_size=24), MAX_W),
        ).arrange(DOWN, buff=0.08)
        title.move_to([0, 3.02, 0])

        frame = meaning_space_frame(stroke=PALETTE["teal_on_ink"])
        frame.move_to([0, -0.2, 0])
        anchor = frame.get_center()

        p_far = plot_point([0.0, -1.9], "quarterly\nearnings", PALETTE["slate_on_ink"], label_dir=UP, font_size=14)
        p_far.shift(anchor)
        # 2026-09-11 fix: see scenes.py's identical note — slate_on_ink at 0.85 keeps
        # ~4.6:1 contrast instead of plain slate's broken 1.16:1 further dimmed to 0.65.
        p_far.set_opacity(0.85)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(frame), FadeIn(p_far), run_time=0.4)
        self.wait(2.6)

        p_412 = plot_point([-0.4, 2.0], "Section 4.12", PALETTE["gold"], label_dir=LEFT, font_size=14)
        p_412.shift(anchor)
        self.play(FadeIn(p_412), run_time=0.4)
        self.wait(6.6)

        p_413 = plot_point([0.3, 1.4], "Section 4.13", PALETTE["gold"], label_dir=RIGHT, font_size=14)
        p_413.shift(anchor)
        ellipse = grouping_ellipse([0.0, 1.7], PALETTE["gold"], w=1.7, h=1.6)
        ellipse.shift(anchor)
        ellipse._qc_intentional = True
        self.play(FadeIn(p_413), run_time=0.4)
        self.play(Create(ellipse), run_time=0.6)

        # GATE V fix (2026-09-10 patch): this connector used to be created
        # after the wait(6.0) below, i.e. ~67% of the way through this
        # 26.83s beat — direct frame extraction confirmed the panel's middle
        # band (between the already-dimmed far point and the cluster) sat
        # empty for most of the beat despite the connector element existing
        # in the file. Moved up to right after the cluster (412 + 413 +
        # ellipse) finishes forming — the earliest point at which both
        # things it visually bridges are actually on screen — so it's now
        # visible from ~43% through instead of ~67%. No run_time/wait value
        # changed, only reordered; the connector's own y-coordinates (0.6 to
        # -1.3) were already computed to sit below the cluster and above the
        # far point regardless of draw order, so no coordinate change was
        # needed.
        connector = distance_connector(
            0.6 + anchor[1], -1.3 + anchor[1], PALETTE["gold"], "different sections",
        )
        connector[0]._qc_intentional = True
        self.play(Create(connector), run_time=0.5)
        self.wait(6.0)

        warn_tri = Triangle(color=PALETTE["crimson"], fill_color=PALETTE["crimson"],
                             fill_opacity=0.2, stroke_width=3)
        warn_tri.scale(0.26)
        warn_bang = Text("!", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD")
        warn_bang.move_to(warn_tri.get_center() + DOWN * 0.02)
        warn_badge = VGroup(warn_tri, warn_bang)
        warn_badge.next_to(title, DOWN, buff=0.15)
        warn_label = VGroup(
            fit(Text("different rules —", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD"), MAX_W),
            fit(Text("different requirements", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD"), MAX_W),
        ).arrange(DOWN, buff=0.06)
        warn_label.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(warn_badge, scale=1.2), run_time=0.6)
        self.wait(2.4)

        exact_line = fit(Text("exactness is the point here", color=PALETTE["bg"], font_size=17), MAX_W)
        exact_line.next_to(warn_label, UP, buff=0.4)
        self.play(Write(exact_line), run_time=0.5)
        self.wait(2.0)

        self.play(FadeIn(warn_label, shift=UP * 0.1), run_time=0.5)
        self.wait(2.83)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: same checkbox+text row shape as the parent (already
# narrow-friendly); text re-wrapped narrower, decision line stacked into 3
# short lines. Timing unchanged (21.22s).
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~52% (real GATE V number) and held there for most of the
        # beat because the decision block (the only element reaching the
        # safe-area floor) didn't land until the very end — same
        # late-arriving-anchor bug as the 16:9 master's own B06 fix. A floor
        # rule now draws with the title (present the whole beat); the
        # decision TEXT still lands late, above it.
        title = fit(Text("Audit One Rule Today", color=PALETTE["ink"], font_size=30), MAX_W)
        title.to_edge(UP, buff=0.65)
        floor_rule = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["gold"], stroke_width=2.5)
        floor_rule.to_edge(DOWN, buff=0.85)
        self.play(Write(title), Create(floor_rule), run_time=0.3)
        self.wait(1.0)

        steps_data = [
            ("Does the wording\nactually vary?", "not just one way to say it"),
            ("Does context flip\nthe meaning?", "right here, wrong elsewhere"),
            ("Is exactness the\nwhole point?", "a close match would be wrong"),
        ]

        rows = VGroup()
        for main, explain in steps_data:
            box = Square(side_length=0.36, color=PALETTE["slate"], stroke_width=2.4)
            main_txt = fit(Text(main, color=PALETTE["ink"], font_size=22, font=MONO, line_spacing=0.9), MAX_W - 0.5)
            explain_txt = fit(Text(explain, color=PALETTE["slate"], font_size=17), MAX_W - 0.5)
            text_col = VGroup(main_txt, explain_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            row = VGroup(box, text_col).arrange(RIGHT, buff=0.3, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        if rows.width > MAX_W:
            rows.scale_to_fit_width(MAX_W)
        if rows.height > 5.4:
            rows.scale_to_fit_height(5.4)
        rows.move_to(ORIGIN).shift(UP * 0.15)

        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.1), run_time=0.2)

        row_holds = [1.7, 1.7, 1.7]
        for row, hold in zip(rows, row_holds):
            explain_txt = row[1][1]
            self.play(FadeIn(explain_txt, shift=UP * 0.06), run_time=0.3)
            self.wait(hold)

        decision = VGroup(
            fit(Text("2 YES + 1 NO", color=PALETTE["teal"], font_size=23, font=MONO, weight="BOLD"), MAX_W),
            fit(Text("-> move that rule to", color=PALETTE["ink"], font_size=18), MAX_W),
            fit(Text("similarity matching", color=PALETTE["ink"], font_size=18), MAX_W),
        ).arrange(DOWN, buff=0.14)
        decision.next_to(floor_rule, UP, buff=0.2)
        self.play(FadeIn(decision, shift=UP * 0.1), run_time=0.5)
        self.wait(12.82)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: 2 lines -> 4 shorter lines. Timing unchanged (9.41s).
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~36% (real GATE V number) — sized up and given a bordered card
        # (top/bottom rules anchored to the SAFE FRAME itself, not the text,
        # same lesson as the 16:9 master's own B07 fix) so the card reaches
        # the safe-area top/bottom regardless of the text block's height.
        statement = VGroup(
            fit(Text("A keyword list only knows", color=PALETTE["ink"], font_size=27), MAX_W),
            fit(Text("the words you thought of.", color=PALETTE["ink"], font_size=27), MAX_W),
            fit(Text("Embeddings measure the", color=PALETTE["ink"], font_size=25), MAX_W),
            fit(Text("meaning you didn't have", color=PALETTE["ink"], font_size=25), MAX_W),
            fit(Text("to spell out —", color=PALETTE["ink"], font_size=25), MAX_W),
        ).arrange(DOWN, buff=0.22)

        gap_line = VGroup(
            fit(Text("but only where closeness", color=PALETTE["ink"], font_size=23), MAX_W),
            fit(Text("is actually what you want.", color=PALETTE["ink"], font_size=23), MAX_W),
        ).arrange(DOWN, buff=0.12)

        content = VGroup(statement, gap_line).arrange(DOWN, buff=0.75)
        content.move_to(ORIGIN)

        top_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=3)
        top_rule.to_edge(UP, buff=0.6)
        bottom_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.to_edge(DOWN, buff=0.9)

        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(statement), run_time=0.5)
        self.wait(0.2)

        highlight = Rectangle(
            width=gap_line.width + 0.3, height=gap_line.height + 0.2,
            fill_color=PALETTE["gold"], fill_opacity=0.15, stroke_width=0,
        ).move_to(gap_line.get_center())
        self.play(FadeIn(highlight), FadeIn(gap_line), Create(bottom_rule), run_time=0.5)
        self.wait(7.91)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition, narrower widths. Timing unchanged
# (1.51s — a very short narration line).
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(Text("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)
        accent = Line(LEFT * 1.1, RIGHT * 1.1, color=PALETTE["gold"], stroke_width=3)
        tagline = VGroup(
            fit(Text("explained with Claude Code —", color=PALETTE["ink"], font_size=14), MAX_W),
            fit(Text("in for Sai Pranavi Jeedigunta", color=PALETTE["ink"], font_size=14), MAX_W),
        ).arrange(DOWN, buff=0.08)
        VGroup(handle, accent, tagline).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.08, tagline.get_corner(DR) + DOWN * 0.08
        )

        self.play(FadeIn(handle, shift=UP * 0.1), Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.3)
        self.play(Create(tagline_underline), run_time=0.2)
        self.wait(0.61)
