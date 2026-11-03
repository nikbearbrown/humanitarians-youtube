# SHOTLIST — How Facial Recognition Actually Works (And When It Shouldn't)

## 185.17s (measured, 4K master) · 12 beats · all Manim, no pantry/toolkit assets

Rebuilt 2026-08-25/26 per program feedback: two new opening beats added
(B00, B01), the original 8-row shotlist's beats shifted down by 2
(old B00→B02 ... old B07→B09; note the original table below used a
pre-restructure 8-beat numbering that no longer matches `beat_sheet.json` —
this table is now the authoritative one).

| Beat | Act | Lane | Medium | Source/Pattern | Measured Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.60s | SILENT — video title (bracketed by gold rules) + @HumanitariansAI, no narration |
| B01 | INTRO | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 11.66s | Spoken personal-intro card: fellow's name, role chip, one-line thesis summary |
| B02 | HOOK | manim | GRAPHIC | B02_EverywhereHook (scenes.py) | 15.48s | Phone/Airport/Store/Policing chips, then debate framing |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_FrameworkLens (scenes.py) | 11.81s | The reusable lens: 3 questions, shown before any example |
| B04 | MECHANISM | manim | GRAPHIC | B04_PipelineMechanism (scenes.py) | 21.12s | Face → Detect → Embedding → Compare → Score gauge (98%), tagged Q3 |
| B05 | BENEFITS | manim | GRAPHIC | B05_LegitimateUses (scenes.py) | 15.14s | List-reveal, sage checks: accessibility, unlock, missing persons, medical — tagged LOW-STAKES |
| B06 | HARMS | manim | GRAPHIC | B06_HarmfulUses (scenes.py) | 12.38s | List-reveal, crimson marks: surveillance, retail tracking, biometric risk — tagged HIGH-STAKES |
| B07 | EVIDENCE | manim | GRAPHIC | B07_NistEvidence (scenes.py) | 31.27s | NIST FRVT bar chart: most-algorithms gap vs. best-performing near-zero gap; industry dissent (Security Industry Association) named on screen |
| B08 | FRAMEWORK-CALLBACK | manim | GRAPHIC | B08_FluencyTrap (scenes.py) | 12.77s | Split panel: fluent paragraph vs. match score, both "looks certain" |
| B09 | WORKED-EXAMPLE | manim | GRAPHIC | B09_WorkedExample (scenes.py) | 26.86s | The 3-question lens applied live to a retail loss-prevention case |
| B10 | CTA | manim | GRAPHIC | B10_YourTurn (scenes.py) | 17.30s | YOUR TURN — the literal 3-question checklist the viewer can run |
| B11 | SIGN-OFF | manim | GRAPHIC | B11_BrandOutro (scenes.py) | 4.92s | @HumanitariansAI, in for Sai Pranavi J. |

## QC plan (as actually run for the 2026-08-25/26 4K rebuild)
- Pre-flight (before any render): `runtime/qc/static_scene_check.py` (GATE A)
  and `runtime/qc/wcag_margin_check.py --palette humanitarians` (GATE W) per
  touched scene — this reel's palette is `humanitarians`, and `run.sh`'s own
  GATE W call does not pass `--palette` explicitly (it reads
  `$ART_PALETTE`/`$VOX_PALETTE`, default `teardown`), so `ART_PALETTE=humanitarians`
  must be exported before running `run.sh`/`compile.py` or GATE W checks the
  wrong palette's contrast tokens.
- Post-render: `runtime/qc/manim_layout_audit.py` (GATE B, per-scene) and
  `runtime/qc/final_frame_check.py` (GATE V, whole compiled reel) — checked
  against the TRUE clean master (`--mp4 <slug>.mp4`), never the `-slate.mp4`
  review cut, which carries a review-only timecode watermark that produces a
  known false-positive "edge-bleed" BLOCKER on every frame (confirmed again
  in this rebuild — the automated `run.sh` GATE V step defaults to the
  `-slate.mp4` and reported 30 false BLOCKERs; the direct `--mp4` check
  against the true master reported 0 BLOCKER).
- Every GATE V MAJOR finding was reviewed by direct frame extraction
  (`ffmpeg -ss <exact sample timestamp>`), not accepted on the automated
  report alone — this caught one real defect (B04's caption animation
  straddling the 50% sample point) that the report itself only described as
  "low-contrast," and confirmed the other 11 findings were cosmetic
  (whole-frame luminance heuristic false positives, or intentionally sparse
  card layouts). See `BUILD-LOG.md` (2026-08-25/26 entries) and
  `SELF-ASSESSMENT.md`.
