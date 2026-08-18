# PEDAGOGY — I Built Lemonade's Claims Bot

**Here's What Production Would Actually Need**

Week 17 · work-derived lane · teaching walkthrough
Register **Pragmatist** · Kokoro **`af_bella`** · brand `claude` · 2160p

Built from `../07-lemonade-agentic-ai-insurtech-CASE-STUDY.md` and its
companion reference implementation `../lemonade_claims_pipeline/`.

> Supersedes the Rev 1 premise (a skeptical teardown built on a three-bucket
> disclosure framework, Teardown register, `am_onyx`). That premise was
> redirected by the author before scripting: this film teaches the workflow
> actually built this week, and what it would take to make it real.

---

## Lane

**Work-derived** — a film about the work actually done this week, the same
lane as Week 15's CommBank reel. Deliberately *not* the repo-topic lane that
produced the Klarna "AI Crossroads" film, which was selected from a
`humanitarians-youtube` topic suggestion. The two lanes are not mixed.

Prior reels were referenced for **format conventions only**. Structure,
visuals, components, register and voice are original to this film. It shares
no act structure with either predecessor: no ASK→RESULT cold open, no
verdict-recap card, no title-restate outro.

## Thesis

Lemonade discloses claims *outcomes* richly and claims *mechanism* thinly. So
I built the workflow myself. The film walks that build one stage at a time and,
at each stage, answers what production would actually demand of it.

The teach is not Lemonade's numbers. It's the method for auditing your own
distance from production.

## The method — four questions

Shown as a structure at **B2B**, before any stage opens; visibly applied at
B4, B6 and B8; handed over at B10.

| # | Question | Answered at |
|---|---|---|
| 1 | **Dependencies** — what's mocked? | B4, B6 |
| 2 | **Invented values** — what did I make up, and does the code admit it? | B6, B7B, B8 |
| 3 | **Failure paths** — what happens when it says no? | B4 |
| 4 | **Accountability** — could you prove, afterwards, what happened and why? | B8 |

B9 lands the punch: 43 green tests prove **none** of the four.

## Act structure — interleaved

The pipeline is walked one stage at a time, each stage immediately followed by
what production demands *of that stage*. The viewer gets the mental model
before the requirement, every time — which is why the production content is
not quarantined into a closing section.

| Beat | Role |
|---|---|
| B1 | Hook — 96% / 55% published, mechanism absent |
| B2 | Who I am + the pipeline map |
| **B2B** | **The four questions**, as a structure, before any stage opens |
| B3 | Intake — Sofia's claim becomes structured fields |
| B4 | *In production* — real model: retries, validation, cost · axes 1, 3 |
| B5 | Verification — four checks, fail-fast |
| B6 | *In production* — real data layer behind an unchanged interface · axes 1, 2 |
| **B6B** | **PREDICT** — what did I put in the gate? |
| B7 | The Authorization Gate — the file with no rule in it |
| **B7B** | **The edge case** — `demo_only_policy`, invented and unlabelled |
| B8 | *In production* — audit, policy version, explanation, idempotency · axes 2, 4 |
| B9 | What 43 green tests prove — and don't |
| B10 | Your turn — run the four questions |
| B11 | Close |

Each production beat moves differently so the middle never goes metronomic:
B4 **branches** into failure, B6 **substitutes** behind a fixed interface, B8
**accumulates** layers around an unchanged decision.

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| 96% of FNOL with no human; ~55% closed end to end | Lemonade FY2025 Form 10-K, filed 25 Feb 2026 (case study §3.1) | OK — primary |
| "claims he is not authorized to settle" | Same 10-K | OK — verbatim |
| No threshold / claim-type list / confidence score anywhere in the public record | Case study §3.2, §6.3 | OK — an audited absence, stated as an absence |
| Three stages, fail-fast, seven named escalation reasons | `orchestrator.py`, `verification.py` | OK — verified in code 2026-08-10 |
| Confidence 0.75 and tolerance 0.05, both `[DEV]`-marked | `config.py` | OK — verified |
| Gate ships with no rule, no default, no `[DEV]` marker | `authorization_gate.py`; DESIGN_DECISIONS 1 | OK — verified |
| `demo_only_policy` is invented and deliberately unlabelled | DESIGN_DECISIONS 2 — a named, logged exception | OK — verified |
| Sofia SETTLED / Zeus ESCALATED (`not_authorized`) | `run_sample_claims.py`, real run 2026-08-10 | OK — real output |
| 43 tests, spies prove sequencing, none call a real model | `tests/`; repo README | OK — **43/43 verified passing** |

No figure goes beyond what the case study or the repository itself sources.

