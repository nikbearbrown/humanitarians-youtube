# PROMPTS — `yatra-interest-media`

## Open slots

**None.** Every beat is machine-rendered from `beat_sheet.json` — no image to source, no
clip to generate, no pantry item, no Higgsfield beat. The free path only (Kokoro +
Remotion + ffmpeg). Nothing in this file is a request to a human.

One deliberate non-slot: **B02 does not show a quotation.** That is not an unfilled slot,
it is a refusal. The human's instruction was to credit Gary Vaynerchuk and *not* quote him,
so `ItmSource` has no `quote` prop — there is nowhere to put one. What appears instead is
the human's own paraphrase under a `PARAPHRASED — NOT A QUOTE` stamp.

This file therefore records the prompts the reel SHOWS, which are the ones that have to be
exact.

---

## The prompts that appear on screen

### B00 — the cold-open ask

```
Gary Vaynerchuk argues social media has become interest media. Explain the shift
from follower-based feeds to interest-based feeds — and what it changes for
someone making content. Credit him, paraphrase him, and do not invent any
statistics.
```

Result lines beneath it (COLD OPEN LAW — the ask lands answered):

```
the old sort key: who you know — your follows, your contacts
the new sort key: what you care about — watched, paused, searched
so the gate moved: a post can now travel before an audience exists
```

Greeting: `Vanakkam, Bella` · folder chip: `@Yatra` · running: `reading the shift…`

### B06 — the generation ask (ASK→RESULT LAW; B07 is the result)

```
Draw the two models side by side: the follower model, where reach is gated behind
an audience you have to build first, and the interest model, where one post can
travel on match alone. No numbers — just the gate and the match.
```

Greeting: `The ask,` · running: `drawing both models…` · no output lines — the next beat
IS the output.

### B11 — the handoff (HANDOFF LAW: read aloud verbatim, then discussed)

```
Look at the last twenty things my feed showed me. How many came from accounts I
actually follow, and what interest was each of the others matching? Then tell me
which interest of mine the feed is most confident about.
```

Rubric shown beneath, and spoken:

```
grade it: can it name the interest, not just the account?
grade it: does it separate follows from matches?
grade it: does it say what it can't know from a feed alone?
```

Greeting: `Your turn.` · running: `paste this into Claude…`

**Why this prompt and not "learn more about interest media":** it runs the episode's claim
on the viewer's own feed, and it is falsifiable in about two minutes. The rubric's third
line is the honest one — a feed alone cannot tell you *why* something was served, and a
good answer should say so rather than confabulate a reason.

---

## Rebuilding this reel

```bash
./art run   /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-interest-media
./art final /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-interest-media
```

Scene source lives in the toolkit, not here:
`runtime/remotion/src/scenes/InterestMedia.tsx` and `InterestMedia916.tsx`, registered in
`runtime/remotion/src/Root.tsx`. If narration changes, regenerate the audio FIRST
(`generate_audio_kokoro.py`), then update each affected composition's `durationInFrames`
in `Root.tsx` to the new measured length × 30 — never hand-tune timing in the sheet.
