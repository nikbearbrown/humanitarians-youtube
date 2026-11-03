"""scenes.py — Manim scenes for zero-for-sixteen (claude-divij, Cross-Agent Validation video 4).

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491,
plus three verdict colors carried over from the-number-that-wasnt-there's Chapter-3
scorecard convention: green #4C9A6A (worked / resolved), amber #C9932E (a real but
informative gap), red #B0473A (a real, unresolved flaw). Type: Montserrat (DISPLAY,
structural default) / EB Garamond (SERIF, editorial voice only) / PT Mono (MONO, data
+code only) — see graphics_lib.py. Boxes are sized to their actual content via
auto_box, never hand-measured.

Every scene ends with hold_to(self, TARGET) so its NATIVE duration matches the beat's
target length — compile.py then never has to stretch a short clip into visible slow
motion. TARGET constants below are the PRE-AUDIO estimated_duration_s from
beat_sheet.json — RETIME against actual Kokoro output per BUILD-PROMPT.md Step 3
before final render. Nothing in this file has been rendered yet.

Safe frame: x in [-6.4, 6.4], y in [-3.6, 3.6].

Never a raw Text("✓")/Text("✕") — Montserrat has no glyph for either and Pango
silently renders a .notdef box. Use checked() from graphics_lib, which composes the
symbol in Manim's default font with the word in DISPLAY.

B00 (cold open + title, Remotion ClaudeComposerAsk) and B15 (outro, Remotion
ClaudeTitleOutro) are not Manim scenes — see beat_sheet.json. B01 through B14 below
are the 14 GRAPHIC beats, one class each, named to match beat_sheet.json's
shot.manim.scene_class exactly.

RUNTIME CUT PASS (2026-09-08, same day as initial authoring): applied the source
script's own "if the runtime needs to shrink (to ~6:00)" guidance. B03_OneFetchNotTwo
drops its lookup_cik/fetch_company_facts timing readout (cut item 2); B06_DedupCollapse
drops its second movement, the _latest_value cross-producer-import case (cut item 1);
B11_RegexTruncation drops its stale-ledger footnote card (cut item 3). Every other
GRAPHIC scene's TARGET was shortened to match beat_sheet.json's trimmed narration, but
none needed its choreography changed — each scene's actual played duration was already
well under its new TARGET, so hold_to's own padding absorbs the difference. B12/B13
(Chapter 7) are untouched, per the script's explicit "never cut chapter 7" instruction.
"""
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"

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
    return label_chip(text, SOFT, size=size)


def num_chip(text, color=INK, size=26):
    t = mono(text, size=size, color=color)
    b = auto_box(t, h_pad=0.22, v_pad=0.16, color=color)
    return VGroup(b, t)


def status_chip(text, status, size=18):
    """A ledger-row status chip, colored by the self_report.py status vocabulary."""
    color = {"OPEN": RED, "UNVERIFIED": AMBER, "RESOLVED": GREEN, "BY_DESIGN": SOFT}[status]
    return label_chip(text, color, size=size)


def counter_line(text, size=26, color=INK):
    return mono(text, size=size, color=color)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_RecapAndGap   (target ~32s)
