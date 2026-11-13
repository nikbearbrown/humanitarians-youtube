"""
Manim scenes for 2026-09-22-hallucination-why-sounding-sure-isnt-being-right
"Hallucination: Why Sounding Sure Isn't the Same as Being Right"

General AI/STEM topic explainer (not a report of the fellow's own engineering
work). Both the fabricated-citation worked example (B04) and the true-fact
falsifiability case (B05) are fully generic/hypothetical — no real model,
vendor, or actual paper named or resembled. See FACTCHECK.md and SOURCES.md.

B00_TitleCard                  — silent title card (TITLE)
B01_ExecSummary                 — spoken personal-intro card (EXEC-SUMMARY)
B02_SameToneHook                 — two identically-confident answers, then labeled (HOOK)
B03_ThreeQuestionsFramework       — the 3-question rubric, shown together (FRAMEWORK)
B04_FabricatedVsRealCitation      — fabricated vs real citation, same fluent tone (WORKED-EXAMPLE)
B05_TrueFactFalsifiability        — same tone, genuinely true case (FALSIFIABILITY)
B06_AuditChecklist                — the 3 questions restated as a task checklist (SCAFFOLDED-TASK)
B07_Statement                    — takeaway statement card (TAKEAWAY)
B08_BrandOutro                   — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest siblings (2026-09-29-the-keyword-that-cried-wolf/scenes.py,
2026-09-22-the-all-clear-that-wasnt-all-there/scenes.py) for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed, this reel has no math.

CRITICAL HOUSE-STYLE RULE: Manim's Text() has a real empirically-confirmed
Pango/Cairo rendering bug where creating Text() directly at font_size <= ~24
inserts phantom gaps inside words (e.g. "video" -> "v ideo"). Every piece of
on-screen text in this file goes through T() below, never Text() directly.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule:
B00=4.06 (silent, fixed target) B01=13.10 B02=12.50 B03=25.75 B04=25.58
B05=25.42 B06=23.16 B07=11.14 B08=1.51 (B08's narration, "Explained with
Claude Code.", is short by design — the approved beat sheet's exact text,
not rewritten here).

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (60-80% of the safe area).
"""

from manim import *
import numpy as np

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1) --
                          # use this, never "teal", for teal text/strokes on
                          # any ink-background scene or ink-filled panel.
    "crimson": "#E4572E", # bad / CVD-safe warm -- only safe as a STROKE/accent
                          # on ink (0.28 luminance sep as text, under the 0.3
                          # floor); use "gold" for bad/alert TEXT on ink.
    "slate":  "#29335C",  # structure -- 0.04 luminance sep on ink (broken);
                          # use "sage" for any note/tag text on ink.
    "gold":   "#F3A712",  # fill/stroke/accent; also safe as alert TEXT on ink.
    "sage":   "#A8C686",  # human / growth / confirmed; safe secondary text on ink.
}

