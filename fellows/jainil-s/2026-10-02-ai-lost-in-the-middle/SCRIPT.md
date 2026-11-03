# SCRIPT — Lost in the Middle

**Slug:** `ai-lost-in-the-middle` · **Voice:** Kokoro `am_onyx` · **Register:** Teardown · **Handle:** @HumanitariansAI

**Beats:** 9 · **Runtime:** 2:19.2 (measured from the generated narration — the master clock)

---

## B00 · ASK — `ClaudeComposerAsk`  (18.56s)

Sawubona. This is Liam, in for Bear. You paste in a forty page document, ask a question, and the model misses something that was definitely in there. The usual explanation is that the context window was too small, so people reach for a bigger one. Often that was never the problem. The answer was inside the window the whole time, sitting in the wrong part of it.

## B01 · BLUF — `BrutalistHesitantWriter`  (15.77s) · `qc.sparse`

Here is the whole video in one correction. We treat the context window as a container: if a fact is inside it, the model can use it. It does not work like that. Where the fact sits inside the window changes how reliably it gets used, and the worst place to put something important is the middle.

## B02 · SETUP — `FormACard`  (17.28s) · `qc.sparse`

Researchers tested this the obvious way. Take a question whose answer sits in one particular document. Bury that document in a pile of irrelevant ones. Then slide it: first position, middle position, last position. Same question, same answer, same amount of text. The only thing that changes is where the answer is.

## B03 · HERO — `PositionCurve`  (17.64s) · `qc.sparse`

And this is the shape that comes back. Strong at the start. Strong at the end. A long sag through everything in between. It is the same curve you get from people asked to memorise a list, which is a genuinely strange thing to find in a machine. Put your key paragraph in the middle of a long prompt and you are putting it in the weakest position available.

## B04 · EVIDENCE — `FormACard`  (18.82s) · `qc.sparse`

That is not my reading of it. That is the paper's own sentence. Performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts. And then the part that should stop you: even for explicitly long-context models.

## B05 · LAND — `WantQuote`  (8.11s) · `qc.sparse`

So a bigger context window is not the same thing as a bigger attention span. Room to put something is not a promise that it gets read.

## B06 · FIX — `FormACard`  (29.65s) · `qc.sparse`

Which gives you four things to do, and none of them are hard. Put the important material at the top or the bottom, never buried mid-stack. Cut the padding, because every irrelevant page you include pushes something real toward the weak zone. Put the question at the end as well as the start, so the thing you actually want is in a strong position too. And if a long prompt is failing, move the key passage and re-run before you assume the model cannot do the task. That one test costs you nothing and it tells you whether you have a model problem or a layout problem.

## B07 · HANDOFF — `ClaudeComposerAsk`  (10.5s)

So here is your turn. Take a long prompt that has been letting you down. Do not rewrite it. Just move the part that matters to the very top, run it again, and see whether the problem was ever the model.

## B08 · OUTRO — `HaiTitleOutro`  (2.86s) · `qc.sparse`

Lost in the middle. Liam, in for Bear.
