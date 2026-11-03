# FRICTIONAL — AAA to D: Rating Mycroft's Risk Score

- **Folder:** `2026-08-03-risk-management-explanation` · reporting week **2026-08-03 → 2026-08-09**
- **Dates inside this folder's artifacts:** `PEDAGOGY.md` audit 2026-07-26 · `beat_sheet.json` 2026-07-27
  (the folder was previously named `2026-07-26-…`; re-dated for the renewal index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-08-03 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A `cli-explainer` reel on the credit-rating change I made to Mycroft's Risk Management
  Agent: Mycroft PR #16, `format-report.js` / `test-format-report.js` (score → AAA…D rating).

**2. What I tried, and what I expected**
- Built the beat sheet around the real PR diff: B03 shows `scoreToRating()` verbatim,
  B06 shows the `camelCaseReport` return block, B04/B07 are Manim output scenes.
- Expected it to fit under the 3:00 cap — the sheet estimated 168 s (2:48) before audio.

**3. Where it resisted, and what I did next**
- At the GATE P audit (2026-07-26) the two Manim scenes (`B04_RatingSweep`,
  `B07_AdditiveMerge`) did not exist yet; they were authored afterwards in `scenes.py`.
- The revision cycle had to be a real one, not a staged bug. The real tension was in the
  test file: the RiskLog Google Sheet auto-maps the 14 original keys, so the rating could
  not be added by reshaping the report — it had to be nested (14 original + 15 camelCase keys).
- The corner logo mark was left unset because the default mark belongs to another channel.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude (Sonnet 5) wrote the GATE P pedagogy audit and drafted the beat sheet from the PR diff.
- Changed on my instruction: dropped the `@NikBearBrown` identity and "in for Bear" sign-off;
  the reel signs off as Mohammed Hussain.
- I signed GATE P (confirmed 2026-10-28). `PEDAGOGY.md` itself still reads "awaiting your sign-off" — the signature was not written back into the file.

**5. What I understand now, and what I still do not**
- Understood: an additive, nested output is how you add a field without breaking a
  downstream consumer that maps keys by name — and the test that locks the key lists is
  what makes that promise enforceable.
- Open: there is no QC report or measured runtime in this folder, so I cannot show from
  these files alone that the final render passed visual QC.

**Evidence in this folder**
- [`PEDAGOGY.md` — GATE P audit, 2026-07-26](PEDAGOGY.md)
- [`beat_sheet.json` — the reel, 2026-07-27](beat_sheet.json)
- [`scenes.py` — B04 rating sweep, B07 additive merge](scenes.py)
