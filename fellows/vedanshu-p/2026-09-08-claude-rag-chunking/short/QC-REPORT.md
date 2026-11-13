# QC-REPORT — claude-rag-chunking-short (9:16)

*VISUAL QC LAW pass for the vertical derivative cut.*
*"Where You Cut The Page." · RAG Foundations, Chapter 4.*

---

## File check (not QC)

| Property | Value |
|---|---|
| Resolution | **2160×3840** (native 4K portrait — not downscaled to 1080×1920) |
| Duration | 151.36s (**2:31**) — under YouTube's 3:00 Shorts cap |
| Frame rate | 24 fps |
| Audio | AAC, mono, per-beat narration |
| Slots | 9/9 filled, zero slates |

## The cut

A **derivative cut, not a re-edit** — `short/` carries its own `beat_sheet.json`
and every Remotion beat is rewired to its `916` composition (RENDER-TARGETS.md
§3). **Nothing is centre-cropped.**

| Kept | Pattern | Role |
|---|---|---|
| B00 | `ClaudeComposerAsk916` | hook — "a piece of text of *what size*?" |
| B01 | `BrutalistHesitantWriter916` | BLUF — chunking is a design decision |
| B02 | `ChunkWholeDocVector916` | whole document → one averaged vector |
| B03 | `ChunkSizeTradeoff916` | fails in both directions |
| B05 | `ChunkThreeStrips916` | the chapter's Fig. 01, redrawn |
| B08 | `ChunkThreeWays916` | one question, three outcomes |
| BHTF | `ClaudeComposerAsk916` | your turn (HANDOFF LAW) |
| BOUT | `TitleOutroChannel916` | title + signature, points to the long cut |
| END | silent branded endcard | `@VedanshuDaxeshPatel` |

**Dropped:** B04 (overlap), B06 (separator ladder), B07 (predict card),
BVDT (verdict recap).

**Why these four, and why not the auto-plan.** `shorts.py`'s greedy planner
drops the LONGEST unprotected beats, which would have taken BHTF (34.3s) and
BVDT (27.0s) — gutting the handoff that HANDOFF LAW makes mandatory. The drops
were therefore driven manually. The verdict recap was cut in preference to the
handoff on the reasoning that **a Short is already a compression**, so a 27s
recap inside one is the redundant element, whereas the handoff is both
law-mandated and the Short's call to action. B04 and B06 are the two extra
design dimensions and B07 is a pacing device — the omission is named out loud
by the rewritten outro, which tells the viewer the full video covers them.

## Defects found and fixed

### B01 — type far too small in portrait — FIXED

**Found.** The BLUF — the single most important text beat in the cut — rendered
at ~55% of frame width with roughly 70% of the frame empty. FILL-THE-CANVAS LAW.

**Root cause (shared component, not this reel).** `BrutalistHesitantWriter`
scales by `Math.min(width / 1920, height / 1080)`. On a 1080×1920 frame that
resolves to the WIDTH ratio, 0.5625 — so portrait type shrinks to 56% even
though the frame is 1.78× *taller*. The component's docstring claims it
"composes at 16:9, 9:16, 1:1 and 4:3"; for 9:16 that is optimistic.

**Fix.** `fontSize` 74 → 100 (and `lineSpacing` 1.30 → 1.34) **in the short's own
beat sheet**, not in the component — changing that scaling math would alter
every other reel that uses it. Result: ~74% of frame width, correction complete
before the cut, no overflow.

**Constraint for anyone re-tuning this:** the writer's lines use
`whiteSpace: 'pre'` and do **not** wrap, so `fontSize` cannot be raised without
checking the longest *corrected* line — "Chunking is a design decision."
(30 chars) — against `maxWidth = width * 0.86`.

### B02 — the match meter vanished entirely in portrait — FIXED

**Found.** In the 9:16 cut the query label ("how many vacation days?") and
"approximate match" both rendered, but **the meter bar between them did not
exist**. Since the bar is what shows the match is only *partial*, the portrait
beat had lost its entire point while looking superficially fine.

**Root cause.** The meter carried `flex: 1`. The query row is a COLUMN in
portrait, so flex-grow resolves against the **height** axis and `flex-basis: 0%`
collapsed the bar to zero height, overriding its explicit `height`.

