# PEDAGOGY — Starting the Lineage Agent (hai cli-explainer, patent agent progress video 6)

A progress-recap video documenting the first build of the Lineage Agent: a free schema check before writing code, an honest scoping decision, a real bug found through careful field-level inspection, and the fix verified correct even though it didn't change the summary's numbers.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real numbers, stated plainly before the twist ✓
- B01 — the real, free schema check before any code was written ✓
- B02 — the honest scoping decision (backward now, forward deliberately deferred) ✓
- B03 — the real bug: BigQuery's empty-string convention defeating an `is not None` check ✓
- B04 — the honest verification that the fix was correct despite an unchanged summary, checked by hand rather than assumed ✓
- B05 — HANDOFF, generalizing the real lesson ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "twelve real citations... one patent, eleven papers" | Real test_lineage_agent.py + inspect_all_citations.py output, this session | OK — cross-checked by inspecting all 12 raw entries by hand |
| The citation schema fields named | Real BigQuery Schema tab, this session, zero query cost | OK — directly observed, not assumed |
| The empty-string bug | Real debug output showing npl_text='' on an entry with a real publication_number | OK — the literal field value from the actual response |
| "same twelve, same one, same eleven" after the fix | Real re-run of test_lineage_agent.py, this session | OK — an honest result reported exactly as it happened |

## Friction protected

- Kept: B04 explicitly states the numbers didn't change and explains why that's still a real, meaningful verification — rather than implying a "before vs. after" that visibly mattered.
- Kept: B02's honest deferral of forward citations names the real reason (untested, likely expensive query) rather than implying it was ruled out or unimportant.

VERDICT: PASS
