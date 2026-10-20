# Sources & Fact-Check — ab-testing-can-lie-to-you

**Checked:** 2026-10-18, against the primary texts themselves — the authors' own PDFs, saved in
`sources/` — not secondary summaries or memory. Every simulated number traces to the saved output
of a script in `py/` that was actually run (Python 3.13.1, standard library only, fixed seeds).

## Citations

| | Citation | How verified |
|---|---|---|
| **[1]** | Fabijan A, Gupchup J, Gupta S, Omhover J, Qin W, Vermeer L, Dmitriev P. Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners. *Proc. 25th ACM SIGKDD (KDD '19)*, Anchorage, Aug 4–8 2019. doi:[10.1145/3292500.3330722](https://doi.org/10.1145/3292500.3330722) | Authors' version, `sources/fabijan-2019-kdd-srm.pdf` (from exp-platform.com, Microsoft's experimentation team site). Title, author list, affiliations, venue and DOI read from page 1 |
| **[2]** | Johari R, Pekelis L, Walsh DJ. Always Valid Inference: Bringing Sequential Analysis to A/B Testing. arXiv:1512.04922v1, Dec 2015. | `sources/johari-pekelis-walsh-arxiv-1512.04922v1.pdf`. Claims below are read from this version only |
| [2′] | Published as: Johari R, Koomen P, Pekelis L, Walsh D. Always Valid Inference: Continuous Monitoring of A/B Tests. *Operations Research* 2022;**70**(3):1806–1821. doi:10.1287/opre.2021.2135 | Bibliographic record only (RePEc). **Not read.** The reel cites [2], the version I read |

**Affiliations (from the papers):** [1] authors: Fabijan, Gupchup, Gupta, Omhover, Qin at Microsoft;
Vermeer at Booking.com; Dmitriev at Outreach.io. So "a paper **led by** Microsoft researchers" holds,
but "Microsoft's paper" would not. [2]: Johari at Stanford (advisor to Optimizely); Pekelis and
Walsh at Optimizely when the work was done. So "Researchers at Stanford and Optimizely" holds.

**LibKey:** the org's LibKey connector is not signed in to this session, so access links haven't
been resolved through it. Run `/mcp` → "Scholarly Full Text Article Access with LibKey" and I'll
resolve both DOIs and add the links here. The facts above don't depend on it.

## What [1] says about the carousel (verbatim, §1 and §5.3)

- §1: "A product team at MSN increased the number of rotating cards on the carousel from 12 to 16."
  "…this experiment revealed a significant decrease in engagement with the cards. Users seeing more
  cards appeared to click less. Based on this result it seemed like a bad idea to ship this change."
- §1 (p. 2): "the treatment group which was exposed to the new 16 card carousel had fewer users in
  the analysis compared to what was configured… After resolving the issue that was causing the SRM…
  it was found that the change was in fact positive and significantly increased the engagement."
- §5.3: "the most engaged users in the treatment group were being classified as computer bots and
  removed from the experiment analysis by an algorithm that scans for bot activity… After
  accounting for the bot classification results, the results were flipped and the correct decision
  to ship the feature was made."
- §4.1: "approximately 6% of experiments at Microsoft exhibit an SRM" (experiments "conducted within
  the last year", i.e. the year before the 2019 paper).
- §2.3.1: "a ratio of 50.2/49.8 (821,588 versus 815,482 users) … the probability that it happened by
  chance is less than 1 in 500k." Recomputed: χ² = 22.77, p = 1.82×10⁻⁶ (1 in 549,000). CONFIRMED.

**What [1] does NOT give:** no per-group user counts, click counts, effect sizes or p-values for
the carousel; no description of *how* the bot classification was corrected; no SRM p-value
threshold. So the reel shows **no** carousel numbers. The code beats simulate the mechanism and are
labeled as a simulation, and the narration never quotes a threshold.

## The simulations (`py/`)

| Script | Output (`py/*.out`, verbatim) | Beat |
|---|---|---|
| `carousel_v1.py` | `control 3.89` · `test 3.20` · `z -40.4   p < 1e-9` | B03, B04 |
| `carousel_v2.py` | `split 200000 vs 196997` · `SRM p 2e-06` · `control 3.89` · `test 4.65` · `z 24.5   p < 1e-9` | B06, B07 |
| `peeking.py` | `peeking 24.6%` · `once 3.8%` · `by day 35 74 102 … 246` | B08 |

Model (both carousel scripts, identical seed 2019): 200,000 users per group. 1.5% are "fans" with
60 clicks before the test; the treatment gives fans +40 (so 100) and 20% of everyone else +1. Bot
rule: more than 80 clicks gets you dropped. In v1 the rule reads clicks *during* the test, so every
treated fan is dropped and no control user is. In v2 it reads clicks from *before* the test, which
the treatment can't change. `p < 1e-9` is printed because the true p underflows to 0.0 in floating
point (`fmt_p` in `abtest.py`).

Peeking model (seed 2015): 1,000 A/A tests, both groups converting at 10%, 500 users per group per
day, 20 days. A two-proportion z-test runs after every day. "Peeking" counts a test as a winner if
any day hits p < 0.05; "once" tests only day 20.

## Claim-by-claim trace

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B01 | a product team at MSN, carousel 12 → 16 rotating cards | [1] §1 | CONFIRMED (verbatim) |
| 2 | B01 | expected more clicks | [1] §1: "expectation… increase in the number of times that users click" | CONFIRMED |
| 3 | B01 | the test showed a statistically significant drop | [1] §1 "significant decrease in engagement" | CONFIRMED |
| 4 | B01 | "On that result, you don't ship." | [1] §1 "it seemed like a bad idea to ship" | CONFIRMED (paraphrase) |
| 5 | B01 | a 2019 paper led by Microsoft researchers | [1] p. 1 | CONFIRMED. See affiliations |
| 6 | B02 | "We can't see MSN's data" | [1] gives no carousel data | CONFIRMED. Sets up the simulation honestly |
| 7 | B03 | 0–6 clicks, 1.5% fans, +40, bots = over 80 | `carousel_v1.py` | CONFIRMED (code) |
| 8 | B03 | "the standard cleanup" (bot filtering) | [1] §5.3, an algorithm that scans for bot activity during data processing | CONFIRMED that bot filtering is routine. The 80-click rule is the sim's |
| 9 | B04 | 3.89 vs 3.20, z −40 | `carousel_v1.out` | CONFIRMED (−40.4) |
| 10 | B06 | chi-square on group sizes vs 50/50 | [1] §2.3.1 "a chi-square test can be used"; `abtest.srm_check` | CONFIRMED |
| 11 | B06 | fix = judge bots on pre-test clicks | `carousel_v2.py`; [1] §5.3: bot removal "based on post-treatment observations can lead to SRM" | CONFIRMED **as our fix in the sim**. Not presented as MSN's fix. See Flag B |
| 12 | B07 | about 3,000 users short | 200,000 − 196,997 = 3,003 | CONFIRMED |
| 13 | B07 | odds by chance about two in a million | χ² = 22.72, p = 1.88×10⁻⁶ | CONFIRMED. See Flag C |
| 14 | B07 | after the fix, 3.89 vs 4.65; the loss was a win | `carousel_v2.out` | CONFIRMED (in the sim; matches the direction [1] reports) |
| 15 | B08 | 1,000 A/A tests, daily for 20 days | `peeking.py` | CONFIRMED (code) |
| 16 | B08 | stopping at the first significant day, a quarter crown a winner | `peeking.out`: 24.6% | CONFIRMED |
| 17 | B08 | looking once: under 5% | `peeking.out`: 3.8% | CONFIRMED. Sampling noise around the nominal 5% (1,000 tests ⇒ ±1.4 pts) |
| 18 | B08 | nonstop checking can push it past 30% | [2] App. C: Type I error "higher than 30% even for the post-hoc power approach… with 10,000 observations"; §2: "Type I error can be inflated by over 30%" | CONFIRMED for continuous monitoring at 10,000 observations. See Flag D |
| 19 | B09 | the bot filter dropped the most engaged users in the 16-card group | [1] §5.3 | CONFIRMED |
| 20 | B09 | once fixed, the result flipped and the feature shipped | [1] §5.3 "results were flipped and the correct decision to ship the feature was made" | CONFIRMED |
| 21 | B09 | about 6% of Microsoft's experiments show this mismatch | [1] §4.1 | CONFIRMED. "This mismatch" = an SRM of any cause, not specifically bot SRMs (wording is accurate) |
| 22 | B09 | if you must peek, use a test built for it | [2]: always-valid p-values / sequential tests for continuous monitoring | CONFIRMED |
| 23 | B09 | fix your sample size in advance | [2] §1: standard p-values assume the experimenter "will not continuously monitor their test… there should be no repeated 'peeking'" | CONFIRMED |
| 24 | B10 | handoff prompt | — | Instruction, not a claim |

## Flags (decided by Supriya 2026-10-18: A, B, D no change; C option (ii) applied)

**A — B01 "On that result, you don't ship."** Accurate paraphrase of [1] ("seemed like a bad idea to
ship"). No change suggested. Listed only because it's the one line that states a decision.

**B — B06 fix vs MSN's fix.** [1] doesn't say how MSN corrected the bot classification, only that
they "accounted for" it. The narration attributes the pre-test-clicks fix to *our simulation*
("And the fix: judge bots by their clicks from before the test"), and B09 stays generic ("Once that
was fixed"). No change suggested. Please confirm you're comfortable with that framing.

**C — the coincidence in B07.** The sim's SRM (50.4/49.6, p = 1.88×10⁻⁶) lands almost exactly on the
odds of [1]'s own textbook example (50.2/49.8, p = 1.82×10⁻⁶). This happened by accident, not by
tuning. Two options: (i) leave it, since nothing on screen claims the numbers are the paper's; or
(ii) add an on-screen source line in B07, "Fabijan et al.'s own example: 821,588 vs 815,482, < 1 in
500k". That shows real-world SRMs are this subtle, and adds no narration. I lean (ii).

**D — B08 "past thirty."** [2]'s 30%+ is for checking after **every observation** up to 10,000. The
sim's 24.6% is for 20 daily looks. The narration keeps them separate ("nonstop checking"), which is
accurate. No change suggested.

## Dating check (DOUBLE-CHECK LAW)

No model names or version numbers. The composer's model chip reads plain "Claude". "Twenty nineteen"
is the paper's date, not the video's. The "about 6%" figure is dated by the paper itself
(experiments in the year before 2019). The narration says "the paper says", so it doesn't present
the figure as current.

## No paid services

Python stdlib, Kokoro (`af_bella`, local), Manim, Remotion. No keys anywhere.
