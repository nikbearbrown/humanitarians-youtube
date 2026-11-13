# VISUAL QC — Lookup, Not Training

**Reel:** `claude-hai-lookup-not-training` · ai-explainer · claude-hai · Bella (`af_bella`)
**Date:** 2026-10-01

| Cut | File | Resolution | Duration | Slots |
|---|---|---|---|---|
| 16:9 master | `claude-hai-lookup-not-training.mp4` | 3840×2160 @30 | 207.18s (3:27) | 14/14, no slates |
| 9:16 short | `short/claude-hai-lookup-not-training-short.mp4` | 1080×1920 @30 | 151.70s (2:31) | 12/12, no slates |

---

## Sampling method — and a correction to how the previous reel was QC'd

The author asked for frames **near t=0 for every scene**, not just mid and end.
Doing that surfaced a problem with the sampling itself before it surfaced anything
about the video.

**`ffmpeg -ss <t> -i <file>` seeks on the input side, which snaps to the nearest
keyframe.** On a 4K H.264 master that can be *seconds* early. The first pass of this
QC produced a contact sheet where B11 showed B10's content, B12 showed B11's, and
the outro was never sampled at all — three beats mislabelled, and a real defect
hidden behind the mislabelling.

Every frame in this report is therefore taken by **exact frame index**
(`select=eq(n\,N)`), which cannot drift. That is also how the boundary sweep below
works.

