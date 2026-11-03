**Series:** STEM & AI Architecture
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

**SCENE 1 — HOOK**
**VISUAL** — Ground fill. A prompt block snaps in.
`AI: Tom Cruise's mother is Mary Lee Pfeiffer.`
`USER: Who is Mary Lee Pfeiffer's son?`
`AI: I don't know.`
**ON SCREEN:** `THE LOGIC BLINDSPOT`
**VO:**
Hi, I am Onkar Bhujbal, and this video is about the Reversal Curse and why language models fail at basic deductive logic. If a human learns that A equals B, they automatically know that B equals A. Large language models do not. This blindspot is a fundamental flaw in how AI is trained.

**SCENE 2 — THE FRAMEWORK**
**VISUAL** — Two mono-text boxes snap in, stacked vertically.
`01 LEFT-TO-RIGHT TRAINING` 
`02 NEXT-TOKEN PREDICTION`
**VO:**
The Reversal Curse happens because models are trained strictly left-to-right using next-token prediction. They memorize sequences in one specific direction. The model learned to predict the name "Mary" after seeing "Tom Cruise's mother." It never practiced predicting "Tom" after seeing "Mary."

**SCENE 3 — WORKED EXAMPLE**
**VISUAL** — Side-by-side comparison. 
**LEFT:** `A -> B (Strong Neural Pathway)`
**RIGHT:** `B -> A (Broken Neural Pathway)`
**VO:**
Imagine driving down a one-way street. You know the exact sequence of houses perfectly. But if someone drops you at the end of the street and tells you to drive it in reverse, the sequence is completely unfamiliar. The data is in the AI's weights, but the neural pathway only flows in a single direction.

**SCENE 4 — FALSIFIABILITY**
**VISUAL** — The screen flashes red.
**ON SCREEN:** `ARCHITECTURAL LIMITATION`
**VO:**
Why is this dangerous? Because it proves AI does not build an internal knowledge graph of facts. It only builds a statistical map of word sequences. You cannot fix the Reversal Curse simply by making the model bigger or feeding it more data. It is a mathematical limitation of the transformer architecture itself.

**SCENE 5 — SCAFFOLDED TASK & CLOSE**
**VISUAL** — Hard cut to a prompt terminal.
`PROMPT: "Who is [Obscure Celebrity's] parent? Now, who is the child of [That Parent]?"`
**VO:**
Audit a language model today. Find an obscure biographical fact and test the AI in both directions. You will immediately see the model confidently answer the first prompt and completely hallucinate the second.
Liam, for Onkar Bhujbal and Humanitarians AI.