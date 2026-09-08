"""scenes.py — Manim scenes for the-number-that-wasnt-there (claude-divij, Video 3).

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491,
plus three verdict colors introduced for the Chapter-3 scorecard: green #4C9A6A
(worked as designed / held), amber #C9932E (a real but informative gap), red
#B0473A (a real, project-redirecting flaw). Type: Montserrat (DISPLAY, structural
default) / EB Garamond (SERIF, editorial voice only) / PT Mono (MONO, data+code
only) — see graphics_lib.py. Boxes are sized to their actual content via
auto_box, never hand-measured.

Every scene ends with hold_to(self, TARGET) so its NATIVE duration matches the
beat's target length — compile.py then never has to stretch a short clip into
visible slow motion. TARGET constants below are the PRE-AUDIO estimated_duration_s
from beat_sheet.json — retime against actual Kokoro output per BUILD-PROMPT.md
Step 3 before final render. Nothing in this file has been rendered yet.

Safe frame: x in [-6.4, 6.4], y in [-3.6, 3.6].

Never a raw Text("✓")/Text("✕") — Montserrat has no glyph for either and Pango
silently renders a .notdef box. Use checked() from graphics_lib, which composes
the symbol in Manim's default font with the word in DISPLAY.

CHAPTER 3 REBUILD (2026-08-29): the source script expanded Chapter 3 from a
three-beat, ~95s summary into a seven-beat, full six-field (WHAT/WHY/GOOD
RESULT/GIVEN/HAPPENED/MEANS) deep-dive on all five tests. B03-B09 below are new;
B01/B02 are the unchanged (B02 lightly trimmed) recap/chapter-2 beats; B10-B13
are the old B06-B09 chapter-4-through-close beats, renumbered only (content and
scene bodies unchanged) to stay in sync with the rebuilt beat_sheet.json.
"""
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"

# Chapter-3 scorecard verdict colors (script's own VISUAL directions: amber,
# amber, green, green, red across the five slots).
GREEN = "#4C9A6A"
AMBER = "#C9932E"
RED = "#B0473A"


def hold_to(scene, target, minimum=0.4):
    """Pad the scene out to `target` seconds of native runtime."""
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, target - elapsed))


def boxed(inner, color=INK, h_pad=0.45, v_pad=0.32, **kw):
    """content -> VGroup(box, content), box sized to the content."""
    b = auto_box(inner, h_pad=h_pad, v_pad=v_pad, color=color, **kw)
    return VGroup(b, inner)


def muted_chip(text, size=24):
    """A de-emphasised chip. Never GHOST-filled — label_chip puts WHITE text on
    the fill, and white on #A9A491 is unreadable. SOFT is the muted floor."""
    return label_chip(text, SOFT, size=size)


def num_chip(text, color=INK, size=26):
    t = mono(text, size=size, color=color)
    b = auto_box(t, h_pad=0.22, v_pad=0.16, color=color)
    return VGroup(b, t)


def scorecard(state, y=3.05, active_idx=None):
    """The 5-slot Chapter-3 scorecard. `state[i]` is None for a still-pending
    slot (grey outline, unfilled) or a hex color for a slot whose test has
    already resolved. `active_idx` (0-based), if given, gets a terracotta
    outline highlight even while still pending — used for "this is the test
    we're on right now" before its color lands. Reused persistently in spirit
    across B03 (all None) through B09 (all filled) — since each Manim beat
    renders independently, the persistence is simulated by every beat
    redrawing the scorecard in its correct cumulative state, same convention
    the old B03-B05 counter_panel used for the five-tests arc."""
    chips = VGroup()
    for i in range(5):
        col = state[i]
        is_active = (active_idx == i) and col is None
        stroke = col if col else (ACC if is_active else GHOST)
        fill = col if col else BG
        txt_color = "#FFFFFF" if col else (ACC if is_active else GHOST)
        t = mono(f"T{i + 1}", size=20, color=txt_color)
        box = Rectangle(width=1.15, height=0.62,
                         stroke_width=(3 if is_active else 2.2),
                         color=stroke, fill_color=fill,
                         fill_opacity=(0.88 if col else 0.05))
        chip = VGroup(box, t)
        t.move_to(box)
        chips.add(chip)
    chips.arrange(RIGHT, buff=0.24).move_to([0, y, 0])
    return chips


def test_card_rows(fields, size=19, label_size=15):
    """fields: list of 6 (label, value) tuples — WHAT/WHY/GOOD RESULT/GIVEN/
    HAPPENED/MEANS. value may contain literal '\\n' for wrapping a long line.
    Returns a left-aligned VGroup, one label+value pair per row, stacked."""
    rows = VGroup()
    for lbl, val in fields:
        lbl_t = label(lbl, size=label_size, weight="BOLD", color=SOFT)
        val_t = label(val, size=size, color=INK, line_spacing=0.82)
        row = VGroup(lbl_t, val_t).arrange(DOWN, buff=0.04, aligned_edge=LEFT)
        rows.add(row)
    rows.arrange(DOWN, buff=0.19, aligned_edge=LEFT)
    return rows


