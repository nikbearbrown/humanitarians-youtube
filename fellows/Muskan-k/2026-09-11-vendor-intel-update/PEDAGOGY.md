# PEDAGOGY — This Week's Fixes. (claude-hai · Vendor Intelligence weekly update, ~2.5–3min)

**Genre:** weekly project update / changelog (creator chose neutral framing — not
a single-framework teaching explainer). Covers three real engineering tasks on
the vendor-intelligence system.

**Light throughline (verdict only):** a confident number can be pure noise —
clean the inputs, fail closed when unsure, and log what actually happened.

**Audience (HAI):** followers of the Fellows' build; smart people who want to see
how a real AI system gets debugged and hardened.

## Act structure
- B00 ASK (composer) — what broke this week, what got fixed ✓
- **Task 1 — wrong-company news:** B01 problem (Scale AI: 72/76 signals were other
  companies'; score 75, 25 pts from an Indian ed-tech raise) · B02 fix (check how
  the name is USED; cleaned 72 rows w/ backup; 75 → honest UNKNOWN) ✓
- **Task 2 + 3a — stability:** B03 (retired model swapped, ~half cost, token limit
  raised; deprecated lib migrated; 4 deps version-locked, 2 breakages this week) ✓
- **Task 3b — the check hardened:** B04 (role-first: 10/16 → 16/16; works for
  unconfigured names) ✓
- **Task 3c — fail closed:** B05 (~1 in 4 checks failed; old code failed OPEN →
  now rejects on uncertainty) ✓
- **Task 3d — observability:** B06 (real prompt/response/tokens; phantom calls
  removed) ✓
- B07 verdict · B08 handoff (audit one number your tools report) · B09 outro ✓
- Body B01–B06 = 4K PIL cards; Claude UI only at B00/B07/B08/B09 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW — verbatim from the creator's change log)
- 72 of 76 Scale AI signals were other companies'; 21 counted as funding; score
  75 with 25 pts from an Indian education company's raise; "raised $1B to scale AI".
- Cleaned 72 rows, backup first; score → UNKNOWN, flagged for review.
- Retired model swapped to current, ~half cost (less internal reasoning), token
  limit raised (was returning empty summaries).
- Deprecated library (builds all 5 agents) migrated; 4 dependencies version-locked;
  two build breakages this week from deps changing underneath.
- Role-first check: 10/16 → 16/16 on unseen cases; works for unconfigured names.
- ~1 in 4 checks failed at old token limit; old behaviour assumed a match on
  failure → changed to reject (fail closed), matching the instruction.
- Observability stored a hand-written summary instead of the real request/response;
  now logs real prompt/response/token counts; also stopped logging phantom AI calls
  (keyword-matched headlines skip the AI) that inflated cost.
- No invented figures; nothing beyond the change log.

## PROOF note (genre caveat)
This is a changelog, not a framework-teaching explainer, so PROOF's teaching
rubric (explicit framework / worked example / falsifiability) is a loose fit and
will score modestly by design. The production gate should still PASS: every claim
carries a legible on-screen number, and the figures are the creator's own.

## Narration review (GATE P)
Listen for: are the numbers exact and legible? Does each task read clearly on its
own card? Is B05 (fail closed) landed as the scariest, most important fix?

VERDICT: PASS — human elected "run straight through" (established workflow);
narration self-reviewed against the change log before audio generation.
