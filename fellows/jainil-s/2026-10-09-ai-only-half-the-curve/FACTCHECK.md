# FACTCHECK — You're Only Seeing Half the Curve

Every claim the reel makes, with its verdict and its source. Claims sourced to
`double_descent_evidence.py` are reproducible by running that file; it ships in
this folder and prints every figure below.

| # | Beat | Claim as made | Verdict | Source |
|---|---|---|---|---|
| 1 | B02 | With 100 training examples fixed, adding parameters first lowers test error, then raises it | **VERIFIED** | `double_descent_evidence.py` — 1.039 at p=2 → 0.700 at p=60 → 1.728 at p=90, median of 12 seeds |
| 2 | B02 | The best model on the classical side uses 60 parameters | **VERIFIED** | ibid. Minimum of the p<100 region, 0.700 |
| 3 | B03 | At p = 100 the test error is 111 | **VERIFIED** | ibid. 111.263, median of 12 seeds |
| 4 | B03 | That is 159× worse than the classical best | **VERIFIED** | 111.263 / 0.700 = 158.9, rounded to 159 |
| 5 | B03 | Past the peak the error falls below the classical best — 0.29 against 0.70 | **VERIFIED** | ibid. 0.293 at p=4000 vs 0.700 at p=60 |
| 6 | B03 | The spike sits at parameters = training examples | **VERIFIED** | ibid. The peak is at p=100 and n=100 by construction; this is the interpolation threshold |
| 7 | B04 | At exactly p = n there is precisely one parameter setting that fits all n points | **VERIFIED (conditional)** | Linear algebra: a square feature matrix of full rank gives a unique exact solution. Full rank holds generically for random features and held in all 12 seeds |
| 8 | B04 | Past the threshold many different settings fit the data exactly | **VERIFIED** | Standard: for p > n the exact-fit system is underdetermined, so the solution set is an affine subspace of dimension ≥ p−n |
| 9 | B04 | Least squares takes the smallest one | **VERIFIED** | `np.linalg.pinv` returns the minimum-L2-norm least-squares solution. This is also what gradient descent from zero initialisation converges to |
| 10 | B04 | "…the smallest one, which is the smoothest one" | **INTERPRETATION — flagged** | The minimum-norm property is a theorem; "smoothest" is the reading of it for random Fourier features, where coefficient norm governs how much high-frequency content the fit carries. True for this construction, stated as mechanism rather than proved. See `SOURCES.md` omission 4 |
| 11 | B04 | Every candidate curve drawn on screen passes through every data point | **VERIFIED** | By construction in `InterpolatorChoice.tsx`: each candidate is the base curve plus `A·sin(π(n−1)qt)`, which is exactly zero at every `t = i/(n−1)` for integer `q`. The dots cannot move |
| 12 | B05 | Training error reaches zero at p = 100 and stays there | **VERIFIED** | `double_descent_evidence.py` — 9.5e-27 at p=100, and 0.00000 to five decimals for every larger p |
| 13 | B05 | The test curve swings through a factor of nearly 400 past the threshold | **VERIFIED** | 111.263 / 0.293 = 380 |
| 14 | B06 | Belkin et al. quotation, shown on the card | **VERIFIED VERBATIM** | PNAS 116(32):15849–15854, 2019, abstract. Checked against the PMC record, PMCID PMC6689936 |
| 15 | B06 | Published in the Proceedings of the National Academy of Sciences, 2019 | **VERIFIED** | ibid. Published 24 July 2019 |
| 16 | B06 | The same experiment family — the paper used these models too | **VERIFIED** | Belkin et al. ran random Fourier features (on an MNIST subset), alongside random forests and 2-layer networks |
| 17 | B06 | Nakkiran et al. showed the shape along training time, not just model size | **VERIFIED** | arXiv:1912.02292 abstract, verbatim: *"double descent occurs not just as a function of model size, but also as a function of the number of training epochs"* |
| 18 | B07 | A parameters-to-examples ratio near 1 is the worst region of the curve | **VERIFIED for this experiment** | ibid. The maximum of the test curve is at exactly that ratio. Stated conditionally in the narration ("if that ratio was anywhere near one"), not as a universal |

## Note on the B06 quotation

Two typographic normalisations were made to the card, and neither changes a
word:

- the original places quotation marks around **"double-descent"** inside the
  sentence; these were dropped to avoid nested quotes inside the card's own
  quotation marks
- the original's en-dash in **bias–variance** renders as a hyphen in the card

Wording, order and punctuation are otherwise exactly as published. The
narration attributes the sentence aloud before it is read.

## Claims considered and cut

| Claim | Why it was cut |
|---|---|
| "Bigger models always generalise better" | False, and the opposite of the reel's point. The peak is real and sitting near it is genuinely bad |
| Any numeric double-descent figure for deep networks | Our numbers describe a linear model with random features. In a deep network the peak tracks effective model complexity, not a parameter count. Transferring the numbers would repeat the exact mistake the reel is about |
| "So regularisation is unnecessary" | Not tested here, and probably false. This experiment is deliberately ridgeless. Tuned ridge can flatten the peak substantially |
| "You should always train past the interpolation threshold" | Not supported. Getting a benefit needs to go *well* past it; stopping just past is worse than stopping well before |

## Changed during the build

**B00's composer output line.** First written as *"You stopped near the worst
point on the curve."* — which asserts the viewer stopped near the interpolation
threshold, and nothing in their question establishes that. Replaced with
*"Depends where you stopped."* before the first render. The hook should not
make a claim the reel then has to qualify.

**B01's corrected sentence was ungrammatical on the first render.** The beat
swaps one word to correct the viewer's misconception. Written as
`"The error curve has one dip."` with `one`→`two`, it rendered as *"has two
dip."* — the swap repaired the number and left the noun singular, which is the
exact defect the skill law names ("correct the SENTENCE, not just the word").
The law's own remedy is a multi-word trigger, which **cannot work** — see
`bugs-and-fixes/authoring-gotchas.md` A11. Rewritten as
`"The error curve dips once."` with `once`→`twice`, which is grammatical under
a single-word swap and is also a better line, since "dips twice" is what
"double descent" literally means. Caught by reading a frame; no gate checks
whether a sentence makes sense.

**The experiment itself was rebuilt twice before the narration was written.**
The first configuration produced a spike but no genuine second descent below the
classical optimum — the right-hand side re-ascended toward the null model. A
second configuration produced a clean classical U but still no winning second
descent. Only the third, after a sweep over feature bandwidth and label noise,
showed the full textbook shape, and it was then checked across 12 seeds before a
single line of narration existed. Had the script been written after the script,
the reel would have claimed a shape its own evidence did not show.
