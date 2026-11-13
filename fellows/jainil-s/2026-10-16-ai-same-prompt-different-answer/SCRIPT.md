# SCRIPT — Same Prompt, Different Answer

Narration as delivered. Kokoro `am_onyx`; measured durations are the master clock.

**Total 2:23.5** across 9 beats. Master 16:9 3840x2160.

---

### B00 — ASK  ·  14.61s

*ClaudeComposerAsk*

> Olá. This is Jainil. You send the same prompt twice and get two different answers, so you file it as a bug. It usually is not one. There is a specific place the difference comes from, and a second place that surprises people even after they have turned the temperature down to zero.

### B01 — BLUF  ·  14.44s

*BrutalistHesitantWriter*

> Here is the whole idea in one breath. The model does not pick a word. It produces a probability for every word it could say next, and then something draws one. Temperature does not add the randomness — it decides how peaked that distribution is before the draw happens.

### B02 — SETUP  ·  17.77s

*BarChart*

> This is one position in one answer. Seven candidate words, and the probability the model assigns to each. The most likely word, the, gets forty-six and a half percent. Which means that at this one position, better than half the time, you get something that is not the. Nothing has gone wrong. That is the distribution doing exactly what it says.

### B03 — TURN  ·  19.33s

*DistributionShape*

> Now turn the temperature down to nought point two. Same model, same scores, same position — but the shape changes. The dashed outline is where we just were. The solid shape is the same distribution at the lower temperature: the top word now takes ninety-five percent and everything else is flattened into the floor. Lower temperature does not mean more correct. It means more peaked.

### B04 — EVIDENCE  ·  19.52s

*PositionCurve*

> And here is why even a low temperature does not buy you a repeatable answer. This is the chance that every single token in an answer takes the top choice, plotted against how long the answer is, at temperature nought point two. One token, ninety-five percent. Ten tokens, sixty percent. Fifty tokens, eight percent. Two hundred tokens — one in twenty-three thousand.

### B05 — LAND  ·  16.87s

*DigitDiff*

> So you set temperature to zero. Now it takes the highest score every time — no draw at all. And it still varies. Here is why. These are the same thousand numbers added up twice: once one at a time, once in ten blocks. Floating point addition is not associative, so the order changes the answer. Look where they stop agreeing.

### B06 — SOURCE  ·  20.25s

*FormACard*

> Be careful with that, though. Non-associativity on its own does not make a model unpredictable — the same code on the same input in the same order gives the same answer every time. What changes the order is dynamic batching. Your request lands in a batch of a different size, the kernel splits its sums differently, and the scores shift by a hair. This is from SGLang's own documentation.

### B07 — HANDOFF  ·  17.02s

*ClaudeComposerAsk*

> Your turn. If you have ever written a test that asserts an exact model output, try this one: I have tests that compare model output to an expected string, and they fail intermittently. Help me rewrite them to assert on the properties I actually care about instead of on exact text. That is the fix. Not a lower temperature.

### B08 — OUTRO  ·  3.71s

*HaiTitleOutro*

> Same prompt, different answer. This is Jainil. Subscribe.
