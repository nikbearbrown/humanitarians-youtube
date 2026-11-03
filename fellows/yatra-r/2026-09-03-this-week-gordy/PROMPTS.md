# PROMPTS — `yatra-this-week-gordy`

## Open slots

**None.** Every beat is machine-rendered from `beat_sheet.json`. No image to
source, no clip to generate, no pantry item, no Higgsfield beat — the free path
only (Kokoro + Remotion + ffmpeg). Nothing here is a request to a human.

One deliberate non-slot: **B06 does not draw the LinkedIn graphics.** That is not
an unfilled slot, it is a refusal — inventing artwork and presenting it as the
week's deliverable would be a fabricated artifact. If you want the real assets on
screen, drop them at `pantry/B06.png` (or `pantry/B06-916.png`).

This file therefore records the prompts the reel SHOWS, which are the ones that
have to be exact.

## The prompts that appear on screen

### B00 — the cold-open ask

```
Recap my week on the Humanitarians AI tool series. This week's tool was Gordy.
Show what I finished, what I shipped, and what is still waiting on approval —
and do not claim anything is published that isn't.
```

Result lines beneath it (COLD OPEN LAW — the ask lands answered):

```
tool used: Gordy — experimented with it properly
made: graphics for the Humanitarians AI LinkedIn page
in review with Nina: 2 articles → Substack once approved
```

The third line does real work: the cold open states the unfinished status before
the reel has said anything else, so the episode cannot be accused of burying it.

### B04 — the ask micro-beat (ASK→RESULT LAW)

The reel's one mid-body ask. This is the ACTUAL generation prompt behind B05's
status board, which is the point of the law: the interface is a receipt.

```
Draw my five stages as a status board, marking each one closed or still open.
Mark 'publish' as open — the articles are with a reviewer, not live — and do
not label anything published.
```

`runningText: "drawing the board…"`, `output: []` — the result is B05.

The constraint is visible inside the prompt the viewer reads, which is the most
honest place to put it.

### B10 — the handoff prompt (HANDOFF LAW)

Read aloud verbatim in the narration, then discussed, then handed over.

```
Help me run a five-stage week on one tool at work — pick, use, make, write,
publish. At the end, tell me which stages I actually closed and which ones I am
only calling closed.
```

The rubric that makes it a SCAFFOLDED task rather than "ask Claude about X":

```
grade it: does it separate finished from published?
grade it: does it name the stage you're stuck on?
grade it: would a stranger know what is not done yet?
```

## Why this prompt, for the handoff

It hands the viewer the episode's own method and its own discomfort. The reel's
subject is a week that ended mid-pipeline, and the prompt makes the viewer run
the same audit on their own work — where the interesting answer is always the
gap between "done" and "published." The third rubric line is the real test: it
asks whether their status would survive being read by someone who wasn't there.

## The source fetch (recorded for reproducibility)

Gordy's on-screen description was taken from the tool page, fetched twice on
2026-09-03:

```
https://www.humanitarians.ai/ai1/tools/gordy-tool
```

Both fetches returned the same one-sentence description and no command
reference. Nothing was inferred to fill the gap — see SOURCES.md.
