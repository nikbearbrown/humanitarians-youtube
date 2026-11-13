# SHOTLIST — How Coding Agents Navigate Code

Native 16:9 (3840×2160) and 9:16 (2160×3840, `vertical/`). 12 beats · Kokoro `am_onyx` · @HumanitariansAI · ~68 s.

| # | Act | Pattern (→ 916 twin) | Show |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | "Ola, Likhith" · ask · AI-narration disclosure + 3 lines |
| B01 | BLUF | BrutalistHesitantWriter | "reads everything, then guesses" → "searches first, then tests a fix" |
| B02 | HOOK | AgentHook | bug report card · wall of 48 unseen files · "?" |
| B03 | EXPLORE | AgentExplore | `find` · real tree: shop/ (6) and tests/ (3) |
| B04 | SEARCH | AgentSearch | `grep 'discount'` · 3 of 9 files light · pricing.py lines 4–6, buggy line marked |
| B05 | EDIT | AgentEdit | line 6 struck → replacement types · "1 line changed · 9 untouched" |
| B06 | VERIFY | AgentVerify | ✓ ✓ F ✓ · "1 failed, 3 passed" · failure verbatim |
| B07 | ITERATE | AgentIterate | read failure → round(…, 2) → ✓✓✓✓ "4 passed" · "messages from a human: 0" |
| B08 | LOOP | AgentLoop | ring Explore→Edit→Verify→Iterate, marker laps twice · pass 1 ✗ / pass 2 ✓ |
| B09 | VERDICT | ClaudeVerdictArtifact | 7 lines incl. tests caveat + human review |
| B10 | YOUR TURN | ClaudeComposerAsk | prompt read aloud |
| B11 | OUTRO | HaiOutro | HAI mark · title · Subscribe · "Narrated by an AI voice." |
