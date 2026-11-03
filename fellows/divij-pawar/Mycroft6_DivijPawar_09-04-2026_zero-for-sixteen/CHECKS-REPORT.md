# CHECKS-REPORT.md — zero-for-sixteen

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **16 beats (B00–B15)**, not the ai-explainer default
of 10, and one more than the series' prior entry (the-number-that-wasnt-there,
15 beats) — see "Beat-count deviation" below.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_RecapAndGap (Manim) | Names a real prior limitation (7/12) and quotes the project's own verbatim admission — deliberately simple per the script's "no new build" instruction, still a real diagram, not narrated past |
| B02 | SHOW | B02_LedgerTable (Manim) | Names the real ledger module, real status vocabulary, and a real generated-caveat mechanism |
| B03 | SHOW | B03_OneFetchNotTwo (Manim) | Names a corrected real architecture (one fetch, two lenses, sequential) against a struck-through wrong assumption — the reel's clearest "checked before building" moment |
| B04 | SHOW | B04_ProvenanceRows (Manim) | The reel's central artifact: a real reconciled number next to the fabricated one, both rendered as actual provenance rows |
| B05 | SHOW | B05_SnapshotDiff (Manim) | Names a real architecture (six layers) and a real verification method (byte-identical snapshot), not narrated past |
| B06 | SHOW | B06_DedupCollapse (Manim) | Names two real duplication bugs, each with its own specific failure mode |
| B07 | SHOW | B07_LayeringViolations (Manim) | A real test, deliberately broken three times on screen, each producing a named failure |
| B08 | SHOW | B08_CorpusBuckets (Manim) | 31 real stored runs, sorted into real outcome buckets — the reel's headline measurement, shown as counted tiles, not asserted |
| B09 | SHOW | B09_DisjointVocabularies (Manim) | Two real concept vocabularies, an explicit empty intersection, and a verbatim-quoted docstring — this reel's sharpest falsifiability moment |
| B10 | SHOW | B10_TwoFixesOneRecord (Manim) | A real record ID (`f4a4c782`), two real same-day fixes, a real suppression mechanism |
| B11 | SHOW | B11_RegexTruncation (Manim) | A real extraction bug, shown truncating a real number on screen |
| B12 | SHOW | B12_TrueNowList (Manim) | Each line is a callback to an already-shown beat's own confirmed claim |
| B13 | SHOW | B13_StillNotTrueAndUncommitted (Manim) | Real ledger counts, a real commit hash, a real file count |
| B14 | SHOW | B14_SixteenZeroReprise (Manim) | Callback + end-card stats; second-to-last per OUTRO-LAW |
| B15 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate, kept deliberately simple |

**16 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph or a stock stand-in. Every claim in
this script is a real mechanism, a real measured result, or a real quoted
docstring/log entry from this project's own code — and, per SOURCES.md,
independently re-verified against the live checkout to an unusually high
degree for this series. All animatable diagrams, not costumes.

**Punt costumes explicitly avoided:** no generic "AI brain" icon, no stock
handshake/checkmark photo standing in for "the tool caught it," no gen-AI
clip for the fabrication moment. The provenance rows (B04), the disjoint
vocabularies (B09), the suppression timeline (B10), and the regex
truncation (B11) are all built as real diagrams that enact the sentence
rather than illustrate it after the fact.

## Beat-count deviation (16, not 10, not the prior reel's 15)

`agents.md`'s Quick Start default is a fixed 10-beat B00–B09 structure. This
reel authors 16 (B00–B15) because:

- **The script's own PRODUCTION NOTES commission exactly 12 named figures**
  with explicit timestamps, one per beat except where noted below — a
  content mass roughly 20% larger than the series' prior entry, which
  commissioned 11 figures across its own expanded Chapter 3.
- **Chapter 1 gets a beat despite carrying no commissioned figure** — the
  script's own stage direction ("no new build") still describes real
  content (the mechanism recap, the 7/12 limitation, the §3.4 quote) that
  needs its own beat for pacing, just a deliberately simpler one.
- **Chapter 7 is split into two beats (B12, B13)** because the script itself
  gives it two separate VISUAL directions ("list one, building line by
  line" vs. "list two, in warning color, held on screen, do not clear it")
  and its combined word count (300 words, ~120s) would otherwise make one
  beat nearly three times the reel's median length — the same "one idea per
  beat" reasoning the prior reel used to split its own five-test chapter
  across seven beats rather than three.

This matches the reel's actual content mass rather than forcing a fixed
count — `fellows/divij-pawar/CLAUDE.md` §4's "one idea per beat" rule was
prioritized over matching any fixed beat count exactly.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the comparator's whole mechanism (two
  agents, same company, flag mismatches, hand off to a person) before any
  measurement content begins, so the viewer has the system's shape before
  watching it get measured.
