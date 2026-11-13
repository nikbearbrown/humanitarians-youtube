# PEDAGOGY — Who Can Approve? (claude-hai · Vendor Intelligence weekly update, ~2.5min)

**Genre:** weekly project update / changelog (neutral framing). One ticket: split the
reviewer and viewer dashboards.

**Light throughline (verdict):** separate what people can *do*, not just what they see —
and watch for inputs that go nowhere.

**Audience (HAI):** followers of the Fellows' build; anyone building tools with a
view/act distinction and human review.

## Act structure
- B00 ASK (composer) — approve was on the public page; corrections vanishing ✓
- B01 THE COUPLING — reviewer panel bolted onto the public search page; anyone could
  approve; no view/act line ✓
- B02 THE SPLIT — index.html now a clean viewer (1,131 → 983) linking to a new
  review.html (366 lines: confidence chips, evidence, anomalies, inline editor, approve,
  offline fallback) ✓
- B03 THE SILENT BUG — a "notes / corrected brief" textarea only sent `notes`;
  corrections filed as notes; corrected-brief API unreachable; now fields separated,
  `brief` sent only when changed ✓
- B04 verdict · B05 handoff (view vs act; does every field get sent?) · B06 outro ✓
- Body B01–B03 = 4K PIL cards; Claude UI only at B00/B04/B05/B06 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW — verbatim from the change log)
- Reviewer panel was on the public search page → anyone browsing could approve.
- frontend/review.html — 366 lines, new: per-dimension confidence chips colour-coded by
  level, evidence counts, anomalies, full brief, inline brief editor, notes, approve;
  falls back to sample data with an offline banner when the API is unreachable.
- frontend/index.html — reviewer panel extracted, 1,131 → 983 lines; clean viewer with a
  link to the review page.
- Silent bug: textarea labelled "Reviewer notes / corrected brief" but code sent only
  `notes`; corrections silently filed as notes; corrected-brief API capability
  unreachable. New page separates the fields and sends `brief` only when it changed.

## PROOF note (genre caveat)
A changelog, not a framework-first explainer — teaching rubric scores modestly by design.
Production gate: every figure legible (1,131 → 983; 366 lines) and sourced from the
creator's own work. The silent-bug beat (B03) is the strongest, most transferable moment.

## Narration review (GATE P)
Listen for: is "anyone could approve" landed as the real risk? Is B03 (corrections filed
as notes) landed as the silent-failure it is? Are the line counts exact?

VERDICT: PASS