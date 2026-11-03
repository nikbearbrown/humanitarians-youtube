# SHOTLIST — KV Caching

Native 16:9 (3840×2160) and 9:16 (2160×3840, `vertical/`). 12 beats · Kokoro `am_onyx` · @HumanitariansAI · ~63.5 s.

| # | Act | Pattern (→ 916 twin) | Show |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | "Ciao, Likhith" · ask · 3 lines · AI-narration disclosure line |
| B01 | BLUF | BrutalistHesitantWriter | "computing faster" → "reusing work" |
| B02 | HOOK | KvHook | prompt · pause bar fills · reply streams, ticks on a timeline |
| B03 | PROBLEM | KvRecompute | step rows 1–6 · older cells recompute (grey) · counter → 21 |
| B04 | FRAMEWORK | KvQkv | q/k/v strips per token · past k,v boxed "never change" |
| B05 | MECHANISM | KvStore | prompt sweep ("the pause") · K/V cells drop into the cache |
| B06 | MECHANISM | KvDecode | new k,v append · q for "mat" scores cached keys · typeset attention equation |
| B07 | EVIDENCE | KvScale | t(t+1)/2 vs t at t=10/100/1,000 (executed counts) · 500.5× |
| B08 | TRADEOFF | KvMemory | bar 0→4,096 tokens, 0→2.00 GiB · typeset formula · model-shape caption |
| B09 | VERDICT | ClaudeVerdictArtifact | 6 lines |
| B10 | YOUR TURN | ClaudeComposerAsk | prompt read aloud |
| B11 | OUTRO | HaiOutro | HAI mark · title · Subscribe · "Narrated by an AI voice" note |
