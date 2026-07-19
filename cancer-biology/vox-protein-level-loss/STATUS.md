# STATUS — vox-protein-level-loss
## Why a Cancer With Intact Tumor Suppressor Genes Still Behaves As If They Are Missing

**Built:** 2026-07-08
**Slug:** `vox-protein-level-loss`
**Topic:** CANCER BIOLOGY
**Source:** `cancer-biology/chapters/10-cancer-etiology-viral-and-bacterial-carcinogens.md`

---

## Deliverable

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-protein-level-loss/vox-protein-level-loss-review.mp4
```

**Review MP4:** `vox-protein-level-loss-review.mp4`
**Duration:** 212.3 s (~3:32)
**Beats:** 13
**Slots:** 12/13 filled (B02 is the SLATE — awaits the ai still)

---

## Gate results

| Gate | Result | Notes |
|------|--------|-------|
| Gate P (pedagogy) | PASS | All act-structure items checked |
| FACTCHECK | PASS | All claims verified; illustrative numbers labeled |
| Gate A (static pre-flight) | PASS | 11 clean, 1 benign warn (B04_QuestionCard pure-quote) |
| Gate W (WCAG + margins) | PASS | All 12 scenes clean after W6 fix |
| Gate 0 (audio) | PASS | 13 mp3s generated, timings.json written |
| Gate B (pixel audit) | WARN | Manim module not installed in qc-tooling env; pixel audit could not execute; scenes passed Gate A and W |

---

## Open slots (for human fill)

| Beat | Type | Status |
|------|------|--------|
| B02 | STILL · ai | SLATE — generate using prompt in PROMPTS.md |

Use the prompt in `PROMPTS.md`. After generating, drop file as `cancer-biology/youtube/vox-protein-level-loss/media/B02.png` and rerun `bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-protein-level-loss`.

---

## Residual warnings

- **Motion histogram:** `drawon` carries 53% of beats (7/13) — above the 40% pantry cap. This is inherent to a sequential mechanism film. To reduce: convert B06_StandardCase or B10_AssayBlind to COMPOSITE/annotate motion type, or accept the warning.
- **Gate B:** Pixel layout audit could not execute — `manim` not installed in qc-tooling path. No pixel collision errors found at Gate A/W. Visual review of the MP4 is the pixel truth.

---

## Color law (as built)

TEAL = intact / present / functional (genes, sequencing report)
CRIMSON = lost / absent / broken (protein degraded, absent)
GOLD = single editor's-pen fill in B12 only, never as text
