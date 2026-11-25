# CHECKS-REPORT: Attention, One Head at a Time

Current as built (ai-explainer, converted 2026-11-24 from tldr). Words are counted from the narration; seconds are the measured audio. Body classes are carried over from the original proof-gate table; the new beats are SHOW.

| Beat | Role | Class | Words | Sec | On-screen artifact |
|---|---|---|---:|---:|---|
| B00 | ASK | SHOW | 32 | 9.3 | Claude composer: greeting, the ask types in, three result lines |
| B01 | BLUF | SHOW | 32 | 10.5 | hesitant writer: "picks the one word it needs" → "blends every word around it" |
| B10 | HOOK | SHOW | 59 | 16.3 | chase's dot lands, then moves when cats → kids; two ghost landings |
| B11 | INSTANCE | SHOW | 60 | 15.6 | blend dot sweeps on a segment, then glides inside the hull |
| B12 | INSTANCE | SHOW | 59 | 17.2 | request docks on each offer; products → score chips; asker changes |
| B13 | NAIVE | SHOW | 49 | 15.3 | four blend dots collapse onto one point |
| B14 | SHIFT (predict) | SHOW | 57 | 16.4 | score grid → ÷2 → softmax heat map; HOLD |
| B15 | TRANSFORM | SHOW | 40 | 11.9 | heat-map cells fly to value points as masses; dot lands on B10's ghost |
| B16 | ABSTRACTION | SHOW | 56 | 15.5 | rows → Q, K, V grids → MathTex Attention(Q,K,V) |
| B17 | TANGENT | SHOW | 120 | 35.3 | five-zone split stage, moving box spotlight, worked row |
| B18 | PAYOFF | SHOW | 59 | 17.9 | B10's dot with pull lines; swap replayed with re-weighting |
| B19 | BOUNDARY | SHOW | 59 | 18.9 | heat-map cells permute, outputs stay still; + position moves cats |
| BVDT | VERDICT | SHOW | 79 | 21.9 | verdict artifact, six lines |
| BHTF | YOUR TURN | SHOW | 117 | 34.1 | composer, prompt read in full, three checks |
| BOUT | OUTRO | SHOW | 10 | 4.6 | locked title outro |

**Total: 888 words · 260.7 s (4:20).**

## ai-explainer spine audit