def fit_fields(fields, x, top=2.05, bottom=-2.55, max_scale=0.84):
    """Scale `fields` down (never up) so its rendered height always fits
    between `top` and `bottom`, regardless of how many rows wrap to two
    lines in a given test card, then move it to the given x, vertically
    centered in that band. Computed rather than hand-tuned per scene:
    the six-field cards vary from 8 to 10 lines of content depending on
    the test, and a fixed guessed scale silently collides with the
    caption text below it on the denser cards (B05/B06) — this guarantees
    clearance instead of hoping a hardcoded number happens to be enough."""
    avail_h = top - bottom
    scale_factor = min(max_scale, (avail_h / fields.height) * 0.94)
    fields.scale(scale_factor).move_to([x, (top + bottom) / 2, 0])
    return fields


# ─────────────────────────────────────────────────────────────────────────────
#  B01_FixtureToRealGrader   (target ~45s)
#  Recap: fixture crossed out, a second real grader in, still nothing observed.
# ─────────────────────────────────────────────────────────────────────────────
class B01_FixtureToRealGrader(Scene):
    TARGET = 37.63  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        head = label("WHAT ALREADY EXISTED", size=28, weight="BOLD", color=SOFT)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        # ── two-panel: fixture out, real grader in ──────────────────────────
        left_t = mono("FIXTURE", size=30, color=SOFT)
        left = boxed(left_t, color=GHOST).move_to([-3.3, 1.3, 0])
        strike = Line(left[0].get_corner(DL), left[0].get_corner(UR),
                      color=SOFT, stroke_width=3)

        right_t = mono("EARNINGS_GRADER.PY", size=26, color=INK)
        right_sub = label("real SEC data", size=22, color=SOFT)
        right_inner = VGroup(right_t, right_sub).arrange(DOWN, buff=0.16)
        right = boxed(right_inner, color=ACC).move_to([3.3, 1.3, 0])

        self.play(FadeIn(left), run_time=0.5)
        self.wait(0.8)
        self.play(Create(strike), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(right), run_time=0.5)
        self.wait(1.6)

        arith = label_chip("SET ARITHMETIC. NO MODEL. NO JUDGE.", ACC, size=24)
        arith.move_to([0, -0.3, 0])
        self.play(FadeIn(arith), run_time=0.5)
        self.wait(2.2)

        self.play(FadeOut(VGroup(left, strike, right, arith, head)), run_time=0.55)

        # ── 143/143, desaturated ─────────────────────────────────────────────
        pass_t = mono("143 / 143", size=56, color=INK)
        pass_sub = label("zero lines changed in the comparator", size=24, color=SOFT)
        pass_group = VGroup(pass_t, pass_sub).arrange(DOWN, buff=0.28)
        pass_group.move_to([0, 1.2, 0])
        self.play(FadeIn(pass_group), run_time=0.5)
        self.wait(1.8)
        self.play(pass_group.animate.set_opacity(0.32), run_time=0.7)
        self.wait(1.0)

        # ── the empty OBSERVED chip ──────────────────────────────────────────
        observed = muted_chip("OBSERVED — STILL EMPTY", size=26)
        observed.move_to([0, -1.6, 0])
        self.play(FadeIn(observed, scale=0.94), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_InputVsInvented   (target ~42s)
#  A local model, then Producer A's real inputs vs. its invented
#  debt-to-equity line — the number that came from nowhere. (Trimmed: the
#  two-failed-API-keys detour was cut from the script; this beat now opens
#  directly on the local-model chip, no crossed "FREE-TIER LIMIT" /
#  "KEY SUSPENDED" chips.)
# ─────────────────────────────────────────────────────────────────────────────
class B02_InputVsInvented(Scene):
    TARGET = 33.15  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        # ── local model, one clean chip (no API-key detour) ─────────────────
        moved = label_chip("RAN ON A MODEL SET UP LOCALLY", ACC, size=24)
        moved.move_to([0, 3.0, 0])
        self.play(FadeIn(moved), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(moved), run_time=0.4)

        # ── left panel: Producer A's real inputs ─────────────────────────────
        head_a = label("PRODUCER A — REAL INPUTS", size=26, weight="BOLD", color=SOFT)
        head_a.move_to([-3.3, 3.0, 0])
        inputs = VGroup(*[num_chip(t) for t in
                          ("Assets", "Revenues", "NetIncomeLoss")])
        inputs.arrange(DOWN, buff=0.3).move_to([-3.3, 1.1, 0])
        self.play(FadeIn(head_a), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in inputs],
                              lag_ratio=0.3), run_time=1.2)
        self.wait(1.4)

        # ── right panel: the invented line ───────────────────────────────────
        head_b = label("WHAT IT WROTE", size=26, weight="BOLD", color=SOFT)
        head_b.move_to([3.3, 3.0, 0])
        claim = serif("\"debt-to-equity ratio\nas 0.34\"", size=28, color=ACC,
                      line_spacing=0.8)
        claim_box = boxed(claim, color=ACC).move_to([3.3, 1.3, 0])
        qsrc = DashedVMobject(
            Rectangle(width=1.1, height=0.75, color=GHOST, stroke_width=2.5),
            num_dashes=20, color=GHOST)
        qmark = label("?", size=44, color=GHOST)
        qmark.move_to(qsrc)
        qgroup = VGroup(qsrc, qmark)
        qgroup.next_to(claim_box, DOWN, buff=0.3)
        qlbl = label("source data", size=20, color=GHOST).next_to(qgroup, DOWN, buff=0.14)

        self.play(FadeIn(head_b), run_time=0.4)
        self.play(FadeIn(claim_box), run_time=0.5)
        self.wait(1.0)
        self.play(Create(qsrc), FadeIn(qmark), FadeIn(qlbl), run_time=0.5)
        self.wait(1.6)

        verdict = label("NOT CLOSE. NOT DERIVED.\nNOT IN THE DATA AT ALL.",
                        size=24, weight="BOLD", color=ACC, line_spacing=0.75)
        verdict.move_to([0, -1.35, 0])
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(2.2)

        self.play(FadeOut(VGroup(head_a, inputs, head_b, claim_box, qgroup,
                                 qlbl, verdict)), run_time=0.6)

        # ── Producer B: zero numbers cited ───────────────────────────────────
        head_c = label("PRODUCER B — ZERO NUMBERS CITED", size=26,
                       weight="BOLD", color=SOFT).move_to([0, 2.2, 0])
        prose = VGroup(
            serif("\"consistent\"", size=26, color=INK, italic=True),
            serif("\"significantly large\"", size=26, color=INK, italic=True),
        ).arrange(DOWN, buff=0.24).move_to([0, 0.7, 0])
        counter = mono("0 numbers cited", size=26, color=ACC).move_to([0, -0.7, 0])

        self.play(FadeIn(head_c), run_time=0.4)
        self.play(FadeIn(prose), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(counter), run_time=0.4)
        self.wait(1.6)

        stamp = label("CONTRADICTION FLAGGED", size=30, weight="BOLD", color=ACC)
        stamp.move_to([0, -2.0, 0])
        self.play(FadeIn(stamp, scale=1.1), run_time=0.5)
        self.wait(1.2)
        caption = label("right call, wrong reason", size=24, color=SOFT)
        caption.next_to(stamp, DOWN, buff=0.3)
        self.play(FadeIn(caption), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ScorecardIntro   (target ~23s)   Chapter 3 opener
#  The blank five-slot scorecard appears — nothing filled in yet.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ScorecardIntro(Scene):
    TARGET = 15.77  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([None] * 5, y=2.85)
        head = label("ONE SURPRISING RESULT COULD BE NOISE", size=21,
                    weight="BOLD", color=SOFT).next_to(card, UP, buff=0.22)
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.8)

        self.play(FadeIn(card, scale=0.94), run_time=0.6)
        self.wait(1.0)

        fields = VGroup(*[
            mono(t, size=18, color=SOFT) for t in
            ("WHAT", "WHY", "GOOD RESULT", "GIVEN", "HAPPENED", "MEANS")
        ]).arrange(RIGHT, buff=0.45).move_to([0, 1.4, 0])
        self.play(LaggedStart(*[FadeIn(f) for f in fields], lag_ratio=0.15),
                  run_time=1.2)
        self.wait(1.2)

        cap = label("not a quick pass or fail —\nthe full six-field treatment, each test",
                   size=24, weight="BOLD", color=INK, line_spacing=0.75)
        cap.move_to([0, -1.4, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.4)

        five = label_chip("HERE'S ALL FIVE", ACC, size=24)
        five.move_to([0, -2.6, 0])
        self.play(FadeIn(five, scale=1.05), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Test1ClaimVerification   (target ~92s)   scorecard slot 1
#  Claim verification correctly flagged the citation, but the regex never
#  even saw the bare-decimal number that started it.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Test1ClaimVerification(Scene):
    TARGET = 72.19  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([None] * 5, active_idx=0)
        self.play(FadeIn(card), run_time=0.5)
        title = label("TEST 1 — CLAIM VERIFICATION", size=25, weight="BOLD",
                     color=INK).next_to(card, DOWN, buff=0.28)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.6)

        fields = test_card_rows([
            ("WHAT", "fetch + match source"),
            ("WHY", "catch fake citations"),
            ("GOOD RESULT", "honest confirm / not-found"),
            ("GIVEN", "debt-to-equity citation + SEC\nsource, 1% tolerance"),
            ("HAPPENED", "extraction never captured \"0.34\" —\nno bare-decimal case"),
            ("MEANS", "checker was starved upstream,\nnot broken itself"),
        ])
        fit_fields(fields, -3.1)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in fields],
                              lag_ratio=0.35), run_time=2.4)
        self.wait(1.0)

        # ── the regex gap, right side ─────────────────────────────────────────
        pattern = mono(r"$..|..%|..x|..bps", size=24, color=INK)
        pattern.move_to([3.3, 1.3, 0])
        pbox = auto_box(pattern, h_pad=0.4, v_pad=0.28, color=GHOST)
        self.play(Create(pbox), FadeIn(pattern), run_time=0.6)
        self.wait(1.0)

        gap = DashedVMobject(
            Rectangle(width=1.1, height=0.5, color=RED, stroke_width=3),
            num_dashes=14, color=RED)
        gap.next_to(pbox, DOWN, buff=0.35)
        gap_lbl = label("bare decimal?", size=18, color=RED).next_to(gap, DOWN, buff=0.14)
        self.play(Create(gap), FadeIn(gap_lbl), run_time=0.5)
        self.wait(0.8)

        num = mono("0.34", size=30, color=RED).move_to([3.3, -1.2, 0])
        self.play(FadeIn(num), run_time=0.4)
        self.play(num.animate.move_to(gap.get_center()).set_opacity(0.0),
                  run_time=0.8)
        self.wait(1.6)

        v1 = label_chip("CITATION CORRECTLY\nFLAGGED AS BROKEN", ACC, size=18)
        v1.move_to([3.3, -2.6, 0])
        self.play(FadeIn(v1), run_time=0.5)
        self.wait(1.0)

        cap = label("but it never saw the number", size=22, weight="BOLD",
                   color=INK)
        cap.move_to([0, -3.25, 0])
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.2)

        new_card = scorecard([AMBER, None, None, None, None])
        new_card.move_to(card.get_center())
        upshot = label("upstream gap", size=16, color=AMBER).next_to(
            new_card[0], DOWN, buff=0.12)
        self.play(Transform(card, new_card), FadeOut(title), FadeIn(upshot), run_time=0.7)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Test2Determinism   (target ~100s)   scorecard slot 2
