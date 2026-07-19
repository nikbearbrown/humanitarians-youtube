# FACTCHECK — vox-skip-rate
**Reading the Skip Rate: Why a Low Skip Rate Means the Filter Is Failing**
Source: `the-reallocation-engine/chapters/15-the-pipeline-tracker-and-the-skip-rate.md`

---

## Claims table

| Beat | Claim | Verdict | Source | Notes |
|------|-------|---------|--------|-------|
| B01 | AI analysis praises 80% apply rate as productive | ILLUSTRATIVE | Chapter Ex.5 pre-generated artifact: "you applied to 24 of 30 roles evaluated (80% apply rate, 20% skip rate), so you're being highly productive" | Constructed example from chapter; labeled illustrative |
| B02 | Weekly tracker: 30 roles evaluated, 24 applied, 6 skipped = 20% skip rate | ILLUSTRATIVE | Chapter Ex.5 artifact above; matches math: 6/30 = 20% | Numbers are illustrative; math is correct |
| B02 | AI read 20% skip rate as "highly productive — covering lots of ground" | ILLUSTRATIVE | Chapter Ex.5 pre-generated artifact verbatim | Illustrative |
| B03 | Question framing | n/a | Derived question — no fact claim | |
| B04 | Pipeline Tracker is the engine's fifth component | minor | Chapter: "The Pipeline Tracker, the engine's fifth component" — chapter says fifth, but the video doesn't use that specific claim | Not asserted in narration |
| B04 | Skip rate target is at least 50 percent | PASS | Chapter: "the target is a skip rate of at least fifty percent" | Exact quote |
| B05 | Below 40%: too loose | PASS | Chapter: "Below forty percent is too loose." | Exact quote |
| B05 | 40–50%: borderline | PASS | Chapter: "Between forty and fifty percent is borderline" | Exact quote |
| B05 | Above 50% with steady applies: healthy | PASS | Chapter: "Above fifty percent with steady applies and rising per-tier response rates is healthy" | Exact quote |
| B05 | Above ~85%: starved | PASS | Chapter: "Above roughly eighty-five percent…means the funnel is starved" | Exact quote |
| B06 | Skip is a decision, not absence | PASS | Chapter: "The skip is not an absence in the log. It is a decision" | Exact quote |
| B06 | Tracker logging only applications misses half the data | PASS | Chapter: "a tracker that logs only applications is missing half the data about how well the filter works" | Exact paraphrase |
| B07 | Below 50% skip rate means filter found almost everything | PASS | Chapter: "If you apply to nearly everything the engine surfaces, your filter is too loose" | Supported |
| B07 | Targeted two-hour block re-expanded | PASS | Chapter: "the targeted two hours from Chapter 2 has swollen back toward eight" | Paraphrase; narration softens to "re-expanded" correctly |
| B08 | Counter going up is not progress, it is the volume instinct | PASS | Chapter: "Low skip rate is not productivity. It is the filter failing." | Supported |
| B08 | Busy and unfiltered is what the engine exists to end | PASS | Chapter: "busy and unfiltered is exactly the state the whole book exists to end" | Exact paraphrase |
| B09 | Week A: 30 evaluated, 6 skipped, 20% skip rate | ILLUSTRATIVE | Invented example per card seed; math correct: 6/30 = 20% | Labeled illustrative in narration |
| B09 | Week B: 30 evaluated, 18 skipped, 60% skip rate | ILLUSTRATIVE | Invented example per card seed; math correct: 18/30 = 60% | Labeled illustrative in narration |
| B09 | Week B: 2 referrals from freed networking hours | ILLUSTRATIVE | Card example seed; invented but plausible | Labeled illustrative in narration |
| B09 | Week A: 0 referrals | ILLUSTRATIVE | Card example seed | Labeled illustrative in narration |
| B10 | Low skip rate felt more productive; high skip rate was | PASS | Chapter: "The reflex to resist is feeling good about a low skip rate because 'I'm applying to a lot of things.'" | Captures the inversion |

---

## Terms table

| Term | Debut beat | Earlier beat creating need |
|------|-----------|---------------------------|
| skip rate | B01 (implied) / B02 (explicit) | B01 — the "praised" situation creates the need for the measuring instrument |
| filter | B02 | B01 — "the praise is a warning sign" creates the need to ask what failed |
| Pipeline Tracker | B04 | B02 — the weekly data implies a tracking instrument |
| decision bands | B05 | B04 — the dial is introduced, bands follow naturally |
| volume instinct | B08 | B07 — "filter collapse" names the dynamic; volume instinct names the driver |

---

## Exclusions confirmed

- No detail on per-tier response rate analysis — excluded. Does not appear anywhere.
- No tracker recipe or analyze-patterns.py implementation — excluded. Does not appear anywhere.
- No discussion of privacy rules around tracker files — excluded. Does not appear anywhere.

---

## Illustrative numbers flagged

All numbers in B09 (the example act) are invented but plausible:
- 30 evaluated, 6 skipped, 20% (Week A) — illustrative
- 30 evaluated, 18 skipped, 60% (Week B) — illustrative
- 2 referrals (Week B) — illustrative
- 0 referrals (Week A) — illustrative

Narration labels these as "Illustrative numbers."

The 30-role / 24-apply / 6-skip example in B02 comes from the chapter's own Exercise 5 pre-generated artifact, labeled illustrative.
