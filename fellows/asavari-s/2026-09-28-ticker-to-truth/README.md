# Ticker to Truth

**Fellow:** Asavari (Ash) Shejwal &nbsp;·&nbsp; **Track:** Mycroft — SEC Filings Financial Metrics Agent &nbsp;·&nbsp; **Date:** 2026-09-28

An end-to-end overview of the SEC Filings Financial Metrics Agent: how a ticker becomes verified financial metrics in five deterministic steps — resolve (ticker → CIK), fetch official XBRL from EDGAR, normalize concepts by explicit tag mapping, derive ratios/margins/growth keyed to the reporting period, and validate (PASS/FAIL/UNKNOWN) with provenance. The through-line for the three deep-dive Mycroft videos; shows why there is no LLM in the critical path.

**Formats:** 16:9 (3840×2160) and 9:16 (2160×3840) — both rendered and checked.
**YouTube:** _pending upload_
**Video source:** [`beat_sheet.json`](beat_sheet.json) — the official Brutalist source. Rendered through the brutalist.art runtime (Remotion beats + Kokoro `af_bella` narration); the 9:16 is a portrait re-render via the `916` compositions, not a crop.
**Rendered masters** (git-ignored, per house convention — published to YouTube, not committed):
- `ticker-to-truth.mp4` (16:9)
- `short/ticker-to-truth-short.mp4` (9:16)

## Beats
1. **B00G** — greeting bookend
2. **B00** — open: ticker in, trusted financials out — what happens in between?
3. **B01B** — executive summary ("Hi, I'm Asavari … this video is about …")
4. **B01** — steps 1–2: resolve (ticker → CIK), fetch official XBRL from EDGAR
5. **B02** — step 3: normalize concepts — map to us-gaap tags, record the match, MISSING never guessed
6. **B03** — steps 4–5: derive metrics by period; validate PASS/FAIL/UNKNOWN with provenance
7. **B04** — the verdict: ticker to truth, deterministically — no LLM in the critical path
8. **B05** — outro

## Related
Deep dives on individual steps: [Same Number, Two Ways](../2026-08-14-same-number-two-ways/) · [One Number, Many Names](../2026-08-14-one-number-many-names/) · [PASS / FAIL / UNKNOWN](../2026-08-14-pass-fail-unknown/)
