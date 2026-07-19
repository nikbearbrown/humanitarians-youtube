# FACTCHECK — vox-fluency-trap

Source of record: `books/the-reallocation-engine/chapters/01-the-fluency-trap.md`
Primary sources, both fetched and verified 2026-07-06:
- Shen, J.H. & Tamkin, A., "How AI Impacts Skill Formation," arXiv:2601.20245 (v1 Jan 28 2026, v2 Feb 1 2026, CC BY-NC-ND 4.0)
- Anthropic research post, "How AI assistance impacts the formation of coding skills," Jan 29 2026 (anthropic.com/research/AI-assistance-coding-skills)

## Core claims — verdicts

| Beat | Claim | Verdict | Source / derivation |
|---|---|---|---|
| B01 | "Two groups of engineers. The same problem, the same clock." | ✓ (after fix) | RCT, same task and time window across arms. **Original narration said "the same hour" and "with the same tool" — both WRONG, fixed 2026-07-06.** Task window was ~35–40 min (blog: 11 min = "30% of the total time allotted"), and the arms had *different* tooling. Regenerate B01 audio. |
| B01/title | "two letter grades dumber — and feeling smarter" / "was sure it learned more" | flourish, labeled | "Nearly two letter grades" is Anthropic's own phrasing (17-pt gap, d=0.738, p=0.01). "Feeling smarter / sure it learned more" is an editorial characterization, NOT a measured outcome — the study did not report perceived-learning or confidence. Defense: the delegation cluster finished fastest with "few or no errors" (blog), i.e. zero felt signal of the deficit; adjacent lit (Lee et al. 2025 survey) supports reduced engagement. Keep as thesis-frame or soften to "and never felt it happen" — Bear's call at the gate. |
| B02 | "A research lab took a group of junior engineers… a Python library none of them had ever seen" | ✓ | 52 mostly-junior engineers, ≥1 yr weekly Python, screened unfamiliar with Trio. "Research lab" = Anthropic (deliberately unnamed on screen; see rendering notes). |
| B03 | "Half got an AI assistant. Half had to write every line by hand." | minor | Arms confirmed (AI sidebar vs no AI). Exact group sizes not in the blog; "half" assumes ~26/26. **Check Table 1 (Balance Table) in the paper v2 before ship**; if unequal, reword to "one group… the other." |
| B03 | "exactly one difference: who did the typing" | ✓ | Chapter's framing of the randomized manipulation; fair for an RCT. |
| B04 | "The AI group finished clean… looked like competence" | ✓ | Blog: No-AI group encountered more errors; delegation cluster had "few or no errors" and finished fastest. AI group ~2 min faster on average (n.s.). |
| B05 | Quiz card: "Do you understand what the code does?" — "14-question comprehension quiz" | ✓ / paraphrase, labeled | The question is the FILM'S OWN paraphrase of the eval's purpose (debugging, code reading, conceptual — per blog), not a quotation from any document. 14 questions per chapter footnote — **spot-check the count in the paper.** See rendering notes. |
| B06 | 67% vs 50%, "seventeen points — nearly two letter grades — … one short session" | ✓ (after fix) | Blog verbatim: AI group 50%, hand-coding 67%, "equivalent of nearly two letter grades" (d=0.738, p=0.01). 67−50=17 ✓. **Original said "in a single hour with the same tool" — WRONG twice, fixed. Regenerate B06 audio.** |
| B07 | "the AI group felt fine… Nothing had failed. The trap never looks like failure." | flourish, defended | Delegation cluster: fastest, few/no errors — no failure signal existed. Chapter: "It feels like productivity because the artifact appears and it runs." |
| B08 | "understanding forms while it gets checked — read, tested, questioned, broken, fixed" | ✓ interpretation | Blog: high scorers used AI "to build comprehension" (follow-ups, explanations, conceptual queries); control likely improved debugging "through resolving these errors independently"; conclusion: "Cognitive effort—and even getting painfully stuck—is likely important for fostering mastery." |
| B09 | interrogators "landed right beside the hand-coders" | ✓ | The convergence claim — chapter fig 1.2's explicit design ("Hand-coding and AI-plus-interrogation sit at nearly the same height, joined by a faint reference line"). Engaged-usage range 65–86% straddles the hand-coders' 67; chapter: "Take a group that gets that same understanding some other way — and the gap closes." Blog: all three engaged clusters averaged ≥65%. Graphic renders the reference line at 67 crossing the band — the convergence is drawn, not asserted. **Narration revised twice; regenerate B09 audio.** |
| B10 | delegators "scored in the twenties and thirties" | ✓ | Chapter/paper: delegation-usage range 24–39%. Blog: low-scoring clusters <40% avg. |
| B10 | "Same tool. Same task. Opposite result." | ✓ | TRUE here (within the AI arm — everyone had the assistant). This is the only place "same tool" belongs; that's why it was cut from B01. |
| B11–B12 | "comprehension debt… compounds… comes due… with interest" | chapter's named concept, labeled | The chapter's coined mechanism (its central metaphor), consistent with the blog's "productivity benefits may come at the cost of skills necessary to validate AI-written code." Film renders it as metaphor (unscaled meter, no fake numbers) — honest. |
| B13 | "The machine is a better typist than you will ever be… the checking was never the machine's job" | ✓ | Chapter: "the machine is a superb typist — faster and more accurate at producing syntax than any human." Closing line is the chapter's thesis. |