#  Same seed, same temperature, five runs — four cluster on one wrong
#  answer, the original outlier never repeats.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Test2Determinism(Scene):
    TARGET = 80.47  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([AMBER, None, None, None, None], active_idx=1)
        self.play(FadeIn(card), run_time=0.5)
        title = label("TEST 2 — DETERMINISM", size=25, weight="BOLD",
                     color=INK).next_to(card, DOWN, buff=0.28)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.6)

        fields = test_card_rows([
            ("WHAT", "same input, 5x"),
            ("WHY", "noise vs. stable pattern"),
            ("GOOD RESULT", "converge, or repeat\nthe same failure"),
            ("GIVEN", "temp 0 (confirmed default), seed 42\n(default; this-run use unconfirmed)"),
            ("HAPPENED", "4-of-5 clustered,\n1 outlier never repeated"),
            ("MEANS", "narrows but doesn't collapse behavior;\nthe fabrication was the outlier"),
        ])
        fit_fields(fields, -3.2)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in fields],
                              lag_ratio=0.35), run_time=2.6)
        self.wait(1.0)

        bubbles = VGroup(*[Circle(radius=0.34, color=GHOST, stroke_width=2.2,
                                  fill_opacity=0.12, fill_color=GHOST)
                           for _ in range(5)])
        bubbles.arrange(RIGHT, buff=0.32).move_to([3.1, 1.5, 0])
        self.play(LaggedStart(*[FadeIn(b, scale=0.8) for b in bubbles],
                              lag_ratio=0.2), run_time=1.1)
        self.wait(0.6)

        cluster = bubbles[:4]
        outlier = bubbles[4]
        self.play(*[c.animate.move_to([2.1 + i * 0.72, 1.5, 0]).set_stroke(
            color=AMBER, width=3).set_fill(color=AMBER, opacity=0.16)
            for i, c in enumerate(cluster)],
            outlier.animate.move_to([4.8, 0.3, 0]).set_opacity(0.4),
            run_time=1.0)
        self.wait(0.8)

        out_lbl = label("ORIGINAL —\nNEVER REPEATED", size=16, color=GHOST,
                        line_spacing=0.65)
        out_lbl.next_to(outlier, DOWN, buff=0.18)
        self.play(FadeIn(out_lbl), run_time=0.5)
        self.wait(1.4)

        cap = label("one dominant, confidently wrong answer.\none earlier outlier.",
                   size=20, weight="BOLD", color=INK, line_spacing=0.7)
        cap.move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.2)

        new_card = scorecard([AMBER, AMBER, None, None, None])
        new_card.move_to(card.get_center())
        upshot = label("real gap, but informative", size=16, color=AMBER).next_to(
            new_card[1], DOWN, buff=0.12)
        self.play(Transform(card, new_card), FadeOut(title), FadeIn(upshot), run_time=0.7)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Test3ConsistencyProbe   (target ~90s)   scorecard slot 3
