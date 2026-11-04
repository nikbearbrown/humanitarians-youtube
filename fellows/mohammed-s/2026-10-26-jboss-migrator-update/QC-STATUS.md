# QC STATUS — Today, Batch Mode Lands.

Build date: 2026-11-03 · 10 beats · 2:12 measured audio · Kokoro `am_onyx` · $0.00

| File | Spec | Duration | Status |
|---|---|---|---|
| `hussain-jboss-migrator-update-2026-11-03-4k-16x9.mp4` | 3840×2160, 24fps, AAC 48kHz stereo | 132.08s | **Approved by presenter** |
| 9:16 (2160×3840) | all 10 portrait beats rendered in `vertical/media/` | — | Not compiled (presenter: not needed for now) |

## Presenter approval

| Field | Value |
|---|---|
| status | approved |
| reviewer_type | human |
| reviewed_by | Mohammed Hussain (presenter) |
| reviewed_at | 2026-11-03T23:34:48-05:00 |
| subject | `hussain-jboss-migrator-update-2026-11-03-4k-16x9.mp4` |
| subject_sha256 | `8ef7d279103825aba864fa3fc84c521e4d49d8cbf8711801f34dcb1f04177bea` |

The presenter stated in the build session that he reviewed the video and asked for it to be approved;
this record was written at his request. The approval covers only the file with the hash above —
any re-render produces a new hash and needs a new review. This is an attestation in the reel's
paperwork, not an authenticated signature (see brutalist.art `docs/PIPELINE-SAFETY.md`).
The toolkit's own approval subjects for this reel are empty (`build_safety.py --fingerprints` → `{}`),
so there is no `metadata.approvals` record to fill.

## Automated checks (16:9)

- `compile.py --height 2160`: GATE F (FACTCHECK/SHOTLIST/PROMPTS) pass, GATE V **0 BLOCKER · 0 MAJOR**,
  promoted to `brutalist.art/renders/` with `build-state.json` status `ready`, same sha256 as above.
- Full decode: zero errors. Audio mean −27.2 dB, peak −5.7 dB.
- Frame review by eye at 55% / 95% of every beat (`_qc/sheet169_*.png`).

## Fixed during the build

- B01: narration claimed every stage has unit tests; `baseline.py` has none → "five of the six" (FACTCHECK.md).
- B09: outro underfilled the safe area (48%) → title "Today, Batch Mode Lands." + repo URL subline (68%).
- 9:16 B05: terminal lines clipped / overflowing the card → re-wrapped to 12 lines; label now `bash`.
- 9:16 B09: subline wrapped mid-URL → short subline.

## Known, accepted

- B00/B08: the composer's grey output lines are small by component design; readable at desktop size.
- Compiler lint: palette=claude wants `ClaudeTitleOutro`, but that card is locked to @NikBearBrown
  (OUTRO-LOCK.md), so the presenter's own `CortexTitleOutro` is used, as in the previous reel.