- [x] **WORKED EXAMPLE** — one continuous thread: the `f4a4c782` fabrication
  case, introduced structurally in the cold open (B00), gets its full
  provenance treatment in B04, and its full suppression-mechanism treatment
  in B10 — the same case walked through at three levels of depth across the
  reel, not four disconnected illustrations.
- [x] **FALSIFIABILITY / edge-case beat** — B09 (structurally disjoint
  vocabularies — the actual reason no comparator tuning can ever help) and
  B07 (an architecture test proven able to fail, three times, on purpose)
  are this reel's two sharpest falsifiability beats. B03's "checked the
  critique and it was worse than stated" and B10's "the fix I already
  shipped now suppresses my own best evidence" are a third and fourth,
  applied to the *process* of building this period's work rather than only
  to the system under test — more falsifiability content, and more varied
  in kind, than either prior reel in this series.
- [x] **SCAFFOLDED viewer task** — **none present, deliberately.** This is a
  weekly work-recap video, not a tutorial; the source script contains no
  "your turn" prompt anywhere in its VO or production notes, and none was
  invented. Matches the series' established precedent.
- [x] **Bookends** — B00 (cold open), B15 (title-restate outro). Same
  two-bookend shape as the-number-that-wasnt-there; no verdict-card or
  handoff bookend, since the honest-ledger content that would normally live
  there is a full two-beat Manim treatment (B12/B13) instead.
- [x] **No source, no verdict** — every claim-bearing beat carries its own
  on-screen artifact: the recap panel and quote card (B01), the ledger and
  null/false chips (B02), the struck-wrong-layout and real four-band layout
  (B03), the provenance rows (B04), the layered architecture and snapshot
  diff (B05), the collapsing duplications (B06), the three named test
  failures (B07), the sorted 31-tile corpus (B08), the disjoint vocabulary
  lists (B09), the suppression timeline (B10), the truncating regex (B11),
  the two honest-ledger lists (B12/B13), and the end-card reprise (B14).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ (4 distinct
moments, more than either prior series entry) | SCAFFOLDED TASK — N/A,
weekly-update format | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Risk flagged, then resolved: runtime, not repetition

Unlike the-number-that-wasnt-there (whose main authored risk was five
near-identical test-card beats), this reel's beats are each structurally
distinct — no two consecutive beats share a template. **The risk was
runtime, not repetition**: the first authoring pass projected ~12:55
against the script's own 8:00 target (+61%, proportionally the largest
overrun in the series so far, vs. the prior reel's +17%).

**Resolved (2026-09-08, same day):** applied the script's own "cut to
~6:00" guidance, targeted toward ~8:00. All three named cut items were
applied in full (B03's timings, B06's `_latest_value` case, B11's
stale-ledger footnote), plus proportional trims to eight other beats.
**Chapter 7 (B12, B13) and the uncommitted-state content inside it were
not touched at all**, honoring the script's explicit never-cut floor by
leaving it completely untouched rather than trimming it least. Result:
~8:19 (499s), a 4% difference from the ~8:00 request. See PEDAGOGY.md
"Runtime — recomputed, then cut" for the full before/after table.

