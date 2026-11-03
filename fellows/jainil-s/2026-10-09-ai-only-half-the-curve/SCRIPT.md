# SCRIPT — You're Only Seeing Half the Curve

Narration as delivered. Kokoro `am_onyx`, measured durations are the master clock.

**Total 2:21.9** across 9 beats. Master 16:9 3840x2160.

---

### B00 — ASK  ·  14.98s

*ClaudeComposerAsk*

> Namaste. This is Jainil. You add parameters, the validation error starts climbing, so you stop and keep the smaller model. Textbook overfitting. That rule is right about what you just saw, and wrong about what happens next, because the curve you were taught is only the left half of the real one.

### B01 — BLUF  ·  10.05s

*BrutalistHesitantWriter*

> Here is the whole idea in one breath. The curve you are carrying around in your head has one dip, and you stop at the bottom of it. The real curve has two, and the second is lower than the first.

### B02 — EVIDENCE  ·  18.11s

*DoubleDescentCurve*

> This is the classical picture, and it is real. One hundred training examples, held fixed. Add parameters and test error falls, because the model finally has the capacity to represent the pattern. Keep adding and it climbs again, because now it is fitting the noise in those hundred examples. Best point: sixty parameters. The rule says stop here.

### B03 — EVIDENCE  ·  17.94s

*DoubleDescentCurve*

> Now watch what the textbook crops out. The axis has to be redrawn to fit it. Push past one hundred parameters, the number of training examples, and the error does not merely climb, it detonates. A hundred and eleven. A hundred and fifty-nine times worse than the best you had. And then, if you keep going, it comes back down, and it lands below the classical best.

### B04 — MECHANISM  ·  19.43s

*InterpolatorChoice*

> Here is why it happens. At exactly one hundred parameters there is precisely one setting that passes through all hundred points, and you get it whether it is sensible or not. Go wider and many different curves pass through those same points. Now the procedure gets to choose, and least squares takes the smallest one, which is the smoothest one. More capacity buys you a better choice, not a worse fit.

### B05 — EVIDENCE  ·  17.96s

*DoubleDescentCurve*

> And your training loss cannot tell you any of this. At one hundred parameters it reaches zero and stays there. Every model to the right fits the training data perfectly. The dotted line is flat on the floor from the cliff onward while the solid one swings through a factor of nearly four hundred. Training loss stops being a signal exactly when you need one.

### B06 — SOURCE  ·  18.84s

*FormACard*

> This is not a quirk of one small experiment. The shape has a name and a paper behind it. Belkin and colleagues, in the Proceedings of the National Academy of Sciences, twenty nineteen, in this same family of models. And Nakkiran and colleagues showed the same shape along training time, not just model size. You can train past the peak as well as build past it.

### B07 — HANDOFF  ·  20.91s

*ClaudeComposerAsk*

> Your turn. Take this one: a model I stopped scaling because validation error started rising — help me work out whether I stopped before or after the interpolation threshold, and design the cheapest experiment to check. Run it against a model you actually abandoned. What you are looking for is the ratio of parameters to training examples. If that ratio was anywhere near one, you may have stopped on the worst point on the whole curve.

### B08 — OUTRO  ·  3.71s

*HaiTitleOutro*

> You're only seeing half the curve. This is Jainil. Subscribe.
