# FACTCHECK — vox-why-hot-ones-are-jerks (Gate F)

Source of record: *Calling Bullshit* (Bergstrom & West), ch. 6 ("Selection
bias"), via `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md`;
the dating construction originates in Jordan Ellenberg, *How Not to Be Wrong*
(2014). Audio was converted from the doodle build — narration text identical,
checked as spoken. Regenerate if any narration or viz data changes.

| beat | claim | verdict | source / derivation | fix |
|---|---|---|---|---|
| A01 | "Everyone you date seems to prove it: the more attractive, the meaner." | editorial (labeled) | The folk observation the film interrogates — framing, not a finding. The film's job is to show it can be an artifact. | — |
| A05–A06 | Niceness and attractiveness are uncorrelated in the population; the flat trend line. | ✓ as ILLUSTRATIVE PREMISE | This is Ellenberg's construction, adopted by Calling Bullshit ch. 6: assume zero correlation, then show selection alone creates one. The film draws a synthetic seeded cloud (SEED 42) — the flatness is BY CONSTRUCTION and must be presented as the setup, never as an empirical survey result. Narration says the line "says" they're unrelated — consistent with a drawn premise. | — |
| A08–A09 | "You skip anyone who is neither cute nor kind" removes the lower corner. | ✓ (mechanism) | The Ellenberg/CB dating filter: you don't date people below your joint bar. Geometrically removes the low-sum corner of the cloud. | — |
| A10–A11 | The people who are both gorgeous and kind skip you; top corner disappears. | ✓ (mechanism) | The second cut in the book's construction ("who'll date you"), removing the high-sum corner. | — |
| A12–A14 | What survives is a diagonal band; a trend line through survivors tilts downward. | ✓ (verified computationally) | With s = u+v and cuts at 0.55 / 1.45 on uniform UV (seed 42): survivors n = 85, correlation **r = −0.423** (computed 2026-07-06 from the exact scene constants). Berkson's mechanism: conditioning on a sum-threshold induces negative dependence. Full population r ≈ 0 by construction. | verify tilt visually at Gate B |
| A15 | "In your dating pool, hotter now really does mean meaner." | ✓ (conditional claim) | True WITHIN the selected sample only — the chip on the plane says "in YOUR pool," which carries the conditionality on screen. | chip required |
| A16 | "Nobody's personality changed — your filters built that slope." | ✓ | By construction: the underlying cloud is untouched; only membership changed. | — |
| A17 | "Statisticians call this trick Berkson's paradox." | ✓ | Joseph Berkson, "Limitations of the Application of Fourfold Table Analysis to Hospital Data," *Biometrics Bulletin* 2(3), 1946 — the canonical source; "Berkson's paradox/bias" is the standard name. | — |
| A18–A19 | Google studied contest coders; among hires, contest success predicted worse job performance. | ✓ per source book | Calling Bullshit ch. 6 reports Google's internal people-analytics finding (associated with Peter Norvig's public remarks) of a negative correlation between programming-contest success and on-the-job performance. The A18 quote card PARAPHRASES with attribution — no invented verbatim quote. | card text = paraphrase + attribution |
| A20 | "The hiring bar had already thrown away everyone who was weak at both." | ✓ (book's explanation) | The book's resolution: hiring selection (a joint threshold) manufactures the negative correlation among hires — same geometry as the dating cuts. Norvig's own alternative conjecture existed; the book argues selection. Film presents the selection mechanism, which is the chapter's claim. | — |
| A21 | "Any time a gate picks winners, the survivors show patterns the world never had." | ✓ (generalization) | Standard statement of collider/selection bias scope (Berkson 1946 generalized; CB ch. 6's closing argument). "Never had" = did not exist in the unselected population, which is exactly what the construction shows. | — |
| A22 | "Ask who got filtered out." | editorial (the book's advice) | CB ch. 6's takeaway, phrased as the closer card. | — |

## Simplifications, defended

1. **Synthetic uniform cloud + sum-threshold cuts** stand in for real dating
   dynamics — this is the book's own pedagogical construction; the film never
   claims survey data.
2. **"Berkson's paradox" naming beat omits the 1946 hospital-data origin** —
   one film, one construction; the citation lives here and in the description.
3. **Google beat compresses** an internal analytics finding + public remarks
   into "Google once studied" — per the book's own compression; attribution on
   the card and in the description.

## Standing obligations before ship

- Gate B eyeball: surviving-band trend visibly negative; highlighter band
  matches the cut geometry.
- A01 still is `ai` — disclosure sidecar required (`A01.source.txt`).
- Description credits: Bergstrom & West ch. 6; Ellenberg construction;
  Berkson 1946.
