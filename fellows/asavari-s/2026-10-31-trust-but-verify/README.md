# Trust, but Verify

**Fellow:** Asavari (Ash) Shejwal &nbsp;·&nbsp; **Track:** Mycroft — SEC Filings Financial Metrics Agent &nbsp;·&nbsp; **Date:** 2026-10-31

How an accuracy benchmark moved the SEC Filings Financial Metrics Agent from SPECIFIED toward VERIFIED. Scaling the independently-sourced golden set from 2 companies to 10 caught three real extraction bugs that were invisible at two — XBRL tag migration across years, a ticker resolving to an empty shell entity, and filers with no aggregate total-liabilities tag. After the fixes: 46 of 46 values match within a 0.5% relative tolerance across 10 companies.

**Formats:** 16:9 (3840×2160) and 9:16 (2160×3840) — both rendered and checked.
**YouTube:** _pending upload_
**Video source:** [`beat_sheet.json`](beat_sheet.json) — the official Brutalist source. Rendered through the brutalist.art runtime (Remotion beats + Kokoro `af_bella` narration); the 9:16 is a portrait re-render via the `916` compositions, not a crop.
**Code:** [nikbearbrown/mycroft PR #13](https://github.com/nikbearbrown/mycroft/pull/13)

## Beats
1. **B00G** — greeting bookend
2. **B00** — open: it passes on two companies — is it actually correct?
3. **B01B** — executive summary ("Hi, I'm Asavari … this video is about …")
4. **B01** — the problem: two passing companies prove almost nothing
5. **B02** — the mechanism: an independent golden set, scored for coverage and accuracy (0.5%)
6. **B03** — the findings: three real bugs caught by scaling 2 → 10 companies
7. **B04** — the verdict: 46/46 earns trust only because the test can fail
8. **B05** — outro

## Related
[Ticker to Truth](../2026-09-28-ticker-to-truth/) · [PASS / FAIL / UNKNOWN](../2026-08-14-pass-fail-unknown/) · [One Number, Many Names](../2026-08-14-one-number-many-names/)
