# FACTCHECK — vox-prompt-spec

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | Researcher sent vague prompt, got polished rewrite wrong for journal/audience | Illustrative | Ch03: "Can you improve this introduction? Two minutes later you have a rewritten paragraph. It is polished... It is also completely wrong for your audience, your journal, and the argument you are making." Near-verbatim | — |
| B04 | Naive expectation: capable model automatically infers context and applies right standard | ✓ | Ch03: "You might expect that if Claude lacks the context it needs, it would say so — or produce noticeably weaker output." (spirit) + general user expectation documented | — |
| B05 | Language model generates fluent text by completing the frame the prompt implies; vague frame -> generic standard applied | ✓ | Ch03: "Give it a vague frame, get a plausible-but-wrong answer. Give it a clear frame, get something you can inspect and use." | — |
| B05 | Model's generic standard: clean prose, shorter sentences, standard academic structure | ✓ | Ch03 opening scene — exactly this outcome described | — |
| B06 | A prompt is a specification of work; four things: what to do, what to use, what to avoid, what finished work looks like | ✓ | Ch03: "A good specification tells the contractor — human or AI — four things: 1. What to do 2. What to use 3. What to avoid 4. What the finished work should look like" — verbatim | — |
| B07 | Six components: task, context, source material, constraints, output format, evaluation criteria | ✓ | Ch03: "Every effective prompt answers six questions" + Table with exactly these six components — verbatim | — |
| B07 | Three most commonly missing: source material, constraints, evaluation criteria | ✓ | Ch03: "The most commonly omitted components are source material, constraints, and evaluation criteria." — verbatim | — |
| B08 | Priya vs Rohan illustrative example — specified prompt returns inspectable output | Illustrative | Constructed from Ch03's worked workflow: CHI venue, causal overclaims, diagnosis before rewriting, no new citations — all from the After example. Names invented. | None needed |
| B09 | Practice move: ask which component is missing, state what 'better' means, write evaluation criteria explicitly | ✓ | Ch03: "Asking Claude to 'make it better' without defining better. Every evaluation criterion is implicit in your prompt. Make it explicit." + exercise descriptions | — |
| B10 | Inspectability check: can you tell from output whether Claude answered YOUR question or a generic version | ✓ | Ch03: "The output of the second prompt is inspectable. You can check whether the issues it flags match your concerns." | — |
| B11 | Bad prompt returns fluent, confident output that passes review without triggering a check | ✓ | Ch03: "end users tend to accept outputs that look plausible rather than testing them against ground truth" (Zamfirescu-Pereira et al. 2023) | — |
| B14 | Model failure vs specification failure — model did what you asked; you asked for the wrong thing | ✓ | Ch03: "Not Claude's failure. Yours. You did not write a specification; you made a wish." — verbatim (spirit) | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| specification | B06 | B01-B05 established vague prompts produce wrong outputs; viewer wants a frame |
| evaluation criteria | B07 | B06 established "specification" as the frame; viewer wants its components |

## Exclusion Confirmation
- NO deep XML tag syntax tutorial: PASS (XML mentioned nowhere in narration or visuals)
- NO prompting-framework literature comparison: PASS (no framework names, no academic taxonomy)
- NO extended chain-of-thought research: PASS (absent)

## Illustrative Examples
- B01: Researcher + vague prompt -> wrong rewrite — ILLUSTRATIVE (from card spec)
- B08: Priya (vague) vs Rohan (specified) — ILLUSTRATIVE (constructed from Ch03 worked workflow; Rohan's spec items are all from the real chapter example)
