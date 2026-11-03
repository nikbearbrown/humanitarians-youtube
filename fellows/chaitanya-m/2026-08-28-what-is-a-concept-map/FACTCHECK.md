# FACTCHECK — What Is a Concept Map

Every claim spoken or set on camera, checked against its source.

**Checked against:** `medhavi-hub` @ `7f10aaa` (2026-08-24), branch `chaitanya` —
the exact commit the source script cites in its Appendix C.
**Checked on:** 2026-08-30, at port-in time.
**Method:** files read directly; fixture counts recomputed from the JSON, not
copied from the script.

This supersedes the "independent verification was not performed by this build"
caveat in [`SOURCES.md`](SOURCES.md). It has now been performed.

## Verdicts

| # | Claim on camera | Source | Verdict |
|---|---|---|---|
| 1 | Node fields and shape | `types/concept-map.ts:10` (`PipelineNode`) | **PASS** — interface begins at line 10; all 12 fields match |
| 2 | Paclitaxel: aliases `["Taxol","paclitaxel"]`, ch 22 § 1, `factual`, prereq `cancer_22_1_microtubules`, confidence `high`, `thin_content: false` | `scripts/20260421_120000.json` | **PASS** — exact match, field for field |
| 3 | 25 nodes | both fixtures | **PASS** — 25 in each |
| 4 | 18 prerequisite edges, 0 dangling | both fixtures | **PASS** — recomputed: 18 edges, every target resolves to a node in the file |
| 5 | Confidence 9 high / 10 medium / 6 low | `scripts/20260421_120000.json` | **PASS** — recounted: 9 / 10 / 6 |
| 6 | 2 nodes flagged `thin_content` | `scripts/20260421_120000.json` | **PASS** — 2 |
| 7 | Knowledge types 13 factual / 9 conceptual / 3 procedural | `scripts/20260421_120000.json` | **PASS** — 13 / 9 / 3 (script Appendix C only; not spoken on camera) |
| 8 | Export hard-blocked while any node is `pending` | `app/api/.../export/route.ts:38` | **PASS** — `if ((pendingCount ?? 0) > 0)` returns HTTP 400 `Export blocked` at line 38 |
| 9 | Three fields stripped on export — `wikipedia_categories`, `confidence`, `source_url` | `app/api/.../export/route.ts:62` | **PASS** — the `VerifiedConceptMap` node projection carries 9 fields; those 3 are absent |
| 10 | Prerequisites copied through verbatim, not re-validated | `app/api/.../export/route.ts:76` | **PASS** — `prerequisite_nodes: node.prerequisite_nodes`, no filter against surviving IDs |
| 11 | Removed nodes are dropped from the export | same route, node query | **PASS** — `.neq('review_status', 'removed')`. Combined with #10, the dangling-edge defect in SCENE 8 is real, not hypothetical |
| 12 | Zero readers of the verified prefix | `grep` across repo | **PASS** — `writeVerifiedMap` is defined at `lib/concept-map/s3.ts:163` and called once, at `export/route.ts:81`. No `readVerifiedMap`, no counterpart of any name |
| 13 | `VerifiedConceptMap` imported by exactly 2 files | `lib/concept-map/s3.ts`, `.../export/route.ts` | **PASS** — those two import it; `types/concept-map.ts:71` defines it |
| 14 | Consumption is roadmap, not shipped | `DEVELOPER.md:569` | **PASS** — "Concept-map-aware navigation (consuming verified maps, §10)" appears in a forward-looking deliverables list for the next-generation chassis, under a Fall pilot plan |

## FAIL — one on-screen value is wrong

**Beat B06, `wikipedia_categories` row.**

| | |
|---|---|
| **On screen** | `["Taxanes", "Antineoplastic"]` |
| **In the fixture** | `["Taxanes", "Mitotic inhibitors", "Chemotherapy drugs"]` |
| **Severity** | Minor — cosmetic, on screen ~20 s, struck through as the VO says it gets stripped |

[`SOURCES.md`](SOURCES.md) flagged this row as invented and "plausible, NOT
verified against the fixture." It is now verified, and it does not match: wrong
second element, and one element short. The narration never speaks the value — it
only names the field — so nothing said aloud is false. But it is a fabricated
value presented as a real record.

**Fix:** `scenes/render_scenes.py` → `NODE_ROWS_FULL`, then re-render B06 and
re-cut. Not blocking, but it should not ship uncorrected.

## PARTIAL — one on-screen value is truncated

**Beat B06, `source_url` row.**

| | |
|---|---|
| **On screen** | `en.wikipedia.org/wiki/Paclitaxel` |
| **In the fixture** | `https://en.wikipedia.org/wiki/Paclitaxel` |
| **Severity** | Cosmetic — scheme dropped, presumably to fit the column |

Also flagged as unverified in `SOURCES.md`. The path is correct; only the
scheme is missing. Acceptable as a display truncation, noted so it is not
mistaken for the stored value.

## Not claimed on camera, deliberately

The import/permissions defects from the underlying audit — missing run picker,
instructor import contradiction, unenforced `textbook_id` invariants — are
implementation bugs, not part of *what a concept map is*. Held for a separate
segment. Nothing in this reel asserts the subsystem is free of them.

## Scope of this check

Claims were verified against the repository at one commit. They were true there
on 2026-08-24 and re-confirmed on 2026-08-30. If `medhavi-hub` moves, the video
still states these numbers — re-check before any re-publication.

Not covered by this check: whether the argument persuades, whether the pacing
works, or anything about the audio. Frame QC covers layout, colour, and
legibility; the rest are human judgments and still open. See the README's
"Open before publication" list.
