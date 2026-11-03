# PROMPTS — weekly-fixtures-before-validators

Beat-prefixed prompts for open slots.

## Open slots: none

Every beat in this reel renders from sources inside this folder — the seven
Remotion beats from registered Claude components, the five Manim beats from
`scenes.py`. Nothing is waiting on a human-supplied asset, so there is no
pantry request card to write.

This file exists because GATE F requires the paperwork set, and because the
next weekly reel may not be so lucky.

## If a beat ever does open up

Write the request card here, beat-prefixed, naming the artifact and the motion
— not a mood. Format:

```
B0X — <what the beat must show, in one line>
      Motion: <how it moves; the spine forbids stills on OUTPUT beats>
      Fill:   pantry/B0X.png  |  media/B0X.mp4  |  manim/B0X.mp4
      Source: <where the asset comes from; CC0/own-capture only>
```

## Reusable asks for the weekly format

These are the prompts that generated this reel's structure, kept so week two is
a swap rather than a redesign.

**The week's opening ask** (B00 composer text — rewrite per week):

```
claude "read the diff for <commit> and tell me the single idea it is evidence
for — not a list of what changed"
```

**The beat-sheet ask:**

```
claude "author a cli-explainer beat sheet for commit <sha>: INTRO, PROBLEM,
two CLI→CODE→OUTPUT cycles, a falsifiability beat, SUMMARY, NEXT STEPS, OUTRO.
Every on-screen number must be re-derived from the repo, not from the commit
message. Show real source in the CODE beats."
```

**The falsifiability ask** — the one that most improved this reel:

```
claude "what does this work NOT establish? Find the limitation the repo itself
already records, and quote it rather than inventing a caveat."
```

For this week that surfaced the manifest's `not_covered` section on wrong-entity
signals, which became B08 — the beat the commit message did not mention.
