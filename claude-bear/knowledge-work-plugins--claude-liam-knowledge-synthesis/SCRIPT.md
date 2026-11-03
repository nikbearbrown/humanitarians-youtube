# Combine, Don't Pick — Narration Script (redo, GATE P)

*Skill: `hai-simple` (redo mode). Register: **Plain**. 7 beats ≈ 1:50.*
*Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-knowledge-synthesis`
(Teardown, 7 beats: B00 composer-ask, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro). Question, facts, and body
argument carried over unchanged (QUESTION.md); carry-out written first
(CARRY-OUT.md).*

**Narrator:** Liam, Kokoro `am_onyx`. **Cold open:** `BrutalistHesitantWriter`
(no puppet host in hai-simple).

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | 1 stakes + 2 wrong guess | "Give Claude a handful of search results, and you might think it just picks the one best result and stops there. It doesn't pick — it combines. So: does Claude just combine the best sources?" | BrutalistHesitantWriter — types "Does Claude just pick the best source?", corrects "pick"→"combine" and "source"→"sources" |
| NB01 | 3 mechanism | A skill is a folder Claude reads before it works. This one is knowledge-synthesis, one job: turn scattered search results into a single answer. SKILL.md lays out the work as steps, run in order — gather, then combine. Linear, unless a step says otherwise. | chip row: SKILL.md → steps → in order |
| NB02 | 3 mechanism | What combining actually means: overlapping results don't get stacked end to end. Repeated claims merge into one, duplicates drop, and every surviving claim keeps a record of which source it came from. | chip row: overlap → one claim → source kept |
| NB03 | 3 mechanism | When sources disagree, the skill doesn't average — it weighs each claim by freshness and authority, and the higher-weighted claim wins. Same sources in, same answer out, every run. | chip row: freshness / authority / same answer |
| **BCRY** | **6 carry-out** | The skill never picks a winning source — it combines every one of them, weighed by how fresh and how authoritative each is, and it always tells you which source each claim came from. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads the paste-ready prompt, then discusses what to check in the reply] | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Combine, Don't Pick. Liam, in for Bear. | OutroSeries (humanitarians skin) |

## Beat-count note (redo)

Source is 7 beats (B00 composer-ask cold open + B01 anatomy + B02 pipeline +
B03 design tell + BVDT verdict + BHTF your-turn + BOUT outro). This redo keeps
the same 7-beat shape:

- **B00** replaces the source's `ClaudeComposerAsk` typed-ask cold open with
  `BrutalistHesitantWriter` per WRITER LAW, and absorbs the wrong-guess move
  directly into the correction (the source had no dedicated wrong-guess beat
  — it never staged a naive misconception, so this redo adds the one honest
  wrong guess a newcomer actually has: that combining multiple sources means
  *picking* the best one, not merging all of them).
- **B01 (anatomy) + B02 (pipeline)** compress into **NB01** — one beat, same
  two facts (a skill is a folder Claude reads before acting; the SKILL.md
  runs as ordered, linear steps).
- **B03 (design tell)** becomes **NB02** — same job description (combine,
  dedupe, attribute), with the Teardown's "what it gets right / what it
  bites" framing removed. Plain states the mechanism; it does not grade it.
- **BVDT (verdict)**'s determinism fact ("same input, same output, every
  run") moves into **NB03** alongside the confidence-weighting fact (the one
  part of B03's "interesting constraint" not yet covered), and BVDT's
  remaining verdict language ("Know the limit: only what the file says") is
  dropped as Teardown judgment rather than carried into Plain narration —
  the limit is implicit in "the skill only does what its SKILL.md specifies"
  (QUESTION.md), which the reel doesn't need to state as a caveat to be true.
- **BCRY** (new act label on the same verdict-slot beat, `BVDT`→`BCRY`)
  carries the CARRY-OUT LAW sentence, compressing BVDT's facts per the law's
  "compress the distinction, not the topic" test.
- **BHTF, BOUT** kept, re-skinned: BHTF's prompt rewritten to be genuinely
  paste-ready (the source's prompt had a grammar artifact, "I want to
  combines search results..."); BOUT swapped from `ClaudeTitleOutro` to
  `OutroSeries` (Humanitarians AI skin, per hai-simple's channel-skin
  override).

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap. This redo's body (NB01–NB03) uses
GRAPHIC/Manim instead of the source's REMOTION cards — a legal substitution
(GRAPHIC is one of hai-simple's two permitted beat kinds) chosen to reuse the
proven generic chip-row template already validated on the
`claude-plugins-official--claude-liam-agent-development` sibling in the same
family.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00; mechanism waits until NB01 |
| Wrong guess surfaced *and corrected* | B00's on-screen correction ("pick"→"combine", "source"→"sources") IS the wrong-guess beat, per WRITER LAW's designed overlap with hai-simple's spine |
| No design judgment | NB01-NB03 state what the skill does and how; none grade it as good/bad design (the source's "what it bites" framing is deliberately not carried over) |
| Carry-out | BCRY compresses the distinction (combine + weigh + attribute, never just pick) rather than restating the topic ("Claude can search many sources") |
| Host handoff | Not applicable — hai-simple has no puppet host; B00 hands off implicitly by moving straight into Liam's mechanism narration at NB01 |

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | B00 | multiple overlapping search results, one answer needed |
| 2 wrong guess | B00 | "pick the best source" — corrected on screen, not a separate beat (redo constraint: source had no dedicated wrong-guess beat to preserve as its own slot) |
| 3 mechanism | NB01, NB02, NB03 | anatomy/pipeline, dedupe+attribution, confidence weighting |
| 4 anchor | N/A | single running example (the knowledge-synthesis skill itself), present throughout — no separate planted/paid-off case exists to pair, consistent with the source's single-worked-example shape |
| 5 both directions | N/A | the reel makes one mechanism claim (combine+weigh+attribute), not an evidentiary claim with two failure directions to state |
| 6 carry-out | BCRY | see CARRY-OUT.md |

## Deliberately not claimed

- **No scoring formula.** The source states two weighing factors (freshness,
  authority); it does not give a formula, threshold, or weighting scheme.
  This reel doesn't invent one.
- **No claim that summarization is a separate mechanism.** The source lists
  "summarizes large result sets effectively" as part of the same skill; this
  reel treats it as the same combine/dedupe/attribute job, not a fourth,
  separately-explained behavior.
- **No accusation, no design verdict.** Plain register: the reel explains
  what the skill does and stops. It does not judge whether combine-then-
  weigh is the right design compared to alternatives.

## Handoff prompt (BHTF, read aloud then discussed)

> "I have three write-ups on the same topic that overlap and disagree in a
> few places. Read all three, combine what's true across them into one
> answer, remove anything repeated, and for each claim you keep, tell me
> exactly which write-up it came from and why you trusted it over the others
> where they disagreed."

Why it's worth running: it is the same three moves the reel just explained
(combine, dedupe, attribute-with-reasoning) applied to the viewer's own
material, immediately checkable against the reply.

---
**GATE P — signed:** ______________________  (human)
