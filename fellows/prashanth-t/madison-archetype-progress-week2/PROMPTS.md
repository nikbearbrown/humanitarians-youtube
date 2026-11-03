# PROMPTS — madison-archetype-progress-week2

Beat-prefixed prompts for open slots.

## There are no open slots

All 14 beats are filled by already-registered deterministic Remotion scenes (see
`SHOTLIST.md`). Nothing is a placeholder slate, a pantry request, or a request for
human-supplied media. GATE F requires the paperwork set to be complete before any
render, and "no open slots" has to be written down rather than assumed.

## ASK→RESULT prompt shown on screen (B05 → B06)

ASK→RESULT LAW requires the generated figure at B06 to be preceded by the actual
prompt that produces it. Verbatim, as typed into the composer at B05:

```
B05: Sketch the scored output for one brand against the Ruler trait profile.
     Every score must carry the line of copy it came from.
```

Its result is B06 — the planned scored output with an evidence quote under every
trait. The pair reads as a receipt: the ask, then what it produced. Note the result
is explicitly a **design target**, not detector output.

## Viewer handoff prompt (BHTF)

HANDOFF LAW requires an interesting prompt that extends the episode into the
viewer's own work, read aloud verbatim and then discussed. Shown and spoken:

```
BHTF: Pick a brand with a strong personality. Quote five lines of its actual
      published copy, then score it against one archetype — giving the exact
      line of evidence behind every single score.
```

Paired with the three-point rubric rendered beside it, which is the same
auditability standard the design itself is built on:

1. does every score cite a real quote from the copy?
2. could someone disagree with a score and point at the reason?
3. did it score the brand's VOICE, or just the obvious keywords?

## If a slot is ever opened

Should a later pass replace an illustration beat with human media, the prompt
belongs here prefixed with its beat id, and the slot contract applies: drop the
replacement in as `media/<BEAT_ID>.mp4` (or `.png`) and rebuild without touching
the edit.
