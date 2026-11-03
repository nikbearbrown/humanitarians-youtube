# Two Ways to Know It's Good
### Mycroft Sprint 5 — Measure Quality

*claude-hai · Simba · target ~4:30 · 16:9 · sprint report backs this one*

---

**[B00 — INTRO]** *(pattern: `ClaudeComposerAsk`)*
> Hi, I am Simba. Through four sprints, my system could tell whether an answer was usable — not empty, not truncated, something that parses and labels correctly. It could not tell whether an answer was actually good. This week I built the two ways you can add that: a human answer key, where a right answer exists — and a stronger model's judgment, where it doesn't.

**[B01 — SUMMARY]** *(pattern: `ClaudeStatement`)*
> Usable and good are different questions. Sprint five didn't replace the checks I already had — it added a second layer on top, for the fixtures where "did it parse" was never going to tell me "was it right."

**[B02 — STRUCTURE]** *(pattern: `AutoregressiveLoop` reused as a compare-loop, or a new pairwise-judge diagram — GATE L to confirm at build time)*
> The judge is a strong model comparing two answers to the same task. But it doesn't judge once — it judges the pair twice, with the answers swapped. If the verdict flips depending on which side comes first, that's not resolved by picking one. It's recorded as inconsistent. The judge is not asked to be right. It's asked to be caught if it isn't consistent.

**[B03 — REASONING]** *(pattern: `FactStack`)*
> That swap-and-compare shape is the whole design. A verdict is a labelled model judgment, never ground truth. A dry run is the default, so nothing gets spent by accident. A cost ceiling is set up front. And every run is paced to the strong tier's per-minute limit, because a judge that gets rate-limited mid-sweep is worse than no judge.

**[B04 — RESULTS]** *(pattern: `DataTable`)*
> Fourteen comparisons, twenty-eight judging calls, twenty-eight answers generated. Ten ties. One win for the mid-tier model. Zero wins for cheap. Three inconsistent — the verdict flipped when I swapped the order. Zero answers the judge couldn't parse.

**[B05 — RESULTS]** *(pattern: `DataTable`)*
> And the cost split is the real finding here. Producing an answer: point-one-seven cents per thousand calls. Judging a pair: point-four-two. Judging costs two-point-four times what answering costs — that's the number, not a guess, and it's the reason a quality judge can never sit in the live request path.

**[B06 — REASONING]** *(pattern: `FactStack`)*
> Three of twenty-eight correct answers failed anyway — not on content, on a bracket. The model cited a full-width bracket where the validator expected a plain one. Same passage, same citation, wrong glyph. In production, each one of those is an escalation to a more expensive tier, paid for by punctuation, not by an actual mistake.

**[B07 — FINDINGS]** *(pattern: `FindingPair`)*
> That's the second bug of this exact shape — sprint four had one with quote spans. Both were invisible in the pass-fail column. Both only showed up when I actually read the raw output instead of trusting the checkmark. A green check tells you the check passed. It doesn't tell you that you looked.

**[B08 — FINDINGS]** *(pattern: `FindingPair`)*
> And the judge disagreed with itself in a specific way — never a flat swap from "A wins" to "B wins." Every inconsistent result was a tie one direction and a winner the other. The same pair, judged twice, gave three different answers across three runs on one fixture alone. One sweep is one sample. It is not a measurement.

**[B09 — SUMMARY / VERDICT]** *(pattern: `ClaudeVerdictArtifact`)*
> So: quality is measured now, not assumed. The judge works, it's honest about its own inconsistency, and it's priced — two-point-four times the cost of the answer it's grading, which rules it out of anything real-time. On the open-ended fixtures, the mid-tier model showed no measurable edge over cheap — ten ties, one win — but that's a hypothesis sitting on eight fixtures no human has checked yet, not a conclusion.

**[B10 — WHAT WENT WRONG]** *(pattern: `FactStack`)*
> The hard part of the week wasn't the judge — it was the answer key. Three straight attempts came out wrong: a prompt typed in as a field name, a fixture keyed backwards, one frozen into the manifest before I'd actually reviewed it. The interactive tool showed one field at a time with the fixture text scrolled off screen — I was labelling blind. I rebuilt it as an answer sheet: the fixture's own text inline, every change shown before it's confirmed.

**[B11 — NEXT STEPS]** *(pattern: `ClaudeComposerAsk`)*
> Your turn. If something in your pipeline passes a check, go read what it actually produced — not the checkmark, the output. Sprint six checks whether the scorer itself can be trusted. It only matters if sprint five's numbers hold up against a human looking at the same fixtures.

**[B12 — OUTRO]** *(pattern: `ClaudeTitleOutro`)*
> Mycroft Sprint 5 — Measure Quality. Simba, for Humanitarians AI.

---
## Build notes
- No new diagram components confirmed needed yet — B02's pairwise-judge swap deserves a real GATE L pass at pipeline time before defaulting to a reused pattern; `AutoregressiveLoop` is a plausible fit (two states connected, compared, looped) but it's built for decode's single-item loop, not a two-item side-by-side compare — check whether it actually reads right or whether this needs its own shape.
- Reused components elsewhere: `ClaudeComposerAsk` (B00, B11), `ClaudeStatement` (B01), `FactStack` (B03, B06, B10), `DataTable` (B04, B05 — or merge into one table beat), `FindingPair` (B07, B08), `ClaudeVerdictArtifact` (B09), `ClaudeTitleOutro` (B12).
- Source: Sprint 5 report (What the sprint was for / What was built / What was run / Results / Findings / What went wrong), as given.
