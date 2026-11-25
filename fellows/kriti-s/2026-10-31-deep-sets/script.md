# Deep Sets, Explained — script (narration as rendered)

Voice: Kokoro `am_onyx`

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · COLD_OPEN
> Hello, this is Liam, in for Kriti, explaining Deep Sets.

### B01 · OVERVIEW_(BLUF)
> Deep Sets treat a group as a set, not a list: the order doesn't matter, and the group can be any size.

### B02 · BODY_TWO_PROBLEMS
> Standard networks have two problems with teams. Swap two teammates and the output can change, though nothing in the world did. And the input size is fixed: train with two teammates, deploy among eight, and the extra numbers have nowhere to go.

### B03 · BODY_DEFINITION
> Deep Sets fixes both. Pass every teammate through the same small network, phi, and add the results. The sum, H, goes to the main network, rho.

### B04 · BODY_PIPELINE
> Each teammate is four numbers: relative position and velocity. The shared network turns each into thirty-two features, and the sum turns them into one thirty-two number summary.

### B05 · BODY_WHY_A_SUM
> Addition is the trick. It ignores order, and the result stays thirty-two numbers whether there are one, three, or ten teammates. With none, it's all zeros.

### B06 · BODY_EXAMPLE
> So you can train a policy on small teams of two or three agents, and run it in a swarm of ten without retraining. Whether it still performs well there is something to test, not assume.

### B07 · BODY_WHERE_IT_FITS
> It fits whenever the input is a set: swarms of agents, point clouds, a bag of items, groups whose size changes.

### B08 · BODY_WHERE_IT_STRUGGLES
> It struggles when order matters, like text or time series; when interactions between members matter, since a plain sum blurs them; and when a growing sum misleads the network, where averaging helps.

### B09 · VERDICT
> The verdict: Deep Sets buys order and size independence by construction, and pays for it by blurring how members relate to each other.

### B10 · YOUR_TURN_HANDOFF
> Your turn: 'My model takes a variable-size group of inputs. Should I use Deep Sets, mean pooling, or attention? Ask me first what matters about order and interactions.' The best answer starts with questions, not an architecture.

### B11 · OUTRO
> Deep Sets, Explained. At Nik Bear Brown.

