# SHOTLIST — Mixture of Experts

Native 16:9 (3840×2160) and 9:16 (2160×3840, `vertical/`). 12 beats · Kokoro `am_onyx` · @HumanitariansAI · ~62 s.

| # | Act | Pattern (→ 916 twin) | Show |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | "Hola, Likhith" · ask · 3 lines · AI-narration disclosure line |
| B01 | BLUF | BrutalistHesitantWriter | "the whole model" → "a few experts" |
| B02 | HOOK | MoeHook | 671B counts up · "work per token: ?" |
| B03 | DENSE | MoeDense | every unit fires per token · 2× size → 2× cost |
| B04 | IDEA | MoeExperts | one FFN block splits into E1…E8 |
| B05 | ROUTER | MoeRouter | "cat" → router → 8 scores → top 2 picked |
| B06 | SPARSE | MoeSparse | 3 tokens, each lights its own 2 of 8 |
| B07 | WHY | MoeScale | Mixtral 47B/13B · DeepSeek-V3 671B/37B |
| B08 | TRADEOFF | MoeMemory | all 8 loaded in GPU memory · 2 compute |
| B09 | VERDICT | ClaudeVerdictArtifact | 6 lines |
| B10 | YOUR TURN | ClaudeComposerAsk | prompt read aloud |
| B11 | OUTRO | HaiOutro | HAI mark · title · Subscribe · "Narrated by an AI voice" note |
