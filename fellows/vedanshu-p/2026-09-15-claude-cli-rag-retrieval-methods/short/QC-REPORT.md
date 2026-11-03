# QC-REPORT — claude-cli-rag-retrieval-methods-short (9:16)

*VISUAL QC LAW pass for the vertical derivative cut.*
*"Watch The Right Answer Get Outvoted." · RAG Foundations, Chapter 6.*

---

## File check (not QC)

| Property | Value |
|---|---|
| Resolution | **2160×3840** (native 4K portrait — not downscaled to 1080×1920) |
| Duration | 153.63s (**2:34**) — under YouTube's 3:00 Shorts cap |
| Frame rate | 24 fps |
| Audio | AAC, mono, per-beat narration |
| Slots | 9/9 filled, zero slates |

## The cut — a SINGLE cycle, per doctrine

cli-explainer's **THE REVISION LAW** names the 9:16 cut as its one exception:
the short "ships a SINGLE cycle — CLI → CODE → OUTPUT, no revision — and points
the viewer to the 16:9 for the complete example."

| Kept | Pattern | Spine role |
|---|---|---|
| B00 | `ClaudeComposerAsk916` | INTRO |
| B01 | `RetrievalTwoQueries916` | PROBLEM — two employees, one policy |
| B02 | `ClaudeComposerAsk916` | CLI — the ask |
| B03 | `ClaudeCodeBeat916` | CODE — real `bm25_search.py` |
| B04 | `CliRunOutput916` | OUTPUT — HIT on the code, MISS on the paraphrase |
| B09 | `RagExecutiveSummary916` | SUMMARY (rewritten) |
| B10 | `ClaudeComposerAsk916` | NEXT STEPS (rewritten) |
| B11 | `TitleOutroChannel916` | OUTRO (rewritten) |
| END | silent branded endcard | `@VedanshuDaxeshPatel` |

**Dropped:** B05, B06, B07, B08 — the revision cycle, the results matrix and
the RRF margin beat.

**What the short therefore is:** a self-contained demonstration of sparse
retrieval's blind spot. BM25 wins the exact-code query precisely because
`TR-114` is rare, and loses the paraphrase because the question shares almost no
words with its answer. The dense retriever, the fusion, and the 0.00025 upset
are all deferred to the 16:9, and the outro and endcard both say so.

A derivative cut, not a re-edit: `short/` carries its own `beat_sheet.json` and
all 8 Remotion beats re-rendered through their `916` compositions
(RENDER-TARGETS.md §3). **Nothing is centre-cropped.**

## Defects

**None.** All eight beats rendered clean on the first pass, with no failures and
no component fixes required — the same outcome as the Chapter 6 landscape
master. The `916` twins of the three new Chapter 6 components were built
dual-aspect from the start rather than retro-fitted.

Notably, B00 did **not** hit the Remotion startup flake that failed the first
beat of the previous two batches.

## Checked and passing

| Beat | Portrait note |
|---|---|
| B00 | Re-banded; greeting, wrapped ask, three output lines, folder chip |
| B01 | **Genuinely re-banded:** the two query cards stack vertically in portrait rather than sitting side by side, arrow and gold TR-114 chunk intact below. Not a crop |
| B02 | "The ask," greeting; the tokenisation clause still legible |
| B03 | **The riskiest beat.** `ClaudeCodeBeat916` wraps the long lines (the TOKEN regex, the `norm =` line, the `s +=` line) rather than clipping. The regex still renders literally as `r"[a-z0-9][a-z0-9\-]*"`. No overflow |
| B04 | Transcript column alignment survives; the first query line wraps but stays legible; scores 3.488 / 3.819 / 1.957 / 1.943 intact; HIT then MISS; verdict present |
| B09 | Rewritten summary reads correctly with no reference to dense, hybrid or fusion |
| B10 | Rewritten handoff prompt legible; "Your turn." greeting |
| B11 | Title wraps with the terracotta stop; handle; author signature |
| END | Handle in EB Garamond, terracotta hairline, "Full video: the hybrid, and how it lost." |

## Minor — noted, deliberately not fixed

**B04 leaves the lower ~50% of the frame empty.** `CliRunOutput`'s portrait
auto-fit only ever SHRINKS the transcript to fit its band; it never grows it, so
a short transcript sits in the upper half.

Unchanged for the same reason as the Chapter 5 short: `CliRunOutput916` is used
by **four other shipped shorts** in this book, and altering its portrait sizing
would silently change all of them on any re-render. The transcript is fully
legible and the spacing is within the component's own designed band, so this is
logged rather than changed.

## Compiler warnings — reviewed, all three accepted

1. **`SKIN LINT: B00 … cold open is 'ClaudeComposerAsk916'`** — false positive.
   The linter matches the landscape id; the `916` twin is exactly what
   RENDER-TARGETS.md §3 requires of a vertical cut.
2. **`SKIN LINT: END … outro is 'un-annotated'`** — false positive. `END` is the
   silent branded endcard the Shorts law mandates, and it follows B11, which
   *is* the title restate.
3. **`'remotion' carries 8/9 beats (88%)`** — accepted; a CLI explainer is
   composer/code/output by construction.

## Windows notes (both pre-empted)

- `shorts.py` symlinks the parent mp3s into `short/mp3/`, which fails without
  elevated privileges (`OSError 1314`). Pre-copied before deriving. Consequence:
  the short's audio is a snapshot — **if parent narration is regenerated,
  re-copy it.**
- `shorts.py`'s endcard helper falls back to an ~11px bitmap font
  (`find_serif()` probes only macOS/Linux paths) and builds at 1080×1920.
  Regenerated at 2160×3840 with bundled EB Garamond — handle at 55% of frame
  width, no upscale.

## Verdict

**PASS** — 2160×3840, 2:34, 9/9 slots filled, zero slates, zero BLOCKER, zero
MAJOR, zero render failures. One MINOR logged with its reason for not acting.
