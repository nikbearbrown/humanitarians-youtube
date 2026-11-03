# PROMPTS — madison-archetype-progress

Beat-prefixed prompts for open slots.

## There are no open slots

All 14 beats are filled by already-registered deterministic Remotion scenes (see
`SHOTLIST.md`). Nothing is a placeholder slate, a pantry request, or a request
for human-supplied media. GATE F requires the paperwork set to be complete before
any render, and "no open slots" has to be written down rather than assumed.

## ASK→RESULT prompt shown on screen (B06 → B07)

ASK→RESULT LAW requires the generated figure at B07 to be preceded by the actual
prompt that produces it. Verbatim, as typed into the composer at B06:

```
B06: Read this brand's copy and its pricing as two separate signals.
     Name the archetype each one points to, and what the gap costs.
```

Its result is B07 — the two-branch figure resolving on the cost of the gap. The
pair reads as a receipt: the ask, then what it produced.

## Viewer handoff prompt (BHTF)

HANDOFF LAW requires an interesting prompt that extends the episode into the
viewer's own work, read aloud verbatim and then discussed. Shown and spoken:

```
BHTF: Take a brand I name. Quote five lines of its actual published copy and
      describe three of its actual visuals. Then argue a primary AND a
      secondary archetype from that evidence alone — and name where the two
      contradict each other.
```

Paired with the three-point rubric rendered beside it, which is what makes the
task scaffolded rather than open-ended:

1. does it quote real copy, or just describe vibes?
2. does it commit to a SECOND archetype, not just one?
3. is the contradiction it names something you could act on?

This handoff has the viewer run the method **by hand**, which is the honest thing
to offer while the tool itself does not exist.

## If a slot is ever opened

Should a later pass replace an illustration beat with human media, the prompt
belongs here prefixed with its beat id, and the slot contract applies: drop the
replacement in as `media/<BEAT_ID>.mp4` (or `.png`) and rebuild without touching
the edit.
