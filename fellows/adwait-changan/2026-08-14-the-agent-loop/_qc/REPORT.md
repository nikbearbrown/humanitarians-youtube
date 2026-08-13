# VISUAL QC REPORT — Episode 2, "The Agent Loop"

VISUAL QC LAW. Contact sheet plus per-beat frames at 50 %, 90 % and 95 % of each beat's
span, read as PNGs. Frames in `_qc/frames/`. Contact sheet: `../qc-sheet.png`.

## Defects found and fixed

### D1 — B03 · a terminal trace rendered as a numbered list · **MAJOR** · FIXED

`ClaudeWindow` numbers every `artifactLine` unconditionally, so the printed
THOUGHT / ACTION / OBSERVATION trace came out as **"1. 2. 3. 4."** — implying four ordered
steps where the source has three moves plus an alternative rendering of the third. The
component also collapsed the run of spaces that aligns the trace's columns, and set it in
UI sans, so it did not read as program output at all.

*Fix (toolkit edit, backwards compatible):* added an optional `numbered` prop to
`runtime/remotion/src/scenes/ClaudeWindow.tsx`, default `true`. When `false`, the number
span is not rendered, the lines set in the mono face, and `whiteSpace: 'pre'` preserves the
column alignment — i.e. a log looks like a log. B03 now passes
`numbered: false, width: 1620, fontSize: 26`. Verified in `_qc/frames/B03_fixed.png`.

### D2 — B03 · canvas underfill · **MAJOR** · FIXED

Same root cause as Episode 1 D3: `ClaudeWindow` declared `width` / `fontSize` in its schema
but never read them, hardcoding 1100 px and 19 px. Fixed in the component (see Episode 1's
`_qc/REPORT.md` D3 for the full write-up); B03 now renders at 1620 px with 26 px mono.

### D3 — B07 · underfill, and the episode's punchline was told rather than shown · **MAJOR** · FIXED

`MedhavyConceptCard` rendered a small centred card (~30 % of frame height) containing a
run-on paragraph, on the beat that carries the episode's whole argument — *"one guess,
repeated eight times."* The viewer was asked to take that on the narrator's word.

*Fix:* extended `trace_loop.py` with `run_lazy()`, which drives the real loop with the lazy
recorder, and **ran it**. Because a lazy observation carries no tool name, `think_names()`
cannot tell what has already been tried and selects the same call every pass — the
repetition is a consequence of the mechanism, not a mock-up. B07 is now a `ClaudeWindow`
log showing the eight identical passes and `stopped: step budget exhausted`, verbatim from
that run. It fills the frame, and the claim is now demonstrated rather than asserted.
FACTCHECK rows 8 and 9 upgraded from "accurate" to **verified by execution**; SOURCES.md
carries the captured output. Verified in `_qc/frames/B07_fixed.png`.

*Note:* this fix also removed the last consecutive-pattern risk — B06 (code) → B07 (window)
→ B08 (chips) now alternate cleanly.

## Checked and passed

| Beat | Finding |
|---|---|
| B02 | Settles correctly — all three feeds check in, "Only one is reality." lands in terracotta at 95 %. The 50 % frame showed two of three feeds; sampling, not a defect. |
| B05 | Three layers, accent on "What went wrong", caption anchors the bottom. Good fill. |
| B06 | Code matches `trace_loop.py` character-for-character. Counted the rendered lines to confirm the narration's "the comment on line five" — `except Exception as err:  # the error IS the observation` is line 5. Claim verified against the frame, not the file. |
| B08 | All four chips land by 95 %; "False completion" reads clearly. |
| B09 | Three stopping rules, accent on the explicit done-check. |
| BVDT | Five verdict lines inside the card, no overflow. |
| B00 / BHTF | Composer legible; typing confined to these two beats per HANDOFF LAW. |
| BOUT | Title, handle, subline inside the title-safe inset; "Episode 2 of 10" present. |

## Rubric audit (9 points)

| Point | Result |
|---|---|
| Edge bleed / clipping | PASS. |
| Title-safe margins | PASS — widest element is B07 at 1620 px, inside the 1728 px safe span. |
| Container overflow | PASS — B07's nine log lines and B03's four trace lines both sit inside their cards with the mono set at 24–26 px. |
| Collision | PASS. |
| Offscreen anchors | PASS. |
| Legibility | PASS after D1–D3. |
| Brand bug | `@HumanitariansAI` chip on B00/BHTF, full handle on BOUT — consistent with Episode 1 and the previously shipped reel. |
| Aspect | PASS — 16:9 throughout. |
| Canvas fill | PASS after D2/D3. B01/B04 act cards keep deliberate negative space (12–14 s breathing beats). B06's code panel has empty space below the seven code lines — the `ClaudeCodeBeat` panel is a fixed-height terminal frame; accepted as the component's house look, same as Episode 1's B06. |

## Accepted, not fixed

- **`lane histogram: remotion 13/13 (100 %)` warning** — as Episode 1. The ~40 % cap is
  `deep-explainer` pantry/vox doctrine; this is an `ai-explainer` reel with no pantry
  stills, and every beat uses a distinct pattern rather than repeated wallpaper.
- **Two `ClaudeWindow` beats (B03, B07)** — separated by three beats, and both play the
  same deliberate role: *printed output of the file that ships with the episode.* The
  repetition is a rhyme, not wallpaper.

## Process note (worth keeping)

The first patch to this episode's `beat_sheet.json` was **silently clobbered**. The
background `remotion_scenes.py` run re-dumps the sheet when it finishes, and the patch was
written after the last `media/*.mp4` appeared but before the script's final dump. The beat
re-rendered with the old props and the defect survived a "fix". Caught only because the
verification frame was read rather than assumed.

*Rule:* wait for the render process to actually exit — not for its output files to appear —
before editing the beat sheet, and re-read the sheet after patching to confirm the write
survived.

## Verdict

> **Zero BLOCKER, zero MAJOR remaining.** 3 defects found, 3 fixed, 2 beats re-rendered
> (B03, B07). Build is clear for the clean master.