## Simplification defended: two registers, not six clusters

The paper identifies SIX interaction patterns; the film compresses to interrogate-vs-delegate. Defense: Anthropic's own top-line split is high-scoring (≥65%: generation-then-comprehension, hybrid code-explanation, conceptual inquiry — all "build comprehension") vs low-scoring (<40%: delegation, progressive reliance, iterative AI debugging — all "cognitive offloading"). The binary is the source's binary; the chapter uses it too. Do NOT add the six clusters to the film (card exclusion territory).

## Exclusions honored (from the candidate card)

No n=52 or randomization mechanics on screen (B03 grid shows NO counts) · no boost/drag terminology · no IBM story · no OPT clock. Also honored: no Cohen's d / p-value on screen — FACTCHECK carries the statistics so the film doesn't have to.

## Rendering honesty checks

- B03 `IsotypeSplitGroups`: equal halves only if Table 1 confirms ~26/26; otherwise proportional. Never print a headcount.
- B05 quote card: typeset as the film's own question card (charcoal serif on newsprint), NOT as a facsimile document — it is a paraphrase, and the attribution line "14-question comprehension quiz" must stay descriptive, not citational.
- B06 `BarCompare`: zero-baseline bars, 67 and 50 as printed values; the "17 points" bracket spans the actual gap — no axis truncation to exaggerate.
- B09/B10 `ThreeColumnConverge` (chapter fig 1.2): one persistent chart — solid 67 bar (hand), band 65–86 (interrogation, RANGE not average), band 24–39 (delegation). The dashed reference line at 67 must visibly cross the interrogation band (the convergence IS the claim); the gold sweep in B10 highlights the empty 39–65 band in the delegation column — real and honest. The two high columns are both BLUE (they share the checking behavior); only delegation is terracotta. Never render this as "hand vs AI" — the chapter explicitly calls that the wrong lesson.
- B11 `DebtLedgerStack`: unscaled meter, no invented numbers — it must read as metaphor, not measurement.
- All `ai`-source plates (B04, B07, B12): synthetic — disclosure line required in the credits block.
- No real person is depicted; Anthropic is never named on screen (narration says "a research lab"); the credits block cites the paper properly.

## Chapter errata (feed back to the book, not the film)

- Chapter dates the study "Feb 3 2026" — actual: arXiv v1 Jan 28 2026, blog Jan 29 2026 (v2 Feb 1). Fix footnote [^01-anthropic].
- Chapter implies "the same hour"; blog arithmetic gives a ~35–40 min allotted window. Soften to "the same session" wherever the chapter states a duration.

## Regenerate before render

Narration changed post-audio for **B01, B06, B09** — their mp3s are stale:
`python3 scripts/generate_audio.py reels/vox-fluency-trap --only B01 B06 B09`
