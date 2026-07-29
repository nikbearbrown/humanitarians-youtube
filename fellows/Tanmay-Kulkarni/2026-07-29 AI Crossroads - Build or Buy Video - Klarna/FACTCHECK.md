# FACTCHECK — The Artificial Intelligence Crossroads: Build or Buy? (Klarna case)

Beat-by-beat audit, run 2026-07-29 against `beat_sheet.json`. Every claim
checked against the strongest available primary source. Nothing was
silently repaired — every correction below was proposed here first, then
applied only after author review.

| Beat | Claim | Verdict | Evidence | Source | Correction |
|---|---|---|---|---|---|
| B00 | Opening premise | Framing, not factual | — | — | None |
| B01 | Feb 2024, 2.3M chats/30 days | SUPPORTED | Direct company figures | Klarna press release, 27 Feb 2024 | None |
| B01 | "Workload of 700 full-time agents" | QUALIFY | Explicitly workload-equivalence, not a headcount cut | Same | None — spoken line + on-screen sub-label already pair correctly; **documented as a must-preserve pairing**, not to be spoken/shown alone |
| B01 | 67% of chats, 11min→<2min | SUPPORTED | Company-reported | Klarna press release / OpenAI case study | None |
| B01 | "On track for $40M in savings" | SUPPORTED, correctly hedged | Explicitly a projection | Klarna press release | None |
| B02 | "Easiest slice of support work" | QUALIFY → **FIXED** | Analyst commentary, not a Klarna statement | Secondary industry analysis | Narration now reads "Analysts point out..."; visual card label changed from "What shipped" to "What analysts noted" |
| B02 | CEO quote (efficiency/cost → lower quality) | SUPPORTED | Verbatim, correctly truncated | Bloomberg, reported by Forbes/CNBC, May 2025 | Dating tightened: "by 2025" → "by May 2025" |
| B03 | Attribution (Brynjolfsson/Rock/Syverson) | SUPPORTED | Peer-reviewed | NBER WP 25148; AEJ:Macro 13(1), 2021 | None |
| B03 | Mechanism description | QUALIFY | Simplified paraphrase of the paper's actual mechanism, faithful in spirit | Same paper | Documentation only — logged below as paraphrase, not quotation |
| B03 | "The dip isn't AI failing. It's the bill for skipped homework." | CONSTRUCTED (interpretive) | Video's own framing — paper never studied Klarna | Video's own synthesis | Documentation only — logged below as editorial framing |
| B04 | Klarna rehired humans | SUPPORTED | On-record, multiple outlets | Bloomberg/CNBC/Forbes, May 2025 | None |
| B04 | Specific categories (disputes/refunds/hardship) | QUALIFY → **FIXED** | Consistent across secondary analyses, no single primary Klarna statement itemizing these exact categories found | Secondary/blog synthesis (consistent across multiple independent write-ups) | Narration now reads "reportedly for disputes, refunds, hardship cases"; caption now separates the CEO-confirmed fact (rehiring) from the reported detail (task split) |
| B04 | "Routine volume stays with the AI" | SUPPORTED (general level) | Consistent with hybrid-model reporting | Same secondary sources | None |
| B05 | Whole beat (AI's job / human's job) | Editorial framing | — | Video's own thesis (`hai` skill's Irreducibly-Human convention) | Documentation only — not a Klarna-specific claim |
| B06 | Q3 2025 figures (853 agents, $60M, 82%, NPS 73) | SUPPORTED | Consistent across outlets on the Nov 2025 earnings call | Yahoo Finance, CX Dive | None |
| B06 | "The hybrid model is the one that actually holds" | Interpretive conclusion | Reasonable given the recovery, but it's the video's synthesis, not Klarna's framing | — | Documentation only |
| B07 | "Klarna bought, partnered with OpenAI" | SUPPORTED | Confirmed partnership | OpenAI's own case study | None |
| B07 | "...still hit the J-Curve dip, **because** the complementary work lagged" | **UNSUPPORTED as stated → FIXED** | Neither Klarna nor the paper's authors connected the specific dip to "the J-Curve." The CEO's own explanation was "we focused too much on efficiency and cost" — consistent with, but not the same as, a confirmed J-Curve mechanism | — | Reworded from a flat causal "because" to an explicit interpretive lens: "hit a dip that reads like the Productivity J-Curve" |
| B08 | Prompt template | Not a factual claim | — | — | None |
| B09 | Title restate | Not a factual claim | — | — | None |

## Documentation-only notes (no script change, logged for the record)

- **B03**: the on-screen mechanism description is a compressed paraphrase of
  Brynjolfsson/Rock/Syverson's actual model (which is about *measured*
  productivity being under/overstated due to unmeasured intangible
  investment) — faithful in spirit, simplified for a general audience. Not
  a direct quotation from the paper.
- **B03 / B07**: applying the J-Curve *specifically* to Klarna is this
  video's own interpretive move — the paper is a general macroeconomic
  model, not a Klarna case study. The CEO's own words ("focused too much on
  cost, not quality") are consistent with this reading, but the connection
  itself is editorial synthesis, not an established fact. B07's wording was
  corrected accordingly (see table); B03's closing line ("bill for skipped
  homework") is left as clearly-voiced interpretation, consistent with the
  Pragmatist register's own conventions.
- **B05**: the entire beat is authorial framing (the `hai` skill's
  "Irreducibly-Human" aside) — a values statement, not a claim about
  Klarna's internal decisions.
- **B06**: "the hybrid model is the one that actually holds" is the video's
  own reading of the recovery in the numbers, not something Klarna itself
  states in those terms.

## Corrections applied (2026-07-29)

1. B02 narration: "This is the easiest slice..." → "Analysts point out this
   was the easiest slice..."; visual card label "What shipped" → "What
   analysts noted".
2. B02 narration: "by 2025" → "by May 2025".
3. B04 narration: "rehired humans for disputes, refunds, hardship cases" →
   "rehired humans, reportedly for disputes, refunds, hardship cases";
   caption split into CEO-confirmed fact vs. reported detail.
4. B07 narration: "still hit the J-Curve dip, because the complementary
   work lagged the rollout" → "still hit a dip that reads like the
   Productivity J-Curve: the complementary work lagging the rollout".

All four changes applied to `beat_sheet.json` after this audit.

## New beat added after this audit (2026-07-29): B07B

A short "Build or buy? They bought." payoff card, added per author request
after review. Claims: "Klarna bought" — already SUPPORTED (B07, OpenAI
partnership); "still hit the dip" — already SUPPORTED (B02/B03). "The
J-Curve doesn't check your invoice" is rhetorical flourish, not a factual
claim. No new sourcing required — restates already-verified claims from
earlier beats in a punchier form.

## Fifth correction — found during visual QC, not the narration audit (2026-07-29)

B06's on-screen `settleLine` read "the dip passed — because the calibration
work got done" — the same causal overreach as the B07 narration issue above
(the calibration-work explanation was never Klarna's own stated reason),
just missed because the narration audit only checked `narration_text`, not
visual-card prop strings. Fixed to "one year later — the hybrid model
holds," which states the recovery without asserting an unproven cause.
This is a reminder to check on-screen card text for the same class of
issue, not just spoken narration, in future fact-check passes.
