# PEDAGOGY — From CLI to API (hai cli-explainer, patent agent progress video 8)

A progress-recap video documenting the real FastAPI backend build wrapping the already-verified ClaimsAgent and LineageAgent, including a real git mistake that briefly cost an uncommitted file, its recovery, and a separate real documentation gap found and fixed in the same pass.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real loss, stated plainly, with the real cause named immediately ✓
- B01 — the real, general reason for an API over a CLI ✓
- B02 — the real API design, explicitly not a reimplementation of already-tested logic ✓
- B03 — the real git mistake, in the actual sequence it happened ✓
- B04 — the honest recovery: just real content that still existed locally, recommitted properly ✓
- B05 — the second real, honest find, fixed in the same pass rather than left for later ✓
- B06 — HANDOFF, a runnable check that generalizes the real lesson ✓
- B07 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| The git divergent-branches error and its exact fix sequence | Real terminal output, this session | OK — matches the actual commands and results |
| "the uncommitted new file didn't survive it" | Real git status/log output confirming api.py was absent after the rebase | OK — directly observed |
| "the same content still existed locally" | The file was regenerated from source already verified earlier | OK — a real, available recovery path |
| The README merge gap | Real grep output showing patent_reader.py and updated lineage numbers absent from main | OK — directly observed before being fixed |

## Friction protected

- Kept: B03 and B04 present the mistake as a real consequence of an ordinary git habit, not a rare failure — the handoff exists because this is a common, repeatable trap.
- Kept: B05 presents the missed README merge as a find made while fixing something else, honestly how it happened.

VERDICT: PASS
