# SCRIPT — Your Feature Importance Is Lying

**Slug:** `dae-your-feature-importance-is-lying` · **Voice:** Kokoro `am_onyx` · **Register:** Teardown · **Handle:** @HumanitariansAI

**Beats:** 10 · **Runtime:** 2:25.9 (measured from the generated narration — the master clock)

---

## B00 · ASK — `ClaudeComposerAsk`  (15.62s)

Merhaba. This is Liam, in for Bear. This week I learned that the tidiest thing I do to a model is also one of the most dangerous. You pull the feature importances, you look at the bottom of the list, you drop the columns that do not matter. That last step can delete the single best thing in your dataset.

## B01 · BLUF — `BrutalistHesitantWriter`  (15.17s) · `qc.sparse`

Here is the whole video in one correction. An importance score is not a measurement of how much a feature matters. It is a measurement of how much the model would miss that particular column if it vanished. Those are the same thing only when no other column carries the same information.

## B02 · SETUP — `BarChart`  (13.29s) · `qc.sparse`

So I built a world where I know the truth. Temperature drives the outcome two and a half times harder than day of week does. Nothing else matters at all. Fit a model, rank the features, and the ranking is exactly right: temperature on top, comfortably.

## B03 · TURN — `BarChart`  (20.46s) · `qc.sparse`

Now I record temperature a second time, in Fahrenheit. No new information, just the same measurement in other units. The model now has two ways to reach the same fact, so it leans on each about half as hard. And permutation importance asks what happens when a column is shuffled. Shuffle one, the model reads the other, and barely notices. Each copy now scores a fraction of what the single column scored.

## B04 · HERO — `BarChart`  (16.85s) · `qc.sparse`

Add a third copy and the thing actually breaks. Each temperature column now measures around zero point one two. Day of week, which never moved, sits at zero point two seven. So the ranking now says day of week is your most important feature. It is not. Temperature is, by a factor of two and a half, in every single run.

## B05 · EVIDENCE — `FormACard`  (17.92s) · `qc.sparse`

And again, this is documented. Scikit-learn's own page says that when two features are correlated and one is permuted, the model still has access to the latter through its correlated feature, which results in a lower reported importance value for both features, though they might actually be important. Their words, on the page that ships the tool.

## B06 · LAND — `WantQuote`  (11.43s) · `qc.sparse`

So the ranking was never wrong about what it measures. It measures what the model would miss. Duplicate a feature and the model misses each copy less, while the thing itself matters exactly as much as it always did.

## B07 · FIX — `FormACard`  (19.14s) · `qc.sparse`

Three habits fix it. Look at a correlation matrix before you look at an importance ranking, never after. Cluster the correlated columns and rank the clusters rather than the columns, which is the fix scikit-learn itself recommends. And when you are about to drop something, drop it, refit, and see whether the score actually moves. That is the only importance measure that cannot be split in half.

## B08 · HANDOFF — `ClaudeComposerAsk`  (12.27s)

So here is your turn. Open the last model you trimmed. Take the two features you dropped for scoring low, and check whether either of them was correlated with something you kept. If it was, you did not remove noise. You removed a witness.

## B09 · OUTRO — `HaiTitleOutro`  (3.8s) · `qc.sparse`

Your feature importance is lying. Liam, in for Bear.