**Fix.** `flex: portrait ? 'none' : 1`, explicit `width: '86%'`, `flexShrink: 0`.
Verified at 1:1 — bar present, filling ~34%.

### END — endcard illegible, then upscaled — FIXED (two separate causes)

**Found (a).** The endcard's handle rendered at ~5% of frame width — unreadable.

**Root cause (a).** `shorts.py`'s `find_serif()` probes only macOS and Linux font
paths and returns `None` on Windows. `ImageFont.truetype(None, size)` then raises,
and the bare `except` falls back to `ImageFont.load_default()` — a fixed ~11px
bitmap font that **ignores the size argument entirely**. The failure is silent.

**Found (b).** `endcard_png()` builds from module constants `W, H = 1080, 1920`,
so compiling at `--height 3840` upscaled the card 2× (compile.py warned).

**Fix.** The endcard was regenerated at native 2160×3840 using the toolkit's own
bundled **EB Garamond** (`runtime/fonts/EB_Garamond/`) — which is both available
on this platform and more on-brand than the Georgia/DejaVu the helper looks for.
Layout, colours and proportions are otherwise identical to `shorts.py`'s. Handle
now spans 55% of frame width.

## Checked and passing

| Beat | Portrait note |
|---|---|
| B00 | Genuinely re-banded — composer card full-width, ask wraps to 4 lines, output lines and folder chip below |
| B01 | Corrected BLUF complete and on screen before the 11.0s cut |
| B02 | Topics list legible at 8s; collapses to one averaged band + one vector dot; meter restored |
| B03 | Failure cards stack (smaller-chunk failure above, larger below); legible at 1:1 phone scale |
| B05 | Three panels stack full-width; all three cut types render; the severing rule and drop line survive; redraw caption present |
| B08 | Rows re-flow to stacked marker/label/outcome; question pinned; only the winning row accented |
| BHTF | Prompt re-flows to 8 lines at a comfortably larger relative size than landscape |
| BOUT | Title, `@VedanshuDaxeshPatel`, signature, terracotta stop |
| END | Handle, terracotta hairline, "Full video: overlap, tooling, the verdict." |

**Type size at true phone scale.** Checked against a native 1080-wide crop rather
than a downscaled preview: body text lands ~22px, card headings ~28px, axis
labels ~20px. Comfortable for mobile. No further type changes were needed — an
earlier concern about the `Chunk*916` beats being undersized was an artifact of
judging a shrunken preview, and was withdrawn after measuring.

## Compiler warnings — reviewed, all three accepted

1. **`SKIN LINT: B00 … cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants
   ClaudeComposerAsk`** — false positive. The linter matches the landscape
   composition id; `916` twins are exactly what RENDER-TARGETS.md §3 requires of
   a vertical cut.
2. **`SKIN LINT: END … outro is 'un-annotated' — OUTRO LAW wants
   ClaudeTitleOutro`** — false positive. `END` is the silent branded endcard the
   Shorts law mandates, and it follows BOUT, which *is* the title restate.
3. **`'remotion' carries 8/9 beats (88%) — over the ~40% pantry cap`** —
   accepted, same reasoning as the landscape master: that cap governs vox
   mixed-media films, and VOX LAW is explicit that a film whose evidence is text
   and diagrams should have zero vox beats.

## Known coupling (Windows)

`shorts.py` symlinks the parent's mp3s into `short/mp3/`, which fails on Windows
without elevated privileges (`OSError 1314`). They were **copied** instead. The
short's audio is therefore a snapshot, not a link: **if parent narration is
regenerated, re-copy `mp3/beat-*.mp3` into `short/mp3/`** or the short will
silently keep the old takes.

Also note `remotion_scenes.py` rewrites the beat sheet when it finishes — editing
the sheet while a render is in flight loses the edit. (That happened once here to
B01's `fontSize` and was caught by re-reading the file after writing.)

## Verdict

**PASS** — 2160×3840, 2:31, 9/9 slots filled, zero slates, zero BLOCKER, zero
MAJOR. Four portrait-only defects found by reading frames; all four fixed and
re-verified.
