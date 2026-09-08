# PROMPTS — `yatra-nobody-wrote-this`

## Open slots

**None.** Every beat is machine-rendered from `beat_sheet.json`. There is no
image to source, no clip to generate, no pantry item to shop for, and no
Higgsfield beat — this reel runs entirely on the free path (Kokoro + Remotion +
ffmpeg). Nothing here is a request to a human.

This file therefore records the prompts the reel SHOWS, which are the ones that
have to be exact.

## The prompts that appear on screen

These are rendered into the composer beats, so they are copy, not instructions —
changing them here changes the video.

### B00 — the cold-open ask

```
How much of what I read on LinkedIn is actually written by AI? Give me measured
numbers across platforms, not vibes — and tell me whether people are lightly
editing with AI or handing the whole post over.
```

Result lines shown beneath it (COLD OPEN LAW — the ask lands answered):

```
41% of long-form LinkedIn posts are fully AI-generated
the highest share of any platform in the study
and it is all-or-nothing — almost nobody edits
```

### B04 — the ask micro-beat (ASK→RESULT LAW)

The reel's one mid-body ask. This is the ACTUAL generation prompt behind B05's
chart, which is the point of the law: the interface is a receipt, not decoration.

```
Chart all five platforms from the scan side by side, sorted high to low, values
printed verbatim with their ranges intact, and mark the cross-platform average
as a reference line.
```

`runningText: "sorting five platforms…"`, `output: []` — the result is B05.

Note "with their ranges intact": the instruction that keeps `25–29%` and `4–13%`
from being flattened to single numbers on screen is visible in the prompt the
viewer reads.

### B12 — the handoff prompt (HANDOFF LAW)

Read aloud verbatim in the narration, then discussed, then handed over.

```
Take my last 10 LinkedIn posts. For each, tell me which parts only I could have
written — a specific number, a name, something that went wrong — and which parts
any model would produce from the same prompt. Then rewrite the weakest one using
only what is unrepeatable.
```

The rubric that makes it a SCAFFOLDED task rather than "ask Claude about X":

```
grade it: does it point at facts only you have?
grade it: does it cut the lines any model could write?
grade it: is the rewrite shorter AND more specific?
```

## Why this prompt, for the handoff

It extends the episode's argument into the viewer's own work instead of asking
them to go read more. The reel's finding is that LinkedIn writing has become
all-or-nothing; the prompt makes the viewer run the same classification on
themselves, and the "only I could have written" test is the operational version
of the thesis — the unrepeatable specifics are exactly what a model cannot
produce from the same brief. The rewrite step turns the audit into an artifact.
