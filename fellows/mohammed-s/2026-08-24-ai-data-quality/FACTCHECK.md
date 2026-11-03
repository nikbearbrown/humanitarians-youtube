# FACTCHECK — `ai-data-quality` · "The Rule, Not The Report."

**DOUBLE-CHECK LAW applied.** This reel has **no external source document**.
It is a conceptual explainer built on a single **declared worked example** —
a fictional warehouse used consistently across all twelve beats. Nothing here
is presented as, or derived from, published industry data.

That decision is enforced two ways:

1. Every beat that puts a number on screen carries the footnote
   **`Worked example · illustrative figures`** (props: `footnote`).
2. The narration never attaches a number to a source, a vendor, a study, or a
   "companies find that…" framing. The numbers are the example's own.

---

## Claim ledger

| # | On-screen / spoken claim | Verdict | Basis | Action taken |
|---|---|---|---|---|
| 1 | "4,000 columns, 12 documented rules" | **WORKED EXAMPLE** | Invented premise of the example warehouse | Footnoted on B00/B02 |
| 2 | "98.7% data quality score" | **WORKED EXAMPLE** | Invented | Footnoted on B01 |
| 3 | Six spellings of one country all pass a presence/type check | **TRUE — mechanism** | A NOT NULL + string-type check cannot distinguish `US` from `United States`; this is definitional, not empirical | Kept; no source needed |
| 4 | "~40 minutes to agree one rule" | **WORKED EXAMPLE** | Invented, deliberately conservative | Footnoted on B02; narration says "about" |
| 5 | 3,988 × 40 min = 330 working days | **ARITHMETIC — VERIFIED** | 3,988 × 40 = 159,520 min = 2,658.7 h ÷ 8 = **332.3 days** → stated as 330 | Rounded down; on-screen strip shows the multiplication so the viewer can check it |
| 6 | "They go stale in ninety [days]" | **WORKED EXAMPLE** | Invented; rhetorical, not measured | Footnoted; narration keeps it as part of the example |
| 7 | "318 candidate checks → 218 ratified / 59 needs owner / 41 rejected" | **WORKED EXAMPLE — RECONCILED** | 218 + 59 + 41 = **318** ✓ matches B00's stated 318 and B00's "flagged 41 columns" | Numbers cross-checked across B00 and B06 |
| 8 | "1,284 rows would newly fail (39%)" | **WORKED EXAMPLE — CONSISTENT** | 1,284 / 0.39 ≈ 3,292 rows; consistent with a sample table. Also consistent with the value distribution shown (22+9+5+3 = **39%** non-`US` values) ✓ | The 39% is *derived from the bars on screen* — the viewer can add them up |
| 9 | Value distribution US 61 / USA 22 / United States 9 / U.S. 5 / blank 3 | **WORKED EXAMPLE — SUMS TO 100** | 61+22+9+5+3 = **100** ✓ | Verified |
| 10 | "ISO_3166_1_ALPHA_2" as the allowed set for country codes | **TRUE** | ISO 3166-1 alpha-2 is the real two-letter country-code standard (`US`, `GB`, `IN`) | Used correctly as the example's allowed set |
| 11 | "Auto-correction produces an edit nobody can trace" | **TRUE — conditional, stated conditionally** | True *when* the correction is applied in place without a change record. The narration says "let it auto correct, and you have inherited a silent edit nobody can trace" — the conditional is intact | Kept |
| 12 | "A column of all-load-date dates passes every check" | **TRUE — mechanism** | A type/nullability/format check on a date column cannot detect that the values are semantically wrong. Definitional | Kept |
| 13 | "Rules rot / the business changed, the check didn't" | **TRUE — mechanism** | A static assertion does not track a changed definition. Definitional | Kept |

## De-sensationalising pass

- **Cut:** any framing of the form "AI can automatically fix your data
  quality" — that is the claim the reel exists to argue against.
- **Cut:** any percentage improvement, ROI figure, or time-saved claim.
  None appear.
- **Cut:** all model names, version numbers, and vendor capability claims
  from the narration (they date the video). "Opus 5" appears only as the UI
  model chip inside the Claude-skin composer beats, which is set dressing,
  not a claim.
- **Kept soft:** "about forty minutes", "roughly", "three hundred and thirty
  working days to write them **once**" — the "once" is doing real work.

## Corrections applied during scripting

1. **11 person-years → 330 working days.** The first draft asserted ~11
   person-years from the same premise. Recomputed: 3,988 × 40 min is 332
   eight-hour days ≈ **1.3** person-years, not 11. The claim was wrong by
   ~8×. Fixed, and the multiplication was moved *on screen* so it is
   checkable rather than asserted.
2. **"41 rejected" reconciled to B00.** B00 says 41 columns had no inferable
   rule; B06's reject lane also reads 41. These are two different facts about
   the same example, so the reject lane note was rewritten to
   "a rule the business never had" to keep them distinguishable.
3. **"green tick" removed from B01's score card.** The Claude palette allows
   exactly one accent (terracotta); a green success tick would break the
   accent law and add a second focal colour. The card now reads as ink-on-
   cream and only the *strike* is terracotta.

## Sources

None. This reel cites no external document and makes no empirical claim.
ISO 3166-1 alpha-2 is referenced as a naming standard only:
<https://www.iso.org/iso-3166-country-codes.html>