> **This invalidates the sampling used on `claude-hai-one-sign-in-many-books`.**
> Re-running the exact-frame boundary sweep against that reel's master finds blank
> frames at **11 of its 13 beat boundaries**, up to 0.80s long — the same defect
> fixed here (see #1), which the keyframe-snapped sampling hid. That reel's other
> findings stand; this one was missed. Flagged to the author rather than silently
> re-rendering a delivered file.

## Defects found and fixed

| # | Sev | Where | Defect | Root-cause fix |
|---|---|---|---|---|
| 1 | **BLOCKER** | B10→B11, B11→B12 | **Blank frames between clips.** The shared `ClaudeVerdictArtifact` and `ClaudeComposerAsk` animate their window in from nothing, so a beat's first frames are an empty cream page. Measured by exact frame index: **0.50s of blank** at the verdict→handoff boundary, 0.13s at close→verdict. Reads as a hole in the cut. | The shared scenes are wrapped in `<Sequence from={-20}>` in `illustrations/haiKit.tsx`, starting them 20 frames "in the past" so their intro has already played at our frame 0. No shared component changed, so every other reel still renders identically. Outro gets `from={-10}` (shorter beat). **Re-swept: 0 of 13 boundaries now have blank frames.** |
| 2 | MAJOR | B10 | The loop was drawn at 0.3 opacity as "base geometry" — over a cream stage that measured **1.84% ink at frame 0** and read as an empty open, which is the exact defect the author's t=0 instruction targets. | Base opacity 0.3 → 0.58, unlit borders darkened, gain cards 0.25 → 0.55. Now 13.24% at frame 0. |
| 3 | MAJOR | B03 | The passage column was an empty void at t=0 — the scene was half-dressed. | Each passage slot now renders as an empty dashed placeholder at p=0 and the passage lands into it. |
| 4 | MINOR | all body beats | The spark line faded up from opacity 0, so every scene's only title was invisible at frame 0. | `HaiStage` now starts it at 0.6 and settles to 1 over the first 2%. |
| 5 | MINOR | subtitles | The one phrase the author wants landed cleanly wrapped mid-phrase: `It's an open-book exam, not a study / session.` | `make_srt.py`'s `wrap()` rewritten to score candidate breaks — balance, plus a bonus for breaking after punctuation and a penalty for orphaning a short word. Now breaks at the comma. |
| 6 | MINOR | short / endcard | `shorts.py` hardcodes `dark=True`, so the silent endcard rendered near-black — wrong for a fidelity palette whose point is the Claude app's cream page. | Regenerated via the same `endcard_png(..., dark=False)`; ground pixel verified `(243,235,221)`. `shorts.py` untouched — dark is correct for the teardown brands. |

**Remaining: zero BLOCKER, zero MAJOR.**

## Opening-state audit (the author's t=0 requirement)

Ink coverage at t+0.12s of every beat, measured against **each frame's own ground**
(illustration beats sit on `#F2F0E9`, UI beats on `#FAF9F5`, so a single reference
colour gives nonsense):

| Beat | 16:9 | 9:16 | Opens dressed? |
|---|---|---|---|
| B00 ASK | 2.0%¹ | 4.4% | yes — chrome, eyebrow, title, greeting, composer card, footer all present |
| B01 | 13.5% | 9.0% | yes — book, dashed arrow + label, model slab |
| B02 | 21.1% | 13.1% | yes — model card with three empty fact rules |
| B03 | 9.9% | 7.1% | yes — question, ruled book, empty passage slots |
| B04 | 13.4% | 13.3% | yes — question, passage stack, ellipsis, model slab |
| B05 | 21.8% | 15.9% | yes — ledger, chapter card with the wrong line, answer card repeating it |
| B06 | 42.0% | 34.2% | yes — both columns framed, headed, each holding the answer |
| B07 | 11.5% | 5.7% | yes — ledger, both cost rows labelled, bars at zero |
| B08 | 20.5% | 15.9% | yes — book, empty index cabinet with ruled slots, trigger chip |
| B09 | 22.1% | 15.0% | yes — book and index **in step**, matching revision stamps, answer card |
| B10 | 13.4% | — | yes — the whole loop drawn, waiting to be lit |
| B11 VERDICT | 45.3%² | — | yes — artifact page open, line one written |
| B12 HANDOFF | 2.1%¹ | — | yes — composer, greeting, prompt already typing |
| B13 OUTRO | 5.7% | 3.6% | yes — title set |
| END | — | 1.8%³ | yes — the silent endcard is genuinely sparse by design |

¹ The composer beats are thin dark type on a cream page; low ink is correct, and the
frames were read to confirm the chrome is all present. ² Was 0.09% (blank) before
fix #1. ³ Two short text lines on a 1080×1920 cream card; inspected, not a defect.

**No scene opens empty, in either cut.**

## Boundary sweep (exact frame index, ±0.8s around every cut point)

| Cut | Boundaries | With blank frames |
|---|---|---|
| 16:9 | 13 | **0** |
| 9:16 | 11 | **0**¹ |

¹ The automated pass flagged B13→END; inspection shows that is the silent endcard's
own low ink crossing a 2% threshold, not a hole.

## Rubric sweep

| Point | 16:9 | 9:16 |
|---|---|---|
| Edge bleed / clipping | pass | pass |
| Title-safe margins (5% inset) | pass | pass |
| Container overflow | pass | pass |
| Collision | pass | pass |
| Offscreen anchors | pass — B07's self-host bar runs past the frame edge **by design**, and carries an arrow marker so it reads as deliberate | pass |
| Legibility | pass | pass |
| Brand bug placement | pass — every beat; full-size on the outro | pass |
| Aspect | 3840×2160 throughout | 1080×1920 throughout |
| Canvas fill | pass (fixes #2, #3) | pass |
| **Opening state at t=0** | pass (fixes #1–#4) | pass |

## Accepted, with reasons

- **SKIN LINT on B00 / B13.** `compile.py` matches on composition *name* and warns
  that the cold open is `ClaudeHaiLookupAsk` rather than `ClaudeComposerAsk`. Both
  are thin wrappers that render exactly those shared components plus the LOGO LAW
  bug and the preroll from fix #1. COLD OPEN LAW and OUTRO LAW are met in substance.
- **`chapters.py` splits `--names` on commas**, so a chapter label cannot contain
  one — "The model is rented, not built" silently became two names and the script
  exited `got 14 names for 13 chapters`. Renamed rather than patching the script.
- **`lead_silence_s: 0.5` on B11 is inert** in this toolkit — nothing reads it.
  Harmless, left in the sheet as authoring intent. It was *not* the cause of the
  blank frames (that was fix #1).

## Author's hard constraints — verified on the built artefacts

| Check | 16:9 | 9:16 |
|---|---|---|
| "RAG" / "embeddings" / "vector search" / "retrieval-augmented" **spoken** | **0** | **0** |
| …**on screen** (props, card text) | **0** | **0** |
| …**in the subtitle file** | **0** | **0** |
| "open-book exam, not a study session" spoken | **exactly 1** | **exactly 1** |
| Any `<number> checks/steps/stages/passages` phrase | **0** | **0** |
| "by default" hedge on the reindex claim | present, spoken **and** on screen | present |

The count discipline is also enforced in the component source: `PassagePull` and
`HandedTogether` render a trailing ellipsis card with their passage group, so three
drawn cards read as "a handful" rather than asserting a number no source supports.

## Chapters

Run **before** `description.txt` was written, against measured `actual_duration_s`:

```
python3 chapters.py --sheet beat_sheet.json --names "…"
→ 13 chapters, shortest 11.86s — valid
  [ok] first chapter starts at 00:00      [ok] timestamps ascending
  [ok] at least 3 chapters                [ok] chapter total == reel length
  [ok] every chapter >= 10s               [ok] no two chapters share a timestamp
```

B13 (4.05s) cannot stand alone — one sub-10s chapter silently disables the whole
list on YouTube — so the script merged it forward into B12. That is why the final
chapter is "Your turn" at 2:52 running 34.64s.

## Subtitles

| Cut | Cues | Coverage |
|---|---|---|
| 16:9 | 81 | 0.00–206.80s of 207.18s; **all 14 beats have cues**, bookends included (B00 5, B11 6, B12 11, B13 2) |
| 9:16 | 59 | 0.00–146.88s of 151.70s; the 4.8s tail is the deliberately silent endcard |

Zero overlapping cues in either file. Timings come from `mp3/words.json`
(faster-whisper word alignment over the Kokoro mp3s) offset by the running sum of
measured beat durations — the same clock the video is cut on.
