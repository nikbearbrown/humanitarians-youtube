# SCRIPT — It Was Still Learning

Narration as delivered. Kokoro `am_onyx`; measured durations are the master clock.

**Total 2:23.3** across 8 beats. Master 16:9 3840x2160.

---

### B00 — ASK  ·  19.67s

*ClaudeComposerAsk*

> Vanakkam. This is Jainil. You are training a model. The training accuracy hits a hundred percent, the loss flattens out, and the validation number has been going nowhere for a while. Every signal you normally watch says the run is finished, so you stop it and keep the checkpoint. This week I ran a case where stopping exactly there would have thrown away a model that was about to become perfect.

### B01 — BLUF  ·  14.66s

*BrutalistHesitantWriter*

> Here is the whole idea in one breath. A network can memorise its training set thousands of steps before it works out the pattern underneath. In between, every held-out number looks like failure. It is not failing. It is still learning, and nothing on your dashboard says so.

### B02 — SETUP  ·  19.99s

*CardSet*

> The task is modular addition: A plus B, modulo twenty-three. Every possible pair is one example, five hundred and twenty-nine of them. Three hundred and seventeen go into training and two hundred and twelve are held back, and no pair appears on both sides. The model is deliberately tiny — one hidden layer, ninety-six units, squared activation — small enough that nothing exotic is hiding in it.

### B03 — EVIDENCE  ·  30.56s

*DoubleDescentCurve*

> Here are both curves. The dashed line is training accuracy: it reaches a hundred percent at step five hundred and never moves again. The solid line is the held-out data, and this is the part to look at. At step five hundred it sits at nought point five percent. Chance, across twenty-three classes, is four point three. So it is not merely uninformed — it is doing worse than guessing. It stays down there for another fifteen hundred steps. Then it climbs, and by step six thousand it is past ninety-five percent. Twelve times later than the moment training looked finished.

### B04 — MECHANISM  ·  22.42s

*ClaudeBarChart*

> So what actually moves it? Weight decay. I ran the same task four times changing only that one number. With none at all the network memorises and simply sits there: nought point nine percent on held-out data after ten thousand steps. At nought point three, ten percent. At nought point five, eighty-six. At nought point eight, ninety-nine and a half. The pressure to keep shrinking the weights is what eventually makes a smaller solution win out over the memorised one.

### B05 — SOURCE  ·  12.80s

*FormACard*

> This has a name and a paper behind it. Power and colleagues, at OpenAI, called it grokking, in twenty twenty-two. And look at the phrase they used for when it happens, because that is the whole lesson: well past the point of overfitting.

### B06 — HANDOFF  ·  19.93s

*ClaudeComposerAsk*

> Your turn. If there is an early-stopping rule anywhere in your training code, take this one to it: here is my early stopping configuration — help me work out whether it could have halted a run that was still improving on held-out data, and what signal other than validation accuracy I could watch instead. Patience settings tend to be inherited from whatever script you started with, not chosen.

### B07 — OUTRO  ·  3.29s

*HaiTitleOutro*

> It was still learning. This is Jainil. Subscribe.