MONO = "Courier New"


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See sibling reels' BUILD-LOG.md for the
    empirical proof."""
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.06s — fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Hallucination:", color=PALETTE["ink"], font_size=50, weight="BOLD"), 12.0)
        title_line2 = fit(T("Why Sounding Sure Isn't", color=PALETTE["ink"], font_size=38, weight="BOLD"), 12.0)
        title_line3 = fit(T("the Same as Being Right", color=PALETTE["ink"], font_size=38, weight="BOLD"), 12.0)
        title = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.28)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=36)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.06s silent track
        self.wait(2.46)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 13.10s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 3.4, RIGHT * 3.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 3.4, RIGHT * 3.4, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.55, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=30, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=42, weight="BOLD"), 9.0)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=22), 7.0)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_row = VGroup(badge_group, name_block).arrange(RIGHT, buff=0.4)

        summary_lines = [
            "This video: why a confident-sounding",
            "answer from an AI model isn't the",
            "same thing as a correct one — and",
            "three questions that catch the",
            "difference before you act on it.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=25), 11.0) for l in summary_lines
        ]).arrange(DOWN, buff=0.18)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 12.648s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 13.10s -> wait 11.0)
        self.wait(10.55)


# --------------------------------------------------------------------------- #
# B02 — HOOK: two answer bubbles, identical confident styling. Neither is
# labeled at first — the point is they are visually indistinguishable by
# tone alone. One is then labeled "REAL", the other "FABRICATED".
# [Source: FACTCHECK.md — generic/hypothetical scenario, no real model named]
# measured audio: 12.50s
# --------------------------------------------------------------------------- #
class B02_SameToneHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two answers. Same confident tone.", color=PALETTE["bg"], font_size=30), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # ---- LEFT bubble ----
        left_panel = panel(width=5.6, height=4.4, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        left_panel.move_to([-3.35, -0.45, 0])
        left_q = fit(T("“When did this happen?”", color=PALETTE["sage"], font_size=19), 4.9)
        left_a = fit(T(
            "“Yes — this is well established,\nand I'm confident in the answer.”",
            color=PALETTE["bg"], font_size=18, line_spacing=1.25,
        ), 4.9)
        left_tag = fit(T("?", color=PALETTE["gold"], font_size=34, font=MONO, weight="BOLD"), 4.0)
        left_content = VGroup(left_q, left_a, left_tag).arrange(DOWN, buff=0.4)
        left_content.move_to(left_panel.get_center())

        # ---- RIGHT bubble ----
        right_panel = panel(width=5.6, height=4.4, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        right_panel.move_to([3.35, -0.45, 0])
        right_q = fit(T("“When did this happen?”", color=PALETTE["sage"], font_size=19), 4.9)
        right_a = fit(T(
            "“Yes — this is well established,\nand I'm confident in the answer.”",
            color=PALETTE["bg"], font_size=18, line_spacing=1.25,
        ), 4.9)
        right_tag = fit(T("?", color=PALETTE["gold"], font_size=34, font=MONO, weight="BOLD"), 4.0)
        right_content = VGroup(right_q, right_a, right_tag).arrange(DOWN, buff=0.4)
        right_content.move_to(right_panel.get_center())

        self.play(Create(left_panel), Create(right_panel), run_time=0.5)
        self.play(FadeIn(left_content, shift=UP * 0.1), FadeIn(right_content, shift=UP * 0.1), run_time=0.5)
        # hold on the identical, unlabeled pair — this is the whole point:
        # nothing in how either answer sounds tells them apart.
        self.wait(4.5)

        # reveal: swap the "?" tag for REAL / FABRICATED labels.
        left_label = T("REAL", color=PALETTE["sage"], font_size=26, font=MONO, weight="BOLD")
        left_label.move_to(left_tag.get_center())
        right_label = T("FABRICATED", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD")
        right_label.move_to(right_tag.get_center())
        self.play(
            FadeOut(left_tag), FadeOut(right_tag),
            FadeIn(left_label), FadeIn(right_label),
            run_time=0.5,
        )
        self.wait(2.0)

        # a later, distinct shape-state change (not just the two panels
        # created up front) — real Rectangles drawn around each revealed
        # label once both are on screen, giving GATE A's static pre-flight a
        # genuine shape-state change partway through the beat.
        left_label_box = box_around(left_label, buff=0.12, color=PALETTE["sage"])
        right_label_box = box_around(right_label, buff=0.12, color=PALETTE["gold"])
        self.play(Create(left_label_box), Create(right_label_box), run_time=0.3)
        self.wait(0.7)

        zinger = fit(T("Nothing in the tone told you which was which.", color=PALETTE["gold"], font_size=26), 10.8)
        zinger.to_edge(DOWN, buff=0.68)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.5(title)+0.5+0.5+0.5+0.3+0.5 = 2.8s
        # waits above = 1.0+4.5+2.0+0.7 = 8.2s
        # remainder tuned to the measured 12.50s Kokoro length (12.50-2.8-8.2=1.5)
        self.wait(1.5)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: the 3-question rubric, shown together before any example.
# measured audio: 25.75s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three questions, before any example:", color=PALETTE["ink"], font_size=30), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def make_card(num, label, body, accent):
            num_badge = Circle(radius=0.34, color=accent, fill_opacity=0, stroke_width=2.5)
            num_txt = T(num, color=accent, font_size=24, font=MONO, weight="BOLD")
            num_txt.move_to(num_badge.get_center())
            num_group = VGroup(num_badge, num_txt)
            label_txt = fit(T(label, color=PALETTE["ink"], font_size=24, weight="BOLD"), 10.5)
            body_txt = fit(T(body, color=PALETTE["slate"], font_size=19), 10.5)
            row = VGroup(num_group, VGroup(label_txt, body_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.12)).arrange(RIGHT, buff=0.4)
            bg = panel(width=11.4, height=row.height + 0.55, fill=PALETTE["bg"], stroke=accent, corner_radius=0.14)
            row.move_to(bg.get_center())
            return VGroup(bg, row)

        q1 = make_card("1", "Checkable?", "Is there something specific here you could actually verify?", PALETTE["teal"])
        q2 = make_card("2", "Would it hedge?", "Asked to rate its own confidence, would it admit uncertainty?", PALETTE["teal"])
        q3 = make_card("3", "Confidence tracks difficulty?", "As sure about the hard, obscure part as the easy part?", PALETTE["crimson"])

        cards = VGroup(q1, q2, q3).arrange(DOWN, buff=0.35).move_to(ORIGIN).shift(DOWN * 0.15)

        # All 3 cards revealed TOGETHER, up front — per BEAT-SHEET.md's
        # Legibility Contract ("rubric card, all 3 questions shown together"),
        # not a sequential build. This also keeps real content mass on
        # screen for nearly the whole beat: GATE V's canvas-fill check
        # samples at 50%/85% of the beat, and an earlier sequential-reveal
        # draft left only 2 of 3 cards up at the 50% sample (51% fill, under
        # the 55% floor) — showing all 3 immediately fixes this with real
        # content, not an oversized invisible box.
        self.play(FadeIn(cards, shift=UP * 0.1), run_time=0.6)
        self.wait(1.0)

        # per-card emphasis pulses, timed to the narration's own pacing
        # (checkable ~5.5s, would-it-hedge ~6.5s, tracks-difficulty ~6.0s),
        # without ever removing the other cards from screen.
        self.play(Indicate(q1[0], color=PALETTE["teal"], scale_factor=1.03), run_time=0.6)
        self.wait(4.9)
        self.play(Indicate(q2[0], color=PALETTE["teal"], scale_factor=1.03), run_time=0.6)
        self.wait(5.9)
        self.play(Indicate(q3[0], color=PALETTE["crimson"], scale_factor=1.03), run_time=0.6)
        self.wait(5.4)

        tell_box = box_around(q3, buff=0.05, color=PALETTE["crimson"])
        self.play(Create(tell_box), run_time=0.3)
        tell_caption = fit(T("That's the tell.", color=PALETTE["crimson"], font_size=24, weight="BOLD"), 10.0)
        # buff 0.4 -> 0.68: GATE B's post-render layout audit caught this
        # caption's real bottom edge at y=-3.6, outside the +/-3.4 safe-area
        # half-height on the true rendered frame (not a guessed margin).
        tell_caption.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(tell_caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5(title)+0.6+0.6+0.6+0.6+0.3+0.4 = 3.6s
        # waits above = 1.0(title)+1.0+4.9+5.9+5.4 = 18.2s
        # remainder tuned to the measured 25.75s Kokoro length (25.75-3.6-18.2=3.95)
        self.wait(3.95)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: a fabricated citation vs a real one, shown side by
# side in identical fluent styling. Both must look equally fluent — the
# whole point is they're visually indistinguishable by tone alone.
# [Source: FACTCHECK.md — both citations fully generic/hypothetical, no
# resemblance to any real paper] "Checkable" callout resolves the fabricated
# one as not resolving to a real source.
# measured audio: 25.58s
# --------------------------------------------------------------------------- #
class B04_FabricatedVsRealCitation(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same fluent tone. One of these isn't real.", color=PALETTE["bg"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def citation_card(header, cite_title, cite_meta, stroke):
            hdr = fit(T(header, color=PALETTE["sage"], font_size=17, font=MONO), 5.0)
            ct = fit(T(cite_title, color=PALETTE["bg"], font_size=17, line_spacing=1.25, weight="BOLD"), 5.0)
            meta = fit(T(cite_meta, color=PALETTE["bg"], font_size=15, line_spacing=1.2), 5.0)
            content = VGroup(hdr, ct, meta).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
            bg = panel(width=5.8, height=content.height + 1.1, fill=PALETTE["ink"], stroke=stroke)
            content.move_to(bg.get_center())
            return VGroup(bg, content), content

        left_card, left_content = citation_card(
            "CITATION A",
            "“Sparse Attention for Long-\nContext Transformers”",
            "Castillo, D. & Ng, P. (2021)\nJournal of Machine Learning Research",
            PALETTE["teal_on_ink"],
        )
        left_card.move_to([-3.35, -0.35, 0])

        right_card, right_content = citation_card(
            "CITATION B",
            "“Recursive Calibration of\nLatent Confidence Vectors”",
            "Harrow, J. & Delacroix, M. (2022)\nJournal of Applied Neural Computation",
            PALETTE["teal_on_ink"],
        )
        right_card.move_to([3.35, -0.35, 0])

        self.play(Create(left_card[0]), Create(right_card[0]), run_time=0.5)
        self.play(FadeIn(left_content, shift=UP * 0.1), FadeIn(right_content, shift=UP * 0.1), run_time=0.6)
        # hold on both, equally fluent, unresolved — matching the narration's
        # "it reads exactly as confidently as a real citation would."
        self.wait(5.0)

        checkable_l = fit(T("CHECKABLE?", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD"), 4.6)
        checkable_l.next_to(left_card, DOWN, buff=0.25)
        checkable_r = fit(T("CHECKABLE?", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD"), 4.6)
        checkable_r.next_to(right_card, DOWN, buff=0.25)
        self.play(FadeIn(checkable_l), FadeIn(checkable_r), run_time=0.4)
        self.wait(3.0)

        verified = T("VERIFIED", color=PALETTE["sage"], font_size=22, font=MONO, weight="BOLD")
        verified.move_to(checkable_l.get_center())
        doesnt_exist = T("DOESN'T EXIST", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD")
        doesnt_exist.move_to(checkable_r.get_center())
        self.play(
            FadeOut(checkable_l), FadeOut(checkable_r),
            FadeIn(verified), FadeIn(doesnt_exist),
            run_time=0.5,
        )
        self.wait(4.5)

        alert_box = box_around(doesnt_exist, buff=0.12, color=PALETTE["gold"])
        self.play(Create(alert_box), run_time=0.3)
        closing = fit(T("The tone never told you.", color=PALETTE["gold"], font_size=22), 10.5)
        closing.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.2s, waits above = 12.5s; remainder tuned to the
        # measured 25.58s Kokoro length (25.58 - 3.2 - 12.5 = 9.88)
        self.wait(8.88)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: the case that would break the rubric if it were
# sloppy — same confident tone, but genuinely true and easy. All 3 rubric
# answers resolve CONFIRMED (sage), visually distinct from B04's failed case.
# [Source: FACTCHECK.md — boiling-point fact, uncontested physical fact]
# measured audio: 25.42s
# --------------------------------------------------------------------------- #
class B05_TrueFactFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same tone. Genuinely true this time.", color=PALETTE["bg"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.5)

        fact_panel = panel(width=9.6, height=2.6, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        fact_panel.move_to([0, 1.5, 0])
        fact_q = fit(T("“Boiling point of water at sea level?”", color=PALETTE["sage"], font_size=20, font=MONO), 8.8)
        fact_a = fit(T("“Yes — 100°C / 212°F. I'm confident in this.”", color=PALETTE["bg"], font_size=20, weight="BOLD"), 8.8)
        fact_content = VGroup(fact_q, fact_a).arrange(DOWN, buff=0.3)
        fact_content.move_to(fact_panel.get_center())

        self.play(Create(fact_panel), run_time=0.5)
        self.play(FadeIn(fact_content, shift=UP * 0.1), run_time=0.6)
        self.wait(4.0)

        def check_tag(label, verdict):
            lbl = fit(T(label, color=PALETTE["bg"], font_size=16, font=MONO), 3.3)
            vd = fit(T(verdict, color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD"), 3.3)
            col = VGroup(lbl, vd).arrange(DOWN, buff=0.18)
            bg = panel(width=3.6, height=col.height + 0.5, fill=PALETTE["ink"], stroke=PALETTE["sage"])
            col.move_to(bg.get_center())
            return VGroup(bg, col)

        t1 = check_tag("CHECKABLE?", "CONFIRMED")
        t2 = check_tag("WOULD IT HEDGE?", "NO NEED")
        t3 = check_tag("TRACKS DIFFICULTY?", "YES — EASY")
        # card width 4.0->3.6, buff 0.4->0.3: GATE V's edge-bleed check found
        # the original 3-card row (12.8 wide) plus its own tags_box buff
        # bled past the +/-6.3 safe-area half-width on the true rendered
        # frame — real margin, not a guessed fix.
        tags = VGroup(t1, t2, t3).arrange(RIGHT, buff=0.3)
        tags.move_to([0, -1.75, 0])

        self.play(FadeIn(tags, shift=UP * 0.1), run_time=0.6)
        self.wait(6.0)

        tags_box = box_around(tags, buff=0.12, color=PALETTE["sage"])
        self.play(Create(tags_box), run_time=0.3)
        self.wait(3.0)

        closing = fit(T("Same fluent tone. Completely different, correct answer.", color=PALETTE["sage"], font_size=22), 11.5)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # closing line's real bottom edge at y=-3.45, outside the +/-3.4
        # safe-area half-height on the true rendered frame.
        closing.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 2.9s, waits above = 13.0s; remainder tuned to the
        # measured 25.42s Kokoro length (25.42 - 2.9 - 13.0 = 9.52)
        self.wait(8.02)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: the 3 questions restated as a concrete checklist —
# a distinct checklist/task card, not a repeat of B03's rubric card.
# measured audio: 23.16s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this on the next answer you get:", color=PALETTE["ink"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def checklist_item(text):
            box = Square(side_length=0.5, color=PALETTE["teal"], stroke_width=3, fill_opacity=0)
            check = T(text, color=PALETTE["ink"], font_size=26)
            row = VGroup(box, fit(check, 11.0)).arrange(RIGHT, buff=0.4)
            return row, box

        row1, box1 = checklist_item("Is it checkable — and did you actually check it?")
        row2, box2 = checklist_item("Would it hedge if you pushed on it?")
        row3, box3 = checklist_item("Does its confidence change with how hard the question is?")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.65)
        list_panel = panel(width=items.width + 1.4, height=items.height + 1.0,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(UP * 0.2)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)

        # All 3 checklist rows revealed TOGETHER (not a sequential build) —
        # keeps real content mass on screen for nearly the whole beat: an
        # earlier sequential-reveal draft left only 1-2 of 3 rows up at
        # GATE V's 50%/85% canvas-fill sample points (50% real fill, under
        # the 55% floor). Checkmarks still land one at a time, timed to the
        # narration's own pacing, so the "ticking through the list" feel is
        # kept without starving the canvas-fill metric.
        self.play(FadeIn(items), run_time=0.6)
        self.wait(1.0)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["crimson"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["crimson"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(5.3)
        self.play(Create(mark2), run_time=0.3)
        self.wait(5.3)
        self.play(Create(mark3), run_time=0.3)
        self.wait(4.0)

        closing = fit(T("No wavering confidence? That's not certainty — that's tone.", color=PALETTE["crimson"], font_size=22), 11.5)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # closing line's real bottom edge at y=-3.45, outside the +/-3.4
        # safe-area half-height on the true rendered frame (same fix
        # pattern as this reel's other titles/closings).
        closing.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5(title)+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 1.0(title)+1.0+5.3+5.3+4.0 = 16.6s
        # remainder tuned to the measured 23.16s Kokoro length
        # (23.16 - 2.8 - 16.6 = 3.76)
        self.wait(3.76)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 11.14s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # font sizes bumped (30/28/32 -> 42/36/46) and buffs widened: GATE
        # V's canvas-fill check measured this beat's real candidate export
        # at only 38% of the safe area (min 55%) — a real underfill, not a
        # false positive. Bigger text is genuine additional content mass,
        # not an oversized invisible frame around the same content.
        line1 = fit(T("A model's tone is generated the same way", color=PALETTE["bg"], font_size=42), 12.0)
        line1b = fit(T("whether it's right or wrong.", color=PALETTE["bg"], font_size=42), 12.0)
        line2 = fit(T("The only question that matters:", color=PALETTE["gold"], font_size=36), 12.0)
        line2b = fit(T("“Can this actually be checked?”", color=PALETTE["gold"], font_size=46, weight="BOLD"), 12.0)

        block1 = VGroup(line1, line1b).arrange(DOWN, buff=0.3)
        block2 = VGroup(line2, line2b).arrange(DOWN, buff=0.4)
        content = VGroup(block1, block2).arrange(DOWN, buff=0.9).move_to(ORIGIN)

        frame = panel(width=content.width + 1.8, height=content.height + 1.2,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(4.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.5)

        # a later, distinct shape-state change (not just the one frame
        # Rectangle created up front) — a real box drawn around the closing
        # question once it has landed, satisfying GATE A's static pre-flight.
        question_box = box_around(line2b, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        # sum of plays = 1.8s, waits above = 6.5s (4.0 + 2.5); remainder
        # tuned to the measured 11.14s Kokoro length (11.14 - 1.8 - 6.5 = 2.84)
        self.wait(2.84)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J. Narration ("Explained with Claude Code.") is short by
# design — the approved beat sheet's exact text — so this card is a brief,
# clean flash, not an extended hold.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font sizes and buff bumped up (handle 64->86, fixed_line 36->46,
        # tagline 30->40, buff 0.55->0.85): GATE V's canvas-fill check
        # measured this beat's real candidate export at only 40% of the
        # safe area (min 55%) — a real underfill, same fix pattern already
        # verified on this fellow's sibling reels' own B08.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=86), 11.6)
        accent = Line(LEFT * 3.6, RIGHT * 3.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=46), 11.0)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=40), 11.0)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame_w = min(content.width + 1.8, 12.4)
        frame_h = min(content.height + 1.1, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        # sum of plays = 0.5s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.01)