| Slot | Required (ai-explainer SKILL.md) | This film | ✓ |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` cold open with result lines; Liam introduced in the first breath | "Hello, this is Liam, in for Bear. The ask: how d…"; three output lines | ✓ |
| B01 | `BrutalistHesitantWriter` BLUF, 20–35 words, `lead_silence_s: 0.8`, window ≥ 9 s, whole-phrase correction | 32 words; lead 0.8 s; 10.5 s | ✓ |
| Body | Manim lesson beats | B10, B11, B12, B13, B14, B15, B16, B17, B18, B19 | ✓ |
| BVDT | `ClaudeVerdictArtifact`, opens "Let's recap with Claude." | 6 lines | ✓ |
| BHTF | `ClaudeComposerAsk`, greeting "Your turn.", prompt read verbatim | unchanged | ✓ |
| BOUT | `ClaudeTitleOutro` (locked) | unchanged | ✓ |

The final passed GATE V, GATE T, the bookend check, the label and bottom-strip check, the master check and loudness. See BUILD-LOG.md for the values.

## History: original tldr checks report (2026-11-22, kept verbatim)

Beat ids in this history are the pre-conversion ones; the body ids did not change. Retired beats: B00, B01, B02, B03.

> # CHECKS-REPORT: written before the first slate (PROOF GATE)
>
> The 17 beats break down as 16 SHOW, 0 HOLD, 1 CARD and 0 PUNT:
> - **SHOW (16):** B00–B02, B10–B19, BVDT, BHTF and BOUT. BVDT and BOUT are mandated bookends.
> - **CARD (1):** B03 TERMS. Rows land one at a time, and it holds prerequisites only.
> - **HOLD and PUNT:** none.
>
> | Beat | Role | Class | Words | Est. s | On-screen artifact named in `shot.show` |
> |---|---|---|---:|---:|---|
> | B00 | TL;DR · WHAT | SHOW | 70 | 20.6 | wordmark, question writes on, three numbered lines on cues |
> | B01 | TL;DR · WHY | SHOW | 57 | 16.9 | page turn, stake writes on, two dash lines on cues |
> | B02 | THE QUESTION | SHOW | 35 | 11.4 | hesitant writer: "pick the word it needs" → "blend the words around it" |
> | B03 | TERMS | CARD | 49 | 14.6 | embedding / dot product / softmax rows land in reading order |
> | B10 | HOOK | SHOW | 59 | 17.5 | chase's dot lands, then moves when cats → kids; two ghost landings |
> | B11 | INSTANCE | SHOW | 60 | 17.7 | blend dot sweeps on a segment, then glides inside the hull |
> | B12 | INSTANCE | SHOW | 59 | 17.5 | request docks on each offer; products → score chips; asker changes |
> | B13 | NAIVE | SHOW | 49 | 14.6 | four blend dots collapse onto one point |
> | B14 | SHIFT (predict) | SHOW | 57 | 16.9 | score grid → ÷2 → softmax heat map; HOLD |
> | B15 | TRANSFORM | SHOW | 40 | 12.0 | heat-map cells fly to value points as masses; dot lands on B10's ghost |
> | B16 | ABSTRACTION | SHOW | 56 | 16.6 | rows → Q, K, V grids → MathTex Attention(Q,K,V) |
> | B17 | TANGENT | SHOW | 120 | 34.9 | five-zone split stage, moving box spotlight, worked row |
> | B18 | PAYOFF | SHOW | 59 | 17.5 | B10's dot with pull lines; swap replayed with re-weighting |
> | B19 | BOUNDARY | SHOW | 59 | 17.5 | heat-map cells permute, outputs stay still; + position moves cats |
> | BVDT | VERDICT | SHOW | 79 | 23.7 | verdict artifact, six lines |
> | BHTF | YOUR TURN | SHOW | 117 | 34.0 | composer, prompt read in full, three checks |
> | BOUT | OUTRO | SHOW | 10 | 3.5 | locked title outro |
>
> **Total: 1,035 words, about 307 s (5.1 min) at 3.5 w/s.** This includes the lead silences and about 0.6 s per beat for pauses. It is the **single-insight tier** (3–6 min).
>
> No two slide-like beats are adjacent. B03 is the only CARD, and it sits between the hesitant writer (B02) and a Manim beat (B10).
>
> ## tldr role audit (the spine, as SKILL.md defines it)
>
> | Slot | Required | This sheet | ✓ |
> |---|---|---|---|
> | B00 | `ClaudeTldrWhat`, 45–70 words, "This is Liam, in for Bear", world hello | Konnichiwa, Liam; 70 words; cues on the clauses | ✓ |
> | B01 | `ClaudeTldrWhy`, 45–65 words, opens "Why should you care?" | 57 words | ✓ |
> | B02 | `BrutalistHesitantWriter`, `lead_silence_s: 0.8`, 20–35 words, one phrase corrected, seed = slug | 35 words; trigger/replacement are whole phrases; read back, the text is the film's question | ✓ |
> | B03 | `ClaudeDefinitions`, 2–5 *prerequisite* terms, never the earned term | 3 terms. Query, key, value and attention are absent (earned in B16) | ✓ |
> | LEARN | positional ids Bk0–Bk9, `role`, `section`, `learn` on every beat | B10–B19, section 1, all 10 with `learn` blocks | ✓ (see note on 10 beats) |
> | BVDT | `ClaudeVerdictArtifact`, opens "Let's recap with Claude.", 4 or 6 lines | 6 lines | ✓ |
> | BHTF | `ClaudeComposerAsk`, greeting "Your turn.", topic has "YOUR TURN", prompt read verbatim plus rubric | `command` is a verbatim substring of the narration (asserted); three checks | ✓ |
> | BOUT | `ClaudeTitleOutro`, title + ".", `@NikBearBrown`, slug, no subline, narration "<title>. At Nik Bear Brown.", `kind: outro_voice`, `tail_silence_s: 1.0` | as specified (asserted) | ✓ |
> | metadata | `skill: tldr`, `style_preset: tldr`, channel, engine, voice, register, palette, `learn_canvas` | all set; plus `pronounce`, `sections`, `evidence` | ✓ |
>
> **Note on 10 LEARN beats.** SKILL.md reserves Bk0 for the SECTION card, which only appears when a film has two or more sections, and its density rule says more than nine *body* beats should become two sections. This film has one section, so B10 is free and holds the HOOK. The nine core roles run B10–B18, and the *optional* BOUNDARY sits at B19, as the brief asks. If the human reads the density rule strictly, fold B19 into B18's last two sentences plus BHTF. The rubric already carries the order-blindness check. **Flagged as an open question.**
>
> ## Gate-1 audit table (pedagogy §13)
>
> | Check | Ref | Pass? | Where |
> |---|---|---|---|
> | Key case named | §1.1 | ✓ | chase lands somewhere new when cats → kids (sections card, metadata) |
> | Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ | B10 uses only "attention head" (already said in B00) and "list of four numbers" |
> | ≥ 2 moving instances before the abstraction | §1.3 | ✓ | B11 (blend sweep) and B12 (dot product replayed, then a different asker) before B16 |
> | Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ | Query, key and value are named in B16 after "request / offer / point" have been used for five beats |
> | Natural wrong turn shown (NAIVE) | §3, §4 | ✓ | B13: equal weights collapse every word onto one point |
> | One representation named in one sentence (SHIFT) | §10 | ✓ | "The heat map: row *i* is word *i*'s blend weights over the value points." |
> | Exactly one TRANSFORM | §4 | ✓ | B15 |
> | Every landed equation followed by a TANGENT | §4 | ✓ | B16 → B17 (about 35 s, five zones, re-entry "Back to chase.") |
> | PAYOFF returns the HOOK's persistent object | §4 | ✓ | B18 reuses B10's sentence, dot and ghost landings |
> | Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ | Multi-head, W^O, residuals, masking and training are deferred (sections card) |
> | Mystery-framed opener; no utility framing | §2 | ✓ | "Chase's own numbers haven't changed, yet it lands somewhere else." |
> | Discovery voice; no "it can be shown that" | §3 | ✓ | "Start" / "Here's the obvious shortcut" / "So let the scores decide" / "Before anything moves" |
> | Every beat has a `learn` block; next_question chains | §9 | ✓ | Asserted in `make_sheet.py`. B19's is empty (last beat). |
> | One `predict: true` beat before the TRANSFORM | §12 | ✓ | B14 ("Before anything moves, where does chase land?") |
> | Boundary: not-taught plus transfer exercise → BHTF | §7 | ✓ | B19 (order-blindness) → BHTF (reverse the words, explain) |
> | Length derived plus tier reported; no pad, no rush | §5 | ✓ | about 5.1 min, single-insight |
>
> ## Detours (density rule §6)
>
> | Anticipated question | Handling |
> |---|---|
> | Why divide by two? | answered inline in the B17 tangent (values claim) |
> | Where do the grids come from? | answered in one clause each: B11 for values, B12 for queries and keys, B16 by name. Training is deferred ("toy numbers, not a trained model") |
> | What about many heads? | deferred. The BVDT/B11 caption says "real heads use 64". Multi-head is a possible future card. |
> | Residual / W^O / "new meaning" precision | deferred. FACTCHECK #4 |
> | Masking in decoders | cut silently |
>
> ## Teaching arc (SHOW-DON'T-TELL)
> Every LEARN beat changes a non-text shape before its final play:
> - moving dots: B10, B11, B13, B15, B18, B19
> - docking rows: B12
> - morphing grid: B14, B16
> - moving spotlight box with zone write-ons: B17. This is the one beat closest to a card, and it is justified by the EQUATIONS.md template.
>
> Comparisons are held for at least 2 s side by side: B10's two landings, B13's stack against B15's spread (ghosted), and B19's still dots against the permuted grid.
>
