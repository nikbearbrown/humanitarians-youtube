# PROMPTS — `yatra-the-mask-slips`

## Open slots

**None.** Every beat is machine-rendered from `beat_sheet.json` — no image to source, no
clip to generate, no pantry item. The free path only (Kokoro + Remotion + ffmpeg).

Two deliberate non-slots, both refusals rather than gaps:

- **No screenshot of either account.** Neither was named to us, and showing a real
  account would identify it. `MskDrop` labels each case by the human's own *description*
  and has no `name`, `handle` or `platform` prop.
- **No AI-generated "influencer" imagery.** Fabricating a face to illustrate a story
  about fabricated faces would be the same error the reel is describing.

This file therefore records the prompts the reel SHOWS.

---

## The prompts that appear on screen

### B00 — the cold-open ask

```
AI influencer accounts are going viral and earning money within days, then
collapsing once audiences work out they are AI. Walk me through the arc — the
rise, the reveal, and what happens to engagement after. Cite the reporting on
screen and do not add figures that aren't in it.
```

Result lines beneath it (COLD OPEN LAW — the ask lands answered):

```
the rise: viral two days after the account was created
the money: a reported $13,700 from one video
the reveal: identified as AI — and roughly half the engagement gone
```

Greeting: `Annyeong, Bella` · folder chip: `@Yatra` · running: `reading the reporting…`

### B04 — the generation ask (ASK→RESULT LAW; B05 is the result)

```
Draw the arc of an AI influencer account: a near-vertical rise to viral, then
the fall that starts at the moment the audience identifies it as AI. Mark the
identification point. No invented numbers — shape only.
```

Greeting: `The ask,` · running: `drawing the arc…` · no output lines — the next beat IS
the output. Note that "no invented numbers — shape only" is not decoration: `MskArc` has
no numeric prop and renders a required `axisNote` saying the curve carries no figures.

### B11 — the handoff (HANDOFF LAW: read aloud verbatim, then discussed)

```
Here's something I'm about to publish. Tell me which parts of it would lose
their meaning if my audience learned a machine made them, and which parts
wouldn't care either way. Then tell me which of those I'd be embarrassed to
have to explain later.
```

Rubric shown beneath, and spoken:

```
grade it: can it tell persuasion from information?
grade it: does it separate 'undisclosed' from 'AI-made'?
grade it: does it name what you'd have to explain later?
```

**Why this prompt:** it turns the episode's claim into a test the viewer can run on their
own work in two minutes, and the second rubric line is the one that matters — the reel's
argument is about *disclosure*, not about machines, and a good answer should keep those
apart rather than collapsing them into "AI bad."

---

## Rebuilding

```bash
./art run   /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-the-mask-slips
./art final /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-the-mask-slips
```

Scene source lives in the toolkit: `runtime/remotion/src/scenes/MaskSlips.tsx` and
`MaskSlips916.tsx`, registered in `runtime/remotion/src/Root.tsx`. If narration changes,
regenerate audio FIRST, then retarget each composition's `durationInFrames` to the new
measured length × 30 — never hand-tune timing in the sheet.
