# PEDAGOGY — Confidently Wrong. (claude-hai · project update)

**The ONE insight:** every bug this week was an *unverified assumption* — that
the model had the evidence, that the code fix reached old data, that a system
printing no errors was working. The rule: **don't assume — verify.**

**Audience (HAI):** practitioners/learners; skeptical spine ("no source, no
verdict") applied to LLM output + observability.

## Act structure
- B00 cold-open ask (composer), answered ✓
- B01 empty summaries · B02 invented departure · B03 stale data · B04 silent tracing — the receipts ✓
- B05 verdict (the rule) · B06 handoff (scaffolded task) · B07 title outro ✓
- Body B01–B04 house-style 4K cards; UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## Evidence discipline (DOUBLE-CHECK LAW — every detail from the change log)
| On screen | Source |
|---|---|
| Empty summaries; real filing text unused; before→after (Ajay K. Puri) | Bug 1, edgar_collector.py |
| Invented AMD departure; boilerplate 5.02 title; 400→900 chars | Bug 2, edgar_collector.py |
| Collector skips by headline; backfill dry-run + saves original; 8 rows / 955 total | Bug 3, backfill_edgar_summaries.py, db.py |
| Langfuse traced nothing; broad catch-all; handler API change; verified by fetching trace | Bug 4, agents/llm.py |
| Flush moved to client; would crash briefs; shipped with bug 4 | Bug 5, agents/llm.py |

## Production gate intent (learned from PROOF last week)
- Show the real receipt at assertion: before→after summary text (B01), the actual
  boilerplate title + AMD correction (B02), the counts (B03), the verify step (B04).
- Active task present (B06). Rule stated as a reusable principle (B05).

## Narration review (GATE P)
Listen for: does each beat show the receipt as the voice states it? Is the closing
rule earned by all four bugs?

VERDICT: PASS — sign "VERDICT: PASS" after review.
