# PROMPTS — weekly-fixtures-before-validators (9:16 SHORT)

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
./art shorts D:/Projects/youtube/weekly-fixtures-before-validators \
  --drop B03 B04 B06 B07 B08 B10 B11 --handle @HumanitariansAI
```

Then, in order:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>/short   # outro only
python3 runtime/scripts/remotion_scenes.py <reel>/short          # 916 bookends
bash runtime/scripts/run.sh <reel>/short --height 1920           # manim + gates + compile
```

The audio for B00, B01, B02, B05 and B09 is the parent's, byte for byte. Only
B12's narration was regenerated, because the Shorts Law requires the outro to
say what was cut and point at the long.

## The one authored line

`shorts.py` auto-drafts the funnel outro by splicing the opening words of each
dropped beat's narration. On this cut that produced a sentence that was not
English — "…method steps 1 + 2 enumerate, plant, Here is step three of and step
1 verify provenance…". It was replaced by hand:

> That's the method. The full video walks it through the real code: the defect
> record, the provenance run, and a prompt to try it on your own suite. Watch
> Build the Defects First. Link below.

Recorded here rather than left as a silent edit — the auto-draft is a starting
point, and on a reel whose beats have long narration it will need rewriting
every time.

## If a beat ever does open up

Write the request card here, beat-prefixed, naming the artifact and the motion
— not a mood. Format:

```
B0X — <what the beat must show, in one line>
      Motion: <how it moves; the spine forbids stills on OUTPUT beats>
      Portrait: <what changes at 4.5 x 8 — never assume the landscape layout>
```