A secondary, smaller risk: **B12 and B13, rendered as two independent Manim
scenes, must read as one continuous "honest ledger" movement** despite the
script's "do not clear it" direction technically applying across what is
now a beat boundary in this pipeline's format (each Manim scene is an
independent render). B13 opens directly into its own warning-color list
without any bridging transition from B12's close, which should be checked
at the first real render (see PEDAGOGY.md's reviewer checklist).

## Slate rules audit (Step 4b)

Not yet run against this reel's `beat_sheet.json` — `runtime/qc/sheet_check.py
--strict` is Step 1 of BUILD-PROMPT.md, to be run once GATE P is signed. A
manual field-length spot-check against `agents.md`'s 16:9 limits table:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 24 chars ("CROSS-AGENT VALIDATION") | 125 hard | yes |
| B00 | `greeting` | "Hola, Divij" | 55 hard | yes |
| B00 | `command` | 75 chars, single line | wraps, not hard | yes |
| B00 | `segment` | "Zero For Sixteen" (17 chars) | 80 hard | yes |
| B15 | `title` | "Zero For Sixteen" (17 chars) | wraps, not hard; ≤48 recommended | yes |
| B15 | `handle` | "@DivijPawar" | ~100 hard (16:9) | yes |
| B15 | `subline` | "Written down, versioned, and executable." (41 chars) | ≤60 recommended | yes |

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact in `shot.manim.scene_class` or
`shot.remotion.pattern`. Two beats carry denser layouts than the reel's
median and should get specific attention at the first real render:

- **B13** stacks a 7-line warning list, a git-commit panel, a large file
  counter, and a closing caption all in one scene without clearing the list
  — the densest single frame in the reel by design (see PEDAGOGY.md
  "Runtime" for why this isn't trimmed). Confirm nothing collides at 4K.
- **B14** stacks a 7-bullet end card beneath the sixteen-zero counter
  reprise — confirm the bullet list, scaled to fit, stays legible and
  doesn't visually compete with the counter above it.

**Not yet verified by actual rendered pixels** — this is an authoring-time
report, per the task's explicit constraint that nothing renders before
GATE P.

## PPT test

No beat is a headline read over a static paragraph. B03's wrong layout is
visibly struck through, not narrated past. B04's two rows literally
reconcile or literally don't. B05's snapshot diff literally lands on "0
DIFFERENCES." B06's three duplicate regex lines literally collapse into
one. B07's three violations literally produce three named failures, then
literally restore. B08's 31 tiles literally sort into buckets, one of which
literally stays empty. B09's two vocabulary lists literally have an empty
gap between them. B10's record card literally desaturates and gets
re-stamped. B11's number literally truncates on screen. B12/B13's lists
literally build and hold, not scroll past.

## Status

Beat sheet, `graphics_lib.py` (copied byte-identical from
the-number-that-wasnt-there, confirmed via `diff`, untouched by this build
per house rule), and `scenes.py` are authored and internally consistent —
verified by direct check: every `shot.manim.scene_class` in
`beat_sheet.json` has exactly one matching `class` in `scenes.py`, no
extras, no gaps (`B01_RecapAndGap` through `B14_SixteenZeroReprise`).
`scenes.py` parses cleanly under `ast.parse`. This pass closes the PROOF
GATE for authoring.

**No audio has been generated. No Manim or Remotion render has been run.**
This build stops here, before GATE P. See `PEDAGOGY.md` for the sign-off
checklist (including the runtime and Chapter-7-split flags) and
`BUILD-PROMPT.md` for the commands to run once a human flips the verdict to
PASS.

## Render log (2026-09-08, after GATE P PASS)

GATE P signed (Divij Pawar). Full pipeline run per `BUILD-PROMPT.md`:

- **Audio:** all 16 beats generated via Kokoro. Real durations came in
  faster than the pre-audio estimates across every beat but one (B15,
  +0.76s) — total measured runtime **6:45 (404.93s)**, not the ~8:19
  estimate. All 14 Manim `TARGET` constants retimed to the measured values
  (see `scenes.py`'s per-class comments).
- **Render:** all 14 Manim scenes rendered clean at both `-qh` (preview)
  and `-qk` (final 4K), zero errors. Both Remotion bookends (B00, B15)
  rendered natively at 3840×2160.
- **Visual QC found two real defects, both fixed before the 4K pass:**
  1. **B08 (`corpus-buckets`):** the collapsing tile piles were moved to
     each bucket box's exact center via `t.animate.move_to(buckets[i])`,
     landing directly on top of the box's own label text — visible as a
     stray colored square sitting on "concepts" and on "other" in the
     rendered frames. Fixed by landing the piles below each box
     (`buckets[i].get_bottom() + DOWN * 0.35`) instead of on its center.
  2. **B04 (`provenance-rows`):** the ⚠ warning glyph (`Text("⚠", ...)`)
     rendered as a `.notdef` fallback — literal hex codepoint digits
     ("26"/"A0") stacked in place of the symbol, the same class of font
     failure `graphics_lib.py` already documents for ✓/✕ (Montserrat and,
     in this case, Manim's own default font too, have no ⚠ glyph on this
     machine). Fixed by replacing the emoji with a drawn `Triangle()` +
     bold "!" — a real vector shape, not a font-dependent glyph.
  Both fixes were verified against real rendered frames at both 1080p and
  the final 4K resolution before compiling the delivered master — neither
  was assumed fixed from the code change alone.
- **Compile:** final 4K master compiled, 16/16 slots filled, zero slates,
  3840×2160 @ 30fps, 404.93s — matches the sum of measured Kokoro
  durations exactly.
- **Captions:** word-level alignment via `align.py` (faster-whisper,
  16/16 beats aligned, 0 fallbacks), `captions.srt` generated (147 cues),
  muxed as a soft `mov_text` stream into `zero-for-sixteen.mp4` — captions
  off by default, on when the viewer enables them, never burned in.
- **9:16 Shorts derivative: complete** (`short/zero-for-sixteen-short.mp4`,
  1080×1920, 2:37.8, captioned). `shorts.py`'s auto-plan wanted to drop
  **B12 and B13 — the entirety of Chapter 7** — to fit the 3:00 cap; this
  was not accepted. Per an explicit decision, B12/B13 were force-kept and
  eleven other beats dropped instead, so the short is mostly the
  honest-ledger chapter plus bookends. Building it required three new
  portrait Manim scenes (`short/scenes.py`), and visual QC on that new
  layout caught and fixed one real collision (B13's file counter
  overlapping its closing caption — fixed by switching hand-placed
  y-coordinates to `.next_to()` chaining). Full account in
  `BUILD-PROMPT.md` "Shorts status."
