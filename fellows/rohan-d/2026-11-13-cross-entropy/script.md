# Cross-Entropy, One Surprise at a Time — script (final, as shot)

Channel claude-liam · Persona Liam (in for Bear) · Register Teardown · Voice Kokoro `am_onyx` (AI narration)
16:9 long cut: 3:06 (185.9s) · 9:16 cut: same length

Timestamps come from the measured audio and are approximate. This is what is spoken in the final render; on-screen props live in `beat_sheet.json`.

Opening line required by the weekly guide (not yet spoken in this video): "Hi, I am Rohan, and this video is about machine learning."

## 16:9 — long cut

### B00 · ask (0:00–0:18)
> Hi, this is Liam, in for Bear. The ask: how does a classifier turn its scores into a loss, and why do confident mistakes cost so much? Show me with real numbers. Cross-entropy turns the scores into probabilities, then charges the model for how little probability it gave the right answer. A small miss costs little. Sure and wrong costs a lot.

### B01 · overview (0:18–0:30)
> Cross-entropy punishes confident mistakes. Not how many answers the model gets wrong, but how sure it was when it was wrong. That is why a model can be right most of the time and still be charged heavily.

### B02 · scores to shares (0:30–0:44)
> A model ends with one score per answer. Here, two, one, and point one for cat, dog and fox. Softmax turns them into shares that add up to one: sixty-six percent, twenty-four, ten. Say the right answer is cat. The model gave it sixty-six percent.

### B03 · the charge (0:44–0:56)
> Now the charge. The loss is minus the natural log of the share given to the right answer. Sixty-six percent gives a loss of point four one seven. Give the right answer more, and the loss shrinks. Give it less, and the loss grows.

### B04 · the curve (0:56–1:09)
> Here is that charge for every share. Ninety percent costs point one. Fifty percent, point seven. Ten percent, two point three. One percent, four point six. The curve doesn't flatten as the answer gets worse. It climbs.

### B05 · two models (1:09–1:26)
> Two models, three questions, and both get two right. Same accuracy, sixty-seven percent. Model A is confident: ninety, ninety and ten percent on the true answer. Mean loss, point eight four. Model B hedges: sixty, sixty and forty. Mean loss, point six five. Accuracy can't tell them apart. Cross-entropy can.

### B06 · one step (1:26–1:45)
> How does the model learn from it? The slope on each score is just the share minus the answer, where the right one counts as one. Minus point three four one, plus point two four two, plus point oh nine nine. Step against the slope, with step size one. Cat's score rises to two point three four, and the loss drops from point four one seven to point two six four.

### B07 · where it bites (1:45–1:59)
> Where it bites. If the model gives the right answer a share of zero, the log is infinite. Real code clips the share, say at one in a trillion, and the loss lands at twenty-seven point six. One confident mistake can outweigh a thousand near-perfect answers.

### BVDT · verdict (1:59–2:21)
> Let's recap with Claude. The loss is minus the log of the share given to the right answer. Scores two, one and point one give shares sixty-six, twenty-four and ten, a loss of point four one seven. The cost climbs steeply as that share falls. Accuracy can't separate a confident model from a hedging one, the loss can. The slope on each score is share minus answer. And a share of zero makes the loss infinite, so real code clips it.

### BHTF · your turn (2:21–3:01)
> Your turn. Paste this into Claude: Write a short Python script, no ML libraries, that turns the scores 2.0, 1.0 and 0.1 into shares with softmax and prints the cross-entropy loss when each of the three classes is the right answer. Then take one gradient step on the scores with step size 1.0, using share minus answer, and print the new loss for class 0. Before running it, predict which class costs the most. Here's what to check. Class zero should cost point four one seven, class one one point four one seven, and class two two point three one seven. After one step the loss for class zero should fall to about point two six four. And see whether Claude explains why the smallest share costs the most, rather than just printing it.

### BOUT · outro (3:01–3:06)
> Cross-Entropy, One Surprise at a Time. At Nik Bear Brown.
