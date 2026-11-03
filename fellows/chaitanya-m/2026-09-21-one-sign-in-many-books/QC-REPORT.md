# VISUAL QC — One Sign-In, Many Books

**Reel:** `claude-hai-one-sign-in-many-books` · ai-explainer · claude-hai · Bella (`af_bella`)
**Date:** 2026-09-21
**Method:** frames sampled with ffmpeg at 15% / 50% / 85% of every beat's measured
span (42 frames for the 16:9, 24 for the 9:16), contact-sheeted, and **read**.
The ffprobe duration/resolution numbers below are a FILE check and do not count as QC.

| Cut | File | Resolution | Duration | Slots |
|---|---|---|---|---|
| 16:9 master | `claude-hai-one-sign-in-many-books.mp4` | 3840×2160 @30 | 208.15s (3:28) | 14/14, no slates |
| 9:16 short | `short/claude-hai-one-sign-in-many-books-short.mp4` | 1080×1920 @30 | 160.12s (2:40) | 12/12, no slates |

Frames: `_qc/frames/` · contact sheet: `_qc/qc-sheet.png` (and `short/_qc/`).

---

## Defects found and fixed

Each was fixed at the root — in scene source or beat-sheet data — and re-rendered.
No defect was papered over at compile.

| # | Sev | Beat | Rubric point | Defect | Root-cause fix |
|---|---|---|---|---|---|
| 1 | MAJOR | B10 | collision | The three mechanism chips (TICKET · CALL BACK · TIMESTAMP) were pinned bottom-centre in an HTML layer; "TIMESTAMP" rendered **on top of the Immunology site card**. | Moved into the SVG viewBox and stacked under the hub, where no card can reach. `ClaudeHaiTicketIllu.tsx` |
| 2 | MAJOR | B04 | container overflow | The ticket identifier wrapped onto a second line and ran **under the seal**, which also obscured the seal's own label. | Stub widened to 1440, text column capped at 55% so the seal owns the right quarter, `whiteSpace: nowrap` + ellipsis, and a shorter placeholder id. |
| 3 | MAJOR | B05 | canvas fill | Both comparison cards were ~65% empty — two list items under a header over a sea of white. | The `show` block's two-stub sort (specified but never implemented) was built: two identical stubs arrive, the hub marks them ✓/✗, the textbook can only mark ?/?. Fills the card *and* delivers the beat. |
| 4 | MAJOR | B01 | edge clipping | With the fan at full spread the top site card's chrome bar was clipped above the viewBox. | Column pitch 236→215 and centre 400→440, so all four cards sit inside the 880-high viewBox. |
| 5 | MAJOR | B01 | collision | The gap caption ran underneath the last site card. | Moved into the SVG as a text node anchored under the hub. |
| 6 | MAJOR | B06 (9:16) | canvas fill | Portrait stretches the checklist panel down the tall axis; the six rows stacked under the header leaving the bottom half empty. | `justifyContent: center` + larger rows in portrait only. |
| 7 | MAJOR | END (9:16) | brand | `shorts.py` hardcodes `dark=True`, so the silent endcard rendered on a near-black ground — wrong for a FIDELITY palette whose whole point is the Claude app's cream page. | Regenerated via the same `endcard_png()` with `dark=False`; verified ground pixel `(243,235,221)`. `shorts.py` left untouched, since dark is correct for the teardown brands. |
| 8 | MINOR | B01/B02/B03/B07/B09 | canvas fill | First pass sized content for a 1280×720 stage; on 1920×1080 everything read timid with dead space. | Type and geometry scaled up across the component file; re-checked against the safe area. |
| 9 | MINOR | B02 | signalling | The answer word "ticket" was still typing at 92% — finishing *after* the voice said it. | Typing window moved to 0.68–0.84 so it lands on the spoken word. |
| 10 | MINOR | B02 | collision | The site's address label overlapped the door panel's inner rule. | Extra bottom inset on the panel. |

**Remaining: zero BLOCKER, zero MAJOR.**

## Accepted, with reasons

- **SKIN LINT on B00 / B13** — `compile.py` warns that the cold open is
  `ClaudeHaiTicketAsk` rather than `ClaudeComposerAsk`, and the outro
  `ClaudeHaiTicketOutro` rather than `ClaudeTitleOutro`. The lint matches on
  composition *name*. Both are thin wrappers that render exactly those shared
  components and add the LOGO LAW corner bug on top. Wrapping rather than editing
  the shared scenes keeps every other reel in the catalogue byte-identical on
  re-render. COLD OPEN LAW and OUTRO LAW are satisfied in substance.
- **B11 verdict card leaves vertical margin** — that is the shared
  `ClaudeVerdictArtifact`'s own proportion (a document card on a page). Changing it
  would re-flow every reel that uses it; out of scope for this build.
- **HAI bug overlaps card whitespace on B07/B06** — the bug sits inside the
  title-safe inset at 0.18–0.22 opacity and covers no text, mark, or figure in any
  sampled frame. LOGO LAW's "never covering content" is met.

## Rubric sweep (final frames)

| Point | 16:9 | 9:16 |
|---|---|---|
| Edge bleed / clipping | pass | pass |
| Title-safe margins (5% inset) | pass | pass |
| Container overflow | pass (fix #2) | pass |
| Collision | pass (fixes #1, #5, #10) | pass |
| Offscreen anchors | pass | pass |
| Legibility (≥24px effective) | pass — smallest sustained type is the 26–30px mono captions | pass |
| Brand bug placement | pass — every beat; full-size on the outro | pass |
| Aspect | 3840×2160 throughout | 1080×1920 throughout |
| Canvas fill | pass (fixes #3, #4, #6, #8) | pass (fix #6) |

## Author's hard constraints — verified on the built artefacts

Run over both compiled beat sheets (narration = what is spoken; props + card text =
what can reach the screen):

| Check | 16:9 | 9:16 |
|---|---|---|
| The banned token acronym, spoken | **0** | **0** |
| The banned token acronym, on screen | **0** | **0** |
| Competing metaphor (unlocking / travel-document / festival-band family) | **0** | **0** |
| Token-shaped string anywhere (`eyJ…`, `Bearer …`, `x.y.z`) | **0** | **0** |
| Any reference to the debug log file | **0** | **0** |

The only identifier rendered anywhere in either cut is on B04:
`TCKT-EXAMPLE-0000` → `TCKT-EXAMPLF-0000`, both invented, carrying the on-screen
caption *"example — not a real ticket"* for the beat's full duration. Confirmed by
reading the B04 frames at 15/50/85%, not by grep alone. The debug log was never
opened at any point in this build.

## Subtitles

| Cut | Cues | Coverage |
|---|---|---|
| 16:9 | 79 | 0.00–207.80s of 208.15s; **every one of the 14 beats has cues**, bookends included (B00 cold open 5, B11 verdict 5, B12 handoff 10, B13 outro 2) |
| 9:16 | 60 | 0.00–155.28s of 160.12s; the 4.84s tail is the deliberately silent endcard |

Zero overlapping cues in either file. Timings come from `mp3/words.json`
(faster-whisper word alignment over the Kokoro mp3s), offset by the running sum of
measured beat durations — the same clock the video is cut on, so captions cannot
drift from the edit.
