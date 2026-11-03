# PEDAGOGY — "How AI Music Generators Turn Text Into Audio"

How the reel is built to teach someone who uses Suno but has never been told how a text prompt
becomes sound.

## The register

*No assumed knowledge* and *the viewer has to learn something*. So the problem (too many numbers)
comes before any mechanism, the one equation is an addition, and the reel ends on four things to do
with the next Suno prompt.

## The shape

| Beat | Job | What the viewer can do after it |
|---|---|---|
| B00 ASK | the question, and the honest scope (Suno's method is unpublished) | name the answer's shape: tokens, prediction, steering |
| B01 BACKGROUND | audio is a huge list of numbers | say why a model can't write raw audio one number at a time |
| B02 MECHANISM | a codec turns each frame into a token | explain what an audio token is |
| B03 MATH | stacked codebooks; tokens per second vs a CD | read "four codebooks, 375 tokens a second" |
| B04 MEASURED | my codec, measured and heard at 1, 4, 12 codebooks | hear what fewer tokens cost: the treble first |
| B05 PREDICT | a model guesses the next token (16.5% vs 0.1%) | explain "learning music" as predicting what comes next |
| B06 THE TEXT | how the prompt steers, in MusicGen and in my toy, heard | say what a prompt can and can't do |
| B07 WHAT TO DO | generate several, name the steerable things, check the treble | prompt Suno for a Lyrical Literacy track more deliberately |
| B08 OUTRO | sign-off | — |

## Choices worth defending

- **Build it small, say it's small.** A codec of plain k-means codebooks and a trigram model is
  tiny next to MusicGen, and the video says so; but every step is the real step, measured.
- **Copying, measured.** A small model trained on little music could just replay it. B06 reports
  the longest copied stretch (0.26 s), so the "it generated" claim is checked, not assumed.
- **Suno named once, honestly.** Fellows use Suno, so it frames the video, but its internals are never
  described: the published systems carry the explanation.
