# FACTCHECK — I Built Lemonade's Claims Bot (Lemonade claims workflow)

Beat-by-beat audit, run 2026-08-10 against `beat_sheet.json` and re-run
2026-08-11 after the B06 and B09/B10 revisions. Every claim checked against the
strongest available primary source, or against the repository artifact it
describes. Nothing was silently repaired — every correction below was proposed
first, then applied only after author review.

Two claim types recur and are graded differently:

- **Claims about Lemonade** — held to primary disclosure. Sourced to the FY2025
  Form 10-K or to the audited findings of `07-lemonade-agentic-ai-insurtech-CASE-STUDY.md`.
- **Claims about this repository's own pipeline** — the artifact is on screen and
  is its own evidence. Verified by running the code, not by citation.

| Beat | Claim | Verdict | Evidence | Source | Correction |
|---|---|---|---|---|---|
| B01 | 96% of first notice of loss taken without human intervention | SUPPORTED | Direct company disclosure, dated | Lemonade FY2025 Form 10-K, filed 25 Feb 2026 | None |
| B01 | ~55% of claims automated end to end | SUPPORTED | Same filing | Same | None |
| B01 | Outcomes disclosed in detail, mechanism not | SUPPORTED | The case study's own central finding, audited across filings, letters, decks, blog posts and interviews | Case study §3.2, §6.1 | None |
| B01 | "No dollar threshold, claim-type list or confidence score appears in any filing, letter, deck or interview" | SUPPORTED as an audited absence | An absence cannot be sourced to one document; the claim self-describes its own audit scope | Case study §3.2, §6.3 | None — flagged as the tightest sourcing point in the film, see notes |
| B02 | Three stages, in order, stopping at the first rejection | SUPPORTED | Describes this repo's pipeline, not Lemonade's; the diagram on screen is the artifact | `orchestrator.py`, `verification.py` — verified 2026-08-10 | None |
| B02B | The four questions | Not a factual claim | Method, stated as method | Video's own framework | None |
| B03 | "Sofia" is an illustrative scenario, not a real customer | CONSTRUCTED — **and labelled as such** | Stated in narration *and* on screen before any of her details are used | Case study §4 preamble | None — the labelling is a must-preserve pairing, not to be shown without it |
| B03 | Extracted fields and 0.95 confidence | SUPPORTED | Real output from a real run, not illustrative numbers | `demo/run_sample_claims.py`, run 2026-08-10 | None |
| B04 | The scaffold's LLM adapter is a deterministic fake | SUPPORTED | The artifact | `llm_provider/fake_adapter.py` | None |
| B04 | A real model will wrap JSON in prose, invent a field, or time out | Editorial — engineering judgment | Not a citable fact about any named entity; stated as what you should expect and design for | Creator's own analysis | Documentation only — logged as judgment, not sourced fact |
| B04 | The extraction instruction is `[DEV]`-marked and untuned | SUPPORTED | The artifact | `intake.py`; repo README | None |
| B05 | Four checks, fail-fast ordering, every escalation reason named | SUPPORTED | Verified by running the suite; spy assertions prove later stages never execute | `verification.py`, `tests/` | None |
| B06 | Record lookup and fraud signal are independent modules | SUPPORTED | Two tests assert neither module imports the other | `tests/test_mock_*.py`; DESIGN_DECISIONS §7 | None |
| B06 | "Outside coverage keeps merging them into one" | QUALIFY → **FIXED** | A claim about third-party coverage. Correctly hedged and attributed to "outside coverage" in narration, but originally carried **no source on screen** | Case study §6.5 | **Source line added beneath the fraud card**: "Forensic Graph and AI Jim are separate systems in Lemonade's FY2025 Form 10-K — case study §6.5." Resolves at ~24s, ahead of the ~28s assertion |
| B06 | The matching tolerance is invented and `[DEV]`-labelled | SUPPORTED | The artifact; the marker is visible on screen | `config.py` | None |
| B06B | Predict beat | Not a factual claim | Poses a question, asserts nothing | — | None |
| B07 | "…triages and assigns claims he is not authorized to settle…" | SUPPORTED | Verbatim quotation, shown on screen with its filing date | Lemonade FY2025 Form 10-K | None |
| B07 | The settlement boundary exists but is nowhere disclosed | SUPPORTED | Audited absence, stated as an absence rather than filled | Case study §3.2, §6.3 | None |
| B07 | `authorization_gate.py` ships with no rule, no default, no `[DEV]` marker | SUPPORTED | The entire file is legible on screen | `authorization_gate.py`; DESIGN_DECISIONS Decision 1 | None |
| B07 | "I could've put a number in there… I don't know that" | Editorial — explicitly first-person | The film's own reasoning about its own design choice, not an inference about Lemonade's motives | Creator's own decision | Documentation only |
| B07B | `demo_only_policy` is `amount < 500`, invented, and deliberately carries no `[DEV]` marker | SUPPORTED | A named, logged exception that predates the video; the absent marker is visible on screen against two marked values | DESIGN_DECISIONS Decision 2 | None |
| B08 | Production requires audit trail, policy version, plain-English explanation, idempotency | Editorial — domain judgment | Prescriptive ("you'd need…"), not a factual assertion about any named insurer | Creator's own analysis | Documentation only |
| B09 | 43 tests; spy assertions prove sequencing; none has called a real model | SUPPORTED | 43/43 verified passing 2026-08-10; adapters tested with the HTTP layer mocked | `tests/`; repo README | Reframed 2026-08-11 — **framing only, claim unchanged**, see corrections |
| B10 | The viewer task | Not a factual claim | A scaffolded exercise | — | Reframed 2026-08-11, framing only |
| B11 | Title restate | Not a factual claim | — | — | None |

