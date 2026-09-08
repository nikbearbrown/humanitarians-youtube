# FACTCHECK — claim-by-claim audit

Every factual, numerical and attributional claim in `beat_sheet.json`, checked before rendering
per PLAYBOOK §1 and GATE F.

**This film's subject is not over-claiming, so it is held to its own rule first.** Where a claim is
mine rather than HSBC's, the film says so on screen.

Verdicts: **SUPPORTED** · **QUALIFY** (true with a stated bound) · **INFERENCE** (labelled as such
in the film) · **CUT** (removed rather than shipped).

---

## 1. HSBC's figures — the left column

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B01, B03 | 60% faster unit testing, 5× faster patching | **SUPPORTED** | HSBC FY2025 Annual Results transcript, 25 Feb 2026, Elhedery, quoted |
| B01, B03, B13 | 1,165 applications retired, c.36% of a ~3,000 target | **SUPPORTED** | HSBC FY2025 Presentation, slide 4 fn 4 |
| B01, B03, B13 | $1.2bn annualised simplification savings realised, ahead of schedule | **SUPPORTED** | FY2025 transcript, Kaur, quoted |
| B03, B07 | "$1.5 billion of annualised simplification saves straight to the bottom line" | **SUPPORTED — verbatim, primary** | FY2025 transcript, read directly (see below) |
| B03, B07 | "the reallocation of circa $1.5 billion from non-strategic or low-returning businesses" | **SUPPORTED — verbatim, primary** | Same transcript |
| B08 | FY2025 $1.8bn = $1.5bn reallocation + $0.3bn Hang Seng synergies | **SUPPORTED — verbatim, primary** | Same transcript: *"adding the expected $0.3 billion of Hang Seng Bank cost synergies to the original $1.5 billion of reallocation costs, taking this to circa $1.8 billion"* |
| B08 | FY2024 $1.8bn = severance and up-front restructuring through 2026 | **SUPPORTED — via case study** | FY2024 transcript, 19 Feb 2025, Elhedery. ⚠️ **Quoted from the case study, not re-read from the primary by me.** The FY2025 side was verified directly; this side was not. |
| B06 | "vibe coding assistants" | **SUPPORTED** | FY2025 transcript, Elhedery |
| B03, B13 | All figures self-reported and unaudited, no published methodology | **SUPPORTED** | Case study §6.7. Stated on screen at B03, once, plainly |

### The two $1.5bn quotes were verified twice, and once corrected

Read out of the primary PDF with text extraction. **The extractor splits figures across lines**
(`$1.` + `5 billion`), and a first-pass quote was reconstructed across a break and came out
**truncated mid-sentence** — the Hang Seng line actually continues *"…of reported-basis cost
synergies across HSBC and Hang Seng Bank."*

Corrected after a second extraction with line breaks joined. **Standing rule for this film:** any
HSBC quote going on screen is re-extracted with `" ".join(text.split())` before it is trusted. A
film about numbers meaning two things cannot ship a quote that stops halfway.

## 2. Absence claims — the ones that needed scoping

| Beat | Claim | Verdict | Note |
|---|---|---|---|
| B05 | HSBC never connects coding assistants to headcount savings | **QUALIFY** | Rewritten before render. Was an absolute across three named documents; now *"I couldn't find HSBC connecting…"* The case study's own wording is *"in any disclosure this case study identified"* (§5.5, §6.5), and the film may not claim more than that. |
| B06 | No tool, model, workflow or baseline disclosed | **QUALIFY** | Case study §6.1 states no HSBC source discloses these. Categorical in the source, so the film's "anywhere" is inherited rather than invented — but it is an absence claim and is flagged as such here. |
| B11 | No HSBC source describes a code-specific review gate | **SUPPORTED** | Case study §3.2, §6.1 — HSBC states a general governance principle only |

## 3. The inference, and its stated overturn condition

| Beat | Claim | Verdict |
|---|---|---|
| B10 | HSBC uses "agentic AI" for the Google Cloud financial-crime system and not for its coding tools | **SUPPORTED** — two disclosures, ~4 months apart |
| B10 | Therefore HSBC treats coding assistants as assistive rather than agentic | **INFERENCE** — labelled on screen as *"my reading, revisable"* |
| B10 | It would be overturned by HSBC describing the coding tools in agentic terms | **SUPPORTED** — the case study states this revision condition itself (§6.3): a future disclosure could do so *without contradicting anything currently on the record* |

The film says out loud that nobody at HSBC put those two announcements side by side, and that the
pattern is the narrator's reading. **This is the single most important calibration in the film.**

## 4. The three outlets — verified directly, and it reversed the beat

| Beat | Claim | Verdict |
|---|---|---|
| B09 | Kingy AI reported the $1.8bn as a reallocation, not new money | **SUPPORTED** — read directly: *"HSBC isn't spending new money on this transformation"* |
| B09 | Metaintro gave the same $1.5bn + $0.3bn breakdown | **SUPPORTED** — read directly |
| B09 | InfotechLead put "reallocates" in the headline | **SUPPORTED** — read directly |
| B09 | There was no culprit | **SUPPORTED** — all three correct |

### CUT — the claim the film was originally built on

The case study (§6.4) states that kingy.ai and metaintro.com "independently conflated the $1.8bn
severance/restructuring figure with 'AI investment'." **Verification showed they did not.** Both
report the FY2025 reallocation accurately; kingy.ai explicitly distinguishes reallocation from new
spending.

**Verdict: CUT.** The film names all three outlets as **correct**, and the beat became stronger for
it — the danger is structural rather than anyone's error. Full record in `VERIFICATION.md`.

A film about not repeating other people's connections could not have shipped an accusation it had
taken on trust.

## 5. Claims deliberately not made

- That AI caused the headcount reduction, the application demise, or the savings
- That the four HSBC figures corroborate one another
- That HSBC's coding assistants are, or are not, agentic **as a matter of HSBC's own statement**
- That any outlet made an error
- That the $1.5bn collision is a fault of HSBC's disclosure — it is two real programmes that
  happen to be sized the same

## Summary

| Verdict | Count |
|---|---:|
| SUPPORTED | 14 |
| SUPPORTED — verbatim, primary-verified | 3 |
| QUALIFY (bound stated) | 2 |
| INFERENCE (labelled on screen) | 1 |
| CUT | 1 |

**One outstanding gap, recorded rather than hidden:** the FY2024 $1.8bn severance figure is sourced
to the case study's quotation of the FY2024 transcript, not re-read from the primary by me. Every
FY2025 figure was verified directly. If B08 is ever challenged, that is the side to check first.
