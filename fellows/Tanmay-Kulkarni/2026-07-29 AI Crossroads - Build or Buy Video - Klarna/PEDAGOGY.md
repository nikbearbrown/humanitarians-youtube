# PEDAGOGY — The Artificial Intelligence Crossroads: Build or Buy? (Klarna case)

## Thesis

The sibling folder `../the-artificial-intelligence-crossroads` built its "build or
buy" scenario around a fictional company (TechServe) and a fictional rival
(StreamlineOS). This version keeps the same theme but replaces the invented
scenario with a real, primary-sourced case: **Klarna's AI customer-service
deployment** (Feb 2024 launch → May 2025 partial reversal → Nov 2025 hybrid
recovery), read through a real peer-reviewed mechanism — the **Productivity
J-Curve** (Brynjolfsson, Rock & Syverson).

Central claim: **build-or-buy was never the operative question.** Klarna
bought (partnered with OpenAI) and still hit the J-Curve dip, because the
*complementary* work — retraining, edge-case handling, deciding which cases
need a human — lagged the rollout. The video's thesis is constructive, not a
cautionary tale alone: the ending is the hybrid model that actually recovered
and improved (Q3 2025 numbers beat the original Feb 2024 numbers), not "AI
failed."

## Persona / register

Built on the **`claude-hai`** channel (ai-explainer skill): Claude visual
fidelity brand, Kokoro **`af_bella`** ("Bella"), **Pragmatist** register —
method, when to use it, when NOT to. This is a direct persona/voice
requirement of `claude-for-design`'s existing HAI content in this repo (see
the sibling folder's metadata: `channel: hai`, `audience: HAI Fellows`); the
original draft's voice (`af_kore`) isn't available in this installed
toolkit, so `af_bella` is the closest in-toolkit equivalent for the same
persona family.

## Act structure

- B00 cold open (ASK→RESULT) states the pattern-recognition premise.
- B01–B02: the launch (real numbers) and the crack (CEO's own admission) —
  each graded on its own terms, not collapsed into one beat.
- B03: the mechanism (Productivity J-Curve) — explains *why* the dip
  happens, not just that it happened.
- B04: the reversal — what Klarna actually changed (hybrid model).
- B05: one bounded "Irreducibly-Human" aside (per the `hai` skill's rule —
  0–1 per video, only where it fits cleanly) — the AI/human task boundary,
  stated once, not repeated.
- B06: the recovery — Q3 2025 numbers, landing the constructive ending.
- B07: verdict recap (ClaudeVerdictArtifact).
- B08: RESEARCH-lane worked exercise (second-to-last, per `hai` skill spec)
  — a genuinely runnable Claude prompt, not illustrative.
- B09: title-restate outro, @HumanitariansAI handle.

## Evidence discipline

| Claim | Source | Date | Confidence |
|---|---|---|---|
| Productivity J-Curve mechanism | Brynjolfsson, Rock & Syverson, NBER WP 25148; *American Economic Journal: Macroeconomics* 13(1), 333-72 | Oct 2018 (WP) / Jan 2021 (journal) | High — peer-reviewed |
| 2.3M chats/30 days, =700 agents, 67% of chats, 11min→<2min, ~$40M projected | Klarna official press release; corroborated by OpenAI's own case study | 27 Feb 2024 | High — primary, company's own numbers. "700 agents" explicitly labeled on-screen as workload-equivalence, not a headcount cut |
| CEO: "we focused too much on efficiency and cost... lower quality"; rehiring humans | CEO Sebastian Siemiatkowski, Bloomberg interview, reported by Forbes/CNBC | 14–18 May 2025 | High — on-record quote, multiple outlets |
| Headcount fell 5,527 (end 2022) → 3,422 (end 2024); CEO separately attributed much of the drop to natural attrition/hiring freeze, "not solely due to AI" | Klarna F-1/S-1 SEC filing | Filed 2025 | High — official regulatory filing. Note: CEO gave inconsistent verbal headcount figures in different interviews — not resolved, not used on screen |
| Q3 2025: 853-agent equivalent, ~$60M savings, 82% faster, NPS 73, hybrid model (humans handle disputes/hardship) | Q3 2025 earnings call, reported by Yahoo Finance / CX Dive | Nov 2025 | Medium-high — company-reported, consistent across outlets |
| Deployment scoped to "easiest" support tickets (authenticated, structured, common intents) | Industry analyst commentary (secondary) | 2024–2025 | Medium — analyst interpretation, not a Klarna admission itself; framed as such on screen |

Not used (flagged low-confidence during research, no primary source found):
the "76% of AI use cases now purchased" and "$780K/14 months wasted" stats —
only found via SEO-aggregator blogs, not the primary Menlo Ventures/Gartner
reports. Excluded from the script rather than risk an unverifiable claim.

## Friction protected

- Kept the CEO's *inconsistent* verbal headcount claims as an unresolved
  discrepancy in this document (not smoothed over) — but kept it **out of
  the on-screen script**, since resolving it isn't necessary to land the
  thesis and airing an unresolved number would be a DOUBLE-CHECK LAW risk.
- Kept B05 (Irreducibly-Human) to exactly one bounded aside, per the `hai`
  skill's "most reels get none" rule — earned here because the thesis is
  literally about that boundary, not forced in as filler.
- Ended on the Q3 2025 recovery, not the May 2025 low point — the honest
  ending, and the one that actually serves an "encourage thoughtful AI
  adoption" goal rather than a pure cautionary tale.

## Outstanding before this can build

Three new Remotion components needed (reel-scoped, not yet built):
`KlarnaStatBlock` (B01, B06), `KlarnaSplitCard` (B02, B04, B05),
`KlarnaJCurve` (B03). B00, B07, B08, B09 reuse existing ready-made
compositions (`ClaudeComposerAsk`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`) unchanged, same as the CommBank reel.

## Fact-check pass (2026-07-29)

Full beat-by-beat audit run against every factual/numerical claim — see
`FACTCHECK.md` for the complete table. Two script corrections required and
applied: B02's "easiest slice of support work" framing was unattributed
analyst commentary presented as fact (now attributed on screen); B07's
"hit the J-Curve dip, *because* the complementary work lagged" overstated
causation Klarna never confirmed (now reworded as an explicit interpretive
lens — "reads like the Productivity J-Curve"). Two lighter corrections also
applied: B02's date tightened to "May 2025"; B04's category breakdown
(disputes/refunds/hardship) reworded as reported rather than flat fact,
since no primary Klarna statement itemizes those exact categories. Full
before/after wording logged in `FACTCHECK.md`. No other beat required a
script change; B01/B03/B05/B06 had documentation-only notes (paraphrase
labeling, editorial-framing disclosure) logged there instead.

VERDICT: PASS — narration reviewed and approved by the author (2026-07-29,
re-confirmed after the fact-check corrections above): reads natural, not
robotic ("sounds as if a human is narrating it"). Cleared to generate
audio.
