# BUILD-LOG — Encrypted Twice

## Output

| | |
|---|---|
| Master 16:9 | `medhavy-credential-encryption.mp4` · 3840x2160 · 24 fps · 107.333 s |
| Master 9:16 | `medhavy-credential-encryption-916.mp4` · 1216x2160 · 24 fps · 107.333 s |
| Audio | AAC 48 kHz stereo, Kokoro `am_onyx`, per-beat timeline |
| Beats | 8, all filled from `media/` |

## Architecture

Same as `medhavy-role-matching`: toolkit read-only, out-of-tree Pillow renderer,
single stacked column so one layout serves both aspects. The `stack()` and `row()`
helpers came over verbatim; only the scene functions are new.

## Duration drift

Script estimate 98 s from 328 words. Measured 106.8 s of narration, 107.3 s
conformed, about 9 percent over. B04 and B06 both read field names and a format
string, which Kokoro reads more slowly than prose — the same cause as the overshoot
on `medhavy-it-requirements` and `medhavy-lti-tables`.

## Defects found in QC and fixed

1. **B04's field labels crossed the title-safe right edge at 9:16.** Drawn at a
   size derived from the row height with no width check. GATE V flagged it as a
   blocker on two sampled frames.
2. **The fix for defect 1 was itself wrong.** Measuring the longest label was
   written as `max(f"{a}   {b}" for a, b in parts)` without `key=len`, which is a
   lexicographic maximum, not the longest string. It returned `v1   VERSION` and
   sized the font to that, so `iv   INITIALISATION VECTOR` still bled. GATE V
   failed again identically. One keyword.

Both are the same shape as the geometry defects elsewhere in this series: a
measurement was asked for and the wrong thing was measured.

## Lints — reported, not silenced

Same two as the rest of the series: the expected `NO RENDERABLE BEATS` false
positive for this architecture, and a motion label over the 40 percent cap, left
as the script's shot list wrote it.

## Honesty notes carried in the fact-check

Row 2 is marked **VENDOR CLAIM** — Supabase's storage-layer AES-256 is their
statement and was not measured here, and the narration is worded accordingly.
Row 7 is a transitional weakness stated on camera: values without the `v1:`
marker pass through as legacy plaintext.

## Gates

GATE F satisfied. GATE V clean on both cuts after the two fixes.
`PEDAGOGY.md` carries `VERDICT: PENDING` and is not self-signed.

## Not done

No captions or word clock.
