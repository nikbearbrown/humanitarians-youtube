# ToDo — Can-AI-discover-new-quantum-materials-9x16

No beat needs media. Every slot is rendered by the composition, so there is no
pantry to fill and no clip to source. What remains is verification and two
optional items.

---

## 1. Verify the ±9.5 K figure — BLOCKS PUBLIC RELEASE (inherited)

- **What:** the out-of-sample RMSE shown at 200 px in Scene 04 (01:00–01:15).
- **Against:** Hamidieh, K. (2018), *Computational Materials Science* 154,
  346–354, §4.
- **Why it blocks:** it is the largest number in the film. Under the film's own
  standard, the most prominent claim cannot be the least verified.
- **Scope:** this is the **same number in both cuts**. Verifying it once
  clears both the 16:9 and the 9:16 masters.
- **If it differs:** edit `MethodScene` in **both** composition files, then
  regenerate beat B05 in the 16:9 project
  (`python runtime/scripts/generate_audio_kokoro.py <16x9 folder> --only B05`),
  update `AUDIO_BEATS` in **both** files to the new measured duration, and
  re-render both cuts.

---

## 2. Optional — give Scene 05 a real campaign

Scene 05 teaches the screening funnel with a labelled illustrative schematic
and no instance. It is the weakest scene in both cuts.

The project brief supplied two 2026 results that would fix this exactly.
Neither came with a citation and neither could be verified, so neither is in
either film. To add one you need:

- **ORNL autonomous discovery loop:** lab, paper title, venue, date, DOI, and
  the specific system the 10–100× acceleration was measured on.
- **The >1.3M-structure screening system:** paper, venue, DOI, the two
  confirmed compound formulas, their measured Tc, and the pressure.

With either in hand the edit is contained: one card in `FunnelScene` in both
compositions, one row in `SOURCES.md`, one row in `FACTCHECK.md`. The
narration does not change — B07 already describes the funnel generically.

---

## 3. Optional — align the Remotion package versions

`@remotion/paths` is on 4.0.490 while the workspace is on 4.0.486, printing a
version-mismatch banner on every render. It does not affect either
composition. This is now the third film in this workspace to carry the note,
so it is worth fixing at the workspace level rather than documenting again.

---

## Not a todo

- **Publishing.** Out of scope for this toolkit and not attempted.
- **Regenerating narration.** This cut deliberately reuses the 16:9 audio. Do
  not generate a second copy here — that is exactly the drift this structure
  avoids.
- **A 1080×1920 variant.** If a smaller vertical file is ever needed, scale the
  4K master down rather than re-rendering; the composition is resolution-
  independent but a downscale is cheaper and guarantees identical framing.
