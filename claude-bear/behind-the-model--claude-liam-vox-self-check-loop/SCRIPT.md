# Why Self-Checking Is Not Independent Verification — Narration Script (hai-simple redo)

*Skill: `hai-simple` (redo of `behind-the-model/claude-liam-vox-self-check-loop`, register
Teardown -> **Plain**). Voice: Liam, Kokoro `am_onyx`. Channel: @HumanitariansAI.*
*Source lock: question, facts, and body argument unchanged from the source sheet; only the
cold open (BrutalistHesitantWriter), the register (judgment stripped, facts kept), and the
outro (Humanitarians AI skin) change, per hai-simple's redo contract.*

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks: if Claude re-checks its own answer, isn't that already verified? Not quite — that's self-checked, not independently verified. Here's the difference, and why it matters." | BrutalistHesitantWriter — types "verified", hesitates, corrects to "self-checked" |
| S01 | stakes | This is Liam, in for Bear. An agent pulls together a competitive analysis from five industry reports. Two competitors named in the final output never appear in any source document. No error message shows up anywhere. | FormBCard — three-line build-up |
| S02 | wrong guess (the check that passed) | The agent actually read two of the five reports. For the rest, it drafted from training data, then ran an internal consistency check. The check found no contradictions — because every part came from the same mind. It reported the task complete. | FormBCard — reports read vs skipped, check passes |
| S03 | the question | So why did a self-check pass on work that had fabricated two data points? | CwcConceptCard — question framing |
| S04 | mechanism | Self-checking and independent verification are not the same thing. A system reviewing its own output works from the same context as the step that produced it — the same reading of the sources, the same assumptions, the same blind spots. A check like that can't catch an error the generation step already baked in. | ClaudeC3TwoColumnState — Generation vs Self-Check, both "same context" |
| S05 | mechanism, compressed | The same system can't independently verify itself. | WantQuote — mechanism card |
| S06 | **anchor** | Take Jae's agent. It misread fifteen percent as fifty percent in a source table. Then it ran a consistency check — comparing its summary to its own recalled version of that table. The recall also said fifty percent. The check passed. Jae opened the actual PDF: fifteen percent. | FormBCard — the 15%/50% mix-up, recall confirms itself |
| S07 | mechanism, the fix | Independent verification means comparing the output to the real source — not to the agent's memory of it. Open the cited document. Find the sentence the agent claims to quote. If the source says something different, this check catches it. The agent's own recall never could. | ClaudeC3TwoColumnState — Self-recall vs Actual source |
| S08 | practical takeaway | After any agent task, open at least two of the cited sources and check the claims made about them yourself. If the agent skipped a file, that file is exactly where a contradiction is most likely hiding. A self-check that passes is not proof the work is right. | StepStream — three-step checklist |
| **BCRY** | carry-out | The check can't catch what the generation already got wrong. Independent verification goes to the source — never to the agent's memory of it. | WantQuote — the sentence, alone |
| BHTF | your turn | Your turn. Here's the prompt — read it with me: "I want to add a verification step to my agent's pipeline, and I'm tempted to just have the same model review its own output. Explain exactly why that fails, what the overlap between generation and self-review looks like, and the smallest architecture change that makes verification genuinely independent." Try it on your own pipeline. | ClaudeComposerAsk |
| BOUT1 | outro (series) | This is part of the Claude Basics series from Humanitarians AI. | OutroSeries |
| BOUT2 | outro (CTA + title restate) | Why Self-Checking Is Not Independent Verification. …Liam, in for Bear. | OutroCTA |

## Redo audit — what changed, what didn't

| Kept from source (locked) | Changed for hai-simple |
|---|---|
| The question: why self-checking != independent verification | Cold open: `ClaudeComposerAsk` puppet-adjacent card -> `BrutalistHesitantWriter` (WRITER LAW) |
| Every fact: the 5-report fabrication case, the Jae 15%/50% case, the mechanism (shared context/blind spots), the checklist | Register: source narration was already fact-first with no verdict language: this pass only tightens word count and removes the source's Teardown framing markers (`color_semantics` verdict palette, `topic: AGENTIC AI` Teardown slug) |
| Body argument order: stakes -> the check that passed anyway -> why (mechanism) -> anchor case -> the fix (independent verification) -> practical checklist -> carry-out | Outro: `ClaudeTitleOutro` / `@NikBearBrown` -> `OutroSeries` + `OutroCTA`, Humanitarians AI skin, restates title, closes "...Liam, in for Bear." |
| Beat count: cold open + 9 content beats + your-turn + outro = 12 (source's B00 + B01-B09 + YOURTURN + OUTRO = 12; source's BVDT/BHTF/BOUT bookend stubs were empty-narration, `status: SLATE`, never built — dead scaffold, not part of the built 11-beat reel, not carried forward) | Voice: unchanged — Liam, Kokoro `am_onyx`, both source and redo |
| No AI-VIDEO, pantry, or human-drop beat existed in the source (its B00 was already `REMOTION ClaudeComposerAsk`, not a generated clip) — so NO-GENAI/NO-PANTRY LAW required no beat replacement beyond the mandatory WRITER LAW swap | Palette: body beats keep the Claude illustration palette (ai-explainer's ILLUSTRATE LAW, per hai-simple's "three things change, nothing else" — body visuals are not one of the three) |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes first | S01-S02; mechanism named explicitly starting S04 |
| Wrong guess surfaced and falsified by a case | S02 states the self-check passing as if it were fine; S06 (Jae) falsifies the assumption that a passing self-check means correct work |
| One inference flag | None needed — every claim here is the source's own worked mechanism, not an inference beyond it (`SOURCES.md`: N/A, this is a redo of an already-sourced sheet) |
| One anchor, planted, paid off | S06 plants Jae's case; S07 pays it off with the general fix (open the source, not the recall) |
| No design judgment | S04/S07 explain why a self-check can't do the job; neither beat rules on whether checking that way was a good decision — that's the removed Teardown material |
| Carry-out | BCRY — survives repetition, compresses the distinction (check vs. verify), not the topic |
| Host handoff | B00 narration performs the writer's own correction; S01 names Liam explicitly |

## Handoff prompt (BHTF, read aloud)

> "I want to add a verification step to my agent's pipeline, and I'm tempted to just have
> the same model review its own output. Explain exactly why that fails, what the overlap
> between generation and self-review looks like, and the smallest architecture change that
> makes verification genuinely independent."

Runnable today, on the reader's own agent pipeline.
