# PEDAGOGY AUDIT — hai-claude-on-average

**Authoritative sheet:** beat_sheet.hai.json
**Build copy:** beat_sheet.json
**Date:** 2026-07-16
**Auditor:** automated (unattended batch)

---

## Beat count and structure

- Total beats: 10 (B00–B09)
- Closing order: B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO ✓

## Metadata check

| Field | Required | Found | Pass? |
|---|---|---|---|
| audience | HAI | HAI | ✓ |
| register | Pragmatist | Pragmatist | ✓ |
| voice_kokoro | am_onyx | am_onyx | ✓ |
| engine | kokoro | kokoro | ✓ |
| palette | humanitarians | humanitarians | ✓ |
| slug | claude-on-average-hai | claude-on-average-hai | ✓ |
| output_file | claude-on-average-hai.mp4 | claude-on-average-hai.mp4 | ✓ |
| outro_source | AUTHOR.MD :: Humanitarians AI | AUTHOR.MD :: Humanitarians AI | ✓ |

## Audience register — Pragmatist

- B00 leads with operational rule: "Treat every Claude response as one sample, not a stable database result." ✓
- Efficient framing: decision rules, not narrative ✓
- When to use stated: options, drafts, summaries, provisional hypotheses (B05, B08) ✓
- When NOT to use stated: payments, eligibility, safety, legal, exact repetition (B05, B06, B08) ✓
- No warmth, no wonder language — direct and instrumental throughout ✓

## CLI exercise check (B08)

- B08 contains cli_exercise block ✓
- lane: BUILD ✓
- ask: paste-ready claude "..." command for five-run variance table ✓
- output_description: "A five-run variance table separating stable claims from unstable wording and recommendations." ✓
- change: "Add consequence-of-error and required-control columns; mark high-consequence unstable fields as blocked." ✓
- output2_description: "A deployment gate table showing which fields need sources, code, or human approval." ✓
- next_step: "Run it on your own production prompt and real acceptance criteria." ✓
- ASK/OUTPUT/CHANGE/OUTPUT2 structure present ✓
- B08 is second-to-last (B09 is outro) ✓

## Factual preservation — Claude, On Average content checks

- Token-by-token from context-conditioned probabilities (B03): "The model predicts the next token from the prompt, system message, and tokens already generated. It constructs the response sequentially. It does not retrieve a complete stored answer. Context changes the probability of every continuation." ✓
- Responses are samples from a distribution (B00, B02): "Treat every Claude response as one sample… Do not cache one generated response as the correct answer." ✓
- Temperature zero narrows but doesn't guarantee fixed context-independent answer (B04): "Temperature zero reduces sampling variation but does not specify an exact output. A changed persona, system message, or preceding context can still change the result." ✓
- B07 verdict lines identical to canonical: distribution not database, temperature steers not specifies, variance/scripts/gates ✓

## B08 AI-USE-BOUNDARY + cli_exercise check (HAI requirement)

- When variability creates value: "drafts, options, summaries, and provisional hypotheses" ✓
- When not to use unverified draw: "payments, eligibility, safety, legal conclusions, or any output that must repeat exactly" ✓
- Controls specified: "deterministic checks and a named human approver" ✓
- cli_exercise operationalizes the boundary: five-run variance test identifies which fields need deterministic control ✓
- Both sides of use/do-not-use boundary present with concrete examples ✓

## Learning sequence

B00 (operational rule: sample not database) → B01 (test: three draws) → B02 (no unique correct answer) → B03 (next-token mechanism) → B04 (temperature reduces but doesn't pin) → B05 (use variance for exploration, not high-consequence) → B06 (one draw insufficient for certification) → B07 (operating rule synthesis) → B08 (use/do-not-use + cli exercise) → B09 (outro)

Sequence follows Pragmatist: rule first → demonstration → categorical reasoning → implementation → accountability → synthesis → boundary + exercise ✓

## Outro check (B09)

- pattern: OutroCTA ✓
- handle: @humanitariansai ✓
- ctaText: "More at humanitarians.ai" ✓
- Narration: "Apply the method with Humanitarians AI. More at humanitarians.ai." ✓

---

VERDICT: PASS
