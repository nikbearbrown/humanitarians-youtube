# Encrypted Twice

Brutalist 4K explainer on why a stored credential gets a second encryption layer
in the application, above the one the database already provides: storage
encryption defends a disk, and cannot defend a secret from a query the database is
required to answer.

| | |
|---|---|
| Master 16:9 | 3840x2160, 24 fps, 107.3 s (1:47.3) |
| Master 9:16 | 1216x2160, 24 fps, 107.3 s |
| Beats | 8, all filled |
| Voice | Kokoro `am_onyx` |
| Scripted and rendered | 2026-10-28 |
| Renders | `medhavy-credential-encryption.mp4` and `medhavy-credential-encryption-916.mp4`, on Drive |

## What is here

| File | What it is |
|---|---|
| [script.md](script.md) | Narration and art direction |
| [beat_sheet.json](beat_sheet.json) | 8 beats |
| [SHOTLIST.md](SHOTLIST.md) | Per-beat shot plan |
| [FACTCHECK.md](FACTCHECK.md) | 8 rows, one marked VENDOR CLAIM and one a stated transitional weakness |
| [SOURCES.md](SOURCES.md) | Narration provenance and exclusions |
| [PEDAGOGY.md](PEDAGOGY.md) | GATE P |
| [BUILD-LOG.md](BUILD-LOG.md) | Durations and the QC defects |
| [scenes/render_scenes.py](scenes/render_scenes.py) | One renderer serving both aspects |
| [qc-sheet-16x9.png](qc-sheet-16x9.png) | All eight settled frames on one contact sheet |
| [qc-sheet-9x16.png](qc-sheet-9x16.png) | The same settled frames from the native portrait render |
| [beat-sheet-short.json](beat-sheet-short.json) | The 9:16 cut's own beat sheet — the portrait build input |

## Two claims carry qualifications

**Row 2 is a vendor claim.** Supabase's storage-layer AES-256 is their statement,
not something measured here, and the narration says "Supabase applies" rather than
"we verified".

**Row 7 is a transitional weakness, stated on camera.** The decrypt path passes
through any value without the `v1:` marker, so a row written before the encryption
shipped still reads in clear. B06 names it and says it should be removed once every
row has been rewritten.

## No key material anywhere

`v1 : iv : tag : ciphertext` is the field layout. No key, no IV, no auth tag and
no real ciphertext appears on camera or in this folder.

## Frictional log

See [FRICTIONAL.md](FRICTIONAL.md).
