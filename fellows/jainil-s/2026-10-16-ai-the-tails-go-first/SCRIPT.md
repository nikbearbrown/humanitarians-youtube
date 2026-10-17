# SCRIPT — The Tails Go First

Narration as delivered. Kokoro `am_onyx`; measured durations are the master clock.

**Total 2:21.7** across 9 beats. Master 16:9 3840x2160.

---

### B00 — ASK  ·  15.15s

*ClaudeComposerAsk*

> Annyeong. This is Jainil. There is a lot of synthetic data around now, and a tempting idea that comes with it: a model generates training data, you train the next model on that data, and round it goes. This week I ran that loop sixty times, and watched what it throws away first.

### B01 — BLUF  ·  12.46s

*BrutalistHesitantWriter*

> Here is the whole idea in one breath. Train a model on its own output, over and over, and the average stays perfectly fine. What disappears is the rare stuff. It goes quietly, nothing warns you, and it does not come back.

### B02 — SETUP  ·  19.05s

*DistributionShape*

> Start with a world that has something rare in it. Most of the data sits in one ordinary lump around zero. Five percent of it sits all the way out here, far from everything else — a small subpopulation that genuinely exists and that you would want a model to know about. Generation zero draws two hundred samples from that world. Four and a half percent of them land in the rare part.

### B03 — TURN  ·  19.09s

*StageRail*

> Now the loop. Generation one is a model fitted to generation zero's samples. Generation two is fitted to generation one's output. And so on down the line. After that first step, no real data ever enters again. Nothing here is adversarial and nothing is badly implemented — every generation simply does its best with whatever the last one handed it.

### B04 — EVIDENCE  ·  17.43s

*PositionCurve*

> Here is the rare subpopulation's share, generation by generation. Four and a half percent to start. Three and a quarter by generation ten. One and a half by generation twenty. By generation thirty it is zero. Across sixty runs it went extinct in forty-nine of them, and in not one of those forty-nine did it ever come back.

### B05 — LAND  ·  21.61s

*DistributionShape*

> And here is the part that should bother you. This is the shape at generation forty, with the original dashed in behind it. The bump is simply gone. But look at the numbers underneath. The mean moved from plus zero point two eight to plus zero point three six. The standard deviation went from one point six to one point seven. Nothing in the ordinary summary statistics tells you that five percent of the world is permanently missing.

### B06 — SOURCE  ·  16.36s

*FormACard*

> This is not my phrasing, it is the paper's own. Shumailov and colleagues, in Nature, twenty twenty-four. They found it across language models, variational autoencoders, and Gaussian mixture models — and that last family is the one I just ran in front of you. Note the word they chose for it: irreversible.

### B07 — HANDOFF  ·  17.05s

*ClaudeComposerAsk*

> Your turn. Take this one at something you actually run: I have a training set that includes model-generated examples — help me work out which parts of my real distribution are underrepresented in it, and what I would have to keep sampling from the real world to avoid losing them. The second half of that prompt is the useful half.

### B08 — OUTRO  ·  3.52s

*HaiTitleOutro*

> The tails go first. This is Jainil. Subscribe.
