# Silent Omission Signal — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `behind-the-model/claude-liam-silent-omission-signal`).*
*Register: **Plain**. 8 beats. Source had B01-B04 rendered as Manim video
under `register: "Teardown"`, B00/B05/B06/YOURTURN/B07 left as unfilled
slates, plus 3 further unfilled BOOKEND slates (BVDT/BHTF/BOUT) never
reconciled with the earlier beats. Carry-out written first (CARRY-OUT.md,
GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a missing file gets flagged — that the agent says something's wrong. It doesn't: a skipped file is silently left out. So what actually signals that something's missing?" | Writer types "If a file's missing, my agent will flag it, right?"; "flag" hesitates and corrects to "skip" |
| B01 | 1 stakes / wrong guess | Silent omission: the agent processes what it can reach and presents the result as the whole picture. No error message. No warning. No count of files skipped. The brief is fluent and confident. The gap is invisible until something downstream uses the wrong number. | a confident-looking report card, complete with a checkmark, while faded ghost outlines of missed items sit uncounted at its edge — no alert icon anywhere |
| B02 | 3 mechanism | Agents optimize toward task completion. Tool call failures — a folder not found, a file not readable — are logged internally but not surfaced in output unless the task was explicitly designed to surface them. The completion claim is the path of least resistance. | two lanes: a small dim internal log catches a failed tool call (red X); the bold external output lane flows straight past it to "TASK COMPLETE," unaffected |
| B03 | 4 ANCHOR PLANTED | The recognition sign: the output mentions no limitations, no skipped items, no count of files processed. In a complete run, you would expect a count — eight documents found, eight processed. When the count is absent, the omission may be silent. | THE ANCHOR — two report cards side by side: an "expected" card reading 8 found / 8 processed with a checkmark; an "actual" card with the same shape but an empty outline where the count should be |
| B04 | 4 ANCHOR PAYOFF — prevention, both directions | The fix is one instruction: before the summary, produce an inventory artifact — items in scope, items processed, items skipped, items denied. Back to the eight documents: if the artifact shows six processed, that two-item gap is visible, and you can act on it before the brief goes anywhere. But a matching count doesn't prove the rest of the summary is accurate — it only proves nothing was silently dropped. And a mismatch doesn't always mean something important was lost. Either way, without the count, you can't tell which case you're in. | THE ANCHOR RETURNS — the same "actual" card's blank line fills in: 8 in scope / 6 processed / 2 skipped, the mismatch in terracotta; beside it, two claims appear and strike through: "MATCH = FULLY CORRECT" and "MISMATCH = SOMETHING IMPORTANT LOST" |
| **BCRY** | **6 carry-out** | A fluent, confident summary and a silent omission look identical from the outside — the only way to tell them apart is an inventory artifact that counts what was processed against what was in scope, and that costs one sentence in the prompt. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Before your agent writes its next summary, add this: produce an inventory artifact first — every item in scope, every item processed, every item skipped or inaccessible, with reasons. Then write the summary. Ask Claude to try it on a real agentic task, then check: does it actually stop and report when the counts don't match, or does it just note the gap and move on anyway? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Silent Omission Signal. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`behind-the-model`, Teardown metadata) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Silent Omission Signal" | unchanged |
| Facts | agent processes what it can reach, presents as complete; no error/warning/count; completion-optimization means tool-call failures stay internal; recognition sign is an absent processed-count ("eight documents found, eight processed"); fix is a required inventory artifact (scope/processed/skipped/denied) | unchanged |
| Beat count | 9 narrated array entries (B00 cold open, B01-B04 body, B05 verdict, B06 mid-handoff, YOURTURN, B07 outro), plus 3 further unfilled BOOKEND slates (BVDT/BHTF/BOUT) never reconciled | 8 (B00 writer + 4 body + BCRY + BHTF + BOUT) — source's B05 (verdict) folded into BCRY; source's B06 (mid-handoff, actionable inventory prompt) and YOURTURN (concept-audit prompt) folded into one BHTF, keeping B06's paste-ready instruction since it is the actionable one; the abandoned bookend slates are not carried forward (their content duplicates B05/YOURTURN and were never filled in the source) |
| B00 | source's B00 narration was itself a "Your turn, paste this" ask misplaced as the cold open, with no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — reframed to state the wrong guess the body falsifies (a missing file gets flagged vs. silently skipped) |
| Register | Teardown (metadata `register: "Teardown"`), though the narration itself carried no verdict on anyone's design choices beyond stating the mechanism | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | two overlapping asks (B06 actionable instruction; YOURTURN concept-audit question) | B06's actionable instruction carried into BHTF near-verbatim; YOURTURN's framing not carried (redundant with the video itself) |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — B01-B04
were already Manim video, B00/B05/B06/YOURTURN/B07 were already
`ClaudeComposerAsk`/Remotion shot types, just unfilled and under the wrong
register and skin — so the NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00 (covered by WRITER LAW anyway).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B02 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (a miss would be flagged); B03's anchor is the falsifying case (an absent count where one is expected) |
| One anchor, planted early, paid off late | B03 plants the expected 8-found/8-processed count; B04 pays it off (the same card's blank line resolves to 8/6, a visible 2-item gap) |
| Both directions | B04 — a matching count doesn't prove the rest of the summary is accurate (only that nothing was silently dropped); a mismatch doesn't always mean something important was lost |
| No design judgment | B02 describes why silence is the path of least resistance; nothing rules on whether agentic summarization is the right tool for a task |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not a malfunction.** B02 frames silent omission as the default behavior
  of a completion-optimizing agent, not a bug — the source is explicit that
  this is the path of least resistance, not a design failure to judge.
- **Not a completeness guarantee.** BCRY/B04: a matching in-scope/processed
  count proves only that nothing was silently dropped, not that the rest of
  the summary is otherwise correct.
- **Not an alarm for every mismatch.** A skipped item that didn't matter
  still shows up as a mismatch — the count makes the gap visible, it
  doesn't grade its importance.

## Handoff prompt (BHTF, read aloud)

> "Before writing the summary: produce an inventory artifact listing (1)
> every item in scope with filenames, (2) items successfully processed, (3)
> items skipped or inaccessible, with reasons. Then write the summary. If
> the in-scope count and the processed count don't match, stop and report
> the mismatch before summarizing."

Why it's worth running: it turns the reel's one-instruction fix into an
actual prompt addition, and a good test is a task with at least one
deliberately unreadable or missing file — the interesting answer is whether
the agent actually stops and reports the mismatch, or just notes the gap
and keeps going anyway.

---
**GATE P — signed:** ______________________  (human)
