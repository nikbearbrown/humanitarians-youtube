# QC-REPORT — claude-cli-rag-vector-databases-short (9:16)

*VISUAL QC LAW pass for the vertical derivative cut.*
*"Watch Exact Search Hit A Wall." · RAG Foundations, Chapter 5.*

---

## File check (not QC)

| Property | Value |
|---|---|
| Resolution | **2160×3840** (native 4K portrait — not downscaled to 1080×1920) |
| Duration | 147.47s (**2:27**) — under YouTube's 3:00 Shorts cap |
| Frame rate | 24 fps |
| Audio | AAC, mono, per-beat narration |
| Slots | 9/9 filled, zero slates |

## The cut — a SINGLE cycle, per doctrine

cli-explainer's **THE REVISION LAW** names the 9:16 cut as its one exception:
the short "ships a SINGLE cycle — CLI → CODE → OUTPUT, no revision — and points
the viewer to the 16:9 for the complete example." That is what this is.

| Kept | Pattern | Spine role |
|---|---|---|
| B00 | `ClaudeComposerAsk916` | INTRO — the hook |
| B01 | `RagExecutiveSummary916` | PROBLEM — exact search doesn't scale |
| B02 | `ClaudeComposerAsk916` | CLI — the ask |
| B03 | `ClaudeCodeBeat916` | CODE — real `brute_force_search.py` |
| B04 | `CliRunOutput916` | OUTPUT — the measured linear cost |
| B09 | `RagExecutiveSummary916` | SUMMARY (rewritten — see below) |
| B10 | `ClaudeComposerAsk916` | NEXT STEPS (HANDOFF LAW) |
| B11 | `TitleOutroChannel916` | OUTRO (rewritten — points to the long cut) |
| END | silent branded endcard | `@VedanshuDaxeshPatel` |

**Dropped:** B05, B06, B07, B08 — the whole revision cycle, plus the scaling
chart and the recall dial.

**What the short therefore is:** a self-contained proof of the *problem*. It
builds exact search, runs it, and shows the cost tracking the collection — which
is exactly what the title promises. The fix is deferred to the 16:9, and both
the rewritten outro and the endcard say so.

A derivative cut, not a re-edit: `short/` carries its own `beat_sheet.json` and
all 8 Remotion beats were re-rendered through their `916` compositions
(RENDER-TARGETS.md §3). **Nothing is centre-cropped.**

## Defects

### B00 — render FAILED on first pass — transient, resolved on retry

**Found.** `remotion_scenes.py` reported
`FAIL: ClaudeComposerAsk916 … Error opening output files: No such file or
directory`, raised inside Remotion's own audio pipeline
(`createSilentAudio` → `mergeAudioTrackUnlimited`, writing `merged.wav`).

**Diagnosis — not a reel defect.** The failure is in Remotion's temp-file
handling, not in the component or its props: the *same* composition
(`ClaudeComposerAsk916`) rendered successfully for B02 and B10 in the same batch.
B00 was simply the first render of the run.

**Resolution.** Re-rendered with `--only B00 --force`; succeeded first try and
the frame was inspected clean. Worth knowing it can recur: **a single-beat FAIL
in a batch is worth retrying before debugging anything.**

### No layout defects found

Unlike the Chapter 4 short — where portrait exposed a collapsed meter bar and
undersized BLUF type — this cut's beats all re-banded correctly on the first
render. Nothing needed a component fix.

## Checked and passing

| Beat | Portrait note |
|---|---|
| B00 | Re-banded; greeting, wrapped ask, all three output lines, folder chip, terracotta send |
| B01 | PROBLEM card legible; generous portrait type |
| B02 | "The ask," greeting; full prompt wraps cleanly |
| B03 | **The riskiest beat.** `ClaudeCodeBeat916` WRAPS long lines rather than clipping them — the docstring and the trailing comment flow to a second line and stay legible. No overflow, no clipped glyphs |
| B04 | **Transcript column alignment survives portrait** (the classic failure for this component); real numbers 0.08 / 1.16 / 10.87 intact; terracotta `$`; verdict line present |
| B09 | Rewritten summary reads correctly with no reference to the dropped build |
| B10 | Handoff prompt legible; "Your turn." greeting |
| B11 | Title wraps to three lines with the terracotta stop; handle; author signature |
| END | Handle in EB Garamond, terracotta hairline, "Full video: the index, and what it costs." |

## Minor — noted, deliberately not fixed

**B04 leaves the lower ~55% of the frame empty.** `CliRunOutput`'s portrait
auto-fit only ever SHRINKS the transcript to fit its band
(`bandTop 0.241` → `bandBottom 0.66` of height); it never grows it. With a
5-line transcript the text therefore sits in the upper half.

Making the auto-fit grow would be a genuine improvement for a phone — but
`CliRunOutput916` is already used by **three other shipped shorts** in this book
(`2026-09-01-claude-summary`, `2026-08-31-claude-cli-rag-introduction`,
`2026-08-31-claude-cli-rag-the-problem`). Changing its portrait sizing would
silently alter all three on any re-render. Scope discipline wins over an
aesthetic tweak: the transcript is fully legible and the spacing is within the
component's own designed band, so this is logged rather than changed.

**B00's third output line wraps** ("…approximate, on / purpose"). Legible;
below the MAJOR threshold.

## Compiler warnings — reviewed, all three accepted

1. **`SKIN LINT: B00 … cold open is 'ClaudeComposerAsk916'`** — false positive.
   The linter matches the landscape id; the `916` twin is precisely what
   RENDER-TARGETS.md §3 requires of a vertical cut.
2. **`SKIN LINT: END … outro is 'un-annotated'`** — false positive. `END` is the
   silent branded endcard the Shorts law mandates, and it follows B11, which
   *is* the title restate.
3. **`'remotion' carries 8/9 beats (88%)`** — accepted. That cap governs vox
   mixed-media films; a CLI explainer is composer/code/output by construction.

## Windows notes (both pre-empted this time)

- `shorts.py` symlinks the parent mp3s into `short/mp3/`, which fails without
  elevated privileges (`OSError 1314`). They were **pre-copied** before running
  the derivation. Consequence: the short's audio is a snapshot — **if parent
  narration is regenerated, re-copy it.**
- `shorts.py`'s endcard helper falls back to an ~11px bitmap font
  (`find_serif()` probes only macOS/Linux paths) and builds at 1080×1920. The
  endcard was regenerated at 2160×3840 with the bundled EB Garamond from
  `runtime/fonts/`, so there is no upscale and no illegible handle.

## Verdict

**PASS** — 2160×3840, 2:27, 9/9 slots filled, zero slates, zero BLOCKER, zero
MAJOR. One transient render failure, retried and verified. Two MINOR items
logged with reasons for not acting.
