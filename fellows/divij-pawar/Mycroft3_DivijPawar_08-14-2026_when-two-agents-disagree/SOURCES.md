# SOURCES.md — when-two-agents-disagree (Video 1 of 2)

**DOUBLE-CHECK LAW.** Every factual claim spoken in this reel traces to the
source script, and through it to the underlying repository documents. Nothing in
the narration was rounded, softened, or sharpened for rhythm.

**No-attribution rule for this reel:** the video must not name a person or a
specific outside project — it stays focused on the topic (cross-agent
validation) rather than on who else has worked on it. This changes how sources
are cited below: findings that trace to a specific named external system are
still fact-checked against that source internally (so a challenged claim can be
re-verified), but the reel itself refers to them only as "the research" or "a
published study," never by name. The one exception is the presenter's own name
in B00/B09 — that's self-attribution, not a reference to someone else's work.

**Primary source:**
`D:/Code/mycroft/verification-layer/divij/video-script-cross-agent-validation-20min.md`
(PART ONE — cold open, chapters 1–6).

**Upstream sources the script itself cites** (verify against these if a claim is
challenged — internal use only, never named on screen):

| Ref | Document |
|---|---|
| S1 | `verification-layer/divij/sub-projects.md` — background on the structural problem (no individuals named in this reel) |
| S2 | `verification-layer/divij/sota-research.md` — staged-detection research, debate taxonomy, a full-scale ablation study (systems referred to generically, never named) |
| S3 | `verification-layer/divij/audit.md` — the accountability layer audit |
| S4 | `verification-layer/consistency.py` — module docstring, scoring weights, thresholds (this project's own code) |
| S5 | `verification-layer/divij/cross-agent-validation-proposal.md` |
| S6 | Project constitution — "AI executes, humans decide" |

---

## Numeric claims spoken aloud

Every number in the narration, with its source. **If a row here cannot be
re-verified, cut the claim from the narration rather than hedging it.**

| Beat | Spoken as | Value | Source |
|---|---|---|---|
| B00 | "revenue grew twelve percent … the other says eight" | 12% / 8% | Script cold open — illustrative example, explicitly hypothetical, not a measured figure |
| B03 | "sixty percent … forty percent" *(implied, not spoken in V1 — see V2 B02)* | — | not spoken in this reel |
| B05 | "about seventy-three percent of pairs with no model call" | 73% | Script ch.4 → S2, a staged-detection study (unnamed on screen) |
| B05 | "sixty-two percent lower cost" | 62% | Script ch.4 → S2 |
| B05 | "ninety point eight percent accuracy held" | 90.8% | Script ch.4 → S2 |
| B06 | "faithfulness drops zero point one one nine" | −0.119 | Script ch.5 ablation table → S2, a full-scale ablation study (unnamed on screen) |
| B06 | "it costs zero point zero zero six" | −0.006 | Script ch.5 ablation table → S2 |
| B07 | "-0.119 … -0.006" *(on-card text only)* | same | same |

**Numbers cut from V1 of this file that this rewrite deliberately drops:** the
exact agent/phase count and question count for the ablation study (previously
"nine agents, eight phases, five hundred questions"). Those figures were
specific to one named system; without naming it on screen, stating its exact
counts would misattribute a specific study's numbers as if they were generic to
"the research." B06 now says "many specialized agents across multiple phases,
evaluated on hundreds of questions" — true in shape, not falsely precise for an
unnamed source. The ablation deltas (−0.119 / −0.006) are kept because they are
introduced explicitly as "one published ablation study," which is honest without
naming it.

## Non-numeric factual claims

| Beat | Claim | Source |
|---|---|---|
| B01 | Verifying correctness requires ground truth; verifying disagreement requires nothing | Script ch.1, "Correctness is not mechanically decidable. Disagreement is." |
| B02 | A model that confabulated a conclusion will confabulate an explanation for it | Script ch.1 |
| B02 | The reasoning trace is itself generated output, not evidence about the conclusion | Script ch.1 |
| B02 | Any system graded only by its own output will always look consistent, because consistency is all it was asked to produce | Reframed from script ch.1's anecdote (see "Simplifications" below) into a structural claim that doesn't depend on any named group |
| B03 | Self-consistency sampling already existed in the system, built months earlier | Script ch.2 → S4 |
| B03 | "Two identical confabulations are still confabulations. High consistency is weak positive evidence… Low consistency is strong negative evidence." | Verbatim from S4's module docstring, quoted in script ch.2 — **VERBATIM QUOTE LAW: do not paraphrase this on screen** |
| B03 | Two samples from one model are two draws from one distribution, not two opinions | Script ch.2 |
| B03 | Cross-model consistency checking measurably outperforms resampling one model | Script ch.2 → S2 |
| B04 | Debate is truth-seeking when agents have different relevant information; with the same information it becomes a persuasion contest | Script ch.3 → S2 (multi-agent debate literature, cited generically) |
| B04 | Averaging outputs or majority voting can amplify shared errors rather than cancel them, when agents share a training distribution | Script ch.3 → S2 (arbitration literature, cited generically) |
| B04 | Ensembling only cancels error when errors are independent | Script ch.3 |
| B05 | The debate literature sorts disagreement into four kinds: stylistic, reasoning, high-confidence, adversarial | Script ch.4 → S2 |
| B05 | For high-confidence disagreement the recommendation is to surface, not synthesize a false consensus | Script ch.4 → S2 |
| B05 | Staged detection: cheap classifier first, escalate only below a confidence threshold | Script ch.4 → S2, threshold 0.7 |
| B06 | Removing adversarial debate is the largest single faithfulness drop in a published ablation | Script ch.5 → S2 |
| B06 | Removing authority weighting costs essentially nothing | Script ch.5 → S2 |
| B06 | A system that arbitrates and answers is the right call for a QA product | Script ch.6, genericized — the source script names a specific system here; this reel does not |
| B06 | Arbitration requires verifiable model heterogeneity; without it, arbitration hides the evidence of error | Script ch.3 + ch.6 |
| B06 | "Machines verify conformance. Humans verify adequacy." | Script ch.6 → S6, project constitution |

## On-screen-only claims (not spoken)

These appear in `show` events or Remotion props and are still bound by the
DOUBLE-CHECK LAW.

| Beat | On-screen text | Source |
|---|---|---|
| B02 | Six identical "CONSISTENT" stamps on an anonymous agent grid | Illustrates the structural claim above — not a quote, not attributed to anyone |
| B05 | "threshold 0.7" | Script ch.4 → S2 |
| B05 | "−62% API COST", "90.8% ACCURACY" | Script ch.4 → S2 |
| B06 | "HUNDREDS OF QUESTIONS" | Genericized from Script ch.5's exact benchmark size (see numeric-claims note above) |
| B06 | Ablation rows: baseline ("full system"), without adversarial debate, without authority weighting | Script ch.5 table → S2, row label genericized from the named system to "full system" |

## Simplifications, declared

1. **The 12% / 8% figures are illustrative, not measured.** They are the script's
   own hypothetical. No beat presents them as an observed result. Video 2 is
   explicit that no genuine cross-agent disagreement has been observed on live
   data — this reel must not imply otherwise.
2. **B02 no longer cites a specific group or count of people.** The source
   script grounds "you cannot check an agent's work" in an anecdote about a
   specific group of builders reaching the same conclusion independently, quoted
   by name. Per the no-attribution rule, this reel drops the anecdote and the
   quotes entirely and states the underlying claim directly: a system graded
   only by its own output looks consistent by construction. This is a stronger,
   more general claim than the anecdote was — it doesn't rely on the reader
   trusting that six particular people's experiences generalize.
3. **The full-scale ablation study's pipeline is shown, not explained, and not
   named.** B06's first movement draws several nodes across multiple phases
   purely to convey scale. No claim is made about what any individual phase
   does, and no system name appears on screen or in narration.
4. **A named system's detailed conflict-type breakdown and its claim-type ×
   modality weighting matrix are cut entirely** rather than partially quoted or
   genericized. Presenting exact figures without their source would misstate
   them as generic findings; omission does not.
5. **"Cross-model consistency checking outperforms resampling"** is stated as a
   research finding, not as something measured in this project. It has not been
   measured in this project.

## Claims deliberately NOT made

The register constraint for this reel: the subject is a system that refuses to
overclaim, so the narration must not either. No beat claims that:

- cross-agent validation catches errors, finds bugs, or improves accuracy;
- disagreement detection tells you which agent is right;
- any of this has been validated on live production disagreement (it has not —
  see Video 2, B07);
- the ablation results shown in B06 transfer to any other domain or benchmark;
- the reader should recognize, trust, or seek out any specific outside system —
  the reel deliberately never names one.
