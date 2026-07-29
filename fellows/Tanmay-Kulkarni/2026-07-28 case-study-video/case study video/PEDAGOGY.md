# PEDAGOGY — Claude, Untangled? (nbb / claude-liam ai-explainer)

Reel built from `05-commbank-agentic-ai-disputes.md`
(Week 15's CommBank case study). The episode's thesis IS the case study's own
central finding (Section 6.2): CommBank has two separate, independently
confirmed AI systems — a thinly-sourced payment-disputes tool and a
well-documented inbound voice bot tied to real 2025 layoffs — and wider
coverage has fused them into one false narrative: an autonomous "Dispute
Resolution Agent" that both handled disputes and caused the layoffs. No
primary source supports that fused version. This reel does not make any new
claim about CommBank; it dramatizes the case study's own sourced correction.

## Act structure
- B00 cold open with RESULT lines (ASK→RESULT at B00) ✓ — the ask states the
  viral premise; the output teases the correction.
- ILLUSTRATE LAW: UI only at B00 / B07 / B08 / B09. B01–B06 illustrate the
  concept with new components (merge myth → record fork → grade disputes tool
  → grade voice bot → predict → no-reconnection twist) — legal because none
  of these beats needs the Claude interface as its subject.
- PREDICT at B05 commits the viewer before the twist ✓ · HANDOFF "Your turn."
  reads the prompt and discusses it (HANDOFF LAW) ✓ · title-restate outro ✓.
- No two consecutive body beats share a visual state: B01 (merge/converge),
  B02 (fork/diverge), B03 (grid), B04 (timeline), B06 (broken two-card
  comparison) are each a distinct shape.

## Evidence discipline (source: the case study's own Sources table)
| Claim | Source | Verdict |
|---|---|---|
| ~15,000 disputes/day of >20M daily payments | Angus Sullivan via CBA newsroom / iTnews, Nov 2024 | OK |
| Disputes tool: 3 confirmed functions (intent / verify / auto-lodge), no name | Dan Jermyn via Evident Insights, 20 Feb 2025 | OK — single-sourced, stated as such |
| CBA's Dec 2025 "Our Approach to Adopting AI" report omits disputes/chargebacks entirely | CBA, Dec 2025 | OK |
| Voice bot launched Jun 2025, Direct Banking / Customer Service Direct | BankInfoSecurity, 25 Aug 2025 | OK |
| 90 roles cut, 45 in Direct Banking tied to voice bot | Finance Sector Union release, 29 Jul 2025 | OK |
| Reversal | Finance Sector Union bulletin, 21 Aug 2025 | OK |
| Chair Paul O'Malley on record, "We made a mistake," AGM | AAP News, 15 Oct 2025 | OK |
| "Dispute Resolution Agent" is vendor/consultancy terminology, not a CBA name | SAP/KPMG/Lyzr/Cognizant materials, reviewed only to confirm non-attribution | OK |
| The two systems have no documented connection to each other's outcome | Absence of any source linking them (case study Section 6.2) | OK — an honest absence, not a manufactured one |
| Same conflation pattern (real systems merged by outside coverage) now visible across 5 series entries (Goldman Sachs, JPMorgan Chase, BlackRock, Allianz, CommBank) | Case study Section 6.2, this series' own cross-entry observation | OK — attributed to outside/secondary coverage repeating the error, not to the case-study author |

No figure in this beat sheet goes beyond what the case study itself sources.
Dates, quotes, and headcounts are carried over verbatim from the case study's
own citations, register-rewritten for Teardown per DOUBLE-CHECK LAW.

## Friction protected
- Kept: B05 commits the viewer before B06's reveal — germane, it IS the
  lesson (most readers assume one system did both things).
- Kept: B03/B04 grade each system on its OWN thin/thick sourcing rather than
  collapsing the two into one "here's what's confirmed" beat — the asymmetry
  in how well-documented each system is is itself part of the finding.
- Removed for time: the case study's Section 5 detour into the *other* two
  CBA efficiency figures (76% scam-loss reduction, 40% wait-time reduction)
  that belong to neither system — genuinely interesting but a third thread a
  1–3 minute reel can't carry without diluting the two-system point. Left in
  the source doc for a longer cut if this ever becomes a deep-explainer.
- Removed: ChatIT (Section 3.3) — confirmed, but unrelated to the disputes
  vs. layoffs conflation this reel exists to correct.

## Editorial decision log
- **B07 wording, resolved 2026-07-28:** the author flagged that crediting "this
  series keeps catching this pattern" could misread as the case-study author's
  own drafts having been wrong, rather than what actually happened — the
  conflation lives in wider secondary coverage, and this series (across 5
  entries: Goldman Sachs, JPMorgan Chase, BlackRock, Allianz, CommBank) is the
  one correcting it against primary sources each time. Line rewritten to name
  "outside coverage" explicitly as the source of the failure. This is a
  strength claim about the author's methodology, not an admission.

## Outstanding before this can build
Five new Remotion components (B01 `CommbankMythMerge`, B02
`CommbankRecordFork`, B03 `CommbankDisputesGrade`, B04
`CommbankVoiceBotTimeline`, B06 `CommbankNoReconnect`) have been authored,
registered in `Root.tsx`, rendered, and visually QC'd (`_qc/REPORT.md`) — one
BLOCKER found (B02 outcome badges bled past the frame edge) and fixed,
confirmed clean on re-render. B05 / B07 / B08 / B09 reuse existing
ready-made compositions unchanged.

**Pre-audio field fix (2026-07-28):** `generate_audio_kokoro.py` (and every
other script that touches narration — captions, slate labels) reads only
`narration_text`, with no fallback. B00, B08, and B09 had been authored with
the actual spoken line in a non-canonical `narration` field while
`narration_text` held the on-screen typed command instead — left as-is, the
audio would have voiced the typed prompt verbatim (and B09's outro would have
said only "Claude, Untangled?" and stopped, dropping the sign-off entirely).
Fixed: the spoken lines now live in `narration_text` for all three beats; the
typed on-screen command for B00/B08 stays in `shot.remotion.props.command`,
independent and untouched. The redundant `narration` field was removed.

VERDICT: PASS — narration and structure reviewed and approved by the author
(2026-07-28), including the B07 revision. Cleared to generate audio.
