# FACTCHECK — A Blank Page and 49 AI Figures

Every claim spoken on camera, checked against its source.

**Checked against:** local clone of `Medhavy/bio-art` (`main`), with the viewer fix applied.
**Checked on:** 2026-11-02.

| # | Beat | Claim on camera | Source | Verdict |
|---|---|---|---|---|
| 1 | B03 | 234 of the 245 catalog entries have no `file` field | `index.json`: 245 entries, 234 without `file` | **PASS** |
| 2 | B03 | The crash was a TypeError at module load, from `chapterFromFile(entry.file)` | `viewer-fix.diff` — the old `loadFigures` mapped every entry through it | **PASS** |
| 3 | B05 | Vite was only serving `images/`, so `figures/` would 404 | `viewer-fix.diff`, `vite.config.js` | **PASS** |
| 4 | B06 | 49 molecule and drug figures | `index.json`: 49 entries with category `molecule` | **PASS** |
| 5 | B06 | 16 are "pixel-identical"; 15 more share a second template; 31 of 49 (63%) are one of five | audit table; PNGs re-checked | **PARTIAL** — no two PNGs are byte-identical (49 distinct MD5s). Many are visually near-identical: the closest pairs differ by < 1/255 mean grey at 64 px. Clustering at a threshold of 3/255 gives groups of 12, 8, 7, 6, 3, 2, 2 — not 16 and 15. 63% stands as the audit's visual judgment. |
| 6 | B07 | Zero of the figures attempt a chemical structure — grep for skeletal formula, bond angle, chemical structure | `grep -rliE` over `annotations/` (234 files): 0 matches | **PASS** |
| 7 | B01 | "Four separate bugs were stacked" | B01 names the auth prompt plus three: npm cache, dev server folder, loader | **PARTIAL** — four only if the clone's auth failure counts; the sentence lists three after "four" |

Five pass, two partial. Neither partial changes the reel's argument; both change a sentence.