**Not depicted anywhere**, per case study §3.2: computer-vision video analysis,
any fraud-algorithm count, or any dollar threshold attributed to Lemonade. The
2021 retraction and the BIPA settlement are out of scope for this cut.

**Sofia is introduced as an illustrative scenario** — in narration and on
screen — before any of her details are used. The case study constructs her;
she is not a real Lemonade customer, and the film says so.

**Test-count caveat.** 43/43 pass. On host Python 3.9 three LLM-adapter tests
error with `ModuleNotFoundError: requests` — an undeclared host dependency, not
a code defect. B9 speaks the count, but its point is the *limit* of what green
means, which holds either way.

## Friction protected

- **B6B commits the viewer before B7 reveals the answer.** Two undisclosed
  values got labelled defaults; the third got nothing. Without the reasoning,
  that asymmetry looks arbitrary — and sitting in that confusion is the lesson.
- **B7B keeps a counterexample that complicates the film's own rule.** The demo
  policy is invented like the others and deliberately carries no `[DEV]` marker.
  Left in rather than smoothed over, because a rule that can absorb its own
  exception is a rule.
- **Removed for time:** the case study's §5 results thread (LAE ratio, the
  $44→$14 pet cost curve, IFP growth), and the 2021 computer-vision retraction
  with the Forensic Graph conflation (§6.2, §6.5). Both are strong, and §6.5 is
  the same conflation pattern the CommBank reel corrected — but they belong to
  a disclosure-reading film, not this engineering one. Left in the source doc.

## PROOF rubric — projected 12/12

Scored honestly at 8/12 on Rev 1 and rebuilt; see `QC-REPORT.md` for the full
checkpoint and what each fix bought.

| Criterion | Score | Basis |
|---|---|---|
| Explicit framework | 2 | Four questions shown as structure at B2B, before any stage |
| Reusable rubric | 2 | Same axes visibly lit at B4/B6/B8 before B10 hands them over |
| Worked example | 2 | Sofia traced through all three stages, real demo output |
| Falsifiability | 2 | B7B — the exception that fits none of the film's own rules |
| Active task | 2 | B10 runs the four questions with explicit pass/fail |
| Friction | 2 | B6B — commit before the reveal |

A projection. Re-scored against the finished cut.

### Production gate

Binary; vetoes publish regardless of teaching score. Verified on real renders,
not asserted — the approved 4K frames are held in the working folder.

- **Legible at the moment of assertion** — B7's whole gate file reads without
  scrolling; B9's terminal output is sharp at render size.
- **Sources on screen** — B1 carries the filing date; B7 shows the verbatim
  10-K quote beside the code it's read against; B6 attributes its
  outside-coverage claim beneath the fraud card.
- **Side-by-side held** — B5/B6 hold identical row geometry so the delta is the
  only thing that moves; B7B contrasts labelled and unlabelled values directly.

**Gate finding, found and fixed 2026-08-10.** A full PROOF audit caught B6
asserting a claim about third-party coverage with no attribution on screen —
the one external claim in the film that wasn't sourced visually, in a film whose
own argument is that you must not assert what you can't show. Fixed with a
dedicated `sourceNote` slot, kept separate from the design note so a citation
never reads as an instruction. Verified on the shipped master at 184.5s, the
moment the claim lands. The finding and its resolution are recorded in
`QC-REPORT.md`; the full PROOF review is held in the working folder.

### Deviation logged

PROOF wants the framework inside the first ~20s. B2B lands at roughly 0:55.
*Framework before examples* holds in full — no stage opens before it — but the
20s target does not, because the hook and the map have to earn attention first.
Logged rather than smoothed over.

## Components

Seven cover all fourteen beats. Built generic and props-driven per PLAYBOOK §2,
not one per beat. All registered in `Root.tsx` before any pattern name entered
`beat_sheet.json`. Authored at 1920×1080, rendered at `--scale=2` for true
3840×2160 with supersampled text. All artwork vector.

| Component | Beats |
|---|---|
| `LemonadeStatGap` | B1 |
| `LemonadePipelineMap` | B2 |
| `LemonadeRubric` | B2B (`board`), B6B (`predict`) |
| `LemonadeStage` | B3, B5 |
| `LemonadeProduction` | B4 (`branch`), B6 (`swap`), B8 (`accumulate`) |
| `LemonadeCodeArtifact` | B7, B7B, B9 |
| `ClaudeComposerAsk` / `ClaudeTitleOutro` | B10, B11 — existing, unchanged |

---

## GATE P

**VERDICT: PASS** — narration and structure reviewed and approved by the author
(2026-08-10), and re-confirmed for the three beats added to reach 12/12 (B2B,
B6B, B7B), which introduce no new factual claim beyond the `demo_only_policy`
exception already logged in `DESIGN_DECISIONS.md` Decision 2.

Cleared to generate audio.
