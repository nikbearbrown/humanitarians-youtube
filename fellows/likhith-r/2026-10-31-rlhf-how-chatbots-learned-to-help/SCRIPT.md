# SCRIPT — RLHF: How Chatbots Learned to Help

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about RLHF, and how chatbots learned to be helpful.

**B01 · BLUF** — The idea: chatbots aren't given rules for helping. They learn it from rankings people give.

**B02 · HOOK** — Ask a raw model how to bake bread; it may reply with more questions. How did it become an assistant?

**B03 · FRAMEWORK** — Pretraining reads huge amounts of text. It can continue anything, but can't judge a good answer.

**B04 · MECHANISM** — Step one: people write example answers, and the model is trained to imitate them.

**B05 · MECHANISM** — Step two: it writes several answers, people rank them, and a reward model learns what they prefer.

**B06 · MECHANISM** — Step three: the reward model scores answers, nudging it higher, with a penalty for drifting from how it wrote.

**B07 · EVIDENCE** — In OpenAI's 2022 InstructGPT paper, people preferred an RLHF model a hundred times smaller than GPT-3.

**B08 · TRADEOFF** — The catch: it learns to please the reward model, not to be right. It agrees, sounds sure: sycophancy, reward hacking.

**B09 · VERDICT** — DPO and AI feedback, like Anthropic's Constitutional AI, cut the cost. Preferences still train every major chatbot.

**B10 · YOUR_TURN** — Your turn. Ask Claude: where might you be telling me what I want to hear? Then push back.

**B11 · OUTRO** — RLHF: how chatbots learned to help. At Humanitarians AI.