## Documentation-only notes (no claim change, logged for the record)

**Test count.** 43/43 pass. On the host's system Python 3.9, three LLM-adapter
tests error with `ModuleNotFoundError: requests` — an undeclared dependency in
that environment, not a code defect; all 43 pass with `requests` installed. B09
speaks the count, but its point is the *limit* of what green proves, which
holds either way.

**Demo output is condensed on screen.** B09's terminal shows all eight claim
outcomes verbatim but omits the per-claim input text lines, and B07 condenses a
12-line module docstring to one line. Both are captioned on screen as
condensed. No logic and no outcome was omitted.

**Causal language.** No beat claims Lemonade withheld the settlement threshold
*because* of anything. B01 and B07 state the absence and stop. B07's reasoning
is explicitly the creator's own, in the first person.

**Not depicted anywhere**, per case study §3.2: computer-vision analysis of
claim video, any fraud-algorithm count ("18 algorithms"), or any dollar
threshold attributed to Lemonade. None is confirmed as current mechanism, and
the video-analysis claim was retracted by Lemonade itself in 2021 and led to a
$4M biometric-privacy settlement. The 2021 episode is out of scope for this cut
and is not referenced.

## Corrections applied

### 2026-08-11 — B06, source on screen (production-gate finding)

A full audit against `PROOF.md` returned teaching 12/12 but **failed the
production gate** on *sources on screen, not just voiced*. B06 asserted a claim
about third-party coverage with no attribution visible anywhere on the frame —
the only external claim in the film not carrying its receipt.

Minor in substance, structural in principle: B07's entire argument is that you
must not assert a shape of answer your source doesn't support, and PROOF holds
a film to its own standard first. Fixed with a dedicated `sourceNote` slot kept
separate from the design note, so a citation never reads as an instruction.
Verified on the shipped master at 184.5s, the moment the claim lands. Gate now
passes all three criteria.

### 2026-08-11 — B09 and B10, framing (no factual change)

Author feedback: B09's closing language read as negative about the test suite,
when a proven scaffold is precisely what this series delivers. The underlying
structural problem was that B08 already closes on "none of that is in my
scaffold," so B09 and B10 stacked two further deflating beats immediately
before the CTA.

**No claim was altered or removed.** B09 still states plainly that no test has
ever called a real model — now as the part left for the viewer to explore
rather than as a shortfall. B10's closing line changed from "most of us are
further away than we think" to "you'll be closer than you think on most of it —
you'll just know exactly where you're not."

## Verdict

Every factual claim in the film is either sourced to primary disclosure, sourced
to an audited finding in the accompanying case study, or is a verifiable
property of the accompanying code — and each is visible on screen at the moment
it is asserted. Editorial judgments are marked as such above and are stated in
the first person in the film itself.
