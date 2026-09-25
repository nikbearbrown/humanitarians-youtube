# SCRIPT — Accuracy Is Lying to You

**Slug:** `ai-accuracy-is-lying-to-you` · **Voice:** Kokoro `am_onyx` · **Register:** Teardown · **Handle:** @HumanitariansAI

**Beats:** 9 · **Runtime:** 2:14.7 (measured from the generated narration — the master clock)

Narration as delivered. Durations are set by Kokoro at generation time;
the visuals conform to them, never the other way round.

---

## B00 · ASK — `ClaudeComposerAsk`  (14.34s)

Hola. This is Liam, in for Bear. A model comes back ninety-five percent accurate, and everyone in the room relaxes. I want to show you a case where ninety-five percent accurate is not a good result. It is the tell that the model has learned nothing at all.

## B01 · BLUF — `BrutalistHesitantWriter`  (14.14s) · `qc.sparse`

Here is the whole video in one correction. Accuracy is the share of predictions you got right. That sounds like exactly what you want to know. It is not, and the reason is simple: when the thing you are looking for is rare, you can be right almost always by never finding it.

## B02 · SETUP — `FormACard`  (14.38s) · `qc.sparse`

Take a concrete case. A condition that affects one person in a thousand. You have a test that never misses a real case, and raises a false alarm five percent of the time. Those two numbers are all we need. Everything from here is arithmetic you can check yourself.

## B03 · HERO — `RareEventGrid`  (15.15s) · `qc.sparse`

So line up a thousand people. One of them actually has it. That is the single terracotta square. Now run the test on the nine hundred and ninety nine who are healthy. Five percent of them come back positive anyway. That is roughly fifty false alarms. Look at the picture. Fifty to one.

## B04 · TURN — `BarChart`  (17.47s)

Fifty-one people just tested positive and one of them is actually sick. So a positive result is right about two percent of the time. Not ninety-five. Two. And here is the part that should bother you: a model that simply answers no to every single person is ninety nine point nine percent accurate, and it finds nobody.

## B05 · LAND — `WantQuote`  (17.32s)

That is the whole trap. Accuracy rewards the majority answer. When one class is rare, the majority answer is always no, so the lazy model wins on the scoreboard. And notice this gets worse, not better, as the problem gets more important. The rarer the thing you are hunting, the more flattering accuracy looks, and the less it is telling you.

## B06 · FIX — `FormACard`  (22.55s) · `qc.sparse`

So read two other numbers instead, and always about the rare class, never the average. Precision: when it says yes, how often is it right. Recall: of the real cases out there, how many did it catch. The lazy model has a recall of zero, and no amount of accuracy hides that. This is not a toy problem either. Fraud in transactions, a defect on a production line, a disease in a screening population: the rare class is exactly the thing you built the model to find.

## B07 · HANDOFF — `ClaudeComposerAsk`  (15.91s)

So here is your turn. Take any classifier you already trust, find out what fraction of your data is the positive class, and work out what accuracy a model would get by never predicting it at all. If that number is close to the one on your dashboard, your model has not learned the thing you think it learned.

## B08 · OUTRO — `HaiTitleOutro`  (3.48s) · `qc.sparse`

Accuracy is lying to you. Liam, in for Bear.
