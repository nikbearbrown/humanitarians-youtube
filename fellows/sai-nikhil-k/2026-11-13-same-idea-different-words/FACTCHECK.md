# FACTCHECK — Same Idea, Different Words

| # | Claim | On screen | How verified | Result |
|---|---|---|---|---|
| 1 | Mollick calls Fable 5.2 "almost AGI", jagged | B00, B04 line 1 | the post (9 Nov 2026): "almost" AGI, "Jagged AGI" | ✔ |
| 2 | "as good as most experts at most computer work" | B00 narration | paraphrase of his working definition, "an AI as good as most human experts at most intellectual tasks you can do with a computer" | ✔ paraphrase |
| 3 | 471 worlds | B00, B01, B03, B04 | `overlap.out`: 471 entries in `src/worlds/index.js` @ 210133f; README says 471 | ✔ |
| 4 | Three are one idea: reindeer rings, manta column, storks circling | B01 | the three entries + their descriptions in `overlap.out`; Mollick names the same three | ✔ |
| 5 | "By his account, no agent noticed" | B01 narration | post: "the AI did not notice these problems itself"; "None of them asked whether the work was too long, too repetitive, or no fun" | ✔ attributed |
| 6 | cos θ = a·b / (‖a‖‖b‖) | B02 row 1 | definition; scikit-learn `cosine_similarity` | ✔ |
| 7 | No shared word ⇒ a·b = 0 ⇒ cos 0 | B02 row 2, note | TF-IDF vectors are non-negative, so a·b = Σ aᵢbᵢ is 0 iff no term is in both; `overlap.out` a·b = 0.000000 for all three pairs | ✔ |
| 8 | 45.5% of pairs share a word | B03, B04 | 50,315 of 110,685 = 45.46% | ✔ |
| 9 | Cyclone pairs 0% | B03, B04, B00 | 0 of 3 | ✔ |
| 10 | Captions differ: two say "cyclone" | B03 note | `overlap.out` last line, cosine 0.167 | ✔ |

## Algebra

- Pairs: 471 × 470 / 2 = 110,685. 50,315 / 110,685 = 0.45458 → 45.5%.
- TF-IDF weights are ≥ 0 and each description vector is L2-normalised
  (‖a‖ = ‖b‖ = 1 in `overlap.out`), so cos θ = a·b. With no shared term every
  product aᵢbᵢ has a zero factor, so a·b = 0 and cos θ = 0.
- `build_beats.py --check` asserts 110,685 = 471·470/2, the 45.5% rounding, 0 of
  3, and the three dot products = 0.

## Rendered-frame math review (2026-11-16, by eye)

B02 at 15 / 50 / 85 % in 16:9, and the portrait master at 0:31:

- Row 1 (cos θ) up from 15 %; row 2 lands by 50 % on "If two descriptions".
  Reveal times are authored in comp time (the 15 s comp is retimed 1.57× into
  the 9.6 s beat).
- Bold vectors a, b, the dot, the double bars ‖·‖, the Σ with its i, ⇒ and θ all
  render (no tofu, no clipping). Portrait rows stack at a smaller scale and stay
  legible; note and conditions clear of row 2.
- B03 table: all three rows visible by 85 % in both aspects; 45.5 prints as 45.5.
- B01 plate: GATE V flagged the first cut (three-across layout, 24 % fill at
  50 %, when only the reindeer is up). Re-laid out as hero + 2; a two-line
  credit then touched the stork panel, so the on-screen credit was cut to one
  line. Final gate 0 / 0 in both aspects.
