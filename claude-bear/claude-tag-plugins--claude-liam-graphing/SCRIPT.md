# Claude, Graphing. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-graphing`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumed Claude already knows how to make a good chart. Not quite — it gets told what to check, in a kit it reads before drawing. Here's what that kit actually spells out." | writer types "Claude already KNOWS how to make a good chart, right?", hesitates on KNOWS, corrects to "has to be told" — lands "Claude already has to be told how to make a good chart, right?" |
| B01 | anatomy | The kit has five primitives and three data helpers. theme sets matplotlib rcParams and returns resolved colors — foreground derives from background luminance. palette builds n colors from a base hex, a cycled list, or the series defaults. finish adds the typographic frame. save writes PNG/SVG. write_html inlines React and Recharts from a local directory — opens offline, no CDN. The three data helpers (zero_fill_days, rolling_mean, log_floor) each carry an explicit skip condition. The absolute path to graphing's scripts must go into sys.path, not a relative one. | reused `GraphingAnatomy` — primitive cards + data-helper cards |
| B02 | design | The four steps: look at the data and decide what it deserves; infer colors from context; write the script; render and look at the result before handing it over — checking legibility, overlap, distinguishable colors, and the story. Five judgement defaults with explicit permission to deviate: rotate labels only on collision, cap bar width for few categories, label bars under a dozen, rank bars unless a natural order exists, title states what the chart shows, legend only for multiple series, annotate only what matters. | reused `GraphingDesign` — four-step cards + judgement-default cards |
| **B03** | **5 both directions** | So does having this kit mean Claude always makes the right chart? Not exactly. Where the kit spells something out plainly — the first-step judgment call, colors that adapt to the background, an offline file that just works — Claude follows it and skips the mistake entirely. Where it's a placeholder string swapped by hand, or one phrase covering an edge case, Claude can still get it wrong, the same way a person skimming the same page would. | `MedhavyTwoColumnCard` — "documented plainly" vs. "easy to miss" |
| **BCRY** | **6 carry-out** | A charting kit doesn't give Claude good taste. It gives Claude judgement defaults to start from and a few sharp edges marked — and Claude only dodges the edges the kit actually marks. | the sentence, alone, serif, large — `WantQuote` |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Give Claude a dataset you've never charted before — something with a real gap in it, or no obvious color to reach for. Before it writes any chart code, ask what it's going to check in the data first, and where the colors are coming from. Then have it render the result, look at the PNG itself, and say what it would fix before handing it to you. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro series | Claude, Graphing. | `OutroSeries` — title restate |
| BCTA | outro cta | …Liam, in for Bear. | `OutroCTA` — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the same underlying facts as the source's B05/BVDT (first-step judgment call, luminance-derived colors, offline write_html, per-helper skip conditions, the absolute-path gotcha, the GRID/ACCENT literal-string trap, the four-criteria render-and-look sentence, rolling_mean's one-phrase edge behavior) as a both-directions split, not a "gets right / where it bites" verdict; the source's `GraphingTell` component and its "Verdict" `ClaudeVerdictArtifact` card are both dropped rather than reused, because their framing (and their `GETS_RIGHT`/`BITES` content) is hardcoded into the visual, not just the narration |
| Stakes → wrong guess → correction | carried entirely by B00 (WRITER LAW): the naive "Claude already knows" framing is spoken, corrected, and the corrected question is read, before any mechanism beat starts |
| Mechanism | B01–B02, reused verbatim from the source (`GraphingAnatomy`, `GraphingDesign`) — already descriptive, not evaluative, in the original narration |
| Both directions | B03 — clearly-documented defaults followed vs. thinly-documented traps still hit |
| Carry-out | BCRY compresses "defaults vs. taste, mapped vs. unmapped," not the graphing skill as a topic |
| Hedge words | none outside a flag; `one_flag` in `beat_sheet.json` metadata is N/A — every claim here is carried directly from the source Teardown's own stated facts, not an inference this build is making |

## Deliberately not claimed

- **Not "Claude never makes a bad chart once it has the skill."** B03 states
  both directions explicitly: clear defaults prevent the mistake, thin
  documentation doesn't guarantee catching it. The source's overall verdict
  is not restated — this reel describes the constraint, it doesn't grade the
  skill.
- **Not "Claude has design taste from training."** B00's correction is
  specifically that Claude is *told* what to check, by a kit it reads before
  drawing — not that it already possessed good chart judgement.
- **No invented technical specifics.** Every primitive, helper, workflow
  step, and judgement default in B01–B02 is carried verbatim from the source
  sheet's own narration and its `GraphingAnatomy`/`GraphingDesign` component
  props (already specific, not placeholders — see QUESTION.md's source-file
  check).

## Handoff prompt (BHTF, read aloud)

> "Give Claude a dataset you've never charted before — something with a real
> gap in it, or no obvious color to reach for. Before it writes any chart
> code, ask what it's going to check in the data first, and where the colors
> are coming from. Then have it render the result, look at the PNG itself,
> and say what it would fix before handing it to you."

Why it's worth running: it turns the reel's central distinction into
something checkable on any dataset, not just the source's examples — and the
check (did it actually look at what it rendered?) is the same
defaults-vs-taste test B00 opened with.

---
**GATE P — signed:** ______________________  (human)
