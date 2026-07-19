# FACTCHECK — vox-silent-join

Source of record: `books/computational-skepticism-for-ai/chapters/05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md` ("The clean dataset that destroyed a deployment").

## The case — TREAT AS TEACHING ANECDOTE, NOT NEWS

The chapter's opening story (a deployment team, three source systems, a 4% join drop concentrated in one subpopulation) names no company, no domain, no dataset, and carries no citation. **Status: composite teaching case.** The film honors this: no company, industry, or dataset is named or implied on any plate; B02's report page is anonymous by design. If the underlying incident is ever pinned to a real deployment, revisit and add the citation here.

## Claims carried into the film

| Beat | Claim | Verdict | Basis |
|---|---|---|---|
| B01–B03 | spotless EDA, clean missing-values check, failures blamed on the model | ✓ anecdote | Chapter ¶2–4, faithfully compressed. "Missing values: none — technically true" is the film's framing of the chapter's point (the check WAS clean; that's the trap). |
| B04 | "assembled from three source systems, joined on a shared identifier" | ✓ anecdote | Chapter, verbatim in substance. Join-type taxonomy excluded per card. |
| B05 | "a four percent drop rate… silently excluded" | ✓ anecdote | Chapter: "The join had a four-percent drop rate — rows that didn't match across all three sources got silently excluded." |
| B06 | drop concentrated in one subpopulation (identifier formatting quirk, years old, one system) | ✓ anecdote | Chapter, faithfully compressed. |
| B07–B08 | "performed beautifully on what was present… failed on exactly them, predictably" | ✓ anecdote | Chapter: "performed beautifully on what was present. Deployed against the full population, it performed predictably worse on the subpopulation it had never seen." |
| B09 | "you cannot compute the missingness of rows that never existed" | ✓ | Chapter's own line, near-verbatim — the film's thesis quote. |
| B10 | "one question would have caught it in the first hour: why are there exactly N rows?" | ✓ | Chapter: "That single question, taken seriously, would have surfaced this entire failure mode in the first hour." |

## The scale model — internal arithmetic

The film renders the anecdote at a countable 100-row scale:
- 100 candidate rows → 96 merged + 4 dropped = **4% drop** ✓ exact.
- Subpopulation: 10 of 100 rows; drops: 3 subpopulation + 1 majority. Disproportion: 3/10 = 30% of the subpopulation lost vs 1/90 ≈ 1.1% of the majority — a ~27× relative risk. "The falling rows were almost all theirs" (3 of 4) ✓ and "disproportionately failed the join" ✓ both honest at this scale.
- B07: the merged grid must show exactly 7 remaining terracotta rows (10 − 3). B08's deployment sample (9 ink + 3 terracotta) is a fresh production draw, not the training rows — the sample's terracotta share (25%) is illustrative of "meeting the full population," not a population estimate; no rate is printed on it.

## Exclusions honored

No SQL join taxonomy (the word "join" appears; inner/left/outer never do) · no MCAR/MAR/MNAR terms · no six-step interrogation procedure (only THE one question, B10) · no imputation methods.

## Rendering honesty checks

- Countable-true: 100 queue, 96 land, 4 fall — freeze-frame counting must match. Fixed seed if any scatter is used.
- The subpopulation's terracotta rows are visible from B05's queue onward — the viewer can see the group existed BEFORE the drop; revealing the color only at B06 would be a cheat.
- The 4 fallen rows leave the frame silently — no error icon, no sound-effect visual; the silence is the point.
- B07's blue ticks land ONLY on present rows; nothing marks the absent ones — absence must look like nothing, exactly as it did to the EDA.
- B10's ledger (expected 100 / received 96) uses the film's scale consistently; "N" in the headline question stays abstract.
- No green anywhere (blue = success per the film's palette); no company or product on any plate; B02 synthetic — disclosure in credits.

## Chapter errata

None — the anecdote is internally consistent and clearly framed as a case the author is recounting; its unnamed status is preserved rather than laundered into fact.
