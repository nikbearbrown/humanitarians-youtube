# QC STATUS — Compiling Is Not Migrating.

Build date: 2026-10-07 · 13 beats · 3:14 measured audio · Kokoro `am_onyx` · $0.00

## Deliverables

| File | Spec | Duration |
|---|---|---|
| `hussain-snowshift-migration-overview-4k-16x9.mp4` | 3840×2160, 24fps, AAC 48kHz stereo | 194.04s |
| `hussain-snowshift-migration-overview-4k-9x16.mp4` | 2160×3840, 24fps, AAC 48kHz stereo | 194.04s |

The 9:16 is a **native reflowed render**, not a crop: `./art vertical` rewired all
13 beats to registered `*916` compositions and every beat was re-rendered portrait.

Both files decode end to end with zero errors. Narration: mean −27.2 dB, peak −3.0 dB.

## How the masters were assembled

`compile.py` conformed every beat for both aspects, then refused to promote a clean
master because `final_frame_check.py` (GATE V) reports MAJOR defects (below). As in
the Cortex reel (`hussain-snowflake-cortex-triage`), the masters were assembled from the compiler's own conformed clips (`clips/concat.txt`,
`vertical/clips/concat.txt`) with its measured narration track
(`clips/_work/master.wav`). The unmodified GATE V was then run against each master.
They have **not** passed the house gate; promoting them formally is a human call.

## GATE V — on the assembled masters

| Aspect | BLOCKER | MAJOR |
|---|---|---|
| 16:9 | **0** | 3 |
| 9:16 | **0** | 2 |

- **B01 underfill (both aspects, mid-beat samples).** B01 is the
  BrutalistHesitantWriter typing beat: at 50% and 85% of its span the overview is
  still being written, so most of the frame is empty by construction. Same finding,
  same cause, as the Cortex reel (see its QC-STATUS.md). Verified on the last frame:
  both corrections land and "Migrating is proving. / Compiling is the start." is
  complete before the cut.
- **B02 low-contrast (16:9 only).** Stage folders not yet revealed sit at 40% opacity
  and read as faint text. **Fixed in source** (`SnowshiftIllus.tsx`, 0.6 floor) but
  **not re-rendered**: the re-render job was stopped by Claude Code for low system
  memory, and the human chose to assemble with the current beats.

## Known cosmetic issues accepted for this cut

Fixed in source, not re-rendered (same reason as above):

- 9:16 B02, B03, B05 — the source footnote is cut short with an ellipsis.
  (B06–B08 rendered after the fix and wrap correctly.)
- 9:16 B03 — code text is smaller than intended.

To pick these up: `remotion_scenes.py <reel> --only B02 --force`, and the same on
`vertical/` for B02, B03 and B05; then recompile and reassemble.

## Defects found and fixed during the build (by reading 4K frames)

1. B01's second correction ran past the beat ("you are |"): the writer adds pauses per
   word and ~1.3s per correction, so three lines could not finish in 9.7s. Rewritten to
   two lines with the same claim.
2. B03 strike lines spanned the column instead of the struck text; pairs were small in
   half-width cards. Strikes now inline; pairs run as large full-width rows.
3. B05 cards were tall empty pillars. Each stage now fills as it runs; the failure stops
   half-filled in the warn tint; type enlarged.
4. B06, B07, B08 type enlarged to fill their panels.
5. Every pending (not-yet-revealed) element raised from 12–25% to ≥40% opacity
   (legibility floor).
6. Root.tsx registrations written as literal `id="…"` entries — `shorts.py` and the
   scene index grep for them, so generated ids would have blocked `./art vertical`.

## Not verified

- Nothing in this reel has been reviewed by the presenter yet; GATE P
  (`PEDAGOGY.md`) is pending his sign-off.
- B09 states the snowshift migration has not run against a live Snowflake account.
  True on 2026-10-07; re-record B09 after the first live deploy.
