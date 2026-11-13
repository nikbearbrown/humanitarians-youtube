# QC-REPORT — claude-rag-no-default-short (9:16)

*VISUAL QC LAW pass for the vertical derivative cut.*
*"There Is No Default." · RAG Foundations, Chapters 4–6 — the summary.*

---

## File check (not QC)

| Property | Value |
|---|---|
| Resolution | **2160×3840** (native 4K portrait — not downscaled to 1080×1920) |
| Duration | 150.18s (**2:30**) — under YouTube's 3:00 Shorts cap |
| Frame rate | 24 fps |
| Audio | AAC, mono, per-beat narration |
| Slots | 10/10 filled, zero slates |

## The cut — nothing dropped

**`shorts.py` reported `dropped: none`.** The parent summary is already a
distillation of three full reels at 2:25, so all nine beats plus the silent
endcard fit inside the cap at 2:30. The cap planner was allowed to decide rather
than being handed a drop list, and it found no cut necessary.

This is the first short in this series where the full cut survives intact, and
it is the honest outcome — trimming a reel that already fits would remove
content for no reason.

| Beat | Pattern |
|---|---|
| B00 | `ClaudeComposerAsk916` |
| B01 | `BrutalistHesitantWriter916` |
| B02 | `ChunkSizeTradeoff916` (Ch4) |
| B03 | `AnnRecallDial916` (Ch5) |
| B04 | `RetrievalMatrix916` (Ch6) |
| B05 | `RrfMargin916` (Ch6) |
| BVDT | `ClaudeVerdictArtifact916` |
| BHTF | `ClaudeComposerAsk916` |
| BOUT | `TitleOutroChannel916` |
| END | silent branded endcard |

**Two consequences of no drops, both good:**

1. `shorts.py` did **not** rewrite the outro, so the `beat_topic()` truncation
   bug — which produced unusable narration on the Chapter 4, 5 and 6 shorts —
   never fired. No narration repair was needed.
2. No audio regeneration: every mp3 carries over from the parent unchanged.

A derivative cut, not a re-edit: `short/` carries its own `beat_sheet.json` and
all nine Remotion beats re-rendered through their `916` compositions
(RENDER-TARGETS.md §3). **Nothing is centre-cropped.**

## Defects

**None found.** Nine beats, zero render failures, zero component fixes.

### One defect PRE-EMPTED rather than discovered

**B01 — `BrutalistHesitantWriter916` portrait type size.**

The component scales by `Math.min(width / 1920, height / 1080)`, so a 1080×1920
frame resolves to the WIDTH ratio (0.5625) even though the frame is 1.78×
*taller*. The landscape `fontSize: 84` would therefore have rendered at roughly
55% of frame width with most of the frame empty — the exact FILL-THE-CANVAS
failure found on the Chapter 4 short.

Rather than render it, find it, and re-render, `fontSize` was raised to **100**
in the short's own beat sheet *before* the batch started. Verified after render:
the corrected BLUF spans ~75% of frame width, the correction ("solved" →
"design") is complete at 11.9s against a 12.22s cut, and there is no overflow.

The constraint was checked first, not assumed: the writer's lines use
`whiteSpace: 'pre'` and do **not** wrap, so the longest *corrected* line —
"Chunk size, recall, and matching" (32 chars) — was measured against
`maxWidth = width * 0.86` before choosing 100.

## Checked and passing

| Beat | Portrait note |
|---|---|
| B00 | Re-banded; greeting, wrapped ask, **all four output lines** fit, folder chip |
| B01 | Type fix verified (see above); correction lands before the cut |
| B02 | Chunk size axis re-bands — failure cards stack, unmarked middle intact |
| B03 | Dial curve, all four measured points, **recall ticks clear of the rotated axis caption** — the reserved tick column added for the Chapter 5 landscape beat holds in portrait too |
| B04 | Three method rows stack; derived **both** column correct; terracotta on the hybrid MISS |
| B05 | Both reciprocal sums legible; gold in terracotta; 0.00025 margin present |
| BVDT | **All four numbered verdict lines fit inside the card, no overflow**, every carried number intact (0.3%/33%, 10.2%/96%, 0.00025) |
| BHTF | Handoff prompt legible; "Your turn." greeting |
| BOUT | Title restate with terracotta stop, handle, author signature |
| END | Handle in EB Garamond, terracotta hairline, "Chapters 4–6, in full." |

## Provenance

Unchanged from the parent: every on-screen number traces to the source reel that
measured it (Ch5 `_run-ann.txt`, Ch6 `_run-hybrid.txt`). The short introduces no
new figure and alters no value — see the parent's SOURCES.md.

## Compiler warnings — reviewed, all three accepted

1. **`SKIN LINT: B00 … cold open is 'ClaudeComposerAsk916'`** — false positive.
   The linter matches the landscape id; the `916` twin is what
   RENDER-TARGETS.md §3 requires of a vertical cut.
2. **`SKIN LINT: END … outro is 'un-annotated'`** — false positive. `END` is the
   silent branded endcard the Shorts law mandates, and it follows BOUT, which
   *is* the title restate.
3. **`'remotion' carries 9/10 beats (90%)`** — accepted; that cap governs vox
   mixed-media films.

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

**PASS** — 2160×3840, 2:30, 10/10 slots filled, zero slates, zero BLOCKER, zero
MAJOR, zero render failures, zero narration repairs. One known portrait defect
pre-empted before it could reach a frame.
