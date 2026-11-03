# FACTCHECK — claim-by-claim audit

Every factual, numerical, and clinical claim in `beat_sheet.json`, checked against the
strongest source available. Written **before** rendering per PLAYBOOK §1, not after.

**Why this exists even though no gate demands it.** GATE F stopped firing once the phantom
Manim scene was removed (`$PENDING` went empty, so the paperwork gate is skipped by
construction). It is bypassed, not satisfied. This film also *criticises* a draft for
citations that don't check out, so under PROOF's grade-the-graders rule it is held to its
own standard first — a single voiced-but-unsourced claim would make it self-refuting.

Verdicts: **SUPPORTED** · **QUALIFY** (true with a stated bound) · **UNSUPPORTED** ·
**CUT** (removed rather than shipped).

---

## 1. The two preprints

| Beat | Claim | Verdict | Evidence |
|---|---|---|---|
| B06 | Baseline 71.6%, minimal persona 68.0%, long persona 66.3% on MMLU | **SUPPORTED** | [arXiv 2603.18507](https://arxiv.org/html/2603.18507v1) Figure 1b, read from the paper's own HTML |
| B06 | "Longer persona prompts damage more" | **SUPPORTED** | Verbatim from the same paper |
| B06 | It is a preprint, not peer reviewed | **SUPPORTED** | arXiv, March 2026, no venue listed |
| B07 | Expertise depth 3.638 → 3.923 | **SUPPORTED** | [arXiv 2605.29420](https://arxiv.org/html/2605.29420) |
| B07 | Clarity 4.896 → 4.550 | **SUPPORTED** | Same |
| B07 | Helps on advisory questions, medicine and psychology | **SUPPORTED** | Quoted in the paper |
| B07 | Plain prompting wins on conceptual/explanatory in finance, legal, science, technology | **SUPPORTED** | Quoted in the paper |
| B07 | Synthetic benchmark, limited models, LLM-judged | **SUPPORTED** | The authors' own stated limitations |
| B08 | Neither paper separates expertise-claim from task-context | **QUALIFY** | An **absence** observed while reading, not a stated claim. B08 was rewritten from "the second paper says it outright" to "never separates them" (PROOF finding M2). The narration must not attribute the observation to the authors. |

### ⚠️ One claim carried a near-miss worth recording

The MMLU figures were **initially sourced only to secondary coverage** because the PRISM
PDF returned unrenderable content. They sat as `[VERIFY: MMLU numbers]` and were explicitly
barred from screen. They were later read from the paper's HTML and promoted to SUPPORTED.

Had the review been skipped, a film about citation accuracy would have put second-hand
numbers on screen. The length-monotonicity claim in particular is load-bearing.

### CUT — the paper's stated mechanism

The extracted explanation for *why* longer prompts hurt was internally inconsistent (it read
as longer prompts interfering *less* while shorter variants are preferable). **Verdict: CUT.**
The numbers and the quoted sentence ship; the causal explanation is never narrated.

---

## 2. The clinical claim — and the reversal

| Beat | Claim | Verdict | Evidence |
|---|---|---|---|
| B04 | Statement quoted from the source draft | **SUPPORTED** | `beat_sheet.SOURCE-DRAFT.json` B02, retained in-folder |
| B04 | "Verifying orders against Beers Criteria is the pharmacist's expertise" | **UNSUPPORTED — and the film says so** | See below |
| B04B | AGS 2023 Beers Criteria written by a 12-member panel spanning medicine, nursing, and pharmacy | **SUPPORTED** | [PubMed 37139824](https://pubmed.ncbi.nlm.nih.gov/37139824/) |
| B04B | Published by the Hartford Institute for Geriatric Nursing, in a series for nurses | **SUPPORTED** | [HIGN ConsultGeri](https://hign.org/consultgeri/try-this-series/american-geriatrics-society-ags-2023-updated-ags-beers-criteria-r) |
| B04B | Described as assisting "nurses and interprofessional team members in medication reviews" | **SUPPORTED** | HIGN, quoted |
| B04B | "Clearing the order in the pharmacy system before it can be dispensed" excludes the nurse | **QUALIFY** | Deliberately phrased as a **workflow** step, not a licensure claim. It asserts who performs a step in a described workflow, not what any profession is legally permitted to do. **Must not drift into scope-of-practice language.** |

### The most important entry in this file

The B04 claim is **false**, and the film's structure depends on that. B04 states it
confidently; B04B checks it against AGS and HIGN and retracts it on screen. The retraction
is the beat, not a patch.

**How it nearly shipped as fact:** Sonnet 5 asserted the pharmacist-licensure framing in our
own experiment trial data — *"a pharmacological clinical-review task requiring pharmacist
licensure, not a nursing scope-of-practice function"* — I found it plausible, and I drafted
it as fact. **A model agreeing with me is not a source.** That is the single most important
lesson in this audit, and it is the same failure mode the film is about.

---

## 3. Our own measurement

All from `experiment/results-20260818T04*.json`, 480 calls, 0 errors, $0.7640.

| Beat | Claim | Verdict |
|---|---|---|
| B10 | 24 statements, 2 models, 5 repeats, 480 calls | **SUPPORTED** |
| B10 | Mean 2.25 (Haiku) / 2.46 (Sonnet 5) distinct neighbours per statement | **SUPPORTED** |
| B10 | 79% / 71% of statements got more than one neighbour | **SUPPORTED** |
| B10 | Same-title degenerate neighbour 15% / 9% | **SUPPORTED** |
| B10B | Verdict flips: free 42% / 17% → pinned 17% / 8% | **SUPPORTED** |
| B10B | Cross-model agreement 67% → 88% | **SUPPORTED** — computed from 33% and 12% disagreement |
| B10B | "This does not show models are bad at this" | **SUPPORTED** — the stated bound |

### CUT — the correctness rates

The `full` / `swapped` / `stripped` PASS rates are **excluded from the film entirely.**
Revision 2 established that three of six `full` statements did not exclude their designated
neighbour and the models were right to fail them, so those cells measure the author's
item-writing rather than model capability. **Verdict: CUT.** They appear in `EXPERIMENT.md`
labelled not-for-screen, and nowhere in the beat sheet.

The one borderline observation — Sonnet 5 passing the length-matched `swapped` control at
47% versus `full` at 50% — is logged as supporting-only in `EXPERIMENT.md` and **is not
narrated**, because `full`'s baseline is contaminated.

---

## 4. Claims CUT before they reached the beat sheet

| Claim | Why |
|---|---|
| "A hundred points — eighty on the rubric, twenty on relative quartile" | No source. Absent from the course repo and every reachable document. |
| "The rubric has six deliverables" | Same |
| "Twenty-one points: the domain-adapted prompt" | Same — and doesn't reconcile: 21+16+11 = 48 of a claimed 80, with bs-01 and bs-03 both claiming the same 21-point component |
| "This component is sixteen points" (bs-02) | Same |
| "One pass of this test is worth ten minutes of re-reading" | Invented quantity in the source draft; no basis |
| "the Loop — predict, decide, verify" | Not locatable in the Botspeak page or the course outline |
| "the Nine **Capacities**" | Contradicted by the primary text's own title: *Botspeak: The Nine **Pillars** of AI Fluency* |
| "the five Specification components, Chapter 3" | Not locatable in any reachable primary source |
| "chapters zero through thirteen" | Course runs Modules 1–15 |
| "A team at USC" | Affiliation never verified; institution added risk without value |

**Every one of these is in the source draft. None survives into this film.** Verified
against the [course repo](https://github.com/nikbearbrown/INFO-7375-Computational-Skepticism-and-AI)
and [humanitarians.ai/botspeak](https://www.humanitarians.ai/botspeak). Full reasoning in
`GAP-ANALYSIS.md`.

---

## 5. Calibration check — does confidence match evidence?

| Beat | Original phrasing | Fixed to |
|---|---|---|
| B02 | "Open **any** prompt-engineering exercise" | "Open **most**" — removed an unfalsifiable universal |
| B06 | "**measurably costs you accuracy**" | "cost accuracy **on that benchmark**" — one preprint, one benchmark |
| B08 | "the second paper **says it outright**" | "**never separates them**" — an absence observed, not a claim made |
| B11 | "Tighten it because length has a measured cost — 66.3 against 71.6" | **Removed.** Those figures were measured on expertise-claim personas; importing them to justify tightening a *task-context* statement is the exact conflation this film exposes. B11 now names the temptation and refuses it aloud. |

**B11 was the critical finding.** Left as drafted, the film would have contradicted its own
thesis in its resolution. The 71.6 / 66.3 figures now appear **only in B06**, verified by a
programmatic check over the beat sheet.

---

## Outstanding before the film can be called done

1. **`[VERIFY: scope-of-practice drift]`** — B04B's replacement phrase must stay a workflow
   description. Re-read the rendered caption; if it reads as a licensure claim, soften.
2. **Production gate / `/show`** — not yet assessable; no frames existed when this was
   written. Sources must be legible *at the moment of assertion*, not merely present.
3. **Narration gate** — unsigned. Current audio is previz-grade for measurement.
4. **`silencedetect` sweep** — B02's category list and B04B's "She could write that phrase.
   She probably has." use deliberate hard stops that can read as dropped words.

## Summary

| Verdict | Count |
|---|---:|
| SUPPORTED | 18 |
| QUALIFY (bound stated on screen) | 3 |
| UNSUPPORTED (retracted *within* the film, by design) | 1 |
| CUT before reaching the beat sheet | 12 |

No claim ships without a visible source. No number from the source draft's rubric survives.
The one false claim in the film is false on purpose, corrected on screen, against a real
source — which is the film's argument rather than an exception to it.
