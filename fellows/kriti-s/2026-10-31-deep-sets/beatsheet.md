# Deep Sets, Explained — Beat Sheet

**Slug:** `claude-liam-deep-sets` · **Voice:** Kokoro `am_onyx`

Generated from [`beat_sheet.json`](beat_sheet.json), which is the source of truth: edit the JSON, not this table. Start times add up each beat's rendered duration.

## 12 beats, 1:47 (107.6s)

| # | Act | Start | Dur | Pattern | Motion | Narration |
|---|---|---|---|---|---|---|
| B00 | COLD_OPEN | 0:00 | 4.3s | ClaudeComposerAsk | type-on | Hello, this is Liam, in for Kriti, explaining Deep Sets. |
| B01 | OVERVIEW_(BLUF) | 0:04 | 6.7s | BrutalistHesitantWriter | hesitant-type | Deep Sets treat a group as a set, not a list: the order doesn't matter, and the group can be any size. |
| B02 | BODY_TWO_PROBLEMS | 0:11 | 13.3s | UpdConceptGrid | motion-in | Standard networks have two problems with teams. Swap two teammates and the output can change, though nothing in the world did. And the input size is fixed: train with two teammates, deploy among eight, and the extra numbers have nowhere to go. |
| B03 | BODY_DEFINITION | 0:24 | 8.8s | TypesetMath | motion-in | Deep Sets fixes both. Pass every teammate through the same small network, phi, and add the results. The sum, H, goes to the main network, rho. |
| B04 | BODY_PIPELINE | 0:33 | 10.7s | UpdFlow | motion-in | Each teammate is four numbers: relative position and velocity. The shared network turns each into thirty-two features, and the sum turns them into one thirty-two number summary. |
| B05 | BODY_WHY_A_SUM | 0:43 | 9.4s | TypesetMath | motion-in | Addition is the trick. It ignores order, and the result stays thirty-two numbers whether there are one, three, or ten teammates. With none, it's all zeros. |
| B06 | BODY_EXAMPLE | 0:53 | 10.6s | UpdCompare | motion-in | So you can train a policy on small teams of two or three agents, and run it in a swarm of ten without retraining. Whether it still performs well there is something to test, not assume. |
| B07 | BODY_WHERE_IT_FITS | 1:03 | 7.2s | UpdChecklist | motion-in | It fits whenever the input is a set: swarms of agents, point clouds, a bag of items, groups whose size changes. |
| B08 | BODY_WHERE_IT_STRUGGLES | 1:11 | 11.1s | UpdScorecard | motion-in | It struggles when order matters, like text or time series; when interactions between members matter, since a plain sum blurs them; and when a growing sum misleads the network, where averaging helps. |
| B09 | VERDICT | 1:22 | 8.3s | PiVerdict | motion-in | The verdict: Deep Sets buys order and size independence by construction, and pays for it by blurring how members relate to each other. |
| B10 | YOUR_TURN_HANDOFF | 1:30 | 13.0s | ClaudeComposerAsk | type-on | Your turn: 'My model takes a variable-size group of inputs. Should I use Deep Sets, mean pooling, or attention? Ask me first what matters about order and interactions.' The best answer starts with questions, not an architecture. |
| B11 | OUTRO | 1:43 | 4.1s | ClaudeTitleOutro | outro-card | Deep Sets, Explained. At Nik Bear Brown. |
