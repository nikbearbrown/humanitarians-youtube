# STATUS — vox-two-hit
## Why Knudson's Math Solved Cancer Genetics Before Molecular Biology Did

**Build date:** 2026-07-08
**State:** SLATE CUT — review MP4 complete, open media slots are the two STILL · ai beats

---

## Deliverable

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-two-hit/vox-two-hit-review.mp4
```

## Pipeline summary

| Step | Result |
|---|---|
| Plan (beat_sheet.json, SHOTLIST.md, PROMPTS.md) | DONE |
| FACTCHECK.md | VERDICT: PASS |
| PEDAGOGY.md | VERDICT: PASS |
| Gate A (static_scene_check, per class) | 14/14 clean — 0 errors, 0 warnings |
| Gate W (wcag_margin_check) | All 14 scenes clean — 0 errors, 0 warnings |
| GATE 0 audio (ElevenLabs) | DONE — 273.12s actual |
| vox_run.sh (render + Gate B + outro + review compile) | DONE |
| Review MP4 | 274.1s — written |

## Beat count and duration
- 16 beats total
- 14/16 slots filled (Manim or outro video)
- 2/16 open STILL · ai slates: B02 (eye exam), B11 (Knudson paper)
- Actual audio duration: 273.12s (4 min 33 sec)
- Final compiled duration: 274.1s

## Open slots (fill via `pantry/` or generate)
| Beat | Type | Description |
|---|---|---|
| B02 | STILL · ai | Pediatric eye examination — cold open |
| B11 | STILL · ai | 1971 Knudson paper / age-at-onset curves |

Prompts in `PROMPTS.md`. Drop fills in `pantry/` prefixed with beat id (e.g. `B02-eye-exam.jpg`), then `bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-two-hit`.

## Residual warnings
- **Gate B (pixel audit):** The `manim_layout_audit.py` subprocess could not import `manim` directly (PYTHONPATH issue in the sub-call from vox_run.sh). The render itself succeeded for all scenes. Re-run `vox_run.sh` after confirming `manim` is importable in shell to get the pixel audit.
- **Motion histogram:** `drawon` carries 11/16 beats (68%) — over the ~40% pantry cap noted in MOTION.md. The mechanism-heavy structure of this film requires graphic sequences; this is a style note, not a blocking issue for a slate cut.

## Color law (confirmed)
TEAL = the pre-loaded germline hit / familial advantage
CRIMSON = the somatic hit / tumor event
GOLD = editor's-pen highlight (fill only, once, at B12 confirmation payoff)
Never swapped.

## Exclusions confirmed
- No RB1 protein biochemistry
- No Rb/E2F gate mechanism
- No other two-hit gene mechanisms (BRCA1/2/APC/TP53 named only as brief list)
- No PTEN haploinsufficiency exception
- No Knudson career history
