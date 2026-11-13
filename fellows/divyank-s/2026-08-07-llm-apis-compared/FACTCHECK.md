# FACTCHECK — Claude, Compared. (OpenAI vs. Anthropic vs. Meta vs. Google)

No book chapter underlies this build. Every pricing/spec claim below was
researched live this session, not recalled from training data, and is
tagged by how it was obtained.

## Anthropic

| # | Claim | Tag | Source |
|---|---|---|---|
| 1 | Claude Opus 5.5: 1M context, 128K max output, $4.00/$20.00 per MTok | Cited, official | `claude-api` skill's cached model table (dated 2026-10-06) — Anthropic's own first-party rates |
| 2 | Claude Sonnet 5.5: 1M context, $2.00/$10.00 per MTok | Cited, official | same source |
| 3 | Claude Haiku 5.5: 1M context, $0.10/$0.50 per MTok (up to 100K-token prompts; $0.50/$2.50 beyond) | Cited, official | same source |
| 4 | Claude Fable 5.1 (most capable): 1M context, 128K max output, $10.00/$50.00 per MTok | Cited, official | same source |

## OpenAI

| # | Claim | Tag | Source |
|---|---|---|---|
| 5 | Current top-tier model: $10.00/$50.00 per MTok (short context, ≤272K tokens) | Cited, official | WebFetch of `developers.openai.com/api/docs/pricing`, fetched this session |
| 6 | Mid-tier model: $2.00/$10.00 per MTok | Cited, official | same |
| 7 | Budget-tier model: $0.10/$0.50 per MTok | Cited, official | same |
| 8 | Context window ~1.05M tokens input, 128K max output, across the current lineup | Cited, official | WebFetch of `developers.openai.com/api/docs/models`, fetched this session |

**Note:** specific model names (e.g. "GPT-6 Astra") are used in the
narration's sparkline labels and ChipGrid captions but are deliberately
*not* spoken as product names in the narration itself, since this
session cannot independently confirm how stable that naming is beyond
the single page fetched. The pricing/context figures themselves are
tied directly to the official docs, not to any specific model name
claim.

## Google

| # | Claim | Tag | Source |
|---|---|---|---|
| 9 | Current flagship: $2.00/$10.00 per MTok through Nov. 30, 2026; $4.00/$20.00 from Dec. 1, 2026 | Cited, official | WebFetch of `ai.google.dev/gemini-api/docs/pricing`, fetched this session |
| 10 | Context window: 1M tokens, stated by Google as a shared input+output window | Cited, official | WebFetch of `ai.google.dev/gemini-api/docs/models`, fetched this session |

## Meta

| # | Claim | Tag | Source |
|---|---|---|---|
| 11 | Meta's newest frontier model (2026) launched as a closed, proprietary, API-only release — a first for Meta's flagship line | Cited, corroborated across 2 sources | WebFetch of `dev.meta.ai` (fetched this session) + a standard-mode WebSearch pass; both independently describe the same closed launch |
| 12 | Meta also shipped a smaller open-weight model under the Apache 2.0 license around the same period | Cited, corroborated across 2 sources | same two sources |
| 13 | Meta operates its own direct hosted API ("Meta Model API") for its current models | Cited, official | WebFetch of `dev.meta.ai`, fetched this session |
| 14 | The historical Llama Community License permits free use/modification but requires a separate commercial license from Meta for a licensee with more than 700 million monthly active users | General/stable | Well-documented, long-standing term of Meta's own published Llama license agreements (Llama 2/3 era); not a perishable claim like a price |

## Explicitly excluded / rejected as sources

- **Third-party pricing-aggregator sites** (returned in initial
  WebSearch passes) were **not used as sources** for any number in this
  video — they gave mutually conflicting figures for the same models
  (e.g. two different numbers for the same Gemini tier) and are
  explicitly flagged by this build as unreliable. Every number actually
  used was re-verified directly against the vendor's own official page
  via WebFetch.
- **No claim about a specific unreleased or rumored model** (e.g. a
  next-generation Llama release some sources speculated about) is
  included — those reports conflicted with each other and were dropped.
- **No benchmark scores, market-share figures, or qualitative
  "best model" claims** are made for any provider.

## Perishability warning

Every price in this video is tagged **current as of October 2026**.
Pricing is the single most perishable category of claim in this
session's own discipline — these numbers will date faster than almost
anything else built this session, including the one already-scheduled
Google price increase (Dec. 1, 2026) baked into this very video.
