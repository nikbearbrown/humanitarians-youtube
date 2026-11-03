# CHECKS-REPORT.md — fifteen-of-sixteen

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **18 beats (B00–B17)**, not the ai-explainer
default of 10, and two more than the series' prior entry
(zero-for-sixteen, 16 beats) — see "Beat-count deviation" below.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_OpenThreads (Manim) | Names the real two-way diagnosis and the order it was tackled in |
| B02 | SHOW | B02_NumberTagging (Manim) | Names the real tagging mechanism with real concept names |
| B03 | SHOW | B03_ThreeBugs (Manim) | Three real, named bugs, each struck FIXED |
| B04 | SHOW | B04_ReplayThroughGate (Manim) | The actual measurement method — same real 16 runs, shown filing through the gate |
| B05 | SHOW | B05_CheckedTwice (Manim) | Two real verification panels landing on the same number |
| B06 | SHOW | B06_TruePositivePreserved (Manim) | The tally, with the survivor explicitly relabeled |
| B07 | SHOW | B07_SharedContextFork (Manim) | Real model names, real run list, the reel's clearest "test never run before" moment |
| B08 | SHOW | B08_ZeroRealNumbers (Manim) | Real vs. fabricated context rendered as actual provenance, not narrated past |
| B09 | SHOW | B09_SignAndMagnitude (Manim) | A real, specific number turned into a real, specific wrong number |
| B10 | SHOW | B10_ModelScoreboard (Manim) | The chapter's own two-sided verdict, shown as a scoreboard not asserted |
| B11 | SHOW | B11_RouteRewire (Manim) | A real route, a real rule swap |
| B12 | SHOW | B12_RegexFix (Manim) | Two real fixes, each with its own mechanism shown |
| B13 | SHOW | B13_VerificationRateZero (Manim) | The real historic fabrication, replayed, with a real stamped rate |
| B14 | SHOW | B14_TrueNowList (Manim) | Each line callbacks to an already-shown beat's own confirmed claim |
| B15 | SHOW | B15_StillNotTrueAndUncommitted (Manim) | Real ledger counts, a real unchanged commit hash, a real growing file count |
| B16 | SHOW | B16_FifteenKilledReprise (Manim) | Callback + end-card stats; second-to-last per OUTRO-LAW |
| B17 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate, kept deliberately simple |

**18 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph or a stock stand-in. Every claim in
this script is a real mechanism, a real measured result, or a real quoted
log/ledger entry from this project's own code — and per SOURCES.md,
independently re-verified against the live checkout to the same high
degree as Mycroft6.

**Punt costumes explicitly avoided:** no generic "AI brain" icon, no stock
handshake/checkmark photo standing in for "the fix worked." The concept
tags (B02), the struck bug cards (B03), the sign-flip (B09), and the
truncating-then-fixed regex (B12) are all built as real diagrams that
enact the sentence rather than illustrate it after the fact.

## Beat-count deviation (18, not 10, not the series' prior 16)

`agents.md`'s Quick Start default is a fixed 10-beat B00–B09 structure.
This reel authors 18 (B00–B17) because:

- **The script's own PRODUCTION NOTES commission exactly 16 named
  figures** with explicit timestamps, one per beat except where noted
  below — a content mass proportionally larger than the prior reel's 12
  figures, reflecting two working sessions (diagnosis + fix) instead of
  one.
- **Chapter 2 gets 5 beats (B02–B06)** for its 4 figures plus a closer,
  the same "one idea per beat" reasoning the series has applied to its
  densest chapter in every prior entry.
