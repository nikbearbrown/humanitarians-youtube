# SOURCES — How the Tutor Stays Grounded in Your Textbook

Every factual claim in the narration traces to code read on **2026-09-08** in
`medhavi-quantum-volume-1`, not to documentation. `medhavi-cancer` shares the same
architecture; `physics-vol-1` differs (see Corrections).

| Claim (beat) | Source |
|---|---|
| The model is rented and interchangeable; nothing is trained or fine-tuned (B00, B01, B02) | `lib/chat-orchestrator.ts:7` — the generation model is read from an environment variable at request time |
| Four steps run before anything reaches the model (B03) | `app/api/analyze-context/route.ts` (the check — no model call, hand-written patterns) → `pickMoEExpert` (how to teach it) → `searchWithPlan` (the search) → the assembled message list at `lib/chat-orchestrator.ts:335` |
| Retrieved passages are pasted above the question as plain text (B01, B03) | `lib/chat-orchestrator.ts:253–258` — `SOURCES:` block prepended to `QUESTION:` |
| Nothing is retained between questions (B01) | No persistence of retrieved chunks anywhere in `streamChatOrchestrated`; only the conversation turns go to memory |
| The book is cut into small pieces and written to one index file at build time (B05) | `lib/chunk-content.mjs:14` — target chunk size 1,100 characters; `scripts/index-build.mjs:13–14` — writes a single `.orama/docs.json` |
| The index is rebuilt on every build and every dev start (B06) | `package.json` — `index:build` runs ahead of both `build` and `dev` |
| A content fix reaches the tutor in about a minute (B06) | Consequence of the above: rebuild + redeploy, no retraining path exists in the codebase |
| A stale index degrades silently (B06, B07) | No staleness check exists anywhere; `lib/local-orama.ts:301` falls back to an in-memory rebuild instead of erroring |
| A chunk carries a section, a URL, a keywords line and content (B05) | `lib/local-orama.ts:16–25`; emitted at `scripts/index-build.mjs:203–211` |
| The keywords line is weighted five times heavier than body text (B05) | `lib/local-orama.ts:355–360` — `boost = { keywords: 5, title: 3, section: 2, content: 1 }` |
| A search engine does not read "1.13" as a word (B05) | `lib/local-orama.ts:206–228` — the tokenizer splits it, which is precisely why `exactLookup` exists to bypass scoring for cited identifiers |
| The passages used are visible to the reader (B02, B07) | `lib/chat-orchestrator.ts:310–323` — the sources are streamed to the client before the answer text begins |

## Corrections applied

1. **Model names and version numbers removed everywhere** — narration and on-screen
   text. They date a video within months, and the episode's own argument is that the
   model is interchangeable. The video says "rented, off the shelf" instead.
2. **"Changing the model is a one-line edit" dropped entirely.** True for
   `medhavi-quantum-volume-1` and `medhavi-cancer`, but `physics-vol-1` hardcodes its
   model at `app/api/chat/route.ts:10` with no environment variable. Rather than qualify
   it on camera, the claim was cut.
3. **Embeddings and hybrid search left out.** Real and significant — including the fact
   that hybrid search needs its key at build time, not run time, and silently degrades
   to keyword-only without it. But it is a second idea, and this episode carries one.
   It belongs in a longer cut.
4. **"The closest passages" (B03) is deliberately vague.** The code requests ten and may
   return fewer after de-duplication, so no number is stated on screen.

## Deliberately not claimed

The concept-map pipeline, and any downstream consumer of exported concept maps, sit
outside these repositories. Neither is referenced in this episode.
