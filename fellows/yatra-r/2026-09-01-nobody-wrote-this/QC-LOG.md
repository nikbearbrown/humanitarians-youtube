# QC LOG — `yatra-nobody-wrote-this`

VISUAL QC LAW pass. The mp4 probe is a FILE check and never counts as QC, so
every beat below was inspected as a rendered PNG at ~92% of its own span (the
point where all of a beat's reveals have landed).

**Every one of the four defects found was invisible to the probe** — duration and
frame count were correct on all fourteen beats, before and after. They were
text-collision and overlap defects that only a look at the pixels can catch.

## Defects found and fixed (root cause in scene source, then re-rendered)

| Beat | Severity | Defect | Root cause | Fix |
|---|---|---|---|---|
| B02 | MINOR | Citation read `Source: Framing: Pangram Labs, …` — doubled colon | `source` prop carried its own `Framing:` prefix while `SourceLine` already prefixes `Source:` | Reworded the prop to `Pangram Labs, "AI in Your Feed," July 2026 (classification scheme)` |
| B06 | MAJOR | The dashed proportional reference struck straight through the label text, cutting the word "scanned" | One continuous rule spanned both bands **and** the gap between them, and the gap is where the first track's label sits | Split into two dashed segments, one per band, sharing the same `refX`. Still reads as a carry-down; collision gone |
| B07 | MAJOR | The dashed remainder band overlapped the citation line **and** the closer | Three 150px bands on a 236px step need 668px; only 604px exists between title and citation. Last band ran to y=972, citation sits at y=908 | Bands 150→118px, step 236→196px. Last band now ends at y=860 — 48px clearance |
| B10 | MAJOR | The date axis rule struck through "August 2, 2026" | Marker label at `AXIS - 34` with a 48px face straddles the rule at `AXIS` | Raised to `AXIS - 86`, fully above the rule |

B06's fix was applied to **both** orientations. B07's and B10's portrait variants
were checked and were already clear (250px step; marker below the axis).

Each fix carries an in-source comment naming the defect it prevents, so the
geometry is not silently reintroduced by a later edit.

### A process note worth keeping

The first re-render attempt used `--only B02 B06 B07 B10`. `remotion_scenes.py`
takes a **single** `--only` value, so it errored and rendered nothing — but the
shell reported **exit code 0** because the command was piped to `tail`. The
failure was caught only because the corrected frame was re-extracted and looked
at, and B07 was visibly unchanged. Re-run as four separate invocations.

Lesson: on this pipeline a zero exit status proves nothing. Verify the artifact.

## GATE V (automated) — clean master

```
Frames sampled: 28  ·  BLOCKER: 0  ·  MAJOR: 2
```

Both MAJOR findings are `underfill` on **B13**, the outro card, and both are
accepted:

- B13 is the stock `ClaudeTitleOutro` — title, terracotta period, handle, no
  subline — which is exactly what OUTRO LAW specifies. Its sparseness is the
  design, and FILL-THE-CANVAS LAW explicitly permits "deliberate negative space
  for emphasis."
- The same finding exists on the delivered reel
  `claude-liam-the-judgment-is-the-job` (its B09, also the outro). This is
  shared-component behaviour, not a regression introduced here.
- It reports 5% here vs 46% there because the locked `@NikBearBrown` outro
  carries a slug-seeded mascot while `@Yatra` reels get title-and-handle only —
  consistent with the two prior `@Yatra` reels.
- Not unilaterally changed: `ClaudeTitleOutro` is shared by every shipped reel,
  so enlarging it would retroactively alter delivered videos. Enlarging the
  outro is a deliberate, scoped decision for the channel owner.

### GATE V's 28 BLOCKERs were a false positive — recorded so it is not re-chased

Run against the reel folder, `final_frame_check.py` prefers `*-slate.mp4`, the
**review** cut. `compile.py` burns a running timecode onto the review cut at
`x=w-text_w-16 : y=16` — the top-right corner, deliberately outside the
title-safe inset. The gate's `BURN_IN_EXCLUDE` mask only covers the bottom-left
strip, so it flags its own review stamp as `edge-bleed` on **every** frame:

```
frames=28 BLOCKER=28   ← review cut  (the timecode)
frames=28 BLOCKER=0    ← clean master (--mp4 <slug>.mp4)
```

The same 100%-of-frames signature appears on the prior delivered reel
(`BLOCKER: 20` on 20 frames). It is a toolkit inconsistency, not a reel defect.
**Always point GATE V at the clean master**, or widen `BURN_IN_EXCLUDE` to
include the top-right timecode box.

The gate's safe-area maths is *not* at fault — `_safe_for()` scales SAFE by
`w/1920`, so it handles the 4K master correctly. That was ruled out before
concluding false positive.

## Per-beat inspection (manual, all 14)

| Beat | Scene | Verdict |
|---|---|---|
| B00 | ClaudeComposerAsk | clean — greeting, ask, terracotta send, three result lines |
| B01 | LnkBluf | clean — reframe performed; struck line replaced on the spoken beat |
| B02 | LnkFrame | fixed (citation), then clean — three empty bins, third reddened |
| B03 | LnkStat | clean — strongest frame in the reel; recommended thumbnail |
| B04 | ClaudeComposerAsk | clean — ask micro-beat, empty output (result is B05) |
| B05 | LnkLadder | clean — ranges intact, dashed 1-in-4 reference, LinkedIn sole accent |
| B06 | LnkDisproportion | fixed (dashed rule), then clean |
| B07 | LnkAllOrNothing | fixed (band geometry), then clean — 4.3% sliver vs 41% reads instantly |
| B08 | LnkContradiction | clean — drives stall on the terracotta marker |
| B09 | LnkFalsify | clean — three stress-tests with reasons, closer lands |
| B10 | LnkPressure | fixed (date marker), then clean — INTERPRETATION vs IN FORCE |
| B11 | ClaudeVerdictArtifact | clean — four lines, each with its citation |
| B12 | ClaudeComposerAsk | clean — prompt types as read aloud, rubric stacks |
| B13 | ClaudeTitleOutro | accepted underfill (see above) |

### Noted, not changed

`ClaudeVerdictArtifact` renders no corner brand bug, unlike the illustration
scenes, so B11 is the one beat without one. LOGO LAW asks for a bug on every
beat, but that composition is shared across every prior reel and all of them
shipped this way. Flagged as pre-existing rather than changed underneath
delivered work.

## The 9:16 vertical

`shorts.py` reported *under the cap → full reformat, no beats cut*: 15 beats
(14 + a 4.5s silent endcard), 172.9s. All 14 REMOTION beats were rewired to
their `916` compositions and **re-rendered portrait**, never centre-cropped —
a crop would have chopped the citation lines and the end-of-bar values, which
are load-bearing in this reel.

Portrait beats inspected as frames: B01 (BLUF reframe), B02 (bins), B05
(ladder — labels above bars, values right-aligned, ranges intact), B06 (fixed
dashed segments), B10 (tagged blocks + date axis). All clean on first render.
B07 and B10 portrait geometry was checked against the 250px step and confirmed
clear of the citation before rendering.

### DEFECT — wrong channel handle on the endcard (fixed)

**Severity: BLOCKER.** The compiled vertical ended on a card reading
**`@nikbearbrown`**. This reel is `@Yatra`.

Cause: `shorts.py` builds the endcard itself and takes the handle from
`--handle`, whose **default is `@nikbearbrown`**. It never reads the reel's own
`metadata.channel_handle`, so any non-Bear channel silently gets Bear's handle
stamped on its Short.

Fix applied here: regenerated `short/media/END.png` via `shorts.endcard_png()`
with `metadata.channel_handle` (asserted `== "@Yatra"`), corrected
`short/beat_sheet.json`'s `card.handle` so the sheet matches what was rendered,
deleted the stale `clips/END.mp4`, and recompiled. Verified in the compiled
mp4 at t=170.5s: the card now reads `@Yatra`.

**This bug is not confined to this reel.** The delivered reel
`claude-liam-the-judgment-is-the-job` has `"handle": "@Yatra"` on its outro beat
and `"handle": "@nikbearbrown"` on its endcard — i.e. its published vertical
very likely ends on the wrong channel too. Worth checking before it is promoted
further.

Recommended upstream fix (NOT applied — it changes shared tooling):
make `--handle` default to the reel's `metadata.channel_handle` and fall back to
`@nikbearbrown` only when absent.

### GATE V — vertical

```
Frames sampled: 30  ·  BLOCKER: 0  ·  MAJOR: 4
```

All four are `underfill`, two on B13 (the outro card — same accepted design as
the master) and two on END (the toolkit's own minimal endcard: a handle, a rule,
and dark ground by design). No action.

### SKIN LINT warnings on the vertical — both false positives

```
B00: cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
END: outro is 'un-annotated' — OUTRO LAW wants ClaudeTitleOutro
```

The lint matches composition names literally and does not know that `…916` is
the sanctioned portrait twin, nor that `shorts.py` appends its endcard after the
real `ClaudeTitleOutro916` outro (B13). The vertical's actual spine is correct:
cold open → BLUF → body → verdict → your turn → title restate → endcard.

## Honesty checks (the reason this reel exists)

Verified against the rendered frames, not just the beat sheet:

- Every figure on screen carries a visible citation: B02, B03, B05, B06, B07,
  B08 render `Source:` lines; B10 carries per-block citations; B11's four lines
  each cite inline.
- **No derived number anywhere.** The human-written share (100 − 41 − 4.3) does
  not appear. B07's remainder band renders dashed and empty with the label
  "the remainder, not published as a figure" — and `LnkAllOrNothing` has no
  prop that could carry a figure for it.
- Ranges render verbatim: `25–29%` and `4–13%` on B05, uncollapsed.
- B10's non-sourced claim is visibly tagged `INTERPRETATION` beside the dated
  fact tagged `IN FORCE`, so the frame does not imply a citation it lacks.
