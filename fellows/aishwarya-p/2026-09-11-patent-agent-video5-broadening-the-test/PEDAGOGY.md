# PEDAGOGY — Broadening the Test (hai cli-explainer, patent agent progress video 5)

A progress-recap video documenting deliberate broader-domain testing of the Claims Agent, a real parser bug it uncovered, the verified fix, and an honest, unresolved pattern in the classifier's results.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real anomaly (0 claims parsed on a patent with 14) ✓
- B01 — the real mechanism (claim-numbering format difference, "1." vs "1 .") ✓
- B02 — the real fix, verified against both the new and the original format ✓
- B03 — the real classifier results across 4 domains, zero refusals on this batch ✓
- B04 — the honest open question (8/8 readings narrow/defensive) — explicitly not concluded either way ✓
- B05 — HANDOFF, a runnable prompt teaching the same real discipline (empty parser output is a signal to inspect, not to assume) ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "one of them came back with zero claims parsed — on a patent that had fourteen" | Real test_broader_domains.py output, this session, confirmed by inspect_parse_failure.py | OK — both the failure and the real claim count are directly observed |
| "1 ." vs "1." formatting difference | Real raw claims text pulled and inspected by hand, this session | OK — the actual quoted fragment matches the real BigQuery response |
| "eight independent claims... zero refusals on this batch" | Real test_broader_domains.py output after the fix, this session | OK — real counts from real output |
| "8 of 8 readings: narrow / defensive" | Real classifier output, this session | OK — accurately counted, not rounded or characterized more strongly than the data supports |

## Friction protected

- Kept: B04 explicitly states the open question is NOT concluded either way, offering both real candidate explanations (patent drafting reality vs. classifier bias) without picking one — this matches the actual epistemic state, which is genuinely uncertain.
- Kept: B05's handoff generalizes the real lesson (empty parser output warrants inspection, not assumption) rather than only describing what happened to this one patent.

VERDICT: PASS
