# PROOF review — the work video's Short, 4K master (2026-09-28)

**File:** `read-the-receipt-backwards-short-final.mp4` · **2160×3840** · 24 fps · **1:28** (88.0s, including the silent
3.5s end card and the 0.3s pauses between beats) · **-15.0 LUFS** / -1.9 dBFS · video = paced (MD5).

**Verdict: clear-for-public.** Trailer gate 12/12; production gate PASS.

## Trailer gate (the Shorts rubric)

| Criterion | Score | Why |
|---|---:|---|
| Hook | 2 | name first, then a well-formed receipt that names someone who never approved it |
| Accuracy / no overclaim | 2 | 11/11 claims on screen when spoken; every result is a live run; the reconstruction is labelled |
| Complete on its own | 2 | one arc: the false receipt → the method → two lines earned live → the seal → the honest open line → the ending; a written join at every cut and the same receipt throughout |
| Honest incompleteness | 2 | the merchant line is "carried, not checked, because Mastercard hasn't published how that check works" |
| Clear CTA | 2 | "The full video reads the whole receipt, and it's linked below"; end card with the handle |
| Brand / technical | 2 | UI zones clean, OFL fonts, no dark frames, cream end card |

## Production gate

| Check | Result |
|---|---|
| GATE V (compile) | 14 frames · 0 / 0 (after the seal fix, below) |
| **Shorts UI zones** (every 0.25s, whole master) | **352 frames · 0 FAIL · 0 LOOK** |
| Dense sweep (every 2%) | 350 frames · the 2 flags are S07's fade-in from cream (designed entrance) |
| Claims on screen at the moment of assertion (Whisper clock, OCR) | **11/11** |
| Dark frames | 0 |
| Continuity at the cuts | the card's geometry is identical across every cut (no zoom jump). What changes is the eyebrow and the highlight moving to the next line on the narration's turn |

## Found and fixed during this build (all on frames or by a gate)

1. Portrait layout: the camera move pushed the full-width card off the frame; lines were ~6pt on a phone;
   three stacked blocks didn't fit the safe band. Fixed with a centred 3% move, ~11pt lines, and one block
   at a time.
2. The bottom stamps reached into the Shorts button column. The card was lifted and `created_at` hidden in
   portrait (text ends by 44.2%).
3. Heading-to-card spacing widened to one consistent gap (Tanmay's note).
4. Terminals: S04's original-build run would have been replaced before its result appeared. It was re-cued
   to finish during the "gate said yes" line; S03 re-cued to type at normal speed.
5. Camera moves ran into the cut (S01, S04). Every move now settles 0.2s before its beat ends.
6. GATE V edge-bleed: the seal hung off the full-width card (S05, S06). Moved inside, then above the card,
   clear of the merchant box.
7. Shorts zones: the raised seal touched the top 12% as it landed and during S06's move. Lowered, with a
   gentler portrait landing (1.2×). 0 FAIL, sampled every 0.1s.
8. compile.py gates: the portrait-plan validation (every beat 916, under 3:00) is stamped by the builder;
   S07's silence is declared intentional.
