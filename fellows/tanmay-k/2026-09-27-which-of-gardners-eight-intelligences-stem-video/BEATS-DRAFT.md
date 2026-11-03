# BEATS — structure, decisions, runtime

**Draft 2: EIGHT ROOMS**, 2026-09-26. `build_beat_sheet.py` generates `beat_sheet.json`, so edit the
script, not the JSON. Draft 1 (three-questions) is archived in `_superseded/draft1-three-questions/`.

**Current state:** 19 beats · 1,087 narration words · ~5:29 estimated at 3.3 words/s (measured on
Week 23's `am_onyx` audio). No audio yet. B11 and B14 rendered as component QC only; they'll be
re-rendered against measured audio.

**Working title:** *Which of Gardner's Eight Intelligences Can a Machine Do?* The outro card reads
"Eight rooms. Six lights. One door ajar."

---

## Why the structure changed

Tanmay, 2026-09-26: most previous films use a "three questions" style device, and this one should
be different and unique to itself. A survey of Weeks 17–23's beat sheets confirmed the pattern.
Almost every film runs *hook → intro → numbered-question framework → worked examples →
twist/cool-down → "your turn" apply-the-questions → outro* (Week 17 four questions, Week 18 four
questions, Week 21 two, Week 22 three, Week 23 checklist). Draft 1 of this film was the same
skeleton again.

**Draft 2 drops all of it:** no numbered framework, no checklist, no "your turn" rubric.

## The shape: EIGHT ROOMS

The structure *is* the subject. Gardner's list becomes the film's chapters, so this shape can't be
reused for another topic.

- **The house** = the theory. **Rooms** = intelligences. **A light** = Gardner's own writing says a
  machine does what the room is for. **Door ajar** = evidence offered, light withheld. **Dark on
  purpose** = the word judged not to apply.
- One metaphor held end to end, including B07 ("this light may have been on since before the house
  was built") and B16 ("who holds the keys").
- **Momentum:** six rooms light in quick succession (B06–B11, ~1:15 total, beats get shorter as the
  count builds) so the viewer expects eight.
- **The turn (B12–B13):** before the last two doors, the film checks *how* the lights were earned.
  The six came on under a new, performance-style inspection, not the 1983 one. That reframes the
  count the viewer just watched.
- **The two last rooms:** B14 door ajar (evidence given, "one should be more cautious"), B15 dark on
  purpose ("category error").
- **Coda:** B16 "cannot / should not" and B17 "optional" against the base essay's "not obsolescence".
- **Ending:** not a checklist. A single open question to the viewer about room seven, the one the
  source itself leaves open.

## Tone arc

| Beat | Act | Intended state |
|---|---|---|
| B01 | COLD OPEN | curious |
| B02 | THE PLAN | warm, clear (subject in plain words, PLAYBOOK §1c) |
| B03 | THE HOUSE | explanatory |
| B04 | SURVEYOR'S NOTE | honest, measured (the *g* caveat) |
| B05 | THE WALKTHROUGH | turning |
| B06 | ROOM 1 | brisk |
| B07 | ROOM 2 | double-take (1956) |
| B08 | ROOM 3 | surprised (chess filed under spatial) |
| B09 | ROOM 4 | brisk |
| B10 | ROOM 5 | disbelief (the body) |
| B11 | ROOM 6 | peak, "multiply intelligent!" |
| B12 | THE INSPECTION | "But hold on", pulling back |
| B13 | THE NEW INSPECTION | quiet realisation |
| B14 | ROOM 7 | slower, genuinely unsure |
| B15 | ROOM 8 | still |
| B16 | THE KEYS | reflective, firmer |
| B17 | OPTIONAL | warm, unhurried |
| B18 | THE DOOR | direct, inviting |
| B19 | OUTRO | warm |

First-person lines mark real turns only: B01, B08, B10, B12, B13, B14.

## Structural differentiation (vs. this fellow's own films)

| Device in earlier films | Present here? |
|---|---|
| Numbered question framework (W17, W18, W21, W22, W23) | **no** |
| "Your turn" apply-the-rubric CTA | **no.** A single open question instead |
| Witnesses (W22), lineage (W23), instrument readings (W20) | **no** |
| Two side-by-side columns (W18) | **no.** Grid plan only |
| Chapters defined by the subject's own taxonomy | **new in this film** |

## New component: `EightRooms` (brutalist.art, local, uncommitted)

- `runtime/remotion/src/scenes/EightRooms.tsx`, registered as `EightRooms` and `EightRooms916` in
  `Root.tsx`; `./art scene-index` re-run, and `./art scenes --check` reports both RENDERABLE
- Library-first check run (`./art scenes`): the nearest candidates were mascot showcase grids and a
  fixed 3×3 brand matrix, none with per-cell state or portrait variants. A genuine gap
- Dual-aspect from the first line: 4×2 landscape, 2×4 portrait, all sizes are fractions of the frame
- Neutral defaults ("Room 1…"), so a forgotten prop can't leak another film's copy
- Timing is absolute seconds. `revealAtSeconds` and `captionAtSeconds` are **computed by the
  builder from a cue phrase in the narration**, so each light comes on as its evidence is spoken.
  Rescale to measured audio after Kokoro runs
- Accent grammar: terracotta marks only the focus room

**Component QC (frames actually viewed, `_qc/`):**
- First render: the heading "Six of eight" was visible before room six lit (spoiler), all six lamps
  were terracotta (accent diluted), and the light came on ~3s before "Light on" was spoken. All
  three were fixed
- Re-render: at B11 5.0s the heading reads "Room 6 · Naturalist", only the focus room carries the
  accent, and the caption is hidden. At 11.0s the "multiply intelligent!" caption is visible. B14
  at 13.0s shows the door-ajar wedge and the evidence caption, legible
- Not yet checked: the 9:16 variant (it renders via `shorts.py` once the long form is done)

## Read-through log (PLAYBOOK §1e), draft 2

1. B06 dropped words from inside a quote without an ellipsis. Re-cut to "clearly exhibit the signs"
   + unquoted remainder
2. B07 "Gardner's own history" → "the authors' own history" (the paper is co-authored)
3. B14 "that's a pass" → "as I read it, that looks like a pass" (the paper never scores it)
4. B16 "a sentence about the whole house" overstretched the metaphor. The Feb 2026 sentence isn't
   about the intelligences. It's now "stepped back from the rooms altogether"
5. B12 "needed" → "had to meet" (matches the paper's "fulfill eight specified criteria")

## Boundaries held (unchanged)

Chinese Room (Week 23), schools/curricula (C27), Visser loadings, "nine intelligences". See
`FACTCHECK.md` → Rejected.

## Shots

| Beat | Pattern | State |
|---|---|---|
| B01 | ClaudeComposerAsk | props set, every default overridden |
| B02, B03, B06–B11, B14, B15, B18 | **EightRooms** | props set; reveal/caption timed to cue phrases |
| B12, B13, B17 | ClaudeArtifactCardFull | props set |
| B19 | ClaudeTitleOutroFull | props set |
| B04, B05, B16 | STILL (screenshot) | **PLANNED: capture needed** (Davis et al. Part 2; MI Oasis 2024 header; Gardner Feb 2026 blog) |
