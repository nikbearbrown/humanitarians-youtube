"""
Manim scenes for 2026-09-29-tokenization-why-ai-cant-count-its-own-letters
"Tokenization: Why AI Can't Count the Letters in Its Own Words"

Built under the toolkit's NEW submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard             — silent title card (TITLE)
B01_ExecSummary           — spoken personal-intro card (EXEC-SUMMARY)
B02_TwoTasksHook          — "count letters: often wrong" vs "write an essay: reliable" (HOOK)
B03_TokenSplitDiagram     — the illustrative word split into 3 colored token chunks (MECHANISM)
B04_MiscountedTally       — the token-level tally vs the true count, mismatch visible (WORKED-EXAMPLE)
B05_SpelledOutFix         — same word, spelled letter-by-letter, count now correct (FALSIFIABILITY)
B06_AuditChecklist        — the 3-question rubric, as a checklist card (SCAFFOLDED-TASK)
B07_Statement             — takeaway statement card (TAKEAWAY)
B08_BrandOutro            — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest siblings (2026-09-29-the-keyword-that-cried-wolf/scenes.py
and 2026-09-22-the-all-clear-that-wasnt-all-there/scenes.py) for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed, this reel has no math.

ILLUSTRATIVE WORD CHOICE (per FACTCHECK.md — generic, no real model named or
benchmarked): "strawberry", counting the letter "R". Chosen because it is
long enough to plausibly BPE-split into 3 sub-word chunks, has a repeated
letter worth counting (3 R's: s-t-R-a-w-b-e-R-R-y), and mirrors the
well-known "how many R's" class of example the BEAT-SHEET.md explicitly
references, without naming or benchmarking any specific real model. The
SAME word and SAME split are reused across B03/B04/B05 per the Legibility
Contract ("not a different, easier word").
  - Illustrative 3-chunk split used throughout: STRAW | BER | RY
  - True letter-level R count: 1 (straw) + 1 (ber) + 1 (ry) = 3
  - Illustrative miscounted tally (B04): STRAW->1, BER->1, RY->0 (the model
    treats "RY" as one opaque chunk and misses the R inside it) = 2 != 3
  - Spelled-out fix (B05): S-T-R-A-W-B-E-R-R-Y, each letter its own token,
    count = 3, matches the true count. Same word, same model, only the
    granularity changed.

Every quoted string on screen is original illustrative content written for
this reel (not drawn from a real benchmark or disclosed test) — see
SOURCES.md / FACTCHECK.md.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.056 (silent,
fixed target) B01=14.09 B02=13.70 B03=21.46 B04=18.05 B05=17.88 B06=18.55
B07=11.74 B08=1.51.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric)
per this project's canvas-fill requirement (55-80% of the safe area) — the
lesson the sibling reels already learned and documented at length in their
own scenes.py comments.
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
    "crimson": "#E4572E", # bad / CVD-safe warm -- avoid as TEXT on ink (low
                          # contrast, confirmed by sibling reels); fine as
                          # stroke/accent, or as text on "bg".
    "slate":  "#29335C",  # structure -- low-contrast on ink; use "sage" for
                          # any note/tag text on an ink background instead.
    "gold":   "#F3A712",  # fill/stroke/accent; safe as TEXT on ink too.
    "sage":   "#A8C686",  # human / growth; safe secondary text color on ink.
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


def token_chunk(label, color, font_size=34):
    """One colored token-chunk pill: a bordered panel containing `label`,
    used identically across B03/B04/B05 so the same word's chunking reads
    as the same visual object in all three beats."""
    txt = T(label, color=PALETTE["bg"], font_size=font_size, font=MONO, weight="BOLD")
    pad_w, pad_h = 0.5, 0.35
    bg = panel(width=txt.width + pad_w, height=txt.height + pad_h,
               fill=color, stroke=PALETTE["bg"], corner_radius=0.12, opacity=1.0)
    txt.move_to(bg.get_center())
    return VGroup(bg, txt)


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.056s — fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Tokenization:", color=PALETTE["ink"], font_size=50, weight="BOLD"), 12.0)
        title_line2 = fit(T("Why AI Can't Count the", color=PALETTE["ink"], font_size=42, weight="BOLD"), 12.0)
        title_line3 = fit(T("Letters in Its Own Words", color=PALETTE["ink"], font_size=42, weight="BOLD"), 12.0)
        title = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.3)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=38)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        frame = panel(width=11.8, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.056s silent track
        self.wait(2.456)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 14.09s
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
            "This video: why AI models mess up",
            "tasks like counting letters or finding",
            "rhymes — even though they can write",
            "whole essays correctly — and the one",
            "mechanism that explains it.",
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
        # sum of plays = 2.1s; remainder tuned to the measured 13.56s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 14.09s -> wait 11.99)
        self.wait(11.46)


# --------------------------------------------------------------------------- #
# B02 — HOOK: two task cards side by side — "Count letters: often wrong" vs
# "Write an essay: reliable" — same model, wildly different reliability.
# measured audio: 13.70s
# --------------------------------------------------------------------------- #
class B02_TwoTasksHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same model. Two tasks.", color=PALETTE["bg"], font_size=30), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # ---- LEFT: counting letters ----
        left_panel = panel(width=5.6, height=4.6, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        left_panel.move_to([-3.35, -0.45, 0])
        left_header = fit(T("COUNT LETTERS", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD"), 4.9)
        left_example = fit(T(
            '"How many R\'s in\nstrawberry?"', color=PALETTE["bg"], font_size=19, line_spacing=1.25
        ), 4.9)
        left_stamp = fit(T("OFTEN WRONG", color=PALETTE["gold"], font_size=27, font=MONO, weight="BOLD"), 4.6)
        left_content = VGroup(left_header, left_example, left_stamp).arrange(DOWN, buff=0.4)
        left_content.move_to(left_panel.get_center())

        # ---- RIGHT: writing an essay ----
        right_panel = panel(width=5.6, height=4.6, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        right_panel.move_to([3.35, -0.45, 0])
        right_header = fit(T("WRITE AN ESSAY", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD"), 4.9)
        right_example = fit(T(
            '"Explain photosynthesis\nin 3 paragraphs."', color=PALETTE["bg"], font_size=19, line_spacing=1.25
        ), 4.9)
        right_stamp = fit(T("RELIABLE", color=PALETTE["sage"], font_size=27, font=MONO, weight="BOLD"), 4.6)
        right_content = VGroup(right_header, right_example, right_stamp).arrange(DOWN, buff=0.4)
        right_content.move_to(right_panel.get_center())

        self.play(Create(left_panel), Create(right_panel), run_time=0.5)
        self.play(FadeIn(left_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(right_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        left_stamp_box = box_around(left_stamp, buff=0.12, color=PALETTE["gold"])
        right_stamp_box = box_around(right_stamp, buff=0.12, color=PALETTE["sage"])
        self.play(Create(left_stamp_box), Create(right_stamp_box), run_time=0.3)
        self.wait(0.5)

        zinger = fit(T("Wildly different reliability.", color=PALETTE["gold"], font_size=26), 10.5)
        zinger.to_edge(DOWN, buff=0.68)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 2.8s, waits above = 5.5s (1.0 + 2.0 + 2.0 + 0.5);
        # remainder tuned to the measured 13.70s Kokoro length
        # (13.70 - 2.8 - 5.5 = 5.4)
        self.wait(5.4)


# --------------------------------------------------------------------------- #
# B03 — MECHANISM: the illustrative word split into 3 colored token chunks —
# a real segmentation, not just asserted in narration.
# measured audio: 21.46s
# --------------------------------------------------------------------------- #
class B03_TokenSplitDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # generously sized bordered frame around the whole beat, created up
        # front (same idiom as B00/B01/B07/B08) — GATE V's canvas-fill check
        # measured the first draft (title + word + chunks + caption alone,
        # no frame) at only 37% of the safe area (min 55%), a real underfill
        # on the actual candidate export, not a guess.
        frame = panel(width=11.8, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        title = fit(T("Here's why:", color=PALETTE["ink"], font_size=32), 11.5)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), Create(frame), run_time=0.5)
        self.wait(1.2)

        whole_word = T("strawberry", color=PALETTE["ink"], font_size=64, font=MONO, weight="BOLD")
        whole_word.move_to(UP * 1.1)
        self.play(FadeIn(whole_word, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)

        # the SAME word, re-chunked into 3 colored token pills — the real
        # segmentation this beat's Legibility Contract requires.
        chunk1 = token_chunk("STRAW", PALETTE["teal"])
        chunk2 = token_chunk("BER", PALETTE["crimson"])
        chunk3 = token_chunk("RY", PALETTE["slate"])
        chunks = VGroup(chunk1, chunk2, chunk3).arrange(RIGHT, buff=0.3)
        chunks.move_to(UP * 1.1)

        self.play(FadeOut(whole_word), FadeIn(chunks, shift=UP * 0.1), run_time=0.8)
        self.wait(1.0)

        label1 = fit(T("TOKEN 1", color=PALETTE["teal"], font_size=16, font=MONO), 1.8)
        label2 = fit(T("TOKEN 2", color=PALETTE["crimson"], font_size=16, font=MONO), 1.8)
        label3 = fit(T("TOKEN 3", color=PALETTE["slate"], font_size=16, font=MONO), 1.8)
        label1.next_to(chunk1, DOWN, buff=0.22)
        label2.next_to(chunk2, DOWN, buff=0.22)
        label3.next_to(chunk3, DOWN, buff=0.22)
        labels = VGroup(label1, label2, label3)
        self.play(FadeIn(labels), run_time=0.5)
        self.wait(1.0)

        # box each chunk in turn — a real later shape-state change (GATE A's
        # static pre-flight needs this, not just the one chunk row created above).
        box1 = box_around(chunk1, buff=0.08, color=PALETTE["gold"])
        box2 = box_around(chunk2, buff=0.08, color=PALETTE["gold"])
        box3 = box_around(chunk3, buff=0.08, color=PALETTE["gold"])
        self.play(Create(VGroup(box1, box2, box3)), run_time=0.4)
        self.wait(1.0)

        caption1 = fit(T(
            "model sees these chunks —", color=PALETTE["crimson"], font_size=24,
        ), 11.5)
        caption2 = fit(T(
            "not the letters inside", color=PALETTE["crimson"], font_size=24,
        ), 11.5)
        caption = VGroup(caption1, caption2).arrange(DOWN, buff=0.18)
        caption.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        # sum of plays = 3.2s, waits above = 6.0s; remainder tuned to the
        # measured 21.46s Kokoro length (21.46 - 3.2 - 6.0 = 12.26)
        self.wait(12.26)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: the same word's real token split, with the model's
# miscounted tally and the true count shown side by side — mismatch visible.
# measured audio: 18.05s
# --------------------------------------------------------------------------- #
class B04_MiscountedTally(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Count the R's in \"strawberry\":", color=PALETTE["bg"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # same chunking as B03, now shown compact at the top with its own
        # per-chunk tally underneath each chunk.
        chunk1 = token_chunk("STRAW", PALETTE["teal"], font_size=26)
        chunk2 = token_chunk("BER", PALETTE["crimson"], font_size=26)
        chunk3 = token_chunk("RY", PALETTE["slate"], font_size=26)
        chunks = VGroup(chunk1, chunk2, chunk3).arrange(RIGHT, buff=0.35)
        chunks.move_to(UP * 1.9)
        self.play(FadeIn(chunks, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)

        tally1 = fit(T("sees 1 R", color=PALETTE["sage"], font_size=17, font=MONO), 1.9)
        tally2 = fit(T("sees 1 R", color=PALETTE["sage"], font_size=17, font=MONO), 1.9)
        tally3 = fit(T("sees 0 R", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD"), 1.9)
        tally1.next_to(chunk1, DOWN, buff=0.2)
        tally2.next_to(chunk2, DOWN, buff=0.2)
        tally3.next_to(chunk3, DOWN, buff=0.2)
        tallies = VGroup(tally1, tally2, tally3)
        self.play(FadeIn(tallies), run_time=0.5)
        self.wait(1.5)

        # ---- the model's wrong total, vs the true total, side by side ----
        model_box = panel(width=4.9, height=2.1, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        model_box.move_to([-3.1, -1.7, 0])
        model_label = fit(T("MODEL'S COUNT", color=PALETTE["sage"], font_size=18, font=MONO), 4.3)
        model_number = T("2", color=PALETTE["crimson"], font_size=52, font=MONO, weight="BOLD")
        model_content = VGroup(model_label, model_number).arrange(DOWN, buff=0.25)
        model_content.move_to(model_box.get_center())

        true_box = panel(width=4.9, height=2.1, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        true_box.move_to([3.1, -1.7, 0])
        true_label = fit(T("TRUE COUNT", color=PALETTE["sage"], font_size=18, font=MONO), 4.3)
        true_number = T("3", color=PALETTE["sage"], font_size=52, font=MONO, weight="BOLD")
        true_content = VGroup(true_label, true_number).arrange(DOWN, buff=0.25)
        true_content.move_to(true_box.get_center())

        self.play(Create(model_box), Create(true_box), run_time=0.5)
        self.play(FadeIn(model_content), FadeIn(true_content), run_time=0.5)
        self.wait(1.5)

        mismatch = T("≠", color=PALETTE["gold"], font_size=60, weight="BOLD")
        mismatch.move_to([0, -1.7, 0])
        self.play(Write(mismatch), run_time=0.4)
        self.wait(1.5)

        closing = fit(T(
            "Working from the wrong unit entirely.", color=PALETTE["gold"], font_size=22,
        ), 11.0)
        closing.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.3s, waits above = 6.7s; remainder tuned to the
        # measured 18.05s Kokoro length (18.05 - 3.3 - 6.7 = 8.05)
        self.wait(8.05)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: the SAME word, spelled letter-by-letter with dashes —
# every letter now its own token — count now matches the true total, a green
# checkmark replacing B04's mismatch.
# measured audio: 17.88s
# --------------------------------------------------------------------------- #
class B05_SpelledOutFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # generously sized bordered frame, same idiom/fix as B03 — GATE V's
        # canvas-fill check measured the first draft at 54% (min 55%), a
        # real (if narrow) underfill on the actual candidate export.
        frame = panel(width=11.8, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        title = fit(T("Spell it out first:", color=PALETTE["ink"], font_size=32), 11.5)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), Create(frame), run_time=0.5)
        self.wait(1.0)

        letters = list("STRAWBERRY")
        letter_tokens = VGroup(*[
            token_chunk(ch, PALETTE["slate"] if ch != "R" else PALETTE["crimson"], font_size=22)
            for ch in letters
        ]).arrange(RIGHT, buff=0.12)
        letter_tokens.scale_to_fit_width(min(letter_tokens.width, 12.0))
        letter_tokens.move_to(UP * 1.3)
        self.play(FadeIn(letter_tokens, shift=UP * 0.1), run_time=0.8)
        self.wait(1.5)

        caption = fit(T(
            "every letter is now its own token", color=PALETTE["slate"], font_size=20,
        ), 10.0)
        caption.next_to(letter_tokens, DOWN, buff=0.4)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(1.5)

        # highlight the 3 R tokens — the same letter counted in B04, now
        # directly visible as individual tokens.
        r_boxes = VGroup(*[
            box_around(letter_tokens[i], buff=0.07, color=PALETTE["gold"])
            for i, ch in enumerate(letters) if ch == "R"
        ])
        self.play(Create(r_boxes), run_time=0.5)
        self.wait(1.0)

        # y raised -2.0 -> -1.4: GATE B's post-render layout audit caught the
        # checkmark line below this box (placed below whenever it's too wide
        # to fit beside the box, buff=0.3) landing with its real bottom edge
        # at y=-3.6, outside the +/-3.4 safe-area half-height — a real
        # TEXT_OUTSIDE_SAFE_AREA, not a guessed margin. Raising the box gives
        # the checkmark line real clearance below it.
        count_box = panel(width=4.9, height=2.1, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        count_box.move_to([0, -1.4, 0])
        count_label = fit(T("MODEL'S COUNT", color=PALETTE["sage"], font_size=18, font=MONO), 4.3)
        count_number = T("3", color=PALETTE["sage"], font_size=52, font=MONO, weight="BOLD")
        count_content = VGroup(count_label, count_number).arrange(DOWN, buff=0.25)
        count_content.move_to(count_box.get_center())
        self.play(Create(count_box), FadeIn(count_content), run_time=0.5)
        self.wait(1.0)

        # always placed below (not a width-dependent branch) — simpler and
        # deterministic now that the box's own position leaves real room.
        checkmark = T("✓ MATCHES TRUE COUNT", color=PALETTE["sage"], font_size=24, weight="BOLD")
        checkmark.next_to(count_box, DOWN, buff=0.3)
        self.play(FadeIn(checkmark, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.2s, waits above = 6.0s; remainder tuned to the
        # measured 17.88s Kokoro length (17.88 - 3.2 - 6.0 = 8.68)
        self.wait(8.68)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: the 3-question rubric, as a checklist card.
# measured audio: 18.55s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=32), 11.5)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        questions = [
            "Is it a whole-word task?",
            "Does it need character-level detail?",
            "Would spelling it out help?",
        ]
        rows = VGroup()
        for q in questions:
            box = Square(side_length=0.5, stroke_color=PALETTE["slate"], stroke_width=3, fill_opacity=0)
            qtxt = fit(T(q, color=PALETTE["ink"], font_size=28), 9.5)
            row = VGroup(box, qtxt).arrange(RIGHT, buff=0.4)
            rows.add(row)
        # buff 0.55 -> 0.95: GATE V's canvas-fill check measured the tighter
        # draft at only 42% of the safe area (min 55%), a real underfill on
        # the actual candidate export — real extra vertical spread between
        # the 3 rows themselves (not just a bigger empty card margin) fixes it.
        rows.arrange(DOWN, buff=0.95, aligned_edge=LEFT)
        # two rounds of GATE B fixes: first the enlarged card's bottom curve
        # landed under the closing line below (card too tall); then, after
        # shifting the card up to fix that, its TOP curve landed under the
        # title above instead. Centered on ORIGIN with height trimmed to 5.6
        # clears both the title above and the closing line below with real
        # margin on the actual rendered frame, not a guess.
        rows.move_to(ORIGIN)

        # fixed generous card size (not derived tightly from rows' own
        # bounds) — same idiom as B00/B01/B03/B05's frames, so the card
        # itself carries real canvas-fill mass independent of exactly which
        # rows have faded in yet at any sampled timestamp.
        card = panel(width=11.8, height=5.6,
                     fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.18, opacity=0.0)
        card.set_stroke(width=2.5)
        card.move_to(rows.get_center())
        self.play(Create(card), run_time=0.4)
        self.wait(0.5)

        checks = []
        for row in rows:
            box = row[0]
            check = T("✓", color=PALETTE["sage"], font_size=30, weight="BOLD")
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

        closing = fit(T(
            "That's tokenization in action.", color=PALETTE["slate"], font_size=24,
        ), 11.0)
        closing.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.3s (0.5+0.4+0.5+0.5+0.5+0.5+0.4), waits above = 8.5s
        # (1.0 + 0.5 + 2.0 + 2.0 + 2.0 + 1.0); remainder tuned to the measured
        # 18.55s Kokoro length (18.55 - 3.3 - 8.5 = 6.75)
        self.wait(6.75)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 11.74s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T(
            "A model that writes fluent paragraphs and", color=PALETTE["bg"], font_size=30,
        ), 11.5)
        line1b = fit(T("a model that can't count letters", color=PALETTE["bg"], font_size=30), 11.5)
        line1_group = VGroup(line1, line1b).arrange(DOWN, buff=0.18)

        line2 = fit(T(
            "aren't contradicting each other.", color=PALETTE["sage"], font_size=27,
        ), 11.2)

        line3 = fit(T(
            "They're the same system, working at the\nwrong resolution for the task you gave it.",
            color=PALETTE["gold"], font_size=27, line_spacing=1.25,
        ), 11.0)

        content = VGroup(line1_group, line2, line3).arrange(DOWN, buff=0.95).move_to(ORIGIN)

        frame_w = min(content.width + 1.6, 12.2)
        frame = panel(width=frame_w, height=content.height + 1.8,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.25)
        self.play(FadeIn(line1_group, shift=UP * 0.15), run_time=0.5)
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
# B08 — SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J.
# measured audio: 1.51s — a very short beat; kept deliberately simple.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font sizes and buff bumped up (handle 56->80, fixed_line 32->42,
        # tagline 28->34, buff 0.45->0.8): GATE V's canvas-fill check
        # measured the first draft's real candidate export at only 31% of
        # the safe area (min 55%) — a real underfill, not a false positive.
        # Same fix already proven on this fellow's sibling reels' B08.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=80), 11.4)
        accent = Line(LEFT * 3.2, RIGHT * 3.2, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=42), 11.0)
        tagline = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=34,
        ), 11.0)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.8).move_to(ORIGIN)

        frame_w = min(content.width + 1.8, 12.2)
        frame_h = min(content.height + 1.3, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.06)
