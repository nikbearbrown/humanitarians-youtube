# PEDAGOGY — "How AI Image Generators Turn Noise Into a Picture"

How the reel is built to teach someone who has only ever typed a prompt.

## The register

Carried over from the two corrections that shaped the week-04 reels, both still
standing: *no assumed knowledge* ("what is a person who knows nothing about
audio going to understand?") and *no empty reel* ("at the end of the day the
viewer has to learn something"). Here that means: a background beat and an
analogy beat before any mechanism, and then exactly one equation — not zero.

## The shape

| Beat | Job | What the viewer can do after it |
|---|---|---|
| B00 ASK | the question everyone has: where do the four pictures come from? | name the surprise — they are made, not found |
| B01 BACKGROUND | every image starts as static; Midjourney says so itself | say what a seed is: the starting static |
| B02 ANALOGY | a photo in the rain — ruining is easy, reversing is the skill | explain why training means "undo one step" |
| B03 MECHANISM | the one rule: part picture + part noise, shares shifting | read the equation's two terms in plain words |
| B04 MEASURED | a real model, trained on a laptop, doing it | believe it — it is not an animation of a claim |
| B05 SEED + PROMPT | the two controls, separated | predict what changing each one does |
| B06 WHAT TO DO | lock the seed when testing a prompt; use style references for a look | use Midjourney better tomorrow |
| B07 OUTRO | sign-off | — |

## Decisions that carry the teaching

- **The analogy is kept on screen as the mechanism arrives.** B02's rained-on
  picture is not an illustration of noise — it *is* the forward process computed
  exactly, so the metaphor and the maths are the same pixels.
- **One equation, read aloud before it is shown.** "Part picture, plus part
  noise" is spoken, and the brackets under the typeset equation carry those same
  words, placed on the measured span of each term.
- **Shares are multipliers, not percentages.** √ᾱ and √(1−ᾱ) do not add to 1
  (their squares do). Showing "78% picture, 62% noise" would teach a false sum,
  so B02 and B03 show "× 0.78 / × 0.62".
- **The model's guess is shown next to the run** (B04). "At first it's only
  guessing" is otherwise an abstraction; the guess tile makes it visible — blurry
  early, sharp late.
- **Separate the two controls in one frame** (B05): same static / different prompt
  on the left, same prompt / different static on the right. A viewer who
  remembers only the picture still has the rule.
- **The takeaway is Midjourney's own advice**, quoted, so a fellow can trust it
  over this reel if they ever disagree.

## The honesty line

The toy is tiny, 16×16, two prompts. It is always labelled as a toy and "not
Midjourney". What transfers is the *method* (noise → repeated denoising, prompt
steering, seed as starting point), and that is all the reel claims transfers.
