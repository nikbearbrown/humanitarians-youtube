# ToDo — can-ai-discover-new-quantum-materials-16x9

No beat needs media. Every slot is rendered by the composition, so there is no
pantry to fill and no clip to source. What remains is verification and one
optional upgrade.

---

## 1. Verify the ±9.5 K figure — BLOCKS PUBLIC RELEASE

- **What:** the out-of-sample RMSE shown at 190 px in Scene 04 (01:00–01:15).
- **Against:** Hamidieh, K. (2018), *Computational Materials Science* 154,
  346–354, §4 — the reported out-of-sample performance table.
- **Why it blocks:** it is the largest number in the film. Under the film's own
  standard, the most prominent claim cannot be the least verified.
- **If it differs:** change the two strings in `MethodScene` inside
  `src/CanAIDiscoverQuantumMaterials.tsx` (the `±9.5 K` value and the caption
  naming the model and split), then re-render. The narration in `B05` says
  "roughly nine and a half kelvin" — if the true figure is materially
  different, regenerate that one beat with
  `python runtime/scripts/generate_audio_kokoro.py <this folder> --only B05`
  and update the measured duration in the composition's `AUDIO_BEATS` table.

---

## 2. Optional — give Scene 05 a real campaign

Scene 05 currently teaches the screening funnel with a labelled illustrative
schematic. It is honest, but it is the film's weakest scene because it asserts
a process without an instance.

The project brief supplied two 2026 results that would fix this exactly. Neither
came with a citation and neither could be verified at build time, so neither is
in the film. To add one:

- **ORNL autonomous discovery loop.** Needed: lab, paper title, venue, date,
  DOI, and the specific system the 10–100x acceleration was measured on.
- **The >1.3M-structure screening system.** Needed: paper, venue, DOI, the two
  confirmed compound formulas, their measured Tc, and the pressure.

With either in hand, the edit is contained: one card in `FunnelScene`, one row
in `SOURCES.md`, one row in `FACTCHECK.md`. The narration does not need to
change — B07 already describes the funnel generically.

---

## 3. Optional — align the Remotion package versions

`@remotion/paths` is on 4.0.490 while the rest of the workspace is on 4.0.486,
which prints a version-mismatch banner on every render. It does not affect this
composition. This is workspace housekeeping, shared with the sibling Mycroft
film.

---

## Not a todo

- **Publishing.** Out of scope for this toolkit and not attempted.
- **A 9x16 cut.** The sibling Mycroft project has one; this film does not. If
  you want it, the pattern to follow is `mycroft-thesisguard-9x16`: a separate
  composition file with a re-laid-out scene set, sharing the same audio.