#  A second independent pass, scored on word/number overlap — the hard
#  divergence flag fires exactly as designed.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Test3ConsistencyProbe(Scene):
    TARGET = 70.42  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([AMBER, AMBER, None, None, None], active_idx=2)
        self.play(FadeIn(card), run_time=0.5)
        title = label("TEST 3 — CONSISTENCY PROBE", size=25, weight="BOLD",
                     color=INK).next_to(card, DOWN, buff=0.28)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.6)

        fields = test_card_rows([
            ("WHAT", "second independent pass,\nscored overlap"),
            ("WHY", "catch drift without\nneeding outside truth"),
            ("GOOD RESULT", "high agreement, or\na hard flag on divergence"),
            ("GIVEN", "weights 0.4 word / 0.6 number"),
            ("HAPPENED", "number appeared once, never repeated\n-> flag fires"),
            ("MEANS", "worked as designed, no gap"),
        ])
        fit_fields(fields, -3.1)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in fields],
                              lag_ratio=0.35), run_time=2.4)
        self.wait(1.0)

        # ── two independent runs, one has the number, one doesn't ────────────
        run1_lbl = label("RUN 1", size=18, color=SOFT).move_to([2.5, 1.7, 0])
        run1_num = mono("0.34", size=28, color=GREEN).next_to(run1_lbl, DOWN, buff=0.2)
        run2_lbl = label("RUN 2", size=18, color=SOFT).move_to([4.6, 1.7, 0])
        run2_num = label("— absent —", size=20, color=GHOST).next_to(
            run2_lbl, DOWN, buff=0.2)
        self.play(FadeIn(run1_lbl), FadeIn(run2_lbl), run_time=0.5)
        self.play(FadeIn(run1_num), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(run2_num), run_time=0.5)
        self.wait(1.2)

        flag = label_chip("HARD DIVERGENCE FLAG", GREEN, size=18)
        flag.move_to([3.55, -0.2, 0])
        bolt = Line([2.6, 1.1, 0], [4.5, 1.1, 0], color=GREEN, stroke_width=2)
        self.play(Create(bolt), FadeIn(flag, scale=1.1), run_time=0.6)
        self.wait(1.4)

        cap = label("of all five tests, the one that worked\nprecisely as intended",
                   size=20, weight="BOLD", color=INK, line_spacing=0.7)
        cap.move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.2)

        new_card = scorecard([AMBER, AMBER, GREEN, None, None])
        new_card.move_to(card.get_center())
        upshot = label("worked as intended", size=16, color=GREEN).next_to(
            new_card[2], DOWN, buff=0.12)
        self.play(Transform(card, new_card), FadeOut(title), FadeIn(upshot), run_time=0.7)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Test4GuardrailStress   (target ~72s)   scorecard slot 4
