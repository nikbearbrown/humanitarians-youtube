# FACTCHECK — claude-liam-context-window (12-beat / 60s cut)

Status: **All rows verified against Anthropic's own docs, except row 6 (marked
inference — no Anthropic source found).** Same claims as the long cut;
renumbered to the new 12-beat structure. Full source URLs, quotes, and
correction history: `SOURCES.md`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00/B02/B03 | System prompt, tools, conversation history, your message, AND Claude's own reply all count toward the context window | ✓ PASS | Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) — verbatim | — |
| 2 | B06 | "Context rot" — recall can slip as tokens grow; more context isn't automatically better | ✓ PASS | Anthropic, Context windows doc — verbatim named term | — |
| 3 | B07 | What happens at the ceiling depends on the app: a hard error, server-side compaction (summarize), or a chat client's rolling FIFO (drop oldest) | ✓ PASS | Anthropic, Context windows doc — three distinct documented mechanisms | — |
| 4 | B06/B08 | The context window ceiling is fixed per model and does not grow mid-conversation | ✓ PASS | Anthropic, Context windows doc | — |
| 5 | B08 | Filling more of a larger window costs more to process | ✓ PASS (inference) | Anthropic's standard per-token pricing model — not a verbatim quote, logged as inference in SOURCES.md | Narration says "filling more of it costs more," not "a bigger window costs more" — keeps the claim about filling, not possessing |
| 6 | B05 | Code, numbers, jargon, and non-English text tend to cost more per word | FLAGGED — inference, not Anthropic-sourced | General BPE-tokenizer behavior; no Anthropic doc found stating this directly | Kept, "tend to" language. No on-screen disclaimer, per prior explicit user instruction — see BUILD-LOG.md item 2 |
| 7 | B06 | Illustrative numbers (room-remaining %, relative scale values in B08: 1/4/16/64) | N/A — not a factual claim | Invented for illustration only | Marked `ILLUSTRATIVE` on screen in both beats; never presented as measured data |

No editorial flourishes beyond the illustrative chart values already disclosed
above. No claims were added or altered in the 60s compression — only cut,
merged, or reworded for length. See `SOURCES.md` for the full compression log.
