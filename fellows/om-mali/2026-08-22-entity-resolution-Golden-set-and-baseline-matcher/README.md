# 2026-08-22 - Building a golden set and a baseline name matcher

**Week covered:** 2026-08-17 - 2026-08-23

**Video:** [Mycroft_OmMali_22_08_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

That only works if you can tell which filings refer to the same company, and
the filings do not make that easy: **Databricks appears under 51 different
spellings, and nothing in the filing says they are the same company.**

- **A hand-labelled answer key of 322 company names was built**, covering 7,276
  holdings, with the evidence for each label recorded so any row can be
  re-checked.
- **The matcher scores 99.6% precision and 100% recall** against that key —
  meaning it almost never claims a company wrongly, and does not miss any.
- **One missing dot was hiding 85 holdings.** The search pattern for "X.AI"
  never matched filings that write it as "XAI", and the fund affected is the
  company's largest holder.
- **Two companies were identified by price rather than by name.** A holding
  filed under a British software company's name is priced to ten significant
  figures identically to confirmed holdings of Anthropic.
- **There is no single cut-off that separates right from wrong.** A wrong match
  and three correct ones score exactly the same, so anything in that range is
  sent to a person instead of being guessed — which is a small, bounded amount
  of human attention.
- **A review overturned one of the project's own labels**, and because the
  original approval had been given on an inaccurate summary of the evidence, it
  is recorded as withdrawn rather than quietly updated.

## Files

| File | What it is |
|---|---|
| `narration_script.md` | The script, with shot directions and delivery notes |
| `images/w4-*.png` | The four figures, 2917 × 1750 |
| `images/w4-*.svg` | Vector sources, if anything needs re-typesetting |
| `figdata_week4.json` | Every number in every figure, as queried |

## Figures, in script order

| Beat | Figure | Shows |
|---|---|---|
| 0:18 | `w4-spellings` | Seven companies wearing 128 distinct name spellings; Databricks alone has 51 |
| 0:42 | `w4-scoreboard` | The two systems on precision and recall, then the dot that hid 85 holdings |
| 1:08 | `w4-reversal` | Five holdings filed as `OpenAir.com, Series C`, all at OpenAI's Series C price |
| 1:38 | `w4-tie` | Four holdings at identical confidence — one wrong, three right |

## Numbers on screen

Every figure is generated from a script that queries the built data at render time and writes
`figdata_week4.json` before drawing. No number is typed into a chart by hand, so a figure
cannot drift from the result it describes.

| Claim | Value |
|---|---|
| Distinct issuer names in the source data | 3,204,853 |
| Distinct spellings, seven universe companies | 128 |
| Labelled issuer names in the ground truth set | 322, covering 7,276 holdings |
| Simple name patterns — precision / recall | 0.9916 / 0.9792 |
| Deterministic matcher — precision / recall | 0.9959 / 1.0000 |
| Holdings recovered by fixing one dot | 85 |
| `OpenAir.com` price, and OpenAI's Series C consensus | 687.6869 both |
| Holdings tied at confidence 0.80 | 4 — one wrong, three right |

## Three things the script is careful about

These are deliberate and should survive editing.

1. **It does not claim a precision win.** On the hardest cases the older, simpler patterns are
   actually cleaner — the new matcher wrongly claims a used-car marketplace whose name contains
   the words "open" and "AI". The honest claim is recall: 85 holdings recovered.
2. **It publishes the worse number next to the better one.** The matcher reaches 1.0000 recall
   only after a fix that this ground truth set prompted. A score measured after fixing what the
   test caught is not a validation, and the script says so.
3. **It does not oversell the ground truth.** 8 of the 322 labels have been reviewed by a
   person. The other 314 are the machine's own work — and one of those 8 turned out wrong,
   which is the reason the video's middle section exists.

## Provenance

Source data: SEC Form N-PORT bulk data sets, 2023Q1–2026Q2, Level 3 holdings only.
Figures follow the repository's `brutalist/DESIGN.md` palette and type stack; both required QA
passes were run — the deterministic layout audit reports zero errors on all four, and each PNG
was read for substance afterwards. That second pass is what caught two real problems the audit
could not: a clipped axis label, and a chart captioned "seven companies" that was actually
showing five universe companies and two watchlisted ones.

---

## The built reel (added by the video build, 2026-08-23)

This README's figure table describes the four SOURCE figures and the script's four body
sections. The reel as built has **12 beats**: the four script sections were split into eight
body beats so no beat carries two ideas, wrapped in the four standard Claude bookends.

- `beat_sheet.json` — the authoritative beat list, and the build record
- `BUILD-LOG.md` — every decision, including the three script splits and the wording changes
- `FACTCHECK.md` — 20 rows; read 2, 12 and 16
- `PEDAGOGY.md` — GATE P
- The four source figures now live in `pantry/` (with their SVGs), not `images/` — the toolkit
  writes compile output into `images/`.
