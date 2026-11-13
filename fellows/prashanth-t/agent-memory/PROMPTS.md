# PROMPTS — agent-memory

Beat-prefixed prompts for open slots.

## There are no open slots

All 14 beats are filled by already-registered deterministic Remotion scenes (see
`SHOTLIST.md`). Nothing is a placeholder slate, a pantry request, or a request for
human-supplied media. GATE F requires the paperwork set to be complete before any
render, and "no open slots" has to be written down rather than assumed.

## ASK→RESULT prompt shown on screen (B06 → B07)

ASK→RESULT LAW requires the generated figure at B07 to be preceded by the actual
prompt that produces it. Verbatim, as typed into the composer at B06:

```
B06: Trace one saved fact from the store back into the next request.
     Show what gets searched and what gets pasted in.
```

Its result is B07 — the store feeding one retrieved line into the next request.
The pair reads as a receipt: the ask, then what it produced.

## Viewer handoff prompt (BHTF)

HANDOFF LAW requires an interesting prompt that extends the episode into the
viewer's own work, read aloud verbatim and then discussed. Shown and spoken:

```
BHTF: I am building an assistant that should remember things about me between
      sessions. List exactly what it should save, where it should save it, and
      the retrieval query it would run at the start of each new chat.
```

Paired with the three-point rubric rendered beside it, which is what makes the
task scaffolded rather than open-ended:

1. does it separate what lives in context NOW from what lives in the store?
2. does it name a real retrieval query, or just say "search"?
3. would you consent to everything on that save list being written down?

## If a slot is ever opened

Should a later pass replace an illustration beat with human media, the prompt
belongs here prefixed with its beat id, and the slot contract applies: drop the
replacement in as `media/<BEAT_ID>.mp4` (or `.png`) and rebuild without touching
the edit.