#  A pure structural test — can the format hold at all, independent of
#  whether the content reasoned correctly.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Test4GuardrailStress(Scene):
    TARGET = 53.95  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([AMBER, AMBER, GREEN, None, None], active_idx=3)
        self.play(FadeIn(card), run_time=0.5)
        title = label("TEST 4 — GUARDRAIL STRESS TEST", size=24, weight="BOLD",
                     color=INK).next_to(card, DOWN, buff=0.28)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.6)

        fields = test_card_rows([
            ("WHAT", "structural parse check,\nnot content check"),
            ("WHY", "everything downstream\ndepends on this layer"),
            ("GOOD RESULT", "~100% first-try parse, 0 halts"),
            ("GIVEN", "24 real calls, first attempt only"),
            ("HAPPENED", "24/24, 0 retries, 0 halts"),
            ("MEANS", "format layer solid; failure is\nin content, not structure"),
        ])
        fit_fields(fields, -3.1)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in fields],
                              lag_ratio=0.35), run_time=2.2)
        self.wait(1.0)

        # ── a simple pass/fail structural indicator ─────────────────────────
        rail = mono("24 / 24", size=48, color=GREEN).move_to([3.3, 1.3, 0])
        self.play(FadeIn(rail), run_time=0.5)
        self.wait(1.0)

        chips = VGroup(
            checked("0 retries", size=18, color=GREEN),
            checked("0 halts", size=18, color=GREEN),
        ).arrange(DOWN, buff=0.24).next_to(rail, DOWN, buff=0.4)
        self.play(FadeIn(chips), run_time=0.5)
        self.wait(1.4)

        cap = label("whatever else is wrong this week,\nit isn't the format layer",
                   size=20, weight="BOLD", color=INK, line_spacing=0.7)
        cap.move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.2)

        new_card = scorecard([AMBER, AMBER, GREEN, GREEN, None])
        new_card.move_to(card.get_center())
        upshot = label("held", size=16, color=GREEN).next_to(
            new_card[3], DOWN, buff=0.12)
        self.play(Transform(card, new_card), FadeOut(title), FadeIn(upshot), run_time=0.7)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_Test5Breadth   (target ~90s)   scorecard slot 5