- **Chapter 5 is split into two beats (B14, B15)** because the script
  itself gives it two separate VISUAL directions ("list one, building line
  by line" vs. "list two, in warning color, held on screen, do not clear
  it") — identical convention to Mycroft6's B12/B13 split.

This matches the reel's actual content mass rather than forcing a fixed
count — `fellows/divij-pawar/CLAUDE.md` §4's "one idea per beat" rule was
prioritized over matching any fixed beat count exactly.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the two-way diagnosis (link concepts
  / test overlap) before either thread's content begins, so the viewer has
  the shape of the whole video before either half plays out.
- [x] **WORKED EXAMPLE** — one continuous thread: the concept-tagging fix
  is introduced in B02, its three bugs walked through in B03, its
  measurement method in B04, its double-check in B05, and its tally in
  B06 — five beats building one worked example, not disconnected
  illustrations. A second thread (the overlap test) gets the same
  treatment across B07–B10.
- [x] **FALSIFIABILITY / edge-case beat** — B08/B09 (the mechanism fires,
  but for the wrong reason, and the specific wrong-sign/magnitude failure)
  and B15's "narrowing is not closing" line are this reel's sharpest
  falsifiability beats, stress-testing the fix's actual scope rather than
  a hypothetical edge case.
- [x] **SCAFFOLDED viewer task** — **none present, deliberately**, matching
  series precedent; this is a weekly-update recap, not a tutorial.
- [x] **Bookends** — B00 (cold open), B17 (title-restate outro). Same
  two-bookend shape as both prior reels.
- [x] **No source, no verdict** — every claim-bearing beat carries its own
  on-screen artifact: the branching-paths card (B01), the tagged sentence
  (B02), the three struck bug cards (B03), the tiles filing through the
  gate (B04), the two check panels (B05), the relabeled tally (B06), the
  context fork (B07), the real-vs-fabricated comparison (B08), the
  sign-flip (B09), the scoreboard (B10), the route diagram (B11), the
  two-fix sequence (B12), the stamped thought log (B13), the two honest-
  ledger lists (B14/B15), and the end-card reprise (B16).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ (two parallel threads,
each fully worked) | FALSIFIABILITY ✓ | SCAFFOLDED TASK — N/A,
weekly-update format | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Risk flagged: runtime pacing across two parallel five/four-beat threads

This reel's two main chapters (2 and 3) each build one continuous worked
example across four to five beats, similar in shape to Mycroft6's own
multi-beat chapters. Unlike Mycroft6, no runtime cut was needed here (the
script's own estimate was accurate), so this risk is about **pacing
variety**, not length: B02–B06 and B07–B10 are each five/four
consecutive beats on one throughline. Mitigations already built into
`scenes.py`: each beat's visual is structurally distinct (tagged sentence,
struck bug cards, filing tiles, dual check panels, relabeled tally, forked
context, real-vs-fake comparison, sign-flip, scoreboard) rather than one
template reused five times, avoiding the specific repetition risk
Mycroft5's own five-test chapter was flagged for. Not fully resolved here —
a human should confirm at the first real render whether the two
back-to-back multi-beat threads read as varied enough, or whether Chapter
2 in particular (5 beats) needs a mid-chapter pacing break.

## Slate rules audit (Step 4b)

Not yet run against this reel's `beat_sheet.json` — `runtime/qc/sheet_check.py
--strict` is Step 1 of BUILD-PROMPT.md, to be run once GATE P is signed. A
manual field-length spot-check against `agents.md`'s 16:9 limits table:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 24 chars ("CROSS-AGENT VALIDATION") | 125 hard | yes |
| B00 | `greeting` | "Hola, Divij" | 55 hard | yes |
| B00 | `command` | 70 chars, single line | wraps, not hard | yes |
| B00 | `segment` | "Fifteen Of Sixteen" (19 chars) | 80 hard | yes |
| B00 | `output[2]` | "One agent invented a quarter, a filing, and a source URL, all fake" (68 chars) | recommended ≤70 | yes |
| B17 | `title` | "Fifteen Of Sixteen" (19 chars) | wraps, not hard; ≤48 recommended | yes |
| B17 | `handle` | "@DivijPawar" | ~100 hard (16:9) | yes |
| B17 | `subline` | "Written down, versioned, and executable." (41 chars) | ≤60 recommended | yes |

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact in `shot.manim.scene_class` or
`shot.remotion.pattern`. Beats carrying denser layouts, flagged for
specific attention at the first real render:

- **B15** stacks a 5-line warning list, a git-commit panel, a file-count
  chip, and a closing caption all in one scene without clearing the list —
  the densest single frame in the reel by design (never trimmed for time,
  per the script's own explicit floor). Confirm nothing collides at 4K.
- **B16** stacks a 7-bullet end card beneath the "15 KILLED / 1 TRUE
  POSITIVE" reprise — confirm the bullet list stays legible and doesn't
  visually compete with the reprise above it, same check Mycroft6's
  equivalent beat needed.
- **B08** places two full context boxes side by side with a stamp beneath —
  confirm the stamp doesn't crowd either box at 4K.
- **B03**'s three-card-and-strike sequence — confirm each `FIXED` stamp
  lands clear of its card's own strike-through line, not overlapping it.

**Not yet verified by actual rendered pixels** — this is an authoring-time
report, per the task's explicit constraint that nothing renders before
GATE P. `graphics_lib.py`'s `warn_icon()` — not used in this reel's
`scenes.py` (no ⚠ needed), but retained in case a future scene needs it,
given the ⚠-glyph failure caught during zero-for-sixteen's own visual QC.

## PPT test

No beat is a headline read over a static paragraph. B02's numbers
literally get tagged on screen. B03's three cards literally strike through
and stamp FIXED. B04's tiles literally file through the gate. B05's two
panels literally connect on the same number. B08's two context boxes
literally show real vs. fabricated content side by side. B09's real
figure literally gets arrowed into its wrong counterpart. B12's number
literally truncates then literally gets corrected back. B14/B15's lists
literally build and hold, not scroll past.

## Status

Beat sheet, `graphics_lib.py` (copied byte-identical from zero-for-sixteen,
confirmed via `diff`, untouched by this build per house rule), and
`scenes.py` are authored and internally consistent — verified by direct
check: every `shot.manim.scene_class` in `beat_sheet.json` has exactly one
matching `class` in `scenes.py`, no extras, no gaps (`B01_OpenThreads`
through `B16_FifteenKilledReprise`). `scenes.py` parses cleanly under
`ast.parse`. This pass closes the PROOF GATE for authoring.

**No audio has been generated. No Manim or Remotion render has been run.**
This build stops here, before GATE P. See `PEDAGOGY.md` for the sign-off
checklist and `BUILD-PROMPT.md` for the commands to run once a human flips
the verdict to PASS.

## Render log (2026-09-20, after GATE P PASS)

GATE P signed (Divij Pawar, via direct chat instruction). Full pipeline run
per `BUILD-PROMPT.md`:

- **Audio:** all 18 beats generated via Kokoro. Real durations came in
  faster than the pre-audio estimates across every beat but one (B17,
  +0.6s) — total measured runtime **6:51 (411.2s)**, not the ~8:50
  estimate, consistent with the ~22% gap this series has now shown on both
  prior reels. All 16 Manim `TARGET` constants retimed to the measured
  values; every scene's actual choreographed elapsed time was already
  comfortably below its new target, so no `self.wait()` calls needed
  adjustment (verified by summing each scene's `run_time`/`wait()` calls
  before assuming this, not carried forward as an assumption).
- **Render:** all 16 Manim scenes rendered clean at both `-qh` (preview)
  and `-qk` (final 4K), zero errors. Both Remotion bookends (B00, B17)
  rendered natively at 3840×2160.
- **Visual QC found one real defect, fixed before the 4K pass:**
  **B08 (`zero-real-numbers`):** the real-context and fabricated-context
  boxes were positioned with hardcoded coordinates (`move_to([-2.6, ...])`
  / `move_to([2.6, ...])`) sized for an assumed content width; the actual
  mono text (`"Assets: 383266000000.0"`, `"sec.gov/fake-filing-000"`) was
  wider than assumed, and the two boxes overlapped with text crossing
  between them — caught only by reading the actual rendered frame, not
  visible from the code. Fixed by building both boxes without explicit
  coordinates and using `VGroup(realbox, fakebox).arrange(RIGHT,
  buff=0.5)` instead, which guarantees clearance regardless of actual
  content width — the same class of fix (arrange, don't hand-guess
  coordinates for variable-width content) as zero-for-sixteen's own B08
  fix. Verified against real rendered frames at both 1080p and the final
  4K resolution before compiling the delivered master.
- **Compile:** final 4K master compiled, 18/18 slots filled, zero slates,
  3840×2160 @ 30fps, 411.2s — matches the sum of measured Kokoro durations
  exactly.
- **Captions:** word-level alignment via `align.py` (faster-whisper,
  18/18 beats aligned, 0 fallbacks), `captions.srt` generated (144 cues),
  muxed as a soft `mov_text` stream into the final file.
- **Delivered as `Mycroft_DivijPawar_09-11-2026.mp4`** per this channel's
  actual naming convention (the pipeline's own output filename is the slug,
  `fifteen-of-sixteen.mp4` — renamed as Step 10, per BUILD-PROMPT.md, which
  built this step in from the start this time based on the correction
  needed on zero-for-sixteen's own delivery).
- **The 9:16 Shorts derivative was not attempted this pass** — per
  BUILD-PROMPT.md's own "Shorts" section, that decision (whether to accept,
  override, or skip the auto-plan given the likely Chapter-5 conflict)
  needs to be made explicitly, the same way it was for zero-for-sixteen,
  rather than defaulted into.
