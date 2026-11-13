# FACTCHECK - Three Things Called Recycling

Status: **GATE F SIGNED - 2026-10-15. 10 rows PASS, 1 premise CORRECTED ON SCREEN,
2 directions NAMED WITH NO FIGURES.**

Topic as commissioned: **"Energy-Recycling Photonic Hardware."**

Primary source for every figure on screen:
Dean, Park, Stokowski, Qi, Robison, Hwang, Herrmann, Fejer, Safavi-Naeini,
*"Low-power integrated optical parametric amplification via second-harmonic
resonance"*, arXiv 2509.26425; published as *Nature* **649**, 1159-1164
(28 January 2026), titled there *"Low-power integrated optical amplification
through second-harmonic resonance"*.

## The premise, checked

| The phrase implies | Verdict | What the reel does |
|---|---|---|
| a single, identifiable research programme | **NOT ONE THING** | Two independent searches returned three unrelated ideas sharing the label: reusing **pump light**, reusing **photons before detection**, and recovering **waste heat**. B01 separates them as the first substantive beat rather than picking one and implying it is the field |

This is the same handling as the HOPE reel, where the commissioned phrase
("Hope training") named something the field does not. Correcting it on screen is
more useful than quietly answering a different question.

## Verified figures used on screen

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B03 | the device is an optical parametric amplifier on thin-film lithium niobate | PASS | abstract |
| 2 | B03 | the pump is generated inside a resonator and recirculates rather than passing once | PASS | abstract - "second-harmonic resonance", pump recirculated |
| 3 | B03, B08 | published in Nature 649, 1159-1164, 28 January 2026 | PASS | journal listing |
| 4 | B04 | gain of more than 17 dB | PASS | abstract |
| 5 | B04 | input power under 200 mW | PASS | abstract |
| 6 | B04 | 95% pump (second-harmonic) conversion efficiency | PASS | abstract |
| 7 | B04 | flat, near-quantum-limited noise across 110 nm | PASS | abstract |
| 8 | B05 | effective pump power rises by nearly an order of magnitude vs conventional single-pass designs | PASS | abstract |
| 9 | B05 | the power needed drops by about an order of magnitude vs previous demonstrations | PASS | abstract |
| 10 | B06 | detection destroys the photon, so light cannot be recycled after measurement | PASS | standard photodetection physics; not a claim from any single paper |

## Deliberately carrying NO figures

**B07 names two further directions and states on screen that no numbers are
claimed for either.** Both are real and both are early:

- **Photon-recycling dielectric laser accelerator** (arXiv 2501.05038, Li,
  Zhang, Zheng, Liu, Pan, Jan 2025). Loops the light remaining after it has
  interacted with an electron beam back for reuse. Its abstract gives **no
  numeric** efficiency, gradient or pass count - only qualitative statements -
  so nothing numeric could be quoted. It is also a **proposal with simulation**,
  not a demonstrated device, and the reel says "a proposal, not a device".
- **Recirculating mesh architectures for photonic neural networks** (arXiv
  2604.18160). Reuses the optical path before detection. No figures were
  verified from a primary source, so none are shown.

Naming them without numbers is the honest option: dropping them would imply the
amplifier is the whole category, and quoting unverified numbers would be worse.

## The noise figure, stated precisely

The abstract reports noise as **"flat, near-quantum-limited" across 110 nm** and
gives **no numeric noise figure in dB**. The reel says exactly that and does not
invent a number. B04's card reads "110 nm of flat, near-quantum-limited noise",
which is the measured quantity (a bandwidth), not a noise value.

## A source that was refused

Stanford's own news page for this work returned HTTP 403 and was never read. A
`sciencedaily` restatement and several aggregator pages were available and were
**not used**, because secondary coverage of this result already disagrees with
itself: one restatement describes the amplification as "about 100 times" and
another gives "a couple hundred milliwatts" without saying what it measures.
"More than 17 dB" is roughly a 50-fold power gain, so "100 times" is a different
quantity or a different operating point. **The reel quotes only the abstract**,
and says "> 17 dB" rather than any fold figure.

This is the third reel in a row where going to the primary source changed a
number that an aggregator had stated confidently.

## Precision notes

- **"~10x" appears twice and means two different comparisons.** B05 keeps both
  baselines on screen - "vs conventional single-pass" and "vs previous
  demonstrations" - because collapsing them into one "10x better" would be the
  exact error the reel is about.
- **The amplifier is not a computer.** B06 states this first among the
  boundaries. Nothing in the reel claims a photonic processor got more
  efficient.
- **"95% conversion" is pump generation efficiency**, not wall-plug efficiency
  and not end-to-end system efficiency. The card says "of the input becomes the
  pump that works".
- **The waste-heat layer is named but not evidenced.** B01 lists it as one of
  the three things the phrase is used for; no heat-recovery figure appears
  anywhere, and B09 tells the viewer that a heat answer means a datacentre
  result, not a computing one.

## Claims deliberately NOT made

- **No claim that photonic computing is close to replacing electronics.**
- **No claim about any company, product or shipping hardware.** The reel names
  no vendor.
- **No claim that tuning-power results are unimportant** - B06 calls them "real
  work, different claim".
- **No efficiency comparison against GPUs or any electronic accelerator.**
- **No fold-gain figure**, for the reason given above.
