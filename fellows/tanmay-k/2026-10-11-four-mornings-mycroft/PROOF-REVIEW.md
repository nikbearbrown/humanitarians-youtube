# Feedback: "Four Mornings" (working title) — Tanmay Kulkarni, Week 26 work video

**Stage:** script, draft 1 (2026-10-10). No beat sheet, components or audio yet. Reviewed from `SCRIPT.md` and
`FACTCHECK.md`. The production gate is checked as **intent**: what each claim beat will show. It is re-checked on
rendered frames later.

**Verdict:** **cleared for Gate P.** Teaching **11/12** (draft). Production gate: PASS as intent, after two pre-production
fixes applied below.

## Rubric

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 2 | B01 names the idea (hand-offs: one part taking another's word for it) and puts the strip of four hand-offs on screen before any morning |
| Reusable rubric | 2 | One question, applied four times: what is it taking on trust, and what would say so if it slipped. B09 hands it to the viewer |
| Worked example | 2 | Each morning walks one hand-off: what slips, what the reader would see, which step now speaks up, with its record |
| Falsifiability / edge | 2 | B07: my own check passed when it should have failed, and how it was fixed; B08: the trusts that remain (live prices, open steps) |
| Active task | **1** | B09 is a real question, but it gives no scaffold (no strong vs weak answer). Optional fix: one line such as "a good answer names the hand-off and the thing that would say so; 'it's always been right' doesn't count" |
| Friction | 2 | B03: the zero price is kept faithfully *and* flagged. The viewer has to hold "the math is right" against "the reader doesn't know" |

## Production gate (intent)

| Check | Result |
|---|---|
| Sources on screen | Every claim beat names a committed file in its evidence panel (`FACTCHECK.md` W1–W19). **Fixed:** B04 voiced the original's error with no artifact on screen; it now shows the two lines of Calculate Metrics with their source. B02 now shows the README quote it paraphrases |
| Evidence at the moment of assertion | To be set with cues once audio exists. Each morning's evidence panel must be up while its claim is spoken |
| Side-by-side | B05: both portfolio copies held side by side while "fifty becomes fifty-five"; B07: the struck "pass" next to the catch |
| Invented numbers labelled | The dashboard carries "Illustration · invented prices" in every beat it appears (B01, B03–B08) |

## Boundaries checked

- **W25 (porting, parity, rounding):** none of them is a beat or a thesis. The only trace is "down to a single cent" in
  B07, as evidence the fixed test bites.
- **No critique:** the zero price and the two copies are "how the workflow works"; the recipe leaves them to the
  maintainers. The only mistake named is mine (B07).
- **Committed files only:** no guard, no fixture builder, nothing from the session.

---

# Review 2: script draft 2, before the beat sheet (2026-10-10)

**Verdict: cleared to build the beat sheet.** Teaching **12/12**. Production gate PASS as intent. One join defect was found
by the straight-through read and fixed; it needs a one-sentence Gate P re-read (B02) before audio.

## Read-through (PLAYBOOK §1e): the joins

| Join | Finding | Action |
|---|---|---|
| B02 → B03, B07 | B03 "I kept that behaviour exactly" and B07 "I broke my own calculation" presume I rebuilt the math step; B02 said only "added checks to both". A first-time viewer would ask *whose* calculation | **[EDIT]** B02 now says "…added checks to both, and rebuilt the math step so it runs on test data." FACTCHECK W3 extended (step 5 script). Logged in PEDAGOGY; re-read needed |
| B01 → B03 | B01's total (65,098) already includes META at its previous close, the very thing morning one reveals. That's a payoff, not a contradiction: the "finished" number in the cold open was already carrying a quiet fallback | keep; B03's dashboard should highlight the same META row the viewer saw in B01 |
| B03 → B08 | B08 says "four hand-offs that now speak up". Morning one speaks up through the record (`price_source`), not by stopping. "Speak up" covers both | keep the wording; B08's strip shows hand-off 1 as "recorded" and 2–4 as "stops" |
| B07 | The only first-person mistake; it lands as evidence (what it caught, the fix), not a confession | keep |
| B09 | The new line gives the closing question a strong and a weak answer | keep |

## Rubric

| Criterion | Draft 1 | Draft 2 | Why |
|---|---|---|---|
| Explicit framework | 2 | 2 | Hand-offs named and shown as a four-part strip in B01, before any morning |
| Reusable rubric | 2 | 2 | "What is it taking on trust; what would say so?" applied four times, then handed over |
| Worked example | 2 | 2 | Each morning: the slip, what the reader sees, the step that speaks up, its record |
| Falsifiability / edge | 2 | 2 | B07 (a check that couldn't fail) and B08 (trusts that remain) |
| Active task | 1 | **2** | B09 now has a strong answer ("names the hand-off, and the thing that would say so") and a weak one ("it's always been right") |
| Friction | 2 | 2 | B03: faithful *and* flagged; "the math is right" against "the reader doesn't know" |

**12/12.**

## Production gate (intent), for the beat sheet to honour

1. **Every claim beat carries an evidence panel** naming its committed file, up from the moment its claim is spoken
   (cues on the measured clock once audio exists).
2. **"Illustration · invented prices"** on the dashboard in every beat it appears.
3. **Side-by-side held:** B05's two portfolio copies, B07's struck "pass" beside the catch.
4. **No W25 material:** no rounding or parity panel, except B07's one-cent catch, shown as the self-test row.

---

# Stills stage (2026-10-10): self-QC before review

20 stills (10 beats × 16:9 and 9:16) from `MorningDashboard` (new, in `brutalist.art`, registered, `tsc` exit 0), the
card and the outro, each at the evidence reveal + 1.6 s (planning clock).

**Fixed before review:**
- **A wrong digit.** The NVDA row showed 25,228.12. The merged file holds 25,228.125, which JavaScript's `toFixed`
  (what the workflow uses) shows as .13. The display formatting was Python's. `money()` now rounds like JavaScript,
  so the illustration can't round differently from the system it illustrates.
- **Text too small in 16:9, with the bottom third empty.** The landscape type scale went up about 30%.
- **The outro under-filled the frame:** Gate V gave B10 43% against a 55% minimum, with the title "Four mornings.".
  The card title is now "Four mornings, one dashboard."; the spoken line is unchanged.

**Checks:**
- Gate V on all ten 16:9 stills: 0 BLOCKER / 0 MAJOR.
- Portrait pixel gate: 9/10 pass. B02's card fails the Shorts zones (the known shared-card limit), so the Short
  uses `MorningDashboard` only (option a, as in the topic video).
