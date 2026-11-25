# Why Attention Divides By The Square Root — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 3:41 (220.8s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · tldr · what (0:00–0:18)
> Hola. This is Liam, in for Bear. This film is about one small piece of the attention formula: why the scores are divided by the square root of the vector length. Longer vectors make wider scores, and wide scores make the softmax pick a single winner. Dividing by the square root keeps the spread the same at any length. The trap is calling it a detail.

### B01 · tldr · why (0:18–0:33)
> Why should you care? Every attention layer scores words against each other, and scores that run too wide break it. Nearly all the weight lands on one word. The softmax passes back almost no learning signal. One short division keeps attention a weighted average instead of a vote.

### B02 · the question (0:33–0:42)
> The question this film is really asking: why does attention divide by the square root of the vector length? Not why it divides at all. Why that number, and not one you could simply pick.

### B03 · terms (0:42–0:56)
> Three terms before we start. A dot product multiplies two vectors entry by entry and adds the results into one number. Softmax turns a list of scores into weights that add up to one. Variance measures how spread out numbers are around their average.

### B10 · learn 1 · HOOK (0:56–1:11)
> One word asks a question of six others. Each gets a score, and softmax turns the scores into weights. With short vectors, the weights look sensible. Now keep the recipe and make the vectors five hundred and twelve numbers long. One key takes ninety-nine point six percent.

### B11 · learn 1 · INSTANCE (1:11–1:25)
> Look at the scores themselves. At four numbers per vector they huddle near zero. At sixteen they spread. At sixty-four, wider. At five hundred and twelve, they run for dozens of units. On average, the biggest weight climbs from fifty-seven percent to ninety-six.

### B12 · learn 1 · INSTANCE (1:25–1:38)
> Why does a winner-take-all softmax matter? Training needs slope. Where the curve is flat, nudging a score changes nothing. Our rough measure of that slope, the biggest p times one minus p, falls from about point two to under point oh three.

### B13 · learn 1 · NAIVE (1:38–1:51)
> The obvious patch: divide every score by ten. Around sixty-four it looks fine. But at four, the bars go nearly flat. At two thousand and forty-eight, one winner takes most of the weight again. A fixed number fits one vector length.

### B14 · learn 1 · SHIFT (1:51–2:04)
> Stop watching the bars. Watch the width of the cloud of scores instead. Length four, the width is two. Sixteen, four. Sixty-four, eight. Every time the length quadruples, the width doubles. Before it moves, commit: what should we divide by?

### B15 · learn 1 · TRANSFORM (2:04–2:10)
> Divide by the square root, and the wide cloud folds back to the width it had at four. The bars recover.

### B16 · learn 1 · ABSTRACTION (2:10–2:23)
> Now the idea deserves a name. Each score is a sum of d products. Each product has variance one. The variances of independent terms add, so the score has variance d. Divide by the square root of d, and the variance is one again.

### B17 · learn 1 · TANGENT (2:23–2:39)
> Read it as a claim. The left side is how wide the score cloud is, squared. The equals sign says: exactly d, when the entries are independent with variance one. Q and k are random; d is a fixed count. Check at five hundred and twelve: measured variance, about five hundred and thirteen; divided, one.

### B18 · learn 1 · PAYOFF (2:39–2:51)
> Back to the six keys at five hundred and twelve. Raw, one key held ninety-nine point six percent. Scaled, the weights spread, from three percent to thirty-six. Attention is a weighted average again, not a vote.

### BVDT · verdict (2:51–3:09)
> Let's recap with Claude. Dot products of longer vectors spread wider. Wide scores saturate the softmax, and a saturated softmax passes back almost no signal. A fixed divisor fits one length only. For random vectors the spread grows as the square root of the length, so dividing by it holds the spread constant.

### BHTF · your turn (3:09–3:36)
> Your turn. Paste this into Claude: Write a short Python script that draws random queries and keys with variance 4 instead of 1, computes the variance of their dot products at vector length 64, and checks whether dividing by the square root of 64 still gives variance 1. Predict the number before you run it, then say what divisor would fix it. Look for two things: did you commit to a number before running it, and is the divisor you named the one that brings the variance back to one.

### BOUT · outro (3:36–3:41)
> Why Attention Divides By The Square Root. At Nik Bear Brown.
