# FACTCHECK — vox-fourier-uncertainty

## Claim-by-claim audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | "Heisenberg says you cannot know position and momentum at the same time" | ✓ | M-06 §Bandwidth Relation: "Narrow a Gaussian in position and its transform fattens in exactly reciprocal proportion" | — |
| B01 | "This rule was already in mathematics — long before quantum mechanics" | ✓ | M-06: "delta-x times delta-k >= 1/2 (pure mathematics of transform pairs)" | — |
| B02 | "Fourier transform predicts pinching a wave in space must widen it in frequency" | ✓ | M-06: bandwidth relation is a theorem about transform pairs | — |
| B02 | "Multiply by h-bar and you get Heisenberg" | ✓ | M-06: "Rescaling to momentum via p = hbar*k converts this to delta-x*delta-p >= hbar/2" | — |
| B03 | "Squeeze the packet into a narrow spike in space and you need many different frequencies" | ✓ | M-06: narrow x requires wide k distribution by bandwidth bound | — |
| B04 | "The wider you spread the packet in space, the fewer frequencies it needs" | ✓ | M-06: wide x-space Gaussian pairs with narrow p-space Gaussian | — |
| B05 | "A narrow Gaussian in x transforms to a wide Gaussian in k" | ✓ | M-06 §Gaussian: "f(x) = e^{-x^2/2a^2} transforms to another Gaussian...with width 1/a" | — |
| B05 | "They breathe in reciprocal proportion" | ✓ | M-06: width in k is 1/a when width in x is a | — |
| B06 | "delta-x times delta-k is at least one half" | ✓ | M-06: "delta-x times delta-k >= 1/2" (boxed in chapter) | — |
| B06 | "The Gaussian saturates this bound exactly" | ✓ | M-06: "The Gaussian is the unique shape that saturates the bandwidth bound: delta-x*delta-k = 1/2 exactly" | — |
| B07 | "In quantum mechanics, momentum is h-bar times wavenumber" | ✓ | M-06: "p = hbar*k" is de Broglie relation, standard | — |
| B07 | "That single substitution converts the math theorem into Heisenberg's inequality" | ✓ | M-06: "Fourier route: delta-x*delta-k >= 1/2 (pure mathematics) → delta-x*delta-p >= hbar/2" | — |
| B08 | "Uncertainty principle applies to sound, light, and radar — any wave system" | ✓ | M-06: bandwidth relation is a mathematical fact applying to all waves | — |
| B09 | "Gaussian packet with position width 0.5 nanometers" | illustrative | Illustrative example per instructions | Labeled illustrative |
| B09 | "Momentum spread of at least h-bar over one nanometer" | illustrative | hbar/(2*0.5e-9) is one form; illustrative order-of-magnitude | Labeled illustrative |
| B09 | "Halve the width — momentum spread doubles" | ✓ | M-06: reciprocal scaling of Gaussian widths | Consistent with bandwidth bound |

## Terms table

| Term | Debut beat | Prior beat creating the need |
|------|-----------|------------------------------|
| wave packet | B03 | B01-B02 establish the concept of position localization |
| Fourier transform | B05 | B03-B04 establish that frequency content matters |
| bandwidth bound | B06 | B05 shows the paired Gaussians; now needs a name |
| wavenumber | B07 | B05-B06 use k; now the name is given |

## Illustrative numbers
- B09: position width 0.5 nm, momentum spread ~hbar/1nm — order-of-magnitude consistent with bandwidth bound; labeled illustrative in narration.

## Exclusions confirmed
- No Robertson/commutator derivation — confirmed absent.
- Only Fourier bandwidth route used — confirmed.