#  Twelve real companies. Eleven flagged. One flagged case, inspected
#  closely, turns out to be a false positive — two correct, unrelated claims.
# ─────────────────────────────────────────────────────────────────────────────
class B08_Test5Breadth(Scene):
    TARGET = 71.98  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([AMBER, AMBER, GREEN, GREEN, None], active_idx=4)
        self.play(FadeIn(card), run_time=0.5)
        title = label("TEST 5 — BREADTH TEST", size=25, weight="BOLD",
                     color=INK).next_to(card, DOWN, buff=0.28)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.6)

        fields = test_card_rows([
            ("WHAT", "same comparison, 12 companies"),
            ("WHY", "rule out a one-company fluke"),
            ("GOOD RESULT", "flags track real contradictions"),
            ("GIVEN", "12 tickers, flag unmodified"),
            ("HAPPENED", "11/12 flagged, 1 clean case\ninspected shows false-positive"),
            ("MEANS", "flag conflates disagreement\nwith topical non-overlap"),
        ])
        fit_fields(fields, -3.1)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in fields],
                              lag_ratio=0.35), run_time=2.4)
        self.wait(0.8)

        # ── twelve ticker tiles, 4 x 3 ────────────────────────────────────────
        tiles = VGroup()
        for i in range(12):
            t = Rectangle(width=0.62, height=0.36, color=GHOST, stroke_width=1.6,
                         fill_opacity=0.08, fill_color=GHOST)
            tiles.add(t)
        tiles.arrange_in_grid(rows=3, cols=4, buff=0.14).move_to([3.3, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.08),
                  run_time=1.0)
        self.wait(0.5)

        flagged_idx = [i for i in range(12) if i != 7]
        self.play(*[tiles[i].animate.set_stroke(color=RED, width=2.2).set_fill(
            color=RED, opacity=0.28) for i in flagged_idx], run_time=0.8)
        grey_lbl = label("both agents cited zero numbers", size=13, color=SOFT)
        grey_lbl.next_to(tiles[7], DOWN, buff=0.14)
        self.play(FadeIn(grey_lbl), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(grey_lbl)),
                  *[FadeOut(t) for i, t in enumerate(tiles) if i != 3],
                  run_time=0.5)
        self.play(tiles[3].animate.move_to([3.3, 2.0, 0]).scale(1.6), run_time=0.5)
        self.wait(0.5)

        colA = VGroup(label("agent A", size=15, color=SOFT),
                     label("real assets + revenue", size=17, color=INK),
                     ).arrange(DOWN, buff=0.12)
        colB = VGroup(label("agent B", size=15, color=SOFT),
                     label("real earnings per share", size=17, color=INK),
                     ).arrange(DOWN, buff=0.12)
        cols = VGroup(colA, colB).arrange(DOWN, buff=0.3).move_to([2.15, 0.3, 0])
        self.play(FadeIn(cols), run_time=0.5)
        self.wait(0.5)
        okA = checked("CORRECT", size=15, color=RED).next_to(colA, RIGHT, buff=0.25)
        okB = checked("CORRECT", size=15, color=RED).next_to(colB, RIGHT, buff=0.25)
        self.play(FadeIn(okA), FadeIn(okB), run_time=0.5)
        self.wait(1.2)

        cap = label("the flag doesn't yet know disagreement\nfrom two agents talking past each other",
                   size=19, weight="BOLD", color=INK, line_spacing=0.72)
        cap.move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.0)

        new_card = scorecard([AMBER, AMBER, GREEN, GREEN, RED])
        new_card.move_to(card.get_center())
        upshot = label("real gap found", size=16, color=RED).next_to(
            new_card[4], DOWN, buff=0.12)
        self.play(Transform(card, new_card), FadeOut(title), FadeIn(upshot), run_time=0.7)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_ScorecardComplete   (target ~12s)   Chapter 3 closer
