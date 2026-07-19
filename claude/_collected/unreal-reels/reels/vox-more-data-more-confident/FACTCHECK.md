# FACTCHECK — vox-more-data-more-confident

Source of record: `books/computational-skepticism-for-ai/chapters/03-bias-where-it-enters-and-who-is-responsible.md` (the estimator-bias definition and the Literary Digest passage).
History independently verified 2026-07-06 via web search; the statistical mechanism is verified by construction (the dart model is the chapter's fig 3.1 in motion).

## The Literary Digest claims — all verified

| Beat | Claim | Verdict | Source / derivation |
|---|---|---|---|
| B01/B02 | "biggest poll in American history — 2.4 million responses" | ✓ | 10 million ballot-questionnaires mailed; ~2.38–2.4 million returned — the largest poll conducted to that point. Chapter says the same. |
| B02 | "mails out ten million ballots… calls the election for Alf Landon" | ✓ | Digest's Oct 31, 1936 issue: Landon 57.08%, 370 electoral votes. |
| B03 | "Roosevelt then won forty-six of the forty-eight states" | ✓ | FDR carried every state except Maine and Vermont (523–8 EV), ~61% of the popular vote. |
| B07 | "its ballots went to people with cars and telephones — in 1936, the comfortable" | ✓ with a scholarly footnote | The mailing frame was auto registrations and telephone directories — the standard account. Scholarship (Squire 1988, "President Landon and the 1936 Literary Digest Poll") adds that NONRESPONSE bias (who mailed back) contributed as much as the frame. The film's one-line cause is the frame; the deeper decomposition belongs to the book, not a 100-second film. If Bear wants it airtight, the line could read "went to — and came back from — the comfortable," which covers both mechanisms in one word. |
| B11 | "the Literary Digest folded within two years" | ✓ | Credibility destroyed; folded within 18 months of the election; ceased publication 1938. |

## The mechanism — verified by construction

| Beat | Claim | Verdict | Basis |
|---|---|---|---|
| B05 | "the truth is a point; every poll is a dart thrown at it" | ✓ model, labeled | The chapter's estimator frame: θ is the true quantity, θ̂ one computed estimate. Standard statistical pedagogy (accuracy/precision target diagram); the chapter's own fig 3.1 caption: "More data narrows the scatter. It does not move the systematic offset." |
| B06 | "an unbiased poll… big samples tighten… more data really does mean closer" | ✓ | Law of large numbers for an unbiased estimator — variance shrinks with n, centered on θ. The film grants the instinct its truth before breaking it. |
| B08 | "the scatter tightens… around the wrong point… tiny, precise, supremely confident cluster, off-center" | ✓ | Chapter, verbatim in substance: "A biased estimator converges, with more data, to the wrong answer — with increasing confidence." Variance → 0 while E[θ̂] − θ stays fixed. |
| B09 | "that distance has a name" — the single label "the bias" | ✓ | Bias(θ̂) = E[θ̂] − θ. Card allows exactly one plain-language label and no notation — honored. |
| B10 | "precision is how tightly the darts cluster; truth is where" | ✓ | The accuracy-vs-precision distinction, stated without the jargon pair. |
| B11 | "more data shrinks your error bars; it does not shrink your blind spot" | ✓ | Restatement of the chapter's thesis line. |

## Exclusions honored (from the candidate card)

No bias-variance decomposition (variance is shown, never named) · exactly one "the bias" label, no E[θ̂] notation anywhere · no ten-mechanism taxonomy (selection bias is never even named — the film shows the mechanism instead) · Literary Digest history = the hook (B02–B03) + one causal line (B07), nothing more · no second historical example.

## Rendering honesty checks

- B06 vs B08 must use the SAME wave structure and the same spread-shrink schedule — the only difference between the honest poll and the Digest is the aim-point. If the animations differ in anything but center, the comparison lies.
- Seeded scatter (fixed rng) — renders reproducible; the clusters are actual Gaussian samples, not hand-placed dots.
- B08's counter (100 → 10,000 → 2,400,000) is the real n-story; the dart COUNT on screen stays in the dozens — the counter carries the magnitude, the darts carry the shape. Never imply the screen shows 2.4M marks.
- B08/B09: the truth dot must remain visible and unmoved throughout — the cluster tightens, the truth never migrates.
- B09: "the bias" label sits clear of the dumbbell line (no text-on-line); the ring is the film's single HandRing.
- B10: both mini-targets identical in size and ring structure; only cluster location and spread differ.
- B02 archive plate: 1936 U.S. press is public domain; sidecar (`B02.source.txt`) still required — STAND-IN X until it exists. B03 derives from B02.
- No candidate portraits, no party colors — the blue/terracotta here are the film's semantic pair (truth/bias), not red/blue politics. The target is abstract; no percentages on it.

## Chapter errata

None — the chapter's Literary Digest line and estimator claim both check out. Optional enrichment: the chapter could cite Squire (1988) for the nonresponse-bias component; its current phrasing ("the bias was structural") is compatible with both mechanisms.

Sources: [Squire — "President" Landon and the 1936 Literary Digest Poll (Cambridge)](https://www.cambridge.org/core/journals/social-science-history/article/president-landon-and-the-1936-literary-digest-poll/E360C38884D77AA8D71555E7AB6B822C) · [Wikipedia — 1936 United States presidential election](https://en.wikipedia.org/wiki/1936_United_States_presidential_election) · [Wikipedia — The Literary Digest](https://en.wikipedia.org/wiki/The_Literary_Digest) · [UPenn math — 1936 election case study](https://www2.math.upenn.edu/~deturck/m170/wk4/lecture/case1.html)
