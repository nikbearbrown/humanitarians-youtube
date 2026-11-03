# SOURCES — What Is a Concept Map

## Narration

Every spoken line is **verbatim** from [`script.md`](script.md).
Nothing was paraphrased, compressed, or added — with one exception, requested by
the human and not present in the source script:

> **B00:** "Hi, I am Chaitanya, and this video is about the Concept Map subsystem
> audit — schema, S3 layer, and why the verified output currently has zero
> consumers."

Verified as an exact string match against the requested wording. The only
transformation on the TTS path is brutalist's standing symbol map, which renders
`—` as a comma pause; no words change.

Scene-to-beat mapping: B01–B09 = the script's SCENE 1–9, in order, unsplit.
Multi-paragraph VO within a scene (Scenes 3, 4, 5, 6, 7, 8, 9) is concatenated
into that scene's single beat, matching Appendix B's nine setups.

## On-screen text

All 17 strings in the script's Appendix A are set, in the scene the appendix
assigns them to. Values in the FIG. 03 / FIG. 04 node record are the script's
own printed values.

Two on-screen strings are **not** from Appendix A, both on B00 (the requested
intro beat, which the script does not cover): `MEDHAVY RESEARCH LOG` and
`2026-08-28 · CONCEPT MAP SUBSYSTEM AUDIT`. Both are drawn from the script's own
front-matter (Series, date, Source line).

Two node-record rows appear on screen that the script's Appendix A does not
print — `wikipedia_categories` and `source_url` — because Scene 6 strikes them
and they must exist to be struck. Their values are the only invented strings in
the build:

| Row | Value shown | Status |
|---|---|---|
| `wikipedia_categories` | `["Taxanes", "Antineoplastic"]` | **Plausible, NOT verified against the fixture** |
| `source_url` | `en.wikipedia.org/wiki/Paclitaxel` | **Plausible, NOT verified against the fixture** |

Flagged rather than buried: these two are on camera for ~20 s of B06. If exact
fidelity to `scripts/20260421_120000.json` matters, replace them in
`scenes/render_scenes.py` → `NODE_ROWS_FULL`. Every other value in that table is
the script's.

## Claims spoken on camera

The script's Appendix C sources each claim to a file and line in the
`medhavi-hub` repository, verified by the script's author against branch
`chaitanya` at commit `7f10aaa` (2026-08-24):

| Claim | Source per Appendix C |
|---|---|
| Node fields and shape | `types/concept-map.ts:10` |
| Paclitaxel record, prereq = microtubules | `scripts/20260421_120000.json` |
| 25 nodes, 18 prerequisite edges, 0 dangling | Both fixtures, verified by count |
| Confidence 9 high / 10 medium / 6 low | `scripts/20260421_120000.json` |
| 2 nodes flagged `thin_content` | `scripts/20260421_120000.json` |
| Export blocked while any node pending | `app/api/concept-map/sessions/[id]/export/route.ts:38` |
| Three fields stripped on export | `.../export/route.ts:62` |
| Prerequisites copied verbatim, not re-validated | `.../export/route.ts:76` |
| Zero readers of the verified prefix | `grep`; `writeVerifiedMap` has no counterpart |
| `VerifiedConceptMap` imported by 2 files only | `lib/concept-map/s3.ts`, `.../export/route.ts` |
| Consumption is roadmap, not shipped | `DEVELOPER.md:569` |

**Independent verification was not performed by this build.** Those paths live
in a different repository at a specific commit; the numbers are reproduced on
the script's own authority. If any have drifted since `7f10aaa`, the video still
states them. Re-checking them is a worthwhile pass before the reel goes anywhere.

## Deliberately not on camera

Per the script's own closing note: the import/permissions defects from the audit
(missing run picker, instructor import contradiction, unenforced `textbook_id`
invariants). They are implementation bugs, not part of *what a concept map is*,
and are held for a separate segment.

## Toolchain

| Component | Version / source |
|---|---|
| Narration | Kokoro-82M via `kokoro-onnx` 0.6.1, voice `am_onyx` ("Onyx" / Liam) |
| Kokoro model | `brutalist/runtime/models/kokoro/kokoro-v1.0.onnx` (read-only) |
| Scene renderer | `scenes/render_scenes.py` — Pillow 10.4.0 → ffmpeg |
| Assembly | `brutalist/runtime/scripts/compile.py` via `./art final` (read-only) |
| Display face | Helvetica Neue Bold (`/System/Library/Fonts/HelveticaNeue.ttc`, index 1) |
| Mono face | Menlo Regular/Bold (`/System/Library/Fonts/Menlo.ttc`, index 0/1) |

No paid service, no API key, no network call at build time beyond the one-time
`pip install kokoro-onnx`.