#  Full scorecard, all five slots filled and colored.
# ─────────────────────────────────────────────────────────────────────────────
class B09_ScorecardComplete(Scene):
    TARGET = 13.14  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        card = scorecard([AMBER, AMBER, GREEN, GREEN, RED])
        self.play(FadeIn(card, scale=1.05), run_time=0.5)
        self.wait(1.0)

        # A per-chip horizontal label (even staggered into two rows) doesn't
        # fit: several of these phrases are wider than the 2.78-unit
        # same-row gap between non-adjacent chips at any legible size. A
        # vertical list below the scorecard, each line tagged and colored
        # to match its chip, has no such width constraint.
        labels = VGroup(*[
            label(f"T{i + 1} — {t}", size=20, color=c) for i, (t, c) in enumerate([
                ("upstream gap", AMBER), ("informative outlier", AMBER),
                ("worked as intended", GREEN), ("clean structural pass", GREEN),
                ("real, redirecting flaw", RED),
            ])
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        labels.move_to([0, -0.55, 0])
        self.play(FadeIn(labels), run_time=0.6)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B10_ThreeFilesSynced   (target ~61s)   [renumbered from old B06]
#  Fix #1: one blind spot, three files, all widened in sync. Fix #2: a
#  named, deliberately incomplete rule.
# ─────────────────────────────────────────────────────────────────────────────
class B10_ThreeFilesSynced(Scene):
    TARGET = 45.12  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        head = label("THE SAME BLIND SPOT, THREE TIMES", size=27,
                    weight="BOLD", color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        files = ["claims.py", "consistency.py", "verification.py"]
        rows = VGroup()
        for nm in files:
            fname = mono(nm, size=26, color=INK)
            line = mono(r"$[\d,]+(?:\.\d+)?|…%|…x|…bps", size=22, color=GHOST)
            row = VGroup(fname, line).arrange(RIGHT, buff=0.5)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to([0, 1.4, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows],
                              lag_ratio=0.3), run_time=1.4)
        self.wait(1.0)

        self.play(*[rows[i][1].animate.set_color(ACC) for i in range(3)],
                  run_time=0.6)
        self.wait(0.8)
        self.play(*[rows[i][1].animate.scale(1.12) for i in range(3)],
                  run_time=0.7)
        self.wait(1.2)

        chip = label_chip("ONE BLIND SPOT. THREE COPIES. ALL FIXED TOGETHER.",
                          ACC, size=22)
        chip.move_to([0, -1.4, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(head, rows, chip)), run_time=0.6)

        # ── the harder decision ──────────────────────────────────────────────
        node_t = label("WHICH CONCEPT DID\nTHIS NUMBER COME FROM?", size=25,
                      weight="BOLD", color=GHOST, line_spacing=0.7)
        node = DashedVMobject(auto_box(node_t, h_pad=0.5, v_pad=0.4, color=GHOST),
                             num_dashes=36, color=GHOST)
        node_group = VGroup(node, node_t).move_to([0, 2.0, 0])
        self.play(FadeIn(node_group), run_time=0.6)
        self.wait(1.6)

        rule = mono("only-one-side cited  =>  not a contradiction alone",
                   size=24, color=INK)
        rule_box = boxed(rule, color=INK).move_to([0, 0.2, 0])
        self.play(FadeIn(rule_box), run_time=0.6)
        self.wait(2.0)

        fixes = checked("FIXES: one agent wasn't asked", size=22, color=ACC)
        fixes.move_to([-2.9, -1.6, 0])
        # checked()'s symbol is composed in Manim's default font (a real glyph),
        # never a raw Text("✕", font=DISPLAY) — Montserrat has no glyph for it.
        nofix = checked("DOES NOT FIX: two real,\nunrelated numbers", size=22,
                       color=GHOST, symbol="✕", line_spacing=0.7)
        nofix.move_to([2.9, -1.6, 0])
        self.play(FadeIn(fixes), run_time=0.5)
        self.play(FadeIn(nofix), run_time=0.5)
        self.wait(1.2)

        stamp = label("LEFT OPEN ON PURPOSE", size=22, weight="BOLD", color=ACC)
        stamp.next_to(nofix, DOWN, buff=0.28)
        self.play(FadeIn(stamp), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_ElevenToSeven   (target ~31s)   [renumbered from old B07]
#  The fix, checked against the same twelve companies, recalculated.
# ─────────────────────────────────────────────────────────────────────────────
class B11_ElevenToSeven(Scene):
    TARGET = 24.98  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("SAME 12 COMPANIES. RECALCULATED, NOT RE-RUN.", ACC,
                          size=22)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.0)

        x0, sc = -1.0, 2.2 / 11.0
        bar = Rectangle(width=1.2, height=11 * sc, color=ACC, stroke_width=2,
                       fill_opacity=0.75, fill_color=ACC)
        bar.move_to([x0, -0.2, 0], aligned_edge=DOWN)
        old_lbl = label("OLD RULE: 11", size=24, weight="BOLD", color=ACC)
        old_lbl.next_to(bar, UP, buff=0.22)
        base = Line([-4.5, -1.3, 0], [4.5, -1.3, 0], color=GHOST, stroke_width=1.5)

        self.play(Create(base), run_time=0.3)
        self.play(GrowFromEdge(bar, DOWN), FadeIn(old_lbl), run_time=0.7)
        self.wait(1.2)

        new_h = 7 * sc
        self.play(bar.animate.stretch_to_fit_height(new_h).move_to(
            [x0, -1.3 + new_h / 2, 0]),
            old_lbl.animate.next_to(bar, UP, buff=0.22),
            run_time=0.9)
        new_lbl = label("NEW RULE: 7", size=24, weight="BOLD", color=ACC)
        new_lbl.next_to(bar, RIGHT, buff=0.5).align_to(bar, UP)
        self.play(FadeIn(new_lbl), run_time=0.4)
        self.wait(1.2)

        tiles = VGroup(*[Rectangle(width=0.7, height=0.5, color=ACC,
                                   stroke_width=2, fill_opacity=0.28,
                                   fill_color=ACC) for _ in range(4)])
        tiles.arrange(RIGHT, buff=0.22).move_to([2.6, -1.7, 0])
        self.play(FadeIn(tiles), run_time=0.5)
        self.wait(0.6)
        self.play(*[t.animate.set_stroke(color=GHOST, width=2).set_fill(
            color=GHOST, opacity=0.1) for t in tiles], run_time=0.7)
        flip_cap = label("one agent hadn't quantified\nanything — false alarm, gone",
                        size=20, color=SOFT, line_spacing=0.7)
        flip_cap.next_to(tiles, DOWN, buff=0.24)
        self.play(FadeIn(flip_cap), run_time=0.4)
        self.wait(1.6)

        cap = label("still flagged — real numbers, different concepts",
                   size=24, weight="BOLD", color=INK)
        cap.move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B12_TwoChipsHonestLedger   (target ~34s)   [renumbered from old B08]
#  Two separate questions, two separate answers.
# ─────────────────────────────────────────────────────────────────────────────
class B12_TwoChipsHonestLedger(Scene):
    TARGET = 27.73  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        head = label("TWO SEPARATE QUESTIONS,\nTWO SEPARATE ANSWERS", size=26,
                    weight="BOLD", color=SOFT, line_spacing=0.7)
        head.move_to([0, 3.15, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(1.2)

        # ── infrastructure: solid ─────────────────────────────────────────────
        infra_outline = Rectangle(width=4.6, height=2.7, color=INK,
                                  stroke_width=3)
        infra_outline.move_to([-3.15, 0.1, 0])
        infra_lbl = label("INFRASTRUCTURE", size=24, weight="BOLD", color=INK)
        infra_lbl.next_to(infra_outline, UP, buff=0.2)
        self.play(Create(infra_outline), FadeIn(infra_lbl), run_time=0.6)
        self.play(infra_outline.animate.set_fill(color=GREEN, opacity=0.85)
                  .set_stroke(color=GREEN), run_time=0.7)
        infra_list = VGroup(*[
            label(t, size=18, color="#FFFFFF") for t in
            ("real filings", "real independent reasoning",
             "full audit trail", "24/24 guardrail held")
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        infra_list.move_to(infra_outline)
        self.play(FadeIn(infra_list), run_time=0.5)
        self.wait(1.6)

        # ── judgment: half-filled ────────────────────────────────────────────
        judg_outline = Rectangle(width=4.6, height=2.7, color=INK,
                                 stroke_width=3)
        judg_outline.move_to([3.15, 0.1, 0])
        judg_lbl = label("JUDGMENT", size=24, weight="BOLD", color=INK)
        judg_lbl.next_to(judg_outline, UP, buff=0.2)
        self.play(Create(judg_outline), FadeIn(judg_lbl), run_time=0.6)

        half = Rectangle(width=4.6, height=1.35, color=ACC, stroke_width=0,
                         fill_color=ACC, fill_opacity=0.85)
        half.move_to(judg_outline.get_bottom(), aligned_edge=DOWN)
        self.play(GrowFromEdge(half, DOWN), run_time=0.7)
        not_yet = label("NOT YET PROVEN", size=20, weight="BOLD", color="#FFFFFF")
        not_yet.move_to(half)
        self.play(FadeIn(not_yet), run_time=0.4)
        self.wait(1.0)

        judg_list = VGroup(*[
            label(t, size=17, color=INK) for t in
            ("mostly disjoint concepts,\nnot real contradictions",
             "one fabrication caught\nby a human, not the system")
        ]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        # Fit into the zone strictly above the "NOT YET PROVEN" fill (never
        # a fixed offset from the outline's top) so the two never overlap
        # regardless of exact text height — the same collision class as
        # the Chapter-3 fields/caption overlap, fixed the same way.
        zone_top = judg_outline.get_top()[1]
        zone_bottom = half.get_top()[1]
        zone_h = zone_top - zone_bottom
        if judg_list.height > zone_h * 0.92:
            judg_list.scale((zone_h * 0.92) / judg_list.height)
        judg_list.move_to([judg_outline.get_center()[0], (zone_top + zone_bottom) / 2, 0])
        self.play(FadeIn(judg_list), run_time=0.5)
        self.wait(2.2)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_CaughtByAHuman   (target ~28s)   [renumbered from old B09]
#  second-to-last beat, OUTRO-LAW
#  The cold-open line returns, restamped; the end-card stats land here, not
#  on the final Remotion outro (B14), which stays a clean title restate.
# ─────────────────────────────────────────────────────────────────────────────
class B13_CaughtByAHuman(Scene):
    TARGET = 19.86  # actual_duration_s (Kokoro-measured)

    def construct(self):
        self.camera.background_color = BG

        quote = serif("\"Calculated the debt-to-equity\nratio as 0.34\"",
                     size=28, color=INK, italic=True, line_spacing=0.8)
        src = mono("[SOURCE: SEC Filings]", size=20, color=SOFT)
        group = VGroup(quote, src).arrange(DOWN, buff=0.24).move_to([0, 1.9, 0])
        self.play(FadeIn(group), run_time=0.6)
        self.wait(1.2)

        stamp = label_chip("CAUGHT BY A HUMAN, NOT THE SYSTEM", ACC, size=22)
        stamp.next_to(group, DOWN, buff=0.4)
        self.play(FadeIn(stamp, scale=1.05), run_time=0.6)
        self.wait(1.2)

        told = label("told on itself, twice, in two days", size=22, color=SOFT)
        told.next_to(stamp, DOWN, buff=0.3)
        self.play(FadeIn(told), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(group, stamp, told)), run_time=0.5)

        card_lines = VGroup(
            mono("24 / 24 structural passes, 0 halts", size=22, color=INK),
            mono("contradiction flag: 11/12 -> 7/12 after the fix", size=22,
                 color=ACC),
            mono("disjoint-concept false positives still open", size=22,
                 color=SOFT),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        card_box = auto_box(card_lines, h_pad=0.5, v_pad=0.35, color=GHOST)
        card = VGroup(card_box, card_lines).move_to([0, 1.1, 0])
        self.play(Create(card_box), run_time=0.4)
        for line in card_lines:
            self.play(FadeIn(line), run_time=0.4)
            self.wait(0.5)

        source = label("source: logs/RUN_LOG.md, 2026-08-28/29", size=18,
                      color=GHOST)
        source.next_to(card, DOWN, buff=0.3)
        self.play(FadeIn(source), run_time=0.4)
        self.wait(1.0)

        closer = serif("proved the plumbing.\nnot yet the judgment.", size=30,
                       color=INK, line_spacing=0.8)
        closer.move_to([0, -2.5, 0])
        self.play(FadeIn(closer), run_time=0.6)
        hold_to(self, self.TARGET)
