# PEDAGOGY AUDIT — hai-claude-judged

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
| slug | claude-judged-hai | claude-judged-hai | ✓ |
| output_file | claude-judged-hai.mp4 | claude-judged-hai.mp4 | ✓ |
| outro_source | AUTHOR.MD :: Humanitarians AI | AUTHOR.MD :: Humanitarians AI | ✓ |

## Audience register — Pragmatist

- B00 leads with method/decision rule: "Use Claude to check a video only when the acceptance criteria are explicit." ✓
- Efficient, no personality tax, no academic hedging ✓
- When to use stated (B00, B02, B05): determinable checks, explicit criteria ✓
- When NOT to use stated (B00, B02, B05): judgeable decisions, publication authority ✓
- No warmth, no philosophy — direct operational framing throughout ✓

## CLI exercise check (B08)

- B08 contains cli_exercise block ✓
- lane: RESEARCH ✓
- ask: paste-ready claude "..." command ✓
- output_description: concrete audit table result ✓
- change: add reversibility column ✓
- output2_description: table with high-risk handoffs highlighted ✓
- next_step: "Run it on your own publishing or service-delivery workflow." ✓
- ASK/OUTPUT/CHANGE/OUTPUT2 structure present ✓
- B08 is second-to-last (B09 is outro) ✓

## Factual preservation

- Determinable vs judgeable distinction (B02): "Separate determinable questions from judgeable ones. Determinable means the answer follows from inspectable evidence… Judgeable means the answer depends on purpose and audience." ✓
- Agents inspect schema, timing, paths, resolution, QC artifacts (B04): "beat count, duration, resolution, paths, and QC artifacts" ✓
- Human authority over publication (B05): "Keep publication authority with a human reviewer." ✓
- B07 artifact lines identical to canonical: schema/timing/paths/resolution (agents), interesting/worth watching/publish (humans) ✓
- B08 AI-USE-BOUNDARY: use when "criterion is explicit, the evidence is available, and a wrong result can be reviewed or reversed"; do not use as "final authority for audience impact, fairness, or publication" ✓

## B08 AI-USE-BOUNDARY + cli_exercise check (HAI requirement)

- When to use: "explicit criteria · available evidence · reversible action" ✓
- When not to use: "impact · fairness · publication" ✓
- Required control: "named human approver" ✓
- cli_exercise implements the boundary as an operational decision rule (audit table with human approver) ✓
- Both sides of boundary covered — operational decision framing (not a drill) ✓

## Learning sequence

B00 (lead with decision rule) → B01 (Gate P — deterministic preflight) → B02 (separate determinable from judgeable) → B03 (use cheap gates early) → B04 (delegate checks with evidence) → B05 (keep publication authority human) → B06 (operating model recap) → B07 (decision rule synthesis) → B08 (use/do-not-use + cli exercise) → B09 (outro)

Sequence follows Pragmatist structure: rule → tool → categories → implementation → accountability → synthesis → boundary + exercise ✓

## Outro check (B09)

- pattern: OutroCTA ✓
- handle: @humanitariansai ✓
- ctaText: "More at humanitarians.ai" ✓
- Narration: "Apply the method with Humanitarians AI. More at humanitarians.ai." ✓

---

VERDICT: PASS
