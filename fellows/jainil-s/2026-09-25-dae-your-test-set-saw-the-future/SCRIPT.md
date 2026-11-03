# SCRIPT — Your Test Set Saw the Future

**Slug:** `dae-your-test-set-saw-the-future` · **Voice:** Kokoro `am_onyx` · **Register:** Teardown · **Handle:** @HumanitariansAI

**Beats:** 9 · **Runtime:** 2:18.2 (measured from the generated narration — the master clock)

Narration as delivered. Durations are set by Kokoro at generation time;
the visuals conform to them, never the other way round.

---

## B00 · ASK — `ClaudeComposerAsk`  (11.88s)

Hej. This is Liam, in for Bear. This week I learned that a model I trusted had been cheating, and that I had written the cheat myself. One line. The line everybody writes without thinking, right at the start of every project.

## B01 · BLUF — `BrutalistHesitantWriter`  (15.79s) · `qc.sparse`

Here is the whole video in one correction. A random train-test split is the default for a reason: it works, for most data. But the moment your rows have an order in time, shuffling them lets the model study Thursday before being tested on Wednesday. And predicting the past is easy, and worth nothing.

## B02 · HERO — `TimelineSplit`  (15.55s) · `qc.sparse`

Picture your rows on a timeline, oldest on the left. A random split scatters the test rows right through it. Every terracotta dot has training data sitting to its right, which means the model already studied what came after. It is being asked to predict a past it has effectively seen.

## B03 · EVIDENCE — `FormACard`  (18.52s) · `qc.sparse`

And I am not editorialising here. This is scikit-learn describing its own tool. The library says plainly that for time-ordered data, other cross-validation methods are inappropriate, because they would lead to training on future data and evaluating on past data. The standard approach is documented as wrong for this case, by the people who ship it.

## B04 · FIX — `TimelineSplit`  (14.59s) · `qc.sparse`

The fix is the same picture, cut once. Everything before a chosen moment trains. Everything after it tests. No test row has training data to its right, so the model is only ever predicting forwards, which is the only thing you will ever ask it to do in production.

## B05 · LAND — `WantQuote`  (12.16s) · `qc.sparse`

What makes this one dangerous is that nothing breaks. No error, no warning. The score just comes back better than it should be, and a better score is the last thing anyone interrogates. You do not go looking for a bug in good news.

## B06 · BODY — `FormACard`  (31.27s) · `qc.sparse`

Two things worth knowing before you reach for the fix. It is a drop-in: the library's own tool returns the first folds as training and the next one as the test, so it slots in where your old splitter was. And it has a precondition the docs state outright: your samples need to be evenly spaced, or the folds stop being comparable. One last thing. Time is not the only order that leaks. If several rows come from the same user, or the same device, splitting them randomly scatters near-duplicates across both sides, and the model gets to study the answer before the exam.

## B07 · HANDOFF — `ClaudeComposerAsk`  (14.81s)

So here is your turn. Open whichever project you are proudest of, find the line where you split the data, and ask one question: do these rows have an order in time? If they do, re-split it chronologically and compare the two scores. The gap between them is what you had been reporting.

## B08 · OUTRO — `HaiTitleOutro`  (3.63s) · `qc.sparse`

Your test set saw the future. Liam, in for Bear.
