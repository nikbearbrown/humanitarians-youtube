# SOURCES.md — knowledge-cutoff

Checked 2026-10-07 against Anthropic's own pages.

| Beat | Claim | Source |
|---|---|---|
| B00 / B01 / B02 / B09 | Claude learns from training data gathered up to a date; it does not know what happened after it. | Anthropic, [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) — every model row lists a "Training data cutoff" and a "Reliable knowledge cutoff". |
| B03 | Anthropic lists two dates per model: the reliable knowledge cutoff (most reliable) and the training data cutoff (broader data range). | Models overview — "Reliable knowledge cutoff: The date through which the model's knowledge is most extensive and reliable. Training data cutoff … is the broader range of data used." |
| B04 | Between the two dates, knowledge thins; past the training data cutoff the model saw nothing. | **Inference** from the definition above ("most extensive and reliable" up to the first date; training data ends at the second). On screen as ILLUSTRATIVE — no real dates, no measured density. |
| B05 / B08 | What falls in the gap: recent news, current prices/rates/scores/stats, facts about people or products that might have changed. Stable topics (established facts, concepts) depend less on it. | Anthropic, [Web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) — "When Claude searches" lists exactly these categories, and "answers directly without searching" for established facts, math, science fundamentals, coding concepts. |
| B06 | Ask about something that changed and you may get the old answer. | **Inference** (direct consequence of the snapshot). Worked example is ILLUSTRATIVE — no real tool or version numbers. "May", not "will". |
| B07 | Fix 1: paste a current source into the chat. Fix 2: web search, which brings live results with citations. | Web search tool — "real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations." Pasting: content in the request is in the context window ([Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows); see claude-liam-context-window/SOURCES.md). |
| B10 | Asking Claude its cutoff and what in a field may have changed. | Prompt for the viewer, not a factual claim. |

## Corrections applied (DOUBLE-CHECK LAW)

- **No dates or model names on screen or in narration.** The per-model dates
  (models overview, [Transparency Hub](https://www.anthropic.com/transparency))
  change with every release — stripped so the reel doesn't date.
- B03 first draft implied the training range is always later than the reliable
  date. On the current lineup both dates are the same month, so the card says
  "The broader data range" — the doc's own word — not "later".
- B06 / B04 hedged ("may", "thins") and labelled ILLUSTRATIVE — not presented as measured behaviour.
