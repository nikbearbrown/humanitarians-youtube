# PROMPTS — Why It Can't Count Letters

Beat-prefixed prompts for open slots. **There are no open slots** — all nine
beats render from registered Remotion compositions.

- **B00** — composer content (on screen):
  "How many r's are in strawberry? And before you answer — show me what you
  actually received when I typed that word."
- **B07** — the viewer handoff prompt (on screen, meant to be pasted):
  "Here's a word a model kept getting wrong. Show me how it tokenises, and tell
  me whether the split explains the error."

No image generation, no stock, no AI video. Free path throughout.

The tokenisation figures are not prompted from a model — they are produced by
`tokenize_evidence.py`, which runs a real tokenizer locally.
