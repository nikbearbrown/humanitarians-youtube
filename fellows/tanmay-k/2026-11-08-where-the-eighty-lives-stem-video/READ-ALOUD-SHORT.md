# READ-ALOUD — Short (9:16), draft 3

Narration only, in order, as the voice will say it. Numbers in words. Read it aloud once at your own pace and mark anything that rushes, confuses or trips your tongue. **For your read, not yet the Gate P sign-off.** Draft 3 corrects the figures after FACTCHECK found the first measurement was not like for like (S06, S07); draft 2 was Gate P signed on 2026-11-07 (`READ-ALOUD-SHORT-v2-signed.md`). Draft 2 applied the PROOF review: S02 and S04 are split so no line is heavier than 40 words, the operation count is scoped, and S06 says which model falls behind. The source line for the eighty is a picture-side item for `SHORT-SCRIPT.md`. Previous draft: `READ-ALOUD-SHORT-v1.md`. Written fresh as its own script: it sets the context first (what a recurrent model is, what the observation is, why we built two models), gives each idea room, and ends on its own finished thought before naming the full film.

**S01 · THE BET** (~7 s)

I read that a small model ran eighty times slower than a bigger one. So I made the arithmetic exactly equal, and went looking for where the time goes.

**S02 · THE CONTEXT** (~10 s)

A recurrent model reads a sequence one step at a time, carrying a memory forward. I read that one of these ran far slower than a bigger model, and I wanted to see why.

**S03 · THE BUILD** (~9 s)

So I built two tiny models with the same weights, the numbers a model learns. I'm Tanmay Kulkarni, in for Humanitarians AI.

**S04 · THE DIFFERENCE** (~16 s)

The first waits for itself. Every step needs the answer from the step before. The second has all its inputs up front, so it applies the same weights to every position at once.

**S05 · THE MATCH** (~11 s)

Same weights. Over a hundred steps, twenty million operations each, an operation being one multiply and one add.

**S06 · THE DIAL AT ZERO** (~14 s)

Now a dial, for how much the chip can do at once. All the way down, one thing at a time. The first took six point one milliseconds. The second, six point four. The same.

**S07 · TURN IT UP** (~16 s)

Turn it up. The second model can load a weight once and use it on many positions. The first cannot, because the next step has to wait. The first falls behind. One point three times slower. Then three point seven.

**S08 · THE WHY** (~13 s)

The arithmetic never changed. What changed is how much work could happen together. The first model fetches its weights again on every single step.

**S09 · THE LIMIT** (~12 s)

This is my laptop, not a small chip, and my gap is smaller than eighty. But it shows where the time can live: in the model and the chip together.

**S10 · THE PAYOFF** (~12 s)

Parameters tell you what a model stores. Operations tell you what it computes. Overlap tells you how long it waits.

**S11 · THE FILM** (~10 s)

The full film is called Where the Eighty Lives: Why a Smaller Model Can Run Far Slower.

---
11 lines · 302 words · about 86 to 101 s at 3.5 to 3.0 words per second (draft 1: 278 words, 9 lines; Week 29 Short: 239 words, about 79 s). Longest line: 40 words (draft 1: 52). Estimate only, to be measured on the voice.