#  Reused, simplified two-column recap (script's own instruction: "no new
#  build"), then the prior-limitation chip and the section 3.4 verbatim quote.
# ─────────────────────────────────────────────────────────────────────────────
class B01_RecapAndGap(Scene):
    TARGET = 31.0  # retimed to actual Kokoro duration (was 29.01)

    def construct(self):
        self.camera.background_color = BG

        head = label("WHAT ALREADY EXISTED", size=28, weight="BOLD", color=SOFT)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        left_t = label("TWO AGENTS -> SAME\nCOMPANY -> FLAG\nMISMATCHES", size=22,
                       color=INK, line_spacing=0.8)
        left = boxed(left_t, color=ACC).move_to([-3.3, 1.2, 0])
        right_t = label("ACCOUNTABILITY LAYER\nAPPEND-ONLY, ONE RECORD\nPER AGENT PER ATTEMPT",
                        size=22, color=INK, line_spacing=0.8)
        right = boxed(right_t, color=SOFT).move_to([3.3, 1.2, 0])

        self.play(FadeIn(left), run_time=0.5)
        self.wait(1.4)
        self.play(FadeIn(right), run_time=0.5)
        self.wait(1.8)

        self.play(FadeOut(VGroup(left, right, head)), run_time=0.5)

        limit = label_chip("7 / 12 OVER-FLAGGED\nREASON SUSPECTED, NEVER MEASURED", ACC, size=22)
        limit.move_to([0, 2.1, 0])
        self.play(FadeIn(limit), run_time=0.5)
        self.wait(1.8)

        quote = serif("\"web/static/index.html and app.js are, as of\nthis document, completely unmodified for\nCross-Agent Validation.\"",
                     size=24, color=INK, italic=True, line_spacing=0.8)
        qsrc = mono("cross-agent-validation-status.md §3.4", size=16, color=SOFT)
        qgroup = VGroup(quote, qsrc).arrange(DOWN, buff=0.22).move_to([0, -0.6, 0])
        self.play(FadeIn(qgroup), run_time=0.6)
        self.wait(2.4)

        self.play(FadeOut(VGroup(limit, qgroup)), run_time=0.5)

        # Split into two chips spread near the top/bottom of the safe frame
        # (rather than one small chip parked dead-center) -- this composition
        # is on screen for the majority of the beat's hold, so it needs to
        # use the frame's full height on its own, not just its width.
        sessions_top = label_chip("FOUR SESSIONS", ACC, size=72)
        sessions_bottom = label_chip("THIS PERIOD", ACC, size=72)
        sessions_top.move_to([0, 2.8, 0])
        sessions_bottom.move_to([0, -2.8, 0])
        sessions = VGroup(sessions_top, sessions_bottom)
        self.play(FadeIn(sessions, scale=1.05), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_LedgerTable   (target ~42s)   Figure 2
#  self_report.py's ledger, live test-count discovery, generated caveat,
#  the null vs false distinction.
# ─────────────────────────────────────────────────────────────────────────────
class B02_LedgerTable(Scene):
    TARGET = 32.51  # retimed to actual Kokoro duration (was 32.3)

    def construct(self):
        self.camera.background_color = BG

        head = label("self_report.py — A SINGLE SOURCE OF TRUTH", size=26,
                    weight="BOLD", color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        rows = VGroup()
        for name, status in [("disjoint-concepts", "OPEN"), ("fabrication-not-caught", "OPEN"),
                              ("session-scope-leak", "OPEN"), ("audit-criticals", "OPEN"),
                              ("retry-halt-unproven", "UNVERIFIED"), ("claim-verification", "RESOLVED")]:
            nm = mono(name, size=17, color=INK)
            chip = status_chip(status, status, size=13)
            row = VGroup(nm, chip).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, buff=0.16, aligned_edge=LEFT).move_to([-1.0, 1.5, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in rows],
                              lag_ratio=0.25), run_time=1.8)
        self.wait(1.4)

        live = label_chip("TEST COUNT: LIVE UNITTEST\nDISCOVERY, NOT A NUMBER IN A FILE",
                          ACC, size=18)
        live.move_to([0, -0.9, 0])
        self.play(FadeIn(live), run_time=0.5)
        self.wait(1.2)

        stale = mono("\"143 TESTS\"  (×3 in README)", size=22, color=SOFT)
        stale.move_to([0, -1.9, 0])
        strike = Line(stale.get_left(), stale.get_right(), color=RED, stroke_width=3)
        self.play(FadeIn(stale), run_time=0.4)
        self.play(Create(strike), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(rows, live, stale, strike)), run_time=0.5)

        # ── generated caveat -> button ───────────────────────────────────────
        ledger_row = boxed(mono("disjoint-concepts — OPEN", size=20, color=INK),
                          color=RED).move_to([-2.8, 1.6, 0])
        caveat = label("\"this comparator over-flags\"", size=22, weight="BOLD",
                       color=ACC).move_to([1.6, 1.6, 0])
        arrow = Arrow(ledger_row.get_right(), caveat.get_left(), buff=0.15,
                     color=SOFT, stroke_width=2.5)
        button = boxed(label("RUN COMPARISON", size=20, weight="BOLD", color="#FFFFFF"),
                      color=INK, h_pad=0.4, v_pad=0.25)
        button[0].set_fill(INK, opacity=1)
        button.next_to(caveat, DOWN, buff=0.5)

        self.play(FadeIn(ledger_row), run_time=0.4)
        self.play(Create(arrow), FadeIn(caveat), run_time=0.6)
        self.wait(1.0)
        self.play(FadeIn(button), run_time=0.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(ledger_row, arrow, caveat, button)), run_time=0.5)

        null_chip = VGroup(
            mono("null", size=28, color=SOFT),
            label("NO COMPARISON WAS POSSIBLE", size=16, color=SOFT),
        ).arrange(DOWN, buff=0.2)
        false_chip = VGroup(
            mono("false", size=28, color=INK),
            label("CHECKED. FOUND NOTHING.", size=16, color=INK),
        ).arrange(DOWN, buff=0.2)
        pair = VGroup(boxed(null_chip, color=GHOST), boxed(false_chip, color=INK))
        pair.arrange(RIGHT, buff=0.3).move_to([0, -0.4, 0])
        self.play(FadeIn(pair[0]), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(pair[1]), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_OneFetchNotTwo   (target ~38s)   Figure 3
#  The wrong assumed two-fetch design struck through; the real four-band
#  layout and the retry path, rendered live. CUT (cut-to-6:00 guidance, item
#  2): the lookup_cik/fetch_company_facts millisecond timings from the
#  original draft are dropped — see SOURCES.md and PEDAGOGY.md.
# ─────────────────────────────────────────────────────────────────────────────
class B03_OneFetchNotTwo(Scene):
    TARGET = 30.68  # retimed to actual Kokoro duration (was 30.7)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("CHECKING THE CRITIQUE BEFORE BUILDING FOR IT", ACC, size=20)
        chip.move_to([0, 3.2, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.0)

        # ── wrong assumed design ─────────────────────────────────────────────
        colA = boxed(label("AGENT A\n\nEDGAR fetch", size=20, color=INK, line_spacing=0.7),
                    color=GHOST).move_to([-2.2, 1.2, 0])
        colB = boxed(label("AGENT B\n\nEDGAR fetch", size=20, color=INK, line_spacing=0.7),
                    color=GHOST).move_to([2.2, 1.2, 0])
        wrong = VGroup(colA, colB)
        self.play(FadeIn(wrong), run_time=0.6)
        self.wait(1.0)
        strike = Line(wrong.get_corner(DL), wrong.get_corner(UR), color=RED, stroke_width=4)
        self.play(Create(strike), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(wrong, strike)), run_time=0.5)

        # ── the real four-band layout ────────────────────────────────────────
        bands = VGroup(*[
            boxed(label(t, size=16, color=INK), color=SOFT, h_pad=0.25, v_pad=0.18)
            for t in ("SETUP", "SHARED\nSPINE", "TWO\nCOLUMNS", "VERDICT")
        ])
        bands.arrange(RIGHT, buff=0.35).move_to([0, 1.6, 0])
        self.play(LaggedStart(*[FadeIn(b) for b in bands], lag_ratio=0.25), run_time=1.4)
        self.wait(0.8)

        band2_lbl = label("ONE PAYLOAD, REUSED\nBY BOTH PRODUCERS", size=16, color=ACC,
                         line_spacing=0.7).next_to(bands[1], DOWN, buff=0.3)
        self.play(FadeIn(band2_lbl), run_time=0.5)
        self.wait(1.4)

        retry = VGroup(
            mono("attempt 1", size=18, color=SOFT),
            mono("parse fail", size=18, color=RED),
            mono("attempt 2", size=18, color=SOFT),
            mono("HALT", size=18, weight="BOLD", color=RED),
        ).arrange(RIGHT, buff=0.5).move_to([0, -0.8, 0])
        self.play(LaggedStart(*[FadeIn(r) for r in retry], lag_ratio=0.3), run_time=1.2)
        self.wait(1.2)

        cap = label("rendered in the HTTP layer, real sequence numbers",
                   size=18, color=SOFT).move_to([0, -2.0, 0])
        self.play(FadeIn(cap), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_ProvenanceRows   (target ~27s)   Figure 4
#  Two provenance rows: a real reconciled figure, and the fabrication.
# ─────────────────────────────────────────────────────────────────────────────
class B04_ProvenanceRows(Scene):
    TARGET = 21.48  # retimed to actual Kokoro duration (was 21.42)

    def construct(self):
        self.camera.background_color = BG

        head = label("EVERY CITED NUMBER, TRACED BACK", size=26, weight="BOLD",
                    color=SOFT).move_to([0, 3.1, 0])
        self.play(FadeIn(head), run_time=0.4)

        row1_l = mono("$383.266 billion", size=26, color=INK)
        row1_r = mono("Assets: 383266000000.0", size=20, color=SOFT)
        ok = Text("✓", font_size=32, color=GREEN)
        row1 = VGroup(row1_l, ok, row1_r).arrange(RIGHT, buff=0.35)
        row1.move_to([0, 1.4, 0])
        self.play(FadeIn(row1), run_time=0.6)
        self.wait(1.6)

        row2_l = mono("0.34", size=26, color=INK)
        row2_r = label("NOT PRESENT IN INPUT", size=20, color=RED)
        # A drawn triangle + "!" rather than the ⚠ emoji glyph — Manim's default
        # font has no glyph for U+26A0 either, and silently renders the raw
        # codepoint digits instead (the same .notdef failure mode graphics_lib's
        # checked() works around for ✓/✕; caught in visual QC on B04's frames).
        warn_tri = Triangle(color=AMBER, fill_color=AMBER, fill_opacity=1,
                             stroke_width=0).scale(0.22)
        warn_bang = label("!", size=20, weight="BOLD", color=BG).move_to(
            warn_tri.get_center() + DOWN * 0.03)
        warn = VGroup(warn_tri, warn_bang)
        row2 = VGroup(row2_l, warn, row2_r).arrange(RIGHT, buff=0.35)
        row2.move_to([0, 0.0, 0])
        self.play(FadeIn(row2), run_time=0.6)
        self.wait(1.4)

        stamp = label_chip("FABRICATION", RED, size=28)
        stamp.next_to(row2, DOWN, buff=0.5)
        self.play(FadeIn(stamp, scale=1.1), run_time=0.5)
        self.wait(1.6)

        cap = label("before this, finding it required reading\na raw log by hand", size=20,
                   color=SOFT, line_spacing=0.7).move_to([0, -2.6, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_SnapshotDiff   (target ~23s)   Figure 5
#  16 flat modules, parser.py's stdlib shadow, 8 move-steps, byte-identical
#  snapshot.
# ─────────────────────────────────────────────────────────────────────────────
class B05_SnapshotDiff(Scene):
    TARGET = 21.74  # retimed to actual Kokoro duration (was 21.55)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("16 MODULES, FLAT AT THE ROOT", ACC, size=22)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.0)

        parser = mono("parser.py", size=28, color=RED)
        warn = label("SHADOWS THE STANDARD LIBRARY", size=16, color=RED)
        pgroup = VGroup(parser, warn).arrange(DOWN, buff=0.15).move_to([0, 1.9, 0])
        self.play(FadeIn(pgroup), run_time=0.5)
        self.wait(1.4)

        self.play(FadeOut(VGroup(chip, pgroup)), run_time=0.4)

        layers = VGroup(*[
            boxed(mono(t, size=21, color=INK), color=SOFT, h_pad=0.26, v_pad=0.17)
            for t in ("core", "adapters", "pipeline", "datasources", "producers", "validation")
        ]).arrange(DOWN, buff=0.28).move_to([-3.6, 0.5, 0])
        self.play(LaggedStart(*[FadeIn(l) for l in layers], lag_ratio=0.15), run_time=1.4)
        self.wait(0.8)

        steps = VGroup(*[num_chip(str(i + 1), color=GREEN, size=22) for i in range(8)])
        steps.arrange(RIGHT, buff=0.22).move_to([2.2, 2.9, 0])
        for s in steps:
            self.play(FadeIn(s), run_time=0.2)
        self.wait(1.0)

        panel = boxed(label("ROUTE TABLE + 9 CALLS\nBEFORE vs AFTER", size=21, color=INK,
                           line_spacing=0.7), color=INK).move_to([2.2, 0.3, 0])
        self.play(FadeIn(panel), run_time=0.5)
        self.wait(1.0)

        result = label("0 DIFFERENCES", size=40, weight="BOLD", color=GREEN)
        result.move_to([2.2, -2.4, 0])
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_DedupCollapse   (target ~18s)   Figure 6
#  The regex duplicated three times, collapsing into one. CUT (cut-to-6:00
#  guidance, item 1): the second movement — the _latest_value
#  cross-producer-import case — is dropped entirely, per the script's own
#  explicit instruction. See SOURCES.md and PEDAGOGY.md.
# ─────────────────────────────────────────────────────────────────────────────
class B06_DedupCollapse(Scene):
    TARGET = 15.06  # retimed to actual Kokoro duration (was 15.19)

    def construct(self):
        self.camera.background_color = BG

        head = label("THREE DUPLICATIONS, EACH A FAILURE\nMODE WAITING TO HAPPEN", size=27,
                    weight="BOLD", color=SOFT, line_spacing=0.75).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.5)

        files = ["claims.py", "consistency.py", "verification.py"]
        rows = VGroup()
        for nm in files:
            fname = mono(nm, size=22, color=INK)
            line = mono(r"QUANTITATIVE_RE", size=18, color=GHOST)
            note = label("keep in sync by hand", size=13, color=GHOST)
            row = VGroup(fname, line, note).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([0, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows],
                              lag_ratio=0.3), run_time=1.4)
        self.wait(1.2)

        shared = boxed(mono("QUANTITATIVE_RE  (shared)", size=34, color=INK), color=ACC)
        shared.move_to([0, 1.0, 0])
        self.play(Transform(rows, shared), run_time=0.9)
        self.wait(1.0)

        cap1 = label("a drifted copy wouldn't error —\nit would quietly report an unverified claim",
                    size=29, color=INK, line_spacing=0.8).move_to([0, -2.5, 0])
        self.play(FadeIn(cap1), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B07_LayeringViolations   (target ~24s)   Figure 7
#  A passing architecture test, stress-tested by three deliberate violations.
# ─────────────────────────────────────────────────────────────────────────────
class B07_LayeringViolations(Scene):
    TARGET = 17.96  # retimed to actual Kokoro duration (was 18.5)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("+47 TESTS — test_layering.py READS THE\nIMPORTS AS A SYNTAX TREE",
                          ACC, size=18)
        chip.move_to([0, 3.0, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(0.8)

        cap = label("a passing architecture test is worthless\nif it can't fail", size=20,
                   weight="BOLD", color=INK, line_spacing=0.7).move_to([0, 1.9, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.0)

        fails = VGroup()
        for i, (f, ln) in enumerate([("web/server.py", 214), ("producers/earnings.py", 58),
                                      ("validation/claims.py", 33)]):
            arrow = Arrow([-2.5, 0, 0], [2.5, 0, 0], color=RED, stroke_width=2)
            label_f = mono(f"FAIL — {f}:{ln}", size=17, color=RED)
            row = VGroup(arrow, label_f).arrange(DOWN, buff=0.1)
            fails.add(row)
        fails.arrange(DOWN, buff=0.32).move_to([0, -0.6, 0])
        for f in fails:
            self.play(FadeIn(f), run_time=0.4)
            self.wait(0.4)
        self.wait(0.8)

        self.play(*[f[0].animate.set_color(GREEN) for f in fails],
                  *[f[1].animate.set_color(GREEN) for f in fails], run_time=0.6)
        stamp = label_chip("RESTORED", GREEN, size=24)
        stamp.move_to([0, -2.9, 0])
        self.play(FadeIn(stamp, scale=1.05), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_CorpusBuckets   (target ~21s)   Figure 8
#  31 stored runs sorting into labeled outcome buckets; genuine_conflict
#  stays empty.
# ─────────────────────────────────────────────────────────────────────────────
class B08_CorpusBuckets(Scene):
    TARGET = 19.05  # retimed to actual Kokoro duration (was 19.05)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("\"7 OF 12\" WAS PROSE. THIS IS A FIXTURE.", ACC, size=27)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(0.8)

        tiles = VGroup(*[Rectangle(width=0.32, height=0.22, color=GHOST, stroke_width=1.4,
                                   fill_opacity=0.15, fill_color=GHOST) for _ in range(31)])
        tiles.arrange_in_grid(rows=4, cols=8, buff=0.08).move_to([0, 1.3, 0])
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.03), run_time=1.0)
        self.wait(0.6)

        buckets = VGroup(
            boxed(label("disjoint\nconcepts", size=16, color=INK, line_spacing=0.6),
                 color=AMBER, h_pad=0.3, v_pad=0.2),
            boxed(label("genuine\nconflict", size=16, color=INK, line_spacing=0.6),
                 color=RED, h_pad=0.3, v_pad=0.2),
            boxed(label("other", size=16, color=INK), color=SOFT, h_pad=0.3, v_pad=0.2),
        ).arrange(RIGHT, buff=1.05).move_to([0, -0.9, 0])
        self.play(FadeIn(buckets), run_time=0.5)
        self.wait(0.6)

        disjoint_tiles = tiles[:16]
        other_tiles = tiles[16:]
        # Land below each bucket's own box, not on its center -- moving to the
        # box's center stacked every tile directly on top of its label text
        # (visible as a stray square sitting on "concepts"/"other" in QC).
        disjoint_landing = buckets[0].get_bottom() + DOWN * 0.35
        other_landing = buckets[2].get_bottom() + DOWN * 0.35
        self.play(*[t.animate.move_to(disjoint_landing).scale(0.6).set_fill(AMBER, opacity=0.5)
                    for t in disjoint_tiles],
                  *[t.animate.move_to(other_landing).scale(0.6).set_fill(SOFT, opacity=0.3)
                    for t in other_tiles],
                  run_time=1.2)
        self.wait(0.6)

        pulse = SurroundingRectangle(buckets[1], color=RED, buff=0.05, stroke_width=3)
        self.play(Create(pulse), run_time=0.4)
        self.play(FadeOut(pulse), run_time=0.4)

        counts = VGroup(
            mono("16 / 31  DISJOINT-CONCEPT", size=27, color=AMBER),
            mono("0 / 31  GENUINE CONFLICT", size=27, color=RED),
        ).arrange(DOWN, buff=0.22).move_to([0, -2.9, 0])
        self.play(FadeIn(counts), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_DisjointVocabularies   (target ~30s)   Figure 9
#  Two concept vocabularies with an empty intersection — the structural
#  reason no amount of tuning fixes the flag.
# ─────────────────────────────────────────────────────────────────────────────
class B09_DisjointVocabularies(Scene):
    TARGET = 27.18  # retimed to actual Kokoro duration (was 27.01)

    def construct(self):
        self.camera.background_color = BG

        head = label("EVERY FLAGGED RUN, THE SAME PAIRING", size=25, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.4)

        left = VGroup(
            label("PRODUCER A", size=18, weight="BOLD", color=SOFT),
            mono("Assets", size=20, color=INK), mono("Revenues", size=20, color=INK),
            mono("NetIncomeLoss", size=20, color=INK),
        ).arrange(DOWN, buff=0.18).move_to([-3.4, 1.0, 0])
        right = VGroup(
            label("PRODUCER B", size=18, weight="BOLD", color=SOFT),
            mono("EarningsPerShare", size=20, color=INK),
            mono("OperatingIncome", size=20, color=INK),
        ).arrange(DOWN, buff=0.18).move_to([3.4, 1.0, 0])
        self.play(FadeIn(left), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(right), run_time=0.5)
        self.wait(1.0)

        gap = DashedVMobject(Rectangle(width=2.4, height=1.6, color=RED, stroke_width=2.5),
                             num_dashes=24, color=RED)
        gap.move_to([0, 1.0, 0])
        gap_lbl = label("EMPTY\nINTERSECTION", size=18, weight="BOLD", color=RED,
                       line_spacing=0.7).move_to(gap)
        self.play(Create(gap), FadeIn(gap_lbl), run_time=0.7)
        self.wait(1.4)

        quote = serif("\"…deliberately disjoint…\"", size=24, italic=True, color=INK)
        qsrc = mono("producers/earnings.py", size=15, color=SOFT)
        qgroup = VGroup(quote, qsrc).arrange(DOWN, buff=0.15).move_to([0, -0.7, 0])
        self.play(FadeIn(qgroup), run_time=0.5)
        self.wait(1.6)

        cap = label("you cannot detect disagreement between two\nwitnesses asked different questions", size=19,
                   weight="BOLD", color=INK, line_spacing=0.7).move_to([0, -1.9, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.6)

        chips = VGroup(
            label_chip("FIX IS UPSTREAM — NOT THIS\nSESSION'S JOB", SOFT, size=16),
            label_chip("+8 TESTS", ACC, size=16),
        ).arrange(RIGHT, buff=0.4).move_to([0, -3.0, 0])
        self.play(FadeIn(chips), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B10_TwoFixesOneRecord   (target ~32s)   Figure 10
#  The record f4a4c782, reprised from the cold open — two same-day fixes
#  converge on it and suppress the one confirmed catch.
# ─────────────────────────────────────────────────────────────────────────────
class B10_TwoFixesOneRecord(Scene):
    TARGET = 22.61  # retimed to actual Kokoro duration (was 23.02)

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("REPLAY THE ONE CONFIRMED CATCH", ACC, size=22)
        chip.move_to([0, 3.1, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.0)

        rec_id = mono("f4a4c782", size=26, color=INK)
        rec_box = boxed(rec_id, color=INK).move_to([0, 1.6, 0])
        old_stamp = label_chip("TRUE POSITIVE", GREEN, size=18).next_to(rec_box, DOWN, buff=0.2)
        self.play(FadeIn(rec_box), run_time=0.5)
        self.play(FadeIn(old_stamp), run_time=0.4)
        self.wait(1.4)

        fixA = label_chip("REGEX WIDENED", SOFT, size=16).move_to([-2.6, 0.0, 0])
        fixB = label_chip("BOTH-SIDES-NON-EMPTY\nGATE ADDED", SOFT, size=16).move_to([2.6, 0.0, 0])
        date = label("same day, August 2026", size=15, color=GHOST).move_to([0, 0.5, 0])
        self.play(FadeIn(date), run_time=0.3)
        self.play(FadeIn(fixA), FadeIn(fixB), run_time=0.5)
        self.wait(1.0)

        lineA = Line(fixA.get_top(), rec_box.get_bottom() + LEFT * 0.4, color=SOFT, stroke_width=2)
        lineB = Line(fixB.get_top(), rec_box.get_bottom() + RIGHT * 0.4, color=SOFT, stroke_width=2)
        self.play(Create(lineA), Create(lineB), run_time=0.7)
        self.wait(0.8)

        self.play(rec_box[0].animate.set_stroke(color=GHOST).set_fill(GHOST, opacity=0.3),
                  rec_id.animate.set_color(GHOST),
                  FadeOut(old_stamp), run_time=0.7)
        new_stamp = label_chip("SUPPRESSED TODAY", RED, size=20).next_to(rec_box, DOWN, buff=0.2)
        self.play(FadeIn(new_stamp, scale=1.1), run_time=0.5)
        self.wait(1.4)

        cap = label("neither fix is wrong on its own", size=20, weight="BOLD",
                   color=INK).move_to([0, -2.6, 0])
        self.play(FadeIn(cap), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_RegexTruncation   (target ~24s)   Figure 11
#  A comma-grouped number truncates to its last digit group. CUT (cut-to-6:00
#  guidance, item 3): the stale-ledger footnote (http-no-model-override) from
#  the original draft is dropped entirely — still logged in SOURCES.md, only
#  cut from the video. See PEDAGOGY.md.
# ─────────────────────────────────────────────────────────────────────────────
class B11_RegexTruncation(Scene):
    TARGET = 20.46  # retimed to actual Kokoro duration (was 20.46)

    def construct(self):
        self.camera.background_color = BG

        head = label("A REAL EXTRACTION BUG", size=32, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.4)

        big = mono("13,971,000,000.0", size=68, color=INK).move_to([0, 2.0, 0])
        self.play(FadeIn(big), run_time=0.5)
        self.wait(1.4)

        # boundary sweep: grey out everything but the last group
        discard = mono("13,971,000,", size=68, color=INK).move_to(big, aligned_edge=LEFT)
        keep = mono("000.0", size=68, color=RED)
        keep.next_to(discard, RIGHT, buff=0.0)
        self.remove(big)
        self.add(discard, keep)
        self.play(discard.animate.set_opacity(0.2), run_time=0.9)
        self.wait(1.2)

        result = label("extracted as:", size=25, color=SOFT).move_to([0, 0.2, 0])
        self.play(FadeIn(result), run_time=0.4)
        result_val = mono("\"000.0\"", size=40, weight="BOLD", color=RED).move_to([0, -0.8, 0])
        self.play(FadeIn(result_val), run_time=0.5)
        self.wait(1.4)

        chip = label_chip("BOTH OPEN. NEITHER FIXED.", RED, size=27)
        chip.move_to([0, -2.9, 0])
        self.play(FadeIn(chip), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B12_TrueNowList   (target ~41s)
#  Chapter 7, first half — the script's own direction: "List one, building
#  line by line."
# ─────────────────────────────────────────────────────────────────────────────
class B12_TrueNowList(Scene):
    TARGET = 33.13  # retimed to actual Kokoro duration (was 33.26)

    def construct(self):
        self.camera.background_color = BG

        head = label("TRUE NOW THAT WASN'T", size=28, weight="BOLD",
                    color=SOFT).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.6)

        lines = VGroup(*[
            checked(t, size=24, color=INK) for t in [
                "interface calls the comparison route",
                "one-fetch, two-lenses design rendered honestly",
                "retry path visible outside the test suite",
                "a fabricated number is findable without a raw log",
                "code sits in enforced layers, enforcement can fail",
                "over-flagging is now a versioned corpus + 8 tests",
                "224 tests, up from 169, green at every step",
            ]
        ]).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([0, -0.5, 0])
        if lines.width > 12.0:
            lines.scale(12.0 / lines.width)
        lines.move_to([0, -0.5, 0])

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.08), run_time=0.35)
            self.wait(0.25)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_StillNotTrueAndUncommitted   (target ~79s)   Figure 12
#  Chapter 7, second half — the script's own direction: "List two, in
#  warning color, held on screen. Do not clear it." Then the uncommitted
#  state: git log and the file count. The reel's longest, densest beat by
#  design — never trim this per the script's own production notes.
# ─────────────────────────────────────────────────────────────────────────────
class B13_StillNotTrueAndUncommitted(Scene):
    TARGET = 60.27  # retimed to actual Kokoro duration (was 60.39)

    def construct(self):
        self.camera.background_color = BG

        head = label("STILL NOT TRUE", size=28, weight="BOLD",
                    color=RED).move_to([0, 3.25, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.4)

        items = [
            "zero tests — compare route, trace module, all JS",
            "no UI work exercised against a real model",
            "retry / halt still only proven against mock failures",
            "over-flagging not fixed",
            "suppressed true positive unresolved — needs a human call",
            "regex bug still corrupting a real figure",
            "14 ledger entries, 12 open/unverified, 1 critical — up from 11",
        ]
        lines = VGroup(*[label(t, size=16, color=INK) for t in items])
        lines.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        if lines.width > 11.0:
            lines.scale(11.0 / lines.width)
        lines.move_to([0, 1.5, 0])

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.06), run_time=0.3)
            self.wait(0.18)
        self.wait(0.6)

        # the list holds, uncleared, while the uncommitted-state reveal builds beneath it
        git_panel = boxed(mono("c53746a", size=22, color=INK), color=SOFT,
                         h_pad=0.35, v_pad=0.22).move_to([-2.4, -2.0, 0])
        git_lbl = label("last commit", size=14, color=SOFT).next_to(git_panel, UP, buff=0.1)
        self.play(FadeIn(git_panel), FadeIn(git_lbl), run_time=0.5)
        self.wait(0.8)

        counter = mono("56", size=44, weight="BOLD", color=RED).move_to([2.4, -1.9, 0])
        counter_lbl = label("CHANGED OR NEW FILES", size=14, color=SOFT).next_to(
            counter, DOWN, buff=0.15)
        self.play(FadeIn(counter, scale=1.1), FadeIn(counter_lbl), run_time=0.6)
        self.wait(1.2)

        cap = label("named after the previous period's check —\nstill true, and now bigger", size=17,
                   weight="BOLD", color=INK, line_spacing=0.7).move_to([0, -3.15, 0])
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B14_SixteenZeroReprise   (target ~25s)   Figure 1 reprise + END CARD
#  second-to-last beat, OUTRO-LAW: the dense factual callouts land here,
#  never on the truly final Remotion outro (B15).
# ─────────────────────────────────────────────────────────────────────────────
class B14_SixteenZeroReprise(Scene):
    TARGET = 18.35  # retimed to actual Kokoro duration (was 17.98)

    def construct(self):
        self.camera.background_color = BG

        closer = serif("the smallest true claim I can make\nabout this week", size=26,
                      color=INK, line_spacing=0.8).move_to([0, 3.0, 0])
        self.play(FadeIn(closer), run_time=0.5)
        self.wait(1.0)

        flagged = label("16 FLAGGED", size=40, weight="BOLD", color=ACC)
        conflicts = label("0 GENUINE CONFLICTS", size=32, weight="BOLD", color=INK)
        counter = VGroup(flagged, conflicts).arrange(DOWN, buff=0.22).move_to([0, 1.2, 0])
        self.play(FadeIn(counter), run_time=0.6)
        self.wait(1.2)

        cursor_lbl = mono("tests/fixtures/cross_agent_real_runs_corpus.json",
                         size=14, color=SOFT).move_to([0, -0.3, 0])
        self.play(FadeIn(cursor_lbl), run_time=0.4)
        self.wait(0.8)

        self.play(FadeOut(VGroup(closer, counter, cursor_lbl)), run_time=0.5)

        bullets = [
            ("16 of 31 stored runs are false positives — 0 are genuine conflicts", INK),
            ("the one confirmed true positive would not flag today", INK),
            ("/api/compare, step_trace.py, and all JS have zero automated tests", INK),
            ("no UI work this period has run against a live model", INK),
            ("12 of 14 ledger entries open or unverified — 1 critical", INK),
            ("nothing described here is committed (last commit c53746a)", RED),
            ("corpus labels are AI-assigned and not yet human-reviewed", SOFT),
        ]
        lines = VGroup(*[mono(t, size=15, color=c) for t, c in bullets])
        lines.arrange(DOWN, buff=0.62, aligned_edge=LEFT)
        if lines.width > 11.5:
            lines.scale(11.5 / lines.width)
        lines.move_to([0, 0.0, 0])

        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.05), run_time=0.3)
            self.wait(0.15)
        hold_to(self, self.TARGET)
