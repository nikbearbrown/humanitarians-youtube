# PROMPTS — state-space-models-and-mamba (9:16 SHORT)

Beat-prefixed prompts for open slots.

## Open slots: none

Every beat in this short renders from sources inside this folder — the two
bookends from registered Claude 916 components (`ClaudeComposerAsk916`,
`ClaudeTitleOutro916`), the four body beats from `scenes.py`, the endcard from
the toolkit. Nothing waits on a human-supplied asset, so there is no pantry
request card to write.

## Provenance of this cut

Derived from the parent reel one directory up:

```bash
./art shorts D:/Projects/youtube/state-space-models-and-mamba \
  --drop B03 B04 B05 B07 B09 B10 --handle @HumanitariansAI
```

Then, in order:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>/short   # outro only
python3 runtime/scripts/remotion_scenes.py <reel>/short          # 916 bookends
bash runtime/scripts/run.sh <reel>/short --height 1920           # manim + gates + compile
```

The audio for B00, B01, B02, B06 and B08 is the parent's, byte for byte. Only
B11's narration was regenerated, because the Shorts Law requires the outro to
say what was cut and point at the long.

## The one authored line

`shorts.py` auto-drafts the funnel outro by splicing the opening words of each
dropped beat's narration. On this cut that produced a sentence that was not
English — "…also covers Score the two you already, A state space model is and
In the earlier versions those…". It was replaced by hand:

> That's the trade. The full video scores recurrent nets and Transformers on the
> same three axes, walks the equations from S4 to Mamba, and hands you an
> architecture to score yourself. Watch State Space Models and Mamba. Link below.

Recorded here rather than left as a silent edit. Note that this sentence makes
claims about what the LONG contains — it is accurate against the parent's
B03 (scoring the incumbents), B04/B05 (the equations, S4) and B10 (your turn).
If the parent is ever re-cut, this line has to be re-checked, not assumed.

## REBUILD LAW

No figure in this short is lifted from any paper. B01's curves are a schematic
of quadratic-vs-linear SHAPE, carrying no axis numbers, because no measured
data backs them — the same reasoning as the parent reel.

## If a beat ever does open up

Write the request card here, beat-prefixed, naming the artifact and the motion
— not a mood. Format:

```
B0X — <what the beat must show, in one line>
      Motion: <how it moves>
      Portrait: <what changes at 4.5 x 8 — never assume the landscape layout>
      Source:  <the citation that must be on screen with the claim>
```
