# SOURCES — claude-liam-claude-api

Source skill: `anthropics/skills/skills/claude-api/SKILL.md`

## Verbatim quotes used on-screen

### B01 — TRIGGER text (ClaudeApiAnatomy.tsx)
Source: SKILL.md frontmatter TRIGGER field (verbatim):
> "Read BEFORE opening the target file — whenever: the prompt names Claude/Anthropic in any form; the user asks about an LLM; OR the task is LLM-shaped with provider unstated."

### B02 — Agent tier rule (ClaudeApiSurfaces.tsx)
Source: SKILL.md § Three API Surfaces / Decision criteria:
> "No to any → stay at a simpler tier."

### B03 — Drift table (ClaudeApiDrift.tsx)
Source: SKILL.md § API Drift table (verbatim per row):

Extended thinking stale:
> "thinking: {type: \"enabled\", budget_tokens: N}"

Extended thinking current:
> "thinking: {type: \"adaptive\"} — budget_tokens deprecated on Opus 4.6 / Sonnet 4.6, REJECTED with a 400 on Fable 5 / Sonnet 5 / Opus 4.8 / 4.7"

Web search stale:
> "web_search_20250305 · web_fetch_20250910"

Web search current:
> "web_search_20260209 · web_fetch_20260209 (dynamic filtering) on Opus 4.8/4.7/4.6, Sonnet 5, Sonnet 4.6"

PHP stale:
> "snake_case wire names as named args (max_tokens)"

PHP current:
> "Top-level named args are camelCase (maxTokens). Nested array keys vary — copy from documented example, do not bulk-convert."

Bottom note (verbatim):
> "Several common Claude API shapes changed in 2025–2026. If you recall a pattern from training, verify it against the {lang}/files in this skill before writing."

Source: SKILL.md § API Drift / bottom note

### B04 — Model table (ClaudeApiModels.tsx)
Source: SKILL.md § Current Models (cached: 2026-06-24)
All model IDs, context windows, and pricing are verbatim from this table.

Rule callout (verbatim):
> "Unless the user explicitly names a different model. This is non-negotiable."

### B04 — Date suffix rule (ClaudeApiModels.tsx)
Source: SKILL.md § Model IDs
Demonstrated: `claude-sonnet-4-6` (correct) vs `claude-sonnet-4-6-20251114` (wrong)

## SELF-DEMO declaration
- B03 (ClaudeApiDrift): renders the SKILL.md API drift table verbatim — data is sourced directly from SKILL.md, no paraphrase
- B04 (ClaudeApiModels): renders the SKILL.md current model table verbatim — data is sourced directly from SKILL.md, no paraphrase
