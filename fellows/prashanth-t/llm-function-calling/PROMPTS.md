# PROMPTS — llm-function-calling

Beat-prefixed prompts for open slots.

## There are no open slots

All 14 beats are filled by deterministic Remotion scenes (see `SHOTLIST.md`).
Nothing in this reel is a placeholder slate, a pantry request, or a request for
human-supplied media, so there is no open-slot prompt to carry here.

This file exists because GATE F requires the paperwork set to be complete before
any render, and "no open slots" is an answer that has to be written down rather
than assumed.

## ASK→RESULT prompt actually shown on screen (B06 → B07)

ASK→RESULT LAW requires the generated figure at B07 to be preceded by the real
prompt that makes it. This is the prompt typed into the composer at B06, verbatim
as it appears in the beat sheet:

```
B06: Trace the Boston weather question through all four steps.
     Show the exact payload at each one.
```

Its result is B07 — the same `FnCallLoop` figure from B04, now carrying a payload
chip on each of the four stages. The pair reads as a receipt: the ask, then what
it produced.

## Viewer handoff prompt (BHTF)

HANDOFF LAW requires an interesting prompt that extends the episode into the
viewer's own work, read aloud verbatim and then discussed. Shown and spoken:

```
BHTF: Describe one task at my job that needs live data. Then write a tool
      definition for it — name, description, and arguments — and show me the
      exact request you'd emit for one real example.
```

Paired with the three-point rubric rendered beside it, which is what makes the
task scaffolded rather than open-ended:

1. does the description say **when** to use the tool, not just what it does?
2. are the arguments things your program can actually supply?
3. is the request valid for your own example?

## If a slot is ever opened

Should a future pass replace an illustration beat with human media, the prompt
belongs here, prefixed with its beat id, and the slot contract applies: drop the
replacement in as `media/<BEAT_ID>.mp4` (or `.png`) and rebuild without touching
the edit.
